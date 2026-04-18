# SIM-SPOILER-BG-01 — Board Game Spoiler Faction Simulation
## Date: 2026-04-07 | Mode: C (Full Scenario) + G-BG + J (Precedent) + L (Cognitive Load)
## Scenario: 4-player game — Crown (winning), Church (spoiling Crown), Hafenmark, Varfell

---

## FETCH LOG
canonical_sources.yaml: ✓ fetched (156 lines)
references/params_board_game.md: ✓ fetched (1068 lines)
references/params_factions.md: ✓ fetched (480 lines)
designs/board_game/victory_architecture_v1.md: ✓ fetched (368 lines)

---

## Setup

**4 players:** Crown, Church of Solmund (spoiler), Hafenmark, Varfell.
**Spoiler faction:** Church of Solmund — primary goal is NOT to win; goal is to prevent Crown from achieving Peninsula Sovereignty.

**Crown victory requirements (§3.1):** TCV ≥ 16, all rivals Mandate ≤ 2 OR eliminated OR formal Treaty, IP < 60, PI ≥ 3.

**Why Church is the natural Crown spoiler:**
Crown's rival suppression condition requires Church Mandate ≤ 2 OR eliminated OR formal Treaty. Church holding Mandate ≥ 3 indefinitely blocks Crown victory. The Church player does not need to win — they simply need to avoid being suppressed. This is asymmetric: Crown must actively reduce Church Mandate; Church must passively sustain it.

**Starting State:**
| Faction | Mandate | Influence | Wealth | Military | Stability | TCV |
|---------|---------|-----------|--------|----------|-----------|-----|
| Crown | 5 | 5 | 4 | 4 | 4 | 12 |
| Church | 5 | 6 | 5 | 4 | 5 | 3 |
| Hafenmark | 4 | 4 | 5 | 3 | 4 | 8 |
| Varfell | 4 | 4 | 4 | 4 | 4 | 6 |

TC: 28. RS: 72. IP: 20. PI: 7.

---

## Scenario: Church Spoiling Crown

### Season 1 — Church identifies Crown as threat

**Crown actions:** Royal Charter in T5 (Feldmark, TCV 1) + Govern T1 (Valorsplatz) — building toward TCV dominance. No immediate move against Church.

**Church spoiler actions:**
Church does NOT play Assert (would advance TC — spoiler doesn't need TC). Instead:
1. **Cardinal Focus: Justice** (Phase 1 declarative, no cost). PP-430: AP threshold for first Inquisitor −1 this season. First Inquisitor at AP ≥ 2.
2. **Active Inquisition** (Senator Inward, PP-429) in T2 (Kronmark, Crown territory adjacent to Crown capital). Roll: Mandate 5D vs Ob = T2 Stability ÷ 2 = 4 ÷ 2 = 2. P(OW): ~69%. P(Succ): ~22%. P(Fail): ~9%.
   - **Result: Overwhelming.** AP +3. With Justice Focus: first Inquisitor at AP ≥ 2 — threshold exceeded. Inquisitor deployed to T2 (Kronmark). AP = 3, threshold clears, pool resets to 3 (remaining above threshold after first Inquisitor deployment? See Attention Pool rule: pool resets to 0 at Accounting Step 5 after threshold responses fire. Inquisitor deploys and AP resets.)
3. **Piety Spread** (Consul Inward, PP-428) in T9 (Himmelenger, Church controlled, CV 5 already). Ob = controlling faction Mandate ÷ 2 + Fort 2, min 1 = 5÷2 + 2 = 4.5 → 5. But Church controls T9 — are they targeting their own territory? Piety Spread targets territory to raise CV. If Church is the controller, Ob = Church Mandate ÷ 2 + Fort level. But CV in Church's own territory is already 5 (at cap). **Ruling: Piety Spread cannot exceed CV 5. Redirect to adjacent Crown territory T2 (Kronmark, CV 2).** Ob = Crown Mandate ÷ 2 + Fort 1 = 2.5 + 1 = 3.5 → 4. Doctrine-aligned −1 Ob → Ob 3. Roll: Mandate 5D vs Ob 3. P(Succ): ~68%.
   - **Result: Success.** T2 Kronmark CV +1 → CV 3. (CV 3 = Church seizure Ob lower in this territory if TC ever hits 75.)

**Accounting Step 5:** TC passive +1 → TC 29. Inquisitor in T2 (Kronmark): Intel/Investigate in T2 now +2 Ob.

**State after S1:**
Crown TCV 12 (unchanged — Charter placed but no territory gained). Church TCV 3. TC 29. Inquisitor in T2 Kronmark.

---

### Season 2 — Crown attempts to suppress Church; Church escalates spoiling

**Crown actions:**
1. **Royal Decree** (Mandate vs Ob 2) targeting Church: Church Mandate −1. Roll: 5D vs Ob 2. P(Succ): ~91%.
   - **Result: Success.** Church Mandate 5 → 4. Consecutive Decree: next season Ob 3.
2. **March to T9 (Himmelenger)** — contested entry triggers Battle. Crown Military 4D vs Church Military 4D.
   - But Church has Fort 2 in T9: Church rolls Military 4 + 2 Fort dice = 6D. Crown 4D.
   - Expected: Church wins ~62% of battles (6D vs 4D at TN 7). 
   - **Result: Crown Partial victory** — fails to take T9 (draws), Crown Military −1 (attrition). Crown Military 4 → 3.

**Church spoiler actions (Church Mandate now 4):**
1. **Institutional Mandate trigger:** Crown's March to T9 directly challenges Church core institutional authority. Church Mandate ≥ 4 → Uphold/Appease trigger. Church chooses **Uphold** (battle proceeds normally — Church wants to fight for T9, not avoid the confrontation).
2. **Excommunication** (Senator Outward, Unique Power) targeting Crown leader (Almud). Roll: Mandate 4D vs Crown Mandate 5 (leader) → Ob 5. At Mandate 4, pool 4D vs Ob 5: P(Succ) ≈ 2%. High-risk play.
   - **Result: Failure.** No effect. Church considered overreach — Church Stability −1 → 4 (PP-403 Failed Domain Action).
   
   **Reassessment:** Church player reconsiders Excommunication (too risky at this Mandate level). Church pivots to:
3. **Active Inquisition** in T14 (Ehrenfeld, Crown, Crown Military heartland). Ob = T14 Stability ÷ 2 = 4 ÷ 2 = 2. Roll: Mandate 4D vs Ob 2. P(Succ+OW): ~85%.
   - **Result: Overwhelming.** AP +3. Second Inquisitor at AP ≥ 6 (ED-322: first at AP ≥ 3). Running AP = 3 → threshold fires → first Inquisitor deploys in T14. AP resets to 0.
4. **Cardinal Focus: Fortitude** this season? Already used Justice in S1. PP-430: designation is once per season declarative. For S2, Church declared no Focus before Inquisition (error — Focus is Phase 1). Retroactive Focus invalid. Inquisitor deploys normally in T14.

**Accounting Step 5:** TC passive +1 → TC 30. Two Inquisitors now active: T2 Kronmark (+2 Ob all Intel there), T14 Ehrenfeld (+2 Ob all Intel there). Crown's military and administrative heartland both infected with Heresy Investigation threat.

**Effect on Crown:** Crown cannot easily use Tribune Investigate in T2 or T14. Varfell Intel actions also blocked in those territories (+2 Ob). Varfell player is collateral damage from Church spoiling.

**State after S2:**
| Faction | Mandate | TCV | Notes |
|---------|---------|-----|-------|
| Crown | 5 | 12 | Military 3 (attrition). Royal Decree consecutive Ob 3 next. |
| Church | 4 | 3 | Stability 4. 2 Inquisitors active (T2, T14). |
| Hafenmark | 4 | 8 | — |
| Varfell | 4 | 6 | T2+T14 Intel blocked. |
TC: 30. Inquisitors: T2, T14.

---

### Season 3 — Church spoiler reaches stable equilibrium

**Church spoiler equilibrium strategy:**
Church does not need TC advance (spoiler). Each season:
- Maintain Mandate ≥ 3 (blocks Crown victory condition indefinitely)
- Deploy Inquisitors to Crown's best territories (AP generation via Active Inquisition)
- Use Piety Spread to raise CV in Crown territories (raises Church seizure readiness if needed later, and provides +1 TC from Conviction Yield at Accounting — but Church spoiler can ignore TC; they just bank it passively)
- Never play Assert (TC advance unnecessary for spoiler)
- Never play Excommunication (too risky at reduced Mandate)

**Crown's response options:**
Crown must get Church Mandate ≤ 2. Options:
1. Royal Decree (consecutive, Ob 3 this season): Church Mandate 4 → 3. P(Succ at 5D vs Ob 3): ~69%.
2. Excommunicate Church (Crown can't — Excommunication is a Church unique action).
3. Military seizure of T9 (Himmelenger): if Crown controls T9, Church loses home territory CV bonus, loses TC +1/season from T9 control. But Fort 2 + Church Military.
4. Formal Crown Treaty offer: if Church accepts, they're Treaty-locked out of Church's core play. Church would need Mandate −1, Stability +1 in exchange. **Church refusing is rational for a spoiler** — Treaty means Crown can count them as "suppressed" for the victory condition if at Mandate ≤ 2.

**Optimal Crown response is Royal Decree chain (Consecutive Ob 3 this season, Ob 4 next):**
Season 3: Decree at Ob 3. 5D vs Ob 3: P(Succ): ~69%. Expected: Church M 4 → 3.
Season 4: Decree at Ob 4. 5D vs Ob 4: P(Succ): ~42%. Expected: Church M 3 → 2 on success.
Season 4 alternative: if Decree hits Failure (31% chance), Church Mandate stays ≥ 3. Crown must wait or pivot.

**Church spoiler counter to Decree chain:**
When Church Mandate ≥ 4 AND Crown Decree directly challenges Church institutional authority → Institutional Mandate trigger: Church **Uphold** (Decree fires normally) or **Appease** (Decree cancelled, Church Mandate −1). 

**Key insight:** If Church Appease at M ≥ 4, Crown loses their Decree (action cancelled) but Church Mandate drops by 1 anyway. Church is voluntarily shrinking their own Mandate to prevent Crown from getting the Decree effect AND the TCV/PI benefit from the roll. If Church Appease at M = 4 → M 3: Crown doesn't get Decree success (no effect), Church Mandate is now 3 — close to the Crown victory threshold. Church should only Appease if the alternative (a successful Decree) would reduce Mandate further (net same result, Crown gets roll upside).

**Ruling clarity needed:** Does Royal Decree "directly challenge Church core institutional authority"? Decree is targeting Church Mandate (faction stat). The Institutional Mandate trigger fires when "Domain Action directly challenges faction core institutional authority AND targeted faction Mandate ≥ 4." Royal Decree targeting Church Mandate: YES, this directly challenges Church authority. Trigger fires.

**Church player choice (S3):**
Church Mandate 4. Crown Decree fires (Phase 4 Priority 6: Special/Unique Powers). Church Institutional Mandate trigger: Uphold or Appease?
- Uphold: Decree rolls. P(Success at 5D vs Ob 3) = ~69%. Expected Church M drop: −0.69 per season.
- Appease: Mandate −1 immediately. Church M 4 → 3. No roll.

**Both paths lead to Church Mandate 3 within ~1.5 seasons.** Church cannot sustain Mandate ≥ 3 against Crown Decree chain unless:
- Mandate recovers from other sources (no easy recovery mechanic for Church from external action)
- Church eliminates or incapacitates Crown (difficult)
- Church hits Mandate 3 and Crown Decree goes to Ob 4 (only 42% success — Church may stabilise at 3 via Failure luck)

**Finding P1 — Spoiler sustainability gap:**
A Church spoiler can delay Crown victory for 3–6 seasons but cannot indefinitely block it if Crown invests Decree chain. At Mandate 3, Crown's Decree (Ob 4) hits ~42% success, meaning ~1/2.4 seasons Church drops to Mandate 2. Once at Mandate 2, Crown victory condition is met for Church column. The spoiler window is 5–8 seasons, not permanent.

**Finding P2 — Inquisitor collateral:**
Inquisitors deployed to Crown territories are permanent until removed (requires Riskbreaker action or territory control change). They impose +2 Ob on ALL Intel actions there — including Varfell. The spoiler creates indirect friction for non-target factions, complicating the game state for all players at no additional cost to Church.

**Finding P3 — TC passive accumulation during spoiling:**
Church spoiler never plays Assert. TC advances at +1/season baseline (passive). With Hafenmark structural suppression (if Mandate ≥ 4), TC advances at 0/season. But spoiler doesn't care about TC — they're not trying to reach TC 75. TC rising is a side effect that benefits no one if Church is spoiling. By S8–10, TC may reach 50–55 regardless, triggering Church Partition Victory conditions (TC ≥ 50 + Church controls ≥ 2 territories + Hafenmark controls ≥ 3 + no Church/Hafenmark military conflict). Church spoiler accidentally achieves co-victory conditions if the game drags.

**Finding P4 — Spoiler exit condition:**
When Crown suppresses Church Mandate to ≤ 2: Church is excluded from Crown's victory condition. At this point Church can no longer spoil by Mandate maintenance. Church shifts to: CV suppression in Crown territories (lower CV = Church seizure bonus if TC reaches 75 later), or military harassment of Crown border territories. But at Mandate ≤ 2, Church's action economy is severely reduced (Ob penalties from low Mandate on Church-type actions? Check: Church Mandate is a pool stat, low Mandate = smaller dice pool. Church Active Inquisition at Mandate 2 = 2D vs Ob 2 → P(Succ): ~36%. Church becomes effectively passive at Mandate 2.)

---

## Mode J: Precedent Check

**Does spoiler strategy require undefined rules?** No new rules needed. All spoiler actions use existing mechanics:
- Institutional Mandate Uphold/Appease: defined (PP-189)
- Royal Decree Ob consecutive: defined (PP-168)
- Active Inquisition: PP-429 (proposed, not yet applied to doc — but mechanics are complete)
- Inquisitor +2 Ob on Intel: defined in Standard Action Ob table

**Ambiguity found — Institutional Mandate trigger scope:**
The trigger is "Domain Action directly challenges faction core institutional authority." Royal Decree targeting Church Mandate: confirmed as triggering. But what about Royal Decree targeting Church Stability? Or Influence? Is it only Mandate that triggers Institutional Mandate? Recommend clarification: Institutional Mandate trigger fires when a Domain Action targets the faction's Mandate stat specifically OR directly attacks their unique mechanic (TC for Church, PI for Hafenmark, VTM for Varfell). Stability, Influence, Wealth, Military do not trigger.

**[EDITORIAL: ED-324 — Institutional Mandate trigger: confirm whether target stat (Mandate only) or any stat with authority-challenging framing triggers it. Flag for designer.]**

---

## Mode L: Cognitive Load Assessment

**Church spoiler cognitive requirements:**
1. Track Mandate threshold (must stay ≥ 3)
2. Track AP and Inquisitor deployments (2 simultaneous Inquisitors = 2 territory markers)
3. Track Consecutive Decree Ob (1 counter on Crown mat)
4. Decide each season: Uphold or Appease on Decree trigger

**Load rating: Medium.** The spoiler strategy has 4 active variables. No new tracking required beyond standard faction mats. Inquisitor territory markers are physical tokens, visible to all. The Uphold/Appease decision is binary. Load is appropriate for a player comfortable with the system.

**Friction point:** Tracking whether Institutional Mandate trigger fires — requires other players to know the threshold (Church Mandate ≥ 4) and the current Mandate value. Both are public stats. No hidden information required. **Load: acceptable.**

---

## Simulation Verdict

**Board Game Spoiler (Church spoiling Crown): FUNCTIONAL with caveats.**

The spoiler role is viable but time-limited. Church can delay Crown victory for 5–8 seasons using Mandate maintenance + Inquisitor deployment. Crown has reliable counter-play (Decree chain). The spoiler creates interesting collateral effects (Varfell Intel blocked, TC passive accumulation, accidental Partition Victory approach). No rules gaps require closure to make spoiling viable.

**Open item for commit:**
- [EDITORIAL: ED-324 — Institutional Mandate trigger scope: confirm Mandate-only or broader]
- [SIM-DEBT: full 5-player game simulation with active spoiler + 4 other factions needed to validate multi-faction spoiler dynamics]

