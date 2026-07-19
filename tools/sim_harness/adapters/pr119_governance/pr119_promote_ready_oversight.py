"""pr119_promote_ready_oversight.py — provisional adapter testing 2 of the 9 promote-ready
proposals, explicitly meant to be authored TOGETHER per the closure register ("Author as part
of the S-2 five-instrument oversight toolkit" / "Author as part of S-2 with HAB-1"):

  - HAB-1 Corregidor (ED-SE-0030): an outside appointee LAYERED OVER the sitting governor
    (override on Hold Court/Investigate only, governor keeps the rest); self-expiring
    term-scoped tags. "The first mechanic to actually mechanize §1.4's suspicion-threshold
    'audit' stub."
  - IT-1 Podestà (ED-SE-0029): an outsider governor who REPLACES the sitting one, immune to
    internal faction rolls, with appointer-liability: end-of-term Sindacato malfeasance bills
    the appointing faction's Legitimacy, not the settlement's.

Tested together because their distinguishing feature IS mechanical: HAB-1 is a concurrent
OVERLAY (both governor and Corregidor hold office simultaneously); IT-1 is a full REPLACEMENT
(reuses the real registry.succeed_governor() call already exercised in
pr119_integrated_campaign.py/pr119_event_deck_engine.py). Modeling both against the same
Goldenfurt scenario makes that distinction a measured, not merely asserted, difference.

canon_row=None: both are "promote-ready, unlanded" -- vetted but never authored into any
canon doc, no CURRENT.md row. contract_module="settlement_layer".
"""
from __future__ import annotations

from systems.settlements.sim import registry

from ...adapter import Adapter, Outcome, register_adapter
from ...depth import DecisionPoint, Tier
from .goldenfurt_fixture import build_goldenfurt_settlement


@register_adapter("pr119_oversight_instruments")
class OversightInstrumentsAdapter(Adapter):
    contract_module = "settlement_layer"
    canon_row = None
    registry_subsystem = "settlement_territory"

    def resolve_params(self, resolver) -> tuple:
        params = {
            "corregidor_term_seasons": 4,
            "p_corregidor_override_fires": 0.3,
            "p_podesta_malfeasance": 0.25,
        }
        provenance = {
            "corregidor_term_seasons": "test-scenario value, not canon-derived: HAB-1 states "
                "'self-expiring term-scoped tags', no stated term length",
            "p_corregidor_override_fires": "test-scenario value, not canon-derived: rate at "
                "which the Corregidor's Hold-Court/Investigate override is actually invoked "
                "during its term",
            "p_podesta_malfeasance": "test-scenario value, not canon-derived: IT-1's end-of-"
                "term Sindacato malfeasance-bill rate is not stated",
        }
        return params, provenance

    def decision_points(self) -> list:
        return [
            DecisionPoint(
                name="corregidor_overlay", default_tier=Tier.MEDIUM,
                branches=["term_expired_no_override", "override_invoked_then_expired"],
                justification="a term-scoped ledger tag write that overlays, not replaces, "
                               "governance -- settlement-scale, tier-2",
            ),
            DecisionPoint(
                name="podesta_replacement", default_tier=Tier.MAJOR,
                branches=["term_clean", "appointer_liable_malfeasance"],
                justification="a real registry.succeed_governor() replacement call plus a "
                               "cross-faction Legitimacy liability -- campaign-defining, tier-3",
            ),
        ]

    def run_once(self, rng, params: dict, decision_point: DecisionPoint) -> Outcome:
        s = build_goldenfurt_settlement()
        if decision_point.name == "corregidor_overlay":
            s.add_tag("Precedent", "corregidor-overlay-active",
                      ttl=params["corregidor_term_seasons"])
            branch = ("override_invoked_then_expired"
                       if rng.random() < params["p_corregidor_override_fires"]
                       else "term_expired_no_override")
            return Outcome(decision_point.name, branch, {"branch": branch})

        if decision_point.name == "podesta_replacement":
            registry.register_settlement(s)
            # Real replacement call, not a modeled overlay -- the mechanical distinction from
            # HAB-1's Corregidor this adapter exists to demonstrate.
            registry.succeed_governor(s.sid, "podesta-appointee", world=None, season=0)
            malfeasant = rng.random() < params["p_podesta_malfeasance"]
            if malfeasant:
                s.add_tag("Grudge", "appointing-faction-legitimacy")
            branch = "appointer_liable_malfeasance" if malfeasant else "term_clean"
            return Outcome(
                decision_point.name,
                {"governor_after_replacement": s.governor_id}, {"branch": branch},
            )

        raise ValueError(f"unknown decision point {decision_point.name!r}")
