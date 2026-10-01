"""`harness.aperture` — THE APERTURE RE-MEASUREMENT, RUN ON THE POPULATED REALM (plan position `★`).

**WHAT "APERTURE" MEANS HERE**, defined where it is invoked (`CLAUDE.md` §4): *the verbs open to a
person*, measured as a FUNNEL rather than as one number, because each stage is closed by a
different owner and a single count hides which one closed it:

    eligible   `person_side_eligible(p, row)` — §F1 clause 2, the PERSON-SIDE gate, read on the
               built world before the season runs
    formed     the verb appeared in `opening_set(p, v, q, fx)` at one of the person's own
               deliberations during the season
    offered    formed AND in `resolvable_verbs()` — `make_chooser`'s own `verbs=` filter, so the
               set the ranking actually sees
    attempted  an Act by this person with this verb reached the fold (`SeasonDriver.resolved`)
    executed   `corpus_run.attribute`'s `made`: the act's row's `emits:` Event is in the log
    refused    `corpus_run.attribute`'s `refused`: its `emits_on_refusal:` Event is in the log

**WHY IT EXISTS.** The plan's `★` names two gaps and fills neither
(`workplans/2026-09-18-governance-settlement-behaviour-plan_part2.md`, *"★ — APERTURE
RE-MEASUREMENT"*). Gap (1): nothing ran the POPULATED realm for formability or execution —
`corpus_run` and `register --requirements` score the 143-case corpus, and
`test_the_generic_remit_seats_every_office_and_unblocks_the_nine` says so in its own docstring.
This module is that instrument, and the plan makes building it the gate's first step. Gap (2): the
figures it is compared against are 2026-09-17 values; this re-takes them, it never re-cites them.

**THE FALSIFIER IT IS BUILT AGAINST** (the plan's own): *a single flat "N of 38 unformable"
reported — that is the category error `13b` exposed.* So nothing here reports one number over the
verb table. Every figure is per HOLDER, per SOURCE, per VERB or per aggregation RULE, and the
unformable set is split into the verbs NOBODY can form (a property of the row) and the verbs a
particular seat withholds (a property of the holder).

**THE CONTROL, AND WHY THESE ARE `harness.populated 1`'s NUMBERS AND NOT A LOOK-ALIKE'S.** The
measured arm runs the season through its own driver, because it has to watch the chooser and the
barrier. So every run also builds a SECOND world from the same seed and runs it through
`populated.run` — the owner, untouched — and `measure` reports whether the two end in the same
`World.content_hash()` with the same act count. Equal hashes mean the instrumentation observed the
season without moving it (`opening_set`, `assemble` and `aggregate_questions` are person-side and
pure, and this proves it rather than assuming it), and that the numbers below ARE the populated
season's. Claims by source are taken from the control arm's own `populated.run` output for the same
reason: that figure has one owner and this module does not re-count it.

**THE STR-4 ARM.** `RULINGS.yaml` STR-4 rests on *"distinct verbs reached is 28 under every
aggregation rule"*, measured as a static snapshot on `build_realm(0, 12)`. Here the same question is
asked AT EVERY REAL DELIBERATION of the season, on the identical person-side state: the person's
delivered `Question[]` is re-aggregated under every rule on `question_aggregation`, re-assembled and
re-opened. Only the shipped rule's answer reaches the chooser; the others are counterfactual, so the
rule is the only difference between the rows — no trajectory confound.

**WHAT THIS DOES NOT DO.** It grades nothing, pins nothing and is wired into no gate. Its output is a
measurement of one seeded season, re-runnable: `python -m engine.season.harness.aperture [seasons]
[seed]`.
"""

from __future__ import annotations

import sys
from collections import Counter, defaultdict

from ..data.rosters import CLAIM_SOURCES, QUESTION_AGGREGATION, QUESTION_SOURCES
from ..data.verbs import VERB_TABLE
from ..decision import (aggregate_questions, assemble, make_chooser, opening_set,
                        person_side_eligible)
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..queries import world_q
from ..state.ids import H, draw_factory
from . import governance_spine, populated
from . import probes as P
from .corpus_run import attribute


def seat_gated(row) -> bool:
    """Does this row's formability depend on a SEAT? True when one of its `eligibility:`
    alternatives is `remit:` — the one kind `person_side_eligible` admits on a holder's grant
    (`decision/options.py::_admitted_through`). Parsed exactly as that walk parses it."""
    return any(alt.partition(":")[0].strip() == "remit" for alt in row.eligibility)


def seats(w) -> dict:
    """`{person id: [office id, ...]}` — every live `hold` whose object is an OFFICE and whose
    subject is a person. A `hold` on a Record or a Rung is not a seat and is not counted."""
    out: dict = defaultdict(list)
    for t in w.tenures:
        if t.kind == "hold" and t.live and t.object in w.offices and t.subject in w.persons:
            out[t.subject].append(t.object)
    return dict(out)


def seat_depth(w, oid: str):
    """Depth of the office's rung below its root (`world_q.ancestry`, the one owner of the walk),
    or `None` for an office with no rung (`Office.rung` is optional, S6.2)."""
    rung = w.offices[oid].rung
    return None if rung is None else len(world_q.ancestry(w, rung)) - 1


def eligible(w) -> dict:
    """`{person id: frozenset(verb)}` — `person_side_eligible` over the WHOLE verb table, per
    person, on the built world. `_rehome()` first, because the driver runs it at every barrier
    before any person-side read and a Tenure still in `_unowned` would read as a seat not held."""
    w._rehome()
    return {pid: frozenset(v for v, row in VERB_TABLE.items() if person_side_eligible(p, row))
            for pid, p in w.persons.items()}


def instrumented_season(w, seasons: int) -> dict:
    """Run `seasons` seasons on `w` with the chooser and the question barrier WATCHED, never
    steered. The driver/chooser construction is `populated.run`'s, line for line, so the control
    in `measure` can compare the two worlds' hashes."""
    d = SeasonDriver(w)
    fx = w.fixtures
    foldable = resolvable_verbs()
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    real = make_chooser(fx, mint, verbs=foldable, draw=draw_factory(w.world_seed, lambda: w.tick))

    delivered: dict = {}                 # person id -> the Question[] this barrier handed them
    q_count: dict = defaultdict(Counter)  # source -> Counter(person id -> questions)
    base = d._questions_at_barrier

    def watched_barrier():
        qmap = base()
        for pid, qs in qmap.items():
            delivered[pid] = qs
            for q in qs:
                q_count[q.source][pid] += 1
        return qmap
    d._questions_at_barrier = watched_barrier

    shipped = fx.get("question_aggregation_rule")
    k_view = fx.get("view_k")
    formed: dict = defaultdict(set)
    per_rule: dict = defaultdict(list)   # rule -> [(referents, candidates, verbs formed)]
    mismatch = 0                          # deliberations where the re-aggregation != the real one

    def watched_choose(p, v, s, ask_budget):
        nonlocal mismatch
        q = getattr(v, "question", None)
        real_cands = opening_set(p, v, q, fx) if q is not None else []
        formed[p.id] |= {c.verb for c in real_cands}
        qs = delivered.get(p.id) or []
        for rule in QUESTION_AGGREGATION:
            q_r = aggregate_questions(qs, rule)
            if rule == shipped:
                if (q_r.id if q_r else None) != (q.id if q else None):
                    mismatch += 1
                cands = real_cands
            else:
                cands = opening_set(p, assemble(p, q_r, k_view), q_r, fx) if q_r else []
            per_rule[rule].append((len(q_r.referents) if q_r else 0, len(cands),
                                   frozenset(c.verb for c in cands)))
        return real(p, v, s, ask_budget)

    for _ in range(seasons):
        d.season(watched_choose, question=None, subsistence=P.SUBSIST,
                 contest_max_depth=fx.get("contest_max_depth"))

    attempted: dict = defaultdict(Counter)
    executed: dict = defaultdict(Counter)
    refused: dict = defaultdict(Counter)
    neither: Counter = Counter()
    both: Counter = Counter()
    refusal_kinds: dict = defaultdict(Counter)   # verb -> Counter(emits_on_refusal kind)
    for a, made, no in attribute(w, d, seasons):
        attempted[a.actor][a.verb] += 1
        if made:
            executed[a.actor][a.verb] += 1
        if no:
            refused[a.actor][a.verb] += 1
            refusal_kinds[a.verb].update(no)
        if made and no:
            both[a.verb] += 1
        if not (made or no):
            neither[a.verb] += 1
    return {"acts": len(d.resolved), "formed": dict(formed), "attempted": dict(attempted),
            "executed": dict(executed), "refused": dict(refused), "neither": dict(neither),
            "both": dict(both), "refusal_kinds": {v: dict(c) for v, c in refusal_kinds.items()},
            "questions": {s: dict(c) for s, c in q_count.items()}, "per_rule": dict(per_rule),
            "shipped_rule": shipped, "rule_mismatch": mismatch, "foldable": foldable,
            "hash": w.content_hash()}


def measure_world(build, seed: int = 0, seasons: int = 1) -> dict:
    """One world, both arms. `build(seed)` is called twice: once for the CONTROL, run through
    `populated.run` untouched, and once for the MEASURED arm, run through `instrumented_season`."""
    wc = build(seed)
    control = populated.run(seasons, seed, w=wc)
    w = build(seed)
    # ⚠ THE CAST IS READ BEFORE THE SEASON, NOT AFTER. A person removed mid-season (a `fight`
    # that kills) leaves `w.persons`, and the first cut of this function read it afterwards, so
    # the unseated count was one short of the persons whose eligibility it reported.
    persons = sorted(w.persons)
    held = seats(w)
    elig = eligible(w)
    depth = {oid: seat_depth(w, oid) for offs in held.values() for oid in offs}
    posts = {oid: w.offices[oid].post for offs in held.values() for oid in offs}
    granted = {pid: sorted({a for t in w.persons[pid].tenures
                            if t.kind == "hold" and t.live and t.object in w.offices
                            for a in t.granted_acts}) for pid in held}
    run = instrumented_season(w, seasons)
    return {"seed": seed, "seasons": seasons, "persons": persons, "survivors": len(w.persons),
            "seats": held, "depth": depth, "posts": posts, "granted": granted,
            "eligible": elig, **run,
            "control": {"acts": control["acts"], "claim_sources": control["claim_sources"],
                        "hash": wc.content_hash()}}


def measure(seed: int = 0, seasons: int = 1) -> dict:
    """The populated realm (`populated.build_realm`) and the thirteen-seat spine
    (`governance_spine.build`), each measured with its own control."""
    return {"verbs": sorted(VERB_TABLE), "resolvable": sorted(resolvable_verbs()),
            "realm": measure_world(populated.build_realm, seed, seasons),
            "spine": measure_world(governance_spine.build, seed, seasons)}


# ---------------------------------------------------------------------------------------------
# REPORTING. Everything below reads `measure`'s dict and prints; nothing below measures.


def deepest(m: dict, pid: str, verb: str) -> str:
    """The deepest funnel stage (holder, verb) reached, as the stage's initial; `r` when attempted
    and only refused; `-` when not eligible and never formed."""
    if m["executed"].get(pid, {}).get(verb):
        return "x"
    if m["attempted"].get(pid, {}).get(verb):
        return "r" if m["refused"].get(pid, {}).get(verb) else "a"
    if verb in m["formed"].get(pid, ()):
        return "o" if verb in m["foldable"] else "f"
    return "e" if verb in m["eligible"][pid] else "-"


def _control_line(m: dict) -> str:
    c = m["control"]
    same = c["hash"] == m["hash"] and c["acts"] == m["acts"]
    return (f"  CONTROL  populated.run acts {c['acts']} vs measured {m['acts']}; content_hash "
            f"{'EQUAL' if c['hash'] == m['hash'] else 'DIFFERENT'} -> "
            f"{'the instrument observed the season without moving it' if same else '⚠ THE INSTRUMENT PERTURBED THE RUN — every number below is suspect'}")


def report(res: dict) -> list:
    out = []
    verbs, foldable = res["verbs"], set(res["resolvable"])
    gated = [v for v in verbs if seat_gated(VERB_TABLE[v])]
    out.append(f"THE APERTURE — {len(verbs)} verb-table rows; the per-row, per-holder, per-source "
               f"figures below are never summed into one (the `★` falsifier)")
    out.append(f"\nRESOLVABLE (`resolvable_verbs()`): {len(foldable)} rows")
    out.append(f"  yes: {sorted(foldable)}")
    out.append(f"  no : {sorted(set(verbs) - foldable)}")
    out.append(f"\nSEAT-GATED ROWS (an `eligibility:` alternative is `remit:`): {gated}")
    for label in ("realm", "spine"):
        m = res[label]
        out.append("\n" + "=" * len(out[0]))
        out.append(f"{label.upper()} — seed {m['seed']}, {m['seasons']} season(s), "
                   f"{len(m['persons'])} persons at build ({m['survivors']} at the end), "
                   f"{len(m['seats'])} seated")
        out.append(_control_line(m))
        # THE FUNNEL'S OWN CONSISTENCY, reported rather than assumed (§0.1 pt 2): an act by a
        # person for a verb the chooser never offered them means an act entered the fold by a
        # route this instrument does not watch; a verb formed by a person not eligible for it at
        # build means their seats changed mid-season. Either would qualify every row below.
        stray = sum(1 for pid, c in m["attempted"].items() for v in c
                    if v not in m["formed"].get(pid, ()) or v not in m["foldable"])
        gained = sum(1 for pid, vs in m["formed"].items() for v in vs
                     if v not in m["eligible"].get(pid, ()))
        out.append(f"  FUNNEL  (person, verb) pairs attempted but never offered: {stray} · "
                   f"formed but not eligible at build: {gained}")
        nobody = sorted(v for v in verbs if not any(v in e for e in m["eligible"].values()))
        out.append(f"\n  UNFORMABLE FOR EVERY PERSON IN THIS WORLD (a property of the ROW): {nobody}")
        # -- per holder -------------------------------------------------------------------
        out.append("\n  PER HOLDER — seat, depth, grant; eligible of rows; unformable beyond the "
                   "row-level set above; then the seat-gated funnel")
        out.append("    legend: - not eligible · e eligible · f formed, not foldable · o offered "
                   "· a attempted · r refused only · x executed")
        # The header is padded by the SAME format the rows use below, so the columns line up.
        out.append(f"    {'':<15} {'':<24} " + " ".join(f"{v[:4]:>4}" for v in gated))
        for pid in sorted(m["seats"]):
            offs = m["seats"][pid]
            seat = "; ".join(f"{m['posts'][o][:18]}@{m['depth'][o]}" for o in offs)
            e = m["eligible"][pid]
            extra = sorted(set(verbs) - e - set(nobody))
            out.append(f"    {pid:<15} {seat:<24} " + " ".join(
                f"{deepest(m, pid, v):>4}" for v in gated))
            out.append(f"      grant {m['granted'][pid]} · eligible {len(e)} of {len(verbs)} · "
                       f"seat-withheld {extra or 'none'}")
        # -- non-holders, grouped by identical eligibility (the control group) --------------
        groups = Counter(m["eligible"][p] for p in m["persons"] if p not in m["seats"])
        out.append(f"\n  NOT SEATED — {sum(groups.values())} persons, "
                   f"{len(groups)} distinct eligible set(s)")
        for e, n in groups.most_common():
            out.append(f"    {n} persons: eligible {len(e)} of {len(verbs)}; not eligible "
                       f"{sorted(set(verbs) - e)}")
        # -- per verb ---------------------------------------------------------------------
        out.append("\n  PER VERB — persons eligible (seated/unseated) · persons formed · persons "
                   "offered · ACTS attempted · executed · refused · both (both columns matched: "
                   "two Events for `march`, ONE graded-loss Event for `tell` — see "
                   "`corpus_run.attribute`) · neither")
        seated = set(m["seats"])
        for v in verbs:
            el_s = sum(1 for p in seated if v in m["eligible"][p])
            el_u = sum(1 for p in m["persons"] if p not in seated and v in m["eligible"][p])
            fo = sum(1 for s in m["formed"].values() if v in s)
            of = fo if v in foldable else 0
            at = sum(c.get(v, 0) for c in m["attempted"].values())
            ex = sum(c.get(v, 0) for c in m["executed"].values())
            rf = sum(c.get(v, 0) for c in m["refused"].values())
            out.append(f"    {v:<16} {'R' if v in foldable else '.'}  elig {el_s:>3}/{el_u:<3} "
                       f"formed {fo:>3}  offered {of:>3}  att {at:>4}  ex {ex:>4}  ref {rf:>4}  "
                       f"both {m['both'].get(v, 0):>3}  neither {m['neither'].get(v, 0)}"
                       + (f"   refused as {m['refusal_kinds'][v]}" if v in m["refusal_kinds"]
                          else ""))
        # -- questions by source ----------------------------------------------------------
        out.append("\n  QUESTIONS BY SOURCE — delivered at barrier 2, summed over every round "
                   "(`questions_for`, via the driver's own projection)")
        for src in list(QUESTION_SOURCES) + sorted(set(m["questions"]) - set(QUESTION_SOURCES)):
            per = m["questions"].get(src, {})
            out.append(f"    {src:<14} {sum(per.values()):>6} questions · {len(per):>3} persons "
                       f"reached · {len(set(per) & seated):>3} of them seated"
                       + ("" if src in QUESTION_SOURCES else "   ⚠ NOT ON THE ROSTER"))
        # -- claims by source -------------------------------------------------------------
        cs = m["control"]["claim_sources"]
        out.append("\n  CLAIMS BY SOURCE — `populated.run`'s own figure, the control arm")
        for src in list(CLAIM_SOURCES) + sorted(set(cs) - set(CLAIM_SOURCES)):
            out.append(f"    {src:<20} {cs.get(src, 0):>6}"
                       + ("" if src in CLAIM_SOURCES else "   ⚠ NOT ON THE ROSTER"))
        # -- STR-4 ------------------------------------------------------------------------
        out.append(f"\n  PER AGGREGATION RULE, AT EVERY REAL DELIBERATION (shipped: "
                   f"{m['shipped_rule']}; re-aggregation mismatches against the real call: "
                   f"{m['rule_mismatch']})")
        reached = {}
        for rule in QUESTION_AGGREGATION:
            rows = m["per_rule"].get(rule, [])
            n = len(rows) or 1
            refs = sum(r for r, _, _ in rows)
            cands = [c for _, c, _ in rows]
            reached[rule] = frozenset().union(*(vs for _, _, vs in rows)) if rows else frozenset()
            out.append(f"    {rule:<15} deliberations {len(rows):>4} · referents/delib "
                       f"{refs / n:6.2f} · candidates/delib {sum(cands) / n:7.2f} "
                       f"(min {min(cands, default=0)}, max {max(cands, default=0)}) · "
                       f"candidates/referent {sum(cands) / (refs or 1):6.2f} · distinct verbs "
                       f"formed {len(reached[rule])} · of them foldable "
                       f"{len(reached[rule] & foldable)}")
        base = reached.get(m["shipped_rule"], frozenset())
        for rule in QUESTION_AGGREGATION:
            if rule != m["shipped_rule"]:
                out.append(f"      vs {m['shipped_rule']}: {rule} adds {sorted(reached[rule] - base)}"
                           f", loses {sorted(base - reached[rule])}")
    return out


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    seasons = int(argv[0]) if argv and argv[0].isdigit() else 1
    seed = int(argv[1]) if len(argv) > 1 and argv[1].isdigit() else 0
    print("\n".join(report(measure(seed, seasons))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
