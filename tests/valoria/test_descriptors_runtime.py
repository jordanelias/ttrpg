"""The descriptor registry's cooked artifact is what the engine reads, and the register of ratified-but-
unimplemented items is pinned here so neither an unauthorised deletion nor a silent addition passes.

CLAUDE.md §0.1 pt 3: a result claim carries the test that would have shown it wrong. The faction-roster
claim this file used to prove ("add a faction stat to `references/descriptor_registry.yaml` without a field in
the executable model and the engine stops importing") went with its subject at plan position `29b`: the
`Faction` dataclass, `game_state.py`'s import-time call and `descriptors.assert_faction_roster_is_covered`
are deleted, and so is the faction block (`ID-13`). Its six tests are retired; their source is in git at `5c5d8ec6`.
"""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))

from engine.substrate import descriptors  # noqa: E402


def test_the_registry_reader_reads_the_cooked_artifact_not_the_yaml():
    """Same discipline as keys.py vs key_types.json: one exporter owns the parse."""
    src = (REPO / 'engine' / 'substrate' / 'descriptors.py').read_text()
    assert 'descriptors.json' in src
    assert 'descriptor_registry.yaml' not in src.split('"""')[2], \
        'the reader must not reach for the YAML outside its docstring'


def test_the_attribute_roster_declares_itself_open_until_the_tenth_is_named():
    """Jordan ruled 2026-08-14 that the roster will be ten. Nine ship. The sentinel must persist
    until the tenth is named, so no reader mistakes the current roster for a closed one."""
    if len(descriptors.ATTRIBUTES) < 10:
        assert descriptors.ATTRIBUTES_PENDING_TENTH, (
            'the roster is short of ten and the pending_tenth sentinel is gone — either the tenth '
            'was named (add it and drop the sentinel) or the sentinel was dropped by accident'
        )
    else:
        assert not descriptors.ATTRIBUTES_PENDING_TENTH


#: The ratified-but-unimplemented rows expected on disk. A row leaves this set ONLY by being
#: implemented, and the commit that implements it edits this line — which is the whole point:
#: deleting a row and deleting its name here are the same act, done deliberately, in one place.
#: `per_stat_floors` left at plan S5d (2026-08-22), wired into `Faction.adjust`. `faction_L` left
#: 2026-08-23: Jordan ruled "Legitimacy is a base", so `fac.legitimacy` is declared in the registry
#: and bound to the `L` field. The register went EMPTY, which is the correct state when nothing is
#: outstanding — and the set comparison below still observes an addition, which is the direction
#: that matters now.
#: ⚠ 2026-09-16: AND AN ADDITION IS WHAT IT OBSERVED. `fac_intel_multiplier` -- `fac.intel` was declared with
#: bounds Jordan RULED on 2026-08-23 and unreachable, because `engine.autoload.game_state.MULTS` carried no
#: `intel` key. It left the set at plan position `29b` (2026-10-01), deleted with `game_state.py`, `Faction`
#: and the `fac.*` registry block, so the register is EMPTY again. An empty register is the correct state
#: when nothing is outstanding, and it is not evidence the register is complete: this pin catches what enters
#: the block, and nothing catches what never reaches it.
EXPECTED_UNIMPLEMENTED = set()


def test_ratified_but_unimplemented_items_stay_visible():
    """These are RATIFIED canon decisions the executable model has not implemented.

    ⚠ REWRITTEN 2026-08-22 after an adversarial pass, because the previous version could not
    observe the failure its own docstring named. It said the list "must never be emptied by deleting
    entries instead of implementing them" and then only iterated whatever rows happened to be
    present, asserting each had a `needs` field. An emptied dict passes a loop over an empty dict —
    §0.1 pt 2, in the file whose subject is the register that records exactly this class of debt.
    It went green through S5d deleting a row from it.

    Now the SET is pinned. Implementing an item and deleting its row is correct and requires editing
    `EXPECTED_UNIMPLEMENTED` above; deleting a row because it was inconvenient fails here. Adding a
    newly-discovered gap also fails here, which is right — a new ratified-but-unimplemented item is
    a thing a human should see named.
    """
    data = json.loads((REPO / 'engine' / 'engine_params' / 'descriptors.json').read_text())
    unimpl = data['unimplemented']
    assert set(unimpl) == EXPECTED_UNIMPLEMENTED, (
        f'the ratified-but-unimplemented register is now {sorted(unimpl)}, expected '
        f'{sorted(EXPECTED_UNIMPLEMENTED)}. If an item was IMPLEMENTED, update the set above in the '
        f'same commit and say where. If one was merely deleted, restore it.'
    )
    for key, row in unimpl.items():
        assert row.get('needs'), f'{key} records no required action'
        assert row.get('why_it_matters'), f'{key} records no consequence'


def test_the_unimplemented_register_guard_can_observe_an_unauthorised_deletion():
    """§0.1 pt 2 for the test above — the property is "the set matches", and a set comparison that
    is never exercised against a mismatch proves nothing about the guard."""
    assert {'faction_L'} != EXPECTED_UNIMPLEMENTED, (
        'faction_L must not compare equal — it was implemented on 2026-08-23'
    )
    assert {'per_stat_floors'} != EXPECTED_UNIMPLEMENTED, (
        'a restored per_stat_floors row must not compare equal — it is implemented'
    )
    assert {'something_new'} != EXPECTED_UNIMPLEMENTED, (
        'a newly-filed gap must not compare equal — an addition is the direction this guard still '
        'protects now that the register is empty'
    )


def test_the_export_is_current():
    """A stale artifact means the engine is running on a roster the registry no longer declares."""
    r = subprocess.run([sys.executable, 'tools/export_descriptors.py', '--check'],
                       cwd=REPO, capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
