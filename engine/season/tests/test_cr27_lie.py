"""v11 CR-27 (M9 taken (a)): `lie`, a spoken falsehood on a held cell claim (`H-357`; H-198 rule (i)).

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


def _cands(w, pid=T, subject="Hh"):
    p = w.persons[pid]
    q = Question("q_cr27", "claim_landed", (subject,), "")
    return opening_set(p, View(p.id, [], w.fixtures.get("view_k"), q), q, w.fixtures)


def _candidate(w, verb, to, subject="Hh"):
    got = [c for c in _cands(w, subject=subject) if c.verb == verb and c.subject == subject and c.operands.get("to") == to]
    return got[0] if got else None


def _season(monkeypatch, w, verb, to, net=3, subject="Hh"):
    """One season in which T is handed the ONE act the offered candidate makes (payload as `pack_scenes` builds
    it) and nobody else chooses; the contest is forced to `net` against obstacle 2. Returns the events."""
    cand = _candidate(w, verb, to, subject)
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

def _less_own_kind(col):
    """A column less `scruple.overridden` (B10.24): `lie` is a refusable row, so it declares the act's own kind beside `tell`'s."""
    if isinstance(col, dict):
        return {k: _less_own_kind(v) for k, v in col.items()}
    return type(col)(k for k in col if k != "scruple.overridden") if isinstance(col, (tuple, list)) else col


def test_the_row_shares_tells_cell_and_kinds_and_mints_no_kind_of_its_own():
    lie, tell = VERB_TABLE["lie"], VERB_TABLE["tell"]
    for col in ("eligibility", "beneficiary", "counterparty", "contests", "requires_typed", "emits",
                "emits_on_refusal", "writes", "emits_by_degree", "refusals_by_clause"):
        assert _less_own_kind(getattr(lie, col)) == getattr(tell, col), col
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


def test_numeric_lie_forms_both_directions_on_a_quantity():
    """B11.54: a liar of a held amount may say it moved either way -- `lie_said_of` gives one `Said` per direction (the upward whole step, then the downward), `opening_set`
    forms one `lie` Candidate per `Said`; the control, a `tell` (a row not in `lie_verbs`), forms the one Candidate saying the held value as it holds it. A step that
    would reach zero comes back as the upward one, so a held 1 has one false number (2), not two."""
    fx = DEFAULT_FIXTURES                                    # band 0.5
    assert [s.value for s in lie_said_of([_claim("stores:grain", 8)], "S", fx)] == [12, 4]
    assert [s.value for s in lie_said_of([_claim("stores:grain", 1)], "S", fx)] == [2]
    assert [s.value for s in lie_said_of([_claim("stores:grain", -3)], "S", fx)] == [-1, -5]
    assert lie_said_of([_claim("stores:grain", 0)], "S", fx) == ()
    for said in lie_said_of([_claim("stores:grain", 8)], "S", fx):
        assert said.chain == () and said.confidence == 70 and (said.subject, said.predicate) == ("S", "stores:grain")
    w = _world()
    lies = [c.operands["said"].value for c in _cands(w) if c.verb == "lie" and c.operands.get("to") == KNOWNOT]
    assert set(lies) == {4, 12} and lies.count(4) == lies.count(12), lies    # the falsifier: one direction only fails here (`in_confidence` fans each said twice)
    tells = [c.operands["said"].value for c in _cands(w) if c.verb == "tell" and c.operands.get("to") == KNOWNOT]
    assert tells and set(tells) == {TRUE_VALUE}, tells         # the control: a row not in `lie_verbs` is unchanged
    ranks = [c.operands.get("said_rank") for c in _cands(w) if c.verb == "lie" and c.operands.get("to") == KNOWNOT]
    assert set(ranks) == {0, 1}, ranks                     # distinct act ids: the rank is what `choice_values` reads


def test_a_held_zero_a_band_of_zero_a_non_roster_value_and_a_non_cell_have_nothing_false_to_say():
    fx = DEFAULT_FIXTURES
    assert lie_said_of([_claim("stores:grain", 0)], "S", fx) == ()
    assert lie_said_of([_claim("stores:grain", 8)], "S", fx.sweep("told_drift_band", 0)) == ()
    assert lie_said_of([_claim("held_by:p", "a string")], "S", fx) == ()
    assert lie_said_of([_claim("person.died", True)], "S", fx) == ()            # a deed kind: no deed lie
    assert lie_said_of([_claim("seen", object())], "S", fx) == ()
    assert lie_said_of([], "S", fx) == ()


def test_a_truth_value_becomes_the_other_member_of_its_roster():
    fx = DEFAULT_FIXTURES
    assert [s.value for s in lie_said_of([_claim("held_by:p", True)], "S", fx)] == [False]
    assert [s.value for s in lie_said_of([_claim("held_by:p", False)], "S", fx)] == [True]


def test_a_cell_is_lied_about_even_when_a_deed_is_the_teller_s_newest_claim():
    deed = Claim("c_deed", "x", "S", "news.told", True, 9, "firsthand", 99, "own")
    got = lie_said_of([_claim("stores:grain", 8), deed], "S", DEFAULT_FIXTURES)
    assert got and {s.predicate for s in got} == {"stores:grain"} and [s.value for s in got] == [12, 4]


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
    assert [s.value for s in lie_said_of([held], "S", DEFAULT_FIXTURES)] == ["owner"]


# ---- the knowledge-model fold's second falsifier (ED-IN-0327) -----------------------------------

def _two_hear_a_lie(competence_gain):
    from ..data.rosters import capability_uses
    w = _world()
    w.fixtures = w.fixtures.sweep("competence_gain", competence_gain)
    w.persons[T].ledger.clear()
    w.persons[T].ledger.append(Claim("c_held", T, *CELL, TRUE_VALUE, 0, "firsthand", 37, "own"))
    for pid in (HOLDER, KNOWNOT):
        w.persons[pid].ledger.clear()
    for pid, a in ((HOLDER, 2), (KNOWNOT, 6)):
        w.persons[pid].attributes = {next(r.key for r in capability_uses() if r.use == "told_claim_credit"): a}
    act = Act(id="a_lie_cr27", actor=T, verb="lie",
              payload={"subject": "Hh", "said": lie_said_of(w.persons[T].ledger, "Hh", w.fixtures)[0]})
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


def test_a_lie_told_to_attunement_2_and_6_at_a_live_gain_is_held_higher_by_the_one_at_6_until_cr83():
    """THE MEASURED GAP, PINNED (`H-200`, ED-IN-0327): CR-19's `competence` cannot tell a lie from a truth, so at a
    live gain the receiver at Attunement 6 holds a lie HIGHER than the one at 2. The falsifier guards the flip
    CR-83's design schedules (`workplans/valoria_master_workplan_v11_part4.md:119`), not the shipped value
    (CR-19 ships at gain 0). THIS ASSERT TURNS RED WHEN CR-83 SUPPLIES THE LIE/TRUTH SEPARATOR; invert it then to
    the plan's form, `got[KNOWNOT] <= got[HOLDER]` (plan rule P8 forbids a standing xfail, so the gap is asserted
    as it is)."""
    got = _two_hear_a_lie(0.5)
    assert got[KNOWNOT] > got[HOLDER], got


# ---- a rumour garbles only an amount (v12 B11.51, `16_PESSIMIST_FI_A` edits 1-3) ----------------------------------

def _partial_telling(w, hearer, held, n):
    """What `hearer` receives when the `n`th `Partial` telling of `held` reaches him (a distinct event id per hop, so a distinct draw)."""
    return W._told_value(w, hearer, Event(f"ev_hop{n}", "news.told", [], [f"a_hop{n}"], 0, "Partial", ()), held)


def test_the_quantity_stems_are_what_the_table_compares_against_a_threshold():
    """`QUANTITY_STEMS` is derived: the cell stems a `scalar_threshold` clause carries; an existence reading, a deed and a `seen` are in no row's threshold."""
    from ..data.verbs import QUANTITY_STEMS
    assert {"stores", "condition"} <= QUANTITY_STEMS
    assert not QUANTITY_STEMS & {"exists", "person.died", "seen", "held_by"}, sorted(QUANTITY_STEMS)


def test_unshared_first_prefers_a_deed_to_a_quantity_to_an_existence_reading():
    """B11.52: at `unshared_first` a teller holding a deed claim (OLDEST), a `stores` amount and a NEWER `exists:Person` reading says the deed; with the deed removed,
    the amount, not the newer existence reading (an existence reading is in `QUANTITY_STEMS`' complement, so it falls in `other`); at `newest` (the control) the newest."""
    from ..data.verbs import DEED_KINDS, QUANTITY_STEMS
    transport = {k for v in ("tell", "lie") for k in (*VERB_TABLE[v].emits, *VERB_TABLE[v].emits_on_refusal)}
    deed = sorted(DEED_KINDS - transport)[0]
    assert "exists" not in QUANTITY_STEMS and "stores" in QUANTITY_STEMS

    def claim(n, predicate, value, when):
        return Claim(f"c{n}", "T", "S", predicate, value, when, "firsthand", 100, "own")
    d, q, e = claim(1, deed, True, 1), claim(2, "stores:grain", 8, 3), claim(3, "exists:Person", 1, 5)
    fx = DEFAULT_FIXTURES.sweep("said_slant", "unshared_first")
    assert said_of([d, q, e], "S", fx).predicate == deed
    assert said_of([q, e], "S", fx).predicate == "stores:grain"
    assert said_of([e], "S", fx).predicate == "exists:Person"                       # an existence reading is still said when it is all he holds (`other`)
    assert said_of([d, q, e], "S", DEFAULT_FIXTURES).predicate == "exists:Person"     # the control: `newest`


def test_partial_told_deed_withholds_the_hand(monkeypatch):
    """B11.53: a hearer of a deed at a band holds what a FINDER at that band holds -- the sighting names the hand where `rosters.yaml: finding_terms`' row shows
    `HAND_TERM`, and names nobody where it does not (`loop/witness.py::_told_pairing` reads that one table). Through the WITNESS barrier: W saw K kill V and tells J at
    each band the telling emits at; J names K as the doer, or nobody. Then the table PLANTED (`Success` loses the hand) and the same telling names nobody."""
    from ..data.rosters import FINDING_TERMS
    from .test_told_pairing import J, K, _doers, _world
    bands = sorted(set(VERB_TABLE["tell"].emits_by_degree) & set(FINDING_TERMS))
    assert W.HAND_TERM in FINDING_TERMS["Success"] and W.HAND_TERM not in FINDING_TERMS["Partial"], FINDING_TERMS      # the shipped table the bands read
    assert len(bands) >= 2, bands
    for band in bands:
        w, tell, _claims = _world("on")
        tell("p_low", K, band)
        assert _doers(w, J) == ((K,) if W.HAND_TERM in FINDING_TERMS[band] else ()), (band, _doers(w, J))
    with monkeypatch.context() as m:                                   # the falsifier: one table, so moving a row moves the hearer
        m.setitem(FINDING_TERMS, "Success", tuple(t for t in FINDING_TERMS["Success"] if t != W.HAND_TERM))
        w, tell, _claims = _world("on")
        tell("p_low", K, "Success")
        assert _doers(w, J) == (), _doers(w, J)


def test_existence_lie_is_a_negation():
    """A lie about an existence reading says the other truth value (`0` for `1`, `1` for `0`), never a whole-band drift of it (`2`)."""
    fx = DEFAULT_FIXTURES
    assert [s.value for s in lie_said_of([_claim("exists:Person", 1)], "S", fx)] == [0]
    assert [s.value for s in lie_said_of([_claim("exists:Person", 0)], "S", fx)] == [1]       # a held 0 has a false thing to say here, unlike an amount
    for v in (0, 1):
        (got,) = lie_said_of([_claim("exists:Record", v)], "S", fx)
        assert got.value in (0, 1) and got.value != v and (got.subject, got.predicate) == ("S", "exists:Record")
    assert [s.value for s in lie_said_of([_claim("stores:grain", 8)], "S", fx)] == [12, 4]      # the control: an amount moves one whole step each way


def test_partial_telling_passes_an_existence_reading_whole():
    """`(King, exists:Person, 1)` told at `Partial` down a six-hop chain reads `1` at every hop, at every hearer; no existence reading leaves {0, 1}."""
    w = P.tiny_world()
    held = Claim("c_king", "p_low", "p_king", "exists:Person", 1, 0, "firsthand", 80, "own")
    seen = []
    for hearer in ("p_mid", "p_high", "p_other"):
        for hop in range(6):
            held = dataclasses.replace(held, value=_partial_telling(w, hearer, held, hop))
            seen.append(held.value)
        held = dataclasses.replace(held, value=1)
    assert len(seen) == 18 and set(seen) == {1}, seen
    assert _partial_telling(w, "p_mid", Claim("c_k0", "p_low", "p_king", "exists:Person", 0, 0, "firsthand", 80, "own"), 0) == 0


def test_quantity_still_drifts_on_a_partial_telling():
    """The control, green before and after: an amount on a quantity stem is moved at `Partial` by `drifted`'s own rule, the grain rows as they were."""
    w = P.tiny_world()
    band = w.fixtures.get("told_drift_band")
    for stem, v in (("stores:grain", 8), ("condition", 3), ("stores:grain", -8)):
        held = Claim("c_q", "p_low", "S", stem, v, 0, "firsthand", 80, "own")
        got = [_partial_telling(w, "p_mid", held, n) for n in range(12)]
        assert any(g != v for g in got), (stem, got)
        ev = Event("ev_hop0", "news.told", [], ["a_hop0"], 0, "Partial", ())
        sel = int(H(w.world_seed, w.tick, "p_mid", f"told:{ev.id}"), 16)
        assert got[0] == drifted(v, band, sel), (stem, got[0])


def test_a_hand_built_lie_on_a_man_s_existence_declines_the_hearers_challenge_only_as_the_negation_it_is(monkeypatch):
    """`p1c_exists.py` (i), the lie produced by a hand-built `lie` and not a plant: T tells HOLDER `(p_other, exists:Person, v)`. After the lie HOLDER holds the
    negation `0` and his own ledger contradicts a `challenge` on `p_other` (§F1 clause 4: no such Candidate forms); after a `tell` (the control) he holds `1`
    and it does not. Before B11.51 the lie said `2`, which `exists` reads as `>= 1` -- a lie that declined nothing."""
    def hearer_declines_the_challenge(verb):
        w = _world()
        w.persons[T].ledger[:] = [c for c in w.persons[T].ledger if (c.subject, c.predicate) != ("p_other", "exists:Person")]
        w.persons[T].ledger.append(Claim("c_exists", T, "p_other", "exists:Person", 1, 0, "firsthand", 80, "own"))   # the reading a refused act's observation deposits: 0/1
        _season(monkeypatch, w, verb, HOLDER, subject="p_other")
        told = [c for c in w.persons[HOLDER].ledger if c.source == "told_by" and (c.subject, c.predicate) == ("p_other", "exists:Person")]
        assert len(told) == 1, told
        return told[0].value, PQ.belief_contradicts(w.persons[HOLDER], VERB_TABLE["challenge"], "p_other", {"subject": "p_other"})
    assert hearer_declines_the_challenge("lie") == (0, True)
    assert hearer_declines_the_challenge("tell") == (1, False)


# ---- a hearer who knows the figure hears it as he holds it (v12 B11.55, `16_PESSIMIST_SC_E` edit 1) ----------------

def test_knower_hears_true_on_a_partial_telling(monkeypatch):
    """B11.55: a `Partial` telling of an amount (net 2 against obstacle 2) to a hearer who holds that cell FIRSTHAND is heard as he holds it: no copy lands (the told deposit
    would be his own claim, and the exact-triple guard drops it), and his `record` of the teller does not fall, whether the teller was honest (`tell`: 8) or a liar (`lie`: 12). A hearer
    who holds nothing on the cell still receives the drifted copy, so the arm touches the knower and nobody else."""
    for verb in ("tell", "lie"):
        w = _world(record_gain=0.5)
        evs = _season(monkeypatch, w, verb, HOLDER, net=2)
        assert [e.degree for e in evs if e.kind == "news.told"] == ["Partial"], [(e.kind, e.degree) for e in evs]
        assert _told(w, HOLDER) == [], (verb, [(c.value, c.chain) for c in _told(w, HOLDER)])
        assert record(w.persons[HOLDER], T, w.fixtures) >= 1.0, verb
    for verb in ("tell", "lie"):
        got = []
        for arm in (True, False):
            w = _world(record_gain=0.5)
            w.fixtures = w.fixtures.sweep("knower_hears_true", arm)
            _season(monkeypatch, w, verb, KNOWNOT, net=2)
            got.append([c.value for c in _told(w, KNOWNOT)])
        assert got[0] == got[1] and len(got[0]) == 1 and got[0][0] != (TRUE_VALUE if verb == "tell" else 12), (verb, got)   # the drifted copy, either arm


def test_knower_hears_true_false_reproduces_todays_branch(monkeypatch):
    """The control: `knower_hears_true` False hands a knower the drifted copy, as before the arm -- an honest `tell` of 8 reaches him as 5 and his `record` of the teller falls below 1.0
    (the falsifier: a landed truthful telling after which the hearer's `record` of the teller is below 1.0)."""
    w = _world(record_gain=0.5)
    w.fixtures = w.fixtures.sweep("knower_hears_true", False)
    _season(monkeypatch, w, "tell", HOLDER, net=2)
    assert [c.value for c in _told(w, HOLDER)] == [5], [(c.value, c.chain) for c in _told(w, HOLDER)]
    assert record(w.persons[HOLDER], T, w.fixtures) < 1.0
