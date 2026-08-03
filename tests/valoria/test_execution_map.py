"""The execution map must describe the code, not a memory of it (ED-IN-0123).

`references/EXECUTION_MAP.md` + `execution_map.json` answer "how does the game run, boot to
termination, with every module, contract, Key and owned scalar". Most of it is JOINED from live
registries and cannot rot independently. One part cannot be: the execution SPINE — the phase
order — is hand-transcribed from `engine/mc_v18.py` and `systems/overview/sim/season.py`, because
run_season's three steps are a documented composition rather than something an AST reveals as
phases.

Hand-transcription is the failure mode this repo keeps hitting: a map that was true when written
and quietly stopped being true. So every phase carries the exact source anchor it came from, and
the checks below re-run those anchors against the files. A refactor that renames
`accounting_boundary()` or drops the `for _ in range(max_s)` loop turns the map red instead of
leaving it confidently wrong.
"""
import json
import os
import subprocess
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MAP_JSON = os.path.join(ROOT, 'references', 'execution_map.json')

pytest.importorskip('yaml')


@pytest.fixture(scope='module')
def emap():
    with open(MAP_JSON, encoding='utf-8') as fh:
        return json.load(fh)


def test_every_spine_anchor_still_exists_in_its_source(emap):
    """THE LOAD-BEARING CHECK. Each phase names a file and a literal snippet; both must hold."""
    broken = []
    for phase in emap['phases']:
        path = os.path.join(ROOT, phase['source'])
        if not os.path.exists(path):
            broken.append((phase['id'], phase['source'], 'FILE MISSING'))
            continue
        if phase['anchor'] not in open(path, encoding='utf-8').read():
            broken.append((phase['id'], phase['source'], phase['anchor']))
    assert not broken, (
        "execution map is stale — these phases name code that no longer exists:\n"
        + "\n".join(f"  {pid}: {src} -> {anchor!r}" for pid, src, anchor in broken)
        + "\nRe-read the source and update SPINE in tools/build_execution_map.py.")


def test_the_spine_is_not_vacuous(emap):
    """A map with no phases, or whose anchors all trivially match, proves nothing.

    Floors per section so that losing one whole region — boot, loop or termination — cannot hide
    behind the others' rows.
    """
    ids = [p['id'] for p in emap['phases']]
    assert len([i for i in ids if i.startswith('boot')]) >= 5, ids
    assert len([i for i in ids if i.startswith('loop')]) >= 7, ids
    assert len([i for i in ids if i.startswith('term')]) >= 3, ids
    assert all(len(p['anchor']) > 12 for p in emap['phases']), (
        "an anchor short enough to match by accident is not an anchor: "
        + str([p['id'] for p in emap['phases'] if len(p['anchor']) <= 12]))


def test_declared_code_paths_resolve(emap):
    """A file map whose paths do not exist reads as coverage. `sim_module: none` is normalised to
    'no code declared' upstream, so anything left here is a genuine dead pointer."""
    dead = {n: m['code'] for n, m in emap['modules'].items()
            if m['code'] and m['code_exists'] is False}
    assert not dead, f"module contracts point at files that do not exist: {dead}"


def test_execution_claims_match_the_manifest(emap):
    """`executes` must be derived, never asserted. Re-derives it from the manifest and compares."""
    import yaml
    with open(os.path.join(ROOT, 'references', 'wiring_manifest.yaml'), encoding='utf-8') as fh:
        man = yaml.safe_load(fh)
    live = set()
    for group in ('modules', 'adapters'):
        for name, row in (man.get(group) or {}).items():
            if row.get('build') in ('live', 'gated'):
                live.add(name)
    claimed = {n for n, m in emap['modules'].items() if m['executes']}
    assert claimed == live, (
        f"execution map disagrees with wiring_manifest about what runs.\n"
        f"  only in map:      {sorted(claimed - live)}\n"
        f"  only in manifest: {sorted(live - claimed)}")
    assert live, "no unit reads as executing — the join is broken, not the game"


def test_map_is_current():
    """Regenerating must be a no-op. Catches a hand-edit of the generated files."""
    proc = subprocess.run(
        [sys.executable, os.path.join(ROOT, 'tools', 'build_execution_map.py'), '--check'],
        capture_output=True, text=True, cwd=ROOT)
    assert proc.returncode == 0, (
        f"execution map is stale — run `python3 tools/build_execution_map.py`.\n"
        f"{proc.stdout}\n{proc.stderr}")
