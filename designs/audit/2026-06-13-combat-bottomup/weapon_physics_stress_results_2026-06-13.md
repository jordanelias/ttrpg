# Weapon-physics stress test — results (2026-06-13, PROVISIONAL)

**Verdict: the bottom-up weapon physics passes. Across 4000 random weapons whose every parameter is
bounded by the existing roster — including the physically-incoherent corners the hand-authored set never
visits — the derivations (`P_auth`, `puncture_pressure`, `M₁`) are monotone, bounded, continuous (no
cliffs), and the engine damage path stays sane (no one-shot, monotone vs armour, no negative damage). No
defect found.**

`[SELF-AUTHORED — bias risk]` Tests Claude-derived physics with a Claude-built harness; an independent
reviewer would note the harness and the derivation share authorship, so a shared blind spot would pass
silently — the checks below are therefore deliberately external (boundedness, monotonicity, damage through
the *engine's own* `core.damage`), not restatements of the derivation.
`[NULL: 4000-weapon bounded random space × 6 checks + 8 deterministic corners — examined, no pathology]`
`[READ: designs/scene/combat_engine_v1/{core,combatant,geometry,config}.py — the damage path the harness drives]`

## Method

- **Bounds** = the min/max of each parameter across the 11 real weapons (the box the random weapons inhabit):

  | param | min | max | param | min | max |
  |---|---|---|---|---|---|
  | mass | 0.300 | 2.700 | point_concentration | 0.020 | 0.950 |
  | pob_frac | 0.050 | 0.600 | cross_section | 0.400 | 0.970 |
  | head_len | 0.700 | 5.500 | edge_keenness | 0.000 | 0.900 |
  | grip_len | 0.400 | 2.800 | strike_concentration | 0.000 | 0.850 |
  | curvature | 0.000 | 0.550 | | | |

- **random_weapon**: each parameter sampled uniformly and *independently* within its bound — so the sample
  deliberately contains incoherent combinations (e.g. a keen edge with a high strike-concentration) that
  the curated roster avoids. Head assigned by a geometry classifier; the **blunt subset (1176 / 4000)** is
  where `P_auth`/`puncture` apply (the gated derivations).
- **Six checks**: (1) boundedness/finiteness; (2) monotonicity of `P_auth` in `s=√mass·pob`; (3) continuity
  (max `|ΔP_auth|` under a ±2%-of-range nudge); (4) impact-uniformity (the Lesson-2 lens); (5) engine damage
  sanity — `core.damage` with the *derived* `P_auth` across armour×degree, default defender (End 4 ⇒ fell at
  40 hp); (6) the eight (mass, pob, strike_conc) box corners.

## Results

- **[1] boundedness — 0 violations.** Every `P_auth ∈ [0,8]`, every `pierce ≥ 0`, every `M₁` finite. No
  NaN/inf anywhere in 4000 weapons.
- **[2] monotonicity — 0 breaks.** `P_auth` is non-decreasing in `s=√mass·pob`, as a function of a single
  positive quantity must be. No inversions.
- **[3] continuity — max `|ΔP_auth|` = 0.27 per 2% nudge** (on an 8-point scale), occurring in the steep
  low-`s` region. A smooth gradient, not a cliff (a cliff would be a large jump from a tiny perturbation).
- **[4] impact-uniformity — +0.05 pob raises `P_auth` by 0.248 at min mass vs 0.13 at max mass (~1.9×).**
  This is the *intended* saturating behaviour: heavy weapons sit near the cap, so a pob increment buys less
  authority there than on a light weapon. Smooth and bounded — the Lesson-2 diminishing-returns-at-the-top,
  by design, not a defect.
- **[5] damage sanity (fell @ End 4 = 40 hp): clean.** Max overwhelming single hit = **18** (< 40 → no
  one-shot); **0** one-shot kills, **0** armour-non-monotone cells (more armour never raises damage), **0**
  negative-damage cells, across the whole blunt subset × 4 armour tiers × 4 degrees.
- **[6] corners — bounded and sensible.** min mass + min pob → `P_auth` **3.23** (floored off zero by the
  saturating power — no zero-authority pathology even at the lightest, most balanced extreme); max mass + max
  pob → **8.0** (capped). `pierce = P_auth × strike_conc`: **0** at a perfectly broad face (a flat hammer
  never punctures — correct) rising to **6.8** at the ultimate-pick corner. The ordering and the bounds hold
  at every corner.

## Honest framing

- The clean verdict is *earned* by the run, not assumed: the six checks plus the deterministic corner sweep
  are the trail. By construction `P_auth` is a smooth saturating function of one positive quantity, so
  monotone/bounded/continuous is the *expected* outcome — the test's job was to confirm it holds across the
  full bounded space (incoherent corners included) and that the engine damage path does not blow up on
  out-of-distribution weapons. It does not.
- **Consistent with the standing PoB caveat.** Damage stays inside its envelope (max 18) because it flows
  through the saturating `tanh` and the `RESIST` lookup — a *derived* authority **reproduces** the existing
  damage envelope, it does not widen it. The stress test reconfirms this is numerically safe: no random
  weapon escapes the envelope. (Making the physics *shift* damage is the separate continuous-transmission
  re-baseline — PoB decision (b).)
- `[GAP: puncture magnitude unvalidated]` The pierce term remains an uncalibrated **ranking**
  (poleaxe ≫ mace), not a damage number. The corners show it bounded and correctly ordered, but it is not
  wired into damage and not validated as a magnitude.
- The `wt` (HEFT light/heavy) was assigned by a mass-median split for the damage probe; HEFT is itself
  hand-set (top-down inventory finding #3), so this is a proxy for the engine's binary class, not its actual
  assignment — it stresses the damage *ranges*, not HEFT fidelity.

## What this licenses

- Nothing new to decide. It **removes a numerical risk** from PoB decision (b) — the derived physics is
  monotone, bounded, and damage-safe even far outside the curated roster, so wiring it would not destabilise
  the damage path. It does **not** by itself argue for wiring; that remains your call.
- `[CONFIDENCE: high]` on the null — the checks are exhaustive over the sampled space and the corners are
  evaluated deterministically.

Files: `weapon_physics_stress.py` (the reusable harness), this results doc.
