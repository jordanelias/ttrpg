"""The identifier census must be current, and `--check` must be able to SEE the roll-up.

WHY THIS EXISTS (ED-IN-0162). `references/identifier_census.json` and the 15
`systems/*/_identifier_census.yaml` were generated 2026-08-04 and left ungated. The docs they
index changed on 08-08 (the personal-combat 5→1 consolidation) and 08-10 (15 flow skeletons), so
by 08-12 the combat census listed SEVEN docs — including `combat_v30.md` and three
`_index`/`_infill` files the consolidation deleted — and had never heard of
`combat_reference_v1.md` or `combat_flow_skeleton_v1.md`.

That would be ordinary staleness except for the direction it flows: `references/glossary/` is
BUILT from the census (`build_glossary._from_identifier_census`) and IS gated by
`test_build_glossary.test_committed_output_matches_a_fresh_build`. A gated artifact downstream of
an ungated one. The glossary's `--check` can only ever prove the glossary matches its inputs; it
is structurally incapable of noticing that its inputs stopped matching the tree — and it ran green
for eight days while doing exactly that.

AND THE TOOL'S OWN `--check` COULD NOT HAVE CAUGHT IT EITHER. `main()` returned on the `--check`
branch BEFORE the roll-up write, so the one file ED-IN-0162 names first was the one file `--check`
never compared. Wiring the old `--check` into a gate would have shipped an assertion incapable of
observing the failure it excludes (CLAUDE.md §0.1 point 2). The fix is in the tool; the falsifier
for the fix is `test_check_sees_a_corrupted_rollup` below, which is the mutation the pre-fix code
survives.

NO WORKING-TREE MUTATION. `test_engine_atlas` plants a probe folder in the real tree under a
reserved name and cleans it up; that is safe there because nothing else reads `zz_atlas_probe`.
Corrupting `references/identifier_census.json` in place would NOT be safe: `test_build_glossary`
reads it, `pytest` runs under `-n auto`, and a concurrent reader seeing a deliberately-broken file
is the C6 race in miniature. So the two-sided tests build a minimal fake repo in `tmp_path` and
monkeypatch the module's `REPO` instead.
"""
import importlib.util
import json
import os
import subprocess
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
BUILDER = os.path.join(ROOT, 'tools', 'build_identifier_census.py')
ROLLUP = os.path.join(ROOT, 'references', 'identifier_census.json')

pytest.importorskip('yaml')


def _census_builder():
    """A FRESH module object per test — the tool memoises `_MODULE_NAMES` / `_DOC_STEMS` on
    globals keyed to whatever `REPO` was when they were first filled. A shared import would let
    one test's fake-repo caches leak into another's real-repo run."""
    # NOT named `_builder`: `test_engine_atlas.py` already owns that name, and
    # `test_test_register.py::test_no_new_duplicated_helpers` is a RATCHET on helper names
    # defined in more than one test file. It caught this collision (22 vs baseline 21).
    # Renamed rather than baselined — raising the baseline is the defect the ratchet exists
    # to prevent (ED-IN-0165 hit the identical case with `_gate`).
    spec = importlib.util.spec_from_file_location('bic', BUILDER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _fake_repo(tmp_path, mod, monkeypatch):
    """Smallest tree the census can render: one subsystem, one doc, one identifier."""
    (tmp_path / 'systems' / 'probe').mkdir(parents=True)
    (tmp_path / 'systems' / 'probe' / 'probe_design_v1.md').write_text(
        '# Probe\n\n## Status: CANONICAL\n\nThe probe_threshold_value governs the probe.\n',
        encoding='utf-8')
    (tmp_path / 'references').mkdir()
    monkeypatch.setattr(mod, 'REPO', str(tmp_path))
    # These caches are populated from `git ls-files` in REPO; a tmp dir is not a repo, so they
    # would stay empty and be re-derived on every call. Reset explicitly so the behaviour does
    # not depend on that happening to be true.
    monkeypatch.setattr(mod, '_MODULE_NAMES', set())
    monkeypatch.setattr(mod, '_DOC_STEMS', set())
    return tmp_path


# ------------------------------------------------------------------------------------------
# The freshness gate itself — what ED-IN-0162 asked for
# ------------------------------------------------------------------------------------------
@pytest.mark.slow
def test_committed_census_matches_a_fresh_build():
    """~3s corpus sweep. This is the gate that did not exist for eight days."""
    r = subprocess.run([sys.executable, BUILDER, '--check'],
                       capture_output=True, text=True, cwd=ROOT)
    assert r.returncode == 0, (
        f'identifier census is stale:\n{r.stdout}\n{r.stderr}\n'
        'Regenerate with `python3 tools/build_identifier_census.py`, then regenerate the '
        'glossary that reads it (`python3 tools/observability/build_glossary.py`), and commit.')


def test_the_rollup_is_committed_and_covers_every_subsystem():
    """The roll-up's subsystem set must equal the per-subsystem files' — the two are one build.

    A roll-up naming a subsystem with no census file (or vice versa) means the two halves were
    written by different runs, which is precisely the state `--check` now refuses.
    """
    payload = json.load(open(ROLLUP, encoding='utf-8'))
    from_rollup = set(payload['by_subsystem'])
    on_disk = {d for d in os.listdir(os.path.join(ROOT, 'systems'))
               if os.path.isfile(os.path.join(ROOT, 'systems', d, '_identifier_census.yaml'))}
    assert from_rollup == on_disk, (
        f'roll-up and per-subsystem files disagree: '
        f'roll-up only {sorted(from_rollup - on_disk)}, disk only {sorted(on_disk - from_rollup)}')


# ------------------------------------------------------------------------------------------
# Two-sided falsifiers — each names the mutation it kills
# ------------------------------------------------------------------------------------------
def test_check_is_green_on_a_freshly_written_tree(tmp_path, monkeypatch):
    """The control. Without it, the two red-side tests below could pass on a --check that is
    simply always 1, which asserts nothing."""
    mod = _census_builder()
    _fake_repo(tmp_path, mod, monkeypatch)
    assert mod.main([]) == 0
    assert mod.main(['--check']) == 0


def test_check_sees_a_corrupted_rollup(tmp_path, monkeypatch, capsys):
    """THE MUTATION THE PRE-FIX CODE SURVIVES (ED-IN-0162).

    Before the fix, `main()` returned on the `--check` branch before ever touching the roll-up,
    so this mutation exited 0 and the ONE artifact the finding names first was ungatable.
    """
    mod = _census_builder()
    repo = _fake_repo(tmp_path, mod, monkeypatch)
    assert mod.main([]) == 0
    rollup = repo / 'references' / 'identifier_census.json'
    payload = json.loads(rollup.read_text())
    payload['engine_names'] = payload['engine_names'] + 1
    rollup.write_text(json.dumps(payload, indent=1, sort_keys=True) + '\n', encoding='utf-8')

    assert mod.main(['--check']) == 1, 'a corrupted roll-up was not reported as drift'
    assert 'identifier_census.json' in capsys.readouterr().out, \
        'the roll-up drifted but the report did not name it'


def test_check_sees_a_corrupted_subsystem_file(tmp_path, monkeypatch):
    """The direction that already worked. Kept so a refactor cannot trade one side for the other."""
    mod = _census_builder()
    repo = _fake_repo(tmp_path, mod, monkeypatch)
    assert mod.main([]) == 0
    per_sub = repo / 'systems' / 'probe' / '_identifier_census.yaml'
    per_sub.write_text(per_sub.read_text() + '\nzz_injected: true\n', encoding='utf-8')
    assert mod.main(['--check']) == 1


def test_a_deleted_rollup_is_drift_not_a_crash(tmp_path, monkeypatch):
    """Absence and mismatch must land in the same bucket. A generator that raises on a missing
    output turns a gate failure into a traceback, which reads as tooling breakage rather than as
    the drift it is."""
    mod = _census_builder()
    repo = _fake_repo(tmp_path, mod, monkeypatch)
    assert mod.main([]) == 0
    (repo / 'references' / 'identifier_census.json').unlink()
    assert mod.main(['--check']) == 1


def test_scoped_check_does_not_report_rollup_drift(tmp_path, monkeypatch):
    """`--subsystem X --check` computes ONE row, so it cannot honestly compare a 15-row roll-up.

    It must stay silent about the roll-up rather than report drift that is an artifact of the
    flag — otherwise the scoped mode is unusable and someone deletes the roll-up check to fix it.
    """
    mod = _census_builder()
    repo = _fake_repo(tmp_path, mod, monkeypatch)
    assert mod.main([]) == 0
    rollup = repo / 'references' / 'identifier_census.json'
    rollup.write_text('{"deliberately": "wrong"}\n', encoding='utf-8')
    assert mod.main(['--subsystem', 'probe', '--check']) == 0, \
        'a scoped check reported roll-up drift it has no standing to judge'
    assert mod.main(['--check']) == 1, \
        'the full check must still catch what the scoped check correctly ignored'
