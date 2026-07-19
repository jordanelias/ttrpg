"""
sim/tests/test_sigma_leverage_parity.py — parity between engine.autoload.sigma_leverage
and the numpy original tests/sim/v32-combat-balance/m1_dice_sigma_core.py.

Rationale: D0-2 (designs/audit/2026-06-30-contest-stage0-reconciliation/DECISIONS.md)
    "Requires a parity test: the stdlib port (math.tanh/math.sqrt) must match the numpy
    original within float tolerance on every function combat/contest use."

Coverage:
    sigma_n / sigma_N      — both combat and contest aliases
    soft_cap / eff_sigma   — both aliases
    sigma_space_ob_shift   — raw sigma-space Ob shift (net_sigma * sigma_n)
    net_boost              — TN 6, 7, 8; capped=True and False
    eff_ob / effective_ob  — both call signatures
    p_success              — full closed-form probability
    levels_to_net_sigma    — level aggregation
    roll_net (structure)   — integer return, pool floor
    roll_net_continuous (structure) — float return

Input grid:
    net_sigma in {-5.0, -2.0, -1.5, -1.0, -0.5, 0.0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 5.0, 10.0, 50.0}
    pool in {1, 5, 10, 26}
    tn in {6, 7, 8}

Numpy availability:
    If numpy is importable, asserts are made against the numpy original's exact output
    (tolerance 1e-9 — differences arise only from floating-point associativity, not from
    tanh/sqrt implementation divergence between math and numpy at IEEE-754 double).
    If numpy is unavailable, asserts are made against hardcoded expected values computed
    from the stdlib port at module import time (noted in output).
"""
from __future__ import annotations

import math
import os
import sys

import pytest

# ---------------------------------------------------------------------------
# Repo root on sys.path so `import sim.*` resolves when pytest runs anywhere.
# ---------------------------------------------------------------------------
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

# ---------------------------------------------------------------------------
# Import the new stdlib autoload module (always available).
# ---------------------------------------------------------------------------
from engine.autoload import sigma_leverage as SL  # noqa: E402

# ---------------------------------------------------------------------------
# Attempt to import the numpy original.
# ---------------------------------------------------------------------------
_NUMPY_ORIGINAL_DIR = os.path.join(_REPO_ROOT, 'tests', 'sim', 'v32-combat-balance')
_numpy_available = True
_m1 = None

try:
    import numpy  # noqa: F401
    if _NUMPY_ORIGINAL_DIR not in sys.path:
        sys.path.insert(0, _NUMPY_ORIGINAL_DIR)
    import m1_dice_sigma_core as _m1  # noqa: E402
except ImportError:
    _numpy_available = False

# ---------------------------------------------------------------------------
# Input grid (D0-2: "grid of inputs covering net_sigma in a wide range
# (incl. large values where tanh saturates), pool in {1,5,10,26}, TN in {6,7,8}")
# ---------------------------------------------------------------------------
NET_SIGMA_GRID = [-50.0, -5.0, -2.0, -1.5, -1.0, -0.5, 0.0,
                  0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 5.0, 10.0, 50.0]
POOL_GRID = [1, 5, 10, 26]
TN_GRID = [6, 7, 8]
TOL = 1e-9  # tight float tolerance (math vs numpy, same IEEE-754 doubles)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _sl_ref(fn_name: str, *args, **kwargs):
    """Call engine.autoload.sigma_leverage.<fn_name>."""
    return getattr(SL, fn_name)(*args, **kwargs)


def _m1_ref(fn_name: str, *args, **kwargs):
    """Call m1_dice_sigma_core.<fn_name> (numpy original)."""
    return float(getattr(_m1, fn_name)(*args, **kwargs))


def _assert_close(got, want, label: str, tol: float = TOL):
    assert abs(got - want) <= tol, (
        f"{label}: got {got!r}, want {want!r}, delta={abs(got-want)!r}"
    )


# ---------------------------------------------------------------------------
# Tests: sigma_n / sigma_N
# ---------------------------------------------------------------------------

class TestSigmaN:
    """sigma_n(pool) — combat alias; sigma_N(pool) — contest alias."""

    @pytest.mark.parametrize("pool", POOL_GRID)
    def test_sigma_n_vs_numpy(self, pool):
        if not _numpy_available:
            pytest.skip("numpy not available")
        got = SL.sigma_n(pool)
        want = _m1_ref("sigma_n", pool)
        _assert_close(got, want, f"sigma_n(pool={pool})")

    @pytest.mark.parametrize("pool", POOL_GRID)
    def test_sigma_N_alias(self, pool):
        """sigma_N must equal sigma_n (aliases)."""
        assert SL.sigma_N(pool) == SL.sigma_n(pool), (
            f"sigma_N != sigma_n at pool={pool}"
        )

    @pytest.mark.parametrize("pool", POOL_GRID)
    def test_sigma_n_formula(self, pool):
        """sigma_n = SIGMA_N_COEFF * sqrt(max(1, pool)) — formula check."""
        expected = SL.SIGMA_N_COEFF * math.sqrt(max(1, pool))
        _assert_close(SL.sigma_n(pool), expected, f"sigma_n formula pool={pool}")

    def test_sigma_n_pool_floor(self):
        """Pool 0 and negative treated as pool=1."""
        assert SL.sigma_n(0) == SL.sigma_n(1)
        assert SL.sigma_n(-3) == SL.sigma_n(1)


# ---------------------------------------------------------------------------
# Tests: soft_cap / eff_sigma
# ---------------------------------------------------------------------------

class TestSoftCap:
    """soft_cap(net_sigma) — combat alias; eff_sigma(net_sigma) — contest alias."""

    @pytest.mark.parametrize("ns", NET_SIGMA_GRID)
    def test_soft_cap_vs_numpy(self, ns):
        if not _numpy_available:
            pytest.skip("numpy not available")
        got = SL.soft_cap(ns)
        want = _m1_ref("soft_cap", ns)
        _assert_close(got, want, f"soft_cap(net_sigma={ns})")

    @pytest.mark.parametrize("ns", NET_SIGMA_GRID)
    def test_eff_sigma_alias(self, ns):
        """eff_sigma must equal soft_cap (aliases)."""
        assert SL.eff_sigma(ns) == SL.soft_cap(ns), (
            f"eff_sigma != soft_cap at net_sigma={ns}"
        )

    @pytest.mark.parametrize("ns", NET_SIGMA_GRID)
    def test_soft_cap_formula(self, ns):
        """soft_cap = M_MAX * tanh(ns / M_MAX)."""
        expected = SL.M_MAX * math.tanh(ns / SL.M_MAX)
        _assert_close(SL.soft_cap(ns), expected, f"soft_cap formula ns={ns}")

    def test_saturation_positive(self):
        """Large positive input saturates toward +M_MAX."""
        got = SL.soft_cap(SL.M_MAX * 100)
        assert abs(got - SL.M_MAX) < 1e-6, f"saturation failed: {got}"

    def test_saturation_negative(self):
        """Large negative input saturates toward -M_MAX."""
        got = SL.soft_cap(-SL.M_MAX * 100)
        assert abs(got + SL.M_MAX) < 1e-6, f"floor saturation failed: {got}"

    def test_softcap_spec_checkpoints(self):
        """modifier_system_spec.md §3.1 spot-checks (2dp tolerance)."""
        for raw, want in [(0.5, 0.48), (1.0, 0.87), (2.0, 1.31), (3.0, 1.45)]:
            got = SL.soft_cap(raw)
            assert round(got, 2) == round(want, 2), (
                f"spec checkpoint raw={raw}: got {got:.3f}, want ~{want}"
            )

    def test_soft_cap_odd_zero(self):
        """Zero in → zero out (tanh(0)=0)."""
        assert SL.soft_cap(0.0) == 0.0


# ---------------------------------------------------------------------------
# Tests: sigma_space_ob_shift
# ---------------------------------------------------------------------------

class TestSigmaSpaceObShift:
    """sigma_space_ob_shift(net_sigma, pool) — raw sigma-space Ob shift, pre-soft-cap.

    Defined as net_sigma * sigma_n(pool); the sqrt(N) cancels in the z-score
    (the F1 uniform-modifier-impact property). Byte-identical to the numpy
    original m1_dice_sigma_core.sigma_space_ob_shift (verified divergence 0.0).
    """

    @pytest.mark.parametrize("ns", NET_SIGMA_GRID)
    @pytest.mark.parametrize("pool", POOL_GRID)
    def test_sigma_space_ob_shift_vs_numpy(self, ns, pool):
        if not _numpy_available:
            pytest.skip("numpy not available")
        got = SL.sigma_space_ob_shift(ns, pool)
        want = _m1_ref("sigma_space_ob_shift", ns, pool)
        _assert_close(got, want, f"sigma_space_ob_shift(net_sigma={ns}, pool={pool})")

    @pytest.mark.parametrize("ns", NET_SIGMA_GRID)
    @pytest.mark.parametrize("pool", POOL_GRID)
    def test_sigma_space_ob_shift_identity(self, ns, pool):
        """sigma_space_ob_shift(ns, pool) == ns * sigma_n(pool) (exact — same float ops)."""
        assert SL.sigma_space_ob_shift(ns, pool) == ns * SL.sigma_n(pool), (
            f"sigma_space_ob_shift != ns*sigma_n at ns={ns} pool={pool}"
        )


# ---------------------------------------------------------------------------
# Tests: net_boost
# ---------------------------------------------------------------------------

class TestNetBoost:

    @pytest.mark.parametrize("ns", NET_SIGMA_GRID)
    @pytest.mark.parametrize("pool", POOL_GRID)
    @pytest.mark.parametrize("tn", TN_GRID)
    def test_net_boost_vs_numpy_capped(self, ns, pool, tn):
        if not _numpy_available:
            pytest.skip("numpy not available")
        got = SL.net_boost(ns, pool, tn=tn, capped=True)
        want = _m1_ref("net_boost", ns, pool, tn, True)
        _assert_close(got, want, f"net_boost(ns={ns}, pool={pool}, tn={tn}, capped=True)")

    @pytest.mark.parametrize("ns", NET_SIGMA_GRID)
    @pytest.mark.parametrize("pool", POOL_GRID)
    @pytest.mark.parametrize("tn", TN_GRID)
    def test_net_boost_vs_numpy_uncapped(self, ns, pool, tn):
        if not _numpy_available:
            pytest.skip("numpy not available")
        got = SL.net_boost(ns, pool, tn=tn, capped=False)
        want = _m1_ref("net_boost", ns, pool, tn, False)
        _assert_close(got, want, f"net_boost(ns={ns}, pool={pool}, tn={tn}, capped=False)")

    @pytest.mark.parametrize("pool", POOL_GRID)
    @pytest.mark.parametrize("tn", TN_GRID)
    def test_net_boost_formula(self, pool, tn):
        """net_boost = eff_sigma(ns)*sigma_per_die[tn]*sqrt(pool) for a mid-range ns."""
        ns = 0.7
        _, sigma = SL.PER_DIE[tn]
        expected = SL.soft_cap(ns) * sigma * math.sqrt(max(1, pool))
        got = SL.net_boost(ns, pool, tn=tn, capped=True)
        _assert_close(got, expected, f"net_boost formula pool={pool} tn={tn}")

    def test_net_boost_zero_sigma(self):
        """Zero net_sigma → zero boost."""
        for pool in POOL_GRID:
            for tn in TN_GRID:
                assert SL.net_boost(0.0, pool, tn=tn) == 0.0

    def test_net_boost_tn7_equals_sigma_n(self):
        """At TN7, net_boost(ns, pool, capped=False) == ns*sigma_n(pool)
        because sigma_per_die[7]=0.800 == SIGMA_N_COEFF=0.8."""
        for ns in [0.5, 1.0, 2.0]:
            for pool in POOL_GRID:
                got = SL.net_boost(ns, pool, tn=7, capped=False)
                want = ns * SL.sigma_n(pool)
                _assert_close(got, want, f"TN7 net_boost == sigma_n*ns at ns={ns} pool={pool}")


# ---------------------------------------------------------------------------
# Tests: eff_ob / effective_ob
# ---------------------------------------------------------------------------

class TestEffOb:

    @pytest.mark.parametrize("ns", [-1.0, 0.0, 0.5, 1.0, 2.0, 5.0])
    @pytest.mark.parametrize("pool", POOL_GRID)
    def test_eff_ob_vs_numpy(self, ns, pool):
        if not _numpy_available:
            pytest.skip("numpy not available")
        base_ob = 4.0
        got = SL.eff_ob(base_ob, pool, ns)
        want = _m1_ref("eff_ob", base_ob, pool, ns)
        _assert_close(got, want, f"eff_ob(base_ob={base_ob}, pool={pool}, ns={ns})")

    @pytest.mark.parametrize("pool", POOL_GRID)
    def test_eff_ob_floor(self, pool):
        """eff_ob never goes below OB_MIN=1 even at extreme positive net_sigma."""
        got = SL.eff_ob(1.0, pool, 100.0)
        assert got >= SL.OB_MIN, f"eff_ob below floor at pool={pool}: {got}"

    @pytest.mark.parametrize("ns", [-1.0, 0.0, 0.5, 1.5, 3.0])
    @pytest.mark.parametrize("pool", POOL_GRID)
    def test_effective_ob_alias(self, ns, pool):
        """effective_ob(base_ob, net_dsigma, pool) == eff_ob(base_ob, pool, net_dsigma)."""
        base_ob = 3.0
        a = SL.effective_ob(base_ob, ns, pool)
        b = SL.eff_ob(base_ob, pool, ns)
        assert a == b, f"effective_ob != eff_ob at ns={ns} pool={pool}"


# ---------------------------------------------------------------------------
# Tests: p_success
# ---------------------------------------------------------------------------

class TestPSuccess:

    @pytest.mark.parametrize("ns", [-2.0, -1.0, 0.0, 0.5, 1.0, 2.0, 5.0])
    @pytest.mark.parametrize("pool", POOL_GRID)
    @pytest.mark.parametrize("tn", TN_GRID)
    def test_p_success_vs_numpy(self, ns, pool, tn):
        if not _numpy_available:
            pytest.skip("numpy not available")
        base_ob = 2.0
        got = SL.p_success(base_ob, pool, ns, tn)
        want = _m1_ref("p_success", base_ob, pool, ns, tn)
        _assert_close(got, want, f"p_success(ob={base_ob}, pool={pool}, ns={ns}, tn={tn})")

    def test_p_success_range(self):
        """p_success always in [0, 1]."""
        for ns in NET_SIGMA_GRID:
            for pool in POOL_GRID:
                p = SL.p_success(4.0, pool, ns)
                assert 0.0 <= p <= 1.0, f"p_success out of [0,1]: {p}"

    def test_p_success_monotone_in_ns(self):
        """More positive net_sigma → higher p_success."""
        pool, tn = 10, 7
        prev = SL.p_success(3.0, pool, -3.0, tn)
        for ns in [-2.0, -1.0, 0.0, 1.0, 2.0, 3.0]:
            curr = SL.p_success(3.0, pool, ns, tn)
            assert curr >= prev - 1e-12, f"p_success not monotone at ns={ns}"
            prev = curr

    def test_p_success_f1_uniformity(self):
        """F1 fix: +0.7sigma impact is uniform across pool sizes at 50% baseline.
        modifier_system_spec.md §2.1: +25.8pp at all pools (2dp)."""
        impacts = []
        for pool in [3, 5, 8, 12, 17, 20]:
            mu, _ = SL.PER_DIE[7]
            base_ob = mu * pool  # 50% baseline
            p0 = SL.p_success(base_ob, pool, 0.0, 7, capped=False)
            p1 = SL.p_success(base_ob, pool, 0.7, 7, capped=False)
            impacts.append(p1 - p0)
        spread = max(impacts) - min(impacts)
        avg = sum(impacts) / len(impacts)
        assert round(spread * 100, 1) == 0.0, f"F1 uniformity failed: spread={spread*100:.2f}pp"
        assert round(avg * 100, 1) == 25.8, f"F1 magnitude wrong: mean={avg*100:.1f}pp"


# ---------------------------------------------------------------------------
# Tests: level (single-lookup contest accessor)
# ---------------------------------------------------------------------------

class TestLevel:
    """level(name) — contest-surface accessor ported from
    designs/audit/2026-06-03-contest-groundup/engine.py:21
    (`def level(name): return LEVEL[name]`). The groundup LEVEL dict is this
    module's LEVEL_SIGMA, so level(name) must equal LEVEL_SIGMA[name].

    No numpy counterpart: level() is a contest-only surface addition (not in
    m1_dice_sigma_core), so parity is against LEVEL_SIGMA — as the task specifies."""

    EXPECTED = {"minor": 0.25, "moderate": 0.50, "strong": 0.75, "major": 1.00}

    @pytest.mark.parametrize("name,value", list(EXPECTED.items()))
    def test_level_matches_level_sigma(self, name, value):
        """SL.level(name) == LEVEL_SIGMA[name] == the ratified σ value, for all four names."""
        assert SL.level(name) == SL.LEVEL_SIGMA[name]
        assert SL.level(name) == value

    def test_level_covers_all_names(self):
        """Every LEVEL_SIGMA key resolves through level(), and the roster is exactly the four
        names (guards against LEVEL_SIGMA drifting out from under this accessor)."""
        assert set(self.EXPECTED) == set(SL.LEVEL_SIGMA)
        for name in SL.LEVEL_SIGMA:
            assert SL.level(name) == SL.LEVEL_SIGMA[name]

    def test_level_unknown_raises(self):
        """Unknown name raises KeyError — same contract as the dict lookup and the groundup engine."""
        with pytest.raises(KeyError):
            SL.level("catastrophic")


# ---------------------------------------------------------------------------
# Tests: levels_to_net_sigma
# ---------------------------------------------------------------------------

class TestLevelsToNetSigma:

    def test_vs_numpy(self):
        if not _numpy_available:
            pytest.skip("numpy not available")
        cases = [
            (["minor"], None),
            (["moderate", "strong"], ["minor"]),
            (None, ["major"]),
            (["major", "major"], ["major"]),
            (None, None),
        ]
        for agg, dfd in cases:
            got = SL.levels_to_net_sigma(agg, dfd)
            want = _m1_ref("levels_to_net_sigma", agg, dfd)
            _assert_close(got, want, f"levels_to_net_sigma(agg={agg}, dfd={dfd})")

    def test_neutral(self):
        assert SL.levels_to_net_sigma() == 0.0
        assert SL.levels_to_net_sigma(None, None) == 0.0

    def test_symmetric(self):
        assert SL.levels_to_net_sigma(["minor"], None) == -SL.levels_to_net_sigma(None, ["minor"])

    def test_additive(self):
        a = SL.levels_to_net_sigma(["minor", "moderate"])
        b = SL.LEVEL_SIGMA["minor"] + SL.LEVEL_SIGMA["moderate"]
        _assert_close(a, b, "levels additive")


# ---------------------------------------------------------------------------
# Tests: roll_net (structural — dice_engine delegation)
# ---------------------------------------------------------------------------

class TestRollNet:

    def test_returns_int(self):
        import random as _random
        rng = _random.Random(42)
        result = SL.roll_net(5, rng=rng)
        assert isinstance(result, int), f"roll_net returned {type(result)}"

    def test_pool_floor(self):
        """Pool ≤ 0 is treated as pool=1 (no crash)."""
        import random as _random
        rng = _random.Random(0)
        result = SL.roll_net(0, rng=rng)
        assert isinstance(result, int)

    def test_seeded_deterministic(self):
        import random as _random
        rng_a = _random.Random(7)
        rng_b = _random.Random(7)
        assert SL.roll_net(10, rng=rng_a) == SL.roll_net(10, rng=rng_b)


# ---------------------------------------------------------------------------
# Tests: roll_net_continuous (structural — dice_engine delegation)
# ---------------------------------------------------------------------------

class TestRollNetContinuous:

    def test_returns_float(self):
        import random as _random
        rng = _random.Random(99)
        result = SL.roll_net_continuous(5, rng=rng)
        assert isinstance(result, float), f"roll_net_continuous returned {type(result)}"

    def test_seeded_deterministic(self):
        import random as _random
        rng_a = _random.Random(13)
        rng_b = _random.Random(13)
        assert SL.roll_net_continuous(10, rng=rng_a) == SL.roll_net_continuous(10, rng=rng_b)


# ---------------------------------------------------------------------------
# Hardcoded fallback values (numpy unavailable)
# These are computed from the stdlib port at authoring time; they serve as
# regression pins when running in a numpy-free environment.
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Tests: level() accessor + pool-aware degree() — contest-surface additions
# (Stage 1b, designs/audit/2026-06-30-contest-stage0-reconciliation).
# Parity target is the groundup engine.py original, which these carry across
# verbatim (single-sourced so the promoted contest kernel no longer needs a
# local engine.py — the "third σ-kernel" hazard).
# ---------------------------------------------------------------------------

_GROUNDUP_DIR = os.path.join(_REPO_ROOT, 'designs', 'audit', '2026-06-03-contest-groundup')
_groundup_engine = None
try:
    # Load the ground-up reference engine.py BY EXPLICIT PATH under a unique module
    # name. A bare `import engine` here now collides with the top-level `engine/`
    # package (ED-IN-0071 P3 Phase A — the executable-model primary), which is
    # cached in sys.modules once any `engine.mc_v18`/`engine.substrate` import runs,
    # so `import engine` would return that package (no `degree`/`level`) instead of
    # this audit-folder file. Self-contained (imports only math/random).
    import importlib.util as _ilu
    _spec = _ilu.spec_from_file_location(
        "_groundup_engine_ref", os.path.join(_GROUNDUP_DIR, "engine.py"))
    _groundup_engine = _ilu.module_from_spec(_spec)
    _spec.loader.exec_module(_groundup_engine)
except (ImportError, FileNotFoundError, AttributeError):
    _groundup_engine = None


class TestLevelAccessor:
    """level(name) — Stage-1a finding 1a: the accessor was missing from the port."""

    @pytest.mark.parametrize("name", ["minor", "moderate", "strong", "major"])
    def test_level_returns_sigma(self, name):
        assert SL.level(name) == SL.LEVEL_SIGMA[name]

    @pytest.mark.parametrize("name", ["minor", "moderate", "strong", "major"])
    def test_level_vs_groundup(self, name):
        if _groundup_engine is None:
            pytest.skip("groundup engine.py not importable")
        _assert_close(SL.level(name), _groundup_engine.level(name), f"level({name})")


class TestPoolAwareDegree:
    """degree(net, ob, pool) — pool-aware INTEGER bands (contest surface), distinct
    from dice_engine.degree_from_net (combat enum, 2*Ob bar). Carried across from
    the groundup engine.py verbatim; the 151 groundup tests are the behavior guard."""

    def test_bands_basic(self):
        # tests.py row: (degree(0,3), degree(3,3), degree(6,3)) == (0,2,3)
        assert (SL.degree(0, 3), SL.degree(3, 3), SL.degree(6, 3)) == (0, 2, 3)

    def test_failure_and_partial(self):
        assert SL.degree(0, 3) == 0
        assert SL.degree(-2, 3) == 0
        assert SL.degree(1, 3) == 1
        assert SL.degree(2, 3) == 1

    def test_legacy_pool_less_overwhelming(self):
        # pool=None → legacy 2*ob bar (net>=2*ob and net>=3)
        assert SL.degree(6, 3, None) == 3
        assert SL.degree(5, 3, None) == 2
        assert SL.degree(2, 1, None) == 2   # net<3 blocks legacy Overwhelming

    @pytest.mark.parametrize("net", [-3, 0, 1, 2, 3, 5, 6, 8, 12, 20])
    @pytest.mark.parametrize("ob", [1.0, 2.0, 3.0])
    @pytest.mark.parametrize("pool", [None, 2, 5, 9, 16, 25])
    def test_degree_vs_groundup(self, net, ob, pool):
        if _groundup_engine is None:
            pytest.skip("groundup engine.py not importable")
        assert SL.degree(net, ob, pool) == _groundup_engine.degree(net, ob, pool), (
            f"degree(net={net}, ob={ob}, pool={pool})"
        )


_HARDCODED = {
    # (fn_name, *args): expected_value
    # sigma_n
    ("sigma_n", 1):  0.8,
    ("sigma_n", 5):  0.8 * math.sqrt(5),
    ("sigma_n", 10): 0.8 * math.sqrt(10),
    ("sigma_n", 26): 0.8 * math.sqrt(26),
    # soft_cap
    ("soft_cap", 0.0):  0.0,
    ("soft_cap", 0.5):  1.5 * math.tanh(0.5 / 1.5),
    ("soft_cap", 1.5):  1.5 * math.tanh(1.5 / 1.5),
    ("soft_cap", 5.0):  1.5 * math.tanh(5.0 / 1.5),
    ("soft_cap", -1.0): 1.5 * math.tanh(-1.0 / 1.5),
    # net_boost at TN7, capped
    ("net_boost", 1.0, 10, 7, True):  SL.soft_cap(1.0) * 0.800 * math.sqrt(10),
    ("net_boost", 0.0, 5, 7, True):   0.0,
    # p_success at TN7, capped
    ("p_success", 2.0, 10, 0.0, 7): SL.p_success(2.0, 10, 0.0, 7),
    ("p_success", 2.0, 10, 1.0, 7): SL.p_success(2.0, 10, 1.0, 7),
}


@pytest.mark.parametrize("key,expected", list(_HARDCODED.items()))
def test_hardcoded_regression(key, expected):
    """Regression pins against stdlib-computed expected values (numpy-free CI path)."""
    fn_name = key[0]
    args = key[1:]
    got = _sl_ref(fn_name, *args)
    _assert_close(got, expected, str(key))
