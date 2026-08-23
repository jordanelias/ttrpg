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
    """Plant a REGISTRY stat with no bound field; the check must raise.

    THE FAILURE IS PLANTED IN `FACTION_STATS`, NOT `FACTION_FIELD_MAP`, AND THAT DISTINCTION IS THE
    ENTIRE VALUE OF THIS TEST. Until 2026-08-21 it mutated `FACTION_FIELD_MAP` — the hand-maintained
    dict in `tools/export_descriptors.py`. That proved the function raises when handed a bad map. It
    could not prove the claim being made, which is about the REGISTRY, and the claim was false: a
    sixth registry stat passed the check and the engine imported. §0.1 pt 2 says an assertion must
    be able to observe the failure it excludes; this one was observing a failure one layer below the
    one it excluded, and was green throughout.
    """
    real = dict(descriptors.FACTION_STATS)
    descriptors.FACTION_STATS['fac.invented'] = {'name': 'Invented', 'floor': 0, 'ceiling': 7}
    try:
        with pytest.raises(RuntimeError) as exc:
            descriptors.assert_faction_roster_is_covered({'L', 'Sta', 'W', 'I', 'Mil', 'intel'})
        assert 'fac.invented' in str(exc.value)
        assert 'do not silence this check' in str(exc.value).lower()
    finally:
        descriptors.FACTION_STATS.clear()
        descriptors.FACTION_STATS.update(real)


def test_the_roster_check_fails_when_a_bound_field_is_deleted():
    """Stage 2 of the check: the registry key is bound, but the dataclass no longer has the field."""
    with pytest.raises(RuntimeError) as exc:
        descriptors.assert_faction_roster_is_covered({'L', 'Sta', 'W', 'I', 'Mil'})  # `intel` gone
    assert 'fac.intel' in str(exc.value)
    assert 'intel' in str(exc.value)


def test_a_registry_edit_breaks_the_engine_end_to_end(tmp_path):
    """THE CLAIM, TESTED WHOLE: registry -> exporter -> reader -> raise. No monkeypatching.

    The two tests above mutate the loaded artifact, which is fast but still one step removed from
    the sentence in `engine/substrate/descriptors.py`: *add a stat to the registry and the engine
    stops importing*. This one adds a sixth faction stat to a COPY of the real
    `references/descriptor_registry.yaml`, runs the real `tools/export_descriptors.py` over it, and
    asserts the real check refuses the result. It is the only test here that would have caught the
    2026-08-21 defect from a cold read, so it is the one that must never be deleted for being slow.
    """
    import importlib.util

    src = (REPO / 'references' / 'descriptor_registry.yaml').read_text(encoding='utf-8')
    anchor = '    - {key: fac.stability,  name: Stability,  scale: "0-7"}'
    assert anchor in src, 'the registry\'s faction_stats block moved — re-anchor this test, do not drop it'
    doctored = tmp_path / 'registry.yaml'
    doctored.write_text(
        src.replace(anchor, anchor + '\n    - {key: fac.zeal,      name: Zeal,      scale: "0-7"}'),
        encoding='utf-8')

    spec = importlib.util.spec_from_file_location(
        '_export_descriptors_probe', REPO / 'tools' / 'export_descriptors.py')
    exporter = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(exporter)
    exporter.SRC = str(doctored)
    cooked = exporter.build()

    assert 'fac.zeal' in cooked['faction_stats'], 'the exporter did not carry the new registry stat'
    assert 'fac.zeal' not in cooked['faction_field_map'], \
        'the field map is hand-maintained; a registry edit must NOT populate it (that is the point)'

    real_stats = dict(descriptors.FACTION_STATS)
    descriptors.FACTION_STATS.clear()
    descriptors.FACTION_STATS.update(cooked['faction_stats'])
    try:
        with pytest.raises(RuntimeError) as exc:
            descriptors.assert_faction_roster_is_covered({'L', 'Sta', 'W', 'I', 'Mil', 'intel'})
        assert 'fac.zeal' in str(exc.value)
    finally:
        descriptors.FACTION_STATS.clear()
        descriptors.FACTION_STATS.update(real_stats)


def test_the_live_engine_roster_passes_the_check():
    """The real Faction dataclass covers every registry-declared faction stat."""
    from dataclasses import fields as dc_fields

    from engine.autoload.game_state import Faction
    covered = descriptors.assert_faction_roster_is_covered({f.name for f in dc_fields(Faction)})
    assert covered == len(descriptors.FACTION_STATS), \
        'the check must report the number of REGISTRY stats verified, not the number of map rows'
    assert covered >= 5, 'the registry declared fewer faction stats than expected — check the export'


def test_the_check_does_not_fire_on_code_fields_with_no_registry_entry():
    """One-way by design — and as of 2026-08-23 it protects nothing that exists, which is exactly
    when the property is worth testing rather than assuming.

    `L` used to be the live instance: declared nowhere, and a check that failed on it would have
    forced a session to answer Jordan's question about whether Legitimacy is a base descriptor. He
    ruled that it IS, so `fac.legitimacy` is declared and there is no unregistered Faction field
    left. The one-way direction stays because the reason was never "there is currently one" — a NEW
    dataclass field's registry status is a ruling, not a check's call.

    So this now plants a HYPOTHETICAL unregistered field rather than naming a real one. That is the
    only way to keep observing the property once the real case is gone; asserting it over the live
    roster would pass whether or not the direction still held."""
    assert descriptors.faction_bounds('L') == (0, 7), 'L is declared now — see the ruling of 2026-08-23'
    assert descriptors.faction_bounds('reputation') is None, 'fixture assumption: no such registry key'

    # The live roster PLUS a field the registry knows nothing about. One-way means this passes.
    descriptors.assert_faction_roster_is_covered(
        {'L', 'Sta', 'W', 'I', 'Mil', 'intel', 'reputation'})


def test_the_roster_check_still_fires_in_the_direction_it_is_supposed_to():
    """§0.1 pt 2 for the test above: "it does not raise" is also what a broken check does. Assert
    the OTHER direction still bites — a registry stat whose field is missing must stop the import."""
    import pytest as _pytest
    with _pytest.raises(RuntimeError):
        descriptors.assert_faction_roster_is_covered({'Sta', 'W', 'I', 'Mil', 'intel'})  # no L


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
#: and bound to the `L` field. The register is EMPTY, which is the correct state when nothing is
#: outstanding — and the set comparison below still observes an addition, which is the direction
#: that matters now.
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
