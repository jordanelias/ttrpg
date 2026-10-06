#!/usr/bin/env python3
"""Drive `/methodology-execute` one batch per fresh `claude -p` process, unattended.

TERMS, defined at the call site (CLAUDE.md §4):
  * **driver** — this loop. Run by a PERSON, outside any session. It arms nothing inside a session
    and so is not the self-scheduling CLAUDE.md §11 denies; it starts the next process only after
    the previous one has exited.
  * **a fresh process is the clear** — `claude -p` starts with an empty context window, which is
    the reset `skills/methodology-execute/SKILL.md` §BATCH BOUNDARY asks for. What survives a
    boundary is what is on disk: commits, the plan, the lane handoff's in-flight row. (Context is
    fresh, not state-free: CLAUDE.md and auto memory still load.)
  * **status line** — the last line each invocation prints, defined in that skill's §THE STATUS
    LINE and nowhere else; this file only reads it by that spelling.

NOT A GUARD (CLAUDE.md §0.1 pt 5). It asserts nothing about the tree and gates nothing; it runs a
skill, reads one line, and stops. It is not part of CI.

USAGE
    python tools/methodology_drive.py [--approved] [--max-batches N] [--attempts N]
        [--timeout SEC] "<free text>" [-- <extra claude args>]

  First run WITHOUT `--approved`: a free text that resolves to more than one position stops at the
  skill's approval step (`STOPPED`), prints the sequence, and exits 3. Read it, then re-run with
  `--approved` — that is the human gate; the driver never supplies it. After a first invocation
  that ran, every later one is sent as `approved: <text>`.

  Everything after `--` goes to `claude` unchanged. The permission posture is YOURS to choose;
  nothing is defaulted here. Examples (check `claude --version`; the docs gate some flags by it):
      -- --permission-mode acceptEdits --max-budget-usd 40
  `permissions.deny` in `.claude/settings.json` applies in every mode, so CLAUDE.md §11's deny list
  holds inside driven sessions. `--dangerously-skip-permissions` is refused for root outside a
  sandbox. Do NOT pass `-c`/`--resume` (that carries context across batches) or `--bare` (it skips
  skills, CLAUDE.md and hooks). Print-mode background subagents keep the process open and the wait
  ceiling is 10 minutes of idle unless `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS` is set; this driver
  sets it to `0` (no ceiling) when you have not, since a terminal critique can run longer.

EXIT: 0 COMPLETE · 3 STOPPED (a person is needed; the reason is printed) · 4 `--max-batches` hit
with batches remaining · 2 usage or environment error. `CLAUDE_BIN` names the binary (default
`claude`).
"""
import argparse
import json
import os
import re
import subprocess
import sys

from ci_common import REPO

SKILL = '.claude/skills/methodology-execute/SKILL.md'
STATUS = re.compile(r'^METHODOLOGY-EXECUTE: (COMPLETE|NEXT (\S.*)|STOPPED (\S.*))$')


def invoke(prompt, extra, timeout):
    """One fresh `claude -p`. Returns (status_or_None, session_id, cost, note)."""
    cmd = [os.environ.get('CLAUDE_BIN', 'claude'), '-p', prompt, '--output-format', 'json', *extra]
    env = dict(os.environ)
    env.setdefault('CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS', '0')
    try:
        done = subprocess.run(cmd, cwd=REPO, env=env, capture_output=True, text=True,
                              timeout=timeout or None)
    except subprocess.TimeoutExpired:
        return None, None, 0.0, 'timed out'
    try:
        out = json.loads(done.stdout)
    except ValueError:
        return None, None, 0.0, 'unparseable output (exit %s): %s' % (done.returncode, done.stdout[-200:] or done.stderr[-200:])
    cost = float(out.get('total_cost_usd') or 0.0)
    sid = out.get('session_id')
    if out.get('is_error') or out.get('subtype') != 'success':
        return None, sid, cost, 'subtype=%s is_error=%s' % (out.get('subtype'), out.get('is_error'))
    lines = [ln.strip() for ln in (out.get('result') or '').splitlines() if ln.strip()]
    hit = STATUS.match(lines[-1]) if lines else None
    return (hit, sid, cost, None) if hit else (None, sid, cost, 'no status line')


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('text')
    ap.add_argument('--approved', action='store_true')
    ap.add_argument('--max-batches', type=int, default=20)
    ap.add_argument('--attempts', type=int, default=2, help='invocations per batch before giving up')
    ap.add_argument('--timeout', type=int, default=0, help='seconds per invocation; 0 = none')
    args, extra = ap.parse_known_args(argv)
    extra = [x for x in extra if x != '--']
    if not os.path.exists(os.path.join(REPO, SKILL)):
        print('driver: %s not found; a `/name` that matches nothing is sent to the model as plain '
              'text, so refusing to start' % SKILL, file=sys.stderr)
        return 2

    total, last_next, ran = 0.0, None, False
    for batch in range(1, args.max_batches + 1):
        prompt = '/methodology-execute %s%s' % ('approved: ' if (args.approved or ran) else '', args.text)
        for attempt in range(1, args.attempts + 1):
            hit, sid, cost, note = invoke(prompt, extra, args.timeout)
            total += cost
            print('driver: batch %d attempt %d session=%s cost=$%.2f total=$%.2f %s'
                  % (batch, attempt, sid, cost, total, hit.group(0) if hit else note), flush=True)
            if hit:
                break
        else:
            print('driver: STOPPED no status line after %d attempt(s): %s' % (args.attempts, note))
            return 3
        ran = True
        if hit.group(1) == 'COMPLETE':
            print('driver: COMPLETE after %d batch(es), total=$%.2f' % (batch, total))
            return 0
        if hit.group(3):
            print('driver: STOPPED %s' % hit.group(3))
            return 3
        if hit.group(2) == last_next:
            print('driver: STOPPED no progress: NEXT %s returned twice' % last_next)
            return 3
        last_next = hit.group(2)
    print('driver: --max-batches %d reached; NEXT %s remains' % (args.max_batches, last_next))
    return 4


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
