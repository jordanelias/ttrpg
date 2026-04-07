# VALORIA BG — Victory Architecture
## ED-306 Resolution (v2)
## Date: 2026-04-06 | Status: DESIGN PROPOSAL — User Review Required
## Supersedes: v1 (same path), params_board_game.md §Victory Conditions, all Deed-based victory systems
## Dependencies: ED-302 (CV confirmed), ED-303 (TC freeze at 75), ED-304 (Partition Victory), ED-305 (WA=0), ED-307 (Baralta cadet branch), BALANCE-001 (equal win probability), BALANCE-004 (Askeheim purpose)
## Source: opus_design_proposal.md (PP-406–PP-418) + user decisions 2026-04-06 + audit findings

---

## Core Frame

This is a game about conquering a peninsula — or at worst, being a co-owner of it. Every faction wins by holding enough territory under conditions that match their vision. The Deed checklist system is dissolved for ALL factions including Löwenritter.

Victory = Territory Held + Faction-Specific Political Conditions, sustained for 2 consecutive Accounting steps.

Two simultaneous contests: who governs the peninsula AND whether it survives. Church and Hafenmark are structurally blind to the Rendering Stability (RS) crisis — they can win fast but their victory is fragile if RS collapses. Crown and Varfell can address RS via Thread path but at cost of political resources.

**Equal win probability** for Crown, Varfell, Hafenmark. Church is the easy/hard mode toggle. Restoration Movement (RM) is hardest mode. (BALANCE-001)

---

## 1. Territory Consolidation Values (TCV)

Every territory has a fixed strategic weight. TCV is the universal measure of territorial dominance.

| T# | Territory | TCV | Controller |
|----|-----------|-----|-----------|
| T1 | Valorsplatz | 5 | Crown |
| T8 | Gransol | 4 | Hafenmark |
| T9 | Himmelenger | 3 | Church |
| T12 | Sigurdshelm | 3 | Varfell |
| T3 | Lowenskyst | 2 | Crown |
| T10 | Spartfell | 2 | Hafenmark |
| T14 | Ehrenfeld | 2 | Crown |
| T2 | Kronmark | 1 | Crown |
| T4 | Grauwald | 1 | Varfell |
| T5 | Feldmark | 1 | Crown |
| T6 | Stillhelm | 1 | Crown |
| T7 | Rendstad | 1 | Hafenmark |
| T11 | Halvardshelm | 1 | Varfell |
| T13 | Oastad | 1 | Varfell |
| T17 | Halvarshelm | 1 | Hafenmark |
| T15 | Askeheim | 0 | Uncontrolled |
| T16 | Schoenland | — | Not in territorial play |
| | **Total** | **30** | |

**Starting TCV by faction:** Crown 12, Hafenmark 8, Varfell 6, Church 3.

---

## 2. Conviction Track (CV)

Per opus_design_proposal.md §1. Range 0–5 per territory. 0 = Restoration pole, 5 = Piety pole.

Starting values, movement rules, Calamity Drift, and Consecrated status per opus_design_proposal.md §1.1–1.4.

Key points:
- T15 (Askeheim) CV hard-fixed at 0. Cannot increase. Justification: P-03 + Foundations §8 — rendering capacity in the Southernmost is structurally compromised; orthodox conviction cannot be sustained where the rendering of ordinary experience fails.
- T9 (Himmelenger) starts at 5, soft cap — can drop under pressure, does not auto-recover.
- CV ±1 per territory per season (cap). One CV movement action per faction per season.
- Calamity Drift (RS-linked CV erosion) ignores the ±1 cap. RS ≤ 50: T6/T13 CV −1. RS ≤ 35: within 2 steps of T15 CV −1. RS ≤ 20: all territories CV −1.
- Community Weaving is a Thread operation: it follows the standard Thread operation procedure including Co-Movement card draw. The CV −1 is the intended primary effect; temporal/epistemic/actual auto-effects fire as standard P-01 consequences.

---

## 3. Victory Conditions — All Factions

Every victory requires holding conditions for **2 consecutive Accounting steps** (not seasons — Accounting). A faction that meets all conditions can be knocked out during the intervening season, which resets the 2-Accounting counter.

### 3.1 Crown — Peninsula Sovereignty (Almud = Liu Bei)

Crown wins by ruling the peninsula with no credible rival. This is the hardest solo victory. Every other faction must be suppressed, including managing the Altonian threat. Eradication, surrender, or Crown-favourable treaties.

**All conditions simultaneous at Accounting:**

| Condition | Threshold | Rationale |
|-----------|-----------|-----------|
| TCV held | ≥ 20 | Crown controls two-thirds of the peninsula |
| Rival suppression | Every other playable faction: Mandate ≤ 2 OR eliminated OR formal Crown treaty in effect | No credible political rival remains |
| IP | < 60 | Altonia is contained |
| PI | ≥ 3 | Institutions still function (Crown is not a tyrant — it is a constitutional monarchy) |

**Formal Crown Treaty:** A Domain Action (Diplomacy, Ob = target faction's Mandate). Both factions must agree. Treaty terms: target faction acknowledges Crown sovereignty, gains +1 Stability, loses 1 Mandate immediately. Treaty is permanent unless Crown breaks it (Crown Stability −2, Mandate −1) or target faction's Mandate reaches 0 (treaty dissolves — faction has collapsed).

**Why no CV condition:** Crown is a secular monarchy. It governs through political authority (Mandate), not ideological alignment (CV). Crown's interest in CV is purely defensive — extreme CV in either direction empowers rivals (Church at high CV, RM at low CV). Crown fights ideological threats through political tools (Royal Decree, Domain Actions, military conquest), not through preaching or cultural programs.

**Design notes:**
- Starting position: TCV 12 (needs +8). Mandate already 5 (but must ALSO suppress 3 rivals). IP 20 (met). PI 7 (met).
- TCV +8 = 4–6 conquests over ~10–15 seasons.
- Suppressing 3 factions from Mandate 4–5 to Mandate ≤ 2: requires ~3 successful hostile Domain Actions per faction = ~9 total. At ~1/season with opposition, this takes 12–18 seasons.
- Territory conquest and faction suppression overlap: conquering a faction's territory reduces its stats. Crown's path is to conquer outward while rivals weaken.
- Crown's total timeline: ~15–18 seasons. The hardest path, achievable in a 20-season game, tight in a 15-season game.

#### Alternate — Dominion

TCV ≥ 22 AND every other playable faction eliminated (Stability 0). No treaties, no negotiation. Pure conquest. Harder than Peninsula Sovereignty but requires no diplomacy.

---

### 3.2 Church of Solmund — Solmundan Orthodoxy

Church wins through TC accumulation → phase transition → territorial seizure → consolidation under orthodox faith. Two phases of play: the accumulation clock and the seizure campaign.

**Phase 1 (TC 0–74):** Accumulate TC via institutional momentum, Conviction Yield, and Assert actions. Per opus_design_proposal.md §3.

**Phase 2 (TC ≥ 75):** TC freezes at 75. Church shifts to territorial seizure. Remaining "TC 75→100" is peninsula conquest, not clock advancement.

**Victory conditions (all simultaneous at Accounting, post-TC 75):**

| Condition | Threshold | Rationale |
|-----------|-----------|-----------|
| TCV held | ≥ 18 | Church controls 60% of available TCV |
| CV in all held territories | ≥ 3 | Orthodox population supports Church governance |

**Church Seizure Ob:** Per opus_design_proposal.md §2. Ob = 2 + Fort Level + max(0, 3 − CV). Prominence required (Church Mandate > controlling faction's Mandate in territory). Church Mandate ≥ 4. On Overwhelming seizure: CV +1 in target territory (population rallies to Church governance).

**Design notes:**
- Starting position: TCV 3 (needs +15). TC 28 (needs 47 to reach 75).
- TC timeline: ~16–20 seasons to TC 75 (per opus_design_proposal.md §3 pacing analysis).
- Post-TC 75 seizure: Influence 6 pool against Ob 2–5 depending on Fort and CV. In unforted CV ≥ 3 territory, Ob 2 = ~80% success at pool 6. Church can seize 1–2 territories per season.
- +15 TCV via seizure = ~8–12 seizures over ~5–8 seasons. Total: ~22–25 seasons.
- This is LONG. Church is designed as hard mode. Church wins if the game goes long and no one stops TC. Church's presence makes the game interesting for everyone else — the TC clock forces collective response.
- Church can accelerate via Conviction Yield (raising CV in target territories before seizing) and Altonian Theocracy Path (alternate victory requiring less territory).

#### Alternate — Altonian Theocracy Path

Per opus_design_proposal.md §4.2. Altonian Ecclesiastical Accord (AEA) clock 0–5. Victory: AEA = 5 + TC ≥ 60 + Church controls T9 (Himmelenger). Requires less territory (only T9 mandatory) but more diplomatic conditions. This is the faster Church path in games where territorial seizure is blocked.

#### Partition — Church + Hafenmark (ED-304)

**Trigger (all simultaneous at Accounting):**
- Crown Mandate ≤ 1
- TC ≥ 50
- Church controls ≥ 2 territories
- Hafenmark controls ≥ 3 territories
- No active military conflict between Church and Hafenmark

**Outcome:** Church agrees to leave Hafenmark alone; Hafenmark agrees to leave Church alone. Hafenmark gets Varfell territories; Church gets Crown territories. Both factions score a conditional victory — better than a loss, worse than a solo win. Game ends.

**No holding requirement** — this is a mutual agreement, not a sustained state. Once declared, both factions win.

---

### 3.3 Hafenmark — Parliamentary Sovereignty (Baralta = Catherine/Isabella)

Hafenmark wins by proving parliamentary governance works while eclipsing Crown authority. Baralta is a cadet branch of the Almqvist royal house — her victory is institutional capture that makes the monarchy irrelevant.

**All conditions simultaneous at Accounting:**

| Condition | Threshold | Rationale |
|-----------|-----------|-----------|
| TCV held | ≥ 14 | Hafenmark controls nearly half the peninsula |
| Hafenmark Mandate | ≥ 4 | Parliamentary authority is functioning |
| PI | ≥ 5 | Institutions are healthy |
| Crown Mandate | ≤ 3 | Crown's institutional authority has been eclipsed |

**Design notes:**
- Starting position: TCV 8 (needs +6). Mandate 4 (met). PI 7 (met). Crown Mandate 5 (must bring to ≤ 3).
- TCV +6 = 3–4 conquests over ~8–12 seasons.
- Crown Mandate suppression: from 5 to 3 requires ~2–3 successful hostile Domain Actions. Achievable in ~4–6 seasons.
- Total timeline: ~10–14 seasons. Middle difficulty.
- Hafenmark's Military 3 is the weakest of the playable factions. Hafenmark must use Wealth (economic pressure, Trade Network Investment) and Influence (Parliamentary Votes, Diplomacy) to expand rather than brute force. This is intentional — Hafenmark wins through institutions, not armies.

#### Alternate — Dynastic Assertion (ED-307)

Baralta seizes the throne by dynastic right as cadet branch of the Almqvist house. Almqvist must resign and his children must give up their claim (or die).

**All conditions simultaneous at Accounting:**

| Condition | Threshold | Rationale |
|-----------|-----------|-----------|
| TCV held | ≥ 12 | Hafenmark controls enough territory to govern |
| Crown Mandate | ≤ 1 | Crown's authority has collapsed completely |
| Hafenmark controls T1 (Valorsplatz) | — | Baralta occupies the capital |
| Hafenmark Mandate | ≥ 5 | Peak institutional authority |
| Torben Loyalty | ≤ 3 OR Torben removed | Almqvist's heir is alienated or eliminated |

**Design notes:** Harder territorial condition than Reformed Sovereignty (must take Valorsplatz, TCV 5) but lower total TCV (12 vs 14). The difficulty is political: Crown Mandate ≤ 1 requires near-complete institutional collapse. This path is for games where Crown is already weakened and Baralta can deliver the killing blow.

---

### 3.4 Varfell — Vaynard's Three Paths (Vaynard = Reinhardt/Brigandine Vaynard)

Varfell starts isolated with the lowest TCV (6). Three victory paths represent three arcs for Vaynard: intelligence hegemon, Southernmost steward, or Thread master. All require Thread awareness and territorial expansion from the fjords.

#### Path A — Intelligence Hegemony

**All conditions simultaneous at Accounting:**

| Condition | Threshold | Rationale |
|-----------|-----------|-----------|
| TCV held | ≥ 14 | Varfell controls a major chunk of the peninsula |
| VTM | ≥ 3 | Thread awareness provides intelligence advantage |
| At least 2 rival factions' stats fully revealed | — | Varfell has penetrated rival intelligence (fixed count, player-count-invariant) |
| Varfell controls ≥ 1 territory outside starting 4 | — | Varfell has expanded |

**Design notes:** TCV +8 from 6 = 4–6 conquests over ~10–16 seasons. VTM 3 requires sustained Thread development. Stat revelation is the intelligence payoff — Varfell's Patience Protocol and Riskbreaker network are the tools. Timeline: ~14–18 seasons.

#### Path B — Southernmost Dominion

**All conditions simultaneous at Accounting:**

| Condition | Threshold | Rationale |
|-----------|-----------|-----------|
| TCV held | ≥ 8 | Minimum viable territorial control |
| Varfell controls T13 (Oastad) | — | Southern fjords — gateway to Askeheim |
| Garrison or Tribune present in T15 (Askeheim) | — | Varfell engages the Southernmost |
| VTM | ≥ 3 | Thread awareness to engage meaningfully |
| Warden Cooperation | ≥ 1 | Wardens recognise Vaynard's stewardship |
| Warden's Accord (WA) | ≥ +1 | RM trusts Vaynard |
| T13 CV | ≤ 1 | Einhir cultural identity maintained in Varfell's southern gateway |

**Blocked if RM has emerged (WA ≤ −2).** RM emergence means Vaynard has alienated the movement — stewardship path closes.

**Design notes:** Lower TCV (8 from 6 = +2) but multiple non-territorial conditions. This is the narrative path — Vaynard discovers the Thread path and becomes a genuine steward of the Southernmost rather than a conqueror. Timeline: ~12–16 seasons.

#### Path C — Thread Supremacy

**All conditions simultaneous at Accounting:**

| Condition | Threshold | Rationale |
|-----------|-----------|-----------|
| TCV held | ≥ 10 | Meaningful territorial control |
| VTM | = 5 | Peak Thread mastery |
| RS | ≥ 50 | The world is intact — Vaynard's Thread power hasn't destroyed it |

**Design notes:** VTM 5 is a multi-season investment (minimum ~S14–16 to achieve). RS ≥ 50 creates tension with Thread operations that degrade RS. TCV 10 from 6 = +4 = 2–4 conquests. Timeline: ~14–18 seasons.

---

### 3.5 Restoration Movement — Cultural Revolution (5 players only, hardest mode)

RM wins by spreading cultural restoration across the peninsula while keeping the world alive. RM does not conquer territory conventionally — it transforms the ideological landscape.

**All conditions simultaneous at Accounting:**

| Condition | Threshold | Rationale |
|-----------|-----------|-----------|
| Territories at CV ≤ 1 | ≥ 5 | Orthodox conviction has collapsed across a third of the peninsula |
| RM Presence markers | ≥ 5, in ≥ 5 non-adjacent territories | Grassroots network, not territorial concentration |
| RS | ≥ 40 | The world survives — RM stewards the rendering, not destroys it |

**Design notes:** No TCV requirement — RM operates through cultural influence (Presence markers), not administrative control. 5 territories at CV ≤ 1 requires sustained Cultural Reclamation and Community Weaving. RS ≥ 40 is the critical tension: Community Weaving produces co-movement consequences (P-01) that can degrade RS. RM must be judicious. Hardest victory in the game — RM is explicitly the challenge mode. Timeline: ~14–20 seasons.

---

### 3.6 Löwenritter — Military Regency (conditional faction, post-coup)

Löwenritter enters after the coup fires. It wins by establishing a legitimate military regency — or failing that, by holding enough territory through force alone.

#### Primary — Regency Establishment

**All conditions simultaneous at Accounting:**

| Condition | Threshold | Rationale |
|-----------|-----------|-----------|
| TCV held | ≥ 12 | Löwenritter controls enough territory for a credible government |
| TC | < 50 | Church theocratic momentum is contained |
| IP | < 60 | Altonia is not invading |
| RS | > 40 | The world is intact |
| PI | ≥ 4 | Institutions support the transition |
| Successor confirmed | Elske confirmed OR Torben Loyalty ≥ 6 | Legitimate succession |

**Design notes:** Löwenritter has Military 6 (highest in game) but Influence 2 and Mandate 3 (weakest political tools). Territory acquisition is fast (military strength) but political conditions require cooperation from other factions. Löwenritter depends on Crown/Hafenmark managing IP and Elske/Torben loyalty. This creates genuine co-victory incentive (Löwenritter + Hafenmark).

#### Alternate — Military Consolidation

**All conditions simultaneous at Accounting:**

| Condition | Threshold | Rationale |
|-----------|-----------|-----------|
| TCV held | ≥ 16 | Löwenritter controls over half the peninsula by force |
| Löwenritter Military | ≥ 5 | Military dominance maintained |
| RS | > 35 | World is still functional |
| TC | < 60 | Church has not consolidated |

Only available if Regency Establishment not achieved after 8 Löwenritter seasons.

---

## 4. Co-Victory Pairings

Co-victories are the "co-owner of the peninsula" outcomes. Both factions score a conditional victory — the game ends, both win, but neither achieves solo dominance.

| Pair | Conditions (all simultaneous at Accounting) |
|------|---------------------------------------------|
| **Crown + Hafenmark** | Crown TCV ≥ 14 AND Hafenmark TCV ≥ 10 AND PI ≥ 5 AND TC < 50 |
| **Crown + Varfell** | Crown TCV ≥ 14 AND Varfell TCV ≥ 8 AND VTM ≥ 3 AND RS ≥ 50 |
| **Varfell + RM** | VTM ≥ 4 AND WA ≥ +2 AND ≥ 4 territories CV ≤ 1 AND RS ≥ 40 AND Warden Cooperation ≥ 2 AND Varfell controls T13 |
| **Hafenmark + RM** | Hafenmark TCV ≥ 10 AND ≥ 4 territories CV ≤ 2 AND PI ≥ 4 AND RS ≥ 40 |
| **Löwenritter + Hafenmark** | Löwenritter TCV ≥ 8 AND Hafenmark TCV ≥ 8 AND PI ≥ 4 |
| **Church + Hafenmark (Partition)** | See §3.2. Crown Mandate ≤ 1, TC ≥ 50, Church ≥ 2 territories, Hafenmark ≥ 3, no active military conflict. |

**Incompatible:** Crown + Church, Crown + Löwenritter, Church + Varfell, Church + RM.

Co-victory pairings are distinct from operational coalition pairs (PP-404/PP-405). Coalitions are in-game alliances with mechanical benefits (combined actions, +1D). Co-victories are game-ending conditions. A faction may pursue a coalition without pursuing a co-victory, and vice versa.

Co-victories require 2 consecutive Accounting steps (same as solo victories) except the Partition, which fires immediately on mutual agreement.

---

## 5. Shared Loss Conditions

| Condition | Trigger | Outcome |
|-----------|---------|---------|
| Rendering Stability Rupture | RS = 0 at Accounting | All factions lose. Second Calamity. |
| Altonian Conquest | IP ≥ 100 AND AER ≤ 1 | Altonia annexes Valoria. All factions lose. |
| Total Institutional Collapse | All playable factions at Stability 0 simultaneously | Anarchy. All factions lose. |

---

## 6. Askeheim and RS (BALANCE-004)

If no faction engages with Askeheim (T15) to help the Wardens, RS trends toward 0 and a second Calamity occurs. The Southernmost is not dead space — it is the existential threat that gives RS its teeth.

**Thread Sensitivity (TS) power/consequence nexus:** Increasing TS makes practitioners more powerful and influential. But Thread operations produce co-movement consequences (P-01) that can accelerate RS decline if not judicious. Power costs. Mending and careful threadwork are the only way to gain Thread power without destroying the world.

**Warden Cooperation track (0–3):**
- WC ≥ 1: +1D to all Thread operations peninsula-wide.
- WC ≥ 2: RS decay rate halved.
- WC ≥ 3: RS +2/season at Accounting.

Multiple victory conditions require RS thresholds. A faction that ignores RS risks losing to Rupture regardless of territorial control.

---

## 7. TC Generation and Church Seizure

Per opus_design_proposal.md §2–3. Starting TC 28. Phase transition at TC 75 (TC freezes).

**Seasonal TC at Accounting (in order):**
1. Institutional Momentum: TC +1 (passive).
2. Conviction Yield: for each territory where Church is prominent (Church Mandate > controlling faction's Mandate), add based on CV. CV 5 = +1, CV 4 = +0.5, others = 0. Total = floor(sum).
3. Assert (optional Church action): Influence vs Ob 2. Success: TC +1. Failure: Stability −1.
4. Suppress (optional opponent action): Mandate vs Ob = Church Mandate. Success: negate Step 1 passive. Failure: Stability −1.
5. Hafenmark Structural Suppression: while Baralta Mandate ≥ 4, TC −1/season.

**Church Seizure Ob (post-TC 75):** Ob = 2 + Fort Level + max(0, 3 − CV). Prominence required. Church Mandate ≥ 4. Overwhelming seizure: CV +1 in target territory (counts against ±1 CV seasonal cap). See opus_design_proposal.md §2 for full seizure results table.

---

## 8. RM Emergence

Per opus_design_proposal.md §5. Warden's Accord (WA) −3 to +3, starts at 0. Triple-condition emergence: WA ≤ −2 AND ≥ 3 territories CV ≤ 1 AND RS ≤ 50. One-shot. Suppression: WA ≥ 0 OR all territories CV ≥ 2 OR RM Stability 0. See opus doc for full stat block and NPC AI.

---

## 9. Hybrid Mode Integration

### 9.1 CV State Transfer

CV is a per-territory stat that crosses the BG ↔ TTRPG boundary.

| Transition | CV Rule |
|-----------|---------|
| **BG → TTRPG (Zoom In)** | Current CV value for the territory is context. GM uses CV to inform NPC attitudes, crowd behaviour, and faith-related scene framing. CV is read-only during the TTRPG scene. |
| **TTRPG → BG (Zoom Out)** | CV changes from personal-scale scenes queue as Domain Echoes. One Zoom In can produce at most ±1 CV in one territory, firing at next Accounting. A single sermon or debate does not move a territory-wide population stat instantly. |
| **Calamity Drift during Zoom In** | Calamity Drift fires at Accounting. If Accounting is suspended during Zoom In, Calamity Drift queues and fires when Accounting resumes. It is a global environmental effect, not a player action — it cannot be skipped. |

Add to state_transfer_spec.md §1 Variables that TRANSFER table:

| BG Variable | TTRPG Equivalent | Transformation |
|-------------|-----------------|----------------|
| Territory CV (0–5) | Scene context (NPC attitudes, crowd faith level) | Read-only. Changes queue as Domain Echo (±1 max per Zoom In). |

Add to state_transfer_spec.md §1 Zoom Out table:

| TTRPG Outcome | BG State Update |
|---------------|----------------|
| Faith-affecting personal scene (sermon, debate about doctrine, Community Weaving) | CV ±1 in that territory, queued to Accounting. Cap: 1 CV Domain Echo per Zoom In. |

### 9.2 Victory Condition Check — Hybrid

state_transfer_spec.md §TC Win-Delay Rule must be rewritten:

**Old (INVALID):** "TC ≥ 65 = Church win fires at Accounting regardless of Zoom In."

**New:** "Victory condition checks (all factions) fire at Accounting Step 12 regardless of active Zoom In. A Zoom In cannot delay or prevent a victory declaration. The 2-Accounting holding requirement is assessed across consecutive Accounting steps — a Zoom In that spans an Accounting boundary counts that Accounting. If a faction meets victory conditions at two consecutive Accounting steps, victory is declared at the second Accounting Step 12."

### 9.3 Hybrid Victory and P-32

P-32 states: "Hybrid victory = BG victory PLUS personal arc resolution."

This principle is retained. In Hybrid mode, a BG victory (meeting all conditions in §3) is mechanically valid. If the winning faction's PC has unresolved Beliefs or Inspirations, the victory is narratively qualified — the faction won, but the character's arc is incomplete. This is a narrative marker, not a mechanical penalty. No Deed-style modifier applies.

The term "Hollow Victory" in the P-32 sense (BG win without personal arc) is distinct from the Church+Hafenmark Partition Victory (§3.2/§4). These are different concepts with different outcomes.

### 9.4 Domain Echo Autonomous Resolution (ED-300)

If ED-300's redesign is canonical (Domain Echoes = scenes available for engagement; uninvestigated echoes escalate and resolve autonomously), then autonomous resolution that changes territory control updates TCV at Accounting. Autonomous TCV changes count toward or against victory conditions. The 2-Accounting holding requirement does not exempt autonomous changes — the world moves whether or not players attend to it.

---

## 10. Win Probability Assessment

| Faction | Starting TCV | Target TCV | TCV Gap | Key Difficulty | Estimated Timeline |
|---------|-------------|------------|---------|----------------|-------------------|
| Crown | 12 | 20 | +8 | Must suppress ALL rivals to Mandate ≤ 2 | 15–18 seasons |
| Church | 3 | 18 | +15 | TC 75 timeline (~16–20 seasons) then seizure campaign | 22–25 seasons (hard mode) |
| Hafenmark | 8 | 14 | +6 | Must bring Crown Mandate from 5 to ≤ 3 | 10–14 seasons |
| Varfell A | 6 | 14 | +8 | Intelligence penetration + expansion from isolation | 14–18 seasons |
| Varfell B | 6 | 8 | +2 | VTM 3 + WA management + Warden engagement | 12–16 seasons |
| Varfell C | 6 | 10 | +4 | VTM 5 (~14+ seasons to achieve) + RS maintenance | 14–18 seasons |
| RM | — | — | — | 5 territories CV ≤ 1 + RS ≥ 40 (hardest mode) | 14–20 seasons |
| Löwenritter | varies | 12 | varies | Late entry, high Military, weak politics | depends on coup timing |

**Equal probability analysis (Crown/Hafenmark/Varfell):**
- Hafenmark ~12 seasons, Varfell ~15 seasons, Crown ~16 seasons. Crown is hardest as intended.
- Hafenmark's faster timeline is offset by Military 3 (weakest — territorial expansion is slow and expensive). Hafenmark compensates with Wealth and Influence but cannot brute-force territory.
- Varfell's medium timeline is offset by starting TCV 6 (lowest) and geographic isolation. Varfell compensates with intelligence tools and Thread capability.
- Crown's slow timeline is offset by the best starting stats and most starting territory. Crown has the strongest tools but the most demanding win condition.

**Church is explicitly hard mode.** Solo Church victory requires 22+ seasons — longer than most campaigns. Church wins in extended games or via the Altonian Theocracy alternate path (~18 seasons). Church's real role is to force the other factions to react to TC accumulation. Church is the pace-setter of the game.

[SIM-DEBT: These timelines are analytical estimates. Simulation with faction AI needed to validate equal probability. Flag as P1.]

---

## 11. Patch Summary

| PP | Scope | Description |
|----|-------|-------------|
| PP-406–418 | Various | Per opus_design_proposal.md |
| PP-419 | Victory | Crown Peninsula Sovereignty — TCV ≥ 20 + universal rival suppression + IP < 60 + PI ≥ 3 |
| PP-420 | Victory | Crown Dominion (alternate) — TCV ≥ 22 + all rivals eliminated |
| PP-421 | Victory | Hafenmark Reformed Sovereignty — TCV ≥ 14 + conditions |
| PP-422 | Victory | Hafenmark Dynastic Assertion (ED-307) |
| PP-423 | Victory | RM Cultural Restoration |
| PP-424 | TCV | Territory Consolidation Values |
| PP-425 | Co-Victory | Full co-victory pairing restructure |
| PP-426 | RS | Warden Cooperation track |
| PP-427 | System | Deed system dissolved for ALL factions including Löwenritter |
| PP-428 | Löwenritter | Regency Establishment — conditions-based (replaces 5-Deed system) |
| PP-429 | Löwenritter | Military Consolidation — conditions-based |
| PP-430 | Hybrid | CV state transfer rules |
| PP-431 | Hybrid | Victory condition check rewrite (replaces TC Win-Delay Rule) |
| PP-432 | Crown | Formal Crown Treaty mechanic |
