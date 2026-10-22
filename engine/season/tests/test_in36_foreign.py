"""v9 IN-36 (batch B-V): AN EXTERNAL EMPIRE AS PERSONS, AND IN-60's GUARD CONTENT.

THE EXIT (#453/#457, verbatim): *with the cast on, a foreign `march` reaches the mass-battle seam against a
realm settlement through the real chooser, with no hand-built act; off, byte-identical to today.*

  (a) THE CONTROL ARM is the realm before the empire existed: `build_realm(0)` seats no Altonian entity of any
      kind, leaves the three cast rows unplaced exactly as before, and its content hash is the pre-change
      `d3edd90a` (read on the base commit; a hash is not pinned in this file, because a later position that
      moves the default realm would turn a pin into a false alarm - the structural assertions are the guard).
  (b) THE CAST ON: Altonia is in `FACTION_BY_PROP` in BOTH arms (it is a `factions` member), its Proposition,
      members, two seats, holds and goals exist only with `foreign=True`.
  (c) THE BORDER: the foreign root is a `territory` outside every `realm` rung, so `endings_reached`'s victory
      selector and `census`'s `uncontrolled_in_realm` do not count it, even when nobody holds it.
  (d) A FOREIGN MARCH REACHES THE SEAM THROUGH THE REAL CHOOSER: the Katepano is asked a real `Question` whose
      one referent is a realm settlement, the real `make_chooser` forms the act and names `via` itself, and the
      real driver folds it to the mass-battle entry. ⚠ SCOPE, STATED: the chooser here is restricted to
      `march` (`test_march.py::test_a_real_chooser_forms_and_folds_a_march_...`'s own shape), so the test shows
      the empire's march FORMS and FOLDS, not that the unrestricted chooser PICKS it - it does not in a
      measured 2-season probe (`hole_register.yaml` H-233).
  (e) IN-60's GUARD CONTENT: with `guards=True` the throne's and each duchy seat's holder has a sworn cohort
      posted at the exact rung he is present at, the King's heavier than a duke's; an ordinary rung with one
      sworn resident reads 0; end the swearer's `oblige` and the value falls with nothing else written.
"""
from __future__ import annotations


import pytest

from engine.season.data import cast
from engine.season.data.matrix import Step, WriteClass
from engine.season.data.rosters import FACTION_BY_PROP, FACTIONS, FOREIGN_CAST, FOREIGN_SEATS, faction_prop_id
from engine.season.decision.choose import make_chooser
from engine.season.decision.options import opening_set
from engine.season.harness import populated as POP
from engine.season.loop.driver import SeasonDriver, mint_token
from engine.season.queries import world_q
from engine.season.seam.wrappers import mass_battle as wrapper
from engine.season.state.carriers import Question, Sensation, View
from engine.season.state.ids import H, draw_factory

EMPIRE = "Altonia"
FID = faction_prop_id(EMPIRE)
CAST = ("p_npc_011", "p_npc_089", "p_npc_090")           # the three cast rows whose faction cell reads `Altonia`
#: Every id a foreign world adds is spelled with one of these, by the places and seats `foreign_cast` /
#: `foreign_seats` author; the control arm must hold none.
FOREIGN_MARKERS = ("alt_1", "terr_alt", "fac_altonia", "off_katepano", "off_kommerkiarios", "goal_altonia",
                   "goal_katepano", "goal_kommerkiarios")


@pytest.fixture(scope="module")
def control():
    return POP.build_realm(0)


@pytest.fixture(scope="module")
def foreign():
    return POP.build_realm(0, foreign=True)


@pytest.fixture(scope="module")
def guarded():
    return POP.build_realm(0, guards=True)


def _ids(w) -> set:
    return ({*w.rungs, *w.persons, *w.propositions, *w.offices} | {t.id for t in w.tenures}
            | {t.object for t in w.tenures} | {t.subject for t in w.tenures})


# ---------------------------------------------------------------------------------------------- (a) + (b)

def test_the_control_arm_seats_no_altonian_entity_and_leaves_the_cast_rows_unplaced(control):
    mentions = sorted(i for i in _ids(control) if any(m in str(i).lower() for m in FOREIGN_MARKERS))
    assert mentions == [], mentions
    assert len(control.persons) == 83, "the control arm's cast count moved"
    unplaced = dict(control._unplaced_cast)
    assert {c: unplaced.get(c) for c in ("NPC-011", "NPC-089", "NPC-090")} == {
        "NPC-011": "Altonia", "NPC-089": "Altonia", "NPC-090": "Altonia"}, unplaced
    # three in the foreign arm are placed and the other unplaced rows are untouched
    assert FID not in control.propositions


def test_the_empire_is_a_faction_in_both_arms_and_its_cast_resolves_with_no_edit(control, foreign):
    assert EMPIRE in FACTIONS and FACTION_BY_PROP[FID] == EMPIRE
    assert set(FOREIGN_CAST) == {EMPIRE}, "a second foreign faction needs its own test row"
    assert [cast.faction_of(cast.row(c))[0] for c in ("NPC-011", "NPC-089", "NPC-090")] == [EMPIRE] * 3
    assert FID in foreign.propositions and str(foreign.propositions[FID].mood) == "HOLDS"
    assert sorted(world_q.members(foreign, FID)) == sorted(CAST)
    # NOT a member of the control arm: the three are unplaced there
    assert not any(t.object == FID for t in control.tenures)


def test_the_empires_persons_live_at_its_settlement_and_the_head_holds_its_root(foreign):
    place = FOREIGN_CAST[EMPIRE]
    root, town = f"terr_{place['territory']['code']}", f"set_{POP._slug(place['settlement']['code'])}"
    assert foreign.rungs[root].kind == "territory" and foreign.rungs[town].kind == "settlement"
    for pid in CAST:
        assert world_q.home_of(foreign)[pid] == town and world_q.residence_of(foreign)[pid] == town
    # the head (the faction's authored leader) holds the root, so `holder_faction_of` reads the town as the empire's
    assert world_q.holder_faction_of(foreign, town) == FID
    assert cast.faction_leader(EMPIRE) == "NPC-089"


def test_two_seats_are_held_and_the_head_alone_may_march(foreign):
    assert [r["faction"] for r in FOREIGN_SEATS] == [EMPIRE, EMPIRE]
    held = {t.object: t.subject for t in foreign.tenures if t.kind == "hold" and t.live
            and t.object in {r["id"] for r in FOREIGN_SEATS}}
    assert held == {"off_katepano": "p_npc_089", "off_kommerkiarios": "p_npc_090"}
    for oid in held:
        o = foreign.offices[oid]
        assert o.faction == EMPIRE and o.rung == f"set_{POP._slug(FOREIGN_CAST[EMPIRE]['settlement']['code'])}"
    granted = {pid: {a for t in foreign.persons[pid].tenures if t.kind == "hold" and t.live
                     for a in (t.granted_acts or ())} for pid in ("p_npc_089", "p_npc_090")}
    assert "dispatch" in granted["p_npc_089"] and "dispatch" not in granted["p_npc_090"], granted


def test_altonias_goal_rows_are_seeded_with_the_seats_goals_derived_from_the_empires(foreign):
    ids = {"goal_altonia_conquer_valoria", "goal_katepano_take_the_chokepoint"}
    assert ids <= set(foreign.propositions)
    assert "goal_kommerkiarios_treaty_order" not in foreign.propositions       # an orientation mints nothing
    committed = {gid: sorted(t.subject for t in foreign.tenures if t.kind == "commit" and t.live
                             and t.object == gid) for gid in ids}
    assert committed["goal_altonia_conquer_valoria"] == sorted(CAST)
    assert committed["goal_katepano_take_the_chokepoint"] == ["p_npc_089"]
    assert foreign.propositions["goal_katepano_take_the_chokepoint"].subject == "set_s_007"


# ---------------------------------------------------------------------------------------------- (c)

def test_the_foreign_root_is_outside_the_realm_for_endings_and_the_uncontrolled_census(control):
    foreign = POP.build_realm(0, foreign=True)          # its own world: the falsifier below ends a hold
    root = f"terr_{FOREIGN_CAST[EMPIRE]['territory']['code']}"
    assert not any(foreign.rungs[a].kind == "realm" for a in POP.ancestry(foreign, root)), "the border is breached"
    assert [r for r in foreign.rungs.values() if r.kind == "realm"] == [foreign.rungs["r_valoria"]]
    # THE FALSIFIER: end the root's only hold so NOBODY holds it. Were it counted under a realm, `uncontrolled`
    # (and so the census) would grow by one against the control arm, which seats no empire at all.
    for t in foreign.tenures:
        if t.kind == "hold" and t.object == root and t.live:
            t.until = foreign.tick
    assert world_q.holder_faction_of(foreign, root) is None
    assert world_q.uncontrolled(foreign, root) == [root], "the test world is not testing the unheld root"
    assert POP.census(foreign)["uncontrolled_in_realm"] == POP.census(control)["uncontrolled_in_realm"]
    # and the predicate `world_q._ending_edges` selects territories by (`world_q.py:1830-1831`), RE-SPELLED here and
    # not called, reaches no foreign territory
    chosen = [r for r in sorted(foreign.rungs) if foreign.rungs[r].kind == "territory"
              and any(a in foreign.rungs and foreign.rungs[a].kind == "realm" for a in POP.ancestry(foreign, r))]
    assert root not in chosen and len(chosen) >= 15


# ---------------------------------------------------------------------------------------------- (d)

def _march_candidate(w, target: str):
    p = w.persons["p_npc_089"]
    q = Question("q:in36_chooser_march", "need", (target,))
    v = View(p.id, [], w.fixtures.get("view_k"), q)
    return p, v, [c for c in opening_set(p, v, q, w.fixtures) if c.verb == "march"]


def test_the_natural_goal_question_forms_a_march_candidate_on_the_chokepoint_for_the_head_alone(foreign):
    """The goal row's own Question (`q:need:<goal id>`, Q4) names `set_s_007`, and clause 3 forms a march
    Candidate on it for the Katepano - and for nobody else of the empire (no `dispatch`)."""
    p = foreign.persons["p_npc_089"]
    qs = {q.id: q for q in world_q.questions_for(foreign, p)}
    q = qs["q:need:goal_katepano_take_the_chokepoint"]
    assert q.referents == ("set_s_007",), q.referents
    cands = opening_set(p, View(p.id, [], foreign.fixtures.get("view_k"), q), q, foreign.fixtures)
    assert any(c.verb == "march" and c.subject == "set_s_007" for c in cands)
    for pid in ("p_npc_011", "p_npc_090"):
        other = foreign.persons[pid]
        q2 = Question("q:in36_nodispatch", "need", ("set_s_007",))
        assert not [c for c in opening_set(other, View(pid, [], foreign.fixtures.get("view_k"), q2), q2,
                                           foreign.fixtures) if c.verb == "march"], pid


def test_a_march_formed_by_a_chooser_restricted_to_march_folds_to_the_mass_battle_entry():
    w = POP.build_realm(0, foreign=True)       # its own world: the driver below relocates the three Altonians
    target = "set_s_001"                  # Valorsplatz: Crown-held and peopled by Crown members (a fought field)
    assert world_q.holder_faction_of(w, target) == "fac_crown" and world_q.mustered(w, target, "fac_crown")
    p, v, cands = _march_candidate(w, target)
    assert [c.subject for c in cands] == [target], "the head forms no march on a realm settlement"
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    chooser = make_chooser(w.fixtures, mint, verbs=frozenset({"march"}),
                           draw=draw_factory(w.world_seed, lambda: w.tick))
    scenes = chooser(p, v, Sensation(0), lambda: 1)
    assert len(scenes) == 1 and len(scenes[0].acts) == 1, scenes
    act = scenes[0].acts[0]
    assert act.verb == "march" and act.payload["subject"] == target and act.actor == "p_npc_089"
    assert act.via == "off_katepano", f"the chooser did not name the empire's seat: {act.via!r}"   # read, not set

    records = []
    real = wrapper.field_input
    wrapper.field_input = lambda *a, **k: records.append(real(*a, **k)) or records[-1]
    try:
        d = SeasonDriver(w)
        w.step = Step.RESOLVE
        w.frozen = False
        events = d.resolve(mint_token(w, WriteClass.ACTS), [act], 2)
        events = events + d.encounter(mint_token(w, WriteClass.ACTS), events, 2)
    finally:
        wrapper.field_input = real
    kinds = [e.kind for e in events]
    assert "march.declared" in kinds and "field.unopposed" not in kinds, kinds
    assert len(records) == 1, f"the mass-battle entry was reached {len(records)} times, not once: {kinds}"
    rec = records[0]
    assert rec.territory == "T1", rec
    assert rec.origin == FOREIGN_CAST[EMPIRE]["territory"]["code"], f"not marched from the foreign root: {rec}"
    assert len(rec.weights[0]) == 3 and len(rec.weights[1]) >= 1, rec.weights    # the three Altonians vs the Crown's


def test_the_same_march_with_no_defender_arrives_unopposed_at_the_chokepoint(foreign):
    """Lowenskyst has no Crown member present as built (its barracks held only the Altonian Doux, who now lives
    at the empire's own settlement), so the goal's own objective is walked into, not fought for. Recorded as a
    FINDING, not a design (H-233): the realm's defence of its chokepoint is garrison Site and nobody."""
    w = POP.build_realm(0, foreign=True)
    assert world_q.mustered(w, "set_s_007", "fac_crown") == []
    p, v, cands = _march_candidate(w, "set_s_007")
    act = make_chooser(w.fixtures, lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}"),
                       verbs=frozenset({"march"}), draw=draw_factory(w.world_seed, lambda: w.tick))(
        p, v, Sensation(0), lambda: 1)[0].acts[0]
    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    w.frozen = False
    events = d.resolve(mint_token(w, WriteClass.ACTS), [act], 2)
    events = events + d.encounter(mint_token(w, WriteClass.ACTS), events, 2)
    assert "field.unopposed" in [e.kind for e in events]
    assert world_q.home_of(w)["p_npc_089"] == "set_s_007", "the army did not arrive"


# ---------------------------------------------------------------------------------------------- (e)

def _guard_weight(w, rung: str) -> int:
    """IN-60's DEFINITION, read off tenures in this file (the Query is B-Y's): the summed weight of persons
    PRESENT at `rung` (exact) who hold a live `oblige` to a seat held by a person ALSO present there."""
    here = set(world_q.presence(w, rung))
    held_by = {t.object: t.subject for t in w.tenures if t.kind == "hold" and t.live}
    return sum(w.persons[t.subject].weight for t in w.tenures
               if t.kind == "oblige" and t.live and t.subject in here and held_by.get(t.object) in here)


def test_the_control_arm_seats_no_guard_and_reads_zero_at_every_hearth(control):
    assert not [p for p in control.persons if p.startswith(POP.COHORT_PREFIX + "guard_")]
    assert all(_guard_weight(control, r) == 0 for r in control.rungs if control.rungs[r].kind == "hearth")


def test_a_guard_stands_where_each_principal_is_and_the_king_is_guarded_harder_than_a_duke(guarded):
    w = guarded
    home = world_q.home_of(w)
    by_seat = {row["seat"]: row["weight"] for row in POP.guard_rows()}
    assert set(by_seat) == {"off_king", "off_duchess_hafenmark", "off_duke_varfell"}
    authored = w._office_census["authored"]
    reads = {}
    for seat, wt in by_seat.items():
        holder = next(t.subject for t in w.tenures if t.kind == "hold" and t.live and t.object == authored[seat])
        reads[seat] = _guard_weight(w, home[holder])
        assert reads[seat] == wt > 1, (seat, reads[seat], wt)
    assert reads["off_king"] > reads["off_duchess_hafenmark"] and reads["off_king"] > reads["off_duke_varfell"], reads
    # An ordinary rung - the inn a sworn Crown obligee lives at - reads 0 with no principal present: the
    # Grand Master (NPC-070, the throne's named obligee) is sworn to the King, and lives apart from him.
    gm_home = home["p_npc_070"]
    assert home["p_npc_020"] != gm_home and _guard_weight(w, gm_home) == 0
    # the guard is a cohort (S9) and holds no title and no commitment
    for pid in (p for p in w.persons if p.startswith(POP.COHORT_PREFIX + "guard_")):
        assert w.persons[pid].weight > 1 and not [t for t in w.tenures if t.subject == pid and t.kind in ("hold", "commit")]


def test_ending_the_guards_oblige_drops_the_reading_with_no_other_write():
    w = POP.build_realm(0, guards=True)
    holder = next(t.subject for t in w.tenures if t.kind == "hold" and t.live and t.object == w._office_census["authored"]["off_king"])
    rung = world_q.home_of(w)[holder]
    before = _guard_weight(w, rung)
    assert before == 4
    for t in w.tenures:
        if t.kind == "oblige" and t.subject == f"{POP.COHORT_PREFIX}guard_off_king":
            t.until = w.tick
    assert _guard_weight(w, rung) == 0, "the guard's live oblige edge is what the definition reads; closing it must drop the read"


def test_guard_rows_refuse_what_they_cannot_read():
    from engine.season.gaps import Forbidden, Unspecified
    with pytest.raises(Unspecified):
        POP.guard_rows("guards: []\n")
    with pytest.raises(Forbidden):
        POP.guard_rows("guards:\n- {seat: off_king, weight: 1}\n")
    with pytest.raises(Unspecified):
        POP.guard_rows("guards:\n- {seat: off_nowhere, weight: 2}\n")
    with pytest.raises(Unspecified):
        POP.guard_rows("guards:\n- {seat: off_king, weight: 2}\n- {seat: off_king, weight: 3}\n")
