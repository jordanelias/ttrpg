"""v9 IN-67 (`workplans/valoria_master_workplan_v9_part5.md`, A-31; ED-IN-0293 (8)) -- A GOAL'S
REFERENTS, READ WHEN THE QUESTION FORMS: `world_q.goal_referents`, the one owner Q4 asks instead of
`(prop.subject,)` (and `attention_key`'s tier 0 with it), and `person_q.deed_doers`, the person-side
read of a `deed_doers` goal over the holder's OWN ledger.

Hand-built goals files are planted through `goals.GOALS_YAML` and the loader's `_CACHE`, as
`test_in66_goals_loader.py` does. What each test proves, and the failure it can observe:

  (a) a Proposition no goal names reads `(subject,)` as before (the shipped file is empty: the hash
      EQUAL claim's own control); `person` and `rung` read it too; `orientation` and a vacant seat
      read nothing.
  (b) `seat_holders` FOLLOWS THE THRONE through a hand-built change of hold -- in the referents, the
      `need` question's referents and `attention_key`'s tier 0 (a claim about the holder ranks 0, a
      claim about the seat id does not). Tier 0 reading `.subject` reddens the last.
  (c) `deed_doers engaging` yields X to a holder whose OWN ledger holds X's deed claim and nothing to
      one whose ledger does not though X did it and the log says so (AX-2: a reader of `w.log`
      reddens it -- MUTATION run both as a test and against the source).
  (d) a `PAIRED_KINDS` claim names its DOER through `deed_doer` in every form, never its subject:
      `kinds: [person.died]` names the killer and never the victim; an unpaired claim names no one.
      MUTATION (run): the pairing replaced by the claim's subject reddens it.
  (e) the holder is never his own referent: not by his own act (`Claim.doer`), nor by a told copy.
  (f) no referent, no question; an `against` cycle terminates.
"""
from __future__ import annotations

import dataclasses

import pytest
import yaml

from ..data import affiliations as AFF
from ..data import goals
from ..data.rosters import SEEN_PREDICATE
from ..epistemic import Seen
from ..queries import person_q as PQ
from ..queries import world_q
from ..state.carriers import Claim, Event, Person, Proposition, StateChange, Tenure
from ..state.ids import ROOT
from ..state.world import World

SEAT = "off_king"
FAC = {"faction": "Löwenritter"}
STRATUM = sorted(PQ._KIND_STRATA["person.died"])[0]


def _row(gid, obj, org=FAC):
    return {"id": gid, "org": org, "text": f"{gid}, as a predicate", "object": obj,
            "pursuits": {"stability": 1}, "source": "test_in67"}


def _plant(monkeypatch, tmp_path, *rows):
    """Load a hand-built goals file through the loader's own patch point."""
    path = tmp_path / "goals.yaml"
    path.write_text(yaml.safe_dump({"goals": list(rows)}, allow_unicode=True), encoding="utf-8")
    monkeypatch.setattr(goals, "GOALS_YAML", path)
    monkeypatch.setattr(goals, "_CACHE", None)
    return goals.goals()


def _deed(cid, subject, kind, n=0, **kw):
    return Claim(cid, "p_obs", subject, kind, True, 0, "firsthand", 100, "own", 0, **kw)


def _seen(cid, subject, who):
    return Claim(cid, "p_obs", subject, SEEN_PREDICATE, Seen(stratum=STRATUM, marks=(), who=who),
                 0, "firsthand", 100, "own", 0)


def _death(victim, killer, n=0):
    """The pair WITNESS deposits for a kill: the patient-subject deed claim and the sighting."""
    return [_deed(f"c_d{n}_{victim}", victim, "person.died"), _seen(f"c_s{n}_{victim}", victim, killer)]


def _world(*goal_ids, obs_ledger=()):
    """An observer committed to an OUGHT per goal id (the Proposition's id IS the goal's id), and
    the persons the tests name."""
    w = World(0)
    obs = Person("p_obs", "p_obs")
    for i, gid in enumerate(goal_ids):
        w.propositions[gid] = Proposition(gid, "OUGHT", "subj_" + gid, f"{gid} ought", True, 0)
        obs.tenures.append(Tenure(f"t_obs_{i}", "p_obs", gid, "commit", 0))
    obs.ledger = list(obs_ledger)
    w.persons["p_obs"] = obs
    for pid in ("p_a", "p_b"):
        w.persons[pid] = Person(pid, pid)
    return w, obs


def _referents(w, gid):
    return world_q.goal_referents(w, w.persons["p_obs"], w.propositions[gid])


def _need(w):
    return {q.about: q.referents for q in world_q.questions_for(w, w.persons["p_obs"])
            if q.source == "need"}


def _throne(w, holder):
    t = Tenure(f"t_hold_{holder}", holder, SEAT, "hold", 0)
    w.persons[holder].tenures.append(t)
    return t


# ---------------------------------------------------------------------------------------------------
# (a) the unchanged cases and the kinds that read the subject or nothing
# ---------------------------------------------------------------------------------------------------

def test_in67_a_proposition_no_goal_names_reads_its_subject_as_today(monkeypatch, tmp_path):
    w, _ = _world("o_plain")
    assert goals.goals() == (), "control: the shipped goals file is empty"
    assert _referents(w, "o_plain") == ("subj_o_plain",)
    assert _need(w) == {"o_plain": ("subj_o_plain",)}, "Q4 asks goal_referents and keeps its question"
    _plant(monkeypatch, tmp_path, _row("g_other", {"kind": "rung", "rung": "terr_T9"}))
    assert goals.goal("g_other") is not None and goals.goal("o_plain") is None
    assert _referents(w, "o_plain") == ("subj_o_plain",), "a goals file that does not name it moves nothing"


def test_in67_person_and_rung_read_the_subject_and_orientation_nothing(monkeypatch, tmp_path):
    _plant(monkeypatch, tmp_path,
           _row("g_person", {"kind": "person", "case": "NPC-020"}),
           _row("g_rung", {"kind": "rung", "rung": "terr_T9"}),
           _row("g_orient", {"kind": "orientation"}))
    w, _ = _world("g_person", "g_rung", "g_orient")
    assert _referents(w, "g_person") == ("subj_g_person",)
    assert _referents(w, "g_rung") == ("subj_g_rung",)
    assert _referents(w, "g_orient") == (), "a pure condition has no referent"
    assert set(_need(w)) == {"g_person", "g_rung"}, "and so forms no question"


# ---------------------------------------------------------------------------------------------------
# (b) seat_holders follows the throne
# ---------------------------------------------------------------------------------------------------

def test_in67_seat_holders_follow_the_throne_through_a_change_of_hold(monkeypatch, tmp_path):
    _plant(monkeypatch, tmp_path, _row("g_king", {"kind": "seat_holders", "seats": [SEAT]}))
    w, obs = _world("g_king")
    for pid in ("p_a", "p_b"):                       # a claim about either reaches the observer
        obs.tenures.append(Tenure(f"t_obl_{pid}", "p_obs", pid, "oblige", 0))
    obs.tenures.append(Tenure("t_obl_seat", "p_obs", SEAT, "oblige", 0))
    obs.ledger = [_deed("c_a", "p_a", "bond.formed"), _deed("c_b", "p_b", "bond.formed"),
                  _deed("c_s", SEAT, "bond.formed")]
    checked = []

    def tiers():
        key = world_q.attention_key(w, obs)
        qs = {q.id: q for q in world_q.questions_for(w, obs)}
        return {c: key(qs[f"q:claim:c_{c}"])[0] for c in "abs"}

    assert _referents(w, "g_king") == () and _need(w) == {}, "a vacant throne names nobody"
    assert tiers() == {"a": 1, "b": 1, "s": 1}
    checked.append("vacant")
    first = _throne(w, "p_a")
    assert _referents(w, "g_king") == ("p_a",) and _need(w) == {"g_king": ("p_a",)}
    assert tiers() == {"a": 0, "b": 1, "s": 1}, "tier 0 is the HOLDER's claim, not the seat id's"
    checked.append("a")
    first.until = w.tick                              # the hold ends ...
    _throne(w, "p_b")                                 # ... and passes
    assert _referents(w, "g_king") == ("p_b",) and _need(w) == {"g_king": ("p_b",)}
    assert tiers() == {"a": 1, "b": 0, "s": 1}
    checked.append("b")
    assert checked == ["vacant", "a", "b"]


def test_in67_mutation_tier_0_reading_the_subject_does_not_follow_the_throne(monkeypatch, tmp_path):
    """THE MUTATION, run as a test: `attention_key` reading `.subject` (the pre-IN-67 aims). The
    throne test's tier assertion must go red."""
    _plant(monkeypatch, tmp_path, _row("g_king", {"kind": "seat_holders", "seats": [SEAT]}))
    w, obs = _world("g_king")
    obs.tenures.append(Tenure("t_obl_a", "p_obs", "p_a", "oblige", 0))
    obs.ledger = [_deed("c_a", "p_a", "bond.formed")]
    _throne(w, "p_a")
    key = world_q.attention_key(w, obs)
    q = next(q for q in world_q.questions_for(w, obs) if q.id == "q:claim:c_a")
    assert key(q)[0] == 0, "control: goal_referents puts the holder's claim in tier 0"
    monkeypatch.setattr(world_q, "goal_referents", lambda w_, p_, prop: (prop.subject,))
    assert world_q.attention_key(w, obs)(q)[0] == 1, "the subject reading misses the holder"


# ---------------------------------------------------------------------------------------------------
# (c) deed_doers engaging -- the holder's OWN ledger, and nothing else (AX-2)
# ---------------------------------------------------------------------------------------------------

ENGAGING = {"kind": "deed_doers", "engaging": "einhir_restoration"}


def _two_holders(monkeypatch, tmp_path, obj=ENGAGING):
    """`p_x` committed a deed that engages the affiliation and the LOG says so. One holder's ledger
    holds the claim; the other's does not."""
    _plant(monkeypatch, tmp_path, _row("g_eng", obj))
    knows, _ = _world("g_eng", obs_ledger=[_deed("c_x", "p_x", "commitment.made")])
    ignorant, _ = _world("g_eng")
    for w in (knows, ignorant):
        w.log.append(Event(id="e_x", kind="commitment.made",
                           changes=[StateChange("p_x", "set", "MATTER", "f")],
                           causes=[ROOT], emitted_at=0))
        assert len(w.log) == 1, "control: the log records X's deed in both worlds"
    return knows, ignorant


def test_in67_engaging_names_x_to_the_holder_whose_ledger_holds_his_deed_and_no_one_else(
        monkeypatch, tmp_path):
    knows, ignorant = _two_holders(monkeypatch, tmp_path)
    assert AFF.engagement("commit", "einhir_restoration") != 0, "control: the cell the test rests on"
    assert _referents(knows, "g_eng") == ("p_x",)
    assert _need(knows) == {"g_eng": ("p_x",)}
    assert _referents(ignorant, "g_eng") == ()
    assert _need(ignorant) == {}, "X did it, the log says so, and the holder was never told: no question"


def test_in67_mutation_a_reader_of_the_log_names_x_to_the_ignorant_holder(monkeypatch, tmp_path):
    """THE AX-2 MUTATION, run as a test: `deed_doers` replaced by one that reads `w.log`. The
    assertion above (`() ` for the holder who was not told) must go red."""
    knows, ignorant = _two_holders(monkeypatch, tmp_path)

    def reads_the_log(ledger, spec, holder, against=()):
        return tuple(ch.subject for ev in ignorant.log for ch in ev.changes
                     if ev.kind == "commitment.made")

    monkeypatch.setattr(world_q, "deed_doers", reads_the_log)
    assert _referents(ignorant, "g_eng") == ("p_x",) != ()


def test_in67_engaging_matches_a_kind_by_its_verbs_cell_and_not_a_kind_that_engages_nothing(
        monkeypatch, tmp_path):
    _plant(monkeypatch, tmp_path, _row("g_eng", ENGAGING))
    ledger = [_deed("c_1", "p_x", "commitment.made"),       # `commit`: the shared column's cell
              _deed("c_2", "p_y", "news.told"),             # `tell`: no cell
              _deed("c_3", "p_z", "compliance.withheld")]   # `evade / defy`: a NEGATIVE shared cell
    assert AFF.engagement("tell", "einhir_restoration") == 0, "control: `tell` has no cell"
    assert AFF.engagement("evade / defy", "einhir_restoration") < 0, "control: a negative cell"
    got = PQ.deed_doers(ledger, ENGAGING, "p_obs")
    assert got == ("p_x", "p_z"), "either sign engages; a verb with no cell does not"


def test_in67_a_paired_kind_engages_only_where_every_row_emitting_it_does(monkeypatch):
    spec = {"kind": "deed_doers", "engaging": "einhir_restoration"}
    ledger = _death("p_v", "p_k")
    assert PQ.deed_doers(ledger, spec, "p_obs") == (), "control: `accept`/`fight` carry no cell"
    cells = {k: dict(v) for k, v in AFF.ENGAGEMENT.items()}
    cells["einhir_restoration"] = {"fight": 1.0}
    monkeypatch.setattr(AFF, "ENGAGEMENT", cells)
    assert PQ.deed_doers(ledger, spec, "p_obs") == (), "one emitter engaging is not all of them"
    cells["einhir_restoration"] = {"fight": 1.0, "accept": 1.0}
    assert PQ.deed_doers(ledger, spec, "p_obs") == ("p_k",), "all engage: the DOER, not the patient"


# ---------------------------------------------------------------------------------------------------
# (d) a paired claim names its doer through the pairing, in every form
# ---------------------------------------------------------------------------------------------------

def test_in67_kinds_person_died_names_the_killer_and_never_the_victim():
    spec = {"kind": "deed_doers", "kinds": ["person.died"]}
    ledger = _death("p_v", "p_k") + [_deed("c_bf", "p_z", "bond.formed")]
    assert PQ.deed_doers(ledger, spec, "p_obs") == ("p_k",)
    assert PQ.deed_doers(ledger, {"kind": "deed_doers", "kinds": ["bond.formed"]}, "p_obs") == ("p_z",), \
        "an unpaired kind reads its subject as its doer"
    # the claim with no sighting, one whose sighting withheld the actor, and a told copy: no doer
    assert PQ.deed_doers([_deed("c_1", "p_v", "person.died")], spec, "p_obs") == ()
    assert PQ.deed_doers([_deed("c_1", "p_v", "person.died"), _seen("c_2", "p_v", None)],
                         spec, "p_obs") == ()
    told = dataclasses.replace(_death("p_v", "p_k")[0], chain=("p_t",))
    assert PQ.deed_doers([told, _death("p_v", "p_k")[1]], spec, "p_obs") == ()


def test_in67_mutation_the_victim_by_subject_is_named_a_doer(monkeypatch):
    """THE MUTATION, run as a test: the pairing replaced by the claim's subject. `kinds:
    [person.died]` must then name the victim -- the failure the assertion above excludes."""
    spec = {"kind": "deed_doers", "kinds": ["person.died"]}
    ledger = _death("p_v", "p_k")
    assert PQ.deed_doers(ledger, spec, "p_obs") == ("p_k",), "control"
    monkeypatch.setattr(PQ, "deed_doer", lambda c, seen: c.subject)
    assert PQ.deed_doers(ledger, spec, "p_obs") == ("p_v",)


def test_in67_against_names_the_doers_of_deeds_done_to_a_goals_referents(monkeypatch, tmp_path):
    _plant(monkeypatch, tmp_path,
           _row("g_king", {"kind": "seat_holders", "seats": [SEAT]}),
           _row("g_threat", {"kind": "deed_doers", "against": "g_king"}))
    w, obs = _world("g_king", "g_threat",
                    obs_ledger=_death("p_a", "p_k1", 1) + _death("p_b", "p_k2", 2)
                    + _death("p_w", "p_k3", 3) + [_deed("c_bf", "p_z", "bond.formed")])
    assert _referents(w, "g_threat") == (), "a vacant throne: no one to be against"
    first = _throne(w, "p_a")
    assert _referents(w, "g_threat") == ("p_k1",), "the killer of the king, not the king, a stranger's killer or a bonder"
    first.until = w.tick
    _throne(w, "p_b")
    assert _referents(w, "g_threat") == ("p_k2",), "and it follows the throne"


# ---------------------------------------------------------------------------------------------------
# (e) never the holder himself
# ---------------------------------------------------------------------------------------------------

def test_in67_the_holders_own_deed_never_makes_him_a_referent():
    spec = {"kind": "deed_doers", "kinds": ["commitment.made", "person.died"]}
    own_act_on_y = _deed("c_1", "p_y", "commitment.made", doer="p_obs")   # his act, its PATIENT the subject
    told_of_himself = dataclasses.replace(_deed("c_2", "p_obs", "commitment.made"), chain=("p_t",))
    own_kill = [dataclasses.replace(c, doer="p_obs") for c in _death("p_v", "p_obs")]
    killed_by_himself_unstamped = _death("p_v2", "p_obs", 9)
    ledger = [own_act_on_y, told_of_himself, *own_kill, *killed_by_himself_unstamped,
              _deed("c_3", "p_x", "commitment.made")]
    assert PQ.deed_doers(ledger, spec, "p_obs") == ("p_x",), "only the other's deed names a doer"
    # the control: the same claims for a holder who is not the doer name every doer
    assert PQ.deed_doers(ledger, spec, "p_other") == ("p_y", "p_obs", "p_x")


# ---------------------------------------------------------------------------------------------------
# (f) no referent, no question; a cycle among `against` references terminates
# ---------------------------------------------------------------------------------------------------

def test_in67_an_ambition_with_no_referent_forms_no_question_and_a_referent_forms_it(
        monkeypatch, tmp_path):
    _plant(monkeypatch, tmp_path, _row("g_eng", ENGAGING))
    w, obs = _world("g_eng")
    assert [q for q in world_q.questions_for(w, obs) if q.source == "need"] == []
    obs.ledger.append(_deed("c_x", "p_x", "commitment.made"))
    need = [q for q in world_q.questions_for(w, obs) if q.source == "need"]
    assert [(q.id, q.referents) for q in need] == [("q:need:g_eng", ("p_x",))]


def test_in67_an_against_cycle_terminates_and_names_no_referent(monkeypatch, tmp_path):
    ledger = _death("p_a", "p_k")
    # control: the same `against` read with no cycle resolves
    _plant(monkeypatch, tmp_path,
           _row("g_king", {"kind": "seat_holders", "seats": [SEAT]}),
           _row("g_a", {"kind": "deed_doers", "against": "g_king"}))
    w, _ = _world("g_king", "g_a", obs_ledger=ledger)
    _throne(w, "p_a")
    assert _referents(w, "g_a") == ("p_k",)
    # the cycles: A against B and B against A; a goal against itself; a tail leading into the loop
    _plant(monkeypatch, tmp_path,
           _row("g_a", {"kind": "deed_doers", "against": "g_b"}),
           _row("g_b", {"kind": "deed_doers", "against": "g_a"}),
           _row("g_self", {"kind": "deed_doers", "against": "g_self"}),
           _row("g_tail", {"kind": "deed_doers", "against": "g_a"}))
    w, _ = _world("g_a", "g_b", "g_self", "g_tail", obs_ledger=ledger)
    asked = []
    for gid in ("g_a", "g_b", "g_self", "g_tail"):
        asked.append((gid, _referents(w, gid)))      # a RecursionError here is the failure
    assert asked == [("g_a", ()), ("g_b", ()), ("g_self", ()), ("g_tail", ())]
    assert [q for q in world_q.questions_for(w, w.persons["p_obs"]) if q.source == "need"] == []
