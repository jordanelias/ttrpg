"""
sim/cross_scale/zoom_in_out.py — Zoom In/Out protocol (§4)

Canon source: designs/architecture/scale_transitions_v30.md §4

Implements §4.1-§4.4: Zoom In legal entry points (PP-103), scene Ob
modifier by board degree, Zoom Out state-transfer + Phase 6 continuation,
trigger registries (§4.3.2 mandatory + §4.3.3 world-state).

Dependencies:
  - sim/autoload/game_state

Entry points:
  - zoom_in(from_phase: str, board_degree: str | None, world: GameState) -> ZoomInResult
  - zoom_out(scene_outcomes: dict, world: GameState) -> ZoomOutResult
  - check_mandatory_triggers(world: GameState) -> list[ZoomTrigger]
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


# §4.1 Legal Zoom In entry points (PP-103)
# [canonical: §4.1 — "After Phase 1 (declarations), After Phase 3 (movement),
#  After Phase 6 Step 1 (damage application). Mid-Phase-5 Zoom In defers to
#  after Phase 6 Step 1 (PP-250, ED-158)."]
LEGAL_ZOOM_IN_PHASES = {"after_phase_1", "after_phase_3", "after_phase_6_step_1"}
MID_PHASE_5_DEFER_TO = "after_phase_6_step_1"

# §4.1 Scene Ob modifier by board degree
# [canonical: §4.1 Scene Opportunity table]
SCENE_OB_MODIFIER_BY_DEGREE = {
    "Failure": +1,          # "Board FAILURE → scene Ob +1 (harder)"
    "Partial": 0,           # implicit — only listed degrees adjust Ob
    "Success": -1,          # "Board SUCCESS → scene Ob −1 (easier)"
    "Overwhelming": -2,     # "Board OVERWHELMING → scene Ob −2"
}

# §4.3.2 Mandatory triggers (Scene Slate Priority 0)
MANDATORY_TRIGGER_PRIORITY = 0

# §4.3.3 World-State triggers (Scene Slate Priority 1)
WORLD_STATE_TRIGGER_PRIORITY = 1


@dataclass
class ZoomInResult:
    valid: bool
    deferred_to: Optional[str]   # If mid-phase-5, the phase to defer to
    scene_ob_modifier: int       # Per §4.1 board-degree table
    notes: list[str] = field(default_factory=list)


@dataclass
class ZoomOutResult:
    domain_echoes_queued: list[dict]
    pc_incap_applied: bool
    contested_figure_wound_ob: int  # ED-167: +1 Ob to commander BG tactic rolls if wound
    notes: list[str] = field(default_factory=list)


@dataclass
class ZoomTrigger:
    """A mandatory or world-state Zoom In trigger per §4.3."""
    trigger_name: str
    priority: int           # 0 (mandatory) or 1 (world-state)
    condition: str
    scene_content: str


def zoom_in(from_phase: str, board_degree: Optional[str], world=None) -> ZoomInResult:
    """Validate Zoom In entry per §4.1 PP-103 and apply scene Ob modifier."""
    notes = []
    deferred_to = None
    if from_phase == "mid_phase_5":
        # PP-250 / ED-158 deferral
        deferred_to = MID_PHASE_5_DEFER_TO
        notes.append("Mid-Phase-5 Zoom In defers to after Phase 6 Step 1 (PP-250, ED-158)")
        valid = True
    elif from_phase in LEGAL_ZOOM_IN_PHASES:
        valid = True
    else:
        valid = False
        notes.append(f"'{from_phase}' is not a legal Zoom In entry per PP-103")

    ob_mod = SCENE_OB_MODIFIER_BY_DEGREE.get(board_degree, 0) if board_degree else 0
    if board_degree and board_degree not in SCENE_OB_MODIFIER_BY_DEGREE:
        notes.append(f"Unknown board_degree '{board_degree}'; scene Ob modifier defaulted to 0")

    return ZoomInResult(
        valid=valid,
        deferred_to=deferred_to,
        scene_ob_modifier=ob_mod,
        notes=notes,
    )


def zoom_out(scene_outcomes: dict, world=None) -> ZoomOutResult:
    """Translate scene outcomes back into BG layer per §4.2.

    scene_outcomes accepts:
      - 'accord_changes': list of dicts (queued as Domain Echoes per §5.5)
      - 'pc_incapacitated': bool (Stage 1 applies immediately per ED-159)
      - 'contested_figure_wounded': bool (ED-167: +1 Ob to commander)
      - 'other_echoes': list of dicts (faction stat changes per §5)
    """
    notes = []
    domain_echoes = []

    # §5.5 Accord changes queue to Accounting
    for ac in scene_outcomes.get('accord_changes', []):
        domain_echoes.append({'type': 'accord', 'detail': ac, 'fires_at': 'accounting_step_4c'})

    # §5 other faction-stat changes also queue
    for oe in scene_outcomes.get('other_echoes', []):
        domain_echoes.append({'type': 'faction_stat', 'detail': oe, 'fires_at': 'accounting'})

    pc_incap = scene_outcomes.get('pc_incapacitated', False)
    if pc_incap:
        # [canonical: §4.2 — "PC incapacitation consequences (Stage 1) apply
        #  immediately on Zoom Out (ED-159)"]
        notes.append("PC incapacitation Stage 1 applies immediately (ED-159)")

    wound_ob = 1 if scene_outcomes.get('contested_figure_wounded', False) else 0
    if wound_ob:
        # [canonical: §4.2 — "Contested Figure wound → +1 Ob to commander's
        #  BG tactic rolls for remainder of battle (ED-167)"]
        notes.append("Contested Figure wound: +1 Ob to commander BG tactic rolls (ED-167)")

    notes.append("Phase 6 Steps 2-6 resolve after Zoom Out with updated state (PP-110)")

    return ZoomOutResult(
        domain_echoes_queued=domain_echoes,
        pc_incap_applied=pc_incap,
        contested_figure_wound_ob=wound_ob,
        notes=notes,
    )


def check_mandatory_triggers(world=None) -> list[ZoomTrigger]:
    """Return the canonical §4.3.2 mandatory trigger list.

    Actual world-state evaluation (settlement Order 0, faction Stability ≤ 2,
    etc) is consumer-side; this returns the trigger schema so callers can
    enumerate and evaluate.
    """
    # [canonical: §4.3.2 Mandatory Zoom In Triggers table]
    return [
        ZoomTrigger("Settlement Revolt", MANDATORY_TRIGGER_PRIORITY,
                    "Player in province containing settlement at Order 0",
                    "Revolt unfolds at specific settlement; player chooses combat/social/fieldwork/flee"),
        ZoomTrigger("Heresy Investigation Target", MANDATORY_TRIGGER_PRIORITY,
                    "Player is target of active Heresy Investigation",
                    "Inquisitor arrives; asymmetric social contest per social_contest §7"),
        ZoomTrigger("Faction Leader Removal", MANDATORY_TRIGGER_PRIORITY,
                    "Player's faction leader assassinated/overthrown/incapacitated",
                    "Witness or learn directly; succession mechanics fire per player_agency §5.2"),
        ZoomTrigger("Mass Battle at Settlement", MANDATORY_TRIGGER_PRIORITY,
                    "Mass battle targets settlement in player's current province",
                    "Caught in battle: participate or escape (Endurance Ob 2; failure = 1 wound)"),
        ZoomTrigger("Companion Arc Trigger", MANDATORY_TRIGGER_PRIORITY,
                    "Companion's arc branch trigger fires (npc_behavior §5.2)",
                    "Companion's transformation scene with player present"),
        ZoomTrigger("Knot Partner in Crisis", MANDATORY_TRIGGER_PRIORITY,
                    "NPC Knotted to player reaches Conviction crisis (Scar count ≥ 3)",
                    "Knot transmits crisis per P-12"),
        ZoomTrigger("Stability Crisis", MANDATORY_TRIGGER_PRIORITY,
                    "Faction Stability ≤ 2 at Accounting OR drops ≥ 2 in single Accounting",
                    "Emergency faction council; cannot be declined; hysteresis ED-749"),
        ZoomTrigger("Rank Advancement Recognition Event", MANDATORY_TRIGGER_PRIORITY,
                    "Player's Standing crosses rank threshold + Formal Recognition Event conditions met",
                    "Formal faction ceremony; player receives rank/insignia/obligations"),
    ]
