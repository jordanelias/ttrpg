#!/usr/bin/env python3
"""Proposal 4 (authority first, staged hearing): are the player's choices real?

MODEL, not code: every hearing chain, plea table, payoff weight and hidden-state prior below is the
proposal's design written as arithmetic, evidence about the DESIGN and not about the tree. What is REAL:
the dice engine (`engine/dice_engine/sigma_leverage.py::p_success`, `roll_net`, `roll_net_continuous`,
`net_boost`) and the ladder (`engine/dice_engine/dice_engine.py::degree_from_net`), used for every band
probability. Nothing here imports `engine/season/`: no proposal-4 code exists to run.

Convention (PR #530's): one flushed, fsynced JSON line per event; `manifest` first; `plan`, `claim`,
`result`, `summary`; `fail` / `null` / `blocked` / `skipped` / `unverified` / `error` for everything that
did not work, false starts kept (the log is opened in APPEND mode and never truncated by this script).
Closed-form band probabilities are exact (no n); the Monte-Carlo controls carry n and a Wilson 95% interval.

THE TEST OF A REAL CHOICE (stated once, applied to every section):
  goods are a vector, oriented higher = better (severity avoided, standing kept, seasons saved, risk
  avoided, and section-specific goods). For each VISIBLE configuration at a pool N, payoffs are averaged
  over the HIDDEN states' prior. An option is
    * Pareto-dominated in a configuration if another option is >= on every good and > on one (weak), or
      > on every good (strict);
    * "ever best" if some weighting of the goods (a grid) makes it the scalar best in some configuration.
  An option SURVIVES at pool N if it is Pareto-undominated in >= 1 configuration at N AND ever best at N.
  A CHOICE survives at N if every one of its options survives. Dominated options are reported, not hidden.

Run:  python proposals/2026-10-29-parliament-and-debate/stress_p4_choices.py [--log PATH] [--mc N]
"""
from __future__ import annotations

import argparse, itertools, json, math, os, platform, random, subprocess, sys, time, traceback
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)

from engine.dice_engine import sigma_leverage as SL          # noqa: E402  (REAL)
from engine.dice_engine.dice_engine import degree_from_net    # noqa: E402  (REAL)

DEFAULT_LOG = os.path.join(HERE, "2026-11-01-stress-log-p4-choices.jsonl")
POOLS = (2, 5, 12)
CEILINGS = {"r37_3": 3.0, "live_2": 2.0, "none": None}
HEADLINE_CEILING = "r37_3"
SEV = {3: 1.00, 2: 0.75, 1: 0.35, 0: 0.10}          # Overwhelming, Success, Partial, admonition (on record, no edge)
SEV_LINEAR = {3: 1.0, 2: 2 / 3, 1: 1 / 3, 0: 0.0}   # control scale
DEG = {"O": 3, "S": 2, "P": 1}


# ----------------------------------------------------------------------------------------------- log
class Log:
    def __init__(self, path):
        self.path = path
        self.f = open(path, "a", encoding="utf-8")
        self.counts = defaultdict(int)

    def w(self, kind, **kw):
        rec = {"t": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "kind": kind}
        rec.update(kw)
        self.f.write(json.dumps(rec, default=_jsonable, sort_keys=False) + "\n")
        self.f.flush()
        os.fsync(self.f.fileno())
        self.counts[kind] += 1

    def close(self):
        self.f.close()


def _jsonable(o):
    if isinstance(o, float) and (math.isnan(o) or math.isinf(o)):
        return str(o)
    if isinstance(o, (set, frozenset, tuple)):
        return list(o)
    return str(o)


def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (round(c - h, 4), round(c + h, 4))


# ---------------------------------------------------------------------------------------- the draw
_BLOCKED = set()
LOG = None


def ob_of(score, ceiling, mod=0.0, apt=0.0):
    """P4's obstacle: the opposing SCORE halved and bounded by the ceiling (R-5, R-37), THEN the instance
    modifiers (the defender's offered proofs, halved) and the act's own aptness price (R-16), which the
    ceiling does not clip. (Departure D-4 of the proposal; the live `roll.obstacle` clips after the room.)"""
    base = score / 2.0
    if ceiling is not None:
        base = min(base, ceiling)
    return base + mod / 2.0 + apt


def bands(N, ob, s=0.0, section="?"):
    """O/S/P/F probabilities from the REAL closed form `p_success` (meets = margin >= 0)."""
    if ob > 2 * max(N, 1.0):
        key = (section, N, round(ob, 3))
        if key not in _BLOCKED and LOG is not None:
            _BLOCKED.add(key)
            LOG.w("blocked", section=section, what="S27.4 would refuse this act (Ob > 2 x pool); treated as a Failure (held), against R-16's 'priced, never refused'",
                  pool=N, ob=round(ob, 3))
        return {"O": 0.0, "S": 0.0, "P": 0.0, "F": 1.0}
    p0 = SL.p_success(ob, N, s)
    p1 = SL.p_success(ob + 1, N, s)
    p3 = SL.p_success(ob + 3, N, s)
    return {"O": p3, "S": p1 - p3, "P": p0 - p1, "F": 1 - p0}


def stage(N, ob, s=0.0, tries=3, section="?"):
    """A contested stage under repair (e): a Failure HOLDS the matter for the next sitting; the third
    Failure closes the stage against the roller. Returns branches (prob, outcome, sittings)."""
    b = bands(N, ob, s, section)
    out = []
    for k in range(1, tries + 1):
        lead = b["F"] ** (k - 1)
        for o in ("O", "S", "P"):
            out.append((lead * b[o], o, k))
    out.append((b["F"] ** tries, "closed", tries))
    return out


def stage_p2_as_written(N, ob, s=0.0, section="?"):
    """CONTROL: P2 as written -- a Failure ends the stage against the roller at once (no hold)."""
    b = bands(N, ob, s, section)
    return [(b["O"], "O", 1), (b["S"], "S", 1), (b["P"], "P", 1), (b["F"], "closed", 1)]


# ----------------------------------------------------------------------------------- the hearing
def judgment(P, cap, k0, stage_fn, sev):
    """The bench's determine grades the disposal; the concession/half-proof caps lower it (repair a)."""
    res = []
    for p, o, k in stage_fn(P["DJ"], ob_of(P["SR_score"], P["C"], P.get("judg_mod", 0.0)), P.get("s_judg", 0.0), section=P["section"]):
        sittings = k0 + k - 1
        if o == "closed":
            res.append((p, None, sittings, "undetermined"))
        else:
            g = max(0, DEG[o] - cap)
            res.append((p, g, sittings, "sentenced"))
    return res


def hearing(plea, P, stage_fn=stage, sev=SEV, cap_route="grade"):
    """All branches of one hearing: (prob, grade|None, sittings, how).

    WHO BEARS EACH STAGE (the rite's): the elements of the charge -- the FACT (proof) and the DEFINITION
    (that the fact is the offence) -- are the accuser's in the accusatorial rite and the bench's in the
    inquisitorial one (its qualifiers rule on the definition: research 02 2.1, 2.2); only an affirmative
    defence (justification, excuse, abjuration at a degree) is the respondent's own roll. The plea fixes
    which question is tried (litis contestatio): deny -> the fact; concede the fact -> the definition;
    concede the definition -> the justification. Each concession caps the sentence one grade (repair a)."""
    out = []
    burden = P["DJ_proof"] if P["rite"] == "inquisitorial" else P["SA"]
    if plea in ("deny", "concede_fact"):
        if plea == "deny":
            mod, cap0 = P.get("proof_mod", 0.0), 0
        else:
            mod, cap0 = P.get("writ_mod", 0.0), (0 if cap_route == "obstacle" else 1)
        Pj = dict(P, judg_mod=mod)
        for p, o, k in stage_fn(burden, ob_of(P["SR_score"], P["C"], mod, P.get("apt_proof", 0.0)),
                                P.get("s_proof", 0.0), section=P["section"]):
            if o == "closed":
                out.append((p, None, k, "acquitted"))
            elif o in ("O", "S"):
                out += [(p * q, g, s, h) for q, g, s, h in judgment(Pj, cap0, k, stage_fn, sev)]
            else:                                  # half shown: the judge's own choice (hidden)
                d = P["d_half"]
                out += [(p * d * q, g, s, h) for q, g, s, h in judgment(Pj, cap0 + 1, k, stage_fn, sev)]
                out.append((p * (1 - d), None, k, "dismissed_half_shown"))
        return out
    if plea == "justify":
        base_cap = 0 if cap_route == "obstacle" else 2
        Pq = dict(P, judg_mod=0.0)
        for p, o, k in stage_fn(P["SR_roll"], ob_of(burden, P["C"], 0.0, P["apt_just"]), P.get("s_q", 0.0), section=P["section"]):
            if o in ("O", "S"):
                out.append((p, None, k, "excused"))
            elif o == "P":
                out += [(p * q, g, s, h) for q, g, s, h in judgment(Pq, base_cap + 1, k, stage_fn, sev)]
            else:
                out += [(p * q, g, s, h) for q, g, s, h in judgment(Pq, base_cap, k, stage_fn, sev)]
        return out
    if plea == "confess":
        return judgment(dict(P, judg_mod=0.0), 2, 1, stage_fn, sev)
    if plea == "grace_confess":                    # inquisitorial term of grace: light penance, names required
        return [(1.0, 0, 1, "penance")]
    raise ValueError(plea)


CONCEDED = {"deny": 0, "concede_fact": 1, "justify": 2, "confess": 3, "grace_confess": 3}


def summarise(branches, plea, P, sev=SEV, bite=1.0):
    tot = sum(b[0] for b in branches)
    E_sev = sum(p * (sev[g] if g is not None else 0.0) for p, g, s, h in branches) * bite
    P_severe = sum(p for p, g, s, h in branches if g is not None and g >= 2)
    P_clear = sum(p for p, g, s, h in branches if g is None)
    E_seas = sum(p * (s - 1) for p, g, s, h in branches)
    wf = P.get("witness_weight", 1.0)
    st = 0.0
    for p, g, s, h in branches:
        lvl = CONCEDED[plea]
        if g is not None:
            lvl = max(lvl, 2) + (0.5 if plea == "deny" else 0.0)     # a sentence publishes fact and wrong; a disproved denial costs more
        st += p * lvl * wf
    # the inquisitio's cluster: a deponent who concedes the fact is asked who else was present (02 1.1 row 5)
    names = P.get("names_cost", 0.0) if (plea != "deny" and P.get("rite") == "inquisitorial") else 0.0
    return {"tot": round(tot, 9), "E_sev": E_sev, "P_severe": P_severe, "P_clear": P_clear, "E_seasons": E_seas,
            "E_standing_loss": st, "names": names}


# ------------------------------------------------------------------------------- dominance engine
def goods_of(s, extra=None):
    g = {"sev": -s["E_sev"], "risk": -s["P_severe"], "stand": -s["E_standing_loss"], "time": -s["E_seasons"]}
    if s.get("names"):
        g["names"] = -s["names"]
    if extra:
        g.update(extra)
    return g


def pareto(opts):
    """opts: {name: goods dict}. Returns {name: (weakly_dominated_by, strictly_dominated_by)}."""
    keys = sorted({k for g in opts.values() for k in g})
    res = {}
    for a, ga in opts.items():
        weak, strict = [], []
        for b, gb in opts.items():
            if a == b:
                continue
            ge = all(gb.get(k, 0) >= ga.get(k, 0) - 1e-12 for k in keys)
            gt = any(gb.get(k, 0) > ga.get(k, 0) + 1e-12 for k in keys)
            if ge and gt:
                weak.append(b)
            if all(gb.get(k, 0) > ga.get(k, 0) + 1e-12 for k in keys):
                strict.append(b)
        res[a] = (weak, strict)
    return res


# Goods in their own units: severity (a full sentence = 1); standing in concession LEVELS (0..3.5); seasons;
# rel = persons made enemies or implicated (1 per person); names = a cluster named to an inquisitor (1);
# keep = proofs or scenes kept unspent; partisan = legitimacy points (0..1) taken from an authority the
# chooser opposes. The grid spans what each unit might be worth in sentences; no exchange rate is asserted.
WEIGHT_GRID = [dict(sev=1.0, risk=r, stand=k, time=c, rel=e, keep=h, names=n, partisan=a, gain=1.0, liab=1.0, stand_signed=1.0)
               for r in (0.0, 0.25) for k in (0.0, 0.05, 0.1, 0.2) for c in (0.0, 0.03, 0.1)
               for e in (0.0, 0.1, 0.2) for h in (0.0, 0.05, 0.2) for n in (0.0, 0.25, 0.5) for a in (0.0, 2.0, 5.0)]


def scalar(g, w):
    return sum(w.get(k, 1.0) * v for k, v in g.items())


def best_under(opts, w):
    vals = {o: scalar(g, w) for o, g in opts.items()}
    m = max(vals.values())
    return sorted(o for o, v in vals.items() if v >= m - 1e-12)


class Tally:
    """Per (section, pool): which options are undominated somewhere and ever best."""

    def __init__(self, section, options):
        self.section, self.options = section, list(options)
        self.undom = defaultdict(lambda: defaultdict(int))
        self.best = defaultdict(lambda: defaultdict(int))
        self.cells = defaultdict(int)
        self.weak_dom_everywhere = defaultdict(lambda: defaultdict(int))
        self.headline_best = defaultdict(lambda: defaultdict(int))

    def add(self, N, opts, headline_weight=None):
        self.cells[N] += 1
        par = pareto(opts)
        for o in self.options:
            if o in opts and not par[o][0]:
                self.undom[N][o] += 1
            if o in opts and par[o][0]:
                self.weak_dom_everywhere[N][o] += 1
        seen = set()
        for w in WEIGHT_GRID:
            for o in best_under(opts, w):
                seen.add(o)
        for o in seen:
            self.best[N][o] += 1
        if headline_weight is not None:
            for o in best_under(opts, headline_weight):
                self.headline_best[N][o] += 1
        return par

    def verdict(self):
        out = {}
        for N in sorted(self.cells):
            per = {}
            for o in self.options:
                per[o] = {"undominated_cells": self.undom[N][o], "ever_best_cells": self.best[N][o],
                          "headline_best_cells": self.headline_best[N][o], "cells": self.cells[N],
                          "survives": self.undom[N][o] > 0 and self.best[N][o] > 0}
            out[N] = {"options": per, "choice_survives": all(v["survives"] for v in per.values()),
                      "options_surviving": sum(v["survives"] for v in per.values()), "of": len(self.options)}
        return out


HEADLINE_W = dict(sev=1.0, risk=0.0, stand=0.1, time=0.03, rel=0.1, keep=0.05, names=0.25, partisan=0.0, gain=1.0, liab=1.0, stand_signed=1.0)
BENCH = 5.0      # the bench's own dice; the CHOOSER's pool is the one varied over 2, 5, 12


def base_params(N, C="r37_3", rite="accusatorial", **kw):
    P = dict(SA=N, SR_score=N, SR_roll=N, DJ=BENCH, DJ_proof=BENCH, C=CEILINGS[C], rite=rite, apt_def=0.5, apt_just=0.25,
             apt_proof=0.0, d_half=0.6, witness_weight=(0.25 if rite == "inquisitorial" else 1.0), section="?")
    P.update(kw)
    return P


def best_plea(P, rite_pleas, w=HEADLINE_W, sev=SEV, bite=1.0):
    vals = {}
    for pl in rite_pleas:
        s = summarise(hearing(pl, P, sev=sev), pl, P, sev=sev, bite=bite)
        vals[pl] = (scalar(goods_of(s), w), s)
    b = max(vals, key=lambda k: (vals[k][0], k))
    return b, vals[b][1], vals


PLEAS_ACC_DRAFT = ("deny", "concede_fact", "justify", "confess")      # run 2's draft; confession cut in run 3
PLEAS_ACC = ("deny", "concede_fact", "justify")
PLEAS_INQ_DRAFT = ("deny", "concede_fact", "justify", "grace_confess")   # run 3's draft; grace moved before citation in run 4
PLEAS_INQ = ("deny", "concede_fact", "justify")


# ============================================================================================ sections
def sec_controls(log, mc_n):
    """C0: the engine pieces this harness leans on, checked against sampling (controls, not claims)."""
    log.w("plan", section="C0.controls", what="p_success bands vs roll_net_continuous and roll_net sampling; closed form E[margin] vs sample mean",
          cells=[(2, 1.0, 0.0), (5, 2.5, 0.0), (12, 3.0, 0.0), (5, 2.5, 0.5)], n=mc_n)
    rng = random.Random(20261101)
    for N, ob, s in [(2, 1.0, 0.0), (5, 2.5, 0.0), (12, 3.0, 0.0), (5, 2.5, 0.5)]:
        b = bands(N, ob, s, "C0")
        for label, sampler in (("continuous", SL.roll_net_continuous), ("discrete", SL.roll_net)):
            cnt = defaultdict(int)
            tot_m = 0.0
            for _ in range(mc_n):
                net = sampler(N, rng=rng) + SL.net_boost(s, N)
                tot_m += net - ob
                cnt[degree_from_net(net, ob).name] += 1
            meets = mc_n - cnt["FAILURE"]
            lo, hi = wilson(meets, mc_n)
            closed = 0.4 * N + 0.8 * math.sqrt(N) * SL.soft_cap(s) - ob
            agree = lo <= (1 - b["F"]) <= hi
            log.w("result", section="C0.controls", sampler=label, pool=N, ob=ob, sigma=s, n=mc_n,
                  meets_closed_form=round(1 - b["F"], 4), meets_sampled=round(meets / mc_n, 4), wilson95=[lo, hi],
                  E_margin_closed_form=round(closed, 4), E_margin_sampled=round(tot_m / mc_n, 4),
                  closed_form_inside_interval=agree)
            if not agree:
                log.w("fail" if label == "continuous" else "unverified", section="C0.controls", sampler=label, pool=N, ob=ob,
                      what=("the closed form disagrees with the sampler it models" if label == "continuous" else
                            "the discrete live path (roll_net, integer pool) differs from the continuous closed form this model uses; the proposal assumes the armature's continuous path (B8), which the live seam does not take"),
                      closed=round(1 - b["F"], 4), sampled=round(meets / mc_n, 4), wilson95=[lo, hi])


def sec_plea(log):
    """C3: the plea (Aristotle Rhet. III.15's descent, by what each concedes)."""
    log.w("claim", section="C3.plea", text="With concession paid in the disposal grade (repair a) and a Failure holding the stage (repair e), deny, concede-the-fact and justify are each a real choice at 2D, 5D and 12D; confession is real only as the inquisitorial term of grace",
          where="P4 section 4, choice 3")
    log.w("plan", section="C3.plea", options={"accusatorial": PLEAS_ACC, "inquisitorial": PLEAS_INQ, "cut": {"confess (accusatorial)": "Pareto-dominated by justify at 12D in run 2 (3 of 3 cells); Aristotle's 'hand the error back' becomes a speech kind at the quality stage"}},
          visible="rite x ceiling x accuser pool x respondent pool x he holds a writ that redefines the act {no, yes: 1.5D, an instance modifier on the DEFINITION question} x he holds a defence proof {none, 1.5D: an instance modifier on the FACT question}; bench 5D; the burden on fact and definition is the accuser's (accusatorial) or the bench's (inquisitorial), on justification the respondent's",
          hidden="d_half (the judge's discretion on a half proof) in {0.3, 0.6, 0.9} uniform",
          controls=["P2 as written: Failure ends the stage, concession rewarded in the OBSTACLE, live ceiling 2", "linear severity scale", "no ceiling"])
    talls = {}
    p2_rows = []
    for rite, pleas in (("accusatorial", PLEAS_ACC), ("inquisitorial", PLEAS_INQ)):
        for C in CEILINGS:
            T = Tally(f"C3.plea.{rite}.{C}", pleas)
            for NA, NR, writ, prf in itertools.product(POOLS, POOLS, (False, True), (0.0, 1.5)):
                opts_acc = defaultdict(lambda: defaultdict(float))
                hid = [(d, 0.0) for d in (0.3, 0.6, 0.9)]
                for d_half, _ in hid:
                    P = base_params(NR, C, rite, SA=NA, DJ=BENCH, DJ_proof=BENCH, proof_mod=prf, writ_mod=(1.5 if writ else 0.0),
                                    d_half=d_half, names_cost=1.0, section=f"C3.{rite}.{C}")
                    for pl in pleas:
                        s = summarise(hearing(pl, P), pl, P)
                        for kk, v in goods_of(s).items():
                            opts_acc[pl][kk] += v / len(hid)
                opts = {k: dict(v) for k, v in opts_acc.items()}
                par = T.add(NR, opts, HEADLINE_W)
                log.w("result", section=f"C3.plea.{rite}.{C}", NA=NA, NR=NR, writ=writ, defence_proof=prf,
                      goods={k: {kk: round(vv, 4) for kk, vv in v.items()} for k, v in opts.items()},
                      weakly_dominated={k: v[0] for k, v in par.items() if v[0]},
                      headline_best=best_under(opts, HEADLINE_W))
            talls[(rite, C)] = T
            log.w("summary", section=f"C3.plea.{rite}.{C}", verdict=T.verdict(), note="pool = the respondent's pool; cells = 3 accuser pools x writ x defence proof; the judge's half-proof discretion averaged")
    # the repair against its control: P2 as written
    for NA, NR in itertools.product(POOLS, POOLS):
        P = base_params(NR, "live_2", "accusatorial", SA=NA, DJ=BENCH, section="C3.control.p2")
        vals = {}
        for pl in ("deny", "concede_fact", "justify"):
            s = summarise(hearing(pl, P, stage_fn=stage_p2_as_written, cap_route="obstacle"), pl, P)
            vals[pl] = goods_of(s)
        hb = best_under(vals, dict(HEADLINE_W, stand=0.0, time=0.0))
        p2_rows.append(hb)
        log.w("result", section="C3.plea.control_p2_as_written", NA=NA, NR=NR, best_on_severity_alone=hb,
              goods={k: {kk: round(vv, 4) for kk, vv in v.items()} for k, v in vals.items()})
    deny_best = sum(1 for r in p2_rows if r == ["deny"])
    log.w("result", section="C3.plea.control_p2_as_written.summary", cells=len(p2_rows), deny_alone_best_on_severity=deny_best,
          note="control arm: P2's transition (Failure ends the stage) and the concession reward routed through the obstacle (here: no reward, which is what the live ceiling 2 clips it to in most cells)")
    return talls


def sec_ceiling_for_deny(log):
    """Which ceiling value keeps 'deny' a real plea at 12D? (a computed handle on G1 / R-37)"""
    log.w("plan", section="C3b.ceiling", what="deny's Pareto status at NA = NR = 12 and 5 across ceiling values 2..7 and none (accusatorial, hidden averaged)")
    for N in POOLS:
        for Cv in (2.0, 3.0, 4.0, 5.0, 6.0, 7.0, None):
            opts = defaultdict(lambda: defaultdict(float))
            hid = list(itertools.product((0.3, 0.6, 0.9), (0.0, 0.5, 1.0)))
            for d_half, apt_def in hid:
                P = base_params(N, "r37_3", "accusatorial", DJ=BENCH, d_half=d_half, apt_def=apt_def, section="C3b")
                P["C"] = Cv
                for pl in PLEAS_ACC_DRAFT:
                    s = summarise(hearing(pl, P), pl, P)
                    for kk, v in goods_of(s).items():
                        opts[pl][kk] += v / len(hid)
            opts = {k: dict(v) for k, v in opts.items()}
            par = pareto(opts)
            log.w("result", section="C3b.ceiling", pool=N, ceiling=Cv, deny_weakly_dominated_by=par["deny"][0],
                  confess_weakly_dominated_by=par["confess"][0],
                  deny_goods={k: round(v, 4) for k, v in opts["deny"].items()},
                  concede_goods={k: round(v, 4) for k, v in opts["concede_fact"].items()})


def defy_cell(rite, N, q, L, ks, C="r37_3"):
    """C1: appear / evade / defy. Bite: a polity row disposes custody (needs the arm if absent); a church
    row disposes a ban (bites as far as the territory heeds the church, ~L, present or absent)."""
    pleas = PLEAS_ACC if rite == "accusatorial" else PLEAS_INQ
    P = base_params(N, C, rite, SA=BENCH, DJ=BENCH + 1.0 * L, DJ_proof=BENCH + 1.0 * L, names_cost=1.0, section=f"C1.{rite}")
    kind = "detain" if rite == "accusatorial" else "ban"
    bite_present = 1.0 if kind == "detain" else L
    _, s_app, _ = best_plea(P, pleas, bite=bite_present)
    # in absentia: no plea, no proofs, no conduct; no resisting person -> obstacle_default 2 (H-127)
    Pa = dict(P, SR_score=4.0)                      # score 4 -> Ob 2, the default, bounded by the ceiling
    br = hearing("deny", Pa)
    p_arrest = 1 - bands(5, ob_of(N, P["C"]), 0.0, "C1.arrest")["F"]
    bite_abs = (q * p_arrest) if kind == "detain" else L
    s_abs = summarise(br, "deny", Pa, bite=bite_abs)
    # contempt (defy only): a ban the bench can open in absentia, no arm needed, bite ~ L (R-36's channel)
    cb = bands(P["DJ"], ob_of(4.0, P["C"]), 0.0, "C1.contempt")
    contempt_sev = (cb["O"] * SEV[3] + cb["S"] * SEV[2] + cb["P"] * SEV[1]) * L * (0.0 if kind == "ban" else 1.0)
    # (a church row's contempt ban and its heresy ban are ONE live edge per seat -- `_eff_determine`'s decline)
    goods = {}
    goods["appear"] = dict(goods_of(s_app), partisan=0.0, stand_signed=0.0, keep=-1.0)     # appearing costs a scene and the road
    goods["evade"] = dict(goods_of(s_abs), partisan=0.0, stand_signed=0.0, keep=0.0)
    g_def = goods_of(dict(s_abs, E_sev=s_abs["E_sev"] + contempt_sev))
    unpunished = (1 - q * p_arrest) if kind == "detain" else 0.5
    g_def.update(partisan=0.02 * unpunished, stand_signed=ks * (1 - 2 * L), keep=0.0)
    goods["defy"] = g_def
    return goods, dict(p_arrest=round(p_arrest, 4), bite_abs=round(bite_abs, 4), contempt_sev=round(contempt_sev, 4))


def sec_defy(log):
    log.w("claim", section="C1.defy", text="With the citation a served writ (repair h), contempt as a ban needing no arm, and a witnessed defiance signed by L (repair i), appear / evade / defy are each best somewhere at every pool", where="P4 choice 1")
    log.w("plan", section="C1.defy", visible="rite x q (chance the arm serves) {0,.5,1} x L {.37,.5,.78} x k_s (standing per witnessed defiance) {0,.1,.25}", hidden="none (q is the server's own later choice: visible to nobody; swept as visible here, which favours the chooser)",
          options=["appear", "evade", "defy"], goods_extra=["auth_L: damage to the defied authority's legitimacy (good for a defier hostile to it)", "stand_signed: standing gained or lost by the witnessed defiance"])
    T = Tally("C1.defy", ["appear", "evade", "defy"])
    for rite in ("accusatorial", "inquisitorial"):
        for N, q, L, ks in itertools.product(POOLS, (0.0, 0.5, 1.0), (0.37, 0.5, 0.78), (0.0, 0.1, 0.25)):
            g, aux = defy_cell(rite, N, q, L, ks)
            par = T.add(N, g, HEADLINE_W)
            log.w("result", section="C1.defy", rite=rite, pool=N, q=q, L=L, k_s=ks, aux=aux,
                  goods={k: {kk: round(vv, 4) for kk, vv in v.items()} for k, v in g.items()},
                  weakly_dominated={k: v[0] for k, v in par.items() if v[0]}, headline_best=best_under(g, HEADLINE_W))
    log.w("summary", section="C1.defy", verdict=T.verdict())
    # control: the P3-as-written arm (no contempt, no standing sign, no L effect, absent party keeps his score)
    wins = defaultdict(int)
    n = 0
    for N, q, L in itertools.product(POOLS, (0.0, 0.5, 1.0), (0.37, 0.5, 0.78)):
        P = base_params(N, "r37_3", "accusatorial", SA=BENCH, DJ=BENCH, section="C1.control")
        s_app = summarise(hearing("deny", P), "deny", P)
        p_arrest = 1 - bands(5, ob_of(N, P["C"]), 0.0, "C1.arrest")["F"]
        s_abs = summarise(hearing("deny", P), "deny", P, bite=q * p_arrest)
        n += 1
        wins["defy" if s_abs["E_sev"] < s_app["E_sev"] - 1e-12 else ("tie" if abs(s_abs["E_sev"] - s_app["E_sev"]) < 1e-12 else "appear")] += 1
    log.w("result", section="C1.defy.control_p3_as_written", cells=n, best_on_severity=dict(wins),
          note="P3's defy (the draw unchanged by defiance, custody only by warrant): defy should be weakly cheaper everywhere, as P3's stress test found 36 of 36")
    return T


def sec_forum(log):
    """C2a: where the ACCUSER brings the matter (polity accusatorial vs church inquisitorial)."""
    log.w("claim", section="C2.forum", text="Each rite is the better forum for some accuser: the church (secret, no accuser liability, the bench proves) for a weak or exposed accuser; the polity (its arm reaches; the King's weight) for a strong one", where="P4 choice 2")
    log.w("plan", section="C2.forum", visible="accuser pool DA x respondent pool DR x church L {.37,.5,.78} x church arm q {0,.5,1} x liability lambda {0,.25,.5} x exposure e {0,.05}; crown L .74; bench pool 5 both; weights King 1.5D, inquisitor 1D (R-36 term)",
          hidden="d_half {0.3,0.6,0.9}", respondent="best-responds with his best plea under each rite (headline weights)")
    T = Tally("C2.forum", ["polity", "church"])
    for DA, DR, Lc, qc, lam, e in itertools.product(POOLS, POOLS, (0.37, 0.5, 0.78), (0.0, 0.5, 1.0), (0.0, 0.25, 0.5), (0.0, 1.0)):
        acc = {}
        for auth in ("polity", "church"):
            tot = defaultdict(float)
            for d_half in (0.3, 0.6, 0.9):
                if auth == "polity":
                    P = base_params(DR, "r37_3", "accusatorial", SA=DA, DJ=BENCH + 1.5 * 0.74, d_half=d_half, section="C2.polity")
                    pl, s, _ = best_plea(P, PLEAS_ACC)
                    bite = 1.0
                    br = hearing(pl, P)
                    p_fail = sum(p for p, g, ss, h in br if h == "acquitted" and pl == "deny")
                    liab = lam * 0.75 * p_fail
                    expo = e
                else:
                    P = base_params(DR, "r37_3", "inquisitorial", SA=DA, DJ=BENCH + 1.0 * Lc, DJ_proof=BENCH + 1.0 * Lc, d_half=d_half,
                                    names_cost=1.0, section="C2.church")
                    pl, _, _ = best_plea(P, PLEAS_INQ, bite=Lc)
                    s = summarise(hearing(pl, P), pl, P)          # unscaled, so the bite is applied once
                    bite = Lc * (0.5 + 0.5 * qc)       # a ban bites by L; custody, where the row adds it, needs the arm
                    liab, expo = 0.0, 0.0
                tot["gain"] += s["E_sev"] * (bite if auth == "church" else 1.0) / 3
                tot["liab"] += -liab / 3
                tot["rel"] += -expo / 3
                tot["time"] += -s["E_seasons"] / 3
            acc[auth] = dict(tot)
        T.add(DA, acc, HEADLINE_W)
        log.w("result", section="C2.forum", DA=DA, DR=DR, L_church=Lc, q_church=qc, lam=lam, e=e,
              goods={k: {kk: round(vv, 4) for kk, vv in v.items()} for k, v in acc.items()}, headline_best=best_under(acc, HEADLINE_W))
    log.w("summary", section="C2.forum", verdict=T.verdict(), note="pool = the accuser's pool")
    return T


def sec_forum_challenge(log):
    """C2b: the respondent's forum challenge (translatio) at the issue stage; decided by precedence (R-34) and prevention."""
    log.w("plan", section="C2b.challenge", visible="sitting rite x royal party {no, yes} x respondent pool x accuser pool",
          hidden="p_claim (the other authority's seat claims the case) {.25,.5,1}; p_consent (the sitting bench consents) {0,.5}",
          rule="P(transfer) = p_claim x (1 if a royal person is a party and the claimer is the polity else p_consent); a challenge costs one sitting and, refused, 0.02 standing")
    T = Tally("C2b.challenge", ["answer", "challenge"])
    for sit, royal, NR, NA in itertools.product(("church", "polity"), (False, True), POOLS, POOLS):
        hid = list(itertools.product((0.25, 0.5, 1.0), (0.0, 0.5)))
        acc = defaultdict(lambda: defaultdict(float))
        for p_claim, p_cons in hid:
            Pp = base_params(NR, "r37_3", "accusatorial", SA=NA, DJ=5 + 1.5 * 0.74, section="C2b.polity")
            Pc = base_params(NR, "r37_3", "inquisitorial", SA=NA, DJ=BENCH + 0.5, DJ_proof=BENCH + 0.5, names_cost=1.0, section="C2b.church")
            _, sp, _ = best_plea(Pp, PLEAS_ACC)
            _, sc, _ = best_plea(Pc, PLEAS_INQ, bite=0.5)
            here, there = (sc, sp) if sit == "church" else (sp, sc)
            if sit == "polity":
                ptr = p_claim * p_cons            # a church claim on a polity case never takes precedence (R-34)
            else:
                ptr = p_claim * (1.0 if royal else p_cons)
            g_here = goods_of(here)
            g_there = goods_of(there)
            keys = set(g_here) | set(g_there)
            g_here = {k: g_here.get(k, 0.0) for k in keys}
            g_ch = {k: ptr * g_there.get(k, 0.0) + (1 - ptr) * g_here[k] for k in keys}
            g_ch["time"] -= 1.0
            g_ch["stand"] -= (1 - ptr) * 0.25
            for k, v in g_here.items():
                acc["answer"][k] += v / len(hid)
            for k, v in g_ch.items():
                acc["challenge"][k] += v / len(hid)
        opts = {k: dict(v) for k, v in acc.items()}
        T.add(NR, opts, HEADLINE_W)
        log.w("result", section="C2b.challenge", sitting=sit, royal=royal, NR=NR, NA=NA,
              goods={k: {kk: round(vv, 4) for kk, vv in v.items()} for k, v in opts.items()}, headline_best=best_under(opts, HEADLINE_W))
    log.w("summary", section="C2b.challenge", verdict=T.verdict())
    return T


def proof_E(ws, elab):
    if not ws:
        return 0.0
    if elab == "high":                      # averaging with a mild count bonus: a weak proof added to a strong one dilutes
        return (sum(ws) / len(ws)) * (1 + 0.25 * (len(ws) - 1))
    return sum(ws)


def sec_proofs(log):
    """C4: which proofs to offer and when. Deny plea; the respondent's offered proofs are an instance modifier on the accuser's proof roll."""
    log.w("claim", section="C4.proofs", text="Offer-strong, offer-both, hold-until-needed and hoard are each best somewhere; the right answer flips with the room's elaboration and with the pool", where="P4 choice 4")
    log.w("plan", section="C4.proofs", proofs="strong 1.5D (firsthand, full grade), weak 0.5D (told, remove 0.5)", elaboration={"high": "mean x (1 + .25(n-1))", "low": "sum"},
          options=["hoard", "strong_now", "both_now", "weak_now", "strong_when_needed"], hidden="r (the accuser holds a rebuttal: halves an offered proof) {0, .5}",
          keep="each proof kept unspent is worth h (a later matter, leverage outside the room), weighted by the grid's keep weight")
    opts_def = {"hoard": [], "strong_now": [1.5], "both_now": [1.5, 0.5]}     # weak_now CUT (run 2: never best at 2D or 5D)
    T = Tally("C4.proofs", list(opts_def))     # strong_when_needed CUT in run 4: a knife-edge (run 3, break-even 0.16-0.17 at 5D)
    for elab, N, NA, C in itertools.product(("high", "low"), POOLS, POOLS, ("r37_3", "none")):
        acc = defaultdict(lambda: defaultdict(float))
        for r in (0.0, 0.5):
            for name, ws in opts_def.items():
                E = proof_E(ws, elab) * (1 - 0.5 * r)
                P = base_params(N, C, "accusatorial", SA=NA, DJ=BENCH, proof_mod=E, judg_mod=E, section="C4")
                s = summarise(hearing("deny", P), "deny", P)
                g = goods_of(s)
                g["keep"] = 2 - len(ws)
                for k, v in g.items():
                    acc[name][k] += v / 2
            # hold until needed: first sitting with nothing; offer the strong proof from the second sitting
            P0 = base_params(N, C, "accusatorial", SA=NA, DJ=BENCH, section="C4")
            E = proof_E([1.5], elab) * (1 - 0.5 * r)
            P1 = dict(P0, proof_mod=E, judg_mod=E)
            b0 = bands(NA, ob_of(N, P0["C"]), 0.0, "C4")
            # sitting 1 succeeds or half-proves without the proof -> as deny with no proof from there; else the rest with the proof (2 more sittings)
            first =[(b0["O"], "O"), (b0["S"], "S"), (b0["P"], "P")]
            out = []
            for p, o in first:
                if o in ("O", "S"):
                    out += [(p * q, g, s, h) for q, g, s, h in judgment(P0, 0, 1, stage, SEV)]
                else:
                    out += [(p * P0["d_half"] * q, g, s, h) for q, g, s, h in judgment(P0, 1, 1, stage, SEV)]
                    out.append((p * (1 - P0["d_half"]), None, 1, "dismissed_half_proof"))
            for p, o, k in stage(NA, ob_of(N, P1["C"], E), 0.0, tries=2, section="C4"):
                pf = b0["F"] * p
                if o == "closed":
                    out.append((pf, None, k + 1, "acquitted_kept" ))
                elif o in ("O", "S"):
                    out += [(pf * q, g, s, h) for q, g, s, h in judgment(P1, 0, k + 1, stage, SEV)]
                else:
                    out += [(pf * P1["d_half"] * q, g, s, h) for q, g, s, h in judgment(P1, 1, k + 1, stage, SEV)]
                    out.append((pf * (1 - P1["d_half"]), None, k + 1, "dismissed_half_proof"))
            s = summarise(out, "deny", P0)
            g = goods_of(s)
            g["keep"] = 2.0 - b0["F"]   # the weak proof always kept; the strong one spent only if sitting 1 failed
            for k, v in g.items():
                acc["strong_when_needed"][k] += v / 2
        held = dict(acc.pop("strong_when_needed"))    # computed for the record, not an option (cut, run 4)
        opts = {k: dict(v) for k, v in acc.items()}
        par = T.add(N, opts, HEADLINE_W)
        be = {}
        for o in ("hoard", "strong_when_needed"):
            if o == "strong_when_needed":
                opts_be = dict(opts, strong_when_needed=held)
            else:
                opts_be = opts
            be[o] = None
            for wk in [x / 100 for x in range(0, 101)]:
                if o in best_under(opts_be, dict(HEADLINE_W, keep=wk)):
                    be[o] = wk
                    break
        log.w("result", section="C4.proofs.break_even", elaboration=elab, NR=N, NA=NA, ceiling=C, keep_weight_at_which_best=be,
              note="the least worth of one kept proof (in sentences) at which the option is the headline best; None = not best up to 1.0")
        log.w("result", section="C4.proofs", elaboration=elab, NR=N, NA=NA, ceiling=C,
              goods={k: {kk: round(vv, 4) for kk, vv in v.items()} for k, v in opts.items()},
              weakly_dominated={k: v[0] for k, v in par.items() if v[0]}, headline_best=best_under(opts, HEADLINE_W))
    log.w("summary", section="C4.proofs", verdict=T.verdict())
    return T


def sec_advocate(log):
    """C5: speak yourself or send an advocate (accusatorial rite only: the inquisitio admits no counsel)."""
    log.w("plan", section="C5.advocate", visible="respondent pool x accuser pool x advocate offset {-2,0,+2,+4}",
          rules="advocate pool x (0.6 brought + 0.4 conduct x latitude 0.7); an advocate may only deny (a principal alone concedes); the principal keeps one scene (keep +1); the advocate absorbs the disproved-denial standing (0.5) but not the principal's lie; fee: one oblige (rel -0.05)")
    T = Tally("C5.advocate", ["self", "advocate"])
    for N, NA, off in itertools.product(POOLS, POOLS, (-2, 0, 2, 4)):
        acc = defaultdict(lambda: defaultdict(float))
        hid = (0.3, 0.6, 0.9)
        for d_half in hid:
            P = base_params(N, "r37_3", "accusatorial", SA=NA, DJ=BENCH, d_half=d_half, section="C5")
            pl, s, _ = best_plea(P, PLEAS_ACC)
            g = goods_of(s)
            g["keep"] = 0.0
            g["rel"] = 0.0
            for k, v in g.items():
                acc["self"][k] += v / len(hid)
            DV = max(1.0, (N + off) * (0.6 + 0.4 * 0.7))
            Pv = dict(P, SR_score=DV)                # the advocate's dice are the defence's score (a worse advocate hurts)
            sv = summarise(hearing("deny", Pv), "deny", Pv)
            sentenced = 1 - sv["P_clear"]
            sv["E_standing_loss"] -= 0.5 * sentenced  # the disproved denial falls on the advocate
            g = goods_of(sv)
            g["keep"] = 1.0
            g["rel"] = -0.5                          # the fee: an `oblige` owed to the advocate
            for k, v in g.items():
                acc["advocate"][k] += v / len(hid)
        opts = {k: dict(v) for k, v in acc.items()}
        T.add(N, opts, HEADLINE_W)
        log.w("result", section="C5.advocate", NR=N, NA=NA, offset=off,
              goods={k: {kk: round(vv, 4) for kk, vv in v.items()} for k, v in opts.items()}, headline_best=best_under(opts, HEADLINE_W))
    log.w("summary", section="C5.advocate", verdict=T.verdict())
    return T


SPEECH = {
    # kind: (aptness price, sigma if hidden state good, sigma if bad, standing on Failure, gain on Success)
    "plain": (0.5, 0.0, 0.0, 0.0, 0.0),
    "cite_licence": (0.0, 0.5, 0.5, 0.0, 0.0),            # needs a held writ; implicates its issuer (rel 1)
    "hand_back": (1.0, 1.0, -0.5, 0.5, 0.5),              # Aristotle's last method: on the room's regard (hidden g); turns the room on the accuser
    "impugn_motive": (0.5, 0.75, 0.75, 0.5, 0.0),         # signals one cannot answer (standing 0.5 level on failure); makes an enemy (rel 1)
}


def sec_speech(log):
    """C6: the speech kind at the respondent's own stage (the justification, his affirmative defence)."""
    log.w("plan", section="C6.speech", kinds=SPEECH, visible="rite x respondent pool x accuser pool x holds a writ {no,yes}",
          hidden="g (the bench regards him: hand_back lands) {.2,.5,.8} uniform", note="no writ: cite_licence is priced +1.0 more (R-16: priced, never refused)")
    T = Tally("C6.speech", list(SPEECH))
    for rite, N, NA, writ in itertools.product(("accusatorial", "inquisitorial"), POOLS, POOLS, (False, True)):
        acc = defaultdict(lambda: defaultdict(float))
        for gstate in (0.2, 0.5, 0.8):
            for kind, (apt, s_good, s_bad, st_f, gain) in SPEECH.items():
                a = apt + (1.0 if (kind == "cite_licence" and not writ) else 0.0)
                s_good_k = s_good
                if kind == "impugn_motive" and rite == "inquisitorial":
                    s_good_k = s_bad = 0.25                     # the accuser's name is secret: a guess
                tot = defaultdict(float)
                for st, pw in ((s_good_k, gstate), (s_bad, 1 - gstate)):
                    P = base_params(N, "r37_3", rite, SA=NA, DJ=BENCH, DJ_proof=BENCH, apt_just=0.25 + a, s_q=st, names_cost=1.0, section="C6")
                    br = hearing("justify", P)
                    s = summarise(br, "justify", P)
                    p_fail_q = sum(p for p, g, ss, h in br if h != "excused")
                    g = goods_of(s)
                    g["stand"] -= st_f * p_fail_q
                    g["stand"] += gain * (1 - p_fail_q)
                    g["rel"] = -(1.0 if kind in ("cite_licence", "impugn_motive") else 0.0)
                    for k, v in g.items():
                        tot[k] += pw * v
                for k, v in tot.items():
                    acc[kind][k] += v / 3
        opts = {k: dict(v) for k, v in acc.items()}
        par = T.add(N, opts, HEADLINE_W)
        log.w("result", section="C6.speech", rite=rite, NR=N, NA=NA, writ=writ,
              goods={k: {kk: round(vv, 4) for kk, vv in v.items()} for k, v in opts.items()},
              weakly_dominated={k: v[0] for k, v in par.items() if v[0]}, headline_best=best_under(opts, HEADLINE_W))
    log.w("summary", section="C6.speech", verdict=T.verdict())
    return T


def sec_procedural(log):
    """C7: challenge a bench member; burn the file; forge the file. (Seizing it is an authority's move.)"""
    log.w("skipped", section="C7.seize", what="seize the case file", reason="`seize` needs a held warrant naming the Record and a seat granted seize (`state/gate.py::may_seize`): an authority's act, not a party's; it is scenario 2's move, traced there, not a party option")
    # (a) challenge a bench member
    T = Tally("C7.challenge", ["accept_bench", "challenge"])
    log.w("plan", section="C7.challenge", rule="the judge's own regard for the respondent enters HIS determine as sigma (his own ledger, F8-clean): hostile +0.5; the challenge is the respondent's act, apt (price 0) if he holds a witnessed grievance against the judge, else priced +1 (R-16), vs Ob = the judge's score/2 (5D, ceiling 3); upheld: a neutral judge, +1 season w.p. .5; refused: hostile for sure at +0.75, standing -0.25 level",
              visible="respondent pool x accuser pool x holds a grievance {no, yes}", hidden="h (the judge is hostile) {.1,.3,.6}: the respondent's belief, from his own ledger, so each h is a cell")
    for N, NA, h, griev in itertools.product(POOLS, POOLS, (0.1, 0.3, 0.6), (False, True)):
        acc = {}
        P = base_params(N, "r37_3", "accusatorial", SA=NA, DJ=BENCH, section="C7a")
        for opt in ("accept_bench", "challenge"):
            tot = defaultdict(float)
            if opt == "accept_bench":
                for sj, pw in ((0.5, h), (0.0, 1 - h)):
                    _, s, _ = best_plea(dict(P, s_judg=sj), PLEAS_ACC)
                    for k, v in goods_of(s).items():
                        tot[k] += pw * v
            else:
                b = bands(N, ob_of(BENCH, P["C"], 0.0, 0.0 if griev else 1.0), 0.0, "C7a")
                up = b["O"] + b["S"] + b["P"]
                _, s_up, _ = best_plea(dict(P, s_judg=0.0), PLEAS_ACC)
                _, s_dn, _ = best_plea(dict(P, s_judg=0.75), PLEAS_ACC)
                gu, gd = goods_of(s_up), goods_of(s_dn)
                for k in set(gu) | set(gd):
                    tot[k] += up * gu.get(k, 0.0) + (1 - up) * gd.get(k, 0.0)
                tot["time"] -= up * 0.5
                tot["stand"] -= (1 - up) * 0.25
            acc[opt] = dict(tot)
        T.add(N, acc, HEADLINE_W)
        log.w("result", section="C7.challenge", NR=N, NA=NA, h=h, grievance=griev,
              goods={k: {kk: round(vv, 4) for kk, vv in v.items()} for k, v in acc.items()}, headline_best=best_under(acc, HEADLINE_W))
    log.w("summary", section="C7.challenge", verdict=T.verdict())
    # (a2) the inquisitorial mortal-enemy rule: name enemies without knowing who accused (02 1.1 row 8; the Spanish tachas)
    Tm = Tally("C7.mortal_enemies", ["name_none", "name_one", "name_three"])
    log.w("plan", section="C7.mortal_enemies", rule="the accuser's name is secret; the respondent names k persons of mortal hatred; if the accuser is among them the charge fails (02 1.1 row 8); each person named learns it (rel 1 each); a bench reads a long list as a smear: k = 3 raises the Ob of his later acts by 0.25 (aptness)",
              hidden="p1 = P(his single best guess is the accuser) {.1,.3,.5}; three names cover min(1, 2.2 x p1)", visible="respondent pool x bench pool 5")
    for N, p1 in itertools.product(POOLS, (0.1, 0.3, 0.5)):
        P = base_params(N, "r37_3", "inquisitorial", SA=BENCH, DJ=BENCH, DJ_proof=BENCH, names_cost=1.0, section="C7a2")
        _, s0, _ = best_plea(P, PLEAS_INQ)
        g0 = goods_of(s0)
        _, s3, _ = best_plea(dict(P, apt_def=P["apt_def"] + 0.25, apt_just=P["apt_just"] + 0.25), PLEAS_INQ)
        g3 = goods_of(s3)
        acc = {"name_none": dict(g0, rel=0.0)}
        for name, k, cover, gg in (("name_one", 1, p1, g0), ("name_three", 3, min(1.0, 2.2 * p1), g3)):
            keys = set(gg) | {"rel"}
            d = {kk: (1 - cover) * gg.get(kk, 0.0) for kk in keys}
            d["rel"] = -float(k)
            acc[name] = d
        Tm.add(N, acc, HEADLINE_W)
        log.w("result", section="C7.mortal_enemies", NR=N, p1=p1, goods={k: {kk: round(vv, 4) for kk, vv in v.items()} for k, v in acc.items()},
              headline_best=best_under(acc, HEADLINE_W))
    log.w("summary", section="C7.mortal_enemies", verdict=Tm.verdict())
    # (b) burn
    T2 = Tally("C7.burn", ["keep_file", "burn"])
    log.w("plan", section="C7.burn", rule="decided after the fact is proved (deny plea, proof Success): burning restarts the case at plea next season (repair c: determine needs the held file); detected w.p. p_det -> obstruction matter, P(convicted) .6 at severity .75, standing -1.0",
          visible="pools x p_det {.1,.3,.6}", precondition="the burner must hold the file (`destroy_record` requires `held_by`): an accomplice holder's own choice, not modelled")
    for N, NA, pdet in itertools.product(POOLS, POOLS, (0.1, 0.3, 0.6)):
        P = base_params(N, "r37_3", "accusatorial", SA=NA, DJ=BENCH, section="C7b")
        # keep: the fact is proved; judgment remains
        sk = summarise(judgment(P, 0, 1, stage, SEV), "deny", P)
        # burn: re-plead from scratch next season
        pl, sb, _ = best_plea(P, PLEAS_ACC)
        gb = goods_of(sb)
        gb["time"] -= 1.0
        gb["sev"] -= pdet * 0.6 * 0.75
        gb["stand"] -= pdet * 1.0
        acc = {"keep_file": goods_of(sk), "burn": gb}
        T2.add(N, acc, HEADLINE_W)
        log.w("result", section="C7.burn", NR=N, NA=NA, p_det=pdet, goods={k: {kk: round(vv, 4) for kk, vv in v.items()} for k, v in acc.items()},
              headline_best=best_under(acc, HEADLINE_W))
    log.w("summary", section="C7.burn", verdict=T2.verdict())
    # (c) forge
    T3 = Tally("C7.forge", ["leave_file", "forge"])
    log.w("plan", section="C7.forge", rule="forge (repair c: forge accepts the case-file kind) the agenda to show the proof stage failed twice, so one more Failure acquits; examined at judgment by the bench: examiner pool vs Ob = forgery quality; found: +1 grade and an obstruction matter (.6 x .75), standing -1.0",
              visible="pools x forgery quality {1,2,3}")
    for N, NA, fq in itertools.product(POOLS, POOLS, (1.0, 2.0, 3.0)):
        P = base_params(N, "r37_3", "accusatorial", SA=NA, DJ=BENCH, section="C7c")
        sl = summarise(hearing("deny", P), "deny", P)
        bx = bands(BENCH, fq, 0.0, "C7c")      # the bench examines the file at judgment
        found = 1 - bx["F"]
        br = []
        for p, o, k in stage(NA, ob_of(N, P["C"]), 0.0, tries=1, section="C7c"):
            if o == "closed":
                br.append((p, None, k, "acquitted"))
            elif o in ("O", "S"):
                br += [(p * q, g, s, h) for q, g, s, h in judgment(P, 0, k, stage, SEV)]
            else:
                br += [(p * P["d_half"] * q, g, s, h) for q, g, s, h in judgment(P, 1, k, stage, SEV)]
                br.append((p * (1 - P["d_half"]), None, k, "dismissed_half_proof"))
        sf = summarise(br, "deny", P)
        # found out: the forgery voids itself (the full three tries resume) and aggravates
        gf_ok = goods_of(sf)
        gf_bad = goods_of(sl)
        gf_bad["sev"] -= 0.6 * 0.75 + 0.1
        gf_bad["stand"] -= 1.0
        gf = {k: (1 - found) * gf_ok[k] + found * gf_bad[k] for k in gf_ok}
        acc = {"leave_file": goods_of(sl), "forge": gf}
        T3.add(N, acc, HEADLINE_W)
        log.w("result", section="C7.forge", NR=N, NA=NA, forgery_quality=fq, p_found=round(found, 4),
              goods={k: {kk: round(vv, 4) for kk, vv in v.items()} for k, v in acc.items()}, headline_best=best_under(acc, HEADLINE_W))
    log.w("summary", section="C7.forge", verdict=T3.verdict())
    return T, Tm, T2, T3


def sec_appeal(log):
    """C8: whether to appeal, and to which authority (R-35): never back to the same bench."""
    log.w("plan", section="C8.appeal", lower="a church bench's sentence (ban or custody) of grade g", options=["accept", "appeal_polity", "appeal_holy_see"],
          rule="review on the record (hoarded proofs cannot enter): the APPELLANT bears the burden of showing error, rolling his pool vs Ob = the lower seat's score/2 (5D, ceiling 3) + 0.5 if the lower finding rested on a full proof; the appellate seat then acts by its OWN choice (hidden disposition d_app {.4,.7,1}: on a shown error it voids w.p. d_app, else commutes one grade; on a Partial it commutes w.p. d_app); Failure x3 stands; costs: one season for the carriage plus sittings; the church's displeasure (rel) .10 for going to the crown, .03 to the Holy See; the polity, if it does not void, still refuses its arm to a church custody w.p. .5",
          visible="grade x kind {ban, detain} x appellant pool x church L {.37,.78} x full proof {yes,no}")
    T = Tally("C8.appeal", ["accept", "appeal_polity", "appeal_holy_see"])
    for g0, kind, N, Lc, full in itertools.product((3, 2, 1), ("ban", "detain"), POOLS, (0.37, 0.78), (True, False)):
        bite = Lc if kind == "ban" else 1.0
        sev0 = SEV[g0] * bite
        acc = {"accept": {"sev": -sev0, "risk": -(1.0 if g0 >= 2 else 0.0), "stand": 0.0, "time": 0.0, "rel": 0.0}}
        # the polity: nearer and readier to void, but its void cannot lift a church ban's social bite (residual .5 x L)
        # the Holy See: the higher seat of the same authority, far (one more season) and slower to undo its own bench
        for opt, rel, dset, far, resid in (("appeal_polity", 1.0, (0.4, 0.7, 1.0), 0.0, 0.5),
                                           ("appeal_holy_see", 0.3, (0.2, 0.5, 0.8), 1.0, 0.0)):
            tot = defaultdict(float)
            for d_app in dset:
                pw = 1 / len(dset)
                st = stage(N, ob_of(5, CEILINGS["r37_3"], 0.0, 0.5 if full else 0.0), 0.0, section="C8")
                E = 0.0
                Pr = 0.0
                Es = 0.0
                branches = []
                for p, o, k in st:
                    if o in ("O", "S"):
                        branches += [(p * d_app, None, k), (p * (1 - d_app), max(0, g0 - 1), k)]
                    elif o == "P":
                        branches += [(p * d_app, max(0, g0 - 1), k), (p * (1 - d_app), g0, k)]
                    else:
                        branches.append((p, g0, k))
                for p, gg, k in branches:
                    b = bite
                    if opt == "appeal_polity" and kind == "detain" and gg is not None:
                        b = 0.5
                    if gg is None and kind == "ban" and resid:
                        E += p * SEV[g0] * Lc * resid     # voided in the crown's law, still heeded by the faithful
                        Pr += p * (1.0 if g0 >= 2 else 0.0) * resid * Lc
                    E += p * (SEV[gg] * b if gg is not None else 0.0)
                    Pr += p * (1.0 if (gg is not None and gg >= 2) else 0.0)
                    Es += p * (k + far)
                tot["sev"] += -pw * E
                tot["risk"] += -pw * Pr
                tot["time"] += -pw * Es
            tot["stand"] = 0.0
            tot["rel"] = -rel
            acc[opt] = dict(tot)
        T.add(N, acc, HEADLINE_W)
        log.w("result", section="C8.appeal", grade=g0, sentence_kind=kind, N=N, L_church=Lc, full_proof=full,
              goods={k: {kk: round(vv, 4) for kk, vv in v.items()} for k, v in acc.items()}, headline_best=best_under(acc, HEADLINE_W))
    log.w("summary", section="C8.appeal", verdict=T.verdict(), note="pool = the appellant's pool (he argues the error on the record)")
    return T


def sec_warrant(log):
    """C9: a warrant-holder's duty (repair i): serve or decline."""
    log.w("plan", section="C9.warrant", options=["serve", "decline"],
          rule="serve: arrest draw server pool vs prisoner's score/2 (ceiling 3); a scene spent (keep -1); success: +0.1 regard with the issuer x his own opinion o of it, -0.05 rel (the prisoner's kin); failure: arrest.resisted, -0.05 standing. decline: the warrant matures unserved -> `warrant.lapsed` witnessed: -0.1 x o with the issuer; if the issuer can revoke his seat (same authority) w.p. .3 a seat worth 1.0 is lost; if not (a polity holder of a church warrant), the church can only ban him: bite L x .35",
          visible="server pool x prisoner pool x o {-1,0,1} x same authority {yes,no} x L {.37,.78}")
    T = Tally("C9.warrant", ["serve", "decline"])
    for Ns, Np, o, same, L in itertools.product(POOLS, POOLS, (-1, 0, 1), (True, False), (0.37, 0.78)):
        b = bands(Ns, ob_of(Np, 3.0), 0.0, "C9")
        ps = 1 - b["F"]
        serve = {"gain": ps * 0.1 * o, "rel": -ps * 1.0, "stand": -(1 - ps) * 0.5, "keep": -1.0, "sev": 0.0}
        dec = {"gain": -0.1 * o, "rel": 0.0, "stand": 0.0, "keep": 0.0,
               "sev": -(0.3 * 1.0 if same else L * 0.35)}
        acc = {"serve": serve, "decline": dec}
        T.add(Ns, acc, HEADLINE_W)
        log.w("result", section="C9.warrant", server=Ns, prisoner=Np, opinion=o, same_authority=same, L=L,
              p_arrest=round(ps, 4), goods=acc, headline_best=best_under(acc, HEADLINE_W))
    log.w("summary", section="C9.warrant", verdict=T.verdict())
    return T


# ================================================================== the capability layer (addendum)
# attribute(s) -> FACULTY (one owner: FACULTY_MAP, data) -> dice (dice_of_faculty) weighted by what the
# rite/stage asks (ROLE_WEIGHTS, row data); title, office x L, faction and evidence add as the row says.
# The attribute ROSTER is behind FACULTY_MAP and is replaceable: three sets below, one code path.
FACULTIES = ("eloquence", "reasoning", "reading", "composure")      # eloquence is the CONDUCT faculty (x latitude, R-18/R-41)
FACULTY_MAP = {
    "registry_nine": {   # references/descriptor_registry.yaml:33-45 (scale 1-7)
        "eloquence": {"CHA": 0.7, "BON": 0.3}, "reasoning": {"ACU": 0.6, "FOC": 0.4},
        "reading": {"ATT": 1.0}, "composure": {"WIL": 0.7, "FOC": 0.3}},
    "scratch_fourteen": {  # proposals/2026-10-16-attributes-from-scratch_part4.md:34-35
        "eloquence": {"Presence": 0.7, "Warmth": 0.3}, "reasoning": {"Reasoning": 0.6, "Forethought": 0.4},
        "reading": {"Reading people": 0.7, "Watchfulness": 0.3}, "composure": {"Composure": 0.5, "Nerve": 0.3, "Constancy": 0.2}},
    "scratch_eight": {     # the same file :193-195, the smaller alternative
        "eloquence": {"Bearing": 1.0}, "reasoning": {"Mind": 1.0}, "reading": {"Perception": 1.0},
        "composure": {"Poise": 0.6, "Heart": 0.4}},
}
CHARACTERS = {   # the same three persons written on each roster (an author's sheet, not derived)
    "commoner": {"registry_nine": dict(STR=3, END=3, AGI=2, FOC=2, ACU=2, WIL=2, ATT=2, CHA=2, BON=2),
                 "scratch_fourteen": {"Presence": 2, "Warmth": 2, "Reasoning": 2, "Forethought": 2, "Reading people": 2, "Watchfulness": 2, "Composure": 2, "Nerve": 2, "Constancy": 2},
                 "scratch_eight": {"Bearing": 2, "Mind": 2, "Perception": 2, "Poise": 2, "Heart": 2}},
    "advocate": {"registry_nine": dict(STR=2, END=3, AGI=3, FOC=4, ACU=5, WIL=4, ATT=4, CHA=7, BON=5),
                 "scratch_fourteen": {"Presence": 7, "Warmth": 5, "Reasoning": 5, "Forethought": 4, "Reading people": 4, "Watchfulness": 4, "Composure": 4, "Nerve": 4, "Constancy": 4},
                 "scratch_eight": {"Bearing": 6, "Mind": 5, "Perception": 4, "Poise": 4, "Heart": 4}},
    "scholar": {"registry_nine": dict(STR=2, END=2, AGI=2, FOC=6, ACU=7, WIL=5, ATT=6, CHA=2, BON=2),
                "scratch_fourteen": {"Presence": 2, "Warmth": 2, "Reasoning": 7, "Forethought": 6, "Reading people": 6, "Watchfulness": 6, "Composure": 5, "Nerve": 5, "Constancy": 6},
                "scratch_eight": {"Bearing": 2, "Mind": 7, "Perception": 6, "Poise": 5, "Heart": 5}},
    "average": {"registry_nine": dict(STR=4, END=4, AGI=4, FOC=4, ACU=4, WIL=4, ATT=4, CHA=4, BON=4),
                "scratch_fourteen": {k: 4 for k in ("Presence", "Warmth", "Reasoning", "Forethought", "Reading people", "Watchfulness", "Composure", "Nerve", "Constancy")},
                "scratch_eight": {k: 4 for k in ("Bearing", "Mind", "Perception", "Poise", "Heart")}},
}
ROLE_WEIGHTS = {   # row data: which faculties a rite's stage weighs, per role [ASSUMPTION; sweep]
    "accusatorial": {"prove": {"eloquence": .4, "reasoning": .4, "composure": .2}, "resist": {"eloquence": .4, "reasoning": .3, "composure": .3},
                     "justify": {"reasoning": .5, "eloquence": .3, "composure": .2}, "bench": {"reasoning": .6, "reading": .4}},
    "inquisitorial": {"prove": {"reading": .6, "reasoning": .4}, "resist": {"composure": .7, "reasoning": .3},
                      "justify": {"reasoning": .7, "composure": .3}, "bench": {"reasoning": .6, "reading": .4}},
}
SPEECH_FACULTY = {   # a speech kind chooses which faculty carries the roll (row data) [ASSUMPTION; sweep]
    "plain": {"reasoning": .8, "composure": .2}, "cite_licence": {"reasoning": .8, "composure": .2},
    "hand_back": {"eloquence": .8, "composure": .2}, "impugn_motive": {"eloquence": .5, "reasoning": .5}}
DICE_PER_FACULTY = 1.25    # [ASSUMPTION; medium; revert: the kernel's max(5, 2f+3)] faculty 4 (average) -> 5D, R-40's reference


def faculty(sheet, roster, f, default=1.0):
    """THE ONE OWNER of attribute -> faculty. A missing attribute reads the registry default (1)."""
    return sum(w * sheet.get(a, default) for a, w in FACULTY_MAP[roster][f].items())


def dice_for(sheet, roster, rite, role, latitude=1.0):
    w = ROLE_WEIGHTS[rite][role]
    return DICE_PER_FACULTY * sum(wt * faculty(sheet, roster, f) * (latitude if f == "eloquence" else 1.0) for f, wt in w.items())


def char_pools(name, roster, rite, latitude=1.0):
    sh = CHARACTERS[name][roster]
    return {r: round(dice_for(sh, roster, rite, r, latitude), 4) for r in ("prove", "resist", "justify", "bench")}


def sec_characters(log):
    """C10 (addendum): the same choices, with pools BUILT FROM ATTRIBUTES; does a choice dominated for one
    character come alive for another?"""
    log.w("claim", section="C10.characters", text="With pools built from attributes through faculties, the same choice is a lookup for one character and live for another; which option is best follows the character's faculties and the rite's weights")
    log.w("plan", section="C10.characters", faculty_map=FACULTY_MAP, role_weights=ROLE_WEIGHTS, dice_per_faculty=DICE_PER_FACULTY,
          characters=CHARACTERS, opponents="accuser: the 'average' sheet in the role 'prove'; bench: 5D (the 'average' bench role) unless stated; inquisitor: average or scholar",
          note="the pools vary by rite as well as by person: that is the faculty layer's whole effect")
    for roster in FACULTY_MAP:
        for nm in CHARACTERS:
            log.w("result", section="C10.faculties", roster=roster, character=nm,
                  faculties={f: round(faculty(CHARACTERS[nm][roster], roster, f), 3) for f in FACULTIES},
                  pools={rite: char_pools(nm, roster, rite) for rite in ROLE_WEIGHTS})
    roster = "registry_nine"
    acc_pool = {rite: char_pools("average", roster, rite)["prove"] for rite in ROLE_WEIGHTS}
    chars = ("commoner", "advocate", "scholar")
    T = {k: Tally(f"C10.{k}", o) for k, o in (("plea_acc", PLEAS_ACC), ("plea_inq", PLEAS_INQ), ("plea_inq_scholar_bench", PLEAS_INQ),
                                                ("defy", ["appear", "evade", "defy"]), ("challenge", ["answer", "challenge"]),
                                                ("advocate", ["self", "advocate"]), ("speech", list(SPEECH)), ("forum", ["polity", "church"]))}
    for nm in chars:
        for rite in ROLE_WEIGHTS:
            cp = char_pools(nm, roster, rite)
            bench_proof = char_pools("scholar" if False else "average", roster, rite)["prove"] if rite == "inquisitorial" else BENCH
            for tag, inq in (((f"plea_acc" if rite == "accusatorial" else "plea_inq"), char_pools("average", roster, "inquisitorial")["prove"]),
                             (("plea_inq_scholar_bench" if rite == "inquisitorial" else None), char_pools("scholar", roster, "inquisitorial")["prove"])):
                if tag is None:
                    continue
                pleas = PLEAS_ACC if rite == "accusatorial" else PLEAS_INQ
                for writ, prf in itertools.product((False, True), (0.0, 1.5)):
                    acc = defaultdict(lambda: defaultdict(float))
                    for d_half in (0.3, 0.6, 0.9):
                        P = base_params(5, "r37_3", rite, SA=acc_pool[rite], SR_score=cp["resist"], SR_roll=cp["justify"], DJ=BENCH, DJ_proof=inq,
                                        proof_mod=prf, writ_mod=(1.5 if writ else 0.0), d_half=d_half, names_cost=1.0, section=f"C10.{tag}")
                        for pl in pleas:
                            for kk, v in goods_of(summarise(hearing(pl, P), pl, P)).items():
                                acc[pl][kk] += v / 3
                    opts = {k: dict(v) for k, v in acc.items()}
                    par = T[tag].add(nm, opts, HEADLINE_W)
                    log.w("result", section=f"C10.{tag}", character=nm, pools=cp, inquisitor_pool=inq if rite == "inquisitorial" else None, writ=writ, defence_proof=prf,
                          goods={k: {kk: round(vv, 4) for kk, vv in v.items()} for k, v in opts.items()},
                          weakly_dominated={k: v[0] for k, v in par.items() if v[0]}, headline_best=best_under(opts, HEADLINE_W))
        # appear / evade / defy, both rites
        for rite in ROLE_WEIGHTS:
            cp = char_pools(nm, roster, rite)
            pleas = PLEAS_ACC if rite == "accusatorial" else PLEAS_INQ
            for q, L, ks in itertools.product((0.0, 0.5, 1.0), (0.37, 0.5, 0.78), (0.0, 0.1, 0.25)):
                P = base_params(5, "r37_3", rite, SA=acc_pool[rite], SR_score=cp["resist"], SR_roll=cp["justify"], DJ=BENCH + L,
                                DJ_proof=char_pools("average", roster, "inquisitorial")["prove"] + L, names_cost=1.0, section="C10.defy")
                kind = "detain" if rite == "accusatorial" else "ban"
                bite_p = 1.0 if kind == "detain" else L
                _, s_app, _ = best_plea(P, pleas, bite=bite_p)
                Pa = dict(P, SR_score=4.0)
                p_arr = 1 - bands(5, ob_of(cp["resist"], P["C"]), 0.0, "C10.arrest")["F"]
                s_abs = summarise(hearing("deny", Pa), "deny", Pa, bite=(q * p_arr) if kind == "detain" else L)
                cb = bands(P["DJ"], ob_of(4.0, P["C"]), 0.0, "C10.contempt")
                csev = (cb["O"] * SEV[3] + cb["S"] * SEV[2] + cb["P"] * SEV[1]) * L * (0.0 if kind == "ban" else 1.0)
                g = {"appear": dict(goods_of(s_app), partisan=0.0, stand_signed=0.0, keep=-1.0),
                     "evade": dict(goods_of(s_abs), partisan=0.0, stand_signed=0.0, keep=0.0)}
                gd = goods_of(dict(s_abs, E_sev=s_abs["E_sev"] + csev))
                gd.update(partisan=0.02 * ((1 - q * p_arr) if kind == "detain" else 0.5), stand_signed=ks * (1 - 2 * L), keep=0.0)
                g["defy"] = gd
                T["defy"].add(nm, g, HEADLINE_W)
                log.w("result", section="C10.defy", character=nm, rite=rite, q=q, L=L, k_s=ks, headline_best=best_under(g, HEADLINE_W))
        # forum challenge, from each rite to the other
        for sit, royal in itertools.product(("church", "polity"), (False, True)):
            acc = defaultdict(lambda: defaultdict(float))
            for p_claim, p_cons in itertools.product((0.25, 0.5, 1.0), (0.0, 0.5)):
                cpa, cpi = char_pools(nm, roster, "accusatorial"), char_pools(nm, roster, "inquisitorial")
                Pp = base_params(5, "r37_3", "accusatorial", SA=acc_pool["accusatorial"], SR_score=cpa["resist"], SR_roll=cpa["justify"], DJ=BENCH + 1.5 * 0.74, section="C10.ch")
                Pc = base_params(5, "r37_3", "inquisitorial", SA=acc_pool["inquisitorial"], SR_score=cpi["resist"], SR_roll=cpi["justify"], DJ=BENCH + 0.5,
                                 DJ_proof=acc_pool["inquisitorial"] + 0.5, names_cost=1.0, section="C10.ch")
                _, sp, _ = best_plea(Pp, PLEAS_ACC)
                _, sc, _ = best_plea(Pc, PLEAS_INQ, bite=0.5)
                here, there = (sc, sp) if sit == "church" else (sp, sc)
                ptr = p_claim * p_cons if sit == "polity" else p_claim * (1.0 if royal else p_cons)
                gh, gt = goods_of(here), goods_of(there)
                keys = set(gh) | set(gt)
                gc = {k: ptr * gt.get(k, 0.0) + (1 - ptr) * gh.get(k, 0.0) for k in keys}
                gc["time"] -= 1.0
                gc["stand"] -= (1 - ptr) * 0.25
                for k in keys:
                    acc["answer"][k] += gh.get(k, 0.0) / 6
                    acc["challenge"][k] += gc[k] / 6
            opts = {k: dict(v) for k, v in acc.items()}
            T["challenge"].add(nm, opts, HEADLINE_W)
            log.w("result", section="C10.challenge", character=nm, sitting=sit, royal=royal, headline_best=best_under(opts, HEADLINE_W),
                  goods={k: {kk: round(vv, 4) for kk, vv in v.items()} for k, v in opts.items()})
        # self or the high-presence advocate (accusatorial only), latitude 0.7 on eloquence
        cp = char_pools(nm, roster, "accusatorial")
        adv = char_pools("advocate", roster, "accusatorial", latitude=0.7)["resist"]
        for d_set in ((0.3,), (0.6,), (0.9,)):
            P = base_params(5, "r37_3", "accusatorial", SA=acc_pool["accusatorial"], SR_score=cp["resist"], SR_roll=cp["justify"], DJ=BENCH, d_half=d_set[0], section="C10.adv")
            _, s_self, _ = best_plea(P, PLEAS_ACC)
            gs = dict(goods_of(s_self), keep=0.0, rel=0.0)
            Pv = dict(P, SR_score=adv)
            sv = summarise(hearing("deny", Pv), "deny", Pv)
            sv["E_standing_loss"] -= 0.5 * (1 - sv["P_clear"])
            ga = dict(goods_of(sv), keep=1.0, rel=-0.5)
            opts = {"self": gs, "advocate": ga}
            T["advocate"].add(nm, opts, HEADLINE_W)
            log.w("result", section="C10.advocate", character=nm, own_resist=cp["resist"], advocate_resist=adv, d_half=d_set[0],
                  goods={k: {kk: round(vv, 4) for kk, vv in v.items()} for k, v in opts.items()}, headline_best=best_under(opts, HEADLINE_W))
        # speech kinds at his own justification
        for rite, writ in itertools.product(ROLE_WEIGHTS, (False, True)):
            cp = char_pools(nm, roster, rite)
            acc = defaultdict(lambda: defaultdict(float))
            for gstate in (0.2, 0.5, 0.8):
                for kind, (apt, s_good, s_bad, st_f, gain) in SPEECH.items():
                    a = apt + (1.0 if (kind == "cite_licence" and not writ) else 0.0)
                    sg, sb = (0.25, 0.25) if (kind == "impugn_motive" and rite == "inquisitorial") else (s_good, s_bad)
                    for st, pw in ((sg, gstate), (sb, 1 - gstate)):
                        kw = SPEECH_FACULTY[kind]
                        roll = DICE_PER_FACULTY * sum(wt * faculty(CHARACTERS[nm][roster], roster, f) for f, wt in kw.items())
                        P = base_params(5, "r37_3", rite, SA=acc_pool[rite], SR_score=cp["resist"], SR_roll=roll, DJ=BENCH,
                                        DJ_proof=acc_pool[rite], apt_just=0.25 + a, s_q=st, names_cost=1.0, section="C10.speech")
                        br = hearing("justify", P)
                        s1 = summarise(br, "justify", P)
                        pf = sum(p for p, g_, ss, h in br if h != "excused")
                        g1 = goods_of(s1)
                        g1["stand"] += -st_f * pf + gain * (1 - pf)
                        g1["rel"] = -(1.0 if kind in ("cite_licence", "impugn_motive") else 0.0)
                        for k, v in g1.items():
                            acc[kind][k] += pw * v / 3
            opts = {k: dict(v) for k, v in acc.items()}
            T["speech"].add(nm, opts, HEADLINE_W)
            log.w("result", section="C10.speech", character=nm, rite=rite, writ=writ, pools=cp, headline_best=best_under(opts, HEADLINE_W),
                  goods={k: {kk: round(vv, 4) for kk, vv in v.items()} for k, v in opts.items()})
        # the character as ACCUSER choosing the forum
        for DR, Lc, qc, lam, e in itertools.product((2.5, 5.0), (0.37, 0.78), (0.0, 1.0), (0.0, 0.5), (0.0, 1.0)):
            acc = {}
            ap = char_pools(nm, roster, "accusatorial")["prove"]
            for auth in ("polity", "church"):
                tot = defaultdict(float)
                for d_half in (0.3, 0.6, 0.9):
                    if auth == "polity":
                        P = base_params(DR, "r37_3", "accusatorial", SA=ap, DJ=BENCH + 1.5 * 0.74, d_half=d_half, section="C10.forum")
                        pl, s1, _ = best_plea(P, PLEAS_ACC)
                        br = hearing(pl, P)
                        pf = sum(p for p, g_, ss, h in br if h == "acquitted")
                        tot["gain"] += s1["E_sev"] / 3
                        tot["liab"] += -lam * 0.75 * pf / 3
                        tot["rel"] += -e / 3
                        tot["time"] += -s1["E_seasons"] / 3
                    else:
                        P = base_params(DR, "r37_3", "inquisitorial", SA=ap, DJ=BENCH + Lc, DJ_proof=acc_pool["inquisitorial"] + Lc, d_half=d_half, names_cost=1.0, section="C10.forum")
                        pl, _, _ = best_plea(P, PLEAS_INQ, bite=Lc)
                        s1 = summarise(hearing(pl, P), pl, P)
                        tot["gain"] += s1["E_sev"] * Lc * (0.5 + 0.5 * qc) / 3
                        tot["time"] += -s1["E_seasons"] / 3
                acc[auth] = dict(tot)
            T["forum"].add(nm, acc, HEADLINE_W)
            log.w("result", section="C10.forum", character=nm, accuser_prove_pool=ap, DR=DR, L_church=Lc, q=qc, lam=lam, e=e,
                  headline_best=best_under(acc, HEADLINE_W), goods={k: {kk: round(vv, 4) for kk, vv in v.items()} for k, v in acc.items()})
    for k, t in T.items():
        log.w("summary", section=f"C10.{k}", verdict=t.verdict(), note="key = the character (pools built from its attributes), not a pool size")
    # roster control: the same persons on the other two rosters give these pools
    for alt in ("scratch_fourteen", "scratch_eight"):
        d = {nm: {rite: {r: round(char_pools(nm, alt, rite)[r] - char_pools(nm, "registry_nine", rite)[r], 3) for r in ("prove", "resist", "justify")}
                  for rite in ROLE_WEIGHTS} for nm in CHARACTERS}
        log.w("result", section="C10.roster_control", roster=alt, pool_difference_from_registry_nine=d,
              note="same code path, a different FACULTY_MAP table and sheet; differences are the authored sheets', not the design's")


def hearing_p2(plea, P):
    """CONTROL: P2 as its stress test modelled it -- deny: the accuser proves, a Failure ends the stage;
    concede: the fact stands, straight to judgment, no reward; justify: concede, then the respondent's own
    justification draw; no hold, no cap (the reward that the live ceiling clips away)."""
    st = stage_p2_as_written
    if plea == "deny":
        return hearing("deny", P, stage_fn=st)
    if plea == "concede":
        return judgment(dict(P, judg_mod=0.0), 0, 1, st, SEV)
    out = []
    for p, o, k in st(P["SR_roll"], ob_of(P["SA"], P["C"], 0.0, P["apt_just"]), 0.0, section=P["section"]):
        if o in ("O", "S"):
            out.append((p, None, k, "excused"))
        else:
            out += [(p * q, g, s_, h) for q, g, s_, h in judgment(dict(P, judg_mod=0.0), 0, k, st, SEV)]
    return out


def sec_plea_p2_control(log):
    log.w("fail", section="C3.plea.control_p2_as_written", what="run 4's in-section control (log lines near 4168-4177) is DEGENERATE: after I moved the definitional burden to the accuser, the control's 'concede' with no cap became the deny chain on another question, so deny tied and 'deny alone best' read 0 of 9. Superseded by C3c, which models P2's own plea semantics")
    log.w("plan", section="C3c.control_p2", options=["deny", "concede", "justify"], ceiling="live 2", rule="P2 as its stress test read it: Failure ends a stage; conceding goes straight to judgment; no concession reward")
    rows = []
    for NA, NR in itertools.product(POOLS, POOLS):
        P = base_params(NR, "live_2", "accusatorial", SA=NA, DJ=BENCH, section="C3c")
        vals = {pl: goods_of(summarise(hearing_p2(pl, P), {"concede": "concede_fact"}.get(pl, pl), P)) for pl in ("deny", "concede", "justify")}
        hb = best_under(vals, dict(HEADLINE_W, stand=0.0, time=0.0))
        par = pareto(vals)
        rows.append((hb, par))
        log.w("result", section="C3c.control_p2", NA=NA, NR=NR, best_on_severity_alone=hb, weakly_dominated={k: v[0] for k, v in par.items() if v[0]},
              goods={k: {kk: round(vv, 4) for kk, vv in v.items()} for k, v in vals.items()})
    log.w("result", section="C3c.control_p2.summary", cells=len(rows), deny_alone_best_on_severity=sum(1 for hb, _ in rows if hb == ["deny"]),
          concede_weakly_dominated=sum(1 for _, par in rows if par["concede"][0]),
          note="the CONTROL for the plea repair: the same engine and pools, P2's transitions. Compare C3.plea.accusatorial.live_2 (the repaired plea under the same ceiling)")


def sec_grace(log):
    """C3d: the inquisitorial term of grace, a decision taken BEFORE any citation (02 1.1 rows 2-3)."""
    log.w("plan", section="C3d.grace", options=["come_forward", "wait"],
          rule="come forward in the term: light penance (admonition, severity 0.10), a public penance (standing 1 level, open), the cluster named (names 1); wait: denounced w.p. p_d (hidden), then cited and heard with his best in-hearing plea, and the cluster named only if he concedes",
          hidden="p_d {.2,.5,.8} (whether someone denounces him: no one tells him)", visible="his pool x the inquisitor's pool x he holds a defence proof")
    T = Tally("C3d.grace", ["come_forward", "wait"])
    for N, NI, prf in itertools.product(POOLS, (5.0, 7.8), (0.0, 1.5)):
        acc = defaultdict(lambda: defaultdict(float))
        P = base_params(N, "r37_3", "inquisitorial", SA=5, DJ=BENCH, DJ_proof=NI, proof_mod=prf, names_cost=1.0, section="C3d")
        _, s_h, _ = best_plea(P, PLEAS_INQ)
        gh = goods_of(s_h)
        for p_d in (0.2, 0.5, 0.8):
            cf = {"sev": -0.10, "risk": 0.0, "stand": -1.0, "time": 0.0, "names": -1.0}
            wt = {k: p_d * gh.get(k, 0.0) for k in set(gh) | {"names"}}
            for k, v in cf.items():
                acc["come_forward"][k] += v / 3
            for k, v in wt.items():
                acc["wait"][k] += v / 3
        opts = {k: dict(v) for k, v in acc.items()}
        T.add(N, opts, HEADLINE_W)
        log.w("result", section="C3d.grace", N=N, inquisitor=NI, defence_proof=prf, goods={k: {kk: round(vv, 4) for kk, vv in v.items()} for k, v in opts.items()},
              headline_best=best_under(opts, HEADLINE_W))
    log.w("summary", section="C3d.grace", verdict=T.verdict())


def main():
    global LOG
    ap = argparse.ArgumentParser()
    ap.add_argument("--log", default=DEFAULT_LOG)
    ap.add_argument("--mc", type=int, default=20000)
    ap.add_argument("--only", default=None)
    a = ap.parse_args()
    log = Log(a.log)
    LOG = log
    try:
        head = subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    except Exception as e:      # pragma: no cover
        head = f"unavailable: {e}"
    log.w("manifest", argv=sys.argv, head=head, python=sys.version.split()[0], platform=platform.platform(),
          pythonhashseed=os.environ.get("PYTHONHASHSEED"), proposal="2026-11-01-social-contest-proposal-4-authority-staged.md",
          harness=os.path.basename(__file__), real=["sigma_leverage.p_success", "roll_net", "roll_net_continuous", "net_boost", "soft_cap", "dice_engine.degree_from_net"],
          model="everything else (hearing chains, rites, payoffs, priors); no proposal-4 code exists",
          pools=POOLS, ceilings=CEILINGS, headline_ceiling=HEADLINE_CEILING, severity=SEV, weight_grid_size=len(WEIGHT_GRID), headline_weights=HEADLINE_W,
          stop_rule="each section ends when its grid is exhausted (exact computation, no sampling horizon); C0's Monte Carlo n is the --mc argument")
    sections = [("C0", lambda: sec_controls(log, a.mc)), ("C3", lambda: sec_plea(log)), ("C3b", lambda: sec_ceiling_for_deny(log)),
                ("C1", lambda: sec_defy(log)), ("C2", lambda: sec_forum(log)), ("C2b", lambda: sec_forum_challenge(log)),
                ("C4", lambda: sec_proofs(log)), ("C5", lambda: sec_advocate(log)), ("C6", lambda: sec_speech(log)),
                ("C7", lambda: sec_procedural(log)), ("C8", lambda: sec_appeal(log)), ("C9", lambda: sec_warrant(log)), ("C10", lambda: sec_characters(log)),
                ("C3c", lambda: sec_plea_p2_control(log)), ("C3d", lambda: sec_grace(log))]
    t0 = time.time()
    for name, fn in sections:
        if a.only and name not in a.only.split(","):
            continue
        ts = time.time()
        try:
            fn()
            log.w("section_end", section=name, wall_s=round(time.time() - ts, 2))
        except Exception as e:
            log.w("error", section=name, type=type(e).__name__, message=str(e), traceback=traceback.format_exc()[-2000:])
    log.w("summary", section="run", wall_s=round(time.time() - t0, 2), counts=dict(log.counts))
    log.close()


if __name__ == "__main__":
    main()
