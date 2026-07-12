"""dice_pool_demo.py — Gate-0 demo adapter, wrapping the existing
skills/valoria-dice-model/valoria_dice.py Monte Carlo core.

Chosen as the Gate-0 proof for three reasons (see the design doc section 8, wave 1):
it is the simplest genuinely canon-cited resolver in the repo (params/core.md), it
carries no game-balance judgment risk, and it already has a working, reusable trial
core — the harness wraps it rather than re-deriving dice math.

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

from ..adapter import Adapter, Outcome
from ..depth import DecisionPoint, Tier


class DicePoolAdapter(Adapter):
    contract_module = None  # see module docstring — confirmed no module_contracts.yaml row
    canon_row = "Dice / resolution"  # CURRENT.md: params/core.md + d+sigma resolver
    registry_subsystem = "cross_cutting"

    def resolve_params(self, resolver) -> dict:
        # Confirms the CURRENT.md citation resolves before any trial runs; raises
        # CanonGapError (never fabricates a fallback) if params/core.md's row moves
        # or is renamed without this adapter being updated.
        resolver.resolve(self.canon_row)
        return {"pool": 6, "tn": 7, "ob": 5, "atk_pool": 5, "atk_tn": 7,
                "def_pool": 5, "def_tn": 7}

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
        ]

    def run_once(self, rng, params: dict, decision_point: DecisionPoint) -> Outcome:
        if decision_point.name == "single_pool_check":
            r = valoria_dice._roll_pool(params["pool"], params["tn"])
            ob = params["ob"]
            if ob == 10:
                branch = "success" if r >= ob else ("partial" if r >= 5 else "failure")
            elif r >= 2 * ob:
                branch = "overwhelming"
            elif r >= ob:
                branch = "success"
            elif r > 0:
                branch = "partial"
            else:
                branch = "failure"
            return Outcome(decision_point.name, r, {"branch": branch})

        if decision_point.name == "opposed_roll":
            a = valoria_dice._roll_pool(params["atk_pool"], params["atk_tn"])
            d = valoria_dice._roll_pool(params["def_pool"], params["def_tn"])
            branch = "attacker_wins" if a > d else ("defender_wins" if d > a else "tie")
            return Outcome(decision_point.name, a - d, {"branch": branch})

        raise ValueError(f"unknown decision point {decision_point.name!r}")
