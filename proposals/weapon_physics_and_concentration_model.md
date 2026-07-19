# Valoria — Weapon-Physics Model + Concentration (implementation spec · v2)

## Status: PARTIALLY SUPERSEDED — §§1–6 composite-mass/PoB model BUILT (combat_engine_v1/weapon_physics.py; ED-PC-0010 resolved recalibration). Residual: §7 concentration-error mechanic (T_err/ERR_K; live conc/conc_max disruption-resistance) never built. HELD FOR JORDAN. [## Status: heading added 2026-07-15]
**2026-06-05 · the new physical-weapon system + the concentration error mechanic**

Supersedes the v1 draft: the invented head-mass fraction `f` is **retired** for the measured **point of balance** plus a **wood/iron composite-mass model**. Engine sites/formulas/current values are **HEAD-verified this session**; physical values are **sourced** (tiers in §6) — ranges where per-specimen data is sparse. `[PROPOSED]` = my call, vetoable; `[RE-VERIFY]` = confirm the constant at implementation (config drifted).

---

## 0. Resolutions recorded
- **Armour = damage reduction only.** RESIST (`core.py:20–23`, armour × mode) is the whole of armour's effect; no flat Health → `WoundTracker.equipment_health` correctly stays unfed (remove as dead or leave inert), and **derived_stats §4.1's "+4/+6/+8 flat Health" line is stale — strike it.** Finding A: closed, not a defect.
- **Concentration = `3·Focus + 2·Spirit`** (verified `systems.conc_max`; ED-902). Any doc carrying `Focus×3` is stale.

## 1. Principle
The resolver is unchanged (σ-leverage + pool). This system replaces the two categorical fields — `wt` (light/heavy) and `reach` (short/long) — that feed five consumers, with continuous physical quantities derived **bottom-up** from real material densities and specimen data. Physics fixes the *shape*; the scaling constants are sim-calibrated to the established targets (mirror=50, the tier spread, no-one-shot `CAP_END`).

## 2. Primitives per weapon
- **`mass`** (kg) — sourced (§6).
- **`PoB`** — point of balance, distance from the cross/hand. The measured mass-distribution quantity. *(My v1 `f` — head-mass fraction — was an invented primitive. The literature's real analog is "blade presence" = blade-weight ÷ total-weight, which is **derived** from mass + PoB + pivot measurements, not asserted. PoB is the primitive; blade-presence / `f` is an output.)*
- **`head_len`, `grip_len`** (existing) — one consistent length unit; values unchanged.
- **`grip`** state {normal, choke, lunge} + the half-sword form — the partition (§3).
- baked geo: `curvature`, `edge_keenness` → `geo.cut`; `point_concentration` → `geo.thrust`; `strike_concentration` → `geo.perc_conc`.

## 3. The partition — grip → effective lengths
Hand position along the weapon. Normal: ahead = `head_len`, behind = `grip_len`.
- **choke** — hand `+δ_choke` toward the head: `eff_head = head_len − δ_choke`, `eff_behind = grip_len + δ_choke`. Less reach, lower MoI, more control/leverage.
- **lunge** — body extension: `+Δ_reach` plus a recovery/tempo penalty; lengths unchanged.
- **half-sword** — hand onto the blade: `eff_head ≈ point only`, `eff_behind` large → supreme control/leverage/gap-thrust, no cut/cadence (already the auto-switched longsword form).

`δ_choke`, `Δ_reach` `[PROPOSED]`.

## 4. Composite-material mass & balance — the bottom-up derivation
**Densities (sourced):** iron/steel ρ_iron ≈ 7.86 g/cm³; haft hardwood (ash/oak) ρ_wood ≈ 0.7 g/cm³ → **R = ρ_iron / ρ_wood ≈ 11** (≈10–12 for hardwood; higher for softwood). At equal volume, iron outweighs wood roughly 11 : 1.

**Model.** A weapon is iron (blade/head + pommel) on wood (grip / haft / shaft). Per unit cross-section × length, the iron zone contributes ~11× the mass of the wood zone. Apply by the **grip : edge length split**, with the iron localised to the actual metal:

- **Swords** (arming, longsword, rapier, sabre, greatsword, dagger): the edge/blade (≈ `head_len`) is iron; the grip (≈ `grip_len`) is wood; **plus an iron pommel — a point mass at the hand.** Blade-iron pulls the balance toward the tip; the pommel pulls it back to the forte; the wood grip is light. Net PoB lands a short way ahead of the cross, and the pommel is *why* it returns near the hand. This reproduces the measured picture — a sword ≈ an iron stick with a point mass at the cross — and predicts "blade presence" (the measured blade-weight ratio) rather than asserting it.
- **Polearms** (spear, poleaxe): iron is **only the head** (a small length at the far end); the rest of the reach plus the haft is **wood shaft**. The iron head (~11×, far out) pulls the balance forward, but the long wood shaft's distributed mass keeps PoB forward-of-centre, not at the head. Heavy *because the shaft is long*, not because the head is heavy.
- **Staff**: no iron → a near-uniform wood stick, balance at centre, light, lowest authority.

**Derived dynamics** (from mass + PoB + length; documented physics — Le Chevalier / Johnsson, ARMA-GTA):
- `static_moment = mass × PoB`
- `MoI_about_hand ≈ static_moment × blade_len` (≈ `mass × PoB × blade_len`) → handling / tempo.
- **authority** scales with MoI / effective impact-mass — **not** with PoB directly (PoB is static; how hard it hits is the dynamic MoI). For blunt heads this is the existing `percussion` field, now *equal to* the derived authority.
- `edge_cut` (edged heads only) ∝ `eff_head` (edge length) × `geo.cut` (keenness × curvature). Point wounds by penetration (`gap` / `geo.thrust`); blunt by authority (`percussion` / `geo.perc_conc`). No edge term for point or blunt.
- `reach` ∝ `eff_head` + 2H bonus + lunge Δ, replacing `reach=='long'` + `HEAD_REACH[head]`.
- `leverage` (existing length ratio) — now grip-modulated via the effective lengths.

**The trade-off (the realistic core):** pushing iron mass forward (`mass × PoB × blade_len`) raises authority but raises MoI faster → harder *and* slower. Head-heavy + long = hard/slow (mace, poleaxe, greatsword); hilt-balanced (heavy pommel) = fast/controllable (rapier, arming); long wood shaft = reach + handling-mass but low authority (spear, staff).

## 5. Consumer wiring (verified sites → new basis)
| Consumer (verified site) | Current (categorical) | New (physical) | Calibration |
|---|---|---|---|
| HEFT / impulse (`core:18,50`) | `{light:4, heavy:6}` | `g(authority)` from MoI | map current weapons onto the curve, then re-tune |
| `percussion` field (blunt) | hand-assigned 0–8 | `=` derived blunt authority | replace literals; `perc_conc` still multiplies |
| `act_cost` (`systems:48`) | `ACT_WEIGHT·(heavy)` | `ACT_WEIGHT·MoI_index` | `[RE-VERIFY]` ACT_WEIGHT |
| `weapon_tempo` (`systems:23`) | `WEIGHT_PEN·(heavy)+HANDS_COMMIT` | bounded `f(MoI_index)` | keep `MAX_TEMPO_PEN` cap |
| `str_demand` (`systems:58`) | `D_WT·(heavy)` | `D_WT·mass` (+ small MoI term) | `[RE-VERIFY]` D_WT |
| `reach_base` (`systems:13`) | `LONG·(long)+HEADR·HEAD_REACH[head]` | from `eff_head` (+2H +lunge) | `reach_adj` folds in |
| cut (`coupling` / `geo.cut`) | head-category via RESIST/DELIVERY | `× edge_cut` for edged heads — finally reads `geo.cut` | — |
| `leverage` (`systems`) | length ratio | same, grip-modulated | — |
| grip-state levers | dormant (`'normal'`) | live — engine selects grip, as half-sword already auto-switches | — |

## 6. Grounded values (sourced; ranges where per-specimen data is sparse)
- **Arming** ~1.0–1.5 kg; hilt-balanced (PoB near the hand). `[T3 Wikipedia, corroborated <2 kg]`
- **Longsword** ~1.2–1.6 kg functional (2–3 kg skews ceremonial); PoB ~10–15 cm. `[T1/T2 — HROARR / Capwell-Verdan]`
- **Rapier** 1.13–1.63 kg (seven Vienna specimens, Fortner & Schrattenecker); PoB ~9–15.5 cm; heavier than its reputation — mass sits at the hand. `[T1]`
- **Sabre** ~0.7–1.2 kg. `[T2/T3]`
- **Greatsword** ~2.7 kg combat (Dawson); pommel-counterbalanced; heavier = parade-only. `[T2]`
- **Poleaxe** 2.67 kg (a Royal Armouries specimen); 1.8–2.7 kg, well counterbalanced. `[T0 — Royal Armouries]`
- **Mace / war hammer** ~1–1.5 kg; head-forward (high static moment); hammers slightly lighter/faster than maces. `[T2/T3]`
- **Spear** ~1.8–2.5 kg; heavy shaft, light head → high MoI, **low** authority, huge reach. `[T2]`
- **Staff** ~1.2–2 kg; uniform, centre-balanced. `[T2/T3]`
- **Dagger** ~0.3 kg `[T3 — not freshly sourced]` · **paired short** ~0.5–0.8 kg each.

**Tiers.** T0 Royal Armouries (museum); T1 Fortner & Schrattenecker (7 Vienna specimens), HROARR database, Le Chevalier/Johnsson dynamics; T2 Dawson/Capwell/Verdan (named experts via secondary); T3 Wikipedia/aggregators (orientation only, corroborated). `[TIER-FLOOR: most masses are study/secondary ranges, not per-specimen singletons; the full numeric per-row tables (Fortner's table is image/late-page; the Ensis dataset; RA records) were not extracted this pass — available on request.]`

## 7. Concentration model (Jordan's spec) — extends the existing resource
The resource already works: `conc_max = 3F+2S`; drains per bout/loss/hit (`CONC_DRAIN_BOUT/LOSS/HIT = 3/2/2`), recovers (`CONC_RECOVER_FRAC = 0.4`); feeds initiative seizure (`INIT_SEIZE_CONC · conc/conc_max`). The Focus levers (`FOCUS_CONSISTENCY_K`, `FOCUS_MENTAL_K`, `DISRUPT_K`, `POISE_FOCUS_K`) exist. Grep-confirmed missing: any error mechanic. Two rewards:
- **Reward 1 — error-onset (NEW).** Threshold `T_err` on the concentration scale: `conc ≥ T_err → P(error)=0`; below, `P(error) = ERR_K · clamp((T_err − conc)/T_err, 0, 1)`. An error is a degraded/misfired action — tempo loss, an opening, a self-penalty. High Focus+Spirit → high `conc_max` → the bout/loss/hit drain crosses `T_err` later or never. The reward is *staying out of the error band*. `T_err`, `ERR_K`, error-effect `[PROPOSED]`.
- **Reward 2 — hit-disruption buffer (extend existing).** Tie the existing disruption-resistance to **current `conc/conc_max`**, not just the Focus stat — a fighter who has burned concentration is more easily disrupted by hits.

**NERS Lesson-5 guard.** Candidate positive loop (hit → drain → more errors + weaker buffer → more hits): bound the error effect and the disruption scaling with **caps**, and concentration **recovers** between exchanges (the damper). Sim must confirm it self-limits and that `T_err` rewards high-Focus without trivialising the bout.

## 8. weapon_axes_v2 revision
§2 axes — `weight | light/heavy` and `reach | short/long` → continuous (`mass`, `PoB`, lengths). §5 roster — add `mass`/`PoB`; authority, MoI, reach become derived, not declared.

## 9. Validation — mandatory after wiring (results-first)
Re-baseline: mirror=50 must hold; **re-run the per-attribute tier** (the weapon change *and* any concentration change re-base it); cap `g(authority)` so no-one-shot survives; keep choke/lunge/half-sword transitions tempo- and reach-monotonic; tune every new constant to the established targets. Nothing ships until the sim confirms good results.

## 10. Provenance / next
- **HEAD-verified this session:** the WEAPONS fields + values, the five categorical-consumer sites, HEFT/RESIST/DELIVERY/coupling, leverage, baked `geo.{cut,thrust,perc_conc}`, the concentration resource (conc_max, drains, recovery, initiative feed) + Focus levers, and the absence of any error mechanic.
- **Sourced:** densities (iron 7.86 / wood ~0.7 g/cm³); specimen masses + PoB ranges (tiers §6).
- `[RE-VERIFY]` at implementation: config scaling constants (`WEIGHT_PEN`, `ACT_WEIGHT`, `D_WT`, the K's).
- `[PROPOSED]`, vetoable: `δ_choke`, `Δ_reach`, `T_err`, `ERR_K`, the error-effect, and the per-weapon **iron-length** + **pommel-mass** descriptors the composite model needs to compute mass/PoB from geometry.
- Implement in a fresh session; pull the full per-specimen tables (Fortner numeric table, Ensis dataset, Royal Armouries records) if exact singletons are wanted.
