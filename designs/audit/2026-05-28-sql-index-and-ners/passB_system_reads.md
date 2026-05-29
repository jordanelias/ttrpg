# Pass B — MASTER (consolidated)

**Date:** 2026-05-28. **Task:** audit (bootstrapped). Index-driven reads via `concept_files`.
**Supersedes** the working batch files `passB_threadwork_and_force3.md`, `passB_batch2_omitted_loops.md`, `passB_batch3_faction_collapse_and_MS.md` (collated here per PI `<document_consolidation>`; originals retained for trail). This is the single Pass-B deliverable feeding Pass C.
`[SELF-AUTHORED — bias risk]`: several reads tested hypotheses the project's own diagnostic advanced; corrections surfaced below are stated as such.

---

## 1. Coverage ledger (systems read this pass)

```
threadwork           params/threadwork.md (full) + threadwork_v30.md + _infill (MS/cap/ops sections)
calamity             calamity_radiation_v30 + _infill (geographic MS framework)  [⚠ RS/MS label drift]
ms_trajectory        ms_trajectory_v1.md (two-force model, historical climb)     [not a concept — see DRIFT]
conviction           conviction_track_v1 (⚠ partial-superseded) + conviction_taxonomy_v30 (current)
insurgency_pipeline  insurgency_pipeline_v30 (GD-3, canonical)
mass_battle          mass_battle_integration_v30 (sim-audit; morale sub-loop)
npc_relational        npc_relational_graph_v30 (PROVISIONAL; defection hooks)
faction (core)       faction_layer_v30 (§1 Stability/recovery/collapse) + faction_behavior_v30 (scan) + military_layer_v30 (§1.3–1.7)
                     [12 of 19 faction files deferred — faction system needs its own completion pass]
```
`[CONFIDENCE: high on MS engine + the five loops; medium on full faction system — core read only.]`

---

## 2. MS engine (consolidated; RS≡MS — label drift, DRIFT-1)

**Two-force model (ms_trajectory_v1 §, params/threadwork.md L112–113):**
- **Force 1 — baseline continuity: POSITIVE, decelerating (logarithmic), rate ∝ remaining disruption** (fastest when MS is low). P-07: this is Ein Sof's constitutive positive being, not the substrate "healing." Historical climb ≈ +13 points over 257 years (Catastrophe floor ~5 → game-start MS). **Implication: a natural damper on MS decline — the closer MS gets to 0, the harder Force 1 pushes back.**
- **Force 2+ (negative, game-era):** warfare (flat −1/battle, cap −3/season — the ×3 multiplier was STRUCK, campaign_architecture §3.1); Gap-bleed (per-scale 1/2/3/5 per open season, params §PP-604 — *or* flat −4/season, threadwork_v30 §5; DRIFT-2); Lock chronic drift (−1→−5/season per territory); one-time hits (Dissolution Failure −8; FR-vs-FR −1..−5); **Foundational ops ×3 MS multiplier** (POP Success −9 / Failure −6 min, threadwork_v30_infill §2.4 — the magnitude×scale multiplier, already canon).
- **Maintain mitigation:** WC2 halves all Gap/Lock drain; WC3 +2 MS/s; Mending Sanctuary +1 MS/s (params §WC); Foundational Calamity-site Mend Ob 12 (~22%/attempt).
- **Start MS = 60** (peninsula already strained, threadwork_v30_infill §5.1). Bands: 59–40 Fragile, 39–20 Fractured (spontaneous Gaps), 19–1 Critical (2–4 season endgame). **MS≤10 → one-time Southernmost Surge; MS 0 → Rupture** (calamity_radiation_v30).

**ED-CANDIDATE (P1) — seasonal MS cap contradicted.** params/threadwork.md (2026-04-14, PP-603) = cap **STRUCK**; threadwork_v30 §5 (2026-04-02) = **±10/season**. Newer file strikes it; design doc retains it. **Owner decision needed.**

**[GAP] — Second-Calamity terminal (10 seasons sustained MS≤5) and the baseline-decay rate are NOT in calamity_radiation or ms_trajectory.** Owner-stated intent without a canonical doc home in the MS design set. Must be formalized (likely a victory/loss doc) before the arc is fully grounded.

---

## 3. Force-3 bound (refined; decision-locked)

Jordan's lock: tearing scales magnitude×scale, threadwork as a **multiplier**; guardrail **MS not 0 in ~4 seasons**; bound the multiplier + Gap-bleed, not warfare. `[ASSUMPTION: −10/season net MS-loss cap — your go on my default; ED cap-contradiction open.]`

**Two stacked guardrails, both grounded:**
1. **Intrinsic damper (Force 1):** because baseline-positive grows as MS drops, net decline naturally slows near 0 — reaching the Calamity-recurs floor *requires sustained extreme tearing* that overwhelms the rising Force 1. Warfare (−3/s) can't (Force 1 near low MS exceeds that); **only heavy threadwork can drive MS to 0.** This is the magnitude×scale lock, satisfied by the physics already in canon.
2. **Hard cap (−10/season net loss):** belt-and-suspenders. From MS 60, ≥6 seasons to 0; from the Fragile floor (40), ≥4. Heavy Foundational/Structural threadwork *saturates* the cap; warfare can't approach it. Guardrail met with margin.

**Net:** the multiplier has teeth (more/deeper Gaps + Locks + Foundational ops → faster decline up to the ceiling), warfare cannot crash MS, and the climax (civil war + invasion + heavy tearing) takes a dramatic ≥4-season Critical phase. Winnable on maintain (WC halves bleed + adds +2–3/s, can claw MS back above the Second-Calamity line); embrace lets MS fall to the playable Post-Calamity state. **Arc length must be validated by a Monte-Carlo run (mc engine) in Pass C** — the per-season *intensity* (concurrent Gap/Lock count) that sets pacing is the free variable. `[CONFIDENCE: medium — rates cited; pacing needs sim.]`

---

## 4. Loop inventory (for the Pass-C map)

| Loop | Chain (cited) | Damper | Cap / bound | Verdict |
|---|---|---|---|---|
| **MS / threadwork** | tearing ops → Gaps/Locks → per-season MS drain → Fractured spontaneous Gaps → more drain | Force 1 baseline-positive ∝ disruption; WC2 halves; Mending | −10/s net cap (contested); Gap self-close 2/4/8/32s | **Bounded** (intrinsic + cap) |
| **Faction-collapse** (cross-system) | Stability 0 → collapse → territory loss → muster → military → instability | Stability recovery +1/s (§1.3) | Survival Exception once/campaign; **reconstitution ≠ extinction** (§1.5 → settlement §6.2); **Military stat sticky** (military §1.7) | **Bounded — CORRECTS diagnostic hypothesis** (was "undamped terminal, no cap"; it is not) |
| **L-CONV** conviction crisis | Scar → crisis → arc transition → multi-Conviction cascade | 1 Scar/season cap; structured-concentration weights (taxonomy §4) | per-Conviction thresholds; cascade needs simultaneous crises | Bounded single-path; cascade tail `[INTENT UNDETERMINED]` |
| **L-DEFECT** npc defection | sworn/liege break → tier-1/2/3 strain cascade → faction-Cascade decrement | strain −1/s; half-rate spillover; valence-isolated; tier-3 rare | strain tiers | Topologically damped **but resolution UNBUILT** (B1.2, §7 hooks-only) |
| **L-SPLIT** succession split | leader vacancy → contest → narrow margin → faction splits → recursive | re-merge at Mandate 3+ | RM emergence 4-season cooldown (untuned) | Bounded; cooldown PROVISIONAL |
| **L-INSURG** GD-3 pipeline | RM PT decay → piety↓ → Latent → Insurgency → Promoted Faction → territorial deltas | suppression Stage 2→1; sustained-2-season gate | Legitimacy thresholds; **Stage 3/4 dissolution UNSPECIFIED** | Up-path defined, **down-path absent** |
| **mass-battle morale** (sub) | rout → contagion −1 Morale adjacent → … | rout contagion **braked** (no further cascade/turn); rally/reform recover | per-turn cap | **Bounded** (confirms prior read) |
| **L-MIRACLE** Solmund RWCE | miracle → Accord +1 (one-time) + SA → Church recognition → SA-gated actions → CI/PI; TD counter | one-time Accord; TD penalises asserter | SA-gated | Bounded; the positive rendered-world pole of the Force-3 spectrum |

---

## 5. Findings / ED-candidates (consolidated; B6-blocked → `[DRIFT]`, staged)
- **P1** — seasonal MS cap contradiction (params struck vs §5 ±10). *Owner decision.*
- **P2** — `npc_relational_graph` defection cascade resolution UNBUILT (B1.2 §7 hooks-only). *Needs PP.*
- **P2** — `insurgency_pipeline` Stage 3/4 dissolution UNSPECIFIED. *Owner authors (INSURGENCY-DISSOLUTION-001).*
- **GAP** — Second-Calamity terminal (10 seasons MS≤5) + baseline-decay rate not in MS design docs. *Formalize.*
- **DRIFT-1** — RS/MS label unpropagated (params/threadwork, calamity_infill use RS; main docs use MS). *Propagate ED-731.*
- **DRIFT-2** — Gap-bleed model inconsistent (per-scale 1/2/3/5 vs flat −4). *Reconcile.*
- **DRIFT-3** — `calamity_radiation` cross-refs stale `threadwork_redesign_v25 §5.3` (now `threadwork_v30 §5`). *Repoint.*
- **DRIFT-4** — `conviction_track_v1` partially superseded (PP-717); current taxonomy in `conviction_taxonomy_v30`. *Conviction loop split across 3 docs.*

---

## 6. Pass C plan (next)
Inputs now complete (modulo the Second-Calamity GAP + faction-system remainder). Pass C:
1. **Rebuild the loop map** from §4 — supersede the old W-series; replace the mis-grounded W1 with the corrected bounded faction-collapse loop; add L-CONV/DEFECT/SPLIT/INSURG/MIRACLE + mass-battle sub-loop.
2. **Re-anchor the scale ladder** to canon's named scales (DC-7): Object · Personal · Relational · Field · Structural · Foundational (threadwork depths) ↔ personal/settlement/territory/peninsula (play scales).
3. **Per-system NERS** on complete reads: faction-collapse loop **passes R** (do NOT add Lesson 5); faction-action **small-pool bare-stat roll still fails R** (Lesson 3) — distinct from the loop; L-DEFECT/L-INSURG **fail R on incompleteness**, not instability.
4. **Fold DC-1..12** + the two-force MS model + the Force-3 bound.
5. **Validate arc length** with a Monte-Carlo run (mc engine): does MS reach the Critical band on the intended civil-war→invasion→unification timescale under plausible play intensity, winnable on maintain?
