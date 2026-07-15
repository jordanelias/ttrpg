# Refutation lane — v2 CHURN engine · DETERMINISM + COST axes

## Status: SUPERSEDED (working record of the emergent-narrative-engine design effort; head RATIFIED as ../narrative_engine_design_v2_churn.md + narrative_engine_design_v1.md-as-amended + spec/churn_amendments.md, ED-IN-0011, 2026-07-05). Not independently ratifiable; retained as record. [status reconciled 2026-07-15, proposal-reconciliation pass, ED-IN-0068]
_Skeptic lane, 2026-07-05, working tree only. Target: `narrative_engine_design_v2_churn.md`
(§3 FORECAST, §4 LIGHT, §7 R-F1). Grounding: `01_workings/dossier_forecast_tractability.md`,
`spec/churn_amendments.md` (s4). Cites `file:line`. Complements the v1-scoped
`refute_determinism_replay.md` (does not repeat its L2/L3/L5 findings; attacks the NEW forecast
organ v2 adds)._

## Thesis

v2's determinism story leans on three claims the dossier states as *mitigations to build*, not
properties in hand — and the design prose promotes them to done. And the cost budget (<100 ms)
is honest for **one** ensemble under **one** policy, but v2's own outputs are specified
**per player lever**, which multiplies the budget by a factor neither doc costs. Verdict:
**SOUND-WITH-FIXES**, with one item (per-lever Layer B cost) that is BLOCKER-grade until scoped.

---

## FINDING 1 (MAJOR · determinism) — `hash(canonical_key_log, …)` is doubly underdefined: the hash FUNCTION is salted and the SERIALIZED ARTIFACT is unspecified

§3 Determinism guards: `ensemble seed = hash(canonical_key_log, accounting_index, future_index)`.
Dossier Q5.3: `seed_i = hash(canonical_serialized_key_log, accounting_index, future_index)` —
"save/load-stable iff the Key-log is serialized in canonical order."

Two holes:

1. **The hash function.** Python's builtin `hash()` over `str`/`bytes` is **salted per process by
   `PYTHONHASHSEED`** — the exact hazard the substrate already fights for `set()` iteration
   (`propagation_spec_v1.md` ORD-2; `faction_action.py:148` "[hash-seed fix]"). If `canonical_key_log`
   is a string/bytes and the seed uses builtin `hash()`, seeds differ every process → forecasts differ
   run-to-run → V4's "same Key log → same forecasts → same text" fails on the seed derivation itself.
   The dossier's "canonical order" fix addresses the INPUT ordering but says nothing about the hash
   PRIMITIVE's own salting. Both docs write `hash(...)` with no algorithm named.
2. **`canonical_key_log` is not defined anywhere.** `grep` finds `KEY_LOG` defined in
   `propagation_spec_v1.md` (§4.1, append-only, `sub_step_index` on append) but **no `canonical_key_log`
   serialization spec** — no field order, no statement of what is included. Critically, each Key's
   `causes[]` "now carries both authored provenance AND runtime re-entrancy parentage, without a
   specified way to distinguish the two edge types on replay" (`refute_determinism_replay.md`:159,
   citing propagation_spec §4.4). If the serialized log that seeds the forecast includes `causes[]`,
   that ambiguity leaks straight into the seed. And V4 itself is CONDITIONAL on ORD-3/ORD-4, which have
   **not landed** (`propagation_spec_v1.md:122,330`). So the seed's own input is not yet deterministic.

**REQUIRED_FIX:** (a) Mandate a fixed, cross-platform hash — `hashlib.sha256` (or blake2) over canonical
bytes, truncated to 64 bits — NEVER builtin `hash()`; add to R-F2. (b) Author a `canonical_key_log`
serialization spec: explicit field set (exclude runtime-only fields — `cascade_depth`, scheduler
state), stable field/record order, and an explicit rule that `causes[]` authored-vs-reentrancy edges
are either both included in a canonicalized order or the reentrancy edges are excluded from the seed
preimage. (c) State the seed's dependency on ORD-3/ORD-4 landing as an explicit Stage-2.5 precondition,
alongside the sim-stub preconditions §3 already lists.

---

## FINDING 2 (MAJOR · determinism) — integer basis-points do NOT remove the cross-platform Φ hazard; they relocate it to the quantization boundary, and the parity harness that would pin it does not yet cover a bespoke Φ

§3 claims, as if in force: "**integer basis-point marginals** (no float-boundary nondeterminism);
shared erf/Φ lookup for the Godot port (no `math.erf` divergence) pinned by the ED-1050-class parity
harness." The dossier is more honest (Q5.4): the resolver-draw parity harness "does **not** yet cover
a bespoke Φ," the shared erf "lookup/poly" is a **mitigation to build**, and the Gate-0 RNG service
is **not yet built** (CLAUDE.md §6).

The design over-claims twice:

1. **Integer basis-points don't eliminate the float boundary — they move it.** `_phi` is
   `(1+math.erf(z/√2))/2` (`sigma_leverage.py:229`), a float. To carry marginals as integers you must
   quantize Φ → 0–10000. That float→int step is itself a boundary comparison: a Φ value within 1 ULP
   of a basis-point edge rounds to different integers on Python vs GDScript unless (i) erf is the SAME
   implementation to the last ULP and (ii) the rounding mode (half-to-even vs truncation) is pinned
   identically. Basis-points fix float **accumulation** (associativity), not the per-step Φ
   **quantization** boundary. §3 asserts "no float-boundary nondeterminism" — false for the Φ→bp step.
2. **`math.erf` vs GDScript.** GDScript has no identical `erf`; the design's "shared erf/Φ lookup"
   is unbuilt and the harness that "pins" it currently covers resolver draws, not a standalone Φ table.
   This is the ED-1050 class the design cites — but cites as *solved by discipline already present*,
   when the dossier says the coverage gap is open.

**REQUIRED_FIX:** Specify the shared Φ as a **precomputed integer lookup table** (Φ pre-quantized to
basis-points, identical bytes shipped to both platforms) so no live `erf` runs on either side and no
per-platform rounding exists — the quantization happens ONCE, offline, in the table. Pin the table in
the parity harness as its own fixture (extend F7). Until that table exists, mark Layer A horizons as
**not port-parity-clean** and gate any Godot forecast on it. Downgrade §3's "no float-boundary
nondeterminism" to "float boundary confined to the offline Φ-table build."

---

## FINDING 3 (BLOCKER-until-scoped · cost) — the <100 ms budget is for ONE ensemble under ONE policy; v2's outputs are specified PER PLAYER LEVER, an uncosted ×L multiplier

Dossier Q4: N=64 × k=4 = 256 season-steps → ~2.6×10⁶ ops (EV) / ~10⁷ (sampled) → "<100 ms." This
is **one** no-intervention ensemble. But:

- §3 Outputs: `stake_horizon{stake, P-band per k, under no-intervention **and per player lever**}` and
  `option_distribution`.
- The dossier's own per-lever recipe (Q3 recommendation, Q4 fidelity note) is "inject the lever as an
  odds/stat shift on the **analytic** layer + a policy change in the `action_callback`." A μ-shift on
  Layer A is genuinely cheap and per-lever-free (§9.1's "assign the spymaster" lever is exactly this —
  a Layer-A `P(fail)` shift). **But that only works for CONTINUOUS stakes.** A per-lever
  `option_distribution` or a per-lever horizon on a **discrete structural branch** (which action fires,
  which target) cannot be obtained by shifting μ on the analytic layer — Q3 itself proves EV-averaging
  discrete branches "collapses the mixture and lies." Per-lever discrete horizons therefore require
  **re-running Layer B under each lever's policy**: cost = N × k × **L**.
- With L ≈ 5–15 candidate domain actions per Accounting, that is 15 × 256 = 3,840 season-steps ≈
  4×10⁷ (EV) – 1.5×10⁸ (sampled) ops ≈ **0.4–1.5 s**, not <100 ms — 5–15× over budget.

Neither doc reconciles the per-lever output spec against the single-ensemble cost model. The <100 ms
number silently assumes exactly the thing the outputs forbid (a single policy).

**REQUIRED_FIX:** Split the per-lever contract by branch class, in §3 and the dossier Q4:
(a) **continuous** stakes → per-lever via Layer-A μ/odds shift (free, no extra ensemble); (b)
**discrete-branch** stakes → EITHER restrict per-lever to a small fixed lever set with an explicit
budget line `N × k × L` (state L, re-cost, e.g. cap L≤4 to stay <400 ms), OR forbid per-lever Layer B
in M1 and mark discrete per-lever horizons as a post-M1 output. Add a cost-envelope row that names L
explicitly; the current envelope table (dossier Q4) omits the lever axis entirely.

---

## FINDING 4 (MAJOR · Layer A analytic) — "exact Normal first-passage" over-claims for state-COUPLED clocks; the closed form holds only for pure drift, and the design drops the dossier's "if known / else sample" caveat

§3 Layer A: "Drift clocks (MS −1/yr, CI +1/season) get **exact Normal first-passage horizons** — P(threshold
within k seasons) with no sampling." The dossier is careful where the design is not:

- Dossier Q1 **1a** (pure-drift: MS baseline −1/yr, CI passive +1/season) → "**Analytic** — hitting time
  = (threshold − x₀)/rate exactly." Genuinely closed-form (deterministic linear drift; not even
  "Normal" — it's exact).
- Dossier Q1 **1b** (accounting-perturbed: CI *generation* PP-412 5-step, IP, Turmoil, Accord) →
  "Deterministic base + **state-dependent delta; some stochastic (insurgency-driven)** … **Analytic IF
  per-season delta distribution known; else sample**."

The design **collapses 1a and 1b** into "drift clocks get exact first-passage," dropping the "if known
/ else sample" gate. CI's real motion is passive drift PLUS state-dependent, insurgency-coupled
generation — its increments depend on the settled state the ensemble is simultaneously evolving, so the
increments are neither i.i.d. nor Normal, and first-passage is NOT closed-form for the coupled
component. This is the cross-clock coupling the task names: **Domain Echo (degree→stat, `domain_echo.py`)
feeds faction/settlement stats, which feed CI/IP generation, which feed thresholds.** A "drift clock" is
not an isolated random walk; it shares drivers with the very stakes whose horizons Layer A computes.

Two consequences the design does not admit:
1. Layer-A horizons for CI/IP/Turmoil/Accord are **approximate**, valid only to the extent the coupled
   generation term is treated as constant drift — an unstated modelling error, not "exact."
2. Independent per-stake first-passage horizons **cannot be multiplied** into joint crossing
   probabilities, because clocks are coupled (one insurgency spikes CI, drops settlement Order, moves
   faction stats together). The design correctly routes *convergence discovery* to Layer B (sampled),
   so this is contained for convergence — but any Layer-A-derived "P-band per k" presented for a coupled
   clock carries a hidden independence assumption.

**REQUIRED_FIX:** In §3 Layer A, split "drift clocks" into (a) **pure-drift** (MS baseline, CI *passive*)
→ exact linear hitting time; (b) **state-coupled** (CI generation, IP, RS, Turmoil, Accord) → Layer-A
horizon is an APPROXIMATION under a frozen-drift assumption, explicitly flagged as such, with the
option to promote to Layer B when the coupling is material. Restore the dossier's "if delta distribution
known / else sample" gate verbatim. Add an honesty-bound line: Layer-A marginals are per-stake and
**not jointly valid** — joint/convergence questions must use Layer B.

---

## FINDING 5 (MEDIUM · determinism) — light-inertia carryover + decay is an unspecified accumulator; the score is integer-basis-points but the DECAY arithmetic is not, and it inherits propagation_spec OF-3

§4(ii): light-inertia = "lit threads carry a **persistent priority term**"; the selection score is
stated "integer basis-points." But the CARRYOVER/DECAY across Accountings (how last Accounting's inertia
discounts into this one) is not specified as integer arithmetic. `churn_amendments.md` s4 adds "the light
ledger (per-thread inertia + budget)" as new engine-owned state but no decay rule.
`propagation_spec_v1.md:178` (OF-3) already flags the analogous `decay()` for the Key-ledger as
UNSPECIFIED and requires it be "a pure function of `key.emitted_at` (no RNG, no hidden state)" to
preserve determinism — and separately notes cross-tick convergence is "conditional on `decay()` being
strictly contractive," "not proven." A float inertia decay compounding over many Accountings reintroduces
exactly the cross-platform accumulation-order hazard the basis-point rule elsewhere kills, AND the
anti-strobe floor is a threshold comparison on that accumulator (another boundary).

**REQUIRED_FIX:** Specify light-inertia carryover as integer/fixed-point with a defined rounding
(e.g. `inertia_bp = inertia_bp * NUM // DEN` floor-division, constants in the Light-Function weight-set
DATA), decay a pure function of season/accounting index only (no float, no RNG), and cite OF-3 as the
governing open flag so the light ledger's decay is disposed together with the Key-ledger's. Add the
anti-strobe floor as an integer threshold. Fold into R-F2.

---

## FINDING 6 (MAJOR · R-F1 shared-code) — "reuse `run_campaign` verbatim / never a parallel model" is in tension with "scenes are NEVER rolled": the scene-EV-summarizer is a NEW forecast-only code path, and 19 stubs sit on the paths run_campaign walks

§3/§7 R-F1: forecast and live "share resolver code … never a parallel model"; the dossier Q2 calls
`run_campaign` "the ensemble entry point, **verbatim**." But:

- `run_campaign` → `run_season` → **step 2 `action_callback`**, which is where BOTH faction actions AND
  **scene resolution** live (`season.py:61` "faction actions, scene resolution, whatever the caller wants";
  mc_v18's live callback also runs `scene_dispatch.run_scene_phase`). The dossier simultaneously requires
  "scenes are **NEVER** rolled in forecast" (Q4; rolling them 10²–10³× the budget). These cannot both
  hold with the SAME callback. The forecast must pass a **different, scene-skipping callback that
  EV-summarizes each scene by its degree distribution** — a code path that **does not exist today** and
  is, at the scene layer, precisely a forecast-only parallel path. So R-F1's "never a parallel model" is
  true for `faction_action`/`accounting`/`domain_echo` (shared) but has a real EXCEPTION at scenes that
  the design states as absolute. `run_campaign` is NOT reused "verbatim" — only its non-scene spine is.
- The stubs on those paths are load-bearing: `npc_ai.select_action` raises `NotImplementedError`
  (`npc_ai.py:22`), plus `ip_track`, `rs_track`, ~8 provincial actions, and the event deck has **no code**.
  `run_campaign` walks these, so it cannot roll a full future until they land. The design lists these as
  Stage-2.5 preconditions (good) — but the design's OUTPUTS that NEED Layer B (`option_distribution`,
  `convergence_candidate` discovery) are therefore blocked on stub completion + a NEW scene-EV path +
  the untrusted ensemble baseline (degenerate ~87% win-share, F7 unbuilt). "By construction" oversells a
  path that is mostly still to be built.

**REQUIRED_FIX:** (a) Author the scene-EV-summary as a **shared, flag-gated mode inside the resolver
seam** (a `strategic_cadence_only` flag on the scene path that BOTH live and forecast honor — live uses
it never, forecast always), so the EV-summary is single-sourced and R-F1-clean rather than a
forecast-only fork; specify it as an R-F1 sub-clause, not an unstated exception. (b) State plainly that
R-F1 "shared code" covers the strategic spine and the flag-gated scene-EV path, and that Layer B's
completeness is bounded by the named stubs (already partly in §3 — make the scene-EV path explicit
alongside them).

---

## NECESSITY GATE (N / Ω / Q) on the FORECAST organ

**Question:** is **Layer B** necessary for M1, or is **Layer A alone** the honest first ship?

- **N (necessity).** Layer A alone delivers the player-facing forecast value: the third legibility
  question (`stake_horizon` continuous), `foreclosure_countdown`, stakes-preview/imminence lines, and
  the Light Function's `imminence` term. It is near-free, needs no stubs, no event deck, no smoke
  oracle. Layer B's UNIQUE contribution is (i) `convergence_candidate` **discovery** beyond the 8
  authored priors and (ii) discrete `option_distribution`. Neither is necessary to ship a legible
  forecast: the 8 authored COLLISIONs can serve as the M1 convergence surface (they are already priors),
  and continuous per-lever horizons cover the lever-preview use case. **Layer B is NOT necessary for M1.**
- **Ω (omissibility).** Layer B is cleanly omissible: §8 already sequences "Layer A first … Layer B
  gated on its preconditions." The omission is architecturally free IF the Light Function's
  `forecast mass` term degrades to Layer-A-only horizons when Layer B is absent. **Today it does not
  cleanly separate** — §4's selection score folds "forecast mass (the §3 horizons)" as one term without
  saying which sub-terms are Layer-A-satisfiable, so the central AUTHOR organ risks a latent dependency
  on the unbuilt/degenerate Layer B.
- **Q (quality floor).** Layer B's current quality floor is **unmet**: the ensemble's structural-branch
  distribution is degenerate (~87%/0%/0% win-share, nothing flags it) and F7 (smoke oracle) is unbuilt.
  Shipping Layer B outputs into the authorial selection score before F7 exists would feed an untrusted
  distribution into the game's authorial voice.

**Verdict:** ship **Layer A only** for M1 (design already leans this way in §8 — make it a hard gate).
**REQUIRED_FIX:** In §4, tag each selection-score term with its forecast dependency; define the
`forecast mass` term to compute from Layer-A horizons + the 8 authored COLLISION priors ALONE for M1,
with Layer-B convergence discovery as an additive term switched on only after F7 passes and the stubs
land. This makes Layer B genuinely omissible (Ω) instead of latently load-bearing.

---

## Defensive credit (tried to break, could not)

- **Accounting-boundary evaluation over settled state** correctly sidesteps mid-cascade ORD-3
  nondeterminism for the forecast's READ side (dossier Q5.3) — right place to snapshot.
- **`action_callback` as lever seam** is real (`season.py:61`): the seam genuinely allows a
  scene-skipping / policy-swapping callback without touching the spine — so per-lever POLICY injection
  is sound (the cost of it, Finding 3, is the issue, not the mechanism).
- **Domain Echo as zero-RNG EV kernel** (`domain_echo.py:27-33`, "zero RNG" confirmed) is a clean
  analytic primitive — no finding.
- **`sigma_leverage.p_success` as the shared EV primitive** is single-sourced (contest resolver imports
  it, `resolver.py:24`) — R-F1 holds cleanly for the continuous resolver families.

## Bottom line

The continuous/analytic half of the forecast is genuinely tractable and mostly shares live code. The
determinism claims fail only where the design promotes dossier *mitigations-to-build* (fixed hash + Φ
table + parity coverage) to done, and where "integer basis-points" is asserted to kill a boundary it
only relocates. The cost claim is honest for one ensemble but silently contradicted by the per-lever
output spec (Finding 3 — the one BLOCKER-grade item until L is scoped). Layer A over-claims exactness
for state-coupled clocks (Finding 4). R-F1 is clean for the spine but has an unstated scene-EV exception
(Finding 6). And Layer B is not necessary for M1 — ship Layer A, gate Layer B behind F7 + stubs, and
sever the Light Function's latent Layer-B dependency. Verdict: **SOUND-WITH-FIXES.**
