"""B09.13 -- THE CHOOSER'S OBSERVER HOOK (`make_chooser(..., watch=None)`), and the one owner of "what the chooser saw".

`watch(p, q, ranked, terms, sampled)` is called once per deliberation after the order is sampled and before it is
packed. It is an OBSERVER (the rule of ED-IN-0225): the chooser ignores its return value and hands it COPIES of its
lists, so a watcher that mutates changes nothing that is packed. Three claims, each executed and each able to fail:

  1. a RECORDING watcher leaves `World.content_hash()` equal to `watch=None` (seed 0 here; seeds 1-2 under `slow`);
  2. a REORDERING watcher -- one that reverses, sorts and empties what it was handed, in place -- changes no act. This
     is the claim that fails if the hook is a steering surface: handing the watcher the chooser's own `sampled` list
     (MUTATION, run at the commit: `watch(p, q, ranked, terms, sampled)` without the `list(...)` copies) reddens it;
  3. `decision_spread`'s deciding-term counts are EQUAL through the hook and through the second-scoring wrapper it
     replaced (`attribute_top` re-scoring the chooser's opening set), deliberation by deliberation.
"""
from __future__ import annotations

from collections import Counter
from types import SimpleNamespace

import pytest

from engine.substrate.descriptors import PURSUITS

from ..boot.realm import build_realm
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.verbs import VERB_TABLE
from ..decision import choose as CH
from ..decision import opening_set
from ..harness import decision_spread as DS
from ..harness import probes as P
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..state.carriers import Candidate, Person
from ..state.ids import draw_factory


def _play(seed: int, seasons: int, watch=None, wrap=None):
    """`populated.run`'s composition over `build_realm(seed)`, the chooser built with `watch`; `wrap(real)` may
    wrap the resulting chooser (a reader that needs the View or the returned scenes). Returns `(world, driver)`."""
    w = build_realm(seed)
    d = SeasonDriver(w)
    ch = P.chooser(w, verbs=resolvable_verbs(), watch=watch)
    ch = ch if wrap is None else wrap(ch, w)
    for _ in range(seasons):
        d.season(ch, question=None, contest_max_depth=w.fixtures.get("contest_max_depth"))
    return w, d


def _recorder():
    calls: list = []

    def watch(p, q, ranked, terms, sampled):
        calls.append((p.id, q, list(ranked), list(terms), list(sampled)))
    return watch, calls


def _scramble(p, q, ranked, terms, sampled):
    """A watcher that does every thing to its arguments a steering surface would: reorders them in place, empties
    them, and returns a list for the chooser to take if it were listening."""
    ranked.reverse()
    sampled.sort(key=lambda c: (c.verb, c.subject or ""), reverse=True)
    terms.clear()
    sampled.clear()
    ranked.clear()
    return [None]


def _acts(w, d):
    return [(a.id, a.actor, a.verb) for a in w.acts], [a.id for a in d.resolved]


def _hash_arm(seed: int) -> None:
    rec, calls = _recorder()
    off, _ = _play(seed, 2)
    on, _ = _play(seed, 2, watch=rec)
    assert len(calls) > 100, f"the recorder saw {len(calls)} deliberations: the hook did not run"
    assert on.content_hash() == off.content_hash()


def test_a_recording_watcher_leaves_the_hash_equal():
    _hash_arm(0)


@pytest.mark.slow
@pytest.mark.parametrize("seed", [1, 2])
def test_a_recording_watcher_leaves_the_hash_equal_other_seeds(seed):
    _hash_arm(seed)


def _hand_built(monkeypatch, n=8):
    """One person, one question, `n` candidates and a `pack_scenes` spy keeping what it was handed: the deliberation
    reduced to the hook's own seam. Returns `(chooser factory, seen)`."""
    cands = [Candidate(v, "p_watch_x") for v in sorted(VERB_TABLE)[:n]]
    monkeypatch.setattr(CH, "opening_set", lambda person, view, q, fx: list(cands))
    seen: dict = {}

    def spy(person, ranked, budget, fx, mint, occasion=None):
        seen["packed"] = [(c.verb, c.subject) for c in ranked]
        return []
    monkeypatch.setattr(CH, "pack_scenes", spy)
    return cands, seen


def _deliberate(chooser, i: int):
    p = Person(id=f"p_watch_{i}", name=f"p_watch_{i}")
    p.pursuits = {PURSUITS[i % len(PURSUITS)]: 1.0, PURSUITS[(i + 3) % len(PURSUITS)]: 0.5}
    chooser(p, SimpleNamespace(question=object()), SimpleNamespace(), lambda: 1)
    return p


def test_the_hook_runs_once_per_deliberation_with_parallel_lists_and_the_packed_order(monkeypatch):
    _, seen = _hand_built(monkeypatch)
    rec, calls = _recorder()
    draw = draw_factory(0, lambda: 0)
    chooser = CH.make_chooser(DEFAULT_FIXTURES, lambda *a: "act", draw=draw, watch=rec)
    for i in range(len(PURSUITS)):
        before = len(calls)
        p = _deliberate(chooser, i)
        assert len(calls) == before + 1, "the hook must run exactly once per deliberation"
        pid, q, ranked, terms, sampled = calls[-1]
        assert pid == p.id and q is not None
        assert len(ranked) == len(terms) == len(sampled) == 8
        assert sorted(map(id, ranked)) == sorted(map(id, sampled))
        assert all(len(t) == 3 for t in terms)
        # the terms are the ranked candidates' own, in rank order: the score is their sum, descending
        totals = [CH.score_total(t) for t in terms]
        assert totals == sorted(totals, reverse=True)
        assert [(c.verb, c.subject) for c in sampled] == seen["packed"], "`sampled` is the order that is packed"
    assert len(calls) == len(PURSUITS) >= 15


def test_a_reordering_watcher_changes_no_act(monkeypatch):
    # (a) the seam: what `pack_scenes` is handed is the same with a scrambling watcher as with none
    _, seen = _hand_built(monkeypatch)
    draw = draw_factory(0, lambda: 0)
    plain = CH.make_chooser(DEFAULT_FIXTURES, lambda *a: "act", draw=draw)
    scrambled = CH.make_chooser(DEFAULT_FIXTURES, lambda *a: "act", draw=draw, watch=_scramble)
    checked = 0
    for i in range(len(PURSUITS)):
        _deliberate(plain, i)
        without = seen.pop("packed")
        _deliberate(scrambled, i)
        assert seen.pop("packed") == without, i
        assert len(without) == 8
        checked += 1
    assert checked >= 15
    monkeypatch.undo()
    # (b) the realm: two seasons through a scrambling watcher leave every act, and the hash, as watch=None left them
    off, doff = _play(0, 2)
    on, don = _play(0, 2, watch=_scramble)
    assert len(on.acts) > 100, "the realm season made no acts: the equality below would prove nothing"
    assert _acts(on, don) == _acts(off, doff)
    assert on.content_hash() == off.content_hash()


def test_decision_spread_counts_equal_through_hook_and_wrapper():
    """THE OLD WRAPPER, kept here as the control: re-score the chooser's opening set, narrowed as it narrows, through
    `attribute_top` (a second scoring). THE HOOK: `choose.deciding_term` over what the chooser itself ranked. The two
    read every deliberation of one season side by side and must agree on each, so the counts are equal."""
    foldable = resolvable_verbs()
    tau = {}
    hooked: list = []
    wrapped: list = []

    def watch(p, q, ranked, terms, sampled):
        hooked.append((p.id, CH.deciding_term(ranked, terms, sampled[0] if sampled else None, tau["v"])))

    def wrap(real, w):
        draw = draw_factory(w.world_seed, lambda: w.tick)
        tau["v"] = float(w.fixtures.get("choice_temperature"))

        def old(p, v, s, ask_budget):
            scenes = real(p, v, s, ask_budget)
            q = getattr(v, "question", None)
            if q is not None:
                cands = [c for c in opening_set(p, v, q, w.fixtures) if c.verb in foldable]
                wrapped.append((p.id, DS.attribute_top(p, cands, w.fixtures, draw, getattr(v, "odds", None))))
            return scenes
        return old

    _play(0, 1, watch=watch, wrap=wrap)
    assert len(hooked) == len(wrapped) > 300, (len(hooked), len(wrapped))

    def key(r):
        return (r["decider"], r["margin"], r["draw_kind"], r["field_zero"],
                None if r["top"] is None else (r["top"].verb, r["top"].subject))
    differing = [(a[0], key(a[1]), key(b[1])) for a, b in zip(hooked, wrapped) if a[0] != b[0] or key(a[1]) != key(b[1])]
    assert not differing, differing[:3]
    tally = Counter(r["decider"] for _, r in hooked)
    assert tally == Counter(r["decider"] for _, r in wrapped)
    assert len(tally) >= 2 and tally["draw"] > 0, f"the season read only {dict(tally)}: the counts proved nothing"
    # and `play_season`, which reads the hook, reports the figures the wrapper's tally gives
    split_old = DS.new_split()
    for pid, r in wrapped:
        DS.tally_split(split_old, pid, r)
    split_new = DS.play_season(build_realm(0), 1)["split"]
    assert split_new == DS.split_figures(split_old)
