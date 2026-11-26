"""v10 REM-31 (IN-46): THE GRID MODE'S SUSPENSION AT ENCOUNTER -- the falsifiers and the control, executed.

What is built (`loop/driver.py::SeasonDriver.season`'s `host`, `seam/wrappers/combat.py::resolve`'s party test,
`modules/combat/fight.py::fight` and `wrapper.fight`'s `decide`): every fight is declared at RESOLVE and fought at
ENCOUNTER (`the body`'s `step:`/`declares:`, `rosters.yaml`), and a PLAYABLE host's per-turn decider is handed to the
engine's own turn loop for a fight one of whose claimants the host plays. The design is
`proposals/2026-10-07-grid-mode-suspension.md` (PROPOSED, held back); reference only -- these runs are the mechanism's
evidence.

THE FALSIFIER (the design's three arms on the shipped `build_realm(0)`, one round of two hand-built `fight` acts):
  1. AUTOMATED (no host);
  2. PLAYABLE, a decider engaging every turn;
  3. PLAYABLE, a decider withdrawing after turn 1.
  `hash(1) == hash(2)`, `hash(3) != hash(1)`, equal `mint_token` counts in 1 and 2, and arm 2 must have SUSPENDED --
  a multi-turn fight among them, or arm 3 could not differ (`CLAUDE.md` §0.1 pt 2). A suspension that consumes a draw
  or mints a token reds the first clause: both mutations are run and must be seen.

THE FIGHTS ARE HAND-BUILT, AND THE WORLD IS THE SHIPPED ONE. This file once reverted three shipped changes (CR-87,
CR-85, CP-T03-04) to get a played season whose fights ran two turns or more. On the shipped tree a played season's one
suspended fight ends at turn 1 (measured: no suspended fight runs two turns, so the withdrawing arm could not differ),
so the arms fold two `fight` acts at RESOLVE and ENCOUNTER on the shipped `build_realm(0)` -- the form
`test_aperture.py`'s CR-14 death census uses -- and nothing is reverted. The permutation arms stay whole-season, with
every person played, on the shipped tree.

THE PERMUTATION FALSIFIER (`04` PART D row 41a, rem-02 rev 2): DELIBERATE's per-person map runs the chooser -- and
through it the host's callback -- so the order it visits persons (`loop/deliberate.py::deliberation_order`) is
shuffled, and the `Scene` set and the season hash must be identical, PLAYABLE on; the control is the same shuffle with
PLAYABLE off; the mutation is a callback writing shared state, which must red it.
"""
from __future__ import annotations

import functools
import random

from engine.dice_engine import draw
from engine.season.data.matrix import Step, WriteClass
from engine.season.decision import make_chooser
from engine.season.harness.play_surface import dispatching_chooser
from engine.season.boot.realm import build_realm
from engine.season.loop import deliberate as deliberate_mod
from engine.season.loop import driver as driver_mod
from engine.season.loop.driver import SeasonDriver, resolvable_verbs
from engine.season.queries.inputs import PlayHost
from engine.season.state.carriers import Act
from engine.season.state.ids import H, draw_factory

SEED = 0
# Two disjoint fights between persons of `build_realm(0)`: each runs three turns or more when both engage (5 and 6 turns,
# read at BA1.99 on the authored cast, `PYTHONHASHSEED=0`), and they share no claimant, so a host playing one claimant leaves the
# other AUTOMATED. BA1.99 re-pin (BA1.01's authored `stats:` and `capabilities:`): the pairs this file held (p_npc_035 against
# p_npc_072, p_npc_005 against p_npc_083) each ended at turn 1 on the authored cast, so no suspended fight ran two turns; the
# pairs now are the scan's, by a round-robin of every person against every other, the seed unmoved (0).
FIGHTS = (("p_npc_005", "p_npc_036"), ("p_npc_041", "p_npc_039"))


def _scripted(p, v, s, ask_budget, auto):
    """PLAYABLE's chooser callback with scripted choices EQUAL TO THE CHOOSER'S: the delegate's own pick."""
    return auto(p, v, s, ask_budget)


def _season(played=None, decider=None, callback=_scripted, shuffle=False):
    """One season on `build_realm(SEED)`. `played` None is AUTOMATED (no host, the plain chooser). `decider` is a
    factory `(w, record) -> (CombatRoundView) -> str`, so a mutation can close over the world. Returns
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
    scenes = frozenset((sc.id, sc.actor, tuple((a.id, a.verb) for a in sc.acts)) for sc in d.w.acts.scenes())
    return w.content_hash(), scenes, record["mints"], record


def _round(played=None, decider=None):
    """One round of `FIGHTS` on `build_realm(SEED)`: each a hand-built `fight` act, declared at RESOLVE and fought at
    ENCOUNTER with the host that `SeasonDriver.season` hands ENCOUNTER, the round's events logged as it logs them. Same
    return shape as `_season`; `record` also carries the kinds RESOLVE declared, the kinds ENCOUNTER produced and
    the world's draw ordinal at the end."""
    w = build_realm(SEED)
    d = SeasonDriver(w)
    record = dict(calls=[], mints=0)
    host = None if played is None else PlayHost(frozenset(played), decider(w, record))
    real_mint = driver_mod.mint_token

    def counting_mint(world, wclass):
        record["mints"] += 1
        return real_mint(world, wclass)

    driver_mod.mint_token = counting_mint
    try:
        md = w.fixtures.get("contest_max_depth")
        acts = [Act(id=f"rem31_{i}", actor=a, verb="fight", payload={"subject": b}) for i, (a, b) in enumerate(FIGHTS)]
        declared = d.resolve(driver_mod.mint_token(w, WriteClass.ACTS), acts, md)
        fought = d.encounter(driver_mod.mint_token(w, WriteClass.ACTS), declared, md, host)
    finally:
        driver_mod.mint_token = real_mint
    w.log.extend(declared + fought)
    record["declared"], record["fought"] = [e.kind for e in declared], [e.kind for e in fought]
    # the draw ordinal is not hashed, and no later draw follows one round; a suspension that consumed one is seen here
    record["draw_after"] = w.draw
    scenes = frozenset((sc.id, sc.actor, tuple((a.id, a.verb) for a in sc.acts)) for sc in d.w.acts.scenes())
    return w.content_hash(), scenes, record["mints"], record


def _engage(w, record):
    def decide(view):
        record["calls"].append((view.claimants, view.round, w.draw, record["mints"]))
        return "engage"
    return decide


def _withdraw_after_first(w, record):
    def decide(view):
        record["calls"].append((view.claimants, view.round, w.draw, record["mints"]))
        return "engage" if view.round == 1 else "withdraw"
    return decide


@functools.lru_cache(maxsize=None)
def _automated(shuffle=False):
    """A whole AUTOMATED season: the control of the permutation arms."""
    return _season(shuffle=shuffle)


@functools.lru_cache(maxsize=None)
def _automated_round():
    return _round()


@functools.lru_cache(maxsize=None)
def _everyone_engaging():
    """Every person played, engaging every turn: the census of the fights a host can suspend, and itself an equal arm."""
    return _round(played=tuple(build_realm(SEED).persons), decider=_engage)


@functools.lru_cache(maxsize=None)
def _played():
    """The person the PLAYABLE arms play: a claimant of the longest suspended fight (ties by id), read off the census."""
    calls = _everyone_engaging()[3]["calls"]
    assert calls, "no fight reached the engine at ENCOUNTER: the falsifier would be vacuous"
    longest = max(t for _, t, _, _ in calls)
    return tuple(sorted({c for cl, t, _, _ in calls if t == longest for c in cl})[:1])


@functools.lru_cache(maxsize=None)
def _playable(decider=_engage):
    return _round(played=_played(), decider=decider)


@functools.lru_cache(maxsize=None)
def _played_season(shuffle=False):
    """A whole season with every person played: each person's callback runs in DELIBERATE's map."""
    return _season(played=tuple(build_realm(SEED).persons), decider=_engage, shuffle=shuffle)


def test_every_fight_is_declared_at_resolve_and_fought_at_encounter():
    """The precondition (§1): `the body` carries `march`'s pair, so the deferral is the same in both modes. And on the
    shipped `build_realm(0)` each hand-built `fight` is DECLARED by RESOLVE and has no outcome until ENCOUNTER."""
    from engine.season import manifest
    row = manifest.resolve("contest", "the body")
    assert (row["step"], row["declares"]) == ("ENCOUNTER", "Declared")
    _, _, _, rec = _automated_round()
    assert rec["declared"].count("fight.declared") == len(FIGHTS), rec["declared"]
    assert "person.died" not in rec["declared"], "a fight was fought at RESOLVE, not deferred"
    assert "person.died" in rec["fought"], "ENCOUNTER fought no fight to an end"


def test_automated_and_playable_with_equal_choices_end_at_one_hash():
    auto_hash, auto_scenes, auto_mints, _ = _automated_round()
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
    assert rec["draw_after"] == census["draw_after"] == _automated_round()[3]["draw_after"]


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
    auto_hash = _automated_round()[0]
    withdraw_hash, _, _, rec = _playable(decider=_withdraw_after_first)
    assert any(t == 2 for _, t, _, _ in rec["calls"]), "the withdrawing decider was never asked at turn 2"
    assert withdraw_hash != auto_hash


def test_the_deliberation_order_does_not_move_the_scene_set_or_the_hash_playable_on():
    play = _played_season()
    shuffled = _played_season(shuffle=True)
    assert shuffled[1] == play[1] and shuffled[0] == play[0]


def test_control_the_same_permutation_with_playable_off():
    auto, shuffled = _automated(), _automated(shuffle=True)
    assert shuffled[1] == auto[1] and shuffled[0] == auto[0]


def test_the_decider_must_answer_from_the_closed_set():
    import pytest
    def bad(w, record):
        return lambda view: "flee"
    with pytest.raises(ValueError, match="not one of"):
        _round(played=_played(), decider=bad)


def _round_from_key(key, r):
    """ROUND `r`'S DRAW, the law spelled out of the engine's own primitives and NOT through the module's `round_draw` (B16.03, PB 2, A-30): the fight's key is
    `H2(<the Draw's key>, "fight:0")` (a fresh `Draw` sits at position 0 when the fight takes its one uniform), the round's `H2(<fight key>, "round:<r>")`. A test
    that called the module's own functions would agree with any `round_draw` that ignored `r`; this one does not."""
    return draw.seeded(draw.H2(draw.H2(key, "fight:0"), f"round:{r}"))


def test_twelve_round_calls_equal_one_fight():
    """B16.01 (PB step 1, PCR-2): `fight` is the loop over `fight_round`. Three hand-built records (the second a longsword against
    plate, the case in which a weapon form is in hand at a round's end; the third unequal ends): the rounds called BY HAND, each handed the
    `DuelState`s and the measure the last one returned, on the one stream, are the fight in one call -- the same events round for round, the same
    wounds at the end, and the same number of draws taken from the stream. FALSIFIER: a state the round does not carry (the hand loop then
    fights another fight), a draw the loop takes that the rounds do not, or a recovery applied where the fight ended."""
    from engine.dice_engine import draw
    from engine.season.queries.inputs import DuelRoundInput, DuelState, PersonalCombatInput
    from engine.substrate import composition
    fight, fight_round = composition.require("combat.fight"), composition.require("combat.round")
    qs = ("felled", "wounds", "max_wounds", "health_remaining", "health_full")
    cases = ((7, (4, 4), ()), (11, (4, 4), (("longsword", "heavy"), ("arming", "light"))), (3, (3, 5), (("spear", "light"), ("mace", "medium"))))
    rounds_seen = 0
    for seed, ends, kits in cases:
        inp = PersonalCombatInput(claimants=("p_a", "p_b"), ends=ends, wound_quantities=qs, kits=kits)
        key = draw.H2("test_twelve_round_calls", seed)
        whole_rng = draw.seeded(key)
        whole = fight(inp, whole_rng)
        states, prev_closed, hand, out = (DuelState(), DuelState()), False, [], None
        for r in range(1, 13):
            out = fight_round(DuelRoundInput(fighters=inp, states=states, plans=({}, {}), round=r, prev_closed=prev_closed), _round_from_key(key, r))
            hand.extend(out.trace)
            states, prev_closed = out.states, out.closed
            if out.felled or out.yielded or any(e["kind"] == "fight_result" for e in out.trace):
                break
        engine_events = [e for e in whole.trace if e["kind"] not in ("fight_start", "fight_result")]
        assert hand == engine_events, (seed, "the rounds called by hand are not the fight in one call")
        assert whole_rng.n == 1, (seed, "the fight took more than its one uniform of its own stream: a round draws from its own key (B16.03)", whole_rng.n)
        for pid in inp.claimants:
            assert {q: getattr(whole.wounds[pid], q) for q in qs} == out.wounds[pid], (seed, pid)
        assert whole.rounds == sum(1 for e in hand if e["kind"] == "round_start"), seed
        rounds_seen += whole.rounds
    assert rounds_seen >= 6, f"the three fights ran {rounds_seen} rounds between them: the hand loop is not observing a carried state"


def test_a_fight_in_one_call_equals_the_same_fight_as_separate_round_calls_from_the_key():
    """B16.03 (PB §2, §7 step 2, A-30): round `r` draws from the key `H2(fight_key, "round:<r>")` and nothing else, so it is recomputable from
    `(fight_key, r)` and the `DuelState`s it is handed. Sixteen fights (three kit sets and three end pairs, as `test_twelve_round_calls_equal_one_fight`'s): the fight in one call
    is read round by round (each round's input states and trace); then every round is called AGAIN, last round first, on a fresh keyed `Draw` and no
    other round having been called in that process step, and must return exactly its slice of the fight's trace. FALSIFIER: a round whose draws
    depend on another round's count (the sequential stream: the reverse-order recompute then differs), or a fight that takes a position of its own
    `Draw` beyond its one uniform (`rng.n` past 1)."""
    from engine.dice_engine import draw
    from engine.season.queries.inputs import DuelRoundInput, DuelState, PersonalCombatInput
    from engine.substrate import composition
    fight, fight_round = composition.require("combat.fight"), composition.require("combat.round")
    qs = ("felled", "wounds", "max_wounds", "health_remaining", "health_full")
    kit_sets = ((), (("longsword", "heavy"), ("arming", "light")), (("spear", "light"), ("mace", "medium")))
    cases = [(seed, ((4, 4), (3, 5), (5, 5))[seed % 3], kit_sets[seed % 3]) for seed in range(16)]
    recomputed = 0
    for seed, ends, kits in cases:
        inp = PersonalCombatInput(claimants=("p_a", "p_b"), ends=ends, wound_quantities=qs, kits=kits)
        key = draw.H2("test_a_round_from_its_key", seed)
        whole_rng = draw.seeded(key)
        whole = fight(inp, whole_rng)
        assert whole_rng.n == 1, (seed, "the fight took more than its one uniform of its own Draw", whole_rng.n)
        rounds, trace = [], [e for e in whole.trace if e["kind"] not in ("fight_start", "fight_result")]
        for e in trace:   # the fight's own trace cut into its rounds
            if e["kind"] == "round_start":
                rounds.append([])
            rounds[-1].append(e)
        assert len(rounds) == whole.rounds, seed
        carried, states, prev_closed = [], (DuelState(), DuelState()), False
        for r in range(1, len(rounds) + 1):   # the states each round was handed: threaded through the rounds' own outcomes
            carried.append((states, prev_closed))
            out = fight_round(DuelRoundInput(fighters=inp, states=states, plans=({}, {}), round=r, prev_closed=prev_closed), _round_from_key(key, r))
            states, prev_closed = out.states, out.closed
        for r in range(len(rounds), 0, -1):   # last round first: no earlier round has been drawn in this pass
            states, prev_closed = carried[r - 1]
            out = fight_round(DuelRoundInput(fighters=inp, states=states, plans=({}, {}), round=r, prev_closed=prev_closed), _round_from_key(key, r))
            expected = [e for e in rounds[r - 1] if e["kind"] != "fight_result"]
            assert [e for e in out.trace if e["kind"] != "fight_result"] == expected, (seed, r, "a round called alone is not that round of the fight")
            recomputed += 1
    assert recomputed >= 12, f"only {recomputed} rounds were recomputed: the test is not observing a keyed round"
