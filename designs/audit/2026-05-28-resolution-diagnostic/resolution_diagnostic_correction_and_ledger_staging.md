# Resolution Diagnostic + Engine Reconciliation — Correction & Ledger Staging

**Date:** 2026-05-28
**Session:** c93a36df
**Purpose:** Single closeout note for the 2026-05-28 audit work. (1) Corrects defects now live on `main` in the committed diagnostic files. (2) Records the self-review's load-bearing findings. (3) Stages all P1 editorial-ledger candidates with pre-assigned IDs for ingestion — **not** appended directly to `canon/editorial_ledger.yaml` because the `2026-05-XX-editorial-ledger-consolidation` handoff is active and a direct write would collide.
**Bias:** `[SELF-AUTHORED — bias risk]` on all referenced artifacts (diagnostic batches 1–2, engine assessments v1+v2). Two of the corrections below fix my own arithmetic errors.

> **UPDATE 2026-05-28 (post-Jordan ruling on F2):** Jordan confirmed **`Ob = floor(stat/2)+1` is the canonical, always-intended Domain Action Ob**; the `faction_layer` "Ob = target stat directly" reading is the stale one. This **resolves ED-866** and **materially downgrades the faction severity** in the less-severe direction. Corrected numbers and revised ledger entries below (see §1a and the amended ED-865/ED-867/ED-868). The catastrophic "weak factions cannot act / deterministic collapse" framing is **retracted**; a narrower smoothness finding survives. The pre-update text is retained for trail; §1a is authoritative where it conflicts.

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

## §1a — Faction severity, re-derived under canonical Ob = floor(stat/2)+1 (AUTHORITATIVE)

Jordan ruled F2: **`Ob = floor(stat/2)+1` was always intended.** Re-derivation (MC 400k, authoritative die rule, μ/die sanity 0.40):

**Success matrix — acting-faction stat (= pool) × target stat (sets Ob):**

| Target (Ob) | 1D | 2D | 3D | 4D | 5D | 6D | 7D |
|---|---|---|---|---|---|---|---|
| stat 1–2 (Ob 1–2) | 0.40 / 0.10 | 0.58 / 0.26 | 0.68 / 0.40 | 0.75 / 0.51 | 0.80 / 0.60 | 0.84 / 0.67 | 0.86 / 0.73 |
| stat 3 (Ob 2) | 0.10 | 0.26 | 0.40 | 0.51 | 0.60 | 0.67 | 0.73 |
| stat 4–5 (Ob 3) | 0.00 | 0.07 | 0.17 | 0.28 | 0.38 | 0.47 | 0.55 |
| stat 6–7 (Ob 4) | 0.00 | 0.01 | 0.05 | 0.12 | 0.20 | 0.28 | 0.36 |

**What the ruling fixes (severity DOWN):**
- A weak faction (Mil-2 → 2D) acting against a **typical peer** (target stat 2–3, Ob 2) succeeds **~26%**, not ~7% and not zero. Bottom-tier factions **can** function. The catastrophic framing is **retracted** — it was anchored to the wrong (target-stat) Ob.
- Ob now compresses into a **1–4 band** (not 1–7), so no faction faces an Ob it structurally cannot meet against same-or-weaker opponents.

**What survives (the narrower, real finding):**
- **Punching-up is near-impossible.** Weak faction (2D) vs strong target (stat 6–7, Ob 4) = **1%**. A small faction effectively cannot act on its strongest rivals — bounded by design or a defect, Jordan's call, but it is a real asymmetry.
- **Jagged even/odd peer matchups (smoothness defect).** Ob steps only at even stat boundaries (`floor(2/2)+1 = floor(3/2)+1 = 2`), so the **symmetric** (equal-stat) matchup is **non-monotonic**: stat-2-vs-peer = 0.26 but stat-3-vs-peer = 0.40. Equal-strength factions have materially different odds of affecting each other depending on which even/odd tier they occupy. This is a genuine NERS-S (smoothness) finding independent of pool size.
- **No Pool Floor / small-pool variance unchanged.** `floor(stat/2)+1` lowers the *target*, not the *variance*; a single die still swings pivotal 2D outcomes. The ED-865 finding survives **as a calibration+variance issue, not a death-spiral.**

**F3 (anti-death-spiral floor) — substantially downgraded, arguably closed.** Under canonical Ob, a Stab-2 faction Accounting Check is 2D vs Ob 2 = **~26% pass**, not the ~1% I reported under the erroneous "Ob capped at 4" reading. That is a meaningful per-season recovery chance — **the floor is functional, not inert.** The "mathematically inactive safeguard" finding was an artifact of the wrong Ob. **Retracted; F3 closed pending confirmation the Accounting Check uses the same Ob formula.**

**Net corrected faction verdict:** still **NON-COMPLIANT**, but on narrower grounds — NERS-S (jagged even/odd peer interaction) + NERS-R (punching-up wall + no variance floor) — **not** the catastrophic "weak factions are doomed" basis originally stated. The fix is calibration/aggregation (smooth the Ob curve so it's monotonic in target strength; add a variance floor), **not** rescue-from-collapse.

---


**Why staged not filed:** `2026-05-XX-editorial-ledger-consolidation` handoff is active (orchestrator editing `canon/editorial_ledger.yaml`). Direct append would collide. These entries are pre-assigned from **ED-865** (live ledger ends at ED-864) for the consolidation owner to ingest. Schema mirrors existing entries; `type`/`archetype` subject to consolidation normalization. **ED-841 is NOT re-filed (C-4).** Mass-battle MB1–MB4 / MB9 are NOT re-filed (already in the 2026-04-29 pipeline / ledger).

```yaml
# Stage into canon/editorial_ledger.yaml during active consolidation.
# Source session: c93a36df (2026-05-28 resolution diagnostic + engine reconciliation).

- id: ED-865
  date: 2026-05-28
  description: 'Faction Domain Action resolves on a BARE faction-stat d10 pool (1-7D) with no
    Pool Floor. Under CANONICAL Ob = floor(target_stat/2)+1 (Jordan-confirmed; supersedes the
    stale "Ob = target stat" reading), the catastrophic case is averted: Mil-2 (2D) vs a peer
    (Ob 2) = 0.26. But two real defects survive: (a) NERS-S - the success curve is NON-MONOTONIC
    in target strength because Ob steps only at even boundaries (stat-2-vs-peer = 0.26 but
    stat-3-vs-peer = 0.40), so equal-strength factions interact with jagged, tier-dependent
    odds; (b) NERS-R - punching-up is near-impossible (2D vs stat-6/7 target, Ob 4 = 0.01) and
    small-pool variance is unbounded (one die swings pivotal 2D outcomes). Fix is CALIBRATION +
    aggregation (smooth Ob to be monotonic in target strength; add a variance floor or aggregate
    the pool per ER-9), NOT rescue-from-collapse. Earlier "weak factions cannot act /
    deterministic" framing RETRACTED (was anchored to wrong Ob).'
  severity: P2
  type: design_defect
  affected_docs: [designs/provincial/faction_layer_v30.md, params/factions/stats_1_7_scale.md]
  status: open
  jordan_decision: pending
  source: resolution_diagnostic F1 / engine_reconciled ER-1 (severity corrected post-F2-ruling)

- id: ED-866
  date: 2026-05-28
  description: 'RESOLVED 2026-05-28 (Jordan): faction Domain Action Ob = floor(stat/2)+1 was
    always the intended formula. The faction_layer design-doc "Ob = target stat directly"
    reading is the STALE one and should be corrected to match params/factions. Action: align
    faction_layer Ob language to floor(stat/2)+1; no open decision remains. Resolution
    materially downgraded the severity of ED-865 and effectively closed the F3 finding
    (ED-867).'
  severity: P1
  type: contradiction
  affected_docs: [designs/provincial/faction_layer_v30.md, params/factions.md]
  status: resolved
  jordan_decision: 'floor(stat/2)+1 canonical (2026-05-28); fix faction_layer to match'
  source: resolution_diagnostic F2

- id: ED-867
  date: 2026-05-28
  description: 'RESOLVED/CLOSED 2026-05-28 by the F2 ruling. The anti-death-spiral floor was
    flagged "mathematically inert" ONLY under the erroneous "Ob capped at 4" reading (Stab-2
    2D vs Ob 4 = 0.01). Under canonical Ob = floor(stat/2)+1, the Stab-2 Accounting Check is
    2D vs Ob 2 = ~0.26 - a meaningful per-season recovery chance. The floor is FUNCTIONAL,
    not inert. Earlier finding was an artifact of the wrong Ob; RETRACTED. Confirm only that
    the Accounting Stability Check uses the floor(stat/2)+1 formula; if so, no action.'
  severity: P3
  type: verification
  affected_docs: [designs/provincial/faction_layer_v30.md]
  status: resolved
  jordan_decision: 'closed by floor(stat/2)+1 ruling; confirm Accounting Check uses same Ob'
  source: resolution_diagnostic F3 (retracted post-F2-ruling)

- id: ED-868
  date: 2026-05-28
  description: 'Faction collapse cascade loops. L1 collapse loop terminates at Stability 0 =
    extinction (a termination, not a recoverable bound); L7 Wealth-0 -> Military-1/season is
    undamped on the Military dimension; decrease>increase asymmetry on Stability. Under
    canonical Ob = floor(stat/2)+1, the per-gate recovery odds are HEALTHIER than first
    reported (e.g. Stab-2 Accounting recovery ~0.26, not ~0.01), so the slide is clearly
    PROBABILISTIC and recoverable in the common case - NOT deterministic (earlier
    "deterministic" wording RETRACTED). Residual structural finding: the terminal state is
    still extinction (no bound short of it) and the Military-side cascade still lacks a damper.
    Fix: a bound short of extinction + a Military-side recovery path; lower priority than first
    assessed.'
  severity: P2
  type: design_defect
  affected_docs: [designs/provincial/faction_layer_v30.md, designs/provincial/military_layer_v30.md]
  status: open
  jordan_decision: pending
  source: resolution_diagnostic F5/F6/F7 (severity corrected post-F2-ruling)

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
