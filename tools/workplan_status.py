#!/usr/bin/env python3
"""
workplan_status.py — print the workplan v6 position from the progress board.

One rule, one home (CLAUDE.md §8): this is the ONLY renderer of
workplans/workplan_v6_progress.yaml. Consumers: the SessionStart banner
(tools/session_status.py, one-line mode) and the valoria-workplan-navigator skill
(--full mode: the ASCII progress diagram + per-row detail).

Modes:
  (none)   one-line position summary
  --full   ASCII progress diagram + per-juncture/stage detail + T0 decisions
  --check  staleness check only (as_of.sha vs HEAD); ALWAYS exits 0

Defensive by contract: never raises, never exits non-zero — a broken/missing board
degrades to one explanatory line (this runs inside the SessionStart hook).
ED-IN-0010.
"""
import os
import subprocess
import sys

BOARD = os.path.join('workplans', 'workplan_v6_progress.yaml')

GLYPH = {
    'done': '■',          # ■
    'in_progress': '◐',   # ◐
    'blocked': '⊘',       # ⊘
    'not_started': '▢',   # ▢
}


def _load():
    try:
        import yaml
        with open(BOARD, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        if not isinstance(data, dict) or 'milestones' not in data:
            return None
        return data
    except Exception:
        return None


def _rows(ms):
    return ms.get('junctures') or ms.get('stages') or []


def _counts(rows):
    c = {'done': 0, 'in_progress': 0, 'blocked': 0, 'not_started': 0}
    for r in rows:
        c[r.get('state') if r.get('state') in c else 'not_started'] += 1
    return c


def _bar(rows):
    return '[' + ''.join(GLYPH.get(r.get('state'), GLYPH['not_started']) for r in rows) + ']'


def _next_ready(board):
    """First ready-now increment: not_started/in_progress with no gate, M1 first."""
    for mkey in ('M1', 'M2', 'M3'):
        ms = board.get('milestones', {}).get(mkey) or {}
        for r in _rows(ms):
            if r.get('state') in ('in_progress', 'not_started') and not r.get('blocked_on'):
                nxt = (r.get('next') or r.get('label') or '').split(';')[0].strip()
                return f"{mkey} {r.get('label', '?')}: {nxt}"
    return 'no ungated increment — rule a T0 decision'


RELEVANT_PREFIXES = ('designs/', 'registers/handoffs/', 'canon/', 'sim/')


def staleness():
    """Warn when workplan-relevant paths changed since the board was last touched.

    The freshness base is the board's own last-touch commit in git (self-maintaining:
    committing a board refresh makes it fresh by definition); the YAML `as_of` is the
    human-facing record. Uncommitted board edits (a refresh in progress) count as fresh.
    """
    board = _load()
    if not board:
        return (f"⚠ workplan board missing/unreadable ({BOARD}) — "
                "run the workplan navigator to regenerate")
    d = subprocess.run(['git', 'status', '--porcelain', '--', BOARD],
                       capture_output=True, text=True)
    if d.returncode == 0 and d.stdout.strip():
        return ''  # board is being refreshed right now
    base = subprocess.run(['git', 'log', '-1', '--format=%H', '--', BOARD],
                          capture_output=True, text=True)
    base_sha = base.stdout.strip() if base.returncode == 0 else ''
    if not base_sha:
        return ''  # board not in history yet (first commit pending)
    r = subprocess.run(['git', 'log', '--name-only', '--pretty=format:',
                        f'{base_sha}..HEAD'], capture_output=True, text=True)
    if r.returncode != 0:
        return f"⚠ workplan board freshness unknown — refresh {BOARD}"
    touched = {ln.strip() for ln in r.stdout.splitlines() if ln.strip()}
    relevant = sorted(p for p in touched
                      if p.startswith(RELEVANT_PREFIXES) and p != BOARD)
    if relevant:
        return (f"⚠ {len(relevant)} workplan-relevant file(s) changed since the board's "
                f"last refresh (as_of {(board.get('as_of') or {}).get('sha', '?')}) — "
                "the navigator skill refreshes it on use")
    return ''


def summary_line():
    board = _load()
    if not board:
        return f"workplan: (no readable board at {BOARD} — run the workplan navigator to regenerate)"
    m1 = board.get('milestones', {}).get('M1') or {}
    rows = _rows(m1)
    c = _counts(rows)
    t0 = len(board.get('decisions_t0_open') or [])
    nxt = _next_ready(board)
    if len(nxt) > 90:
        nxt = nxt[:87] + '...'
    return (f"workplan: M1 {c['done']}/{len(rows)} junctures done "
            f"({c['in_progress']} in progress, {c['blocked']} blocked) · "
            f"next: {nxt} · T0 open: {t0}")


def full():
    board = _load()
    if not board:
        print(summary_line())
        return
    out = ['NORTH STAR ─── M1 one playable season ──▶ '
           'M2 any-seed story ──▶ M3 godot slice']
    here_done = False
    for mkey in ('M1', 'M2', 'M3'):
        ms = board.get('milestones', {}).get(mkey) or {}
        rows = _rows(ms)
        if not rows:
            continue
        c = _counts(rows)
        tail = (f"{c['done']} done · {c['in_progress']} in progress · "
                f"{c['blocked']} blocked · {c['not_started']} open")
        here = ''
        if not here_done and c['done'] < len(rows):
            here = '   ← YOU ARE HERE'
            here_done = True
        out.append(f"{mkey:3} {_bar(rows)}  {ms.get('label', '')} — {tail}{here}")
        for r in rows:
            g = GLYPH.get(r.get('state'), GLYPH['not_started'])
            key = str(r.get('n') or r.get('key') or '?')
            gate = f"  [gate: {r['blocked_on']}]" if r.get('blocked_on') else ''
            out.append(f"     {key:>4}{g} {r.get('label', '?')}{gate}")
            if r.get('next'):
                out.append(f"          next: {r['next']}")
    t0 = board.get('decisions_t0_open') or []
    if t0:
        out.append('T0 decisions open: ' + ' · '.join(t0))
    lp = board.get('last_progress') or []
    if lp:
        out.append('recent progress:')
        out.extend(f"  - {ln}" for ln in lp[-5:])
    out.append('glyphs: ■ done  ◐ in progress  ⊘ blocked(gate)  ▢ not started'
               f"  · as_of {(board.get('as_of') or {}).get('sha', '?')}"
               f" {(board.get('as_of') or {}).get('date', '')}")
    print('\n'.join(out))


def main():
    try:
        if '--check' in sys.argv:
            w = staleness()
            print(w if w else 'workplan board: fresh '
                              '(no workplan-relevant changes since its last refresh)')
        elif '--full' in sys.argv:
            full()
            w = staleness()
            if w:
                print(w)
        else:
            print(summary_line())
            w = staleness()
            if w:
                print(w)
    except Exception as e:  # never break a hook
        print(f"workplan: (status unavailable: {e})")
    sys.exit(0)


if __name__ == '__main__':
    main()
