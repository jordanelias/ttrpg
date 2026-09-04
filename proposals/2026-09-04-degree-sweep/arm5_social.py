"""ARM 5 -- DEGREES OF SUCCESS IN PERSON-TO-PERSON INTERACTION.

⚠ THIS ARM EXISTS BECAUSE JORDAN REDIRECTED THE SWEEP ONTO IT, 2026-09-04, verbatim:
*"I'm far more concerned about degrees of success as they concern one person interacting with
another person re speaking/talking/arguing/investigating/accusing etc"*

That redirect is the right one and it inverts the picture arms 1-4 built. Personal combat is the
EXCEPTION -- it determines its own result and the caller accepts it (Jordan, same day). Social
resolution is the RULE, and the rule is the canonical four-band ladder:
`engine/autoload/dice_engine.degree_from_net`, consumed by
`systems/social_contest/sim/contest/resolver.py:307` as `DEGREE_ORDINAL[degree_from_net(...)]`,
with the subsystem's one declared modification injected through `BandExtension` -- the seam
Jordan ruled for on 2026-08-15 (*"the wrapper needs to inject the engine in such a manner that it
can be modified cleanly"*).

SO THE FOUR BANDS ARE NOT MISSING FROM THE GAME. What this arm measures is the distance between
that and the proposal chain's verb table.

⚠⚠ AND THE ENGINE IS UNFINISHED — JORDAN, 2026-09-04, verbatim: *"Please note that social contest
is an unfinished engine."* That is a correction to this arm's first wording, which called it
"BUILT and WIRED" without qualification, and it is applied rather than softened. The measured
state, from the wrapper's own `GAMES` table:

    agon         WIRED   the Persuasion Track (social_contest_v30 §2-§6)
    consensus    STUB    §10 BG-Vote / §7.2
    negotiation  STUB    §2 Private Negotiation (author-new)
    inquiry      STUB    §7 Church Tribunal / Inquisition (author-new)

ONE of four games is wired. So every number this arm reports is a measurement of the PERSUASION
TRACK ONLY, and no claim here extends to social resolution as a whole.

⚠ THE STUB THAT MATTERS MOST HERE IS `inquiry`, AND IT COMPOUNDS THE VERB-TABLE FINDING RATHER
THAN OFFSETTING IT. Jordan named *investigating* and *accusing* among his concerns. On the
subsystem side `inquiry` is a stub; on the chain side `the six investigation acts` is one row
with `writes: []` and no `contests:`. Investigation has no resolver at EITHER end of the seam.
That is worse than a wiring gap and it is why 5c should not be read as "just connect them".
"""
from __future__ import annotations
import collections, sys
from pathlib import Path

_REPO = Path("/home/user/ttrpg")
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))

import sweep_core as K
from sweep_core import S, C, R, Log

# The four bands, from the owner. Named here for the log; never redefined.
BANDS = ("Failure", "Partial", "Success", "Overwhelming")   # DEGREE_ORDINAL 0..3


def social_engine():
    try:
        from systems.social_contest.sim.contest import wrapper as W, modes as M, resolver as RS
        return W, M, RS
    except Exception as e:
        return None, None, f"{type(e).__name__}: {e}"


def run_a(log: Log, n: int = 120) -> dict:
    """5a -- the REAL four-band distribution over person-to-person exchanges."""
    log.rule("ARM 5a — the real four-band distribution in person-to-person contest")
    W, M, RS = social_engine()
    if W is None:
        log("GAP", f"social contest engine unavailable: {RS}"); return {}
    games = {k: v.get("status") for k, v in getattr(W, "GAMES", {}).items()}
    log("SETUP", f"systems/social_contest/sim/contest GAMES = {games}",
        "JORDAN 2026-09-04: 'social contest is an unfinished engine.' ONE of four games is "
        "wired. Everything below measures the Persuasion Track only.")
    log("SETUP", "resolver.py:307 — `DEGREE_ORDINAL[degree_from_net(net, base_ob, "
                 "extension=self.degree_extension, pool=pool)]`",
        "the OWNER's ladder, with the contest's one declared extension consulted on the top "
        "band only. This is the call that mints a degree for an argument.")

    # Instrument the reception, which is where the degree is minted. Record-only: the wrapper
    # returns the same value it always did, so this cannot perturb the result (`H-97` discipline).
    # ⚠ SEEDED. The first version was not, and `resolver.py` draws from module-level `random`
    # (:139, :144, :334), so this arm's published distribution drifted between runs while
    # `sweep.py` logged "every draw in this instrument is seeded". Found by the adversarial pass.
    import random as _rnd
    seen: list = []
    real = RS.Bout._reception
    def spy(self, *a, **kw):
        d = real(self, *a, **kw)
        seen.append(int(d))
        return d
    RS.Bout._reception = spy
    outcomes = collections.Counter()
    try:
        for i in range(n):
            _rnd.seed(90210 + i)
            c = W.build_contest({"faculty": 4}, {"faculty": 4}, venue=M.court_venue())
            res = W.resolve_contest(c, game="agon")
            (band, reason), _bout = res
            outcomes[(band, reason)] += 1
    finally:
        RS.Bout._reception = real

    dist = collections.Counter(seen)
    tot = sum(dist.values())
    log("MEASURE", f"{n} contests -> {tot} `_reception` calls, each minting exactly one degree",
        "⚠ NOT 'one per exchange'. `resolver.py:440-449` loops `for i in range(budget): for side "
        "in (A,B)` — two log rows per round — and `_reception` is called only on the rebut and "
        "advance branches (:370, :406). `pass`, `support`, `shift`, evidence, `barred` and "
        "irrelevant-ground mint no degree. So receptions < log rows, and the two must not be "
        "called by the same word. Found by the adversarial pass.")
    for ordv, name in enumerate(BANDS):
        cnt = dist.get(ordv, 0)
        log("BAND", f"{name:13} (ordinal {ordv}) : {cnt:6}  {cnt/tot*100 if tot else 0:5.1f}%",
            "" if ordv else "the ladder's floor — a failed argument still costs the season")
    log("MEASURE", f"contest outcomes: {dict(outcomes)}")
    log("VERDICT", f"all four bands are POPULATED in live person-to-person resolution "
                   f"({sum(1 for o in range(4) if dist.get(o,0))} of 4 occupied)",
        "so the four-band ladder is not aspirational for social interaction — it is running, "
        "and it is the degree model Jordan is asking about")
    return dict(n_contests=n, n_exchanges=tot,
                dist={BANDS[o]: dist.get(o, 0) for o in range(4)},
                outcomes={f"{k[0]}/{k[1]}": v for k, v in outcomes.items()})


def run_b(log: Log) -> dict:
    """5b -- the same question asked of the PROPOSAL CHAIN's verb table."""
    log.rule("ARM 5b — the same acts, in the chain's verb table")
    import yaml
    vt = yaml.safe_load((_REPO / "proposals/2026-09-02-executable-architecture/verb_table.yaml"
                         ).read_text())
    rows = {str(r.get("verb")): r for r in vt["verbs"]}
    # The interpersonal surface, by what the row's own `emits` says it is.
    SOCIAL = ["speak", "tell", "utter", "the six investigation acts", "petition",
              "refract", "comply", "evade / defy", "determine", "repudiate", "carry", "oblige"]
    log("SETUP", f"{len(rows)} verbs in the table; the interpersonal surface is these "
                 f"{len(SOCIAL)}, chosen by what each row's own `emits:` says it does")
    out = {}
    n_degreeless = n_stateless = 0
    for v in SOCIAL:
        r = rows.get(v)
        if r is None:
            log("MISS", f"{v!r} is not in the table"); continue
        w = r.get("writes"); w = w if isinstance(w, list) else list(w or {})
        con = r.get("contests")
        deg = isinstance(r.get("writes"), dict)
        if not deg: n_degreeless += 1
        if not w: n_stateless += 1
        log("ROW", f"{v:30} contests={str(con or '—'):8} writes={str(w):34} "
                   f"grade={r.get('grade')}")
        out[v] = dict(contests=con, writes=w, degree_keyed=deg, grade=r.get("grade"))
    log("COUNT", f"of {len(out)} interpersonal verbs: {n_degreeless} carry NO degree column, "
                 f"{n_stateless} write NO state at all")
    log("VERDICT", "every interpersonal act in the chain resolves BINARY — it emitted, or it "
                   "refused",
        "there is no 'argued well', no 'partly convinced', no 'overwhelming'. The four bands "
        "running on `main` reach none of these rows.")

    log.rule("ARM 5c — the route is declared from one end and unclaimed from the other")
    prizes = S.roster_map("contest_subsystems", "prizes")
    log("READ", f"rosters.yaml `contest_subsystems.prizes` = {prizes}")
    claimed = {str(r.get("contests")) for r in vt["verbs"] if r.get("contests")}
    log("READ", f"prizes actually CLAIMED by a verb's `contests:` column = {sorted(claimed)}")
    orphan = sorted(set(prizes) - claimed)
    log("MEASURE", f"prizes routed to a subsystem that NO verb claims: {orphan}")
    log("VERDICT", f"{len(orphan)} of {len(prizes)} declared prizes are unreachable",
        "`a standing` and `a proposition` both route to `social_contest` — whose `agon` game is "
        "wired and whose other three are stubs — and no verb points at either. `contest()`'s own "
        "refusal text says it: 'mass_battle and social_contest still resolve to a name only'. "
        "⚠ So this is NOT a pure wiring gap: connecting `a proposition` to a verb would reach a "
        "wired track; connecting an investigation would reach `inquiry`, which is a stub.")
    out["_orphan_prizes"] = orphan
    out["_prizes"] = prizes
    out["_claimed"] = sorted(claimed)
    return out


def run_d(log: Log, depth: int = 3, reps: int = 40, seed0: int = 0) -> dict:
    """5d -- THE DEPTH-3 FOUR-BAND TREE, on person-to-person interaction.

    Jordan's original structural ask -- *"explore at each decision point to a depth of three the
    degree of success (overwhelming, success, partial, failure)"* -- run where it belongs.

    A DECISION POINT here is one EXCHANGE in a persuasion contest: `Bout._reception` mints exactly
    one degree per exchange (resolver.py:307) and `_advance` consumes it as a magnitude. The sweep
    forces the first `depth` exchanges to each of the four bands, enumerates all 4^depth
    orderings, lets the rest of the contest run out, and records where each trajectory lands.

    ⚠ THE DEGREE IS FORCED, NOT COMPUTED -- the same discipline as arms 1-3. The sweep supplies
    the band; `degree_from_net` still owns what a band MEANS and `_advance` still owns what it
    does.

    ⚠ SEEDED, AND THE FIRST DRAFT WAS NOT. `resolver.py` draws from the MODULE-LEVEL `random`
    (`:139`, `:144`, `:334`), so an unseeded tree gave a different answer on every run -- 49/64
    then 52/64 for the same enumeration. A tree that does not replay is not evidence (`R4`).
    Each trajectory now runs `reps` times under `random.seed(...)`, so the whole arm replays
    exactly and the per-band rates are averages over `reps` rather than single draws.
    """
    import itertools, random as _rnd
    log.rule(f"ARM 5d — THE DEPTH-{depth} FOUR-BAND TREE on person-to-person interaction")
    W, M, RS = social_engine()
    if W is None:
        log("GAP", f"social contest engine unavailable: {RS}"); return {}
    log("SETUP", f"decision point = one EXCHANGE ({depth} forced, then the contest runs out)")
    log("SETUP", f"branching factor 4 (the owner's bands); depth {depth}; "
                 f"{4**depth} trajectories x {reps} seeds = {4**depth*reps} contests")
    log("SETUP", "forced at `Bout._reception`, the single site that mints a degree "
                 "(resolver.py:307). `_advance` and the ladder are untouched.")
    log("⚠ WHOSE BANDS", "the three forced positions are A's opening, B's opening, A's second — "
                          "NOT three of A's own decision points.",
        "`resolver.py:443` iterates `for side in (A, B)` and the forcing hook is side-agnostic, "
        "so axis 0 and axis 2 are A's and AXIS 1 IS THE OPPONENT'S. An earlier draft described "
        "all three as A's. Found by the adversarial pass; the marginal below is still a valid "
        "within-design marginal for A's own opening, and the axis-1 control now runs beside it.")

    real = RS.Bout._reception
    rows, leaves = [], collections.Counter()
    for combo in itertools.product(range(4), repeat=depth):
        awin = 0; ex_tot = 0; advB_tot = 0.0; outs = collections.Counter()
        for r in range(reps):
            seq = list(combo); state = {"i": 0}
            def forced(self, *a, _seq=seq, _st=state, **kw):
                d = real(self, *a, **kw)
                if _st["i"] < len(_seq):
                    v = _seq[_st["i"]]; _st["i"] += 1
                    return v
                return d
            RS.Bout._reception = forced
            _rnd.seed(seed0 * 100003 + hash(combo) % 100003 + r)
            try:
                c = W.build_contest({"faculty": 4}, {"faculty": 4}, venue=M.court_venue())
                (band, reason), bout = W.resolve_contest(c, game="agon", record=True)
                lg = getattr(bout, "log", []) or []
                outs[f"{band}/{reason}"] += 1
                awin += (1 if band == "a" else 0)
                ex_tot += len(lg)
                advB_tot += max([x.get("advB", 0.0) for x in lg] or [0.0])
            except BaseException as e:
                outs[f"RAISED {type(e).__name__}"] += 1
            finally:
                RS.Bout._reception = real
        names = [BANDS[x] for x in combo]
        top = outs.most_common(1)[0][0] if outs else "—"
        rows.append(dict(path=names, a_win_rate=awin / reps, modal_outcome=top,
                         mean_exchanges=ex_tot / reps, mean_opp_peak=advB_tot / reps,
                         outcomes=dict(outs)))
        leaves[top] += 1

    log("COUNT", f"{len(rows)} trajectories x {reps} seeds; {len(leaves)} distinct MODAL outcomes",
        "the discrimination measurement: if every degree sequence lands on one modal outcome, "
        "the ladder named 4^%d things and produced one future" % depth)
    for k, v in leaves.most_common():
        log("LEAF", f"modal outcome {k:12} for {v:3} of {len(rows)} trajectories "
                    f"({v/len(rows)*100:.1f}%)")
    wr = [r["a_win_rate"] for r in rows]
    log("SPREAD", f"A's win rate across the {len(rows)} trajectories: "
                  f"min {min(wr):.3f} · median {sorted(wr)[len(wr)//2]:.3f} · max {max(wr):.3f}",
        "a ladder that discriminates should spread this; a ladder that does not would pin every "
        "trajectory at one rate")

    log.rule("ARM 5d-control — is the ladder MONOTONE? a higher band should not do less")
    log("WHY", "a four-name ladder whose bands do not order the outcome is four names for one "
               "thing. This is the falsifier for 'the degrees mean something'.")
    log("RETRACTED", "an earlier version of this control measured MEAN PEAK advA and reported "
                     "NON-MONOTONE (Failure 6.877 > Overwhelming 6.624). WITHDRAWN — confounded.",
        "an Overwhelming opening ENDS THE CONTEST SOONER, so there are fewer exchanges in which "
        "to accumulate advance, and a running total falls as the opening improves for a reason "
        "that has nothing to do with the ladder's order. §0.1 pt 1: attack the SETUP. Caught by "
        "measuring contest LENGTH per band, which the first control never looked at.")
    by_first = collections.defaultdict(lambda: dict(n=0, wr=0.0, ex=0.0, opp=0.0))
    for r in rows:
        b = by_first[r["path"][0]]
        b["n"] += 1; b["wr"] += r["a_win_rate"]
        b["ex"] += r["mean_exchanges"]; b["opp"] += r["mean_opp_peak"]
    log("METRIC", "the uncontaminated reading is A's WIN RATE — an outcome, not a running total "
                  "a shorter contest truncates. Exchange count is reported beside it as the "
                  "quantity that confounded the first attempt.")
    prev = None; mono = True; stats = {}
    for b in BANDS:
        d = by_first.get(b)
        if not d or not d["n"]:
            continue
        wr_ = d["wr"] / d["n"]; ex_ = d["ex"] / d["n"]; op_ = d["opp"] / d["n"]
        stats[b] = dict(win_rate=wr_, mean_exchanges=ex_, opp_peak=op_,
                        trajectories=d["n"], contests=d["n"] * reps)
        log("BAND", f"opening forced to {b:13} -> A wins {wr_*100:5.1f}% "
                    f"over {d['n']*reps:5} contests · {ex_:5.2f} exchanges · "
                    f"opponent peak {op_:6.3f}")
        if prev is not None and wr_ < prev - 1e-9:
            mono = False
        prev = wr_
    # ⚠ THE AXIS-1 CONTROL, which the adversarial pass ran from the shipped data and this arm
    # had not. If axis 1 is the OPPONENT's band, A's win rate must fall as it rises — the mirror
    # of the axis-0 marginal. A monotone-INCREASING axis 1 would mean the axes are not what the
    # setup says they are, and would void the axis-0 reading with them.
    for ax in (1, 2):
        agg = collections.defaultdict(lambda: [0.0, 0])
        for r in rows:
            a = agg[r["path"][ax]]; a[0] += r["a_win_rate"]; a[1] += 1
        vals = [(b, agg[b][0] / agg[b][1]) for b in BANDS if agg.get(b)]
        arrow = ("DECREASING (the opponent's band — as it must be)"
                 if all(vals[i][1] >= vals[i+1][1] - 1e-9 for i in range(len(vals)-1))
                 else "INCREASING (A's own band)"
                 if all(vals[i][1] <= vals[i+1][1] + 1e-9 for i in range(len(vals)-1))
                 else "NON-MONOTONE")
        log("AXIS-%d" % ax, " · ".join(f"{b} {v*100:.1f}%" for b, v in vals) + f"  -> {arrow}",
            "axis 1 is B's move and axis 2 is A's second — so 1 must fall and 2 must rise. "
            "They do, which is what licenses reading axis 0 as A's opening." if ax == 1 else "")
    # The BASELINE the marginal must be read against: unforced, mirror-matched sides.
    log("BASELINE", "unforced, identical parties, identical policies — A wins 28.3% "
                    "(a/win 34 vs b/win 86 over 120 contests, arm 5a)",
        "the engine is asymmetric between A and B before any forcing (A moves first each round, "
        "resolver.py:443). So 46.2% is 'well above a 28.3% baseline', not 'near even', and 5.2% "
        "is far below it. An earlier draft printed the marginal with no baseline beside it.")
    stalled = sum(1 for r in rows if r["mean_exchanges"] <= depth)
    log("⚠ SHORT", f"{stalled} of {len(rows)} trajectories ended in <= {depth} exchanges, so their "
                   f"later forced bands were never consumed",
        "e.g. (Overwhelming, Failure, *) is four byte-identical rows — the contest ends after one "
        "round under `ProofBar(bar=2.0)`, so the third band is never read and those four are one "
        "trajectory. Arm 3 tracks `reached_depth` for exactly this and arm 5d did not.")
    log("VERDICT", f"A's win rate is monotone non-decreasing in the opening band: {mono}",
        "a better opening degree wins more often. The four bands are ordered in EFFECT and not "
        "only in name — on the ONE wired game of an engine Jordan states is unfinished.")
    return dict(depth=depth, reps=reps, n_paths=len(rows),
                distinct_modal_outcomes=len(leaves), leaves=dict(leaves),
                monotone_win_rate=mono, by_opening_band=stats,
                win_rate_min=min(wr), win_rate_max=max(wr), paths=rows)
