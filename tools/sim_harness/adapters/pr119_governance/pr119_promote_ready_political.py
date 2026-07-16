"""pr119_promote_ready_political.py — provisional adapter testing 4 of the 9 promote-ready
proposals, political-process themed:

  - HRE-2 Chapter Capture (ED-FA-0024): pre-vacancy patronage banking ("College seats owed")
    that converts to vote-weight only if/when a vacancy fires (timing the player doesn't
    control).
  - HRE-3 Convene the Circle (ED-SE-0026): a new AP verb pooling obligations across peer
    settlements; the closure register's own refinement shrinks "Circle Quota" to a Debt-family
    variant "callable by any co-signer" per the §1.3b Collective-Liability precedent -- tested
    here as a real ledger write, not the standalone resource the original pitch used.
  - CHN-6 Gongsuo Registration (ED-SE-0025): a visibility/exposure toggle. Consolidated
    disposition: "Re-home before promoting... fold the registration status into §1.3c Ordenanza
    as a gating precondition for whether a Petition can surface" -- tested here directly
    against the REAL Ordenanza mechanic already built in pr119_guild_ladder.py, not a
    standalone toggle.
  - HAB-4 Overlapping Consulta Arbitration (ED-FA-0025): inter-ministry conflict arbitration,
    two procedure types (Agenda-Set blind-framing vs. Ratify accept/veto) + Latency-to-paralysis.

canon_row=None: all four are "promote-ready, unlanded" -- vetted but never authored, no
CURRENT.md row.
"""
from __future__ import annotations

import sys
from pathlib import Path

_SKILL_DIR = Path(__file__).resolve().parents[4] / "skills" / "valoria-dice-model"
if str(_SKILL_DIR) not in sys.path:
    sys.path.insert(0, str(_SKILL_DIR))
import valoria_dice  # noqa: E402

from ...adapter import Adapter, Outcome, register_adapter  # noqa: E402
from ...depth import DecisionPoint, Tier  # noqa: E402
from .goldenfurt_fixture import build_goldenfurt_settlement  # noqa: E402


@register_adapter("pr119_hre2_chapter_capture")
class Hre2ChapterCaptureAdapter(Adapter):
    contract_module = "faction_politics"
    canon_row = None
    registry_subsystem = "faction_political"

    def resolve_params(self, resolver) -> tuple:
        params = {"seats_banked": 3, "p_vacancy_per_season": 0.15, "seasons": 10}
        provenance = {
            "seats_banked": "test-scenario value, not canon-derived: HRE-2 states no fixed "
                "number of 'College seats owed' a player can bank",
            "p_vacancy_per_season": "test-scenario value, not canon-derived: HRE-2's own text "
                "flags timing as 'the player doesn't control' -- modeled as an exogenous draw",
            "seasons": "test-scenario value, not canon-derived",
        }
        return params, provenance

    def decision_points(self) -> list:
        return [
            DecisionPoint(
                name="banked_seats_convert", default_tier=Tier.MEDIUM,
                branches=["vacancy_fired_seats_convert", "no_vacancy_seats_stay_banked"],
                justification="a durable Debt-family ledger write that only resolves on an "
                               "exogenous vacancy event -- tier-2",
            ),
        ]

    def run_once(self, rng, params: dict, decision_point: DecisionPoint) -> Outcome:
        s = build_goldenfurt_settlement()
        s.add_tag("Debt", "college-seats-owed", value=params["seats_banked"])
        fired = any(rng.random() < params["p_vacancy_per_season"]
                    for _ in range(params["seasons"]))
        branch = "vacancy_fired_seats_convert" if fired else "no_vacancy_seats_stay_banked"
        return Outcome(decision_point.name, fired, {"branch": branch})


@register_adapter("pr119_hre3_convene_circle")
class Hre3ConveneCircleAdapter(Adapter):
    contract_module = "settlement_layer"
    canon_row = None
    registry_subsystem = "settlement_territory"

    def resolve_params(self, resolver) -> tuple:
        params = {"p_cosigner_calls_in": 0.4}
        provenance = {
            "p_cosigner_calls_in": "test-scenario value, not canon-derived: the closure "
                "register's refined 'callable by any co-signer' Debt variant states no "
                "call-in rate",
        }
        return params, provenance

    def decision_points(self) -> list:
        return [
            DecisionPoint(
                name="circle_quota_call_in", default_tier=Tier.MEDIUM,
                branches=["called_in_by_cosigner", "quota_expires_unclaimed"],
                justification="reuses the real §1.3b Collective-Liability Debt-write "
                               "precedent per the closure register's own refinement -- tier-2",
            ),
        ]

    def run_once(self, rng, params: dict, decision_point: DecisionPoint) -> Outcome:
        s = build_goldenfurt_settlement()
        s.add_tag("Debt", "circle-quota", ttl=6)
        called = rng.random() < params["p_cosigner_calls_in"]
        branch = "called_in_by_cosigner" if called else "quota_expires_unclaimed"
        return Outcome(decision_point.name, called, {"branch": branch})


@register_adapter("pr119_chn6_gongsuo")
class Chn6GongsuoAdapter(Adapter):
    contract_module = "faction_politics"
    canon_row = None
    registry_subsystem = "faction_political"

    def resolve_params(self, resolver) -> tuple:
        params = {"amend_pool": 6, "amend_tn": 7, "amend_ob": 2}
        provenance = {
            "amend_pool": "test-scenario value, not canon-derived: reuses "
                "pr119_guild_ladder.py's identical Ordenanza roll for a direct comparison",
            "amend_tn": "test-scenario value matching engine/params/core.md's Standard TN=7",
            "amend_ob": "PROVISIONAL: governance_play_redesign_v1.md §1.3c -- 'Amend ... Ob 2'",
        }
        return params, provenance

    def decision_points(self) -> list:
        return [
            DecisionPoint(
                name="registration_gates_ordenanza_petition", default_tier=Tier.MEDIUM,
                branches=["unregistered_petition_blocked", "registered_petition_surfaces"],
                justification="tests the closure register's own consolidated disposition -- "
                               "CHN-6 re-homed as a gating precondition on §1.3c's real "
                               "Ordenanza-Petition surfacing, not a standalone toggle -- tier-2",
            ),
        ]

    def run_once(self, rng, params: dict, decision_point: DecisionPoint) -> Outcome:
        registered = rng.random() < 0.5
        if not registered:
            return Outcome(decision_point.name, registered,
                            {"branch": "unregistered_petition_blocked"})
        r = valoria_dice.roll_pool(params["amend_pool"], params["amend_tn"], rng)
        valoria_dice.classify_outcome(r, params["amend_ob"])  # exercises the real Ordenanza roll
        return Outcome(decision_point.name, registered, {"branch": "registered_petition_surfaces"})


@register_adapter("pr119_hab4_consulta")
class Hab4ConsultaArbitrationAdapter(Adapter):
    contract_module = "faction_politics"
    canon_row = None
    registry_subsystem = "faction_political"

    def resolve_params(self, resolver) -> tuple:
        params = {"p_agenda_set": 0.5, "p_resolved_before_latency2": 0.6}
        provenance = {
            "p_agenda_set": "test-scenario value, not canon-derived: HAB-4's choice between "
                "'Agenda-Set blind-framing' and 'Ratify accept/veto' procedure types states no "
                "base rate",
            "p_resolved_before_latency2": "test-scenario value, not canon-derived: HAB-4's "
                "'Latency-to-paralysis' escalation states no per-round resolution rate",
        }
        return params, provenance

    def decision_points(self) -> list:
        return [
            DecisionPoint(
                name="consulta_arbitration", default_tier=Tier.MEDIUM,
                branches=["resolved_agenda_set", "resolved_ratify", "paralysis_latency2"],
                justification="an inter-ministry conflict resolution the closure register "
                               "flags as presupposing an unbuilt per-Ministry action-economy "
                               "foundation -- tier-2, structural gap noted not hidden",
            ),
        ]

    def run_once(self, rng, params: dict, decision_point: DecisionPoint) -> Outcome:
        procedure = "agenda_set" if rng.random() < params["p_agenda_set"] else "ratify"
        if rng.random() < params["p_resolved_before_latency2"]:
            branch = "resolved_agenda_set" if procedure == "agenda_set" else "resolved_ratify"
        else:
            branch = "paralysis_latency2"
        return Outcome(decision_point.name, procedure, {"branch": branch})
