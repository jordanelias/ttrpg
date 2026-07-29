"""Apparatus must not be keyed on a tree that has moved (ED-IN-0087).

WHY. `sim/` was retired 2026-07-21 (ED-IN-0071 P4). Two tools kept walking it, and neither made a
sound, because `os.walk` on a missing directory yields nothing rather than raising:

  · `tools/mechanics_index_gen.py` looked for `canon/` + `sim/` to locate the repo root, so it exited
    2 with `[FATAL] Could not find repo root` on every run. Its CI job carries
    `continue-on-error: true`, so a FATAL and a clean pass rendered identically in the checks list.
    Once revived it immediately reported 39 stale pointers and 3 schema errors it had been unable to
    report for a week.
  · `tools/ci_quantity_vocabulary_check.py` walked `sim/` for stat literals. That half of the check
    scanned **zero files** while the tool kept printing its contract-side findings and looking
    healthy — the worst shape a gate can take, since it is loudly doing half its job.

This is CLAUDE.md §0.1 point 5 exactly: the code was correct when written and stopped working
because something else moved. The prescribed answer is one owner for the operation, every site
routed through it, and a guard that fails on recurrence. `ci_common.sim_reference_roots()` is the
owner; this is the guard.

⚠️ The guards below assert COVERAGE, not just correctness of a path list. A root list that resolves
but covers no files is the exact failure being guarded against, and it would satisfy any assertion
that only checked the paths.
"""
import importlib.util
import os
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
TOOLS = os.path.join(ROOT, 'tools')
if TOOLS not in sys.path:
    sys.path.insert(0, TOOLS)

import ci_common  # noqa: E402


def _load(name):
    path = os.path.join(TOOLS, name)
    spec = importlib.util.spec_from_file_location(f'_{name[:-3]}_under_test', path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


# ─────────────────────────────────────────────── the owner: sim_reference_roots

def test_every_root_exists():
    roots = ci_common.sim_reference_roots(ROOT)
    assert roots, "sim_reference_roots() is empty — every caller now scans nothing"
    for r in roots:
        assert os.path.isdir(r), f"{r} does not exist"


def test_the_retired_flat_tree_is_not_among_them():
    roots = {os.path.relpath(r, ROOT).replace(os.sep, '/') for r in ci_common.sim_reference_roots(ROOT)}
    assert 'sim' not in roots, "the retired flat sim/ tree is back in the root list"
    assert 'engine' in roots, "the sim-reference CORE (engine/) is missing from the root list"


def test_roots_cover_every_subsystem_sim_package():
    """The glob is the point: a NEW subsystem's sim must be picked up without editing a list.

    Guards against someone 'simplifying' the glob into a hardcoded roster, which is how the
    hardcoded `sim/` got stale in the first place.
    """
    import glob
    expected = {os.path.relpath(p, ROOT).replace(os.sep, '/')
                for p in glob.glob(os.path.join(ROOT, 'systems', '*', 'sim')) if os.path.isdir(p)}
    got = {os.path.relpath(r, ROOT).replace(os.sep, '/') for r in ci_common.sim_reference_roots(ROOT)}
    assert expected, "no systems/*/sim packages found — this test would pass vacuously"
    missing = expected - got
    assert not missing, f"subsystem sim package(s) not covered by sim_reference_roots(): {sorted(missing)}"


def test_the_roots_actually_cover_python_files():
    """COVERAGE, not just resolvability. `os.walk` on a missing dir yields nothing silently, so a
    root list can be 'valid' and scan zero files — which is the defect, not the absence of it."""
    n = 0
    for r in ci_common.sim_reference_roots(ROOT):
        for _dirpath, _dirs, files in os.walk(r):
            n += sum(1 for f in files if f.endswith('.py'))
    assert n > 50, (
        f"the sim-reference roots cover only {n} .py file(s). The reference is ~11k LOC across "
        f"engine/ and systems/*/sim/; a number this low means the roots have gone stale again.")


# ──────────────────────────────────────── the two sites that were keyed on sim/

def test_quantity_vocabulary_check_scans_the_live_roots():
    mod = _load('ci_quantity_vocabulary_check.py')
    roots = ci_common.sim_reference_roots(ROOT)
    walked = sum(1 for _dp, _d, fs in mod._walk_all(roots) for f in fs if f.endswith('.py'))
    assert walked > 50, (
        f"scan_sim_literals would walk only {walked} .py file(s) — it walked 0 for the week after "
        f"sim/ was retired, while the tool kept printing contract-side findings and looking fine.")
    # It must not throw on the real corpus; a zero FINDING count is legitimate (the live call sites
    # use variable keys, e.g. engine/cross_scale/echo_transport.py's
    # `stat_deltas={er.affected_stat: er.delta}`, which carry no literal name to check).
    assert isinstance(list(mod.scan_sim_literals(roots)), list)


def test_scan_sim_literals_can_actually_find_a_literal(tmp_path):
    """POSITIVE CONTROL for the zero above (§0.1 point 4: a number needs a control, in either
    direction).

    On the live corpus this scanner finds nothing, and that is the true answer — but "finds nothing
    because the code moved to variable keys" and "finds nothing because the scan is dead" produce
    the identical output, which is the exact confusion that let it walk zero files for a week. So:
    hand it a corpus with a known literal and require it to come back with that literal. A mutation
    that empties the walk survived every other assertion here until this one existed.
    """
    mod = _load('ci_quantity_vocabulary_check.py')
    (tmp_path / 'mod.py').write_text(
        "def emit():\n"
        "    return Target(stat_deltas={'Legitimacy': 2, 'Stability': -1},\n"
        "                  impact_vector={'coercion': 0.5})\n", encoding='utf-8')
    hits = list(mod.scan_sim_literals([str(tmp_path)]))
    names = {h[3] for h in hits}
    assert names == {'Legitimacy', 'Stability', 'coercion'}, (
        f"the scanner missed literals it is supposed to catch: found {sorted(names)}. Either the "
        f"walk is dead or _STAT_DICT_RE no longer matches the call shape it targets.")
    surfaces = {h[0] for h in hits}
    assert surfaces == {'stat_deltas', 'impact_vector'}, f"surface labels wrong: {surfaces}"


def test_quantity_vocabulary_check_takes_its_DEFAULT_roots_from_the_owner():
    """Observes the DEFAULT path, not a root list the test supplies.

    The test above passes roots in, so it cannot see `main()` quietly going back to a hardcoded
    `sim/` — and a mutation that did exactly that survived until this test existed. Here the scanner
    is intercepted and `main([])` run with no arguments, so what is asserted is what the tool
    actually scans when nobody tells it where to look.
    """
    mod = _load('ci_quantity_vocabulary_check.py')
    seen = []
    real = mod.scan_sim_literals

    def spy(roots):
        seen.append(list(roots) if not isinstance(roots, str) else [roots])
        return real(roots)

    mod.scan_sim_literals = spy
    try:
        mod.main([])
    finally:
        mod.scan_sim_literals = real

    assert seen, "scan_sim_literals was never called — the code-side scan is gone entirely"
    roots = [os.path.relpath(r, ROOT).replace(os.sep, '/') for r in seen[0]]
    assert 'sim' not in roots, (
        f"the default roots include the retired flat sim/ tree: {roots}. os.walk on a missing "
        f"directory yields nothing, so this scans zero files while still printing findings.")
    expected = {os.path.relpath(r, ROOT).replace(os.sep, '/')
                for r in ci_common.sim_reference_roots(ROOT)}
    assert set(roots) == expected, (
        f"default roots diverge from ci_common.sim_reference_roots(), the single owner: "
        f"got {sorted(roots)}, owner says {sorted(expected)}")


def test_mechanics_index_gen_knows_godot_home_is_a_real_field():
    """`godot_home` records where a mechanic lives in the Godot port. The validator's key list never
    learned it, so it warned "unknown key" on legitimate data — invisible for as long as the tool
    was fataling out before it reached validation."""
    mod = _load('mechanics_index_gen.py')
    assert 'godot_home' in mod.OPTIONAL_MECHANIC_KEYS
    errs = mod.validate_mechanic('combat', {
        'scale': 'personal', 'faction': 'universal', 'sim_module': 'x.py',
        'test_status': 'not_implemented', 'canon_sources': [], 'godot_home': 'godot/skeleton/',
    }, {})
    assert not [e for e in errs if 'godot_home' in e.message], \
        f"godot_home flagged as an unknown key: {[str(e) for e in errs]}"


def test_mechanics_index_gen_finds_the_repo_root():
    """It returned None for a week, so `--strict` exited 2 before validating anything."""
    mod = _load('mechanics_index_gen.py')
    assert 'sim' not in mod.REPO_ROOT_MARKERS, (
        "mechanics_index_gen is keyed on the retired sim/ tree again — find_repo_root() will "
        "return None and the tool will exit 2 without validating anything.")
    for marker in mod.REPO_ROOT_MARKERS:
        assert os.path.isdir(os.path.join(ROOT, marker)), \
            f"repo-root marker {marker!r} does not exist — the walk cannot succeed"
    from pathlib import Path
    assert mod.find_repo_root(Path(ROOT)) == Path(ROOT).resolve()
    assert mod.find_repo_root(Path(os.path.join(ROOT, 'tests', 'valoria'))) == Path(ROOT).resolve(), \
        "find_repo_root does not walk up from a subdirectory"


def test_mechanics_index_gen_accepts_a_declared_absence():
    """`sim_module: null` states "no implementation exists" (scenario_authoring, ED-IN-0023). It is
    a declaration, and erroring on it pushed authors toward omitting the key or inventing a path."""
    mod = _load('mechanics_index_gen.py')
    errs = mod.validate_mechanic('x', {
        'scale': 'service', 'sim_module': None, 'test_status': 'not_implemented',
        'canon_sources': [],
    }, {})
    assert not [e for e in errs if 'sim_module' in e.message], \
        f"sim_module: null rejected: {[str(e) for e in errs]}"
    bad = mod.validate_mechanic('x', {
        'scale': 'service', 'sim_module': 42, 'test_status': 'not_implemented',
        'canon_sources': [],
    }, {})
    assert [e for e in bad if 'sim_module' in e.message], \
        "a genuinely wrong type is no longer caught — the fix went too far"


# NOTE. An earlier revision of this module asserted that ci_hooks_verifier ANNOUNCED Check 5 as
# inert — the interim measure taken while "what should skeleton-debt measure now?" was filed as a
# ruling this lane did not own. Jordan ruled it, and the answer made the announcement moot: the rule
# already had an owner in compliance_check, so Check 5 was deleted rather than repointed. The live
# assertion is test_check_5_is_retired_not_revived_because_the_rule_lives_elsewhere below, which
# pins the coverage that deletion depends on.


@pytest.mark.parametrize('rel', ['registers/mechanics_index.yaml'])
def test_no_retired_tree_pointers_remain_in_the_mechanics_index(rel):
    """The 39 pointers the revived gate surfaced are fixed; this stops them coming back.

    Scoped to `sim/` and `designs/` at the start of a path token — both trees are gone, so any
    occurrence is stale by construction rather than by judgment.

    Two exclusions, and both are real distinctions rather than convenience:
      · a line that STATES the path is gone is documentation of the correction, not a pointer to
        follow. The vocabulary for "this line declares an absence" already exists in
        `ci_claude_workflow_paths.ABSENCE_MARKER`, so it is imported rather than re-written
        (CLAUDE.md §8: never re-implement a rule). The line this catches reads *"sim/personal/
        contest.py no longer exists; live kernel is this package"* — beside an already-correct
        `sim_module:`.
      · a `canon_authoring_target` naming a doc that was never authored is not drift. Where an
        unwritten doc would eventually live is a design call owned by its subsystem lane, not by
        the IN lane running this sweep — observe, don't judge.
    """
    import re
    cwp = _load('ci_claude_workflow_paths.py')
    pat = re.compile(r'(?<![A-Za-z0-9_/.\-])(?:sim|designs)/[A-Za-z0-9_./\-]+\.(?:py|md|ya?ml|json)')
    real, excused = [], []
    with open(os.path.join(ROOT, rel), encoding='utf-8') as fh:
        for lineno, line in enumerate(fh, 1):
            for hit in pat.findall(line):
                if cwp.ABSENCE_MARKER.search(line) or f'{hit} (Pass' in line:
                    excused.append(hit)
                else:
                    real.append(f'{rel}:{lineno} {hit}')
    assert excused, (
        "no excused occurrences found — the two exclusions above are now untested, so this "
        "assertion no longer proves it can tell a live pointer from a documented absence.")
    assert not real, (
        f"{rel} points at the retired sim/ or designs/ trees: {real}. Resolve through "
        f"references/restructure_ledger.md — `tools/ci_claude_workflow_paths.py` has the resolver.")


# ─────────────────────────────── ED-IN-0088/0089: the rulings Jordan made on the filed items

def test_no_authoring_target_points_at_a_retired_tree():
    """The seven never-authored docs now name a LIVE subsystem home (ED-IN-0088).

    They previously carried `designs/…` prefixes for a tree retired 2026-07-19. That was filed as
    "not mine to rule" — where an unwritten doc belongs looked like a subsystem-lane design call.
    Jordan ruled it, and the resolution turned out to be derivable rather than discretionary: RULED
    §2a binds one subsystem = one folder = one ID lane, so each doc's home follows from its OWN
    `sim_module`, which already lives in a subsystem package. This asserts that derivation holds —
    if a mechanic's sim moves, its authoring target must move with it.
    """
    import yaml
    with open(os.path.join(ROOT, 'registers', 'mechanics_index.yaml'), encoding='utf-8') as fh:
        idx = yaml.safe_load(fh)
    checked, bad = 0, []
    for name, e in (idx.get('mechanics') or {}).items():
        target = e.get('canon_authoring_target')
        if not isinstance(target, str):
            continue
        checked += 1
        path = target.split(' (')[0].strip()
        if path.startswith(('designs/', 'sim/')):
            bad.append(f"{name}: authoring target still in a retired tree — {path}")
            continue
        sim = e.get('sim_module')
        if not (isinstance(sim, str) and sim.startswith('systems/')):
            continue
        # systems/<subsystem>/sim/x.py  ->  the doc belongs at systems/<subsystem>/
        subsystem = '/'.join(sim.split('/')[:2])
        if not path.startswith(subsystem + '/'):
            bad.append(f"{name}: doc home {path!r} does not match its sim's subsystem {subsystem!r}")
    assert checked >= 7, f"only {checked} authoring targets examined — expected at least the 7 ruled on"
    assert not bad, bad


def test_combat_carries_a_lane_qualified_validation_status():
    """ED-IN-0088. `validated` matched no enum value and errored every run. The replacement names
    the LANE and its standard rather than adding another Monte-Carlo tier — those are different
    kinds of evidence, and ranking them on one scale is what made the gap invisible."""
    import yaml
    with open(os.path.join(ROOT, 'registers', 'mechanics_index.yaml'), encoding='utf-8') as fh:
        idx = yaml.safe_load(fh)
    assert idx['mechanics']['combat']['test_status'] == 'validated_pc'
    assert 'validated_pc' in idx['test_status_values'], \
        "the value is used but not DEFINED in test_status_values — a vocabulary nobody can look up"
    mod = _load('mechanics_index_gen.py')
    assert 'validated_pc' in mod.VALID_TEST_STATUS
    assert 'validated' not in mod.VALID_TEST_STATUS, \
        "the bare `validated` must NOT be legalised — it is the ambiguity the lane tag replaces"


def test_check_5_is_retired_not_revived_because_the_rule_lives_elsewhere():
    """ED-IN-0088. Repointing Check 5 at systems/ would have re-implemented a rule
    compliance_check already owns (CLAUDE.md §8). This asserts the coverage the deletion relies on:
    if compliance_check ever stops reporting oversized systems/ docs, the rule has NO owner."""
    src = open(os.path.join(TOOLS, 'ci_hooks_verifier.py'), encoding='utf-8').read()
    assert 'skeleton-debt' not in src or 'RETIRED' in src, \
        "Check 5 appears to be live again — if it was re-specified, say so here and delete this test"
    import subprocess
    r = subprocess.run([sys.executable, os.path.join(TOOLS, 'compliance_check.py'),
                        '--check-only', '--repo-state', '.'],
                       cwd=ROOT, capture_output=True, text=True)
    out = r.stdout + r.stderr
    # The largest actionable doc the correct (§4) rule identifies. If the owner stops seeing it,
    # nothing in the repo is checking doc size any more.
    assert 'faction_politics_v30.md' in out and 'size_exceeded' in out, (
        "compliance_check no longer reports oversized systems/ docs. Check 5 was deleted BECAUSE "
        "this check owned the rule; with no owner, doc-size hygiene is unenforced.")


def test_stamp_staleness_ignores_apparatus_but_existence_still_covers_it():
    """ED-IN-0089. The stamp asks "has a canonical head moved?", which a validator or a unit test
    cannot answer — 24% of stamp-tripping commits moved no canonical head at all. Narrowed to the
    canon trees. The EXISTENCE half is deliberately NOT narrowed, and that is the half that catches
    CURRENT.md naming a deleted tool, so this asserts both directions."""
    sys.path.insert(0, TOOLS)
    import currency_consistency_check as C
    with open(os.path.join(ROOT, 'CURRENT.md'), encoding='utf-8') as fh:
        text = fh.read()
    all_paths, canon = C._current_md_paths(text), C._canonical_head_paths(text)
    assert canon, "no canonical-head paths — the staleness check would be inert"
    apparatus = [p for p in all_paths if p not in canon]
    assert apparatus, "no apparatus paths tracked — this test would pass vacuously"
    assert all(p.split('/')[0] in ('tools', 'tests') for p in apparatus), \
        f"something other than tools//tests/ was excluded from staleness: {apparatus}"
    assert 'tools' not in {p.split('/')[0] for p in canon}, \
        "tools/ is back in the staleness set — every apparatus commit will demand a stamp bump again"
    # …and the existence half must still see them.
    import inspect
    src = inspect.getsource(C.check_current_paths_exist)
    assert '_current_md_paths' in src and '_canonical_head_paths' not in src, (
        "the EXISTENCE check was narrowed too. CURRENT.md naming a deleted tool is real drift and "
        "must stay caught — only the STALENESS question was apparatus-blind.")


def test_a_tools_only_commit_does_not_trip_the_stamp_but_a_canon_head_does():
    """BEHAVIOURAL, not source-shaped. Asserting the path SETS differ leaves the stamp check free to
    keep using the wide one — a mutation reverting exactly that survived until this test existed.

    So: pretend every tracked path was committed far in the future, once for apparatus and once for
    a canonical head, and check which one the stamp actually reacts to.
    """
    sys.path.insert(0, TOOLS)
    import currency_consistency_check as C
    with open(os.path.join(ROOT, 'CURRENT.md'), encoding='utf-8') as fh:
        text = fh.read()
    canon = set(C._canonical_head_paths(text))
    apparatus = [p for p in C._current_md_paths(text) if p not in canon]
    real = C._git_last_commit_date

    def only(group):
        return lambda path: '2099-01-01' if any(
            path == g.rstrip('/') for g in group) else None

    try:
        C._git_last_commit_date = only(apparatus)
        drift = []
        C.check_current_stamp(drift)
        assert not drift, (
            f"a tools//tests/-only change tripped the staleness stamp: {drift}. That is the reflex "
            f"date-bump treadmill ED-IN-0089 removed — 24% of stamp trips moved no canonical head.")

        C._git_last_commit_date = only(canon)
        drift = []
        C.check_current_stamp(drift)
        assert drift, (
            "a CANONICAL HEAD moving no longer trips the stamp — the narrowing went too far and the "
            "check now catches nothing. Both halves of this test matter.")
    finally:
        C._git_last_commit_date = real
