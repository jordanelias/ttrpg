# NERS Verdict — Fieldwork (Exploration / Investigation / Socializing)

**Date:** 2026-06-10 · **Session:** audit | ef659454b0c8 · **Skill:** valoria-resolution-diagnostic, Stages 3–4
**Inputs:** Stage 0–2 in `resolution_diagnostic_fieldwork.md`; Mode A–E findings in `00_MASTER.md` (this folder). All citations there; values below re-cite only where load-bearing.
**Supersedes:** `designs/audit/2026-05-28-resolution-diagnostic/resolution_diagnostic_investigation.md` Stage-3 verdict (index-depth, NERS-COMPLIANT) per that file's own supersession clause. Its architecture findings INV1–INV9 **stand** — re-derived at full depth, unreversed. What reverses is the spec/propagation layer the index read could not see.
`[GAP: omega framework — not read this session; NERS retained as the verdict frame per the skill's own caveat. Do not assume omega supersedes it.]`

---

## Stage 3 — Verdict

```
ENGINE: Fieldwork rolling resolution (Explore / Investigate / Social / Thread-Read / Knot / Sincerity / Concealment)
INSTANCE: A (healthy Mode-A pools on genuine setup axes; deterministic spine — Five-Filter Chain,
          Dialogue Lattice, Scene-as-Graph, NPE — correctly owns decisions and is excluded per Scope Gate)
COMPONENTS: per Phase 0 table, resolution_diagnostic_fieldwork.md

VERDICT: NON-COMPLIANT — the roll's inputs are canonically indeterminate (E, P1): three live documents
         give two different pools for Thread-Read and two different Disposition→Ob rules for every social
         roll; and the R-mandated ER-2 continuity correction is unlanded exactly where wound-floored
         fieldwork pools operate (P2). Architecture is sound; the canonical record is not.

N: PASS — no redundant roll. Evidence is a clock, not a disguised binary (INV2/INV3 re-confirmed);
   the deterministic pipeline owns disclosure/stance decisions; rolls survive only where a genuine
   uncertainty axis exists (Depth prep, Disposition, Inspiration, allies, concealment). No
   over-correction: no healthy dice engine was migrated to Mode B.
R: FAIL (P2, scoped) — the R checklist names "continuity correction present (ER-2)"; it is absent from
   params/core §Continuous Engine while params/core §Pool Floor explicitly routes wound-penalised
   fieldwork pools to the 1D floor (RD-1: odds 4–32% low below ~5D; TTRPG↔Godot divergence at the
   exact pools wounded explorers roll). Everything else under R holds at the extremes: loops bounded
   (Stage 4), clamps monotonic (min-1 Ob floors checked), graded recoverable output (Fail-Forward,
   Compromised recoverable), no fragile bare-stat binary with material stakes (Sincerity Gate is
   bare-Spirit but stakes cap at Disposition −1; Knot formation's sub-5D exposure is RD-3,
   [INTENT UNDETERMINED]). Validation debt RD-2 rides this letter: "holds at extremes" is argued
   from spot-checks + CLT, not a per-system sweep.
S: PASS — transitions clean across scales (Mode 1/2 scene↔season; BG Survey abstraction; Godot POI
   activation per §3.3); the rolling layer sits consistently on the deterministic spine — dice feed
   the Evidence clock, the chain adjudicates (Lesson 4 done well; no dice-on-a-ledger pattern).
E: FAIL (P1) — odds are not legible because the rule itself is not determinable: RD-S1 (Thread-Read
   Spirit×2+Hist+TPS vs Attunement×2+TPS; effective-Ob stepped table vs max(1, Ob−Disposition);
   three Disposition ranges/ceilings). A player or implementer reading canon cannot compute P for
   the same declared action. Secondary: RD-5 — §10.5 specifies per-face d10 UI the continuous
   engine doesn't run (presentation leak); P2-11 — hidden-threshold rule (§4.1) vs legible Case
   Board tiers, unsuperseded.

REMEDIATION (worst-first):
  P1  Adopt one canonical line (master fieldwork_v30 recommended; aligns with 2026-06-04 F-DISP
      "resolve → ceiling = Bonds"), regenerate params/fieldwork + splits from it; Jordan decides
      stepped-vs-subtraction and −3-vs-−4 floor explicitly (00_MASTER §6.1–.4).
  P1  Fix Thread-Read attribute in params/fieldwork + fieldwork_investigation.md (PP-619/PP-626).
  P1  Repair the propagation layer: fieldwork key in canonical_sources.yaml (the §12 "DONE PP-575"
      claim is false against the live file); dead parent paths; PP-719 record.
  P2  Land ER-2 `net − (Ob − 0.5)` in params/core §Continuous Engine (one line; no shift ≥5D).
  P2  Run the continuous-engine sweep at fieldwork parameters; fill sim/personal/{fieldwork,
      investigation}.py stubs; close or re-pose SIM-DEBT-SOC-01..03.
  P2  Rewrite §10.5 as magnitude-gauge presentation; declare §4.1 threshold-legibility supersession.
  P2  Remaining P2 set per 00_MASTER §3 (Niflhel propagation, Piety→Conviction naming, Interview
      schedule, pending-decision register entries, Depth-3 gate, Exposure schedule, F3 lifecycle).
```

---

## Stage 4 — Loop and cross-system re-test

Every rolling-layer feedback loop attacked; each either bounded by an explicit cap or ejects. Reported per `honest_findings` — survivals are findings.

| Loop | Mechanism | Bound | Result |
|---|---|---|---|
| Exposure failure spiral | fail → +Exposure → Noticed +1 Ob → harder | Success clears Desperate Trail; concealment −2, cover −1/scene, faction −2/season; territory-exit + season resets; **Compromised ejects** (recoverable terminal) | **survived** (intent-gated pass; deliberate with safeguards) |
| Desperate Trail | TN→8 + Exposure doubled (+4/fail) + GM complication | ≈20% Success at floor (math below) → 3–4 fails ≈ +12–16 Exposure → forced Compromised ejection | **survived** — the doubling IS the hard bound |
| Church AP feed | Exposure → Church Action Points | +1/character, +2/territory per season (PP-581; ≈11% of max CI acceleration) | **survived** |
| Domain Echo | fieldwork outcomes → territory state | ±2/season cap | **survived** |
| Knot strain | strain events → break | capacity 4/7 (Distant/Close), decay, break-at-Accounting boundary (EC-F2.B-01) | **survived** — stress_01 verified 22/24 NERS cells; 2 pre-known ⚠ Horizontal (low-Bonds lockout) |
| NPE stance convergence | season-end pairwise attraction | Volatility-check gated; Stance clamped 1–5; ecology re-weights generation | **survived**, with a long-run homogenization question parked under RD-2 (unsimmed, not asserted) |

Cross-system channels (from `fieldwork_lifecycle_stress_01` R-threads): FR Dissolution → Knot rupture → Conviction-Scar permanence (R1) — rupture floor is P1-1's −3/−4 subject, channel itself closed; Disposition +3 → named-officer companionship eligibility (R4) — gated by the same divergent Disposition spec, flagged not re-opened; Wager Obligation Knot-prerequisite (R5) — verified in `combat_arch_residual_stress_01 R5`, not re-run.

---

## Quantitative spot-checks (engine: params/core, Decision E)

Per-die: net = successes − count(1s); faces ≥ TN succeed; face 10 = +2 flat, **no chain** (PP-246). EV/die: TN6 +0.5, TN7 +0.4, TN8 +0.3; σ ≈ 0.8/die at TN7.

| Case | Pool / TN / Ob | P | Reading |
|---|---|---|---|
| Floor pool, Depth 1 | 5D / TN7 / Ob 1 | ≈ 71% Success | healthy baseline at the design floor |
| Floor pool, Depth 3 | 5D / TN7 / Ob 3 | ≈ 29% | preparation axis bites as designed |
| Depth 3 + hostile + foreign | 5D / TN7 / Ob 5 | ≈ 5% | steep, but low-irreversibility (clock progress retained, Fail-Forward) |
| Desperate Trail floor | 5D / TN8 / Ob 3 | ≈ 20% Success; P(net ≥ 1) ≈ 61% | **independently confirms ED-504's published ≈60%** |

Pools span 5–24D against a continuous engine validated at 5–17D (Decision E): 17–24D is CLT-safe extrapolation (σ√N regime improves with N); **below 5D is not reached by design except via wound penalties and the two sub-5D constructions — exactly RD-1/RD-3's territory**. The spot-checks support R's "holds at extremes" only at and above the floor; they do not substitute for the RD-2 sweep.

`[CONFIDENCE: high]` Stage-3 letter verdicts (textual + arithmetic); `[CONFIDENCE: medium]` RD-2-dependent claims (unvalidated ≠ wrong).
`[NULL: Stage-4 loop set — examined, no unbounded loop found]` — trail above, one row per loop.
