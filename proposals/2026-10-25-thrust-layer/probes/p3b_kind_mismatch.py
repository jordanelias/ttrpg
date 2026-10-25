"""P3b -- kind mismatch across ALL verbs: an admission (loop/resolve.py `_admits`) refused whose
verdict carries an `exists:<Kind>` Observation with value 0 on a subject that exists in ANOTHER world
collection (the subject is real, just the wrong kind for the verb). Also: refusal clause split
(ineligible / typed-precondition False / UNKNOWN), and admissions that passed `_admits` but whose act
was still refused (refusal at the effect or ENCOUNTER), using the driver's own act classification.

  PYTHONHASHSEED=0 python3 probes/p3b_kind_mismatch.py SEASONS SEED [SEED ...]
"""
import sys
from collections import Counter, defaultdict

sys.path.insert(0, "/home/user/ttrpg")

from engine.season.decision import make_chooser
from engine.season.loop.driver import SeasonDriver, resolvable_verbs
from engine.season.loop import resolve as R
from engine.season.data.verbs import VERB_TABLE
from engine.season.state.ids import H, draw_factory
from engine.season.state.carriers import subject_of
from engine.season.harness import probes as P
from engine.season.harness.populated import build_realm

COLL = {"persons": "Person", "rungs": "Rung", "offices": "Office", "sites": "Site",
        "records": "Record", "propositions": "Proposition", "dates": "Date"}

seasons = int(sys.argv[1])
T = Counter()
per_verb_mm = Counter()
post_admit_ref = Counter()
for seed in [int(s) for s in sys.argv[2:]]:
    w = build_realm(seed, None)
    d = SeasonDriver(w)
    orig = d._admits
    admitted = {}

    def admits(w_, a, row, _o=orig):
        ok, kinds, verdict = _o(w_, a, row)
        T["admissions"] += 1
        if ok:
            T["admitted"] += 1
            admitted[a.id] = a.verb
            return ok, kinds, verdict
        if not R._eligible(d, w_, a, row):
            T["ref_inelig"] += 1
            return ok, kinds, verdict
        T[f"ref_req_{verdict.value}"] += 1
        sid = subject_of(a)
        have = [COLL[c] for c in COLL if sid is not None and sid in getattr(w_, c)]
        mm = any(str(o.predicate).startswith("exists:") and o.value in (0, False)
                 and str(o.subject) == str(sid) and have
                 and str(o.predicate).split(":", 1)[1] not in have
                 for o in (verdict.observed or ()))
        if mm:
            T["ref_kind_mismatch"] += 1
            per_verb_mm[a.verb] += 1
        return ok, kinds, verdict

    d._admits = admits
    orig_res = d.resolve
    def resolve(tok, acts, cmd, _o=orig_res):
        ev = _o(tok, acts, cmd)
        refused = set()
        for e in ev:
            a = d.act_of.get(e.id)
            if a is not None and e.kind in (VERB_TABLE[a.verb].emits_on_refusal or ()):
                refused.add(a.id)
        for aid in refused:
            if aid in admitted:
                post_admit_ref[admitted[aid]] += 1
        admitted.clear()
        return ev
    d.resolve = resolve
    mint = lambda pid, verb, sj: H(w.world_seed, w.tick, pid, f"act:{verb}:{sj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                      draw=draw_factory(w.world_seed, lambda: w.tick))
    for _ in range(seasons):
        d.season(ch, question=None, subsistence=P.SUBSIST,
                 contest_max_depth=w.fixtures.get("contest_max_depth"))
    print(f"seed={seed} log={len(w.log)} hash={w.content_hash()[:16]}", flush=True)

print("TOTALS", dict(T))
print("kind-mismatch by verb", per_verb_mm.most_common())
print("admitted-then-refused by verb (effect/ENCOUNTER refusals)", post_admit_ref.most_common())
