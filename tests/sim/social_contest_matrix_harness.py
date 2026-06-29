#!/usr/bin/env python3
"""
social_contest_matrix_harness.py — factor-isolation / sensitivity harness for the social contest.

Operationalizes tests/sim/social_contest_test_matrix_v1.md. Isolates the marginal contribution of
every contributor (venue, adjudicator, faction allegiance, character faculty/standing/evidence,
policy, pressure, win-condition, faults, genre/tense, faction-layer) by:
  - a matched BASELINE control (symmetry must hold),
  - one-factor-at-a-time (OFAT) main effects,
  - per-unit marginal curves,
  - curated 2-way interaction cells,
with common-random-number (CRN) seeding for paired variance reduction.

Layer A (resolution architecture) runs against the validated groundup engine
(designs/audit/2026-06-03-contest-groundup/, 36/36 tests). Layer B-skeleton (pool->track->win)
runs against sim/personal/contest.py. Layer B-full (derived economy + bonus stack + interaction
types + ripple) is spec'd in the matrix doc and pending a canonical reference impl.

Run:
  python tests/sim/social_contest_matrix_harness.py [--n N] [--quick] [--block 0|1|2|3|4|sim|all] [--seed S]
"""
from __future__ import annotations
import os
import sys
import argparse
import random
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
_GROUNDUP = os.path.abspath(os.path.join(_HERE, "..", "..", "designs", "audit", "2026-06-03-contest-groundup"))
_REPO = os.path.abspath(os.path.join(_HERE, "..", ".."))
sys.path.insert(0, _GROUNDUP)  # bare-name groundup modules (engine, contract, ...) resolve here first

from contract import A, B, Adjudicator, Panel, Pressure          # noqa: E402
from primitives import Stasis, Dossier, EvidenceItem             # noqa: E402
from resolver import (Venue, Bout, Contestant, ThresholdRace,    # noqa: E402
                      TallyAtClose, ProofBar, GraceThreshold, VoteAtClose, PersuasionTrack)
from modes import (ContestedMode, VENUES, CROSS_CULTURAL_VENUES,  # noqa: E402
                   single_arbiter_mode, deliberative_body_mode, scholastic_disputation_mode)
import policy as POL                                              # noqa: E402
import faction as FX                                              # noqa: E402
from faction import Faction                                       # noqa: E402

try:                                  # Windows cp1252 console can't encode → × Δ ⌊⌋
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:                     # noqa: BLE001
    pass

# ---- presets -------------------------------------------------------------
NEUT = Adjudicator()
LOGOS = Adjudicator(discipline=.9, char_logos=.7, char_ethos=.2, char_pathos=.1)
PATHOS = Adjudicator(discipline=.3, char_pathos=.65, char_ethos=.2, char_logos=.15)
ETHOS = Adjudicator(discipline=.5, char_ethos=.7, char_pathos=.15, char_logos=.15)
CROWD = Adjudicator(discipline=.85, char_pathos=.65, char_ethos=.2, char_logos=.15)
ADJ = {"neutral": NEUT, "logos": LOGOS, "pathos": PATHOS, "ethos": ETHOS, "crowd": CROWD}

POL_MAP = {
    "logos": POL.logos_spammer, "pathos": POL.demagogue, "ethos": POL.courtier,
    "build": POL.build_then_close, "exploit": POL.exploiter,
    "overreach": POL.overreacher, "stall": POL.staller, "advocate": POL.advocate,
}
LOG, DEM, COU = POL.logos_spammer, POL.demagogue, POL.courtier

# proof-weight presets standing in for faction boost / allegiance axis
def venue_weights(ethos, pathos, logos, win=None, ground=Stasis.QUALITY, **kw):
    return Venue(proof_ethos=ethos, proof_pathos=pathos, proof_logos=logos,
                 start_ground=ground, win=win or ThresholdRace(5.0), **kw)

ALLEGIANCE = {
    "ethos-dominant": venue_weights(.55, .25, .20),
    "pathos-dominant": venue_weights(.20, .55, .25),
    "logos-dominant": venue_weights(.20, .25, .55, ground=Stasis.FACT),
    "balanced": venue_weights(.34, .33, .33),
}

WIN_CONDS = {
    "ThresholdRace": ThresholdRace(5.0),
    "TallyAtClose": TallyAtClose(),
    "ProofBar(defender)": ProofBar(4.0),
    "GraceThreshold": GraceThreshold(5.0),
    "VoteAtClose": VoteAtClose(jurors=7, noise=1.2),
    "PersuasionTrack": PersuasionTrack(),
}

# ---- runners (CRN-seeded) ------------------------------------------------
def rate(venue, fa, fb, pa, pb, adj=NEUT, N=1500, seed0=0, **kw):
    """ContestedMode-based outcome distribution with paired (CRN) seeding."""
    M = ContestedMode(venue, adjudicator=adj)
    w = Counter()
    for s in range(N):
        random.seed(seed0 + s)
        w[M.play(fa, fb, pa, pb, **kw)[0]] += 1
    return {k: v / N for k, v in w.items()}

def brate(fa, ca_extra, fb, cb_extra, venue, pa, pb, adj=NEUT, N=1500, seed0=0):
    """Bout-based runner so per-contestant standing/dossier can be set on each side.
    faculty is passed POSITIONALLY (the engine only ever does Contestant(<faculty>, ...))."""
    w = Counter()
    for s in range(N):
        random.seed(seed0 + s)
        b = Bout(Contestant(fa, **ca_extra), Contestant(fb, **cb_extra), venue, adj)
        w[b.resolve(pa, pb)[0]] += 1
    return {k: v / N for k, v in w.items()}

def a_adv(d):
    """A's net advantage = P(A-side outcomes) - P(B-side outcomes); handles banded PersuasionTrack."""
    a = d.get("a", 0) + d.get("A_decisive", 0) + d.get("A_total", 0)
    b = d.get("b", 0) + d.get("B_decisive", 0) + d.get("B_total", 0)
    return a - b

def fmt(d):
    return " ".join(f"{k}={v:.3f}" for k, v in sorted(d.items()))

def line(label, d, base_adv=None):
    s = f"  {label:<34} {fmt(d)}"
    if base_adv is not None:
        s += f"   Δadv={a_adv(d) - base_adv:+.3f}"
    print(s)

# ---- Block 0: symmetry / baseline control --------------------------------
def block0(N):
    print("\n== BLOCK 0 — symmetry / baseline control (matched 4v4 LOG/LOG, NEUTRAL) ==")
    print("  symmetric win-conditions must give |pA-pB| < 0.06; ProofBar/Grace are defender-favoured by design.")
    for name, wc in WIN_CONDS.items():
        v = venue_weights(.34, .33, .33, win=wc)
        d = rate(v, 4, 4, LOG, LOG, adj=NEUT, N=N)
        adv = a_adv(d)
        tol = max(0.06, 2.0 / (N ** 0.5))   # N-aware ~95% Monte-Carlo band; gate shouldn't cry wolf at low N
        flag = ""
        if name.startswith("ProofBar") or name.startswith("Grace"):
            flag = "  [asymmetric by design — expect defender lead]"
        elif abs(adv) > tol:
            flag = f"  [!! SYMMETRY FAIL > tol {tol:.3f}]"
        line(name, d)
        print(f"        A-adv={adv:+.3f}{flag}  (tol {tol:.3f})")

# ---- Block 1: OFAT main effects ------------------------------------------
def block1(N):
    print("\n== BLOCK 1 — OFAT main effects ==")
    base = rate("disputation", 4, 4, LOG, LOG, adj=NEUT, N=N)
    b_adv = a_adv(base)
    print(f"  baseline (disputation 4v4 LOG/LOG NEUTRAL): A-adv={b_adv:+.3f}")

    print(" -- venue (matched 4v4 LOG/LOG NEUTRAL; intrinsic resolution shape) --")
    for ven in ["disputation", "court", "assembly", "appeal"]:
        line(ven, rate(ven, 4, 4, LOG, LOG, adj=NEUT, N=N))
    for ven in ["public_oration", "inquisition_hearing", "excommunication_court",
                "imperial_petition", "secret_council", "memorial_remonstrance"]:
        m = CROSS_CULTURAL_VENUES[ven]()
        w = Counter()
        for s in range(N):
            random.seed(s)
            w[m.play(4, 4, LOG, LOG)[0]] += 1
        line(ven, {k: v / N for k, v in w.items()})

    print(" -- adjudicator (court, logos-orator A vs pathos-orator B; Δ shows judge flip) --")
    for an, adj in ADJ.items():
        line(an, rate("court", 4, 4, LOG, DEM, adj=adj, N=N))

    print(" -- allegiance / boost axis (orator style vs a logos-weighted venue; boost-match wins) --")
    for pn in ["logos", "pathos", "ethos"]:
        line(f"A={pn} vs logos-venue", rate(ALLEGIANCE["logos-dominant"], 4, 4, POL_MAP[pn], LOG, adj=NEUT, N=N))

    print(" -- orator style/policy (disputation, A=style vs B=logos NEUTRAL) --")
    for pn in ["logos", "pathos", "ethos", "build", "exploit", "overreach", "stall"]:
        line(pn, rate("disputation", 4, 4, POL_MAP[pn], LOG, adj=NEUT, N=N), b_adv)

    print(" -- institutional pressure (flat venue, toward A) --")
    for inst in [0.0, 0.25, 0.5]:
        v = venue_weights(.34, .33, .33, pressure=Pressure(toward="a", institutional=inst))
        line(f"institutional={inst}", rate(v, 4, 4, LOG, LOG, adj=NEUT, N=N), b_adv)

    print(" -- evidence (A holds k relevant FACT items; logos/FACT venue) --")
    vev = venue_weights(.25, .20, .55, ground=Stasis.FACT)
    for k in [0, 1, 2, 3]:
        doss = Dossier([EvidenceItem(Stasis.FACT, 2.5 - 0.5 * i) for i in range(k)])
        line(f"evidence={k}", rate(vev, 4, 4, POL.advocate, LOG, adj=NEUT, N=N, da=doss), b_adv)

# ---- Block 2: per-unit marginal curves -----------------------------------
def block2(N):
    print("\n== BLOCK 2 — per-unit marginal curves ==")
    print(" -- faculty (A faculty 1..7 vs B=4; disputation LOG/LOG NEUTRAL) --")
    prev = None
    for fa in range(1, 8):
        d = rate("disputation", fa, 4, LOG, LOG, adj=NEUT, N=N)
        adv = a_adv(d)
        slope = "" if prev is None else f"  Δ/pt={adv - prev:+.3f}"
        print(f"  faculty={fa}  A-adv={adv:+.3f}{slope}")
        prev = adv

    print(" -- standing (A standing 0..9 vs B default; fused venue, NEUTRAL) --")
    vf = Venue(start_ground=Stasis.FACT, win=TallyAtClose(), split_standing=False)
    for stg in [0, 2, 5, 7, 9]:
        d = brate(4, dict(standing_start=stg), 4, {}, vf, LOG, LOG, adj=NEUT, N=N)
        print(f"  standing={stg}  A-adv={a_adv(d):+.3f}")
    print("   (split-standing comparison at standing=9: should lend ~no force)")
    vs = Venue(start_ground=Stasis.FACT, win=TallyAtClose(), split_standing=True)
    d = brate(4, dict(standing_start=9), 4, {}, vs, LOG, LOG, adj=NEUT, N=N)
    print(f"  standing=9 SPLIT  A-adv={a_adv(d):+.3f}")

    print(" -- panel size (court, logos-orator vs demagogue, mixed logos+pathos panel; softens single judge) --")
    line("single logos judge", rate("court", 4, 4, LOG, DEM, adj=LOGOS, N=N))
    for k in [2, 3, 5, 7]:
        members = tuple((LOGOS if i % 2 == 0 else PATHOS) for i in range(k))
        line(f"panel({k})", rate("court", 4, 4, LOG, DEM, adj=Panel(members), N=N))

    print(" -- public pressure x crowd-judge unlock (demagogue vs logos, logos-role venue) --")
    vrole = venue_weights(.25, .20, .55, ground=Stasis.FACT)
    for pub in [0.0, 0.35, 0.7]:
        v = venue_weights(.25, .20, .55, ground=Stasis.FACT, pressure=Pressure(public=pub))
        line(f"public={pub}", rate(v, 4, 4, DEM, LOG, adj=CROWD, N=N))

    print(" -- CR6 uniform-impact diagnostic: Δadv from a +1 faculty step at base 2/4/6 --")
    for base in [2, 4, 6]:
        lo = a_adv(rate("disputation", base, base, LOG, LOG, adj=NEUT, N=N))
        hi = a_adv(rate("disputation", base + 1, base, LOG, LOG, adj=NEUT, N=N))
        print(f"  base={base}: Δadv(+1 faculty)={hi - lo:+.3f}   (uniform-impact ⇒ ~constant across bases)")

# ---- Block 3: interaction cells ------------------------------------------
def block3(N):
    print("\n== BLOCK 3 — 2-way interaction cells ==")
    print(" -- venue x adjudicator (logos-orator A vs demagogue B) --")
    for ven in ["disputation", "court", "assembly"]:
        row = {an: round(a_adv(rate(ven, 4, 4, LOG, DEM, adj=adj, N=N)), 3) for an, adj in
               (("logos", LOGOS), ("pathos", PATHOS))}
        print(f"  {ven:<12} A-adv by judge: {row}")

    print(" -- faculty-gap x win-condition (A=6 vs B=2; does the venue damp the skill gap?) --")
    for name, wc in [("ThresholdRace", ThresholdRace(5.0)), ("ProofBar", ProofBar(4.0)),
                     ("PersuasionTrack", PersuasionTrack())]:
        v = venue_weights(.34, .33, .33, win=wc)
        line(name, rate(v, 6, 2, LOG, LOG, adj=NEUT, N=N))

    print(" -- standing x split-flag (A standing 9 vs 4) --")
    for split in [False, True]:
        v = Venue(start_ground=Stasis.FACT, win=TallyAtClose(), split_standing=split)
        d = brate(4, dict(standing_start=9), 4, {}, v, LOG, LOG, adj=NEUT, N=N)
        print(f"  split_standing={split}: A-adv={a_adv(d):+.3f}")

    print(" -- public-pressure x adjudicator-discipline (crowd vs neutral, demagogue A) --")
    for an, adj in (("crowd", CROWD), ("neutral", NEUT)):
        lo = a_adv(rate(venue_weights(.25, .20, .55, ground=Stasis.FACT), 4, 4, DEM, LOG, adj=adj, N=N))
        hi = a_adv(rate(venue_weights(.25, .20, .55, ground=Stasis.FACT,
                                      pressure=Pressure(public=0.7)), 4, 4, DEM, LOG, adj=adj, N=N))
        print(f"  {an}: public 0.0->0.7  Δadv={hi - lo:+.3f}")

# ---- Block 4: faction layer (BG) -----------------------------------------
def block4(N):
    print("\n== BLOCK 4 — faction layer (BG votes / succession / censure) ==")
    Fc = lambda n, m: Faction(n, m, 4, (.34, .33, .33))
    strong = [(Fc("a", 4), "pro"), (Fc("b", 3), "pro"), (Fc("c", 2), "anti"), (Fc("d", 2), "anti")]
    bal = [(Fc("a", 4), "pro"), (Fc("b", 2), "pro"), (Fc("c", 4), "anti"), (Fc("d", 2), "anti")]
    print(f"  coalition strong-pro : {FX.coalition_rate(strong, N=N)}")
    print(f"  coalition balanced   : {FX.coalition_rate(bal, N=N)}")
    print(f"  coalition bal +lobby : {FX.coalition_rate(bal, N=N, lobby=1.0)}")
    print(f"  succession 4v4 (split expected)     : {FX.succession_rate(4, 4, NEUT, N=N)}")
    print(f"  succession 7v1 (decisive/unified)   : {FX.succession_rate(7, 1, NEUT, N=N)}")
    prop = Faction("P", 4, 5, (.45, .2, .35)); targ = Faction("T", 2, 3, (.2, .35, .45))
    body = [prop, targ, Faction("H", 3, 4, (.2, .2, .6)), Faction("C", 2, 4, (.6, .2, .2))]
    dist, _ = FX.rate_banded(prop, targ, body, "censure", LOG, DEM, N=N)
    print(f"  censure (strong proposer)           : {dist}")

# ---- reduced-sim block (Layer B-skeleton) --------------------------------
def block_sim(N):
    print("\n== BLOCK sim — reduced sim (Layer B-skeleton: pool->track->win) ==")
    if _REPO not in sys.path:
        sys.path.append(_REPO)
    try:
        from sim.personal.contest import run_contest
    except Exception as e:  # noqa: BLE001
        print(f"  [skipped — could not import sim.personal.contest: {e}]")
        return

    class Actor:
        def __init__(self, side, attr, history=3, focus=4):
            self.side = side; self.actor_id = side
            self.primary_attribute = attr; self.history = history; self.focus = focus

    def srate(attr_a, attr_b=4, resistance=1, exchanges=3, start=5, N=N):
        w = Counter(); tv = 0
        for s in range(N):
            parties = [Actor("A", attr_a), Actor("B", attr_b)]
            res = run_contest(parties, dict(exchange_count=exchanges, resistance=resistance,
                                            starting_track=start), rng=random.Random(s))
            w[res.winner or "compromise"] += 1
            tv += 1 if res.total_victory else 0
        return {k: v / N for k, v in w.items()}, tv / N

    print(" -- primary attribute A 1..7 (vs B=4, resistance=1, 3 exchanges) --")
    for a in range(1, 8):
        d, tv = srate(a)
        print(f"  attr={a}  A-win={d.get('A', 0):.3f} B-win={d.get('B', 0):.3f} compromise={d.get('compromise', 0):.3f} total={tv:.3f}")
    print(" -- audience resistance 0..2 (A=5 vs B=4) --")
    for r in [0, 1, 2]:
        d, tv = srate(5, resistance=r)
        print(f"  resistance={r}  A-win={d.get('A', 0):.3f} compromise={d.get('compromise', 0):.3f}")
    print(" -- exchange count 1/3/5 (A=5 vs B=4) --")
    for ex in [1, 3, 5]:
        d, tv = srate(5, exchanges=ex)
        print(f"  exchanges={ex}  A-win={d.get('A', 0):.3f} compromise={d.get('compromise', 0):.3f} total={tv:.3f}")
    print(" -- starting track 3/5/7 (A=4 vs B=4; track bias) --")
    for st in [3, 5, 7]:
        d, tv = srate(4, start=st)
        print(f"  start={st}  A-win={d.get('A', 0):.3f} B-win={d.get('B', 0):.3f} compromise={d.get('compromise', 0):.3f}")

# ---- Block bfull: canonical reference (Layer B-full) ---------------------
def block_bfull(N):
    print("\n== BLOCK bfull — canonical reference (derived economy + bonus stack + interaction types + ripple) ==")
    try:
        from social_contest_reference import Orator, Venue as RV, run_reference_contest
    except Exception as e:  # noqa: BLE001
        print(f"  [skipped — could not import social_contest_reference: {e}]"); return

    BA = dict(primary=4, history=3, cha=4, focus=4, spirit=3, attunement=4, genre="Memory", orientation="Revealing")
    BB = dict(primary=4, history=3, cha=4, focus=4, spirit=3, attunement=4, genre="Memory", orientation="Obscuring")
    BV = dict(proceeding="Formal", exchanges=3, resistance0=1, start_track=5, primary_genre="Memory", erosion=True)

    def rref(aov=None, bov=None, vov=None, n=N, seed0=0):
        aov, bov, vov = aov or {}, bov or {}, vov or {}
        agg = Counter(); tv = spent = 0; strB = strA = exr = 0; rip = Counter()
        for s in range(n):
            a = Orator("A", **{**BA, **aov}); b = Orator("B", **{**BB, **bov}); v = RV(**{**BV, **vov})
            r = run_reference_contest(a, b, v, random.Random(seed0 + s))
            agg[r.winner or "comp"] += 1; tv += r.total_victory; spent += r.spent_events
            strB += r.strain_dealt["B"]; strA += r.strain_dealt["A"]; exr += r.exchanges_run
            for fl, on in (("obligation", r.obligation), ("ms", r.ms_comove),
                           ("scar", r.scar), ("fatigue", bool(r.contest_fatigue))):
                if on:
                    rip[fl] += 1
            if r.domain_echo:
                rip["echo_" + r.domain_echo] += 1
        return dict(winA=agg["A"] / n, winB=agg["B"] / n, comp=agg["comp"] / n, total=tv / n,
                    spent=spent / n, strB=strB / n, exch=exr / n, rip={k: v / n for k, v in rip.items()})

    def adv(m):
        return m["winA"] - m["winB"]

    base = rref()
    print(f"  baseline CLASH (matched Mem/Rev vs Mem/Obs): winA={base['winA']:.3f} winB={base['winB']:.3f} "
          f"comp={base['comp']:.3f}  A-adv={adv(base):+.3f}  (symmetry: |A-adv| should be small)")

    print(" -- Charisma(A) 1..7 → Composure buffer + strain dealt (Cha-mod) --")
    for c in range(1, 8):
        m = rref(aov=dict(cha=c))
        print(f"  chaA={c}  A-adv={adv(m):+.3f}  strain_to_B={m['strB']:.2f}")
    print(" -- Focus×Spirit(A) → Concentration → Spent frequency --")
    for fo, sp in [(1, 1), (2, 3), (4, 3), (6, 3), (7, 7)]:
        m = rref(aov=dict(focus=fo, spirit=sp))
        print(f"  focA={fo} spiA={sp}  Conc={3 * fo + 2 * sp}  mean_spent_events={m['spent']:.2f}  A-adv={adv(m):+.3f}")
    print(" -- interaction type (forced via genre/orientation) --")
    for name, ao, bo in [("CLASH", {}, {}),
                         ("REINFORCE", dict(orientation="Revealing"), dict(orientation="Revealing")),
                         ("CROSS", dict(genre="Memory"), dict(genre="Projection"))]:
        m = rref(aov=ao, bov=bo)
        print(f"  {name:<10} winA={m['winA']:.3f} winB={m['winB']:.3f} comp={m['comp']:.3f} strain_to_B={m['strB']:.2f}")
    print(" -- bonus-dice stack (A only), Δadv vs baseline --")
    for label, ao, vo in [("+audience-boost", {}, dict(boost_axis="orientation", boost_value="Revealing")),
                          ("+Recall(+2D)", dict(uses_recall=True), {}),
                          ("+Findings(+2D ex1)", dict(findings=2), {}),
                          ("+Resonant(+1D)", dict(resonant=True), {}),
                          ("+Momentum(1)", dict(momentum=1), {})]:
        m = rref(aov=ao, vov=vo)
        print(f"  {label:<20} A-adv={adv(m):+.3f}  Δ={adv(m) - adv(base):+.3f}")
    print(" -- CR6 uniform-impact: Δadv from Recall(+2D) at primary 2/4/6 (uniform ⇒ ~constant) --")
    for p in [2, 4, 6]:
        lo = adv(rref(aov=dict(primary=p), bov=dict(primary=p)))
        hi = adv(rref(aov=dict(primary=p, uses_recall=True), bov=dict(primary=p)))
        print(f"  primary={p}: Δadv(Recall +2D)={hi - lo:+.3f}")
    print(" -- audience resistance × erosion → compromise rate (Grand, 5 exchanges) --")
    for r0 in [0, 1, 2]:
        for er in [True, False]:
            m = rref(vov=dict(resistance0=r0, erosion=er, proceeding="Grand", exchanges=5))
            print(f"  res0={r0} erosion={er!s:<5}: comp={m['comp']:.3f}  A-adv={adv(m):+.3f}")
    print(" -- RIPPLE rates (Grand, A primary 6 vs 4 to force decisives; Resonant on) --")
    m = rref(aov=dict(primary=6, resonant=True), vov=dict(proceeding="Grand", exchanges=5))
    print(f"  winA={m['winA']:.3f} comp={m['comp']:.3f} total={m['total']:.3f}  ripple={m['rip']}")


# ---- main ----------------------------------------------------------------
BLOCKS = {"0": block0, "1": block1, "2": block2, "3": block3, "4": block4,
          "bfull": block_bfull, "sim": block_sim}

def main():
    ap = argparse.ArgumentParser(description="Social-contest factor-isolation harness")
    ap.add_argument("--n", type=int, default=1500, help="replicates per cell (default 1500)")
    ap.add_argument("--quick", action="store_true", help="N=400 smoke run")
    ap.add_argument("--block", default="all", help="0|1|2|3|4|sim|all")
    ap.add_argument("--seed", type=int, default=20260623, help="master seed")
    args = ap.parse_args()
    N = 400 if args.quick else args.n
    random.seed(args.seed)
    print(f"social_contest_matrix_harness — N={N} per cell, master seed={args.seed}")
    print(f"groundup engine: {_GROUNDUP}")
    order = ["0", "1", "2", "3", "4", "bfull", "sim"] if args.block == "all" else [args.block]
    for key in order:
        fn = BLOCKS.get(key)
        if fn is None:
            print(f"  [unknown block: {key}]"); continue
        fn(N)
    print("\ndone.")

if __name__ == "__main__":
    main()
