"""`decision/` -- the `opening_set` member of `04_CODE_ARCHITECTURE.md` §A.2 (the `decision/` row), and its helpers.

⚠ **THE FILE IS `options.py` AND THE MEMBER IS `opening_set`, DELIBERATELY.** §A.2 (the `decision/` row) names four
members; a module named `opening_set.py` beside a function named `opening_set` makes
`decision.opening_set` ambiguous -- `__init__.py`'s re-export shadows the submodule -- and the
rebind surface needs the MODULE by name. "Option set" is the tree's own existing phrase for what
this returns, so the filename is idiomatic rather than coined (`CLAUDE.md` §4).

`opening_set` and its operand machinery (`operands_for`, `_derive_operand`, `_REFERENT_OPERANDS`,
`containing_rung_of`, `store_kind_of`, `_from_content_claim`, `_from_shortfall_claim`), the
eligibility predicate, and the two agreement/standing readers.

⚠ `entrenchment` SITS HERE PROVISIONALLY AND L3 RE-ADJUDICATES IT. `budget` and `opening_set` are
named by §A.2 (the `decision/` row) as `decision/` MEMBERS and cannot move to `queries/person_q`.
`entrenchment` is the one function here that §A.2 does not name, so it is the only real
`queries/person_q` candidate in this file, and L3 owns that call.

AX-2 binds every file under `decision/`: no `World`, as an import, a name, an attribute or a
string. Enforced BY PATH over this directory (`04 §E.1`).
"""

from __future__ import annotations

import itertools
from typing import Any, Callable, Optional
from ..data.rosters import RIG_KEY, RIG_LEVELS, STANCE_MAX
from ..data.requires import (
    OWN_STATE_STEMS, RECORD_SOURCED_OPERANDS, SENSITIVITY_STEMS, SHORTFALL_PREDICATE,
    SHORTFALL_SOURCED_OPERANDS, VIA, binding_of, evaluate,
)
from ..data.rosters import (
    CHALLENGE_KIND, COVERT_KINDS, PURSUIT_AXES, SUCCESSIONS,
    FACTION_BY_PROP, refusable, refusing_pole, require_member,
)
# `align` is imported, never `ALIGNMENT`: the table's one binding is `data.verbs.ALIGNMENT`, which the
# `H-66` sweep rebinds, and `align` reads it there.
from ..data.verbs import (
    CHOICE_RANGES, CHOICE_SOURCED, CITED_KEY, CITES_KEY, CONTEXT_KEY, CONTEXT_TERMS, CONCLUDED_KEY, CONCLUDED_RANK_KEY, CONCLUDING_VERBS, DETAINEE_CLASS, DISPOSAL_EVENTS, ELIGIBILITY_KINDS, ENEMY_CLASS, FILING_VERBS, HELD_DOCUMENT_DECLINES, HELD_EDGE_DECLINES, HELD_EDGE_SOURCED, LEDGER_RANGES, LIE_VERBS,
    OPPOSED_WITHOUT_PRIZE, OWN_EDGE_DECLINES, OWN_STANCE_DECLINES, RIGGED_VERBS, SAID_KEY, SAID_RANK_KEY, OWN_TITLE_DECLINES, RECORD_SUBKINDS_BY_VERB, RECORD_SUBKINDS_HELD,
    TERMS_SOURCED, VERB_TABLE, VIOLENCE_CONTEXTS, VIOLENT_VERBS, VOCATION_SOURCED, VOCATIONS, WARRANT_SOURCED,
    align,
)
from ..gaps import Forbidden
# B11.21: `agreement` .. `teller_weight` and `belief_contradicts` are `queries/person_q.py`'s now (`loop/witness.py` reads two of them and may not
# import `decision/`); re-bound here by name, as `opening_set` and `standing_of` call them and the tests reach them as `options.<name>`.
from ..queries.person_q import (
    BOND_STEM, PAIRED_KINDS, LedgerReader, OwnStateReader, addressed_to, agreement, attackers_of, belief_contradicts, channel_remove,
    cited_said, commanded_read, contradicts, competence, conclusion_cites, content_kind, content_said, decisiveness, dissents, held_against, known_persons, ledger_names, ledger_range,
    held_cites, is_cell as _is_cell, ledger_weigh, lie_said_of, projected_axes, rank, record, refracted_confidence, regard, said_of, said_set,
    teller_weight, telling_hearers,
    _judgement_factor, _judgement_rows,
)
from ..state.carriers import Act, Candidate, Claim, Person, Question, Record, View, fade_of, in_custody
from ..trace_log import TRACE

# v9 IN-12 step 7: THE CLASS A HELD WRIT RIDES THE QUESTION AS -- the carrier's own type name, which is
# what `queries/world_q.py::_stamped` stamps for a document (`World.class_of`) and what
# `rosters.yaml: referent_classes` declares; read off the type, never spelt.
_HELD_WRIT_CLASS = Record.__name__

# The Event kinds a bench's disposal emits (`rosters.yaml: own_edge_declines`' `DISPOSAL_EVENTS` values), as a set for the per-claim membership test.
_DISPOSAL_KINDS = frozenset(DISPOSAL_EVENTS.values())


def _hears_by_presence(row: "VerbRow") -> bool:
    """WHETHER `row`'s CELL CARRIES A `with` CONJUNCT ON `to` -- the hearer must be with the actor (`tell`'s, `lie`'s, `give`'s,
    `argue`'s and `accept`'s cells). `VerbRow.with_operands` is the one reader of the conjunct (B11.69); this asks it of `to`."""
    return "to" in row.with_operands()


def opening_set(p: Person, v: View, q: Question, fx: "Fixtures") -> list[Candidate]:
    """§F1 -- COMPUTED FROM THE VERB TABLE. No `roster` parameter: that is `D2` entire.

    `questions_for()` produces `q`, so the set is computed from it:

        { Candidate(verb, subject, operands) :                   -- §F1's `why`: gone, `14`
            verb    in the verb table                            -- clause 1
          , eligibility(verb, p) holds                           -- clause 2
          , subject in referents(q)                              -- clause 3
          , requires(verb) not KNOWN-FALSE from p's OWN claims    -- clause 4
          , every operand requires(verb) names is DERIVABLE }     -- `W-C`, `H-94`

    ⚠ THE FIFTH LINE IS NOT A FIFTH CLAUSE OF §F1 AND MUST NOT BE READ AS ONE. Clauses 1-4
    are the design's; this is the instrument declining to MINT AN ACT WITH A HOLE. The
    difference matters because the two have opposite polarities: a clause of §F1 narrows what
    a person is willing to attempt, and this narrows what the person can COHERENTLY SAY. An
    act missing an operand is refused by the fold for the instrument's reason, and `W-B` will
    deposit that refusal as a belief -- so forming it would put a fabricated fact about a
    granary nobody named into every witness's ledger. `operands_for` traces every decline, so
    the count is measurable rather than inferred from a verb's absence.

    ⚠ `fx` IS THE FOURTH PARAMETER AND IT IS `budget`'s PRECEDENT, NOT A WIDENING. §F1 types
    this `opening_set(p, view, q)`. `Fixtures` is the PARAMS REGISTRY -- flat numbers, no
    entity, identical for every person in the season, assigned to `params` by #353 §22 -- and
    `Query.budget` already takes one for exactly this reason, with the argument written out
    there. Two of `transfer`'s operands (`kind`, `amount`) are values the design supplies NO
    number for, so they are fixtures with a register row and a sweep (`H-94`), and a person
    who cannot reach the registry cannot derive them. What §F1's signature is protecting is that no
    AUTHORED OPTION LIST reaches here (`D2`); a params registry is not one, and the AST proof
    still sees no `World`.

    ⚠ CLAUSE 4 IS THE EPISTEMIC DESIGN AND IS NOT "requires holds". §F1: the person filters on
    WHAT THEY BELIEVE, "so a person who *wrongly* believes the granary full still forms the
    Candidate, acts, and gets `transfer.refused` from the fold. That is T3 and L2 working; a
    filter on world truth would be `choose` reading the world." Jordan, 2026-09-02: *"our
    understanding of all other words and actions is subjective and singular."* So the test is
    KNOWN-FALSE — a claim the person holds that contradicts the requirement — and NOT
    "unproven". Absence of a belief is not a belief in the negative.

    `remit:` is evaluated person-side off the `hold` Tenure's granted acts, and `presence:` is
    the only eligibility kind that still declines unconditionally (`person_side_eligible`)."""
    TRACE.query("opening_set", "person")
    out: list[Candidate] = []
    tick, decay = fade_of(p)     # B09.01: his claims are read at his tick, faded (`state/ledgers.py::present_confidence`)
    weigh = ledger_weigh(p, fx, tick)
    # Own-ledger reads every row asks alike, computed at most once per call and only when a row
    # needs one: `ledger_names` for a `referent_named` row, `known_persons` for a fanned row's bags.
    named: Optional[frozenset] = None
    people: Optional[tuple] = None
    hearers: Optional[tuple] = None     # B11.08, B11.69: `telling_hearers`, for a row whose cell has a `with` conjunct (on `to`: the fan; on `subject`: the referent)
    records: Optional[list] = None
    held: Optional[frozenset] = None
    read: Optional[dict] = None         # `documents_known_as`, once per call, only if a sub-kind row is reached
    # v9 IN-26 (`H-156` option (a) as a switch, `Fixtures withheld_verbs`): A VERB HELD OUT OF FORMATION
    # forms no Candidate for anybody, before any other read -- so a withheld row costs the season nothing
    # and the hand-built fold, which never asks this, is untouched. A member the table lacks is refused,
    # not ignored: a misspelt hold would release the verb it meant to withhold.
    withheld = frozenset(fx.get("withheld_verbs") or ())
    if not withheld <= VERB_TABLE.keys():
        raise Forbidden(
            f"`Fixtures withheld_verbs` names {sorted(withheld - VERB_TABLE.keys())}, which the verb table "
            "lacks", "H-156", needs="`verb_table.yaml` verbs only",
            law="IN-26 -- a withheld verb is one the table forms; a name it lacks withholds nothing")
    for verb, row in sorted(VERB_TABLE.items()):
        if verb in withheld:
            continue
        # v11 CR-27 (M9 taken (a), `rosters.yaml: lie_verbs`): A ROW THAT SAYS A FALSE VALUE IS FORMED ONLY WHILE
        # `Fixtures lie_offered` is True, and the gate is HERE, in formation, not in `loop/driver.py::
        # resolvable_verbs()`: a hand-built `lie` still folds, and the person simply does not offer it.
        if verb in LIE_VERBS and not fx.get("lie_offered"):
            continue
        if not person_side_eligible(p, row):
            continue
        # v9 PC-06 K-3 (`H-85`): A ROW WHOSE CELL ASKS THE ACTOR'S OWN STATE FORMS ONLY WHERE HIS OWN
        # STATE ADMITS IT -- `thread_read`'s Thread Sensitivity gate, read off the cell's stems
        # (`OWN_STATE_STEMS`), never off a verb name. Canon's verb-level statement is *TS >= 30
        # required* (`fieldwork_v30.md` §4.2; reference, not the mechanism). §2.2's *cannot attempt*
        # governs the attribute gates, and ED-FI-0009's retraction withdrew reading it as verb
        # availability; that a person below the gate does not FORM the act is THIS branch's reasoning
        # and its test -- so a person below it, or with no authored value, never forms the
        # Candidate, rather than forming it and being refused. The polarity is
        # NOT clause 4's (known-false declines, unknown forms): his sensitivity is not a belief about
        # the world he can be wrong about, the self-contest decline's reasoning below. The SAME cell,
        # asked of the same answerer the fold delegates to (`OwnStateReader`), so the two cannot
        # disagree; `build_typed_requires` refuses a cell mixing these stems with any other.
        # B10.59 (`02_CHAR_offer_what_can_be_done` edits 1-2): THE SAME READ, NOW FOR EVERY ROW WHOSE CELL ASKS ANY OWN-STATE STEM
        # (`held_by`, `dispute`, `individual` of the actor, beside the sensitivity pair), and asked BELOW, once the Candidate's
        # own operands are bound -- a cell over `subject` cannot be read before there is one. A cell of the sensitivity pair ONLY
        # (`thread_read`) keeps `is not True` (no authored value is UNKNOWN and declines); every other cell declines on `False`
        # alone, so a conjunct this reader cannot answer (UNKNOWN) still forms the Candidate, and clause 4 and the fold keep
        # theirs. Not a decline on a skill: there is no `capability` stem (A-11).
        own_stems = set(row.requires_typed.stems()) if row.requires_typed is not None else set()
        own_read = bool(OWN_STATE_STEMS & own_stems)
        own_only = own_read and own_stems <= SENSITIVITY_STEMS
        # B10.24: THE DEONTOLOGICAL GATE IS NOT HERE. It moved to `choose.make_ranker`, after scoring and before the sample, so the
        # struck candidate's score is known and the Scene can keep what was given up (`Scene.forgone`).
        # v9 IN-12 step 10 (`rosters.yaml: held_document_declines`): A VERB A PERSON DOES NOT FORM WHILE HE
        # HOLDS A DOCUMENT OF A NAMED KIND ABOUT HIMSELF -- `conceal` while he holds a cover (#453 §9.3's
        # person-side decline). His own Tenures and own ledger, no World (`holds_own_document`).
        held_kind = HELD_DOCUMENT_DECLINES.get(verb)
        if held_kind is not None and holds_own_document(p, held_kind):
            continue
        refs = row.referents_of(q)
        # v9 IN-12 step 7 (`rosters.yaml: terms_sourced`): A VERB THAT MAY FORM ON WHAT A HELD WRIT SAYS
        # forms, beside its own referents, on the `terms` of each writ this question carries as a held
        # `Record` (`writs_held`'s stamp) whose kind the roster names -- read off the person's OWN content
        # claim (`held_record_claims`, `record_sourced_operands`' `subject` key), so a covenant's addressee
        # forms `commit` on its Proposition once he holds it. The writ is the referent; a question that
        # carries none adds nothing, and `refs` is unchanged.
        terms_kinds = TERMS_SOURCED.get(verb)
        if terms_kinds:
            writs = q.referents_for(_HELD_WRIT_CLASS)
            if writs:
                if records is None:
                    records = held_record_claims(p, tick, decay)
                # v10 IN-12 step 5a: ONLY A DOCUMENT ADDRESSED TO HIM (`person_q.addressed_to`, the one
                # owner `writs_held` asks too) -- a petitioner holding his own petition is not who it
                # asks, and forms nothing on its `terms`. A writ reached here only through `writs_held`'s
                # addressee stamp, so for a dispensation this narrows nothing.
                said = (_content_answer(c, "subject") for c in records
                        if c.subject in writs and content_kind(c) in terms_kinds
                        and addressed_to(content_said(c), p.id))
                refs = tuple(refs) + tuple(t for t in dict.fromkeys(said)
                                           if t is not None and t not in refs)
        # B10.72 (`rosters.yaml: held_edge_sourced`): A VERB THAT FORMS ALSO ON THE OBJECT OF A LIVE EDGE HE HOLDS -- `release` on a
        # `commit` of his own, which no question is about (the `need` question names the seat's holder). His own live Tenures, no
        # World; it ADDS the objects he holds and nothing else, so a person committed to nothing forms what he formed before.
        sourced_kind = HELD_EDGE_SOURCED.get(verb)
        if sourced_kind is not None:
            # NOT A FACTION MEMBERSHIP (a `commit` whose object is a faction, `fac_...`): releasing it is leaving the faction, and
            # at lap 0 every cast person did, so `holder_faction_of` read None and a march folded `field.unopposed` (B10.99's
            # bisect of test_in36_foreign and test_task_draw to B10.72). Release stays for a commit to a Proposition.
            mine = tuple(dict.fromkeys(t.object for t in p.tenures if t.kind == sourced_kind and t.live
                                       and t.object not in FACTION_BY_PROP))
            refs = tuple(refs) + tuple(o for o in mine if o not in refs)
        # v12 B11.72 (`08_FI_07` §2 (a); `rosters.yaml: choice_sourced`'s `ledger_ranges`): A VERB WHOSE `site` IS CHOICE-SOURCED (`examine`) ALSO FORMS ON EACH ID HIS
        # OWN LEDGER PRESENTS AS A SITE (`person_q.ledger_range`) -- the place he has heard of, which is not what any question is about. His own claims and no
        # World; it ADDS referents and nothing else, `site` binds the referent as ever (`_derive_operand`), and whether the id is a Site and whether he
        # stands at it are the fold's `existence` and `present_at`. [ASSUMPTION; medium; Jordan to correct; revert: the question's subject.]
        for key in CHOICE_SOURCED.get(verb, ()):
            if key in LEDGER_RANGES:
                refs = tuple(refs) + tuple(r for r in ledger_range(p.ledger, key) if r not in refs)
        # B10-09 close one, D3 (`rosters.yaml: held_edge_declines`): A VERB A PERSON DOES NOT FORM ON AN OBJECT
        # HE ALREADY HOLDS A LIVE EDGE OF THE NAMED KIND ON -- `commit` on a Proposition he commits to
        # (`_eff_commit` always opens a fresh Tenure). After every widening above, so it covers each route
        # that carried the referent. His own live Tenures, no World. It NARROWS and widens nothing.
        edge_kind = HELD_EDGE_DECLINES.get(verb)
        if edge_kind is not None and refs:
            on = {t.object for t in p.tenures if t.kind == edge_kind and t.live}
            refs = tuple(r for r in refs if r not in on)
        # v9 IN-12 step 13 (`rosters.yaml: own_stance_declines`): A VERB A PERSON FORMS ONLY ON A REFERENT HE
        # HOLDS A ROW AGAINST -- `forgive` (#453 §9.4's person-side own-state decline). His own stance rows
        # (`person_q.held_against`, the reader the effect reads too), no World. It NARROWS the referents the
        # question carries and widens nothing (§F1 clause 3 stands).
        if verb in OWN_STANCE_DECLINES:
            refs = tuple(r for r in refs if held_against(p, r))
        # v11 CR-87 (`rosters.yaml: violence_contexts`, ED-IN-0337): A VERB A PERSON FORMS ONLY ON A SUBJECT HE
        # HOLDS A CONTEXT OF VIOLENCE AGAINST -- `fight` (war, crime, duel, defence; `violence_context_of`). His
        # own Tenures, ledger and the question he answers, no World. It NARROWS and widens nothing.
        contexts = VIOLENCE_CONTEXTS.get(verb)
        if contexts and refs:
            if records is None:
                records = held_record_claims(p, tick, decay)
            memo: dict = {}          # what a reader derives from the actor alone, once per call, not once per referent
            # B15.08 (PHY_A A3): THE CONTEXT THAT ADMITTED A REFERENT RIDES ITS CANDIDATE (`CONTEXT_KEY`), the first of the line that holds
            # (`violence_context_of`, the one reader), for `combat_input` to read the fight's terms by (`rosters.yaml: context_terms`).
            context_of = {r: violence_context_of(p, q, r, contexts, records, memo) for r in refs}
            refs = tuple(r for r in refs if context_of[r] is not None)
        # v9 IN-26 (`A-13`): A VERB A PERSON FORMS ONLY ON A REFERENT HE HIMSELF HOLDS (`destroy_record`, `give`, `carry`,
        # `found`, `build`) is declined BELOW, with the rest of what he reads off himself: its cell's `held_by` conjunct is
        # asked of `OwnStateReader` (B10.59), which reads his own live `hold` Tenures. B10.61 deleted the roster that did
        # it here (`own_hold_declines`): the two readings gave the same candidate set on every person, seeds 0-2.
        # v10 IN-61 (`rosters.yaml: own_title_declines`, RS-27): A VERB A PERSON FORMS ONLY ON A SEAT WHOSE
        # `successions` TITLE HE HIMSELF HOLDS -- `succeed`, the person-side reading of the claim's title
        # conjunct (`state/gate.py::may_claim`). His own live `hold` objects against the roster (the law,
        # not world state), no World. It NARROWS and widens nothing; the seat's vacancy stays the fold's.
        if verb in OWN_TITLE_DECLINES:
            if held is None:
                held = _held_objects(p)
            refs = tuple(r for r in refs if any(t in held for t in SUCCESSIONS.get(r, ())))   # B21.16: any listed title
        # VB-A commit A1 (B21.07, `rosters.yaml: own_edge_declines`): A VERB A PERSON FORMS ONLY ON A REFERENT HE IS TIED TO BY A
        # LIVE EDGE OF A KIND THE ROW'S OWN `domain:` NAMES -- `release`, which the fold refuses on any referent he owns no
        # releasable edge toward (a person releasing the King, a cohort the settlement it lives in): no scene is spent on a refusal
        # of the row's conjunct he could have known. His own live Tenures, no World. It NARROWS and widens nothing; the
        # predicate is unchanged and stays the fold's check. (After every widening above, `held_edge_sourced`'s too.)
        kinds = OWN_EDGE_DECLINES.get(verb)
        if kinds is not None and refs:
            live = [t for t in p.tenures if t.kind in kinds and t.live]
            tied = {t.object for t in live}
            refs = tuple(r for r in refs if r in tied)
            # VRES §4 edit 1 (A-37; the formation half, the fold's being `loop/predicates.py::_req_release`): A PARTY DOES NOT RELEASE
            # AN EDGE A BENCH IMPOSED, so a referent he holds a claim of a determination on, naming his own edge to it, is dropped.
            # The claim is the generic Event claim (`loop/witness.py`): `subject` the disposal edge's id, `predicate` the Event kind
            # (`DISPOSAL_EVENTS`), `value` True -- it names the judge and the edge and never the party, whose own `tenures` say the
            # edge is his. `decision/` never reads the log (`04` §B.9: `state/acts` is resolver-side): his own ledger and Tenures only.
            if refs:
                found = {c.subject for c in p.ledger if c.predicate in _DISPOSAL_KINDS}
                imposed = {t.object for t in live if t.id in found}
                refs = tuple(r for r in refs if r not in imposed)
        # B11 lane A (`data/verbs.py::RECORD_SUBKINDS_BY_VERB`): A `Record` ROW WHOSE CELL ASKS A SUB-KIND forms only
        # on a Record his own content claims say is of that kind (`documents_known_as`) -- `accept` on a challenge,
        # `comply` on a dispensation. The kind is read off the row's own cell, never a verb name; a document is known
        # by what it says, so one he holds no reading of is no challenge to him (the addressee of a challenge made
        # before him reads it, `loop/witness.py`'s content deposit). It NARROWS and widens
        # nothing; the fold's `existence` conjunct stays for a hand-built act. [ASSUMPTION; medium; Jordan to
        # correct; revert: empty `RECORD_SUBKINDS_BY_VERB`.]
        # A HOLDING row (`RECORD_SUBKINDS_HELD`: `carry`, `found`, `build`, held by the person, whose own `held_by` reading is `OwnStateReader`'s) keeps
        # a document he holds no reading of -- unknown forms, clause 4's polarity -- and declines one his reading says is
        # of another kind.
        kinds_asked = RECORD_SUBKINDS_BY_VERB.get(verb)
        if kinds_asked and refs:
            if read is None:
                read = documents_known_as(p)
            if verb in RECORD_SUBKINDS_HELD:
                refs = tuple(r for r in refs if r not in read or read[r] & kinds_asked)
            else:
                refs = tuple(r for r in refs if read.get(r, frozenset()) & kinds_asked)
        if not refs:
            continue
        # v9 IN-12 step 9 (`rosters.yaml: vocation_sourced`): A VERB THAT CARRIES A VOCATION forms one
        # Candidate per vocation in the RANGE -- `verb_capability`'s values (`data/verbs.py::VOCATIONS`,
        # #453 K-20) -- the key riding on the roster's operand. ⚠ NEVER THE ACTOR'S OWN `capability`:
        # capability GATES NOTHING (#353 §9.2, probe P11, which zeroes it and asks that the option set not
        # move), so whether a training lands is the effect's (the subject must already hold the key, J-13
        # (iii)), not a formation the actor's dice decide. A row the roster does not name is untouched.
        voc_operand = VOCATION_SOURCED.get(verb)
        vocations = ()
        if voc_operand is not None:
            vocations = tuple(sorted(VOCATIONS))
            if not vocations:
                continue
        # v9 IN-12 step 6 (`rosters.yaml: warrant_sourced`): A VERB WHOSE SUBJECT COMES FROM A WARRANT
        # forms only on a referent a HELD record of the warrant kind names -- IN-10's held-Record
        # channel (`held_record_claims`, answered through `record_sourced_operands`' `subject` key),
        # the person's own Tenures and own ledger and no World. It NARROWS the referents the question
        # carries and widens nothing (§F1 clause 3 stands), so `seize` is never formed for a seat that
        # holds no warrant naming what it was asked about.
        warrant_kind = WARRANT_SOURCED.get(verb)
        warranted = None
        if warrant_kind is not None:
            if records is None:
                records = held_record_claims(p, tick, decay)
            warranted = {_content_answer(c, "subject") for c in records
                         if content_kind(c) == warrant_kind}
        # `19`: the seat(s) this row's act would exercise -- the untraced walk `pack_scenes` names
        # `Act.via` by (`seat_of`) -- for the belief test's `basis` conjunct below.
        # `H-134`: WHERE THE ADMITTING `remit:` ALTERNATIVE IS GRANTED BY SEVERAL OF THE PERSON'S
        # SEATS, EACH IS A SEAT THE ACT CAN BE EXERCISED THROUGH, and the Candidate is formed once
        # per seat (below) -- the fold's gate asks the one seat the act names. No seat is picked FOR
        # the person: the seat-Candidates score and draw alike (`choose.py` keys both on
        # `(verb, subject)`), so Tenure order still orders them in the ranking. One seat (or none)
        # leaves `seats` a single value that is `exercised_seat` exactly, and nothing below differs.
        seats = exercisable_seats(p, row)
        # `T4`: only a NAMED own-ledger conjunct carries `said` (`tell`'s `holds`, and since IN-10
        # `issue`'s `terms`, which nothing reads `said` off -- the row's note); `survey` and
        # `reconstruct` share the form unnamed and carry nothing (telling workplan, "From Batch 1").
        ledger_of = row.requires_typed.named_own_ledger_operands() if row.requires_typed else ()
        opposes_subject = subject_is_opponent(row)
        cites_of = verb in FILING_VERBS and CITES_KEY in CHOICE_SOURCED.get(verb, ())      # B24.27: a filing verb whose choice line names `cites` forms a citing variant
        said_of_entity: dict = {}           # entity -> `said_of` (this row's own-ledger read, per entity)
        concluded = None                    # B11.73: `conclusion_cites` of his own ledger, read once per call for a row that reports a conclusion
        # IN-10 (a) (H-203): a row declaring `referent_named` forms only on a classed referent the
        # person's OWN LEDGER names (`person_q.ledger_names`: a deposit, or a held document's
        # `terms`) -- `oblige` on a seat he was told of, never on a vacancy a world read stamped.
        # Own state, no World; computed once per call, only if such a row has a referent.
        if row.referent_named and named is None:
            named = ledger_names(p.ledger)
        told = named if row.referent_named else None
        # IN-53 (H-207, DECISION 2026-10-13 D1): THE CLASS IS A PARTITION. A row declaring a
        # `referent_class:` iterates only the referents the question carries as that class; a row
        # declaring none iterates the plain `referents`, exactly as before (`VerbRow.referents_of`,
        # `Question.referents_for`) -- no World, no id test, no verb name, because this function
        # cannot ask what kind of thing an id is (L2).
        # v12 B11.69 (`14_VERBS_SOCIAL1_A` edit 3): A ROW WHOSE CELL ASKS ITS `subject` TO BE WITH THE ACTOR (`tend`, `train`, `fight`, `capture`,
        # `challenge`) forms only on a referent his OWN ledger places with him -- `telling_hearers`' reading, the one reader of believed co-location
        # (`known`, the control, is every person he knows, so it drops none). Read off the cell (`VerbRow.with_operands`), never a verb name; the
        # fold's `with` stays world-only, so a man who is wrong is still refused there. TWO KEPT: a person stands with himself, and a referent he
        # does not know at all -- no belief places him elsewhere, and clause 4's polarity is that only a belief declines (`to` is fanned over known persons alone).
        with_subject = "subject" in row.with_operands()
        for subject in refs:
            if told is not None and subject not in told:
                continue
            if warranted is not None and subject not in warranted:
                continue
            if with_subject and subject != p.id:
                if hearers is None:
                    hearers = telling_hearers(p.ledger, p.id, fx)
                if people is None:
                    people = known_persons(p.ledger, p.id)
                if subject in people and subject not in hearers:
                    continue
            # ⚠⚠ A CONTEST NEEDS TWO CLAIMANTS, AND A PERSON IS NOT THEIR OWN ADVERSARY.
            # `move`'s `contain_path` cell keeps the same shape of rule -- *"a node is not a path
            # to itself"* -- as the reader's own, and this is that rule one seam over. It reads
            # the ROW'S OWN COLUMN (`contests:`), never a verb name, so it holds for whatever
            # else declares a prize later. `opening_set` offers every person THEMSELVES as a
            # referent for every verb, so without this a person attacks himself.
            #
            # ⚠ WHY IT DECLINES HERE RATHER THAN REFUSING IN THE FOLD, which is the opposite of
            # the choice clause 4 makes: clause 4 is EPISTEMIC -- a person who wrongly believes
            # the granary full SHOULD form the Candidate and learn otherwise -- and being alone
            # in a room is not a belief anyone can be wrong about. There is no world-read here
            # and no `World`: `p.id` against a referent the person already holds.
            # ⚠ ONLY WHERE THE ROW'S SECOND SIDE IS ITS SUBJECT (telling workplan `T4`, Decision 3;
            # CR-16: no `counterparty:`, or `counterparty: subject`). A row that names its second
            # side on another operand contests against THAT (`tell`'s `to`),
            # so its `subject` is a topic and a person may tell somebody about themselves; the
            # counterparty rule below still declines the person as their own second side.
            # CP-T05-02 (iii): ...EXCEPT A ROW DECLARING `subject_may_be_self` (`speak`: a person may answer for himself; the
            # fold admits it only for a docketed party). The column is the row's own, never a verb name.
            if opposes_subject and subject == p.id and not row.subject_may_be_self:
                continue
            # ⚠ OPERANDS BEFORE THE BELIEF TEST, AND THE ORDER IS THE POINT. Clause 4 asks
            # whether the requirement is known-false ABOUT THIS BINDING, so the binding has to
            # exist first -- asking it of an unbound cell is what made the person read a
            # different granary from the fold.
            # `T4`: ONE CANDIDATE PER BAG -- one bag for every row but one whose `to` is a KNOWN
            # PERSON (`operand_bags`), which forms one per person the teller knows.
            # `H-134`: seat-major, each seat's own bags (`from` is that seat's rung). One seat: the
            # one pass `operand_bags` made before.
            # IN-10: and the Records the person holds, whose addressees a fanned row's bags add.
            # v12 B11.08 (`08_FI_02` edit 5): A ROW WHOSE CELL CARRIES A `with` CONJUNCT ON `to` (`tell`, `lie`, `give`, `argue`, `accept`) OFFERS
            # ITS ACT TO THE PERSONS `Fixtures telling_hearers` names -- `known` (the control) or `seen_since_move`; every other fanned
            # row ranges over everybody he knows.
            fanned = None
            if row.known_person_operands():
                if _hears_by_presence(row):
                    if hearers is None:
                        hearers = telling_hearers(p.ledger, p.id, fx)
                    fanned = hearers
                else:
                    if people is None:
                        people = known_persons(p.ledger, p.id)
                    fanned = people
                if records is None:
                    records = held_record_claims(p, tick, decay)
            bagged = [(st, ops) for st in (seats or (None,))
                      for ops in operand_bags(p, row, q, subject, fx, seat=st, people=fanned,
                                              records=records, tick=tick)]
            if vocations:                   # IN-12 step 9: one bag per vocation carried (above)
                bagged = [(st, {**ops, voc_operand: k}) for st, ops in bagged for k in vocations]
            for st, ops in bagged:
                # ⚠ AND A TWO-SIDED ACT NEEDS A SECOND SIDE (plan position `15`, `ED-IN-0210` ruling
                # 2). The rule above, one column over: a row naming its `counterparty:` operand forms
                # no Candidate whose counterparty is the person -- a petition to oneself is the
                # Tenure(X,X) fiat ruling 1 names. Declined HERE, not refused in the fold, for the
                # reason the contest rule gives: no read the fold makes can say *that is you*, so a
                # refusal teaches nothing: it feeds itself (the refusal's claim about the
                # petitioner raises the next question about them). Reads the row's column, never a
                # verb name, and the loader guarantees the operand is carried.
                # ⚠ AND A SECOND SIDE NOBODY CAN NAME IS NO SECOND SIDE (plan position 16). On a TYPED
                # row the loader guarantees the counterparty is carried, so `None` cannot arise there.
                # On an UNTYPED row (`give` until plan position `14` typed it; `oblige` carries its
                # `subject` since IN-10 (a)) nothing may be carried, and forming the Candidate would mint an act with no second party --
                # refused by the fold every time, for the instrument's reason, and each takes a
                # scene -- *a constant scene tax with nothing behind it*.
                # IN-53 D2: the self half waived for a row declaring `counterparty_may_be_self`
                # (`VerbRow.self_counterparty_refused`, the one owner the fold asks too).
                if row.counterparty and row.self_counterparty_refused(ops.get(row.counterparty), p.id):
                    continue
                # B10.59: WHAT HE CAN READ OFF HIMSELF, ASKED OF THIS CANDIDATE'S OWN BINDING (the K-3 branch above says why).
                # B10.64, B10.65: `believes=True` -- the PERSON'S answer for a key in `SELF_BELIEVED` is his own `self:<key>` claim (read by `weigh`, so a claim he was told is
                # graded by his regard for the teller), so the two readers differ for him alone and by design: he does not deliberately read a Thread he does not know he
                # reads, and a hand-built act still folds.
                if own_read:
                    own_verdict = evaluate(row.requires_typed, OwnStateReader(p, fx, believes=True, weigh=weigh), binding_of(p.id, ops)).value
                    if own_verdict is False or (own_only and own_verdict is not True):
                        continue
                # `19`: THE SEAT THE ACT WILL BE EXERCISED THROUGH rides into the belief test as it rides
                # onto `Act.via` (`pack_scenes`), so a `basis` conjunct is asked of the same seat both
                # sides. `st` is the seat this Candidate is formed for.
                # `T3a`: and the person reads their own ledger WEIGHING hearsay by its teller.
                if belief_contradicts(p, row, subject, ops, st, weigh=weigh, tick=tick, decay=decay):
                    continue
                # WHAT THE TELLER WILL SAY IS DECIDED HERE, AT CHOOSE, AND RIDES THE ACT (`T1`,
                # `workplans/2026-10-01-telling-workplan.md`): a row whose typed cell holds a NAMED
                # `own_ledger` conjunct (`T4`; found by walking the form, never by a verb name)
                # passes on what the actor HOLDS about the clause's entity, copied out of their own
                # ledger now, so WITNESS reads the Act and never the teller's live ledger. Placed
                # after every decline so the copy is paid only for a Candidate that is formed;
                # `said` is not a `requires_operands` member, so `binding_of` drops it from both
                # readers' bindings.
                # ⚠ AND NOTHING TO SAY IS DECLINED: a telling that carries nothing passes nothing on,
                # and the fold would refuse it on `holds` -- a scene spent on a refusal the person could
                # have known. Only the named conjunct declines; `survey` and
                # `reconstruct` carry no `said` and are untouched.
                saids: tuple = (None,)
                if ledger_of:
                    # `said` depends on the entity alone, never on the hearer, so a subject's
                    # telling is read once however many hearers it fans to.
                    entity = ops.get(ledger_of[0])
                    if entity not in said_of_entity:
                        # CR-27: a row in `lie_verbs` says the claim FALSELY (`lie_said_of`), every other row
                        # says it as held (`said_of`); both are the actor's own ledger and nothing else.
                        # v12 B11.10 (`08_FI_02` edit 7): AND ONE CANDIDATE PER CLAIM -- the top `said_choices` the slant ranks (`said_set`).
                        # Only a row whose `choice_sourced` line names `said` ranges over several (`issue` shares the form and takes the one pick).
                        # v12 B11.54: a `lie` of an amount says it BOTH ways (`lie_said_of`'s tuple, spread by `said_set`), one Candidate each; the loop below forms them.
                        said_of_entity[entity] = said_set(
                            p.ledger, entity, fx, p, pick=lie_said_of if verb in LIE_VERBS else said_of, tick=tick, weigh=weigh,
                            choose=SAID_KEY in CHOICE_SOURCED.get(verb, ()))
                    saids = said_of_entity[entity]
                    if not saids:
                        continue
                # B11.73 (`08_FI_03` §3 act 1; FRES §7 (1)): A ROW THAT REPORTS A CONCLUSION (`CONCLUDING_VERBS`: `reconstruct`, read off its `emits:`) CARRIES WHAT HIS OWN
                # LEDGER LETS HIM CONCLUDE of this subject -- `(the one the deed was done to, deed kind, doer)`, `person_q._concluded`, fixed here as `said` is so WITNESS
                # reads the act and never his live ledger -- under `CONCLUDED_KEY`, and nothing where his ledger names no doer (the key is absent, the act folds as any
                # reconstruct). It is no operand (`binding_of` drops it) and no part of the act's id (`act_key`). Own ledger only, no World.
                # v12 B11.75 (`19_LACUNA` R-19-04, "Which doer"): AND WHERE HIS LEDGER NAMES SEVERAL, THE SUSPECT IS A CHOICE -- ONE CANDIDATE PER `(deed kind, doer)` (`conclusion_cites`,
                # `_concluded`'s reading in ledger order), each carrying the deed claims that name him under `CITES_KEY` (what a later `utter` of the conclusion cites and what
                # `settle_conclusions` weighs it by) and, where there is more than one, its place among them (`CONCLUDED_RANK_KEY`, so the acts' ids differ, as `said`'s do).
                # `decision/choose.py::settle_conclusions` keeps one. One doer is no choice: no rank, no rename.
                conclusions: tuple = (None,)
                if verb in CONCLUDING_VERBS:
                    if concluded is None:
                        concluded = conclusion_cites(p.ledger, p.id, COVERT_KINDS)
                    named_by = tuple((k, ids) for k, ids in concluded.items() if k[0] == subject)
                    if named_by:
                        conclusions = named_by
                for said_rank, said in enumerate(saids):
                    cand_ops = ops
                    if said is not None:
                        cand_ops = {**ops, "said": said}
                        if len(saids) > 1:       # a real choice: the rank is what the act's id and score read (`data/verbs.py::choice_values`)
                            cand_ops[SAID_RANK_KEY] = said_rank
                    # `H-134`: the seat rides on the Candidate ONLY where it was chosen among several,
                    # under `VIA` -- not a cell operand, so `binding_of` drops it (the seat reaches the
                    # binding as `via=`), exactly as `said` is dropped; `pack_scenes` reads it onto
                    # `Act.via`. A single-seat Candidate carries nothing extra: byte-identical.
                    if len(seats) > 1:
                        cand_ops = {**cand_ops, VIA: st}
                    # B24p.24: AND HOW HARD HE WOULD RIG THE SITTING, where the act carries a rig and he has the power to work one.
                    if verb in RIGGED_VERBS:
                        cand_ops = rig_offer(p, v, verb, subject, cand_ops, fx)
                    if contexts:                 # B15.08: the context that admitted this subject (set above where the decline reads it)
                        cand_ops = {**cand_ops, CONTEXT_KEY: context_of[subject]}
                    for place, concl in enumerate(conclusions):
                        c_ops = cand_ops
                        if concl is not None:
                            c_ops = {**cand_ops, CONCLUDED_KEY: concl[0], CITES_KEY: concl[1]}
                            if len(conclusions) > 1:
                                c_ops[CONCLUDED_RANK_KEY] = place
                        out.append(Candidate(verb, subject, operands=c_ops))
                        # B24.27 (EVID_B edit 6; FI_05_B E-1): AND THE SPEECH THAT CITES, where he holds claims about the matter a speech could be admitted on -- the one variant citing
                        # ALL of them (`held_cites`), each with the `Said` it carries (`CITED_KEY`, copied out of his own ledger now, as `said` is), and the Records he holds whose content names the matter (`held_record_claims`' `subject`, B24.43: a Record's id is cited, its content claim is the reading that names the matter). The variant above, citing nothing, is the
                        # speech as it was. It rides the same score terms; what it costs is the room learning the items and their chain (E-7).
                        # NEVER ON HIS OWN PLEA (`subject == p.id`): the ledger arm weighs the opponent's deeds and reads 0.0 where the opponent is the actor (`world_q.proofs`), so a citing variant there is a speech no proof backs.
                        if cites_of and subject != p.id:
                            held = held_cites(p.ledger, subject)
                            if records is None:
                                records = held_record_claims(p, tick, decay)
                            kept = tuple(dict.fromkeys(c.subject for c in records if _content_answer(c, "subject") == subject))      # B24.43: the Records he holds whose content names the matter
                            if held or kept:
                                out.append(Candidate(verb, subject, operands={**c_ops, CITES_KEY: tuple(c.id for c in held) + kept, CITED_KEY: {c.id: cited_said(c) for c in held}}))
    return out


#: The stake the arranger reckons a rig on (V2 p2 §H's `2 x stake x P(carried) - price`), in the fold's units: one, the unit V2's own grid of rig levels is
#: read at ("stakes up to 1"); the matter's worth to him is no number the tree holds (`Fixtures.stakes_ob` ships at its control, 0).
_RIG_STAKE = 1.0       # [canonical: V2 p4 §F 19 / §K C3 -- the rig levels' grid, "the 27-case grid at stakes up to 1"; ASSUMPTION; Jordan to correct]


def rig_worth(stake: float, odds: float, tilt: float, price: float) -> float:
    """WHAT A RIG IS WORTH TO THE MAN WHO WORKS IT (V2 p2 §H, p4 §F 19): `2 x stake x P(carried) - price x tilt^2`, `price` the fold's `rig_price`.
    The one formula, read by `rig_offer` for each level and by nothing else: the price is `price x tilt^2` whoever is in the room and it rises with the rig,
    so no level is dearer for being secret, and a rig of no tilt costs nothing and buys nothing."""
    return 2.0 * stake * odds - price * tilt * tilt


def best_rig(stake: float, readings: dict, price: float) -> float:
    """THE LEVEL THE RECKONING PICKS: of `readings`, `{level: (odds, tilt)}`, the level whose `rig_worth` is greatest, the lowest where two tie (a rig
    is worked for what it buys, never for itself). Every level of `RIG_LEVELS` is best somewhere: none where the stake is small, the half where a little
    of the tilt pays, the whole where the stake is large."""
    return max(readings, key=lambda r: (rig_worth(stake, readings[r][0], readings[r][1], price), -r))


def rig_offer(p: Person, v: View, verb: str, subject, ops: dict, fx: "Fixtures") -> dict:
    """`ops`, WITH THE RIG THE RECKONING PICKS WHERE HE HAS THE POWER TO WORK ONE (B24p.24; V2 p2 §H, p4 §F 19). The host answers what the room
    would be (`View.odds.arranged(act, rig)`: his believed odds that the matter carries and the tilt his rig gives the forum, from the one room
    `proceeding_input` builds); a tilt only where he has more power than the other party, so between equals (a tilt of 0 at the full rig) nothing is
    offered and `ops` is what it was. Where there is a tilt, each level of `RIG_LEVELS` is priced on `rig_worth` and the best is the one Candidate this
    forms (a level above 0 rides under `RIG_KEY`; the best being 0, the act carries none): the chooser then scores that act as it scores every
    other, so the rig is ranked with the rest of what he could do and never beside it. [ASSUMPTION; medium; Jordan to correct: the reckoning
    picks the level rather than forming one Candidate per level, which would share one act id (`data/verbs.py::act_key`) and score alike, the chooser's
    score having no price term to tell them apart.] A View that cannot ask (`odds` None, or one with no `arranged`) offers none."""
    ask = getattr(getattr(v, "odds", None), "arranged", None)
    if ask is None:
        return ops
    act = Act(f"rig:{verb}:{subject}", p.id, verb, payload={**ops, "subject": subject})
    top = ask(act, RIG_LEVELS[-1])
    if top is None or top[1] <= 0.0:
        return ops
    readings = {r: (top if r == RIG_LEVELS[-1] else ask(act, r)) for r in RIG_LEVELS}
    if any(x is None for x in readings.values()):
        return ops
    best = best_rig(_RIG_STAKE, readings, fx.get("fold_rig_price"))
    return {**ops, RIG_KEY: best} if best > 0 else ops


def subject_is_opponent(row: "VerbRow") -> bool:
    """WHETHER AN ACT OF `row` IS CONTESTED AGAINST ITS `subject` -- the row declares a prize
    (`contests:`) and its second side IS its subject: it names no `counterparty:`, or names
    `counterparty: subject` (`determine`'s party, `arrest`'s prisoner). The test itself is
    `VerbRow.contested_against_subject` (`data/verbs.py`, the fold's own opponent rule,
    `payload[row.opponent_operand()]`, asked by `loop/resolve.py::_contest` too); this name is kept for its
    readers. Read off the row's own columns, never a verb name. One owner for two readers:
    `opening_set`'s self-subject decline (a person is not their own adversary) and
    `decision/choose.py`'s score term 2 under `stance_polarity: declared` (v9 IN-18 `G2`: an act
    against a disliked opponent scores higher, not lower). B11 lane A: OR the row is listed in `rosters.yaml: opposed_without_prize` (`challenge`:
    no prize, done against the man it calls out)."""
    return row.opposed_to_subject(OPPOSED_WITHOUT_PRIZE)


# v11 CR-87: THE VIOLENT ROWS WHOSE SUBJECT IS THEIR OPPONENT (`data/verbs.py::VIOLENT_VERBS`, off `rosters.yaml:
# violent_prizes`, narrowed by `subject_is_opponent`): `fight` and `capture`. `accept` is violent and its opponent is
# `to` (PC-10b), so it is not in it (H-255). One owner for the conjunct the grudge bound (`choose.stance_term`), the
# DEFENCE deed kinds and the violence-decline import check each ask.
VIOLENT_OPPONENT_VERBS = frozenset(v for v in VIOLENT_VERBS if subject_is_opponent(VERB_TABLE[v]))


# v11 CR-87 (ED-IN-0337): THE CONTEXTS OF VIOLENCE, each a person-side reader `(p, q, subject, records, memo) -> bool`
# over the actor's own Tenures, his own ledger (`records`: `held_record_claims(p)`, computed once per
# `opening_set` call) and the question he answers -- never a World (AX-2). `rosters.yaml: violence_contexts`
# names which of them admit a verb; this mapping is the closed set of names (a fact of code: the readers).
_WARRANT_KINDS = frozenset(WARRANT_SOURCED.values())
VIOLENCE_CONTEXT_READERS: dict = {}


def _context(name: str):
    """Registers a context reader under its roster name (`data/requires.py::requirement_form`'s shape): the closed set
    of contexts is the set of readers defined here, one name each, and no list of names is written out."""
    def register(fn):
        VIOLENCE_CONTEXT_READERS[name] = fn
        return fn
    return register


@_context("war")
def _war_context(p: Person, q: Question, r: str, records: list, memo: dict) -> bool:
    """WAR: `r` is stamped `Enemy` on his question (`world_q.enemies_heard`: a war he knows of, `r` of the other
    faction)."""
    return r in q.referents_for(ENEMY_CLASS)


@_context("crime")
def _crime_context(p: Person, q: Question, r: str, records: list, memo: dict) -> bool:
    """CRIME: a warrant he holds, ADDRESSED TO HIM, names `r` (a held Record of a `warrant_sourced` kind, answered
    through `record_sourced_operands`' `subject` key -- the reading `arrest` forms on -- whose addressee is he,
    `person_q.addressed_to`, IN-12 step 5a's one owner), or `r` is stamped `Detainee` on his question (a live `detain`
    on a seat he holds: `arrest`'s and `capture`'s custody, `world_q.detainees_held`).
    THE ADDRESSEE TEST NARROWS "A WARRANT HIS SEAT ISSUED OR HOLDS" [ASSUMPTION; medium; Jordan to correct; revert:
    drop the `addressed_to` test]: a dispensation whose `terms` is a person is a warrant to the tree
    (`warrant_sourced`), so the maker of any writ about the King held a "warrant" against him. The man a warrant charges is its addressee, not its maker."""
    return (r in q.referents_for(DETAINEE_CLASS)
            or any(content_kind(c) in _WARRANT_KINDS and _content_answer(c, "subject") == r
                   and addressed_to(content_said(c), p.id) for c in records))


@_context("duel")
def _duel_context(p: Person, q: Question, r: str, records: list, memo: dict) -> bool:
    """DUEL: he holds a `challenge` Record (PC-10b) whose two parties -- its challenger (`to`'s key) and the
    challenged (`subject`'s), read through `record_sourced_operands` -- are himself and `r`, either way round."""
    pair = {p.id, r}
    return any(content_kind(c) == CHALLENGE_KIND
               and {_content_answer(c, "to"), _content_answer(c, "subject")} == pair for c in records)


@_context("defence")
def _defence_context(p: Person, q: Question, r: str, records: list, memo: dict) -> bool:
    """DEFENCE [ASSUMPTION; medium; Jordan to correct; revert: drop `defence` from the roster]: he saw `r` do to him,
    in the newest season his ledger holds, a deed of a kind a violent opponent-rule row emits (`person_q.attackers_of`,
    `_OPPONENT_DEED_KINDS` below)."""
    if "attackers" not in memo:        # depends on the actor alone, never on `r`: one ledger pass per call
        memo["attackers"] = attackers_of(p.ledger, p.id, _OPPONENT_DEED_KINDS, strata=_OPPONENT_STRATA)
    return r in memo["attackers"]


# The deed kinds a DEFENCE reads: the paired kinds (a patient on the claim) emitted by a VIOLENT opponent-rule row
# (`data/verbs.py::VIOLENT_VERBS`: `fight`, `capture`), off the table, no kind listed. NARROWED from "any opponent-rule
# row" [ASSUMPTION; medium; Jordan to correct; revert: drop the `VIOLENT_VERBS` test]: `speak` is an opponent-rule
# row too, and its `pursuit.moved` would make a hard word a licence to fight.
_OPPONENT_DEED_KINDS = frozenset(k for v in VIOLENT_OPPONENT_VERBS for k in VERB_TABLE[v].emits if k in PAIRED_KINDS)
# The strata those rows act at: a doer is an attacker only if seen acting at one of them (a kind `train` also emits is no blow).
_OPPONENT_STRATA = frozenset(VERB_TABLE[v].stratum for v in VIOLENT_OPPONENT_VERBS)


def violence_context_of(p: Person, q: Question, r: str, contexts: tuple, records: list,
                        memo: Optional[dict] = None) -> Optional[str]:
    """THE FIRST OF `contexts` (`rosters.yaml: violence_contexts`' line) IN WHICH `p` HOLDS VIOLENCE AGAINST `r`, or
    `None`. The one reader of the decline, for `opening_set` and any instrument that asks why a fight formed."""
    memo = {} if memo is None else memo
    return next((name for name in contexts if VIOLENCE_CONTEXT_READERS[name](p, q, r, records, memo)), None)


for _v, _ctx in VIOLENCE_CONTEXTS.items():
    if set(_ctx) - VIOLENCE_CONTEXT_READERS.keys() or not subject_is_opponent(VERB_TABLE[_v]):
        raise Forbidden(
            f"`rosters.yaml: violence_contexts` names {_v!r}: {list(_ctx)}, and either a context has no reader "
            f"({sorted(VIOLENCE_CONTEXT_READERS)}) or the row's subject is not its opponent", "rosters.yaml",
            needs="a verb contested against its subject, and contexts `decision/options.py` reads",
            law="CR-87 -- a violence decline narrows an attack on its subject by a context the actor holds")


def _check_context_terms(terms: dict) -> dict:
    """B15.08 (PHY_A A3): `rosters.yaml: context_terms` held to the readers, or import refuses naming the line -- each key a name in
    `VIOLENCE_CONTEXT_READERS`, the range `CONTEXT_KEY` carries. A function, so a test can plant a bad line and watch it refuse."""
    if set(terms) - VIOLENCE_CONTEXT_READERS.keys():
        raise Forbidden(
            f"`rosters.yaml: context_terms` names {sorted(set(terms) - VIOLENCE_CONTEXT_READERS.keys())}, which is no context reader "
            f"({sorted(VIOLENCE_CONTEXT_READERS)})", "rosters.yaml",
            needs="a context `decision/options.py::VIOLENCE_CONTEXT_READERS` reads",
            law="PHY_A A3 -- a fight's terms follow a context the decline can record on the Candidate")
    return terms


_check_context_terms(CONTEXT_TERMS)


# ⚠ `project` LIVES HERE, NOT IN `choose.py`, BECAUSE OF AN IMPORT CYCLE: `opening_set` calls it
# (`ED-IN-0261`'s refusal gate, `H-146`) and `choose.py` imports this module at top level, so
# importing it from `choose` inside a function body would be a `choose <-> options` cycle hidden
# from an instrument, not removed (`tests/valoria/test_import_cycle_game_state_npe.py`). It is
# defined ONCE, here, and `choose.py` imports it back -- the edge runs one way only.
#
# `align` lives in `data/verbs.py` beside `ALIGNMENT`, so the `H-66` rebind is `data.verbs.ALIGNMENT`
# and reaches `choose`'s score and this module's `refuses` gate through the one function.
# `project`'s stated single owner is `data/pursuits.to_axes`; it is not moved here.


def project(p: Person, scar_shift: float = 0.0, manner: bool = True, **scar_read) -> dict:
    """A person's fifteen pursuit weights, in the seven-axis basis. `U3` / R-06a.

    ⚠⚠ **§F2's `conviction[axis]` IS COMPUTED, NOT LOOKED UP.** V2 §F2 spells
    `score(c) = Σ_axis conviction[axis] · alignment(c.verb, axis)`, and that indexing needs a
    person's convictions KEYED BY AXIS:

        conviction[axis]  :=  Σ_conv  p.pursuits[conv] · projection[conv][axis]

    and `Σ_axis` above is untouched. A person holds weights over the FIFTEEN pursuits; the projection is
    the only thing that knows about axes.

    ⚠ **THE MATRIX IS READ, NOT INVENTED** — `conviction_axis_matrix_v30.md` §2, with a per-cell
    rationale in its §3. That is the difference between this table and `alignment`, whose own note
    says of its cells *"a reason is not a citation"*. They multiply together, so which of the two
    is argued and which is cited is worth being able to see.

    ⚠ **A CONVICTION THE MATRIX DOES NOT LIST PROJECTS TO NOTHING, AND THAT IS THE SPARSE DEFAULT
    RATHER THAN A SILENT DROP.** `PROJECTION_DEFAULT_CELL` is the declared 0.0; the loader has
    already refused any conviction name outside the roster, so an unlisted pair here is a cell the
    data chose to leave sparse, not a typo that got through.

    ⚠ DELEGATED, NOT DUPLICATED. `data.pursuits.to_axes` is the one owner of *convictions → axes*,
    because a second caller does not have a `Person`: `data.cast.loyalty` projects a
    ROLE TEMPLATE's expected-conviction vector through the same 15×7. `to_axes` reads
    `data.verbs.PURSUIT_PROJECTION` at call time, so that is still the rebind that reaches here.

    ⚠ `scar_shift` is IN-08 H9's crisis reader (`Fixtures.scar_weight_shift`, `H-187`): the weights
    `to_axes` projects are `person_q.crisis_weights(p, scar_shift)` -- a pursuit whose scar count has
    reached threshold 2 gives weight to the others. `0`, the shipped control, hands `to_axes` the
    person's own `pursuits` untouched. Only `choose`'s score passes it; `refusal_tolerance` (dormant)
    reads the unshifted weight. `scar_read` is `hold=` and `mass=` (`Fixtures.scar_hold`, `scar_primary_mass`; `person_q.crisis_weights`'s): a reader that holds the
    fixtures passes both, so the shifted weights keep the shift among a person's primaries at `scar_hold: primary`, as the writer scars them (B10.07).

    ⚠ `manner` (B10.58) IS `person_q.projected_axes`'s: `False` projects his pursuits WITHOUT his stored manner offset, and `refusal_tolerance` alone asks it (M37)."""
    return projected_axes(p, scar_shift, manner, **scar_read)


def refusal_tolerance(p: Person, axis: Optional[str]) -> Optional[float]:
    """`ED-IN-0261`'s deontological gate, the PERSON half: their SHARE of the gating axis in the
    projected vector, `project(p)[axis] / ‖project(p)‖` (0.0 for a zero vector), which IS the
    threshold (Jordan: *"the weighting is a threshold for certain actions"*). A share lies on ±1 as
    an alignment cell does, so the two are compared on one scale; the raw weight's size moves with
    how many pursuits the registry authors and is not. Read through `data.pursuits.to_axes`
    (`project`), the norm in `_AXES` order (`person_q.decisiveness`).
    `None` when `refusal_axis` is unset -- the control arm, under which `choose.make_ranker` strikes
    nothing. The axis is whatever `Fixtures` names, checked against the live roster, never a
    literal here.

    ⚠ RUNS `project(p)` TWICE MORE FOR THE SAME PERSON `choose()` PROJECTS FOR `score` (`decisiveness`
    is the second), AND THIS IS KNOWN AND DEFERRED, NOT MISSED. Dormant today -- `refusal_axis` ships unset, and this
    line short-circuits above before `project` is ever called. The ranker holds the shifted projection in its memo,
    but this reads the unshifted weight (the `scar_shift` note above); threading one through is worth doing WITH `H6`,
    when the gate ships live and the cost stops being theoretical, not as a speculative widening now."""
    if axis is None:
        return None
    require_member(axis, PURSUIT_AXES, f"refusal axis {axis!r} is not on the pursuit_axes roster",
                   "H-146", law="ED-IN-0261 -- the gate reads a ROSTERED axis; an unrostered one "
                                "would raise `Unspecified` rather than project to a real weight")
    refusing_pole(axis)       # CR-21: an armed axis the roster authors no pole for refuses HERE, not at an engaged verb
    refusable(axis)           # B10.21: nor an armed axis with a pole and no authored list of refusable verbs: it refuses at arming, not at the first verb `scruple` is asked of
    # B10.58 / M37: NO MANNER AXIS FEEDS THE GATE. The armed axis can be one a person holds a stored offset on, so both the weight and the length are read from his pursuits alone.
    reach = decisiveness(p, manner=False)   # the vector's length, `_AXES` order (`person_q.decisiveness`, the one owner of the norm)
    return project(p, manner=False)[axis] / reach if reach else 0.0


def scruple(verb: str, axis: str, tolerance: float) -> float:
    """HOW FAR `verb`'s cell on `axis` sits PAST `tolerance` toward the refused pole (B10.23): a margin, not a boolean, so a large
    scruple is an act far past what he allows himself and a small one is near it. `0.0` where the cell does not lie past it, where
    the axis does not engage the verb (a zero cell, including the sparse default) and for a verb outside `refusable(axis)`.

    The refused pole is `data.rosters.refusing_pole(axis)`'s sign, as `refuses` has always read it: the cell is past the tolerance
    where `sign * (cell - tolerance) < 0`, and the margin is that gap, `-sign * (cell - tolerance)`. `tolerance` is on the cells' ±1
    scale (`refusal_tolerance`). Reads `data.verbs.align`, the one `choose`'s score reads too."""
    if verb not in refusable(axis):
        return 0.0
    a = align(verb, axis)
    return max(0.0, -refusing_pole(axis) * (a - tolerance)) if a else 0.0


def refuses(verb: str, axis: str, tolerance: float) -> bool:
    """Does a person whose weight on `axis` is `tolerance` refuse `verb`? It is `scruple(...) > 0`. The PERSON-SIDE refusal
    `score` cannot express: it ranks, and at `choice_temperature` 0.1 a good enough outcome
    outranks any finite penalty (`ED-IN-0261`).

    WHICH POLE REFUSES IS DATA (CR-21, H-146's repair): `data.rosters.refusing_pole(axis)` reads it
    from `rosters.yaml: pursuit_axes.refusing_pole` -- `-1`, the NEG pole, for `deontological` on
    `deontological/instrumental` (ED-IN-0261). A verb is refused when its alignment sits further toward
    the OPPOSITE pole than the person's own weight: `sign * (cell - weight) < 0`, which for `-1` is
    `cell > weight`. An axis with no authored pole raises, so the gate cannot invert or
    default silently. Only a verb the axis ENGAGES can be refused -- a zero cell, including the sparse
    default, is not one of the *"certain actions"* the ruling gates; the scar's
    `person_q.elements_violated_by` reads engagement the same way.

    ONLY A LISTED VERB CAN BE REFUSED (B10.21): `data.rosters.refusable(axis)` is the closed set of *certain actions*
    (`rosters.yaml: pursuit_axes.refusable`); a verb outside it is never refused, whatever its cell.

    Reads `data.verbs.align`, the one `choose`'s score reads too, so a rebind of
    `data.verbs.ALIGNMENT` moves the gate and the ranking together."""
    return scruple(verb, axis, tolerance) > 0.0


def person_side_eligible(p: Person, row: "VerbRow") -> bool:
    """§F1 clause 2, PERSON-SIDE. `own | remit | hold | presence`, NEVER `capability`.

    A DISJUNCTION: `transfer` is eligible by `remit:issue` OR `own` OR `hold:<store>`, so one
    alternative admitting is enough and one alternative declining decides nothing.

    ⚠ **ONE OF THE FOUR KINDS DECLINES HERE: `presence:`. `remit:` ADMITS** (`13b`, `H-71`): the
    grant rides on the `hold` Tenure (`World._grant_remit` writes it at `add_tenure`,
    `Tenure.granted_acts` owns the shape) and the body below admits on `arg in t.granted_acts`.

    ⚠ THE DECLINING KIND NAMES ITS HOLE, and neither it nor any other branch admits on an
    unevaluable predicate -- that would be a silent fill off the register (`G1`) at the opposite
    polarity to §42.2, which sends zero evidence to the verdict AGAINST the thing measured. The
    resolver's `_eligible` still evaluates both, because it HAS a `World`; this is the person's
    reading, and the gap between the two readings is the finding.

      * `remit:<act>` -- ADMITS (closed 2026-09-18; not a declining kind): it needs the OFFICE's `remit_acts`, and #353 §11.1: "who holds an office
        is NOT a field on the office -- it is a `hold` Tenure, owned by the holder". Two holders
        of one office share one remit, so it is not the person's state to move; a SNAPSHOT of the
        office's remit is stamped onto the Tenure when the hold opens, so the person reads their
        own row and `choose` still receives no `World`.
      * `presence:<rung>` -- declined because the ARGUMENT IS A PLACEHOLDER naming a kind of
        rung rather than an id, which is `H-75`, and is the same reasoning the `hold:<store>`
        branch already carries one block below."""
    return _admitted_through(p, row, trace=True)[0]


def exercised_seat(p: Person, row: "Optional[VerbRow]") -> Optional[str]:
    """G3 -- THE SEAT A COMPUTED ACT EXERCISES, BY DEFAULT: the office id its
    `Act.via` carries, or `None`. The FIRST of `exercisable_seats`; `opening_set` forms the
    Candidate per seat where there are several, so this is the answer only for a person with one.

    `04 §B.9` gives `Act` a `via : SeatId?` and `04:350` asks purview of the seat exercised, so
    the act a person mints has to say which seat it is exercised through -- and only the person can
    say, because only the person's own Tenures are in scope here (AX-2). It is the seat through
    which `person_side_eligible` ADMITTED the verb, read by the SAME walk (`_admitted_through`) so
    the two cannot disagree: a `remit:` alternative admits through a live `hold` whose grant
    carries the act, and that hold's object is the seat. An `own` or `hold` alternative admits the
    person AS THEMSELVES, and no seat is exercised -- `kill / wound`, `release` mint with `via=None`,
    and so does `transfer` for a person whose seats grant no `issue` (its first alternative is
    `remit:issue` since `H-160` limit 1, so a holder of a seat granting `issue` WITH A RUNG gives
    THROUGH it, from its rung). The fold's `_eligible` then admits the same act through the same
    seat, so making `via` required there moves no computed act.

    ⚠ WHEN SEVERAL SEATS GRANT THE ACT (`H-134`) THIS IS ONLY THE FIRST: `opening_set` forms ONE
    Candidate per seat (`exercisable_seats`), the seat riding on it (`VIA` in its operands) to
    `Act.via` (`seat_of`), and the fold's gate asks that seat. The person cannot say which seat
    reaches a target (that needs the containment tree, which is not the person's state), so a seat
    that does not reach it is refused there. `confer` reaches it since IN-53: a computed `confer`
    names its office on `subject` (`loop/predicates.py::office_named_by`), formed only on an Office
    referent (`H-207`). `revoke` does not (D1): it declares no referent class and reads its office
    from the payload's `office` alone (`_req_revoke`), so a computed `revoke` stays refused at its
    precondition as at the base.
    Traces nothing: the admission it mirrors already traced. A verb on no row (`row is None` -- a
    hand-ranked candidate naming an invented verb) exercises nothing; the fold refuses the verb
    itself, and inventing a seat for it here would be a second answer."""
    seats = exercisable_seats(p, row)
    return seats[0] if seats else None


def exercisable_seats(p: Person, row: "Optional[VerbRow]") -> tuple:
    """EVERY SEAT THE ACT OF `row` CAN BE EXERCISED THROUGH, in the person's own Tenure order -- the
    live `hold`s granting the act of the `remit:` alternative that admitted the verb
    (`_admitted_through`), distinct by seat. `()` for an act exercised as oneself (an `own` or
    `hold` alternative admitted it, or nothing did) and for `row is None`; one seat for nearly
    everyone. `exercised_seat` is the first; `opening_set` forms a Candidate per seat when there are
    several (`H-134`). Traces nothing: the admission it mirrors already traced."""
    if row is None:
        return ()
    return _admitted_through(p, row, trace=False)[1]


def seat_of(p: Person, c: Candidate) -> Optional[str]:
    """THE SEAT A CANDIDATE'S ACT IS EXERCISED THROUGH -- the one `pack_scenes` puts on `Act.via`.
    The seat `opening_set` formed it for where it chose among several (`VIA` in its operands); else
    `exercised_seat`'s, which is the only seat there is. One reader, so a Candidate and the act
    minted from it cannot name two seats.

    NONE FOR A HOLDER IN CUSTODY (B21.11, A-23): a live `detain` he owns suspends every seat he holds
    (`state/gate.py::_seat_grants`, asked by every remit-act basis and by `loop/resolve.py::_eligible`'s `remit:` branch, refuses
    the act through it), so his candidate names no seat: `opening_set` still forms it, the act mints with `via=None`, and the fold
    admits it only on an eligibility alternative that needs no seat. The seat's `hold` is untouched: custody suspends, it does not vacate.
    The reading is `state/carriers.py::in_custody`'s, over the person's own Tenures because a `decision/` reader holds no `World`."""
    if in_custody(p.tenures):
        return None
    seat = (c.operands or {}).get(VIA)
    return seat if seat is not None else exercised_seat(p, VERB_TABLE.get(c.verb))


def _granting_holds(p: Person, act: str, need_treasury: bool = False) -> tuple:
    """The seats of the person's OWN live `hold`s whose grant carries `act`, in Tenure order and
    distinct by seat (a person seated on one office twice is one seat) -- the one person-side
    reading of *which seats grant this* (`H-71` arm 2's snapshot). `()` for none.

    `need_treasury` is set for a row whose cell binds `from`: an act exercised through a seat gives
    from the seat's rung (`treasury_of`), so a seat whose grant carries no rung grants nothing such
    an act can be exercised through, and is passed over. Every reader of the seat (`opening_set`'s
    belief seat, `_operands`, `pack_scenes`' `via`) goes through here, so `via` and `from` agree."""
    return tuple(dict.fromkeys(
        t.object for t in p.tenures if t.kind == "hold" and t.live and act in t.granted_acts
        and (not need_treasury or t.seat_rung is not None)))


def _admitted_through(p: Person, row: "VerbRow", trace: bool) -> tuple:
    """`(admitted, seats)`: `person_side_eligible`'s walk over the row's DISJUNCTION, once, for both
    of its readers -- the FIRST alternative that admits decides, and `seats` are the offices it
    admitted through (`()` unless that alternative was `remit:`; every seat granting the act, in
    Tenure order). `trace=False` is `exercisable_seats`' reading of a verb the first reading already
    traced, so the trace records each decline once.
    The declines are held and traced only when NO alternative admits, so a person a later
    alternative admits leaves no note that the verb declined."""
    need_treasury = None                    # read only by the `remit` branch; computed there, once
    pending: list = []                      # this walk's decline notes, traced only on (False, ())
    for alt in row.eligibility:
        kind, _, raw = alt.partition(":")
        kind, raw = kind.strip(), raw.strip()
        # A `<...>` argument is a PLACEHOLDER naming a KIND of object (`hold:<store>`), not an id.
        # Keeping the distinction is what lets the `hold` branch below refuse to guess.
        placeholder = raw.startswith("<") and raw.endswith(">")
        arg = raw.strip("<>")
        if kind not in ELIGIBILITY_KINDS:
            raise Forbidden(
                f"eligibility kind {kind!r} is not in the eligibility_kinds roster", "§E4",
                needs="one of the four; `capability` GATES NOTHING (#353 §9.2)",
                law="#353 §9.2 -- 'capability supplies dice and GATES NOTHING'. A fifth kind is a "
                    "new way to make a verb unavailable and needs a ruling, not a table edit")
        if kind == "own":
            return (True, ())
        if kind == "hold":
            # ⚠ THE ARGUMENT IS COMPARED. It was parsed and thrown away, so `transfer`'s
            # `hold:<store>` and `destroy_record`'s `hold:<record>` admitted anyone holding ANY
            # office -- an OVER-admission, which `G4` makes a defect of equal weight to an
            # over-refusal. `<store>`/`<record>` are PLACEHOLDERS naming a kind of object, not
            # ids, so a placeholder cannot be matched against a Tenure's `object` and this
            # DECLINES rather than guessing which store the act meant: that binding is `H-75`.
            if not raw:                       # bare `hold` -- holding anything admits
                if any(t.kind == "hold" and t.live for t in p.tenures):
                    return (True, ())
            elif not placeholder:             # a literal object id
                if any(t.kind == "hold" and t.live and t.object == arg for t in p.tenures):
                    return (True, ())
            elif trace:
                pending.append(f"`hold:<{arg}>` names an object KIND, not an id (H-75); "
                               f"{row.verb!r} declines rather than admitting on any held object")
        # `remit` and `presence` decline: see the docstring. TRACE records the decline so the
        # count is measurable rather than inferred from a verb's absence.
        elif kind == "remit":
            # ⚠ `H-71` CLOSED HERE, arm 2. The grant rides on the Tenure: `World._grant_remit`
            # stamps the office's remit acts into the `hold` Tenure's `payload` at the ONE writer,
            # and `Tenure.granted_acts` owns the shape both sides read. So the holder's own state
            # answers this, `choose` still receives no `World`, and `AX-2` is untouched.
            # A placeholder is not matched, for the same reason `hold:<store>` refuses: `<act>`
            # names a KIND of act, not one, and admitting on it would be the over-admission `G4`
            # weighs equally with an over-refusal. Every live `remit:` cell in `verb_table.yaml`
            # is a literal (`remit:issue`, `remit:confer`), so this refuses nothing that exists.
            # G3: the hold that grants it IS the seat exercised -- returned, not just found.
            # `H-134`: ALL of them, so `opening_set` can form the Candidate per seat.
            # A row binding `from` gives from the seat's rung when exercised through one
            # (`_granting_holds`).
            if need_treasury is None:
                need_treasury = (row.requires_typed is not None
                                 and "from" in row.requires_typed.operands())
            seats = _granting_holds(p, arg, need_treasury) if arg and not placeholder else ()
            if seats:
                return (True, seats)
            if not trace:
                continue
            if placeholder:
                pending.append(f"`remit:<{arg}>` names an ACT KIND, not an act (H-75); "
                               f"{row.verb!r} declines rather than admitting on any granted remit")
            elif not arg:
                pending.append(f"bare `remit` names no act; {row.verb!r} declines")
            else:
                pending.append(f"`remit:{arg}` not granted on any live `hold` this person holds; "
                               f"{row.verb!r} declines")
        elif kind == "presence" and trace:
            pending.append(f"`presence:` eligibility is unevaluable person-side (H-33, the "
                           f"presence index); {row.verb!r} declines rather than admitting")
    for note in pending:
        TRACE.note(note)
    return (False, ())


def containing_rung_of(p: Person) -> Optional[str]:
    """WHERE THE ACTOR IS, READ OFF THE ACTOR: the object of their own live `contain` Tenure.

    A person's live `contain` Tenure. The tenure store is on the Person so a person-side function
    can ask this without a World: #353 `:730` gives a Person "every Tenure whose subject they are",
    and where you are is one of them.

    ⚠ IT IS NOT A CHOICE, AND THAT IS WHY IT IS DERIVED RATHER THAN OFFERED. `H-94` asked where
    `transfer`'s operands come from and the answer differs per operand: where the actor is, is
    STATE (the actor is somewhere, and it is wherever they are), the receiver is the question's
    referent, and `kind`/`amount` are values the design does not supply at all. Only the third
    kind needs a fixture. Reading the first as a choice would invent an option the person does not
    have; reading it as a fixture would invent a place.

    ⚠ THE NAME IS NOT `hearth_of`. §54 item 7 writes `stores(hearth(giver), kind) >= amount` and
    supplies THE TOKEN AND NO DEFINITION (`ARCHITECTURE.md:1898`, `ARCHITECTURE_V2.md:418`) --
    while `hearth` is SEPARATELY a member of `rosters.yaml: rung_kinds` (`person, hearth,
    community, settlement, territory, province, duchy, realm`; `ARCHITECTURE.md:376`). So the term
    has a second, narrower reading the document neither states nor excludes, and a function named
    for it would claim the document had chosen.

      READING A (this one, SHIPPED): the actor's containing rung, WHATEVER ITS KIND.
      READING B (the alternative, NAMED so the choice is visible): walk up the containment ladder
        to the nearest rung whose `kind` is `hearth`.

    A person may legitimately sit ABOVE a hearth in a hand-built world -- `tiny_world` seats the
    Duke in the settlement and the King in the realm, deliberately -- and there the two readings
    differ.

    ⚠ READING B IS REFUSED ON ARCHITECTURE (§0 test 5). It is not
    person-side: `Rung.kind` and `Query.parent_of` are WORLD reads, and this function is exactly
    the site §F1's L2 keeps World-free -- a person knows WHICH rung contains them, because that
    Tenure is their own, and does not know WHAT KIND of rung it is, because kinds are the world's.
    Giving it a `World` turns
    `test_w5_sense_is_still_the_only_world_taking_non_decision_function` red, which is the
    falsifier for this paragraph rather than a claim about it. The remaining alternative -- let
    the FOLD compute `hearth(giver)`, which does have a World -- gives one operand two owners
    again.

    `None` for a person with no live containment -- a person nowhere cannot give from a store, and
    the Candidate is not formed. That is a REFUSAL and not a hole in the design: #353 seats every
    person on the ladder, so a person off it is a WORLD the case failed to build."""
    return next((t.object for t in p.tenures if t.kind == "contain" and t.live), None)


def treasury_of(p: Person, seat: str) -> Optional[str]:
    """WHERE A HOLDER GIVES FROM WHEN HE GIVES THROUGH HIS SEAT: the seat's rung, its TREASURY (the
    retirement plan's G2, *"treasury = `Rung.stores` at the office's own rung"*), read off the
    person's OWN live `hold` on `seat` (`Tenure.seat_rung`, the grant's snapshot, `H-71` arm 2's
    shape). `None` for a seat he does not hold or a rungless seat, which has no treasury -- and the
    computed path never asks it of a rungless seat when the row binds `from` (`_granting_holds`'s
    `need_treasury` passes such a seat over, so the act is exercised as himself).

    `H-160` limit 1 / `H-158` [ASSUMPTION; medium; Jordan to correct; revert: a ruling that an `own`
    verb may be exercised through a seat]: `containing_rung_of`'s *where the actor is* stays the
    answer for an act exercised AS HIMSELF; an act exercised THROUGH A SEAT (`seat_of`: the seat
    `opening_set` formed the Candidate for, `exercised_seat`'s for one seat) gives from the seat's rung, because that is where the seat's
    matter is, and `loop/effects_economy.py::_renewals` already reads a payment of upkeep as exactly
    that (`seat.rung == from`). One rule for both positions of the actor, no verb named."""
    return next((t.seat_rung for t in p.tenures
                 if t.kind == "hold" and t.live and t.object == seat), None)


def _claim_by_id(p: Person, claim_id) -> Optional["Claim"]:
    """THE ONE CLAIM IN `p`'S OWN LEDGER WITH THIS ID, or `None`. `store_kind_of` and
    `_from_content_claim` (both below) each look a claim up by `q.about` before reading its
    predicate -- this is that lookup, factored once so it is not two loops over `p.ledger` written
    the same way. §20's constraint (a person's own ledger, never the world) lives at the call
    site, not here: this takes the ledger it is handed."""
    for c in p.ledger:
        if c.id == claim_id:
            return c
    return None


def store_kind_of(p: Person, q: "Question") -> Optional[str]:
    """The matter kind THE QUESTION IS ABOUT, from the person's own ledger. `None` if it says none.

    `q.about` is the originating object's id; for §F1's Q2 (`claim_landed`) that is a Claim in
    THIS person's ledger, and a claim whose predicate is `stores:<kind>` names a kind. The
    predicate is the one the grammar DERIVES (`f"{scalar}:{key}"`, `Observation`'s docstring), so
    this reads the same namespace `belief_contradicts` reads and the write side has a name to aim
    at -- which is `H-116`'s other half and is `W-B`, not this item.

    ⚠ PERSON-SIDE, AND THE LEDGER IS THE REASON IT CAN BE. §20: claims live in the holder's own
    ledger and nobody else may read it. Looking `q.about` up in the WORLD would make this a
    resolver read wearing a person's signature."""
    if q is None or not q.about:
        return None
    c = _claim_by_id(p, q.about)
    if c is None:
        return None
    # `stores` is `transfer`'s own `scalar:`, and `f"{scalar}:{key}"` is how `Observation`
    # derives the predicate -- so this reads the namespace the cell writes rather than a
    # second vocabulary. A claim about anything else names no matter kind.
    stem, sep, arg = str(c.predicate).partition(":")
    return arg if sep and arg and stem == "stores" else None


def _from_content_claim(p: Person, q: "Question", name: str):
    """AN OPERAND READ OFF A HELD (or merely witnessed) WRIT -- position `15c`, r2
    `02_THE_WRIT_AND_THE_WORD.md` §A.13: *"the operands are the WRIT's, not the fixtures'."*
    Modelled on `store_kind_of`, one paragraph above: both read a claim by `q.about`, never by
    the referent, because a document's content is what the PERSON HOLDING IT believes, and
    `AX-2` puts a belief nowhere else (§20) -- `subject`/the referent is a different fact and
    stays on its own branch below.

    `None` when `q.about` names no claim in `p`'s own ledger, the claim's predicate does not
    start `content:`, or its kind maps nothing for `name` (`_content_answer`). ⚠ THE MAP IS PER
    KIND (`rosters.yaml: record_sourced_operands`). ⚠ AND `subject` IS NEVER ASKED HERE, though both
    kinds map it: on a question about a document the act is about the document itself, so
    `_derive_operand` answers `subject` with the referent before it reaches this reader. A HELD
    Record answers `subject` too, through `held_record_claims` (`_derive_operand`'s `held=`).

    ⚠ A SINGLETON LIST COLLAPSES TO ITS ONE ID; ANY OTHER COUNT DECLINES. `to`'s writ-side type
    is `[PersonId|OfficeId]` (r2 §A.3) -- a LIST, because a document may address several people
    -- but every operand this vocabulary carries is a SCALAR (`_derive_operand`'s own
    `to`/`subject`/`site` branches, `_eff_transfer`'s single `w.rungs.get(...)`). Returning the
    raw tuple would form `petition`/`transfer` Candidates carrying it verbatim -- each one UNABLE
    TO EVER RESOLVE, because `w.persons`/
    `w.rungs` key on strings and a tuple matches nothing there, EVEN WHEN the sole named
    addressee genuinely exists. That would be the instrument inventing a NEW way to refuse an act
    for a reason that is not there (§42.2's polarity), on top of the ones the design already has.
    Naming WHICH of several addressees a scalar operand means is a choice nobody has ruled --
    `ID-13`'s `floor` precedent -- so more than one, or none, declines exactly as an unreadable
    floor does; exactly one is not a choice at all, so it is not held back."""
    if q is None or not q.about:
        return None
    return _content_answer(_claim_by_id(p, q.about), name)


def _content_answer(c: Optional["Claim"], name: str):
    """WHAT A DOCUMENT'S CONTENT CLAIM ANSWERS FOR OPERAND `name`, or `None` -- plan position IN-10
    (#453 §10.1). Read through `rosters.yaml: record_sourced_operands`, PER KIND: the claim's kind
    (`content:<kind>`) maps `name` to one of its own content keys, and that key's value is the
    answer. `None` when `c` is no content claim, its kind maps nothing for `name`, or the key is
    absent. A singleton id list collapses to its one id and any other count declines
    (`_from_content_claim`'s docstring). The one reader of the map, for both
    channels (`_from_content_claim`, `_derive_operand`'s `held=`)."""
    said = None if c is None else content_said(c)   # `person_q`'s one reader of the claim's shape
    if said is None:
        return None
    key = RECORD_SOURCED_OPERANDS.get(content_kind(c), {}).get(name)
    if key is None:
        return None
    v = said.get(key)
    if isinstance(v, tuple):
        return v[0] if len(v) == 1 else None
    return v


# Every operand name SOME record kind answers -- derived from the roster, never listed (the
# `test_jordan_no_definition_is_hardcoded_in_a_body` (retired) finding at `_derive_operand`'s document branch).
_RECORD_ANSWERABLE = frozenset(n for m in RECORD_SOURCED_OPERANDS.values() for n in m)


def _held_objects(p: Person) -> frozenset:
    """The ids of what `p` holds: the objects of his own live `hold` Tenures (an edge is owned by its
    subject, so this reads his `tenures`, never an index over every edge)."""
    return frozenset(t.object for t in p.tenures if t.kind == "hold" and t.live)


def held_record_claims(p: Person, tick: int = 0, decay: int = 0) -> list:
    """THE CONTENT CLAIMS OF THE RECORDS `p` HOLDS -- plan position IN-10, #453 §10.1's *"held
    Records"*: for each of `p`'s OWN live `hold` Tenures, the newest `content:<kind>` claim on its
    object in `p`'s OWN ledger, where `rosters.yaml: record_sourced_operands` maps that kind. In
    tenure order, one per held Record. Person-side and World-free (`AX-2`): the person's own Tenures
    and own ledger, never the Record itself -- a Record held but never read answers nothing.

    WHAT IT IS FOR: `_derive_operand(..., held=c)` answers an operand off one of these, `subject`
    included -- the act is about what the document SAYS (a dispensation's `terms`) -- and
    `operand_bags` forms one bag per such claim whose `terms` is the referent (its docstring)."""
    held = [t.object for t in p.tenures if t.kind == "hold" and t.live]       # TENURE ORDER (below)
    if not held:
        return []
    # NEWEST BY `LedgerReader._best`'s comparator, the one owner of *most recent, then most
    # confident* (strict `>`, first found wins a tie) -- not a second ladder.
    held_set = set(held)
    pool = [c for c in p.ledger if c.subject in held_set]
    out = []
    for o in dict.fromkeys(held):
        c = LedgerReader([c for c in pool if c.subject == o and content_said(c) is not None
                          and content_kind(c) in RECORD_SOURCED_OPERANDS], tick=tick, decay=decay).belief_among()
        if c is not None:
            out.append(c)
    return out


def document_read(p: Person, rid, tick: int = 0, decay: int = 0) -> Optional["Claim"]:
    """`p`'s OWN READING OF DOCUMENT `rid`: the newest `content:<kind>` claim on it in his ledger (`LedgerReader`'s
    comparator, `held_record_claims`' rule), whether he holds the Record or only read it made before him; `None`
    where he holds no reading. Person-side and World-free (AX-2)."""
    return LedgerReader([c for c in p.ledger if c.subject == rid and content_said(c) is not None
                         and content_kind(c) in RECORD_SOURCED_OPERANDS], tick=tick, decay=decay).belief_among()


def documents_known_as(p: Person) -> dict:
    """WHAT `p`'s OWN LEDGER SAYS EACH DOCUMENT IS: `{record id: frozenset of kinds}` over every `content:<kind>` claim
    he holds (`person_q.content_kind`, the one reader of the stem). Person-side and World-free (AX-2): what a document
    is, to him, is what his reading of it says (B11 lane A, `opening_set`'s sub-kind rule). A document he holds no
    reading of is absent: its kind is unknown to him."""
    out: dict = {}
    for c in p.ledger:
        k = content_kind(c)
        if k is not None:
            out[c.subject] = out.get(c.subject, frozenset()) | {k}
    return out


def holds_own_document(p: Person, kind: str) -> bool:
    """DOES `p` HOLD A DOCUMENT OF `kind` WHOSE CONTENT NAMES HIM? -- v9 IN-12 step 10, the read
    `rosters.yaml: held_document_declines` declines a verb on (`conceal` while a cover is held). Person-side
    and World-free (`AX-2`), `held_record_claims`' sources: his OWN live `hold` Tenures and the
    `content:<kind>` claims his OWN ledger holds on their objects (`loop/witness.py`'s content deposit to
    a new holder), read through `person_q.content_kind` / `content_said`. A Record held and never read
    answers nothing. "Names him" is any content value equal to his id: the kind's keys are the roster's,
    and none is spelt here."""
    held = _held_objects(p)
    if not held:
        return False
    for c in p.ledger:
        if c.subject not in held or content_kind(c) != kind:
            continue
        said = content_said(c)
        if said and any(v == p.id or (isinstance(v, tuple) and p.id in v) for v in said.values()):
            return True
    return False


def _from_shortfall_claim(p: Person, q: "Question", name: str):
    """AN OPERAND READ OFF A HELD SHORTFALL CLAIM. Plan position `19d`, the retirement plan's G3:
    *"wiring the existing `transfer` verb's operands from a shortfall claim"*. The claim is
    `(rung, "shortfall:<kind>", units)`. MATTER records it on the write of a larder its draw ran
    dry with a mouth unfed, as `demanded - delivered` over the rung's subtree
    (`queries/world_q.py`), and WITNESS deposits it into those who saw that write. So a person
    asked about it knows WHICH matter the place lacks and HOW MUCH. This reads the two:
      * `kind`   -- the predicate's argument (`store_kind_of`'s own move, one stem over);
      * `amount` -- the claim's value, when it is a positive whole number of units.
    Both are read by `q.about` from `p`'s OWN ledger, never by the referent, on
    `_from_content_claim`'s precedent (§20, `AX-2`).

    ⚠ `to` IS NOT READ HERE. For a `claim_landed` question the referent IS the claim's subject, so
    the referent rule already binds `to` to the drained rung (`rosters.yaml:
    shortfall_sourced_operands`' note). ⚠ `from` IS NOT READ HERE EITHER. The giver gives from where
    they stand (`containing_rung_of`), or through a seat from the seat's own rung (`treasury_of`,
    `H-160` limit 1), for r2 §A.13's reason: a claim about somewhere else must not reach into a
    larder the actor neither stands in nor holds the seat of.

    ⚠ `None` IS SILENT BY DESIGN. It means no claim by `q.about` in `p`'s own ledger, a predicate
    that is not `shortfall:<kind>`, or an amount that is not a positive whole number, and the caller
    falls through to `store_kind_of`/the fixtures exactly as before. A drifted retelling (`15b`'s
    `_told_value`) stays positive by construction: it preserves sign and never crosses zero. So a
    rumour can misstate how short a place is, and it can never turn the shortfall into a surplus.

    REJECTED SHAPES, each for a reason:
      * A `content:` WRIT CARRYING `kind`/`amount` (`15c`'s reader, a new record kind). The writ is
        a document someone ISSUES. Here nobody asks: the larder ran dry and a witness saw it.
        Minting a document for a fact nobody authored is the automatic promotion S36.1 forbids
        (probe `F19`'s law).
      * THE `stores:<kind>` OBSERVATION `store_kind_of` already reads. That is a store LEVEL. A
        level is not a lack: a larder at 30 is plenty for three mouths and a famine for thirty, and
        a person cannot know the mouths (`demanded` is a world read).
      * THE PER-PERSON SHORTFALL, as witnessed through item 3b's `body.changed`.
        (`World._subsistence_shortfall` is census-only and is no claim at all.) That claim is about
        a PERSON, so its referent is no rung and a transfer to it refuses (`_eff_transfer`: no
        rung, no transfer). It carries no kind or amount either (`value` is `True`). It is also the
        per-person scale `ED-IN-0255` ruled away from: *"i don't think having lords and guild
        members etc worry about subsistence is worthwhile"*, *"it's a territorial issue"*."""
    if q is None or not q.about:
        return None
    c = _claim_by_id(p, q.about)
    if c is None:
        return None
    stem, sep, kind = str(c.predicate).partition(":")
    if not sep or not kind or stem != SHORTFALL_PREDICATE:
        return None
    if name == "kind":
        return kind
    if name == "amount":
        v = c.value
        ok = isinstance(v, int) and not isinstance(v, bool) and v > 0
        return v if ok else None
    return None


def _derive_operand(p: Person, name: str, q: "Question", subject, fx: "Fixtures",
                    seat: Optional[str] = None, held: Optional["Claim"] = None,
                    on_referent: bool = True):
    """ONE OPERAND, FROM THE PERSON'S OWN STATE. `None` means THIS PERSON CANNOT SUPPLY IT.

    `on_referent` is False when the ROW forms on a classed referent (`not VerbRow.referent_class`,
    passed by `_operands`): such a row's subject rides the question without being what it is about,
    so the three readers of the claim `q.about` names (the document, the shortfall,
    `store_kind_of`) answer nothing for it -- even when the same id is ALSO one of `q.referents`.

    `held` (plan position IN-10, #453 §10.1) is the content claim of a Record the person HOLDS
    (`held_record_claims`), or `None`. When given it answers FIRST, for every name its kind maps in
    `rosters.yaml: record_sourced_operands` -- `subject` included: a held dispensation's `terms`
    answers `subject`, the act being about what the document says, and its addressee `to`. Without
    it nothing below moves.

    `seat` is the seat the act will be exercised through (`seat_of`), `None` for an act the
    person performs as himself. It moves ONE operand, `from`: through a seat, the giver gives from
    the seat's rung (`treasury_of`, `H-160` limit 1); as himself, from where he stands.

    ⚠ THE CHAIN IS NOT THE ROUTER `G2` FORBIDS, on `WorldReader.read`'s own precedent. It
    enumerates the CLOSED OPERAND VOCABULARY -- `rosters.yaml: requires_operands`, where an
    unrostered one already refuses at load -- and not verbs, entities or outcomes. There
    is no shape to forbid instead: each name is a different question, and a per-verb table
    would be the special case `G2` is actually about.

    THE RULE IT IMPLEMENTS, stated once so the branches are readable as one decision rather than
    eight: AN OPERAND NAMING WHAT THE ACT IS ABOUT BINDS THE QUESTION'S REFERENT; AN OPERAND
    NAMING THE ACTOR'S OWN POSITION BINDS THE ACTOR'S OWN STATE; AN OPERAND THE DESIGN SUPPLIES NO
    VALUE FOR IS A FIXTURE. That is why `subject`, `to` and `site` all bind the referent and are
    not one name -- the cells name them differently because they mean different things TO THE
    VERB, and the person answers all three the same way, with the thing they were asked about.

    ⚠ POSITION `15c` ADDS A FOURTH READING: AN OPERAND THE DOCUMENT THE QUESTION IS ABOUT ANSWERS
    BINDS THE DOCUMENT, not the referent and not the fixture. `15c` asked it for `to`/`kind`/`amount`
    (r2 §A.13: *"the executor's act is `transfer`, whose operands -- `from`, `to`, `kind`, `amount`
    -- are all in the closed eight"*); since IN-10 the names are the document's kind's, per
    `rosters.yaml: record_sourced_operands`, and only `to` resolves on a question (`subject` stays
    the referent; a HELD Record answers it, through `held=`). `from` is DELIBERATELY EXCLUDED
    from this check: r2's own ruling keeps *where you are* off the writ (*"a writ that could name
    `from` would let a Duke's document reach into a larder the executor is not standing in"*), so
    it stays on `containing_rung_of` alone, below. `at` -- the writ's OWN place of discharge -- is
    also excluded here, and DELIBERATELY: `at` is not (and r2 rules it must not become, *"I do not
    coin a ninth operand"*) a member of `requires_operands`, so no typed cell can ever ask
    `operands_for` for it and `_derive_operand` is never called with `name == "at"` at all -- a
    branch here would be dead code no test could reach (`ID-13`). `13f`/`19`/`19b`/`found` are
    where a NEW verb cell earns `at` a roster place, if one ever needs to bind it directly; this
    position supplies the READER those positions build on, not the roster edit.

    ⚠ POSITION `19d` ADDS A FIFTH SOURCE, FOR TWO NAMES: `kind` and `amount` are read off a held
    SHORTFALL claim (`_from_shortfall_claim`), ahead of `store_kind_of` and the fixtures. `to` is
    not among them, because a shortfall claim's subject already IS the question's referent.

    ⚠ S5 (round-1 `01_THE_BUILD_ORDER.md`, row S5): this widening adds no fifth carrier.
    `beneficiary_kinds` (`rosters.yaml`) stays four members (`actor, subject, to, none`) --
    CAT-2 closed the beneficiary as a STATIC verb-table column resolving to a carrier the
    Candidate already holds, never a new operand name, so `beneficiary_of(p, c)` inherits nothing
    new to read from this branch.

    ⚠ THE REFERENT IS WORLD-SOURCED, AND THAT IS §F1'S OWN SHAPE RATHER THAN A WIDENING OF IT.
    One of the two question sources reads the world directly (`questions_for` Q4 `need`
    from `w.propositions`); Q2 `claim_landed` is ledger-sourced -- `for c in p.ledger` -- but
    ADMITTED through `reach`/`place_of` (`queries/world_q.py`, position `11a`), which read
    world state (`w.tenures`, `w.offices`, `w.rungs`) to decide whether the person may be ASKED
    about a claim their own ledger already holds. `W-C` promotes that referent from *which Candidate forms* to *an operand of the
    minted act*. §F1 states the derivation in terms -- `subject ∈ referents(q)`, "what the
    question is ABOUT" -- and puts the epistemic constraint in a DIFFERENT clause: `requires(verb)
    not KNOWN-false FROM p's OWN CLAIMS`, with its own warning that softening THAT clause is the
    breach. So the belief filter is on the requirement, never on the referent; and `to`/`site` are
    the referent under the two other names the closed operand vocabulary has for it, not a second
    channel.
    Two things make the promotion safe rather than merely licensed, and both are properties of
    code above rather than of this paragraph. (a) EVERY SOURCE IS ADDRESSED TO THE PERSON: Q2
    reads their own ledger, filtered by `reach(w, p)` -- never another person's, and never widening
    who WITNESSED (`01` §A.4.4) -- and Q4 is their own live `commit`. A person cannot be handed a
    referent they have no reach to. (b) THE REFERENT PROPOSES AND THE FOLD DISPOSES: naming a
    receiver is not moving matter to it. `_eff_transfer` returns nothing when a
    side is no rung and the fold emits `transfer.refused`; `move`'s `contain_path` cell reads
    UNKNOWN off the world and `contain_ascends` blocks a sibling -- so world-sourced ids do not
    DECIDE where matter goes.

    ⚠ AN OPERAND WITH NO BRANCH DECLINES, AND `floor` IS THE LIVE CASE. §12.1's floors are
    per-SITE-KIND (`band_floors`), and person-side there is no way to learn a site's kind without
    `w.sites` -- so a person cannot name the floor, and a cell binding `floor` as an OPERAND would
    form no Candidate and say so in the trace. No live cell does: `work` reads its floor as a
    SECOND READ on the site (`threshold_predicate`), which the world answers. Declining is
    therefore the honest branch AND the one with nothing dead behind it (`ID-13`) -- the
    alternative, `min` over every kind's floors, is a number nobody chose."""
    if name == "actor":
        return p.id
    # A HELD RECORD ANSWERS FIRST (IN-10), for every name its kind maps, `subject` included.
    if held is not None:
        v = _content_answer(held, name)
        if v is not None:
            return v
    # What the act is ABOUT, on a question: the referent, even when the question is about a
    # document -- the act is then about the document itself (`give` it, answer it), so the
    # document's own `terms` never re-aims it here. Only a HELD Record does, above.
    if name == "subject":
        return subject
    # THE DOCUMENT THE QUESTION IS ABOUT ANSWERS NEXT, for the names its kind maps in
    # `rosters.yaml: record_sourced_operands` (`to`; `from`/`at` are on no kind -- this function's
    # docstring). A question naming no document, or one whose kind maps no such name, falls
    # straight through to the referent/fixture below -- `None` is silent by design.
    # A CLASSED row (`on_referent` False) skips this reader and the shortfall and `store_kind_of`
    # readers below: each reads the claim `q.about` names, a claim about the question's own referent,
    # and a classed subject (a seat, a writ, a stamped place) rides the question without being what
    # it is about -- even when the stamped id is also a plain referent (B-K close, COR 4).
    if name in _RECORD_ANSWERABLE and on_referent:
        v = _from_content_claim(p, q, name)
        if v is not None:
            return v
    # AND A HELD SHORTFALL CLAIM ANSWERS NEXT (plan position `19d`), for the names
    # `rosters.yaml: shortfall_sourced_operands` declares (`kind`, `amount`). A question has one
    # `about`, and a claim is either a writ's or a shortfall's, never both, so the two readers
    # never compete for one operand and their order does not matter. Both come before
    # `store_kind_of` and the fixtures: a claim that NAMES the matter and the quantity outranks
    # a default that names neither.
    if name in SHORTFALL_SOURCED_OPERANDS and on_referent:
        v = _from_shortfall_claim(p, q, name)
        if v is not None:
            return v
    # What the act is ABOUT -- three cell-side names for the one thing the person was asked about
    # (`subject` answered above, before the document the question is about could re-aim it).
    if name == "to":
        return subject
    if name == "site":
        return subject
    # Where the ACTOR is. §54 item 7's `hearth(giver)`, READ AS the actor's containing rung of
    # any kind -- a declared assumption with a named alternative and a measurement, not a reading
    # the document supplies. See `containing_rung_of`, and register row `H-94`. THROUGH A SEAT the
    # actor's position is the seat's, so `from` is its rung (`treasury_of`, `H-160` limit 1).
    if name == "from":
        return treasury_of(p, seat) if seat is not None else containing_rung_of(p)
    # Values the design states no number for. `H-94`, declared / defaulted / swept.
    if name == "kind":
        return (store_kind_of(p, q) if on_referent else None) or fx.get("default_store_kind")
    if name == "amount":
        return fx.get("default_transfer_amount")
    # v9 IN-33 (H-58), restored at v10 REM-2B [ASSUMPTION; medium; Jordan to correct]: WHAT THE ACTOR
    # RECEIVES IN RETURN -- `exchange`'s other side. The question names what the actor gives (`kind`/
    # `amount`, above) and nothing about what comes back, so both are the third rule's: values the design
    # states no number for, fixtures. `return_kind` is its own (`default_return_kind`); `return_amount` is
    # the instrument's one unit of matter moved by an act (`default_transfer_amount`). No writ or
    # shortfall claim answers either (their rosters do not list them). REVERT: delete both branches.
    if name == "return_kind":
        return fx.get("default_return_kind")
    if name == "return_amount":
        return fx.get("default_transfer_amount")
    return None


# ⚠ TWO NAMES, AND THEY ARE THE SAME FACT. `subject` is *what the act is about* and `to` is *the
# far end it is aimed at*; the person answers both with the referent they were asked about, so
# carrying both is one fact under the two names the closed vocabulary has for it -- not a second
# decision. A Candidate carries them BEYOND the operands its own cell binds, and the reason is in
# Part E's write column rather than in its `requires` column: `transfer` declares
# `writes: [Rung.stores, Rung.stores]` -- TWO rungs -- and its cell names ONE (`from`, the giver's
# hearth). The receiver is declared by the WRITE and asked for by no precondition, so a rule that
# carried only what the precondition binds would mint a transfer that cannot be performed.
# ⚠ `site` IS NOT IN THIS TUPLE AND THE OMISSION IS THE POINT. `subject` and `to` are POSITIONS in
# an act; `site` asserts a TYPE -- *this referent is a Site* -- and only a cell that actually reads
# it may make that assertion on the person's behalf. `existence`'s `needs:` admits `site`, so
# including it here would put a `site` on every `carry`.
# roster-exempt: MECHANISM, and under the guard's own threshold besides. These are two members of
# `rosters.yaml: requires_operands` singled out by the argument above -- the roster is still the
# declaration of WHAT AN OPERAND MAY BE; this names which two the person answers with the referent.


_REFERENT_OPERANDS = ("subject", "to")


def operands_for(p: Person, row: "VerbRow", q: "Question", subject,
                 fx: "Fixtures") -> Optional[dict]:
    """§F1'S MISSING CHANNEL: the operands a Candidate carries, DERIVED PERSON-SIDE. `None` means
    THIS PERSON CANNOT FORM THIS CANDIDATE.

    ⚠ THE RETURN OF `None` IS THE LOAD-BEARING HALF, NOT THE DICT. Never mint an act with a hole.
    An act missing an operand is refused by the fold for a reason that is about the INSTRUMENT
    rather than about the world, and once `W-B` attaches a Verdict's reads to its Event that
    refusal is deposited at WITNESS and becomes a belief every witness holds -- a FALSE one, about
    a granary that was never asked about. Refusing to form the Candidate keeps the instrument's
    own gap out of everybody's ledger, and `TRACE.note` makes it countable instead.

    ⚠ WHAT IS CARRIED: THE CELL'S OWN OPERANDS, PLUS `subject`/`to` WHERE THE FORM ADMITS THEM.
    The rule the item states is *a form whose `needs` cannot be bound forms no Candidate*, and
    `needs:` is read here as the CEILING on what may be carried rather than the FLOOR of what must
    bind. Both halves of that are load-bearing and neither is a softening:
      * as a FLOOR it declines on operands nobody asks about. `scalar_threshold`'s `needs:`
        includes `floor`, which no live cell binds as an operand (`work` reads its floor as a
        SECOND READ on the site, which the world answers) and which a person cannot derive at all
        -- §12.1's floors are per SITE KIND and a kind is a world read. So the floor reading
        refuses `transfer` and `work` for want of a value neither of them reads, which is a
        refusal for a reason that is not there.
      * as a CEILING it is exactly what keeps the two vocabularies apart. `existence`'s `needs:`
        admits `site` and `from`; carrying them would put a `site` on every `carry`, for no
        reader. And an UNTYPED verb carries NOTHING, which is what stops `kind` -- a MATTER kind
        here and a RECORD kind in `_eff_create_record` -- from arriving on a `create_record` and
        silently making every record a record of grain.

    ⚠ AN UNTYPED VERB IS NOT DECLINED. `{}` is the right answer for `utter` and `create_record`:
    the grammar states no precondition, nothing to bind, and
    refusing them would be reading "no cell" as "an unmet cell" -- the UNKNOWN/False collapse the
    whole of this block exists to refuse. Their effects want operands of their own (`stages` is
    `H-80`, `harm` is `W-E`); those are not in `requires_operands` and are not this item.

    ⚠ NO WORLD, AND THE GUARD ACTUALLY REACHES IT. The AST proof in
    `test_w5_sense_is_still_the_only_world_taking_non_decision_function` examines every function
    whose FIRST parameter is annotated `Person`, which is why `p` is first here and not `row`.

    ⚠ TELLING WORKPLAN `T4`: THE FIRST OF `operand_bags`, for the callers that ask for one bag. A
    row whose `to` is a known person has one bag per person known; this answers the first, or
    `None` for none."""
    bags = operand_bags(p, row, q, subject, fx)
    return bags[0] if bags else None


def operand_bags(p: Person, row: "VerbRow", q: "Question", subject,
                 fx: "Fixtures", seat: Optional[str] = None,
                 people: Optional[tuple] = None, records: Optional[list] = None, tick: int = 0) -> list[dict]:
    """EVERY OPERAND BAG `p` CAN FORM FOR `row` ON `subject` -- `[]` when none (telling workplan
    `T4`, `ED-IN-0282`). One bag for every row whose operands all come from `_derive_operand`
    (`operands_for`'s rule, unchanged); for a row whose cell binds a known-person operand beside
    `subject` (`TypedRequires.known_person_operands`: `tell`'s `to`, since plan position `14`
    `give`'s, and since plan position IN-10 `issue`'s, so a writ's `terms` and its executor separate
    -- `petition` binds `to` without `subject`, so `to` is what it is about and keeps the referent
    rule in `_derive_operand`), one bag PER PERSON `p` KNOWS (`queries/person_q.py::known_persons`, from `p`'s own claims,
    never the actor; since IN-18 step 2a the topic may be the hearer), in that function's sorted order. Nobody known is no bag:
    a telling to nobody is an act with a hole (`operands_for`'s `None`), traced and not formed.

    ⚠ PERSON-SIDE AND WORLD-FREE, like `operands_for` -- `p` first for the AST guard's reason
    recorded there. WHETHER the person told is present is the fold's `hearer` conjunct; a known
    person who is elsewhere still gets a Candidate. THE TELLER DOES NOT LEARN IT FROM THE REFUSAL: the
    `with` read is observed, never deposited, and `tell.refused` is one kind for
    both conjuncts, so a refused telling to an absent hearer is retried whenever the teller
    re-deliberates -- a scene tax with nothing behind it. (CP-T05-03: a LOST telling, `news.untold`,
    is a realised act and is not retried within the season; only the refusal is.)
    `give` (plan position `14`) shares the shape: its
    receiver is a known person and its `with` conjunct the fold's. `people` is `known_persons`'
    answer when the caller already holds it (`opening_set`, once per call); `None` computes it.

    ⚠ PLAN POSITION IN-10 (#453 §10.1, *"`operand_bags` fans one Candidate per held Record whose
    kind has an entry, as it fans known persons"*): ON A FANNED ROW, ONE BAG MORE PER RECORD `p`
    HOLDS WHOSE `terms` IS THIS REFERENT (`held_record_claims`; `records` is its answer when the
    caller holds it). The held Record answers through `_derive_operand`'s `held=` -- `subject` off
    its `terms`, the fan's operand off its addressee -- so a commission naming a seat and a person
    is a `confer` of that seat on that person, known to the holder or not. `terms` must BE the
    referent: §F1 clause 3 (`subject in referents(q)`, which `opening_set` iterates) is not widened,
    and a Record about anything else forms nothing here. A Record whose kind maps none of the fan's
    operands, or whose addressee is a known person's bag already, adds nothing (same act id,
    `data/verbs.py::act_key`). A row with no fan is untouched: its operands are what it is about."""
    bags = _person_bags(p, row, q, subject, fx, seat, people, records, tick)
    # B21.55 (`14_VERBS_BINDING_D` commit D2, A-22): A ROW THAT ORDERS A PERSON (`VerbRow.commanded_operand`: `issue`'s `to`, `dispatch`'s
    # `subject`) FORMS ONLY ON THE ONES `p` CAN READ AS COMMANDED (`person_q.commanded_read`), so a seat's writ or order is not offered to a
    # stranger the fold would refuse (`world_q.commands`, which still decides) and nobody orders himself. NARROWS and widens nothing.
    ordered = row.commanded_operand()
    if ordered is not None and bags:
        commanded = commanded_read(p)
        bags = [b for b in bags if b.get(ordered, subject if ordered == "subject" else None) in commanded]
    return _fanned_choices(row, bags)


def _fanned_choices(row: "VerbRow", bags: list) -> list:
    """CP-T04-02 (`rosters.yaml: choice_sourced`): FOR A ROW THAT CARRIES A CHOICE, EACH BAG BECOMES ONE PER COMBINATION
    of the closed sets its keys range over (`data/verbs.py::CHOICE_RANGES`), each value riding on the bag under its own
    name -- `marshal`'s `role` x `retreat_at`, or no NPC ever marshals. The ranges are the module's vocabulary read
    through the roster pointers, in their own order; no value is chosen here (the chooser's draw is content-blind,
    `decision/choose.py`). A row the roster does not name returns its bags untouched.

    CP-T04-06: A KEY WHOSE RANGE HAS ONE MEMBER IS NOT FANNED -- there is nothing to choose among, and riding the lone
    value on every bag would rename every act (`data/verbs.py::act_key` suffixes the choice) and move the draws under
    those ids. `march`'s `posture` ships over `[storm]`, so no `march` Candidate carries one; `besiege` joining the
    roster is what makes the posture a choice."""
    sourced = CHOICE_SOURCED.get(row.verb)
    if not sourced:
        return bags
    keys = tuple(k for k in sourced if len(CHOICE_RANGES.get(k, ())) > 1)   # `said` has no roster: `opening_set` fans it over the claims `said_set` ranks
    if not keys:
        return bags
    combos = tuple(itertools.product(*(CHOICE_RANGES[k] for k in keys)))
    return [{**b, **dict(zip(keys, c))} for b in bags for c in combos]


def _person_bags(p: Person, row: "VerbRow", q: "Question", subject, fx: "Fixtures", seat: Optional[str] = None,
                 people: Optional[tuple] = None, records: Optional[list] = None, tick: int = 0) -> list[dict]:
    """`operand_bags`' body before the choice fan: one bag, or one per known person / held Record (its docstring)."""
    fan = row.known_person_operands()
    if not fan:
        ops = _operands(p, row, q, subject, fx, {}, seat)
        return [] if ops is None else [ops]
    # B11 lane A (the duel chain's fourth link, [ASSUMPTION; medium; Jordan to correct; revert: drop this branch]):
    # A ROW ABOUT A DOCUMENT (`referent_class: Record`) WHOSE SUBJECT HE HAS READ, AND WHOSE KIND ANSWERS EVERY FAN
    # OPERAND (`rosters.yaml: record_sourced_operands`, `_content_answer`), takes them from the document, not one bag
    # per person known: `accept` is fought against the challenge's `challenger`; a Candidate per
    # acquaintance would be refused by the fold's `names:to` for all but one. `subject` stays the document (no `held=`: the act answers the Record itself).
    if row.referent_class == _HELD_WRIT_CLASS:
        doc = document_read(p, subject, tick, fx.claim_decay())
        given = {n: _content_answer(doc, n) for n in fan}
        if doc is not None and None not in given.values():
            ops = _operands(p, row, q, subject, fx, given, seat)
            return [] if ops is None else [ops]
    if people is None:
        # B11.69 (`14_VERBS_SOCIAL1_A` edit 3): A FAN OPERAND THE CELL ASKS TO BE WITH THE ACTOR ranges over `telling_hearers`, as `opening_set`
        # hands it (which holds that answer once per call); a caller that hands none gets the same reading, never a wider one.
        people = telling_hearers(p.ledger, p.id, fx) if any(n in row.with_operands() for n in fan) else known_persons(p.ledger, p.id)
    # IN-53 D2 (H-207): A ROW DECLARING `counterparty_may_be_self` (`confer`) ALSO RANGES OVER THE
    # PERSON THEMSELF -- a person knows himself from his own state, so this adds no source of
    # knowledge and no world read (`known_persons` stays its three sources, AX-2, ED-IN-0282); the
    # lord who assumes a vacant seat. Appended after the known, so their bags keep their order.
    if row.counterparty_may_be_self and p.id not in people:
        people = tuple(people) + (p.id,)
    out = []
    for who in people:
        ops = _operands(p, row, q, subject, fx, {n: who for n in fan}, seat)
        if ops is not None:
            out.append(ops)
    if records is None:
        records = held_record_claims(p, tick, fx.claim_decay())
    formed = {tuple(b.get(n) for n in fan) for b in out}
    for c in records:
        # The Record's own `terms` must BE the referent; a Record saying nothing about it (no
        # `terms`, several) answers `None` and forms no bag.
        if _content_answer(c, "subject") != subject:
            continue
        given = {n: _content_answer(c, n) for n in fan}
        key = tuple(given.values())
        if None in key or key in formed:
            continue
        ops = _operands(p, row, q, subject, fx, given, seat, held=c)
        if ops is not None:
            formed.add(key)
            out.append(ops)
    if not out and not people:
        TRACE.note(f"{row.verb!r} needs {list(fan)} from a person {p.id} knows, and they know "
                   f"nobody; NO Candidate is formed (T4)", "§F1/H-94")
    return out


def _operands(p: Person, row: "VerbRow", q: "Question", subject, fx: "Fixtures",
              given: dict, seat: Optional[str] = None,
              held: Optional["Claim"] = None) -> Optional[dict]:
    """`operands_for`'s body: the cell's own operands plus `subject`/`to` where the form admits
    them, each from `given` if it names it (`operand_bags`' known person or held Record's addressee)
    else `_derive_operand` (with `held`, the held Record's content claim, IN-10); `None` for a bound
    operand nobody can supply. The rules are `operands_for`'s docstring's."""
    req = row.requires_typed
    if req is None:
        # An UNTYPED row carries nothing but what a known person fills for its named counterparty
        # (`VerbRow.known_person_operands`: `confer`'s `to`, IN-53); `given` is empty for every other.
        # IN-10 (a): AND ITS COUNTERPARTY WHERE THAT IS THE REFERENT ITSELF (`counterparty:
        # subject`, `oblige`'s seat), so the counterparty clause here and the fold's read the seat
        # the Candidate is formed on rather than nothing. The payload is unchanged (`_payload_of`
        # puts `subject` on every computed act); only the person-side decline can now see it.
        return {**given, "subject": subject} if row.counterparty == "subject" else dict(given)
    bound = tuple(req.operands())
    admitted = req.needs()
    names = bound + tuple(n for n in _REFERENT_OPERANDS if n in admitted and n not in bound)
    # The seat the act will be exercised through -- the walk `pack_scenes` names `Act.via` by -- so
    # the operands and the act's `via` cannot disagree about whether the actor acts as a seat.
    # `_derive_operand` reads it for `from` alone, so the (untraced) walk runs only for a bag
    # carrying `from`. `H-134`: a `seat` the caller names (`opening_set`, forming one Candidate per
    # seat) is the one the act will be exercised through and is used as given; `None` is the walk's
    # first seat.
    if seat is None and "from" in names:
        seat = exercised_seat(p, row)
    out: dict = {}
    for name in names:
        # `actor` is structural on both sides and is never carried; see `binding_of`.
        if name == "actor":
            continue
        v = given[name] if name in given else _derive_operand(
            p, name, q, subject, fx, seat, held, on_referent=not bool(row.referent_class))
        if v is None:
            if name not in bound:
                # An operand the CELL does not read cannot make the act malformed -- it is simply
                # not carried. Declining here would refuse a verb for want of a value nothing asks
                # for, which is the FLOOR reading this function's docstring rejects.
                continue
            TRACE.note(f"{row.verb!r} needs operand {name!r} and {p.id} cannot derive it "
                       f"person-side (H-94); NO Candidate is formed -- an act minted with a hole "
                       f"is refused for the instrument's reason and witnessed as a false belief",
                       "§F1/H-94")
            return None
        out[name] = v
    # v9 IN-33 (H-58), restored at v10 REM-2B: WHAT COMES BACK IN RETURN IS ANOTHER KIND. A bag whose
    # `return_kind` is its own `kind` is a kind traded for itself -- nothing, or a `transfer` of the
    # difference -- and `_eff_exchange` refuses it; the person can see the two operands are one kind (own
    # derivation, no World), so it is declined here rather than spent as a scene on a refusal that teaches
    # nothing (the counterparty self-decline's reason, `opening_set`). Read off the operand names, never a
    # verb name: only a cell binding `return_kind` carries it.
    if "return_kind" in out and out["return_kind"] == out.get("kind"):
        TRACE.note(f"{row.verb!r} by {p.id}: `return_kind` is `kind` ({out['return_kind']!r}), "
                   f"a kind traded for itself; NO Candidate is formed", "H-58")
        return None
    return out




def standing_of(p: Person, fx: "Fixtures", tick: int = 0) -> int:
    """S18.2's scalar, PERSON-SIDE, as a fixed-point int on `condition_scale` (S48).

        standing(p) = gap( told_by claims about p , p's own firsthand claims about p )

    0 means everyone reads you exactly as you read yourself; `condition_scale` is total mismatch.
    §18.2 calls it "the GAP", so it is computed as a gap and not silently inverted into a
    reputation score -- ⚠ the WORD "standing" ordinarily suggests the opposite polarity, and that
    tension is recorded rather than resolved, because resolving it would be picking a meaning the
    design did not state.

    ⚠ NO PAIRED PREDICATE RETURNS THE MAXIMUM GAP, NOT ZERO, and that is `H-29`'s swept default.
    Zero would mean "nobody has told you anything about yourself, therefore everyone agrees with
    you", which is §42.2's polarity rule run backwards -- zero evidence maps to the verdict
    AGAINST the thing measured, and the flattering reading is the one that rule exists to refuse.
    Raising instead would restore the blocker §F4 warns about."""
    scale = fx.get("condition_scale")
    told = [c for c in p.ledger if c.subject == p.id and c.source == "told_by"]
    own = [c for c in p.ledger if c.subject == p.id and c.source == "firsthand"]
    _agree, dis, paired = agreement(told, own, tick, fx.claim_decay())
    return scale if paired == 0 else (dis * scale) // paired
