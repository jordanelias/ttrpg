"""`season.loop.effects_information` -- records, propositions, matters: create_record, issue,
covenant, conceal, open_case, carry, determine, argue, petition, survey, forge, give, seize, arrest,
destroy_record, utter, commit.

EXTRACTED from `effects.py` at the per-subsystem split (Phase 4). Holds the document/proposition/
matter cluster: the one mint (`_mint_document`) that `create_record`, `issue`, `petition` and
`open_case` share, plus its own small readers (`_content_of`, `_addressed`, `_seat_rung`) -- all four
stay local, since nothing outside this file's own verbs calls any of them. See `effects_shared.py`
for `effect_for`, `_operand` and the cross-file helper this file's `determine` calls
(`_new_oblige_term`).
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Optional

from ..data.arrangements import ARRANGEMENTS
from ..data.matrix import matrix_row
from ..data.requires import RECORD_SOURCED_OPERANDS, REQUIRES_OPERANDS
from ..data.rosters import COVER_KEY, COVER_KIND, RECORD_CONTENT, RECORD_KIND_KEYS
from ..data.verbs import VERB_TABLE, WARRANT_SOURCED
from ..queries import faction_q
from ..queries.person_q import ABOUT_KEYS, argued_pursuits, consequence_pursuits
from ..queries.world_q import (
    BAN_KIND, DETAIN_KIND, DOCKET_ARRANGEMENT, DOCKET_PETITION, docketed, docketed_under,
    faction_holding, faction_of, hold_force, issuing_seat, place_of, restrained,
    slot_for, works_for, works_target,
)
from ..state.carriers import Proposition, Record, Tenure
from ..state.carriers import DETERMINED_BY
from ..state.gate import (
    DISPOSABLE_KINDS, NO_CHANGE, UNDECLARED_DISPOSAL, Change, Subject, may_determine, may_seize,
    may_warrant,
)
from ..state.ids import H

from .effects_shared import _new_oblige_term, _operand, effect_for, occupying_faction

# v9 SC-02 `22b` step 24: the kind a pursuit write earns, read off its matrix row (`write_matrix.yaml`
# `(Person, pursuits)`, `emits:`), never spelt here; a row emitting other than one kind fails at import.
PURSUIT_MOVED, = matrix_row("Person", "pursuits").emits


@effect_for("create_record")
def _eff_create_record(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """§E3: `create_record` writes `(Record, exists)` and `(Record, stages)`. `H-63` is why the
    VALUES are here and not in the table.

    ⚠ THE STAGES COME FROM THE ACT, NOT FROM A DEFAULT. #353 `:1043` (§54 item 14) makes the
    stage list ACT-DECLARED -- "the act DECLARES the stages and their terms" -- so an act that
    names none creates a record with none, and the instrument does not invent a ladder. That is
    what makes Carin's season the case `PLAN.md` §6.1 chose: a Record with act-declared stages is
    the largest ruled row in the corpus and nothing about it needs a default.

    G4 -- WHAT IT NAMES: THE RECORD, whole -- what it always reported; the maker's `hold` is not
    named (a second receipt on every `record.created` would move every hash that has one). A new
    id always moves (absent -> present). The one no-op is an act naming an id that ALREADY holds
    an identical Record: the Record does not move, the gate refuses, and the `hold` the write
    opened beside it is PUT BACK with the refusal -- so the maker does not end up holding a second
    edge on a record the act did not make. A differing Record on an existing id is still an
    overwrite, as it was; whether a Record id may be re-made at all is not this position's to
    decide (`utter` refuses the same case for a Proposition by immutability, S14).

    ⚠ PLAN POSITION `15`: THE MINT MOVED INTO `_mint_document`, UNCHANGED, SO `issue` AND
    `petition` SHARE IT. What this verb adds is only its own reading of the act: the kind the act
    declares (else `text`), the content the act carries verbatim, and the rung the act names (else
    the actor -- r2 `02` §A.4 records that default as a defect and leaves it to `place_of`'s owner).
    MEASURED, WITH A CONTROL: on the finished position with `petition` withheld from the option set,
    `headless.run(3, 0)` and `populated.run(2, 0)` hash byte-identically to the tree before it -- the
    Record, the `hold` and the `Change` are built exactly as they were, and the one hash move the
    position makes is `petition` entering `resolvable_verbs()`.

    ⚠ PLAN POSITION `24e`: THIS IS THE `works`' PRODUCER, AND IT DECLINES A SECOND LIVE WORKS ON ONE
    TARGET. r2 `04` §A.6.2's moment 1 -- *"DECLARE the works: `create_record` -- exists, RUNS"* -- so
    the kind needed no new verb: an act declaring `kind: works` and `subject_matter: {plan, at}`
    mints one, with the maker's `hold` that makes him its master. The one thing added is r2 §A.6.3's
    *"one works per target"*: `queries/world_q.py::ceiling` cannot say which of two works bounds a
    fabric, so a works whose `(plan, at)` a live works already plans is `NO_CHANGE` -- the refusal
    the fold emits for any declined mint (`act.refused`, this row declaring no kind of its own;
    `F.20b`). r2 put the guard on `found` as a `cardinality` conjunct; see `works_for` for why it
    lives at the producer instead. Every other kind, and a computed act (which carries no payload
    and so always mints `text`), reads exactly as before -- no world built before `24e` holds a
    works, so no hash moves."""
    d = a.payload if isinstance(a.payload, dict) else {}
    kind = d.get("kind") or "text"
    plan, at = works_target(kind, d.get("subject_matter"))      # (None, None) for any other kind
    if works_for(w, at, plan):
        return NO_CHANGE
    return _mint_document(w, a, kind, d.get("subject_matter"), d.get("rung") or a.actor)


def _content_of(a: "Act", kind: str) -> Optional[dict]:
    """WHAT A DOCUMENT OF `kind` SAYS, READ OFF THE ACT THAT MINTS IT -- `None` for a kind with no
    keys (`text`), which is what every Record minted before `record_kinds` already carries.

    ONE RULE FOR EVERY KEY, AND THE RULE IS DATA (`rosters.yaml: record_kinds.content`): a key is
    read from the act's operand of the same name unless `read_from` names another (`terms` is the
    act's `subject` -- what the document is ABOUT). A source that is a `requires_operands` member
    goes through `_operand`, so a missing one is the caller defect it is everywhere else in this
    file; a source that is NOT an operand (`at`, r2 `02` §A.6's place of discharge, which the closed
    vocabulary cannot carry) is read as declared and may be absent. Nothing here names a kind's
    keys: they come from the roster the constructor refuses against, so the two cannot disagree."""
    keys = RECORD_KIND_KEYS[kind]
    if not keys:
        return None
    read_from = RECORD_CONTENT.get("read_from") or {}
    d = a.payload if isinstance(getattr(a, "payload", None), dict) else {}
    out = {}
    for key in keys:
        src = read_from.get(key, key)
        out[key] = _operand(a, src) if src in REQUIRES_OPERANDS else d.get(src)
    return out


def _addressed(content):
    """`content` with its addressee key (`record_kinds.content.addressee`) as an id LIST. The one
    owner of that shape: the mint stores it."""
    addr = RECORD_CONTENT.get("addressee")
    if not isinstance(content, dict) or content.get(addr) is None:
        return content
    v = content[addr]
    return {**content, addr: list(v) if isinstance(v, (list, tuple)) else [v]}


def _makers_hold(w: "World", actor: str, obj: str) -> Tenure:
    """THE MAKER'S `hold`: the edge a maker keeps on what they made (S13 -- possession is a `hold`
    Tenure owned by the holder, never a field on the thing held), opened `since` this tick. The one
    owner of its construction: `_mint_document`'s Record and `_eff_utter`'s Proposition both mint it
    here. The id is `H(seed, tick, actor, f"hold:{obj}")`, unsalted by the act (a maker makes one
    thing per id). ⚠ `"hold"` STAYS A STRING LITERAL IN THIS FILE: `data/verbs.py::OPENERS-DERIVE`
    walks a decorated effect into the same-file helpers it calls and reads the kind off the literal,
    so the seven minters reaching this call -- `create_record`, `issue`, `open_case`, `petition`, `survey`,
    `forge` (through `_mint_document`) and `utter` (through `_eff_utter`) -- remain `hold`'s openers.

    ⚠ NONE OF THE SEVEN DECLARES `Tenure.since` IN ITS `writes:`. The hold opens inside the declared
    `Proposition.exists` / `Record.exists` write, and only the authority check (`refuse_unauthored`)
    sees it. CONVENTION against `04` §C.2/§C.4 and PART D's rows on matrix and step: no scan sees it.
    Declaring it would add a gated write and move the hash, so it is not done."""
    return Tenure(H(w.world_seed, w.tick, actor, f"hold:{obj}"), actor, obj, "hold", since=w.tick)


def _declared_stages(w: "World", a: "Act") -> list:
    """THE STAGES AN ACT WINDS ON A DOCUMENT: the act's declared `stages`, else `H-80`'s default.
    The one owner of that rule -- `_mint_document` winds them on a Record it mints, and `carry` on
    the petition it puts before the room (IN-45). Factored out of `_mint_document` unchanged.

    `H-80`, DECLARED AND SWEPT. The act SHOULD declare these (#353 §13.1) and a computed act cannot:
    §F1's Candidate is `(verb, subject, why)` with no operand channel. Refusing instead would make
    `(Record, stages)` -- a Part D row -- unreachable from any person's decision, so the honest form
    is §G's declare-default-sweep rather than either an invention or a blocker. Each stage is
    `(due_tick, label, the act that wound the clock)`."""
    d = a.payload if isinstance(a.payload, dict) else {}
    stages = list(d.get("stages") or [])
    if not stages:
        n = w.fixtures.get("record_stages_default")
        term = w.fixtures.get("record_stage_term")
        stages = [(w.tick + (i + 1) * term, f"stage{i + 1}", a.id) for i in range(n)]
    return stages


def _docket_item(matter, arrangement, petition, date=None) -> dict:
    """ONE DOCKET ITEM AS AN ACT WRITES IT -- `World.docket`'s shape, the one owner for the two
    acts that put a matter before a room (`open_case` by remit, `carry` by right). `date` is the
    sitting's Date when the matter fills a slot CALENDAR formed (`_eff_open_case`, v9 SC-01
    fired-slot step), else `None`: no sitting was convened for it."""
    return {"date": date, "matter": matter,
            DOCKET_ARRANGEMENT: arrangement, DOCKET_PETITION: petition}


def _mint_document(w: "World", a: "Act", kind: str, content, rung: str,
                   forgery_quality: int = 0) -> Change:
    """THE ONE MINT: a `Record` of `kind` saying `content`, drawn up at `rung`, and the maker's
    `hold` on it -- `create_record`, `issue` and `petition` are three readings of an act onto this
    body, which is r2 `02` §A.6's *one function, three registrations* with the kind supplied by the
    verb that knows it rather than by a table beside the effects (`OPENERS-DERIVE`'s precedent: the
    construction is the single owner of what a verb makes).

    ⚠ THE ADDRESSEE KEY IS STORED AS AN ID LIST, whatever the act carried (`record_kinds.content.
    addressee`, r2 §A.9.1), so a petition to one person and a writ to five executors spell the
    same key one way. The kind's KEY SET is not checked here: `Record.__post_init__` refuses a wrong one
    (⊕L35), before anything is written, and a refusal written twice is two rules.

    `forgery_quality` (v9 SC-02 `22b` step 25, `H-210`): `0` for every document but a forgery, whose
    quality `_eff_forge` passes -- the one writer of `Record.forgery_quality`, so the field is written
    where the Record is made and nowhere else."""
    d = a.payload if isinstance(a.payload, dict) else {}
    rid = d.get("record") or f"rec:{a.id}"
    content = _addressed(content)
    rec = Record(rid, rung, kind, subject_matter=content, stages=_declared_stages(w, a),
                 forgery_quality=forgery_quality)
    held = _makers_hold(w, a.actor, rid)

    def perform() -> None:
        w.records[rid] = rec
        w.add_tenure(held)
    return Change((Subject.entity("records", rid),), perform)


def _seat_rung(w: "World", a: "Act") -> str:
    """WHERE A SEAT-BORNE DOCUMENT IS DRAWN UP: the rung of the seat the act exercises (r2 `03`
    §A.10 -- *a seat-borne act draws on the SEAT's rung, and that is `Act.via`'s job*). `Record.rung`
    is required, so the answer is decided here rather than defaulted: the seat named by `Act.via`.
    A seat with no rung (an office-cluster, `rung? = null`, S6.2) has no place to draw a document up
    in -- and a hand-built act may name no seat at all -- and only then does the mint fall back to
    `create_record`'s own reading of the act, the one existing default rather than a new one.

    ⚠ FACTORED AT PLAN POSITION `19` OUT OF `_eff_issue`, WHERE IT WAS THREE INLINE LINES, BECAUSE
    `_eff_open_case` DRAWS ITS CASE FILE UP THE SAME WAY (§8). For both, the fallback is no longer
    guaranteed unreachable from an ADMITTED act: each row's `purview` conjunct (`data/requires.py::
    Basis`) refuses a rungless seat only by its OWN ground, and since v9 IN-40 a rungless seat passes
    when a sworn holder brings ground (`state/gate.py::purview_reaches`' oblige clause). Such a seat
    reaches the mint with no rung of its own, and the fallback draws the case file up at the act's
    declared `rung` or the actor's id. It also serves the hand-built act that skips the precondition."""
    seat = w.offices.get(a.via) if a.via else None
    d = a.payload if isinstance(a.payload, dict) else {}
    return seat.rung if seat is not None and seat.rung is not None else (d.get("rung") or a.actor)


@effect_for("issue")
def _eff_issue(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """§37.1: a DISPENSATION IS A `Record` OF KIND `dispensation`, minted with the issuer's `hold`
    -- r2 `02` §A.3's schema `{terms, to, at}`: the OUGHT it carries (the act's `subject`), the
    executors it names (`to`), and where it is discharged (`at`, absent unless declared).

    ⚠ REACHABLE SINCE PLAN POSITION `19`, WHICH GAVE `issue` ITS EVALUABLE CELL -- the executor
    exists and is a person, and the issuing seat's purview reaches him (`verb_table.yaml`'s `issue`
    row). Until then this docstring said *"NOTHING REACHES THIS YET"*: the prose `requires:` had no
    predicate, the fold raised before any effect ran, and `resolvable_verbs()` excluded the verb.
    This body is UNCHANGED by `19` but for the rung, factored into `_seat_rung` (`_eff_open_case`
    draws up the same way): the thing `15` built it to mint is what the precondition now admits.

    ⚠ A COMPUTED `issue` WAS ADDRESSED TO WHAT IT IS ABOUT -- `terms` and `to` both bound the
    question's one referent (`H-94`'s single-referent limit), so its `terms` named the executor
    himself. Since plan position IN-10 `to` fans over the persons the issuer knows (the row's
    `terms` conjunct binds `subject`, #453 §10.1), so `terms` is the referent and `to` an executor.
    `petition`'s row keeps the single-referent limit. This body is unchanged by it."""
    return _mint_document(w, a, "dispensation", _content_of(a, "dispensation"), _seat_rung(w, a))


@effect_for("covenant")
def _eff_covenant(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """v9 IN-12 step 7 (#453 §9.2, the `covenant` row; K-54): A COVENANT'S INSTRUMENT IS A `Record` OF
    KIND `dispensation` -- `issue`'s body exactly: `terms` the Proposition the act names (`subject`),
    `to` the counterparty, drawn up at the exercised seat's rung, minted with the maker's `hold`. No
    new kind (K-11): what makes it a covenant rather than a writ is what its `terms` names, and what
    the row asks (a Proposition, a counterparty across purview), not the document.

    THE MINT HOLDS ONLY THE MAKER (`_mint_document`), and this body hands it to nobody: the
    counterparty learns the terms only when he holds the Record (#453 K-54), which is `give`'s. His
    acceptance is his own `commit` to the Proposition, formed from the held dispensation
    (`rosters.yaml: terms_sourced`, `decision/options.py::opening_set`). The instrument is in force
    when both holders are committed -- a reading nothing performs yet: its readers (tribute through
    `_renewals`, allied sides through `mustered`) are deferred (#453 §10.4 step 7)."""
    return _eff_issue(w, a, res)


@effect_for("conceal")
def _eff_conceal(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """v9 IN-12 step 10 (#453 §9.3; K-19): A COVER IS A `Record` OF KIND `cover` WHOSE ONE KEY NAMES THE
    ACTOR -- written HERE, whatever the act's `subject` (a computed act's `subject` is its question's
    referent, which a cover is not about), so `_content_of`'s `read_from` (`terms` <- `subject`) is not
    asked. The Record's own id is the alias. Minted through `_mint_document`, the one mint: the maker's
    `hold` opens with it and the stages it winds are the mint's (`_declared_stages`), which MATTER
    matures. Drawn up where `create_record` draws a document an act names no seat for (the act's
    declared `rung`, else the actor's id); `place_of` reads a held Record at its holder's place either way.

    What the cover DOES is not here: `state/attribution.py::anchor_of` reads it (`live_cover`)."""
    d = a.payload if isinstance(a.payload, dict) else {}
    return _mint_document(w, a, COVER_KIND, {COVER_KEY: a.actor}, d.get("rung") or a.actor)


@effect_for("open_case")
def _eff_open_case(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """PLAN POSITION `19` -- A CASE IS OPENED: the matter goes on the docket, and a case file is
    drawn up at the opening seat's rung. The plan's `19`: *"`open_case` gains `writes:
    DocketItem.matter` and the world reader a `docket` branch: a proceeding with zero authored acts
    needs somebody to have put the matter before the room, and no step did that."* CALENDAR forms
    docket SLOTS (`matter: None`, `loop/calendar.py`) and until v9 SC-01's fired-slot step nothing
    filled one (below); this is the act that puts a matter before a bench, and `determine`'s docket conjunct is the act that needs it.

    WHAT IT WRITES, IN ONE `apply`:
      * THE CASE FILE -- `_mint_document`, the one mint (`create_record`/`issue`/`petition`'s), so
        the row's `Record.exists`/`Record.stages` are written exactly as `create_record` writes them:
        the act's declared stages, else `H-80`'s default (*"its typed cell declares stages, as
        `create_record`'s does"*). Kind `text`, with no content: a `case` kind with its own keys is
        a `record_kinds` member with no reader yet (that roster's own note: a kind lands WITH the
        reader that needs it), and the matter is carried where it is read -- on the docket.
      * THE DOCKET ITEM -- `{"date": ..., "matter": <subject>, DOCKET_ARRANGEMENT: ...,
        DOCKET_PETITION: ...}`, `World.docket`'s own shape. v9 SC-01 FIRED-SLOT STEP (#453 pass-1
        step 4): WHERE A SITTING WHOSE VENUE HOLDS THE MATTER HAS AN EMPTY SLOT (`world_q.slot_for`:
        a Date that fired with a holder -- `_eff_convene` now gives it the convener's seat -- and
        CALENDAR formed `{"date": <id>, "matter": None}` for it), THE NEAREST SUCH SLOT IS FILLED in
        place, keeping its `date`; only where none exists is a dateless item appended, as before.
        [ASSUMPTION; medium; Jordan to correct -- Jordan names another key] THE VENUE IS THE MATCH
        KEY, walked up from the matter's place (`slot_for`'s docstring has the reading and its
        REVERT: append the dateless item always, the pre-step shape, and every slot stays empty).
        The case file is still drawn up at the opening seat's rung; which sitting hears the matter
        is the matter's place, not the opener's.

    G4 -- WHAT IT NAMES: THE CASE FILE, whole, as `create_record` names its Record; it always moves
    (a new id). ⚠ THE DOCKET APPEND IS NOT A NAMED SUBJECT AND CANNOT BE ONE: `Subject`'s three shapes
    are an entity in a `_STATE_COLLECTIONS` member, an edge, and a staged cell, and `docket` is a
    SEQUENCE (`World._STATE_SEQUENCES`), which the gate has no `get()` for. So the append rides on
    the Record's receipt, the way `create_record`'s maker's `hold` does -- and, like that hold, a
    refused write would NOT put it back (the gate restores Tenures only). Two declines therefore come
    FIRST, before anything is built: a matter ALREADY on the docket (`docketed`, the one owner --
    it is before the room already, and a second item would let it be determined twice), and an act
    naming a case-file id that already exists (the only way the mint could be a no-op).

    Where it is drawn up: `_seat_rung`, as `issue`. `via.scope`'s purview reaching the matter is the
    row's precondition (`Basis`, `purview`), asked before this runs.

    ⚠ v9 SC-03a (#453 §10.4 step 2b, K-55): THE ITEM NAMES THE ARRANGEMENT ROW THE MATTER IS HEARD
    UNDER AND THE PETITION IT ROSE FROM, read off the act under the item's own key names
    (`world_q.DOCKET_ARRANGEMENT`/`DOCKET_PETITION`, `TERM_KEY`'s shape: payload keys no typed cell
    binds). Two readers answer `_eff_determine`'s old objection to a key *"nobody else reads"*: the
    determination reads the row's `disposes:`, and `interrogate`/the contested bench will read the
    petition's charge (#453 step 5). A COMPUTED `open_case` carries neither (no operand channel names
    them, `H-80`/§F1) and writes both `None` -- which is why every world where `open_case` executes
    moves its content hash once (the item gained two keys) and no further. TWO MORE DECLINES, before
    anything is built, so a docket never names what does not exist: an arrangement no
    `arrangements.yaml` row carries, and a petition that is not a Record of kind `petition`.
    ⚠ WHICH arrangement a computed case is heard under is NOT DERIVED here -- no source exists
    (`queries/world_q.py::judging_set` records the gap); a hand-built act declares it."""
    matter = _operand(a, "subject")
    d = a.payload if isinstance(a.payload, dict) else {}
    arrangement, petition = d.get(DOCKET_ARRANGEMENT), d.get(DOCKET_PETITION)
    # A NAMED arrangement must be a row id (`str` first: a list or dict payload is unhashable and
    # `in ARRANGEMENTS` would raise) whose `disposes:` is a Tenure kind `determine` can open
    # (`DISPOSABLE_KINDS`) -- else the matter would dock and `determine` decline it forever, and
    # `docketed` would block any second `open_case` (a wedge). `None` -- every computed case -- is
    # the realm's path, unchanged.
    if arrangement is not None and not (
            isinstance(arrangement, str) and arrangement in ARRANGEMENTS
            and ARRANGEMENTS[arrangement]["disposes"] in DISPOSABLE_KINDS):
        return NO_CHANGE
    if petition is not None and not (
            isinstance(petition, str) and getattr(w.records.get(petition), "kind", None) == "petition"):
        return NO_CHANGE
    if docketed(w, matter) or d.get("record") in w.records:
        return NO_CHANGE
    made = _mint_document(w, a, "text", None, _seat_rung(w, a))

    def perform() -> None:
        made.apply()
        slot = slot_for(w, matter)        # read at the write, so two cases never share one slot
        if slot is not None:              # the sitting's slot, filled where it stands (`date` kept)
            slot.update(_docket_item(matter, arrangement, petition, slot.get("date")))
        else:
            w.docket.append(_docket_item(matter, arrangement, petition))
    return Change(made.subjects, perform)


@effect_for("carry")
def _eff_carry(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """v9 IN-45 -- A HELD PETITION IS PUT BEFORE THE ROOM: the one route by which someone without a
    seat dockets a matter (`open_case` dockets by remit). Built on `_eff_open_case`'s body, on the
    gate's EXISTING `entity` shape -- no fourth `Subject` shape, so `state/gate.py` is untouched.

    WHAT IT WRITES, IN ONE `apply`:
      * THE PETITION'S STAGES (`Record.stages`) -- re-wound by THIS act (`_declared_stages`: the
        act's declared stages, else `H-80`'s default from this tick). The petition is its own case
        file: where `open_case` mints a case file and winds its clock, a carried petition already is
        the document, so the carriage winds the clock on it, and MATTER's maturation of those stages
        cites the carriage (`loop/matter.py`'s `prior` is the last Event whose changes name the
        petition, which is this act's). REPLACED, not appended: an appended list could repeat a
        `(due, label)` the filing wound on the same tick. [ASSUMPTION; medium; Jordan to correct;
        revert: append the carriage's stages to the filing's.]
      * THE DOCKET ITEM -- `_docket_item(<terms>, None, <petition>)`: the matter is the petition's
        `terms`, what it is ABOUT (`rosters.yaml: record_kinds.content`: `terms` is the filing act's
        `subject`), and the item names the petition it rose from (v9 SC-03a, K-55). Precedent:
        `open_case` dockets its subject, the party `determine` binds through `docketed`, and an
        accusation petition's `terms` names the accused. No arrangement row: none is derivable for
        a computed case (`queries/world_q.py::judging_set`'s gap, as `open_case`'s).
        [ASSUMPTION; medium; Jordan to correct; revert: the matter is the petition's own id.]

    G4 -- WHAT IT NAMES: THE PETITION, whole (`Subject.entity("records", ...)`, `create_record`'s
    shape). The receipt names the petition id, and the docket item this write appends names that
    same id under `DOCKET_PETITION`, so the receipt names the record the append is keyed by. The
    append itself rides on that receipt, as `open_case`'s rides on its case file -- the docket is a
    SEQUENCE the gate has no `get()` for, and a refused write would NOT put it back (the gate restores
    Tenures only). So every decline comes FIRST, before anything is built: a subject that is not a
    petition `Record`; a petition with no `terms` to docket; a matter ALREADY on the docket
    (`docketed`, the one owner -- `open_case`'s decline); and stages that would read the same after
    as before (the only way the named subject could fail to move).

    ⚠ THE STAGES DECLINE, MEASURED BY ARM (B-K close, COR 2 / LOG 8). At `record_stages_default` >= 1
    it never fires for a computed carry: every wound stage names THIS act's id, so the list differs
    from the filing's; only a declared `stages` equal to the petition's trips it. At
    `record_stages_default` = 0 -- arm 0 of `H-80`'s declared sweep -- filing and carriage both wind
    `[]`, so it REFUSES EVERY CARRY and nothing a petition says reaches the docket. Registered at
    `H-80` and pinned by `test_in45_carry.py`; latent (the shipped arm is 3) and NOT wound to
    `max(n, 1)`. [ASSUMPTION; medium; Jordan to correct.]

    Who may carry: the row's typed cell -- the petition exists, and the ACTOR HOLDS IT (`held_by`,
    `found`'s cell): the petitioner, or whoever `give` handed it to."""
    pid = _operand(a, "subject")
    rec = w.records.get(pid) if isinstance(pid, str) else None
    if rec is None or rec.kind != "petition":
        return NO_CHANGE
    # What the petition is ABOUT, by `person_q.ABOUT_KEYS`' key for its kind (B-K close, ARC 1).
    about = ABOUT_KEYS.get(rec.kind)
    matter = (rec.subject_matter or {}).get(about) if about else None
    if not isinstance(matter, str) or docketed(w, matter):
        return NO_CHANGE
    stages = _declared_stages(w, a)
    if stages == list(rec.stages):
        return NO_CHANGE
    item = _docket_item(matter, None, pid)

    def perform() -> None:
        rec.stages = stages
        w.docket.append(item)
    return Change((Subject.entity("records", pid),), perform)


@effect_for("determine")
def _eff_determine(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """PLAN POSITION `19` -- A DETERMINATION DISPOSES OF A MATTER: it binds the party to the bench,
    and takes the matter off the docket. `21_RECONCILIATION.md:575`, the plan's corrected observable:
    *"a determination opens the disposal Tenure on its subject via the seat"*.

    THE DISPOSAL TENURE, AND WHY IT IS THIS ONE -- each choice named with the reading it rejects:
      * ⚠ v9 SC-03a (#453 §10.4 steps 2b/3, K-55): THE KIND IS THE DOCKETED ARRANGEMENT'S. The docket
        item names the row the matter is heard under (`world_q.docketed_under`, written by
        `open_case`), and the edge opened is the kind that row `disposes:` -- `oblige`, `detain` or
        `ban` -- through ONE LITERAL `Tenure(...)` SITE PER KIND (`_disposal`, below), so the derived
        opener map reads `determine` beside each and C-1's report stays empty. An item naming NO row
        -- every computed case -- disposes `state/gate.py::UNDECLARED_DISPOSAL`, the `oblige` the
        bullet below argues, so every world without a declared arrangement determines as before.
        A row disposing a `Record` or `none` DECLINES: a Record disposal is not on this row's
        `writes:`, and is unbuilt (named, not guessed). So does a docket naming two rows for one
        matter (only a hand-planted docket can), rather than choose between them. The bullet below
        is the `oblige` case's reasoning, unchanged:
      * KIND `oblige`. Five of `arrangements.yaml`'s seven seeded rows dispose a Tenure kind (`oblige`
        for `arbitration`, `detain` and `ban` for the SC-03a rows); the other two dispose a `Record`.
        This bullet is the `oblige` case: C-1 (`21_RECONCILIATION.md:167`,
        RULED A there): *"who owns the Tenure a determiner opens: its SUBJECT ... exactly `confer`,
        which opens a `hold` whose subject is the conferee"*, and its price, stated: *"the subject
        may `release` what the finding opened (T-m) ... a convict can discharge his own penance"* --
        `oblige` is in `release`'s domain, so that price is paid as ruled. The kind is a LITERAL
        here because `data/verbs.py::_derive_openers_from_effects` reads a `Tenure(...)` site's kind
        off its string literal (`_eff_commit`'s docstring records what factoring it cost), and
        that derivation is what `data/arrangements.py::arrangements_without_a_disposal_opener`
        (C-1's load check, REPORTED) reads: `arbitration` leaves that report with this line.
        REJECTED: a `hold` on a seat -- `04 §B.7`'s *"conferral: ... determine by <judging seats>"*,
        a determination FILLING a seat -- because a computed act carries one referent and that
        reading needs two (whom, and which seat): `confer`'s 100% refusal at `★` is that trap.
      * OWNED BY THE SUBJECT, the party the matter names -- C-1's owner, and `_eff_oblige`'s edge
        shape exactly (`subject` a person, `object` a seat).
      * ON THE SEAT EXERCISED (`via`) -- *"via the seat"*: the party is bound to the bench that bound
        him, and so joins its `establishment_of` like any obligee. REJECTED: the seat that opened
        the case -- the docket item does not record it, and adding a key nobody else reads would be
        a field for one reader.
      * (`oblige` only -- `detain` and `ban` open with NO term, `_disposal`'s assumption.) CARRYING
        `_eff_oblige`'s TERM (`oblige_term`, `H-159`), declared by THIS act (T-n: *"the
        opening act declares the terms"*), so a disposal lapses at MATTER like any unpaid service,
        citing the determination that wound it (AX-5). `None` (the control) opens it with none.
      * THE EDGE'S `degree` IS THE BAND THE CONTEST DECIDED (v9 SC-03b, H-162's producer). `determine`
        is a CONTESTED act now (`contests: a proposition`, the `social_contest` provider), so the fold
        arrives here with a `Resolution` whose `degree` is the ladder's reading of the judge's margin
        (`seam/ladder.py::degree_of`), and the disposal is opened WITH it (`Overwhelming`, `Success` or
        `Partial`: the row's keyed `writes:`). At `Failure` the row writes `[]`, the fold never calls this
        body, and nothing opens. ⚠ THE GATE ADMITS A `degree` ON AN EDGE ONLY WHEN THE SAME WRITE OPENS IT
        (`determination` asks `opened` first: authority to bind is not authority to re-grade), which is
        why the degree is set on the edge being OPENED, not written to one already live. `res` is `None`
        only for a hand-built call of this body with no contest, and the edge then carries no degree, as it
        did before SC-03b. `Partial` declares the same three pairs as `Success` (the row's `writes_note`), and
        opens the disposal graded `Partial`.

    AND IT TAKES THE MATTER OFF THE DOCKET: every item naming the party is written back to
    `matter: None` -- the row's `DocketItem.matter` -- so the slot a sitting formed survives and the
    matter leaves it. That is what makes a second determination of one matter in one fold REFUSE
    (the docket conjunct reads 0), §27.1's scarcity on a docket as `requisition`'s is on a larder.

    ONE DECLINE (`NO_CHANGE` -> `determine.refused` on the `write` clause), a NEGATION the grammar
    cannot spell: the party already owes this seat a live `oblige` (one edge per person and seat --
    `_req_oblige` clause 4's rule; a second would list him twice in `establishment_of`) -- since
    SC-03a, a live edge OF THE DISPOSED KIND on this seat (a man already banned by this bench is not
    banned twice), beside the two arrangement declines above. The second
    this body carried -- the party is the actor, a judge binding himself -- was already DEAD: the
    `bench` conjunct's `may_determine` refuses it first (`determine.refused`, flattened at v9 SC-03b), and an act
    naming no subject dies at `party`, so the fold's `counterparty` clause (`loop/resolve.py::
    _admits`, plan position `14`, on this row's `counterparty: subject`) is asked of neither and
    cannot fire for this row.

    G3 -- THE EDGE IS SOMEBODY ELSE'S, AND ITS BASIS IS `determination` (`state/gate.py::
    may_determine`, the EIGHTH): a judging seat the actor sits in, whose bench's ground holds the
    party's home. The row's `bench` conjunct asks that same function first, so the fold refuses (and
    emits) before this runs rather than meeting `NotYours` here. ⚠ The docket write is not a Tenure
    and the gate does not restore it: were the gate ever to refuse this write, the matter would be
    off the docket with no edge opened. The shared predicate is what keeps that unreachable.

    G4 -- WHAT IT NAMES: THE EDGE, which always moves (absent -> present).

    ⚠ v9 SC-02 `22b` STEP 24 -- AND THE DETERMINER'S OWN PURSUITS, BY CONSEQUENCE (`19_PLAN.md` step 24,
    *"Conviction moves by consequence"*; the plan's `convictions` is `(Person, pursuits)` since
    `ED-IN-0261` item 1 -- `Person.conviction`, IN-08's affiliations, is another field). The same write
    moves the ACTOR'S `pursuits` by `person_q.consequence_pursuits` -- each held pursuit by
    `pursuit_shift x DEGREE_STEP[band] x pursuit_lean(determine, e)`: `Overwhelming` twice as far as
    `Success`, `Partial` (the held matter) not at all -- and the band's `writes:` names `Person.pursuits`
    beside the edge. It is the actor's own act at RESOLVE, owner-clean (the writer is the actor), never a
    witness's: WITNESS does not write the field. The pursuit subject earns `pursuit.moved` (the matrix
    row's kind) and the edge the band's own kind BY NAME, so a judge whose pursuits do not move (none
    held, none leaning, or `pursuit_shift` 0, the control) publishes exactly what he did before -- the
    edge earning `None` would earn the band's whole `emits:`, `pursuit.moved` included, a move that did
    not happen (found by this step's control test). ⚠ NOT AT `Failure`, WHERE THE PLAN MOVES HIM
    AGAINST HIS AXIS (`H-221`): the row writes `[]` there and the fold never calls this body; making it
    write would give a failed hearing's Event a change, so WITNESS's empty-changes rule (`epistemic.
    claim_subjects`) would land its claim on the JUDGE instead of the party (`deed:matter.undetermined`'s
    cell reads the party), the scar would run on an act that did nothing, and a judge who holds no leaning
    pursuit would turn `matter.undetermined` into `determine.refused` (`NoOpReceipt`). Named, not built."""
    party, seat = _operand(a, "subject"), a.via
    rows = docketed_under(w, party)
    if seat is None or len(rows) > 1:
        return NO_CHANGE
    row = next(iter(rows), None)
    if row is not None and row not in ARRANGEMENTS:
        return NO_CHANGE                  # a hand-planted item naming no row `open_case` admits
    kind = ARRANGEMENTS[row]["disposes"] if row is not None else UNDECLARED_DISPOSAL
    if any(t.kind == kind and t.subject == party and t.object == seat and t.live
           for t in w.tenures):
        return NO_CHANGE
    nt = _disposal(w, a, party, seat, kind, res.degree if res is not None else None)
    if nt is None:
        return NO_CHANGE
    items = docketed(w, party)
    judge = w.persons.get(a.actor)
    moved = None
    subjects = (Subject.edge(nt),)        # a hand-built call with no contest: the edge, as before
    if res is not None:
        if judge is not None:
            moved = consequence_pursuits(judge, a.verb, res.degree, w.fixtures.get("pursuit_shift"))
        # THE EDGE EARNS THE BAND'S OWN KIND BY NAME, ALWAYS: an edge earning `None` earns every kind
        # the band declares (`loop/resolve.py`), and `pursuit.moved` is declared on the moving bands
        # -- so a judge whose pursuits did not move (the `0` control arm, measured) would publish a
        # move that did not happen. The pursuit subject alone earns `pursuit.moved`.
        band_kind, = (k for k in VERB_TABLE[a.verb].emits_at(res.degree) if k != PURSUIT_MOVED)
        subjects = (Subject.edge(nt, earns=band_kind),)
        if moved is not None:
            subjects += (Subject.entity("persons", a.actor, earns=PURSUIT_MOVED,
                                        fields=("pursuits",)),)

    def perform() -> None:
        w.add_tenure(nt)
        for item in items:
            item["matter"] = None
        if moved is not None:
            judge.pursuits = moved
    return Change(subjects, perform)


@effect_for("argue")
def _eff_argue(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """v9 IN-12 step 9 (#453 §9.4; K-21) -- A WON ARGUMENT MOVES THE HEARER'S `Person.pursuits`.

    The row is contested (`contests: a proposition`, the social contest module's roll), so this body runs
    only on a band whose `writes:` names `Person.pursuits` (`Overwhelming`, `Success`); `Partial` and
    `Failure` write `[]` and the fold never calls it there. The hearer is the row's counterparty (`to`);
    his held pursuits move toward the ARGUER's own by `queries/person_q.py::argued_pursuits` -- the
    ARGUMENT half of the row's *'moved by argument and consequence'*, `determine`'s consequence write one
    verb over, and like it the write is the actor's act at RESOLVE, never a witness's.

    G4 -- WHAT IT NAMES: THE HEARER, read as his `pursuits` alone; it earns every kind the band declares
    (`argument.won`, `pursuit.moved`), because the only change the band makes IS the moved pursuit. A won
    argument that moves nothing (the hearer already where the arguer stands, no pursuit held, or
    `pursuit_shift` 0, the control) is `NO_CHANGE` -> `argument.refused` at its write (F9): a success
    Event over an unmoved mind would be a deed that did not happen.

    DECLINES: no resolution (a hand-built call with no contest), no hearer, no arguer, or nothing moves."""
    hearer, arguer = w.persons.get(_operand(a, "to")), w.persons.get(a.actor)
    if res is None or hearer is None or arguer is None:
        return NO_CHANGE
    moved = argued_pursuits(hearer, arguer, res.degree, w.fixtures.get("pursuit_shift"))
    if moved is None:
        return NO_CHANGE

    def perform() -> None:
        hearer.pursuits = moved
    return Change((Subject.entity("persons", hearer.id, fields=("pursuits",)),), perform)


def _disposal(w: "World", a: "Act", party: str, seat: str, kind: str,
              degree: Optional[str] = None) -> Optional[Tenure]:
    """THE DISPOSAL EDGE OF `kind`, owned by `party` on `seat` -- one LITERAL `Tenure(...)` per
    disposable kind, because `data/verbs.py::_derive_openers_from_effects` reads an opener's kind off
    the literal (and walks this same-file helper as if inlined). `None` for any other kind -- a
    `Record` or `none` disposal, or a Tenure kind a future row names with no site here -- so the
    effect declines rather than open an edge the row did not ask for.

    `oblige` carries `_eff_oblige`'s declared term (`H-159`), exactly as before SC-03a, and its id is
    byte-identical to the pre-SC-03a one (`oblige:<seat>:<act>`). `detain` and `ban` carry NO term
    [ASSUMPTION; medium; SC-03a; revert: pass `term=_new_oblige_term(w, a)` to both]: #453 §8.1
    writes both as lasting *"until pardon"* / *"until released"*, `oblige_term` is the length of a
    SERVICE (`H-159`), not of a sentence, and a restraint lapsing at MATTER would make the bench's
    custody a timer nobody declared; the arrangement's `term_required` key has no reader yet.
    `degree` is the band the contest decided (`_eff_determine`), `None` for a hand-built call."""
    tid = H(w.world_seed, w.tick, party, f"{kind}:{seat}:{a.id}")
    if kind == UNDECLARED_DISPOSAL:
        # `payload={"determined_by": a.id}` marks the edge as IMPOSED, not sworn: `state/gate.py::
        # purview_reaches`' oblige clause reads an OATH and skips an edge carrying this key (a sentence
        # must not hand the bench the convict's own seat ground). `establishment_of` still lists him.
        return Tenure(tid, party, seat, "oblige", since=w.tick, term=_new_oblige_term(w, a),
                      payload={DETERMINED_BY: a.id}, degree=degree)
    if kind == DETAIN_KIND:
        return Tenure(tid, party, seat, "detain", since=w.tick, degree=degree)
    if kind == BAN_KIND:
        return Tenure(tid, party, seat, "ban", since=w.tick, degree=degree)
    return None


@effect_for("petition")
def _eff_petition(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """§36.1 / #353 §26.3: A PETITION IS A `Record` OF KIND `petition`, minted with the
    petitioner's `hold` -- `{terms, to, from}`: what it is about (the act's `subject`), the person
    it is addressed to (`to`), and the place it rises from (`from`). Drawn up where it rises from,
    so `Record.rung` is a place and not the petitioner's id (the defect r2 `02` §A.4 measured on
    every `create_record`).

    ⚠ TWO-SIDED (`ED-IN-0210` ruling 2 -- *withdraw (petitioner) or deny (receiver)*): the row's
    typed cell makes both sides EXIST, `opening_set` never forms a Candidate addressed to its own
    petitioner (the row's `counterparty:`), and the FOLD refuses the same case for a HAND-BUILT act
    (`loop/resolve.py::_admits`'s counterparty clause, plan position `14`) before this body runs.
    This body carried that decline itself until `14` moved it into the fold, where every row naming
    a second party shares it. ⚠ WHAT THIS DOES NOT BUILD: the two closers. Ruling 2's
    WITHDRAW and DENY both close `(Record, exists)`, whose one closer is `destroy_record` -- which
    declines on both its eligibility alternatives today (`H-75`; plan position `14` built its
    formable shape and HELD it on measurement, the row's `formation_decline_note`), and which the receiver
    can only reach once `give` (position `16`) puts the petition in his hand. The fold makes both
    sides NAMEABLE on the document; neither side can yet end it."""
    return _mint_document(w, a, "petition", _content_of(a, "petition"), _operand(a, "from"))


@effect_for("survey")
def _eff_survey(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """PLAN POSITION `20-iii` -- THE INFORMATION CLUSTER (narrative #14 §F; `D1-a` of
    `proposals/2026-09-27-mc-v18-retirement-plan/PROPOSAL.md`: *"A Record whose `subject_matter` is a
    frozen `faction_q.resolve(...)` snapshot, commissioned by an act, read free by holders, forgeable
    and destructible"*). A SURVEY IS COMMISSIONED: a `Record` of kind `faction_q.SHEET_KIND` whose
    content is `faction_q.resolve`'s five-field view of one faction, RESOLVED AT THE MOMENT OF WRITING,
    minted through `_mint_document` -- the one mint -- with the surveyor's `hold`. Proposal 14
    (`proposals/2026-09-12-emergent-narrative-primitives-v2/01_THE_TEN.md`): *"a faction sheet is
    those Queries, resolved at the moment of writing and frozen into a `Record`"*; and the attack it
    survived, which is why an act is spent here and nowhere else: *"The cost belongs to COMMISSIONING
    ... Free to read, costly to obtain, stale by construction."*

    WHICH FACTION -- `world_q.faction_of(w, subject)` (through `_resolved_sheet`), THE ONE DISPATCH OVER
    THE OWNERS OF *which faction does this cohere under*. `faction_holding` answers for a faction's own
    Proposition (itself, if the roster carries it) and for a person (the one faction he is committed
    to; `None` for none or for two, where canon states no precedence). So the literal reading --
    survey the Crown -- and the reachable one -- survey the faction of the man you were asked about --
    are ONE read, and no referent-to-faction rule is written here. ⚠ AND A RUNG, SINCE v9 IN-12
    (`survey` + Rung, H-169 limit 6): *who holds this valley* is `world_q.holder_faction_of`, the
    owner the march path and `uncontrolled` already ask, so a survey of a place reads the faction that holds it as `loop/sides.py` reads its defender
    (`_resolved_sheet` dispatches on `World.class_of`). The sheet is the same five-field view, so the
    sheet consumer (`rosters.yaml: record_sourced_operands.faction_sheet`) reads it unchanged.
    REJECTED, each with its reason:
      * THE SUBJECT IS THE FACTION AND NOTHING ELSE (`commit`'s cell, `existence` of `subject`, kind
        `Proposition`). No computed act's referent is ever a Proposition -- `questions_for`'s clause
        1 admits a claim only if its subject is in the asker's `reach`, and `place_of` of a
        Proposition is `None` (BO-9/BO-10's gap; `commit` MEASURED refused 33 of 33 in one realm
        season, `python -m engine.season.harness.aperture`) -- so a survey would be formed on every
        referent and refused on every one: a fourth instance of `H-156`'s scene tax, and a
        mechanism that runs in no shipped world.
      * (`20-iii`'s, LIFTED at v9 IN-12) `holder_faction_of` FOR A RUNG as *a second derivation
        the position does not name*: the plan named it at IN-12, and it is a call to the owner, not a
        derivation written here.
      * `create_record` DECLARING `kind: faction_sheet` (`works`' route at `24e`). Three reasons,
        any one sufficient. (a) A sheet's content is RESOLVED, and `create_record` stores what the
        act carries VERBATIM (r2 `02` §A.4, *verbatim or not at all*): a sheet whose maker supplies
        its content is a forgery by construction, and teaching `create_record` to resolve for one
        kind is a kind-keyed branch changing what a generic verb means. (b) A COMPUTED
        `create_record` carries nothing -- the row is untyped, so `operands_for` returns `{}` -- and
        could never say WHICH faction; it mints `text`, as it does 46 times a realm season. (c)
        `issue`'s and `petition`'s precedent: one mint, the kind supplied by the verb that knows it
        (r2 `02` §A.6's *one function, several registrations*).

    WHAT IT WRITES -- `asdict(faction_q.resolve(...))`: a fresh mapping of fresh lists, so nothing
    done to the world afterwards reaches the document (and `loop/witness.py::content_value` freezes it
    again, as tuples, for a holder's ledger). The keys are `Faction`'s fields, which `faction_q.py`
    checks against `rosters.yaml: record_kinds` at import. No date is written into it: the
    document-side date proposal 14 asks for (*"dated"*) has no key -- `at` is a PLACE in every kind
    that has it -- and is `H-169`'s; a holder's belief carries its own `when`.
    WHERE IT IS DRAWN UP -- where the surveyor stands, `world_q.place_of(actor)`, the one owner of
    *the rung a thing is at* (`give`'s reading of the same person). ⚠ NOT `create_record`'s default,
    the actor's own id, which r2 `02` §A.4 records as a defect; that default is kept only for an actor
    standing nowhere, where there is no rung to name.

    DECLINES (`NO_CHANGE` -> `survey.refused`, the `write` clause): the subject coheres under no single
    faction -- a person committed to none or to two, a rung nobody up its chain holds (or whose holder
    coheres under none), a site, an office, a document, an unrostered Proposition. The cell has already
    asked that the surveyor has heard of the subject (`own_ledger`).

    ⚠ WHAT THIS DOES NOT BUILD, each registered (`H-169`): proposal 14.1's bound -- *what the sheet
    can contain is bounded by who you have* (the seats you have filled) -- so every survey is
    complete and exact, and anyone may commission one; `destroy_record` declines for every actor
    (`H-75`), so no act burns one. (A false sheet is `_eff_forge`'s, below, since v9 IN-45.)

    G3 -- THE `hold` IS THE SURVEYOR'S OWN, `T-m`, exactly `create_record`'s. G4 -- WHAT IT NAMES: THE
    RECORD, whole, earning `faction.surveyed`; a new id always moves (absent -> present)."""
    return _mint_sheet(w, a)


def _mint_sheet(w: "World", a: "Act", forged: bool = False) -> Change:
    """THE BODY `survey` AND `forge` SHARE: the resolved sheet (`NO_CHANGE` where the subject coheres
    under no faction), with one key falsified and `default_forgery_quality` written if `forged` (v9
    SC-02 `22b` step 25; a survey's sheet carries `0`), minted through `_mint_document` where the
    maker stands. `"hold"` still opens inside `_mint_document`, so the opener derivation reaches it."""
    sheet = _resolved_sheet(w, a)
    if sheet is None:
        return NO_CHANGE
    if forged:
        sheet[_FORGED_SHEET_KEY] = a.actor
    quality = w.fixtures.get("default_forgery_quality") if forged else 0
    return _mint_document(w, a, faction_q.SHEET_KIND, sheet, place_of(w, a.actor) or a.actor,
                          forgery_quality=quality)


def _resolved_sheet(w: "World", a: "Act") -> Optional[dict]:
    """WHAT A SHEET ON THE ACT'S `subject` SAYS TODAY -- `faction_q.resolve`'s view of the one faction
    the subject coheres under, as a fresh mapping (`asdict`), or `None` when it coheres under none.
    `survey` mints it as it is; `forge` mints it with one key false. Factored at v9 IN-45 so the two
    verbs read WHICH faction one way (`_eff_survey`'s docstring).

    WHICH FACTION: `world_q.faction_of`, the one dispatch by the subject's class (`World.class_of`):
      * a RUNG -- `holder_faction_of`, *who holds this valley*: the faction of the holder of the
        nearest held rung at or above it (`ancestry`), `None` where nobody up the chain holds or the
        holder coheres under no single faction. v9 IN-12 `survey` + Rung (H-169 limit 6).
      * anything else -- `faction_holding`: a faction's own Proposition answers for itself, a person
        for the one faction he is committed to.
    A dead man's rung leaves with him (`World.remove_person`), so `class_of` answers `None` and the
    sheet declines."""
    subject = _operand(a, "subject")
    prop = faction_of(w, subject)
    return None if prop is None else asdict(faction_q.resolve(w, prop))


# THE KEY A FORGED SHEET FALSIFIES: the one its holders' decisions read their addressee from
# (`rosters.yaml: record_sourced_operands`, the sheet consumer, H-169 limit 5). Read off that map,
# never spelt here, so the forgery always lies about exactly what a reader acts on -- a perturbation
# of a key nothing reads would be `ID-13`'s dead carrier -- and a map that drops the sheet fails here
# at import instead of forging a lie nobody reads.
_ADDRESSEE_KEY = RECORD_CONTENT.get("addressee")
_FORGED_SHEET_KEY = RECORD_SOURCED_OPERANDS[faction_q.SHEET_KIND][
    (RECORD_CONTENT.get("read_from") or {}).get(_ADDRESSEE_KEY, _ADDRESSEE_KEY)]


@effect_for("forge")
def _eff_forge(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """v9 IN-45 -- A FORGED FACTION SHEET: `survey`'s document, minted through the same one mint (r2
    `02` §A.15's *"the same one-line delegation `issue` gets"*), saying ONE THING FALSE -- that the
    FORGER heads the faction. #453's row for the verb
    (`proposals/2026-10-03-verb-coverage-and-gap-fill.md` `:515`): *"a faction the forger holds a
    claim on (`survey`'s cell); `survey`'s mint with perturbed content"*.

    WHAT IS FALSE, AND WHY THAT KEY: `_FORGED_SHEET_KEY`, the key the sheet consumer reads a holder's
    addressee off (`head`). A petition its holder files on the strength of it is addressed to the
    forger, who then holds the petition (`give` it, sit on it). The rest is TRUE AT THE MOMENT OF
    WRITING: a forgery a reader could check against the world on every key but one is the
    convincing kind, and one false key is the least the verb can say and still be a forgery.
    [ASSUMPTION; medium; Jordan to correct; revert: another key, or the act declaring its lie --
    which a computed act cannot carry (`H-94`).]

    ⚠ v9 SC-02 `22b` STEP 25: `Record.forgery_quality` IS WRITTEN HERE, WITH ITS READER IN THE SAME
    CHANGE (`H-210`): the minted sheet carries `Fixtures.default_forgery_quality` (`_mint_sheet`, through
    `_mint_document`), and an EXAMINATION contests it -- an inquiry's roll on the Record (`research`,
    rolled through `graded_inquiries`' route) carries the quality into its obstacle
    (`seam/wrappers/sigma.py::contest_input` -> `modules/social_contest/roll.py::obstacle`), so a better
    forgery is harder to find, and what a finding then deposits stays FI-03's (`_found_claims`). A
    HOLDER still cannot read it -- *"a forged writ and a genuine writ are indistinguishable in every
    executor's ledger -- by construction, not by a flag"* (r2 §A.15) -- so the content deposit
    (`loop/witness.py`) hands a holder the same claim either way; what this forgery does downstream is
    its false `head`, and how hard it is to find out. [ASSUMPTION; medium; Jordan to correct; revert:
    `default_forgery_quality = 0`, the control, and the examination reads every Record alike.]

    DECLINES (`NO_CHANGE` -> `forge.refused`, the `write` clause) exactly where `survey` does: the
    subject coheres under no single faction. (So a forge on a RUNG mints since v9 IN-12, as a survey
    does: the two read WHICH faction through one helper, `_resolved_sheet`, by design.)
    G3 -- THE FORGER'S OWN `hold`, `T-m`, `survey`'s. G4 -- WHAT IT NAMES: THE RECORD, whole,
    earning `record.forged`; a new id always moves.
    ⚠ THE FORGER HOLDS IT, SO HE IS ITS FIRST HOLDER and the deposit hands him what it says, as it
    would any holder: the instrument does not know he wrote it (the deposit carries no attribution,
    r2 §A.9). His own petition on it would be addressed to himself and is declined person-side
    (`counterparty:`), so the lie misleads others, not him, on the one decision that reads it."""
    return _mint_sheet(w, a, forged=True)


# The kind each half of `give` earns: the `give` row's `emits:` in its declared order (`verb_table.yaml`,
# Record then Rung), read off the table so neither kind is spelt here -- `_SEIZED_RECORD`'s shape.
_GIVEN_RECORD, _GIVEN_RUNG = VERB_TABLE["give"].emits


@effect_for("give")
def _eff_give(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """Plan position 16 (`H-84`): the actor's `hold` on the Record ENDS and the receiver's OPENS, in
    ONE write -- the first verb that moves a Record to another person.

    CLOSE, THEN OPEN, INSIDE ONE `apply`, AND THE ORDER IS THE GATE'S CONDITION RATHER THAN THIS
    BODY'S DISCIPLINE. The giver's close is `T-m`; the receiver's open is admitted only under the
    `handover` basis (`state/gate.py::tenure_write_basis`), which requires the actor to have ended
    their own live `hold` on the same object in the SAME write. So a `give` that forgot the release
    is `NotYours` with both edges put back -- `hold_force` never sees two holders -- and one that
    released in an earlier write finds no licence in this one.

    WHICH EDGE CLOSES: the ONE live `hold` on the Record, read through `hold_force` (the owner of
    *who holds this*, which raises on two rather than choosing), and only if it is the ACTOR's --
    `_eff_confer` closes every hold on its object because a conferral displaces the incumbent;
    a gift displaces nobody but the giver, and closing another person's edge here would be
    refused by the gate anyway. Anything else declines (`NO_CHANGE` -> `give.refused`). Whether the
    receiver may be given it at all is asked first and not twice: a person standing here is the
    row's typed cell (`with`, plan position `14`, which retired `_req_give`), and not the giver is
    the fold's `counterparty` clause.

    v9 IN-12 (`give` + Rung, #453 §9.6): THE OBJECT MAY BE A RUNG -- a CESSION, the one consensual route by
    which title moves. Same two-hold write, same gate basis (`handover` is general over every non-seat
    `hold`); the kind earned is `rung.ceded` there and `record.given` for a Record. A rung whose `hold` the
    actor does not carry (nobody holds it, or somebody else does) declines, as a Record does.

    G4 -- WHAT IT NAMES: the two edges, OPENED FIRST as `_eff_confer` names them. Both are `edge`
    subjects the tenure diff judges, and both earn the object's kind (`record.given`, or `rung.ceded`). The receipts
    therefore name TENURES, not the Record -- `_eff_confer`'s lesson on what a receipt may assert --
    and every reader that wants the Record goes through `epistemic._hold_tenure_ends`, which is
    `claim_subjects`' and `seen_subject`'s route and, since this position, WITNESS's deposit rule's.

    THE RECEIVER'S EDGE ID carries the act (`hold:<record>:<act>`): a Record handed A -> B -> A
    inside one tick would otherwise re-mint A's first `hold` id, and two Tenures sharing an id is
    what `World._tenure_changes` tolerates rather than wants."""
    rid, to = _operand(a, "subject"), _operand(a, "to")
    # v9 IN-12 (`give` + Rung, #453 §9.6): THE OBJECT IS A RECORD OR A RUNG, and the cell no longer says
    # which (the grammar has no disjunction), so the kind is asked HERE. Anything else -- a seat, a person
    # -- declines (`NO_CHANGE` -> `give.refused`); the gate's `handover` would refuse a seat regardless.
    # The kind earned follows the object: a ceded rung publishes `rung.ceded`, never `record.given`.
    if rid in w.records:
        earns = _GIVEN_RECORD
    elif rid in w.rungs:
        earns = _GIVEN_RUNG
    else:
        return NO_CHANGE
    held = hold_force(w, rid)
    if held is None or held.subject != a.actor:
        return NO_CHANGE
    nt = Tenure(H(w.world_seed, w.tick, to, f"hold:{rid}:{a.id}"), to, rid, "hold", since=w.tick)

    def perform() -> None:
        held.until = w.tick                # the giver's release, FIRST
        w.add_tenure(nt)                   # then the receiver's hold
    return Change((Subject.edge(nt, earns), Subject.edge(held, earns)), perform)


# WHICH RECORD KIND IS A WARRANT FOR A VERB, and WHICH OF ITS CONTENT KEYS NAMES WHAT IT AUTHORIZES: the
# kind is `data/verbs.py::WARRANT_SOURCED`'s (`rosters.yaml: warrant_sourced`, the one loader both the person
# side and this one import), the key `person_q.ABOUT_KEYS`' (the one owner of "what a document is about"),
# never spelt here. v9 IN-12 step 5: `arrest` reads the same map, so the reading is one function for both.
def _held_warrants(w: "World", actor: str, verb: str, named: str) -> tuple:
    """THE WARRANTS THE ACTOR HOLDS NAMING `named`, for `verb` -- the ids of the Records on his own live
    `hold` edges whose kind is `verb`'s warrant kind (`rosters.yaml: warrant_sourced`) and whose
    about-key content says `named`, in tenure order. World-side: the effect owns the licence because the
    gate never reads a Record's content (K-52); the person-side twin is `decision/options.py::
    opening_set`'s formation on the same reading, off his own ledger."""
    kind = WARRANT_SOURCED[verb]
    key = ABOUT_KEYS[kind]
    out = []
    for t in w.tenures:
        if t.kind != "hold" or not t.live or t.subject != actor or t.object not in w.records:
            continue
        rec = w.records[t.object]
        sm = rec.subject_matter
        if rec.kind == kind and isinstance(sm, dict) and sm.get(key) == named:
            out.append(t.object)
    return tuple(dict.fromkeys(out))


def _held_warrant_names(w: "World", actor: str, rid: str) -> bool:
    """DOES A WARRANT THE ACTOR HOLDS NAME RECORD `rid`? -- `seize`'s licence (IN-12 step 6), read
    through `_held_warrants`, the one reading `arrest` shares."""
    return bool(_held_warrants(w, actor, "seize", rid))


# The kind each half earns: the `seize` row's `emits:` in its declared order (`verb_table.yaml`, Record
# then Rung), read off the table so neither kind is spelt here.
_SEIZED_RECORD, _SEIZED_RUNG = VERB_TABLE["seize"].emits


def _take_hold(w: "World", a: "Act", obj: str, held: Optional[Tenure], earns: str) -> Change:
    """THE TAIL BOTH HALVES OF `seize` SHARE: the actor OPENS a `hold` on `obj`, and the `hold` it
    displaces (`held`, or `None` when nobody held it) CLOSES, in ONE write. THE NEW EDGE'S ID carries the
    act (`hold:<obj>:<act>`), `_eff_give`'s salting. G4 -- WHAT IT NAMES: the two edges, the opened one
    first, both earning `earns`. The close is written FIRST, then the open.
    ⚠ THE `Tenure` KIND IS A STRING LITERAL HERE ON PURPOSE, NOT A PARAMETER: `data/verbs.py::
    _derive_openers_from_effects` reads which verb opens which kind off that literal, walking same-file
    helpers from the registered effect, so `seize` stays a `hold` opener through this helper (the
    `_eff_commit` note below records what a parameterised kind did to the walk)."""
    nt = Tenure(H(w.world_seed, w.tick, a.actor, f"hold:{obj}:{a.id}"), a.actor, obj, "hold", since=w.tick)

    def perform() -> None:
        if held is not None:
            held.until = w.tick            # the dispossessed holder's hold, FIRST
        w.add_tenure(nt)                   # then the seizer's
    return Change(tuple(Subject.edge(e, earns=earns) for e in (nt, held) if e is not None), perform)


@effect_for("seize")
def _eff_seize(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """v9 IN-12 step 6 (#453 §10.4, the `seize` row), THE RECORD HALF: the previous holder's `hold` on a
    Record ENDS and the actor's OPENS, in ONE write, WITHOUT the holder's consent -- `give`'s body, the
    one other verb that moves a Record, with the licence that `give` takes from the giver's own edge
    replaced by a warrant and a seat.

    WHAT LICENSES IT, IN THE ORDER IT IS ASKED, each one owner of its rule: (1) the Record exists and
    one other person holds it (`hold_force`, the owner of *who holds this*); (2) the actor HOLDS A
    WARRANT NAMING IT (`_held_warrant_names`) -- the effect's, because it is a Record's content;
    (3) the exercised seat may seize from that holder (`may_seize`, the gate's own predicate, so an act
    the precondition admitted is never killed at the gate by a disagreement about the holder's home).
    Anything else declines (`NO_CHANGE` -> `seize.refused`). A Record the actor already holds, or that
    nobody holds, moves nothing.

    THE GATE: the close is `seizure` (`state/gate.py`), the open is `T-m` (the actor opening a non-seat
    `hold` for himself). A SEAT IS NEVER SEIZED: the gate's `seizure` clause admits only a Record or a
    Rung, so a hand-built act that skipped the precondition is `NotYours`, not a taking. ⚠ SINCE v9
    IN-13 the row's `existence` conjunct is gone (the object widened to a Rung, `verb_table.yaml`'s
    `requires_typed_note`): an Office has no place, so the `authority` conjunct refuses it first
    (`seize.unauthorized`); planted past it, a seat is no Record and no settlement and `_seize_rung`
    declines it; and the gate still admits neither half on an Office. A subject that is no Record goes
    to `_seize_rung`, the Rung half.

    G4 -- WHAT IT NAMES: the two edges, the opened one first as `_eff_give` and `_eff_confer` name
    theirs; both earn the Record half's kind, `record.seized` (the Rung half earns `rung.seized`). The receipts name TENURES, not the Record.
    THE NEW EDGE'S ID carries the act (`hold:<record>:<act>`), `_eff_give`'s salting, so a Record taken
    and taken back inside one tick does not re-mint the first `hold` id."""
    rid = _operand(a, "subject")
    if rid not in w.records:
        return _seize_rung(w, a, rid)
    held = hold_force(w, rid)
    if held is None or held.subject == a.actor:
        return NO_CHANGE
    if not _held_warrant_names(w, a.actor, rid) or not may_seize(w, a.actor, a.via, held.subject):
        return NO_CHANGE
    return _take_hold(w, a, rid, held, _SEIZED_RECORD)


def _seize_rung(w: "World", a: "Act", rid: str) -> Change:
    """v9 IN-13 (#453 §10.4 step 8), `seize`'S RUNG HALF: the actor opens a `hold` on an OCCUPIED
    SETTLEMENT, and whatever `hold` it already carries closes -- one town changing hands without its
    territory (#453 §9.1: a hold on the settlement itself shadows a territory hold in
    `holder_faction_of`'s walk). The ROW stays keyed as IN-12 step 6 built it; the halves split HERE, on
    what the subject is (a Record, or not), and share the gate's `seizure` basis for the closure and
    `T-m` for the opening.

    WHO MAY SEIZE: with no hold on the town, the seat's authority comes only from the fold's precondition
    (eligibility `remit:issue` via `seat_hold`, plus the `authority` purview conjunct); the Record half
    calls `may_seize` in the effect, so the gate does not later refuse an act the precondition admitted.

    THE LICENCE IS OCCUPATION, read at the effect as `raze`'s will be (#453 §10.4 steps 8 and 11): the
    exercised seat's FACTION (`faction_prop_id` of its display faction) `mustered` at the settlement
    (`world_q.mustered`, the one query of who stands there), the settlement held by ANOTHER faction
    (`holder_faction_of`). It asks nothing of the defenders: an opposed `Won` that removed nobody still
    leaves the attacker mustered there, so the seizure is admitted (#453 exit (vii)). DECLINES
    (`NO_CHANGE` -> `seize.refused`, the `write` clause), each one change from an admitted seizure:
      * the subject is not a Rung of a `march_target_kinds` kind (a seat, a person's own rung, a
        territory, a hearth) [ASSUMPTION; medium; Jordan to correct: occupation is defined at the
        places a march arrives at; revert: any Rung kind, the licence still occupation];
      * the actor is not committed to the seat's faction (`faction_holding`; the title written is his own
        hold) [ASSUMPTION; medium; Jordan to correct; revert: drop the decline];
      * the seat's faction is not mustered there (no occupation);
      * nobody holds the settlement (H-166: who holds an unheld place is unruled) or the seat's own
        faction already does (nothing to take);
      * the actor already holds it, or the closure's holder is one the seat may not seize from
        (`may_seize` with the rung as the place, so an act the precondition admitted is never killed
        at the gate).
    ⚠ THE RUNG HALF'S FORMATION AND EXECUTION LICENCES DIFFER: it forms person-side wherever a held
    dispensation's `terms` names the rung (`rosters.yaml: warrant_sourced`; `test_season_shape.py` plants
    one on a hearth), but at the effect it licenses on OCCUPATION, not on the warrant. No computed source
    of such a warrant has been measured -- a named residue, not a wiring gap in this effect."""
    mine = occupying_faction(w, a.via, rid)
    if mine is None:
        return NO_CHANGE
    # The title written is the ACTOR'S OWN hold, and a hold coheres under the faction its holder is
    # committed to (`faction_holding`; `None` for no commit or two): an actor not committed to the seat's
    # faction would take the town for a faction that is not his [ASSUMPTION; medium; Jordan to correct;
    # revert: drop the decline].
    if faction_holding(w, a.actor) != mine:
        return NO_CHANGE
    held = hold_force(w, rid)
    if held is not None and (held.subject == a.actor
                             or not may_seize(w, a.actor, a.via, held.subject, rid)):
        return NO_CHANGE
    return _take_hold(w, a, rid, held, _SEIZED_RUNG)


def _may_close_custody(w: "World", seat: str, prisoner: str) -> bool:
    """Could the seat's LIVE HOLDER close a `detain` the prisoner owns on it -- `may_determine`, the
    predicate `state/gate.py`'s `determination` clause closes a restraint under (`pardon`'s basis)? An
    unheld seat closes nothing."""
    held = hold_force(w, seat)
    return held is not None and may_determine(w, held.subject, seat, prisoner)


@effect_for("arrest")
def _eff_arrest(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """v9 IN-12 step 5 (#453 §9.1, the `arrest` row): A `detain` EDGE OPENS, the prisoner (the act's
    `subject`) -> THE SEAT THAT ISSUED THE WARRANT the actor holds naming him (`issuing_seat`, K-17/K-52):
    the enforcement seat (`Act.via`) acts but does not own the custody, so the issuing seat's bench is
    who may `pardon` it (`state/gate.py`'s `determination` closes a restraint only through the seat that
    is its object). The row is contested (`a standing`); the fold calls this body on `Overwhelming`,
    `Success` and `Partial` only, each opening the same edge (#453: no degraded magnitude for an edge).

    WHAT LICENSES IT, IN THE ORDER IT IS ASKED, each one owner of its rule: (1) the subject is a person
    and not already in custody (`world_q.restrained`, the restraint's one read -- one live `detain` per
    prisoner, #453 §8.1 Custody [ASSUMPTION; medium; Jordan to correct; revert: a second bench's
    warrant opens a second custody, "relaxation to the secular arm"]); (2) the actor HOLDS A WARRANT
    NAMING HIM (`_held_warrants`, `seize`'s reading); (3) the warrant's issuing seat is readable
    (`issuing_seat`) AND ITS LIVE HOLDER COULD CLOSE THE CUSTODY (`may_determine` over the prisoner,
    the gate's own predicate for `determination`, which `pardon` closes under): a custody is opened only
    on a seat whose bench could `pardon` it, so a warrant from an issue-only seat, or from a seat whose
    ground does not hold the prisoner, opens nothing
    [ASSUMPTION; medium; Jordan to correct; revert: arrest opens a custody on any issuing seat and a
    custody nothing can close is a recorded limit]; (4) the exercised seat may take him (`may_warrant`,
    the gate's own predicate, so an act the precondition admitted is never killed at the gate). Anything
    else declines (`NO_CHANGE` -> `arrest.refused`, the `write` clause). Several warrants: the first in
    tenure order whose issuing seat is readable and could close it.

    THE GATE: `warrant` (`state/gate.py`: an opened `detain` whose object is a seat, owned by another
    person, by a seat granted `WARRANT_ACT` whose purview reaches his home). The kind is a LITERAL so
    `data/verbs.py::_derive_openers_from_effects` reads `arrest` as a `detain` opener.
    G4 -- WHAT IT NAMES: the edge, which always moves (absent -> present)."""
    prisoner = _operand(a, "subject")
    if prisoner not in w.persons or prisoner == a.actor or restrained(w, prisoner, DETAIN_KIND):
        return NO_CHANGE
    seat = next((s for s in (issuing_seat(w, rid)
                             for rid in _held_warrants(w, a.actor, a.verb, prisoner))
                 if s is not None and _may_close_custody(w, s, prisoner)), None)
    if seat is None or not may_warrant(w, a.actor, a.via, prisoner):
        return NO_CHANGE
    nt = Tenure(H(w.world_seed, w.tick, prisoner, f"detain:{seat}:{a.id}"), prisoner, seat, "detain",
                since=w.tick)
    return Change((Subject.edge(nt),), lambda: w.add_tenure(nt))


@effect_for("destroy_record")
def _eff_destroy_record(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """§E3: writes `(Record, exists)`. The Record goes, and every `hold` on it ends -- S15.3's
    rule that a tenure dies THROUGH the death of what it is over, never beside it.

    G4 -- WHAT IT NAMES: THE RECORD, whose existence is the whole of the declared write; it always
    moves (present -> absent), so a destruction that finds its record is never a no-op and one that
    does not declines (`NO_CHANGE` -> `destroy.refused`, as the old `None` did). The closed holds
    are the cascade -- F3 admits each as `destroy's cascade` because this same write removed the
    id -- and are not named, as they were never reported.

    v9 IN-26 (BOUND-PAPER, `A-13`): THE RECORD IS THE BOUND `subject` -- the row's typed cell binds it
    (`existence` kind `Record`, `held_by` the actor) and a computed Candidate carries it; the `record`
    payload key this read before no Candidate carried, so it is gone rather than kept as a second
    spelling. It is the SINK for paper the verb-coverage survey found none for (`Record.ttl` has no
    reader): a holder burns what he holds. Whether anybody FORMS it is `opening_set`'s
    (`Fixtures withheld_verbs`, `rosters.yaml: own_hold_declines`), never this body's. A Proposition
    is never a subject here: §14 makes it undestroyable, and the cell's `existence` conjunct refuses
    one before this runs."""
    d = a.payload if isinstance(a.payload, dict) else {}
    rid = d.get("subject")
    if rid is None or rid not in w.records:
        return NO_CHANGE

    def perform() -> None:
        del w.records[rid]
        for t in w.tenures:
            if t.object == rid and t.live:
                t.until = w.tick
    return Change((Subject.entity("records", rid),), perform)


@effect_for("utter")
def _eff_utter(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """§E3: writes `(Proposition, exists)`. §14: a Proposition is IDENTITY-BEARING AND IMMUTABLE,
    fixed at utterance and never destroyed -- `Proposition` is a frozen dataclass, so that is
    structural here rather than asserted.

    G4 -- WHAT IT NAMES: THE PROPOSITION, whole; it always moves (absent -> present), because an
    id already uttered is declined before anything is built (`NO_CHANGE` -> `act.refused`, the
    fold's own kind, since the row declares no refusal -- as the old `None` produced).

    v9 IN-11 (#453 §10.4 step 2) -- THE UTTERER HOLDS WHAT HE UTTERED. Beside the Proposition the
    effect opens a `hold` Tenure owned by the actor whose object is the new Proposition, the
    maker's-hold shape `_mint_document` already gives a Record (S13: possession is a `hold`, never
    a field; `rosters.yaml: hold_object_kinds` admits a Proposition). It is what makes `commit`
    reachable from computed play: a Proposition has no place (`world_q.place_of` answers `None`),
    so until it is somebody's own edge no question can be ABOUT it -- `reach`'s limb 2 (every live
    Tenure's object) is the one route, and Q2 then raises the utterer's own claim about the
    Proposition as a question whose referent `commit`'s cell (`existence` of `subject` kind
    `Proposition`) admits. The edge is the actor's own (`T-m`), like the Record maker's. NOT
    NAMED as a subject, on `_mint_document`'s precedent: the receipt this write mints is the
    Proposition's (`Proposition.exists`, the row's first pair), and naming the edge would mint a
    `(tenure, Proposition.exists)` receipt for a write that pair never made (`_eff_confer`'s
    ID-9 note); G3's tenure observation still judges it. What a hold costs is `H-92`'s (it buys
    budget, `decision/budget.py`) -- registered, not decided here."""
    d = a.payload if isinstance(a.payload, dict) else {}
    pid = d.get("proposition") or f"prop:{a.id}"
    if pid in w.propositions:
        return NO_CHANGE                  # immutable: an utterance never overwrites one
    prop = Proposition(pid, d.get("mood") or "OUGHT", d.get("subject") or a.actor,
                       d.get("predicate") or "", d.get("value"), w.tick)
    held = _makers_hold(w, a.actor, pid)

    def perform() -> None:
        w.propositions[pid] = prop
        w.add_tenure(held)
    return Change((Subject.entity("propositions", pid),), perform)


@effect_for("commit")
def _eff_commit(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """§E3 `:426`: commits the actor to a Proposition -- a new `commit` Tenure opens, subject the
    actor, object the Proposition the act names (`Act.subject`, the row's typed precondition:
    *the Proposition exists, immutable, §14*). Plan position `7a`. `commit` is a `tenure_kinds`
    member (`rosters.yaml`) with no opener until this effect -- `tenure_kinds_without_an_opener()`
    reported it, and `resolvable_verbs()` (`loop/driver.py`) excluded the verb for want of one,
    per §E3's `writes: ["Tenure.since"]` with nothing to perform it.

    ⚠ THE BAREST OPENER IN THIS FILE: no seat, no closure, no per-kind branch. `commit` is
    `own`-eligible with `beneficiary: actor` and carries no `via`, so the edge it opens names the
    actor as its own subject and is admitted under `T-m` (`state/gate.py::tenure_write_basis`) --
    the same basis `_eff_confer`'s new `hold` and `_eff_release`'s closures stand on. Read
    `_eff_confer` above for the general shape (name the edge, defer the mint into the closure);
    its seat/incumbent-closure logic does not apply here, because nothing closes and no `via` is
    read.

    G4 -- WHAT IT NAMES: THE EDGE, whole -- the one write the row declares. It always moves
    (absent -> present: `add_tenure` mints a fresh Tenure, never overwrites one), so a `commit`
    that reaches this effect is never a no-op; the row's one refusal (the Proposition does not
    exist) is the typed precondition's, asked before this ever runs, and there is nothing left for
    the effect itself to decline.

    THE ID SALTS ON THE OBJECT AND THE ACT, `_eff_give`'s `f"hold:{rid}:{a.id}"` pattern (`H`'s
    `subject_id` slot is the new Tenure's own subject, its `purpose` is `f"{kind}:{object}:{act}"`)
    -- BATCH-CLOSE FINDING (methodology-close Phase 1, antagonist), corrected from the plain
    `f"commit:{prop_id}"` this shipped with: two different actors committing to the same
    Proposition already minted distinct ids (each one's `subject_id` is its own actor), but an
    actor who releases a `commit` and re-commits to the SAME Proposition within the same tick
    would otherwise mint the identical id as the now-closed one -- the same collision `_eff_give`'s
    own docstring names and salts against. When this salt landed `commit` never executed in computed
    play (H-156), so no release-then-reopen path was reachable; since v9 IN-11 `commit` EXECUTES
    (utter mints the utterer's hold, Q2 raises the Proposition as a referent) and `release` closes
    it, so the path is reachable and the salt is load-bearing, not merely free.

    ⚠ BUILD-ORDER BO-9/BO-10 (`proposals/2026-09-17-governance-and-behaviour/01_THE_BUILD_ORDER.md`
    §7.2): the first build of this effect, before any question source offered a Proposition
    referent, measured `commitment.made : 0` / `commitment.refused : 42` on one populated season --
    a structural gap in `operands_for`/`questions_for`, not in this body, and HELD rather than
    shipped. Items 5/7/8 (here `15`, `15c`, `15b`) are what BO-10 named as opening that aperture;
    this effect is unchanged from the held draft, because the diagnosis put the gap upstream of it.

    ⚠ NOT FACTORED WITH `_eff_oblige` BELOW, THOUGH THE TWO BODIES ARE IDENTICAL BUT FOR ONE STRING
    -- BATCH-CLOSE FINDING (methodology-close Phase 2, REUSE/SIMPLIFICATION lenses), REVERTED after
    trying it: `_derive_openers_from_effects` (`data/verbs.py::OPENERS-DERIVE`) is an AST walk over
    THIS FILE's own source that reads which verb opens which `tenure_kinds` member off a STRING
    LITERAL at each `Tenure(...)` call site, by design (its docstring: *"every site today names
    `kind` as a STRING LITERAL"*). A shared helper taking `kind` as a parameter makes that literal
    disappear from this file's source, and the walker silently stopped seeing `commit`/`oblige` as
    openers at all (`test_obligees.py::test_17a_oblige_is_resolvable_and_takes_releases_route`
    caught it: `_OPENERS_FROM_EFFECTS.get("oblige")` went from `["oblige"]` to `[]`). The
    duplication is real and the fix is not -- this is `create_record`/`issue`/`petition`'s
    `_mint_document` in reverse: that helper is safe to share because all three name the SAME
    literal kind (`hold`) inside it; `commit` and `oblige` do not, so nothing here can be factored
    without either losing the literal or hand-editing the derived roster back into a second copy."""
    prop_id = _operand(a, "subject")
    nt = Tenure(H(w.world_seed, w.tick, a.actor, f"commit:{prop_id}:{a.id}"), a.actor, prop_id,
                "commit", since=w.tick)
    return Change((Subject.edge(nt),), lambda: w.add_tenure(nt))
