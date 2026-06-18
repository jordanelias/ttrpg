# Stage 2a combat-engine reconciliation — continuous-transmission damage (balance re-validation)
**2026-06-17 · ED-935 · reconciles `combat_engine_v1` per `combat_reconciliation_plan.md` §2 Stage 2a · status: COMMITTED (Jordan-ratified 2026-06-17)**

## Change
Replaces the tanh-saturated damage stack (HEFT-binary + tier-RESIST + tanh cap) with the ground-up LINEAR continuous-transmission model [damage_model.py / armour_axes.py, Jordan 2026-05-30, ratified 2026-06-17]:
- `damage = Impact × Coupling × Quality × DMG_SCALE (1.55)`, **NO tanh/cap** — head/strength/armour drive damage as a live gradient.
- `Impact = strength + heft`; blunt heft CONTINUOUS from P_auth (Stage 1), cut/thrust heft weight-class (continuous-mass cut-impact deferred, plan #9).
- `Coupling = DELIVERY(head) × transmit(material-resistance-per-mode) × gap(coverage)`. Tier→material per `armour_axes` presets.
- `cut_thrust` VERSATILE: `max(edge shear, half-sword puncture)` — restores the prior engine's mode-shift (HEMA half-swording vs plate).

## Emergent re-validation (Stage 1 committed vs Stage 1+2a — the emergent testing Jordan directed)
- MIRROR 52.6→50.0 (fair); mean draw across 12 weapons 3.6%→4.1% (sane).
- Reproduces canon: `armour_axes` → RATIFIED_TABLE (5×4); `damage_model` → WI anchor (Success ≈ 1 wound).
- Damage gradients RESTORED: blunt 12/12/12 (saturated-flat) → 17/14/13 (gradient); cuts collapse-then-half-sword vs plate (longsword 3→5).
- Weapon meta shifts toward reach/percussion: blunt recovers (staff 50→62, poleaxe 41→55, mace 6→12); thrust moderates from overpowered (rapier 87→72, spear 72→51); light cuts settle (arming 55→35, paired_short 70→47).
- Strength more decisive (+14 span, 65→79) — linear damage rewards force.
- Abilities preserved (vorschlag 49.9 dead; indes 52.4; mezzo 51.1).

## Emergent-derived corrections (found via testing — the Jordan-endorsed loop)
1. **Half-sword mode-shift restored** — without it cut-thrust craters vs plate (arming 27, 14% draws); restored → arming 35, 4% draws. Grounded (prior engine + HEMA).
2. **DMG_SCALE confirmed at the anchored 1.55** (1 Success ≈ 1 WI) — emergent pacing sane; no inflation needed (the mode-shift was the fix).

## Honesty
- `[CONFIDENCE: high]` emergent re-validation across mirror/stat/weapon/ability/pacing.
- `[BAL]` the weapon-meta + strength shift are genuine balance changes, ratified by Jordan 2026-06-17.
- Observation: mace low (12 vs B0) is reach-driven (short weapon vs longsword reach), not a damage bug — separate reach-tuning question.
- DEFERRED: continuous-mass cut-impact (#9); per-weapon gap-skill (folds into 2b). **2b (puncture pick-vs-plate) is next — a canon call.**
