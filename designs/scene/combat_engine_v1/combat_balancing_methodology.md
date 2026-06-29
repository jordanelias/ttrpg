# Combat — Variable-Balancing Methodology (scene-combat WS-8)

**Status:** Methodology + instrument doc (mechanical-tier; not canon-gated). The numbers in §7 are a measured
point-in-time baseline, not balance targets. Instrument: `workbench/balance.py`.

This is the repeatable method every combat-tuning pass runs through — the attributes/dice/calculations the
workbench (WS-6) exposes, the morphology gains (WS-2), the tradition effectiveness functions and the
imposition cyclic/cost (WS-4/WS-5). It consolidates the repo's existing balance practice into one place so
"how do you balance the variables" has a concrete, cited answer rather than eyeballing.

Grounded in: `designs/audit/2026-05-14-balance-audit/` (variance calibration, quasibinomial, Monte-Carlo),
`designs/audit/2026-05-29-combat-armature/weapon_balance_proposal.md` (weapon-only + attribute-parity two-pass,
the duel-vs-battlefield contextual principle), `designs/audit/2026-06-22-combat-analysis/` (marginal-attribute
table, reach-grounding), and the `r8_parity_harness` Class-M method constants (the single source for trial
count / Wilson z / acceptance band — `balance.py` imports them, never re-declares).

## 1. Statistical core — analytical ⇄ Monte-Carlo, ±2pp

The continuous engine's degree distribution is computable in closed form (`workbench/probabilities.py`:
`net ~ Normal(mu·pool + soft_cap(net_sigma)·sigma_n, sigma_n)` banded by `core.degree`). Validate any
Monte-Carlo result against the analytical distribution; they must agree within **±2pp** (the 2026-05-14
calibration standard; MC at N≈100k matches analytical to ±0.3pp). Every mechanical constant a sweep owns
carries a verification-ledger citation (the sim-fabrication gate). The ratified dice distribution is the
smooth continuous engine (Jordan Q4, 2026-05-15) — VFIVE board-game sampling was rejected for the videogame.

## 2. Decoupling & attribution — one factor, position-swapped, mirror = 50

To attribute an effect cleanly: vary **one** factor against a uniform baseline; **position-swap** (run half
the trials with A/B as written, half swapped) to cancel the first-mover/aggressor-alternation artifact;
attribute as decisive −1/0/+1; confirm the **mirror cell sits at ~50%** (fairness — a mirror that drifts off
50 is a bug, not a finding). Report a **Wilson 95% CI**; the parity noise floor is **±2–3pp at N≈3000**
(`r8.FINAL_TRIALS`/`WILSON_Z`; acceptance band `r8.BAND_LO`–`r8.BAND_HI` = 0.40–0.60). `balance.py` does the
position-swap + Wilson CI by construction.

## 3. Two-pass audit — weapon-only THEN attribute-parity

Run **both** passes and compare (the 2026-05-29 lesson — Strength dominance was a *weapon* problem, not an
attribute one):
- **weapon-only** (`weapon_matchup_table`): neutral build both sides, vary only the weapon, all-vs-baseline ×
  armour. Surfaces weapon imbalance isolated from stats.
- **attribute-parity** (`attribute_parity_table`): equal-budget builds, raise one attribute, measure the
  marginal point. Surfaces stat imbalance.
If an imbalance moves under the weapon fix, it was a weapon problem; budget against the marginal table, not the
cumulative endpoints.

## 4. Multi-parameter JOINT optimization, not single-knob

Weapon balance is a joint fit (3 damage classes × 4 armour tiers × speed × reach × N weapons). Two coupled
advantages (e.g. reach-at-distance + heavy-damage on a long heavy weapon) cannot be separated by any single
knob — the 2026-05-29 convergence finding. Tune the grid jointly; a single-knob pass that "fixes" one cell
usually breaks another.

## 5. Contextual / paradigm balance — C1, the principle that answers asymmetry

**You do not flatten asymmetric options to sameness.** Balance the **unconditional** mean flat and let
**context flip the conditional** advantage — ratified **C1: no option globally best**. The precedent is
duel-vs-battlefield: the war-hammer isn't duel-balanced; it owns the armoured press, and *that* is correct.
The in-engine instance is phase-dependent reach (reach wins the approach, inverts in the bind). This is the
rigorous form of the scene-combat "preferred paradigm": each fighter/weapon/tradition has a context where it
wins; the balancing requirement is that the **unconditional win-rate over all opponents/contexts is level**
(`tradition_field_table`), while matchup tables stay deliberately spiky.

## 6. Ablation gate — every new lever must move outcomes

A lever (ability, channel, morphology term, imposition gate) that does **not** move outcomes beyond the noise
floor is cut, not kept — the proven-inert `seize` precedent (re-adding a washed-out mechanic is lever-pile).
Before shipping any WS-2/WS-4/WS-5 lever: ablate it (run with/without) on `balance.py` and require a non-zero,
bounded delta, or retire it.

## 7. Current baseline (measured 2026-06-28, N=300/cell — point-in-time, not targets)

Run `python workbench/balance.py all 3000` for the publication-grade pass; this quick read already shows the
shape the methodology is meant to manage:

- **Weapons (vs arming):** reach-dominated — spear 91 · rapier 88 · staff 84 … arming 49 · dagger 31 · mace 28.
  Matches combat_analysis §2 (r≈0.83 reach, mace/dagger tank). A healthy *matchup* spread (§5); the duel table
  is not meant to be flat.
- **Attributes (marginal +1):** cog +26 · strength +20 · agi +20 · history +15 … disp +4.5 (≈neutral by design,
  "both poles cost"). Ranking matches combat_analysis §1.
- **Traditions (unconditional vs field):** spread **6.8pp** (spanish 51.9 … none 45.1) — **exceeds the ±2–3pp
  band**. The channel-weight vector is not vacuum-balanced (none is *lowest*, so the weights give a systematic
  edge). This is the empirical confirmation of `combat_tradition_representation_alternatives` (the scalar vector
  cannot specialize AND balance) and the **baseline §C's re-architecture must beat**: the WS-4 tradition model
  (affinity budget + abilities-as-access) has to bring this spread inside the band while staying qualitatively
  distinct (C1), or it falls back to keep-bias.
- **UPDATE 2026-06-29 — WS-4 dissolution landed; §C PARTIALLY met.** The affinity point-buy budget (every
  tradition normalised to an equal total) + the imposition gate (default on) **fixed the `none` injustice**
  (45.1→~49, no longer lowest) and beats the keep-bias baseline on spread + qualitative differentiation. BUT the
  new **C1 contextual test** (`balance.tradition_context_matrix`, tradition×weapon, 5 contexts) shows full
  context-balance is **not** achieved: only **2 distinct leaders** across the 5 contexts (the top cluster is
  noise-tight — two runs disagreed on the non-spanish leader), with **spanish broadly strong** (clean niche at
  rapier = its measure paradigm) and **chinese broadly weak** (never leads, ≤47.6%). The residual is channel
  **LEVERAGE** (some channels move win-rate more than others, so a shape emphasising them — spanish's
  measure/balance — wins across contexts; chinese's burst loses across them). Equalising the *budget* removed the
  gross total-competence edge but not the per-channel leverage. **Closing it** = the effectiveness-functions
  calibration (normalise each channel's marginal value so each paradigm is decisive in *its* context), which is
  design-laden (paradigm-strength = Jordan's call) — run `balance.py context` to re-measure after any change.

## How to use it

1. Make a change behind a workbench scratch preset (Class-C/B only; Class-A guarded).
2. `balance.py all` (or the workbench Monte-Carlo) — read the three tables.
3. Check: mirror ≈ 50; matchup tables spiky (good); unconditional means inside ±2–3pp; the changed lever passed
   its ablation.
4. Promote on ratify (the workbench emits the patch + ledger stub).
