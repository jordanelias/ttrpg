<!-- version: v0.14+design-ST2 | sources: debate_system_redesign_v1.md Part 6 (compiled) | last_updated: 2026-04-02 -->
<!-- PATCHES APPLIED: D-01–D-10, R-01–R-07, v2-P01–v2-P04, R-65, R-66 -->
<!-- POOL FORMULA CONFIRMED: (Presence × 2) + History bonus, TN 7 -->
<!-- SIM-DEBT-01: All stress-test calibration used Cognition+History pool. Re-simulation needed with Presence×2 before values are final. -->
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

<!-- patch_history: references/params_debate_history.md -->
<!-- canonical_sources: references/canonical_sources.yaml -->
