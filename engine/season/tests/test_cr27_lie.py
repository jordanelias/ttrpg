"""v11 CR-27 (M9 taken (a)): `lie`, a spoken falsehood on a held cell claim (`H-347`; H-198 rule (i)).

`lie` is `tell`'s row with a false value: the same cell, the same contest, the same kinds, and a `said` that
`queries/person_q.py::lie_said_of` has made false at CHOOSE. It is offered while `Fixtures lie_offered` is True
(SHIPPED), `False` the swept control, and the offer is gated in `decision/options.py::opening_set`, not in
`loop/driver.py::resolvable_verbs()`. The DEED lie (H-198 rule (ii)) is unbuilt.

FALSIFIER: teller T holds `(Hh, stores:grain, 8)` firsthand, hearer H holds the same firsthand, hearer K holds
nothing on the cell. At True, T's `lie(Hh, to=K)` deposits a value other than 8 with K, T's cell claim is unchanged,
every emitted kind is one of `tell`'s, and after `lie(Hh, to=H)` H's `record(H, T)` reads below 1.0 while an honest
teller's reads 1.0 or more. PLANTED FAILURES (run 2026-11-08, each restored): `lie_said_of` returning `said_of`'s
true value reddens `test_a_lie_to_a_hearer_who_holds_nothing_...`, `test_a_lie_to_a_hearer_who_holds_the_cell_...`
and the unit tests; `opening_set`'s gate removed reddens `test_at_the_control_...`.
CONTROL: T forming `tell(Hh, to=K)` deposits 8; at False `lie` is absent from T's offered candidates, and the
realm at False is the pre-item realm (a scratch reading in the commit: `build_realm(0)` ×1 / ×2 at False equal the
base hashes).
"""
from __future__ import annotations

import dataclasses

import pytest

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import WriteClass
from ..data.verbs import LIE_VERBS, VERB_TABLE
from ..decision import options as OPT
from ..decision.options import opening_set, record
from ..epistemic import observers_for
from ..harness import probes as P
from ..harness.play_surface import dispatching_chooser
from ..loop import witness as W
from ..loop.driver import SeasonDriver, mint_token, resolvable_verbs
from ..manifest import MODULE_ENTRIES
from ..queries import person_q as PQ
from ..queries.inputs import Margin
from ..queries.person_q import drifted, lie_said_of, said_of
from ..state.carriers import Act, Claim, Event, Question, Scene, View
from ..state.ids import H

T, HOLDER, KNOWNOT = "p_low", "p_mid", "p_other"     # all three stand in `Hh`
CELL = ("Hh", "stores:grain")
TRUE_VALUE = 8
TELL_KINDS = {k for row in (VERB_TABLE["tell"],) for k in (*row.emits, *row.emits_on_refusal)}


def _world(lie_offered=True, record_gain=None):
    w = P.tiny_world()
    if record_gain is not None:
        w.fixtures = w.fixtures.sweep("record_gain", record_gain)
    w.fixtures = w.fixtures.sweep("lie_offered", lie_offered)
    for pid in (T, HOLDER):
        w.persons[pid].ledger.append(Claim(f"c_held_{pid}", pid, *CELL, TRUE_VALUE, 0, "firsthand", 80, "own"))
    assert not [c for c in w.persons[KNOWNOT].ledger if c.subject == "Hh"], "fixture: K must hold nothing on Hh"
    for pid in (HOLDER, KNOWNOT):         # T knows both hearers (`known_persons`), so `opening_set` forms a `to` for each
        w.persons[T].ledger.append(Claim(f"c_knows_{pid}", T, pid, PQ.KNOWN_PERSON_CLAIM["predicate"], True, 0,
                                         "firsthand", 80, "own"))
    return w


def _cands(w, pid=T):
    p = w.persons[pid]
    q = Question("q_cr27", "claim_landed", ("Hh",), "")
    return opening_set(p, View(p.id, [], w.fixtures.get("view_k"), q), q, w.fixtures)


def _candidate(w, verb, to):
    got = [c for c in _cands(w) if c.verb == verb and c.subject == "Hh" and c.operands.get("to") == to]
    return got[0] if got else None


def _season(monkeypatch, w, verb, to, net=3):
    """One season in which T is handed the ONE act the offered candidate makes (payload as `pack_scenes` builds
    it) and nobody else chooses; the contest is forced to `net` against obstacle 2. Returns the events."""
    cand = _candidate(w, verb, to)
    assert cand is not None, f"`{verb}` to {to} was not offered"
    d = SeasonDriver(w)                  # constructed first: the registrar fills the module table
    asked = []

    def choose(p, v, s, ask_budget, auto):
        if asked:
            return []
        asked.append(1)
        aid = H(w.world_seed, w.tick, p.id, f"act:{verb}:{to}")
        return [Scene(H(w.world_seed, w.tick, p.id, "scene:cr27"), p.id,
                      [Act(aid, p.id, verb, payload={"subject": cand.subject, **cand.operands})])]

    with monkeypatch.context() as m:
        m.setitem(MODULE_ENTRIES, "social_contest.roll", dataclasses.replace(
            MODULE_ENTRIES["social_contest.roll"], fn=lambda inp, rng: Margin(net=net, ob=2)))
        d.season(dispatching_chooser(P.NOCHOOSE, {T: choose}), question=None,
                 contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert asked, "the teller was never asked"
    return [e for e in w.log if e.kind in TELL_KINDS or e.kind.startswith("lie")]


def _told(w, pid):
    return [c for c in w.persons[pid].ledger if c.source == "told_by" and (c.subject, c.predicate) == CELL]


def _teller_cell(w):
    return [(c.subject, c.predicate, c.value, c.confidence, c.source, c.chain)
            for c in w.persons[T].ledger if (c.subject, c.predicate) == CELL]


# ---- the falsifier ------------------------------------------------------------------------------

def test_a_lie_to_a_hearer_who_holds_nothing_deposits_a_false_value_and_leaves_the_teller(monkeypatch):
    w = _world()
    before = _teller_cell(w)
    evs = _season(monkeypatch, w, "lie", KNOWNOT)
    told = _told(w, KNOWNOT)
    assert len(told) == 1 and told[0].value != TRUE_VALUE, [(c.value, c.chain) for c in told]
    assert told[0].value == 12, "ceil(0.5 * 8) = 4 above 8: one whole step of `told_drift_band`'s unit"
    assert told[0].chain == (T,), "the liar is the origin of what he says"
    assert _teller_cell(w) == before, "a lie changes nothing the liar holds"
    kinds = {e.kind for e in evs}
    assert "news.told" in kinds and kinds <= TELL_KINDS, kinds
    assert not any(e.kind.startswith("lie") for e in w.log), "there is no `lie.*` kind"


def test_a_lie_to_a_hearer_who_holds_the_cell_firsthand_lowers_the_liars_record_and_an_honest_teller_does_not(
        monkeypatch):
    w = _world(record_gain=0.5)
    _season(monkeypatch, w, "lie", HOLDER)
    told = _told(w, HOLDER)
    assert len(told) == 1 and told[0].value != TRUE_VALUE, "the lie must reach a hearer who already holds the truth"
    assert record(w.persons[HOLDER], T, w.fixtures) < 1.0
    honest = _world(record_gain=0.5)
    _season(monkeypatch, honest, "tell", HOLDER)
    assert record(honest.persons[HOLDER], T, honest.fixtures) >= 1.0


def test_the_control_tell_to_the_same_hearer_deposits_the_true_value(monkeypatch):
    w = _world()
    evs = _season(monkeypatch, w, "tell", KNOWNOT)
    told = _told(w, KNOWNOT)
    assert [c.value for c in told] == [TRUE_VALUE] and told[0].chain == (T,), told
    assert {e.kind for e in evs} <= TELL_KINDS


def test_at_the_control_lie_is_absent_from_the_offered_candidates_and_tell_is_not():
    off, on = _world(lie_offered=False), _world(lie_offered=True)
    assert not [c for c in _cands(off) if c.verb == "lie"]
    assert [c for c in _cands(off) if c.verb == "tell"], "the control must still offer `tell`"
    lies = [c for c in _cands(on) if c.verb == "lie"]
    assert lies and all(c.operands["said"].value != TRUE_VALUE for c in lies), lies
    assert DEFAULT_FIXTURES.get("lie_offered") is True, "SHIPPED True"


def test_the_offer_is_gated_in_opening_set_and_not_in_resolvable_verbs():
    assert "lie" in resolvable_verbs()          # `resolvable_verbs()` takes no fixtures: it cannot read the switch
    import inspect
    assert "lie_offered" not in inspect.getsource(resolvable_verbs)


# ---- the row ------------------------------------------------------------------------------------

def test_the_row_shares_tells_cell_and_kinds_and_mints_no_kind_of_its_own():
    lie, tell = VERB_TABLE["lie"], VERB_TABLE["tell"]
    for col in ("eligibility", "beneficiary", "counterparty", "contests", "requires_typed", "emits",
                "emits_on_refusal", "writes", "emits_by_degree", "refusals_by_clause"):
        assert getattr(lie, col) == getattr(tell, col), col
    assert LIE_VERBS == {"lie"}
    assert not any(k.startswith("lie") for r in VERB_TABLE.values() for k in (*r.emits, *r.emits_on_refusal))


# ---- the false-value rule -----------------------------------------------------------------------

def _claim(pred, value, pid="x", chain=()):
    return Claim(f"c_{pred}_{value}", pid, "S", pred, value, 0, "firsthand", 70, "own", chain=chain)


def test_a_number_moves_one_whole_step_sign_preserving_and_never_across_zero():
    fx = DEFAULT_FIXTURES                                    # band 0.5
    got = {v: lie_said_of([_claim("stores:grain", v)], "S", fx) for v in (8, 1, -8, -1, 3, -3)}
    assert {v: s.value for v, s in got.items()} == {8: 12, 1: 2, -8: -4, -1: -2, 3: 5, -3: -1}
    for v, s in got.items():
        assert s.value != v and (s.value > 0) == (v > 0), (v, s.value)
        assert s.chain == () and s.confidence == 70 and (s.subject, s.predicate) == ("S", "stores:grain")


def test_a_held_zero_a_band_of_zero_a_non_roster_value_and_a_non_cell_have_nothing_false_to_say():
    fx = DEFAULT_FIXTURES
    assert lie_said_of([_claim("stores:grain", 0)], "S", fx) is None
    assert lie_said_of([_claim("stores:grain", 8)], "S", fx.sweep("told_drift_band", 0)) is None
    assert lie_said_of([_claim("held_by:p", "a string")], "S", fx) is None
    assert lie_said_of([_claim("person.died", True)], "S", fx) is None            # a deed kind: no deed lie
    assert lie_said_of([_claim("seen", object())], "S", fx) is None
    assert lie_said_of([], "S", fx) is None


def test_a_truth_value_becomes_the_other_member_of_its_roster():
    fx = DEFAULT_FIXTURES
    assert lie_said_of([_claim("held_by:p", True)], "S", fx).value is False
    assert lie_said_of([_claim("held_by:p", False)], "S", fx).value is True


def test_a_cell_is_lied_about_even_when_a_deed_is_the_teller_s_newest_claim():
    deed = Claim("c_deed", "x", "S", "news.told", True, 9, "firsthand", 99, "own")
    got = lie_said_of([_claim("stores:grain", 8), deed], "S", DEFAULT_FIXTURES)
    assert got is not None and got.predicate == "stores:grain" and got.value == 12


def test_the_liars_number_and_the_channels_lossy_copy_are_one_rule(monkeypatch):
    """No second copy of `_told_value`'s clauses: both call `person_q.drifted`. Pinned by replacing the one owner."""
    assert drifted(8, 0.5, 0, whole_band=True) == 12
    held = Claim("c_h", "x", "S", "stores:grain", 8, 0, "firsthand", 70, "own")
    w = P.tiny_world()
    ev = Event("ev_x", "news.told", [], ["a_x"], 0, "Partial", ())
    assert W._told_value(w, "p_mid", ev, held) != 8, "the lossy copy at Partial drifts a number"
    monkeypatch.setattr(W, "drifted", lambda *a, **k: "owner")
    monkeypatch.setattr(PQ, "drifted", lambda *a, **k: "owner")
    assert W._told_value(w, "p_mid", ev, held) == "owner"
    assert lie_said_of([held], "S", DEFAULT_FIXTURES).value == "owner"


# ---- the knowledge-model fold's second falsifier (ED-IN-0327) -----------------------------------

def _two_hear_a_lie(competence_gain):
    from ..decision.options import COMPETENCE_ATTRIBUTE
    w = _world()
    w.fixtures = w.fixtures.sweep("competence_gain", competence_gain)
    w.persons[T].ledger.clear()
    w.persons[T].ledger.append(Claim("c_held", T, *CELL, TRUE_VALUE, 0, "firsthand", 37, "own"))
    for pid in (HOLDER, KNOWNOT):
        w.persons[pid].ledger.clear()
    for pid, a in ((HOLDER, 2), (KNOWNOT, 6)):
        w.persons[pid].attributes = {COMPETENCE_ATTRIBUTE: a}
    act = Act(id="a_lie_cr27", actor=T, verb="lie",
              payload={"subject": "Hh", "said": lie_said_of(w.persons[T].ledger, "Hh", w.fixtures)})
    w.acts.append(act)
    ev = Event(H(w.world_seed, w.tick, T, f"ev:news.told:{act.id}"), "news.told", [], [act.id], w.tick, "Success", ())
    w.log.append(ev)
    d = SeasonDriver(w)
    d.act_of[ev.id] = act
    chans = dict(observers_for(w, ev, "all_five", list(w.persons)))
    assert chans.get(HOLDER) == chans.get(KNOWNOT) == "co_located", chans
    d.witness(mint_token(w, WriteClass.INTERIOR), [ev])
    out = {}
    for pid in (HOLDER, KNOWNOT):
        told = _told(w, pid)
        assert len(told) == 1 and told[0].value == 12, told
        out[pid] = told[0].confidence
    return out


def test_a_lie_told_to_attunement_2_and_6_at_the_shipped_gain_is_held_equal():
    got = _two_hear_a_lie(DEFAULT_FIXTURES.get("competence_gain"))
    assert got[HOLDER] == got[KNOWNOT], got


@pytest.mark.xfail(strict=True, reason=(
    "CR-19's `competence` cannot tell a lie from a truth (`H-200`, ED-IN-0327): at a live gain the receiver at "
    "Attunement 6 holds a lie HIGHER than the one at 2. This is the falsifier the flip must pass, not a shipped "
    "behaviour (CR-19 ships at gain 0); it goes green only when CR-83's design gives the separator, and a strict "
    "xfail then fails loudly so the flip is declared."))
def test_a_lie_told_to_attunement_2_and_6_at_a_live_gain_is_not_held_higher_by_the_one_at_6():
    got = _two_hear_a_lie(0.5)
    assert got[KNOWNOT] <= got[HOLDER], got
