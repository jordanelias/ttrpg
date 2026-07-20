# Domain Action Resolver — Deterministic+Stochastic (Tested Candidate)

**Date:** 2026-05-29
**Develops:** the faction bare-stat cluster — ED-865/F1 (floor degeneracy), ED-874 (σ-leverage non-uniformity), and the punching-up wall — via the direction Jordan selected (deterministic+stochastic).
**Sim:** `sim_domain_resolver.py` (this folder), 200k-trial MC, authoritative die rule for the comparison baseline.
**Owner contract:** this is a **tuned, Stage-4-tested candidate.** The decision to adopt — and the final parameter values — are Jordan's. PROPOSED parameters are flagged throughout.
**Bias:** `[SELF-AUTHORED — bias risk]`. §6 surfaces the candidate's costs and the assumptions it rests on.
**Scope discipline:** this resolver is proposed for **bare-stat faction Domain Actions only.** Healthy dice systems (personal combat, social contest, aggregated mass battle) are explicitly **out of scope** — replacing them would be over-correction (NERS-N/E).

---

## §0 — The concept: deterministic odds, stochastic resolution

The bare faction dice pool fails twice at once: at small N it gives neither **legible odds** (the player cannot read their chance off the board) nor **uniform leverage** (a stat point is worth a different amount at every stat level, via 1/√N). The fix is not to remove chance — a deterministic *outcome* would be exploitable and dull — but to **make the odds deterministic and legible while keeping the outcome stochastic**:

> **P(success) is a clean function of the stat contest the player can read and predict; the outcome is still drawn against it.**

This is the CK3/EU/KoDP idiom for strategic-scale resolution, and it matches the faction layer's own deterministic-accounting spine (the layer's original NERS-S failure was *dice resolution sitting on a deterministic ledger* — this removes that inconsistency).

---

## §1 — The resolver (PROPOSED, tuned)

**Contest margin** `M = acting_stat − difficulty`, where *difficulty* is the contested target's relevant stat (contested actions) or a fixed action-difficulty rating (non-contested actions). The existing `Ob = floor(stat/2)+1` maps to a difficulty (see §4).

**Probabilities** (clamped):

```
P_success(M)       = clamp(BASE + SLOPE·M, FLOOR, CAP)            # at-least-Success
P_overwhelming(M)  = clamp(BASE + SLOPE·M − OVW_OFFSET, 0, OVW_CAP)
P_atleast_partial  = clamp(BASE + SLOPE·M + PARTIAL_BAND, P_success, FAIL_FLOOR)
```

**Resolution** — draw `r ~ U[0,1)` (lower is better), band it:

| `r` falls in | Degree |
|---|---|
| `r < P_overwhelming` | Overwhelming |
| `P_overwhelming ≤ r < P_success` | Success |
| `P_success ≤ r < P_atleast_partial` | Partial |
| `r ≥ P_atleast_partial` | Failure |

**Tuned parameters** (PROPOSED — clean round values, all ledger-cited):

| Param | Value | Meaning |
|---|---|---|
| BASE | 0.50 | even contest (M=0) is a fair coin-tilt, not a degenerate pool |
| SLOPE | 0.10 | **leverage: +10% per stat point of margin — CONSTANT** |
| FLOOR | 0.05 | punching-up floor: hard but never impossible |
| CAP | 0.90 | overmatch cap: reliable but never certain |
| OVW_OFFSET | 0.35 | Overwhelming requires being this far into the success zone |
| OVW_CAP | 0.55 | even a dominant actor never auto-overwhelms |
| PARTIAL_BAND | 0.20 | width of the Partial band below Success |
| FAIL_FLOOR | 0.97 | ≥3% residual failure even at max overmatch (nothing is automatic) |

**The headline number a player sees is P_success, and it moves by exactly SLOPE (10%) per point of contest margin** — the uniform, legible leverage the dice pool could not provide.

---

## §2 — Matchup matrix (P(success), acting × target)

```
       tgt:    1     2     3     4     5     6     7
  act 1:     0.50  0.40  0.30  0.20  0.10  0.05  0.05
  act 2:     0.60  0.50  0.40  0.30  0.20  0.10  0.05
  act 3:     0.70  0.60  0.50  0.40  0.30  0.20  0.10
  act 4:     0.80  0.70  0.60  0.50  0.40  0.30  0.20
  act 5:     0.90  0.80  0.70  0.60  0.50  0.40  0.30
  act 6:     0.90  0.90  0.80  0.70  0.60  0.50  0.40
  act 7:     0.90  0.90  0.90  0.80  0.70  0.60  0.50
```

Symmetric, legible, bounded. The diagonal (even contest) is 0.50; each step of advantage adds a flat 0.10; corners clamp at 0.05 / 0.90. The live leverage zone is `M ∈ [−4, +4]`, which covers essentially every realistic faction matchup (stat gaps of 0–4).

---

## §3 — The three pathologies, fixed (vs current dice)

| Pathology | Current bare dice | **Determ+stoch** | Verdict |
|---|---|---|---|
| Floor degeneracy (weak stat 2 vs Ob 3) | **0.069** | **0.300** | fixed — playable, not degenerate |
| Punching-up wall (stat 2 vs strong 7, Ob 4) | **0.010** | **0.050** | fixed — hard but a real underdog chance, no brick wall |
| Even peer (stat 3 vs 3, Ob 2) | 0.399 | 0.500 | fair contest |
| Dominant / ceiling (stat 7 vs weak 2) | 0.727 | 0.900 (capped) | reliable, never automatic (3% residual fail) |
| σ-leverage uniformity (ED-874) | non-uniform (1/√N: 0.354/pt @ stat2 → 0.189/pt @ stat7) | **flat 0.10/pt** | **fixed by construction** |

The σ-leverage row is the one the Stage-4 aggregation sweep proved *cannot* be fixed by pool transformation — only a deterministic+stochastic resolver makes leverage constant. This candidate delivers that.

---

## §4 — Domain Echo interface (drop-in: OUTPUT unchanged)

The resolver produces the **same four-degree ladder** (Failure / Partial / Success / Overwhelming) the dice system produced, so everything downstream is unchanged:

- **Domain Echo** (`scale_transitions_v30 §5`): Success → +1, Overwhelming → +2 to the faction stat, cap ±2. The resolver's degree output feeds this directly — no change to Domain Echo.
- **Degree distribution shifts smoothly with margin** (200k MC):

  | Contest | OVW | SUC | PAR | FAIL |
  |---|---|---|---|---|
  | even (M=0) | 0.15 | 0.35 | 0.20 | 0.30 |
  | advantage (M=+2) | 0.35 | 0.35 | 0.20 | 0.10 |
  | underdog (M=−3) | 0.00 | 0.20 | 0.20 | 0.60 |
  | dominant (M=+5) | 0.55 | 0.35 | 0.07 | 0.03 |

- **Ob → difficulty mapping:** existing `Ob = floor(D/2)+1` inverts to a representative difficulty `D = max(1, (Ob−1)·2)`. So Assert's "Ob 2" → difficulty 2–3; a contested action keeps the target's actual stat as difficulty. The spec recommends migrating contested actions to the **direct stat contest** (`M = acting − target`) and fixed-Ob actions to a **fixed difficulty** read off the current Ob — both are one-line conversions.

**Only the resolution METHOD changes; the degree OUTPUT and every consumer of it (Domain Echo, cost tables, CI formula) are untouched.** This is what makes it a contained change rather than a faction-layer rewrite.

---

## §5 — Interface elsewhere at faction level (where bare stats are most exposed)

The same resolver generalizes to every bare-stat faction check. This is a **NERS-S consistency win**: all faction-scale stat resolution would use one legible form, instead of a patchwork of bare-pool-vs-Ob rolls each degenerate at small N. Inventory of the exposed checks and the recommendation for each:

| Faction check | Current | Exposure | Recommendation |
|---|---|---|---|
| **Domain Actions** (Assert: Influence vs Ob 2; Reconstitute: Influence Ob 4; Govern; Claim Masterless) | bare stat vs `floor(stat/2)+1` | **High** — pivotal, often low stat | **Migrate** — primary target of this spec |
| **Suppress** (Mandate vs `floor(Church-L/2)+1`; Failure → Stab −1) | bare Mandate pool | **High** — the one PP-403 Stability-cost exception, so failure is load-bearing | **Migrate**, preserving the Suppress-failure → Stab −1 hook on the resolver's Failure degree |
| **Parliamentary Rebuttal** (vs Censure/Outlawry; Overwhelming → +1 effect) | bare stat pool | **Medium** — graded (Overwhelming matters), so degrees must be preserved | **Migrate** — the resolver's graded degrees map directly; Rebuttal Overwhelming still triggers its +1 |
| **§1.4 Accounting Stability Check** (Stability pool vs `Ob = magnitude of attribute loss`) | bare Stability vs loss-magnitude | **High** — fires during cascades, exactly when Stability is already low (small pool) | **Migrate** with care — model as `M = Stability − loss_magnitude`; this makes *recovery/See-it-coming* legible too, and removes the small-pool degeneracy at the worst moment. **Interacts with the §1.3 recovery mechanic (CC-4)** — co-design the two. |
| **Mass-battle resolution** (Trigger-5 source) | aggregated dice pool `min(Size,Cmd)+Cmd` | n/a | **Keep dice** — pool is aggregated/healthy; ED-876 already fixed its cliff. **Orthogonal to this resolver.** |
| Personal combat, social contest | dice pools 5–18D | n/a | **Keep dice** — healthy; out of scope (NERS-N/E) |

**Migration consistency note.** If all four bare-stat faction checks (Domain Actions, Suppress, Rebuttal, Accounting Stability Check) move to the one resolver, the faction layer gains a single, uniform, legible resolution rule for every stat contest — a direct NERS-S improvement and the strongest argument for doing the migration as a set rather than piecemeal. The named hooks on specific outcomes (Suppress-failure → Stab −1; Rebuttal-Overwhelming → +1) attach cleanly to the corresponding degree and are preserved.

**Sequencing caveat (CC-4 dependency).** The §1.4 Accounting Stability Check shares the stage with the §1.3 Institutional Consolidation recovery (the deterministic clean-season +1 found in CC-4). Migrating §1.4 to the resolver should be **co-designed with the recovery mechanic** so the damage-check and the recovery don't double-count or fight — recommend doing the Domain-Action migration first (clean, isolated) and the §1.4 migration in a second pass alongside a recovery review.

---

## §6 — Stage-4 self-critique, limits, and what stays Jordan's

**Stage-4 new-defect checks (all PASS):** no auto-success (3% residual failure at max overmatch); underdog viable (5% floor); P(success) monotonic in margin (no cliffs); degree bands well-ordered (`pov ≤ ps ≤ pap`) for all M. The fix introduces none of the defects its predecessors did.

**What is robust:** the structural result — deterministic+stochastic gives constant leverage and bounded, legible odds, fixing all three pathologies including the one aggregation provably cannot. `[CONFIDENCE: high]`.

**What is Jordan's (PROPOSED, not settled):**
- **The parameter values.** BASE 0.50 / SLOPE 0.10 / FLOOR 0.05 / CAP 0.90 and the band offsets are tuned *illustrations* chosen for clean legibility, not calibrated against a measured target faction win-rate curve or playtest. A designer may want, e.g., BASE 0.45 (defender's edge), or a steeper SLOPE 0.12 (stats matter more, narrower live zone), or a lower CAP 0.85. The *form* is the proposal; the *numbers* are a starting point.
- **Whether even-contest should be 0.50.** A 50% coin-tilt at parity is fair but some designers prefer initiative or defender bias. Trivially tuned via BASE.
- **Whether to migrate the full set or just Domain Actions.** §5 argues for the set (consistency); the minimal change is Domain Actions alone.
- **The §1.4 co-design with recovery (CC-4)** — flagged, not resolved here.

**Limits:** no weighted-event outcome tables modeled (the resolver gives degrees; a richer "which specific consequence on Success" table could layer on top — optional enrichment, out of scope). Multi-faction interaction and the Domain-Echo-feedback loop under the new resolver are unsimulated (the degree distribution is compatible, but the closed-loop dynamics over a campaign were not run).

---

## §7 — Ledger impact (consolidated master)

- **ED-865/F1 + ED-874:** add this tested candidate. Floor degeneracy and σ-leverage both fixed; the latter only achievable this way (per the Stage-4 aggregation proof). Status: **candidate ready for Jordan's adopt/tune decision** — not applied to canon (this is a spec, not a canon edit).
- Recommends a **two-phase migration**: (1) Domain Actions (clean, isolated); (2) Suppress + Rebuttal + §1.4 Accounting Stability Check as a consistency set, with §1.4 co-designed against the §1.3 recovery mechanic (CC-4).
- Orthogonal to ED-876 (applied) — Trigger-5/mass-battle is dice and out of scope.
- Not appended to the live ledger (JSONL migration owns it); recorded in `ledger_candidates_consolidated.json`.

`[CONFIDENCE: high]` — the resolver form, the pathology fixes, and the Stage-4 passes. `[CONFIDENCE: medium]` — the specific parameter values and whether to migrate the full set, both Jordan's calls.
