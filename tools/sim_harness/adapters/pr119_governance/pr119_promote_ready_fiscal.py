"""pr119_promote_ready_fiscal.py — provisional adapter testing 3 of the 9 "promote-ready,
unlanded" comparative-governance proposals (designs/audit/2026-07-12-governance-compendium/
tier3_proposal_status_closure.md §3.2b) -- vetted buildable-without-a-Jordan-ruling, but never
authored into any canon doc and never stress-tested (none are in PR#119). Fiscal/resource-
extraction themed:

  - HRE-4 Borrow (ED-FA-0029): a loan secured against a named extractive right; spawns an
    Investigate-discoverable financier-actor; the hard clawback reuses Quo Warranto (a
    Concession-family tag).
  - VEN-SE-2 Boschi Pubblici Requisition (ED-SE-0028): a Directive type tying a province to a
    named production dependency; Defy starves the dependent building. The closure register
    flags a REAL unresolved ambiguity: "state explicitly whether Requisition is a species of
    Extract (inheriting §1.3a Compact auto-resolution) or immune to it" -- this adapter tests
    BOTH readings against the real Compact-collision bug (pr119_ledger_family_collision.py)
    and shows they diverge, sharpening a closure-register question mark into a measured fact.
  - IT-2 Condotta (ED-FA-0026): a Ferma->Aspetto->Lapsed three-state mercenary contract machine.

canon_row=None: all three are "promote-ready, unlanded" -- vetted but never authored, no
CURRENT.md row. contract_module="faction_politics" (HRE-4, IT-2 are FA-lane EDs) /
"settlement_layer" (VEN-SE-2 is SE-lane) -- see per-class binding below.
"""
from __future__ import annotations

from systems.settlements.sim import ledger

from ...adapter import Adapter, Outcome, register_adapter
from ...depth import DecisionPoint, Tier
from .goldenfurt_fixture import build_goldenfurt_settlement


@register_adapter("pr119_hre4_borrow")
class Hre4BorrowAdapter(Adapter):
    contract_module = "faction_politics"
    canon_row = None
    registry_subsystem = "faction_political"

    def resolve_params(self, resolver) -> tuple:
        params = {"p_financier_discovered": 0.5, "p_clawback_wins": 0.4}
        provenance = {
            "p_financier_discovered": "test-scenario value, not canon-derived: "
                "tier3_proposal_status_closure.md §3.2b HRE-4 -- 'spawns an Investigate-"
                "discoverable financier-actor', no stated discovery rate",
            "p_clawback_wins": "test-scenario value, not canon-derived: HRE-4 'reuses Quo "
                "Warranto for the hard clawback' -- no stated contest odds",
        }
        return params, provenance

    def decision_points(self) -> list:
        return [
            DecisionPoint(
                name="borrow_clawback", default_tier=Tier.MEDIUM,
                branches=["loan_serviced", "financier_discovered_clawback_wins",
                          "financier_discovered_clawback_fails", "financier_undiscovered"],
                justification="a real Debt/Concession ledger write with a Quo-Warranto-scale "
                               "contest gating a settlement's extractive right -- tier-2",
            ),
        ]

    def run_once(self, rng, params: dict, decision_point: DecisionPoint) -> Outcome:
        s = build_goldenfurt_settlement()
        s.add_tag("Debt", "hre4-financier-loan", ttl=8)
        if rng.random() >= params["p_financier_discovered"]:
            return Outcome(decision_point.name, "undiscovered", {"branch": "financier_undiscovered"})
        s.add_tag("Grudge", "financier-exposed")
        if rng.random() < params["p_clawback_wins"]:
            branch = "financier_discovered_clawback_wins"
        else:
            branch = "financier_discovered_clawback_fails"
        return Outcome(decision_point.name, branch, {"branch": branch})


@register_adapter("pr119_venSE2_requisition")
class VenSe2RequisitionAdapter(Adapter):
    contract_module = "settlement_layer"
    canon_row = None
    registry_subsystem = "settlement_territory"

    def resolve_params(self, resolver) -> tuple:
        params = {"p_defy": 0.4}
        provenance = {
            "p_defy": "test-scenario value, not canon-derived: VEN-SE-2's Defy/Bargain "
                "response rates are not stated",
        }
        return params, provenance

    def decision_points(self) -> list:
        return [
            DecisionPoint(
                name="requisition_as_extract_species", default_tier=Tier.MEDIUM,
                branches=["compact_auto_resolves", "compact_collision", "defy_starves_building"],
                justification="tests the closure register's own open question -- whether "
                               "Requisition inherits §1.3a Compact auto-resolution -- against "
                               "the real ledger.TAG_KINDS collision, a settlement-scale ledger "
                               "write, tier-2",
            ),
            DecisionPoint(
                name="requisition_as_immune_directive", default_tier=Tier.MEDIUM,
                branches=["complied", "defy_starves_building"],
                justification="the alternate reading (Requisition immune to Compact) -- same "
                               "tier as the Extract-species reading for direct comparison",
            ),
        ]

    def run_once(self, rng, params: dict, decision_point: DecisionPoint) -> Outcome:
        s = build_goldenfurt_settlement()
        if decision_point.name == "requisition_as_extract_species":
            # Reading A: Requisition IS a species of Extract -> inherits §1.3a's Compact
            # auto-resolution path, which the ledger_family_collision adapter already
            # confirmed silently accepts an unrecognized 6th kind.
            if rng.random() < params["p_defy"]:
                return Outcome(decision_point.name, "defy", {"branch": "defy_starves_building"})
            s.add_tag("Compact", "boschi-pubblici-requisition")
            collides = "Compact" not in ledger.TAG_KINDS
            branch = "compact_collision" if collides else "compact_auto_resolves"
            return Outcome(decision_point.name, {"collides": collides}, {"branch": branch})

        if decision_point.name == "requisition_as_immune_directive":
            # Reading B: Requisition is immune to Compact -- no ledger collision is even
            # reachable via this path, a materially different mechanical shape than Reading A.
            branch = "defy_starves_building" if rng.random() < params["p_defy"] else "complied"
            return Outcome(decision_point.name, branch, {"branch": branch})

        raise ValueError(f"unknown decision point {decision_point.name!r}")


@register_adapter("pr119_it2_condotta")
class It2CondottaAdapter(Adapter):
    contract_module = "faction_politics"
    canon_row = None
    registry_subsystem = "faction_political"

    def resolve_params(self, resolver) -> tuple:
        params = {"p_ferma_to_aspetto": 0.3, "p_aspetto_to_lapsed": 0.4, "seasons": 8}
        provenance = {
            "p_ferma_to_aspetto": "test-scenario value, not canon-derived: IT-2's "
                "Ferma->Aspetto->Lapsed transition rates are not stated numerically",
            "p_aspetto_to_lapsed": "test-scenario value, not canon-derived",
            "seasons": "test-scenario value, not canon-derived: horizon for the 3-state "
                "contract machine to play out",
        }
        return params, provenance

    def decision_points(self) -> list:
        return [
            DecisionPoint(
                name="condotta_state_machine", default_tier=Tier.MEDIUM,
                branches=["ferma", "aspetto", "lapsed"],
                justification="a multi-season contract state machine gating a faction's "
                               "military-pool availability (per the closure register's own "
                               "note that it must reconcile against 4 real faction.Mil read "
                               "sites) -- tier-2, not yet campaign-composed with the other "
                               "adapters in this cluster",
            ),
        ]

    def run_once(self, rng, params: dict, decision_point: DecisionPoint) -> Outcome:
        state = "ferma"
        for _season in range(params["seasons"]):
            if state == "ferma" and rng.random() < params["p_ferma_to_aspetto"]:
                state = "aspetto"
            elif state == "aspetto" and rng.random() < params["p_aspetto_to_lapsed"]:
                state = "lapsed"
                break
        return Outcome(decision_point.name, state, {"branch": state})
