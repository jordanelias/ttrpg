# Combat engine — reconciliation plan
### `combat_engine_v1` ↔ the prior-work corpus ↔ the directives

**2026-06-16 · status: PROPOSED, Jordan-vetoable · next Lane-A id ED-935 · proposed landing `designs/audit/2026-06-16-combat-reconciliation/`**

**What this is.** A single map from each of your fourteen points to a concrete change against the live engine, the canonical document that grounds it, who owns the call, and the order to do it in. Nothing here is committed; the canon engine is unchanged.

**Built bottom-up against the live engine at HEAD + the prior-work corpus this session:**
`[READ: designs/scene/combat_engine_v1/{core,systems,combatant,wrapper,config}.py + r1/r2/r5/m1/r8 — full, formulae and constants verbatim]`
`[READ: designs/audit/2026-06-13-combat-bottomup/{combat_puncture_and_topdown_inventory, combat_residuals_pob_f5_findings, combat_ability_emergent_reframe, combat_ability_gating_chain_and_sets}_2026-06-13.md]`
`[READ: designs/audit/2026-05-29-combat-armature/sigma_leverage_handoff.md §0–§2]`
`[READ: designs/audit/2026-05-31-percell-combat/{percell_integration_plan, percell_validation_stage4}.md]`
`[READ: designs/audit/2026-05-28-combat-reframe/{combat_mechanical_armature, derived_stats_audit}.md]`

`[SELF-AUTHORED — bias risk: this corrects my own flatten, which analyzed the engine in isolation and missed this corpus. Stated against that interest.]`

---

## §0 — The unifying finding

The engine's **dynamics are bottom-up and sound** — σ-pool resolution, reach, tempo, stamina, concentration, initiative, poise, bind, leverage, feint, defence-selection all derive from stats and weapon geometry over tuning coefficients. Two regions are **top-down**, and that is the whole of what you are pointing at:

1. **The weapon-vs-armour damage layer** — `RESIST`/`DELIVERY`/`HEFT`/`ADEF`/the percussion path — is a stack of hand-set lookup tables. The bottom-up replacements **already exist** (`percussion_authority.py`'s `P_auth`; the v32 `armour_axes.py`/`damage_model.py`; `geometry.py`'s `perc_conc`/`cut`/`thrust`) but are **dangling or unwired** — only `gap` is live. This is the `2026-06-13` top-down inventory's §2 verdict, not a new claim.
2. **The resolution applies σ-leverage as an Ob-shift floored at 1**, which r1 itself labels *display-only* and which distorts the degree bands — when the canonical σ-leverage spec (`sigma_leverage_handoff §1` = armature **A1/A2**) is a μ-shift that leaves the base Ob fixed and boosts the roll.

The reconcile is therefore mostly **wiring work that already exists** plus a **resolution correction the code's own docstrings prescribe**, calibrated to the σ-leverage armature (**A1** uniform-impact, **A2** `tanh` saturation, **A5** derive-don't-tabulate). A handful of pieces genuinely change outcomes or are unbuilt — those are yours, and they are flagged.

**Ownership legend.** `[MECH]` mechanical, I execute (reproduces canon or is a clean wiring/cleanup; logged, vetoable) · `[BAL]` changes outcomes/feel, you ratify · `[CANON]` touches Class-A canon or an authored/ratified value, you decide · `[NEW]` genuinely unbuilt mechanism, you scope.

---

## §1 — The directive map

| # | Your point | Concrete change | Canonical basis | Owner | Stage |
|---|---|---|---|---|---|
| 8·13 | **F4: effective_ob must use the μ-shift; calibrate the Ob chain per σ-leverage** | In `core`/`wrapper` resolve path: stop using `effective_ob` (Ob-shift, floored 1) as the Ob. Keep base Ob = 3 fixed; **boost the roll** by `eff_σ·σ_N` = `1.5·tanh(net_σ/1.5)·0.8·√pool`; take the degree against the fixed Ob. | `sigma_leverage_handoff §1` (A1/A2): `σ_N=0.8√pool`, `eff_σ=1.5·tanh(net_σ/1.5)`; r1 `eff_ob` docstring: *"resolution uses p_success (the μ-shift)… boosts the roll instead"* | `[MECH]` to implement + `[BAL]` re-validate | **1** |
| 3 | **Where is Point of Balance?** (dead input) | Wire `P_auth = min(8, 9.5·(√mass·pob_frac)^0.30)` (blunt heads only) **in place of** the hand-set `percussion`. `pob_frac`/`mass` stop being dead. | `combat_residuals_pob_f5 §2`; `percussion_authority.py` (reproduces 11/12 blunt cells, self-test green) | `[MECH]` | **1** |
| 6 | **What happened to emergent blunt percussiveness?** (it's a `perc/8` table) | (a) `P_auth` as above. (b) Replace `RESIST`/`DELIVERY`/`ADEF` with the **continuous transmission model** (`v32 armour_axes`/`damage_model`, currently calibrated to `RATIFIED_TABLE`) so mass/balance drive damage as a live gradient. (c) Add the **puncture mode** (`puncture_pressure = authority × strike_concentration`) so a poleaxe beak ≠ a mace face. | top-down inventory §2 (#1/#2/#6); `geometry.percussion_concentration()` (`perc_conc` derived, dangling) | (a)`[MECH]` (b)`[BAL]` re-baseline (c)`[CANON]` | 1 / **2** |
| 9 | **HEFT light/heavy binary is top-down** | Derive impact from continuous `mass` (sourced per-weapon, used nowhere). Folds into the §6(b) transmission model. | top-down inventory §2 finding #3 | `[BAL]` (part of the re-baseline) | **2** |
| 5a | **Pool: why `max(5, …)` if it's History+6?** | Drop the dead `POOL_FLOOR` branch — `History ≥ 1 ⇒ pool ≥ 7 > 5`, the floor never binds. Cosmetic. | `r1.resolution_pool`; `derived_stats_audit §1` (pool reformed to History-only) | `[MECH]` | **1** |
| 5b | **Recompute the pool as a composite** (combat-experience / tradition / stamina / focus, like `atk_sig`) | New pool form, e.g. `pool = base + relevant_history + f(tradition, stamina, focus)`. **Significant**: the pool sets `σ_N = 0.8√pool`, so this re-scales the σ-leverage and must hold A6 parity (≈0.30σ/pt). The current History-only pool deliberately closed the Agi-dominance channel (C-04). | `sigma_leverage_handoff §0` (C-04 is the pathology), armature **A6** | `[NEW]` | **3** |
| 12 | **atk_sig should use Concentration, not Focus** | Change `atk_sig`'s consistency term `0.10·(Focus−3)` → drive it from the **Concentration tracker** (`3·Focus+2·Spirit`, which depletes), so consistency reflects current gas, not the static stat. | `conc_max` = `3·Focus+2·Spirit` (ED-902); F5 residuals (conc = execution quality) | `[MECH]` + small `[BAL]` check | **1** |
| 4·7·11 | **Make degree (and quality) a continuum, not stepped** | Replace the 4-band degree with a continuous `severity = (net − base_Ob)/σ_N` (clean once on the μ-shift), and the `QUAL{.35/1.0/1.5}` multipliers with a continuous **saturating** function → 1.5. One change: continuous `p_success` → continuous severity → continuous saturating damage multiplier. | armature **A5** (derive/emerge); top-down inventory #10 (`QUAL` hand-set) | `[NEW]`/`[BAL]` | **3** |
| 2 | **Disposition should bias which maneuvres/abilities/skills get chosen, and when** | Build a **selection layer**: disposition weights *selection-propensity and timing* over the tradition-taught maneuver/ability set. The current 3 hooks (commit/counter/init) measure NULL and are a different, weak mechanism — the intended selection role is unbuilt. | emergent reframe (competence budget defines the *available* set); gating-chain §1–2 (`mode`/`set` structures); disposition is your canon-intent | `[NEW]` | **4** |
| 1·14 | **Where are Stamina and Concentration?** | They **are** in the engine (stamina→`≤−4` separation + tempo fatigue; concentration→`mental_fat`→read; `conc=3Foc+2Spi`). My flatten under-showed them — surface them as first-class state. Optional: the F5-A wound→stamina/conc enrichment. | `derived_stats_v30`/ED-902; F5 residuals §1 | `[MECH]` (representation) + optional `[BAL]` (F5-A) | **1** / parked |
| 10 | **reading = (2Cog+Att)/3 — does the /3 damping change everything?** | Measured answer: it damps per-point差异 but **does not** prevent Cog/History dominance — the read→mode→`net_σ`→Ob chain is the steep lever, and the read contest compounds both ways (my sweep: Cog +86pp across 1–7). Whether the read *should* dominate physical stats is a balance tune, not a defect. | my contribution sweep; armature **A6** | `[BAL]` observation (no change unless you want it) | parked |
| — | **Cleanup: dead `seize` lever** | `vorschlag`/`sen_no_sen` point at the cut `seize` lever and sit at baseline (empirically dead). Repoint to a live lever or retire. | `systems.py:242` (seize cut 2026-06-05); my ability sweep | `[MECH]` | **1** |

---

## §2 — Staged execution

Each stage is gated: I do the `[MECH]` work and **stop for your ratification** before any `[BAL]`/`[CANON]`/`[NEW]` item. Every change ships behind reproduce-the-anchors validation (mirror ≈ .50; the committed parity anchors: longsword mirror .481, wound-handicap .490/.329/.215).

**Stage 1 — mechanical drop-ins (reproduce canon; I can execute now).**
The μ-shift reconcile (§3), `P_auth` wiring, drop the dead pool floor, `atk_sig→Concentration`, repoint/retire the dead `seize` lever, and surface stamina/concentration in the state representation. All reproduce or correct toward canon; each re-validated against the anchors. The μ-shift and `atk_sig→Concentration` shift the degree/consistency distributions slightly, so Stage 1 ends with a **balance re-validation** I bring to you before locking.

**Stage 2 — emergent damage wiring (a re-baseline; your call to start).**
Wire the continuous transmission model (`armour_axes`/`damage_model`) to replace `RESIST`/`DELIVERY`/`HEFT`/`ADEF`, making mass/balance a live damage gradient; add the puncture mode. These **change outcomes** (the point of going continuous) and the puncture pick-vs-plate magnitude needs a canon decision. I stage the wiring; you decide whether to adopt the re-baseline.

**Stage 3 — resolution/output redesign (your design calls).**
Continuum degree + continuum saturating quality (one coherent change atop the μ-shift), and the pool-recompute as a composite. Each changes the resolution feel and/or the σ-leverage scale; I bring worked proposals with measured win-rate/parity effects, you choose.

**Stage 4 — new mechanics (unbuilt; your scope).**
Disposition-as-selection (the maneuver/ability/skill selection-and-timing layer), built on the emergent competence budget. Genuinely new design — I scope the mechanism with you before building.

---

## §3 — The μ-shift reconcile + Ob calibration (detail — the two you pressed hardest)

**The change** (a few lines in the resolve path):

```
# current (the F4 seam — Ob-shift, floored, r1 calls it display-only)
ob  = effective_ob(pool, net_sigma)          # max(1, 3 − 1.5·tanh(net_σ/1.5)·0.8·√pool)
net = roll_net(pool, rng)                     # ~ Normal(0.40·pool, 0.80·√pool)
deg = degree(net, ob)

# reconciled (μ-shift — canonical σ-leverage; base Ob fixed, roll boosted)
base_ob = 3
boost   = soft_cap(net_sigma) * sigma_n(pool) # = 1.5·tanh(net_σ/1.5) · 0.8·√pool
net     = roll_net(pool, rng) + boost
deg     = degree(net, base_ob)
```

**Why it is the canonical model, not a new one.** Shifting the Ob by `eff_σ·σ_N` and boosting the roll by `eff_σ·σ_N` move the success z-score by the *same* `−eff_σ` — identical P(success) by construction (A1's uniform impact, ≈25.8pp per `δσ=1.0` at every pool size). The constants are the canon ones already in the engine: `SIGMA_N_COEFF=0.8`, `M_MAX=1.5`, levels Minor/Moderate/Strong/Major = 0.25/0.50/0.75/1.00.

**What it fixes** (measured this session):
- **The degree distortion.** The floored Ob made *overwhelming* trivial (`2·1=2` on the raw roll); the μ-shift restores the canonical band (`2·base_Ob=6` on the boosted roll). Measured at pool 11, `net_σ+1`: P(overwhelm) 0.70 → 0.61; at `net_σ−1`: 0.009 → 0.070. The band becomes **consistent** across the net_σ range instead of swinging with the floor.
- **The implicit advantage-cap.** The floor-at-1 quietly capped a high-leverage attacker; the μ-shift removes it (the `tanh` M=1.5 stays the real bound). P(success) is **preserved mid-range** (`net_σ−1`: Δ0.000; `net_σ+0.5`: Δ0.000) and **rises slightly at high leverage** (`net_σ+1`: +0.020; `+2`: +0.067).

**The gate.** That last point is why this is `[MECH]` to implement but needs `[BAL]` sign-off: removing the floor's cap slightly widens the win-rate spread for high-`net_σ` builds (which my flatten already showed are Cog/History-driven). I implement it, re-run the parity anchors + the contribution sweep, and bring you the measured spread change before locking. If the widening is unwanted, the `tanh` `M_MAX` is the dial (lower M = tighter cap) — a one-constant tune, not a redesign.

---

## §4 — Your decision points (parked, with my recommendation)

1. **Continuous transmission re-baseline** (Stage 2) — adopt `armour_axes`/`damage_model` so mass/balance drive damage as a gradient (vs keep the tables, wire only `P_auth` which reproduces them). *Recommend: yes, but as a deliberate re-baseline with full re-validation* — it is the structural fix behind half your damage questions.
2. **Puncture pick-vs-plate** (Stage 2) — does a poleaxe beak out-defeat a mace through plate? The ratified table flattens them (`blunt_heavy` single row); honouring the derived `pierce 6.80 vs 3.60` **refines an authored canonical value** — your call, plus a calibration anchor that does not yet exist (`[GAP]`).
3. **Continuum degree + quality** (Stage 3) — adopt the continuous severity/quality (vs keep the 4 bands). *Recommend: yes, paired with the μ-shift* — it is the same change carried through to damage, and "videogame, not d10 table" is your stated direction.
4. **Pool recompute** (Stage 3) — make the pool a composite (tradition/combat-experience/stamina/focus). *Caution: it re-scales σ-leverage* — worth doing for richness, but it must hold A6 parity, and I'd bring the measured re-calibration before committing.
5. **F5-A wound enrichment** (parked) — add wound→stamina/concentration channels on top of the Class-A `−1D`. *Recommend: only if you want wounds more textured* — the measurement says the `−1D` is already sufficient and uniform enough; do **not** amend `derived_stats §4.1` on uniformity grounds.
6. **Read-dominance** (parked) — if Cog/History dominating physical stats is unwanted, that is an A6 balance tune, not a defect.

---

## §5 — What stays untouched (canon or sound — I will not change these)

- **The `−1D`-per-wound pool penalty** — Class-A canon (`derived_stats_v30 §4.1`, PP-717). Augment-only; no §4.1 amendment proposed.
- **`RATIFIED_TABLE`** — the canonical weapon-vs-armour anchor every bottom-up model reproduces. Top-down *by design*.
- **`TRADITIONS`/`ABILITIES`/`FAMILIARITY`** — authored cognitive-mode content, grounded in the historical-precedents corpus. Cultural emphasis is a design choice, not physics.
- **`UPSET_FLOOR` 0.05** — the deliberate 95% videogame cap.
- **The ~100 `config` coefficients** — Class-C calibration scaling, not outcome-encoding (the resolution skeleton — `COMMIT_SIGMA`, `ACT_THRESHOLD`, the `degree` thresholds — is hand-structured by design).
- **The world, characters, metaphysics, HEMA/bind texture, naming** — off-limits per the project-owner contract; none of the above touches them.

---

## §6 — Honesty block

- `[CONFIDENCE: high]` on: the σ-leverage constants (`0.8`/`1.5`, verbatim from `m1`); the μ-shift⇄Ob-shift P(success) equivalence and the measured degree-band correction (computed this session); the top-down/unwired status of every damage-layer table (verified by consumption grep + the inventory's read-cited rows); `P_auth` reproducing the blunt cells.
- `[BAL]` items genuinely change outcomes — I will not commit them on my own judgment; each comes back to you with measured win-rate/parity effects.
- `[CANON]` items (puncture row, any wound amendment) refine authored/ratified values — yours alone.
- `[GAP: pick-vs-plate magnitude]` — the puncture pierce term is a validated *ranking*, not a calibrated number; no ratified anchor exists.
- `[ASSUMPTION: the disposition-as-selection mechanism — basis: your stated intent that disposition bias maneuver/ability/skill choice and timing; the engine has no such layer today, so this is scope-then-build, not a wiring.]`
- Nothing here is committed. The canon engine is unchanged; `pob_frac`, the wound `−1D`, and the resolve path remain exactly as at HEAD.
