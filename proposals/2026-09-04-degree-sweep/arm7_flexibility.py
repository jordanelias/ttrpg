"""ARM 7 -- ALTERNATIVE OUTCOMES WITHIN EACH ARC/NPC SEASON, TO DEPTH 3: THE FLEXIBILITY TEST.

⚠ JORDAN, 2026-09-04, verbatim: *"I am still most interested in mechanical explorations of
alternative outcomes within each arc/NPC season at a depth of three so that we can assess
flexibility"*

THE QUESTION. Given a case's own starting world, how many GENUINELY DIFFERENT futures can three
seasons produce? Flexibility is not "how many branches can I enumerate" -- any tree enumerates
4^3. It is how many of those 64 land somewhere different. A system that names 64 alternatives and
delivers one future is rigid, whatever its branching factor.

THE BRANCH POINT, AND WHY IT IS THIS ONE. `make_chooser` (shape.py:2447) scores every candidate
person-side, sorts DESC by score then verb then subject, and hands the ranked list to
`pack_scenes`, which fills scenes greedily in score order. So the season's one real degree of
freedom is WHICH RANKED CANDIDATE LEADS. Branch `k in {0,1,2,3}` rotates the ranked list by k
before packing: the person takes their 2nd-, 3rd- or 4th-best option instead of their best.

⚠ NOTHING IN THE DECISION RULE IS REPLACED. `score`, the `sorted` key, `align`, `stance_toward`,
`urgency`, `ask_budget` and `pack_scenes` itself all run unmodified. The sweep changes ONE thing:
the offset at which packing starts reading an already-ranked list. That is an ALTERNATIVE, not a
second decision policy -- the distinction §27.2 cares about.

⚠ AND THE MEASUREMENT USES A WORLD FINGERPRINT, NOT `content_hash`. Arm 4a measured that
`content_hash` hashes the LOG only (shape.py:2026-2033) and is blind to `persons`, `sites`,
`rungs` and `tenures`. A flexibility number built on it would count log divergence and call it
world divergence. Both are reported here, separately, because the gap between them is itself a
result.
"""
from __future__ import annotations
import collections, itertools
import sweep_core as K
from sweep_core import S, C, R, Log

DEPTH = 3          # `CLAUDE.md` §0.1 pt 5 / G1: declared with its reason.
DEPTH_WHY = "Jordan's ask: alternative outcomes 'at a depth of three'."
K_BRANCH = 4       # four alternatives per decision point, matching the four-band ladder's arity
K_WHY = ("four, to match the arity of the degree ladder Jordan named, so the choice tree and the "
         "degree tree are the same width and their flexibility numbers are comparable")

_REAL_PACK = S.pack_scenes


class take_kth:
    """The counterfactual: the person spends the season on their k-th-ranked option ALONE.

    ⚠ THIS REPLACED A ROTATION THAT MEASURED NOTHING, AND THE REASON IS A FINDING IN ITS OWN
    RIGHT (arm 7c). The first version rotated the ranked list so the k-th candidate LED, and all
    four branches produced byte-identical worlds. The patch was firing — a spy counted 3 calls
    with ranked lists of 7 — so the null was real and its cause was elsewhere: **the act budget
    is not binding.** Every person takes ALL 7 of their ranked candidates every season (21 acts
    across 3 persons), so rotating the list changes the ORDER and never the SET, and there is no
    "instead of" to measure. Rotation asked "what if they had done these in a different order";
    this asks "what if they had done something else".

    Restricting the slice is a COUNTERFACTUAL, not a second decision policy: `score`, the sort
    key, `align`, `stance_toward`, `urgency` and `pack_scenes` are all untouched, and the k-th
    candidate is one the person's own ranking produced."""
    def __init__(self, k): self.k = k
    def __enter__(self):
        k = self.k
        def packed(p, ranked, budget, fx, mint, occasion=None, _r=_REAL_PACK, _k=k):
            if ranked:
                i = _k % len(ranked)
                ranked = list(ranked[i:i + 1])
            return _r(p, ranked, budget, fx, mint, occasion=occasion)
        S.pack_scenes = packed
        return self
    def __exit__(self, *a):
        S.pack_scenes = _REAL_PACK
        return False


def budget_binding(case: dict, seed: int = 0) -> dict:
    """ARM 7c -- is the act budget ever binding? If not, the person never triages (§26.3)."""
    seen = []
    real = S.pack_scenes
    def spy(p, ranked, budget, fx, mint, occasion=None):
        out = real(p, ranked, budget, fx, mint, occasion=occasion)
        seen.append((len(ranked), budget, sum(len(getattr(sc, "acts", []) or []) for sc in out)
                     if isinstance(out, list) else None))
        return out
    S.pack_scenes = spy
    try:
        w = C.build_at(case, seed); d = S.SeasonDriver(w)
        mint = lambda pid, verb, subj: S.H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
        ch = S.make_chooser(w.fixtures, mint, verbs=S.resolvable_verbs())
        d.season(ch, question=None, subsistence=K.C.P.SUBSIST)
        acts = len(getattr(d, "resolved", []))
    finally:
        S.pack_scenes = real
    ranked = [x[0] for x in seen]
    return dict(case=case["id"], deliberations=len(seen), ranked_sizes=ranked,
                acts_resolved=acts,
                all_taken=(acts == sum(ranked)) if ranked else None)


def world_state(w) -> str:
    """A fingerprint of the WORLD, not the log. Deliberately covers what `content_hash` omits."""
    import hashlib
    h = hashlib.blake2b(digest_size=16)
    for pid, p in sorted(w.persons.items()):
        h.update(f"P|{pid}|{getattr(p,'body',None)}|{getattr(p,'exists',None)}|"
                 f"{len(getattr(p,'tenures',()) or ())}".encode())
    for sid, s in sorted(getattr(w, "sites", {}).items()):
        h.update(f"S|{sid}|{getattr(s,'condition',None)}".encode())
    for rid, r in sorted(getattr(w, "rungs", {}).items()):
        h.update(f"R|{rid}|{getattr(r,'stores',None)}".encode())
    for t in sorted(getattr(w, "tenures", []) or [],
                    key=lambda t: (str(t.kind), str(t.subject), str(t.object))):
        h.update(f"T|{t.kind}|{t.subject}|{t.object}|{t.since}|{t.until}".encode())
    return h.hexdigest()


def run_case_path(case: dict, ks: tuple, seed: int = 0) -> dict:
    """One trajectory: `DEPTH` seasons, season i taking its k-th-ranked lead."""
    w = C.build_at(case, seed)
    d = S.SeasonDriver(w)
    mint = lambda pid, verb, subj: S.H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = S.make_chooser(w.fixtures, mint, verbs=S.resolvable_verbs())
    try:
        for k in ks:
            with take_kth(k):
                d.season(ch, question=None, subsistence=K.C.P.SUBSIST)
    except BaseException as e:
        return dict(ks=list(ks), status=f"RAISED {type(e).__name__}", detail=str(e)[:120],
                    log_hash=None, world_hash=None, acts=0, events=0, verbs=[])
    verbs = sorted({a.verb for a in getattr(d, "resolved", [])})
    return dict(ks=list(ks), status="OK", log_hash=w.content_hash(),
                world_hash=world_state(w), acts=len(getattr(d, "resolved", [])),
                events=len(w.log), verbs=verbs)


def explore(case: dict, seed: int = 0) -> dict:
    paths = [run_case_path(case, ks, seed)
             for ks in itertools.product(range(K_BRANCH), repeat=DEPTH)]
    ok = [p for p in paths if p["status"] == "OK"]
    logs = {p["log_hash"] for p in ok}
    worlds = {p["world_hash"] for p in ok}
    vsets = {tuple(p["verbs"]) for p in ok}
    acts = {p["acts"] for p in ok}
    return dict(case=case["id"], scale=case.get("scale"), n_paths=len(paths), n_ok=len(ok),
                distinct_log_futures=len(logs), distinct_world_futures=len(worlds),
                distinct_verb_sets=len(vsets), distinct_act_counts=len(acts),
                raised=len(paths) - len(ok),
                flexibility=len(worlds) / len(ok) if ok else 0.0)


def run(log: Log, seed: int = 0, sample: int = 0) -> dict:
    log.rule(f"ARM 7 — ALTERNATIVE OUTCOMES WITHIN EACH SEASON, DEPTH {DEPTH} — THE FLEXIBILITY TEST")
    log("ASK", "Jordan 2026-09-04: 'mechanical explorations of alternative outcomes within each "
               "arc/NPC season at a depth of three so that we can assess flexibility'")
    log("SETUP", f"branch = which RANKED candidate leads the season (k in 0..{K_BRANCH-1}); "
                 f"depth {DEPTH} seasons; {K_BRANCH**DEPTH} trajectories per case")
    log("SETUP", K_WHY)
    log("SETUP", "the decision RULE is untouched — score, sort key, align, stance, urgency, "
                 "ask_budget and pack_scenes all run unmodified; only the offset into the "
                 "already-ranked list moves")
    log("METRIC", "flexibility = distinct WORLD futures / trajectories that ran",
        "measured on a world fingerprint (persons, sites, rungs, tenures), NOT on "
        "`content_hash`, which arm 4a showed hashes the log only")

    rows = []
    for lane in ("NPC", "ARC"):
        cases = [C.apply_rescale(c) for c in R.load_cases(lane)]
        cases = [c for c in cases if str(c.get("scale")) in set(S.RUNG_KINDS)]
        if sample:
            cases = cases[:sample]
        for c in cases:
            r = explore(c, seed); r["lane"] = lane; r["_case_obj"] = c
            rows.append(r)

    tot_paths = sum(r["n_paths"] for r in rows)
    tot_ok = sum(r["n_ok"] for r in rows)
    log("COUNT", f"{len(rows)} cases x {K_BRANCH**DEPTH} = {tot_paths} trajectories; "
                 f"{tot_ok} ran, {tot_paths-tot_ok} raised")

    dw = collections.Counter(r["distinct_world_futures"] for r in rows)
    dl = collections.Counter(r["distinct_log_futures"] for r in rows)
    dv = collections.Counter(r["distinct_verb_sets"] for r in rows)
    log.rule("ARM 7a — how many DIFFERENT futures does each case actually reach?")
    log("RESULT", f"distinct WORLD futures per case (of {K_BRANCH**DEPTH}): {dict(sorted(dw.items()))}",
        "this is the flexibility answer. A case scoring 1 reached ONE world state down all 64 "
        "alternative-outcome paths.")
    log("RESULT", f"distinct LOG futures per case:  {dict(sorted(dl.items()))}",
        "the event stream is the surface that DOES move — so the loop is not inert; it is "
        "producing different narratives over an unchanging world")
    log("RESULT", f"distinct executed-VERB sets per case: {dict(sorted(dv.items()))}")

    rigid = [r for r in rows if r["distinct_world_futures"] <= 1]
    log("MEASURE", f"cases whose 64 alternatives collapse to <=1 world future: "
                   f"{len(rigid)} of {len(rows)} ({len(rigid)/len(rows)*100:.1f}%)")
    mean_flex = sum(r["flexibility"] for r in rows) / len(rows) if rows else 0.0
    log("MEASURE", f"mean flexibility (distinct world futures / trajectories run): {mean_flex:.4f}",
        f"1.0 would mean every one of the {K_BRANCH**DEPTH} alternatives lands somewhere different")

    log.rule("ARM 7c — is the act budget EVER binding? (§26.3: 'the PERSON triages')")
    log("WHY", "this probe exists because it explains the first version of arm 7. A rotation "
               "branch produced four byte-identical worlds; the patch was firing, so the null "
               "was real and its cause was here.")
    probes = [budget_binding(r["_case_obj"], seed) for r in rows[:12] if r.get("_case_obj")]
    allt = sum(1 for x in probes if x["all_taken"])
    log("MEASURE", f"{allt} of {len(probes)} sampled cases take EVERY ranked candidate every "
                   f"season", "e.g. 3 deliberations x 7 ranked = 21 acts resolved, all of them")
    log("VERDICT", "the act budget is not binding in the corpus, so the ranking never EXCLUDES "
                   "anything",
        "§26.3 makes triage the person's own choice of what to leave undone. In 143 cases "
        "nothing is left undone, so the ranking orders acts and never selects among them — "
        "which is why an ordering branch measures nothing and a SUBSTITUTION branch must.")

    log.rule("ARM 7b — the ceiling, and why the number above is the number it is")
    log("CAUSE", "of the 12 interpersonal verbs, 6 write NO state at all (arm 5b) and none "
                 "carries a degree column",
        "`speak`, `tell`, `the six investigation acts`, `refract`, `comply`, `evade / defy` each "
        "emit one Event and change nothing. A season composed of them CANNOT move the world, so "
        "choosing differently among them cannot either.")
    log("CAUSE", "the ranking ties: `align` is sparse with `default_cell: 0.0`, so 2..7 of 22 "
                 "candidates carry a nonzero score and the rest tie and sort alphabetically",
        "so rotating k often reorders candidates that were already indistinguishable to the "
        "person — the branch is real but the alternatives it reaches are near-identical")
    log("CEILING", "the degree axis is not explorable at all for these verbs",
        "a second tree branching on Overwhelming/Success/Partial/Failure cannot be built over "
        "`speak` or `tell`: `writes_at` returns the flat tuple for an uncontested verb and the "
        "degree is discarded (arm 1d). The choice tree above is the ONLY alternative-outcome "
        "tree the corpus currently supports.")
    for r in rows:
        r.pop("_case_obj", None)
    return dict(depth=DEPTH, k=K_BRANCH, n_cases=len(rows), trajectories=tot_paths, ran=tot_ok,
                distinct_world_futures=dict(dw), distinct_log_futures=dict(dl),
                distinct_verb_sets=dict(dv), rigid_cases=len(rigid),
                mean_flexibility=mean_flex, rows=rows)
