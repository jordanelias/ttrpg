#!/usr/bin/env python3
"""m1_acceptance.py — the acceptance oracle for "one playable season" (ED-IN-0112).

WHAT THIS IS. "Fully simulatable" is the gate that must be passed before any content
port to Godot, because the Python sim is the ORACLE the port validates against and you
cannot validate against a gap (CLAUDE.md §7; ED-1050's port-never-corrects-its-oracle
rule is vacuous where the oracle does not cover the behaviour). Left as a phrase,
"fully simulatable" is unbounded and becomes the scope problem it was meant to end.
This file makes it five falsifiable rows.

WHAT CHANGED (S2, workplans/return_to_game_queue.yaml, ED-IN-0112). The "headless season run
that does not exist" this file used to name as the blocker for rows 1-2 DOES exist —
engine.mc_v18.run_campaign already runs 50-season campaigns in ~2.5s with a deterministic
KeyLog hash. Rows 1 and 2 were blocked only because nothing pointed this oracle at it; they
are now MEASURED from a real headless 1-season probe run (`_run_probe_season` below). Row 5
still needs the full season loop wired through invariant assertions — not attempted here —
but a first, narrower slice of its "properties over individual engines TODAY, ahead of the
loop" guidance is now live in tests/valoria/test_dice_engine_properties.py (dice_engine.py's
Pool Minimum / Die Rule bounds and the degree-ladder margin formula), independent of this
row's own `state` (still `blocked`, honestly — that file does not touch a season KeyLog).
A gate that reports readiness it has not measured is worse than no gate — it is the
confounded-measurement failure of ED-MB-0042 rebuilt as infrastructure, so every MEASURED
row below reports its real value, pass or fail, never a guess (CLAUDE.md §0.1 point 4).

  row                     measurable today?  unblocked by
  ----------------------  -----------------  ---------------------------------------
  1 stub_invocations      YES (S2)           a headless season run
  2 determinism           YES (S2)           a headless season run (2 seeds)
  3 key_log_closure       PARTIAL            static contract check now; full at run
  4 m1_junctures          YES                the progress board
  5 invariant_violations  no                 property tests over a season run
                                              (begun at the individual-engine level — see above)

USAGE
  python3 tools/m1_acceptance.py --summary
  python3 tools/m1_acceptance.py --json      (dashboard_data.py consumes this)
  python3 tools/m1_acceptance.py --check     exit 1 only on a MEASURED failure
"""

import argparse
import json
import os
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    print("m1_acceptance: PyYAML required", file=sys.stderr)
    sys.exit(2)

# Primitives (repo root, lane roster, token estimate, ids, Status reader) are
# owned by tools/ci_common.py — plan G7, ED-IN-0159 §8.3. See its module docstring;
# the two lines below are the bootstrap, anchored on THIS file's directory.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = ci_common.REPO   # ONE OWNER (plan G7, ED-IN-0159 §8.3)

# engine.mc_v18 is the headless season run rows 1-2 need (S2). Imported defensively — never
# fatally — so a broken engine import degrades those two rows back to `blocked` with the real
# exception named, rather than crashing every other row's --summary/--json/--check output.
sys.path.insert(0, REPO_ROOT)
try:
    from engine import mc_v18 as _mc_v18
    _ENGINE_IMPORT_ERROR = None
except Exception as _exc:  # pragma: no cover - defensive; surfaced via row detail, not raised
    _mc_v18 = None
    _ENGINE_IMPORT_ERROR = _exc

BOARD = os.path.join('workplans', 'workplan_v6_progress.yaml')
CONTRACTS = os.path.join('references', 'module_contracts.yaml')

# Fixed probe seed for rows 1-2 (S2). FIXED, not time-derived: CLAUDE.md §0.1 point 4 — "a
# number without a control is not a measurement" — and the control here is that both rows read
# the SAME seed's probe run, so a --summary invocation an hour from now reproduces the same
# stub-invocation count and the same content_hash a reader can independently re-derive. Value
# is arbitrary (the queue step's authoring date, S2/ED-IN-0112); only its fixedness matters.
M1_PROBE_SEED = 20260819


def _repo(p):
    return os.path.join(REPO_ROOT, p)


def _run_probe_season(seed):
    """Run ONE headless season of engine.mc_v18 under `seed`. Single owner for rows 1-2.

    NO stubwire reset here, deliberately (S2 adjudication). The queue step and this file's
    own pre-S2 blocker text both said "a headless season run wrapped in
    stubwire.reset_invocations()"; executing it proved that wrapper INERT and wrong on two
    counts. (1) engine/mc_v18.py:222 already snapshots `_stub_start = stubwire.invocations`
    and :300 returns `stub_hits = stubwire.invocations - _stub_start` — run_campaign is the
    single owner of that delta (CLAUDE.md §8: never re-implement a rule that already lives
    once), so a leading reset cannot change the reported number. FALSIFIER, executed: with
    reset_invocations() monkeypatched to a no-op and the cumulative counter left at 6, this
    row still reported exactly 2. (2) engine/substrate/stubwire.py:70-72 declares
    reset_invocations() test-only and "never called from a production code path" — and
    tools/dashboard_data.py imports this module and calls collect() IN-PROCESS, so the reset
    made a reporting surface mutate process-global engine state for no effect.

    Caps the campaign at 1 season via CAMPAIGN_SEASONS. Note `max_seasons` alone is DEAD:
    mc_v18.py:231 reads `effective_params.get('CAMPAIGN_SEASONS', max_seasons)` and
    DEFAULT_PARAMS always supplies CAMPAIGN_SEASONS, so the params entry is what binds.
    MEASURED cost of the three campaigns collect() now runs (controlled, both arms, one
    session, 3 runs each): --summary median 0.153s pre-S2 -> 0.617s post-S2, +0.46s.
    """
    return _mc_v18.run_campaign(seed=seed, max_seasons=1, params={'CAMPAIGN_SEASONS': 1})


def _blocked(key, label, unblocked_by, detail=''):
    return {
        'row': key, 'label': label, 'state': 'blocked',
        'value': None, 'passes': None,
        'unblocked_by': unblocked_by, 'detail': detail,
    }


def row_stub_invocations():
    """Stub invocations on the M1 path must be 0.

    MEASURED (S2): a headless 1-season mc_v18 run (_run_probe_season). The value is
    CampaignResult.stub_hits, which run_campaign computes as its own before/after delta on the
    process-cumulative engine.substrate.stubwire.invocations counter — reading that counter at
    rest would report 0 and mean nothing, a false green.

    SCOPE, stated because the row label overstates it: an mc_v18 season is a PROXY for "the M1
    path", not the M1 path. Row 4 in this same report shows 0/7 M1 junctures executing, so most
    M1 stub sites are unreachable by this probe. Parked as S2-R1.
    """
    if _mc_v18 is None:
        return _blocked(
            'stub_invocations',
            'Stub invocations on the M1 path == 0',
            'a working engine.mc_v18 import',
            f'engine import failed: {type(_ENGINE_IMPORT_ERROR).__name__}: {_ENGINE_IMPORT_ERROR}',
        )
    result = _run_probe_season(M1_PROBE_SEED)
    value = result.stub_hits
    return {
        'row': 'stub_invocations',
        'label': 'Stub invocations on the M1 path == 0',
        'state': 'measured',
        'value': value,
        'passes': value == 0,
        'unblocked_by': None,
        'detail': (
            f'1-season probe (seed={M1_PROBE_SEED}): {value} stub_resolve call(s) '
            'during the run; CampaignResult.stub_hits, which run_campaign computes as its own '
            'before/after delta on the process-cumulative '
            'engine.substrate.stubwire.invocations counter).'
        ),
    }


def row_determinism():
    """Same seed -> same KeyLog.content_hash().

    MEASURED (S2): the same seed run twice, independently, and their
    engine.substrate.keys.KeyLog.content_hash() values compared. This file previously
    conceded the hash "exists ... it needs a run to hash" (row_determinism, pre-S2) — the run
    now exists (_run_probe_season).
    """
    if _mc_v18 is None:
        return _blocked(
            'determinism',
            'Same seed -> same KeyLog.content_hash()',
            'a working engine.mc_v18 import',
            f'engine import failed: {type(_ENGINE_IMPORT_ERROR).__name__}: {_ENGINE_IMPORT_ERROR}',
        )
    r1 = _run_probe_season(M1_PROBE_SEED)
    r2 = _run_probe_season(M1_PROBE_SEED)
    h1, h2 = r1.key_log_hash, r2.key_log_hash
    match = bool(h1) and h1 == h2
    return {
        'row': 'determinism',
        'label': 'Same seed -> same KeyLog.content_hash()',
        'state': 'measured',
        'value': f'{h1[:12]}…' if h1 else '(empty)',
        'passes': match,
        'unblocked_by': None,
        'detail': (
            f'two independent 1-season runs, seed={M1_PROBE_SEED}: '
            + ('hashes match' if match else 'HASHES DIVERGE OR EMPTY')
            + f' ({h1[:12] if h1 else "<empty>"}… vs {h2[:12] if h2 else "<empty>"}…, '
              f'{r1.keys_emitted}/{r2.keys_emitted} keys emitted)'
        ),
    }


def row_key_log_closure():
    """Every emitted key has a registered consumer or a declared terminal.

    PARTIAL today: module_contracts.yaml declares each module's key IN/OUT, so an
    emitted type with no declared consumer is statically visible. That is a real
    finding and worth surfacing now. It is NOT the full row — the full row is
    measured over an actual season KeyLog, where a contract-declared consumer that
    never fires is also a defect and static analysis cannot see it.
    """
    path = _repo(CONTRACTS)
    if not os.path.exists(path):
        return _blocked('key_log_closure', 'Every emitted key has a consumer or declared terminal',
                        'references/module_contracts.yaml', 'contracts file not found')
    try:
        with open(path, encoding='utf-8') as fh:
            data = yaml.safe_load(fh) or {}
    except Exception as exc:
        return _blocked('key_log_closure', 'Every emitted key has a consumer or declared terminal',
                        'a parseable module_contracts.yaml', f'{type(exc).__name__}')

    # Schema (references/module_contracts.yaml, 27 modules):
    #   emits:    [{type: <id>, terminal: <bool>}]
    #   consumes: [{type: <id>, from: [<module>, ...]}]
    # `terminal: true` IS this row's "declared terminal" — the contract already carries
    # the distinction the acceptance row asks for, so the static half is exact, not a proxy.
    modules = data.get('modules')
    if not isinstance(modules, list):
        return _blocked('key_log_closure', 'Every emitted key has a consumer or declared terminal',
                        'module_contracts.yaml with a top-level `modules` list',
                        f'unexpected shape: {type(modules).__name__}')

    emitted, terminal, consumed = set(), set(), set()
    wildcard_consumers = 0
    for spec in modules:
        if not isinstance(spec, dict):
            continue
        for e in spec.get('emits') or []:
            if isinstance(e, dict) and e.get('type'):
                emitted.add(str(e['type']))
                if e.get('terminal'):
                    terminal.add(str(e['type']))
        for c in spec.get('consumes') or []:
            if isinstance(c, dict) and c.get('type'):
                t = str(c['type'])
                # `- {type: "*", from: engine}` is a QUANTIFIER, not a key name. Two modules
                # declare it, one commented "universal reader of the full Key stream
                # (substrate §8.7)". The first version of this row put the literal "*" into
                # the consumed set and never expanded it, which is the term-vs-concept error:
                # it reported 2 orphans while the contract says every emit has a consumer.
                if t == '*':
                    wildcard_consumers += 1
                    continue
                consumed.add(t)

    strict = sorted(emitted - consumed - terminal)          # ignoring wildcards
    effective = [] if wildcard_consumers else strict         # honouring them

    # BOTH READINGS ARE REPORTED, because neither alone is honest. Honouring the wildcard
    # makes the row vacuous (always 0 while any universal reader exists); ignoring it
    # overstates. `value` is the STRICT count — the one that names something a human can
    # act on — and the detail says plainly that a universal reader exists.
    return {
        'row': 'key_log_closure',
        'label': 'Every emitted key has a consumer or declared terminal',
        'state': 'partial',
        'value': len(strict),
        'value_effective': len(effective),
        # Never True from static analysis alone: a contract-declared consumer that never
        # fires at runtime is a dead seam this pass cannot see. Only a season KeyLog can —
        # and a wildcard consumer is exactly the case where "declared" says least about
        # "fires", which is the argument for measuring this over a real KeyLog.
        'passes': None,
        'unblocked_by': 'a season KeyLog (a declared — especially wildcard — consumer may never fire)',
        'detail': (
            f"{len(emitted)} emitted · {len(terminal)} declared terminal · "
            f"{len(strict)} unconsumed by name"
            + (f" ({', '.join(strict[:3])})" if strict else '')
            + (f"; {wildcard_consumers} module(s) declare a `*` universal-reader consume, "
               f"under which the static orphan count is {len(effective)}"
               if wildcard_consumers else '')
        ),
        'note_terminal_unused': (
            'no emit in the corpus sets terminal: true, so the "or declared terminal" '
            'branch has never been exercised' if not terminal else ''
        ),
    }


def row_m1_junctures():
    """All seven M1 junctures execute. Measurable today from the progress board."""
    path = _repo(BOARD)
    try:
        data = ci_common.load_yaml(path)
        junctures = data['milestones']['M1']['junctures']
    except Exception as exc:
        return _blocked('m1_junctures', 'All seven M1 junctures execute',
                        'a readable workplan progress board', f'{type(exc).__name__}')

    done = sum(1 for j in junctures if j.get('state') == 'done')
    total = len(junctures)
    states = {}
    for j in junctures:
        states[j.get('state', '?')] = states.get(j.get('state', '?'), 0) + 1

    # ⚠ THIS ROW IS DOC-DERIVED, AND SAYS SO. Labelled 2026-08-19 after two independent read-only
    # audits found the same hole: CLAUDE.md §0.2 names this tool THE instrument of "done means it
    # runs" and asserts a juncture may not be marked done on a document — but this row counts
    # `state: done` strings in a hand-edited YAML board. Seven one-word edits green it, and the
    # ratchet in review_core would bank that as real improvement.
    #
    # NOT SILENTLY FIXED, because the honest fix is not available yet: closing it requires a
    # per-juncture EXECUTION artifact to check `state: done` against, and no such artifact exists
    # for any of the seven. Inventing a schema here would be scripting drift. So the row keeps
    # measuring what it can measure and DECLARES its own weakness in the output, where a reader
    # deciding whether to trust the verdict will actually see it. Rows 1-2 are execution-derived
    # (real seeded mc_v18 probe runs); this one is not, and the two must not read alike.
    return {
        'row': 'm1_junctures',
        'label': 'All M1 junctures execute',
        'state': 'measured',
        'derived_from': 'document',
        'value': done,
        'total': total,
        'passes': done == total,
        'unblocked_by': None,
        'detail': (' · '.join(f'{k}: {v}' for k, v in sorted(states.items()))
                   + '  ⚠ DOC-DERIVED: counts `state: done` in workplan_v6_progress.yaml, not'
                     ' execution. Editing the board greens this row — unlike rows 1-2.'),
    }


def row_invariant_violations():
    """N seeds, zero invariant violations — over a season run. Still `blocked` (S2 did not
    wire this): the season-loop invariant sweep this row measures is a materially larger
    lift than rows 1-2 (a per-season assertion battery, not a single probe run + hash
    compare). A first, narrower step toward it now exists at the individual-engine level —
    tests/valoria/test_dice_engine_properties.py, seeded property sweeps over
    engine/autoload/dice_engine.py's Pool Minimum / Die Rule bounds and degree ladder — per
    this row's own guidance below, "ahead of the loop". That file does not touch a season
    KeyLog, so it cannot make this row `measured`; it is the beginning this row named, not
    its completion.
    """
    return _blocked(
        'invariant_violations',
        'N seeds, zero invariant violations',
        'property-based tests (Hypothesis) over a season run',
        'properties can be authored against individual engines TODAY, ahead of the loop '
        '(begun: tests/valoria/test_dice_engine_properties.py)',
    )


ROWS = [
    row_stub_invocations,
    row_determinism,
    row_key_log_closure,
    row_m1_junctures,
    row_invariant_violations,
]


def collect():
    rows = [fn() for fn in ROWS]
    measured = [r for r in rows if r['state'] == 'measured']
    failed = [r for r in measured if r['passes'] is False]
    blocked = [r for r in rows if r['state'] in ('blocked', 'partial')]

    if failed:
        verdict = 'NOT MET'
    elif blocked:
        verdict = 'NOT YET MEASURABLE'
    else:
        verdict = 'MET'

    return {
        'available': True,
        'gate': 'fully simulatable season',
        'verdict': verdict,
        'rows': rows,
        'measured': len(measured),
        'blocked': len(blocked),
        'failed': len(failed),
        'note': ('Rows 1-2 now measured from a real headless probe season (S2). Row 3 stays '
                 'PARTIAL (static contract check only) and row 5 stays blocked (needs a '
                 'season-run invariant sweep, not yet wired). This gate reports what it '
                 'measured and never guesses the rest.'),
    }


def _fmt(result):
    lines = [f"M1 acceptance gate — {result['gate']}", '']
    glyph = {'measured': '●', 'partial': '◐', 'blocked': '○'}
    for r in result['rows']:
        g = glyph.get(r['state'], '?')
        if r['state'] == 'measured':
            val = f"{r['value']}/{r.get('total')}" if 'total' in r else str(r['value'])
            mark = 'PASS' if r['passes'] else 'FAIL'
            lines.append(f"  {g} {r['label']:<48} {val:>8}  {mark}")
        else:
            lines.append(f"  {g} {r['label']:<48} {'—':>8}  {r['state'].upper()}")
        if r.get('detail'):
            lines.append(f"      {r['detail']}")
        if r.get('unblocked_by'):
            lines.append(f"      unblocked by: {r['unblocked_by']}")
    # Machine-readable failure count. `failed` was already computed and only ever reached the
    # --json path, so no gate could read this tool's verdict — which is why the game's acceptance
    # state was absent from every Stop-hook and CI signal (T2, CLAUDE.md §0.3). review_core.py's
    # `m1.acceptance` row parses this line. Printing an existing number, not measuring a new one.
    lines += ['', f"  verdict: {result['verdict']}",
              f"  {result['failed']} row(s) failing",
              '', '  ' + result['note']]
    return '\n'.join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--json', action='store_true')
    ap.add_argument('--summary', action='store_true')
    ap.add_argument('--check', action='store_true',
                    help='exit 1 only on a MEASURED failure; blocked rows never fail the gate')
    args = ap.parse_args(argv)

    result = collect()
    print(json.dumps(result, indent=2) if args.json else _fmt(result))

    if args.check and result['failed']:
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
