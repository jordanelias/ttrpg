"""B34.15 -- ONE SCENE CONTRACT: a registered module is a season call and a playable scene by the same entry (`01_CORE_one_scene_contract` edits 1, 2, 4).

What is built: `PlayHost.deciders` and `decider_for` (a decider per module role), `seam/wrappers/_entry.py::played_by` (the party test, once), and `harness/scene.py::play`,
the module's scene run alone from a small world. The world here is `FIXTURES["fight_headless"]` (Carin's three people, a `fight` between the first two): the `duel`
fixture is HELD (`hole_register.yaml` H-580, its builder retired unbuilt), so nothing below stages it. The hearing's arm of gate 3 is
`test_sc_hearing_negotiation.py::test_scripted_player_reproduces_auto_hash` (the same `played_by`, a deviating decider moving the sitting). The nesting-cap test
(`test_a_duel_round_called_from_a_battle_may_not_call_a_third_scene`) is B30's. Lane: the season loop, placed in the `in` suite (`references/season_test_suites.yaml`).
"""
from __future__ import annotations

import functools

from engine.season.harness import scene
from engine.season.harness.carin import BAILIFF, CARIN, WARDEN, build_world
from engine.season.loop import resolve as resolve_mod
from engine.season.loop.driver import SeasonDriver
from engine.season.queries.inputs import PlayHost
from engine.season.state.carriers import Act

SEEDS = range(6)
FIXTURE = scene.FIXTURES["fight_headless"]
ROLE = FIXTURE["role"]


def _one_act_season(seed: int, host) -> str:
    """The content hash of `build_world(seed)` after a season in which Carin's `fight` against the bailiff is the one act chosen, under `host`."""
    w = build_world(seed)
    act = Act(id="scene_0", actor=CARIN, verb="fight", payload={"subject": BAILIFF})
    SeasonDriver(w).season(lambda p, v, s, ask: [act] if p.id == CARIN else [], None, contest_max_depth=w.fixtures.get("contest_max_depth"), host=host)
    return w.content_hash()


def test_echo_decider_equals_no_decider():
    """GATE 1: `scene.play('combat.fight', ...)` with no decider and with a decider that echoes the engine's own per-round policy (`engage`) return one record at the
    same seed (the trace of every round included), and the echo WAS ASKED at every seed (a host never called proves nothing, CLAUDE.md section 0.1 pt 2).
    FALSIFIER: a wrapper that builds another input, or draws another key, when a host is present."""
    asked = []
    for seed in SEEDS:
        auto = scene.play(ROLE, FIXTURE, seed=seed)
        echo = scene.play(ROLE, FIXTURE, seed=seed, decide=lambda view: (asked.append(view.round), "engage")[1])
        assert echo == {**auto, "played": True}, seed
    assert len(asked) >= len(SEEDS), asked


def test_empty_deciders_is_hash_equal_to_no_host():
    """GATE 2, the control that the contract moves nothing where no decider is asked: a one-act season ends at one content hash with no host, with a host that plays
    the fighter and names no decider (`PlayHost(deciders={})`), and with a host holding a decider for a person who is not in the fight (the party test, `played_by`:
    never asked). FALSIFIER: a present host changes what the season does. CONTROL, THE ARM THAT MUST MOVE: a host that plays the fighter and withdraws."""
    moved, asked = 0, []
    for seed in SEEDS:
        base = _one_act_season(seed, None)
        assert _one_act_season(seed, PlayHost(frozenset({CARIN}), deciders={})) == base, seed
        assert _one_act_season(seed, PlayHost(frozenset({WARDEN}), deciders={ROLE: lambda view: asked.append(view) or "withdraw"})) == base, seed
        moved += _one_act_season(seed, PlayHost(frozenset({CARIN}), deciders={ROLE: lambda view: "withdraw"})) != base
    assert not asked and moved > 0, (len(asked), moved)


def test_a_deviating_decider_moves_a_played_module():
    """GATE 3, for `combat.fight`: a decider that engages the first round and withdraws after it ends the scene differently from the automated one at some seed
    (the decider is the module loop's input, handed through `played_by`). FALSIFIER: an identical record at every seed, the decider being read nowhere."""
    differ = 0
    for seed in SEEDS:
        auto = scene.play(ROLE, FIXTURE, seed=seed)
        out = scene.play(ROLE, FIXTURE, seed=seed, decide=lambda view: "engage" if view.round == 1 else "withdraw")
        differ += out["result"] != auto["result"]
    assert differ > 0, differ


def test_apply_false_goes_through_seam_contest():
    """`apply=False` calls `seam.contest`, not the provider: a fixture planting `max_depth` 0 is refused with the seam's typed `ContestError` (`max_depth reached`, no
    degree), where a call straight to the provider would have resolved the fight; the same fixture at depth 1 resolves. AND the standalone result is the season's for the
    same act, world and seed: the provider's whole return is the one the one-act season's ENCOUNTER got, and the one ladder grades both at one degree.
    FALSIFIER: a standalone run whose result differs from the season's."""
    capped = scene.play(ROLE, {**FIXTURE, "max_depth": 0}, seed=0)
    assert (capped["status"], capped["degree"], capped["refusal"], capped["result"]) == ("DEPTH-CAPPED", None, "max_depth reached", None)
    assert scene.play(ROLE, {**FIXTURE, "max_depth": 1}, seed=0)["status"] == "RESOLVED"
    seen, real = [], resolve_mod.contest
    resolve_mod.contest = lambda *a, **k: (seen.append(real(*a, **k)), seen[-1])[1]
    try:
        for seed in SEEDS:
            seen.clear()
            alone = scene.play(ROLE, FIXTURE, seed=seed)
            season = scene.play(ROLE, FIXTURE, seed=seed, apply=True)
            assert len(seen) == 1 and seen[0] == alone["result"], seed
            assert season["degree"] == alone["degree"], seed
    finally:
        resolve_mod.contest = real
    assert "engaged" in " ".join(alone["not_asked"])      # the record says what a standalone call does not ask (A-63)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# B34.17 -- ONE ROLL, PLAYED (`IS-DICE-01`): `scene.play('social_contest.roll', FIXTURES['roll'])` prints the dice's own record. Lane: the season loop (`in` suite).
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
ROLL_SEEDS = 2000
EFFORT_SEEDS = 200


def _roll_fixture() -> dict:
    return scene.FIXTURES["roll"]


@functools.lru_cache(maxsize=None)
def _dealt() -> tuple:
    """`(degree, printed exact odds, printed obstacle sum, obstacle)` of the roll fixture's `scene.play` at seeds 0..1,999, `apply=False`: the one run the odds test and the
    reach test share."""
    out = []
    for seed in range(ROLL_SEEDS):
        record = scene.play(_roll_fixture()["role"], _roll_fixture(), seed=seed)
        roll = record["roll"]
        out.append((record["degree"], tuple(roll["exact"][band] for band in scene.BAND_ORDER), roll["obstacle"]))
    return tuple(out)


def test_the_roll_fixture_prints_terms_that_sum_to_the_obstacle():
    """The record the fixture prints names every term of the obstacle and the terms sum to the obstacle the roll was thrown at (`roll.py::obstacle`: *the values in
    `terms` sum to `ob`*), at every seed; the pool's parts sum to the pool; the dealt band is one of the four. FALSIFIER: a term left out of the print, or a printed `ob`
    that is not the roll's own, leaves a gap of at least a tenth (the smallest term, `difficulty`, is 0.8)."""
    checked = 0
    for seed in SEEDS:
        record = scene.play(_roll_fixture()["role"], _roll_fixture(), seed=seed)
        roll = record["roll"]
        terms = roll["obstacle"]["terms"]
        assert {"even", "difficulty", "opposition"} <= {name for name, _ in terms}, terms
        assert abs(sum(value for _, value in terms) - roll["obstacle"]["sum"]) <= 1e-9, (seed, terms)
        assert abs(roll["obstacle"]["sum"] - record["result"]["ob"]) <= 1e-9 and roll["obstacle"]["ob"] == record["result"]["ob"], seed
        parts = roll["pool"]["parts"]
        assert abs(max(parts["floor"], parts["skill"] + parts["governing"] + parts["addends"] + parts["base"]) - roll["pool"]["pool"]) <= 1e-9, (seed, parts)
        assert roll["pool"]["pool"] == record["result"]["pool"] and parts["skill"] > 0, seed          # the authored skill score is in the pool
        assert record["degree"] in scene.BAND_ORDER and roll["draw"]["key"], seed
        assert abs(sum(roll["exact"].values()) - 1.0) <= 1e-9, seed
        checked += 1
    assert checked == len(SEEDS), checked


def test_printed_odds_match_realised_bands():
    """The exact odds the record prints (`sigma_leverage.band_odds` over the roll's own pool, obstacle and leverage) are the odds of the bands the same call deals, over
    2,000 seeds: each band's realised count is within four standard deviations of the sum of the odds printed for it (a Poisson-binomial: each seed is its own world and
    prints its own odds). FALSIFIER: odds printed from another pool or another boost misses a band's count by far more than that."""
    dealt = _dealt()
    assert len(dealt) == ROLL_SEEDS
    for place, band in enumerate(scene.BAND_ORDER):
        expected = sum(odds[place] for _, odds, _ in dealt)
        spread = sum(odds[place] * (1.0 - odds[place]) for _, odds, _ in dealt) ** 0.5
        realised = sum(1 for degree, _, _ in dealt if degree == band)
        assert abs(realised - expected) <= 4.0 * spread, (band, realised, expected, spread)


def test_effort_changes_the_printed_odds_and_some_dealt_band():
    """An act at effort 2 brings two levels FOR the roller (CP-T01-05): at every one of seeds 0..199 the printed exact odds move toward the better bands, and at some seed
    the one dealt draw lands in another band (the draw's key is the same, so the band moves only by the shifted odds). FALSIFIER: an effort the print or the roll ignores."""
    role, checked, moved = _roll_fixture()["role"], 0, 0
    for seed in range(EFFORT_SEEDS):
        plain = scene.play(role, scene.staged(_roll_fixture(), effort=0), seed=seed)
        pushed = scene.play(role, scene.staged(_roll_fixture(), effort=2), seed=seed)
        assert plain["roll"]["draw"]["key"] == pushed["roll"]["draw"]["key"], seed
        assert pushed["roll"]["exact"][scene.BAND_ORDER[-1]] > plain["roll"]["exact"][scene.BAND_ORDER[-1]], seed
        assert pushed["roll"]["exact"][scene.BAND_ORDER[0]] < plain["roll"]["exact"][scene.BAND_ORDER[0]], seed
        moved += pushed["degree"] != plain["degree"]
        checked += 1
    assert checked >= EFFORT_SEEDS and moved > 0, (checked, moved)


def test_each_band_is_reached_and_each_writes():
    """All four bands are dealt within seeds 0..1,999, and at the first seed of each the one-act season (`apply=True`) folds the SAME band and the world carries a write
    of that act beyond the scene's budget (which is the driver's, not the world's): the verb's declared write where its row declares one at the band (`Tenure.since`: a
    `detain` edge), and at every band the claims its witnesses deposited. FALSIFIER: a band whose act leaves the world as it was."""
    role, row = _roll_fixture()["role"], scene.VERB_TABLE[_roll_fixture()["act"]["verb"]]
    first = {}
    for seed, (degree, _, _) in enumerate(_dealt()):
        first.setdefault(degree, seed)
    assert set(first) == set(scene.BAND_ORDER), sorted(first)
    for band, seed in first.items():
        folded = scene.play(role, _roll_fixture(), seed=seed, apply=True)
        assert folded["degree"] == band and folded["status"] == "FOLDED", (band, seed, folded["status"], folded["degree"])
        wrote = folded["wrote"]
        assert wrote["durable"] and wrote["deposited"] > 0, (band, wrote)
        assert bool(wrote["changes"]) == bool(row.writes_by_degree[band]), (band, wrote["changes"], row.writes_by_degree[band])
