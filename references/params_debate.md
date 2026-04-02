<!-- version: v0.14+design | sources: stage9_social.md (empty), designs/debate/debate_system_redesign_v1.md, debate_stress_test_v2.md | last_updated: 2026-03-30 -->
<!-- NOTE: stage9_social.md is empty in v0.14. All debate params are from design proposals only. -->
<!-- STALE CHECK: All values marked [PROPOSAL]. Not compiled. Verify against compiled stage9 before use. -->

# params_debate.md — Debate System

## Pool Formula [PROPOSAL — debate_system_redesign_v1.md]
Argue pool: Cognition + History bonus, TN 7
Read pool: Attunement only (no History), TN 7 Ob 1
Memory bonus: +2D when citing a specific named verifiable claim (binary)

## Exchange Structure [PROPOSAL — stress_test_v2.md patched system]

### Step 1 — Read
| Net | Output |
|-----|--------|
| Failure (0) | Misleading signal — one weak genre identified as strong |
| Partial (1) | Primary genre identified only |
| Success (2) | Primary genre + orientation preference |
| Overwhelming (3+) | Genre + orientation + one specific detail |

### Step 2 — Choose
Each orator selects: Genre (Past / Present / Future) + Orientation (Revealing / Obscuring)

### Step 3 — Argue
Initiative holder declares and rolls first. Respondent hears, then rolls.

### Step 4 — Resolve (by interaction type)
**CLASH** (same genre, opposite orientation): compare successes, margin = difference.
**AMPLIFY** (same genre, same orientation): both pools combined against Conviction Track.
**CROSS** (different genres): each roll evaluated independently against track.
**DIVERGE** (Post-Diverge state): no Read, no genre selection; direct pool vs pool with flat orientation weights.

## Conviction Track [PROPOSAL]
Range: 0–10. Side A wins at ≥7. Side B wins at ≤3. Compromise zone: 4–6.
Starting position: GM-set, typically 4–6 for neutral audience.
Audience resistance = average Stability of represented factions (round up, typical 1–3).

Movement formula: If (margin × genre_weight × orientation_weight) ≤ resistance → 0 movement.
If greater → (margin × genre_weight × orientation_weight) − resistance, rounded down.

## Genre Weights [PROPOSAL]
- Primary genre: ×1.0
- Other two genres: ×0.5 base
- Audience ethical mode adjusts ONE genre by +0.5:

| Faction ethical mode | Boosted genre |
|---------------------|--------------|
| Virtue Ethics (Crown) | Present +0.5 |
| Divine Command (Church) | Past +0.5 |
| Categorical Imperative (Hafenmark) | Past +0.5 |
| Consequentialism (Varfell) | Future +0.5 |
| Moral Relativism (Guilds) | GM picks |
| Rawlsian Social Contract (Restoration) | Future +0.5 |

Weight range: 0.5 / 1.0 / 1.5. Never 0, never above 1.5. Fixed at setup.

## Orientation Weights [PROPOSAL]
Revealing: ×1.0 | Obscuring: ×0.75 (invertible for specific scenarios)

## Initiative [PROPOSAL]
Exchange 1: higher Presence goes first.
Subsequent: transfers to exchange winner. Tie: stays with holder.
Post-Diverge: stays with holder.

## Composure [PROPOSAL]
Composure = Endurance + Poise (or Presence — [GAP: attribute mapping not finalised])
Rattled threshold: Composure ≤ 2 → −2D on all Argue rolls.
Recovery: Reframe action (costs initiative, Ob 2 Cognition check).
Concession: voluntary or forced at Composure 0.
