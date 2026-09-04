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

TWO CENSUSES ADDED BY THE `W-D` ADVERSARIAL PASS, 2026-09-04, BOTH BECAUSE A CAUSAL CLAIM WAS
BEING MADE WITH NO INSTRUMENT UNDER IT:

  4. EVENT KINDS. `PLANT_WHY` says the `act.refused` plant fired zero times "because no corpus
     world emits that kind". `_fold` returns `ev(row.emits_on_refusal or ("act.refused",), ...)`
     at two sites, so that kind is a LIVE emission path and the zero was equally consistent with
     the predicate never matching a candidate's own subject. `event_kinds` is the census that
     decides which, and nothing in `runs/` was one.
  5. QUESTION SOURCES. `H-122` retracts arm 9c's "the only channel ... is a CLAIM in the actor's
     ledger" and names ONE ledger channel beside `belief_contradicts`. But `questions_for` has
     four sources and THREE of them are pure WORLD reads — Q1 `w.dates`/`w.docket`, Q3
     `w.crossings`/`Query.presence`, Q4 `w.propositions` — none of which touches `p.ledger`. Which
     of the four actually fire in this corpus was unmeasured, so the retraction's scope was
     asserted rather than known. `question_sources` is that count.
"""
from __future__ import annotations
import collections, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import wd_acceptance as W
import arm9_forking as A9
from sweep_core import S

_REAL_QF = S.questions_for


def corpus_drops(mode: str):
    """Every §F1 clause-4 drop over the 89 worlds at the acceptance fixture point, with the
    carrier's depositing Event — no forking, just the baselines. This is the population the
    divergences are drawn from."""
    fx = W.fixtures_for(mode, "narrow")
    rows, false_rec = [], []
    kinds = collections.Counter()          # census 4 -- every Event kind the corpus emits
    qsrc = collections.Counter()           # census 5 -- every Question, by source
    qlead = collections.Counter()          # ... and the source of the one `first` actually takes
    qmulti = collections.Counter()         # how often >1 question SHARES the leading source

    def qspy(w, p):
        out = _REAL_QF(w, p)
        for q in out:
            qsrc[q.source] += 1
        if out:
            qlead[out[0].source] += 1
            qmulti[sum(1 for q in out if q.source == out[0].source) > 1] += 1
        return out

    for lane, case in W.CASES:
        sink = []
        S.questions_for = qspy
        try:
            (_r, drops, deps) = W._instrumented(
                lambda: A9._run(case, W.SEED, W.SEASONS, fixtures=fx))
        finally:
            S.questions_for = _REAL_QF
        w = W._WORLDS[-1]
        kinds.update(e.kind for e in w.log)
        by_cid = {d["cid"]: d for d in deps}
        for d in drops:
            c = d.get("carrier") or {}
            # ⚠ `prov` STAYS EMPTY WHEN THE WALK FINDS NOTHING, AND THAT IS A THIRD ANSWER, NOT A
            # NO. `cross_person` below is False both when the depositor IS the holder and when the
            # walk failed, so an unresolved provenance would silently join the not-cross-person
            # count and make "0 of 123 cross-person" read stronger than it is. It is a live hazard
            # rather than a hypothetical -- the walk needs `claim.deposited` to carry the claim id
            # as its `subject` AND that Event to name a cause AND the cause to still be in the log.
            # `provenance_resolved` is therefore recorded per row and counted in the summary, so
            # the denominator of the cross-person claim is visible instead of assumed.
            # ⚠ AND `dep_actor` IS `Event.subject`, WHICH IS THE ACTOR FOR WHAT `_fold` EMITS AND
            # IS NOT ESTABLISHED FOR EVERY KIND -- `claim_subjects`' `per_change` rule mints claims
            # about THE THING CHANGED, whose Event subject is still the actor, but nothing here
            # proves that for a kind the corpus has not yet emitted. Stated rather than assumed.
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
                             provenance_resolved=(prov.get("actor") is not None),
                             cross_person=(prov.get("actor") is not None
                                           and prov.get("actor") != d["pid"]),
                             true_when_recorded=(by_cid.get(c.get("cid")) or {}).get(
                                 "true_when_recorded")))
        false_rec.extend([d for d in deps if d["in_grammar"] and not d["true_when_recorded"]])
    return rows, false_rec, dict(kinds), dict(qsrc), dict(qlead), {str(k): v for k, v in qmulti.items()}


if __name__ == "__main__":
    out = {}
    for mode in ("none", "actor", "total"):
        rows, false_rec, kinds, qsrc, qlead, qmulti = corpus_drops(mode)
        pred = collections.Counter((r["verb"], r["predicate"]) for r in rows)
        out[mode] = dict(
            n_drops=len(rows),
            self_referential=sum(1 for r in rows if r["self_ref"]),
            not_self_referential=sum(1 for r in rows if not r["self_ref"]),
            cross_person=sum(1 for r in rows if r["cross_person"]),
            # §0.1 pt 2 -- THE DENOMINATOR OF THE CROSS-PERSON CLAIM, REPORTED BESIDE IT. A row
            # whose provenance walk failed counts as not-cross-person, so this is what says
            # whether "0 cross-person" is a measurement or an artifact of failed lookups.
            provenance_resolved=sum(1 for r in rows if r["provenance_resolved"]),
            provenance_unresolved=sum(1 for r in rows if not r["provenance_resolved"]),
            true_when_recorded=collections.Counter(str(r["true_when_recorded"])
                                                   for r in rows),
            by_verb_predicate={f"{a}|{b}": n for (a, b), n in pred.items()},
            depositing_kinds=dict(collections.Counter(r["dep_kind"] for r in rows)),
            non_self_referential_rows=[r for r in rows if not r["self_ref"]][:20],
            n_false_when_recorded=len(false_rec),
            false_when_recorded_predicates=dict(collections.Counter(
                d["predicate"] for d in false_rec)),
            false_when_recorded_examples=false_rec[:6],
            # CENSUS 4 -- every Event kind emitted over the 89 baselines. Settles whether
            # `act.refused` is absent from the corpus or merely never matched by the plant.
            event_kinds=dict(sorted(kinds.items(), key=lambda kv: -kv[1])),
            act_refused_emitted=kinds.get("act.refused", 0),
            # CENSUS 5 -- every Question by source, the source of the one `first` actually takes,
            # and how often the leading source is SHARED (which is when the `q.id` tiebreak, a
            # lexicographic order over content-hashed claim ids, decides what a person answers).
            question_sources=dict(sorted(qsrc.items(), key=lambda kv: -kv[1])),
            question_leading_source=dict(sorted(qlead.items(), key=lambda kv: -kv[1])),
            leading_source_is_shared=qmulti,
        )
        print(mode, {k: v for k, v in out[mode].items()
                     if k not in ("non_self_referential_rows", "false_when_recorded_examples",
                                  "event_kinds")})
        print("   event_kinds:", out[mode]["event_kinds"])
        print()
    json.dump(out, open(Path(__file__).parent / "runs" / "wd_extra.json", "w"), indent=1,
              default=str)
    print("wrote runs/wd_extra.json")
