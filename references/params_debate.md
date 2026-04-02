<!-- version: v0.14+design-ST | sources: debate_system_redesign_v1.md Part 6 (compiled) | last_updated: 2026-04-02 -->
<!-- PATCHES APPLIED: D-01–D-10, R-01–R-07, v2-P01–v2-P04 compiled into Part 6 of redesign_v1 -->
<!-- stage9_social.md is EMPTY in v0.14. All values from design proposals. -->
<!-- STALE CHECK: All values [PROPOSAL]. Verify against compiled stage9 before use. -->

# params_debate.md — Debate System (v1, patched)

## Pools
| Roll | Pool | TN | Notes |
|------|------|----|-------|
| Argue | Cognition + History bonus | 7 | Main contest roll |
| Read | Attunement only (no History) | 7 Ob 1 | Per exchange, before Choose |
| Memory bonus | +2D | — | When citing specific named verifiable claim. Binary. Any genre. |
| Composure damage | — | — | From losing exchanges |

## Initiative
Exchange 1: higher Presence acts first.
Subsequent: transfers to exchange winner. Tie: stays with holder.
Post-Diverge state: stays with holder. No re-Read.

## Exchange Structure
**Step 1 — Read** (both orators, Attunement, TN7 Ob1):
| Net | Information |
|-----|-------------|
| Failure | Misleading signal: one weak genre identified as strong |
| Partial (1) | Primary genre identified only |
| Success (2) | Primary genre + orientation preference |
| Overwhelming (3+) | Genre + orientation + one specific detail |

**Step 2 — Choose:** Each orator selects Genre (Past/Present/Future) + Orientation (Revealing/Obscuring).

**Step 3 — Argue:** Initiative holder declares and rolls first. Respondent hears, then declares and rolls.

**Step 4 — Resolve** (by interaction type):

| Interaction | Condition | Resolution |
|-------------|-----------|-----------|
| CLASH | Same genre, opposite orientation | Compare successes. Margin = difference. Apply movement formula. |
| AMPLIFY | Same genre, same orientation | Combined pools vs Conviction Track resistance. |
| CROSS | Different genres | Each evaluated independently. |
| DIVERGE | Post-Diverge state | No Read/Choose. Direct pool vs pool, flat orientation weights. |

## Conviction Track
Range: 0–10. Side A wins ≥ 7. Side B wins ≤ 3. Compromise zone: 4–6.
Starting position: GM-set, typically 4–6 neutral.
Audience resistance = average Stability of represented factions (round up; typical 1–3).

Movement formula:
- If (margin × genre_weight × orientation_weight) ≤ resistance → 0 movement.
- If greater → ⌊(margin × genre_weight × orientation_weight) − resistance⌋ toward winner.

## Genre Weights
Primary genre: ×1.0. Other two genres: ×0.5 base.
One genre boosted +0.5 by audience ethical mode:
| Faction / Mode | Boosted Genre |
|----------------|--------------|
| Crown (Virtue Ethics) | Present |
| Church (Divine Command) | Past |
| Hafenmark (Categorical Imperative) | Past |
| Varfell (Consequentialism) | Future |
| Guilds (Moral Relativism) | GM picks |
| Restoration (Rawlsian Social Contract) | Future |

Weight range: 0.5–1.5. Never 0, never above 1.5. Fixed at setup.

## Orientation Weights
Revealing: ×1.0 | Obscuring: ×0.75 (invertible for specific scenarios).
Fixed at setup; recorded in ledger.

## Composure
[GAP: exact Composure formula not finalised — attribute mapping pending. From design intent:]
Pool likely: Endurance + Poise or Presence.
Rattled threshold: Composure ≤ 2 → −2D all Argue rolls.
Recovery: Reframe action (costs initiative; Ob 2 Cognition check).
Concession: voluntary, or forced at Composure 0.

## Diverge State
Triggered when: margin threshold met but Conviction Track still in compromise zone after N exchanges (GM discretion).
Effect: No Read, no genre choice. Orientation weights flatten. Initiative stays with holder.
Ends: when Conviction exits compromise zone or Composure concession fires.

## Multi-Party Debates
[GAP: multi-party procedure not yet defined — design_v1.md F-5 identifies this as a structural gap.]

## COMPILED MECHANICS SUMMARY (from debate_system_redesign_v1.md Part 6, 2026-04-02)

### Key Formulas
Presence modifier = floor((Presence − 3) / 2) → +0/+1/+2
Focus defence = floor(Focus / 2) → passive, no roll
Composure = Poise + Bonds + 3
Concentration = Focus + Presence (depletes −1/exchange, −1 extra on loss)
Attunement read pool = Attunement only (no History)
Memory bonus = +2D for specific named verifiable citation (binary)

### Conviction Track
Scale 0–10. Side A wins ≥7, Side B wins ≤3, compromise 4–6.
Audience resistance = avg Stability − 1 (min 0).
Movement: effective_margin = floor(margin × genre_weight × orientation_weight).
If effective_margin > resistance → Δ = effective_margin − resistance. Else 0.
Divergence uses half successes: floor((successes/2) × weight).

### Genre Weights
Primary genre: ×1.0. Others: ×0.5 base. Ethical mode adjusts one genre +0.5.
Crown: Present +0.5. Church/Hafenmark: Past +0.5. Varfell/Restoration: Future +0.5.
Guilds: GM picks. Range: 0.5/1.0/1.5.

### Strain
Strain = margin + 1 + Presence_modifier. Reduced by floor(Focus/2).
Rattled at strain ≥ Composure: −2D, lose Focus defence.

### Interaction Types
CLASH (same genre, opposite orientation): standard resolution.
COMPETITION (same genre, same orientation): reduced strain (margin−1 min 1).
DIVERGENCE (different genre): half-successes, no strain, initiative stays.
OBSCURING win: no tracker movement; place Doubt Marker (−2 to opponent's next effective_margin).
TIE: both take 1 strain, tracker +1 toward initiative holder.

### Asymmetric Proceedings
Disadvantaged party faces halved resistance (round up) for their tracker movement.

## PENDING EDITORIALS
- ED-044: Obscuring as pure denial — confirm design intent (P1)
- ED-041: Niflhel social mode scope (P2)
- ED-042: Grand Debate role alternation (P2)
- ED-043: Corroboration in Church Tribunal (P2)
- ED-045: Genre pivot mid-debate (P2)
