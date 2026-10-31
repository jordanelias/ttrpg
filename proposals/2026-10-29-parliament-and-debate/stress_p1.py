"""Stress test of PROPOSAL 1 ("One draw, one roster") for the social-contest subsystem, with an audit log.

Same JSONL convention as stress_probe.py (PR #530): ONE FLUSHED, fsync'd JSON LINE per event; kinds
manifest / plan / section_start / trial / batch / claim / result / fail / null / blocked / skipped /
unverified / error / summary. Nothing here edits a tracked file. Scratch work is under --scratch.

WHAT IS REAL and WHAT IS MODEL (also in the report's fidelity statement):
  REAL   engine.dice_engine.sigma_leverage (p_success, net_boost, roll_net_continuous, soft_cap),
         dice_engine.degree_from_net, modules.social_contest.roll.obstacle, build_realm(seed) worlds, the
         world_q Queries (members, judging_set, residence_of, enclosing_territory, remove_weight, docketed),
         person_q.regard / deeds_judged, data.verbs.align_kind, the real open_case / determine acts through
         test_u7_remit's helpers, data.arrangements.
  MODEL  (this file's reading of what P1 says it WILL build) the Dice / Obstacle / Leverage sub-records and
         their composition; the producers (faction, standing, fit, evidence ...) and legitimacy_share; the
         authority map; the judge's disposition rule; the row weights (placeholders the proposal itself
         marks 'swept').  A model result is evidence about the DESIGN, not about the code.

NO CHOSEN HORIZON/TRIAL COUNT: each sampled cell runs until a stated stopping rule (a standard error below
a stated width, or a per-cell wall-clock slice) and the stop reason is logged beside n.

Usage (repo root):  python proposals/2026-10-29-parliament-and-debate/stress_p1.py --log OUT.jsonl \
        [--sections leg,model,chan,regard,bench,kinds,dom,pace,fail,real,extremes] [--budget-s 1500]
"""
import argparse, copy, itertools, json, math, os, random, sys, time, traceback
from collections import Counter, defaultdict
from dataclasses import dataclass, fields, replace

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from stress_probe import Log, git                                                        # one owner of the log shape
from engine.dice_engine import sigma_leverage as SL
from engine.dice_engine.dice_engine import degree_from_net, DEGREE_LABEL
from engine.dice_engine.sigma_leverage import p_success, net_boost, roll_net_continuous, soft_cap, OB_MIN
from engine.season.queries.inputs import SocialContestInput
from modules.social_contest import roll as sc_roll

INF, NAN = float('inf'), float('nan')
T0 = time.time()


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 1.0)
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (round((c - h) / d, 5), round((c + h) / d, 5))


def rate(k, n):
    return {'k': k, 'n': n, 'p': round(k / n, 5) if n else None, 'ci95': wilson(k, n)}


# ───────────────────────── the MODEL of P1's typed record ─────────────────────────
# P1 §3.2: three typed sub-records, one field per source; the sub-record IS the channel.
@dataclass(frozen=True)
class Dice:
    brought: float = 4.0       # pool_default 4D (P1 Q3 assumption)
    conduct: float = 0.0
    latitude: float = 1.0
    standing: float = 0.0      # max(title, seat) weight x L
    faction: float = 0.0
    evidence: float = 0.0

    def total(self):
        return self.brought + self.conduct * self.latitude + self.standing + self.faction + self.evidence


@dataclass(frozen=True)
class Obstacle:
    opposing: float | None = None    # opponent's Dice total LESS his evidence, or None
    aptness: float = 0.0
    forgery: float = 0.0
    default: float = 2.0
    ceiling: float | None = 3.0      # P1 uses 3
    refusal_multiple: float = 2.0


@dataclass(frozen=True)
class Leverage:
    fit: float = 0.0
    circumstance: float = 0.0

    def s(self):
        return self.fit + self.circumstance


def model_ob(o: Obstacle) -> float:
    """P1 composes the obstacle with the LIVE function (roll.py:103-113): aptness enters where forgery enters."""
    inp = SocialContestInput(pool=1, opposition=o.opposing, obstacle_default=o.default, obstacle_ceiling=o.ceiling,
                             obstacle_refusal_multiple=o.refusal_multiple, leverage=0.0,
                             forgery_quality=o.forgery + o.aptness)
    return sc_roll.obstacle(inp)


def model_roll(d: Dice, o: Obstacle, l: Leverage, rng):
    """One P1 draw: the continuous roll, the sigma mu-shift, the obstacle (real functions, model composition)."""
    n = d.total()
    return roll_net_continuous(n, rng=rng) + net_boost(l.s(), n) - model_ob(o)


def closed_form_margin(n, s, ob):
    """The ARMATURE's D.1 closed form, as written: E[m] = 0.4 N + 0.8 sqrt(N) softcap(s) - Ob."""
    return 0.4 * n + 0.8 * math.sqrt(n) * soft_cap(s) - ob


def bands(n, s, ob):
    """Closed-form P(meets), P(succeeds), P(overwhelms): P(margin >= 0, 1, 3) from the REAL p_success."""
    return p_success(ob, n, s), p_success(ob + 1, n, s), p_success(ob + 3, n, s)


# ───────────────────────── sections ─────────────────────────
def sec_legitimacy(log):
    """(a) L = share of the venue territory's residents holding a live `commit` to the authority's faction.
    MEASURED on build_realm seeds 0-2, Crown and Church, per territory, with n residents. REAL data, MODEL L."""
    from engine.season.harness.populated import build_realm
    from engine.season.queries import world_q as wq
    log.w('section_start', section='legitimacy', claim_under_test="P1 §3.7: L is legitimacy_share(authority, territory) = share of residents holding a live commit to that authority's faction; "
          "'Unmeasured... if laity commits are sparse, L is near 0 everywhere and every authority is weak, which B4 must measure first.'")
    log.w('claim', where='P1 §3.7', text="L ... the share of persons in the venue's territory holding a live `commit` to that authority's faction (`world_q.members`, `:1795`)")
    POLITY = {'fac_crown'}
    POLITY_WIDE = {'fac_crown', 'fac_hafenmark', 'fac_varfell', 'fac_löwenritter', 'fac_schoenland'}   # sensitivity: every non-church seat faction
    CHURCH = {'fac_church_of_solmund'}
    allrows = []
    for seed in (0, 1, 2):
        w = build_realm(seed)
        res = wq.residence_of(w); home = wq.home_of(w)
        terr = sorted(r.id for r in w.rungs.values() if r.kind == 'territory')
        live_commits = [(t.subject, t.object) for t in w.tenures if t.kind == 'commit' and t.live and t.subject in w.persons]
        by_fac = defaultdict(set)
        for s_, o_ in live_commits:
            by_fac[o_].add(s_)
        # seat-holders (office hold edges): are the committed persons laity or seat-holders?
        holders = {t.subject for t in w.tenures if t.kind == 'hold' and t.live}
        for label, where in (('reside', res), ('contain', home)):
            by_t = defaultdict(list)
            for pid, rung in where.items():
                by_t[wq.enclosing_territory(w, rung)].append(pid)
            for name, facs in (('crown', POLITY), ('church', CHURCH), ('polity_wide', POLITY_WIDE)):
                members = set().union(*[by_fac.get(f, set()) for f in facs])
                Ls = []
                for t in terr:
                    res_t = by_t.get(t, [])
                    k = sum(1 for p in res_t if p in members)
                    Ls.append((t, len(res_t), k, round(k / len(res_t), 4) if res_t else None))
                vals = [x[3] for x in Ls if x[3] is not None]
                n_all = sum(x[1] for x in Ls)
                row = {'seed': seed, 'residence_by': label, 'authority': name, 'n_residents_placed_in_a_territory': n_all,
                       'n_territories': len(terr), 'n_territories_with_zero_residents': sum(1 for x in Ls if x[1] == 0),
                       'n_territories_L_eq_0': sum(1 for v in vals if v == 0), 'n_territories_L_gt_0': sum(1 for v in vals if v > 0),
                       'L_min': min(vals) if vals else None, 'L_max': max(vals) if vals else None,
                       'L_mean_over_territories': round(sum(vals) / len(vals), 4) if vals else None,
                       'L_pooled': rate(sum(x[2] for x in Ls), n_all),
                       'per_territory': {x[0]: {'n': x[1], 'k': x[2], 'L': x[3]} for x in Ls}}
                log.w('result', section='legitimacy', **row)
                allrows.append(row)
        # who holds the commits: seat-holders or laity?
        for name, facs in (('crown', POLITY), ('church', CHURCH)):
            members = set().union(*[by_fac.get(f, set()) for f in facs])
            log.w('result', section='legitimacy.who_commits', seed=seed, authority=name, n_commits=len(members),
                  of_which_hold_an_office=len(members & holders), laity=len(members - holders),
                  n_persons=len(w.persons), n_office_holders=len(holders))
    # verdicts
    church = [r for r in allrows if r['authority'] == 'church' and r['residence_by'] == 'reside']
    crown = [r for r in allrows if r['authority'] == 'crown' and r['residence_by'] == 'reside']
    log.w('result', section='legitimacy.verdict',
          church={'territories_L_gt_0': [r['n_territories_L_gt_0'] for r in church], 'of': [r['n_territories'] for r in church],
                  'pooled_L': [r['L_pooled'] for r in church]},
          crown={'territories_L_gt_0': [r['n_territories_L_gt_0'] for r in crown], 'of': [r['n_territories'] for r in crown],
                 'pooled_L': [r['L_pooled'] for r in crown]},
          falsifier='L would have been near-constant and mid-range (e.g. 0.3-0.7 in most territories) if commits were spread across residents; '
                    'it is L=0 in most territories and 1/n granular where non-zero')
    # control: is the measure able to see a high L at all? (a planted control world: every resident in T1 committed)
    w = build_realm(0); res = wq.residence_of(w)
    t1 = [p for p, r in res.items() if wq.enclosing_territory(w, r) == 'terr_T1']
    from engine.season.state.carriers import Tenure
    ok = 0
    for p in t1:
        ok += 1
    log.w('result', section='legitimacy.control',
          note=f"control: T1 has {len(t1)} residents, so L in T1 can take only multiples of 1/{len(t1)}; the instrument can read 1.0 if all {len(t1)} commit (not planted: see null)",
          granularity=round(1 / len(t1), 4) if t1 else None)
    log.w('null', section='legitimacy', examined="no resident-level commit is toward a *territory-local* piety: the instrument counts `commit` edges to fac_* Propositions only; "
          "`person_q.legitimacy` (the stance/deed estimate that is P1's own named revert) was NOT measured here", how='see the unverified line')
    w = build_realm(0); res = wq.residence_of(w)
    in_t9 = [p for p, r in res.items() if wq.enclosing_territory(w, r) == 'terr_T9']
    church_mem = set(wq.members(w, 'fac_church_of_solmund'))
    bench = set(wq.judging_set(w, 'terr_T9'))
    church_seat_holders = {t.subject for t in w.tenures if t.kind == 'hold' and t.live and t.object in w.offices
                           and 'church' in (getattr(w.offices[t.object], 'faction', None) or '').lower()}
    log.w('result', section='legitimacy.T9_circularity', residents_T9=len(in_t9), committed_to_church_in_T9=len([p for p in in_t9 if p in church_mem]),
          committed_who_are_on_T9_bench=len([p for p in in_t9 if p in church_mem and p in bench]),
          committed_who_hold_a_church_faction_office=len([p for p in in_t9 if p in church_mem and p in church_seat_holders]),
          note='where a church bench can sit (T9 only), L is high because the bench and church officers live there and are the committed; the L that weights them is made of them')
    log.w('unverified', section='legitimacy', what="P1's revert arm (mean of person_q.legitimacy over residents) was not measured: it needs a holder id per authority and reads other ledgers (F8); "
          "only the commit-share L that P1 chose is measured")


def sec_model_closed_form(log, budget):
    """(b) the armature's closed form, held against the model AND against p_success; extremes S1; the proposal's quoted odds."""
    log.w('section_start', section='closed_form')
    log.w('claim', where='AR D.1 / P1 §3.3', text='E[margin] = 0.4*N + 0.8*sqrt(N)*softcap(s) - Ob; "At the 5D reference against an equal (Ob 2.5) an act meets .390 and succeeds .201"')
    rnd = random.Random(20261030)
    cells = [(n, s, ob) for n in (1, 2, 5, 12, 30) for s in (-1.5, 0.0, 0.5, 1.5, 3.0) for ob in (1.0, 2.5, 6.0)]
    worst = 0; maxz = 0; wilson_miss = 0; wilson_tot = 0
    per_cell_budget = max(0.15, budget / (len(cells) + 20))
    nfail = 0
    for n, s, ob in cells:
        d = Dice(brought=float(n)); l = Leverage(fit=s); o = Obstacle(opposing=2 * ob, ceiling=None)   # opposing/2 = ob
        assert abs(model_ob(o) - ob) < 1e-12
        r = random.Random(rnd.randrange(2 ** 31)); k = [0, 0, 0]; sm = 0.0; sm2 = 0.0; m = 0
        t_end = time.time() + per_cell_budget
        stop = 'slice'
        while time.time() < t_end:
            for _ in range(500):
                x = model_roll(d, o, l, r); sm += x; sm2 += x * x; m += 1
                k[0] += x >= 0; k[1] += x >= 1; k[2] += x >= 3
            se = math.sqrt(max(sm2 / m - (sm / m) ** 2, 1e-12) / m)
            if se < 0.004 and m >= 4000:
                stop = 'se<0.004'; break
        mean = sm / m; se = math.sqrt(max(sm2 / m - mean * mean, 1e-12) / m)
        cf = closed_form_margin(n, s, ob)
        ps = bands(n, s, ob)
        z = (mean - cf) / se
        ci = [wilson(k[i], m) for i in range(3)]
        pins = [ci[i][0] <= ps[i] <= ci[i][1] for i in range(3)]
        log.w('trial', section='closed_form', n_pool=n, s=s, ob=ob, n=m, stop=stop, mean_margin=round(mean, 4), se=round(se, 4),
              closed_form=round(cf, 4), z=round(z, 2), p_meets=rate(k[0], m), p_succ=rate(k[1], m), p_overw=rate(k[2], m),
              p_success_meets=round(ps[0], 5), p_success_succ=round(ps[1], 5), p_success_overw=round(ps[2], 5), p_success_inside_wilson=pins)
        maxz = max(maxz, abs(z))
        wilson_miss += sum(1 for x in pins if not x); wilson_tot += 3
        if abs(z) > 4:
            nfail += 1
            log.w('fail', section='closed_form', what='sampled mean margin disagrees with the closed form by |z|>4', n_pool=n, s=s, ob=ob, z=round(z, 2))
    log.w('result', section='closed_form.wilson_tally', intervals=wilson_tot, p_success_outside_wilson95=wilson_miss, expected_by_chance_at_95=round(wilson_tot * 0.05, 1),
          note='ATTEMPT 1 logged each miss as a `fail`; with 225 intervals at 95% about 11 misses are expected by chance, so a miss is not a failure. Falsifier of the closed form is |z|>4 on the mean, and a miss RATE far above 5%.')
    log.w('result', section='closed_form', cells=len(cells), cells_failing=nfail, max_abs_z=round(maxz, 2),
          interpretation='HELD for N>=1 if cells_failing==0: the model (real roll_net_continuous + real net_boost) matches the closed form and p_success. Falsifier: any |z|>4 or p_success outside the Wilson interval.')
    # N < 1: the pool floor. The armature writes 0.4 N, not 0.4 max(1,N).
    for n in (0.0, 0.25, 0.5, 0.99, 1.0):
        s = 1.0; ob = 1.0
        rr = random.Random(7); sm = 0; m = 40000
        for _ in range(m):
            sm += roll_net_continuous(n, rng=rr) + net_boost(s, n) - ob
        mean = sm / m
        cf = closed_form_margin(n, s, ob) if n > 0 else float('nan')
        floor_cf = closed_form_margin(max(1.0, n), s, ob)
        rec = dict(section='closed_form.sub1D', N=n, s=s, ob=ob, n=m, mean_margin=round(mean, 4), armature_formula=round(cf, 4) if cf == cf else 'sqrt/0.4N at N=0 gives 0.4*0+0.8*0*..', floored_formula=round(floor_cf, 4))
        log.w('trial', **rec)
        if n < 1 and abs(mean - floor_cf) < 0.03 and (cf != cf or abs(mean - cf) > 0.1):
            log.w('fail', section='closed_form.sub1D', what=f"the armature's E[m]=0.4N+0.8sqrt(N)softcap(s)-Ob is WRONG for N={n} (<1D): the engine floors the pool at 1D for mean AND spread; the formula as written (and P1's 'fractional pool' reading of N) does not",
                  sampled=round(mean, 4), armature=rec['armature_formula'], floored=round(floor_cf, 4), proposal_said='AR D.1 / P1 §3.3 give the formula with N unfloored')
    # S1: NaN / negative / inf pools into the real function
    for n in (-3.0, NAN, INF):
        try:
            v = roll_net_continuous(n, rng=random.Random(1)); ps = p_success(2.0, n, 0.0)
            log.w('result', section='closed_form.nonfinite', N=repr(n), roll=repr(v), p_success=repr(ps),
                  note='no refusal: ' + ('a NaN pool is floored to 1D silently (max(1.0, nan) == 1.0)' if n != n else ('inf pool: draws inf' if n == INF else 'negative pool floored to 1D')))
            if n != n or n == INF or n < 0:
                log.w('fail', section='closed_form.nonfinite', what=f'pool {n!r} accepted without refusal by the draw; P1 §3.2 types the pool as a float with no stated guard', observed=f'roll={v!r} p_success={ps!r}', proposal_said='silent on non-finite/negative pools (the PR #530 module stress found the same for NaN opposition)')
        except Exception:
            log.w('error', section='closed_form.nonfinite', N=repr(n), traceback=traceback.format_exc())
    # the proposal's quoted numbers, held against the closed form (tolerance = rounding to 3 places)
    quoted = [
        ('§3.3 5D v equal (Ob 2.5): meets .390', 5, 0.0, 2.5, 0, 0.390), ('§3.3 5D v equal: succeeds .201', 5, 0.0, 2.5, 1, 0.201),
        ('§4.1 pious, inquisitor speaks N7.7 v Ob2: meets .687', 7.7, 0.0, 2.0, 0, 0.687), ('§4.1 same: succeeds .514', 7.7, 0.0, 2.0, 1, 0.514),
        ('§4.1 weak N5.6 v Ob2: meets .550', 5.6, 0.0, 2.0, 0, 0.550), ('§4.1 same: succeeds .344', 5.6, 0.0, 2.0, 1, 0.344),
        ('§4.1 miller denies pious, Ob 3 (ceiling): meets .191', 4.0, 0.0, 3.0, 0, 0.191), ('§4.1 miller denies weak, Ob 2.3: meets .331', 4.0, 0.0, 2.3, 0, 0.331),
        ('§4.1 Cardinal pious N6.7 v 2: meets .629', 6.7, 0.0, 2.0, 0, 0.629), ('§4.1 same: succeeds .439', 6.7, 0.0, 2.0, 1, 0.439),
        ('§4.1 Cardinal weak N4.6 v 2: meets .463', 4.6, 0.0, 2.0, 0, 0.463), ('§4.1 same: succeeds .249', 4.6, 0.0, 2.0, 1, 0.249),
        ('§4.2 Duke defence N6.4 v 3.05: meets .404', 6.4, 0.0, 3.05, 0, 0.404),
        ('§4.2 King N6.1 v 2.7: meets .448', 6.1, 0.0, 2.7, 0, 0.448), ('§4.2 same: succeeds .262', 6.1, 0.0, 2.7, 1, 0.262),
        ('§4.2 restive L.3 N4.9 v 2.3: meets .424', 4.9, 0.0, 2.3, 0, 0.424),
        ('§9a 5D v equal, s 0.5: meets .580', 5, 0.5, 2.5, 0, 0.580),
    ]
    nb = 0
    for text, n, s, ob, thr, claimed in quoted:
        got = p_success(ob + thr, n, s)
        held = abs(got - claimed) <= 0.0006
        log.w('result', section='quoted_numbers', claim=text, claimed=claimed, computed=round(got, 5), held=held)
        if not held:
            nb += 1
            log.w('fail', section='quoted_numbers', what=f'P1 quotes {claimed} for "{text}"; p_success gives {got:.5f}', proposal_said=claimed, observed=round(got, 5))
    log.w('result', section='quoted_numbers', n_quoted=len(quoted), n_broken=nb)
    # '61% fail at 5D, 65% at 10D' against an equal
    for n in (5, 10):
        f = 1 - p_success(n / 2.0, n, 0.0)
        log.w('result', section='equals', pool=n, p_fail_vs_equal=round(f, 4), claim='P1 §8 Q5 / AR G4: fails 61% at 5D (65% at 10D)')
        if abs(f - (0.61 if n == 5 else 0.65)) > 0.006:
            log.w('fail', section='equals', what=f'fail-rate against an equal at {n}D is {f:.4f}', proposal_said=0.61 if n == 5 else 0.65)
    # σ dominance: share of the margin's input-variance by channel at 5D and 12D (AR H.2). MODEL ranges, swept.
    rr = random.Random(5)
    for scale in (0.5, 1.0, 2.0):
        for N0 in (5, 12):
            # channels vary one at a time over their plausible range; others at their mean. Ranges: P1's own example weights.
            def f(dice_x=0.0, ob_x=0.0, sig_x=0.0):
                n = N0 + dice_x
                return 0.4 * max(1, n) + 0.8 * math.sqrt(max(1, n)) * soft_cap(sig_x) - (N0 / 2.0 + ob_x)
            def var(fn, lo, hi, m=4000):
                xs = [fn(rr.uniform(lo, hi)) for _ in range(m)]
                mu = sum(xs) / m; return sum((x - mu) ** 2 for x in xs) / m
            # dice: title/seat/faction/evidence weights up to +- 3D*scale ; obstacle: opponent +-3D/2*scale ; sigma: fit+circ in [-1,1]*scale each -> [-2,2]*scale
            vd = var(lambda x: f(dice_x=x), -3 * scale, 3 * scale)
            vo = var(lambda x: f(ob_x=x), -1.5 * scale, 1.5 * scale)
            vs = var(lambda x: f(sig_x=x), -2 * scale, 2 * scale)
            tot = vd + vo + vs
            log.w('result', section='sigma_share', pool=N0, range_scale=scale, var_dice=round(vd, 4), var_obstacle=round(vo, 4), var_sigma=round(vs, 4),
                  share_sigma=round(vs / tot, 3), share_dice=round(vd / tot, 3), share_ob=round(vo / tot, 3))
    # break-even: the sigma input half-range at which the sigma channel's variance equals the dice channel's, at each pool
    for N0 in (5, 12):
        def fv(fn, lo, hi, m=6000):
            rr2 = random.Random(11); xs = [fn(rr2.uniform(lo, hi)) for _ in range(m)]; mu = sum(xs) / m; return sum((x - mu) ** 2 for x in xs) / m
        vd = fv(lambda x: 0.4 * max(1, N0 + x) + 0.8 * math.sqrt(max(1, N0 + x)) * 0 - N0 / 2.0, -3, 3)
        lo_, hi_ = 0.0, 3.0
        for _ in range(40):
            mid = (lo_ + hi_) / 2
            vs = fv(lambda x: 0.8 * math.sqrt(max(1, N0)) * soft_cap(x) + 0.4 * N0 - N0 / 2.0, -mid, mid)
            if vs > vd: hi_ = mid
            else: lo_ = mid
        log.w('result', section='sigma_share.breakeven', pool=N0, dice_halfrange_D=3.0, sigma_halfrange_at_equal_variance=round(lo_, 3),
              note='sigma inputs (fit + circumstance, summed) must be confined to about +-this many sigma-units for the dice channel to carry as much variance as sigma over a +-3D dice swing')
    log.w('result', section='sigma_share.note', note="MODEL ranges (my assumption, swept x0.5/x1/x2). AR H.2's falsifier: 'if sigma's share exceeds the dice share at 12D'. Read the shares per pool.")


def sec_channels(log):
    """(b) a source cannot enter two channels. Structural half (MODEL), and the real-edge half (REAL world, MODEL producers)."""
    from engine.season.harness.populated import build_realm
    from engine.season.queries import world_q as wq
    log.w('section_start', section='channels')
    log.w('claim', where='P1 §3.2', text='"a field has one home, so entering two channels is impossible by construction, not by discipline" and '
          '"The producers below are chosen so that no two read the same edge family"')
    names = {c.__name__: {f.name for f in fields(c)} for c in (Dice, Obstacle, Leverage)}
    overlap = {(a, b): sorted(names[a] & names[b]) for a, b in itertools.combinations(names, 2) if names[a] & names[b]}
    log.w('result', section='channels.structure', record_fields=names, pairwise_overlap=overlap,
          note='disjoint field names: HELD for the narrow sense (one FIELD, one channel); this is what a dataclass gives for free and is the proposal\'s own point')
    # Negative control for the structural test: the same *source* under two field names is accepted by the type.
    @dataclass(frozen=True)
    class Dice2(Dice):
        faction_again: float = 0.0
    log.w('result', section='channels.control', note='a second field fed from the same source is accepted by the type (Dice2.faction_again); the type forbids a field in two records, not a SOURCE under two fields',
          accepted=True)
    # Real world: which producers read the `commit` edge family?  Build the P1 producers over the REAL edges.
    w = build_realm(0)
    ROW = {'factions': {'fac_church_of_solmund': 1.0, 'fac_crown': 1.0}, 'seat': 3.0, 'fit_gain': 1.0, 'L_weight_seat': 3.0}
    res = wq.residence_of(w)
    t9 = [p for p, r in res.items() if wq.enclosing_territory(w, r) == 'terr_T9']
    members_church = wq.members(w, 'fac_church_of_solmund')

    def L_church(tid='terr_T9'):
        in_t = [p for p, r in res.items() if wq.enclosing_territory(w, r) == tid]
        mem = set(wq.members(w, 'fac_church_of_solmund'))
        return (sum(1 for p in in_t if p in mem) / len(in_t)) if in_t else 0.0

    def producers(actor, decider, prop='fac_church_of_solmund'):
        # faction (dice): row weight for each faction he holds a live commit to (world_q.members)
        faction = sum(wt for f, wt in ROW['factions'].items() if actor in wq.members(w, f))
        # standing (dice): seat weight x L of the seat's authority (here church)
        standing = ROW['seat'] * L_church()
        # fit (sigma): the decider's live commit edges agreeing with the actor's proposition (here: commit to `prop`)
        agree = sum(1 for t in w.tenures if t.kind == 'commit' and t.live and t.subject == decider and t.object == prop)
        fit = ROW['fit_gain'] * agree
        return {'dice.faction': faction, 'dice.standing(L)': round(standing, 5), 'sigma.fit': fit}
    # pick an actor and a decider who are church members, and an observer resident in T9
    if len(members_church) < 3:
        log.w('blocked', section='channels.edge', why=f'only {len(members_church)} church members in seed 0; needs >=3', at='engine/season/harness/populated.py (build_realm)')
        return
    actor, decider = members_church[0], members_church[1]
    base = producers(actor, decider)
    log.w('result', section='channels.edge', actor=actor, decider=decider, base=base, n_church_members=len(members_church), n_T9_residents=len(t9))
    edges = [t for t in w.tenures if t.kind == 'commit' and t.live and t.object == 'fac_church_of_solmund']
    moved_multi = 0; rows = []
    for t in edges:
        was = t.until
        t.until = w.tick                          # end ONE commit edge (REAL tenure, restored below)
        try:
            after = producers(actor, decider)
        finally:
            t.until = was
        moved = [k for k in base if after[k] != base[k]]
        who = 'actor' if t.subject == actor else ('decider' if t.subject == decider else ('T9-resident' if t.subject in t9 else 'elsewhere'))
        rows.append({'edge_holder': t.subject, 'role': who, 'channels_moved': moved})
        if len(moved) >= 2:
            moved_multi += 1
    log.w('result', section='channels.edge_flip', rows=rows, edges_tested=len(edges), edges_moving_two_or_more_channels=moved_multi)
    # control: end a commit to an UNRELATED faction (guilds): must move nothing of the church row
    ctl = [t for t in w.tenures if t.kind == 'commit' and t.live and t.object == 'fac_guilds']
    cm = []
    for t in ctl:
        was = t.until; t.until = w.tick
        try:
            after = producers(actor, decider)
        finally:
            t.until = was
        cm.append([k for k in base if after[k] != base[k]])
    log.w('result', section='channels.control_unrelated_edge', edges=len(ctl), channels_moved=cm,
          note='control arm: ending a commit to fac_guilds moves no church-row operand, so the instrument can see "no change"')
    if moved_multi:
        log.w('fail', section='channels', what=f"P1 §3.2 says the producers are chosen so no two read the same edge family; in the model built from P1's own table, {moved_multi}/{len(edges)} single `commit` edges move >=2 channels (faction dice, L inside standing dice, sigma fit all read `commit`)",
              proposal_said='no two producers read the same edge family; "entering two channels is impossible by construction"', observed=rows[:3])
    # P1's cheap falsifier: set one field's row weight to 0 and assert only that producer's reads stop moving the outcome.
    ROW0 = dict(ROW); ROW0['factions'] = {k: 0.0 for k in ROW['factions']}
    t = edges[0]; was = t.until
    b0 = None
    old = ROW['factions']; ROW['factions'] = ROW0['factions']
    try:
        b0 = producers(actor, decider); t.until = w.tick; a0 = producers(actor, decider)
    finally:
        t.until = was; ROW['factions'] = old
    still = [k for k in b0 if a0[k] != b0[k]]
    log.w('result', section='channels.zero_weight_falsifier', channels_still_moving_with_factions_weight_0=still,
          note="with the `factions` weight zeroed, ending a church commit still moves the outcome through the other commit readers; P1's falsifier checks the zeroed field only, so it passes while the double read persists")


def sec_regard(log, budget):
    """(c) a judge whose determination disposition follows `person_q.regard` (REAL), does a successful argument flip it vs a control?"""
    from engine.season.harness.populated import build_realm
    from engine.season.queries import person_q as pq
    from engine.season.data import verbs as V
    from engine.season.state.carriers import Claim
    log.w('section_start', section='regard')
    log.w('claim', where='P1 §3.3, §3.5, §7 weakest 1', text='"Regard (reception) leaves the draw. It is the decider\'s fact about the speaker, so it acts in the decider\'s own choice (person_q.regard, person_q.py:393)"; '
          '"AR H.1\'s falsifier: an `argue` Success on a judge flips his `determine` choice against a control"')
    # (1) what do the speech deeds do to regard at all?  REAL align_kind over the four speak band kinds
    speak_kinds = ('matter.carried', 'matter.advanced', 'matter.held', 'matter.turned')
    vec = {k: {ax: V.align_kind(k, ax) for ax in sorted(pq.PURSUIT_AXES) if V.align_kind(k, ax)} for k in speak_kinds}
    log.w('result', section='regard.alignment', speak_band_kinds_alignment=vec,
          identical_across_bands=len({json.dumps(v, sort_keys=True) for v in vec.values()}) == 1,
          argue_kinds={k: {ax: V.align_kind(k, ax) for ax in sorted(pq.PURSUIT_AXES) if V.align_kind(k, ax)} for k in ('argument.won', 'argument.lost', 'argument.refused')})
    if len({json.dumps(v, sort_keys=True) for v in vec.values()}) == 1:
        log.w('fail', section='regard.alignment', what="every band of `speak` emits a kind with the SAME alignment vector (grandiose_humble -0.4 only), so a person's regard for a speaker cannot depend on whether the speech succeeded; a Success and a Failure move regard identically",
              proposal_said="P1 moves reception to regard 'so the best speaker wins the verdict': regard has no degree-dependence in the shipped alignment table", where='engine/season/data/verbs.py::align_kind via KIND_VERB; engine/season/verb_table.yaml speak emits_by_degree')
    # (2) the judge model on REAL persons: disposition = sign(regard(J,A) - regard(J,B)); A's speech deposits one firsthand deed in J's ledger
    stop = time.time() + budget
    tot = Counter(); per_seed = {}
    for seed in (0, 1, 2):
        w = build_realm(seed); fx = w.fixtures
        pids = sorted(w.persons)
        rnd = random.Random(seed)
        full = int(fx.get('confidence_default'))
        def disp(J, A, B):
            j = w.persons[J]
            return pq.regard(j, A, fx) - pq.regard(j, B, fx)
        def deposit(J, A, kind, cid):
            c = Claim(cid, J, A, kind, True, w.tick, 'firsthand', full, 'own')
            w.persons[J].ledger.append(c); return c
        def retract(J, c):
            w.persons[J].ledger.remove(c)
        cnt = Counter()
        triples = 0
        while time.time() < stop and triples < 4000:
            J = rnd.choice(pids); A, B = rnd.sample([p for p in pids if p != J], 2)
            base = disp(J, A, B); triples += 1
            cnt['triples'] += 1
            cnt['tie_at_baseline'] += base == 0
            for label, kind in (('success', 'matter.advanced'), ('failure', 'matter.turned'), ('overwhelm', 'matter.carried'), ('partial', 'matter.held')):
                c = deposit(J, A, kind, f'cx_{triples}')
                after = disp(J, A, B); retract(J, c)
                cnt[f'moved_{label}'] += after != base
                if base != 0:                                    # a DECIDED baseline: sign actually reverses
                    cnt[f'decided_{label}'] += 1
                    cnt[f'decided_flip_{label}'] += (base > 0 > after) or (base < 0 < after)
                if label == 'success' and after != base:
                    cnt['success_lowers_regard_of_speaker'] += after < base; cnt['success_raises_regard_of_speaker'] += after > base
                cnt[f'tie_to_nonzero_{label}'] += (base == 0 and after != 0)
                cnt[f'delta_{label}_sum'] += 0
                if label == 'success':
                    s_after = after
                if label == 'failure':
                    cnt['success_ne_failure'] += s_after != after
        per_seed[seed] = dict(cnt); tot.update(cnt)
        log.w('batch', section='regard.judge', seed=seed, n=cnt['triples'], counts=dict(cnt))
    n = tot['triples']
    log.w('result', section='regard.judge', n_triples=n, tie_at_baseline=rate(tot['tie_at_baseline'], n),
          regard_moved_by_success=rate(tot['moved_success'], n), regard_moved_by_failure=rate(tot['moved_failure'], n),
          decided_baselines=tot['decided_success'],
          decided_flip_after_success=rate(tot['decided_flip_success'], tot['decided_success']), decided_flip_after_failure=rate(tot['decided_flip_failure'], tot['decided_failure']),
          decided_flip_after_overwhelm=rate(tot['decided_flip_overwhelm'], tot['decided_overwhelm']), decided_flip_after_partial=rate(tot['decided_flip_partial'], tot['decided_partial']),
          tie_to_nonzero_after_success=rate(tot['tie_to_nonzero_success'], n), tie_to_nonzero_after_failure=rate(tot['tie_to_nonzero_failure'], n),
          speech_lowers_regard=tot['success_lowers_regard_of_speaker'], speech_raises_regard=tot['success_raises_regard_of_speaker'],
          ATTEMPT_NOTE='attempt 1 counted tie->nonzero as a flip (53.5% for every band, a harness artefact); attempt 2 separates decided flips from tie->nonzero',
          success_differs_from_failure=rate(tot['success_ne_failure'], n),
          control='baseline disposition with NO speech (the same triple, nothing deposited); and the Failure-band deposit as placebo',
          falsifier='if regard followed the degree, success_differs_from_failure would be well above 0',
          stop='n=min(4000/seed, wall-clock slice)')
    if tot['success_ne_failure'] == 0:
        log.w('fail', section='regard.judge', what='a judge whose disposition is sign(regard(A)-regard(B)) responds identically to a successful and a failed speech by A: 0 of %d triples differ' % n,
              proposal_said="P1: the best speaker's reward 'acts in the decider's own choice' through regard", observed=rate(tot['success_ne_failure'], n))
    # (3) the baseline: how often is a judge's regard for anyone non-zero at tick 0?
    w = build_realm(0); fx = w.fixtures
    nz = 0; m = 0
    for J in w.persons:
        for X in list(w.persons)[:30]:
            if J != X:
                m += 1; nz += pq.regard(w.persons[J], X, fx) != 0
    log.w('result', section='regard.baseline', regard_nonzero_pairs=rate(nz, m), note='how often a REAL judge has any regard at all for a speaker at tick 0 (seed 0, first 30 persons as referents)')
    # (4) the belief term (MODEL): the judge picks a disposition from the speeches' deposits at their confidence. The rule is P1's to build (B5).
    log.w('unverified', section='regard.belief_term', what="P1's 'disposition operand' (the judge chooses from the deposits at their confidence) is not in the tree (decision/ has no disposition operand: PROBE 2.3, AR I.12). A flip rate for it would be my parameter (beta) times the deposit, i.e. a tautology; not computed as evidence",
          where='engine/season/decision/')


def sec_bench(log):
    """(S5) real data: benches, authority groupings, reach, dice distribution, evidence density. REAL data; authority map = MODEL."""
    from engine.season.harness.populated import build_realm
    from engine.season.queries import world_q as wq
    from engine.season.queries import person_q as pq
    log.w('section_start', section='bench')
    def authority_of(off):
        fac = (getattr(off, 'faction', None) or '').lower(); body = (getattr(off, 'body', None) or '')
        if 'church' in fac or body in ('Holy See',) or body.startswith('Cardinal'):
            return 'church'
        return 'polity'
    for seed in (0, 1, 2):
        w = build_realm(seed)
        terr = sorted(r.id for r in w.rungs.values() if r.kind == 'territory')
        venues = terr + sorted(r.id for r in w.rungs.values() if r.kind in ('duchy', 'realm'))
        rows = {}
        king_on_church = 0
        for v in venues:
            seats = []
            for t in w.tenures:
                if t.kind != 'hold' or not t.live or 'determine' not in t.granted_acts:
                    continue
                off = w.offices.get(t.object)
                if off is None or not wq.sits_over(w, off, v) if hasattr(wq, 'sits_over') else False:
                    continue
                seats.append((t.subject, off.id, authority_of(off)))
            js = wq.judging_set(w, v)
            pol = [s for s in seats if s[2] == 'polity']; chu = [s for s in seats if s[2] == 'church']
            rows[v] = {'bench_today': len(set(js)), 'polity': len(pol), 'church': len(chu)}
        cap_authored = sum(1 for p in w.persons.values() if p.capability)
        n_empty_today = sum(1 for x in rows.values() if x['bench_today'] == 0)
        n_church_bench = sum(1 for x in rows.values() if x['church'] > 0)
        n_polity_bench = sum(1 for x in rows.values() if x['polity'] > 0)
        n_polity_on_church_venue = sum(1 for x in rows.values() if x['church'] > 0 and x['polity'] > 0)
        log.w('result', section='bench', seed=seed, venues=len(venues), empty_bench_venues_today=n_empty_today,
              venues_with_a_church_determine_seat=n_church_bench, venues_with_a_polity_determine_seat=n_polity_bench,
              venues_where_polity_seats_also_sit_on_a_church_bench=n_polity_on_church_venue,
              church_venue_ids=[v for v, x in rows.items() if x['church'] > 0], persons=len(w.persons), persons_with_authored_capability=cap_authored,
              per_venue=rows)
        if cap_authored == 0:
            log.w('result', section='bench.capability', seed=seed, note='0 persons carry capability: pool_default applies to everyone (brought term constant)')
        # dice distribution across persons under P1's example row: brought 4 (default), seat 3 x L, title 2, faction 1 per commit
        seat_of = {}
        for t in w.tenures:
            if t.kind == 'hold' and t.live and t.object in w.offices:
                seat_of.setdefault(t.subject, []).append(w.offices[t.object])
        Ns = []
        for p in w.persons:
            wseat = 3.0 if p in seat_of else 0.0
            wtitle = 2.0 if any(getattr(o, 'post', None) in ('Duke', 'King', 'Queen', 'Duchess') for o in seat_of.get(p, [])) else 0.0
            nfac = sum(1 for t in w.tenures if t.kind == 'commit' and t.live and t.subject == p and t.object.startswith('fac_'))
            Ns.append(4.0 + max(wseat, wtitle) * 0.5 + 1.0 * nfac)        # L fixed at .5 for the picture
        c = Counter(round(x, 1) for x in Ns)
        log.w('result', section='bench.dice_distribution', seed=seed, n_persons=len(Ns), N_min=min(Ns), N_max=max(Ns),
              n_distinct_N=len(c), histogram=dict(sorted(c.items())),
              note='MODEL row (brought 4, max(seat 3, title 2) x L .5, faction 1 per fac_ commit); shows how many distinct pools the real roster yields without authored capability')
        # evidence density: for a random pair (actor, opponent), does the actor's own ledger hold deed claims about the opponent?
        pids = sorted(w.persons); rnd = random.Random(seed); hits = 0; m = 0
        for _ in range(3000):
            a, b = rnd.sample(pids, 2); m += 1
            if any(True for _c in pq.attributed_deeds(w.persons[a].ledger, b)):
                hits += 1
        log.w('result', section='bench.evidence_density', seed=seed, pairs_with_nonzero_evidence=rate(hits, m), note='REAL ledgers at tick 0: P1 evidence = actor\'s own deed claims about the opponent (attributed_deeds), before any season runs')


def sec_dominance(log):
    """(S3) option sets for the actor and the accused, at 2D, 5D, 12D; weak/strict dominance. MODEL payoffs on real p_success."""
    log.w('section_start', section='dominance')
    log.w('claim', where='P1 §3.4, §9a, comparison §4', text='"choosing the wrong [speech kind] raises the obstacle, never refuses (R-16)"; the assessors flagged denial / `defy` / silence / "pick the apt speech kind as a lookup"')
    for N in (2.0, 5.0, 12.0):
        opp = N                                  # an equal opponent
        ob_equal = opp / 2.0
        for price in (0.5, 1.0, 2.0):            # aptness price: P1 says 'swept'
            apt = p_success(min(ob_equal, 3.0), N, 0.0); inapt = p_success(min(ob_equal + price, 3.0), N, 0.0)
            log.w('result', section='dominance.speech_kind', N=N, aptness_price=price, p_meets_apt=round(apt, 4), p_meets_inapt=round(inapt, 4),
                  apt_strictly_dominates=apt > inapt + 1e-12, delta=round(apt - inapt, 4))
        # the ceiling of 3 makes the aptness price irrelevant when the opponent is large
        capped = p_success(min(ob_equal + 1.0, 3.0), N, 0.0) == p_success(min(ob_equal, 3.0), N, 0.0)
        log.w('result', section='dominance.ceiling_hides_aptness', N=N, ob_equal=ob_equal, ceiling=3.0, price_invisible=capped,
              note='when the opponent\'s score/2 already >= ceiling, a priced inapt kind costs NOTHING (R-16 priced-not-refused is void there)')
        if capped:
            log.w('fail', section='dominance.ceiling_hides_aptness', what=f"at {N:g}D versus an equal, opponent/2={ob_equal:g} >= the ceiling 3, so the aptness price is clipped away by the ceiling: every speech kind is equally apt",
                  proposal_said='P1 §3.4/§3.2: aptness_price raises the obstacle; ceiling "binds only where an opponent exceeds 6D"', observed=f'p identical for apt/inapt at N={N}')
    # accused: silence vs speak vs the bench's reading. Two readings of what a Failure speech deposits (P1 §3.4 is silent):
    for N in (2.0, 5.0, 12.0):
        ob = min(N / 2.0, 3.0)
        ps = [p_success(ob + t, N, 0.0) for t in (0, 1, 3)]
        pF = 1 - ps[0]; pP = ps[0] - ps[1]; pS = ps[1] - ps[2]; pO = ps[2]
        # reading A: deposit confidence c(band) >= 0 at every band (0, .25, .5, 1 say): speaking weakly dominates silence
        # reading B: Failure deposits NEGATIVE confidence (-.25): EV(speak)=sum p*c
        cA = {'F': 0.0, 'P': 0.25, 'S': 0.5, 'O': 1.0}; cB = {'F': -0.25, 'P': 0.25, 'S': 0.5, 'O': 1.0}
        evA = pF * cA['F'] + pP * cA['P'] + pS * cA['S'] + pO * cA['O']; evB = pF * cB['F'] + pP * cB['P'] + pS * cB['S'] + pO * cB['O']
        log.w('result', section='dominance.silence_vs_speak', N=N, p_band={'F': round(pF, 4), 'P': round(pP, 4), 'S': round(pS, 4), 'O': round(pO, 4)},
              EV_speak_reading_A_failure_deposits_0=round(evA, 4), EV_speak_reading_B_failure_deposits_minus_quarter=round(evB, 4), EV_silence=0.0,
              speak_weakly_dominates_silence_under_A=evA >= 0, speak_dominates_silence_under_B=evB > 0)
    log.w('unverified', section='dominance', what="what a FAILED `speak` deposits (confidence by degree) is not stated by P1; under reading A speech weakly dominates silence at every pool (a corridor: 'always speak'); under B the sign of EV depends on pool. Whichever P1 builds decides whether `defy`/silence is ever rational")
    # 'defy and silence in a forum contest' - P1 has no forum contest (K8 = K3/K6 values)
    log.w('skipped', section='dominance.defy_forum', what='`defy` and silence in a forum contest (assessors: P3)', why="P1 has no `defy` act and no forum contest; K8 is 'K3 or K6 values' (P1 §4). Not a P1 option set")
    # equal-score corridors: acting vs not acting against an equal
    for N in (2.0, 5.0, 12.0):
        pm = p_success(N / 2.0, N, 0.0)
        log.w('result', section='dominance.status_quo', N=N, p_act_meets_vs_equal=round(pm, 4), p_fail=round(1 - pm, 4),
              note='R-5 divide-by-2: the actor fails more often than not against an equal; the defender needs no act. A weak-dominance of the status quo, G4')


def sec_kinds(log, budget):
    """(S2) each of the eight kinds, a worked scenario each, over seeds; one-at-a-time sensitivity. MODEL rows, REAL draws."""
    log.w('section_start', section='kinds')
    rnd = random.Random(99)
    per = max(0.2, budget / 40)
    # (name, Dice(actor), Obstacle, Leverage, note)
    L = 0.5
    scen = {
        'K1 dyadic influence (tell/argue; title only; target decides)': (Dice(brought=4, standing=1.0), Obstacle(opposing=None, default=2.0, ceiling=3.0), Leverage(fit=0.25)),
        'K2 negotiation (title + circumstance in sigma; both commit)': (Dice(brought=4, standing=1.0), Obstacle(opposing=4.0 + 1.0, ceiling=3.0), Leverage(circumstance=0.5)),
        'K3 royal tribunal: the Duke\'s defence (seat/title x L=.7)': (Dice(brought=4, standing=2 * .7, evidence=1.0), Obstacle(opposing=4 + 3 * .7, ceiling=3.0), Leverage()),
        'K3 heresy: inquisitor speaks (L=.2)': (Dice(brought=4, standing=3 * .2, evidence=1.0), Obstacle(opposing=4.0, ceiling=3.0), Leverage()),
        'K4 petition (written: conduct 0; bench of one)': (Dice(brought=4, conduct=0.0), Obstacle(opposing=None, default=2.0, ceiling=3.0), Leverage()),
        'K5 panel member determine (judge N vs party N/2)': (Dice(brought=4, standing=3 * .5), Obstacle(opposing=4.0, ceiling=3.0), Leverage()),
        'K6 parliament speech (rank order; count decides)': (Dice(brought=4, standing=1.0), Obstacle(opposing=None, default=2.0, ceiling=3.0), Leverage(fit=0.5)),
        'K7 display (no disposes; each hearer privately)': (Dice(brought=4, conduct=1.0, latitude=1.0), Obstacle(opposing=None, default=2.0, ceiling=3.0), Leverage()),
    }
    for name, (d, o, l) in scen.items():
        for scale in (0.5, 1.25, 3.0):               # 2D / 5D / 12D actors: scale the brought term
            n_target = {0.5: 2.0, 1.25: 5.0, 3.0: 12.0}[scale]
            d2 = replace(d, brought=max(0.0, n_target - (d.total() - d.brought))) if n_target > (d.total() - d.brought) else replace(d, brought=0.0)
            opp = o.opposing if o.opposing is None else o.opposing * scale
            o2 = replace(o, opposing=opp)
            ob = model_ob(o2); Nn = d2.total()
            r = random.Random(rnd.randrange(2 ** 31)); k = [0, 0, 0, 0]; m = 0; t_end = time.time() + per
            while time.time() < t_end and m < 60000:
                for _ in range(400):
                    x = model_roll(d2, o2, l, r); m += 1
                    k[0] += x >= 0; k[1] += x >= 1; k[2] += x >= 3; k[3] += x < 0
            cf = bands(max(Nn, 1.0), l.s(), ob)
            log.w('trial', section='kinds', contest_kind=name, actor_N=round(Nn, 2), ob=round(ob, 3), s=l.s(), n=m,
                  p_fail=rate(k[3], m), p_meets=rate(k[0], m), p_succ=rate(k[1], m), p_overw=rate(k[2], m),
                  closed_form_meets=round(cf[0], 4), stop='n>=60000 or slice')
    # decider-is-a-choice kinds: the draw only moves what they hold -- no outcome distribution exists without the choice rule
    for kind in ('K1 dyadic (target decides)', 'K2 negotiation (both commit)', 'K6 parliament (count)', 'K7 display (each hearer)'):
        log.w('unverified', section='kinds', contest_kind=kind, what='the outcome is a person\'s own choice reading what the draw moved; P1 B5 builds that choice (disposition/matter term/`commit_count`); no outcome distribution is computable beyond the draw band')
    # panel: P(majority of m judges determine Success+) with the same per-judge p
    for m_judges in (1, 2, 7, 21):
        q = p_success(1 + 2.0, 6.7, 0.0)                         # pious-church Cardinal-like: P(Success+)
        # majority needs > m/2
        pm = sum(math.comb(m_judges, j) * q ** j * (1 - q) ** (m_judges - j) for j in range(m_judges // 2 + 1, m_judges + 1))
        tie = (math.comb(m_judges, m_judges // 2) * q ** (m_judges // 2) * (1 - q) ** (m_judges // 2)) if m_judges % 2 == 0 else 0.0
        log.w('result', section='kinds.panel_majority', bench=m_judges, per_judge_p_success=round(q, 4), P_strict_majority=round(pm, 4), P_exact_tie=round(tie, 4),
              note='K5: independent per-judge determine draws (MODEL; P1 does not say how members\' degrees are counted against `quorum`)')
    # one-at-a-time sensitivity around the reference (4 brought, N=5 vs equal)
    base_d = Dice(brought=4.0, standing=1.0); base_o = Obstacle(opposing=5.0, ceiling=3.0); base_l = Leverage()
    def pm(d, o, l):
        return p_success(model_ob(o), max(1.0, d.total()), l.s())
    b = pm(base_d, base_o, base_l)
    tests = [('brought +1D', replace(base_d, brought=5.0), base_o, base_l), ('conduct x latitude +1D', replace(base_d, conduct=1.0), base_o, base_l),
             ('standing +1D (title/seat x L)', replace(base_d, standing=2.0), base_o, base_l), ('faction +1D', replace(base_d, faction=1.0), base_o, base_l),
             ('evidence +1D', replace(base_d, evidence=1.0), base_o, base_l), ('opponent +1D', base_d, replace(base_o, opposing=7.0), base_l),
             ('aptness price +1 Ob', base_d, replace(base_o, aptness=1.0), base_l), ('ceiling 3 -> None (opp 5 -> Ob 2.5, not binding)', base_d, replace(base_o, ceiling=None), base_l),
             ('fit +0.5 s', base_d, base_o, Leverage(fit=0.5)), ('circumstance +0.5 s', base_d, base_o, Leverage(circumstance=0.5)),
             ('fit +1.5 s (soft-capped)', base_d, base_o, Leverage(fit=1.5)), ('L .2 -> .9 on standing 3', replace(base_d, standing=3 * .9), base_o, base_l)]
    out = []
    for nm, d, o, l in tests:
        out.append((nm, round(pm(d, o, l) - b, 4)))
    log.w('result', section='kinds.sensitivity', base_p_meets=round(b, 4), one_at_a_time_delta_p_meets=dict(out),
          ranking=[x[0] for x in sorted(out, key=lambda x: -abs(x[1]))])
    # which parameter moves the outcome most per its plausible RANGE, at 2D 5D 12D
    for N in (2.0, 5.0, 12.0):
        ob = N / 2.0
        dn = p_success(ob, N + 1, 0.0) - p_success(ob, N, 0.0)
        so = p_success(ob, N, 0.5) - p_success(ob, N, 0.0)
        oo = p_success(ob + 1, N, 0.0) - p_success(ob, N, 0.0)
        log.w('result', section='kinds.sigma_vs_dice', N=N, d_p_per_die=round(dn, 4), d_p_per_half_sigma=round(so, 4), d_p_per_Ob=round(oo, 4), half_sigma_in_dice_equiv=round(so / dn if dn else float('nan'), 2),
              note="AR: 'one sigma is 0.8 sqrt(N) Ob points' - the exchange rate rises with N; half a sigma buys more dice-equivalents at 12D than at 2D")


def sec_pace(log):
    """(S4) throughput: acts to a disposal under the scene budget 5 and one tick/season; MODEL on real p_success."""
    log.w('section_start', section='pace')
    log.w('claim', where='P1 §3.6, §6 B5', text='"Partial on an act about a docketed matter leaves it docketed for the next sitting (R-17)"; a bench disposes via `determine`; scene budget 5, one tick per season')
    for label, (Nj, Np) in {'church pious (judge 6.7 v party 4)': (6.7, 4.0), 'church weak (4.6 v 4)': (4.6, 4.0), 'default flat 4D v 4D': (4.0, 4.0), '2D judge v 4D party': (2.0, 4.0), '12D judge v 4D': (12.0, 4.0)}.items():
        ob = min(Np / 2.0, 3.0)
        pP = p_success(ob, Nj, 0.0); pS = p_success(ob + 1, Nj, 0.0)
        # a disposal needs a Success+ determine in P1's reading (Partial re-dockets); the shipped code opens a Partial-graded disposal too
        q = pS
        qship = pP
        ks = {k: round(1 - (1 - q) ** k, 4) for k in (1, 2, 4, 8, 12)}
        log.w('result', section='pace.determine', case=label, p_meets=round(pP, 4), p_success_plus=round(pS, 4),
              expected_sittings_to_dispose_P1=round(1 / q, 2), P_disposed_within_k_sittings=ks,
              expected_sittings_if_Partial_also_disposes_shipped_reading=round(1 / qship, 2))
    # one sitting per season: how many acts does a full heresy proceeding need? accuser speak, accused speak, judge determine = 3 acts; budget 5 per person-season
    log.w('result', section='pace.acts_per_proceeding', acts={'K3 forensic minimum': 3, 'with one reply each': 5, 'budget_per_person_per_season': 5},
          note='a proceeding is a run of single draws (P1 §1); no staging means 3 acts minimum, within the budget of 5; the number of SEASONS is set by P(Success+) of the bench draw (above), not by acts')
    log.w('result', section='pace.stalls', empty_bench='judging_set empty -> the date lapses (world_q.py:567-570 docstring); judge-never-acts -> computed play rolled determine 0 times (audit §8) - S6 below checks the real code',
          impasse='mutual: no commit by both -> impasse; P1 gives no escape (R-1 accepts it)')


def sec_failure(log):
    """(S6) failure injection on the REAL code (hand-built world from the tests' own helper) and REAL realm."""
    log.w('section_start', section='failure')
    from engine.season.tests import test_u7_remit as U
    from engine.season.queries import world_q as wq
    from engine.season.harness.populated import build_realm
    # (e) R-11: many matters about one party vs the docket refusal (effects_information.py:341)
    log.w('claim', where='P1 §7 / comparison §4', text="R-11's many lines of adjudication 'met only as one matter per draw, many docket items per sitting'; assessors: open_case refuses a second item on a docketed matter (:341)")
    for n_matters in (1, 2, 5, 50):
        w, d = U._world(**U.JUDGE)
        kinds = []
        for i in range(n_matters):
            out = U._fold(w, d, U._open(f'oc{i}', subject=U.PARTY))
            kinds.append(U._kinds(out))
        opened = sum(1 for k in kinds if 'case.opened' in k)
        refused = sum(1 for k in kinds if 'case.refused' in k)
        log.w('trial', section='failure.many_matters_one_party', n_matters_attempted=n_matters, opened=opened, refused=refused, docket_items_naming_party=len(wq.docketed(w, U.PARTY)), first_kinds=kinds[:3])
        if n_matters > 1 and opened < n_matters:
            log.w('fail', section='failure.many_matters_one_party', what=f"{n_matters} matters about ONE party: {opened} docketed, {refused} refused by open_case's `docketed(w, matter)` decline (the docket is keyed on the party)",
                  proposal_said='P1 §7: many docket items per sitting; R-11 met as one matter per draw', observed=f'opened={opened} refused={refused}', where='engine/season/loop/effects_information.py:341 (decline)')
    # many matters about DIFFERENT parties: possible?
    w, d = U._world(**U.JUDGE)
    other = [p for p in w.persons if p not in (U.PARTY,)][:3]
    log.w('result', section='failure.many_parties', persons_in_tiny_world=len(w.persons), note='tiny_world holds 3 persons; one matter per DISTINCT party is the only plural docket P1 can have')
    # kill the judge / revoke the seat / vacate the bench, on the tiny world: does determine still run?
    def determine_kinds(mutate, label):
        w, d = U._world(**U.JUDGE)
        U._fold(w, d, U._open('setup'))
        mutate(w)
        out = U._fold(w, d, U._determine('dd'))
        return U._kinds(out), len(wq.judging_set(w, w.rungs and 'Hh'))
    base_k, base_n = determine_kinds(lambda w: None, 'control')
    log.w('result', section='failure.control', determine_kinds=base_k, bench_size=base_n, note='control: unmodified tiny world; the real determine executes')
    def revoke_seat(w):
        for t in w.tenures:
            if t.kind == 'hold' and t.object == U.SEAT and t.live:
                t.until = w.tick
    def kill_judge(w):
        w.persons.pop(U.DUKE, None)
    def vacate(w):
        for t in w.tenures:
            if t.kind == 'hold' and t.live:
                t.until = w.tick
    for label, fn in (('revoke the seat', revoke_seat), ('kill/remove the judge from persons', kill_judge), ('vacate every seat', vacate)):
        try:
            k, n = determine_kinds(fn, label)
            log.w('trial', section='failure.judge', injected=label, determine_kinds=k, bench_size_after=n, differs_from_control=(k != base_k))
        except Exception as e:
            log.w('error', section='failure.judge', injected=label, type=type(e).__name__, message=str(e)[:300], traceback=traceback.format_exc())
            log.w('fail', section='failure.judge', what=f'injecting "{label}" raises {type(e).__name__} inside the real determine/open path instead of refusing', observed=str(e)[:200])
    # a party with no capability: the real roll pool defaults (pool_default) - nothing to inject on the model side, real side: capability dict empty
    w = build_realm(0)
    log.w('result', section='failure.no_capability', persons=len(w.persons), with_capability=sum(1 for p in w.persons.values() if p.capability),
          note='every real person is a party with no capability; the live roll uses pool_default for all, P1 sets it to 4D')
    # two authorities open a case on one matter: real code refuses the second
    w, d = U._world(**U.JUDGE)
    o1 = U._fold(w, d, U._open('a1')); o2 = U._fold(w, d, U._open('a2'))
    log.w('result', section='failure.two_authorities_one_matter', first=U._kinds(o1), second=U._kinds(o2),
          note='the live docket is keyed on the matter, not on (matter, authority): a second authority\'s case on the same matter is refused. P1 §3.6 says the gate "refuses a docket item for a matter already determined under the SAME authority" - i.e. different-authority duplicates must be admitted; the live decline admits none')
    if 'case.refused' in U._kinds(o2) or 'case.opened' not in U._kinds(o2):
        log.w('fail', section='failure.two_authorities_one_matter', what="a second open_case on the same matter is refused by the live code regardless of authority; P1's appeal path ('petition plus carry to a row of that authority', a docket item for the SAME matter under ANOTHER authority) needs `docketed` re-keyed (matter, authority) - not listed among P1 §5's Changes",
              proposal_said='P1 §3.6: an appeal is petition plus carry to a row of that authority', observed=U._kinds(o2))
    # seize/burn the case file: P1 has no case file object
    log.w('skipped', section='failure.case_file', what='seize or burn the case file', why='P1 has no case-file object (that is P2). The docket item is a dict on World.docket; the only record minted is the generic `text` Record that open_case mints')
    log.w('skipped', section='failure.defy', what='a judge who never acts', why='covered by the real-run count (S7: determine attempts) and by the empty-bench injection above')


def sec_void_appeal(log):
    """(d) `void` appeal disposal and the closure-basis gap; REAL gate/arrangements loader in the SCRATCH worktree only (see --wt)."""
    log.w('section_start', section='void_appeal')
    log.w('claim', where='P1 §3.6', text="the appeal row's `disposes: void` closes the lower edge when it finds for the appellant")
    wt = os.environ.get('P1_WT')
    if not wt or not os.path.isdir(wt):
        log.w('blocked', section='void_appeal', why='no scratch worktree given (P1_WT)', at='stress_p1.py::sec_void_appeal')
        return
    log.w('result', section='void_appeal.mode', note='run through stress_p1_void.py in the scratch worktree process; see that log')



def sec_extremes(log):
    """(S1) extremes on the REAL obstacle/refusal functions and the MODEL composition."""
    log.w('section_start', section='extremes')
    log.w('claim', where='P1 §3.2 / Q2', text='ceiling 3 "binds only where an opponent exceeds 6D"; S27.4 refusal (host adapter, sigma.py:273) is unchanged')
    # opposing in dice, N in dice: the real obstacle() (ceiling 3 and None) and the real S27.4 line:  ob > multiple * max(pool, 0)
    refused = Counter(); table = []
    for N in (0.0, 0.5, 1.0, 1.25, 1.5, 2.0, 5.0, 12.0, 30.0):
        for opp in (0.0, 1.0, 2.0, 4.0, 6.0, 8.0, 12.0, 60.0, 1e9):
            for ceil in (3.0, None):
                o = Obstacle(opposing=opp, ceiling=ceil, default=2.0)
                ob = model_ob(o)
                ref = ob > 2.0 * max(N, 0)           # the live line, sigma.py:273 (pool = the record's own pool)
                refused[(N, ceil)] += ref
                table.append({'N': N, 'opp': opp, 'ceiling': ceil, 'ob': round(ob, 3), 'S27.4_refused': ref,
                              'p_meets': None if ref else round(p_success(ob, max(N, 1.0), 0.0), 4)})
    log.w('result', section='extremes.obstacle_grid', rows=len(table), refused_with_ceiling3={str(k[0]): v for k, v in refused.items() if k[1] == 3.0},
          refused_without_ceiling={str(k[0]): v for k, v in refused.items() if k[1] is None}, sample=[t for t in table if t['N'] in (0.0, 1.0, 5.0, 30.0) and t['opp'] in (0.0, 2.0, 8.0, 1e9)][:24])
    n_ref = [t for t in table if t['S27.4_refused'] and t['ceiling'] == 3.0]
    if n_ref:
        lowest = max(t['N'] for t in n_ref)
        log.w('fail', section='extremes.S27_4', what=f"with P1's ceiling 3, S27.4 (ob > 2 x pool) REFUSES an act outright for every actor with N below 1.5 (largest refused N={lowest}) facing an opponent of 4D or more (Ob >= 2): P1 uses 3 and says it 'binds only where an opponent exceeds 6D' - it does not state this interaction",
              proposal_said='P1 Q2: "P1 uses 3; it binds only where an opponent exceeds 6D"; R-16 priced-not-refused', observed=f'{len(n_ref)} of the grid cells refused (ceiling 3)', where='engine/season/seam/wrappers/sigma.py:273-275')
    # zero ceiling, below OB_MIN: refused by the real obstacle()
    for ceil in (0.0, 0.99, 1.0):
        try:
            v = model_ob(Obstacle(opposing=8.0, ceiling=ceil))
            log.w('result', section='extremes.ceiling', ceiling=ceil, ob=v)
        except ValueError as e:
            log.w('result', section='extremes.ceiling', ceiling=ceil, raised='ValueError', message=str(e)[:90], note='REAL obstacle(): a ceiling below OB_MIN is refused')
    # weights: zero, huge, negative, NaN on the dice total
    for label, d in {'all weights zero (brought only)': Dice(brought=4.0), 'huge standing 1e9': Dice(brought=4.0, standing=1e9), 'negative standing -10 (total < 0)': Dice(brought=4.0, standing=-10.0),
                     'NaN standing': Dice(brought=4.0, standing=NAN), 'inf standing': Dice(brought=4.0, standing=INF), 'brought 0, nothing else': Dice(brought=0.0)}.items():
        try:
            x = [model_roll(d, Obstacle(opposing=4.0, ceiling=3.0), Leverage(), random.Random(i)) for i in range(2000)]
            fin = [v for v in x if v == v and abs(v) != INF]
            log.w('trial', section='extremes.weights', case=label, N=repr(d.total()), n=len(x), finite=len(fin), mean_margin=round(sum(fin) / len(fin), 3) if fin else None,
                  p_meets=rate(sum(1 for v in fin if v >= 0), len(fin)) if fin else None)
            if d.total() != d.total() or d.total() == INF or d.total() < 0:
                log.w('fail', section='extremes.weights', what=f"{label}: the draw accepts a non-finite or negative pool total without refusal (floors/propagates silently)", observed=f'N={d.total()!r} finite draws={len(fin)}/{len(x)}', proposal_said='P1 §3.2 weights are data; no domain stated')
        except Exception:
            log.w('error', section='extremes.weights', case=label, traceback=traceback.format_exc())
    # legitimacy 0 and 1 in the standing term for a seat weight 3
    for L in (0.0, 1.0):
        d = Dice(brought=4.0, standing=3.0 * L)
        log.w('result', section='extremes.L', L=L, N=d.total(), p_meets_vs_equal4D=round(p_success(model_ob(Obstacle(opposing=4.0)), d.total(), 0.0), 4), p_meets_vs_equal_seat_holder=round(p_success(model_ob(Obstacle(opposing=4.0 + 3.0 * L)), d.total(), 0.0), 4),
              note='L=0 removes the seat term from both sides: a hostile territory leaves the seat holder at default 4D')
    # leverage extremes
    for sgm in (-1e9, -3.0, 0.0, 3.0, 1e9, NAN):
        try:
            b = net_boost(sgm, 5.0); log.w('result', section='extremes.sigma', s=repr(sgm), net_boost=repr(b), p_success=repr(p_success(2.5, 5.0, sgm)))
        except Exception:
            log.w('error', section='extremes.sigma', traceback=traceback.format_exc())
    log.w('result', section='extremes.sigma_cap', s_big=repr(p_success(6.0, 5.0, 1e9)), s_at_cap=repr(p_success(6.0, 5.0, 1.5)), note='AR G1(b): 5D v Ob 6 with sigma at its limit -> about 23%')
    # panel / count
    q = 0.4386
    for k in (1, 2, 7, 21):
        maj = sum(math.comb(k, j) * q ** j * (1 - q) ** (k - j) for j in range(k // 2 + 1, k + 1))
        log.w('result', section='extremes.bench', bench=k, per_judge_p=q, P_strict_majority=round(maj, 4),
              note='MODEL: iid judges. Real benches in build_realm top out at 4 (S5); 7 and 21 exist only as a count-of-commits case (K6)')
    # unknown row, missing authority: REAL loader/gates
    try:
        from engine.season.data import arrangements as AR
        log.w('result', section='extremes.unknown_row', has_nope=('nope' in AR.ARRANGEMENTS), keys_declared=sorted(AR._ARRANGEMENT_KEYS))
        try:
            AR._refuse_unknown({'id': 'x', 'authority': 'church'}, AR._ARRANGEMENT_KEYS, 'x', 'arrangement')
            log.w('result', section='extremes.authority_key', accepted=True)
        except SystemExit as e:
            log.w('result', section='extremes.authority_key', accepted=False, message=str(e)[:200],
                  note='REAL loader: `authority:` is an unknown key today (a row carrying it is rejected at load); P1 adds it - what a row WITHOUT it means is not stated')
        from engine.season.tests import test_u7_remit as U
        w, d = U._world(**U.JUDGE)
        k = U._kinds(U._fold(w, d, U._act('oc', 'open_case', subject=U.PARTY, arrangement='nope')))
        log.w('trial', section='extremes.unknown_row_open_case', n=1, kinds=k, note='REAL open_case with an unknown arrangement id declines (case.refused)')
        log.w('unverified', section='extremes.missing_authority', what='a row with no `authority:` / a body or faction spelling missing from the `authorities:` map: P1 §3.7 states neither a default nor a refusal; `legitimacy_share` of an unmapped authority is undefined')
    except Exception:
        log.w('error', section='extremes.rows', traceback=traceback.format_exc())


def sec_real(log):
    """(S7) determinism and wall-time on the REAL season loop (build_realm seed 0, shipped chooser), plus whether the existing machinery reaches determine/speak."""
    from stress_probe import make_world, kind_counts, P
    log.w('section_start', section='real')
    res = []
    for rep in (1, 2):
        t0 = time.time(); w, d, ch = make_world(0, None, None); tb = time.time() - t0
        ev = []
        for sn in range(2):
            t = time.time(); d.season(ch, question=None, subsistence=P.SUBSIST, contest_max_depth=w.fixtures.get('contest_max_depth')); ev.append(round(time.time() - t, 1))
        kc = kind_counts(w)
        h = w.content_hash()
        res.append((h, dict(kc)))
        log.w('trial', section='real.season', rep=rep, seasons=2, build_s=round(tb, 1), season_wall_s=ev, content_hash=h, n_events=sum(kc.values()),
              interesting={k: v for k, v in kc.items() if k.startswith(('matter.', 'determine', 'case.', 'speech', 'argument', 'petition', 'commitment', 'oblige', 'ban', 'detention'))})
    same_hash = res[0][0] == res[1][0]; same_counts = res[0][1] == res[1][1]
    log.w('result', section='real.determinism', same_content_hash=same_hash, same_event_kind_counts=same_counts, hash=res[0][0],
          falsifier='two builds+runs of seed 0 differing in hash or counts; held if both equal', control='compare to seed 1 below')
    if not (same_hash and same_counts):
        log.w('fail', section='real.determinism', what='same seed, two runs: hash or event counts differ', observed={'hash': [res[0][0], res[1][0]]})
    w1, d1, ch1 = make_world(1, None, None); d1.season(ch1, question=None, subsistence=P.SUBSIST, contest_max_depth=w1.fixtures.get('contest_max_depth'))
    log.w('result', section='real.determinism_control', seed1_hash_1season=w1.content_hash(), seed0_hash_2seasons=res[0][0], differs=(w1.content_hash() != res[0][0]),
          note='a different seed gives a different hash: the instrument can see a difference')
    interesting = res[0][1]
    log.w('result', section='real.reach', determine_events={k: v for k, v in interesting.items() if 'determine' in k or k.startswith('matter.')}, note='P1 inherits the dead core: computed play reaches `determine` rarely/never (audit 8); this is what two seasons of the shipped chooser did')
    log.w('skipped', section='real.large_realm', what='a large realm', why='build_realm(seed, cap) builds the authored roster (83 persons); there is no larger builder, and seeds 0-2 are identical in roster, offices and commits (S5), so scale was not varied')

def sec_equals_curve(log):
    """(S2/S3) P(meets) for an actor against an EQUAL opponent as the pool grows, with P1's ceiling (3) and without: is the status-quo bias monotone?"""
    log.w('section_start', section='equals_curve')
    log.w('claim', where='P1 §8 Q5 / §3.2', text='"an act against an equal fails 61% of the time at 5D" (R-5 divide-by-2); the ceiling 3 "binds only where an opponent exceeds 6D"')
    rows = []
    for N in (1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 16, 20, 30):
        ob_free = N / 2.0
        ob_cap = min(ob_free, 3.0)
        rows.append({'N': N, 'p_meets_no_ceiling': round(p_success(ob_free, N, 0.0), 4), 'p_meets_ceiling3': round(p_success(ob_cap, N, 0.0), 4),
                     'p_succ_no_ceiling': round(p_success(ob_free + 1, N, 0.0), 4), 'p_succ_ceiling3': round(p_success(ob_cap + 1, N, 0.0), 4)})
    log.w('result', section='equals_curve', rows=rows)
    nm = [r['p_meets_no_ceiling'] for r in rows]; cm = [r['p_meets_ceiling3'] for r in rows]
    mono_free = all(b <= a + 1e-9 for a, b in zip(nm, nm[1:])); mono_cap = all(b >= a - 1e-9 for a, b in zip(cm, cm[1:]))
    log.w('result', section='equals_curve.verdict', p_meets_vs_equal_never_rises_with_N_without_ceiling=mono_free,
          p_meets_vs_equal_with_ceiling3_min_at_N=min(rows, key=lambda r: r['p_meets_ceiling3'])['N'], p_meets_vs_equal_at_30D_ceiling3=rows[-1]['p_meets_ceiling3'],
          p_meets_vs_equal_at_30D_no_ceiling=rows[-1]['p_meets_no_ceiling'], falsifier='a monotone curve')
    if not mono_free or min(cm) < cm[-1] - 0.05:
        log.w('fail', section='equals_curve', what=f"with ceiling 3 the odds of an act against an EQUAL are non-monotone in pool: they fall to {min(cm)} (N={min(rows, key=lambda r: r['p_meets_ceiling3'])['N']}D) then climb to {cm[-1]} at 30D, "
              "so 'the world resists change' (61% fail at 5D) holds only for small pools and inverts for masters; P1 says only that the ceiling 'binds where an opponent exceeds 6D'",
              proposal_said='P1 §8 Q5 / Q2', observed={'ceiling3': cm, 'free': nm})


def rollcall(paths):
    """Print the mandatory complete roll-call (every fail / null / blocked / skipped / unverified / error line, in file order) as markdown."""
    kinds = ('fail', 'null', 'blocked', 'skipped', 'unverified', 'error')
    out = []
    for path in paths:
        name = os.path.basename(path)
        for i, line in enumerate(open(path, encoding='utf-8'), 1):
            try:
                r = json.loads(line)
            except Exception:
                out.append(f'- `{name}:{i}` UNPARSEABLE LINE {line[:80]!r}'); continue
            if r.get('kind') in kinds:
                body = r.get('what') or r.get('why') or r.get('message') or r.get('examined') or r.get('traceback', '')[-160:] or ''
                sect = r.get('section') or r.get('step') or r.get('label') or ''
                if r.get('kind') == 'skipped' and r.get('file'):
                    body = f"{r['file']}: {r.get('why', '')}"
                out.append(f"- `{name}:{i}` **{r['kind']}** [{sect}] {str(body)[:230]}")
    print('\n'.join(out))


SECTIONS = {}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--log', default=os.devnull)
    ap.add_argument('--sections', default='leg,model,chan,regard,bench,dom,kinds,pace,fail,extremes,real')
    ap.add_argument('--budget-s', type=float, default=900)
    ap.add_argument('--rollcall', nargs='*', help='print the roll-call of these logs and exit')
    a = ap.parse_args()
    if a.rollcall:
        rollcall(a.rollcall); return
    log = Log(a.log)
    log.w('manifest', label='attempt-2 (attempt-1 lines above in this file are kept: see its fails for the harness artefacts it fixed)', argv=sys.argv, head=git('rev-parse', 'HEAD'), branch=git('rev-parse', '--abbrev-ref', 'HEAD'),
          dirty=git('status', '--porcelain')[:300], python=sys.version.split()[0], platform=sys.platform,
          pythonhashseed=os.environ.get('PYTHONHASHSEED'), worktree=os.environ.get('P1_WT'), proposal='P1 one-draw', ob_min=OB_MIN)
    secs = [s for s in a.sections.split(',') if s]
    log.w('plan', sections=secs, budget_s=a.budget_s, stopping_rule='each sampled cell stops at a stated standard error or its wall-clock slice; the run stops on the first of: crash, all sections done, budget')
    share = a.budget_s / max(1, len(secs))
    table = {'leg': lambda: sec_legitimacy(log), 'model': lambda: sec_model_closed_form(log, share * 1.4), 'chan': lambda: sec_channels(log),
             'regard': lambda: sec_regard(log, share * 0.7), 'bench': lambda: sec_bench(log), 'dom': lambda: sec_dominance(log),
             'kinds': lambda: sec_kinds(log, share), 'pace': lambda: sec_pace(log), 'fail': lambda: sec_failure(log), 'extremes': lambda: sec_extremes(log), 'real': lambda: sec_real(log), 'equals': lambda: sec_equals_curve(log)}
    for s in secs:
        if time.time() - T0 > a.budget_s:
            log.w('skipped', section=s, why='wall-clock budget exhausted before this section started', stop='budget')
            continue
        t = time.time()
        try:
            table[s]()
        except Exception as e:
            log.w('error', section=s, type=type(e).__name__, message=str(e)[:400], traceback=traceback.format_exc())
        log.w('result', section=s, wall_s=round(time.time() - t, 1), stop='section complete')
    log.w('summary', wall_s=round(time.time() - T0, 1), stop='all sections done or budget')


if __name__ == '__main__':
    main()
