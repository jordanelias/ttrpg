# Valoria — Weapon-Physics Preliminary: Point of Balance / Heft / Leverage
**2026-06-22 · scope: personal-combat / weapon (unwired layer) · status: PRELIMINARY, Jordan-vetoable**

`[SELF-AUTHORED — bias risk: I computed this; validation is against the engine's own `pob_frac` (which may itself be hand-assigned) and the sourced specimen ranges in `weapon_physics_and_concentration_model.md §6`.]`
Bootstrapped this session (token 26c398fe; live `main`). Method is **Jordan-specified** (wood-cylinder grip → head = remainder of known mass → PoB) plus a minimal 3-class refinement for hafted weapons. **Every constant is a flagged first-pass guess.** This is the bottom-up grounding pass the unwired weapon-physics proposal needs — not final values, and nothing here is wired or canon.

`[READ: combatant.py — WEAPONS mass/head_len/grip_len/pob_frac]` · `[READ: weapon_physics_and_concentration_model.md §4/§6 — composite model + sourced masses/PoB]`

---

## §1 — The method

**Jordan's rule (the core).** A weapon's known total mass splits into a grip and a head. Model the **grip as a wood cylinder** (base diameter × grip length → volumetric mass). Whatever mass is left over is the **head mass** (`m_head = m_total − m_grip`), sitting forward. From the grip/head mass split and the lever arms, derive **point of balance, static moment (head-heaviness), and moment-of-inertia (heft/swing-weight)**.

**Why this is the right shape.** It uses the one quantity we actually know — the measured total mass — as ground truth, and only *models* the simple part (the grip). It inverts the proposal's forward model (build mass from materials) into a back-solve that can't contradict the known mass.

**The two exceptions the raw rule needs (found by running it — §3).**
1. **Material by weapon (Jordan's "wood for everything but swords").** A sword grip is steel tang + wood scales + a steel **pommel**, far denser than a wood haft and rearward-loaded — that pommel is *why* swords balance at the hand. Swords get a steel-inclusive grip density + a pommel point-mass; everything else gets wood.
2. **Hafted weapons aren't grip-plus-head.** For a spear/staff/poleaxe the long forward length (`head_len`) is mostly **wood shaft**, not iron head. Treating it as head mass throws the balance wildly forward. These are modelled as a wood shaft over the *full* length plus a small iron mass at the tip.

This yields three classes — **bladed** (grip + distributed blade + pommel), **hafted-tip** (full shaft + iron point), **hafted-block** (haft + iron head lump). They are exactly the three the proposal's §4 already distinguishes.

## §2 — Constants (all PROPOSED; calibration basis noted)

| Constant | Value | Basis |
|---|---|---|
| `RHO_WOOD` | 700 kg/m³ | ash/oak hardwood (proposal §6 source) |
| `RHO_STEEL` | 7860 kg/m³ | — |
| `UNIT_M` (length-unit → m) | 0.30 m/unit | **calibrated**: rapier (3.8 units) → 1.14 m; spear (6.7) → 2.01 m; greatsword (5.4) → 1.62 m — all plausible |
| `D_GRIP` (base grip/haft Ø) | 3.5 cm | base, per Jordan; **staff (pure wood, 1.5 kg) back-solves to 4.0 cm** — see §5 sensitivity |
| `RHO_SWORD_GRIP` | 1500 kg/m³ | steel tang + wood scales, computed effective ~1300, rounded |
| `M_POMMEL` (swords) | 0.12 + 0.07·head_len, clamp [0.15, 0.45] kg | scales with blade length (longer blade → bigger counterweight); flagged heuristic |
| head-mass centroid (frac of head_len) | bladed 0.45 · hafted-tip 0.97 · hafted-block 0.88 | distributed blade vs iron-at-point vs iron-lump |

## §3 — Pass 1: the raw uniform rule, and where it breaks (the diagnostic)

Applying Jordan's rule uniformly (wood/steel grip, `head = total − grip`, blade centroid at mid-head) ranks most weapons correctly **but mis-ranks the two physical extremes**:

- **Mace came out *under*-forward** (PoB-frac 0.31, below spear) — wrong; a mace is the **most** head-heavy weapon. Cause: its iron head is a lump at the *tip*, but the rule placed head mass at mid-head.
- **Spear came out absurdly forward** (PoB 72 cm) — wrong; a spear is shaft-balanced. Cause: `head_len = 5.5` is almost all **wood shaft**, but the rule counted it as iron head (`head = total − tiny grip = 1.8 kg` forward).

These two failures *are the result* — they show precisely why the uniform rule needs the material/centroid split (and they reproduce the proposal's §4 reasoning from scratch).

## §4 — Pass 2: 3-class refined results

`UNIT_M=0.30 · D=3.5 cm`. PoB measured from the cross (+ forward / − rearward); `PoB-frac` = PoB ÷ total length, comparable to the engine's `pob_frac`. **MoI = heft** (swing inertia about the hand). Sorted hand-balanced → head-heavy.

| weapon | class | mass | L (m) | m_head | **PoB cm** | **PoB-frac** | (existing pf) | heft (MoI) |
|---|---|---|---|---|---|---|---|---|
| longsword_halfsword | bladed | 1.4 | 1.20 | 0.06 | −42.7 | −0.36 | 0.12 | 0.31 |
| longsword | bladed | 1.4 | 1.32 | 0.39 | −12.1 | −0.09 | 0.14 | 0.17 |
| sabre | bladed | 0.9 | 0.99 | 0.29 | 0.9 | 0.01 | 0.18 | 0.05 |
| arming | bladed | 1.2 | 0.96 | 0.57 | 6.0 | 0.06 | 0.12 | 0.08 |
| greatsword | bladed | 2.7 | 1.62 | 1.55 | 12.6 | 0.08 | 0.22 | 0.53 |
| staff | hafted-tip | 1.5 | 1.68 | 0.37 | 20.0 | 0.12 | 0.05 | 0.51 |
| rapier | bladed | 1.3 | 1.14 | 0.70 | 16.6 | 0.15 | 0.10 | 0.14 |
| dagger | bladed | 0.3 | 0.33 | 0.22 | 5.3 | 0.16 | 0.25 | 0.00 |
| paired_short | bladed | 0.7 | 0.57 | 0.60 | 15.1 | 0.26 | 0.22 | 0.02 |
| poleaxe | hafted-tip | 2.5 | 1.32 | 1.61 | 41.3 | 0.31 | 0.45 | 0.79 |
| mace | hafted-block | 1.2 | 0.75 | 0.69 | 34.5 | 0.46 | 0.60 | 0.19 |
| spear | hafted-tip | 2.0 | 2.01 | 0.65 | 95.4 | 0.47 | 0.42 | 2.67 |

**Validation.**
- **Against sourced specimens** (proposal §6, the real anchor): rapier computed **16.6 cm** vs sourced **9–15.5 cm** (just forward — pommel slightly light); greatsword **12.6 cm**, pommel-counterbalanced, in range; spear shaft-balanced (frac 0.47 ≈ existing 0.42). These land.
- **Against the engine's `pob_frac`**: Spearman rank correlation **ρ = 0.69** — the gross structure is recovered (head-heavy cluster = mace/spear/poleaxe on top; hand-balanced swords on the bottom).
- **Heft (MoI)** orders sensibly: spear (2.67) and the 2H weapons highest (hard, slow); dagger/paired-short ≈ 0 (flick-fast); rapier low (0.14, lively despite reach) — matching the lived feel the categorical `wt` can't express.

## §5 — Honest residuals (all tuning, not method)

ρ=0.69, not 0.9 — three named misses, each a flagged constant, not a structural fault:

1. **Longsword & half-sword come out rearward** (−0.09 / −0.36 vs +0.14 / +0.12). The steel-grip density + pommel is **overtuned rearward** for long-gripped 2H swords. Fix: lower `RHO_SWORD_GRIP` or make the pommel grip-length-aware.
2. **Staff sits slightly forward** (0.12 vs 0.05, centered). `D=3.5 cm` under-masses the shaft, leaving a spurious ~0.37 kg "iron." At the staff-calibrated **4.0 cm** it centers. → **PoB is sensitive to haft diameter**; hand-weapon grips (~3 cm) and hafts (~4 cm) likely need different base Ø.
3. **Poleaxe too forward** (41 cm; 0.31 vs 0.45 in the field but real poleaxes are *well*-counterbalanced). My hafted-tip model has **no butt counterweight**; poleaxes carry a rear spike/queue. Fix: add a butt mass to hafted-tip.

**The honest verdict:** the method produces physically-ordered PoB and heft from the real masses, and the 3-class structure is necessary and sufficient at this resolution. The exact numbers will move once `D_GRIP` (per class), `RHO_SWORD_GRIP`/pommel, and a poleaxe butt-mass are **fit to the sourced specimen PoBs** (proposal §6) rather than eyeballed. That fit is a short calibration pass, not new modelling.

## §6 — How this plugs into the unwired engine

These derived quantities are the inputs the **dead `mass`/`pob_frac` fields** (audit F5) were added for. Per `weapon_physics_and_concentration_model.md §5`, they feed five categorical-consumer sites — `reach_base`, `weapon_tempo`, `str_demand`, `act_cost`, HEFT/impulse — replacing `reach=='long'`/`wt=='heavy'`. **Wiring requires the proposal's §9 sim re-baseline** (mirror = 50 holds; re-run the per-attribute tier; cap so no one-shot survives). Nothing ships on these numbers until the sim confirms it.

## §7 — The rest of the unwired personal-combat / weapon layer (scoped per directive)

Beyond the weapon-physics substrate, the personal-combat layer carries these specified-but-unwired items (verified this session unless noted):

- **`mass` / `pob_frac`** — dead data (F5); *this doc gives them first-pass values.*
- **`precommit` channel** — registered in `tradition.py`, **zero consumption sites** (F2); the Japanese tradition's defining channel cannot fire.
- **5 of 8 ability levers** — `seize` CUT (2026-06-05); `leverage`/`measure`/`visual`/`tactile`/`precommit`/`balance` inert pending `eff_cw` wiring; only `counter_success`/`counter_select`/`anti_overcommit` live.
- **Concentration error mechanic** — specified in the physics proposal §7 (Jordan's spec: error-onset reward + hit-disruption buffer); proposal confirms "grep-confirmed missing." Unbuilt.
- **`clinch` field** — unconsumed by traced engine paths.
- **`halfsword_target`** — keyed but neutral; German armoured-half-sword technique unexpressed.
- **`weapon_physics_and_concentration_model.md`** — the parent proposal; PROPOSED 2026-06-05, un-implemented.

---
*Preliminary. Constants flagged PROPOSED/Jordan-vetoable. Values change on calibration; the method and the 3-class split are the load-bearing claim. Source of truth: `jordanelias/ttrpg` @ live `main`.*
