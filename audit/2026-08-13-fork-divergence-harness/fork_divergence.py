#!/usr/bin/env python3
"""Feed ONE real restructure-ledger row through every parser and record what each concludes.

WHY THIS EXISTS. `audit/2026-08-12-alias-index-consolidation/00_plan.md` rests its entire
sequencing argument on one claim: *"five parsers disagree about what its rows mean … the same row
resolves five different ways, two of them inside BLOCKING gates."* That claim was **read off the
page** — derived by reading five modules, never by running them. The plan says so itself (§6): the
first executable step should be a harness that *reproduces* the divergence, because everything else
depends on it. This is that harness.

WHAT IT IS NOT. It is not a fix, and it deliberately does not consolidate anything. Phase A2 does
that. This exists so Phase A starts from a measurement instead of a reading.

THE CONTROL IS THE POINT, AND THE PLAN DOES NOT HAVE ONE. Asking "do the consumers disagree about a
FORK row?" is the easy half. The question that matters is the one `tests/valoria/test_forked_status.py`
was written to defend:

    a path that left deliberately (FORK row) must not look like a path that never existed (no row).

So every probe below runs against BOTH — a real FORK row and a fabricated path with no row at all.
A consumer that returns the same verdict for both has collapsed the repo's anti-fabrication
property, and no amount of disagreement-about-FORK analysis surfaces that. Measured: **four of six
consumers collapse it.** The plan asserts "three of five" from reading; the difference is what a
control buys.

HOW EACH CONSUMER IS INVOKED — the real code path, never a re-implementation. Re-deriving a
consumer's semantics here would measure this file's model of it, which is the defect class §0.1
point 2 names and which this harness would otherwise be a fresh instance of.

⚠ ONE MODELLING TRAP, HIT ON THE FIRST RUN AND RECORDED SO THE NEXT READER DOES NOT REPEAT IT.
`broken_dependency_checker._resolve_remap()` is NOT the decision. It returns a mapped path; the
caller (`:217-227`) then tests membership in `all_files` and only THEN chooses INFO vs broken. A
first version of this harness modelled the helper alone and reported `params/core.md` as "mapped",
contradicting the plan — the plan was right and the instrument was wrong. Model the decision, not
the helper.

    python3 audit/2026-08-13-fork-divergence-harness/fork_divergence.py
    python3 audit/2026-08-13-fork-divergence-harness/fork_divergence.py --check
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(REPO, 'tools'))
sys.path.insert(0, os.path.join(REPO, 'skills', 'valoria-vector-audit', 'scripts'))

# A path with NO ledger row. Everything hinges on telling this apart from a FORK row.
CONTROL = 'totally/made/up/never/existed.md'

# Real rows, chosen to exercise the three shapes the plan names.
PROBES = [
    ('engine/params/core.md', 'FORK via dir-prefix row, 1 hop'),
    ('params/core.md', 'FORK via CHAINED rows, 2 hops (params/ -> engine/params/ -> FORK)'),
    ('references/values_master.yaml', 'FORK via EXACT row, 1 hop'),
    (CONTROL, 'CONTROL — no row at all; must NOT look like the rows above'),
]

# (consumer, query) pairs where the consumer's verdict DIFFERS from its own control verdict —
# i.e. where forked-vs-fabricated actually survives. MEASURED 2026-08-13.
#
# PER-PAIR, NOT PER-CONSUMER, AND THAT DISTINCTION IS ITSELF A FINDING. The first version of this
# baseline was a set of consumer names, on the assumption that a consumer either understands FORK
# or does not. `broken_dependency_checker` refuted it: it returns INFO-EVACUATED for a 1-hop FORK
# row (distinguished) and BROKEN for a 2-hop chain (identical to a fabricated path). Its
# anti-fabrication property is CONDITIONAL ON HOP COUNT. A per-consumer roster cannot express
# that, and would have recorded bdc as either wholly safe or wholly broken — both false.
#
# The ratchet may only GROW. A pair leaving this set is an anti-fabrication regression.
DISTINGUISHING_BASELINE = frozenset({
    ('pathres', 'engine/params/core.md'),
    ('pathres', 'params/core.md'),
    ('pathres', 'references/values_master.yaml'),
    ('broken_dependency_checker', 'engine/params/core.md'),
    ('broken_dependency_checker', 'references/values_master.yaml'),
    # ('broken_dependency_checker', 'params/core.md') is ABSENT ON PURPOSE — see above. Adding it
    # is the fix; asserting it today would be asserting something untrue.
})


def _all_files() -> set[str]:
    out = set()
    for dirpath, dirnames, filenames in os.walk(REPO):
        dirnames[:] = [d for d in dirnames if d not in ('.git', '__pycache__', 'node_modules')]
        for fn in filenames:
            out.add(os.path.relpath(os.path.join(dirpath, fn), REPO))
    return out


def probe_all(queries: list[str]) -> dict[str, dict[str, str]]:
    """{query: {consumer: verdict}} — each via the consumer's own code."""
    files = _all_files()
    verdicts: dict[str, dict[str, str]] = {q: {} for q in queries}

    import pathres
    for q in queries:
        r = pathres.resolve(q)
        verdicts[q]['pathres'] = r.status

    import broken_dependency_checker as bdc
    remap = bdc._load_restructure_map()
    for q in queries:
        # The DECISION, transcribed from bdc:217-227 — not `_resolve_remap` alone. See the
        # modelling trap in the module docstring.
        new_home = bdc._resolve_remap(q, remap)
        if bdc._is_forked(new_home):
            verdicts[q]['broken_dependency_checker'] = 'INFO-EVACUATED'
        elif new_home and new_home in files:
            verdicts[q]['broken_dependency_checker'] = 'INFO-MAPPED'
        else:
            verdicts[q]['broken_dependency_checker'] = 'BROKEN'

    import ci_claude_workflow_paths as cicwp
    exact, prefix = cicwp.load_alias_map()
    for q in queries:
        verdicts[q]['ci_claude_workflow_paths'] = 'ALIASED' if cicwp.resolve(q, exact, prefix) else 'DEAD'

    import vector_audit as va
    va_remap = va._restructure_remap(Path(REPO))
    for q in queries:
        verdicts[q]['vector_audit'] = 'live' if va._resolve_live(Path(REPO), q, va_remap) else 'missing'

    import workbench as wb
    wb_remap = wb._restructure_remap(REPO)
    for q in queries:
        nh = bdc._resolve_remap(q, wb_remap)
        ok = bool(nh) and os.path.isfile(os.path.join(REPO, nh))
        verdicts[q]['workbench'] = 'remapped' if ok else 'missing'

    # gen_audit (:375-386): exact-row, ZERO hop, membership in a FILE set.
    for q in queries:
        if q in files:
            v = 'live'
        else:
            nh = remap.get(q)
            v = 'moved' if (nh and nh in files) else 'nonexistent'
        verdicts[q]['gen_audit'] = v

    return verdicts


def distinguishing(verdicts: dict[str, dict[str, str]]) -> set[tuple[str, str]]:
    """(consumer, query) pairs where the FORK verdict differs from that consumer's control verdict."""
    pairs = set()
    for c in verdicts[CONTROL]:
        ctrl = verdicts[CONTROL][c]
        for q, _ in PROBES:
            if q != CONTROL and verdicts[q][c] != ctrl:
                pairs.add((c, q))
    return pairs


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--check', action='store_true',
                    help='exit 1 if fewer consumers distinguish forked-from-fabricated than the baseline')
    args = ap.parse_args(argv)

    queries = [q for q, _ in PROBES]
    verdicts = probe_all(queries)
    consumers = sorted(verdicts[CONTROL])

    for q, why in PROBES:
        print(f'\n=== {q}\n    ({why})')
        for c in consumers:
            print(f'    {c:28s} {verdicts[q][c]}')

    distinct_verdicts = {verdicts[PROBES[0][0]][c] for c in consumers}
    keep = distinguishing(verdicts)
    fork_rows = [q for q, _ in PROBES if q != CONTROL]
    total_pairs = len(consumers) * len(fork_rows)

    print('\n' + '=' * 78)
    print(f'One 1-hop FORK row yields {len(distinct_verdicts)} DISTINCT verdicts across '
          f'{len(consumers)} consumers: {sorted(distinct_verdicts)}')

    print(f'\nForked-vs-fabricated survives in {len(keep)} of {total_pairs} '
          f'(consumer x fork-row) pairs. Per consumer:')
    for c in consumers:
        ok = [q for q in fork_rows if (c, q) in keep]
        if not ok:
            state = 'COLLAPSED on every row'
        elif len(ok) == len(fork_rows):
            state = 'preserved on every row'
        else:
            state = f'PARTIAL — preserved on {len(ok)}/{len(fork_rows)}, collapses on ' \
                    f'{[q for q in fork_rows if q not in ok]}'
        print(f'    {c:28s} {state}')
    print('  A collapsed pair gives an evacuated path and a fabricated one the SAME answer —')
    print('  the distinction tests/valoria/test_forked_status.py exists to defend.')

    if args.check:
        lost = DISTINGUISHING_BASELINE - keep
        if lost:
            print(f'\n[fork-divergence FAIL] pair(s) STOPPED distinguishing forked from '
                  f'fabricated: {sorted(lost)}')
            print('  This is an anti-fabrication regression, not a style drift.')
            return 1
        gained = keep - DISTINGUISHING_BASELINE
        if gained:
            print(f'\n[fork-divergence] {sorted(gained)} now distinguish — progress. Add them to '
                  f'DISTINGUISHING_BASELINE in this commit so the ratchet holds.')
        print('\n[fork-divergence OK] every baseline pair still separates evacuated from fabricated.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
