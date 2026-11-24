"""`season.loop.predicates` — the `requires:` cells the grammar does not type. The verbs are the keys
of `REQUIRES_PREDICATES` below, which is the owner: this comment names no list and carries no count.

The registry and its decorator live with the functions they register: **a decorator-filled table
lives in the module that defines the decorated things**, or the table is empty at the moment the
loader reads it.

A verb carries a typed cell in `verb_table.yaml` or a predicate here, never both. §8's rule is that
a rule lives once, and a verb carrying both would be two readings of one prose cell.
`test_wa_one_owner_a_verb_has_a_typed_cell_or_a_predicate_and_never_both` is the guard; it reads
`S.REQUIRES_PREDICATES`, which is this module's dict.
"""

from __future__ import annotations

from typing import NamedTuple, Optional

from ..data.requires import binding_from_act
from ..data.verbs import DISPOSAL_EVENTS, _OPENERS_FROM_EFFECTS
from ..data.rosters import (BINDS_BASES, FOUNDED_CONFERRAL, FOUNDED_REVOCATION, FOUNDER_KEEPS, RELEASABLE_KINDS,
                            RUNG_KINDS)
from ..gaps import Forbidden, Unowned, Unspecified
from ..queries.person_q import ABOUT_KEYS
from ..queries.world_q import (BAN_KIND, DETAIN_KIND, DOCKET_PETITION, commands, docketed, founded_office_id, founded_post,
                               founds_over, restrained)
from ..state.attribution import causing_act
from ..state.carriers import Office, operand_of, subject_of
from ..trace_log import TRACE
# G3: THE SEAT-AUTHORITY RULES LIVE WITH THE GATE THAT ENFORCES THEM. The write gate's F3 clause
# evaluates `seated_on_the_rung_above` and `REVOCATION_RULES` (T-o) and `has_conferral_basis` (the
# conferral basis), and `state/` may not import the loop. Ruling (3)'s rule is asked of the SEAT
# exercised instead of the actor (`04:332`). The names are imported, not copied, so a precondition
# here and the gate there cannot disagree (`CLAUDE.md` §8) -- and a `monkeypatch` of this module's
# `has_conferral_basis` still reaches both preconditions that call it by that name.
from ..state.gate import (  # noqa: F401 -- `REVOCATION_RULES`, `in_holdings`, `seated_on_the_rung_above` re-exported
    REVOCATION_RULES, has_conferral_basis, has_filler, has_revocation_disposal, in_holdings, may_claim, may_fill,
    may_revoke, purview_reaches, seat_hold, seated_on_the_rung_above)


# A `requires:` predicate. The table states preconditions in PROSE, which the fold cannot read --
# the same defect `resolve` had, one column along. A verb with a prose precondition and no
# predicate here REFUSES, naming what is missing, rather than silently succeeding.
REQUIRES_PREDICATES: dict = {}


class Answer(NamedTuple):
    """B09.19: A NAMING PREDICATE'S ANSWER, `(ok, clause)`. `clause` is the one of the names the predicate declared at
    `requires_predicate(clauses=...)` that refused it (`None` when admitted). It is truthy exactly when `ok` is, so a caller
    that asks only *did it pass* (`if pred(w, a)`, `assert not pred(w, a)`) reads it as it read the bool, and a bare tuple's
    always-true `(False, name)` is not a trap. `loop/resolve.py::_admits` is the reader of `clause`: it becomes
    `Verdict.failed`, which `row.refusal_for` turns into the kind a KEYED row declares for that clause."""
    ok: bool
    clause: Optional[str] = None

    def __bool__(self) -> bool:
        return self.ok


ADMITTED = Answer(True)


def requires_predicate(verb: str, clauses: tuple = ()):
    """Register `fn` as `verb`'s `requires:` predicate. `clauses` are the names a refusal of it can carry, in branch order:
    THE ONE OWNER OF THEM. A predicate that declares none answers a bare bool, as the others do; one that declares them
    answers `Answer`, and `data/verbs.py::VerbRow.precondition_evaluable` admits a KEYED row of that verb only when its keys
    are exactly these (the loader cannot import `loop/`, so the names reach it through the predicate table)."""
    def deco(fn):
        fn.clauses = tuple(clauses)
        REQUIRES_PREDICATES[verb] = fn
        return fn
    return deco


def _refuse(clause: str, ids: str) -> bool:
    """REM-14: THE CLAUSE A PREDICATE REFUSED ON, LEFT IN THE TRACE. Returns `False`, so a refusing
    branch reads `return _refuse(...)`. The fold's own row (`loop/resolve.py`, "<verb> by <actor>:
    precondition unmet") says THAT a precondition failed; a predicate with several `return False`
    lines could not say WHICH. `"<clause> -> <ids>"` is the cluster-key form `harness/report.py` groups
    DECISION rows by (`what.split(" -> ")[0]`), as `loop/effects_migration.py` writes it.

    ⚠ A TRACE ROW AND NOTHING ELSE. The predicate carries no `observed` reads: returning a `Verdict`
    with them would deposit claims through WITNESS and move the world hash. What a refusal's NAME can
    change is its kind, through `_refuse_at`, and only on a keyed row."""
    TRACE.decision(f"{clause} -> {ids}", "E2/S27.1", chose="refuse",
                   alternatives=["admit the act and leave the refusal to the effect or the write "
                                 "gate"])
    return False


def _refuse_at(clause: str, ids: str, said: Optional[str] = None) -> Answer:
    """`_refuse` for a predicate that declares `clauses=`: the same trace row, and the refusal answers `Answer(False, clause)`.
    `clause` is one of the names the caller declared (`test_predicates_clause.py` walks every call and checks it). `said` is the
    trace's phrase where it is a sentence rather than the name (the cluster key `harness/report.py` groups by), PAIRED with the
    name at the branch it describes, so the two cannot drift apart: the name is the owner and the phrase is its gloss."""
    _refuse(said or clause, ids)
    return Answer(False, clause)


# ---------------------------------------------------------------------------
# THE GOVERNANCE SLICE. Jordan, 2026-09-02, asked for governance and management across scales of
# governing bodies. The verbs for it are the eight `binding_decision` rows; `post_remit` and
# `chronicle`, two of `W6`'s five witness channels, need a binding decision.
#
# ⚠ A FACTION DOES NOT ACT. `ARCHITECTURE_V2.md:93` puts *"a faction acting as an actor"* in its
# REFUSAL table at `L1`, with three corpus cases that wanted it, and `H-21` completes it -- *"a
# faction's treasury is matter at the rung or office that holds it"*. Governance at a scale above
# the person is A PERSON HOLDING AN OFFICE acting at a rung, which is what these four do.
# ---------------------------------------------------------------------------


@requires_predicate("confer", clauses=("office", "basis", "term", "conferee", "purview", "held", "displacement"))
def _req_confer(w: "World", a: "Act") -> Answer:
    """Part E, IN FULL: *"the office's **conferral basis**, and 1-per-object: no live `hold` on the
    object, **or** the holder-Proposition has zero live `commit` (§54 it. 20)"*.

    ⚠ BOTH CLAUSES, AND THE `or` DISJUNCT. Dropping a disjunct is an OVER-REFUSAL -- an office
    whose holder-Proposition has no live commit would be refused where Part E admits it -- and `G4`
    weighs that equally with an invention.

    ⚠ G3 (plan position 6) ADDS TWO CONJUNCTS, AND BOTH ARE THE WRITE GATE'S OWN RULES ASKED EARLY.
    `_eff_confer` writes two Tenures that are somebody else's -- it OPENS the conferee's `hold` and,
    on a held office, CLOSES the incumbent's -- and the gate now refuses both unless a basis admits
    them (`04 §C.2` F3). A precondition that admitted what the gate refuses would turn a refusal
    that EMITS (`confer.refused`, `§E2`) into a gate refusal the fold emits unnamed (B03.76), so this asks the
    gate's own predicates, not a copy of them:
      * the CONFERRAL basis -- the seat the act exercises (`Act.via`) has purview over the office
        conferred (`may_fill`: ruling (4), `04:332`'s *"every purview walk uses `via.scope`"*);
      * on a held office, T-o for the incumbent's edge -- `via`'s revocation authority over the
        seat (`may_revoke`: ruling (3)) -- unless the incumbent IS the actor (T-m: his own edge).
    `04 §C.2`'s own F3 note names `confer` beside `revoke` as *"writing `Tenure.until` on an edge
    whose subject is somebody else"*, which is why the displacement is T-o and not a second reading
    of the conferral basis.

    B09.19: THE ANSWER IS `Answer(ok, clause)`, the clause one of the seven declared on the decorator -- `office`, `basis`,
    `term` (B21.01: the act declares a term that is no positive whole number), `conferee`, `purview` (G3's `may_fill`), `held` (1-per-object: the seat is held and the conferral is to its own holder or
    displaces one who carries a live `commit`) and `displacement` (T-o over the incumbent). The trace phrase beside each is the
    sentence the REM-14 rows have always carried."""
    obj = office_named_by(a)
    if not obj or not isinstance(obj, str) or obj not in w.offices:
        # (a list `subject`/`office` is unhashable: refuse, never raise)
        return _refuse_at("office", f"{a.actor} on {obj!r}", "a confer names no office the world holds")
    off = w.offices[obj]
    if not has_conferral_basis(off):
        return _refuse_at("basis", f"{a.actor} on {obj!r}", "a confer of an office with no conferral basis")
    # B21.01: A DECLARED TERM IS A POSITIVE WHOLE NUMBER, asked before `may_fill` so a malformed one refuses (and EMITS
    # `confer.refused`) where `_declared_term`'s raise would end the season; that raise stays as the backstop for an act that skipped this.
    declared = a.payload.get(TERM_KEY) if isinstance(a.payload, dict) else None
    if declared is not None and (isinstance(declared, bool) or not isinstance(declared, int) or declared < 1):
        return _refuse_at("term", f"{a.actor} on {obj!r} term {declared!r}", "a confer declares a malformed term")
    # Batch B-I close (C1): THE CONFEREE IS A LIVING PERSON. `to` comes from the conferrer's own
    # claims (`known_persons`), which can name somebody since dead, and nothing downstream asks:
    # `_admits` refuses only a missing or self `to`, and the gate admits the hold under the
    # conferral basis, which reads `via` alone. `tell` gets this from its `hearer` conjunct; this row
    # is untyped, so it is asked here -- before `may_fill`'s purview walk, the dearer conjunct.
    conferee = operand_of(a, "to")         # a non-string `to` (a list is unhashable) reads as "": refused, never raised
    if conferee not in w.persons:
        return _refuse_at("conferee", f"{a.actor} to {conferee!r}",
                          "a confer on a conferee who is no living person the world holds")
    if not may_fill(w, a.actor, a.via, off):
        # G3: the seat exercised does not reach the seat conferred
        return _refuse_at("purview", f"{a.actor} via {a.via!r} on {obj!r}",
                          "a confer the seat exercised does not reach the office conferred")
    tenures = w.tenures                    # one view for the three scans below
    if not any(t.kind == "hold" and t.object == obj and t.live for t in tenures):
        return ADMITTED                    # 1-per-object satisfied
    # THE `or` DISJUNCT: a held office is still conferrable when the holder-Proposition carries
    # no live `commit`. §54 item 20.
    # ⚠ READ AGAINST THE ROW AT IN-53 step (4) AND KEPT, WITH THE REASON. §54 item 20 (*"a
    # memberless faction's `hold`"*) counts the live `commit` edges TO a Proposition that HOLDS; this
    # counts any live `commit` BY the holder. The literal reading is unreachable as built: a `hold`
    # is a PERSON's edge (`holonic §15`; `World._refuse_bad_hold`), so no Proposition holds a seat,
    # and the tree already migrated the row to the holder (`harness/probes.py` F2: *"~~holder-
    # Proposition~~ -> holder, per `holonic §15`"*). Taking the literal reading would make this
    # disjunct, and with it `confer`'s displacement under T-o, dead code
    # (`test_g3_not_yours.py::test_g3_confer_refuses_at_the_precondition_what_the_gate_would_refuse`
    # arm `c3` reddens, measured); F2's *"zero commits to the cause he held it for"* needs a
    # seat -> cause map nothing declares. Neither is this position's to invent; left as it is.
    holder = next((t.subject for t in tenures
                   if t.kind == "hold" and t.object == obj and t.live), None)
    if holder is None or holder == conferee:
        # B-I close, Phase 3 F1: conferring a seat on its own holder changes nothing but closes and
        # reopens his edge
        return _refuse_at("held", f"{a.actor} to {conferee!r} on {obj!r}", "a confer of a seat on its own holder")
    if any(t.kind == "commit" and t.subject == holder and t.live for t in tenures):
        return _refuse_at("held", f"{a.actor} displacing {holder!r} on {obj!r}",
                          "a confer displacing a holder who carries a live commit")
    # G3: displacing the holder CLOSES HIS EDGE -- T-o, through the seat exercised.
    if holder == a.actor or may_revoke(w, a.actor, a.via, off):
        return ADMITTED
    return _refuse_at("displacement", f"{a.actor} via {a.via!r} displacing {holder!r} on {obj!r}",
                      "a confer displacing a holder the seat exercised has no revocation authority over")


@requires_predicate("succeed", clauses=("operand", "banned", "claim"))
def _req_succeed(w: "World", a: "Act") -> Answer:
    """v10 IN-61 (RS-27): THE HEIR'S CLAIM -- *admitted iff the throne has no live `hold` and the actor
    holds `successions[throne]`*. The seat is the act's `subject` (the classed `Office` referent of the
    question he answers: `world_q.seats_named`, the vacancy he was told of). The whole test is the write
    gate's own `may_claim`, asked with the seats the actor holds live -- so a claim the gate would refuse
    is refused here first and EMITS (`succession.refused`) rather than raising `NotYours` out of the fold.
    Untyped: the closed grammar has no cell for *no live `hold` on the subject* nor for a roster lookup.

    B09.19: THE ANSWER IS `Answer(ok, clause)`: `operand` (the subject is no seat), `banned`, and `claim` -- the gate's own
    `may_claim` refusing (a live hold on the seat, or no `successions` entry the actor holds), which the declared two did not
    name and which now leaves its trace row like every other refusing branch."""
    seat = subject_of(a)                   # a non-string `subject` (a list is unhashable) reads as "": refused, never raised
    if seat not in w.offices:
        return _refuse_at("operand", f"{a.actor} on {seat!r}")
    if restrained(w, a.actor, BAN_KIND, at=w.offices[seat].rung):
        # a banned man is seated by no route within the banning seat's reach (`confer` declines him, `_req_oblige` 5)
        return _refuse_at("banned", f"{a.actor} on {seat!r}")
    titles = {t.object for t in w.seat_holds(a.actor)}
    if may_claim(w, a.actor, w.offices[seat], titles):
        return ADMITTED
    return _refuse_at("claim", f"{a.actor} on {seat!r}", "a succeed the heir's claim does not admit")


#: IN-10 (b): THE PAYLOAD KEY A `confer` DECLARES ITS SEAT-HOLD'S TERM UNDER -- the carrier's own field name (`Tenure.term`), not a
#: `requires_operands` member: no typed cell binds it (the row is untyped), exactly as `create_record`'s act-declared `stages` and a
#: hand-built `confer`'s `office` are payload keys the effect reads and no cell does. A computed act carries none. It lives beside
#: `office_named_by`, the other payload key `confer` reads, because `_req_confer` asks it before `loop/effects_governance.py`
#: (which imports this module) reads it; the seat row's `term:` (`offices.yaml`) is the same word.
TERM_KEY = "term"


def office_named_by(a: "Act") -> "Optional[str]":
    """THE OFFICE A `confer` ACT NAMES -- the one reader `_req_confer` and `_eff_confer` share
    (IN-53 step 2).

    A hand-built act supplies it on the payload's `office` key (the corpus overlays,
    `corpus_run._check_office`); a COMPUTED act carries it as its `subject`, the classed Office
    referent of the question it was formed from (`queries/world_q.py::questions_for`'s vacancies),
    read through `binding_from_act`, the fold's own binding. `office` wins where both are present,
    so no hand-built act changes meaning; `None` when the act names neither. `revoke` is a caller
    too (B21.13, BIND_C commit C2): `_req_revoke` and `_eff_revoke` read the seat through it, so a
    computed `revoke`, which carries the seat as `subject`, reaches its roll. `establish` is not a
    caller: the office it names does not exist yet (`office_described_by`)."""
    d = a.payload if isinstance(a.payload, dict) else {}
    return d.get("office") or binding_from_act(a).get("subject")


def office_described_by(a: "Act") -> "Optional[Office]":
    """THE OFFICE AN `establish` ACT DESCRIBES, read once for the precondition and the effect.

    The operands are the office overlay's own keys (`corpus_run._check_office`,
    `boot/realm.py::build_realm`): `office` (the id), `post`, `rung`, `remit`, `body` and/or `faction`,
    `conferral`, `revocation`. `None` when the id, post, rung or remit is absent, or any operand is
    not the shape the constructor takes -- which is every COMPUTED `establish` today, because the
    row is untyped and `operands_for` carries nothing (`15c` is what changes that).

    ⚠ OTHERWISE IT CONSTRUCTS THE `Office`, AND THE CONSTRUCTOR'S RAISES PROPAGATE. That is the
    point: `Office.__post_init__` is where a remit act is checked against `REMIT_ACTS` (`Unowned`),
    where `office_faction` refuses an unknown body or faction, a mismatch or an office belonging to
    nothing (`Unspecified`/`Forbidden`), where a title seated in a body is refused
    (`Forbidden`), and -- since `13d-i` -- where a declared `conferral` or `revocation` off its
    roster is refused (`Unspecified`). `corpus_run._check_office` validates an overlay the same
    way, for the reason it gives: *the validator is the constructor, not a second copy of its
    rules*. The object returned
    is held by nothing -- no `World` is read or written here."""
    d = a.payload if isinstance(a.payload, dict) else {}
    oid, post, rung, remit = d.get("office"), d.get("post"), d.get("rung"), d.get("remit")
    if not all(isinstance(x, str) and x.strip() for x in (oid, post, rung)):
        return None
    if not isinstance(remit, (list, tuple)) or not all(isinstance(x, str) for x in remit):
        return None
    body, faction = d.get("body"), d.get("faction")
    conferral, revocation = d.get("conferral"), d.get("revocation")
    if not all(x is None or isinstance(x, str) for x in (body, faction, conferral, revocation)):
        return None
    return Office(oid, post, rung, list(remit), conferral=conferral, revocation=revocation,
                  body=body, faction=faction)


# v11 CR-25 (CR-11's design §1): WHAT A COMPUTED FOUNDING DECLARES is `offices.yaml: founding:` (B04.23), read here
# through `data/rosters.py` (`FOUNDER_KEEPS`, `FOUNDED_CONFERRAL`, `FOUNDED_REVOCATION`) and checked against their
# rosters at load. The id rule and the post rule are `queries/world_q.py`'s (`founded_office_id`, `founded_post`): the
# stamp that offers a holding and the derivation that founds it read the one owner.


def office_founded_by(w: "World", a: "Act") -> "Optional[Office]":
    """THE OFFICE AN `establish` ACT FOUNDS, WITH THE WORLD (v11 CR-25, CR-11's design §1; [ASSUMPTION; medium;
    Jordan to correct; revert: drop `holdings_to_found` and the derivation]) -- `office_described_by`'s
    World-taking sibling, read once for the precondition and the effect (`_req_establish`, `_eff_establish`), so
    the two cannot disagree on what is founded.

    A HAND-BUILT ACT CARRYING THE OVERLAY KEYS KEEPS ITS READING: where `office_described_by(a)` returns an
    office, that office is returned unchanged, and is admitted by the same `founds_over` check (H-291): asked of
    the actor, the seat `Act.via` names and the described office's rung, exactly as the derived arm asks it, and
    `None` where it refuses (`_req_establish` names that clause). Otherwise the office is DERIVED from what a
    computed act already carries -- `subject`, a rung, and `Act.via`, the seat exercised (`state/carriers.py::Act`) -- with no ninth
    operand and no office coined by name:

      rung        `subject`, admitted by `queries/world_q.py::founds_over`'s four conjuncts (holding, purview,
                  rank, the seat on its parent);
      post        `queries/world_q.py::founded_post` (`offices.yaml: titles.domains`, `TITLE_DOMAINS`, post -> kind,
                  read in reverse for the rung's kind), as data and never a branch on a kind; where a kind has two posts (King/Queen,
                  Duke/Duchess, Count/Countess) the FIRST IN AUTHORED ORDER [ASSUMPTION; medium; Jordan to
                  correct; revert: the second, or the eventual holder's];
      faction,    the exercised seat's (a seat with a `body` founding a titled post is refused by the constructor,
      body        `refuse_a_title_in_a_body`, which clause 1 translates to False);
      remit       the founder's GRANT on the seat (`seat_hold(...).granted_acts`, the `13e` snapshot of the seat's
                  `remit_acts` that `_eligible` reads -- the design names `remit_acts`; the two are equal unless the
                  office was hand-mutated after seating, and `13e` makes the grant the one consumer read
                  [ASSUMPTION; medium; Jordan to correct; revert: the office's `remit_acts`]) less
                  `FOUNDER_KEEPS` (`offices.yaml: founding: keeps`, where its [ASSUMPTION] mark now sits);
      conferral   `FOUNDED_CONFERRAL`; revocation `FOUNDED_REVOCATION`; id `founded_office_id(rung, post)`.

    `None` when the seat or the subject is absent, a conjunct refuses, or no post names the rung's kind.
    ⚠ THE CONSTRUCTOR'S RAISES PROPAGATE, as `office_described_by`'s do, and for its reason: the caller
    translates them (clause 1)."""
    off = office_described_by(a)
    held = seat_hold(w, a.actor, a.via)
    seat = w.offices[a.via] if held is not None else None
    if off is not None:
        # H-291: the overlay arm asks the call the derived arm makes, for the described office's rung
        return off if seat is not None and founds_over(w, a.actor, seat, off.rung) else None
    rung = subject_of(a)
    if seat is None or not founds_over(w, a.actor, seat, rung):
        return None
    post = founded_post(w, rung)
    if post is None:
        return None
    return Office(founded_office_id(rung, post), post, rung,
                  [x for x in held.granted_acts if x not in FOUNDER_KEEPS],
                  conferral=FOUNDED_CONFERRAL, revocation=FOUNDED_REVOCATION,
                  body=seat.body, faction=seat.faction)


@requires_predicate("establish", clauses=("office resolves", "rung held", "conferral basis", "filler", "re-founding",
                                          "may fill", "reduction needs revocation"))
def _req_establish(w: "World", a: "Act") -> Answer:
    """W3's row: *"the establishing office's conferral basis, and a rung to establish it at"*.

    ⚠ THE READING, STATED BECAUSE THE PROSE ADMITS TWO: *the establishing office* is THE OFFICE
    THE ACT DESCRIBES -- the one being founded, or re-remitted on an id that already exists -- and
    NOT the office the actor sits in. The basis `_req_confer` tests is a property of the office
    being FILLED (*"the office's conferral basis"*), so read the same way here it asks whether the
    new seat declares how it is filled. The other reading makes the founder's own seat's basis
    decide whether ANY office may be founded, which nothing in the row motivates; and it would let
    an establish found a seat with no basis, which `_req_confer` then refuses forever -- an office
    that exists and can never be filled. Eligibility (`remit:confer`) already says who may act.

    FOUR CLAUSES, EACH A REFUSAL AND NONE A RAISE -- a `NotYours` from inside the effect's `apply()`
    is caught by the fold since B03.76 and emits the row's refusal (a Tenure write put back, an
    entity the same `apply()` wrote kept), so a refusal asked HERE is cleaner and writes nothing:
      1. the office resolves: `office_founded_by` returns one (since v11 CR-25: the overlay keys
         `office_described_by` reads, else the derivation from `subject` and `Act.via`; since H-291 either
         arm only where `founds_over` admits it, an overlay act refused there naming its own clause), and the constructor's refusals
         (the three it raises) are translated to False HERE, so each rule still lives once, in the
         constructor. They remain the loud backstop inside the effect;
      2. its rung is one the world holds;
      3. it has a conferral basis, by the ONE basis test `_req_confer` also asks;
      4. its id is new -- held by no collection (a `hold` opened on it early is what the effect
         re-stamps) -- or it is an EXISTING office and the act changes its remit and nothing else.

    ⚠ CLAUSE 4's SECOND ARM IS A REMIT CHANGE, NOT A REFUSAL. `establish` is the only verb whose
    `writes:` name the office's remit, so refusing it on an existing id would leave no act able to
    change a remit. Any other difference -- a different post, rung, body, faction, conferral or
    revocation -- REFUSES: naming a different belonging for an existing id is re-founding, which
    `writes:` does not declare. The act restates the office in full; an operand it omits is read
    as the constructor reads it (`None`), never filled from the office it would replace.
    ⚠ SO AN OFFICE WITH NO RUNG (`Office.rung` is Optional, the office-cluster case §6.2) cannot
    have its remit changed by this verb: clause 2 requires a rung and clause 4 requires the same
    one. That is the row's prose, applied, not a choice made here.

    ⚠ CLAUSE 5 IS G3's, AND IT EXISTS BECAUSE `13f`'s RE-STAMP WRITES OTHER PEOPLE'S TENURES -- a
    fourth live non-owner write the G3 plan text did not list beside `revoke`, `confer` and
    `kill / wound`. `_eff_establish` re-stamps the grant (`Tenure.payload`) on every live `hold` on
    the office, and a sitting holder's `hold` is HIS edge -- the ACTOR's OWN included, since T-m
    never admits re-granting a seat-hold (`state/gate.py::tenure_write_basis`, corrected by G3's
    own antagonist pass). The write gate admits the re-stamp only under the conferral basis -- the
    authority that may fill a seat may re-grant it -- so this refuses first, with the gate's own
    predicate, whenever ANY live hold exists on the office, self included: 5. the seat the act
    exercises may fill the office (`may_fill`: purview over its rung, `via` not the office itself).
    A founding is unaffected, since there is no hold yet for `may_fill` to be asked about; ⚠ since
    v11 CR-25 (H-144 (b)) a VACANT EXISTING office is no longer: any existing office asks it, and a
    reduction of a sitting holder's grant also asks `may_revoke` (H-132 (b)), both at the clause. ⚠ It is STRICTER THAN THE GATE by one case, deliberately: a
    re-stamp that changes no grant writes nothing the gate would see, and this still asks for the
    authority -- mirroring `_grant_remit`'s equal-grant test here would be a second copy of it
    (§8).

    B09.19: THE ANSWER IS `Answer(ok, clause)`, the clause one of the seven declared on the decorator, in branch order:
    `office resolves` (clause 1: the constructor's refusals, an overlay act `founds_over` refuses, an operand missing),
    `rung held` (2), `conferral basis` (3), `filler`, `re-founding` (4: a different belonging, and an id some other class
    holds, which clause 4's *the id is new* also refuses), `may fill` (5) and `reduction needs revocation`."""
    try:
        off = office_founded_by(w, a)      # v11 CR-25: the overlay keys, else the derivation from subject and via
    except (Unowned, Unspecified, Forbidden):
        # the constructor refused it: translated, never filled
        return _refuse_at("office resolves", f"{a.actor} via {a.via!r}", "an establish the office's constructor refused")
    if off is None:
        described = office_described_by(a)
        if described is not None:
            # H-291: an overlay act whose seat does not found over the described rung (clause 1's own refusal)
            return _refuse_at("office resolves", f"{a.actor} via {a.via!r} at {described.rung!r}",
                              "an establish over a rung the seat exercised does not found over")
        return _refuse_at("office resolves", f"{a.actor} via {a.via!r}", "an establish lacking an operand the office needs")
    if off.rung not in w.rungs:
        # "a rung to establish it at"
        return _refuse_at("rung held", f"{a.actor} at {off.rung!r}", "an establish at no rung the world holds")
    if not has_conferral_basis(off):
        # "the establishing office's conferral basis"
        return _refuse_at("conferral basis", f"{a.actor} on {off.id!r}",
                          "an establish of an office with no conferral basis")
    if not has_filler(off):
        # a seat only the heir's claim opens, with no title passing it (v10 IN-61)
        return _refuse_at("filler", f"{a.actor} on {off.id!r}",
                          "an establish of a seat only the heir's claim opens, with no title passing it")
    held_as = w.class_of(off.id)
    if held_as is not None:
        if held_as != "Office":
            # the id is a person's, a rung's... -- `class_of` ambiguity
            return _refuse_at("re-founding", f"{a.actor} on {off.id!r}", "an establish on an id some other class holds")
        cur = w.offices[off.id]
        if not (off.post == cur.post and off.rung == cur.rung and off.body == cur.body
                and off.faction == cur.faction and off.conferral == cur.conferral
                and off.revocation == cur.revocation):
            # re-founding, which `writes:` does not declare
            return _refuse_at("re-founding", f"{a.actor} on {off.id!r}",
                              "an establish naming a different belonging for an existing office (re-founding)")
    # 5. G3 -- the re-stamp writes EVERY sitting holder's grant, the actor's own included.
    #
    # ⚠ THE ACTOR'S OWN HOLD IS NOT EXCLUDED: T-m NEVER admits re-granting a seat-hold
    # (`state/gate.py::tenure_write_basis`, `04:330`), not even the actor's own, so a sole holder's
    # re-stamp needs `may_fill` exactly as another person's does -- else `p_king`, sole holder of
    # `off_mayor`, re-establishing it via `off_mayor` itself would pass this precondition and
    # raise an UNCAUGHT `NotYours` inside `_fold`. A FOUNDING IS UNAFFECTED: no holder exists yet,
    # so `may_fill` is asked only where a live `hold` already exists to re-stamp (or the id is an
    # existing Office, below).
    #
    # v11 CR-25, M8 taken, H-144 (b) [ASSUMPTION; medium; Jordan to correct; revert: `return not held or
    # may_fill(...)` over `held` alone]: A REMIT CHANGE ON AN EXISTING OFFICE, VACANT OR HELD, ASKS `may_fill`
    # (and so the exercising seat's purview). The test is "the id is an existing Office", which clause 4
    # computed as `held_as == "Office"`, no longer "a live hold exists": a vacant office was re-remittable from
    # anywhere in the realm. A founding is no existing office; its purview check is `founds_over`'s (ii).
    holds = [t for t in w.tenures if t.kind == "hold" and t.object == off.id and t.live]
    if (held_as == "Office" or holds) and not may_fill(w, a.actor, a.via, off):
        return _refuse_at("may fill", f"{a.actor} via {a.via!r} on {off.id!r}",
                          "an establish on an existing office the seat exercised does not reach")
    # v11 CR-25, M8 taken, H-132 (b) [ASSUMPTION; medium; Jordan to correct; revert: drop this clause]: A
    # REDUCTION IS A PARTIAL REVOCATION. A re-stamp that drops from a sitting holder's grant
    # (`Tenure.granted_acts`, the snapshot the re-stamp overwrites) an act the new remit does not carry must
    # pass `may_revoke` on the office as it stands -- the one owner that wraps `REVOCATION_RULES` with
    # `seat_hold` and the basis-roster test, never `REVOCATION_RULES` read here (§8). Asked only where a live
    # hold exists, because H-132 concerns a sitting holder's grant [ASSUMPTION; medium; Jordan to correct;
    # revert: ask it on every existing office]. M8 (a) follows: a seat with `revocation: None` is in no basis,
    # so its grant cannot be reduced.
    # (A hold opened on the id before the office existed carries no grant to reduce, so the clause needs the
    # office: `held_as == "Office"`.)
    keeps = set(off.remit_acts)
    if (held_as == "Office" and any(set(t.granted_acts) - keeps for t in holds)
            and not may_revoke(w, a.actor, a.via, w.offices[off.id])):
        return _refuse_at("reduction needs revocation", f"{a.actor} via {a.via!r} on {off.id!r}",
                          "an establish reducing a sitting holder's grant without revocation authority")
    return ADMITTED


@requires_predicate("release")
def _req_release(w: "World", a: "Act") -> bool:
    """`04 §A.3` row 14: *one `release` verb, eligibility `own`, generic over kind*. Part E:
    *"a live tenure of a releasable kind, owned by the actor, toward the subject"*.

    THREE CLAUSES, AND THE FIRST IS THE ONE THE DESIGN IS ABOUT. `t.subject == a.actor` is
    eligibility `own` made real: `_eligible` returns True for every `own` verb without looking at
    anything (*"every person may attempt their own acts"*), so a verb whose whole point is that it
    acts on WHAT THE ACTOR HOLDS must check ownership in its precondition or it is a licence to
    close other people's edges.

    ⚠ THIS CANNOT FABRICATE, AND THAT IS STRUCTURAL RATHER THAN CAREFUL. `_eff_oblige` was reverted
    (F8, `ED-IN-0211`) for opening a Tenure to `einhir_texts`, a bare string naming no entity,
    because an OPENER takes an id and asserts a relation into existence. A CLOSER scans relations
    that already exist: a subject naming nothing matches no Tenure, the effect touches nothing, and
    the fold emits `release.refused`. There is no path here that mints a fact about a thing nobody
    named -- which is why the antonym half of Jordan's ruling is buildable today while the opener
    half waits on distinct operands (`decision/options.py:307-312`).

    ⚠ `contain` IS EXCLUDED BY THE ROSTER, NOT BY A LITERAL HERE. See `RELEASABLE_KINDS`."""
    subj = subject_of(a)
    if not subj:
        return _refuse("a release names no subject", a.actor)
    owned = [t for t in w.tenures
             if t.subject == a.actor and t.object == subj and t.kind in RELEASABLE_KINDS and t.live]
    if not owned:
        return _refuse("a release of a tenure the actor does not own toward the subject "
                       "(live, of a releasable kind)", f"{a.actor} toward {subj!r}")
    # VRES §4 edit 1 (A-37, B21.07): A PARTY DOES NOT RELEASE AN EDGE A BENCH IMPOSED -- an imposed service ends by the bench's
    # `pardon` or its term, as detention and banishment do. `_eff_release` closes EVERY live edge the actor owns toward the
    # subject, so one such edge among them refuses the act. The opening Event is the first logged Event naming the edge whose causing
    # Act (`state/attribution.py::causing_act`) is of a verb that opens its kind (`_OPENERS_FROM_EFFECTS`, `_opened_by_acts`' proxy:
    # a later closure naming the edge is not its opening), and the act is a bench's when that verb is a `DISPOSAL_EVENTS` key
    # (`rosters.yaml: own_edge_declines: disposal`). No field is added to `Tenure`.
    for t in owned:
        openers = {v for v in DISPOSAL_EVENTS if v in _OPENERS_FROM_EFFECTS.get(t.kind, ())}
        if openers and _opened_by(w, t, openers):
            return _refuse("own: an edge a bench imposed is not the party's to release (A-37)",
                           f"{a.actor} toward {subj!r}")
    return True


def _opened_by(w: "World", t, verbs: set) -> bool:
    """Is `t`'s OPENING Event the work of an Act of one of `verbs`? The opening is the first logged Event that names the edge
    and was caused by an Act whose verb opens the edge's kind (`_OPENERS_FROM_EFFECTS`), so a re-grant or a closure naming it
    later is not it. A seeded edge, or one planted by hand, has no opening Event and answers False."""
    opens = _OPENERS_FROM_EFFECTS.get(t.kind, ())
    for e in w.log:
        if any(c.subject == t.id for c in e.changes):
            a = causing_act(w, e)
            if a is not None and a.verb in opens:
                return a.verb in verbs
    return False


@requires_predicate("oblige", clauses=("seat", "binds", "own_seat", "one_edge", "banned"))
def _req_oblige(w: "World", a: "Act") -> Answer:
    """Plan position `17a` (r2 item 9; `03_SEATS_AND_CONTENT.md` §A.9; `05` §A.1.5 RULED (b)): *the
    subject is a seat whose `binds` admits the joiner, the actor does not hold it, and no live
    `oblige` from the actor to it*. The seat rides `subject`, as `commit`'s Proposition does and as
    `release` -- the closer every `oblige` ends through -- reads it back.

    ⚠ `_eff_oblige` WAS WRITTEN AND REVERTED ONCE, AND THIS IS WHY IT HAS A PRECONDITION (`ED-IN-0211`,
    recorded at `_req_release` above): it opened a Tenure to `einhir_texts`, a bare string naming no
    entity, because an OPENER takes an id and asserts a relation into existence. `03` §A.9: *"the
    re-build must take the id from the payload and refuse a non-office: that is `_req_oblige`'s
    job."* So clause 1 is the reversion's own lesson.

    FIVE CLAUSES (four until v9 SC-03a), EACH A REFUSAL (`duty.refused`) AND NONE A RAISE:
      1. the subject is a seat -- `w.offices`. A person, a rung, a Record or a bare string refuses.
         (`holonic §15` also allows `oblige : Person -> Person`; no position builds that half, and
         `establishment_of` asks only about seats, so admitting it here would open edges nothing
         reads.)
      2. the seat's `binds` is a rostered basis (`BINDS_BASES`) -- `ARCH F.17`'s own resolution,
         *"`oblige`'s `requires` reads the seat's `binds`"*, taken as r2 `05` RULED (b) takes it and
         over `03` §A.9's refusal of it. `has_conferral_basis`'s shape one field along: the
         constructor refuses an off-roster value at build, and this asks membership at the act. ⚠
         ONE BASIS IS RULED (`members_by_admission`: the joiner's own act admits him), so every
         seat constructed today passes -- conceded in the roster's own note, and a second basis
         arrives with its rule HERE, not as a value this line would read as the first.
      3. the actor does not hold the seat -- the occupant is not his own staff. `establishment_of`
         returns those who serve and `hold_force` the one who sits (§22); `03` §A.14's schema
         refuses a seat's `obligees:` naming its `holder` for the same reason. Asked as `_req_confer` asks it, by a
         scan for the actor's own live `hold`, and NOT through `world_q.hold_force`, which RAISES on
         two live holders: a precondition that raised would kill the season where `duty.refused`
         should emit, and whether a seat has one holder is not this verb's question.
      4. no live `oblige` from the actor to this seat -- one edge per pair. `oblige` is MANY per
         person (`holonic §15`; probe `P40` holds two), never two to the same seat, which would make
         `establishment_of` list one person twice.
      5. v9 SC-03a (#453 §10.4 step 3, §8.1 Excommunication): the actor holds no live `ban` -- a
         banned person cannot serve (`world_q.restrained`, the restraint's one read) a seat within the
         banning seat's reach: asked `at` this seat's rung (B21.02) [ASSUMPTION; medium; Jordan to
         correct; revert: drop the argument].
    ⚠ NOT BUILT, AND SAID SO: `03` §A.9's reach clause (*"its `rung` reaches the actor's containing
    rung"*). `05` RULED (b) closes `ARCH F.17` by `binds` *"rather than by a substitute rule"*, and the
    reach clause was part of `03`'s substitute. A person may oblige to a seat from anywhere; what he
    LEARNS through it is place-bound (`epistemic._ch_post_remit`: at the seat or nothing).

    ⚠ NO COMPUTED ACT REACHES THIS TODAY, and that is the row's `counterparty: subject`, not this
    predicate: on the UNTYPED row no operand is carried, so `opening_set` forms no `oblige`
    Candidate at all -- `give`'s precedent (plan position 16) for a second party the chooser cannot
    yet name -- and no Question's referent is ever a seat in any case (plan position `15` measured
    it for `petition`). An `oblige` executes from an act that names its seat.

    B09.19: THE ANSWER IS `Answer(ok, clause)`, the clause being the name each of the five numbered above carries on the
    decorator (`seat`, `binds`, `own_seat`, `one_edge`, `banned`)."""
    seat = subject_of(a)
    off = w.offices.get(seat) if seat else None
    if off is None:
        # 1. an opener takes a SEAT's id (ED-IN-0211)
        return _refuse_at("seat", f"{a.actor} on {seat!r}")
    if off.binds not in BINDS_BASES:
        # 2. ARCH F.17: the seat's `binds` admits the joiner
        return _refuse_at("binds", f"{a.actor} on {seat!r}")
    mine = [t for t in w.tenures if t.subject == a.actor and t.object == seat and t.live]
    if any(t.kind == "hold" for t in mine):
        # 3. the occupant is not his own seat's obligee
        return _refuse_at("own_seat", f"{a.actor} on {seat!r}")
    if any(t.kind == "oblige" for t in mine):
        # 4. one edge per (person, seat)
        return _refuse_at("one_edge", f"{a.actor} on {seat!r}")
    if restrained(w, a.actor, BAN_KIND, at=off.rung):
        # 5. v9 SC-03a: a banned man serves no seat
        return _refuse_at("banned", f"{a.actor} on {seat!r}")
    return ADMITTED


@requires_predicate("interrogate")
def _req_interrogate(w: "World", a: "Act") -> bool:
    """v10 IN-12 step 5, H-226 ROUTE (a) [ASSUMPTION; medium; Jordan to correct; revert: route (b), the
    fold running an effect on a band whose writes are empty]: #453 §9.1, *the subject is a person; custody
    is read ... which declines a subject holding no live `detain` edge; the charge is read ... once the
    docket item names the petition*. #453 puts both reads AT THE EFFECT, but the row writes `[]` at every
    band and `loop/resolve.py::_fold` runs an effect only for a non-empty `writes_at` (H-226), so they are
    read HERE, in the fold's `requires` step -- which runs before the seam is called (`loop/resolve.py::
    resolve`'s contest branch asks `_admits` first), so a refused act costs no draw.

    THREE CLAUSES, EACH A REFUSAL (`interrogation.refused`, the row's one kind) AND NONE A RAISE:
      1. the subject is a person -- `w.persons`. A rung, a Record, a Proposition or nothing refuses.
      2. CUSTODY: he owns a live `detain` (`world_q.restrained`, the restraint's one read, K-18: not a new
         stem). ANY SEAT, `restrained`'s own [ASSUMPTION]: the predicate does not ask that the custody
         is the interrogating seat's.
      3. THE CHARGE: a docket item naming him (`world_q.docketed`, the one owner) names a petition
         (`world_q.DOCKET_PETITION`, K-55) whose `terms` -- what the document is ABOUT,
         `person_q.ABOUT_KEYS` for its kind, the one owner of that key -- is he: the accusation
         `carry` put before the room (K-35; #453 §8.1, Charge). THE `HOLDS`-PROPOSITION FORM (a
         petition whose `terms` is a `HOLDS` Proposition whose `subject` is the prisoner) WAITS: a
         computed `utter` mints `OUGHT` only (#453 §14.9's `mood` source), and the plan's decided
         route reads the accused alone.
    The record kind is not compared: a Record named under the docket's petition key is one `carry`
    docketed, and `carry` docketed only a petition (`_eff_carry`)."""
    subj = subject_of(a)                   # a non-string `subject` reads as "": refused, never raised
    if subj not in w.persons:
        return _refuse("an interrogation of no person the world holds", f"{a.actor} on {subj!r}")
    if not restrained(w, subj, DETAIN_KIND):
        return _refuse("an interrogation of a man held in no custody", f"{a.actor} on {subj!r}")
    for item in docketed(w, subj):
        rec = w.records.get(item.get(DOCKET_PETITION))
        said = rec.subject_matter if rec is not None and isinstance(rec.subject_matter, dict) else {}
        if said.get(ABOUT_KEYS.get(rec.kind) if rec is not None else None) == subj:
            return True
    return _refuse("an interrogation with no docketed petition naming the prisoner",
                   f"{a.actor} on {subj!r}")


@requires_predicate("revoke")
def _req_revoke(w: "World", a: "Act") -> bool:
    """Part E: *"the office's **revocation basis**, and a live `hold` exists"*.

    ⚠ THE OFFICE CLAUSE: without a check that the object IS AN OFFICE, any live `hold` on the
    payload's object would do, and §13 makes possession of a Record a `hold` Tenure -- a holder of
    `remit:revoke` could revoke a person's possession of a book. Asymmetric with `confer`, which
    checks.

    ⚠ (`13d-i`) THE BASIS IS A ROSTERED VALUE AND IT SELECTS THE RULE -- no `is_title` branch
    (`H-109`). `ED-IN-0256` ruling (3), *"rung above of same faction"*, is one structural rule over
    every seat, and it arrives as the VALUE of the seat's declared `revocation` basis, dispatched
    through `REVOCATION_RULES`, never as a code path computed from a name. (Jordan, 2026-09-02:
    purview alone for an office; purview + holdings + strictly higher rank for a title --
    superseded by ruling (3).)

    THREE CLAUSES: the office's basis is on `rosters.yaml: revocation_bases` (`None` or off-roster
    refuses -- a seat declaring no basis is strippable by nobody); the actor satisfies the rule
    that basis names; and a live `hold` exists to close. v9 IN-31 adds a backstop BEFORE them: the
    seat's conferral basis has a revocation disposal (`has_revocation_disposal`), else refuse.

    ⚠ `remit:revoke` IS STILL NECESSARY, at eligibility. `H-91` registered that Jordan's 2026-09-02
    *"so long as"* made PURVIEW sufficient while Part E kept the remit necessary. Ruling (3) is
    silent on the remit, so the same question now reads *is the seat above sufficient?* -- still
    `H-91`'s, still not resolved by editing the transcribed `eligibility:` column."""
    obj = office_named_by(a)               # `office`, else the computed act's `subject` (B21.13)
    if not obj or not isinstance(obj, str) or obj not in w.offices:   # a list is unhashable: refused, never raised
        return _refuse("a revoke names no office the world holds", f"{a.actor} on {obj!r}")
    off = w.offices[obj]
    # v9 IN-31 (H-100): PROVENANCE UNREADABLE MEANS REFUSE. What the revocation costs is read off the
    # seat's conferral basis (`state/gate.py::REVOCATION_DISPOSAL`, total over the roster and `None`),
    # so a basis with no disposal -- reached only by a hand-mutated office, `Office.__post_init__`
    # refuses one -- refuses here (`revoke.refused`) rather than default to some cost.
    if not has_revocation_disposal(off):
        return _refuse("a revoke of a seat whose conferral basis has no revocation disposal",
                       f"{a.actor} on {obj!r}")
    # ⚠ G3: THE WRITE GATE'S T-o PREDICATE, ASKED EARLY -- `may_revoke` is `seat_hold` (`via`
    # present, the actor seated in it) + the basis on the roster (`None` or off-roster: the seat
    # cannot be stripped) + the rule that basis names, asked of `via`'s seat (`04:332`: the seat
    # exercised, not the actor).
    # The same function refuses the write at the gate, so this cannot admit what the gate refuses.
    if not may_revoke(w, a.actor, a.via, off):
        return _refuse("a revoke the seat exercised has no revocation authority over the seat",
                       f"{a.actor} via {a.via!r} on {obj!r}")
    if any(t.kind == "hold" and t.object == obj and t.live for t in w.tenures):
        return True
    return _refuse("a revoke of a seat nobody holds", f"{a.actor} on {obj!r}")


@requires_predicate("dispatch")
def _req_dispatch(w: "World", a: "Act") -> bool:
    """Part E: *the named person exists*; and (`16_PESSIMIST_FA_C` edit 3, B21.21) *the seat he is sent by commands him*.

    THE SAME BASIS `issue` ASKS (B21.20): `world_q.commands(w, actor, via, subject)` -- his sworn man, the holder of a seat
    this seat may revoke, or an unseated person in its land (A-22). A `dispatch` is an order, so an order to a stranger
    (a man seated in another chain, living inside the sender's land) is refused here as `issue`'s writ is: he is not the
    sender's man by living where the sender's purview reaches. The basis reads the seat the act exercises (`a.via`); a
    dispatch naming none commands nobody (`commands` is False for a `via` that is no office).

    B21.57 (`IS-B3-FA-05`, CP-T09-08): THE OPTIONAL DESTINATION. An order that names one (`dest`, the key `_eff_dispatch` reads)
    names a Rung the seat's purview reaches (`purview_reaches`, the gate's one walk): a seat orders a man only to ground it
    holds. An order naming none is the order it was, unchanged [ASSUMPTION; medium; Jordan to correct; revert: drop this
    clause and `dest` is any rung the world holds]."""
    subject = subject_of(a)                # a non-string `subject` (a list is unhashable) reads as "": refused, never raised
    if subject not in w.persons:
        return _refuse("a dispatch names no person the world holds", f"{a.actor} to {subject!r}")
    if not commands(w, a.actor, a.via, subject):
        return _refuse("not commanded", f"{a.actor} via {a.via!r} to {subject!r}")
    dest = a.payload.get("dest") if isinstance(a.payload, dict) else None
    if dest is not None:
        seat = w.offices.get(a.via) if isinstance(a.via, str) else None
        if not isinstance(dest, str) or seat is None or dest not in w.rungs or not purview_reaches(w, seat, dest):
            return _refuse("a dispatch to a place outside the seat's purview", f"{a.actor} via {a.via!r} to {dest!r}")
    return True


@requires_predicate("convene")
def _req_convene(w: "World", a: "Act") -> bool:
    """CORRECTED (plan position `18`/PROC-A, 2026-09-29; `21_RECONCILIATION.md` PHASE 2 step 9;
    `03_PARAMETERS.md` §C.1). Part E's cell was *the venue's **container** resolves, or is NONE*
    (§6.2) -- a bug the ordinal test below both fixes and replaces: a REALM has no container by
    construction (it IS the root of the containment tree), so that clause refused a convening at
    the top of the ladder, which Jordan's ruling admits explicitly: *"convene could happen at any
    scale except individual/person."* The lawful clause is the ordinal (`03_PARAMETERS.md` §C.1):

        rank(subject.kind) > rank(person)

    `rung_kinds` is ORDERED with `person` first (rank 0), so this is
    `RUNG_KINDS.index(kind) > 0` -- correct if a sub-settlement tier is ever added, where an
    enumerated kind list would not be. ⚠ THE GROUND IS A TYPE FACT, NOT AN OCCUPANCY FACT: *"the
    `person` kind is the address slot and the `Person` is who stands in it ... a proceeding
    convenes at a place; a person-rung is an address, not a place"* (§C.1, verbatim) -- so this
    reads `Rung.kind`, never who or how many live there.

    ⚠ THE VENUE RIDES `subject`, NOT `venue` -- C-11 (`21_RECONCILIATION.md:379`): *"subject
    already binds the rung."* `requires_operands` has never carried a `venue` member and a
    computed act cannot bind one; `_derive_operand`'s `subject` branch already returns the
    Question's own referent, so a person-formed convening needs no new plumbing. `_eff_convene`
    reads the same key.

    ⚠ NOT A `scalar_threshold` TYPED CELL, AND THAT IS A NAMED SCOPE-DOWN. That form's `check()`
    reads BOTH sides off the SAME bound entity (`subj`), so it has no channel for a literal
    constant: `threshold:` must be a `requires_operands` NAME carrying ONE meaning across every
    verb (`decision/options.py::_derive_operand`'s own stated rule -- *"a per-verb table would be
    the special case G2 is actually about"*), and `threshold_predicate:` is a second READ on the
    SAME subject, never a different one, so it cannot compare against `rank(person)` as a
    constant. Coining a ninth `requires_operands` member or overloading `floor`'s already-declared
    (and structurally different, per-site-kind) meaning would be exactly the collision that rule
    exists to forbid. The `rank` STEM is real, general infrastructure (`REQUIRES_STEMS`,
    `WorldReader.read`) for whatever next needs it typed; this predicate reads the same roster
    ordinal directly rather than smuggling a second stem in to dodge the constant."""
    d = a.payload if isinstance(a.payload, dict) else {}
    if d.get("subject") is None:
        return True                        # §6.2's carve-out: tested on the RAW key, before the read below
    subject = subject_of(a)                # a non-string `subject` (a list is unhashable) reads as "": refused, never raised
    r = w.rungs.get(subject)
    if r is None:
        return _refuse("a convene at a venue that is no rung the world holds",
                       f"{a.actor} at {subject!r}")
    if RUNG_KINDS.index(r.kind) > 0:
        return True
    return _refuse("a convene at a person-rung (an address, not a place)",
                   f"{a.actor} at {subject!r}")


# ---------------------------------------------------------------------------
# ⚠ `transfer`, `tell`, `move`, `work` AND `give` CARRY NO PREDICATE HERE: each is a TYPED CELL in
# `verb_table.yaml`'s `requires_typed:` column, read by `evaluate()`, and §8's rule is that the rule
# lives once -- a verb with both would be two readings of one cell, which is how `_req_confer` came
# to drop a disjunct and `_req_revoke` an entire clause.
# `test_wa_one_owner_a_verb_has_a_typed_cell_or_a_predicate_and_never_both` is the guard that
# fails on a recurrence.
#
# THE ONES THAT REMAIN are the keys of `REQUIRES_PREDICATES` (read the registry; no count is kept here).
# `confer`, `revoke`, `dispatch` and `convene` are `remit:`-eligible,
# not `own`-eligible, and `W-A`'s scope is the `own` rows. Two of them need grammar forms with no
# `own` cell (`cardinality`, `basis`) and `confer` needs a DISJUNCTION, which no `own` cell has
# and which is therefore not built (`ID-13`: a combinator nothing uses is a dead carrier).
# ⚠ `release` IS AN `own` ROW. `W-A`'s scope IS the `own` rows, and a predicate on one would ordinarily be a
# cell somebody failed to type. It is not here, and the reason is the same DISJUNCTION that keeps
# `confer` out: `release`'s domain is a SET of six tenure kinds, `data/requires.py` carries `all`
# and no `any`, and §F.24a form 1 `existence` takes ONE `kind:` -- so `all` of the six would mean
# *a live edge of every kind at once*, which is the opposite requirement, and one `existence`
# would silently narrow the verb to one kind. Adding `any` is a GRAMMAR CHANGE (`REQUIRES_STEMS`
# is closed) and `04 §A.3` row 14 asks for a verb, not a form. The verb row states the same thing
# at its `requires_typed_note:` and closes with the condition under which this stops being true:
# *"IF AN `any` COMBINATOR IS EVER RULED, THIS CELL IS THE FIRST THING TO TYPE."*
# ⚠ `establish` (`13f`, 2026-09-25), `remit:`-eligible like `confer`, `revoke`, `dispatch` and `convene`. Its
# operands -- post, rung, remit, body/faction, conferral -- are not in `requires_operands`, and its
# clauses ask the `Office` constructor and `World.class_of`, neither of which is a grammar form.
# ⚠ `oblige` (position `17a`, 2026-09-29), an `own` row. Its clauses read
# `Office.binds` (no stem reads a seat's own field), the seat's occupant, and a NEGATION -- no live
# `oblige` already -- and the grammar has no `not`, the same wall `release`'s disjunction hits.
# ---------------------------------------------------------------------------
