"""v9 SC-01 step 14 -- THE OBSTACLE CEILING (`workplans/valoria_master_workplan_v9_part6.md` §SC-01, the
CARRIED block's *Step 14*: Contradiction 3 resolved -- take the obstacle CEILING, its value injected and
swept, never a pool floor; the seam's own obstacle site is deleted, ED-SC-0033 clause (3), one owner).

WHAT IS BUILT, and where each piece is read:
  * THE OWNER. `modules/social_contest/roll.py::obstacle` composes a social contest's obstacle -- the
    opposition's score halved, the `obstacle_default` stand-in where there is no score, bounded above
    by the ceiling. The host input builder (`seam/wrappers/sigma.py::contest_input`) carries the raw
    operands in `SocialContestInput` and composes nothing: the record has no `ob` field to put a
    second site's value in.
  * THE CEILING. `Fixtures obstacle_ceiling` (`H-213`), injected into the record, swept [1, 2, 3].
    `None` is the CONTROL arm (no ceiling, the tree before this step).
  * ED-SC-0038's PICK, made here: PER MATTER. One injected value bounds the obstacle of EACH matter's
    draw independently; there is no aggregate obstacle over a bundle of matters (`H-213`'s `default:`).

M-7 (`proposals/2026-09-05-proceedings-subsystem/19_PLAN.md` M-7; run at `21_RECONCILIATION.md`'s
PHASE 0 result): at the 1D pool floor against the maximum plausible composed obstacle, the chance of a
non-Failure band must not be effectively zero. "EFFECTIVELY ZERO" is named here, not left to a reader:
`EFFECTIVELY_ZERO = 0.001`, because the reconciliation's own table calls its Ob-3 row (0.0006) the
point where the floor "reaches zero". The quantity is `1 - F` of `sigma_leverage.band_odds(1, ob)` with
`ob = obstacle(record)` for a requested obstacle of 4..11 (`opposition = 2 x Ob`), checked at B05.02 against
`HITS_N` seeded rolls of the real module entry graded by the real ladder (the one sampler, A-5; it was the
exact count of the ten d10 faces forced in turn until the faces left the social roll).

RE-MEASURED AT B05.02 (the one sampler): `band_odds` is the Normal closed form of the sampler the roll draws,
so the figures below return to the Gaussian column of the CP-T01-03 table (0.226627 / 0.02275 / 0.000577 /
3e-06 at ceilings 1 / 2 / 3 / None, 1D, Ob = the ceiling): the verdicts are unchanged (the control and the
ceiling-3 arm fail M-7, the shipped arm clears it). The figures further down this docstring are the whole-dice
ones and are history.

RE-MEASURED AT CP-T01-03 (B10-08): the instrument moved from `p_success`, the Gaussian closed form
(up to 17 points wrong on these dice: 17.3 at the ceiling-1 pair, 7.7 at the shipped one), to
`band_odds`, the exact enumeration. The two disagree where the closed form is worst. Chance of a non-Failure band at the 1D floor, old `p_success` -> new `band_odds`:
  ceiling 1  0.226627 -> 0.4      (4 of 10 faces)
  ceiling 2  0.02275  -> 0.1      (1 of 10 faces; the shipped arm)
  ceiling 3  0.000577 -> 0.0      (0 of 10 faces)
  None       3e-06 at Ob 4, 0.0 above -> 0.0 at every Ob 4..11
Every verdict is unchanged (the control and the ceiling-3 arm fail M-7, the shipped arm clears it), and
`band_odds` now equals the forced-face count exactly, which `p_success` never did. ONE CLAIM WAS
WRONG IN ITS FIRST FORM, and CP-T01-04 undid the correction: at CP-T01-03 (whole successes only) no
level's boost (<= 0.70) moved a whole success at pool 1, so the odds read flat at 0.1. With the
fraction rule (CP-T01-04) a boost `b` under one success is worth its fraction: at pool 1 against Ob 2
the chance of a non-Failure band is 0.1 + 0.3 * b, that is 0.1595 / 0.2157 / 0.2664 / 0.3098 at
minor / moderate / strong / major. So the sigma-channel IS live under the ceiling, strictly, and the
test below asserts it strictly (a dead channel reads 0.1 at every level and fails).

THE FALSIFIERS (each seen red before the build, 2026-10-16: the record had no `opposition` /
`obstacle_ceiling` field, `DEFAULT_FIXTURES` no `obstacle_ceiling`, `sigma` still held `_obstacle_of`):
  * M-7 at the floor clears Ob >= 4 with the ceiling, and FAILS on the control arm (no ceiling).
  * the sweep straddles M-7's boundary: the arm at 3 fails it, so the test can observe a failure.
  * the seam has no second obstacle site: the obstacle on a resolved act FOLLOWS the module's
    function when that function is replaced (a call, not a copy).
  * the ceiling is injected: changing the fixture changes the act's obstacle and its band
    distribution through the real seam on a hand-built world.
"""

from __future__ import annotations

import importlib
import math
import random
from dataclasses import asdict, fields

import pytest

from engine.dice_engine.dice_engine import DEGREE_LABEL, Degree
from engine.dice_engine.sigma_leverage import LEVEL_SIGMA, OB_MIN, band_odds, net_boost
from engine.substrate import composition

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.verbs import VERB_TABLE
from ..harness import probes as P
from ..harness import register as REG
from ..loop.driver import SeasonDriver
from ..queries.inputs import SocialContestInput
from ..seam import ladder
from ..seam.wrappers import sigma

EFFECTIVELY_ZERO = 0.001
FLOOR = 1                       # the 1D pool (the one-die roll M-7 is read at)
M7_OBS = range(4, 12)           # requested obstacles 4..11 (11: the reconciliation's own pool sweep)
FAILURE = DEGREE_LABEL[Degree.FAILURE]
ROW = "H-213"


def _module():
    """The `social_contest` module, found the way the host finds it: by the composition row's target
    string (`engine/` never imports module code by name)."""
    target = composition.ROLES["social_contest.roll"]["target"]
    return importlib.import_module(target.split(":", 1)[0])


def _record(opposition, ceiling, *, pool=FLOOR, leverage=0.0):
    return SocialContestInput(
        pool=pool, opposition=opposition,
        difficulty=0.0, pool_default=2 * STAND_IN, pool_add=0, opposition_rate=0.5,
        obstacle_ceiling=ceiling,
        obstacle_refusal_multiple=DEFAULT_FIXTURES.get("obstacle_refusal_multiple"),
        leverage=leverage)


STAND_IN = 2.0                  # what `obstacle_default` was: B05.14 composes it as `opposed_ob(pool_default)` = 0.5 x 4, at difficulty 0, for these records
HITS_N = 4000                   # seeded rolls per record in `_hits`


def _hits(mod, rec) -> int:
    """How many of `HITS_N` seeded rolls of the real entry the real ladder grades above Failure (the
    `Margin` graded as the host grades it, as its `net`/`ob` pair)."""
    rng = random.Random(7)
    return sum(ladder.degree_of(asdict(mod.roll(rec, rng))) != FAILURE for _ in range(HITS_N))


def _clear(pool, ob, boost=0.0) -> float:
    """The chance of a non-Failure band: `1 - F` of the exact odds."""
    return 1.0 - band_odds(pool, ob, boost)[0]


def _m7(mod, ceiling) -> dict:
    """M-7 at the 1D floor for each requested obstacle in `M7_OBS`, on one ceiling arm."""
    out = {}
    for ob in M7_OBS:
        rec = _record(2 * ob, ceiling)
        eff = mod.obstacle(rec)[0]
        hits = _hits(mod, rec)
        out[ob] = (eff, _clear(FLOOR, eff), hits)
        # the instrument is the dealt roll: its chance is the sampled rate, to four standard errors
        chance = out[ob][1]
        assert abs(chance - hits / HITS_N) <= 4 * math.sqrt(chance * (1 - chance) / HITS_N) + 1e-9, (ceiling, ob, out[ob])
    return out


def test_m7_at_the_1d_floor_clears_ob_4_and_above_under_the_ceiling_and_fails_without_it():
    mod = _module()
    shipped = DEFAULT_FIXTURES.get("obstacle_ceiling")
    assert shipped is not None, "the shipped arm is the control; the ceiling is not wired"
    before, after = _m7(mod, None), _m7(mod, shipped)
    checked = 0
    for ob in M7_OBS:
        eff0, p0, hits0 = before[ob]
        eff1, p1, hits1 = after[ob]
        # CONTROL: with no ceiling the composed obstacle IS the requested one, and M-7 fails --
        # the reconciliation's measurement, reproduced through the owner rather than cited.
        assert eff0 == ob, (ob, eff0)
        assert p0 < EFFECTIVELY_ZERO and hits0 == 0, (
            f"control arm: Ob {ob} at 1D gave chance {p0:.6f} and {hits0}/{HITS_N} rolls -- M-7 "
            f"should FAIL without a ceiling; if it passes, the instrument cannot see the failure")
        # THE CLAIM: the ceiling bounds the obstacle, and the floor-pool speaker keeps a chance.
        assert eff1 == shipped, (ob, eff1)
        assert p1 >= EFFECTIVELY_ZERO and hits1 >= 1, (
            f"Ob {ob} at the 1D floor under ceiling {shipped}: chance {p1:.6f}, {hits1}/{HITS_N} "
            f"rolls -- M-7 still fails (`EFFECTIVELY_ZERO` = {EFFECTIVELY_ZERO})")
        checked += 1
    assert checked == len(M7_OBS)
    # CONTROL 2: an obstacle BELOW the ceiling is untouched -- the ceiling bounds, it does not shift.
    for ob in (1, 2):
        if ob <= shipped:
            assert mod.obstacle(_record(2 * ob, shipped))[0] == mod.obstacle(_record(2 * ob, None))[0] == ob
    # M-7's second clause: without the ceiling, BUYING ADVANTAGE does not rescue Ob 4 at the floor
    # (remedy (a) refuted, `21_RECONCILIATION.md`) -- every rostered level stays effectively zero.
    for lv, s in LEVEL_SIGMA.items():
        boost = net_boost(s, FLOOR)
        assert _clear(FLOOR, 4, boost) < EFFECTIVELY_ZERO, (lv, _clear(FLOOR, 4, boost))
        # under the ceiling, buying advantage RAISES the chance at the floor, strictly (a boost is a mu-shift of
        # the one sampler, worth its shift at every size) ...
        assert boost > 0 and _clear(FLOOR, shipped, boost) > _clear(FLOOR, shipped, 0.0), lv
    # ... and no level clears a whole success at pool 1, while pool 4's major level does.
    assert max(net_boost(s, FLOOR) for s in LEVEL_SIGMA.values()) < 1.0
    major4 = net_boost(LEVEL_SIGMA["major"], 4)
    assert major4 > 1.0 and _clear(4, shipped, major4) > _clear(4, shipped, 0.0)


def test_the_ceiling_is_swept_and_the_sweep_straddles_m7():
    """`H-213` declares the sweep; each point is RUN, not listed. A verdict that flips across the
    sweep is itself the finding S42.2.1 asks for: the arm at 3 fails M-7, so this test can observe
    a failure, and the shipped arm passes."""
    rows = {r["id"]: r for r in REG.load()["rows"]}
    row = rows.get(ROW)
    assert row is not None, f"{ROW} (the ceiling's register row) is missing"
    sweep = row["sweep"]
    assert len({str(x) for x in sweep}) >= 3, sweep
    assert DEFAULT_FIXTURES.get("obstacle_ceiling") in sweep, sweep
    mod = _module()
    verdict = {}
    for c in sweep:
        m = _m7(mod, c)
        verdict[c] = all(p >= EFFECTIVELY_ZERO and hits >= 1 for _, p, hits in m.values())
        assert all(eff == c for eff, _, _ in m.values()), (c, m)   # each arm reaches the record
    assert verdict[DEFAULT_FIXTURES.get("obstacle_ceiling")], verdict
    assert not all(verdict.values()), (
        f"every sweep point passes M-7 ({verdict}); the sweep cannot observe the failure")


def test_a_ceiling_below_the_ob_minimum_is_refused_and_one_at_it_is_read():
    """`obstacle`'s refusal branch, reached: a ceiling under `OB_MIN` (PP-232) would breach the floor,
    so it raises rather than bounding anything; the ceiling AT the minimum is the control, read."""
    mod = _module()
    with pytest.raises(ValueError, match="below the Ob minimum"):
        mod.obstacle(_record(10, OB_MIN - 0.5))[0]
    assert mod.obstacle(_record(10, OB_MIN))[0] == OB_MIN


def test_the_seam_has_no_second_obstacle_site(monkeypatch):
    """ED-SC-0033 clause (3): one owner. The host's record has no field an obstacle could travel in,
    the host builder holds no obstacle function, and a resolved act's obstacle is whatever the
    module's `obstacle` returns -- replace that function and the act follows it."""
    assert "ob" not in {f.name for f in fields(SocialContestInput)}, (
        "the host record carries an `ob`: a host-derived obstacle can reach the roll again")
    assert not hasattr(sigma, "_obstacle_of"), "the seam's own obstacle site is back"
    mod = _module()
    # B05.14: read with no difficulty and a hearer holding his resisting attribute at 0, so the obstacle is score / 2: this test is about WHO
    # composes the obstacle, not its terms (`test_obstacle_form.py`'s)
    w = P.tiny_world(DEFAULT_FIXTURES.sweep("difficulty_ob", {k: 0 for k in DEFAULT_FIXTURES.get("difficulty_ob")}))
    SeasonDriver(w)                                  # the registrar fills MODULE_ENTRIES
    w.persons["p_mid"].capability = {"copying": 3}
    w.persons["p_mid"].attributes = {VERB_TABLE["tell"].opposed_attribute: 0}
    seen = sigma.resolve(w, ["p_low"], ["c"], "a standing", verb="tell", subject="p_mid",
                         rng=random.Random(0))
    assert seen["status"] == "RESOLVED" and seen["ob"] == 1.5, seen
    monkeypatch.setattr(mod, "obstacle", lambda inp: (1.25, ()))
    moved = sigma.resolve(w, ["p_low"], ["c"], "a standing", verb="tell", subject="p_mid",
                          rng=random.Random(0))
    assert moved["ob"] == 1.25, (
        f"the act's obstacle did not follow the owner ({moved}): something else composes it")


def _arm(ceiling):
    # the FIXED arm (CP-T01-06 ships the per-pool arm; the 1 / 2 / 3 sweep is read on the fixed one)
    # B05.14: on score / 2 alone (no difficulty, resisting attributes held at 0), the composition these figures were read on; the
    # ceiling bounds the form's obstacle the same way (`roll.py::obstacle`'s `ceiling` term)
    w = P.tiny_world(DEFAULT_FIXTURES.sweep("ceiling_per_pool", False).sweep("obstacle_ceiling", ceiling)
                     .sweep("difficulty_ob", {k: 0 for k in DEFAULT_FIXTURES.get("difficulty_ob")}))
    SeasonDriver(w)
    for who in ("p_mid", "p_other", "p_king", "p_low"):
        w.persons[who].attributes = {VERB_TABLE["tell"].opposed_attribute: 0}
    # roster-exempt: TEST FIXTURE capabilities -- one matter far over every sweep point, one under.
    w.persons["p_mid"].capability = {"copying": 10}       # score/2 = 5
    w.persons["p_other"].capability = {"copying": 3}      # score/2 = 1.5
    return w


@pytest.mark.parametrize("subject,want", [("p_mid", {2: 2.0, 3: 3.0}),
                                          ("p_other", {2: 1.5, 3: 1.5}),
                                          ("p_king", {2: 1.0, 3: 1.0}),
                                          ("site_harbour", {2: 1.0, 3: 1.0})])
def test_the_ceiling_is_injected_and_bounds_each_matter_on_its_own(subject, want):
    """Through the real seam on a hand-built world: the fixture's value is what bounds the act's
    obstacle (2 -> 2.0, 3 -> 3.0 for a subject whose score/2 is 5), an obstacle under the ceiling is
    untouched (1.5), a person holding nothing opposes at the untrained score (B05.11: `pool_default` 2 / 2 = 1.0 on every arm,
    where the stand-in was 2), and the no-score stand-in (`opposed_ob(pool_default)`, 2 here) is bounded the same way for a subject
    who is no person (a site: nobody opposite).
    PER MATTER (ED-SC-0038): each subject's draw is bounded on its own; nothing aggregates them."""
    for c, ob in want.items():
        out = sigma.resolve(_arm(c), ["p_low"], ["c"], "a standing", verb="tell", subject=subject,
                            rng=random.Random(0))
        assert out["status"] == "RESOLVED" and out["ob"] == ob, (c, out)


def test_changing_the_ceiling_changes_the_outcome():
    """The band distribution over the same seeds moves when only the fixture moves."""
    hits, differ = {}, 0
    worlds = {c: _arm(c) for c in (2, 3)}
    for s in range(300):
        bands = {c: ladder.degree_of(sigma.resolve(w, ["p_low"], ["c"], "a standing", verb="tell",
                                                   subject="p_mid", rng=random.Random(s)))
                 for c, w in worlds.items()}
        for c, b in bands.items():
            hits[c] = hits.get(c, 0) + (b != FAILURE)
        differ += bands[2] != bands[3]
    assert differ > 0 and hits[2] > hits[3], (hits, differ)


# ---------------------------------------------------------------------------------------------
# CP-T01-06 -- THE CEILING SOLVED PER POOL (the `chance_floor` arm)
# ---------------------------------------------------------------------------------------------
# Below one die the fixed value applies as it always did. From one die, the composed obstacle is
# capped at the highest Ob at which THIS pool still keeps `H-213`'s chance -- Partial-or-better of
# `band_odds(1, obstacle_ceiling)`, 2.2 % on the one sampler (B05.02; it was 10 % on whole dice) -- so a larger
# pool is never worse for the cap, and an admitted roll keeps a real chance. The cap is solved at the largest
# lawful disadvantage (`-M_MAX`, `roll.py::_chance_floor_cap`), and the same z-shift cancels on both sides, so the
# cap equals the one solved with no advantage and the chance AT the cap, with no advantage, is the one-die floor. The detector below is run on the rejected `2 * pool` cap too
# (301 inversions measured at the base of CP-T01-06): a count of zero means something only because
# the same count sees the others fail.
POOLS = (0, 0.5) + tuple(range(1, 9))
QUARTERS = tuple(q / 4 for q in range(0, 81))             # composed Ob 0 .. 20 in quarter steps
CHANCE_FLOOR = 1.0 - band_odds(1, DEFAULT_FIXTURES.get("obstacle_ceiling"))[0]    # H-213's shipped chance at the 1D floor, no advantage
EPS = 1e-12                                               # float noise on a 1 - F; not a tolerance on a rule


def _pooled(pool, ob, *, per_pool=True, ceiling=None, fixed=True):
    """A record whose composed obstacle, before any ceiling, is `ob` (opposition = 2 x ob)."""
    return SocialContestInput(
        pool=pool, opposition=2 * ob,
        difficulty=0.0, pool_default=2 * STAND_IN, pool_add=0, opposition_rate=0.5,
        obstacle_ceiling=DEFAULT_FIXTURES.get("obstacle_ceiling") if fixed else ceiling,
        obstacle_refusal_multiple=DEFAULT_FIXTURES.get("obstacle_refusal_multiple"),
        leverage=0.0, ceiling_per_pool=per_pool)


def _plus(pool, ob):
    """(Partial-or-better, Success-or-better) of the exact odds."""
    f, p, s, o = band_odds(pool, ob)
    return 1.0 - f, s + o


def _inversions(eff_of):
    """Cells (pool 1..7 against the next pool, composed Ob >= OB_MIN) where the larger pool has the
    LOWER Partial-or-better or Success-or-better. `eff_of(pool, ob)` is the capped obstacle."""
    cells = bad = 0
    for pool in range(1, 8):
        for ob in QUARTERS:
            if ob < OB_MIN:
                continue
            small, large = _plus(pool, eff_of(pool, ob)), _plus(pool + 1, eff_of(pool + 1, ob))
            cells += 1
            bad += large[0] < small[0] - EPS or large[1] < small[1] - EPS
    assert cells == 7 * sum(q >= OB_MIN for q in QUARTERS)       # it looked at every cell
    return bad


def test_the_shipped_arm_is_the_chance_floor_and_the_old_arms_stay_selectable():
    assert DEFAULT_FIXTURES.get("ceiling_per_pool") is True
    mod = _module()
    # the fixed arm (what shipped before) is one fixture away, and the uncapped arm is `None`
    assert mod.obstacle(_pooled(4, 20, per_pool=False))[0] == DEFAULT_FIXTURES.get("obstacle_ceiling")
    assert mod.obstacle(_pooled(4, 20, per_pool=True, ceiling=None, fixed=False))[0] == 20
    assert mod.obstacle(_pooled(4, 20, per_pool=True))[0] > DEFAULT_FIXTURES.get("obstacle_ceiling")


def test_the_enumeration_pools_by_composed_ob():
    """The home's falsifier (1)-(3), over pools {0, 0.5, 1 .. 8} x composed Ob 0 .. 20 in quarters."""
    mod = _module()
    fixed = DEFAULT_FIXTURES.get("obstacle_ceiling")
    multiple = DEFAULT_FIXTURES.get("obstacle_refusal_multiple")
    below_one = at_or_above_one = 0
    table = {}
    for pool in POOLS:
        for ob in QUARTERS:
            eff = mod.obstacle(_pooled(pool, ob))[0]
            base = mod.obstacle(_pooled(pool, ob, per_pool=False))[0]
            assert base == max(OB_MIN, min(ob, fixed))                     # the control arm is today's, over B05.14's floor
            assert eff <= max(ob, OB_MIN) + EPS and (eff == ob or eff >= OB_MIN), (pool, ob, eff)   # (1) a cap is never under OB_MIN
            table[(pool, ob)] = _plus(pool, eff)
            if pool < 1:
                assert eff == base, (pool, ob, eff, base)                  # (2) below a die: the base, refused as now
                below_one += 1
                continue
            assert eff <= multiple * pool + EPS, (pool, ob, eff)           # (2) S27.4 never refuses a derived pair
            assert table[(pool, ob)][0] >= CHANCE_FLOOR - EPS, (pool, ob, eff, table[(pool, ob)])   # (2) a real chance
            at_or_above_one += 1
    assert below_one == 2 * len(QUARTERS) and at_or_above_one == 8 * len(QUARTERS)
    # (3) for every composed Ob at or above OB_MIN, both readings are non-decreasing in pool
    checked = 0
    for ob in QUARTERS:
        if ob < OB_MIN:
            continue
        for lo, hi in zip(POOLS, POOLS[1:]):
            assert table[(hi, ob)][0] >= table[(lo, ob)][0] - EPS, ("Partial+", lo, hi, ob)
            assert table[(hi, ob)][1] >= table[(lo, ob)][1] - EPS, ("Success+", lo, hi, ob)
            checked += 1
    assert checked == len(POOLS[1:]) * sum(q >= OB_MIN for q in QUARTERS)


def test_the_inversion_count_is_zero_and_the_detector_sees_the_rejected_caps():
    mod = _module()
    solved = lambda pool, ob: mod.obstacle(_pooled(pool, ob))[0]
    assert _inversions(solved) == 0
    # the same detector on the cap CP-T01-06 rejected (`2 * pool`): it must see the failure it excludes
    assert _inversions(lambda pool, ob: min(ob, 2.0 * pool)) >= 300


def test_the_cap_is_the_floor_met_exactly_and_the_pool_below_one_keeps_the_fixed_value():
    mod = _module()
    caps = {p: mod.obstacle(_pooled(p, 20))[0] for p in range(1, 9)}
    assert caps[1] == pytest.approx(2.0, abs=1e-9)                         # the 1D floor's own value
    assert list(caps.values()) == sorted(caps.values())                    # the cap rises with the pool
    for pool, cap in caps.items():
        assert _plus(pool, cap)[0] == pytest.approx(CHANCE_FLOOR, abs=1e-9)   # met, not exceeded
        assert _plus(pool, cap + 0.05)[0] < CHANCE_FLOOR - 1e-6              # and no higher Ob keeps it
    assert round(caps[2], 3) == 3.063 and round(caps[3], 3) == 3.971 and round(caps[4], 2) == 4.8
    # the closed form keeps a chance at every ceiling (a 1D roll at Ob 3 keeps 0.06 %, not nothing), so the
    # per-pool arm solves at a ceiling of 3 too: it no longer falls back to the fixed value
    assert _module().obstacle(_pooled(4, 20, ceiling=3, fixed=False))[0] == pytest.approx(0.4 * 4 + 2.6 * 2, abs=1e-3)
    with pytest.raises(ValueError, match="below the Ob minimum"):
        mod.obstacle(_pooled(4, 20, ceiling=OB_MIN - 0.5, fixed=False))[0]


def test_the_chance_floor_reaches_the_resolved_act_through_the_seam():
    """The fixture is carried by the host and read by the module: pool 2 against a score/2 of 5."""
    for per_pool in (False, True):
        fx = DEFAULT_FIXTURES.sweep("ceiling_per_pool", per_pool)
        w = P.tiny_world(fx)
        SeasonDriver(w)
        w.persons["p_mid"].capability = {"copying": 10}       # roster-exempt: TEST FIXTURE, score/2 = 5
        out = sigma.resolve(w, ["p_low"], ["c"], "a standing", verb="tell", subject="p_mid",
                            rng=random.Random(0))
        assert out["status"] == "RESOLVED", out
        if per_pool:
            assert 2.0 < out["ob"] < 5.0
        else:
            assert out["ob"] == 2.0


# ---------------------------------------------------------------------------------------------
# B05.54 -- THE CEILING'S FORM (`ceiling_form`: `hard` a flat bound, `soft` the excess saturating toward the cap)
# ---------------------------------------------------------------------------------------------
# `16_PESSIMIST_DICE_soft_ceiling` gates 2 and 3, on the closed form. The floor the bent bound must keep is the one-die chance at the
# fixed ceiling (`CHANCE_FLOOR`, `1 - band_odds(1, ceiling)[0]`): the cap IS the Ob at which every pool holds that chance
# (`_chance_floor_cap`), so a bound that stays under the cap never gives a pool less. The source's own sentence reads
# `1 - band_odds(pool_floor, ceiling)[0]`, which is the chance of `pool_floor` dice AT the knee (0.50 at 5 dice) -- not a floor
# the cap holds (the chance AT the cap is the one-die figure, 0.0228), so that reading fails by construction and is not asserted.


def _formed(pool, ob, form, *, forgery=0.0):
    """A record whose composed obstacle, before any ceiling, is `ob` (opposition = 2 x ob) plus the forgery, on the shipped ceiling and
    the per-pool cap, in the given ceiling form."""
    return SocialContestInput(
        pool=pool, opposition=2 * ob,
        difficulty=0.0, pool_default=2 * STAND_IN, pool_add=0, opposition_rate=0.5,
        obstacle_ceiling=DEFAULT_FIXTURES.get("obstacle_ceiling"),
        obstacle_refusal_multiple=DEFAULT_FIXTURES.get("obstacle_refusal_multiple"),
        leverage=0.0, ceiling_per_pool=True, ceiling_form=form, forgery_quality=forgery)


def test_soft_bound_is_strictly_decreasing_and_floored():
    mod = _module()
    knee = DEFAULT_FIXTURES.get("obstacle_ceiling")
    floor = DEFAULT_FIXTURES.get("pool_floor")
    steps = [knee + k * 0.005 for k in range(0, int(round((14 - knee) / 0.005)) + 1)]
    checked = 0
    for pool in range(floor, floor + 11):
        prev = None
        bent = 0
        for ob in steps:
            hard = mod.obstacle(_formed(pool, ob, "hard"))[0]
            soft, terms = mod.obstacle(_formed(pool, ob, "soft"))
            assert hard == min(ob, mod._chance_floor_cap(pool, knee)), (pool, ob, hard)        # the control inside the test: `hard` is `min`
            assert soft <= hard + 1e-9, (pool, ob, soft, hard)                                 # bending only eases what the flat bound held
            bent += soft < hard - 1e-9
            chance = _clear(pool, soft)
            assert chance >= CHANCE_FLOOR - EPS, (pool, ob, soft, chance)                      # never under the one-die chance at the ceiling
            assert prev is None or chance < prev, (pool, ob, chance, prev)                     # strictly decreasing in the obstacle
            prev = chance
        assert bent > 0, pool                              # the arm bends somewhere: a `hard` that ignored the field would read bent == 0
        checked += 1
    assert checked >= 11


def test_four_forgery_qualities_give_four_ordered_chances():
    mod = _module()
    pool = DEFAULT_FIXTURES.get("pool_floor")
    base = 5.0                                             # above the knee, under the floor pool's cap (5.58); a forgery of 1 or more passes the cap
    qualities = (0.0, 0.5, 1.0, 3.0)
    hard = [_clear(pool, mod.obstacle(_formed(pool, base, "hard", forgery=q))[0]) for q in qualities]
    soft = [_clear(pool, mod.obstacle(_formed(pool, base, "soft", forgery=q))[0]) for q in qualities]
    assert all(a > b for a, b in zip(soft, soft[1:])), soft                    # soft: four strictly ordered chances
    assert hard[2] == hard[3], hard                                            # hard: the last two are equal -- the assertion that can fail
    assert hard[0] > hard[1] > hard[2], hard
