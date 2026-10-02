"""Plan position `17` (U8) -- `person_q.ambitions(p, propositions)` and `corpus_run.build_at`'s cast.

What each test proves, and the failure it can observe:

  (a) `ambitions` reads LIVE `commit` edges to OUGHT Propositions off a person's OWN tenures, and
      ignores every other shape an edge can take: an ended edge, a non-`commit` edge, a `commit`
      to a non-OUGHT Proposition (the distractor here is a bare HOLDS; real faction membership is
      NOT one for six of the nine factions -- `populated.py` mints those creeds as OUGHT, and only
      `Guilds`, `Schoenland` and `faction x` keep HOLDS), a `commit` to an id no Proposition has. Each
      distractor is tried ALONE (a person holding only it has no ambition) so a loop that happened
      to pass on the sum cannot hide one, and the positive control asserts the answer is non-empty.
  (b) AX-2: the `sense`-is-the-only-World-taker guard SEES `ambitions` (it is in the guard's own
      `found` list) and turns RED when `ambitions` is given a `World` parameter. The mutation is
      applied to a COPY of `person_q.py` in a tmp dir and the guard is re-pointed at it, so the
      run-and-restore is automatic and the tree is never edited.
  (c) With a `cast:` the people come from it: `p_b`/`p_c` are named for the cast, an 11-entry cast
      seats eleven and RUNS, a `WAITS-ON-PLAYER` entry is not seated and is reported, each entry's
      `capability` lands on its own seat only.
  (d) CONTROL: with `cast:` absent `build_at` seats the three anonymous people and every tally is
      unchanged -- compared to an arm with the overlay table emptied, and (for a one-entry cast) to
      the same world with the one seated name put back, so seating can be seen to move NOTHING
      but the name. NPC-020 carries no overlay.
  (e) Q4 (`world_q.questions_for`) fires for more than one proposition: one per person across a
      cast, and more than one per PERSON when a person holds two ambitions.

NOT BUILT HERE (plan position `17` stopped on three keys): `office:` and `ought:` were built at `17-cast`
and are tested in `test_u8_cast_fields.py`; `knowledge` -> initial Claims is REFUSED by name at load
(a new `Claim`-construction site, AX-7), tested there too.
"""
import ast

import pytest

from engine.season.data.rosters import RUNG_KINDS
from engine.season.harness import corpus_run as C
from engine.season.harness import run_cases as RC
from engine.season.queries import person_q, world_q
from engine.season.state.carriers import Person, Proposition, Tenure


# ---------------------------------------------------------------------------
# (a) `ambitions`
# ---------------------------------------------------------------------------

def _person_with(*edges) -> Person:
    p = Person("p_x", "x")
    p.tenures.extend(edges)
    return p


PROPS = {
    "o1": Proposition("o1", "OUGHT", "p_y", "a first ambition", True, 0),
    "o2": Proposition("o2", "OUGHT", "p_z", "a second ambition", True, 0),
    "fac": Proposition("fac", "HOLDS", "Crown", "is a faction of this world", True, 0),
}

# Every shape of edge that is NOT an ambition, one per row. A distractor held alone must answer [].
DISTRACTORS = {
    "ended commit to an OUGHT": Tenure("d1", "p_x", "o1", "commit", 0, until=3),
    "a hold (not a commit) on an OUGHT": Tenure("d2", "p_x", "o1", "hold", 0),
    # a HOLDS Proposition: `populated.py` mints this shape for only three factions (Guilds,
    # Schoenland, faction x); the other six creeds are OUGHT commits that `ambitions` DOES return
    # (Jordan, 2026-09-13).
    "commit to a HOLDS (a faction with no creed)": Tenure("d3", "p_x", "fac", "commit", 0),
    "commit to an id no Proposition has": Tenure("d4", "p_x", "nowhere", "commit", 0),
}


def test_ambitions_is_the_live_commit_to_an_ought_and_nothing_else():
    ours = [Tenure("a1", "p_x", "o1", "commit", 0), Tenure("a2", "p_x", "o2", "commit", 1)]
    got = person_q.ambitions(_person_with(*ours), PROPS)
    assert got == ["o1", "o2"], got            # edge order, and non-empty: a vacuous loop cannot pass
    assert len(got) >= 1

    for label, edge in DISTRACTORS.items():
        assert person_q.ambitions(_person_with(edge), PROPS) == [], label

    # The sum: the distractors may not displace the real edges nor add to them.
    mixed = [DISTRACTORS["ended commit to an OUGHT"], ours[0],
             DISTRACTORS["commit to a HOLDS (a faction with no creed)"], ours[1],
             DISTRACTORS["commit to an id no Proposition has"],
             DISTRACTORS["a hold (not a commit) on an OUGHT"]]
    p = _person_with(*mixed)
    assert len(p.tenures) == 6                  # the person really holds all six edges
    assert person_q.ambitions(p, PROPS) == ["o1", "o2"]


def test_ambitions_counts_one_proposition_once_and_ends_with_the_edge():
    twice = [Tenure("a1", "p_x", "o1", "commit", 0), Tenure("a2", "p_x", "o1", "commit", 2)]
    assert person_q.ambitions(_person_with(*twice), PROPS) == ["o1"]
    # An ambition ENDS with its edge: the same person, the edge closed in place.
    p = _person_with(Tenure("a1", "p_x", "o1", "commit", 0))
    assert person_q.ambitions(p, PROPS) == ["o1"]
    p.tenures[0].until = 4
    assert person_q.ambitions(p, PROPS) == []


# ---------------------------------------------------------------------------
# (b) AX-2
# ---------------------------------------------------------------------------

def test_ax2_guard_sees_ambitions_and_goes_red_when_it_is_given_a_world(tmp_path, monkeypatch):
    from engine.season.tests import test_season_shape as TS
    guard = TS.test_w5_sense_is_still_the_only_world_taking_non_decision_function
    guard()                                    # CONTROL: green on the tree as it stands
    real = TS._model_modules()
    (path,) = [m for m in real if m.name == "person_q.py"]
    src = path.read_text(encoding="utf-8")
    sig = "def ambitions(p: Person, propositions) -> list:"
    assert src.count(sig) == 1, "the signature this mutation targets moved; re-point it"
    mutated = tmp_path / "person_q.py"
    mutated.write_text(src.replace(sig, 'def ambitions(p: Person, propositions, w: "World") '
                                        '-> list:'), encoding="utf-8")
    monkeypatch.setattr(TS, "_model_modules", lambda: [mutated if m == path else m for m in real])
    with pytest.raises(AssertionError) as red:
        guard()
    assert "ambitions" in str(red.value), str(red.value)


# ---------------------------------------------------------------------------
# (c) the cast seats the people
# ---------------------------------------------------------------------------

NO_OVERLAY = "NPC-020"      # carries no `cast:` overlay (`test_w28_cast...` asserts the same)


def _case(cid: str) -> dict:
    return C.apply_rescale({c["id"]: c for c in RC.load_cases("NPC")}[cid])


def _host_case() -> dict:
    """A representable NPC case that carries no overlay, other than the control: the host a fixture
    cast is hung on. Derived, not named, so a corpus change cannot strand it."""
    for c in RC.load_cases("NPC"):
        c = C.apply_rescale(c)
        if (str(c.get("scale")) in set(RUNG_KINDS) and c["id"] not in C.CAST
                and c["id"] != NO_OVERLAY):
            return c
    raise AssertionError("no representable overlay-free NPC case")


def _entries(seated: int, waiting_at: int | None = None) -> list:
    es = [{"who": f"Fixture {i}", "role": "protagonist" if i == 0 else "ally"}
          for i in range(seated)]
    if waiting_at is not None:
        es.insert(waiting_at, {"who": "the player", "role": "WAITS-ON-PLAYER"})
    return es


def test_p_b_and_p_c_come_from_the_cast_and_the_floor_stays_three(monkeypatch):
    case = _host_case()
    monkeypatch.setitem(C.CAST, case["id"], _entries(2))
    w = C.build_at(case, 0)
    assert list(w.persons) == ["p_a", "p_b", "p_c"]
    assert [p.name for p in w.persons.values()] == ["Fixture 0", "Fixture 1", "p_c"]
    monkeypatch.setitem(C.CAST, case["id"], _entries(3))
    w = C.build_at(case, 0)
    assert [p.name for p in w.persons.values()] == ["Fixture 0", "Fixture 1", "Fixture 2"]


def test_eleven_actors_seat_a_player_is_not_one_and_capability_lands_on_its_own_seat(monkeypatch):
    case = _host_case()
    es = _entries(11, waiting_at=3)
    es[4]["capability"] = {"copying": 3}       # the fifth entry in file order: 4th seated -> p_e
    assert len(es) == 12 and C.seating({**case, "id": "x"}) == ([], [])
    monkeypatch.setitem(C.CAST, case["id"], es)
    seated, waiting = C.seating(case)
    assert len(seated) == 11 and [e["who"] for e in waiting] == ["the player"]
    w = C.build_at(case, 0)
    assert list(w.persons) == [f"p_{c}" for c in "abcdefghijk"]
    assert [p.name for p in w.persons.values()] == [f"Fixture {i}" for i in range(11)]
    assert "the player" not in {p.name for p in w.persons.values()}
    # `es[4]` is the SEATED entry with `who` "Fixture 3" (the player was inserted at index 3).
    assert {pid: p.capability for pid, p in w.persons.items() if p.capability} == \
        {"p_d": {"copying": 3}}, "capability must land on its own seat and on no other"
    # Every seat is a person with a person-rung, a home, and exactly one OUGHT commitment.
    for pid in w.persons:
        assert pid in w.rungs and w.rungs[pid].kind == "person"
        assert [t.object for t in w.persons[pid].tenures if t.kind == "commit"] == [f"prop_{pid}"]


def test_an_eleven_actor_case_runs(monkeypatch):
    case = _host_case()
    monkeypatch.setitem(C.CAST, case["id"], _entries(11, waiting_at=3))
    r = C.run_case(case, 0, "NPC")
    assert r["checks"] and r["checks"]["R1"] is True, r
    assert r["status"] not in {"HALTS", "INSTRUMENT-DEFECT", "DESIGN-GAP"}, r
    # `persons` is read AFTER the run and a `fight` can remove one, so it is bounded, not equal.
    assert 3 < r["persons"] <= 11, r["persons"]
    assert r["waits_on_player"] == ["the player"], r["waits_on_player"]
    assert r["executed"], "eleven people ran a season and nothing executed"
    # And MORE THAN THREE PEOPLE ACTED: the same driver `run_case` builds, over the same world.
    w = C.build_at(case, 0)
    d = C.SeasonDriver(w)
    mint = lambda pid, verb, subj: C.H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = C.make_chooser(w.fixtures, mint, verbs=C.resolvable_verbs(),
                        draw=C.draw_factory(w.world_seed, lambda: w.tick))
    for _ in range(C.seasons_for(case)):
        d.season(ch, question=None, subsistence=C.P.SUBSIST,
                 contest_max_depth=w.fixtures.get("contest_max_depth"))
    actors = {a.actor for a in d.resolved}
    assert len(actors) > 3 and actors <= set(w.persons) | {f"p_{c}" for c in "abcdefghijk"}, actors


def test_a_malformed_cast_entry_refuses_at_load_and_a_good_one_loads(tmp_path, monkeypatch):
    monkeypatch.setattr(C.files, "EXERCISES_DIR", tmp_path)
    (tmp_path / "X-1.yaml").write_text("case: X-1\ncast:\n- who: Someone\n  role: protagonist\n",
                                       encoding="utf-8")
    assert C.cast_overlay() == {"X-1": [{"who": "Someone", "role": "protagonist"}]}
    (tmp_path / "X-1.yaml").write_text("case: X-1\ncast:\n- role: protagonist\n", encoding="utf-8")
    with pytest.raises(SystemExit):
        C.cast_overlay()


# ---------------------------------------------------------------------------
# (d) the control: no cast -> exactly what `build_at` always built
# ---------------------------------------------------------------------------

def _tally(w) -> dict:
    return dict(persons=sorted(w.persons), names=[p.name for p in w.persons.values()],
                propositions=sorted(w.propositions), tenures=len(w.tenures),
                capability={k: p.capability for k, p in w.persons.items()},
                pursuits={k: p.pursuits for k, p in w.persons.items()},
                rungs=sorted(w.rungs), sites=sorted(w.sites), docket=len(w.docket),
                hash=w.content_hash())


def test_npc_020_has_no_overlay_and_builds_three_anonymous_people(monkeypatch):
    assert NO_OVERLAY not in C.CAST
    case = _case(NO_OVERLAY)
    w = C.build_at(case, 0)
    assert list(w.persons) == ["p_a", "p_b", "p_c"]
    assert [p.name for p in w.persons.values()] == ["p_a", "p_b", "p_c"]
    assert sorted(w.propositions) == ["prop_p_a", "prop_p_b", "prop_p_c"]
    assert all(not p.capability for p in w.persons.values())
    # The arm with EVERY overlay removed is the same world, byte for byte.
    base = _tally(w)
    monkeypatch.setattr(C, "CAST", {})
    assert _tally(C.build_at(case, 0)) == base


def test_a_one_entry_cast_moves_nothing_but_the_seated_name(monkeypatch):
    """The CONTROL that makes the seating falsifiable: with a single protagonist entry (and no
    `capability`) the world must differ from the no-cast world in the NAME of `p_a` and in nothing
    else. If seating touched a tenure, a proposition, a pursuit or a rung, the hash differs."""
    case = _host_case()
    plain = C.build_at(case, 0)
    monkeypatch.setitem(C.CAST, case["id"], _entries(1))
    cast = C.build_at(case, 0)
    assert cast.persons["p_a"].name == "Fixture 0" and plain.persons["p_a"].name == "p_a"
    assert cast.content_hash() != plain.content_hash(), "the name should be in the hash"
    cast.persons["p_a"].name = "p_a"
    assert _tally(cast) == _tally(plain)


# ---------------------------------------------------------------------------
# (e) Q4 fires for more than one proposition
# ---------------------------------------------------------------------------

def _need_props(w) -> set:
    return {q.about for p in w.persons.values() for q in world_q.questions_for(w, p)
            if q.source == "need"}


def test_q4_fires_for_every_seated_persons_ambition(monkeypatch):
    case = _host_case()
    pre = _need_props(C.build_at(case, 0))
    assert pre == {"prop_p_a", "prop_p_b", "prop_p_c"}
    monkeypatch.setitem(C.CAST, case["id"], _entries(11, waiting_at=3))
    post = _need_props(C.build_at(case, 0))
    assert post == {f"prop_p_{c}" for c in "abcdefghijk"}, post
    assert len(post) > len(pre) > 1


def test_q4_fires_once_per_ambition_for_one_person_and_through_ambitions():
    w = C.build_at(_case(NO_OVERLAY), 0)
    me = w.persons["p_a"]
    before = [q for q in world_q.questions_for(w, me) if q.source == "need"]
    assert [q.about for q in before] == person_q.ambitions(me, w.propositions) == ["prop_p_a"]
    # A SECOND ambition, a commit to a HOLDS Proposition (not an ambition: the three creedless
    # factions' shape -- the other six creeds ARE ambitions) and an ended one.
    w.propositions["o2"] = Proposition("o2", "OUGHT", "p_c", "a second cause", True, 0)
    w.propositions["fac"] = Proposition("fac", "HOLDS", "Crown", "is a faction", True, 0)
    w.add_tenure(Tenure("t_o2", "p_a", "o2", "commit", 0))
    w.add_tenure(Tenure("t_fac", "p_a", "fac", "commit", 0))
    w.add_tenure(Tenure("t_dead", "p_a", "prop_p_b", "commit", 0, until=1))
    needs = [q for q in world_q.questions_for(w, me) if q.source == "need"]
    assert sorted(q.about for q in needs) == ["o2", "prop_p_a"], [q.about for q in needs]
    assert sorted(person_q.ambitions(me, w.propositions)) == ["o2", "prop_p_a"]
