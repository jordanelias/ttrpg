"""W-D sensitivity check — IS THE DECISION FINGERPRINT WIDE ENOUGH?

`arm9_forking.recorder` records a deliberation as `(person, [verb, ...], tick)` — **VERBS ONLY**.
`Query.opening_set` returns `Candidate(verb, subject, why, operands)`, so two candidate lists with
the same verbs and DIFFERENT SUBJECTS compare EQUAL and the fork is scored RECONVERGED. That bias
runs one way — it can only make reconvergence look HIGHER — so the shipped 95.77% is an upper
bound on reconvergence and the acceptance is safe. **But the NEGATIVE CONTROL is the number it
could ruin**: a `none` arm that is 100% on verbs and less than 100% on (verb, subject) would mean
the pre-`W-B` channel was never fully closed, and every reading in `W-D` would need restating.

So this runs the identical probe on a COPY of `arm9_forking.py` whose ONLY edit is
`[c.verb for c in ranked]` -> `[(c.verb, c.subject) for c in ranked]`. The shipped instrument is
untouched; this is a second measurement beside it, not a replacement.
"""
from __future__ import annotations
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import wd_acceptance as W
import arm9_subj as A9S

if __name__ == "__main__":
    mode, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    fx = W.fixtures_for(mode, "narrow")
    import collections
    rows, kinds = [], collections.Counter()
    for _, c in W.CASES[a:b]:
        r = A9S.fork_case(c, W.SEED, W.SEASONS, fixtures=fx)
        rows.append(r)
        if not r.get("ok"):
            continue
        divs = [f for f in r["forks"] if f.get("status") == "DIVERGED"]
        if not divs:
            continue
        # CLASSIFY EVERY CHANGED WINDOW SLOT. The point of the widened fingerprint is to say WHAT
        # changed, not only that something did: a verb leaving the set is `W-B`'s clause 4, and a
        # subject substitution under an identical verb sequence is the OTHER channel — `q.referents`
        # from `questions_for`, consumed by `opening_set` clause 3.
        base = A9S._run(c, W.SEED, W.SEASONS, fixtures=fx)
        for f in divs:
            fk = A9S._run(c, W.SEED, W.SEASONS, fork_at=f["at"], take=f["take"],
                          fork_slot=f["in_budget"], fixtures=fx)
            for wnd in f["window"]:
                if wnd["same"] is not False:
                    continue
                j = wnd["at"]
                bb, ff = base["decisions"][j][1], fk["decisions"][j][1]
                vb, vf = [v for v, _ in bb], [v for v, _ in ff]
                if set(bb) == set(ff):
                    k = "ORDER-ONLY"
                elif vb == vf:
                    k = "SUBJECT-ONLY"
                elif sorted(vb) == sorted(vf):
                    k = "VERB-ORDER+SUBJECT"
                else:
                    k = "VERB-SET"
                kinds[k] += 1
    good = [r for r in rows if r.get("ok")]
    real = [f for r in good for f in r["forks"]
            if f.get("status") in ("DIVERGED", "RECONVERGED")]
    div = [f for f in real if not f["reconverged"]]
    out = dict(mode=mode, chunk=[a, b], n_cases_ok=len(good), n_cases_failed=len(rows) - len(good),
               probed=sum(r["n_forks"] for r in good),
               no_live_window=sum(r["n_no_live_window"] for r in good),
               inert=sum(r["n_inert"] for r in good),
               genuine=len(real), diverged=len(div), reconverged=len(real) - len(div),
               changed_slot_kinds=dict(kinds))
    json.dump(out, open(Path(__file__).parent / "runs" / f"wd_subj_{mode}_{a}_{b}.json", "w"),
              indent=1, default=str)
    print(f"(verb,subject) {mode}[{a}:{b}] cases {out['n_cases_ok']}/{len(rows)} probed "
          f"{out['probed']} nolive {out['no_live_window']} inert {out['inert']} genuine "
          f"{out['genuine']} DIVERGED {out['diverged']} kinds {out['changed_slot_kinds']}")
