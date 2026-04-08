# VALORIA BG — Victory Architecture
## ED-306 Resolution (v3 — PP-199 territory numbering, TC 75 canonical, CV cap clarified)
## Date: 2026-04-06 | Status: DESIGN — pending Varfell Path B user decision (ED-311)
## Supersedes: v2 (same path), params_board_game.md §Victory Conditions, all Deed-based victory systems
## Dependencies: ED-302 (CV confirmed), ED-303 (TC freeze at 75), ED-304 (Partition Victory), ED-305 (WA=0), ED-307 (Baralta cadet branch), BALANCE-001 (equal win probability), BALANCE-004 (Askeheim purpose)
## Territory numbering: PP-199 definitive (all T-numbers match params_board_game PP-199 table)

---

## Core Frame

Victory = Territory Held + Faction-Specific Political Conditions, sustained for 2 consecutive Accounting steps.

Two simultaneous contests: who governs the peninsula AND whether it survives. Church and Hafenmark are structurally blind to the Rendering Stability (RS) crisis — they can win fast but their victory is fragile if RS collapses. Crown and Varfell can address RS via Thread path but at cost of political resources.

**Equal win probability** for Crown, Varfell, Hafenmark. Church is the easy/hard mode toggle. Restoration Movement (RM) is hardest mode. (BALANCE-001)

---

## 1. Territory Consolidation Values (TCV)

Every territory has a fixed strategic weight. TCV is the universal measure of territorial dominance.
All territory numbers match PP-199 definitive table.

| T# | Territory | TCV | Controller |
|----|-----------|-----|-----------| 
| T12 | Valorsplatz | 5 | Crown★ |
| T5 | Gransol | 4 | Hafenmark★ |
| T14 | Himmelenger | 3 | Church★ |
| T2 | Sigurdshelm | 3 | Varfell |
| T7 | Spartfell | 2 | Hafenmark |
| T8 | Lowenskyst | 2 | Hafenmark |
| T9 | Arcansheld | 2 | Crown |
| T1 | Varfell | 1 | Varfell |
| T3 | Halvardshelm | 1 | Varfell |
| T4 | Vargstad | 1 | Varfell |
| T6 | Eidursjo | 1 | Hafenmark |
| T10 | Nordhelm | 1 | Crown |
| T11 | Mittelmark | 1 | Crown |
| T13 | Stillhelm | 1 | Crown |
| T15 | Askeheim | 0 | Uncontrolled |
| T16 | Schoenland | — | Not in territorial play |
| | **Total** | **28** | |

**Starting TCV by faction:** Crown 10, Hafenmark 9, Varfell 6, Church 3.

---

## 2. Conviction Track (CV)

Per-territory track. Range 0–5 per territory. 0 = Restoration pole, 5 = Piety pole.

Starting values, movement rules, Calamity Drift, and Consecrated status per opus_design_proposal.md §1.1–1.4.

Key rules:
- T15 (Askeheim) CV hard-fixed at 0. Cannot increase. (P-03 + Foundations §8)
- T14 (Himmelenger) starts at 5, soft cap — can drop under pressure, does not auto-recover.
- **CV action cap:** Each faction may initiate at most one deliberate CV-moving action per territory per season (±1 max). Calamity Drift, Church Seizure Overwhelming CV bonus, and Domain Echoes from Zoom In are consequences — they are not faction actions and are not cap-governed.
- Calamity Drift (RS-linked CV erosion) ignores the action cap. RS ≤ 50: T6/T13 CV −1. RS ≤ 35: territories within 2 steps of T15 CV −1. RS ≤ 20: all territories CV −1.
- Community Weaving is a Thread operation: follows standard Thread procedure including Co-Movement card draw. CV −1 is the primary effect; temporal/epistemic/actual auto-effects fire per P-01.

---

## 3. Victory Conditions — All Factions

Every victory requires holding all conditions for **2 consecutive Accounting steps**. A faction knocked out between steps resets its counter.

### 3.1 Crown — Peninsula Sovereignty

**All conditions simultaneous at Accounting:**

| Condition | Threshold |
|-----------|-----------|
| TCV held | ≥ 16 |
| Rival suppression | Every other playable faction: Mandate ≤ 2 OR eliminated OR formal Crown Treaty in effect |
| IP | < 60 |
| PI | ≥ 3 |

**Formal Crown Treaty:** Diplomacy action, Ob = target faction's Mandate. Both factions must agree. Target faction: Mandate −1, Stability +1. Treaty dissolves if Crown breaks it (Crown Stability −2, Mandate −1) or target faction Mandate reaches 0.

#### Alternate — Dominion
TCV ≥ 22 AND every other playable faction eliminated (Stability 0). No treaties.

---

### 3.2 Church of Solmund — Solmundan Orthodoxy

**Phase 1 (TC 0–74):** Accumulate TC via institutional momentum, Conviction Yield, and Assert. Per opus_design_proposal.md §3.

**Phase 2 (TC ≥ 75):** TC freezes at 75. Church shifts to territorial seizure.

**Victory conditions (all simultaneous at Accounting, post-TC 75):**

| Condition | Threshold |
|-----------|-----------|
| TCV held | ≥ 10 |
| CV in all held territories | ≥ 3 |

**Church Seizure Ob (post-TC 75):** Ob = 2 + Fort Level + max(0, 3 − CV). 

**Prominence prerequisite:** Church may only seize a territory where Church is Prominent — defined as Church Mandate exceeding the controlling faction's Mandate in that territory. Church Mandate is the Church faction's global Mandate stat. Controlling faction Mandate is their global Mandate stat. Prominence is assessed at seizure declaration.

Church Mandate ≥ 4 required to initiate any seizure. Overwhelming seizure: CV +1 in target territory (this is a consequence, not a cap-governed action).

#### Alternate — Altonian Theocracy Path
Altonian Ecclesiastical Accord (AEA) track 0–5. Victory: AEA = 5 + TC ≥ 60 + Church controls T14 (Himmelenger). Requires less territory but more diplomatic conditions.

#### Partition — Church + Hafenmark (ED-304)
**Trigger (all simultaneous at Accounting):**
- Crown Mandate ≤ 1
- TC ≥ 50
- Church controls ≥ 2 territories
- Hafenmark controls ≥ 3 territories
- No active military conflict between Church and Hafenmark

**Outcome:** Mutual agreement ends the game. Both factions score a conditional victory. No holding requirement — fires immediately on mutual declaration.

---

### 3.3 Hafenmark — Parliamentary Sovereignty

**All conditions simultaneous at Accounting:**

| Condition | Threshold |
|-----------|-----------|
| TCV held | ≥ 12 |
| Hafenmark Mandate | ≥ 4 |
| PI | ≥ 5 |
| Crown Mandate | ≤ 3 |

#### Alternate — Dynastic Assertion (ED-307)

| Condition | Threshold |
|-----------|-----------|
| TCV held | ≥ 12 |
| Crown Mandate | ≤ 1 |
| Control T12 (Valorsplatz) | held |
| Hafenmark Mandate | ≥ 5 |
| Torben Loyalty | ≤ 3 OR Torben removed |

---

### 3.4 Varfell — Vaynard's Three Paths

#### Path A — Intelligence Hegemony

| Condition | Threshold |
|-----------|-----------|
| TCV held | ≥ 10 |
| VTM | ≥ 3 |
| At least 2 rival factions' stats fully revealed | fixed count |
| Varfell controls ≥ 1 territory outside starting 4 | — |

#### Path B — Southernmost Dominion
[ED-311 RESOLVED — Option A (4 conditions + WR track), 2026-04-07]

| Condition | Threshold |
|-----------|-----------|
| TCV held | ≥ 8 |
| Control T4 (Grauwald) AND T13 (Oastad) | both held |
| VTM | ≥ 3 |
| Warden Recognition (WR) | ≥ 2 |

**WR track (0–4):** See params_board_game.md §Varfell Path B for full WR track rules.
**Blocked if:** WR has ever returned to 0 after first advancing past 1.

#### Path C — Thread Supremacy

| Condition | Threshold |
|-----------|-----------|
| TCV held | ≥ 10 |
| VTM | = 5 |
| RS | ≥ 50 |

---

### 3.5 Restoration Movement — Cultural Revolution (5 players only, hardest mode)

RM has no faction stats. It operates purely through Presence markers and Community Weaving. It cannot hold territory, raise armies, or act in any domain that requires a faction stat. It cannot be targeted by Royal Decree, Excommunicate, or Suppress. Its only vulnerability is CV reversal (Church Piety Spread) and Inquisitor disruption of Weaving.

**Two-phase win condition:**

#### Phase 1 — Cultural Majority (threshold to unlock Phase 2)
CV ≤ 1 in ≥ 8 of the 15 playable territories (T1–T14, T17). Checked at each Accounting. Once met and held, Phase 2 becomes available. If the majority drops below 8, Phase 2 is locked again until it recovers.

#### Phase 2 — Cultural Uprising of T9 Himmelenger
Available only while Phase 1 condition is met. Declared once per game at any Accounting where Phase 1 holds. RM plays their Pontifex card and rolls: **Weaver Thread pool vs Ob = TC ÷ 10 (round up, min 1, max 5).**

Modifiers:
- T9 CV ≤ 1: Ob −1 (Cathedral already culturally shifted)
- WC ≥ 2: +1D (Wardens support the Uprising)
- TC ≥ 50 at declaration: Ob +1 (Church institutional authority is strong enough to resist)
- Church Mandate ≥ 5: Ob +1 (Church actively suppresses)

| Degree | Effect |
|--------|--------|
| Overwhelming | T9 transfers to RM administration. Church Mandate −2. TC −3 (institutional rupture). |
| Success | T9 transfers to RM administration. Church Mandate −1. |
| Partial | T9 does not transfer. CV in T9 −1 (popular sentiment shifted). Uprising attempt used up for this arc. |
| Failure | Uprising crushed. TC +2 (Church authority strengthened by resistance). T9 CV +1. Uprising attempt used up for this arc. |

**Win condition:** T9 under RM administration AND Phase 1 held, for 2 consecutive Accounting steps. Church cannot perform Territorial Seizure on T9 while RM holds it (the population actively resists institutional reconquest — Seizure Ob +3 vs RM-held T9).

---

### 3.6 Löwenritter — Military Regency (conditional faction, post-coup)

#### Primary — Regency Establishment

| Condition | Threshold |
|-----------|-----------|
| TCV held | ≥ 10 |
| TC | < 50 |
| IP | < 60 |
| RS | > 40 |
| PI | ≥ 4 |
| Successor confirmed | Elske confirmed OR Torben Loyalty ≥ 6 |

#### Alternate — Military Consolidation
Only available if Regency Establishment not achieved after 8 Löwenritter seasons (track with counter on Löwenritter mat).

| Condition | Threshold |
|-----------|-----------|
| TCV held | ≥ 16 |
| Löwenritter Military | ≥ 5 |
| RS | > 35 |
| TC | < 60 |

---

## 4. Co-Victory Pairings

Co-victories require 2 consecutive Accounting steps except Partition (immediate on mutual agreement).

| Pair | Conditions (all simultaneous at Accounting) |
|------|---------------------------------------------|
| **Crown + Hafenmark** | Crown TCV ≥ 12 AND Hafenmark TCV ≥ 9 AND PI ≥ 5 AND TC < 50 |
| **Crown + Varfell** | Crown TCV ≥ 12 AND Varfell TCV ≥ 8 AND VTM ≥ 3 AND RS ≥ 50 |
| **Varfell + RM** | VTM ≥ 4 AND WR ≥ 2 AND ≥ 4 territories CV ≤ 1 AND RS ≥ 40 AND Varfell controls T13 |
| **Hafenmark + RM** | Hafenmark TCV ≥ 10 AND ≥ 4 territories CV ≤ 2 AND PI ≥ 4 AND RS ≥ 40 |
| **Löwenritter + Hafenmark** | Löwenritter TCV ≥ 8 AND Hafenmark TCV ≥ 8 AND PI ≥ 4 |
| **Church + Hafenmark (Partition)** | See §3.2. Crown Mandate ≤ 1, TC ≥ 50, Church ≥ 2 territories, Hafenmark ≥ 3, no active military conflict. |

**Incompatible:** Crown + Church, Crown + Löwenritter, Church + Varfell, Church + RM.

Co-victories are distinct from operational coalitions (PP-404/405). A faction may pursue a coalition without pursuing a co-victory.

---

## 5. Shared Loss Conditions

| Condition | Trigger | Outcome |
|-----------|---------|---------| 
| Rendering Stability Rupture | RS = 0 at Accounting | All factions lose. Second Calamity. |
| Altonian Conquest | IP ≥ 100 AND AER ≤ 1 | Altonia annexes Valoria. All factions lose. |
| Total Institutional Collapse | All playable factions at Stability 0 simultaneously | Anarchy. All factions lose. |

---

## 6. Askeheim and RS (BALANCE-004)

If no faction engages with Askeheim (T15), RS trends toward 0 and a second Calamity occurs.

**Warden Cooperation track (0–3):**
- WC ≥ 1: +1D to all Thread operations peninsula-wide.
- WC ≥ 2: RS decay rate halved.
- WC ≥ 3: RS +2/season at Accounting.

Multiple victory conditions require RS thresholds. A faction that ignores RS risks losing to Rupture regardless of territorial control.

**Warden Recognition (WR) track (0–4) — Varfell Path B:**
- WR 0: Wardens unaware or indifferent.
- WR 1: Wardens have observed Vaynard (≥ 1 successful Expedition).
- WR 2: Wardens recognise Vaynard as steward.
- WR 3: Active cooperation (+1D Thread ops, as WC ≥ 1 equivalent).
- WR 4: Edeyja makes substantive contact.

WC and WR are distinct tracks. WC advances through any faction's Expedition engagement. WR advances only through Varfell's Expedition actions.

---

## 7. TC Generation and Church Seizure

Starting TC: 28. Phase transition at TC 75 (TC freezes, Church shifts to seizure mode).

**Seasonal TC at Accounting:**
1. Institutional Momentum: TC +1 (passive).
2. Conviction Yield: per territory where Church is Prominent (Church Mandate > controlling faction Mandate), add by CV. CV 5 = +1, CV 4 = +0.5, others = 0. Total = floor(sum).
3. Assert (optional Church action): Influence vs Ob 2. Success: TC +1. Failure: Stability −1.
4. Suppress (optional opponent action): Mandate vs Ob = Church Mandate. Success: negate Step 1 passive. Failure: Stability −1.
5. Hafenmark Structural Suppression: while Baralta Mandate ≥ 4, TC −1/season.

**Church Seizure Ob (post-TC 75):** Ob = 2 + Fort Level + max(0, 3 − CV). Prominence required. Church Mandate ≥ 4. Overwhelming: CV +1 in target territory.

---

## 8. RM Emergence

WA track −3 to +3, starts 0. Triple-condition emergence: WA ≤ −2 AND ≥ 3 territories CV ≤ 1 AND RS ≤ 50. One-shot. Suppression: WA ≥ 0 OR all territories CV ≥ 2 OR RM Stability 0. See opus_design_proposal.md §5 for full stat block and AI.

---

## 9. Hybrid Mode Integration

### 9.1 CV State Transfer

| Transition | CV Rule |
|-----------|---------|
| BG → TTRPG (Zoom In) | CV is read-only context. GM uses CV to inform NPC attitudes and faith-related framing. |
| TTRPG → BG (Zoom Out) | CV changes from personal scenes queue as Domain Echoes. Cap: ±1 CV in one territory per Zoom In, firing at next Accounting. |
| Calamity Drift during Zoom In | Queues and fires when Accounting resumes. Cannot be skipped. |

**Variables that TRANSFER (BG → TTRPG):**

| BG Variable | TTRPG Equivalent | Transformation |
|-------------|-----------------|----------------|
| Territory CV (0–5) | Scene context (NPC attitudes, crowd faith level) | Read-only. Changes queue as Domain Echo (±1 max per Zoom In). |

**Zoom Out (TTRPG → BG):**

| TTRPG Outcome | BG State Update |
|---------------|----------------|
| Faith-affecting personal scene (sermon, debate, Community Weaving) | CV ±1 in that territory, queued to Accounting. Cap: 1 CV Domain Echo per Zoom In. |

### 9.2 Victory Condition Check — Hybrid

Victory condition checks (all factions) fire at Accounting Step 12 regardless of active Zoom In. A Zoom In cannot delay or prevent a victory declaration. The 2-Accounting holding requirement is assessed across consecutive Accounting steps — a Zoom In spanning an Accounting boundary counts that Accounting.

### 9.3 Hybrid Victory and P-32

P-32 ("Hybrid victory = BG victory PLUS personal arc resolution") is retained. A BG victory is mechanically valid. If the winning faction's PC has unresolved Beliefs or Inspirations, the victory is narratively qualified — no mechanical penalty. "Hollow Victory" in the P-32 sense is distinct from the Church + Hafenmark Partition Victory. These are different concepts.

### 9.4 Domain Echo Autonomous Resolution (ED-300)

Autonomous TCV changes from uninvestigated Domain Echoes count toward or against victory conditions. The 2-Accounting holding requirement does not exempt autonomous changes.

---

## 10. Win Probability Assessment

| Faction | Start TCV | Target TCV | Gap | Key Difficulty | Est. Timeline |
|---------|-----------|------------|-----|----------------|---------------|
| Crown | 10 | 16 | +6 | Suppress ALL rivals (×3 political) | 14–16 seasons |
| Church | 3 | 10 | +7 | TC 75 clock (~S16-18) then seizure | 20–24 seasons (hard mode) |
| Hafenmark | 9 | 12 | +3 | Mil 3 handicap + Crown Mandate suppression | 10–14 seasons |
| Varfell A | 6 | 10 | +4 | Geographic isolation + VTM 3 + intel reveals | 12–14 seasons |
| Varfell B | 6 | 8 | +2 | VTM 3 + Warden Recognition + T13 control | 12–16 seasons |
| Varfell C | 6 | 10 | +4 | VTM 5 (~S14+) + RS maintenance | 14–18 seasons |
| RM | — | — | — | 5 territories CV ≤ 1 + RS ≥ 40 | 14–20 seasons |

[SIM-DEBT: Full faction-AI simulation needed to validate non-military acquisition paths, fortification effects, multi-faction interaction dynamics. Flag as P1.]

---

## 11. Open Editorial Items

| ED | Description | Status |
|----|-------------|--------|
| ED-311 | Varfell Path B redesign — see varfell_path_b_redesign_ed311.md | AWAITING USER DECISION |

---

## 12. Patch Register

| PP | Scope | Description |
|----|-------|-------------|
| PP-408 | TCV | Territory Consolidation Values — remapped to PP-199 numbering |
| PP-409 | Victory | Crown Peninsula Sovereignty — TCV ≥ 16 (gap restored to +6 after remapping) |
| PP-410 | Victory | Crown Dominion alternate — TCV ≥ 22 |
| PP-411 | Victory | Hafenmark Parliamentary Sovereignty — TCV ≥ 12 |
| PP-412 | Victory | Hafenmark Dynastic Assertion — T12 Valorsplatz (corrected from old T-number) |
| PP-413 | Victory | Church Altonian Theocracy — T14 Himmelenger (corrected from old T-number) |
| PP-414 | Victory | Varfell Path B provisional (ED-311 pending) |
| PP-415 | Victory | RM Cultural Revolution — RS ≥ 40 confirmed canonical |
| PP-416 | CV | CV action cap clarified — consequences not cap-governed |
| PP-417 | Church | Prominence mechanic defined (Church Mandate > controlling faction Mandate per territory) |
| PP-418 | Löwenritter | Military Consolidation — 8-season timer requires counter on Löwenritter mat |
| PP-419 | Hybrid | CV state transfer rules (replaces §9.1 directives-to-author format) |
| PP-420 | Hybrid | Victory condition check — replaces TC Win-Delay Rule |
| PP-421 | TC | TC 75 canonical freeze + seizure threshold. TC 80 in params_board_game struck. |
| PP-422 | Co-Victory | WA/WC references replaced with WR in Varfell+RM co-victory |
| PP-423 | Crown | Formal Crown Treaty mechanic |
| PP-424 | System | Deed system dissolved — all factions |
| PP-425 | WR | Warden Recognition track defined (0–4) |


---

## 5. Total Domination (ED-318 RESOLVED, 2026-04-07)

Available to all playable factions as alternate victory path.

| Condition | Threshold |
|-----------|-----------|
| TCV held | ≥ 28 |
| All rival factions | Stability 0 (eliminated) OR Submitted |

Both conditions must hold simultaneously for 2 consecutive Accounting steps.

**Submission:** Any faction at Stability 0 that has not been eliminated may formally Submit at Accounting. Submitted faction: removed from victory competition, remains on board as NPC vassal (stats halved rounded down, no independent actions). The Total Domination faction must hold all non-Submitted, non-eliminated rivals at Stability 0 simultaneously.

---

## 6. Notes on Spoiler Dynamics (SIM-SPOILER-BG-01 + SIM-SPOILER-HY-01, 2026-04-07)

Simulation confirms that spoiler strategies are functional. Key findings:
- Church spoiling Crown: viable 5–8 season delay via Mandate maintenance + Inquisitor deployment. Crown counter: Royal Decree chain.
- Varfell spoiling Church: TC suppression via Counter-Narrative is minor (−0.135 TC/use expected); primary effect is AP pressure. Hybrid mode allows invisible spoiling via personal-scale Zoom In actions.
- Institutional Mandate trigger scope: [EDITORIAL: ED-324 — confirm trigger fires on Mandate-targeting actions only.]
- Church Prominence tracker: [EDITORIAL: ED-326 — recommend tracker on Church mat for Counter-Narrative eligibility.]
