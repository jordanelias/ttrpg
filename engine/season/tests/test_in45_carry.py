"""v9 IN-45, `carry`'s row (`workplans/valoria_master_workplan_v9_part5.md`, batch B-K): a HELD
PETITION IS PUT BEFORE THE ROOM. `carry` was DECLINED (plan position `14`): its one write is an append
to `World.docket`, a sequence the gate has no `get()` for, so every carry would have named nothing
that moved. Built on the gate's EXISTING `entity` shape (no fourth `Subject`): the act re-winds the
petition's `Record.stages`, the petition moves and is receipted, and the docket item the same write
appends names that petition (`loop/effects_information.py::_eff_carry`).

THE FALSIFIERS, each asked of the real fold, the real loader and the real gate on a HAND-BUILT world
(`probes.tiny_world`: `p_low` files a petition about `p_mid` to the Duke, `p_high`):
  * G4: an executed carry's receipt names the petition the docket item names; and a refused carry
    leaves the docket as it was. MUTATION (seen red, 2026-10-16): `_eff_carry`'s `perform` drops
    `rec.stages = stages` -> the gate finds nothing moved, raises `NoOpReceipt`, the fold emits
    `carry.refused` -- and the docket item STANDS (the gate restores Tenures only), which
    `test_in45_a_carry_moves_the_docket_iff_its_receipt_names_the_petition` fails on.
  * the matter: the item's `matter` is the petition's `terms`. MUTATION (seen red): `matter = pid`.
  * the control: a carry by someone who does not hold the petition is refused, and so is a carry of
    a Record that is not a petition, and a second carry of a matter already on the docket.
  * composition: a bench `determine`s the carried matter (the item is the docket `open_case` writes).
No test here asserts execution in the seed-0 realm.
"""

from __future__ import annotations

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import WriteClass
from ..data.verbs import VERB_TABLE
from ..decision.options import opening_set
from ..harness import probes as P
from ..loop import effects_information as EI
from ..loop.driver import SeasonDriver, mint_token, resolvable_verbs
from ..loop.effects import EFFECTS
from ..queries import world_q
from ..state.carriers import Act, Claim, Question, Record, Tenure, View
from .test_u7_remit import JUDGE, OPENS

SEAT, DUKE = "off_duke", "p_high"
PETITIONER, PARTY, OTHER = "p_low", "p_mid", "p_other"
PETITION = "pet_in45"


def _world(fx=DEFAULT_FIXTURES):
    w = P.tiny_world(fx)
    # `issue`'s precedent in `test_u7_remit.py::_world`: the Duke knows the party a bench would bind.
    w.persons[DUKE].ledger.append(Claim("c_knows_party", DUKE, PARTY, "exists:Person", 1, 0,
                                        "firsthand", 100, "own"))
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _fold(w, d, *acts):
    out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts),
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return out


def _kinds(events):
    return [e.kind for e in events]


def _filed(fx=DEFAULT_FIXTURES):
    """A world where `p_low` has filed a petition about `p_mid`, through the real `petition` fold."""
    w, d = _world(fx)
    out = _fold(w, d, Act(id="file", actor=PETITIONER, verb="petition",
                          payload={"record": PETITION, "subject": PARTY, "to": DUKE, "from": "Hh"}))
    assert _kinds(out) == ["petition.filed"], _kinds(out)
    assert w.records[PETITION].subject_matter["terms"] == PARTY
    assert world_q.hold_force(w, PETITION).subject == PETITIONER
    return w, d


def _carry(key, actor=PETITIONER, subject=PETITION):
    return Act(id=key, actor=actor, verb="carry", payload={"subject": subject})


def test_in45_carry_is_resolvable_on_a_typed_cell_and_an_effect():
    assert "carry" in resolvable_verbs()
    assert EFFECTS["carry"] is EI._eff_carry
    row = VERB_TABLE["carry"]
    assert row.writes == ("Record.stages", "DocketItem.matter",
                          "DocketItem.arrangement", "DocketItem.petition"), row.writes
    assert not row.effect_decline_note, "a row with an effect keeps no decline note"


def test_in45_a_carry_moves_the_docket_iff_its_receipt_names_the_petition():
    """G4: the success Event's receipts name exactly the petition, the item appended names the same
    petition, and the petition's stages were re-wound by the carrying act. A refused carry (the
    non-holder) leaves the docket untouched -- the invariant the stage-write mutation breaks."""
    w, d = _filed()
    before = list(w.docket)
    out = _fold(w, d, _carry("c_no", actor=OTHER))
    assert _kinds(out) == ["carry.refused"], _kinds(out)
    assert w.docket == before, "a refused carry moved the docket"
    out = _fold(w, d, _carry("c_yes"))
    grew = [i for i in w.docket if i not in before]
    # THE INVARIANT FIRST: the docket moved exactly when a success Event receipted the write.
    assert bool(grew) == (_kinds(out) == ["petition.carried"]), (
        f"docket grew by {grew} under {_kinds(out)} -- an unreceipted docket write (G4 bypassed)")
    assert _kinds(out) == ["petition.carried"], _kinds(out)
    ev, = out
    assert [c.subject for c in ev.changes] == [PETITION], ev.changes
    item, = [i for i in w.docket if i not in before]
    assert item[world_q.DOCKET_PETITION] == PETITION, item
    assert item[world_q.DOCKET_ARRANGEMENT] is None and item["date"] is None, item
    stages = w.records[PETITION].stages
    assert stages and all(s[2] == "c_yes" for s in stages), stages


def test_in45_a_carried_petition_puts_its_terms_before_the_room():
    """The matter is what the petition is ABOUT (`terms`, here `p_mid`), not the petition's own id
    and not its petitioner. MUTATION: `matter = pid` in `_eff_carry` -> red here."""
    w, d = _filed()
    assert world_q.docketed(w, PARTY) == []
    assert _kinds(_fold(w, d, _carry("c1"))) == ["petition.carried"]
    item, = world_q.docketed(w, PARTY)
    assert item["matter"] == w.records[PETITION].subject_matter["terms"] == PARTY, item
    assert world_q.docketed(w, PETITION) == [] and world_q.docketed(w, PETITIONER) == []


def test_in45_carry_is_refused_without_a_held_petition():
    """CONTROLS, each one clause from the executing carry: a carrier who does not hold the petition
    (`held_by`); a held Record that is not a petition (`existence`, kind); a second carry of a
    matter already before the room (the effect's `docketed` decline, `open_case`'s). Each refusal
    leaves the docket empty of the matter."""
    w, d = _filed()
    assert _kinds(_fold(w, d, _carry("c_other", actor=OTHER))) == ["carry.refused"]
    assert _kinds(_fold(w, d, _carry("c_duke", actor=DUKE))) == ["carry.refused"]
    assert world_q.docketed(w, PARTY) == []
    w.records["txt_in45"] = Record("txt_in45", "Hh", "text")
    w.add_tenure(Tenure("hold:txt_in45", PETITIONER, "txt_in45", "hold", since=w.tick))
    assert _kinds(_fold(w, d, _carry("c_text", subject="txt_in45"))) == ["carry.refused"]
    assert world_q.docketed(w, PARTY) == []
    assert _kinds(_fold(w, d, _carry("c_first"))) == ["petition.carried"]
    assert _kinds(_fold(w, d, _carry("c_again"))) == ["carry.refused"]
    assert len(world_q.docketed(w, PARTY)) == 1


def _carries(w, p, q, shipped=True):
    """The `carry` Candidates `p` forms on `q`, through the real `opening_set`. `shipped` False reads it
    with `carry`'s `referent_class` blanked in-process (see the test below): the formation of the REM-24
    tree (`f2381695`), which the first test below was written against."""
    import dataclasses
    from unittest import mock
    from ..decision import options as _options
    table = VERB_TABLE if shipped else {
        **VERB_TABLE, "carry": dataclasses.replace(VERB_TABLE["carry"], referent_class="")}
    with mock.patch.object(_options, "VERB_TABLE", table):
        return [c for c in opening_set(p, View(p.id, [], w.fixtures.get("view_k")), q, w.fixtures)
                if c.verb == "carry"]


def test_in45_the_petitioner_forms_a_carry_on_a_question_naming_his_petition():
    """WIRED, person-side: `opening_set` forms `carry` on a petition the question names (a filed
    petition reaches its petitioner's questions through his `claim_landed` deposits). CONTROL: a
    question naming nothing forms no `carry`.

    v10 REM-25 (B10-05): READ WITH `carry`'s `referent_class: Record` BLANKED IN-PROCESS -- the formation
    of the REM-24 tree, which this test was written against. THE UNIT AND THE REASON: `carry` declares
    `Record` and forms on a Record-classed referent alone, and a hand-written Question naming the petition
    among its PLAIN referents carries no class, so under the shipped table it forms none -- asserted by
    `test_rem25_carry_forms_on_the_petition_he_holds_and_not_on_a_question_that_merely_names_it` below. What
    this test asserts (the referent binds `subject`, a question naming nothing forms none) is unchanged and
    still executes; the shipped route is the holding one."""
    w, _d = _filed()
    p = w.persons[PETITIONER]
    got = [c.subject for c in _carries(w, p, Question("q:in45", "need", (PETITION,)), shipped=False)]
    assert got == [PETITION], got
    none = _carries(w, p, Question("q:in45:0", "need", ()), shipped=False)
    assert none == [], none


def test_rem25_carry_forms_on_the_petition_he_holds_and_not_on_a_question_that_merely_names_it():
    """THE NEW BEHAVIOUR, WHERE THE CONSUMER IS TESTED (v10 REM-25, B10-05): under the shipped class the
    petitioner is asked a question by the real `questions_for` and it carries his held petition as a
    `Record`, so `carry` forms on it -- but a Question that only NAMES the petition among its plain referents
    (a claim's subject, a hand-written one) forms no `carry`. CONTROLS: with the column blanked the plain
    Question forms one (so it is the class that closes that route), and `p_mid`, who holds no petition, is
    stamped none and forms none."""
    w, _d = _filed()
    p = w.persons[PETITIONER]
    plain = Question("q:in45", "need", (PETITION,))
    assert _carries(w, p, plain) == []
    assert [c.subject for c in _carries(w, p, plain, shipped=False)] == [PETITION]
    (held,) = world_q.questions_for(w, p)
    assert (PETITION, "Record") in held.classes, held
    assert [c.subject for c in _carries(w, p, held)] == [PETITION]
    q_mid = world_q.questions_for(w, w.persons[PARTY])
    assert not [r for q in q_mid for r, k in q.classes if k == "Record"], q_mid
    assert world_q.records_held_for_holding_rows(w, w.persons[PARTY]) == ()
    assert world_q.records_held_for_holding_rows(w, p) == (PETITION,)


def test_in45_a_bench_determines_a_carried_matter():
    """The carried item is the docket `open_case` writes: the Duke's bench `determine`s the party
    and takes the matter off it. CONTROL: with no carry the same determination is refused (nothing
    on the docket). v9 SC-03b: `determine` is contested, so the bench is a STRONG JUDGE (`pool_default`
    30, as `test_u7_remit.JUDGE`) and the control asserts the band it opened at."""
    w, d = _filed(DEFAULT_FIXTURES.sweep("pool_default", JUDGE["pool_default"]))
    det = Act(id="dt0", actor=DUKE, verb="determine", via=SEAT, payload={"subject": PARTY})
    assert _kinds(_fold(w, d, det)) == ["determine.refused"]
    assert _kinds(_fold(w, d, _carry("c1"))) == ["petition.carried"]
    det = Act(id="dt1", actor=DUKE, verb="determine", via=SEAT, payload={"subject": PARTY})
    out = _fold(w, d, det)
    assert _kinds(out) == ["matter.determined"] and out[0].degree in OPENS, out
    assert world_q.docketed(w, PARTY) == []


def test_in45_carry_at_stages_arm_0_is_refused():
    """H-80's declared sweep, ARM 0 (B-K close, COR 2 / LOG 8): at `record_stages_default` = 0 the
    filing and the carriage both wind `[]`, so `_eff_carry`'s same-stages decline REFUSES the holder's
    carry and nothing reaches the docket. This PINS the latent refusal registered at `H-80`; it does
    not bless it. CONTROL, one change: the shipped arm (3) carries the same petition."""
    w, d = _filed(DEFAULT_FIXTURES.sweep("record_stages_default", 0))
    assert w.records[PETITION].stages == [], w.records[PETITION].stages   # anti-vacuity: arm 0
    assert _kinds(_fold(w, d, _carry("c0"))) == ["carry.refused"]
    assert world_q.docketed(w, PARTY) == []
    w, d = _filed()
    assert DEFAULT_FIXTURES.get("record_stages_default") >= 1
    assert _kinds(_fold(w, d, _carry("c3"))) == ["petition.carried"]
