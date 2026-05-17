# VALORIA — Mass Battle Integration Spec (v18 / sim/provincial/massbattle.py)

## Status: CANONICAL — Pass 2n authoring 2026-05-17

## Scope: integration plan for porting the sim_mb_06_v22 mass-battle feature set into sim/provincial/massbattle.py and companion modules. Inventory of currently-implemented v22 features (PRESENT in sim_mb_06_v22 line, requiring port to v18 armature) and the deferred features that v22 surfaced but never built (rally / reform / threadwork hooks, cell displacement ripple, LETHALITY restoration, equal-speed tiebreaker, internal-collision discipline trigger, flanking detection in resolve_engagements).

## Companion canon: `designs/provincial/mass_battle_v30.md` (CANONICAL, approved 2026-04-17). This doc does NOT supersede mass_battle_v30; it specifies what implementation in sim/ must cover, identifies gaps, and orders the work.

## GD constraints: GD-1 binding. Mass battle resolution produces faction stat / territorial-control deltas only. No `mass_battle_outcome → game_victory` triggers permitted at this scale (per `canon/02_canon_constraints.md` §B GD-1).

## Sources of authority:
- `designs/provincial/mass_battle_v30.md` — canonical mass battle design (Part A TTRPG, Part B BG, Part D World Bridge, Part E Battle Consequences)
- `params/mass_combat.md` — extracted params (PP-NNN, ED-NNN)
- `tests/sim/sim_mb_06_v22.py` — current sim (2143 lines, tested mass-battle implementation)
- `tests/sim/sim_audit_v5_to_v22.md` — comprehensive feature audit
- `tests/sim/HANDOFF_v22.md` — v22 session end-state
- `tests/sim/battery_report_v22.md` — D-8 calibration analysis
- `canon/02_canon_constraints.md` §B GD-1
- `canon/mechanics_index.yaml` entry: `mass_battle`

---

## 1. Module decomposition

The current `sim_mb_06_v22.py` is a 2143-line monolith. Port into the armature decomposes it across multiple modules per `sim/CONVENTIONS.md`:

| Concern | Target module | Notes |
|---|---|---|
| Top-level orchestrator | `sim/provincial/massbattle.py` | `resolve_mass_battle`, `run_multi_unit_battle`, `run_battle`, `run_multi_turn_battle` |
| Unit classes + stats | `sim/provincial/units.py` | Unit, Subunit, Cell dataclasses; stat 1-7 floats per §A.4 |
| Tactic cards | `sim/provincial/tactic_cards.py` | Card pool + pool modifiers (contested per Jordan diagnosis 2026-05-17) |
| Volley / ranged | `sim/provincial/massbattle.py` (sub-module) | Phase 2 VOLLEY_TN=6 |
| Phase boundary hooks | `sim/provincial/massbattle.py` | `stamina_check`, `morale_check_phase`, `rout_resolution`, `rally_check`, `reform_check`, `threadwork_check` |
| Stamina model | `sim/provincial/massbattle.py` (sub-module) | per-contact-cell drain + phase recovery |
| Cavalry pursuit | `sim/provincial/massbattle.py` (sub-module) | Speed field, recall Ob 2 |
| Mass-battle Thread ops | `sim/thread/operations.py` | Called via cross_scale handoff; mass-scale damage formulas in massbattle |
| Domain echo back to strategic | `sim/cross_scale/domain_echo.py` | Battle result → faction Mil/Morale/territory state |
| Battle consequences | `sim/peninsular/accounting.py` (Part E §E.1 / §E.2) | Immediate + accounting consequences |

`massbattle.py` itself stays under 600 lines by delegating to sub-modules and to `units` / `tactic_cards` companions.

---

## 2. Feature inventory — what to port (currently PRESENT in v22)

These features are functional in `sim_mb_06_v22.py` and validated. Port directly to `sim/provincial/massbattle.py`. Source: `sim_audit_v5_to_v22.md` Summary table + HANDOFF_v22.md.

### 2.1 Core resolution loop

| Feature | Intro version | v22 status | Port priority |
|---|---|---|---|
| Pool variant C-ii (Bii formula) | v6 | PRESENT (active default) | P0 |
| Per-cell movement (`cell_offsets`) | v5 | PRESENT | P0 |
| 25×25 battlefield + 5-cell buffer | v5 | PRESENT | P0 |
| Per-cell facing (`cell_facing_vec`) | v6 | PRESENT | P0 |
| Engagement angle FRONT/FLANK/REAR (GREEN/YELLOW/RED octagon) | v6/v10 | PRESENT | P0 |
| ANGLE_DEF_MOD = {GREEN: 0, YELLOW: -1, RED: -2} | v6 | PRESENT | P0 |
| Octagon facing model | v10 | PRESENT | P0 |
| Per-cell octagon angle (`_per_cell_angle_mod`) in `resolve_engagements` | v11 | PRESENT | P0 |
| Column-local targeting | v12 | PRESENT | P1 |

### 2.2 Sub-phase cascading + cell support

| Feature | Intro version | v22 status | Port priority |
|---|---|---|---|
| F-i Cell support stacking (`SUPPORT_WEIGHTS={1:1.0, 2:0.7, 3:0.5}`) | v8 | PRESENT | P0 |
| F-ii Puncture (pool bonus only, no displacement) | v8 | PRESENT | P0 |
| F-iii Cascading sub-phases (`CASCADING_ENABLED`, `MAX_SUB_PHASES=5`) | v8 | PRESENT | P0 |
| Tip support gap (`TIP_SUPPORT_GAP=2`) | v7 | PRESENT (default no-op at gap=2) | P1 |

### 2.3 Volley + ranged + Thread

| Feature | Intro version | v22 status | Port priority |
|---|---|---|---|
| Phase 2 Volley (VOLLEY_TN=6) | v9 | PRESENT | P0 |
| Unit-type field (melee/ranged) | v9 | PRESENT | P0 |
| Ranged-melee pool penalty (`pool/3`, strengthened v12 from `/2`) | v11/v12 | PRESENT | P0 |
| Mass-battle Thread ops (offensive Thread own phase, ED-050) | v30 canon | partial — calls into thread layer | P1 |

### 2.4 Phase boundary architecture (v14)

| Feature | Intro version | v22 status | Port priority |
|---|---|---|---|
| TICKS_PER_PHASE=6 architecture | v14 | PRESENT | P0 |
| `phase_boundary` dispatcher (called every 6 ticks) | v14 | PRESENT | P0 |
| `stamina_check` hook | v14 / v15-filled | PRESENT | P0 |
| `morale_check_phase` hook | v14 / v15-filled | PRESENT | P0 |
| `rout_resolution` hook | v14 / v15-filled | PRESENT | P0 |

### 2.5 Stamina model (v15)

| Feature | Intro version | v22 status | Port priority |
|---|---|---|---|
| G-1 Stamina (per-contact-cell drain, v22 re-model) | v15/v20 | PRESENT | P0 |
| `STAMINA_DRAIN_PER_CONTACT_CELL` (1→3 per stage) | v20 | PRESENT | P0 |
| Stamina phase-boundary recovery (recovery=8 per reserve rank) | v15 | PRESENT | P0 |
| Stamina exhausted pool penalty (-1D) | v15 | PRESENT | P0 |
| `STAMINA_MAX = 100` | v15 | PRESENT | P0 |
| `BETWEEN_TURN_STAMINA_RECOVERY = 30` | v20 | PRESENT | P0 |

### 2.6 Multi-turn structure (v16+)

| Feature | Intro version | v22 status | Port priority |
|---|---|---|---|
| `run_multi_turn_battle` structure | v16 | PRESENT | P0 |
| Continuous effective_size (float, not floored) | v16 | PRESENT | P0 |
| `h_per_size = min(Discipline, Command) + DR` | v16 | PRESENT | P0 |
| Casualty-pct morale triggers (30% / 50%) | v16 | PRESENT | P0 |
| Between-turn recovery | v20 | PRESENT | P0 |

### 2.7 Simultaneous resolution (v21 BIAS-1 fix)

| Feature | Intro version | v22 status | Port priority |
|---|---|---|---|
| Target centroid caching (BEFORE any movement) | v21 | PRESENT (BIAS-1 root fix) | P0 |
| Simultaneous HP application (both units take damage, THEN both recalc_size) | v21 | PRESENT | P0 |
| Simultaneous morale (erosion computed for both, THEN rout checked for both) | v21 | PRESENT | P0 |

Validation reference: Mirror Cmd 4v4 n=40 → A 50% / B 42.5%, p=0.62 NOT significant. T4 simultaneous resolution validated.

### 2.8 Multi-unit orchestrator + tactical interactions (v22)

| Feature | Intro version | v22 status | Port priority |
|---|---|---|---|
| `run_multi_unit_battle(side_a, side_b, pairings)` | v22a | PRESENT | P0 |
| Morale cascade Ob 1 on rout (adjacent friendly units Discipline check Ob 1, fail = Morale -1) | v22a | PRESENT — `MORALE_CASCADE_OB = 1` (§A.12) | P0 |
| Rout contagion (-1 Morale to adjacent friendlies, braked — can't cascade further this turn) | v22a | PRESENT — `ROUT_CONTAGION_MORALE_HIT = 1` (L167) | P0 |
| Freed-attacker flanking (non-Fast victor of resolved engagement flanks enemy in adjacent pair, full pool at -1D) | v22a | PRESENT — `FREED_ATTACKER_FLANK_PENALTY = 1` (§A.4 YELLOW) | P0 |

Validation: 2v2 + 3v3 staggered routs → cascade + freed-attacker chain. Cascade failure rates Disc 2 = 33.5%, Disc 5 = 17%.

### 2.9 Cavalry pursuit (v22b — G-11)

| Feature | Intro version | v22 status | Port priority |
|---|---|---|---|
| `Speed` field on Unit ("Slow" / "Standard" / "Fast") | v22b | PRESENT | P0 |
| Pursuit damage (Fast victors pursue routing unit; routing unit takes HP = pursuer net Offence × (1+Power) - DR; no Defence for Slow/Standard routing units) | v22b | PRESENT (§A.12) | P0 |
| Rearguard (Fast routing unit may defend at -2D Off) | v22b | PRESENT — `REARGUARD_PENALTY = 2` (§A.12) | P0 |
| Recall check (Command Ob 2 per turn → pursuit ends, pursuer becomes freed attacker) | v22b | PRESENT — `RECALL_OB = 2` (§A.12) | P0 |
| Battle continuation while pursuit active even if no engagements remain | v22b | PRESENT | P0 |

Validation: Standard mirror casualty ratio 1.25x. Fast mirror 1.22x (rearguard offsets). Asymmetric Cmd 4 Fast vs Cmd 3 Std = 8.43x with pursuit vs 6.09x without (~40% loser casualty increase).

[ASSUMPTION — sim_mb_06_v22 SPEED-1 marker: Speed tier assignment is not in a canonical params table. Inferred from L429: Cavalry = Fast, Heavy Infantry = Slow, others = Standard. Resolution pending — see §6 unresolved-canonical-questions below.]

### 2.10 Volume constants (v22, all canonical)

Port these constants verbatim to `sim/provincial/massbattle.py` module-level:

| Constant | Value | Canon source |
|---|---|---|
| `STAMINA_MAX` | 100 | §A.7 stamina spec |
| `STAMINA_DRAIN_PER_CONTACT_CELL` | 3 (v20 re-model from 1) | §A.7 |
| `STAMINA_RECOVERY_PER_RESERVE_RANK` | 8 | §A.7 |
| `STAMINA_EXHAUSTED_POOL_PENALTY` | -1 | §A.7 |
| `BETWEEN_TURN_STAMINA_RECOVERY` | 30 | v20 patch §A.7 |
| `TICKS_PER_PHASE` | 6 | v14 architecture |
| `BATTLEFIELD_SIZE` | 25 | §A.3b |
| `BUFFER_CELLS` | 5 | §A.3b |
| `MORALE_CASCADE_OB` | 1 | §A.12 |
| `ROUT_CONTAGION_MORALE_HIT` | 1 | §A.12 |
| `FREED_ATTACKER_FLANK_PENALTY` | 1 | §A.4 (YELLOW) |
| `REARGUARD_PENALTY` | 2 | §A.12 |
| `RECALL_OB` | 2 | §A.12 |
| `ROUT_FLOOR_LOSS_PCT` | 0.20 | v15 G-2 / §A.12 |
| `VOLLEY_TN` | 6 | §A.7 Phase 2 |
| `RANGED_MELEE_POOL_DENOMINATOR` | 3 | v12 patch (strengthened from 2) |
| `SUPPORT_WEIGHTS` | {1: 1.0, 2: 0.7, 3: 0.5} | v8 F-i |
| `MAX_SUB_PHASES` | 5 | v8 F-iii |
| `TIP_SUPPORT_GAP` | 2 | v7 |
| `CASCADING_ENABLED` | True | v8 F-iii |
| `ANGLE_DEF_MOD` | {GREEN: 0, YELLOW: -1, RED: -2} | §A.4 octagon |
| `BLOCK_SIZE` | 100 | v19 (problem source — see §3.1 below) |
| `LETHALITY_SCALE` | **TO BE RESTORED** (target 0.10 baseline, calibration §3.1) | §A.7 |

---

## 3. Deferred work — features specified but not built / broken

These are the issues raised in `sim_audit_v5_to_v22.md`. Resolve during v18 port, in priority order. Each gets a sim/ module assignment.

### 3.1 LETHALITY_SCALE restoration (Audit Issue 1, **highest severity**)

**Problem.** v17 introduced `LETHALITY_SCALE = 0.10` to calibrate ~15% casualties per 3-phase engagement. v18 kept it. v19 dropped it alongside switching HP model from `Size × h_per_size` (~5 HP per soldier-equivalent) to `Size × BLOCK_SIZE` (100 HP — 20× inflation). Rationale stated in v19 header: "HP = TroopCount; damage = soldier casualties (no scaling)." But the damage formula `(1+Power) - DR ≈ 3-5 per success` was unchanged, applied to 20× more HP.

**Effect.** Single-engagement `run_battle` cannot produce decisive outcomes in 18 ticks. The v9-v18 historical battery (calibrated against decisive single engagements) returns 100% draws on v22. Multi-turn structure was added to compensate but calibration was never redone — formation advantages accumulate over 5-10 turns and amplify into landslides. Multi-turn battery shows 2/13 in-band.

**Fix decision per Pass 2n.** Restore `LETHALITY_SCALE` with a multi-turn-aware target:

- Damage formula applies LETHALITY_SCALE multiplier: `damage_applied = floor(LETHALITY_SCALE × ((1 + Power) × net_successes - DR × defender_size))`
- Calibration target: ~15% casualties per single-engagement turn under T3 equal stats (P4/C4/D5/M6, mirror Line vs Line)
- Initial value: LETHALITY_SCALE = 0.10 (v17 baseline)
- Validation gate: D-8 battery `tests/sim/battery_v22.py` must run within new band ranges (NOT v9 single-turn bands — see §3.2)

**Implementation:** `sim/provincial/massbattle.py` core damage step.

[PROVISIONAL: 0.10 starting value untested at v22's multi-turn structure. Calibration sweep required at first port — adjust toward ~14-16% per-turn casualty target.]

### 3.2 Battery band recalibration (Audit Issue 6 + battery_report_v22 D-8)

**Problem.** v9 single-turn bands (in `tests/sim/sim_mb_06_v9_historical_spec.md`) are not appropriate for v22's multi-turn model. Per `battery_report_v22.md` analysis: in multi-turn, contact frontage becomes dominant — wide formations (GappedLine, RefusedFlank) crush narrow ones (Arrowhead, Horseshoe), reversing historical correctness.

**Root cause per battery_report.** `resolve_engagements` treats all contact as equal. Missing mechanics:

1. **Flanking detection**: cells contacting enemy's non-front row should apply octagon facing modifier (YELLOW -1D, RED -2D per §A.4). Currently per-cell facing is computed but the engagement loop does not check it against enemy formation position.
2. **Penetration morale shock**: a wedge tip cell that advances past enemy's front row should cause morale erosion proportional to penetration depth.
3. **Formation integrity check**: when cells are displaced from their pattern shape (e.g., wedge tip pushed back, breaking arrowhead), apply discipline-like penalty.

**Fix decision per Pass 2n.** The bands are canonically correct (historically derived). The sim is wrong. Build the three missing mechanics, then re-run battery against original v9 bands. Do NOT adopt "interim bands" — they describe broken behavior.

**Implementation order:**
1. Flanking detection in `resolve_engagements` — single highest-impact fix. Makes Horseshoe and Arrowhead work.
2. Penetration morale shock — makes Arrowhead punch above contact width.
3. Formation integrity check — discipline penalty for cell pattern disruption.

**Implementation:** `sim/provincial/massbattle.py` `resolve_engagements`.

### 3.3 Cell displacement ripple (Audit Issue 3, **high severity**)

**Problem.** Jordan's v13 design (quoted in v13 manifest): *"if a phase ends and a subunit cell like cavalry is occupying the same spot as an opponent, then the opponent cells will shift back to accommodate them."* Documented as deferred in v13: *"Charge-through (cavalry past static infantry) and end-of-phase displacement: deferred — no cavalry in current battery."* Now cavalry exists (v22 G-11); displacement still isn't built.

**Effect.** F-ii (v8) added pool bonus from speed differential but no physical displacement. Cavalry that pierces a line gets +D and stops at adjacency. Penetration is not modeled physically; only as a stat bonus.

**Fix per Pass 2n.** Implement displacement ripple in `resolve_cross_side_contention`:

- When a high-speed cell forces overlap with a lower-speed cell, the loser shifts back one cell along the attacker's vector
- If that displaces another cell of the loser's unit, propagate (chain displacement)
- Chain length gated by discipline check (Ob 1 per chain link, fail breaks formation cohesion for that subunit)
- Discipline penalty for cells displaced through this mechanic on subsequent ticks (-1D until reform fires)

**Implementation:** `sim/provincial/massbattle.py` `resolve_cross_side_contention` + chain-displacement helper.

### 3.4 Equal-speed contention tiebreakers (Audit Issue 4, medium severity)

**Problem.** `resolve_cross_side_contention` skips ties (`if a_speed == b_speed: continue`). Trace shows Arrowhead vs Line at speed-1 each → 5-16 cells of cross-side overlap per tick that persist post-contention.

**Effect.** Cells from opposing sides occupy same grid positions during engagement. Octagon facing computes angles between same-position cells (degenerate geometry). Encirclement counts may be inflated.

**Fix per Pass 2n.** Jordan's v13 rule: size tiebreaker, then random.

```python
if a_speed == b_speed:
    if a_size > b_size:    winner = 'a'
    elif b_size > a_size:  winner = 'b'
    else:                  winner = random.choice(['a', 'b'])
    # winner stays in place; loser reverts to prev_offset
```

**Implementation:** `sim/provincial/massbattle.py` `resolve_cross_side_contention`.

### 3.5 Phase-boundary hooks (Audit Issue 5, medium severity)

**Problem.** Three v14-introduced phase-boundary hooks remain empty stubs: `rally_check`, `reform_check`, `threadwork_check`. v15 implemented stamina and morale hooks; these three never got mechanics.

**Effect.** Units don't rally (degraded morale never recovers within a battle), don't reform (formations don't re-cohere after disruption), Thread ops don't fire during battle (no narrative-state integration).

**Fix per Pass 2n.**

| Hook | Implementation |
|---|---|
| `rally_check` | Per §A.4 / §A.12 canonical: Command check Ob 2 each phase boundary. Success → +1 Morale (cap at starting Morale). Failure → no change. Allow rally only if current Morale > 0. Routing units cannot rally — they pursue Recall path instead. |
| `reform_check` | Discipline-gated. At phase boundary, if subunit has cells out-of-pattern (geometric drift > 2 cells from intended formation position) AND unit not currently engaged this phase, attempt Discipline check Ob 2 to restore positions. Success → cells move 1 step toward pattern. Failure → cells held until next phase boundary. |
| `threadwork_check` | TBD pending Thread canon implementation. Initial stub: invokes `sim/thread/operations.py` cross-scale handoff if any Thread practitioner present in unit AND offensive Thread phase fired this turn (§A.10). |

**Implementation:** `sim/provincial/massbattle.py` phase_boundary dispatcher fills the three stubs.

### 3.6 Within-side formation hold (Audit Issue 2, medium severity)

**Problem.** `resolve_internal_collisions` implemented on Subunit at v13 but has 0 call sites. Jordan's v13 design (manifest quote): *"a cell of troops joining another cell of troops... that cell will have a vector that faces the midpoint... subunits abandoning their subformation where cells merge partially/completely into other cells is a tactical failure... this comes down to discipline."* Disabled because it "over-tuned battery 12/13 → 9/13" without paired discipline-gated trigger.

**Fix per Pass 2n.** Wire `resolve_internal_collisions` with bad-facing trigger:

- Internal collision penalty fires only when colliding cells have facing vectors >90° divergence (geometric "tactical failure," not blanket merger)
- Penalty: subunit-level Discipline -1 for current phase
- Cells revert to closest valid pattern position if reform_check (§3.5) succeeds next phase boundary

**Implementation:** `sim/provincial/massbattle.py` post-movement step; call `resolve_internal_collisions` on each subunit with bad-facing filter.

### 3.7 `halt_before_enemy` resolution (Audit Issue 7, low severity)

**Problem.** Function body comment: *"over-run correction disabled."* Called twice but does nothing. Redundant with `resolve_cross_side_contention`.

**Fix per Pass 2n.** Delete the function. Its prior intent (preventing over-run) is fully handled by `resolve_cross_side_contention` + §3.3 displacement ripple. Trace the two call sites and remove them.

**Implementation:** `sim/provincial/massbattle.py` cleanup.

### 3.8 STAMINA_DRAIN model documentation (Audit other-observations)

**Problem.** v15 → v20 changed semantics from `16/tick uniform` to `per-contact-cell variable`. v15 calibration is no longer valid. Wide-contact formations now drain stamina faster (GappedLine penalized more than Horseshoe). Not a regression but undocumented model shift.

**Fix per Pass 2n.** Document the semantic in module docstring + params/mass_combat.md update. No code change.

**Implementation:** `sim/provincial/massbattle.py` docstring + params/mass_combat.md amendment in companion commit.

### 3.9 POOL_VARIANT C-ii uncited constant (Audit other-observations)

**Problem.** C-ii pool formula uses `max(base × 0.5 × engage_frac, base × troops_frac × engage_frac)`. The `0.5` is uncited (not in patch ledger).

**Fix per Pass 2n.** Either canonize (add to params/mass_combat.md with patch number) or remove. Default: canonize with explicit derivation note pending Jordan ratification.

**Implementation:** params/mass_combat.md edit in companion commit. Sim code unchanged pending Jordan decision.

[PROVISIONAL: canonization-of-0.5 deferred to Jordan ratification.]

---

## 4. v22 → v18 migration plan

Steps to migrate the working `sim_mb_06_v22.py` into the `sim/` armature:

### 4.1 Step 1 — Bare port (no behavior change)

1. Copy `sim_mb_06_v22.py` → working file at `sim/provincial/massbattle.py`
2. Extract Unit / Subunit / Cell dataclasses → `sim/provincial/units.py`
3. Extract `FACTION_TACTIC_CARD_POOL_MODIFIERS` dict → `sim/provincial/tactic_cards.py`
4. Add module docstrings per `sim/CONVENTIONS.md`
5. Run `tests/sim/battery_v22.py` against new module path — expect IDENTICAL output to v22 baseline
6. Commit step 1 only after byte-equivalent outputs verified

[PROVISIONAL: byte-equivalence target may need to flex if dataclass extraction changes call signatures. Acceptable if statistical equivalence (Mirror Cmd 4v4 still p>0.05) holds.]

### 4.2 Step 2 — Fix LETHALITY_SCALE (§3.1)

1. Restore `LETHALITY_SCALE = 0.10` in damage formula
2. Run T3 mirror at n=40 — verify ~15% casualties per turn (target range 14-16%)
3. Run D-8 battery `tests/sim/battery_v22.py` — record new results
4. Iterate LETHALITY_SCALE within 0.05-0.20 if T3 casualty target missed
5. Commit step 2 with calibrated LETHALITY_SCALE value cited

### 4.3 Step 3 — Build flanking detection (§3.2 priority 1)

1. Add per-engagement flanking check in `resolve_engagements`: identify cells contacting enemy non-front rows
2. Apply ANGLE_DEF_MOD per octagon facing (YELLOW -1D, RED -2D)
3. Re-run D-8 battery — expect Horseshoe and Arrowhead in-band restoration
4. Commit step 3

### 4.4 Step 4 — Build penetration morale shock (§3.2 priority 2)

1. Detect wedge tip cells past enemy front row
2. Apply morale erosion per penetration depth
3. Re-run battery — expect Arrowhead in-band against Line
4. Commit step 4

### 4.5 Step 5 — Cell displacement ripple (§3.3)

1. Build chain-displacement helper in `resolve_cross_side_contention`
2. Discipline check Ob 1 per chain link
3. Verify cavalry penetration produces physical line break (manual trace test + battery)
4. Commit step 5

### 4.6 Step 6 — Equal-speed tiebreakers (§3.4)

1. Add size tiebreaker + random tiebreaker to `resolve_cross_side_contention`
2. Verify no persistent same-position cell overlap (trace check)
3. Commit step 6

### 4.7 Step 7 — Phase-boundary hooks (§3.5)

1. Implement `rally_check` (Command Ob 2)
2. Implement `reform_check` (Discipline Ob 2)
3. Stub `threadwork_check` (cross-scale handoff)
4. Verify single-turn battery still in-band, multi-turn shows recovery dynamics
5. Commit step 7

### 4.8 Step 8 — Internal collision wiring (§3.6)

1. Wire `resolve_internal_collisions` with bad-facing filter
2. Run battery — verify discipline penalty fires only on geometric tactical failure
3. Commit step 8

### 4.9 Step 9 — Cleanup (§3.7, §3.8, §3.9)

1. Delete `halt_before_enemy`
2. Document STAMINA_DRAIN semantic shift
3. Decide on POOL_VARIANT 0.5 canonization
4. Commit step 9

### 4.10 Step 10 — Integration with strategic layer

1. `sim/cross_scale/domain_echo.py` consumes battle result → faction Mil/Morale/territory deltas
2. `sim/peninsular/accounting.py` integrates §E.1 + §E.2 consequences
3. `sim/provincial/faction_action.py` invokes `resolve_mass_battle` for Military Conquest (HR-8 / §B GD-1)
4. Commit step 10

---

## 5. Test plan

Tests under `sim/tests/provincial/test_massbattle.py` mirror the v22 verification structure:

| Test | Purpose | Gate criterion |
|---|---|---|
| `test_pool_formula_c_ii` | Verify C-ii pool computation | Output matches PP-233 worked example |
| `test_octagon_facing` | Verify YELLOW -1D / RED -2D fires correctly | Per-cell angle test grid |
| `test_simultaneous_resolution` | Mirror Cmd 4v4 n=40 | p > 0.05 (validated 2026-05-14: p=0.62) |
| `test_multi_unit_orchestrator` | 2v2 cascade chain | Cascade fires; freed-attacker flanks |
| `test_cavalry_pursuit` | Casualty ratio with/without pursuit | Asymmetric ~40% loser casualty increase |
| `test_d8_battery` | D-8 historical battery | After §3.2 fixes: 12/13 in-band v9 spec |
| `test_lethality_calibration` | T3 mirror casualty per turn | 14-16% per turn |
| `test_phase_boundary_hooks` | rally / reform / threadwork fire | Smoke test each hook |
| `test_displacement_ripple` | Cavalry breaks line | Cells shift back along attacker vector |
| `test_gd_1_no_victory_trigger` | mass_battle never returns game-end victory | Output type assertion |

Battery `tests/sim/battery_v22.py` continues as canonical historical-band gate. Co-file `tests/coverage_matrix.md` updated each commit per pre_commit_gate.

---

## 6. Unresolved canonical questions (forward-flagged)

These canon-level questions are surfaced by the v22 audit but require Jordan ratification before sim work continues past relevant step. Each gets a stub editorial-ledger entry at Pass 2k.

| ID | Question | Source | Blocks step |
|---|---|---|---|
| SPEED-1 | Canonical Speed tier table (Cavalry / Heavy Inf / others). v22 has [ASSUMPTION] inferred from L429. | sim_audit Other observations + HANDOFF_v22 §SPEED-1 | Step 1 acceptable as-is; ratify before step 10 |
| POOL-0.5 | The 0.5 multiplier in POOL_VARIANT C-ii — canonize or remove? | sim_audit §3.9 | Step 9 |
| D-2 | Shared grid vs per-unit grid — sim uses shared, canon may require per-unit | HANDOFF_v22 D-2 | Step 10 (strategic integration) |
| D-8-interim | Should "interim bands" (broken-multi-turn bands) be canonized as fallback? Pass 2n says NO. | battery_report_v22 | Already resolved no in this doc; ratify in Pass 2k ED |

[PROVISIONAL: this section enumerates canonical questions surfaced by sim work. Resolution is Jordan's; resolutions feed into Pass 2k editorial-ledger batch.]

---

## 7. Cross-references

### Companion canon (NOT superseded by this doc)

- `designs/provincial/mass_battle_v30.md` — full design (Part A TTRPG / Part B BG / Part C resolved editorial / Part D World Bridge / Part E Battle Consequences). This integration spec implements Part A + selected Part B mechanics in sim/.
- `params/mass_combat.md` — all PP-NNN and ED-NNN params referenced by canon
- `designs/scene/combat_v30.md` §9 (Mass Combat TTRPG-scale)
- `designs/scene/combat_v30.md` §11 (Faction Unit Rosters)

### v22 sim artifacts (consumed; not canon)

- `tests/sim/sim_mb_06_v22.py` — source-of-truth implementation
- `tests/sim/sim_audit_v5_to_v22.md` — audit identifying §3.1-§3.9 issues above
- `tests/sim/HANDOFF_v22.md` — v22 session end-state + priority order
- `tests/sim/battery_report_v22.md` — D-8 calibration analysis
- `tests/sim/sim_mb_06_v9_historical_spec.md` — historical-band canonical target
- `tests/sim/audit_sim_mb_06_v16.md` — 10-gap analysis (earlier audit)

### v18 armature integration points

- `sim/provincial/massbattle.py` — port target (this doc's primary subject)
- `sim/provincial/units.py` — Unit / Subunit / Cell classes
- `sim/provincial/tactic_cards.py` — tactic card pool (contested per Jordan diagnosis — content audit pending)
- `sim/provincial/faction_action.py` — invokes `resolve_mass_battle` for Military Conquest (GD-1 enforcement boundary)
- `sim/cross_scale/domain_echo.py` — battle result → faction state propagation
- `sim/peninsular/accounting.py` — §E.1 / §E.2 battle consequences
- `sim/thread/operations.py` — mass-battle Thread ops (§A.10)
- `canon/mechanics_index.yaml` — `mass_battle` entry; v22_features_pending field updated to "specced in canon" post-commit

### Canon governance

- `canon/02_canon_constraints.md` §A P-01..P-15 (Foundations — Coherence rules referenced by Thread integration)
- `canon/02_canon_constraints.md` §B GD-1 (no mass-battle game-victory triggers)
- `canon/02_canon_constraints.md` §B GD-2 (deterministic threat response — Muster mandatory triggers may invoke mass battle indirectly)
- `references/canonical_sources.yaml` — co-file updated in commit alongside this doc

---

## 8. Test status declaration

This integration spec is CANONICAL design content. The mechanical contents (constants, formulas, references) trace directly to existing canon (`mass_battle_v30.md`, `params/mass_combat.md`) and tested sim artifact (`sim_mb_06_v22.py`). Items marked [PROVISIONAL] are the calibration values and uncertain assumptions that require Pass 2n step-2-onward implementation testing to confirm.

The integration plan (§4 steps 1-10) is the test plan. Each step has a verification gate. Steps 4-7 unlock canonical-band restoration per §3.2.

[STATUS: CANONICAL — Pass 2n authoring 2026-05-17. Implementation gated per §4 step sequence. Calibration values [PROVISIONAL] pending step-2 sweep.]

---

## 9. Changelog

- **v30 init (2026-05-17, Pass 2n):** Initial authoring. Mass battle integration spec for v18/sim armature. Inventories v22 PRESENT features for port; specifies §3.1-§3.9 deferred work with implementation decisions; sequences §4 10-step migration; defines §5 test plan; forward-flags §6 unresolved canon questions to Pass 2k ED batch. Companion to `mass_battle_v30.md` (does not supersede).
