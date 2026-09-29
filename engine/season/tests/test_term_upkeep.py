"""Plan position `17b` -- TERM · UPKEEP. `workplans/2026-09-28-the-plan-one-order-mc-v18-retired.md`
§3.2 row 10 and its "Contradiction 1" box: *"`Tenure.term`, the T-n basis at the gate, `Office.upkeep`'s
reader, and payment by `transfer` renewing `oblige` terms."* Content owners: `04_CODE_ARCHITECTURE.md`
§B.8 (`term? (matures_at, declared_by, …)`), F.3 (*"MATTER matures it"*), F.18 (*"the repair is a
verb"*), and the `mc_v18` retirement plan's G2.

What the position built, each asked of the real fold, the real MATTER barrier and the real gate:
  * `Tenure.term` (`state/carriers.py::Term`) -- `_eff_oblige` declares it on the edge it opens.
  * MATTER closes every live edge whose `term.matures_at` has come, `causes = [term.declared_by]`,
    admitted at the gate under `T-n` (actorless, a pure closure, the edge's own term due).
  * `Office.upkeep` typed, read at ONE owner (`world_q.upkeep_of`, fixture `default_upkeep`).
  * a `transfer` exercised through a seat by its seated holder, out of the seat's own rung, to an
    obligee's home, renews as many of that seat's `oblige` terms as the amount covers -- the gate's
    seventh basis, `renewal`.

THE FALSIFIERS, and the control each carries:
  * T-n: an unpaid term lapses AT its maturity and not one season before; the lapse cites the act
    that wound it. Control: the paid twin survives the same barrier.
  * Narrative #3 (*embezzlement "already runs"*): two worlds identical but for WHERE the holder sends
    the same unit out of the treasury. Paid to the obligee's home, the establishment survives;
    moved to his own hearth, it lapses -- with no line of code that knows the word "embezzle".
  * The gate: every basis-shaped change `17b` admits has a refused twin one clause away, and a
    refused renewal leaves the term exactly as it was (the store is put back).

The fixture is `probes.tiny_world`: `R` > `D` > `S` > `Hh`. `p_high` (the duke) holds `off_duke`,
whose rung -- and so whose TREASURY -- is `D`; he lives in `S`. `p_low`, `p_mid`, `p_other` live in
`Hh`. `p_king` lives in `R` and holds nothing.
"""

from __future__ import annotations

import pytest

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import MATRIX, Step, WriteClass
from ..data.verbs import VERB_TABLE
from ..gaps import Forbidden
from ..harness import probes as P
from ..loop import effects as EF
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..state import gate as G
from ..state.carriers import Act, Office, Tenure, Term
from ..state.gate import RENEWAL, T_N, Change, NotYours, Subject

SEAT, DUKE, TREASURY, HOME = "off_duke", "p_high", "D", "Hh"
DUKES_HEARTH = "S"


def _world(**fx):
    """`tiny_world` at the given fixture arms, one MATTER barrier run (tick 0), and a treasury:
    `D` holds no stores in the probe, and a seat with an empty treasury can pay nobody."""
    fixtures = DEFAULT_FIXTURES
    for name, value in fx.items():
        fixtures = fixtures.sweep(name, value)
    w = P.tiny_world(fixtures)
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    w.rungs[TREASURY].stores = {"grain": 12}
    return w, d


def _fold(w, d, *acts):
    """One RESOLVE pass over `acts`, its Events logged as `SeasonDriver.season` logs them."""
    out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts),
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return out


def _season(w, d):
    """The next season's MATTER barrier and nothing else: the tick advances, MATTER runs."""
    w.tick += 1
    return d.matter(mint_token(w, WriteClass.MATTER), [])


def _oblige(w, d, who, key, seat=SEAT):
    return _fold(w, d, Act(id=key, actor=who, verb="oblige", payload={"subject": seat}))


def _pay(w, d, key, amount=1, to=HOME, frm=TREASURY, actor=DUKE, via=SEAT):
    return _fold(w, d, Act(id=key, actor=actor, verb="transfer", via=via,
                           payload={"from": frm, "to": to, "kind": "grain", "amount": amount}))


def _edge(w, who, seat=SEAT):
    """`who`'s `oblige` on `seat` -- the one this test opened, live or ended."""
    found = [t for t in w.tenures if t.kind == "oblige" and t.subject == who and t.object == seat]
    assert len(found) == 1, found
    return found[0]


def _kinds(events):
    return [e.kind for e in events]


# ======================================================================================
# 1 -- THE TERM: DECLARED BY THE OPENING ACT
# ======================================================================================

@pytest.mark.parametrize("arm", [None, 1, 4])
def test_17b_oblige_declares_its_term_and_the_control_arm_declares_none(arm):
    """`_eff_oblige` opens the edge with `Term(tick + oblige_term, <the oblige act>)` -- T-n's *"the
    opening act declares the terms"*. At `H-159`'s control arm (`None`) the edge opens with no term,
    which is the `17a` edge exactly. All three sweep points run, so a fixture that stopped reaching
    the effect would fail at two of them."""
    w, d = _world(oblige_term=arm)
    out = _oblige(w, d, "p_mid", "ob1")
    assert _kinds(out) == ["duty.taken"], _kinds(out)
    t = _edge(w, "p_mid")
    assert t.live
    assert t.term == (None if arm is None else Term(w.tick + arm, "ob1")), t.term


# ======================================================================================
# 2 -- T-n: AN UNPAID TERM MATURES AT MATTER, AND CITES WHO WOUND IT
# ======================================================================================

def test_17b_an_unpaid_term_lapses_at_its_maturity_citing_the_act_that_wound_it(monkeypatch):
    """THE `T-n` FALSIFIER. Obliged at tick 0 with a two-season term: still serving at tick 1, gone at
    tick 2's MATTER -- `until == 2`, one `tenure.closed` whose cause is the `oblige` act itself (AX-5,
    *"a matured term cites the act that wound it"*), carried in what MATTER returns (so WITNESS fans
    it out), and the seat's `establishment_of` shrinks by exactly that person. The gate admitted it
    as `T-n` and as nothing else: observed through the real `tenure_write_basis`."""
    seen = []
    real = G.tenure_write_basis

    def spy(*a, **k):
        b = real(*a, **k)
        seen.append(b)
        return b
    monkeypatch.setattr(G, "tenure_write_basis", spy)
    w, d = _world(oblige_term=2)
    _oblige(w, d, "p_mid", "ob1")
    t = _edge(w, "p_mid")
    assert world_q.establishment_of(w, SEAT) == ["p_mid"]

    early = _season(w, d)                                    # tick 1: not yet
    assert t.live and not [e for e in early if e.kind == "tenure.closed"], "matured a season early"
    assert world_q.establishment_of(w, SEAT) == ["p_mid"]

    seen.clear()
    due = _season(w, d)                                      # tick 2: matures_at
    lapses = [e for e in due if e.kind == "tenure.closed"]
    assert t.until == 2, t
    assert len(lapses) == 1, _kinds(due)
    assert lapses[0].causes == ["ob1"], lapses[0].causes
    assert [c.subject for c in lapses[0].changes] == [t.id]
    assert world_q.establishment_of(w, SEAT) == []
    assert T_N in seen, seen

    # AND ONLY ONCE: a lapsed edge is not live, so the next barrier has nothing to mature.
    assert not [e for e in _season(w, d) if e.kind == "tenure.closed"]


def test_17b_a_term_lapses_whoever_is_left_to_pay_it():
    """THE OPPOSITE POLARITY FROM A RECORD'S STAGES, pinned. A half-made copy STOPS when its copyist
    is gone (`loop/matter.py`'s Record branch); a term LAPSES when nobody is left to pay it -- that is
    `T-n`'s point. The duke resigns his seat (`release`, `T-m`), so the seat is vacant and nobody CAN
    pay: a transfer he still makes through it renews nothing (`may_renew` -- he no longer sits), and
    the term matures on schedule."""
    w, d = _world(oblige_term=2)
    _oblige(w, d, "p_mid", "ob1")
    _fold(w, d, Act(id="quit", actor=DUKE, verb="release", payload={"subject": SEAT}))
    assert world_q.hold_force(w, SEAT) is None, "fixture: the seat is vacant"
    out = _pay(w, d, "pay_vacant")
    assert "transfer.made" in _kinds(out) and "term.renewed" not in _kinds(out), _kinds(out)
    assert _edge(w, "p_mid").term == Term(2, "ob1")
    _season(w, d)
    _season(w, d)
    assert not _edge(w, "p_mid").live


# ======================================================================================
# 3 -- RENEWAL: THE SEAT PAYS ITS ESTABLISHMENT, AND THE PAYMENT WINDS THE CLOCK
# ======================================================================================

def test_17b_a_paid_term_runs_on_from_where_it_stood_and_the_next_lapse_cites_the_payment(
        monkeypatch):
    """The duke pays one unit (`default_upkeep`'s shipped `1`) out of `D` to `Hh`, where `p_mid`
    lives. The term moves from `2` to `4` -- ON FROM WHERE IT STOOD, not from now -- and is re-
    declared by the payment. Both kinds are emitted (`transfer.made` by the rungs, `term.renewed` by
    the edge), the treasury is down by exactly the unit, the edge survives the barrier that would
    have ended it, and when it finally lapses the cause is the PAYMENT, the last hand on the clock.
    The gate admitted the renewal as `renewal`."""
    seen = []
    real = G.tenure_write_basis

    def spy(*a, **k):
        b = real(*a, **k)
        seen.append(b)
        return b
    monkeypatch.setattr(G, "tenure_write_basis", spy)
    w, d = _world(oblige_term=2)
    _oblige(w, d, "p_mid", "ob1")
    t = _edge(w, "p_mid")
    before = dict(w.rungs[TREASURY].stores)
    out = _pay(w, d, "pay1")
    assert sorted(_kinds(out)) == ["term.renewed", "transfer.made"], _kinds(out)
    assert t.term == Term(4, "pay1"), t.term
    assert w.rungs[TREASURY].stores["grain"] == before["grain"] - 1
    assert RENEWAL in seen, seen

    for tick in (1, 2, 3):
        _season(w, d)
        assert t.live, f"lapsed at tick {tick} though paid to 4"
    last = [e for e in _season(w, d) if e.kind == "tenure.closed"]    # tick 4
    assert not t.live and [e.causes for e in last] == [["pay1"]], last


def test_17b_narrative_3_embezzlement_is_a_lapse_nobody_scripted():
    """NARRATIVE #3 (`01_THE_TEN.md` §3, *"a `transfer` from the settlement store to a steward's own
    hearth is embezzlement, today, with no new object"*), MADE OBSERVABLE. Two worlds, identical to
    the unit: the same oblige, the same holder, the same seat, the same unit out of the same
    treasury, both transfers executed. The ONE difference is `to` -- the obligee's home, or the
    holder's own. At the old term's maturity the paid seat still has its man and the skimmed seat
    has lost him, and the lapse cites the oblige nobody renewed. Nothing in the engine names
    embezzlement: the unpaid term simply matures."""
    worlds = {}
    for label, to in (("paid", HOME), ("skimmed", DUKES_HEARTH)):
        w, d = _world(oblige_term=2)
        _oblige(w, d, "p_mid", "ob1")
        out = _pay(w, d, f"move_{label}", to=to)
        assert "transfer.made" in _kinds(out), (label, _kinds(out))
        worlds[label] = (w, d)
    wp, ws = worlds["paid"][0], worlds["skimmed"][0]
    assert wp.rungs[TREASURY].stores == ws.rungs[TREASURY].stores, "control: the same unit left"
    lapses = {}
    for label, (w, d) in worlds.items():
        _season(w, d)
        lapses[label] = [e for e in _season(w, d) if e.kind == "tenure.closed"]    # tick 2
    assert world_q.establishment_of(wp, SEAT) == ["p_mid"]
    assert world_q.establishment_of(ws, SEAT) == []
    assert lapses["paid"] == []
    assert [e.causes for e in lapses["skimmed"]] == [["ob1"]]


def _both_obliged(**fx):
    """`p_low` obliged at tick 0 and `p_mid` at tick 1, both at home in `Hh`: two terms that mature
    one season apart, so *soonest-maturing first* has something to choose between."""
    w, d = _world(**fx)
    _oblige(w, d, "p_low", "ob_low")
    _season(w, d)
    _oblige(w, d, "p_mid", "ob_mid")
    return w, d


def test_17b_a_payment_covers_as_many_as_it_pays_for_soonest_maturing_first():
    """Per-obligee upkeep, counted. At `upkeep 1` one unit renews ONE of the two -- `p_low`, whose
    term comes first -- and leaves the other exactly as it was; two units renew both. At the
    fixture's control arm `0` (keeping an establishment costs nothing) one unit renews every obligee
    at the home it reaches."""
    w, d = _both_obliged(oblige_term=4)
    low, mid = _edge(w, "p_low"), _edge(w, "p_mid")
    assert (low.term.matures_at, mid.term.matures_at) == (4, 5), "fixture"
    _pay(w, d, "one")
    assert low.term == Term(8, "one") and mid.term == Term(5, "ob_mid"), (low.term, mid.term)

    w, d = _both_obliged(oblige_term=4)
    _pay(w, d, "two", amount=2)
    assert [_edge(w, p).term for p in ("p_low", "p_mid")] == [Term(8, "two"), Term(9, "two")]

    w, d = _both_obliged(oblige_term=4, default_upkeep=0)
    _pay(w, d, "token")
    assert [_edge(w, p).term.declared_by for p in ("p_low", "p_mid")] == ["token", "token"]


def test_17b_a_declared_upkeep_is_what_a_payment_is_counted_against():
    """`Office.upkeep` read, not the fixture, when the seat declares one: at `3`, two units renew
    nobody and three renew the one obligee -- the SAME transfer, the same world, the one difference
    being the amount against the seat's own declared price."""
    for amount, renewed in ((2, False), (3, True)):
        w, d = _world(oblige_term=2)
        w.offices[SEAT].upkeep = 3
        assert world_q.upkeep_of(w, SEAT) == 3
        _oblige(w, d, "p_mid", "ob1")
        out = _pay(w, d, f"pay{amount}", amount=amount)
        assert "transfer.made" in _kinds(out)
        assert (_edge(w, "p_mid").term == Term(4, f"pay{amount}")) is renewed, _edge(w, "p_mid")


# The four clauses of `loop/effects.py::_renewals`, each broken alone. Every case still MOVES THE
# MATTER (`transfer.made`) -- the payment happens and buys nothing -- so a refusal here is the
# renewal's, never the transfer's.
_ONE_CLAUSE_BROKEN = {
    "no seat exercised (every computed transfer)": dict(via=None),
    "a seat the actor does not sit in": dict(actor="p_king"),
    "not out of the seat's own rung (a gift from the settlement store)": dict(frm="S"),
    "not to an obligee's home": dict(to=DUKES_HEARTH),
}


@pytest.mark.parametrize("why", sorted(_ONE_CLAUSE_BROKEN))
def test_17b_a_transfer_is_upkeep_only_when_every_clause_holds(why):
    w, d = _world(oblige_term=2)
    _oblige(w, d, "p_mid", "ob1")
    out = _pay(w, d, "pay", **_ONE_CLAUSE_BROKEN[why])
    assert _kinds(out) == ["transfer.made"], (why, _kinds(out))
    assert _edge(w, "p_mid").term == Term(2, "ob1"), why


def test_17b_the_control_for_every_broken_clause_renews():
    """The four cases above with no clause broken -- the same helper, the same defaults. Without it
    the parametrized test would also pass if nothing ever renewed."""
    w, d = _world(oblige_term=2)
    _oblige(w, d, "p_mid", "ob1")
    assert "term.renewed" in _kinds(_pay(w, d, "pay"))
    assert _edge(w, "p_mid").term == Term(4, "pay")


def test_17b_paying_yourself_is_no_payment():
    """Clause 3, asked of the rule directly because no probe person lives AT a seat's rung: a
    transfer from the treasury to the treasury (G4 already refuses it as a no-op) and a transfer of
    nothing renew nobody -- otherwise a seat whose obligee lived at its own rung could wind his
    clock without spending a grain. Control: the same call to `Hh` renews him."""
    w, d = _world(oblige_term=2)
    _oblige(w, d, "p_mid", "ob1")
    a = Act(id="x", actor=DUKE, verb="transfer", via=SEAT, payload={})
    assert EF._renewals(w, a, TREASURY, TREASURY, 1) == []
    assert EF._renewals(w, a, TREASURY, HOME, 0) == []
    assert EF._renewals(w, a, TREASURY, HOME, 1) == [(_edge(w, "p_mid"), Term(4, "x"))]


def test_17b_a_seat_pays_only_its_own_establishment():
    """The duke also holds a Mayor's seat at `S`, and `p_mid` is obliged to BOTH seats. A payment
    through the Mayor's seat, out of `S`, renews `p_mid`'s term on the Mayor's seat and not on the
    duke's -- upkeep is what the post pays ITS establishment (`holonic_ARCHITECTURE.md:428`)."""
    w, d = _world(oblige_term=2)
    w.offices["off_mayor"] = Office("off_mayor", "Mayor", "S", ["issue"], faction="Crown")
    w.add_tenure(Tenure("t_mayor", DUKE, "off_mayor", "hold", 0))
    _oblige(w, d, "p_mid", "ob_duke")
    _oblige(w, d, "p_mid", "ob_mayor", seat="off_mayor")
    out = _pay(w, d, "pay_mayor", frm="S", via="off_mayor")
    assert "term.renewed" in _kinds(out), _kinds(out)
    assert _edge(w, "p_mid", "off_mayor").term == Term(4, "pay_mayor")
    assert _edge(w, "p_mid", SEAT).term == Term(2, "ob_duke")


def test_17b_an_ordinary_transfer_emits_exactly_what_it_did_before():
    """The shape every computed transfer has -- no `via` -- after `17b` put `term.renewed` on the
    row: one kind, `transfer.made`, carrying the two rung receipts and nothing else. (Each rung
    earns `transfer.made` by name; left earning `None` they would earn EVERY declared kind.)"""
    w, d = _world()
    out = _fold(w, d, Act(id="plain", actor="p_mid", verb="transfer",
                          payload={"from": HOME, "to": "S", "kind": "grain", "amount": 1}))
    assert _kinds(out) == ["transfer.made"], _kinds(out)
    assert [c.subject for c in out[0].changes] == [HOME, "S"]


# ======================================================================================
# 4 -- THE GATE: EACH BASIS `17b` ADMITS HAS A REFUSED TWIN ONE CLAUSE AWAY
# ======================================================================================

def _gate_world(**fx):
    """Tick 0, `p_mid` obliged to the duke's seat with `Term(2, "ob1")`."""
    fx.setdefault("oblige_term", 2)
    w, d = _world(**fx)
    _oblige(w, d, "p_mid", "ob1")
    return w, d, _edge(w, "p_mid")


def _mature(w, t, matured=True):
    """The write MATTER's tenure-term branch makes, bare: an actorless MATTER-class closure of `t`,
    with nothing but the gate asked."""
    w.step = Step.MATTER
    return w.write("until", mint_token(w, WriteClass.MATTER), lambda: setattr(t, "until", w.tick),
                   record_kind="Tenure", fieldname="until", driver="Event", emits="tenure.closed",
                   subject=t.id, causes=[t.term.declared_by],
                   **({"matured_term": t.id} if matured else {}))


def test_17b_gate_T_n_admits_only_an_actorless_closure_of_a_term_that_has_come():
    """Three refusals and the admission they bracket. (1) The caller NAMING a matured term is not
    enough: at tick 0 the term is due at 2, and F3 refuses the closure (`NotYours`), store put back.
    (2) Naming NO cause at all is refused before F3 is ever asked -- S15.3's pre-check, generalised
    to two causes and not to three. (3) At tick 2 the term HAS come, and a stranger's ACT closing
    the edge is still refused: a matured term licenses its own lapse, never someone else's hand.
    Then MATTER's actorless write at tick 2 is admitted."""
    w, d, t = _gate_world()
    with pytest.raises(NotYours):
        _mature(w, t)
    assert t.live, "a refused lapse must leave the edge as it was"
    with pytest.raises(Forbidden) as no_cause:
        _mature(w, t, matured=False)
    assert not isinstance(no_cause.value, NotYours) and no_cause.value.where == "S15.3"
    assert t.live

    w.tick = 2
    w.step = Step.RESOLVE
    with pytest.raises(NotYours):
        w.write("Tenure", mint_token(w, WriteClass.ACTS), lambda: setattr(t, "until", w.tick),
                record_kind="Tenure", fieldname="until", driver="Act", actor="p_king")
    assert t.live
    _mature(w, t)
    assert t.until == 2


def _wind(w, t, term, actor=DUKE, via=SEAT):
    """The write `_eff_transfer`'s renewal makes, bare: an ACTS-class `Change` setting `t.term`."""
    w.step = Step.RESOLVE
    return w.write("term", mint_token(w, WriteClass.ACTS), None, record_kind="Tenure",
                   fieldname="term", driver="Act", actor=actor, via=via,
                   change=Change((Subject.edge(t),), lambda: setattr(t, "term", term)))


def _a_tie_on_the_seat(w, t):
    """A NON-`oblige` edge on the seat, carrying a term -- so `kind` is the ONE clause broken."""
    return w.add_tenure(Tenure("tie_on_seat", "p_other", SEAT, "tie", 0, term=Term(2, "ob1")))


def _closed(w, t):
    t.until = w.tick
    return t


def _termless(w, t):
    return w.add_tenure(Tenure("ob_termless", "p_low", SEAT, "oblige", 0))


_RENEWAL_REFUSED = {
    "no seat exercised":              (lambda w, t: t, Term(4, "x"), dict(via=None)),
    "a stranger exercising the seat": (lambda w, t: t, Term(4, "x"), dict(actor="p_king")),
    "shortening the term":            (lambda w, t: t, Term(1, "x"), {}),
    "re-declaring, not extending":    (lambda w, t: t, Term(2, "x"), {}),
    "imposing a term on an edge that had none": (_termless, Term(4, "x"), {}),
    "an ended oblige":                (_closed, Term(4, "x"), {}),
    "an edge on the seat that is not an oblige": (_a_tie_on_the_seat, Term(4, "x"), {}),
}


@pytest.mark.parametrize("why", sorted(_RENEWAL_REFUSED))
def test_17b_gate_renewal_is_refused_one_clause_away(why):
    """Every refusal puts the term back EXACTLY -- which is only possible because `term` is one of
    the fields the tenure snapshot records (`world.py::_written_fields`). Were it not, the gate
    would see no change at all and this would fail as `NoOpReceipt`, not `NotYours`."""
    w, d, t = _gate_world()
    pick, term, kw = _RENEWAL_REFUSED[why]
    target = pick(w, t)
    was = target.term
    with pytest.raises(NotYours):
        _wind(w, target, term, **kw)
    assert target.term == was, (why, target.term)


def test_17b_gate_renewal_control_the_seated_holder_pushing_it_later():
    """The admission every refusal above is one clause away from."""
    w, d, t = _gate_world()
    got = _wind(w, t, Term(4, "x"))
    assert t.term == Term(4, "x") and [r.subject for _s, r in got] == [t.id]


# ======================================================================================
# 5 -- THE TYPES, THE FIXTURES, THE CELL
# ======================================================================================

@pytest.mark.parametrize("bad", [-1, True, 1.5, "1"])
def test_17b_office_upkeep_refuses_what_cannot_count_obligees(bad):
    with pytest.raises(Forbidden):
        Office("off_x", "Reeve", "S", ["issue"], faction="Crown", upkeep=bad)


def test_17b_upkeep_is_read_at_one_owner_with_the_fixture_behind_it():
    """`None` is not free: it is the fixture's (`H-158`). A declared `0` IS free, and wins over the
    fixture -- the difference between *declares none* and *declares nothing to pay*. A fixture arm
    that cannot count obligees is refused at the one reader."""
    w, _ = _world()
    assert w.offices[SEAT].upkeep is None
    assert world_q.upkeep_of(w, SEAT) == DEFAULT_FIXTURES.get("default_upkeep") == 1
    assert world_q.upkeep_of(_world(default_upkeep=3)[0], SEAT) == 3
    w.offices[SEAT].upkeep = 0
    assert world_q.upkeep_of(w, SEAT) == 0
    with pytest.raises(Forbidden):
        world_q.upkeep_of(_world(default_upkeep=0.5)[0], SEAT)


@pytest.mark.parametrize("bad", [0, -1, True, 1.5])
def test_17b_a_term_that_cannot_outlive_its_own_season_is_refused(bad):
    w, _ = _world(oblige_term=bad)
    with pytest.raises(Forbidden):
        EF._oblige_term(w)


def test_17b_the_term_cell_is_an_act_cell_and_matter_cannot_move_it():
    """`(Tenure, term)` is RES-only and `social: true`: an ACT declares a term and an act renews it.
    MATTER matures a term by closing its edge (`(Tenure, until)`'s MAT cell), never by moving the
    term -- a MATTER write of the cell is refused and the term is untouched. Both writers declare
    the pair, on `establish`'s `Tenure.payload` precedent."""
    row = MATRIX[("Tenure", "term")]
    assert set(row.steps) == {Step.RESOLVE}, row.steps
    assert "Tenure.term" in VERB_TABLE["oblige"].writes
    assert "Tenure.term" in VERB_TABLE["transfer"].writes
    assert "term.renewed" in VERB_TABLE["transfer"].emits
    w, d, t = _gate_world()
    w.step = Step.MATTER
    with pytest.raises(Forbidden):
        w.write("term", mint_token(w, WriteClass.MATTER),
                lambda: setattr(t, "term", Term(9, "ob1")), record_kind="Tenure",
                fieldname="term", driver="Event", emits="term.renewed", subject=t.id,
                causes=["ob1"])
    assert t.term == Term(2, "ob1")
