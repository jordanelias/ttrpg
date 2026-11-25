"""B21.01 -- a seat row may name its term (`offices.yaml`'s `term: <positive int> | null`, row data and not a `Seat` field);
a malformed term is refused. B21.02 turns the last test green.

The row's `term:` is the DEFAULT a conferral writes onto the hold's `term?` (`loop/effects_governance.py::_declared_term`:
the act's own declared term first, else `Term(tick + n, act)` from the row, else none). Every test plants the row in
`SEAT_ROW_BY_ID` (no shipped row carries one), through the real fold and the real MATTER barrier where the claim is a
season's.
"""
from __future__ import annotations

import pytest

from ..data.matrix import Step, WriteClass
from ..data.rosters import SEAT_ROW_BY_ID
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..loop.matter import _die
from ..queries import world_q
from ..queries.world_q import BAN_KIND
from ..state.carriers import Act, Tenure
from ._seat_at_success import seat_at_success  # noqa: F401  (the fixture; its reason is in its module)
from .test_g3_not_yours import _gov_world, _hold

SEAT, CONFERRER, VIA, CONFEREE = "off_reeve", "p_king", "off_crown", "p_mid"
pytestmark = pytest.mark.usefixtures("seat_at_success")   # B21.14: a seat row's term and a ban's reach are the fold's; the draw is C3's test


def _plant(monkeypatch, term):
    monkeypatch.setitem(SEAT_ROW_BY_ID, SEAT, {"id": SEAT, "term": term})


def _classed(w):
    """Per person, the ids their questions carry as classed referents (`test_in53_vacancy_need.py::_classed`)."""
    return {pid: {r for q in world_q.questions_for(w, p) for r, _ in q.classes} for pid, p in w.persons.items()}


def _seasons(n):
    """`n` seasons of the governance world through `SeasonDriver.season`; the King confers `off_reeve` on `p_mid` (through
    `off_crown`) in the FIRST season only, naming NO term. Returns the world, the act's id and the hold that season opened."""
    w, _ = _gov_world()
    start = w.tick
    acts = {}

    def choose(p, v, s, ask_budget):
        if p.id == CONFERRER and w.tick == start:
            a = P.Act_(w, p, "confer", via=VIA, payload={"subject": SEAT, "to": CONFEREE})
            acts["confer"] = a.id
            return [a]
        return []
    d = P._run_d(w, choose, n=1)
    first = _hold(w, SEAT)
    for _ in range(n - 1):
        d.season(choose, question=None)
    return w, acts["confer"], first


def _resolve(w, d, act):
    w.step = Step.RESOLVE
    w.frozen = False
    return d.resolve(mint_token(w, WriteClass.ACTS), [act], contest_max_depth=w.fixtures.get("contest_max_depth"))


def _confer_act(aid, **payload):
    return Act(id=aid, actor=CONFERRER, verb="confer", payload={"office": SEAT, "to": CONFEREE, **payload}, via=VIA)


def test_a_confer_with_no_term_onto_a_row_termed_seat_opens_a_termed_hold(monkeypatch):
    _plant(monkeypatch, 2)
    w, aid, first = _seasons(4)
    assert first is not None and first.subject == CONFEREE, "the conferral did not open"
    assert first.term is not None and first.term.declared_by == aid, "the row's term did not ride the hold"
    assert first.term.matures_at == first.since + 2, first
    assert not first.live and first.until == first.term.matures_at, ("the row-termed hold never matured", first)
    assert _hold(w, SEAT) is None, "the seat is not left vacant"
    assert [e for e in w.log if e.kind == "tenure.closed" and e.causes == [aid]], "no MATTER closure cites the conferral"
    assert SEAT in _classed(w)[CONFERRER], "the vacancy is not among the conferrer's classed referents"


def test_a_row_with_no_term_opens_an_untermed_hold_the_control(monkeypatch):
    _plant(monkeypatch, None)
    w, _, first = _seasons(4)
    assert first is not None and first.term is None and first.live
    assert _hold(w, SEAT) is first, "an untermed hold closed"


@pytest.mark.parametrize("bad", [0, -1, "2", True, 1.5])
def test_malformed_terms_0_minus1_str_true_float_each_refuse(bad):
    w, d = _gov_world()
    out = _resolve(w, d, _confer_act("cf_bad", term=bad))
    assert [e.kind for e in out] == ["confer.bad_term"], (bad, [e.kind for e in out])      # B21.80: the `term` clause's kind
    assert _hold(w, SEAT) is None, "a refused conferral left a hold"
    # control: a lawful declared term is admitted by the same precondition
    w, d = _gov_world()
    out = _resolve(w, d, _confer_act("cf_ok", term=2))
    assert "tenure.opened" in [e.kind for e in out] and _hold(w, SEAT).subject == CONFEREE


def test_term_null_reproduces_the_hash(monkeypatch):
    hashes = {}
    for name, row in (("absent", None), ("null", {"id": SEAT, "term": None}), ("two", {"id": SEAT, "term": 2})):
        if row is not None:
            monkeypatch.setitem(SEAT_ROW_BY_ID, SEAT, row)
        else:
            monkeypatch.delitem(SEAT_ROW_BY_ID, SEAT, raising=False)
        w, _, _ = _seasons(4)
        hashes[name] = w.content_hash()
    assert hashes["null"] == hashes["absent"], hashes
    assert hashes["two"] != hashes["absent"], ("control: a termed row moved nothing", hashes)


def test_a_seat_emptied_by_a_death_is_offered_as_a_vacancy():
    w, _ = _gov_world()
    w.add_tenure(Tenure("t_reeve_held", CONFEREE, SEAT, "hold", w.tick))
    assert SEAT not in world_q.vacancies(w, w.persons[CONFERRER]), "control: a held seat is no vacancy"
    w.step = Step.MATTER
    _die(w, mint_token(w, WriteClass.MATTER), CONFEREE)
    assert CONFEREE not in w.persons and _hold(w, SEAT) is None
    assert SEAT in world_q.vacancies(w, w.persons[CONFERRER])
    assert SEAT in _classed(w)[CONFERRER]


def test_a_ban_is_scoped_to_the_banning_seats_purview():
    """A banned man is refused a seat under the banning seat's purview and admitted to one outside it. `off_duke` (rung D)
    reaches `off_reeve` (rung S, inside D); `off_duke2` (rung D2, a sibling duchy) does not."""
    refused, admitted = {}, {}
    for name, banning, into in (("inside", "off_duke", refused), ("outside", "off_duke2", admitted)):
        w, d = _gov_world()
        w.add_tenure(Tenure(f"t_ban_{name}", CONFEREE, banning, BAN_KIND, w.tick))
        out = _resolve(w, d, _confer_act(f"cf_{name}"))
        into[name] = ("tenure.opened" in [e.kind for e in out], getattr(_hold(w, SEAT), "subject", None))
    assert refused["inside"] == (False, None), ("a ban under the banning seat's purview did not bar", refused)
    assert admitted["outside"] == (True, CONFEREE), ("a ban outside the banning seat's purview barred", admitted)


# ---- the loader -----------------------------------------------------------------------------------

# ---- B21.04: a seat ends on a clock only where its body rotates --------------------------------------

def test_only_rotating_body_seats_carry_a_term():
    """The shipped rows: the Guild's two seats and the commune's representative are termed (4 seasons); the life and
    heritable seats (Confessor, the Duke of Varfell, the Jarls, the Skald-Chief, the Restoration leader) read `None`."""
    termed = {s: SEAT_ROW_BY_ID[s].get("term") for s in ("off_guild_comptroller", "off_guild_leader", "off_commune_rep_hm")}
    assert termed == {s: 4 for s in termed}, termed
    unterm = ("off_confessor", "off_duke_varfell", "off_senior_jarl_west", "off_military_jarl", "off_skald_chief",
              "off_restoration_leader")
    assert [s for s in unterm if SEAT_ROW_BY_ID[s].get("term") is not None] == []
    assert sorted(s for s, r in SEAT_ROW_BY_ID.items() if r.get("term") is not None) == sorted(termed), "a stray termed row"
