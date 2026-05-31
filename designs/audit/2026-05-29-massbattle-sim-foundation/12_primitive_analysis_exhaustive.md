# Mass Battle — Exhaustive Primitive Analysis (all directions, all scales, all scopes)

**Date:** 2026-05-29
**Skill:** valoria-simulator (NERS framing: valoria-resolution-diagnostic)
**Scope:** simulation · diagnosis only (no tuning — bottom-up-primitives-only rule in force)
**Session token:** df5079812d207c7e
**Standing rule (this work):** counters emerge from bottom-up primitives ONLY; history (`precedents_warfare.md`) is the validation gate, never an input. No counter tables, no per-matchup δσ, no shape-keyed damage multipliers. This document is the diagnosis that precedes any primitive work.

`[SELF-AUTHORED — bias risk]` I spent this session installing top-down counter crutches that this rule bars; that work is retired. This analysis is the corrected footing. Challenge surface §9.

---

## VERDICT

**No — the engine does not yet have enough variables for the formation counters to emerge bottom-up, and the gaps are specific and nameable.** The engine already implements a *spatial* primitive stack that is genuinely good (per-cell facing/octagon flank model, depth-weighted support stacking, speed-based puncture, encirclement, contact frontage). What it lacks splits into two classes:

1. **Canonical primitives the DESIGN specifies but the engine never implemented** — chiefly **weapon-class × armour-class effectiveness** (§A.2 / the DR tables) and **mounted/cavalry** (charge, shock, pursuit). These are not new inventions; they are documented canon reduced to flat scalars (`power`, `dr`) in the sim. This is the single largest gap.
2. **Primitives that are too COARSE to separate the matchups** — the facing model is a 3-zone octagon (front/flank/rear) averaged over contact cells; the speed model is a small integer with no true vector/velocity; there is no reach, no FoV-gated targeting, no formation-break state with consequences. These exist but under-resolve the physics, so counters that depend on *fine* spatial advantage wash out.

The ~5/11 the pure-geometry engine produces is the direct, honest consequence: with weapon/armour collapsed to flat scalars and facing at 3-zone resolution, the geometry cannot generate enough differential to push the offensive counters (wedge, envelopment, manipular) decisively into band at realistic casualties. **The fix is to add/deepen the missing primitives — in priority order below — and re-validate against the historical bands, never to re-install a counter table.**

---

## §1 — METHOD

`[READ: sim_mb_06_v22_DB.py — FULL primitive inventory: all module constants, both dataclasses (Subunit 700–735, Unit 953–979), all 40+ methods/functions incl. advance_cells, cell_speed, support_engage_frac, octagon_angle, _per_cell_angle_mod, role_at_contact, base_combat_pool, resolve_engagements(_cascading), volley_phase, run_battle tick loop, pursuit/recall/freed-attacker]`
`[READ: designs/provincial/mass_battle_v30.md — full heading structure + §A.2 weapon effectiveness, §A.4 stat block, §A.6 formations, §A.8 tactics, §A.9 environment, §A.12 rout/pursuit, §A.14b/c campaign supply/levy]`
`[READ: params/mass_combat.md — DR tables (melee LC/HC/LB/HB × armour; projectile LP/HP/LBl/HBl), weapon-effectiveness matrix, PP-104/188/189/233/235/245/251/504/530, cavalry Dmg Mod +3/+5, artillery sight-line PP-106]`
`[READ: references/historical/precedents_warfare.md — all 326 lines, prior turn]`
`[READ: designs/scene/derived_stats_v30.md §7 TroopCount, §10.2 Army Morale, §10.4 — prior turn]`

Three-column inventory per primitive family: **ENGINE** (what `v22_DB` actually computes) · **DESIGN** (what canon specifies) · **GAP** (absent / underpowered), each tagged with the **historical counter it blocks** and the **scale/scope** it lives at.

---

## §2 — PRIMITIVE INVENTORY (what the engine ACTUALLY has)

The engine's implemented primitive stack, bottom-up:

**State primitives (dataclass fields):**
- *Subunit:* `shape, troop_type, tier, starting_position, advance_dir, stance, unit_type(melee/ranged), cell_offsets(_c), halted_cells, target_atom, cell_last_speed, cell_facing_vec, merged_cells, _moved_this_turn`
- *Unit:* `power, command, discipline(_start), morale(_start), dr, h_per_size, size(_max), hp(_max), routed, broken, stance, speed(Slow/Standard/Fast), stamina(_max)`

**Behavior primitives (the physics):**
- **Cell geometry:** `CELL_PATTERN_FN` (5 shapes), `oriented_pattern` (row-flip by advance_dir), `atom_max_width`, `cells_to_orig_coords`
- **Movement:** `advance_cells` (discipline-gated, caps at adjacency), `cell_speed` (per-cell integer 0/1/2 by shape position), `halt_before_enemy`, `_momentum_speed`
- **Facing/flank:** `octagon_angle` (3-zone GREEN<45°/YELLOW 45–90°/RED≥90°), per-cell `cell_facing_vec`, `_rotate_defender_facing` (dynamic facing on contact), `_per_cell_angle_mod` (averages `ANGLE_DEF_MOD` over contact cells)
- **Contact/engagement:** `find_contacts`, `assign_targets`, `count_engagements_per_atom`, `resolve_cross_side_contention` (speed-priority, equal-speed→co-locate), `role_at_contact` (front/tip/wing/center/gap/refused)
- **Damage:** `base_combat_pool` (min(Size,Cmd)+Cmd), `support_engage_frac` (depth-weighted: depth1=1.0/depth2=0.7/depth3=0.5), `resolve_engagements` → pool × frac × angle-mod × puncture − encirclement → `roll_pool`→`compute_degree`→`DAMAGE_BY_DEGREE`−`dr` × `CASUALTY_SCALE`
- **Resolve modifiers present:** support stacking, octagon angle, puncture (speed differential, cap 3), encirclement (−1 if ≥2 engagements), ranged-melee penalty (pool÷3)
- **Morale/rout:** `morale` erosion = dmg/(disc×cmd), rout at ≤0; `stamina` drain by contact cells; `discipline_penalty`; phase-boundary checks (stamina/morale/discipline/rally/reform/threadwork — last three stubbed)
- **Multi-turn/campaign:** `run_multi_turn_battle`, `between_turn_recovery`, `pursuit_damage`, `recall_check`, `freed_attacker_damage`, `run_multi_unit_battle`

This is a **real bottom-up engine** — the counters partially emerge (mirror 50/50, wedge slightly favored, envelopment via contact-wrap). The problem is resolution depth and missing physical dimensions, below.

---

## §3 — THE CANDIDATE VARIABLES, GRADED (your list, against ground truth)

| # | Candidate variable | ENGINE status | DESIGN status | Gap severity | Historical counter it blocks |
|---|---|---|---|---|---|
| 1 | **Vectorized pathing — velocity** | PARTIAL: `cell_speed` integer 0/1/2, `_momentum_speed`, `cell_last_speed`; used for puncture + contention | §A.8 charge, "battle pace vs marching pace" (Leuctra); cavalry charge momentum | **MEDIUM** — speed is a scalar, not a true velocity vector; no acceleration/charge build-up | Cavalry shock, oblique-order timing (Leuctra), feigned-retreat-then-turn |
| 2 | **Vectorized pathing — angle** | PARTIAL: per-cell `cell_facing_vec` (raw movement vector), but consumed only as 3-zone octagon | §A.4 octagon (canonical 3-zone); finer angle implied by "wedge concentration" | **MEDIUM** — angle exists per cell but is quantized to 3 zones before use; fine concentration lost | Wedge point-concentration vs line; refused-flank oblique angle |
| 3 | **Field of vision** | ABSENT at unit scale (octagon is a *defender-facing* arc, not a perception/targeting gate); FoV exists in personal combat (`m7_facing_fov`) only | Not specified at mass scale; artillery has a sight-line rule (PP-106) | **LOW–MEDIUM** — FoV-gated targeting would let flanks go unseen/unreacted; currently all contacts are "seen" | Surprise/ambush, rear attack going unanswered, screen/skirmisher blinding |
| 4 | **Weapon types** | ABSENT: flat `power` int; `DAMAGE_BY_DEGREE(power)` only | §A.2 + DR tables: LC/HC/LB/HB melee classes, LP/HP/LBl/HBl projectile, per-class Dmg Mod (cavalry +3/+5, HeavyBlunt vs Heavy) | **HIGH** — the single biggest gap; weapon class is canonical and entirely collapsed | Pike vs cavalry, heavy-blunt vs heavy-armour, archer marginal-in-melee (partly done via ÷3) |
| 5 | **Weapon reach** | ABSENT entirely | Implied by §A.2 weapon classes (pike/spear reach); not yet a parameter | **HIGH** — reach is *the* phalanx/pike primitive; without it a pike wall ≈ a sword line | Phalanx vs sword (Pydna's inverse — why the phalanx wins on open ground), pike-vs-cavalry, spear-hedge |
| 6 | **Armour types** | ABSENT: flat `dr` int (damage reduction) | DR tables: None/Light/Medium/Heavy × weapon class, full matrix in params | **HIGH** — armour collapsed to one scalar; the weapon×armour interaction (the core of §A.2) is gone | Heavy-infantry resilience, why blunt beats armour, why arrows fail vs heavy (partly: RANGED_DR) |
| 7 | **Mobility** | PARTIAL: `speed` (Slow/Standard/Fast) on Unit, `STANCE_SPEED_MOD`; not differentiated by troop type | §A.8 fast-units rearguard/recall; speed tiers | **MEDIUM** — mobility exists but is not tied to troop_type/armour weight (heavy ≠ slow) | Light-vs-heavy kiting, fast envelopment, skirmisher screen |
| 8 | **Mounted / cavalry** | ABSENT in battery: `troop_type='cavalry'` is a legacy field, never branched; contention code says "no cavalry in current battery / charge-through deferred" | §A.2 cavalry +5 HeavyCut, charge, pursuit; PP-245 +3 Dmg Mod; Altonian Cavalry block | **HIGH** — cavalry is fully specified canon, entirely unimplemented; charge/shock/pursuit-superiority all missing | Cannae (cavalry envelopment!), shock charge breaking lines, pursuit lethality, combined-arms |
| 9 | **Tactical cohesion** | PARTIAL: `discipline` gates advance + formation hold; `resolve_internal_collisions` (formation-break merge) IMPLEMENTED BUT NOT INVOKED ("over-tuned battery, left available") | §A.4 Discipline, PP-231/251 cohesion-as-asymmetry, formation integrity | **MEDIUM** — cohesion-under-pressure exists but is switched off; formations don't physically degrade mid-fight | Formation breaking under flank pressure, manipular flexibility vs rigid phalanx (Pydna!), rout contagion |
| 10 | **Unit discipline** | PRESENT: `discipline`, `discipline_penalty`, degradation, `MIN_DISCIPLINE` per shape, `check_drift` (shape collapses to Line below threshold) | §A.4 + PP-251 asymmetry precondition, discipline degradation | **LOW** — well-modeled; the one mature non-spatial primitive | (already supports) cohesion-loss cascade |
| 11 | **Facing directions** | PRESENT: per-cell facing vector + dynamic rotation on contact + octagon | §A.4 octagon (canonical) | **LOW–MEDIUM** — present but 3-zone-quantized (see #2) | flank/rear bonus (works); fine wedge concentration (lost) |
| 12 | **Flanking** | PRESENT: octagon YELLOW/RED, `freed_attacker_damage` (−1D flank), encirclement (≥2 engagements −1) | §A.8 envelopment, §A.4 octagon | **LOW–MEDIUM** — flanking works but is damage-side only; no FoV/reaction gate, no "flank causes break" | envelopment (works partially); flank-induced rout (missing — needs #9 invoked) |
| 13 | **Breaking formations** | PARTIAL: `routed`/`broken` bools, `check_drift` (discipline→Line), but `resolve_internal_collisions` (the mid-fight break) NOT invoked | §A.12 rout, PP-273 formation break (Discipline 0), morale cascade | **MEDIUM** — terminal break exists (rout); *progressive* formation degradation under pressure does not | progressive collapse, manipular-absorbs-and-reforms vs phalanx-shatters, fighting-withdrawal |

---

## §4 — THE TWO ROOT GAPS (synthesis)

Everything in §3 collapses to two root causes:

### Root Gap A — The weapon×armour×reach×mount matrix is collapsed to two scalars
The engine reduces all of `{weapon class, armour class, reach, mounted}` to `power` (one int → `DAMAGE_BY_DEGREE`) and `dr` (one int subtracted). **Canon (§A.2 + the DR tables) specifies a full interaction matrix** — LC/HC/LB/HB × None/Light/Medium/Heavy, projectile splits, cavalry +5, blunt-beats-armour, the artillery sight-line counter. This is the largest single source of missing counter-differential, and it is *canonical, not invented*. Without it:
- Pike/spear **reach** (the phalanx's whole advantage) does not exist → Pydna's matchups are decided by abstract contact geometry, not the reach-vs-flexibility physics that actually drove them.
- **Cavalry** does not exist → **Cannae itself is unmodellable bottom-up** (Hannibal's envelopment was *cavalry* sweeping the flanks and rear; the engine has no cavalry, so it fakes Cannae with infantry contact-wrap).
- Weapon-vs-armour gives no reason for heavy infantry to win a grind, or blunt to beat plate.

### Root Gap B — The spatial primitives are too coarse to separate fine advantages
The facing model quantizes a real per-cell angle into 3 zones and *averages* over contact cells; speed is a 0/1/2 integer; formation-break-under-pressure is switched off. So advantages that are *fine and local* — a wedge's point concentrating force on 1–2 cells, an oblique's marginal angle, a formation buckling progressively at the flank — get smeared into the average and wash out. The geometry is right in *direction* but too low-resolution in *magnitude* to push the offensive counters decisively into band.

---

## §5 — GAP → HISTORICAL COUNTER MAP (which missing primitive unlocks which battle)

| Historical counter (precedents §A.6/§A.8) | Currently emerges? | Blocked by | Needs |
|---|---|---|---|
| **Line vs Line** (mirror) | YES (50/50) | — | — |
| **Wedge vs Line** (cuneus) | WEAK | Root B (point concentration smeared by cell-averaging) | finer angle/concentration (#2,#11): weight the tip's local force, don't average |
| **Envelopment vs Line** (Cannae frontal) | PARTIAL (contact-wrap) | Root A (no cavalry — real envelopment is mounted) + Root B | cavalry (#8) for true envelopment; flank-causes-break (#9,#13) |
| **Envelopment vs Wedge** (Cannae proper) | PARTIAL | Root A (cavalry) | cavalry (#8) |
| **Refused flank vs Envelopment** (Leuctra) | PARTIAL | Root B (oblique angle + charge timing smeared) | velocity/charge timing (#1), finer angle (#2) |
| **Refused flank vs Line** (oblique) | WEAK | Root B | velocity (#1), angle (#2) |
| **Manipular vs Line** (Pydna) | WEAK/over (geometry artifact) | Root A (no reach — phalanx's edge) + Root 9 (no flexibility-vs-rigidity) | reach (#5) for the phalanx, formation-break/flex (#9,#13) for the maniple |
| **Manipular vs Wedge** | PARTIAL | Root 9 | formation flexibility (#9) |

**Reading:** the mirror is solid; every *offensive* counter is blocked by Root A (weapon/armour/reach/mount) or Root B (spatial resolution), usually both. **Cannae and Pydna — the two canonical showpieces — are the most blocked**, because Cannae needs cavalry (absent) and Pydna needs reach + formation-flexibility (absent).

---

## §6 — ALL SCALES & SCOPES (the cross-scale view)

| Scale | Primitive layer | Status | Gap |
|---|---|---|---|
| **Personal** (`derived_stats §4`, combat-armature) | weapon/armour/reach/FoV/stance — RICH in the σ-leverage combat work (M3 weapons, M5 stance, M7 FoV, M9 wounds) | the personal engine HAS the weapon×armour×reach×FoV primitives the mass engine lacks | **mass battle does not inherit them** — §A.2 says "inherits personal combat table [COMPILED]" but the sim never wired it |
| **Scene** (zoom transitions) | bridge personal↔unit | partial (Thread ops, commander personal combat PP-506) | scale-bridge for weapon/armour exists on paper (§A.2 "inherits"), not in sim |
| **Unit / settlement** (`mass_battle_v30` Part A, `derived_stats §7,§10`) | the engine analyzed here | the spatial stack is good; the matrix layer is missing | Root A + Root B |
| **Territory / campaign** (§A.13/§A.14b/c) | reinforcement, campaign supply, levy restriction | §A.14b/c are NEW canon (supply, levy) | not in sim; affect *between-battle* force quality, not the counter (lower priority for this work) |
| **Peninsula / victory** | deterministic clocks | out of scope for counters | — |

**Key cross-scale finding:** the weapon×armour×reach×FoV primitives that Root Gap A says are missing **already exist at the personal scale** (the combat-armature M3/M5/M7 modules). §A.2 *specifies* mass battle inherits the personal weapon/DR table. So Root Gap A is partly a **scale-bridge that was never built**, not a from-scratch design — the primitives exist one scale down and need lifting/aggregating to unit scale. This also connects to the `10` σ-leverage finding: the personal engine is σ-leverage-based, so lifting its primitives would naturally pull mass battle toward the σ-leverage substrate (the `10` §6 architecture question).

---

## §7 — PRIORITY ORDER (what to build first, bottom-up, validate each against the bands)

Strict priority — each step adds a primitive, then re-runs the gauge with Wilson CIs and checks emergent win-rates against the historical bands. **No counter table at any step.**

1. **[HIGHEST] Weapon-class × armour-class effectiveness (Root A).** Wire the canonical §A.2/DR matrix: replace flat `power`/`dr` with `(weapon_class, armour_class) → effectiveness`. Lift from the personal table per §A.2's "inherits." Unlocks heavy-vs-light, blunt-vs-armour, archer realism. Highest counter-differential per unit of work, and it's canonical not invented.
2. **[HIGHEST] Weapon reach.** Add reach as a primitive (pike/spear/sword/none). The phalanx/pike advantage and Pydna's physics depend on it. Pairs with #1.
3. **[HIGH] Mounted / cavalry.** Implement the canonical cavalry primitive (charge momentum, shock, pursuit superiority, +5 cut). **Required for Cannae to emerge bottom-up at all.** Branch `troop_type='cavalry'` (the field exists).
4. **[MEDIUM] Finer facing/concentration (Root B).** Stop averaging the octagon zone over contact cells; weight local concentration (the wedge tip, the oblique angle) so fine spatial advantage isn't smeared. Possibly more angle zones or a continuous angle→modifier (σ-leverage-friendly).
5. **[MEDIUM] Invoke formation-break-under-pressure.** Turn on `resolve_internal_collisions` (already implemented, switched off) with a proper flank/cohesion trigger so formations progressively degrade — unlocks manipular-flex-vs-phalanx-rigidity and flank-induced collapse.
6. **[MEDIUM] True velocity vector + charge build-up.** Promote `cell_speed` from integer to a velocity with acceleration, so charge timing (Leuctra) and cavalry shock have physical basis.
7. **[LOWER] FoV-gated targeting/reaction.** Let flanks/rear go unseen-and-unanswered (screening, surprise) rather than all-contacts-seen.
8. **[LOWER] Mobility tied to armour weight + troop type.** Heavy = slow, light = fast — feeds kiting/screening.
9. **[CAMPAIGN, separate track] §A.14b/c supply + levy** — affects force quality between battles, not the in-battle counter; defer.

**Validation discipline at every step:** after adding a primitive, run the gauge (Wilson 95% CI, n≥300 pooled ≥3 banks, the `10` method), check which historical bands the emergent win-rates now hit, and **stop adding when the bands are met** — do not over-build (NERS-N/E). If a primitive doesn't move its target counter toward band, it's the wrong primitive or wrong magnitude — diagnose, don't paper over.

---

## §8 — INTERACTION WITH THE OPEN ARCHITECTURE DECISION (`10` §6)

This analysis and the `10` σ-leverage question are now coupled, cleanly:
- **Root Gap A's primitives already exist at personal scale on the σ-leverage substrate.** Lifting them (§6) naturally moves mass battle toward σ-leverage resolution — which is `10` option B. So "strengthen the primitives bottom-up" (your directive) and "migrate to the σ-leverage core" (`10` B) may be **the same project approached from the primitive end**: build the missing primitives *in σ-leverage form* (uniform-impact δσ contributions from weapon/armour/reach/facing), and the resolution substrate migrates as a consequence.
- The `unit_b`-tie skew (investigate-2, `11`) is in the attrition rout loop; if the primitive build pulls resolution toward σ-leverage (Ob-space), that skew is mooted (no discrete-threshold tie). If any attrition resolution remains, apply the `11` simultaneous-rout fix.

**Recommendation for sequencing:** treat §7 #1–#3 (weapon/armour/reach/cavalry) as the first bottom-up build, expressed in σ-leverage form per `10`, validated against the bands with Wilson CIs. That single track advances your "bottom-up primitives only," the `10` architecture decision, and the historical-validation gate simultaneously. **All of it remains your call on scope and order — this is the diagnosis, not an authorization to build.**

---

## §9 — Independent-reviewer challenge surface `[SELF-AUTHORED — bias risk]`

1. **"You spent the session on counter tables; now you say primitives. Whiplash."** Correct — the counter-table work is retired under the rule Jordan set, and this analysis is the corrected footing. The retired work wasn't wasted: it *proved* the geometry alone gives ~5/11 and that top-down patches don't generalize, which is exactly the evidence that the missing primitives (not a table) are the real gap.
2. **"Is 'weapon×armour matrix missing' really the issue, or are you reaching for canon to look thorough?"** It's the issue and it's canonical: §A.2 + the full DR tables specify the matrix; the sim collapses it to `power`/`dr`. The sim file has no weapon-class branch and no armour-class branch — verified by full read. This is a real, large, documented gap.
3. **"Cavalry for Cannae — are you sure the engine can't fake it with infantry?"** It currently *does* fake it (contact-wrap envelopment), which is exactly why H3/H4 are geometry artifacts (`08`/`09`). Real Cannae is cavalry sweeping flanks+rear; the engine has no cavalry branch (the field is legacy/unused, contention code says "no cavalry in current battery"). Faking it is the over-fit; the bottom-up fix is cavalry.
4. **"This is a huge build. Is it scoped?"** §7 is strictly prioritized and the validation gate ("stop when bands met") bounds it. The highest-value items (#1–#3) are canonical primitives partly liftable from the personal scale, not from-scratch invention. But yes — this is a multi-session build, and I flag that honestly rather than implying it's quick. `[CONFIDENCE: high — the inventory and the two root gaps; medium — the exact priority ordering, which depends on Jordan's architecture choice]`
5. **"Did you check ALL scales?"** §6 covers personal→peninsula. The deepest finding is cross-scale (the primitives exist one scale down). I did not exhaustively read the personal combat-armature modules' internals this turn (only their manifest from `10`); the "personal scale has these primitives" claim rests on the m3/m5/m7 module descriptions, not a full re-read. `[GAP: personal-scale primitive internals not re-read this turn — basis: combat-armature handoff manifest; verify before lifting]`

---

## §10 — Next steps

- **Jordan decision:** confirm the §7 priority order, and whether to build the primitives in **σ-leverage form** (coupling to `10` option B) or attrition form. This is the scope+architecture call.
- **First build (on authorization):** §7 #1 (weapon×armour matrix, lifted from §A.2/personal table), validated against the bands with Wilson CIs. Then #2 reach, #3 cavalry.
- **Carried:** the `11` simultaneous-rout fix (apply if any attrition resolution remains); the personal-scale primitive re-read (§9.5 GAP) before lifting.
- **No primitive work begins** until you confirm scope — this is diagnosis only, per the bottom-up rule and the owner contract.

---

### Audit trail
- `[READ: sim_mb_06_v22_DB.py — full primitive inventory (constants, 2 dataclasses, 40+ methods/functions)]` · `[READ: mass_battle_v30.md — full structure + §A.2/A.4/A.6/A.8/A.9/A.12/A.14]` · `[READ: params/mass_combat.md — DR tables, weapon-effectiveness, PP-104/188/233/245/251/504, cavalry]` · `[READ: precedents_warfare.md — all 326 lines, prior turn]` · `[READ: derived_stats_v30 §7/§10.2 — prior turn]`
- `[FINDING: two root gaps — A) weapon×armour×reach×mount collapsed to flat power/dr (canonical §A.2 matrix unimplemented); B) spatial primitives (facing/speed/break) too coarse to separate fine counters]`
- `[FINDING: Cannae unmodellable bottom-up without cavalry (absent); Pydna needs reach (absent) + formation-flex (switched off) — the two showpiece counters are the most blocked]`
- `[FINDING: Root-A primitives already exist at personal scale (combat-armature M3/M5/M7); §A.2 specifies mass inherits them — the gap is partly an unbuilt scale-bridge, coupling to the 10 σ-leverage architecture decision]`
- `[ASSUMPTION: personal scale has weapon/armour/reach/FoV primitives — basis: combat-armature manifest (10), not a full module re-read this turn]`
- `[CONFIDENCE: high — primitive inventory, two root gaps, gap→counter map; medium — priority order (depends on architecture choice)]`
- `[GAP: personal-scale module internals not re-read; verify before lifting primitives]`
- `[DRIFT: B6 resolved on main; github_ops.py re-fetched]`
- `[PASS-3: verdict stands — not enough variables; gaps are weapon×armour×reach×mount (Root A, canonical-unimplemented) + spatial resolution (Root B); priority §7; couples to the 10 architecture decision; diagnosis only, no build without Jordan scope]`
