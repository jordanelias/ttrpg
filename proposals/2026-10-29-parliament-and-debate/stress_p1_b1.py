"""Proposal 1 (one draw, one roster) stress test, S8: apply its FIRST BATCH (B1 'delete') to a SCRATCH
git worktree, run the specific test files it touches, count what breaks. Writes ONE FLUSHED JSON LINE per
event (same shape as stress_probe.py's Log). Never edits the main tree; the worktree is --wt.

  python proposals/2026-10-29-parliament-and-debate/stress_p1_b1.py --wt <worktree> --phase P0 --log OUT.jsonl
Phases (each is CUMULATIVE on the worktree state; the harness applies only the edits of its own phase):
  P0   control: no edit (HEAD)                              P1a  item 1a: `git rm` the kernel directory only
  P1b  item 1b: the proposal's repointings of the kernel's dependants (json entries, module_contracts row,
       kernel tests)                                         P1c  items 2 + 5 (cross-ledger reads, row keys)
  P1d  items 3 + 4 (discrete path, leverage=0.0, _pool_of/_opposition_of/VERB_CAPABILITY) literally
  RUN  only run the test set on the worktree as it stands (label via --phase RUN:<label>)
Stop rule: a phase ends when every file has finished or hit its per-file wall-clock timeout (--file-timeout).
"""
import argparse, concurrent.futures as cf, os, re, subprocess, sys, time, traceback
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from stress_probe import Log, git

TESTS = """engine/tests/test_contest_kernel.py
engine/tests/test_sigma_leverage_parity.py
engine/season/tests/test_season_shape.py
engine/season/tests/test_arrangements.py
engine/season/tests/test_social_contest_module.py
engine/season/tests/test_sc01_obstacle_ceiling.py
engine/season/tests/test_sc01_provider.py
engine/season/tests/test_sc01_speak.py
engine/season/tests/test_sc01_the_bar.py
engine/season/tests/test_sc02_reception.py
engine/season/tests/test_sc02_22b_consequence_and_forgery.py
engine/season/tests/test_stress_proceedings_rehost.py
engine/season/tests/test_in12_step9.py
engine/season/tests/test_u7_remit.py
engine/season/tests/test_u8_cast_fields.py
tests/valoria/test_import_cycle_game_state_npe.py
tests/valoria/test_engine_does_not_import_systems.py
tests/valoria/test_band_extension_seam.py
tests/valoria/test_tn7_always.py
tests/valoria/test_balance_oracle_arms.py
tests/valoria/test_structure_audit.py
tests/valoria/test_degree_ladder_single_owner.py
tests/valoria/test_export_sim_params.py
tests/valoria/test_link_values_pointers.py
tests/valoria/test_modules_reachable_closure.py
tests/valoria/test_wiring_validation.py
tests/valoria/test_pointer_audit.py
tests/valoria/test_stubwire.py
tests/valoria/test_sim_fabrication_scope.py
tests/valoria/test_tool_input_paths_resolve.py
tests/valoria/test_combat_capability_clamp.py""".split()


NOX = False


def sh(wt, *cmd, timeout=600):
    p = subprocess.run(cmd, cwd=wt, capture_output=True, text=True, timeout=timeout,
                       env={**os.environ, 'PYTHONHASHSEED': '0', 'PYTHONUTF8': '1'})
    return p.returncode, p.stdout, p.stderr


def run_file(wt, f, tmo):
    t = time.time()
    if not os.path.exists(os.path.join(wt, f)):
        return dict(file=f, outcome='absent', wall_s=0.0, tail=[])
    try:
        rc, out, err = sh(wt, sys.executable, '-m', 'pytest', f, '-q', *([] if NOX else ['-x']), '-p', 'no:cacheprovider', '--no-header', timeout=tmo)
    except subprocess.TimeoutExpired:
        return dict(file=f, outcome='timeout', wall_s=round(time.time() - t, 1), tail=[])
    lines = (out or '').strip().splitlines()
    m = re.search(r'(\d+) failed', ' '.join(lines[-3:])); p = re.search(r'(\d+) passed', ' '.join(lines[-3:]))
    e = re.search(r'(\d+) error', ' '.join(lines[-3:]))
    fail_lines = [l for l in lines if l.startswith('FAILED') or l.startswith('ERROR')][:4]
    return dict(file=f, outcome='pass' if rc == 0 else 'fail', rc=rc, wall_s=round(time.time() - t, 1),
                passed=int(p.group(1)) if p else 0, failed=int(m.group(1)) if m else 0, errors=int(e.group(1)) if e else 0,
                first_failures=fail_lines, tail=lines[-3:], stderr_tail=(err or '').strip().splitlines()[-3:])


def run_set(log, wt, label, tmo, jobs, only='', skip=''):
    t0 = time.time()
    global TESTS
    full = list(TESTS)
    if only:
        TESTS = [t for t in full if any(o in t for o in only.split(','))]
    for sk in [x for x in skip.split(',') if x]:
        for t in [t for t in TESTS if sk in t]:
            log.w('skipped', label=label, file=t, why='run separately with a long timeout in the end-state worktree (it takes 5-13 minutes alone)')
        TESTS = [t for t in TESTS if sk not in t]
    log.w('section_start', label=label, section='run_set', n_files=len(TESTS), jobs=jobs, file_timeout_s=tmo)
    res = []
    with cf.ThreadPoolExecutor(jobs) as ex:
        for r in ex.map(lambda f: run_file(wt, f, tmo), TESTS):
            res.append(r)
            log.w('batch', label=label, n=1, **r)
            if r['outcome'] in ('fail', 'timeout'):
                log.w('fail', label=label, what=f"{r['file']} {r['outcome']} in phase {label}", detail=r.get('first_failures') or r.get('tail'))
    c = {k: sum(1 for r in res if r['outcome'] == k) for k in ('pass', 'fail', 'timeout', 'absent')}
    log.w('result', label=label, counts=c, n_files=len(res), wall_s=round(time.time() - t0, 1),
          failing=[r['file'] for r in res if r['outcome'] in ('fail', 'timeout')], stop='all files finished')
    return res


def edit(path, fn):
    s = open(path, encoding='utf-8').read(); n = fn(s)
    open(path, 'w', encoding='utf-8').write(n); return n != s



# ---------------------------------------------------------------------------------------------
# The B1 edits, one function per phase. Each returns the list of edits it applied (logged verbatim).
# They apply ONLY what P1 section 5 / section 6 B1 says; a deletion with no replacement is applied as a deletion.
# ---------------------------------------------------------------------------------------------
def _sub(path, pat, repl, count=0, flags=0):
    s = open(path, encoding='utf-8').read()
    n, k = re.subn(pat, repl, s, count=count, flags=flags)
    open(path, 'w', encoding='utf-8').write(n)
    return k


def edit_p1b(wt):
    """item 1b: the proposal's repointings of the kernel's dependants, as P1 lists them (6 tests, sim_params.json, value_pointer_links.json,
    the `sim_module:` pointer and the stale row in references/module_contracts.yaml:448-470)."""
    out = []
    j = lambda *p: os.path.join(wt, *p)
    # the sim_module pointer / stale row: point at nothing
    k = _sub(j('references/module_contracts.yaml'), r'(\n  - module: social_contest\n(?:.*\n)*?    sim_module: )systems/social_contest/sim/contest/', r'\1none', count=1)
    out.append(f'module_contracts.yaml: social_contest sim_module -> none ({k} edit)')
    # json entries naming kernel files: delete those entries
    import json as _j
    for rel in ('engine/engine_params/sim_params.json', 'engine/engine_params/value_pointer_links.json'):
        path = j(rel); d = _j.load(open(path, encoding='utf-8'))
        def strip(o):
            if isinstance(o, list):
                keep = [strip(x) for x in o if 'systems/social_contest/sim/contest' not in _j.dumps(x)]
                return keep
            if isinstance(o, dict):
                return {k: strip(v) for k, v in o.items()}
            return o
        before = len(_j.dumps(d)); d2 = strip(d)
        open(path, 'w', encoding='utf-8').write(_j.dumps(d2, indent=2, ensure_ascii=False) + '\n')
        out.append(f'{rel}: removed entries naming the kernel ({before - len(_j.dumps(d2))} chars)')
    # tests that test the kernel itself: delete
    for rel in ('engine/tests/test_contest_kernel.py',):
        if os.path.exists(j(rel)):
            os.remove(j(rel)); out.append(f'deleted {rel}')
    return out


def edit_p1c(wt):
    """items 2 + 5: the cross-ledger reads and the unread arrangement keys."""
    out = []
    j = lambda *p: os.path.join(wt, *p)
    sh(wt, 'git', 'checkout', '--', 'engine/season/queries/inputs.py', 'modules/social_contest/roll.py', 'engine/season/seam/wrappers/sigma.py',
       'engine/season/queries/world_q.py', 'engine/season/data/arrangements.py', 'engine/season/arrangements.yaml')
    out.append('reset the six files this phase edits to HEAD (idempotent re-run after a failed first attempt, kept in the log)')
    # --- item 2: fields, room term, host reads, the two Queries
    k = _sub(j('engine/season/queries/inputs.py'), r'\n    reception: float = 0\.0\n    reception_gain: float = 0\.0\n    proofs: float = 0\.0\n    proof_step: float = 0\.0', '')
    out.append(f'inputs.py: removed reception/reception_gain/proofs/proof_step fields ({k})')
    k = _sub(j('modules/social_contest/roll.py'), r'    room = float\(inp\.reception_gain\).*\n    ob = max\(ob - room.*\n', '')
    out.append(f'roll.py: removed the room term lines 104-105 ({k})')
    k = _sub(j('engine/season/seam/wrappers/sigma.py'), r'from \.\.\.queries\.world_q import proofs, reception\n', '')
    k2 = _sub(j('engine/season/seam/wrappers/sigma.py'), r'    room_terms = \{\}\n    if room is not None:\n        room_terms = dict\(.*\n.*\n.*\n.*\n', '', flags=0)
    k3 = _sub(j('engine/season/seam/wrappers/sigma.py'), r', \*\*room_terms\)', ')')
    out.append(f'sigma.py: removed the proofs/reception import ({k}), the room_terms block ({k2}), the **room_terms spread ({k3})')
    path = j('engine/season/queries/world_q.py'); s = open(path, encoding='utf-8').read()
    a = s.index('_UNREAD = object()'); b = s.index('# \u26a0 `home_of(w)` WAS HERE')
    open(path, 'w', encoding='utf-8').write(s[:a] + s[b:])
    out.append(f'world_q.py: deleted `_UNREAD`, `reception`, `proofs` ({b - a} chars)')
    # --- item 5: arrangement keys
    ap = j('engine/season/data/arrangements.py')
    out.append(f'arrangements.py: written_only out of _ORDER_VALUES ({_sub(ap, chr(34) + "scripted" + chr(34) + ", " + chr(34) + "written_only" + chr(34), chr(34) + "scripted" + chr(34))})')
    out.append(f'arrangements.py: bench_basis, records_dissent out of _ARRANGEMENT_KEYS ({_sub(ap, r"\"bench_basis\", ", "", count=1)}, {_sub(ap, r"\"records_dissent\", ", "", count=1)})')
    s = open(ap, encoding='utf-8').read()
    for blk in ('    bench_basis = need("bench_basis")\n    if bench_basis != "none":\n        _refuse_not_in(name, "bench_basis", bench_basis, REMIT_ACTS, "`none` or a `remit_acts` member")\n',
                '    records_dissent = need("records_dissent")\n    if not isinstance(records_dissent, bool):\n        raise SystemExit(f"arrangements.yaml: {name!r} has `records_dissent: {records_dissent!r}`, "\n                         "not `true`/`false`.")\n'):
        assert blk in s, 'need() block not found verbatim'
        s = s.replace(blk, '')
    s = s.replace('"disposal": disposal, "bench_basis": bench_basis,', '"disposal": disposal,').replace(' "records_dissent": records_dissent,', '')
    open(ap, 'w', encoding='utf-8').write(s)
    out.append('arrangements.py: removed the two need() blocks and their row-dict entries')
    k = _sub(j('engine/season/arrangements.yaml'), r'^ *(bench_basis|records_dissent): .*\n', '', flags=re.M)
    out.append(f'arrangements.yaml: removed {k} bench_basis / records_dissent lines')
    return out


def edit_p1d(wt):
    """items 3 + 4 LITERALLY: the discrete path, the int cast, leverage=0.0, _capability/_pool_of/_opposition_of, VERB_CAPABILITY."""
    out = []
    j = lambda *p: os.path.join(wt, *p)
    out.append(f'roll.py: roll_net -> roll_net_continuous ({_sub(j("modules/social_contest/roll.py"), r"roll_net\(inp\.pool, rng=rng\)", "roll_net_continuous(inp.pool, rng=rng)")}, import {_sub(j("modules/social_contest/roll.py"), r"import OB_MIN, net_boost, roll_net", "import OB_MIN, net_boost, roll_net_continuous")})')
    sp = j('engine/season/seam/wrappers/sigma.py'); s = open(sp, encoding='utf-8').read()
    a = s.index('def _capability('); b = s.index('def contest_input(')
    s = s[:a] + s[b:]
    s = s.replace('pool=_pool_of(w.persons[claimants[0]], verb, fx),', 'pool=fx.get("pool_default"),').replace('opposition=_opposition_of(w, subject, verb),', 'opposition=None,')
    open(sp, 'w', encoding='utf-8').write(s)
    out.append('sigma.py: deleted _capability, _pool_of, _opposition_of; contest_input now reads pool_default and opposition None (the least edit that still imports)')
    out.append(f'rosters.py: VERB_CAPABILITY map -> {{}} ({_sub(j("engine/season/data/rosters.py"), r"^VERB_CAPABILITY[^\n]*\n(?:[ \t]+.*\n)*", "VERB_CAPABILITY = {}\n", flags=re.M)})')
    return out


def edit_p1b2(wt):
    """item 1b, corrected: the two JSON files are GENERATED, so they are regenerated, not hand-edited (undoes phase P1b's hand edit)."""
    out = []
    rc, o, e = sh(wt, 'git', 'checkout', '--', 'engine/engine_params/sim_params.json', 'engine/engine_params/value_pointer_links.json'); out.append(f'git checkout the two JSON files (rc {rc})')
    for cmd in (['tools/export_sim_params.py', '--build'], ['tools/link_values_pointers.py', '--build']):
        rc, o, e = sh(wt, sys.executable, *cmd); out.append(f"python {' '.join(cmd)} -> rc {rc}: {(o or e).strip().splitlines()[-1][:120]}")
    return out


def edit_p1b3(wt):
    """item 1b, the dependant P1 does NOT list: engine/tests/test_sigma_leverage_parity.py imports the kernel's degree_extension (:52).
    Repoint = drop the import and the two definitions that call it (TestPoolAwareDegree, the pre-ruling-rows test)."""
    import ast
    path = os.path.join(wt, 'engine/tests/test_sigma_leverage_parity.py'); src = open(path, encoding='utf-8').read()
    tree = ast.parse(src); lines = src.split('\n'); drop = []
    for n in tree.body:
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)) and 'CD.' in ast.get_source_segment(src, n):
            drop.append((n.lineno - 1 - len(n.decorator_list), n.end_lineno, n.name))
    out = [f'dropping {[d[2] for d in drop]}']
    for a_, b_, _ in sorted(drop, reverse=True):
        del lines[a_:b_]
    new = '\n'.join(lines).replace('from systems.social_contest.sim.contest import degree_extension as CD  # noqa: E402\n', '')
    open(path, 'w', encoding='utf-8').write(new)
    rc, o, e = sh(wt, sys.executable, '-m', 'pytest', 'engine/tests/test_sigma_leverage_parity.py', '-q', '-x', '-p', 'no:cacheprovider', '--no-header')
    out.append(f'then pytest parity: rc {rc}: {(o or e).strip().splitlines()[-1][:120]}')
    return out


EDITS = {'P1b3': ('item 1b, unlisted dependant: repoint test_sigma_leverage_parity', edit_p1b3), 'P1b2': ('item 1b corrected: regenerate the generated JSON', edit_p1b2), 'P1b': ('item 1b: repoint the kernel dependants as P1 lists them', edit_p1b),
         'P1c': ('items 2 and 5: delete the cross-ledger reads and the unread row keys', edit_p1c),
         'P1d': ('items 3 and 4 literally: discrete path, int cast, _pool_of/_opposition_of/VERB_CAPABILITY', edit_p1d)}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--wt', required=True); ap.add_argument('--phase', required=True)
    ap.add_argument('--log', required=True); ap.add_argument('--file-timeout', type=float, default=420)
    ap.add_argument('--jobs', type=int, default=3)
    ap.add_argument('--no-x', action='store_true', help='do not stop a file at its first failure (count failing tests)')
    ap.add_argument('--only', default='', help='comma list of path substrings: run only these files')
    ap.add_argument('--skip', default='', help='comma list of path substrings to skip (logged as skipped)')
    a = ap.parse_args()
    global NOX
    NOX = a.no_x
    log = Log(a.log); wt = a.wt
    log.w('manifest', label=a.phase, argv=sys.argv, head=git('rev-parse', 'HEAD'), branch=git('rev-parse', '--abbrev-ref', 'HEAD'),
          python=sys.version.split()[0], pythonhashseed='0', worktree=wt, wt_head=sh(wt, 'git', 'rev-parse', 'HEAD')[1].strip(),
          utc_note='see t')
    try:
        if a.phase == 'P0':
            log.w('plan', label='P0', what='control: run the B1-affected test files at unmodified HEAD in the scratch worktree')
        elif a.phase == 'P1a':
            log.w('plan', label='P1a', what='git rm -r systems/social_contest/sim/contest ONLY (no repointing): which files break?')
            rc, o, e = sh(wt, 'git', 'rm', '-r', '-q', 'systems/social_contest/sim/contest')
            log.w('result', label='P1a', applied='git rm kernel dir', rc=rc, stderr=e[-300:], files_left=sorted(os.listdir(os.path.join(wt, 'systems/social_contest/sim'))))
        elif a.phase.startswith('RUN'):
            pass
        elif a.phase in EDITS:
            log.w('plan', label=a.phase, what=EDITS[a.phase][0])
            for ln in EDITS[a.phase][1](wt):
                log.w('result', label=a.phase, applied=ln)
        else:
            log.w('blocked', label=a.phase, why='unknown phase; use P0, P1a, P1b, P1c, P1d or RUN:<label>', at='stress_p1_b1.py::main')
            return
        label = a.phase.replace('RUN:', '') if a.phase.startswith('RUN') else a.phase
        run_set(log, wt, label, a.file_timeout, a.jobs, a.only, a.skip)
    except Exception:
        log.w('error', label=a.phase, traceback=traceback.format_exc())
    log.w('summary', label=a.phase)

if __name__ == '__main__':
    main()
