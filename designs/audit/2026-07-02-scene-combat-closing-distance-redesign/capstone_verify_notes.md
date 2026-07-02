# Capstone verification notes — emergence-gate lens

## Constant enumeration + classification

### NEW constants the plan introduces
| Constant | Plan value | Bucket | Evidence |
|---|---|---|---|
| SWING_FLOOR | ≈0.5 | (B) SIM-CALIBRATE | plan D2 line 287 tags `[SIM-CALIBRATE]`; line 325 "SWING_FLOOR/r*/σ/floor all carry [SIM-CALIBRATE]"; I2 acc #10. OK. |
| r* (ideal-grip ref) | (unspecified) | (B) SIM-CALIBRATE | tagged D2/I2 #10 + orphan discipline. OK, but numeric value never given — see note. |
| σ (Φ shape) | (unspecified) | (B) SIM-CALIBRATE | tagged. OK |
| floor (Φ floor) | (unspecified) | (B) SIM-CALIBRATE | tagged. OK |
| ρ(g)=S_g(g)/S_g(0) | derived | (A) PRIMITIVE-DERIVED | S_g from at_grip parallel-axis (weapon_physics:468-469). Guarded ρ:=1 at S_g(0)≤ε. OK |
| ε (NaN guard) | small | (C) FIAT-numerical | guard threshold; acceptable numerical epsilon, not a physics knob. Should carry a tag but trivial. |
| pc_sel blend `pc_sel·1 + (1-pc_sel)·Φ_swing` | pc_sel derived | (A) PRIMITIVE-DERIVED **but see MUST-FIX-1** | pc_sel = selected element's geo['point_concentration'] (real primitive, geometry.py:76 passthrough). BUT the widened return (dm,h,sel_gap,sel_perc) never carries it. |
| GRIP_MIN_WORKING (0.30) | existing | (A/C) existing FIAT primitive | weapon_physics.GRIP_MIN_WORKING=0.30, already tagged [FIAT] in code line 434. Reused, not new. OK |
| close_efficacy f(measure_gap,range_avail) | shape | (B) SIM-CALIBRATE | D5; flags.json weakly_grounded (no cut-arc-truncation treatise). Tagged. OK |
| facing profile term | near-0 | (C) FIAT — C1 | D6 tags `[FIAT — C1]`. OK |
| rear_clearance | derived | (A) PRIMITIVE-DERIVED | -min over _all_parts(x-extent/2)+u(g). From located parts. OK |
| geom_slide (floored) | derived | (A) PRIMITIVE-DERIVED | min(grip_travel_max/UNIT_M, head_len-GRIP_MIN_WORKING/UNIT_M). OK |
| Beta reshape (range_avail→Beta params) | shape | (B) SIM-CALIBRATE | D4/I5; reshapes params only, no draw reorder (systems:520 one betavariate). OK |
| Φ_room on percussion | shape | (B) SIM-CALIBRATE, ablation-gated | D2b; retained on percussion (reaches sigma). OK |
| Φ_room on heft | CUT | n/a (removed) | R-8/JD-1(d); code check asserts no room operand × WP.heft. OK — correctly NOT shipped. |
| SWING retention gates (0.76/0.88) | measured | (B) measured thresholds | worst-case-across-STR gates; these are acceptance thresholds, not engine constants. OK |

### Thrust grip-invariance (Φ_thrust≡1.0)
- Keyed on `sel_head=='point'` — the SELECTED element's head token. VERIFIED per-selected-element:
  select_mode→afforded_heads→element_afforded derives the token from each mode_element's own geo,
  NO weapon name. bear_spear (single element, head='point', no mode_elements) → afforded_heads={'point'}
  → h='point'. So Φ_thrust≡1.0 fires via the selected element, not a class. CONFIRMED emergent.
- `[ASSERTED — rigid-body first principles]` label, with Rinaldi/PMC cites HONESTLY DEMOTED (D2 grounding
  para, lines 320-325). Matches recoverability_factor's own practice. OK — this is (C) legitimately, tagged.

## Two load-bearing forks

### Fork (i) — hook pull-vs-bind DROPPED, no data boolean
- D9 (lines 615-643): pull-hook hardware OUT OF SCOPE; `pull_capable`/`hook` boolean EXPLICITLY FORBIDDEN.
- I7b acc #7 (line 916-917): "no `pull_capable`/`hook` data boolean exists in weapons.py (an explicit
  grep-assertion)". PRESENT. ✓
- Verified test_no_weapon_name_literal (test_combat_invariants.py:70-82) scans ONLY weapon-NAME literals
  via AST in core/systems/wrapper — does NOT catch data booleans in weapons.py. Plan's claim (D9 line
  628-630) is ACCURATE; the grep-assertion is the correct additional guard. ✓ RESOLVED THE EMERGENT WAY.

### Fork (ii) — thrust-damage grip-invariance keyed on SELECTED ELEMENT mode
- Keyed on sel_head==point per element via systems.select_mode + _mode_elements + element_afforded.
  Confirmed genuinely per-selected-element, cannot be a name/class proxy. ✓
- BUT the pc_sel used in the cut_thrust blend (D2 line 288) + close_efficacy (D5 line 514) + swing-room
  legibility (line 489/970) is NOT carried by the widened return. See MUST-FIX-1.

## MUST-FIX-1 (SERIOUS): pc_sel is load-bearing but the return contract does not produce it
- D2 line 288-289: `Φ_grip = pc_sel·1.0 + (1−pc_sel)·Φ_swing`, pc_sel = selected element's own pc.
- D5 line 514, D4 line 489/970: close_efficacy + swing-room legibility both read (1−pc_sel).
- D2b widened return (lines 341-354, orphan table line 964): carries `(dm, h, sel_gap, sel_perc)` +
  element_afforded carries `(gap, perc, element_ref)`. NONE of these is point_concentration.
- geometry.bake (geometry.py:79): gap = gap_precision(pc, cs) — a NONLINEAR PRODUCT of pc AND cross_section.
  So sel_gap CANNOT recover pc_sel. element_ref indexes elements[] (mass), which has no pc.
- pc_sel IS available on the winning mode_element's baked geo['point_concentration'] (geometry.py:76
  passthrough) — but the plan never threads it. The I2 #2/#3 and I4 #4 gates reference pc_sel while the
  data-flow that would produce it is unspecified.
- EXACT FIX: widen the carried tuple to include sel_pc = winning element's geo['point_concentration']
  (a 5-tuple, or carry the winning element_ref AND read its mode_element geo). Add sel_pc to the orphan
  table + the Combatant fields. Minimal, in-keeping with sel_gap/sel_perc.

## Poleaxe select_mode point-selection (JD-3) — confirmed a genuine PHASE-C red, not a plan defect
- poleaxe mode_elements: hammer(blunt), beak(point pc0.60), top spike(point pc0.85). afforded_heads=
  {blunt, point}. test_use_mode_selection expected=[kama_yari,ji,bec_de_corbin,lucerne_hammer] EXCLUDES
  poleaxe (line 112). test asserts poleaxe does NOT flip → RED by design (percussion lifted above mace).
  Plan surfaces as JD-3 + accepted-red #6. HONEST. ✓

## Constants I could not fully verify numerically (numpy not run — read-only)
- The exact retention numbers (guandao 0.71-0.759, voulge 0.808-0.875, greatsword Φ0.9996) — NOT
  independently recomputed. grip_choke_max(greatsword)=0.15 VERIFIED BY HAND (grip_len 1.3, bladed,
  _gather_len=0.39m, Lu=1.3, (1.3-1.0)/2.0=0.15). Consistent with g*=0.045.
- These are surfaced as measured ranges + JD-1, not asserted as clean — appropriate.
