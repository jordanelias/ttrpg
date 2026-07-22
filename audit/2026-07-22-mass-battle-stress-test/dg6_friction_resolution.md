# DG-6 resolution — scale-invariant combat friction (per-battle CEV)

**Status: PROPOSED (grounded + calibrated + gauge-validated). ED-MB-0016. Jordan-directed 2026-07-22**
("validate emergent results top-down from historical precedent; extend code as required to resolve
standing issues using academic research, military theory, mathematics, historical precedent").

Resolves **DG-6** — the mass-battle engine's *over-decisiveness*: envelopment / force-ratio matchups
resolve to 100%/0% where the historical record shows **bands** (a 2:1 or envelopment advantage won
~65–83%, never with certainty). This is the dominant gauge-divergence class (`H2–H8`, `C1`, `C4`), open
since ED-MB-0006/0007.

---

## 1. Root cause (confirmed, mathematical)

Melee attrition is resolved by summing `N` independent per-soldier dice (`roll_pool(N)`). This is a
**self-averaging** process: its coefficient of variation shrinks as **O(1/√N)** by the Central Limit
Theorem. Measured directly in this engine:

| N (pool) | 4 | 16 | 64 | 256 | 1024 |
|---|---|---|---|---|---|
| CV of net | 0.89 | 0.49 | 0.25 | 0.12 | 0.06 |

Because the combat pool scales ~linearly with troop count (`eff_power·eff_size`), large battles get
large, near-deterministic pools → `compute_degree(net, ob)` returns a **fixed tier from the force
ratio alone** → certain, not banded, outcomes.

This is **not** an implementation bug — it is what summing i.i.d. per-soldier outcomes *does*, and the
stochastic-Lanchester literature documents exactly this vanishing relative variance at scale (Kingman
2002; arXiv:1905.03122: "stochastic effects are minimal when the odds are overwhelming"). **Refining the
attrition core cannot fix it** — the fix must add variance at a different layer.

## 2. The grounded model — a two-layer (mixture) resolution

The historical/OR literature is unanimous that real combat-outcome variance is dominated **not** by
attrition (which self-averages) but by **correlated, battle-level phenomena**: morale/rout breakpoints,
command friction, "fog of war". These are drawn *once (or a few times) per battle*, not once per
soldier, so their variance is **force-independent** — it does not vanish at scale.

**Model:** keep the self-averaging attrition core, and multiply each side's combat power by a
**per-battle, per-side combat-effectiveness (CEV) factor** drawn once per battle:

> `M_side ~ LogNormal(0, σ²)`, `σ = PC_FRICTION_SIGMA`

By the **law of total variance**, `Var(outcome) = E[Var(outcome | M)] + Var(E[outcome | M])`. The first
term → 0 as N → ∞ (the attrition core, kept — correct). The second term is driven by `M_A, M_B`, each
drawn once per battle regardless of army size, so it stays **O(1)** — the outcome probability converges
to a fixed, non-degenerate number (a band), not to 0/1.

This is the standard hierarchical/mixture structure underlying the "friction multiplier" and
"breakpoint / first-passage boundary" treatments in the combat-modelling literature. It is exactly
Dupuy's **Combat Effectiveness Value (CEV)**: a per-force multiplier on combat power capturing command,
training, morale, surprise, terrain — the human factors treated as first-class causal variables.

## 3. Grounding (citations)

**Attrition self-averages (the problem is real, not our bug):**
- J.F.C. Kingman, "Stochastic aspects of Lanchester's theory of warfare," *J. Applied Probability*
  39(3) (2002), 455–465 — canonical Markov birth-death Lanchester; self-averaging.
- "On a stochastic version of Lanchester's model of combat," arXiv:1905.03122 (2019) — variance
  vanishes under lopsided odds; non-negligible only near parity.
- Isbell & Marlow, "Attrition Games," *NRLQ* 3 (1956); Weinberg, *J. Defense Modeling & Simulation*
  (2024), DOI 10.1177/15485129241284640 — correlation across combatants is the formal lever that
  breaks CLT self-averaging (a single shared per-battle shock is the simplest such correlation).

**Variance lives at the battle scale (morale/friction), not the soldier scale:**
- A.D. Beyerchen, "Clausewitz, Nonlinearity, and the Unpredictability of War," *International Security*
  17(3) (1992), 59–90, DOI 10.2307/2539130 — friction as nonlinear, sensitive-dependent (the opposite
  of self-averaging).
- Ardant du Picq, *Battle Studies* — morale interaction, not bloodletting, is the decisive mechanism.
- D.K. Clark (1954) + The Dupuy Institute, "The 40% Rule" / "What Is A Breakpoint?" (2018/2024) —
  empirical **falsification of fixed-casualty-% breakpoints**: of 91 US WWII divisions, only 2 ever
  exceeded 30% weekly casualties, yet many broke well below — the breakpoint is a *distributed*,
  stochastic threshold, not a hard casualty line.
- D. Rowland, *The Stress of Battle* — combat effectiveness degrades as a **shared, correlated** unit
  state under fire (~15% of range effectiveness), not per-shot independent draws.
- T.N. Dupuy, *Numbers, Predictions and War* (1979) — the QJM/TNDM CEV: human factors as multipliers
  on combat power.

**Historical decisiveness bands (the calibration target — see §4):**
- The Dupuy Institute **Division-level Engagement Database (DLEDB)**, 752 cases 1904–1991: attacker
  win-rate ≈ 55% at ~1.2:1, ~62% at 1.5:1, ~66–70% at ~2:1, **74–83% at 3:1+ (plateaus, never
  certain)**. Dupuy's own QJM re-fights matched historical outcomes 92–95% — *with* all human factors,
  never 100%.
- P. Sabin, *Lost Battles* (2007) — the architectural precedent: ancient battles modelled as
  probabilistic, morale-gated, multi-*impulse* resolution (units take ~2 hits before breaking); a
  winning tactic shifts *probabilities per impulse*, never guarantees the outcome.
- Envelopment (Cannae) is **conjunctive** — center-holds × cavalry-sufficiency × terrain, each < 1.0;
  attempts *usually failed* (Frederick, Moltke, Schlieffen). Only the completed case annihilates.
  (Goldsworthy, *Cannae* 2001; Polybius 3.107–118.)
- Cavalry vs infantry is a **cohesion-state switch** (Keegan, *Face of Battle*; Waterloo squares 11/11;
  Bannockburn schiltrons) — already modelled by the Stage E brace/reach mechanic (gauge C2/C6 REPEL).

## 4. Calibration (gauge-INDEPENDENT — vs the Dupuy DLEDB curve, not the gauge)

`PC_FRICTION_SIGMA` is fixed against the **independent** Dupuy force-ratio win-rate curve, using pure
force-ratio matchups (same troop type, Line vs Line, troop-count ratios), **not** the gauge — so the
gauge stays an independent validation surface (I5: calibrate to history, not to the target).

Measured attacker win-rate (n=60/ratio) vs σ:

| σ (per-side log-SD) | 1.2:1 | 1.5:1 | 2:1 | 3:1 |
|---|---|---|---|---|
| **Dupuy target** | **55** | **62** | **70** | **80** |
| 0.0 (no friction) | 82 | 100 | 100 | 100 |
| 0.5 | 68 | 82 | 97 | 100 |
| 0.9 | 63 | 67 | 80 | 87 |
| **1.1 (chosen)** | **57** | **62** | **70** | **82** |
| 1.3 | 57 | 65 | 70 | 78 |

**`PC_FRICTION_SIGMA = 1.1`** reproduces the Dupuy curve across the whole 1.2:1–3:1 range. (The math
prediction from the analytic `P = Φ(ln R / σ_ratio)` model was σ_ratio ≈ 1.32 ⇒ σ_per-side ≈ 0.93; the
engine needs slightly more because its multi-tick resolution amplifies small pool edges — calibrated to
the data, as grounding discipline requires.)

## 5. Implementation

- `config.py`: `PC_FRICTION_CEV` (gate) + `PC_FRICTION_SIGMA=1.1`. **Default OFF** pending A/B +
  default-flip ratification (mirrors the PER_CELL / FIELD_MOVEMENT field-default precedent).
- `orchestration._draw_friction_cev(unit)`: draws `M = exp(gauss(0, σ))` **once per battle**, lazily —
  the first `run_battle` entry for a fresh unit draws it; multi-turn re-entries keep the single draw
  (per-turn re-draws would self-average the shock away). Seeded `random` stream → **I2 determinism
  holds** (verified).
- `core/exchange.subunit_combat_pool`: `raw *= unit._friction_cev` (the Dupuy CEV multiplier on the
  whole combat score). 1.0 when the gate is off → byte-exact.
- **I4**: the byte-exact grid oracle pins `PC_FRICTION_CEV=0` (like the other field gates) → grid modes
  untouched.

## 6. Validation & disclosure — friction is NECESSARY but NOT SUFFICIENT (ships gated OFF)

**Force-ratio validation (the mechanism works, vs independent Dupuy data): PASS.** With σ=1.1 the
force-ratio win-curve reproduces the Dupuy DLEDB band (§4); the mechanism-test
(`test_friction_cev.py::test_variance_does_not_collapse_at_scale`) confirms a large-force 2:1 collapses
to ≥95% (certain) WITHOUT friction and stays banded (<90%) WITH it — the scale-invariant variance is
restored exactly as designed. I1 conservation + I2 determinism hold.

**Gauge A/B (the independent tactical check): friction σ=1.1 moves the 20-row gauge 6/20 → 4/20 — it
does NOT resolve the gauge, and ships DEFAULT OFF.** Honest per-row reading:
- It *helps* several force-dominated rows band correctly (H9, C1, C3 → OK).
- But a **uniform** per-battle friction is the wrong tool for two failure classes the history research
  (dg6 §3) explicitly flagged as *not* force-ratio variance:
  1. **Envelopment (H3/H4) stays ~100%** — its over-decisiveness is **structural** (the envelopment
     geometry concentrates force), not a force-ratio the symmetric CEV noise can band. History says
     envelopment is **conjunctive** (center-holds × cavalry-sufficiency × terrain, each <1.0) — it needs
     a *conjunctive probabilistic gate*, not global noise.
  2. **Cavalry-vs-braced (C2/C6) breaks: REPELLED → NOT-REPELLED.** A braced line repelling cavalry is a
     **near-deterministic** historical outcome (Waterloo squares 11/11; Keegan). A large CEV draw now
     occasionally lets the cavalry break the wall (attacker win-rate ~5% → ~35%), *undoing* the Stage E
     brace mechanic. Friction must **not** apply to (or must be damped within) the brace repel.
  3. Near-parity/mirror rows (H1) get pushed just out of band by the added draw rate + noise.

**Conclusion:** the CEV friction is a **validated, grounded building block** for force-ratio outcome
variance — but a single global σ cannot simultaneously band the force-ratio curve AND preserve the
gauge's near-deterministic tactical outcomes (brace repel) and structural ones (envelopment). It
therefore ships **gated OFF** (byte-exact, inert). The **complete DG-6 resolution** is a composite,
scoped as follow-on: (a) this CEV friction, (b) a **conjunctive envelopment gate** (multi-probability,
per Goldsworthy/Sabin), (c) **brace-repel preservation** (exempt or damp the CEV where a braced,
disciplined, deep wall faces a frontal charge). Every magnitude here is grounded (§3) or calibrated to
independent history (§4) — **no constant tuned to the gauge**; the gauge is the independent check and it
reported the honest verdict above.
