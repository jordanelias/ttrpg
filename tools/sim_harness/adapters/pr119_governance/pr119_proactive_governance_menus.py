"""pr119_proactive_governance_menus.py — provisional adapter testing "proactive governance":
designs/audit/2026-07-12-governance-compendium/41_proactive_scale_menus.md, Proactive Player-
Action Menus across four scales (Organization, Settlement, Territory, Faction) -- PROPOSED
research, "numbers are deliberately absent by design" per the doc itself (structure/identity
only, no simulatable constants), so this adapter is deliberately structural/deterministic
(tier-1, same style as pr119_structural_gaps.py) rather than a Monte Carlo -- there is nothing
numeric here yet to sample.

What it checks, against real code:
  - Settlement is the ONLY one of the four scales with built machinery
    (systems/settlements/sim/registry.py's Settlement dataclass); Organization and Territory have no
    registry/entity of their own anywhere in sim/ -- confirmed by source-text absence, not
    asserted from the doc's own claim.
  - The doc's one genuinely-concrete new lever (Relay Tier / Beacon Network, "the single
    strongest new-state case in the corpus") is explicitly contingent on an unauthored
    temporal model -- confirmed against references/module_contracts.yaml: `engine_clock` has
    `doc: null` (CLAUDE.md §6's own "10/27 modules have doc: null... including engine_clock,
    the temporal spine").

canon_row=None: 41_proactive_scale_menus.md is PROPOSED research, no CURRENT.md row.
contract_module=None: deliberately -- this adapter's whole point is that Organization/Territory
have no module_contracts.yaml row to bind to (that absence IS the finding), and engine_clock's
row exists but is doc:null; no single row correctly represents "checking for an absence".
"""
from __future__ import annotations

from pathlib import Path

from ...adapter import Adapter, Outcome, register_adapter
from ...depth import DecisionPoint, Tier

_REPO_ROOT = Path(__file__).resolve().parents[4]
_REGISTRY_PY = _REPO_ROOT / "systems" / "settlements" / "sim" / "registry.py"
_MODULE_CONTRACTS = _REPO_ROOT / "references" / "module_contracts.yaml"


@register_adapter("pr119_proactive_governance_menus")
class ProactiveGovernanceMenusAdapter(Adapter):
    contract_module = None
    canon_row = None
    registry_subsystem = "cross_cutting"

    def resolve_params(self, resolver) -> tuple:
        params = {
            "registry_py_path": str(_REGISTRY_PY.relative_to(_REPO_ROOT)),
            "module_contracts_path": str(_MODULE_CONTRACTS.relative_to(_REPO_ROOT)),
        }
        provenance = {k: "test-scenario value, not a canon citation: a literal repo path "
                      "this adapter inspects at run time" for k in params}
        return params, provenance

    def decision_points(self) -> list:
        return [
            DecisionPoint(
                name="scale_entity_check", default_tier=Tier.MINOR,
                branches=["only_settlement_built", "multiple_scales_built", "none_built"],
                justification="a single deterministic source-text check across the four "
                               "scales -- tier-1 per the rubric",
            ),
            DecisionPoint(
                name="relay_tier_temporal_dependency", default_tier=Tier.MINOR,
                branches=["contingent_on_unauthored_engine_clock", "engine_clock_authored"],
                justification="a single deterministic module_contracts.yaml lookup -- tier-1",
            ),
        ]

    def run_once(self, rng, params: dict, decision_point: DecisionPoint) -> Outcome:
        if decision_point.name == "scale_entity_check":
            text = _REGISTRY_PY.read_text(encoding="utf-8")
            built = []
            if "class Settlement" in text:
                built.append("Settlement")
            if "class Organization" in text:
                built.append("Organization")
            if "class Territory" in text:
                built.append("Territory")
            if len(built) == 0:
                branch = "none_built"
            elif built == ["Settlement"]:
                branch = "only_settlement_built"
            else:
                branch = "multiple_scales_built"
            return Outcome(decision_point.name, built, {"branch": branch})

        if decision_point.name == "relay_tier_temporal_dependency":
            import yaml
            data = yaml.safe_load(_MODULE_CONTRACTS.read_text(encoding="utf-8"))
            entries = {m.get("module"): m for m in data.get("modules", []) if m.get("module")}
            engine_clock = entries.get("engine_clock")
            authored = bool(engine_clock and engine_clock.get("doc"))
            branch = ("engine_clock_authored" if authored
                       else "contingent_on_unauthored_engine_clock")
            return Outcome(
                decision_point.name,
                {"engine_clock_entry_present": engine_clock is not None,
                 "engine_clock_doc": engine_clock.get("doc") if engine_clock else None},
                {"branch": branch},
            )

        raise ValueError(f"unknown decision point {decision_point.name!r}")
