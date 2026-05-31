# Damage — Ground-Up Rebuild

**Status:** Class-C **proposal**, Jordan-vetoable. Per Jordan directive 2026-05-30 ("redevelop damage from the ground up; pretend no formulas except how the new combat works and how health/wounds work"). **Supersedes** the inherited damage formula (`net + STR×mult + weapon_armour_mod`, the ×1/×1.5/×2/×3 multipliers, crit-doubles-mod). Built from ONLY the two grounded systems below. No canon file edited; the supersession is flagged for ratification.

`[READ: derived_stats §4.1 wound model; params/core degree tiers — this session, exact.]` `[CONFIDENCE: high — self-test 8/8 + full-roster validation; behaviours emerge from the factors, not a lookup.]`

## The two grounded systems damage bridges

- **From combat (resolution):** a contested roll yields **net** (margin) and a **degree** — Overwhelming (net ≥ 2·Ob ∧ net ≥ 3) / Success (net ≥ Ob) / Partial (0 < net < Ob).
- **To the wound model (consumer):** **WI = End + 6**; **wounds = ⌊total_damage / WI⌋**; **MW = min(⌊End/2⌋+1, 3)**; **Health = WI×(MW+1)**; −1D per wound. (End4 → WI 10, MW 3, Health 40.)

Damage is the bridge: **how much wound-capacity (WI) a blow consumes.**

## The model — Damage = Impact × Coupling × Quality

Three principled factors, each one of the variables you named, none a flat lookup:

**1. Impact (force behind the blow) = Strength + Heft(weight).**
Additive force — **no Strength × weight multiplier** (the thing you disliked is gone). Heft: light +0, heavy +3. A strong fighter and a heavy weapon both add force; they *sum*, so a strong fighter does **not** get disproportionately more from a heavy weapon (validated: the STR-gap is constant across weights). Trade-off vs the old multiplicative synergy: simpler, decoupled, addresses the dislike — flagged if you want some synergy back.

**2. Coupling (head vs armour — how much force becomes a wound) = Delivery(head) × Transmission(material, mode) × GapAccess(coverage).**
Derived from **material resistance-per-mode**, replacing the +mod table. Each head has an attack **mode** (blunt→percussion, point→puncture, all cutting heads→shear) and a **delivery** (how well it puts its mode into flesh). Each material has a **resistance** per mode:

| resist (frac stopped) | percussion | shear | puncture |
|---|---|---|---|
| none (flesh) | 0.00 | 0.00 | 0.00 |
| cloth (gambeson) | 0.10 | 0.35 | 0.15 |
| mail | 0.20 | 0.80 | 0.45 |
| plate | 0.30 | 0.95 | 0.70 |

Transmission = 1 − resistance; a **puncture** additionally takes the better of through-the-material or the **gap** (coverage), so a thrust finds gaps vs plate and bursts rings vs mail. This makes the entire weapon-vs-armour matrix *emerge*: cut deflected by plate, point through the gaps, blunt transmits, thrust beats mail — all derived, no per-weapon rows.

**3. Quality (degree of success, from the contest) = Partial 0.6 / Success 1.0 / Overwhelming 1.5.**
Replaces "crit doubles the weapon mod." The σ-leverage contest — the whole of how the new combat resolves — *is* what sets Quality. A clean/telling blow transfers more force.

**Calibration:** one constant `DMG_SCALE = 1.55`, set so an **even Success hit from an average fighter ≈ 1 WI** (one telling blow ≈ one wound). Everything else scales from that anchor. The constant is tunable; the structure is the design.

## Validated behaviours (8/8 self-test + roster)

- **Anchor:** even Success, STR4, light cut vs none = 8 ≈ 0.8 WI (≈ 1 wound). ✓
- **Degree scales:** Partial 5 < Success 8 < Overwhelming 13. ✓
- **Heft (additive):** heavy 15 > light 8; STR-gap constant across weights (additive, not multiplicative). ✓
- **vs plate (emergent matrix):** cut 2 (deflected) < point 3 (gaps) < blunt 13 (transmits). ✓
- **vs mail:** cut 3 < point 5 (the rise of the thrust). ✓
- **Pacing:** unarmoured ~3–5 clean hits to fell; vs plate a cut takes 14 (useless), blunt/grapple 4 — the duel/battlefield split falls out of the coupling. ✓
- **Coverage:** partial-plate takes more than full-plate (bare zones). ✓
- **Duel decisiveness:** an Overwhelming blow unarmoured = 1.3–2.6 wounds — when the σ-contest is won, it tells. ✓

## What it supersedes / unifies (flagged for ratification)

- **Replaces** the STR multiplier lookup (×1/×1.5/×2/×3) → derived **Impact** (additive) + **Coupling**.
- **Folds in** the weapon-vs-armour mod table (W1/W5) → the **Coupling** (one mechanism, no double-count of armour). The matrix the ratified table encoded now *emerges* from material resistance-per-mode and reproduces the same relationships (cut→0 vs plate, blunt high, point gaps).
- **Replaces** crit-doubles-weapon-mod → the **Quality** factor (smooth degree scaling).
- The wound model (WI, MW, Health) is **unchanged** — damage feeds it in its own units.

## NERS + over-engineering guard

- **Necessary/Elegant:** three intuitable factors (force / head-vs-armour / how-well-landed); the player reasons "heavier + cleaner + the right tool for that armour." No lookup tables to memorise.
- **Robust:** holds across the roster and all armour tiers; the matrix emerges rather than being hand-set per weapon.
- **Smooth:** consumes the engine's native (net, degree) and produces wound-model units directly; one calibration constant.
- **Over-engineering guard:** **no per-body-part damage, no separate weapon base-damage table, no damage-type subsystem beyond the three modes.** The coupling is a 3-mode × 4-material resistance grid — a function of head and material, as directed — not a per-weapon lookup.

## What remains yours (contract)

1. **Ratify** the model + its supersession of the inherited damage formula (this is canon-touching by direction).
2. **Additive vs multiplicative Strength** — confirm you want force additive (STR + heft, no synergy), or want some STR×weight synergy back.
3. **Calibration** — `DMG_SCALE` and the resistance grid are tunable seeds; sign off or adjust the target pacing.
4. **In-world** naming untouched.

`[ASSUMPTION: an even Success hit ≈ 1 WI is the right anchor (one telling blow ≈ one wound); flag if you want hits lighter (more grind) or heavier (more swing).]`
`[GAP: ranged/projectile damage not covered here (ED-129-adjacent) — this is melee; flag if you want ranged folded into the same Impact×Coupling×Quality frame.]`
