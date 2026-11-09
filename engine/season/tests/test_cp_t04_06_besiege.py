"""CP-T04-06 (B10-12; AM-C-11 REPAIR): `besiege`, a march that sits before the walls. `march` gains a `posture` payload key
(`rosters.yaml: march_postures`, shipped `[storm]`); an OPPOSED `besiege` fights no field and is graded `Invested`
(`field_degree_bands`, emitting `siege.pressed`), and `_eff_march` lowers each garrison Site in the target's subtree by
`_fall(w, site)` DIRECTLY through the gate (`write_matrix.yaml`'s `(Site, condition)` gains `ENC`). This file is the item's
own; nothing here is a shared pin.

THE POSTURE IS BUILT BY SWEEPING THE ROSTER IN A TEST COPY. The shipped roster stays `[storm]`, so `besiege` is a posture
no shipped season declares; `_swept` sets `rosters.MARCH_POSTURES` and `CHOICE_RANGES["posture"]` to `(storm, besiege)` for
one test and puts them back (`monkeypatch`).

THE FIELD IS HAND-BUILT, NOT NATURAL. One shipped season fights almost no field and `restore` is never attempted in a natural
run, so the walls are worn only by acts built here: the Crown's two marchers (`set_s_014`, `WEIGHT` each) on the Church's six
(`set_s_036`), the record `test_cp_t04_05_graded_walls.py` builds (`field_walls_dr = 3`, an OPEN_FLAT place), so a storm reads
the walls the siege left.

FALSIFIER (the entry's): (1) after k besieging acts the garrison condition reads the `_fall` iterate, computed here from the
share and the condition by integer arithmetic (the test holds its own copy of the iterate, not `_fall`), with `n` fixed at 3 by
putting two bystanders at the garrison's rung; (2) a storm afterwards wins more often over paired seeds than a storm at full
walls. MINIMUM n: `SEEDS` = 100 -- measured at the build, the attacker's share is 0.37 at full walls against 0.52 after one
besieging act at 100 paired seeds (0.35 against 0.55 at 60, 0.435 against 0.605 at 200): the 15-point gap clears the +-7 band
the CP-T04-05 file uses at about two standard errors of the difference, where 60 (a 20-point gap on a 9-point error) would
not be credible. A module-side fold costs 7-10 ms (a driver fold ~75 ms), so the arm is ~1.5 s. PLANTED FAILURE: the posture is ignored (`MARCH_POSTURE_KEY` repointed), the
condition never moves, and the same predicate reddens. CONTROLS: no act declares `besiege` (a storm with the posture named is
the storm with none, hash-equal); an UNOPPOSED `besiege` is the storm's `Unopposed`; the shipped roster refuses a `besiege`;
the roster `[storm]` fans nothing in `operand_bags` and `[storm, besiege]` fans two."""
from __future__ import annotations

import random

import pytest

from engine.season.data import rosters
from engine.season.data.verbs import CHOICE_RANGES, VERB_TABLE, act_key
from engine.season.decision.options import operand_bags
from engine.season.gaps import Unspecified
from engine.season.harness.populated import build_realm
from engine.season.queries import world_q
from engine.season.seam.wrappers import mass_battle as wrapper
from engine.season.state.carriers import Act, Question, Tenure
from engine.season.state.world import World
from engine.season.tests.test_cp_t04_05_graded_walls import MARCHERS, TARGET, _mb, _record, _world
from engine.season.tests.test_march import _fold_one

SEEDS, NOISE = range(100), 0.07
UNHELD = "set_s_037"                # no holder: a march on it has no opposing side
VIA = "off_spymaster"
BYSTANDERS = ("p_npc_001", "p_npc_002")     # re-homed to the garrison's rung to make `n` 3, then `share` is (1, 3)


@pytest.fixture
def swept(monkeypatch):
    """`march_postures` swept to `[storm, besiege]` in a test copy, at both places the roster is read."""
    monkeypatch.setattr(rosters, "MARCH_POSTURES", ("storm", "besiege"))
    monkeypatch.setitem(CHOICE_RANGES, "posture", ("storm", "besiege"))


def _act(aid, target=TARGET, posture=None, actor=MARCHERS[0]):
    payload = {"subject": target} if posture is None else {"subject": target, "posture": posture}
    return Act(id=aid, actor=actor, verb="march", payload=payload, via=VIA)


def _garrison(w, rung=TARGET):
    (s,) = [s for s in w.sites.values() if s.kind == "garrison" and s.rung == rung]
    return s


def _crowd(w, rung):
    """Put `BYSTANDERS` at `rung` (their old `contain` closed, a new one opened), so `presence` there is 3, whoever else is."""
    for i, pid in enumerate(BYSTANDERS):
        for t in w.tenures:
            if t.subject == pid and t.kind == "contain" and t.live:
                t.until = w.tick
        w.add_tenure(Tenure(f"t_bz{i}", pid, rung, "contain", w.tick))
    assert len(world_q.presence(w, rung)) == 3 and world_q.share(w, _garrison(w, rung)) == (1, 3)


def _iterate(c, n, k):
    """The garrison's condition after k falls at a fixed share 1/n: `c - c*1//n`, k times (`_fall`'s formula, written here)."""
    for _ in range(k):
        c -= (c * 1) // n
    return c


def _besiege(w, k, posture="besiege", target=TARGET):
    """k besieging acts folded one after another through the real driver; the condition after each."""
    out = []
    for i in range(k):
        _fold_one(w, _act(f"b{i}", target, posture))
        out.append(_garrison(w, target).condition)
    return out


def test_shipped_roster_is_storm_and_a_besiege_is_refused_before_a_field_is_fought():
    assert rosters.MARCH_POSTURES == ("storm",)
    w = _world(3, 1.0)
    with pytest.raises(Unspecified):
        _fold_one(w, _act("b0", posture="besiege"))
    assert _garrison(w).condition == w.fixtures.get("condition_scale")


def test_falsifier_the_condition_reads_the_fall_iterate_after_k_acts(swept):
    w = _world(3, 1.0)
    _crowd(w, TARGET)
    c0 = _garrison(w).condition
    assert c0 == w.fixtures.get("condition_scale")
    got = _besiege(w, 3)
    assert got == [_iterate(c0, 3, k) for k in (1, 2, 3)] == [667, 445, 297], got
    # nobody was hurt or moved, and no journey was written: a besieger makes no journey
    assert [w.persons[p].travel_leg for p in MARCHERS] == [[], []]
    assert [w.persons[p].body for p in MARCHERS] == [1000, 1000]
    assert world_q.march_origin(w, MARCHERS[0]) == world_q.march_origin(build_realm(0), MARCHERS[0])


def test_the_write_is_direct_wear_is_never_staged_through_world_stage(swept, monkeypatch):
    def refuse(*a, **k):
        raise AssertionError("`World.stage` was called: a besiege's wear must be written directly")
    monkeypatch.setattr(World, "stage", refuse)
    w = _world(3, 1.0)
    assert _besiege(w, 1) == [0]            # n = 1 at the realm's garrison: one act zeroes the walls (the entry's stated limit)


def test_the_event_is_siege_pressed_graded_invested_and_a_second_act_on_dead_walls_is_refused(swept):
    w = _world(3, 1.0)
    ev = _fold_one(w, _act("b0", posture="besiege"))
    assert [(e.kind, e.degree) for e in ev] == [("march.declared", "Declared"), ("siege.pressed", "Invested")]
    ev = _fold_one(w, _act("b1", posture="besiege"))            # nothing left to lose: the band writes nothing, so it declines
    assert [e.kind for e in ev] == ["march.declared", "march.refused"], [e.kind for e in ev]


def test_planted_failure_ignoring_the_posture_leaves_the_condition_where_it_was(swept, monkeypatch):
    """MUTATION: the provider reads the posture under a key no act carries, so a `besiege` is a storm. The falsifier's
    predicate (the condition reads the iterate, i.e. it MOVED) must then fail on the same fold."""
    monkeypatch.setattr(wrapper, "MARCH_POSTURE_KEY", "not_posture")
    w = _world(3, 1.0)
    _crowd(w, TARGET)
    got = _besiege(w, 1)
    assert got != [_iterate(w.fixtures.get("condition_scale"), 3, 1)]
    assert got == [w.fixtures.get("condition_scale")], got           # a storm does not wear the walls
    with pytest.raises(AssertionError):
        assert got == [667]


def _attacker_share(w):
    """Attacker win share over the paired `SEEDS`, on the record `field_input` builds from the world as it stands."""
    inp = _record(w)
    wins = sum(bool(_mb().resolve_field(inp, random.Random(s))["attacker_wins"]) for s in SEEDS)
    return wins / len(SEEDS), inp.walls_dr


def test_planted_failure_a_siege_that_moved_nothing_leaves_the_storm_at_full_walls(swept, monkeypatch):
    """MUTATION, on the second half of the falsifier: the posture is ignored, the walls stand, and the storm after it is the
    storm at full walls -- the same predicate (`after - before >= NOISE`) is false."""
    before, _ = _attacker_share(_world(3, 1.0))
    monkeypatch.setattr(wrapper, "MARCH_POSTURE_KEY", "not_posture")
    w = _world(3, 1.0)
    _besiege(w, 1)
    after, dr = _attacker_share(w)
    assert dr == 3 and not (after - before >= NOISE), (before, after)


def test_falsifier_a_storm_after_a_siege_wins_more_often_than_a_storm_at_full_walls(swept):
    before, dr0 = _attacker_share(_world(3, 1.0))
    w = _world(3, 1.0)
    assert _besiege(w, 1) == [0]
    after, dr1 = _attacker_share(w)
    assert (dr0, dr1) == (3, 0)                                   # the record carried the walls the siege left
    assert after - before >= NOISE, (before, after)


def test_control_no_act_declares_besiege_a_storm_with_the_posture_named_is_the_storm_with_none(swept):
    hashes = []
    for posture in (None, "storm"):
        w = _world(3, 1.0)
        ev = _fold_one(w, _act("m1", posture=posture), contest_max_depth=2)
        assert any(e.kind.startswith("field.") for e in ev), [e.kind for e in ev]
        hashes.append(w.content_hash())
    assert hashes[0] == hashes[1]


def test_an_unopposed_besiege_resolves_unopposed_as_a_storm_would(swept):
    out = []
    for posture in ("storm", "besiege"):
        w = build_realm(0)
        before = _garrison(w, UNHELD).condition
        ev = _fold_one(w, _act("m1", UNHELD, posture))
        out.append(([(e.kind, e.degree) for e in ev], w.content_hash(), _garrison(w, UNHELD).condition))
        assert _garrison(w, UNHELD).condition == before          # an empty place needs no siege
    assert out[0][0] == out[1][0] and out[0][1] == out[1][1], out
    assert [k for k, _ in out[0][0]][-1] in ("field.unopposed", "army.arrived")


def test_operand_bags_ranges_the_posture_only_when_there_is_one_to_choose(monkeypatch):
    w = build_realm(0)
    p, q = w.persons[MARCHERS[0]], Question("q:bz", "need", (TARGET,))
    plain = operand_bags(p, VERB_TABLE["march"], q, TARGET, w.fixtures)
    assert plain and all("posture" not in b for b in plain)           # [storm] fans nothing: the shipped acts keep their ids
    monkeypatch.setattr(rosters, "MARCH_POSTURES", ("storm", "besiege"))
    monkeypatch.setitem(CHOICE_RANGES, "posture", ("storm", "besiege"))
    fanned = operand_bags(p, VERB_TABLE["march"], q, TARGET, w.fixtures)
    assert sorted(b["posture"] for b in fanned) == ["besiege", "storm"] * len(plain)
    ids = {act_key("march", TARGET, b) for b in fanned}
    assert len(ids) == len(fanned)                                  # two postures on one subject are two acts
