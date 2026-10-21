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
from engine.season.harness import populated as POP
from engine.season.harness import probes as P
from engine.season.loop import driver as DRV
from engine.season.decision import make_chooser
from engine.season.loop.driver import SeasonDriver, mint_token, resolvable_verbs
from engine.season.queries import world_q as Q
from engine.season.state.carriers import Act, Event, Tenure
from engine.season.state.ids import H, ROOT, draw_factory

from .test_g3_not_yours import _gov_world, _hold
from .test_governance_build import _establish, _establish_world, _founding, _seat_reeve
from .test_season_weather import BASE_HASHES

CHURCH = R.faction_prop_id("Church of Solmund")
CROWN = R.faction_prop_id("Crown")
#: A row naming the governance world's unheld appointed seat (`off_reeve`, post `Reeve`), planted where
#: the Query reads its rows: the shipped rows name a King, whose seat no act can confer (its conferral is
#: hereditary, `offices.yaml: off_king`).
REEVE_ROW = {"crowned_reeve": R.EndingRow(False, ("post", "Reeve"), "Crown", "a test fixture")}


def _fold(w, d, *acts):
    """Fold hand-built acts through the shipped `SeasonDriver.resolve` and log what it emits, as
    `season()` does (S19.5 -- one log)."""
    out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts),
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return [e.kind for e in out]


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
    w = POP.build_realm(0)
    d = SeasonDriver(w)
    off, king = _king(w)
    assert Q.faction_holding(w, king) == CROWN and CHURCH in w.propositions, "fixture"
    assert Q.endings_reached(w) == [], "the built realm reached an ending with no act"
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
    w = POP.build_realm(0)
    last = _all_but_one_under_the_crown(w)
    row = _row("peninsular_sovereignty")
    assert w.rungs["terr_T16"].kind == "territory" and "terr_T16" not in _realm_territories(w), "fixture"
    assert Q.governing_hold(w, "terr_T16") is None, "fixture: the foreign root is held by nobody"
    assert not Q._ending_edges(w, row) and Q.endings_reached(w) == [], "fixture: one holder is under none"
    kinds = _fold(w, SeasonDriver(w), Act(id="in27_swear", actor=last, verb="commit",
                                          payload={"subject": CROWN}))
    assert kinds == ["commitment.made"], kinds
    (got,) = Q.endings_reached(w)
    assert got.ending == "peninsular_sovereignty" and got.victory is True, got
    assert got.acts == ("in27_swear",) and len(got.holds) > 1, got
    # THE REALM'S TERRITORIES ARE SELECTED, AND THE FOREIGN ROOT IS NOT (an unheld selected rung
    # would have made the condition false and the report empty)
    selected = {t.object for t in Q._ending_edges(w, row) if t.kind == "hold"}
    assert "terr_T16" not in selected and selected == set(_realm_territories(w)), selected

    control = POP.build_realm(0)
    last = _all_but_one_under_the_crown(control)
    control.add_tenure(Tenure("t_in27_last_crown", last, CROWN, "commit", 0))
    assert Q._ending_edges(control, row), "control: the planted condition does not hold"
    assert Q.endings_reached(control) == [], "GD-1's row fired with no person's act among its antecedents"


def test_in27_one_faction_is_not_met_by_a_holder_who_commits_elsewhere():
    """KILLS `want = set(facs)` (A-F2 ii): with every realm territory a Crown man's but one, that last
    holder's own `commit` goes to the CHURCH. The holders now cohere under two factions, so `one_faction`
    fails and nothing is reported, though an act opened an edge the mutated condition would read."""
    w = POP.build_realm(0)
    last = _all_but_one_under_the_crown(w)
    kinds = _fold(w, SeasonDriver(w), Act(id="in27_stray", actor=last, verb="commit",
                                          payload={"subject": CHURCH}))
    assert kinds == ["commitment.made"] and Q.faction_holding(w, last) == CHURCH, kinds
    assert not Q._ending_edges(w, _row("peninsular_sovereignty"))
    assert Q.endings_reached(w) == [], "holders under two factions were read as under one"


def test_in27_a_king_who_commits_to_a_third_faction_is_no_theocracy():
    """KILLS deleting `set(facs) != want` (A-F2 i): the built realm's King releases the Crown and commits
    by act to a rostered faction that is neither the Crown nor the Church. He coheres under a faction,
    his act opened the edge, and `theocracy` is still not reached: his faction is not the row's."""
    w = POP.build_realm(0)
    _, king = _king(w)
    third = next(f for f in sorted(R.FACTION_BY_PROP) if f in w.propositions and f not in (CROWN, CHURCH))
    kinds = _fold(w, SeasonDriver(w),
                  Act(id="in27_release3", actor=king, verb="release", payload={"subject": CROWN}),
                  Act(id="in27_commit3", actor=king, verb="commit", payload={"subject": third}))
    assert "commitment.made" in kinds and Q.faction_holding(w, king) == third, kinds
    assert "theocracy" not in [r.ending for r in Q.endings_reached(w)], "a King of a third faction"


def test_in27_a_redundant_commit_by_act_is_not_credited():
    """MAJOR 2's falsifier. Arm 1 of the control below (the King planted into the Church by construction:
    the condition true, nothing reported), then the King folds a `commit` to the Church he already
    coheres under. `commit` needs only the Proposition and `_eff_commit` mints a fresh edge, so the act
    executes and changes nothing the condition reads -- it must not be reported as the antecedent."""
    w = POP.build_realm(0)
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
    w = POP.build_realm(0)
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
    w.log.append(Event("ev_in27_root", "tenure.opened", [P.about("t_reeve_planted")], [ROOT], w.tick))
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
    monkeypatch.setattr(Q, "ENDINGS", {"none_such": R.EndingRow(False, ("post", "Pope"), "Crown",
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

    called = SeasonDriver(w).season(P.NOCHOOSE, question=None, subsistence=P.SUBSIST, **kw)
    assert [r.ending for r in called["endings"]] == ["crowned_reeve"], called["endings"]

    other = _reached_world(monkeypatch)
    monkeypatch.setattr(Q, "endings_reached", lambda _w: [])
    skipped = SeasonDriver(other).season(P.NOCHOOSE, question=None, subsistence=P.SUBSIST, **kw)
    assert skipped["endings"] == []
    assert _state(w) == _state(other), "the ending step moved the season"
    assert {k: v for k, v in called.items() if k != "endings"} == \
        {k: v for k, v in skipped.items() if k != "endings"}


# ======================================================================================
# (d) THE LOADER REFUSES A MALFORMED ROW, NAMING IT
# ======================================================================================

_GOOD = {"victory": False, "holds": {"post": "King"}, "under": "Church of Solmund", "source": "GD-1"}


def _load(members):
    return R._load_endings(members, R.FACTIONS, R.RUNG_KINDS,
                           frozenset(s.get("post") for s in R.OFFICES_SEATS))


@pytest.mark.parametrize("row, says", [
    ("not a row", "is not a row"),
    (dict(_GOOD, threshold=3), "unknown key"),
    (dict(_GOOD, victory="yes"), "victory"),
    (dict(_GOOD, holds={"post": "King", "rung_kind": "territory"}), "holds"),
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
    and its answer is that season's reported `endings`, `[]`; each season lands on the hash
    `test_season_weather.py` pins for it (`BASE_HASHES[1]`, `BASE_HASHES[2]`)."""
    real, calls = Q.endings_reached, []

    def spy(w):
        got = real(w)
        calls.append((w, got))
        return got
    monkeypatch.setattr(Q, "endings_reached", spy)
    assert DRV.world_q is Q, "the driver reads a different module than the one spied"
    w = POP.build_realm(0)
    # `harness/populated.py::run`'s chooser, the one the pinned hashes are taken under.
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                      draw=draw_factory(w.world_seed, lambda: w.tick))
    d = SeasonDriver(w)
    checked = 0
    for s in (1, 2):
        out = d.season(ch, question=None, subsistence=P.SUBSIST,
                       contest_max_depth=w.fixtures.get("contest_max_depth"))
        assert len(calls) == s and calls[-1][0] is w, calls
        assert "endings" in out and out["endings"] == [] and calls[-1][1] is out["endings"], out.get("endings")
        assert out["hash"] == BASE_HASHES[s], f"the ending step moved the pinned {s}-season hash"
        checked += 1
    assert checked == 2
