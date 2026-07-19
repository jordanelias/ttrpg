"""pr119_ledger_family_collision.py — provisional adapter testing PR#119's §1.3a Locked
Extraction Figures (ED-SE-0018/ED-SE-0019), specifically the `Compact` Ledger-of-Consequence
family governance_play_redesign_v1.md §1.6 introduces:

    "Compact (NEW — ED-SE-0019, 2026-07-09; §1.3a) — a fifth family: a negotiated,
    fixed-term extraction agreement (Encabezamiento) ..."

The reconciliation doc (designs/audit/2026-07-12-settlement-season-stress-sim/
reconciliation_with_existing_territory_work.md §C.1, flagged "★ the single most actionable
new find") observes the BUILT systems/settlements/sim/ledger.py already has five tag kinds —
{Precedent, Grudge, Debt, Reputation, Leverage} — so `Compact` is not actually the built
system's fifth family; it is either a sixth family, a collision with Leverage, or should
reuse an existing kind. That claim was made by reading ledger.py's docstring; this adapter
calls the REAL ledger.py directly so the check can never silently drift from the live code.

canon_row=None: §1.3a/§1.6's Compact family is PROPOSED, no CURRENT.md row.
"""
from __future__ import annotations

from systems.settlements.sim import ledger

from ...adapter import Adapter, Outcome, register_adapter
from ...depth import DecisionPoint, Tier
from .goldenfurt_fixture import build_goldenfurt_settlement


@register_adapter("pr119_ledger_family_collision")
class LedgerFamilyCollisionAdapter(Adapter):
    contract_module = "settlement_layer"  # references/module_contracts.yaml -> systems/settlements/settlement_layer_v30.md
    canon_row = None
    registry_subsystem = "settlement_territory"

    def resolve_params(self, resolver) -> tuple[dict, dict]:
        params = {
            "proposed_family": "Compact",
            # Read live, not hardcoded — see run_once: this is what the check actually
            # compares against on every call, so it can never go stale relative to the
            # docstring claim above.
            "built_family_count": len(ledger.TAG_KINDS),
        }
        provenance = {
            "proposed_family": "PROVISIONAL: systems/settlements/governance_play_redesign_v1.md "
                "§1.6 — 'Compact (NEW -- ED-SE-0019, 2026-07-09; §1.3a) -- a fifth family'",
            "built_family_count": "live systems/settlements/sim/ledger.py TAG_KINDS, read at call time "
                "(not a canon citation — this is the built code's own current state, the "
                "thing the proposal is being checked against)",
        }
        return params, provenance

    def decision_points(self) -> list[DecisionPoint]:
        return [
            DecisionPoint(
                name="compact_fifth_family_claim", default_tier=Tier.MINOR,
                branches=["collision_confirmed", "no_collision"],
                justification="a single, deterministic structural check against live code "
                               "— locally reversible (re-running it costs nothing) — tier-1 "
                               "per the rubric's 'single check' row",
            ),
            DecisionPoint(
                name="compact_tag_silently_coexists", default_tier=Tier.MEDIUM,
                branches=["silently_added_unrecognized", "rejected"],
                justification="ledger_add() is a real settlement-scale write path consumed "
                               "cross-scale (every governance verb routes through it) — "
                               "tier-2 per the rubric",
            ),
        ]

    def run_once(self, rng, params: dict, decision_point: DecisionPoint) -> Outcome:
        if decision_point.name == "compact_fifth_family_claim":
            # §1.6 calls Compact "a fifth family". The built set already has 5 members and
            # does not include Compact -- so adding Compact would make a SIXTH kind, not
            # complete a fifth. Check both halves of the claim against live code.
            already_five = params["built_family_count"] == 5
            compact_absent = params["proposed_family"] not in ledger.TAG_KINDS
            collision = already_five and compact_absent
            branch = "collision_confirmed" if collision else "no_collision"
            return Outcome(
                decision_point.name,
                {"live_tag_kinds": sorted(ledger.TAG_KINDS), "already_five": already_five,
                 "compact_absent": compact_absent},
                {"branch": branch},
            )

        if decision_point.name == "compact_tag_silently_coexists":
            # Exercise the real write path: does ledger_add() reject an unrecognized kind,
            # or does it silently accept it as a de-facto 6th family? (registry.Settlement
            # .add_tag() -> ledger.ledger_add(), the same path every governance verb uses.)
            s = build_goldenfurt_settlement()
            s.add_tag(params["proposed_family"], "encabezamiento-test", created_season=0, ttl=6)
            present = ledger.ledger_has(s.ledger, params["proposed_family"], "encabezamiento-test")
            branch = "silently_added_unrecognized" if present else "rejected"
            return Outcome(decision_point.name, present, {"branch": branch})

        raise ValueError(f"unknown decision point {decision_point.name!r}")
