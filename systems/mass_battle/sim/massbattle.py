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
command 4, discipline 5, morale 5, power = round(faction.Mil)), and the canon engine can express far
more than that — troop types, equipment, formations, multi-subunit hierarchies, orders of battle.
Every one of those is a design question about what a faction's army IS at the strategic scale, and
none of them is answered by porting an engine. The defaults are carried over UNCHANGED and marked,
so the behaviour delta measured for this commit is attributable to the ENGINE swap alone and not to
a simultaneous change in how armies are built.

[GAP: faction -> unit construction lacks canonical spec — carried over from the pre-port adapter.]
"""
from __future__ import annotations

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

    def __init__(self, name, Mil):
        self.name = name
        self.Mil = Mil


def _faction_to_unit(faction):
    """Build a canon-engine Unit from a strategic-layer faction.

    Field-for-field identical to the pre-port construction. The canon engine's `Unit`/`Subunit`
    dataclasses accept the same names, which is why this survived the swap unchanged — and it is
    also why the swap is a clean single-variable experiment on the RESOLUTION model.
    """
    # [canonical: mass_battle_integration_v30.md §4.10 sub-step 3 — the strategic entry point. ⚠ THE
    #  VALUES BELOW ARE NOT CANON AND THIS COMMENT DOES NOT CLAIM THEY ARE. They are the pre-port
    #  adapter's minimum-viable defaults, carried over FIELD-FOR-FIELD so the engine swap is a
    #  single-variable experiment, and the [GAP] on this function is the honest status: no canonical
    #  spec exists for faction.Mil -> Unit construction. The fabrication gate is right to ask; the
    #  answer is "inherited, with a recorded gap", not "derived".]
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
    return Unit(
        name=f'{faction.name}_force',
        faction=faction.name,
        power=power,
        command=4,                       # [canonical: inherited default — see GAP above]
        discipline=5,                    # [canonical: inherited default — see GAP above]
        discipline_start=5,              # [canonical: inherited default — see GAP above]
        morale=5,                        # [canonical: inherited default — see GAP above]
        morale_start=5,                  # [canonical: inherited default — see GAP above]
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
