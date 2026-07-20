# PP-686 Simulation v2 Evaluation

**Subject:** PP-686 with structured-concentration NPCs + Self-Other orientation + 5 calibration deltas from v1
**Method:** 8 scenarios (7 from v1 + new scenario 8 testing Self-Other attribution)
**Implementation:** `pp686_sim_v2.py`
**Output:** `pp686_sim_v2_output.txt`
**Compares to:** v1 evaluation (`2026-04-30_PP-686_simulation_evaluation.md`)

---

## §0 Summary

Of 5 calibration deltas applied: **3 confirmed working, 1 partial-success, 1 ineffective.**
Of 2 architectural changes (structured NPCs, Self-Other axis): **both worked as intended**, with one new calibration consequence to flag.

| Delta | v1 Status | v2 Result |
|---|---|---|
| Ob ±2 cap | proposed | ✓ effective; public ceremony Ob now −2 (was −3) |
| drift_coef 0.3 → 0.45 | proposed | ✗ ineffective (smoother NPC vectors offset the increase) |
| β-fidelity gating on negative outcomes | proposed | ✓ effective; honest-defeat ΔPS now −1.79 (was −0.63, was over-cushioned) |
| strictness reward path for aligned actions | proposed | ✓ partial; reward saturates triadic sum, hits cap easily |
| orphan NPC rule (α = 1.0) | proposed | ✓ effective; orphans contribute correctly to aggregate |

| Architectural change | v2 Result |
|---|---|
| Structured-concentration NPCs (primary + cultural background) | ✓ aggregate vectors smoother and more interpretable; cascade fidelity reads more nuanced |
| Self-Other orientation as outcome modulator | ✓ scenario 8 shows public-spirited vs self-aggrandizing leaders produce distinguishable state evolution from same raw outcomes |

---

## §1 Scenario-by-Scenario Comparison

### §1.1 Scenario 1 — Static Parity

| | v1 | v2 |
|---|---|---|
| Aggregate effective | Virtue:0.36, Authority:0.29, Order:0.15, Utility:0.13 | Virtue:0.32, Authority:0.24, Order:0.13, Utility:0.10, Scholastic:0.07, Faith:0.03 |
| Cascade fidelity | 0.910 | 0.904 |
| Public ceremony Ob | **−3** | **−2** |
| Covert assassination Ob | +1 | +1 |
| Treaty signing Ob | −2 | −2 |

**Findings:**

- **±2 cap effective.** Public ceremony Ob dropped from −3 (v1) to −2 (v2) — the dominant-strategy concern is contained.
- **Strictness reward path is structurally suspicious.** Detail row for public ceremony:
  ```
  m=−1  c=−1  e=−0.96  | csim=0.90  esim=1.00  str=0.54
  ```
  e_align alone contributes −0.96 (nearly a full −1) because at strictness 0.54, the reward path scales the alignment by `0.5 + (1 − 0.54) = 0.96`. Combined with m=−1 and c=−1, raw total = −2.96 → capped to −2. The cap is doing work; without it Ob would be −3.
  
  **Implication:** the strictness reward path is *saturating against the cap*, not adding nuance. Recommend reducing the reward coefficient (0.5 + 0.5×(1−strictness)) or re-evaluating whether the strictness reward path is needed at all. The cap alone may be sufficient.
- **Aggregate vectors are smoother** with structured NPCs. v2 has 6 nonzero entries vs v1's 4. This is a feature, not a bug — it produces more interpretable aggregates that reflect background culture, not just primary Convictions.

### §1.2 Scenario 2 — Succession Dynamics

| | v1 (drift 0.3) | v2 (drift 0.45 + structured NPCs) |
|---|---|---|
| Cesare succession final fidelity | 0.571 (S6) | 0.631 (S8) |
| Lorenzo succession final fidelity | 0.785 (S6) | 0.786 (S8) |

**Finding:** v2 converges *slower* than expected despite higher drift_coef. The smoother NPC vectors (more nonzero entries) reduce the magnitude of change per cascade re-resolution. Net effect: succession effects span 8+ seasons.

**Recommendation:** drift_coef needs to go higher still — try 0.55-0.65 — *or* the cascade math needs to operate on top-N truncated vectors when computing intermediate values.

### §1.3 Scenario 3 — Conviction Crisis

| | v1 | v2 |
|---|---|---|
| Fidelity variance over 8 seasons | 0.0074 | **0.0051** (lower!) |

**Finding:** v2 is *less* responsive to crisis than v1, despite the higher drift_coef. Same root cause as §1.2: smoother NPC vectors damp aggregate response.

**This is a P1 calibration issue.** A leader in active Conviction crisis should produce visible faction instability. Currently it produces nearly nothing. Two options:

1. **Crisis-bypass rule:** when `leader.scars >= 3`, suspend cascade damping for that leader's tier; new leader Convictions propagate immediately each season.
2. **Drift-by-magnitude:** scale drift_coef by the *magnitude of change* in the leader's personal_convictions (high change → high drift this season).

Option 1 is simpler and matches dramatic intent.

### §1.4 Scenario 4 — Strictness Feedback Loop

| | v1 | v2 |
|---|---|---|
| Final L | 4.86 | 4.86 |
| Final PS | 7.00 (capped) | 7.00 (capped) |
| Strictness range | 0.44–0.54 | 0.44–0.54 |

**Finding:** No change. PS still pegs ceiling. The β-fidelity gating only kicks in on negative outcomes; in this mixed sequence, positive outcomes still let β contribute fully.

**Implication:** scenario 4 isn't actually testing the calibration. Need a sequence with persistent failures to see β-gating distinguish v1 from v2. (Scenario 5 does this; see below.)

### §1.5 Scenario 5 — Honest Defeat

| | v1 | v2 |
|---|---|---|
| ΔL over 8 seasons | +0.76 | +0.76 |
| ΔPS over 8 seasons | **−0.63** | **−1.79** |

**Finding:** β-gating works as intended. v1 over-cushioned PS during persistent failure (β-fid contribution kept adding positive PS even as outcomes were negative). v2 cuts that contribution in half during negative seasons; PS now bleeds at the realistic rate.

The dignified-fallen-king signature is still preserved — Legitimacy grows while Popular Support erodes — but the magnitudes now feel right. ΔPS −1.79 over 8 seasons is meaningful drift; ΔPS −0.63 was barely-noticeable.

### §1.6 Scenario 6 — Successful Tyrant

| | v1 | v2 |
|---|---|---|
| L–PS divergence | 2.83 | 2.79 |

**Finding:** Essentially unchanged. Calibrations didn't disturb this dramatic pattern; the strong-but-fragile signature is robust to the parameter changes.

### §1.7 Scenario 7 — Edge Cases (Orphan)

| | v1 | v2 |
|---|---|---|
| Orphan effective_convictions | zero (silent bug) | **populated** (Liberty:0.60, Utility:0.19, ...) |
| Aggregate includes orphan? | Yes but as zero contribution (deflates magnitude) | Yes correctly |

**Finding:** Orphan rule fix works. P2-4 from audit resolved.

### §1.8 Scenario 8 — Self-Other Attribution (NEW)

Two leaders, identical Mission victories, different self_other_orientation:

| Leader | Orientation | Attributed outcome | Final L | Final PS | Final fid |
|---|---|---|---|---|---|
| Almud | +0.1 | 0.95 (full credit) | 5.38 | 7.00 | 0.904 |
| Cesare | +0.8 | 0.60 (40% loss to self-attribution) | 5.09 | 6.75 | 0.626 |

**Finding:** Self-Other axis successfully separates two leaders who would have looked identical under raw mission_outcome. Cesare's high orientation produces:

1. **Lower attribution:** 0.60 of each Mission win lands as Popular Support gain (40% is "for himself" not "for the populace").
2. **Lower fidelity:** Cesare's Convictions (Authority + Utility) match sovereign role less well than Almud's (Virtue + Authority).
3. **Compound effect:** Cesare's L bleeds slower (less violation cost in this scenario), but PS climbs slower too. Net divergence is preserved.

The architectural addition works without disturbing other dynamics. **Self-Other axis is ratifiable.**

**Refinement:** the formula `attributed = raw × (1 − 0.5 × max(0, orient))` is provisional. Future calibration could explore (a) full bidirectional scaling (negative orientation = altruism gives bonus), (b) non-linear scaling (e.g., orientation^2), (c) dependence on context (orient matters for Mission attribution but not for L drift).

---

## §2 New Findings from v2

### §2.1 Smoother NPC vectors offset cascade dynamics

**The core finding.** Structured-concentration NPCs produce smoother aggregate vectors, which reduces sensitivity of cascade math. Two consequences:

- **Succession effects slower than v1** despite higher drift_coef.
- **Crisis less visible than v1** — variance dropped, not increased.

This is the trade for the architectural improvement. Smoother vectors are *desirable* for cascade nuance and player legibility but *undesirable* for visible succession/crisis dynamics. Resolution: more aggressive drift_coef (0.55-0.65) or crisis-bypass rule.

### §2.2 Strictness reward path saturates the cap

The strictness reward path makes the e_align contribution scale up to ~1.0 at low strictness. With m_align and c_align also at full ±1, the triadic sum easily exceeds the ±2 cap. The cap is doing the work; the reward path is moot.

**Recommendation:** drop the strictness reward path. Use only strictness-as-penalty-modulator (the original §3.6 design). The cap alone provides sufficient response variation.

### §2.3 Self-Other modulator composes cleanly

Scenario 8 shows the axis adds discrimination without disrupting other dynamics. This is the cleanest of the v2 changes — pure architectural addition, no negative interactions surfaced.

---

## §3 Calibration Recommendations for PP-686 v3 spec

| # | Change | Source | Confidence |
|---|---|---|---|
| C1 | Cap Ob_modifier at ±2 | v1 | confirmed v2 |
| C2 | Drop strictness reward path | v2 | new |
| C3 | drift_coef = 0.55-0.65 (was proposed 0.45) | v2 | needs further sim |
| C4 | Add crisis-bypass rule: leader.scars ≥ 3 → cascade damping suspended | v1 | confirmed v2 (problem persists) |
| C5 | β-fidelity gating during negative outcomes (×0.5) | v1 | confirmed v2 |
| C6 | Orphan NPC rule: α = 1.0, contribute normally | v1 | confirmed v2 |
| C7 | Self-Other orientation: provisional formula `attributed = raw × (1 − 0.5 × max(0, orient))`, calibrate further at Stage 10 | v2 | provisional |
| C8 | NPC personal_convictions = primary (1-3, 0.6-0.8 weight) + cultural background (0.2-0.4 weight) | from prior conversation | confirmed v2 |
| C9 | Codify aggregate as Standing-weighted normalized sum | v1 | confirmed v2 |
| C10 | Cultural background templates as separate canonical authoring layer | v2 | new |

These C1–C10 are the calibration delta set for inclusion in PP-686 v3 specification.

---

## §4 NERS Re-Evaluation Post-v2

| Direction | v1 post-sim | v2 post-sim |
|---|---|---|
| Top-down N | STRONG | STRONG |
| Top-down R | MODERATE | **STRONG** (Self-Other adds robustness in customization axis) |
| Top-down S | WEAK | WEAK (cross-system specs still unaddressed) |
| Top-down E | MODERATE (Ob saturation) | **MODERATE** (Ob cap works but reward-path saturates; net same) |
| Bottom-up N | STRONG | STRONG |
| Bottom-up R | STRONG | STRONG |
| Bottom-up S | MODERATE | MODERATE |
| Bottom-up E | STRONG | STRONG |
| Vertical N | STRONG | STRONG |
| Vertical R | STRONG | STRONG |
| Vertical S | MODERATE | MODERATE |
| Vertical E | MODERATE | MODERATE |
| Diagonal N | STRONG | **STRONG** (Self-Other adds new diagonal dimension: leader-orientation → faction-attribution) |
| Diagonal R | MODERATE | MODERATE |
| Diagonal S | WEAK | WEAK |
| Diagonal E | MODERATE | MODERATE |
| Lateral | unchanged | unchanged (untested) |
| Horizontal R | STRONG | STRONG |
| Horizontal S | MODERATE | MODERATE |
| Horizontal E | MIXED | MIXED |

**Net:** v2 strengthens Top-down R and Diagonal N (Self-Other axis). Other directions unchanged.

The remaining weak directions (lateral, diagonal smoothness) are exactly what PP-687 (universal Key substrate) is designed to address.

---

## §5 Verdict

The v2 simulation **confirms the architectural soundness** of PP-686 with structured-concentration NPCs and Self-Other orientation. The calibration set (C1–C10) provides a ratifiable parameter package.

**Two refinements remain for PP-686 v3 spec finalization:**

1. **Crisis-bypass rule** (C4) — concrete, well-scoped.
2. **drift_coef calibration** (C3) — needs one more sim run with drift = 0.6 to confirm succession reaches equilibrium within 4-5 seasons (player-perceivable timescale).

Both can be batched into the PP-686 spec revision after PP-687 ratifies. PP-687 will likely simplify the cascade math anyway by giving Keys as the substrate for cross-system event propagation.

**The session moves on to PP-687 drafting.**

---

**End v2 evaluation.**
