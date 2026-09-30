"""Plan position `28-ii` (M6, successor goldens) -- `28-i`'s own record (§8.5,
`workplans/2026-09-28-the-plan-one-order-mc-v18-retired.md`) names the gap this file closes:
`test_mc_v18_regression.py`'s seed-0 golden (`run_batch(n=2, base_seed=0)`, two 50-season
`engine/mc_v18` campaigns) needs a season-side successor, and "which [existing test] is [one] was
not verified" (the plan's own §9).

CHECKED, NOT ASSUMED. Two existing candidates pin `World.content_hash()` determinism already, and
NEITHER qualifies:
  * `tests/valoria/test_m1_acceptance_probe.py::test_probe_season_hash_matches_across_independent_
    helper_calls` runs `engine.season.harness.headless.run(seasons=1, seed=M1_PROBE_SEED)` --
    `headless`'s THREE-person Carin world (`NPC-088`'s own fixture), for ONE season.
  * `test_season_shape.py::test_r4_event_ids_are_unique_per_draw_and_reproducible` runs
    `P.tiny_world()` (`_w()`) through ONE pass of the driver, not a season at all.

Neither is `harness.populated.build_realm(0)` -- the populated, canonical-geography, full-cast
world (83 persons, 412 rungs at this writing) -- run across MULTIPLE seasons, which is the shape
the retired golden actually exercised (two-campaign, many-tick). This is that pin, named:
`build_realm(0)`, the SAME seed, run for `_SEASONS` seasons through the REAL `SeasonDriver`/
`make_chooser`, TWICE, independently, comparing `World.content_hash()`.

⚠ A THIRD, EQUIVALENT PIN ALREADY EXISTS, AND IT IS NARROWER (BATCH-CLOSE Phase-1 antagonist
finding, disclosed rather than left for a later session to rediscover):
`test_aperture.py::test_aperture_the_measured_season_is_the_populated_season` (its module-scoped
`realm` fixture, `test_aperture.py:32-34`) already builds `build_realm(0)` TWICE via
`harness/aperture.py::measure_world` -- once through `populated.run` (the control arm) and once
through `instrumented_season` (the measured arm) -- and asserts `c["hash"] == realm["hash"]` at
`test_aperture.py:44-47`. A dedicated pin here still earns its place: that equality is between
`populated.run` and `aperture.py`'s OWN instrumentation wrapper around the same driver, so a
failure there is ambiguous between a real `build_realm`/`SeasonDriver` non-determinism and a bug
in the instrumentation `aperture.py` adds on top (the counterfactual re-aggregation, the funnel
bookkeeping). This file's pin runs the SAME `build_realm`/`run` pairing on BOTH sides with no
instrumentation in between, so a failure here is unambiguously `build_realm`/`SeasonDriver`'s own
determinism, not `aperture.py`'s wrapper.

⚠ `_SEASONS = 1`, MEASURED RATHER THAN GUESSED, AND FOR A DIFFERENT REASON THAN THE OLD GOLDEN'S
50. This pin is a REGRESSION TRIPWIRE for `CLAUDE.md` §7's/the retirement plan's own gate -- "a
same-seed hash pin ... must have actually RUN" -- not a balance instrument (`harness/arms.py`,
`28-i`, is that, and already exists). `populated.run` does NOT cost a flat per-season amount at
this cast size: measured directly, `build_realm(0)` + season 1 alone is ~12s, and a SECOND season
on the same world costs another ~80-90s on top of that (more claims, more ledger reads, more
Question sources to evaluate as state accumulates) -- so two independent `_SEASONS=2` runs for
each of this file's two tests would cost this file alone more than the 143-case corpus test this
package also carries. `M1_POP_SEASONS = 1` in `tools/m1_acceptance.py` is the tree's own existing
precedent for capping the populated world at one season for exactly this reason; this file follows
it rather than re-arguing it. `content_hash()` already folds every state collection (`H-118`), not
only the log, so ONE season already exercises the property this pin exists to guard.
"""
from __future__ import annotations

import pytest

from ..harness.populated import build_realm, run


_SEASONS = 1
_SEED = 0


@pytest.fixture(scope="module")
def seed0_hash():
    """The determinism test below already proves `build_realm(_SEED)` + one season is reproducible
    across two INDEPENDENT from-scratch builds -- that is the property under test there and must
    stay two real builds. The sensitivity test only needs *some* already-verified-reproducible
    seed-0 hash to diff a seed-1 run against; a third from-scratch (build_realm(0) + run) cycle to
    get it was pure duplication (`/simplify`, BATCH-CLOSE Phase 2 -- ~12s, ~25% of this file's
    cost, measured), fixed here the same way `test_aperture.py`'s own module-scoped `realm` fixture
    (`test_aperture.py:32-34`) already avoids the identical duplication for its own three tests."""
    w = build_realm(_SEED)
    run(seasons=_SEASONS, seed=_SEED, w=w)
    return w.content_hash()


def test_build_realm_seed_0_is_deterministic_across_n_seasons():
    """Same seed, `_SEASONS` seasons, run TWICE independently through the real driver -- the
    successor to `test_mc_v18_regression.py::test_mc_v18_batch_is_deterministic`, over
    `engine/season` (the head) rather than the superseded `engine/mc_v18` campaign driver."""
    w1 = build_realm(_SEED)
    # ⚠ CAPTURED BEFORE `run()`, AND CHECKED BELOW (BATCH-CLOSE Phase-1 antagonist finding,
    # CLAUDE.md §0.1 pt 2 -- "assert it asserted"): without this, `len(h1) == 32` holds even for a
    # world the season never touched, so this test could not tell "the season ran and changed
    # nothing" apart from "the season never ran at all".
    pre = w1.content_hash()
    run(seasons=_SEASONS, seed=_SEED, w=w1)
    w2 = build_realm(_SEED)
    run(seasons=_SEASONS, seed=_SEED, w=w2)
    h1, h2 = w1.content_hash(), w2.content_hash()
    assert h1 == h2, (
        f"two independent {_SEASONS}-season runs of `build_realm({_SEED})` diverged: "
        f"{h1!r} != {h2!r} -- the season loop is not reproducible under a fixed seed")
    # Falsifier for a vacuous pass (CLAUDE.md §0.1 pt 2): a constant/empty hash would satisfy
    # equality trivially without the run having done anything.
    assert h1 and len(h1) == 32, f"content_hash() returned {h1!r}, not a real 32-hex digest"
    assert h1 != pre, (
        f"the {_SEASONS}-season run left `content_hash()` unchanged from before it started "
        f"({pre!r}) -- this pin would pass identically whether the season ran at all")


def test_build_realm_hash_is_sensitive_to_what_the_season_did(seed0_hash):
    """Companion falsifier to the pin above, on `test_m1_acceptance_probe.py`'s own precedent
    (`test_a_different_seed_can_diverge_from_the_probe_seed`): two DIFFERENT seeds must not
    collide, or `content_hash()` would not actually be keyed on campaign content and the
    determinism pin above would be trivially satisfiable by a constant. The seed-0 side reuses
    `seed0_hash` (already proven reproducible by the test above) rather than a third from-scratch
    build+run of the same seed."""
    w2 = build_realm(_SEED + 1)
    run(seasons=_SEASONS, seed=_SEED + 1, w=w2)
    assert seed0_hash != w2.content_hash(), (
        "seed 0 and seed 1 produced the identical content_hash() over "
        f"{_SEASONS} seasons -- either both runs are no-ops or the hash is not sensitive to "
        "what the season actually did")
