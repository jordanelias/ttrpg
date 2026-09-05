"""W-D -- THE ACCEPTANCE RUN. Did `W-B` change the forking result?

⚠ THIS FILE BUILDS NO PROBE. `arm9_forking.py` IS THE INSTRUMENT AND IT IS IMPORTED UNMODIFIED.
Everything here is (a) a fixture/arm loop over `A9.fork_case`, (b) the two controls the result is
worthless without, and (c) forensics on whatever diverges. A re-implemented probe measuring a
different thing is the confound that would waste the item, so `fork_case` -- which owns the
strictly-later-tick window, the NO-LIVE-WINDOW exclusion and the INERT-BY-CONSTRUCTION split -- is
called, never copied.

WHAT `W-D` ASKS. The forking exercise flipped every mechanical decision in the ARC/NPC corpus and
followed three decisions on: 100% reconvergence. Its diagnosis (arm 9c/9d) was that
`Query.opening_set` never consults world state, so the ONLY channel from what happened to what is
next decided is a claim in the actor's own ledger -- and `belief_contradicts` could read no claim
the corpus deposited. `W-B` opened that channel (`Event.observed`, deposited at WITNESS under
`observation_deposit_mode`). Does reconvergence now fall below 100%?

THE ACCEPTANCE CRITERION: reconvergence STRICTLY BELOW 100% at the shipped default (`actor`), with
the control (`none`) at 100%. A 100% reading at every arm is a legitimate result and is reported
as one -- no fixture, window or scoring rule is adjusted to produce divergence (`CLAUDE.md` §0.1
point 4).

⚠ THE FIXTURE POINT IS NOT A FREE PARAMETER AND IT WAS FIXED BEFORE ANY RESULT WAS SEEN.
`H-117` measured that at `DEFAULT_FIXTURES` (scene_budget 5 x interactions_per_scene 3 = 15 slots)
the act budget NEVER BINDS -- every person takes ALL of their ranked candidates -- so under the
native fork every probe is INERT-BY-CONSTRUCTION and there is NO `x instead of y` moment to flip.
The question is unaskable there. A genuine fork needs an alternative OUTSIDE the real budget and
within `A9.MAX_ALT` (3) of the taken one, i.e. a deliberation whose in-budget count is `L <= 3`.

⚠⚠ **AND THE FIRST WRITING OF THIS PARAGRAPH SAID `exactly ONE cell gives L <= 3: 2 x 1`, WHICH
IS FALSE. TWO CELLS QUALIFY, AND THE ONE THAT WAS NOT RUN IS THE SMALLER INTERVENTION.** Found by
an independent read-only critic, 2026-09-04. The error is one substitution with two consequences:

  * **`L` IS THE PACKER'S OWN TAKE, NOT THE SLOT PRODUCT.** `recorder.in_budget` records what
    `pack_scenes` returned; the argument above used `scene_budget x interactions_per_scene` as a
    proxy for it. `take()` charges an extended scene `extended_scene_cost` (2) and takes a whole
    chunk whenever `ext <= left`, so at **2 x 3** the first chunk of three candidates is taken
    ENTIRE for a cost of 2 and **L = 3, not 6** -- inside `MAX_ALT`, so that cell is askable too.
  * **`L` IS PER DELIBERATION, NOT PER CELL.** MEASURED over the corpus (`wd_cells.py`): at 2 x 1
    `L` is `{2: 715, 3: 264, 4: 89}` and at 2 x 3 it is `{3: 842, 4: 164, 6: 62}`. So `L <= 3` is
    a property of a DELIBERATION, and a cell is askable when ANY of its deliberations has one.

MEASURED over all nine cells of the cross, 89 worlds, seed 0 (`runs/wd_cells.json`): **2 of 9 are
askable -- 2 x 1 (1,467 genuine forks) and 2 x 3 (733). The other seven yield 0.** `2 x 3` is
`scene_budget=2` with `interactions_per_scene` LEFT AT ITS DEFAULT -- **ONE** declared-arm change
against 2 x 1's **two** -- so on this file's own criterion (minimum departure from the shipped
fixture at which the question is askable) 2 x 3 was the better acceptance point and it was never
run. It is run now and reported beside 2 x 1; see `wd_collect.py` W-D.2b. Both values in both
cells are arms of existing register rows and none is invented here, and no cell was selected on
its answer -- but "forced by `MAX_ALT`" was the wrong word for it, and this is the right one:
`MAX_ALT` narrows the cross to two, and the item ran the more expensive of the two.

ALL THREE fixture points -- 15 slots, 2 slots, 6 slots -- are run and all three are reported.

⚠ HOW TO RUN IT. `main()` below runs every arm in ONE process and DOES NOT FINISH: two attempts
were killed silently at ~18 minutes with no traceback and no output. The live path is
`wd_chunk.py <mode> <default|narrow|2x3> <a> <b>` (four slices per arm) followed by
`wd_collect.py`, which concatenates the chunks and runs the controls and the forensics. `main()`
is kept because it is the same calls in the same order and reading it is how you check that the
chunked path is not a different experiment. **DO NOT CITE `main()` AS A REPRODUCTION COMMAND** --
it is dead code, and a test docstring did cite it until 2026-09-04.

⚠ THE CAUSE OF THE SILENT KILL IS NOW MEASURED RATHER THAN UNKNOWN, which matters because "a
process died and we split the work" is the kind of unexplained event that hides a real defect.
`trace_log.TRACE` is a MODULE-LEVEL SINGLETON whose `rows` list nothing in `arm9_forking` or any
`wd_*.py` ever resets, and `Trace._row` appends on every step, barrier, decision, write, act,
event, claim and query. MEASURED 2026-09-04 over six cases, arm A untouched vs arm B clearing
`TRACE.rows` per case:

    arm A  case 1  rows   222,119  peak RSS 121 MB      arm B  case 1  rows 222,119
    arm A  case 6  rows 1,324,298  peak RSS 604 MB      arm B  case 6  rows 219,320

Growth is strictly linear at ~221,000 rows and ~97 MB per case, and clearing holds it flat at no
time cost. One corpus arm is 89 cases (~19.6M rows, ~8.6 GB extrapolated) and `main()` runs SIX
of them in one process, which is a sufficient cause for a SIGKILL with no traceback. **The values
are unaffected and the scheduling-split claim upholds**: nothing reads `TRACE.rows` mid-run,
`Fixtures.sweep` returns a copy, the `build_at` spy keeps a one-element buffer, and
`wd_collect.collect` checks that each arm covers all 89 case slots exactly once. The clear is NOT
applied to `sweep_arm` here -- changing the memory behaviour of the runner that produced the
committed numbers needs its own control -- but it IS applied in `wd_cells.py` and `wd_extra.py`,
where the re-run reproducing the committed figures is that control. Diagnosed by an independent
read-only critic and then measured, 2026-09-04.
"""
from __future__ import annotations
import collections, json, sys, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import sweep_core as K
from sweep_core import S, C, R, Log
import arm9_forking as A9

SEED = 0
SEASONS = 4          # arm 9's own published run: `runs/arm9.json` records seasons=4, seed=0.
ARMS = ("none", "actor", "total")
OUT = Path(__file__).parent / "runs"

# ⚠ CAPTURE THE WORLD WITHOUT TOUCHING THE PROBE. `A9._run` builds through `C.build_at` and keeps
# the world local; the forensics below need its log and its persons. Wrapping the builder is the
# only edit-free way in, and it is a pure side-channel: the returned object is the real one.
_REAL_BUILD = C.build_at
_WORLDS: list = []


def _build_spy(case, seed):
    w = _REAL_BUILD(case, seed)
    # ⚠ KEEP ONLY THE LAST. The first writing of this appended, and a corpus sweep builds
    # thousands of worlds each holding a full event log -- the process was killed before it
    # printed anything. The forensics needs the world from the run that just finished and no
    # other, so a one-element buffer is the whole requirement.
    _WORLDS[:] = [w]
    return w


C.build_at = _build_spy


FIXTURE_CELLS = {
    # key        (scene_budget, interactions_per_scene)  slots  what it is
    "default":   ((5, 3),  15, "`DEFAULT_FIXTURES` — the shipped point. 0 genuine forks."),
    "narrow":    ((2, 1),   2, "`H-10` arm 2 x `H-76` arm 1. TWO declared-arm changes."),
    "2x3":       ((2, 3),   6, "`H-10` arm 2, `interactions_per_scene` LEFT AT ITS DEFAULT — ONE "
                               "declared-arm change, so it is the SMALLER intervention of the two "
                               "cells at which the question is askable."),
}


def fixtures_for(mode: str, slots: str) -> "S.Fixtures":
    """⚠ `narrow` IS `2x1` UNDER ITS OLD NAME AND IS KEPT SPELLED THAT WAY ON PURPOSE. The
    committed `H-122` reproduce line, the shipped `runs/wd_chunk_narrow_*.json` artifacts and two
    test docstrings all name it; renaming it would orphan them for no gain (`CLAUDE.md` §4's
    no-retrofit posture). New cells are named by the cell — `2x3` reads cold as what it is."""
    fx = S.DEFAULT_FIXTURES
    if slots == "narrow":
        fx = fx.sweep("scene_budget", 2).sweep("interactions_per_scene", 1)
    elif slots == "2x3":
        # ONE sweep, not two: `interactions_per_scene` already defaults to 3.
        fx = fx.sweep("scene_budget", 2)
    elif slots != "default":
        raise KeyError(f"unknown fixture cell {slots!r}; known: {sorted(FIXTURE_CELLS)}")
    return fx.sweep("observation_deposit_mode", mode)


def runnable(lane: str) -> list:
    """⚠ `apply_rescale` FIRST -- confound 4. Filtering the raw `scale:` gives 86 worlds where
    `corpus_run` runs 89, and both bases are legitimate. `A9.run` applies the rescale, so this
    matches the instrument being reused: THE 89 BASIS, stated at every figure below."""
    cs = [C.apply_rescale(c) for c in R.load_cases(lane)]
    return [c for c in cs if str(c.get("scale")) in set(S.RUNG_KINDS)]


CASES = [(lane, c) for lane in ("NPC", "ARC") for c in runnable(lane)]


def sweep_arm(mode: str, slots: str, cases=None, seasons: int = SEASONS) -> dict:
    """One (deposit mode x fixture point) cell, over the corpus. `A9.fork_case` unmodified."""
    fx = fixtures_for(mode, slots)
    rows = []
    t0 = time.time()
    for lane, c in (cases if cases is not None else CASES):
        r = A9.fork_case(c, SEED, seasons, fixtures=fx)
        r["lane"] = lane
        rows.append(r)
    good = [r for r in rows if r.get("ok")]
    bad = [r for r in rows if not r.get("ok")]

    # §0.1 pt 2 -- ASSERT THAT IT ASSERTED, AND REPORT THE DENOMINATOR BEFORE THE RATIO.
    # (a) every scored fork's live window is STRICTLY LATER-TICK (confound 1), checked rather
    #     than trusted, with the count of windows actually inspected.
    windows = same_tick = 0
    fork_rows_failed = 0
    for r in good:
        by_idx = {i: d for i, d in enumerate(r["decisions"])}
        for f in r["forks"]:
            if not f.get("ok"):
                fork_rows_failed += 1
                continue
            if f.get("status") not in ("DIVERGED", "RECONVERGED"):
                continue
            ti = by_idx[f["at"]][2]
            for j in f["live_window"]:
                windows += 1
                if by_idx[j][2] <= ti:
                    same_tick += 1
    real = [f for r in good for f in r["forks"]
            if f.get("status") in ("DIVERGED", "RECONVERGED")]
    div = [f for f in real if not f["reconverged"]]
    return dict(
        mode=mode, slots=slots, seconds=round(time.time() - t0, 1),
        n_cases_attempted=len(rows), n_cases_ok=len(good), n_cases_failed=len(bad),
        failures=[(r.get("case"), r.get("why")) for r in bad][:10],
        fork_rows_failed=fork_rows_failed,
        probed=sum(r["n_forks"] for r in good),
        no_live_window=sum(r["n_no_live_window"] for r in good),
        inert=sum(r["n_inert"] for r in good),
        genuine=len(real), reconverged=len(real) - len(div), diverged=len(div),
        reconvergence_rate=((len(real) - len(div)) / len(real)) if real else None,
        window_slots_checked=windows, window_slots_same_tick=same_tick,
        acts_differ=sum(1 for f in real if f.get("acts_differ")),
        hash_differ=sum(1 for f in real if f.get("hash_differ")),
        stream_only=sum(1 for f in real
                        if (f.get("acts_differ") or f.get("hash_differ")) and f["reconverged"]),
        changed_distribution=dict(collections.Counter(f["n_changed"] for f in real)),
        divergences=[dict(case=r["case"], lane=r["lane"], at=f["at"], take=f["take"],
                          tick=f["tick"], person=r["decisions"][f["at"]][0],
                          from_verb=f["from_verb"], to_verb=f["to_verb"],
                          in_budget=f["in_budget"], changed_at=f["changed_at"],
                          live_window=f["live_window"],
                          changed_idx=[w["at"] for w in f["window"] if w["same"] is False])
                     for r in good for f in r["forks"]
                     if f.get("status") == "DIVERGED"],
        rows=[{k: v for k, v in r.items() if k not in ("forks", "decisions")} for r in rows],
    )


# ---------------------------------------------------------------------------------------------
# FORENSICS -- for a fork that diverged: WHICH claim carried the change, and was it TRUE WHEN
# RECORDED? `W-B`'s whole retraction was that a self-refuting belief produced 95% of its published
# effect, so a divergence driven by a belief that was false at deposit is a DEFECT, not a result.
# ---------------------------------------------------------------------------------------------
_REAL_BC = S.belief_contradicts
_REAL_WITNESS = S.SeasonDriver.witness


def _instrumented(fn):
    """Run `fn()` with two spies installed:
       drops[]    -- every §F1 clause-4 refusal, with the Observations `LedgerReader` returned
       deposits[] -- every observation-claim, re-read against `WorldReader` AT THE BARRIER THAT
                     STORED IT. That comparison is the general form of the check that caught
                     `claim.held`: a deposit whose value the world does not agree with at the
                     moment of recording is FALSE WHEN RECORDED."""
    drops: list = []
    deps: list = []

    def bc(p, row, subject, operands):
        res = _REAL_BC(p, row, subject, operands)
        if res:
            v = S.evaluate(row.requires_typed, S.LedgerReader(p.ledger),
                           S.binding_of(p.id, operands))
            obs = [(o.subject, o.predicate, o.value) for o in v.observed]
            carrier = None
            for (osub, opred, oval) in obs:
                best = None
                for c in p.ledger:
                    if c.subject == osub and c.predicate == opred:
                        if best is None or (c.when, c.confidence) > (best.when, best.confidence):
                            best = c
                if best is not None:
                    carrier = dict(cid=best.id, subject=best.subject, predicate=best.predicate,
                                   value=best.value, when=best.when, source=best.source,
                                   confidence=best.confidence)
                    break
            drops.append(dict(pid=p.id, verb=row.verb, subject=subject,
                              operands={k: v2 for k, v2 in (operands or {}).items()},
                              observed=obs, carrier=carrier))
        return res

    def witness(self, events):
        before = {pid: {c.id for c in pp.ledger} for pid, pp in self.w.persons.items()}
        out = _REAL_WITNESS(self, events)
        for pid, pp in self.w.persons.items():
            for c in pp.ledger:
                if c.id in before.get(pid, ()):
                    continue
                # ⚠ THE CHECK IS ONLY MEANINGFUL WHERE THE READER HAS A BRANCH. A claim whose
                # predicate is an EVENT KIND (`yield.taken`, `stores.changed`) is the pre-`W-B`
                # deposit: `WorldReader` dispatches on `REQUIRES_STEMS` and returns UNKNOWN for
                # anything else, so comparing it to the stored `True` would score 1,412 of 1,422
                # deposits "false when recorded" and mean nothing. `in_grammar` splits them, and
                # the true-when-recorded verdict is reported over the in-grammar subset ONLY --
                # which is exactly the population §F1 clause 4 can read, and the population
                # `claim.held` was found in.
                stem = str(c.predicate).partition(":")[0]
                in_grammar = stem in S.REQUIRES_STEMS
                world_now = (S.WorldReader(self.w, pid).read(c.subject, c.predicate)
                             if in_grammar else None)
                deps.append(dict(tick=self.w.tick, holder=pid, cid=c.id, subject=c.subject,
                                 predicate=c.predicate, value=c.value, in_grammar=in_grammar,
                                 world_at_deposit=world_now,
                                 true_when_recorded=(None if not in_grammar
                                                     else world_now == c.value)))
        return out

    S.belief_contradicts = bc
    S.SeasonDriver.witness = witness
    try:
        res = fn()
    finally:
        S.belief_contradicts = _REAL_BC
        S.SeasonDriver.witness = _REAL_WITNESS
    return res, drops, deps


def forensics(case: dict, mode: str, slots: str, at: int, take: int, in_budget: int,
              seasons: int = SEASONS) -> dict:
    """Re-run BASELINE and the one FORK with the spies on, and diff. Same `A9._run`, same seed,
    same fixtures -- the spies are read-only wrappers, so the runs are the runs."""
    fx = fixtures_for(mode, slots)
    (b, bd, bdep) = _instrumented(lambda: A9._run(case, SEED, seasons, fixtures=fx))
    wb = _WORLDS[-1]
    (f, fd, fdep) = _instrumented(
        lambda: A9._run(case, SEED, seasons, fork_at=at, take=take, fork_slot=in_budget,
                        fixtures=fx))
    wf = _WORLDS[-1]

    def key(d):
        return (d["pid"], d["verb"], d["subject"],
                (d["carrier"] or {}).get("subject"), (d["carrier"] or {}).get("predicate"),
                (d["carrier"] or {}).get("value"), (d["carrier"] or {}).get("when"))
    bk = collections.Counter(key(d) for d in bd)
    fk = collections.Counter(key(d) for d in fd)
    only_fork = [d for d in fd if fk[key(d)] > bk[key(d)]]
    only_base = [d for d in bd if bk[key(d)] > fk[key(d)]]
    # de-duplicate on the key so the report names distinct drops, not repeated deliberations
    def uniq(ds):
        seen, out = set(), []
        for d in ds:
            if key(d) in seen:
                continue
            seen.add(key(d)); out.append(d)
        return out

    def deposit_of(w, cid):
        """The Event that deposited this claim: `w.write(... emits='claim.deposited',
        subject=<claim id>, causes=[<event id>])`, then that Event's own kind/subject."""
        for e in w.log:
            if e.kind == "claim.deposited" and e.subject == cid:
                src = e.causes[0] if e.causes else None
                for e2 in w.log:
                    if e2.id == src:
                        return dict(deposit_event=e.id, by_event=e2.id, by_kind=e2.kind,
                                    by_subject=e2.subject, by_actor=getattr(e2, "subject", None))
                return dict(deposit_event=e.id, by_event=src, by_kind=None, by_subject=None)
        return dict(deposit_event=None)

    def annotate(ds, w, deps):
        by_cid = {d["cid"]: d for d in deps}
        out = []
        for d in ds:
            c = d.get("carrier")
            if c:
                d = dict(d)
                d["provenance"] = deposit_of(w, c["cid"])
                rec = by_cid.get(c["cid"])
                d["true_when_recorded"] = (rec or {}).get("true_when_recorded")
                d["world_at_deposit"] = (rec or {}).get("world_at_deposit")
                d["world_now"] = S.WorldReader(w, d["pid"]).read(c["subject"], c["predicate"])
            out.append(d)
        return out

    return dict(
        case=case["id"], mode=mode, slots=slots, at=at, take=take,
        base_ok=b["ok"], fork_ok=f["ok"],
        n_drops_base=len(bd), n_drops_fork=len(fd),
        drops_only_in_fork=annotate(uniq(only_fork), wf, fdep),
        drops_only_in_base=annotate(uniq(only_base), wb, bdep),
        deposits_base=len(bdep), deposits_fork=len(fdep),
        in_grammar_base=sum(1 for d in bdep if d["in_grammar"]),
        in_grammar_fork=sum(1 for d in fdep if d["in_grammar"]),
        false_when_recorded_base=sum(1 for d in bdep
                                     if d["in_grammar"] and not d["true_when_recorded"]),
        false_when_recorded_fork=sum(1 for d in fdep
                                     if d["in_grammar"] and not d["true_when_recorded"]),
        false_examples=[d for d in (bdep + fdep)
                        if d["in_grammar"] and not d["true_when_recorded"]][:6],
        in_grammar_examples=[d for d in bdep if d["in_grammar"]][:12],
    )


# ---------------------------------------------------------------------------------------------
# POSITIVE CONTROL -- §0.1 pt 2: the assertion must be able to observe the failure it excludes.
# If the scorer cannot see a divergence planted by hand, a 100% reading is unfalsifiable.
# ---------------------------------------------------------------------------------------------
PLANT_PREDICATES = ("travel.moved", "stores.changed", "record.created", "yield.taken")
PLANT_WHY = ("event-kind claims the corpus ACTUALLY deposits about the candidate's own subject, "
             "measured rather than guessed: a first plant on `act.refused` fired ZERO times "
             "because no corpus world emits that kind, and a plant that never fires is not a "
             "control. All four are run, not one, so the result does not rest on a lucky pick.")


def positive_control(cases, slots: str = "narrow", mode: str = "none") -> dict:
    """PLANT: clause 4 widened by ONE predicate, at the CONTROL arm.

    The plant is deliberately the same SHAPE as the mechanism under test -- a claim in the
    person's own ledger narrowing their own candidate set -- one predicate wider: a person
    declines a verb about subject S if they hold a claim about S whose predicate is an EVENT KIND
    the corpus deposits. Those claims exist in EVERY arm (they are the pre-`W-B` deposit
    behaviour) and WHICH of them a person holds differs between baseline and fork, because the
    fork changes which acts are performed. So the plant creates a real world -> decision channel
    that `none` otherwise does not have, through the same `belief_contradicts` -> `opening_set`
    path `W-B` opened.

    Run at `none`, where the unplanted answer is 0 divergences. If the plant does not move the
    scorer off 0, the scorer is blind and every 100% in this file means nothing."""
    fx = fixtures_for(mode, slots)
    out = []
    for pred in PLANT_PREDICATES:
        def bc(p, row, subject, operands, _p=pred):
            if _REAL_BC(p, row, subject, operands):
                return True
            return any(c.subject == subject and c.predicate == _p for c in p.ledger)
        S.belief_contradicts = bc
        try:
            rows = [A9.fork_case(c, SEED, SEASONS, fixtures=fx) for _, c in cases]
        finally:
            S.belief_contradicts = _REAL_BC
        good = [r for r in rows if r.get("ok")]
        real = [f for r in good for f in r["forks"]
                if f.get("status") in ("DIVERGED", "RECONVERGED")]
        div = [f for f in real if not f["reconverged"]]
        out.append(dict(predicate=pred, n_cases=len(good), genuine=len(real),
                        diverged=len(div), reconverged=len(real) - len(div),
                        detected=(len(div) > 0)))
    return dict(mode=mode, slots=slots, why=PLANT_WHY,
                cases=[c["id"] for _, c in cases], plants=out,
                detected_all=all(o["detected"] for o in out),
                detected_any=any(o["detected"] for o in out))


def comparator_control(cases, slots: str = "narrow", mode: str = "none") -> dict:
    """A SECOND, cruder positive control on the COMPARATOR alone: perturb the fork's own decision
    stream directly and confirm the window reports DIVERGED. This separates 'the scorer cannot
    see a change' from 'the channel does not carry one'."""
    fx = fixtures_for(mode, slots)
    real_run = A9._run
    state = {"n": 0}

    def run(case, seed, seasons, fork_at=-1, take=0, fork_slot=None, fixtures=None):
        out = real_run(case, seed, seasons, fork_at, take, fork_slot, fixtures)
        if fork_at >= 0 and out["ok"] and len(out["decisions"]) > fork_at + 1:
            # rewrite ONE later decision's ranked list -- a change the window must see
            d = list(out["decisions"])
            j = len(d) - 1
            d[j] = (d[j][0], ["__PLANTED__"] + list(d[j][1]), d[j][2])
            out = dict(out); out["decisions"] = d
            state["n"] += 1
        return out

    A9._run = run
    try:
        rows = [A9.fork_case(c, SEED, SEASONS, fixtures=fx) for _, c in cases]
    finally:
        A9._run = real_run
    good = [r for r in rows if r.get("ok")]
    real = [f for r in good for f in r["forks"]
            if f.get("status") in ("DIVERGED", "RECONVERGED")]
    div = [f for f in real if not f["reconverged"]]
    return dict(perturbations_applied=state["n"], genuine=len(real), diverged=len(div),
                detected=(len(div) > 0))


def main(argv) -> int:
    OUT.mkdir(exist_ok=True)
    log = Log()
    out: dict = {"seed": SEED, "seasons": SEASONS, "n_cases": len(CASES),
                 "basis": "89 (apply_rescale applied, as `A9.run` and `sweep.runnable` do)"}

    log.rule("W-D — THE ACCEPTANCE RUN: did `W-B` change the forking result?")
    log("INSTRUMENT", "`arm9_forking.fork_case`, imported UNMODIFIED. This file loops it over "
                      "(deposit mode x fixture point) and adds the two controls.")
    log("BASIS", f"{len(CASES)} cases = {len([1 for l,_ in CASES if l=='NPC'])} NPC + "
                 f"{len([1 for l,_ in CASES if l=='ARC'])} ARC, `apply_rescale` applied "
                 f"(THE 89 BASIS). The 86 basis is the raw `scale:` filter and is NOT used here.",
        "confound 4: `runnable()` skipping `apply_rescale` gives 86 where the corpus runs 89")
    log("SEED", f"{SEED}; seasons {SEASONS} — `runs/arm9.json`'s own published configuration")
    log("CONTEST", "`contest_max_depth` is NOT passed by `A9._run` and does NOT need to be "
                   "(confound 2, checked not assumed): the only contesting verb is "
                   f"{sorted(v for v,r in S.VERB_TABLE.items() if getattr(r,'contests',''))} and "
                   f"`resolvable_verbs()` — the verb set `A9._run` hands `make_chooser` — "
                   f"excludes it, so `resolve()`'s `Forbidden` branch is unreachable. "
                   f"intersection = "
                   f"{sorted(set(v for v,r in S.VERB_TABLE.items() if getattr(r,'contests','')) & set(S.resolvable_verbs()))}",
        "the probe is therefore left unedited; `n_cases_failed` below is the empirical check")

    # ---- 1. the published result, re-derived at the SHIPPED FIXTURE POINT -------------------
    log.rule("W-D.1 — THE SHIPPED FIXTURE POINT (15 slots): the question is UNASKABLE here")
    out["default_fixture"] = {}
    for mode in ARMS:
        print(f"... default/{mode}", flush=True)
        r = sweep_arm(mode, "default")
        out["default_fixture"][mode] = r
        log("MEASURE", f"mode={mode:5} slots=15  cases {r['n_cases_ok']}/{r['n_cases_attempted']} ok "
                       f"| probed {r['probed']} = NO-LIVE-WINDOW {r['no_live_window']} + "
                       f"INERT {r['inert']} + GENUINE {r['genuine']} "
                       f"| reconverged {r['reconverged']}/{r['genuine']} "
                       f"rate {r['reconvergence_rate']}  [{r['seconds']}s]")

    # ---- 2. the acceptance fixture point ----------------------------------------------------
    log.rule("W-D.2 — THE ACCEPTANCE FIXTURE POINT (2 slots): scene_budget=2 (`H-10` arm) x "
             "interactions_per_scene=1 (`H-76` arm)")
    out["narrow_fixture"] = {}
    for mode in ARMS:
        print(f"... narrow/{mode}", flush=True)
        r = sweep_arm(mode, "narrow")
        json.dump(out, open(OUT / "wd_partial.json", "w"), indent=1, default=str)
        out["narrow_fixture"][mode] = r
        log("MEASURE", f"mode={mode:5} slots=2   cases {r['n_cases_ok']}/{r['n_cases_attempted']} ok "
                       f"| probed {r['probed']} = NO-LIVE-WINDOW {r['no_live_window']} + "
                       f"INERT {r['inert']} + GENUINE {r['genuine']} "
                       f"| RECONVERGED {r['reconverged']}/{r['genuine']} "
                       f"({(r['reconvergence_rate'] or 0)*100:.2f}%) DIVERGED {r['diverged']} "
                       f"[{r['seconds']}s]")
        log("WINDOW", f"  strictly-later-tick check: {r['window_slots_checked']} window slots "
                      f"inspected, {r['window_slots_same_tick']} same-or-earlier tick "
                      f"(must be 0 — confound 1)")
        log("STREAM", f"  acts differ {r['acts_differ']}/{r['genuine']} · event-log hash differs "
                      f"{r['hash_differ']}/{r['genuine']} · CHANGED THE STREAM BUT NOT A DECISION "
                      f"{r['stream_only']}")

    # ---- 3. controls -------------------------------------------------------------------------
    log.rule("W-D.3 — CONTROLS")
    n = out["narrow_fixture"]["none"]
    log("NEGATIVE", f"`observation_deposit_mode = none` at 2 slots: "
                    f"{n['reconverged']}/{n['genuine']} reconverged = "
                    f"{(n['reconvergence_rate'] or 0)*100:.2f}%, DIVERGED {n['diverged']}",
        "THE SINGLE MOST IMPORTANT NUMBER. `none` is the pre-`W-B` deposit behaviour exactly; if "
        "it is not 100% then something other than `W-B` moved the harness and every other figure "
        "in this item is confounded")
    sample = CASES[:3]
    pc = positive_control(sample)
    out["positive_control"] = pc
    log("POSITIVE", f"planted widened clause 4 at `none`, cases {pc['cases']} — "
                    f"detected on ALL {len(pc['plants'])} plants: {pc['detected_all']}",
        PLANT_WHY)
    for o in pc["plants"]:
        log("  PLANT", f"predicate {o['predicate']:15} genuine {o['genuine']:3}  "
                       f"DIVERGED {o['diverged']:3}  detected {o['detected']}")
    cc = comparator_control(sample)
    out["comparator_control"] = cc
    log("POSITIVE-2", f"comparator-only plant: {cc['perturbations_applied']} fork decision "
                      f"streams perturbed, genuine {cc['genuine']}, DIVERGED {cc['diverged']} "
                      f"-> detected: {cc['detected']}")

    # ---- 4. forensics on every divergence ----------------------------------------------------
    log.rule("W-D.4 — PER-FORK FORENSICS on every divergence")
    out["forensics"] = {}
    by_case = {c["id"]: c for _, c in CASES}
    for mode in ("actor", "total"):
        divs = out["narrow_fixture"][mode]["divergences"]
        sig = collections.Counter((d["from_verb"], d["to_verb"], tuple(d["changed_at"]))
                                  for d in divs)
        log("COUNT", f"mode={mode}: {len(divs)} divergent forks over "
                     f"{out['narrow_fixture'][mode]['genuine']} genuine")
        log("SIGNATURES", f"  (from_verb -> to_verb, which of the next 3 changed) x count: "
                          f"{dict(sig)}")
        # one representative per distinct signature, plus per distinct changed-decision person,
        # so the forensics covers every SHAPE the divergence takes rather than a prefix of a list.
        seen, reps = set(), []
        for d in divs:
            k = (d["from_verb"], d["to_verb"], tuple(d["changed_at"]), d["person"])
            if k in seen:
                continue
            seen.add(k); reps.append(d)
        reps = reps[:24]
        det = []
        for d in reps:
            fr = forensics(by_case[d["case"]], mode, "narrow", d["at"], d["take"], d["in_budget"])
            fr["fork"] = d
            det.append(fr)
            for side, ds in (("fork-only", fr["drops_only_in_fork"]),
                             ("base-only", fr["drops_only_in_base"])):
                for x in ds:
                    c = x.get("carrier") or {}
                    ops = x.get("operands") or {}
                    self_ref = any(v == x["subject"] for k2, v in ops.items() if k2 != "subject")
                    log("  DROP", f"{mode} {fr['case']} fork(at={d['at']},take={d['take']}) "
                                  f"{d['from_verb']}->{d['to_verb']} | clause-4 drop present only "
                                  f"in {side}: {x['pid']} declines `{x['verb']}` on "
                                  f"{x['subject']!r} ops={ops} SELF-REFERENTIAL={self_ref}")
                    log("  CLAIM", f"    carrier ({c.get('subject')!r}, {c.get('predicate')!r}, "
                                   f"{c.get('value')!r}) when={c.get('when')} "
                                   f"conf={c.get('confidence')} deposited by Event "
                                   f"{x.get('provenance',{}).get('by_event')} kind="
                                   f"{x.get('provenance',{}).get('by_kind')} | "
                                   f"TRUE WHEN RECORDED = {x.get('true_when_recorded')} "
                                   f"(world at deposit {x.get('world_at_deposit')!r}; "
                                   f"world now {x.get('world_now')!r})")
        out["forensics"][mode] = det
        log("SAMPLED", f"  forensics executed on {len(det)} representatives of {len(divs)} "
                       f"divergences ({len(seen)} distinct signatures)")
        fw = sum(f["false_when_recorded_base"] + f["false_when_recorded_fork"] for f in det)
        ig = sum(f["in_grammar_base"] + f["in_grammar_fork"] for f in det)
        log("TRUTH", f"  over the {ig} in-grammar deposits in those runs, "
                     f"{fw} disagreed with `WorldReader` at the barrier that stored them "
                     f"(the `claim.held` class of defect, generalized; 0 is the clean answer)")

    (OUT / "WD_LOG.txt").write_text(log.text() + "\n")
    json.dump(out, open(OUT / "wd_acceptance.json", "w"), indent=1, default=str)
    print(log.text())
    print(f"\nwrote {OUT/'WD_LOG.txt'} and {OUT/'wd_acceptance.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
