"""pr119_guild_ladder.py — provisional adapter testing PR#119's Guild-ladder items:
  - designs/provincial/faction_politics_v30.md §2.5a Entry and Mastership Forks
    (ED-FA-0022/ED-FA-0023): guarantor-gated entry vs. sole-patron entry; capital-gated
    Free Mastership vs. the existing Masterpiece Examination.
  - designs/territory/governance_play_redesign_v1.md §1.3c Ordenanza Ratification
    (ED-SE-0023), which requires a Gu-Std 3+ Guild Master — cross-references §2.5.

Grounded on Orsk Tallow (NPC-G02), Goldenfurt's real Grainmaster/Guild factor
(goldenfurt_fixture.py) — the entry/mastership forks are tested against a generic
applicant under Orsk's Forum; the Ordenanza roll is tested as Orsk's own §1.3c action.

canon_row=None: §2.5a and §1.3c are both PROPOSED, no CURRENT.md row.
"""
from __future__ import annotations

import sys
from pathlib import Path

_SKILL_DIR = Path(__file__).resolve().parents[4] / "skills" / "valoria-dice-model"
if str(_SKILL_DIR) not in sys.path:
    sys.path.insert(0, str(_SKILL_DIR))
import valoria_dice  # noqa: E402

from ...adapter import Adapter, Outcome, register_adapter
from ...depth import DecisionPoint, Tier
from .goldenfurt_fixture import NPCS

_ORSK = NPCS["NPC-G02"]


@register_adapter("pr119_guild_ladder")
class GuildLadderAdapter(Adapter):
    contract_module = "faction_politics"
    canon_row = None
    registry_subsystem = "faction_political"

    def resolve_params(self, resolver) -> tuple[dict, dict]:
        std_tn = resolver.verify_citation(
            "Dice / resolution", "engine/params/core.md", "| Standard | 7 | Default |",
        )
        params = {
            "orsk_guild_standing": _ORSK["guild_standing"],
            "p_choose_guarantor_path": 0.5,
            "p_entry_violation": 0.3,
            "n_guarantors": 4,
            "p_choose_capital_buyin": 0.4,
            "p_masterpiece_pass": 0.6,
            "p_caste_reject_on_fail": 0.5,
            "amend_pool": 6,
            "amend_tn": 7,
            "amend_ob": 2,
        }
        provenance = {
            "orsk_guild_standing": "PROVISIONAL: see goldenfurt_fixture.NPCS['NPC-G02'] — "
                "test-scenario transcription (Gu-Std not stated numerically in npc_cast.md), "
                "used only to confirm Orsk meets §1.3c's Gu-Std 3+ Ordenanza-authoring gate",
            "p_choose_guarantor_path": "test-scenario value, not canon-derived: §2.5a BYZ-3 "
                "describes the applicant choosing one of two entry paths, no base rate given",
            "p_entry_violation": "test-scenario value, not canon-derived: no base violation "
                "rate stated for the Gu-Std 0/1 Demotion Triggers §2.5a's entry fork reacts to",
            "n_guarantors": "PROVISIONAL: designs/provincial/faction_politics_v30.md §2.5a "
                "BYZ-3 — 'Recruit 3-5 existing Guild members ... as guarantors' (midpoint "
                "test-scenario choice within the cited 3-5 range)",
            "p_choose_capital_buyin": "test-scenario value, not canon-derived: §2.5a IT-8 "
                "states no base rate for choosing the capital buy-in over the Masterpiece "
                "Examination",
            "p_masterpiece_pass": "test-scenario value, not canon-derived: no pass rate "
                "stated for the Masterpiece Examination",
            "p_caste_reject_on_fail": "PROVISIONAL: designs/provincial/faction_politics_v30.md "
                "§2.5 caste note — 'the committee can reject Einhir candidates on procedural "
                "grounds' — modeled here as one possible cause of a Masterpiece Examination "
                "failure (rate itself is test-scenario, not stated numerically in canon)",
            "amend_pool": "test-scenario value, not canon-derived: dice pool size is "
                "character-build-dependent, no single fixed pool size for this roll",
            "amend_tn": f"engine/params/core.md verified: {std_tn!r} (TN Values / Standard)",
            "amend_ob": "PROVISIONAL: designs/territory/governance_play_redesign_v1.md "
                "§1.3c — 'Amend — Charisma/Cognition vs the Guild Master, Ob 2'",
        }
        return params, provenance

    def decision_points(self) -> list[DecisionPoint]:
        return [
            DecisionPoint(
                name="entry_fork", default_tier=Tier.MEDIUM,
                branches=["guarantor_clean", "guarantor_burned", "sole_patron_clean", "sole_patron_burned"],
                justification="§2.5a BYZ-3: writes a durable Vouched-For/Vouches-Carelessly "
                               "tag and a Disposition swing across multiple NPCs — a "
                               "cross-actor ledger write, tier-2 per the rubric",
            ),
            DecisionPoint(
                name="mastership_fork", default_tier=Tier.MEDIUM,
                branches=["masterpiece_pass", "masterpiece_reject_caste", "capital_buyin_upstart"],
                justification="§2.5a IT-8: writes a durable Upstart tag with a 4-season "
                               "mentorship lockout and an Ob-1 Schism-check exposure — a "
                               "durable settlement/faction-scale write",
            ),
            DecisionPoint(
                name="ordenanza_ratification", default_tier=Tier.MEDIUM,
                branches=["overwhelming", "success", "partial", "failure"],
                justification="§1.3c Hold Court branch: a contest verdict that gates a "
                               "possible caste-exclusion policy lock-in — tier-2 per the "
                               "'contest verdict' rubric row",
            ),
        ]

    def run_once(self, rng, params: dict, decision_point: DecisionPoint) -> Outcome:
        if decision_point.name == "entry_fork":
            guarantor_path = rng.random() < params["p_choose_guarantor_path"]
            violated = rng.random() < params["p_entry_violation"]
            if guarantor_path:
                branch = "guarantor_burned" if violated else "guarantor_clean"
            else:
                branch = "sole_patron_burned" if violated else "sole_patron_clean"
            return Outcome(decision_point.name, branch, {"branch": branch})

        if decision_point.name == "mastership_fork":
            if rng.random() < params["p_choose_capital_buyin"]:
                branch = "capital_buyin_upstart"
            elif rng.random() < params["p_masterpiece_pass"]:
                branch = "masterpiece_pass"
            else:
                branch = "masterpiece_reject_caste"
            return Outcome(decision_point.name, branch, {"branch": branch})

        if decision_point.name == "ordenanza_ratification":
            r = valoria_dice.roll_pool(params["amend_pool"], params["amend_tn"], rng)
            branch = valoria_dice.classify_outcome(r, params["amend_ob"])
            return Outcome(decision_point.name, r, {"branch": branch})

        raise ValueError(f"unknown decision point {decision_point.name!r}")
