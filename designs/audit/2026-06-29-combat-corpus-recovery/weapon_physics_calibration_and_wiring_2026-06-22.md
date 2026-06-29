# Valoria — Weapon-Physics: Calibration + Wiring Spec (turnkey)
**2026-06-22 · scope: personal-combat / weapon · status: calibration DONE & validated · wire SPEC'd, commit gated on sim**

`[SELF-AUTHORED — bias risk]` Bootstrapped this session (token 26c398fe; live `main`, task_gate design). Calibration validated against **sourced specimen PoB** (proposal §6); physics module **self-tested** (max 0.05 cm deviation). Companion artifact: `weapon_physics.py`.

`[CORRECTION — to my own earlier statements this session]` `mass`/`pob_frac` are **not fully dead**. `core.py:27-30` already wired them: `P_auth = min(8, 9.5·(√mass · pob_frac)^0.30)` replaced the hand-set blunt `percussion` ("combat_residuals_pob_f5 §2"). The migration off categorical/dead inputs **already began in the blunt branch**; this wire extends it to `reach`/`wt`. My "F5 dead-data" claims earlier this session are stale for that branch.

`[READ: systems.py:11/17/47/57 · core.py:27-30/40/72 — the five categorical sites + P_auth]` · `[READ: weapon_physics_and_concentration_model.md §4/§6/§8]`

---

## §1 — Calibration result (validated against sourced specimens)

**Constants (physical; flagged):** `UNIT_M=0.30` m/u (length-validated) · `RHO_WOOD=700`, `RHO_IRON=7860` kg/m³ (sourced) · `D_HAFT=0.040` m (staff back-solve), `D_GRIP=0.030` m · `RHO_SWORD_GRIP=900` (wood scales + thin tang) · guard-at-cross {compound 0.30, simple 0.12, none 0} · poleaxe butt 0.22 · head-centroid {bladed 0.45, hafted-tip 0.97, hafted-block 0.88}.

**The new primitive — `pommel_kg`, back-solved from sourced PoB** (see §2). All land in the physical range and match reputation (rapier/greatsword heaviest):

| weapon | pommel_kg | weapon | pommel_kg |
|---|---|---|---|
| rapier | 0.348 | sabre | 0.195 |
| arming | 0.234 | dagger | 0.021 |
| longsword | 0.140 | paired_short | 0.202 |
| greatsword | 0.548 | halfsword | = longsword |

**Validation — every weapon in its sourced PoB envelope:**

| weapon | PoB cm | sourced range | ✓ | weapon | PoB cm | sourced | ✓ |
|---|---|---|---|---|---|---|---|
| rapier | 12.2 | 9–15.5 (Vienna×7) | ✓ | spear | 75.6 | 60–95 (heavy shaft) | ✓ |
| arming | 12.5 | 10–15 | ✓ | staff | 1.2 | ~0 (centre) | ✓ |
| longsword | 12.5 | 10–15 | ✓ | poleaxe | 22.8 | 20–45 (RA 2.67 kg) | ✓ |
| greatsword | 16.0 | 10–22 | ✓ | mace | 30.5 | 25–45 (head-fwd) | ✓ |
| sabre | 11.5 | 8–15 | ✓ | halfsword | −12.9 | rearward (choked) | ✓ |

Swords hit their ranges **by construction** (pommel fit to each); hafted weapons land from the **shaft+tip model alone** (no fitting) — independent corroboration that the class split is right.

## §2 — The structural finding (why calibration needed a new primitive)

With only `{mass, head_len, grip_len}`, **PoB is under-determined**: two swords of equal mass and length but different blade/pommel distribution balance differently, so no global constant set can place them both. The physically-correct resolution is to add the one missing primitive — **pommel mass** — and *infer it from the measured PoB* (a legitimate back-solve: pommel is real and measurable). This is exactly the descriptor the proposal §8 lists as required ("the per-weapon iron-length + pommel-mass descriptors the composite model needs"). Outcome: a **complete primitive set** `{mass, head_len, grip_len, pommel_kg, wclass, hilt}` from which PoB (and everything below) derives, matching history.

## §3 — The physics module (`weapon_physics.py`, self-tested)

Computes, from the primitive set: `PoB`, `m_head`, `MoI` (heft/swing-inertia), `static_moment`, forward extent (reach), length. **Self-test: max 0.05 cm deviation from the calibration across all 12 weapons — PASS.** Heft (MoI) orders correctly: spear 1.92 (long, hard/slow) → greatsword 0.58 → poleaxe 0.72 → rapier 0.11 (lively) → dagger ~0 (flick-fast) — the lived feel `wt='heavy'` cannot express.

## §4 — Wiring spec (the five sites; turnkey)

Replace each categorical read with a `weapon_physics` call. Current → replacement:

| site | current (systems/core) | replacement |
|---|---|---|
| `reach_base` | `L0 + LONG*(reach=='long') + HEADR*HEAD_REACH[head] + reach_adj` | `wp.reach_term(w,cfg)` = `L0 + K_REACH·fwd_extent_m + HANDS2·2H + reach_adj` |
| `weapon_tempo` pen | `WEIGHT_PEN*(wt=='heavy') + HANDS_COMMIT*(2H&heavy)` | `wp.tempo_penalty(w,cfg)` = `K_TEMPO·MoI` |
| `act_cost` | `ACT_WEIGHT*(weight=='heavy')` | `K_ACT·mass` (continuous) |
| `str_demand` | `D_WT*(wt=='heavy')` | `wp.strdemand_term(w)` = `K_STRD·static_moment` |
| `HEFT` (non-blunt) | `HEFT={'light':0,'heavy':3}` | `wp.heft_term(w)` = `clamp(K_HEFT·MoI,0,4)` |
| `P_auth` (blunt) | **already wired** `min(8,9.5·(√mass·pob_frac)^0.30)` | keep; ensure `pob_frac` = calibrated value |

Then **retire `reach`/`wt`** from `combatant.py` WEAPONS and **add `pommel_kg`** (and set `pob_frac` to the calibrated values §1) so `P_auth` and the new terms read one consistent source.

**Scale-mapping gains** `K_REACH=2.05, K_HEFT=5.2, K_TEMPO=1.5, K_STRD=0.55, K_ACT≈` are **`[SIM-CALIBRATE]`** — chosen so the new outputs sit in the engine's existing numeric ranges, but the *relative* values shift (that is the point), so they are fit in the re-baseline (§5), not asserted.

## §5 — Sim re-baseline (the commit gate — proposal §9)

The wire **deliberately changes resolution values**, so it cannot be committed unvalidated. Before any commit, run and pass:
1. **Mirror = 50** — identical fighters must hold ~50/50 (no systemic bias introduced).
2. **Attribute tier spread** — the History/Agility/Cognition-dominant ordering must survive (per the 2026-06-22 combat-analysis sims).
3. **No-one-shot `CAP_END`** — no weapon/attribute combination produces a one-exchange kill.
Harness: the `combat_engine_v1` exerciser — start at `skills/valoria-combat-simulator/scripts/combat_sim.py` and `tests/sim/sim_combat_exhaustive.py` (the v32-combat-balance suite targets the deprecated v32, not this engine — confirm before reusing). The `K_*` gains are fit here until the three checks pass.

## §6 — Handoff (fresh session — why, and exact steps)

**Commit deferred, intentionally:** wiring canonical resolution code (combat_engine_v1, ED-900-904) requires the §5 sim gate, which means reading + running the harness — and the proposal itself says "implement in a fresh session." Rushing it on remaining budget risks a half-applied edit to canonical code or a skipped sim gate. The wire is now **turnkey**:

1. Drop `weapon_physics.py` into `designs/scene/combat_engine_v1/`.
2. Apply the six §4 edits; add `pommel_kg` + calibrated `pob_frac` to WEAPONS; remove `reach`/`wt`.
3. Run §5; fit `K_*`; confirm mirror-50 / tier / no-one-shot.
4. `safe_commit` (multi-file: engine + combatant + weapon_physics) with `Citations:` (weapon_physics proposal, combatant, systems, core) + co-file updates (canonical_sources if a new module is canonicalised) + an editorial-ledger entry recording the calibrated constants, the `pommel_kg` primitive, and the sim result. Jordan-vetoable.

**Open `[SIM-CALIBRATE]`:** the five `K_*` gains. **Open `[PROPOSED]`:** `pommel_kg` values (back-solved, physical, but not specimen-measured singletons — pull Fortner's numeric table / RA records if exact values are wanted).

---
*Calibration validated against sourced specimens; module self-tested. Constants flagged. Canonical commit gated on the §5 re-baseline. Source of truth: `jordanelias/ttrpg` @ live `main`.*
