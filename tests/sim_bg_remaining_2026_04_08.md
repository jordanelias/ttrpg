# Valoria BG — Remaining SIM-DEBT Simulation
## Date: 2026-04-08 | SIM-DEBT-BG-03 + 04 + 05 + 06
## Modes: A (isolation) + D (edge cases)
## Source: params_board_game.md (1500L), victory_architecture_v1.md (434L) — freshly fetched post-PP-478

---

## FETCH LOG
references/params_board_game.md: ✓ (1500 lines, post-PP-478)
designs/board_game/victory_architecture_v1.md: ✓ (434 lines, post-PP-478)

---

## SIM-DEBT-BG-03: Co-Victory Pairings — Reachability Analysis

### A: Conditions Matrix

Using params_board_game.md TCV table (canonical geography_design numbering) and PROVISIONAL Crown TCV target of 16:

**Starting TCVs:** Crown 12, Hafenmark 8, Varfell 6, Church 3.
**Note: victory_arch §4 still uses stale TCV numbering (PP-199). All co-victory TCV thresholds evaluated against params geography_design numbers.**

| Pair | Key Thresholds | Crown start | Hafen start | Varfell start | Gap analysis |
|------|---------------|-------------|-------------|---------------|--------------|
| Crown + Hafenmark | Crown TCV ≥ 12, Hafen TCV ≥ 9, PI ≥ 5, TC < 50 | 12 ✓ at start | 8 → gap 1 | — | Crown already meets TCV. Hafen needs 1 TCV. PI ≥ 5 main gate (starts 7 ✓). TC < 50 main gate (starts 28 ✓). **Near-immediate co-victory path if Crown and Hafen ally early.** |
| Crown + Varfell | Crown TCV ≥ 12, Varfell TCV ≥ 8, VTM ≥ 3, RS ≥ 50 | 12 ✓ at start | — | 6 → gap 2 | Crown at start. Varfell needs TCV +2 AND VTM 3 (~S7-9). RS ≥ 50 = passive (starts 72, must not decay below 50 by S7-9). **Reachable S10-14 with no RS crisis.** |
| Varfell + RM | VTM ≥ 4, WR ≥ 2, ≥ 4 territories CV ≤ 1, RS ≥ 40, Varfell T13 | — | — | — | Hybrid only post-PP-478. VTM 4 ~S10-12. WR ≥ 2 requires 2 successful Expeditions ~S8-12. CV ≤ 1 in 4 territories requires sustained RS decline AND no Church CV pushback. **Available S14-18 in Hybrid.** |
| Hafenmark + RM | Hafen TCV ≥ 10, ≥ 4 territories CV ≤ 2, PI ≥ 4, RS ≥ 40 | — | 8 → gap 2 | — | Hybrid only post-PP-478. Hafen TCV gap 2. PI 4 (starts 7 ✓). 4 territories CV ≤ 2 requires RS ≤ ~50 (Calamity Drift). **Available S12-16 in Hybrid.** |
| Löwenritter + Hafenmark | Löw TCV ≥ 8, Hafen TCV ≥ 8, PI ≥ 4 | — | 8 ✓ at start | — | Post-coup only. Löwenritter starts with inherited Crown territory access. TCV ≥ 8 achievable if Löwenritter keeps 4-5 territories from pre-coup Crown position. PI ≥ 4 (starts 7-3=4 post-coup: PI −3 from coup. **PI 4 exactly at coup: passes immediately.** |
| Church + Hafenmark (Partition) | Crown Mandate ≤ 1, TC ≥ 50, Church ≥ 2 terr, Hafen ≥ 3 terr, no military conflict | — | 8 ✓ (4 terr) | — | TC ≥ 50: ~S12-14 uncontested. Crown Mandate ≤ 1: requires sustained suppression. Church ≥ 2: starting 1, needs seizure. **Available S14-20 if Crown politically destroyed.** |

### B: Edge Cases

**D-03-01: Crown + Hafenmark immediate co-victory threat.**
Crown TCV 12 (start ✓) + Hafenmark TCV 8 (1 short). If Hafenmark takes any TCV-1 territory in Season 1 (March into undefended T17, adjacent to T8): TCV 9. TC < 50 ✓. PI ≥ 5 ✓ (starts 7). All conditions met by Season 1 Accounting.

**This is a Season-1 co-victory risk.** Crown and Hafenmark are geographically separated (Crown: T1/T2/T3/T5/T6/T14; Hafenmark: T7/T8/T10/T17). They don't need to coordinate militarily — they just need to hold existing territories AND not be politically suppressed below the thresholds.

**P2 finding — Co-Victory-01:** Crown + Hafenmark co-victory is achievable as early as Season 1–2 with zero active play if both players hold existing territories and TC stays below 50. The 2-consecutive-Accounting-step requirement is the only gate — they must hold for 2 seasons. But if no other player attacks them, this is essentially free.

**Recommendation:** Reduce Crown TCV threshold from 12 to 14 (forces Crown to take one additional territory) OR add a condition (Crown Mandate ≥ 4 sustained 2 seasons, requiring active political management). [EDITORIAL: ED-343]

**D-03-02: Löwenritter + Hafenmark PI cliff.**
Löwenritter Coup: PI −3. Starts at 7 → 4. Co-victory condition: PI ≥ 4. Passes at 4 exactly (immediately post-coup). But if any other PI-degrading event fires before the co-victory check: Emergency Powers (PI −1) → PI 3 → co-victory blocked. 

Church Seizure (PI −1) also blocks. So the Löwenritter + Hafenmark co-victory has zero margin for PI loss post-coup. Extremely fragile.

**D-03-03: Hafenmark + RM requires RM to be founded first (PP-478).**
RM Founding requires PW ≥ 3 which takes ~3-5 seasons minimum (PW advances 1/season under ideal conditions). Then Founding roll. Then RM established. Hafenmark co-victory conditions include RM as active party. In a Hybrid game where RM is founded S5-7: co-victory potentially achievable S12-16. In BG-only: not available. Correct per PP-478.

**D-03-04: Church + Hafenmark Partition — no mechanical "no military conflict" tracking.**
The Partition condition includes "no active military conflict between Church and Hafenmark." This is a state that must be verified at Accounting but there is no token or track recording it. If Church and Hafenmark fought 3 seasons ago, does that count? The rule likely means "no military conflict this season or previous season" but this is undefined.

**[PATCH PP-479: Church + Hafenmark Partition condition "no active military conflict" defined as: no Legionary card played by either faction targeting a territory held by the other in the current season OR the immediately prior season. Physical marker: "Conflict Marker" placed on Church or Hafenmark mat when military conflict occurs; removed at second Accounting after placement.]**

### C: Co-Victory Balance Assessment

| Pair | Estimated earliest (Hybrid) | Difficulty | Balance |
|------|---------------------------|-----------|---------|
| Crown + Hafenmark | S1-2 | Very easy | P2: too easy if passive |
| Crown + Varfell | S10-14 | Medium | Balanced |
| Varfell + RM | S14-18 | Hard | Balanced for hardest path |
| Hafenmark + RM | S12-16 | Medium-hard | Balanced |
| Löwenritter + Hafenmark | S2-4 post-coup | Easy but coup-gated | Acceptable |
| Church + Hafenmark Partition | S14-20 | Hard | Balanced |

---

## SIM-DEBT-BG-04: Faction Unique Actions — Balance Analysis

### Church Actions (Piety Spread, Active Inquisition, Cardinal Focus)

**Piety Spread (PP-428):** Consul Inward, AP ≥ 1 prerequisite, pool = Mandate 5.
- Ob = target Mandate ÷ 2 + Fort. Crown T1 (Mandate 5, Fort 2): Ob = 2+2 = 4. Church pool 5 at Ob 4: P(Success) ≈ 19%. Very hard.
- Church's own territory (no fort, CV already high): Ob = 1. P(Success) ≈ 91%. Trivial.
- Finding: Piety Spread is effectively a self-reinforcement tool (Church holds territory, spreads CV in it). Cross-territory CV pushing into fortified rivals is nearly impossible without TC ≥ 50 modifier (doctrine-aligned −1 Ob).

**Active Inquisition (PP-429):** Senator Inward, pool = Mandate 5.
- Ob = territory Stability ÷ 2 round up. Lowest Stability faction (Restoration post-founding S3: Stability 3 → Ob 2). Church pool 5 at Ob 2: P(AP +2) = Success = 69%. AP accumulates quickly.
- High-Stability targets (Crown Stability 4 → Ob 2; Hafenmark Stability 4 → Ob 2). Same Ob. All mid-game targets produce Ob 2. Active Inquisition is equally effective against all non-collapsed factions.
- Finding: No Ob differentiation by target for mid-game Stability values. All produce Ob 2. Church generates AP at ~E(1.7/season) per territory with Active Inquisition.

**Cardinal Focus (PP-430):** Phase 1 declarative. No roll, no cost.
- Prudence (+1 Wealth): guaranteed. E(Wealth/season from Prudence) = 1. No opportunity cost beyond Focus slot.
- Temperance (+1 AER): guaranteed. AER 3 by Season 1 (confirmed dominant — ED-328 still flagged).
- Justice (AP threshold −1): useful when AP is at threshold-1. Situational.
- Fortitude (Templar without Legionary): powerful card-economy save. Situational.

**Finding F-Church-01:** Cardinal Focus Temperance is strictly dominant in Seasons 1-3 (free AER bypass of Hafenmark structural suppression). After AER 5, Cardinal Prudence becomes dominant (free Wealth every season). Church gets ≥1 guaranteed resource per season with zero mechanical cost. This is a strong consistent passive compared to other factions' declarative actions requiring rolls.

### Hafenmark Actions (Parliamentary Challenge, Parliamentary Session, Diplomat)

**Parliamentary Challenge (PP-431-COR):** REPLACES structural suppression when played.
- Already analysed in prior stress test: E(TC from Challenge) = −0.65 vs structural −1.0. Challenge is worse on expected TC suppression.
- Finding confirmed: Structural suppression is mechanically better than Challenge on TC impact alone. Challenge is only worth playing for the Uphold/Appease trigger (9% Overwhelming) and PI ≥ 5 Ob reduction. No Hafenmark player should regularly substitute Challenge for structural.

**Parliamentary Session (PP-432):** Once per arc. All factions vote.
- With 4 Diplomatic Tokens placed (maximum 1 per faction mat, so max 3 others): 3 factions count as Support regardless of vote. Majority = 3+1 (Ministry if AP in T1) vs 0-1 Oppose. Overwhelming majority.
- With 0 Diplomatic Tokens: depends on rival political interests. Church likely Opposes (PI growth weakens Crown suppression path Church benefits from). Varfell Abstains (covert). Crown supports if allied. Löwenritter depends.
- Finding: Parliamentary Session value is 100% conditional on Hafenmark's prior Diplomat card investment. Without Diplomatic Tokens, the vote is genuinely contested. The Diplomat→Parliamentary Session pipeline is Hafenmark's primary engine.

**Diplomat Card (ED-320):** Senator Outward, once/season.
- Pool = Influence 4. Ob = target Mandate ÷ 2 round up, min 1. Against Crown (Mandate 5) = Ob 3. P(Token placed) = Success = P(net ≥ 3) at pool 4 ≈ 27%. Low success rate against high-Mandate targets.
- Against Löwenritter post-coup (Mandate 3) = Ob 2. P(Success) ≈ 56%. Easier against weakened factions.
- Finding F-Hafen-01: Hafenmark's Diplomat success rate against strong rivals (Crown Mandate 5, Church Mandate 5) is ~19-27%. Building 3 Diplomatic Tokens for a Parliamentary Session majority takes ~6-12 seasons of investment at these rates. The pipeline is long and requires sustained Hafenmark political dominance.

### Crown Actions (Royal Charter, Royal Decree Enhancement, Thread Liaison, Diplomatic Outreach)

**Royal Charter (PP-433):** Ob = Prosperity ÷ 2, −1 Ob (Virtue Ethics). T1 (Prosperity 6): Ob = 3-1 = 2. Pool = Mandate 5. P(Success) ≈ 69%.
- Charter grants Crown own actions −2 Ob in that territory. Crown Govern in chartered T1: Ob = Prosperity/2 = 3 - 1 (capital) - 2 (charter) = Ob 0 → floor 1. Every Crown Govern in chartered capital is Ob 1.
- Max charters = Mandate/2 = 2-3. Crown can charter 2-3 territories simultaneously.
- Finding F-Crown-01: Royal Charter creates a Crown safe-zone where Ob floors at 1 for Crown's own actions. Combined with Charter's Church Seizure +1 Ob: T1 Fort 2 + Charter = Church Seizure Ob = 2+2+1 = 5. Church Mandate 5 at Ob 5: P(Success) ≈ 9%. T1 is functionally unassailable by Church seizure if chartered. Strong but requires 2 Consul Inward actions (Charter + Govern) per territory.

**Royal Decree Enhancement (PP-435):** Overwhelming only (net ≥ 4 AND ≥ 3 at Ob 2). P(OW) ≈ 9%.
- Enhancement fires ~9% of the time. The standard Success (stat ±1) fires 47% of the time.
- E(stat change from Royal Decree per use) ≈ 0.09 × 2 + 0.47 × 1 = 0.65 stat points.
- Finding F-Crown-02: Royal Decree Enhancement's Overwhelming option is low-probability but the standard Decree is Crown's primary political suppression tool. The Fragmentation modifier (+2 Ob if 3+ factions Stability ≤ 2) severely limits late-game use when exactly that situation arises (late game = high-attrition = many low-Stability factions). This punishes Crown in scenarios where they most need suppression.

**[EDITORIAL: ED-344 — Royal Decree Fragmentation modifier: +2 Ob when 3+ factions have Stability ≤ 2. This fires exactly when Crown needs Decree most (political crisis = suppression urgency). Is the intent to make Decree harder in crises (realism) or to create a reliable suppression tool (gameplay)? Suggest: Fragmentation adds +1 Ob (not +2) to preserve relevance while retaining the crisis-difficulty flavour.]**

**Thread Liaison (PP-436):** Phase 1 declarative. No roll. Links allied faction Thread operations to Crown's co-victory RS tracking.
- This is only relevant for Crown + Varfell co-victory (RS ≥ 50 condition). It allows Varfell's Thread ops to count toward Crown's RS threshold.
- Finding: Thread Liaison is a single-purpose ability (Crown+Varfell co-victory setup). In other game states it is a dead card slot. Low versatility.

### Varfell Actions (VTM Discretion, Revelation Tokens, Counter-Narrative)

**VTM Discretion (PP-438):** Spend 1 PC (at VTM 4+) to suppress VTM TC contribution. Cooldown every 2 seasons.
- VTM TC contribution not defined in params. VTM presence is public at VTM 3+. What is the exact TC generated by VTM? **[GAP: VTM TC contribution value not specified.]**
- Finding: VTM Discretion's value is entirely dependent on an unquantified TC contribution. Cannot balance until that value is specified.
- **[EDITORIAL: ED-345 — VTM TC contribution per level. How much TC does public VTM presence generate per season? This value determines whether VTM Discretion is worth 1 PC.]**

**Revelation Tokens (PP-439):** 4 consecutive PC Spy successes OR Overwhelming Tribune Investigate → permanent token.
- 4 consecutive Spy successes: P(single success at pool 4, Ob = target Intel/2)... Intel stat not defined for most factions. **[GAP: Intel stat not in faction stat table — Influence is used for Intel actions per PP-180 Intel Advancement Counter.]**
- Assuming Intel = Influence (pool 4 for Varfell), target Intel = Influence ÷ 2 = Ob 2. P(success per Spy) ≈ 56%. P(4 consecutive) ≈ 0.56⁴ ≈ 9.8%. 
- Per Overwhelming Tribune Investigate: P(OW) ≈ 9% per roll.
- Finding: Revelation Token accumulation is slow (~10% per attempt). Path A (2 tokens) expected time: ~10-20 sessions of Tribune actions. Patience Protocol exists for a reason.

**Counter-Narrative (PP-441-COR):** TC −0.5 on Overwhelming only (PP-441-COR confirmed). E(TC per use) = −0.04 to −0.135/season (from prior simulation SIM-PP-06). Primary use: AP pressure, not TC suppression.
- Combined with Intelligence Hegemony Path A: Varfell uses Counter-Narrative to generate AP (triggering Church response) while Intel actions build Revelation Tokens. The Counter-Narrative Failure exposes Varfell's presence (+2 Ob next season in that territory). In Church-prominent territories (where Counter-Narrative is most valuable), Inquisitors add +2 Ob already. A Failure → 4 Ob total on Counter-Narrative in that territory next season: near-impossible.
- Finding F-Var-01: Counter-Narrative becomes increasingly risky as Church deploys Inquisitors (+2 Ob baseline) and a prior Failure compounds (+2 Ob more). Varfell should prioritise Counter-Narrative in non-Inquisitor territories and accept the Inquisitor-territory AP as a secondary effect of Active Inquisition.

---

## SIM-DEBT-BG-05: Ministry NPC AI — Interaction Analysis

### Ministry Priority Tree (Phase 4, Priority 4)

| Priority | Condition | Action |
|----------|-----------|--------|
| 1 | PI ≤ 3 | Govern T13 (Ob 1): PI +1 |
| 2 | T13 has no Ministry AP-token | Govern T13 (Ob 1): place token |
| 3 | Any AP-token territory has Church Seizure pending | Senator vs Church (Ob = Church Mandate): delay seizure 1 season |
| 4 | Crown Mandate ≥ 4 AND PI < 5 | Senator Inward (Decree support): PI +1 |
| 5 (default) | None above | Govern in highest-Prosperity uncontested AP-token territory |

**Ministry pool = Mandate 3D.**

**Priority 1 (PI ≤ 3, Govern T13 Ob 1):**
- P(Success) at pool 3D, Ob 1 ≈ 74%. P(fail) = 26%. On failure, PI stays at ≤ 3.
- If PI = 0 (constitutional crisis): Ministry Priority 1 fires but Ministry Stabilisation is suspended after Löwenritter Coup. Ministry cannot restore PI from 0 without the Reconstitution action (PP-462, Löwenritter only). **Gap: non-Löwenritter PI=0 recovery.** If PI drops to 0 without a Löwenritter Coup (e.g., Emergency Powers + Church Seizure chain): only Hafenmark Parliamentary Manoeuvre (+1 PI on success) or Crown Parliamentary Session (+1 PI) can recover it. Ministry Priority 1 targets PI ≤ 3, not PI = 0 specifically.

**Finding F-Ministry-01:** Ministry NPC Priority 1 fires Govern T13 at Ob 1 (74% success). At PI ≤ 3, Ministry correctly shores up Parliament. However, Ministry Govern in T13 is a Domain action at Phase 4 Priority 4 — same tier as all Consul actions. If another faction (Crown, Hafenmark) has already taken T13 with a Govern action this phase, Ministry's action in T13 is redundant (territory already Governed). No conflict resolution rule states what happens when Ministry and a player faction both Govern the same territory. **[GAP: Ministry Domain action conflict when a player faction acts in the same territory same phase.]**

**[PATCH PP-480: Ministry NPC actions in a territory already acted on by a player faction this phase: Ministry's Domain action is redirected to the next-priority territory per its AI tree. Ministry does not "stack" Governs with player factions. If all viable territories are acted-on this phase: Ministry takes its Priority 5 default in an uncontested AP-token territory regardless.]**

**Priority 3 (Church Seizure pending, Senator vs Church Ob = Church Mandate 5):**
- Ministry pool 3D at Ob 5: P(Success) ≈ 4%. Near-impossible. Ministry Priority 3 almost never succeeds. It exists as narrative flavour (the clerks object, but Church ignores them) rather than mechanical effect.
- Finding F-Ministry-02: Priority 3 is a dead action. 4% success rate means Ministry delays Church Seizure ~4% of the time. Recommend raising effectiveness or reframing as a delay mechanism that doesn't require a roll.
- **[EDITORIAL: ED-346 — Priority 3 Ministry vs Church Seizure: should this be a contested roll or an automatic 1-season procedural delay? Ministry's institutional role (procedural objection, legislative record) suggests the delay should be automatic regardless of roll, with the roll determining whether Ministry takes damage. Suggested: Priority 3 fires = Church Seizure delayed 1 season automatically. Roll: Ministry Mandate vs Ob 2. Failure: Ministry Stability −1 (Church overrides the objection and damages the institution). Success: no Ministry damage.]**

### Ministry Collapse Cascade

Ministry Mandate 0 → collapse. Crown Policy unavailable. Parliamentary Manoeuvre +1 Ob. During collapse (2 seasons): all Ministry NPC actions suspended.
Recovery: Hafenmark or Crown Govern in T13 (Ob 2).

**Cascade risk:** If Crown is in Emergency Powers (Crown Mandate crisis) AND Ministry collapses simultaneously → Crown cannot issue Policy → Crown cannot use the one tool (Emergency Powers) that might stabilise. Crown's Stability spiral accelerates. This validates the Ministry design as a meaningful structural check on power consolidation — a Crown that destabilises Ministry loses its political toolkit. Correct design.

---

## SIM-DEBT-BG-06: RS Decay — 20-Season Projection

### RS Decay Sources (cumulative per season)

| Source | Rate | Condition |
|--------|------|-----------|
| Baseline drift | −1 | Year-End only (every 4th season) |
| Thread operations (adverse) | Variable | Per Thread Debt token aged >1 season |
| Calamity Drift (CV ≤ 1 territories) | −1 per eligible territory | RS ≤ 50 for T6/T13; RS ≤ 35 for broader; RS ≤ 20 global |
| Warden Cooperation ≥ 2 | Halves baseline | WC ≥ 2 |
| Warden Cooperation = 3 | +2/season | WC = 3 |
| Thread Wound (TT ≥ 15, PROVISIONAL ED-341) | −1/Wound at Accounting | If ED-341 adopted |

### 20-Season RS Projection (no Warden engagement, no Thread Wounds)

**RS = 72 at start. Baseline drift = −1/Year-End = −0.25/season average.**

Seasons 1-4 (Year 1): RS 72 → 71 (−1 at Season 4 Year-End).
Seasons 5-8 (Year 2): RS 71 → 70.
Seasons 9-12 (Year 3): RS 70 → 69.
Seasons 16-20 (Year 5): RS 69 → 67.

**Baseline drift alone over 20 seasons: RS 72 → 67. Not threatening.**

However, Thread Debt tokens aged >1 season add RS −1 each. At 2 Thread operations/season with 20% Thread Debt rate (3/20 Co-Movement cards): 2 × 0.2 = 0.4 Thread Debt tokens/season average. After 1 season aging: 0.4 RS/season loss from Thread Debt.

**Adding Thread Debt (moderate Thread activity):**
RS 72 → 67 − (0.4 × 20) = 67 − 8 = **RS ~59 at Season 20.** Above the RS ≤ 60 Calamity Drift threshold for T6/T13 (barely). No Calamity Drift fires.

**High Thread activity (4 ops/season, 30% Debt rate):**
Thread Debt contribution: 4 × 0.3 = 1.2 tokens/season → 1.2 RS/season. Over 20 seasons: 24.
RS 72 − 5 (baseline) − 24 (Thread Debt) = **RS ~43.** Calamity Drift fires for T6/T13 at RS ≤ 50 (fires ~Season 14). Each drifted territory: CV −1/season. With 2 territories drifting: −2 CV/season across board = accelerating RM Founding conditions (more CV ≤ 1 territories).

**With WC ≥ 2 (Warden engagement from Season 8 approximately):**
Baseline halved → −0.5/Year-End. Thread Debt still applies. RS at Season 20: 72 − 2.5 − 12 (high Thread) = **RS ~57.** Much safer.

**Finding F-RS-01:** RS is not at existential risk in a 20-season game unless:
1. Thread activity is consistently high (4+ ops/season), AND
2. Warden Cooperation never reaches ≥ 2, AND
3. Thread Wounds accumulate (ED-341, if adopted: each Wound −1 RS/Accounting).

Without Thread Wounds, RS only becomes critical (< 40) under very high Thread activity + zero Warden engagement. The shared loss condition (RS = 0) is essentially impossible in a 20-season game under normal play. However, RS ≤ 60 (RM Founding threshold for PW) is achievable by Season 8-12 under high Thread play, which meaningfully enables RM emergence.

**Finding F-RS-02:** RS ≤ 50 (CV threshold for T6/T13 Calamity Drift) fires S14-18 under high Thread play. This creates a self-reinforcing cycle: high Thread → RS ≤ 50 → Calamity Drift → CV ≤ 1 territories → PW advances → RM Founding → RM Weaving → more Thread activity → faster RS decline. The system has positive feedback that escalates in the late game. This is the intended escalating pressure the clocks are designed to produce. Correct design.

**Finding F-RS-03: WC ≥ 2 is essential for long campaigns.** In 25+ season campaigns (if the game extends), RS threatens critical range (< 40) by Season 22-25 under high Thread activity. WC ≥ 2 halves decay and buys ~8-10 additional seasons. Expedition investment early (Varfell VTM 3+ around S7-9) is the critical intervention point.

---

## P1/P2/P3 FINDINGS FROM THIS SIMULATION

### P1

**P1-08 — Crown + Hafenmark co-victory achievable Season 1-2 with zero active play.**
Crown TCV 12 ✓ at start. Hafenmark needs TCV 9 (has 8, gains 1 from any territorial hold). TC < 50 ✓ at start. PI ≥ 5 ✓ at start. If neither Crown nor Hafenmark is attacked and they hold existing territories for 2 Accounting steps: co-victory declared. No other faction can prevent this purely by holding their own territories.
Severity: P1 — effectively removes the co-victory's value as a meaningful arc goal.
**[EDITORIAL: ED-343 — Strengthen Crown + Hafenmark co-victory requirements. Options: (a) Crown TCV ≥ 14 (forces active expansion), (b) add Crown Mandate ≥ 4 sustained 2 seasons, (c) require PI ≥ 7 (currently starts at 7, degrades easily — forces PI maintenance). Provisional: add Crown Mandate ≥ 4 condition.]**

### P2

**P2-07 — Church + Hafenmark Partition "no active military conflict" undefined.**
No tracking mechanism. Ambiguous lookback period.
Fixed by PP-479.

**P2-08 — Ministry Priority 3 effectively dead (4% success rate).**
Church Seizure delay via Ministry Mandate roll at Ob = Church Mandate 5 with pool 3D is near-impossible.
[EDITORIAL: ED-346 — automatic delay with roll for Ministry damage.]

**P2-09 — VTM TC contribution unspecified.**
VTM Discretion (PP-438) cannot be balanced without knowing the TC contribution of public VTM presence.
[EDITORIAL: ED-345]

**P2-10 — Royal Decree Fragmentation modifier fires at worst time.**
+2 Ob when 3+ factions at Stability ≤ 2 = late-game political crisis = exactly when Crown needs Decree most.
[EDITORIAL: ED-344 — reduce to +1 Ob.]

**P2-11 — Ministry Domain action conflict undefined.**
When Ministry and a player faction both act in the same territory in Phase 4 Priority 4: no resolution rule.
Fixed by PP-480.

**P2-12 — Löwenritter + Hafenmark co-victory has zero PI margin post-coup.**
PI hits exactly 4 (the threshold) after the coup's PI −3. Any subsequent PI loss (Emergency Powers, Church Seizure) blocks co-victory. Near-impossible in practice without sustained PI protection.
Severity: P2 — intended fragility but worth noting. No patch; design-coherent with the Löwenritter's precarious position.

### P3

**P3-03 — Thread Liaison is single-purpose.**
Crown unique action (PP-436) only useful for Crown+Varfell co-victory RS tracking. Dead in all other contexts.
Severity: P3 — acceptable faction-specific tool.

**P3-04 — Revelation Token accumulation rate (~10% per attempt) is very slow.**
Patience Protocol is explicitly designed for slowness. P3 — correct design, no change.

---

## NEW PATCHES

| PP | Scope | Description |
|----|-------|-------------|
| PP-479 | Co-victory | Church + Hafenmark Partition "no military conflict" defined: no Legionary action by either faction targeting other's territory in current or immediately prior season. Conflict Marker (flip token) tracks this. |
| PP-480 | Ministry | Ministry NPC Domain action redirects if target territory already acted on by player faction same phase. |

## NEW EDITORIALS

| ED | Priority | Description |
|----|---------|-------------|
| ED-343 | P1 | Crown + Hafenmark co-victory requires strengthening (achievable Season 1-2 passively) |
| ED-344 | P2 | Royal Decree Fragmentation modifier: +2 Ob (current) vs +1 Ob (proposed) |
| ED-345 | P2 | VTM TC contribution per level (required to balance VTM Discretion) |
| ED-346 | P2 | Ministry Priority 3 vs Church Seizure: automatic 1-season delay vs near-impossible roll |

---

## COVERAGE MATRIX UPDATE

| Mechanic | Mode A | Mode D | Status | Issues |
|----------|--------|--------|--------|--------|
| Co-victory pairings | ✓ | ✓ | Issues found | P1-08 Crown+Hafen, P2-07 Partition tracking |
| Church unique actions | ✓ | ✓ | Issues found | F-Church-01 (Cardinal Focus dominant), balance noted |
| Hafenmark unique actions | ✓ | ✓ | Issues found | P2 (Challenge<structural confirmed), F-Hafen-01 |
| Crown unique actions | ✓ | ✓ | Issues found | P2-10 (Decree Fragmentation), P3-03 (Thread Liaison single-purpose) |
| Varfell unique actions | ✓ | ✓ | Issues found | P2-09 (VTM TC undefined), F-Var-01 |
| Ministry NPC AI | ✓ | ✓ | Issues found | P2-08 (Priority 3 dead), P2-11 (Domain conflict) |
| RS decay (20-season) | ✓ | — | Complete | F-RS-01/02/03 — system healthy, WC critical long-term |
| Battle resolution | ✓ | ✓ | Complete | PP-476 applied |
| Thread operations (BG) | ✓ | ✓ | Issues found | ED-338-342 open |

**All SIM-DEBT items addressed.** No further queued simulations.

