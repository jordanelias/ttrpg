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

import pytest

from engine.season import decision
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


def _run(overrides_for, rule=None):
    """`headless.run`'s season loop with the chooser routed through the seam. `overrides_for`
    receives the world's `(fx, mint, foldable, draw)` and returns the `{person id: callback}` map,
    so a callback can build a chooser over the same clock the delegate uses."""
    w = headless.build_world(SEED)
    if rule is not None:
        w.fixtures = w.fixtures.sweep("question_aggregation_rule", rule)   # BEFORE the chooser
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    draw = draw_factory(w.world_seed, lambda: w.tick)
    foldable = resolvable_verbs()
    auto = make_chooser(w.fixtures, mint, verbs=foldable, draw=draw)
    choose = dispatching_chooser(auto, overrides_for(w.fixtures, mint, foldable, draw))
    for _ in range(SEASONS):
        d.season(choose, None,
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


# ---------------------------------------------------------------------------------------------
# CP-T02-07 -- the seated person sees every question, in order. The View carries the SEPARATE
# questions (`View.questions`, `attention_key` order) beside the one `question` the aggregation rule
# picked or merged; `auto` reads the one, so the shipped run is byte-identical.
#
# FALSIFIER: a callback that builds the View on `questions[0]` and asks `auto` there reproduces the
# shipped hash (the CONTROL); one that builds it on `questions[1]` moves it; and at
# `question_aggregation_rule = all` the callback's merged `question` is not what the list returns.
# ---------------------------------------------------------------------------------------------

def _list_run(index, rule=None):
    """Carin asks `auto` for its proposal on her `index`-th listed question, whenever she has that
    many; with fewer she leaves the pick to `auto` on the View she was handed."""
    seen = {"calls": 0, "on_index": 0}

    def overrides_for(fx, mint, foldable, draw):
        k = fx.get("view_k")

        def cb(p, v, s, ask_budget, auto):
            seen["calls"] += 1
            if len(v.questions) <= index:
                return auto(p, v, s, ask_budget)
            seen["on_index"] += 1
            on = decision.assemble(p, v.questions[index], k, questions=v.questions)
            return auto(p, on, s, ask_budget)
        return {WHO: cb}
    w, d = _run(overrides_for, rule)
    return w, d, seen


def test_cp_t02_07_the_first_question_callback_reproduces_the_shipped_hash():
    """The control. The callback demonstrably ran on a person with a first question, and rebuilding
    the View on `questions[0]` is the View `deliberate` built, so the hash is the shipped one."""
    w, _, seen = _list_run(0)
    assert seen["on_index"] >= 1, seen            # §0.1 pt 2: the arm ran on a real list
    assert w.content_hash() == headless.run(SEASONS, SEED)["hash"]


def test_cp_t02_07_the_second_question_callback_moves_the_hash():
    """The pair to the control: a legal proposal asked of `auto` on the person's SECOND question.
    Carin holds several questions in most deliberations of this seed, so the list is not vacuous."""
    w, d, seen = _list_run(1)
    assert seen["on_index"] >= 1, seen
    assert w.content_hash() != headless.run(SEASONS, SEED)["hash"]


def test_cp_t02_07_the_second_arm_needs_the_list_not_the_picked_question(monkeypatch):
    """The mutation, kept as a test: a View that carries only the picked question gives the
    second-picking callback no second question, so it never runs on one and the hash does NOT move --
    the failure the arm above excludes."""
    real = decision.assemble
    monkeypatch.setattr(
        decision, "assemble",
        lambda p, q, k, rule="recent", questions=(): real(
            p, q, k, rule, (q,) if q is not None else ()))
    w, _, seen = _list_run(1)
    assert seen["calls"] >= 1 and seen["on_index"] == 0, seen
    assert w.content_hash() == headless.run(SEASONS, SEED)["hash"]


def test_cp_t02_07_at_all_the_merged_question_is_not_what_the_list_returns():
    """`all` is a partial carrier: ONE merged `Question` (the union of the referents, under the first
    one's source). The View returns the separate ones, the merge among none of them."""
    rows = []

    def overrides_for(fx, mint, foldable, draw):
        def look(p, v, s, ask_budget, auto):
            if len(v.questions) >= 2:
                rows.append((v.question, v.questions))
            return auto(p, v, s, ask_budget)
        return {WHO: look}
    _run(overrides_for, "all")
    assert rows, "Carin never held two questions under `all`; the arm observed nothing"
    for merged, listed in rows:
        assert merged not in listed
        assert merged.id == f"q:agg:all:{listed[0].id}" and merged.source == listed[0].source
        assert set(merged.referents) == {r for q in listed for r in q.referents}
        assert len({q.id for q in listed}) == len(listed) >= 2


def test_cp_t02_07_a_non_question_in_the_list_is_refused():
    from engine.season.gaps import InstrumentDefect
    with pytest.raises(InstrumentDefect):
        decision.assemble(SimpleNamespace(id="p_x", ledger=[]), None, 3, questions=("q",))
