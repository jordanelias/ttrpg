"""v9 IN-40 -- `H-101`, VASSALAGE: SOMETHING CAN BE UNDER SOMETHING, ACROSS FACTIONS.
v9 IN-40 (landed `3f320093`; its entry left the plan at the B-J boundary).

What the position built, each asked of the real fold, the real MATTER barrier and the real gate:
  * `state/gate.py::purview_reaches`' OBLIGE CLAUSE: a seat also reaches the ground (rung and its
    descendants) of every seat whose holder owes it a live `oblige` -- ONE EDGE DEEP. No stored
    parent: "under" is the swearer's own edge, read downward from the seat sworn to.
  * `state/gate.py::sworn_to` -- the live `oblige` edges sworn to a seat -- re-exported as
    `world_q.sworn_to`, and the walk `world_q.establishment_of` now composes on.

THE EXIT AND THE FALSIFIERS, each with the mutation that turns it red:
  1. THE EHRENWALL SPLIT. The Grandmaster's live `oblige` to a Crown seat lets that seat's purview
     reach his rungs (and lets it confer a seat there, through the real fold); after the `oblige`
     is `release`d, or lapses unrenewed at MATTER, the same question answers no.
     Mutations: delete the clause (red at "reaches while sworn"); read closed edges too (red at
     "answers no after").
  2. CONTAINMENT: purview over a seat whose ground is neither in the superior's rung subtree nor in
     a sworn swearer's -> refused. Mutation: the clause reads every oblige the swearer holds, not
     only those sworn to THIS seat.
  3. NO UPWARD REACH: a seat asked about the rung above it, with nobody sworn to it -> refused; and
     the swearer's own seat gains nothing over the seat he swore to. Mutation: make the clause
     upward (a seat reaches the ground of the seat ITS holder swore to).
  4. ONE EDGE DEEP (the position's chain-depth decision, attacked): a vassal's own sworn vassal is
     not reached through him. Mutation: recurse through `purview_reaches`.

The fixture is `probes.tiny_world` (`R` > `D` > `S` > `Hh`; `p_high` holds `off_duke`, a Crown seat
at `D`), plus two sibling grounds under `R`, OUTSIDE the duke's: `D2` (the Löwenritter's, with a
commandery `C` inside it), held through `off_lion` by `p_other`; and `D3` (a Hafenmark barony),
held through `off_baron` by `p_low`. `off_lion_reeve` is an UNHELD appointed seat at `C`.
"""

from __future__ import annotations

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import WriteClass
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..state import gate as G
from ..state.carriers import Act, Office, Rung, Tenure
from ..state.gate import may_fill, purview_reaches

CROWN, DUKE = "off_duke", "p_high"
LION, MASTER = "off_lion", "p_other"
BARONY, BARON = "off_baron", "p_low"
REEVE = "off_lion_reeve"


def _world(**fx):
    """The split world (module docstring), one MATTER barrier run (tick 0)."""
    fixtures = DEFAULT_FIXTURES
    for name, value in fx.items():
        fixtures = fixtures.sweep(name, value)
    w = P.tiny_world(fixtures)
    for rid, kind, parent in (("D2", "duchy", "R"), ("C", "settlement", "D2"),
                              ("D3", "duchy", "R")):
        w.rungs[rid] = Rung(rid, kind)
        w.add_tenure(Tenure(f"t_{rid}_in", rid, parent, "contain", 0))
    # roster-exempt: TEST FIXTURE ids.
    for oid, post, rung, faction, holder in ((LION, "Grandmaster", "D2", "Löwenritter", MASTER),
                                             (BARONY, "Baron", "D3", "Hafenmark", BARON),
                                             (REEVE, "Reeve", "C", "Löwenritter", None)):
        w.offices[oid] = Office(oid, post, rung, ["issue"], faction=faction, conferral="appointed")
        if holder:
            w.add_tenure(Tenure(f"t_{oid}", holder, oid, "hold", 0))
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


def _swear(w, d, who, seat, key):
    out = _fold(w, d, Act(id=key, actor=who, verb="oblige", payload={"subject": seat}))
    assert _kinds(out) == ["duty.taken"], ("fixture: the oblige was not taken", _kinds(out))


def _reaches(w, seat, rung):
    return purview_reaches(w, w.offices[seat], rung)


def _season(w, d):
    """The next season's MATTER barrier and nothing else (`test_term_upkeep.py`'s shape)."""
    w.tick += 1
    return d.matter(mint_token(w, WriteClass.MATTER), [])


# ================================================================================================
# 0 -- THE READER: `sworn_to` IS THE LIVE `oblige` EDGES ON A SEAT, AND `establishment_of` READS IT
# ================================================================================================

def test_in40_sworn_to_reads_live_obliges_on_the_seat_and_is_world_qs_query():
    w, d = _world()
    assert world_q.sworn_to is G.sworn_to, "two bodies for one walk"
    assert world_q.sworn_to(w, CROWN) == [] and world_q.sworn_to(w, None) == []
    _swear(w, d, MASTER, CROWN, "ob1")
    _swear(w, d, "p_mid", LION, "ob2")
    [t] = world_q.sworn_to(w, CROWN)
    assert (t.subject, t.object, t.kind, t.live) == (MASTER, CROWN, "oblige", True)
    assert [x.subject for x in world_q.sworn_to(w, LION)] == ["p_mid"]
    assert world_q.establishment_of(w, CROWN) == [MASTER]
    _fold(w, d, Act(id="rel", actor=MASTER, verb="release", payload={"subject": CROWN}))
    assert world_q.sworn_to(w, CROWN) == [] and world_q.establishment_of(w, CROWN) == []


# ================================================================================================
# 1 -- THE EXIT: THE EHRENWALL SPLIT, BY `release` AND BY AN UNRENEWED TERM
# ================================================================================================

def test_in40_ehrenwall_split_by_release():
    """Sworn, the Crown seat reaches the Grandmaster's ground (`D2`) and what it contains (`C`);
    released, the same two questions answer no. Nothing but the edge changed."""
    w, d = _world()
    assert not _reaches(w, CROWN, "D2") and not _reaches(w, CROWN, "C"), (
        "fixture: the Crown seat reaches the Löwenritter ground with nobody sworn")
    _swear(w, d, MASTER, CROWN, "ob_split")
    assert _reaches(w, CROWN, "D2") and _reaches(w, CROWN, "C"), (
        "a live oblige to the Crown seat did not extend its purview to the swearer's ground")
    assert _reaches(w, CROWN, "D"), "the seat's own ground is still its own"
    out = _fold(w, d, Act(id="forswear", actor=MASTER, verb="release", payload={"subject": CROWN}))
    assert _kinds(out) == ["tenure.closed"], _kinds(out)
    assert not _reaches(w, CROWN, "D2") and not _reaches(w, CROWN, "C"), (
        "the purview is unchanged after the oblige ended -- not built")


def test_in40_ehrenwall_split_by_an_unrenewed_term_at_matter():
    """`_eff_oblige` opens the edge with `Term(tick + oblige_term)`; nobody renews it, so MATTER
    matures it (T-n) and the purview goes with it -- a detachment nobody acted to cause."""
    n = 2
    w, d = _world(oblige_term=n)
    _swear(w, d, MASTER, CROWN, "ob_term")
    [t] = world_q.sworn_to(w, CROWN)
    assert t.term is not None and t.term.matures_at == w.tick + n, t.term
    for _ in range(n - 1):
        _season(w, d)
        assert t.live and _reaches(w, CROWN, "D2"), "lapsed before its term"
    _season(w, d)
    assert not t.live, "fixture: MATTER did not mature the unrenewed term"
    assert not _reaches(w, CROWN, "D2") and not _reaches(w, CROWN, "C"), (
        "the purview outlived the lapsed oblige")


def test_in40_the_swearers_ground_goes_when_he_gives_up_the_seat_he_brought():
    """The sworn purview is the swearer's LIVE holds: the oblige stands, but once the Grandmaster ends
    his own `hold` on the Löwenritter seat he brings no ground. Mutation: drop `h.live` from the
    clause's hold walk (red: a closed `hold` still extends the purview)."""
    w, d = _world()
    _swear(w, d, MASTER, CROWN, "ob_hold")
    assert _reaches(w, CROWN, "D2")
    out = _fold(w, d, Act(id="step_down", actor=MASTER, verb="release", payload={"subject": LION}))
    assert _kinds(out) == ["tenure.closed"], _kinds(out)
    assert [t.subject for t in world_q.sworn_to(w, CROWN)] == [MASTER], "the oath ended with the seat"
    assert not _reaches(w, CROWN, "D2") and not _reaches(w, CROWN, "C"), (
        "a closed hold still brought its ground to the sworn seat")


def test_in40_the_split_moves_an_outcome_through_the_fold():
    """WHO HAS PURVIEW OVER WHOM CHANGES WHAT EXECUTES: the duke, exercising the Crown seat, may fill
    the Löwenritter reeve's seat at `C` only while the Grandmaster is sworn to it (`may_fill` ->
    `purview_reaches`). Asked of the predicate and of a real `confer` through the fold."""
    w, d = _world()
    assert not may_fill(w, DUKE, CROWN, w.offices[REEVE])
    _swear(w, d, MASTER, CROWN, "ob_fill")
    assert may_fill(w, DUKE, CROWN, w.offices[REEVE])
    _fold(w, d, Act(id="forswear", actor=MASTER, verb="release", payload={"subject": CROWN}))
    assert not may_fill(w, DUKE, CROWN, w.offices[REEVE]), "the split did not end the conferral right"

    w2, d2 = _world()
    _swear(w2, d2, MASTER, CROWN, "ob_fill2")
    _fold(w2, d2, Act(id="cf", actor=DUKE, verb="confer", via=CROWN,
                      payload={"office": REEVE, "to": "p_mid"}))
    held = [t.subject for t in w2.tenures if t.kind == "hold" and t.object == REEVE and t.live]
    assert held == ["p_mid"], ("a sworn Grandmaster's commandery seat was not conferrable", held)

    w3, d3 = _world()
    out = _fold(w3, d3, Act(id="cf", actor=DUKE, verb="confer", via=CROWN,
                            payload={"office": REEVE, "to": "p_mid"}))
    assert not [t for t in w3.tenures if t.kind == "hold" and t.object == REEVE and t.live], (
        "control: with nobody sworn, the Crown seat filled a seat outside its ground", _kinds(out))


# ================================================================================================
# 2 -- FALSIFIER: CONTAINMENT -- NEITHER IN THE SUBTREE NOR IN A SWORN SWEARER'S
# ================================================================================================

def test_in40_purview_over_ground_neither_contained_nor_sworn_is_refused():
    """The Grandmaster is sworn to the Crown seat; the Baron is sworn to NOBODY's seat that matters
    here -- he swore to a seat of his own choosing elsewhere (the dicastery). The Crown seat reaches
    `D2`, never `D3`; and a person sworn to the Crown seat who holds no seat brings no ground."""
    w, d = _world()
    _swear(w, d, MASTER, CROWN, "ob1")
    _swear(w, d, BARON, "off_dicastery", "ob2")
    _swear(w, d, "p_mid", CROWN, "ob3")                    # sworn, but holds nothing
    assert _reaches(w, CROWN, "D2")
    assert not _reaches(w, CROWN, "D3"), (
        "the Crown seat reached a barony neither in its ground nor in a sworn holder's")
    assert not may_fill(w, DUKE, CROWN, w.offices[BARONY])
    checked = 0
    for rung in ("R", "D3"):
        assert not _reaches(w, CROWN, rung), rung
        checked += 1
    assert checked == 2


# ================================================================================================
# 3 -- FALSIFIER: NO UPWARD REACH
# ================================================================================================

def test_in40_no_upward_reach_with_or_without_an_oblige():
    """With nobody sworn to it, a seat asked about the rung above it answers no. And the clause is
    not symmetric: the Grandmaster's seat, whose holder swore to the Crown seat, gains nothing over
    the Crown seat's ground or the rung above -- *"Upward reach is petition, never purview"*."""
    w, d = _world()
    assert G.parent_of(w, "D2") == "R"
    assert not _reaches(w, LION, "R"), "a seat nobody swore to reached the rung above it"
    _swear(w, d, MASTER, CROWN, "ob_up")
    for rung in ("R", "D", "S", "Hh"):
        assert not _reaches(w, LION, rung), f"the swearer's seat reached {rung} by his own oblige"
    assert not _reaches(w, CROWN, "R"), "the seat sworn to reached the rung above its own"


# ================================================================================================
# 4 -- THE CHAIN-DEPTH DECISION: ONE EDGE DEEP
# ================================================================================================

def test_in40_one_edge_deep_a_vassals_vassal_is_not_reached_through_him():
    """The Baron swears to the Grandmaster's seat; the Grandmaster to the Crown seat. The
    Grandmaster's seat reaches the barony (one edge); the Crown seat does not (two edges) -- the
    Baron swore to the Grandmaster, not to the Crown. A cycle of mutual obliges terminates."""
    w, d = _world()
    _swear(w, d, BARON, LION, "ob_b")
    _swear(w, d, MASTER, CROWN, "ob_m")
    assert _reaches(w, LION, "D3"), "one edge: the Grandmaster's seat does not reach his sworn baron"
    assert _reaches(w, CROWN, "D2")
    assert not _reaches(w, CROWN, "D3"), "the Crown seat reached its vassal's vassal -- chained"
    _swear(w, d, DUKE, LION, "ob_cycle")                     # the duke swears back: a cycle
    assert _reaches(w, LION, "D") and _reaches(w, CROWN, "D2")
    assert not _reaches(w, BARONY, "D2"), "nobody swore to the barony"


# ================================================================================================
# 5 -- A DETERMINATION-IMPOSED OBLIGE IS NOT AN OATH (SC-03a x IN-40 close)
# ================================================================================================

def _convicted(w, d, key="sent"):
    """`DUKE`, exercising the Crown seat (a judging seat over `Hh`, where `MASTER` lives), opens a case
    on `MASTER` and determines it with NO declared arrangement -- the undeclared disposal, an
    `oblige` of `MASTER`'s on the Crown seat that he never swore."""
    out = _fold(w, d, Act(id=f"{key}_oc", actor=DUKE, verb="open_case", via=CROWN,
                          payload={"subject": MASTER}))
    assert _kinds(out) == ["case.opened"], ("fixture: the case was not opened", _kinds(out))
    out = _fold(w, d, Act(id=f"{key}_dt", actor=DUKE, verb="determine", via=CROWN,
                          payload={"subject": MASTER}))
    assert _kinds(out) == ["matter.determined"], ("fixture: not determined", _kinds(out))
    assert out[0].degree in ("Overwhelming", "Success"), out[0].degree


def test_in40_a_determination_imposed_oblige_is_not_an_oath_and_extends_no_purview():
    """A judge's finding binds the convict to the bench (he joins `establishment_of`, C-1) and must not
    hand the bench the convict's own seat ground: the clause reads an OATH, and a sentence is not one.
    CONTROL, one clause away: the same man voluntarily sworn to the same seat DOES extend it.
    Mutation: drop the `determined_by` skip in `purview_reaches` (red at the reach assertion).
    v9 SC-03b: `determine` is contested, so the judge is a STRONG one (`pool_default` 30) and the fixture
    asserts the band it opened at."""
    w, d = _world(pool_default=30)
    assert not _reaches(w, CROWN, "D2"), "fixture: the Crown seat reaches D2 with nobody bound"
    _convicted(w, d)
    assert MASTER in world_q.establishment_of(w, CROWN), "the sentence did not bind him to the bench"
    [edge] = world_q.sworn_to(w, CROWN)
    assert edge.payload == {"determined_by": "sent_dt"}, edge.payload
    assert not _reaches(w, CROWN, "D2") and not _reaches(w, CROWN, "C"), (
        "a convict's imposed oblige gave the judging seat purview over his own seat ground")
    w2, d2 = _world()
    _swear(w2, d2, MASTER, CROWN, "oath")
    assert _reaches(w2, CROWN, "D2") and _reaches(w2, CROWN, "C"), "control: a sworn oblige must reach"
