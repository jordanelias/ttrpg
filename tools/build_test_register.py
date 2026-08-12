#!/usr/bin/env python3
"""build_test_register.py — a generated, queryable inventory of what the test suite GUARDS.

WHY THIS EXISTS (Jordan, 2026-08-02): "track all your tests and their results in such a way that
they don't just become detritus." The suite is 130+ files and ~25,000 LOC, and what each file
defends lives only in its docstring — so the corpus is unqueryable. Nobody can ask "which guards
are mutation-verified?", "which tests assert nothing?", or "what protects the Key substrate?"
without reading everything, which means nobody asks.

GENERATED, NEVER HAND-MAINTAINED. That is the whole design constraint, and it is not a style
preference: this session measured seven separate registries that had rotted into fiction because a
human had to remember to update them. A register that requires maintenance becomes the detritus it
was built to prevent. Everything here is derived from the AST at build time, so it cannot drift
from the tree — if a test is deleted, its row vanishes on the next build.

WHAT IT DERIVES, and why each field earns its place:
  * `guards` — the module docstring's first line: the one-sentence answer to "what breaks if this
    is deleted?" A file with no docstring is reported with `guards: null`, which is itself the
    finding (an unexplained guard is one nobody can evaluate).
  * `mutation_verified` — parsed from the `mutation-verified N/M` convention this repo uses.
    Distinguishes a guard someone TRIED TO BREAK from one merely written. CLAUDE.md §0.1 point 3:
    "adversarially reviewed" without an artifact is unfalsifiable.
  * `measured` — whether the docstring cites a measurement (`MEASURED`, a `N -> M` transition).
    A guard whose docstring states what it found is auditable; one that does not is a claim.
  * `assertions` / `assertionless` — AST count of `assert` statements per test. A test function with
    zero assertions and no `pytest.raises`/`pytest.fail` is decoration: it executes code and cannot
    fail. This is the single most useful column, because that failure mode is invisible in a green
    run — the exact "reports clean over nothing" shape found seven times in tools/ this session.
  * `baselines` — module-level KNOWN_/EXPECTED_ sets, the shrink-only ratchets. Surfacing them means
    a permanent waiver has to be looked at rather than forgotten.

RESULTS. `--with-results` runs pytest per file and records pass/fail/duration. Kept OPTIONAL and
OFF by default because the full suite is ~4 minutes: a register that is expensive to build gets
built rarely and is stale when read. The static half is ~1 second and is the half that answers
"what do we guard".

    python3 tools/build_test_register.py                # static inventory (fast)
    python3 tools/build_test_register.py --with-results  # + live pass/fail (slow)
    python3 tools/build_test_register.py --check         # drift gate, no write
"""
from __future__ import annotations

import argparse
import ast
import json
import os
import re
import subprocess
import sys
import time

# Primitives (repo root, lane roster, token estimate, ids, Status reader) are
# owned by tools/ci_common.py — plan G7, ED-IN-0159 §8.3. See its module docstring;
# the two lines below are the bootstrap, anchored on THIS file's directory.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

ROOT = ci_common.REPO
sys.path.insert(0, os.path.join(ROOT, 'tools', 'observability'))
try:
    # REUSE the owned lane mapper (CLAUDE.md §8 — every rule lives once). `infer_lane` returns None
    # honestly when nothing matches rather than force-classifying, which is the behaviour this
    # register needs: an undetermined lane must read as undetermined, not as a guess.
    from obs_core import infer_lane as _infer_lane
except Exception:                                    # pragma: no cover - degraded, still useful
    def _infer_lane(_p):
        return None
TEST_DIR = os.path.join(ROOT, 'tests', 'valoria')
OUT = os.path.join(ROOT, 'references', 'test_register.json')

# Two separate facts, because the corpus proved they are not the same one. MEASURED at
# introduction: 32 of 132 files CLAIM mutation verification, but almost none state a kill count —
# phrasings run from "mutation-verified: import deleted" to "Mutation-verified at introduction".
# A claim and an artifact are different things (CLAUDE.md §0.1 point 3), so the register records
# the claim as a boolean and the count only when one is actually given. Collapsing them into a
# single N/M field reported 0/132 and was simply false.
MUTATION_CLAIM_RE = re.compile(r'mutation[- ]verified', re.I)
MUTATION_COUNT_RE = re.compile(r'mutation[- ]verified[^.\n]{0,40}?(\d+)\s*/\s*(\d+)', re.I)
MEASURED_RE = re.compile(r'\bMEASURED\b|\d+\s*(?:->|→)\s*\d+')


IMPORT_RE = re.compile(r'^\s*(?:from|import)\s+((?:systems|engine|tools)[\w.]*)', re.M)
# MEASURED: only 8 of 135 test files import their subject directly — 122 reach it through
# `spec_from_file_location`, `importorskip`, or a `sys.path` insert, naming the target as a PATH
# STRING or a bare module name. Deriving subject from import statements alone found 5 of 132 and
# was measuring how I assumed tests are written, not how they are.
PATHLIT_RE = re.compile(r'[\'"]((?:systems|engine|tools|references|registers)[\w/.\-]*)[\'"]')
SEGLIT_RE = re.compile(r'[\'"](systems|engine|tools)[\'"]\s*,\s*[\'"]([\w\-]+)[\'"]')


def _subject(src: str):
    """(lane, modules) — WHAT this test guards, derived from what it imports.

    Jordan, 2026-08-02: "test needs to indicate lane and, ideally, module or submodule." Derived
    rather than declared, for the same reason everything else here is: a hand-written `LANE = 'FA'`
    header is one more field to forget. A test's imports are what it actually exercises, and they
    cannot go stale without the test breaking first.

    A test importing several subsystems gets several modules and, honestly, whichever lanes those
    map to — cross-lane tests exist and flattening one to a single lane would be a fabricated
    tidiness. `declared_lane` (an optional module-level `LANE = "XX"`) overrides, for the cases
    where imports genuinely do not reveal the subject (a pure-tooling or corpus-wide guard).
    """
    mods = sorted({m.group(1) for m in IMPORT_RE.finditer(src)})
    paths = {m.replace('.', '/') + '.py' for m in mods}
    # Path strings, the way most of this suite actually names its subject.
    for m in PATHLIT_RE.finditer(src):
        lit = m.group(1)
        paths.add(lit)
        mods.append(lit)
    # os.path.join('tools', 'x.py') — the segment-pair form, invisible to a whole-path regex.
    for m in SEGLIT_RE.finditer(src):
        joined = f'{m.group(1)}/{m.group(2)}'
        paths.add(joined)
        mods.append(joined)
    mods = sorted(set(mods))
    lanes = sorted({ln for ln in (_infer_lane(p) for p in paths) if ln})
    return lanes, mods


def _first_line(doc: str | None) -> str | None:
    if not doc:
        return None
    for ln in doc.splitlines():
        ln = ln.strip()
        if ln:
            return ln[:180]
    return None


def _counts(fn: ast.AST) -> tuple[int, bool]:
    """(assert_count, has_other_failure_path) for one test function.

    `pytest.raises`, `pytest.fail`, `pytest.skip` and `self.assertX` are real failure paths that
    contain no `assert` statement, so counting bare asserts alone would libel them as decoration.
    """
    asserts = 0
    other = False
    for node in ast.walk(fn):
        if isinstance(node, ast.Assert):
            asserts += 1
        elif isinstance(node, ast.Call):
            f = node.func
            name = f.attr if isinstance(f, ast.Attribute) else getattr(f, 'id', '')
            if name in ('raises', 'fail', 'skip', 'xfail', 'importorskip', 'warns',
                        'approx', 'exit') or str(name).startswith('assert'):
                other = True
    return asserts, other


def scan() -> dict:
    files = {}
    for name in sorted(os.listdir(TEST_DIR)):
        if not (name.startswith('test_') and name.endswith('.py')):
            continue
        path = os.path.join(TEST_DIR, name)
        src = open(path, encoding='utf-8').read()
        try:
            tree = ast.parse(src)
        except SyntaxError:
            files[name] = {'error': 'unparseable'}
            continue
        mod_doc = ast.get_docstring(tree)
        # Scan the WHOLE SOURCE, not just the module docstring. First version looked only at the
        # module docstring and reported 3/132 while 32 files demonstrably mention mutation
        # verification — authors write the claim wherever it belongs: a function docstring next to
        # the guard it describes, or an inline comment. Restricting the scan measured my assumption
        # about where people write, not what they wrote.
        claim = bool(MUTATION_CLAIM_RE.search(src))
        cnt = MUTATION_COUNT_RE.search(src)
        tests, baselines, helpers = {}, [], []
        for node in tree.body:
            # Module-level non-test functions are HELPERS: reusable logic that lives inside a test
            # file, where nothing can import it. Jordan, 2026-08-02: "problematic ... especially if
            # they may end up containing useful code that gets missed for import." MEASURED at
            # introduction: 253 helper defs / 2,235 LOC across the suite, and 21 names defined in
            # MORE THAN ONE file — `_load` written 12 separate times, `_unit` 9, `field_path` 6.
            # Each duplicate is a helper someone needed, could not import, and rewrote.
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and \
                    not node.name.startswith('test_'):
                helpers.append({'name': node.name,
                                'loc': (node.end_lineno or node.lineno) - node.lineno + 1})
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and \
                    node.name.startswith('test_'):
                a, other = _counts(node)
                tests[node.name] = {
                    'summary': _first_line(ast.get_docstring(node)),
                    'assertions': a,
                    'assertionless': (a == 0 and not other),
                }
        for node in tree.body:
            if isinstance(node, ast.Assign):
                for t in node.targets:
                    if isinstance(t, ast.Name) and re.match(r'^(KNOWN|EXPECTED|BASELINE)_', t.id):
                        try:
                            n = len(ast.literal_eval(node.value))
                        except Exception:
                            n = None
                        baselines.append({'name': t.id, 'size': n})
        lanes, mods = _subject(src)
        declared = None
        for node in tree.body:
            if isinstance(node, ast.Assign):
                for t in node.targets:
                    if isinstance(t, ast.Name) and t.id == 'LANE':
                        try:
                            declared = ast.literal_eval(node.value)
                        except Exception:
                            pass
        files[name] = {
            'lanes': ([declared] if declared else lanes),
            'declared_lane': declared,
            'lane_derived': not declared and bool(lanes),
            'modules_under_test': mods,
            'guards': _first_line(mod_doc),
            'documented': bool(mod_doc),
            'mutation_claimed': claim,
            'mutation_count': (f'{cnt.group(1)}/{cnt.group(2)}' if cnt else None),
            'cites_measurement': bool(MEASURED_RE.search(mod_doc or '')),
            'test_count': len(tests),
            'assertionless_count': sum(1 for t in tests.values() if t['assertionless']),
            'baselines': baselines,
            'helpers': helpers,
            'helper_loc': sum(h['loc'] for h in helpers),
            'loc': src.count('\n') + 1,
            'tests': tests,
        }
    return files


def add_results(files: dict) -> None:
    for name in files:
        t0 = time.time()
        r = subprocess.run([sys.executable, '-m', 'pytest', os.path.join(TEST_DIR, name),
                            '-q', '--no-header'], capture_output=True, text=True, cwd=ROOT)
        tail = (r.stdout or '').strip().splitlines()
        files[name]['result'] = {
            'returncode': r.returncode,
            'summary': tail[-1][:200] if tail else '',
            'seconds': round(time.time() - t0, 1),
        }


def summarize(files: dict) -> dict:
    ok = [f for f in files.values() if 'error' not in f]
    byname: dict = {}
    for name, f in files.items():
        for h in (f.get('helpers') or []):
            byname.setdefault(h['name'], []).append(name)
    dupes = {k: sorted(v) for k, v in byname.items() if len(v) > 1}
    return {
        'files': len(files),
        'tests': sum(f.get('test_count', 0) for f in ok),
        'undocumented_files': sum(1 for f in ok if not f['documented']),
        'files_claiming_mutation': sum(1 for f in ok if f['mutation_claimed']),
        'files_with_a_kill_count': sum(1 for f in ok if f['mutation_count']),
        'files_citing_a_measurement': sum(1 for f in ok if f['cites_measurement']),
        'assertionless_tests': sum(f.get('assertionless_count', 0) for f in ok),
        'ratchet_baselines': sum(len(f.get('baselines') or []) for f in ok),
        'helper_defs': sum(len(f.get('helpers') or []) for f in ok),
        'helper_loc': sum(f.get('helper_loc', 0) for f in ok),
        # The extraction work-list: a helper name written in N files is a helper that wanted to be
        # importable. Ranked so the worst offenders are the first thing anyone reads.
        'duplicated_helpers': dict(sorted(dupes.items(), key=lambda kv: -len(kv[1]))),
        'duplicated_helper_names': len(dupes),
        'files_with_a_lane': sum(1 for f in ok if f.get('lanes')),
        'files_naming_a_module': sum(1 for f in ok if f.get('modules_under_test')),
        'by_lane': {ln: sum(1 for f in ok if ln in (f.get('lanes') or []))
                    for ln in sorted({x for f in ok for x in (f.get('lanes') or [])})},
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument('--with-results', action='store_true', help='run pytest per file (slow)')
    ap.add_argument('--check', action='store_true',
                    help='do not write; FAIL (exit 1) if the committed register has drifted')
    a = ap.parse_args()

    files = scan()
    if a.with_results:
        add_results(files)
    reg = {
        '_generated': ('GENERATED by tools/build_test_register.py — derived from the AST of '
                       'tests/valoria/. NEVER hand-edit: regenerate. A hand-maintained test '
                       'register becomes the detritus it exists to prevent.'),
        'schema_version': 1,
        'summary': summarize(files),
        'files': files,
    }
    text = json.dumps(reg, indent=1, sort_keys=True) + '\n'
    if a.check:
        # A DRIFT GATE THAT CANNOT FAIL IS DECORATION (ED-IN-0142). `--check` printed the fresh
        # stats and exited 0 unconditionally, so the register went stale three times in one
        # session and each time it was `tests/valoria/test_test_register.py` in CI -- not this
        # gate, not the local hook -- that noticed. The tool that owns the artifact must be the
        # one that reports it stale, or the local tier is green while CI is red, which is exactly
        # how a gate stops being trusted.
        if not os.path.exists(OUT):
            print(f'[test-register] MISSING: {OUT} — run the builder')
            return 1
        with open(OUT, encoding='utf-8') as f:
            if f.read() != text:
                print(f'[test-register] DRIFT: {OUT} does not match a fresh build.')
                print('           A test file was added, renamed or deleted. Re-run '
                      '`python3 tools/build_test_register.py` and commit the result.')
                return 1
    else:
        with open(OUT, 'w', encoding='utf-8') as f:
            f.write(text)
    s = reg['summary']
    print(f"[test-register] {s['files']} files · {s['tests']} tests")
    print(f"   claim mutation-verified : {s['files_claiming_mutation']}/{s['files']}")
    print(f"   ...WITH a kill count    : {s['files_with_a_kill_count']}   <- claim vs artifact")
    print(f"   files citing a measurement: {s['files_citing_a_measurement']}/{s['files']}")
    print(f"   undocumented files      : {s['undocumented_files']}")
    print(f"   ASSERTIONLESS tests     : {s['assertionless_tests']}   <- decoration if non-zero")
    print(f"   shrink-only baselines   : {s['ratchet_baselines']}")
    print(f"   files with a lane       : {s['files_with_a_lane']}/{s['files']}"
          f"  ({s['files_naming_a_module']} name a module under test)")
    print(f"   by lane: {s['by_lane']}")
    print(f"   helpers buried in tests : {s['helper_defs']} defs / {s['helper_loc']:,} LOC")
    print(f"   ...names in >1 file     : {s['duplicated_helper_names']}   <- extraction work-list")
    if not a.check:
        print(f"   -> {os.path.relpath(OUT, ROOT)}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
