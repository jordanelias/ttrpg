# SIM-COMPREHENSIVE-01 — Comprehensive Simulation Batch
## Date: 2026-04-10
## Modes: A + B + C + D + G + L
## Systems: Personal Combat (Wound), Social Contest (AMPLIFY), Mass Combat (Command Cap),
##           Calamity Radiation (all modes), Clock Registry, Victory Architecture (BG),
##           Co-Victory Pairings, RM Cultural Uprising
## Status: COMPLETE

---

## BATCH A — Unpatched P1 Gap Simulations

### SIM-WOUND-01 — Wound Accumulation Ob Penalty (Modes A + D)
**System:** Personal Combat | **Source:** combat_design_v1.md + params_combat.md

**Verdict:** ED-candidate-F finding does NOT support Ob penalty patch. Pool-reduction model (−1D/wound, PP-232) is correctly calibrated for in-session wound ranges (0–4 wounds). Pool floor 5 at 8 wounds = ~54% vs Ob 4 — not a zombie state.

| Finding | Severity | Description | Action |
|---------|----------|-------------|--------|
| F-WOUND-01 | P3 | Pool floor 5 ≠ zombie state — ED-candidate-F analytically imprecise | No patch. Reclassify ED-candidate-F to P3. |
| F-WOUND-02 | P2 | No wound recovery rule between sessions for wounds > 4 | GAP-WOUND-01 logged |
| F-WOUND-03 | P2 | Pool floor 5 ambiguity: applies pre- or post-wound reduction? | GAP-WOUND-02 logged |

**Probability Table (Pool 13D baseline, TN7):**

| Wounds | Pool | P(Success vs Ob 3) | P(Success vs Ob 4) | Viable? |
|--------|------|-------------------|-------------------|---------|
| 0 | 13D | ~97% | ~91% | Yes |
| 4 | 9D | ~92% | ~81% | Yes |
| 8 | 5D | ~72% | ~54% | Degraded |
| 10 | 3D | ~47% | ~29% | Severely degraded |

---

### SIM-AMPL-01 — AMPLIFY Stalemate (Modes A + D)
**System:** Social Contest v2 | **Source:** social_contest_system_v2.md + params_contest.md

**Confirmed P1 stalemate condition:** AMPLIFY pool ≤ resistance × 2.5 AND non-primary genre → mathematically irresolvable. No CT movement, no Composure damage, no fallback.

| Finding | Severity | Description | Action |
|---------|----------|-------------|--------|
| F-AMPL-01 | P1 | Pool ≤ resistance × 2.5 + wrong genre = irresolvable stalemate in CLASH/AMPLIFY | [PROVISIONAL: AMPL-01] |
| F-AMPL-02 | P2 | No GM pre-combat stalemate detection test in params_contest.md | GAP-AMPL-01 logged |
| F-AMPL-03 | P2 | Stalemate paradox: high-Composure targets (most important chars) most prone to irresolvable debate | Design review note |

**[PROVISIONAL: AMPL-01]** Add to §4 AMPLIFY + §3 general stalemate rule:
> "If net successes = 0 for 3 consecutive exchanges in the same CLASH or AMPLIFY sequence, both sides exhaust their arguments. The exchange ends without Conviction Track movement. Each participant loses 1 Composure (narrative attrition). The Doubt Marker advances 1 toward the non-initiating side."

---

### SIM-CMD-01 — Command Cap Degenerate (Modes A + D)
**System:** Mass Combat | **Source:** mass_battle_v3.md + params_mass_combat.md

**Prior finding (SIM-MC-01) partially incorrect.** "Zero offensive benefit" overstates the problem. Size > Command is glass-cannon, not zero-benefit. Size-7/Command-2 wins against Size-3/Command-3 but takes disproportionate damage.

| Finding | Severity | Description | Action |
|---------|----------|-------------|--------|
| F-CMD-01 | REVISED | "Zero offensive benefit" incorrect — Power (damage/success) increases with Size. Glass cannon, not useless. | No new patch. Correct SIM-MC-01 finding. |
| F-CMD-02 | P1 | No mechanism to boost pool beyond Command cap — unit composition trivially solved (Command = Size optimal always) | [PROVISIONAL: CMD-01] |
| F-CMD-03 | P2 | Command-investment incentive is thematically coherent but creates tactical monoculture | Design note |

**[PROVISIONAL: CMD-01]** Add to mass_battle_v3.md §Unit Combat:
> "Overwhelming Size Advantage: when Size ≥ 2×Command, the unit may add +1D to its pool once per Battle Turn (Phase 4 only), representing mass weight of numbers overcoming command limitations. This bonus does not apply in Defensive formation or on defensive orders."

---

## BATCH B — New System Simulations

### SIM-CR-01 — Calamity Radiation Cross-Mode Integration (Modes A + G)
**System:** Calamity Radiation | **Source:** calamity_radiation.md + threadwork_v25.md + params_board_game.md

**RS band transition timeline (WC=0, worst-case seasonal decay):**

| Season | RS | Band | Distance-1 effects | Distance-2 effects |
|--------|----|----|-------------------|-------------------|
| 0 | 72 | Strained | Folklore only | None |
| 12 | 60 | Fragile | Thread +1 Ob; Shifting Objects | Folklore |
| 32 | 40 | Fractured | Gaps auto; all +1 Ob | Shifting Objects |
| 52 | 20 | Critical | Persistent presences; Gaps semi-regular | Consistent instability |

| Finding | Severity | Description | Action |
|---------|----------|-------------|--------|
| F-CR-01 | P1 | BG Radiation Table references "Thread orders" but BG uses Domain Action abstraction — no definition of which Domain Actions = Thread orders | [PROVISIONAL: CR-01] |
| F-CR-02 | P1 | Hybrid mode: Radiation-caused Thread failures — Domain Echo generation unspecified | [PROVISIONAL: CR-02] |
| F-CR-03 | P2 | Southernmost Surge timing if RS drops to 10 intra-Accounting | Conservative ruling: fires at Accounting AFTER RS ≤ 10 confirmed |
| F-CR-04 | P2 | Forgetting + Archival Thread ops at T15 — interaction unspecified | GAP-CR-02 logged |
| F-CR-05 | P3 | Calamity Drift and Radiation Matrix are consistent (CLEAN) | No action |
| GAP-CR-01 | BLOCKER | RS decay "−1/year" (PP-255) vs seasonal Accounting — conversion undefined | Blocks precise BG RS simulation |

**[PROVISIONAL: CR-01]** "Thread orders" in BG Radiation Table = Domain Actions bearing [THREAD] tag. Expedition and Mending-coordination are always [THREAD]-tagged. Govern, Assert, Reinforce etc. are NOT [THREAD]-tagged.

**[PROVISIONAL: CR-02]** Radiation-caused Thread failures in Hybrid Personal Phase do NOT generate Domain Echoes. Domain Echoes require deliberate faction-intent Thread operations.

---

### SIM-CLK-01 — Clock Registry Interaction Chains (Modes B + G)
**System:** All shared clocks | **Source:** clock_registry.md + params_board_game.md + victory_architecture_v1.md

**Interaction chains confirmed:**
- RS ↓ → CV erosion (Calamity Drift) → Conviction Yield lower → TC slower (intended)
- TC ↑ → Church Seizure stronger → Rival TCV lost → Mandate drop → less Suppress → TC accelerates (self-reinforcing, known)
- WC ↑ → RS decay halved → Radiation pressure delayed (clear cooperation incentive)

| Finding | Severity | Description | Action |
|---------|----------|-------------|--------|
| F-CLK-01 | P2 | RS decline CV erosion at Distance-2 (T5 Feldmark) reduces Church Seizure Ob on Crown territory — may be unintended | GAP-CLK-01: confirm intentionality |
| F-CLK-02 | P2 | AER (clock_registry) vs AEA (victory_architecture) naming inconsistency | GAP-CLK-02: reconcile naming |
| F-CLK-03 | P1 | PI thresholds undefined (ED-361 pending) — blocks SIM-PI-CASCADE and affects 3 victory conditions | [PROVISIONAL: CLK-01] |
| F-CLK-04 | P2 | WC advancement procedure references outdated stage4_southernmost.md | GAP-CLK-03: Expedition rules need design-layer doc |

**[PROVISIONAL: CLK-01 — PI thresholds, pending ED-361]:**
- PI 0–2: Parliamentary debate only
- PI 3: Faction Mandate cap −1
- PI 5: Parliamentary Session mandatory at Accounting
- PI 7: Löwenritter Coup Counter +1 auto; RM Founding eligibility
- PI 10: Structural collapse — all factions Stability −1 at Accounting until PI < 7

---

### SIM-VIC-01 — Victory Architecture Endgame Race (Modes C + D)
**System:** Victory Architecture | **Source:** victory_architecture_v1.md

**Season 10 race projection (4-player standard):**

| Faction | Season 10 State | Victory Horizon | Notes |
|---------|----------------|-----------------|-------|
| Crown | TCV ~14, rivals Mandate 4–5 | Season 18–22 | Suppression bottleneck |
| Church | TCV ~5, TC ~55 | Season 14–17 | CV management bottleneck |
| Hafenmark | TCV ~12, PI ~3 | Season 10–14 | Fastest solo path |
| Varfell A | TCV ~7, VTM ~1 | Season 14–16 | Intel reveal bottleneck |
| Crown+Hafenmark co | — | Season 7–10 | Passive co-victory risk (ED-343 still open) |

| Finding | Severity | Description | Action |
|---------|----------|-------------|--------|
| F-VIC-01 | P2 | Church Conviction Yield: automatic Prominence in self-controlled territories not specified | [PROVISIONAL: VIC-01] |
| F-VIC-02 | P1 | Crown victory "Suppress all rivals" produces 20+ season timeline — intended? (ED-candidate-A) | EDITORIAL: confirm intended |
| F-VIC-03 | P2 | Crown+Hafenmark passive co-victory reachable Season 7–10 (ED-343, still open) | Cross-reference prior finding |
| F-VIC-04 | P2 | WR Expedition failure consequence unspecified | GAP-VIC-01 logged |
| F-VIC-05 | P1 | Church TC-75 CV management creates 2–3 season vulnerability window (CLEAN — intended design pressure) | No action |
| F-VIC-06 | P1 | Hafenmark has shortest passive solo victory path — prior PP-203 balance fix needs verification | GAP-VIC-02: confirm PP-203 scope |

**[PROVISIONAL: VIC-01]** Church is automatically Prominent in all self-controlled territories. Mandate comparison applies only to territories controlled by rival factions.

---

## BATCH C — Victory Edge Cases and RM Calibration

### SIM-VIC-02 — Co-Victory Pairings Stress Test (Modes D + L)

**Clean results:**
- Partition vs Crown+Hafenmark: mutually exclusive (TC < 50 vs TC ≥ 50) — CLEAN
- Crown+Varfell RS ≥ 50: creates cooperation incentive for Expedition — CLEAN
- Treaty lapse/Partition interaction: Treaty lapse ≠ military conflict — CLEAN

| Finding | Severity | Description | Action |
|---------|----------|-------------|--------|
| F-CO-01 | P2 | Löwenritter co-victory timing: coup may fire at PI < 4, delaying eligibility by 1 season | Minor tension — no patch |
| F-CO-02 | P1 | Varfell+RM co-victory unachievable in race conditions (VTM 4+ + WR 2+ + 4× CV ≤ 1 by Season 16–20 = too slow) | EDITORIAL: ED-candidate-new-1 — confirm aspirational design |
| F-CO-03 | P3 | Co-victory tracking requires 8–10 simultaneous variables for first-game players | GM reference card recommended |

---

### SIM-VIC-03 — RM Cultural Uprising Calibration (Modes A + C)

**Phase 2 success rate (Pontifex TS ~50):**

| Conditions | Ob | P(Success) |
|-----------|----|------------|
| Base (TC 28) | 3 | ~37% |
| T9 CV ≤ 1 | 2 | ~54% |
| T9 CV ≤ 1 + WC ≥ 2 | 2, +1D | ~66% |
| TC ≥ 50 + T9 CV ≤ 1 | 3 | ~37% |

| Finding | Severity | Description | Action |
|---------|----------|-------------|--------|
| F-VIC-RM-01 | P1 | Phase 1 threshold conflict: §3.5 text says ≥ 8 territories; PP-478 override says ≥ 5 territories | [PROVISIONAL: VIC-RM-01] |
| F-VIC-RM-02 | P2 | Pontifex Thread pool value not specified — blocks precise Phase 2 P(success) | GAP-VIC-RM-01 logged |
| F-VIC-RM-03 | P2 | RS ≥ 25 prerequisite correctly calibrated (CLEAN) | No action |
| F-VIC-RM-04 | P3 | "Arc" in "attempt used up for this arc" should be defined as "campaign" | Minor clarification |

**[PROVISIONAL: VIC-RM-01]** PP-478 supersedes §3.5 Phase 1 threshold. Phase 1 = ≥ 5 territories CV ≤ 1 in Hybrid mode (post-Founding). §3.5 ≥ 8 text is pre-PP-478 BG-only (now struck since RM is BG-unavailable).

---

## CONSOLIDATED FINDING REGISTER

### P1 Findings (require action)

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| F-AMPL-01 | SIM-AMPL-01 | AMPLIFY irresolvable stalemate: pool ≤ resistance × 2.5 + wrong genre | PROVISIONAL: AMPL-01 |
| F-CMD-02 | SIM-CMD-01 | No mechanism to boost Size > Command pool — unit composition trivially solved | PROVISIONAL: CMD-01 |
| F-CR-01 | SIM-CR-01 | BG "Thread orders" undefined in Radiation Table | PROVISIONAL: CR-01 |
| F-CR-02 | SIM-CR-01 | Hybrid Radiation failure Domain Echo generation undefined | PROVISIONAL: CR-02 |
| F-CLK-03 | SIM-CLK-01 | PI thresholds entirely undefined — blocks 3 victory conditions | PROVISIONAL: CLK-01 |
| F-VIC-02 | SIM-VIC-01 | Crown suppress-all 20+ season timeline — intended? | EDITORIAL |
| F-VIC-06 | SIM-VIC-01 | Hafenmark passive dominance — PP-203 verification needed | GAP-VIC-02 |
| F-CO-02 | SIM-VIC-02 | Varfell+RM co-victory unachievable in race conditions | EDITORIAL |
| F-VIC-RM-01 | SIM-VIC-03 | RM Phase 1 threshold conflict (8 vs 5 territories, §3.5 vs PP-478) | PROVISIONAL: VIC-RM-01 |

### P2 Findings

| ID | Source | Description |
|----|--------|-------------|
| F-WOUND-02 | SIM-WOUND-01 | No wound recovery rule between sessions for wounds > 4 |
| F-WOUND-03 | SIM-WOUND-01 | Pool floor 5: pre- or post-wound reduction ambiguity |
| F-AMPL-02 | SIM-AMPL-01 | No GM stalemate detection test in params_contest.md |
| F-AMPL-03 | SIM-AMPL-01 | High-Composure targets most prone to irresolvable debate (design paradox) |
| F-CMD-03 | SIM-CMD-01 | Command = Size always optimal creates tactical monoculture |
| F-CR-03 | SIM-CR-01 | Surge timing ambiguity if RS hits 10 intra-Accounting |
| F-CR-04 | SIM-CR-01 | Forgetting + Archival Thread ops at T15 undefined |
| F-CLK-01 | SIM-CLK-01 | RS decline → CV erosion → Church Seizure easier on Crown territories (intentional?) |
| F-CLK-02 | SIM-CLK-01 | AER vs AEA naming inconsistency |
| F-CLK-04 | SIM-CLK-01 | WC advancement procedure references outdated stage4 |
| F-VIC-01 | SIM-VIC-01 | Church Prominence in self-controlled territories undefined |
| F-VIC-03 | SIM-VIC-01 | Crown+Hafenmark passive co-victory Season 7–10 (ED-343 open) |
| F-VIC-04 | SIM-VIC-01 | WR Expedition failure consequence unspecified |
| F-CO-01 | SIM-VIC-02 | Löwenritter co-victory timing friction |
| F-VIC-RM-02 | SIM-VIC-03 | Pontifex Thread pool unspecified |

### P3 Findings (design notes)

| ID | Source | Description |
|----|--------|-------------|
| F-WOUND-01 | SIM-WOUND-01 | ED-candidate-F imprecise — no Ob penalty needed |
| F-CR-05 | SIM-CR-01 | Calamity Drift and Radiation Matrix consistent (CLEAN) |
| F-CO-03 | SIM-VIC-02 | Co-victory tracking cognitive load for first-game players |
| F-VIC-RM-04 | SIM-VIC-03 | "Arc" definition in Phase 2 reuse rule |

### Clean Scenarios

- SIM-WOUND-01: Wound pool reduction calibration is correct for in-session ranges
- SIM-CR-01: Calamity Drift / Radiation Matrix consistency
- SIM-CLK-01: RS/TC/WC cooperation loop coherent and intended
- SIM-VIC-01: Church TC-75 CV vulnerability window is intended design pressure
- SIM-VIC-02: Partition vs Crown+Hafenmark structural exclusivity
- SIM-VIC-02: Crown+Varfell co-victory RS incentive
- SIM-VIC-02: Treaty lapse / Partition independence
- SIM-VIC-03: RS ≥ 25 Uprising prerequisite correctly calibrated

### Gaps Logged

| ID | Description |
|----|-------------|
| GAP-CR-01 | RS decay "−1/year" (PP-255) vs seasonal Accounting — conversion unspecified |
| GAP-CR-02 | Forgetting + Archival Thread ops at T15 — interaction unspecified |
| GAP-WOUND-01 | Wound recovery between sessions for wounds > 4 — no rule |
| GAP-WOUND-02 | Pool floor 5 — pre- or post-wound reduction |
| GAP-AMPL-01 | No GM stalemate detection table in params |
| GAP-CLK-01 | RS CV erosion on Crown territories — intentionality unconfirmed |
| GAP-CLK-02 | AER vs AEA naming inconsistency |
| GAP-CLK-03 | WC advancement procedure references outdated stage4 |
| GAP-VIC-01 | WR Expedition failure consequence unspecified |
| GAP-VIC-02 | PP-203 Hafenmark balance scope unverified |
| GAP-VIC-RM-01 | Pontifex Thread pool value unspecified |

---

## Provisional Patches Applied This Session

| ID | Target | Text |
|----|--------|------|
| AMPL-01 | social_contest_system_v2.md §4 + §3 | 3-exchange zero-net stalemate break: CT no movement; each side −1 Composure; Doubt Marker +1 toward non-initiating side |
| CMD-01 | mass_battle_v3.md §Unit Combat | Size ≥ 2×Command: +1D to pool once per Battle Turn Phase 4, not on defensive orders |
| CR-01 | calamity_radiation.md §BG Implementation | "Thread orders" = Domain Actions with [THREAD] tag |
| CR-02 | calamity_radiation.md §Hybrid Mode | Radiation-caused failures do not generate Domain Echoes |
| CLK-01 | params_board_game.md §PI | Provisional PI thresholds pending ED-361 |
| VIC-01 | victory_architecture_v1.md §3.2 | Church auto-Prominent in self-controlled territories |
| VIC-RM-01 | victory_architecture_v1.md §3.5 | PP-478 supersedes ≥8 territories; Phase 1 = ≥5 territories CV ≤ 1 |

