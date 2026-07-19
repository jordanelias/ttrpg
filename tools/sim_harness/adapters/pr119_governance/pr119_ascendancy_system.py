"""pr119_ascendancy_system.py — provisional adapter testing the "character political standing/
advancement/demotion" system: designs/audit/2026-07-12-governance-compendium/
40_roster_officer_system.md (the "Ascendancy" system, PROPOSED, zero ratification, zero sim/
implementation per the compendium research pass). This is the piece explicitly missing from
the first two verification passes -- neither PR#119's 12 items nor the interdependency/event-
deck engines model how an NPC (or the player) actually GAINS and CONSOLIDATES political power,
only how a sitting governor loses it.

Core mechanic (40_roster_officer_system.md): every NPC's rise is typed by a `power_base` enum
{patronage, merit, kinship, bureaucratic, military, purchased, ideological} whose CLIMB driver
and DOWNFALL liability are structurally matched (the Omega-d non-dominance design principle) --
e.g. patronage rises via clientele breadth, collapses top-down when the patron falls; purchased/
bureaucratic power rises via bribery, collapses when the bribery is discovered. A
`consolidation_progress` (0-5) counter (the doc reuses ambition.progress/trajectory directly,
no new field) advances autonomously each season; at threshold it fires an "Ascendancy card".

Grounded on two real Goldenfurt NPCs whose npc_cast.md dossiers already imply a power_base:
  - Konrad (NPC-G06): bureaucratic/patronage -- "he takes Orsk's coin for advance levy notice"
    (npc_cast.md) is a textbook Omega-d bureaucratic-corruption liability, already exercised as
    a real ledger write (Leverage:konrad-corrupt) in pr119_integrated_campaign.py and
    pr119_event_deck_engine.py -- reused here, not re-derived.
  - Orsk (NPC-G02): purchased/bureaucratic -- pursues "a perpetual Guild charter" via "bribery
    (he pays Konrad)" per npc_cast.md's own escalation ladder.

canon_row=None: 40_roster_officer_system.md is PROPOSED research, no CURRENT.md row.
contract_module="faction_politics": Ascendancy is explicitly a rank/Standing-ladder overlay
(the compendium's own "shared rank space" decision -- NPCs climb the SAME Standing ladder as
the player), closest existing module_contracts.yaml binding.
"""
from __future__ import annotations

from ...adapter import Adapter, Outcome, register_adapter
from ...depth import DecisionPoint, Tier
from .goldenfurt_fixture import NPCS, build_goldenfurt_settlement

_KONRAD = NPCS["NPC-G06"]
_ORSK = NPCS["NPC-G02"]
_CONSOLIDATION_THRESHOLD = 5  # 40_roster_officer_system.md: "consolidation_progress (0-5)"


@register_adapter("pr119_ascendancy_system")
class AscendancySystemAdapter(Adapter):
    contract_module = "faction_politics"
    canon_row = None
    registry_subsystem = "faction_political"

    def resolve_params(self, resolver) -> tuple:
        params = {
            "consolidation_threshold": _CONSOLIDATION_THRESHOLD,
            "seasons": 10,
            "p_advance_bureaucratic": 0.4,
            "p_advance_patronage": 0.3,
            "p_liability_discovered_per_season": 0.15,
        }
        provenance = {
            "consolidation_threshold": "PROVISIONAL: designs/audit/2026-07-12-governance-"
                "compendium/40_roster_officer_system.md -- 'consolidation_progress (0-5)'",
            "seasons": "test-scenario value, not canon-derived: a mid-length window for a "
                "climb-and-possible-downfall arc to play out",
            "p_advance_bureaucratic": "test-scenario value, not canon-derived: the doc's "
                "'power_base-typed driver' table gives per-type advance RULES (e.g. "
                "'purchased: instant on Treasury spend') but not a probability -- this is a "
                "documented simplification for Konrad/Orsk's bureaucratic/purchased path",
            "p_advance_patronage": "test-scenario value, not canon-derived: same table, "
                "patronage-type advance rate",
            "p_liability_discovered_per_season": "test-scenario value, not canon-derived: "
                "the doc's Omega-d downfall table states EACH power_base writes a legible, "
                "rival-exploitable liability, not a discovery rate -- reuses the same "
                "corruption-discovery shape already parameterized in pr119_clerk_capacity.py",
        }
        return params, provenance

    def decision_points(self) -> list:
        return [
            DecisionPoint(
                name="consolidation_climb", default_tier=Tier.MEDIUM,
                branches=["reached_threshold", "stalled"],
                justification="an Ascendancy-card fire is a faction-scale rank event with "
                               "cross-NPC consequences (the doc's own worked example: 'install "
                               "successor, capture the gate, purge predecessor') -- tier-2 per "
                               "the rubric",
            ),
            DecisionPoint(
                name="downfall_exploitation", default_tier=Tier.MEDIUM,
                branches=["exploited_bureaucratic", "exploited_patronage", "undiscovered"],
                justification="exploiting the Omega-d liability writes a real cross-scale "
                               "Leverage ledger tag (reused from pr119_integrated_campaign.py) "
                               "-- tier-2 per the rubric",
            ),
        ]

    def run_once(self, rng, params: dict, decision_point: DecisionPoint) -> Outcome:
        if decision_point.name == "consolidation_climb":
            progress = 0
            for _season in range(params["seasons"]):
                if rng.random() < params["p_advance_bureaucratic"]:
                    progress += 1
                if progress >= params["consolidation_threshold"]:
                    break
            branch = ("reached_threshold" if progress >= params["consolidation_threshold"]
                       else "stalled")
            return Outcome(decision_point.name, progress, {"branch": branch})

        if decision_point.name == "downfall_exploitation":
            s = build_goldenfurt_settlement()
            bureaucratic_progress = 0
            patronage_progress = 0
            exposed_bureaucratic = False
            exposed_patronage = False
            for season in range(params["seasons"]):
                bureaucratic_progress += 1 if rng.random() < params["p_advance_bureaucratic"] else 0
                patronage_progress += 1 if rng.random() < params["p_advance_patronage"] else 0
                if (bureaucratic_progress > 0
                        and rng.random() < params["p_liability_discovered_per_season"]):
                    exposed_bureaucratic = True
                    # Real ledger write -- the same Leverage tag both campaign engines already
                    # use as Konrad's Omega-d bureaucratic-corruption liability.
                    s.add_tag("Leverage", "konrad-corrupt", created_season=season)
                    break
                if (patronage_progress > 0
                        and rng.random() < params["p_liability_discovered_per_season"]):
                    exposed_patronage = True
                    s.add_tag("Grudge", "patron-fell", created_season=season)
                    break
            if exposed_bureaucratic:
                branch = "exploited_bureaucratic"
            elif exposed_patronage:
                branch = "exploited_patronage"
            else:
                branch = "undiscovered"
            return Outcome(
                decision_point.name,
                {"bureaucratic_progress": bureaucratic_progress,
                 "patronage_progress": patronage_progress,
                 "leverage_tag_written": s.has_tag("Leverage", "konrad-corrupt")},
                {"branch": branch},
            )

        raise ValueError(f"unknown decision point {decision_point.name!r}")
