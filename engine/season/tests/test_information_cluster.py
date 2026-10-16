"""Plan position `20-iii` -- THE INFORMATION CLUSTER. `workplans/2026-09-28-the-plan-one-order-mc-v18-
retired.md` §3.2 row 18: *"narrative #14 §F (D1-a) and the chain half of #7 (intelligence before
action)"*; `proposals/2026-09-27-mc-v18-retirement-plan/PROPOSAL.md` D1-a: *"A Record whose
`subject_matter` is a frozen `faction_q.resolve(...)` snapshot, commissioned by an act, read free by
holders, forgeable and destructible."* Content owner: `proposals/2026-09-12-emergent-narrative-
primitives-v2/01_THE_TEN.md` §F and proposal 14 (Jordan's).

What the position built, each asked of the real fold, the real WITNESS and the real gate:
  * a `faction_sheet` is a `Record` kind (`rosters.yaml: record_kinds`) whose keys are
    `faction_q.Faction`'s fields -- checked at import, and the check has a falsifier here;
  * `survey` commissions one: `own_ledger` of `subject` (the surveyor has heard of it), then the
    faction the subject coheres under (`world_q.faction_holding`, one read for a faction and a person),
    resolved AT THE MOMENT OF WRITING and minted through the one mint with the surveyor's `hold`.

THE FOUR PROPERTIES THE PLAN NAMES, each with the control that stops it passing vacuously:
  * FROZEN -- the world moves after the survey and the document does not; a SECOND survey in the
    moved world does record the move (so the first sheet's stillness is not a verb that ignores the
    world).
  * COMMISSIONED BY AN ACT -- no act, no sheet; a subject under no single faction is refused and
    mints nothing, while the same world's faction member is surveyed (so the refusals are not a
    broken verb).
  * READ FREE BY HOLDERS -- NO CODE WAS WRITTEN FOR THIS, and the tests below are why that is a
    finding rather than an omission: the content deposit (`loop/witness.py`, plan position `15`)
    already puts what a held document says into its holder's ledger at WITNESS. The surveyor spends
    exactly one act; a receiver by `give` spends NONE and holds the content; a co-located bystander
    of the same `give` holds none (the control: it is holding, not presence, that reads).
  * FORGEABLE AND DESTRUCTIBLE -- the CARRIER admits both (a false sheet is a lawful Record and reads
    exactly like a true one in a holder's ledger; `destroy_record`'s effect ends a sheet and its
    `hold` and leaves the belief standing). `forge` EXECUTES SINCE v9 IN-45 (section 5b: the sheet
    consumer first, then `_eff_forge`; its tripwire below is re-pinned to forge through the fold);
    `destroy_record` still declines for every actor (`H-75`), and its tripwire asserts exactly that.

The fixture is `probes.tiny_world` with one rostered faction planted: `fac_crown`, committed to by
`p_high` (who holds `off_duke`) and `p_mid` (who holds the hearth `Hh`). `p_low`, `p_mid` and
`p_other` stand in `Hh`; `p_high` in `S`.
"""

from __future__ import annotations

import copy
import dataclasses

import pytest

from ..data.matrix import Step, WriteClass
from ..data.rosters import FACTION_BY_PROP, RECORD_CONTENT, RECORD_KIND_KEYS, faction_prop_id
from ..data.verbs import _OPENERS_FROM_EFFECTS, VERB_TABLE
from ..decision import make_chooser
from ..decision.options import opening_set
from ..gaps import Unspecified
from ..harness import populated
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token, resolvable_verbs
from ..loop.effects import EFFECTS
from ..loop.witness import content_value
from ..queries import faction_q, world_q
from ..state.carriers import Act, Claim, Proposition, Question, Record, Tenure, View
from ..state.ids import H, draw_factory

FAC = faction_prop_id("Crown")
OTHER_FAC = faction_prop_id("Hafenmark")
SHEET = faction_q.SHEET_KIND
_CONTENT = f"{RECORD_CONTENT['predicate']}:{SHEET}"


def _world():
    """`tiny_world` with the Crown planted as a faction: its Proposition, two members' `commit`
    edges, and a rung held by one of them -- so the sheet has a member list, a holding and a seat
    to be right or wrong about."""
    w = P.tiny_world()
    for fac, name in ((FAC, "Crown"), (OTHER_FAC, "Hafenmark")):
        assert fac in FACTION_BY_PROP, f"{name} is no rostered faction -- the fixture is stale"
        w.propositions[fac] = Proposition(fac, "HOLDS", name, "is a faction of this world", True, 0)
    for pid in ("p_high", "p_mid"):
        w.add_tenure(Tenure(f"t_commit_{pid}", pid, FAC, "commit", since=0))
    w.add_tenure(Tenure("t_hold_Hh", "p_mid", "Hh", "hold", since=0))
    return w, SeasonDriver(w)


def _hear(w, holder, subject):
    """Put a firsthand claim ON `subject` in `holder`'s own ledger -- what `survey`'s cell asks
    (`own_ledger`, *the surveyor has heard of it*). An existence observation, a stem the reader
    already answers, so the planted belief means nothing beyond *I know this exists*."""
    kind = ("Proposition" if subject in w.propositions else "Person" if subject in w.persons
            else "Rung")
    p = w.persons[holder]
    p.ledger.append(Claim(f"c_{holder}_{subject}_{len(p.ledger)}", holder, subject,
                          f"exists:{kind}", 1, w.tick, "firsthand", 1, "own"))


def _fold(w, d, *acts):
    out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts),
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return out


def _kinds(events):
    return [e.kind for e in events]


def _survey(key, subject, actor="p_low"):
    return Act(id=key, actor=actor, verb="survey", payload={"subject": subject})


def _sheets(w):
    return [r for r in w.records.values() if r.kind == SHEET]


def _content_claims(p, rid):
    return [c for c in p.ledger if c.subject == rid and c.predicate == _CONTENT]


# ======================================================================================
# 1 -- THE KIND, THE VERB, AND THE TWO OWNERS OF ONE KEY LIST
# ======================================================================================

def test_20iii_survey_is_resolvable_and_opens_the_surveyors_hold_through_the_one_mint():
    """The verb is typed and effected, so `resolvable_verbs()` carries it; its one write is
    `(Record, exists)`, `issue`'s and `petition`'s column; and the derived opener map
    (`OPENERS-DERIVE`) sees its `hold` through `_mint_document` with no hand-written edit."""
    assert "survey" in resolvable_verbs() and "survey" in EFFECTS
    row = VERB_TABLE["survey"]
    assert row.writes == ("Record.exists",) and row.emits == ("faction.surveyed",), row
    assert row.eligibility == ("own",) and row.requires_typed is not None
    assert "survey" in _OPENERS_FROM_EFFECTS["hold"], _OPENERS_FROM_EFFECTS["hold"]


def test_20iii_the_sheet_keys_are_factions_fields_and_a_drifted_roster_refuses_at_import():
    """`faction_q._check_sheet_keys` is the import check; its falsifier is here (§0.1 pt 3). Every
    drift refuses: a key missing, a key extra, the same keys reordered (`content_value` freezes in
    the mapping's order, so a reordered row describes a document nobody writes), and no row at all.
    CONTROL: the shipped row passes, and it IS the dataclass's field list."""
    want = tuple(f.name for f in dataclasses.fields(faction_q.Faction))
    assert tuple(RECORD_KIND_KEYS[SHEET]) == want, (RECORD_KIND_KEYS[SHEET], want)
    faction_q._check_sheet_keys(RECORD_KIND_KEYS[SHEET])
    for drifted in (want[:-1], want + ("purview",), tuple(reversed(want)), None):
        with pytest.raises(Unspecified, match="record_kinds"):
            faction_q._check_sheet_keys(drifted)


# ======================================================================================
# 2 -- COMMISSIONED BY AN ACT: WHAT IS WRITTEN, WHERE, AND IN WHOSE HAND
# ======================================================================================

def test_20iii_a_survey_mints_the_resolution_at_the_moment_of_writing_into_the_surveyors_hand():
    """The expectation is written out from the planted edges, not read back through `resolve`
    (which would check the effect against the function it calls): the Crown's members are the two
    it was given, their one held rung is `Hh`, their one held seat `off_duke`, and `head` is
    `None` (`F.4`). The sheet is drawn up where the surveyor STANDS (`place_of`), not at his id."""
    w, d = _world()
    _hear(w, "p_low", "p_high")
    out = _fold(w, d, _survey("s1", "p_high"))
    assert _kinds(out) == ["faction.surveyed"], _kinds(out)
    rec = w.records["rec:s1"]
    assert rec.kind == SHEET
    assert rec.subject_matter == {"proposition": FAC, "members": ["p_high", "p_mid"],
                                  "holdings": ["Hh"], "seats": ["off_duke"], "head": None}, rec
    assert world_q.hold_force(w, rec.id).subject == "p_low", "the surveyor does not hold his sheet"
    assert rec.rung == world_q.place_of(w, "p_low") == "Hh", rec.rung


def test_20iii_one_read_for_a_faction_and_for_a_person_who_coheres_under_it():
    """`faction_holding` answers for the faction's own Proposition and for a member alike, so a
    survey OF the Crown and a survey of a Crown man write the same document."""
    w, d = _world()
    _hear(w, "p_low", FAC)
    _hear(w, "p_low", "p_mid")
    assert _kinds(_fold(w, d, _survey("s_fac", FAC), _survey("s_man", "p_mid"))) == [
        "faction.surveyed", "faction.surveyed"]
    assert w.records["rec:s_fac"].subject_matter == w.records["rec:s_man"].subject_matter


def test_20iii_a_subject_under_no_single_faction_is_refused_and_mints_nothing():
    """The effect's decline (`write` clause), one case per way the sheet's faction answers `None`: a
    person committed to no faction, a person committed to two, a rung nobody up its chain holds, and
    a Proposition the roster does not carry as a faction. CONTROL: in the same world, after all four,
    a Crown member is surveyed -- so the refusals are the subjects', not a verb that refuses
    everything. ⚠ RE-RECORDED at v9 IN-12 (`survey` + Rung): the rung case was `Hh`, which `p_mid`
    (Crown) holds, and a held rung is surveyed since then (section 2b); it is now `S`, held by nobody
    up `S -> D -> R`, the case `holder_faction_of` answers `None` for."""
    w, d = _world()
    w.add_tenure(Tenure("t_c1", "p_other", FAC, "commit", since=0))
    w.add_tenure(Tenure("t_c2", "p_other", OTHER_FAC, "commit", since=0))
    w.propositions["prop_x"] = Proposition("prop_x", "OUGHT", "R", "the roads stay open", True, 0)
    for subject in ("p_low", "p_other", "S", "prop_x"):
        _hear(w, "p_low", subject)
    before = dict(w.records)
    for i, subject in enumerate(("p_low", "p_other", "S", "prop_x")):
        out = _fold(w, d, _survey(f"bad{i}", subject))
        assert _kinds(out) == ["survey.refused"], (subject, _kinds(out))
    assert w.records == before, "a refused survey left a document behind"
    _hear(w, "p_low", "p_high")
    assert _kinds(_fold(w, d, _survey("good", "p_high"))) == ["faction.surveyed"]


def test_20iii_the_cell_refuses_a_subject_the_surveyor_has_never_heard_of():
    """`own_ledger`: nobody commissions a survey of what he has no claim on. CONTROL: the same act,
    once he holds one, executes."""
    w, d = _world()
    assert _kinds(_fold(w, d, _survey("s1", "p_high"))) == ["survey.refused"]
    assert not _sheets(w)
    _hear(w, "p_low", "p_high")
    assert _kinds(_fold(w, d, _survey("s2", "p_high"))) == ["faction.surveyed"]


def test_20iii_a_person_forms_a_survey_carrying_its_subject_and_the_fold_holds_the_cells_teeth():
    """Person-side (`opening_set`): the typed cell is what carries `subject` onto the Candidate -- an
    untyped row would carry nothing. ⚠ CLAUSE 4 DOES NOT DECLINE IT FOR WANT OF A CLAIM, and that is
    §F1's rule, not a gap: clause 4 declines only what the person's own claims make KNOWN-FALSE, and
    *"absence of a belief is not a belief in the negative"* (`opening_set`'s docstring). So the
    Candidate forms either way, and it is the FOLD that refuses the survey of a stranger
    (`test_20iii_the_cell_refuses_...`). In the shipped worlds a referent is nearly always the subject
    of a claim the person holds (`questions_for`'s Q2 is a claim landing), so the cell rarely bites
    there; it bites on a hand-built act and on a `need` question's referent."""
    w, _ = _world()
    p = w.persons["p_low"]
    view = View("p_low", [], w.fixtures.get("view_k"))

    def surveys(referent):
        q = Question("q:ic", "need", (referent,))
        return [(c.subject, c.operands.get("subject"))
                for c in opening_set(p, view, q, w.fixtures) if c.verb == "survey"]
    assert surveys("p_high") == [("p_high", "p_high")]
    _hear(w, "p_low", "p_high")
    assert surveys("p_high") == [("p_high", "p_high")]


# ======================================================================================
# 2b -- v9 IN-12 `survey` + RUNG (H-169 limit 6): WHO HOLDS THIS VALLEY
# ======================================================================================
# A Rung subject is answered by `world_q.holder_faction_of` (the march path's owner of *which faction
# holds this rung*), dispatched on `World.class_of` in `loop/effects_information.py::_resolved_sheet`.
# Hand-built worlds only (v9 §0.5, RULED 2026-10-13): nothing here asserts a verb executed in the
# seed-0 realm.

def _hafenmark_holds_s(w):
    """`p_other` is Hafenmark's and holds `S`, the settlement `p_high` (Crown) stands in, while
    `p_mid` (Crown) holds `Hh` beneath it -- so THE HOLDER'S faction, THE FACTION OF WHO STANDS
    THERE and THE FACTION OF THE RUNG BELOW are three different answers for `S`."""
    w.add_tenure(Tenure("t_commit_p_other", "p_other", OTHER_FAC, "commit", since=0))
    w.add_tenure(Tenure("t_hold_S", "p_other", "S", "hold", since=0))


def test_in12_a_survey_of_a_rung_mints_the_sheet_of_the_faction_that_holds_it(monkeypatch):
    """`:3391`, *a `faction_sheet` minted on a Rung subject*: a survey of `S` writes Hafenmark's
    sheet (its holder's faction), not the Crown's (whose man stands there); a survey of `Hh` writes
    the Crown's (its own holder's, the nearest held rung at or above it). The expectations are
    written out from the planted edges, not read back through `resolve`. `forge` reads WHICH faction
    through the same helper, so a forged sheet on `S` is Hafenmark's too, with the forger as head.
    THE MUTATION, in place: the rung lookup swapped back to `faction_holding` (`20-iii`'s reading,
    which takes a holder and not a held thing) -- the same survey of `S` is `survey.refused` and
    mints nothing, so the sheet is the lookup's and not the verb's."""
    w, d = _world()
    _hafenmark_holds_s(w)
    for subject in ("S", "Hh"):
        _hear(w, "p_low", subject)
    out = _fold(w, d, _survey("s_S", "S"), _survey("s_Hh", "Hh"))
    assert _kinds(out) == ["faction.surveyed", "faction.surveyed"], _kinds(out)
    assert w.records["rec:s_S"].subject_matter == {
        "proposition": OTHER_FAC, "members": ["p_other"], "holdings": ["S"], "seats": [],
        "head": None}, w.records["rec:s_S"]
    assert w.records["rec:s_Hh"].subject_matter["proposition"] == FAC, w.records["rec:s_Hh"]
    assert world_q.hold_force(w, "rec:s_S").subject == "p_low"
    assert _kinds(_fold(w, d, Act(id="f_S", actor="p_low", verb="forge",
                                  payload={"subject": "S"}))) == ["record.forged"]
    assert w.records["rec:f_S"].subject_matter == {
        **w.records["rec:s_S"].subject_matter, "head": "p_low"}, w.records["rec:f_S"]
    # THE MUTATION: the pre-IN-12 lookup for a rung
    from ..loop import effects_information as EI
    monkeypatch.setattr(EI, "holder_faction_of", world_q.faction_holding)
    before = dict(w.records)
    assert _kinds(_fold(w, d, _survey("s_S2", "S"))) == ["survey.refused"]
    assert w.records == before, "the mutated lookup still minted a sheet -- the cause is elsewhere"


def test_in12_a_rung_with_no_holding_faction_is_refused_and_mints_nothing():
    """THE CONTROL: the two ways `holder_faction_of` answers `None` -- nobody holds a rung at or
    above `S` (`S -> D -> R`, all unheld), and then, once `p_low` (committed to no faction) holds
    `D`, a held rung whose holder coheres under none -- each `survey.refused` (the `write` clause,
    the row's one refusal kind) with no Record minted. In the same world a survey of `Hh`, which a
    Crown man holds, is `faction.surveyed` -- so the refusals are the subjects'."""
    w, d = _world()
    for subject in ("S", "D", "Hh"):
        _hear(w, "p_low", subject)
    before = dict(w.records)
    assert _kinds(_fold(w, d, _survey("r0", "S"))) == ["survey.refused"]
    w.add_tenure(Tenure("t_hold_D", "p_low", "D", "hold", since=0))
    assert _kinds(_fold(w, d, _survey("r1", "S"), _survey("r2", "D"))) == [
        "survey.refused", "survey.refused"]
    assert w.records == before, "a refused rung survey left a document behind"
    assert _kinds(_fold(w, d, _survey("ok", "Hh"))) == ["faction.surveyed"]


def test_in12_the_person_path_is_unchanged_a_man_is_not_read_through_the_ground_he_stands_on():
    """THE CONTROL ON THE PERSON PATH: every person also has a `person`-kind rung of his id, so a
    dispatch on `subject in w.rungs` would send `p_low` (committed to no faction, standing in `Hh`,
    which the Crown holds) through `holder_faction_of` and write him a Crown sheet. `class_of` reads
    him as a Person first: still `survey.refused`. A Crown member still writes the Crown's sheet,
    the same document a survey of the faction itself writes (`20-iii`'s one read). MUTATION that
    reddens the first assertion: `w.class_of(subject) == "Rung"` -> `subject in w.rungs`."""
    w, d = _world()
    assert w.rungs["p_low"].kind == "person", "the fixture: a person has a rung of his own id"
    for subject in ("p_low", "p_mid", FAC):
        _hear(w, "p_low", subject)
    out = _fold(w, d, _survey("pl", "p_low"), _survey("pm", "p_mid"), _survey("pf", FAC))
    assert _kinds(out) == ["survey.refused", "faction.surveyed", "faction.surveyed"], _kinds(out)
    assert "rec:pl" not in w.records
    assert w.records["rec:pm"].subject_matter == w.records["rec:pf"].subject_matter
    assert w.records["rec:pm"].subject_matter["proposition"] == FAC


def test_in12_the_sheet_consumer_reads_a_rung_subject_sheet_as_it_reads_any(monkeypatch):
    """`c435a5ec`'s consumer (`record_sourced_operands.faction_sheet`, `to: head`) reads a sheet's
    CONTENT and never its subject, so a sheet commissioned on a rung carries the same keys and
    addresses its holder's petition the same way: to the head it names. Through the real fold and
    WITNESS (`_hold_sheet`). CONTROL: the consumer row dropped, the address falls back to the
    referent -- so the address is the sheet's."""
    w, _ = _world()
    _head(w, "p_high")
    rec, claim = _hold_sheet(w, "p_low", subject="Hh")
    assert rec.kind == SHEET and rec.subject_matter["proposition"] == FAC
    assert tuple(rec.subject_matter) == tuple(RECORD_KIND_KEYS[SHEET]), rec.subject_matter
    assert _petition_to(w, "p_low", rec, claim) == "p_high"
    from ..data.requires import RECORD_SOURCED_OPERANDS
    monkeypatch.delitem(RECORD_SOURCED_OPERANDS, SHEET)
    assert _petition_to(w, "p_low", rec, claim) == rec.id


# ======================================================================================
# 3 -- FROZEN: THE WORLD MOVES, THE DOCUMENT DOES NOT
# ======================================================================================

def test_20iii_the_sheet_is_frozen_the_world_moves_and_the_document_does_not():
    """After the survey the Crown loses `p_mid` (his `commit` ends) and gains `p_other`. The Record
    still says what was true when it was written; `resolve` says what is true now. CONTROL: a
    second survey in the moved world records the move -- so the first sheet's stillness is the
    snapshot, not a verb that never reads the world."""
    w, d = _world()
    _hear(w, "p_low", "p_high")
    _fold(w, d, _survey("s1", "p_high"))
    first = w.records["rec:s1"]
    said = copy.deepcopy(first.subject_matter)
    w.tick += 1
    next(t for t in w.tenures if t.id == "t_commit_p_mid").until = w.tick
    w.add_tenure(Tenure("t_commit_p_other", "p_other", FAC, "commit", since=w.tick))
    now = dataclasses.asdict(faction_q.resolve(w, FAC))
    assert now["members"] == ["p_high", "p_other"] and now["holdings"] == [], now
    assert first.subject_matter == said, "the sheet changed when the world did"
    _fold(w, d, _survey("s2", "p_high"))
    assert w.records["rec:s2"].subject_matter == now
    assert w.records["rec:s2"].subject_matter != first.subject_matter


# ======================================================================================
# 4 -- READ FREE BY HOLDERS: HOLDING IS READING, AND COSTS NO ACT
# ======================================================================================

def test_20iii_read_free_the_holder_and_a_receiver_by_give_learn_it_and_spend_no_act_to():
    """Season 1: `p_low` surveys, and at WITNESS holds `(sheet, content:faction_sheet, <frozen
    content>)` -- one act spent, the commissioning. Season 2: he GIVES it to `p_mid`, who takes NO act
    in either season and ends holding the same content, frozen and hashable. CONTROL: `p_other`,
    standing in the same hearth and witnessing the same `give`, learns nothing of what it says --
    the deposit follows the `hold`, not presence."""
    w, _ = _world()
    _hear(w, "p_low", "p_high")
    acts = {"n": 0}

    def season_one(p, v, s, ask_budget):
        if p.id == "p_low":
            acts["n"] += 1
            return [P.Act_(w, p, "survey", payload={"subject": "p_high"})]
        return []
    d1 = P._run_d(w, season_one)
    (rec,) = _sheets(w)
    assert [a.verb for a in d1.resolved if a.actor == "p_low"] == ["survey"], d1.resolved
    got = _content_claims(w.persons["p_low"], rec.id)
    assert len(got) == 1 and got[0].value == content_value(rec.subject_matter), got
    hash(got[0].value)
    assert dict(got[0].value)["members"] == ("p_high", "p_mid")
    assert not [c for pid, p in w.persons.items() if pid != "p_low"
                for c in _content_claims(p, rec.id)], "somebody who holds nothing read the sheet"

    def season_two(p, v, s, ask_budget):
        if p.id == "p_low":
            return [P.Act_(w, p, "give", payload={"subject": rec.id, "to": "p_mid"})]
        return []
    d2 = P._run_d(w, season_two)
    assert "record.given" in _kinds(w.log), _kinds(w.log)
    assert world_q.hold_force(w, rec.id).subject == "p_mid"
    assert not [a for d in (d1, d2) for a in d.resolved if a.actor == "p_mid"], "p_mid acted"
    theirs = _content_claims(w.persons["p_mid"], rec.id)
    assert [c.value for c in theirs] == [got[0].value], theirs
    assert not _content_claims(w.persons["p_other"], rec.id), "a bystander read the sheet"


# ======================================================================================
# 5 -- FORGEABLE AND DESTRUCTIBLE: WHAT THE CARRIER ADMITS, AND WHAT NO ACT YET DOES
# ======================================================================================

def test_20iii_a_false_sheet_is_a_lawful_record_and_reads_exactly_like_a_true_one():
    """r2 `02` §A.15: *"a forged writ and a genuine writ are indistinguishable in every executor's
    ledger -- by construction, not by a flag"*. A FORGED sheet, made through the real fold by
    `p_other` and handed on to `p_mid`, deposits a claim of the same predicate and source as a true
    sheet's, carrying nothing of its forgery. ⚠ RE-PINNED AT v9 IN-45, AS THIS TRIPWIRE ASKED: it
    asserted `forge` had no effect body and the forgery here was PLANTED; `forge` is typed and
    effected now (`_eff_forge`), so the sheet is forged through the fold and `H-169` (2) is narrowed.
    `Record.forgery_quality` is not written (`H-210`), so the forgery is told apart here by its maker."""
    assert "forge" in EFFECTS and "forge" in resolvable_verbs()
    w, _ = _world()
    _hear(w, "p_low", "p_high")
    _hear(w, "p_other", "p_high")

    def season_one(p, v, s, ask_budget):
        if p.id == "p_low":
            return [P.Act_(w, p, "survey", payload={"subject": "p_high"})]
        if p.id == "p_other":
            return [P.Act_(w, p, "forge", payload={"subject": "p_high"})]
        return []
    P._run_d(w, season_one)
    (forged,) = [r for r in _sheets(w) if world_q.hold_force(w, r.id).subject == "p_other"]
    (true_sheet,) = [r for r in _sheets(w) if world_q.hold_force(w, r.id).subject == "p_low"]
    P._run_d(w, lambda p, v, s, b: ([P.Act_(w, p, "give", payload={"subject": forged.id,
                                                                    "to": "p_mid"})]
                                    if p.id == "p_other" else []))
    true_claim = _content_claims(w.persons["p_low"], true_sheet.id)[0]
    (false_claim,) = _content_claims(w.persons["p_mid"], forged.id)
    assert dict(false_claim.value)["head"] == "p_other" != dict(true_claim.value)["head"]
    assert (false_claim.predicate, false_claim.source) == (true_claim.predicate, true_claim.source)
    assert "forgery" not in repr(false_claim), false_claim


def test_20iii_destroy_ends_a_sheet_and_its_hold_and_the_belief_survives_but_no_act_can_yet():
    """Through the gate at a synthetic RESOLVE barrier (`test_record_kind_fold._mint`'s shape, for a
    verb the fold will not admit): `_eff_destroy_record` removes the sheet and closes its `hold`
    (S15.3's cascade), and the surveyor's belief STANDS -- r2 §A.16, *"he still believes what it said
    and can no longer prove it"*. ⚠ THE TRIPWIRE: through the real fold the holder's own
    `destroy_record` is refused and the sheet survives, because its eligibility declines for every
    actor (`H-75`). When that changes, this assertion goes red and the test should burn through the
    fold instead."""
    w, _ = _world()
    _hear(w, "p_low", "p_high")
    P._run_d(w, lambda p, v, s, b: ([P.Act_(w, p, "survey", payload={"subject": "p_high"})]
                                    if p.id == "p_low" else []))
    (rec,) = _sheets(w)
    belief = _content_claims(w.persons["p_low"], rec.id)
    assert belief, "the survey deposited nothing, so the survival below would be vacuous"
    d = SeasonDriver(w)
    burn = Act(id="burn1", actor="p_low", verb="destroy_record", payload={"record": rec.id})
    out = _fold(w, d, burn)
    assert "record.destroyed" not in _kinds(out) and rec.id in w.records, (
        f"`destroy_record` executed through the fold ({_kinds(out)}) -- `H-75` moved; burn "
        "through the fold and narrow `H-169`")
    assert set(_kinds(out)) <= set(VERB_TABLE["destroy_record"].emits_on_refusal) | {
        "act.ineligible"}, _kinds(out)
    hold = world_q.hold_force(w, rec.id)
    w.step = Step.RESOLVE
    w.write("exists", mint_token(w, WriteClass.ACTS), None, record_kind="Record",
            fieldname="exists", driver="Act", actor="p_low", via=None,
            change=EFFECTS["destroy_record"](w, Act(id="burn2", actor="p_low",
                                                     verb="destroy_record",
                                                     payload={"record": rec.id})))
    assert rec.id not in w.records and hold.until == w.tick and not hold.live
    assert _content_claims(w.persons["p_low"], rec.id) == belief, "the belief burned with the page"


# ======================================================================================
# 5b -- v9 IN-45: THE SHEET CONSUMER, THEN `forge`, THEN WHAT READS A FORGERY DIFFERENTLY
# ======================================================================================
# The consumer is `rosters.yaml: record_sourced_operands.faction_sheet` (`to: head`), read person-side
# by `decision/options.py::_from_content_claim`: on a question about a sheet its holder holds, a
# petition is addressed to the head the sheet names (H-169 limit 5). Hand-built worlds only (v9 §0.5,
# RULED 2026-10-13): nothing here asserts a verb executed in the seed-0 realm.

def _head(w, pid):
    """Make `pid` the Crown's head: `faction_q.head` reads the live `commit` carrying a degree, and
    no builder in the tree writes one, so a true sheet names a head only on a hand-built world."""
    next(t for t in w.tenures if t.id == f"t_commit_{pid}").degree = "x"


def _hold_sheet(w, holder, verb="survey", subject="p_high"):
    """`holder` commissions (or forges) a sheet on `subject` (`p_high` unless told) through the real
    fold and, at WITNESS, holds what it says. Returns the Record and the content claim."""
    _hear(w, holder, subject)
    before = set(w.records)
    P._run_d(w, lambda p, v, s, b: ([P.Act_(w, p, verb, payload={"subject": subject})]
                                    if p.id == holder else []))
    (rid,) = set(w.records) - before
    (c,) = _content_claims(w.persons[holder], rid)
    return w.records[rid], c


def _petition_to(w, holder, rec, claim):
    """The `to` of the petition `holder` forms on the question the sheet's content claim raises
    (`questions_for`'s `claim_landed`: referent the Record, `about` the claim) -- person-side,
    through `opening_set`, the real derivation."""
    q = Question(f"q:claim:{claim.id}", "claim_landed", (rec.id,), claim.id)
    p = w.persons[holder]
    got = [c.operands for c in opening_set(p, View(holder, [], w.fixtures.get("view_k")), q,
                                           w.fixtures) if c.verb == "petition"]
    assert len(got) == 1, got
    return got[0]["to"]


def test_in45_the_sheet_consumer_addresses_a_petition_to_the_head_the_sheet_names(monkeypatch):
    """H-169 limit 5, BUILT BEFORE `forge` IS READ: a TRUE sheet (a real `survey`) naming `p_high` as
    the Crown's head, and its holder's petition on it is addressed to `p_high` -- off the sheet, not
    off the question's referent. Then folded: the petition Record names him. CONTROLS, each the
    reading with one cause removed: (a) the same world with no head -- the sheet names nobody and the
    petition falls back to the referent, as before IN-45; (b) THE MUTATION, the consumer row dropped
    from `record_sourced_operands` -- the same sheet, and the address no longer comes from it."""
    w, d = _world()
    _head(w, "p_high")
    rec, claim = _hold_sheet(w, "p_low")
    assert rec.subject_matter["head"] == "p_high", rec
    to = _petition_to(w, "p_low", rec, claim)
    assert to == "p_high", to
    out = _fold(w, d, Act(id="pet1", actor="p_low", verb="petition",
                          payload={"subject": rec.id, "to": to, "from": "Hh"}))
    assert _kinds(out) == ["petition.filed"], _kinds(out)
    assert w.records["rec:pet1"].subject_matter["to"] == ["p_high"]
    # (a) no head on the sheet: nothing to read, the referent rule as before
    w2, _ = _world()
    rec2, claim2 = _hold_sheet(w2, "p_low")
    assert rec2.subject_matter["head"] is None
    assert _petition_to(w2, "p_low", rec2, claim2) == rec2.id
    # (b) THE MUTATION: the consumer row gone, the same sheet with its head no longer read
    from ..data.requires import RECORD_SOURCED_OPERANDS
    monkeypatch.delitem(RECORD_SOURCED_OPERANDS, SHEET)
    assert _petition_to(w, "p_low", rec, claim) == rec.id


def test_in45_forge_mints_a_sheet_true_but_for_its_head_into_the_forgers_hand():
    """`_eff_forge` through the real fold: `survey`'s document (`faction_q.resolve` of the faction the
    subject coheres under, at the moment of writing) with the FORGER as its head, and the forger's
    `hold`; the one kind is `record.forged`. `forgery_quality` stays a genuine Record's `0` -- the
    field is deferred, writer with reader, to SC-02 `22b` (`H-210`), and asserted unwritten so a
    writer landing without its reader goes red here. CONTROL: in the same world a forge on a subject
    under no single faction is `forge.refused` and mints nothing -- so the mint is the subject's,
    not a verb that always writes."""
    w, d = _world()
    _hear(w, "p_other", "p_low")
    before = dict(w.records)
    assert _kinds(_fold(w, d, Act(id="f0", actor="p_other", verb="forge",
                                  payload={"subject": "p_low"}))) == ["forge.refused"]
    assert w.records == before, "a refused forge left a document behind"
    rec, _ = _hold_sheet(w, "p_other", verb="forge")
    truth = dataclasses.asdict(faction_q.resolve(w, FAC))
    assert rec.kind == SHEET and rec.subject_matter == {**truth, "head": "p_other"}, rec
    assert truth["head"] != "p_other", "the fixture: the forger is not the true head"
    assert rec.forgery_quality == 0, "a writer of `forgery_quality` landed without its reader (H-210)"
    assert world_q.hold_force(w, rec.id).subject == "p_other"
    assert "record.forged" in _kinds(w.log) and "record.created" not in _kinds(w.log)


def test_in45_forges_emits_agree_with_the_matrix_row_of_the_field_it_forges():
    """The row's falsifier: `emits:` disagreeing with the matrix row `(Record, forgery_quality)` ->
    fail. Read from both owners, never restated: the row emits exactly the kind the matrix names
    for a forgery, and the column it writes (`(Record, exists)`) carries that kind too. MUTATION:
    `emits: ["record.created"]` (the row before IN-45) reddens the first assertion. The field
    itself is not written (`H-210`): its matrix row declares `unproduced:` until SC-02 `22b`."""
    from ..data.matrix import matrix_row
    row = VERB_TABLE["forge"]
    assert row.emits == matrix_row("Record", "forgery_quality").emits == ("record.forged",), (
        row.emits, matrix_row("Record", "forgery_quality").emits)
    assert row.writes == ("Record.exists",), row.writes
    assert "record.forged" in matrix_row("Record", "exists").emits
    assert matrix_row("Record", "forgery_quality").unproduced.startswith("H-210")


def test_in45_a_forged_sheet_reads_differently_from_a_true_one_downstream():
    """ID-13's half this position can build: the forgery's CONTENT is read. Two holders of a sheet on
    the same faction -- `p_low` a true one, `p_mid` a forgery `p_other` made and gave him -- each form
    the petition the consumer addresses, and the two go to different people: the true head
    (`p_high`) and the forger. Both holders' claims are the same predicate and source (the test
    above), so it is what the document SAYS, not a flag, that moves the decision. MUTATIONS that
    redden it: `_eff_forge` not writing the forger into the sheet (both go to `p_high`); the consumer
    row dropped (both go to the referent). `forgery_quality` is not written at all (`H-210`): it
    returns with its reader at SC-02 `22b` step 25, so no field here has a writer and no reader."""
    w, _ = _world()
    _head(w, "p_high")
    true_rec, true_claim = _hold_sheet(w, "p_low")
    forged, _ = _hold_sheet(w, "p_other", verb="forge")
    P._run_d(w, lambda p, v, s, b: ([P.Act_(w, p, "give", payload={"subject": forged.id,
                                                                    "to": "p_mid"})]
                                    if p.id == "p_other" else []))
    (got,) = _content_claims(w.persons["p_mid"], forged.id)
    assert _petition_to(w, "p_low", true_rec, true_claim) == "p_high"
    assert _petition_to(w, "p_mid", forged, got) == "p_other"


# ======================================================================================
# 6 -- DONE MEANS IT RUNS: THE POPULATED REALM COMMISSIONS SHEETS ON ITS OWN
# ======================================================================================

def test_20iii_the_populated_realm_commissions_sheets_with_no_hand_built_act():
    """`CLAUDE.md` §0.2: one season of `populated.build_realm(0)` under the shipped chooser --
    `populated.run`'s own construction -- and the survey EXECUTES: at least one `faction.surveyed`,
    every sheet names a rostered faction and at least one member, and every sheet's holder holds a
    content claim equal to what it says. Refusals happen too (a referent under no single faction)
    and are counted, not asserted away. The rates are the aperture's to report, never pinned here."""
    w = populated.build_realm(0)
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                      draw=draw_factory(w.world_seed, lambda: w.tick))
    d.season(ch, question=None, subsistence=P.SUBSIST,
             contest_max_depth=w.fixtures.get("contest_max_depth"))
    kinds = _kinds(w.log)
    assert kinds.count("faction.surveyed") >= 1, "no survey executed in the populated realm"
    # v9 IN-45: A FORGED SHEET IS A SHEET TOO (`_eff_forge`, `record.forged`), so the surveys are
    # counted against the GENUINE ones -- the Records a `record.forged` Event names are set aside
    # (the field that would mark them is unwritten, `H-210`); how many forgeries the realm makes is
    # not asserted (v9 §0.5).
    forged = {c.subject for e in w.log if e.kind == "record.forged" for c in e.changes}
    sheets = [r for r in _sheets(w) if r.id not in forged]
    assert len(sheets) == kinds.count("faction.surveyed"), (len(sheets), kinds.count(
        "faction.surveyed"))
    # v9 IN-57: A SHEET WHOSE MAKER DIED IN THE SAME SEASON HAS NO LIVE HOLD (a dead person's
    # tenures leave the world), so it has no holder whose ledger can be read; it is counted, not
    # checked. MEASURED, one season of `build_realm(0)`: 4 sheets, all held, at IN-57's base
    # `5b5e31ef`; 5, all held, after it; 6 with the attention tiers and no own-act screen, one of them
    # unheld (its surveyor `p_npc_070` died at tick 0) -- the case this branch exists for.
    checked = skipped = 0
    for rec in sheets:
        assert rec.subject_matter["proposition"] in FACTION_BY_PROP, rec.subject_matter
        assert rec.subject_matter["members"], rec.subject_matter
        held = world_q.hold_force(w, rec.id)
        if held is None:
            from ..state.attribution import causing_act
            makers = {causing_act(w, e).actor for e in w.log if e.kind == "faction.surveyed"
                      and any(c.subject == rec.id for c in e.changes)}
            assert makers and not makers & set(w.persons), (
                f"{rec.id} has no live hold and its maker {makers} is alive")
            skipped += 1
            continue
        checked += 1
        holder = held.subject
        assert [c.value for c in _content_claims(w.persons[holder], rec.id)] == [
            content_value(rec.subject_matter)], (holder, rec.id)
    assert checked >= 4, (checked, skipped)
