"""pr119_clerk_capacity.py — provisional adapter testing PR#119's §1.1a Clerk Capacity
(ED-SE-0022, designs/territory/governance_play_redesign_v1.md), the one item of the 12
authored PR#119 mechanics that pr119_structural_gaps.py's earlier verification pass flagged
as a real scope gap ("no dedicated decision point this wave") rather than silently leaving
untested.

    "New verb Retain Clerks (1 AP + W-1/season, auto-succeeds, no roll): grants +1 effective
    AP per point of Clerk Capacity (CC, 0-3 per settlement), uncapped by FacilityTier. Each CC
    point also silently increments a hidden Clerk Corruption counter, raising the draw-weight
    of a new Intrigue-family trigger ... The counter is discoverable only via Investigate,
    never surfaced up front the way every other AP source is."

Tested here in isolation (single-mechanic, matching the other 6 per-item adapters' scope);
its genuinely interesting CROSS-mechanic behavior — Clerk Corruption sits on the exact same
Orsk/Konrad bribery web npc_cast.md already authors (Konrad "takes Orsk's coin for advance
levy notice"), so a Clerk-Corruption Investigate can plausibly surface Konrad's own
corruption too — is tested compositionally in pr119_integrated_campaign.py, not here.

canon_row=None: §1.1a is PROPOSED, no CURRENT.md row.
"""
from __future__ import annotations

from ...adapter import Adapter, Outcome, register_adapter
from ...depth import DecisionPoint, Tier

_CC_CAP = 3  # §1.1a: "Clerk Capacity (CC, 0-3 per settlement)"


@register_adapter("pr119_clerk_capacity")
class ClerkCapacityAdapter(Adapter):
    contract_module = "settlement_layer"
    canon_row = None
    registry_subsystem = "settlement_territory"

    def resolve_params(self, resolver) -> tuple[dict, dict]:
        params = {
            "cc_cap": _CC_CAP,
            "seasons": 6,
            "p_retain_each_season": 0.5,
            "corruption_discovery_k": 0.12,
        }
        provenance = {
            "cc_cap": "PROVISIONAL: designs/territory/governance_play_redesign_v1.md §1.1a "
                "— 'Clerk Capacity (CC, 0-3 per settlement)'",
            "seasons": "test-scenario value, not canon-derived: chosen to let CC accumulate "
                "toward its cap within one trial",
            "p_retain_each_season": "test-scenario value, not canon-derived: §1.1a states no "
                "base rate for choosing to Retain Clerks each season",
            "corruption_discovery_k": "test-scenario value, not canon-derived: §1.1a states "
                "the corruption counter 'raises the draw-weight of a new Intrigue-family "
                "trigger' but no numeric weight — modeled as a per-CC-point linear discovery "
                "probability (discovery_p = corruption_discovery_k * clerk_corruption, "
                "capped at 1.0), a documented simplification of an unspecified curve",
        }
        return params, provenance

    def decision_points(self) -> list[DecisionPoint]:
        return [
            DecisionPoint(
                name="clerk_ap_gain", default_tier=Tier.MEDIUM,
                branches=["capacity_grows", "capped", "dismissed"],
                justification="a real, uncapped-by-FacilityTier AP-source write consumed "
                               "every subsequent season — a settlement-scale write, tier-2 "
                               "per the rubric",
            ),
            DecisionPoint(
                name="clerk_corruption_discovery", default_tier=Tier.MEDIUM,
                branches=["undiscovered", "discovered_via_investigate"],
                justification="§1.1a: discovery seeds a new Intrigue-family card and (per "
                               "the doc) is the only AP source with a hidden liability — a "
                               "settlement-scale, cross-card-family write, tier-2",
            ),
        ]

    def run_once(self, rng, params: dict, decision_point: DecisionPoint) -> Outcome:
        if decision_point.name == "clerk_ap_gain":
            if rng.random() >= params["p_retain_each_season"]:
                return Outcome(decision_point.name, 0, {"branch": "dismissed"})
            # Simulate one season's worth of accumulation from a fresh CC=0 start.
            cc = 0
            for _season in range(params["seasons"]):
                if rng.random() < params["p_retain_each_season"] and cc < params["cc_cap"]:
                    cc += 1
            branch = "capped" if cc >= params["cc_cap"] else "capacity_grows"
            return Outcome(decision_point.name, cc, {"branch": branch})

        if decision_point.name == "clerk_corruption_discovery":
            cc = 0
            corruption = 0
            discovered = False
            for _season in range(params["seasons"]):
                if rng.random() < params["p_retain_each_season"] and cc < params["cc_cap"]:
                    cc += 1
                corruption += cc  # "each CC point also silently increments" -- per season held
                p_discover = min(1.0, params["corruption_discovery_k"] * corruption)
                if rng.random() < p_discover:
                    discovered = True
                    break
            branch = "discovered_via_investigate" if discovered else "undiscovered"
            return Outcome(decision_point.name, corruption, {"branch": branch})

        raise ValueError(f"unknown decision point {decision_point.name!r}")
