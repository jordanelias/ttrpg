# Resolution Diagnostic + Engine Reconciliation — Correction & Ledger Staging

**Date:** 2026-05-28
**Session:** c93a36df
**Purpose:** Single closeout note for the 2026-05-28 audit work. (1) Corrects defects now live on `main` in the committed diagnostic files. (2) Records the self-review's load-bearing findings. (3) Stages all P1 editorial-ledger candidates with pre-assigned IDs for ingestion — **not** appended directly to `canon/editorial_ledger.yaml` because the `2026-05-XX-editorial-ledger-consolidation` handoff is active and a direct write would collide.
**Bias:** `[SELF-AUTHORED — bias risk]` on all referenced artifacts (diagnostic batches 1–2, engine assessments v1+v2). Two of the corrections below fix my own arithmetic errors.

---

## §1 — Corrections to committed artifacts

### C-1 — Stale batch-1 README (M8)
`resolution_diagnostic_README.md` (committed `05f523a3`) states: *"Stages 1–4 complete for 4 of 7 systems… remaining 3 deferred to follow-up session."* **This is stale.** All 7 systems were completed in the same session; batch 2 (`76bdf99`) shipped social / investigation / peninsula-victory. The batch-1 README was never updated. Authoritative status: **7 of 7 complete.** `resolution_diagnostic_README_batch2.md` carries the correct cross-system summary.

### C-2 — Faction F1 / F3 probabilities were wrong, twice (M1 empirics)
The committed faction files cite F1 ≈ **P 0.16** and a later pass asserted **P 0 / "deterministic death spiral."** **Both used a simplified "die ≥ 7 = +1 success" model** that ignores the authoritative rule (face 1 = −1, face 10 = +2). Corrected under the real rule (`params/core.md`, Monte Carlo 300k, μ/die sanity-checked to 0.3999 vs spec 0.400):

| Finding | Stated (wrong) | **Corrected (authoritative die rule)** |
|---|---|---|
| F1: Military-2 → 2D vs Ob 3 | 0.16 / 0 | **0.070** |
| F1: Military-2 → 2D vs Ob 4 (design-doc Ob = target stat) | 0.16 / 0 | **0.010** |
| F3: Stab-2 → 2D vs Ob 4 (anti-death-spiral cap) | "structurally unreachable / 0" | **~0.010** (effectively inert, not literally unreachable) |
| Contrast: healthy Mil-5 → 5D vs Ob 3 | — | 0.381 |

**Qualitative findings stand** — a ~7% bare-stat pivotal action is degenerate, and a ~1%-pass "safeguard" is inert. But the severity language was overstated: the faction collapse is **probabilistic and heavily loss-weighted, not deterministic.** Earlier "deterministic" wording (F6/F7 last pass) is retracted.

### C-3 — NERS verdict rubric is ambiguous; "broadly compliant" overstated (M1)
The skill says a system is NERS-compliant *only when it passes all four* criteria, and defines **Smooth** as "calculations consistent in methodology with other mechanics" — yet *also* scopes consistency-checking out ("that's `valoria-mechanic-audit`'s job"). These conflict. A canon contradiction is simultaneously an S-failure (by the rubric) and out-of-scope (by the disclaimer). My verdicts silently picked the lenient reading via the undisclosed phrase "under resolution-fitness lens."

`[GAP: NERS-S scope — does Smooth include canon-consistency? Skill is internally contradictory. Jordan ruling required; it swings the tally.]`

- **Lenient reading** (S = resolution-smoothness only): **6/7 compliant**, faction non-compliant.
- **Strict reading** (S includes consistency): **2/7 compliant** (social, investigation); 5/7 non-compliant — but of those 5, **1 is mechanically broken** (faction) and **4 are mechanically sound but documentation-inconsistent** (combat, threadwork, mass battle, peninsula). Different remediation classes; do not collapse.

The committed READMEs' headline "broadly NERS-compliant, 6 of 7" should be read with this ambiguity attached.

### C-4 — T6 (Knot TIER-DRIFT-001) was already ledgered (M6/M3)
The threadwork verdict surfaced T6 as a cross-system finding. **It is already tracked as ED-841** (confirmed present in `canon/editorial_ledger.yaml` this session). Over-claim of novelty **retracted.** Do **not** file a duplicate; the threadwork verdict's cross-system impact note remains useful annotation on the existing ED-841.

### C-5 — C2 (PP-717 D2 Pool DR propagation) confirmed live
Verified this session: both `designs/scene/combat_v30.md` and `params/combat.md` still carry the pre-PP-717 `(Agility × 2)` formula and contain no Pool DR term. The propagation gap is open **as of today**, not merely as of the historical audit. Finding stands at full strength.

### C-6 — ER-2 closed; engine verdict firmer
The reconciled engine assessment (`engine_replacement_audit_reconciled` → committed `56e83862`) closes the v1 P1 (ER-2): discrete↔continuous engines diverge 2.7–4.4× below 5D, but the divergence is a **missing continuity correction** (`Ob − 0.5` restores agreement to within ~few % at 2D), not a CLT failure. ER-1 (resolver degeneracy) and ER-2 (engine fidelity) are **separable** with separate fixes; v1 had bundled them. Verdict unchanged: do not replace the engine.

### C-7 — Roadmap gap (flagged, not actioned)
Neither engine-side fix appears on `references/roadmap_state.yaml` (currently Phase 2). The continuity correction is a Phase-0-class one-line repair to `params/core.md`; the faction resolver redesign is a Phase-3/4 item gated on F2. **I am not editing the roadmap** — phase assignment is Jordan's call per the project-owner contract. Flagged for Jordan to slot.

---

## §2 — Editorial-ledger candidates (STAGED, pre-numbered; NOT appended)

**Why staged not filed:** `2026-05-XX-editorial-ledger-consolidation` handoff is active (orchestrator editing `canon/editorial_ledger.yaml`). Direct append would collide. These entries are pre-assigned from **ED-865** (live ledger ends at ED-864) for the consolidation owner to ingest. Schema mirrors existing entries; `type`/`archetype` subject to consolidation normalization. **ED-841 is NOT re-filed (C-4).** Mass-battle MB1–MB4 / MB9 are NOT re-filed (already in the 2026-04-29 pipeline / ledger).

```yaml
# Stage into canon/editorial_ledger.yaml during active consolidation.
# Source session: c93a36df (2026-05-28 resolution diagnostic + engine reconciliation).

- id: ED-865
  date: 2026-05-28
  description: 'Faction Domain Action resolves on a BARE faction-stat d10 pool (1-7D)
    vs Ob, statistically degenerate where stakes are highest. Military-2 faction = 2D:
    P(success) = 0.070 at Ob 3, 0.010 at Ob 4 (authoritative die rule, MC 300k). The
    only scale rolling bare small pools; every other scale aggregates or is deterministic.
    Fix: aggregate the pool (mass-battle summed-pool model, ER-9) OR deterministic+stochastic
    resolver (GD-2 mandate; CK3/EU/KoDP precedent). Resolver-design change at faction
    scale only; NOT an engine replacement. Prerequisite: ED-866 (Ob formula).'
  severity: P1
  type: design_defect
  affected_docs: [designs/provincial/faction_layer_v30.md, params/factions/stats_1_7_scale.md]
  status: open
  jordan_decision: pending
  source: resolution_diagnostic F1 / engine_reconciled ER-1

- id: ED-866
  date: 2026-05-28
  description: 'Faction Domain Action Ob formula contradiction. faction_layer design doc
    sets Ob = target stat directly; params/factions sets Ob = floor(stat/2)+1. The two
    give materially different degeneracy severities (design-doc: weak factions auto-near-fail
    above stat-2 targets). Determines the real severity of ED-865 and must resolve before
    the ED-865 resolver fix is specified.'
  severity: P1
  type: contradiction
  affected_docs: [designs/provincial/faction_layer_v30.md, params/factions.md]
  status: open
  jordan_decision: pending
  source: resolution_diagnostic F2 (prerequisite for ED-865)

- id: ED-867
  date: 2026-05-28
  description: 'Anti-death-spiral floor is mathematically inert. The Accounting Stability
    Check caps Ob at 4 for low-Stability factions as a safeguard, but a Stab-2 faction
    rolls 2D, which passes Ob 4 with P ~= 0.010. Capping the TARGET without raising the
    POOL is not a safeguard. Dissolved by the ED-865 resolver fix (aggregation raises the
    pool); standalone, the cap should raise the pool or convert to deterministic recovery.'
  severity: P2
  type: design_defect
  affected_docs: [designs/provincial/faction_layer_v30.md]
  status: open
  jordan_decision: pending
  source: resolution_diagnostic F3

- id: ED-868
  date: 2026-05-28
  description: 'Faction collapse cascade loops under-bounded. L1 collapse loop terminates at
    Stability 0 = faction extinction (a termination, not a recoverable bound); L7 Wealth-0 ->
    Military-1/season cascade is undamped on the Military dimension; decrease>increase
    asymmetry (multiple Stability-loss triggers vs +1 per clean season). Probabilistic and
    heavily loss-weighted (NOT deterministic - earlier "deterministic" wording retracted);
    every recovery gate is itself a small-pool roll (~1-7% at the floor). ED-865 resolver fix
    raises recovery odds; a bound short of extinction and a Military-side damper are the
    structural fixes.'
  severity: P1
  type: design_defect
  affected_docs: [designs/provincial/faction_layer_v30.md, designs/provincial/military_layer_v30.md]
  status: open
  jordan_decision: pending
  source: resolution_diagnostic F5/F6/F7 (consolidated; corrected severity)

- id: ED-869
  date: 2026-05-28
  description: 'PP-686 v2 stat-schema drift: a 6-stat schema reference persists where the
    canonical schema is 7 stats. Surfaced in faction-layer review; propagation incomplete.'
  severity: P1
  type: contradiction
  affected_docs: [designs/provincial/faction_layer_v30.md]
  status: open
  jordan_decision: pending
  source: resolution_diagnostic F8

- id: ED-870
  date: 2026-05-28
  description: 'PP-717 D2 (Pool DR above Agility 4) ratified in audit but NOT propagated to
    combat. combat_v30.md and params/combat.md both still carry pre-PP-717 (Agility x 2) and
    no Pool DR term (verified live 2026-05-28). Propagation gap open as of today.'
  severity: P1
  type: missing
  affected_docs: [designs/scene/combat_v30.md, params/combat.md]
  status: open
  jordan_decision: pending
  source: resolution_diagnostic C2 (currency-confirmed)

- id: ED-871
  date: 2026-05-28
  description: 'Mending Coherence cost contradiction. canon/02_foundations_amendment_leap_mechanism.md
    Amendment 3 states "Mending Coherence cost is zero" (structural consequence of restorative
    alignment); threadwork_v30 §3.2 lists "Mending | -1". Foundations supersedes design doc per
    project hierarchy; §3.2 row is stale. Blocks the Edeyja lifetime-Mending capability the
    Foundations explicitly argue for. Cross-check §31 for consistency on fix.'
  severity: P1
  type: contradiction
  affected_docs: [designs/threadwork/threadwork_v30.md, canon/02_foundations_amendment_leap_mechanism.md]
  status: open
  jordan_decision: pending
  source: resolution_diagnostic T1

- id: ED-872
  date: 2026-05-28
  description: 'Mass battle has no Pool Floor; unit deletion (Size->0) serves as the implicit
    floor. Pool = min(Size,Command)+Command floors at 2D (Cmd-1, Size-1) - same degenerate
    math as ED-865 (P(>=3 | 2D) ~ 0.07), unlike personal combat (floor 5) and threadwork
    (floor 5). The unit-deletion-as-floor choice is architecturally legitimate but silent in
    canon and not player-legible. Options: explicit Pool Floor; document + UI surface;
    Pool Floor = Command. Jordan-decision; do not prescribe.'
  severity: P1
  type: design_defect
  affected_docs: [designs/provincial/mass_battle_v30.md, params/mass_combat.md]
  status: open
  jordan_decision: pending
  source: resolution_diagnostic MB5 (novel)

- id: ED-873
  date: 2026-05-28
  description: 'Continuous (videogame) engine omits a continuity correction. Raw Normal(muN,
    sigma*sqrt N) P(success) runs 2.7-4.4x low vs discrete below 5D and 4-32% low even at
    validated 5-17D pools; net-(Ob-0.5) restores agreement to within ~1-3% across pools 1-17
    (MC 300k, 2026-05-28). One-line edit to params/core.md Continuous Engine. Closes prior
    ER-2 (downgraded P1->P3). No design risk; recommend apply.'
  severity: P3
  type: missing
  affected_docs: [params/core.md]
  status: open
  jordan_decision: pending
  source: engine_reconciled ER-2 (closed)

# --- P2/P3 secondary block (compact; consolidation may merge or defer) ---
- id: ED-874
  date: 2026-05-28
  description: 'Combat secondary canon items (consolidated): C3 out-of-bounds x Pool-Floor
    interaction underspecified; C5 Health super-linear at low Endurance; C6 Strength
    multiplier ambiguity. All P2; combat mechanically sound (PASS), these are
    consistency/clarity.'
  severity: P2
  type: clarity
  affected_docs: [designs/scene/combat_v30.md, designs/scene/derived_stats_v30.md, params/combat.md]
  status: open
  jordan_decision: pending
  source: resolution_diagnostic C3/C5/C6

- id: ED-875
  date: 2026-05-28
  description: 'Threadwork secondary canon items: T2 FR Coherence surcharge base table (min
    total -2) vs PP-196 PROVISIONAL (-1 at Object/Personal), both in canon; T7 COMPOSURE-
    DRIFT-001 articulation §2.4 cites "5 per ED-773" but ED-773 says 4. Both P2 canon
    cleanup.'
  severity: P2
  type: contradiction
  affected_docs: [designs/threadwork/threadwork_v30.md, designs/articulation/articulation_layer_v30.md]
  status: open
  jordan_decision: pending
  source: resolution_diagnostic T2/T7

- id: ED-876
  date: 2026-05-28
  description: 'Social contest: three pre-flagged 2026-04-08 stress-test items (D-01 genre
    weight 0.5 near-inert at R=1; D-04 Regroup-on-Spent dominant strategy; D-05 Focus-1
    Regroup trap) have UNVERIFIED post-patch status as of 2026-05-28. Action: verify against
    current canon (commit-log scan) before treating as open or closed.'
  severity: P2
  type: verification
  affected_docs: [designs/scene/social_contest_v30.md]
  status: needs_verification
  jordan_decision: pending
  source: resolution_diagnostic SC3/SC4/SC5

- id: ED-877
  date: 2026-05-28
  description: 'Engine cross-scale + settlement (consolidated): ER-3 pool-size shock (same 1-7
    stat -> 17D personal / 7D faction-bare / clocks) is engine-invariant and a scale-mapping
    decision; ER-6 settlement resolver unspecified (PENDING multipliers) risks importing the
    ED-865 bare-stat degeneracy - specify deterministic-first (ROTK/CK3 pattern).'
  severity: P2
  type: design_defect
  affected_docs: [designs/territory/settlement_layer_v30.md, designs/scene/derived_stats_v30.md]
  status: open
  jordan_decision: pending
  source: engine_reconciled ER-3/ER-6
```

---

## §3 — What is committed vs deferred

**Committed to `main` this session (4 commits):**
- `05f523a3` — diagnostic batch 1 (9 files)
- `76bdf99` — diagnostic batch 2 (5 files)
- `56e838628` — reconciled engine assessment (1 file)
- this note — corrections + staged ledger candidates

**Deliberately NOT committed (flagged):**
- **Direct append to `canon/editorial_ledger.yaml`** — blocked by active `2026-05-XX-editorial-ledger-consolidation` handoff. 13 candidates staged above (ED-865–ED-877) for the consolidation owner to ingest. ED-841 not re-filed; mass-battle 2026-04-29 items not re-filed.
- **In-place edits to the 6 verdict files** — superseded by §1 corrections per repo supersession convention; editing large committed files in place is higher-risk and not warranted.
- **Roadmap edits** — phase assignment for ED-865 (resolver) and ED-873 (continuity) is Jordan's call (C-7).

`[CONFIDENCE: high]` — §1 corrections (all trace to verified data: live file greps, MC with sanity-checked die rule, confirmed ED-841 presence, confirmed active handoff). `[CONFIDENCE: medium]` — ledger candidate `type`/`archetype` fields (consolidation will normalize); the F2-dependent severity of ED-865 until ED-866 resolves.
