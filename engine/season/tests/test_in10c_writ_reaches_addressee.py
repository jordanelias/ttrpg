"""IN-10 (c) (H-203, SCHEDULED 2026-10-12 [ASSUMPTION; medium; Jordan to correct]) -- A WRIT REACHES
ITS ADDRESSEE.

`loop/effects_information.py::_mint_document` takes the holder from its caller: `_eff_issue` passes
the writ's `to` (`_addressee`), so a dispensation's one live `hold` is its addressee's and the issuer
keeps none (one holder per Record, `give`'s convention); every other minter (`petition`,
`create_record`, `open_case`, `survey`) still passes its maker. The addressee's edge is admitted at
the gate under `founding`'s newborn-`hold` clause (`state/gate.py::tenure_write_basis`).

  (1) a hand-folded `issue` opens the hold on `to`, and nothing on the issuer; a writ to several
      (probe `F5`'s) stays with its maker, which of several being unruled;
  (2) the gate clause: the first `hold` on a newborn non-seat thing is admitted for a non-actor; the
      same edge on a thing that already existed is not; a second first-hold is not;
  (3) THE FALSIFIER, `build_realm(0)`, one season through the real chooser: every computed `issue`
      that executed left its dispensation's one live `hold` on `payload['to']`, the issuer holding
      none; every computed `petition` that executed is still held by its maker.

MUTATION, run at the build: `_addressee(a)` -> `a.actor` in `_eff_issue` (the holder restored to the
actor) reddens (1) and (3); the gate clause deleted reddens (1), (2) and (3) (the write raises
`NotYours`).
"""
from collections import Counter

import pytest

from engine.season.harness import populated as POP
from engine.season.harness import probes as P
from engine.season.harness.corpus_run import attribute
from engine.season.decision import make_chooser
from engine.season.loop.driver import SeasonDriver, resolvable_verbs
from engine.season.loop.effects import EFFECTS
from engine.season.queries.world_q import hold_force
from engine.season.state import gate as G
from engine.season.state.carriers import Record, Rung, Tenure
from engine.season.state.ids import H, draw_factory

from .test_record_kind_fold import _mint


def _edges_on(w, rid):
    return [(t.subject, t.kind, t.live) for t in w.tenures if t.object == rid]


# (1) ----------------------------------------------------------------------------------------------

def test_in10c_an_issued_writ_opens_in_its_addressees_hand_and_the_issuer_keeps_none():
    w = P.tiny_world()
    act = P.Act_(w, w.persons["p_high"], "issue", payload={"subject": "prop_x", "to": "p_low"},
                 via="off_duke")
    _mint(w, act)
    rid = f"rec:{act.id}"
    assert w.records[rid].kind == "dispensation"
    assert _edges_on(w, rid) == [("p_low", "hold", True)], _edges_on(w, rid)
    assert hold_force(w, rid).subject == "p_low"


def test_in10c_a_petition_still_opens_on_its_maker():
    w = P.tiny_world()
    act = P.Act_(w, w.persons["p_low"], "petition",
                 payload={"subject": "p_mid", "to": "p_mid", "from": "Hh"})
    _mint(w, act)
    rid = f"rec:{act.id}"
    assert _edges_on(w, rid) == [("p_low", "hold", True)], _edges_on(w, rid)


def test_in10c_a_writ_to_several_stays_with_its_maker():
    """Which of several executors holds a writ is unruled, so a writ to several (probe `F5`'s, a
    hand-built act; the fold refuses a list at `executors`) declines to its maker, as before IN-10;
    a list of ONE is not a choice and goes to that one."""
    w = P.tiny_world()
    act = P.Act_(w, w.persons["p_high"], "issue",
                 payload={"subject": "prop_x", "to": ["p_low", "p_mid"]}, via="off_duke")
    _mint(w, act)
    assert _edges_on(w, f"rec:{act.id}") == [("p_high", "hold", True)]
    one = P.Act_(w, w.persons["p_high"], "issue", key="one",
                 payload={"subject": "prop_x", "to": ["p_low"]}, via="off_duke")
    _mint(w, one)
    assert _edges_on(w, f"rec:{one.id}") == [("p_low", "hold", True)]


# (2) ----------------------------------------------------------------------------------------------

def test_in10c_the_gate_admits_a_newborns_first_hold_and_nothing_else():
    w = P.tiny_world()
    w.records["r_new"] = Record("r_new", "D", "text")
    t = w.add_tenure(Tenure("th", "p_low", "r_new", "hold", since=w.tick))
    born = frozenset({"r_new"})
    assert G.tenure_write_basis(w, t, None, "p_high", None, frozenset(), born=born) == G.FOUNDING
    # NOT BORN IN THIS WRITE: no basis (that is `handover`'s, by `give`, the holder's own act).
    assert G.tenure_write_basis(w, t, None, "p_high", None, frozenset()) is None
    # A SECOND FIRST HOLD on the same newborn: neither is the only one, so neither is admitted.
    w.add_tenure(Tenure("th2", "p_mid", "r_new", "hold", since=w.tick))
    assert G.tenure_write_basis(w, t, None, "p_high", None, frozenset(), born=born) is None
    # ANOTHER KIND on a newborn: not a custody edge.
    w.records["r_n2"] = Record("r_n2", "D", "text")
    tie = w.add_tenure(Tenure("tt", "p_low", "r_n2", "tie", since=w.tick))
    assert G.tenure_write_basis(w, tie, None, "p_high", None, frozenset(),
                                born=frozenset({"r_n2"})) is None
    # A NEWBORN RUNG (batch B-I close, A1): founding opens only its `contain`. A first `hold` on it
    # would feed `in_holdings` and the `rung_above_in_holdings` revocation basis -- a claim of
    # ownership nobody made (`loop/effects_founding.py`, H-166) -- so the clause is Records only.
    w.rungs["r_rung"] = Rung("r_rung", "hearth")
    hr = w.add_tenure(Tenure("thr", "p_low", "r_rung", "hold", since=w.tick))
    assert G.tenure_write_basis(w, hr, None, "p_high", None, frozenset(),
                                born=frozenset({"r_rung"})) is None


# (3) THE FALSIFIER, IN COMPUTED PLAY ------------------------------------------------------------

@pytest.fixture(scope="module")
def realm1():
    """`populated.run`'s construction, one season, seed 0, through the real chooser -- with the
    `issue` and `petition` effects WRAPPED (instrumentation only: the effect, its subjects and its
    write are the shipped ones) so the live holders of each minted Record are read the instant the
    gate applies the mint. Read at the end of the season instead they can be gone: a person's
    Tenures leave the store with him (`World.tenures`), and the one writ `build_realm(0)` issues in
    season 1 is addressed to `p_npc_020`, who dies that season."""
    seen: dict = {}
    w = POP.build_realm(0)

    def watching(fn):
        def eff(w_, a, res=None):
            ch = fn(w_, a, res)
            if not ch.subjects:
                return ch

            def apply():
                ch.apply()
                rid = ch.subjects[0].id
                seen[a.id] = (rid, [t.subject for t in w_.tenures
                                    if t.kind == "hold" and t.object == rid and t.live])
            return G.Change(ch.subjects, apply)
        return eff

    with pytest.MonkeyPatch.context() as mp:
        for verb in ("issue", "petition"):
            mp.setitem(EFFECTS, verb, watching(EFFECTS[verb]))
        d = SeasonDriver(w)
        mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
        ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                          draw=draw_factory(w.world_seed, lambda: w.tick))
        d.season(ch, question=None, subsistence=POP.P.SUBSIST,
                 contest_max_depth=w.fixtures.get("contest_max_depth"))
    return w, attribute(w, d, 1), seen


def test_in10c_every_computed_writ_is_held_by_its_addressee(realm1):
    w, rows, seen = realm1
    issued = [a for a, made, _ in rows if a.verb == "issue" and made]
    assert issued, sorted(Counter(a.verb for a, made, _ in rows if made).items())
    for a in issued:
        rid, holders = seen[a.id]
        assert w.records[rid].kind == "dispensation", a
        assert a.payload["to"] != a.actor
        assert holders == [a.payload["to"]], (a, holders)


def test_in10c_every_computed_petition_is_held_by_its_maker(realm1):
    w, rows, seen = realm1
    filed = [a for a, made, _ in rows if a.verb == "petition" and made]
    assert filed, "no petition was filed in the season, so the control observed nothing"
    for a in filed:
        rid, holders = seen[a.id]
        assert w.records[rid].kind == "petition" and holders == [a.actor], (a, holders)
