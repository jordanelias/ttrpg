# External Audit — `engine_replacement_reconciled.md`

**Date:** 2026-05-28
**Subject:** `designs/audit/2026-05-28-engine-replacement/engine_replacement_reconciled.md`
**Auditor:** independent session (bootstrap token `174e63d8…`); task gate `audit` passed; skill `valoria-mechanic-audit` (spine) + `valoria-resolution-diagnostic` (verification instrument).
**Bias disclosure:** `[SELF-AUTHORED — bias risk]` — the subject is prior-Claude output and *this audit is also Claude output*. The subject was treated as fully external per the diagnostic skill's "never defend prior output" guardrail. A self-review of this audit's own limits is in §6.
**Method:** full read of subject; authoritative git-tree existence sweep of every referenced artifact; **exact-convolution re-derivation** of the §2 table (independent of the subject's 300k Monte Carlo); verbatim verification of every load-bearing canonical claim against committed canon. Sources in the Citations block.

---

## §0 — Verdict

**The document's quantitative spine is sound and exact-verified, and the conclusion it reaches — "do not replace the core engine" — is correct and independently corroborated. But the document delivers that correct conclusion on top of two serious defects, plus a tail of smaller ones.**

1. **One severe canonical misattribution (A1):** it cites GD-2 three times as canon that *"already mandates"* a deterministic+stochastic **resolver**. The actual GD-2 governs action-**selection ordering** and is silent on resolution. The doc manufactured canonical authority for a design direction — the project's named worst-failure-mode.
2. **A manufactured "0 P1" headline (A2):** the committed resolution diagnostic rated the faction layer with **five P1 + two P1-canon-defect** findings. The reconciled doc reaches *"0 P1, more firmly repair-and-keep than v1"* by closing one finding legitimately (ER-2) and then **dropping four diagnostic findings, demoting a fifth to a footnote, and silently downgrading a sixth** — mostly without argument. The engine conclusion survives intact; the *cleanliness and completeness* the document claims do not.

The faction layer is genuinely NON-COMPLIANT with a thick P1 stack (the diagnostic is right about that). The reconciled doc makes it read as a tidy two-fix situation. Use the engine verdict; do not rely on the finding-distribution or the GD-2 justification as written.

---

## §1 — Findings (worst-first)

| # | Sev | Finding | Evidence |
|---|---|---|---|
| **A1** | **P1** | **GD-2 misattribution.** Doc §0/§6/§7: deterministic+stochastic resolver "as GD-2 already mandates." Actual GD-2 (`canon/02_canon_constraints.md`): *"Deterministic threat response precedes stochastic action **selection**"* — mandatory Muster/Govern scheduled before the stochastic candidate pass. A **selection-ordering** rule, orthogonal to outcome **resolution**. No canonical mandate for the ER-1 fix exists. | verbatim, canon/02 |
| **A2** | **P1** | **Manufactured "0 P1" / incomplete reconciliation.** Diagnostic Phase-6 triage: F1,F3,F5,F6,F7 = **P1**; F2,F8 = **P1 (canon defect)**; F4,F9 = P2. Reconciled §6 register carries only F1,F3,F6,F7; **drops F4, F5, F8, F9 entirely** (F5 & F8 are P1), **demotes F2 to an §8 "gap,"** and **downgrades F1 P1→P2** with no argument. §3's "agree everywhere… individually complete elsewhere" and the "0 P1" headline both misrepresent the finding landscape. | both registers read |
| **A3** | P2 | **Overstated ER-2 closure (CLT residual).** After the continuity correction the residual vs exact discrete is **15.4% relative (1.5pp) at 1D Ob2** and **14.9% at 2D Ob4** — the finite-N / non-normality error a continuity correction *cannot* remove, sitting at the small-pool stress points the analysis exists to address. The doc's "not a CLT failure / within a few percent / one-line / no design risk / P1→P3" is too clean there. (Practical impact is small — absolute probabilities are tiny — so this is a precision-of-claim defect, not "the fix fails.") | exact convolution |
| **A4** | P2 | **Silent severity reconciliation.** v1 rates the central faction finding P2 (ER-1); the diagnostic rates the same issue P1 (F1). The doc adopts P2 and calls them *"the same conclusion from two angles"* without arguing for the lower rating. | both registers |
| **A5** | P2 | **"One-line fix" likely incomplete.** A *consistent* continuity correction shifts Success (Ob−0.5) **and** Overwhelming (2·Ob), Partial, and the magnitude gauge `net−Ob` (`core.md` §Continuous Engine) by 0.5. The doc specifies only the Success threshold; applied alone it desynchronises the degree bands. | reasoned from core.md |
| **A6** | P2 | **No claim-trail.** Heavy canonical assertions (GD-2, PP-717, ER/F IDs, paths, formulas) in a committed-canon document with **zero `[READ:]` evidence trail** — the discipline whose absence directly enabled A1. | structural |
| **A7** | P2 | **Self-review blind to its own central weakness.** §8 lists F2/settlement/continuity-sufficiency limits but omits the A2 completeness/severity gap. The bias discipline is applied to the priors, never to the reconciliation itself. | structural |
| **A8** | P3 | **Upstream diagnostic left wrong.** Committed `ners_verdict_faction.md` / `resolution_diagnostic_faction.md` still state F1 *"P ≈ 0."* The doc corrects this to 0.010 only in itself, leaving two committed artifacts disagreeing, without flagging the upstream patch. | verified |
| **A9** | P3 | **"Recommend: apply" (§7.2)** sits adjacent to design-level calls and the open scene-combat handoff's explicit *"NOT recommendation"* stance; A1 compounds it by lending false canonical authority to §7.1's resolver recommendation. | governance |
| **A10** | P3 | **No confidence tag on the register-completeness / "firmer than v1" conclusion** — its weakest claim — while the quantitative claims are well-tagged. | structural |
| **A11** | P3 | **Imprecise spec.** "Add `Ob − 0.5`" (§7) is ambiguous about the operand; the precise rule is "compare the sampled `net` against `Ob − 0.5`." | precision |
| **A12** | P3 | **MB5 valence inversion.** Diagnostic triage rates MB5 (*"No Pool Floor at mass scale"*) as **P1 (NOVEL)** — a problem. §3 cites it approvingly as *"unit-deletion substitute… explains why mass battle escapes the faction degeneracy"* — recasting a P1 problem as a benign feature, with no acknowledgment or argument (same class as A2/A4). | diagnostic mass-battle triage |

### A1 — detail (the worst finding)
GD-2's full text: faction action-*selection* runs a mandatory-actions pass (Muster on Accord-≤3 ungarrisoned territory; Govern on Accord-≤2 garrisoned) **before** stochastic candidate generation. That constrains *which actions the AI queues and in what order* — it has nothing to say about *how an action's success is resolved*. ER-1 is a resolution defect (a bare 2D pool deciding a pivotal, irreversible outcome). GD-2 does not touch it. The doc did not cite weakly; it asserted canon *"already mandates"* its preferred resolver, three times, as a pillar of §7.1's recommendation. The likely mechanism is a phrase-level conflation (GD-2 contains the words "deterministic" and "stochastic"), not deliberate invention — but the effect is a confidently-wrong canonical claim, and A6 (no claim-trail) is exactly why it was never caught: pasting GD-2's actual text would have exposed it on sight.

### A2 — detail (the central structural problem)
"0 P1" is assembled from one legitimate move and several illegitimate ones:
- **Legitimate:** ER-2 closed P1→P3 (the §2 test is sound — see §2).
- **Illegitimate:** F1 downgraded P1→P2 (adopting v1 over the diagnostic, unargued); F4, F5, F8, F9 dropped from the register entirely; F2 demoted to an §8 limits-gap.

Of the dropped/demoted, **F2, F4, F5, F9 are squarely resolution-architecture findings** the document claims to cover (F2 = the Ob formula feeding the resolver; F4 = non-uniform stat-damage impact, the same √N effect §4 discusses; F5 = the trigger-asymmetry feeding the collapse loop §3 partially engages; F9 = a disguised-binary shallow clock). Only **F8** (PP-686 stat-schema drift) is plausibly outside engine scope — and even that warrants a "carried elsewhere" note in a document whose §3 is literally titled a reconciliation map. The defect is not that each omission is necessarily wrong on the merits; it is that the document **claims completeness and agreement it has not established**, and the "0 P1 / more firmly repair-and-keep" framing depends on that overclaim.

---

## §2 — Quantitative spine: verified correct

Independent **exact convolution** (single-die net pmf `{−1:.1, 0:.5, +1:.3, +2:.1}`, μ=0.40, σ=0.80; continuous = `Normal(0.4N, 0.8√N)`; continuity = compare against `Ob−0.5`) reproduces the §2 table:

| Pool / Ob | discrete (exact) | doc | raw cont. | +continuity | doc | ratio | cc-residual |
|---|---|---|---|---|---|---|---|
| 1D Ob2 | 0.1000 | 0.101 | 0.023 | 0.085 | 0.085 | 4.40× | 1.54pp / **15.4%** |
| 2D Ob3 | **0.0700** | 0.070 | 0.026 | 0.066 | 0.067 | 2.70× | 0.35pp / 5.0% |
| 2D Ob4 | **0.0100** | 0.010 | 0.002 | 0.009 | 0.009 | 4.28× | 0.15pp / **14.9%** |
| 3D Ob3 | 0.1720 | 0.171 | 0.097 | 0.174 | 0.174 | 1.77× | 0.21pp / 1.2% |
| 4D Ob3 | 0.2794 | 0.278 | 0.191 | 0.287 | 0.287 | 1.46× | 0.75pp / 2.7% |
| 5D Ob3 | 0.3800 | 0.381 | 0.288 | 0.390 | 0.390 | 1.32× | 0.99pp / 2.6% |
| 8D Ob3 | 0.6142 | 0.615 | 0.535 | 0.621 | 0.622 | 1.15× | 0.73pp / 1.2% |
| 12D Ob3 | 0.7957 | 0.796 | 0.742 | 0.797 | 0.797 | 1.07× | 0.10pp / 0.1% |
| 17D Ob3 | 0.9061 | 0.907 | 0.875 | 0.904 | 0.904 | 1.04× | 0.23pp / 0.3% |

**Confirmed correct in the document:**
- **Die rule** matches `params/core.md §Die Rule` exactly (face 1=−1, 7–9=+1, 10=+2 flat, no chain, net may be negative); μ=0.40, σ=0.80 confirmed.
- **§2 table** is arithmetically exact across all nine cells; the `Ob−0.5` continuity correction is the correct textbook adjustment; the disc/raw ratios are right.
- **ER-2 validation-gap closure is legitimate** — v1 explicitly deferred this exact small-pool sim as debt; the doc ran it. Canon itself pre-flagged the gap (`core.md` WS-D-1/ED-836: equivalence validated for mean/std only at 5–17D; faction small-pool *"would benefit from dedicated sanity-check"*).
- **Caught a real upstream error:** the committed diagnostic says F1 *"P ≈ 0"*; the doc corrects to 0.010 — exact convolution confirms **0.0100**.

The only quantitative overstatement is A3 (the residual the continuity correction leaves at the smallest pools).

---

## §3 — Canonical fidelity: accurate vs misattributed

| Claim | Status |
|---|---|
| GD-2 mandates det+stochastic resolver | **FALSE (A1)** — GD-2 governs action-selection ordering |
| v1 register (ER-1…ER-9, 1 P1/4 P2/4 P3, deferred test, repair-and-keep verdict) | **ACCURATE** — verbatim match |
| F2 = Ob "target stat (factions_personal §8.1) vs floor(target/2)+1 (params)" | **ACCURATE** (best-handled diagnostic finding; but demoted from register — A2) |
| Diagnostic faction verdict = NON-COMPLIANT | **ACCURATE** |
| Diagnostic combat verdict = NERS-COMPLIANT; PP-717 implements lessons | **ACCURATE** — PP-717 is real, combat-scoped (Fiore half-step TN; MW cap; D1–D3) |
| ER-9 summed-pool model (`Σ Martial + floor(Military/2)`) | **ACCURATE** — battle pool is "aggregated, not bare" per diagnostic Phase-0 |
| MB5 = "no Pool Floor (unit-deletion substitute)" | descriptively accurate, but **valence-inverted (A12)** — diagnostic rates it P1 (NOVEL) |
| Both reconciliation targets exist as committed canon | **CONFIRMED** (v1 + the 14-file diagnostic artifact both present) |

---

## §4 — Closed residuals

- **C9 / F2:** closed. Two formulas verified verbatim from the diagnostic Phase-0 table; the doc's characterization is correct. (Note one side, the `params` formula, lives under the PP-686-superseded faction architecture — a wrinkle the doc does not mention, but it does not affect the doc's "open prerequisite" framing.)
- **C7 / MB5:** closed. MB5 is a diagnostic **P1 (NOVEL)** finding, not the benign mechanism §3 implies — see A12.

---

## §5 — Staged editorial-ledger candidates (NOT committed — finding B6)

Commits to `main` are blocked by branch protection (B6), and `canon/editorial_ledger.yaml` is over-threshold mid-consolidation (flagged at bootstrap). Per the subject's own pattern, candidates are staged inline:

- **ED-NEW (A1):** `engine_replacement_reconciled.md` §0/§6/§7 miscite GD-2 — strike/replace the "as GD-2 already mandates" claims; GD-2 (`canon/02 §GD-2`) governs action-selection ordering, not resolution. The det+stochastic resolver direction must stand on its own design merits (CK3 precedent), not on a fabricated canonical mandate.
- **ED-NEW (A2):** `engine_replacement_reconciled.md` §3/§6 omit diagnostic F4/F5/F8/F9, demote F2, and downgrade F1 unargued; the "0 P1" distribution is inconsistent with the diagnostic's 5 P1 + 2 P1-canon-defect faction findings. Re-issue the register with explicit in-scope/out-of-scope tagging for each diagnostic finding.
- **ED-NEW (A8):** `ners_verdict_faction.md` / `resolution_diagnostic_faction.md` F1 = "P ≈ 0" superseded by exact 0.010 — add `[SUPERSEDED-BY]` markers to the upstream files so the corrected number is canonical at source.

---

## §6 — This audit's own limitations (Pass-3 self-review)

`[SELF-AUTHORED — bias risk]` Limits an independent reviewer would add:
- **Scope caveat on A2/A12.** The subject is scoped to *engine replacement*, so dropping faction-layer findings that are not engine-resolver issues (F8 especially; arguably MB5 at mass scale) is *partially* a defensible scope decision, not pure defect. A2 is framed accordingly — the defect is the **completeness/agreement overclaim**, not a blanket "every omission is wrong."
- **The verdict is sound.** Twelve findings do not imply the engine conclusion is wrong. "Do not replace the core engine" is correct and corroborated by v1, the diagnostic's per-system compliance, and the verified §2 analysis. The findings concern the document's *rigor and claims*, not its bottom line.
- **A1 is conflation, not proven malice.** Severity derives from the load-bearing misuse and the false "already mandates" framing, not from intent.
- **This audit is not exhaustive on every surface.** The diagnostic's other per-system verdicts (investigation, peninsula, social, threadwork) and v1 §3.1–3.9 external-game precedent were accepted as-is per the agreed scope, not independently re-derived. Treated as `[UNVERIFIED]` where the subject relies on them.

---

## §7 — Confidence

- `[CONFIDENCE: high]` — A1 (verbatim GD-2), A2 (both registers read), A3 (exact convolution), §2 verification, A8, C9, C7/A12, all "accurate" rows in §3.
- `[CONFIDENCE: medium]` — A5 (degree-band desync is reasoned from core.md, not tested against an implementation), A4/A7/A9/A10 (structural/governance judgments).
- `[CONFIDENCE: low]` — none load-bearing.

---

**Citations** (canonical files consulted this session — modeling the discipline A6 flags as absent in the subject):
- `params/core.md` — §Die Rule, §Continuous Engine, §EV per die, §Quick Reference
- `canon/02_canon_constraints.md` — GD-1/2/3, P-01–P-15
- `designs/audit/2026-05-28-resolution-diagnostic/resolution_diagnostic_faction.md` — Phase-0 component table, §7 triage, §8 lesson map
- `designs/audit/2026-05-28-resolution-diagnostic/ners_verdict_faction.md` — verdict (NON-COMPLIANT)
- `designs/audit/2026-05-28-resolution-diagnostic/ners_verdict_combat.md` — verdict (NERS-COMPLIANT)
- `designs/audit/2026-05-28-resolution-diagnostic/resolution_diagnostic_mass_battle.md` — §7 triage (MB5 P1)
- `designs/audit/2026-05-28-engine-replacement/engine_replacement_audit.md` — v1 §0/§4/§6/§9
- `references/canonical_sources.yaml`, `params/factions.md` — gd_binding, supersession (PP-686)
- subject: `designs/audit/2026-05-28-engine-replacement/engine_replacement_reconciled.md` — full
