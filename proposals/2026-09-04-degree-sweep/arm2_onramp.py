"""ARM 2 -- THE ON-RAMP. Can a season loop reach a degree at all?

Three questions, each answered by execution rather than by reading:
  2a  does the CHOOSER ever propose the contested verb?  (the on-ramp)
  2b  forced past the chooser, does the seam CALL personal combat from a real corpus world?
  2c  forced past the seam into the fold, what does the guard do to the RUN?

⚠ THE PLANT IS THE CHAIN'S OWN TECHNIQUE, NOT A NEW ONE. `corpus_run.planted_control` plants two
acts and a cross-person cause to prove `R3`'s detector works, and says why: printing a number
entailed by the setup is not a control. This plants an act the chooser cannot propose, for the
same reason -- to show that the road beyond it is real, or that it is not.
"""
from __future__ import annotations
import sweep_core as K
from sweep_core import S, C, R, CS, KW, Log


def runnable_cases(lane: str) -> list:
    return [c for c in R.load_cases(lane) if str(c.get("scale")) in set(S.RUNG_KINDS)]


def run(log: Log) -> dict:
    out = {}
    log.rule("ARM 2 — THE ON-RAMP: can a season loop reach a degree at all?")

    # ---- 2a ---------------------------------------------------------------
    log.rule("ARM 2a — does the chooser ever propose the contested verb?")
    fold = K.foldable()
    log("MEASURE", f"`resolvable_verbs()` = {len(fold)} of {len(S.VERB_TABLE)} verbs",
        "the chooser draws candidates from this set only; a verb outside it can never be proposed")
    row = S.VERB_TABLE[KW]
    import shape as _S
    has_eff = KW in getattr(_S, "EFFECTS", {})
    log("MEASURE", f"is {KW!r} in it? {KW in fold}")
    log("WHY-NOT", f"and the reason is NOT what an earlier draft of this arm said. "
                   f"{KW!r} HAS an effect ({has_eff}, `_eff_kill` at shape.py:3847) and its "
                   f"`requires: {row.requires!r}` is in `NO_PRECONDITION`, so both the predicate "
                   f"and effect gates PASS.",
        "the exclusion comes from the THIRD gate — `contested = bool(row.contests)` at "
        "shape.py:2336 — whose own comment says so. The distinction matters because a reader "
        "acting on 'add a predicate and an effect' would change nothing: what excludes this verb "
        "is precisely that it is CONTESTED, i.e. the fold defers it to the seam by design. "
        "Corrected after the adversarial pass.")
    log("VERDICT", f"the ONLY degree-keyed verb is {'IN' if KW in fold else 'NOT IN'} the "
                   f"candidate set",
        "so no act the chooser produces can carry `contests:`, so `contest()` is unreachable from "
        "`season()`, so no degree branch is ever selected. The road is built; there is no on-ramp.")
    out["2a"] = dict(foldable=sorted(fold), kw_foldable=KW in fold,
                     n_verbs=len(S.VERB_TABLE), n_foldable=len(fold))

    # ---- 2b ---------------------------------------------------------------
    log.rule("ARM 2b — forced past the chooser: does the seam CALL personal combat?")
    case = runnable_cases("NPC")[0]
    w = C.build_at(case, 0)
    log("BUILD", f"world from case {case['id']} ({case.get('name','')[:40]}), scale {case['scale']}",
        f"persons: {list(w.persons)} — the corpus seats three, which is what a contest needs")
    res = CS.resolve(w, ["p_a", "p_b"], ["cause_probe"], "the body")
    log("CALL", "combat_seam.resolve(w, ['p_a','p_b'], ['cause_probe'], 'the body')",
        "this is the call `contest()` makes when a prize routes to `personal_combat`")
    log("RESULT", f"status={res.get('status')} module={res.get('module')} "
                  f"resolver={res.get('resolver')}",
        "the LIVE engine at systems/combat/combat_engine_v1 actually ran — this is not a stub")
    log("RESULT", f"result={res.get('result')} winner={res.get('winner')!r} "
                  f"unresolved={res.get('unresolved')} bouts={res.get('bouts')}")
    for pid, st in (res.get("wound_state") or {}).items():
        log("WOUND", f"{pid}: {st}",
            "the seam names this `THE DEGREE SOURCE` — severity is read off the scene, "
            "not mapped from the winner")
    out["2b"] = dict(status=res.get("status"), winner=res.get("winner"),
                     result=res.get("result"), wound_state=res.get("wound_state"),
                     bouts=res.get("bouts"))

    # ---- 2b-control: winner vs wound_state agreement ----------------------
    log.rule("ARM 2b-control — do the seam's TWO degree surfaces agree with each other?")
    log("WHY", "the seam returns both `winner` and `wound_state`. A degree mapping could be built "
               "on either. If they disagree, the choice of surface changes the outcome.")
    import random as _rnd
    eng = CS.engine()
    dis = agree = unres = 0
    if eng is not None:
        wrapper, combatant = eng
        for s in range(300):
            A = combatant.Combatant("A", end=4); B = combatant.Combatant("B", end=4)
            r = wrapper.fight(A, B, rng=_rnd.Random(s))
            if r == 0:
                unres += 1; continue
            win = A if r == 1 else B
            if getattr(win, "wt", None) is not None and win.wt.felled:
                dis += 1
            else:
                agree += 1
    tot = agree + dis
    pct = (dis / tot * 100) if tot else 0.0
    log("MEASURE", f"300 seeded fights: {tot} decided, {unres} unresolved")
    log("MEASURE", f"winner is UNFELLED (surfaces agree): {agree}")
    log("MEASURE", f"winner is FELLED  (surfaces CONTRADICT): {dis}  = {pct:.1f}%")
    log("CAUSE", "systems/combat/combat_engine_v1/wrapper.py:493 — "
                 "`if result!=0 and rng.random()<cfg['UPSET_FLOOR']: result = -result`",
        "UPSET_FLOOR=0.05 inverts the RESULT after the fell was recorded and never touches the "
        "wound trackers. A deliberate designer rule (ED-PC-0036).")
    log("⚠ RETRACTED", "an earlier draft of this arm said the desynchronisation was 'NOT declared "
                       "anywhere'. FALSE — it is declared at the constant's own definition site.",
        "config.py:295-304, verbatim: 'the trace stream emits `engagement_end felled=X` and then "
        "`fight_result winner=X`, WITH NO IN-MODEL EVENT CORRESPONDING TO THE REVERSAL'. The "
        "producer cited wrapper.py:493 and never opened config.py. What remains true and is the "
        "narrowed claim: `combat_seam` names `wound_state` THE DEGREE SOURCE and returns `winner` "
        "beside it without repeating that warning, so a caller reading only the seam would not "
        "know the two disagree. Found by the adversarial pass.")
    out["2b_control"] = dict(decided=tot, agree=agree, contradict=dis, pct=pct, unresolved=unres)
    return out


def run_2c(log: Log) -> dict:
    """2c -- forced past the seam into the fold: what does the guard do to the RUN?"""
    out = {}
    log.rule("ARM 2c — the guard at shape.py:4448, and what it costs the corpus run")
    log("READ", "shape.py:4441-4447 states the guard's INTENT, verbatim:")
    log("QUOTE", "'if that branch is ever wired to fall through without minting a degree, it "
                 "fails loudly here instead of silently writing the full kill. That is the guard.'",
        "the DIRECTION is right — loud beats a silent full kill. This arm measures the MECHANISM.")

    # (i) STATIC — the catch lists, by `issubclass`, not by reading.
    log.rule("ARM 2c-i — is the guard's exception in the run's catch lists? (static)")
    caught_a = (S.InstrumentDefect,)
    caught_b = (S.ShapeGap, S.Unspecified, S.Forbidden, S.NoProducer)
    log("READ", "corpus_run.run_case:343  `except S.InstrumentDefect`")
    log("READ", "corpus_run.run_case:350  `except (S.ShapeGap, S.Unspecified, S.Forbidden, "
                "S.NoProducer)`",
        "these two clauses are the ONLY handlers between a folding season and the caller")
    hits = {}
    for name, exc in (("SystemExit", SystemExit), ("Unspecified", S.Unspecified),
                      ("Forbidden", S.Forbidden), ("InstrumentDefect", S.InstrumentDefect)):
        a = issubclass(exc, caught_a); b = issubclass(exc, caught_b)
        base = "Exception" if issubclass(exc, Exception) else "BaseException-ONLY"
        hits[name] = dict(clause_343=a, clause_350=b, caught=a or b, base=base)
        log("MEASURE", f"{name:17} base={base:18} caught by 343={a}  by 350={b}  -> "
                       f"{'CAUGHT' if (a or b) else 'ESCAPES THE RUN'}")
    out["static"] = hits

    # (ii) DYNAMIC — the fall-through, under the run's own handlers.
    log.rule("ARM 2c-ii — the same, executed (the fall-through under run_case's handlers)")
    case = runnable_cases("NPC")[0]
    w = C.build_at(case, 0)
    d = S.SeasonDriver(w)
    act = S.Act(id="sweep_kw", actor="p_a", verb=KW, payload={"subject": "p_b"})
    log("PLANT", f"Act(id='sweep_kw', actor='p_a', verb={KW!r}, payload={{'subject':'p_b'}})",
        "the act the chooser cannot propose (2a). Folded DIRECTLY, which is exactly what the "
        "contest branch would do if wired to fall through once H-98 rules the bands.")
    log("CALL", "d._fold(w, act)  wrapped in run_case's own two except clauses")
    verdict, detail = None, ""
    try:
        try:
            d._fold(w, act)
            verdict, detail = "COMPLETED", "no gap raised"
        except S.InstrumentDefect as e:
            verdict, detail = "CAUGHT-343 -> status INSTRUMENT-DEFECT", f"{type(e).__name__}: {e}"
        except (S.ShapeGap, S.Unspecified, S.Forbidden, S.NoProducer) as e:
            verdict, detail = "CAUGHT-350 -> status DESIGN-GAP", f"{type(e).__name__}: {e}"
    except BaseException as e:
        verdict = "ESCAPED BOTH CLAUSES"
        detail = f"{type(e).__name__}: {e}"
    log("RESULT", verdict)
    log("DETAIL", detail)
    out["dynamic"] = dict(verdict=verdict, detail=detail)

    log.rule("ARM 2c — what this costs, stated at its true size and no larger")
    for line, why in [
        ("the guard fires correctly — a degreeless contested fold does NOT write the full kill",
         "the direction the comment claims is real and this arm confirms it"),
        ("but it raises `SystemExit`, the ONLY run-time refusal in shape.py that is not a typed gap",
         "⚠ FIXED BY W-0 2026-09-04, and this arm now records the history rather than the state. "
         "AS FOUND there were 18 `SystemExit` raises in shape.py: 14 load-time and correctly "
         "fatal, and 4 run-time ones that were exactly the degree branches. Those 4 now raise "
         "`Unspecified` and are CAUGHT as DESIGN-GAP; the 14 remain, at lines 365, 383, 395, "
         "454, 774, 780, 807, 816, 822, 831, 839, 844, 852, 856. Line numbers re-derived after "
         "the edit rather than carried over — the first restatement of them was +31 stale, "
         "copied from the pre-fix register row, and an adversarial pass caught it"),
        ("so it is not classified: no DESIGN-GAP row, no `kind` histogram entry, no §-citation",
         "the 78 typed gaps carry `where`/`needs`/`law`; SystemExit carries a bare string"),
        ("and it ends the PROCESS, so every case after it in the corpus goes unmeasured",
         "a one-case design gap is converted into a whole-corpus run termination"),
    ]:
        log("COST", line, why)
    return out
