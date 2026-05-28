# Matchup-Table Derivation Analysis — Piece 1

**Question (from F6 remediation):** Can combat_v31's three matchup tables (Stance Counter, Reaction-aspect, Aspect coherence) be **derived from a few interpretable per-element primitives**, reducing the player's cognitive surface without losing matchup texture?

**Method:** falsifiable numerical test. Each table fit by candidate low-dimensional models; reproduction measured against **fractional-Ob granularity (±0.5)** — the system's own resolution. A derivation "succeeds" only if (a) it reproduces cells within ±0.5 AND (b) the recovered primitives are *physically interpretable* (a player can reason about them). Abstract coordinates that fit numerically but mean nothing do NOT reduce cognitive load and count as failure for the F6 purpose.

**Headline result:** the recommendation holds for **1 of 3 tables cleanly, 1 partially, 1 not at all.** My prior medium-confidence prediction that Stance Counter would reduce to ~3 primitives is **falsified.** No-bias note: I predicted reducibility; the data refused for the hardest case, and I report that.

---

## Result summary

| Table | Best interpretable model | Cells within ±0.5 | Verdict | F6 action |
|---|---|---|---|---|
| **Reaction-aspect** (5×4) | 2 params/reaction: baseline + depth-slope | **18/20** (rank-2: 20/20) | **DERIVABLE** | Replace table with 2 interpretable params/reaction |
| **Aspect coherence** (9 aspects, 36 pairs) | rank-2 embedding (2 props/aspect) | **31/36 (86%)**; rank-3: 33/36 (92%) | **PARTIAL** | Embedding (clusters) + hand-list 3–5 exceptions |
| **Stance Counter** (5×5) | circular "matchup wheel" (angle/stance) | **19/25** (abstract 3-prim: 23/25) | **NOT DERIVABLE (interpretably)** | Keep authored table OR redesign to wheel |

---

## 1A — Stance Counter: NOT cleanly derivable

**Structure (Hodge/Helmholtz decomposition of the antisymmetric matrix):**
- **84.6% cyclic** (rock-paper-scissors), only **15.4% transitive** (rankable dominance).
- The cyclic part is 93.6% rank-2 (one dominant cycle) but has a non-trivial second cycle (the 0.836 eigenpair).

**Interpretation:** stance matchups are *fundamentally non-transitive* — there is no "best stance," which is good design (Lesson 3 / NERS-R: no dominant option). But it means a scalar dominance ranking captures only 15% of the matrix.

**Fit results:**
- **Interpretable circular model** (each stance = an angle θ on a "matchup wheel"; `Counter ≈ R·sin(θ_def − θ_agg)`; 6 params total): **19/25 within ±0.5, max error 0.94, RMS 0.42.** The wheel places stances at Centered 0°, Raised 26°, Forward-point 142°, Low 166°, Side 210° — a plausible ordering, but it loses 6 cells.
- **Abstract 3-primitive** (1 scalar potential + 2D Hodge embedding): 23/25 within ±0.5, max 0.567 — better numerically, but the 2D coordinates are not physically interpretable, so they do **not** reduce player cognitive load. Fails criterion (b).

**Root cause (diagnosed precisely):** the matrix contains **two hard counters (±2) that both involve Forward-point** — "Centered vs Forward-point = +2" (Forward-point punishes Centered) and "Side vs Forward-point = −2" (Side answers Forward-point). No smooth low-dimensional model can place two hard counters on the *same* stance without distorting that stance's other matchups — which is exactly why every large residual in the wheel model involves Forward-point (0.94, 0.70, 0.56).

**Conclusion:** these hard counters are **design content, not noise.** Deriving the table from primitives would *flatten* the specific designed asymmetries that give the stance system its tactical identity. The F6 "derive from primitives" move is the wrong tool here.

**Revised F6 options for Stance Counter:**
- **(a) Keep the authored 5×5 (recommended).** It is only 10 free numbers (upper triangle). Players learn matchup charts in fighting games routinely; this is a learnable artifact, not unmanageable overhead. The F6 complexity concern is better addressed for this table by **state-gating** (Lever B — Stance Counter only applies at Commit/opening, not every sub-action) than by derivation.
- **(b) Redesign stances onto a true matchup wheel** *if* cognitive load is the overriding priority — accept that ~6 matchup values change (e.g., Forward-point can have at most one hard counter). This trades designed texture for learnability. A design-judgment call for Jordan, not a free win.

---

## 1B — Reaction-aspect: cleanly DERIVABLE (the win)

**Model:** each reaction has **2 interpretable parameters** — a **baseline** (effectiveness vs tentative attacks) and a **depth-slope** (how effectiveness changes as attacker commitment deepens). `Ob_mod(reaction, depth) = baseline + slope × depth_index`.

**Fit:** 18/20 cells within ±0.5 (max error 0.50); rank-2 SVD captures 20/20 at 97% variance. Voiding is *exactly* linear (+2,+1,0,−1).

**Recovered parameters are physically meaningful:**

| Reaction | baseline | depth-slope | physical reading |
|---|---|---|---|
| Voiding | +2.0 | −1.0 | evasion: dominates probes, insufficient vs full commitment |
| Pressing | +1.3 | −0.7 | counter-pressure: beats tentative, neutral vs deep |
| Hand-led | +0.8 | −0.7 | weapon parry: beats light, fails vs committed force |
| Body-led | −0.1 | +0.4 | whole-body: improves vs deep commitment |
| Yielding | −0.5 | +1.0 | redirect: turns overcommitment against the attacker |

**Player mental model:** "each reaction has an effectiveness level and a stance toward commitment — some reactions punish hesitation (negative slope: Voiding, Pressing, Hand-led), some punish overcommitment (positive slope: Body-led, Yielding)." That is **one sentence per reaction**, replacing 4 memorized cells with 2 meaningful dials. **F6 validated for this table.**

**Revision action:** replace the §7.2 table with the 2-parameter formulation; the table becomes the *display* of a derived rule. The 2 cells that miss by exactly 0.5 (Hand-led vs Deep; Yielding vs Probe) round correctly and are within tolerance.

---

## 1C — Aspect coherence: PARTIALLY derivable

**Distribution:** 16 Synergistic, 18 Neutral, 2 Antagonistic (of 36). Baseline (predict all-Neutral) = 50%.

**Embedding fit (verdict = sign of bilinear form with a neutral band):**
- rank-2 (2 props/aspect): **31/36 (86%)**
- rank-3 (3 props/aspect): 33/36 (92%)
- rank-4 (4 props/aspect): 35/36 (97%)

**Interpretation:** a 2–3 dimensional aspect embedding captures the gross Synergistic/Neutral structure — aspects cluster into compatibility groups, and same-group pairs synergize. But the **2 rare Antagonistic pairs** (Anticipation×Reaction, Commitment×Disengage) are outliers a smooth embedding struggles to produce; they're the residual.

**Conclusion:** **hybrid is the right model.** Derive the bulk (Synergistic/Neutral) from a small aspect embedding — i.e., assign each aspect a position in a 2–3D "compatibility space," same-cluster = synergistic — and **hand-specify the 2–5 exceptions** (the rare antagonisms) as named special cases. This reduces the 36-cell table to "9 aspect positions + a short exception list," which is a meaningful cognitive reduction (cluster reasoning + a couple of "these two fight" rules). **F6 partially validated.**

**Revision action:** present coherence as 2–3 aspect clusters (synergy within cluster) + an explicit short list of cross-cluster antagonisms. The full 36-pair table remains as generated reference, but the *player-facing* model is clusters + exceptions.

---

## What Piece 1 changes about the F6 remediation

The original F6 remediation said "derive matchup tables from primitives." Evidence revises this to a **per-table** prescription:

| Table | Revised prescription |
|---|---|
| Reaction-aspect | **Derive** — 2 interpretable params/reaction. Clean win. |
| Aspect coherence | **Hybrid** — cluster embedding + short exception list. |
| Stance Counter | **Do NOT derive** — keep authored (10 numbers, learnable) and reduce its load via **state-gating** instead. Optionally redesign to a wheel if learnability is paramount (design call; costs ~6 matchup values). |

**Cross-cutting insight:** "derive from primitives" is not a universal elegance move — it works when a table's structure is smooth/transitive or low-rank-with-meaning (Reaction, mostly coherence), and *fails* when the table's value is in specific designed asymmetries (Stance Counter's hard counters). The diagnostic's F6 fix must be applied selectively, and **state-gating (Lever B) is the more universal F6 reducer** because it cuts decisions-per-moment regardless of whether the underlying table derives.

---

## Scope/scale/direction coverage (per the all-directions directive)

- **Scope:** all three matchup tables tested (complete scope of the "derive tables" question). No matchup table left unexamined.
- **Scale:** these tables are **personal-scale-only** mechanics — they do not appear at settlement/territory/peninsula scales, so cross-scale derivation concerns do not arise here. (Cross-scale modifier concerns belong to Piece 2's σ-space treatment, where mass-combat interaction is live.)
- **Directions:** a derivation test is not a NERS-directional audit; the directional/loop analysis was completed in the resolution diagnostic. Piece 1's contribution is the falsifiable reducibility test that the diagnostic's F6 remediation depended on.

`[CONFIDENCE: high — all claims are numerical fits verified in-script against ±0.5 granularity; the Stance Counter non-reducibility is robust (tested both interpretable circular and abstract embedding models)]`
`[CORRECTION: my prior medium-confidence claim that Stance Counter would reduce to ~3 primitives is falsified; reported and revised here]`
`[SELF-AUTHORED — bias risk: I designed these tables; the derivation test is adversarial to my own F6 recommendation, and I let the data overturn the Stance Counter case rather than defending the prediction]`
