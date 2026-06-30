# Combat Engine v1 — Comprehensive NERS Audit (All Directions)

**Scope:** the personal-combat engine as built — `combat_engine_v1/` (core resolver delegation, net_sigma
composition, armour/damage model, the six subsystem modules, the geometry layer) **plus** the required-module
question raised by the HEMA/academic gap analysis (initiative, contratempo, stringer/disengage, armour energetics).
**Instrument:** `valoria-resolution-diagnostic` (Stage 0–4, Phase 0–6, P-i…P-v, six lessons) + canonical NERS
(N/R/S/E) + the six directions (top-down / bottom-up / vertical / diagonal / lateral / horizontal).
**Date:** 2026-06-02 · **HEAD:** (committed through 36abf82) · **Method:** bottom-up from fetched committed source.

`[READ: skills/valoria-resolution-diagnostic/SKILL.md (full — engine instances A/B/C, P-i..P-v, Stage 0–4, six
lessons, decision rule); designs/audit/2026-05-30-lps-mandate-ners-audit/lps_mandate_comprehensive_ners_audit.md
(prior NERS format + axis usage); references/canonical_sources.yaml + roadmap_state.yaml (NERS history, combat_v32
status); designs/scene/combat_engine_v1/{core,combatant,config,systems,tradition,wrapper,geometry}.py (committed)]`

`[SELF-AUTHORED — bias risk]` Every module audited here was built by me across this session. Counter-measures:
the resolver-delegation claim is checked against the actual `core.py` calls (not assumed); the clinch revert and the
two flagged emergent cells (rapier-high, longsword-low unarmoured) are reported as live N/R reservations against my
own work; the geometry layer (my most recent addition) is the one most scrutinised for E (added apparatus).

`[GAP: canonical NERS wording — canon/definitions.yaml not reachable in this index (404); axis criteria reconstructed
from the resolution-diagnostic skill's Stage-3 table + the prior audit's Stage-3 block, which are authoritative and
mutually consistent. Treat the N/R/S/E pass-tests below as faithful-but-reconstructed.]`

---

## VERDICT (worst-first, no false balance)

**NERS-COMPLIANT AS BUILT for the resolution + physical-substrate layer — no hard mechanical defect.** The combat
engine does **not** reimplement resolution: `core.effective_ob`/`core.roll_net` delegate to the ratified
sigma-leverage continuous engine (Instance A), so P-i…P-v are **inherited**, and the audit's real surface is what the
combat layer *adds* (net_sigma composition, armour/damage, derived surfaces). That added surface holds at its
extremes (95% upset cap verified; armour monotonic [51,57,75,91]; no-one-shot 18<24; no unbounded loop).

**The one material NERS finding is N (Necessary), and it is an N-of-omission, not redundancy:** measured against the
literature the engine is built to model, **a required module is missing — INITIATIVE (Vor/Nach/Indes)** — the single
most-emphasised concept in the source corpus. Two further required modules (contratempo/single-time counter;
stringer+disengage) are partial/missing. These are *completeness* gaps in the modelled domain, not defects in what
exists. Four items need a Jordan call; none blocks the existing engine.

---

## PHASE 0 — COMPONENT CLASSIFICATION (scope gate + engine-selection; the spine of the audit)

The engine is a **composite**. Classify each component, then diagnose only what this instrument scopes (rolling
parts via P-i…P-v); recognise-and-route the rest (deterministic/derived) so a derived table is not mis-flagged as a
resolver cliff.

| Component | Category | Engine | In NERS scope here |
|---|---|---|---|
| `core.effective_ob` / `roll_net` / `degree` | **Rolling engine (delegated)** | **Instance A** (sigma-leverage continuous) | inherited — verify delegation only |
| `net_sigma` composition (wrapper sums module σ) | **Roll input** (assembles the Δσ the engine consumes) | feeds A | **yes** — the combat layer's real σ surface |
| `coupling`/`damage`/`RESIST` (armour transmit) | **Deterministic accounting** (post-resolution magnitude) | none (no draw) | recognise; check S/R (bounds, monotonic) |
| `GEOMETRY` → `geometry.bake` surfaces (gap/thrust/cut/perc) | **Derived base-parameter composite** (precomputed) | none | recognise; check N (redundancy) + E |
| `WEAPONS` attribute table (reach/wt/head/gap/percussion/clinch) | **Base parameters** (roll inputs) | none | recognise; check N (overlap) |
| `config.py` tunables (weights/thresholds) | **Base parameters** (calibration) | none | recognise; flag `[OPEN — calibration]` |
| Engagement state machine (measure/approach/close/reopen) | **Deterministic control flow** + event gates | drives A per beat | recognise; check R (loop bounds) |
| `tradition` channel-weights + familiarity | **Derived modifier** on reads | feeds A | recognise; check N/S |
| Upset cap (95%) / Ob-floor | **Bound** | guards A | **yes** — P-iii/P-iv |

**Scope-gate result:** one delegated rolling engine (A) + a rich roll-input/deterministic-accounting/derived-surface
composite. No second rolling engine, no card/timing draw → **no Instance C**. The legacy raw-d10 success-pool is
**not** used (correct; videogame path is A).

---

## STAGE 1 — DIAGNOSTIC (Phase 1–6), rolling surface

**Engine-selection (Phase 0 rule):** personal combat pools are healthy (~5–18D) with a genuine setup/skill axis →
**Instance A is the correct engine.** Not bare-stat-pivotal (so not B); not aggregable-to-reduce (already healthy);
not a shallow clock. Correct engine for the regime (Lesson 3 ✓).

**P-i (modes agree / fidelity).** Resolution is delegated to A; the combat layer adds no parallel odds computation.
*Inherited caveat:* A's **continuity correction (`net − (Ob−0.5)`, ER-2) is "recommended, not yet landed"** in
`params/core.md`. Personal combat runs ~5–18D where the effect is small, but sub-~5D exchanges (a brief stop-hit
resolved on a thin pool) would inherit the 4–32% TTRPG/videogame divergence. **Finding F-i (low, inherited):** carry
the engine-level continuity-correction `[OPEN]`; verify combat never resolves a pivotal sub-5D draw without it.

**P-ii (leverage uniform across the whole range).** The combat layer expresses every advantage as **Δσ summed into
net_sigma**, then hands it to A, whose Δσ→Ob-shift is pool-size-uniform by construction. The combat layer respects
this (it never scales dice count for advantage). **Pass** — but the *verification obligation* (Lesson 2) applies: the
**number of σ contributors is large** (reach, tempo, leverage, mode, bind, adef, legibility, clinch-data, geometry),
and their **sum** could in principle push net_sigma into A's tanh-saturation at the extremes. Verified empirically:
mirror ≈ 50, mastery H6v3 ≈ 78, spear>dagger ≈ 94, and the 95% cap holds at n≥4000 → the summed σ stays in-band.
**Pass (flag):** keep the aggregate-σ band under test when new σ modules are added (initiative will add one).

**P-iii (bounded, continuous; no stacked cliffs; Ob-floor).** Armour transitions are **monotonic and continuous**
([51,57,75,91] across seeds) after the F2 + light-rung fixes (the light→medium cut-transmit cliff was explicitly
removed; cut_thrust takes best-of-mode at every level). The upset cap saturates at 95% (does not violate via an
Ob-shift below floor — it caps probability, not Ob). **Pass.** *Watch:* the percussion `perc/8` and geometry `gap`
scalings are continuous multipliers (no thresholds) → no new cliff introduced. **Pass.**

**P-iv (graded, recoverable; residual failure).** Output is the four-degree ladder (Overwhelming/Success/Partial/
Failure) with the 95% cap guaranteeing ≥5% residual upset even at max overmatch — exceeds the resolver's ≥3% norm.
No fragile binary; the no-one-shot rule (max blow 18 < End-2 Health 24) keeps a single exchange recoverable.
**Pass.**

**P-v (right engine for the pool).** Covered in Phase 0 — Instance A is correct for healthy combat pools. **Pass.**

**Phase 4 — loops the engine drives.** Engagement state machine: measure→approach→close→(event-gated)reopen. The
reopen is **event-gated**, not free, and fatigue is monotone-draining → no undamped+unbounded loop. Feint is
**capped (max streak 3) and readable** → bounded. **Pass (Lesson 5).** *Note:* if initiative is added as a
self-reinforcing "whoever has the Vor keeps winning" state, it is a **positive feedback loop** and must ship with a
sized safeguard (lose-the-Vor conditions) — flagged pre-emptively for the build.

**Phase 5 — intent gate.** Every discontinuity examined is deliberate with an adequate safeguard (armour caps,
upset floor, feint cap, no-one-shot). No accidental cliff found.

**Stage-1 findings (worst-first):**

| Finding | Component | Engine | Property | Stress | Severity | Intent |
|---|---|---|---|---|---|---|
| F-i continuity correction not landed (inherited) | core delegation → A | A | P-i/P-iii | sub-5D pivotal draw | low | `[OPEN engine-level]` |
| F-ii aggregate-σ saturation watch as modules grow | net_sigma sum | A-input | P-ii | many summed Δσ at extremes | low | in-band now (verified) |

No P-level **defect** in the combat layer; both findings are watch-items, one inherited.

---

## STAGE 2 — LESSON MAPPING
- F-i → **Lesson 6** (continuity correction present): inherited engine `[OPEN]`; combat remedy = ensure no pivotal
  sub-5D combat draw resolves without it (or keep combat pools ≥5D, which they are by construction).
- F-ii → **Lesson 2** (verify leverage in-band across the whole range): standing obligation; re-run the cap/mirror/
  mastery invariants whenever a σ module is added.
- *(No Lesson-1/3/4/5 defect: roles are not conflated, engine is correct for the regime, no disguised-binary clock,
  no undamped loop.)*

---

## STAGE 3 — NERS VERDICT

```
ENGINE: Combat Engine v1 (personal combat)
INSTANCE: A (sigma-leverage continuous, delegated) + deterministic-accounting/derived composite
COMPONENTS: core delegation to A · net_sigma σ-sum · armour/damage accounting · geometry-derived surfaces ·
            weapon base params · engagement state machine · tradition modifiers · upset cap/Ob-floor
VERDICT: NERS-COMPLIANT AS BUILT (resolution + physical substrate) — no hard mechanical defect.
         ONE material finding: N-of-omission (a required module, INITIATIVE, is missing). 4 items for Jordan.

N (Necessary): PASS for what exists (flag) — no redundant roll; resolution correctly delegated (not reimplemented),
   so no duplicate engine. Geometry SUBSUMES the hand-set `gap` (replaces it, not parallel to it) → not redundant.
   FLAGS:
     • [N-OMISSION, P1-for-scope] REQUIRED MODULE MISSING — INITIATIVE (Vor/Nach/Indes). The literature's #1
       concept; the engine models the bind's Stark/Schwach and momentary aggressor but not initiative as a
       persistent, seizable, *stealable* state, and Indes is absent. This is the audit's headline gap.
     • [N-PARTIAL, P2] CONTRATEMPO / single-time counter + body-void: partial (2-tempo riposte + approach stop-hit
       only); no one-tempo line-closing counter, no body void (passata sotto/inquartata).
     • [N-PARTIAL, P2] STRINGER + DISENGAGE (cavazione/durchwechseln): missing pre-attack blade engagement and
       bind-escape; spans both schools.
     • [N-WATCH] clinch attribute present as inert data (built+reverted twice as a global term). Not redundant
       (unused), but either wire it as a TARGETED rule or drop the attribute to keep N clean.
     • [N-WATCH] WEAPON base params vs GEOMETRY: `head` category + geometry now both inform cut/thrust; once
       curvature→cut/thrust is CONSUMED, verify `head` is not double-stating what geometry derives (collapse if so).

R (Robust): PASS — holds at extremes: upset cap 95% verified n≥4000; armour monotonic [51,57,75,91] across seeds;
   no-one-shot 18<24; no fragile binary (graded ladder); loops bounded (event-gated reopen, capped feint, draining
   fatigue); geometry/percussion scalings are continuous (no new cliff). The light→medium cut cliff was removed (F2).
   INHERITED WATCH: A's continuity correction not yet landed (F-i) — immaterial at ≥5D combat pools, real sub-5D.

S (Smooth): PASS — scales cleanly settlement-of-concern (exchange → fight → match) and is consistent with the
   deterministic spine it sits on (it feeds A; it does not roll on a deterministic ledger — the faction layer's old
   S-failure is absent here). Armour rollup consistent across states; damage accounting consistent with the σ result.
   NOTE: the geometry bake is the one non-trivial derivation link, but it is build-time and reproduces the validated
   tiers (max gap Δ 0.12) → no scale inconsistency.

E (Elegant): PASS (reservation) — the resolver path is legible (delegated A; player reads odds off the σ).
   RESERVATION: the engine is now LARGE (six modules + a geometry layer with five geometric params/weapon feeding a
   bake). Direction is intuitable (longer reach helps; curved cuts better/thrusts worse; steel beats wood on plate);
   MAGNITUDE is not player-facing (the σ weights, the bake constants, K-like coefficients). This is the elegance cost
   of physical fidelity — acceptable for a simulation engine, but the least-elegant aspect. Adding initiative/
   contratempo must not bolt on apparatus beyond what the concept needs (E discipline).

REMEDIATION (worst-first):
  P1 [N-OMISSION]  Build INITIATIVE (Vor/Nach/Indes) as a persistent, seizable, stealable state conferring a standing
                   σ edge while held; lost by over-commit / being-read / losing the bind; stolen Indes by winning the
                   read in the opponent's tempo. SHIP WITH A SIZED SAFEGUARD (it is a positive feedback loop —
                   Lesson 5): bound how long the Vor persists / how much edge it confers so it cannot snowball.
  P2 [N-PARTIAL]   CONTRATEMPO: add a single-tempo line-closing counter + a body-void defence (distinct from
                   weapon-parry), gated on reading a committed/over-extended attacker. Reuse the displacement hook.
  P2 [N-PARTIAL]   STRINGER + DISENGAGE: a pre-attack "gain the line" action (raises attack safety, opposed by
                   disengage) + a `disengage` out of an unfavourable bind at a tempo cost.
  P3 [N-WATCH]     Resolve the clinch attribute: wire as a TARGETED pure-reach-vs-clinch rule OR remove the inert
                   attribute. (Global clinch term twice shown net-negative — do not re-add globally.)
  P3 [E/N-WATCH]   When curvature→cut/thrust is consumed, audit `head`-category vs geometry for double-statement;
                   collapse the redundant one. Keep the geometry bake as the single source for cut/thrust/gap.
  P3 [R, inherited] Land A's continuity correction (`net − (Ob−0.5)`) at engine level, or assert combat pools ≥5D.
  --- separately tracked (validation, not NERS-structural): rapier over-strong unarmoured (~82), longsword
      under-valued unarmoured (~41); armour energetic cost (Jaquet) absent → cheap, grounded endurance refinement.
```

---

## ALL-DIRECTIONS COVERAGE
- **Top-down** (emergent tiers vs intent/history): sound except the two flagged unarmoured cells; not a NERS-structural defect.
- **Bottom-up** (each primitive physically correct): reach, leverage, armour-defeat, geometry — verified from source.
- **Vertical** (exchange → fight → match): consistent (the σ result drives degree drives damage drives Health).
- **Diagonal** (armour × weapon interaction): monotonic rotation cuts→percussion/thrust as armour rises; verified.
- **Lateral** (weapon vs weapon within a state): tier-list historically validated; lopsided matchups are correct.
- **Horizontal** (combat layer ↔ canonical engine / other systems): clean — delegates to A; no dice-on-ledger; the
  one cross-system loop risk (initiative as feedback) is pre-flagged for its build.

## PROVENANCE
`[READ: resolution-diagnostic SKILL.md full; prior NERS audit; canonical_sources + roadmap; all 7 committed engine
modules]` · `[VERIFIED: this session — resolver delegation in core.py; upset cap n≥4000; armour monotonicity 3 seeds;
no-one-shot; geometry reproduces validated tiers]` · `[CONFIDENCE: high on structure + the N-omission headline;
medium on the exact canonical N/R/S/E wording (definitions.yaml unreachable — reconstructed from skill + prior audit,
which agree)]`
