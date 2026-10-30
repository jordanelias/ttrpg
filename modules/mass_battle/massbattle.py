"""Season-facing adapter: `resolve_field` -> the canon mass-battle engine (it was the strategic-layer faction adapter).

WHAT THIS FILE IS NOW, AND WHAT IT WAS. Until 2026-08-24 this module WAS the mass-battle engine —
1,905 lines of resolution, geometry, morale and rout code that the campaign ran. Jordan ruled that
day to port `tests/sim/mass_battle/` (11,342 lines, called "the canon mass-battle engine" by
`tests/valoria/test_degree_ladder_single_owner.py:25-27`, imported by 43 of 156 `tests/valoria`
files, and the target of every recent ED-MB batch) over the top of it. The engine now lives beside
this file as `orchestration.py`, `hierarchy/`, `core/`, `geometry.py`, `percell.py` and the rest.

WHAT SURVIVED THE OVERWRITE, AND WHY IT HAD TO. The canon engine's entry point is TACTICAL —
`run_battle(unit_a, unit_b, max_turns=18)` takes constructed Units. The campaign's entry point is
STRATEGIC: `faction_action._try_conquest` has two factions and needs a degree back. The adapter
between them — `resolve_mass_battle`, `_faction_to_unit`, the garrison stub, and the size-ratio ->
degree map — existed ONLY in the old engine, and `systems/factions/sim/faction_action.py:393`
imports it by this exact path (this citation previously read `:462`, a stale line number pointing at
an unrelated Muster-cost line — corrected 2026-09-27, ED-MB-0070, caught by adversarial review).
Overwriting the file wholesale would have broken the campaign at
import. So the engine was replaced and the adapter was kept, which is what "port the engine" has to
mean if the campaign is to keep running.

⚠ THIS IS THE "MB CANON ADAPTER" A SEPARATE AUDIT RECORDED AS NEVER BUILT. It is built here in the
narrow sense (the campaign reaches the canon engine) and NOT in the wide one: the faction -> Unit
construction below is still the old engine's minimum-viable default (one Line subunit, tier 2,
command 4, discipline 5, power = round(faction.Mil)) for every field EXCEPT morale — see the
2026-09-26 update below. The canon engine can express far more than any of this — troop types,
equipment, formations, multi-subunit hierarchies, orders of battle. Every one of those is a design
question about what a faction's army IS at the strategic scale, and none of them is answered by
porting an engine. The remaining defaults are carried over UNCHANGED and marked, so the behaviour
delta measured for the 2026-08-24 engine-swap commit was attributable to the ENGINE swap alone and
not to a simultaneous change in how armies are built.

[GAP: faction -> unit construction lacks canonical spec — carried over from the pre-port adapter.]

[DELETED 2026-10-01, plan position `29b`: `resolve_mass_battle`, `_faction_to_unit` and
`_morale_start_from_stability` went with `game_state.Faction` and `systems/factions/`, which held their
only caller (`faction_action._try_conquest`). What is left is the season-facing path: `resolve_field`,
`_weighted_unit`, `_run_and_grade`. The paragraphs above and below that name the deleted three are the
history of the 2026-08-24 port and the d.1 change, kept as written; the code is in git at `5c5d8ec6`.
`_GarrisonStub` and the `_STA_MORALE_*` names are gone, and `_round_half_up` now serves the morale
source built at `20-iv` (the next block).]

[UPDATED 2026-10-01, plan position `20-iv`]: `resolve_field` now takes its morale-start from season state
-- each side's mean stance toward its own faction, the carrier `_eff_march` writes a lost field's
"decrease in morale" onto (`_morale_start`'s docstring) -- and its terrain from the target's territory
and garrison (`terrain_row_for_territory`, with A.9's Walls DR applied in `_run_and_grade`).
`_round_half_up` and the morale bounds (renamed `_MORALE_FLOOR`/`_MORALE_CEIL`, no longer Stability's)
have that reader. `_GarrisonStub` had none once `resolve_mass_battle` went, and is deleted (ID-13); it is
in git at `5c5d8ec6`.

[SUPERSEDED 2026-10-01 by the `20-iv` block above: nothing reads `faction.Sta` any more, and
`_morale_start_from_stability` and `_GarrisonStub` are deleted. The block below is history.]

[UPDATED 2026-09-26, d.1 / ED-MB-0068]: morale is no longer part of the flat, carried-over default
this header describes — it is now derived from `faction.Sta` (`_morale_start_from_stability`).
This is the ONE field this docstring's "carried over UNCHANGED" claim no longer covers; every other
field it names is still exactly as described. d.1's own behaviour delta is isolated the same way
the 2026-08-24 swap was: `_GarrisonStub` (the uncontrolled-territory arm) holds its pre-d.1 flat
morale-start fixed, so the movement traces to real factions' Stability alone — see its docstring.
"""
from __future__ import annotations

import math

from modules.mass_battle import rngsource
from modules.mass_battle.config import CELL_CAP
from modules.mass_battle.hierarchy.units import Subunit, Unit
from modules.mass_battle.orchestration import run_battle
from modules.mass_battle.orderofbattle import OrderOfBattle, Subformation, build_unit as _build_oob_unit
from modules.mass_battle.troop_types.recruitment import under_arms_cap
from modules.mass_battle.terrain import (FOREST_BROKEN, RIVER_CROSSING, RIVER_CROSSING_OFF_D,
                                             SPEED_TIERS, UPHILL, UPHILL_ATTACKER_OFF_D,
                                             UPHILL_DEFENDER_DEF_D, WALLS, WALLS_DEFENDER_DR,
                                             river_crossed, terrain_row_for_territory)

#: Size-ratio -> degree thresholds. CARRIED OVER VERBATIM from the pre-port adapter so that the
#: golden movement this commit causes is attributable to the engine swap and nothing else. These are
#: NOT the canonical degree ladder (`engine/dice_engine/dice_engine.degree_from_net`, margin-based);
#: they are a bespoke post-hoc classification of a finished battle's survivor ratios, and
#: reconciling the two is open MB-lane work, not a port concern.
# [canonical: carried over unchanged from the pre-port adapter, systems/mass_battle/sim/massbattle.py
#  @ FORK ref e4070d4^ — see this module's header. NOT independently derived: they are the same three
#  survivor-ratio thresholds the campaign has used since Phase 7, preserved verbatim so the engine
#  swap is a single-variable experiment. Their GROUNDING is open MB-lane work — no canon states them.]
OVERWHELMING_ATTACKER_MIN = 0.75   # [canonical: inherited from the pre-port adapter — see note above]
OVERWHELMING_DEFENDER_MAX = 0.25   # [canonical: inherited from the pre-port adapter — see note above]
PARTIAL_ATTACKER_MIN = 0.50        # [canonical: inherited from the pre-port adapter — see note above]


#: [d.1, ED-MB-0068; re-sourced at plan position `20-iv`] Canon's Morale ladder, the range a
#: morale-start must land in: `mass_battle_v30.md:230-231` states it directly ("Morale (1-7)").
#: These were `_STA_MORALE_FLOOR`/`_CEIL` while `Faction.Sta` (0..7) was the source; the source is
#: gone (`29b`) and the ladder is not, so the names lose the `STA`. The floor is 1, not 0: rout
#: fires at morale <= 0, so a side cannot START already routed -- the same reading the d.1
#: derivation took, and still this implementation's own, Jordan-vetoable.
_MORALE_FLOOR = 1  # [JUSTIFIED: mass_battle_v30.md:230-231 states canon's Morale range directly ("Morale (1-7)") — this is the direct citation, not an inference from the separate in-battle erosion floor at :254]
_MORALE_CEIL = 7  # [JUSTIFIED: Morale's canon ceiling, mass_battle_v30.md:230-231, "Morale (1-7)"]

#: The morale-start of a side whose members' stance toward their own faction is zero -- no field
#: lost, nothing written. It is the flat value every strategic and season unit started at before
#: d.1 (`_faction_to_unit`'s and then `_weighted_unit`'s literal `morale=5`), so a world where
#: nobody has lost a field fights exactly as it did before `20-iv`: that is the control arm, and it
#: is the shipped world (`build_realm` seeds no stance row on a faction id; `_morale_start`).
_MORALE_START_BASE = 5  # [canonical: inherited default — the pre-port adapter's flat morale-start, carried by _faction_to_unit until d.1 and by _weighted_unit since; see GAP above]


def _round_half_up(x):
    """Round half UP (toward +inf), not Python's builtin `round()` (round-half-to-even / banker's
    rounding). Its input is `_MORALE_START_BASE` plus a side's mean stance, which can be negative;
    every value below 0.5 then clamps to `_MORALE_FLOOR` in `_morale_start`, so how a NEGATIVE half
    rounds never reaches a result, and half-up and half-away-from-zero agree on every input that does.

    WHY THIS EXISTS, NOT bare `round()`: a side's mean stance lands on an exact .5 in ordinary play --
    half the side lost a field at `field_morale_weight` 1 and half did not -- and `round()` at those
    boundaries is asymmetric in a way that has nothing to do with game state: `round(4.5) == 4` but
    `round(3.5) == 4` too, so one loss across half a side would cost a point of morale at one level
    and nothing at the next. `_round_half_up` treats every .5 boundary the same way. (The reason was
    first written for `Faction.Sta`'s 0.1 steps, d.1; the arithmetic is the same.)"""
    return math.floor(x + 0.5)


def _morale_start(stance, loyalty=0.0, gain=0):
    """A side's starting morale from its members' mean stance toward their own faction -- plan
    position `20-iv`, d.1 (`ED-MB-0067`: *faction state sets the morale baseline*) carried onto the
    season path after `29b` deleted the `Faction.Sta` it read.

    THE SOURCE, AND WHY IT IS THIS ONE. The season has no faction stat vector, by architecture
    (`04_CODE_ARCHITECTURE.md`, the faction view's list: *"NEVER: a member of `World` · a field of its own · ..."*), so faction state
    is what members hold toward the faction. Jordan's M4 ruling on a lost field (`ED-IN-0279` clause
    (b): *"casualties only, decrease in morale, and a grudge token"*) is already built as a stance row
    on each loser, `(own faction, -1.0, field_morale_weight)` (`loop/effects_combat.py::_eff_march`):
    that row IS the season's morale, and until this function it had a writer and no reader on the
    battle path (CLAUDE.md §0.1 pt 1). The provider sums it through `queries.person_q.stance_toward`, the one
    reader of a stance row, and hands each side's weight-mean here.

    THE MAPPING, AND THE ONE THING IT ASSUMES. One stance unit toward one's own faction is one point
    of morale, added to `_MORALE_START_BASE` and clamped to canon's ladder. That identity is the
    assumption; it adds no knob, because the magnitude is already `field_morale_weight`'s (`H-148`,
    swept 0/1/3): while `_eff_march` is the only writer of a stance row on a faction id (measured at
    `build_realm(0)`: its 32 seeded rows all name a person), a scale factor here would only multiply
    that weight. At weight 0 a lost field writes a zero row and this returns the base -- the control.
    ONE EXCEPTION (`H-151`): in a SAME-FACTION march winner and loser are one faction, so each loser also
    carries the grudge row `(faction, -1.0, field_grudge_weight)` and `stance_toward` sums both: the next
    morale-start is `5 - (morale_w + grudge_w)` (3 at the defaults 1/1), and at weight 0 the grudge still
    moves it. The control above holds for a cross-faction field only.

    THE BUILD-TIME LOYALTY ROW, BEHIND A GAIN (MB-03, `ED-MB-0078`'s superseding row, option (b)).
    `loyalty` is the side's weight-mean stance toward its faction creed's UTTERER -- the row
    `data/cast.py::stance_from_loyalty` seeds at build, `-5..+5` -- and it is added at `gain`, the
    season's `field_morale_loyalty_gain` fixture. It is a SECOND TERM, not merged into `stance`: the
    loyalty row names the faction's LEADER, a person, and the morale row names the faction, so the host
    reads and hands on the two referents apart and only their sum on the ladder is shared. AT `gain` 0
    THE TERM IS ZERO and the result is the shipped option (a), battle history only, exactly (the
    control, swept 0 / 0.4 / 1; `data/fixtures.py` says how each arm is derived). At 0.4 a side with
    loyalty >= 3.75 already reaches the ceiling, and the 1:1 arm saturates most creed-holding
    factions at `build_realm(0)` (the row's own finding, with the per-side starts pinned in
    `tests/valoria/test_mass_battle_d1_morale_baseline.py`), which is why the magnitude is the gain's
    and is swept rather than chosen here."""
    return max(_MORALE_FLOOR, min(_MORALE_CEIL, _round_half_up(
        _MORALE_START_BASE + float(stance) + float(gain) * float(loyalty))))


#: [canonical: mass_battle_integration_v30.md §4.10 sub-step 3 — the strategic entry point. ⚠ THE
#:  VALUES BELOW ARE NOT CANON AND THIS COMMENT DOES NOT CLAIM THEY ARE. They are the pre-port
#:  adapter's minimum-viable defaults, carried over FIELD-FOR-FIELD so the engine swap is a
#:  single-variable experiment, and the [GAP] on both this module's construction paths is the
#:  honest status: no canonical spec exists for army -> Unit construction of ANY kind. The
#:  fabrication gate is right to ask; the answer is "inherited, with a recorded gap", not
#:  "derived".] SHARED, until `29b` deleted `_faction_to_unit`, BY THAT FUNCTION AND `_weighted_unit` (§8:
#: one owner for the MVP shape); `_weighted_unit` is now the only user. `concentration` is deliberately
#: NOT here -- it is continuous-mode-only (`_weighted_unit` sets it; the deleted tier-sized Subunit
#: did not).
_MVP_SUBUNIT_SHAPE = dict(
    shape='Line',
    troop_type='infantry',
    tier=2,                          # [canonical: inherited default — 200 troops, see GAP above]
    starting_position=(8, 12),      # [canonical: inherited default — see GAP above]
    advance_dir=1,
    stance='balanced',
    unit_type='melee',
)

#: SAME SHARING, FOR THE UNIT SIDE. `power`/`morale`/`morale_start` are NOT here: they are set by
#: `_weighted_unit` itself (morale from `_morale_start`, since plan position `20-iv`).
_MVP_UNIT_COMMAND = dict(
    command=4,                       # [canonical: inherited default — see GAP above]
    discipline=5,                    # [canonical: inherited default — see GAP above]
    discipline_start=5,              # [canonical: inherited default — see GAP above]
)


#: A season `Person` carries no troop-density signal at all -- `power` is a Unit-level QUALITY
#: stat (baseline for a subunit with no per-subunit override; `eff_power`'s own fallback, cited
#: there as "[canonical: sim_mb_06_v9_historical_spec.md -- P4 tier baseline default]"), not
#: something army headcount should feed. Re-used here rather than derived from weight -- headcount
#: is a SIZE fact (below), and conflating it with quality was this function's own first-draft
#: mistake, caught on review (a Crown-sized force would have out-CLASSED a Guild-sized one on
#: quality alone, backwards of what more bodies means).
_SEASON_FORCE_POWER = 4  # [canonical: sim_mb_06_v9_historical_spec.md — P4 tier baseline default, eff_power's own fallback]

#: [known risk, disclosed rather than fixed: `resolve_field` has no ratified person-weight ->
#: troop-count conversion, and this module is not the place to invent one.] `Subunit.troops` is
#: fed the RAW weight sum with no scale factor -- honest as a NUMBER (weight is the one quantity a
#: season Person carries that is a headcount), but this engine's own calibration
#: (`config.py: SUBUNIT_ROUT_FLOOR`, "a subunit routs below SUBUNIT_ROUT_FLOOR total") targets
#: battles of hundreds of troops, and a real corpus faction's weight sum (single/double digits,
#: measured against `harness.populated.build_realm(0)`) routs on contact regardless of who wins.
#: A season-Person-weight -> troop-count conversion is open work this function does not invent one
#: of; until it lands, `resolve_field`'s outcomes are honest about their INPUT and not yet
#: calibrated to the engine's own battle scale.
_MIN_TROOPS = 1.0  # floor only -- `Unit.total_troops() == 0` divides by zero deep in
                   # `orchestration.resolve_engagements`; this is the smallest value that avoids
                   # that crash, not a claim about what a minimal army is.


def _weighted_unit(name, weight, morale_start=_MORALE_START_BASE):
    """One `Unit`, one `Subunit`, sized by `troops=` (the Jordan-directed continuous-scale field,
    `hierarchy/units.py`: "when `troops` is set the footprint is generated from (troops,
    concentration) ... `tier` becomes vestigial") rather than by `tier`'s fixed lookup table.

    `_MVP_SUBUNIT_SHAPE`'s `tier=2` is still passed because `Subunit.__post_init__` requires SOME
    tier even in continuous mode; it is inert here (troops overrides it). `concentration` is set
    to `config.CELL_CAP` -- pack as densely as the engine allows before it would open a second
    cell, the smallest-footprint reading available and not a claim about real troop density.
    `morale_start` is `_morale_start`'s value for this side (the base when omitted); `morale` starts
    equal to it, and the Subunit sets neither, so its `eff_morale` falls through to the Unit's.
    Every other Subunit/Unit field is the non-canonical inherited default of the pre-port adapter
    (`_faction_to_unit`, deleted at `29b`), carried via `_MVP_SUBUNIT_SHAPE`/`_MVP_UNIT_COMMAND`."""
    sub = Subunit(**_MVP_SUBUNIT_SHAPE, troops=max(float(weight), _MIN_TROOPS),
                  concentration=float(CELL_CAP))
    return Unit(name=name, faction=name, power=_SEASON_FORCE_POWER, **_MVP_UNIT_COMMAND,
                morale=morale_start, morale_start=morale_start,
                subunits=[sub])


#: The troop type a side with no order of battle fights as, once the OTHER side has one. It is the nearest canonical
#: stand-in for `_MVP_SUBUNIT_SHAPE`'s bare 'infantry' (which has no stat preset): one line of light infantry, sized by
#: the side's headcount. NOT `levy`, though a levy is what a side that raised nothing could call up: measured at 300 a
#: side over twelve seeds, a levy line closes to contact in 0 of them and every other infantry or mounted type in 11-12
#: (`Unit` discipline 1), so a levy fallback would make a field against a headcount side a standing-still draw. [ASSUMPTION; medium; Jordan to correct -- ED-IN-0306 phase 5 gives every faction a real
#: preset order of battle, after which this fallback is reached only by a hand-built record.]
_HEADCOUNT_LINE_TYPE = 'light_infantry'


def _oob_unit(oob, weight, side, morale_start):
    """The Unit for a side when the field carries orders of battle (ED-IN-0306). `oob` None -> a single
    `_HEADCOUNT_LINE_TYPE` subformation, so both sides deploy by the same rule. Its size is the most the side's
    `weight` could put under arms, `under_arms_cap(weight)` (`troop_types/recruitment.py`), NOT the bare weight:
    an order of battle counts troops (a weight-12 cohort raises up to 120) and a season weight counts households,
    so a side left at its weight would meet a hundred troops with twelve. [ASSUMPTION; medium; Jordan to correct;
    revert: `max(float(weight), _MIN_TROOPS)`, and a headcount side is a tenth the army it could muster.]
    Built with `faction` 'A'/'B', the engine's deployment convention, rather than `_weighted_unit`'s side names:
    the sides must start on opposite rows, which the single-line path's shared (8, 12) never needed."""
    if oob is None:
        oob = OrderOfBattle((Subformation('line', _HEADCOUNT_LINE_TYPE,
                                          max(float(under_arms_cap(weight)), _MIN_TROOPS)),))
    return _build_oob_unit(oob, f'side_{side.lower()}', side, morale_start=morale_start)


def _run_and_grade(unit_a, unit_b, terrain, rng, walls_dr=None, by_troops=False):
    """`run_battle` plus the survivor-ratio classification -- extracted from `resolve_mass_battle`
    (deleted at `29b`; `resolve_field` is now its only caller).

    `walls_dr` (plan position `20-v`, `H-150`): the defender DR the WALLS row adds. `None` -- the
    default -- is A.9's own number, `terrain.WALLS_DEFENDER_DR`, read here and never copied; an int
    overrides it for the one call (the season's `field_walls_dr` fixture, swept 3 / 0 / 1).

    ⚠ CAVEATS THAT LIVED IN THE DELETED FUNCTION'S DOCSTRING AND STILL BIND THIS PATH.
    DETERMINISM: `rng` is scoped over the battle by `rngsource.using`; the canon engine drew from the
    global `random` module at seven sites, so without that holder a seeded run is unpinnable.
    TERRAIN: UPHILL, RIVER_CROSSING and WALLS are applied (UPHILL's two A.9 clauses fully; NARROW_PASS
    is identified and applies nothing, see below); the attacker is `unit_a`, the defender `unit_b`.
    FOREST_BROKEN's speed half is INERT -- `run_battle` never reads `.speed` (only
    `orchestration.pursuit_damage` and `run_multi_unit_battle` do, and neither is reachable from here).
    WALLS (plan position `20-iv`, the garrisoned march target) adds `terrain.WALLS_DEFENDER_DR` to the
    DEFENDER's `dr`, read live at every melee and rout hit (`eff_dr` falls through to the Unit;
    `h_per_size`, the one field derived from `dr` at construction, has no reader), so mutating it here is
    the same in-place shape the speed half uses. WALLS' other clauses, "no flanking; Slow cannot
    advance", are NOT applied: this engine's one-subunit season units have no flank or advance order to
    forbid. UPHILL and RIVER_CROSSING (MB-05) are dice rows: their A.9 dice go onto
    `Unit.terrain_off_d`/`terrain_def_d` (`terrain.py`'s constants, which say how a die reaches the
    engine -- `config.SIGMA_PER_D`, calibrated debt); RIVER_CROSSING also steps the crosser one
    `SPEED_TIERS` slower (inert, as forest's is). NARROW_PASS is identified and NOT applied, and it is
    not a deferral: "1 engagement per side; Fibonacci impossible" restricts how many subunits engage and
    the Concentration tactic, and a season unit is ONE subunit with no tactic -- both clauses already
    hold on every field this function fights, so applying them would change nothing. DEGREE: the bands
    below are the bespoke survivor-ratio thresholds carried over from the pre-port adapter, not
    `dice_engine.degree_from_net`.

    Takes `rng` directly rather than a `world`-shaped object -- this is the only thing either
    caller ever reads off `world`, so narrowing the parameter to what is actually used means
    `resolve_field` (which has no `World`, only a bare `rng`) needs no adapter object to satisfy
    an attribute it does not otherwise have."""
    if terrain == FOREST_BROKEN:
        if unit_a.speed == 'Fast':
            unit_a.speed = 'Standard'
        if unit_b.speed == 'Fast':
            unit_b.speed = 'Standard'
    elif terrain == WALLS:
        unit_b.dr += WALLS_DEFENDER_DR if walls_dr is None else walls_dr
    elif terrain == UPHILL:
        unit_a.terrain_off_d += UPHILL_ATTACKER_OFF_D
        unit_b.terrain_def_d += UPHILL_DEFENDER_DEF_D
    elif terrain == RIVER_CROSSING:
        unit_a.terrain_off_d += RIVER_CROSSING_OFF_D
        unit_a.speed = SPEED_TIERS[max(0, SPEED_TIERS.index(unit_a.speed) - 1)]

    with rngsource.using(rng):
        # [canonical: mass_battle_v30.md §A.7 — 18-tick battle (3 phases x 6), the canon engine's own default]
        run_battle(unit_a, unit_b, max_turns=18)

    if by_troops:
        # ED-IN-0306 phase 3: the survivor share counted in TROOPS (`hp` over `hp_max`), the quantity `march` scales a
        # losing side's bodies by. `effective_size / size_max` is not that for an army that is not a whole number
        # of `TROOPS_PER_SIZE` blocks: `size_max` floors, `effective_size` does not, so 120 troops read as 1 block
        # against 1.2 and a side that lost troops could score above 1.0 (found by `test_army_battle.py`: a lost
        # field raised the loser's body to 1092 of 1000). The headcount path keeps its form, so its goldens do not move.
        a_size_pct = unit_a.hp / max(1.0, unit_a.hp_max)
        b_size_pct = unit_b.hp / max(1.0, unit_b.hp_max)
    else:
        a_size_pct = unit_a.effective_size / max(1, unit_a.size_max)
        b_size_pct = unit_b.effective_size / max(1, unit_b.size_max)
    attacker_wins = (not unit_a.routed) and (unit_b.routed or a_size_pct > b_size_pct)

    if attacker_wins and a_size_pct >= OVERWHELMING_ATTACKER_MIN and b_size_pct <= OVERWHELMING_DEFENDER_MAX:
        degree = 'Overwhelming'
    elif attacker_wins:
        degree = 'Success'
    elif not unit_a.routed and a_size_pct >= PARTIAL_ATTACKER_MIN:
        degree = 'Partial'
    else:
        degree = 'Failure'

    return {
        'attacker_wins': attacker_wins,
        'degree': degree,
        'attacker_size_pct': a_size_pct,
        'defender_size_pct': b_size_pct,
    }


def resolve_field(inp, rng=None, *, troops_a=None, troops_b=None):
    """THE SEASON-FACING ENTRY POINT, AND THE `mass_battle` MODULE'S ENTRY (A-25, plan position `31c`) --
    `04 §C.5.1`'s roster contract, reconciled with this module's OWN requirement for a `Unit` to hand
    `run_battle`.

    THE ENTRY. The composition row `mass_battle.resolve_field` (`references/module_contracts.yaml`,
    `entry: verb_call`, `verb: march`) targets this function; the registrar resolves it by string into
    `manifest.MODULE_ENTRIES` at driver construction, and the host adapter
    `engine/season/seam/wrappers/mass_battle.py::resolve` -- the `@provider("contest", "mass_battle")` the
    prize row `a field` names -- calls it with the typed input record its builder `field_input` made
    (`engine/season/queries/inputs.py::MassBattleInput`) and the seeded `rng`. It never reads or writes
    `World` (until `31c` it took `w` and summed `w.persons[pid].weight` itself), holds no token, and keeps
    no state between calls: the draws are scoped to this call by `rngsource.using` (`_run_and_grade`), the
    geography arrives on the record (`inp.geography`, the host's read), and no trace block is opened.

    §C.5.1: *"units = PersonId[] at weight — one type. There is NO unit class, at any scale."* The
    record's `weights` are each side's `Person.weight`s (`state/carriers.py`: "A COHORT IS A PERSON AT
    weight > 1"); no `Unit`/`Faction`-shaped object crosses this boundary. Internally, `run_battle` still
    needs a `Unit` -- that requirement does not go away because the caller's contract changed -- and
    `_faction_to_unit` (deleted at `29b`) was not reused here: it read `faction.Mil` into `Unit.power`, a
    QUALITY stat, and headcount is a SIZE fact, not a quality one (see `_weighted_unit`, and
    `_SEASON_FORCE_POWER`'s note on the mistake this corrects). "No unit class, at any scale" is honoured
    at the SEAM this function's signature draws; it does not reach inside an adapter whose whole job has
    always been "become a `Unit` for the engine that only speaks one".

    ⚠ **AN EMPTY DEFENDING SIDE gets `_MIN_TROOPS`' crash-avoidance floor, not an invented auto-win.**
    What an empty defending force MEANS is eligibility policy for whichever verb calls this (open,
    per `ED-IN-0279` clause (a)'s live design fork on the season-side spatial join -- NOT yet
    Jordan's ruling on an auto-win specifically, which this function does not attribute to that row)
    -- the same discipline `seam/wrappers/*` already follows: derive what you can, decide nothing
    you were not asked to. See `_MIN_TROOPS`' own docstring for the SCALE gap this does not solve
    either -- a real corpus side's weight sum is nowhere near this engine's calibrated battle size,
    and this function does not invent the missing conversion.

    THE RECORD'S FIELDS (plan position `20-iv` and after), each a plain value the host read off the world:
      `weights` -- `(attacker, defender)`, each side's member weights, SUMMED here into its Unit's troops.
      `territory`, `fort_level` -- the geography territory id of the place fought over and its
          fortification (`world_q.fortification_of`, `[0.0, 1.0]`), turned into ONE A.9 row by
          `terrain_row_for_territory` and applied in `_run_and_grade`. The second side is the DEFENDER,
          so walls stiffen it. `None` territory is the lookup's own no-modifier fallback, whatever the
          fortification, because that function asks "is this a known territory" first.
      `stances` -- `(attacker, defender)`: each side's weight-mean stance toward its own faction, which
          `_morale_start` turns into a morale-start. `0.0` is the base: the pre-`20-iv` flat 5.
      `walls_dr` -- plan position `20-v` (`H-150`): the defender DR a WALLS field adds, handed to
          `_run_and_grade` unchanged. `None` is A.9's number, `terrain.WALLS_DEFENDER_DR`; an int
          overrides it. Inert on a field `terrain_row_for_territory` does not call WALLS.
      `origin` -- MB-05r: the territory the attacking side marched from, or `None`. Whether the march
          crossed a river is `terrain.river_crossed(origin, territory)` (the geography's water, which
          the host never reads), handed to `terrain_row_for_territory` as its `river_crossing`, the
          one place RIVER_CROSSING can come from. `None` crosses nothing: the field as before MB-05r.
      `loyalties`, `loyalty_gain` -- MB-03: `(attacker, defender)` build-time loyalty rows and the
          gain `_morale_start` adds them at; gain `0` is the control, battle history only.
    The row is derived here from the facts that decide it (`territory`, `fort_level`, `origin`), so
    no caller can hand in a row that disagrees.
      `geography` -- the parsed geography file both lookups read, the HOST's (read once per process by
          `engine/season/data/geography.py`). This module opens no file and never writes into it.

    v9 IN-52 (the levy-to-field feed): `troops_a`/`troops_b` are each side's FIELDED troops when the host
    provisioned the field (`settlements.provision`, read by the adapter), `None` -- the default -- meaning
    the side's Σ weight, the field before the feed. They size the Unit in the weight's place and nothing
    else; `_MIN_TROOPS`' floor still applies, so an unprovisioned side (`0`) fields the crash floor.

    Returns exactly what `_run_and_grade` returns."""
    weight_a, weight_b = (sum(side) for side in inp.weights)
    if troops_a is not None:
        weight_a = troops_a
    if troops_b is not None:
        weight_b = troops_b
    stance_a, stance_b = inp.stances
    loyalty_a, loyalty_b = inp.loyalties
    morale_a = _morale_start(stance_a, loyalty_a, inp.loyalty_gain)
    morale_b = _morale_start(stance_b, loyalty_b, inp.loyalty_gain)
    oob_a, oob_b = inp.orders_of_battle or (None, None)
    armies = oob_a is not None or oob_b is not None
    if not armies:
        unit_a = _weighted_unit("side_a", weight_a, morale_a)
        unit_b = _weighted_unit("side_b", weight_b, morale_b)
    else:
        # ED-IN-0306: a side with an order of battle fights as that order says. Its headcounts are authoritative,
        # so `troops_a`/`troops_b` (the provisioning feed) are not applied to it -- recruiting is what bounds an
        # order of battle's size (phase 2), and scaling it here would silently overrule that.
        unit_a = _oob_unit(oob_a, weight_a, 'A', morale_a)
        unit_b = _oob_unit(oob_b, weight_b, 'B', morale_b)
    # No territory: `river_crossed` answers False and the lookup OPEN_FLAT. WALLS outranks a crossing
    # (`terrain_row_for_territory`), so a fortified field does not derive one.
    crossing = inp.fort_level <= 0 and river_crossed(inp.origin, inp.territory, geography=inp.geography)
    return _run_and_grade(unit_a, unit_b,
                          terrain_row_for_territory(inp.territory, inp.fort_level, crossing,
                                                    geography=inp.geography),
                          rng, walls_dr=inp.walls_dr,
                          **({'by_troops': True} if armies else {}))
