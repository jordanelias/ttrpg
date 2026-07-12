"""dice_pool_demo.py — Gate-0 demo adapter, wrapping the existing
skills/valoria-dice-model/valoria_dice.py Monte Carlo core.

Chosen as the Gate-0 proof for three reasons (see the design doc section 8, wave 1):
it is the simplest genuinely canon-cited resolver in the repo (params/core.md), it
carries no game-balance judgment risk, and it already has a working, reusable trial
core — the harness wraps it rather than re-deriving dice math.

Canon-fidelity discipline: resolve_params() distinguishes two kinds of values.
TN=7 ("Standard") and Ob=5 ("Entrenched") are genuine documented constants in
params/core.md's TN Values / Obstacle Scale tables — resolve_params() calls
resolver.verify_citation(...) to confirm each is STILL literally present in that
doc before trusting it, rather than hardcoding a number that could silently go
stale. Pool sizes (pool/atk_pool/def_pool), by contrast, are NOT a fixed canon
constant anywhere in params/core.md — dice pool size is character-build-dependent
(attribute + skill + situational modifiers), so there is no single "the" canonical
pool size to cite. Those are declared, explicit test-scenario values, and their
provenance entries say so plainly instead of implying a citation that doesn't exist.

Real, confirmed finding this adapter surfaces on its own: dice-pool resolution is
cross-cutting substrate with NO row of its own in references/module_contracts.yaml
(grepped for dice/roll/resolution/core across all 27 module names — zero matches).
contract_module is therefore explicitly None here, not a placeholder — see
Adapter.contract_module's docstring for why that's a deliberate opt-out the harness
logs rather than a silent skip.
"""
from __future__ import annotations

import sys
from pathlib import Path

_SKILL_DIR = Path(__file__).resolve().parents[3] / "skills" / "valoria-dice-model"
if str(_SKILL_DIR) not in sys.path:
    sys.path.insert(0, str(_SKILL_DIR))
import valoria_dice  # noqa: E402  (skills/valoria-dice-model/valoria_dice.py)

from ..adapter import Adapter, Outcome, register_adapter
from ..depth import DecisionPoint, Tier


@register_adapter("dice_pool_demo")
class DicePoolAdapter(Adapter):
    contract_module = None  # see module docstring — confirmed no module_contracts.yaml row
    canon_row = "Dice / resolution"  # CURRENT.md: params/core.md + d+sigma resolver
    registry_subsystem = "cross_cutting"

    def resolve_params(self, resolver) -> tuple[dict, dict]:
        std_tn = resolver.verify_citation(
            self.canon_row, "params/core.md", "| Standard | 7 | Default |",
        )
        entrenched_ob = resolver.verify_citation(
            self.canon_row, "params/core.md", "| 5 | Entrenched |",
        )
        params = {
            "pool": 6, "tn": 7, "ob": 5,
            "atk_pool": 5, "atk_tn": 7,
            "def_pool": 5, "def_tn": 7,
        }
        provenance = {
            "pool": "test-scenario value, not canon-derived: dice pool size is "
                    "character-build-dependent (attribute+skill+situational), "
                    "params/core.md defines no single fixed pool size",
            "tn": f"params/core.md verified: {std_tn!r} (TN Values / Standard)",
            "ob": f"params/core.md verified: {entrenched_ob!r} (Obstacle Scale / Entrenched)",
            "atk_pool": "test-scenario value, not canon-derived: see 'pool'",
            "atk_tn": f"params/core.md verified: {std_tn!r} (TN Values / Standard)",
            "def_pool": "test-scenario value, not canon-derived: see 'pool'",
            "def_tn": f"params/core.md verified: {std_tn!r} (TN Values / Standard)",
        }
        return params, provenance

    def decision_points(self) -> list[DecisionPoint]:
        return [
            DecisionPoint(
                name="single_pool_check",
                default_tier=Tier.MINOR,
                branches=["overwhelming", "success", "partial", "failure"],
                justification="a single skill check is locally reversible next tick",
            ),
            DecisionPoint(
                name="opposed_roll",
                default_tier=Tier.MEDIUM,
                branches=["attacker_wins", "defender_wins", "tie"],
                justification="an opposed roll's result is consumed by a caller "
                               "outside this event, per the harness rubric default",
            ),
            DecisionPoint(
                name="stub_probe",
                default_tier=Tier.MINOR,
                branches=[],
                justification="synthetic probe, not a real subsystem event: "
                               "deliberately raises NotImplementedError so Gate-0 "
                               "ships a real, working end-to-end demonstration of "
                               "the harness's automatic STUB_HIT capture (Harness."
                               "_run_one_trial's except NotImplementedError clause) "
                               "instead of only a theoretical claim about it",
            ),
        ]

    def run_once(self, rng, params: dict, decision_point: DecisionPoint) -> Outcome:
        # rng is passed through explicitly to valoria_dice's roll functions rather
        # than relying on the harness's global random.seed() call alone — that call
        # still happens (belt-and-suspenders for any code that reads global random
        # state some other way) but this adapter's own determinism no longer
        # depends on it silently continuing to happen.
        if decision_point.name == "single_pool_check":
            r = valoria_dice.roll_pool(params["pool"], params["tn"], rng)
            branch = valoria_dice.classify_outcome(r, params["ob"])
            return Outcome(decision_point.name, r, {"branch": branch})

        if decision_point.name == "opposed_roll":
            a = valoria_dice.roll_pool(params["atk_pool"], params["atk_tn"], rng)
            d = valoria_dice.roll_pool(params["def_pool"], params["def_tn"], rng)
            branch = "attacker_wins" if a > d else ("defender_wins" if d > a else "tie")
            return Outcome(decision_point.name, a - d, {"branch": branch})

        if decision_point.name == "stub_probe":
            raise NotImplementedError(
                "Gate-0 synthetic probe — not a real subsystem gap, demonstrates "
                "STUB_HIT capture end-to-end"
            )

        raise ValueError(f"unknown decision point {decision_point.name!r}")
