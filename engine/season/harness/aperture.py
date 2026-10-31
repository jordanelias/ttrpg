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
    executed   `corpus_run.attempts`'s `made`: the act's row's `emits:` Event is in the log. An act refused
               AT ADMISSION whose refusal kind is also an `emits:` kind (`finding.none` on `examine` and
               `research`, `news.untold` on `tell`) reads executed too and is also `both`: `ex` counts
               acts that emitted a declared kind, not completions, and `ex - both` is an execution that
               is no refusal
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

**THE POOLED CENSUS AND ITS THREE BLOCKS (CR-14).** `aperture <seasons> --seeds S [S ...]` runs
`measure` at each seed (printing each seed's own report, as before) and then the realm POOLED over the
seeds (`pooled_report`): a PER SEED table of the headline figures, the PER VERB block summed, REM-11's
lines pooled, and three blocks read off every run (per seed too):

    WRONG KIND        per ATTEMPTED act, the first refusal Event that read `exists:<K>` = 0 on the act's
                      subject, classed by where the subject lives (`wrong_kind`); the first class is the
                      wrong-kind share, the rest are counted apart; admitted-then-refused stands beside
    DEATH CENSUS      the `person.died` Events by the killing act's verb and the seats the victim held at
                      the start of the season (`death_census`)
    ANSWERED-BY-SOURCE  two units: DELIBERATIONS by the source (and goal class) of the question the
                      person deliberated under, and SCENES by the source of their occasion
                      (`scene_sources`, P2's unit), with `news.told` / `news.untold`

"Goal class" is `decision_spread.goal_class`, imported; this module classifies no question itself.

**WHAT THIS DOES NOT DO.** It grades nothing, pins nothing and is wired into no gate. Its output is a
measurement of one seeded season, re-runnable: `python -m engine.season.harness.aperture [seasons]
[seed]` or `... <seasons> --seeds S [S ...]`.
"""

from __future__ import annotations

import sys
from bisect import bisect_right
from collections import Counter, defaultdict

from ..data.matrix import MATRIX
from ..data.requires import UNKNOWN, binding_from_act, evaluate
from ..data.rosters import (CLAIM_SOURCES, QUESTION_AGGREGATION, QUESTION_SOURCES, RECORD_KINDS,
                            TENURE_KINDS)
from ..data.verbs import COUNTERPARTY_CLAUSE, EMITTED_KINDS, VERB_TABLE, WRITE_CLAUSE
from ..decision import (aggregate_questions, assemble, make_chooser, opening_set,
                        person_side_eligible)
from ..gaps import Unspecified
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..queries import world_q
from ..queries.world_q import DOCKET_KIND
from ..state.carriers import subject_of
from ..state.ids import H, draw_factory
from ..state.world import World
from . import governance_spine, populated
from .corpus_run import attempts, graded_loss, graded_losses, unrowed_acts
from .decision_spread import goal_class


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


def read_label(obs) -> str:
    """`predicate=value` for one `Observation`, as the DECIDING READ block prints it. The suffix of
    `exists:<Kind>` and `stores:<good>` names a KIND (`data/requires.py`: `Existence.kind`,
    `ScalarThreshold.scalar`) and stays; any other suffix is an entity id and is dropped, so a stem's
    reads pool across ids. A number prints as itself under `exists` and as `0` / `>0` elsewhere."""
    stem = obs.predicate.partition(":")[0]
    pred = obs.predicate if stem in ("exists", "stores") else stem
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
    Returns `{"reasons": {verb: {reason: n}}, "post_admission": {verb: n}, "post_acts": {act id}}`
    (`post_acts` names the acts behind `post_admission`, for the readers that class per act)."""
    emitted = _events_by_act(w, d)          # the one act -> Events index (`wrong_kind` reads it too)
    reasons: dict = defaultdict(Counter)
    post: Counter = Counter()
    post_acts: set = set()
    for a, made, no in rows:
        if not no:
            continue
        row = VERB_TABLE[a.verb]
        evs = [e for _, e in emitted.get(a.id, ()) if e.kind in no]
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
            post_acts.add(a.id)
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
    return {"reasons": {v: dict(c) for v, c in reasons.items()}, "post_admission": dict(post),
            "post_acts": post_acts}


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


# ---------------------------------------------------------------------------------------------
# CR-14 -- THE WRONG-KIND COLUMNS (v), THE DEATH CENSUS (iii), THE ANSWERED-BY-SOURCE BLOCK (ii).
# Three readers over a finished run, each a pure function of `(w, d, ...)`; none writes.

#: A death is the Event kind `person.died`, whichever of `Person.body` or `Person.exists` carries its
#: Receipt (the realm's carries `body`): the one kind both rows emit, asserted against the matrix. THE ONE
#: HOME of the fact for the harness; `harness/arc.py` imports it (`arc` -> `storybar` -> this module).
DEATH_KIND = "person.died"
assert DEATH_KIND in MATRIX[("Person", "exists")].emits and DEATH_KIND in MATRIX[("Person", "body")].emits

#: The classes of the wrong-kind columns, in print order. The first two together are THE wrong-kind
#: share (HR-9): a subject of the wrong collection. The rest are counted apart and are not in it.
WRONG_KIND_FIRST = ("collection", "record_in_collection")
WRONG_KIND_CLASSES = (*WRONG_KIND_FIRST, "record_subkind", "docket", "absent", "other", "after")


def _events_by_act(w, d) -> dict:
    """`{act id: [(log index, Event), ...]}` -- every logged Event `d.act_of` ties to an act, in log
    order. The act's first Event is its first entry."""
    out: dict = defaultdict(list)
    for i, e in enumerate(w.log):
        a = d.act_of.get(e.id)
        if a is not None:
            out[a.id].append((i, e))
    return out


def deaths_of(w, d) -> list:
    """`[(log index, Event, victim id)]` -- the FIRST `person.died` Event per victim, in log order. The
    victim is the first change carrying a subject (`state/attribution.py::anchor_of`'s own tier-2 rule
    for an Event with no act); a death whose Event names no subject is skipped (an instrument defect
    if it is ever the case)."""
    seen: set = set()
    out = []
    for i, e in enumerate(w.log):
        if e.kind != DEATH_KIND:
            continue
        victim = next((c.subject for c in e.changes if c.subject), None)
        if victim is None or victim in seen:
            continue
        seen.add(victim)
        out.append((i, e, victim))
    return out


def _exists_zero_on(event, sid):
    """The wanted kind `K` of the FIRST `exists:<K>` read on `sid` that came back 0 in this refusal
    Event's `observed`, else `None`. Reads through `_observed_of`, the one read of `Event.observed`."""
    for o in _observed_of(event):
        p = str(o.predicate)
        if (p.startswith("exists:") and o.value is not UNKNOWN and o.value in (0, False)
                and str(o.subject) == str(sid)):
            return p.partition(":")[2]
    return None


def _lives_in(w, collection, sid, cast, died_at, first_i) -> bool:
    """Does `sid` live in `w.<collection>` as the wrong-kind columns read it: a person is present when
    he is in `cast` and no death naming him is logged before `first_i`; any other collection is read as
    the run left it. A subject that is not a string lives nowhere."""
    if not isinstance(sid, str) or not sid:
        return False
    if collection == "persons":
        return sid in cast and died_at.get(sid, first_i) >= first_i
    return sid in getattr(w, collection)


def wrong_kind(w, d, rows, post_acts, cast) -> dict:
    """THE WRONG-KIND-AT-ADMISSION COLUMNS (CR-14 (v); the register's G-08). Per ATTEMPTED act that
    was refused (never per `_admits` call), the first refusal Event whose `observed` holds
    `exists:<K>` = 0 on the act's subject (`subject_of`) decides:

      collection           K is a collection class (`World._STATE_COLLECTIONS`: `exists:Site`) and the
                           subject lives in another collection              \\ the first class: THE
      record_in_collection K is a Record sub-kind (`RECORD_KINDS`) and the   / wrong-kind share
                           subject lives in a collection other than `records`
      record_subkind       K is a Record sub-kind and the subject is a Record (of another sub-kind)
      docket               K is `DocketItem`: a read of the docket, not a collection
      absent               the subject lives in no collection
      other                a refusal with none of the above that is not post-admission (a read other
                           than `exists:` failed, a graded loss, an act with no recorded read)
      after                admitted-then-refused: REM-11's post-admission act (`post_acts`)

    The order is the order of these tests, so every refused act is in exactly one class and the seven
    sum to the refused acts. WHERE A SUBJECT LIVES: a person is present at the act when he is in
    `cast` (the persons read BEFORE the season) and no `person.died` Event naming him precedes the
    act's first Event; the other collections are read at the run's end. ⚠ TIMING: the probe this
    follows classed against the live world at admission, so a record removed during the run, or a
    person whose death followed the act, can class differently here.

    Returns `{"attempted": n, "refused": n, "classes": {class: n}, "by_verb": {verb: {class: n}},
    "other_detail": {"graded-loss": n, "no-read": n, "no-event": n}}` (a key is present only when counted)."""
    by_act = _events_by_act(w, d)
    died_at = {victim: i for i, _, victim in deaths_of(w, d)}
    collections = World._STATE_COLLECTIONS
    classes: Counter = Counter()
    by_verb: dict = defaultdict(Counter)
    detail: Counter = Counter()
    refused = 0
    for a, made, no in rows:
        if not no:
            continue
        refused += 1
        evs = by_act.get(a.id, [])
        first_i = evs[0][0] if evs else len(w.log)
        sid = subject_of(a)
        cls = None
        for _, e in evs:
            if e.kind not in no:
                continue
            kind = _exists_zero_on(e, sid)
            if kind is None:
                continue
            if kind in TENURE_KINDS:                 # an edge read, not an object class
                break
            where = [c for c in collections if _lives_in(w, c, sid, cast, died_at, first_i)]
            if kind == DOCKET_KIND:
                cls = "docket"
            elif kind in RECORD_KINDS:
                cls = ("absent" if not where else "record_subkind" if "records" in where
                       else "record_in_collection")
            elif kind.lower() + "s" in collections:
                cls = ("absent" if not where
                       else "collection" if kind.lower() + "s" not in where else None)
            break                                    # the first read decides, classed or not
        if cls is None:
            cls = "after" if a.id in post_acts else "other"
            if cls == "other":
                refusal = [e for _, e in evs if e.kind in no]
                if not refusal:
                    detail["no-event"] += 1      # no Event at all: `refusal_reading` labels the same act `no-event`
                elif graded_loss(a, refusal):
                    detail["graded-loss"] += 1
                elif not any(_observed_of(e) for e in refusal):
                    detail["no-read"] += 1
        classes[cls] += 1
        by_verb[a.verb][cls] += 1
    return {"attempted": len(rows), "refused": refused,
            "classes": {c: classes.get(c, 0) for c in WRONG_KIND_CLASSES},
            "by_verb": {v: dict(c) for v, c in by_verb.items()}, "other_detail": dict(detail)}


def death_census(w, d, marks) -> dict:
    """THE DEATH CENSUS (CR-14 (iii); the register's G-20). Each death the watched seasons held (the
    FIRST `person.died` Event per victim, `deaths_of`), by the verb of the killing act (`d.act_of` of
    the Event; a death with no act -- a MATTER `_die` -- is its own `no act` row) and the seats the
    victim held. `marks` is `[(log length, seats(w)), ...]`, one per season, taken at that season's
    START: a death is placed in the season whose log span holds it and its seats are that season's.
    ⚠ A seat gained and lost inside one season is not seen.
    Returns `{"deaths": [{"victim", "season", "verb", "seats"}], "events": person.died Events}`."""
    starts = [n for n, _ in marks]
    out = []
    for i, e, victim in deaths_of(w, d):
        if not starts or i < starts[0]:
            continue
        s = bisect_right(starts, i) - 1
        a = d.act_of.get(e.id)
        out.append({"victim": victim, "season": s, "verb": a.verb if a is not None else "no act",
                    "seats": list(marks[s][1].get(victim, ()))})
    return {"deaths": out,
            "events": sum(1 for i, e in enumerate(w.log) if e.kind == DEATH_KIND
                          and starts and i >= starts[0])}


def source_key(q) -> tuple:
    """The `(source, class)` key a question is tabled under in the ANSWERED-BY-SOURCE blocks: `("none", "-")`
    for a deliberation with no question."""
    return ("none", "-") if q is None else (q.source, class_label(q))


def class_label(q) -> str:
    """A question's goal class as the ANSWERED-BY-SOURCE tables print it: `decision_spread.goal_class`'s
    answer (THE one classifier -- aperture imports it and writes no second), with an org goal's own id
    collapsed to `org goal` (`goal_class` returns the goal's id for one, and returns it for nothing
    else). A non-`need` question is `-`."""
    c = goal_class(q)
    return "org goal" if q.source == "need" and c == q.about else c


def scene_sources(d) -> dict:
    """SCENES BY OCCASION SOURCE (CR-14 (ii), P2's unit): each Scene of `d.scenes`, read at the season's
    end, by its `occasion`'s source (`harness/soak.py::_occasion_row` reads it the same way; a scene
    with no occasion is `none`), and a `need` scene by `class_label`. Returns
    `{"scenes": n, "rows": {(source, label): n}, "need": n, "need_goal": n}` where `need_goal` is the
    need scenes about a goal Proposition (an `org goal` row) and the rest of `need` are the others."""
    rows: Counter = Counter()
    for sc in d.scenes.values():
        q = getattr(sc, "occasion", None)
        rows[source_key(q)] += 1
    need = sum(n for (s, _), n in rows.items() if s == "need")
    return {"scenes": sum(rows.values()), "rows": dict(rows), "need": need,
            "need_goal": rows.get(("need", "org goal"), 0)}


def instrumented_season(w, seasons: int) -> dict:
    """Run `seasons` seasons on `w` with the chooser and the question barrier WATCHED, never
    steered. The driver/chooser construction is `populated.run`'s, line for line, so the control
    in `measure` can compare the two worlds' hashes."""
    d = SeasonDriver(w)
    fx = w.fixtures
    cast = frozenset(w.persons)          # the persons BEFORE the season, for the wrong-kind columns
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
    answered: Counter = Counter()         # (source, class label) -> deliberations; `none` has no question

    def watched_choose(p, v, s, ask_budget):
        nonlocal mismatch
        q = getattr(v, "question", None)
        real_cands = opening_set(p, v, q, fx) if q is not None else []
        formed[p.id] |= {c.verb for c in real_cands}
        answered[source_key(q)] += 1
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

    marks: list = []                     # per season, at its START: (log length, seats), for the death census
    for _ in range(seasons):
        marks.append((len(w.log), seats(w)))
        d.season(watched_choose, question=None,
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
    told = census["counts"].get("news.told", {}).get("events", 0)
    untold = census["counts"].get("news.untold", {}).get("events", 0)
    return {"acts": len(d.resolved), "reasons": why["reasons"],
            "post_admission": why["post_admission"], "kinds": census,
            "formed": dict(formed), "attempted": dict(attempted),
            "executed": dict(executed), "refused": dict(refused), "neither": dict(neither),
            "both": dict(both), "graded": dict(graded), "unrowed": unrowed_acts(w),
            "refusal_kinds": {v: dict(c) for v, c in refusal_kinds.items()},
            "wrong_kind": wrong_kind(w, d, rows, why["post_acts"], cast),
            "deaths": death_census(w, d, marks), "answered": dict(answered),
            "deliberations": len(per_rule.get(shipped, ())), "scenes": scene_sources(d),
            "news": {"told": told, "untold": untold},
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


def _control_same(m: dict) -> bool:
    """The CONTROL arm and the measured arm agree on the hash and on the acts."""
    c = m["control"]
    return c["hash"] == m["hash"] and c["acts"] == m["acts"]


def _control_line(m: dict) -> str:
    c = m["control"]
    same = _control_same(m)
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


# The PER VERB row's columns, one owner for the per-seed block and the pooled one. `elig_s` / `elig_u`
# are PERSONS (seated / unseated); every column is a count that sums over seeds.
VERB_COLUMNS = ("elig_s", "elig_u", "formed", "offered", "att", "ex", "ref", "both", "graded",
                "neither")


def verb_counts(m: dict, verbs, foldable) -> dict:
    """`{verb: {column: n, ..., "refused_as": {kind: n}}}` for one world: the PER VERB row's figures."""
    seated = set(m["seats"])
    out = {}
    for v in verbs:
        fo = sum(1 for s in m["formed"].values() if v in s)
        out[v] = {"elig_s": sum(1 for p in seated if v in m["eligible"][p]),
                  "elig_u": sum(1 for p in m["persons"] if p not in seated and v in m["eligible"][p]),
                  "formed": fo, "offered": fo if v in foldable else 0,
                  "att": sum(c.get(v, 0) for c in m["attempted"].values()),
                  "ex": sum(c.get(v, 0) for c in m["executed"].values()),
                  "ref": sum(c.get(v, 0) for c in m["refused"].values()),
                  "both": m["both"].get(v, 0), "graded": m["graded"].get(v, 0),
                  "neither": m["neither"].get(v, 0),
                  "refused_as": dict(m["refusal_kinds"].get(v, {}))}
    return out


def pool_verb_counts(per_seed: list) -> dict:
    """The PER VERB figures pooled over seeds: every column summed, `refused_as` summed per kind. Pure
    over `verb_counts`' dicts; a verb absent from one seed's dict counts 0 there."""
    out: dict = {}
    for vc in per_seed:
        for v, c in vc.items():
            o = out.setdefault(v, {**{k: 0 for k in VERB_COLUMNS}, "refused_as": {}})
            for k in VERB_COLUMNS:
                o[k] += c.get(k, 0)
            for kind, n in c.get("refused_as", {}).items():
                o["refused_as"][kind] = o["refused_as"].get(kind, 0) + n
    return out


def _verb_line(v: str, c: dict, foldable) -> str:
    return (f"    {v:<16} {'R' if v in foldable else '.'}  elig {c['elig_s']:>3}/{c['elig_u']:<3} "
            f"formed {c['formed']:>3}  offered {c['offered']:>3}  att {c['att']:>4}  ex {c['ex']:>4}  "
            f"ref {c['ref']:>4}  both {c['both']:>3}  graded {c['graded']:>3}  "
            f"neither {c['neither']}"
            + (f"   refused as {c['refused_as']}" if c["refused_as"] else ""))


def verb_totals(vc: dict) -> dict:
    """Every PER VERB column summed over the verbs."""
    return {k: sum(c[k] for c in vc.values()) for k in VERB_COLUMNS}


def _verb_total_line(vc: dict) -> str:
    """The sum of every verb row's attempted / executed / refused / both / graded / neither, with
    `att - ref` beside them (the acts that drew no refusal kind; `ex` also counts a graded loss and an act
    refused at admission whose refusal kind is an emitted kind -- the larger part of `both` -- so `att - ref`
    and `ex` are not the same number)."""
    t = verb_totals(vc)
    return (f"    {'TOTAL':<16}    att {t['att']:>5}  ex {t['ex']:>5}  ref {t['ref']:>5}  "
            f"att-ref {t['att'] - t['ref']:>5}  both {t['both']:>4}  graded {t['graded']:>4}  "
            f"neither {t['neither']}")


# ---------------------------------------------------------------------------------------------
# CR-14 blocks and pooling. `pool_worlds` sums what is a count and intersects what is an absence;
# the printers take a world dict OR the pooled dict, which have the same keys.

def pool_worlds(ms: list) -> dict:
    """The per-world figures a pooled block reads, summed over `ms` (`measure_world`'s dicts):
    `reasons` and `post_admission` per verb; `kinds` (declared once, `never` = the kinds absent from
    EVERY seed's log, `counts` summed); `wrong_kind`; `deaths` (the deaths concatenated, tagged by
    seed, `runs` counted); `answered` and `scenes` rows summed; `news`; `deliberations`. A pure
    function over the dicts: it reads no world."""
    reasons: dict = defaultdict(Counter)
    post: Counter = Counter()
    for m in ms:
        for v, c in m["reasons"].items():
            reasons[v].update(c)
        post.update(m["post_admission"])
    counts: dict = {}
    for m in ms:
        for kind, c in m["kinds"]["counts"].items():
            o = counts.setdefault(kind, {"events": 0, "acts": 0, "no_act": 0})
            for k in o:
                o[k] += c[k]
    never = sorted(set.intersection(*(set(m["kinds"]["never"]) for m in ms))) if ms else []
    wk_classes = Counter()
    wk_verb: dict = defaultdict(Counter)
    wk_detail = Counter()
    for m in ms:
        wk = m["wrong_kind"]
        wk_classes.update(wk["classes"])
        for v, c in wk["by_verb"].items():
            wk_verb[v].update(c)
        wk_detail.update(wk["other_detail"])
    answered = Counter()
    scene_rows = Counter()
    for m in ms:
        answered.update(m["answered"])
        scene_rows.update(m["scenes"]["rows"])
    return {
        "reasons": {v: dict(c) for v, c in reasons.items()}, "post_admission": dict(post),
        "kinds": {"declared": max((m["kinds"]["declared"] for m in ms), default=0),
                  "never": never, "counts": dict(sorted(counts.items()))},
        "wrong_kind": {"attempted": sum(m["wrong_kind"]["attempted"] for m in ms),
                       "refused": sum(m["wrong_kind"]["refused"] for m in ms),
                       "classes": {c: wk_classes.get(c, 0) for c in WRONG_KIND_CLASSES},
                       "by_verb": {v: dict(c) for v, c in wk_verb.items()},
                       "other_detail": dict(wk_detail)},
        "deaths": {"runs": len(ms), "events": sum(m["deaths"]["events"] for m in ms),
                   "deaths": [{**x, "seed": m["seed"]} for m in ms for x in m["deaths"]["deaths"]]},
        "answered": dict(answered), "deliberations": sum(m["deliberations"] for m in ms),
        "scenes": {"scenes": sum(m["scenes"]["scenes"] for m in ms), "rows": dict(scene_rows),
                   "need": sum(m["scenes"]["need"] for m in ms),
                   "need_goal": sum(m["scenes"]["need_goal"] for m in ms)},
        "news": {k: sum(m["news"][k] for m in ms) for k in ("told", "untold")},
    }


def _wrong_kind_blocks(m: dict) -> list:
    wk = m["wrong_kind"]
    c, att, ref = wk["classes"], wk["attempted"], wk["refused"]
    first = sum(c[k] for k in WRONG_KIND_FIRST)
    classed = sum(c.values())
    share = 100 * first / att if att else 0.0
    post_total = sum(m["post_admission"].values())
    od = wk["other_detail"]
    out = ["\n  WRONG KIND AT ADMISSION — per ATTEMPTED act, the first refusal Event whose `observed` "
           "holds `exists:<K>` = 0 on the act's subject; the subject classed by where its id lives "
           "(a person present when in the pre-season cast and not yet dead at the act's first Event; "
           "every other collection as the run left it)",
           f"    attempted {att} · refused {ref}",
           f"    WRONG-KIND (first class) {first} of {att} attempts ({share:.1f}%) — "
           f"a collection class wanted, the subject in another collection {c['collection']} · a Record "
           f"sub-kind wanted of a subject in another collection {c['record_in_collection']}",
           f"    wrong Record sub-kind {c['record_subkind']} · `exists:DocketItem` = 0 {c['docket']} · "
           f"absent subject {c['absent']}",
           f"    other {c['other']} (of them graded-loss {od.get('graded-loss', 0)}, a lost contest that "
           f"passed admission; no recorded read {od.get('no-read', 0)}; no event {od.get('no-event', 0)}) "
           f"· admitted-then-refused {c['after']} "
           f"(REM-11 post-admission TOTAL {post_total})",
           # holds by construction: `refused` and exactly one class are counted per refused act in one loop
           # (`wrong_kind`), so this observes a class missing from WRONG_KIND_CLASSES and nothing else
           f"    SUM CONTROL  first {first} + sub-kind {c['record_subkind']} + docket {c['docket']} + "
           f"absent {c['absent']} + other {c['other']} + after {c['after']} = {classed} vs refused "
           f"{ref} -> {'OK' if classed == ref else 'DIFFERENT'}"]
    for v in sorted(wk["by_verb"]):
        bv = wk["by_verb"][v]
        out.append(f"      {v:<16} " + " · ".join(f"{k} {bv[k]}" for k in WRONG_KIND_CLASSES if bv.get(k)))
    return out


def _death_blocks(m: dict) -> list:
    dc = m["deaths"]
    deaths = dc["deaths"]
    by_verb = Counter(x["verb"] for x in deaths)
    holders = sum(1 for x in deaths if x["seats"])
    out = ["\n  DEATH CENSUS — `person.died` (the first per victim) by the killing act's verb "
           "(`d.act_of`; `no act` = a MATTER death); seats read at the START of the season the death "
           "falls in, so a seat gained and lost within one season is not seen",
           f"    runs {dc.get('runs', 1)} · deaths {len(deaths)} (person.died Events {dc['events']}) · "
           f"seat-holder victims {holders} · by killing verb "
           f"{dict(sorted(by_verb.items(), key=lambda kv: (-kv[1], kv[0]))) or 'none'}"]
    for x in deaths:
        tag = f"seed {x['seed']} " if "seed" in x else ""
        out.append(f"      {tag}{x['victim']} season {x['season']} by {x['verb']} seats {x['seats'] or 'none'}")
    return out


def _answered_blocks(m: dict) -> list:
    ans, sc = m["answered"], m["scenes"]
    sources = list(QUESTION_SOURCES) + sorted({s for s, _ in ans if s != "none"} - set(QUESTION_SOURCES))

    def rows_in(rows: dict) -> list:
        return [f"      {src:<14} {label:<11} {n:>5}" for src in [*sources, "none"]
                for (s, label), n in sorted(rows.items()) if s == src]

    out = ["\n  ANSWERED-BY-SOURCE — two units, each its own table. `need` is split by "
           "`decision_spread.goal_class` (the one classifier): own want · creed · org goal · other need",
           "    DELIBERATIONS by the source of the question delivered under the shipped rule "
           "(`none` = the person deliberated with no question)"]
    out.extend(rows_in(ans))
    total = sum(ans.values())
    # holds by construction: `answered` and the shipped rule's `per_rule` row both grow once per deliberation
    # (`watched_choose`), so this fails only if the shipped rule is off `QUESTION_AGGREGATION`
    out.append(f"      rows + none = {total} vs the PER AGGREGATION RULE deliberation count "
               f"{m['deliberations']} -> {'OK' if total == m['deliberations'] else 'DIFFERENT'}")
    out.append("    SCENES by occasion source (`d.scenes` read at the season's end; P2's unit)")
    out.extend(rows_in(sc["rows"]))
    out.append(f"      scenes {sc['scenes']} · need {sc['need']}, of them about a goal Proposition "
               f"{sc['need_goal']} · other {sc['need'] - sc['need_goal']}")
    out.append(f"    news.told {m['news']['told']} · news.untold {m['news']['untold']}")
    return out


def cr14_blocks(m: dict) -> list:
    """The CR-14 blocks for one world or a pooled one: wrong-kind columns, death census,
    answered-by-source."""
    return [*_wrong_kind_blocks(m), *_death_blocks(m), *_answered_blocks(m)]


def seed_row(m: dict, verbs, foldable) -> dict:
    """One seed's headline figures, for the PER SEED table: the PER VERB totals, the first wrong-kind
    class and the others, the deaths and the told / untold counts."""
    t = verb_totals(verb_counts(m, verbs, foldable))
    c = m["wrong_kind"]["classes"]
    d = m["deaths"]["deaths"]
    return {**t, "att-ref": t["att"] - t["ref"], "first": sum(c[k] for k in WRONG_KIND_FIRST), "subkind": c["record_subkind"],
            "docket": c["docket"], "absent": c["absent"], "other": c["other"], "after": c["after"],
            "deaths": len(d), "holders": sum(1 for x in d if x["seats"]),
            "told": m["news"]["told"], "untold": m["news"]["untold"],
            "need": m["scenes"]["need"], "need_goal": m["scenes"]["need_goal"],
            "scenes": m["scenes"]["scenes"], "delib": m["deliberations"]}


def pooled_report(results: list) -> list:
    """The realm pooled over `results` (each `measure`'s dict): a PER SEED table of the headline
    figures with a POOLED row; the PER VERB block summed; REM-11's lines pooled; the CR-14 blocks.
    The spine world stays per-seed (it is in each seed's own `report`)."""
    verbs, foldable = results[0]["verbs"], set(results[0]["resolvable"])
    ms = [r["realm"] for r in results]
    seeds = [m["seed"] for m in ms]
    out = ["=" * 100,
           f"POOLED OVER SEEDS {seeds} — realm, {ms[0]['seasons']} season(s); every count summed over "
           f"the seeds (the elig columns are persons-per-seed); the spine stays per seed above"]
    out.append("  CONTROL per seed: " + " · ".join(
        f"seed {m['seed']} {'EQUAL' if _control_same(m) else 'DIFFERENT'}"
        for m in ms))
    cols = ("att", "ex", "ref", "att-ref", "both", "graded", "neither", "first", "subkind", "docket",
            "absent", "other", "after", "deaths", "holders", "told", "untold", "need", "need_goal",
            "scenes", "delib")
    rows = [seed_row(m, verbs, foldable) for m in ms]
    pooled = {k: sum(r[k] for r in rows) for k in cols}
    out.append("\n  PER SEED — att/ex/ref/att-ref/both/graded/neither: the PER VERB totals · first "
               "wrong-kind class, then sub-kind/docket/absent/other/after · deaths, seat-holders · "
               "news.told/untold · need scenes, of them about a goal · scenes · deliberations")
    out.append("    " + f"{'seed':>6} " + " ".join(f"{c:>8}" for c in cols))
    for m, r in zip(ms, rows):
        out.append("    " + f"{m['seed']:>6} " + " ".join(f"{r[c]:>8}" for c in cols))
    out.append("    " + f"{'POOLED':>6} " + " ".join(f"{pooled[c]:>8}" for c in cols))
    out.append("\n  PER VERB, POOLED — persons eligible (seated/unseated) · persons formed · persons "
               "offered · ACTS attempted · executed · refused · both · graded · neither")
    vc = pool_verb_counts([verb_counts(m, verbs, foldable) for m in ms])
    for v in verbs:
        out.append(_verb_line(v, vc[v], foldable))
    out.append(_verb_total_line(vc))
    pm = pool_worlds(ms)
    out.extend(_refusal_blocks(pm))
    out.extend(cr14_blocks(pm))
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
                   "columns matched: two Events for `march`, ONE graded-loss Event for `tell`, and "
                   "an admission refusal whose kind is also an emitted kind, `finding.none` on "
                   "`examine`/`research`, the larger part — see `corpus_run._attribute_acts`) · graded (a lost contest: a kind in both "
                   "columns at degree Failure, always also `both`) · neither")
        seated = set(m["seats"])
        vc = verb_counts(m, verbs, foldable)
        for v in verbs:
            out.append(_verb_line(v, vc[v], foldable))
        out.append(_verb_total_line(vc))
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
        # -- CR-14: wrong kind at admission, the death census, answered-by-source ------------
        out.extend(cr14_blocks(m))
    return out


def parse_args(argv: list):
    """`(seasons, seeds)` from `[seasons] [seed]` (the original form: `seeds` is `[seed]`) or
    `[seasons] --seeds S [S ...]`. Returns `(seasons, seeds, pooled)`; raises `ValueError` on a
    `--seeds` with no seed, a non-numeric seed, or both a positional seed and `--seeds`."""
    if "--seeds" not in argv:
        seasons = int(argv[0]) if argv and argv[0].isdigit() else 1
        seed = int(argv[1]) if len(argv) > 1 and argv[1].isdigit() else 0
        return seasons, [seed], False
    i = argv.index("--seeds")
    head, tail = argv[:i], argv[i + 1:]
    if len(head) > 1 or (head and not head[0].isdigit()):
        raise ValueError("with --seeds the only positional argument is `seasons`")
    if not tail or not all(t.isdigit() for t in tail):
        raise ValueError("--seeds takes one or more non-negative integer seeds")
    return (int(head[0]) if head else 1), [int(t) for t in tail], True


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    try:
        seasons, seeds, pooled = parse_args(argv)
    except ValueError as e:
        print(f"aperture: {e}\nusage: aperture [seasons] [seed] | aperture seasons --seeds S [S ...]",
              file=sys.stderr)
        return 2
    results = []
    for seed in seeds:
        res = measure(seed, seasons)
        results.append(res)
        print("\n".join(report(res)), flush=True)
    if pooled:
        print("\n".join(pooled_report(results)), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
