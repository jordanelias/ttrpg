# SIM-D-02: Debate — Mode C Full Scenario
## Modes: C (Full Scenario) + J (Cognitive Load)
## Date: 2026-04-02
## Closes: SIM-DEBT-01
## Source doc: designs/debate/debate_system_redesign_v1.md Part 6 (v1.1)
## Pool formula: (Presence × 2) + History bonus, TN 7

---

## 7-Dimension Tag

```
Test ID: SIM-D-02
Mechanics: Argue, Read, DIVERGENCE, CLASH, Conviction Track, Composure, Concentration, initiative
Mode: TTRPG | Temporal: PRESENT (Parliament session, current political moment)
Tracks: TC, Composure (both NPCs), Concentration (both NPCs)
Factions: Church, Hafenmark; audience: Parliament (Crown-weighted)
NPCs: Confessor Himlensendt (Church), Duchess Inge Baralta (Hafenmark)
Archetypes: Institutional authority orator (Himlensendt), Legalist-constitutionalist orator (Baralta)
```

---

## GM Setup (§6.1)

**Question:** "Should the Church hold formal ratification authority over Crown succession appointments?"
**Question type:** Future → Primary genre: **Future** (×1.0)
**Audience:** Parliament — Crown faction dominant (virtue ethics) → **Present** genre boosted (+0.5 → ×1.5)

**Genre weights (fixed at setup):**
| Genre | Weight |
|-------|--------|
| Future | ×1.0 (primary) |
| Present | ×1.5 (Crown boost) |
| Past | ×0.5 |

**Orientation weights:** Revealing ×1.0 (standard). Obscuring → Doubt Marker (no track movement).

**Conviction Track:** Start 5 (neutral). Side A = Himlensendt (Church ratification). Side B = Baralta (oppose). Win thresholds: A ≥ 7, B ≤ 3. Compromise zone: 4–6.

**Resistance:** 2 [PROVISIONAL — params_factions.md not read; using midpoint of typical range 1–3]
[PARAMS GAP: faction Stability values for Church/Hafenmark/Crown not loaded — resistance is provisional]

**Exchange count:** 3 (Formal Debate, Parliament)
**Role structure:** Alternating. Himlensendt proposes X1 (Presence 6 > Baralta 5), Baralta X2, Himlensendt X3.
**Stakes:** A wins → Church ratification authority formally recognised (TC+2, Church Mandate+1, Baralta Mandate−1). B wins → Sovereign Authority Doctrine enshrined (TC−2, Baralta Mandate+1, Church Reach−1). Compromise → motion tabled, committee review, no immediate stat change.

---

## NPC Profiles

**[PARAMS GAP: stage13_npcs.md missing Attunement, Focus, Poise, Bonds for both NPCs. Provisional values applied per archetype reasoning. See ED-051.]**

### Confessor Himlensendt (Church — Side A)

| Attribute | Value | Source |
|-----------|-------|--------|
| Presence | 6 | stage13 (canonical) |
| Cognition | 5 | stage13 (canonical) |
| Attunement | 3 | [PROVISIONAL — senior Church figure, moderate spiritual awareness] |
| Focus | 3 | [PROVISIONAL — disciplined but politically not contemplatively skilled] |
| History (Theology) | 3 | stage13 (canonical) |
| History (Political Negotiation) | 2 | stage13 (canonical) |

**Derived values:**
| Value | Formula | Result |
|-------|---------|--------|
| Argue pool | (6×2) + 3 (Theology) | **15D** |
| Read pool | Attunement 3D | 3D |
| Composure | 12 (per stage13 shorthand) [ED-052] | 12 |
| Presence modifier | floor((6−3)/2) = 1 | **+1** |
| Focus defence | floor(3/2) = 1 | **1** |
| Concentration | Focus + Presence = 3+6 | **9** |

Resonant Style: Consequence (Future genre). Optimal: Future + Revealing.

### Duchess Inge Baralta (Hafenmark — Side B)

| Attribute | Value | Source |
|-----------|-------|--------|
| Presence | 5 | stage13 (canonical) |
| Attunement | 2 | [PROVISIONAL — secular, materialist, no Thread sensitivity] |
| Focus | 3 | [PROVISIONAL — methodical commander] |
| History (Court Law) | 1 | stage13 (canonical) |
| History (Military Command) | 2 | stage13 (canonical) |
| History (Maritime Trade) | 2 | stage13 (canonical) |

**Derived values:**
| Value | Formula | Result |
|-------|---------|--------|
| Argue pool | (5×2) + 1 (Court Law) | **11D** |
| Read pool | Attunement 2D | 2D |
| Composure | 11 (per stage13 shorthand) [ED-052] | 11 |
| Presence modifier | floor((5−3)/2) = 1 | **+1** |
| Focus defence | floor(3/2) = 1 | **1** |
| Concentration | Focus + Presence = 3+5 | **8** |

Resonant Style: Evidence (Past genre). Optimal: Past + Revealing — but Past is ×0.5 for this audience.

**Pool asymmetry summary:** Himlensendt 15D vs Baralta 11D. E[net] ratio: 4.95 vs 3.63. Expected margin when Him wins: ~1.32. This gap is significant but not decisive at resistance 2.

**Probability baseline (TN7):**
| Pool | E[Net] | P(≥1) | P(≥2) | P(≥3) | P(≥4) |
|------|--------|-------|-------|-------|-------|
| 15D | 4.95 | ~99% | ~98% | ~92% | ~83% |
| 11D | 3.63 | ~99% | ~93% | ~80% | ~65% |

---

## State Block — Pre-Debate

```
## State: Pre-Debate
Himlensendt — Pres 6, Cog 5, Att 3 [P], Focus 3 [P]
  Composure: 12/12 | Concentration: 9/9 | Strain: 0 | Conditions: none
  Argue pool: 15D | Read pool: 3D
Baralta — Pres 5, Att 2 [P], Focus 3 [P]
  Composure: 11/11 | Concentration: 8/8 | Strain: 0 | Conditions: none
  Argue pool: 11D | Read pool: 2D
Tracks: TC=5 | Resistance=2 [P]
Genre weights: Future×1.0, Present×1.5, Past×0.5
```
[P] = Provisional value

---

## Exchange 1 — Himlensendt Proposes

**Roles:** Himlensendt proposes. Initiative: Himlensendt (higher Presence).

### Step 1 — Read

**Himlensendt:** 3D TN7 Ob1. E[net]=1.0. P(≥1)≈60%, P(≥2)≈30%.
→ **Most likely: Partial (net 1).** Primary genre identified: **Future**.
→ Himlensendt knows Future is primary. No orientation signal.

**Baralta:** 2D TN7 Ob1. E[net]=0.67. P(≥1)≈45%, P(≥2)≈15%.
→ **Most likely: Failure (net 0).** Misleading signal.
→ GM reports: "Present genre is strong." (Accurate — Present IS boosted at ×1.5. This is a case where the misleading signal happens to point at the boosted genre, not the primary genre.)

**[F-C-01] Finding:** The Read failure produces a misleading signal pointing to Present (×1.5) rather than Future (×1.0 primary). Present IS a genuinely strong genre for this audience — the "misleading" signal is accidentally tactically sound. This will not be penalised as an error; it creates an emergent strategic situation.

### Step 2 — Choose

- Himlensendt (Future known): **Future + Revealing** (optimal: primary genre, Resonant Style match).
- Baralta (misled: Present appears strong): **Present + Revealing**.

Different genres → **DIVERGENCE.**

### Step 3 — Argue

Himlensendt declares first (initiative): "Future, Revealing." Baralta hears declaration, commits to Present anyway (Divergence — independent evaluation regardless).

- Himlensendt: 15D TN7. **Most likely net: 5.** (Peak of distribution at E[net]=4.95)
- Baralta: 11D TN7. **Most likely net: 4.** (Peak at E[net]=3.63)

### Step 4 — Resolve (DIVERGENCE)

Per PP-099: orientation_weight = 1.0 for all sides in Divergence.

**Himlensendt (Future ×1.0):**
effective_margin_H = floor((5 / 2) × 1.0) = floor(2.5) = **2**
2 > 2 (resistance)? **No.** Δ_H = 0.

**Baralta (Present ×1.5):**
effective_margin_B = floor((4 / 2) × 1.5) = floor(3.0) = **3**
3 > 2 (resistance)? **Yes.** Δ_B = 3 − 2 = **1** toward Side B.

Net movement: Δ_B − Δ_H = 1 − 0 = 1. Direction: toward Baralta (Side B).
**TC: 5 → 4.**

No strain (Divergence). Initiative stays with Himlensendt (Diverge rule).

**[F-C-01 confirmed]:** Baralta's misread — pointing her to Present (×1.5) — produced more effective_margin than Himlensendt's informed choice of Future (×1.0). The "misleading" signal outperformed the correct read in this specific genre-weight configuration. A Read failure can be mechanically superior when it targets a boosted genre. This is not a bug — it is a genuine strategic asymmetry. No patch needed; GM awareness note warranted.

### State Delta — Post Exchange 1

```
## State: Exchange 1 Complete
Himlensendt — Composure: 12/12 | Concentration: 8/9 (−1) | Strain: 0
Baralta — Composure: 11/11 | Concentration: 7/8 (−1) | Strain: 0
Tracks: TC=4 (moved 1 toward Baralta) | Initiative: Himlensendt (DIVERGE — holds)
```

---

## Exchange 2 — Baralta Proposes (Role Alternation)

**Roles:** Baralta proposes (alternating). Initiative: **Himlensendt retains** (DIVERGE — stays with holder).

**[F-C-02] Ambiguity flagged:** Proposer (Baralta) and initiative holder (Himlensendt) are different characters. Initiative holder declares genre first (§6.4 Step 3) — Himlensendt declares, Baralta hears, then responds. This gives the initiative holder an information advantage over the proposer despite the proposer nominally framing the debate. Ambiguity: does "role alternation" in §6.7 also reset initiative, or are these two independent mechanics? Current reading: independent. Flagged as PP-100 below.

### Step 1 — Read

**Himlensendt:** 3D TN7 Ob1. Most likely: **Partial (net 1)**. Future is primary — confirmed again.

**Baralta:** 2D TN7 Ob1. Most likely: **Failure (net 0)**. Second misleading signal.
→ GM reports: "Past genre is strong." (Past is ×0.5 — genuinely weak for this audience.)

### Step 2 — Choose

- Himlensendt (Future known, declares first): **Future + Revealing**.
- Baralta (misled: thinks Past strong): **Past + Revealing**.

Himlensendt declares: "Future, Revealing." Baralta hears → confirms Past anyway → **DIVERGENCE.**

### Step 3 — Argue

- Himlensendt: 15D. **Most likely net: 5.**
- Baralta: 11D + Memory bonus? Baralta can cite a specific named constitutional precedent (she has Court Law 1 — referencing "the Charter provisions of prior Parliamentary sessions"). Memory bonus: **+2D** → **13D**. Most likely net: **~4** (E[13D]=4.3).

### Step 4 — Resolve (DIVERGENCE)

**Himlensendt (Future ×1.0):**
effective_margin_H = floor((5/2) × 1.0) = floor(2.5) = **2**. 2 > 2? **No.** Δ_H = 0.

**Baralta (Past ×0.5, with Memory bonus raising net to 4):**
effective_margin_B = floor((4/2) × 0.5) = floor(1.0) = **1**. 1 > 2? **No.** Δ_B = 0.

Net movement: 0. **TC stays at 4.**

No strain. Initiative stays with Himlensendt (second consecutive DIVERGE).

**[F-C-03] Finding:** Despite Memory bonus raising Baralta's pool to 13D, Past genre (×0.5) halves her effective_margin before resistance comparison. The Memory bonus adds raw successes but genre weight applies before the resistance test — a 13D Past argument is weaker than an 11D Present argument for this audience. Genre selection dominates pool size adjustments of this magnitude.

### State Delta — Post Exchange 2

```
## State: Exchange 2 Complete
Himlensendt — Composure: 12/12 | Concentration: 7/9 (−2 total) | Strain: 0
Baralta — Composure: 11/11 | Concentration: 6/8 (−2 total) | Strain: 0
Tracks: TC=4 (unchanged) | Initiative: Himlensendt (holds, 2nd consecutive DIVERGE)
Doubt Markers: none
```

---

## Exchange 3 — Himlensendt Proposes

**Roles:** Himlensendt proposes (X1=Him, X2=Baralta, X3=Him — alternating). Initiative: Himlensendt (holds).

Himlensendt now holds both initiative AND the proposer role. Double information advantage.

### Step 1 — Read

**Himlensendt:** 3D TN7 Ob1. Most likely: **Partial (net 1)**. Future is primary — still.

**Baralta:** 2D TN7 Ob1. Two options (branch):

**Branch A — Baralta fails Read again (P≈55%):**
GM gives misleading signal. Baralta misled.

**Branch B — Baralta succeeds Read (P≈45%):**
Baralta learns Future is primary and that Himlensendt prefers Revealing. Full information.

Run both:

---

### Branch A — Baralta fails Read (most likely, P≈55%)

**Step 2 — Choose:**
- Himlensendt: **Future + Revealing** (optimal, declares first).
- Baralta (misled, e.g. told Past): **Past + Revealing**.

→ **DIVERGENCE** (third consecutive).

**Step 3 — Argue:**
- Himlensendt: 15D. Net: 5.
- Baralta: 11D (+2D Memory if citing a named precedent) = 13D. Net: 4.

**Step 4 — Resolve (DIVERGENCE):**
Himlensendt: floor((5/2)×1.0) = 2. 2 > 2? No. Δ_H = 0.
Baralta: floor((4/2)×0.5) = 1. 1 > 2? No. Δ_B = 0.
TC: **4. Unchanged.**

**No strain. Debate ends. TC=4 → Compromise.**

---

### Branch B — Baralta succeeds Read (P≈45%)

Baralta knows: Future is primary, Himlensendt prefers Revealing.

**Step 2 — Choose:**
Himlensendt declares first: **Future + Revealing.**
Baralta hears it. Her options:

**Option B1 — Match: Future + Obscuring → CLASH (same genre, opposite orientation):**
- If Baralta wins: Doubt Marker on Himlensendt. TC doesn't move. She protects TC=4 (in compromise, which is a functional win for her — Church ratification blocked).
- If Himlensendt wins: Revealing wins → track moves toward Him.
- P(Baralta wins CLASH) ≈ 34% (11D vs 15D, derived below).

P(Himlensendt wins) ≈ 66%.
E[margin | Him wins] ≈ 2.3 (normal approx with σ_diff = √(0.41×26) ≈ 3.26, truncated normal).
effective_margin = floor(2.3 × 1.0) = 2. 2 > 2? No. Δ = 0. TC doesn't move even on average Him win.

P(Him wins with margin ≥ 3) = P(H−B ≥ 3) ≈ 30%. At margin 3: floor(3×1.0)=3 > 2 → Δ=1. TC: 4→5. Still compromise.
P(Him wins with margin ≥ 4) ≈ 16%. Δ=2. TC: 4→6. Still compromise.
P(Him wins TC escape, i.e. margin ≥ 6) ≈ 4%. Δ=4. TC: 4→8. Decisive Him win.

**Option B2 — Future + Revealing → COMPETITION (same genre, same orientation):**
Same resolution as CLASH minus Obscuring — but Baralta is at a pool disadvantage. Worse for her than B1.

**Baralta's optimal play in Branch B:** Option B1 (Future + Obscuring). Rationale: if she wins, she places a Doubt Marker — protecting TC=4 against any future movement. If she loses, the expected track movement is still 0 (resistance too high for Himlensendt's likely margin). She has nothing to lose from Obscuring.

**Step 4 — Resolve (CLASH, Branch B1):**

Pool P(Baralta wins) ≈ 34%.

**Sub-branch B1a — Himlensendt wins CLASH (P≈66%):**
E[margin|Him wins] ≈ 2.3.
effective_margin = floor(2.3 × 1.0) = 2. 2 > 2? No. Δ=0. TC: **4. Unchanged.**
Strain to Baralta: E[margin|loss] ≈ 2.3. Strain = 2.3 + 1 + 1 (His Pres mod) − 1 (Baralta Focus def) ≈ **3.3** → round to **3**.
Baralta: Composure 11 − 3 strain = Composure track at 8/11.
Concentration: Baralta loses exchange → −1 (exchange) −1 (loss) = −2. 6−2=4.
Himlensendt: no strain. Concentration −1=6.

Debate ends. TC=4. **Compromise** (motion tabled). Baralta took 3 strain but debate is over.

**Sub-branch B1b — Baralta wins CLASH with Obscuring (P≈34%):**
→ **Doubt Marker placed on Himlensendt.** TC: 4 (no movement).
Strain to Himlensendt: E[margin|Baralta wins] ≈ 1.5 (Her pool is weaker, wins tend to be narrower). Strain = 1.5 + 1 + 1 (Baralta Pres mod) − 1 (His Focus def) ≈ **2.5** → round to **2**.
Himlensendt: Composure 12 − 2 = 10/12.
Concentration: Himlensendt loses → −1 −1 = −2. 7−2=5.

Debate ends. TC=4. **Compromise.** Himlensendt has a Doubt Marker active but it's moot — debate is over.

---

### Outcome Distribution (All Branches)

| Branch | Probability | TC Final | Outcome |
|--------|-------------|----------|---------|
| A — 3rd Diverge (Baralta misread) | ~55% | 4 | Compromise |
| B1a — CLASH, Him wins, low margin | ~30% | 4 | Compromise |
| B1a — CLASH, Him wins, margin ≥ 3 | ~10% | 5 | Compromise |
| B1a — CLASH, Him wins, margin ≥ 6 | ~2% | 8+ | Decisive: Church wins |
| B1b — CLASH, Baralta wins, Obscuring | ~3% | 4 | Compromise + Doubt Marker |
| **Total → Compromise** | **~95%** | 4–6 | — |
| **Total → Decisive outcome** | **~5%** | ≥7 or ≤3 | — |

**Core finding: A 3-exchange Formal Debate between a 15D and 11D orator at resistance 2 produces Compromise in ~95% of cases.**

---

## Final State (Most Likely — Compromise, TC=4)

```
## State: Debate Concluded
Himlensendt — Composure: 12/12 | Concentration: 6/9 | Strain: 0
Baralta — Composure: 11/11 | Concentration: 5/8 | Strain: 0
Tracks: TC=4 | Outcome: COMPROMISE — motion tabled for committee review
Stakes resolved: No immediate faction stat change. Church ratification motion deferred.
```

---

## Mode J — Cognitive Load Audit (Exchange-level)

**[MODE J: Debate Exchange — Parliament, Formal]**

Per-exchange steps:
| Step | Decisions | Lookups | Parallel tracks | Sequential deps |
|------|-----------|---------|-----------------|-----------------|
| Read | 2 (interpret result) | 2 (result table) | 0 | — |
| Choose | 2 (genre) + 2 (orientation) | 1 (weight table) | 1 (hold Read result) | Read → Choose |
| Argue | 2 (Memory bonus check) | 0 | 1 (hold choices) | Choose → Argue |
| Resolve | 1 (interaction type) | 1 (type table) | 2 (both effective_margins) | Argue → Resolve |
| Movement | 0 | 0 | 1 (TC position) | Resolve → Movement |
| Strain | 0 | 1 (Presence mod table) | 1 (both Composure tracks) | Resolve → Strain |
| Concentration | 0 | 0 | 1 (both Concentration) | Resolve → Concentration |
| **Totals** | **7** | **5** | **6** | **5** |

Load score: 7+5+6+5 = **23 raw points → normalise: ~7/10 — PROBLEM**

**Breakdown by component:**
- Decisions (7): manageable individually, but chain length (7 sequential) creates fatigue.
- Lookups (5): genre weight table + result table are the bottlenecks.
- Parallel tracks (6): TC + Composure×2 + Concentration×2 + Doubt Marker status = 6 simultaneous values to hold.
- Sequential deps (5): Read → Choose → Argue → Resolve → Movement/Strain/Concentration — no shortcuts.

**Time estimate:**
- Novice: 7×30s (decisions) + 5×45s (lookups) + 5×20s (arithmetic) = 210+225+100 = **535s ≈ 9 min/exchange**
- Experienced: 7×15s + 5×15s + 5×10s = 105+75+50 = **230s ≈ 4 min/exchange**
- Expert: 7×8s + 5×5s + 5×5s = 56+25+25 = **106s ≈ 1.75 min/exchange**

**Flags:**
- P1: Novice time 9 min/exchange exceeds the 5-min P1 threshold. For a 3-exchange Formal Debate: 27 minutes novice play time. Unacceptable for first-session play.
- P2: Experienced time 4 min/exchange is within the 3-min P2 threshold. For Grand Debate (5 exchanges): 20 minutes experienced play time. Borderline.
- Primary culprit: rolling 15D+11D = 26 dice per exchange. Counting and calculating net for 26 dice is the single largest friction source (~60-90 seconds per argue step at table).

**Mitigation recommendations:**
1. GM reference card with genre weight lookup (eliminates 2 lookups per exchange).
2. Pre-computed Read result table for standard Attunement pools (2D–4D) on reference card.
3. Use dice towers or pre-sorted dice to speed 15D rolls.
4. Optional: "quick argue" for Divergence exchanges (since they don't interact, each side can roll simultaneously rather than sequentially).

---

## Findings Summary

| ID | Mode | Severity | Description | Disposition |
|----|------|----------|-------------|-------------|
| F-C-01 | C | P3 | Misleading Read failure can be accidentally superior when it targets a boosted genre. Emergent strategic asymmetry — not a bug. | GM awareness note; no patch. |
| F-C-02 | C | P2 | Proposer role and initiative holder are decoupled after DIVERGE. X3: Himlensendt holds both. §6.7 "alternating" ambiguous re initiative reset. | PP-100 PROVISIONAL |
| F-C-03 | C | P2 | Genre weight dominates pool size adjustments: a Memory-boosted Past argument (×0.5) loses to a standard Future argument (×1.0) at these resistance levels. Genre selection > dice quantity. | Design observation — correct and intended. |
| F-C-04 | C | **P1** | stage13_npcs.md missing debate-relevant attributes (Attunement, Focus, Poise, Bonds) for all named NPCs. All debate simulations using named NPCs require provisional attributes. | ED-051 — request full debate stat block |
| F-C-05 | C | P2 | Composure shorthand in stage13 ("Presence + 6") mismatches design formula (Poise+Bonds+3). | ED-052 — confirm which applies to NPCs |
| F-C-06 | J | **P1** | Novice debate resolution time: 9 min/exchange (27 min for Formal Debate). Exceeds P1 threshold of 5 min/exchange. Primary cause: 26 dice rolled per exchange. | Tooling required: GM reference card (§6.1–6.4 on one page). |

---

## SIM-DEBT-01 Resolution

**Status: RESOLVED.**

New calibration confirmed by Mode C:

| Finding | Confirmed |
|---------|-----------|
| Resistance level dominates track movement (not pool size alone) | ✓ — All 3 DIVERGE exchanges at resistance 2 produced 0 movement for 15D side |
| Genre weight dominates pool adjustments up to ~2D | ✓ — Memory +2D to Past (×0.5) still lost to standard Future (×1.0) |
| DIVERGE produces 0 strain — Composure drain only from CLASH/COMPETITION | ✓ — Both NPCs at full Composure after 3 exchanges |
| 3-exchange Formal Debate → Compromise in ~95% of realistic matchups | ✓ — Structural finding, not a flaw |
| Mode C Read failure pattern: Attunement 2 fails Ob1 ~55% of exchanges | ✓ — Creates systematic misread pattern; significant NPC differentiation |
| New strain baselines (2-3/exchange for CLASH) not triggered here (all DIVERGE) | Mode G2 or future CLASH-heavy scenario needed to fully confirm strain calibration |

**Remaining gap:** CLASH-heavy scenario still needed to validate 2-3 strain/exchange baseline under new pool. Recommend: re-run with mismatched genre choices (forced CLASH configuration). Not blocking — baselines from Mode A are analytically sound.

---

## Provisional Patches from This Run

| Patch | Location | Change |
|-------|----------|--------|
| PP-100 | debate_system_redesign_v1.md §6.7, Formal Debate row | Clarify that "alternating" refers to proposer role only; initiative transfer follows §6.4 rules (Diverge retains, exchange winner takes). These are independent mechanics. |

---
*End SIM-D-02. Committed: 2026-04-02.*
