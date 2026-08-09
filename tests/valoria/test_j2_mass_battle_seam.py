"""J2's execution blocker, stated so it can fail — the guard for ED-MB-0065.

WHAT J2 SAID AND WHY IT HAS NOT HAPPENED.

Jordan ruled (J2, 2026-08-03) that canon mass battle is `tests/sim/mass_battle/` (28 modules) and
that the 5-module `systems/mass_battle/sim/` tree "is retired, not kept alongside". `CURRENT.md`
recorded that as resolved. It was not executed, and the 2026-08-06 vector audit (ED-IN-0148) found
the retired tree still present AND still structurally load-bearing.

Investigating it (ED-MB-0065) turned up a blocker that neither the ruling nor the audit had:

  1. The retired tree carries the campaign's ONLY strategic-layer seam.
     `engine/mc_v18.py` -> `faction_take_action` -> `_try_conquest` ->
     `systems.mass_battle.sim.massbattle.resolve_mass_battle(faction_a, faction_b, terrain, world)`.
     This runs every season. Deleting the tree breaks Military Conquest.

  2. The canon tree cannot receive that call. It is unit/geometry-scale
     (`run_battle(unit_a, unit_b)`, `run_multi_unit_battle(side_a, side_b, pairings, shapes...)`),
     not faction-scale, and it is CELL-BASED where the retired tree is the pre-cell v22 model.
     Feeding it a unit built by the strategic adapter `_faction_to_unit` raises
     `AttributeError: 'Subunit' object has no attribute 'cells_float'`. That is measured below,
     not asserted from reading.

  3. A LATER decision already contradicted J2. The evacuation keep-set (ED-IN-0127/0128,
     2026-08-04 — one day after J2) pins `systems/mass_battle/sim/massbattle.py` as 'keep', and
     `tests/valoria/test_evacuation_plan.py` guards that pin. So the tree is not lingering by
     neglect; a subsequent ruling kept it.

So J2 is RULED-BUT-NOT-EXECUTABLE until someone writes a strategic -> cell-based-Unit adapter.
`_faction_to_unit`'s own docstring already concedes the mapping is unspecified
("[GAP: no canonical spec for faction.Mil -> Unit construction]").

WHY THIS TEST IS A DISJUNCTION, NOT AN ASSERTION THAT THE GAP EXISTS.

A guard that simply pinned "the canon tree rejects strategic units" would fail the day someone
FIXES it, punishing the work it exists to invite. Instead this asserts the seam is *coherent* in
exactly one of two states:

  A. TODAY — the retired tree exists and the campaign imports it. Conquest resolves.
  B. AFTER J2 IS EXECUTED — the canon tree accepts a strategically-built unit, and the campaign's
     import has moved off the retired tree.

What it fails on is the HALF-DONE migration: the retired tree deleted while `faction_action` still
imports it, or the import repointed at a canon tree that cannot serve it. That is the failure mode
a naive execution of J2 produces, and it is the one worth catching.
"""
import importlib
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[2]
RETIRED_TREE = ROOT / 'systems' / 'mass_battle' / 'sim' / 'massbattle.py'
CAMPAIGN_IMPORTER = ROOT / 'systems' / 'factions' / 'sim' / 'faction_action.py'
STRATEGIC_SEAM = 'resolve_mass_battle'


def _importer_still_binds_the_retired_tree() -> bool:
    """Does the campaign's conquest path import the retired tree?"""
    src = CAMPAIGN_IMPORTER.read_text()
    return 'from systems.mass_battle.sim.massbattle import' in src


def _canon_accepts_a_strategic_unit() -> bool:
    """Can the canon tree resolve a battle between units built from strategic factions?

    Returns False on the specific incompatibility measured in ED-MB-0065, and True once a
    strategic -> cell-based-Unit adapter makes the call work. Any OTHER exception propagates —
    a new failure mode should be read, not silently folded into "still blocked".
    """
    sys.path.insert(0, str(ROOT / 'tests' / 'sim'))
    try:
        old = importlib.import_module('systems.mass_battle.sim.massbattle')
        canon = importlib.import_module('mass_battle.orchestration')
    except ImportError:
        return False
    finally:
        try:
            sys.path.remove(str(ROOT / 'tests' / 'sim'))
        except ValueError:
            pass

    class _Faction:
        Mil = 4.0
        name = 'GuardProbe'

    try:
        a = old._faction_to_unit(_Faction())
        b = old._faction_to_unit(_Faction())
    except Exception:
        return False

    try:
        canon.run_battle(a, b, max_turns=2)
    except AttributeError as exc:
        if 'cells_float' in str(exc):
            return False        # the measured ED-MB-0065 blocker, unchanged
        raise
    return True


def test_the_mass_battle_strategic_seam_is_in_a_coherent_state():
    """Exactly one of the two coherent states above must hold."""
    retired_present = RETIRED_TREE.exists()
    importer_binds = _importer_still_binds_the_retired_tree()

    state_a = retired_present and importer_binds
    state_b = (not importer_binds) and _canon_accepts_a_strategic_unit()

    assert state_a or state_b, (
        'the mass-battle strategic seam is half-migrated.\n'
        f'  retired tree present : {retired_present}\n'
        f'  campaign imports it  : {importer_binds}\n'
        'J2 (2026-08-03) retires systems/mass_battle/sim/, but the campaign path\n'
        'mc_v18 -> faction_take_action -> _try_conquest -> resolve_mass_battle() is the only\n'
        'faction-scale entry point in the corpus, and the canon tree tests/sim/mass_battle/ is\n'
        'unit/cell-scale. Executing J2 requires a strategic -> cell-based-Unit adapter FIRST.\n'
        'See ED-MB-0065 and registers/handoffs/HANDOFF_MB.md.'
    )


def test_the_campaign_conquest_path_can_actually_resolve():
    """State A is not merely declared — the seam must import and be callable.

    Skips (rather than fails) once J2 has been executed and the retired tree is gone, so this
    guard does not block the migration it documents.
    """
    if not RETIRED_TREE.exists():
        pytest.skip('retired tree gone — J2 executed; the state-coherence test above governs')
    mod = importlib.import_module('systems.mass_battle.sim.massbattle')
    seam = getattr(mod, STRATEGIC_SEAM, None)
    assert callable(seam), (
        f'{STRATEGIC_SEAM} is the campaign\'s only faction-scale battle entry point '
        '(faction_action.py:_try_conquest) and it is not callable'
    )


def test_the_later_keep_decision_is_still_recorded():
    """ED-IN-0127/0128 (2026-08-04) pinned this file as 'keep' one day AFTER J2 retired it.

    That conflict is the reason J2 reads 'resolved' while the tree is still here, and it must stay
    legible — if the pin is dropped without J2 being executed, the contradiction has been erased
    rather than settled.
    """
    plan = (ROOT / 'tests' / 'valoria' / 'test_evacuation_plan.py')
    if not plan.exists():
        pytest.skip('evacuation-plan guard retired; conflict recorded in ED-MB-0065')
    src = plan.read_text()
    assert "('systems/mass_battle/sim/massbattle.py', 'keep')" in src or not RETIRED_TREE.exists(), (
        'the evacuation keep-pin for systems/mass_battle/sim/massbattle.py was removed while the '
        'file is still present. Either J2 was executed (delete the file too) or the pin should '
        'stand — see ED-MB-0065 for why the two rulings conflict.'
    )
