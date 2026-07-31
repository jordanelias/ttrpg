"""[W8d] The personal-combat RNG draw stream — audit the INSTRUMENT the plan's measurements rest on.

`combat_completion_plan_v4.md` §4 W8d, scheduled deliberately BEFORE W1's ablation. Every acceptance
criterion in that plan is a paired-seed claim ("same seeds, term at zero, measure the delta"), and the
premise of a paired-seed claim is that the two arms are the same experiment. Nobody had checked. They
frequently are not.

WHAT THESE GUARDS ARE, HONESTLY (§1.6 tagging applied to a test suite, not just to constants): they are
**recorded measurements**, not pre-registered predictions. §3.2's pre-registration rule governs changing
a term and predicting the effect; this suite changes nothing and predicts nothing — it pins what the
current engine's stream actually does so that the next change to it cannot be silent. Every number below
was measured at `8535cea` and the measuring command is named in the assertion that carries it.

THE FINDING, in one line: **a change that shifts the draw count by ONE flips the outcome of 40.2% of
seeded fights** — 161 of 400 seeds, longsword vs rapier. Seeds are not experimental control across a
code change that moves the stream. (That 400-seed figure is the characterisation run; the shipped guard
re-measures it at n=200 to keep the suite under 5s, and asserts a 25% floor.)

FOUR MECHANISMS, each pinned by a guard below:

 1. **Input-conditional gates.** `wrapper.py:93` says so in its own comment — "represent_p==1.0
    (none/light) draws NO rng — the gate is inert on the stream off-plate". One seed, longsword vs
    arming: 57 underlying draws at `armour='none'`, **168 at `'heavy'`**.
 2. **A parity latch inside the stdlib.** `random.Random.gauss` caches its second Box-Muller variate,
    so k `gauss` calls consume `2*ceil(k/2)` underlying draws. `core.resolve` reaches `gauss` on the
    same object the engine draws `random()` from, so adding one resolution shifts the bare-`random()`
    sub-stream by 0 or 2 depending on parity. Non-uniform, so no constant offset corrects it.
 3. **34 draw calls across 33 lines** — one line (`wrapper.py:327`) carries two. Line granularity
    cannot separate them, which is a limit of the instrument and is asserted rather than hidden.
 4. **Three draw sites a 256-fight sweep never reaches.** Reported, NOT deleted: `state_graph.py`
    already records (ED-PC-0042) that this exact sweep produced two false "dead branch" verdicts, and
    the honest response to an unreached guard is a wider probe, not a smaller engine.

WHAT IS *NOT* CLAIMED. This suite does not show the shipped levers' measurements were wrong. It shows
their instrument is unvalidated and quantifies by how much that matters, which is the W8d scope. Whether
ED-PC-0052/0054's aggregate-inert results survive a stream-controlled re-measurement is W8a's job and is
still owed.

MUTATIONS — ALL RUN, with the OUTCOMES recorded rather than the intentions (§0.1 #4: a declared
mutation that was never executed is not evidence). 8 distinct mutants, 7 killed, 1 equivalent, plus one
deliberate survivor that exists to prove another guard's strictness is load-bearing.

  MUT-1 KILLED  `RecordingRandom`'s `_depth` guard removed, so nested stdlib draws count as engine sites
                -> reds `test_static_inventory_matches_dynamic_reach` AND
                   `test_recorder_observes_the_stream`. Broader than first declared; recorded as measured.
  MUT-2 KILLED  `_site()` frame offset 2 -> 3
                -> reds `test_static_inventory_matches_dynamic_reach`. This is not hypothetical: offset 3
                   was the instrument's first form and it attributed 6,470 draws to one wrapper line.
  MUT-3 KILLED  one extra `rng.random()` added in `wrapper.engagement`
                -> reds `test_static_draw_site_inventory_is_pinned` AND the reach cross-check.
  MUT-4 KILLED  fragility guard's `burn=1` -> `burn=0`
                -> reds `test_one_extra_underlying_draw_flips_a_large_share_of_outcomes` (0% flips).
  MUT-5a EQUIVALENT  engine perturbed by `+ 1e-16*curvature` at K=0 -> survived, and it SHOULD:
                `1.0 + 1.5e-17 == 1.0` in float64, so the mutant is unrepresentable, not undetected.
                Recorded because "a mutation survived" and "the guard is weak" are different findings
                and collapsing them is how a suite acquires false confidence in both directions.
  MUT-5a' KILLED  same perturbation at `1e-12` (representable)
                -> reds `test_curve_recovery_k_zero_is_exactly_inert`.
  MUT-5b SURVIVES BY DESIGN  MUT-5a' re-run with that guard's `==` weakened to `pytest.approx`
                -> PASSES. That is the artifact proving the exactness is load-bearing rather than
                   stylistic: the identical engine defect is invisible under `approx`. §0.1 #2's
                   1-ulp-crossing-a-damage-boundary case, reproduced on demand.
  MUT-6 KILLED  `gauss` parity formula `2*((k+1)//2)` -> `2*k`
                -> reds `test_gauss_carries_a_parity_latch`.
  MUT-7 KILLED  `PARRY_MOMENT_K`'s `sig +=` line duplicated (a §1.1 double-charge)
                -> reds `test_moment_gain_applies_exactly_once[PARRY_MOMENT_K]`. It ALSO reds
                   `test_same_seed_is_not_the_same_experiment_across_armour`, which is this file's own
                   thesis demonstrating itself: a sigma change altered the draw stream.
  MUT-8 KILLED  the `* atten` factor dropped from the exactly-once expectation
                -> reds PARRY and WIND but correctly NOT BIND, whose attenuation is 1.0.
"""
import copy
import math
import os
import random
import sys

import pytest

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_ENGINE = os.path.join(_ROOT, 'systems', 'combat', 'combat_engine_v1')
for _p in (_ROOT, _ENGINE):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from valoria import _draw_stream as DS          # noqa: E402  the single owner (CLAUDE.md §8)

import wrapper as W                              # noqa: E402
import combat_systems as S                       # noqa: E402
import tradition as TR                           # noqa: E402
import vocabulary as V                           # noqa: E402
import weapon_physics as WP                      # noqa: E402
from combatant import Combatant                  # noqa: E402
from config import CFG                           # noqa: E402
from weapons import WEAPONS                      # noqa: E402


# ---------------------------------------------------------------------------
# pinned measurements (all at 8535cea; instrument = valoria/_draw_stream.py)
# ---------------------------------------------------------------------------
# {(module, method): number_of_rng_CALLS}. Calls, not lines: wrapper.py:327 carries two `rng.random()`
# on one line, so summing this dict gives 34 while the distinct-line count is 33. The call-count form is
# the stronger recurrence guard — a second draw added to an existing line still moves it.
PINNED_STATIC_SHAPE = {
    ('capabilities.py', 'uniform'): 1,
    ('combat_systems.py', 'betavariate'): 1,
    ('combat_systems.py', 'random'): 2,
    ('combat_systems.py', 'randrange'): 1,
    ('contact.py', 'random'): 2,
    ('dice_engine.py', 'gauss'): 1,
    ('wrapper.py', 'random'): 25,
    ('wrapper.py', 'randrange'): 1,
}
PINNED_STATIC_CALLS = 34
PINNED_STATIC_LINES = 33
# TWO DELIBERATE SCOPE CHOICES, noted because they will surprise whoever trips them:
#  · `dice_engine.py` lives in `engine/autoload/` — OUTSIDE the PC lane. It is in scope anyway because
#    `core.resolve` reaches it for every resolution, so an rng call added there genuinely moves the
#    combat stream. A cross-lane change tripping this PC guard is the coupling being reported, not a
#    false positive; the fix is to re-pin here and re-measure, not to narrow the scan.
#  · `capabilities.py:154` is inside a `__main__` self-test with its own local `random.Random(0)`.
#    Deleting that self-test would red this pin for no behavioural reason. Kept in scope rather than
#    special-cased: an AST scan that starts excluding call sites by context is a scan that can be argued
#    into missing one, and the failure message says which site moved.

# Draw sites the 256-fight sweep below never reaches, each with WHY. Pinned by (module, method) rather
# than line number so an unrelated edit above them does not flake the guard.
DISCLOSED_UNREACHED = {
    # A `__main__` self-test probe with its own local `random.Random(0)` — genuinely off the
    # engagement path, not a cold engine branch.
    ('capabilities.py', 'uniform'),
    # The exact-tie aggressor tiebreak: reached only when `ready[A] == ready[B]` as FLOATS, after both
    # have accumulated continuous cadence. Effectively unreachable, but a real guard — do not delete it
    # on this evidence (ED-PC-0042's lesson, recorded in state_graph.py).
    ('wrapper.py', 'randrange'),
}
# `wrapper.py:419` (`rng.random() > S.disrupt_resist_p(...)`) is also unreached by this sweep. It is a
# `random` site in a module that HAS reached `random` sites, so it cannot be pinned at (module, method)
# granularity — it is caught instead by the line-level count in
# `test_static_inventory_matches_dynamic_reach`.
PINNED_UNREACHED_LINE_COUNT = 3

SWEEP_WEAPONS = ('rapier', 'arming', 'longsword', 'spear', 'mace', 'shamshir', 'poleaxe', 'dagger')
SWEEP_ARMOURS = ('none', 'light', 'medium', 'heavy')


def _fight(wa, wb, seed, armour='none', cfg=None, burn=0):
    """One seeded fight through the recording RNG. `burn` consumes N underlying draws BEFORE the fight,
    which is how the fragility guard perturbs the stream by a known amount without touching the engine."""
    rec = DS.RecordingRandom(seed)
    for _ in range(burn):
        random.Random.random(rec)          # bypass the recorder: perturb the stream, not the trace
    result = W.fight(Combatant('X', weapon=wa, armor=armour),
                     Combatant('Y', weapon=wb, armor=armour), cfg or CFG, rec)
    return result, rec


def _sweep_traces():
    traces = []
    for i, wa in enumerate(SWEEP_WEAPONS):
        for j, wb in enumerate(SWEEP_WEAPONS):
            for armour in SWEEP_ARMOURS:
                _, rec = _fight(wa, wb, 1000 + i * 37 + j * 7, armour)
                traces.append(rec.trace)
    return traces


# ---------------------------------------------------------------------------
# 1. the instrument works at all
# ---------------------------------------------------------------------------
def test_recorder_observes_the_stream():
    """A silently-broken recorder makes every guard below vacuous (§0.1 #2: an assertion must be able
    to observe the failure it excludes). So: assert it recorded, and assert the two counters DIVERGE —
    `underlying` must exceed the engine-level trace, because `gauss` and `betavariate` consume nested
    `random()` calls the trace deliberately attributes to their outer site. Equal counters would mean
    the depth guard is inert."""
    _, rec = _fight('longsword', 'arming', 4242)
    assert len(rec.trace) > 10, f'recorder saw only {len(rec.trace)} engine draws — instrument broken'
    assert rec.underlying > len(rec.trace), (
        f'underlying({rec.underlying}) must exceed engine draws({len(rec.trace)}) — nested stdlib '
        f'draws are not being counted, so the depth guard or the counters are broken')


# ---------------------------------------------------------------------------
# 2. the recurrence guard — a new draw site anywhere reds this
# ---------------------------------------------------------------------------
def test_static_draw_site_inventory_is_pinned():
    """THE RECURRENCE GUARD (§0.1 #5: if you cannot write the guard you have not understood the
    pattern). Adding, removing or relocating an `rng.<method>(...)` call in the engine changes the
    stream for every draw after it, which silently invalidates any paired-seed measurement that spans
    the change. This pins the inventory so that becomes a red test rather than a quiet re-shuffle.

    STATIC (AST) rather than dynamic on purpose: 3 of 33 sites are unreached by a 256-fight sweep, so a
    dynamic pin would be one tuning change away from missing a new draw on a cold branch.

    Reds on MUT-3 (one added `rng.random()`)."""
    shape = DS.static_site_shape()
    assert shape == PINNED_STATIC_SHAPE, (
        'RNG draw-site inventory moved. This is not a formatting matter: it re-orders the draw stream, '
        'so every golden fixture and every paired-seed measurement taken across this change is '
        'comparing different random experiments.\n'
        f'  expected: {sorted(PINNED_STATIC_SHAPE.items())}\n'
        f'  actual:   {sorted(shape.items())}\n'
        'If the change is intended: re-pin here, and re-measure anything that claimed a paired-seed '
        'delta across it.')
    calls = DS.static_draw_sites()
    assert len(calls) == PINNED_STATIC_CALLS, f'{len(calls)} rng calls, pinned {PINNED_STATIC_CALLS}'
    assert len(set(calls)) == PINNED_STATIC_LINES, (
        f'{len(set(calls))} distinct draw LINES, pinned {PINNED_STATIC_LINES}. The gap from '
        f'{PINNED_STATIC_CALLS} calls is wrapper.py:327, which carries two draws on one line.')


def test_static_inventory_matches_dynamic_reach():
    """Cross-check the two independent instruments against each other. The static scan needs no
    reachability and the dynamic recorder needs no AST, so a disagreement beyond the disclosed
    unreached set means one of them is wrong — which is exactly how this suite caught its own
    instrument bugs (an off-by-one frame offset attributed 6,470 draws to one line; a missing depth
    guard reported the recorder itself as an engine site).

    Reds on MUT-1 and MUT-2."""
    static_lines = set(DS.static_draw_sites())
    reached = set()
    for trace in _sweep_traces():
        reached.update(trace)

    spurious = reached - static_lines
    assert not spurious, (
        f'dynamic recorder saw {len(spurious)} draw site(s) the AST scan does not know about: '
        f'{sorted(spurious)}. Either the recorder is mis-attributing frames (MUT-2) or counting its '
        f'own nested calls (MUT-1) — the engine cannot draw from a line that holds no rng call.')

    unreached = static_lines - reached
    assert len(unreached) == PINNED_UNREACHED_LINE_COUNT, (
        f'{len(unreached)} unreached draw site(s), pinned {PINNED_UNREACHED_LINE_COUNT}: '
        f'{sorted(unreached)}.\n'
        'MORE than pinned = a newly-cold draw, i.e. a branch this sweep stopped exercising.\n'
        'FEWER = a previously-cold branch became live, which is a behaviour change.\n'
        'Either way do NOT delete the draw on this evidence — ED-PC-0042 records that this same sweep '
        'produced two false dead-branch verdicts (collapse / beat_exhaustion fired 164 and 1,135 times '
        'under a wider probe). Widen the sweep instead.')
    assert {(m, meth) for m, _l, meth in unreached} >= DISCLOSED_UNREACHED, (
        f'the disclosed-unreached set changed: {sorted(unreached)}')


# ---------------------------------------------------------------------------
# 3. same seed is not the same experiment
# ---------------------------------------------------------------------------
def test_same_seed_is_not_the_same_experiment_across_armour():
    """The hazard made executable rather than asserted in prose. `wrapper.py:93`'s own comment states
    the represent gate draws no RNG off-plate; the consequence is that one seed buys a ~3x longer
    stream at heavy armour than at none, so "we used the same seeds" is not a control when the
    contexts differ.

    Measured at 8535cea, longsword vs arming, seed 4242: none 57 underlying, light 53, medium 116,
    heavy 168. The assertion takes a 2.0x floor, well inside the measured 2.95x."""
    counts = {}
    for armour in SWEEP_ARMOURS:
        _, rec = _fight('longsword', 'arming', 4242, armour)
        counts[armour] = rec.underlying
    assert all(v > 0 for v in counts.values()), counts
    ratio = counts['heavy'] / counts['none']
    assert ratio >= 2.0, (
        f'heavy/none underlying-draw ratio fell to {ratio:.2f} (measured 2.95 at 8535cea): {counts}. '
        f'If this converged to 1.0 the stream became context-independent, which would be good news '
        f'and must be verified, not assumed — re-check the represent gate at wrapper.py:93.')


def test_one_extra_underlying_draw_flips_a_large_share_of_outcomes():
    """THE FALSIFIER for "paired seeds are safe across a code change" (§0.1 #3 — name the test that
    would show the claim wrong).

    Perturb the stream by exactly ONE underlying draw — the smallest possible change, and less than a
    single added `core.resolve` costs (which consumes 0 or 2) — and count how many seeded fights end
    differently. Measured 161/400 = 40.2% at 8535cea, longsword vs rapier.

    The floor is 25%, chosen below the measurement with room for build/tuning drift but far above
    anything that could be called noise. Reds on MUT-4."""
    n = 200
    flips = 0
    for seed in range(n):
        a, _ = _fight('longsword', 'rapier', seed)
        b, _ = _fight('longsword', 'rapier', seed, burn=1)
        if a != b:
            flips += 1
    rate = flips / n
    assert rate >= 0.25, (
        f'one extra draw flipped only {flips}/{n} ({rate:.1%}) outcomes; measured 40.2% at 8535cea. '
        f'A collapse toward 0 would mean the engine became stream-insensitive — verify it, because it '
        f'would also mean the RNG stopped reaching a decision node.')
    # assert-that-it-asserted: the loop must not be vacuous in the other direction either
    assert flips < n, f'ALL {n} outcomes flipped, which suggests `burn` is doing more than one draw'


# ---------------------------------------------------------------------------
# 4. the stdlib latch behind the fragility (environment pin)
# ---------------------------------------------------------------------------
def test_gauss_carries_a_parity_latch():
    """ENVIRONMENT PIN, and the mechanism behind the fragility guard's 40%.

    `random.Random.gauss` computes two variates per Box-Muller pass and caches the second in
    `self.gauss_next`, so consumption is `2*ceil(k/2)`: two underlying draws on odd calls, zero on
    even. `core.resolve` -> `sigma_leverage.roll_net_continuous` -> `dice_engine.continuous_engine_sample`
    calls `gauss` on the SAME object the engine draws `random()` from, so adding one resolution shifts
    the bare-`random()` sub-stream by 0 or 2 depending on how many resolutions preceded it. That
    non-uniformity is why no constant offset can realign two streams.

    Pinned because a CPython change to `gauss` would move every combat golden with no other signal.
    Reds on MUT-6."""
    class _Counting(random.Random):
        def __init__(self, seed):
            super().__init__(seed)
            self.n = 0

        def random(self):
            self.n += 1
            return super().random()

    for k in range(1, 9):
        c = _Counting(99)
        for _ in range(k):
            c.gauss(0.0, 1.0)
        expected = 2 * ((k + 1) // 2)
        assert c.n == expected, (
            f'{k} gauss() calls consumed {c.n} underlying random() draws, expected {expected} '
            f'(2*ceil(k/2)). random.Random.gauss changed its caching behaviour in this Python '
            f'({sys.version.split()[0]}) — every combat golden is affected and must be re-recorded '
            f'deliberately.')


# ---------------------------------------------------------------------------
# 5. K=0 really is the neutral element
# ---------------------------------------------------------------------------
def test_curve_recovery_k_zero_is_exactly_inert():
    """§1.5's ablation requirement at the primitive level, asserted EXACTLY (`==`, not `approx`).

    `_recovery_mode_commitment` multiplies by `curve_ease = 1.0 - CURVE_RECOVERY_K * curvature`
    (combat_systems.py:227). At K=0 that must be exactly 1.0, so varying curvature must leave the
    result BIT-identical; at the shipped K it must not. The second half is what makes the first half a
    test rather than a tautology (§0.1 #2).

    Reds on MUT-5a' (engine perturbed by a representable `1e-12*curvature` at K=0). MUT-5b then re-ran
    that SAME mutant with this guard's `==` weakened to `pytest.approx` and it PASSED — which is the
    artifact showing the exactness is load-bearing, not stylistic. It is the defect class §0.1 #2 was
    written about: a 1-ulp aggregate error crossed a damage-degree boundary while its own identity test
    passed. (MUT-5a, at `1e-16`, is an EQUIVALENT mutant — `1.0 + 1.5e-17 == 1.0` in float64 — and is
    recorded as equivalent rather than as a surviving mutant, because those are different findings.)"""
    base = copy.deepcopy(WEAPONS['shamshir'])
    curvatures = (0.0, 0.15, 0.30, 0.45)

    cfg0 = dict(CFG)
    cfg0['CURVE_RECOVERY_K'] = 0.0
    ablated = []
    for curv in curvatures:
        w = copy.deepcopy(base)
        w['geo']['curvature'] = curv
        ablated.append(S._recovery_mode_commitment(w, 0.0, cfg0))
    assert all(v == ablated[0] for v in ablated), (
        f'CURVE_RECOVERY_K=0 is NOT inert — curvature still moved the commitment: {ablated}. '
        f'"Ablatable" (§1.5) means the term vanishes exactly, not approximately.')

    cfg1 = dict(CFG)
    live = []
    for curv in curvatures:
        w = copy.deepcopy(base)
        w['geo']['curvature'] = curv
        live.append(S._recovery_mode_commitment(w, 0.0, cfg1))
    assert cfg1['CURVE_RECOVERY_K'] != 0.0, 'shipped CURVE_RECOVERY_K is 0 — this guard cannot observe'
    assert len(set(live)) == len(curvatures), (
        f'at the shipped CURVE_RECOVERY_K={cfg1["CURVE_RECOVERY_K"]} curvature must still move the '
        f'commitment, else the inertness half above is vacuous: {live}')


# ---------------------------------------------------------------------------
# 6. the three contact-moment gains are applied exactly once, at their real weight
# ---------------------------------------------------------------------------
# NOT DUPLICATED FROM ED-PC-0052 (CLAUDE.md §8). `test_combat_bind_moment.py` already owns
# antisymmetry, scale-invariance, ablatability and the leverage-purity check FOR `BIND_MOMENT_K` — those
# are not re-asserted here. What that suite does NOT cover, and what this section adds:
#   · `PARRY_MOMENT_K` and `WIND_MOMENT_K` had **zero test coverage anywhere** before this file. ED-PC-0052
#     shipped three gains and guarded one.
#   · EXACTLY-ONCE application. The §1.1 hazard is a fact charged twice; nothing checked that a gain is
#     applied once, at the weight its constant names.
#
# The method: replace `contact_moment_edge` with one that returns `real + DELTA` and require the sigma to
# move by exactly the algebraically predicted amount. That is a stronger statement than "the term is
# live" and it cannot be satisfied by a tautology.
_MOMENT_DELTA = 1.0


def _patched_edge(delta):
    """Context-manager-free swap of the module-global `contact_moment_edge` the sigma functions call."""
    real = S.contact_moment_edge

    class _Swap:
        def __enter__(self):
            S.contact_moment_edge = lambda a, b: real(a, b) + delta
            return self

        def __exit__(self, *exc):
            S.contact_moment_edge = real
            return False
    return _Swap()


def _moment_case(gain, a, b, cfg):
    """(sigma_value, attenuation) for the sigma function that consumes `gain`.

    `attenuation` is the factor the gain's contribution is multiplied by before it reaches the returned
    sigma — 1.0 for `bind_sigma`, and the defender's own mode affinity for `mode_sigma`, whose last line
    is `return (base+sig)*cap` (combat_systems.py:356)."""
    if gain == 'BIND_MOMENT_K':
        return S.bind_sigma(a, b, cfg, TR), 1.0
    mode = V.DEF_PARRY if gain == 'PARRY_MOMENT_K' else V.DEF_WIND
    cap = WP.defense_affinities(b.w)[mode]
    return S.mode_sigma(mode, a, b, 3.0, True, 0.0, cfg), cap


@pytest.mark.parametrize('gain', ['BIND_MOMENT_K', 'PARRY_MOMENT_K', 'WIND_MOMENT_K'])
def test_moment_gain_applies_exactly_once(gain):
    """Each ED-PC-0052 gain must be applied ONCE, at exactly `K x attenuation`.

    Two halves, and the second is what makes the first non-vacuous (§0.1 #2):
      · at K=0 the sigma must be BIT-identical with the edge function perturbed — exact inertness,
        which a tautology like `0.0 * edge == 0.0` does not test at all (that was this guard's first
        form; it asserted a property of floating-point multiplication, not of the engine);
      · at the shipped K the sigma must move by exactly `K * DELTA * attenuation`. Applying the gain
        twice, or moving it outside `mode_sigma`'s `*cap`, changes that product and reds this.

    Reds on MUT-7 (duplicate the `sig +=` line) and MUT-8 (drop `*cap` from the expectation)."""
    a = Combatant('A', weapon='falchion')     # highest grip moment among 1H civilian swords (0.2415)
    b = Combatant('B', weapon='tsurugi')      # the lowest (0.1130) — the inversion ED-PC-0052 targets
    assert abs(S.contact_moment_edge(a, b)) > 0.1, 'pairing has no real moment difference to observe'

    cfg_off = dict(CFG)
    cfg_off[gain] = 0.0
    base_off, _ = _moment_case(gain, a, b, cfg_off)
    with _patched_edge(_MOMENT_DELTA):
        pert_off, _ = _moment_case(gain, a, b, cfg_off)
    assert pert_off == base_off, (
        f'{gain}=0 is NOT inert: perturbing contact_moment_edge by {_MOMENT_DELTA} still moved the '
        f'sigma {base_off!r} -> {pert_off!r}. "Ablatable" (§1.5) means exactly zero, and this is '
        f'asserted with `==` rather than `approx` on purpose (§0.1 #2).')

    cfg_on = dict(CFG)
    assert cfg_on[gain] != 0.0, f'shipped {gain} is 0 — this guard cannot observe anything'
    base_on, atten = _moment_case(gain, a, b, cfg_on)
    with _patched_edge(_MOMENT_DELTA):
        pert_on, _ = _moment_case(gain, a, b, cfg_on)
    moved = pert_on - base_on
    expected = cfg_on[gain] * _MOMENT_DELTA * atten
    assert moved == pytest.approx(expected, abs=1e-12), (
        f'{gain} does not apply exactly once at its nominal weight: sigma moved {moved:+.9f} for a '
        f'{_MOMENT_DELTA} edge perturbation, expected {expected:+.9f} '
        f'(K={cfg_on[gain]} x attenuation={atten}). A 2x figure means the gain is charged twice '
        f'(§1.1); a different attenuation means it moved relative to mode_sigma\'s `*cap`.')
    assert math.isfinite(base_on), f'{gain} produced a non-finite sigma: {base_on}'


def test_nominal_moment_gain_parity_is_not_effective_parity():
    """DISCLOSURE, pinned so a later "fix" is deliberate rather than accidental.

    `BIND_MOMENT_K = PARRY_MOMENT_K = WIND_MOMENT_K = 0.30`, and ED-PC-0052's ledger entry presents that
    as considered parity ("its OWN gain — mirroring how the guard fact already carries three gains").
    In effect they are NOT equal: `bind_sigma` returns its terms unattenuated, while `mode_sigma` returns
    `(base+sig)*cap` where `cap` is the defender's own mode affinity. Measured at 8535cea, falchion vs
    tsurugi, for a 1.0 edge perturbation: bind moves 0.300, parry and wind move **0.120** each
    (tsurugi's parry and wind affinities are both exactly 0.40).

    So the effective parry/wind gain is weapon-dependent — rapier's parry affinity is 0.70 against
    tsurugi's 0.40, a 1.75x spread in the *same* declared constant. Whether the moment fact should be
    affinity-attenuated (it is a property of the weapon's mass, not of how well it parries) is a design
    question for the W8c double-count audit, not something to change here.

    This guard pins the structure, not a preference: it fails if the three gains become effectively
    equal, or if the weapon-to-weapon spread disappears."""
    a = Combatant('A', weapon='falchion')
    light_parry = Combatant('B', weapon='tsurugi')
    good_parry = Combatant('B', weapon='rapier')

    cap_tsurugi = WP.defense_affinities(light_parry.w)[V.DEF_PARRY]
    cap_rapier = WP.defense_affinities(good_parry.w)[V.DEF_PARRY]
    assert cap_tsurugi != cap_rapier, (
        f'parry affinity no longer differs between tsurugi ({cap_tsurugi}) and rapier ({cap_rapier}) — '
        f'the spread this guard documents has gone, so the attenuation may have been removed')

    def moved(gain, defender):
        cfg = dict(CFG)
        base, _ = _moment_case(gain, a, defender, cfg)
        with _patched_edge(_MOMENT_DELTA):
            pert, _ = _moment_case(gain, a, defender, cfg)
        return pert - base

    bind = moved('BIND_MOMENT_K', light_parry)
    parry = moved('PARRY_MOMENT_K', light_parry)
    assert CFG['BIND_MOMENT_K'] == CFG['PARRY_MOMENT_K'], (
        'the two constants are no longer nominally equal, so this disclosure needs rewriting')
    assert parry < bind - 1e-9, (
        f'nominal parity is now EFFECTIVE parity: bind moved {bind:+.6f}, parry {parry:+.6f} for the '
        f'same constant and the same perturbation. If mode_sigma stopped attenuating, ED-PC-0052\'s '
        f'effective balance changed and must be re-measured.')

    parry_rapier = moved('PARRY_MOMENT_K', good_parry)
    assert parry_rapier > parry + 1e-9, (
        f'the effective PARRY_MOMENT_K no longer varies by defender weapon '
        f'(tsurugi {parry:+.6f} vs rapier {parry_rapier:+.6f})')
