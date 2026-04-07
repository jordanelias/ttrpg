# VALORIA BG — Victory Architecture Redesign
## ED-306 Resolution
## Date: 2026-04-06 | Status: DESIGN PROPOSAL — User Review Required
## Scope: All faction victory conditions, Conviction Track integration, co-victory restructuring
## Supersedes: params_board_game.md §Victory Conditions (v04 B5)
## Dependencies: ED-302 (CV confirmed), ED-303 (TC freeze at 75), ED-304 (Hollow Victory), ED-305 (WA=0), ED-307 (Baralta cadet branch), BALANCE-001 (equal win probability), BALANCE-004 (Askeheim purpose)
## Source: opus_design_proposal.md (PP-406–PP-418) + user decisions 2026-04-06

---

## Design Principles

1. **Territorial dominance + ideological alignment.** Every faction wins by controlling enough peninsula territory where conditions match their vision. The Deed checklist is dissolved for all factions.
2. **Conviction Track (CV) is the ideological axis contested by all factions.** CV 0–5 per territory. 0 = Restoration pole. 5 = Piety pole.
3. **Two simultaneous contests:** Who governs the peninsula AND whether it survives. Church/Hafenmark are structurally blind to Rendering Stability (RS) crisis — they can win fast but victory is fragile if RS collapses. Crown/Varfell can address RS via Thread path but at cost of political resources.
4. **Equal win probability** for Crown/Varfell/Hafenmark. Church is easy/hard mode toggle. Restoration Movement is hardest mode. (BALANCE-001)
5. **Askeheim (T15) is not dead space.** It is the existential threat that gives RS its teeth. (BALANCE-004)

---

## 1. Conviction Track (CV) — Canonical Specification

Per opus_design_proposal.md §1. Starting values, movement rules, Calamity Drift, and Consecrated status unchanged from that document. Key values reproduced here for reference.

### 1.1 Starting Values

| T# | Territory | Controller | CV |
|----|-----------|-----------|-----|
| T1 | Valorsplatz | Crown | 4 |
| T2 | Kronmark | Crown | 4 |
| T3 | Lowenskyst | Crown | 4 |
| T4 | Grauwald | Varfell | 2 |
| T5 | Feldmark | Crown | 3 |
| T6 | Stillhelm | Crown | 3 |
| T7 | Rendstad | Hafenmark | 3 |
| T8 | Gransol | Hafenmark | 3 |
| T9 | Himmelenger | Church | 5 |
| T10 | Spartfell | Hafenmark | 3 |
| T11 | Halvardshelm | Varfell | 2 |
| T12 | Sigurdshelm | Varfell | 2 |
| T13 | Oastad | Varfell | 2 |
| T14 | Ehrenfeld | Crown | 4 |
| T15 | Askeheim | Uncontrolled | **0** |
| T16 | Schoenland | Schoenland | — |
| T17 | Halvarshelm | Hafenmark | 3 |

**T15 hard-fixed:** Cannot increase by any means. The Calamity annihilated orthodox Piety at the Einhir epicentre. Metaphysically irreversible (P-07).

**T9 soft cap:** Starts at 5, can drop under pressure, does not auto-recover.

### 1.2 Movement Rules

Per opus_design_proposal.md §1.2–1.4. Seasonal cap ±1 CV per territory per season. No drift (CV is sticky). Exception: Calamity Drift (RS-linked erosion, §1.3 of opus doc).

### 1.3 Calamity Drift

| RS Threshold | Effect |
|-------------|--------|
| RS ≤ 50 | T6, T13 (adjacent to T15): CV −1 at Accounting if CV > 0 |
| RS ≤ 35 | All territories within 2 steps of T15: CV −1 at Accounting if CV > 0 |
| RS ≤ 20 | All territories: CV −1 at Accounting if CV > 0 |

Calamity Drift ignores the ±1/season cap. Cannot reduce T15 below 0.

---

## 2. Territory Consolidation Values (TCV)

Every territory has a fixed strategic weight reflecting its political, economic, and symbolic importance. TCV is used by all factions as the basis for victory calculations.

| T# | Territory | TCV | Rationale |
|----|-----------|-----|-----------|
| T1 | Valorsplatz | 5 | Capital — seat of Crown power, river-sea trade nexus |
| T8 | Gransol | 4 | Hafenmark capital — industrial-parliamentary centre |
| T12 | Sigurdshelm | 3 | Varfell seat — fjord power centre |
| T9 | Himmelenger | 3 | Cathedral city — ecclesiastical centre, 5 connections (kingmaker) |
| T3 | Lowenskyst | 2 | Primary Altonian crossing — military chokepoint |
| T14 | Ehrenfeld | 2 | Military hinge — 5 connections, Crown fortress |
| T10 | Spartfell | 2 | Secondary Altonian crossing — border castle |
| T2 | Kronmark | 1 | Crown heartland |
| T4 | Grauwald | 1 | Highland timber |
| T5 | Feldmark | 1 | Breadbasket |
| T6 | Stillhelm | 1 | Southern farmland, Askeheim gate |
| T7 | Rendstad | 1 | Timber valley |
| T11 | Halvardshelm | 1 | Central fjords |
| T13 | Oastad | 1 | Southern fjords, Askeheim gate |
| T17 | Halvarshelm | 1 | Northern mines |
| T15 | Askeheim | 0 | Cannot be seized or held conventionally |
| T16 | Schoenland | — | Island — not in territorial play |
| **Total** | | **30** | |

[EDITORIAL: TCV values differ from opus proposal (which had total 25). Gransol raised from 3→4 to reflect Hafenmark's industrial significance. Spartfell raised from 1→2 as a strategic chokepoint. This gives a more differentiated landscape and raises the total available pool, allowing finer-grained victory thresholds.]

---

## 3. Victory Conditions — All Factions

### 3.1 Crown — Constitutional Sovereignty

**Design logic (Almud = Liu Bei):** Crown wins by being the legitimate government of a stable, unified Valoria. This requires broad territorial control, suppression of existential threats (Church overreach AND Altonian invasion), AND political legitimacy via functioning institutions. Crown victory is the hardest solo path because it requires suppressing everyone — eradication, surrender, or Crown-favourable treaties.

#### Primary Victory — Constitutional Sovereignty

**All of the following must be met simultaneously at Accounting:**

| Condition | Threshold | Rationale |
|-----------|-----------|-----------|
| **TCV held** | ≥ 18 | 60% of available TCV — broad territorial dominance |
| **Crown Mandate** | ≥ 5 | Institutional authority at peak |
| **TC** | < 50 | Church does not dominate spiritual life |
| **IP** | < 60 | Altonia is not at the gates |
| **PI** | ≥ 4 | Parliamentary institutions function |
| **CV alignment** | ≥ 3 territories held at CV 3–4 | Crown governs a moderate, secular-leaning populace — not theocratic (CV 5) nor revolutionary (CV 0–1) |

**Holding requirement:** 2 consecutive seasons at Accounting.

**Design notes:**
- TCV ≥ 18 at starting control = Crown holds T1(5)+T2(1)+T3(2)+T5(1)+T6(1)+T14(2) = 12. Needs +6 TCV via conquest/diplomacy — at least 2 significant targets or 6 minor ones.
- TC < 50 forces Crown to actively suppress Church throughout the game. This is a sustained commitment, not a one-time check.
- IP < 60 forces Crown to manage the Altonian threat — either through military readiness, diplomacy, or Schoenland relationships.
- CV 3–4 band means Crown cannot ally with Church to push CV to 5 everywhere (that helps Church, not Crown) nor let CV collapse to 0–1 (that fuels RM). Crown governs the moderate centre.
- The hardest victory condition in the game. Equal win probability is achieved not by making this easier but by making Crown's tools more flexible (Royal Decree, highest starting Mandate, Ehrenfeld military hinge).

#### Alternate Victory — Dominion

**Control ≥ 10 territories (TCV ≥ 22) AND one Submission Condition:**
- Every other playable faction has Mandate ≤ 2, OR
- Crown has formal treaties with all surviving factions (treaty terms favour Crown: at minimum, mutual defence + Crown trade priority).

**Holding requirement:** 2 consecutive seasons.

**Design notes:** This is the "eradication or surrender" path. It is harder than Constitutional Sovereignty in territorial terms (22 vs 18 TCV) but does not require TC/IP/PI maintenance. A pure conquest path for players who want to overwhelm the peninsula.

---

### 3.2 Church of Solmund — Solmundan Orthodoxy

**Design logic:** Church wins by achieving theocratic territorial consolidation — the peninsula governed under orthodox Solmundan faith. The TC clock is Phase 1 (accumulation). TC ≥ 75 triggers Phase 2 (territorial seizure). Church must then hold enough territory at high CV to declare victory.

Per opus_design_proposal.md §2–4. Reproduced with confirmed decisions integrated.

#### Primary Victory — Territorial Consolidation (TC ≥ 75 phase transition)

**Phase 1 — Accumulation (TC 0–74):** Church accumulates TC through institutional momentum (+1 passive/season), Conviction Yield (per-territory CV-based TC gain), and Assert actions. Hafenmark may Suppress (negate passive +1 for one season). TC generation per opus_design_proposal.md §3.

**Phase 2 — Consolidation (TC ≥ 75):** TC freezes at 75. Neither side can increase or decrease TC by passing a season. The game shifts from clock-watching to territorial seizure.

**Victory condition:** Church holds territories whose TCV sum ≥ **18** AND all held territories have CV ≥ 3.

**Holding requirement:** 2 consecutive seasons at Accounting.

**Church Seizure Ob:** Per opus_design_proposal.md §2. Ob = 2 + Fort Level + max(0, 3 − CV). Prominence required (Church Mandate > controlling faction's Mandate in territory).

**Design notes:**
- TCV ≥ 18 with CV ≥ 3 everywhere means Church cannot just grab low-CV territories. It must Preach/Consecrate to raise CV before or after seizure.
- Church starts with T9 (TCV 3, CV 5). Needs +15 TCV. This requires seizing ~4 significant territories or many minor ones.
- Hafenmark suppression is a voluntary trade-off. Church gain outstrips Hafenmark unless Hafenmark actively sacrifices other activities to suppress. Once TC 75 is reached, suppression is moot — TC is frozen.
- Church/Hafenmark are structurally blind to RS crisis. Church can win while RS trends toward 0. This makes Church victory narratively fragile — it may win the game but "lose the world."

#### Alternate Victory — Altonian Theocracy Path

Per opus_design_proposal.md §4.2. AEA clock 0–5. Victory at AEA = 5 + TC ≥ 60 + Church controls T9 (Himmelenger).

#### Hollow Victory — Church + Hafenmark Partition (ED-304)

**Trigger:** Crown Mandate ≤ 1 AND TC ≥ 50 AND Church controls ≥ 2 territories AND Hafenmark controls ≥ 3 territories AND no active military conflict between Church and Hafenmark.

**Outcome:** Church agrees to leave Hafenmark alone; Hafenmark agrees to leave Church alone. Hafenmark gets Varfell territories; Church gets Crown territories. Conditional co-victory for both factions — a negotiated partition. Better than a loss, worse than a solo win.

---

### 3.3 Hafenmark — Baralta's Sovereignty

**Design logic (Baralta = Catherine/Isabella):** Baralta is a cadet branch of the Almqvist royal house. She can win by institutional capture (parliamentary authority that makes the Crown irrelevant), by dynastic assertion (forcing Almqvist to resign and claiming the throne), or by reformed governance (demonstrating that Hafenmark's constitutional model is superior). Hafenmark is landlocked, militarily weak, but economically and institutionally strong.

#### Primary Victory — Reformed Sovereignty

**All of the following must be met simultaneously at Accounting:**

| Condition | Threshold | Rationale |
|-----------|-----------|-----------|
| **TCV held** | ≥ 14 | Hafenmark doesn't need the whole peninsula — it needs enough to prove its model works |
| **Hafenmark Mandate** | ≥ 4 | Parliamentary authority is functioning |
| **PI** | ≥ 5 | Institutions are healthy |
| **Crown Mandate** | ≤ 3 | Crown's institutional authority has been eclipsed |
| **CV alignment** | ≥ 3 territories held at CV 2–4 | Reformed territory — neither fully orthodox nor fully Restoration. Hafenmark governs the pragmatic centre. |
| **No active Heresy Investigation targeting Hafenmark** | — | Church has either failed to prosecute or Hafenmark has survived investigation |

**Holding requirement:** 2 consecutive seasons.

**Design notes:**
- TCV ≥ 14 at starting control = Hafenmark holds T7(1)+T8(4)+T10(2)+T17(1) = 8. Needs +6 TCV — achievable by taking Gransol's neighbours plus one significant territory.
- Crown Mandate ≤ 3 means Hafenmark must actively undermine Crown authority. This can be done through Parliamentary Votes, Reformed Settlement, or Baralta's dynastic claim.
- CV 2–4 band means Hafenmark cannot rely on Church (CV 5) or RM (CV 0–1). It governs the reformed middle — faith is lived, not mediated.
- Lower TCV threshold than Crown (14 vs 18) reflects that Hafenmark's victory is about institutional quality, not territorial quantity. Balanced by the Crown Mandate ≤ 3 requirement, which forces active conflict.

#### Alternate Victory — Dynastic Assertion (ED-307)

**All of the following must be met simultaneously at Accounting:**

| Condition | Threshold | Rationale |
|-----------|-----------|-----------|
| **Crown Mandate** | ≤ 1 | Almqvist's authority has collapsed |
| **Baralta controls T1 (Valorsplatz)** | — | Baralta occupies the capital |
| **Hafenmark Mandate** | ≥ 5 | Peak institutional authority |
| **Torben Loyalty** | ≤ 3 OR Torben removed from play | Almqvist's heir is either alienated or eliminated |
| **PI** | ≥ 4 | Institutions support the dynastic transition |

**Holding requirement:** 2 consecutive seasons.

**Narrative:** Baralta forces Almqvist to resign (Crown Mandate ≤ 1 = institutional collapse), occupies Valorsplatz, and claims the throne by dynastic right as cadet branch. Almqvist's children must give up their claim (Torben Loyalty ≤ 3 = Torben has been alienated from Crown) or be dead. This is Catherine's coronation — Baralta's assertion of sole sovereignty.

---

### 3.4 Varfell — Vaynard's Three Paths

**Design logic (Vaynard = Reinhardt/Brigandine Vaynard):** Vaynard is a conqueror who may discover the Thread path. Three victory paths represent three possible arcs: intelligence hegemon, Southernmost steward, or Thread master. All three require Thread awareness (VTM ≥ 2+) but to different degrees.

Per opus_design_proposal.md §6, redesigned with territorial dominance integration.

#### Path A — Intelligence Hegemony

**All of the following must be met simultaneously at Accounting:**

| Condition | Threshold | Rationale |
|-----------|-----------|-----------|
| **TCV held** | ≥ 14 | Varfell controls enough peninsula to be a power |
| **VTM** | ≥ 3 | Thread awareness provides intelligence advantage |
| **All other factions' stats revealed at least once** | — | Varfell has penetrated every rival's intelligence |
| **Varfell controls ≥ 1 territory outside starting 4** | — | Varfell has expanded beyond the fjords |

**Holding requirement:** 2 consecutive seasons.

**Design notes:**
- TCV ≥ 14 at starting control = Varfell holds T4(1)+T11(1)+T12(3)+T13(1) = 6. Needs +8 TCV — significant expansion required. Varfell starts with the fewest TCV points of any faction.
- Equal win probability is achieved by Varfell's intelligence advantages: Patience Protocol, VTM-based Intel, and Riskbreaker network. Varfell's low starting TCV is compensated by the ability to see what others cannot and act on perfect information.

#### Path B — Southernmost Dominion

Per opus_design_proposal.md §6.1. 3 Deeds: Extend the Reach (T13+T15 garrison, VTM ≥ 2), Walk the Wound (Southernmost Expedition, VTM ≥ 3, Warden Cooperation ≥ 1), Keeper's Mandate (T13 at CV ≤ 1 + WA ≥ +1 for 2 seasons, VTM ≥ 3).

**Blocked if RM has emerged (WA ≤ −2).**

**Additional condition (territorial dominance integration):** Varfell must also hold TCV ≥ 8 (minimum viable territorial control — Varfell starting TCV + T15 garrison counts as +0 TCV but satisfies the "stewardship not conquest" narrative).

#### Path C — Thread Supremacy

Per opus_design_proposal.md §6.2. 3 Deeds: Thread Mastery (VTM = 5), Territorial Command (T4+T13+≥1 other), World Intact (RS ≥ 50).

**Additional condition (territorial dominance integration):** Varfell must hold TCV ≥ 10.

---

### 3.5 Restoration Movement — People's Victory (5 players only)

**Design logic:** RM is the hardest faction. It has no military, minimal institutional backing, and must build from nothing. Its victory is about cultural transformation — replacing orthodox Solmundan faith with recovered Einhir identity across enough of the peninsula that the old order becomes irrelevant.

#### Primary Victory — Cultural Restoration

**All of the following must be met simultaneously at Accounting:**

| Condition | Threshold | Rationale |
|-----------|-----------|-----------|
| **Territories at CV ≤ 1** | ≥ 5 | Orthodox conviction has collapsed in a third of the peninsula |
| **RS** | ≥ 40 | The world is still intact — RM is not destroying the rendering, it is restoring Einhir stewardship |
| **RM Presence markers** | ≥ 5, in ≥ 5 non-adjacent territories | Grassroots network, not territorial concentration |
| **Held for 2 consecutive seasons** | — | Sustained, not flash |

**Design notes:**
- This is the old Network Victory with CV integration. 5 territories at CV ≤ 1 is achievable but requires sustained Cultural Reclamation and Community Weaving across the peninsula.
- RS ≥ 40 is the critical tension: Community Weaving produces RS effects. Over-Weaving can crash RS. RM must be judicious.
- No TCV requirement — RM does not hold territory conventionally. Presence markers represent cultural influence, not administrative control.
- Hardest victory in the game. Equal win probability is NOT achieved for RM — RM is explicitly "hardest mode" (BALANCE-001).

---

### 3.6 Löwenritter — Regency (conditional faction)

**Unchanged from current design.** Löwenritter enters post-coup. Regency Resolution (5 Deeds + legitimate successor) or Military Consolidation (≥8 territories + Military ≥ 5 + RS > 35 + TC < 60). Regency Resolution almost requires co-victory. This is intentional — Löwenritter is a regency faction, not a conquest faction.

---

## 4. Co-Victory Pairings (Replaces v04 B15)

| Pair | Conditions | Narrative |
|------|-----------|-----------|
| **Crown + Hafenmark** | Crown TCV ≥ 14 AND Hafenmark TCV ≥ 10 AND PI ≥ 5 AND TC < 50 AND both factions hold at CV 3–4 territories | Constitutional coalition — moderate, secular, stable |
| **Crown + Varfell** | Crown TCV ≥ 14 AND Varfell TCV ≥ 8 AND VTM ≥ 3 AND RS ≥ 50 | Intelligence alliance — Crown governs, Varfell watches |
| **Varfell + RM (latent)** | Per opus_design_proposal.md §7. VTM ≥ 4, WA ≥ +2, ≥ 4 territories CV ≤ 1, RS ≥ 40, Warden Cooperation ≥ 2, Varfell controls T13. | Einhir Restoration — Vaynard and the movement recover Einhir culture |
| **Hafenmark + RM** | Hafenmark TCV ≥ 10 AND ≥ 4 territories CV ≤ 2 AND PI ≥ 4 AND RS ≥ 40 | Reformed coalition — parliamentary governance + cultural restoration |
| **Löwenritter + Hafenmark** | Regency Resolution (all 5 Deeds) AND Hafenmark PI ≥ 4 AND Hafenmark TCV ≥ 8 | Regency Alliance — institutional restoration |
| **Church + Hafenmark (Hollow)** | See §3.2 Hollow Victory. Crown Mandate ≤ 1, TC ≥ 50, Church ≥ 2 territories, Hafenmark ≥ 3, no active conflict. Hafenmark gets Varfell; Church gets Crown. | Negotiated partition — conditional win for both |

**Incompatible pairings:** Crown + Church, Crown + Löwenritter, Church + Varfell, Church + RM.

---

## 5. RS as Existential Threat (BALANCE-004 Integration)

**The Southernmost is the existential threat that gives RS its teeth.**

If no faction engages with Askeheim (T15) to help the Wardens, RS trends toward 0 and a second Calamity occurs. This creates a global spoiler dynamic: someone must invest in RS maintenance or everyone loses.

**Thread Sensitivity (TS) power/consequence nexus:** Increasing TS makes practitioners increasingly powerful and influential across the world. But Thread operations produce co-movement consequences (P-01) that can accelerate RS decline. Power has a cost. Being judicious with threadwork — Mending, careful use — is the only way to gain Thread power without destroying the world.

**RS = 0:** Rendering Stability Rupture. Shared loss for all factions (existing mechanic). The world tears open. No winner.

**Board game incentive to engage T15:**
- Warden Cooperation track (0–3). Advancing WC requires Southernmost Expedition or Domain Actions directed at T15 via T6 or T13.
- WC ≥ 1: +1D to all Thread operations peninsula-wide (Wardens share knowledge).
- WC ≥ 2: RS decay rate halved (Warden stabilisation efforts).
- WC ≥ 3: RS +2/season at Accounting (active Warden intervention).
- Several victory conditions require RS thresholds (Crown: implicitly via stability, Varfell Path B/C, RM, co-victories). A faction that ignores RS risks losing to Rupture.

---

## 6. Shared Loss Conditions

| Condition | Trigger | Outcome |
|-----------|---------|---------|
| **Rendering Stability Rupture** | RS = 0 at Accounting | All factions lose. Second Calamity. |
| **Altonian Conquest** | IP ≥ 100 AND AER ≤ 1 | Altonia annexes Valoria. All factions lose. |
| **Total Institutional Collapse** | All playable factions at Stability 0 simultaneously | No functioning government. Anarchy. |

---

## 7. Dissolution of Deed System

The Deed checklist system is **dissolved** for Crown, Church, Hafenmark, and Varfell. Victory is now expressed as simultaneous conditions that must be held for 2 consecutive seasons.

**What changes:**
- No more "Deed Tokens" as physical game components for Crown/Church/Hafenmark/Varfell.
- No more "Hollow Victory modifier reduces effective Deed count" — Hollow Victory is now a specific Church+Hafenmark partition outcome (ED-304).
- Löwenritter retains its 5-Deed structure (it is a conditional faction with a different victory rhythm — Deeds make sense for its "restore legitimacy" arc).
- RM retains its Network Victory structure (presence markers, not Deeds).

**What stays:**
- Victory declaration at Accounting Step 12 (unchanged).
- 2-season holding requirement for all primary victories (standardized — was present for some paths, now universal).
- Co-victory pairings (restructured, see §4).
- Shared loss conditions (unchanged).

---

## 8. Conviction Track (CV) — Movement Actions (Full Reference)

Per opus_design_proposal.md §1.2. Reproduced for completeness.

| Action | Faction(s) | Direction | Condition | Ob | Effect |
|--------|-----------|-----------|-----------|-----|--------|
| Preach | Church | CV +1 | Church prominent in territory | Influence vs Ob 2 | CV +1 in target territory |
| Suppress Heresy | Church | CV +1 | Territory CV ≤ 2 | Influence vs Ob 3 | Success: CV +1. Failure: CV −1 (backlash) |
| Cultural Reclamation | Varfell | CV −1 | Varfell controls territory OR Einhir presence | Influence vs Ob 2 | CV −1 in target territory |
| Community Weaving | RM | CV −1 | Territory CV ≤ 3 | See RM rules | CV −1 (plus RS effects) |
| Secular Governance | Hafenmark | CV −1 | Hafenmark controls territory | Mandate vs Ob 2 | CV −1. Cannot reduce below 2 via this action. |
| Consecrate | Church | CV +1 | Church controls territory AND CV ≥ 3 | Influence vs Ob 3 | CV +1. Territory becomes Consecrated. |
| Missionary Work | Church | CV +1 | Territory not Church-controlled, CV ≤ 3 | Influence vs Ob = controlling faction Mandate | CV +1 |

**Frequency:** One CV movement action per faction per season (not per territory).

**Crown CV tool:** Crown does not have a dedicated CV movement action. Crown's CV influence is indirect: Royal Decree can target factions whose actions affect CV; Crown's moderate governance (CV 3–4 band) is maintained by preventing Church Preaching and RM Weaving in Crown territories. This is intentional — Crown governs the centre by blocking extremes, not by pushing in either direction.

---

## 9. Church Seizure Ob (Full Reference)

Per opus_design_proposal.md §2.

**Trigger:** TC ≥ 75. Once per season per eligible territory.

**Eligibility:** Church prominent (Church Mandate > controlling faction's Mandate in territory). Church Mandate ≥ 4.

**Ob = 2 + Fort Level + max(0, 3 − CV)**

Fort levels per geography_design.md:

| Territory | Fort Level |
|-----------|-----------|
| T1 (Valorsplatz) | 2 |
| T3 (Lowenskyst) | 3 (max 4) |
| T8 (Gransol) | 1 |
| T10 (Spartfell) | 2 |
| T12 (Sigurdshelm) | 1 |
| T14 (Ehrenfeld) | 3 (max 4) |
| T16 (Schoenland) | 1 |
| All others | 0 |

**Example Ob calculations:**

| Target | Fort | CV | Ob | Notes |
|--------|------|-----|-----|-------|
| T2 (Kronmark, CV 4) | 0 | 4 | 2+0+0 = **2** | Easy seizure — high faith, no fort |
| T1 (Valorsplatz, CV 4) | 2 | 4 | 2+2+0 = **4** | Capital fortified |
| T14 (Ehrenfeld, CV 4) | 3 | 4 | 2+3+0 = **5** | Military fortress — very hard |
| T4 (Grauwald, CV 2) | 0 | 2 | 2+0+1 = **3** | Low faith adds resistance |
| T13 (Oastad, CV 2) | 0 | 2 | 2+0+1 = **3** | Same |
| T15 (Askeheim, CV 0) | 0 | 0 | 2+0+3 = **5** | Near impossible — population fully Einhir |

---

## 10. TC Generation (Full Reference)

Per opus_design_proposal.md §3. Starting TC 28. Phase transition at TC 75.

Seasonal TC at Accounting:
1. **Institutional Momentum (passive):** TC +1.
2. **Conviction Yield:** For each territory where Church is prominent, add TC based on CV (CV 5 = +1, CV 4 = +0.5, others = 0). Total = floor(sum).
3. **Assert (optional Church action):** Influence vs Ob 2. Success: TC +1. Failure: Stability −1.
4. **Suppress (optional opponent action):** One faction, Mandate vs Ob = Church Mandate. Success: negate Step 1 passive +1. Failure: Stability −1.
5. **Hafenmark Structural Suppression:** While Baralta Mandate ≥ 4: TC −1/season.

**TC freeze at 75.** No further TC changes from any source once TC ≥ 75.

---

## 11. RM Emergence

Per opus_design_proposal.md §5. Warden's Accord (WA) −3 to +3, starts at 0 (ED-305). Triple-condition emergence trigger: WA ≤ −2 AND ≥ 3 territories CV ≤ 1 AND RS ≤ 50. One-shot emergence. Suppression conditions: WA ≥ 0 OR all territories CV ≥ 2 OR RM Stability 0.

---

## 12. Gaps and Simulation Debt

| Gap | Description | Priority |
|-----|-------------|----------|
| [SIM-DEBT] TC pacing | TC 75 timeline (~S20) is analytical. Needs faction AI simulation. | P1 |
| [SIM-DEBT] AEA pacing | Altonian Theocracy clock — achievable but not trivial? | P2 |
| [SIM-DEBT] RM emergence frequency | Triple condition may be too restrictive or permissive. | P2 |
| [SIM-DEBT] Community Weaving feedback loop | CV −1 + RS effect. Positive feedback risk. | P1 |
| [SIM-DEBT] TCV balance | Are TCV thresholds (18/14/14/8/10) balanced for equal win probability? | P1-BLOCKER |
| [SIM-DEBT] Crown moderate-CV maintenance | Crown has no direct CV tool. Can it maintain CV 3–4 passively? | P2 |
| [SIM-DEBT] Calamity Drift cascade | At RS ≤ 20, all territories CV −1/season. Combined with ongoing Thread ops, RS may crater too fast. | P2 |
| [GAP] Hafenmark Secular Governance floor | Cannot reduce CV below 2. Is this the right floor for RM co-victory? | P2 |
| [GAP] Consecrated interaction with seizure | −1 Ob on seizure + CV 5 requirement. May make high-CV territories too easy. | P2 |
| [GAP] Crown alternate victory submission conditions | "Formal treaties favour Crown" needs mechanical definition. | P2 |
| [GAP] Warden Cooperation advancement mechanics | How exactly does WC advance? Needs specification. | P2 |

---

## 13. Patch Summary

| PP | Scope | Description |
|----|-------|-------------|
| PP-406 | Track | CV starting values (from opus doc) |
| PP-407 | Track | T15 hard-fix rule |
| PP-408 | Track | CV movement rules |
| PP-409 | Track | Calamity Drift |
| PP-410 | Track | Consecrated status |
| PP-411 | Seizure | Church Seizure Ob redesign |
| PP-412 | TC | TC generation redesign |
| PP-413 | Victory | Church Primary Victory — TC 75 → TCV ≥ 18 + CV ≥ 3 |
| PP-414 | Victory | Altonian Theocracy Path |
| PP-415 | Victory | Hollow Victory (Church + Hafenmark partition) (ED-304) |
| PP-416 | RM | RM Emergence via Warden's Accord |
| PP-417 | Varfell | Path B/C redesign |
| PP-418 | Co-Victory | Einhir Restoration Co-Victory |
| PP-419 | Victory | Crown Constitutional Sovereignty — TCV ≥ 18 + conditions |
| PP-420 | Victory | Crown Dominion (alternate) — TCV ≥ 22 + submission |
| PP-421 | Victory | Hafenmark Reformed Sovereignty — TCV ≥ 14 + conditions |
| PP-422 | Victory | Hafenmark Dynastic Assertion (ED-307) — capital seizure + lineage |
| PP-423 | Victory | RM Cultural Restoration — 5 territories CV ≤ 1 + RS ≥ 40 |
| PP-424 | TCV | Territory Consolidation Values — 15 territories scored |
| PP-425 | Co-Victory | Full co-victory pairing restructure |
| PP-426 | RS | Warden Cooperation track boardgame incentive for Askeheim |
| PP-427 | System | Deed system dissolved for Crown/Church/Hafenmark/Varfell |
