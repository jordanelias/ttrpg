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

from ..data.matrix import WriteClass
from ..data.rosters import RECORD_CONTENT
from ..loop import witness as WIT
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..queries.person_q import addressed_to, said_of
from ..state.carriers import Act, Claim, Event, Tenure
from ..state.ids import H
from .test_in10_record_operands import _resolve
from .test_in12_covenant import DUKE, OTHER, SEAT, _covenant, _utter, _world

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
