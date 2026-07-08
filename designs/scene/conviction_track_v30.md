<!-- SKELETON — mechanical spec only — atomized 2026-04-13 -->
<!-- Infill: conviction_track_v30_infill.md -->

<!-- v30 baseline — renamed from designs/conviction_track/opus_design_proposal.md on 2026-04-13 -->
# Valoria BG — Piety Track & Church Victory Redesign
## PP-406 through PP-418
## Date: 2026-04-05 | Status: CANONICAL — approved 2026-04-17 (editorial batch acceptance) | Solmund correction applied | Sections §4.2, §4.3, §6, §7 SUPERSEDED-BY GD-1 (2026-05-17 — peninsula-only victory)2026-04-17 (ED-643)
## Scope: Piety Track, Church Seizure, CI Generation, ED-110 Victory, RM Emergence, Varfell Paths B/C, Co-Victory

> **Glossary note:** **CI** = Church Influence (Church institutional advancement clock, 0–100;
> renamed from **Theocracy Counter (TC)**). Piety Track (PT) is always written in full.
> **Citation corrected 2026-07-08 (ED-IN-0029 docket, OPT-AV-7):** this note previously read
> "renamed from Church Influence per ED-782" — self-referential nonsense (fixed to name the actual
> predecessor, TC) — and cited a second ID, "ED-756", that does not exist anywhere in
> `canon/editorial_ledger.jsonl`. ED-782 itself IS a confirmed, already-flagged double-booked ID
> (`_migration_flag: "ID-CONFLICT: multiple distinct descriptions — Jordan resolve"`, with an
> `_migration_alt` note referencing exactly this TC→CI glossary rename) — not re-resolved here;
> cited as the known-conflicted ID it is, not asserted as clean.

---

## 1. Piety Track — Per-Territory Stat

**Name:** Conviction (PT)
**Range:** 0–5 per territory.
**Poles:** 0 = Einhir Restoration pole. 5 = Solmund Orthodoxy pole.


[EDITORIAL: ED-302 — Confirm track name "Conviction" (PT). Alternative candidates: "Devotion", "Orthodoxy", "Glaube".]

[EDITORIAL: ED-644 — PT ≡ PT terminology equivalence (2026-04-17). Conviction (PT) here is the same per-territory stat as Piety (PT) in tc_political_redesign_v30 §1. Newer design docs prefer "PT" terminology; this file retains "PT" for skeleton stability. Full rename (PT → PT, file rename conviction_track_v30.md → piety_track_v30.md) deferred to future cleanup pass. Mechanical equivalence: use PT rules in tc_political_redesign when conflict arises.]

### 1.1 Starting Values (PP-406)

| T# | Territory | Controller | PT | Notes |
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

**T9 soft cap:** Himmelenger starts at PT 5 but is not locked. Sustained pressure (Hafenmark suppression, Varfell cultural actions, MS decline) can reduce it. It does not auto-recover to 5.

### 1.2 Movement Rules (PP-408)

**Seasonal cap:** ±1 PT per territory per season. No combination of actions can move a territory's PT by more than 1 in a single season.


**Exception — Calamity Drift (MS decline):** When Mending Stability (MS) drops below a threshold, territories adjacent to T15 experience PT erosion. See §1.3.

#### Movement Actions

| Action | Faction(s) | Direction | Condition | Ob | Effect |
|--------|-----------|-----------|-----------|-----|--------|
| Preach | Church | PT +1 | Church controls or is prominent in territory | Influence vs Ob 2 | Success: PT +1 in target territory |
| Suppress Heresy | Church | PT +1 | Territory PT ≤ 2 | Influence vs Ob 3 | Success: PT +1. Failure: PT −1 (backlash) |
| Cultural Reclamation | Varfell | PT −1 | Varfell controls territory OR territory has Einhir cultural presence | Influence vs Ob 2 | Success: PT −1 in target territory |
| Community Weaving | RM (latent or active) | PT −1 | Territory PT ≤ 3 | See §5.3 | Success: PT −1 (plus MS effects per existing mechanic) |
| Secular Governance | Hafenmark | PT −1 | Hafenmark controls territory | Mandate vs Ob 2 | Success: PT −1. Cannot reduce below 2 via this action. |
| Consecrate | Church | PT +1 | Church controls territory AND PT ≥ 3 | Influence vs Ob 3 | Success: PT +1. Additionally: territory becomes Consecrated (see §1.4) |
| Missionary Work | Church | PT +1 | Territory not controlled by Church, PT ≤ 3 | Influence vs Ob = controlling faction's Mandate | Success: PT +1 in that territory |


**Church prominence:** Church Mandate > controlling faction's Mandate in that territory. Required for Preach. Not required for Missionary Work (which targets territories where Church lacks prominence — hence the higher Ob).

### 1.3 Calamity Drift — MS-Linked PT Erosion (PP-409)


| MS Threshold | Effect |
|-------------|--------|
| MS ≤ 50 | Territories adjacent to T15 (T6, T13): PT −1 at Accounting if PT > 0 |
| MS ≤ 35 | All territories within 2 steps of T15: PT −1 at Accounting if PT > 0. Adjacency per map. |
| MS ≤ 20 | All territories: PT −1 at Accounting if PT > 0. Orthodoxy collapses under rendering strain. |

Calamity Drift applies after all faction actions resolve but before CI calculation. Calamity Drift ignores the ±1/season cap (it stacks with faction-driven movement). Calamity Drift cannot reduce T15 below 0 (already there) or increase any PT.

### 1.3b Thread Operation PT Drift (ED-676)

Visible Thread operations in a territory shift PT:

| Thread Event | PT Change | Condition |
|---|---|---|
| Public Dissolution | PT −1 | Witnesses present. Thread reality undeniable. |
| Public Mending | No change | Ambiguous: Church claims miracle; practitioners claim mastery. |
| Public Weaving (non-harmful) | PT −0.5 (rounded at Accounting) | Mild exposure. Accumulates slowly. |
| Visible Rendering Crisis | PT +1 | Thread danger reinforces Church framework. |
| Monstrous Incursion (spontaneous, from radiation) | PT −1 | Substrate instability visible beyond Church explanation. |

**Scope:** "Public" = witnessed by non-practitioner NPCs. Concealed operations (threadwork_v30 §2.3) do not trigger.

**Interaction with Calamity Drift (§1.3):** Stacks. Both fire at Accounting. Cap: PT ±2 per territory per season from Thread sources (Calamity Drift + Thread Operation Drift combined).

### 1.4 Consecrated Status (PP-410)

A territory that reaches PT 5 via a Consecrate action gains **Consecrated** status.

Effects:
- Church seizure Ob in this territory: −1 (population welcomes Church governance).
- Consecrated status is lost if Church loses control AND PT drops below 4.

---

## 2. Church Seizure Ob — Redesign (PP-411)

**Replaces:** Current "Fort level + 1" and the church_territorial_seizure.md CI 80 procedure.

**Trigger:** CI ≥ 75 (phase transition — see §4). Church may attempt seizure once per season per eligible territory.

**Eligibility:** Church prominent in territory (Church Mandate > controlling faction's Mandate). Church Mandate ≥ 4.

**Roll:** Church Influence vs Ob.

### Ob Formula

**Ob = Base + Fort Modifier + PT Modifier**

| Component | Value |
|-----------|-------|
| **Base** | 2 |
| **Fort Modifier** | +1 per Fortification level in territory (0–3 range) |
| **PT Modifier** | +(3 − PT), minimum 0. At PT 5: +0. At PT 4: +0. At PT 3: +0. At PT 2: +1. At PT 1: +2. At PT 0: +3. |

Simplified: **Ob = 2 + Fort Level + max(0, 3 − PT)**

| PT | PT Modifier | Interpretation |
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
| Altonian diplomacy ≥ 3 (Altonian ecclesiastical backing) | +1D to Church roll |
| Previous failed seizure on this territory this campaign | +1 Ob per failure |
| Löwenritter units present | +1 Ob |

### Seizure Results

| Degree | Outcome |
|--------|---------|
| Overwhelming | Church seizes administrative control. Controlling faction's Mandate −1 in territory. PT +1 (if below 5). PI −1. |
| Success | Church seizes administrative control. PI −1. |
| Partial | No seizure. Church Mandate +1, controlling faction Mandate −1 in that territory. |
| Failure | No seizure. Church Mandate −1 (overreach). CI −2 (visible failure undermines institutional momentum). |


**Loss of seized territory:** If PT drops below 2 in a Church-controlled territory, a Stability check (Ob 2) is required at Accounting. Failure: Church loses administrative control; territory reverts to prior controller (or becomes Uncontrolled if prior controller has Mandate 0).

---

## 3. CI Generation — Redesign (PP-412)

**Replaces:** Flat passive +1/season + Piety Domain Action.

**Starting CI:** 28 (canonical BG). **No phase-transition freeze** — CI runs to 100 with no freeze (PP-421 superseded the CI-75 freeze; see ci_political_v30 §0/§2.1/§7.6). *(This doc lagged that supersession; propagated 2026-07-07.)*

### Seasonal CI Calculation

At Accounting, CI adjusts as follows (in order):

**Step 1 — Institutional Momentum (passive):** CI +1. (Unchanged from PP-402. Church institutional presence generates baseline pressure regardless of territory holdings.)

**Step 2 — Conviction Yield:** For each territory where Church is prominent (Church Mandate > controlling faction's Mandate), add CI bonus based on that territory's PT:

| PT | CI Yield |
|----|----------|
| 5 | +1 |
| 4 | +0.5 (track half-steps; round down total across all territories) |
| 3 | +0 |
| 2 | +0 |
| 1 | +0 |
| 0 | +0 |

**Total Conviction Yield = floor(Σ yield across all prominent territories)**

Maximum theoretical Conviction Yield per season: if Church is prominent in all 15 eligible territories (implausible), and all are PT 5: +15. Realistic early game: prominent in T9 (PT 5) + maybe T1, T2 (PT 4): +1 + 0.5 + 0.5 = floor(2) = +2.

**Step 3 — Assert (optional Church action):** Church may spend a Standard Action to Assert. Roll: Influence vs Ob 2. Success: CI +1 (in addition to Steps 1–2). Failure: no additional CI; Stability −1 (PP-403 applies).

**Step 4 — Suppress (optional opponent action):** One opposing faction may spend a Standard Action to Suppress. Roll: Mandate vs Ob = Church Mandate. Success: negate Step 1 passive +1 for this season only. Does not affect Conviction Yield or Assert. Failure: no effect; Stability −1 (PP-403 applies).

**Step 5 — Hafenmark Structural Suppression:** While Baralta's Mandate ≥ 4: CI −1/season (existing mechanic, unchanged). Excommunication of Baralta: CI +4 immediately (unchanged).

### Piety Domain Action — DISSOLVED

The old Piety Domain Action (Mandate pool, TN 7, Ob 2, CI +1) is replaced by the Conviction Yield system + Assert action. There is no separate "Piety Domain Action" in the redesigned system.

### CI Pacing Analysis

Early game (S1–S5): Church prominent in ~1–2 territories (T9 at PT 5). CI gain ≈ +1 (passive) +1 (PT yield from T9) −1 (Hafenmark suppress if Baralta active) = +1/season. CI at S5 ≈ 33.

Mid game (S6–S12): Church expands prominence via Mandate growth, Preaching raises PT. Prominent in 3–5 territories, some at PT 4–5. CI gain ≈ +1 +2 −1 = +2/season. CI at S12 ≈ 47.

Late game (S13–S20): Church at peak prominence, 5–8 territories, active Preaching. CI gain ≈ +1 +3 = +4/season (Hafenmark suppression may have ended). ~~CI 75 reached ~S20.~~ **[STALE — assumes the superseded CI-75 freeze model (PP-421 struck); no canonical CI-100 pacing estimate exists yet.]**

~~This gives a 20-season timeline to CI 75 under active Church play with moderate opposition — consistent with a full campaign.~~ **[STALE — the CI-75 endpoint is superseded by the CI-100 no-freeze model (PP-421); pacing needs re-derivation against CI-100.]**

[GAP: CI pacing needs simulation with actual faction AI behavior to validate 20-season estimate. Flag for SIM-DEBT.]

---

## 4. Church Victory Conditions — ED-110 Resolution (PP-413)

### 4.1 Primary Victory — Territorial Consolidation

> **⚠️ SUPERSEDED (2026-07-07, CI-75→CI-100 propagation).** This Church "Primary Victory — Territorial Consolidation" framing is superseded twice over: **(1) PP-421** — CI runs **0–100, no freeze** (the "Phase 2, CI capped at 75" model below is struck; milestones now 40/55/65/80/100 per ci_political_v30 §2.1; Mass Seizure is a one-shot at CI ≥ 60 per victory_v30 §3.2; a Theocracy Unification Attempt fires at CI 100 per ci_political_v30 §2.2); and **(2) GD-1 / ED-NEW-CI-10** — no faction-specific victory survives, **Peninsular Sovereignty is the sole win path** (ci_political_v30 §7.1), so this entire §4 Church-victory apparatus is historical. **ED-303 (freeze at 75?) — RESOLVED-BY-SUPERSESSION:** the shipped answer is "no freeze, CI runs to 100" (PP-421), the opposite of this note's original "Recommend freeze." NOTE: the GD-1 propagation checklist (canon/02_canon_constraints.md §B) lists §4.2/§4.3/§6.1/§6.2/§7 for [SUPERSEDED-BY: GD-1] strikes but omits §4.1 — whether §4.1 belongs on that ratified checklist is flagged (CI75-11) for a dedicated GD-1 session, not decided here.

*Original Phase-1/Phase-2 text retained for history:*

**Phase 1 — Accumulation (CI 0–74):** Church accumulates CI through institutional momentum, Conviction Yield, and Assert actions. This phase is passive/incremental.

**Phase 2 — Consolidation (CI ≥ 75):** Church shifts to territorial seizure. CI stops advancing (capped at 75). The counter is no longer relevant — the game is now about holding territory.


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



**Erosion:** If PT drops below 2 in a Church-held territory, Stability check required (see §2). Loss of territory reduces TCV sum — Church can lose its victory position.

### 4.2 Alternate Victory — Altonian Theocracy Path (PP-414)
> **[SUPERSEDED-BY: GD-1]** Canon §B GD-1 (peninsula-only victory; see `canon/02_canon_constraints.md`) STRIKES this section. Content preserved as supersession-trail evidence. Date: 2026-05-17.



**Mechanic:** Altonian Ecclesiastical Accord (AEA) clock. Range: 0–5.

**Starting value:** 0.

**Advancement conditions (each advances AEA by +1, each may fire at most once per season):**

| Condition | AEA +1 |
|-----------|--------|
| CI ≥ 50 AND Altonian diplomacy ≥ 3 | Church's Valoria-side institutional weight + Altonian diplomatic backing |
| Church controls ≥ 3 territories | Territorial proof of governance capability |
| Church Mandate ≥ 6 | Peak institutional authority |
| Crown Mandate ≤ 2 | Secular authority has collapsed |
| IP ≥ 60 (Altonian pressure high) | Altonian branch leverages invasion threat to force ecclesiastical unification |

**AEA reduction:**
- Hafenmark Sovereign Authority Doctrine success: AEA −1.
- Crown Royal Decree targeting Church: AEA −1.
- Altonian diplomacy drops below 2: AEA resets to 0 (Altonian branch withdraws).

**Victory:** AEA reaches 5 AND CI ≥ 60 AND Church controls Himmelenger (T9). The Church declares Ecclesiastical Primacy — a transnational theocracy with Himmelenger as its capital. Valoria and the Altonian Church territories form a single ecclesiastical jurisdiction.

**Interaction with Primary path:** AEA and CI accumulation run in parallel. The Church player can pursue either or both. AEA victory requires less territorial control (only T9 mandatory) but more diplomatic conditions.

### 4.3 Hollow Victory — Church + Hafenmark (PP-415)
> **[SUPERSEDED-BY: GD-1]** Canon §B GD-1 (peninsula-only victory; see `canon/02_canon_constraints.md`) STRIKES this section. Content preserved as supersession-trail evidence. Date: 2026-05-17.


**Trigger conditions (all must be met simultaneously):**
- Crown Mandate ≤ 1
- CI ≥ 50
- Church controls ≥ 2 territories
- Hafenmark controls ≥ 3 territories
- No active military conflict between Church and Hafenmark




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
| Varfell raises PT in own territory (via any means) | WA −1 |
| Varfell allies with Church (formal alliance declared) | WA −2 (immediate) |
| Varfell suppresses Community Weaving in own territory | WA −1 |
| MS drops below 50 while Varfell controls T13 | WA −1 (Einhir sites destabilise; movement blames Varfell inaction) |

**Seasonal cap:** ±1 WA per season (same discipline as PT).

**WA does not track separately from PT.** WA is Vaynard's political relationship with the movement; PT is the population's faith level. They interact but are independent stats.

### 5.2 Emergence Trigger

RM **emerges as an active NPC faction** when ALL of the following are true at Accounting:

1. WA ≤ −2 (Varfell has alienated the movement)
2. At least 3 territories have PT ≤ 1
3. MS ≤ 50 (rendering instability feeds cultural desperation)



### 5.3 Active RM — Stats and Actions

**Starting Stats (on emergence):**

| Stat | Value | Derivation |
|------|-------|------------|
| Mandate | Count of territories with PT ≤ 1 (min 2, max 5) | Popular mandate from low-conviction populations |
| Influence | 4 | Grassroots network |
| Wealth | 1 | No institutional backing |
| Military | 0 | Non-violent movement |
| Stability | 3 | Decentralised resilience |

**Ethical Framework:** Equity Social Contract (unchanged from stage6 design). −1 Ob for actions benefiting common population; +1 Ob for actions concentrating power.

**NPC AI priority:** Reduce PT in adjacent territories. Protect MS. Oppose Church and any faction with Mandate ≥ 5.

**Actions (once per season, NPC-controlled):**

| Action | Roll | Effect |
|--------|------|--------|
| Community Weaving | Influence vs Ob = Thread Tension ÷ 20 (round up, min 1). Requires practitioner TS 30+ affiliated. | Overwhelming: MS +2, PT −1 in target territory. Success: MS +1, PT −1. Partial: no effect. Failure: Stability −1, MS −1. Co-Movement card drawn. |
| Grassroots Organising | Influence vs Ob 2 | Success: RM Mandate +1 in one territory with PT ≤ 2. Caps at Mandate 5. |
| Resist Seizure | Influence vs Church Influence | When Church attempts seizure in territory with PT ≤ 2: RM adds +1 Ob to Church seizure roll. Passive — does not consume RM's action. |

**Territory presence:** Active RM has presence in every territory with PT ≤ 1. RM does not control territory — it exerts influence within it. RM presence adds +1 Ob to any Church action in that territory.

### 5.4 Suppression and Resolution

**Suppression:** RM can be suppressed back to latency if:
- WA returns to ≥ 0 (Varfell reconciles), OR
- All territories rise to PT ≥ 2 (movement loses popular base), OR
- RM Stability reaches 0 (movement collapses internally).



---

## 6. Varfell Paths B & C — Redesign (PP-417)
> **[SUPERSEDED-BY: GD-1]** Canon §B GD-1 (peninsula-only victory; see `canon/02_canon_constraints.md`) STRIKES this section. Content preserved as supersession-trail evidence. Date: 2026-05-17.


### 6.1 Path B — Southernmost Dominion (full redesign)
> **[SUPERSEDED-BY: GD-1]** Canon §B GD-1 (peninsula-only victory; see `canon/02_canon_constraints.md`) STRIKES this section. Content preserved as supersession-trail evidence. Date: 2026-05-17.


**Deed structure: 3 Deeds. All must be completed.**

| Deed | Condition | Gate |
|------|-----------|------|
| **Deed 1 — Extend the Reach** | Control T13 (Oastad) + garrison or Tribune present in T15 (Southernmost) simultaneously for 2 consecutive seasons. | VTM ≥ 2 (must have Thread awareness to engage the Southernmost meaningfully). |
| **Deed 2 — Walk the Wound** | Complete a Southernmost Expedition (existing mechanic) with Vaynard's personal participation. Pass the Forgetting Check. | VTM ≥ 3. Warden Cooperation ≥ 1. |
| **Deed 3 — Keeper's Mandate** | Hold T13 at PT ≤ 1 AND WA ≥ +1 for 2 consecutive seasons. | VTM ≥ 3. The movement must trust Vaynard — this cannot be achieved if RM has emerged as hostile. |



### 6.2 Path C — Thread Supremacy (territory name correction + validation)
> **[SUPERSEDED-BY: GD-1]** Canon §B GD-1 (peninsula-only victory; see `canon/02_canon_constraints.md`) STRIKES this section. Content preserved as supersession-trail evidence. Date: 2026-05-17.


**Deed structure: 3 Deeds. Unchanged except territory references.**

| Deed | Condition | Gate |
|------|-----------|------|
| **Deed 1 — Thread Mastery** | VTM = 5. | — |
| **Deed 2 — Territorial Command** | Control T4 (Grauwald) + T13 (Oastad) + ≥ 1 other territory simultaneously. | — |
| **Deed 3 — World Intact** | MS ≥ 50 at the moment of victory declaration. | — |

**Corrections applied:** T4 = Grauwald (was "Vargstad"). T13 = Oastad (was "Stillhelm"). Deed structure is otherwise sound — VTM 5 is a genuine multi-season investment (minimum ~S14–S16 to achieve), territorial control is non-trivial, and MS ≥ 50 creates tension with Thread operations that degrade MS.

**No further changes required for Path C.**

---

## 7. Co-Victory Replacement — Varfell + RM (PP-418)
> **[SUPERSEDED-BY: GD-1]** Canon §B GD-1 (peninsula-only victory; see `canon/02_canon_constraints.md`) STRIKES this section. Content preserved as supersession-trail evidence. Date: 2026-05-17.


**Old co-victory (DISSOLVED):** Varfell Thread Supremacy + Restoration Network Victory (both MS ≥ 50). Invalid — RM is no longer a primary faction with its own victory path.

**Replacement: Einhir Restoration Co-Victory**

**Conditions (all must be met simultaneously):**

| Condition | Faction Responsible |
|-----------|-------------------|
| VTM ≥ 4 | Varfell |
| WA ≥ +2 | Varfell (cultivation choices) |
| ≥ 4 territories at PT ≤ 1 | Both (Varfell Cultural Reclamation + latent RM Community Weaving) |
| MS ≥ 40 | Both (Community Weaving sustains MS; Varfell Thread operations must not collapse it) |
| Warden Cooperation ≥ 2 | Varfell |
| Vaynard controls T13 (Oastad) | Varfell |



---

## 8. Resolved Editorial Items

| ED | Resolution | Patch |
|----|-----------|-------|
| ED-110 | **Resolved (historical) — [SUPERSEDED-BY: PP-421 + GD-1].** Church victory *was* CI 75 phase transition → territorial consolidation (TCV ≥ 18 for 2 seasons); Alternate Altonian Theocracy (AEA = 5); Hollow Church + Hafenmark partition. Superseded twice over: PP-421 (CI runs 0–100, no freeze) and GD-1/ED-NEW-CI-10 (no faction-specific victory — Peninsular Sovereignty is the sole win path, ci_political_v30 §7.1). | PP-413, PP-414, PP-415 (superseded) |
| ED-112 | **Closed.** Hafenmark −1/season vs Church +1/season is a pacing concern under old system. Under new CI generation (Conviction Yield + Assert), the interaction is richer: Hafenmark suppression negates passive +1 but cannot touch Conviction Yield. No longer a deadlock risk. | — |
| ED-111 | **Superseded** by PP-412 (CI generation redesign). Old Piety Domain Action dissolved; replaced by Conviction Yield + Assert. | PP-412 |

**New editorial items raised:**

| ED | Description | Priority |
|----|-------------|----------|
| ED-302 | Confirm track name "Conviction" (PT) | P2 |
| ED-303 | Does CI freeze at 75 or continue advancing? Design recommends freeze. | P1 |
| ED-304 | Hollow Victory scoring — co-win or draw? Design recommends conditional victory for both. | P2 |
| ED-305 | Varfell-RM Relationship Track (Warden's Accord) starting value — 0 is proposed. Confirm. | P2 |

---

## 9. Gaps Identified

| Gap | Description |
|-----|-------------|
| [GAP: CI pacing — no simulation] | ~~CI 75 timeline estimate (~S20)~~ superseded (PP-421: CI runs to 100, no freeze); no canonical CI-100 pacing estimate exists yet — OPEN against the CI-100 model. Needs simulation with faction AI. Flag as SIM-DEBT. |
| [GAP: AEA pacing — no simulation] | Altonian Theocracy clock has 5 advancement conditions. Needs simulation to confirm it is achievable but not trivial. |
| [GAP: RM emergence frequency] | The triple condition (WA ≤ −2, 3 territories PT ≤ 1, MS ≤ 50) may be too restrictive or too permissive. Needs stress test. |
| [GAP: Community Weaving dual effect] | Community Weaving now affects both MS and PT. Need to verify this does not create a positive feedback loop (low PT → more Weaving → lower PT → more RM power). |
| [GAP: Consecrated status interaction with seizure] | Consecrated territories get −1 Ob on seizure but also require PT ≥ 5 via Consecrate action. This may make high-PT territories too easy to seize. Needs edge case check. |
| [GAP: Hafenmark Secular Governance floor] | Secular Governance cannot reduce PT below 2. Is this the right floor? If Hafenmark wants to support RM, they may need to push lower. |
| [GAP: Fort Level data] | Seizure Ob formula uses Fort Level (0–3). Confirm which territories have which Fort Levels — not in handoff. |

---

## 10. Patch Summary

| PP | Scope | Description |
|----|-------|-------------|
| PP-406 | Track | Conviction (PT) starting values — 15 eligible territories, 0–5 range |
| PP-407 | Track | T15 hard fix rule — PT permanently 0, no exceptions |
| PP-408 | Track | PT movement rules — faction actions, frequency, seasonal cap ±1 |
| PP-409 | Track | Calamity Drift — MS-linked PT erosion at MS ≤ 50/35/20 |
| PP-410 | Track | Consecrated status — PT 5 via Consecrate action, floor of 4 while Church controls |
| PP-411 | Seizure | Church Seizure Ob = 2 + Fort Level + max(0, 3 − PT). Prominence required. |
| PP-412 | CI | CI generation redesign — passive +1, Conviction Yield, Assert, Suppress, Hafenmark structural |
| PP-413 | Victory | ~~Church Primary Victory — CI 75 phase transition, TCV ≥ 18 for 2 seasons~~ **[SUPERSEDED — PP-421 (CI ceiling 0–100, no freeze) + GD-1/ED-NEW-CI-10 (sole Peninsular Sovereignty victory)]** |
| PP-414 | Victory | Altonian Theocracy Path — AEA clock 0–5, victory at AEA 5 + CI ≥ 60 + hold T9 |
| PP-415 | Victory | Hollow Victory — Church + Hafenmark partition, Crown Mandate ≤ 1 |
| PP-416 | RM | RM Emergence — Warden's Accord track, triple-condition trigger, active NPC rules |
| PP-417 | Varfell | Path B redesign (3 Deeds) + Path C territory correction |
| PP-418 | Co-Victory | Einhir Restoration Co-Victory — Varfell + latent RM, 6 conditions |

---

## 11. Piety Track Presentation Layer (NEW — World→Player Bridge)

### §11.1 PT Change Environmental Events

When Conviction (PT) changes in a territory, the change should be experienceable by any player present. PT is not just a number — it is the cultural identity of a community shifting.

| PT Transition | Environmental Description |
|--------------|--------------------------|
| PT +1 (any → higher) | Church influence deepens. **Settlement type modulation:** Cathedral settlements amplify this effect (total Church presence). Market/Port settlements mute it (commerce dampens extremes). Outpost settlements show minimal change. New description: the morning bells ring longer. A priest who used to preach from memory now reads directly from the Solmund Codex. A shrine appears at the crossroads that wasn't there last season. The tavern-keeper has hung a blessing plaque by the door. |
| PT −1 (any → lower) | Einhir heritage resurfaces. **Settlement type modulation:** Outpost/Town settlements show this most strongly (frontier culture is closer to Einhir roots). Cathedral settlements resist (institutional inertia). New description: someone has left wildflowers at the old Einhir stone circle outside town. Children are singing a song in a language the Church doesn't teach. An elder tells a story about what the land was before Solmund, and no one shushes them. |
| PT reaches 5 (Consecrated) | Total Church dominance. The territory feels different. Church officials are present in every public space. The old Einhir names for landmarks have been replaced with Solmundic names on the official signposts. Non-Church social gatherings require permission. |
| PT reaches 0 | Einhir restoration complete. Church architecture is repurposed or abandoned. Thread-sensitive characters perceive a subtle difference in the substrate — the rendering is thinner here, closer to what it was before the orthodoxy. |

**TTRPG/Hybrid:** GM narrates the transition. The description does not specify the PT number — the player perceives the change through lived texture, not statistics.

**Videogame:** Environmental art shifts per PT level: shrine placement, banner type, ambient NPC dialogue, architectural details, lighting warmth.

### §11.2 Church Attention Pool — Player-Facing Indicators

The Church Attention Pool (AP) is now tracked per settlement (per settlement_bridge_unification C-15), not per province. AP accumulates where the player acts, not across the whole territory. The player should perceive its effects without knowing the number.

| AP Level | Player-Perceivable Indicator |
|----------|------------------------------|
| 0 | No Church surveillance activity. Normal environment. |
| 1 | A clerk in Church vestments is seen watching the market from a second-floor window. A merchant mentions that a Church official asked about recent visitors. |
| 2 | A Church procession passes through the territory — formal and deliberate. An NPC mentions that the Church has been "asking questions about Thread activity." |
| 3 | Inquisitor's seal appears on a public notice in the town square. NPCs with Disposition ≤ 0 toward the player avoid being seen with them in public. |
| 4+ | The Inquisitor is present. Church guards patrol. NPCs whisper. Anyone seen talking to the player in private may be questioned afterward. Fieldwork Exposure +1 automatic per scene (the environment itself is hostile to investigation). |

### §11.3 CI Milestone Presentation

When the Church Influence (CI) crosses a milestone threshold, the change is visible across the peninsula — not just in the affected territory.

| CI Threshold | Presentation |
|-------------|-------------|
| CI 40 | Church authority is becoming assertive. In Church-controlled territories: new construction (chapels, schools). In non-Church territories: Church envoys arrive with formal diplomatic proposals. |
| CI 55 | Church is the dominant institutional force. Parliamentary debates increasingly reference Church doctrine. Crown officials are seen attending Church ceremonies. Trade guilds negotiate with Church officials directly. |
| CI 65 | Church is approaching hegemony. Non-Church factions must actively resist or be absorbed. Suppress Heresy actions fire in border territories. The atmosphere shifts from institutional competition to institutional survival. |
| CI 75 → *(milestone set superseded)* | **[STALE — pre-redesign milestone; PP-421 replaces the CI-75 freeze with the 40/55/65/80/100 milestone set. Exact table renumbering is deferred by ruling (armature §5.11, ratified via ED-IN-0026 — "doesn't need a winner yet"); not rewritten to specific new thresholds here.]** Graduated Seizure eligible. The Church is no longer competing — it is consolidating. The question for every other faction is not "how do we win" but "how do we survive." |
