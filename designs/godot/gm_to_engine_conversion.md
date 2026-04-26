# Phase 5.1 — GM-to-Engine Rule Conversion
# Date: 2026-04-18
# Purpose: Define deterministic engine rules for every "GM" action in videogame mode.
# These rules are the Godot engine's resolution layer — no human judgment required.

---

## Conversion Registry

| Source | GM Reference | Deterministic Engine Rule |
|--------|-------------|--------------------------|
| Contest §2 Step 7 | "GM records on hidden ledger" | Engine tracks all contest state internally. Conviction Track, Composure, Concentration, and Resonant Style targeting are engine-managed. Player sees: current track position, their own Composure, opponent's visible state. Hidden: opponent's exact Composure, their targeting declaration before reveal. |
| NPC Behavior §3.3 | "GM judgment" for Scar progression | **Binary threshold:** Scar fires on any Decisive contest win (track ≥7 or ≤3) where the winner used the correct Resonant Style matching the NPC's vulnerability. No discretion. Correct MS + Decisive = Scar. Incorrect MS + Decisive = no Scar. Partial/Compromise = no Scar regardless. |
| Combat §4 Stunt | "GM sets N, max 5" | **Environmental modifier table:** Stunt bonus = POI type modifier + terrain modifier. POI types: Fortress interior +2, Ruins +3, Market/crowd +1, Open field +0, Ship deck +1, Cathedral +2. Terrain: elevation advantage +1, difficult footing −1, darkness +1 (ambush), water −2. Total capped at 5. Engine evaluates from scene location metadata. |
| Threadwork §3.6 | "GM determines domain type" for Lock MS drift | **Domain-type lookup from settlement type:** Seat = slow-change (MS drift −1/season), City/Town = moderate (−1/2 seasons), Port = moderate, Fortress = slow-change, Cathedral = slow-change (institutional inertia), Mine/Outpost = fast-change (−1/season + settlement Prosperity modifier). Engine reads settlement type from settlement_data.tres. |
| Fieldwork §4.1 | "GM sets threshold at investigation opening" | **Threshold = scope-based (already defined):** Simple = 3, Complex = 5, Structural = 8. Scope determined by Evidence Track depth: Depth 0-1 = Simple, Depth 2-3 = Complex, Depth 4-5 = Structural. No GM discretion — the investigation's depth determines its complexity. |
| Social Contest §2 Step 4 | "GM narrates partial outcome proportional to final position" | **Outcome table indexed by final Conviction Track position:** Track 4 = slight compromise toward A (A gets 60% of their demand, B gets 40%). Track 5 = true middle (50/50 split). Track 6 = slight compromise toward B. Track 3 or 7 = Decisive. Implementation: each contest defines an outcome table with position-indexed results. Generic fallback: Disposition ±1 for slight, ±2 for Decisive. |
| Investigation Systems | NPE "GM grants Belief revelation" | **Deterministic Belief reveal:** Belief revealed on (1) Observation: NPC acts on Belief in player's presence during a scene — the engine flags any NPC action that maps to a Belief keyword. (2) Appraise Overwhelming: pool check produces 3+ net → all three Beliefs revealed. (3) Thread-Read at TS ≥ 30 on NPC: one Belief revealed per successful Thread-Read. |

---

## Implementation Notes

### Videogame Mode Tags
Design docs may be annotated with `[VIDEOGAME: rule]` tags to inline the deterministic rule adjacent to the original GM-dependent text. This is optional — the conversion registry above is the canonical source. If both exist, this registry is authoritative.

### Engine Resolution Priority
When multiple deterministic rules could apply (e.g., a contest in a cathedral during a mass battle), the engine resolves in priority order:
1. Scene type determines primary resolution system (combat/contest/fieldwork/threadwork)
2. Location metadata provides environmental modifiers
3. NPC state provides targeting/Scar eligibility
4. Global clocks provide threshold checks

### Godot Architecture
Each conversion maps to a GDScript function in the relevant system autoload:
- `ContestManager.resolve_outcome(track_position)` → outcome table lookup
- `CombatManager.get_stunt_bonus(poi_type, terrain)` → environmental modifier
- `NPCManager.check_scar_eligibility(npc, contest_result, rs_used)` → binary threshold
- `FieldworkManager.get_investigation_threshold(depth)` → scope-based lookup
- `ThreadworkManager.get_lock_drift_rate(settlement_type)` → domain-type lookup
