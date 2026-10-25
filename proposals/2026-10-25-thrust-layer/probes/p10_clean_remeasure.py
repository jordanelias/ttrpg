"""P10 -- the three measurements the antagonist's A3/A6/A5 findings put in dispute, re-taken per ACT.

  (1) `_admits` calls vs UNIQUE acts (A3b: P3b's 7,737 counted calls, not acts).
  (2) Wrong-kind refusal classified CORRECTLY, per act: record sub-kinds (`works`, `petition`,
      `dispensation`, ...) are not collections (a Record of another sub-kind is its own class); `DocketItem`
      is a world-state read (`docketed(w, subject)`), not a collection class. Four classes:
        collection_mismatch   wanted a collection class (Person/Rung/Office/Site/...), subject lives in another
        subkind_mismatch      wanted a Record sub-kind; subject is a Record of another sub-kind
        subkind_wrong_coll    wanted a Record sub-kind; subject lives in a different collection
        world_read_docket     wanted `exists:DocketItem`; a world read, S12's own "stays a refusal"
        absent_subject        subject exists in no collection
  (3) Graded loss (A6): an act whose every refusal-kind Event has degree Failure AND whose kind is also in the
      row's `emits` -- the contest ran and went against the actor; the driver's rule counts it refused.
  Per-act tick tags let one 4-season run give both the 2-season figures (ticks 0,1) and the 4-season ones.
  Repeats: (actor, verb, subject) keys that are wrong-kind refused in more than one season.

Classification of refused/executed copies loop/driver.py:489-505, as P1 did. Run:
  PYTHONHASHSEED=0 python3 probes/p10_clean_remeasure.py SEASONS SEED [SEED ...]
"""
import json
import os
import sys
from collections import Counter, defaultdict

sys.path.insert(0, "/home/user/ttrpg")

from engine.season.decision import make_chooser
from engine.season.loop.driver import SeasonDriver, resolvable_verbs
from engine.season.loop import resolve as R
from engine.season.data.verbs import VERB_TABLE
from engine.season.data.rosters import RECORD_KINDS
from engine.season.state.ids import H, draw_factory
from engine.season.state.carriers import subject_of
from engine.season.harness import probes as P
from engine.season.harness.populated import build_realm

COLL = {"persons": "Person", "rungs": "Rung", "offices": "Office", "sites": "Site",
        "records": "Record", "propositions": "Proposition", "dates": "Date"}
COLL_CLASSES = set(COLL.values())

seasons = int(sys.argv[1])
seeds = [int(s) for s in sys.argv[2:]]


def classify(w, a, verdict):
    """-> class of the FIRST exists:<Kind>=0 observation on the act's subject, or None."""
    sid = subject_of(a)
    for o in (verdict.observed or ()):
        p = str(o.predicate)
        if not (p.startswith("exists:") and o.value in (0, False) and str(o.subject) == str(sid)):
            continue
        kind = p.split(":", 1)[1]
        have = [COLL[c] for c in COLL if sid is not None and sid in getattr(w, c)]
        if kind == "DocketItem":
            return "world_read_docket", kind
        if kind in COLL_CLASSES:
            if not have:
                return "absent_subject", kind
            return ("collection_mismatch", kind) if kind not in have else (None, kind)
        if kind in RECORD_KINDS:
            if not have:
                return "absent_subject", kind
            if "Record" in have:
                return "subkind_mismatch", kind
            return "subkind_wrong_coll", kind
        return "other_kind", kind
    return None, None


# per (seed, tick-window) accumulators, keyed by window label "s2" (ticks 0-1) and "s4" (all)
A = {k: Counter() for k in ("s2", "s4")}
byverb = {k: defaultdict(Counter) for k in ("s2", "s4")}
repeats = Counter()          # (seed, actor, verb, subject) -> number of distinct ticks wrong-kind refused
call_hist = Counter()        # admits calls per unique act id
hashes = {}
for seed in seeds:
    w = build_realm(seed, None)
    d = SeasonDriver(w)
    orig = d._admits
    calls = Counter()
    first_refusal = {}       # act id -> (class, kind, verbname)
    acts_seen = {}           # act id -> tick

    def admits(w_, a, row, _o=orig):
        ok, kinds, verdict = _o(w_, a, row)
        calls[a.id] += 1
        if not ok and a.id not in first_refusal and R._eligible(d, w_, a, row):
            first_refusal[a.id] = classify(w_, a, verdict) + (a.verb,)
        elif not ok and a.id not in first_refusal:
            first_refusal[a.id] = ("ineligible", None, a.verb)
        return ok, kinds, verdict

    captured = []
    orig_res, orig_enc = d.resolve, d.encounter

    def resolve(tok, acts, cmd):
        t = w.tick
        ev = orig_res(tok, acts, cmd)
        captured.append([t, list(acts), list(ev)])
        return ev

    def encounter(tok, events, cmd):
        ev = orig_enc(tok, events, cmd)
        captured[-1][2].extend(ev)
        return ev

    d._admits, d.resolve, d.encounter = admits, resolve, encounter
    mint = lambda pid, verb, sj: H(w.world_seed, w.tick, pid, f"act:{verb}:{sj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                      draw=draw_factory(w.world_seed, lambda: w.tick))
    for _ in range(seasons):
        d.season(ch, question=None, subsistence=P.SUBSIST,
                 contest_max_depth=w.fixtures.get("contest_max_depth"))
    hashes[seed] = w.content_hash()[:16]
    print(f"seed={seed} log={len(w.log)} tick={w.tick} hash={hashes[seed]}", flush=True)

    for t, acts, events in captured:
        em = defaultdict(list)
        for e in events:
            a = d.act_of.get(e.id)
            if a is not None:
                em[a.id].append(e)
        for a in acts:
            row = VERB_TABLE.get(a.verb)
            evs = em.get(a.id, [])
            refkinds = row.emits_on_refusal or ()
            ref = [e for e in evs if e.kind in refkinds]
            for win in (("s2", "s4") if t < 2 else ("s4",)):
                C = A[win]
                C["attempted"] += 1
                call_hist[calls[a.id]] += 1 if win == "s4" else 0
                if not evs:
                    C["null"] += 1
                    continue
                if not ref:
                    C["executed"] += 1
                    byverb[win][a.verb]["executed"] += 1
                    continue
                C["refused"] += 1
                byverb[win][a.verb]["refused"] += 1
                graded = all(e.degree == "Failure" for e in ref) and any(k in (row.emits or ()) for k in {e.kind for e in ref})
                # `emits` holds the kinds an executed act may emit; a kind in BOTH columns is the graded loss
                both = bool(set(e.kind for e in ref) & set(row.emits or ()))
                if both:
                    C["refused_kind_also_in_emits"] += 1
                if graded:
                    C["graded_loss"] += 1
                fr = first_refusal.get(a.id)
                if fr is None:
                    C["refused_not_at_admission"] += 1
                else:
                    cls = fr[0]
                    C["adm_ref:" + str(cls)] += 1
                    byverb[win][a.verb]["adm_ref:" + str(cls)] += 1
                    if cls in ("collection_mismatch", "subkind_wrong_coll"):
                        C["wrongkind_collection"] += 1
                        if win == "s4":
                            repeats[(seed, a.actor, a.verb, subject_of(a), t)] += 1
                    if cls in ("collection_mismatch", "subkind_wrong_coll", "subkind_mismatch"):
                        C["wrongkind_any"] += 1

print()
for win in ("s2", "s4"):
    C = A[win]
    n = C["attempted"]
    print(f"== window {win}: attempted={n} executed={C['executed']} refused={C['refused']} null={C['null']} "
          f"refused_share={C['refused'] / n:.4f}")
    print(f"   refused whose refusal kind is ALSO in the row's `emits` (both columns): {C['refused_kind_also_in_emits']}"
          f"  ({C['refused_kind_also_in_emits'] / max(1, C['refused']):.4f} of refused)")
    print(f"   graded_loss (all refusal events degree Failure AND kind in emits): {C['graded_loss']}"
          f"  ({C['graded_loss'] / n:.4f} of attempted)")
    for k in sorted(c for c in C if c.startswith("adm_ref:")):
        print(f"   {k:34s} {C[k]:6d}  ({C[k] / n:.4f} of attempted)")
    print(f"   refused_not_at_admission {C['refused_not_at_admission']}")
    print(f"   wrongkind_collection (collection_mismatch+subkind_wrong_coll) {C['wrongkind_collection']}"
          f" ({C['wrongkind_collection'] / n:.4f} of attempted)")
    print(f"   wrongkind_any (+subkind_mismatch) {C['wrongkind_any']} ({C['wrongkind_any'] / n:.4f})")
    print("   top verbs by wrongkind_collection:",
          sorted(((v, c["adm_ref:collection_mismatch"] + c["adm_ref:subkind_wrong_coll"]) for v, c in byverb[win].items()),
                 key=lambda x: -x[1])[:10])

print("\n_admits calls per unique act (s4 window):", dict(sorted(call_hist.items())))
keys = Counter((s, ac, v, sj) for (s, ac, v, sj, t) in repeats)
rep = sum(1 for k, n in keys.items() if n > 1)
tot_ticks = Counter()
for (s, ac, v, sj, t), n in repeats.items():
    tot_ticks[(s, ac, v, sj)] += 1
multi = sum(1 for k, n in tot_ticks.items() if n > 1)
print(f"wrong-kind (collection) keys (seed,actor,verb,subject): {len(tot_ticks)}; refused in >1 season: {multi}; "
      f"wrong-kind acts total {sum(repeats.values())}")
print("hashes", hashes)
json.dump({k: dict(A[k]) for k in A}, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "p10_out.json"), "w"), indent=1)
