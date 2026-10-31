"""Proposal 1, claim (d): the `void` appeal disposal, tried on the REAL code in a SCRATCH git worktree (never the main tree).
  python proposals/2026-10-29-parliament-and-debate/stress_p1_void.py --wt <worktree> --log OUT.jsonl
Applies in the worktree ONLY what P1 section 5 lists: `void` added to `_DISPOSES_LITERALS` (data/arrangements.py:68) and an appeal row with
`disposes: void`. Then it asks the real loader, the real `open_case`/`determine`/`pardon` acts (test_u7_remit helpers) what happens.
Each step logs a line; the worktree's edits are logged verbatim so the attempt is reproducible. The parent applies the edits and re-runs
itself as a child process (`--child`) so the interpreter loads the edited worktree fresh."""
import argparse, datetime, json, os, subprocess, sys, traceback

ap = argparse.ArgumentParser()
ap.add_argument('--wt', required=True)
ap.add_argument('--log', required=True)
ap.add_argument('--child', action='store_true')
a = ap.parse_args()
WT = os.path.abspath(a.wt)
LOG = os.path.abspath(a.log)               # absolute: the child runs with cwd = the worktree
f = open(LOG, 'a', encoding='utf-8', buffering=1)


def W(kind, **kw):
    f.write(json.dumps({'t': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'), 'kind': kind, **kw}, default=str) + '\n')
    f.flush(); os.fsync(f.fileno())


if not a.child:
    head = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=WT, capture_output=True, text=True).stdout.strip()
    W('manifest', label='void-attempt-3', argv=sys.argv, worktree=WT, wt_head=head, python=sys.version.split()[0], pythonhashseed=os.environ.get('PYTHONHASHSEED'))
    W('plan', what='P1 3.6: appeal_basis becomes an authority; the appeal row `disposes: void` closes the lower edge when it finds for the appellant. Try it on the real code.')
    W('claim', where='P1 3.6 / 5 Changes', text="`void` added to `_DISPOSES_LITERALS`, `:68`; the appeal row's `disposes: void` closes the lower edge when it finds for the appellant")
    p = os.path.join(WT, 'engine/season/data/arrangements.py')
    s = open(p, encoding='utf-8').read()
    s2 = s.replace('_DISPOSES_LITERALS = frozenset({"Record", "none"})', '_DISPOSES_LITERALS = frozenset({"Record", "none", "void"})')
    W('result', step='edit_literals', changed=(s != s2), file='engine/season/data/arrangements.py', line_pattern='_DISPOSES_LITERALS')
    open(p, 'w', encoding='utf-8').write(s2)
    p2 = os.path.join(WT, 'engine/season/arrangements.yaml')
    y = open(p2, encoding='utf-8').read()
    row = ("\n  - id:               appeal_to_crown\n    disposal:          bench\n    bench_basis:        determine\n    floor:              closed\n    records_dissent:    false\n"
           "    venue_min_rank:     settlement\n    term_required:      false\n    appeal_basis:       none\n    interposed:         [office, procedure, document]\n    order:              scripted\n"
           "    proofs:             [testimony, record]\n    disposes:           void\n    disposal_reach:      body\n")
    if 'appeal_to_crown' not in y:
        open(p2, 'w', encoding='utf-8').write(y.rstrip('\n') + '\n' + row)
    W('result', step='edit_yaml', appended_row=row)
    env = {**os.environ, 'PYTHONPATH': WT, 'PYTHONHASHSEED': '0'}
    r = subprocess.run([sys.executable, os.path.abspath(__file__), '--wt', WT, '--log', LOG, '--child'], cwd=WT, env=env, capture_output=True, text=True, timeout=600)
    W('result', step='child_exit', rc=r.returncode, stderr_tail=r.stderr.strip().splitlines()[-6:])
    W('summary', stop='child finished')
    sys.exit(0)

# ---- child: runs inside the worktree ----
sys.path.insert(0, WT)
os.chdir(WT)
try:
    from engine.season.data import arrangements as AR
    W('result', step='loader', loaded=True, n_rows=len(AR.ARRANGEMENTS), has_appeal_row='appeal_to_crown' in AR.ARRANGEMENTS,
      note='the real loader accepts `disposes: void` once the literal is added')
except BaseException as e:
    W('error', step='loader', traceback=traceback.format_exc())
    W('fail', what='loader refuses the void row after the one edit P1 lists', observed=str(e)[:300])
    sys.exit(0)
try:
    from engine.season.tests import test_u7_remit as U
    from engine.season.state import gate as G
    from engine.season.queries import world_q as wq
    from engine.season.state.carriers import Office, Tenure
    # (1) can the matter be docketed under the void row?
    w, d = U._world(**U.JUDGE)
    out = U._fold(w, d, U._act('oc', 'open_case', subject=U.PARTY, arrangement='appeal_to_crown'))
    k = U._kinds(out)
    W('trial', step='open_case_under_void_row', n=1, kinds=k, docketed=len(wq.docketed(w, U.PARTY)), void_in_DISPOSABLE_KINDS=('void' in G.DISPOSABLE_KINDS))
    if 'case.opened' not in k:
        W('fail', what="`open_case` declines a docket item naming the void row: `ARRANGEMENTS[row]['disposes'] in DISPOSABLE_KINDS` (effects_information.py:362-363) and `void` is not a disposable kind; P1 section 5's change list does not touch `DISPOSABLE_KINDS`, `open_case` or `_eff_determine`",
          proposal_said='P1 3.6 / 5: only `_DISPOSES_LITERALS` gains `void`', observed=k, where='engine/season/loop/effects_information.py:362-363; engine/season/state/gate.py DISPOSABLE_KINDS')
    # (2) control: a row that disposes a real kind does dock
    w, d = U._world(**U.JUDGE)
    k2 = U._kinds(U._fold(w, d, U._act('oc', 'open_case', subject=U.PARTY, arrangement='tribunal')))
    W('trial', step='open_case_control_tribunal', n=1, kinds=k2)
    # (3) hand-plant the item (as the tests do) and determine: what does _eff_determine do with void?
    w, d = U._world(**U.JUDGE)
    w.docket.append({'date': None, 'matter': U.PARTY, 'arrangement': 'appeal_to_crown', 'petition': None})
    k3 = U._kinds(U._fold(w, d, U._determine('dd')))
    W('trial', step='determine_hand_planted_void_item', n=1, kinds=k3, edges=[(t.kind, t.subject, t.object) for t in w.tenures if t.kind in ('oblige', 'detain', 'ban')])
    if 'matter.determined' not in k3:
        W('fail', what='`determine` on a hand-planted void item opens nothing and closes nothing (the real `_disposal` has no void site); the lower edge is untouched',
          observed=k3, where='engine/season/loop/effects_information.py::_eff_determine/_disposal')
    # (4) the closure basis: a lower bench's edge, then a SECOND seat tries to close it (pardon is the real closer)
    w, d = U._world(**U.JUDGE)
    w.offices['off_court'] = Office('off_court', 'Judge', 'R', ['determine', 'issue'], faction='Crown')
    w.add_tenure(Tenure('t_court', 'p_king', 'off_court', 'hold', since=0))
    w.docket.append({'date': None, 'matter': U.PARTY, 'arrangement': 'tribunal', 'petition': None})
    k4 = U._kinds(U._fold(w, d, U._determine('dd')))
    lower = [(t.kind, t.subject, t.object, t.live) for t in w.tenures if t.kind in ('detain', 'oblige', 'ban')]
    W('trial', step='lower_bench_disposal', n=1, kinds=k4, edges=lower)
    ok = any(e[0] in ('detain', 'ban') for e in lower)
    if not ok:
        W('unverified', step='closure_basis', what='the lower bench opened no restraint on this draw; the closure test below is vacuous', observed=k4)
    act = U._act('pd', 'pardon', via='off_court', actor='p_king', subject=U.PARTY)
    k5 = U._kinds(U._fold(w, d, act))
    after = [(t.kind, t.subject, t.object, t.live) for t in w.tenures if t.kind in ('detain', 'oblige', 'ban')]
    W('trial', step='appeal_seat_pardon', n=1, kinds=k5, edges_after=after)
    still_live = any(e[3] for e in after if e[0] in ('detain', 'ban'))
    if ok and still_live:
        W('fail', what="a second seat (the appeal bench) cannot close the lower bench's restraint: `pardon` closes only edges whose OBJECT is the exercised seat (effects_governance.py:335-338,348); the lower edge's object is the lower seat",
          proposal_said="P1 3.6: the appeal row's `disposes: void` closes the lower edge when it finds for the appellant", observed=k5, where='engine/season/loop/effects_governance.py:335-349')
    # (5) control for (4): the lower seat's own pardon closes it
    if ok:
        w2, d2 = U._world(**U.JUDGE)
        w2.docket.append({'date': None, 'matter': U.PARTY, 'arrangement': 'tribunal', 'petition': None})
        U._fold(w2, d2, U._determine('dd'))
        k6 = U._kinds(U._fold(w2, d2, U._act('pd', 'pardon', via=U.SEAT, actor=U.DUKE, subject=U.PARTY)))
        a6 = [(t.kind, t.live) for t in w2.tenures if t.kind in ('detain', 'ban')]
        W('trial', step='lower_seat_pardon_control', n=1, kinds=k6, edges_after=a6)
except BaseException:
    W('error', step='child', traceback=traceback.format_exc())
