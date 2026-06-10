# Resolution Diagnostic — Fieldwork (Exploration / Investigation / Socializing)

**Date:** 2026-06-10 · **Session:** audit | ef659454b0c8 · **Skill:** valoria-resolution-diagnostic (Stages 0–2; Stage 3/4 in `ners_verdict_fieldwork.md`)
**Supersedes:** `resolution_diagnostic_investigation.md` (2026-05-28, index-depth) per its own supersession clause. `[SELF-AUTHORED — bias risk]` on that prior verdict; treated as external and re-derived from full reads.

## Stage 0 — Calibration

Run against the adjudicated rows before trusting this session's verdicts: pre-resolver faction = NON-COMPLIANT ✓ (reproduced); post-resolver faction = compliant ✓; continuous engine below 5D without `Ob − 0.5` = finding ✓ (applied here to wound-floored fieldwork pools — same rule, new site); eff_Ob < 1 = finding ✓ (fieldwork's Disposition reductions and Inspiration spend both carry explicit min-1 floors — checked, no violation); MB cliff row not exercised (out of scope). **No verdict flips; no canon-ratified pattern flagged as defect. Calibrated.**

## Phase 0 — Scope gate, decompose, assign engine

Rolling engine present. Decomposition (recognize-and-exclude per Scope Gate):

| Component | Mechanism | Class | Engine |
|---|---|---|---|
| Fieldwork Pool (Explore/Investigate/Social actions) | (Attr×2)+Hist, 5–24D, TN 6/7/8, Ob 1–8+mods (fieldwork_v30 §1–§5; params/fieldwork §Pool) | rolling | **A** (healthy pool, genuine setup axis: Depth prep, Disposition, Inspiration, allies) |
| Thread-Read | (Spirit×2)+Hist+TPS (§4.5 PP-619/PP-626) | rolling | **A** |
| Knot formation | Spirit×2, TN 7, Ob 2 (§5.6a) — 2–14D, no History term | rolling | **A at Spirit ≥3; sub-5D at Spirit 1–2** → Decision-Rule tension (see RD-3) |
| Sincerity Gate | bare Spirit, TN 7, Ob 1 (§5.3) — 1–7D | rolling | bare-stat; stakes low (Disposition −1 max) |
| Concealment / Contested-investigation pools | Cog×2 (+Hist for concealer) (§6.4, §4.6) | rolling | A |
| Assistants | own pool at Ob+1; Success → +1 net to leader (§3.2) | rolling | A (rider) |
| Evidence Track 3/5/8 | deep multi-threshold accumulator (§4.1) | non-rolling | excluded (clock) |
| Five-Filter Chain / Lattice / Scene-Graph / NPE | deterministic pipeline / state machine / graph (investigation_systems §1–§4) | non-rolling | excluded → mechanic-audit (00_MASTER) |
| Cover / Exposure / Disposition | continuous resources & tracks feeding rolls | non-rolling | roll inputs, excluded |

Raw-d10 leak check: resolution text is engine-agnostic (degree table per params/core); **one presentation leak** — §10.5 specifies per-face d10 UI in Godot mode (RD-5).

## Stage 1 findings (Phases 1–6) + Stage 2 lesson mapping

| Finding | Component | Engine | Property | Stress point | Outcome@stress | Impact | Exposure | Irreversibility | Intent | Phase | Severity | Lesson(s) | Remediation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **RD-S1** Roll inputs canonically indeterminate: Thread-Read attribute Spirit (master §2.1/§4.5) vs Attunement (params/fieldwork, split §4.2); effective Ob stepped (master §5.1) vs max(1, base−Disp) (params PP-632) | all social/investigation rolls | A | P-i/P-iii (odds unreadable; response rule ambiguous) | any roll with Disposition ≠ 0 or Thread-Read | two different pools / two different Obs for the same action | H | H (routine) | M | accidental (propagation failure) | 0/3b | **P1** | L3 (one engine, one spec) | adopt master line; regenerate params; Jordan picks stepped-vs-subtraction (00_MASTER P1-1/P1-2) |
| **RD-1** ER-2 continuity term unlanded while pools reach 1–4D (wound-penalised pools named at params/core §Pool Floor; −1D/wound §2.2; bare-Spirit gates) | continuous resolution of small pools | A | P-iii/P-i | wounded Endurance-explore/Surveil; Spirit 1–3 gates | odds 4–32% low vs discrete (engine_replacement §2: 1D/Ob2 4.43×, 2D/Ob3 2.71×); TTRPG↔videogame divergence | M | M (wounds routine in fieldwork arcs) | L (retryable) | accidental (fix recommended, not landed) | 3c | **P2** | L6 | land `net − (Ob − 0.5)` in params/core §Continuous Engine |
| **RD-2** Continuous-engine behavior never validated at fieldwork parameters (ED-836 "by construction"; SIM-DEBT-FW-* validated discrete pre-Decision-E; sim stubs) | Fieldwork Pool 5–24D, TN 6/7/8, Ob 1–8 | A | P-ii (unverified) | full range | unknown — claim untested | M | H (all fieldwork) | L | accidental (documented gap) | 3a | **P2** | L2 (verification obligation) | run the per-system sweep against params/fieldwork values; fill sim stubs |
| **RD-3** Pool-construction deviation on pivotal sub-5D rolls: Knot formation Spirit×2 no-History (2–4D at Spirit 1–2, 4-season cooldown on Failure); Sincerity bare Spirit | Knot formation; Sincerity Gate | A (sub-5D edge) | P-iv/P-v | Spirit 1–2 actor at Disposition +5 | Knot: P(net≥2) small + 4-season lockout; Sincerity: low stakes | M (Knot) / L (Sincerity) | M (low-Spirit builds legitimate) | M (seasons, recoverable) | **[INTENT UNDETERMINED]** (Spirit choice explicit ED-503; bare/no-Hist construction not) | 1/2c | **P2** | L3 candidate | Jordan: ratify deviation or normalize to (Attr×2)+Hist; if kept sub-5D, RD-1's correction is load-bearing here |
| **RD-4** Flat Ob modifiers (hostile/foreign ±1, Disposition, Inspiration −1, MS band, Concealment Ob) give non-uniform per-point dP across 5–24D (1/√N); no leverage layer specified for fieldwork (combat-armature Δσ layer scoped to combat) | Ob-modifier stack | A | P-ii | 5D vs 24D actors | same modifier moves P by very different amounts | M | H (modifiers routine) | L (clock increments, Fail-Forward) | pre-leverage-layer design; **[INTENT UNDETERMINED]** whether fieldwork receives the σ-leverage layer | 3a | **P3** (stakes recoverable; P2 only at pivotal rolls, which are RD-3's) | L2 | decide leverage-layer scope for fieldwork when combat armature lands |
| **RD-5** §10.5 d10 dice-face visualisation (skull/pip/check/chain per face) in Godot mode vs Decision-E continuous magnitude gauge | presentation layer | A | P-i | every videogame roll | UI displays a mechanic the engine doesn't run | M | H | L | accidental (doc predates Decision E) | 0 | **P2** | L3 (presentation leak) | rewrite §10.5 as magnitude-gauge presentation |
| **RD-6** Exposure loop (fail→+Exp→Noticed +1 Ob→harder) | Exposure ↔ roll Ob | A (loop through roll output) | P-iii/P-iv | Desperate Trail + hostile territory | escalating Ob | M | M | L (Compromised recoverable; resets exist) | **deliberate with adequate safeguards** (clears on Success/season; reduction tools; AP caps PP-581 ~11%) | 4/5 | **intent-gated PASS** | L5 satisfied | none |
| **RD-7** Reconstruct Failure → false conclusion, GM-concealed (§4.1) | Reconstruct | A | P-iv | threshold-met synthesis | player acts on wrong conclusion | M | M | M (reopenable) | **deliberate, design-explicit** ("GM does not reveal the error"; reopen path stated) | 5 | **intent-gated PASS** | — | none |

Phase 6 triage: RD-S1 ≫ RD-1 ≈ RD-2 ≈ RD-5 > RD-3 > RD-4. RD-6/RD-7 close as intent-gated passes (recorded per honest_findings — attacked, survived).

**Architecture re-confirmation:** INV1–INV9 (2026-05-28) re-derived at full depth and **stand** — the Five-Filter Chain owns decisions, dice feed the Evidence clock (Lesson 4 done well), Evidence/Cover/Exposure are exempt multi-threshold/continuous structures. The reversal in Stage 3 comes from the spec layer (RD-S1) and the engine-fidelity layer (RD-1/RD-2), not from the architecture.

`[CONFIDENCE: high]` RD-S1/RD-5 (textual); `[CONFIDENCE: medium]` RD-2 impact (unvalidated ≠ wrong), RD-3/RD-4 severity (intent undetermined).
