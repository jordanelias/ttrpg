"""The generated atlas must stay fresh, deterministic, and honest about what it skipped.

`references/ENGINE_ATLAS.md` renders the countable half of the engine picture: which subsystems
exist, which contracts they own, what a seeded campaign actually called, and which public
callables the authored flow skeletons never name. It is generated, so the failure modes are the
generator's, not a writer's:

  1. STALENESS — the committed file no longer equals a fresh render, so a reader makes decisions
     against numbers that stopped describing the tree.
  2. NON-DETERMINISM — the same inputs render different bytes, which makes (1) unfalsifiable.
     This is not hypothetical: the sibling `build_contract_index.py` shipped exactly this defect
     (a non-total sort over a set difference) and its `--check` was a coin flip until it was
     found. Same class, so it is pinned here from the start.
  3. SILENT SKIPPING — the worst one, and the reason this tool reconciles the filesystem against
     the roster instead of trusting either. An atlas that quietly omits a subsystem someone added
     last week is more dangerous than no atlas, because its completeness is assumed.

(3) is what the drift assertions below exist for: a new folder must SHOW UP as undeclared rather
than vanish, and a deleted one must be reported rather than crash the render.
"""
import importlib.util
import json
import os
import shutil
import subprocess
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
BUILDER = os.path.join(ROOT, 'tools', 'build_engine_atlas.py')
OUT_MD = os.path.join(ROOT, 'references', 'ENGINE_ATLAS.md')
OUT_JSON = os.path.join(ROOT, 'references', 'engine_atlas.json')

pytest.importorskip('yaml')


def _builder():
    spec = importlib.util.spec_from_file_location('bea', BUILDER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_atlas_is_current():
    r = subprocess.run([sys.executable, BUILDER, '--check'],
                       capture_output=True, text=True, cwd=ROOT)
    assert r.returncode == 0, (
        f'engine atlas is stale:\n{r.stdout}\n{r.stderr}\n'
        'Regenerate with `python tools/build_engine_atlas.py` and commit.')


def test_render_is_deterministic():
    """Same inputs, same bytes — otherwise `--check` above is a coin flip.

    Digested with sha256, never `hash()`: Python's builtin string hash is itself seed-randomised,
    so a `hash()`-based comparison across seeds can never agree and would fail on a perfectly
    deterministic renderer.
    """
    mod = _builder()
    first, second = mod.build(), mod.build()
    for path in first:
        assert first[path] == second[path], \
            f'{os.path.relpath(path, ROOT)} differs between two builds in one process'

    digests = set()
    for seed in ('0', '1', '9999'):
        env = dict(os.environ, PYTHONHASHSEED=seed)
        r = subprocess.run(
            [sys.executable, '-c',
             'import importlib.util,sys,hashlib;'
             f'spec=importlib.util.spec_from_file_location("bea",{BUILDER!r});'
             'm=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);'
             'd=m.build();h=hashlib.sha256();'
             '[h.update(d[k].encode()) for k in sorted(d)];'
             'sys.stdout.write(h.hexdigest())'],
            capture_output=True, text=True, env=env, cwd=ROOT)
        assert r.returncode == 0, f'render failed under PYTHONHASHSEED={seed}: {r.stderr}'
        digests.add(r.stdout.strip())
    assert len(digests) == 1, (
        f'render differs across PYTHONHASHSEED values ({len(digests)} distinct) — something '
        'iterates a set or dict whose order is not pinned')


def test_every_subsystem_folder_on_disk_appears():
    """Discovery is from the FILESYSTEM, so an addition can never be silently skipped."""
    mod = _builder()
    rows, drift, _ = mod.build_rows()
    listed = {r['subsystem'] for r in rows}
    on_disk = set(mod.discovered_subsystems())
    assert listed == on_disk, (
        f'atlas rows {sorted(listed)} do not match the folders on disk {sorted(on_disk)} — '
        'the generator is not discovering subsystems from the filesystem')


def test_an_added_subsystem_surfaces_as_drift(tmp_path):
    """A new folder must APPEAR, flagged as not-yet-declared — not vanish.

    Mutation-verified by construction: this test creates the mutation. It writes a real folder
    under `systems/`, rebuilds, and asserts the generator both rows it and names it as drift.
    The folder is removed in a `finally`, so a failure cannot leave the tree dirty.
    """
    mod = _builder()
    new = os.path.join(ROOT, 'systems', 'zz_atlas_probe')
    # Self-heal our OWN reserved name. A previous run killed mid-test leaves the folder behind,
    # which then pollutes the generated atlas and fails test_atlas_is_current with a confusing
    # message about staleness. Only ever removed when it looks like our probe and nothing else —
    # clobbering a real subsystem folder would be far worse than a confusing failure.
    if os.path.isdir(new):
        leftover = sorted(os.listdir(new))
        assert leftover in ([], ['thing.py'], ['__pycache__', 'thing.py']), (
            f'{new} exists and is not this test\'s probe ({leftover}) — refusing to remove it')
        shutil.rmtree(new)
    os.makedirs(new)
    try:
        with open(os.path.join(new, 'thing.py'), 'w', encoding='utf-8') as fh:
            fh.write('def probe_entry():\n    return 1\n')
        rows, drift, _ = mod.build_rows()
        names = {r['subsystem'] for r in rows}
        assert 'zz_atlas_probe' in names, \
            'a newly added subsystem folder did not appear in the atlas at all'
        assert 'zz_atlas_probe' in drift['folders_without_roster_row'], \
            'a newly added folder was not reported as missing a roster row'
        row = next(r for r in rows if r['subsystem'] == 'zz_atlas_probe')
        assert row['declared_in_roster'] is False
        assert row['coverage']['public'] >= 1, \
            'the coverage check did not see the new file\'s public callable'
    finally:
        shutil.rmtree(new, ignore_errors=True)


def test_missing_input_is_reported_not_silently_absorbed(monkeypatch):
    """An absent input must be stated, because its absence looks exactly like a finding.

    Without the execution trace every subsystem renders as "not in trace", which a reader would
    read as "nothing runs" rather than "the file was not there".
    """
    mod = _builder()
    monkeypatch.setattr(mod, 'EXEC_TRACE', os.path.join(ROOT, 'references', '__no_such_file.json'))
    _, drift, _ = mod.build_rows()
    assert any('__no_such_file' in p for p in drift['absent_inputs']), \
        'a missing input file was absorbed silently instead of being reported'


def test_json_and_markdown_agree_on_the_roster():
    """The two outputs are rendered from one pass; if they disagree, one is stale."""
    assert os.path.isfile(OUT_JSON), 'engine_atlas.json not generated'
    payload = json.load(open(OUT_JSON, encoding='utf-8'))
    md = open(OUT_MD, encoding='utf-8').read()
    for row in payload['subsystems']:
        assert f"`{row['subsystem']}`" in md, \
            f"{row['subsystem']} is in the JSON but not the rendered atlas"
