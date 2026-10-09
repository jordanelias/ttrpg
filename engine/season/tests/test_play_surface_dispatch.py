"""v9 PC-06 `S-1`: the dispatching `choose` (`harness/play_surface.py`), held by a hash.

FALSIFIER (the plan's, two-sided):
  * the CONTROL — a callback replaying `make_chooser`'s own pick leaves `World.content_hash()`
    equal to the shipped `headless.run` on the same seed, and the callback demonstrably ran;
  * the PLANTED DEVIATION — one person's callback returns a different legal pick from that person's
    own options, and the hash moves.
Each side alone is satisfiable by a seam that does nothing (the control) or by one that breaks every
run (the deviation); the pair is what observes a working dispatch.
"""
from __future__ import annotations

from types import SimpleNamespace

from engine.season.decision import make_chooser
from engine.season.harness import headless
from engine.season.harness.play_surface import dispatching_chooser
from engine.season.loop.driver import SeasonDriver, resolvable_verbs
from engine.season.state.ids import H, draw_factory

SEED, SEASONS = 0, 2
# A test parameter, not a branch in the seam: the seam names nobody. Carin is the person
# `headless` was built around, so her season is the one most certain to deliberate.
WHO = headless.CARIN


def _acts(picked) -> list:
    """The Acts in a `choose` return, in order — it may hold Scenes (`W17`) or bare Acts."""
    out = []
    for item in picked:
        out.extend(getattr(item, "acts", None) or [item])
    return out


def _run(overrides_for):
    """`headless.run`'s season loop with the chooser routed through the seam. `overrides_for`
    receives the world's `(fx, mint, foldable, draw)` and returns the `{person id: callback}` map,
    so a callback can build a chooser over the same clock the delegate uses."""
    w = headless.build_world(SEED)
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    draw = draw_factory(w.world_seed, lambda: w.tick)
    foldable = resolvable_verbs()
    auto = make_chooser(w.fixtures, mint, verbs=foldable, draw=draw)
    choose = dispatching_chooser(auto, overrides_for(w.fixtures, mint, foldable, draw))
    for _ in range(SEASONS):
        d.season(choose, None, headless.subsistence,
                 contest_max_depth=w.fixtures.get("contest_max_depth"))
    return w, d


def test_s1_a_callback_replaying_the_choosers_own_pick_leaves_the_hash_equal():
    """The control. The baseline is the SHIPPED harness's run, not a second copy of this file's
    construction, so a seam that perturbs the run in any way is visible against code it did not
    write."""
    calls = {"n": 0, "acts": 0}

    def replay(p, v, s, ask_budget, auto):
        picked = auto(p, v, s, ask_budget)
        calls["n"] += 1
        calls["acts"] += len(_acts(picked))
        return picked

    w, _ = _run(lambda *_: {WHO: replay})
    # §0.1 pt 2: the equality below is vacuous unless the callback was dispatched and its replayed
    # pick carried something — an empty pick would equal the plain run only if nobody acted.
    assert calls["n"] >= 1, "the callback was never dispatched"
    assert calls["acts"] >= 1, "every replayed pick was empty; the control observed nothing"
    assert w.content_hash() == headless.run(SEASONS, SEED)["hash"]


def test_s1_a_planted_deviation_for_one_person_moves_the_hash():
    """The deviation is a LEGAL pick from the person's own options, chosen by the owner of the
    pick: `make_chooser` over the same clock with the verb `auto` ranked first withheld. So the
    person still triages within their own budget, from their own candidate set, and simply does
    not do what the policy would have done first."""
    seen = {"n": 0, "deviated": 0}

    def overrides_for(fx, mint, foldable, draw):
        def deviate(p, v, s, ask_budget, auto):
            seen["n"] += 1
            own = _acts(auto(p, v, s, ask_budget))
            if not own:
                return []
            other = make_chooser(fx, mint, verbs=foldable - {own[0].verb}, draw=draw)
            picked = other(p, v, s, ask_budget)
            if [a.verb for a in _acts(picked)] != [a.verb for a in own]:
                seen["deviated"] += 1
            return picked
        return {WHO: deviate}

    w, d = _run(overrides_for)
    assert seen["n"] >= 1 and seen["deviated"] >= 1, seen
    plain = headless.run(SEASONS, SEED)
    assert w.content_hash() != plain["hash"]
    # And the move is the overridden person's: their realised verbs differ from the plain run's.
    mine = sorted(a.verb for a in d.resolved if a.actor == WHO)
    w0, d0 = _run(lambda *_: {})
    assert w0.content_hash() == plain["hash"]          # the empty map IS the shipped run
    assert mine != sorted(a.verb for a in d0.resolved if a.actor == WHO)


def test_s1_the_seam_routes_by_person_id_and_hands_the_callback_no_world():
    """The dispatch itself, on stubs: an overridden id reaches its callback with DELIBERATE's four
    arguments plus the delegate, and every other id reaches the delegate with exactly four."""
    log = []
    auto = lambda p, v, s, ask_budget: log.append(("auto", p.id, (v, s, ask_budget))) or ["a"]

    def cb(p, v, s, ask_budget, delegate):
        log.append(("cb", p.id, (v, s, ask_budget)))
        assert delegate is auto
        return ["c"]

    choose = dispatching_chooser(auto, {"p_x": cb})
    budget = lambda: 3
    assert choose(SimpleNamespace(id="p_x"), "V", "S", budget) == ["c"]
    assert choose(SimpleNamespace(id="p_y"), "V", "S", budget) == ["a"]
    assert log == [("cb", "p_x", ("V", "S", budget)), ("auto", "p_y", ("V", "S", budget))]
