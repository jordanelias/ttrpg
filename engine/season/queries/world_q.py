"""`season.queries.world_q` — THE WORLD-FIRST HALF OF `Query`, AND THE TWO WORLD-FIRST
FUNCTIONS THAT WERE NEVER IN IT.

EXTRACTED, step 5 of the decomposition. `04_CODE_ARCHITECTURE.md` §A.3 row 2 is the ruling and it
is a MODULE ruling, not a signature one: *"one `Query` class holding both families -> two modules;
the second cannot import the first ... In one class, a person-side function calls a resolver-side
one with no import to scan."* The eleven functions here all take a `World` FIRST. The four
person-side statics stay on `Query` in `shape.py` until step 7 puts them in `decision`, which is
the module that may not name `World` at all.

⚠ THE ELEVEN ARE MODULE FUNCTIONS NOW, AND `shape.Query` BINDS THEM AS `staticmethod`s. That is a
re-export, not a copy — `Query.parent_of is parent_of` — so every call site reading
`Query.<world-first>` resolves to these bodies and there is exactly one owner of each rule. The
binding is what makes the class deletable at step 7 without a second migration.

⚠ THIS MODULE MUST NOT LEARN A PERSON. Its one-way rule is the same one `state/` states: nothing
here imports `shape`, `decision`, `loop` or `seam`. `questions_for` takes a `Person` as its SECOND
argument and asks the WORLD about them; that is a world-first function, not a person-side one, and
the AST guard (`test_w5_sense_is_still_the_only_world_taking_non_decision_function`) is what keeps
the distinction checkable by signature rather than by intention.

⚠ THAT SENTENCE WAS FALSE WHEN FIRST WRITTEN AND IS MADE TRUE RATHER THAN SOFTENED. The guard
parsed `files.SHAPE_PY` alone, so it could not see this module at all — a claim of enforcement
naming a gate that does not read the file it is written in, which is the §47 defect the package
records twice already. Caught by a read-only critic; the guard now parses the model set, and
`_model_modules()` derives that set from a recursive glob, so it will read the module a later
step adds without anyone remembering to say so.
"""

from __future__ import annotations

import copy
import functools
from dataclasses import dataclass, replace
from typing import Callable, Optional

from ..data.requires import OWN_STATE_STEMS, UNKNOWN, binding_from_act
from ..data.rosters import (
    BAN_KIND, DETAIN_KIND, DOMINANCE_KINDS, ENDING_ANY_ONE, ENDINGS, FACTION_BY_PROP,
    QUESTION_SOURCES, RECORD_CONTENT, RECORD_KINDS, REMOVE_ORDINAL, RESTRAINT_KINDS, RUNG_KINDS,
    SITE_KINDS, STANDING_CROSSED, TENURE_KINDS, faction_prop_id,
)
# IN-09: the Record kinds a held document is an occasion for, derived off the verb table's rows;
# v9 IN-49: the remit acts a seat exercises on a `Rung`-classed referent, the same way.
# v9 IN-27: `_OPENERS_FROM_EFFECTS` is which verbs open which Tenure kind, derived off the effects
# (`OPENERS-DERIVE`); `endings_reached` evaluates the `ENDINGS` vocabulary imported above.
from ..data.verbs import RECORD_REFERENT_KINDS, RUNG_REMIT_ACTS, _OPENERS_FROM_EFFECTS
from ..gaps import Forbidden, InstrumentDefect, Unspecified
# Telling `T7` (v9 IN-16): the declared-intent claim's stem and its value's reader, owned once in
# the asker-first module (which may not import this one; this edge runs the other way).
from .person_q import LedgerReader, OwnStateReader, content_said, intent_named, ledger_names
# v9 IN-57: `attention_key`'s tier 2 scores a deed claim by `deed_valence`, one owner per factor.
from .person_q import (
    _seen_index, crisis_weights, deed_valence, paired_deed_term, projected_axes)
# v9 SC-02 `22a`: `reception` and `proofs` read which claims record a person's deeds, what each is worth
# to its holder, and which deeds were done TO him, off the same person-side owners `regard` reads.
from .person_q import attributed_deeds, deed_term, suffered_deeds
# v9 IN-69: the one cosine (`cast.loyalty` calls it too).
from ..data.pursuits import pursuit_cosine_axes, to_axes
# v9 IN-67: `goal_referents` reads a goal's `object:` off the ONE loader and a `deed_doers` goal's
# doers off the person-side family.
from ..data import goals as _goals
from .person_q import deed_doers
# v9 IN-70: a person's opinion of a faction -- the formula person-side, membership and the faction's
# expectations here; the doer of a paired deed is the pairing rule's (IN-58).
from ..data.verbs import DEED_KINDS
from .person_q import PAIRED_KINDS, opinion
from ..state.attribution import anchor_of, causing_act, event_by_id, matured_terms  # noqa: F401 -- re-exported
from ..state.carriers import Person, Question, Site, Tenure
# ⚠ `parent_of` AND `descendants` ARE RE-EXPORTED, NOT DEFINED HERE (G3, plan position 6). The
# write gate's F3 clause needs both -- ruling (3)'s parent rung and ruling (4)'s purview subtree --
# and the gate is in `state/`, which may not import this module. The bodies moved down unchanged;
# these names are the same function objects, so every `world_q.parent_of(...)` call is unaffected.
from ..state.containment import descendants, parent_of  # noqa: F401 -- re-exported
# ⚠ AND `ancestry`/`home_of` BY THE SAME ROUTE (plan position `19`, U7-remit): the write gate's
# `determination` basis asks the bench's containment test of the party's home, so both walks moved
# down, unchanged. Same function objects; every `world_q.ancestry(...)`/`world_q.home_of(...)` caller
# is unaffected.
from ..state.containment import ancestry, home_of  # noqa: F401 -- re-exported
# `19`: the bench's two rules, owned by the gate that enforces them (`judging_set` asks both), and
# the seat-authority predicates the `basis` form's stems read (`WorldReader.read`, below).
from ..state.gate import BENCH_BASIS, may_determine, may_fill, purview_reaches, sits_over
# ⚠ AND `sworn_to` BY THE SAME ROUTE (v9 IN-40, `H-101`): THE QUERY OF THE LIVE `oblige` EDGES SWORN
# TO A SEAT. `purview_reaches`' oblige clause asks it, and the gate may not import this module, so
# its one body lives in `state/gate.py`; `world_q.sworn_to is gate.sworn_to`. `establishment_of`
# (below) composes on it.
from ..state.gate import sworn_to
from ..state.ids import H, ROOT, draw_factory
from ..state.world import World
from ..trace_log import TRACE


# ===========================================================================
# S17 -- QUERY. THE SIDE COLUMN IS THE ENFORCEMENT.
# ===========================================================================

# ---- resolver-side: World FIRST, always -----------------------------
# `parent_of(w, rung_id)` and `descendants(w, rung_id)` -- see the import above and
# `state/containment.py`.

def r1_aggregate(w: World, rung_id: str, over: Callable[[str], int]) -> int:
    """R-1: COMPUTE ON DEMAND over DESCENDANTS. Never received, never stored. S22.4 cl.3:
    LIVE EDGES ONLY. S6.2: this is a claim about the CONTAINMENT TREE."""
    TRACE.query("r1_aggregate", "resolver")
    return sum(over(d) for d in descendants(w, rung_id))

def aggregate_guard(w: World, name: str, *, per_person_tally: bool = False,
                    over_ended_edges: bool = False) -> None:
    """S22.4 -- THE AGGREGATION BOUNDARY.

    REV 2 HONESTY NOTE. S22.4 clause 2 is a READ-SIDE rule and is therefore checkable by
    GREPPING THE RESOLVER for a Query crossing holders -- a static check, not a runtime one.
    This function is the runtime half and THE CALLER VOLUNTEERS ITS OWN VIOLATION, which
    detects nothing on its own. `commit_count_guard` below is the part that actually
    detects, because it inspects the edge set rather than trusting a flag."""
    if per_person_tally:
        raise Forbidden(
            f"resolver-side Query '{name}' aggregates per-person tallies ACROSS HOLDERS",
            "S22.4", law="L3 clause 2 -- THAT IS STORED, MONOTONE, NEVER-DECAYING UNREST IN ALL BUT NAME -- worse than the field L3 banned, because the banned field could at least go down")
    if over_ended_edges:
        raise Forbidden(
            f"Query '{name}' composes over ENDED edges and is monotone", "S22.4",
            law="L3 clause 3 -- any Query monotone in the ENDED-edge set is a ratchet and is REFUSED. `count{commit}` over live AND ended rows is monotone; `count{hold: until != null}` is revocations-ever; each is built only from 'structural' edges and each EVADES clause 2")

def single_holder_counter(w: World, person: str, axis: str, registry: set[str]) -> int:
    """L3 CLAUSE 1 -- and rev 4 exists because revisions 1-3 refused what this clause
    EXPLICITLY PERMITS.

    The head, verbatim: *"a monotone counter exists ONLY per `(Person, axis)` where `axis`
    is on a closed registry"*, and its own note calls such a counter **"legal, since every
    increment is in the holder's own ledger"**. Clause 2 bars only the CROSS-HOLDER SUM.

    Revisions 1-3 routed every "a character's risk builds up quietly" row to a probe that
    raised clause 2 -- on a need that never crosses a holder. It was THE LARGEST SINGLE
    BLOCKER IN THE CORPUS (18 cases), and it was the instrument measuring AGAINST the
    design, which S0.1 point 4 rules is no more acceptable than flattering it.

    What is genuinely missing is narrower and is what this raises: THE CLOSED REGISTRY."""
    TRACE.query("single_holder_counter", "resolver")
    if not registry:
        raise Unspecified(
            f"the closed `axis` registry L3 clause 1 requires (asked for '{axis}')",
            "S22.4",
            needs="a closed roster of axes, and a write-matrix row admitting the increment",
            law="L3 clause 1 permits a monotone counter PER (Person, axis) -- 'legal, since every increment is in the holder's own ledger' -- but ONLY where `axis` is ON A CLOSED REGISTRY. No such registry exists in the chain, and no S30 row admits the write. S54 item 6 adds that the axis must not be spelled `exposure` bare, or it collides with the need scalar",
        )
    if axis not in registry:
        raise Forbidden(f"axis '{axis}' is not on the closed registry", "S22.4",
                        law="L3 clause 1 -- ONLY where `axis` is on a closed registry")
    return sum(1 for c in w.persons[person].ledger if c.predicate == axis)

def commit_count_guard(w: World, edges: list[Tenure], name: str) -> int:
    """The DETECTING half of clause 3: it looks at the rows, not at a flag."""
    ended = [t for t in edges if not t.live]
    if ended:
        raise Forbidden(
            f"aggregate '{name}' composed over {len(ended)} ENDED edge(s)", "S22.4",
            needs="filter to until == null before summing",
            law="L3 clause 3 -- ended Tenures PERSIST as historical claim subjects (S15.2), so a count over live AND ended rows is monotone non-decreasing. That is a ratchet built entirely out of 'structural' edges")
    return len(edges)

def lateral(w: World, name: str, kind: str) -> list[Tenure]:
    """S6.2/S38 -- THE LATERAL GRAPH. Not governed by R-1/R-2. Resolver-side, World first,
    therefore unreachable from choose() BY CONSTRUCTION."""
    TRACE.query(f"lateral:{name}", "resolver")
    return [t for t in w.tenures if t.kind == kind and t.live]

def verbs(w: World, site: Site, floors: dict[str, int]) -> set[str]:
    """S12.1 -- condition GATES VERBS. The comparison is on a SUMMED FIXED-POINT INT."""
    TRACE.query("verbs", "resolver")
    return {v for v, floor in floors.items() if site.condition >= floor}

def hold_force(w: World, obj: str) -> Optional[Tenure]:
    """S15 -- `hold` is 1 PER OBJECT. S54 item 20's lawful form rests on this cardinality."""
    live = [t for t in w.tenures if t.kind == "hold" and t.object == obj and t.live]
    if len(live) > 1:
        raise Forbidden(f"{len(live)} live `hold` Tenures on {obj}", "S15",
                        law="S15 -- `hold` cardinality is 1 PER OBJECT")
    return live[0] if live else None

# The write matrix's name for the carrier `World.docket` holds (`(DocketItem, matter)`) -- the kind an
# `existence` cell names to ask *is this matter on a docket* (`WorldReader.read`'s `docket` branch).
DOCKET_KIND = "DocketItem"


def docketed(w: World, matter: Optional[str]) -> list[dict]:
    """THE DOCKET ITEMS NAMING `matter` -- the one owner of *is this matter before a room* (plan
    position `19`; `21_RECONCILIATION.md` PHASE 2 step 10). Read by the reader's `docket` branch
    (`exists:DocketItem`, `determine`'s docket conjunct) and by the two effects that write the
    cell: `open_case` declines a matter already on it, and `determine` takes the matter off it.

    A docket item is a plain dict on `World.docket` (a `_STATE_SEQUENCES` member, so the content
    hash folds it): CALENDAR forms one per sitting with `matter: None` (`loop/calendar.py`, an empty
    slot), and `open_case` fills the nearest open slot, by ancestry from the matter's place, when the
    matter is a person (v9 SC-01 fired-slot step, `slot_for`) or, where none is open, appends `{"date": None, "matter": <subject>,
    DOCKET_ARRANGEMENT: <row id or None>, DOCKET_PETITION: <Record id or None>}` -- a filled slot has
    the same keys and keeps its `date` (v9 SC-03a, K-55: the item names the arrangement
    it is heard under and the petition it rose from; `docketed_under` reads the first). `matter is None` is never
    docketed -- an empty slot names nothing, and a `None` subject asks about nothing -- so a
    determination that CLEARS an item's matter (writes it back to `None`) takes the matter off the
    docket without deleting the slot the calendar formed."""
    if matter is None:
        return []
    return [d for d in w.docket if d.get("matter") == matter]


# v9 SC-03a (#453 §10.4 step 2b, K-55): THE TWO KEYS A DOCKET ITEM GAINED, named once, `TERM_KEY`'s
# shape (`loop/effects_governance.py`) -- each is also the PAYLOAD key a hand-built `open_case`
# declares it under, so the act's word and the item's word cannot drift. `DOCKET_ARRANGEMENT` names an
# `arrangements.yaml` row (`_eff_determine` reads the kind it `disposes:`); `DOCKET_PETITION` names the
# `petition` Record the matter rose from (its reader, `interrogate` and the contested bench reading the
# charge the petition's `terms` names, is #453 §10.4 step 5's, not yet built). A computed `open_case`
# carries neither -- no operand channel names them (`H-80`/§F1) -- and writes both as `None`.
DOCKET_ARRANGEMENT = "arrangement"
DOCKET_PETITION = "petition"


# CALENDAR's Event kind for a date that came due, named once: `loop/calendar.py` emits and chains
# on it, and `sittings_before` reads it; WITNESS deposits it as the claim's predicate
# (`Claim.predicate` is `e.kind`).
FIRED_KIND = "date.fired"


def slot_venue(w: World, item: dict) -> Optional[str]:
    """THE VENUE OF THE SITTING A DOCKET ITEM WAS FORMED FOR -- its Date's `venue` -- or `None` for a
    dateless item (`open_case`'s, where no sitting was convened) or a date the world no longer holds.
    v9 SC-01 fired-slot step: the name for *which room is this item before*, read by
    `open_slots`/`slot_for` (the act that fills a slot) and `sittings_before` (the bench that hears
    it). Read straight off `w.dates`, not through `place_of`: that answers a person, site, record or
    rung id as well, and a docket item whose `date` names one of those is no sitting."""
    return (w.dates.get(item.get("date")) or {}).get("venue")


def _is_person_id(w: World, x) -> bool:
    """`x` names a person the world holds (a matter that is a person; `slot_for`, `sittings_before`)."""
    return isinstance(x, str) and x in w.persons


def open_slots(w: World, venue: Optional[str]) -> list[dict]:
    """THE EMPTY SLOTS A SITTING AT `venue` HAS ON THE DOCKET, oldest first -- the items CALENDAR formed
    (`{"date": <id>, "matter": None}`, `loop/calendar.py`, for a date that fired WITH a holder) whose
    Date sits at `venue` and whose `matter` is `None`. v9 SC-01 fired-slot step: `_eff_open_case`
    fills the first (through `slot_for`), where it used to append a dateless item beside it. A slot a determination emptied
    (`_eff_determine` writes the matter back to `None` and keeps the slot) is open again: a sitting
    hears matters one after another, and nothing rules when a sitting ends. `None` venue: none."""
    if venue is None:
        return []
    return [d for d in w.docket if d.get("matter") is None and slot_venue(w, d) == venue]


def slot_for(w: World, matter: Optional[str]) -> Optional[dict]:
    """THE SLOT A NEWLY OPENED MATTER FILLS, or `None` -- v9 SC-01 fired-slot step. The first open slot
    (`open_slots`) of the NEAREST sitting whose venue holds the matter: walking up from where the
    matter is (`place_of`) through `ancestry` (the start rung included), so a sitting at the matter's
    own settlement is filled before one at its duchy. ONLY A PERSON FILLS A SLOT: the one writer that
    empties a slot is `_eff_determine`, whose party cell binds a person, so any other matter (a rung,
    a Record -- `open_case` accepts any id) would hold its slot for ever and be asked about every
    season; it appends the dateless item instead. [ASSUMPTION; medium; Jordan to correct --
    Jordan names another key] THE VENUE IS THE MATCH KEY, matched by the containment walk the bench
    itself is found by (`sits_over`): `_eff_convene` keys its Date on `venue`, and a sitting hears
    what stands within it -- so any judge `judging_set` seats over the venue also sits over the
    matter's place, and `determine`'s `bench` conjunct holds wherever the slot was found. A matter
    with no place (`None`) fills nothing. REVERT: return `None` (every case appends a dateless item)."""
    if not _is_person_id(w, matter):
        return None
    place = place_of(w, matter)
    if place is None:
        return None
    for r in ancestry(w, place):
        slots = open_slots(w, r)
        if slots:
            return slots[0]
    return None


def sittings_before(w: World, p: Person) -> list[tuple]:
    """THE FIRED SITTINGS WITH A MATTER BEFORE `p`'s BENCH, AND THE CLAIM BY WHICH HE KNOWS EACH FIRED --
    `[(date id, claim, (matter, ...)), ...]` in docket order. v9 SC-01 fired-slot step (H-163 limit 2,
    #453 pass-1 step 4): `questions_for`'s sitting question, *a judge is asked about a docketed
    matter*. A sitting is before `p` when:
      * a docket item formed for its Date holds a matter that is a person (`slot_venue`,
        `_is_person_id`; a dateless item is no sitting, an empty slot names nothing, `docketed`'s
        rule, and a non-person matter is one `determine` can never clear -- `slot_for` admits none,
        and a hand-planted one is skipped here; a date left with no such matter is no sitting);
      * `p` is on the bench at its venue (`judging_set`, the one owner of who sits over a rung);
      * `p`'s OWN ledger holds a `date.fired` claim about that venue made ON THE FIRING'S TICK --
        CALENDAR's Event, deposited firsthand at WITNESS since IN-29, and CALENDAR fires a date only
        at its `due_at`. A judge who never heard the sitting fired is not asked; HEARSAY OF A FIRING
        (a claim landing on a later tick) IS NOT ADMITTED, and a later firing at the same venue does
        not stand for an earlier one. The claim is also what the question cites, so an act formed
        from it walks back to the firing (`occasioned_by`'s `claim_landed` route). Newest such
        claim, by `LedgerReader`'s comparator.
    ⚠ ONE CONVENE IS A STANDING COURT: `open_slots` re-opens a slot a determination emptied, and
    nothing rules when a sitting ends, so its bench is asked again whenever a new matter fills it.
    World-reading by construction, as `vacancies` and Q4 are (`questions_for`'s docstring): what is on
    the room's docket is the room's own business, and its bench is told."""
    by_date: dict[str, list] = {}
    for item in w.docket:
        matter = item.get("matter")
        if _is_person_id(w, matter) and slot_venue(w, item) is not None:
            by_date.setdefault(item["date"], []).append(matter)
    out = []
    for did, matters in by_date.items():
        venue, due = w.dates[did]["venue"], w.dates[did].get("due_at")
        heard = [c for c in p.ledger if c.subject == venue and c.predicate == FIRED_KIND
                 and c.when == due]
        if heard and p.id in judging_set(w, venue):
            out.append((did, LedgerReader(heard).belief_among(), tuple(dict.fromkeys(matters))))
    return out


def docketed_under(w: World, matter: Optional[str]) -> set:
    """THE ARRANGEMENT ROWS THE DOCKET HEARS `matter` UNDER -- every `DOCKET_ARRANGEMENT` named by an
    item `docketed` lists for it, `None` included for an item that names none. One element in every
    world an act built (`open_case` declines a matter already docketed); more than one only in a
    hand-planted docket, which `_eff_determine` declines rather than choosing between."""
    return {d.get(DOCKET_ARRANGEMENT) for d in docketed(w, matter)}


# ===========================================================================
# THE WORKS -- plan position `24e` (WORKS & FOUNDING), r2 `04_MATTER_AND_WORKS.md` §A.6. RESOLVER-SIDE
# Queries, World first, owned by nobody and storing nothing (`AX` T-a).
# ===========================================================================

# THE `record_kinds` MEMBER A WORKS IS. r2 §A.6's ruling: *"a `works` IS A `Record` KIND WITH
# ACT-DECLARED STAGES, OPENED BY THE `create_record` THAT ALREADY RUNS"* -- so it is named once here,
# `DOCKET_KIND`'s shape, for its four readers (`works_for` below, and `create_record`'s one-per-target
# decline, `found` and `build` in `loop/effects.py`). Refused at import if the roster stops carrying
# it: every works Query would otherwise match nothing forever and read as an honest absence.
WORKS_KIND = "works"
if WORKS_KIND not in RECORD_KINDS:
    raise Unspecified(
        f"record kind {WORKS_KIND!r} is not a `record_kinds` member ({sorted(RECORD_KINDS)})",
        "rosters.yaml -- record_kinds",
        needs=f"a `{WORKS_KIND}: [plan, at]` row, or every works reader retired with it",
        law="r2 04 §A.6 -- a works is a Record KIND; a reader keyed on a kind the roster does not "
            "carry answers 'none' for every world, which is a dead reader wearing a query's clothes")


def works_target(kind: Optional[str], content) -> tuple:
    """`(plan, at)` -- WHAT A WORKS MAKES AND WHERE -- read off a document of `kind` saying
    `content` (a Record's `kind` and `subject_matter`, or an act's declared ones before the mint), or
    `(None, None)` for a document that is no works or whose content is malformed.

    `plan` is a KIND (a `rung_kinds` member for `found`, a `site_kinds` member for `build`) and `at`
    is a RUNG id, so a works reads *"a <plan> at <at>"* (`rosters.yaml: record_kinds`' note says why
    r2's `{plan: {as, kind}}` was not taken). The key set is `Record.__post_init__`'s to refuse; this
    only declines to read what is not there, so a hand-planted Record cannot crash a reader -- and a
    `plan` or `at` that is not a plain id (r2's nested `{as, kind}`, a list) reads as no target at
    all, since every reader looks both up in a keyed store and an unhashable one would raise inside
    RESOLVE (`WorldReader.read`'s own unhashable-subject rule, one reader over)."""
    if kind != WORKS_KIND or not isinstance(content, dict):
        return (None, None)
    plan, at = content.get("plan"), content.get("at")
    if not isinstance(plan, str) or not isinstance(at, str):
        return (None, None)
    return (plan, at)


def works_for(w: World, at: Optional[str], plan: Optional[str]) -> list:
    """EVERY LIVE WORKS PLANNING A `plan` AT `at` -- the one owner of *which works names this*.

    LIVE means HELD: a works whose master's `hold` has ended (he died -- `World.remove_person` closes
    it -- or he destroyed the Record) bounds nothing and plans nothing, r2 §A.6.3's *"a works with no
    master is not a bound"*. `hold_force` is the reader of *who holds this*, and it RAISES on two
    holders rather than choosing. The kind and target are compared FIRST, so a world with no works
    reaches no `hold_force` scan at all (every world built before `24e`).

    ⚠ THE TARGET IS THE PAIR `(at, plan)`, AND ONE LIVE WORKS PER TARGET IS KEPT AT ITS ONE PRODUCER.
    r2 §A.6.3 rules *"one works per target"* and has `ceiling` RAISE on two, because a Query that
    picked one of two would answer *plausibly and wrongly, forever* (`AX` ID-5). r2 put the guard on
    `found`'s precondition as a `cardinality` conjunct -- but `cardinality` has no implementation
    (`data/requires.py`), and the thing that could make a second works is `create_record`, not
    `found`. So `_eff_create_record` declines a works whose target already has a live one (the
    grammar has no negation to spell it in the row), and `ceiling`'s raise is unreachable from any
    act -- a backstop against a hand-built world, not a refusal a season can meet."""
    if at is None or plan is None:
        return []
    return [r for r in (w.records[k] for k in sorted(w.records))
            if works_target(r.kind, r.subject_matter) == (plan, at)
            and hold_force(w, r.id) is not None]


# `matured_terms` -- HOW MANY OF A RECORD'S DECLARED TERMS HAVE RIPENED, counted off the log -- is owned by
# `state/attribution.py` since v9 IN-12 step 10 (the `anchor_of` cover read asks it, and `state/` imports
# nothing from `queries/`); imported above and read here by `ceiling`, unchanged.


def ceiling(w: World, site: Site) -> int:
    """HOW FAR A FABRIC MAY BE RAISED NOW -- r2 `04` §A.6.3's `ceiling`, DECIDED OFF THE EMISSION LOG:
    `condition_scale x matured // declared` for the one live works naming the site, and the full
    scale when none does (or when it declares no terms).

    *"Progress is the condition and PERMISSION TO PROGRESS is the ceiling, so nothing needs
    counting"* (r2 §A.6.1, which refused a `stage` key on the works for that reason). So
    *"you cannot hurry mortar"*: a fabric at its ceiling is raised by nobody until another term
    ripens, which is arithmetic, not a cooldown (r2 §A.6.6's TERM-STALL).

    A works NAMES a site when it plans that site's KIND at that site's RUNG (`works_for`), so one
    works bounds both the fabric it builds (`build` makes a `<plan>` at `<at>`) and the fabric of
    that kind already standing there -- which is r2's *"building and repairing are one act at
    different bands"* without a second matching rule.

    ⚠ MULTIPLY FIRST, DIVIDE LAST: `scale * n // d`, so a 2-of-3 works reads 666 and not 0 -- the
    fixed-point discipline `condition` is kept in (S48). `min(matured, declared)` makes the ratio
    total if a later act shortened the declared list below what the log has seen ripen.

    ⚠ IT IS A BOUND ON THE RISE AND NEVER A CUT. r2 wrote the clamp as `min(ceiling, condition +
    total)`, which would LOWER a standing fabric the moment a works naming it was declared (0 terms
    ripe: ceiling 0) and any delta was staged. The fold's one clamp (`loop/resolve.py::resolve`)
    therefore takes `max(condition, ceiling)` as its upper bound: a ceiling below a fabric's
    condition stops it rising, and takes nothing away that stands."""
    scale = w.fixtures.get("condition_scale")
    live = works_for(w, site.rung, site.kind)
    if len(live) > 1:
        raise Forbidden(
            f"{len(live)} live works plan a {site.kind!r} at {site.rung!r}: "
            f"{[r.id for r in live]}", "S15",
            law="r2 04 §A.6.3 -- one works per target, `hold_force`'s cardinality reading one "
                "object up; `create_record` declines a second, so this world was built by hand")
    if not live:
        return scale
    declared = len(live[0].stages)
    if declared == 0:
        return scale
    return scale * min(matured_terms(w, live[0].id), declared) // declared


def share(w: World, site: Site) -> tuple:
    """`share(w, ...)` -- DECLARED in `holonic_ARCHITECTURE.md` §17's resolver-side roster (`:600`)
    and never implemented until plan position `24e`. An actor's share of a fabric as a RATIO,
    `(1, n)`, where `n` is how many persons stand at its rung (`presence`), floored at one so a
    fabric nobody stands at is not divided by zero.

    r2 `04` §A.6.4, RULED: *"an actor's share of a fabric is one over the number of persons present
    at its rung. It is derived from a live edge, needs no field, and is the reading that keeps the
    commons."* NOT `Site.drawers` (deleted at `18a`; nothing could write it) and NOT `1` (mandatory
    single holdership, which makes single-act closure of a commons possible -- r2 cites
    `proposals/2026-08-31-ideal/10_SUPERSEDING.md:1275-1279`). ⚠ r2 DECLARES A SWEEP
    (`presence_reciprocal, holders_reciprocal, one`) and it is NOT built: a sweep is a fixture with a
    register row, and no measurement here needs a second arm yet -- the shape is ruled, the reading
    is the default, and `H-164` carries the unbuilt arms."""
    return (1, max(1, len(presence(w, site.rung))))


def judging_set(w: World, venue: str, matter: Optional[str] = None) -> list[str]:
    """`H-32`, BUILT -- plan position `18` (PROC-A), `21_RECONCILIATION.md` PHASE 2 step 7 /
    `03_PARAMETERS.md` §D's `bench_basis`. Live holders of a `hold` Tenure GRANTED the bench's
    basis AND whose Office's `scope_rung` CONTAINS `venue` -- the containment walk
    `ancestry(w, venue)` already owns (§8: the walk is a rule, lives once), not a bare equality,
    which is the "a purview walk one rung up still finds it" falsifier: a seat scoped one rung
    above `venue` still governs it. EMPTY SET -> the date fires and lapses; no forced decision
    (S61 -- *"nothing is decided at a sitting"* by fiat of this Query, only by who is actually
    seated).

    ⚠ THE GRANT, NOT THE OFFICE'S OWN FIELD -- plan position `13e`'s consolidation
    (`Tenure.granted_acts`, `H-71` arm 2). *"An office whose remit changes does so by an ACT ...
    a hand-mutation reaches nobody."* Reading `off.remit_acts` here would be a SIXTH reader of the
    field `13e` moved every consumer off of, and would let a bare attribute edit change who may
    judge without a `confer`/`establish` ever running -- exactly the drift that consolidation
    exists to stop. `test_13e_no_remit_acts_attribute_read_outside_the_three_allow_listed_sites`
    is the AST guard that catches a new reader of the retired field; this one reads the Tenure's
    own snapshot instead, the same as `person_side_eligible`.

    ⚠ `matter` IS ACCEPTED, NOT YET LOAD-BEARING. The design's signature is
    `judging_set(w, venue, matter)` because a per-arrangement `bench_basis` (`engine/season/arrangements.yaml`,
    part 3 of this same position) is meant to select the remit act a matter's disposal reads --
    but nothing yet maps a docketed matter to its governing arrangement row (that is PHASE 2 step
    10's docketing, explicitly weighed and left OPEN by this position's own record rather than
    built here). Until that mapping exists, `matter` is carried on the signature the design
    specifies and the basis is `H-32`'s own swept default, `"determine"` -- the one remit act any
    live matter in the corpus currently asks a bench to exercise. Wiring `matter` through is one
    line here (`basis = bench_basis_of(w, matter) or "determine"`) once that mapping exists, and
    is deliberately NOT invented now (§0.05: a mapping this position does not own is not smuggled
    in to make the signature look busier).
    ⚠ PLAN POSITION `19` BUILT THE DOCKETING HALF AND NOT THE MAPPING: `open_case` now puts a matter
    on `World.docket` (`docketed`, above), and `determine` asks this function -- through `WorldReader`'s
    `bench.size` stem -- for the bench at the matter's PLACE (`place_of`).
    ⚠ v9 SC-03a BUILT THE MAPPING'S CARRIER, AND STILL NOT THIS READ: a docket item now names its
    arrangement (`DOCKET_ARRANGEMENT`, `docketed_under`, written by a hand-built `open_case`; a
    computed one names `None`), and `_eff_determine` reads the row's `disposes:`. `matter` stays
    unused HERE, and the basis stays the one constant (`BENCH_BASIS`), because every seeded row's
    `bench_basis` is `determine` -- the constant already -- so
    wiring `bench_basis_of` would change no bench; it is the one line above, the day a row declares
    another basis.

    ⚠ A SEAT WITH NO `scope_rung` REACHES NOTHING -- the office-cluster case (S6.2, `Office.rung
    is None`) has no ground to be contained on, exactly as `purview_reaches` treats it. It is a
    CONTENT fact about such a seat, not a bug here.

    ⚠ CORRECTED (methodology close, terminal critique, 2026-09-29): THE PARAGRAPH ABOVE OVERSTATES
    THE EQUIVALENCE. `off.scope_rung is None` does NOT only happen in the office-cluster case
    (`off.rung is None`) -- `carriers.py::Office.__post_init__` auto-sets `scope_rung` ONLY for a
    TITLED post (`title_domain(self.post)` non-`None`); a seated, RANKED, non-titled office
    (`off.rung` set, no title) gets no `scope_rung` from the constructor. `offices.yaml` has no
    scope key to supply one: a seat's `scope_rung` is set by whoever BUILDS it -- the realm
    (`populated.build_realm`) sets `scope_rung = rung` for every authored row, and
    `corpus_run._seat_office` leaves an untitled seat at the titled-only default
    (`state/carriers.py`, `Office.__post_init__`). This function excludes a seat left at `None` from
    EVERY bench, silently, the same way it excludes a true cluster seat -- a different content fact
    than the one this docstring claimed, not the same one restated. `state/gate.py::purview_reaches` asks the same containment question of
    `off.rung` (always set for a seated office) and would not exclude it. This function reads
    `scope_rung` rather than `rung`/`purview_reaches` by `H-32`'s own ruled default
    (`hole_register.yaml`, H-32), which is precedent this correction does not reopen -- it corrects
    only the FALSE claim that the two fields' `None` cases coincide, not the choice of field.

    ⚠ PLAN POSITION `19`: THE TWO RULES THIS LOOP APPLIED ARE NOW NAMED AND OWNED IN `state/gate.py`,
    UNCHANGED -- the basis (`BENCH_BASIS`, was the local literal `basis = "determine"`) and the
    containment test (`sits_over`, was `off.scope_rung in set(ancestry(w, venue))`). The write gate's
    `determination` basis (`may_determine`) asks both of the seat a determination is exercised
    through, and a bench listed here by one reading and admitted there by another is the
    disagreement §8 forbids. Same answers: `test_field_deletions.py`/`test_stress_proceedings_
    rehost.py` pin them, and `ancestry` stays trace-free."""
    TRACE.query("judging_set", "resolver")
    seats: list[str] = []
    for t in w.tenures:
        if t.kind != "hold" or not t.live or BENCH_BASIS not in t.granted_acts:
            continue
        off = w.offices.get(t.object)
        if off is None or not sits_over(w, off, venue):
            continue
        seats.append(t.subject)
    return seats


# ===========================================================================
# THE ROOM READS YOU -- v9 SC-02 `22a`, proceedings `19_PLAN.md` PHASE 3 steps 17, 18 and 20 (intent).
# RESOLVER-SIDE Queries, World first, storing nothing. ⚠ NEVER IMPORTABLE FROM DECISION CODE: a person
# deciding whether to speak may not read the bench's ledgers or his opponent's -- he GUESSES them, and
# that guess is the game (`19_PLAN.md` step 18). `decision/` cannot name this module at all
# (`test_decision_package_never_names_world_anywhere_under_it`), and
# `engine/season/tests/test_sc02_reception.py` holds these two by name as well. The host input builder
# (`seam/wrappers/sigma.py::contest_input`) is their one caller; the obstacle they move is composed by
# the social contest module alone (`modules/social_contest/roll.py::obstacle`, ED-SC-0033 clause (3)).
# ===========================================================================

def remove_weight(source: str) -> float:
    """HOW MUCH A CLAIM HELD UNDER `source` COUNTS, by the ordinal of remove (`data/rosters.py::
    REMOVE_ORDINAL`, `19_PLAN.md`'s *firsthand > knot-sourced > told > inferred*):

        remove_weight = (K - k) / K,   k = the source's rank (0 strongest), K = the ranks

    1 firsthand, falling by `1/K` a rank, so every rank counts and a farther one strictly less.
    EQUAL SPACING is the [ASSUMPTION] `H-199` already makes for refraction's `channel_remove`, read off
    the same ranks; the form differs from `channel_remove`'s `k/(K-1)` only so the most removed rank
    still counts (an `inferred` claim is evidence, weaker; `1 - channel_remove` would weigh it zero)."""
    return (len(REMOVE_ORDINAL) - REMOVE_ORDINAL.index(source)) / len(REMOVE_ORDINAL)


_UNREAD = object()      # `reception`'s "not read yet" marker (None is a legitimate reading: no bluff called)


def reception(w: World, speaker: str, venue: Optional[str]) -> float:
    """HOW THE BENCH AT `venue` RECEIVES `speaker` -- `19_PLAN.md` step 17, the room reading the person
    who rises in it. Signed: above zero the bench is disposed toward him, below it against him.

        reception = Σ_h∈bench Σ_c∈deeds_h(speaker)  remove_weight(c.source) · c.confidence/full · v_h(c)

      * the BENCH is `judging_set(w, venue)` -- the one owner of who sits over a rung -- each seated
        person once, never the speaker himself (a man does not receive himself);
      * `deeds_h(speaker)` is `person_q.attributed_deeds` over `h`'s OWN ledger: the deed claims that
        record an act of the speaker's, a paired kind's doer read off its sighting's `seen.who`
        (R8.1's struct, `21_RECONCILIATION.md` PHASE 3's correction), never a bare subject;
      * `v_h(c)` is `person_q.deed_term` -- `h`'s own projected pursuits against the alignment of the
        act's kind (`data/verbs.py::align_kind`), the valence `regard` already reads. ⚠ THE VALENCE
        SOURCE WAS THE SWEPT CHOICE (step 17): THIS IS ARM 1, the existing alignment table, and it
        SHIPS BY DEFAULT, NOT BY WINNING. Arm 2, the dedicated regard table the plan names, was never
        authored: the arm run in its place read only the authored `deed:<kind>` cells (three kinds),
        so it was zero almost everywhere by construction and did not test the question (over three
        seeded realms it read non-zero on 19 (bench, speaker) pairs where arm 1 read 3,434;
        `hole_register.yaml` H-215 carries the numbers and says the sweep is open). The conflation
        arm 1 names -- what a hearer prefers to DO standing in for how he REGARDS a doer -- is
        recorded there, not resolved;
      * `full` is `confidence_default`, so a claim decayed to half counts half.

    STEP 20, ROUTE EROSION, INSIDE THE SUM: a hearer who holds, UNTOLD, a `dominance`-route deed done
    TO the speaker by somebody else (`person_q.suffered_deeds`; `rosters.yaml: standing_routes`) has
    called his bluff: every `dominance`-route deed of the speaker's that hearer holds no newer
    (`(when, round)`) than the latest such sighting counts zero. ⚠ `(when, round)` IS THE CLAIM'S
    DEPOSIT TIME, NOT THE DEED'S: a told or found copy is stamped with the tick it was deposited
    (`loop/witness.py`), so a hearer told after the bluff of a deed from before it keeps that copy
    at full weight; no field carries the deed's own tick on a copy (`H-215`'s named limit). One
    success against him is enough, and only the witnesses who saw it are moved; a challenger who
    fails suffers the deed himself, so the speaker's weight stands. A later coercive deed counts
    again.

    `venue` `None` (a placeless speaker) or an empty bench -> 0.0: nobody is in the room."""
    TRACE.query("reception", "resolver")
    if venue is None or speaker not in w.persons:
        return 0.0
    full = float(w.fixtures.get("confidence_default"))
    shift = w.fixtures.get("scar_weight_shift")
    total = 0.0
    for hid in dict.fromkeys(judging_set(w, venue)):
        h = w.persons.get(hid)
        if h is None or hid == speaker:
            continue
        called = _UNREAD            # the latest bluff called, read on the first dominance-route deed
        axis_w = None
        for c in attributed_deeds(h.ledger, speaker):
            if c.predicate in DOMINANCE_KINDS:
                if called is _UNREAD:
                    called = max(((s.when, s.round) for s in suffered_deeds(h.ledger, speaker)
                                  if s.predicate in DOMINANCE_KINDS), default=None)
                if called is not None and (c.when, c.round) <= called:
                    continue
            if axis_w is None:
                axis_w = projected_axes(h, shift)
            total += remove_weight(c.source) * (c.confidence / full) * deed_term(h, axis_w, c)
    return total


def proofs(w: World, speaker: str, opponent: Optional[str], venue: Optional[str]) -> float:
    """THE PROOFS `speaker` CAN SPEND AGAINST `opponent`, weighed by remove and discounted by the mirror
    -- `19_PLAN.md` step 18, a Query over two ledgers. Each deed claim in the speaker's OWN ledger
    recording an act of the opponent's (`person_q.attributed_deeds`) counts `remove_weight(c.source)`,
    UNLESS THE OPPONENT CAN MIRROR IT: he holds a claim with the same subject and predicate
    (`18_FINDINGS.md`'s mirror test, *does the opponent hold a claim with the same subject and
    predicate?*), and then it counts exactly zero. A non-person opponent holds no ledger and mirrors
    nothing. `venue` is the room that hears the speaker: with nobody on its bench (or no venue) there
    is no one to spend a proof on, and the answer is 0.0, the rule `reception` states.

    ⚠ NAMED LIMITS (`H-216`): every attributed deed counts, creditable or not and whatever the matter
    docketed (the plan's text asks for neither); the mirror keys on (subject, predicate) alone; and
    the arrangement's admitted `proofs` column is not read here.

    ⚠ WHAT IS TOLD IS EVERY SUCH CLAIM THE SPEAKER HOLDS, AND THAT IS A NAMED LIMIT, NOT THE DESIGN: the
    design spends proofs one at a time inside a nested run (`21_RECONCILIATION.md` step 15, unbuilt),
    which is where hoarding one becomes a choice; one `speak` is one act, so it spends its whole
    inventory. The mirror is still hidden from him -- nothing person-side reads it."""
    TRACE.query("proofs", "resolver")
    who = w.persons.get(speaker)
    if who is None or opponent is None or opponent == speaker or venue is None:
        return 0.0
    held = list(attributed_deeds(who.ledger, opponent))
    if not held or not any(hid != speaker for hid in judging_set(w, venue)):
        return 0.0
    opp = w.persons.get(opponent)
    mirror = {(c.subject, c.predicate) for c in opp.ledger} if opp is not None else set()
    return sum(remove_weight(c.source) for c in held if (c.subject, c.predicate) not in mirror)

# ⚠ `home_of(w)` WAS HERE; IT MOVED DOWN TO `state/containment.py` AT PLAN POSITION `19`, body and
# `TRACE` line unchanged, and is re-exported by this module's import block (`world_q.home_of is
# containment.home_of`). The write gate's `determination` basis asks where the PARTY a determination
# binds IS PRESENT (`home_of` reads `contain`, presence, since `19c`'s split -- residence is
# `residence_of`'s `reside` edge, and this basis was never revisited to say which it means), and
# `state/` may not import `queries/`: `parent_of`/`descendants`' G3 route.


def place_of(w: World, x: Optional[str]) -> Optional[str]:
    """`ARCH §F.14`'s OWN NAME, PROMOTED (position `11a`, r2 `01_ATTENTION_AND_REACH.md` §A.3).
    The rung a THING is at, for ANY id -- moved in from `epistemic._event_place`, which took only
    an Event. That caller becomes `event_place(w, e)`, below (`epistemic.py`'s two sites).

    ⚠ PERSON BEFORE RUNG, AND THE ORDER IS THE WHOLE OF THIS FUNCTION'S CORRECTNESS -- carried
    over from `_event_place`'s own docstring rather than restated: testing `x in w.rungs` FIRST
    would answer a person's own same-id `person`-kind Rung, and `Query.presence` on THAT answers
    "who is contained in themselves" -- nobody. A channel BROKEN CLOSED, not merely narrow, and
    `P15`'s history is the worked case (`epistemic.py`, `_ch_co_located`'s docstring). THIS IS A
    REPEAT of a conflation `witness` had already retracted once; the order is what prevents it a
    third time.

    Two limbs promoted `_event_place` did not have, plus the NO SILENT DEFAULT floor (`ID-5`):
      * person  -> `home_of(w)[x]` -- the single owner, not a hand-rolled `contain` scan.
      * site    -> `Site.rung`, the maintained side (S12).
      * record  -> its live holder's place (`hold_force` -- S15's cardinality-1 guard makes this
                   total), else the record's own `Record.rung` (non-optional).
      * date    -> `venue` -- `_eff_convene` always sets one, and `_req_convene` requires
                   `venue in w.rungs`, so this limb is total for every date the engine can mint.
      * rung    -> itself.
      * anything else, including `None` -> `None`. Absence maps to the refusal, never to a
                   plausible guess.

    ⚠ MAY NOT READ A LEDGER (`AX-2`) and MAY NOT BE CALLED FROM `decision/` -- world-first,
    `queries/world_q` only (`ARCH §A.2`: reads *any store, via `World`*). It answers ONE place; a
    multi-rung actorless Event (a plague spanning many rungs) is a named LIMIT this does not
    solve (`01` §A.3.1) -- `_ch_co_located`'s membership test stays exactly that, not an
    intersection, and widening the signature is `ARCH §F.14`'s own ruling text to amend, not an
    edit to make here."""
    if x in w.persons:
        return home_of(w).get(x)
    if x in w.sites:
        return getattr(w.sites[x], "rung", None)
    if x in w.records:
        h = hold_force(w, x)
        return place_of(w, h.subject) if h is not None else w.records[x].rung
    if x in w.dates:
        return w.dates[x].get("venue")
    if x in w.rungs:
        return x
    return None


def event_place(w: World, e) -> Optional[str]:
    """WHERE AN EVENT HAPPENED -- `place_of` of the causing act's actor for an act-caused Event, else of
    `anchor_of(w, e)` (v9 IN-12 step 10: a cover's anchor is not where anyone stood), the one expression the tree used for
    it at WITNESS (`epistemic._ch_co_located` and `epistemic.seen_subject`), now owned once, plus one
    limb `place_of` cannot carry: A DEATH HAS A PLACE (H-206).

    `World.remove_person` takes the dead out of `w.persons` and closes every edge naming him in the
    write that kills him, and WITNESS runs after. An Event no act caused (a death at MATTER) anchors
    on the removed person (`state/attribution.py`, tier 2), `place_of` of a person is `home_of(w)`'s
    LIVE `contain` edge, and so it answered `None` -- the event found no observer under any channel
    that needs a place, and a dead seat-holder was reported to nobody. A death at RESOLVE anchors on
    the killer, who is alive, which is why only the MATTER-written one was lost.

    The limb, for an ACTORLESS Event only (no act among its causes): when the anchor is a person the
    world NO LONGER HOLDS, his place is where he stood when
    `remove_person` took him out, if that was this Event's own tick (`World.departed_from`) -- the
    container of the `contain` edge the cascade closed. It cannot be read off `w.tenures`: a Tenure is
    owned by its subject, so his own edge left the store with him (probed on `build_realm(0)`).
    It is NOT `place_of`'s person limb, deliberately: `place_of` is also asked about the dead by
    `reach` (a claim about a dead man), and answering there would move every reader of an old
    claim; only an EVENT's own tick has a place for him. ⚠ ACTORLESS ONLY, MEASURED: without that clause
    the limb also placed the refusals of a victim's own acts later in the killing tick (`act.ineligible`,
    `travel.blocked`, ... anchored on the dead ACTOR, tier 1); the class is reproduced by
    `test_h206_an_act_caused_event_of_the_dead_actor...`. `None` otherwise, exactly as before.

    The limb places every ACTORLESS Event anchored on a person removed in that Event's own tick, so
    at MATTER also the same dying cohort's `body.changed` and its tier-3 `condition.band_crossed`
    (reachable only at `body_step > 0`, unmeasured; H-206), and an actorless MATTER Event about a
    person killed at RESOLVE later in the same tick, e.g. `travel.ended` (`loop/matter.py`'s travel
    pass), which is reachable at shipped defaults and unmeasured (H-206)."""
    # v9 IN-12 step 10: AN ACT-CAUSED EVENT IS PLACED WHERE ITS ACTOR STOOD, NOT WHERE ITS ANCHOR IS.
    # A cover's anchor is the cover's id, and `place_of` of a Record is its LIVE holder's place
    # (or, once the holder's hold closed, `Record.rung` -- the actor's own id for a computed
    # `conceal`, which `remove_person` pops): CENSUS then indexed `w.rungs` by a dead person and
    # raised, and a cover `give`n away moved an earlier round's Event. Uncovered, the anchor IS the
    # actor (tier 1), so this is the old answer.
    a = causing_act(w, e)
    if a is not None:
        return place_of(w, a.actor)
    who = anchor_of(w, e)
    here = place_of(w, who)
    if here is not None:
        return here
    return w.departed_from(who, e.emitted_at)     # `departed_from(None, t)` is None


# ⚠ v9 SE-01 (`24g`), P1's OTHER HALF -- THE PERSON-KEYED CROSSING REPAIR IS THE PERSON LIMB ABOVE,
# AND NO NEW CODE WAS NEEDED FOR IT. The plan's instruction (*"`world_q` derives `at` from
# `w.sites.get(who)`; the repair is `at = parent_of(w, who)` when `who` names a person"*) was written
# against Q3's old `w.crossings` tuple read, which position `11a` deleted: a crossing now reaches a
# witness through `epistemic._ch_co_located` as `event_place(w, e)` (`place_of` of its anchor), and for a person that
# is `home_of(w)[who]` -- the person's one live `contain` parent, which is `parent_of(w, who)`. So a
# cohort's `condition.band_crossed` (anchored, tier 3, on its own `body.changed`) is placed at the
# settlement the cohort stands in, and everyone standing there is `co_located` with it.
# `tests/test_territorial_subsistence.py::test_se01_a_person_keyed_crossing_is_placed_at_the_person_s_parent`
# executes it under a non-zero `body_step`; the plan position is stale on this half, not open.


def ever_named(w: World, eid: str) -> bool:
    """Has the world held or recorded this id? `class_of` has no `dates` and forgets the dead, so
    "unheld" is not "never was": a date is held (`place_of` admits it as a referent), and a recorded
    id is one a logged Event's change already names -- the death names the dead (`person.died`), the
    convening names the date. (A log scan: the cost a tombstone set on `World` would remove, and a
    carrier change, so not here.)"""
    return (w.class_of(eid) is not None or eid in w.dates
            or any(c.subject == eid for e in w.log for c in e.changes))


def demanded_person(w: World, a) -> Optional[str]:
    """v9 SE-01 (`24g`) / `H-51` -- P3: THE PERSON AN ACT DEMANDS, or `None`.

    An act DEMANDS a person when its `subject` operand names an id THE WORLD DOES NOT HOLD -- the
    order to a clerk nobody has individuated. `World.class_of` is the one resolver of *which
    collection holds this id*, and its `None` is documented as *"NOT YET, NOT NOT A THING"*, which is
    exactly what a demand is: a person not yet individuated. ⚠ AN ID THE WORLD HOLDS AS SOMETHING
    ELSE IS NOT A DEMAND: a `dispatch` naming a building (measured on `build_realm(0)`, 2 seasons:
    14 of 15 `dispatch` acts name a rung, site or record and are refused) asks for no person, so it
    individuates nobody. An act naming no subject at all demands nobody either.

    Read through `binding_from_act`, the one reader of an act's operands, so this and the fold's
    `subject` are one value. Read twice: by the fold, which earns `person.demanded` on the refusal
    of a row that declares it (`loop/resolve.py`), and by CENSUS, which individuates the id it names
    (`loop/census.py`) -- one owner of the PREDICATE. They agree because of stratum order, not
    because there is one owner: the fold reads the log before this RESOLVE's Events are appended,
    CENSUS after, so a death folded earlier in the same RESOLVE pass would be invisible to the first
    and visible to the second (unreachable today: `dispatch` is a binding decision and resolves
    before the contested physical acts that kill)."""
    s = binding_from_act(a).get("subject")
    return s if isinstance(s, str) and s and not ever_named(w, s) else None


def reach(w: World, p: Person) -> set[str]:
    """`01_ATTENTION_AND_REACH.md` §A.4 -- the ids a question may be ABOUT for this person. A
    FILTER over what a WITNESS channel already deposited, and never a fan (§A.4.4, LB-2b): it is
    not called from `witness`, `observers_for` is untouched, and `questions_for`'s Q2 still reads
    only `p.ledger` -- so a claim not already in this person's own ledger cannot become a question
    no matter how wide `reach` is. World-first, owns nothing, stored nowhere, recomputable at any
    barrier (`ARCH §A.2`).

    FOUR LIMBS, none of them a new rule -- each composes on an existing owner (§A.4.2):
      1. me                  -- `{p.id}`, today's first Q2 disjunct.
      2. mine                -- every live Tenure's object -- `questions_for`'s own `mine`, read
                                 the same way.
      3. the ladder above me -- `ancestors-or-self` of `home_of(w)[p.id]`, via `parent_of` -- the
                                 walk `ancestry` (below) owns. `under_purview` and
                                 `conferral_path` made it too, and are deleted (`13d-i`, `18a`).
      4. purview             -- `{seat.rung} | descendants(seat.rung)` over every live `hold` on
                                 an Office with a rung. `descendants` EXCLUDES its own rung
                                 (`state/containment.py`), so the seat's own rung must be unioned
                                 in explicitly, or a Duke seated at his own duchy would never be
                                 reached by a claim about the duchy itself -- LB-2e, the
                                 inclusive-walk falsifier.

    ⚠ MAY NOT READ A LEDGER, NOT EVEN `p`'S OWN (`AX-2`): a reach computed from beliefs would make
    "what I may be asked about" a function of what I believe, and a false belief would silently
    widen the world I can act on (`01` §A.4.3). MAY NOT read another person's tenures -- it answers
    for `p` alone."""
    TRACE.query("reach", "resolver")
    R = {p.id}
    R |= own_purview(w, p)                                       # limbs 2 and 4
    cur, seen = home_of(w).get(p.id), set()
    while cur is not None and cur not in seen:
        R.add(cur); seen.add(cur); cur = parent_of(w, cur)
    return R


def own_purview(w: World, p: Person) -> set[str]:
    """`reach`'s limbs 2 and 4, extracted ONCE (v9 IN-57, `CLAUDE.md` §8) so `reach` and
    `attention_key`'s tier 1 read one rule: every live Tenure's object (`mine`), and
    `{seat.rung} | descendants(seat.rung)` over every live `hold` on an Office with a rung (the
    inclusive walk, LB-2e). Reads `p`'s own tenures and the office/rung stores only; no ledger
    (`reach`'s AX-2 note). Writes no TRACE row of its own, but `descendants`, which it calls,
    writes a `TRACE.query` (`state/containment.py`), and `reach` and `attention_key` each compute
    it, so one `questions_for` walks a seat's subtree twice. Handing one computation to both moves
    `runs/TRACE.txt` and `results.json`'s QUERY count (measured: 29,405 -> 28,620; no game state
    moves), which is why the two calls stand."""
    P = set()
    for t in p.tenures:
        if not t.live:
            continue
        P.add(t.object)
        if t.kind == "hold" and t.object in w.offices:
            rg = w.offices[t.object].rung
            if rg is not None:
                P |= _subtree(w, rg)
    return P


def governors_of(w: World, rung_id: Optional[str]) -> list[str]:
    """v9 IN-22 (#457 `CARRY-SHORTFALL`, `H-160` limit 2) -- THE PERSONS WHOSE SEAT'S PURVIEW REACHES
    `rung_id`: every live `hold` on an Office for which `state/gate.py::purview_reaches` answers
    True, by its holder, sorted. `[]` for a rung no seat reaches and for `None`; a rungless seat's
    holder is listed only through `purview_reaches`' oblige clause (v9 IN-40), never by its own ground.

    ⚠ v9 IN-40: WHERE THE OBLIGE CLAUSE FIRES, THIS IS WIDER THAN `reach`'s LIMB 4, which may not read
    another person's tenures and so cannot see a sworn holder's seats. A superior listed here for his
    vassal's ground is deposited a claim no question of his admits. Measured inert in `build_realm(0)`
    (its one live `oblige`'s swearer holds no seat); named, not repaired, at IN-40.

    ⚠ THE SAME RELATION AS `reach`'s LIMB 4, ASKED FROM THE RUNG'S SIDE. Limb 4 unions
    `{seat.rung} | descendants(seat.rung)` over the person's own holds, and `purview_reaches` is
    `rung == seat.rung or rung in descendants(seat.rung)` (plus, v9 IN-40, the oblige clause above) --
    one walk (`descendants`), so a person this lists by his OWN ground has `rung_id` in `reach(w, p)`,
    and a claim about `rung_id` deposited into his ledger is admitted by `questions_for`'s clause 1.
    A person listed ONLY through the oblige clause does not (paragraph above): there the deposit is
    not admitted by any question. Where it is his own ground, that is what makes the WITNESS route that calls this
    (`loop/witness.py`, the purview deposit) end in a question rather than in a silent ledger slot.

    ⚠ A WORLD READ, AND NOT A FAN BY ITSELF. It reads `w.tenures`/`w.offices`/the containment tree
    and no ledger (`AX-2`). WHO RECEIVES WHAT is `loop/witness.py`'s rule, which narrows this to an
    actorless Event's reads; `reach` stays a filter over what a deposit already put in a ledger
    (`01` §A.4.4) and is not called from WITNESS."""
    if rung_id is None:
        return []
    return sorted({t.subject for t in w.tenures
                   if t.kind == "hold" and t.live and t.subject in w.persons
                   and t.object in w.offices
                   and purview_reaches(w, w.offices[t.object], rung_id)})


def named(c) -> tuple:
    """CLAUSE 3's `named(c)` -- position `15c`, r2 `01_ATTENTION_AND_REACH.md` §A.5.3/§A.5.4 and
    `02_THE_WRIT_AND_THE_WORD.md` §A.9.1. The id set inside a `content:<kind>` claim's value, so
    that a writ can name someone into a question WITHOUT a place query -- `holonic §37.3`'s
    *"scope enumerates EXECUTORS, not places."*

    ⚠ **RULED: read from `record_kinds`, never from the value's strings.** `RECORD_CONTENT`'s
    `addressee` key (`rosters.yaml: record_kinds.content`) names the ONE key, shared by every
    kind that has one, under which an addressee id list sits -- `to`, for `dispensation` and
    `petition` alike. A generic *"every id anywhere in the value"* would make a `works` plan's
    site ids into addressees and a petition's `from` into a summons; this reads the roster that
    types the schema, which is one owner for both facts. A kind with no such key (`works`,
    `text`) simply has no `to` entry, so this returns `()` for it without a second branch.

    `()` -- never `None`, so a bare caller need not guard -- for a claim whose `predicate` does
    not start `content:`, or whose `value` names nobody. Takes a `Claim`, not a `World`: it reads
    one object already in hand, the same shape as `place_of(w, c.subject)` beside it in `Q2`, and
    is not a second read of `p.ledger` (`AX-2` stays satisfied by the caller's own loop).

    ⚠ A SECOND KIND OF CONTENT NAMES SOMEBODY: A DECLARED INTENT (telling `T7`, G9; v9 IN-16). A
    hearer told that the teller will do an act holds `(teller, intent:<verb>, ((name, id), ...))`
    (`rosters.yaml: intent_claim`), and the ids it carries are whom the intent is aimed at. Read
    through `person_q.intent_named`, the one owner of that value's shape, so a hearer whose reach
    covers the act's target is asked about the teller -- *the realm hears what A means to do to B*.
    No intent claim exists while `intent_disclosure` is 0, so the branch reads nothing there."""
    got = intent_named(c)            # `()` unless the stem is the intent's, which is never `content:`
    if got:                          # (`person_q._check_intent_claim`'s `taken` refuses that at import)
        return got
    said = content_said(c)           # `person_q`'s one reader of the content claim's shape
    if said is None:
        return ()
    ids = said.get(RECORD_CONTENT.get("addressee"))
    return tuple(ids) if ids else ()


def nearest_store(w: World, rung_id: Optional[str], kind: str,
                  available: Optional[dict] = None) -> Optional[str]:
    """THE LARDER LADDER: the nearest rung AT OR ABOVE `rung_id` holding any `kind`, or `None`.

    ⚠⚠ IT EXISTS BECAUSE THE SUBSISTENCE ECONOMY IS TWO HALVES THAT NEVER MEET. MEASURED on
    `build_realm(0)` after one season, before this Query: **4,810 units, every one of them at the
    37 SETTLEMENT rungs and none at the 211 hearths**, while all 46 persons live in **26 hearths**
    — so `matter`'s per-rung draw counted **zero eaters at every rung that had stores** and the
    whole subsistence step was INERT on a world that runs. The walk is the join, and it moves no
    matter and creates no store: a person reaches UP the ladder they already live on.

    ⚠ IT RETURNS THE RUNG ITSELF WHERE THE RUNG HAS STOCK, which is what makes this a
    GENERALISATION rather than a replacement. A hearth with its own larder feeds its own people
    exactly as before; the walk is a no-op wherever the old per-rung code was already right. That
    is the control `LB-3a` pairs with, and if it ever moves, the walk is not a generalisation.

    ⚠ `None` AT THE ROOT IS A SHORTFALL, NEVER AN ERROR. A person under a realm that holds nothing
    goes hungry, and hunger is a fact about the world; raising here would make an empty larder an
    instrument defect. What the caller does with it is the caller's — today MATTER records it and
    acts on nothing (L5: a threshold crossing MAY NEVER PRODUCE AN OUTCOME).

    ⚠ `available` IS THE CALLER'S RUNNING VIEW DURING ONE DRAW, and it is the reason two eaters
    cannot spend the same unit. `{(rung_id, kind): units_left}`; absent, the world's own stores
    answer. Without it a caller that defers its writes — as MATTER must, because the gate applies
    the write — would show every eater the FULL larder and scarcity would never bind, which is the
    exact defect `loop/effects.py`'s own header names for `transfer` (*"`transfer` twice from a
    one-unit larder succeeds twice: the scarcity §27.1 rests on never happens"*).

    ⚠ ITERATIVE WITH A VISITED SET, on `descendants`'s precedent (S38.1). `contain_ascends` makes
    the ladder strictly ascending at `add_tenure`, so a cycle should be unreachable — but a walk
    that hangs on a malformed fixture is a worse failure than one that stops, and the guard costs
    one set."""
    TRACE.query("nearest_store", "resolver")
    seen: set = set()
    cur = rung_id
    while cur is not None and cur in w.rungs and cur not in seen:
        seen.add(cur)
        if available is not None:
            held = available.get((cur, kind))
            if held is None:
                held = (w.rungs[cur].stores or {}).get(kind, 0)
        else:
            held = (w.rungs[cur].stores or {}).get(kind, 0)
        if held > 0:
            return cur
        cur = parent_of(w, cur)
    return None


def season_of_year(w: World) -> Optional[int]:
    """v9 IN-21: which season of the year `w.tick` falls in, or `None` when no year is declared. The
    year is the length of `season_factor_draw`'s table (one entry per season, in order), so the
    calendar position is READ OFF `tick` and no field stores it. A world declaring no table has no
    year to be in, which is the control (`season_factor` alone)."""
    table = w.fixtures.get("season_factor_draw")
    return w.tick % len(table) if table else None


def season_factor_of(w: World) -> float:
    """v9 IN-21 / `H-26`: the multiplier on this season's `yield`. THE ONE OWNER of the term MATTER's
    yield step scales by.

    `season_factor` is the constant (swept 0.5 / 1 / 2). When `season_factor_draw` declares a table
    the factor is that constant times ONE outcome drawn from the current season of the year's entry,
    the outcomes equally likely. The draw is KEYED, not random: `ids.draw_factory`, seeded from `(world_seed, tick, ...)`, is the
    same mint every id uses, so the same seed twice gives one hash and two seeds differ. An EMPTY
    table is the control arm and returns the bare constant, so the default world's arithmetic is
    untouched (`test_season_weather.py` holds the three-hash equality)."""
    base = w.fixtures.get("season_factor")
    s = season_of_year(w)
    if s is None:
        return base
    outcomes = w.fixtures.get("season_factor_draw")[s]
    if not outcomes:
        # An empty season entry has nothing to draw from; without this `choose` below dies with a
        # bare IndexError naming neither the fixture nor the season.
        raise Unspecified(f"`season_factor_draw` season {s} declares no outcomes", "H-26",
                          needs="at least one multiplier per season, or `()` for the control",
                          law="IN-21: each season of the year holds the equally likely multipliers it draws from")
    draw = draw_factory(w.world_seed, lambda: w.tick)("world", "season_factor")
    return base * draw.choice(outcomes)


def age_of(w: World, pid: str) -> int:
    """v9 IN-34: how many seasons old `pid` is -- `w.tick - Person.born`. READ OFF THE CLOCK, never
    stored (IN-21's `season_of_year` precedent), so no write is needed for anyone to age. This and
    `body_hazard` are the only readers of `Person.born` (ID-13)."""
    return w.tick - w.persons[pid].born


def body_hazard(w: World, pid: str) -> float:
    """v9 IN-34 FORCE-BODIES: THE CHANCE `pid` DIES OF AGE OR ILLNESS THIS SEASON. The one owner of
    the term MATTER's bodies pass draws against; a Query over `Person.born` (ID-13: a hazard is a
    reader over a field, never a stored value).

    `illness_rate + age_step * age`, capped at 1. Both rates ship at 0, the control, so this returns
    0 and MATTER takes no draw. A rate outside [0, 1] raises (`telling_privacy`'s rule, `H-190`): a
    NaN or a negative chance must refuse, not answer.

    ⚠ A COHORT HAS NO HAZARD, AND THAT IS THE RECORDED POPULATION BOUND, NOT A SPECIAL CASE. A
    cohort is a population (S9, `Person.is_cohort`; `ED-IN-0255`), and what bounds a population is
    E-1's answer as recorded -- matter plus hearth capacity (`ED-SE-0051`, RR-2) -- not one
    person's old age. It is `SE-01`'s split from the other side: only a cohort goes hungry, only an
    individual ages."""
    age_step = float(w.fixtures.get("age_step"))
    illness = float(w.fixtures.get("illness_rate"))
    for name, rate in (("age_step", age_step), ("illness_rate", illness)):
        if not 0 <= rate <= 1:        # `not ... <=`, so a NaN is refused too
            raise ValueError(f"{name} {rate} is not a chance in [0, 1] (H-208)")
    p = w.persons[pid]
    if p.is_cohort or (age_step == 0 and illness == 0):
        return 0.0
    return min(1.0, illness + age_step * max(0, age_of(w, pid)))


def subsistence_draw(w: World) -> dict:
    """THE LARDER DRAW, AS A RECORD: `{person id: (home rung, {kind: (want, take, source)})}` -- what
    every housed eater asks of the larder ladder this season, what the ladder gives them, and from
    which rung. Read-only; it writes nothing. Plan position `19d`.

    ⚠ EXTRACTED FROM MATTER, NOT WRITTEN BESIDE IT. `loop/matter.py`'s larder pass (item 3a) did
    exactly this arithmetic inline, and `demanded`/`delivered` below need the same arithmetic. With
    two copies of *what an eater wants, and what the walk gives them*, MATTER could feed a person
    whom the Queries report as hungry (§8). MATTER now calls this and derives its writes and its
    `_subsistence_shortfall` from the record; the two Queries sum it over a subtree. So there is
    one owner, and the Queries cannot disagree with the draw that actually runs.

    ⚠⚠ ONLY A COHORT EATS (plan position `24f`, `ED-IN-0255`, Jordan 2026-09-18: *"NPC synecdoches
    that just represent the overall population affected ... i don't think having lords and guild
    members etc worry about subsistence is worthwhile"*; *"it's a territorial issue"*). A person at
    `weight == 1` -- a named individual, the office-holder the ruling names -- is NOT IN THE RECORD:
    he wants nothing, draws nothing, is never short, and so MATTER never falls his body for dearth.
    The test is `Person.is_cohort`, S9's own sentence, owned once on the carrier. It is HERE, in the
    one owner, and not at MATTER's loop, so `demanded`/`delivered` and the body write cannot
    disagree about who eats (§8). WHO EATS INSTEAD is `cohorts.yaml`: authored `weight > 1` rows,
    one per populated rung, seated by `harness/populated.py::build_realm` at world-gen
    (`ED-WR-0011` option A -- nothing mints one at run time). The exemption landed IN THE SAME
    COMMIT as that producer, because alone it empties this record on every built world: `Person
    .weight` defaults to 1 and no builder set it higher (the plan's own attack on the candidate,
    `_part2` 24f). A world with no authored cohort -- the corpus's `build_at`, `tiny_world`,
    `headless`, the spine -- therefore has no eater, and `H-171` says so.
    REJECTED, each for a reason: exempting by OFFICE (a seat is not what the ruling measures -- a
    guild member holds none, and an unseated lord is still a lord); exempting at MATTER only (the
    Queries would then report a hunger the draw no longer feeds); keeping the individual in the
    record at `want = 0` (a row that can never be short is noise every reader must skip).

    THE ARITHMETIC IS ITEM 3a's, UNCHANGED, and every clause keeps its reason (see MATTER's pass):
      * per housed COHORT (`home_of`), in SORTED id order: the write order must be deterministic;
      * per `subsistence_weight` kind, SORTED: `want = weight x Person.weight`, skipped when `<= 0`.
        `Person.weight` is the cohort multiplier, *"A COHORT IS A PERSON AT weight > 1"*, so a
        synecdoche of two hundred wants what two hundred eat (`24f`'s territorial quantity is this);
      * the source is `nearest_store` over the RUNNING view `left`, so two eaters cannot spend the
        same unit (`nearest_store`'s own `available` paragraph);
      * `take = min(want, held)`, and the remainder is NOT walked further up. `source None` means
        no rung at or above the home holds any of that kind.
    No weights registered gives `{}`, which is MATTER's own `if weights:`.

    ⚠ IT DOES NOT `TRACE`, on `ancestry`'s rule: a helper extracted to remove duplication must be
    INVISIBLE to its callers. The `home_of` and per-eater `nearest_store` calls inside it trace
    exactly as MATTER's inline loop did, in the same order, so MATTER's trace and every committed
    artifact are unchanged by the extraction. MEASURED at `19d`: the regenerated `runs/` are
    byte-identical, and so are four worlds' content hashes, event counts and claim counts
    (`headless`, `governance_spine`, `tiny_world`, `populated.build_realm(0)`). The in-tree control
    is `test_w15_report_py_reproduces_every_committed_artifact_byte_for_byte`."""
    weights = w.fixtures.get("subsistence_weight")
    out: dict = {}
    if not weights:
        return out
    homes = home_of(w)
    left: dict = {}           # (rung, kind) -> units still unspent this draw
    for pid in sorted(homes):
        person = w.persons[pid]
        if not person.is_cohort:
            continue                  # `24f`: the individual does not eat from the larder (above)
        row: dict = {}
        # `H-11`'s rule, unchanged: the loop is over the WEIGHTS registry, so a kind with no weight
        # is not drawn at all -- a missing row is never read as a weight of zero.
        for k, wt in sorted(weights.items()):
            want = wt * person.weight
            if want <= 0:
                continue
            src = nearest_store(w, homes[pid], k, available=left)
            if src is None:
                row[k] = (want, 0, None)
                continue
            held = left.get((src, k))
            if held is None:
                held = (w.rungs[src].stores or {}).get(k, 0)
            take = min(want, held)
            left[(src, k)] = held - take
            row[k] = (want, take, src)
        out[pid] = (homes[pid], row)
    return out


def demanded(w: World, rung_id: str, draw: Optional[dict] = None) -> dict:
    """`{kind: units}`: WHAT THE PEOPLE UNDER `rung_id` NEED FROM THE LARDER IN A SEASON. It is the
    sum of every housed eater's `want` whose home is `rung_id` or any rung beneath it -- and since
    `24f` an eater is a COHORT (`subsistence_draw`), so this is the TERRITORIAL quantity `ED-IN-0255`
    asks for: the need of the population synecdoches under a rung, never a lord's. Plan position
    `19d`, the retirement plan's G3: *"two new read-only queries (`demanded`, `delivered`)"*.

    ⚠ A NEED IS A QUERY, NOT A THING A PLACE HAS. `01_AXIOMS.md` §D.10 (ratified): *"a need | a
    `Sensation` plus a Query"*, and *"every aggregate | a Query, owned by Nobody (T-a)"*. A Rung owns
    *"arrangements, not wants"* (probe `F19`'s law, S36.1), so this Query is not a demand the place
    makes. Nobody files it. It is the arithmetic of the mouths under a roof, and something happens
    about it only when a person learns of it and acts: `loop/matter.py` records the gap on the
    drained larder's own write, WITNESS deposits it as a claim, and
    `decision/options.py::_from_shortfall_claim` reads that claim into a `transfer`.

    ⚠ AN R-1 AGGREGATE OVER THE CONTAINMENT SUBTREE (`_subtree`: the rung and its descendants), and
    §22.4 clause 2 does not bar it. That clause forbids a Query that sums a per-person TALLY across
    holders, which is a monotone counter in a ledger. `want` is `Person.weight` (a cohort's head
    count, `T-l`) times a registered table, so this is `density`'s weighted HEADCOUNT and not a
    tally. It reads live `contain` edges only, through `home_of` (clause 3).

    ⚠ `draw` is MATTER's own record when MATTER asks, so the numbers are the draw that ran. When it
    is omitted, it is the draw the stores AS THEY NOW STAND would give. For `demanded` the two agree
    anyway: `want` reads no store. Kinds are those `subsistence_weight` registers with a positive
    want; `delivered` returns the same keys.

    REJECTED READINGS, each for a reason:
      * ROUND ONE'S `demanded(levy, rung)` -- the share a `levy:` policy clause demanded of a rung
        (`proposals/2026-09-17-governance-and-holdings/01_SEATS_AND_POLICY.md` §A.13). Its carrier
        is gone: r2 withdrew both Queries (`04_MATTER_AND_WORKS.md` §A.3.4, §B.2), superseded the
        policy clauses with the writ (`02_THE_WRIT_AND_THE_WORD.md`), and ruled `levy` deleted
        (§A.20). What a writ demands is already `15c`'s `_from_content_claim`.
      * THE STORES THEMSELVES (`Rung.stores` against some notion of population). A store is supply,
        not need; a rung holding nothing still has mouths under it.
      * THE EATERS WHOSE WALK *ENDS* AT `rung_id`. That set depends on which rungs hold stock, so an
        empty settlement would demand nothing: the need would vanish exactly where it is unmet."""
    TRACE.query("demanded", "resolver")
    return _drawn_under(w, rung_id, draw, 0)


def delivered(w: World, rung_id: str, draw: Optional[dict] = None) -> dict:
    """`{kind: units}`: WHAT THE LARDER LADDER DELIVERS AGAINST `demanded(w, rung_id)`. It is the sum
    of the same eaters' `take`, from whichever larder at or above their home the walk found. So
    `demanded - delivered`, per kind, is exactly the unmet subsistence of the people under the rung.
    That is the shortfall. Plan position `19d`, G3's second Query.

    ⚠ IT IS THE DRAW ITSELF, NOT A LEDGER OF WHAT ARRIVED. Given MATTER's record (`draw`), this is
    what MATTER delivered. Without it, this is what MATTER's draw would deliver from the stores as
    they now stand: the arithmetic of the next draw, read without writing. It is never stored.
    `Rung.__setattr__` refuses an aggregate field (*"L3 -- every aggregate is a function, never a
    field"*).

    REJECTED READINGS, each for a reason:
      * MATTER DELIVERED IN BY `transfer` (G3's phrase *"delivery between settlements"*, read
        literally as the `transfer.made` receipts landing on the rung). A transfer lands in STORES,
        and the draw already reads stores. Counting both measures one flow twice. A count over past
        receipts is also monotone in the log, which is §22.4 clause 3's ratchet. The act restocks
        the larder, and the larder feeds the people: r2 `04` §A.3, *"MATTER STAYS WHERE IT IS
        PRODUCED. IT MOVES ONLY BY `transfer`. EATERS DRAW UP THE CONTAINMENT LADDER, AND THE WALK
        IS THE WHOLE MECHANISM."*
      * `World._subsistence_shortfall` subtracted from `demanded`. That field is census-only. Its
        own site says *"never read by the loop"*. It is also a snapshot of the last MATTER, so
        subtracting it from a LIVE demand mixes two instants. A person who moved since would count
        in one term and not the other.
      * ROUND ONE'S `delivered(levy, rung, season)`, for `demanded`'s reason above."""
    TRACE.query("delivered", "resolver")
    return _drawn_under(w, rung_id, draw, 1)


def _drawn_under(w: World, rung_id: str, draw: Optional[dict], i: int) -> dict:
    """The shared body of `demanded` (`i = 0`, want) and `delivered` (`i = 1`, take): one pass over
    the draw record, keeping the eaters homed in `rung_id`'s subtree. Both read the same cells, so
    both return the same keys. Does not `TRACE`; its two callers own their names."""
    here = _subtree(w, rung_id)
    record = subsistence_draw(w) if draw is None else draw
    out: dict = {}
    for _pid, (home, row) in record.items():
        if home not in here:
            continue
        for k, cell in row.items():
            out[k] = out.get(k, 0) + cell[i]
    return dict(sorted(out.items()))


def presence(w: World, rung_id: str) -> list[str]:
    """S28 -- the PRESENCE INDEX the global fan-out reads."""
    TRACE.query("presence", "resolver")
    return [t.subject for t in w.tenures
            if t.kind == "contain" and t.object == rung_id and t.live
            and t.subject in w.persons]


# ===========================================================================
# RESIDENCE -- plan position `19c` (MIGRATE). Where a person LIVES, as distinct from where they ARE.
# ===========================================================================

# THE `tenure_kinds` MEMBER A RESIDENCE IS, named once for its readers here and for the builders that
# mint one per person (`WORKS_KIND`'s shape). `loop/effects.py::_eff_migrate` spells the literal at
# its one `Tenure(...)` construction, because `data/verbs.py::_derive_openers_from_effects` reads a
# kind off that call as a string CONSTANT. Refused at import if the roster stops carrying it: every
# residence Query would otherwise match nothing and read as a world where nobody lives anywhere.
RESIDE_KIND = "reside"
if RESIDE_KIND not in TENURE_KINDS:
    raise Unspecified(
        f"tenure kind {RESIDE_KIND!r} is not a `tenure_kinds` member ({sorted(TENURE_KINDS)})",
        "rosters.yaml -- tenure_kinds",
        needs=f"a `{RESIDE_KIND}` member, or every residence reader retired with it",
        law="plan position `19c` -- a residence is a Tenure; a reader keyed on a kind the roster "
            "does not carry answers 'nobody lives here' for every world")


def residence_of(w: World) -> dict:
    """`{person id: the rung they LIVE in}` for every person with a live `reside` edge -- `home_of`'s
    mirror, and the reason the two are separate Queries is the whole of plan position `19c`.

    `home_of` reads `contain`: WHERE A PERSON IS (`04_CODE_ARCHITECTURE.md` §B, *"its contain edge is
    where they are"*), which `move` re-homes. This reads `reside`: WHERE THEY LIVE, which only
    `migrate` changes (`_eff_migrate`'s docstring carries the design and the rejected carriers). Every
    world builder mints a `reside` beside each person's first `contain`, so at build the two agree
    and they diverge exactly when somebody travels without settling.

    ⚠ A PERSON WITH NO LIVE `reside` IS ABSENT FROM THE MAP, NEVER DEFAULTED TO WHERE THEY STAND. A
    fallback to `contain` would make every writer of `contain` a silent writer of residence -- the
    read/write asymmetry `CLAUDE.md` §0.1 pt 1 names -- and a `move` would then re-home everyone a
    builder did not mint for. Absent means of no fixed abode (a hand-built world, today), and such a
    person counts toward no rung's `population`.

    ⚠ TWO LIVE `reside` EDGES FOR ONE PERSON RAISE, on `hold_force`'s rule: `_eff_migrate` closes the
    old edge in the same write that opens the new, so two can only come from a hand-built world, and
    a Query that picked one would answer plausibly and wrongly forever (`AX` ID-5)."""
    TRACE.query("residence_of", "resolver")
    out: dict = {}
    for t in w.tenures:
        if t.kind != RESIDE_KIND or not t.live or t.subject not in w.persons:
            continue
        if t.subject in out:
            raise Forbidden(
                f"{t.subject!r} has two live `{RESIDE_KIND}` edges ({out[t.subject]!r}, "
                f"{t.object!r})", "S15",
                law="plan position `19c` -- a person lives in ONE place; `migrate` closes the old "
                    "residence as it opens the new, so this world was built by hand")
        out[t.subject] = t.object
    return out


def restrained(w: World, person: Optional[str], kind: str) -> bool:
    """DOES `person` OWN A LIVE EDGE OF THE RESTRAINT `kind` -- a `detain` (he is in custody) or a
    `ban` (he is excluded)? v9 SC-03a (#453 §10.4 step 3, K-53): the ONE read behind every reader
    the two kinds ship with, so *is this man a prisoner* cannot mean one thing to `move` and another
    to a muster: `_eff_move`/`_eff_migrate` and `loop/sides.py` ask it of `DETAIN_KIND`,
    `_req_oblige` and `_eff_confer` of `BAN_KIND`.

    ⚠ ANY SEAT, AND THAT IS AN [ASSUMPTION; medium; revert: also require the edge's object seat's
    purview to reach where the restraint is read]: a custody holds a man everywhere (he is not free
    to travel to a place the detaining seat does not govern), and #453 §8.1 states the ban's readers
    without a scope (*"a banned person cannot serve or be seated"*). A kind off `RESTRAINT_KINDS` is a
    caller defect -- every other kind has a reader of its own -- and raises rather than answer False."""
    if kind not in RESTRAINT_KINDS:
        raise InstrumentDefect(
            f"`restrained` asked of {kind!r}, not a restraint kind ({sorted(RESTRAINT_KINDS)})")
    if person is None:
        return False
    return any(t.kind == kind and t.subject == person and t.live for t in w.tenures)


def population(w: World, rung_id: str, residence: Optional[dict] = None) -> int:
    """HOW MANY LIVE UNDER `rung_id`: the summed `Person.weight` of everyone whose `residence_of` is
    the rung or any rung beneath it. RR-2's capacity bounds POPULATION (its floor is *"applied here
    to births rather than acts"*), and this is the population it bounds. Plan position `19c`.

    RESIDENTS, NOT PERSONS PRESENT: a traveller standing in a town lives elsewhere and does not fill
    it, which is what makes `migrate` -- the act that makes someone a resident -- the one a full rung
    refuses, and `move` the one it does not (`_eff_migrate`'s docstring). `weight`, not a head count,
    because *"a cohort IS a Person at weight > 1"* (`state/carriers.py`): a household of two hundred
    fills two hundred places, as it eats for two hundred at the larder (`subsistence_draw`).
    ⚠ THE INDIVIDUAL STILL COUNTS HERE, THOUGH SINCE `24f` HE NO LONGER EATS THERE. The exemption is
    the larder's (`ED-IN-0255`: a lord does not worry about subsistence), not the roof's: a named
    person occupies a dwelling whether or not he draws on the granary, so housing and eating are two
    Queries and read `weight` two ways on purpose.

    ⚠ AN R-1 AGGREGATE AND §22.4 DOES NOT BAR IT, on `density`'s and `demanded`'s ground: a weighted
    headcount over live `reside` edges, not a per-person tally summed across holders (clause 2), and
    no ended edge is read (clause 3). ⚠ `Rung.envelope` -- the population not individuated as persons
    -- is NOT counted: it has no producer anywhere (`loop/census.py` writes no envelope), so a term for
    it would be a read of a dead carrier (`ID-13`). `24f` did not give it one: the territorial
    population it builds is carried by authored cohort PERSONS (`cohorts.yaml`, S9's one class), so
    it is counted above through `weight`, and `envelope` stays the ratified-but-unwritten field
    `04 §B.3` declares (`H-171`).

    `residence` -- a precomputed `residence_of(w)`, for a caller (`_eff_migrate`) that already built
    one this same act and would otherwise pay the full-Tenure scan twice (`/simplify`, BATCH-CLOSE
    Phase 2). `None` (every existing caller) computes it here exactly as before."""
    TRACE.query("population", "resolver")
    here = _subtree(w, rung_id)
    residents = residence_of(w) if residence is None else residence
    return sum(w.persons[pid].weight for pid, home in residents.items() if home in here)


# THE `site_kinds` MEMBER `capacity` COUNTS -- Jordan's `ED-SE-0055` (2026-09-25): *"add a `dwelling`
# SITE KIND; `build_realm` mints one dwelling Site per hearth rung; `capacity(w, rung)` queries
# descendant Sites of that kind"*. Named once, `WORKS_KIND`'s shape, and refused at import if the
# roster stops carrying it: `capacity` would otherwise count nothing and every rung would read its
# floor forever.
DWELLING_KIND = "dwelling"
if DWELLING_KIND not in SITE_KINDS:
    raise Unspecified(
        f"site kind {DWELLING_KIND!r} is not a `site_kinds` member ({sorted(SITE_KINDS)})",
        "rosters.yaml -- site_kinds",
        needs=f"a `{DWELLING_KIND}` member, or `capacity` retired with it",
        law="ED-SE-0055 -- capacity counts the rung's dwelling Sites; a count keyed on a kind the "
            "roster does not carry is a dead reader wearing a query's clothes")


def capacity(w: World, rung_id: str) -> int:
    """`ED-SE-0051` / RR-2, RULED: *"a `capacity(w, rung)` QUERY over the rung's dwelling Sites,
    with a FLOOR -- never a fixture table"*. Plan position `24d-ii`, landed IN THE SAME COMMIT AS ITS
    FIRST CALLER, `19c`'s `migrate` (a Query nobody calls is `ID-13`'s shape).

        capacity(w, rung) = max( floor[dwelling],  the dwelling Sites at `rung` and below it )

    * THE DERIVED QUANTITY IS THE SITES THEMSELVES: what one dwelling houses is not a cell (plan
      `24d-ii`, corrected 2026-09-25) -- a per-kind *houses N* is the `hearth_capacity` fixture RR-2
      refused. So `found` + `build` (`24e`) GROW capacity by standing a dwelling, and a `migrate` into
      a rung whose `population` would pass it is REFUSED -- RR-2's *"`found` is the throttle"*, read
      as the lever that lifts the bound rather than an act the bound refuses (`24d`'s reading).
    * THE FLOOR is `rosters.yaml: capacity_floor` (`H-167`, swept), read through the fixtures so a
      sweep reaches it. A lower bound on the derived count, `W5`'s floor-of-1 shape RR-2 cites: a rung
      with no dwelling at all still houses the floor, never zero.
    * THE RUNG'S OWN SITES COUNT: `descendants` EXCLUDES its own rung (`state/containment.py`), and a
      hearth's own dwelling hangs off the hearth by `Site.rung`, so the rung is unioned in explicitly
      (`_subtree`) -- a hearth counts its dwelling, and every ancestor counts it again. That is what
      makes one more dwelling under a rung raise its capacity and every ancestor's by the same step.
    * NOTHING IS STORED: `Rung.__setattr__` refuses an aggregate field, and this is recomputed at
      every call (`AX` T-a)."""
    TRACE.query("capacity", "resolver")
    here = _subtree(w, rung_id)
    built = sum(1 for s in w.sites.values() if s.kind == DWELLING_KIND and s.rung in here)
    return max(w.fixtures.get("capacity_floor")[DWELLING_KIND], built)


# ===========================================================================
# §14.2 -- THE POLITY QUERIES. "A faction IS a Proposition plus its `commit` edges."
#
# §22's `Nobody` row assigns FACTION, LEADERS, PRESENCE, DENSITY and FOOTPRINT to nobody, as
# Queries stored nowhere, and §17 names each in the resolver-side list. Four of the five had no
# body. They are written here rather than in a new module because `04 §A.2` types `queries/` as
# `world_q · person_q · cache` -- a `polity_q.py` for THESE functions would be a fourth member and
# a conformance defect, and these are world-first reads like every other function in this file.
#
# ⚠ `faction_q.py` IS NOT A COUNTEREXAMPLE TO THIS RULE; IT IS A DIFFERENT CASE, DISTINGUISHED AT
# ITS OWN SITE. This paragraph's "no fourth module" holds for functions §A.2 does not name outside
# this file -- exactly the case for `members`/`leaders`/`footprint` below, and for `WorldReader`
# before unit L3 folded it in. `faction_q.resolve` is named by its OWN dotted path in §B.6.1 and
# §C.5.1, both ratified, neither touched by this docstring's reasoning; see `faction_q.py`'s and
# `queries/__init__.py`'s own docstrings for why that is a genuinely different ambiguity, named
# rather than resolved the same way.
#
# ⚠ THE SEMANTICS ARE NOT TRANSCRIBED, BECAUSE §17 GIVES ONLY `name(w, ...)`. What IS transcribed
# is the definition each rests on -- §14.2 for membership, §15's cardinality table for the edge
# kinds, §22.4's three L3 clauses for what an aggregate may compose over. Where the argument list
# or the denominator is this module's choice, the docstring says so in those words.
#
# ⚠ EVERY ONE READS LIVE EDGES ONLY. §22.4 clause 3 REFUSES any aggregate monotone in the ENDED
# edge set -- `count{commit}` over live AND ended rows is "members ever", which is a ratchet built
# out of structural edges. `t.live` is not a filter for tidiness; dropping it changes the kind of
# thing the function is.
# ===========================================================================

def members(w: World, faction: str) -> list[str]:
    """Everyone with a LIVE `commit` to this Proposition. §14.2: *"Membership is `commit`."*

    ⚠ THIS IS THE WHOLE OF MEMBERSHIP AND THERE IS NO SECOND ROUTE. Before this, the only way a
    person belonged to a faction was to hold an Office whose `body` resolved to one -- so a
    faction had no laity, no rank-and-file and no congregation, and `role_templates` keyed on
    faction described a population that could not exist. `commit` was already the ruled edge and
    was carrying only a person's private want."""
    TRACE.query("members", "resolver")
    return sorted(t.subject for t in w.tenures
                  if t.kind == "commit" and t.object == faction and t.live
                  and t.subject in w.persons)


def leaders(w: World, faction: str) -> list[str]:
    """The members who hold an Office belonging to this faction. §17 · §22's `Nobody` row.

    ⚠ IT IS THE INTERSECTION AND NOT EITHER HALF, which is the claim worth stating: an
    office-holder who has not committed is staff, not a leader, and a committed member holding no
    office is a member. Both readings were available and this one is what §14.2 leaves room for --
    the faction is the Proposition plus its commits, so leadership has to be read THROUGH
    membership rather than beside it.

    ⚠ `Office.faction` IS DERIVED AT CONSTRUCTION from `body` (`Office.__post_init__`), so this
    never re-derives it and cannot disagree with the constructor.

    ⚠⚠ TWO IDENTIFIERS NAME ONE FACTION, AND THIS FUNCTION HAS NOW RETURNED `[]` FOR A WORLD WITH
    LEADERS IN IT TWICE, FOR TWO DIFFERENT REASONS. `members` keys on the PROPOSITION ID
    (`fac_hafenmark`) because that is what a `commit` edge points at; `Office.faction` carries the
    FACTION NAME (`Hafenmark`) because that is what `rosters.yaml: factions` holds and what
    `office_faction` validates against. So a translation is needed, and WHERE IT READS THE NAME
    FROM is the whole question.

    The first writing compared the two identifiers directly. The second read `Proposition.subject`,
    which was the faction's name -- until the creed commit made `subject` the LEADER'S PERSON ID
    for every faction that has a creed and moved the name to `value`, leaving this reader pointed
    at a field whose meaning had changed underneath it. MEASURED at `build_realm(0)`: `[]` for
    Crown, Church of Solmund, Hafenmark and Varfell -- all four factions that hold seats -- hiding
    19 of 19 occupied offices.

    It now reads `FACTION_BY_PROP`, which `data/rosters.py` DERIVES from the roster, so there is no
    field to guess and no mood to dispatch on. ⚠ BOTH FAILURES WERE INVISIBLE FOR ONE REASON: `[]`
    is a plausible answer for a faction with no office-holders -- four of the eight genuinely have
    none -- so nothing raised, and a test asserting `leaders <= members` is satisfied by the empty
    set. `test_leaders_are_found_for_every_faction_that_holds_a_seat` asserts the non-empty case."""
    TRACE.query("leaders", "resolver")
    name = FACTION_BY_PROP.get(faction, faction)
    held = {t.object: t.subject for t in w.tenures if t.kind == "hold" and t.live}
    inside = set(members(w, faction))
    return sorted(who for oid, who in held.items()
                  if who in inside
                  and oid in w.offices and w.offices[oid].faction == name)


def footprint(w: World, faction: str) -> list[str]:
    """Every rung the faction REACHES: the rungs it holds, plus the rungs its members sit in.

    ⚠ THE UNION IS THIS MODULE'S CHOICE AND THE TWO HALVES ARE DIFFERENT CLAIMS. Holding is
    title; presence is reach. A faction with members in a city it does not hold has a footprint
    there and no claim to it, which is the distinction the strategic layer turns on, so collapsing
    to either half alone would answer a different question. §14.2 names `footprint` beside
    `presence` and `density` without defining any of the three.

    ⚠ A FACTION HOLDS A RUNG AS THE `hold` SUBJECT, WHICH §15's TABLE TYPES AS `Person -> ...`.
    §14.2's own closing note is the licence and the warning: *"A Proposition may be a `hold`
    subject and is never destroyed, so a memberless faction leaves territory held by a banner
    nobody carries."* That defect is declared there and is not repaired here."""
    TRACE.query("footprint", "resolver")
    out = {t.object for t in w.tenures
           if t.kind == "hold" and t.subject == faction and t.live and t.object in w.rungs}
    inside = set(members(w, faction))
    out |= {t.object for t in w.tenures
            if t.kind == "contain" and t.live and t.subject in inside and t.object in w.rungs}
    return sorted(out)


def _subtree(w: World, rung_id: str) -> set:
    """`rung_id` plus everything under it, by containment (`descendants`). Extracted (M4 review
    pass, `/simplify` reuse finding): `density`, `mustered` and `fortification_of` each wrote
    `{rung_id, *descendants(w, rung_id)}` independently -- `mustered`'s own docstring already
    named the duplication ("density's own composition, one line above") rather than ending it."""
    return {rung_id, *descendants(w, rung_id)}


def density(w: World, rung_id: str, faction: str) -> tuple[int, int]:
    """`(members of this faction present, persons present)` over the containment subtree.

    An R-1 aggregate: computed on demand over descendants, never received and never stored
    (§22.4 clause 1's licensed shape). It counts PEOPLE, never anything a person holds inside
    them -- clause 2 bars a Query that sums a per-person tally across holders, and a headcount is
    not one.

    ⚠ THE DENOMINATOR IS PERSONS PRESENT, NOT THE FACTION'S TOTAL MEMBERSHIP, so this reads as
    *"how much of this place is theirs"* rather than *"how much of them is in this place"*. The
    other denominator is the other question; both are one line, and the caller should say which
    it means rather than this returning a bare ratio."""
    TRACE.query("density", "resolver")
    here = _subtree(w, rung_id)
    inside = set(members(w, faction))
    present = [t.subject for t in w.tenures
               if t.kind == "contain" and t.live
               and t.object in here and t.subject in w.persons]
    return sum(1 for p in present if p in inside), len(present)


def mustered(w: World, rung_id: str, faction: str) -> list[str]:
    """M4 (`ED-IN-0279` clause (a)). This faction's members present in `rung_id`'s subtree --
    settlement plus everything under it, Jordan's ruling on what "present at the target" means
    for a march (planning round 2). `density`'s own composition, one line above, minus the count:
    person containment seldom terminates AT a settlement rung in the seeded corpus -- every person's
    `contain` targets a `home` building beneath one (`harness/populated.py`) -- so a literal exact-rung
    read finds nobody home, and the subtree is the only reading that finds anyone at all. (Since v9
    IN-13 an ARRIVED army's `contain` DOES terminate at the settlement rung, `_eff_march`'s legs.)

    Who a march may draw on at its origin, and who a field battle's defending side draws from at
    its target -- both the same query, the faction and the rung simply swapped. `04 §C.5.1`'s own
    pseudocode: *"squad combat: the squad is `members ∩ present-at-rung`"*."""
    TRACE.query("mustered", "resolver")
    here = _subtree(w, rung_id)
    inside = set(members(w, faction))
    return sorted(t.subject for t in w.tenures
                  if t.kind == "contain" and t.live
                  and t.object in here and t.subject in inside)


def fortification_of(w: World, rung_id: str) -> float:
    """M4 (`ED-IN-0279` clause (a)). A settlement's defensive strength, `0.0` to `1.0`, read off
    the `garrison` Site(s) in `rung_id`'s subtree -- `H-38`'s *"`Site.condition` is the model"*
    applied to fortification, Jordan's choice over a cohort-Person alternative (planning round 2).
    `0.0` with no garrison in the subtree: an unfortified settlement, not a refusal -- absence of
    a garrison Site is a legitimate world state (`harness/populated.py`'s M4 build step 11 seeds
    one per settlement, but nothing enforces that it must).

    ⚠ MULTIPLE GARRISONS AVERAGE RATHER THAN SUM: one per settlement is what step 11 ships, and an
    average keeps the return in `[0.0, 1.0]` regardless, which summing would not.

    ⚠ ITS CALLER IS THE BATTLE PATH (plan position `20-iv`, `H-150`; until then nothing called
    this). `seam/wrappers/mass_battle.py::resolve()` reads it at the march target and passes it to
    `massbattle.resolve_field` as `fort_level`, where any positive value makes the field A.9's
    WALLS row (`terrain.py::terrain_row_for_territory`). This Query decides none of that."""
    TRACE.query("fortification_of", "resolver")
    here = _subtree(w, rung_id)
    garrisons = [s for s in w.sites.values() if s.kind == "garrison" and s.rung in here]
    if not garrisons:
        return 0.0
    scale = w.fixtures.get("condition_scale")
    return sum(s.condition for s in garrisons) / (scale * len(garrisons))


def enclosing_territory(w: World, rung_id: Optional[str]) -> Optional[str]:
    """v9 IN-35: the first `territory` rung on `rung_id`'s containment walk up (`ancestry`, the one
    walk; the rung itself included), or `None` where the walk meets none -- a Site at the realm or a
    duchy, or a rung outside the tree. Read by `loop/matter.py::_lattice_strain`, which couples a Site
    to the Sites of its own and the bordering territories (`data/geography.py::adjacent_territories`).
    Traces nothing, as `ancestry` traces nothing: the coupling's control arm never calls it."""
    for r in ancestry(w, rung_id) if rung_id else ():
        rung = w.rungs.get(r)
        if rung is not None and rung.kind == "territory":
            return r
    return None


def closed_uses(w: World, rung_id: str) -> dict:
    """v9 IN-35, THE CALAMITY'S EFFECT PER TERRITORY, AS A QUERY OVER BAND FLOORS (#457 `:131`):
    `{site id: (the site-use verbs it has fallen below, sorted)}` for every Site in `rung_id`'s
    containment subtree that is below at least one floor of its kind. Composed on `verbs` (S12.1's one
    owner of *condition gates verbs*) against `band_floors` keyed by the Site's kind. ⚠ THE BAND TABLE
    KEYS ON SITE KIND AND THIS QUERY KEYS IT ON A TERRITORY BY CONTAINMENT, so no territory-keyed floor
    is needed and none is written (`H-38`: one band scheme). Computed on demand and never stored (L3).

    ⚠ ITS READER IS A REPORT, `harness/populated.py::census` (`uncontrolled`'s precedent: a report, not
    a rule). No decision reads it: what a person meets is the crossing itself, an Event `_crossings`
    emits and WITNESS fans out, and the use it closed, which the `floor` stem and `yield` already read
    off `Site.condition`. Empty where nothing in the subtree is below a floor."""
    floors_all = w.fixtures.get("band_floors") or {}
    here = _subtree(w, rung_id)
    out: dict = {}
    for sid in sorted(w.sites):
        s = w.sites[sid]
        if s.rung not in here:
            continue
        floors = floors_all.get(s.kind, {})
        shut = tuple(sorted(set(floors) - verbs(w, s, floors)))
        if shut:
            out[sid] = shut
    return out


def sovereign_fraction(w: World, rung_id: str) -> tuple[float, int]:
    """§17's one Query with a DECLARED return type: `-> (fraction, undetermined_count)`.

    Over the rungs of the subtree: the share held by the single largest holder, and how many are
    held by nobody. The signature is the architecture's; the denominator -- DETERMINED rungs only,
    so an unheld rung lowers nothing and is reported separately -- is this module's reading of why
    §17 bothered to return the second number at all. A fraction over all rungs would make
    `undetermined_count` derivable and therefore pointless.

    ⚠ `0.0, 0` FOR A SUBTREE OF ONE UNHELD RUNG IS THE HONEST ANSWER AND NOT A FAILURE. Nobody
    holds anything, so no fraction is sovereign; the caller distinguishes that from a contested
    subtree by the second number, which is what it is for.

    ⚠ PERSON-KIND RUNGS ARE EXCLUDED, AND THE FIRST WRITING COUNTED THEM. `descendants` walks
    `contain`, and a person's own rung is contained like everything else, so a realm with four
    inhabitants reported four more `undetermined` places than it has. Counting heads in the
    denominator makes a populous duchy look less determined than an empty one. The exclusion is
    this module's reading and is stated rather than silent -- §10's ladder does put `person` on it,
    and `own` eligibility is "a person governing themselves", so the other reading exists and is
    simply not what this Query answers.

    ⚠⚠ `undetermined_count` IS NOT "UNHELD TERRITORY", AND THIS DOCSTRING USED TO SAY *"sovereignty
    is over TERRITORY"*, WHICH INVITED EXACTLY THAT READING -- a reviewer made it. EVERY OTHER rung
    kind in the denominator is GOVERNABLE: `offices.yaml: titles: domains:` declares a title for
    each (moved from `rosters.yaml: titles`, position `8a`, 2026-09-29 -- `TITLE_DOMAINS`/
    `title_domain` in `data/rosters.py` read the survivor), and `Family Head` governs
    `community`, `Mayor` governs `settlement`, `Lord` territory, `Duke`/`Duchess` duchy,
    `King`/`Queen` realm. So an unheld hearth is a governable seat nobody holds, not noise.

    MEASURED at `build_realm(0)`, `r_valoria`: `(0.4, 304)`, and those 304 are
    `hearth 205 · community 58 · settlement 36 · duchy 3 · territory 1 · realm 1`. That shape is
    the WORLD's, not this Query's -- the populated world seats 19 offices and none below
    territory. A caller wanting unheld TERRITORY filters `w.rungs[r].kind` itself; this number is
    every governable rung in the subtree that nobody holds, which is what §17 asked for."""
    TRACE.query("sovereign_fraction", "resolver")
    here = [r for r in [rung_id, *descendants(w, rung_id)]
            if r in w.rungs and w.rungs[r].kind != "person"]
    holder_of: dict[str, str] = {}
    for t in w.tenures:
        if t.kind == "hold" and t.live and t.object in w.rungs:
            holder_of[t.object] = t.subject
    held = [holder_of[r] for r in here if r in holder_of]
    undetermined = len(here) - len(held)
    if not held:
        return 0.0, undetermined
    top = max(held.count(h) for h in set(held))
    return top / len(held), undetermined


def provinces_of(w: World, rung_id: str) -> dict:
    """`{faction Proposition id: [territory ids]}` — the provinces that EXIST right now.

    ⭐ `systems/settlements/reference/scale_hierarchy_v1.md` §2, **RATIFIED, direct Jordan ruling
    2026-07-13**: *"Provinces are only formed if the same faction holds the constituent
    territories … territories are the fixed geographic units; a province is an emergent aggregation
    that exists only while its constituent territories share a common faction holder."* It replaces
    PP-726 §2.3's fracturing state-machine: *"A province isn't a container that sometimes breaks —
    it's a name for 'these territories, right now, cohering under one faction.'"*

    ⚠⚠ SO A PROVINCE IS A QUERY AND NOT A RUNG, AND THAT IS THE RULING ARRIVING AT THE SAME PLACE
    §22 DOES FROM THE OTHER SIDE. §22.1's reason for giving every aggregate to Nobody — *"if the
    aggregate is a function it cannot go stale, and it cannot be initialised and then forgotten"* —
    is exactly what an existence-conditional province needs: the moment a territory changes hands
    the province it was part of stops existing, and nothing has to be told. `province` stays a
    declared `rung_kind` (the ladder names it, and `contain_ascends` permits `territory -> duchy`
    directly), and `build_realm` builds none.

    ⚠ NO MINIMUM SIZE IS IMPOSED, BECAUSE CANON STATES NONE. A single territory held alone comes
    back as a group of one. Jordan's title note — a Count governs ONE province, a Lord may govern
    several territories *"that have not been assembled into a province"* — implies a threshold
    exists without giving it, so the caller decides and this does not invent one.

    ⚠ LIVE `hold` EDGES ONLY, like every aggregate here (§22.4 clause 3).

    ⚠⚠ THE ROOT RUNG IS NOT IN ITS OWN SUBTREE HERE, AND IT IS IN `sovereign_fraction`'s. Both
    docstrings say "the subtree" and they mean different sets -- `descendants(w, rung_id)` versus
    `[rung_id, *descendants(...)]` -- so `provinces_of(w, 'terr_T1')` is `{}` while
    `sovereign_fraction(w, 'terr_T1')` is `(1.0, 33)` for the same held territory.

    THE REASON IS WHAT EACH QUESTION IS ABOUT. Sovereignty is a property OF the rung asked about,
    so its own holder belongs in its own answer. A province is an aggregation of the territories
    BENEATH one, so the rung asked about is the container and not a member.

    ⚠ AN EARLIER DRAFT OF THIS PARAGRAPH JUSTIFIED IT BY SAYING THE ROOT WOULD OTHERWISE "report a
    lone territory as a province of one, which the ruling refuses" -- AND THAT IS FLATLY
    CONTRADICTED EIGHT LINES ABOVE, where this same docstring says *"NO MINIMUM SIZE IS IMPOSED,
    BECAUSE CANON STATES NONE. A single territory held alone comes back as a group of one."* The
    code agrees with the older paragraph: the grouping below applies no cardinality filter. Written
    down because two incompatible readings of one ratified sentence, both in one docstring, is the
    §4 idempotence trap -- and it was a fresh adversarial read that caught it, not this author."""
    TRACE.query("provinces_of", "resolver")
    here = {r for r in descendants(w, rung_id)
            if r in w.rungs and w.rungs[r].kind == "territory"}
    holder_of: dict[str, str] = {}
    for t in w.tenures:
        if t.kind != "hold" or not t.live or t.object not in here:
            continue
        fac = faction_holding(w, t.subject)
        if fac is not None:
            holder_of[t.object] = fac
    out: dict = {}
    for terr, holder in sorted(holder_of.items()):
        out.setdefault(holder, []).append(terr)
    return out


def faction_holding(w: World, subject: str) -> "str | None":
    """WHICH FACTION A `hold`'s SUBJECT COHERES UNDER — the faction Proposition id, or `None`.

    ⚠⚠ THIS EXISTS BECAUSE ITEM 16 RE-HOMED EVERY RUNG `hold` FROM A FACTION TO A PERSON AND
    `provinces_of` READ THE SUBJECT DIRECTLY. `holonic §15` makes `hold` a PERSON's edge, and
    `01_BUILD_ORDER` item 16 enforced it -- so the subject stopped being a faction Proposition and
    `provinces_of`'s `t.subject in w.propositions` filter matched nothing. MEASURED: the Query went
    from grouping 16 territories to returning `{}`, silently, and the only thing that caught it was
    a test asserting the OLD shape. The plan that scheduled item 16 did not price this.

    ⚠ **THE RATIFIED SENTENCE IS PRESERVED RATHER THAN AMENDED, AND THAT IS THE WHOLE POINT.**
    `scale_hierarchy_v1.md` §2 (RATIFIED, direct Jordan ruling 2026-07-13) says a province exists
    *"only while its constituent territories share a common FACTION holder."* A person holding land
    is a member of a faction, so "the same faction holds these territories" is still exactly the
    question -- it is now answered through the holder rather than read off the edge. Grouping by
    the PERSON instead would have quietly replaced a ratified rule with a different game (a
    magnate's demesne, not a faction's province) by way of a data change.

    ⚠ MEMBERSHIP HAS ONE OWNER AND THIS DOES NOT MINT A SECOND. §14.2: *"Membership is `commit`"*,
    and `members()` above reads exactly this edge from the other end. A subject that is itself a
    faction Proposition still answers for itself, so a world built the old way reads the same.

    ⚠ NONE AND MANY BOTH RETURN `None`, AND NEITHER IS A DEFAULT. A holder committed to no faction
    holds land that coheres into no province -- which is the same reading `Uncontrolled` already
    gets, and a thing to play for. A holder committed to two is a genuine question this Query does
    not get to answer by picking one: canon states no precedence between a magnate's two
    allegiances, so inventing one here would put a ruling in a Query."""
    if subject in w.propositions and subject in FACTION_BY_PROP:
        return subject
    if subject not in w.persons:
        return None
    facs = {t.object for t in w.persons[subject].tenures
            if t.kind == "commit" and t.live and t.object in FACTION_BY_PROP}
    return next(iter(facs)) if len(facs) == 1 else None


def holder_faction_of(w: World, rung_id: str) -> Optional[str]:
    """M4 (`ED-IN-0279` clause (a)). Which faction holds `rung_id` -- the faction Proposition id,
    or `None` -- read up its own ancestry, since a SETTLEMENT is the object of a `hold` Tenure only
    after a `seize` (v9 IN-13) or a `found` (v9 IN-28); `hold_force` on a seeded one returns `None`:
    every seeded live `hold` targets a `territory` or an `Office`, and the walk takes the nearest held rung either way.
    `nearest_store`'s own walk, applied to holding rather than to a larder: the nearest rung AT OR
    ABOVE `rung_id` that IS held, then `faction_holding` on ITS holder (a person) -- never on
    `rung_id` itself, which `faction_holding` cannot answer
    for at all (`subject not in w.persons` returns `None` immediately; it takes the HOLDER, not
    the held object -- confirmed against the live fixture before this was written, not assumed
    from the name).

    ⚠ `None` FOR "NOBODY HOLDS ANY RUNG UP THIS CHAIN" IS A SHORTFALL, NOT AN ERROR --
    `nearest_store`'s own reading of an empty root. What a `march` targeting an unheld
    (`Uncontrolled`) settlement means is `march`'s own eligibility to decide, not this Query's.

    ⚠ THE WALK IS `ancestry`, NOT A FOURTH HAND-ROLLED COPY (M4 review pass, `/simplify` reuse
    finding). A first writing repeated `ancestry`'s own visited-set-guarded parent walk inline,
    one screen away from `ancestry` itself in this same file -- exactly the duplication that
    function's own docstring exists to end."""
    TRACE.query("holder_faction_of", "resolver")
    t = governing_hold(w, rung_id)
    return faction_holding(w, t.subject) if t is not None else None


def governing_hold(w: World, rung_id: str) -> Optional[Tenure]:
    """The live `hold` that governs `rung_id` -- on the nearest rung AT OR ABOVE it that is held
    (`ancestry`), or `None`. `holder_faction_of`'s walk, its one owner; `endings_reached` reads the
    Tenure itself, for the act that opened it."""
    for cur in ancestry(w, rung_id):
        t = hold_force(w, cur)
        if t is not None:
            return t
    return None


def faction_of(w: World, subject: str) -> Optional[str]:
    """WHICH FACTION `subject` COHERES UNDER, whatever it is -- the faction Proposition id, or `None`.
    The one dispatch over the two owners below it, by `World.class_of` (which tries `Person` BEFORE
    `Rung`: every person also has a `person`-kind rung of the same id, so a man committed to no
    faction must not answer with the faction that holds the ground he stands on):
      * a RUNG that is not a person -- `holder_faction_of`, *who holds this valley*;
      * anything else -- `faction_holding`: a faction's own Proposition answers for itself, a person
        for the one faction he is committed to.
    The dispatch is HERE and not a Rung branch inside `faction_holding`, because `holder_faction_of`
    calls `faction_holding` on a holder and would recurse."""
    if w.class_of(subject) == "Rung":
        return holder_faction_of(w, subject)
    return faction_holding(w, subject)


def uncontrolled(w: World, rung_id: str) -> list[str]:
    """THE REVOLT QUERY (plan position `24h` P5). The territories at or under `rung_id` that no
    faction holds -- GD-3's *Uncontrolled* status, what a revolt leaves behind -- sorted. A read:
    it takes no token, stores nothing, and is recomputed at every call (`AX` T-a).

    ⚠ ITS ORACLE IS CODE, RETIRED AT `29d` AND RECOVERABLE:
    `git show 5c5d8ec6:systems/world/sim/insurgency_pipeline.py`. `check_insurgency_triggers` began
    from every territory with `is_uncontrolled()` (`owner is None`, `engine/autoload/game_state.py`
    at the same ref). This is that line with one season-native stand-in, `holder_faction_of(w, r)
    is None`: the single owner of *which faction holds this rung*, which the march path
    (`loop/sides.py`, `loop/effects_combat.py`) also asks, so the two cannot disagree about who
    holds a place. (`faction_q.resolve(...).holdings` is a second reading with no ancestry walk: a
    two-faction holder's land is in both factions' holdings and uncontrolled here.) Three readings
    come with it, none the oracle's:
      * no live `hold` on the territory or any rung above it -> uncontrolled. `build_realm`'s
        geography value `Uncontrolled` writes no edge; nor does faction land with no authored head,
        and a holder's death closes his `hold` (`remove_person`), so a succession gap reads the same;
      * a holder committed to NO rostered faction, or to MORE THAN ONE -> uncontrolled, because
        `faction_holding` returns `None` for both (read as `provinces_of` reads it; a Proposition
        not on the roster counts as none, `FACTION_BY_PROP`);
      * an unheld territory beneath a faction-held rung -> NOT uncontrolled: `holder_faction_of`
        walks `ancestry`, so the nearest held title governs (the oracle had no cascade).

    ⚠ IT IS SMALLER THAN THE ORACLE ON PURPOSE: contiguity (the oracle grouped by `ADJACENCY`, which
    the season does not carry), the two-season streak (a counter the oracle wrote) and promotion
    (the retired stat vectors) have no season stand-in, and inventing one would put a rule in a
    Query. `rung_id` SCOPES the answer, as `provinces_of` and `density` take theirs; it is not
    contiguity. `H-186` registers what is missing and why.

    ⚠ ITS ONE CALLER IS A REPORT: `harness/populated.py::census` counts it over each realm. That
    meets the letter of r2 `05` §A.1.5 RULED (d), as `establishment_of` below records (*a Query
    with no consumer is a false N-line*), and no more: nothing in the loop or the chooser asks it,
    so the content hash cannot move by it and, under `CLAUDE.md` §0.2, it is a tested read that a
    harness reports. `engine/season/tests/test_revolt_query.py` is its falsifier.
    ⚠ v9 IN-30 TRIED TO GIVE IT A CALLER AND STOPPED: no existing verb takes or governs unheld land
    (`seize` declines it, `march` moves presence only), and the `Rung` stamp reaches only `migrate`
    and `requisition`, which read no holding -- so any caller needs a ruling first (`H-186`)."""
    TRACE.query("uncontrolled", "resolver")
    return sorted(r for r in _subtree(w, rung_id)
                  if r in w.rungs and w.rungs[r].kind == "territory"
                  and holder_faction_of(w, r) is None)


@dataclass(frozen=True)
class EndingReached:
    """One reached ending, as `endings_reached` reports it: the row's id and `victory`, the hold ids its
    condition reads, and its antecedents -- the opening Events' ids and their acts' ids. Sorted tuples."""
    ending: str
    victory: bool
    holds: tuple
    events: tuple
    acts: tuple


def endings_reached(w: World) -> list:
    """v9 IN-27 (H-176, GD-1; #457 D6: *"a Query over holds and seats that the season reports -- never
    an actor"*). The `rosters.yaml: endings` rows the realm has reached, in file order, each an
    `EndingReached`: the hold ids its condition reads, and its ANTECEDENTS -- the logged Events that
    opened the edges the condition stands on, and the acts that caused them. A read: it takes no token,
    stores nothing, emits nothing, and is recomputed at every call (`T-a`).

    A ROW'S CONDITION: every hold its `holds:` selects is live (a `post` selects every Office with that
    post, `hold_force`; a `rung_kind` every rung of that kind UNDER A `realm` RUNG, `governing_hold`),
    and every holder coheres under `under:` (`faction_holding`; `one_faction`: all under the same one).
    Nothing selected is not reached: "every King is a Church man" is vacuously true of a realm with no
    King. ⚠ UNDER A REALM, by `ancestry`, the walk `harness/populated.py::census` sums its
    `uncontrolled_in_realm` over: `build_realm` leaves `terr_T16`, Schoenland's foreign territory, a
    root rung outside the realm on purpose and held by nobody, so a selector over every territory
    would ask a hold no person can ever take and the victory row would be unreachable by construction.

    ⚠ `T-b`: WHAT IS BUILT IS *AN ACT OPENED AT LEAST ONE EDGE THE CONDITION STANDS ON*. The edges the
    condition reads are the selected `hold`s and each person-holder's live `commit` to the faction he
    coheres under, WHEN IT IS HIS SOLE LIVE COMMIT TO IT (`faction_holding` reads that edge, so a king
    who converts reaches the row by his own act; a second commit to a faction he already coheres under
    is an edge the condition does not fail without, so an act minting it changed nothing and is not
    credited -- `_eff_commit` mints a fresh edge every time). Each selected hold is the one live hold on
    its object, so it needs no such rule. An edge's antecedent is the first logged Event naming it whose
    causing act (`causing_act`) is of a verb that opens its kind (`data/verbs.py`'s derived opener
    table) -- so a re-grant or a closure naming the edge is not its opening (a proxy on the causing
    verb; `_opened_by_acts` says why it holds). The realm AS BUILT
    therefore reaches nothing, even where a row's condition already holds at build: a seeded edge has
    no opening Event, and nor does an edge planted by hand. One such act suffices, and THE CROSSING
    ITSELF MAY BE AUTHORLESS: an old `commit` act is credited while a MATTER death (no act) is what
    completes the condition, and no pure read can locate the crossing, because the moment the
    condition was last false is not stored (`T-a`) [ASSUMPTION; medium; Jordan to correct]. It is NOT
    "reached only with a person's act among the crossing's antecedents". Revert: every edge the
    condition reads opened by an act -- under which every seeded territory hold must be re-opened by
    an act and `terr_T15`'s, unheld at build, by a verb that does not exist (`H-186`), so
    `peninsular_sovereignty` becomes unreachable by construction.

    ⚠ NO `TRACE.query` ROW, `ambitions`' reason: `SeasonDriver.season` calls this once per season, the
    probe corpus runs seasons, and a row here moved the committed `runs/TRACE.txt` and `results.json`
    (MEASURED, `test_w15_report_py_reproduces_every_committed_artifact_byte_for_byte`) -- a read-only
    step must move no artifact. It reads through `governing_hold`, not `holder_faction_of`, for the same
    reason."""
    out: list = []
    for name, row in ENDINGS.items():
        edges = _ending_edges(w, row)
        if not edges:
            continue
        opened = _opened_by_acts(w, edges)
        if not opened:
            continue
        out.append(EndingReached(name, row.victory,
                                 tuple(sorted(t.id for t in edges if t.kind == "hold")),
                                 tuple(sorted({e.id for e, _ in opened.values()})),
                                 tuple(sorted({a.id for _, a in opened.values()}))))
    return out


def _ending_edges(w: World, row) -> tuple:
    """The live edges an `endings` row's condition reads, or `()` when it does not hold."""
    sel, val = row.holds
    if sel == "post":
        holds = [hold_force(w, o) for o in sorted(w.offices) if w.offices[o].post == val]
    elif sel == "rung_kind":
        holds = [governing_hold(w, r) for r in sorted(w.rungs) if w.rungs[r].kind == val
                 and any(a in w.rungs and w.rungs[a].kind == "realm" for a in ancestry(w, r))]
    else:       # the loader admits `ENDING_SELECTORS` only; a third must be given a branch here
        raise Forbidden(f"ending selector {sel!r} has no enumerator", "queries/world_q.py::_ending_edges",
                        f"a branch for it, beside `ENDING_SELECTORS`' two")
    if not holds or any(t is None for t in holds):
        return ()
    facs = [faction_holding(w, t.subject) for t in holds]
    want = {facs[0]} if row.under == ENDING_ANY_ONE else {faction_prop_id(row.under)}
    if None in facs or set(facs) != want:
        return ()
    commits = []
    for t, f in zip(holds, facs):
        mine = [c for c in (w.persons[t.subject].tenures if t.subject in w.persons else ())
                if c.kind == "commit" and c.live and c.object == f]
        if len(mine) == 1:                  # the SOLE commit: one the condition fails without
            commits += mine
    return tuple({t.id: t for t in holds + commits}.values())


def _opened_by_acts(w: World, edges: tuple) -> dict:
    """`{edge id: (opening Event, its Act)}` for each edge an act opened (`endings_reached` says how).
    ⚠ A PROXY: an Event "opens" an edge it names when the verb that CAUSED it opens that edge's kind,
    not by anything the Event records, which is true only because `establish`, `release` and `revoke`
    -- which name a hold edge they re-stamp or close -- are not `hold` openers (`loop/effects_governance.py`
    constructs a `Tenure(` only at its three opener sites: `confer`'s hold, `revoke`'s ban, `oblige`)."""
    kind_of = {t.id: t.kind for t in edges}
    out: dict = {}
    for e in w.log:
        for c in e.changes:
            if c.subject not in kind_of or c.subject in out:
                continue
            a = causing_act(w, e)
            if a is not None and a.verb in _OPENERS_FROM_EFFECTS.get(kind_of[c.subject], ()):
                out[c.subject] = (e, a)
    return out


def establishment_of(w: World, office_id: str) -> list[str]:
    """§11 -- *"the named persons the office employs. Finite, contested, durable."* -- AS A QUERY
    OVER LIVE `oblige` TENURES, the persons obliged to this seat, in `w.tenures` order.

    ⚠ REWRITTEN AT PLAN POSITION `17a` (r2 item 9, `03_SEATS_AND_CONTENT.md` §A.9): the body is
    §A.9's own, verbatim, and the name and signature did not move. It read `Office.establishment`,
    a field `[]` on every office in every world (nothing wrote it), and `ARCH §B.7` call 2 deletes
    it: *"`establishment` is a Query over `oblige`, not a field. A set of persons on a seat is two
    homes for one fact. A person joins by `oblige : Person -> Seat` and leaves by `release`."* The
    field is gone; this is the one home. A council is one seat whose members oblige (`AX §E.2.5`).

    ⚠ WITH A CALLER, OR NOT AT ALL (r2 `05` §A.1.5 RULED (d)). It had ZERO callers for as long as
    it read the field, and a Query with no consumer is a false N-line. Its consumer is
    `epistemic._ch_post_remit`, the obligee channel, which asks it rather than re-deriving the set --
    so the witness layer and anything else that asks *who serves this seat* get one answer.

    It is NOT the holder: §22 is explicit that an Office never owns *who holds it* -- that is a
    `hold` Tenure -- so this returns those who serve and `hold_force` returns the seat's occupant.
    `_req_oblige` refuses the holder obliging to his own seat, so the two do not overlap by an act.

    ⚠ `H-34`'s *"establishment size per office kind"* is no longer a number anybody must supply:
    the size is however many have obliged. `ARCH §B.7` call 2 rejected that number by name (*"a
    number nobody can source"*); closed in `hole_register.yaml` at `17a`."""
    TRACE.query("establishment_of", "resolver")
    # v9 IN-40: the walk is `sworn_to`'s (`state/gate.py`, re-exported at the import block), shared with
    # `purview_reaches`' oblige clause, so *who is sworn to this seat* has one answer.
    return [t.subject for t in sworn_to(w, office_id) if t.subject in w.persons]


def upkeep_of(w: World, office_id: str) -> int:
    """`Office.upkeep`'S READER -- plan position `17b`, and the field's first since the ratified `04
    §B.7` `Seat := ( …, upkeep, dates[], exists )` declared it. WHAT THIS SEAT PAYS EACH PERSON
    OBLIGED TO IT, PER TERM: the seat's own declared amount, or the fixture `default_upkeep`
    (`H-158`) when it declares none. The ONE place that fallback is read, so no caller carries a
    number of its own -- `_eff_transfer` asks it to count how many obligees a payment covers.

    `F.18` is the gap it answers: *"upkeep's source -- 'out of the office's stake', and `stake` was
    retired ... no economic pressure on any office. A MATTER payment would be a fourth clock, so the
    repair is a verb."* The verb is the existing `transfer` (the plan's Contradiction-1 box, and the
    retirement plan's G2: *"treasury = `Rung.stores` at the office's own rung; payment = the
    existing `transfer` verb"*), so this Query supplies the amount and nothing moves on its own.

    ⚠ UNITS OF WHATEVER MATTER THE PAYING `transfer` CARRIES -- A LIMIT, STATED. `04 §B.7` names the
    field and no document names its matter kind, so a grain payment and a salt payment count alike
    here. Keying upkeep by kind (`{grain: 2}`) would need a kind nobody has ruled and a second
    schema for one Seat field; the int is the smallest type that makes a payment countable, and
    `H-158`'s row carries the kind question rather than this body deciding it."""
    TRACE.query("upkeep_of", "resolver")
    off = w.offices[office_id]
    if off.upkeep is not None:
        return off.upkeep                 # `Office.__post_init__` already refused a bad declaration
    v = w.fixtures.get("default_upkeep")
    # THE FIXTURE GETS THE SAME REFUSAL THE FIELD DOES, here at its one reader: a sweep arm of `0.5`
    # or `-1` would otherwise count fractional or negative obligees and renew a number nobody set.
    if isinstance(v, bool) or not isinstance(v, int) or v < 0:
        raise Forbidden(
            f"fixture default_upkeep is {v!r}", "ARCH §B.7",
            needs="a whole, non-negative amount per obligee per term (H-158's sweep is 0 / 1 / 3)",
            law="ARCH §B.7 / F.18 -- upkeep counts how many obligees a payment covers; "
                "`Office.__post_init__` refuses the same value on the field")
    return v


# ⚠ `ancestry(w, rung_id)` WAS HERE; IT MOVED DOWN TO `state/containment.py` AT PLAN POSITION `19`,
# body unchanged, beside `home_of` (above), and is re-exported by this module's import block -- the
# write gate's `determination` basis asks the bench's containment test, and `state/` may not import
# `queries/`. `world_q.ancestry is containment.ancestry`; its docstring moved with it.


# ⚠ `conferral_path(w, office_id)` WAS HERE AND IS DELETED (plan position `18a`, r2 item 14). It
# was `ancestry(w, off.rung)` behind a name and a TRACE line, and r2 `05:450-451` names what
# supersedes it: *"superseded by `descendants(w, seat.rung)`, which `03`'s purview rule uses"* --
# `13d-ii`'s purview walk. Its one caller was a TEST, the executed check of Jordan's 2026-09-13
# subordination ruling (*"the duchy is underneath the Crown"*), and that test now asserts through
# `ancestry(w, o.rung)`, the primitive this wrapped, so the check survives the wrapper. No game
# code called it and no committed run artifact traced it.


def ambitions(w: World, p: Person) -> list:
    """WHAT THIS PERSON IS COMMITTED TO AS AN OUGHT: the Proposition ids on `p`'s own LIVE `commit`
    edges whose Proposition (looked up in `w.propositions`) is mood OUGHT, in the order the edges
    were opened, each once. Plan position `17`; `R-06`'s *"a READ over it"*. A belief is a `commit`
    to an OUGHT, not a field (`04` PART D row 44), so this READS the edge and keeps nothing: it is
    computed when asked and never stored.

    ⚠ IT LIVES HERE, NOT IN `person_q`, BECAUSE IT READS A STORE. A `commit` edge's object is only
    an id, and the same edge kind also binds a person to a faction, a treaty and a WAR, so the edge
    cannot say whether it is an ambition; the Proposition's MOOD can, and the Proposition is in
    `w.propositions`. `04` §A.2 admits a `PersonInterior` snapshot only (no store handle) to
    `person_q`, and admits any store, via `World`, to this module; the function was first written
    in `person_q` taking `w.propositions` as a second argument, which no row of that table allows.
    It reads only the keys `p`'s own edges name and never enumerates the store.

    ⚠ FACTION MEMBERSHIP IS NOT A HOLDS THAT THE MOOD FILTERS OUT, FOR SIX OF THE NINE FACTIONS.
    `populated.build_realm` mints each creed as an OUGHT Proposition (Jordan, 2026-09-13, *"Faction
    creed as an ought: sure"*, subject the faction's authored leader) and membership is a `commit`
    to it, so `ambitions` DOES return a member's `fac_*` creed (MEASURED, `build_realm(0)`, Batch C
    close: 35 of 83 persons' `ambitions` include one). Only the three factions with no leader or
    template in canon (`Guilds`, `Schoenland`, `faction x`) keep HOLDS and are filtered by mood -- and `Altonia`
    (v9 IN-36), which has a head and no template, in a `foreign=True` world.

    ⚠ ONE OWNER OF *"a live `commit` to an OUGHT"*. `questions_for`'s Q4 source reads this rather
    than restating it, so the ambition mechanism `R-06` names exists once. A proposition id that is
    not in `w.propositions` is NOT an ambition (absent is the refusal, not a default); an ended edge
    (`until` set) is not one either; two live edges to one Proposition are one ambition. No TRACE
    row is written: `TRACE.query` rows are folded into the committed `runs/TRACE.txt` per call, and
    Q4 calls this once per person per deliberation."""
    out: list = []
    for t in p.tenures:
        if t.kind != "commit" or not t.live or t.object in out:
            continue
        prop = w.propositions.get(t.object)
        if prop is not None and str(prop.mood).upper() == "OUGHT":
            out.append(t.object)
    return out


def goal_referents(w: World, p: Person, prop) -> tuple:
    """WHO OR WHAT AN AMBITION IS ABOUT, read when the question forms (v9 IN-67, A-31 / ED-IN-0293
    (8)) -- THE ONE OWNER Q4 asks instead of `(prop.subject,)`, and `attention_key`'s tier 0 with it,
    so a goal's tier-0 claims are about its referents and never about the id of a seat. `()` forms no
    question (`harness/populated.py`'s rule, *an OUGHT about nobody is not a motive*, now at read).

    The Proposition's id IS the goal's id (`data/goals.py`, the row mints it), so a Proposition no goal
    names -- every creed, tie and want, and every Proposition a goal row does not mint -- reads
    `(prop.subject,)` exactly as before. A goal reads by the kind of its `object:` (`_goal_referents`):

      * `person`, `rung` -> `(prop.subject,)`: seeding (IN-68) minted the Proposition about them;
      * `seat_holders` -> the persons now holding any listed seat (a live `hold`, `w.tenures` order),
        so the referent FOLLOWS A SUCCESSION and a vacant throne names nobody;
      * `deed_doers` -> `person_q.deed_doers` over `p`'s OWN ledger (its three forms; `against: <goal>`
        takes that goal's referents, resolved by this same read);
      * `orientation` -> `()`: a pure condition has no referent, and mints no Proposition.

    ⚠ `seat_holders` IS A WORLD READ WITH NO CLAIM BEHIND IT, `vacancies`' shape: it hands `p` the
    identity of whoever sits on a throne he may never have been told of. THAT PRECEDENT IS ON JORDAN'S
    QUEUE (ED-IN-0292 (2), `needs_jordan`: the `vacancies` stamp against AX-7), and this read follows
    that answer -- if it comes back a claim reaching persons through the channels, `seat_holders`
    becomes a read of the holders `p`'s own ledger names. [ASSUMPTION; medium; Jordan to correct --
    revert: the holders the person's own ledger names, `seats_named`-style, which reads nobody at
    world-gen (H-203).] `deed_doers` is NOT that read: it takes nothing from the world.

    No TRACE row is written (`ambitions`' reason): Q4 calls this once per ambition per person."""
    goal = _goals.goal(prop.id)
    if goal is None:
        return (prop.subject,)
    return _goal_referents(w, p, goal, prop, frozenset())


def _goal_referents(w: World, p: Person, goal, prop, path: frozenset) -> tuple:
    """`goal_referents` for a loaded `goal` whose Proposition is `prop` (None if the world minted none);
    `path` the goal ids on the way down. ⚠ `against:` NAMES ANOTHER GOAL, whose referents are themselves
    computed, and
    the loader does not refuse a cycle among them (A against B, B against A): a goal met twice on the
    path yields `()` -- the looping goal has no referent -- so the read terminates. A target goal with
    no Proposition in the world has no subject: `person`/`rung` read `()` for it, the other kinds need
    none."""
    if goal.id in path:
        return ()
    obj, kind = goal.object, goal.object["kind"]
    subject = prop.subject if prop is not None else None
    if kind in ("person", "rung"):
        return (subject,) if subject is not None else ()
    if kind == "seat_holders":
        # The Office ids seeding recorded (`Proposition.scope`: a loop-built seat is not named by its
        # `offices.yaml` id); a world that minted no scope reads the listed ids as Office ids.
        seats = set(prop.scope) if prop is not None and prop.scope else set(obj["seats"])
        return tuple(dict.fromkeys(t.subject for t in w.tenures
                                   if t.kind == "hold" and t.live and t.object in seats
                                   and t.subject in w.persons))
    if kind != "deed_doers":
        return ()
    against = ()
    if "against" in obj:
        target = _goals.goal(obj["against"])
        if target is not None:
            against = _goal_referents(w, p, target, w.propositions.get(target.id), path | {goal.id})
    return deed_doers(p.ledger, obj, p.id, against)


# A `deed_doers` goal's referents are the doers it acts AGAINST: every authored form names them so --
# "threats" (`against:`), "corruption" (`kinds:`), "heresy" (`engaging:`) -- and the row carries no
# `stance:` of its own. So a goal engaging a pole without a `stance:` takes the opposed side.
# [ASSUMPTION; medium; Jordan to correct -- v9 IN-70; revert: a goal with no `stance:` engages no side,
# and the affiliation term reads 0 for every authored faction.]
_DEED_DOERS_SIDE = -1


def engaged_poles(faction: str) -> tuple:
    """THE AFFILIATION POLES A FACTION'S OWN GOALS ENGAGE, and the side each takes: `((affiliation,
    sign), ...)` in `goals.yaml` order, one pair per goal (v9 IN-70's affiliation term). A goal engages
    a pole when its `object:` is a `deed_doers` naming it (`engaging: <affiliation>`, IN-67's form); its
    side is the goal's `stance:` where authored, else `_DEED_DOERS_SIDE`. `faction` is the faction's
    NAME, as `goals.yaml`'s `org: {faction: ...}` and `data/goals.py::expected` key it; its bodies' and
    seats' goals are theirs, not the faction's (`expected`'s scope). The creed engages no pole: it names
    a leader, not an affiliation [ASSUMPTION; medium; Jordan to correct; revert: the creed's engagement
    (`data/affiliations.py::engagement`) joins the pairs, signed by it; the entry's text names "goals
    or creed"]. Reads the one goals loader; no World."""
    return tuple((g.object["engaging"], g.stance if g.stance is not None else _DEED_DOERS_SIDE)
                 for g in _goals.goals()
                 if (g.org_kind, g.org) == ("faction", faction)
                 and g.object["kind"] == "deed_doers" and "engaging" in g.object)


def opinion_of(w: World, p: Person, faction: str) -> float:
    """v9 IN-70 (RS-23, RS-24; ED-IN-0293 (6)): `p`'s OPINION OF THE FACTION whose Proposition id is
    `faction`, on `[-3, +3]`, computed when asked and stored nowhere (A-29, T-a). The formula and its
    three normalisations are `person_q.opinion`'s (`04` §A.2: the person-side family reads a
    `PersonInterior` only); THIS reads what that family cannot -- the World half -- and hands it down:

      * what the faction expects of its members: `data/goals.py::expected("faction", name)` (IN-69's
        owner: its role template plus its faction goals' pursuits);
      * the poles its goals engage: `engaged_poles`;
      * whom `p` regards on its behalf: its head -- the subject of its creed Proposition, the authored
        leader `harness/populated.py` subjects the creed on, where that is a living person -- then every
        doer `p`'s OWN ledger names (`person_q.deed_doers` over every deed kind: a paired deed's doer
        by the `seen.who` pairing, any other by its subject) who is a live member of it (`members`:
        membership is `commit`, a World read, IN-67's `seat_holders` precedent). `p` himself never.

    `Unspecified` for an id that is no rostered faction's Proposition: a non-faction has no opinion,
    and none is guessed.

    [ASSUMPTION; medium; Jordan to correct; revert: the entry's own wording, a SUM of the three terms'
    inputs rather than the affiliation and regard MEANS: a term then leaves `[-1, +1]` with the number
    of poles or regarded persons] The affiliation and regard terms are MEANS, so each stays on `[-1, +1]`."""
    name = FACTION_BY_PROP.get(faction)
    if name is None:
        raise Unspecified(f"{faction!r} is not a faction's Proposition", "rosters.yaml: factions",
                          needs="a faction Proposition id (`FACTION_BY_PROP`)",
                          law="v9 IN-70 -- an opinion is of a faction")
    inside = set(members(w, faction))
    creed = w.propositions.get(faction)
    head = creed.subject if creed is not None and creed.subject in w.persons else None
    regarded = tuple(x for x in dict.fromkeys(
        ((head,) if head is not None else ())
        + tuple(d for d in deed_doers(p.ledger, {"kinds": DEED_KINDS}, p.id) if d in inside))
        if x != p.id)
    return opinion(p, _goals.expected("faction", name), engaged_poles(name), regarded, w.fixtures)


def opinion_referents(w: World, p: Person, c, memo: Optional[dict] = None) -> tuple:
    """WHOM A DEED DONE TO SOMEONE TURNS `p` TOWARD, read when the question forms (v9 IN-70, RS-23: *"the
    members of the faction whose member killed my lord"*) -- the faction-level referents of the
    question `c` raises. `c` is a claim `p` holds. For an untold `PAIRED_KINDS` deed claim that `p`
    JUDGES -- `person_q.paired_deed_term`, the ONE scorer (IN-58, IN-72): his pursuits lean on its kind
    (the authored `deed:` cells, a death or a wound) and its `seen.who` pairing names one doer, never a
    guess -- whose doer coheres under exactly one faction (`faction_holding`) and of which `p`'s
    `opinion_of` is BELOW INDIFFERENCE (`< 0`, every term's midpoint): the doer, then every other live
    member of that faction, `members` order, `p` himself never. `()` otherwise -- a hidden hand, a deed
    `p` does not judge (a `finding.made`), a doer of no single faction (LIMIT: a DEAD doer is in no
    `members` and so in no faction -- `faction_holding` reads a living person's `commit` edges), a
    faction `p` is indifferent to or favours.

    So ALLEGIANCE decides it, not the deed alone: two witnesses of one killing with the same pursuits
    read different referents when one is the victim's ally (his regard of the killer falls through
    IN-58's `_bond`) or holds the pole the killer's faction hunts (the affiliation term). It ADMITS
    nothing: `questions_for` adds these to a question it already formed from `c` (Q2, through `reach`),
    so a claim `reach` refuses -- a dead victim's death claim, H-209 -- raises no faction either.

    [ASSUMPTION; medium; Jordan to correct; revert: no gate, the referents form whatever the sign] The
    gate is `opinion_of < 0`: a faction `p` is indifferent to or favours is not turned toward.
    [ASSUMPTION; medium; Jordan to correct; revert: only the members `p`'s own ledger names, `opinion_of`'s
    `regarded` set] The referents are every live member of the doer's faction, the RS-23 text
    ("the members of the faction whose member killed my lord"); membership is world truth read by this
    function, not a belief `p` holds (the `seat_holders` precedent, ED-IN-0292 (2)).

    `memo` is the caller's per-`p`, per-call cache: `questions_for` asks this once per claim in `p`'s
    ledger, and the pursuit axes, the `seen.who` index (each O(ledger)), `opinion_of` and `members` (each a
    scan of every Tenure) do not change between claims, so each is computed once per call (axes and index)
    or per faction, and not once per claim."""
    if c.predicate not in PAIRED_KINDS:
        return ()
    if memo is None:
        memo = {}
    if "axes" not in memo:
        memo["axes"] = projected_axes(p, w.fixtures.get("scar_weight_shift"))

    def _seen():                           # built once, and only if some claim's lean asks for it
        if "seen" not in memo:
            memo["seen"] = _seen_index(p.ledger)
        return memo["seen"]
    doer, _term = paired_deed_term(p, memo["axes"], c, _seen)
    if doer is None or doer == p.id:
        return ()
    faction = faction_holding(w, doer)
    if faction is None:
        return ()
    if ("opinion", faction) not in memo:
        memo[("opinion", faction)] = opinion_of(w, p, faction)
    if memo[("opinion", faction)] >= 0:
        return ()
    if ("members", faction) not in memo:
        memo[("members", faction)] = members(w, faction)
    return (doer,) + tuple(m for m in memo[("members", faction)] if m not in (doer, p.id))


def vacancies(w: World, p: Person) -> tuple:
    """THE VACANT SEATS `p` MAY FILL (IN-53, H-207 'VACANCY AS NEED'), sorted by id: every Office
    with no live `hold` -- the test `_req_confer` runs before its `or` disjunct -- for which
    `may_fill` holds through some seat of `p`'s own live `hold`s whose grant carries `confer`
    (`Tenure.granted_acts`, the one owner of the grant's shape). `()` for a person granted no
    `confer`, which is nearly everyone, so the store is read only for a conferrer.

    Resolver-side and read-only: it supplies seat IDS, which `questions_for` adds to the question
    the person answers, as classed referents (D1); whether the conferral then passes is the fold's (`_req_confer`). It asks the
    write gate's own `may_fill`, so it names no seat the gate would refuse to have filled through
    that seat. `confer` is named here because it is the remit act the predicate it mirrors serves.
    ⚠ THAT PROMISE IS THIS FUNCTION'S, NOT THE CLASS'S: the seats a person was told of
    (`seats_named`) ride the same `Office` class and `confer` does not declare `referent_named`, so
    it forms on a told-of seat `may_fill` would refuse (or one he holds) too, and the fold refuses it
    there at the cost of a scene (batch B-I close, C4; H-207). A seat he holds himself is refused as
    a no-op by `_req_confer` (Phase 3 F1: conferring a seat on its own holder)."""
    seats = [t.object for t in p.tenures
             if t.kind == "hold" and t.live and t.object in w.offices and "confer" in t.granted_acts]
    if not seats:
        return ()
    held = {t.object for t in w.tenures if t.kind == "hold" and t.live}
    return tuple(o.id for o in sorted(w.offices.values(), key=lambda o: o.id)
                 if o.id not in held and any(may_fill(w, p.id, s, o) for s in seats))


def seats_named(w: World, p: Person, named: Optional[frozenset] = None) -> tuple:
    """THE SEATS `p` HAS BEEN TOLD OF (IN-10 (a), #453 K-25 / `:524`), sorted by id: the Offices
    among `person_q.ledger_names(p.ledger)` -- a claim about the seat (chiefly the `tenure.opened`
    claim a witness of a conferral holds, `epistemic.claim_subjects`' Tenure expansion) or a held
    document whose `terms` names it. `()` for nearly everyone: before any seat changes hands no
    ledger holds a claim about one (H-203).

    Reads `p`'s OWN LEDGER, never the store's Records (AX-2: a document's content is what the person
    holding it believes); the World is asked only which ids are seats (`w.offices`), the class
    `_stamped` stamps. Resolver-side and read-only, `vacancies`' shape: it supplies seat IDS, which
    `questions_for` adds to the question the person answers as CLASSED referents, and whether an act
    on one passes is the fold's (`_req_oblige`, `_req_confer`). `named` is `ledger_names(p.ledger)`
    when the caller already holds it (`questions_for` asks it once for the three readers)."""
    if named is None:
        named = ledger_names(p.ledger)
    return tuple(sorted(o for o in named if o in w.offices))


def writs_held(w: World, p: Person) -> tuple:
    """THE WRITS `p` HOLDS (v9 IN-09, H-203, DECISION 2026-10-13 [ASSUMPTION; medium; Jordan to
    correct]), sorted by id: the Records on `p`'s own live `hold` edges whose kind a row declaring
    `referent_class: Record` answers (`data/verbs.py::RECORD_REFERENT_KINDS`, `dispensation`). #453
    `:502`: *"the executor holds the writ ... `comply` forms on the held writ"*. ONLY A WRIT THAT
    NAMES HIM: a writ is minted into its maker's hand (the writ-to-addressee mint, IN-10 (c), was
    refused 2026-10-14: the user, ED-IN-0292 (1), *"just say no for now"*), so a holder who is not
    in the writ's addressee list is the issuer or a custodian, not the person the writ orders, and
    is offered nothing. A writ reaches its addressee only by a `give`. `()` for nearly everyone.

    A STANDING OCCASION, `vacancies`' shape: resolver-side and read-only, it supplies Record IDS,
    which `questions_for` adds to the question the person answers as CLASSED referents, and whether
    the act then passes is the fold's (the rows' typed cells: the actor's own ledger holds a claim on
    the writ). It reads `p`'s own edges and the store only for the kinds of the Records they name.
    ⚠ NO 'ALREADY ANSWERED' DECLINE: a holder who complied once is offered the writ again while he
    holds it -- the scene tax IN-10 (a) recorded for a repeated `oblige` (H-203)."""
    def _addressees_of(rec) -> tuple:
        sm = rec.subject_matter
        return tuple(sm.get(RECORD_CONTENT.get("addressee")) or ()) if isinstance(sm, dict) else ()
    return tuple(sorted({t.object for t in p.tenures
                         if t.kind == "hold" and t.live and t.object in w.records
                         and w.records[t.object].kind in RECORD_REFERENT_KINDS
                         and p.id in _addressees_of(w.records[t.object])}))


def places_named(w: World, p: Person, named: Optional[frozenset] = None) -> tuple:
    """THE PLACES `p` HAS BEEN TOLD OF AND COULD SETTLE IN (v9 IN-45 `migrate`, H-168 limit 1,
    [ASSUMPTION; medium; Jordan to correct]), sorted by id: the Rungs among
    `person_q.ledger_names(p.ledger)` -- a claim about the place (a `stores.changed` larder he saw
    drawn, a `rung.founded` hearth, a seat's town a deposit names) or a held document whose
    `terms` names it -- that the §10 ladder will seat him in (`World.contain_ascends`, the one
    owner: never another person's rung) and that he does NOT ALREADY LIVE UNDER (his live `reside`
    edge and every rung above it, `ancestry`). H-168's design order, *"a question whose referent is
    ANOTHER place a person could live in"*: the destination channel `migrate`'s `to` binds, carried
    on the question he answers as `Rung`-classed referents (`_stamped`), so `to` still binds a
    referent and no operand is coined.

    `seats_named`' shape, one class over: reads `p`'s OWN LEDGER and his OWN `reside` edge; the World
    is asked only which ids are rungs (`World.class_of`, the class `_stamped` stamps, so a person's
    own `person`-kind rung, classed `Person`, is never stamped as a place) and what the ladder and
    the containment walk say. ⚠ ROOM IS NOT READ HERE: whether the place has room is the fold's
    (`loop/effects_migration.py::_eff_migrate`'s capacity decline, `verb_table.yaml`'s `migrate`
    note), so a person who wrongly hopes a full hearth has space still tries and is refused. ⚠ WHY
    NOT WHAT HE LIVES UNDER: a settler who already lives under `dest` changes no population and
    settles nowhere new (`_eff_migrate`'s newcomer rule), and his own residence is the refusal H-168
    limit 1 measured. REVERT: exclude the residence alone, and a settler may re-seat himself at the
    town above his hearth. `named` is `ledger_names(p.ledger)` when the caller holds it already.
    The cheap tests run first (class, ladder, his own hearth) and the ancestry walk only for a
    survivor; `ancestry` includes its start, so a hearth is `under` itself."""
    if named is None:
        named = ledger_names(p.ledger)
    cands = [r for r in named if w.class_of(r) == "Rung" and w.contain_ascends(p.id, r)]
    if not cands:
        return ()
    homes = {t.object for t in p.tenures if t.kind == RESIDE_KIND and t.live}
    cands = [r for r in cands if r not in homes]
    if not cands:
        return ()
    under = {r for h in homes for r in ancestry(w, h)}
    return tuple(sorted(r for r in cands if r not in under))


def larders_in_purview(w: World, p: Person, named: Optional[frozenset] = None) -> tuple:
    """THE LARDERS `p`'S SEAT MAY REQUISITION (v9 IN-49 `requisition`, H-163 limit 3, [ASSUMPTION; medium; Jordan
    to correct]), sorted by id: the Rungs among `person_q.ledger_names(p.ledger)` (he has been told of
    the place -- chiefly the deposit a witnessed `stores.changed` leaves) that hold a positive amount
    of the matter a computed requisition carries, at least that amount, and that the purview of some seat of
    his own live `hold`s granting a `Rung` row's remit act reaches (`data/verbs.py::RUNG_REMIT_ACTS`;
    `state/gate.py::purview_reaches`, the one owner `requisition`'s `authority` conjunct asks) WITHOUT BEING
    THAT SEAT'S OWN RUNG: the seat's rung is its treasury, and a requisition of the treasury into itself
    moves nothing (`loop/effects_governance.py::_eff_requisition`, G4's `NoOpReceipt` -> `requisition.refused`).
    MEASURED before that clause (`corpus_run`, seed 0): every computed corpus requisition (4, all NPC-083)
    was its seat's own rung, refused on the `write` clause -- `places_named`' residence rule, one
    effect over (a settler who lives under the place changes nothing there). H-163 limit
    3's design order, #453's *"a question whose referent is a full larder in purview (a positive
    `stores.changed`)"*: the subject `requisition` binds, carried on the question he answers as
    `Rung`-classed referents (`_stamped`), so `subject` still binds a referent and no operand is
    coined.

    `places_named`' shape, one occasion over: `p`'s OWN LEDGER says which places he knows of and his
    OWN `hold` edges which seats he sits in; the World is asked which ids are rungs (`World.class_of`),
    what a rung holds (`Rung.stores`) and whether the seat reaches it. ⚠ THE STORES ARE READ HERE,
    UNLIKE `places_named`' ROOM, and that is `vacancies`' precedent (it asks the write gate's own
    `may_fill`), not an oversight: an empty larder is an occasion for nothing, and a requisition question
    raised over one is the refusal H-163 limit 3 measured (`requisition.refused` on the `stores` conjunct).
    The person still learns nothing he did not hold; a scarcity between this read and the fold (two
    requisitions on one larder) is the fold's (`requisition.refused`, §27.1).
    ⚠ THE AMOUNT AND KIND are the fixtures' (`default_store_kind`, `default_transfer_amount`, H-94 /
    H-121), because that is what `decision/options.py::_derive_operand` carries on a CLASSED ROW
    (`requisition`'s `referent_class: Rung`): a claim the question is about (a stores level, a shortfall)
    does not re-aim it, even when the stamped rung is also the question's plain referent (B-K close,
    COR 4), so the stamp and the act read the same two values. ⚠ PURVIEW IS ASKED LAST, only of a
    named, stocked rung: `purview_reaches` walks `w.tenures` for its oblige clause when the seat's own
    ground does not reach (the gate's walk, not a new one here). `()` for a person granted no such
    act, which is nearly everyone, so nothing else is read for him. REVERT: drop the term in
    `questions_for` (or `requisition`'s `referent_class`, which empties `RUNG_REMIT_ACTS`). `named` is
    `ledger_names(p.ledger)` when the caller holds it already."""
    if not RUNG_REMIT_ACTS:
        return ()
    seats = [w.offices[o] for o in dict.fromkeys(
        t.object for t in p.tenures
        if t.kind == "hold" and t.live and t.object in w.offices
        and any(a in t.granted_acts for a in RUNG_REMIT_ACTS))]
    if not seats:
        return ()
    if named is None:
        named = ledger_names(p.ledger)
    kind, amount = w.fixtures.get("default_store_kind"), w.fixtures.get("default_transfer_amount")
    out = []
    for r in sorted(named):
        if w.class_of(r) != "Rung":
            continue
        held = (w.rungs[r].stores or {}).get(kind, 0)
        if held > 0 and held >= amount and any(r != s.rung and purview_reaches(w, s, r)
                                               for s in seats):
            out.append(r)
    return tuple(out)


def _stamped(q: Question, added: tuple, w: World) -> Question:
    """`q` carrying the ids in `added` as CLASSED referents (IN-53, DECISION 2026-10-13 D1) -- the
    one stamp site. Each id's class is the collection the World holds it in (`World.class_of`:
    `Office` for a seat in `w.offices`, `Record` for a document in `w.records` since IN-09), never a
    literal, and `Question` refuses a class `rosters.yaml: referent_classes` does not declare. The
    plain `referents` are untouched (the class is a partition)."""
    return replace(q, classes=q.classes + tuple((o, w.class_of(o)) for o in added))


_SOURCE_ORDER = {src: i for i, src in enumerate(QUESTION_SOURCES)}


def attention_key(w: World, p: Person, ambs: Optional[list] = None,
                  refs_of: Optional[dict] = None) -> Callable[[Question], tuple]:
    """THE ORDER `p` ANSWERS HIS QUESTIONS IN (v9 IN-57, RS-22: *"sorted by saliency to
    ambition/needs then office/tenure then then convictions"*) -- a sort key over `questions_for`'s
    output, built once per call. Five tiers, the first that holds:

      0. a question, not the `need` question, whose referent is a referent of one of `p`'s own
         ambitions (`ambitions`, the one owner of the live-`commit`-to-an-OUGHT rule;
         `goal_referents`, the one owner of what an ambition is about -- its subject, or v9 IN-67's
         goal referents);
      1. a referent among `p`'s own live-tenure objects or inside a seat's purview (`own_purview`,
         `reach`'s limbs 2 and 4);
      2. a question whose `about` is a deed claim in `p`'s own ledger with nonzero valence under
         `p`'s pursuits, ordered by -|valence|: an unpaired kind by `deed_valence(projected_axes(p,
         scar_weight_shift), c)`; a `PAIRED_KINDS` claim (a death or wound -- `deed_valence` is 0 for
         it, IN-58) by `|lean * bond|` for the doer its `seen.who` pairing names
         (`person_q.paired_deed_term`, the ONE scorer `deeds_judged` sums too; v9 IN-72, RS-23). A
         paired claim whose pairing names no doer (no `seen`, `who` withheld, ambiguous) scores 0 and
         stays in tier 4, so a hidden actor stays hidden [ASSUMPTION; medium; Jordan to correct -- v9
         IN-72; revert: paired claims at tier 4]. LIMIT: a dead victim's `person.died` never reaches the
         question set (`reach` admits a claim by its subject's place, and a dead man has none: H-209), so
         in play this tier scores wound (`body.changed`) and `contest.undecided` claims;
      3. the `need` question -- the standing ambition question, PLAN `W5`'s quiet-season fallback;
      4. the rest -- AND every question whose claim records HIS OWN act (`Claim.doer == p.id`,
         stamped by WITNESS), whatever its referent: the echo of his own deed is not news.

    SALIENCE ORDERS WITHIN TIERS 0 AND 3, DESCENDING, NEVER ACROSS TIERS (v9 IN-69, ED-IN-0293 (10)): the
    key's second slot is `-salience`, the cosine (`data/pursuits.py::pursuit_cosine`, the owner `cast.loyalty`
    calls) of `p`'s `crisis_weights` against what the ambition's organization expects of its members: an
    org goal -> `expected(org) + goal.pursuits`, the faction creed -> `expected(faction)` (`data/goals.py::
    expected`: the role template plus the org's goals' pursuits); `p`'s own want (every other ambition)
    -> `0.0`, indifference. A `need` question takes its own ambition's salience, a tier-0 claim the
    maximum over the ambitions whose `goal_referents` contain its referent. So a member whose pursuits
    point with his faction answers the org goal that fits him best first, and one who points against it
    answers his own want first. Tier 2 keeps -|valence|; tiers 1 and 4 carry 0. Salience is `p`'s own
    state against the stores his edges name (AX-2). An org that expects nothing (no template, no goal)
    reads `0.0`.

    `(order[source], q.id)` -- the key before IN-57 -- stays the final tiebreak, so within a tier
    (and a salience) the old order holds; magnitudes inside tier 1 are not ranked (LIMIT). A source added later
    takes its tier from its referents, so `question_sources`' order is not edited. `ambs` is
    `ambitions(w, p)` where the caller already holds it (`questions_for`); `None` computes it.

    ⚠ READS ONLY THE QUESTION AND `p`'S OWN STATE: his edges, ledger (a held claim's `doer` among it)
    and pursuits, the stores those edges name (a proposition's subject, a seat's rung and its
    descendants) and the scar-shift arm (`Fixtures.scar_weight_shift`, the value `choose` projects
    with). Never the log, never another person, never how important an event is (intent:
    `07_DYNAMICS.md` §7).
    [ASSUMPTION; medium; Jordan to correct -- the five membership tests and the own-act screen.
    The entry's tier 0 put the `need` question first; that arm (measured, `build_realm(0)`, two
    seasons: events 21,735 -> 15,738, `news.told` 14 -> 7; first-season chained told claims 0 at
    every seed 0..39; corpus executed verbs 21 -> 12) starved news, so the standing question ranks
    after the salient claims. Without the own-act screen a person answered the echo of his own act
    on his ambition's subject -- chiefly its refusal (`release.refused`, `migrate.refused`,
    `travel.blocked`) -- and acted on that subject again: 80% of first claim questions were his own
    act's echo (34% before IN-57), and the corpus's R3 propagation fell 46 -> 43 of 46 NPC cases and
    97 -> 91 of 97 ARC cases; the screen restores 46/46 and 97/97. With the screen the corpus
    still shows combat high (felled 82, wounded 116 against base 47/66), through `accept` forming
    with no challenge behind it (HANDOFF_IN's accept residue): the screen did not restore that.
    Revert: the screen off (B), the
    entry's tier 0 literal (`need` in tier 0), or before IN-57 the `(source, id)` key.]"""
    if ambs is None:
        ambs = ambitions(w, p)
    if refs_of is None:
        refs_of = {pid: set(goal_referents(w, p, w.propositions[pid])) - {None} for pid in ambs}
    aims = set().union(*refs_of.values())
    mine = own_purview(w, p)
    held_by_id = {c.id: c for c in p.ledger}

    @functools.cache
    def axis_w() -> dict:
        return projected_axes(p, w.fixtures.get("scar_weight_shift"))

    @functools.cache
    def seen_of() -> tuple:
        return _seen_index(p.ledger)

    @functools.cache
    def salience(pid: str) -> float:
        """How far the ambition `pid` points where `p` does, `[-1, +1]` (v9 IN-69): an org goal against
        `expected(org) + goal.pursuits`, a faction's creed against `expected(faction)`, `p`'s own want
        (any other ambition) `0.0` -- indifference, the cosine's midpoint. `pursuit_cosine_axes` is `None` for an
        organization expecting nothing (no template, no goal) and for a `p` with no pursuits: `0.0`."""
        goal = _goals.goal(pid)
        if goal is not None:
            target = _goals.expected(goal.org_kind, goal.org)
            for name, wt in goal.pursuits.items():
                target[name] = target.get(name, 0.0) + float(wt)
        elif pid in FACTION_BY_PROP:
            target = _goals.expected("faction", FACTION_BY_PROP[pid])
        else:
            return 0.0
        cosine = pursuit_cosine_axes(axis_w(), to_axes(target))
        return 0.0 if cosine is None else cosine

    def key(q: Question) -> tuple:
        tie = (_SOURCE_ORDER[q.source], q.id)
        # Salience orders WITHIN tiers 0 and 3, descending (second slot is ascending); across tiers the
        # first slot decides, so no salience lifts a question over another tier's.
        if q.source == "need":
            return (3, -salience(q.about) if q.about in refs_of else 0.0) + tie
        held = held_by_id.get(q.about)
        if held is not None and held.doer == p.id:
            return (4, 0.0) + tie
        if any(r in aims for r in q.referents):
            return (0, -max(salience(pid) for pid, refs in refs_of.items()
                            if any(r in refs for r in q.referents))) + tie
        if any(r in mine for r in q.referents):
            return (1, 0.0) + tie
        if held is None:
            return (4, 0.0) + tie
        # IN-72: a paired claim (death, wound) scores `|lean · bond|` for the doer its `seen.who`
        # pairing names, `person_q.paired_deed_term` -- the scorer `deeds_judged` sums; unpaired: 0.
        v = deed_valence(axis_w(), held) or paired_deed_term(p, axis_w(), held, seen_of)[1]
        return ((2, -abs(v)) if v else (4, 0.0)) + tie
    return key


def landing_floor(w: World, since: Optional[tuple] = None) -> tuple:
    """THE `(tick, round)` A CLAIM MUST HAVE LANDED AT OR AFTER TO BE NEW: `since` (the person's last
    deliberation, `U2`), else `(w.tick - 1, 0)` -- last season's WITNESS. `questions_for` reads it as
    Q2's boundary and `loop/matter.py::_standing_crossings` as the cut between the past claims and all
    of them (v9 SC-02 `22b` step 23), so the two agree on what *new* means."""
    return since if since is not None else (w.tick - 1, 0)


def standing_crossing_id(w: World, pid: str) -> str:
    """The id of `pid`'s standing crossing at this tick -- one per person per MATTER barrier, minted by
    `loop/matter.py::_standing_crossings` and looked up by `questions_for` through the log's id set."""
    return H(w.world_seed, w.tick, pid, "crossing:standing")


def standing_crossed(w: World, p: Person, since: Optional[tuple] = None) -> Optional[Question]:
    """v9 SC-02 `22b` STEP 23: THE QUESTION A STANDING CROSSING RAISES, ABOUT THE PEOPLE WHOSE CLAIMS MADE IT.

    `p`'s crossing this season (MATTER's record, `standing_crossing_id`), when it is new to him -- it
    precedes round 0, so it is new unless he has deliberated this season (`landing_floor`). Its
    REFERENTS are every person on the `chain` of a told claim among the crossing's causes (the claims
    whose `claim.deposited` it cites), origin first, `p` himself excepted: the people who TOLD, by
    the claim (`Claim.chain`, `T3b`), including an origin who never spoke to `p` -- *"who may have said
    nothing"*. Its `about` is the crossing, which `occasioned_by` returns, so an act formed from it
    cites the crossing. A `claim_landed` question (`11a`'s fold: no third source), as the bench
    question is (`sittings_before`, below). `None` when there is no crossing or no teller.

    ⚠ IT READS AND WRITES NOTHING ELSE: `p`'s own ledger, the log's id set, and the one record."""
    xid = standing_crossing_id(w, p.id)
    if not w.log.has_id(xid) or not landing_floor(w, since) < (w.tick, 0):
        return None
    ev = event_by_id(w, xid)
    causes = set(ev.causes) if ev is not None else set()
    tellers: list = []
    for c in p.ledger:
        if c.chain and w.last_emission_of("claim.deposited", c.id) in causes:
            tellers.extend(t for t in c.chain if t != p.id and t not in tellers)
    return Question(f"q:claim:{xid}", "claim_landed", tuple(tellers), xid) if tellers else None


def questions_for(w: World, p: Person, since: Optional[tuple] = None) -> list[Question]:
    """§F1's `q` producer -- TWO sources, resolver-side, at the DELIBERATE barrier, plus FIVE
    STANDING OCCASIONS stamped onto the first question as classed referents (`_stamped`, below the
    sort): the vacant seats the person may fill (`vacancies`, IN-53), the seats he has been told of
    (`seats_named`, v9 IN-10 (a)), the writs he holds (`writs_held`, v9 IN-09), the places he has
    been told of and could settle in (`places_named`, v9 IN-45 `migrate`) and the larders his seat
    may requisition (`larders_in_purview`, v9 IN-49 `requisition`). They are not
    sources: no id or source changes; a person with one of them and no question gets one `need`
    question carrying them. And, since v9 SC-01's fired-slot step, one `claim_landed` question per
    fired sitting whose docket holds a matter and whose bench he sits on (`sittings_before`; the loop
    after Q4 says why it is no third source). And, since v9 SC-02 `22b` step 23, one `claim_landed`
    question on his own standing crossing this season, about the people who told (`standing_crossed`).

    ⚠ THIS CLOSES `H-04` AND §61's `NoProducer`, which between them blocked every NPC case: with
    no producer for `q`, `assemble(person, question)` was UNSATISFIABLE and DELIBERATE had no
    declared entry point, so `opening_set` had nothing to compute a set FROM. That is why the
    instrument needed an authored `roster` -- `D2`.

    ⚠ FOLDED TO TWO AT POSITION `11a` (r2 `01_ATTENTION_AND_REACH.md` §A.2, `05_LEDGER_AND_BUILD.md`
    §A.4.1 item 2). `date_due` and `band_crossed` MEASURED zero questions in every world the engine
    could build -- Q1's addressing clause was unsatisfiable and Q3 keyed a verb string where an id
    was needed (`H-110`) -- and `04 §B.13` `ID-13` treats a declared source that reaches no code as
    the defect, not as a source worth keeping. Both fold into `claim_landed` rather than vanish: a
    fired date and a band crossing are each already an Event that WITNESS already deposits as a
    claim, so the fold is entirely in what admits that claim as a question, not in what produces
    it. `date_due`'s half needs CALENDAR to emit `date.fired` first (position `11b`, BUILT
    2026-09-29 -- `loop/calendar.py`'s write now carries `emits="date.fired"`) AND needs that
    emission to reach WITNESS, which IN-29 closed: `calendar()` returns its own Events and
    `season()` hands them to `witness()` in round 0 beside MATTER's, so a fired date deposits a
    claim (`test_calendar_a_forced_corpus_date_*` pins `claimed_any`). Whether `claim_landed` then
    admits that claim as a question is not measured here;
    `band_crossed`'s half needs nothing further, because `_crossings` (`loop/matter.py`) already
    emits a witnessable Event whose claim's subject is the site (`epistemic.claim_subjects`'s
    anchor fallback) -- `reach`/`place_of`, below, are what let a claim about a place reach someone
    who was never at that place: a seat's own purview, the ladder above their home.

    Q4 `need` (PLAN `W5`, #353 `:509`, `:605`, `:1297`) survives untouched: a live `commit` to an
    OUGHT Proposition generates a standing question every season, and without it "an NPC with a
    standing ambition and a quiet season forms no candidates at all", which is most of the NPC
    corpus. The order the person answers them in is `attention_key`'s (v9 IN-57); `rosters.yaml`'s
    `question_sources` order is its tiebreak within a tier.

    Resolver-side by construction: it takes a `World`. §F1 says both are "already produced by the
    loop" -- no new step, no new carrier, no clock -- and that is what this reads.

    ⚠ `since` IS `U2`'s ONE ADDITION AND IT GENERALISES Q2 EXACTLY. §F1 Q2 is *a claim LANDING in
    the holder's ledger*, and while a season was ONE PASS "landing" could be read off `when` alone:
    the previous season's WITNESS stamped `when = tick - 1` and DELIBERATE read it at `tick`. Once
    a season is several rounds, a claim can land in round 1 and be new to a person deliberating in
    round 2 of the SAME tick, which `when` cannot express. `since` is the driver-owned
    `(tick, round)` of that person's LAST deliberation, and `Claim.round` is the field that makes
    the pair comparable.
    ⚠ THE DEFAULT REPRODUCES THE OLD READING BIT FOR BIT, WHICH IS WHY THIS IS A GENERALISATION
    AND NOT A CHANGE. `since=None` means `(w.tick - 1, 0)`; every claim carries `when <= tick - 1`
    at DELIBERATE, because WITNESS stamps `when = t` and the tick advances after it -- so
    `(c.when, c.round) >= (tick - 1, 0)` selects exactly the claims `c.when == w.tick - 1` did.
    The one-round arm of `H-124`'s sweep is the executed control for that claim."""
    TRACE.query("questions_for", "resolver")
    out: list[Question] = []

    # Q2 -- a claim landing in p's own ledger, ADMITTED THROUGH `reach` (`01` §A.4-§A.5): the
    # claim's own subject is something REACH covers (today's test, generalised -- `me`/`mine`
    # subsume `c.subject == p.id or c.subject in mine`), OR the claim's subject is AT a place
    # REACH covers. `since_tick` is the season boundary: "landing" is new.
    # ⚠ THE PREVIOUS SEASON'S WITNESS, NOT THIS ONE'S. §F1 Q2 is "a claim LANDING in the
    # holder's ledger AT WITNESS", and WITNESS runs at the END of a season: the deposit is
    # stamped `when = t` and DELIBERATE reads it at `t + 1`. Testing `c.when == w.tick` therefore
    # matched nothing, ever — Q2 was dead for every person in every season, which is half of why
    # nothing propagated. Found by running `headless.py` and reading the ledgers.
    # `U2`: the boundary is *since this person last deliberated*, which is the season boundary
    # when nothing else is supplied. See the docstring for why the two readings coincide at R = 1.
    #
    # ⚠ THE PLACE CLAUSE IS A FILTER, NOT A FAN (`01` §A.4.4, LB-2b): `reach(w, p)` is read-only
    # over `p`'s own tenures and the world's tenure/office/rung stores, `observers_for` is untouched
    # and unaware `reach` exists, and this loop still reads only `p.ledger`. Widening `R` changes
    # which of THIS PERSON'S ALREADY-LANDED claims become a question; it cannot put a claim in a
    # ledger it was never witnessed into. `place_of` may return `None` (a Proposition-subject claim
    # has no place), and `None in R` must be impossible -- the walrus binds it once so the `is not
    # None` guard is written rather than relied on by accident (`01` §A.5.2, `AR-6`).
    #
    # ⚠ CLAUSE 3 (`named(c)`, the id set inside a `content:`-predicate claim) SHIPS HERE, at
    # position `15c` (r2 `01` §A.5.3/§A.5.4, `02` §A.9.1): the deposit rule landed at positions
    # `15`/`16` (`loop/witness.py`'s content deposit), so a `content:<kind>` claim now carries the
    # Record's real `subject_matter` instead of `True` -- the producer §A.5.3 was waiting for.
    # ⚠ NOT A FOURTH SOURCE (§A.5.4). One `Question` shape, one `source` string ("claim_landed",
    # unchanged), one `occasioned_by` route. Clause 3 only ADMITS the claim into `out`; it does not
    # change what the Question is ABOUT: that is `(c.subject,)`, widened only by v9 IN-70's
    # `opinion_referents` (below), when the holder's opinion of the doer's faction is under 0.
    # `requires_operands` is untouched by this clause for exactly that reason.
    R = reach(w, p)
    floor = landing_floor(w, since)
    opinions: dict = {}                    # `opinion_referents`' per-call memo of `opinion_of` by faction
    for c in p.ledger:
        if (c.when, c.round) < floor:
            continue
        if (c.subject in R                                       # clause 1 -- the thing itself
                or ((pl := place_of(w, c.subject)) is not None and pl in R)   # clause 2 -- where it is
                or any(x in R for x in named(c))):                # clause 3 -- whom the CONTENT names
            # v9 IN-70: a paired deed's question also turns `p` toward the doer's faction where his
            # opinion of it is below indifference (`opinion_referents`); the subject stays first, and
            # admission (the three clauses above) is untouched. REVERT: `(c.subject,)` alone.
            extra = tuple(x for x in opinion_referents(w, p, c, opinions) if x != c.subject)
            out.append(Question(f"q:claim:{c.id}", "claim_landed", (c.subject,) + extra, c.id))

    # v9 SC-02 `22b` STEP 23: A STANDING CROSSING IS A QUESTION ABOUT THE PEOPLE WHO TOLD (`standing_crossed`,
    # above). The crossing question read only SITE crossings before (through WITNESS and Q2); this is the
    # person-keyed one, which no witness carries. Still `claim_landed`, no source added: the claims that
    # landed are what crossed. REVERT: drop these two lines; MATTER's record then raises nothing.
    if (sq := standing_crossed(w, p, since)) is not None:
        out.append(sq)

    # Q4 -- `need`. A live `commit` Tenure whose object is an OUGHT Proposition is a STANDING
    # question: it recurs every season until the commitment ends, which is what makes an NPC with
    # an ambition act in a quiet season.
    # `17`: the live-`commit`-to-an-OUGHT rule is `ambitions`' alone (above; R-06's READ), so this
    # asks it rather than restating it; one Question per ambition, in edge order, as before.
    ambs = ambitions(w, p)
    # v9 IN-67: what the ambition is ABOUT is `goal_referents`' (a goal's, else the subject as before);
    # an ambition about nobody forms no question.
    refs_of: dict = {}                     # handed to `attention_key`, which reads the same referents
    for pid in ambs:
        refs = goal_referents(w, p, w.propositions[pid])
        refs_of[pid] = set(refs) - {None}
        if refs:
            out.append(Question(f"q:need:{pid}", "need", refs, pid))

    # v9 SC-01 FIRED-SLOT STEP (H-163 limit 2, #453 pass-1 step 4): A JUDGE IS ASKED ABOUT THE
    # MATTERS BEFORE A SITTING HE SITS ON. One question per fired sitting (`sittings_before`: a docket
    # slot its Date formed holds a matter, he is on the bench at its venue, and he holds the
    # `date.fired` claim), whose REFERENTS ARE THE DOCKETED MATTERS and whose `about` is that claim --
    # so `determine`'s `subject` binds the party by the unchanged referent rule
    # (`decision/options.py::_derive_operand`, which is person-side and World-free and so cannot read
    # a docket itself), and an act formed from it cites the firing (`occasioned_by`'s `claim_landed`
    # route: the deposit's cause is CALENDAR's Event). NOT A THIRD SOURCE: `11a` folded `date_due`
    # into `claim_landed` (`rosters.yaml: question_sources`), and this is that fold's sitting half.
    # STANDING, not "new since he last deliberated": the matter waits on the docket until a
    # determination clears it (`docketed`), as an ambition waits (Q4), so a slot filled after the
    # firing's claim landed is still asked. Several matters ride one question (`H-94`'s single
    # referent widened for this source only; `H-54`'s `first` rule delivers it only when it sorts
    # first, `attention_key` deciding). REVERT: drop this loop -- no question names a docketed
    # matter, and a determination needs a referent coincidence again (H-163 limit 2).
    # THE ID NAMES THE MATTERS: a slot emptied and refilled (even in one RESOLVE) is a new question.
    for did, c, matters in sittings_before(w, p):
        out.append(Question(f"q:sitting:{did}:{'|'.join(matters)}", "claim_landed", matters, c.id))

    # v9 IN-57: the order is `attention_key`'s tiered read of the person's own state; the old
    # `(source, q.id)` key is its final tiebreak (history: hole_register H-54).
    out.sort(key=attention_key(w, p, ambs, refs_of))
    # IN-53 (H-207, DECISION 2026-10-13 D1): A VACANT SEAT THE PERSON MAY FILL IS A STANDING
    # OCCASION, AND IT RIDES ON WHATEVER QUESTION HE ANSWERS. After the sort, so it displaces
    # nothing: `out[0]` -- the question every aggregation rule delivers (`first` returns it; `all`/
    # `one_per_source` keep its id and source) -- carries the vacancies as CLASSED referents
    # (`_stamped`), which only a row declaring that class forms on (`Question.referents_for`, a
    # partition: its plain `referents` are untouched). A person with vacancies and no question gets
    # one `need` question carrying them (the 'no ambition' case). No source added, no id or source
    # changed (`H-54`); with no vacancy the output is byte-identical.
    # IN-10 (a) (H-203, DECISION 2026-10-13 [ASSUMPTION; medium; Jordan to correct]): AND SO DO THE
    # SEATS HE HAS BEEN TOLD OF (`seats_named`: a deposit about the seat, or a held document whose
    # `terms` names it -- #453 K-25), by IN-53 D1's precedent, after his vacancies and never twice.
    # The class is `Office` either way, so every row declaring it (`confer`, `oblige`) forms on both;
    # whether a seat is held is the fold's question, not the referent's.
    # IN-09 (H-203, DECISION 2026-10-13 [ASSUMPTION; medium; Jordan to correct]): AND SO DO THE WRITS
    # HE HOLDS (`writs_held`), after the seats, as `Record` -- only `comply` declares that class, so
    # no other row's formations move. REVERT: drop the term.
    # v9 IN-45 `migrate` (H-168 limit 1, [ASSUMPTION; medium; Jordan to correct]): AND SO DO THE
    # PLACES HE HAS BEEN TOLD OF AND COULD SETTLE IN (`places_named`), as `Rung`. REVERT: drop the term.
    # v9 IN-49 `requisition` (H-163 limit 3, [ASSUMPTION; medium; Jordan to correct]): AND SO DO THE
    # LARDERS HIS SEAT MAY REQUISITION (`larders_in_purview`), last, as `Rung`, never twice. The class is
    # `Rung` either way, so both rows declaring it (`migrate`, `requisition`) form on both: whether a place
    # has room, or a seat reaches it, is then the fold's (`vacancies`/`seats_named`' Office precedent,
    # H-207; H-163 records what the cross-reading costs). No source is added, so no `question_sources`
    # order moves (IN-57: the occasion rides the question he answers). REVERT: drop the term.
    vacant = vacancies(w, p)
    told = ledger_names(p.ledger)
    places = places_named(w, p, told)
    added = (vacant + tuple(o for o in seats_named(w, p, told) if o not in vacant)
             + writs_held(w, p) + places
             + tuple(r for r in larders_in_purview(w, p, told) if r not in places))
    if added:
        head = out[0] if out else Question(f"q:need:{added[0]}", "need", (), added[0])
        out[:1] = [_stamped(head, added, w)]
    return out


def occasioned_by(w: "World", q: Optional["Question"]) -> list:
    """What EVENT occasioned a question — the antecedent an act formed from it must cite.

    ⚠ THIS IS `N3`'s MISSING EDGE, AND `N3` WAS MEASURED, NOT INFERRED: *60 act-Events, 0
    resolving to a question*. An act emitted `causes=[a.id]` and nothing else, so the graph knew
    which act made an Event and never which Event made the act — and `R3` (an act by one person
    caused by an act of another) scored **0 of 30** while `R1`, `R4` and `R5` all passed. The
    chain Reading 07 §4 calls *"the one that is actually the game"* — a claim lands in a ledger,
    raises a question, forms a candidate, becomes an act, emits an Event, is witnessed, deposits
    in SOMEONE ELSE'S ledger — was built end to end except for this one edge.

    **ONE ROUTE, since position `11a` folded `date_due` and `band_crossed` out of
    `question_sources` (`01_ATTENTION_AND_REACH.md` §A.2, `05_LEDGER_AND_BUILD.md` §A.3.1):**

      * `claim_landed` — the deposit Event names the claim in its `changes[]`; its `causes[]`
        name the Event the claim is ABOUT. **The originating Event is returned, not the deposit.**
        The claim IS a belief about that Event — `Claim.predicate` is literally `e.kind` at the
        deposit — so citing the transport instead would put the postman in the arc. The deposit
        stays in the graph on its own `causes[]`; nothing is lost by not naming it twice.
      * `need` — **empty, on purpose.** A standing commitment to an OUGHT is interior; no Event
        caused it this season, and `ID-5`'s polarity says absence maps to the refusal rather than
        to a plausible default. An act taken out of a standing ambition genuinely has no
        antecedent but the actor, and `[ROOT]` is what the design already has for that.

    ⚠ **WHAT THIS DELETES IS A GUARD AND AN UNREACHABLE SEARCH, NOT TWO BRANCHES.** `date_due` and
    `band_crossed` never had a branch of their own here — `05` §A.3.1's correction to an earlier
    draft of this same plan: *"there is no `date_due` branch and no `band_crossed` branch … a
    NEGATIVE membership guard … lets exactly those two fall through to the generic id search …
    which finds nothing."* `date_due` was dead because CALENDAR emitted no Event for a fired Date;
    `band_crossed` was dead because the Question it built carried the crossing's **verb** —
    `"work"` — where an id belongs, so the id search could never match (`H-110`). Deleting the two
    sources deletes the guard's tuple and leaves the id search with no caller, so the search goes
    with it rather than surviving as dead code with nothing left to reach it.

    ⚠ **This count has been wrong twice before landing here**: *"one route per question source"*
    first, then *"two of four"* after a critic found `band_crossed` still nominally rostered. **The
    lesson is in the count, not in the routes: a route's liveness is a property of its PRODUCER,
    and this function cannot see its producers** — which is why, now that both dead sources are
    gone from the roster, there is exactly one route left to get wrong.

    ⚠ **IT RETURNS IDS AND WRITES NOTHING.** Resolver-side, read-only over `w.log`, callable from
    a test without a driver — which is `ID-10`: a check that cannot observe the failure it
    excludes is absent, and this one can be asked directly what it found."""
    if q is None:
        return []
    about = str(getattr(q, "about", "") or "")
    if not about or q.source == "need":
        return []
    if q.source == "claim_landed":
        for e in reversed(w.log):
            if e.kind == "claim.deposited" and any(c.subject == about for c in e.changes):
                return [x for x in (e.causes or []) if x != ROOT]
        # v9 SC-02 `22b` step 23: a standing crossing's question is about the crossing itself, which no
        # deposit names (nobody witnesses it), so the occasion IS that record -- whose own causes are the
        # deposits. Reached only after the deposit search finds nothing, so no earlier route moves.
        if w.log.has_id(about):
            ev = event_by_id(w, about)
            if ev is not None and ev.kind == STANDING_CROSSED:
                return [about]
        return []
    # ⚠ NOT A BARE `else`, AND STILL DEFENCE IN DEPTH RATHER THAN THE FIRST GATE. An undeclared
    # source reaching here would otherwise need a branch nobody wrote, which the polarity `ID-5`
    # refuses: zero evidence maps to the verdict AGAINST the thing measured, never to a quiet
    # default. `Question.__post_init__` already refuses a source outside `question_sources`, so
    # this raise is unreachable from a rostered question and fires only if that constructor is
    # bypassed, or the roster grows a source this function is not taught a route for.
    raise Unspecified(
        f"no occasion route for question source {q.source!r}", "ID-16",
        needs=f"a route here, or one of {sorted(QUESTION_SOURCES)}",
        law="ID-5 -- refuse, don't default. A new question source silently taking a plausible "
            "default would answer wrongly for every question it raised")


# ---------------------------------------------------------------------------
# v9 PC-06 `S-2` / `L-1` (#445 `03` S-2, `01` L-1): ONE PERSON'S PROJECTION -- what a client reads
# for that person, so an interface need not reach into `World` or the driver.
# ---------------------------------------------------------------------------

def _person_or_refuse(w: World, pid: str) -> Person:
    p = w.persons.get(pid)
    if p is None:
        raise Unspecified(f"no person {pid!r} in this world", "S20",
                          needs="the id of a person `w.persons` holds",
                          law="ID-5 -- refuse, don't default: an empty projection for an unknown id "
                              "would read as a person who knows nothing")
    return p


def witnessed(w: World, pid: str) -> list:
    """L-1: THE EVENTS IN `w.log` THIS PERSON WITNESSED, IN LOG ORDER -- `w.log` filtered by witness.

    A witness is a deposit (S28 stage 2: *"DEPOSIT IS PER-PERSON, into that person's OWN ledger and no
    other"*): every claim WITNESS puts in a ledger is written with `emits="claim.deposited"`
    (`loop/witness.py`, six deposit sites). Five write `causes=[e.id]`, the Event the claim is
    about; the sixth, v9 FI-03's found deposit, writes `causes=[e.id, f.id]` -- the finding AND the
    covert trail Event it uncovered. So the Events `pid` witnessed are the causes of the
    `claim.deposited` Events naming a claim `pid` holds, and that set therefore ALSO lists a trail
    Event the person INFERRED from a finding and never saw. ⚠ OBSERVATION, NOT A RULING: whether
    `witnessed` should exclude inferred Events is the PC-06 / S-2 owner's contract question; the code
    below is unchanged by FI-03. The ORIGINATING Event is returned, not the deposit --
    `occasioned_by`'s rule, for its reason (the deposit is the transport). Each once, in the order
    the log holds them.

    ⚠ A FORGOTTEN WITNESSING IS NOT HERE. A claim the `ledger_cap` eviction removed leaves no trace
    on the person: eviction emits nothing (`loop/witness.py`, *"nobody can witness a forgetting"*),
    and a claim id cannot be traced back to its holder. So this is what the person still holds
    evidence of having witnessed, which is the epistemic contract S-2 asks for; it equals every
    deposit made for `pid` only while nothing was evicted from `pid`'s ledger.

    Read-only over `w.log` and `p.ledger`; no TRACE row (`ambitions`' reason: `TRACE.query` rows are
    folded into the committed `runs/TRACE.txt`)."""
    held = {c.id for c in _person_or_refuse(w, pid).ledger}
    if not held:
        return []
    seen: set = set()
    for e in w.log:
        if e.kind == "claim.deposited" and any(c.subject in held for c in e.changes):
            seen.update(x for x in (e.causes or []) if x != ROOT)
    if not seen:
        return []
    return [e for e in w.log if e.id in seen]


@dataclass(frozen=True)
class PersonProjection:
    """S-2: what a client reads for ONE person, and nothing else -- never a `World`.

      * `holder`    -- the person's id;
      * `claims`    -- the person's OWN ledger, in ledger order (S20: a claim lives in its holder's
                       ledger and no other, so no other person's claim can be here);
      * `witnessed` -- `witnessed(w, holder)`, L-1's read, in log order: cumulative over the whole
                       log, every season so far, not this season's alone.

    Both are COPIES. A projection holding the live `Claim`s and `Event`s would hand a client a write
    path around the gate (AX-4: the gate applies every write); a copy is the read-side equivalent of
    `View`'s *"holds IDS, NEVER REFERENCES"* (S18.1) for a reader that has no `World` to resolve ids
    against. Each witnessed Event's copy carries `observed == ()`: an Event's `observed` is what the
    fold READ, and which of those reads a person receives is WITNESS's decision, delivered as that
    person's claims (above) -- the Event's own copy would hand every witness all of them.
    The person's View and candidates are not here: DELIBERATE passes `choose` the person, View,
    Sensation and budget query `(p, v, s, ask_budget)`, and `choose` builds the candidates itself
    (`decision/choose.py`, `opening_set`); S-1's callback receives the same four plus `auto`, the
    delegate chooser (`harness/play_surface.py`)."""
    holder: str
    claims: tuple
    witnessed: tuple


def projection(w: World, pid: str) -> PersonProjection:
    """S-2: `pid`'s own claims and the Events `pid` witnessed, as copies, each Event's `observed`
    emptied (`PersonProjection` says why). Read-only."""
    p = _person_or_refuse(w, pid)
    return PersonProjection(pid, tuple(copy.deepcopy(c) for c in p.ledger),
                            tuple(copy.deepcopy(replace(e, observed=())) for e in witnessed(w, pid)))


# ---------------------------------------------------------------------------
# `WorldReader` -- MOVED HERE FROM `queries/readers.py` AT UNIT L3 (ED-IN-0206), and the move ANSWERS
# a question `queries/__init__.py` had already framed and deferred: *"By source they would split
# `WorldReader` -> `world_q` and `LedgerReader` -> `person_q`; `person_q` does not exist until step 7
# ... whether §A.2's roster then absorbs them is a Layer-1 call for that step, not this one."*
# `person_q` exists now, so this is that call, taken the way that docstring predicted rather than
# left as a FOURTH module in a package `04 §A.2` enumerates with three. `WorldReader` asks THE WORLD
# -- it takes a `World` and reads the actor's own ledger through it -- so it belongs in the
# World-first module; `LedgerReader` takes claims and nothing else, and is in `person_q`.
# ---------------------------------------------------------------------------

class WorldReader:
    """§F.24a's questions asked OF THE WORLD, with every read recorded as an `Observation`.

    ⚠ THE ACTOR'S OWN LEDGER AND NO OTHER, STRUCTURALLY. `04_CODE_ARCHITECTURE.md` §B.2's
    corrected row (`F8`): *"the carve-out is exact and it is not a widening: the fold may ask the
    ACTOR'S OWN ledger ... and no other. A Query taking a ledger and an asker who is not its
    holder still does not exist."* This reader is constructed with ONE actor id, so there is no
    argument by which a caller could name somebody else's claims -- the same move the
    `valoria-critic` agent definition makes against a read-only promise written in a prompt.

    ⚠ THE `if stem ==` CHAIN IS NOT THE ROUTER `G2` FORBIDS. It enumerates the GRAMMAR'S OWN
    predicates -- the strings `Observation` derives from the seven forms -- not verbs, entities or
    outcomes. A predicate it does not know is UNKNOWN, so an unanswerable question refuses."""

    def __init__(self, w, actor: str):
        self._w, self._actor = w, actor

    def _ancestry(self, start: str) -> list:
        return ancestry(self._w, start)

    def read(self, subject, predicate: str):
        w = self._w
        # ⚠ AN UNHASHABLE SUBJECT IS A QUESTION ABOUT NO ONE THING, AND IT REFUSES RATHER THAN CRASHES
        # (plan position `19`). Every stem below looks the subject up in a keyed store, and a LIST
        # raised `TypeError` from inside `_admits`, ending the season where the row's refusal should
        # emit. It is reachable once `issue`'s cell reads `to`: a hand-built writ may name several
        # executors (r2 §A.3 types the addressee as a list), and a cell that asks about ONE id cannot
        # say which. UNKNOWN is the grammar's answer to an operand it cannot read (§42.2's polarity).
        try:
            hash(subject)
        except TypeError:
            return UNKNOWN
        stem, _, arg = str(predicate).partition(":")
        if stem == "exists":
            # An EDGE kind is a `tenure_kinds` member and an OBJECT class is one of `World`'s own
            # collections. Both are DATA -- neither is a list written here.
            if arg in TENURE_KINDS:
                return sum(1 for t in w.tenures
                           if t.kind == arg and t.object == subject and t.live)
            # A RECORD KIND is a `record_kinds` member, and asks for a Record OF THAT KIND -- plan
            # position `15`, where `Petition` stopped being a collection of its own and became a
            # kind of `Record` (`04 §B.5`). `carry`'s cell is the reader. The two vocabularies are
            # disjoint by a load-time refusal (`data/rosters.py`), so this order decides nothing.
            if arg in RECORD_KINDS:
                r = w.records.get(subject)
                return 1 if r is not None and r.kind == arg else 0
            # ⚠ THE `docket` BRANCH (plan position `19`; `21_RECONCILIATION.md` PHASE 2 step 10:
            # *"a `docket` reader branch so `exists:DocketItem` evaluates"*, whose falsifier is *"the
            # cell still returns UNKNOWN"* -- and it did: `DocketItem` is a SEQUENCE of dicts, not
            # one of `_STATE_COLLECTIONS`, so the fallback below read `docketitems` and answered
            # UNKNOWN in every world). It counts the docket items naming `subject` as their matter,
            # through `docketed`, the one owner of that question.
            if arg == DOCKET_KIND:
                return len(docketed(w, subject))
            attr = arg.lower() + "s"
            if attr in World._STATE_COLLECTIONS:
                return 1 if subject in getattr(w, attr) else 0
            return UNKNOWN
        if stem == "stores":
            r = w.rungs.get(subject)
            return UNKNOWN if r is None else (r.stores or {}).get(arg, 0)
        if stem == "condition":
            s = w.sites.get(subject)
            return UNKNOWN if s is None else s.condition
        if stem == "floor":
            s = w.sites.get(subject)
            if s is None:
                return UNKNOWN
            floors = w.fixtures.get("band_floors").get(s.kind)
            if not floors:
                # `_req_work`'s refusal, carried unchanged: `H-08` owns the per-kind floors and
                # §42.2.1 forbids picking a plausible number for a kind nobody registered.
                # `not floors` catches BOTH a missing kind (`None`) and a kind registered with no
                # uses (`{}`, `dwelling`'s control-arm row, `24d-i`) -- `min({}.values())` is a bare
                # `ValueError`, not this typed refusal, and `is None` alone let it through.
                raise Unspecified(
                    f"no band floors for site kind {s.kind!r}", "S12.1",
                    needs="a per-kind floor table -- register row H-08",
                    law="§12.1 gates verbs on `condition` against per-kind FLOORS, and §42.2.1 "
                        "forbids picking a plausible number for a kind nobody registered")
            # ⚠ THE LOOSEST FLOOR, AND AN ADVERSARIAL PASS CALLED THIS AN UNDER-REFUSAL.
            # The objection was exact and is answered rather than dismissed. It said: the prose is
            # `condition >= floor(verb)`, `band_floors`' inner keys are SITE-USE verbs
            # (bulk_shipping, fishing, deep_mining …) which its roster note says are "NOT
            # verb-table rows", so `work` is not among them and `min` silently substitutes the
            # loosest floor for the one the prose names — admitting, on a harbour, every condition
            # in 100..800 where `floor(bulk_shipping)` is 800.
            #
            # WHAT THE OBJECTION GETS RIGHT: this is not `floor(verb)`, and the site-USE is an
            # operand neither the act nor `requires_operands` carries (`H-94`).
            # WHAT IT GETS WRONG, AND WHY `min` STAYS: `work` is the GENERIC labour verb, so the
            # question its precondition asks is *can this site be worked at all* — and a site is
            # workable if it clears the floor of its LEAST demanding use. A seam at condition 100
            # cannot be deep-mined and CAN be surface-gleaned (`surface_gleaning: 50`); a harbour
            # at 150 cannot take bulk shipping and can be fished. So `min` is the READING of
            # `floor(verb)` for a verb that names no use, not a substitute for it.
            #
            # BOTH ALTERNATIVES WERE BUILT AND MEASURED BEFORE SETTLING HERE, which is why this
            # comment is long: `max` refuses a seam at 100 that surface-gleaning supports, and
            # turned `test_w8_...` red for exactly that site; `UNKNOWN` destroys the gate outright
            # — `work`'s precondition could then never return False, so §12.1's condition gate
            # could not observe the failure it exists to exclude (§0.1 point 2), and it turned
            # `test_w3_...` red. `min` is the only one of the three that both refuses an unworkable
            # site and admits a workable one.
            #
            # WHAT REMAINS OPEN AND IS NOT PAPERED OVER: a `work` that MEANS deep-mining is
            # admitted on a seam only surface-gleaning could support, because nothing on the act
            # says which use is intended. That is `H-94`'s operand, and when it exists this line
            # reads `floors[use]` and the reading collapses to the prose.
            return min(floors.values())
        if stem == "contain.path":
            if subject not in w.rungs or arg not in w.rungs:
                return UNKNOWN
            if subject == arg:
                return False           # a node is not a path to itself
            return bool(set(self._ancestry(subject)) & set(self._ancestry(arg)))
        if stem == "held_by":
            return any(t.kind == "hold" and t.subject == arg and t.object == subject and t.live
                       for t in w.tenures)
        if stem == "present_at":
            s = w.sites.get(subject)
            place = s.rung if s is not None else (subject if subject in w.rungs else None)
            return UNKNOWN if place is None else (arg in presence(w, place))
        if stem == "with":
            # Telling workplan `T4`: TWO PERSONS IN ONE PLACE -- `subject` (the cell's `of:`, a
            # telling's hearer) and `arg` (the actor). Through `place_of`, the one owner of where a
            # thing is, whose person-before-rung order is the trap `epistemic._ch_co_located`'s
            # docstring records (a person's same-id `person`-kind Rung answers *nobody is here*). The
            # hearing channel reads the same `place_of`, so a hearer this admits is one WITNESS can
            # reach. UNKNOWN for a side that is no person or has no place: absence refuses, never a
            # guessed place (`ID-5`). The person side never answers this (`WORLD_ONLY_STEMS`).
            if subject not in w.persons or arg not in w.persons:
                return UNKNOWN
            here, there = place_of(w, subject), place_of(w, arg)
            return UNKNOWN if here is None or there is None else here == there
        if stem == "claim.held":
            p = w.persons.get(self._actor)
            return UNKNOWN if p is None else any(c.subject == subject for c in p.ledger)
        if stem == "rank":
            # `21_RECONCILIATION.md` PHASE 2 step 9 / `03_PARAMETERS.md` §C.1 -- THE ORDINAL, NOT
            # A KIND CHECK. `rung_kinds` is an ORDERED roster (`person` first), so a rung's rank
            # is its own kind's position in it -- correct if a sub-settlement tier is ever added,
            # where an enumerated kind list would not be (§C.2's falsifier: change the roster's
            # membership and see what breaks). A Person's own rung carries kind `"person"`
            # (`tiny_world`'s `w.rungs[pid] = Rung(pid, "person")`), so this stem answers for a
            # person address exactly as for any other rung, at rank 0.
            r = w.rungs.get(subject)
            return UNKNOWN if r is None else RUNG_KINDS.index(r.kind)
        # ⚠ PLAN POSITION `19` -- THE FOUR STEMS OF THE REMIT VERBS' CELLS. The first two are
        # `Basis`'s (§F.24a form 7, *"a basis lookup on the exercised seat"*): the argument is THE
        # SEAT (`purview:<via>`), which the form reads off the binding (`Act.via`, structural like
        # the actor), so each answer is a fact about one seat and one subject. Neither is a rule
        # of this reader's: each ASKS the write gate's own predicate, so the precondition refuses
        # exactly what the gate would (`_req_confer`/`may_fill`'s one-owner shape, `CLAUDE.md` §8).
        if stem == "purview":
            # Ruling (4), `04:330`: the seat's purview reaches the place the subject is AT --
            # `place_of`, the one owner of *the rung a thing is at*. A thing with no place (a
            # Proposition) is reached by nothing, which `purview_reaches` answers `False`.
            seat = w.offices.get(arg)
            return UNKNOWN if seat is None else purview_reaches(w, seat, place_of(w, subject))
        if stem == "bench":
            # `may_determine`, the `determination` basis whole: the seat is a judging seat the ACTOR
            # sits in, and its bench's ground holds the subject's home. Actor-relative through
            # `seat_hold`, which is why this reader holds the one actor it was built for.
            return UNKNOWN if arg not in w.offices else may_determine(w, self._actor, arg, subject)
        if stem == "bench.size":
            # `determine`'s quorum, the LEFT side: how many persons sit on the bench for the
            # subject's place -- `judging_set`, the one owner of the bench (`H-32`). Distinct
            # PERSONS, the design's *"members of the bench"*; a seat held twice by one person is not
            # two members. A subject with no place has no bench to count: UNKNOWN, which refuses.
            venue = place_of(w, subject)
            return UNKNOWN if venue is None else len(set(judging_set(w, venue, subject)))
        if stem == "quorum":
            # The RIGHT side, a second read on the same subject as `work`'s `floor` is: the fixture
            # `bench_quorum` (`H-161`), the stand-in for an arrangement's own `quorum:` until a
            # docketed matter maps to its arrangement row. The same for every subject today.
            return w.fixtures.get("bench_quorum")
        if stem in OWN_STATE_STEMS:
            # v9 PC-06 K-3 (`H-85`): `thread_sensitivity` and its gate, through
            # `person_q.OwnStateReader` -- the one answerer, which the person's own formation asks
            # too, so the fold and the person cannot read it apart. ⚠ BUILT ON THIS READER'S OWN
            # ACTOR, NOT ON THE CELL'S SUBJECT (`claim.held`'s precedent, above): the reader's
            # `subject == self._p.id` test then holds at the fold as on the person side, so a cell
            # naming another person (`of: subject`) reads UNKNOWN and refuses -- a person reads
            # nobody else's. An actor that is no person has no sensitivity: UNKNOWN, which refuses.
            p = w.persons.get(self._actor)
            return UNKNOWN if p is None else OwnStateReader(p, w.fixtures).read(subject, predicate)
        return UNKNOWN
