"""The descriptor registry is load-bearing at RUNTIME, and this proves the check can fail.

CLAUDE.md §0.1 pt 3: a result claim carries, in the same commit, the specific test that would have
shown it wrong. The claim being made by `engine/substrate/descriptors.py` and the import-time call
in `engine/autoload/game_state.py` is: *add a faction stat to `references/descriptor_registry.yaml`
without adding its field to the executable model and the engine stops importing.* A check that
cannot be observed failing is not a check (pt 2), so these tests plant the failure.

Subject test, under §0.1 pt 5's load-bearing predicate: this guards the engine's faction-stat
roster against canon — the executable model, not this repository's process. It earns its existence.
"""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys

import pytest

REPO = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))

from engine.substrate import descriptors  # noqa: E402


def test_the_roster_check_can_actually_fail():
    """Plant a registry stat with no implementing field; the check must raise."""
    real = dict(descriptors.FACTION_FIELD_MAP)
    descriptors.FACTION_FIELD_MAP['fac.invented'] = 'NoSuchField'
    try:
        with pytest.raises(RuntimeError) as exc:
            descriptors.assert_faction_roster_is_covered({'L', 'Sta', 'W', 'I', 'Mil', 'intel'})
        assert 'fac.invented' in str(exc.value)
        assert 'do not silence this check' in str(exc.value)
    finally:
        descriptors.FACTION_FIELD_MAP.clear()
        descriptors.FACTION_FIELD_MAP.update(real)


def test_the_live_engine_roster_passes_the_check():
    """The real Faction dataclass covers every registry-declared faction stat."""
    from dataclasses import fields as dc_fields

    from engine.autoload.game_state import Faction
    covered = descriptors.assert_faction_roster_is_covered({f.name for f in dc_fields(Faction)})
    assert covered == len(descriptors.FACTION_FIELD_MAP)
    assert covered >= 5, 'the registry declared fewer faction stats than expected — check the export'


def test_the_check_does_not_fire_on_code_fields_with_no_registry_entry():
    """One-way by design: `L` is declared nowhere and must NOT raise.

    Whether Legitimacy/Mandate is a base faction descriptor or a derived aggregate is an open
    ruling. A check that failed on it would force a session to answer Jordan's question.
    """
    assert descriptors.faction_bounds('L') is None
    descriptors.assert_faction_roster_is_covered({'L', 'Sta', 'W', 'I', 'Mil', 'intel'})


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


def test_ratified_but_unimplemented_items_stay_visible():
    """These are RATIFIED canon decisions the executable model has not implemented. The list may
    shrink as they land; it must never be emptied by deleting entries instead of implementing them."""
    data = json.loads((REPO / 'engine' / 'engine_params' / 'descriptors.json').read_text())
    unimpl = data['unimplemented']
    for key, row in unimpl.items():
        assert row.get('needs'), f'{key} records no required action'
        assert row.get('why_it_matters'), f'{key} records no consequence'


def test_the_export_is_current():
    """A stale artifact means the engine is running on a roster the registry no longer declares."""
    r = subprocess.run([sys.executable, 'tools/export_descriptors.py', '--check'],
                       cwd=REPO, capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
