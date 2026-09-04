"""ARM 4 -- (a) what `content_hash` observes, and (b) WHAT THE SUBSYSTEM RETURNS, which the
calling code has to accept.

⚠⚠ ARM 4b's ORIGINAL QUESTION WAS THE WRONG QUESTION, AND IT IS RETRACTED (Jordan, 2026-09-04).
It asked *"can four bands be read off what personal combat returns?"* -- i.e. it treated the
subsystem's output as a quantity for THIS code to band. Jordan, verbatim:

    *"why would there be four bands for combat data? the combat engine determines the result
    there. your code just has to accept the result"*

That is a ruling and it dissolves the question rather than answering it. `degree_from_net`'s four
bands are for a roll THE LOOP ITSELF MAKES -- a pool against an obstacle, where the margin is the
loop's own arithmetic. A contested act does not make that roll: it DISPATCHES, and personal
combat decides. So the seam has no band to compute and no mapping to invent; it has a result to
ACCEPT FAITHFULLY.

TWO CONSEQUENCES, AND THE SECOND IS THE ONE THAT MATTERS.
1. `kill / wound` REFUSING the four canonical tokens (Arm 1a, 0 of 4) is CORRECT BEHAVIOUR, not
   a gap. Its declared `Felled | Wounded | Untouched` mirrors the engine's own terminal states,
   which is what accepting the result looks like. Arm 1a's numbers stand; the reading that they
   evidenced a missing ladder does not, and is withdrawn everywhere it appeared.
2. The question becomes ACCEPTANCE FIDELITY: given what the engine returned, does the calling
   code do what the engine said? Arms 1-3 answer that, and the answer is no, by three
   independent mechanisms. This arm's measurement is retained ONLY as a description of the
   result-shape the code must accept -- never as a proposal for bands over it.
"""
from __future__ import annotations
import collections, random
import sweep_core as K
from sweep_core import S, C, R, CS, Log


def run_a(log: Log) -> dict:
    log.rule("ARM 4a — what does `content_hash` actually observe?")
    log("READ", "shape.py:2026-2033 — `content_hash` iterates `self.log` ONLY",
        "it hashes each Event's id/kind/subject/emitted_at/degree/causes and each StateChange's "
        "subject/mode/driver/field/delta. It reads `w.persons`, `w.tenures`, `w.sites`, "
        "`w.rungs` — the WORLD — not at all.")
    case = [c for c in R.load_cases("NPC") if str(c.get("scale")) in set(S.RUNG_KINDS)][0]
    w1, w2 = C.build_at(case, 0), C.build_at(case, 0)
    h0 = (w1.content_hash(), w2.content_hash())
    log("BUILD", f"two identical worlds from {case['id']}: hashes equal = {h0[0] == h0[1]}")
    victim = "p_b"
    del w2.persons[victim]
    h1 = (w1.content_hash(), w2.content_hash())
    log("MUTATE", f"delete person {victim!r} from world 2 — no Event appended",
        "this is the state a `Felled` fold leaves if its Event is dropped or never logged")
    log("RESULT", f"world1 hash == world2 hash ? {h1[0] == h1[1]}",
        "a world missing a person hashes identically to one that has them")
    log("VERDICT", "`content_hash` is a hash of the LOG, not of the WORLD",
        "R4 — named a load-bearing control in PR #362 — pins that the EVENT STREAM replays "
        "identically. It does not pin that the world state does. A divergence in state that "
        "leaves the log identical is invisible to it. That is a narrower guarantee than the name "
        "`content_hash` suggests, and narrower than 'byte-identical corpus_run output' implies.")
    return dict(equal_before=h0[0] == h0[1], equal_after_delete=h1[0] == h1[1])


def run_b(log: Log, n: int = 600) -> dict:
    log.rule("ARM 4b — WHAT THE ENGINE RETURNS, which the calling code has to accept")
    log("RETRACTED", "this arm first asked 'can four bands be read off this?' — the wrong "
                     "question, retracted on Jordan's ruling 2026-09-04",
        "'the combat engine determines the result there. your code just has to accept the "
        "result.' The measurement below is kept as a DESCRIPTION of the result-shape; the "
        "four-band verdict it originally carried is withdrawn.")
    eng = CS.engine()
    if eng is None:
        log("GAP", f"engine unavailable: {CS.load_error()}"); return {}
    wrapper, combatant = eng
    rows = []
    for s in range(n):
        A = combatant.Combatant("A", end=4); B = combatant.Combatant("B", end=4)
        r = wrapper.fight(A, B, rng=random.Random(s))
        win, lose = (A, B) if r == 1 else ((B, A) if r == -1 else (None, None))
        rows.append(dict(result=r,
                         a_w=A.wt.wounds, b_w=B.wt.wounds,
                         a_f=A.wt.felled, b_f=B.wt.felled,
                         a_hr=A.wt.health_remaining, b_hr=B.wt.health_remaining,
                         win_w=(win.wt.wounds if win else None),
                         win_hr=(win.wt.health_remaining if win else None),
                         win_hf=(win.wt.health_full if win else None),
                         lose_hr=(lose.wt.health_remaining if lose else None)))
    log("MEASURE", f"{n} seeded fights, identical parties (the corpus derives one field, `end`)")
    dec = [x for x in rows if x["result"] != 0]
    log("MEASURE", f"decided {len(dec)}, unresolved {len(rows)-len(dec)} "
                   f"({(len(rows)-len(dec))/len(rows)*100:.1f}%)",
        "`result == 0` is a RULED outcome (Jordan 2026-06-02), not a failure")
    out = {}
    for name, key in (("winner's WOUNDS", "win_w"),
                      ("winner's HEALTH REMAINING", "win_hr"),
                      ("loser's HEALTH REMAINING", "lose_hr")):
        vals = [x[key] for x in dec if x[key] is not None]
        c = collections.Counter(vals)
        out[key] = dict(distinct=len(c), dist=dict(sorted(c.items())))
        log("MEASURE", f"{name}: {len(c)} distinct value(s) — {dict(sorted(c.items()))}",
            "this is the quantity a band edge would have to cut")
    wv = out["win_w"]["distinct"]
    log("SHAPE", f"the result the code must accept is a TERMINAL STATE plus a severity reading: "
                 f"felled/not, and a wound count taking {wv} distinct values",
        "that is what `combat_seam.resolve` already returns in `wound_state`, and it is what "
        "`Felled | Wounded | Untouched` is a faithful three-way reading of")
    nz = sum(v for k, v in out["lose_hr"]["dist"].items() if k != 0)
    log("CROSS-CHECK", f"{nz} of {len(dec)} 'losers' are NOT at health 0 "
                       f"({nz/len(dec)*100:.1f}%)",
        "`wrapper.fight` sets a result ONLY when a fighter is felled, so a loser above 0 health "
        "can only be an UPSET_FLOOR inversion. This independently reproduces Arm 2b-control's "
        "~5% from a different quantity, which is why it is reported: two measurements of the "
        "same mechanism that did not share a code path")
    out["upset_cross_check_pct"] = nz / len(dec) * 100 if dec else 0.0
    out["n"] = n; out["decided"] = len(dec)
    return out
