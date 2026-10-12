"""v9 PC-06 `M-1` (#445 `05` M-1 / `03` S-4): the combat host adapter returns the scene's trace.

`seam/wrappers/combat.py::resolve` used to reduce the trace the module entry captures
(`modules/combat/fight.py::fight`) to `bouts`; it now returns it as `trace`, beside `bouts`.

EXIT (the plan's): `World.content_hash()` equal before and after on a seeded season. Here the
"before" is an arm whose provider strips `trace` from what it returns, run on the same seed in the
same process, so any path by which the returned trace reaches `World` moves one hash and not the
other. FALSIFIER: the returned trace is non-empty and its `turn_start` count equals `bouts`.

The seeded season is `headless`'s, with S-1's dispatching `choose` (`harness/play_surface.py`) handing
Carin one `fight` against the bailiff: a test parameter, not a branch in any engine file, and the
cheapest seeded season this tree has that reaches the combat provider (the shipped chooser does not
pick `fight` in `headless`).
"""
from __future__ import annotations

import pytest

import engine.season.seam.wrappers  # noqa: F401 -- registers the `contest` providers
from engine.season.decision import make_chooser
from engine.season.harness import headless
from engine.season.harness.play_surface import dispatching_chooser
from engine.season.loop.driver import SeasonDriver, resolvable_verbs
from engine.season.manifest.providers import PROVIDERS
from engine.season.state.carriers import Act
from engine.season.state.ids import H, draw_factory

SEED, SEASONS = 0, 1
KEY = ("contest", "personal_combat")
# The shipped provider, read once at import: a second arm in one test must wrap THIS, not the
# first arm's spy (which would count each fight twice and strip nothing from the first arm).
SHIPPED = PROVIDERS[KEY]


def _season(monkeypatch, keep_trace: bool):
    """One seeded `headless` season in which Carin fights the bailiff; returns the world and every
    dict the combat provider returned, in call order."""
    from engine.season.seam.wrappers import combat as C
    if C.engine() is None:                       # a NAMED gap, never a silent skip
        assert C.load_error(), "the engine is unavailable and the seam reports no reason"
        pytest.skip(f"personal_combat engine unavailable: {C.load_error()}")
    calls: list = []

    def spy(*a, **k):
        out = SHIPPED(*a, **k)
        if not keep_trace:
            out = {k2: v for k2, v in out.items() if k2 != "trace"}
        calls.append(out)
        return out

    monkeypatch.setitem(PROVIDERS, KEY, spy)
    w = headless.build_world(SEED)
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    auto = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                        draw=draw_factory(w.world_seed, lambda: w.tick))

    def fight_the_bailiff(p, v, s, ask_budget, delegate):
        return [Act(id=mint(p.id, "fight", headless.BAILIFF), actor=p.id, verb="fight",
                    payload={"subject": headless.BAILIFF})]

    choose = dispatching_chooser(auto, {headless.CARIN: fight_the_bailiff})
    for _ in range(SEASONS):
        d.season(choose, None, headless.subsistence,
                 contest_max_depth=w.fixtures.get("contest_max_depth"))
    return w, calls


def test_m1_the_returned_trace_is_the_scene_and_bouts_is_its_turn_start_count(monkeypatch):
    _, calls = _season(monkeypatch, keep_trace=True)
    resolved = [c for c in calls if c.get("status") == "RESOLVED"]
    # §0.1 pt 2: every assertion below is per fight, so a season with none would pass vacuously.
    assert resolved, f"the seeded season reached the combat provider {len(calls)} time(s), none RESOLVED"
    for out in resolved:
        trace = out["trace"]
        assert isinstance(trace, list) and trace, out.get("bouts")
        assert sum(1 for e in trace if e.get("kind") == "turn_start") == out["bouts"] >= 1, (
            out["bouts"], [e.get("kind") for e in trace][:12])


def test_m1_returning_the_trace_leaves_the_seeded_seasons_content_hash_equal(monkeypatch):
    w_with, with_calls = _season(monkeypatch, keep_trace=True)
    w_without, without_calls = _season(monkeypatch, keep_trace=False)
    # The control observes a fight in BOTH arms, and the arms differ in exactly the trace.
    assert any(c.get("status") == "RESOLVED" for c in with_calls), with_calls
    assert len(with_calls) == len(without_calls)
    assert all("trace" in c for c in with_calls) and not any("trace" in c for c in without_calls)
    assert w_with.content_hash() == w_without.content_hash()
