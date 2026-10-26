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
    attempted  an Act by this person with this verb entered RESOLVE -- the ACT STORE (`w.acts`,
               read by `corpus_run.attempts`), which holds a contested act refused at admission
               that never reaches the fold (`SeasonDriver.resolved`)
    executed   `corpus_run.attempts`'s `made`: the act's row's `emits:` Event is in the log
    refused    `corpus_run.attempts`'s `refused`: its `emits_on_refusal:` Event is in the log
    graded     `corpus_run.graded_loss`: a LOST contest, whose refusal-kind Event is also an `emits:`
               kind and carries degree `Failure` -- counted in `both`, never a refusal in the sense
               of a failed `requires`

The CONTROL line still compares `populated.run`'s `acts` with `len(d.resolved)`, the fold set: the
two arms share that owner, and the act-store reading is a different quantity.

**WHY EACH REFUSAL REFUSED (REM-11).** `refused` says an act drew a refusal kind, not which clause
refused it. Four further blocks are read off the same run, each keyed on the ACT (`d.act_of`: Event
id -> Act, the driver's own map), never on a trace row's `act` column, which is unreliable for WRITE
and GAP rows:

    DECIDING READ     per verb, one reason per refused act: `clause:<name>` where the row keys
                      `emits_on_refusal` by clause (`VerbRow.refusals_by_clause`), else
                      `last-read <predicate>=<value>` (the LAST `Event.observed` read, which is not
                      always the one that decided -- `AllOf` reads past an UNKNOWN), `no-read` when
                      the Event carries none, `graded-loss` for a contest that ran and was lost
    POST-ADMISSION    a refusal Event whose every recorded read passed: `evaluate` replayed over the
                      Event's own `observed` (`_Replay`) returns True, so the act cleared its
                      `requires` and was refused at the counterparty or write clause
    NEVER EMITTED     `EMITTED_KINDS` together with the write matrix's `emits:` column, minus the kinds
                      in the log
    EMITTED KINDS     one count line per kind in the log: Events, and the distinct acts they came from

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

from ..data.matrix import MATRIX
from ..data.requires import UNKNOWN, binding_from_act, evaluate
from ..data.rosters import CLAIM_SOURCES, QUESTION_AGGREGATION, QUESTION_SOURCES
from ..data.verbs import COUNTERPARTY_CLAUSE, EMITTED_KINDS, VERB_TABLE, WRITE_CLAUSE
from ..decision import (aggregate_questions, assemble, make_chooser, opening_set,
                        person_side_eligible)
from ..gaps import Unspecified
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..queries import world_q
from ..state.ids import H, draw_factory
from . import governance_spine, populated
from . import probes as P
from .corpus_run import attempts, graded_loss, graded_losses, unrowed_acts


def seat_gated(row) -> bool:
    """Does this row's formability depend on a SEAT? True when one of its `eligibility:`
    alternatives is `remit:` — the one kind `person_side_eligible` admits on a holder's grant
    (`decision/options.py::_admitted_through`). Parsed exactly as that walk parses it."""
    kinds = [alt.partition(":")[0].strip() for alt in row.eligibility]
    return "remit" in kinds and "own" not in kinds


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


class _Replay:
    """A `reader` that answers `data.requires.evaluate` from the reads an Event RECORDED
    (`Event.observed`, a tuple of `Observation(subject, predicate, value)`), so the one evaluator
    can be asked again, after the fact, what the fold's own verdict was -- no second evaluator.
    A read the Event did not record is UNKNOWN."""

    def __init__(self, observed):
        self._seen = {(o.subject, o.predicate): o.value for o in observed}

    def read(self, subject, predicate):
        return self._seen.get((subject, predicate), UNKNOWN)


def _observed_of(event) -> tuple:
    """The reads the fold recorded on `event`. The ONE place the instrument reads
    `Event.observed`: the deciding read and the post-admission test both come through here."""
    return tuple(event.observed or ())


def read_label(obs, kind_stems=("exists", "stores")) -> str:
    """`predicate=value` for one `Observation`, as the DECIDING READ block prints it. The suffix of
    `exists:<Kind>` and `stores:<good>` names a KIND (`data/requires.py`: `Existence.kind`,
    `ScalarThreshold.scalar`) and stays; any other suffix is an entity id and is dropped, so a stem's
    reads pool across ids. A number prints as itself under `exists` and as `0` / `>0` elsewhere."""
    stem = obs.predicate.partition(":")[0]
    pred = obs.predicate if stem in kind_stems else stem
    v = obs.value
    if v is UNKNOWN:
        val = "UNKNOWN"
    elif isinstance(v, (bool, str)) or v is None:
        val = str(v)
    elif isinstance(v, (int, float)):
        val = (f"{v:g}" if stem == "exists" else "0" if v == 0 else ">0")
    else:
        val = type(v).__name__
    return f"{pred}={val}"


def _replayed(row, act, observed):
    """`evaluate`'s Verdict for `act` over its own recorded `observed`, or `None` when it cannot be
    asked: the row has no typed cell (a predicate row records no reads) or the Event recorded none."""
    if row.requires_typed is None or not observed:
        return None
    try:
        return evaluate(row.requires_typed, _Replay(observed), binding_from_act(act))
    except Unspecified:
        return None


def refusal_reading(w, d, rows) -> dict:
    """WHY EACH REFUSED ACT REFUSED. `rows` is `corpus_run.attempts(w, n)`; for each act whose
    `refused` is non-empty, its refusal-kind Events are found through `d.act_of` (Event id -> Act),
    never through a trace row. One reason per ACT, from its first refusal Event:

      `graded-loss`           `corpus_run.graded_loss`: the contest ran and was lost, not a refusal
      `clause:<name>`         the row keys `emits_on_refusal` by clause (`refusals_by_clause`): the
                              clause(s) whose kinds hold the Event's kind, narrowed to the one the
                              replayed verdict named (`Verdict.failed`), or, when every read passed,
                              to the write / counterparty clause
      `last-read <p>=<v>`     otherwise, the last `Event.observed` read (`read_label`)
      `no-read`               the Event recorded no read
      `no-event`              the act drew a refusal kind by `attempts`'s id rule but `d.act_of` holds
                              no Event of it for the act (an instrument defect if it is ever > 0)

    POST-ADMISSION: the replayed verdict over the Event's own reads is True -- every recorded read
    passed, so the act cleared its `requires` and the refusal fell at the counterparty or write
    clause. A refusal that records no read, or whose row has no typed cell, is never counted there.
    Returns `{"reasons": {verb: {reason: n}}, "post_admission": {verb: n}}`."""
    emitted: dict = defaultdict(list)
    for e in w.log:
        a = d.act_of.get(e.id)
        if a is not None:
            emitted[a.id].append(e)
    reasons: dict = defaultdict(Counter)
    post: Counter = Counter()
    for a, made, no in rows:
        if not no:
            continue
        row = VERB_TABLE[a.verb]
        evs = [e for e in emitted.get(a.id, ()) if e.kind in no]
        if not evs:
            reasons[a.verb]["no-event"] += 1
            continue
        if graded_loss(a, evs):
            reasons[a.verb]["graded-loss"] += 1
            continue
        obs = _observed_of(evs[0])
        verdict = _replayed(row, a, obs)
        passed = verdict is not None and verdict.value is True
        if passed:
            post[a.verb] += 1
        cands = [c for c, ks in row.refusals_by_clause.items() if evs[0].kind in ks]
        if verdict is not None and verdict.failed in cands:
            cands = [verdict.failed]
        elif passed:
            cands = [c for c in cands if c in (WRITE_CLAUSE, COUNTERPARTY_CLAUSE)] or cands
        if cands:
            reasons[a.verb]["clause:" + "|".join(cands)] += 1
        elif obs:
            reasons[a.verb]["last-read " + read_label(obs[-1])] += 1
        else:
            reasons[a.verb]["no-read"] += 1
    return {"reasons": {v: dict(c) for v, c in reasons.items()}, "post_admission": dict(post)}


def kind_census(w, d) -> dict:
    """The Event kinds of a world's log against the kinds declared. `declared` is `EMITTED_KINDS`
    (every kind some verb row emits, on success or refusal) together with the `emits:` column of
    the write matrix (`data/matrix.py::MATRIX`); `never` is `declared` minus the kinds in the log.
    `counts` is `{kind: {"events": n, "acts": distinct acts, "no_act": events with no act}}` over the
    log, the act of an Event being `d.act_of`'s (a MATTER or CALENDAR Event has none)."""
    declared = set(EMITTED_KINDS) | {k for m in MATRIX.values() for k in m.emits}
    events: Counter = Counter()
    no_act: Counter = Counter()
    acts: dict = defaultdict(set)
    for e in w.log:
        events[e.kind] += 1
        a = d.act_of.get(e.id)
        if a is None:
            no_act[e.kind] += 1
        else:
            acts[e.kind].add(a.id)
    return {"declared": len(declared), "never": sorted(declared - set(events)),
            "counts": {k: {"events": n, "acts": len(acts[k]), "no_act": no_act[k]}
                       for k, n in sorted(events.items())}}


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
    rows = attempts(w, seasons)
    for a, made, no in rows:
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
    graded = Counter(a.verb for a in graded_losses(w, seasons))
    why = refusal_reading(w, d, rows)
    census = kind_census(w, d)
    return {"acts": len(d.resolved), "reasons": why["reasons"],
            "post_admission": why["post_admission"], "kinds": census,
            "formed": dict(formed), "attempted": dict(attempted),
            "executed": dict(executed), "refused": dict(refused), "neither": dict(neither),
            "both": dict(both), "graded": dict(graded), "unrowed": unrowed_acts(w),
            "refusal_kinds": {v: dict(c) for v, c in refusal_kinds.items()},
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


def exists_zero(reasons: dict) -> int:
    """Refused acts whose deciding read was `exists:<Kind>=0` -- the act named a subject that is not
    a `<Kind>` -- summed over verbs. Only the `last-read` reasons carry it; a row that keys its
    refusals by clause reports the clause instead."""
    return sum(n for c in reasons.values() for r, n in c.items()
               if r.startswith("last-read exists:") and r.endswith("=0"))


def _refusal_blocks(m: dict) -> list:
    """The four REM-11 blocks for one world: the deciding read per refusal, the post-admission
    refusals, the declared kinds never emitted, and one count line per emitted kind."""
    out = []
    reasons, post = m["reasons"], m["post_admission"]
    total = sum(sum(c.values()) for c in reasons.values())
    out.append("\n  DECIDING READ PER REFUSAL — per verb, one reason per refused ACT (`d.act_of`): "
                "`clause:` where the row keys its refusals by clause, else `last-read` (the last "
                "`Event.observed` read, not always the one that decided)")
    for v in sorted(reasons):
        c = reasons[v]
        out.append(f"    {v:<16} ref {sum(c.values()):>4}  " + " · ".join(
            f"{r} {n}" for r, n in sorted(c.items(), key=lambda kv: (-kv[1], kv[0]))))
    out.append(f"    TOTAL refused acts {total} · exists:*=0 {exists_zero(reasons)} · graded-loss "
               f"{sum(c.get('graded-loss', 0) for c in reasons.values())} · no-read "
               f"{sum(c.get('no-read', 0) for c in reasons.values())} · no-event "
               f"{sum(c.get('no-event', 0) for c in reasons.values())}")
    out.append("\n  POST-ADMISSION — refusals whose every recorded read passed (`evaluate` replayed "
               "over the Event's own `observed`): the act cleared its `requires`")
    for v in sorted(post):
        out.append(f"    {v:<16} post-admission {post[v]:>4} of ref {sum(reasons[v].values())}")
    out.append(f"    TOTAL post-admission {sum(post.values())}")
    k = m["kinds"]
    out.append(f"\n  DECLARED KINDS NEVER EMITTED — {len(k['never'])} of {k['declared']} "
               f"(`EMITTED_KINDS` with the write matrix's `emits:`, minus the log): {k['never']}")
    out.append(f"\n  EMITTED KINDS — {len(k['counts'])} in the log: events · distinct acts "
               f"(through `d.act_of`) · events with no act")
    for kind, c in k["counts"].items():
        out.append(f"    {kind:<28} events {c['events']:>5}  acts {c['acts']:>5}  no-act {c['no_act']:>5}")
    return out


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
        out.append(f"  UNROWED  acts in the act store whose verb is no table row: {m['unrowed']}")
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
                   "offered · ACTS attempted (the act store) · executed · refused · both (both "
                   "columns matched: two Events for `march`, ONE graded-loss Event for `tell` — "
                   "see `corpus_run._attribute_acts`) · graded (a lost contest: a kind in both "
                   "columns at degree Failure, always also `both`) · neither")
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
                       f"both {m['both'].get(v, 0):>3}  graded {m['graded'].get(v, 0):>3}  "
                       f"neither {m['neither'].get(v, 0)}"
                       + (f"   refused as {m['refusal_kinds'][v]}" if v in m["refusal_kinds"]
                          else ""))
        # -- why each refusal refused (REM-11) ----------------------------------------------
        out.extend(_refusal_blocks(m))
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
