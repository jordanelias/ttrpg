# Valoria BG — Conviction Track & Church Victory Redesign
## PP-406 through PP-418
## Date: 2026-04-05 | Status: Design Proposal — Awaiting User Review
## Scope: Conviction Track, Church Seizure, TC Generation, ED-110 Victory, RM Emergence, Varfell Paths B/C, Co-Victory

---

## 1. Conviction Track — Per-Territory Stat

**Name:** Conviction (CV)
**Range:** 0–5 per territory.
**Poles:** 0 = Einhir Restoration pole. 5 = Galbadian Orthodoxy pole.

**Rationale for name:** Conviction captures popular belief — what the people hold to be true. This is not institutional Church power (that is Mandate) nor theological correctness (the Church is sincerely wrong per canon). It is the strength of orthodox faith in the population. The Restoration pole is the absence of that conviction — not a competing faith, but recovered cultural memory that displaces orthodox certainty.

[EDITORIAL: ED-302 — Confirm track name "Conviction" (CV). Alternative candidates: "Devotion", "Orthodoxy", "Glaube".]

### 1.1 Starting Values (PP-406)

| T# | Territory | Controller | CV | Notes |
|----|-----------|-----------|-----|-------|
| T1 | Valorsplatz | Crown | 4 | Capital — Crown-Church symbiosis |
| T2 | Kronmark | Crown | 4 | Heartland |
| T3 | Lowenskyst | Crown | 4 | Border fortress |
| T4 | Grauwald | Varfell | 2 | Highland timber — Einhir memory persists |
| T5 | Feldmark | Crown | 3 | Breadbasket |
| T6 | Stillhelm | Crown | 3 | Southern farmland, Calamity-adjacent |
| T7 | Rendstad | Hafenmark | 3 | Timber valley |
| T8 | Gransol | Hafenmark | 3 | Hafenmark capital |
| T9 | Himmelenger | Church | 5 | Cathedral city — soft cap (can drop under pressure) |
| T10 | Spartfell | Hafenmark | 3 | Border castle |
| T11 | Halvardshelm | Varfell | 2 | Central fjords |
| T12 | Sigurdshelm | Varfell | 2 | Varfell seat |
| T13 | Oastad | Varfell | 2 | Southern fjords |
| T14 | Ehrenfeld | Crown | 4 | Military hinge |
| T15 | Southernmost | Uncontrolled | **0** | **HARD FIXED — cannot increase by any means** |
| T16 | Schoenland | Schoenland | — | Not in play |
| T17 | Halvarshelm | Hafenmark | 3 | Northern mines |

**T15 rule (PP-407):** T15 Conviction is permanently 0. No action, event, faction ability, or seasonal drift may increase it. The Calamity annihilated orthodox Piety at the Einhir epicentre. This is metaphysically irreversible — the rendering itself is compromised there (P-07).

**T9 soft cap:** Himmelenger starts at CV 5 but is not locked. Sustained pressure (Hafenmark suppression, Varfell cultural actions, RS decline) can reduce it. It does not auto-recover to 5.

### 1.2 Movement Rules (PP-408)

**Seasonal cap:** ±1 CV per territory per season. No combination of actions can move a territory's CV by more than 1 in a single season.

**Drift:** None. CV is sticky — it holds its current value unless actively pushed. Populations do not spontaneously become more or less devout. This creates strategic friction: changing conviction requires sustained factional investment.

**Exception — Calamity Drift (RS decline):** When Rendering Stability (RS) drops below a threshold, territories adjacent to T15 experience CV erosion. See §1.3.

#### Movement Actions

| Action | Faction(s) | Direction | Condition | Ob | Effect |
|--------|-----------|-----------|-----------|-----|--------|
| Preach | Church | CV +1 | Church controls or is prominent in territory | Influence vs Ob 2 | Success: CV +1 in target territory |
| Suppress Heresy | Church | CV +1 | Territory CV ≤ 2 | Influence vs Ob 3 | Success: CV +1. Failure: CV −1 (backlash) |
| Cultural Reclamation | Varfell | CV −1 | Varfell controls territory OR territory has Einhir cultural presence | Influence vs Ob 2 | Success: CV −1 in target territory |
| Community Weaving | RM (latent or active) | CV −1 | Territory CV ≤ 3 | See §5.3 | Success: CV −1 (plus RS effects per existing mechanic) |
| Secular Governance | Hafenmark | CV −1 | Hafenmark controls territory | Mandate vs Ob 2 | Success: CV −1. Cannot reduce below 2 via this action. |
| Consecrate | Church | CV +1 | Church controls territory AND CV ≥ 3 | Influence vs Ob 3 | Success: CV +1. Additionally: territory becomes Consecrated (see §1.4) |
| Missionary Work | Church | CV +1 | Territory not controlled by Church, CV ≤ 3 | Influence vs Ob = controlling faction's Mandate | Success: CV +1 in that territory |

**Frequency:** Each faction may attempt one CV movement action per season total (not per territory). Choose where to invest.

**Church prominence:** Church Mandate > controlling faction's Mandate in that territory. Required for Preach. Not required for Missionary Work (which targets territories where Church lacks prominence — hence the higher Ob).

### 1.3 Calamity Drift — RS-Linked CV Erosion (PP-409)

The Calamity's Thread damage radiates outward from the Southernmost. As RS declines, the rendering destabilises, and populations closest to the epicentre lose faith — not because they reason their way out of orthodoxy, but because the rendering itself cannot sustain the experiential certainty that grounds belief.

| RS Threshold | Effect |
|-------------|--------|
| RS ≤ 50 | Territories adjacent to T15 (T6, T13): CV −1 at Accounting if CV > 0 |
| RS ≤ 35 | All territories within 2 steps of T15: CV −1 at Accounting if CV > 0. Adjacency per map. |
| RS ≤ 20 | All territories: CV −1 at Accounting if CV > 0. Orthodoxy collapses under rendering strain. |

Calamity Drift applies after all faction actions resolve but before TC calculation. Calamity Drift ignores the ±1/season cap (it stacks with faction-driven movement). Calamity Drift cannot reduce T15 below 0 (already there) or increase any CV.

### 1.4 Consecrated Status (PP-410)

A territory that reaches CV 5 via a Consecrate action gains **Consecrated** status.

Effects:
- CV cannot drop below 4 while Church controls the territory (institutional infrastructure locks in faith).
- Church seizure Ob in this territory: −1 (population welcomes Church governance).
- Consecrated status is lost if Church loses control AND CV drops below 4.

---

## 2. Church Seizure Ob — Redesign (PP-411)

**Replaces:** Current "Fort level + 1" and the church_territorial_seizure.md TC 80 procedure.

**Trigger:** TC ≥ 75 (phase transition — see §4). Church may attempt seizure once per season per eligible territory.

**Eligibility:** Church prominent in territory (Church Mandate > controlling faction's Mandate). Church Mandate ≥ 4.

**Roll:** Church Influence vs Ob.

### Ob Formula

**Ob = Base + Fort Modifier + CV Modifier**

| Component | Value |
|-----------|-------|
| **Base** | 2 |
| **Fort Modifier** | +1 per Fortification level in territory (0–3 range) |
| **CV Modifier** | +(3 − CV), minimum 0. At CV 5: +0. At CV 4: +0. At CV 3: +0. At CV 2: +1. At CV 1: +2. At CV 0: +3. |

Simplified: **Ob = 2 + Fort Level + max(0, 3 − CV)**

| CV | CV Modifier | Interpretation |
|----|------------|----------------|
| 5 | +0 | Population fully orthodox — welcomes Church rule |
| 4 | +0 | Strong faith — minimal resistance |
| 3 | +0 | Moderate faith — acquiescent |
| 2 | +1 | Weak faith — population resists |
| 1 | +2 | Restoration-leaning — active resistance |
| 0 | +3 | Einhir restoration — seizure nearly impossible |

**Ob floor:** 1.
**Ob ceiling:** None (stacks freely).

**Additional modifiers (cumulative):**

| Condition | Modifier |
|-----------|----------|
| Consecrated territory | −1 Ob |
| AER ≥ 3 (Altonian ecclesiastical backing) | +1D to Church roll |
| Previous failed seizure on this territory this campaign | +1 Ob per failure |
| Löwenritter units present | +1 Ob |

### Seizure Results

| Degree | Outcome |
|--------|---------|
| Overwhelming | Church seizes administrative control. Controlling faction's Mandate −1 in territory. CV +1 (if below 5). PI −1. |
| Success | Church seizes administrative control. PI −1. |
| Partial | No seizure. Church Mandate +1, controlling faction Mandate −1 in that territory. |
| Failure | No seizure. Church Mandate −1 (overreach). TC −2 (visible failure undermines institutional momentum). |

**Post-seizure governance:** Church controls the territory. Church ethical framework modifiers apply to all Domain Actions in the territory. Church may Preach and Consecrate freely in controlled territories.

**Loss of seized territory:** If CV drops below 2 in a Church-controlled territory, a Stability check (Ob 2) is required at Accounting. Failure: Church loses administrative control; territory reverts to prior controller (or becomes Uncontrolled if prior controller has Mandate 0).

---

## 3. TC Generation — Redesign (PP-412)

**Replaces:** Flat passive +1/season + Piety Domain Action.

**Starting TC:** 28 (canonical BG). **Phase transition:** TC 75.

### Seasonal TC Calculation

At Accounting, TC adjusts as follows (in order):

**Step 1 — Institutional Momentum (passive):** TC +1. (Unchanged from PP-402. Church institutional presence generates baseline pressure regardless of territory holdings.)

**Step 2 — Conviction Yield:** For each territory where Church is prominent (Church Mandate > controlling faction's Mandate), add TC bonus based on that territory's CV:

| CV | TC Yield |
|----|----------|
| 5 | +1 |
| 4 | +0.5 (track half-steps; round down total across all territories) |
| 3 | +0 |
| 2 | +0 |
| 1 | +0 |
| 0 | +0 |

**Total Conviction Yield = floor(Σ yield across all prominent territories)**

Maximum theoretical Conviction Yield per season: if Church is prominent in all 15 eligible territories (implausible), and all are CV 5: +15. Realistic early game: prominent in T9 (CV 5) + maybe T1, T2 (CV 4): +1 + 0.5 + 0.5 = floor(2) = +2.

**Step 3 — Assert (optional Church action):** Church may spend a Standard Action to Assert. Roll: Influence vs Ob 2. Success: TC +1 (in addition to Steps 1–2). Failure: no additional TC; Stability −1 (PP-403 applies).

**Step 4 — Suppress (optional opponent action):** One opposing faction may spend a Standard Action to Suppress. Roll: Mandate vs Ob = Church Mandate. Success: negate Step 1 passive +1 for this season only. Does not affect Conviction Yield or Assert. Failure: no effect; Stability −1 (PP-403 applies).

**Step 5 — Hafenmark Structural Suppression:** While Baralta's Mandate ≥ 4: TC −1/season (existing mechanic, unchanged). Excommunication of Baralta: TC +4 immediately (unchanged).

### Piety Domain Action — DISSOLVED

The old Piety Domain Action (Mandate pool, TN 7, Ob 2, TC +1) is replaced by the Conviction Yield system + Assert action. There is no separate "Piety Domain Action" in the redesigned system.

### TC Pacing Analysis

Early game (S1–S5): Church prominent in ~1–2 territories (T9 at CV 5). TC gain ≈ +1 (passive) +1 (CV yield from T9) −1 (Hafenmark suppress if Baralta active) = +1/season. TC at S5 ≈ 33.

Mid game (S6–S12): Church expands prominence via Mandate growth, Preaching raises CV. Prominent in 3–5 territories, some at CV 4–5. TC gain ≈ +1 +2 −1 = +2/season. TC at S12 ≈ 47.

Late game (S13–S20): Church at peak prominence, 5–8 territories, active Preaching. TC gain ≈ +1 +3 = +4/season (Hafenmark suppression may have ended). TC 75 reached ~S20.

This gives a 20-season timeline to TC 75 under active Church play with moderate opposition — consistent with a full campaign.

[GAP: TC pacing needs simulation with actual faction AI behavior to validate 20-season estimate. Flag for SIM-DEBT.]

---

## 4. Church Victory Conditions — ED-110 Resolution (PP-413)

### 4.1 Primary Victory — Territorial Consolidation

**Phase 1 — Accumulation (TC 0–74):** Church accumulates TC through institutional momentum, Conviction Yield, and Assert actions. This phase is passive/incremental.

**Phase 2 — Consolidation (TC ≥ 75):** Church shifts to territorial seizure. TC stops advancing (capped at 75). The counter is no longer relevant — the game is now about holding territory.

[EDITORIAL: ED-303 — Does TC freeze at 75 or continue advancing? Freezing creates cleaner phase transition. Continuing creates pressure for other factions to suppress even post-75. Recommend freeze.]

**Victory condition:** Church holds territories whose Territory Consolidation Values (TCV) sum to ≥ **18**.

**Territory Consolidation Values (user-confirmed):**

| Territory | TCV | Notes |
|-----------|-----|-------|
| T1 — Valorsplatz | 5 | Capital — seat of Crown-Church symbiosis |
| T8 — Gransol | 3 | Hafenmark capital — symbolic conquest |
| T12 — Sigurdshelm | 3 | Varfell seat — ecclesiastical reach into the fjords |
| T3 — Lowenskyst | 2 | Border fortress — military dominance |
| T14 — Ehrenfeld | 2 | Military hinge — strategic control |
| All others (10 territories) | 1 each | T2, T4, T5, T6, T7, T10, T11, T13, T17 |
| T15 — Southernmost | **0** | Cannot be seized. Not counted. |
| T16 — Schoenland | **—** | Not in play. |
| **Total available** | **25** | |

**Victory threshold: 18.** This requires either:
- Both high-TCV targets (Valorsplatz + Gransol or Sigurdshelm) + several standard territories, OR
- One high-TCV target + all secondary targets + many standard territories.

18/25 = 72% of available consolidation value. The Church cannot win by cherry-picking — it must achieve broad territorial dominance. But it need not hold everything.

**Holding requirement:** Church must hold qualifying territories for **2 consecutive seasons** after reaching ≥ 18 TCV. This prevents flash seizures from counting as victory.

**Erosion:** If CV drops below 2 in a Church-held territory, Stability check required (see §2). Loss of territory reduces TCV sum — Church can lose its victory position.

### 4.2 Alternate Victory — Altonian Theocracy Path (PP-414)

**Concept:** The Church works with its Altonian branch to create a cross-border ecclesiastical authority that supersedes national governance in both Valoria and Altonia. This is institutional, not military — Altonia is not conquerable territory.

**Mechanic:** Altonian Ecclesiastical Accord (AEA) clock. Range: 0–5.

**Starting value:** 0.

**Advancement conditions (each advances AEA by +1, each may fire at most once per season):**

| Condition | AEA +1 |
|-----------|--------|
| TC ≥ 50 AND AER ≥ 3 | Church's Valoria-side institutional weight + Altonian diplomatic backing |
| Church controls ≥ 3 territories | Territorial proof of governance capability |
| Church Mandate ≥ 6 | Peak institutional authority |
| Crown Mandate ≤ 2 | Secular authority has collapsed |
| IP ≥ 60 (Altonian pressure high) | Altonian branch leverages invasion threat to force ecclesiastical unification |

**AEA reduction:**
- Hafenmark Sovereign Authority Doctrine success: AEA −1.
- Crown Royal Decree targeting Church: AEA −1.
- AER drops below 2: AEA resets to 0 (Altonian branch withdraws).

**Victory:** AEA reaches 5 AND TC ≥ 60 AND Church controls Himmelenger (T9). The Church declares Ecclesiastical Primacy — a transnational theocracy with Himmelenger as its capital. Valoria and the Altonian Church territories form a single ecclesiastical jurisdiction.

**Interaction with Primary path:** AEA and TC accumulation run in parallel. The Church player can pursue either or both. AEA victory requires less territorial control (only T9 mandatory) but more diplomatic conditions.

### 4.3 Hollow Victory — Church + Hafenmark (PP-415)

**Trigger conditions (all must be met simultaneously):**
- Crown Mandate ≤ 1
- TC ≥ 50
- Church controls ≥ 2 territories
- Hafenmark controls ≥ 3 territories
- No active military conflict between Church and Hafenmark

**Outcome:** Crown is functionally dissolved. Church and Hafenmark partition Valoria — Church governs spiritual/cultural sphere, Hafenmark governs civil/economic sphere. Neither achieves full victory. The Hollow Victory is declared at Accounting when all conditions are met; it is a game-ending state but neither faction scores a solo win.

**Narrative:** This is the "comfortable authoritarian duopoly" ending. The Church gets institutional permanence without theocracy; Hafenmark gets mercantile freedom without democratic accountability. Both suppress the Restoration Movement and Varfell. The Southernmost is ignored.

[EDITORIAL: ED-304 — Is the Hollow Victory a "win" for both players or a "draw"? Recommend: both score it as a conditional victory — better than a loss, worse than a solo win.]

---

## 5. RM Emergence as Latent Faction (PP-416)

### 5.1 Varfell-RM Relationship Track

**Name:** Warden's Accord (WA). Range: −3 to +3. Starting value: 0.

**Poles:**
- +3 = Cultivation. Vaynard is the Restoration Movement's champion. RM supports Varfell.
- 0 = Neutral. RM is ambient — neither allied nor hostile.
- −3 = Alienation. Vaynard has exploited or suppressed the movement. RM turns hostile.

**Movement:**

| Action / Event | WA Change |
|----------------|-----------|
| Varfell Cultural Reclamation in own territory (success) | WA +1 |
| Varfell protects a practitioner from Church persecution (narrative trigger) | WA +1 |
| Varfell uses Thread operations in Varfell territory AND VTM is public (≥ 3) | WA +1 (once only — first reveal) |
| Varfell seizes territory from another faction using military force | WA −1 |
| Varfell raises CV in own territory (via any means) | WA −1 |
| Varfell allies with Church (formal alliance declared) | WA −2 (immediate) |
| Varfell suppresses Community Weaving in own territory | WA −1 |
| RS drops below 50 while Varfell controls T13 | WA −1 (Einhir sites destabilise; movement blames Varfell inaction) |

**Seasonal cap:** ±1 WA per season (same discipline as CV).

**WA does not track separately from CV.** WA is Vaynard's political relationship with the movement; CV is the population's faith level. They interact but are independent stats.

### 5.2 Emergence Trigger

RM **emerges as an active NPC faction** when ALL of the following are true at Accounting:

1. WA ≤ −2 (Varfell has alienated the movement)
2. At least 3 territories have CV ≤ 1
3. RS ≤ 50 (rendering instability feeds cultural desperation)

When RM emerges, it becomes a fully active NPC faction with stats, actions, and territorial ambitions.

**One-shot:** Emergence fires once. If RM is suppressed back to latency (see §5.4), it cannot re-emerge.

### 5.3 Active RM — Stats and Actions

**Starting Stats (on emergence):**

| Stat | Value | Derivation |
|------|-------|------------|
| Mandate | Count of territories with CV ≤ 1 (min 2, max 5) | Popular mandate from low-conviction populations |
| Influence | 4 | Grassroots network |
| Wealth | 1 | No institutional backing |
| Military | 0 | Non-violent movement |
| Stability | 3 | Decentralised resilience |

**Ethical Framework:** Rawlsian Social Contract (unchanged from stage6 design). −1 Ob for actions benefiting common population; +1 Ob for actions concentrating power.

**NPC AI priority:** Reduce CV in adjacent territories. Protect RS. Oppose Church and any faction with Mandate ≥ 5.

**Actions (once per season, NPC-controlled):**

| Action | Roll | Effect |
|--------|------|--------|
| Community Weaving | Influence vs Ob = Thread Tension ÷ 20 (round up, min 1). Requires practitioner TS 30+ affiliated. | Overwhelming: RS +2, CV −1 in target territory. Success: RS +1, CV −1. Partial: no effect. Failure: Stability −1, RS −1. Co-Movement card drawn. |
| Grassroots Organising | Influence vs Ob 2 | Success: RM Mandate +1 in one territory with CV ≤ 2. Caps at Mandate 5. |
| Resist Seizure | Influence vs Church Influence | When Church attempts seizure in territory with CV ≤ 2: RM adds +1 Ob to Church seizure roll. Passive — does not consume RM's action. |

**Territory presence:** Active RM has presence in every territory with CV ≤ 1. RM does not control territory — it exerts influence within it. RM presence adds +1 Ob to any Church action in that territory.

### 5.4 Suppression and Resolution

**Suppression:** RM can be suppressed back to latency if:
- WA returns to ≥ 0 (Varfell reconciles), OR
- All territories rise to CV ≥ 2 (movement loses popular base), OR
- RM Stability reaches 0 (movement collapses internally).

**Suppression does not restore RM to its pre-emergence state.** Territories retain their CV values. The movement simply ceases to act as an organised faction.

**If RM is never suppressed:** It persists as a permanent NPC faction for the remainder of the campaign. It cannot achieve a solo victory — it is a spoiler faction that complicates Church, Varfell, and Crown objectives.

---

## 6. Varfell Paths B & C — Redesign (PP-417)

### 6.1 Path B — Southernmost Dominion (full redesign)

**Deed structure: 3 Deeds. All must be completed.**

| Deed | Condition | Gate |
|------|-----------|------|
| **Deed 1 — Extend the Reach** | Control T13 (Oastad) + garrison or Tribune present in T15 (Southernmost) simultaneously for 2 consecutive seasons. | VTM ≥ 2 (must have Thread awareness to engage the Southernmost meaningfully). |
| **Deed 2 — Walk the Wound** | Complete a Southernmost Expedition (existing mechanic) with Vaynard's personal participation. Pass the Forgetting Check. | VTM ≥ 3. Warden Cooperation ≥ 1. |
| **Deed 3 — Keeper's Mandate** | Hold T13 at CV ≤ 1 AND WA ≥ +1 for 2 consecutive seasons. | VTM ≥ 3. The movement must trust Vaynard — this cannot be achieved if RM has emerged as hostile. |

**Path B is blocked if:** RM has emerged (WA ≤ −2). Once RM emerges, Deed 3 is mechanically impossible (WA cannot reach +1 while RM is active and hostile). Varfell must prevent Emergence to keep Path B open.

**Design logic:** Path B tests whether Vaynard can be a genuine steward of the Southernmost — Thread-aware (VTM ≥ 3), trusted by the Restoration Movement (WA ≥ +1), and willing to sustain low-conviction Einhir culture in his own territories (CV ≤ 1 in T13).

### 6.2 Path C — Thread Supremacy (territory name correction + validation)

**Deed structure: 3 Deeds. Unchanged except territory references.**

| Deed | Condition | Gate |
|------|-----------|------|
| **Deed 1 — Thread Mastery** | VTM = 5. | — |
| **Deed 2 — Territorial Command** | Control T4 (Grauwald) + T13 (Oastad) + ≥ 1 other territory simultaneously. | — |
| **Deed 3 — World Intact** | RS ≥ 50 at the moment of victory declaration. | — |

**Corrections applied:** T4 = Grauwald (was "Vargstad"). T13 = Oastad (was "Stillhelm"). Deed structure is otherwise sound — VTM 5 is a genuine multi-season investment (minimum ~S14–S16 to achieve), territorial control is non-trivial, and RS ≥ 50 creates tension with Thread operations that degrade RS.

**No further changes required for Path C.**

---

## 7. Co-Victory Replacement — Varfell + RM (PP-418)

**Old co-victory (DISSOLVED):** Varfell Thread Supremacy + Restoration Network Victory (both RS ≥ 50). Invalid — RM is no longer a primary faction with its own victory path.

**Replacement: Einhir Restoration Co-Victory**

**Conditions (all must be met simultaneously):**

| Condition | Faction Responsible |
|-----------|-------------------|
| VTM ≥ 4 | Varfell |
| WA ≥ +2 | Varfell (cultivation choices) |
| ≥ 4 territories at CV ≤ 1 | Both (Varfell Cultural Reclamation + latent RM Community Weaving) |
| RS ≥ 40 | Both (Community Weaving sustains RS; Varfell Thread operations must not collapse it) |
| Warden Cooperation ≥ 2 | Varfell |
| Vaynard controls T13 (Oastad) | Varfell |

**Narrative:** Vaynard and the Restoration Movement together recover enough Einhir cultural memory to create a viable alternative to Galbadian orthodoxy, while keeping the rendering stable enough for the world to survive the transition. The Wardens recognise Vaynard as a legitimate steward of the Southernmost.

**Scoring:** This is a co-victory — Varfell player scores a win. RM (latent NPC faction) does not "win" in the scoring sense, but the narrative outcome is positive for the movement. If RM has emerged as hostile, this co-victory is impossible (WA ≥ +2 cannot coexist with active hostile RM).

---

## 8. Resolved Editorial Items

| ED | Resolution | Patch |
|----|-----------|-------|
| ED-110 | **Resolved.** Church victory is TC 75 phase transition → territorial consolidation (TCV ≥ 18 for 2 seasons). Alternate: Altonian Theocracy (AEA = 5). Hollow: Church + Hafenmark partition. | PP-413, PP-414, PP-415 |
| ED-112 | **Closed.** Hafenmark −1/season vs Church +1/season is a pacing concern under old system. Under new TC generation (Conviction Yield + Assert), the interaction is richer: Hafenmark suppression negates passive +1 but cannot touch Conviction Yield. No longer a deadlock risk. | — |
| ED-111 | **Superseded** by PP-412 (TC generation redesign). Old Piety Domain Action dissolved; replaced by Conviction Yield + Assert. | PP-412 |

**New editorial items raised:**

| ED | Description | Priority |
|----|-------------|----------|
| ED-302 | Confirm track name "Conviction" (CV) | P2 |
| ED-303 | Does TC freeze at 75 or continue advancing? Design recommends freeze. | P1 |
| ED-304 | Hollow Victory scoring — co-win or draw? Design recommends conditional victory for both. | P2 |
| ED-305 | Varfell-RM Relationship Track (Warden's Accord) starting value — 0 is proposed. Confirm. | P2 |

---

## 9. Gaps Identified

| Gap | Description |
|-----|-------------|
| [GAP: TC pacing — no simulation] | TC 75 timeline estimate (~S20) is analytical only. Needs simulation with faction AI to validate. Flag as SIM-DEBT. |
| [GAP: AEA pacing — no simulation] | Altonian Theocracy clock has 5 advancement conditions. Needs simulation to confirm it is achievable but not trivial. |
| [GAP: RM emergence frequency] | The triple condition (WA ≤ −2, 3 territories CV ≤ 1, RS ≤ 50) may be too restrictive or too permissive. Needs stress test. |
| [GAP: Community Weaving dual effect] | Community Weaving now affects both RS and CV. Need to verify this does not create a positive feedback loop (low CV → more Weaving → lower CV → more RM power). |
| [GAP: Consecrated status interaction with seizure] | Consecrated territories get −1 Ob on seizure but also require CV ≥ 5 via Consecrate action. This may make high-CV territories too easy to seize. Needs edge case check. |
| [GAP: Hafenmark Secular Governance floor] | Secular Governance cannot reduce CV below 2. Is this the right floor? If Hafenmark wants to support RM, they may need to push lower. |
| [GAP: Fort Level data] | Seizure Ob formula uses Fort Level (0–3). Confirm which territories have which Fort Levels — not in handoff. |

---

## 10. Patch Summary

| PP | Scope | Description |
|----|-------|-------------|
| PP-406 | Track | Conviction (CV) starting values — 15 eligible territories, 0–5 range |
| PP-407 | Track | T15 hard fix rule — CV permanently 0, no exceptions |
| PP-408 | Track | CV movement rules — faction actions, frequency, seasonal cap ±1 |
| PP-409 | Track | Calamity Drift — RS-linked CV erosion at RS ≤ 50/35/20 |
| PP-410 | Track | Consecrated status — CV 5 via Consecrate action, floor of 4 while Church controls |
| PP-411 | Seizure | Church Seizure Ob = 2 + Fort Level + max(0, 3 − CV). Prominence required. |
| PP-412 | TC | TC generation redesign — passive +1, Conviction Yield, Assert, Suppress, Hafenmark structural |
| PP-413 | Victory | Church Primary Victory — TC 75 phase transition, TCV ≥ 18 for 2 seasons |
| PP-414 | Victory | Altonian Theocracy Path — AEA clock 0–5, victory at AEA 5 + TC ≥ 60 + hold T9 |
| PP-415 | Victory | Hollow Victory — Church + Hafenmark partition, Crown Mandate ≤ 1 |
| PP-416 | RM | RM Emergence — Warden's Accord track, triple-condition trigger, active NPC rules |
| PP-417 | Varfell | Path B redesign (3 Deeds) + Path C territory correction |
| PP-418 | Co-Victory | Einhir Restoration Co-Victory — Varfell + latent RM, 6 conditions |
