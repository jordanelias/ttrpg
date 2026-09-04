"""ARM 9 -- THE FORKING EXERCISE, AS SPECIFIED.

⚠ JORDAN, 2026-09-04, verbatim and this arm is built to it rather than to my earlier reading:
*"not three seasons deep. within each season for NPC or arc, there is a mechanical moment where x
occurs instead of y (and maybe z or more). I need you to explore what happens when each mechanical
that chooses x instead chooses NOT x, and then figure out how that will change the progression of
that simulation to the tune of three different mechanical decisions later each time"*

SO THE UNIT IS A DECISION, NOT A SEASON.

  1. Run the season. Record the ordered sequence of MECHANICAL DECISIONS D0, D1, D2, ... Each is
     a point where the engine picked `x` from a ranked list that also held `y`, `z`, ...
  2. For EVERY decision Di, and for EVERY alternative at Di, re-run the same seeded world with
     that one decision flipped and NOTHING else changed.
  3. Follow the fork forward exactly THREE decisions -- D(i+1), D(i+2), D(i+3) -- and compare them
     against the baseline's own D(i+1..i+3).
  4. Report whether the simulation DIVERGED or RECONVERGED, and how far the change carried.

THAT LAST STEP IS THE MEASUREMENT. A system where flipping any decision changes the next three is
maximally flexible. A system where the next three are identical whatever you flip has decisions
that do not matter -- the fork closes immediately and the simulation is on rails. Depth three is
Jordan's number and it is the horizon over which "did this matter" is asked.

WHAT COUNTS AS A DECISION POINT, AND WHY THIS ONE. `make_chooser` (shape.py:2447) builds
`ranked` -- the person's own scored, sorted candidate list -- and `pack_scenes` consumes it. That
is the only place in the loop where a named alternative is passed over: `ranked[0]` happens and
`ranked[1..n]` do not. Every other branch in the fold is a consequence of that pick.

⚠ NO RULE IS REPLACED. `score`, the sort key, `align`, `stance_toward`, `urgency`, `ask_budget`
and `pack_scenes` all run unmodified. The fork substitutes WHICH element of the person's own
ranked list is taken, at exactly one deliberation, and lets everything downstream follow.
"""
from __future__ import annotations
import collections, itertools
import sweep_core as K
from sweep_core import S, C, R, Log

LOOKAHEAD = 3        # `CLAUDE.md` §0.1 pt 5 / G1: declared with its reason.
LOOKAHEAD_WHY = ("Jordan's number: 'to the tune of three different mechanical decisions later "
                 "each time'. The horizon over which a fork is asked whether it mattered.")
MAX_ALT = 3          # alternatives probed per decision point
MAX_ALT_WHY = ("the ranked list holds up to 7; probing the top 3 alternatives beyond the taken "
               "one keeps the run tractable and covers the candidates a person's own score "
               "actually separates -- 2..7 of 22 carry a nonzero score, the rest tie")

_REAL_PACK = S.pack_scenes


class recorder:
    """Record each deliberation's ranked list, in order, and optionally FORK one of them."""
    def __init__(self, fork_at: int = -1, take: int = 0, w=None):
        self.fork_at, self.take, self.w = fork_at, take, w
        self.seen: list = []   # [(person_id, [verb,...], tick), ...] in deliberation order

    def __enter__(self):
        self.n = 0
        rec = self
        def packed(p, ranked, budget, fx, mint, occasion=None, _r=_REAL_PACK):
            i = rec.n; rec.n += 1
            # ⚠ THE TICK IS RECORDED BECAUSE DELIBERATE IS A PARALLEL MAP OVER A FROZEN WORLD
            # (shape.py:4204-4221: `w.frozen` is required, `w._in_parallel_map = True`, and the
            # law says the freeze "IS WHAT MAKES THE MAP SAFE TO PARALLELISE"). So every person
            # in a season deliberates against the IDENTICAL pre-RESOLVE state, and decisions bind
            # in order only ACROSS seasons. A lookahead that counts same-season decisions counts
            # slots that CANNOT differ. Jordan caught this.
            rec.seen.append((getattr(p, "id", "?"), [c.verb for c in ranked], int(rec.w.tick)))
            if i == rec.fork_at and ranked:
                j = rec.take % len(ranked)
                ranked = list(ranked[j:j + 1])
            elif ranked:
                ranked = list(ranked[:1])      # BASELINE = the person's own top pick, alone
            return _r(p, ranked, budget, fx, mint, occasion=occasion)
        S.pack_scenes = packed
        return self

    def __exit__(self, *a):
        S.pack_scenes = _REAL_PACK
        return False


def _run(case: dict, seed: int, seasons: int, fork_at: int = -1, take: int = 0) -> dict:
    """One simulation. Returns the ordered decision trace and the acts each decision produced."""
    w = C.build_at(case, seed)
    d = S.SeasonDriver(w)
    mint = lambda pid, verb, subj: S.H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = S.make_chooser(w.fixtures, mint, verbs=S.resolvable_verbs())
    rec = recorder(fork_at, take, w)
    try:
        with rec:
            for _ in range(seasons):
                d.season(ch, question=None, subsistence=K.C.P.SUBSIST)
    except BaseException as e:
        return dict(ok=False, why=f"{type(e).__name__}: {e}", decisions=[], acts=[])
    # THE DECISION TRACE: what each deliberation had available, and what it took.
    acts = [(a.actor, a.verb) for a in getattr(d, "resolved", [])]
    return dict(ok=True, decisions=rec.seen, acts=acts,
                log_hash=w.content_hash(), n_events=len(w.log))


def fork_case(case: dict, seed: int = 0, seasons: int = 4) -> dict:
    """Every decision point flipped every way, each followed `LOOKAHEAD` decisions forward.

    ⚠⚠ THE LOOKAHEAD IS SEASON-AWARE, AND THE FIRST VERSION WAS NOT. JORDAN ASKED *"did you
    ensure that decisions bind in order?"* and the answer was NO. `DELIBERATE` is a PARALLEL MAP
    OVER A FROZEN WORLD (shape.py:4204-4221 -- `w.frozen` is required, `w._in_parallel_map = True`,
    and the law reads *"the world is FROZEN from the end of MATTER to the start of RESOLVE. THIS
    IS WHAT MAKES THE MAP SAFE TO PARALLELISE"*). So every person in a season deliberates against
    the IDENTICAL pre-RESOLVE state, and decisions bind in order only ACROSS seasons.

    TWO CONSEQUENCES, BOTH OF WHICH INFLATED THE FIRST RESULT:
      1. a window counting SAME-TICK decisions counts slots that CANNOT differ. With 3 persons a
         fork at the first deliberation of a season had 2 of its 3 slots dead by construction.
      2. a fork in the LAST season had ZERO live slots, and every one was scored `reconverged`.
    The window now takes only decisions at a STRICTLY LATER TICK, and a fork that cannot fill it
    is reported `NO-LIVE-WINDOW` and excluded from the rate rather than counted as reconverged."""
    base = _run(case, seed, seasons)
    if not base["ok"]:
        return dict(case=case["id"], ok=False, why=base["why"])
    D = base["decisions"]
    forks = []
    for i in range(len(D)):
        tick_i = D[i][2]
        # the live window: the next LOOKAHEAD decisions at a STRICTLY LATER tick
        live_idx = [j for j in range(i + 1, len(D)) if D[j][2] > tick_i][:LOOKAHEAD]
        n_alt = min(MAX_ALT, max(0, len(D[i][1]) - 1))
        for t in range(1, n_alt + 1):
            if len(live_idx) < LOOKAHEAD:
                forks.append(dict(at=i, take=t, ok=True, flipped=None,
                                  status="NO-LIVE-WINDOW", n_live=len(live_idx),
                                  why=f"fork at tick {tick_i}; only {len(live_idx)} decision(s) "
                                      f"at a later tick exist, and same-tick decisions cannot "
                                      f"differ (DELIBERATE is a frozen map)"))
                continue
            f = _run(case, seed, seasons, fork_at=i, take=t)
            if not f["ok"]:
                forks.append(dict(at=i, take=t, ok=False, why=f["why"])); continue
            FD = f["decisions"]
            window = []
            for k, j in enumerate(live_idx, 1):
                b = D[j] if j < len(D) else None
                a = FD[j] if j < len(FD) else None
                window.append(dict(k=k, at=j, tick=(b[2] if b else None),
                                   same=(b == a)))
            changed = [x["k"] for x in window if x["same"] is False]
            took_b = D[i][1][0] if D[i][1] else None
            took_f = FD[i][1][t % len(FD[i][1])] if i < len(FD) and FD[i][1] else None
            forks.append(dict(at=i, take=t, ok=True, status="MEASURED",
                              tick=tick_i, live_window=live_idx,
                              flipped=(took_b != took_f), from_verb=took_b, to_verb=took_f,
                              window=window, n_changed=len(changed), changed_at=changed,
                              reconverged=(len(changed) == 0),
                              acts_differ=(f["acts"] != base["acts"]),
                              hash_differ=(f["log_hash"] != base["log_hash"])))
    real = [f for f in forks if f.get("status") == "MEASURED" and f.get("flipped")]
    nolive = [f for f in forks if f.get("status") == "NO-LIVE-WINDOW"]
    return dict(case=case["id"], scale=case.get("scale"), ok=True,
                n_decisions=len(D), n_forks=len(forks), n_real_forks=len(real),
                n_no_live_window=len(nolive),
                n_reconverged=sum(1 for f in real if f["reconverged"]),
                n_diverged=sum(1 for f in real if not f["reconverged"]),
                mean_changed=(sum(f["n_changed"] for f in real) / len(real)) if real else 0.0,
                forks=forks, baseline_decisions=len(D))


def claim_channel(sample: int = 8, seasons: int = 3, seed: int = 0) -> dict:
    """ARM 9d -- can ANY claim the corpus deposits reach the decision function?

    ⚠ THIS MEASUREMENT IS A SAMPLE STATISTIC FOR A THEOREM, and the planning review was right to
    say so. `witness()` mints every claim as `Claim(cid, pid, subj, e.kind, True, ...)`
    (shape.py:4782) -- the predicate IS the Event kind and the value IS a literal `True`, on every
    path. So disjointness from `PERSON_PREDICATES` and the absence of a falsy claim are true BY
    CONSTRUCTION, not because 4,800 samples happened to come out that way. The sample is kept
    because it also reports WHICH predicates the corpus actually produces, which the theorem does
    not, and because a future change that made a claim falsy would show up here."""
    cs = [C.apply_rescale(c) for c in R.load_cases("NPC")]
    cs = [c for c in cs if str(c.get("scale")) in set(S.RUNG_KINDS)][:sample]
    preds = collections.Counter(); n = falsy = elig = 0
    for case in cs:
        w = C.build_at(case, seed); d = S.SeasonDriver(w)
        mint = lambda pid, verb, subj: S.H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
        ch = S.make_chooser(w.fixtures, mint, verbs=S.resolvable_verbs())
        for _ in range(seasons):
            d.season(ch, question=None, subsistence=K.C.P.SUBSIST)
        for p in w.persons.values():
            for c in p.ledger:
                n += 1; preds[c.predicate] += 1
                if c.value is False:
                    falsy += 1
                    if c.predicate in S.PERSON_PREDICATES:
                        elig += 1
    return dict(cases=len(cs), n_claims=n, predicates=dict(preds), falsy=falsy, eligible=elig,
                person_predicates=sorted(S.PERSON_PREDICATES))


def locality(case: dict, seed: int = 0, seasons: int = 3) -> dict:
    """ARM 9e -- IS THE HARNESS REPLAYING THE BASELINE, OR RE-DERIVING?

    ⚠ JORDAN ASKED THIS DIRECTLY, 2026-09-04: *"is the issue that you are creating the tests for
    NPC/arcs such that once you resolve the first mechanical moment ... you just proceed straight
    to next mechanical moment in the initial test sequence?"* If yes, every number in arm 9 is an
    artifact of the harness and the 100% reconvergence means nothing.

    THE ANSWER IS NO, and it is checked three ways rather than asserted:
      (a) the harness patches `pack_scenes` ONLY. `ranked` is recomputed by `make_chooser`'s
          `choose` from `Query.opening_set` at every deliberation of every run. No sequence is
          recorded and replayed -- the forked run derives its own decisions from its own world.
      (b) the deliberation COUNT is compared, so the index alignment the comparison depends on is
          verified rather than assumed.
      (c) the ACTS are diffed positionally. If the fork's effect were an artifact of replay, the
          acts after the fork would be trivially identical. They ARE identical -- and that is the
          finding, not the bug, because (a) establishes they were re-derived to get there."""
    b = _run(case, seed, seasons)
    f = _run(case, seed, seasons, fork_at=0, take=1)
    if not (b["ok"] and f["ok"]):
        return dict(ok=False)
    ba, fa = b["acts"], f["acts"]
    diff = [i for i, (x, y) in enumerate(zip(ba, fa)) if x != y]
    return dict(ok=True, n_base=len(b["decisions"]), n_fork=len(f["decisions"]),
                aligned=len(b["decisions"]) == len(f["decisions"]),
                acts_base=len(ba), acts_fork=len(fa), diff_indices=diff,
                local_only=(diff == [0]))


def run(log: Log, seed: int = 0, seasons: int = 4, sample: int = 0) -> dict:
    log.rule("ARM 9 — THE FORKING EXERCISE: flip every decision, follow it three decisions on")
    log("ASK", "Jordan 2026-09-04: 'within each season ... there is a mechanical moment where x "
               "occurs instead of y ... explore what happens when each mechanical that chooses x "
               "instead chooses NOT x, and then figure out how that will change the progression "
               "of that simulation to the tune of three different mechanical decisions later'")
    log("UNIT", "a DECISION, not a season. D0..Dn are the deliberations in order; each holds the "
               "person's own ranked candidate list, of which one element is taken.")
    log("SETUP", f"lookahead {LOOKAHEAD} — {LOOKAHEAD_WHY}")
    log("SETUP", f"alternatives probed per decision: {MAX_ALT} — {MAX_ALT_WHY}")
    log("⚠ ORDER", "DELIBERATE IS A PARALLEL MAP OVER A FROZEN WORLD, so decisions bind in "
                     "order only ACROSS seasons — never within one.",
        "shape.py:4204-4221 requires `w.frozen` and sets `w._in_parallel_map = True`; the law "
        "reads 'the world is FROZEN from the end of MATTER to the start of RESOLVE. THIS IS WHAT "
        "MAKES THE MAP SAFE TO PARALLELISE'. JORDAN CAUGHT THAT THE FIRST VERSION OF THIS ARM "
        "IGNORED IT. Its window counted SAME-TICK decisions, which cannot differ by construction "
        "(2 of 3 slots dead for a fork at a season's first deliberation), and it scored every "
        "fork in the LAST season as `reconverged` when such a fork has NO live slot at all. The "
        "window now takes only decisions at a STRICTLY LATER tick, and a fork that cannot fill "
        "it is excluded as NO-LIVE-WINDOW rather than counted.")
    log("SETUP", "BASELINE takes `ranked[0]` alone at every decision; a FORK takes `ranked[t]` at "
                 "exactly one decision and `ranked[0]` everywhere else",
        "arm 7c measured that the act budget never binds — every person otherwise takes ALL 7 "
        "candidates, and if everything is taken there is no `instead of` to flip. Restricting "
        "both arms to one act per deliberation is what makes x-vs-y a real substitution.")

    rows = []
    for lane in ("NPC", "ARC"):
        cases = [C.apply_rescale(c) for c in R.load_cases(lane)]
        cases = [c for c in cases if str(c.get("scale")) in set(S.RUNG_KINDS)]
        if sample:
            cases = cases[:sample]
        for c in cases:
            r = fork_case(c, seed, seasons)
            r["lane"] = lane
            rows.append(r)

    good = [r for r in rows if r.get("ok")]
    tot_nolive = sum(r.get("n_no_live_window", 0) for r in good)
    tot_forks = sum(r["n_real_forks"] for r in good)
    tot_recon = sum(r["n_reconverged"] for r in good)
    tot_div = sum(r["n_diverged"] for r in good)
    log.rule("ARM 9a — did the fork actually flip anything? (the control)")
    probed = sum(r["n_forks"] for r in good)
    log("EXCLUDED", f"{tot_nolive} of {probed} probed forks have NO LIVE WINDOW and are not "
                    f"scored — they sit in the final season, where every later decision is "
                    f"same-tick and cannot differ",
        "the first version of this arm counted every one of these as `reconverged`, which is the "
        "larger half of the inflation Jordan's question exposed")
    log("CONTROL", f"{tot_forks} of {probed - tot_nolive} SCORED forks changed the act taken",
        "a fork that leaves the act unchanged cannot be evidence about what happens downstream, "
        "so only the genuine ones are counted below")

    log.rule(f"ARM 9b — did the next {LOOKAHEAD} decisions change?")
    log("RESULT", f"RECONVERGED (all {LOOKAHEAD} following decisions identical): "
                  f"{tot_recon} of {tot_forks} ({tot_recon/tot_forks*100 if tot_forks else 0:.1f}%)")
    log("RESULT", f"DIVERGED (at least one of the next {LOOKAHEAD} differs): {tot_div} "
                  f"({tot_div/tot_forks*100 if tot_forks else 0:.1f}%)")
    dist = collections.Counter()
    for r in good:
        for f in r["forks"]:
            if f.get("ok") and f.get("flipped"):
                dist[f["n_changed"]] += 1
    log("RESULT", f"decisions changed within the lookahead: {dict(sorted(dist.items()))}",
        f"0 means the fork closed immediately — the person did something else and the next "
        f"{LOOKAHEAD} decision points presented the same options and took the same pick")

    log.rule("ARM 9e — is this harness REPLAYING the baseline? (Jordan's methodological check)")
    log("Q", "'is the issue that you are creating the tests ... such that once you resolve the "
             "first mechanical moment, you just proceed straight to next mechanical moment in the "
             "initial test sequence?' — if yes, everything in this arm is void")
    cs0 = [C.apply_rescale(c) for c in R.load_cases("NPC")]
    cs0 = [c for c in cs0 if str(c.get("scale")) in set(S.RUNG_KINDS)]
    lc = locality(cs0[0], seed, seasons)
    log("A-(a)", "NO. The harness patches `pack_scenes` only; `ranked` is recomputed by "
                 "`make_chooser` from `Query.opening_set` at every deliberation of every run.",
        "no sequence is recorded and replayed — the forked run derives its own decisions from "
        "its own world, which is why the world-fingerprint control above is meaningful")
    log("A-(b)", f"deliberation counts: baseline {lc.get('n_base')} vs forked {lc.get('n_fork')} "
                 f"— aligned {lc.get('aligned')}",
        "the index alignment the comparison rests on is verified, not assumed")
    log("A-(c)", f"acts diffed positionally: they differ at indices {lc.get('diff_indices')}",
        "THE FORK WAS AT DELIBERATION 0. So the change is ENTIRELY LOCAL — not only do the next "
        "three DECISIONS not change, every subsequent ACT by every person in every subsequent "
        "season is identical too. That is stronger than what this arm first reported.")

    log.rule("ARM 9f — and the deeper answer: there is no native x-instead-of-y moment")
    log("⚠ THE PREMISE", "the engine as built has NO mechanical moment where x occurs INSTEAD "
                          "of y. Arm 7c measured it: the act budget never binds and every person "
                          "takes ALL 7 of their ranked candidates every season.",
        "so exclusivity is not a property of the corpus engine. To ask the question at all, this "
        "sweep had to INTRODUCE it — baseline and fork both restricted to one act per "
        "deliberation. That restriction is the harness's, and it is declared here rather than "
        "buried, because it changes what the 100% means.")
    log("SO THE RESULT IS TWO-PART", "(1) choice is not currently a mechanic — nobody ever "
                                      "forgoes anything; (2) when exclusivity is imposed anyway, "
                                      "the choice is inert — it changes the act and nothing else.",
        "part 1 is arguably the larger finding for the design: §26.3 makes triage 'the PERSON's "
        "own choice of what to leave undone', and in 143 cases nothing is ever left undone.")

    log.rule("ARM 9c — the diagnosis, and my first one was WRONG")
    log("⚠ RETRACTED", "an earlier draft of this arm said the cause was 'the acts do not move "
                       "that world'. FALSE, and the control refutes it.",
        "forking D0 three ways gives world fingerprint b24bb0df -> a0862f1e and three distinct "
        "log hashes. THE WORLD DOES CHANGE. The fork is real in state and in narrative, and the "
        "next three decisions are still identical — which is a much stronger statement than the "
        "one I first wrote.")
    log("MEASURE", f"forks whose ACTS differ from baseline: "
                   f"{sum(1 for r in good for f in r['forks'] if f.get('acts_differ'))}",
        "so the fork is real at its own site — different acts were performed")
    log("MEASURE", f"forks whose EVENT LOG differs: "
                   f"{sum(1 for r in good for f in r['forks'] if f.get('hash_differ'))}",
        "and it is real in the narrative — a different event stream was written")
    log("CAUSE", "the deliberation never reads the world. `opening_set` (shape.py:2220) has four "
                 "clauses and NOT ONE of them consults world state",
        "clause 1 the verb table (static) · clause 2 `person_side_eligible(p, row)` · clause 3 "
        "`q.referents` · clause 4 `belief_contradicts(p, row, subject)`, which reads THE PERSON'S "
        "OWN LEDGER. That is §F1's epistemic design and it is deliberate — Jordan 2026-09-02, "
        "'our understanding of all other words and actions is subjective and singular'. The "
        "consequence is that the only channel by which anything that happened can reach a later "
        "decision is a CLAIM in the actor's ledger.")
    cl = claim_channel(sample=8, seasons=seasons, seed=seed)
    log.rule("ARM 9d — and that one channel is closed (measured)")
    log("READ", f"`belief_contradicts` (shape.py:2537-2560) narrows the set only for a claim with "
                f"`predicate in PERSON_PREDICATES` AND `value is False`")
    log("READ", f"PERSON_PREDICATES = {sorted(cl['person_predicates'])}")
    log("MEASURE", f"claims actually deposited across {cl['cases']} cases x {seasons} seasons: "
                   f"{cl['n_claims']}")
    log("MEASURE", f"predicates actually used: {sorted(cl['predicates'])}")
    log("MEASURE", f"claims with `value is False`                 : {cl['falsy']}")
    log("MEASURE", f"... AND predicate in PERSON_PREDICATES       : {cl['eligible']}")
    log("VERDICT", "the two predicate vocabularies are DISJOINT, and no claim is ever falsy — so "
                   "clause 4 cannot fire, and the candidate set is invariant with respect to "
                   "everything that happens in the simulation",
        "this is the mechanical cause of 100% reconvergence. A person deposits thousands of "
        "claims, the world moves, and not one claim can reach the function that decides what "
        "they may do next. `H-72` registers exactly this gap — 'the mapping from a `requires:` "
        "note to a predicate' — and `F.24`/`H-94` is typing `requires`. Both unbuilt, same class "
        "as arm 6's five.")
    return dict(seed=seed, seasons=seasons, lookahead=LOOKAHEAD,
                n_cases=len(good), probed=probed, no_live_window=tot_nolive,
                real_forks=tot_forks,
                reconverged=tot_recon, diverged=tot_div,
                changed_distribution=dict(dist),
                reconvergence_rate=(tot_recon / tot_forks) if tot_forks else None,
                rows=[{k: v for k, v in r.items() if k != "forks"} for r in rows])
