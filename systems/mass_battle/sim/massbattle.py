"""Strategic-layer adapter: faction-scale Military Conquest -> the canon mass-battle engine.

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
history of the 2026-08-24 port and the d.1 change, kept as written; the code is in git at the parent of
the deleting commit. `_GarrisonStub`, `_round_half_up` and the `_STA_MORALE_*` bounds were left standing
for `20-iv`, which decides what the season path's morale source is.]

[UPDATED 2026-10-01, plan position `20-iv`]: `resolve_field` now takes its morale-start from season state
-- each side's mean stance toward its own faction, the carrier `_eff_march` writes a lost field's
"decrease in morale" onto (`_morale_start`'s docstring) -- and its terrain from the target's territory
and garrison (`terrain_row_for_territory`, with A.9's Walls DR applied in `_run_and_grade`).
`_round_half_up` and the morale bounds (renamed `_MORALE_FLOOR`/`_MORALE_CEIL`, no longer Stability's)
have that reader. `_GarrisonStub` had none once `resolve_mass_battle` went, and is deleted (ID-13); it is
in git at `79d690ce`.

[UPDATED 2026-09-26, d.1 / ED-MB-0068]: morale is no longer part of the flat, carried-over default
this header describes — it is now derived from `faction.Sta` (`_morale_start_from_stability`).
This is the ONE field this docstring's "carried over UNCHANGED" claim no longer covers; every other
field it names is still exactly as described. d.1's own behaviour delta is isolated the same way
the 2026-08-24 swap was: `_GarrisonStub` (the uncontrolled-territory arm) holds its pre-d.1 flat
morale-start fixed, so the movement traces to real factions' Stability alone — see its docstring.
"""
from __future__ import annotations

import math

from systems.mass_battle.sim import rngsource
from systems.mass_battle.sim.config import CELL_CAP
from systems.mass_battle.sim.hierarchy.units import Subunit, Unit
from systems.mass_battle.sim.orchestration import run_battle
from systems.mass_battle.sim.terrain import (FOREST_BROKEN, WALLS, WALLS_DEFENDER_DR,
                                             terrain_row_for_territory)

#: Size-ratio -> degree thresholds. CARRIED OVER VERBATIM from the pre-port adapter so that the
#: golden movement this commit causes is attributable to the engine swap and nothing else. These are
#: NOT the canonical degree ladder (`engine/autoload/dice_engine.degree_from_net`, margin-based);
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


def _morale_start(stance):
    """A side's starting morale from its members' mean stance toward their own faction -- plan
    position `20-iv`, d.1 (`ED-MB-0067`: *faction state sets the morale baseline*) carried onto the
    season path after `29b` deleted the `Faction.Sta` it read.

    THE SOURCE, AND WHY IT IS THIS ONE. The season has no faction stat vector, by architecture
    (`04`'s NEVER list: *"it never makes a faction stat vector a field of its own"*), so faction state
    is what members hold toward the faction. Jordan's M4 ruling on a lost field (`ED-IN-0279` clause
    (b): *"casualties only, decrease in morale, and a grudge token"*) is already built as a stance row
    on each loser, `(own faction, -1.0, field_morale_weight)` (`loop/effects_combat.py::_eff_march`):
    that row IS the season's morale, and until this function it had a writer and no reader on the
    battle path (CLAUDE.md §0.1 pt 1). The provider sums it through `decision.stance_toward`, the one
    reader of a stance row, and hands each side's weight-mean here.

    THE MAPPING, AND THE ONE THING IT ASSUMES. One stance unit toward one's own faction is one point
    of morale, added to `_MORALE_START_BASE` and clamped to canon's ladder. That identity is the
    assumption; it adds no knob, because the magnitude is already `field_morale_weight`'s (`H-148`,
    swept 0/1/3): while `_eff_march` is the only writer of a stance row on a faction id (measured at
    `build_realm(0)`: its 32 seeded rows all name a person), a scale factor here would only multiply
    that weight. At weight 0 a lost field writes a zero row and this returns the base -- the control.

    NOT TAKEN: the build-time loyalty rows (`data/cast.py::stance_from_loyalty`). They name the
    faction's LEADER, a person, not the faction, so reading them would merge two referents the
    morale writer keeps apart; whether ideology should also stiffen an army is a separate question
    this function does not answer."""
    return max(_MORALE_FLOOR, min(_MORALE_CEIL, _round_half_up(_MORALE_START_BASE + float(stance))))


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


def _run_and_grade(unit_a, unit_b, terrain, rng):
    """`run_battle` plus the survivor-ratio classification -- extracted from `resolve_mass_battle`
    (deleted at `29b`; `resolve_field` is now its only caller).

    ⚠ CAVEATS THAT LIVED IN THE DELETED FUNCTION'S DOCSTRING AND STILL BIND THIS PATH.
    DETERMINISM: `rng` is scoped over the battle by `rngsource.using`; the canon engine drew from the
    global `random` module at seven sites, so without that holder a seeded run is unpinnable.
    TERRAIN: two rows are applied, each in part. FOREST_BROKEN's speed half is INERT -- `run_battle`
    never reads `.speed` (only `orchestration.pursuit_damage` and `run_multi_unit_battle` do, and
    neither is reachable from here). WALLS (plan position `20-iv`, the garrisoned march target) adds
    `terrain.WALLS_DEFENDER_DR` to the DEFENDER's (`unit_b`'s) `dr`, read live at every melee and rout
    hit (`eff_dr` falls through to the Unit; `h_per_size`, the one field derived from `dr` at
    construction, has no reader), so mutating it here is the same in-place shape the speed half uses.
    WALLS' other clauses, "no flanking; Slow cannot advance", are NOT applied: this engine's one-subunit
    season units have no flank or advance order to forbid. UPHILL, NARROW_PASS and RIVER_CROSSING are
    identified by `terrain_row_for_territory` and not applied: UPHILL's number is a dice count
    (+1D/-1D), which this engine reaches only through `config.SIGMA_PER_D`, a calibrated-debt
    conversion -- the step WALLS' DR did not need, and terrain work `20-iv` (a garrison position) did
    not take. DEGREE: the bands below are the bespoke survivor-ratio thresholds carried over from the
    pre-port adapter, not `dice_engine.degree_from_net`.

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
        unit_b.dr += WALLS_DEFENDER_DR

    with rngsource.using(rng):
        # [canonical: mass_battle_v30.md §A.7 — 18-tick battle (3 phases x 6), the canon engine's own default]
        run_battle(unit_a, unit_b, max_turns=18)

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


def resolve_field(w, side_a, side_b, *, territory=None, fort_level=0.0, stance_a=0.0, stance_b=0.0,
                  rng=None):
    """THE SEASON-FACING ENTRY POINT — `04 §C.5.1`'s roster contract, reconciled with this module's
    OWN requirement for a `Unit` to hand `run_battle`.

    §C.5.1: *"units = PersonId[] at weight — one type. There is NO unit class, at any scale."*
    `side_a`/`side_b` are `PersonId[]`, weighed by `w.persons[pid].weight` (`state/carriers.py`:
    "A COHORT IS A PERSON AT weight > 1"); no `Unit`/`Faction`-shaped object crosses this boundary.
    Internally, `run_battle` still needs a `Unit` -- that requirement does not go away because the
    caller's contract changed -- and `_faction_to_unit` (deleted at `29b`) was not reused here: it read
    `faction.Mil` into `Unit.power`, a QUALITY stat, and headcount is a SIZE fact, not a quality
    one (see `_weighted_unit`, and `_SEASON_FORCE_POWER`'s note on the mistake this corrects).
    "No unit class, at any scale" is honoured at the SEAM this function's signature draws; it does
    not reach inside an adapter whose whole job has always been "become a `Unit` for the engine
    that only speaks one".

    ⚠ **AN EMPTY `side_b` gets `_MIN_TROOPS`' crash-avoidance floor, not an invented auto-win.**
    What an empty defending force MEANS is eligibility policy for whichever verb calls this (open,
    per `ED-IN-0279` clause (a)'s live design fork on the season-side spatial join -- NOT yet
    Jordan's ruling on an auto-win specifically, which this function does not attribute to that row)
    -- the same discipline `seam/wrappers/*` already follows: derive what you can, decide nothing
    you were not asked to. See `_MIN_TROOPS`' own docstring for the SCALE gap this does not solve
    either -- a real corpus side's weight sum is nowhere near this engine's calibrated battle size,
    and this function does not invent the missing conversion.

    THE SEASON INPUTS (plan position `20-iv`), each a plain value the provider read off the world --
    this module imports nothing from `engine/` and reads no carrier but `Person.weight`:
      `territory`, `fort_level` -- the geography territory id of the place fought over and its
          fortification (`world_q.fortification_of`, `[0.0, 1.0]`), turned into ONE A.9 row by
          `terrain_row_for_territory` and applied in `_run_and_grade`. `side_b` is the DEFENDER, so
          walls stiffen it. `None` territory is the lookup's own no-modifier fallback, whatever the
          fortification, because that function asks "is this a known territory" first.
      `stance_a`, `stance_b` -- each side's weight-mean stance toward its own faction, which
          `_morale_start` turns into a morale-start. `0.0` (the default) is the base: the pre-`20-iv`
          flat 5.
    The old `terrain=` keyword, which the one caller always passed as `None`, is gone: the row is
    derived here from the two facts that decide it, so no caller can hand in a row that disagrees.

    Returns exactly what `_run_and_grade` returns."""
    weight_a = sum(w.persons[pid].weight for pid in side_a if pid in w.persons)
    weight_b = sum(w.persons[pid].weight for pid in side_b if pid in w.persons)
    unit_a = _weighted_unit("side_a", weight_a, _morale_start(stance_a))
    unit_b = _weighted_unit("side_b", weight_b, _morale_start(stance_b))
    return _run_and_grade(unit_a, unit_b, terrain_row_for_territory(territory, fort_level), rng)
