"""`06_FA_decree_binds` (V12 B21.17, B21.18, then B21.22, B21.23) -- A DECREE IS PROCLAIMED: whoever learns that a writ was
made by `issue` holds its terms (ruling A-21), while a covenant's counterparty learns them only from the paper.

B21.18 (edit 2): `loop/witness.py::addressee_reads` reads `rosters.yaml: proclaimed` (`data/rosters.py::PROCLAIMED`) beside
`read_to_addressee`, both qualified by the verb of the Record's creating act (`queries/world_q.py::minting_verb`), so WITNESS's
fourth deposit gives `content:dispensation` to every witness of an `issue` (the chronicle channel's `told_by` witnesses
included: they learn the terms with the news) and to nobody new for a `covenant`. The told branch (a `tell` of a proclaimed
Record) deposits the terms as a second told claim on the same telling. Every test drives a hand-built world (`tiny_world` via
`test_in12_covenant._world`) through the real fold (`SeasonDriver.resolve`) and the real WITNESS.

MUTATIONS, run once at B21.18's build (receipt; not kept): the `PROCLAIMED` branch dropped from `addressee_reads` -> the
bystander test RED; the verb qualifier dropped (`rec.kind in PROCLAIMED`) -> the covenant test RED; the told branch's second
claim dropped -> the hearer test RED.
"""

from __future__ import annotations

import pytest

from ..data.matrix import WriteClass
from ..data.rosters import RECORD_CONTENT
from ..loop import witness as WIT
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..queries.person_q import addressed_to, said_of
from ..state.carriers import Act, Claim, Event, Office, Tenure
from ..state.ids import H
from .test_in10_record_operands import _resolve
from .test_in12_covenant import DUKE, OTHER, SEAT, _covenant, _utter, _world
from .test_in53_vacancy_need import _formed
from ._seat_at_success import writ_at_success  # noqa: F401  (the fixture; its reason is in its module)

pytestmark = pytest.mark.usefixtures("writ_at_success")   # B21.56: the decree's reach and answers are the fold's; the draw is D3's test

_CONTENT = RECORD_CONTENT["predicate"]
BYSTANDERS = ("p_low", "p_mid", "p_other")      # neither the issuer, nor the writ's addressee (`OTHER`)


def revert_b21_18(monkeypatch) -> None:
    """B21.18 AT ITS REVERT, for the life of one test: `proclaimed` read as `{}` where it is read (the content deposit and the
    told branch, `witness.PROCLAIMED`; the writ limb of `admits_audience`, `world_q.WRIT_MINTING_VERBS`). A test pinning a
    pre-B21.18 hash calls it."""
    monkeypatch.setattr(WIT, "PROCLAIMED", {})
    monkeypatch.setattr(world_q, "WRIT_MINTING_VERBS", frozenset())


def _issue(w, d, key="fa_is", witness=True):
    """`DUKE`, through his seat, issues a writ on `S` (whose grain he holds a claim of: the `terms` conjunct) to `OTHER`."""
    w.persons[DUKE].ledger.append(Claim(f"c_{key}", DUKE, "S", "stores:grain", 8, 0, "firsthand", 100, "own"))
    out = _resolve(w, d, Act(id=key, actor=DUKE, verb="issue", via=SEAT, payload={"subject": "S", "to": OTHER}))
    assert [e.kind for e in out] == ["dispensation.issued"], [e.kind for e in out]
    if witness:
        d.witness(mint_token(w, WriteClass.INTERIOR), out)
    return w.records[f"rec:{key}"]


def _content(w, pid, rec):
    return [c for c in w.persons[pid].ledger if c.subject == rec.id and c.predicate == f"{_CONTENT}:{rec.kind}"]


def _witnessed(w, pid, rec, kind):
    return any(c.subject == rec.id and c.predicate == kind for c in w.persons[pid].ledger)


def test_a_bystander_who_witnessed_the_issue_holds_its_terms():
    """A-21: a person who learns a decree was issued holds its terms, though it names him nowhere and he holds no paper."""
    w, d = _world()
    rec = _issue(w, d)
    said = WIT.content_value(rec.subject_matter)
    checked = 0
    for pid in BYSTANDERS:
        assert not addressed_to(rec.subject_matter, pid) and world_q.hold_force(w, rec.id).subject != pid
        assert _witnessed(w, pid, rec, "dispensation.issued"), f"{pid} did not witness the issue: the fixture moved"
        got = _content(w, pid, rec)
        assert [c.value for c in got] == [said], (pid, got)
        assert got[0].source == "told_by", "the chronicle's witness learns the terms with the news, at its source"
        checked += 1
    assert checked >= 3


def test_a_covenant_counterparty_holds_no_content_claim():
    """D-U1-05's falsifier: `covenant` mints a `dispensation` through `issue`'s body, and its counterparty, who witnesses
    the making and is its addressee, still learns its terms only from the paper (A-21 keeps covenants in person)."""
    w, d = _world()
    prop = _utter(w, d)
    out = _resolve(w, d, _covenant(prop))
    assert [e.kind for e in out] == ["covenant.offered"]
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    rec = w.records["rec:cv_c"]
    assert rec.kind == "dispensation" and addressed_to(rec.subject_matter, OTHER)
    checked = 0
    for pid in (OTHER, *BYSTANDERS):
        if pid == OTHER:
            assert _witnessed(w, pid, rec, "covenant.offered"), "the counterparty did not witness: the fixture moved"
        assert _content(w, pid, rec) == [], pid
        checked += 1
    assert checked >= 4
    assert _content(w, DUKE, rec), "CONTROL: the maker holds the paper, and so its terms"


def _tell_the_issue(w, d, rec, hearer="p_low"):
    """`DUKE` tells what he holds of `rec` (that it was issued, and nothing of its terms) to `hearer`, knotted to him; the
    issue itself was not witnessed, so the telling is the only way `hearer` learns of it."""
    w.add_tenure(Tenure("t_knot_fa18", DUKE, hearer, "knot", since=0))
    teller = w.persons[DUKE]
    teller.ledger.append(Claim("c_fa18_iss", DUKE, rec.id, "dispensation.issued", True, w.tick, "firsthand", 100, "own"))
    said = said_of(teller.ledger, rec.id, w.fixtures)
    assert said is not None and said.predicate == "dispensation.issued", said
    act = Act(id="a_tell_fa18", actor=DUKE, verb="tell", payload={"subject": rec.id, "said": said})
    w.acts.append(act)
    ev = Event(H(w.world_seed, w.tick, DUKE, f"ev:news.told:{act.id}"), "news.told", [], [act.id], w.tick, "Success", ())
    w.log.append(ev)
    d.act_of[ev.id] = act
    d.witness(mint_token(w, WriteClass.INTERIOR), [ev])


def test_a_hearer_told_of_the_issue_holds_its_terms():
    """The told branch: a person TOLD that a decree was issued holds its terms, as a told claim on the same telling."""
    w, d = _world()
    rec = _issue(w, d, witness=False)
    _tell_the_issue(w, d, rec)
    told = [c for c in w.persons["p_low"].ledger if c.subject == rec.id and c.source == "told_by"]
    assert {c.predicate for c in told} >= {"dispensation.issued"}, "the telling reached no one: the fixture moved"
    got = _content(w, "p_low", rec)
    assert [(c.value, c.source, c.chain) for c in got] == [(WIT.content_value(rec.subject_matter), "told_by", (DUKE,))], got


def _scene(w, d):
    rec = _issue(w, d, key="fa_h1")
    prop = _utter(w, d)
    out = _resolve(w, d, _covenant(prop))
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    w2_rec = _issue(w, d, key="fa_h2", witness=False)
    _tell_the_issue(w, d, w2_rec, hearer="p_mid")
    return rec


def test_dispensation_absent_from_proclaimed_reproduces_the_hash(monkeypatch):
    """CONTROL: with the `dispensation` entry absent from `proclaimed`, the hand-built scene (an issue witnessed, a covenant
    witnessed, an issue told) ends in the world the pre-B21.18 rule leaves -- `addressee_reads` as `read_to_addressee` by
    kind alone -- and with the entry present it ends elsewhere (so the comparison can see the item). The realm reading
    (seed 0, one and two seasons) is the item's receipt, not an assertion here."""
    hashes = {}
    for arm in ("treatment", "revert", "pre_item"):
        with monkeypatch.context() as m:
            if arm != "treatment":
                revert_b21_18(m)
            if arm == "pre_item":
                m.setattr(WIT, "addressee_reads", lambda rec, pid, *_: (rec.kind in WIT.READ_TO_ADDRESSEE
                                                                        and addressed_to(rec.subject_matter, pid)))
            w, d = _world()
            _scene(w, d)
            hashes[arm] = w.content_hash()
    assert hashes["revert"] == hashes["pre_item"], hashes
    assert hashes["treatment"] != hashes["revert"], "the scene cannot see the item"


# B21.22 (edit 3): WHO IS OFFERED THE ANSWER -- `world_q.writs_addressed`, the writs a person holds addressed to him OR
# whose terms his own ledger holds naming him, where the issuing seat commands him (A-22), less those he answered.

THREE = ("comply", "evade / defy", "construe")
EMITS = {"comply": "compliance.given", "evade / defy": "compliance.withheld", "construe": "terms.distorted"}


def _offered(w, pid, rid):
    """The answers formed on `rid` over every question `pid` is asked (`opening_set`, the real formation)."""
    return {c.verb for q in world_q.questions_for(w, w.persons[pid])
            for c in _formed(w, pid, q) if c.verb in THREE and c.subject == rid}


def test_an_addressee_is_offered_comply_defy_construe():
    """A-21 with A-22: the addressee witnessed the issue, holds its terms and no paper, and the issuing seat commands
    him (an unseated man in its land): he is offered all three answers. CONTROL: the issuer, who holds the paper and the
    terms and is not its addressee, is offered none."""
    w, d = _issue_scene()
    rec = w.records["rec:fa_is"]
    assert world_q.hold_force(w, rec.id).subject == DUKE and _content(w, OTHER, rec), "fixture: terms without paper"
    assert world_q.commands(w, DUKE, SEAT, OTHER), "fixture: the seat commands the addressee"
    assert world_q.writs_addressed(w, w.persons[OTHER]) == (rec.id,)
    assert _offered(w, OTHER, rec.id) == set(THREE)
    assert world_q.writs_addressed(w, w.persons[DUKE]) == () and not _offered(w, DUKE, rec.id)


def _issue_scene():
    w, d = _world()
    _issue(w, d)
    return w, d


@pytest.mark.parametrize("verb,netted", [("comply", True), ("evade / defy", True), ("construe", False)])
def test_writs_addressed_nets_an_answered_writ(verb, netted):
    """Edit 3's third clause: an addressee who has complied or withheld compliance (a claim of his own doing on the writ,
    in his own ledger) is not offered the writ again; a construal is a reading, not an answer, and nets nothing. CONTROL:
    a witnessed answer on the same writ (the claim, no `doer`) leaves the writ offered."""
    w, d = _issue_scene()
    rec, other = w.records["rec:fa_is"], w.persons[OTHER]
    other.ledger.append(Claim("c_seen_answer", OTHER, rec.id, EMITS["comply"], True, w.tick, "firsthand", 100, "own"))
    assert world_q.writs_addressed(w, other) == (rec.id,), "a witnessed answer is not his own"
    out = _resolve(w, d, Act(id="fa_ans", actor=OTHER, verb=verb, payload={"subject": rec.id}))
    assert EMITS[verb] in [e.kind for e in out], [e.kind for e in out]
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    assert any(c.subject == rec.id and c.predicate == EMITS[verb] and c.doer == OTHER for c in other.ledger), \
        "WITNESS deposited no claim of his own answer: the fixture moved"
    assert world_q.writs_addressed(w, other) == (() if netted else (rec.id,))
    assert bool(_offered(w, OTHER, rec.id)) is not netted


def test_a_bystander_is_offered_nothing():
    """The B10-05 close's defect must not return under A-21: each bystander witnessed the issue, holds the
    `content:dispensation` claim and is a man the issuing seat commands, yet is not the writ's addressee -- so
    `writs_addressed` is empty for him and no answer forms."""
    w, d = _issue_scene()
    rec = w.records["rec:fa_is"]
    checked = 0
    for pid in BYSTANDERS:
        assert _content(w, pid, rec) and world_q.commands(w, DUKE, SEAT, pid), f"{pid}: the fixture moved"
        assert world_q.writs_addressed(w, w.persons[pid]) == (), pid
        assert not _offered(w, pid, rec.id), pid
        checked += 1
    assert checked >= 3


def test_a_writ_to_the_issuers_superior_forms_no_comply():
    """A-22: a writ whose addressee the issuing seat does not command is a petition to him, not an order. The addressee,
    commanded while unseated, takes the Crown (a seat the Duke's may not revoke): the writ he knows of now forms no
    answer. CONTROL: the same writ before he is seated is offered."""
    w, d = _issue_scene()
    rec, other = w.records["rec:fa_is"], w.persons[OTHER]
    assert world_q.writs_addressed(w, other) == (rec.id,), "control: commanded, the writ is his to answer"
    w.offices["off_crown"] = Office("off_crown", "King", "R", ["confer", "revoke"], faction="Valorsmark")
    w.add_tenure(Tenure("t_fa_crown", OTHER, "off_crown", "hold", since=w.tick))
    assert not world_q.commands(w, DUKE, SEAT, OTHER), "fixture: the Duke's seat commands the King"
    assert world_q.writs_addressed(w, other) == ()
    assert not _offered(w, OTHER, rec.id)


# B21.23 (edit 4): SUSPICION IS A FOLD, AND DEFIANCE OPENS THE ISSUER'S RECALL -- `person_q.suspicion_of` counts the seasons in
# which the writ-maker's own ledger holds a withheld answer, less those he holds only a given one (E11), floored at zero, and
# `world_q.recalls` names the defier and his seats `may_revoke` admits once it reaches `Fixtures recall_suspicion`.

STEWARD = "off_steward"
DEFY, COMPLY = "evade / defy", "comply"


def _recall_scene():
    """The Duke's seat on the rung above a Steward's, in his faction (`rung_above_same_faction`), and `OTHER` the Steward."""
    w, d = _world()
    w.offices[STEWARD] = Office(STEWARD, "Steward", "S", ["issue"], faction="Valorsmark", revocation="rung_above_same_faction")
    w.add_tenure(Tenure("t_fa_stw", OTHER, STEWARD, "hold", since=w.tick))
    assert world_q.may_revoke(w, DUKE, SEAT, w.offices[STEWARD]), "fixture: the Duke's seat may strip the Steward's"
    return w, d


def _season(w, d, season, *answers):
    """One season: the Duke issues a writ to `OTHER` for each answer, and `OTHER` answers it (`comply` or `evade / defy`)."""
    w.tick = season
    for n, verb in enumerate(answers):
        key = f"fa_s{season}_{n}"
        rec = _issue(w, d, key=key)
        out = _resolve(w, d, Act(id=f"{key}_ans", actor=OTHER, verb=verb, payload={"subject": rec.id}))
        assert EMITS[verb] in [e.kind for e in out], [e.kind for e in out]
        d.witness(mint_token(w, WriteClass.INTERIOR), out)


def _recall_named(w):
    """Does the question the Duke is next delivered carry the Steward as a `Person` and his seat as an `Office` referent?"""
    qs = world_q.questions_for(w, w.persons[DUKE])
    return any(OTHER in q.referents_for("Person") and STEWARD in q.referents_for("Office") for q in qs)


def test_suspicion_floors_at_zero_and_a_complied_season_delays_the_recall():
    """Edit 4, D6 and E11: at the shipped 3 the Duke's question names the Steward and his seat after three defied seasons, and
    not before; a complied season between them delays it by one; the cap is one a season; the fold floors at zero; and the
    recall names only a seat `may_revoke` admits. At the sweep arm 1, one withheld answer is enough; at `None` (the revert) the
    occasion is off."""
    from ..queries import person_q

    def sus(w):
        return person_q.suspicion_of(w.persons[DUKE], OTHER)
    w, d = _recall_scene()
    assert w.fixtures.get("recall_suspicion") == 3, "the shipped value"
    checked = 0
    for season in (0, 1):
        _season(w, d, season, DEFY)
        assert sus(w) == season + 1 and not _recall_named(w), season
        checked += 1
    _season(w, d, 2, DEFY)
    assert sus(w) == 3 and _recall_named(w) and world_q.recalls(w, w.persons[DUKE]) == (OTHER, STEWARD)
    # a seat the Duke's may not strip is not named (the gate's own predicate): the Steward also sits on the Crown
    w.offices["off_crown"] = Office("off_crown", "King", "R", ["confer", "revoke"], faction="Valorsmark")
    w.add_tenure(Tenure("t_fa_crown", OTHER, "off_crown", "hold", since=w.tick))
    assert not world_q.may_revoke(w, DUKE, SEAT, w.offices["off_crown"])
    assert world_q.recalls(w, w.persons[DUKE]) == (OTHER, STEWARD)
    # E11: a complied season in between delays the recall by one season
    w, d = _recall_scene()
    for season, verb in enumerate((DEFY, COMPLY, DEFY, DEFY)):
        _season(w, d, season, verb)
        checked += 1
    assert sus(w) == 2 and not _recall_named(w), "defy, comply, defy, defy: three less one"
    _season(w, d, 4, DEFY)
    assert sus(w) == 3 and _recall_named(w)
    # the cap: two withheld answers in one season count once
    w, d = _recall_scene()
    _season(w, d, 0, DEFY, DEFY)
    assert sus(w) == 1
    # the floor: obedience banks no credit below zero
    w, d = _recall_scene()
    _season(w, d, 0, DEFY)
    for season in (1, 2, 3):
        _season(w, d, season, COMPLY)
    assert sus(w) == 0
    _season(w, d, 4, COMPLY)
    assert sus(w) == 0 and not _recall_named(w)
    # the sweep arm and the revert, on one season's defiance
    w, d = _recall_scene()
    _season(w, d, 0, DEFY)
    assert not _recall_named(w)
    w.fixtures = w.fixtures.sweep("recall_suspicion", 1)
    assert _recall_named(w)
    w.fixtures = w.fixtures.sweep("recall_suspicion", None)
    assert not _recall_named(w) and world_q.recalls(w, w.persons[DUKE]) == ()
    assert checked >= 6
