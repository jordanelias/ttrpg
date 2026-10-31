"""Stress harness for PROPOSAL 2, "Staged proceeding" (social-contest-proposal-2-staged-proceeding.md).

Sections (run from the repo root; each writes ONE flushed JSON line per event, PR #530's audit-log shape):
  model    -- a MODEL of P2's stage lists as Markov chains over the REAL engine's band probabilities
              (pace / stall, plea dominance, R-24 collapse, sensitivity, sigma channel, model extremes)
  world    -- REAL-code probes on `build_realm` / `tiny_world`: the case file as carrier, forum detour vs the
              live refusal of a second case, failure injection, real data (S5), determinism and wall time
  batches  -- P2's FIRST BATCH (S1 deletions) and its pinned-hash claims applied to a SCRATCH git worktree
              (never the main tree); pytest per file, counted, baseline first

FIDELITY. REAL: engine.dice_engine (die rule, degree_from_net, sigma_leverage.net_boost), modules.social_contest.roll
(obstacle, roll), seam/wrappers/sigma.py's S27.4 rule (re-stated, see model_s274), the effect functions open_case /
determine / seize / destroy_record / forge, matter.py's maturation, build_realm worlds, test files in the worktree.
MODEL (mine; evidence about the design, not the code): every stage list, band->transition table, plea payoff, scene
budget sitting rule and collapse rule. P2 builds none of them, so none can be run as code.

USAGE (repo root; scratch worktree for `batches*` is made first with `git -C . worktree add <SCRATCH>/wt HEAD` and removed after):
  python proposals/2026-10-29-parliament-and-debate/stress_p2.py --section model|world|batches|batches2|batches3 --log OUT.jsonl [--parts q0,draws,sens2,cite | w1..w5,s2]
  The model section was run whole, then its --parts follow-ups appended to the same log; the world section whole, then w1 twice and s2 appended; batches whole, then batches2 and batches3.

NO CHOSEN HORIZON OR TRIAL COUNT: chains run to absorption or a 'quiet' window (no mass change > 1e-12 over a window of
seasons) or the wall-clock budget; MC controls and real-world runs stop on the first of crash / quiet / budget and the
stop reason is logged.
"""
import argparse, itertools, json, math, os, random, subprocess, sys, time, traceback
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from stress_probe import Log, git  # one owner of the audit-log shape

SCRATCH = '/tmp/claude-0/-home-user-ttrpg/b9ffadb9-a21e-55d5-8bf9-c652527b3c6b/scratchpad/stress/p2'
WT = os.path.join(SCRATCH, 'wt')
PROP = '2026-10-30-social-contest-proposal-2-staged-proceeding.md'
INF, NAN = float('inf'), float('nan')


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (round((c - h) / d, 5), round((c + h) / d, 5))


def manifest(log, section, extra=None):
    log.w('manifest', section=section, argv=sys.argv, head=git('rev-parse', 'HEAD'), branch=git('rev-parse', '--abbrev-ref', 'HEAD'),
          python=sys.version.split()[0], platform=sys.platform, pythonhashseed=os.environ.get('PYTHONHASHSEED'),
          scratch_worktree=WT, proposal=PROP, **(extra or {}))


# ====================================================================== MODEL
from engine.dice_engine import dice_engine as DE
from engine.dice_engine.sigma_leverage import net_boost, OB_MIN, p_success
from engine.season.queries.inputs import SocialContestInput
from modules.social_contest import roll as sc_roll

DIE = {-1: .1, 0: .5, 1: .3, 2: .1}   # from DE._die_result over faces 1..10 (verified in model_control)
_net_cache = {}


def net_pmf(pool):
    """Exact pmf of the integer net of roll_pool(pool): convolution of the die rule (same faces as DE._die_result)."""
    n = max(1, int(round(pool)))
    if n in _net_cache:
        return _net_cache[n]
    pm = {0: 1.0}
    for _ in range(n):
        nx = defaultdict(float)
        for k, p in pm.items():
            for d, q in DIE.items():
                nx[k + d] += p * q
        pm = dict(nx)
    _net_cache[n] = pm
    return pm


def bands(pool, ob, lev=0.0):
    """P(Overwhelming, Success, Partial, Failure) for the live roll: net = roll_net(pool) + net_boost(lev, pool); graded by
    DE.degree_from_net (the real ladder) -- exact over the integer pmf."""
    out = {'O': 0.0, 'S': 0.0, 'P': 0.0, 'F': 0.0}
    b = net_boost(lev, pool)
    for k, p in net_pmf(pool).items():
        d = DE.degree_from_net(k + b, ob).name
        out[{'OVERWHELMING': 'O', 'SUCCESS': 'S', 'PARTIAL': 'P', 'FAILURE': 'F'}[d]] += p
    return out


def ob_of(pool_opp, ceiling, default=2.0, extra=0.0):
    inp = SocialContestInput(pool=1, opposition=pool_opp, obstacle_default=default, obstacle_ceiling=ceiling,
                             obstacle_refusal_multiple=2.0, leverage=0.0, forgery_quality=extra)
    return sc_roll.obstacle(inp)


def model_control(log):
    """CONTROL: the exact pmf against the real sampler DE.roll_pool (seeded), Wilson interval on P(margin>=0)."""
    log.w('section_start', section='model.control', note='exact net pmf vs DE.roll_pool MC; falsifier: exact outside the interval')
    for pool, ob in ((1, 1.0), (2, 2.0), (5, 2.5), (12, 6.0), (30, 12.0)):
        rng = random.Random(pool * 7919)
        n = 200000
        k = sum(1 for _ in range(n) if DE.roll_pool(pool, rng=rng).net - ob >= 0)
        ex = bands(pool, ob)
        pe = ex['O'] + ex['S'] + ex['P']
        lo, hi = wilson(k, n)
        ok = lo <= pe <= hi
        log.w('result', section='model.control', pool=pool, ob=ob, n=n, mc_rate=round(k / n, 5), ci95=[lo, hi],
              exact=round(pe, 5), exact_inside_ci=ok, stop='n fixed by quiet-window rule: 200k is >10x the interval needed (width<0.003)')
        if not ok:
            log.w('fail', section='model.control', what='exact pmf outside MC interval', pool=pool, ob=ob, exact=pe, ci=[lo, hi])


ROWS = {
    'K3_royal(6)': ['admit', 'forum', 'plea', 'proof', 'quality', 'judgment'],
    'K3_heresy(4)': ['admit', 'plea', 'proof', 'judgment'],
    'K2_K4(2)': ['admit', 'judgment'],
    'K1_K7(1)': ['judgment'],
}


def S274_refused(pool, ob, mult=2.0):
    return ob > mult * max(pool, 0)


def chain(row, pb, B=5, q_forum=1.0, plea=(('deny', 1.0),), regime='sitting', referral=0.0, refused=False, maxseasons=400):
    """Exact season-by-season distribution of P2's staged proceeding (MY MODEL; the transition table is the proposal's
    flowchart column). Returns dict: cum (outcome -> list per season), stall mass, mean seasons.
    pb: band probabilities of the closing draw (same at every stage unless pb is a dict stage->bands).
    regime 'sitting': a judge closes up to B stages per season, a Partial detour ends the sitting;
           'season_per_stage': Q1's alternative, every closing act is a season.
    refused: S27.4 refusal -> the closing act is refused and the stage can never close (stall)."""
    stages = ROWS[row] if isinstance(row, str) else row
    getb = (lambda st: pb[st]) if (isinstance(pb, dict) and 'O' not in pb) else (lambda st: pb)
    Bm = 1 if regime == 'season_per_stage' else B

    def plea_branches(rest):
        has_q = 'quality' in rest
        out = []
        for mode, w in plea:
            if w <= 0:
                continue
            if mode == 'deny':
                a = [s for s in rest if s != 'quality']
            elif mode == 'justify':
                a = [s for s in rest if s != 'proof']
            else:   # concede
                a = [s for s in rest if s not in ('proof', 'quality')]
            if mode == 'justify' and not has_q:
                a = [s for s in rest if s != 'proof']
            out.append((w, tuple(a)))
        return out

    def run(ag, b):
        """-> list of (p, kind, val): ('abs', outcome) | ('next', agenda)"""
        if not ag:
            return [(1.0, 'abs', 'disposed')]
        head, rest = ag[0], ag[1:]
        if head == 'plea':
            res = []
            for w, a in plea_branches(rest):
                res += [(w * p, k, v) for p, k, v in run(a, b)]
            return res
        if head == 'forum':
            res = []
            if q_forum < 1.0:
                res += [((1 - q_forum) * p, k, v) for p, k, v in run(rest, b)]
            if q_forum > 0:
                res += [(q_forum * p, k, v) for p, k, v in roll_stage(ag, b)]
            return res
        return roll_stage(ag, b)

    def roll_stage(ag, b):
        head, rest = ag[0], ag[1:]
        if b == 0:
            return [(1.0, 'next', ag)]
        if refused:
            return [(1.0, 'next', ag)]       # S27.4: refused, no band, the stage does not close and nothing is emitted
        p = getb(head)
        res = []
        adv = lambda w: [(w * pp, k, v) for pp, k, v in (run(rest, b - 1) if rest else [(1.0, 'abs', 'disposed')])]
        if head == 'admit':
            res += adv(p['O'] + p['S'])
            res.append((p['F'], 'abs', 'dismissed'))
            res.append((p['P'] * referral, 'abs', 'referred'))
            res.append((p['P'] * (1 - referral), 'next', ag))
        elif head == 'forum':
            res.append((p['O'] + p['S'], 'abs', 'translated'))
            res += adv(p['F'])
            res.append((p['P'], 'next', ag))
        elif head == 'proof':
            res += adv(p['O'] + p['S'])
            res.append((p['F'], 'abs', 'not_proved'))
            res.append((p['P'], 'next', ag))
        elif head == 'quality':
            res += adv(1.0)
        elif head == 'judgment':
            res.append((p['O'] + p['S'], 'abs', 'disposed'))
            res.append((p['F'], 'abs', 'undetermined'))
            back = ('proof', 'judgment') if 'proof' in stages else ('judgment',)
            res.append((p['P'], 'next', back))
        else:
            raise ValueError(head)
        return [(w, k, v) for w, k, v in res if w > 0]

    def merge(res):
        d = defaultdict(float)
        for p, k, v in res:
            d[(k, v)] += p
        return d

    dist = {tuple(stages): 1.0}
    absorbed = defaultdict(lambda: [0.0])          # outcome -> cumulative prob at end of season s (index s)
    cum = defaultdict(float)
    hist = []
    quiet = 0
    for s in range(1, maxseasons + 1):
        nd = defaultdict(float)
        for ag, m in dist.items():
            for (k, v), p in merge(run(ag, Bm)).items():
                if k == 'abs':
                    cum[v] += m * p
                else:
                    nd[v] += m * p
        dist = nd
        left = sum(dist.values())
        hist.append((dict(cum), left))
        if len(hist) > 6 and abs(hist[-1][1] - hist[-6][1]) < 1e-12:
            quiet += 1
            if quiet >= 3:
                break
        else:
            quiet = 0
    left = hist[-1][1]
    tot = defaultdict(float, hist[-1][0])
    mean = None
    # expected seasons to absorption among the absorbed mass: sum_s P(not absorbed by s-1)
    surv = [1.0] + [h[1] + 0.0 for h in hist]
    # surv[s] = P(still open after s seasons); absorbed-or-open partition; E[T; T finite] approx = sum surv
    mean = sum(surv[:-1]) if left < 1e-9 else None
    def at(k):
        h = hist[min(k, len(hist)) - 1]
        return h[0]
    return dict(seasons_run=len(hist), open_mass_end=left, outcomes_end={k: round(v, 6) for k, v in tot.items()},
                mean_seasons=mean, hist=hist, at=at)


def summarise(r, ks=(1, 2, 3, 5, 10, 20)):
    out = {'seasons_run': r['seasons_run'], 'open_mass_end': round(r['open_mass_end'], 6), 'outcomes_end': r['outcomes_end'],
           'mean_seasons_if_all_absorb': None if r['mean_seasons'] is None else round(r['mean_seasons'], 4)}
    dc = [h[0].get('disposed', 0.0) for h in r['hist']]
    dend = dc[-1]
    if dend > 1e-9:
        prev = 0.0
        cm = 0.0
        for i, v in enumerate(dc):
            cm += (i + 1) * (v - prev)
            prev = v
        out['mean_seasons_given_disposed'] = round(cm / dend, 4)
        out['P_disposal_takes_3plus_seasons_given_disposed'] = round(1 - (dc[min(1, len(dc) - 1)] / dend), 5)
        out['P_disposal_same_season_given_disposed'] = round(dc[0] / dend, 5)
    else:
        out['mean_seasons_given_disposed'] = None
    for k in ks:
        h = r['hist'][min(k, len(r['hist'])) - 1]
        cum, left = h
        out[f'disposed<={k}'] = round(cum.get('disposed', 0.0), 5)
        out[f'terminal<={k}'] = round(1 - left, 5)
    return out


def tv(a, b):
    ks = set(a) | set(b)
    return 0.5 * sum(abs(a.get(k, 0) - b.get(k, 0)) for k in ks)


def pace_section(log, budget_end):
    log.w('section_start', section='model.pace',
          claim_text="One tick is a season; a six-stage trial with two adjournments takes three seasons and most of a judge's scene budget. (P2 section 7, Weakest 1)")
    log.w('claim', section='model.pace', text="every act is one draw; a closing act is one draw; plea and licence have none (P2 3.2)", where='P2 3.2')
    log.w('claim', section='model.pace', text="a forensic row of six stages costs six closing acts plus the advocacy, against roughly the advocacy plus one under P1 (P2 3.2)", where='P2 3.2')
    log.w('plan', section='model.pace', grid='row x roller pool J x opposition pool P x ceiling {live 2, 3, None} x regime {sitting B=5, sitting B=2, season_per_stage} x plea {deny, justify}',
          baselines='P1-style single draw: (A) Partial terminal, (B) Partial re-dockets next season',
          closing_draw='roller J dice vs Ob = obstacle(opposition P) via the REAL modules.social_contest.roll.obstacle; S27.4 refusal when Ob > 2J')
    n = 0
    headline = []
    for ceil_lbl, ceil in (('live2', 2.0), ('g1a3', 3.0), ('none', None)):
        for J in (2, 5, 12):
            for Pp in (2, 5, 12):
                if time.time() > budget_end:
                    log.w('skipped', section='model.pace', what='remaining grid', why='wall-clock budget')
                    return
                ob = ob_of(Pp, ceil)
                pb = bands(J, ob)
                ref = S274_refused(J, ob)
                base_disp = pb['O'] + pb['S']
                # P1-style baselines (exact, closed form)
                baseA = dict(one_season_disposal=round(base_disp, 5), partial_docketed=round(pb['P'], 5), undetermined=round(pb['F'], 5))
                baseB = dict(eventual_disposal=round(base_disp / (1 - pb['P']), 5) if pb['P'] < 1 else 0.0,
                             mean_seasons=round(1 / (1 - pb['P']), 4) if pb['P'] < 1 else None)
                for row in ROWS:
                    for regime, B in (('sitting', 5), ('sitting', 2), ('season_per_stage', 1)):
                        for pl in ('deny', 'justify'):
                            r = chain(row, pb, B=B, q_forum=1.0, plea=((pl, 1.0),), regime=regime, refused=ref)
                            s = summarise(r)
                            n += 1
                            rec = dict(section='model.pace', row=row, J=J, P=Pp, ceiling=ceil_lbl, ob=round(ob, 3), s274_refused=ref,
                                       regime=regime, B=B, plea=pl, bands={k: round(v, 5) for k, v in pb.items()},
                                       p1_baselineA=baseA, p1_baselineB=baseB, **s)
                            log.w('result', **rec)
                            if J == Pp and pl == 'deny' and B == 5 and regime == 'sitting':
                                headline.append(rec)
    log.w('batch', section='model.pace', n=n, note='exact DP, no sampling: the only n is the pmf (verified by model.control)')
    # explicit stall/cycle report: where Partial detours cycle
    for ceil_lbl, ceil in (('live2', 2.0), ('none', None)):
        for J in (2, 5, 12):
            ob = ob_of(J, ceil)
            pb = bands(J, ob)
            r = chain('K3_royal(6)', pb, B=5, q_forum=1.0, plea=(('deny', 1.0),), refused=S274_refused(J, ob))
            exp_adj = None
            # expected adjournments = sum over seasons of P(season s starts open) - 1 (first season is the sitting)
            surv = [1.0] + [h[1] for h in r['hist']]
            open_seasons = sum(surv[:-1])
            log.w('result', section='model.pace.stall', ceiling=ceil_lbl, J=J, P=J, ob=round(ob, 3),
                  p_partial_per_closing_act=round(pb['P'], 4), seasons_with_case_still_open_sum=round(open_seasons, 4),
                  p_open_after_5=round(r['hist'][min(4, len(r['hist']) - 1)][1], 5), p_open_after_20=round(r['hist'][min(19, len(r['hist']) - 1)][1], 6),
                  note='falsifier: if the open mass after 20 seasons is ~0 the chain does not stall; a refusal (S27.4) or pP=1 would show mass that never leaves')
    # forced-Partial cycle: impugn_motive 'Partial by construction' (arrangements.yaml reachable_bands [Partial])
    fp = {'O': 0.0, 'S': 0.0, 'P': 1.0, 'F': 0.0}
    r = chain('K2_K4(2)', fp, B=5)
    log.w('result', section='model.pace.forced_partial', what="a stage whose only apt act is capped at Partial (arrangements.yaml speech_kinds impugn_motive reachable_bands [Partial])",
          open_mass_end=r['open_mass_end'], seasons_run=r['seasons_run'], outcomes_end=r['outcomes_end'])
    if r['open_mass_end'] > 0.99:
        log.w('fail', section='model.pace.forced_partial', what='P2 says "Each Partial either pushes a stage or writes a docket item" and "A cap is optional row data" (3.5); with a Partial-capped act and no cap the case never leaves its stage',
              proposal_said='cap is optional row data', observed_open_mass=r['open_mass_end'])
    return headline



def pace_q0(log):
    """FOLLOW-UP to the first full model run: the main pace grid sets q_forum=1 (every case meets a forum challenge, and the challenger
    wins as often as the accuser), which sends 15-88% of K3 royal cases out by `translated`. This re-runs the royal row with no forum
    challenge (q_forum=0) so the six-stage pace is not read through that assumption. Logged as its own section; the first run's lines stay."""
    log.w('section_start', section='model.pace_q0', note='royal row with q_forum=0; false-start reason: q=1 conflates pace with forum exits')
    n = 0
    for ceil_lbl, ceil in (('live2', 2.0), ('none', None)):
        for J in (2, 5, 12):
            for Pp in (2, 5, 12):
                ob = ob_of(Pp, ceil)
                pb = bands(J, ob)
                ref = S274_refused(J, ob)
                for regime, B in (('sitting', 5), ('sitting', 2), ('season_per_stage', 1)):
                    for pl in ('deny', 'justify'):
                        r = chain('K3_royal(6)', pb, B=B, q_forum=0.0, plea=((pl, 1.0),), regime=regime, refused=ref)
                        n += 1
                        log.w('result', section='model.pace_q0', row='K3_royal(6)', q_forum=0.0, J=J, P=Pp, ceiling=ceil_lbl, ob=round(ob, 3), s274_refused=ref,
                              regime=regime, B=B, plea=pl, bands={k: round(v, 5) for k, v in pb.items()}, **summarise(r))
    log.w('batch', section='model.pace_q0', n=n, note='exact DP')


def draw_count(log):
    """How many closing DRAWS (not stages) does each plea path of P2's stage lists cost? P2 3.2 says 'a forensic row of six stages costs six
    closing acts'. P2's own roster says plea and licence have no draw, and the plea edits the agenda (deny: proof then judgment; concede: proof
    leaves; justify: quality is added). Counted from the flowchart's rules, not sampled."""
    log.w('section_start', section='model.draw_count', claim="A forensic row of six stages costs six closing acts plus the advocacy, against roughly the advocacy plus one under P1 (P2 3.2)", where='P2 3.2')
    row = ROWS['K3_royal(6)']
    paths = {'deny': ['admit', 'forum', 'proof', 'judgment'], 'concede': ['admit', 'forum', 'judgment'], 'justify(concede+quality)': ['admit', 'forum', 'quality', 'judgment'],
             'deny+justify in the alternative (proof AND quality)': ['admit', 'forum', 'proof', 'quality', 'judgment']}
    out = {k: len(v) for k, v in paths.items()}
    log.w('result', section='model.draw_count', listed_stages=len(row), stages_with_no_draw=['plea'], max_draws_if_no_plea_edit=len(row) - 1,
          draws_by_plea_path_forum_raised=out, draws_by_plea_path_no_forum={k: len(v) - 1 for k, v in paths.items()}, scene_budget=5)
    log.w('fail', section='model.draw_count', what='the six-stage royal row costs at most 5 closing draws (plea has none) and, on any single plea path of P2\'s own plea table, 3 to 5 (4 with a forum challenge); never six. '
          'With a scene budget of 5 a judge can close every stage of a sitting in one season, so the pace cost the proposal names comes only from Partial adjournments, not from stage count',
          proposal_said='"six stages costs six closing acts" (3.2) and Weakest (1) "a six-stage trial with two adjournments takes three seasons and most of a judge\'s scene budget"', counts=out)


def cite_check(log):
    """Open each file:line the proposal (or the brief) cites and test that the cited line carries the cited thing (CLAUDE.md 0.1 pt 3: 'as F says at :L')."""
    log.w('section_start', section='model.cite', note='each citation opened at its cited line; hit = the expected token is on that line or within +-1')
    checks = [
        ('engine/season/state/carriers.py', 783, 'stages: list[tuple]'),
        ('engine/season/loop/effects_information.py', 143, '_declared_stages'),        # P2 3.1: Record.stages / _declared_stages at :143-158
        ('engine/season/loop/effects_information.py', 162, '_docket_item'),            # P2 3.1: _docket_item at :162-166
        ('engine/season/loop/effects_information.py', 274, 'open_case'),               # P2 3.1: open_case at :274-354
        ('engine/season/loop/effects_information.py', 341, 'docketed'),                # brief/P2 flowchart: second case refused at :341
        ('engine/season/loop/effects_information.py', 419, '_eff_determine'),          # P2 3.1: _eff_determine at :419
        ('engine/season/loop/matter.py', 336, 'rec.stages'),                           # P2: matter.py:330-346
        ('engine/season/loop/matter.py', 340, 'due != w.tick'),
        ('engine/season/data/fixtures.py', 228, 'scene_budget=5'),
        ('engine/season/data/fixtures.py', 530, 'record_stages_default'),
        ('engine/season/loop/driver.py', 524, 'w.tick += 1'),
        ('engine/season/state/gate.py', 245, 'DISPOSABLE_KINDS'),                      # P2 5: gate.py:245-258
        ('engine/season/tests/test_season_weather.py', 378, 'BASE_HASHES'),            # P2 6 / brief (g): 378-380
        ('engine/season/tests/test_go07_canonical_digest.py', 469, 'BASE = {'),
        ('engine/season/arrangements.yaml', 265, 'excommunication_deliberation'),
        ('engine/season/seam/wrappers/sigma.py', 149, 'def contest_input'),
        ('engine/season/seam/contest.py', 118, 'def grade'),
        ('engine/season/queries/world_q.py', 566, 'judging_set'),
    ]
    miss = 0
    for f, ln, tok in checks:
        try:
            lines = open(os.path.join(ROOT, f), encoding='utf-8').read().splitlines()
            win = ' '.join(lines[max(0, ln - 2):ln + 1])
            hit = tok in win
            where = None
            if not hit:
                where = next((i + 1 for i, l in enumerate(lines) if tok in l), None)
            log.w('trial', section='model.cite', file=f, cited_line=ln, token=tok, n=1, hit=hit, actual_first_line_with_token=where)
            if not hit:
                miss += 1
                log.w('fail', section='model.cite', what=f'{f}:{ln} does not carry {tok!r}; the token is first at line {where}', proposal_said='citations opened at their line (P2 header, closing confidence line)')
        except Exception as e:
            log.w('error', section='model.cite', file=f, type=type(e).__name__, message=str(e)[:200], traceback=traceback.format_exc())
    log.w('result', section='model.cite.summary', checked=len(checks), missed=miss)


def collapse_section(log):
    log.w('section_start', section='model.collapse', claim="Collapsing breaks AR B30's 'the draw is identical at both fidelities' (P2 section 8 Q3); R-24",
          where='P2 8 Q3, 9a')
    log.w('plan', section='model.collapse', full='every stage as acts (chain, B=5, deny, q_forum=1)', collapsed_A='terminal judgment draw only',
          collapsed_B='terminal judgment draw but with the proof gate kept as a single product (pSO_proof*pSO_judgment)')
    rows = []
    for ceil_lbl, ceil in (('live2', 2.0), ('g1a3', 3.0), ('none', None)):
        for J in (2, 5, 12):
            for Pp in (2, 5, 12):
                ob = ob_of(Pp, ceil)
                pb = bands(J, ob)
                ref = S274_refused(J, ob)
                for row in ('K3_royal(6)', 'K3_heresy(4)'):
                    full = chain(row, pb, B=5, q_forum=1.0, plea=(('deny', 1.0),), refused=ref)['outcomes_end']
                    full_norm = defaultdict(float)
                    for k, v in full.items():
                        full_norm['disposed' if k == 'disposed' else ('undetermined' if k == 'undetermined' else 'other_terminal')] += v
                    col = chain(['judgment'], pb, B=5, plea=(('deny', 1.0),), refused=ref)['outcomes_end']
                    colA = {'disposed': col.get('disposed', 0), 'undetermined': col.get('undetermined', 0), 'other_terminal': 0.0}
                    d = tv(dict(full_norm), colA)
                    rec = dict(section='model.collapse', row=row, J=J, P=Pp, ceiling=ceil_lbl, ob=round(ob, 3),
                               full_outcomes={k: round(v, 5) for k, v in full_norm.items()},
                               collapsed_terminal_only={k: round(v, 5) for k, v in colA.items()}, tv_distance=round(d, 5),
                               disposed_full=round(full_norm['disposed'], 5), disposed_collapsed=round(colA['disposed'], 5))
                    log.w('result', **rec)
                    rows.append(rec)
    big = [r for r in rows if r['tv_distance'] > 0.05]
    log.w('result', section='model.collapse.summary', configs=len(rows), configs_tv_gt_0_05=len(big), max_tv=max(r['tv_distance'] for r in rows),
          min_tv=min(r['tv_distance'] for r in rows))
    if big:
        log.w('fail', section='model.collapse', what='collapsing to the terminal stage changes the outcome distribution by TV>0.05 in %d of %d configs, '
              'so a collapsed unwatched contest is a different game from a staged one even with the identical terminal draw' % (len(big), len(rows)),
              proposal_said='P2 8 Q3 names only that "collapsing breaks AR B30\'s same draw at both fidelities"; it does not say the distribution differs, nor by how much')
    # B30 nuance: per-act draws are keyed H(seed,tick,subject,purpose); the terminal draw value is the same in both runs
    log.w('result', section='model.collapse.b30_nuance',
          text="draws are keyed H(seed, tick, subject, purpose) (sigma.py docstring of resolve): the judgment-stage draw VALUE is identical in a collapsed and a staged run when tick/subject/purpose agree; "
               "what differs is whether it is reached. B30 'the same draw' therefore can hold while the OUTCOME distribution still differs (rows above). unverified: no keyed draw was executed here",
          status='unverified')
    log.w('unverified', section='model.collapse.b30_nuance', what='that the judgment draw value is identical across fidelities', why='needs a built stage-aware purpose key; not buildable here')


def plea_section(log):
    log.w('section_start', section='model.plea',
          claim="The assessor found denial weakly dominant for the respondent where the accuser bears the burden: at 5D an act against an equal fails 61% under R-5's divide-by-two (comparison 4; P2 4 'plea' stage, 3.1 roster)")
    log.w('claim', section='model.plea', text="The stasis ladder becomes a choice a player can make: concede the fact, fight on justification. That is R's 'intuit complex outcomes from simple choices'. (P2 7 Strongest)", where='P2 7')
    log.w('plan', section='model.plea', options='deny | concede | justify (concede + plead justification)',
          burden='accuser bears burden | respondent bears burden', control='concession rewarded: judgment Ob +delta against the accuser (delta in 0,.5,1,2), applied (i) through the real obstacle() so the live ceiling clips it and (ii) post-ceiling',
          utility='-severity: O 1.0, S 0.75, P 0.35, F 0; justification Success excuses (0), Partial halves; per-season cost c in {0, .05, .15}',
          roller='the burden-bearing side rolls its dice D vs Ob = opposing dice/2 (R-5); judge choice step not modelled')
    SEV = {'O': 1.0, 'S': 0.75, 'P': 0.35, 'F': 0.0}

    def sev(pj):
        return pj['O'] * SEV['O'] + pj['S'] * SEV['S']

    rows = []
    for ceil_lbl, ceil in (('live2', 2.0), ('g1a3', 3.0), ('none', None)):
        for DA in (2, 5, 12):
            for DR in (2, 5, 12):
                for burden in ('accuser', 'respondent'):
                    for delta_mode, delta in (('none', 0.0), ('pre', .5), ('pre', 1.0), ('pre', 2.0), ('post', .5), ('post', 1.0), ('post', 2.0)):
                        # judgment draw: accuser rolls DA vs Ob = DR/2 (+delta reward on concede)
                        ob_j = ob_of(DR, ceil)
                        pj_deny = bands(DA, ob_j)
                        if delta_mode == 'pre':
                            ob_c = ob_of(DR, ceil, extra=delta)
                        elif delta_mode == 'post':
                            ob_c = ob_j + delta
                        else:
                            ob_c = ob_j
                        pj_con = bands(DA, ob_c)
                        # proof draw
                        if burden == 'accuser':
                            pp = bands(DA, ob_of(DR, ceil))
                            a, b = pp['O'] + pp['S'], pp['P']       # a: proof succeeds against respondent
                            c = pj_deny['P']
                            Sev = sev(pj_deny)
                            denom = 1 - a * c - b
                            V_deny = -a * Sev / denom if denom > 1e-12 else float('nan')
                            N_deny = (b + a * c) / denom if denom > 1e-12 else float('inf')
                        else:   # respondent bears the burden: R rolls DR vs Ob = DA/2; success exonerates
                            pp = bands(DR, ob_of(DA, ceil))
                            a, b = pp['O'] + pp['S'], pp['P']       # a: respondent proves innocence
                            f = pp['F']
                            c = pj_deny['P']
                            Sev = sev(pj_deny)
                            # fail -> judgment with fact established; partial -> adjourn; success -> 0
                            denom = 1 - f * c - b
                            V_deny = -f * Sev / denom if denom > 1e-12 else float('nan')
                            N_deny = (b + f * c) / denom if denom > 1e-12 else float('inf')
                        c2 = pj_con['P']
                        Sev_c = sev(pj_con)
                        V_con = -Sev_c / (1 - c2) if c2 < 1 else float('nan')
                        N_con = c2 / (1 - c2) if c2 < 1 else float('inf')
                        pq = bands(DR, ob_of(DA, ceil))              # respondent rolls the justification
                        V_jus = -((pq['P'] * 0.5 + pq['F']) * (Sev_c / (1 - c2) if c2 < 1 else float('nan')))
                        N_jus = c2 / (1 - c2) if c2 < 1 else float('inf')
                        for cost in (0.0, 0.05, 0.15):
                            u = {'deny': V_deny - cost * N_deny, 'concede': V_con - cost * N_con, 'justify': V_jus - cost * N_jus}
                            best = max(u, key=lambda k: (u[k], k))
                            weak = [o for o in u if all(u[o] >= u[x] - 1e-12 for x in u)]
                            strict = [o for o in u if all(u[o] > u[x] + 1e-12 for x in u if x != o)]
                            dominated = [o for o in u if any(u[x] > u[o] + 1e-12 for x in u if x != o)]
                            rows.append(dict(ceiling=ceil_lbl, DA=DA, DR=DR, burden=burden, reward_mode=delta_mode, delta=delta, season_cost=cost,
                                             u={k: round(v, 5) for k, v in u.items()}, best=best, weakly_dominant=weak, strictly_dominant=strict,
                                             strictly_dominated=dominated, adj={'deny': round(N_deny, 3), 'concede': round(N_con, 3)}))
    for r in rows:
        log.w('result', section='model.plea', **r)
    # control arm summary: base = no reward, no cost
    base = [r for r in rows if r['delta'] == 0.0 and r['season_cost'] == 0.0]
    for burden in ('accuser', 'respondent'):
        b = [r for r in base if r['burden'] == burden]
        deny_best = sum(1 for r in b if 'deny' in r['weakly_dominant'])
        deny_strict = sum(1 for r in b if 'deny' in r['strictly_dominant'])
        con_dom = sum(1 for r in b if 'concede' in r['strictly_dominated'])
        jus_dom = sum(1 for r in b if 'justify' in r['strictly_dominated'])
        log.w('result', section='model.plea.summary', arm='no reward, no season cost (the proposal as written)', burden=burden, configs=len(b),
              deny_weakly_dominant=deny_best, deny_strictly_dominant=deny_strict, concede_strictly_dominated=con_dom, justify_strictly_dominated=jus_dom,
              note='exact computation over the engine pmf; n = number of (ceiling, DA, DR) configs, no sampling')
        if burden == 'accuser' and deny_best >= len(b) * 0.9:
            log.w('result', section='model.plea.verdict', text='assessor claim HELD under accuser-burden: denial is weakly dominant in %d of %d configs' % (deny_best, len(b)))
    # control: with reward, at what delta does concede beat deny
    flip = defaultdict(list)
    for r in rows:
        if r['burden'] == 'accuser' and r['season_cost'] == 0.0:
            flip[(r['ceiling'], r['DA'], r['DR'], r['reward_mode'])].append((r['delta'], r['best']))
    summ = {}
    for k, lst in flip.items():
        lst.sort()
        summ['|'.join(map(str, k))] = [(d, b) for d, b in lst]
    log.w('result', section='model.plea.control_reward', note='best option per reward delta (accuser burden, no season cost); a flip to concede/justify shows the reward is what would make the plea a real choice',
          table=summ)
    flipped = sum(1 for lst in flip.values() if any(b != 'deny' for d, b in lst if d > 0))
    log.w('result', section='model.plea.control_reward.summary', cells=len(flip), cells_where_a_reward_flips_best_away_from_deny=flipped)
    # does the live ceiling clip the 'pre' reward?
    clip = [r for r in rows if r['ceiling'] == 'live2' and r['reward_mode'] == 'pre' and r['delta'] == 2.0 and r['burden'] == 'accuser' and r['season_cost'] == 0.0]
    nodiff = sum(1 for r in clip if abs(r['u']['concede'] - next(x for x in rows if x['ceiling'] == 'live2' and x['reward_mode'] == 'none' and x['DA'] == r['DA'] and x['DR'] == r['DR'] and x['burden'] == 'accuser' and x['season_cost'] == 0.0)['u']['concede']) < 1e-9)
    log.w('result', section='model.plea.ceiling_clip', text='under the live ceiling 2, a concession reward routed through the obstacle (pre-ceiling) changes the concede payoff in %d of %d configs; the rest are clipped to nothing (roll.py: the ceiling bounds the result)' % (len(clip) - nodiff, len(clip)),
          unchanged=nodiff, of=len(clip))
    return rows


def sensitivity_section(log, base=None, tag='model.sensitivity'):
    log.w('section_start', section=tag, claim="armature H.2: 'sigma dominates at high pools'; and which parameter moves the staged outcome most (S2)")
    base = base or dict(row='K3_royal(6)', J=5, P=5, ceil=None, B=5, q=0.5, plea='deny', lev=0.0, referral=0.0, regime='sitting')

    def metric(**o):
        kw = {**base, **o}
        ob = ob_of(kw['P'], kw['ceil'])
        pb = bands(kw['J'], ob, kw['lev'])
        r = chain(kw['row'], pb, B=kw['B'], q_forum=kw['q'], plea=((kw['plea'], 1.0),), regime=kw['regime'], referral=kw['referral'],
                  refused=S274_refused(kw['J'], ob))
        h = r['hist'][min(2, len(r['hist']) - 1)]
        return h[0].get('disposed', 0.0), 1 - h[1], r['mean_seasons']
    b0 = metric()
    log.w('result', section=tag + '.base', base=base, disposed_le3=round(b0[0], 5), terminal_le3=round(b0[1], 5))
    sweeps = {'J': [1, 2, 5, 8, 12, 30], 'P': [1, 2, 5, 8, 12, 30], 'ceil': [2.0, 3.0, None], 'B': [1, 2, 3, 5, 10], 'q': [0.0, 0.5, 1.0],
              'plea': ['deny', 'justify', 'concede'], 'lev': [-1.0, -0.5, 0.0, 0.5, 1.0, 1.5], 'referral': [0.0, 0.5, 1.0],
              'row': list(ROWS), 'regime': ['sitting', 'season_per_stage']}
    rng_ = {}
    for k, vs in sweeps.items():
        vals = []
        for v in vs:
            m = metric(**{k: v})
            vals.append((v, round(m[0], 5), round(m[1], 5)))
            log.w('result', section=tag, param=k, value=v, disposed_le3=round(m[0], 5), terminal_le3=round(m[1], 5))
        spread = max(x[1] for x in vals) - min(x[1] for x in vals)
        rng_[k] = round(spread, 5)
    ranked = sorted(rng_.items(), key=lambda kv: -kv[1])
    log.w('result', section=tag + '.rank', metric='range of P(disposed within 3 seasons) over the parameter sweep, others at base', ranked=ranked)
    # sigma vs dice vs Ob at 2,5,12,30: Ob-equivalent of +1.5 sigma (capped 1.14) measured by exact P(meets)
    for N in (2, 5, 12, 30):
        ob = 0.5 * N
        base_p = sum(v for k, v in bands(N, ob).items() if k != 'F')
        target = sum(v for k, v in bands(N, ob, 1.5).items() if k != 'F')
        a, b = -60.0, ob
        for _ in range(80):
            mid = (a + b) / 2
            pm = sum(v for k, v in bands(N, mid).items() if k != 'F')
            if pm > target:      # p falls as ob rises: mid is too easy, search higher
                a = mid
            else:
                b = mid
        ob_equiv = ob - (a + b) / 2
        dice_p = {n: sum(v for k, v in bands(N + n, ob).items() if k != 'F') for n in (1, 2, 3)}
        log.w('result', section='model.sigma_channel', pool=N, ob=ob, p_meets_base=round(base_p, 5), p_meets_sigma1p5=round(target, 5),
              ob_points_equivalent_to_sigma1p5=round(ob_equiv, 3), armature_closed_form_ob=round(0.8 * math.sqrt(N) * 1.5 * math.tanh(1.5 / 1.5), 3),
              p_meets_plus_dice=dice_p, note='closed form vs exact discrete pmf; falsifier: armature H.2 says sigma exceeds dice share at 12D')
    log.w('null', section='model.sigma_channel.variance_share', what='the armature falsifier "share of outcome variance by channel across seeded realms at 5D and 12D"',
          how='not run: no producer for reception/argument/circumstance sigma exists in the tree (armature F: sigma channel is paper, sigma.py:191 literal 0.0), so a seeded realm has zero sigma variance by construction',
          status='untestable')
    return ranked


def extremes_section(log):
    log.w('section_start', section='model.extremes', note='S1 on the model and on the real obstacle/roll for the operands P2 adds (aptness price as an Ob term, stage list shapes)')
    # real roll at pool extremes with an aptness price (P2 3.2) added to Ob via forgery_quality (the only extra additive Ob operand the real obstacle() has)
    for pool in (-1, 0, 1, 5, 12, 30):
        for price in (-1.0, 0.0, 0.5, 2.0, 1e9, NAN, INF):
            inp = SocialContestInput(pool=pool, opposition=pool if pool > 0 else None, obstacle_default=2.0, obstacle_ceiling=None,
                                     obstacle_refusal_multiple=2.0, leverage=0.0, forgery_quality=price)
            try:
                rr = random.Random(3)
                m = sc_roll.roll(inp, rr)
                log.w('trial', section='model.extremes.aptness_as_ob', pool=pool, price=repr(price), net=m.net, ob=m.ob if m.ob == m.ob else 'nan',
                      s274_refused=bool(m.ob > 2.0 * max(pool, 0)) if m.ob == m.ob else 'nan_compares_false', n=1)
            except Exception as e:
                log.w('error', section='model.extremes.aptness_as_ob', pool=pool, price=repr(price), type=type(e).__name__, message=str(e)[:200], traceback=traceback.format_exc())
    log.w('result', section='model.extremes.aptness_as_ob.note',
          text='NaN price: ob is NaN and `ob > 2*pool` is False, so S27.4 does NOT refuse a NaN-obstacle act (sigma.py:273); the ladder then grades NaN margin. A pool of -1 rolls as 1D (roll_net floors); pool 0 as 1D.')
    nanm = SocialContestInput(pool=5, opposition=5, obstacle_default=2.0, obstacle_ceiling=None, obstacle_refusal_multiple=2.0, leverage=0.0, forgery_quality=NAN)
    m = sc_roll.roll(nanm, random.Random(1))
    try:
        d = DE.degree_from_net(m.net, m.ob)
        log.w('result', section='model.extremes.nan_ladder', net=m.net, ob=repr(m.ob), degree=str(d))
        if str(d).endswith('Failure'):
            log.w('fail', section='model.extremes.nan_ladder', what='a NaN obstacle grades as a silent Failure (not refused)', proposal_said='P2 3.2 adds an aptness price to Ob with no domain; a NaN price silently fails the stage',
                  degree=str(d))
    except Exception as e:
        log.w('error', section='model.extremes.nan_ladder', type=type(e).__name__, message=str(e), traceback=traceback.format_exc())
    # chain shape extremes
    pb = bands(5, 2.5)
    shapes = {'empty_stage_list': [], 'single_plea_only': ['plea'], 'forum_only': ['forum'], 'unknown_stage': ['admit', 'banana', 'judgment'],
              'duplicate_proof': ['admit', 'proof', 'proof', 'judgment'], 'no_judgment': ['admit', 'proof']}
    for nm, stg in shapes.items():
        try:
            r = chain(stg, pb, B=5, q_forum=1.0)
            log.w('result', section='model.extremes.stage_shapes', shape=nm, stages=stg, outcomes_end=r['outcomes_end'], open_mass_end=round(r['open_mass_end'], 6), seasons_run=r['seasons_run'])
            if nm == 'empty_stage_list' and r['outcomes_end'].get('disposed', 0) == 1.0:
                log.w('fail', section='model.extremes.stage_shapes', what='an empty stage list is treated as an immediate disposal (a case file with no agenda disposes of itself); P2 says the loader refuses an unknown stage id but is silent on an empty list or a list with no terminal stage',
                      proposal_said='"the loader refuses an unknown id" (3.1); empty / no-terminal lists unspecified')
            if nm == 'no_judgment' and r['outcomes_end'].get('disposed', 0) == 1.0:
                log.w('fail', section='model.extremes.stage_shapes', what='a row with no judgment stage disposes by default when the list runs out', proposal_said='"The terminal stage opens the row\'s disposal" (3.6): a row whose list has no judgment-kind terminal is unspecified')
        except Exception as e:
            log.w('error' if nm != 'unknown_stage' else 'result', section='model.extremes.stage_shapes', shape=nm, type=type(e).__name__, message=str(e)[:200],
                  note='in the MODEL an unknown stage raises ValueError; P2 places that refusal in the loader (unbuilt), so this is the model, not the code' if nm == 'unknown_stage' else '',
                  traceback=traceback.format_exc() if nm != 'unknown_stage' else '')
    # zero and huge weights are armature B-level (the weights column); the model has no weights. Log skipped with reason.
    log.w('skipped', section='model.extremes', what='zero and huge weights, legitimacy 0/1, empty bench, bench of 1/2/7/21', why='those operands belong to the armature (weights column, L, count Query), which P2 inherits and does not change; no P2-specific code path exists to run them against. The real-code empty-bench/seat probes are in the world section (S6).')
    # 1..50 matters per party: the docket refuses a second item per matter; model: how many cases can one party hold
    log.w('result', section='model.extremes.matters_per_party', text='open_case refuses a matter already docketed (effects_information.py:352 in this tree; P2 cites :341), so 1..50 matters about one party cannot be docketed as separate cases; the world section opens 1 and 5 to count', status='see world')


def run_model(log, budget_s, parts=None):
    manifest(log, 'model', {'parts': parts})
    if parts == ['cite']:
        cite_check(log)
        log.w('summary', section='model', parts=parts, stop='finished')
        return
    if parts == ['sens2']:
        sensitivity_section(log, dict(row='K3_royal(6)', J=8, P=5, ceil=2.0, B=5, q=0.0, plea='deny', lev=0.0, referral=0.0, regime='sitting'), tag='model.sensitivity_favourable')
        log.w('summary', section='model', parts=parts, stop='finished')
        return
    if parts == ['draws']:
        draw_count(log)
        log.w('summary', section='model', parts=parts, stop='finished')
        return
    if parts == ['q0']:
        pace_q0(log)
        log.w('summary', section='model', parts=parts, stop='finished')
        return
    t0 = time.time()
    end = t0 + budget_s
    log.w('plan', section='model', budget_s=budget_s, stages=['control', 'pace', 'collapse', 'plea', 'sensitivity', 'extremes'])
    for fn in (model_control, ):
        fn(log)
    pace_section(log, end)
    collapse_section(log)
    plea_section(log)
    sensitivity_section(log)
    extremes_section(log)
    log.w('summary', section='model', wall_s=round(time.time() - t0, 2), stop='finished all stages (exact computation; no sampling horizon)')


# ====================================================================== WORLD (real code)
def run_world(log, budget_s, parts=None):
    manifest(log, 'world', {'parts': parts})
    world_main(log, budget_s, parts)


def run_batches(log, budget_s):
    manifest(log, 'batches')
    batch_main(log, budget_s)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--section', required=True, choices=['model', 'world', 'batches', 'batches2', 'batches3'])
    ap.add_argument('--budget-s', type=float, default=600.0)
    ap.add_argument('--parts', default='', help='world only: comma list of w1,w2,w3,w4,w5 (default all)')
    ap.add_argument('--log', required=True)
    a = ap.parse_args()
    log = Log(a.log)
    try:
        if a.section == 'world':
            run_world(log, a.budget_s, [p for p in a.parts.split(',') if p] or None)
        else:
            if a.section == 'model':
                run_model(log, a.budget_s, [p for p in a.parts.split(',') if p] or None)
            elif a.section == 'batches3':
                manifest(log, 'batches3')
                batch_seed_hashes(log, a.budget_s)
            elif a.section == 'batches2':
                manifest(log, 'batches2')
                batch_followup(log, a.budget_s)
            else:
                run_batches(log, a.budget_s)
    except Exception as e:
        log.w('error', section=a.section, type=type(e).__name__, message=str(e)[:400], traceback=traceback.format_exc())
        log.w('summary', section=a.section, stop='crash')



# ---------------------------------------------------------------------------------------------- world section
def _tb(e):
    return traceback.format_exc()


def world_main(log, budget_s, parts=None):
    t0 = time.time()
    end = t0 + budget_s
    log.w('plan', section='world', budget_s=budget_s,
          parts=['w1 case file lifecycle (tiny_world, real fold, P2 stage labels declared on the act)',
                 'w2 forum detour vs the live refusal (effects_information.py second-case refusal) and the eight rows',
                 'w3 failure injection', 'w4 real data on build_realm 0,1,2 (S5)', 'w5 seasons: case files, determinism, wall time (S4/S7)'])
    for fn in (w1_case_file, w2_forum_and_rows, w3_failures):
        if parts and fn.__name__.split('_')[0] not in parts:
            continue
        try:
            fn(log)
        except Exception as e:
            log.w('error', section='world.' + fn.__name__, type=type(e).__name__, message=str(e)[:300], traceback=traceback.format_exc())
    for fn in (w4_realm_data, w5_seasons, s2_proxy):
        if parts and fn.__name__.split('_')[0] not in parts:
            continue
        try:
            (fn(log) if fn is s2_proxy else fn(log, end))
        except Exception as e:
            log.w('error', section='world.' + fn.__name__, type=type(e).__name__, message=str(e)[:300], traceback=traceback.format_exc())
    log.w('summary', section='world', wall_s=round(time.time() - t0, 1),
          stop='all parts finished' if time.time() < end else 'wall-clock budget')


def _imports():
    from engine.season.tests import test_u7_remit as U
    from engine.season.tests import test_in12_seize as S12
    from engine.season.loop.driver import mint_token
    from engine.season.data.matrix import WriteClass
    from engine.season.state.carriers import Act
    from engine.season.queries import world_q
    return U, S12, mint_token, WriteClass, Act, world_q


def _act(Act, key, verb, actor, via=None, **payload):
    return Act(id=key, actor=actor, verb=verb, via=via, payload=payload)


def _matter_tick(w, d, mint_token, WriteClass):
    evs = d.matter(mint_token(w, WriteClass.MATTER), [])
    w.tick += 1
    return evs or []


def w1_case_file(log):
    U, S12, mint_token, WriteClass, Act, world_q = _imports()
    kinds = U._kinds
    DUKE, SEAT, PARTY = U.DUKE, U.SEAT, U.PARTY
    log.w('section_start', section='world.w1', note='tiny_world (probes.tiny_world) is real engine state, hand-built; build_realm variant follows in w1b')
    log.w('claim', section='world.w1', where='P2 3.1', text="The case file's Record.stages ... `open_case` already mints (effects_information.py:274-354); its labels are placeholders (stage1.., H-80, record_stages_default=3, data/fixtures.py:530)")
    log.w('claim', section='world.w1', where='P2 3.1', text='MATTER does not mature a stage whose holder is gone (loop/matter.py:330-346), and seize and destroy_record exist')
    log.w('claim', section='world.w1', where='P2 flowchart, 1, 8 Q2', text='the file can be seized, forged or destroyed, and it stops when its holder is gone')
    log.w('claim', section='world.w1', where='P2 9a', text='S: it pauses correctly (an empty bench halts the agenda; a seated one resumes it)')

    def fresh(stages_labels=None, row='legal_trial'):
        w, d = U._world(**U.JUDGE)
        labels = stages_labels or ROWS['K3_royal(6)']
        stages = [(w.tick + i + 1, lab, 'oc') for i, lab in enumerate(labels)]
        out = U._fold(w, d, U._open('oc', arrangement=row, stages=stages))
        return w, d, out, stages

    # A. winding with P2's labels, read back
    w, d, out, stages = fresh()
    rid = 'rec:oc'
    rec = w.records.get(rid)
    log.w('result', section='world.w1.A', events=kinds(out), record_found=rec is not None,
          stages=[list(s[:2]) + ['<act>'] for s in (rec.stages if rec else [])], record_kind=getattr(rec, 'kind', None),
          docket=[{k: (v if not isinstance(v, str) or len(v) < 40 else v[:40]) for k, v in i.items()} for i in w.docket],
          docket_has_case_key=any('case' in i for i in w.docket))
    if rec and [s[1] for s in rec.stages] == ROWS['K3_royal(6)']:
        log.w('result', section='world.w1.A', verdict='HELD', text='a declared stage list is wound onto the case file verbatim by the existing open_case (labels are not validated: any string is accepted)')
    # label validation: nothing refuses an unknown stage label at the record
    w2, d2 = U._world(**U.JUDGE)
    o2 = U._fold(w2, d2, U._open('oc', arrangement='legal_trial', stages=[(1, 'banana', 'oc'), (2, '', 'oc')]))
    log.w('result', section='world.w1.A.unknown_label', events=kinds(o2), accepted=kinds(o2) == ['case.opened'],
          note='P2 puts the refusal of an unknown stage id in the arrangements loader (3.1); a case file wound by an act is not loader-checked, so stage labels on the file are unvalidated')

    # B. maturation control: holder present, every due tick
    w, d, out, stages = fresh()
    matured = {}
    for _ in range(8):
        evs = _matter_tick(w, d, mint_token, WriteClass)
        for e in evs:
            if e.kind == 'term.matured' and any(c.subject == rid for c in e.changes):
                matured[w.tick - 1] = matured.get(w.tick - 1, 0) + 1
    log.w('result', section='world.w1.B_control', matured_per_tick=matured, stages_declared=len(stages), rec_matured_flag=w.records[rid].matured,
          stages_after=[s[1] for s in w.records[rid].stages], note='control: holder present; MATTER matures one stage per due tick and never pops the list (agenda head never advances by MATTER)')
    if len(stages_set := [s[1] for s in w.records[rid].stages]) == len(stages):
        log.w('result', section='world.w1.B_control', verdict='HELD', text='no existing code pops Record.stages: the agenda transition P2 adds (pop head, push detour) is wholly new')

    # C. holder gone at a due tick, then back
    def holder_gap(variant):
        w, d, out, stages = fresh()
        holder = DUKE
        seen = {}
        for step in range(8):
            if step == 2:     # MATTER at tick 2 (stage 2's due tick) must find the holder absent (RERUN 2: the first version used step 1 and so skipped stage 1)
                if variant == 'person_deleted':
                    saved = w.persons.pop(holder)
                else:
                    saved = [t for t in w.tenures if t.object == rid and t.kind == 'hold' and t.live]
                    for t in saved:
                        t.until = w.tick
            if step == 3:     # back at tick 3
                if variant == 'person_deleted':
                    w.persons[holder] = saved
                else:
                    for t in saved:
                        t.until = None
            evs = _matter_tick(w, d, mint_token, WriteClass)
            for e in evs:
                if e.kind == 'term.matured' and any(c.subject == rid for c in e.changes):
                    seen[w.tick - 1] = seen.get(w.tick - 1, 0) + 1
        return seen, len(stages)
    for variant in ('person_deleted', 'hold_closed'):
        try:
            seen, n = holder_gap(variant)
            missing = [t for t in range(1, n + 1) if t not in seen]
            log.w('result', section='world.w1.C_holder_gap', variant=variant, matured_ticks=seen, stages_declared=n, ticks_never_matured=missing)
            if missing:
                log.w('fail', section='world.w1.C_holder_gap', variant=variant,
                      what='a stage whose due tick passes while its holder is absent NEVER matures, even after the holder returns (matter.py matures only at due == w.tick); the agenda does not "resume" on a seated holder, it is dead for good',
                      proposal_said="S: 'an empty bench halts the agenda; a seated one resumes it' (9a) and 'it stops when its holder is gone' (flowchart)",
                      observed={'matured_ticks': seen, 'never': missing})
        except Exception as e:
            log.w('error', section='world.w1.C_holder_gap', variant=variant, type=type(e).__name__, message=str(e)[:300], traceback=traceback.format_exc())

    # D. burn
    w, d, out, stages = fresh()
    before_docket = list(w.docket)
    o = U._fold(w, d, _act(Act, 'burn', 'destroy_record', DUKE, subject=rid))
    log.w('result', section='world.w1.D_burn', events=kinds(o), record_gone=rid not in w.records,
          docket_item_survives=bool(world_q.docketed(w, PARTY)),
          docket=[i.get('matter') for i in w.docket])
    o2 = U._fold(w, d, U._determine('dt'))
    log.w('result', section='world.w1.D_burn.determine_after_burn', events=kinds(o2),
          note='existing code: determine reads the DOCKET, never the case file, so burning the file does not stall the proceeding')
    if kinds(o2) == ['matter.determined'] or any(k == 'matter.determined' for k in kinds(o2)):
        log.w('fail', section='world.w1.D_burn', what='burning the case file does not stall anything in the existing code: determine still executes against the docket item',
              proposal_said="'a burnt, seized or orphaned file stalls the proceeding inside the world' (1); only true if P2 adds the stage_of read to determine's admission (its S4/S5), which is unbuilt",
              events=kinds(o2))
    # a next MATTER pass with the record gone: no crash
    try:
        _matter_tick(w, d, mint_token, WriteClass)
        log.w('null', section='world.w1.D_burn.matter', what='MATTER run after the case file is destroyed', how='ran d.matter on the world with the Record deleted', found='no exception, no term.matured for the dead id')
    except Exception as e:
        log.w('error', section='world.w1.D_burn.matter', type=type(e).__name__, message=str(e)[:300], traceback=traceback.format_exc())

    # E. forge: (i) the forge verb on the case file, (ii) create_record overwriting the existing id
    w, d, out, stages = fresh()
    o = U._fold(w, d, _act(Act, 'f1', 'forge', DUKE, subject=rid))
    log.w('result', section='world.w1.E_forge_verb', events=kinds(o),
          note='forge mints a NEW faction sheet with one false key (_eff_forge); it cannot alter an existing Record')
    if kinds(o) != ['record.forged']:
        log.w('fail', section='world.w1.E_forge_verb', what='the forge verb cannot forge a case file (it mints a faction sheet only)',
              proposal_said="'the file can be seized, forged or destroyed' (flowchart; 1 'burnt, seized or orphaned'; 8 Q2 'seizing, forging or burning'; 7 'it can be burnt, stolen and forged')", events=kinds(o))
    # the overwrite route
    fake = [(99, 'judgment', 'x')]
    for actor in ('p_other', 'p_low', DUKE):
        w, d, out, stages = fresh()
        o = U._fold(w, d, _act(Act, 'cr', 'create_record', actor, record=rid, kind='text', stages=fake))
        r2 = w.records.get(rid)
        changed = r2 is not None and [s[1] for s in r2.stages] == ['judgment']
        log.w('result', section='world.w1.E_create_record_overwrite', actor=actor, events=kinds(o), agenda_overwritten=changed,
              holds_on_file=[(t.subject, t.live) for t in w.tenures if t.object == rid and t.kind == 'hold'],
              stages_after=[s[1] for s in r2.stages] if r2 else None)
        if changed:
            log.w('fail', section='world.w1.E_create_record_overwrite', what=f'{actor} (not necessarily the holder) overwrote the case file\'s whole agenda with create_record naming the existing id; no seizure, no warrant, no seat',
                  proposal_said='P2 asks (8 Q2) whether procedure may be attacked through the file by seizing, forging or burning; it does not know the existing mint lets any person with create_record replace the agenda', actor=actor)

    # F. the file is in another person's hands (PLANTED precondition: `give` is refused across rungs, see F_give), then the Duke seizes it with a warrant
    w, d, out, stages = fresh()
    o = U._fold(w, d, _act(Act, 'gv', 'give', DUKE, via=None, subject=rid, to='p_low'))
    log.w('result', section='world.w1.F_give', events=kinds(o), holder_now=getattr(world_q.hold_force(w, rid), 'subject', None),
          note='give needs the receiver present where the giver is (verb_table give eligibility); tiny_world seats the Duke alone in S, so the verb is refused (first false start for F: kept)')
    from engine.season.state.carriers import Tenure
    for t in w.tenures:
        if t.object == rid and t.kind == 'hold' and t.live:
            t.until = w.tick
    w.add_tenure(Tenure('plant_hold_low', 'p_low', rid, 'hold', since=w.tick))
    log.w('result', section='world.w1.F_plant', holder_now=getattr(world_q.hold_force(w, rid), 'subject', None), note='hand-planted precondition, not a verb')
    S12._hold_document(w, w.persons[DUKE], 'dispensation', S12._warrant(rid), rec_id='rec_w')
    o = U._fold(w, d, _act(Act, 'sz', 'seize', DUKE, via=SEAT, subject=rid))
    log.w('result', section='world.w1.F_seize', events=kinds(o), holder_after=getattr(world_q.hold_force(w, rid), 'subject', None))
    seen = {}
    for _ in range(7):
        for e in _matter_tick(w, d, mint_token, WriteClass):
            if e.kind == 'term.matured' and any(c.subject == rid for c in e.changes):
                seen[w.tick - 1] = seen.get(w.tick - 1, 0) + 1
    log.w('result', section='world.w1.F_seize.after', matured_ticks=seen, note='a seized file keeps maturing under its new holder: seizure moves the hold (3.7 is right) but stops nothing; the agenda is the holder\'s, no bench reads who holds it')
    # P2 vs existing summary line
    log.w('result', section='world.w1.summary', text='existing code: MATTER matures only at due==tick and needs a live holder in w.persons; nothing pops the list; determine ignores the file; destroy_record removes it silently; create_record can replace it; seize moves the hold. P2 states the stall property as if it were the existing behaviour; it is true only for maturation, not for any act.')

    # w1b: the same on a REAL build_realm world
    try:
        w1b_realm(log, U, mint_token, WriteClass, Act, world_q)
    except Exception as e:
        log.w('error', section='world.w1b', type=type(e).__name__, message=str(e)[:300], traceback=traceback.format_exc())


def w1b_realm(log, U, mint_token, WriteClass, Act, world_q):
    from engine.season.harness.populated import build_realm
    from engine.season.loop.driver import SeasonDriver
    log.w('section_start', section='world.w1b', note='real build_realm(0): find an open_case-granting seat and a person in its purview')
    w = build_realm(0)
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    cand = []
    for t in w.tenures:
        if t.kind == 'hold' and t.live and 'determine' in (t.granted_acts or ()) and t.object in w.offices:
            off = w.offices[t.object]
            if t.subject in w.persons and off.scope_rung:
                cand.append((t.subject, off))
    log.w('result', section='world.w1b', seats_with_determine=len(cand), sample=[(p, o.post, o.scope_rung, o.faction) for p, o in cand[:8]])
    tried = 0
    for pid, off in cand:
        # a party inside the seat's purview: another person whose home is under scope_rung
        homes = world_q.home_of(w)
        anc = lambda r: set(world_q.ancestry(w, r)) if r else set()
        parties = [q for q in sorted(w.persons) if q != pid and off.scope_rung in anc(homes.get(q))]
        if not parties:
            continue
        party = parties[0]
        tried += 1
        stages = [(w.tick + i + 1, lab, 'ocr') for i, lab in enumerate(ROWS['K3_royal(6)'])]
        out = d.resolve(mint_token(w, WriteClass.ACTS), [Act(id='ocr', actor=pid, verb='open_case', via=off.id, payload={'subject': party, 'arrangement': 'legal_trial', 'stages': stages})],
                        contest_max_depth=w.fixtures.get('contest_max_depth'))
        w.log.extend(out)
        ks = [e.kind for e in out]
        log.w('result', section='world.w1b', seat=off.id, post=off.post, holder=pid, party=party, events=ks)
        if ks == ['case.opened']:
            rid = 'rec:ocr'
            rec = w.records.get(rid)
            log.w('result', section='world.w1b.open', record=rid, stages=[s[1] for s in rec.stages], holder=world_q.hold_force(w, rid).subject)
            # holder gone at stage 2's due tick
            seen = {}
            saved = None
            for step in range(6):
                if step == 2:
                    saved = w.persons.pop(pid)
                if step == 3:
                    w.persons[pid] = saved
                for e in _matter_tick(w, d, mint_token, WriteClass):
                    if e.kind == 'term.matured' and any(c.subject == rid for c in e.changes):
                        seen[w.tick - 1] = seen.get(w.tick - 1, 0) + 1
            log.w('result', section='world.w1b.holder_gap', matured_ticks=seen, stages_declared=len(stages),
                  note='on the real realm (a full tick of MATTER over 80+ persons): stage 2 (tick 2) is skipped while the holder is out and never matures')
            if 2 not in seen:
                log.w('fail', section='world.w1b.holder_gap', what='real-realm replication of the holder-gap: stage due at tick 2 never matures after the holder returns at tick 3', proposal_said='an empty bench halts the agenda; a seated one resumes it')
            # burn on the real realm
            o = d.resolve(mint_token(w, WriteClass.ACTS), [Act(id='burn', actor=pid, verb='destroy_record', via=None, payload={'subject': rid})],
                          contest_max_depth=w.fixtures.get('contest_max_depth'))
            log.w('result', section='world.w1b.burn', events=[e.kind for e in o], record_gone=rid not in w.records, docket_item_survives=bool(world_q.docketed(w, party)))
            break
        if tried >= 12:
            break
    if tried == 0:
        log.w('blocked', section='world.w1b', first_blocker='no seat with a determine grant had a party in purview in build_realm(0)')


def w2_forum_and_rows(log):
    U, S12, mint_token, WriteClass, Act, world_q = _imports()
    from engine.season.data.arrangements import ARRANGEMENTS
    kinds = U._kinds
    log.w('section_start', section='world.w2')
    log.w('claim', section='world.w2', where='P2 4 worked example 2; 3.5; 9b(3)',
          text='Partial keeps the treason case but docket-items "jurisdiction over this clerk" under the row appeal_basis names, and the trial waits at proof; two benches each hold an item about one man')
    # open under royal row; then a second open_case on the same matter under the church row
    for first, second in (('legal_trial', 'inquisition_hearing'), ('legal_trial', 'legal_trial'), ('tribunal', 'excommunication_deliberation')):
        w, d = U._world(**U.JUDGE)
        o1 = U._fold(w, d, U._open('a', arrangement=first))
        o2 = U._fold(w, d, U._open('b', arrangement=second))
        items = world_q.docketed(w, U.PARTY)
        log.w('result', section='world.w2.second_case_same_matter', first=first, second=second, ev1=kinds(o1), ev2=kinds(o2), docket_items_for_matter=len(items))
        if kinds(o2) == ['case.refused']:
            log.w('fail', section='world.w2.second_case_same_matter', what='a second open_case on a docketed matter is refused (case.refused); two benches cannot each hold an item about one man',
                  proposal_said='worked example 2 and 9b(3): the forum detour docket-items a second matter and two benches each hold an item', first=first, second=second)
    # the escape: dock the subsidiary question under a different matter id (the case file's id)
    w, d = U._world(**U.JUDGE)
    U._fold(w, d, U._open('a', arrangement='legal_trial'))
    rid = 'rec:a'
    o2 = U._fold(w, d, U._open('b', subject=rid, arrangement='inquisition_hearing'))
    log.w('result', section='world.w2.subsidiary_as_record_matter', events=kinds(o2), docket_matters=[i.get('matter') for i in w.docket])
    if kinds(o2) == ['case.opened']:
        o3 = U._fold(w, d, U._determine('dt', subject=rid))
        log.w('result', section='world.w2.subsidiary_as_record_matter.determine', events=kinds(o3),
              note='determine binds a PERSON (party cell); a Record matter docks (open_case accepts any id) but cannot be determined')
        if kinds(o3) != ['matter.determined']:
            log.w('fail', section='world.w2.subsidiary_as_record_matter', what='a subsidiary item docketed under a Record id is accepted by open_case but determine refuses it: the item is a wedge, never decided',
                  proposal_said='"writes a subsidiary docket item (referred; a question taken up)" (3.5)', events=kinds(o3))
    else:
        log.w('blocked', section='world.w2.subsidiary_as_record_matter', first_blocker='open_case refused a Record id as matter', events=kinds(o2))
    # wedge after determination (P2 says its transition ends it)
    w, d = U._world(**U.JUDGE)
    U._fold(w, d, U._open('a', arrangement='legal_trial'))
    od = U._fold(w, d, U._determine('d1'))
    o2 = U._fold(w, d, U._open('b', arrangement='legal_trial'))
    od2 = U._fold(w, d, U._determine('d2'))
    log.w('result', section='world.w2.reopen_wedge', determine1=kinds(od), reopen=kinds(o2), determine2=kinds(od2), docket_after=[i.get('matter') for i in w.docket],
          note='P2 3.6: its transition "also ends today\'s wedge, where a re-opened matter stays docketed forever (PROBE 2.3)"')
    if kinds(o2) == ['case.opened'] and kinds(od2) != ['matter.determined'] and any(i.get('matter') == U.PARTY for i in w.docket):
        log.w('result', section='world.w2.reopen_wedge', verdict='HELD', text='the wedge exists in the existing code: re-opened matter stays docketed, second determine does not execute (the claim of PROBE 2.3 is reproduced); P2\'s fix is unbuilt')
    # the eight rows
    rows = {}
    for name, row in sorted(ARRANGEMENTS.items()):
        w, d = U._world(**U.JUDGE)
        o = U._fold(w, d, U._open('a', arrangement=name))
        od = U._fold(w, d, U._determine('d')) if kinds(o) == ['case.opened'] else []
        rows[name] = dict(disposes=row['disposes'], open_case=kinds(o), determine=kinds(od))
        log.w('trial', section='world.w2.eight_rows', row=name, n=1, **rows[name])
    refused = [r for r, v in rows.items() if v['open_case'] != ['case.opened']]
    log.w('result', section='world.w2.eight_rows.summary', rows=len(rows), open_case_refused=refused,
          note='parliamentary_debate and council_of_state dispose a Record: open_case declines them up front (_eff_open_case), so P2\'s K6 [admit, licence] cannot be opened by the case-file route that winds its stages')
    if refused:
        log.w('fail', section='world.w2.eight_rows', what=f'open_case refuses {refused} (disposes: Record), so the case-file agenda P2 hangs K6 on cannot be created for a parliament',
              proposal_said='K6 parliament row [admit, licence] with the case file as the carrier (4, 3.1)')
    # S1-style extremes on the real fold
    for nm, kw in (('unknown_row', dict(arrangement='no_such_row')), ('list_row', dict(arrangement=['x'])), ('missing_party', dict(subject=None)),
                   ('empty_stages', dict(stages=[])), ('nan_due_stage', dict(stages=[(float('nan'), 'admit', 'a')])), ('neg_due_stage', dict(stages=[(-5, 'admit', 'a')])),
                   ('50_stages', dict(stages=[(i + 1, 'proof', 'a') for i in range(50)]))):
        w, d = U._world(**U.JUDGE)
        try:
            kw2 = dict(kw)
            subj = kw2.pop('subject', U.PARTY)
            if 'subject' in kw:
                act = Act(id='a', actor=U.DUKE, verb='open_case', via=U.SEAT, payload=kw2)
            else:
                act = U._open('a', **kw2)
            o = U._fold(w, d, act)
            rec = w.records.get('rec:a')
            log.w('trial', section='world.w2.real_extremes', case=nm, n=1, events=kinds(o), record_stages=(len(rec.stages) if rec else None))
        except Exception as e:
            log.w('error', section='world.w2.real_extremes', case=nm, type=type(e).__name__, message=str(e)[:300], traceback=traceback.format_exc())


def w3_failures(log):
    U, S12, mint_token, WriteClass, Act, world_q = _imports()
    kinds = U._kinds
    log.w('section_start', section='world.w3')
    log.w('claim', section='world.w3', where='P2 9a(S), R breaks at one extreme', text='a stage with no seated decider wedges until its file matures (lapse, R-1); an empty bench halts the agenda; a seated one resumes it')
    # judge's seat revoked / judge gone / bench vacated
    for variant in ('seat_hold_closed', 'judge_deleted', 'control'):
        w, d = U._world(**U.JUDGE)
        U._fold(w, d, U._open('a', arrangement='legal_trial', stages=[(1, 'proof', 'a'), (2, 'judgment', 'a')]))
        if variant == 'seat_hold_closed':
            for t in w.tenures:
                if t.kind == 'hold' and t.object == U.SEAT and t.live:
                    t.until = w.tick
        elif variant == 'judge_deleted':
            w.persons.pop(U.DUKE)
        bench = world_q.judging_set(w, 'Hh')
        try:
            od = U._fold(w, d, U._determine('d1'))
            ev = kinds(od)
        except Exception as e:
            ev = ['EXC:' + type(e).__name__ + ':' + str(e)[:120]]
            log.w('error', section='world.w3', variant=variant, type=type(e).__name__, message=str(e)[:300], traceback=traceback.format_exc())
        # let the file mature to its end, then see whether the docket item lapses
        for _ in range(6):
            try:
                _matter_tick(w, d, mint_token, WriteClass)
            except Exception as e:
                log.w('error', section='world.w3.matter', variant=variant, type=type(e).__name__, message=str(e)[:300], traceback=traceback.format_exc())
                break
        still = bool(world_q.docketed(w, U.PARTY))
        rec = w.records.get('rec:a')
        log.w('result', section='world.w3.injection', variant=variant, bench=bench, determine=ev, docket_item_after_6_ticks=still,
              file_matured_flag=getattr(rec, 'matured', None), stages=[s[1] for s in rec.stages] if rec else None)
        if variant != 'control' and still:
            log.w('fail', section='world.w3.injection', what=f'{variant}: the docket item is still there 6 ticks after the file matured; nothing lapses a docketed matter',
                  proposal_said="'lapse when the file matures open (R-1)' (4 K4 row; 9a R): a lapse is claimed as the end of a wedged stage", variant=variant)
    log.w('unverified', section='world.w3', what='the lapse itself (docket item removed when the case file matures open)', why='no code reads Record.matured to remove a DocketItem; P2 builds no lapse reader in S1-S8 either')
    # party with no capability: pool default 2 vs ceiling 2 -> degrees
    from engine.season.data.fixtures import DEFAULT_FIXTURES
    w, d = U._world()          # shipped pool_default 2
    U._fold(w, d, U._open('a', arrangement='legal_trial'))
    ks = Counter()
    for i in range(60):
        w2, d2 = U._world()
        U._fold(w2, d2, U._open('a', arrangement='legal_trial'))
        ks[tuple(kinds(U._fold(w2, d2, U._determine(f'd{i}'))))] += 1
    n = sum(ks.values())
    k_ok = sum(v for kk, v in ks.items() if kk == ('matter.determined',))
    log.w('batch', section='world.w3.no_capability_determine', n=n, determined=k_ok, ci95=list(wilson(k_ok, n)), by_outcome={str(k): v for k, v in ks.items()},
          note='shipped pool_default 2 judge vs obstacle default 2: the act ids differ per trial so the keyed draw differs; this is the live determine success rate for an uncapable judge')


def s2_proxy(log):
    """P2's S2 (AR's draw: continuous pool, producers, aptness) is unbuilt. PROXY (my model of its effect): sweep the shipped fixture
    `pool_default` (the one input every computed roll reads) and compare the one-season content hash with the pin. If a pool change moves the
    pinned one-season hash, S2 (which changes the pool of every computed roll) moves it too, and P2's list of hashes that move (S4 only) is short."""
    from engine.season.harness.populated import (build_realm, make_chooser, SeasonDriver, resolvable_verbs, H, draw_factory, P)
    log.w('section_start', section='world.s2_proxy', claim="P2 6: S4 'Re-pins BASE_HASHES and the per-seed BASE content hashes'; S2 is listed as moving nothing (no re-pin in its row)", where='P2 6 rows S2, S4; 9c; comparison 4 ("S2 moves every computed roll")')
    PIN = '873525dfb363231695cefb17ad4b17a1'
    for lbl, kv in (('control_shipped', {}), ('pool_default_3', {'pool_default': 3}), ('pool_default_5', {'pool_default': 5})):
        t = time.time()
        w = build_realm(0)
        for k, v in kv.items():
            w.fixtures = w.fixtures.sweep(k, v)
        d = SeasonDriver(w)
        mint = lambda pid, verb, subj, w=w: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
        ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(), draw=draw_factory(w.world_seed, lambda w=w: w.tick))
        d.season(ch, question=None, subsistence=P.SUBSIST, contest_max_depth=w.fixtures.get('contest_max_depth'))
        h = w.content_hash()
        log.w('trial', section='world.s2_proxy', arm=lbl, n=1, hash=h, equals_pin=h == PIN, log_events=len(w.log), wall_s=round(time.time() - t, 1))
        if lbl != 'control_shipped' and h != PIN:
            log.w('result', section='world.s2_proxy', arm=lbl, text='a pool change moves the pinned one-season seed-0 hash; S2 (continuous pool per person) would therefore re-pin BASE_HASHES[1] and the go07 BASE entries too, not only S4')
        if lbl == 'control_shipped' and h != PIN:
            log.w('fail', section='world.s2_proxy', what='control arm does not reproduce the pin: the proxy is not interpretable', hash=h)


def w4_realm_data(log, end):
    from engine.season.harness.populated import build_realm
    from engine.season.queries import world_q
    from engine.season.data.verbs import VERB_TABLE
    log.w('section_start', section='world.w4', claim="the King and Queen sit on every bench (AR I item 7; world_q.py:566, walk at :636-642); a church bench reaches only venues inside T9; stage_of plus decider_basis gives judging_set the filter it lacks (P2 3.4)")
    for seed in (0, 1, 2):
        if time.time() > end:
            log.w('skipped', section='world.w4', what=f'seed {seed}', why='wall-clock budget')
            continue
        t = time.time()
        w = build_realm(seed)
        # live seats granting determine
        seats = []
        for tn in w.tenures:
            if tn.kind == 'hold' and tn.live and 'determine' in (tn.granted_acts or ()) and tn.object in w.offices:
                off = w.offices[tn.object]
                seats.append(dict(holder=tn.subject, in_world=tn.subject in w.persons, post=off.post, faction=off.faction, scope=off.scope_rung, rung=off.rung))
        by_fac = Counter(s['faction'] for s in seats)
        posts = Counter(s['post'] for s in seats)
        log.w('result', section='world.w4.seats', seed=seed, determine_seats=len(seats), by_faction=dict(by_fac), by_post=dict(posts),
              unseated=sum(1 for s in seats if not s['in_world']))
        # bench reach per rung kind
        reach = defaultdict(Counter)
        kingq = Counter()
        church_only = Counter()
        mixed = Counter()
        for rid, r in w.rungs.items():
            if r.kind in ('person',):
                continue
            ids = world_q.judging_set(w, rid)
            reach[r.kind][len(ids)] += 1
            facs = set()
            for pid in ids:
                for tn in w.tenures:
                    if tn.kind == 'hold' and tn.live and tn.subject == pid and tn.object in w.offices and 'determine' in (tn.granted_acts or ()):
                        facs.add(w.offices[tn.object].faction)
            if ids and any(w.offices[tn.object].post in ('King', 'Queen') for tn in w.tenures if tn.kind == 'hold' and tn.live and tn.subject in ids and tn.object in w.offices):
                kingq[r.kind] += 1
            if ids:
                (church_only if facs and all('Church' in str(f) for f in facs) else mixed)[r.kind] += 1
        nonempty = {k: sum(v for n, v in c.items() if n > 0) for k, c in reach.items()}
        tot = {k: sum(c.values()) for k, c in reach.items()}
        log.w('result', section='world.w4.bench_reach', seed=seed, rung_totals=tot, rungs_with_nonempty_bench=nonempty,
              empty_bench_share={k: round(1 - nonempty[k] / tot[k], 4) for k in tot},
              bench_size_hist={k: dict(sorted(c.items())) for k, c in reach.items()},
              benches_containing_king_or_queen=dict(kingq), benches_church_only=dict(church_only), benches_mixed_authority=dict(mixed),
              build_s=round(time.time() - t, 2))
        n_ben = sum(nonempty.values())
        n_kq = sum(kingq.values())
        log.w('result', section='world.w4.king_on_every_bench', seed=seed, nonempty_benches=n_ben, with_king_or_queen=n_kq,
              share=round(n_kq / n_ben, 4) if n_ben else None, ci95=list(wilson(n_kq, n_ben)),
              note='AR I item 7: judging_set has no authority filter; P2 claims stage_of + decider_basis repairs it. This counts how far the filter would have to reach.')
        # case-opening seats: eligibility remit:determine ~ determine grant; open_case seat reach to persons
        homes = world_q.home_of(w)
        covered = Counter()
        for pid in w.persons:
            h = homes.get(pid)
            if h is None:
                covered['no_home'] += 1
                continue
            covered['reachable_by_bench' if world_q.judging_set(w, h) else 'no_bench_over_home'] += 1
        log.w('result', section='world.w4.person_reach', seed=seed, persons=len(w.persons), **dict(covered),
              note='a person is a possible respondent only if some determine seat sits over his home; share with no bench = persons no staged row can try')
        # church reach: church-faction determine seats and the rungs they sit over
        church_rungs = set()
        for rid, r in w.rungs.items():
            for pid in world_q.judging_set(w, rid):
                for tn in w.tenures:
                    if tn.kind == 'hold' and tn.live and tn.subject == pid and tn.object in w.offices and 'Church' in str(w.offices[tn.object].faction) and 'determine' in (tn.granted_acts or ()):
                        church_rungs.add(rid)
        log.w('result', section='world.w4.church_reach', seed=seed, church_bench_rungs=len(church_rungs), sample=sorted(church_rungs)[:6])
        # case files present at build
        log.w('result', section='world.w4.case_files_at_build', seed=seed, records=len(w.records), kinds=dict(Counter(r.kind for r in w.records.values())),
              docket=len(w.docket), note='no case file exists at build; stages on records at build belong to planned_works')
    log.w('result', section='world.w4.eligibility', open_case=VERB_TABLE['open_case'].eligibility, determine=VERB_TABLE['determine'].eligibility,
          note='open_case and determine share eligibility remit:determine, so the opener seat and the closer seat are one grant: P2\'s separation of an accusing seat (admit) from the bench needs a grant that does not exist')


def w5_seasons(log, end):
    from engine.season.harness.populated import (build_realm, make_chooser, SeasonDriver, resolvable_verbs, H, draw_factory, P)
    log.w('section_start', section='world.w5', claim="Falsifier (P2 7): 'S8's count of case files whose head moved, over three seeds'; S7 determinism; S1 wall time")
    out = {}
    for seed in (0, 1, 2):
        if time.time() > end:
            log.w('skipped', section='world.w5', what=f'seed {seed}', why='wall-clock budget')
            continue
        w = build_realm(seed)
        d = SeasonDriver(w)
        mint = lambda pid, verb, subj, w=w: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
        ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(), draw=draw_factory(w.world_seed, lambda w=w: w.tick))
        for s in range(2):
            if time.time() > end:
                log.w('skipped', section='world.w5', what=f'seed {seed} season {s + 1}', why='wall-clock budget')
                break
            before = Counter(e.kind for e in w.log)
            t = time.time()
            try:
                d.season(ch, question=None, subsistence=P.SUBSIST, contest_max_depth=w.fixtures.get('contest_max_depth'))
            except Exception as e:
                log.w('error', section='world.w5', seed=seed, season=s + 1, type=type(e).__name__, message=str(e)[:300], traceback=traceback.format_exc())
                break
            after = Counter(e.kind for e in w.log)
            dk = {k: after[k] - before.get(k, 0) for k in after if k in ('case.opened', 'case.refused', 'matter.determined', 'matter.undetermined', 'determine.refused', 'petition.carried', 'carry.refused', 'term.matured', 'record.created', 'commitment.made')}
            casefiles = [r for r in w.records.values() if r.kind == 'text' and r.stages and all(isinstance(x, tuple) and str(x[1]).startswith('stage') for x in r.stages)]
            docket_filled = [i for i in w.docket if i.get('matter') is not None]
            log.w('trial', section='world.w5.season', seed=seed, season=s + 1, n=1, wall_s=round(time.time() - t, 2), events_delta=dk,
                  h80_text_records=len(casefiles), docket=len(w.docket), docket_filled=len(docket_filled),
                  docket_arrangements=dict(Counter(str(i.get('arrangement')) for i in w.docket)), content_hash=w.content_hash())
            out[(seed, s + 1)] = (w.content_hash(), dk)
    # falsifier count
    opened = sum(v[1].get('case.opened', 0) for v in out.values())
    determined = sum(v[1].get('matter.determined', 0) + v[1].get('matter.undetermined', 0) for v in out.values())
    log.w('result', section='world.w5.falsifier', seed_seasons=len(out), case_opened_total=opened, determine_executed_total=determined,
          case_files_whose_head_moved_by_a_closing_act=0 if determined == 0 else 'see determine_executed_total',
          note='P2 7 falsifier: "if computed play cannot carry a case past two stages in a season, every staged row is a dead seat". Computed play opened %d cases and executed determine %d times in these runs; the head-moving act (determine) is the one that never fires' % (opened, determined))
    if determined == 0:
        log.w('fail', section='world.w5.falsifier', what='P2\'s own falsifier is met: computed play on three seeds closes no stage (determine/undetermine executed 0 times)', proposal_said='S8: a computed season moves one case file across two stages', seeds=3,
              seasons_each=2, opened=opened)
    # pinned control: seed 0 season 1 hash equals the repo's BASE_HASHES[1]
    if (0, 1) in out:
        pin = '873525dfb363231695cefb17ad4b17a1'
        log.w('result', section='world.w5.pin_control', seed0_season1_hash=out[(0, 1)][0], BASE_hash_in_test_go07_seed0_new=pin, equal=out[(0, 1)][0] == pin)
    # determinism: seed 0 season 1 again, a fresh process state not available; same process twice
    if time.time() < end:
        w = build_realm(0)
        d = SeasonDriver(w)
        mint = lambda pid, verb, subj, w=w: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
        ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(), draw=draw_factory(w.world_seed, lambda w=w: w.tick))
        t = time.time()
        d.season(ch, question=None, subsistence=P.SUBSIST, contest_max_depth=w.fixtures.get('contest_max_depth'))
        h2 = w.content_hash()
        log.w('result', section='world.w5.determinism', run=2, hash=h2, equals_run1=h2 == out.get((0, 1), (None,))[0], wall_s=round(time.time() - t, 2),
              note='same seed twice in one process; across processes the pinned BASE value is the control (above)')
    log.w('skipped', section='world.w5.large_realm', what='a large realm', why='build_realm has only `cap` (smaller) and a fixed roster of 81-83 persons; no larger realm exists to build (populated.py build_realm docstring)')


# ---------------------------------------------------------------------------------------------- batches section
BATCH_FILES = [
    # kernel dependants (grep of the repo for systems.social_contest.sim.contest / sim/contest)
    'engine/tests/test_contest_kernel.py',
    'engine/tests/test_sigma_leverage_parity.py',
    'engine/season/tests/test_social_contest_module.py',
    'engine/season/tests/test_sc01_obstacle_ceiling.py',
    'tests/valoria/test_import_cycle_game_state_npe.py',
    'tests/valoria/test_engine_does_not_import_systems.py',
    'tests/valoria/test_band_extension_seam.py',
    'tests/valoria/test_tn7_always.py',
    'tests/valoria/test_balance_oracle_arms.py',
    'tests/valoria/test_structure_audit.py',
    'tests/valoria/test_degree_ladder_single_owner.py',
    # ladder fallback / contest extension / arrangements keys / case-file labels
    'engine/season/tests/test_arrangements.py',
    'engine/season/tests/test_u7_remit.py',
    'engine/season/tests/test_sc01_fired_slot.py',
    'engine/season/tests/test_in45_carry.py',
]
HASH_TESTS = [
    'engine/season/tests/test_season_weather.py::test_in21_control_draw_off_and_draw_at_one_reproduce_the_base_hashes',
    'engine/season/tests/test_go07_canonical_digest.py::test_go07_control_the_world_did_not_move_only_its_digest',
]


def _pytest(log, wt, files, label, timeout=420):
    res = {}
    for f in files:
        if not os.path.exists(os.path.join(wt, f.split('::')[0])):
            res[f] = dict(rc='missing')
            log.w('trial', section='batches.pytest', label=label, file=f, n=1, rc='missing', note='file does not exist in the worktree at this stage')
            continue
        t = time.time()
        try:
            p = subprocess.run([sys.executable, '-m', 'pytest', f, '-q', '-p', 'no:cacheprovider', '--no-header', '-W', 'ignore'], cwd=wt,
                               capture_output=True, text=True, timeout=timeout, env={**os.environ, 'PYTHONPATH': wt, 'PYTHONHASHSEED': '0'})
            tail = p.stdout.strip().splitlines()[-6:]
            summ = next((l for l in reversed(p.stdout.strip().splitlines()) if ' passed' in l or ' failed' in l or ' error' in l or 'no tests ran' in l), '')
            res[f] = dict(rc=p.returncode, summary=summ)
            log.w('trial', section='batches.pytest', label=label, file=f, n=1, rc=p.returncode, summary=summ, wall_s=round(time.time() - t, 1), tail=tail,
                  first_failure=[l for l in p.stdout.splitlines() if l.startswith('FAILED') or l.startswith('ERROR')][:3])
        except subprocess.TimeoutExpired:
            res[f] = dict(rc='timeout')
            log.w('error', section='batches.pytest', label=label, file=f, type='TimeoutExpired', message=f'>{timeout}s', traceback='')
    return res


def _sh(wt, *a):
    return subprocess.run(list(a), cwd=wt, capture_output=True, text=True)


def batch_main(log, budget_s):
    wt = WT
    t0 = time.time()
    log.w('plan', section='batches', worktree=wt, note="P2 section 6: S1 = deletions: (a) kernel systems/social_contest/sim/contest/ (b) ladder.degree_ladder fallback (c) contest() unread `extension` "
          "(d) H-80 placeholder labels on case files (e) records_dissent and venue_min_rank keys folded away. Each applied cumulatively in the scratch worktree; tests run per file; baseline first. "
          "Then (g) the S4 `case` docket key and the pinned hashes.", files=BATCH_FILES, hash_tests=HASH_TESTS)
    if not os.path.isdir(wt):
        log.w('blocked', section='batches', first_blocker=f'{wt} does not exist (git worktree add)')
        return
    log.w('result', section='batches.worktree', head=_sh(wt, 'git', 'rev-parse', 'HEAD').stdout.strip(), status=_sh(wt, 'git', 'status', '--short').stdout[:300])
    log.w('skipped', section='batches', what='engine/season/tests/test_season_shape.py', why='first attempt included it (a grep hit); it is a 15,000-line season-shape suite that only mentions the kernel path in a comment (line 15021) and ran >7 min on a shared machine at load 9; killed and removed from the list. The killed attempt\'s baseline results for the first 2 files are in the log above')
    base = _pytest(log, wt, BATCH_FILES + HASH_TESTS, 'baseline')
    bad = {k: v for k, v in base.items() if v.get('rc') not in (0,)}
    log.w('result', section='batches.baseline', red_before_any_change=bad, note='pre-existing reds are subtracted from every later count')
    # (a) the kernel
    r = _sh(wt, 'git', 'rm', '-r', '-q', 'systems/social_contest/sim/contest')
    log.w('result', section='batches.S1a_kernel_delete', rc=r.returncode, err=r.stderr[:200], files_removed=_sh(wt, 'git', 'status', '--short').stdout.count('\nD ') + 1)
    ra = _pytest(log, wt, BATCH_FILES, 'after_S1a_kernel')
    broke_a = {k: v for k, v in ra.items() if v.get('rc') not in (0, 'missing') and base.get(k, {}).get('rc') in (0,)}
    log.w('result', section='batches.S1a', newly_red=broke_a, newly_missing=[k for k, v in ra.items() if v.get('rc') == 'missing'])
    for k, v in broke_a.items():
        log.w('fail', section='batches.S1a', what=f'{k} goes red after the kernel deletion', proposal_said="S1: 'suite green with fewer files' (6); the comparison and the code audit say the dependants are 9 files", result=v)
    # sim_params / value_pointer_links / module_contracts pointers (no edit made): do their exporters' --check still pass?
    for cmd in (['python', 'tools/export_sim_params.py', '--check'], ['python', 'tools/export_engine_params.py', '--check']):
        if os.path.exists(os.path.join(wt, cmd[1])):
            p = subprocess.run(cmd, cwd=wt, capture_output=True, text=True, env={**os.environ, 'PYTHONPATH': wt})
            log.w('trial', section='batches.S1a.exporters', cmd=' '.join(cmd), n=1, rc=p.returncode, tail=(p.stdout + p.stderr).strip().splitlines()[-4:])
        else:
            log.w('skipped', section='batches.S1a.exporters', what=' '.join(cmd), why='tool absent in the worktree')
    # (b) ladder fallback and (c) extension
    p1 = os.path.join(wt, 'engine/season/seam/ladder.py')
    s = open(p1).read()
    old = """    global _LADDER, _LADDER_ERROR
    if _LADDER is not None or _LADDER_ERROR:
        return _LADDER
    root = files.REPO_ROOT
    try:
        if str(root) not in sys.path:
            sys.path.insert(0, str(root))
        from engine.dice_engine.dice_engine import (  # noqa: E402
            DEGREE_LABEL as _L, degree_from_net as _d)
        _LADDER = (_d, _L)
        return _LADDER
    except Exception as e:                        # a real import failure is a NAMED gap
        _LADDER_ERROR = f"{type(e).__name__}: {e}"
        return None
"""
    new = """    global _LADDER
    if _LADDER is None:
        from engine.dice_engine.dice_engine import DEGREE_LABEL as _L, degree_from_net as _d
        _LADDER = (_d, _L)
    return _LADDER
"""
    if old in s:
        open(p1, 'w').write(s.replace(old, new))
        log.w('result', section='batches.S1b_ladder_fallback', applied=True)
    else:
        log.w('blocked', section='batches.S1b_ladder_fallback', first_blocker='engine/season/seam/ladder.py:108-128 text did not match the patch anchor')
    p2 = os.path.join(wt, 'engine/season/seam/contest.py')
    s = open(p2).read()
    old2 = "            extension: Optional[Callable[[str], bool]] = None,\n"
    if old2 in s:
        open(p2, 'w').write(s.replace(old2, ""))
        log.w('result', section='batches.S1c_contest_extension', applied=True)
    else:
        log.w('blocked', section='batches.S1c_contest_extension', first_blocker='engine/season/seam/contest.py:184 anchor not found')
    FILES_LADDER = [f for f in BATCH_FILES if any(k in f for k in ('degree_ladder', 'band_extension', 'sc01_obstacle', 'social_contest_module', 'u7_remit', 'sigma_leverage_parity'))]
    rb = _pytest(log, wt, FILES_LADDER, 'after_S1bc')
    rb = {**{k: v for k, v in ra.items() if k not in rb}, **rb}
    broke_b = {k: v for k, v in rb.items() if v.get('rc') not in (0, 'missing') and ra.get(k, {}).get('rc') in (0,)}
    log.w('result', section='batches.S1bc', newly_red_vs_after_S1a=broke_b)
    for k, v in broke_b.items():
        log.w('fail', section='batches.S1bc', what=f'{k} goes red after deleting the degree_ladder fallback and the contest() extension parameter', result=v)
    # (d) H-80 placeholder labels on case files: open_case mints with no stages
    p3 = os.path.join(wt, 'engine/season/loop/effects_information.py')
    s = open(p3).read()
    old3 = 'def _mint_document(w: "World", a: "Act", kind: str, content, rung: str,\n                   forgery_quality: int = 0) -> Change:'
    new3 = 'def _mint_document(w: "World", a: "Act", kind: str, content, rung: str,\n                   forgery_quality: int = 0, stages=None) -> Change:'
    old3b = "    rec = Record(rid, rung, kind, subject_matter=content, stages=_declared_stages(w, a),\n"
    new3b = "    rec = Record(rid, rung, kind, subject_matter=content, stages=(_declared_stages(w, a) if stages is None else stages),\n"
    old3c = '    made = _mint_document(w, a, "text", None, _seat_rung(w, a))\n\n    def perform() -> None:\n        made.apply()\n        slot = slot_for(w, matter)'
    new3c = '    made = _mint_document(w, a, "text", None, _seat_rung(w, a), stages=list((a.payload or {}).get("stages") or []) if isinstance(a.payload, dict) else [])\n\n    def perform() -> None:\n        made.apply()\n        slot = slot_for(w, matter)'
    if old3 in s and old3b in s and old3c in s:
        open(p3, 'w').write(s.replace(old3, new3).replace(old3b, new3b).replace(old3c, new3c))
        log.w('result', section='batches.S1d_h80_labels', applied=True, what="open_case mints its case file with NO default H-80 stages (an act's declared stages still wind)")
    else:
        log.w('blocked', section='batches.S1d_h80_labels', first_blocker='effects_information.py:_mint_document / _eff_open_case anchors not found')
    FILES_CASE = [f for f in BATCH_FILES if any(k in f for k in ('u7_remit', 'fired_slot', 'in45_carry'))]
    rc_ = _pytest(log, wt, FILES_CASE + HASH_TESTS, 'after_S1d_h80')
    rc_ = {**{k: v for k, v in rb.items() if k not in rc_}, **rc_}
    broke_c = {k: v for k, v in rc_.items() if v.get('rc') not in (0, 'missing') and rb.get(k, {}).get('rc') in (0, None)}
    log.w('result', section='batches.S1d', newly_red_vs_after_S1bc=broke_c)
    for k, v in broke_c.items():
        log.w('fail', section='batches.S1d', what=f'{k} goes red after deleting the H-80 placeholder labels from open_case case files', result=v)
    # (e) records_dissent and venue_min_rank
    import re
    pa = os.path.join(wt, 'engine/season/arrangements.yaml')
    pl = os.path.join(wt, 'engine/season/data/arrangements.py')
    sy = open(pa).read()
    sy2 = re.sub(r'^\s+(records_dissent|venue_min_rank):.*\n', '', sy, flags=re.M)
    sl = open(pl).read()
    sl2 = sl.replace('"id", "disposal", "bench_basis", "floor", "records_dissent", "venue_min_rank",', '"id", "disposal", "bench_basis", "floor",')
    sl2 = re.sub(r'    records_dissent = need\("records_dissent"\)\n    if not isinstance\(records_dissent, bool\):\n(?:.*\n){0,2}?    venue_min_rank = need\("venue_min_rank"\)\n    _refuse_not_in\(name, "venue_min_rank".*\n(?:.*\n){0,1}?', '', sl2)
    sl2 = sl2.replace('"records_dissent": records_dissent,\n        "venue_min_rank": venue_min_rank, ', '')
    if sy2 != sy and sl2 != sl:
        open(pa, 'w').write(sy2)
        open(pl, 'w').write(sl2)
        chk = subprocess.run([sys.executable, '-c', 'from engine.season.data.arrangements import ARRANGEMENTS; print(len(ARRANGEMENTS))'], cwd=wt, capture_output=True, text=True, env={**os.environ, 'PYTHONPATH': wt})
        log.w('result', section='batches.S1e_keys', applied=True, loader_import_rc=chk.returncode, out=chk.stdout.strip()[-80:], err=chk.stderr.strip()[-300:])
        if chk.returncode != 0:
            log.w('fail', section='batches.S1e_keys', what='a mechanical removal of records_dissent and venue_min_rank from the loader and the eight rows leaves the loader unimportable; the fold into disposal_reach / admit gate is a repoint, not a deletion',
                  err=chk.stderr.strip()[-300:])
    else:
        log.w('blocked', section='batches.S1e_keys', first_blocker='regex patch did not change arrangements.yaml or data/arrangements.py')
    FILES_ARR = [f for f in BATCH_FILES if any(k in f for k in ('arrangements', 'u7_remit'))]
    re_ = _pytest(log, wt, FILES_ARR, 'after_S1e_keys')
    re_ = {**{k: v for k, v in rc_.items() if k not in re_}, **re_}
    broke_e = {k: v for k, v in re_.items() if v.get('rc') not in (0, 'missing') and rc_.get(k, {}).get('rc') in (0, None)}
    log.w('result', section='batches.S1e', newly_red_vs_after_S1d=broke_e)
    for k, v in broke_e.items():
        log.w('fail', section='batches.S1e', what=f'{k} goes red after removing records_dissent and venue_min_rank', result=v)
    all_red = {k for step in (ra, rb, rc_, re_) for k, v in step.items() if v.get('rc') not in (0, 'missing')}
    base_red = {k for k, v in base.items() if v.get('rc') not in (0,)}
    log.w('result', section='batches.S1.summary', files_run=len(BATCH_FILES), red_baseline=sorted(base_red), red_after_any_S1_step=sorted(all_red), newly_red=sorted(all_red - base_red),
          proposal_said='S1 suite green with fewer files; one FORK: row per deletion', note='only the named files were run; the full suite was not (brief)')
    # (g) S4: the `case` docket key; pinned hashes
    s = open(p3).read()
    old4 = '    return {"date": date, "matter": matter,\n            DOCKET_ARRANGEMENT: arrangement, DOCKET_PETITION: petition}'
    new4 = '    return {"date": date, "matter": matter,\n            DOCKET_ARRANGEMENT: arrangement, DOCKET_PETITION: petition, "case": None}'
    if old4 in s:
        open(p3, 'w').write(s.replace(old4, new4))
        log.w('result', section='batches.S4_case_key', applied=True, what='_docket_item gains one key `case` (None for computed play, as arrangement is)')
        rh = _pytest(log, wt, HASH_TESTS, 'after_S4_case_key', timeout=1500)
        moved = {k: v for k, v in rh.items() if v.get('rc') not in (0,)}
        log.w('result', section='batches.S4_case_key.hashes', red=moved,
              proposal_said="S4 'Re-pins BASE_HASHES (test_season_weather.py:378-380) and the per-seed BASE content hashes (test_go07_canonical_digest.py:469-481)' (6); 'the pinned season hashes in S4's row move once, as SC-03a's two docket keys moved them' (9c)")
        for k, v in rh.items():
            if v.get('rc') == 0:
                log.w('fail', section='batches.S4_case_key.hashes', what=f'{k} still PASSES with the new `case` docket key: the key does not move that pin', proposal_said='the S4 key moves BASE_HASHES and BASE', result=v)
    else:
        log.w('blocked', section='batches.S4_case_key', first_blocker='_docket_item text not found at effects_information.py')
    log.w('summary', section='batches', wall_s=round(time.time() - t0, 1), stop='all steps finished')


def batch_followup(log, budget_s):
    """FOLLOW-UP to the first batches run, which had a defect of MINE: its S1e regex patch left arrangements.py with an IndentationError (line 174),
    so S1e's result and the S4 hash result that ran after it on the same tree are invalid. Here each step is applied ALONE to a reset scratch worktree."""
    wt = WT
    t0 = time.time()
    log.w('error', section='batches.attempt1', type='HarnessDefect', message='attempt 1 S1e regex patch broke data/arrangements.py (IndentationError at line 174: a dangling `repr_fn=list)`); S1e and S4 results of attempt 1 are INVALID and are redone below, each step alone on a reset worktree',
          traceback='see batches.S1e_keys in attempt 1: loader_import_rc 1')
    def reset():
        r1 = _sh(wt, 'git', 'reset', '-q', '--hard', 'HEAD')
        return r1.returncode
    def tail_of(files):
        out = {}
        for f in files:
            p = subprocess.run([sys.executable, '-m', 'pytest', f, '-q', '-p', 'no:cacheprovider', '--no-header', '--tb=short', '-W', 'ignore'], cwd=wt, capture_output=True, text=True,
                               timeout=420, env={**os.environ, 'PYTHONPATH': wt, 'PYTHONHASHSEED': '0'})
            summ = next((l for l in reversed(p.stdout.strip().splitlines()) if ' passed' in l or ' failed' in l or ' error' in l), '')
            msgs = [l for l in p.stdout.splitlines() if l.startswith('E ')][:4]
            out[f] = dict(rc=p.returncode, summary=summ, first_errors=[m[:260] for m in msgs])
            log.w('trial', section='batches2.pytest', file=f, n=1, **out[f])
        return out
    p3 = os.path.join(wt, 'engine/season/loop/effects_information.py')
    # --- S1d alone
    log.w('result', section='batches2.reset', rc=reset(), head=_sh(wt, 'git', 'rev-parse', 'HEAD').stdout.strip())
    s = open(p3).read()
    old3 = 'def _mint_document(w: "World", a: "Act", kind: str, content, rung: str,\n                   forgery_quality: int = 0) -> Change:'
    new3 = 'def _mint_document(w: "World", a: "Act", kind: str, content, rung: str,\n                   forgery_quality: int = 0, stages=None) -> Change:'
    old3b = "    rec = Record(rid, rung, kind, subject_matter=content, stages=_declared_stages(w, a),\n"
    new3b = "    rec = Record(rid, rung, kind, subject_matter=content, stages=(_declared_stages(w, a) if stages is None else stages),\n"
    old3c = '    made = _mint_document(w, a, "text", None, _seat_rung(w, a))\n\n    def perform() -> None:\n        made.apply()\n        slot = slot_for(w, matter)'
    new3c = '    made = _mint_document(w, a, "text", None, _seat_rung(w, a), stages=list((a.payload or {}).get("stages") or []) if isinstance(a.payload, dict) else [])\n\n    def perform() -> None:\n        made.apply()\n        slot = slot_for(w, matter)'
    if old3 in s and old3b in s and old3c in s:
        open(p3, 'w').write(s.replace(old3, new3).replace(old3b, new3b).replace(old3c, new3c))
        log.w('result', section='batches2.S1d_alone', applied=True)
        r = tail_of(['engine/season/tests/test_u7_remit.py::test_19_open_case_puts_the_matter_on_the_docket_and_the_reader_now_sees_it',
                     'engine/season/tests/test_season_weather.py::test_in21_control_draw_off_and_draw_at_one_reproduce_the_base_hashes',
                     'engine/season/tests/test_go07_canonical_digest.py::test_go07_control_the_world_did_not_move_only_its_digest'])
        for k, v in r.items():
            if v['rc'] != 0:
                log.w('fail', section='batches2.S1d_alone', what=f'{k} red after S1d alone (deleting the H-80 placeholder stages from open_case case files)',
                      proposal_said="S1 is deletions only: 'suite green with fewer files'; hashes re-pinned only at S4", result=v)
    else:
        log.w('blocked', section='batches2.S1d_alone', first_blocker='effects_information.py patch anchors not found')
    # --- S4 `case` key alone
    log.w('result', section='batches2.reset', rc=reset())
    s = open(p3).read()
    old4 = '    return {"date": date, "matter": matter,\n            DOCKET_ARRANGEMENT: arrangement, DOCKET_PETITION: petition}'
    new4 = '    return {"date": date, "matter": matter,\n            DOCKET_ARRANGEMENT: arrangement, DOCKET_PETITION: petition, "case": None}'
    if old4 in s:
        open(p3, 'w').write(s.replace(old4, new4))
        log.w('result', section='batches2.S4_case_key_alone', applied=True)
        files = ['engine/season/tests/test_season_weather.py::test_in21_control_draw_off_and_draw_at_one_reproduce_the_base_hashes',
                 'engine/season/tests/test_go07_canonical_digest.py::test_go07_control_the_world_did_not_move_only_its_digest',
                 'engine/season/tests/test_sc01_fired_slot.py', 'engine/season/tests/test_u7_remit.py', 'engine/season/tests/test_in45_carry.py',
                 'engine/season/tests/test_seen_claim.py', 'engine/season/tests/test_referent_class_stamps.py']
        r = tail_of(files)
        for k, v in r.items():
            if v['rc'] != 0:
                log.w('fail', section='batches2.S4_case_key_alone', what=f'{k} red after the `case` docket key alone', result=v,
                      proposal_said='S4 re-pins two named hashes; no other test is claimed to move')
            else:
                log.w('null', section='batches2.S4_case_key_alone', what=f'{k} after the `case` key', how='ran the test in the worktree with only `case: None` added to _docket_item', found='passes: the key does not move it')
        hash_moves = [k for k, v in r.items() if ('season_weather' in k or 'go07' in k) and v['rc'] != 0]
        log.w('result', section='batches2.S4_case_key_alone.hashes', pinned_hash_tests_red=hash_moves, other_files_red=[k for k, v in r.items() if v['rc'] != 0 and k not in hash_moves])
    else:
        log.w('blocked', section='batches2.S4_case_key_alone', first_blocker='_docket_item text not found')
    # --- S1e alone, done by exact text
    log.w('result', section='batches2.reset', rc=reset())
    import re
    pa = os.path.join(wt, 'engine/season/arrangements.yaml')
    pl = os.path.join(wt, 'engine/season/data/arrangements.py')
    sy = open(pa).read()
    sy2 = re.sub(r'^\s+(records_dissent|venue_min_rank):.*\n', '', sy, flags=re.M)
    sl = open(pl).read()
    sl2 = sl.replace('"id", "disposal", "bench_basis", "floor", "records_dissent", "venue_min_rank",', '"id", "disposal", "bench_basis", "floor",')
    blk = ('    records_dissent = need("records_dissent")\n    if not isinstance(records_dissent, bool):\n'
           '        raise SystemExit(f"arrangements.yaml: {name!r} has `records_dissent: {records_dissent!r}`, "\n'
           '                         "not `true`/`false`.")\n    venue_min_rank = need("venue_min_rank")\n'
           '    _refuse_not_in(name, "venue_min_rank", venue_min_rank, RUNG_KINDS, "a `rung_kinds` member",\n                   repr_fn=list)\n')
    ok_blk = blk in sl2
    sl2 = sl2.replace(blk, '')
    ret_old = '"floor": floor_form, "floor_basis": floor_basis, "records_dissent": records_dissent,\n        "venue_min_rank": venue_min_rank, "term_required": term_required,'
    ret_new = '"floor": floor_form, "floor_basis": floor_basis,\n        "term_required": term_required,'
    ok_ret = ret_old in sl2
    sl2 = sl2.replace(ret_old, ret_new)
    log.w('result', section='batches2.S1e_alone', block_found=ok_blk, return_found=ok_ret, yaml_changed=sy2 != sy)
    if ok_blk and ok_ret and sy2 != sy:
        open(pa, 'w').write(sy2)
        open(pl, 'w').write(sl2)
        chk = subprocess.run([sys.executable, '-c', 'from engine.season.data.arrangements import ARRANGEMENTS; print(len(ARRANGEMENTS))'], cwd=wt, capture_output=True, text=True, env={**os.environ, 'PYTHONPATH': wt})
        log.w('result', section='batches2.S1e_alone', loader_import_rc=chk.returncode, out=chk.stdout.strip()[-40:], err=chk.stderr.strip()[-200:])
        r = tail_of(['engine/season/tests/test_arrangements.py', 'engine/season/tests/test_u7_remit.py', 'engine/season/tests/test_sc01_fired_slot.py'])
        for k, v in r.items():
            if v['rc'] != 0:
                log.w('fail', section='batches2.S1e_alone', what=f'{k} red after folding away records_dissent and venue_min_rank (mechanical removal from rows and loader)', result=v,
                      proposal_said="'records_dissent folds into disposal_reach and venue_min_rank into admit's gate, as AR section C' is listed under S1 'deletions'; test_arrangements.py pins the key set")
    else:
        log.w('blocked', section='batches2.S1e_alone', first_blocker='arrangements.py text anchors not found (see block_found/return_found)')
    log.w('result', section='batches2.reset', rc=reset())
    log.w('summary', section='batches2', wall_s=round(time.time() - t0, 1), stop='all steps finished')


def batch_seed_hashes(log, budget_s):
    """go07's test stops at the first seed that moves. Does the `case` docket key (S4) also move seeds 1 and 2's one-season pins? Run in the scratch worktree
    (reset, `case` key applied, then reset again), one season each, in a subprocess so the worktree's engine is the one imported."""
    wt = WT
    log.w('section_start', section='batches3.seed_hashes', claim="S4 moves 'the per-seed BASE content hashes' (P2 6, test_go07_canonical_digest.py:469-481)")
    _sh(wt, 'git', 'reset', '-q', '--hard', 'HEAD')
    p3 = os.path.join(wt, 'engine/season/loop/effects_information.py')
    s = open(p3).read()
    old4 = '    return {"date": date, "matter": matter,\n            DOCKET_ARRANGEMENT: arrangement, DOCKET_PETITION: petition}'
    new4 = '    return {"date": date, "matter": matter,\n            DOCKET_ARRANGEMENT: arrangement, DOCKET_PETITION: petition, "case": None}'
    if old4 not in s:
        log.w('blocked', section='batches3.seed_hashes', first_blocker='_docket_item text not found')
        return
    PINS = {0: '873525dfb363231695cefb17ad4b17a1', 1: '3c6c0de333bba66196eb5b76a07d75ed', 2: '07a0c78487abfd59764989aae839694a'}
    code = ("import sys; sys.path.insert(0, %r)\n"
            "from engine.season.harness.populated import build_realm, make_chooser, SeasonDriver, resolvable_verbs, H, draw_factory, P\n"
            "seed=int(sys.argv[1]); w=build_realm(seed); d=SeasonDriver(w)\n"
            "mint=lambda pid,verb,subj,w=w: H(w.world_seed,w.tick,pid,f'act:{verb}:{subj}')\n"
            "ch=make_chooser(w.fixtures,mint,verbs=resolvable_verbs(),draw=draw_factory(w.world_seed,lambda w=w:w.tick))\n"
            "d.season(ch,question=None,subsistence=P.SUBSIST,contest_max_depth=w.fixtures.get('contest_max_depth'))\n"
            "import collections; c=collections.Counter(e.kind for e in w.log)\n"
            "print(w.content_hash(), c['case.opened'], len(w.log))\n") % wt
    open(p3, 'w').write(s.replace(old4, new4))
    try:
        for seed in (0, 1, 2):
            p = subprocess.run([sys.executable, '-c', code, str(seed)], cwd=wt, capture_output=True, text=True, env={**os.environ, 'PYTHONPATH': wt, 'PYTHONHASHSEED': '0'}, timeout=600)
            h, opened, nlog = (p.stdout.split() + ['?', '?', '?'])[:3]
            log.w('trial', section='batches3.seed_hashes', n=1, seed=seed, arm='case_key_applied', hash=h, pin=PINS[seed], moved=h != PINS[seed], case_opened=opened, log_events=nlog, rc=p.returncode, err=p.stderr[-200:])
            if h == PINS[seed]:
                log.w('null', section='batches3.seed_hashes', what=f'seed {seed} one-season hash with the `case` key', how='worktree run vs the go07 pin', found='unchanged: the key does not move this seed (no open_case executed or no docket item written)')
    finally:
        _sh(wt, 'git', 'reset', '-q', '--hard', 'HEAD')
    log.w('summary', section='batches3')


if __name__ == '__main__':
    main()
