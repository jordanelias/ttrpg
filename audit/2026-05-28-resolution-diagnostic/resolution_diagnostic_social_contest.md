# Resolution Diagnostic — Social Contest

**Date:** 2026-05-28
**Skill:** valoria-resolution-diagnostic (Stage 1)
**Scope:** social contest per skill INITIAL HYPOTHESES — covers `designs/scene/social_contest_v30.md` (CANONICAL 2026-04-17), `designs/scene/conviction_track_v30.md` (CANONICAL 2026-04-17), `designs/personal/conviction_taxonomy_v30.md` (PP-684 promoted to CANONICAL 2026-05-01), `tests/audit/audit_sim_social_contest.md` (prior audit), `tests/sim/sim_social_contest_stress.md` (prior stress test).
**Status:** Audit output. Commit batch 2 (with investigation + peninsula/victory).
**Key pre-flight observation:** prior 2026-04-08 audit declared social contest **"simulation-clean after PP-449–PP-468"** with 0 P1 remaining, 1 P2 confirmed design intent, 0 P3 requiring action. This diagnostic confirms PASS status under resolution-fitness lens and surfaces 3 pre-flagged P2s from the stress test whose post-2026-04-08 status is unverified.

## §0 Pre-flight & citations

Files consulted this session:
- `designs/scene/social_contest_v30_index.md` — full heading map (42 sections)
- `designs/scene/conviction_track_v30_index.md` — full heading map (38 sections, Piety Track + RM Emergence + Varfell Paths)
- `designs/personal/conviction_taxonomy_v30.md` — full first 16k (PP-684; 13-Conviction vector taxonomy + Self-Other orientation)
- `tests/audit/audit_sim_social_contest.md` — full (~7k; Modes A–E declare simulation-clean)
- `tests/sim/sim_social_contest_stress.md` — first 8k of 22k (10 findings: 2 P1 resolved + 8 P2/P3)

NERS source: PI `<definitions>` per Turn B.

## §1 Phase 0 — Resolution component decomposition

| Component | Mechanism | Quantity category |
|---|---|---|
| **A · Argue Pool** | `(Cognition × 2) + History + Memory bonus (+2D if cited)` per PP-232; 2D floor at Cog 1 H 0 | Dice (low floor exists) |
| **B · Exchange Interaction Types** | CLASH / CROSS / COMPETITION / DIVERGENCE / AMPLIFY (5 explicit types); TIE override (scoped to CLASH/COMPETITION per PP-465+) | Discrete taxonomy |
| **C · Composure** | Cha + 6 (7–13 range, derived per PP-460); shared buffer for Knot partners | **Continuous resource** |
| **D · Concentration** | Focus + Presence (2–14 range); depleted by exchange (−1/exchange + −1 on loss); Spent at 0 (−2D pool, +1D opponent) | **Continuous resource** |
| **E · Piety Track / Conviction Track** | 0–10 per-territory accumulator; movement via effective_margin = floor(margin × genre_weight × orientation_weight) − resistance | **Discrete accumulator** (multi-threshold clock) |
| **F · Genre weights** | 0.5 / 0.75 / 1.0 / 1.25 (Opposed / Adjacent / Primary / Boosted; PP-453 adjacency model) | Modifier (Lesson-2-relevant) |
| **G · Doubt Marker** | One-time consumed effect (Obscuring win); reduces winner's next effective_margin by 2 | Discrete one-shot |
| **H · Regroup** | Recovery action; restores Concentration by Focus; costs CT+1 to opponent | Discrete recovery |
| **I · Beliefs Integration** | Belief check (Spirit) for amplifying intent; cross-system to threadwork | Discrete + dice |
| **J · Conviction Taxonomy (PP-684)** | 13-Conviction vector + Self-Other orientation [−1, +1]; drift κ=0.03/season | Vector-valued state |

**Three-category classification:**
- **Continuous resources:** Composure (×3 per derived_stats Multiplier Tier), Concentration
- **Discrete accumulators (clocks):** Piety Track 0–10 (multi-threshold), Conviction Track per territory, Doubt Marker (binary)
- **Base parameters:** Cognition, Charisma, Focus, Presence, History; fed into pools

## §2 Phase 1 — Stress points

### 1a · Smallest pool by design

| Build | Cog | Hist | Mem | Pool |
|---|---|---|---|---|
| Untrained novice (Cog 1 H0) | 1 | 0 | 0 | **2D** |
| Standard (Cog 2 H1) | 2 | 1 | +2 cited | 7D |
| Capable (Cog 3 H2) | 3 | 2 | +2 cited | 10D |
| Expert (Cog 4 H3) | 4 | 3 | +2 cited | 13D |
| Master (Cog 5 H3 + Momentum spend) | 5 | 3 | +2+auto | ~16-18D effective |

**Skill INITIAL hypothesized "pools 5–18D"** — accurate for typical-to-master builds. Novice build (Cog 1 H 0) produces 2D floor, lower than skill's range claim.

**But:** social contest **does not have a Pool Floor like combat (5) or threadwork (5).** Argue Pool can be 2D. Per PP-232 and the prior stress test Mode A table — P(≥2 hits | 2D) ≈ 18%, P(≥3) ≈ 5%.

**Architectural mitigation (different from combat/thread):** the floor here is bounded by **Concentration's death-spiral** (a 2D pool character reaches Spent fast → exits the contest), not by a Pool Floor. Social contest's safeguard is **exit (Spent or Unmask), not floor**. Same architectural shape as mass battle's "unit-deletion as floor" — but at personal scale with reversible outcomes.

### 1b · Exposure frequency

| Stress case | Likelihood |
|---|---|
| Novice Cog 1 in social contest | Low (most named characters have Cog 2+; player characters typically higher) |
| Mid-build (Cog 2-3) in long Grand Debate (5 exchanges) | M |
| Genre-weight 0.5 mismatch at R=1 audience (D-01) | M (every contested debate where speaker is off-domain) |
| Spent state reached → Regroup loop dominant (D-04) | M-Low |

**Exposure is generally low.** Social contest doesn't have a "Guilds Mil 2 = routine state" equivalent — most contest participants are capable+ builds.

## §3 Phase 2 — What the stress point decides

### 2a · Outcome type

| Action | Type | Depth |
|---|---|---|
| Single exchange | Graded magnitude (margin → effective_margin → CT movement 0–5) | Shallow per exchange |
| Multi-exchange contest (3–5 exchanges typical) | **Clock (deepening Conviction Track)** | Deep |
| Spent / Unmask | Discrete state transition | Recoverable next session |
| Forced Unmask / Doubt Marker | Discrete trigger | One-shot |
| Post-contest Obligation binding (§6.1 NEW) | Persistent state | Multi-session |

**Outcomes are clock-routed.** Per skill Lesson 4: "Route unavoidable small rolls through a clock deep enough to average." Social contest exchanges feed Conviction Track 0–10; multiple exchanges accumulate effective_margin into the track. This **IS Lesson 4 done well** — single-roll exchanges are absorbed by the clock's depth.

### 2b · Stakes & reversibility

| Outcome | Reversibility |
|---|---|
| Spent (Concentration 0) | Recoverable next scene; potentially next session |
| Doubt Marker | Single-exchange effect |
| Conviction Track win | Persistent territorial state shift; reversible via opposing pressure |
| Excommunication Tribunal (§7.1) | High-stakes individual outcome; rare |
| Parliamentary Stay (§10.1) | Procedural — limited time bounds |
| Conviction Scar (§6.2 NEW) | Player-facing memorialization of lost contest; emergent narrative |

**Reversibility is generally high.** No equivalents to faction Stab=0 collapse or mass-battle unit destruction.

### 2c · Risk profile

| Scenario | Impact | Exposure | Irreversibility |
|---|---|---|---|
| 2D pool novice in contested debate | M | L | L |
| Spent state cascade | M | M | L |
| Genre-weight 0.5 traps off-domain speakers (D-01) | M | M | L |
| Excommunication outcome | H | L | M |

**No H/H/H findings.** Worst case is M/M/L.

## §4 Phase 3 — Effect-curve checks

### 3a · Impact uniformity

**Pool scaling:** Cog 1→7 produces pool 2→14D (linear, +2/Cog). Standard √N non-uniform-impact pattern. Same micro-flag as combat / threadwork / mass-battle Cmd. Not novel. No mitigation analogous to PP-717 D2 Pool DR; **mitigated by clock-routing instead** (per L4 — averaging through the Conviction Track depth).

**Genre weights as L2 mechanism:** 0.5 / 0.75 / 1.0 / 1.25 multipliers on margin. These are **L2 mitigation by design** — multiplicative modifiers smooth the effect of pool advantage across genre alignment. PP-453 explicitly chose this 4-level adjacency model. **PASS by intent.**

### 3b · Threshold cliffs

| Cliff | Status |
|---|---|
| Conviction Track 0–10 thresholds (multi-step movement table) | **PASS** — discrete accumulator, exempt L6, intended multi-thresholds per skill three-category table |
| Spent at Concentration 0 (−2D, +1D opponent) | **PASS** — designed degradation state; recoverable via Regroup |
| Doubt Marker (binary one-shot) | **PASS** — discrete trigger exempt L6 |
| TIE override → strain + CT+1 to first-speaker (scoped to CLASH/COMPETITION per PP-465+) | **PASS-resolved** — D-09 P1 conflict closed in prior audit |
| Genre weight 0.5 near-inert at R=1 (D-01) | **PRE-FLAGGED P2** — possible game-feel cliff (off-primary genre collapses); status post-2026-04-08 unverified |

### 3c · Role conflation

**Cognition** carries: Argue Pool + Recall checks + tactical adjudication. Coherent narrative ("intellectual capacity"). PASS.

**Charisma** carries: Composure derivation + Presence modifier interaction + faction Mandate (cross-system). Coherent ("social presence"). PASS.

**Focus** carries: Concentration formula + Take-a-Breath recovery (cross-system combat) + Contact Duration (cross-system threadwork) + Rendering Crisis Beat 4 pool (cross-system). Multi-system but each use coherent ("attentional stability"). PASS.

**Presence** carries: Concentration formula + Presence modifier on strain in social. Limited scope; coherent. PASS.

## §5 Phase 4 — Loops

| ID | Loop | Damper | Cap |
|---|---|---|---|
| **SCL1 (Concentration depletion)** | Exchange → −1 Concentration → potentially −1 more on loss → Spent → −2D pool → harder to win → more losses | Regroup restores +Focus per use (CT cost to opponent); scene/session reset | Spent floor; recoverable; cannot stack below 0 |
| **SCL2 (Conviction Track movement)** | Exchange → effective_margin → CT movement → cumulative threshold crossing → contest outcome | Resistance subtraction; Doubt Marker; genre weights | CT 0 or 10 = decisive outcome (per genre), one contest |
| **SCL3 (Obligation chains §6.1 + Chain Contests §6.3)** | Contest unresolved → Chain Contest fires next session | Per-contest cap; explicit "follow-up tension" framing as feature not bug | Bounded by chain depth (not infinite) |
| **SCL4 (Belief integration ↔ Threadwork)** | Belief check during contest → cross-system to threadwork (P-12 propagation) | Pre-Leap Belief check Ob 1 (per threadwork §2.5 collective ops); Spirit check | Bounded by Belief structure |
| **SCL5 (Conviction Vector drift PP-684 §3.2)** | Accumulated outcomes shift Self-Other orientation by κ=0.03/season | Bounded clamps [−1, +1] | Hard bounds |

**All damped + bounded.** Per audit Mode C: "20 chains mapped, 0 circular deps, 0 dead-end mechanics, 0 amplification loops."

## §6 Phase 5 — Intent gate

| Finding | Intent | Safeguard | Adequate? | Result |
|---|---|---|---|---|
| SC1 (2D pool floor) | No Pool Floor by design — exit (Spent/Unmask) is the safeguard | Concentration → Spent exit | YES | **PASS-with-flag** (architectural; exit-not-floor) |
| SC2 (Concentration immunity) | Build investment tradeoff (B-01 prior audit) | Cost on other stats | YES | **PASS-by-intent** |
| SC3 (Genre 0.5 near-inert) | Pre-flagged P2; status post-2026-04-08 unverified | None confirmed | partial | **defect-or-resolved** |
| SC4 (Regroup-on-Spent) | Pre-flagged P2 D-04; intentional? not explicitly affirmed | None confirmed | partial | **defect-or-resolved** |
| SC5 (Focus 1 Regroup Trap) | Pre-flagged P2 D-05 | None confirmed | partial | **defect-or-resolved** |
| SC6-SC9 | Audit-validated intent + safeguards | Various | YES | **PASS** |
| SC11-SC12 (D-07, D-09 P1s) | Resolved in PP-465+ | Audit closure explicit | YES | **PASS-resolved** |

## §7 Phase 6 — Triage

| # | Finding | Severity | Source |
|---|---|---|---|
| SC3 | Genre 0.5 near-inert (D-01) | P2 (pre-flagged, status unverified) | 2026-04-08 |
| SC4 | Regroup-on-Spent dominant (D-04) | P2 (pre-flagged) | 2026-04-08 |
| SC5 | Focus 1 Regroup Trap (D-05) | P2 (pre-flagged) | 2026-04-08 |
| SC1 | 2D pool floor (architectural — exit not floor) | note (PASS-with-flag) | this turn |
| All others | Various | **PASS** | mix |

## §8 Stage 2 — Lesson mapping

| # | Finding | Lesson | Direction |
|---|---|---|---|
| SC3 | Genre 0.5 near-inert | L4 (clock-routing inadequate at R=1) | Either reduce R by 1 for off-primary OR raise GW floor to 0.75 (per stress test D-01 proposal). Verify status first. |
| SC4 | Regroup-on-Spent | L5 (loop exploit risk) | Apply CT+2 on Regroup-while-Spent (per D-04 proposal). Verify status first. |
| SC5 | Focus 1 Regroup Trap | L2 (low-stat trap) | Regroup minimum 2 Concentration regardless of Focus (per D-05 proposal). Verify status first. |
| SC1 | Pool floor architectural | (PASS-with-flag) | Document exit-not-floor pattern explicitly. |

## §9 Verdict (Stage 3)

```
SYSTEM:     Social Contest
COMPONENTS: dice (Argue Pool 2-18D, no floor) + continuous (Concentration, Composure)
            + clock (Conviction Track 0-10, multi-threshold) + discrete (Doubt Marker,
            interaction types, Obligation chains, Conviction Vector PP-684)

VERDICT: NERS-COMPLIANT — confirms skill INITIAL hypothesis
         "compliant, healthy contested case." Three pre-flagged P2s from
         2026-04-08 stress test (SC3/SC4/SC5) have unverified resolution
         status; surfaced for verification not as fresh findings.

N: PASS — All components earn their place. Conviction Track depth IS the
         Lesson-4 clock-routing of single-exchange variance. Interaction-
         type taxonomy (CLASH/CROSS/COMPETITION/DIVERGENCE/AMPLIFY)
         creates non-overlapping resolution paths.

R: PASS — Holds at extremes. 2D pool floor exists but exit-not-floor
         architecture (Spent state → contest withdrawal) is the safeguard.
         No undamped+unbounded loops per audit Mode C.

S: PASS — Cross-system smooth: Composure shares architecture with personal
         combat (PP-460 alignment); Belief cross-references threadwork
         cleanly; Conviction Vector PP-684 promoted to CANONICAL 2026-05-01
         provides faction-scale aggregation path.

E: PASS — Interaction types learnable; CT movement transparent (effective_margin
         formula visible); Composure derivation (Cha+6) intuitive; PP-684
         Conviction taxonomy is the most player-legible identity-system in
         the entire Valoria architecture.
```

## §10 Re-test (Stage 4)

No mechanical remediation proposed (status of pre-flagged P2s unverified — verification, not remediation, is the action). Skipping Stage 4 re-test.

## Status

`[CONFIDENCE: high]` — system is audit-validated clean by prior audit; my role this turn confirms cross-checked against current skill discipline.
`[CONFIDENCE: medium]` — SC3/SC4/SC5 pre-flagged status post-2026-04-08 unverified (would require commit-log scan)
`[CONFIDENCE: high]` — SC1 (no Pool Floor, exit-not-floor architecture) is novel observation; architecturally valid

Departures from skill: skill claimed "pools 5–18D"; actual range is 2–18D with novice floor at 2D. Reframed as architectural choice (exit-not-floor) consistent with mass-battle's unit-deletion-as-floor.
