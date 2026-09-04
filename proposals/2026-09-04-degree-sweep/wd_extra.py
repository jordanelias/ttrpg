"""W-D supplement — three questions the 24-representative forensics sample could not close.

  1. AT `total`, IS ANY CARRYING BELIEF CROSS-PERSON? `total` fans a read to every witness, and
     that is the propagation §F1 wants. The sampled representatives were all holder == depositor,
     but a sample is not a corpus, and the sampled signatures are not weighted by frequency.
     Measured over the WHOLE corpus by wrapping `belief_contradicts` and reading the carrier's
     depositing Event out of the log.
  2. WHOSE DECISION CHANGED — the fork's own person, or somebody else's? Read off the baseline
     decision trace at the changed index.
  3. WHAT ARE THE IN-GRAMMAR DEPOSITS THAT DISAGREE WITH THE WORLD AT THEIR OWN BARRIER? None of
     them carried a divergence, but 6/120 and 75/957 is not nothing and the shape matters.
"""
from __future__ import annotations
import collections, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import wd_acceptance as W
import arm9_forking as A9
from sweep_core import S


def corpus_drops(mode: str):
    """Every §F1 clause-4 drop over the 89 worlds at the acceptance fixture point, with the
    carrier's depositing Event — no forking, just the baselines. This is the population the
    divergences are drawn from."""
    fx = W.fixtures_for(mode, "narrow")
    rows, false_rec = [], []
    for lane, case in W.CASES:
        sink = []
        (_r, drops, deps) = W._instrumented(
            lambda: A9._run(case, W.SEED, W.SEASONS, fixtures=fx))
        w = W._WORLDS[-1]
        by_cid = {d["cid"]: d for d in deps}
        for d in drops:
            c = d.get("carrier") or {}
            prov = {}
            for e in w.log:
                if e.kind == "claim.deposited" and e.subject == c.get("cid"):
                    src = e.causes[0] if e.causes else None
                    for e2 in w.log:
                        if e2.id == src:
                            prov = dict(kind=e2.kind, actor=e2.subject)
                    break
            ops = d.get("operands") or {}
            rows.append(dict(case=case["id"], lane=lane, pid=d["pid"], verb=d["verb"],
                             subject=d["subject"],
                             self_ref=any(v == d["subject"] for k, v in ops.items()
                                          if k != "subject"),
                             carrier_subject=c.get("subject"), predicate=c.get("predicate"),
                             value=c.get("value"), when=c.get("when"),
                             dep_kind=prov.get("kind"), dep_actor=prov.get("actor"),
                             cross_person=(prov.get("actor") is not None
                                           and prov.get("actor") != d["pid"]),
                             true_when_recorded=(by_cid.get(c.get("cid")) or {}).get(
                                 "true_when_recorded")))
        false_rec.extend([d for d in deps if d["in_grammar"] and not d["true_when_recorded"]])
    return rows, false_rec


if __name__ == "__main__":
    out = {}
    for mode in ("none", "actor", "total"):
        rows, false_rec = corpus_drops(mode)
        pred = collections.Counter((r["verb"], r["predicate"]) for r in rows)
        out[mode] = dict(
            n_drops=len(rows),
            self_referential=sum(1 for r in rows if r["self_ref"]),
            not_self_referential=sum(1 for r in rows if not r["self_ref"]),
            cross_person=sum(1 for r in rows if r["cross_person"]),
            true_when_recorded=collections.Counter(str(r["true_when_recorded"])
                                                   for r in rows),
            by_verb_predicate={f"{a}|{b}": n for (a, b), n in pred.items()},
            depositing_kinds=dict(collections.Counter(r["dep_kind"] for r in rows)),
            non_self_referential_rows=[r for r in rows if not r["self_ref"]][:20],
            n_false_when_recorded=len(false_rec),
            false_when_recorded_predicates=dict(collections.Counter(
                d["predicate"] for d in false_rec)),
            false_when_recorded_examples=false_rec[:6],
        )
        print(mode, {k: v for k, v in out[mode].items()
                     if k not in ("non_self_referential_rows", "false_when_recorded_examples")})
        print()
    json.dump(out, open(Path(__file__).parent / "runs" / "wd_extra.json", "w"), indent=1,
              default=str)
    print("wrote runs/wd_extra.json")
