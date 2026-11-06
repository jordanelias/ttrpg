"""CP-T03-05 -- COMBAT'S ODDS, SAMPLED LIVE FOR THE PLAYER'S DISPLAY (`-08` AM-C-02).

`seam/wrappers/combat.py::fight_estimate` runs the combat module `estimate_samples` times on a private rng and
returns the shares of the four endings (actor felled, subject felled, yielded, undecided); `sigma.odds_of`, mode
(a), returns them for a row contesting `the body`. Read-only: it is the display, no loop calls it.

  FALSIFIER (1): the DISPLAYED shares equal the shares `resolve` REALISES over held-out worlds -- other world
  seeds, other causing acts, so none of the realised scenes shares a seed with the sampler -- within `Z`
  standard errors of their difference. The realised side classifies a scene a DIFFERENT way from the sampler
  (the trackers' `felled` flags and the `surrender` on `resolve`'s dict, not the result's sign), so a swapped
  actor/subject share reads red here.
  FALSIFIER (2): the call consumes no season draw and writes nothing: the draw counter, `content_hash` and a
  one-season run of the realm are those of the control world that never made the call.
  MUTATION (run by hand at the build, reported in the commit body): `w.new_draw()` inside `fight_estimate`
  turns (2) red on the draw counter.
  CONTROL: the same worlds without the call.

EVERY assertion fails as an assertion: an engine run that raises is caught and re-raised as an AssertionError
naming the call (`_ran`), so a crash is never mistaken for a pass or left as a bare traceback.
"""
from __future__ import annotations

import math

from ..harness import populated, probes as P
from ..loop.driver import SeasonDriver
from ..seam.wrappers import combat, sigma
from ..state.carriers import Act

ACTOR, SUBJECT = "p_low", "p_mid"
# body -> `end` on the tiny world's `band_floors["body"]` (800 / 500 / 100): 1000 -> 4, 750 -> 3, 300 -> 2, 50 -> 1
_BODY = {4: 1000, 3: 750, 2: 300, 1: 50}
MATCHUPS = ((4, 4), (4, 1), (1, 4), (3, 2))       # (actor end, subject end)
REALISED = 3000                                     # held-out scenes per matchup
HELD_OUT_SEEDS = (11, 12, 13, 14, 15, 16)           # world seeds the sampler's key (seed 1, tick 0) never used
Z = 4.0                                             # standard errors of the difference a share may stray
# the widest `Z` standard errors of the difference can be (a share of 0.5, 400 shown against `REALISED`): 0.1065.
# A tolerance past it means `Z` or the sample was loosened, and a wrong display would pass.
MAX_TOLERANCE = 0.11


def _ran(what, fn, *a, **k):
    """Run `fn`; an exception becomes an AssertionError naming `what`, never a bare traceback."""
    try:
        return fn(*a, **k)
    except AssertionError:
        raise
    except Exception as e:                                       # noqa: BLE001 -- the point is to catch all
        raise AssertionError(f"{what} raised {type(e).__name__}: {e}") from e


def _world(ends=(4, 4)):
    """The tiny world with a driver built (the registrar fills the combat entry at construction) and the
    two fighters' bodies set to give the wanted `end`s."""
    def build():
        w = P.tiny_world()
        SeasonDriver(w)
        w.persons[ACTOR].body, w.persons[SUBJECT].body = _BODY[ends[0]], _BODY[ends[1]]
        return w
    return _ran("building the world", build)


def _estimate(w):
    got = _ran("fight_estimate", combat.fight_estimate, w, ACTOR, None, SUBJECT, "fight")
    assert got.get("status") == "ESTIMATED", f"fight_estimate refused: {got}"
    return got


def _shares(got) -> tuple:
    return tuple(got[k] for k in combat.ESTIMATE_OUTCOMES)


def _realised(ends) -> tuple:
    """`(shares, n)` over scenes `resolve` deals, classified from the trackers and the surrender, not from the
    result's sign (the sampler's reading)."""
    w = _world(ends)
    tally = dict.fromkeys(combat.ESTIMATE_OUTCOMES, 0)
    per_seed = REALISED // len(HELD_OUT_SEEDS)
    for seed in HELD_OUT_SEEDS:
        w.world_seed = seed
        for i in range(per_seed):
            r = _ran("resolve", combat.resolve, w, [ACTOR, SUBJECT], [f"held{i}"], "the body", verb="fight")
            assert r["status"] == "RESOLVED", r
            felled = {p: r["wound_state"][p]["felled"] for p in (ACTOR, SUBJECT)}
            if r["surrender"] is not None:
                tally["yielded"] += 1
            elif felled[ACTOR] and not felled[SUBJECT]:
                tally["actor_felled"] += 1
            elif felled[SUBJECT] and not felled[ACTOR]:
                tally["subject_felled"] += 1
            else:
                tally["undecided"] += 1
    n = per_seed * len(HELD_OUT_SEEDS)
    return tuple(tally[k] / n for k in combat.ESTIMATE_OUTCOMES), n


def _tolerance(shown, realised, n_shown, n_realised) -> float:
    """`Z` standard errors of the difference of two independent binomial shares, at the pooled share. At a
    pooled share of exactly 0 or 1 the tolerance is 0: both sides must agree exactly (a never-yielding fight
    must display 0 yielded)."""
    pooled = (shown * n_shown + realised * n_realised) / (n_shown + n_realised)
    return Z * math.sqrt(pooled * (1 - pooled) * (1 / n_shown + 1 / n_realised))


def test_the_shares_are_shares_and_sum_to_one():
    checked = 0
    for ends in MATCHUPS:
        w = _world(ends)
        got = _estimate(w)
        shares = _shares(got)
        assert got["samples"] == w.fixtures.get("estimate_samples"), got
        assert all(0.0 <= s <= 1.0 for s in shares), (ends, shares)
        assert math.isclose(sum(shares), 1.0, abs_tol=1e-12), (ends, shares, sum(shares))
        assert _estimate(w) == got, f"{ends}: asking twice in a tick showed two figures"
        checked += 1
    assert checked == len(MATCHUPS), checked


def test_the_displayed_shares_equal_the_realised_shares_within_sampling_over_held_out_seeds():
    checked = 0
    for ends in MATCHUPS:
        w = _world(ends)
        shown = _shares(_estimate(w))
        n_shown = w.fixtures.get("estimate_samples")
        realised, n_real = _realised(ends)
        for name, s, r in zip(combat.ESTIMATE_OUTCOMES, shown, realised):
            tol = _tolerance(s, r, n_shown, n_real)
            assert tol <= MAX_TOLERANCE, f"{ends} {name}: tolerance {tol:.3f} is too wide to tell a wrong display"
            assert abs(s - r) <= tol + 1e-12, (
                f"{ends} {name}: displayed {s:.4f} vs realised {r:.4f}, beyond {Z} standard errors ({tol:.4f})")
            checked += 1
    assert checked == len(MATCHUPS) * len(combat.ESTIMATE_OUTCOMES), checked
    # `yielded` is 0 on both sides by construction until CP-T03-09 passes a yield term (lethal terms only), so those
    # comparisons cannot fail; the felled and undecided shares carry the claim.


def test_the_tolerance_can_fail_a_display_of_a_different_fight():
    """The control that the comparison above is not vacuous: the display of an even fight, set against the
    realised shares of a lopsided one, is OUTSIDE the same tolerance in a felled share."""
    w = _world((4, 4))
    shown = _shares(_estimate(w))
    n_shown = w.fixtures.get("estimate_samples")
    realised, n_real = _realised((4, 1))
    outside = [name for name, s, r in zip(combat.ESTIMATE_OUTCOMES, shown, realised)
               if abs(s - r) > _tolerance(s, r, n_shown, n_real)]
    assert "subject_felled" in outside and "actor_felled" in outside, (
        f"the even fight's display {shown} passes for the lopsided one's realised {realised}: {outside}")


def test_the_sampler_does_not_swap_the_parties():
    """A strong actor against a weak subject fells the subject more often than it is felled; reversed, the
    other way. Read off the display alone, with the actor in the first claimant's place both times."""
    strong = _estimate(_world((4, 1)))
    weak = _estimate(_world((1, 4)))
    assert strong["subject_felled"] > strong["actor_felled"], strong
    assert weak["actor_felled"] > weak["subject_felled"], weak


def test_the_shares_follow_the_trackers_not_the_sign_of_the_result():
    """The control the tolerance cannot be: NO SAMPLING NOISE. The sampler's own stream is replayed here (same key,
    same module entry, same input), each scene is classified the two ways, and (1) the display equals the
    trackers' tally EXACTLY, (2) the result's sign disagrees with the trackers on at least one scene, so the
    exclusion this asserts is one the stream can show (`wrapper.fight` flips the sign in `UPSET_FLOOR` of the
    decided fights and leaves the trackers alone)."""
    import random
    from ..seam.wrappers._entry import entry_for
    from ..state.ids import H
    w = _world((4, 1))
    got = _estimate(w)
    entry, refusal = entry_for(combat._PRIZE, combat._PROVIDER)
    assert entry is not None, refusal
    inp = _ran("combat_input", combat.combat_input, w, [ACTOR, SUBJECT])
    rng = random.Random(int(H(w.world_seed, w.tick, ACTOR, "estimate"), 16))
    n = w.fixtures.get("estimate_samples")
    by_trackers = dict.fromkeys(combat.ESTIMATE_OUTCOMES, 0)
    disagree = scenes = 0
    for _ in range(n):
        r = _ran("entry.fn", entry.fn, inp, rng)
        a, b = bool(r["wound_state"][ACTOR]["felled"]), bool(r["wound_state"][SUBJECT]["felled"])
        if combat.surrender_of(r["trace"]) is not None:
            by_trackers["yielded"] += 1
        elif a and not b:
            by_trackers["actor_felled"] += 1
            disagree += r["result"] != -1
        elif b and not a:
            by_trackers["subject_felled"] += 1
            disagree += r["result"] != 1
        else:
            by_trackers["undecided"] += 1
        scenes += 1
    assert scenes == n and scenes >= 100, scenes
    for k in combat.ESTIMATE_OUTCOMES:
        assert got[k] == by_trackers[k] / n, (k, got[k], by_trackers[k] / n)
    assert disagree >= 1, "the stream never showed the sign and the trackers disagreeing: the control cannot fail"


def _fight_act():
    return Act(id="est1", actor=ACTOR, verb="fight", payload={"subject": SUBJECT})


def test_odds_of_returns_the_shares_for_a_row_contesting_the_body_and_nothing_for_a_believer():
    w = _world((4, 1))
    act = _fight_act()
    odds = _ran("odds_of", sigma.odds_of, w, act)
    assert odds is not None, "odds_of dealt no odds for a fight"
    assert odds == _shares(_estimate(w)), (odds, _shares(_estimate(w)))
    assert math.isclose(sum(odds), 1.0, abs_tol=1e-12), odds
    believer = w.persons[ACTOR]
    # mode (b) is not built for a fight: the believer's figure is None, and so is the chooser's query
    assert _ran("odds_of (b)", sigma.odds_of, w, act, believer=believer) is None
    assert _ran("believed_chance", sigma.believed_chance, w, believer, act, ("Wounded", "Felled")) is None


def test_the_estimate_consumes_no_season_draw_and_writes_nothing():
    control, called = _world((4, 1)), _world((4, 1))
    assert control.draw == called.draw and control.content_hash() == called.content_hash()
    for _ in range(3):
        _estimate(called)
    _ran("odds_of", sigma.odds_of, called, _fight_act())
    assert called.draw == control.draw, f"the estimate moved the season draw counter {control.draw} -> {called.draw}"
    assert called.content_hash() == control.content_hash(), "the estimate moved the world's content hash"
    assert called.new_draw() == control.new_draw(), "the next season draw differs after the estimate"


def test_a_season_run_of_the_realm_is_the_same_with_and_without_the_call():
    """The control run (no call) against a run whose world made the call before the season began. The call
    sits between build and season, where a draw taken would be reset at the tick's start, so this reads the
    STATE (a write would show); the draw counter above reads the draws."""
    def one_season(call):
        w = populated.build_realm(0)
        if call:
            SeasonDriver(w)
            people = sorted(w.persons)[:2]
            got = combat.fight_estimate(w, people[0], None, people[1], "fight")
            assert got["status"] == "ESTIMATED", got
        populated.run(seasons=1, seed=0, w=w)
        return w.content_hash()
    control = _ran("the control season", one_season, False)
    with_call = _ran("the season after the call", one_season, True)
    assert with_call == control, f"a season after the estimate hashes {with_call}, the control {control}"


def test_the_sample_count_is_refused_unless_a_whole_number_of_at_least_one():
    checked = 0
    for bad in (0, -3, 2.5, "400", None, True):
        w = _world((4, 4))
        w.fixtures = w.fixtures.sweep("estimate_samples", bad)
        try:
            combat.fight_estimate(w, ACTOR, None, SUBJECT, "fight")
        except Exception as e:                                   # noqa: BLE001
            assert type(e).__name__ == "Forbidden", f"{bad!r}: raised {type(e).__name__}, not Forbidden"
        else:
            raise AssertionError(f"estimate_samples {bad!r} was accepted")
        checked += 1
    assert checked == 6, checked
    w = _world((4, 4))
    w.fixtures = w.fixtures.sweep("estimate_samples", 7)
    assert _estimate(w)["samples"] == 7


def test_a_party_gap_is_a_refusal_not_a_figure():
    w = _world((4, 4))
    checked = 0
    for actor, target in ((ACTOR, ACTOR), (ACTOR, "nobody"), ("nobody", SUBJECT)):
        got = _ran("fight_estimate", combat.fight_estimate, w, actor, None, target, "fight")
        assert got["status"] == "PARTY-GAP", (actor, target, got)
        checked += 1
    assert checked == 3, checked
