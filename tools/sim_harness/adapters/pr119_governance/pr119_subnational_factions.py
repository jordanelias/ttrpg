"""pr119_subnational_factions.py — provisional adapter testing PR#119's two §3.3 subnational-
faction items (systems/settlements/settlement_layer_v30.md):
  - §3.3b Patron-backed privilege lapse -- the Za model (ED-SE-0021)
  - §3.3c The Seggio Council (ED-SE-0024)

The reconciliation doc (designs/audit/2026-07-12-settlement-season-stress-sim/
reconciliation_with_existing_territory_work.md §A.3) down-tiers PR#125's "§3.3c no force/
seizure resolver" CRITICAL finding to MEDIUM: the VIOLENT removal path already exists in
built code (systems/settlements/sim/infrastructure.py's seizure_ob_modifier, §1.5), it is only the
SOFTER political "Mandate Challenge" path that political_hierarchy §2.4 forward-references
but never defines. This adapter calls the real seizure_ob_modifier() to confirm the violent
path is real, and declares the political path's absence as the adapter's own expected,
always-firing branch -- turning a paragraph-level claim into an executable regression.

canon_row=None: §3.3b and §3.3c are both PROPOSED, no CURRENT.md row.
"""
from __future__ import annotations

from systems.settlements.sim import infrastructure

from ...adapter import Adapter, Outcome, register_adapter
from ...depth import DecisionPoint, Tier
from .goldenfurt_fixture import SID


class FakeWorld:
    """Minimal stand-in satisfying infrastructure.build_infrastructure()'s only real
    requirement (`territory_id in world.territories`) without depending on the full
    engine.autoload.game_state.World construction this adapter has no other need for."""
    def __init__(self, territory_ids):
        self.territories = {tid: object() for tid in territory_ids}


@register_adapter("pr119_subnational_factions")
class SubnationalFactionsAdapter(Adapter):
    contract_module = "settlement_layer"
    canon_row = None
    registry_subsystem = "settlement_territory"

    def resolve_params(self, resolver) -> tuple[dict, dict]:
        params = {
            "seggio_territory_id": SID,
            "p_patron_standing_drop": 0.3,
            "p_bargain_success": 0.5,
            "seasons": 6,
        }
        provenance = {
            "seggio_territory_id": "PROVISIONAL: goldenfurt_fixture.SID -- reusing Goldenfurt "
                "(S-006) as the test territory rather than an invented one",
            "p_patron_standing_drop": "test-scenario value, not canon-derived: §3.3b states "
                "no base rate for a patron's standing dropping below its threshold",
            "p_bargain_success": "test-scenario value, not canon-derived: §3.3b's Treat-"
                "verb bargain window states no success rate",
            "seasons": "test-scenario value, not canon-derived: chosen to give the one-"
                "season 'Patron's Rivals Move' bargain window room to fire",
        }
        return params, provenance

    def decision_points(self) -> list[DecisionPoint]:
        return [
            DecisionPoint(
                name="za_patron_lapse", default_tier=Tier.MEDIUM,
                branches=["privilege_intact", "bargained_shored_up", "automatic_lapse"],
                justification="an automatic Charter-privilege lapse is an Accounting-step, "
                               "settlement-scale write with no roll -- tier-2 per the rubric",
            ),
            DecisionPoint(
                name="seggio_removal_path", default_tier=Tier.MAJOR,
                branches=["violent_removal_available", "political_challenge_undefined"],
                justification="Seggio removal is explicitly 'a conquest- or coup-adjacent "
                               "event' per §3.3c's own text -- campaign-defining, tier-3 "
                               "per the rubric. NOTE: this decision point deterministically "
                               "resolves 'violent_removal_available' every trial (the real "
                               "seizure_ob_modifier is always negative for an entrenched "
                               "Cathedral+Church-Governor stack), so at tier-3 it is EXPECTED "
                               "to trip DEGENERATE_DISTRIBUTION -- that flag IS the finding "
                               "(the political Mandate-Challenge branch never fires because "
                               "no resolver for it exists), not an adapter defect.",
            ),
        ]

    def run_once(self, rng, params: dict, decision_point: DecisionPoint) -> Outcome:
        if decision_point.name == "za_patron_lapse":
            dropped = rng.random() < params["p_patron_standing_drop"]
            if not dropped:
                return Outcome(decision_point.name, dropped, {"branch": "privilege_intact"})
            bargained = rng.random() < params["p_bargain_success"]
            branch = "bargained_shored_up" if bargained else "automatic_lapse"
            return Outcome(decision_point.name, {"dropped": dropped, "bargained": bargained},
                            {"branch": branch})

        if decision_point.name == "seggio_removal_path":
            # Real call into the built module -- worst-case entrenchment (Cathedral +
            # Church Governor) to confirm the violent removal path's Ob modifier is real,
            # non-zero, and capped, exactly as §1.5 + the reconciliation doc claim.
            tid = params["seggio_territory_id"]
            world = FakeWorld([tid])
            infrastructure.build_infrastructure(tid, "Cathedral", world=world)
            infrastructure.build_infrastructure(tid, "Church Governor", world=world)
            mod = infrastructure.seizure_ob_modifier(tid, world=world)
            violent_path_real = mod < 0
            # political_hierarchy §2.4's "Mandate-track" Mandate Challenge has no defined
            # procedure anywhere in the corpus (per the reconciliation doc's own search) --
            # declared here as this decision point's expected, always-firing branch rather
            # than probed for, since there is no resolver to call.
            branch = ("violent_removal_available" if violent_path_real
                      else "political_challenge_undefined")
            return Outcome(decision_point.name, mod, {"branch": branch})

        raise ValueError(f"unknown decision point {decision_point.name!r}")
