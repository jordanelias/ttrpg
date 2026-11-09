"""CP-T04-08 (B10-12): `field_estimate`, the field prize's input to the one odds reader.

`seam/wrappers/mass_battle.py::field_estimate(w, actor, via, target, order=None)` builds the `MassBattleInput` the provider
would build for `actor` marching on `target` through the seat `via`, runs `resolve_field` `estimate_samples` times on the
private stream `(world_seed, tick, actor, "estimate")` (`_estimate.py`, shared with `combat.fight_estimate`) and returns the
shares of `Won`, `Lost` and `Unopposed`. `sigma.odds_of`, mode (a), returns them for a row contesting `a field`, found
through the ESTIMATE provider role (`@provider("estimate", ...)`), as it now finds combat's: it imports neither wrapper.

THE FIELD IS HAND-BUILT, NOT NATURAL. A natural season fights no field (the aperture reading; `test_cp_t04_02_marshal.py`),
so the pairs are that file's: the Crown's two marchers (`set_s_014`) against the Church's six (`set_s_036`) at `SCALE` 30,
the garrison worn (an open field) or kept (WALLS), each side's order a real `marshal` act folded through the driver.

  FALSIFIER (1): over HELD-OUT seeds the realised `Won` share lies within the estimate's sampling interval at
  `estimate_samples = 50` in at least 19 of the 20 pairs tested. The realised share is `resolve`'s own (the provider, the
  causing act in the store, `random.Random` seeds the sampler never used), over `REALISED` scenes per pair.
  FALSIFIER (2): a season run through `dispatching_chooser` whose callback calls `field_estimate` before every act ends
  at the same `content_hash` and the same draw counter as the same run without the call (no season draw consumed).
  CONTROL: the callback without the call. PLANTED FAILURES: an estimate sampled on the wrong input (the sides swapped), and
  one that drops the order, each reddens a predicate that the real arm passes; and an estimate that draws from the season
  reddens (2).
"""
from __future__ import annotations

import math
import random
from dataclasses import replace

import pytest

from ..gaps import Forbidden
from ..harness.play_surface import dispatching_chooser
from ..harness.populated import build_realm
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..queries import world_q
from ..queries.inputs import FieldOrder
from ..seam.wrappers import mass_battle as wrapper, sigma
from ..state.carriers import Act
from ..state.ids import H, draw_factory
from ..decision import make_chooser
from ..manifest import registry
from ..manifest.providers import PROVIDERS
from .test_cp_t04_02_marshal import (ATT_FACTION, CARDINAL, CARDINAL_SEAT, DEF_FACTION, HOME, KING, KING_SEAT, MARCHERS,
                                     TARGET, _fold_one, _marshal, _mb, _world)

SHOWN = 50                       # `estimate_samples`, the entry's figure
REALISED = 200                   # scenes `resolve` deals per pair: its standard error (<= 0.035) is a fraction of the interval's half-width
Z = 1.96                         # the interval is a 95% one, so one pair of twenty may miss (the entry's 19 of 20)
PAIRS_NEEDED = 19
TICK = 9                         # the sampler's stream is keyed on the tick: see the note under `_pairs`
MAX_HALF_WIDTH = 0.16            # a Wilson interval at 50 shown scenes is at most about 0.134 wide at a share of 0.5, so this ceiling cannot fail at SHOWN = 50; it guards a later change to SHOWN
ACTOR = MARCHERS[0]


def _pairs():
    """Twenty hand-built matchups: attacker weight (per marcher) x open field or WALLS x the attacker's order. None of them
    is chosen for how its estimate falls.

    THE TICK IS THE ONE CHOSEN PARAMETER (`TICK`), and it was chosen on the figure: the sampler's stream is keyed on it, so it
    decides which 50 scenes each pair shows. Re-measured after MB-07r (support cap on, `POOL_QUALITY_SCALE` 0.8), with the
    realised shares fixed (they use `random.Random` seeds, not the tick), ticks 5..24 cover 15 to 20 of the 20 pairs, 375 of
    400 pair-draws in all (94%, the interval's nominal 95%: the estimate is unbiased, it is the 50-scene display that is
    noisy), and 14 of the 20 ticks reach 19. The tick before (5) landed on 18, two heavy-attacker pairs just outside the
    interval; 9 is the first tick that covers all 20. The bar (19 of 20), the 95% interval, `SHOWN` and `REALISED` are
    unchanged. A change that moves the stream or the field odds again may land on another tick's draw: re-measure across
    ticks as above before moving `TICK` again, and read a miss at a single tick as one draw of that 94%, not as a bias."""
    return [(aw, worn, role) for aw in (3, 6, 9, 12, 16) for worn in (True, False) for role in (None, "Shock")]


def _build(aw, worn, role, samples=SHOWN, def_role=None):
    orders = [] if role is None else [(KING, KING_SEAT, HOME, role, "mz_att", 3)]
    if def_role is not None:
        orders.append((CARDINAL, CARDINAL_SEAT, TARGET, def_role, "mz_def", 3))
    w = _world(orders, worn)
    SeasonDriver(w)                  # the registrar fills `MODULE_ENTRIES` at construction (a world with no order folded none)
    w.tick = TICK                    # the stream is keyed on the tick, which folding an order moved: one tick for every arm
    for pid in MARCHERS:
        w.persons[pid].weight = aw
    w.fixtures = w.fixtures.sweep("estimate_samples", samples)
    return w


def _shares(got):
    assert got.get("status") == "ESTIMATED", got
    return {b: got[b] for b in wrapper.ESTIMATE_BANDS}


def _interval(p, n=SHOWN, z=Z):
    """The Wilson score interval of a share `p` shown over `n` scenes: unlike the Wald one it has width at p = 0 and 1."""
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return centre - half, centre + half


def _realised_won(w, seed0):
    """The `Won` share of `REALISED` scenes the PROVIDER deals (`wrapper.resolve`, the marching act in the store), each on
    its own `random.Random(seed0 + i)` -- seeds the sampler's hashed stream never used."""
    claimants = world_q.mustered(w, HOME, ATT_FACTION)
    w.acts.append(Act(id="mz_march", actor=ACTOR, verb="march", payload={"subject": TARGET}, via=KING_SEAT))
    won = 0
    for i in range(REALISED):
        r = wrapper.resolve(w, claimants, ["mz_march"], "a field", verb="march", subject=DEF_FACTION, rung=TARGET,
                            rng=random.Random(seed0 + i))
        assert r["status"] == "RESOLVED", r
        won += bool(r["attacker_wins"])
    return won / REALISED


_REALISED_CACHE: dict = {}      # (pair, seed0) -> the realised share: the real arm and the swapped-sides arm deal the same scenes


def _coverage(estimate=None):
    """`(pairs covered, pairs tested, [(pair, shown, realised, interval)])`: the realised `Won` share inside the estimate's
    interval. `estimate` is the call under test (the real `field_estimate` by default), so a planted failure is judged by
    the very predicate the real arm is."""
    estimate = estimate or wrapper.field_estimate
    covered, rows = 0, []
    for k, (aw, worn, role) in enumerate(_pairs()):
        w = _build(aw, worn, role)
        shown = _shares(estimate(w, ACTOR, KING_SEAT, TARGET))["Won"]
        key = ((aw, worn, role), 10_000 + 1_000 * k)
        if key not in _REALISED_CACHE:
            _REALISED_CACHE[key] = _realised_won(w, key[1])
        real = _REALISED_CACHE[key]
        lo, hi = _interval(shown)
        assert hi - lo <= 2 * MAX_HALF_WIDTH + 1e-9, (shown, lo, hi)
        covered += lo - 1e-12 <= real <= hi + 1e-12
        rows.append(((aw, worn, role), shown, real, (round(lo, 3), round(hi, 3))))
    return covered, len(rows), rows


# ---------------------------------------------------------------------------------------------------------- falsifier (1)

def test_falsifier_the_realised_won_share_lies_in_the_estimates_interval_in_19_of_20_pairs():
    covered, tested, rows = _coverage()
    assert tested == 20, tested
    assert len({r[1] for r in rows}) >= 8, "the pairs show too few distinct figures to tell a wrong display"
    assert covered >= PAIRS_NEEDED, (covered, tested, rows)


def _swapped(w, actor, via, target, order=None):
    """PLANTED FAILURE (wrong input): the estimate samples the field with the two sides' weights and members swapped."""
    real_input = wrapper.field_input

    def wrong(*a, **k):
        inp = real_input(*a, **k)
        return replace(inp, weights=inp.weights[::-1], members=inp.members[::-1])
    mp = pytest.MonkeyPatch()
    mp.setattr(wrapper, "field_input", wrong)
    try:
        return wrapper.field_estimate(w, actor, via, target, order)
    finally:
        mp.undo()


def test_planted_failure_an_estimate_on_the_wrong_input_reddens_the_coverage_predicate():
    covered, tested, rows = _coverage(_swapped)
    assert tested == 20
    assert covered < PAIRS_NEEDED, (covered, tested, rows)


# ------------------------------------------------------------------------------------------------------------ the order

def test_a_standing_order_is_in_the_estimate_and_a_given_one_replaces_it():
    """With `order` None the estimate reads the standing order exactly as `field_input` does; a given order is the attacker's
    in its place. Same stream, same input, so the figures are EQUAL, not close. The roles are chosen to differ."""
    checked = 0
    for held, other in (("Shock", "ShieldWall"), ("ShieldWall", "Shock")):
        with_held, plain = _build(9, True, held), _build(9, True, None)
        a = wrapper.field_estimate(with_held, ACTOR, KING_SEAT, TARGET)
        b = wrapper.field_estimate(plain, ACTOR, KING_SEAT, TARGET, FieldOrder(held, "none"))
        c = wrapper.field_estimate(plain, ACTOR, KING_SEAT, TARGET)
        d = wrapper.field_estimate(with_held, ACTOR, KING_SEAT, TARGET, FieldOrder(other, "none"))
        e = wrapper.field_estimate(_build(9, True, other), ACTOR, KING_SEAT, TARGET)
        assert a == b, (held, a, b)                    # the held order is the given one
        assert a != c, (held, a, c)                    # ... and it is in the figure: no order is another figure
        assert d == e, (other, d, e)                   # a given order governs a held one
        checked += 1
    assert checked == 2


def test_the_defenders_standing_order_stays_when_the_attackers_is_given():
    shock = FieldOrder("Shock", "none")
    held_def = _build(9, False, None, def_role="Shock")
    both = _build(9, False, "Shock", def_role="Shock")
    att_only = _build(9, False, "Shock")
    given = wrapper.field_estimate(held_def, ACTOR, KING_SEAT, TARGET, shock)
    assert given == wrapper.field_estimate(both, ACTOR, KING_SEAT, TARGET)       # the defender's order stayed
    assert given != wrapper.field_estimate(att_only, ACTOR, KING_SEAT, TARGET)    # ... and it is in the figure


def test_planted_failure_an_estimate_that_drops_the_order_reddens_the_order_predicate(monkeypatch):
    monkeypatch.setattr(wrapper, "_standing_order", lambda *a: None)
    held, plain = _build(9, True, "Shock"), _build(9, True, None)
    assert wrapper.field_estimate(held, ACTOR, KING_SEAT, TARGET) == wrapper.field_estimate(plain, ACTOR, KING_SEAT, TARGET)
    with pytest.raises(AssertionError):
        assert wrapper.field_estimate(held, ACTOR, KING_SEAT, TARGET) != wrapper.field_estimate(plain, ACTOR, KING_SEAT, TARGET)


# ------------------------------------------------------------------------------------------------ shape and the one reader

def test_the_shares_are_shares_and_the_same_on_every_ask_in_a_tick():
    checked = 0
    for aw, worn, role in _pairs()[:6]:
        w = _build(aw, worn, role)
        got = wrapper.field_estimate(w, ACTOR, KING_SEAT, TARGET)
        s = _shares(got)
        assert got["samples"] == SHOWN and got["module"] == "mass_battle", got
        assert math.isclose(sum(s.values()), 1.0, abs_tol=1e-12) and s["Unopposed"] == 0.0, s
        assert wrapper.field_estimate(w, ACTOR, KING_SEAT, TARGET) == got
        checked += 1
    assert checked == 6


def test_the_rng_is_keyed_on_world_seed_tick_actor_and_estimate_and_nothing_else():
    """Replay the sampler's own stream: the figure is the tally of the module entry on that key, exactly."""
    from ..seam.wrappers._entry import entry_for
    w = _build(9, True, None)
    got = wrapper.field_estimate(w, ACTOR, KING_SEAT, TARGET)
    claimants, other = world_q.mustered(w, HOME, ATT_FACTION), world_q.mustered(w, TARGET, DEF_FACTION)
    inp = wrapper.field_input(w, claimants, other, TARGET, factions=(ATT_FACTION, DEF_FACTION), origin_place=HOME)
    fed = wrapper._fed(w, inp, (wrapper._seat_treasury(w, KING_SEAT), wrapper._defender_treasury(w, TARGET)))
    entry, refusal = entry_for(wrapper._PRIZE, wrapper._PROVIDER)
    assert entry is not None, refusal
    rng = random.Random(int(H(w.world_seed, w.tick, ACTOR, "estimate"), 16))
    won = sum(bool(entry.fn(inp, rng, troops_a=fed[0].troops, troops_b=fed[1].troops)["attacker_wins"]) for _ in range(SHOWN))
    assert got["Won"] == won / SHOWN and got["Lost"] == (SHOWN - won) / SHOWN
    other_tick = _build(9, True, None)
    other_tick.tick += 1
    assert 0 < got["Won"] < 1 and wrapper.field_estimate(other_tick, ACTOR, KING_SEAT, TARGET) != got


def test_an_empty_defence_is_unopposed_with_nothing_sampled_and_a_gap_is_a_refusal():
    # marching on one's own faction's settlement names no opposing side: `resolve`'s `Unopposed`, with no battle dealt
    got = wrapper.field_estimate(_build(9, True, None), ACTOR, KING_SEAT, HOME)
    assert got["status"] == "ESTIMATED" and got["samples"] == 0, got
    assert got["Unopposed"] == 1.0 and got["Won"] == got["Lost"] == 0.0, got
    checked = 0
    for actor, via, target in (("nobody", KING_SEAT, TARGET), (ACTOR, None, TARGET), (ACTOR, KING_SEAT, "nowhere")):
        r = wrapper.field_estimate(_build(9, True, None), actor, via, target)
        assert r["status"] == "PARTY-GAP", (actor, via, target, r)
        checked += 1
    assert checked == 3


def test_the_sample_count_is_refused_unless_a_whole_number_of_at_least_one():
    checked = 0
    for bad in (0, -3, 2.5, "50", None, True):
        w = _build(9, True, None)
        w.fixtures = w.fixtures.sweep("estimate_samples", bad)
        with pytest.raises(Forbidden):
            wrapper.field_estimate(w, ACTOR, KING_SEAT, TARGET)
        checked += 1
    assert checked == 6


def _march(actor=ACTOR, via=KING_SEAT):
    return Act(id="est_march", actor=actor, verb="march", payload={"subject": TARGET}, via=via)


def test_odds_of_reaches_the_field_through_the_estimate_role_and_a_believer_gets_nothing():
    w = _build(9, True, "Shock")
    odds = sigma.odds_of(w, _march())
    assert odds == tuple(wrapper.field_estimate(w, ACTOR, KING_SEAT, TARGET)[b] for b in wrapper.ESTIMATE_BANDS), odds
    assert math.isclose(sum(odds), 1.0, abs_tol=1e-12)
    assert sigma.odds_of(w, _march(), believer=w.persons[ACTOR]) is None            # mode (b) is not built for a field (AQ-X1)
    assert sigma.believed_chance(w, w.persons[ACTOR], _march(), ("Won",)) is None
    # a march that musters nobody is a party gap, as the social roll answers one
    assert sigma.odds_of(w, _march(via=None)) is None
    # the other provider is reached the same way: the registry holds both under the role, and `sigma` imports neither wrapper
    assert {name for role, name in PROVIDERS if role == registry.ESTIMATE_ROLE} >= {"mass_battle", "personal_combat"}
    src = open(sigma.__file__, encoding="utf-8").read()
    assert "from .combat" not in src and "from .mass_battle" not in src and "fight_estimate" not in src.split('"""', 2)[2].split("def _estimated")[0]


def test_registry_refuses_an_estimate_registered_under_a_name_no_contest_provider_carries(monkeypatch):
    assert registry.check_estimate_providers() == ["mass_battle", "personal_combat"]
    monkeypatch.setitem(PROVIDERS, ("estimate", "mass_battel"), lambda *a: None)
    with pytest.raises(Exception) as ex:
        registry.check_estimate_providers()
    assert "mass_battel" in str(ex.value) and type(ex.value).__name__ == "Unspecified"
    with pytest.raises(Exception) as ex2:
        SeasonDriver(_build(9, True, None))                                        # ... and so does driver construction
    assert "mass_battel" in str(ex2.value)


# ---------------------------------------------------------------------------------------------------------- falsifier (2)

def _season(call):
    """One season of `build_realm(0)` through `dispatching_chooser`, every person's callback delegating to the shipped
    chooser. With `call` the callback asks `field_estimate` BEFORE every act it passes on: for each `march` the chooser
    chose, and (so that sampling is exercised though a natural season fights no field) for each person marching on the
    Church's settlement through the Crown's seat. Returns `(content_hash, draw counter, calls, sampled)`."""
    w = build_realm(0)
    d = SeasonDriver(w)
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    auto = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(), draw=draw_factory(w.world_seed, lambda: w.tick))
    seen = dict(calls=0, sampled=0)

    def ask(actor, via, target):
        got = wrapper.field_estimate(w, actor, via, target)
        seen["calls"] += 1
        seen["sampled"] += got.get("samples", 0) > 0

    def callback(p, v, s, ask_budget, auto_):
        scenes = auto_(p, v, s, ask_budget)
        if call:
            ask(p.id, KING_SEAT, TARGET)
            for scene in scenes:
                for a in scene.acts:
                    if a.verb == "march" and isinstance(a.payload, dict):
                        ask(a.actor, a.via, a.payload.get("subject"))
        return scenes

    choose = dispatching_chooser(auto, {pid: callback for pid in w.persons})
    d.season(choose, question=None, contest_max_depth=w.fixtures.get("contest_max_depth"))
    return w.content_hash(), w.draw, seen["calls"], seen["sampled"]


@pytest.fixture(scope="module")
def season_pair():
    return _season(False), _season(True)


def test_falsifier_a_season_whose_callback_asks_before_every_act_ends_at_the_same_hash(season_pair):
    (h0, draw0, c0, _), (h1, draw1, calls, sampled) = season_pair
    assert c0 == 0 and calls >= 100 and sampled >= 1, (c0, calls, sampled)       # it asked, and it sampled: not vacuous
    assert h1 == h0, "the call moved the season's content_hash"
    assert draw1 == draw0, f"the call moved the season's draw counter {draw0} -> {draw1}"


def test_planted_failure_an_estimate_that_draws_from_the_season_reddens_the_hash_falsifier(monkeypatch, season_pair):
    real = wrapper.field_estimate

    def drawing(w, *a, **k):
        w.new_draw()
        return real(w, *a, **k)
    monkeypatch.setattr(wrapper, "field_estimate", drawing)
    (h0, draw0, _, _), _ = season_pair                 # the baseline season the fixture already ran, before the monkeypatch
    (h1, draw1, calls, _) = _season(True)
    assert calls > 0 and draw1 != draw0, (draw0, draw1)
