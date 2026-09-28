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
from systems.mass_battle.sim.terrain import FOREST_BROKEN

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


class _GarrisonStub:
    """Minimal faction-shaped stub for an uncontrolled territory's garrison.

    [GAP: defenderless-territory garrison strength lacks canonical spec; Mil=1.5 roughly matches the
     pre-mass-battle v17 Ob 2 vs Ob 4 single-roll spread. Carried over unchanged.]
    """

    #: [d.1, ED-MB-0068] No strategic Faction backs an uncontrolled territory, so there is no
    #: Stability to derive a morale-start from. Held at the PRE-d.1 flat default so an
    #: uncontrolled garrison's starting morale is UNCHANGED by this commit — any golden movement
    #: this commit causes is then attributable to real factions' Stability alone, not to a
    #: simultaneous change in the garrison stub.
    Sta = 5.0  # [canonical: inherited default — pre-d.1 flat morale-start, unchanged; see GAP above]

    def __init__(self, name, Mil):
        self.name = name
        self.Mil = Mil
        self.Sta = 5.0  # [canonical: inherited default — pre-d.1 flat morale-start, unchanged; see GAP above]


#: [d.1, ED-MB-0068] `Faction.Sta` floors at 0 / ceilings at 7 (registry-declared — the
#: descriptors module's per-stat bounds function, keyed 'Sta', confirmed by
#: test_faction_stat_bounds.py; deliberately not spelled as a literal call above, since
#: `massbattle.py` never actually calls that function itself — only `adjust` may, per
#: tests/valoria/test_faction_write_sweep.py's single-caller check — and writing the name
#: immediately followed by an open paren here would read as a second call site to that
#: check's own text search). MORALE IS A
#: DIFFERENT, NARROWER LADDER, NOT the same range: `mass_battle_v30.md:230-231` states canon's own
#: Morale range directly ("Morale (1-7)"), so `_STA_MORALE_FLOOR` is 1, not 0 — a Sta=0 faction
#: still has to land somewhere inside Morale's 1-7, not fall outside it.
_STA_MORALE_FLOOR = 1  # [JUSTIFIED: mass_battle_v30.md:230-231 states canon's Morale range directly ("Morale (1-7)") — this is the direct citation, not an inference from the separate in-battle erosion floor at :254]
_STA_MORALE_CEIL = 7  # [JUSTIFIED: mirrors Faction.Sta's own registry ceiling (test_faction_stat_bounds.py) and matches Morale's canon ceiling (mass_battle_v30.md:230-231, "Morale (1-7)")]
# Floor=1 (not 0) is THIS IMPLEMENTATION'S OWN choice, Jordan-vetoable — see the derivation's own
# docstring below for the full basis, including why it is ALSO consistent with :254's separate
# in-battle erosion floor and with rout firing at morale<=0.


def _round_half_up(x):
    """Round-half-AWAY-FROM-ZERO, not Python's builtin `round()` (round-half-to-even / banker's
    rounding). `Faction.Sta` floors at 0 (registry-declared), so this only ever sees non-negative
    input — 'away from zero' and 'half up' coincide here, no negative branch needed.

    WHY THIS EXISTS, NOT bare `round()`: Sta moves in increments of `1 / MULTS['Sta']` = 0.1
    (`Faction.adjust`, engine/autoload/game_state.py), and a plain Stability-Failure penalty is
    exactly -5 granular, i.e. -0.5 Sta (`faction_action.py:490`, Govern Failure) — so Sta lands on
    an exact .5 boundary in ordinary play, not only in theory. Python's `round()` at those
    boundaries is asymmetric in a way that has nothing to do with game state: `round(4.5) == 4`
    but `round(3.5) == 4` too, so a faction moving Sta 5.0 -> 4.5 (one Govern failure) loses a
    point of morale_start (5 -> 4) while a faction moving Sta 4.0 -> 3.5 (the same failure, same
    magnitude) does NOT (4 -> 4 either way) — an undisclosed, purely arithmetic asymmetry with no
    mechanical basis. `_round_half_up` treats every .5 boundary the same way instead.
    """
    return math.floor(x + 0.5)


def _morale_start_from_stability(faction):
    """d.1 — a faction's starting morale is derived from its strategic Stability (ED-MB-0067).

    THIS SUPERSEDES THE UNTAGGED MORALE-STARTING-FORMULA SENTENCE AT `mass_battle_v30.md:230-231`
    ("Starting = general's Command + unit quality modifier (cap 7)") — NOT PP-711. PP-711 is a
    DIFFERENT rule: the battle-boundary morale RESET (`orchestration.py:reset_morale_between_battles`,
    citing "§PP-711 (Morale resets between battles)" in its own docstring). PP-711 is unaffected by
    this change — reinforced, even, since that function now resets a unit's morale to a real
    Stability-derived value instead of a flat hardcoded stub, WHEN IT RUNS. The starting-formula
    sentence itself carries no PP number of its own; `mass_battle_v30.md:660` (the RESET section)
    merely references it for context, which is how the wrong "supersedes PP-711" framing first arose
    — corrected in `registers/editorial_ledger_mb.jsonl`'s ED-MB-0067, third correction row; do not
    re-cite PP-711 here. No code ever implemented the starting-formula sentence — `_faction_to_unit`
    hardcoded morale=5/morale_start=5 with an honest [canonical: inherited default — see GAP above]
    comment — so this is a NEW derivation, not an edit to prior logic.

    [CORRECTION 2026-09-26, ED-MB-0069] The above previously claimed `reset_morale_between_battles`
    is "called at every campaign battle boundary" — a second citation error in this same docstring,
    found by an adversarial pass on unrelated work and confirmed by grep: no call site exists
    anywhere in `engine/` or this file; only test code (`test_persubunit_stress.py`,
    `tests/valoria/test_mass_battle_signals.py`) invokes it directly. `engine/mc_v18.py`'s campaign
    loop never references it, `morale`, or this file's own `_faction_to_unit` by that claim.

    [RESOLVED 2026-09-27, ED-MB-0070] The prior row left open whether PP-711 is enforced some other
    way or simply unenforced. Half right, half wrong — corrected by an adversarial review (Opus,
    2026-09-27) that opened `orchestration.py` directly rather than trusting this docstring's own
    prior claim, the same discipline that caught the PP-711/starting-formula conflation above.
    `resolve_mass_battle` (below) calls `_faction_to_unit` fresh for BOTH sides on every invocation,
    and `_try_conquest` (`systems/factions/sim/faction_action.py:393-400`) calls `resolve_mass_battle`
    fresh for every Military Conquest — no `Unit` this function returns is cached or persisted on
    `faction`/`world` between calls (grep-confirmed: no `lru_cache`/memoization wraps either
    function). Every campaign battle therefore starts from a brand-new `Unit` whose MORALE is derived
    from the faction's Stability AT THAT MOMENT — for morale alone, a stronger property than "reset
    between battles", since there is no stale morale ever available to reset.

    WRONG PART, NOW CORRECTED: `reset_morale_between_battles` does NOT "stay live in `run_battle`'s
    own internal multi-turn loop" — it has NO production call site anywhere in this package.
    `run_multi_turn_battle` calls `reset_positions`, `run_battle` and `between_turn_recovery` between
    turns, never this function; its own docstring says so directly ("NOT within a single battle:
    between_turn_recovery handles the within-battle turn boundary"). Every caller is a test writing to
    a hand-built `Unit` directly (`tests/valoria/test_mass_battle_signals.py`,
    `test_persubunit_stress.py`, `tests/valoria/test_charger_latch.py`,
    `tests/valoria/test_morale_write_sweep.py`, `tests/valoria/test_octagon_damage.py`) — it is dead
    in production, full stop, not merely unreached at this one seam.

    SCOPE, STATED PRECISELY: fresh construction closes the gap for PP-711 (morale) ONLY. The same
    function's docstring also carries PP-712 ("Discipline persists between battles") — fresh
    construction does NOT satisfy that: `_faction_to_unit` hardcodes `discipline=5,
    discipline_start=5` every call, so Discipline does not carry over either, which is the SAME
    pre-existing `[GAP: faction -> unit construction lacks canonical spec]` this file already
    declares above, not a new one. This paragraph is about PP-711 alone.

    Would become load-bearing at the strategic seam the moment a `Unit` persists across more than
    one battle here. `engine/season/seam/contest.py` now HAS a provider for `"a field"`
    (`ED-IN-0279`, M3, `engine/season/seam/wrappers/mass_battle.py`) — but that provider calls
    `resolve_field`, not `resolve_mass_battle`/`_faction_to_unit` (season Persons carry no `.Sta`
    to derive from; `_weighted_unit` builds morale flat, not via this function), and constructs a
    fresh `Unit` on every call exactly as `_try_conquest`'s strategic path already does. So this
    paragraph's premise — no `Unit` persists across battles — still holds on BOTH paths; still not
    a currently-open item.

    [ASSUMPTION: rounded to the nearest int (half-up, see `_round_half_up`) and floored at 1 rather
    than 0 — basis: `mass_battle_v30.md:230-231` states canon's own Morale range directly ("Morale
    (1-7)"), which is NARROWER than `Faction.Sta`'s registry-declared 0-7 (test_faction_stat_bounds.py)
    — Sta and Morale are NOT the same ladder, so Sta=0 must still clamp into Morale's 1-7 range.
    Floor=1 is separately consistent with `:254`'s in-battle erosion floor ("Morale floor = 1"
    while the general is present) and with rout firing at morale<=0 (confirmed by grep against
    core/state.py:189 `atom.eff_morale <= 0` and hierarchy/units.py:2454-2455's aggregate-morale
    rout derivation), so a Stability-0 faction must not field a unit that starts pre-routed.
    Rounding an otherwise-continuous stat to an integer STARTING value is also consistent with
    ED-1024 (`registers/editorial_ledger.jsonl:197` — Morale is continuous IN PLAY, but its own
    text states "B.2 starting values are integers"). The concept synthesis's own Stability -> s0
    mapping (proposals/2026-09-25-squad-engagement-synthesis.md) is itself an open placeholder at
    the faction scale; this floor-and-round choice is THIS IMPLEMENTATION'S OWN, not something
    already ruled to this precision. Jordan-vetoable.]
    """
    # [known risk, low priority: silently gives 5.0 — the garrison default — to ANY object lacking
    #  .Sta, not only a real _GarrisonStub. Accepted rather than fixed: Sta is an established field
    #  name on every real Faction (engine/autoload/game_state.py) and no other caller is known to
    #  construct a Faction-shaped object without it.]
    sta = getattr(faction, 'Sta', _GarrisonStub.Sta)
    return max(_STA_MORALE_FLOOR, min(_STA_MORALE_CEIL, _round_half_up(sta)))


#: [canonical: mass_battle_integration_v30.md §4.10 sub-step 3 — the strategic entry point. ⚠ THE
#:  VALUES BELOW ARE NOT CANON AND THIS COMMENT DOES NOT CLAIM THEY ARE. They are the pre-port
#:  adapter's minimum-viable defaults, carried over FIELD-FOR-FIELD so the engine swap is a
#:  single-variable experiment, and the [GAP] on both this module's construction paths is the
#:  honest status: no canonical spec exists for army -> Unit construction of ANY kind. The
#:  fabrication gate is right to ask; the answer is "inherited, with a recorded gap", not
#:  "derived".] SHARED BY `_faction_to_unit` AND `_weighted_unit` (§8: one owner for the MVP
#: shape, so the two construction paths cannot silently drift apart on a field neither has a
#: reason to vary). `concentration` is deliberately NOT here -- it is continuous-mode-only
#: (`_weighted_unit` sets it; `_faction_to_unit`'s tier-sized Subunit does not), a real
#: difference between the two modes rather than something that drifted.
_MVP_SUBUNIT_SHAPE = dict(shape='Line', troop_type='infantry', tier=2,
                          starting_position=(8, 12), advance_dir=1,
                          stance='balanced', unit_type='melee')

#: SAME SHARING, FOR THE UNIT SIDE. `power`/`morale`/`morale_start` are NOT here: `power`'s
#: SOURCE is the very thing the two construction paths differ on, and morale is derived
#: (`_faction_to_unit`) vs. flat (`_weighted_unit`) for the same reason (no season-side Stability
#: to derive from).
_MVP_UNIT_COMMAND = dict(command=4, discipline=5, discipline_start=5)


def _faction_to_unit(faction):
    """Build a canon-engine Unit from a strategic-layer faction.

    Field-for-field identical to the pre-port construction, WITH ONE EXCEPTION (d.1, ED-MB-0068):
    morale/morale_start are now derived from `faction.Sta` rather than hardcoded — see
    `_morale_start_from_stability`. Every other field is untouched, so the swap this docstring
    otherwise describes (a single-variable experiment on the RESOLUTION model) still holds for
    everything but morale.
    """
    power = max(1, int(round(faction.Mil)))
    sub = Subunit(**_MVP_SUBUNIT_SHAPE)
    m0 = _morale_start_from_stability(faction)
    return Unit(
        name=f'{faction.name}_force',
        faction=faction.name,
        power=power,
        **_MVP_UNIT_COMMAND,
        morale=m0,                       # [d.1, ED-MB-0068: derived from faction.Sta — see above]
        morale_start=m0,                 # [d.1, ED-MB-0068: derived from faction.Sta — see above]
        subunits=[sub],
    )


#: A season `Person` carries no troop-density signal at all -- `power` is a Unit-level QUALITY
#: stat (baseline for a subunit with no per-subunit override; `eff_power`'s own fallback, cited
#: there as "[canonical: sim_mb_06_v9_historical_spec.md -- P4 tier baseline default]"), not
#: something army headcount should feed. Re-used here rather than derived from weight -- headcount
#: is a SIZE fact (below), and conflating it with quality was this function's own first-draft
#: mistake, caught on review (a Crown-sized force would have out-CLASSED a Guild-sized one on
#: quality alone, backwards of what more bodies means).
_SEASON_FORCE_POWER = 4

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


def _weighted_unit(name, weight):
    """One `Unit`, one `Subunit`, sized by `troops=` (the Jordan-directed continuous-scale field,
    `hierarchy/units.py`: "when `troops` is set the footprint is generated from (troops,
    concentration) ... `tier` becomes vestigial") rather than by `tier`'s fixed lookup table.

    `_MVP_SUBUNIT_SHAPE`'s `tier=2` is still passed because `Subunit.__post_init__` requires SOME
    tier even in continuous mode; it is inert here (troops overrides it). `concentration` is set
    to `config.CELL_CAP` -- pack as densely as the engine allows before it would open a second
    cell, the smallest-footprint reading available and not a claim about real troop density.
    Every other Subunit/Unit field is the SAME non-canonical inherited default `_faction_to_unit`
    uses, shared via `_MVP_SUBUNIT_SHAPE`/`_MVP_UNIT_COMMAND` -- this function changes WHICH
    NUMBER SIZES THE FORCE, not what else is carried over unchanged."""
    sub = Subunit(**_MVP_SUBUNIT_SHAPE, troops=max(float(weight), _MIN_TROOPS),
                  concentration=float(CELL_CAP))
    return Unit(name=name, faction=name, power=_SEASON_FORCE_POWER, **_MVP_UNIT_COMMAND,
                morale=5, morale_start=5, subunits=[sub])


def _run_and_grade(unit_a, unit_b, terrain, rng):
    """`run_battle` plus the survivor-ratio classification -- extracted from `resolve_mass_battle`
    so `resolve_field` shares it rather than re-deriving it (§8: the rule lives once). Identical to
    what `resolve_mass_battle` always did with its own two Units; see that function's docstring for
    the terrain/RNG/degree-band caveats, which are unchanged and apply here too.

    Takes `rng` directly rather than a `world`-shaped object -- this is the only thing either
    caller ever reads off `world`, so narrowing the parameter to what is actually used means
    `resolve_field` (which has no `World`, only a bare `rng`) needs no adapter object to satisfy
    an attribute it does not otherwise have."""
    if terrain == FOREST_BROKEN:
        if unit_a.speed == 'Fast':
            unit_a.speed = 'Standard'
        if unit_b.speed == 'Fast':
            unit_b.speed = 'Standard'

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


def resolve_field(w, side_a, side_b, *, terrain=None, rng=None):
    """THE SEASON-FACING ENTRY POINT — `04 §C.5.1`'s roster contract, reconciled with this module's
    OWN requirement for a `Unit` to hand `run_battle`.

    §C.5.1: *"units = PersonId[] at weight — one type. There is NO unit class, at any scale."*
    `side_a`/`side_b` are `PersonId[]`, weighed by `w.persons[pid].weight` (`state/carriers.py`:
    "A COHORT IS A PERSON AT weight > 1"); no `Unit`/`Faction`-shaped object crosses this boundary.
    Internally, `run_battle` still needs a `Unit` -- that requirement does not go away because the
    caller's contract changed -- but `_faction_to_unit` is NOT reused here: that function reads
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

    Returns exactly what `_run_and_grade` returns."""
    weight_a = sum(w.persons[pid].weight for pid in side_a if pid in w.persons)
    weight_b = sum(w.persons[pid].weight for pid in side_b if pid in w.persons)
    unit_a = _weighted_unit("side_a", weight_a)
    unit_b = _weighted_unit("side_b", weight_b)
    return _run_and_grade(unit_a, unit_b, terrain, rng)


def resolve_mass_battle(faction_a, faction_b, terrain, world):
    """Strategic entry point for Military Conquest resolution.

    Per `mass_battle_integration_v30.md §4.10 sub-step 3` and `canon/02_canon_constraints.md` §B
    GD-1: produces faction stat / territorial-control deltas only — no mass_battle_outcome ->
    game_victory trigger.

    Returns {'attacker_wins', 'degree', 'attacker_size_pct', 'defender_size_pct'}.

    ⚠ DETERMINISM. `world.rng` is scoped over the battle via `rngsource.using`. The canon engine drew
    from the GLOBAL `random` module at seven sites; the engine it replaced threaded an explicit `rng`
    end to end, after a 2026-05-20 fix whose own note records that pre-fix "run_batch results varied
    between runs at the same seed". Porting without restoring that property would not have moved the
    seeded goldens — it would have made them UNPINNABLE. See `rngsource.py` for why the property is
    restored with a holder rather than a threaded parameter.

    terrain: [A7, ED-MB-0067 Part A / ED-MB-0074] One of `terrain.py`'s six A.9 row constants (its
    caller, `faction_action._try_conquest`, derives it from the engagement province via
    `terrain.terrain_row_for_territory` — no separate coordinate plumbing needed, the province tid
    IS the geography query key). Was accepted and silently discarded since this adapter's creation
    (a `[GAP]` comment at the one call site said so plainly).

    [CORRECTED, adversarial review 2026-09-27] The FOREST_BROKEN branch below writes `unit.speed`, but
    THIS FUNCTION CALLS `run_battle`, and `run_battle` never reads `.speed` at all — only
    `orchestration.pursuit_damage` and `orchestration.run_multi_unit_battle` do (neither reachable from
    here). The write is not "mechanically applied and merely campaign-unreachable pending a Fast-speed
    side"; it is inert on ITS OWN TERMS, independent of `_faction_to_unit` never producing a Fast unit —
    even a hand-built Fast-speed pair run through THIS function would see no effect. Kept rather than
    removed because it is harmless (dead-writes a field this call path never reads) and is the correct
    first half of A.9's "Cavalry -> Standard" rule for whichever future seam DOES reach `.speed`'s real
    readers — but it is not evidence of anything working today, and the ledger/handoff text saying so
    was wrong. NOT yet applied, disclosed rather than silently ignored: UPHILL (a damage/defense
    magnitude — ED-MB-0018's own precedent, "the octagon is NOT a pool penalty, it's a MULTIPLIER",
    says how but not how much — A.9's own table does give one, "+3 DR"-adjacent numbers for the other
    rows, but translating them is a separate pass since it moves goldens), WALLS (a DR bonus, same
    reason), NARROW_PASS ("1 engagement per side" — vacuous at THIS seam anyway, since `run_battle`
    below is already a single 1v1 pair; would only bind once army-scale multi-Unit plans exist, per
    Part A's own 'Sequenced' table; ALSO not currently reachable from any real, unfortified territory —
    see `terrain_row_for_territory`'s own docstring for the geometric reason, not a fortification one),
    and RIVER_CROSSING (not yet reachable from `terrain_row_for_territory` at all — see its own module
    docstring). OPEN_FLAT is A.9's own "no modifiers" row and needs no branch.

    [CORRECTED, adversarial review 2026-09-27] UPHILL/WALLS above are not missing a number from canon —
    A.9's table already gives one each ("+1D Def / -1D Off", "+3 DR"). What is deferred is TRANSLATING
    that dice-pool-era number into this engine's sigma/degree model, the way ED-MB-0018 translated the
    octagon's facing bonus from a pool modifier into a damage multiplier — a real design step, not a
    blank to fill in, and one that moves goldens once done. That translation work is deferred, not the
    number itself.
    """
    # [A7, ED-MB-0067 Part A / ED-MB-0074] A.9: "Forest / broken: Cavalry -> Standard; flanking
    # impossible." Only the speed half is attempted here (flanking-impossible would need the
    # envelopment pipeline, out of scope for this pass — see this function's own docstring).
    # [CORRECTED, adversarial review 2026-09-27] This write is inert, full stop — not merely
    # campaign-unreachable. `run_battle` below never reads `.speed` (only `pursuit_damage` and
    # `run_multi_unit_battle` do, neither called from this function), so even a hand-built Fast-speed
    # unit run through THIS path would see no effect. Doubly inert today because `_faction_to_unit`
    # never sets `speed` either (its own [GAP] comment covers that half) — but fixing only that half
    # would not make this branch do anything. See this function's own docstring for the full disclosure.
    #
    # ⚠ THE BODY BELOW MOVED INTO `_run_and_grade`, EXTRACTED SO `resolve_field` (M3) SHARES IT
    # RATHER THAN RE-DERIVING IT (§8). Byte-identical: same two calls, same order, same operands.
    unit_a = _faction_to_unit(faction_a)
    if faction_b is None:
        # Defenderless-territory garrison strength has no canonical spec; Mil=1.5 approximates the
        # pre-mass-battle v17 Ob 2 vs Ob 4 single-roll spread. Carried over from the pre-port adapter.
        # [canonical: inherited default — recorded [GAP], not canon; see the module header]
        unit_b = _faction_to_unit(_GarrisonStub(name='Uncontrolled', Mil=1.5))
    else:
        unit_b = _faction_to_unit(faction_b)
    return _run_and_grade(unit_a, unit_b, terrain, getattr(world, 'rng', None))
