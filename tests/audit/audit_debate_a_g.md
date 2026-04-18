# AUDIT-D-01: Debate System Mechanic Audit — Modes A–G
## Date: 2026-04-02
## Source: designs/debate/debate_system_redesign_v1.md Part 6 (v1.2)
## Params: references/params_debate.md (v0.14+design-ST2), references/params_core.md (v0.14)

---

## 7-Dimension Tag
```
Test ID: AUDIT-D-01
Mechanics: All debate mechanics (§6.0–6.10)
Mode: TTRPG primary; cross-mode in Mode G
Tracks: Composure, Concentration, Conviction Track, Doubt Marker
Factions: All (genre weight system covers all)
NPCs: Generic
Archetypes: All debate-capable
```

---

## MODE A — Formula Validation

| ID | Formula | Variables | Min | Max | Issues | Status |
|----|---------|-----------|-----|-----|--------|--------|
| FA-01 | Presence modifier = floor((Presence−3)/2) | Presence 1–7 | −1 (Pres 1) | +2 (Pres 6–7) | **FAIL:** Formula yields −1 at Pres 1–2. Table states Pres 1–3 = +0. Missing max(0,…). | **P2 — PATCH** |
| FA-02 | Concentration depletion: −1/exchange, −1/loss | Concentration ≥ 0 | Can reach −1 in one step (Conc=1, loss: −2) | — | **FAIL:** No floor at 0. Spent fires at 0 but a single-exchange double depletion can skip Spent and go negative. Missing floor(Concentration, 0) after depletion. | **P2 — PATCH** |
| FA-03 | Strain_CLASH = margin+1+Pres_mod−Focus_def | margin ≥ 1; Pres_mod 0–2; Focus_def 0–3 | 0 (margin 1, Pres_mod 0, Focus_def 2) | ~25 | **FAIL:** No minimum strain stated. margin=1, Pres_mod=0, Focus_def=2 → Strain=0. Winning an exchange should deal minimum 1 strain. | **P2 — PATCH** |
| FA-04 | Strain_COMPETITION = (margin−1, min 1)+1+Pres_mod−Focus_def | same | 0 | ~24 | **FAIL:** Same minimum-zero issue as FA-03. | **P2 — PATCH** |
| FA-05 | effective_margin_CLASH = floor(margin × genre_weight × orientation_weight) | margin ≥ 1; genre_weight 0.5–1.5; orient 1.0 | 0 (margin 1, weight 0.5 → floor 0.5 = 0) | unbounded | **PASS** — floor correctly produces 0 for low inputs. Degenerate case (effective_margin=0) is valid. |  |
| FA-06 | Track movement = effective_margin − resistance, min 0 | effective_margin ≥ 0; resistance ≥ 0 | 0 | unbounded high (no per-exchange cap) | **PASS** — no cap needed; win condition (≥7 or ≤3) terminates. Min 0 implied by "if effective_margin > resistance" gate. |  |
| FA-07 | effective_margin_DIVERGE = floor((successes/2) × genre_weight × 1.0) | successes may be negative (fumbles > hits) | Negative input → negative margin (treated as 0 by gate) | unbounded | **WARN:** Negative net successes produce negative effective_margin. Handled correctly by gate (not > resistance → 0 movement) but not explicitly stated. P3 — add note. |  |
| FA-08 | Composure = Poise + Bonds + 3 | Poise 1–7, Bonds 1–7 | 5 | 17 | **PASS.** |  |
| FA-09 | Concentration = Focus + Presence | Focus 1–7 (assumed), Presence 1–7 | 2 | 14 | **PASS** — but see FA-02 re: depletion floor. |  |
| FA-10 | Focus defence = floor(Focus/2) | Focus 1–7 | 0 (Focus 1) | 3 (Focus 6–7) | **PASS.** |  |
| FA-11 | Read pool = Attunement | Attunement 1–7 | 1 | 7 | **PASS** — pool minimum of 1D per params_core covers the Attunement=0 edge (if achievable). |  |
| FA-12 | Argue pool = (Presence×2) + History bonus | Presence 1–7, History 0–6, Memory +2D | 2 | 22 | **PASS** — no negative pool possible. |  |

**P2 patches required from Mode A: FA-01, FA-02, FA-03, FA-04.**
**P3 clarification: FA-07.**

---

## MODE B — Number System Coherence

| System | Range | Scale Basis | Analogous System | Inconsistency |
|--------|-------|-------------|-----------------|--------------|
| Argue pool | 2–22D | Presence×2 + History 0–6 + Memory ±2 | Combat pool: Agility×2 + History + 3 | MISMATCH: Combat has flat +3; debate has no flat bonus. Low-History debaters have proportionally smaller pools than low-History fighters. |
| Read pool | 1–7D | Attunement score only | No combat equivalent | Disjoint from Argue pool — different attribute, much smaller. By design. |
| Composure | 5–17 | Poise + Bonds + 3 | Combat Stamina: explicit track | MISMATCH: Combat Stamina has a stated per-round depletion rate. Composure has no per-exchange baseline depletion — only strain from exchange results. Very different resource dynamics. |
| Concentration | 2–14 | Focus + Presence | Combat Stamina | MISMATCH: Concentration depletes every exchange AND on loss. Combat Stamina depletes once per round (−1). Concentration depletes 1–2× per exchange. Rates inconsistent. |
| Conviction Track | 0–10 | Fixed | Combat Health 0–10 | Win zone asymmetry: 4 positions win for A (7,8,9,10), 4 for B (0,1,2,3), 3 compromise (4,5,6). Not fully symmetric around 5. |
| Resistance | 0–~5 | Faction Stability avg −1 | No direct combat parallel | No upper cap defined. Resistance of 5 would make track movement near-impossible (margin ≥ 6 required at primary genre). |
| Strain per exchange | 0–25+ | Formula (margin-based) | Combat damage per round | MISMATCH: Combat damage capped by weapon type and Armour DR. Debate strain is uncapped. A single exchange can produce more strain than total Composure. |
| Genre weight | 0.5/1.0/1.5 | Fixed multiplier | No combat parallel | CONSISTENT internally. Ternary values never 0 or above 1.5 — clean. |
| Effective_margin | 0–33+ | floor(margin × weight) | No equivalent | Unbounded ceiling vs bounded Track (0–10). Track absorbs excess naturally via win condition. Functional but mismatched scales. |
| Presence modifier | 0–2 (effective) | floor((Pres−3)/2), max(0) | Combat: Strength modifier for damage | CONSISTENT with combat approach. Combat uses similar breakpoint-modifier pattern. |

**Key incoherence findings:**
- **B-01 (P2):** Strain uncapped per exchange vs Composure bounded 5–17. One catastrophic CLASH can produce 25 strain against Composure 5. This is a valid outcome (immediate Rattled) but creates a cliff that doesn't exist in combat (where DR caps per-hit damage). No patch needed — acknowledged as design asymmetry. Monitor in playtesting.
- **B-02 (P2):** Concentration depletion rate (1–2/exchange) vs Composure depletion rate (0–25+/exchange). These resources don't deplete at comparable rates. Composure only depletes in CLASH/COMPETITION; Concentration depletes every exchange. Result: Concentration is the binding constraint in Divergence-heavy debates; Composure is the constraint in CLASH-heavy debates. Dual resource with different triggers is valid, but the design doesn't call this out explicitly.
- **B-03 (P3):** Argue pool (2–22D) vs Read pool (1–7D). The two pools within a single system vary by a factor of ~3. A character with Presence 7 arguing in their best genre is evaluated against Attunement for reading. If Attunement is low (1–2), this character will consistently misread despite being an elite orator — the Read/Argue attribute split creates a consistent mismatch for specialists.

---

## MODE C — Interaction Chain Analysis

| Mechanic | Upstream Inputs | Downstream Outputs | Chain Length | Flags |
|----------|----------------|-------------------|--------------|-------|
| Read roll | Attunement | Genre/Orientation choice | 2 | None |
| Choose | Read result, Genre weights (setup) | Interaction type | 2 | None |
| Argue roll | Presence×2 + History + Memory bonus | Net successes → margin | 3 | Memory bonus binary — no partial credit |
| effective_margin_CLASH | margin, genre_weight, orient_weight | Track movement | 4 | Floor at each step creates dead zones |
| Strain | margin, Pres_mod, Focus_def | Composure depletion → Rattled | 4 | No minimum strain (FA-03) |
| Concentration | Exchange result (win/lose), Focus score | Spent state → −2D Argue | 3 | No depletion floor (FA-02) |
| Rattled | Composure ≥ threshold | −2D Argue, Focus_def lost | 2 | Stacks with Spent (−4D total) — no stated cap |
| Spent | Concentration = 0 | −2D Argue, opp +1D | 2 | Interaction with Regroup provisional (PP-098) |
| Doubt Marker | Obscuring WIN | −2 effective_margin on next opp win | 2 | Single marker limit — replacement rule confirmed (PP-099) |
| Regroup | Player declares | Concentration restores, TC +1 opp, Spent consumed | 3 | PP-098 provisional |
| Corroboration (§3.5) | Bonds, Knot requirement | +1D/+2D to Argue | 2 | **NOT INTEGRATED into §6.4 exchange steps.** §3.5 exists in Part 3 but §6.4 has no corroboration step. Dead reference in operative system. |
| Thread consequence (§3.8) | Winning genre + orientation | RS/TC/Domain Echo effects | 1 | Downstream only — clean. §6.5 references §3.8 |
| Audience resistance | Faction Stability avg −1 | effective_margin gate | 1 | Resistance formula not in §6.4 — only in §6.1. Forward reference only. |

**Circular dependencies:** None found.

**Dead-end mechanics:**
- **C-01 (P1):** Corroboration (§3.5) is referenced in Part 3 and §6.8 as "untested" but has **no integration step in §6.4**. §6.4 defines the exchange as Read→Choose→Argue→Resolve. Corroboration should be a declared action between Step 2 and Step 3 (Choose and Argue) but the operative system has no procedure for it. This is a dead reference — the mechanic exists in Parts 1–4 but was not ported to Part 6. **P1 gap.**

**Amplification loops:**
- **C-02 (P2):** Rattled (−2D Argue) + Spent (−2D Argue, opp +1D) stack to −4D Argue / opp +1D. No stated maximum penalty cap. A character who hits both thresholds is functionally incapacitated (2D pool at Presence 1, Attunement roll impossible at 0D → uses pool minimum 1D from params_core). The amplification terminates at pool minimum — not an infinite loop. Manageable.

**Unconnected systems:**
- **C-03 (P2):** Beliefs (NPC profiles) have no integration with Debate outcomes. An orator arguing in alignment with their Belief should (per core principles) gain a mechanical benefit. Currently Beliefs are narrative only in Debate context.
- **C-04 (P2):** Inspiration/Spirit economy has no presence in Debate. Characters cannot spend Inspiration/Spirit to add automatic successes to Argue rolls (Momentum from params_core says "non-Thread rolls only" — Debate is non-Thread, so Momentum should be spendable). GAP: Momentum spending not explicitly permitted or prohibited in Debate context.

---

## MODE D — Gap Detection

New gaps found (GAP-DS-01 through GAP-DS-08 already in §6.9):

| ID | Type | Description | Location | Severity |
|----|------|-------------|----------|---------|
| GAP-DS-09 | Missing rule | Strain minimum — CLASH/COMPETITION can produce 0 strain at high Focus defence | §6.4 CLASH/COMPETITION | P2 |
| GAP-DS-10 | Missing rule | Concentration depletion floor — can go below 0 in one exchange | §6.4 Step 6 | P2 |
| GAP-DS-11 | Missing rule | Presence modifier formula — gives −1 at Pres 1–2 vs table stating +0 | §6.2 | P2 |
| GAP-DS-12 | Missing rule | Corroboration (§3.5) not integrated into §6.4 exchange steps | §6.4 | P1 |
| GAP-DS-13 | Missing rule | Debate initiation gate — "when to roll" condition not defined (Principle 1) | §6.0 | P2 |
| GAP-DS-14 | Missing rule | Rattled + Spent simultaneous — −4D total; no explicit stacking rule or cap | §6.4 Step 6 | P2 |
| GAP-DS-15 | Stale text | §6.10 still says "SIM-DEBT-01 — re-simulation needed" — now resolved | §6.10 | P3 (cleanup) |
| GAP-DS-16 | Missing rule | Post-debate strain recovery — when does strain clear? (scene end / session / never?) | §6.5 | P2 |
| GAP-DS-17 | Missing rule | Momentum spending in Debate — permitted or prohibited? params_core allows non-Thread | §6.4 | P2 |
| GAP-DS-18 | Missing rule | Corroboration in asymmetric proceedings — can accused have corroborators in Tribunal? | §6.7 | P2 |
| GAP-DS-19 | Missing rule | Belief alignment bonus — arguing in Belief alignment has no mechanical effect in Debate | §6.4 | P2 |
| GAP-DS-20 | Missing rule | DIVERGE effective_margin with negative net successes — behavior not explicitly stated | §6.4 DIVERGENCE | P3 |

---

## MODE E — Core Principles Compliance

| # | Principle | Status | Notes |
|---|-----------|--------|-------|
| 1 | Roll only when meaningful | ALTERED | Read roll mandatory every exchange even in Tribunal (where institutional outcome is predetermined). No "when to roll" gate stated (GAP-DS-13). |
| 2 | Let It Ride | PRESENT (implied) | Each exchange is a new roll — no re-roll of same attempt. Not explicitly stated. |
| 3 | Fail Forward | PRESENT | Compromise (TC 4–6) provides narrative output even in failure. Total loss (≤3) has consequences. |
| 4 | Histories, not Skills | PRESENT | History bonus is lived experience. Theology, Court Law, Military Command — all appropriate history categories. |
| 5 | Pool = Attribute + History bonus | ALTERED | Pool = (Presence × 2) + History. Multiplier departs from additive formula. Justified (social combat needs wider variance range) but departs from stated principle. |
| 6 | Wound system | N/A | Debate uses Composure/Strain, not wounds. Correct separation. |
| 7 | Inspiration/Spirit economy | ABSENT | No Belief invocations, no Inspiration/Spirit integration. GAP-DS-17, GAP-DS-19. |
| 8 | Beliefs as moral character | ABSENT from mechanics | NPC Beliefs exist in stage13 but have no mechanical hook in §6.4. GAP-DS-19. |
| 9 | Social combat via Rhetoric | PRESENT | Debate is the primary Rhetoric procedure. Genre system is sophisticated. Negotiation as separate procedure not yet defined. |
| 10 | Reach/Speed priority | N/A | Not applicable. |
| 11 | Phase-based | PRESENT | Exchange structure (7 steps) is phase-based. |
| 12 | Beginner's Luck | PRESENT (implied) | No History = (Presence × 2) only. Accessible to untrained characters. Not explicitly labelled. |
| 13 | Circles and Resources | PARTIAL | Corroboration uses Bonds (if Corroboration is integrated — GAP-DS-12). Otherwise absent. |

**Key compliance failures:**
- **E-01 (P2):** Principle 7 (Inspiration/Spirit) absent from Debate — no Momentum/Belief integration.
- **E-02 (P2):** Principle 8 (Beliefs) not mechanically expressed in Debate exchanges.
- **E-03 (P2):** Principle 5 (pool formula) altered without explicit design note in operative section.

---

## MODE F — Playtest Burden Analysis

*(References SIM-D-02 Mode J — expanding with Mode F metric format)*

| Mechanic | Time(s) novice | Lookups | Tracking | Decisions | Load | Flag |
|----------|---------------|---------|----------|-----------|------|------|
| Read roll (per orator) | 30s | 1 (result table) | 0 | 1 (interpret) | Low | None |
| Choose genre+orient | 20s | 1 (weight table) | 1 (hold Read) | 2 | Low | None |
| Argue roll (×2, 26D total) | 90s | 0 | 1 | 1 (Memory check) | **High** | **P1: >2 lookups if weight table consulted again; 90s alone** |
| Resolve interaction type | 15s | 1 (type table) | 2 | 0 | Medium | None |
| effective_margin calc | 25s | 0 | 2 | 0 | **High** | **P2: floor × 3 operands** |
| Strain calc | 15s | 1 (Pres mod table) | 2 | 0 | Medium | None |
| Concentration update | 10s | 0 | 2 | 0 | Low | None |
| **Full exchange** | **~205s (3.4 min)** | **5 total** | **6 peak** | **7** | **7/10 — PROBLEM** | **P1: >2 parallel lookups per exchange** |

**P1 flags (Mode F):**
- **F-01:** 5 mandatory lookups per exchange exceeds the ">2 parallel lookups → P1 if every round" threshold.
- **F-02:** Novice per-exchange time ~540s (9 min) at table (accounting for dice retrieval, pool counting, discussion). Exceeds 5-min P1 threshold.

**Mitigations (design-level):**
1. GM reference card covering §6.1 setup + §6.4 flowchart + genre weight table. Eliminates 3 of 5 lookups for experienced players.
2. Optional: pre-print ledger sheet with TC track + Composure/Concentration counters per orator.
3. Optional: Simultaneous argue rolls for DIVERGENCE (no information dependency when genres confirmed different).

---

## MODE G — Cross-Mode Consistency

| Mechanic | Modes Present | Transition Defined? | State Preserved? | Flag |
|----------|--------------|--------------------|--------------------|------|
| Full debate exchange | TTRPG only | N/A | N/A | None — correctly TTRPG-only per R-65 |
| Parliamentary Vote | BG (implied) | **No** | **No** | **P1: BG Parliamentary Vote procedure undefined (GAP-DS-05)** |
| Faction resonance / genre weights | TTRPG | N/A for BG | N/A | Faction ethical modes used in TTRPG only |
| Thread consequences from debate (§3.8) | TTRPG + Hybrid | Partially (§6.10) | Partially | P2: Hybrid debate procedure not documented |
| Conviction Track | TTRPG only | N/A | N/A | Not equivalent to any BG stat |
| Composure / Concentration | TTRPG only | N/A | N/A | No BG equivalent |
| Domain Echo from debate win | TTRPG → BG | Partially | Faction stat change defined | TC/Mandate changes documented in stakes; cross-mode propagation not in state_transfer_spec |

**Mode G findings:**
- **G-01 (P1):** BG Parliamentary Vote has no procedure. Referenced in §6.8 (GAP-DS-05). Blocks BG political play.
- **G-02 (P2):** Hybrid debate — no documented variant. A Hybrid session mid-debate has no rules for what the BG-layer parallel is.
- **G-03 (P1):** Domain Echo from debate win produces faction stat changes (TC, Mandate, Reach). These cross the TTRPG→BG boundary. No entry in state_transfer_spec for debate-originated Domain Echo. Propagation path unverified.
- **G-04 (P2):** Thread consequences from debate (§3.8) specify RS changes and Domain Echo. In Hybrid mode, RS changes affect both TTRPG and BG layers. No documented procedure for how debate RS change propagates to BG Thread Order queue.

---

## AUDIT FINDINGS SUMMARY

**P1 findings (blocks play):**

| ID | Mode | Description | Disposition |
|----|------|-------------|-------------|
| FA-01 | A | Presence modifier formula gives −1 at Pres 1–2; table says +0. Missing max(0,…). | PP-101 — patch §6.2 |
| FA-02 | A | Concentration depletion has no floor at 0; can go negative in one exchange. | PP-102 — patch §6.4 Step 6 |
| FA-03 | A | Strain_CLASH minimum = 0; no stated minimum. | PP-103 — patch §6.4 CLASH |
| FA-04 | A | Strain_COMPETITION minimum = 0; no stated minimum. | PP-103 — patch §6.4 COMPETITION |
| GAP-DS-12 | C/D | Corroboration (§3.5) not integrated in §6.4. Dead reference. | PP-104 — stub integration point in §6.4 |
| F-01 | F | 5 mandatory lookups per exchange (>2 threshold). | Tooling: GM reference card |
| F-02 | F | Novice time 9 min/exchange (>5 min threshold). | Tooling: GM reference card |
| G-01 | G | BG Parliamentary Vote undefined. | Editorial: ED-053 |
| G-03 | G | Debate Domain Echo not in state_transfer_spec. | PP-105 — add to state_transfer_spec |

**P2 findings:**

| ID | Mode | Description | Disposition |
|----|------|-------------|-------------|
| B-01 | B | Strain uncapped vs Composure bounded. | Design acknowledgment note |
| B-03 | B | Read/Argue attribute split disadvantages specialists. | Design observation |
| C-02 | C | Rattled + Spent stack to −4D; no cap. | PP-106 — note in §6.4 |
| C-03 | C | Beliefs not integrated mechanically. | GAP-DS-19, ED-054 |
| C-04 | C | Momentum spending not permitted/prohibited. | GAP-DS-17 — design decision needed |
| E-01 | E | Principle 7 (Inspiration/Spirit) absent. | GAP-DS-17, GAP-DS-19 |
| GAP-DS-13 | D | No debate initiation gate ("when to roll"). | PP-107 — add gate to §6.0 |
| GAP-DS-14 | D | Rattled + Spent simultaneous — no stacking rule. | PP-106 covers this |
| GAP-DS-16 | D | Post-debate strain recovery timing undefined. | PP-108 — add to §6.5 |
| GAP-DS-18 | D | Corroboration in asymmetric proceedings undefined. | ED-055 |
| G-02 | G | Hybrid debate variant not documented. | ED-056 |
| G-04 | G | Debate RS changes in Hybrid — BG propagation undefined. | ED-057 |

**P3 findings:**

| ID | Mode | Description |
|----|------|-------------|
| FA-07 | A | Negative net successes in DIVERGE — handled correctly but unstated. Add note. |
| B-02 | B | Concentration vs Composure depletion rate mismatch — design acknowledgment. |
| GAP-DS-15 | D | §6.10 stale SIM-DEBT-01 note — cleanup. |
| GAP-DS-20 | D | DIVERGE negative successes — add explicit note matching FA-07. |

---
*End AUDIT-D-01. Patches PP-101 through PP-108 to be applied in-place. Editorials ED-053 through ED-057 to be logged.*
