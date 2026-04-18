# VALORIA — Complete Game Systems Reference (Revision 2)
## Supersedes: valoria_complete_systems.md (Revision 1)
## Companion to: valoria_canonical_definitive_r2.md
## All issues resolved. All proposals accepted. Recency prioritized.
## Date: 2026-04-15

---

# PART 1: NAMED NPCs

## 1.1 Conviction Taxonomy

Seven Convictions: Faith (divine authority), Order (structure), Reason (evidence), Equity (just distribution), Precedent (legal continuity), Autonomy (self-determination), Continuity (sustained practice).

## 1.2 Pressure Point Types

Evidence (facts contradicting belief), Consequence (outcomes framework fails to explain), Authority (recognized binding source), Loyalty (relational obligation).

**Mapping to Contest Styles:** Evidence → Citation (Precedent + Revealing). Consequence → Vision (Prospect + Revealing). Authority → Suppression (Precedent + Obscuring). Loyalty → Any + Revealing (requires active Knot).

## 1.3 Ethical Framework Ob Modifiers

| Faction | Framework | Aligned (−1 Ob) | Contradictory (+1 Ob) |
|---|---|---|---|
| Crown | Virtue Ethics | Public, principled action | Covert, expedient action |
| Church | Divine Command | Doctrine-aligned | Against doctrine (Thread truth: +2 Ob) |
| Hafenmark | Categorical Imperative | Legal/constitutional | Ad hoc/precedent-breaking |
| Varfell | Consequentialist | Measurable outcomes within one season | Uncertain/long-term payoff |
| Guilds | Moral Relativism | Trade, guild autonomy | Moral consistency |
| Niflhel | Amoral Consequentialism | Covert (always −1 Ob) | Public (+2 Ob) |
| Löwenritter | Martial Honour | Protecting Valorian sovereignty | Personal/factional gain at Valoria's expense (+2 Ob) |
| Restoration | Rawlsian Social Contract | Benefits common population | Concentrates power |

## 1.4 King Almud Almqvist (Crown)

Not indecisive — burdened by incommensurate contradictory pressures. No good choice, only least bad.

**Convictions:** Order (primary), Reason (secondary, suppressed — privately sympathizes with Restoration, recognizes Thread reality may be true, does not act). **Pressure Point:** Consequence (primary — show the cost of maintaining order), Loyalty (secondary — via intimate Knot only). **Thread Sensitivity:** 28. **Certainty:** 3. **Authority Challenge Ob:** 2.

**Beliefs:** (1) "The peninsula survives because I hold the center." (2) "Thread truth may be real, but acknowledging it publicly would shatter the consensus." (3) "Torben must be kept from Altonian influence."

**AI Priority Stack:** 1. Survival (Stability ≤ 2 or Coup ≥ 3): internal consolidation. 2. Existential (MS ≤ 40 or IP ≥ 60): diplomacy/military redeployment. 3. Framework-aligned (public, principled, −1 Ob): Crown Treaty, Diplomacy, Governance. 4. Institutional: Suppress Church Influence if ≥ 40. Govern capital. Maintain Accord. 5. Secondary: Torben (Loyalty ≤ 3), Lenneth evaluation. 6. Reactive: proportional military response. 7. Pass.

**NPC Simulation Patch PP-NPC-01:** Crown Decree gated on Mandate ≥ 3. Prevents death spiral where Almud issues Decrees at low Mandate, fails, loses more Mandate.

**Arcs:** A (Reformer: Certainty → 0-1, Coup ≤ 1, publicly acknowledges Thread), B (Fortress: Stability ≤ 2, Certainty ≥ 3, Order doubles down), C (Overthrown: Coup Counter ≥ 3, exile).

## 1.5 Confessor Arne Himlensendt (Church)

Sincerely devout. Not cynical — wrong.

**Convictions:** Faith (primary), Order (secondary). **Pressure Point:** Evidence (primary), Authority (secondary — only Holy See or revelation). **TS:** 0. **Certainty:** 5. **Authority Challenge Ob:** 3.

**Beliefs:** (1) "Solmund's word is the only truth." (2) "The people need the Church's protection." (3) "Thread practitioners are dangerous."

**AI Priority Stack:** 1. Survival (Stability ≤ 2): suspend Investigations, focus governance. 2. Conviction-critical: Thread op in Church territory → Heresy Investigation. 3. Framework-aligned (CI < 75, Mandate ≥ 4): Assert. 4. Institutional: Piety expansion, Consul in lowest-Accord. 5. Secondary: Altonian diplomacy. 6. Reactive: Templar deployment. 7. Pass.

**PP-NPC-03:** Church Influence drift conditioned on Stability ≥ 3 AND CI < 75 AND yearly cycle.

**Arcs:** A (Zealot — default), B (Crisis of Faith: Total Victory defeat via Evidence or Temperance findings), C (Confrontation: Arc B public → Stability −3).

## 1.6 Duchess Inge Baralta (Hafenmark)

**Convictions:** Precedent/Faith (privatized). **Pressure Point:** Evidence/Consequence. **TS:** 0 (triple barrier Ob 4). **Certainty:** 5. **Authority Challenge Ob:** 1.

**AI:** 1. Survival: T8. 2. Conviction-critical: Seizure/Treaty targeting HF → Sovereign Authority Doctrine. 3. Framework-aligned: legislative, Token placement. 4. Institutional: Govern/Trade. 5. Secondary: Piety maintenance. 6. Reactive: Military (defensive only). 7. Pass.

## 1.7 Duke Magnus Vaynard (Varfell)

**Convictions:** Reason/Autonomy. **Pressure Point:** Consequence/Evidence. **TS:** 14. **Certainty:** 3. **Authority Challenge Ob:** 2.

**AI:** 1. Survival. 2. VTM at risk → prioritize. 3. Espionage (−1 Ob). 4. Investigate rivals, VTM, Wardens. 5. Southernmost expansion. 6. Counter-intelligence. 7. Pass.

**PP-NPC-04:** Varfell Private Collection cooldown enforced.

## 1.8 Grandmaster Lisbeth Ehrenwall (Löwenritter)

**Convictions:** Order (national survival)/Autonomy. **Pressure Point:** Consequence/Loyalty. **TS:** 0–5. **Certainty:** 4. **Authority Challenge Ob:** 2.

**AI:** 1. Survival. 2. Coup readiness (Counter ≥ 2): pre-position T14. 3. Border defense (−1 Ob). 4. Monitor Military stats. 5. Crown Mandate < 3 or Torben < 3 → Riskbreaker. 6. Full military response. 7. Pass.

**PP-NPC-02:** Coup requires active Church Assert, not passive TC.

**Löwenritter Five-Arm Structure:**

| Arm | Function | Mechanical Effect |
|---|---|---|
| Lions' Table | Military command, garrison | Standard military Domain Actions |
| Lions' Helm | Naval, sea route security | Secure route (+1D trade), blockade, coastal defense vs Altonian approach |
| Knights of the Peace | Patrol, law enforcement | +1 Ob covert actions in patrolled territory |
| Royal Investigators | Investigation, counter-espionage | Covert Domain Actions |
| Riskbreakers | Infiltration, deniable ops | Loyal to Valoria concept, not institutions — structural coup fault line |

**Royal Guard:** +2 Ob assassination attempts on Court members.

## 1.9 Maret Vossen (Restoration Movement)

**Convictions:** Equity/Continuity. **Pressure Point:** Loyalty/Consequence. **TS:** 0. **Certainty:** 2. **Authority Challenge Ob:** 2.

**AI:** 1. Survival. 2. Piety ≤ 1 in 3+ territories → Presence. 3. Benefits common population (−1 Ob). 4. Protect agents. 5. Community Weaving if MS ≤ 60. 6. Non-violent appeal. 7. Pass.

## 1.10 Other Named NPCs

**Torben** (Crown Heir): Conviction undefined — set by first faction at Loyalty ≥ 5. Governed by Loyalty track. **Elske** (Altonian Proxy): Autonomy/Precedent. Loyalty track. Return at IP < 60. Needs characterization (NPC audit: 24/40). **Edeyja** (Warden-Chief): Continuity/Reason. TS 75–80. Coherence 9. **Haelgrund** (Church Internal): Order/Reason (hidden). TS 12 (hidden). NPC audit: 39/40 (highest). **Lenneth** (Crown Reformist): Proposed Equity/Order (reformed). TS 8. Needs mechanical expression (NPC audit: 28/40). **Maret Uln** (Varfell Succession): Equity/Reason. TS 35. **Cardinals:** Fortitude (military), Justice (hardline), Prudence (fiscal), Temperance (scholarly — most dangerous to Himlensendt). **Guilds:** Autonomy, Moral Relativism. **Niflhel:** Autonomy, Amoral Consequentialism.

## 1.11 NPC Decision Procedure

Step 1: Institutional Filter (Ob modifiers). Step 2: Conviction Filter. Step 3: Decision Fork — Conviction Wound 0 → Conviction. Wound 1 → unaddressed Conviction. Wound ≥ 2 → Crisis table. Stability ≤ 1 → Autonomy (survival exempt). Non-named NPCs: Institutional Filter only.

## 1.12 NPC Recruitment

Identify → Approach (Cha×2+H+3, Ob = floor(NPC highest Disp/2)+1) → Offer (one incentive, max −2 Ob; Strong Hook → Ob 1) → Resolution. Failure: warned, no retry 2 seasons. Success: joins, current faction Mandate −1. OW: joins +2 Disp, brings Evidence.

---

# PART 2: COMBAT

## 2.1 Core

Pool: (Agi×2)+H+3, min 5. TN 7. Initiative: versus roll, higher net declares last. Damage: net hits + STR + weapon mod − armour DR. Crit (net ≥ 3): weapon mod doubled.

Health: Wound Threshold = End+6. Accumulates, resets on wound. Multi-wound possible. Max Wounds = floor(End/2)+1. Each Wound: −1D all pools. Stamina: End+1, min 2 (armour mod). 0 = Out of Breath (−2D).

## 2.2 Weapon System

Three axes: Reach (Short −1 TN / Long +0), Weight (Light −1 / Heavy +0), Type (Blade +0 / Blunt +1). TN 5 (Short Light Blade) to 8 (Long Heavy Blunt / Unarmed). STR minimums. Blunt ignores armour advantage (flat modifier). Blade scales down against heavier armour.

## 2.3 Actions

| Action | Key Detail |
|---|---|
| Strike | Split Off/Def, standard damage |
| Feint | **Partial commitment** (N dice min 3, rest for Def — PP-294). Margin = dice opponent loses next round. |
| Disarm | Off vs (STR+Agi) as Ob |
| Tie Up | Both −2D, blocks escape 1 round |
| Retrieve | Opposed Agi if melee |
| Establish Distance | Contested Agi |
| Escape | Agi TN 7 Ob 1, contested. Cannot if Tied Up. Out of Breath −2D. |
| Full Guard | All dice Def |
| Take a Breath | Restore Stamina by End score. Cannot in melee. |
| Dodge | Full pool passive Def vs ranged. Forfeit Off. |
| Rescue | **No Defence on redirect** (PP-285). Armour DR only. +2 Momentum on success. Outnumbered ally only. |
| Stunt | +1D to +5D environmental |
| Desperate Strike | Spend 2 Stamina, +bonus Off |
| Parry | Spend 1 Stamina, +1D Def |

Group combat Fibonacci: 2v1 +1D, 3v1 +2D, 4-5v1 +3D, 6-7v1 +4D, 8+ +5D cap.

---

# PART 3: SOCIAL CONTESTS

Setup: Adjudicator → Primary Attr (Expert: Cog, Crowd: Cha, None: Att). Conviction Track 0–10, start 5. **Style (single choice — 4 options):** Precedent (Memory + Revealing) · Suppression (Memory + Obscuring) · Vision (Projection + Revealing) · Insinuation (Projection + Obscuring).

**Exchange:** Appraise (Att+Rec, Ob = floor(Cha/2)+1) → Declare → Corroborate (optional, +1D) → Argue (Primary×2+H+3, +style bonus dice) → Resolve (Clash/Reinforce/Cross/Tie) → Forfeit options (Regroup, Concede).

Resources: Composure (Cha+6), Concentration (Foc+Rec). Institutional Mandate: Uphold or Appease (Mandate −1 to cancel).

**Calibration:** ±1 Cha = 25–30% win rate. ±4 Cha = Total Victory in 2 exchanges.

---

# PART 4: THREAD OPERATIONS

Pool: (Spi×2)+H+TPS, min 5. TN 7/8/9. Leap required (TS 30+). Contact = Focus rounds. Three-axis Ob (Depth Fibonacci + Breadth + Distance).

**Operations:** Weaving (cohere), Pulling (open), POP (temporal displacement, TN 8), Locking (freeze, TN 8, chronic MS drift), Dissolution (tear, TN 8, Gap risk), Mending (repair, Depth Ob −1, **immune to opposition**), Community Weaving (RM, Ob 3).

**Opposing:** +floor(opponent TPS/2) min +1. Winner at one degree lower. **N-way (3+):** automatic lattice collapse, all fail, Gap forms, MS −(2×practitioners).

Coherence 10→0. War-scale: 7-turn battle = 10→3. Recovery: season non-practice +1, Knot Anchoring +1.

---

# PART 5: FIELDWORK

**Investigation:** Evidence Track (Simple 3, Complex 5, Structural 8). Actions: Examine, Interview, Research, Surveil (+2 Exp), Thread-Read, Reconstruct. Calibration: 5D→D1, 13D→D1-3. Pacing: 3–5 scenes for 5-threshold.

**Socializing (PP-632):** Disposition −4 to floor(Bonds/2)+1. Ob = max(1, base−Disp). Decay above +2. Sincerity Gate: Spirit TN 7 Ob 1 (37% failure on instrumental Connect). Neutral→Bonded = 6–8 actions, 3–4 seasons.

**Stealth:** Sneak (Agi), Hide (Agi), Lockpick (Cog), Pickpocket (Agi), Disguise (Cha), Sabotage (Cog). All universal pool formula. Ambush: successful Sneak → no Def first exchange.

**Exposure:** Cover = Cog + History. Cover 3 = 3 scenes. Cover 9 = full season. Cover 12+ = near-immune.

---

# PART 6: MASS COMBAT

**Unit Health = Type Health × Size.** Heavy Infantry (10) at Size 4 = Overall 40. Pool = min(Size, Command) + Command. Seven phases: Strategy → Volley → Manoeuvre → Thread → Engagement → Cascade → Reform.

Formations: Line, Shield Wall (−1D/+2D), Wedge (+2D/−1D), Skirmish, Column, Reserve. Tactics: Envelopment, Feigned Retreat, Ambush, Concentration, Refused Flank, Hammer and Anvil.

**Splitting dominates concentration +9% to +45%.** Counters: Narrow Pass terrain, Feigned Retreat.

Battle consequences: MS −1 (Campaign −2), IP +2/season, Political Stability +1/season. Conquest → Accord 1.

---

# PART 7: FACTION LAYER & VICTORY

**Stability:** PP-403 repealed. Five triggers + Suppress Failure exception + Accounting Check + Consolidation recovery.

**Occupation:** TCV 0 both parties. Wealth −1/territory/season. Accord −1/season.

**Parliament:** Voting = Mandate. Church +floor(CI/20). Opposing Church −floor(CI/30).

**Acquisition:** Crown Treaty, Graduated Seizure (Ob = 6−Piety on 0–4), Dynastic Proclamation, Cultural Reformation, Martial Governance.

**Victory:** Universal Peninsular Sovereignty (all 15, Accord ≥ 2, Political Stability ≤ 6, 2 consecutive). 8 faction-specific alternates. Partition co-victory. Shared loss: Rupture (MS 0), Altonian Conquest (IP 100), Anarchy.

---

# PART 8: SCALE, KNOTS, AI

**Domain Echo:** Sufficient Scope → OW ±2, Success ±1, Partial narrative, Failure −1.

**Knots (PP-632):** Being-with, not Thread ops. Pool = (Bonds×2)+3. Max = floor(Bonds/2)+1 (same formula as Disposition ceiling). Close 5 / Medium 2 / Loose 1. Rupture: Disp → −4. Loss: Coherence −1 mandatory.

**AI Posture:** 1. Existential. 2. Defend. 3. Consolidate. 4. Counter-threat (CI ≥ 55). 5. Expand. 6. Opportunistic.

**Simulation baseline:** Church 53%, Crown Treaty 14%, Timeout 32%. Hafenmark collapses 27.8%. tc_political_redesign_v30 addresses via CI milestones, political legitimacy bonus, conditional passive.

**Unvalidated:** Accord+Political Stability+battle compound (ED-538). TC reform+TCV+Seizure Accord compound (ED-539). Accord-aware AI vs Hafenmark collapse. Dynastic Proclamation/Cultural Reformation.
