#!/usr/bin/env python3
"""duplication_census.py — the instrument behind every number in 00_code_leanness.md (ED-IN-0159).

WHY THIS EXISTS. The audit next to it argues that instruments left uncommitted and unrun are the
repo's recurring defect (§4: `flag_ablation.py`, `harness.py` and a 22-check invariant battery all
sit in audit folders, runnable, in no CI job). An audit making that argument from ad-hoc inline
python would be self-refuting — and `ci_claim_provenance_check` (ED-PC-0040) correctly refused the
ledger entry until this file existed. So: every quantitative claim in the companion document is
reproduced here, and a number that this script cannot reproduce should be treated as withdrawn.

Read-only. Writes nothing, imports nothing from the repo. Run:  python3 duplication_census.py

WHAT IT DOES NOT MEASURE, deliberately. No orphan/dead-code census. Three separate attempts at one
were discarded for method defects (00_code_leanness.md §7) — an AST import graph cannot dot-resolve
`combat_engine_v1`'s bare imports and calls a demonstrably-live module an orphan; a reference scan
counts pytest-collected test files as uncalled. Shipping a number I know to be unsound, next to
numbers I have verified, would launder the bad one.
"""
import os
import re
import subprocess
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))


SELF = 'audit/2026-08-11-code-leanness/duplication_census.py'


def git_ls(*patterns):
    """Tracked paths matching `patterns`, minus deprecated/ and minus THIS FILE.

    Self-exclusion is not cosmetic. This script's own source contains the literals
    `params/core.md`, `MU_PER_DIE` and `## Status:` as the patterns it searches for, and it lives
    under `audit/`, so without this filter it counted itself as a citing module, a constant
    hardcoding and a probe script — inflating three published figures by one each. Caught on the
    re-run after PR #302 merged, when the counts moved and the merge could not explain all of it.
    """
    out = subprocess.run(['git', 'ls-files', *patterns], cwd=REPO,
                         capture_output=True, text=True).stdout.split()
    return [p for p in out if not p.startswith('deprecated/') and p != SELF]


def read(rel):
    try:
        with open(os.path.join(REPO, rel), encoding='utf-8', errors='ignore') as fh:
            return fh.read()
    except OSError:
        return ''


# ── the tooling population (§1) ───────────────────────────────────────────────
POPULATION = ('tools/*.py', 'tools/**/*.py', 'skills/**/*.py')

SHARED_LIBS = {
    'ci_common': r'(?:import|from)\s+ci_common\b',
    'obs_core':  r'\bobs_core\b',
    'names':     r'(?:from\s+names\s+import|import\s+names\b)',
    'registry':  r'(?:from\s+registry\s+import|import\s+registry\b)',
    'pathres':   r'\bpathres\b',
}

PRIMITIVES = {
    'repo-root / path anchoring': r'Path\(__file__\)\.resolve\(\)\.parents?\[|os\.path\.dirname\(os\.path\.dirname|ROOT\s*=\s*Path\(__file__\)',
    'YAML register load':         r'yaml\.safe_load',
    'staged/changed-file listing': r'diff\s+--cached|--name-only|git\s+diff',
    '`## Status:` parsing':       r'##\s*Status',
    'the 9-lane roster':          r"['\"]MB['\"]\s*,\s*['\"]PC['\"]|LANES\s*=|lane_codes",
    'restructure_ledger parsing': r'restructure_ledger',
    'editorial-ledger read':      r'editorial_ledger[\w_]*\.jsonl',
    'id_reservations read':       r'id_reservations',
    'token estimation (len//4)':  r'len\([^)]*\)\s*//\s*4|def tokens',
    'PP-NNN / ED-NNN regex':      r'PP-\\d|ED-\\d|ED-\[A-Z\]',
}

# The five live `## Status:` readers, transcribed from their sources (§1.3a). Each comment is the
# owning module; the divergence between them is the finding, so they are quoted, not normalised.
STATUS_READERS = {
    'dashboard_data          (^#{1,3}\\s*Status:)':        re.compile(r'^#{1,3}\s*Status:', re.M),
    'build_identifier_census (^##\\s*Status:)':            re.compile(r'^##\s*Status:', re.M),
    'ci_generation_consistency (#{0,3}\\s*Status\\s*:)':   re.compile(r'^\s*#{0,3}\s*Status\s*:', re.M | re.I),
    'obs_core.STATUS_RE      (^#{0,3}\\s*Status\\s*:)':    re.compile(r'^#{0,3}\s*Status\s*:\s*(.+)$', re.M | re.I),
    'build_incompleteness    (#{0,4}\\s*Status\\s*:)':     re.compile(r'^\s*#{0,4}\s*Status\s*:', re.M | re.I),
}


def section(title):
    print('\n' + '=' * 78)
    print(title)
    print('=' * 78)


def main():
    mods = [f for f in git_ls(*POPULATION) if f.endswith('.py')]
    src = {f: read(f) for f in mods}
    fail = []

    section(f'1.1  shared-library adoption  (population: {len(src)} modules)')
    for name, pat in SHARED_LIBS.items():
        rx = re.compile(pat)
        hits = [f for f, t in src.items()
                if rx.search(t) and os.path.basename(f)[:-3] != name]
        print(f'  {name:12s} imported by {len(hits):3d} / {len(src)}')

    section('1.2  primitive re-implementation')
    for name, pat in PRIMITIVES.items():
        rx = re.compile(pat)
        print(f'  {name:32s} {sum(1 for t in src.values() if rx.search(t)):4d}')

    section('1.3a  do the `## Status:` readers agree?')
    docs = [f for f in git_ls('*.md')]
    seen = {name: set() for name in STATUS_READERS}
    for f in docs:
        t = read(f)
        for name, rx in STATUS_READERS.items():
            if rx.search(t):
                seen[name].add(f)
    for name in STATUS_READERS:
        print(f'  {len(seen[name]):5d}  {name}')
    union = set().union(*seen.values())
    inter = set.intersection(*seen.values())
    disputed = sorted(union - inter)
    print(f'\n  {len(docs)} tracked .md scanned · union {len(union)} · agreed {len(inter)} '
          f'· DISPUTED {len(disputed)}')
    for f in disputed:
        missing = [n.split()[0] for n in STATUS_READERS if f not in seen[n]]
        print(f'     {f}\n         invisible to: {", ".join(missing)}')
    if not disputed:
        fail.append('the Status readers now agree — §1.3(a) is void and must be withdrawn')

    section('1.3b  repo-root spellings')
    idioms = {}
    for f, t in src.items():
        for m in re.finditer(r'^\s*(?:_?REPO\w*|ROOT|HERE|_HERE)\s*=\s*(.+)$', t, re.M):
            idioms.setdefault(m.group(1).strip()[:70], []).append(f)
    for k, v in sorted(idioms.items(), key=lambda x: -len(x[1]))[:8]:
        print(f'  {len(v):3d}  {k}')
    print(f'  distinct spellings: {len(idioms)}')

    section('2  provenance citations to an evacuated path')
    cites = [f for f in git_ls('*.py') if 'params/core.md' in read(f)]
    n = sum(len(re.findall(r'params/core\.md', read(f))) for f in cites)
    print(f'  `params/core.md` cited {n} time(s) across {len(cites)} live .py file(s)')
    for rel in ('params/core.md', 'engine/params/core.md'):
        print(f'    {rel:28s} exists: {os.path.exists(os.path.join(REPO, rel))}')
    cap = read('engine/engine_params/params_tables.yaml')
    key = 'engine/params/bg/core.md:' in cap
    print(f'    remedy in tree — params_tables.yaml keyed by original path: {key}')
    if not key:
        fail.append('params_tables.yaml no longer carries the original-path key — §2 remedy is wrong')

    section('3  syntax-gate coverage')
    wf = read('.github/workflows/valoria-ci.yml')
    listed = {m for m in re.findall(r'^\s+(tools/[\w/]+\.py)\s*\\?$', wf, re.M)}
    have = set(git_ls('tools/*.py', 'tools/**/*.py'))
    print(f'  tools/*.py tracked: {len(have)} · named in the syntax-check list: {len(listed)} '
          f'· UNCOVERED: {len(have - listed)}')

    section('4  are the audit probe scripts still runnable?')
    probes = [f for f in git_ls('audit/**/*.py')]
    broken = []
    for f in probes:
        t, d = read(f), os.path.dirname(f)
        for m in re.finditer(
                r"os\.path\.join\(\s*(?:_HERE|os\.path\.dirname\(\s*(?:os\.path\.abspath\()?__file__\)?\s*\))"
                r"\s*,\s*((?:'[^']*'|\"[^\"]*\")(?:\s*,\s*(?:'[^']*'|\"[^\"]*\"))*)\s*\)", t):
            parts = [p.strip().strip('\'"') for p in m.group(1).split(',')]
            if not os.path.exists(os.path.join(REPO, os.path.normpath(os.path.join(d, *parts)))):
                broken.append(f)
                break
    print(f'  {len(probes)} probe script(s) · anchors resolve: {len(probes) - len(broken)} '
          f'· BROKEN: {len(broken)}')
    for f in broken:
        print(f'     {f}')

    section('5  the forked resolution core')
    forked = [f for f in git_ls('*.py') if 'MU_PER_DIE' in read(f)]
    print(f'  MU_PER_DIE hardcoded in {len(forked)} file(s):')
    for f in forked:
        vals = re.findall(r'MU_PER_DIE\s*=\s*([\d.]+)|SD_PER_DIE\s*=\s*([\d.]+)', read(f))
        flat = [v for pair in vals for v in pair if v]
        print(f'     {f}  {flat}')

    section('6  ledger ID uniqueness  (ED-IN-0158 §8.1)')
    # Added after a live SAME-LANE double collision: this branch and PR #302 both read
    # `next_free: 156` and both allocated 156+157. Nothing in the tree catches that, so the
    # measurement behind the finding lives here — and this is the shape the guard would take.
    ids = []
    for led in git_ls('registers/editorial_ledger*.jsonl'):
        for line in read(led).splitlines():
            line = line.strip()
            if not line:
                continue
            m = re.match(r'\{"id":\s*"([^"]+)"', line)
            if m:
                ids.append(m.group(1))
    counts = {}
    for i in ids:
        counts[i] = counts.get(i, 0) + 1
    dupes = sorted((k, v) for k, v in counts.items() if v > 1)
    print(f'  {len(ids)} ledger entr(y/ies) · {len(dupes)} id(s) appearing more than once')
    for k, v in dupes:
        print(f'     {k} x{v}')
    print('  NOTE: some are deliberate progress-appends, others may be unresolved collisions.')
    print('  Nothing in the register distinguishes them — that indistinguishability is the finding.')

    # next_free must exceed every allocated id in its lane, or the counter has already been passed.
    resv = read('references/id_reservations.yaml')
    for lane in ('IN',):
        m = re.search(r'\b' + lane + r':\s*\{[^}]*next_free:\s*(\d+)', resv)
        if not m:
            continue
        nf = int(m.group(1))
        allocated = [int(i.rsplit('-', 1)[1]) for i in ids
                     if i.startswith(f'ED-{lane}-') and i.rsplit('-', 1)[1].isdigit()]
        top = max(allocated) if allocated else 0
        ok = nf > top
        print(f'  lane {lane}: next_free={nf} · highest allocated={top} · '
              f'{"OK" if ok else "PASSED — next_free is not ahead of the ledger"}')
        if not ok:
            fail.append(f'lane {lane}: next_free {nf} is not ahead of allocated max {top}')

    print('\n' + '=' * 78)
    if fail:
        print('CENSUS INVALIDATED — a claim in 00_code_leanness.md no longer reproduces:')
        for f in fail:
            print(f'  ! {f}')
        return 1
    print('census reproduced; see 00_code_leanness.md §6 for the per-claim falsifiers')
    return 0


if __name__ == '__main__':
    sys.exit(main())
