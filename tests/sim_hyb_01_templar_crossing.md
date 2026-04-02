# SIM-HYB-01: "The Templar Crossing" — Complete Hybrid Session Simulation
## Date: 2026-04-02
## Status: Session A (G4 + G1 + K2 + C + G3 + G2 + K2 Zoom Out)
## Session B pending: D + J + L + M

---

## 7-DIMENSION TAG

```
Test ID: SIM-HYB-01
Mechanics: G1 Mass Combat, G2 Debate, G3 Threadwork, G4 Faction Seasonal, K2 Transition, C Full Scenario
Mode: HYB
Temporal: PRES (~Season 2, 245 AG)
Tracks: TC, RS, IP, PI, Stability, Coherence, Composure, Health/Wounds, Unit Str/Morale/Cohesion
Factions: Church, Varfell, Crown, Hafenmark
NPCs: Vaynard (practitioner proxy), Cardinal Klapp, Generic Church Templar Sergeant
Archetypes: Practitioner-Scholar, Church Militant, Institutional Legalist
```

---

## SCENARIO SEED

**Title:** The Templar Crossing  
**Trigger:** Season 2. TC = 34 after accounting. Church declares Templar deployment into T6 (Varfell Highlands) — a contested border territory. BG Battle Resolution fires. Vaynard is present in T6 conducting covert Thread research → Zoom In triggers. Scene: Vaynard operates during Phase 4 (Offensive Thread), stabilising a growing Gap as the battle rages. Post-engagement, Cardinal Klapp commands him to surrender. Debate fires. If Vaynard loses the debate, the Sergeant enforces capture.

---

## STARTING STATE

**BG Clocks:** TC=32, RS=68, IP=22, PI=5  
**Faction Stats (BG starting):**

| Faction | M | I | W | Mil | Sta |
|---------|---|---|---|-----|-----|
| Crown | 5 | 5 | 4 | 4 | 4 |
| Church | 5 | 6 | 5 | 4 | 5 |
| Varfell | 3 | 4 | 3 | 4 | 4 |
| Hafenmark | 4 | 4 | 5 | 3 | 4 |

---

## MODE G4 — FACTION PLAY (SEASONAL): SEASON 2

### Phase 1: Clock Accounting

- **Church Assert** (mandatory, TC > 28): TC +1 → TC = 33  
- **T3 territory control** (Church holds T3): TC +1 → TC = 34  
- **IP base advance:** 0/season (event-driven). No events this season yet. IP = 22.  
- **RS:** No automatic change. RS = 68.  
- **PI:** No domain actions targeting Parliament this season. PI = 5.

**Post-accounting clocks: TC=34, RS=68, IP=22, PI=5**

### Phase 2: Domain Actions (relevant to scenario)

**Church Action: Templar Deployment → T6 Varfell Highlands**  
- Rolls into BG Battle Resolution. See Mode G1.

**Varfell Action: Defend T6**  
- Defensive. Triggers defender terrain bonus.

**Crown Action: Diplomatic Opposition (Domain Action: Influence)**  
- Crown attempts to pressure Church via Parliamentary Manoeuvre: pool = Crown Influence (5D) TN7 vs Ob 2 (+1 PI≥5 condition: PI=5 exactly, no modifier).  
- E[net] = 5 × 0.30 = 1.5. P(≥2) ≈ 70%.  
- **Most likely: Crown succeeds.** Effect: Church must pay +1 Mandate if battle proceeds (Diplomatic Cost mechanic).

[PARAMS GAP: BG "Diplomatic Opposition" mechanic — no specific rule extracted. Using parliamentary opposition as proxy. Flag for params update.]

**Church Mandate cost: −1 (diplomatic penalty for contested military action). Church M: 5→4.**

---

## MODE G1 — MASS COMBAT: BATTLE OF T6

### Setup (BG Battle Resolution)

**Church Templar Force:**
- Pool: Church Military 4D, TN7
- E[net] = 4 × 0.30 = 1.2

**Varfell Border Garrison:**
- Pool: Varfell Military 4D, TN7, +1D defender terrain (home territory [PROVISIONAL])
- Total: 5D, E[net] = 5 × 0.30 = 1.5

[PROVISIONAL: defender home territory = +1D to pool (not Ob modifier). No confirmed BG Battle modifier rule — params_board_game P-16 table truncated.]

### Probability Analysis

Church 4D vs Varfell 5D (TN7, E[net] comparison):

| Scenario | Church net | Varfell net | Winner |
|----------|-----------|------------|--------|
| Expected | 1.2 | 1.5 | Varfell (margin 0.3) |
| Church high (75th) | ~2 | ~2 | Tie |
| Varfell high (75th) | ~1 | ~2-3 | Varfell decisive |

P(Varfell wins): ~50%  
P(Tie): ~15%  
P(Church wins): ~35%

**Most likely BG outcome: Varfell successful defence. T6 holds. Church Military: 4→3 (losses).**

### Zoom In Trigger

Vaynard is present in T6 conducting Thread research. BG Battle fires → Zoom In is mandatory per state_transfer_spec.md.  
BG turn suspended at Battle Phase 5 (Engagement ongoing).

---

## MODE K2 — TRANSITION: BG → HYB (ZOOM IN)

### State Inventory Check

| BG Variable | TTRPG Equivalent | Handled? | Notes |
|-------------|-----------------|----------|-------|
| Church Military (4→3) | Church Templar unit Strength | ✓ | [PROVISIONAL: BG Military × 1.5 rd down = Str. Church 3 × 1.5 = 4] |
| Varfell Military (4) | Varfell garrison unit Strength | ✓ | [PROVISIONAL: 4 × 1.5 = 6] |
| TC = 34 | Reference only (no TTRPG clock mechanic) | ✓ | Suspended |
| RS = 68 | RS track — direct transfer | ✓ | 1:1 |
| IP = 22 | Reference only | ✓ | Suspended |
| Current BG phase | Battle Phase 5 suspended | ✓ | Per spec |
| Faction stats (all) | Not directly transferred | ✓ | Queue to Accounting |
| Commander present? | Generic Church Templar Sergeant | ✓ | Stat block generated |

**Suspension check:**
- BG Domain Actions: ✓ suspended
- BG Seasonal Accounting: ✓ suspended  
- BG Co-Movement draws: ✓ suspended  
- All other faction turns: ✓ hold

### P1 Gap Found

**[GAP-K2-01 — P1]: BG Military stat → TTRPG unit Strength conversion formula not defined.**  
BG Military (1-7 faction stat) and TTRPG Unit Strength (0-10 headcount proxy) are different constructs. The state_transfer_spec says "1:1 (same scale)" but they are not the same scale. A faction Military = 4 in BG does not mean 4 Strength in TTRPG — Military governs max CP tier and starting Cohesion ceiling (from params_mass_combat), not unit Strength directly.  
**Effect:** Every Zoom In involving a military unit carries an undefined state variable. This is a P1 structural gap.  
**Provisional resolution:** [PROVISIONAL: For Zoom In, treat BG Military stat as the unit's CP (not Strength). Strength = Military × 2 (represents multiple sub-units). Crown Military 4 → CP 4, Strength 8. This matches the params_mass_combat CP tier table.]  
**→ PP-101 needed: Define BG Military → TTRPG unit state conversion in state_transfer_spec.**

Applying provisional: Church Templar unit Str = 8, CP = 4 (Veteran tier). Varfell garrison Str = 8, CP = 4.

**Zoom In state transfer: COMPLETE (with provisionals noted).**

---

## MODE C — FULL SCENARIO: "VAYNARD AT THE CROSSING"

### TTRPG Scene Starting State

**Location:** T6 Varfell Highlands, a fortified river crossing. Battle Phase 5 (Engagement) ongoing — Varfell garrison holding the line. Vaynard is behind the Varfell defensive formation (protected from direct Engagement). A growing Gap has appeared near the crossing — RS dropping as combat stresses local Thread fabric.

**State: Battle Phase 4 / Round 1**

```
Vaynard — Agi 2, Pre 3, Cog 4, End 2, Str 2, Spi 4, Att 3
Health: 2/2 | Wounds: 0 | Stamina: 3 | Combat Pool: 7D | Composure: 8
TS: 55 | TD: 4 | TPS: 5 (TS÷10) | Coherence: 10 | Focus: 3
Conditions: None | Armour: None | Weapon: None (unarmed, Ob 8 attack)
Tracks: RS=68, TC=34

Church Templar Unit — CP: 4 | Str: 8 | Cohesion: 5 | Morale: 5 | Armour: Medium | Weapon: Heavy Cut
Varfell Garrison Unit — CP: 4 | Str: 8 | Cohesion: 5 | Morale: 5 | Armour: Light | Weapon: Heavy Cut

Cardinal Klapp (rear, not in combat)
Pre 4, Cog 4, Composure: 10 | Debate pool: (4×2)+3 = 11D | History (Church Law): 3
Beliefs: Divine authority governs temporal power; Confession removes spiritual stain only (not temporal crime)
Primary debate genre: Past (Church canonical precedent)

Templar Sergeant (Phase 6 Step 4 antagonist — not yet active)
Agi 3, Str 4, End 4 | Combat Pool: 9D | Stamina: 5 | Health: 4/4 | Wounds: 0
Armour: Medium | Weapon: Heavy Cut (TN6 attack / TN7 defence / Dmg +4-5)
```

---

### PHASE 4 — OFFENSIVE THREAD: VAYNARD'S OPERATION

**Situation:** RS = 68. A forming Gap near the crossing (stress from mass combat). Vaynard diagnoses and attempts Weaving (Object/Personal scale — targeting the specific thread configuration destabilising near the crossing).

**Step 1: Diagnosis**  
Priority 4. No roll. Mandatory before Weaving.  
GM describes: configuration loosely actualised (Pulling outward — not yet a Gap, but trending). Temporal weight: moderate (recent conflict has disrupted co-movement). Epistemic: low (it's physical-world threading, not belief-complex).  
Diagnosis complete. Weaving Ob 1 (Object/Personal scale, TS 55 ≥ 30 required: ✓).

**Step 2: Leap Roll**  
Vaynard is behind the defensive line — not in melee, not targeted by Phase 5. Eligible for Leap.  
Eligibility check: Approach Training ✓ | TS 55 ≥ 30 ✓ | Not in melee ✓ | Not at incapacitation threshold ✓  

Pool: Attunement (3) + Thread Scholarship History bonus (+2) + TPS (5) = 10D, TN7, Ob1 (TS 50+ = Ob 1 ✓).

E[net] = 10 × 0.30 = 3.0. This is well above Ob 1.

P(Overwhelming, net ≥ 2×1 = 2): P(≥2 net, 10D TN7) ≈ 90%  
P(Success, net ≥ 1): ≈ 99%

**Most likely Leap: Overwhelming.**  
Result: Clean suspension. Next operation Ob −1 (min 1, so Ob already 1 → stays 1). +1 TS (TS: 55→56).

State delta: TS = 56, TPS = 5 (no change — 56÷10 still = 5). Contact established. Focus = 3 → 2 op rounds available (Round 1 = Leap, Rounds 2-3 = ops).

**State: Phase 4 Round 1 post-Leap**
```
Vaynard — TS: 56 | Coherence: 10 | Contact established | Ops remaining: 2
Weaving Ob: 1 (was 1, -1 from Overwhelming but floor 1 applies)
```

---

### PHASE 4 — ROUND 2: WEAVING OPERATION

Pool: Spirit (4) + Thread Scholarship (+2) + TPS (5) = 11D, TN7, Ob1.

E[net] = 11 × 0.30 = 3.3. P(Overwhelming, ≥2): ≈ 93%.

**Most likely: Overwhelming Weaving.**

Weaving degree table (Object scale, Overwhelming):
- RS +1 (Relational+ only — Object scale does NOT trigger RS gain). Object scale: no RS change.
- +1 TS: TS 56→57. TPS = 5 (no change).
- Coherence: 0 penalty.
- Gap formation check: Gap was imminent (RS=68 with trending); Weaving success stabilises the configuration. RS unchanged at 68 (Object-scale Weaving does not increase RS; it stabilises the local configuration only).

Wait — does Weaving restore RS? From params_threadwork: "Overwhelming: RS +1 (Relational+ only)". Object scale: no RS change. The Gap risk is mitigated by stabilising the Object-level configuration. RS stays 68. The Gap does not form this scene.

**Co-movement fires (mandatory, P-01 compliance):**

Three auto-effects:
1. **Temporal auto-effect** (Object scale): Narrative only (no Coherence cost for Object/Personal scale per params). "The river crossing feels slightly outside its moment — observers note the water runs strangely still during the weave." No mechanical effect.
2. **Epistemic auto-effect** (by degree): Overwhelming → "Primary genre + orientation + one specific detail" — the operation reveals something about the thread fabric. Vaynard learns: the Gap is not combat-stress-induced — it has been present for longer. Pre-existing instability. +1 future investigation roll re: this location.
3. **Actual d6**: Not rolled (simulator uses expected values). At Object scale, Actual consequence is typically minor. [Expected: narrative flourish — a soldier nearby stumbles momentarily].

P-01 COMPLIANCE: All three auto-effects confirmed fired. ✓

**State delta:**
```
Vaynard — TS: 57 | Coherence: 10 | Ops remaining: 1
RS: 68 (unchanged — Object scale, no RS modification)
Gap: AVERTED (local configuration stabilised for this scene)
```

**Vaynard has one operation round remaining.**

---

### PHASE 4 — ROUND 3: SECOND OPERATION (optional)

Vaynard can use the final op round or hold. Given the stabilised configuration, a second Weaving at Ob 1 is redundant. He uses the round for Diagnosis of the broader territory — gathering intelligence for future ops.

Diagnosis: No roll. Reveals: The territory has 2 additional unstable configurations at Relational scale (too large for Vaynard's current contact to address — would require TS 50+ at Ob 3, and he'd need to restart contact). These are flagged for future session.

**Contact ends naturally (Focus = 3, ops complete).**

**Coherence Retention Roll (end of Leap contact):**  
Pool: Spirit (4) + Thread Scholarship (+2) + TPS (5) = 11D, TN7  
Ob: sum of all operation Obs this contact = 1 (one Weaving at Ob 1)  
E[net] = 3.3 >> Ob 1. P(pass): ~99%.

**Coherence retained: 10 (unchanged).**

---

### PHASE 5 — ENGAGEMENT (Mass Combat Ongoing)

Vaynard is not in the Engagement. The main battle resolves:

**Church Templar unit vs Varfell Garrison (from G1):**

Both units CP 4, Str 8, TN7. Each allocates pool between Offence/Defence. Assume symmetric allocation (4D Offence, 0D Defence each — mass combat doesn't split the same way as personal combat):

[PARAMS GAP: Mass combat pool split — does Phase 5 Engagement use a pool-split mechanic (like personal combat) or simultaneous rolls with fixed allocation? params_mass_combat says "Pool split, roll, damage recorded. Max 3 simultaneous (TTRPG)" — this implies pool split applies to mass combat too. But the split parameters (how much to Offence vs Defence) are undefined for mass combat units.]

[PROVISIONAL: Mass combat units split CP = ½ to Offence, ½ to Defence (rounded down to Offence, round up to Defence for defensive engagements). CP 4 → Off 2D, Def 2D.]

Church Offence 2D vs Varfell Defence 2D (TN7):  
E[net Off] = 0.60, E[net Def] = 0.60. Expected margin = 0. Tie → no territory change, minimal Strength loss.

Varfell Offence 2D vs Church Defence 2D (TN7):  
Same — expected tie.

**Expected Phase 5 outcome: Low-damage exchange. Neither side routs. Both take minor Strength losses.**

Applying mass combat damage formula (expected 1 excess success × weapon modifier: this is mass combat so damage scale applies differently):

[PARAMS GAP: Mass combat damage formula — how excess successes translate to Strength loss at unit level. params_mass_combat has damage table for personal weapons but no unit-scale damage formula. DR table exists for armour but no "Strength points lost per excess success" formula.]

[PROVISIONAL: 1 excess success = 1 Strength point lost per engaged unit. Applying: Church Str 8→7, Varfell Str 8→7 (symmetric exchange).]

Cohesion check: Strength lost (1) ≤ Cohesion (5) → no Cohesion penalty.  
Morale: no triggers fired (Str not < 50% max).

**Post-Phase 5 state:**
```
Church Templar unit — Str: 7 | CP: 4 | Cohesion: 5 | Morale: 5
Varfell Garrison — Str: 7 | CP: 4 | Cohesion: 5 | Morale: 5
```

---

### PHASE 6, STEP 4 — PERSONAL ACTION: TEMPLAR SERGEANT CONFRONTATION

The main engagement winds down. A surviving Templar Sergeant pushes through to Vaynard's position, demanding surrender. Cardinal Klapp arrives at the perimeter — he recognises Vaynard as a Thread practitioner and sees an opportunity to assert Church authority.

**The Sergeant raises his blade. Vaynard has three options:**
1. Fight (7D vs Sergeant's 9D — see F-HYB-01 below)
2. Attempt to flee (Agility check — very slow character)
3. Address Klapp directly (Debate — the more viable path)

**Vaynard chooses: Address Cardinal Klapp (triggers Mode G2 Debate).**

The Debate mechanic preempts the combat resolution: if Vaynard can convince Klapp that his Thread work served the Church's interest (and the broader Valoria interest), Klapp calls off the Sergeant.

**Finding logged:**

**[F-HYB-01 — P1]: Scholar practitioner has no viable combat survival path.**  
Vaynard at 7D vs Templar Sergeant 9D: E[Sergeant margin] = (9-7)×0.30 = 0.6 excess successes/round. With Heavy Cut Dmg +4-5, No Armour: single hit = ~1+4+4 = 9 damage vs Health 2 = instant incapacitation with overwhelming probability (~95%). No Leap possible from incapacitation state. A practitioner in this scenario has no mechanically viable path to Threadwork if combat resolves before Phase 4.  
**Critical dependency:** Phase 4 safe-zone rule is implied but not stated. Any scenario where the practitioner enters Phase 5 engagement without allies blocking is auto-lose.  
**Patch required:** Add explicit positioning rule — practitioners behind front line are not targeted by Phase 5 Engagement unless their zone is breached. Zone breach is a Phase 3 (Manoeuvre) outcome, not automatic.  
→ **PP-101 needed.**

---

## MODE G2 — DEBATE: VAYNARD vs CARDINAL KLAPP

**Setup:**  
- Vaynard addresses Klapp directly, invoking the Thread evidence he gathered during the operation.  
- Issue: Was Vaynard's presence here legitimate? Does the Church have authority to detain a private Thread researcher operating in Varfell territory?  
- Stakes: Conviction Track 0–10. Start: 5 (neutral). Win for Vaynard ≥ 7. Win for Klapp ≤ 3.  
- Audience: Templar soldiers (Church-loyal, Stability 5). Resistance = ⌈5÷2⌉ = 3. [PROVISIONAL: resistance = Stability÷2 round up — formula not confirmed, typical 1-3.]

### Debate Pools

**Vaynard:**  
(Presence × 2) + History = (3×2) + 1 (Research/Political History) = 7D  
Memory bonus (+2D when citing specific verifiable claim): eligible when invoking diagnostic findings.  
Read pool: Attunement (3) only, TN7 Ob1.  
Primary genre affinity: Future (consequentialist — "what happens if TC reaches 65 and the Church seizes all Thread practitioners?")  
Genre weight modifier: Varfell audience → Consequentialism → Future boosted +0.5 → Future weight: 1.5

Wait — Audience ethical mode modifier applies to the *audience* genre preference. Varfell faction ethical mode = Consequentialism → Future boosted. But the audience here is Church Templars, not Varfell. Church ethical mode = Divine Command → Past boosted.

Revising: Audience = Church Templars. Ethical mode = Divine Command. Past genre: boosted +0.5 → Past weight: 1.5. Future weight: 0.5.

This means Vaynard (Future primary) is at a disadvantage against this audience. His Future arguments carry weight 0.5, while Klapp's Past arguments carry 1.5.

**This is intentional design — the mechanic penalises arguing out-of-mode to a hostile audience.**

**Klapp:**  
(Presence × 2) + History = (4×2) + 3 = 11D  
Read pool: Cognition (4) — wait, Read uses Attunement only per params_debate. Klapp's Attunement:  
[PARAMS GAP: Cardinal Klapp Attunement stat not defined in any NPC stat block. Using Cognition as proxy = 4.]  
[PROVISIONAL: Klapp Attunement = 2 (Church officials have low Thread sensitivity; Church suppresses Thread knowledge — canon-consistent).]  
Klapp Read: 2D only. TN7 Ob1. E[net] = 0.6. P(success) ≈ 50%.  
Primary genre: Past (canonical precedent, Divine Command). Past weight: 1.5 (audience bonus).

---

### EXCHANGE 1

**Step 1 — Read:**

Vaynard Read (3D TN7 Ob1): E[net] = 0.9. P(≥1) ≈ 75%.  
Most likely: **Success** → Vaynard identifies Klapp's primary genre (Past) + orientation preference (Revealing — Klapp wants to expose Vaynard's activity as unauthorised).

Klapp Read (2D TN7 Ob1): E[net] = 0.6. P(≥1) ≈ 60%.  
Most likely: **Partial** → Klapp identifies Vaynard's primary genre only (Future).

**Step 2 — Choose:**  
Vaynard: knowing Klapp will use Past+Revealing, chooses **Past+Revealing** (CLASH — same genre, opposite... wait: same genre AND same orientation = AMPLIFY, not CLASH). 

Reread: CLASH = Same genre, *opposite* orientation. AMPLIFY = Same genre, *same* orientation.

Vaynard considers: if he picks Past+Revealing (same as Klapp), that's AMPLIFY (both trying to reveal Past truths). If he picks Past+Obscuring, that's CLASH.

**Vaynard's strategic choice:**  
CLASH: Vaynard argues same genre (Past), opposite orientation (Obscuring — he wants to reframe the historical precedent). Risk: Klapp has 11D vs his 7D; margin likely favours Klapp.  
AMPLIFY: Both use Past+Revealing — combined pool vs Conviction Track resistance. Pool = Vaynard 7D + Klapp 11D = 18D vs resistance 3. Track would move heavily — toward whoever has narrative framing.

Wait — AMPLIFY: "Combined pools vs Conviction Track resistance." If both orators pick AMPLIFY, which direction does the track move? The design seems to be that both are arguing the same case (same genre, same orientation). But Vaynard and Klapp have opposing positions. If both pick Revealing+Past, they're both saying "look at the historical truth" — but they disagree on what that truth implies.

[PARAMS GAP: AMPLIFY with opposing speakers — direction of track movement unresolved. If both orators pick same genre+orientation but argue opposite conclusions, AMPLIFY combined pool doesn't specify which direction the track moves. Assumes cooperative framing, but adversarial same-genre AMPLIFY is mechanically undefined.]

This is a P2 design gap. In an adversarial debate, AMPLIFY with opposing positions is incoherent — you can't both be "revealing the same truth" while arguing opposite conclusions. The rule needs clarification.

**[F-HYB-02 — P2]: AMPLIFY in adversarial debate — no track direction rule.**  
When two orators choose same genre + same orientation but hold opposing positions, AMPLIFY combined pool resolves without specifying which direction the track moves. Rule assumes cooperative framing (both building the same case), but adversarial AMPLIFY is mechanically undefined.  
**Patch:** In adversarial debate, AMPLIFY = initiative holder's pool +3D (audience boosted by shared genre), respondent pool unchanged. Track moves toward initiative holder if initiative holder's net > resistance. This preserves AMPLIFY's power while assigning direction.  
→ **PP-102 needed.**

**Vaynard opts for CLASH** (Past+Obscuring vs Klapp's Past+Revealing) — the mechanically defined path.

**Step 3 — Argue:**

Initiative holder: Higher Presence acts first (Exchange 1). Klapp Presence 4 > Vaynard Presence 3 → Klapp has initiative.

**Klapp rolls first (CLASH, Past+Revealing):**  
Pool: 11D TN7.  
E[net] = 11 × 0.30 = 3.3.  
P(Overwhelming, ≥2× Ob ... wait, CLASH doesn't use Ob in the standard sense — it's margin-based): The winning margin is the difference in successes, not Ob-based.

Let me use the CLASH resolution as: Klapp net − Vaynard net = margin. Apply movement formula.

**Klapp net: E = 3.3** (expected 3-4 successes at 11D TN7)  
**Vaynard net: E = 2.1** (7D TN7, expected 2 successes)

**Expected margin: 3.3 − 2.1 = 1.2 → approximately 1.**

Movement formula:  
margin (1) × genre_weight (Past = 1.5 for Church audience) × orientation_weight (Revealing = 1.0 standard) = 1.5.  
1.5 > resistance (3)? No — 1.5 < 3. **Track movement: 0.**

Conviction Track stays at 5. Despite Klapp's advantage, the Church Templar audience already believes what Klapp is saying (high resistance blocks track movement when margin × weight < resistance).

**Finding: High resistance absorbs the genre advantage entirely at median pools.**  
This confirms SIM-D-02's finding: resistance dominates track movement, especially with a sympathetic audience. This is mechanically coherent — changing Church soldiers' convictions is expected to be very hard.

**Composure:** Losing CLASH orator takes strain.  
Vaynard lost by margin 1. Strain formula: margin = composure damage = 1. Vaynard Composure: 8→7.

**State: Post-Exchange 1**  
```
Vaynard — Composure: 7 | Conviction Track: 5 (no movement)
Klapp — Composure: 10 (no change — won)
Initiative: transfers to exchange winner (Klapp won → Klapp retains)
```

---

### EXCHANGE 2

**Step 1 — Read:**

**Vaynard adjusts.** Klapp won Exchange 1 with Past. The audience is Church soldiers. Vaynard cannot win a Past argument against Klapp (11D vs 7D). He needs to shift to Cross (different genres) to prevent direct pool comparison.

[PROVISIONAL: Vaynard invokes Memory Bonus — cites the specific diagnostic finding from the Thread operation (the Gap predated the battle — evidence of pre-existing Church-adjacent activity). Memory bonus: +2D → Pool 9D.]

**Vaynard chooses: Future+Revealing** (consequentialist — "if you detain the one person who identified this Gap, what happens when RS drops and a Monstrous Incursion fires?")  
**Klapp chooses: Past+Revealing** (precedential — "canonical law requires practitioners to register with the Church.")

Different genres → **CROSS**. Each evaluated independently.

**Step 3 — Argue (CROSS):**

Vaynard's Future+Revealing:  
Pool: 9D (7+2 Memory bonus), TN7. E[net] = 9 × 0.30 = 2.7.  
Genre weight: Future = 0.5 (Church audience, Past-boosted). Orientation: Revealing = 1.0.  
Effective: 2.7 × 0.5 × 1.0 = 1.35. vs resistance 3 → **0 movement.**

Klapp's Past+Revealing:  
Pool: 11D, TN7. E[net] = 3.3.  
Genre weight: Past = 1.5. Orientation: Revealing = 1.0.  
Effective: 3.3 × 1.5 × 1.0 = 4.95. vs resistance 3 → movement = ⌊4.95 − 3⌋ = 1 toward Klapp (toward 3-end of scale).

**Conviction Track: 5 → 4 (toward Klapp victory).**

Composure (CROSS — each evaluated, but who takes strain?):  
[PARAMS GAP: CROSS composure damage — who takes strain in a CROSS interaction? No explicit rule in params. Assuming: loser of each independent evaluation takes strain proportional to margin.]  
[PROVISIONAL: CROSS — each orator takes 0 strain (both made their arguments independently; no clash).]  
→ PP-103 needed for CROSS composure rule.

**State: Post-Exchange 2**
```
Vaynard — Composure: 7 | Conviction Track: 4 (Klapp closer to winning at ≤3)
Klapp — Composure: 10 | Initiative: Klapp (exchange winner, Past moved track)
```

---

### EXCHANGE 3

**Vaynard is in trouble.** Track at 4 — one more successful Klapp exchange could push to 3 (Klapp wins). Vaynard needs to either:
a) Win a CLASH to push track back toward 7
b) Win the next CROSS exchange with a genre change

Vaynard's options are limited. His Future arguments are heavily penalised (0.5 weight). Past: Klapp dominates (11D vs 9D max). Present: Crown ethical mode (Virtue Ethics → Present) — but the audience is Church, not Crown.

[FINDING: Vaynard cannot win this debate as constructed. 11D vs 9D with Past × 1.5 (audience) favours Klapp. Future × 0.5 penalises Vaynard's strongest genre. CROSS buys time but doesn't reverse movement. Vaynard's only viable path: change the audience composition (bring in Varfell soldiers who would have Consequentialist framing → Future × 1.5), or find a mechanism to shift audience ethical mode.]

**This is a design feature, not a bug:** An outnumbered scholar arguing Future ethics to Church soldiers in a Church-framed scene should lose. The mechanics correctly produce this outcome.

**However:** Vaynard has one last option — invoke the Canon evidence of the Gap directly.

**Vaynard: "Your Eminence, there is a pre-existing Gap here — not caused by this battle. Something made it. If I leave without resolving it, you face a Monstrous Incursion within the season."**

This shifts the stakes. It's not an argument about canonical law anymore — it's a conditional threat (Incursion if Vaynard is detained). This would be a **Leverage play** — forcing a Belief/Position change through threat rather than persuasion.

[PARAMS GAP: Leverage plays in debate — using credible threat as debate move. No rule in params_debate. The debate mechanic covers Logos/Pathos/Ethos via genre, but not conditional threats with factual backing.]

**[F-HYB-03 — P2]: No mechanic for credible-evidence leverage in debate.**  
A character with specific factual evidence that changes the stakes of the debate has no designated mechanic for "conditional threat" or "evidence deposition." The Read mechanic can reveal genre preferences but not allow asymmetric information as a debate tool. The Memory Bonus (+2D) is the closest mechanic, but it applies to citing claims, not leverage.  
**Patch (editorial):** [EDITORIAL: ED-054 — Define evidence leverage mechanic in debate: when one orator presents verifiable evidence that changes the stakes of the Conviction outcome (e.g., "if you win, a structural consequence you don't want fires"), Cognition+History roll vs Ob 2. Success: audience ethical mode shifts one step toward the presenting orator's genre for the remaining debate. This preserves the genre/weight system while allowing factual evidence to matter.]  
→ ED-054 added.

[PROVISIONAL applying ED-054: Vaynard rolls Cognition (4) + History (1) = 5D vs Ob 2.  
E[net] = 5 × 0.30 = 1.5. P(≥2) ≈ 55%.  
Most likely: Partial success → Klapp's manner shifts (he's uncertain) but audience mode doesn't change. Track does not regress. Composure check deferred.  
Failure: Klapp dismisses it as practitioner manipulation. Track moves toward Klapp.]

**Most likely outcome (Partial):** Klapp is visibly unsettled. He orders the Sergeant to hold. He does not release Vaynard, but he does not press the debate to conclusion this scene. **Stalemate.**

**Conviction Track: 4 (no movement on Partial leverage). Debate ends inconclusively.**

**Debate outcome: Vaynard is detained but not killed. Klapp has insufficient canonical evidence to formally condemn him. The scene ends as Varfell forces approach — forcing both parties to withdraw.**

---

### STATE: END OF PERSONAL SCENE

```
Vaynard — Composure: 7 | Coherence: 10 | TS: 57 | Wounds: 0 | Detained (narrative state)
Klapp — Composure: 10 | Conviction Track: 4 (slight Klapp advantage, inconclusive)
RS: 68 (Gap averted by Weaving; two Relational-scale instabilities remain — flagged for future session)
TC: 34 (no change from personal scene — domain echoes queue)
Templar Sergeant: stands down on Klapp's order. No personal combat occurred.
```

---

## MODE K2 — TRANSITION: HYB → BG (ZOOM OUT)

### Zoom Out State Transfer

Per state_transfer_spec.md §1 "Zoom Out: TTRPG → BG state update":

| TTRPG Outcome | BG State Update | Applied? |
|---------------|----------------|----------|
| Unit Strength changes (combat) | Church Templar Str 7→ BG Military: [PROVISIONAL] Church Mil 3 (post-battle loss, unchanged by personal scene) | ✓ |
| Named NPC killed | N/A — no NPC killed | ✓ |
| PC Domain Action in scene | Vaynard's Weaving → Gap averted → Queue as Domain Echo | ✓ |
| Wounds taken by PC | 0 wounds — no change | ✓ |
| Thread operation RS consequence | RS unchanged (Object-scale Weaving, no RS modification) | ✓ |
| Fortification damaged | No siege | ✓ |

**Domain Echo queued:** Gap aversion in T6 → Fires at next BG Accounting. Effect: RS +0 (Object scale), but narrative consequence: the pre-existing instability is known. Flags an Investigation Action for next season (Church or Varfell can take Tribune Investigate to follow up).

**BG Domain Actions resume.** All other faction turns resume.

### Post-Zoom-Out BG State

```
TC: 34 | RS: 68 | IP: 22 | PI: 5

Church: M 4→4 (Mandate unchanged — lost battle but this was expected; −1 for diplomatic opposition = 4), 
        I 6, W 5, Mil 3 (battle loss applied), Sta 5
Varfell: M 3, I 4, W 3, Mil 4, Sta 4 (holds T6)
Crown: M 5, I 5, W 4, Mil 4, Sta 4
Hafenmark: M 4, I 4, W 5, Mil 3, Sta 4
```

**Note:** Church Mandate was 5 at season start, −1 diplomatic (PP-102 domain action result) = 4. Church Military 4→3 from battle.

---

## FINDINGS SUMMARY (Session A)

### P1 Findings

| ID | Description | Patch |
|----|-------------|-------|
| F-HYB-01 | Practitioner vs Veteran melee: no viable survival path without explicit Phase positioning rule. Scholar incapacitated R1 at ~95%. Threadwork blocked. | PP-101 |
| GAP-K2-01 | BG Military → TTRPG unit Strength conversion undefined. State transfer spec says "1:1 same scale" — incorrect. | PP-101 scope includes this |

### P2 Findings

| ID | Description | Patch |
|----|-------------|-------|
| F-HYB-02 | AMPLIFY in adversarial debate: track direction undefined when opposing orators pick same genre+orientation. | PP-102 |
| F-HYB-03 | Evidence leverage in debate: no mechanic for conditional threat backed by verifiable fact. | ED-054 (editorial) |

### Params Gaps (not P-tier findings — tooling gaps)

| ID | Description |
|----|-------------|
| PARAMS-GAP-01 | BG Battle Resolution modifier table (P-16) truncated in params_board_game.md — defender terrain bonus unconfirmed |
| PARAMS-GAP-02 | BG Battle Partial outcome — no Partial degree defined for BG Battle (only Win/Lose binary) |
| PARAMS-GAP-03 | BG "Diplomatic Opposition" mechanic — no specific domain action extracted |
| PARAMS-GAP-04 | Mass combat pool split — Offence/Defence allocation undefined for unit-scale combat |
| PARAMS-GAP-05 | Mass combat damage formula — Strength loss per excess success not defined at unit level |
| PARAMS-GAP-06 | CROSS composure damage — who takes strain in a CROSS interaction? |
| PARAMS-GAP-07 | Cardinal Klapp Attunement stat not in any NPC stat block |

### Editorial Items

| ID | Description |
|----|-------------|
| ED-054 (NEW) | Define evidence leverage mechanic in debate: verifiable-fact conditional change. Cognition+History roll to shift audience ethical mode. |

### Stale Params

| File | Issue |
|------|-------|
| params_debate.md | SIM-DEBT-01 still marked "PARTIALLY RESOLVED" — should be RESOLVED (coverage matrix confirmed SIM-D-02) |

---

## PROVISIONAL DECISIONS MADE THIS RUN

| ID | Decision |
|----|----------|
| [PROVISIONAL-HYB-01] | BG Military stat → TTRPG: Military = CP tier; Strength = Military × 2. |
| [PROVISIONAL-HYB-02] | Defender home territory = +1D to battle pool (not Ob modifier). |
| [PROVISIONAL-HYB-03] | Audience resistance = Stability÷2, round up. |
| [PROVISIONAL-HYB-04] | Mass combat pool split = ½ Offence / ½ Defence (round down Offence). |
| [PROVISIONAL-HYB-05] | Mass combat 1 excess success = 1 Strength point lost per engaged unit. |
| [PROVISIONAL-HYB-06] | CROSS composure: neither orator takes strain in CROSS (no direct clash). |
| [PROVISIONAL-HYB-07] | Evidence leverage (ED-054): Cognition+History 5D vs Ob 2. Partial = Klapp unsettled, stalemate. |

---

## SESSION B PENDING

- Mode D — Edge case discovery (9 categories)
- Mode J — Cognitive load audit (Zoom In/Out procedure + debate procedure)
- Mode L — Precedent comparison (3 analogue systems)
- Mode M — Narrative flowchart (The Templar Crossing, 3-mode branching)
- Commit Session B findings

---

## PATCHES REQUIRED (pre-commit)

### PP-101 — Practitioner Positioning Rule (Mass Combat Phase Structure)

**Finding:** F-HYB-01 / GAP-K2-01  
**Source:** SIM-HYB-01  
**Severity:** P1  
**Description:** Add explicit practitioner safe-zone rule to mass combat phase structure; define BG Military → TTRPG unit Strength conversion.  
**Affects:** designs/mass_combat/mass_battle_v3.md §Phase Structure; skills/valoria-orchestrator/references/state_transfer_spec.md §1  
**Canon risk:** NONE

### PP-102 — AMPLIFY Adversarial Direction Rule

**Finding:** F-HYB-02  
**Source:** SIM-HYB-01  
**Severity:** P2  
**Description:** In adversarial AMPLIFY, initiative holder's pool +3D; track moves toward initiative holder if net > resistance.  
**Affects:** designs/debate/debate_system_redesign_v1.md §AMPLIFY resolution  
**Canon risk:** LOW (extends, doesn't contradict)

---

## PARAMS STALE NOTES (require params update in commit)

- `params_debate.md`: Update SIM-DEBT-01 line from "PARTIALLY RESOLVED" to "RESOLVED — SIM-D-02 confirmed Mode C."
- `params_mass_combat.md`: Note PARAMS-GAP-04 and PARAMS-GAP-05 as open (unit pool split, Strength-loss formula).
- `params_scale_transitions.md`: Note GAP-K2-01 (BG Military → TTRPG unit conversion).
