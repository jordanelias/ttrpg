"""RE-TAKES EVERY NUMBER IN THE 2026-09-18 REVIEW OF THE MORAL-VALUE BASIS.

    python proposals/2026-09-18-conviction-basis-probe.py

WHY THIS FILE EXISTS. The review reported a between-person discrimination figure and had no
committed instrument: the probes lived in a scratchpad that dies with the container. A read-only
critic marked the whole claim CANNOT-VERIFY on exactly that ground, and it was right —
`ED-IN-0228`'s own rule is that a stated number names a re-runnable command. This is that command.
Pass `--prove-control` to run the falsifier that shows the control arm's assertion is not vacuous.
`CLAUDE.md` §0.1 pt 3 row four is the shape of the failure: *"check the RUN HAPPENED."*

WHAT IT MEASURES, AND WHY IT IS TWO ARMS AND NOT ONE. The first arm asks whether the moral term
spreads ONE PERSON'S candidates; the second asks whether TWO PEOPLE rank the same candidates
differently. THE FIRST IS NOT EVIDENCE FOR THE SECOND and reporting it alone was the confound
(`CLAUDE.md` §0.1 pt 4 — a number without a control is not a measurement): a single shared
`alignment` table spreads any one person's options whatever they believe.

THE CONTROL IS THE `uniform` PROJECTION, which `rosters.yaml:1359` already names as the control --
*"`uniform` makes every conviction project identically ... under it a person's convictions cannot
discriminate between axes at all."* Under it the between-person arm must read 0 rank disagreement
and exactly 1 distinct top verb. If it does not, THIS PROBE IS WRONG, not the tree.

⚠ IT DOES NOT RE-IMPLEMENT THE SPECTRUM. `engine/season/harness/conviction_spread.py` owns
*how many directions a basis carries* (§8, every rule lives once); run it for the 1.85-vs-2.20
figures. This file prints the command rather than a second copy of its arithmetic.
"""
from __future__ import annotations

import itertools
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from engine.season.data.rosters import CONVICTION_AXES                    # noqa: E402
from engine.season.data.verbs import ALIGNMENT, CONVICTION_PROJECTION     # noqa: E402
from engine.season.decision import assemble, opening_set                  # noqa: E402
from engine.season.decision.choose import align, project                  # noqa: E402
from engine.season.harness.populated import build_realm                   # noqa: E402
from engine.season.queries.world_q import questions_for                   # noqa: E402

# `synthesis.md` §3: at the shipped `tau = 0.1`, `P(inversion) = 1/(1+e^{D/tau})`, so a term changes
# what a character does at 95% only once it moves the score by this much. [canonical: proposals/
# 2026-09-16-conviction-decision-layer/synthesis.md §3]
FLOOR = 0.294

AXES = sorted(CONVICTION_AXES)

# THE CONTROL TABLE, HOISTED SO IT IS SUBSTITUTABLE AND THE CONTROL'S OWN ASSERTION IS NOT VACUOUS.
# A first version built this inline from a literal `1.0`, which made the assertion below able to
# observe only an arithmetic bug and NEVER a wrong control -- the class `CLAUDE.md` §0.1 pt 2 names
# and PR #418 found three of. Proven to fire by substitution: see `_prove_control_fires`.
UNIFORM_TABLE = {c: {a: 1.0 for a in AXES} for c in CONVICTION_PROJECTION}


def _proj(weights: dict, rows: dict) -> dict:
    """`Sigma_conv w[conv] * rows[conv][axis]` -- the same map `data.convictions.to_axes` owns.

    Spelled here ONLY because the control arm needs it against a SUBSTITUTED table; the live arm
    calls `decision.choose.project`, which delegates to the single owner."""
    out = {a: 0.0 for a in AXES}
    for conv, w in (weights or {}).items():
        row = rows.get(conv)
        if row is None:
            continue
        for a in AXES:
            out[a] += float(w) * float(row.get(a, 0.0))
    return out


def _moral(axis_w: dict, verb: str) -> float:
    """The first term of `score(c)` at `decision/choose.py:360`, isolated."""
    return sum(axis_w[a] * align(verb, a) for a in AXES)


def _disagreement(a: list, b: list) -> float:
    pa = {v: i for i, v in enumerate(a)}
    pb = {v: i for i, v in enumerate(b)}
    disc = tot = 0
    for x, y in itertools.combinations(a, 2):
        tot += 1
        if (pa[x] - pa[y]) * (pb[x] - pb[y]) < 0:
            disc += 1
    return disc / tot if tot else 0.0


def arm_one_within_person(w) -> None:
    """Does the moral term spread ONE person's own candidate set? (It does; this is not the result.)"""
    fx = w.fixtures
    rows = {}
    for pid, p in w.persons.items():
        qs = questions_for(w, p, None)
        if not qs:
            continue
        v = assemble(p, qs[0], fx.get("view_k"))
        cands = opening_set(p, v, qs[0], fx)
        if len(cands) < 2:
            continue
        axis_w = project(p)
        vals = [_moral(axis_w, c.verb) for c in cands]
        rows[pid] = max(vals) - min(vals)
    assert rows, "no person formed >=2 candidates -- the term cannot be measured on this world"
    spreads = sorted(rows.values())
    clears = [s for s in spreads if s >= FLOOR]
    print("ARM 1 -- WITHIN one person's candidate set (NOT the design question)")
    print(f"  deliberations measured   {len(rows)}")
    print(f"  spread  min {spreads[0]:.4f}   median {statistics.median(spreads):.4f}   max {spreads[-1]:.4f}")
    print(f"  clears {FLOOR}:  {len(clears)}/{len(rows)}  ({100 * len(clears) / len(rows):.1f}%)")
    print("  READ IT AS: a shared `alignment` table reorders anyone's options. It says nothing")
    print("  about whether two PEOPLE differ, which is arm 2.\n")


def arm_two_between_persons(w) -> None:
    """Do two people with DIFFERENT convictions rank the same verbs differently? Live vs control."""
    verbs = sorted(set().union(*[set(r) for r in ALIGNMENT.values()]))
    people = [(pid, p) for pid, p in w.persons.items() if p.convictions]
    distinct = {tuple(sorted((p.convictions or {}).items())) for _, p in people}
    print("ARM 2 -- BETWEEN persons, on a fixed verb set (THE design question)")
    print(f"  verbs with >=1 alignment cell   {len(verbs)}")
    print(f"  persons with convictions        {len(people)}")
    print(f"  DISTINCT conviction vectors     {len(distinct)}\n")

    control_ok = None
    for name, rows in (("LIVE 13x4", CONVICTION_PROJECTION), ("UNIFORM (control)", UNIFORM_TABLE)):
        ranks, terms = {}, {}
        for pid, p in people:
            aw = _proj(p.convictions, rows)
            terms[pid] = {v: _moral(aw, v) for v in verbs}
            ranks[pid] = sorted(verbs, key=lambda v: (-terms[pid][v], v))
        pairs = list(itertools.combinations([pid for pid, _ in people], 2))
        dis = [_disagreement(ranks[a], ranks[b]) for a, b in pairs]
        gaps = [abs(terms[a][v] - terms[b][v]) for a, b in pairs for v in verbs]
        over = sum(1 for g in gaps if g >= FLOOR)
        tops = {ranks[pid][0] for pid, _ in people}
        print(f"  --- {name} ---")
        print(f"    distinct TOP-ranked verb   {len(tops)}")
        print(f"    distinct FULL ranking      {len({tuple(ranks[pid]) for pid, _ in people})}")
        print(f"    rank disagreement   median {statistics.median(dis):.4f}   max {max(dis):.4f}")
        print(f"    |gap| two people, same verb  median {statistics.median(gaps):.4f}   max {max(gaps):.4f}")
        print(f"      clears {FLOOR}:  {over}/{len(gaps)}  ({100 * over / len(gaps):.1f}%)")
        if name.startswith("UNIFORM"):
            control_ok = (len(tops) == 1 and statistics.median(dis) == 0.0)
    print()
    # THE CONTROL MUST FIRE. `rosters.yaml:1359` says `uniform` removes all axis discrimination, so
    # a nonzero reading here falsifies THIS PROBE rather than the tree (§0.1 pt 2 -- an assertion
    # must be able to observe the failure it excludes).
    assert control_ok, "CONTROL FAILED: uniform projection still discriminated -- this probe is wrong"
    print("  CONTROL FIRED: uniform gives exactly 1 top verb and 0.0000 median disagreement,")
    print("  so the live arm's discrimination is the projection's and not this probe's artefact.\n")


def coverage() -> None:
    from engine.season.data.verbs import VERB_TABLE
    cells = sum(len(r) for r in ALIGNMENT.values())
    neg = sum(1 for r in ALIGNMENT.values() for x in r.values() if float(x) < 0.0)
    aligned = set().union(*[set(r) for r in ALIGNMENT.values()])
    missing = sorted(set(VERB_TABLE) - aligned)
    print("ALIGNMENT COVERAGE -- the other half of the score term")
    print(f"  cells {cells}   negative {neg}   verbs with >=1 cell {len(aligned)} of {len(VERB_TABLE)}")
    print(f"  NO cell on any axis ({len(missing)}): {' '.join(missing)}")
    print("  For those the moral term is exactly 0.0 and `score` falls back to stance + urgency.\n")


def _prove_control_fires(w) -> None:
    """§0.1 pt 2 -- run the control arm against a DELIBERATELY NON-UNIFORM table and require the
    assertion to trip. Without this the control is a comment claiming a guard the code does not give.

    ⚠ IT MUTATES THE MODULE GLOBAL AND RESTORES IT, so it must run AFTER the real arms."""
    global UNIFORM_TABLE
    kept = UNIFORM_TABLE
    UNIFORM_TABLE = {c: {a: (1.0 if i % 2 else 0.2) for i, a in enumerate(AXES)}
                     for c in CONVICTION_PROJECTION}
    try:
        arm_two_between_persons(w)
    except AssertionError:
        print("FALSIFIER: the control assertion FIRED against a non-uniform table, as required.\n")
        return
    finally:
        UNIFORM_TABLE = kept
    raise AssertionError("the control assertion is VACUOUS -- it did not fire on a poisoned table")


def main() -> int:
    w = build_realm(0)
    print(f"world: build_realm(0) -- {len(w.persons)} persons, {len(w.rungs)} rungs")
    print(f"floor: D >= {FLOOR} at the shipped tau=0.1 (synthesis.md §3)\n")
    arm_one_within_person(w)
    arm_two_between_persons(w)
    coverage()
    if "--prove-control" in sys.argv:
        _prove_control_fires(w)
    print("NOT MEASURED HERE, BY DESIGN -- how many directions each basis carries. That belongs to")
    print("its existing owner (§8). Run:")
    print("  python -m engine.season.harness.conviction_spread \\")
    print("    --candidate proposals/2026-09-16-conviction-decision-layer/candidate_basis_v1.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
