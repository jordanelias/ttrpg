"""B34.15 -- ONE SCENE CONTRACT: a registered module is a season call and a playable scene by the same entry (`01_CORE_one_scene_contract` edits 1, 2, 4).

What is built: `PlayHost.deciders` and `decider_for` (a decider per module role), `seam/wrappers/_entry.py::played_by` (the party test, once), and `harness/scene.py::play`,
the module's scene run alone from a small world. The world here is `FIXTURES["fight_headless"]` (Carin's three people, a `fight` between the first two): the `duel`
fixture is HELD (`hole_register.yaml` H-580, its builder retired unbuilt), so nothing below stages it. The hearing's arm of gate 3 is
`test_sc_hearing_negotiation.py::test_scripted_player_reproduces_auto_hash` (the same `played_by`, a deviating decider moving the sitting). The nesting-cap test
(`test_a_duel_round_called_from_a_battle_may_not_call_a_third_scene`) is B30's. Lane: the season loop, placed in the `in` suite (`references/season_test_suites.yaml`).
"""
from __future__ import annotations

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
