"""
ED-871 regression: Mending costs 0 Coherence at every degree (restorative operation).

WHY THIS EXISTS
---------------
ED-871 (ruled 2026-05-31) established that Mending, as a RESTORATIVE operation type, costs
0 Coherence regardless of Gap scale or degree (canon/02 Amendment 3 — operation type, not
scale, determines Coherence risk). The ruling sat unexecuted in the sim for 5+ weeks: the
audit (U-6 / C-TW-2 / C-VERIFY-13) found attempt_mending charged -1 base and, via the shared
blanket Partial/Failure degree-penalty in _resolve_operation, -2 on a bad roll. The doc side
was propagated 2026-07-07 (threadwork_v30 §3.2 + params/threadwork.md); this pins the sim
side, which had ZERO test coverage (sim/thread was a total island).

NOTE: the fix exempts ONLY Mending from the blanket penalty. The separate C-TW-3 defect —
the same blanket penalty mis-hits Leap against its own "Failure does NOT cost Coherence"
docstring — is intentionally NOT fixed here (ED-WR-0005 Stratum-B tail).
"""
import os
import sys
import random

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from systems.threadwork.sim.operations import attempt_mending, attempt_weaving  # noqa: E402


class _Practitioner:
    """Duck-typed actor per operations.py's [ASSUMPTION] contract."""

    def __init__(self, actor_id="prac", spirit=4, ts=30, history=0):
        self.actor_id = actor_id
        self.spirit = spirit
        self.ts = ts
        self.history = history


def test_ed871_mending_zero_coherence_every_degree():
    """attempt_mending nets 0 Coherence for ALL degrees, including Partial/Failure."""
    degrees = set()
    for seed in range(300):
        r = attempt_mending(_Practitioner(), {"scale": "Relational"}, rng=random.Random(seed))
        degrees.add(r.degree)
        assert r.coherence_delta == 0, (
            f"Mending {r.degree} cost {r.coherence_delta} Coherence — ED-871 requires 0 at every degree"
        )
    # The exemption only matters if bad rolls actually occur — prove Partial/Failure are hit.
    assert degrees & {"Partial", "Failure"}, f"no Partial/Failure degree exercised (got {degrees})"


def test_ed871_exemption_is_mending_only():
    """The blanket Partial/Failure Coherence penalty still fires for non-Mending ops.

    Weaving at Relational scale: base -1; on Partial/Failure the blanket penalty adds -1 (net -2);
    on Success/Overwhelming it stays -1. Guards against the exemption accidentally disabling the
    penalty for every operation.
    """
    saw_penalized = False
    for seed in range(300):
        r = attempt_weaving(_Practitioner(), {"scale": "Relational"}, rng=random.Random(seed))
        if r.degree in ("Partial", "Failure"):
            assert r.coherence_delta == -2, (
                f"Weaving {r.degree} cost {r.coherence_delta}; expected -2 (base -1 + blanket -1) "
                "— the ED-871 exemption must be Mending-only"
            )
            saw_penalized = True
        else:
            assert r.coherence_delta == -1, f"Weaving {r.degree} cost {r.coherence_delta}; expected -1"
    assert saw_penalized, "no Weaving Partial/Failure exercised — cannot confirm the penalty still fires"
