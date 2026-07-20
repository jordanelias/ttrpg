# Antagonist audit — BIOMECHANICS + FACTICITY lens (plan_corrected_r0.md)

All numbers computed live against C:/Github/ttrpg-morph-rearch/designs/scene/combat_engine_v1/
with the live weapon_physics/config. Code trusted over prose.

## BLOCKER — Φ_grip = S_g(g)/S_g(0) collapses thrust impact to 0 in normal play; facticity fraud
- S_g = m·|d_g|, d_g = PoB − u. at_grip clamps u_max at PoB (gather stops at CoM), so d_g→0, S_g→0 as g→1.
- COMPUTED Φ_grip at the grip a CLOSED weapon actually adopts (systems.grip_target):
  spear grip 0.865 → Φ_grip 0.135 (thrust impact = 14% of ideal)
  yari  grip 1.000 → Φ_grip 0.000 (thrust impact = 0%  — non-lethal thrust)
  ji    grip 0.666 → Φ_grip 0.335 ; guisarme grip 0.396 → 0.604
  (poleaxe/bec choke little in play → ~0.92/0.95, so blunt path mostly spared EXCEPT at full choke where →0)
- S_g in THIS codebase is the thrust-RETRACT / balance-recovery quantity (_recovery_mode_commitment,
  at_grip docstrings; combined_brief.md line 29). The plan repurposes it as thrust-DELIVERED-IMPACT.
  Physically wrong: a thrust drives ~the whole weapon mass m (invariant under grip) along the line;
  choking a spear shortens reach + improves control, it does NOT null the point. The cited sources
  (Rinaldi 2018 kinetic chain; fencing-lunge PMC10203838) say thrust force scales with body-drive/
  chain completion, NOT inversely with hand-to-CoM distance.
- FACTICITY: plan calls Φ_grip "grounded (parallel-axis static moment)". Parallel-axis grounds the
  EXISTENCE of S_g, not its use as an impact proxy. This is a recovery scalar dressed as a damage scalar.
- Contrast: Φ_room has an explicit floor (0.55) and IS grounded (Bolander interior optimum) — well-formed.
  Φ_grip has NO floor and no valid grounding.

## BLOCKER-adjacent — JD-1 dishonest: the plan's OWN default's pathology is not surfaced
- JD-1 surfaces only the *literal I_g-as-energy* variant's reach-inversion (correctly: ½·I_g·ω² at fixed ω
  gives spear 0.98 > poleaxe 0.73 > greatsword 0.51 — verified). It presents its chosen S_g-ratio as the
  clean fix and lists "spear Φ_grip(1.0)=0.0, poleaxe 0.0" as a VERIFIED FALSIFIABLE (success), never
  flagging that 0 = the reach weapon's thrust going non-lethal in the close — the exact viability the plan
  is trying to preserve. Jordan is asked to ratify S_g-ratio without being shown it zeroes yari/spear.
  The brief's test ("pathological variant surfaced as HIS decision, not silently overridden") FAILS for the
  plan's own default.

## SERIOUS — staff (and any center-balanced weapon) → Φ_grip = 0/0 = NaN, unguarded
- staff PoB=0 → S_g=0 for all g → Φ_grip = 0/0 = NaN. D2b applies the SAME Φ_grip to percussion_authority,
  which the staff routes through. NaN·(anything) = NaN → NaN heft/percussion → NaN damage. Plan D2 gives no
  floor/epsilon guard on the S_g(0) denominator. (goedendag/mace S_g>0 so spared; staff is the live NaN.)

## MINOR — M-04 magnitude misquote (self-correcting, plan flags a unit test)
- Plan says raw-u subtraction under-scales the choke "~1.57×". Actual: geometry enters reach at
  REACH_GEOM_SCALE/UNIT_M = 0.635/0.30 = 2.117 reach-units per metre; raw u = 1.0 → true factor 2.117×
  (choke removes ~47% of what it should). Fix prescribed (REACH_GEOM_SCALE·geom_slide/UNIT_M) is correct.

## CREDIT (defensible / accurate — do NOT invent problems here)
- KE-abandonment diagnosis SOUND: ½·I_g·ω² re-manufactures reach (verified); τ/I_g dimensional inversion
  makes dagger dominant (1/I_g: dagger 334.9 ≫ arming 6.65 ≫ greatsword 0.98) — verified.
- heft ideal ordering spear 0.892 < arming 0.934 < longsword 1.000 < greatsword 2.089 — verified exact.
- Φ_room: floored unimodal, interior optimum r*=0.85, energy ≤ linear in room, honors C4/Bolander —
  reproduces plan's greatsword/mace/rapier numbers at σ≈0.2–0.3. SOUND.
- Structural claims all accurate: no Contact STATE / no 'contact' TRACE_KIND / contact.axis site
  '(WS-5, unbuilt)' (M-11); reach_base ignores grip (M-03/D3); er frozen wrapper.py:32-33, longer/shorter
  :37 (M-03); select_mode receives closed, never reads it (M-05/D5); core.strike reads whole-weapon w['gap']
  + whole-weapon percussion_authority (M-02/M-08); clinch has ZERO live engine readers (C5/D9).
- Primitive-law test present (tests/valoria/test_combat_invariants.py). C1 neutral-default FIAT-flagged,
  C2 per-guard-not-class, C5 by-derivation — all handled consistent with flags.json.
