"""pr119_pressure_homeostat.py — provisional adapter re-testing the Pi (pressure) homeostat
formula from systems/settlements/goldenfurt_slice/sim_build_spec.md §5, the CG-1-fixed
bidirectional restoring term:

    Pi_next = clamp(Pi + unserved_needs + active_grudges + ambitions_in_motion + external_shock
                     - player_releases + restore_toward(3), 0, 10)
    restore_toward(3) := sign(3 - Pi) * min(1, abs(3 - Pi))

This is the formula the reconciliation doc credits with ALREADY FIXING PR#125's #1 finding
("Pi death-spiral / no circuit-breaker") — but that credit was argued by reading the spec
prose, not by running the formula. This adapter transcribes it verbatim and Monte Carlo's a
multi-season trajectory from Goldenfurt's real opening Pi=4 (goldenfurt_fixture.py), giving a
THIRD independent, code-executed data point alongside PR#125's LLM-narrative sim and the prior
500-seed settlement_mgmt_stress_01 batch — both of which found a negative-death-spiral bias
under the PRE-CG-1 (mis-signed) formula.

Sim code for governance_play_redesign_v1.md §1-6 (the deck engine, ambition tick, per-season
pressure inputs) is not yet built (goldenfurt_slice/README.md: "S0-S1 are now built ... Next,
in order: S2 governance verbs ... S4 deck engine ... S5 NPC ambition tick"). The per-season
input terms below are therefore explicit test-scenario stochastic proxies for those inputs,
not derived from a real deck/ambition-tick run — documented per-term below, not hidden.

canon_row=None: sim_build_spec.md is a PROPOSAL doc (goldenfurt_slice/README.md), no
CURRENT.md row.
"""
from __future__ import annotations

from ...adapter import Adapter, Outcome, register_adapter
from ...depth import DecisionPoint, Tier
from .goldenfurt_fixture import NPCS, build_goldenfurt_settlement


def _restore_toward(pi: float, target: float = 3.0) -> float:
    """Verbatim transcription of sim_build_spec.md §5's CG-1 fix:
    restore_toward(3) := sign(3-Pi) * min(1, abs(3-Pi))."""
    delta = target - pi
    if delta == 0:
        return 0.0
    sign = 1.0 if delta > 0 else -1.0
    return sign * min(1.0, abs(delta))


@register_adapter("pr119_pressure_homeostat")
class PressureHomeostatAdapter(Adapter):
    contract_module = "settlement_layer"
    canon_row = None
    registry_subsystem = "settlement_territory"

    def resolve_params(self, resolver) -> tuple[dict, dict]:
        goldenfurt = build_goldenfurt_settlement()
        params = {
            "pi_start": goldenfurt.pressure,
            "seasons": 20,
            "p_unserved_need": 0.4,
            "unserved_need_pressure": 1.5,
            "p_grudge_active": 0.3,
            "grudge_pressure_each": 0.5,
            "ambitions_in_motion_max": len(NPCS),  # 6 real Goldenfurt NPCs, each with an ambition track
            "ambition_pressure_each": 0.5,
            "p_external_shock": 0.15,
            "external_shock_magnitude": 1.0,
            "p_player_release": 0.5,
            "player_release_magnitude": 1.0,
        }
        provenance = {
            "pi_start": "PROVISIONAL: goldenfurt_fixture.build_goldenfurt_settlement()."
                "pressure, read at call time -- README.md worked example 'Pi = 4'",
            "seasons": "test-scenario value, not canon-derived: chosen to give a multi-"
                "year-arc trajectory (a year-arc is 4 seasons per governance_play_redesign_"
                "v1.md §1.1) room to show drift, not a canon-cited horizon",
            "p_unserved_need": "test-scenario value, not canon-derived: §1.5 states Needs "
                "are deck-driven with no stated base emission rate",
            "unserved_need_pressure": "test-scenario value, not canon-derived: "
                "sim_build_spec.md §5 formula cites 'pressure_if_ignored' as a per-card "
                "field, not a fixed constant -- 1.5 is a representative magnitude",
            "p_grudge_active": "test-scenario value, not canon-derived",
            "grudge_pressure_each": "PROVISIONAL: sim_build_spec.md §5 -- '+0.5 per Grudge tag'",
            "ambitions_in_motion_max": "PROVISIONAL: goldenfurt_fixture.NPCS -- Goldenfurt's "
                "real 6 NPC dossiers, each carrying an ambition track per npc_cast.md",
            "ambition_pressure_each": "PROVISIONAL: sim_build_spec.md §5 -- '+0.5 per NPC "
                "with progress > 0 and not firing'",
            "p_external_shock": "test-scenario value, not canon-derived: sim_build_spec.md "
                "§5 cites 'province war / calamity bleed' with no base rate",
            "external_shock_magnitude": "test-scenario value, not canon-derived",
            "p_player_release": "test-scenario value, not canon-derived: the player's own "
                "response cadence is out of scope for this formula-only adapter",
            "player_release_magnitude": "test-scenario value, not canon-derived",
        }
        return params, provenance

    def decision_points(self) -> list[DecisionPoint]:
        return [
            DecisionPoint(
                name="pi_trajectory_band", default_tier=Tier.MAJOR,
                branches=["stable_dramatic_band", "collapsed_low", "runaway_high"],
                justification="a multi-season Pi trajectory feeds the deck's draw count and "
                               "family bias every season for the whole settlement -- a "
                               "campaign-defining, cross-scale aggregate per the tier-3 "
                               "rubric row, and the direct re-test of PR#125's #1 finding",
            ),
        ]

    def run_once(self, rng, params: dict, decision_point: DecisionPoint) -> Outcome:
        pi = params["pi_start"]
        trajectory = [pi]
        for _season in range(params["seasons"]):
            unserved = (params["unserved_need_pressure"]
                        if rng.random() < params["p_unserved_need"] else 0.0)
            n_grudges = sum(1 for _ in range(2) if rng.random() < params["p_grudge_active"])
            grudges = n_grudges * params["grudge_pressure_each"]
            n_ambitions = sum(1 for _ in range(params["ambitions_in_motion_max"])
                               if rng.random() < 0.5)
            ambitions = n_ambitions * params["ambition_pressure_each"]
            shock = (params["external_shock_magnitude"]
                     if rng.random() < params["p_external_shock"] else 0.0)
            release = (params["player_release_magnitude"]
                       if rng.random() < params["p_player_release"] else 0.0)
            pi = pi + unserved + grudges + ambitions + shock - release + _restore_toward(pi)
            pi = max(0.0, min(10.0, pi))
            trajectory.append(pi)

        if pi < 2.0:
            branch = "collapsed_low"
        elif pi > 6.0:
            branch = "runaway_high"
        else:
            branch = "stable_dramatic_band"
        return Outcome(decision_point.name, trajectory, {"branch": branch})
