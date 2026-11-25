"""v9 IN-27 (END-VICTORY; H-176, GD-1), batch B-U: THE ENDING VOCABULARY, A QUERY THE SEASON REPORTS.

#457 D6's adopted answer: *"the ending vocabulary is a Query over holds and seats that the season reports --
never an actor"*. The vocabulary is `rosters.yaml: endings` (loaded by `data/rosters.py::_load_endings`),
the Query is `queries/world_q.py::endings_reached`, and `loop/driver.py::SeasonDriver.season` reports it as
`endings`.

THE EXIT (#457, verbatim): *an ending reached by choices only* -- (a), on the built realm with the shipped
`theocracy` row: the King's own `release` and `commit`, folded through the real `resolve`, reach it, and the
report names his act. THE FALSIFIER (T-b): *an ending fired by a threshold with no person's act among its
antecedents -> fail* -- (b), the same conditions planted by direct Tenure construction, as the seeded realm
has its edges, are TRUE and report nothing.

  (a) a person's act reaches an ending, and the report names the act: the King converts (shipped row,
      `build_realm(0)`); a `confer` opens the selected hold (a planted row, the governance world).
  (b) THE CONTROL: each condition planted with no act reports nothing, while the condition holds.
  (c) the Query and `season()` move nothing: content hash, log length and gate writes are those of a
      season with the Query not called, and calling it on a world changes none of them.
  (d) the loader refuses a malformed ending row, naming it, and a second victory row (GD-1).
  (e) `season()` on `build_realm(0)` executes the step (spied) and reports `endings == []`, at the pinned
      one- and two-season hashes.
"""
from __future__ import annotations

import pytest

from engine.season.data import rosters as R
from engine.season.data.matrix import WriteClass
from engine.season.gaps import Unspecified
from engine.season.boot.realm import build_realm
from engine.season.harness import probes as P
from engine.season.loop import driver as DRV
from engine.season.decision import make_chooser
from engine.season.loop.driver import SeasonDriver, mint_token, resolvable_verbs
from engine.season.queries import world_q as Q
from engine.season.state import gate
from engine.season.state.carriers import Act, Event, Tenure
from engine.season.state.ids import H, ROOT, draw_factory

from .test_g3_not_yours import _gov_world, _hold
from .test_governance_build import _establish, _establish_world, _founding, _seat_reeve

CHURCH = R.faction_prop_id("Church of Solmund")
CROWN = R.faction_prop_id("Valorsmark")
#: A row naming the governance world's unheld appointed seat (`off_reeve`, post `Reeve`), planted where
#: the Query reads its rows: the shipped rows name a King, whose seat no act can confer (its conferral is
#: `inheritance` since v10 IN-61, claimed by the heir's `succeed`, never conferred: `offices.yaml: off_king`).
REEVE_ROW = {"crowned_reeve": R.EndingRow(False, ("post", "Reeve"), "Valorsmark", "a test fixture")}


def _fold(w, d, *acts):
    """Fold hand-built acts through the shipped `SeasonDriver.resolve` and log what it emits, as
    `season()` does (S19.5 -- one log)."""
    out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts),
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return [e.kind for e in out]


def _admit(w, joiner, fac, tag):
    """B21.63: joining a faction is answered by it. Fold, BEFORE the joiner's own `commit` (a batch is not folded in the order written), the two
    acts by which a person who may admit (`gate.may_admit`: the head seat's holder or a member whose seat confers) utters an `OUGHT` naming
    `joiner` and `fac` and commits to it. The tests below were each a unilateral join."""
    who = next(m for m in sorted(w.persons) if gate.may_admit(w, m, fac))
    d = SeasonDriver(w)
    said = _fold(w, d, Act(id=f"in27_say_{tag}", actor=who, verb="utter", payload={"mood": "OUGHT", "subject": joiner, "value": fac}))
    yes = _fold(w, d, Act(id=f"in27_yes_{tag}", actor=who, verb="commit", payload={"subject": f"prop:in27_say_{tag}"}))
    assert said == ["proposition.uttered"] and yes == ["commitment.made"], (said, yes)


def _king(w):
    """The King's seat in the built realm and the person on it (`off_<holder>`, not `offices.yaml`'s id)."""
    off = next(o for o in sorted(w.offices) if w.offices[o].post == "King")
    return off, Q.hold_force(w, off).subject


def _membership(w, pid, fac):
    return [t for t in w.persons[pid].tenures if t.kind == "commit" and t.live and t.object == fac]


def _row(name):
    return R.ENDINGS[name]


# ======================================================================================
# (a) AN ENDING REACHED BY CHOICES ONLY
# ======================================================================================

def test_in27_the_king_converts_and_the_realm_reaches_theocracy_by_his_act():
    """THE EXIT. The built realm's King coheres under the Crown; he releases that membership and commits
    to the Church of Solmund, two `own` acts through the real fold. The shipped `theocracy` row is then
    reached, and its antecedents are his `commit` act and the Event it emitted."""
    w = build_realm(0)
    d = SeasonDriver(w)
    off, king = _king(w)
    assert Q.faction_holding(w, king) == CROWN and CHURCH in w.propositions, "fixture"
    assert Q.endings_reached(w) == [], "the built realm reached an ending with no act"
    _admit(w, king, CHURCH, "church")
    kinds = _fold(w, d, Act(id="in27_release", actor=king, verb="release", payload={"subject": CROWN}),
                  Act(id="in27_commit", actor=king, verb="commit", payload={"subject": CHURCH}))
    assert "commitment.made" in kinds and not _membership(w, king, CROWN), kinds
    assert Q.faction_holding(w, king) == CHURCH, "the conversion did not move his faction"
    got = {r.ending: r for r in Q.endings_reached(w)}
    assert set(got) == {"theocracy"}, got
    th = got["theocracy"]
    assert th.victory is False and th.acts == ("in27_commit",), th
    assert th.holds == (Q.hold_force(w, off).id,), th
    opened = [e for e in w.log if e.id in th.events]
    assert [e.kind for e in opened] == ["commitment.made"] and opened[0].causes[0] == "in27_commit", opened


def test_in27_a_confer_opens_the_selected_hold_and_the_report_names_it(monkeypatch):
    """The hold half: `p_king` confers the unheld `off_reeve` on `p_mid`, a Crown man by a seeded
    membership. The planted row is reached and its antecedent is the `confer` act, though the
    membership it also reads opened by no act."""
    monkeypatch.setattr(Q, "ENDINGS", REEVE_ROW)
    w, d = _gov_world()
    w.add_tenure(Tenure("t_mid_crown", "p_mid", CROWN, "commit", 0))
    assert _hold(w, "off_reeve") is None and Q.endings_reached(w) == [], "fixture"
    kinds = _fold(w, d, Act(id="in27_cf", actor="p_king", verb="confer", via="off_crown",
                            payload={"subject": "off_reeve", "office": "off_reeve", "to": "p_mid"}))
    assert kinds == ["tenure.opened"], kinds
    (got,) = Q.endings_reached(w)
    assert got.ending == "crowned_reeve" and got.acts == ("in27_cf",), got
    assert got.holds == (_hold(w, "off_reeve").id,), got


def _realm_territories(w):
    """The territories under the built realm's `realm` rung -- not `terr_T16`, Schoenland's foreign root."""
    inside = {r for x in w.rungs if w.rungs[x].kind == "realm" for r in Q.descendants(w, x)}
    return sorted(r for r in inside if r in w.rungs and w.rungs[r].kind == "territory")


def _all_but_one_under_the_crown(w):
    """Every territory OF THE REALM governed by a Crown man, by construction, except that one territory
    holder coheres under no faction: the realm's uncontrolled territory is given to the King, and every
    other holder's faction memberships are closed and a Crown one planted. Returns that last holder, the
    one person whose membership decides GD-1's row. `terr_T16` (outside the realm) is left unheld."""
    _, king = _king(w)
    holders = []
    for r in _realm_territories(w):
        t = Q.governing_hold(w, r)
        if t is None:
            w.add_tenure(Tenure(f"t_in27_{r}", king, r, "hold", 0))
        elif t.subject not in holders and t.subject != king:
            holders.append(t.subject)
    last = holders[-1]
    for pid in holders:
        for t in w.persons[pid].tenures:
            if t.kind == "commit" and t.live and t.object in R.FACTION_BY_PROP:
                t.until = w.tick
        if pid != last:
            w.add_tenure(Tenure(f"t_in27_{pid}_crown", pid, CROWN, "commit", 0))
    return last


def test_in27_peninsular_sovereignty_is_reached_by_the_last_holders_act_and_not_without_it():
    """GD-1's one victory row, both arms on the built realm. With every territory a Crown man's but one
    holder's (by construction) the condition fails; that holder's own `commit` to the Crown reaches the
    row, naming his act. CONTROL: the same membership planted by construction makes the condition true
    and reports nothing."""
    w = build_realm(0)
    last = _all_but_one_under_the_crown(w)
    row = _row("peninsular_sovereignty")
    assert w.rungs["terr_T16"].kind == "territory" and "terr_T16" not in _realm_territories(w), "fixture"
    assert Q.governing_hold(w, "terr_T16") is None, "fixture: the foreign root is held by nobody"
    assert not Q._ending_edges(w, row) and Q.endings_reached(w) == [], "fixture: one holder is under none"
    _admit(w, last, CROWN, "crown")
    kinds = _fold(w, SeasonDriver(w), Act(id="in27_swear", actor=last, verb="commit", payload={"subject": CROWN}))
    assert kinds[-1] == "commitment.made", kinds
    (got,) = Q.endings_reached(w)
    assert got.ending == "peninsular_sovereignty" and got.victory is True, got
    assert got.acts == ("in27_swear",) and len(got.holds) > 1, got
    # THE REALM'S TERRITORIES ARE SELECTED, AND THE FOREIGN ROOT IS NOT (an unheld selected rung
    # would have made the condition false and the report empty)
    selected = {t.object for t in Q._ending_edges(w, row) if t.kind == "hold"}
    assert "terr_T16" not in selected and selected == set(_settled_territories(w)), selected
    assert set(_realm_territories(w)) - selected == {"terr_T15"}, "only the unsettled territory is not asked for"

    control = build_realm(0)
    last = _all_but_one_under_the_crown(control)
    control.add_tenure(Tenure("t_in27_last_crown", last, CROWN, "commit", 0))
    assert Q._ending_edges(control, row), "control: the planted condition does not hold"
    assert Q.endings_reached(control) == [], "GD-1's row fired with no person's act among its antecedents"


def _settled_territories(w):
    """The realm's territories with a `settlement` rung among their descendants -- what the shipped
    `peninsular_sovereignty` row's `settled: true` selects (B12a.09)."""
    return [r for r in _realm_territories(w)
            if any(x in w.rungs and w.rungs[x].kind == "settlement" for x in Q.descendants(w, r))]


def _settled_all_but_one_under_the_crown(w):
    """`_all_but_one_under_the_crown`, then every UNSETTLED realm territory (`terr_T15`, which the helper
    gave the King) left unheld again, so the planted world holds exactly the settled territories. Returns
    the last holder."""
    last = _all_but_one_under_the_crown(w)
    settled = set(_settled_territories(w))
    unsettled = [r for r in _realm_territories(w) if r not in settled]
    assert unsettled, "fixture: the realm has an unsettled territory (terr_T15)"
    for r in unsettled:
        for t in w.tenures:
            if t.live and t.kind == "hold" and t.object == r:
                t.until = w.tick
        assert Q.governing_hold(w, r) is None, "fixture"
    return last


def test_peninsular_sovereignty_is_reached_when_every_settled_territory_is_held_under_one_faction_by_an_act():
    """B12a.09 / `09_WR_world_motion` gate (3): the unsettled `terr_T15` stays unheld (no verb holds it), every
    SETTLED territory is a Crown man's but one holder's, and that holder's own `commit` reaches the shipped
    row, naming his act; the selected holds are the settled territories and no other. FALSIFIER: the row
    reached with a SETTLED territory unheld (the last arm)."""
    w = build_realm(0)
    last = _settled_all_but_one_under_the_crown(w)
    settled = set(_settled_territories(w))
    assert len(settled) >= 14 and "terr_T15" not in settled, settled
    assert Q.governing_hold(w, "terr_T15") is None, "fixture: the unsettled territory is unheld"
    _admit(w, last, CROWN, "crown9")
    kinds = _fold(w, SeasonDriver(w), Act(id="in27_swear9", actor=last, verb="commit", payload={"subject": CROWN}))
    assert kinds[-1] == "commitment.made", kinds
    (got,) = Q.endings_reached(w)
    assert got.ending == "peninsular_sovereignty" and got.victory is True and got.acts == ("in27_swear9",), got
    selected = {t.object for t in Q._ending_edges(w, _row("peninsular_sovereignty")) if t.kind == "hold"}
    assert selected == settled, selected
    # the leak arm: one settled territory unheld -> not reached, though every other condition stands
    gone = sorted(settled)[0]
    for t in w.tenures:
        if t.live and t.kind == "hold" and t.object == gone:
            t.until = w.tick
    assert Q.governing_hold(w, gone) is None, "fixture"
    assert Q.endings_reached(w) == [], "reached with a settled territory unheld"


def test_it_is_not_reached_when_one_settled_territory_is_held_by_another_faction():
    """The same planted world, but one settled territory's holder coheres under the Church: not reached; with
    that holder back under the Crown it is (the same act is credited), so the one difference is the holder."""
    w = build_realm(0)
    last = _settled_all_but_one_under_the_crown(w)
    king = _king(w)[1]
    other = next(Q.governing_hold(w, r).subject for r in sorted(_settled_territories(w))
                 if Q.governing_hold(w, r).subject not in (last, king))
    for t in w.persons[other].tenures:
        if t.kind == "commit" and t.live and t.object in R.FACTION_BY_PROP:
            t.until = w.tick
    w.add_tenure(Tenure("t_in27_other_church", other, CHURCH, "commit", 0))
    assert Q.faction_holding(w, other) == CHURCH, "fixture"
    _admit(w, last, CROWN, "crown9b")
    _fold(w, SeasonDriver(w), Act(id="in27_swear9b", actor=last, verb="commit", payload={"subject": CROWN}))
    assert Q.endings_reached(w) == [], "a Church man's territory was read as one faction's"
    for t in w.persons[other].tenures:
        if t.kind == "commit" and t.live and t.object == CHURCH:
            t.until = w.tick
    w.add_tenure(Tenure("t_in27_other_crown", other, CROWN, "commit", 0))
    assert [r.ending for r in Q.endings_reached(w)] == ["peninsular_sovereignty"]


def test_in27_one_faction_is_not_met_by_a_holder_who_commits_elsewhere():
    """KILLS `want = set(facs)` (A-F2 ii): with every realm territory a Crown man's but one, that last
    holder's own `commit` goes to the CHURCH. The holders now cohere under two factions, so `one_faction`
    fails and nothing is reported, though an act opened an edge the mutated condition would read."""
    w = build_realm(0)
    last = _all_but_one_under_the_crown(w)
    _admit(w, last, CHURCH, "stray")
    kinds = _fold(w, SeasonDriver(w), Act(id="in27_stray", actor=last, verb="commit", payload={"subject": CHURCH}))
    assert kinds[-1] == "commitment.made" and Q.faction_holding(w, last) == CHURCH, kinds
    assert not Q._ending_edges(w, _row("peninsular_sovereignty"))
    assert Q.endings_reached(w) == [], "holders under two factions were read as under one"


def test_in27_a_king_who_commits_to_a_third_faction_is_no_theocracy():
    """KILLS deleting `set(facs) != want` (A-F2 i): the built realm's King releases the Crown and commits
    by act to a rostered faction that is neither the Crown nor the Church. He coheres under a faction,
    his act opened the edge, and `theocracy` is still not reached: his faction is not the row's."""
    w = build_realm(0)
    _, king = _king(w)
    third = next(f for f in sorted(R.FACTION_BY_PROP) if f in w.propositions and f not in (CROWN, CHURCH))
    _admit(w, king, third, "third")
    kinds = _fold(w, SeasonDriver(w), Act(id="in27_release3", actor=king, verb="release", payload={"subject": CROWN}),
                  Act(id="in27_commit3", actor=king, verb="commit", payload={"subject": third}))
    assert "commitment.made" in kinds and Q.faction_holding(w, king) == third, kinds
    assert "theocracy" not in [r.ending for r in Q.endings_reached(w)], "a King of a third faction"


def test_in27_a_redundant_commit_by_act_is_not_credited():
    """MAJOR 2's falsifier. Arm 1 of the control below (the King planted into the Church by construction:
    the condition true, nothing reported), then the King folds a `commit` to the Church he already
    coheres under. `commit` needs only the Proposition and `_eff_commit` mints a fresh edge, so the act
    executes and changes nothing the condition reads -- it must not be reported as the antecedent."""
    w = build_realm(0)
    _, king = _king(w)
    for t in _membership(w, king, CROWN):
        t.until = w.tick
    w.add_tenure(Tenure("t_king_church_planted", king, CHURCH, "commit", 0))
    assert Q._ending_edges(w, _row("theocracy")) and Q.endings_reached(w) == [], "fixture"
    kinds = _fold(w, SeasonDriver(w), Act(id="in27_again", actor=king, verb="commit",
                                          payload={"subject": CHURCH}))
    assert "commitment.made" in kinds and len(_membership(w, king, CHURCH)) == 2, kinds
    assert Q.faction_holding(w, king) == CHURCH, "two commits to one faction are one faction"
    assert Q._ending_edges(w, _row("theocracy")), "the condition still holds"
    assert Q.endings_reached(w) == [], "an act that changed nothing the condition reads was credited"


# ======================================================================================
# (b) THE CONTROL -- THE SAME CONDITIONS, NO ACT: TRUE, AND NOT AN ENDING (T-b)
# ======================================================================================

def test_in27_a_condition_planted_with_no_act_is_true_and_reports_nothing(monkeypatch):
    """THE FALSIFIER OBSERVING THE FAILURE IT EXCLUDES. Each arm makes a row's condition TRUE by direct
    Tenure construction -- the way the seeded realm has every edge -- and the Query reports nothing.
    Each arm asserts the condition holds first (`_ending_edges` non-empty), so a nothing reported because
    the condition failed cannot pass for the act requirement working."""
    checked = 0
    # arm 1: the built realm, its King planted into the Church (the shipped row)
    w = build_realm(0)
    _, king = _king(w)
    for t in _membership(w, king, CROWN):
        t.until = w.tick
    w.add_tenure(Tenure("t_king_church_planted", king, CHURCH, "commit", 0))
    assert Q._ending_edges(w, _row("theocracy")), "control: the planted condition does not hold"
    assert Q.endings_reached(w) == [], "an ending fired with no person's act among its antecedents"
    checked += 1
    # arm 2: the governance world, its Reeve seated by construction (the planted row)
    monkeypatch.setattr(Q, "ENDINGS", REEVE_ROW)
    w, _ = _gov_world()
    w.add_tenure(Tenure("t_mid_crown", "p_mid", CROWN, "commit", 0))
    w.add_tenure(Tenure("t_reeve_planted", "p_mid", "off_reeve", "hold", 0))
    assert Q._ending_edges(w, REEVE_ROW["crowned_reeve"]), "control: the planted condition does not hold"
    # an Event NAMING the planted hold, caused by `[ROOT]` (no act): the walk reaches it, `causing_act`
    # answers `None`, and it is neither an opening nor a raise (A-F6)
    w.log.append(Event("ev_in27_root", "tenure.opened", [P.about(w, "t_reeve_planted")], [ROOT], w.tick))
    assert Q.causing_act(w, w.log[-1]) is None, "fixture: the planted Event has a causing act"
    assert Q.endings_reached(w) == [], "an ending fired with no person's act among its antecedents"
    checked += 1
    # arm 3: an act NAMES the planted hold without opening it -- `establish` re-stamps a sitting
    # holder's grant (`tenure.payload_set`); a re-grant is not the act the condition stands on
    w, d = _establish_world()
    _seat_reeve(w, ["issue"])
    w.add_tenure(Tenure("t_mid_crown", "p_mid", CROWN, "commit", 0))
    out = _establish(w, d, "in27_restamp", _founding(remit=["issue", "dispatch"]))
    w.log.extend(out)
    assert "tenure.payload_set" in [e.kind for e in out], [e.kind for e in out]
    assert Q._ending_edges(w, REEVE_ROW["crowned_reeve"]), "control: the planted condition does not hold"
    assert Q.endings_reached(w) == [], "a re-grant naming a seeded hold was read as its opening"
    checked += 1
    assert checked == 3


def test_in27_nothing_selected_reaches_nothing(monkeypatch):
    """"Every King is a Church man" is vacuously true of a world with no King: a row whose selector
    finds nothing is not reached, even with acts in the log."""
    w, d = _gov_world()
    _fold(w, d, Act(id="in27_cf", actor="p_king", verb="confer", via="off_crown",
                    payload={"subject": "off_reeve", "office": "off_reeve", "to": "p_mid"}))
    monkeypatch.setattr(Q, "ENDINGS", {"none_such": R.EndingRow(False, ("post", "Pope"), "Valorsmark",
                                                                "a test fixture")})
    assert Q._ending_edges(w, Q.ENDINGS["none_such"]) == () and Q.endings_reached(w) == []


# ======================================================================================
# (c) A READ: THE QUERY AND THE STEP MOVE NOTHING
# ======================================================================================

def _reached_world(monkeypatch):
    monkeypatch.setattr(Q, "ENDINGS", REEVE_ROW)
    w, d = _gov_world()
    w.add_tenure(Tenure("t_mid_crown", "p_mid", CROWN, "commit", 0))
    _fold(w, d, Act(id="in27_cf", actor="p_king", verb="confer", via="off_crown",
                    payload={"subject": "off_reeve", "office": "off_reeve", "to": "p_mid"}))
    return w


def _state(w):
    return w.content_hash(), len(w.log), list(w.writes)


def test_in27_the_query_and_the_season_step_write_nothing(monkeypatch):
    """Called on a world that HAS reached an ending (so the Query does its whole walk), the Query moves
    no hash, log or write; and a season whose step reports that ending leaves the world byte-equal to
    the same season with the Query not called."""
    w = _reached_world(monkeypatch)
    before = _state(w)
    assert Q.endings_reached(w), "fixture: the Query must have something to report"
    assert _state(w) == before, "calling the Query moved the world"
    kw = dict(contest_max_depth=w.fixtures.get("contest_max_depth"))

    called = SeasonDriver(w).season(P.NOCHOOSE, question=None, **kw)
    assert [r.ending for r in called["endings"]] == ["crowned_reeve"], called["endings"]

    other = _reached_world(monkeypatch)
    monkeypatch.setattr(Q, "endings_reached", lambda _w: [])
    skipped = SeasonDriver(other).season(P.NOCHOOSE, question=None, **kw)
    assert skipped["endings"] == []
    assert _state(w) == _state(other), "the ending step moved the season"
    assert {k: v for k, v in called.items() if k != "endings"} == \
        {k: v for k, v in skipped.items() if k != "endings"}


# ======================================================================================
# (d) THE LOADER REFUSES A MALFORMED ROW, NAMING IT
# ======================================================================================

_GOOD = {"victory": False, "holds": {"post": "King"}, "under": "Church of Solmund", "source": "GD-1"}


def _load(members):
    return R._load_endings(members, R.FACTIONS, R.RUNG_KINDS, R.OFFICE_POSTS)


@pytest.mark.parametrize("row, says", [
    ("not a row", "is not a row"),
    (dict(_GOOD, threshold=3), "unknown key"),
    (dict(_GOOD, victory="yes"), "victory"),
    (dict(_GOOD, holds={"post": "King", "rung_kind": "territory"}), "holds"),
    (dict(_GOOD, holds={"rung_kind": "territory", "settled": False}), "holds"),            # `settled: true` only
    (dict(_GOOD, holds={"rung_kind": "territory", "settled": "yes"}), "holds"),
    (dict(_GOOD, holds={"post": "King", "settled": True}), "holds"),                       # beside `rung_kind` only
    (dict(_GOOD, holds={"rung_kind": "territory", "settled": True, "post": "King"}), "holds"),
    (dict(_GOOD, holds={"settled": True}), "holds"),
    (dict(_GOOD, holds={"seat": "off_king"}), "holds"),
    (dict(_GOOD, holds={"post": "Emperor"}), "no offices.yaml seat carries"),
    (dict(_GOOD, holds={"rung_kind": "continent"}), "not a rung_kinds member"),
    (dict(_GOOD, holds={"post": ["King"]}), "no offices.yaml seat carries"),   # non-scalar, refused by name
    (dict(_GOOD, under="Church"), "under"),
    (dict(_GOOD, under=["Church of Solmund"]), "under"),                        # non-scalar, refused by name
    ({k: v for k, v in _GOOD.items() if k != "source"}, "source"),
])
def test_in27_the_loader_refuses_a_malformed_ending_row_naming_it(row, says):
    assert _load({"ok": _GOOD})["ok"].holds == ("post", "King"), "control: the good row loads"
    with pytest.raises(Unspecified) as e:
        _load({"ok": _GOOD, "bad_row": row})
    assert "'bad_row'" in str(e.value) and says in str(e.value), str(e.value)


def test_in27_the_loader_admits_settled_true_beside_rung_kind():
    """The control of the refusals above: the optional key is admitted where it may stand."""
    row = _load({"ok": dict(_GOOD, holds={"rung_kind": "territory", "settled": True})})["ok"]
    assert row.holds == ("rung_kind", "territory") and row.settled is True, row
    assert _load({"ok": dict(_GOOD, holds={"rung_kind": "territory"})})["ok"].settled is False


def test_in27_the_loader_refuses_a_second_victory_row():
    """GD-1: *the sole victory condition*. The shipped roster carries exactly one."""
    assert [n for n, r in R.ENDINGS.items() if r.victory] == ["peninsular_sovereignty"]
    with pytest.raises(Unspecified, match="victory"):
        _load({"a": dict(_GOOD, victory=True), "b": dict(_GOOD, victory=True)})


# ======================================================================================
# (e) THE STEP EXECUTES IN A REAL SEASON, AND THE BUILT REALM REACHES NOTHING
# ======================================================================================

def test_in27_two_seasons_of_the_built_realm_run_the_step_and_report_no_ending(monkeypatch):
    """`season()` on `build_realm(0)`, twice: the Query is CALLED (spied, once per season, on this world)
    and its answer is that season's reported `endings`, `[]`. (The seasons' hashes are `_realm_goldens.py`'s; this
    test pins none.)"""
    real, calls = Q.endings_reached, []

    def spy(w):
        got = real(w)
        calls.append((w, got))
        return got
    monkeypatch.setattr(Q, "endings_reached", spy)
    assert DRV.world_q is Q, "the driver reads a different module than the one spied"
    w = build_realm(0)
    # `harness/populated.py::run`'s chooser, the one the pinned hashes are taken under.
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                      draw=draw_factory(w.world_seed, lambda: w.tick))
    d = SeasonDriver(w)
    checked = 0
    for s in (1, 2):
        out = d.season(ch, question=None,
                       contest_max_depth=w.fixtures.get("contest_max_depth"))
        assert len(calls) == s and calls[-1][0] is w, calls
        assert "endings" in out and out["endings"] == [] and calls[-1][1] is out["endings"], out.get("endings")
        checked += 1
    assert checked == 2


def test_in27_a_selector_the_query_cannot_enumerate_is_refused_not_read_as_a_rung_kind():
    """`ENDING_SELECTORS` has two members and `_ending_edges` a branch for each; a third that passed the loader
    would once have fallen into the `rung_kind` branch silently. The trip-wire names it."""
    from types import SimpleNamespace
    from engine.season.gaps import Forbidden
    from engine.season.queries import world_q
    w = build_realm(0, 5)
    with pytest.raises(Forbidden, match="no enumerator"):
        world_q._ending_edges(w, SimpleNamespace(holds=("bogus", "x"), under=R.ENDING_ANY_ONE))
