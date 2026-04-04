<!-- version: v0.14+design-ST4-R1 | sources: debate_system_redesign_v1.md Part 6 v1.5 | last_updated: 2026-04-03 -->
<!-- NEW SECTIONS: §6.11 Pre-Debate Prep, §6.12 Multi-Party, §6.13 BG Vote, §6.14 Hybrid, §6.15 Thread -->
<!-- GAP-DS-01/02/03/04/05/06/07/08/16/17/18/19 all resolved in v1.4/v1.5 -->
<!-- SIM-DEBT-02: Corroboration in CLASH calibration pending -->
<!-- PATCHES APPLIED: D-01–D-10, R-01–R-07, v2-P01–v2-P04, R-65, R-66 -->
<!-- PP-232: Argue pool corrected to (Cognition × 2) + History; Initiative to Attunement; -->
<!--         Step 1 action name flagged ED-132; Diverge trigger flagged ED-133; -->
<!--         SIM-DEBT-01 baselines invalidated pending re-sim with corrected pool formula. -->
<!-- SIM-DEBT-01: INVALIDATED by PP-232 pool correction. All baselines below are STALE. Re-sim required. -->
<!-- STALE CHECK: All values [PROPOSAL]. Verify against compiled stage9 before use. -->

# params_debate.md — Debate System (v1, patched)


## SIM-DEBT-01 Baselines — INVALIDATED (PP-232)
**All prior baselines (Pres 3 + Hist 2 = 8D etc.) are INVALID.** Pool formula was wrong.
Correct pool = (Cognition × 2) + History. Re-simulation required before these values are usable.

## Pools
| Roll | Pool | TN | Notes |
|------|------|----|-------|
| Argue | (Cognition × 2) + History bonus | 7 | Main contest roll. (PP-232) |
| Step 1 Appraise | Attunement only (no History) | 7 Ob 1 | Per exchange, before Choose. Action name [EDITORIAL: ED-132]. |
| Memory bonus | +2D | — | When citing specific named verifiable claim. Binary. Any genre. |

## Initiative
Exchange 1: higher **Attunement** acts last (has most information; declares second). (PP-232)
Subsequent: transfers to exchange winner. Tie: stays with holder; no damage to either side. (PP-232)
Post-Diverge state: stays with holder.

## Exchange Structure
**Step 1 — [EDITORIAL: ED-132 — action name: "Read" disputed; candidates include Appraise, Judge]**
(both orators, Attunement, TN7 Ob1):
| Net | Information |
|-----|-------------|
| Failure | Misleading signal: one weak genre identified as strong |
| Partial (1) | Primary genre identified only |
| Success (2) | Primary genre + orientation preference |
| Overwhelming (3+) | Genre + orientation + one specific detail |

**Step 2 — Choose:** Each orator selects Genre (Past/Present/Future) + Orientation (Revealing/Obscuring).

**Step 3 — Argue:** Lower Attunement (lower initiative) declares first. Higher Attunement hears, then declares and rolls. (PP-232)

**Step 4 — Resolve** (by interaction type):

| Interaction | Condition | Resolution |
|-------------|-----------|-----------|
| CLASH | Same genre, opposite orientation | Compare successes. Margin = difference. Apply movement formula. |
| AMPLIFY | Same genre, same orientation | Combined pools vs Conviction Track resistance. |
| CROSS | Different genres | Each evaluated independently. |
| DIVERGE | Post-Diverge state | No Step 1/Choose. Direct pool vs pool, flat orientation weights. [EDITORIAL: ED-133] |

## Conviction Track
Range: 0–10. Side A wins ≥ 7. Side B wins ≤ 3. Compromise zone: 4–6.
Starting position: Game Master-set, typically 4–6 neutral.
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
| Guilds (Moral Relativism) | Game Master picks |
| Restoration (Rawlsian Social Contract) | Future |

Weight range: 0.5–1.5. Never 0, never above 1.5. Fixed at setup.

## Orientation Weights
Revealing: ×1.0 | Obscuring: ×0.75 (invertible for specific scenarios).
Fixed at setup; recorded in ledger.

## Composure
[EDITORIAL: ED-127 — Composure to mirror Health/Wound structure with Rattled as wound-equivalent threshold. Formula and track pending design decision.]
Recovery: Reframe action (costs initiative; Cognition Ob 2 — [EDITORIAL: ED-127]).
Concession: voluntary, or forced at Composure 0.

## Diverge State
[EDITORIAL: ED-133 — Diverge trigger and justification need design rationale. Current trigger (GM discretion at margin threshold) is disputed. Full design required before this state is treated as final.]
Effect pending ED-133 resolution: No Step 1, no genre choice. Orientation weights flatten. Initiative stays with holder.
Ends: when Conviction Track exits compromise zone or Composure concession fires.

## Multi-Party Debates
[GAP: multi-party procedure not yet defined — design_v1.md F-5 identifies this as a structural gap.]

## Composure Restoration (ED-060 resolved — provisional)
Full Composure restores at scene end. Between-session: full restore. No partial recovery mechanic. [PROVISIONAL]

## Momentum in Debate (ED-059 resolved — provisional)
Momentum may be spent in Debate rolls (1 Momentum = 1 automatic success, reduces effective Ob by 1). Applies to Argue and Step 1 rolls. Does not apply to Coherence Retention rolls. [PROVISIONAL]

## Genre Pivot Mid-Debate (ED-045 resolved — provisional)
An orator may pivot their primary genre once per debate (not per exchange). Costs Concentration −1 extra on the exchange of the pivot. Must be declared during Choose step. [PROVISIONAL]

## Grand Debate Role Alternation (ED-042 resolved — provisional)
Proposer role alternates per exchange. First proposer: higher Attunement (ties: initiative holder). Alternation is independent of initiative transfer. [PROVISIONAL — PP-100 applies to §6.7 separately; PP-232 corrects Attunement as initiative stat]

## Niflhel Social Toolkit (ED-041 resolved — provisional)
Niflhel cannot participate in Formal or Grand Debates. Their social toolkit:
- Private Negotiation: one-on-one only; uses Cognition + History, TN 7, Ob = target's Stability.
- Bribery: spend 1 Wealth token; target takes −1 Ob on next roll toward Niflhel interests.
- Thread Insight (TS≥30 only): Attunement Step 1 before negotiation; reveals one unstated position.
[PROVISIONAL — ED-041]

## Poise Attribute (ED-027 resolved — provisional)
'Poise' is deprecated. All references to Poise in debate mechanics use Composure. [PROVISIONAL — ED-127 governs Composure formula]

## NPC Composure Formula (ED-052 resolved — provisional)
[PROVISIONAL — pending ED-127 Composure redesign.]

## Debate Corroboration — Asymmetric Proceedings (ED-055b resolved — provisional)
Accused in Church Tribunal (Inquisitorial proceeding) may not have corroborators. Accused may only: Object (Phase 2) and Distinction (Phase 5). [PROVISIONAL]

## Evidence Leverage Audience Mode Shift — Cap (PP-183)
Audience ethical mode weight shifts capped at weight 2.0. Multiple leverage attempts do not stack. [PP-183]

<!-- patch_history: references/params_debate_history.md -->
<!-- canonical_sources: references/canonical_sources.yaml -->

## Confirmed Debate Mechanics (PP-203)

### Dual Win-Conditions (ED-012 resolved)
1. Exchange majority: win more exchanges than opponent.
2. Audience capture: end Debate with audience Friendly AND opponent Hostile or worse.
Outcomes: Procedural victory / Popular victory / Total victory.
Domain Echo fires from audience response when Popular or Total victory.

### Church Tribunal Corroboration (ED-043 resolved)
Accused has no Sed Contra phase, no Corroboration, cannot Call for Division. Tribunal = doctrinal enforcement, not justice.

### Debate End Conditions (ED-058 resolved)
End triggers: exchange limit reached (Inquisitor sets 1–5; Formal/Grand minimum 3).
Stalemate (tied exchanges at limit): Proposer loses — burden of proof not met.

### Hybrid Debate (ED-057a resolved)
Resolved in debate_system_redesign_v1 §6.14.
