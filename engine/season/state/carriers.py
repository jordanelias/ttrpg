"""`season.state.carriers` -- THE PRIMITIVES. The sixteen things the model is made of.

`Tenure`, `StateChange`, `Event`, `Claim`, `Sensation`, `View`, `Question`, `Candidate`, `Scene`,
`Act`, `Person`, `Site`, `Record`, `Proposition`, `Office`, `Rung` -- and
`matrix_rows_without_a_field`, which is not a carrier and is here for a reason given below.
Importers name this module directly (`from ..state.carriers import Person`; ED-IN-0203).

⚠ WHY `matrix_rows_without_a_field` IS IN THIS MODULE AND NOT IN `data/`. It answers *does this
matrix row's `fieldname` name a real field of its `record_kind`* by looking the KIND UP AS A NAME
(`globals().get(kind)`) and reading the class's declared fields. That lookup resolves in the
module it is written in, so it has to be written where the classes are -- and `season.data` cannot
import this module, because the carriers read `data.rosters` and `data.fixtures` and the arrow
would reverse. Put it in `data/matrix.py` and it silently reports every kind `unmodelled`: no
exception, no red test, just a clean bill over a check that stopped looking. A reflective lookup answers
about the FILE IT RUNS IN, and moving the file moves the answer without moving the code.

⚠ THIS MODULE IMPORTS NOTHING FROM `world` OR ABOVE, AND THE DIRECTION IS THE POINT. A carrier is
a thing the world holds; it may not know about the store that holds it. `state/world.py` imports
these nine classes and this module imports nothing back, so the two files together carry no cycle
-- which is checkable in one grep (`grep -n 'import' state/carriers.py`) rather than asserted here.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from types import MappingProxyType
from typing import Any, Mapping, NamedTuple, Optional

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import MATRIX
from ..data.rosters import (
    BINDS_BASES, CONFERRAL_BASES, DETAIN_KIND, QUESTION_SOURCES, RECORD_KIND_KEYS, RECORD_KINDS,
    REFERENT_CLASSES, REMIT_ACTS, REVOCATION_BASES, RUNG_KINDS, office_faction, require_member,
    title_domain,
)
from ..gaps import Forbidden, Unowned, Unspecified
from ...substrate.descriptors import ATTRIBUTE_CEILING, ATTRIBUTE_FLOOR, ATTRIBUTES
from .ids import SeatId, draw_factory


@dataclass(frozen=True)
class Term:
    """`04 §B.8`'s `term?` -- A DECLARED END ON A TENURE, and the field `T-n` has always needed.
    `04` §F's `F.3` row: *"`Tenure.term`; MATTER matures it"*.

    `matures_at` is the tick at whose MATTER barrier the term matures -- `loop/matter.py`'s tenure-
    term branch closes the edge there, through the gate's `T-n` basis, with `causes[] =
    [declared_by]` (`04 §B.8`: *"a `matures_at` MATTER matures with `causes[] = term.declared_by`"*;
    AX-5: *"a matured term cites the act that wound it"*). `declared_by` is that act's id -- the
    opening act, or the act that last RENEWED the term (`_eff_transfer`'s payment of `upkeep`), so a
    lapse always cites whoever last wound the clock, which is the act that makes it a story rather
    than a timer.

    ⚠ FROZEN, AND A RENEWAL REPLACES IT WHOLE. A term is a value, not a place: an act that winds it
    again writes a new `Term`, so `World._tenure_snapshot` can compare it by value with no copy, and
    no effect can advance a clock in place where the tenure diff cannot see it.

    ⚠ `closer` IS NOT CARRIED, AND THAT IS `ID-13`, NOT AN OMISSION. `04 §B.8` spells `term?
    (matures_at, declared_by, closer)` and then says of `closer` itself: *"`Seat.revocation` is
    authoritative and `term.closer` names a basis, not a second authority"*. Ending a hold early is
    already `T-o`, the seat's revocation basis through `Act.via`, and nothing reads a
    per-term closer -- a field declared for a reader that does not exist is the defect a
    `Tenure.conferrer` would be (see the note in `Tenure`). The day a term needs a closer the seat's own basis cannot
    express, it is added with that reader."""
    matures_at: int
    declared_by: str


# THE PAYLOAD KEY THAT MARKS A DETERMINATION-IMPOSED `oblige` (`_eff_determine`'s `_disposal` writes it,
# value the determining act's id): the edge is a SENTENCE, not an OATH. Read through `Tenure.imposed`.
DETERMINED_BY = "determined_by"


@dataclass
class Tenure:
    """S15 -- THE ONE EDGE. Owned by its SUBJECT (S15.1)."""
    id: str
    subject: str
    object: str
    kind: str
    since: int
    until: Optional[int] = None
    # NO `conferrer` FIELD: it would reach no reader, which by `ID-13` is not a weak field but one that
    # does not exist, wearing a schema's clothes. WHO MAY REVOKE is the
    # Seat's declared `revocation` basis (`T-o`), not the identity of whoever conferred; WHAT
    # CONFERRED a Tenure is the opening Act, in an append-only log with `causes[]`. A field here
    # would be a second home for a fact the act already holds — `ID-2`.
    degree: Optional[str] = None
    payload: Any = None
    # `04 §B.8`'s `term?`; `Term`'s own docstring says what it is and who
    # writes it. ⚠ BESIDE `payload`, NOT IN ITS PLACE, WHATEVER `04 §B.8`'s *"Replaces
    # payload?"* AND `write_matrix.yaml`'s 2026-09-03 note ASKED: `payload` has a writer (`World._grant_remit`,
    # the remit grant a seat confers on its holder), a reader in `granted_acts` below, and the gate's
    # `conferral` re-grant clause (`moved == {"payload"}`). A grant and a declared end are two facts, so
    # they are two fields. ⚠ `Tenure`'s ENCODING FOLDS INTO `World.content_hash` AND CARRIES EVERY FIELD
    # NAME, so a field here moves the digest of every world holding a Tenure.
    term: Optional[Term] = None

    # THE VERSION OF THIS EDGE: it counts every attribute assignment, so `World._tenure_snapshot` and
    # `_tenure_changes` can tell an unmoved Tenure from a possibly-moved one by comparing one int
    # instead of reading eight fields. A class attribute and NOT a dataclass field (no annotation), so it
    # is in no repr, no `==`, no `content_hash` encoding. It counts SETS and not changes: a set to the same
    # value costs one comparison of the eight fields, never a missed change. What it cannot see is a write
    # that bypasses `__setattr__` (`t.__dict__[...]`, `object.__setattr__`); `World.discard_caches` checks
    # for exactly that at every barrier and raises `InstrumentDefect`. An in-place edit of a payload dict
    # is not an assignment either; the diff compares every non-None payload by value.
    _v = 0

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)
        object.__setattr__(self, "_v", self._v + 1)

    @property
    def live(self) -> bool:
        return self.until is None

    @property
    def imposed(self) -> bool:
        """A determination imposed this edge (an `oblige` sentence); it is not an oath the holder swore."""
        return isinstance(self.payload, dict) and DETERMINED_BY in self.payload

    @property
    def granted_acts(self) -> tuple:
        """THE GRANT THIS TENURE CARRIES -- `H-71` arm 2, and the ONE owner of the payload's shape.

`World._grant_remit` is the ONLY writer of the grant (`remit_acts`); its readers are this
        property and `seat_rung` below: §8 -- the shape of a payload is a
        rule, so it lives once. (An `oblige` a determination imposes carries one other key,
        `DETERMINED_BY`, read through `imposed` above, so that `purview_reaches` does not read it
        as an oath.) A caller that reaches into `payload["remit_acts"]` itself has
        re-implemented it and will drift.

        WHAT IT IS, and it is NOT a mirror of the office. `H-71`'s ruled arm 2: *"THE GRANT RIDES
        ON THE TENURE -- `confer` writes the office's remit acts into the `hold` Tenure's
        `payload`, and `person_side_eligible` reads them there."* A remit on the Tenure is not a
        second copy of the office's remit; it is **the grant, which is what a holder actually
        has**. So this is a SNAPSHOT taken when the Tenure opened, and an office whose `remit_acts`
        change later does not retroactively re-grant its sitting holders -- *"an office whose
        remit changes does so by an ACT, which is how everything else in this engine changes."*
        `_grant_remit` carries the same statement from the writing side. ⚠ THAT ACT EXISTS: `establish` re-stamps every live `hold` on the office it
        writes, through `_grant_remit(force=True)` -- so a hand-mutation still reaches nobody and
        the act reaches every sitting holder.

        Returns `()` for every Tenure that carries no grant, which is every kind but `hold` and
        every `hold` on a non-office. A tuple rather than a set: it keeps the order the grants were
        made in.
        """
        p = self.payload
        if not isinstance(p, dict):
            return ()
        acts = p.get("remit_acts")
        # ⚠ RETURNED AS STORED ON THE COMMON PATH, NOT RE-TUPLED. `_grant_remit` writes a tuple,
        # and this property is read inside `any(... for t in p.tenures)` which is itself inside
        # `person_side_eligible`'s loop over `row.eligibility` -- so re-tupling cost N*M
        # constructions of a value that cannot change between them. The `tuple(...)` fallback
        # stays for a payload some other writer set as a list.
        if acts is None:
            return ()
        return acts if isinstance(acts, tuple) else tuple(acts)

    @property
    def seat_rung(self) -> Optional[str]:
        """THE SEAT'S RUNG AS GRANTED -- where the seat's TREASURY is (*"treasury = `Rung.stores` at the office's own rung"*), read off the grant the holder owns.
        `H-160` limit 1 / `H-158`: a holder paying out of his seat's rung gives FROM it
        (`decision/options.py::treasury_of`), and the person-side reader has no `World` (`AX-2`),
        so the rung rides on the Tenure beside `remit_acts`, `H-71` arm 2's own shape and writer
        (`World._grant_remit`). The same SNAPSHOT semantics: as at seating, re-stamped by `establish`.
        It extends `H-71` arm 2's precedent (the grant rides on the Tenure) to the seat's rung, which
        no act can change: `_req_establish` refuses a rung difference on an existing id
        (`loop/predicates.py`; MECHANICAL for `establish`). Layer-1 grade of the stamp itself
        (`04` §B.8's `Tenure :=` lists no payload field; it is a second home for `Office.rung`):
        CONVENTION, an untyped dict key with no per-property guard.

        `None` for every Tenure carrying no grant, and for the grant of a rungless seat -- which has
        no treasury, so a payment through it is not formed."""
        p = self.payload
        return p.get("seat_rung") if isinstance(p, dict) else None




@dataclass
class StateChange:
    """S16 -- THE ONE STATE CHANGE."""
    subject: str
    mode: str
    driver: str
    field: Optional[str] = None
    delta: Any = None
    spec: Any = None


@dataclass
class Receipt(StateChange):
    """G1a -- WHAT THE GATE HANDS BACK, and the only kind of change an Event may carry.

    A `StateChange` says WHAT CHANGED. A `Receipt` says what changed AND THAT THE GATE IS THE ONE
    THAT CHANGED IT. Those are different claims and the tree only ever made the first, so an
    Event's `changes[]` was a set of assertions with no provenance: any caller could construct
    `StateChange(...)` naming a write that never happened, append the Event, and every reader
    downstream -- the witness fold, `claim_subjects`, the content hash -- would take it. That is
    `ID-9` with no instrument against it.

    ⚠ `serial` IS PROVENANCE, NOT DATA, AND THE CONTENT HASH DOES NOT FOLD IT. `World.content_hash`
    reads five named fields off each change -- `subject|mode|driver|field|delta` -- which this
    inherits unchanged. That is deliberate: a provenance token is a fact about who wrote, not about what the world is,
    and folding it would make two worlds with identical state hash differently because their
    receipts were minted in a different order.

    ⚠ IT IS FORGEABLE IN PYTHON AND THE GUARD IS NOT THE CONSTRUCTOR. Nothing stops
    `Receipt(..., serial=7)`; what stops it counting is `state/log.py`, which checks the minting
    gate still holds THAT OBJECT under THAT serial (`minted.get(r.serial) is r`). An identity
    check, not an equality one -- a forged receipt carrying a real serial is a different object
    and fails. `S34`'s enforcement column rates this class of rule *"convention -- the named
    residual risk"* for `__slots__`; this one is stronger than convention because the check is
    executed at append rather than asserted in prose, but it is still Python and a determined
    author with the gate in hand can spell around it. What it forecloses is the ACCIDENT: a
    hand-built change reaching the log because nobody remembered the gate.
    """
    # -1 is the UNMINTED sentinel and is never a key in the gate's minted map, so a `Receipt`
    # built by hand is refused by the same check that refuses a `StateChange` -- it does not need
    # its own branch, and a branch per forgery shape is how a checker acquires a gap.
    serial: int = -1


@dataclass
class Event:
    """S19 -- THE RECORD THAT WAS MISSING. S19.3: three fields are NOT on it and each absence
    is a design decision -- no actor (attribution is a per-witness Claim), no target (observers
    are computed at WITNESS from presence; THE EMITTER DECLARES NO RECIPIENT), no stat_deltas.

    ⚠ `Event` IS AN ATYPICAL SENSE OF THE WORD -- read it as "the occurrence", NEVER as "the
    message". Ordinary usage, and every other engine's usage, makes an event a thing someone did
    to someone; here it is neither, by `T-d` and `T-e`. If you are looking for who did it you want
    a `Claim`; for who learned of it, `WITNESS`. A reader who brings the ordinary sense looks for
    the actor field, does not find it, and concludes the carrier is incomplete -- which is the
    mistake the three absences exist to prevent. Defined at both sites per `CLAUDE.md` §4:
    `architecture/meta/01_AXIOMS.md` §D.9 is the prose home (ED-IN-0220).

    ⚠ THERE IS NO `subject` ON `Event` -- `04:402`'s
    *"No `actor`, no `target`, no `subject` on `Event`"*. Both the actor and the thing written are read
    off the channels that already hold them, through `state/attribution.py` -- `actor_of` walks
    `causes[]` into the act store, `anchor_of` falls back to `changes[]` and then to the cause's own
    anchor. An emitter with no
    act, no change and no antecedent has NOTHING that says what it concerns, and `anchor_of`
    answers `None` for it; `test_g1b_attribution.py` plants one and asserts WITNESS deposits
    nothing, so that channel going quiet is observed rather than assumed. A hand-built Event that
    needs an anchor carries a change naming it (`harness/probes.py::about`)."""
    id: str
    kind: str
    changes: list[StateChange]
    causes: list[str]
    emitted_at: int
    degree: Optional[str] = None
    # `W-B`. WHAT THE FOLD READ TO REACH THIS EVENT -- a tuple of `Observation`, the same triple a
    # `Claim` carries, which is what `Observation`'s own docstring says it is: *"an Observation is
    # what a Claim would be if the reader wrote one."*
    #
    # ⚠ IT IS NOT A FOURTH ABSENT FIELD. S19.3 names three fields deliberately NOT on an Event --
    # actor, target, stat_deltas -- and each absence is a design decision about ATTRIBUTION or
    # RECIPIENCY. This is neither: it is the record of what the fold read, and §27.1 already makes
    # reading the precondition the fold's business. `PLAN.md` §8.1's ban is on `target`/`actor`,
    # and `H-79` spent its own argument on reading `changes[]` rather than adding a field, so the
    # bar for adding one is stated here: this carries something NO existing field holds. `changes[]`
    # is what the act WROTE; `observed` is what it READ, and a refusal writes nothing and reads
    # everything.
    #
    # ⚠ EMPTY IS HONEST AND IS THE COMMON CASE. An untyped verb, a `NO_PRECONDITION` verb, and
    # every Event `matter()` or `calendar()` emits carry `()`: no read went through the
    # `Observation` channel. A verb on `REQUIRES_PREDICATES` reads the world through a hand-written
    # predicate that records nothing, so it too carries `()` -- that is a gap in the OLD channel,
    # not a claim that nothing was read, and it closes when the verb is typed.
    #
    # B14.03: and the outcomes an effect derives from the scene it wrote (a felling's source, a body that broke
    # first, a named draw), as Observations WITNESS deposits. `fell_to` and the scene's numbers name no one as a doer; `fell_to_hand` (B14.16) names the standing party, and `first_blood` the one who struck first.
    observed: tuple = ()
    # CP-T03-02. HOW A FIGHT ENDED, PER PARTY -- a tuple of `(person id, "felled" | "yielded" |
    # "prevailed" | "undecided")` pairs, read off the scene's lifted `wound_state` and `surrender` by the effect that
    # wrote the band (`loop/effects_combat.py::fight_ending`). Stamped on every success Event of
    # `fight`/`accept` at Felled/Wounded, and of `capture` at any band where an edge is opened (its
    # Untouched band runs the effect: a clean yield's `person.captured` carries it). Empty on every other
    # Event, which is nearly all of them.
    # THE ORDER is the `claimants` order, actor first -- the convention `PersonalCombatInput`'s `ends`,
    # `kits`, `scores` and `addends` follow -- a convention, NOT a role field.
    # ⚠ NO PRODUCTION READER EXISTS YET. The plan gives it as the band Event's payload (the
    # CP-T03-02 home: with the body Observation, it is what CP-T03-05 (mode b) and CP-T03-08 "get their
    # lawful input" from); until one of them reads it, only the tests and `World.content_hash` do.
    # ⚠ NOT AN `actor`/`target` FIELD UNDER ANOTHER NAME (S19.3): it names no doer and no recipient --
    # WHO did it stays a per-witness Claim. It records the OUTCOME the scene already decided, the same
    # class of fact `degree` is (the act's band), split by party because a fight has two.
    # [ASSUMPTION; medium; Jordan to correct; revert: the field and the Observation] -- the carrier is
    # a new Event field rather than a payload key, since an Event carries no payload; a carrier+hash
    # schema mover, folded by `World.content_hash` only where non-empty.
    # B05.18 (SC-P1, H-284). TWO SHAPES, BY PROVIDER: (1) a SCENE provider (personal combat) -- the per-party
    # endings above, `rosters.yaml: fight_endings`' words, `data/rosters.py::ENDING_*`; (2) a MARGIN provider
    # (the social contest) -- `((key, value), ...)` in `rosters.yaml: margin_endings`' order (`data/rosters.py::
    # MARGIN_ENDING`: pool, ob, net, margin, terms, levels, leverage), the roll that graded the act, built in
    # `loop/resolve.py::_fold` from what `seam/wrappers/sigma.py::resolve` returned, on every Event of the act
    # (the Failure band's too); a refusal carries none (no dice were dealt). No act is both.
    # B24p.20: AND (3) A PROCEEDING -- a tuple of tagged tuples (`rosters.yaml: proceeding_endings`): the sitting's head, its beats, the
    # whole `Sitting` and each verdict's band, written by `loop/resolve.py::_proceeding_ending` on every Event of the act (a refusal after
    # the sitting's too); read through `queries/world_q.py::ending_beats` and its siblings.
    # ⚠ A DEPARTURE FROM `04` §B.9, NAMED HERE: its `Event` record names `degree?` and no `ending`; the field already
    # ships for combat (H-266), and its use for a margin provider's tuple is a departure (`skills/layer-conformance`
    # B4, third disposition; C3-C16). Its readers: `harness/chronicle.py` and the GO surface's account. It carries
    # no actor, target or subject (`04` PART D row 9) and is no `Observation`, so no hearer learns the speaker's
    # pool from being in the room (D-U1-06; `test_sc01_provider.py::test_no_claim_predicate_is_a_margin_ending_after_witness`).
    ending: tuple = ()

    def __post_init__(self) -> None:
        if not self.causes:
            raise Forbidden(
                f"Event {self.kind} emitted with causes=[]", "S19.4",
                needs="causes: [ROOT] for an antecedent-free emission",
                law="S19.4 -- causes[] is REQUIRED AND NON-EMPTY; [ROOT] makes the empty list unrepresentable rather than merely discouraged",
            )


@dataclass
class Claim:
    """S20. Lives in the HOLDER'S OWN ledger.

    ⚠ `lap` IS THE ONLY CARRIER FIELD `U2` ADDS, AND THE ONLY ONE IT MAY ADD. The scene tick
    subdivides a season into laps, and §F1's Q2 asks for *a claim LANDING in the holder's ledger*
    — which was readable off `when` alone while a season was one pass, and is not once a season is
    several. `when` still says WHICH SEASON and is what eviction and decay read
    (`p.ledger.sort(key=lambda c: c.confidence * (c.when + 1))`); `lap` says WHICH LAP WITHIN
    it, so `questions_for(w, p, since=(tick, lap))` can ask *since I last deliberated* rather
    than *since last season*.
    ⚠ IT DEFAULTS TO `0` AND EVERY EXISTING CONSTRUCTION IS POSITIONAL, so a Claim built anywhere
    that predates the tick reads as lap 0 — which is exactly what a claim from the one-pass loop
    WAS. The generalisation is therefore exact at `R = 1`: `since == (tick - 1, 0)` selects the
    same claims `c.when == w.tick - 1` did.
    ⚠ AND NO OTHER CARRIER GETS ONE (`D-21`, and U2's falsifier (d)). The lap index is a DRIVER
    LOCAL — `SeasonDriver.lap` — because it is a fact about where the loop is, not about any
    thing in the world. A `lap` on `Act` or `Event` would make it world state and put a fourth
    clock in the model."""
    id: str
    holder: str
    subject: str
    predicate: str
    value: Any
    when: int
    source: str
    confidence: int
    # `visibility` -- `"own"`, or a CIRCLE: the tuple of ids the claim was confided among (v9 IN-18
    # `G6`, `H-197`). Only the told deposit writes a circle (`loop/witness.py`, `(teller, addressee)`
    # when `_circle_of`'s chance says the telling was private; never at the shipped control 0), and
    # the fold reads it (`loop/resolve.py::_confidence_broken`): a holder who tells a claim held under
    # a circle to someone outside it emits `confidence.broken`. It binds what a holder may RETELL,
    # never who hears (§10 decision 1). Every other deposit is `"own"`.
    visibility: str | tuple
    lap: int = 0
    # ⚠ `chain` -- WHO PASSED THIS CLAIM ON, ORIGIN FIRST, AS IT WAS PRESENTED (telling workplan `T3b`,
    # `ED-IN-0282`; closes `RULINGS.yaml` CAT-3, *"STORE THE TELLER... The edit is one argument, not a
    # lookup"*). `()` for every claim nobody told (firsthand, seen, inferred, content-deposit, and a
    # `told_by` deposit through a channel with no speaking actor); the told channel's deposit
    # (`loop/witness.py`) sets `said.chain + (act.actor,)`, so a retelling of a told claim is a longer
    # chain and the origin is `chain[0]`. What it is FOR is READ TIME: `decision/options.py::
    # teller_weight` weighs a claim by `told_weight ** hops` and the hearer's relation to the TELLER,
    # and `queries/person_q.py::LedgerReader` counts support over distinct ORIGINS. Nothing is
    # frozen at deposit: the chain records WHO told, and the grade is the reader's, so a revised
    # regard re-grades every claim a teller ever passed on. `chain` replaces the `teller` field
    # `teller` and `hops` are derived (below). KEYWORD-ONLY:
    # a stray string passed positionally would read as a chain of one-character hops.
    chain: tuple = field(default=(), kw_only=True)
    # `doer` (v9 IN-57, ED-IN-0294: Layer 1 amended by the user, `04` §B.9) -- the holder's own id
    # when the claim records HIS OWN act, else `None`. WITNESS stamps it only where the witness is
    # the actor (`loop/witness.py`, `pid == act.actor`) on the event-kind, `obs`, `seen` and content
    # deposits, never on a told copy: a person always knows his own act, so it leaks nothing a
    # channel withholds. Its one reader in game code is `queries/world_q.py::attention_key`, which
    # sorts the echo of his own deed last -- it is not news (`harness/soak.py` serialises it). Not
    # `person_q.deed_doer`, which infers the DOER OF ANOTHER'S deed from `seen.who`; this field is only
    # the holder's own id on his own act's deposits. KEYWORD-ONLY, default `None`: every other
    # construction (told copies, tests, fixtures) is untouched.
    doer: Optional[str] = field(default=None, kw_only=True)

    @property
    def teller(self) -> Optional[str]:
        """The LAST hop: the one who told THIS holder (`chain[-1]`), or `None` if nobody did. A
        derived reading, not a field -- a second stored teller beside `chain` would be two owners
        of one fact. Read-only; construct with `chain=`."""
        return self.chain[-1] if self.chain else None

    @property
    def hops(self) -> int:
        """How many tellings stand between the origin and this holder: `len(chain)`, `0` firsthand."""
        return len(self.chain)

    @property
    def firsthand(self) -> bool:
        """The holder's OWN observation: nobody told it (`not chain`) and it was deposited
        `firsthand`. A derived reading, not a field."""
        return not self.chain and self.source == "firsthand"


class Said(NamedTuple):
    """WHAT A TELLING PASSES ON, fixed at CHOOSE: the teller's own claim about the act's subject,
    copied out of their ledger by `queries/person_q.py::said_of` and carried on
    `Act.payload["said"]`, so WITNESS reads what the telling carried and never the teller's live
    ledger (the `F8` carve-out: a ledger is asked by its own holder, person-side).

    A NamedTuple, not a Claim: it has no id, holder, `when` or source, because it is not a belief
    anyone holds -- it is a thing said. `chain` is the chain of the claim the teller picked
    (`said_of` copies `Claim.chain`; `()` for a claim the teller holds firsthand), and the told
    deposit extends it by the teller. A confidence's circle is NOT carried here (see
    `Claim.visibility`).

    `pairing` (B11.22, `Fixtures.told_pairing`): the `epistemic.Seen` value the teller pairs with a deed of a `PAIRED_KINDS` kind he is
    passing on, as he holds it (`person_q.said_of`), or `None` -- the sighting of WHO did it, which the deed claim alone does not say. The told
    deposit (`loop/witness.py`) deposits it as a told `seen` claim beside the deed. A NamedTuple member cannot be keyword-only, so the
    default `None` is what leaves every construction as it was."""
    subject: str
    predicate: str
    value: Any
    confidence: int
    chain: tuple = ()
    pairing: Any = None



class Sensation:
    """S18.2 -- the bridge from world truth into `choose`; it carries ONE scalar, `standing`.

    It carries no `subsistence` (`H-73`): a need is a Query (`world_q.hunger` for a settlement)
    plus the shortfall claims a person holds about it. `sense()` computes `standing` via `standing_of`,
    and reading it on a Sensation built without it raises rather than answering 0. 04 §B.10 grades the
    Python one-scalar shape `convention`."""

    # roster-exempt: MECHANISM -- `__slots__` is a Python language construct naming this
    # class's own attributes, as on `View`.
    __slots__ = ("_standing",)

    def __init__(self, standing: Optional[int] = None):
        self._standing = standing

    @property
    def standing(self) -> int:
        """S18.2's scalar. COMPUTED; see `standing_of`. The direct route -- reading a value off every
        other person -- is barred by §20, "Claims live in the holder's own ledger... Nobody else may
        read or write it" (S22.4 clause 2 governs RESOLVER-SIDE Queries and `sense()` is explicitly not
        one)."""
        if self._standing is None:
            raise Unspecified(
                "Sensation.standing", "S18.2",
                needs="construct the Sensation through `sense()`, which computes `standing`",
                law="S18.2 -- a Sensation built without `standing` is half a Sensation, and "
                    "reading the missing scalar must refuse rather than answer 0 -- §42.2's "
                    "polarity rule applied to a constructor")
        return self._standing


class View:
    """S18.1 -- a View holds IDS, NEVER REFERENCES. L2 is enforced BY CONSTRUCTION: any attempt
    to reach a world collection through a View raises. S18: AT MOST K ids, BUILT NOT FILTERED."""

    # roster-exempt: MECHANISM. `__slots__` is a PYTHON LANGUAGE CONSTRUCT — it names this
    # class's own attributes and the interpreter reads it, so changing it changes how the code
    # works, never what the game is. The guard counts the tuple once, as one declared site
    # (`EXEMPT_CEILING` in `test_season_shape.py`).
    __slots__ = ("holder", "claim_ids", "question", "questions", "odds")

    def __init__(self, holder: str, claim_ids: list[str], k: int, question: Any = None,
                 questions: tuple = (), odds: Any = None):
        if len(claim_ids) > k:
            raise Forbidden(f"View built with {len(claim_ids)} ids against cap K={k}", "S18",
                            law="S18 -- at most K claim ids from the holder's OWN ledger")
        object.__setattr__(self, "holder", holder)
        object.__setattr__(self, "claim_ids", list(claim_ids))
        # ⚠ THE VIEW CARRIES ITS QUESTION. §F2 types `choose(p, view, sensation, ask_budget)` -- FOUR parameters --
        # and its body then reads `candidates = opening_set(p, view, q)`, where `q` IS FREE: the
        # pseudocode uses a variable its own signature does not bind. Widening `choose` to five
        # would break the signature §26 states, so the binding goes where §F1 already put it --
        # `assemble(person, question) -> View` builds the View FROM the question, so the View is
        # the thing that knows which question it was built for. No signature changes.
        object.__setattr__(self, "question", question)
        # CP-T02-07: THE SEPARATE QUESTIONS, in `attention_key` order (`questions_for` sorts them), beside
        # the one `question`. `question` is what `question_aggregation_rule` selected and, at `all` or
        # `one_per_source`, a MERGE -- the union of the referents under the first one's source (at
        # `one_per_source` the first question PER SOURCE) -- so it cannot name the throne apart from the
        # cause. This is the whole list. `auto` reads `question` and never this, so the shipped run is
        # unchanged; a callback may `assemble` a View on any one of these and ask `auto` for its proposal
        # there. It holds `Question` objects, as `question` does (carriers of ids, no World reference).
        # ⚠ THE STANDING-OCCASION STAMPS RIDE THE HEAD QUESTION ALONE (`world_q.questions_for`: vacancies,
        # heard-of OUGHTs, `Detainee`, ... are attached to `out[0]`), so a View built on a later question
        # carries no classed referents and the rows that form on a class (`confer`, `succeed`, `commit`,
        # `interrogate`) form nothing there.
        object.__setattr__(self, "questions", tuple(questions))
        # CR-17: THE PERSON'S BELIEVED-ODDS QUERY, `(act, bands) -> chance or None`, BOUND TO `holder`
        # (`seam/wrappers/sigma.py::believed_chance`, closed by `loop/deliberate.py` over the frozen
        # store). It is a QUERY the person asks, as `choose` asks `ask_budget`, not a store the View
        # holds: `choose` keeps its four parameters (`test_decision_package_never_names_world_anywhere_under_it`), the View keeps
        # ids and questions and one callable, and `decision/` still names no World. `None` -- a View
        # built by hand, a test, a seated person's callback -- is "he cannot say", and the chooser then
        # leaves the pursuit term as it was (`Fixtures.odds_weighting`, H-248).
        object.__setattr__(self, "odds", odds)

    def __getattr__(self, name: str) -> Any:
        raise Forbidden(
            f"choose() reached for world state '{name}' through its View", "S3-L2",
            needs="a person decides from their own claims; world truth enters only via sense()",
            law="L2 -- choose never receives a World. NOT BY DISCIPLINE -- BY TYPE",
        )


@dataclass(frozen=True)
class Question:
    """§F1's `q` -- the thing a person is deliberating ABOUT, and the input `opening_set` derives
    its subjects from. `H-04` / §61's `NoProducer` is closed by `questions_for()` below.

    `source` is one of `question_sources` in `rosters.yaml`. `referents` are the ids the question
    is ABOUT -- §F1 clause 3: "subject in referents(q)". `about` is the originating object's id,
    kept so a Candidate can say WHY it exists without the resolver re-deriving it.

    `classes` (IN-53, H-207, DECISION 2026-10-13 D1) are THE CLASSED REFERENTS: `((id, class),
    ...)`, a SECOND PARTITION beside `referents`, filled by `queries/world_q.py::questions_for`
    (which has the World; `_stamped`, the one stamp site): the vacant seats a person may fill
    (`vacancies`, IN-53) and the seats he has been told of (`seats_named`, v9 IN-10 (a)), as
    `Office`, the writs he holds (`writs_held`, v9 IN-09), as `Record`, and the places he has been
    told of and could settle in (`places_named`, v9 IN-45 `migrate`) and the larders his seat may
    requisition (`larders_in_purview`, v9 IN-49 `requisition`), as `Rung`; and, since v10 B10-05, the
    Records he holds that a holding row asks for (`records_held_for_holding_rows`, REM-25) as `Record`,
    the matters on the docket he saw opened are plain referents of the docket question
    (`docket_question`, CP-T05-04), and the question's OWN referents of every other class a row declares
    (`own_referents_of_class`, REM-21: `Site`, `Proposition`, `Person`, and `Record` since REM-2C, a writ
    excepted), each stamped with its collection's name. A verb row declaring
    `referent_class: C` forms ONLY on the ids carried here as `C`; a row declaring none forms ONLY on `referents` (`referents_for`, read
    by `VerbRow.referents_of`). Kept apart rather than spliced into `referents` so the partition is
    exact: an id may be BOTH a plain referent (a claim about the seat) and a classed one (the seat
    as a vacancy), and neither side's formations move the other's. It rides per referent, not on
    `source`, because `decision/questions.py::aggregate_questions` folds several questions under ONE
    source and unions the pairs. A Question is not in `World._STATE_COLLECTIONS` and is never
    hashed, so the field moves no `content_hash`; `()` carries none.

    `mandatory` (B10.71, A-47): the question a person may not pass over for another -- `questions_for` sorts it first, ahead of
    `attention_key`, and sets it only on the `need` question of an ambition whose `goal_stages` row says `opens: mandatory`
    while he stands on the row's last stage. It opens a scene and DECIDES NOTHING: which act he takes is the chooser's draw.
    Not hashed, as the rest of a Question is not."""
    id: str
    source: str
    referents: tuple
    about: str = ""
    classes: tuple = ()
    mandatory: bool = False

    def referents_for(self, cls: Optional[str]) -> tuple:
        """THE REFERENTS A ROW DECLARING `cls` FORMS ON: the plain `referents` for `None` (a row
        declaring no class), else the ids carried in `classes` as exactly `cls`, in their order."""
        if cls is None:
            return self.referents
        return tuple(r for r, c in self.classes if c == cls)

    def __post_init__(self) -> None:
        bad = [rc for rc in self.classes
               if not (isinstance(rc, tuple) and len(rc) == 2 and rc[1] in REFERENT_CLASSES)]
        if bad or len(set(self.classes)) != len(self.classes):
            raise Forbidden(
                f"question {self.id!r} carries a classed referent of no declared class, or one "
                f"twice: {bad or self.classes}", "IN-53",
                needs="`classes` pairs `(id, class)` once each, the class a "
                      "`rosters.yaml: referent_classes` value",
                law="a class is read by the verb rows that declare it; one no row may declare is "
                    "read by nothing and hides a stamping error")
        if self.source not in QUESTION_SOURCES:
            raise Forbidden(
                f"question source {self.source!r} is not in the question_sources roster",
                "§F1", needs="add it to rosters.yaml, or use one of the four",
                law="§F1 -- a question is produced by these sources and by nothing else. V2 said "
                    "THREE and was wrong by one; the roster is where a fifth would be argued for")


@dataclass
class Candidate:
    """S17 -- `opening_set` RETURNS Candidate[], NOT Act[].

    ⚠ `operands` IS THE STRUCTURAL HALF OF `H-94`, AND IT IS NOT A FIELD BOLTED ON. Without it
    `transfer`'s `stores(hearth(giver), kind) >= amount` has no `kind` and no `amount` that any part of
    the deliberation-to-resolution pipeline can carry, so the verb would be attempted and refused in
    every world. The row asked WHERE OPERANDS LIVE. They live here, on the Candidate,
    because the person is who derives them -- `hearth(giver)` is the giver's own Tenure and the
    referent is the person's own question -- and a channel anywhere further down (the Act, the
    Scene, the payload) would have to be filled by something that is not the person, which is L2.

    ⚠ AND THE FIELD IS NEVER PARTIAL. A form whose operands cannot all be bound forms NO
    Candidate (`operands_for` returns `None`), because an act minted with a hole is refused by the
    fold for a reason that is about the INSTRUMENT, and once `W-B` deposits observations that
    refusal becomes a FALSE BELIEF held by everyone who witnessed it.

    ⚠ THERE IS NO `why` (S17 typed one). Nothing read it, and the question that occasioned an act is
    recovered from `Scene.occasion` (`epistemic._term_why`'s docstring). `04` licenses a reader or a
    removal, never a hole row -- a field nothing reads is the dead carrier `ID-13` refuses."""
    verb: str
    subject: Optional[str] = None
    operands: dict = field(default_factory=dict)


@dataclass
class Scene:
    """THE BUDGETED UNIT. Ruled by Jordan, 2026-09-02: *"5 scenes for a character to play per
    season"*.

    ⚠ IT IS A LEVEL ABOVE THE VERB TABLE AND CHANGES NOTHING BENEATH IT. Parts D and E stand
    unaltered: the table's rows are the INTERACTIONS, and a Scene carries 1-3 of them. `PLAN.md`
    `W17` says so and it is worth restating -- this is the cheapest shape the ruling could have
    taken, and nothing about the write matrix or the resolver moves.

    #353 §26.3's prose counts ACTS throughout. Re-stated in scenes, its argument is unaltered:
    "a wounded duke gets fewer SCENES than a healthy one", and five scenes each spent petitioning
    is exactly the triage the budget exists to create. The noun changes; the spray argument does
    not.

    A scene filling more than one interaction slot (`slots`) costs more than one scene action
    (`H-77`, swept). Both that cost and the interactions bound are FIXTURES and register rows --
    Jordan ruled the UNIT and the NUMBER and ruled neither of these.

    ⚠ LAYER 1 DEPARTURE, NAMED HERE (B4's third disposition; C3-C16): `04` §B.9's `Scene` record is `(id, person, occasion, place,
    interactions)` and has no `decided`. `decided` is not in it and `04` is not edited. Its one reader is `harness/chronicle.py`
    (ID-13: `lines`' per-act line). THE DECIDING TERM: the term of the score, or the draw, that put the Scene's FIRST act on top
    of the candidates still unspent when it was taken -- `choose.deciding_term`'s label for it (`pursuit`, `stance`, `fit`, a `+`
    of them, `draw`, `tiebreak`, `sole` or `overdetermined`). `decision/` stamps it (`choose.pack_scenes`); the Scene is its own
    return value, so this is no write, and nothing is hashed from it. `""` is a Scene packed from a list no chooser ranked (a
    hand-built one, or a player's pick), where no deliberation said what decided it.

    A SECOND DEPARTURE, NAMED THE SAME WAY (B10.24; B4's third disposition; `04` not edited): `forgone`, `((verb, subject, margin), ...)`,
    the candidates his scruple (`decision/options.py::scruple`) struck that he ranked above what he did -- the struck candidates whose
    score exceeded the one that leads this Scene -- and, once a strike can be a draw, the candidates it left standing at a positive
    margin that this Scene carries. It is the chooser's record of what was given up, NOT a belief the person holds about himself.
    `choose.pack_scenes` stamps it from the ranker; its one reader is the fold (`loop/resolve.py::_scruple_overridden`), which
    emits `scruple.overridden` where the act's own `(verb, subject)` stands in it at a positive margin. `()` is a Scene whose
    deliberation struck nothing (the gate unarmed, the shipped control) or that no chooser ranked."""
    id: str
    actor: str
    acts: list = field(default_factory=list)
    # ⚠ `occasion` IS THE QUESTION THE SCENE IS ABOUT, and it is the field that binds DELIBERATE
    # into the causal graph: without it an act never cites what made it, so `causes[]` cannot walk from one
    # person's act back to another's.
    # The meta-architecture types it here rather than on the Act: `Scene := (id, person,
    # occasion : Question, place : RungId, interactions : Act[])`, because the occasion is what
    # the person is spending the scene ON and the interactions are what they do in it.
    # ⚠ `place` IS DELIBERATELY NOT ADDED. `ID-13` — a declared field must reach a reader — and
    # nothing here reads a scene's place; `place_of(w, event)` already answers that question from
    # the Event. Adding it to match a type signature would be the defect the idiom names.
    occasion: Optional["Question"] = None
    decided: str = ""      # the deciding term of the Scene's first act; the docstring names it (a Layer 1 departure)
    forgone: tuple = ()    # `((verb, subject, margin), ...)`: what his scruple struck that he ranked above his lead act; the docstring names it

    # roster-exempt: MECHANISM. `PLAIN_COST` is the DEFINITION OF THE UNIT -- one ordinary scene
    # is one scene action -- not a tunable value. `H-77` tunes what an EXTENDED scene costs
    # relative to it, and a "cost" whose base was itself variable would make the budget's units
    # undefined. Named rather than inlined because §42.2.1's rule is that no bare literal sits in
    # a body, and because naming it is what makes the distinction from `extended_cost` visible.
    PLAIN_COST = 1

    @property
    def slots(self) -> int:
        """THE INTERACTION SLOTS THIS SCENE FILLS: `sum(1 + effort_of(a))` over its acts (CP-T01-05). An act
        at effort `e` fills `1 + e` of the scene's `interactions_per_scene`, so effort's whole cost is the acts
        the person does not take in that scene. With no act carrying effort (the shipped chooser) this is
        `len(self.acts)`. DERIVED FROM THE ACTS EVERY TIME, never stored: a filter that rewrites `acts` (`loop/
        deliberate.py::_drop_what_was_already_done`) cannot leave it stale."""
        return sum(1 + effort_of(a) for a in self.acts)

    def cost(self, extended_cost: int) -> int:
        """Scene actions this scene spends: `extended_cost` when it fills more than one slot, else
        `PLAIN_COST`. PRICED FROM THE SLOTS (CP-T01-05), not from a flag a caller sets: a scene's price is
        what it carries, so a play-surface callback returning one effort-2 act pays for three slots."""
        return extended_cost if self.slots > 1 else self.PLAIN_COST


EFFORT = "effort"       # the payload key (`Candidate.operands` -> `Act.payload`) `effort_of` reads and `decision/choose.py` forms


def effort_of(act: "Act") -> int:
    """The `effort` an act carries in its payload: a whole number of extra scene slots, `0` when it carries
    none (CP-T01-05). The one reader of the field -- `Scene.slots` counts it and `loop/resolve.py` hands it
    to the roll. A payload that is not a mapping, or has no `effort`, carries none. A negative or non-whole
    effort is REFUSED: it would shrink a scene below its acts, and an engine that quietly clamped it would
    be deciding for the caller. The upper bound is not here: it is the scene's own, `interactions_per_scene`
    (an act at effort `e` needs `1 + e` of them), checked in DELIBERATE."""
    payload = act.payload if isinstance(act.payload, dict) else {}
    e = payload.get(EFFORT)
    if e is None:
        return 0
    if isinstance(e, bool) or not isinstance(e, int) or e < 0:
        raise Forbidden(f"act {act.id!r} carries effort {e!r}", "CP-T01-05",
                        needs="`effort` a non-negative whole number of extra scene slots",
                        law="an act at effort e fills 1 + e interaction slots; a negative or fractional "
                            "effort would fill fewer slots than the act itself")
    return e


@dataclass
class Act:
    id: str
    actor: str
    verb: str
    changes: list[StateChange] = field(default_factory=list)
    reads: list[str] = field(default_factory=list)
    contests: list[str] = field(default_factory=list)
    payload: Any = None
    # S27's five strata. 4 == "social", the stratum most acts in this corpus belong to; the
    # value is declared rather than silent, and A37 exercises the ordering.
    # ⚠ THIS DEFAULT IS ALSO THE SENTINEL, AND THE TWO JOBS CONTRADICT EACH OTHER. `stratum_of`
    # decides "did the caller declare a stratum?" by comparing against THIS VALUE
    # (`a.stratum != Act.__dataclass_fields__["stratum"].default`), so an act that deliberately
    # declares `stratum=4` is indistinguishable from one that declared nothing and is routed to
    # the verb table instead -- against `stratum_of`'s own promise that "a caller that sets it
    # explicitly is taken at its word". 19 of the 32 verb-table rows carry a stratum
    # other than `social`, so a declared 4 would be silently overridden on those verbs.
    # LATENT, NOT LIVE, and only by coincidence: the sole explicit call site (`probes.py`) is
    # verb `speak`, whose row is `social` -- so the override lands on the same
    # value and the A37 arm cannot tell "set" from "unset".
    # [JUSTIFIED: an INDEX into the `strata` roster (#353 §27), inherited -- `social` is index 4 and `stratum_of` returns `STRATA.index(row.stratum)`. NOT `[canonical:]`: this 4 is also the "caller declared nothing" sentinel `stratum_of` tests against, so it is a fitted default doing two jobs, not a ratified value -- see the ⚠ below]
    stratum: int = 4
    # ⚠ WHICH SCENE THIS INTERACTION BELONGS TO. The meta-architecture's `Act` carries `scene`,
    # and it is what lets the fold ask what occasioned an act without the Act itself carrying a
    # Question — the Scene owns the occasion, the Act names its Scene. Stamped by the driver as
    # it flattens scenes into the produced list, so a caller that returns bare Acts (the
    # pre-`W17` accounting, still lawful under `as_scenes`) simply has none.
    scene: Optional[str] = None
    # THE SEAT EXERCISED. `04 §B.9`: `Act := (id, actor : PersonId, via : SeatId?, ...)`, and
    # `04:120` (AX-1): *"only a person acts ... a seat enters through `Act.via`"*. An office id, or
    # `None` for a person acting as themselves. It is what `_eligible`'s `remit:` branch, `_req_revoke`,
    # `_req_confer`, `_req_establish` and the write gate's F3 clause (T-o and the conferral basis)
    # ask -- never the actor's other seats -- so a Duke who is also a Chancellor acts as ONE of them
    # per act. Set person-side at the mint (`decision/choose.py::pack_scenes`), from the same grant
    # `person_side_eligible` admitted on; the gate refuses a `via` the actor does not occupy.
    via: Optional[str] = None
    # B08.02 (`16_PESSIMIST_CORE_a_scene_runs_in_its_own_order.md` edit 2; ruling A-9: a scene is a short sequence): THE
    # BANDS OF THE SCENE'S PREVIOUS INTERACTION AT WHICH THIS ONE IS ATTEMPTED -- band labels, the strings the verb table
    # keys degrees by (`writes:`/`emits:` maps; `DEGREE_LABEL`'s values for a four-band row). `None`: always, as before.
    # Read by the fold only (`loop/resolve.py::_sequence_refusal`, ID-13): outside the named bands the interaction is
    # refused at the clause `sequence` (`data/verbs.py::SEQUENCE_CLAUSE`). Not in `World.content_hash` (the act store is not hashed).
    after: Optional[tuple] = None

    def __post_init__(self) -> None:
        # `04` §B.9 `via : SeatId?`, §B.1: the seat exercised is a TYPED seat id -- the same string,
        # tagged (`state/ids.py::SeatId`), so `content_hash` folds what it always folded. `None` (the
        # person acting as themselves) stays `None`. The converse -- a `SeatId` as `actor` -- is refused
        # in the fold (`loop/resolve.py::_survives`), not here: AX-1's refusal belongs where the act is
        # folded, and a hand-built Act carrying one must reach that refusal to be observed.
        if self.via is not None:
            self.via = SeatId(self.via)
        # `after` is a tuple of band labels or `None`: a bare string would be read as its letters, and a list would let a
        # holder of the act re-point what it hangs on after the chooser composed it.
        if self.after is not None and not (isinstance(self.after, tuple) and all(isinstance(b, str) for b in self.after)):
            raise Forbidden(f"act {self.id!r} carries after={self.after!r}", "B08.02",
                            needs="`after` a tuple of band labels, or None",
                            law="an interaction hangs on the bands of the one before it, named as the verb table names them")


# S27: FIVE STRATA. movement / binding decisions / contested physical / uncontested material / social


def generated_attributes(world_seed: int, pid: str, span: Any) -> dict:
    """AN ATTRIBUTE VALUE DRAWN FOR A PERSON NOBODY AUTHORED (B01a.01; Jordan, 2026-11-13/14: every person's attributes
    drawn, so every later pin and calibration records against a varied world). THE ONE OWNER of what a person holds on
    an attribute no cast row authors: it fills `Person.attributes`, and lane A's flat seating at `pool_default`
    (B01) is gone.

    (1) WHAT IS DRAWN. All ten of `engine/substrate/descriptors.py::ATTRIBUTES` (B01a.06: Spirit is its own group, `attr.spirit.will`), each uniform on the whole numbers `lo`
    to `hi` of `span` -- `Fixtures generated_attribute_range`, shipped `(1, 6)`, inside the attribute scale
    (`ATTRIBUTE_FLOOR` to `ATTRIBUTE_CEILING`). `span` None returns `{}` (nothing generated: the world before B01, a
    fighter reads its class defaults and a roll reads `pool_default`); two whole numbers `lo <= hi` inside the scale
    are the range; anything else is `Forbidden`, naming the setting and H-856.
    (2) THE KEY. One keyed draw per (person, attribute) through `state/ids.py::draw_factory`, `lambda: 0` as the clock,
    purpose `attr.generated:<key>`, one `die(lo, hi)` taken from each stream: a sheet is a function of (seed,
    person id, attribute) alone, whenever and wherever the person is minted. No wall clock, no `random.Random(` here.
    (3) AUTHORED OVERRIDES. The caller lays an authored value over this dict key by key (`{**generated, **authored}`),
    so an authored key replaces its own draw and no other: all ten draws are taken whatever a person authors.
    (6) PROVISIONAL. [ASSUMPTION; medium; Jordan to correct] -- replaced by BA1's authored cast and the later
    generator; H-856 is graded `assumption` and swept `(1, 6)` SHIPPED / `(2, 2)` B01's flat seating, the control /
    `None` nothing generated. A sweep applied AFTER the build does not reach a seated sheet."""
    if span is None:
        return {}
    ok = (isinstance(span, (tuple, list)) and len(span) == 2
          and all(type(v) is int for v in span)
          and ATTRIBUTE_FLOOR <= span[0] <= span[1] <= ATTRIBUTE_CEILING)
    if not ok:
        raise Forbidden(
            f"`Fixtures generated_attribute_range` is {span!r}: it must be two whole numbers lo <= hi inside the attribute "
            f"scale {ATTRIBUTE_FLOOR}..{ATTRIBUTE_CEILING}, or None",
            "engine/season/hole_register.yaml H-856",
            needs="(lo, hi) whole numbers, ATTRIBUTE_FLOOR <= lo <= hi <= ATTRIBUTE_CEILING; None generates nothing",
            law="B01a.01 -- one keyed draw per person and attribute, uniform on the declared range")
    lo, hi = span
    draw = draw_factory(world_seed, lambda: 0)
    return {key: draw(pid, f"attr.generated:{key}").die(lo, hi) for key in ATTRIBUTES}


def in_custody(tenures) -> bool:
    """Does a person own a live `detain`, given his own Tenures (a `Person`'s or a `PersonInterior`'s)? (B21.11, A-23: custody suspends a holder's
    every seat.) The one reading, asked by `state/gate.py::_seat_grants` and `may_admit` and by `decision/options.py::seat_of`
    (a `decision/` reader holds no `World`)."""
    return any(t.kind == DETAIN_KIND and t.live for t in tenures)


@dataclass
class Person:
    """S9. A COHORT IS A PERSON AT weight > 1. ONE CLASS (S9.1)."""
    id: str
    name: str = ""
    weight: int = 1
    capability: dict = field(default_factory=dict)
    stance: list[tuple] = field(default_factory=list)
    pursuits: dict = field(default_factory=dict)
    # A belief is a `commit` to an OUGHT, not a field (`04:179` / `04:980`, PART D row 44): `Person`
    # carries no `beliefs`.
    ledger: list[Claim] = field(default_factory=list)
    # Part D carries `(Person, body)` and `(Person, travel_leg)`; a row naming a field the class lacks is
    # the `(Record, held_by)` defect (see `matrix_rows_without_a_field`). `budget` reads both, person-side, which is PLAN §3.3's
    # smaller amendment: a Person owns every Tenure whose subject they are, so office-holding,
    # body and travel are all the person's own state and `sense()` keeps §18.2's "the ONE".
    # `condition_scale`, not a literal 1000: a person at full body is at the top of the same
    # fixed-point scale `Site.condition` uses, which is what `H-38` closing on "`Site.condition`
    # is the model" MEANS. A bare 1000 here would be a second, silent copy of that scale — the
    # defect `G1` names — and it would drift the moment the fixture moved.
    body: int = field(default_factory=lambda: DEFAULT_FIXTURES.get("condition_scale"))
    # v11 CP-T03-07 (P32): THE BODY'S CEILING -- what a recovery heals toward, as `Site.condition` has
    # one. Built at `condition_scale`, so an unmarked person heals whole. WRITTEN only by the fight
    # (`loop/effects_combat.py::_eff_kill`, through `marked_ceiling`; `write_matrix.yaml` row
    # `(Person, body_ceiling)`); READ by every raiser of `body` (`_eff_tend` today), which heals to it
    # and never to `condition_scale` -- `engine/season/tests/test_cp_t03_07_body_ceiling.py` fails on a
    # new bare `body` write that does not say how it stands to this field (CLAUDE.md §0.1 pt 1).
    body_ceiling: int = field(default_factory=lambda: DEFAULT_FIXTURES.get("condition_scale"))
    # v9 IN-34 FORCE-BODIES: THE BIRTH TICK, the one field the bodies clock adds, and its ONLY READER
    # is `queries/world_q.py::age_of` -> `body_hazard` (ID-13: no field without a reader). Age is NOT
    # stored; it is `w.tick - born`, a Query over the clock (IN-21's `season_of_year` precedent), so
    # nothing writes to age anyone. Default `-age_at_build`, the fixture: no source authors a person's
    # age (`references/npc_registry.yaml`: `age: null [GAP]` on most rows, no key on the rest), and a
    # literal here would be a second, silent copy of a number Jordan sets. `loop/census.py::_individuate`
    # passes its own (a person minted at tick t is `age_at_build` old at t, not at 0).
    born: int = field(default_factory=lambda: -DEFAULT_FIXTURES.get("age_at_build"))
    # ⚠ `scar` IS `{element: count}` -- IN-08 H3, `ED-IN-0261`'s scar model (*"counted PER
    # ELEMENT ... the unit is a COUNT, thresholds 1/2/3"*). An element is a PURSUIT name (the
    # fifteen of `references/descriptor_registry.yaml`'s `pursuit_roster`) or, since IN-08 H11, an
    # AFFILIATION name (`affiliation_roster`, the keys of `conviction` below; the two rosters are
    # refused a shared name). One count per act this person OBSERVED that violated that element,
    # written at RESOLVE by the act (`loop/resolve.py::_scar_witnesses`), never at WITNESS (S9.3).
    # Keys are never literals here and the dict is never
    # pre-seeded: a pursuit nobody has been scarred on is absent, not 0, so an unscarred person's
    # `repr` is unchanged. READERS: `person_q.crisis_weights` (threshold 2, H9), `conviction_after_crisis` (3, H13).
    scar: dict = field(default_factory=dict)
    # IN-08 H10 -- `conviction` IS `{affiliation: intensity}` (ED-IN-0251 R1/R2): which religious
    # affiliations this person holds, each an int on `affiliation_roster.scale` (0-5; 5 is full
    # intensity), validated by `data/affiliations.py::conviction_map` -- not the pursuit `doctrine`,
    # which is the magnitude of religious concern, not its side. A key's ABSENCE is not held; a stored 0 is a held rejection (v9 IN-63). Filled at
    # world build from the cast's authored `affiliations:` (`data/cast.py::conviction_of`); its
    # `write_matrix.yaml` row admits a RESOLVE/ENCOUNTER write, made only by the crisis at scar
    # threshold 3 (`loop/resolve.py::_conviction_crisis`, IN-08 H13). Confliction is DERIVED
    # from it (`queries/person_q.py::confliction`), never stored here.
    conviction: dict = field(default_factory=dict)
    # v9 PC-06 K-3 (`H-85`): THREAD SENSITIVITY, the design's one class-shaped gate (#353 §9.2), as a
    # per-person whole number. Filled ONCE at world build from the cast's authored `ts:` key
    # (`data/cast.py::thread_sensitivity_of`, `conviction_of`'s precedent) and NEVER WRITTEN IN PLAY,
    # `born`'s precedent: it has no `write_matrix.yaml` row, so the gate refuses any write to it.
    # `None` IS "NO AUTHORED VALUE", NOT 0: most cast rows carry `ts: null # [GAP]` and every corpus
    # person carries no row at all, and a `None` reads UNKNOWN to the gate, which refuses -- so a
    # person nobody screened cannot attempt, rather than reading 0 and passing a gate swept to 0. Its
    # ONE READER is `queries/person_q.py::OwnStateReader` (the `thread_sensitivity` stem of
    # `data/requires.py`), which both the fold's `WorldReader` and the person's own decline ask.
    thread_sensitivity: Optional[int] = None
    # v10 CR-20 (M2): THE ATTRIBUTE CARRIER -- `{registry key: whole number 1-7}` over Jordan's ten
    # (`references/descriptor_registry.yaml: attributes`, ED-IN-0328; `engine/substrate/descriptors.py::
    # ATTRIBUTES`). A person's INPUT is `faculty`, derived at read; these are what it reads. Filled ONCE, at world
    # build (`boot/realm.py::build_realm`) and at an in-play mint (`loop/census.py::_individuate`), by
    # `generated_attributes` (above) under any value a cast row's `stats:` authors (`data/cast.py::attributes_of`,
    # key by key), and NEVER WRITTEN IN PLAY: no `write_matrix.yaml` row, so the gate refuses any write to it. A key
    # nobody holds is missing, never the registry's `default` and never 0 -- the pool then falls to `pool_default`
    # (`seam/wrappers/sigma.py::faculty`): that is `boot/realm.py::build_realm(cast_attributes=False)`, or `Fixtures
    # generated_attribute_range` None. `decision/sheet.py`'s creation sheet only READS it. READERS:
    # `seam/wrappers/sigma.py::faculty` (the pool's base) and `_opposition_of` (the score the obstacle halves), and
    # (PC-06 K-1) `seam/wrappers/combat.py::combat_input`/`party_end`, which pass them to the fight on `PersonalCombatInput.attributes`.
    attributes: dict = field(default_factory=dict)
    # v10 CR-30: HERITAGE -- DESCENT, one of `references/descriptor_registry.yaml: heritage_roster`'s five
    # (`engine/substrate/descriptors.py::HERITAGES`), as a read-off field (`architecture/meta/01_AXIOMS.md`
    # §D.1.1): the one member of the dropped `marks[]` no Tenure derives. `None` IS "UNAUTHORED", never a
    # default member. Filled ONCE at world build from a cast row's `heritage:` (`data/cast.py::heritage_of`) and
    # NEVER WRITTEN IN PLAY, `thread_sensitivity`'s precedent: no `write_matrix.yaml` row, so the gate refuses a
    # write. ONE READER: `epistemic.py::_term_marks`, which deposits it TRUE and verbatim to every co-located
    # witness beside `who` (AX-7: no competence or prior-belief mediation).
    heritage: Optional[str] = None
    # B04.07 (A-107): TRAITS -- what this person is MOVED BY, the members of `descriptors.TRAITS` he holds, each held or
    # not and never giving dice. Filled ONCE at world build from a cast row's `resonant_style:`
    # (`data/cast.py::traits_of`; `frozenset()` where unauthored), held APART from `capability` (the skill map holds
    # skills only), and written at build only (`write_matrix.yaml`'s `Person.traits` row has no step). No reader reads it
    # yet: the `edge` reader that will (U1-B step 4) reads 1 if the subject holds the trait, else 0.
    traits: frozenset = frozenset()
    # B10.58 (A-108): A PERSON'S OWN MANNER OFFSET -- `{axis: float}` over `rosters.yaml: manner_offset_axes`, how far his way of going about things sits from what
    # his pursuits alone would make it, on that axis (each within `+-Fixtures.manner_offset_bound`). Filled ONCE at world build from a cast row's `manner:`
    # (`data/cast.py::manner_offset_of`), written at build only (`write_matrix.yaml`'s `Person.manner_offset` row has no step), and EMPTY where unauthored: an axis nobody
    # holds is absent, never 0.0. ONE READER: `queries/person_q.py::projected_axes` adds it to the projected axis; the refusal gate asks for the projection without it.
    manner_offset: Mapping[str, float] = field(default_factory=dict)
    travel_leg: list[str] = field(default_factory=list)
    # ⚠ THE TENURE STORE IS HERE, as `Tenure`'s OWN DOCSTRING says: "S15 -- THE ONE EDGE. Owned by its
    # SUBJECT (S15.1)." `budget : (Person, View) -> int` reads "own `hold` Tenures" WITH NO WORLD
    # (#353 `:877`, `:912-913`; `H-28`), which a flat world list would make UNSATISFIABLE and would make
    # `budget` a SECOND non-decision function taking a `World` -- breaking `:634`'s "the ONE
    # non-decision function permitted a World". PLAN §3.3 takes the smaller amendment: #353 `:730` gives
    # Person "every Tenure whose subject they are". `World.tenures` is a READ-ONLY VIEW over these; see
    # `_TenureView`.
    tenures: list = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.weight < 1:
            raise Forbidden("Person.weight < 1", "S9", law="S9 -- weight >= 1, default 1")

    @property
    def is_cohort(self) -> bool:
        """S9's own sentence as a predicate: *"A COHORT IS A PERSON AT weight > 1"*. One owner for
        the test, because `ED-IN-0255` makes it decide something: the larder
        draw feeds cohorts and exempts the individual (`queries/world_q.py::subsistence_draw`).
        A PROPERTY, NOT A FIELD: it is read off `weight` every time, so it can never disagree with
        the field it is about, and it is not state (`matrix_rows_without_a_field` reads fields,
        and no write-matrix row names it)."""
        return self.weight > 1


@dataclass(frozen=True, eq=False)
class PersonInterior:
    """WHAT `choose` IS HANDED OF A PERSON: `04` §B.2 row 2 *"a frozen copy with no store handle"*, §C.3 *"In: a
    frozen `PersonInterior`"*. A person interior is what is inside the person, copied out at the barrier: no
    assignment to the interior's own fields, and no item assignment into its mappings, reaches the `Person`.
    That is NOT "nothing the interior holds can change the store": `ledger` and `tenures` share the
    LIVE carriers (below; a stance row is a tuple, so `stance` is not a route), so an assignment THROUGH one of them (`interior.tenures[0].until = ...`) lands on the store.

    THE FIELDS ARE THE ONES `decision/` READS, derived by an `ast` walk of attribute reads on the person
    parameter there (and in the `queries/person_q.py` and `epistemic.py` callees it hands the whole person to), plus
    `loop/deliberate.py`'s own `p.id`; the walk found no write to any of them. Mappings are `MappingProxyType`
    over a copy, sequences are tuples. `ledger` and `tenures` hold the carrier objects themselves
    (`Claim`, `Tenure`), not copies of them: a `Tenure` counts its own assignments
    (`_v`, `World._tenure_changes`), so a copy would be a different object to the diff. The reader a
    caller wants over the ledger is `queries/person_q.py::LedgerReader(interior.ledger)` -- built there, because
    this module may not import `queries/`.

    `eq=False`: identity equality, so an interior with mappings in it is hashable. Not stored anywhere."""
    id: str
    name: str
    capability: Mapping
    pursuits: Mapping
    conviction: Mapping
    scar: Mapping
    attributes: Mapping
    manner_offset: Mapping
    body: int
    thread_sensitivity: Optional[int]
    stance: tuple
    travel_leg: tuple
    tenures: tuple
    ledger: tuple
    weight: int = 1       # S9: a cohort is a Person at weight > 1; a chooser's callback may ask (harness/probes.py P21)
    heritage: Optional[str] = None   # B04.13: read by `decision/sheet.py`'s development sheet, as `thread_sensitivity` is.
    # 04 §B.2 calls `heritage?` a read-off field whose resolver is WITNESS's `marks` term, and §A.2 / §B.2 make this
    # record the person's own state; the two rows meet here. The pick: admitted, as his OWN field -- §B.2 excludes only
    # "anything about another person", and another person's heritage is still read only through a held claim.
    # B09.01 -- THE TICK HIS CLAIMS ARE READ AT, AND THE RATE THEY FADE AT. A claim's stored `confidence` is what it
    # was deposited at and nothing rewrites it (`state/ledgers.py::present_confidence`), so a reader of the person's
    # ledger needs both, and `decision/` may not ask the World for either. Not person state: the barrier's own tick and
    # `Fixtures.claim_decay()`, copied in by `interior_of`. `fade_of` reads them; a hand-built `Person` carries neither.
    tick: int = 0
    claim_decay: int = 0

    @property
    def is_cohort(self) -> bool:
        """`Person.is_cohort`, the one owner of the test (B10.59: `OwnStateReader` asks it of the person forming, who is an
        interior here). A property reading `weight`, so it is no field and no second copy of the predicate."""
        return Person.is_cohort.fget(self)


def frozen(d) -> Mapping:
    """A read-only copy of a mapping (`None` reads as empty): what a handed-down record holds in place of the store's dict."""
    return MappingProxyType(dict(d or {}))


def interior_of(p: Person, tick: int, claim_decay: int) -> PersonInterior:
    """THE ONE BUILDER of a `PersonInterior`: copy the fields `decision/` reads out of `p`, mappings read-only, and the
    `tick` and `claim_decay` his claims are read at (B09.01)."""
    return PersonInterior(
        p.id, p.name, frozen(p.capability), frozen(p.pursuits), frozen(p.conviction), frozen(p.scar),
        frozen(p.attributes), frozen(p.manner_offset),
        p.body, p.thread_sensitivity, tuple(p.stance), tuple(p.travel_leg), tuple(p.tenures), tuple(p.ledger),
        p.weight, p.heritage, tick, claim_decay)


def fade_of(p) -> tuple:
    """`(tick, claim_decay)`, the pair a person's held claims are read at (`state/ledgers.py::present_confidence`): an
    interior's own (`interior_of`), and `(0, 0)` for a stored `Person` a test or a probe built by hand, whose claims then
    read as deposited. The one place `decision/` asks, so no site spells the fallback."""
    return getattr(p, "tick", 0), getattr(p, "claim_decay", 0)


@dataclass
class Site:
    """S12. `condition` is PRIMARY STATE, a FIXED-POINT INT (S48), and it GATES VERBS (S12.1)."""
    id: str
    rung: str
    kind: str
    condition: int


@dataclass
class Record:
    """S13 -- a LIVE CARRIER. S30.1: it has NO Partition row, so every Record write is an
    unmarked cell -- which this instrument reports rather than papering over.

    ⚠ PETITIONS AND DISPENSATIONS ARE KINDS OF THIS CLASS, NOT CLASSES OF THEIR OWN
    (`04_CODE_ARCHITECTURE.md` §B.5's synthesis call, PART A row 11), so `forge`, `destroy_record`,
    `hold` and `carry` reach them, and a `hold` on a dispensation has something to point at.
    `kind` is a `record_kinds` member and `subject_matter` is that kind's EXACT key set; both
    are refused at construction (`__post_init__`, below)."""
    id: str
    rung: str
    kind: str
    forgery_quality: int = 0
    subject_matter: Any = None
    stages: list[tuple] = field(default_factory=list)
    # ⚠⚠ **RULED BY JORDAN, 2026-09-10: "add `Record.matured`, write it at MATTER".** Of three
    # costed options — add the field and write it; make the Event carry no change; move maturation
    # to RESOLVE as act-declared — he took the first, on the grounds that THE MATRIX ROW IS THE
    # GAME and the field should exist. `write_matrix.yaml`'s `(Record, matured)` row has named this
    # field since it was written: `steps: [MAT]`, `class: MATTER`, `emits: term.matured`,
    # `by: "D7 — MATTER matures a term the act declared; causes[] names that act"`.
    # ⚠ `(Record, stages)` is `steps: [RES]`, `class: ACTS`, *"terms are act-declared, never
    # MATTER-advanced"*: a MATTER-step Event claiming a change to it would name the one field the
    # matrix forbids MATTER to touch, and report a change nothing wrote (`ID-9`). So MATTER writes
    # `matured`.
    matured: bool = False

    def __post_init__(self) -> None:
        """⊕L35 (r2 `05_LEDGER_AND_BUILD.md:671`): A RECORD WHOSE `subject_matter` KEYS ARE NOT ITS
        KIND'S IS REFUSED, AND SO IS A KIND THE ROSTER DOES NOT LIST.

        ⚠ THE REFUSAL SHAPE IS `Rung`'s, COPIED RATHER THAN RE-INVENTED. `Rung.__init__` refuses an
        unrostered kind and `Rung.__setattr__` refuses an undeclared field, each as `Forbidden`
        naming the field, the section, what is needed and the law inline. The same two refusals
        here, on the same terms: `kind` is a member of `record_kinds` or nothing, and the content's
        keys are the kind's declared keys or nothing.

        ⚠ `__post_init__` AND NOT `__setattr__`, AND THE DIFFERENCE IS DELIBERATE. `Rung` is a plain
        class guarding a whitelist on every write; `Record` is a dataclass every mint constructs by
        keyword. Its `subject_matter` is written once, inside `(Record, exists)`'s gate (r2 `02` §A.4: *verbatim or
        not at all*), and again only for the `army` kind (ED-IN-0306 phase 2: `(Record, subject_matter)`, whose
        writers are the four army verbs, each validating what it writes). So construction is the one write
        there is to refuse for every other kind, and `Office`'s roster checks sit at the same place for the same
        reason.

        ⚠ BOTH DIRECTIONS, because a missing key and an extra key are the same defect from two
        sides: a missing one is an operand no reader can bind, an extra one is a second vocabulary.
        `None` has no keys, which is why every `text` Record minted before this check stays lawful
        and nothing already in a world is re-read by it."""
        want = RECORD_KIND_KEYS.get(self.kind)
        if want is None:
            raise Forbidden(
                f"Record.kind {self.kind!r} -- not a member of `record_kinds`", "ARCH §B.5",
                needs=f"one of {sorted(RECORD_KINDS)}, or a new row in rosters.yaml: record_kinds",
                law="ARCH §B.5 -- Petition and Dispensation are KINDS of Record, and a kind is a "
                    "roster member: a free string would mint a document no key list describes")
        sm = self.subject_matter
        if sm is not None and not isinstance(sm, dict):
            raise Forbidden(
                f"Record {self.id!r} carries subject_matter of type {type(sm).__name__}",
                "⊕L35", needs=f"a mapping over exactly {list(want)}, or None for a kind with none",
                law="r2 02 §A.5 -- `subject_matter: Any` is a schema hole unless its keys are the "
                    "kind's; a value with no keys cannot be checked against them")
        have = set(sm or ())
        if have != set(want):
            raise Forbidden(
                f"Record {self.id!r} of kind {self.kind!r} carries subject_matter keys "
                f"{sorted(have)}", "⊕L35",
                needs=f"exactly {list(want)} -- missing {sorted(set(want) - have)}, "
                      f"extra {sorted(have - set(want))}",
                law="r2 05 ⊕L35 -- a document's content is its kind's keys and no others. A missing "
                    "key is an operand no reader can bind; an extra key is a second vocabulary")


def subject_of(a: "Act") -> str:
    """The act's subject, or `""`. THE ONE READ, beside the carrier it reads.

    ⚠ `isinstance(..., dict)` AND NOT `a.payload or {}`, because a hand-built probe Act may carry a
    STRING payload. `loop/effects.py::_operand` guards the same way and for the same reason; it is
    a DIFFERENT rule (it raises on any missing named operand) and is deliberately not folded here.

    ⚠⚠ **IT LIVES HERE BECAUSE THREE CALLERS NEED IT AND INLINE COPIES DISAGREE.**
    `loop/deliberate.py` would return `""` for a subject-less act; `loop/driver.py` and
    `loop/predicates.py` would each inline
    `(a.payload or {}).get("subject") if isinstance(a.payload, dict) else None` and return
    `None`. `""` and `None` are both falsy, so nothing breaks until a
    caller writes `subj is None` or puts the result in a set beside a `""`. `carriers` is the leaf
    all three already reach, and neither `deliberate` nor `predicates` imports the other, so this
    is the only home that costs no new edge."""
    return operand_of(a, "subject")


def operand_of(a: "Act", name: str) -> str:
    """The act's payload operand `name` (`office`, `to`, `subject`), or `""` where it is absent or is not a string.

    B09.18: THE ONE REFERRING READ, AND IT CANNOT RETURN AN UNHASHABLE. A hand-built or client-returned act may
    carry a list under an operand; every caller looks the result up in a dict or a set, and the fold calls a
    predicate with no catch, so a list handed back raises `TypeError` out of the season. A value that is not a
    `str` reads as `""`, which every caller already treats as no operand. Same payload guard as `subject_of`."""
    d = a.payload if isinstance(getattr(a, "payload", None), dict) else {}
    v = d.get(name)
    return v if isinstance(v, str) else ""


@dataclass(frozen=True)
class Proposition:
    """S14. IDENTITY-BEARING AND IMMUTABLE. Fixed at utterance, never destroyed.
    `frozen=True` makes the immutability structural rather than asserted.

    `support` (v12 B11.74; `19_LACUNA_conclusion_is_a_committed_assertion.md` R-19-03, FRES §7 (3)): THE CLAIM IDS AND RECORD IDS THE UTTERER
    CITED FOR WHAT HE ASSERTS -- a conclusion says why its utterer believes it. A tuple of ids, fixed at utterance with the rest (`_eff_utter` stores the
    act's `cites`, each refused unless he held it at the act), `()` for every Proposition that cites nothing, which is every one the realm builds
    or mints today. ⚠ LAYER 1, NAMED AT THE SITE: `04` §B.6/§B.9 list no `support` on a Proposition. The member is a DEPARTURE from them (the record
    and the board are its two readers, neither built), taken under `layer-conformance` B4's third disposition: the code carries it and `04` is
    not edited to match (CLAUDE.md §0.05; C3-C16). A hashed carrier gains a member, so the realm content hash moves by encoding for every world
    holding a Proposition (D-04); a trailing defaulted member moves no construction (every site is positional up to `when`, or `scope`).
    [ASSUMPTION; medium; Jordan to correct; revert: delete the member and `_eff_utter`'s `support=`.]"""
    id: str
    mood: str
    subject: str
    predicate: str
    value: Any
    when: int
    scope: Any = None
    support: tuple = ()


def refuse_a_title_in_a_body(office_id: str, post: Optional[str], body: Optional[str]) -> None:
    """THE TITLE-IN-A-BODY REFUSAL, AS A FUNCTION OF ITS OWN.

    ⚠ A TITLE IS NOT AN OFFICE, AND CONFLATING THEM PUT A KING IN THE CHURCH. `titles` carries
    the governance ladder Jordan ruled, so a `post` that names a TITLE is a seat on that ladder and
    cannot also be an organ of a faction. The overlay `{post: "King", body: "Cardinal of Justice"}`
    would be ACCEPTED without this check and produce a realm title whose Church affiliation exists
    nowhere in canon.

    WHY IT IS A FUNCTION. r2 `03_SEATS_AND_CONTENT.md` §A.8 homes this clause in `offices.yaml`'s loader
    as a CONTENT rule, "same refusal, same law string"; the loader (`data/rosters.py::_load_offices`)
    and `Office.__post_init__` both call it.

    ⚠ IT ASKS `title_domain`: *Is this post a title?* has exactly one owner in the tree,
    `title_domain`/`TITLE_DOMAINS` (`data/rosters.py`), which reads `offices.yaml: titles: domains:`."""
    if body is not None and title_domain(post) is not None:
        raise Forbidden(
            f"office {office_id!r} names the TITLE {post!r} and the body {body!r}",
            "offices.yaml -- titles vs office_bodies",
            needs="a title is held at a rung on the governance ladder, not seated in an organ",
            law="Jordan 2026-09-02 -- the title ladder turns on holdings and purview; an "
                "office belongs to a faction's body. A post is one or the other, never both")


@dataclass
class Office:
    """S11. `rung?` is OPTIONAL; null is the office-cluster case (S6.2)."""
    id: str
    post: str
    rung: Optional[str]
    remit_acts: list[str]
    scope_rung: Optional[str] = None
    binds: str = "members_by_admission"
    conferral: Optional[str] = None
    revocation: Optional[str] = None
    # NO `establishment` FIELD: `ARCH §B.7` call 2: *"`establishment` is a Query over `oblige`, not a
    # field. A set of persons on a seat is two homes for one fact."* `queries/world_q.py::establishment_of`
    # answers it over live `oblige` Tenures. NO `dates[]` FIELD: it has no reader and no writer (every
    # `.dates` in the package is `World.dates`, the calendar's dict) and no matrix row; `04 §B.7`'s `Seat :=`
    # spells `dates[]`, which Jordan's `RR-B` ruling (limb `B-1`, 2026-09-17) AMENDS, and `04:314` carries
    # the amendment inline. `Office`'s encoding folds into `World.content_hash` and carries every field NAME,
    # so a field added or removed here moves the digest of every world holding an office.
    # `04 §B.7`'s RATIFIED `Seat := ( …, upkeep, dates[], exists )` -- WHAT THE SEAT PAYS EACH
    # PERSON OBLIGED TO IT, PER TERM, out of its own rung's stores (`holonic_ARCHITECTURE.md:428`:
    # *"what the post pays its establishment out of the office's stake"*). Its reader is
    # `queries/world_q.py::upkeep_of` (`F.18`: *"the repair is a verb"*), which `_eff_transfer` asks when a seated holder pays an obligee. `None` -- every seat any
    # builder makes today -- is not "free": it defers to the fixture `default_upkeep` (`H-158`),
    # read at that one owner, so no caller substitutes a number of its own. Units of whatever matter
    # the paying `transfer` carries; see `upkeep_of` for the limit that states.
    upkeep: Optional[int] = None
    # ⚠ `H-99`: `body` AND `faction` ARE FIELDS BECAUSE A VALUE VALIDATED AND DISCARDED
    # (`office_faction`'s return at overlay load) CAN BE READ BY NOTHING DOWNSTREAM -- the criterion on
    # which `governance_modes` and `power_bases` were deleted from `rosters.yaml`: an artifact nothing
    # reads.
    body: Optional[str] = None
    faction: Optional[str] = None
    # B05.20 (U1-D, D-U1-01a): THE ONE LEVEL AN ACT EXERCISED THROUGH THIS SEAT BRINGS TO A ROOM ITS BENCH SITS OVER -- a
    # `sigma_leverage.LEVEL_SIGMA` name, authored as `offices.yaml`'s row key `modifier:` (refused at load if it is no level)
    # and read by `seam/wrappers/sigma.py`'s `office` source alone. `None` -- every seat today -- is *none*: *"a seat declaring
    # none behaves as today"*. Written at build only (`write_matrix.yaml`'s `(Office, modifier)` row has no step): never a die in
    # the pool and never an opposition. THE FIELD NAME FOLDS INTO `World.content_hash` (see the encoding note above), so adding
    # it moved the digest of every world holding an office, by name alone: a declared encoding mover, not a behaviour one.
    modifier: Optional[str] = None

    def __post_init__(self):
        # `04` §B.1: A SEAT'S ID IS A `SeatId` -- the same string, tagged (`state/ids.py`), so the fold
        # can refuse it as an `Act.actor`. Tagged HERE because this is where a seat id enters the tree.
        self.id = SeatId(self.id)
        # The remit is a fixture choice; its MEMBERS are not. A typo here would mint a remit act
        # and every `remit:<that act>` eligibility would silently never match -- a verb quietly
        # unavailable to everyone, which is the worst shape a failure can take.
        bad = [a for a in self.remit_acts if a not in REMIT_ACTS]
        if bad:
            raise Unowned(f"office {self.id!r} claims remit acts not on the roster: {bad}",
                          "S11", needs="an act from rosters.yaml: remit_acts",
                          law="#353 §11 -- the remit acts are a CLOSED set")
        # The three canon axes, resolved ONCE, at construction, on the object the world holds.
        # `office_faction` refuses an unknown body, an unknown faction, a body/faction mismatch
        # and an office that belongs to nothing.
        # ⚠ REQUIRED ON EVERY OFFICE: requiring it neither breaks every fixture (there are FOUR Office
        # construction sites in the whole chain) nor imports canon into the substrate (the canon factions
        # are read from `rosters.yaml` at import either way). Jordan, 2026-09-02: *"Why would requiring a
        # faction on every office break canon? Wouldn't it just imply that we don't have enough factions?"*
        #
        # ⚠ THAT IS §42.2's POLARITY RULE, AND IT CUTS THE RIGHT WAY. Optional turns an office
        # nobody can place into a silent `None`; required turns it into a REFUSAL that names the
        # gap -- either the roster is missing a faction, or the office is mis-conceived, and both
        # are findings worth having. An office belongs to something or we do not know what it is.
        self.faction = office_faction(self.body, self.faction)
        # HOW THE SEAT IS FILLED AND WHO MAY STRIP IT -- ED-IN-0256 rulings (2) and (3), `13d-i`.
        # The remit clause's shape, one field along: a typo in a declared basis would otherwise
        # make a seat nobody can ever fill or strip, and look like a working precondition while
        # it did. `None` stays lawful -- a seat declaring no basis is refused by the predicates,
        # not here, because every world builder in the tree still constructs seats without one.
        if self.conferral is not None:
            require_member(
                self.conferral, CONFERRAL_BASES,
                f"office {self.id!r} declares the conferral basis {self.conferral!r}",
                "rosters.yaml -- conferral_bases",
                law="ED-IN-0256 (2) -- a seat is filled by one of a CLOSED set of ways; an "
                    "off-roster basis would pass no conferral, silently, forever")
        if self.revocation is not None:
            require_member(
                self.revocation, REVOCATION_BASES,
                f"office {self.id!r} declares the revocation basis {self.revocation!r}",
                "rosters.yaml -- revocation_bases",
                law="ED-IN-0256 (3) -- who may strip a seat is a CLOSED set of rules; an "
                    "off-roster basis would admit no revocation, silently, forever")
        # HOW THE SEAT TAKES ON THOSE WHO SERVE IT -- r2 `05` RULED (b), `ARCH F.17`. The two clauses above, one field along. Never `None`: the field has a default, so
        # every seat declares one, and an off-roster value would make a seat nobody can join while
        # `_req_oblige` looked like a working precondition.
        require_member(
            self.binds, BINDS_BASES,
            f"office {self.id!r} declares the binds basis {self.binds!r}",
            "rosters.yaml -- binds_bases",
            law="ARCH F.17 -- how a person joins a seat is a CLOSED set; an off-roster basis "
                "would admit no `oblige`, silently, forever")
        # WHAT THE SEAT PAYS EACH OBLIGEE. `None` defers to the fixture (see
        # the field); a declared value must be a whole, non-negative amount, because `upkeep_of`'s
        # reader divides a payment by it and a negative or fractional upkeep would renew a number
        # of terms nobody could state. `bool` is refused by name: `True` is an `int` to Python and
        # an upkeep of one unit to nobody.
        if self.upkeep is not None and (isinstance(self.upkeep, bool)
                                        or not isinstance(self.upkeep, int) or self.upkeep < 0):
            raise Forbidden(
                f"office {self.id!r} declares the upkeep {self.upkeep!r}", "ARCH §B.7",
                needs="a whole, non-negative amount per obligee per term, or None for the "
                      "fixture `default_upkeep`",
                law="ARCH §B.7 `Seat := ( …, upkeep, … )` / F.18 -- upkeep is what the seat pays "
                    "each person obliged to it; `_eff_transfer` counts how many a payment covers")
        # A TITLE IS NOT AN OFFICE -- the refusal and its reasoning live in the function
        # (`refuse_a_title_in_a_body`'s own docstring has the fuller account; `offices.yaml`'s
        # loader calls `title_domain` the same way).
        refuse_a_title_in_a_body(self.id, self.post, self.body)
        # A titled post must sit at the rung its title governs. Otherwise a Duke seated at the
        # realm has realm-wide purview (`under_purview` walks up to the SEAT), which is the
        # governance canon inverted by a data-entry slip.
        # ⚠ `scope_rung` HAS A READER IN THE GAME: `queries/world_q.py::judging_set` reads `off.scope_rung`
        # directly as the whole mechanism by which a bench's purview reaches a venue (`H-32`), and Jordan's
        # `RR-B` ruling (limb `B-1`) KEEPS `scope?` in the ratified `Seat :=`; deleting the field would
        # silently reopen `H-32`.
        dom = title_domain(self.post)
        if dom is not None and self.scope_rung is None and self.rung is not None:
            self.scope_rung = self.rung




class Rung:
    """S10 -- THE HOLON. Eight kinds, ONE type. A Rung owns NO SOCIAL AGGREGATE (S10.1).

    A WHITELIST over S10's declared field set -- a concept check rather than a term check (a
    blacklist of spellings would pass `r.morale` and `r.stability`).
    Any attribute not in S10's record raises, whatever it is called."""

    # NO `stake`, `transmission` OR `judging_set_rule`: `04 §B.3` deletes each by name, *"DELETED: stake
    # (retired, no producer) · judging_set_rule · transmission"*. The judging set is a Query over seats
    # (`04:176`), `queries/world_q.py::judging_set`; transmission is `succeed`, owned by the holder
    # (`04:177`). The `object.__setattr__` calls in `__init__` bypass the whitelist, so a field is
    # added or removed in both places at once. A caller passing any of the three meets the
    # undeclared-fields refusal in `__init__`.
    #
    # ⚠ `sites`, `records` AND `dates` STAY, THOUGH r2's LIST DELETES THEM. `04 §B.3`'s RATIFIED
    # `Rung := ( id, kind, matter(stores, sites[], records[]), dates[], envelope, exists )` declares
    # all three (and `01_AXIOMS.md` §D.2 has a Rung OWN "its Sites, its Records ... dates"). Jordan's
    # `RR-B` ruling amended `04` limb by limb and none of its eight limbs is this line, so deleting
    # them would overwrite ratified text no ruling amends -- the ground on which `Office.upkeep` was
    # kept (*"Layer 1 has the field"*). Zero readers each
    # (`loop/matter.py` calls `sites` a back-reference nothing maintains): ID-13's defect, stated
    # here rather than resolved by overwriting the ratified line.
    #
    # roster-exempt: MECHANISM. These are the FIELD NAMES of this dataclass, checked so an
    # undeclared attribute raises. They are the code's own shape, not the game's vocabulary.
    # ⚠ `yield` IS PART D's FIELD NAME AND IT IS A PYTHON KEYWORD, so it is reached with
    # `getattr`/`setattr` rather than dotted access. Renaming it here would break the
    # `(record_kind, fieldname)` key the write gate, the write class and the emission all share
    # (§8) — the key is the same string Part D uses, and Part D says `yield`. A matrix row naming a
    # field the class lacks is reported by `matrix_rows_without_a_field`, which reads `_DECLARED`.
    _DECLARED = {"id", "kind", "stores", "sites", "records", "dates", "envelope", "yield"}

    def __init__(self, id: str, kind: str, **kw: Any):
        if kind not in RUNG_KINDS:
            raise Forbidden(f"Rung.kind '{kind}'", "S10", law=f"S10 -- eight kinds: {RUNG_KINDS}")
        object.__setattr__(self, "id", id)
        object.__setattr__(self, "kind", kind)
        # `yield` is #353 §25's *"only here"* row: what this rung PRODUCED this season, per
        # matter kind. Empty for a rung that produces nothing, which is most of them.
        for f_, d in (("stores", dict), ("sites", list), ("records", list),
                      ("dates", list), ("envelope", list), ("yield", dict)):
            object.__setattr__(self, f_, kw.pop(f_, None) or d())
        if kw:
            raise Forbidden(f"Rung given undeclared fields {sorted(kw)}", "S10.1",
                            law="S10.1 -- a Rung owns NO social aggregate: no norms, no densities, no reputation, no unrest, no legitimacy. EVERY ONE IS A QUERY")

    def __setattr__(self, k: str, v: Any) -> None:
        if k not in self._DECLARED:
            raise Forbidden(
                f"Rung.{k} assigned -- not a declared field of S10's record", "S10.1",
                needs="a Query over the containment subtree, owned by Nobody",
                law="L3 -- every aggregate is a function, never a field. S22.1 -- if the aggregate is a function it CANNOT go stale and CANNOT be initialised and then forgotten, because there is nothing to initialise",
            )
        object.__setattr__(self, k, v)


def matrix_rows_without_a_field() -> dict:
    """Every matrix row whose `(kind, field)` names no field of that kind's model.

    ⚠ NOTHING ELSE CHECKS THAT A MATRIX ROW'S `fieldname` IS A REAL FIELD OF ITS `record_kind` (the
    `(Record, held_by)` defect). It reports rather than raising, because a row can legitimately outrun the model:
    Part D is the SPECIFICATION and this file is one implementation of it, so a row naming a field
    the instrument has not built yet is a TODO for the instrument, not a defect in Part D.

    Kinds the instrument models as DICTS rather than classes — `Date`, `DocketItem`,
    `ConveningCondition` — cannot be checked at all and are reported separately, so the number is
    never mistaken for a clean bill.

    ⚠ `Rung` IS CHECKED THROUGH ITS `_DECLARED` SET, NOT `is_dataclass`: it is a plain class with an
    explicit `_DECLARED` field set — the whitelist S10 gives it, so that an undeclared attribute
    raises — and `is_dataclass` alone would report its five rows, `(Rung, yield)` among them, as
    *uncheckable*. A declared field set is a field set whatever shape it is stored in."""
    import dataclasses as _dc
    out = {"absent": [], "unmodelled": []}
    for (kind, fld) in sorted(MATRIX):
        cls = globals().get(kind)
        declared = (set(getattr(cls, "_DECLARED", ()) or ()) or
                    ({f.name for f in _dc.fields(cls)} if _dc.is_dataclass(cls) else set()))
        if cls is None or not declared:
            out["unmodelled"].append((kind, fld))
            continue
        if fld == "exists":
            continue                     # existence is the collection's membership, not a field
        if fld not in declared:
            out["absent"].append((kind, fld))
    return out
