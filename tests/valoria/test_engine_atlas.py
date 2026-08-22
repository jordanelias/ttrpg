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


# `test_atlas_is_current` stood here and is GONE (culling wave 5, ED-IN-0194, 2026-08-22). The
# atlas is no longer committed, so "the committed copy is stale" is not a state the tree can be
# in. That the builder runs and writes its two artifacts is asserted once, for all six builders,
# in `test_generated_layer.py`; failure mode (1) in the docstring above is therefore retired and
# (2) and (3) — which are the ones a generator can still commit — are what this file now owns.


def test_render_is_deterministic(generated_layer):
    """Same inputs, same bytes.

    Requests `generated_layer` because "same inputs" is a PRECONDITION here, not a given: `build()`
    reads `references/{key_graph,execution_trace,execution_map}.json` through an `opt()` helper that
    substitutes an empty default when a file is absent. Those files are untracked as of culling
    wave 5, so on a clean checkout an early render can see them missing and a later one see them
    present — two honest renders of two different input sets, reported here as non-determinism.
    Depending on the fixture makes them present before the first render.

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

    Mutation-verified by construction: this test creates the mutation, then asserts the generator
    both rows it and names it as drift.

    THE MUTATION IS MADE IN A PRIVATE TREE, NOT IN `systems/` (fixed 2026-08-22 after CI caught it).
    This test used to `os.makedirs(ROOT/systems/zz_atlas_probe)` — a write to the SHARED working
    tree — while `test_render_is_deterministic` renders that same tree three times in three
    subprocesses. Under CI's `-n auto` the two land on different workers, the probe blinks into
    existence between two renders, and the digests differ. Locally the failure reads
    `15 subsystems` vs `16 subsystems`; on CI it surfaced one assertion later, where the message
    blames `PYTHONHASHSEED` — a misdiagnosis by construction, since the renderer was never at fault.

    The retired ED-IN-0172 note in `test_identifier_census.py` records this exact class from the
    other side: *"this file was careful never to WRITE to the working tree, and then shipped a test
    that READ the entire working tree while another test wrote to it."* Coordinating the readers is
    the other available fix; removing the write removes the hazard instead, which is why it is the
    one taken. `tmp_path` mirrors `systems/` by SYMLINK, so every real subsystem is still measured
    — no copy, no second tree to drift — and only the probe is genuinely new.
    """
    mod = _builder()

    # CHECKED FIRST, so the message is the true one. Mutation-verified 2026-08-22: with a probe
    # present in the real tree this assertion fires; without it here, `probe.mkdir()` below raises
    # a bare `FileExistsError` from pathlib (the real dir is already symlinked into the fake tree)
    # — a real detection wearing a message that points nowhere. Two causes reach this line: a
    # leftover from the pre-2026-08-22 version of this test, which really did write here and could
    # be killed mid-run, or someone reintroducing that write.
    real_probe = os.path.join(ROOT, 'systems', 'zz_atlas_probe')
    assert not os.path.isdir(real_probe), (
        f'{os.path.relpath(real_probe, ROOT)} exists in the REAL tree. This test builds its probe '
        f'in tmp_path precisely so it never does — a probe here is what races '
        f'test_render_is_deterministic under -n auto. Remove it, and if a test wrote it, stop '
        f'that write rather than deleting the folder on each run.')

    fake_systems = tmp_path / 'systems'
    fake_systems.mkdir()
    for entry in sorted(os.listdir(mod.SYSTEMS)):
        os.symlink(os.path.join(mod.SYSTEMS, entry), fake_systems / entry)
    probe = fake_systems / 'zz_atlas_probe'
    probe.mkdir()
    (probe / 'thing.py').write_text('def probe_entry():\n    return 1\n', encoding='utf-8')

    # Every `systems/` access in the builder routes through this one module constant, so repointing
    # it is sufficient — verified by grep at fix time (lines 52, 60, 92, 95, 96, 146, 197-198).
    # `SCAN_ROOTS` still scans the REAL tree for nomenclature, which is correct: a throwaway probe
    # must not contribute contract-name occurrences.
    mod.SYSTEMS = str(fake_systems)

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
    assert not os.path.isdir(real_probe), \
        'this test put its probe in the REAL tree — that is the -n auto race it exists to avoid'


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


def test_json_and_markdown_agree_on_the_roster(generated_layer):
    """The two outputs are rendered from one pass; if they disagree, one is stale."""
    assert os.path.isfile(OUT_JSON), 'engine_atlas.json not generated'
    payload = json.load(open(OUT_JSON, encoding='utf-8'))
    md = open(OUT_MD, encoding='utf-8').read()
    for row in payload['subsystems']:
        assert f"`{row['subsystem']}`" in md, \
            f"{row['subsystem']} is in the JSON but not the rendered atlas"
