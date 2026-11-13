"""v10 REM-30 (IN-47): the character sheet's three spaces (`decision/sheet.py`), executed.

THE FALSIFIER AND THE CONTROL the plan names, and what each can observe:

  * CONTROL -- the creation arm switched off (`seat(rows, None, ...)`, the shipped state) reproduces the
    pre-build `build_realm(s).content_hash()` at 1 season, seeds 0-2, PINNED below from the parent tree
    (`96136014`, REM-31's commit, `PYTHONHASHSEED=0`) before any REM-30 edit.
  * CONTROL -- the arm ON with the development space's `take_ranked` pick is the automated chooser by
    construction (same `make_ranker` order, same `release`): equal hash.
  * MOVER -- the arm ON with a pick that differs from the ranking moves the hash (the space reaches the
    world only through the acts RESOLVE folds).
  * REFUSALS -- creation seats only a person the builder seated; development selects only among the
    candidates the opening set formed (no second option generator).
  * CHRONICLING writes nothing: reading every person's chronicle between seasons leaves the hash equal.
  * THE WRITE FALSIFIER is not here: a space that assigns a `Person` field reddens
    `test_g2_token.py::test_g2_deliberate_mutates_no_store_by_any_route` (its spaces arm).
"""
import pytest

from engine.season.decision import make_chooser
from engine.season.decision.sheet import (
    chronicle, creation_sheet, development_space, seat, take_ranked,
)
from engine.season.gaps import Forbidden
from engine.season.harness import headless as HL
from engine.season.harness import populated as PO
from engine.season.harness.play_surface import dispatching_chooser
from engine.season.loop.driver import SeasonDriver, resolvable_verbs
from engine.season.state.carriers import Claim, Person
from engine.season.state.ids import H, draw_factory

# The parent tree's realm hash after 1 season (`PYTHONHASHSEED=0`), the arm off. The OFF arm must reproduce these.
# RE-RECORDED at v10 REM-30's second commit (the `verb_capability` rows, a DECLARED MOVER): was, from REM-31's commit
# `96136014` read before REM-30 touched anything, 36378f25... / 8899cdd5... / 048a326b... for seeds 0 / 1 / 2. CONTROL: this
# commit's four source files reverted read the old three exactly (the first REM-30 commit's own run).
# RE-PINNED ONCE at v10 CR-30 for CR-20 + CR-30 (Person.attributes / Person.heritage in every repr; four authored heritage rows):
# was 027c7516... / 5b000930... / 891860d4.... The arm-off event list over two seasons equals the parent tree's at seeds 0 / 1 / 2.
# RE-PINNED ONCE at v10 CR-33 (NPC-088's `lifepath: 3-CF4` holds `inquiry` at `pool_default`; a Person repr, the event list unmoved): was
# f2e5e265... / 0d25717b... / 05f065f4.... CONTROL: `data/cast.py::capability_of` stubbed to `{}` reads the old three exactly
# (`test_cr33_lifepaths.py::BASE`), and the ordered (kind, id) event list equals the parent tree's at seeds 0 / 1 / 2.
# RE-PINNED ONCE at v10 CP-T03-09 (`capture`, a declared mover of the one-season realm): was 71ff6e92... / 73af0d1e... / 011a4605.... CONTROL: `capture` withheld
# from `populated.resolvable_verbs` reads the old three exactly. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED ONCE at v10 PC-10b (a challenge is a Record; `accept` binds to one; a declared mover wherever a challenge forms): was
# 009f9f31... / daca4682... / db5bd6f0.... CONTROL: the base tree (`95f58adb`'s `engine/season`) reads the old three. A GOLDEN
# RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED ONCE at v11 CR-87 (violence made exceptional: a declared mover of the build and of every season that fought): was
# 0fb73bc8... / 3b407a74... / 47151656.... CONTROL: `test_cr87_violence_contexts.py::revert_cr87` reads the old seed-0 pin
# exactly. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED ONCE at v10 CP-T03-02 (a fight band's `Event.ending` and the body Observation, a declared mover wherever a
# Felled/Wounded fight lands): seeds 1, 2 were f4330aac... / a030141a...; seed 0 does not move. CONTROL:
# `test_cp_t03_02_band_ending_and_body.py::revert_cp_t03_02` reads the old three exactly. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED ONCE at v11 CR-85 (`faculty` replaces `history` in combat's pool and Ob, ED-IN-0330; every season fight
# rolls pool 8 against Ob 1.0, was 9 against 1.5): seed 1 was f89ea45d...; seeds 0 and 2 do not move (seed 0 fights
# nothing, seed 2's fights land where they did). CONTROL: `test_cr85_faculty_replaces_history.py::revert_cr85` (the
# seam's faculty at 3 for every party) reads the old value exactly. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED ONCE at v11 CP-T03-04 (`arms` in `verb_capability`'s range: a FORMATION mover even at control, one more `train`
# Candidate per `train` formation with nobody holding the key): seeds 0 / 1 / 2 were 20accb03... / 6e25b047... / fe9032ed...; no roll moves (nobody
# holds `arms`). CONTROL: `test_cp_t03_04_arms.py::revert_cp_t03_04` (the three roster rows and the vocation off) reads the
# old three exactly. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED ONCE at v11 CP-T03-07 (`Person.body_ceiling`, a SCHEMA mover of every realm, and the lasting mark, an outcome
# mover where a survivor reached the deepest gate -- one person at seed 2): seeds 0 / 1 / 2 were b2dde1fc... / 07634b99... /
# 1cc4370d.... CONTROL: `test_cp_t03_07_body_ceiling.py::revert_cp_t03_07` (`body_mark_model: none` and the field out of
# the canonical encoding) reads the old three exactly. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# RE-PINNED ONCE at v11 CP-T03-08 (`tend` declares `referent_class: Person` and `wounded_with` stamps the wounded: a
# FORMATION mover of every season, and an outcome mover -- a man below his ceiling tends himself whole): seeds 0 / 1 / 2
# were eb2919ae... / fc3201f3... / 6da144ff.... CONTROL: `test_cp_t03_08_tend_on_the_wounded.py::revert_cp_t03_08` (the
# column emptied, the term returning `()`) reads the old three exactly. A GOLDEN RE-RECORDED, NOT A BALANCE CLAIM.
# Seeds 1 and 2 are the post-B10-11b reading (`reading @4b334f2a`), re-recorded by the batch pin commit (was d9f3be70... /
# 285fb92a...): PC-20 (1) (the head-weighted strike impact, `K_STR_HEAD`) moves a one-season run that reaches `strike_impact`.
PRE_BUILD = {
    0: "d796fd5e099aecdb52545dcc8c55ac51",   # B01 re-pin (B11 lane A, both commits rebased): was 25660615...; B10-13 batch pin commit: was d4c83c8c...; CP-T03-08: was eb2919ae...; CP-T03-07: was b2dde1fc...; CP-T03-04: was 20accb03...
    1: "056bff314ba696f54e8ff21212057221",   # B01 re-pin (B11 lane A, both commits rebased): was aa58ef0b...; B10-13 batch pin commit: was 7cacc763...; CP-T03-08: was fc3201f3...; CP-T03-07: was 07634b99...; CP-T03-04: was 6e25b047...; CR-85: was f89ea45d...
    2: "7f93eb2554768480d816c5fd040ffd9e",  # B01 re-pin (B11 lane A, both commits rebased): was a21ab6e1...; B10-12 pin commit (CR-24 + MB-07r): was 77a09697...; B10-13 batch pin commit: was 447ed0d8...; CP-T03-08: was 6da144ff...; CP-T03-07: was 1cc4370d...; CP-T03-04: was fe9032ed...; CR-33 verify pass (NPC-004's `lifepath: 3-CH5` holds `inquiry`, a Person repr): was 43d2c524... (seeds 0 and 1: NPC-004 has left the world by season 1)
}


def _wiring(w):
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    draw = draw_factory(w.world_seed, lambda: w.tick)
    return mint, draw


def _run(w, seasons, person_id=None, pick=take_ranked, between=None):
    """`populated.run`'s chooser, behind the creation arm: `person_id=None` is the arm off."""
    mint, draw = _wiring(w)
    auto = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(), draw=draw)
    space = development_space(w.fixtures, mint, pick, verbs=resolvable_verbs(), draw=draw)
    choose = dispatching_chooser(auto, seat(creation_sheet(w.persons.values()), person_id, space))
    d = SeasonDriver(w)
    for _ in range(seasons):
        d.season(choose, None, contest_max_depth=w.fixtures.get("contest_max_depth"))
        if between is not None:
            between(w)
    return w.content_hash()


@pytest.mark.parametrize("seed", sorted(PRE_BUILD))
def test_rem30_creation_arm_off_reproduces_the_pre_build_hash(seed, monkeypatch):
    from .test_strife_credit import revert_cr79
    revert_cr79(monkeypatch)
    assert _run(PO.build_realm(seed), 1) == PRE_BUILD[seed]


def _counting(pick, seen):
    def counted(sheet):
        seen.append(len(sheet.candidates))
        return pick(sheet)
    return counted


def test_rem30_development_space_taking_the_ranking_is_the_automated_chooser():
    """At the realm's first person by id and at Carin (`headless`): seated, with the control pick, equal
    hash; and the space was really called with candidates (a seat nobody deliberated for proves nothing)."""
    for build, seasons in ((lambda: HL.build_world(0), 2), (lambda: PO.build_realm(0), 1)):
        off = _run(build(), seasons)
        w = build()
        pid = sorted(w.persons)[0] if len(w.persons) > 3 else "p_carin"
        seen: list = []
        on = _run(w, seasons, pid, _counting(take_ranked, seen))
        assert on == off
        assert seen and max(seen) >= 1, (pid, seen)


def test_rem30_a_pick_that_differs_from_the_ranking_moves_the_hash():
    off = _run(HL.build_world(0), 2)
    seen: list = []
    flipped = _counting(lambda sh: list(reversed(range(len(sh.candidates)))), seen)
    on = _run(HL.build_world(0), 2, "p_carin", flipped)
    assert max(seen) >= 2, f"no deliberation offered two candidates to reverse: {seen}"
    assert on != off


def test_rem30_creation_seats_only_a_person_the_builder_seated():
    w = HL.build_world(0)
    rows = creation_sheet(w.persons.values())
    assert [r.id for r in rows] == sorted(w.persons)
    assert seat(rows, None, object()) == {}
    assert list(seat(rows, "p_carin", "space")) == ["p_carin"]
    with pytest.raises(Forbidden):
        seat(rows, "p_minted_by_the_player", "space")
    # the row is a copy: writing through it raises, and the person is untouched
    with pytest.raises(TypeError):
        rows[0].pursuits["planted"] = 1
    assert "planted" not in w.persons[rows[0].id].pursuits


@pytest.mark.parametrize("bad", [lambda sh: [len(sh.candidates)], lambda sh: [0, 0]])
def test_rem30_development_refuses_a_pick_outside_the_formed_set(bad):
    with pytest.raises(Forbidden):
        _run(HL.build_world(0), 1, "p_carin", bad)


def test_rem30_chronicling_writes_nothing():
    off = _run(HL.build_world(0), 2)
    read: list = []
    on = _run(HL.build_world(0), 2,
              between=lambda w: read.extend(chronicle(p) for p in w.persons.values()))
    assert on == off
    assert any(c.ledger for c in read), "no chronicle read a ledger; the arm observed nothing"


def test_rem30_chronicle_splits_scar_by_roster_and_by_holding():
    """The review's display rules (a) and (b), on a planted person: two rosters; a count on an unheld
    creed is history. And `beliefs` is `LedgerReader`'s pick per subject, not a re-ranking."""
    from engine.season.data.rosters import AFFILIATIONS
    held, unheld = sorted(AFFILIATIONS)[:2]
    p = Person("p_plant")
    p.scar = {"wealth": 2, held: 3, unheld: 1}
    p.conviction = {held: 4}
    old = Claim("c_old", "p_plant", "p_x", "at", "here", 0, "seen", 9, "own")
    new = Claim("c_new", "p_plant", "p_x", "at", "there", 1, "seen", 5, "own")
    p.ledger = [old, new]
    c = chronicle(p)
    assert dict(c.scar_pursuits) == {"wealth": 2}
    assert dict(c.scar_affiliations_held) == {held: 3}
    assert dict(c.scar_affiliations_history) == {unheld: 1}
    assert c.beliefs == (("p_x", new),)
    assert c.ledger == (old, new)
