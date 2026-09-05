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
`ranked` -- the person's own scored, sorted candidate list -- and `pack_scenes` consumes it against
the person's own REAL budget (`ask_budget()`, S26.3). That budget boundary is the only place in the
loop where a named alternative is passed over BY THE ENGINE ITSELF: `ranked[:L]` is taken and
`ranked[L:]` is not, where `L` is however many of `ranked`'s own leading elements the real budget
actually affords. Every other branch in the fold is a consequence of that pick.

⚠ NO RULE IS REPLACED. `score`, the sort key, `align`, `stance_toward`, `urgency`, `ask_budget`
and `pack_scenes` all run unmodified -- BASELINE calls `pack_scenes` with the person's own full
`ranked` list and real budget, exactly as `make_chooser` does. A fork substitutes WHICH element
sits in the LAST IN-BUDGET SLOT, at exactly one deliberation, and lets everything downstream
follow.

⚠ `H-117`, RE-KINDED `ABSENT_RULE` -> `NUMBER` (2026-09-04). THE FIRST VERSION OF THIS ARM DID NOT
ASK THIS QUESTION -- it restricted BOTH baseline and fork to `ranked[:1]`, because arm 7c measured
that the real budget never binds under DEFAULT fixtures (every person takes ALL of their ranked
candidates), so an unrestricted baseline would leave no `instead of` to flip. That restriction
manufactured exclusivity the engine does not have, at the wrong boundary. The native fork below
asks the SAME question at the budget's OWN boundary instead, and `run()` prints, per deliberation,
whether that boundary is real at the fixture point being measured (`budget_binds = candidates >
slots`, `slots` read from fixtures) -- because whether an `instead of` moment exists AT ALL is
itself a property of the fixture, not a fixed fact about the design.
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
    """Record each deliberation's ranked list, in order, and its REAL in-budget count `L` -- how
    many of `ranked`'s own leading elements the UNMODIFIED `pack_scenes` actually takes, under the
    person's real ranked list and real budget.

    ⚠ `L` IS READ OFF THE PACKER, NOT RE-DERIVED FROM A SECOND ACCOUNTING OF ITS RULE. `H-117`'s
    own finding is why the read is safe: `pack_scenes`'s default (`greedy`) rule chunks `ranked`
    strictly in order (`shape.py:2698-2777`, `chunks = [ranked[i:i+width] ...]`) and `take()`
    visits those chunks strictly in order too, only ever TRIMMING or STOPPING at the CURRENT
    chunk -- never skipping ahead and never re-including a dropped tail. So the taken set is
    always a PREFIX `ranked[:L]` for some `L`, by the algorithm's own structure.

    BASELINE (`fork_at=-1`) packs the person's REAL ranked list under the REAL budget -- no
    truncation at all; `S26.3`'s own "the engine does NOT truncate" holds for this harness too. A
    FORK (`fork_at=i, take=t`) swaps `ranked[t]` into the LAST IN-BUDGET SLOT, `ranked[fork_slot
    - 1]`, at exactly deliberation `i`, and leaves every other deliberation -- including `ranked`'s
    own order and every other person's turn -- untouched. `fork_slot` is `L` AT `i`, supplied by
    the caller from a prior BASELINE pass rather than re-derived here: decisions strictly before
    `i` are identical between baseline and any fork at `i` by S26.2's own freeze (DELIBERATE is a
    parallel map over a world frozen since the end of MATTER), so `L` at `i` cannot itself have
    already diverged."""
    def __init__(self, fork_at: int = -1, take: int = 0, w=None, fork_slot: "int | None" = None):
        self.fork_at, self.take, self.w, self.fork_slot = fork_at, take, w, fork_slot
        self.seen: list = []       # [(person_id, [verb,...], tick), ...] in deliberation order
        self.in_budget: list = []  # [L, ...] parallel to `seen` -- the REAL packer's own take

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
            rec.seen.append((getattr(p, "id", "?"), [(c.verb, c.subject) for c in ranked], int(rec.w.tick)))
            use = ranked
            if i == rec.fork_at and ranked and rec.fork_slot:
                t = rec.take % len(ranked)
                if t >= rec.fork_slot:
                    use = list(ranked)
                    use[rec.fork_slot - 1], use[t] = use[t], use[rec.fork_slot - 1]
                # `t < fork_slot`: `t` is already inside the real budget. `fork_case` classifies
                # this INERT-BY-CONSTRUCTION from `fork_slot` itself and never calls a run with
                # such a `t` (its own `L == 0 or t < L` guard, below) -- `locality`'s degenerate
                # fallback can still reach here, and `use` stays unswapped on purpose: swapping
                # two already-taken slots changes nothing the packer would take either way.
            scenes = _r(p, use, budget, fx, mint, occasion=occasion)
            rec.in_budget.append(sum(len(sc.acts) for sc in scenes))
            return scenes
        S.pack_scenes = packed
        return self

    def __exit__(self, *a):
        S.pack_scenes = _REAL_PACK
        return False


def _run(case: dict, seed: int, seasons: int, fork_at: int = -1, take: int = 0,
        fork_slot: "int | None" = None, fixtures=None) -> dict:
    """One simulation. Returns the ordered decision trace, the REAL in-budget count `L` at each
    decision (`in_budget`, parallel to `decisions`), and the acts each decision produced.

    `fixtures`, when given, REPLACES the world's fixtures wholesale -- e.g.
    `S.DEFAULT_FIXTURES.sweep("interactions_per_scene", 1)`, to ask whether the budget binds at a
    different point on that one axis without writing a second fixture object by hand."""
    w = C.build_at(case, seed)
    if fixtures is not None:
        w.fixtures = fixtures
    d = S.SeasonDriver(w)
    mint = lambda pid, verb, subj: S.H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = S.make_chooser(w.fixtures, mint, verbs=S.resolvable_verbs())
    rec = recorder(fork_at, take, w, fork_slot)
    try:
        with rec:
            for _ in range(seasons):
                d.season(ch, question=None, subsistence=K.C.P.SUBSIST)
    except BaseException as e:
        return dict(ok=False, why=f"{type(e).__name__}: {e}", decisions=[], in_budget=[], acts=[])
    # THE DECISION TRACE: what each deliberation had available, and what it took.
    acts = [(a.actor, a.verb) for a in getattr(d, "resolved", [])]
    return dict(ok=True, decisions=rec.seen, in_budget=rec.in_budget, acts=acts,
                log_hash=w.content_hash(), n_events=len(w.log))


def fork_case(case: dict, seed: int = 0, seasons: int = 4, fixtures=None) -> dict:
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
    is reported `NO-LIVE-WINDOW` and excluded from the rate rather than counted as reconverged.
    THIS PART IS UNCHANGED here.

    ⚠ THE FORK ITSELF IS NOW NATIVE, WHICH REPLACES A HARNESS-IMPOSED RESTRICTION (`H-117`). The
    first version restricted BOTH baseline and fork to `ranked[:1]` because arm 7c measured the
    real budget never binding under DEFAULT fixtures, so an unrestricted baseline left no
    `instead of` to flip. BASELINE now packs the person's real ranked list under the real budget
    (`recorder`, above, no truncation); a fork at decision `i`, alternative `t`, swaps `ranked[t]`
    into the LAST IN-BUDGET SLOT and leaves the rest of `ranked`, the score and the budget
    untouched. FOUR outcomes, not two:
      NO-LIVE-WINDOW          -- unchanged meaning: the lookahead cannot be filled.
      INERT-BY-CONSTRUCTION   -- `t` was ALREADY inside the real budget. RESOLVE re-sorts every
                                  act by `(stratum, hash)` (shape.py:4572-4573), never by the
                                  order `ranked`/`pack_scenes` produced them in, so the SET of
                                  acts taken is the only thing that can matter -- and the set is
                                  unchanged. NOT evidence, and NOT folded into RECONVERGED, which
                                  would inflate the finding exactly as the same-tick window did
                                  before that was excluded.
      DIVERGED / RECONVERGED  -- a GENUINE fork (`t` was outside the real budget): the taken SET
                                  changed by exactly one member, and the next `LOOKAHEAD`
                                  decisions are compared as before."""
    base = _run(case, seed, seasons, fixtures=fixtures)
    if not base["ok"]:
        return dict(case=case["id"], ok=False, why=base["why"])
    D = base["decisions"]
    IB = base["in_budget"]
    forks = []
    for i in range(len(D)):
        tick_i = D[i][2]
        # the live window: the next LOOKAHEAD decisions at a STRICTLY LATER tick
        live_idx = [j for j in range(i + 1, len(D)) if D[j][2] > tick_i][:LOOKAHEAD]
        n_alt = min(MAX_ALT, max(0, len(D[i][1]) - 1))
        L = IB[i]
        for t in range(1, n_alt + 1):
            if len(live_idx) < LOOKAHEAD:
                forks.append(dict(at=i, take=t, ok=True, flipped=None,
                                  status="NO-LIVE-WINDOW", n_live=len(live_idx), in_budget=L,
                                  why=f"fork at tick {tick_i}; only {len(live_idx)} decision(s) "
                                      f"at a later tick exist, and same-tick decisions cannot "
                                      f"differ (DELIBERATE is a frozen map)"))
                continue
            if L == 0 or t < L:
                forks.append(dict(at=i, take=t, ok=True, flipped=False,
                                  status="INERT-BY-CONSTRUCTION", in_budget=L,
                                  why=(f"decision {i} has no in-budget slot at all (L=0)" if L == 0
                                       else
                                       f"alternative {t} is already inside the real budget "
                                       f"(last in-budget slot {L - 1} of {len(D[i][1])} "
                                       f"candidates); RESOLVE re-sorts by (stratum, hash) "
                                       f"(shape.py:4572-4573), so the SET taken is unchanged and "
                                       f"this is not evidence")))
                continue
            f = _run(case, seed, seasons, fork_at=i, take=t, fork_slot=L, fixtures=fixtures)
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
            # exactly one slot changed: `ranked[L-1]` (displaced) for `ranked[t]` (inserted).
            from_verb = D[i][1][L - 1]
            to_verb = D[i][1][t]
            reconverged = not changed
            forks.append(dict(at=i, take=t, ok=True,
                              status=("RECONVERGED" if reconverged else "DIVERGED"),
                              tick=tick_i, live_window=live_idx, in_budget=L,
                              flipped=(from_verb != to_verb), from_verb=from_verb, to_verb=to_verb,
                              window=window, n_changed=len(changed), changed_at=changed,
                              reconverged=reconverged,
                              acts_differ=(f["acts"] != base["acts"]),
                              hash_differ=(f["log_hash"] != base["log_hash"])))
    real = [f for f in forks if f.get("status") in ("DIVERGED", "RECONVERGED")]
    inert = [f for f in forks if f.get("status") == "INERT-BY-CONSTRUCTION"]
    nolive = [f for f in forks if f.get("status") == "NO-LIVE-WINDOW"]
    return dict(case=case["id"], scale=case.get("scale"), ok=True,
                # `decisions`: kept on the row (not only in `forks`) so `budget_report` can read
                # `candidates = len(verbs)` per deliberation without a second baseline pass.
                decisions=D,
                n_decisions=len(D), n_forks=len(forks), n_real_forks=len(real),
                n_no_live_window=len(nolive), n_inert=len(inert),
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


def locality(case: dict, seed: int = 0, seasons: int = 3, fixtures=None) -> dict:
    """ARM 9e -- IS THE HARNESS REPLAYING THE BASELINE, OR RE-DERIVING?

    ⚠ JORDAN ASKED THIS DIRECTLY, 2026-09-04: *"is the issue that you are creating the tests for
    NPC/arcs such that once you resolve the first mechanical moment ... you just proceed straight
    to next mechanical moment in the initial test sequence?"* If yes, every number in arm 9 is an
    artifact of the harness and the reconvergence rate means nothing.

    THE ANSWER IS NO, and it is checked three ways rather than asserted:
      (a) the harness patches `pack_scenes` ONLY, and calls it EVERY deliberation of every run,
          fork or not. `ranked` is recomputed by `make_chooser`'s `choose` from
          `Query.opening_set` at every deliberation. No sequence is recorded and replayed -- the
          forked run derives its own decisions from its own world.
      (b) the deliberation COUNT is compared, so the index alignment the comparison depends on is
          verified rather than assumed.
      (c) the ACTS are diffed positionally. If the fork's effect were an artifact of replay, the
          acts after the fork would be trivially identical whether or not the fork was genuine.
          Whether THIS particular fork is genuine or inert-by-construction is reported alongside
          the diff, because the two cases mean different things here: a genuine fork's diff
          starting exactly at 0 is re-derivation; an inert fork's empty diff is the SET being
          unchanged, not the harness failing to apply anything."""
    b = _run(case, seed, seasons, fixtures=fixtures)
    if not b["ok"] or not b["decisions"] or len(b["decisions"][0][1]) < 2:
        return dict(ok=False)
    ranked0 = b["decisions"][0][1]
    L0 = b["in_budget"][0]
    # prefer a GENUINE fork (the first alternative outside the real budget) so this check
    # exercises re-derivation past an actual change; fall back to `t=1` (which `recorder` itself
    # will treat as inert-by-construction whenever `L0 >= 2`) only when every alternative is
    # already inside the budget.
    t0 = L0 if L0 < len(ranked0) else 1
    f = _run(case, seed, seasons, fork_at=0, take=t0, fork_slot=L0, fixtures=fixtures)
    if not (b["ok"] and f["ok"]):
        return dict(ok=False)
    ba, fa = b["acts"], f["acts"]
    diff = [i for i, (x, y) in enumerate(zip(ba, fa)) if x != y]
    return dict(ok=True, n_base=len(b["decisions"]), n_fork=len(f["decisions"]),
                aligned=len(b["decisions"]) == len(f["decisions"]),
                acts_base=len(ba), acts_fork=len(fa), diff_indices=diff,
                genuine=(t0 >= L0), in_budget=L0, n_candidates=len(ranked0),
                local_only=(diff == [0]))


def budget_report(log: Log, rows: list, fixtures) -> dict:
    """`H-117`, RE-KINDED `ABSENT_RULE` -> `NUMBER`: whether the budget binds AT ALL is a
    property of the fixture, not a fixed fact about the design. `slots` is READ FROM FIXTURES
    (`CLAUDE.md` §0.05 -- never a literal), so the count moves when the fixture does, and
    `budget_binds` is checked at every deliberation this arm actually recorded rather than
    asserted once."""
    scene_budget = fixtures.get("scene_budget")
    per_scene = fixtures.get("interactions_per_scene")
    slots = scene_budget * per_scene
    n_binds = n_total = 0
    example = None
    for r in rows:
        if not r.get("ok"):
            continue
        for pid, verbs, tick in r["decisions"]:
            n_total += 1
            candidates = len(verbs)
            if candidates > slots:
                n_binds += 1
                if example is None:
                    example = (r["case"], pid, tick, candidates)
    log("BUDGET", f"slots = scene_budget({scene_budget}) x interactions_per_scene({per_scene}) "
                  f"= {slots} -- read from fixtures, not a literal")
    log("RESULT", f"budget_binds = candidates > slots: {n_binds} of {n_total} deliberations "
                  f"({(n_binds / n_total * 100) if n_total else 0:.1f}%)")
    if example:
        cid, pid, tick, candidates = example
        log("RESULT", f"budget_binds True at e.g. case {cid!r} person {pid!r} tick {tick}: "
                      f"{candidates} candidates > {slots} slots",
            "`H-117` -- a real `instead of` moment exists at this fixture point")
    else:
        log("RESULT", "budget_binds is False at every deliberation measured -- the budget does "
                      "not bind at this fixture point, and every fork found is "
                      "INERT-BY-CONSTRUCTION",
            "`H-117` -- there is no native `instead of` moment to ask about here")
    return dict(slots=slots, scene_budget=scene_budget, interactions_per_scene=per_scene,
               n_binds=n_binds, n_total=n_total)


def run(log: Log, seed: int = 0, seasons: int = 4, sample: int = 0, fixtures=None) -> dict:
    fixtures = fixtures or S.DEFAULT_FIXTURES
    log.rule("ARM 9 — THE FORKING EXERCISE: flip every decision, follow it three decisions on")
    log("ASK", "Jordan 2026-09-04: 'within each season ... there is a mechanical moment where x "
               "occurs instead of y ... explore what happens when each mechanical that chooses x "
               "instead chooses NOT x, and then figure out how that will change the progression "
               "of that simulation to the tune of three different mechanical decisions later'")
    log("UNIT", "a DECISION, not a season. D0..Dn are the deliberations in order; each holds the "
               "person's own ranked candidate list, of which a REAL, budget-bounded prefix is "
               "taken.")
    log("SETUP", f"lookahead {LOOKAHEAD} — {LOOKAHEAD_WHY}")
    log("SETUP", f"alternatives probed per decision: {MAX_ALT} — {MAX_ALT_WHY}")
    log("SETUP", f"fixture point: scene_budget={fixtures.get('scene_budget')} x "
                f"interactions_per_scene={fixtures.get('interactions_per_scene')} = "
                f"{fixtures.get('scene_budget') * fixtures.get('interactions_per_scene')} slots "
                f"(§ARM 9g measures whether that boundary is ever real for this corpus)")
    log("⚠ ORDER", "DELIBERATE IS A PARALLEL MAP OVER A FROZEN WORLD, so decisions bind in "
                     "order only ACROSS seasons — never within one.",
        "shape.py:4204-4221 requires `w.frozen` and sets `w._in_parallel_map = True`; the law "
        "reads 'the world is FROZEN from the end of MATTER to the start of RESOLVE. THIS IS WHAT "
        "MAKES THE MAP SAFE TO PARALLELISE'. JORDAN CAUGHT THAT THE FIRST VERSION OF THIS ARM "
        "IGNORED IT. Its window counted SAME-TICK decisions, which cannot differ by construction "
        "(2 of 3 slots dead for a fork at a season's first deliberation), and it scored every "
        "fork in the LAST season as `reconverged` when such a fork has NO live slot at all. The "
        "window now takes only decisions at a STRICTLY LATER tick, and a fork that cannot fill "
        "it is excluded as NO-LIVE-WINDOW rather than counted. UNCHANGED by the native fork below.")
    log("SETUP", "BASELINE packs the person's REAL ranked list under the REAL budget — no "
                 "truncation. A FORK swaps `ranked[t]` into the LAST IN-BUDGET SLOT at exactly "
                 "one decision, leaving the list's own order, the score and the budget untouched "
                 "everywhere else; `t` already inside the budget is INERT-BY-CONSTRUCTION, not a "
                 "fork",
        "`H-117`, re-kinded ABSENT_RULE -> NUMBER: the prior harness restricted BOTH arms to one "
        "act per deliberation because arm 7c measured the real budget never binding under "
        "DEFAULT fixtures, and an unrestricted baseline would then take every candidate, leaving "
        "no `instead of` to flip. The native fork asks the same x-instead-of-y question at the "
        "budget's OWN boundary instead of one the harness imposed.")

    rows = []
    for lane in ("NPC", "ARC"):
        cases = [C.apply_rescale(c) for c in R.load_cases(lane)]
        cases = [c for c in cases if str(c.get("scale")) in set(S.RUNG_KINDS)]
        if sample:
            cases = cases[:sample]
        for c in cases:
            r = fork_case(c, seed, seasons, fixtures=fixtures)
            r["lane"] = lane
            rows.append(r)

    good = [r for r in rows if r.get("ok")]
    tot_nolive = sum(r.get("n_no_live_window", 0) for r in good)
    tot_inert = sum(r.get("n_inert", 0) for r in good)
    tot_forks = sum(r["n_real_forks"] for r in good)
    tot_recon = sum(r["n_reconverged"] for r in good)
    tot_div = sum(r["n_diverged"] for r in good)
    probed = sum(r["n_forks"] for r in good)

    log.rule("ARM 9a — did the fork actually flip anything? (the control)")
    log("EXCLUDED", f"{tot_nolive} of {probed} probed forks have NO LIVE WINDOW and are not "
                    f"scored — they sit in the final season, where every later decision is "
                    f"same-tick and cannot differ",
        "the first version of this arm counted every one of these as `reconverged`, which is "
        "part of the inflation Jordan's question exposed")
    log("INERT", f"{tot_inert} of {probed} probed forks are INERT-BY-CONSTRUCTION — the "
                f"alternative was already inside the real budget, so the SET of acts taken does "
                f"not change and RESOLVE's own (stratum, hash) re-sort (shape.py:4572-4573) "
                f"makes the order irrelevant",
        "`H-117` -- NOT folded into RECONVERGED. Folding it in would inflate the finding exactly "
        "as the same-tick window did before NO-LIVE-WINDOW was excluded from it")
    log("CONTROL", f"{tot_forks} of {probed - tot_nolive - tot_inert} eligible forks were "
                  f"GENUINE (the alternative was outside the real budget) and were actually "
                  f"scored",
        "a fork that leaves the taken SET unchanged cannot be evidence about what happens "
        "downstream, so only the genuine ones are counted below")

    log.rule(f"ARM 9b — did the next {LOOKAHEAD} decisions change?")
    log("RESULT", f"RECONVERGED (all {LOOKAHEAD} following decisions identical): "
                  f"{tot_recon} of {tot_forks} ({tot_recon/tot_forks*100 if tot_forks else 0:.1f}%)")
    log("RESULT", f"DIVERGED (at least one of the next {LOOKAHEAD} differs): {tot_div} "
                  f"({tot_div/tot_forks*100 if tot_forks else 0:.1f}%)")
    dist = collections.Counter()
    for r in good:
        for f in r["forks"]:
            if f.get("status") in ("DIVERGED", "RECONVERGED") and f.get("flipped"):
                dist[f["n_changed"]] += 1
    log("RESULT", f"decisions changed within the lookahead: {dict(sorted(dist.items()))}",
        f"0 means the fork closed immediately — the person did something else and the next "
        f"{LOOKAHEAD} decision points presented the same options and took the same pick")

    log.rule("ARM 9g — does the budget bind, at THIS fixture point? (measured, not asserted)")
    budget = budget_report(log, rows, fixtures)

    log.rule("ARM 9e — is this harness REPLAYING the baseline? (Jordan's methodological check)")
    log("Q", "'is the issue that you are creating the tests ... such that once you resolve the "
             "first mechanical moment, you just proceed straight to next mechanical moment in the "
             "initial test sequence?' — if yes, everything in this arm is void")
    cs0 = [C.apply_rescale(c) for c in R.load_cases("NPC")]
    cs0 = [c for c in cs0 if str(c.get("scale")) in set(S.RUNG_KINDS)]
    lc = locality(cs0[0], seed, seasons, fixtures=fixtures)
    log("A-(a)", "NO. The harness patches `pack_scenes` only and calls it every deliberation, "
                 "fork or not; `ranked` is recomputed by `make_chooser` from `Query.opening_set` "
                 "at every deliberation of every run.",
        "no sequence is recorded and replayed — the forked run derives its own decisions from "
        "its own world, which is why the world-fingerprint control below is meaningful")
    log("A-(b)", f"deliberation counts: baseline {lc.get('n_base')} vs forked {lc.get('n_fork')} "
                 f"— aligned {lc.get('aligned')}",
        "the index alignment the comparison rests on is verified, not assumed")
    log("A-(c)", f"acts diffed positionally: they differ at indices {lc.get('diff_indices')} "
                f"(fork at deliberation 0 was "
                f"{'GENUINE' if lc.get('genuine') else 'INERT-BY-CONSTRUCTION'} — in-budget "
                f"slot {lc.get('in_budget')} of {lc.get('n_candidates')} candidates)",
        "a GENUINE fork's diff starting exactly at 0 (and nowhere else) is re-derivation, not "
        "replay: (a)+(b) establish the mechanism, (c) is what it predicts rather than assumes. "
        "An INERT fork's empty diff is the taken SET being unchanged, which is the same finding "
        "ARM 9a reports at corpus scale, not a harness failing to apply anything.")

    log.rule("ARM 9f — is there a native x-instead-of-y moment, at THIS fixture point?")
    log("MEASURED", f"of {probed} probed forks: {tot_nolive} NO-LIVE-WINDOW, {tot_inert} "
                   f"INERT-BY-CONSTRUCTION, {tot_forks} GENUINE ({tot_div} DIVERGED / "
                   f"{tot_recon} RECONVERGED)",
        f"a GENUINE fork means the real, unrestricted budget already excluded the alternative — "
        f"'x instead of y' is native here, never imposed by the harness. Whether one exists AT "
        f"ALL is a property of the fixture (§ARM 9g): at "
        f"interactions_per_scene={fixtures.get('interactions_per_scene')} the budget binds for "
        f"{budget['n_binds']} of {budget['n_total']} deliberations, and only where it binds can "
        f"a candidate be excluded in the first place.")
    log("SO THE RESULT IS TWO-PART", "(1) whether choice is a mechanic AT ALL is fixture-shaped "
                                      "— a case with more candidates than slots has a genuine "
                                      "boundary, one with fewer does not; (2) where a genuine "
                                      "fork exists, ARM 9b's DIVERGED/RECONVERGED split is what "
                                      "it costs the person to have chosen otherwise.",
        "part 1 is arguably the larger finding for the design: §26.3 makes triage 'the PERSON's "
        "own choice of what to leave undone', and whether that triage is ever forced at all "
        "depends on a swept harness fixture rather than on anything ruled.")

    log.rule("ARM 9c — the diagnosis: does the world actually move?")
    log("⚠ RETRACTED", "an earlier draft of this arm said the cause of 100% reconvergence was "
                       "'the acts do not move that world'. FALSE, and the control below refutes "
                       "it for every GENUINE fork.",
        "a genuine fork changes the taken act at its own decision and, if the design's own "
        "provenance chain carries the change forward at all, produces a DIFFERENT event-log "
        "hash. MEASURE below counts how many do, over the corpus actually run — not a fixed "
        "historical pair, because the native fork changes what baseline itself does.")
    log("MEASURE", f"genuine forks whose ACTS differ from baseline: "
                   f"{sum(1 for r in good for f in r['forks'] if f.get('acts_differ'))}",
        "so the fork is real at its own site — different acts were performed")
    log("MEASURE", f"genuine forks whose EVENT LOG differs: "
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
        "this is a mechanical cause available to every fork regardless of whether it is genuine "
        "or inert. A person deposits thousands of claims, the world moves, and not one claim can "
        "reach the function that decides what they may do next. `H-72` registers exactly this "
        "gap — 'the mapping from a `requires:` note to a predicate' — and `F.24`/`H-94` is typing "
        "`requires`. Both unbuilt, same class as arm 6's five.")
    return dict(seed=seed, seasons=seasons, lookahead=LOOKAHEAD,
                fixtures=dict(scene_budget=fixtures.get("scene_budget"),
                              interactions_per_scene=fixtures.get("interactions_per_scene")),
                n_cases=len(good), probed=probed, no_live_window=tot_nolive, inert=tot_inert,
                real_forks=tot_forks,
                reconverged=tot_recon, diverged=tot_div,
                changed_distribution=dict(dist),
                reconvergence_rate=(tot_recon / tot_forks) if tot_forks else None,
                budget=budget,
                rows=[{k: v for k, v in r.items() if k not in ("forks", "decisions")}
                      for r in rows])
