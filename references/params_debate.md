<!-- version: v0.14+design-ST4 | sources: debate_system_redesign_v1.md Part 6 v1.5 | last_updated: 2026-04-02 -->
<!-- NEW SECTIONS: §6.11 Pre-Debate Prep, §6.12 Multi-Party, §6.13 BG Vote, §6.14 Hybrid, §6.15 Thread -->
<!-- GAP-DS-01/02/03/04/05/06/07/08/16/17/18/19 all resolved in v1.4/v1.5 -->
<!-- SIM-DEBT-02: Corroboration in CLASH calibration pending -->
<!-- PATCHES APPLIED: D-01–D-10, R-01–R-07, v2-P01–v2-P04, R-65, R-66 -->
<!-- POOL FORMULA CONFIRMED: (Presence × 2) + History bonus, TN 7 -->
<!-- SIM-DEBT-01: PARTIALLY RESOLVED. Modes A+D complete (SIM-D-01 2026-04-02). New baselines below. Mode C still needed. -->
<!-- PP-097 PROVISIONAL: DIVERGE+TIE → Tie rule fires. -->
<!-- PP-098 PROVISIONAL: Regroup at Concentration=0 → consumes Spent without penalty. -->
<!-- PP-099 PROVISIONAL: Obscuring in Divergence → Doubt Marker; orientation_weight=1.0 for calc. -->
<!-- stage9_social.md is EMPTY in v0.14. All values from design proposals. -->
<!-- STALE CHECK: All values [PROPOSAL]. Verify against compiled stage9 before use. -->

# params_debate.md — Debate System (v1, patched)


## SIM-DEBT-01 Recalibrated Baselines (SIM-D-01)
**All prior v1+v2 strain/Composure values are INVALID.** Use values below.

| Value | Old (INVALID) | New baseline |
|-------|--------------|-------------- |
| Typical pool (Pres 3, Hist 2) | 5D | 8D |
| E[winning margin, symmetric] | ~1.6 | ~2.0 |
| P(Overwhelming) symmetric | ~25% | ~60% |
| Typical strain/exchange (CLASH, Pres 3 winner, Focus 2 loser) | 1-2 | 2-3 |
| Exchanges to Rattled (Composure 9) | 7-9 | 3-5 |
| Exchanges to Rattled (Composure 7) | 5-7 | 2-4 |
| Track movement/exchange (primary genre, res=1) | 0 (often) | 1 (consistent) |
| Concentration durability (Conc=6, 50% loss rate) | — | ~4 exchanges |

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
[GAP: exact Composure formula not finalised — attribute mapping pending. From design intent:]
Pool likely: Endurance + Poise or Presence.
Rattled threshold: Composure ≤ 2 → −2D all Argue rolls.
Recovery: Reframe action (costs initiative; Ob 2 Cognition check).
Concession: voluntary, or forced at Composure 0.

## Diverge State
Triggered when: margin threshold met but Conviction Track still in compromise zone after N exchanges (Game Master discretion).
Effect: No Read, no genre choice. Orientation weights flatten. Initiative stays with holder.
Ends: when Conviction exits compromise zone or Composure concession fires.

## Multi-Party Debates
[GAP: multi-party procedure not yet defined — design_v1.md F-5 identifies this as a structural gap.]

## Composure Restoration (ED-060 resolved — provisional)
Full Composure restores at scene end. Between-session: full restore. No partial recovery mechanic. [PROVISIONAL]

## Momentum in Debate (ED-059 resolved — provisional)
Momentum may be spent in Debate rolls (1 Momentum = 1 automatic success, reduces effective Ob by 1). Applies to Argue and Read rolls. Does not apply to Coherence Retention rolls. [PROVISIONAL]

## Genre Pivot Mid-Debate (ED-045 resolved — provisional)
An orator may pivot their primary genre once per debate (not per exchange). Costs Concentration −1 extra on the exchange of the pivot. Must be declared during Choose step. [PROVISIONAL]

## Grand Debate Role Alternation (ED-042 resolved — provisional)
Proposer role alternates per exchange. First proposer: higher Presence (ties: initiative holder). Alternation is independent of initiative transfer. [PROVISIONAL — PP-100 applies to §6.7 separately]

## Niflhel Social Toolkit (ED-041 resolved — provisional)
Niflhel cannot participate in Formal or Grand Debates. Their social toolkit:
- Private Negotiation: one-on-one only; uses Cognition + History, TN 7, Ob = target's Stability.
- Bribery: spend 1 Wealth token; target takes −1 Ob on next roll toward Niflhel interests.
- Thread Insight (TS≥30 only): Attunement Read before negotiation; reveals one unstated position.
[PROVISIONAL — ED-041]

## Poise Attribute (ED-027 resolved — provisional)
'Poise' is deprecated. All references to Poise in debate mechanics use Composure (derived: Presence + 4, range 5–11). [PROVISIONAL]

## NPC Composure Formula (ED-052 resolved — provisional)
NPC Composure = Presence + 4. Prior shorthand "Presence + 6" is superseded. [PROVISIONAL]

## Debate Corroboration — Asymmetric Proceedings (ED-055b resolved — provisional)
Accused in Church Tribunal (Inquisitorial proceeding) may not have corroborators. The Inquisitor controls the proceeding structure. Accused may only: Object (Phase 2) and Distinction (Phase 5). [PROVISIONAL — consistent with §6.7]

## Evidence Leverage Audience Mode Shift — Cap (PP-183)

Audience ethical mode weight shifts from evidence leverage (ED-077: Cognition+History Ob2 to shift audience genre preference) are capped at weight 2.0. Subsequent successful leverage rolls in the same debate do not push the weight above 2.0. Multiple leverage attempts do not stack. [PP-183]

<!-- patch_history: references/params_debate_history.md -->
<!-- canonical_sources: references/canonical_sources.yaml -->
