"""v10 REM-31 (IN-46): THE GRID MODE'S SUSPENSION AT ENCOUNTER -- the falsifiers and the control, executed.

What is built (`loop/driver.py::SeasonDriver.season`'s `host`, `seam/wrappers/combat.py::resolve`'s party test,
`modules/combat/fight.py::fight` and `wrapper.fight`'s `decide`): every fight is declared at RESOLVE and fought at
ENCOUNTER (`the body`'s `step:`/`declares:`, `rosters.yaml`), and a PLAYABLE host's per-turn decider is handed to the
engine's own turn loop for a fight one of whose claimants the host plays. The design is
`proposals/2026-10-07-grid-mode-suspension.md` (PROPOSED, held back); reference only -- these runs are the mechanism's
evidence.

THE FALSIFIER (the design's three arms on one seed, `build_realm(0)`, one season):
  1. AUTOMATED (no host);
  2. PLAYABLE, a scripted chooser callback returning the chooser's own pick and a decider engaging every turn;
  3. PLAYABLE, a decider withdrawing after turn 1.
  `hash(1) == hash(2)`, `hash(3) != hash(1)`, equal `mint_token` counts in 1 and 2, and arm 2 must have SUSPENDED --
  a multi-turn fight among them, or arm 3 could not differ (`CLAUDE.md` §0.1 pt 2). A suspension that consumes a draw
  or mints a token reds the first clause: both mutations are run and must be seen.

THE PERMUTATION FALSIFIER (`04` PART D row 41a, rem-02 rev 2): DELIBERATE's per-person map runs the chooser -- and
through it the host's callback -- so the order it visits persons (`loop/deliberate.py::deliberation_order`) is
shuffled, and the `Scene` set and the season hash must be identical, PLAYABLE on; the control is the same shuffle with
PLAYABLE off; the mutation is a callback writing shared state, which must red it.
"""
from __future__ import annotations

import functools
import random

from engine.season.data.matrix import WriteClass
from engine.season.decision import make_chooser
from engine.season.harness.play_surface import dispatching_chooser
from engine.season.harness.populated import build_realm
from engine.season.loop import deliberate as deliberate_mod
from engine.season.loop import driver as driver_mod
from engine.season.loop.driver import SeasonDriver, resolvable_verbs
from engine.season.queries.inputs import PlayHost
from engine.season.state.ids import H, draw_factory
from engine.season.tests.test_cr87_violence_contexts import revert_cr87
from engine.season.tests.test_cr85_faculty_replaces_history import revert_cr85
from engine.season.tests.test_cp_t03_04_arms import revert_cp_t03_04

import pytest

SEED = 0


@pytest.fixture(autouse=True)
def _the_world_this_was_measured_on(monkeypatch):
    """v11 CR-87 RE-TOOK THESE READINGS ON THE WORLD THEY WERE MEASURED ON: CR-87's contexts leave no `fight` formed on
    `build_realm(0)` in one season, so no fight reaches ENCOUNTER and every arm here would be vacuous (the census asserts
    it). The suspension is REM-31's and does not read CR-87; it is read with CR-87 at its revert
    (`test_cr87_violence_contexts.py::revert_cr87`, whose own control reproduces the pre-CR-87 hash).
    v11 CR-85 (`faculty` replaces `history` in the pool and the Ob) moves which fights this world forms: with it, every
    fight on the seed involves the played person and the AUTOMATED branch of the party test goes unexercised. So it is
    read at CR-85's revert too (`test_cr85_faculty_replaces_history.py::revert_cr85`, whose own control reproduces the
    pre-CR-85 hash).
    v11 CP-T03-04 (`arms` in the vocation range, a formation mover of every season) is reverted too
    (`test_cp_t03_04_arms.py::revert_cp_t03_04`), so these readings stand on the world they were measured on."""
    revert_cr87(monkeypatch)
    revert_cr85(monkeypatch)
    revert_cp_t03_04(monkeypatch)


def _scripted(p, v, s, ask_budget, auto):
    """PLAYABLE's chooser callback with scripted choices EQUAL TO THE CHOOSER'S: the delegate's own pick."""
    return auto(p, v, s, ask_budget)


def _season(played=None, decider=None, callback=_scripted, shuffle=False):
    """One season on `build_realm(SEED)`. `played` None is AUTOMATED (no host, the plain chooser). `decider` is a
    factory `(w, record) -> (CombatTurnView) -> str`, so a mutation can close over the world. Returns
    `(hash, scene set, mint count, record)`; `record` collects what the decider saw."""
    w = build_realm(SEED)
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    auto = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(), draw=draw_factory(w.world_seed, lambda: w.tick))
    record = dict(calls=[], mints=0)
    host, choose = None, auto
    if played is not None:
        choose = dispatching_chooser(auto, {pid: callback for pid in played})
        host = PlayHost(frozenset(played), decider(w, record))
    real_mint, real_order = driver_mod.mint_token, deliberate_mod.deliberation_order

    def counting_mint(world, wclass):
        record["mints"] += 1
        return real_mint(world, wclass)

    def shuffled(world):
        persons = real_order(world)
        random.Random(1).shuffle(persons)
        return persons

    driver_mod.mint_token = counting_mint
    if shuffle:
        deliberate_mod.deliberation_order = shuffled
    try:
        d.season(choose, None, contest_max_depth=w.fixtures.get("contest_max_depth"), host=host)
    finally:
        driver_mod.mint_token, deliberate_mod.deliberation_order = real_mint, real_order
    scenes = frozenset((sc.id, sc.actor, tuple((a.id, a.verb) for a in sc.acts)) for sc in d.scenes.values())
    return w.content_hash(), scenes, record["mints"], record


def _engage(w, record):
    def decide(view):
        record["calls"].append((view.claimants, view.turn, w.draw, record["mints"]))
        return "engage"
    return decide


def _withdraw_after_first(w, record):
    def decide(view):
        record["calls"].append((view.claimants, view.turn, w.draw, record["mints"]))
        return "engage" if view.turn == 1 else "withdraw"
    return decide


def _draws(w, record):
    """MUTATION: a suspension that consumes a draw (the world's per-tick ordinal) at its first turn."""
    def decide(view):
        if view.turn == 1:
            w.new_draw()
        return "engage"
    return decide


def _mints(w, record):
    """MUTATION: a suspension that mints ENCOUNTER's write class a second time at its first turn."""
    def decide(view):
        if view.turn == 1:
            driver_mod.mint_token(w, WriteClass.ACTS)
        return "engage"
    return decide


@functools.lru_cache(maxsize=None)
def _automated(shuffle=False):
    return _season(shuffle=shuffle)


@functools.lru_cache(maxsize=None)
def _everyone_engaging():
    """Every person played, engaging every turn: the census of the fights a host can suspend, and itself an equal arm."""
    return _season(played=tuple(build_realm(SEED).persons), decider=_engage)


@functools.lru_cache(maxsize=None)
def _played():
    """The person the PLAYABLE arms play: a claimant of the longest suspended fight (ties by id), read off the census."""
    calls = _everyone_engaging()[3]["calls"]
    assert calls, "no fight reached the engine at ENCOUNTER on the seed: the falsifier would be vacuous"
    longest = max(t for _, t, _, _ in calls)
    return tuple(sorted({c for cl, t, _, _ in calls if t == longest for c in cl})[:1])


@functools.lru_cache(maxsize=None)
def _playable(decider=_engage, shuffle=False):
    return _season(played=_played(), decider=decider, shuffle=shuffle)


def test_every_fight_is_declared_at_resolve_and_fought_at_encounter():
    """The precondition (§1): `the body` carries `march`'s pair, so the deferral is the same in both modes."""
    from engine.season import manifest
    row = manifest.resolve("contest", "the body")
    assert (row["step"], row["declares"]) == ("ENCOUNTER", "Declared")
    w = build_realm(SEED)
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    d.season(make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                          draw=draw_factory(w.world_seed, lambda: w.tick)),
             None, contest_max_depth=w.fixtures.get("contest_max_depth"))
    kinds = [e.kind for e in w.log]
    assert kinds.count("fight.declared") + kinds.count("accept.declared") >= 1, "no fight was declared on the seed"


def test_automated_and_playable_with_equal_choices_end_at_one_hash():
    auto_hash, auto_scenes, auto_mints, _ = _automated()
    all_hash, _, all_mints, census = _everyone_engaging()
    play_hash, play_scenes, play_mints, rec = _playable()
    # the arm must not be identical by construction: it SUSPENDED, and a suspended fight ran two turns or more
    assert rec["calls"], "the PLAYABLE arm never entered the suspension"
    assert max(t for _, t, _, _ in rec["calls"]) >= 2, "no suspended fight ran two turns: arm 3 could not differ"
    # the party test: only a fight with a played claimant suspends
    assert all(set(cl) & set(_played()) for cl, _, _, _ in rec["calls"])
    assert len({cl for cl, _, _, _ in census["calls"]}) > len({cl for cl, _, _, _ in rec["calls"]}), \
        "every fight on the seed involves the played person: the AUTOMATED branch of the party test went unexercised"
    assert play_hash == auto_hash and all_hash == auto_hash
    assert play_scenes == auto_scenes
    assert play_mints == auto_mints == all_mints


def test_no_draw_and_no_mint_while_suspended():
    """(f): within each suspended fight, the world's draw ordinal and the mint count stand still across its turns."""
    _, _, _, rec = _playable()
    by_fight: dict = {}
    for cl, turn, draw, mints in rec["calls"]:
        by_fight.setdefault(cl, []).append((turn, draw, mints))
    for cl, seen in by_fight.items():
        runs = []                   # a claimant pair may fight more than once: split at each turn-1 call
        for turn, draw, mints in seen:
            if turn == 1:
                runs.append([])
            runs[-1].append((draw, mints))
        for r in runs:
            assert len(set(r)) == 1, f"{cl}: the draw ordinal or the mint count moved inside one suspension: {r}"


def test_a_differing_scripted_choice_moves_the_hash():
    auto_hash = _automated()[0]
    withdraw_hash, _, _, rec = _playable(decider=_withdraw_after_first)
    assert any(t == 2 for _, t, _, _ in rec["calls"]), "the withdrawing decider was never asked at turn 2"
    assert withdraw_hash != auto_hash


def test_a_suspension_that_consumes_a_draw_or_mints_a_token_reds_the_first():
    """The two mutations the falsifier must be able to see: each breaks `hash(1) == hash(2)` or the equal mint count."""
    auto_hash, _, auto_mints, _ = _automated()
    assert _season(played=_played(), decider=_draws)[0] != auto_hash, "a consumed draw left the hash unmoved"
    assert _season(played=_played(), decider=_mints)[2] != auto_mints, "a second mint left the count unmoved"


def test_the_deliberation_order_does_not_move_the_scene_set_or_the_hash_playable_on():
    play = _playable()
    shuffled = _playable(shuffle=True)
    assert shuffled[1] == play[1] and shuffled[0] == play[0]


def test_control_the_same_permutation_with_playable_off():
    auto, shuffled = _automated(), _automated(shuffle=True)
    assert shuffled[1] == auto[1] and shuffled[0] == auto[0]


def test_mutation_a_callback_writing_shared_state_reds_the_permutation():
    """A callback that writes state shared across persons -- here a counter every played person's callback bumps,
    taking the chooser's pick only on an even count -- makes the map depend on its visit order. Every person is played
    so the shared state is written on every visit; the permutation must see it."""
    shared = {"n": 0}

    def writes_shared(p, v, s, ask_budget, auto):
        shared["n"] += 1
        return auto(p, v, s, ask_budget) if shared["n"] % 2 == 0 else []

    everyone = tuple(build_realm(SEED).persons)
    shared["n"] = 0
    straight = _season(played=everyone, decider=_engage, callback=writes_shared)
    shared["n"] = 0
    permuted = _season(played=everyone, decider=_engage, callback=writes_shared, shuffle=True)
    assert permuted[1] != straight[1] and permuted[0] != straight[0]


def test_the_decider_must_answer_from_the_closed_set():
    import pytest
    def bad(w, record):
        return lambda view: "flee"
    with pytest.raises(ValueError, match="not one of"):
        _season(played=_played(), decider=bad)
