"""goldenfurt_fixture.py — shared Goldenfurt (S-006) test data for the pr119_governance
adapter cluster.

Builds a real systems.settlements.sim.registry.Settlement (the actual dataclass, not a
re-implementation) populated with values hand-transcribed from
systems/settlements/goldenfurt_slice/{npc_cast,event_deck,sim_build_spec}.md — the one
worked, adversarially-verified vertical slice governance_play_redesign_v1.md was authored
against. Every value's provenance is documented in PROVENANCE below, mirroring the
Adapter.resolve_params() discipline: nothing here is a fabricated number.

Grounding this cluster in Goldenfurt rather than inventing settlements (as PR#125's
LLM-narrative stress test did) is the explicit recommendation of
designs/audit/2026-07-12-settlement-season-stress-sim/reconciliation_with_existing_territory_work.md:
"Ground future runs in Goldenfurt... any re-run should seed from goldenfurt_slice... and
should include the existing work in-kernel so it stops re-deriving solved problems."

build_goldenfurt_settlement() returns a FRESH Settlement on every call — trials mutate
state (ledger writes, suspicion, pressure), so a shared singleton would leak state across
decision points and across trials within one decision point.
"""
from __future__ import annotations

from systems.settlements.sim.registry import Settlement

SID = "S-006"
SETTLEMENT_NAME = "Goldenfurt"

# NPC dossiers -- id -> the fields this adapter cluster actually consumes.
# Source: systems/settlements/goldenfurt_slice/npc_cast.md.
NPCS = {
    "NPC-G01": {"name": "Hedda Vorn", "role": "Magistrate (local law)", "disposition": 1},
    "NPC-G02": {
        "name": "Orsk Tallow", "role": "Grainmaster (Guild factor)", "disposition": 1,
        # npc_cast.md calls Orsk a "Guild factor" pursuing "a perpetual Guild charter" but
        # states no numeric Gu-Std rank. Transcribed as Gu-Std 3 (Guild Master) — the rank
        # faction_politics_v30 §2.5/§2.5a's ordenanza-authoring and §3.3a/b charter-holding
        # both require — a test-scenario value, not a canon-derived one (npc_cast.md itself
        # never states it numerically).
        "guild_standing": 3,
    },
    "NPC-G03": {"name": "Curate Wessel", "role": "Church, parish priest", "disposition": 1},
    "NPC-G04": {"name": "Tomas Vorn", "role": "smuggler (Niflhel-linked broker)", "disposition": 0},
    "NPC-G05": {"name": "Greta Saatfeld", "role": "RM cell elder", "disposition": 0},
    "NPC-G06": {
        "name": "Bailiff Konrad Ems", "role": "Crown levy agent", "disposition": 1,
        "progress": 0,                    # npc_cast.md NPC-G06 "Timeline: 4 seasons. Progress: 0."
        "progress_cap_per_season": 1,     # event_deck.md EVT-G606: "Konrad's advance is capped +1/season"
        "fires_threshold": 4,             # event_deck.md EVT-G606: "fires when G06 progress >= 4"
    },
}
# npc_cast.md "Minor Local Actors (petition generators)" table.
LOCAL_ACTORS = ["LA-G01", "LA-G02", "LA-G03"]  # Mertha, Old Brun, Sister Aldith

PROVENANCE = {
    "identity": "PROVISIONAL: systems/settlements/goldenfurt_slice/README.md — "
        "'S-006 Goldenfurt, a Crown breadbasket river-town in Kronmark province'",
    "pressure/facility_tier": "PROVISIONAL: systems/settlements/goldenfurt_slice/README.md "
        "worked-example opening state — 'AP = 3 (Town, FacilityTier 1). Pi = 4.' "
        "(registry.Settlement.ap = 2 + facility_tier for a Town, so facility_tier=1 "
        "reproduces the cited AP=3.)",
    "npc_ids": "PROVISIONAL: systems/settlements/goldenfurt_slice/npc_cast.md — NPC-G01..G06 "
        "+ LA-G01..G03 (9 named actors total)",
    "npc dispositions/progress": "PROVISIONAL: systems/settlements/goldenfurt_slice/npc_cast.md, "
        "each NPC's own 'Loyalty/Disposition(governor)' and (for Konrad, G06) 'Progress' lines; "
        "event_deck.md EVT-G606 for the +1/season cap and >=4 fire threshold",
    "religious_building": "PROVISIONAL: npc_cast.md NPC-G03's ambition is to upgrade the town "
        "'Chapel to a Church' — the opening state is therefore pre-upgrade, transcribed as "
        "'Chapel' (registry.Settlement's own default is 'None', which Goldenfurt's README "
        "does not describe; 'Chapel' is the state NPC-G03's arc upgrades FROM)",
    "suspicion": "test-scenario value, not canon-derived: no explicit start value is stated "
        "anywhere in goldenfurt_slice — the worked example opens with the first Directive "
        "as the first suspicion-bearing event, so a new governor's opening suspicion is "
        "declared here as 0",
    "legitimacy/popular_support": "PROVISIONAL: left at registry.Settlement's own default (0) "
        "— per registry.py's own inline note, these fields are PORT-BLOCKING/inert "
        "(ED-FA-0004): 'declared but NEVER READ OR WRITTEN anywhere in sim/'",
}


def build_goldenfurt_settlement() -> Settlement:
    """A fresh Settlement per call — see module docstring."""
    return Settlement(
        sid=SID, name=SETTLEMENT_NAME, stype="Town", province_id="Kronmark",
        owner_faction="Crown", governor_id=None,
        prosperity=3, defense=1, order=2, fort_level=0, garrison=False,
        legitimacy=0, popular_support=0,
        facility_tier=1, suspicion=0, pressure=4.0,
        religious_building="Chapel",
        npc_ids=list(NPCS) + list(LOCAL_ACTORS),
    )
