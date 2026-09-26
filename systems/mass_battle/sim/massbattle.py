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
degree map — existed ONLY in the old engine, and `systems/factions/sim/faction_action.py:462`
imports it by this exact path. Overwriting the file wholesale would have broken the campaign at
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
from systems.mass_battle.sim.hierarchy.units import Subunit, Unit
from systems.mass_battle.sim.orchestration import run_battle

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


#: [d.1, ED-MB-0068] `Faction.Sta` floors at 0 / ceilings at 7 (registry-declared,
#: `descriptors.faction_bounds('Sta')`, confirmed by test_faction_stat_bounds.py). MORALE IS A
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
    loop never references it, `morale`, or this file's own `_faction_to_unit` by that claim. Whether
    PP-711 is enforced in the live campaign some OTHER way (each battle rebuilding a fresh Unit from
    Faction stats, so there is no stale morale to reset) or is simply unenforced there is not yet
    determined — flagged, not resolved, in `registers/handoffs/HANDOFF_MB.md`.

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


def _faction_to_unit(faction):
    """Build a canon-engine Unit from a strategic-layer faction.

    Field-for-field identical to the pre-port construction, WITH ONE EXCEPTION (d.1, ED-MB-0068):
    morale/morale_start are now derived from `faction.Sta` rather than hardcoded — see
    `_morale_start_from_stability`. Every other field is untouched, so the swap this docstring
    otherwise describes (a single-variable experiment on the RESOLUTION model) still holds for
    everything but morale.
    """
    # [canonical: mass_battle_integration_v30.md §4.10 sub-step 3 — the strategic entry point. ⚠ THE
    #  VALUES BELOW ARE NOT CANON AND THIS COMMENT DOES NOT CLAIM THEY ARE. They are the pre-port
    #  adapter's minimum-viable defaults, carried over FIELD-FOR-FIELD so the engine swap is a
    #  single-variable experiment, and the [GAP] on this function is the honest status: no canonical
    #  spec exists for faction.Mil -> Unit construction. The fabrication gate is right to ask; the
    #  answer is "inherited, with a recorded gap", not "derived". (Morale is now the one EXCEPTION —
    #  see _morale_start_from_stability and its docstring above.)]
    power = max(1, int(round(faction.Mil)))
    sub = Subunit(
        shape='Line',
        troop_type='infantry',
        tier=2,                          # [canonical: inherited default — 200 troops, see GAP above]
        starting_position=(8, 12),       # [canonical: inherited default — see GAP above]
        advance_dir=1,
        stance='balanced',
        unit_type='melee',
    )
    m0 = _morale_start_from_stability(faction)
    return Unit(
        name=f'{faction.name}_force',
        faction=faction.name,
        power=power,
        command=4,                       # [canonical: inherited default — see GAP above]
        discipline=5,                    # [canonical: inherited default — see GAP above]
        discipline_start=5,              # [canonical: inherited default — see GAP above]
        morale=m0,                       # [d.1, ED-MB-0068: derived from faction.Sta — see above]
        morale_start=m0,                 # [d.1, ED-MB-0068: derived from faction.Sta — see above]
        subunits=[sub],
    )


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
    """
    unit_a = _faction_to_unit(faction_a)
    if faction_b is None:
        # Defenderless-territory garrison strength has no canonical spec; Mil=1.5 approximates the
        # pre-mass-battle v17 Ob 2 vs Ob 4 single-roll spread. Carried over from the pre-port adapter.
        # [canonical: inherited default — recorded [GAP], not canon; see the module header]
        unit_b = _faction_to_unit(_GarrisonStub(name='Uncontrolled', Mil=1.5))
    else:
        unit_b = _faction_to_unit(faction_b)

    with rngsource.using(getattr(world, 'rng', None)):
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
