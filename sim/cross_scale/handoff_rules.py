"""
sim/cross_scale/handoff_rules.py — 8 handoff rules between scales (§3)

Canon source: designs/architecture/scale_transitions_v30.md §3

Implements the 8 named handoff rules §3.1-§3.8 plus the §3.9 Fieldwork
cross-system table. Each handoff is a typed rule: given a from_scale and
to_scale, it returns a HandoffResult describing the procedure to apply.

This module is a rule registry + dispatcher. It does NOT execute downstream
mechanics (that's the receiving module's responsibility). It produces the
shape and timing of the transition so callers know what to do next.

[ASSUMPTION: dispatcher returns a procedure descriptor rather than executing
 receiver-side mechanics — basis: §3 rules name procedures but their
 execution lives in receiver-modules (mass_battle, contest, fieldwork,
 etc). Cross-scale module owns the protocol; receiver modules own the
 mechanics. Avoids duplicating logic that lives in already-implemented
 modules.]

Dependencies:
  - sim/autoload/game_state

Entry points:
  - apply_handoff(from_scale: str, to_scale: str, payload: dict, world: GameState) -> HandoffResult
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


# §2 Scale labels (canonical names used in handoff routing)
# [canonical: designs/architecture/scale_transitions_v30.md §2 Scale Table]
SCALE_PERSONAL = "Personal"
SCALE_SCENE = "Scene"        # Contest / fieldwork scenes
SCALE_THREAD = "Thread"
SCALE_FACTION = "Faction"    # BG strategic
SCALE_MASS = "Mass"          # Mass battle
SCALE_FIELDWORK = "Fieldwork"

# Handoff rule names from §3.1-§3.8
RULE_PERSONAL_TO_THREAD = "§3.1 Personal → Thread"
RULE_PERSONAL_TO_FACTION = "§3.2 Personal → Faction"
RULE_PERSONAL_TO_SCENE = "§3.3 Personal → Scene (Contest)"
RULE_SCENE_TO_FACTION = "§3.4 Scene → Faction (Domain Echo)"
RULE_THREAD_TO_FACTION = "§3.5 Thread → Faction"
RULE_THREAD_TO_MASS = "§3.6 Thread → Mass (Mass Battle Integration)"
RULE_MASS_TO_PERSONAL = "§3.7 Mass → Personal (General Duel)"
RULE_SCENE_TO_MASS = "§3.8 Scene → Mass"


# §3.6 Thread → Mass coherence costs by Thread Saturation
# [canonical: §3.6 — "Skirmish/Company (TS ≥ 30, Coherence cost 0/op),
#  Battle/Campaign (TS ≥ 50, Coherence cost −1/op), War (TS ≥ 70,
#  Coherence cost −2/op)"]
TS_SKIRMISH_MIN = 30   # TS >= 30: Coherence 0/op
TS_BATTLE_MIN = 50     # TS >= 50: Coherence -1/op
TS_WAR_MIN = 70        # TS >= 70: Coherence -2/op

# §3.7 Mass → Personal General Duel limits
# [canonical: §3.7 — "Limit: 1 exchange per battle turn. Maximum 5 exchanges
#  before forced disengage or incapacitation."]
GENERAL_DUEL_EXCHANGES_PER_TURN = 1
GENERAL_DUEL_MAX_EXCHANGES = 5

# §3.8 Scene → Mass modifier durations
# [canonical: §3.8 — "1 turn duration"]
SCENE_TO_MASS_MODIFIER_TURNS = 1


@dataclass
class HandoffResult:
    """Descriptor of a scale transition's procedure + side effects."""
    rule_name: str               # §3.x rule label
    valid: bool                  # False if from→to is unsupported
    procedure: list[str]         # ordered procedure steps from canon
    coherence_cost: int = 0      # If applicable (§3.6 TS-banded)
    modifier_turns: int = 0      # If applicable (§3.8)
    notes: list[str] = field(default_factory=list)


def _ts_to_coherence_cost(ts: int) -> int:
    """Per §3.6 TS bands."""
    if ts >= TS_WAR_MIN:
        return -2
    if ts >= TS_BATTLE_MIN:
        return -1
    return 0  # Skirmish/Company default — TS >= 30 also returns 0


def apply_handoff(from_scale: str, to_scale: str, payload: dict, world=None) -> HandoffResult:
    """Look up and return the §3 handoff rule for the given scale transition.

    payload carries rule-specific context (e.g. {'TS': 55} for §3.6, or
    {'degree': 'Success'} for §3.4 Domain Echo trigger).
    world is preserved for callers that need state lookup; this dispatcher
    does not mutate world.
    """
    key = (from_scale, to_scale)

    if key == (SCALE_PERSONAL, SCALE_THREAD):
        # [canonical: §3.1 — "Leap triggers. Contact duration starts on the
        #  round Leap succeeds. Thread pool and operations become available.
        #  Return to Personal scale on Contact end or voluntary withdrawal."]
        return HandoffResult(
            rule_name=RULE_PERSONAL_TO_THREAD,
            valid=True,
            procedure=[
                "Roll Leap (per threadwork §2.3)",
                "On success: Contact duration starts; Thread pool available",
                "On contact end / voluntary withdrawal: return to Personal scale",
            ],
        )

    if key == (SCALE_PERSONAL, SCALE_FACTION):
        # [canonical: §3.2 — "Personal Ob resolves first, then Domain Action
        #  Ob. Same roll — the personal action produces the faction
        #  consequence through Domain Echo (§5)."]
        return HandoffResult(
            rule_name=RULE_PERSONAL_TO_FACTION,
            valid=True,
            procedure=[
                "Resolve Personal Ob",
                "Apply Domain Action Ob to same roll result",
                "Domain Echo per §5 fires on Sufficient Scope (§7)",
            ],
        )

    if key == (SCALE_PERSONAL, SCALE_SCENE):
        # [canonical: §3.3 — stub-filled section per ED-748]
        return HandoffResult(
            rule_name=RULE_PERSONAL_TO_SCENE,
            valid=True,
            procedure=["Open Contest scene per social_contest_v30"],
            notes=["§3.3 is brief in canon — see social_contest_v30 for full procedure"],
        )

    if key == (SCALE_SCENE, SCALE_FACTION):
        # [canonical: §3.4 — Sufficient Scope (§7) gating; PP-329 cap]
        return HandoffResult(
            rule_name=RULE_SCENE_TO_FACTION,
            valid=True,
            procedure=[
                "Check Sufficient Scope (§7) — if not met, no Echo fires",
                "Apply §5.2 amount table by degree",
                "Cap: 1 Domain Echo per faction per scene (PP-329)",
                "Multi-condition tie-break by priority order (§3.2)",
            ],
            notes=["Priority order: Thread op → Combat victory → Settlement governance → Disposition reach → Investigation completion → Faction-leader-direct → Other"],
        )

    if key == (SCALE_THREAD, SCALE_FACTION):
        # [canonical: §3.5 — "Thread operation targeting faction-level
        #  configuration resolves as Domain Action. Thread pool used,
        #  appropriate Ob applied. No extra roll — the Thread operation IS
        #  the faction action."]
        return HandoffResult(
            rule_name=RULE_THREAD_TO_FACTION,
            valid=True,
            procedure=[
                "Thread operation resolves as Domain Action (no extra roll)",
                "Use Thread pool",
                "Apply Domain-Action-appropriate Ob",
            ],
        )

    if key == (SCALE_THREAD, SCALE_MASS):
        # [canonical: §3.6 — Thread Substrate cost differential by TS band]
        ts = payload.get('TS', 0)
        cost = _ts_to_coherence_cost(ts)
        return HandoffResult(
            rule_name=RULE_THREAD_TO_MASS,
            valid=True,
            procedure=[
                "Position Phase 4 (offensive) or Phase 6 step 4-5 (support)",
                "Resolve per mass_battle §A.10",
                "Apply at Phase 6 Step 1 (simultaneous with Volley + Engagement)",
                f"Coherence cost {cost} per op (TS={ts} band)",
            ],
            coherence_cost=cost,
            notes=[f"TS bands: <{TS_BATTLE_MIN}=0/op, <{TS_WAR_MIN}=-1/op, >={TS_WAR_MIN}=-2/op"],
        )

    if key == (SCALE_MASS, SCALE_PERSONAL):
        # [canonical: §3.7 — "Personal Action available at Phase 5 (Priority 8).
        #  Limit: 1 exchange per battle turn. General's Command Rating
        #  suspended while in personal combat. Maximum 5 exchanges before
        #  forced disengage or incapacitation. One mass combat turn = one
        #  personal combat exchange."]
        return HandoffResult(
            rule_name=RULE_MASS_TO_PERSONAL,
            valid=True,
            procedure=[
                f"Available at Phase 5 (Priority 8); limit {GENERAL_DUEL_EXCHANGES_PER_TURN} exchange/battle turn",
                "Suspend General's Command Rating (PP-232)",
                f"Maximum {GENERAL_DUEL_MAX_EXCHANGES} exchanges before forced disengage/incap",
                "1 mass turn = 1 personal exchange (PP-111)",
            ],
        )

    if key == (SCALE_SCENE, SCALE_MASS):
        # [canonical: §3.8 — Scene win modifiers apply to next mass battle
        #  turn only, 1 turn duration, PP-261/ED-151]
        return HandoffResult(
            rule_name=RULE_SCENE_TO_MASS,
            valid=True,
            procedure=[
                "Social win: +1D to relevant unit Command (next turn only)",
                "Investigation win: +1D to first Volley (next turn only)",
                "Combat win: one free Reform action (next turn only)",
            ],
            modifier_turns=SCENE_TO_MASS_MODIFIER_TURNS,
            notes=["Modifier targets most relevant unit per scene type (PP-261, ED-151)"],
        )

    # Fieldwork ↔ All Systems (§3.9) — return descriptive result
    if SCALE_FIELDWORK in key:
        return HandoffResult(
            rule_name=f"§3.9 Fieldwork ↔ {to_scale if from_scale == SCALE_FIELDWORK else from_scale}",
            valid=True,
            procedure=[f"See §3.9 table for {from_scale} → {to_scale} procedure"],
            notes=["§3.9 has detailed per-pair table not enumerated in this dispatcher; consumer-side lookup expected"],
        )

    # Unsupported transition
    return HandoffResult(
        rule_name=f"({from_scale} → {to_scale})",
        valid=False,
        procedure=[],
        notes=[f"No §3 rule defined for {from_scale} → {to_scale}; transition invalid"],
    )
