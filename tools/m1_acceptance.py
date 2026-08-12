#!/usr/bin/env python3
"""m1_acceptance.py — the acceptance oracle for "one playable season" (ED-IN-0112).

WHAT THIS IS. "Fully simulatable" is the gate that must be passed before any content
port to Godot, because the Python sim is the ORACLE the port validates against and you
cannot validate against a gap (CLAUDE.md §7; ED-1050's port-never-corrects-its-oracle
rule is vacuous where the oracle does not cover the behaviour). Left as a phrase,
"fully simulatable" is unbounded and becomes the scope problem it was meant to end.
This file makes it five falsifiable rows.

WHAT IT DELIBERATELY DOES NOT DO. Four of the five rows are NOT MEASURABLE YET because
the season loop does not exist. This tool reports them as `blocked`, names the artifact
that unblocks each, and NEVER guesses a value. A gate that reports readiness it has not
measured is worse than no gate — it is the confounded-measurement failure of ED-MB-0042
rebuilt as infrastructure.

  row                     measurable today?  unblocked by
  ----------------------  -----------------  ---------------------------------------
  1 stub_invocations      no                 a headless season run
  2 determinism           no                 a headless season run (2 seeds)
  3 key_log_closure       PARTIAL            static contract check now; full at run
  4 m1_junctures          YES                the progress board
  5 invariant_violations  no                 property tests over a season run

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

BOARD = os.path.join('workplans', 'workplan_v6_progress.yaml')
CONTRACTS = os.path.join('references', 'module_contracts.yaml')


def _repo(p):
    return os.path.join(REPO_ROOT, p)


def _blocked(key, label, unblocked_by, detail=''):
    return {
        'row': key, 'label': label, 'state': 'blocked',
        'value': None, 'passes': None,
        'unblocked_by': unblocked_by, 'detail': detail,
    }


def row_stub_invocations():
    """Stub invocations on the M1 path must be 0.

    engine.substrate.stubwire.invocations is process-cumulative, so this is only
    meaningful as a delta around an actual season run. Importing the module and
    reading the counter at rest would report 0 and mean nothing — a false green.
    """
    return _blocked(
        'stub_invocations',
        'Stub invocations on the M1 path == 0',
        'a headless season run wrapped in stubwire.reset_invocations()',
        'stubwire.invocations is process-cumulative; a static read is not a measurement',
    )


def row_determinism():
    return _blocked(
        'determinism',
        'Same seed -> same KeyLog.content_hash()',
        'a headless season run executed twice under one seed',
        'KeyLog.content_hash() exists (engine/substrate/keys.py); it needs a run to hash',
    )


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

    return {
        'row': 'm1_junctures',
        'label': 'All M1 junctures execute',
        'state': 'measured',
        'value': done,
        'total': total,
        'passes': done == total,
        'unblocked_by': None,
        'detail': ' · '.join(f'{k}: {v}' for k, v in sorted(states.items())),
    }


def row_invariant_violations():
    return _blocked(
        'invariant_violations',
        'N seeds, zero invariant violations',
        'property-based tests (Hypothesis) over a season run',
        'properties can be authored against individual engines TODAY, ahead of the loop',
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
        'note': ('Four of five rows require a headless season run that does not exist yet. '
                 'This gate reports what it measured and never guesses the rest.'),
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
    lines += ['', f"  verdict: {result['verdict']}",
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
