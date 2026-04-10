<!-- DEPRECATED: 2026-04-09 — SUPERSEDED BY designs/board_game/valoria_bg_v05_simulation_and_patches.md. Do not use as a mechanical reference. Retained for audit trail only. -->

# BG IMPROVEMENT — CONSOLIDATED SYNTHESIS

**Date:** 2026-03-31
**Inputs:** bg_improvement_review.md (Opus canon review), bg_synthesis.md (Sonnet throughline synthesis)
**Purpose:** Merge findings, resolve divergences, produce authoritative assessment

---

## WHERE BOTH REVIEWS AGREE

These findings are confirmed by independent analysis from different angles:

| Finding | Opus (Canon) | Sonnet (Throughline) | Status |
|---------|-------------|---------------------|--------|
| MP-10 Hafenmark Einhir lineage | P-08 FAIL — hereditary TS violates §14 | Cut — "TS is gained through held confrontation, not heredity" | **Confirmed violation. Cut the card.** |
| MP-31 Concordia as primary action economy | Mechanically sound, no canon concerns | "Most Valorian action economy proposal across all four waves" | **Confirmed. Adopt.** |
| MP-17 Fate Cards | No canon flag raised | Hard cut — "metaphysically incoherent in Valoria; no fate to cheat" | **Confirmed. Cut.** |
| MP-01 Mandate Dice | No strong flag | Cut — randomness contradicts TTRPG deterministic capability | **Confirmed. Cut.** |
| MP-13 Order Fatigue | No strong flag | Cut — superseded by MP-29 | **Confirmed. Cut.** |
| MP-19 Token Commitment | No strong flag | Cut — double jeopardy without setting justification | **Confirmed. Cut.** |
| MP-15 Development Tracks | No flag | Cut — superseded by MP-30 | **Confirmed. Cut.** |
| Self-assessed compliance is unreliable | 33/33 self-assessed PASS; 4 failures found | (Not explicitly flagged but Sonnet independently catches the MP-10 violation) | **Confirmed. Institute independent review.** |

---

## WHERE THE REVIEWS DIVERGE

These are the productive disagreements. Each needs resolution.

### 1. MP-24 Church Attention Pool — Detection Mechanism

**Opus:** P-08 PARTIAL FAIL. The trigger "+2 Attention for any Thread operation" implies the Church detects Thread operations as such. §9.1–9.2 say Church theology forecloses this perceptual capacity. Triggers must be rewritten as consequence-detection (behavioral/social indicators), not operation-detection.

**Sonnet:** KEEP. "Institutional surveillance mechanic. The Church IS the world's monitoring apparatus for Thread activity (P-08 rendered-world institutional expression)."

**Resolution:** Opus is correct on the mechanism, Sonnet is correct on the function. The Church *does* monitor for heretical activity — but it monitors rendered-world indicators (behavioral patterns, community gatherings, structural anomalies), not Thread operations directly. The Church cannot perceive Thread events because its theology forecloses Thread sensitivity (§9.1). It perceives the *social and physical consequences* of Thread events.

**Fix:** Keep MP-24. Rewrite trigger language. Mechanical outcome is identical. The Church's Attention Pool fills when Thread operations produce visible rendered-world disturbances — which they always do (P-01 co-movement guarantees actualized consequences). The fiction is: the Church's surveillance network detects heretical *behavior*, not Thread *operations*. Same numbers, correct epistemology.

---

### 2. MP-12 Thread Debt — Dischargeable Resource

**Opus:** P-11 INSUFFICIENCY. Thread Debt reduces temporal disjunction to bookkeeping — incur, repay, done. The Foundations say temporal disjunction accumulates and the rendering re-integrates *slowly* (§20.3). Substrate strain persists regardless of subsequent Mend operations.

**Sonnet:** KEEP as-is. "Most canon-coherent unimplemented proposal. P-11 (temporal disjunction is universal) expressed mechanically."

**Resolution:** Opus raises a legitimate point that Sonnet misses. However, the fix should be proportional — Thread Debt is a good mechanic that needs a residual cost, not a redesign. 

**Fix:** Thread Debt tokens can be "repaid" (stopping the RS −1/season bleed), but repayment leaves a permanent **Substrate Scar** marker in the territory where the debt was incurred. Substrate Scars have minor persistent effects: +1 Ob to all Thread operations in that territory permanently, TR +1 baseline in that territory permanently (the substrate remembers the strain). This preserves Thread Debt's playability while expressing the Foundations' insistence that temporal manipulation has irreducible residual cost. Scars accumulate — a territory with 3+ Scars is mechanically approaching Thread Wound status.

---

### 3. MP-18 Revolution — Thread-Only Faction

**Opus:** P-01/P-08 TENSION. Making Community Weaving Revolution's *sole active action* conflates the political movement with Thread practice. Not all Revolution members are practitioners.

**Sonnet:** KEEP. "Rawlsian framework expressed as distributed community infrastructure."

**Resolution:** Both are partially right. The Revolution is a political movement that *includes* Thread practitioners but is not *exclusively* Thread practice. The Quiet Year framing (Sonnet's core reference) is correct — Revolution builds community projects, which are rendered-world political activities. Community Weaving is the Thread-specific subset.

**Fix:** Revolution has two action types within the Presence system:
1. **Community Organizing** (rendered-world): Move Presence markers, build non-Thread Projects (Fortification, Diplomatic Mission), recruit. No Thread operation. No co-movement. No Attention Pool trigger.
2. **Community Weaving** (Thread operation): RS restoration, Einhir Memory Recovery. Requires practitioner Presence in territory. Produces full three-dimensional co-movement. Triggers Attention Pool.

The distinction matters: Revolution can spread politically without triggering Church surveillance. When they engage in actual Thread work, the full metaphysical cost structure applies. This is the rendered-world/ontological boundary made playable.

---

### 4. MP-04 Thread Resonance — High-TR Effects for Non-Sensitives

**Opus:** P-08 BORDERLINE. TR 4–5 gives non-sensitive factions informational access to Thread-level phenomena.

**Sonnet:** KEEP without qualification. "Environmental sensitivity without capability (P-08 preserved)."

**Resolution:** Opus is correct that TR 4–5 for non-sensitive factions is questionable. The cap solution is clean: non-Thread factions cap at TR 3 unless they have a Thread-sensitive agent present in the relevant territory. TR 4–5 effects represent deeper Thread awareness that requires someone who can actually perceive at that level.

**Fix:** Add to TR rules: "Factions without a Thread-sensitive agent in the affected territory: TR caps at 3. TR 4–5 available only when a Thread-sensitive character (Revolution member, Varfell TK-qualified agent, or practitioner NPC) is present."

---

### 5. P-14 Co-Movement in BG Mode

**Opus:** SYSTEMIC FAIL. No Thread-labeled BG proposal implements three-dimensional co-movement. §21.1 describes the required solution (triangular track). P-14 violation test: "Does any play mode allow thread operations without three-dimensional co-movement? If yes → FAIL."

**Sonnet:** Not addressed. The synthesis endorses Thread proposals (MP-12, MP-21, MP-24) without noting the missing co-movement protocol.

**Resolution:** Opus is correct. This is the single largest canon gap in the entire BG design. Every Thread operation in the BG must produce effects across all three dimensions. The existing co-movement card deck is an event system, not a consequence system.

**Required new design work:** A BG Co-Movement Resolution Protocol. For every Thread operation:
- **Actualized effect:** The intended result (RS change, Community Weave completion, etc.)
- **Temporal auto-effect:** History Resonance marker placed in territory (represents temporal disjunction; affects future operations there)
- **Epistemic auto-effect:** Information consequence (something revealed or obscured — Church Attention Pool trigger, faction stat visibility change, or Thread Veil interaction)

This can be encoded on Thread operation cards or as a fixed table on the faction card. It does not require GM judgment — it is deterministic, per §21.1.

[EDITORIAL: Co-movement auto-effect tables for BG Thread operations. This is mechanical design, not setting content — but the specific epistemic and temporal consequences per operation type need authoring.]

---

### 6. MP-16 Conviction — Resonant Style Labels

**Opus:** P-03 CONCERN. Resonant Styles are Thread-ontological categories being given to non-sensitive political actors.

**Sonnet:** KEEP. "Direct TTRPG throughline."

**Resolution:** This is a terminology issue, not a mechanical one. The fix is renaming, not cutting. Use politically descriptive labels in BG context — the mechanical function is identical but the epistemic boundary is cleaner.

---

## WHAT SONNET SURFACES THAT OPUS MISSES

### The BG Is Not a Standalone Game

Sonnet's Fact 1 — "Board game is primarily GM-side scenario engine; never faction-only" — is a critical framing that changes how every proposal should be evaluated. The BG is the strategic phase of a hybrid system. Proposals that make the BG feel *complete* as a standalone experience (extensive solo mode, hidden secondary objectives, full victory scoring) risk undermining the hybrid architecture.

**Implication:** MP-23 (Hidden Secondary Objectives) and MP-36 (Hollow Victory) are correctly labeled as BG-only rules that disable in hybrid. MP-06 (Solo) is an accessibility accommodation, not a core mode.

### MP-34 Institutional Belief — The Missing Core

Sonnet correctly identifies that the TTRPG's central mechanic (Beliefs generating friction) has no BG equivalent. MP-34 (Institutional Mandate with Uphold/Compromise response) fills the gap. This is the most significant new proposal across either review.

The Uphold/Compromise structure maps directly to the TTRPG's Belief-challenge-response loop and creates the BG's version of the hollow victory question: what does it mean to win while compromising what you claim to stand for?

**Assessment:** MP-34 should be Tier 1. Canon-compliant — Institutional Mandates are rendered-world political identity statements, not Thread-ontological claims.

### MP-35 Cascade Phase Card Effects

Sonnet's proposal for personal-scale outcomes modifying the BG card economy (MP-31) is an excellent hybrid bridge design. It makes the Cascade Phase mechanically consequential in a way that current Domain Echoes do not.

**Assessment:** MP-35 is well-designed. Tier 2 (requires MP-31 adoption first). Compatible with all canon constraints.

### MP-36 Hollow Victory Scoring

The Legitimacy Modifiers system (Contempt reduces Deeds, Mandate upheld increases them, RS below 20 = all victories hollow) gives the BG-only mode a version of the hybrid's moral-weight mechanic.

**Assessment:** Good BG-only rule. Tier 2.

### Landmark Game Feel Assessment

Sonnet's categorization of reference games into "Deeply Right / Right in Principle / Productive but Incompatible / Thematically Opposed" is more useful than the V1–V4 documents' flat "here's what this game teaches." The key insight: **The Quiet Year, Pax Pamir, Concordia, and Pendragon understand what Valoria is. War of the Ring, Root, and Malifaux do not.**

The central argument — "Valoria's board game should feel like what happens when powerful institutions try to manage a world that is quietly dying" — is the correct throughline test for every proposal.

---

## WHAT OPUS SURFACES THAT SONNET MISSES

### RS vs TC/IP Philosophical Asymmetry

RS is ontological (substrate degradation). TC and IP are rendered-world (political/institutional). The Foundations give RS metaphysical priority — if RS fails, TC and IP are meaningless because the world sustaining them has structurally failed. No proposal or synthesis makes this asymmetry mechanically explicit. RS degradation should affect the baseline difficulty of all territorial actions (the substrate supporting activity is weakening), not just trigger threshold events.

### Foundations Amendment Implications

The Self-Rendering Amendment establishes that all beings always-already threadwork their own existence. At Coherence 0, outcomes branch by TS. If Champion NPCs approach Coherence 0 during BG play (which the TTRPG arcs suggest for Vaynard, Almud, and Lenneth), their continued existence *strains the substrate* proportionally to their TS (Amendment §4). The Champion system (MP-25) and Research Tracks (MP-30) don't account for this. A Resonant Champion at Coherence 0 is a localized Calamity risk.

### Process: Independent Canon Review

The fact that self-assessed compliance produced 33/33 PASS while independent review found 4 failures, 2 borderlines, and a systemic gap is a methodological finding. Future BG proposals should undergo independent canon-guard review, not self-assessment.

---

## CONSOLIDATED VERDICT TABLE

| ID | Opus | Sonnet | Consolidated Verdict |
|----|------|--------|---------------------|
| MP-01 | — | CUT | **CUT** |
| MP-02 | No flag | KEEP (mod: sealed pledges) | **KEEP (modified)** |
| MP-03 | No flag | KEEP (integrated) | **KEEP** |
| MP-04 | P-08 borderline (TR 4–5) | KEEP | **KEEP + cap TR at 3 for non-sensitive factions** |
| MP-05 | No flag | KEEP (mod: institutional flavor) | **KEEP (modified)** |
| MP-06 | No flag | KEEP (mod: Concordia solo) | **KEEP (modified)** |
| MP-07 | No flag | KEEP (integrated) | **KEEP** |
| MP-08 | No flag | KEEP (integrated) | **KEEP** |
| MP-09 | No flag | KEEP (integrated) | **KEEP** |
| MP-10 | P-08 FAIL (Hafenmark card) | KEEP (cut Baralta lineage) | **KEEP + cut Baralta lineage card** |
| MP-11 | No flag | KEEP (mod: domain expertise) | **KEEP (modified)** |
| MP-12 | P-11 insufficiency | KEEP | **KEEP + add Substrate Scar residual** |
| MP-13 | — | CUT | **CUT** |
| MP-14 | No flag | KEEP (mod: defensive only) | **KEEP (modified)** |
| MP-15 | — | CUT | **CUT** |
| MP-16 | P-03 concern (labels) | KEEP | **KEEP + rename Resonant Style refs** |
| MP-17 | — | CUT (hard) | **CUT** |
| MP-18 Rev | P-01/P-08 tension | KEEP | **KEEP + split Community Organizing / Community Weaving** |
| MP-18 Church | No flag | KEEP | **KEEP** |
| MP-18 Niflhel | No flag | KEEP | **KEEP** |
| MP-18 Guilds | No flag | KEEP (mod: 1 merc unit) | **KEEP (modified)** |
| MP-19 | — | CUT | **CUT** |
| MP-20 | No flag | KEEP (Leader Age optional) | **KEEP (modified)** |
| MP-21 | P-14 (no co-movement) | KEEP | **KEEP + requires BG co-movement protocol** |
| MP-22 | No flag | KEEP | **KEEP** |
| MP-23 | No flag | KEEP (BG-only) | **KEEP (BG-only)** |
| MP-24 | P-08 partial fail (triggers) | KEEP | **KEEP + rewrite triggers as consequence-detection** |
| MP-25 | No flag | KEEP + Niflhel mod | **KEEP (modified)** |
| MP-26 | No flag | KEEP | **KEEP** |
| MP-27 | No flag | KEEP | **KEEP** |
| MP-28 | No flag | KEEP (simplified) | **KEEP (simplified)** |
| MP-29 | No flag | KEEP | **KEEP** |
| MP-30 | No flag | KEEP (reduced: 2 tracks) | **KEEP (reduced)** |
| MP-31 | No flag | KEEP — primary | **KEEP — primary structural recommendation** |
| MP-32 | No flag | KEEP | **KEEP** |
| MP-33 | No flag | KEEP | **KEEP** |
| MP-34 | — | NEW (Institutional Belief) | **ADOPT — Tier 1** |
| MP-35 | — | NEW (Cascade Phase) | **ADOPT — Tier 2** |
| MP-36 | — | NEW (Hollow Victory) | **ADOPT — Tier 2** |

**Summary:** 6 cut, 27 kept (12 modified), 3 new adopted.

---

## OUTSTANDING DESIGN WORK REQUIRED

Before any Tier 1 integration:

1. **BG Co-Movement Resolution Protocol** — deterministic three-dimensional auto-effects for all Thread operations in BG mode. Required by P-14. Blocks all Thread-labeled proposals.

2. **RS as Substrate Modifier** — mechanical rule making RS level affect baseline Ob for all territorial actions, not just trigger threshold events. Addresses the throughline gap where Thread is treated as subsystem rather than substrate.

3. **MP-34 Institutional Mandate text and trigger conditions** — per-faction content. [EDITORIAL]

4. **BG-E-30 decision** — MP-31 (Concordia Card-Hand) adoption. All Tier 1 proposals assume this as foundation.

These four items are preconditions. Without them, integration of Tier 1 proposals will produce the same "well-constructed Euro with a fantasy skin" problem the V1 gap analysis identified.

---

## REVISED IMPLEMENTATION SEQUENCE

### Preconditions (resolve before any Tier 1 work)
- BG-E-30: Adopt MP-31 (Concordia Card-Hand) — Y/N
- Design BG Co-Movement Resolution Protocol (P-14 compliance)
- Design RS-as-substrate-modifier rule
- [EDITORIAL] MP-34 Institutional Mandate text per faction

### Tier 1 — Structural core
1. MP-31 (Card-Hand) + MP-29 (Action Wheel) + MP-33 (Orientation)
2. MP-18 Revolution (split Organizing/Weaving) + MP-18 Church (TC-as-currency)
3. MP-34 (Institutional Belief) + MP-16 (Conviction, renamed)
4. MP-12 (Thread Debt + Substrate Scars) + MP-24 (Attention Pool, triggers rewritten)
5. MP-21 (Community Projects, with co-movement) + MP-22 (Contempt) + MP-27 (Crown Policy)

### Tier 2 — Deepening
MP-02, MP-11 (modified), MP-14 (defensive), MP-18 Niflhel + Guilds, MP-25, MP-26, MP-30 (2-track), MP-32, MP-35, MP-36

### Tier 3 — Polish
MP-05, MP-06, MP-10 (revised), MP-20, MP-23 (BG-only), MP-28
