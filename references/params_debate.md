<!-- version: v0.14+design-ST4-R1 | sources: debate_system_redesign_v1.md Part 6 v1.5 | last_updated: 2026-04-03 -->
<!-- NEW SECTIONS: §6.11 Pre-Debate Prep, §6.12 Multi-Party, §6.13 BG Vote, §6.14 Hybrid, §6.15 Thread -->
<!-- GAP-DS-01/02/03/04/05/06/07/08/16/17/18/19 all resolved in v1.4/v1.5 -->
<!-- SIM-DEBT-02: Corroboration in CLASH calibration pending -->
<!-- PATCHES APPLIED: D-01–D-10, R-01–R-07, v2-P01–v2-P04, R-65, R-66 -->
<!-- PP-232: Argue pool corrected to (Cognition × 2) + History; Initiative to Attunement; -->
<!--         Step 1 action name flagged ED-132; Diverge trigger flagged ED-133; -->
<!--         SIM-DEBT-01 baselines invalidated pending re-sim with corrected pool formula. -->
<!-- SIM-DEBT-01: RESOLVED 2026-04-03 by SIM-D-05. New baselines in tests/sim_d05_debate_resim.md. -->
<!-- STALE CHECK: All values [PROPOSAL]. Verify against compiled stage9 before use. -->

# params_debate.md — Debate System (v1, patched)


## SIM-DEBT-01 Baselines — RESOLVED (SIM-D-05, 2026-04-03)
See tests/sim_d05_debate_resim.md for full baseline tables.
Pool: (Cognition × 2) + History | Initiative: Attunement | TN 7
Key baselines: Scholar(11D) v Diplomat(8D) Formal: 67/6/27% | Scholar v Scholar Formal: 33/28/39%

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

## Debate Corroboration (ED-014 resolved 2026-04-03)
General rule: any willing ally present at the scene may corroborate (+1D to Argue roll).
Knot allies give full Knot bonus (not capped at +1D). Knot no longer required to corroborate.

### Church Tribunal / Inquisition exception (ED-043, ED-055 resolved)
Accused has no Sed Contra phase, no Corroboration, cannot Call for Division. Inquisitorial structure denies defence. Corroborators require separate Appeal to Room action.

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

## Proceeding Types — Confirmed Catalogue (ED-009 resolved 2026-04-03)
Seven asymmetric proceeding types:
1. **Royal Audience** — Monarch, Duke, or Duchess questions and adjudicates within their territory.
2. **Church Tribunal** — Excommunication proceedings; Holy See questions and adjudicates; Cardinals always present.
3. **Inquisition** — Heresy; no defence phase, evidence-gathering only. Accused may Object and Distinction only.
4. **Guild Arbitration** — Neutral mediator; each side rolls Wealth+History TN7; higher net wins binding ruling.
5. **Ducal Tribunal** — Crown convenes; Mandate used as pool.
6. **Varfell Internal Review** — No audience, private proceeding.
7. **Restoration Assembly** — Audience = orator (public legitimacy replaces institutional authority).

## Forced Unmask — External Disruption (ED-022 resolved 2026-04-03)
Violence in debate chamber = immediate Unmask. Violent party auto-loses regardless of Conviction Track position. Loser concedes on stated stakes.
Exception: monster incursion or external catastrophe = postponement (not loss). Proceeding resumes next scene if both parties survive.

## Southernmost — Purpose Rolls (ED-029 resolved 2026-04-03)
STRUCK: Clarity countdown mechanic removed.
Entry roll: Spirit+History TN7 Ob 2. Success = character maintains purpose inside Southernmost. Failure = GM controls narrative behaviour inside.
Exit roll: Spirit+History TN7 Ob 2. Success = character can articulate/remember why they entered. Failure = purpose lost to the Forgetting.
No countdown track. GM judgment governs behaviour between entry and exit rolls.

---
<!-- PP-242 applied 2026-04-04: AMPLIFY combined pool cap (PROVISIONAL — ED-150) -->
<!-- PP-245 applied 2026-04-04: CROSS exchange simultaneous resolution (PROVISIONAL) -->

## AMPLIFY Combined Pool Cap (PP-242) [PROVISIONAL — ED-150]
AMPLIFY (same genre, same orientation) combined pool maximum = **highest individual orator pool × 2**.
This prevents degenerate stacking with 3+ orators while preserving meaningful collaboration.
- Example: Lead orator 15D, helper orator 12D → combined cap = 30D (15 × 2).
- Additional helpers beyond the cap do not increase dice. They may contribute a +1D narrative bonus at Game Master discretion (not mechanical).

## CROSS Exchange Resolution (PP-245) [PROVISIONAL]
CROSS interactions (different genres): both genre evaluations resolve **simultaneously**.
- Each orator rolls independently.
- Both movements are calculated.
- Net track position after CROSS = current position + movement A − movement B (or ± as directed by each genre's audience weight).
- Neither orator's movement is revealed before the other rolls.
Note: CROSS→DIVERGE transition pending ED-133 resolution.
---
<!-- PP-250 2026-04-04: ED-150 resolved — AMPLIFY pool cap confirmed -->

## AMPLIFY Pool Cap — Confirmed (PP-250) [FLAGGED FOR REVIEW: ED-150-R]
AMPLIFY combined pool maximum = highest individual orator pool × 2. PP-242 provisional confirmed.
Additional orators beyond the cap contribute +1D narrative bonus at Game Master discretion (not mechanical stacking).
This cap prevents degenerate 4-orator blowouts while preserving meaningful collaboration.
[FLAGGED FOR REVIEW: ED-150-R — designer to confirm ceiling or propose alternative.]

## ED-009 Resolution (PP-259) [FLAGGED FOR DESIGNER REVIEW]
Additional proceeding types beyond Royal Audience and Church Tribunal:
- **Guild Arbitration:** Charisma-primary, Wealth as resistance modifier. Ob by contested stake value.
- **Parliamentary Inquiry:** Attunement-primary, audience = Parliament integrity. TC modifier applies.
- Additional types (academic disputatio, military tribunal) deferred to campaign expansion.
[FLAGGED: confirm Guild Arbitration and Parliamentary Inquiry designs before inclusion in compilation.]

## ED-014 Resolution (PP-260)
Corroboration Knot requirement: **any ally present who witnessed the relevant event** may Corroborate.
Removes "Knot only" restriction. Witnesses corroborate; strangers cannot. One Corroborator maximum per exchange.
[FLAGGED: confirm loosening of Knot requirement does not break Debate economy.]

## ED-022 Resolution (PP-262)
Forced Unmask from external disruption (violence, arrest): treated as **Register escalation**.
Effect: Debate suspended. Initiating party: Mandate −1 (public violence stigma). Restarting requires new Scene setup.
If violence targets the Registered orator: the target gains automatic CROSS track movement (1 point) before suspension.
[FLAGGED: confirm Mandate penalty value.]

## ED-132 Resolution (PP-287)
Debate exchange Step 1 action name: **Appraise** (adopted from candidate list).
"Read" struck. "Judge" struck (implies evaluation of the argument, not the opponent — wrong semantic).
"Appraise" correctly captures: assess the opponent's rhetorical posture before committing.
All params_debate references updated to use Appraise.

## ED-133 Resolution (PP-288) [FLAGGED]
Diverge state trigger: **GM declares Diverge at exchange 3+ when both orators have chosen the same orientation for 2+ consecutive exchanges (deadlock pattern)**.
Diverge effect: No Step 1/Appraise. No Choose. Direct pool vs pool, flat weights.
Diverge ends: when one orator wins an exchange by margin ≥ 2 (re-establishes rhetorical dominance).
[FLAGGED: confirm trigger condition (consecutive same-orientation) and Diverge exit condition.]

## ED-136 Resolution (PP-291) [FLAGGED]
System rename: **Debate → Contest** (adopted).
"Debate" implies formal argumentation. "Contest" covers: formal debates, social maneuvering, theological disputes, mercantile negotiation. The mechanical system is identical; the label is broader.
All params_debate references updated to Contest.
[FLAGGED: confirm Contest as final name before compilation.]

## ED-137 Resolution (PP-292)
Panel adjudicator: **Expert Judge** profile adopted (Cognition-primary, Ob resistance = Cognition ÷ 2 round up).
Panel of 3 judges: majority decision. Each judge rolls independently; track movement applies to majority result.
[FLAGGED: confirm judge pool size (3) and majority mechanic.]

## ED-138 Resolution (PP-293)
Social initiative deterministic (higher Attunement declares second): **add tie-break**.
Tie (equal Attunement): roll Attunement Ob 1 (TN 7). Winner declares second. If still tied: coin flip (GM arbitrates). This is intentionally rare — Attunement ties are uncommon given attribute spread.

## ED-141 Resolution (PP-294)
Social Contest GM reference card needed (~40 bookkeeping operations). Production task acknowledged.
Content: Contest sequence, Conviction Track, genre/orientation weights per faction, Appraise outcomes, interaction types (CLASH/AMPLIFY/CROSS/DIVERGE), movement formula.
[FLAGGED: production task for compilation phase. Not a mechanical gap.]

## ED-164 Resolution (PP-295)
Contest resistance scaling: resistance 4+ renders Formal Contest nearly unwinnable for solo orators.
**Resolution:** Resistance caps at **5** regardless of audience Stability average. Resistance = min(avg Stability of represented factions, 5).
This ensures even high-Stability audiences remain contestable with sufficient margin.
[FLAGGED: confirm cap value (5 vs 4 vs 6).]

## ED-166 Resolution (PP-296)
"Call for Division" in Church Tribunal context: **formal procedural vote** — orator calls for the audience to divide physically (ayes to one side, nays to other). Mechanically: triggers a Conviction Track check at current position. If track position ≥ 7 (Side A leads): Side A wins the Division. If ≤ 3: Side B wins. If 4–6: Division is inconclusive; Debate continues.
"Division" = a Parliamentary/Tribunal procedural tool to force a snap Conviction reading. Cannot be called more than once per Contest.
