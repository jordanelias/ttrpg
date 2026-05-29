# Engine Replacement Audit — Reconciled

**Date:** 2026-05-28
**Supersedes:** `engine_replacement_audit.md` (v1, session b1141a77) — retained for trail; this version reconciles it with the resolution diagnostic (session c93a36df, `designs/audit/2026-05-28-resolution-diagnostic/`) and closes its lone P1 (ER-2) with the empirical test v1 filed as debt but never ran.
**Bias disclosure:** Both prior artifacts are Claude-authored in earlier sessions. `[SELF-AUTHORED — bias risk]` applies to **both** the v1 assessment and the resolution diagnostic; this recreation treats each as external and surfaces what each got wrong, including two arithmetic errors of my own (below).
**Method:** Reconcile the two prior analyses; test the one empirical claim both depend on (discrete↔continuous equivalence at faction-scale pools); re-derive the verdict from the corrected evidence. Six-direction lens applied in §4. Decision ownership: Jordan specifies; this informs.

---

## §0 — Reconciled Verdict

**Do not replace the core engine — confirmed, and now on firmer ground than v1.** The faction-scale problem both prior analyses circled is **two separable problems with two separate fixes**, and disentangling them shrinks the case for replacing anything:

1. **Bare-stat faction dice are statistically degenerate** (ER-1 / diagnostic F1/F3). A Military-2 faction rolling 2D succeeds at a Domain Action with P ≈ 0.070 (Ob 3) or 0.010 (Ob 4). This is a **resolver-design** problem at one scale — fixable by aggregating the pool (as mass battle already does, §3.5/ER-9) or going deterministic+stochastic (as CK3/EU/KoDP exemplify). It does **not** implicate the engine elsewhere.
2. **The continuous (videogame) engine misrepresents the discrete distribution at small pools** (ER-2). The test below shows the divergence is 2.7–4.4× at 1–4D — but it is **almost entirely a missing continuity correction**. Adding `Ob − 0.5` restores agreement to within a few percent even at 2D. ER-2's fix is a **one-line engine-implementation term**, not a resolver change and not a paradigm finding.

v1 bundled these as joint grounds for "replace the resolver at faction scale." They are not joint. **ER-2 is now closed as a continuity-correction defect (downgraded P1 → P3-implementation).** Only ER-1 remains as a genuine resolver-design question, and even that is a swap *at one scale*, not an engine replacement.

**The resolution diagnostic and this assessment agree and reconcile cleanly:** the diagnostic's faction-layer **NON-COMPLIANT** verdict and v1's **repair-and-keep** verdict are the same conclusion from two angles. Keep the graded resolver everywhere pools are healthy (personal combat, social, thread, aggregated mass battle); the faction layer needs (a) a resolver redesign and (b) the engine needs a continuity term. Neither touches the substrate at personal/social/thread/mass scales.

**Combat feel remains a separate architecture decision** (turn-vs-real-time), orthogonal to the dice engine — v1's ER-4 reasoning is sound and the diagnostic's combat verdict (COMPLIANT; PP-717 implements the relevant lessons) agrees. No tension.

---

## §1 — What This Recreation Changes

| v1 / diagnostic claim | Correction |
|---|---|
| Diagnostic F1: faction bare 2D ≈ **P 0.16** (original), then **P 0 / "deterministic death spiral"** (last pass) | **Both wrong** — used a simplified "die ≥ 7 = +1 success" model. Authoritative rule (face 1 = −1, 10 = +2) gives **0.070 at Ob 3, 0.010 at Ob 4**. Degenerate, but neither zero nor deterministic. Retracted and corrected. |
| Diagnostic F3: anti-death-spiral floor "structurally unreachable / P≈0" | Stab-2 → 2D vs the Ob-4 cap = **P ≈ 0.010**. Effectively inert (1% recovery per Accounting is no safeguard), but ~1%, not 0. Qualitative finding stands; "unreachable" softened to "effectively inert." |
| v1 ER-2 (P1): continuous-engine equivalence "unvalidated" at faction scale; filed as validation debt | **Closed empirically** (§2). Equivalence holds ≥5D; diverges 2.7–4.4× <5D; the divergence is a missing continuity correction, fixed by `Ob − 0.5`. **Downgraded P1 → P3-implementation.** |
| v1 framing: ER-1 + ER-2 jointly justify replacing the faction resolver | **Disentangled** — ER-2 is an engine-implementation fix, ER-1 is a resolver-design question. Only ER-1 bears on resolver replacement. |
| Diagnostic last-pass: faction collapse is **deterministic** for weak factions | **Corrected** — with ~1–7% recovery odds at each gate, the spiral is heavily loss-weighted **probabilistic**, not deterministic. |

---

## §2 — Logic-Pipeline Test (closes ER-2)

Discrete vs continuous engine, `P(net ≥ Ob)`, TN 7, authoritative die rule (face 1 = −1, 2–6 = 0, 7–9 = +1, 10 = +2; net may be negative). Monte Carlo 300k/cell; sanity μ/die = 0.3999 vs spec 0.400.

| Pool | Ob | discrete | cont (raw) | cont (+continuity) | disc/raw | regime |
|---|---|---|---|---|---|---|
| 1 | 2 | 0.101 | 0.023 | 0.085 | 4.43× | <5D faction |
| 2 | 3 | 0.070 | 0.026 | 0.067 | 2.71× | <5D faction |
| 2 | 4 | 0.010 | 0.002 | 0.009 | 4.37× | <5D faction |
| 3 | 3 | 0.171 | 0.097 | 0.174 | 1.76× | <5D faction |
| 4 | 3 | 0.278 | 0.191 | 0.287 | 1.46× | <5D faction |
| 5 | 3 | 0.381 | 0.288 | 0.390 | 1.32× | ≥5D validated |
| 8 | 3 | 0.615 | 0.535 | 0.622 | 1.15× | ≥5D validated |
| 12 | 3 | 0.796 | 0.742 | 0.797 | 1.07× | ≥5D validated |
| 17 | 3 | 0.907 | 0.875 | 0.904 | 1.04× | ≥5D validated |

**Two findings:**
- **The spec's "validated at 5–17D" is correct for mean/std but the raw continuous `P(success)` still runs 4–32% low** at those pools because the implementation omits a continuity correction. The continuity-corrected column tracks discrete to within ~1–3% across the *entire* range, including 1–4D.
- **The faction-scale fidelity gap (ER-2) is a continuity-correction artifact, not a CLT failure.** `net − (Ob − 0.5)` is the fix; it restores discrete↔continuous agreement at 2D (0.067 vs 0.070). This is a one-line edit to `params/core.md §Continuous Engine`, not a resolver decision.

The degeneracy itself (ER-1/F1) is independent of which engine renders it: discrete 0.070 and corrected-continuous 0.067 at 2D Ob 3 *agree* that a bare 2D pivotal action is ~7%. The engines now concur; the resolver is still too small for the stakes.

---

## §3 — Reconciliation Map: Diagnostic ↔ Engine Findings

| Resolution-diagnostic finding | Engine-assessment finding | Reconciled status |
|---|---|---|
| F1 — bare-stat NPC Domain pool degenerate | ER-1 — bare 1–7D pool degenerate where stakes highest | **Same finding.** Corrected number: 0.070 @ Ob 3. Fix: aggregate (ER-9 model) or deterministic+stochastic (CK3/EU/KoDP precedent). |
| F3 — anti-death-spiral floor inactive | (not in v1) | Diagnostic-only; survives at ~1% (effectively inert). Same resolver fix dissolves it. |
| F6/F7 — L1 collapse / L7 Wealth-0 cascade | (not in v1) | Diagnostic-only; **corrected** from "deterministic" to "probabilistic, loss-weighted." Resolver fix raises recovery odds. |
| (not in diagnostic) | ER-2 — continuous equivalence unvalidated <5D | **Closed here** (§2); continuity-correction fix; P1→P3. |
| Combat: COMPLIANT, PP-717 implements lessons | ER-4 — combat feel is combat-layer, not engine | **Agree.** No tension. |
| Threadwork: COMPLIANT, consequence-architecture | ER-8 — resolver incidental, must stay graded | **Agree.** |
| Mass battle MB5 — no Pool Floor (unit-deletion substitute) | ER-9 — summed pool avoids degeneracy; model for ER-1 | **Complementary.** MB5's unit-deletion floor + ER-9's summed pool together explain why mass battle escapes the faction degeneracy. |
| Investigation/peninsula: deterministic, COMPLIANT | §3.3/§3.8 — engine correctly absent/demoted | **Agree.** |

**Net reconciliation:** the two analyses overlap on faction (F1↔ER-1), agree everywhere they both speak, and are individually complete elsewhere. The only genuine conflict — whether the faction issue is "balance" (diagnostic) or "engine" (assessment) — dissolves: it is **balance (resolver too small) plus a now-closed engine-fidelity sub-issue (continuity)**, not a paradigm problem.

---

## §4 — All-Directions Analysis

- **Top-down (intent_of_game loop).** The engine must emit graded magnitude to drive Domain Echo / co-movement / clocks; the continuous gauge does this and the continuity fix improves low-pool fidelity. PASS — but the faction-side *input* to the loop is the degenerate pool (ER-1), so the loop's strategic arm is noisy until the resolver is fixed.
- **Bottom-up (die mechanics).** Tested (§2). Engine sound ≥5D; small-pool behavior is a continuity artifact (engine) over a too-small pool (resolver).
- **Vertical (stat→pool scaling).** Same 1–7 stat → 17D personal / 7D faction-bare / clocks peninsula. ER-3 pool-size shock is real and **engine-invariant** — it recurs under any resolver and is a scale-mapping decision, not an engine defect.
- **Diagonal (cross-system).** Graded output is the cross-scale currency (v1 §1.4); a hard constraint on any replacement. The continuity fix *strengthens* the diagonal (finer Domain Echo at low pools).
- **Lateral (peer parity).** Faction is the sole outlier: every other scale has healthy pools or is deterministic. Lateral comparison is the strongest single argument that the *resolver*, not the *engine*, is the faction problem.
- **Horizontal (TTRPG vs videogame).** Without the continuity fix, the same faction action has materially different odds in discrete (TTRPG) vs raw-continuous (videogame) mode — a horizontal inconsistency v1's finding (2) glossed by asserting "it's already continuous." §2 both exposes and fixes it.

---

## §5 — Critical Findings About the Prior Assessment (unbiased)

1. **v1 finding (2) is in tension with v1 finding (3)/ER-2, unreconciled.** Finding (2) argues "the videogame already runs a continuous engine, so the d10 critique is moot"; ER-2 admits that continuous engine is unvalidated exactly at faction scale. So (2)'s reassurance does not reach the scale where (3) locates the problem. §2 resolves it: raw continuous *diverges* at faction scale, so "it's already continuous" was not a defense there — though the continuity fix now makes it one.
2. **v1 filed its one P1 as debt and never ran it.** ER-2's "run a small-pool sim" is the test in §2. Leaving the lone P1 unexecuted while issuing a confident verdict is the same read-then-defer pattern the resolution diagnostic's own self-review flagged. Closed here.
3. **v1 conflated ER-1 and ER-2** as joint "replace at faction scale" grounds. They have different fixes (resolver vs engine-implementation). The conflation inflated the apparent case for resolver replacement.
4. **Neither prior artifact referenced the other**, despite same-day authoring on overlapping ground (the faction small-pool problem). This recreation is the missing cross-reference.
5. **Roadmap gap.** Neither fix is on `roadmap_state.yaml` (currently Phase 2, subsystem documentation). The continuity correction is a Phase-0-class immediate repair to `params/core.md`; the faction resolver redesign is a Phase-3/4 item. Both should be added to the roadmap; currently they appear in no phase or pending-decision.

---

## §6 — Reconciled Findings Register

| # | Finding | Sev | Fix | Status |
|---|---|---|---|---|
| ER-1 / F1 | Bare-stat faction pool degenerate (0.070 @ Ob 3) | P2 | Aggregate (ER-9) or deterministic+stochastic (CK3/EU/KoDP precedent) — **resolver** | open; Jordan call §7 |
| ER-2 | Continuous engine diverges 2.7–4.4× <5D | ~~P1~~ **P3** | Add continuity correction `Ob − 0.5` — **engine** | **CLOSED** (§2) |
| F3 | Anti-death-spiral floor ~1% (inert) | P2 | dissolved by ER-1 resolver fix | open |
| F6/F7 | Faction collapse loops (probabilistic, loss-weighted) | P2 | ER-1 fix raises recovery odds | open; corrected |
| ER-3 | Cross-scale pool-size shock; engine-invariant | P2 | scale-mapping decision (not engine) | open |
| ER-4 | Combat feel mis-attributed to engine | P2 | combat-layer / architecture | open; agrees w/ diagnostic |
| ER-6 | Settlement resolver unspecified | P2 | specify deterministic-first | open |
| ER-5/7/8/9 | TN/Ob channels; social heaviness; threadwork-graded; 2-attr unit pool | P3 | polish | as v1 |

**Distribution after reconciliation (ENGINE-scope ER-findings only): 0 open P1 in the engine register (ER-2 closed → P3), 6 P2, 5 P3. No paradigm finding.** The engine verdict is *more* firmly repair-and-keep than v1, because its only P1 dissolved into a one-line fix.

**[CORRECTED 2026-05-28, ED-866 — scope tagging.** The "0 P1" above is the count of **engine-replacement (ER-series) findings only**, and reflects ER-2's downgrade plus the F2 ruling's argued downgrades of the faction findings (commit 67c10722). It does **not** mean the project has zero P1 issues. **Out of scope for this engine register, in scope for the resolution diagnostic:** the faction-layer findings retain their own status there — F1 (now P2 post-F2-ruling), the L1-collapse-terminal-bound and Wealth-Military-cascade items (ED-868 in the corrected ledger numbering), the PP-686 schema drift, the threadwork Mending contradiction (ED-868 JSONL), etc. This register adjudicates the *engine*; it does not subsume or resolve the *system-design* findings the diagnostic owns. Reading "0 P1" as a project-wide all-clear was the defect ED-866 names.]**

---

## §7 — Jordan's Calls (sharpened)

1. **Faction resolver (the one real change).** Aggregate the pool (mass-battle ER-9 model: sum relevant unit/derived values so faction actions roll healthy pools) **or** go deterministic+stochastic (CK3/EU/KoDP-style capped-% + weighted events). *Input:* ER-1 degeneracy is now quantified (0.070 @ Ob 3); the mass-battle layer's summed pool is the in-project precedent for the aggregation fix. This is a resolver swap at one scale, not an engine replacement. **[CORRECTED 2026-05-28, ED-865:** earlier text cited **GD-2** as mandating a deterministic+stochastic *resolver*. That is a miscitation — GD-2 (`canon/02 §B`) governs faction action-**selection** ordering (mandatory threat-response before stochastic candidate generation), **not** resolution. GD-2 imposes no resolver requirement; the deterministic+stochastic option stands on acclaimed-game precedent, not on GD-2.**]**
2. **Continuity correction (cheap, do regardless).** Add `Ob − 0.5` to the continuous-engine spec so TTRPG and videogame modes agree at all pool sizes. Closes ER-2; one-line edit; no design risk. *Recommend: apply.*
3. **Combat substrate (unchanged from v1).** Turn-resolved degree vs real-time HEMA is an architecture decision orthogonal to the dice; Battle Brothers shows the five desired properties are reachable turn-based. Not an engine question.
4. **Settlement (ER-6).** Specify deterministic-first to avoid importing the faction degeneracy.

---

## §8 — Limits & Confidence

- `[CONFIDENCE: high]` — §2 test (sanity-checked against spec μ; continuity result is a clean closed-form match). The ER-2 closure and the ER-1/ER-2 disentanglement are the load-bearing new results and are robust.
- `[CONFIDENCE: high]` — corrected F1/F3 numbers (authoritative die rule, verified μ).
- `[CONFIDENCE: medium]` — that the continuity correction is *sufficient* for all faction-scale uses; tested at Ob 2–4 / pools 1–17; not exhaustively across every faction action's actual Ob distribution (which is itself unresolved pending the F2 Ob-formula contradiction).
- `[CONFIDENCE: medium]` — settlement (ER-6, unspecified rung), as in v1.
- `[GAP: F2 Ob-formula contradiction]` — whether faction Domain Action Ob = target stat (design doc) or floor(stat/2)+1 (params) still determines the real degeneracy severity; resolving F2 is prerequisite to finalizing the ER-1 resolver fix.
- **Did not re-cover:** v1's full per-system precedent research (§3.1–3.9, §6) — accepted as-is where this recreation does not contradict it; the combat/social/investigation/mass/peninsula verdicts stand. Precedent numbers indicative, not authoritative.
- **Not committed beyond this file.** Editorial-ledger entries (ER-1 resolver, continuity correction, F2 prerequisite) staged for a dedicated ledger session.

**One-line answer:** *Do not replace the core engine — the case is now weaker than v1 thought, because v1's only P1 (continuous-engine fidelity at faction scale) is a one-line continuity correction, not a resolver problem. The single genuine change is the faction resolver (aggregate per the mass-battle ER-9 precedent, or deterministic+stochastic per CK3/EU/KoDP), and even that is a one-scale swap, not an engine replacement. The resolution diagnostic and this assessment agree: keep the engine where pools are healthy, fix the faction resolver, add the continuity term, treat combat feel as a separate architecture decision.*
