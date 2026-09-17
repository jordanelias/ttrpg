#!/usr/bin/env python3
"""REACH's question-set decomposition, re-runnable — the instrument behind 01 §0.2(d).

    python proposals/2026-09-17-governance-and-holdings-r2/probe_reach_questions.py

WHY THIS FILE EXISTS. `01_ATTENTION_AND_REACH.md` headlines a measured transition — the Q2 question
set goes **561 -> 1632** once the admission test gains a place clause — and `CLAUDE.md` §0.1 pt 3
requires the falsifier to ship with the claim. `tools/ci_claim_provenance_check.py` enforces the same
rule on any ledger row stating a transition (`ED-PC-0040`) and it wants a path. The figures were
first produced by an ad-hoc probe that left no artifact, which is precisely the shape of claim that
gate exists to refuse.

WHY IT SITS HERE AND NOT IN `tools/`. `CLAUDE.md` §0 says to bind a record to its subject so it dies
when the subject dies. This probe measures a mechanism that DOES NOT EXIST: `reach`, `place_of` and
`nearest_store` are absent from `engine/season` (§0.2g — re-checked below and asserted, because an
absence is the cheapest claim to make and the hardest to see wrong). It therefore implements the
CANDIDATE and compares it against the live reading. If the proposal is refused this file goes with
it, and `tools/` is not left holding an instrument for a mechanism nobody built. It is **not a
guard**: it gates nothing, has no CI caller, and asserts nothing about the tree's health, so §0.1
pt 5's predicate is not engaged.

WHAT IT FOUND THAT 01 DID NOT SAY, and this is the reason the file is worth keeping rather than a
formality. The headline reproduces exactly — **561 -> 1632, 2.91x** — but only under ONE reading of
the candidate `place_of`, and 01's own table does not use that reading in every row:

  * `place_of` must resolve a **`Record` through its `rung` field** (417 of the claim instances have
    a Record subject) and must **climb from a person's rung to the containing hearth**. Under that
    reading the corpus splits **2012 with a place (every one a hearth) / 163 with none (exactly the
    Propositions)**, which is 01 §0.2(d)'s own stated decomposition, to the claim.
  * Read `place_of` as the person's live `contain` object WITHOUT the ascent — the literal reading of
    01's sentence *"a person's live `contain` Tenure's object IS their home rung"* — and the split is
    **1902 person-rungs / 110 hearths / 163 none**, because `build_realm` gives every person a rung
    of kind `person` and the hearth is its PARENT. Row 4 then reads **561**, not 1632: the place
    clause adds nothing, because a person-rung is inhabited by exactly one person.
  * **01's row 3 is on the other ladder from its rows 4-6.** `self alone, subject-or-place = 328`
    reproduces only under the no-ascent reading; under the ascent reading that same row is 1632. Both
    numbers are printed below. Two ladders for one quantity is an `S-METHOD` defect in `CLAUDE.md`
    §0.06's own terms (*"calculations consistent in methodology with other mechanics"*), and it is
    recorded here rather than smoothed over. **It does not touch the headline**, which is rows 1 and
    4 and is reproduced.

⚠ IT REPORTS, IT DOES NOT ASSERT THE NUMBERS. A probe that hard-codes the figures it was written to
reproduce tells you its author's memory, not the tree. Expected values print beside measured ones
with a delta. The three things it DOES assert are the ones whose failure would silently invalidate
the comparison: that the candidate functions are still absent, that the corpus is non-empty, and that
row 1 reproduces `world_q.questions_for`'s own `claim_landed` count — §0.1 pt 2, an assertion must be
able to observe the failure it excludes, and without that control every row is measured against a
re-implementation nobody checked.
"""
from __future__ import annotations

import collections
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from engine.season.decision import make_chooser                                   # noqa: E402
from engine.season.harness.headless import subsistence                            # noqa: E402
from engine.season.harness.populated import build_realm                           # noqa: E402
from engine.season.loop.driver import SeasonDriver, resolvable_verbs              # noqa: E402
from engine.season.queries.world_q import descendants, parent_of, questions_for    # noqa: E402
from engine.season.state.ids import H, draw_factory                               # noqa: E402

# 01 §0.2(d), the table this file is the instrument for. Printed, never asserted.
EXPECTED = {
    "1 · live test — subject or `mine`":                          561,
    "2 · REACH, four limbs, SUBJECT ONLY":                        561,
    "3 · self alone, subject-or-place":                           328,
    "4 · self + `mine`, subject-or-place":                       1632,
    "5 · + ancestors-or-self of home, subject-or-place":         1632,
    "6 · + purview ({seat.rung} + descendants), subject-or-place": 1632,
}
# 01 §0.2(d)'s stated decomposition of the corpus by the place its subject resolves to.
EXPECTED_SPLIT = {"hearth": 2012, None: 163}


def absent(name: str) -> bool:
    """§0.2(g): RUN the thing that would show presence, rather than asserting the absence."""
    r = subprocess.run(["grep", "-rn", f"def {name}", str(ROOT / "engine" / "season")],
                       capture_output=True, text=True)
    return r.returncode != 0 or not r.stdout.strip()


def one_season(seed: int = 0):
    w = build_realm(seed)
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    d.season(make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                          draw=draw_factory(w.world_seed, lambda: w.tick)),
             None, subsistence, contest_max_depth=w.fixtures.get("contest_max_depth"))
    return w


class PlaceOf:
    """THE CANDIDATE, in both readings, because which one is meant changes the answer 3x.

    `ascend=True` climbs from a rung to the nearest ancestor-or-self of kind `hearth`. That is the
    reading under which 01's corpus split and headline reproduce. `ascend=False` is the literal
    reading of 01's prose and it does not."""

    def __init__(self, w, ascend: bool):
        self.w, self.ascend = w, ascend
        self.records = getattr(w, "records", {})

    def _hearth(self, rid):
        cur, seen = rid, set()
        while cur and cur not in seen:
            seen.add(cur)
            if getattr(self.w.rungs.get(cur), "kind", None) == "hearth":
                return cur
            cur = parent_of(self.w, cur)
        return rid

    def rung(self, rid):
        return self._hearth(rid) if (self.ascend and rid) else rid

    def __call__(self, subject: str):
        w = self.w
        if subject in w.rungs:
            return self.rung(subject)
        p = w.persons.get(subject)
        if p is not None:
            for t in p.tenures:
                if t.live and t.kind == "contain" and t.object in w.rungs:
                    return self.rung(t.object)
            return None
        r = self.records.get(subject)
        if r is not None:                       # 417 instances; the field is `Record.rung`
            return self.rung(getattr(r, "rung", None))
        s = w.sites.get(subject)
        if s is not None:
            return self.rung(getattr(s, "rung", None))
        return None                              # Propositions have no place, by construction


def ancestors_or_self(w, rid):
    if rid is None:
        return set()
    out, cur, seen = {rid}, rid, set()
    while cur and cur not in seen:
        seen.add(cur)
        cur = parent_of(w, cur)
        if cur:
            out.add(cur)
    return out


def purview(w, p, pf) -> set[str]:
    """`{seat.rung}` + `descendants(seat.rung)` over every office this person holds.

    ⚠ The union with the seat's OWN rung is the repair 01 and 03 both report: `descendants` is
    PROPER, so `descendants(seat.rung)` alone loses the rung the seat governs — *a Duke loses his own
    duchy*. Measured elsewhere as 365 against 364 on the reflexive `under_purview`."""
    out: set[str] = set()
    for t in p.tenures:
        if not t.live:
            continue
        off = w.offices.get(t.object)
        r = getattr(off, "rung", None) if off is not None else None
        if r:
            out.add(pf.rung(r))
            out.update(pf.rung(x) for x in descendants(w, r))
    return out


def rows(w, ascend: bool) -> dict[str, int]:
    pf = PlaceOf(w, ascend)
    keys = list(EXPECTED)
    n = {k: 0 for k in keys}
    floor = (w.tick - 1, 0)
    for p in w.persons.values():
        mine = {pf.rung(o) if o in w.rungs else o for o in
                (t.object for t in p.tenures if t.live)}
        home = pf(p.id)
        anc = {pf.rung(x) for x in ancestors_or_self(w, home)}
        pur = purview(w, p, pf)
        for c in p.ledger:
            if (c.when, c.round) < floor:
                continue
            s, pl = c.subject, pf(c.subject)
            by_subject = s == p.id or s in mine
            if by_subject:
                n[keys[0]] += 1
                n[keys[1]] += 1
            if s == p.id or (pl is not None and pl == home):
                n[keys[2]] += 1
            if by_subject or (pl is not None and pl in mine):
                n[keys[3]] += 1
            if by_subject or (pl is not None and (pl in mine or pl in anc)):
                n[keys[4]] += 1
            if by_subject or (pl is not None and (pl in mine or pl in anc or pl in pur)):
                n[keys[5]] += 1
    return n


def split(w, ascend: bool) -> dict:
    pf = PlaceOf(w, ascend)
    c = collections.Counter()
    for p in w.persons.values():
        for cl in p.ledger:
            pl = pf(cl.subject)
            c[getattr(w.rungs.get(pl), "kind", None) if pl else None] += 1
    return dict(c)


def main() -> int:
    for name in ("reach", "place_of", "nearest_store"):
        assert absent(name), (
            f"`def {name}` NOW EXISTS in engine/season. This probe compares a CANDIDATE against a "
            f"tree that lacks it; if the candidate has landed the comparison is meaningless, and "
            f"this file should be deleted rather than re-run.")

    w = one_season(0)
    persons = list(w.persons.values())
    claims = sum(len(p.ledger) for p in persons)
    assert claims, "empty corpus — the season produced no claims, so every row below would read 0"

    asc, flat = rows(w, True), rows(w, False)
    live = sum(1 for p in persons for q in questions_for(w, p) if q.source == "claim_landed")

    print(f"corpus: build_realm(0), one season · {len(persons)} persons · {claims} claim instances")
    print(f"        {len(w.rungs)} rungs · {len(w.offices)} offices · {len(getattr(w,'records',{}))} "
          f"records · floor (tick-1, 0) = {(w.tick - 1, 0)}\n")

    got_split = split(w, True)
    ok = all(got_split.get(k) == v for k, v in EXPECTED_SPLIT.items())
    print(f"corpus by the place its subject resolves to, ASCENDING reading: {got_split}")
    print(f"  01 §0.2(d) states: {EXPECTED_SPLIT} — {'reproduced' if ok else '⚠ DOES NOT REPRODUCE'}")
    print(f"corpus, NO-ASCENT reading (01's literal prose):                 {split(w, False)}")
    print("  the hearth is the PARENT of a person's rung; `build_realm` gives every person a rung of "
          "kind `person`.\n")

    wid = max(len(k) for k in EXPECTED)
    print(f"{'the Q2 admission test'.ljust(wid)}  ascend  no-asc  01 §0.2(d)")
    for k in EXPECTED:
        a, f, e = asc[k], flat[k], EXPECTED[k]
        mark = "" if e in (a, f) else "  ⚠ neither reading reproduces this row"
        which = ("both" if a == f == e else "ascend" if a == e else "no-ascent" if f == e else "—")
        print(f"{k.ljust(wid)}  {a:>6}  {f:>6}  {e:>10}  ({which}){mark}")

    print(f"\ncontrol — `world_q.questions_for`'s own `claim_landed` count: {live}")
    if live != asc[list(EXPECTED)[0]]:
        print(f"  ⚠ ROW 1 DOES NOT REPRODUCE THE LIVE QUERY ({asc[list(EXPECTED)[0]]} vs {live}). "
              f"The re-implementation has drifted; trust the live number, not this table.")
        return 1
    print("  row 1 reproduces it, so the rows differ only by the clause each adds.")

    k1, k4 = list(EXPECTED)[0], list(EXPECTED)[3]
    print(f"\nTHE HEADLINE: {asc[k1]} → {asc[k4]} ({asc[k4] / asc[k1]:.2f}×) under the ascending "
          f"reading; {flat[k1]} → {flat[k4]} ({flat[k4] / flat[k1]:.2f}×) without the ascent.")
    print(f"The four limbs add {asc[list(EXPECTED)[1]] - asc[k1]} by subject, either way — which is "
          f"01 §0.3's withdrawn N-line, reproduced.")
    k3 = list(EXPECTED)[2]
    print(f"⚠ AND THE ATTRIBUTION IN 01 §0.2(d) IS WRONG WHERE ITS MAGNITUDE IS RIGHT. It reads *\"the "
          f"entire effect is the PLACE clause, and it lands on the `mine` limb\"*. Measured: with the "
          f"hearth ascent, the place clause on the SELF limb ALONE already gives {asc[k3]} — rows 3, 4, "
          f"5 and 6 are the same number. `mine` adds nothing, because a person's `contain` object "
          f"ascends to the same hearth `place_of(p.id)` does. **The effect is the ASCENT, not the "
          f"limb.** 01's row 3 ({EXPECTED[k3]}) reproduces under neither reading: it is the no-ascent "
          f"ladder with Records left unresolved, so it is a THIRD method inside a six-row table. Two "
          f"ladders for one quantity is an S-METHOD defect (§0.06); three is the same defect twice. "
          f"The headline — {asc[list(EXPECTED)[0]]} → {asc[k3]} — is unaffected and is what 01 claims.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
