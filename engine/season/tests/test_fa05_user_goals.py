"""v9 FA-05 (`workplans/valoria_master_workplan_v9_part7.md`; ED-FA-0039; ED-IN-0293 (8), (9)) -- THE GOALS
THE USER STATED, AND THE CROWN GOAL THEY DERIVE FROM: the first rows of `engine/season/goals.yaml`.

What each test proves, and the failure it can observe. The rows are CONTENT; the mechanism (loader, seeding,
referents) is IN-66..IN-69's and is not tested here again.

  (a) the shipped rows load, seed and count (7 Propositions, 2 orientations), every `source:` carries its
      provenance, and the rows the user spoke to quote the user (the reader's-discipline half of the entry,
      checked for the string being present, not for being right).
  (b) DELETE ONE ROW AND ITS COMMITS VANISH: the same file minus a leaf row builds a realm whose census loses
      exactly that row's commits and whose Proposition is gone -- the rows are what the commits come from.
  (c) AX-2: an Inquisitor whose OWN ledger holds no Einhir-engaging deed forms no heresy question, whatever the
      world holds; with one believed deed it forms one naming the doer. The same for a Riskbreaker and
      corruption (`terms.distorted`).
  (d) the Loewenritter rows derive from the Crown row by `influences` in the DATA, and every Loewenritter
      member then holds the Crown goal too -- the entry's falsifier (it was red until `seed_goals` applied
      `influences`; the cross-faction mutation is `test_in68_goal_seeding.py`'s).
  (e) the Riskbreakers commit to their three goals and not to the throne-security goal they `establish` over;
      the royal-safety goal names the four Royal Family holders.
  (f) the Restoration Movement's -1 goal writes stance rows toward the two capturing seats' holders, each the
      creed's own call (`cast.stance_from_loyalty`) negated.
"""
from __future__ import annotations

import pytest
import yaml

from ..data import cast, files, goals
from ..data.verbs import DEED_KINDS
from ..harness import populated as P
from ..queries import world_q
from ..state.carriers import Claim

CROWN = "goal_crown_peninsular_sovereignty"
LOW_ORIENT = "goal_lowenritter_military_security"
LOW_THRONE = "goal_lowenritter_throne_security"
RB_SAFE = "goal_riskbreakers_royal_safety"
RB_THREAT = "goal_riskbreakers_prevent_threats"
RB_CORRUPT = "goal_riskbreakers_prevent_corruption"
INQ = "goal_inquisitors_find_heresy"
RES_ORIENT = "goal_restoration_einhir_revival"
RES_EVADE = "goal_restoration_evade_capture"
ALL = {CROWN, LOW_ORIENT, LOW_THRONE, RB_SAFE, RB_THREAT, RB_CORRUPT, INQ, RES_ORIENT, RES_EVADE}
ORIENTATIONS = {LOW_ORIENT, RES_ORIENT}

ROYAL = {"p_npc_020", "p_npc_032", "p_npc_031", "p_npc_030"}    # off_king, _widow_regent, _heir, _princess
CAPTURERS = {"p_npc_038", "p_npc_004"}                          # off_cardinal_justice, off_senior_inquisitor
RISKBREAKERS = {"p_npc_005", "p_npc_080"}
INQUISITORS = {"p_npc_004", "p_npc_038"}                        # the Cardinal of Justice's body's two seats


def _shipped_doc() -> dict:
    return yaml.safe_load(files.GOALS_YAML.read_text(encoding="utf-8"))


def _realm(monkeypatch, tmp_path, rows, **kw):
    """`build_realm(0)` over `rows` planted through the loader's patch point."""
    path = tmp_path / "goals.yaml"
    path.write_text(yaml.safe_dump({"goals": list(rows)}, allow_unicode=True), encoding="utf-8")
    monkeypatch.setattr(goals, "GOALS_YAML", path)
    monkeypatch.setattr(goals, "_CACHE", None)
    return P.build_realm(0, **kw)


def _committed(w, gid) -> set:
    return {t.subject for t in w.tenures if t.kind == "commit" and t.object == gid and t.live}


@pytest.fixture(scope="module")
def shipped():
    """The shipped file's realm, read-only."""
    return P.build_realm(0)


# ---------------------------------------------------------------------------------------------------
# (a) the rows load and seed
# ---------------------------------------------------------------------------------------------------

def test_fa05_the_rows_load_seed_and_carry_their_provenance(shipped):
    rows = goals.goals()
    assert {g.id for g in rows} == ALL and len(rows) == 9
    c = P.census(shipped)
    assert (c["goals"], c["goal_orientation"], c["goal_dropped"]) == (7, 2, 0)
    assert c["goal_commits"] > 0 and c["goal_stance_rows"] > 0
    for g in rows:
        assert g.source.strip() and g.pursuits and g.text.strip(), g.id
        assert (g.id in shipped.propositions) == (g.id not in ORIENTATIONS), g.id
    byid = {g.id: g for g in rows}
    # the user's own words, quoted in the rows that rest on them (ED-IN-0293 rows 3-4)
    for gid in (RB_SAFE, RB_THREAT, RB_CORRUPT):
        assert "riskbreaker goal is to ensure safety of royal family monarch as well as prevent corruption " \
               "and threats" in " ".join(byid[gid].source.split()), gid
    for gid in (LOW_ORIENT, LOW_THRONE):
        assert "lowenritter is to have military security and stability" in " ".join(byid[gid].source.split()), gid
    # the Crown's row names the extract and says it is intent; the readings are tagged
    assert "ASSUMPTION" in byid[CROWN].source and "intent" in byid[CROWN].source
    for gid in (LOW_THRONE, INQ, RES_EVADE, RB_CORRUPT):
        assert "ASSUMPTION" in byid[gid].source, gid
    # the Loewenritter rows derive from the Crown row by `influences`; the Riskbreakers from throne security
    for gid in (LOW_ORIENT, LOW_THRONE):
        assert (byid[gid].derives_from, byid[gid].derives_kind) == (CROWN, "influences"), gid
    for gid in (RB_SAFE, RB_THREAT, RB_CORRUPT):
        assert (byid[gid].derives_from, byid[gid].derives_kind) == (LOW_THRONE, "establishes"), gid
    # the deed kinds named as corruption are the registry's, not the plan text's
    assert set(byid[RB_CORRUPT].object["kinds"]) <= DEED_KINDS


# ---------------------------------------------------------------------------------------------------
# (b) delete one row and its commits vanish
# ---------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("gone, held_by", [(INQ, INQUISITORS), (RES_EVADE, None)])
def test_fa05_deleting_a_row_removes_its_proposition_and_its_commits(monkeypatch, tmp_path, shipped, gone, held_by):
    full = P.census(shipped)
    assert gone in shipped.propositions and (held_by is None or _committed(shipped, gone) == held_by), \
        "control: the shipped realm holds the row and its commits"
    n_commits = len(_committed(shipped, gone))
    assert n_commits > 0
    rows = [r for r in _shipped_doc()["goals"] if r["id"] != gone]
    assert len(rows) == 8
    w = _realm(monkeypatch, tmp_path, rows)
    assert gone not in w.propositions and _committed(w, gone) == set()
    c = P.census(w)
    assert c["goals"] == full["goals"] - 1
    assert c["goal_commits"] == full["goal_commits"] - n_commits, "exactly the deleted row's commits vanish"
    assert w.content_hash() != shipped.content_hash(), "the hash observes the row"


# ---------------------------------------------------------------------------------------------------
# (c) AX-2: a deed goal reads the holder's own ledger
# ---------------------------------------------------------------------------------------------------

def _need_referents(w, p, gid):
    return {q.about: q.referents for q in world_q.questions_for(w, p) if q.source == "need"}.get(gid)


def _believed(doer, kind, holder):
    """A firsthand deed claim in the holder's ledger (an unpaired kind's subject IS its doer)."""
    return Claim(f"c_fa05_{kind}", holder, doer, kind, True, 0, "firsthand", 100, "own", 0)


@pytest.mark.parametrize("holder, gid, kind", [
    ("p_npc_004", INQ, "commitment.made"),          # `commit` engages `einhir_restoration` (0.7)
    ("p_npc_005", RB_CORRUPT, "terms.distorted"),   # `construe`
])
def test_fa05_a_deed_goal_forms_no_question_without_a_believed_deed(holder, gid, kind):
    w = P.build_realm(0)
    p = w.persons[holder]
    assert gid in {t.object for t in p.tenures if t.kind == "commit" and t.live}, "control: he holds the goal"
    assert not [c for c in p.ledger if c.predicate == kind]
    assert _need_referents(w, p, gid) is None, "no believed deed: no referent, no question (AX-2)"
    # the deed happened in the world and the log says so, but the holder was not told: still nothing
    assert _need_referents(w, p, gid) is None
    p.ledger.append(_believed("p_npc_050", kind, holder))
    assert _need_referents(w, p, gid) == ("p_npc_050",), "one believed deed names its doer"


# ---------------------------------------------------------------------------------------------------
# (d) `influences` is applied: a Loewenritter member holds the Crown goal too
# ---------------------------------------------------------------------------------------------------

def _without_crown(w) -> set:
    return {pid for pid in _committed(w, LOW_THRONE) if pid not in _committed(w, CROWN)}


def test_fa05_the_lowenritter_rows_derive_from_the_crown_row_by_influences_in_the_data():
    byid = {g.id: g for g in goals.goals()}
    for gid in (LOW_ORIENT, LOW_THRONE):
        assert (byid[gid].derives_from, byid[gid].derives_kind) == (CROWN, "influences"), gid


def test_fa05_every_lowenritter_member_holds_the_crown_goal_too(shipped):
    mem = _committed(shipped, LOW_THRONE)
    assert len(mem) >= 2, "control: the goal has members (the Grand Master and a rank-and-file knight)"
    assert _without_crown(shipped) == set(), "influences not applied: a member holds no Crown commit"
    assert _committed(shipped, CROWN) > mem, "and the Crown goal keeps its own members"


# ---------------------------------------------------------------------------------------------------
# (e) the Riskbreakers
# ---------------------------------------------------------------------------------------------------

def test_fa05_the_riskbreakers_hold_their_three_goals_and_not_the_throne_security_they_establish_over(shipped):
    for gid in (RB_SAFE, RB_THREAT, RB_CORRUPT):
        assert _committed(shipped, gid) == RISKBREAKERS, gid
    assert not RISKBREAKERS & _committed(shipped, LOW_THRONE), "`establishes` replaces the parent for the body"
    for pid in RISKBREAKERS:
        p = shipped.persons[pid]
        assert world_q.goal_referents(shipped, p, shipped.propositions[RB_SAFE]) and \
            set(world_q.goal_referents(shipped, p, shipped.propositions[RB_SAFE])) == ROYAL
        # EXIT reading (seed 0): the question is formed and names the four royal holders. WHICH need
        # question a Riskbreaker answers first is IN-69's salience, not this content's, so it is not pinned:
        # NPC-005 answers the Crown goal (naming the King) first, NPC-080 the creed (naming the Grand Master).
        assert _need_referents(shipped, p, RB_SAFE) is not None
        assert set(_need_referents(shipped, p, RB_SAFE)) == ROYAL


# ---------------------------------------------------------------------------------------------------
# (f) the Restoration Movement's -1
# ---------------------------------------------------------------------------------------------------

def test_fa05_the_restoration_goal_writes_negated_stance_toward_the_capturers(shipped):
    members = _committed(shipped, RES_EVADE)
    assert members, "control: the Movement's members commit"
    checked = 0
    for pid in sorted(members):
        row = cast.row("NPC-" + pid.rsplit("_", 1)[1])
        st = cast.stance_from_loyalty(cast.loyalty(row, "Restoration Movement")) if row else None
        if st is None:
            continue
        for ref in CAPTURERS:
            assert (ref, -1 * st[0], st[1]) in shipped.persons[pid].stance, (pid, ref)
            checked += 1
    assert checked >= 2, "the loop asserted"
    assert RES_ORIENT not in shipped.propositions and not _committed(shipped, RES_ORIENT), "orientation mints nothing"
