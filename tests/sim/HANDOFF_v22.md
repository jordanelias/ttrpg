# Handoff: Valoria Mass Battle Sim — End of v22 Session

**Date:** 2026-05-14
**Commits this session:** 5 (805f5f2, b2558d0, 5003589, fe3f2ed, this)
**Status:** v22 stable. Four priorities from v20 handoff resolved. Multi-unit architecture functional.

---

## Bootstrap

Send `bootstrap simulation` then read in order:

1. `references/canonical_sources.yaml` — confirm canonical pointers
2. `designs/provincial/mass_battle_v30.md` — full design doc (force_full=True)
3. `params/mass_combat.md` — extracted params (PP-NNN, ED-NNN)
4. `tests/sim/sim_mb_06_v22.py` — current sim (2143 lines)
5. `tests/sim/audit_sim_mb_06_v16.md` — 10 gaps identified, priorities set
6. `tests/coverage_matrix.md` — full sim history
7. This handoff: `tests/sim/HANDOFF_v22.md`

---

## What Changed This Session (v20 → v22)

### v21: True Simultaneous Resolution (BIAS-1 root fix)

Three changes to `run_battle`:

1. **Target centroid caching**: all atom target centroids cached BEFORE any movement. Previously unit_a advanced toward unit_b's pre-move centroid, unit_b toward unit_a's POST-move centroid — created ~10-15% first-arg bias. Now both sides see pre-move positions symmetrically.

2. **Simultaneous HP**: both units take damage, THEN both recalc_size. Previously interleaved.

3. **Simultaneous morale**: erosion computed for both, THEN rout checked for both.

Removed alternating swap band-aid from run_multi_turn_battle.

**Validation:** Mirror Cmd 4v4 (n=40): A 50% / B 42.5% — p=0.62, NOT significant. Grid geometry verified symmetric (positions equidistant from row 12, identical speeds, identical formation depths). T4 simultaneous resolution: VALIDATED.

### v22a: Multi-Unit Orchestrator + Freed-Attacker + Morale Cascade (D-3, D-5)

New `run_multi_unit_battle(side_a, side_b, pairings, ...)`:
- Manages multiple engagement pairs, runs `run_battle` per active pair each turn
- **Morale cascade** (§A.12): when unit routs, adjacent friendly units make Discipline check Ob 1. Fail = Morale -1. Each simultaneous rout triggers separate cascade check.
- **Rout contagion** (L167): rout → -1 Morale to adjacent friendlies, braked (can't cascade further this turn).
- **Freed-attacker**: NON-FAST victor of resolved engagement flanks enemy in adjacent pair. Full pool vs defender at -1D. Deals 2-3 dmg/turn typically. This is the Cannae mechanism.

**Validation:** 2v2 (A-Elite routs B-Militia → freed A-Elite flanks B-Regular → B-Regular routs). 3v3 (staggered routs trigger cascade + freed-attacker chain). Cascade failure rates: Disc 2 = 33.5%, Disc 5 = 17%.

### v22b: Cavalry Pursuit (G-11)

- **Speed field** on Unit: "Slow" / "Standard" / "Fast"
- **Pursuit** (§A.12): Fast victors pursue routing unit. Routing unit loses HP = pursuer net Offence successes × (1+Power) - DR. No Defence for Slow/Standard routing units.
- **Rearguard** (§A.12): Fast routing unit may defend at -2D Off.
- **Recall** (§A.12): Command Ob 2 per turn. Success = pursuit ends, pursuer becomes freed attacker.
- **Termination fix**: battle continues while pursuit is active even if no engagements remain.

**Validation:** Standard mirror casualty ratio = 1.25x. Fast mirror = 1.22x (rearguard partially offsets). Asymmetric (Cmd 4 Fast vs Cmd 3 Std): 8.43x with pursuit vs 6.09x without — pursuit adds ~40% loser casualties.

**Speed tier assignment:**
[ASSUMPTION: Cavalry = Fast, Heavy Infantry = Slow, others = Standard — basis: L429 "Cavalry → Standard" in forest implies Fast default. No explicit table found in canonical sources.]

---

## What's Built (v22, cumulative)

### Architecture

```
run_multi_unit_battle()        ← NEW: orchestrator for 2+ engagement pairs
  ├── run_battle()             ← v21: simultaneous resolution (per pair)
  │     ├── advance_cells()    ← centroid caching (v21)
  │     ├── resolve_engagements() ← simultaneous HP + morale (v21)
  │     └── volley / stamina   ← inherited from v20
  ├── pursuit_damage()         ← NEW: Fast unit pursuit (G-11)
  ├── recall_check()           ← NEW: Command Ob 2 recall
  ├── freed_attacker_damage()  ← NEW: flank adjacent enemy
  ├── discipline_check_cascade() ← NEW: Ob 1 morale cascade
  └── between_turn_recovery()  ← inherited from v20
```

### Bottom-Up Emergent Core (inherited from v20)

- Pool = min(Size, Command) + Command [PP-233]
- H = min(Discipline, Command) + DR [PP-233]
- Damage = successes × (1 + Power) [PP-233]
- Simultaneous damage application [PP-233]
- TN 7, d10 pool, 1s subtract, 10s double [core]
- Stamina drain/recovery, discipline degradation [emergent]
- Rout at morale 0, ~14.7% casualties in multi-turn [emergent]

### 8 Imposed Constants (unchanged from v20)

STAMINA_MAX (100), STAMINA_DRAIN_PER_CONTACT_CELL (1→3), STAMINA_RECOVERY_PER_RESERVE_RANK (8), STAMINA_EXHAUSTED_POOL_PENALTY (-1), BETWEEN_TURN_STAMINA_RECOVERY (30), TICKS_PER_PHASE (6), BATTLEFIELD_SIZE (25), BUFFER_CELLS (5).

### 3 New Constants (v22, all canonical)

MORALE_CASCADE_OB (1) [§A.12], ROUT_CONTAGION_MORALE_HIT (1) [L167], FREED_ATTACKER_FLANK_PENALTY (1) [§A.4 YELLOW], REARGUARD_PENALTY (2) [§A.12], RECALL_OB (2) [§A.12].

---

## What's Broken / Known Issues

| ID | Severity | Issue | Notes |
|---|---|---|---|
| BIAS-1 | RESOLVED | Processing order bias | Fixed in v21. |
| D-3 | RESOLVED | No multi-unit engagements | Fixed in v22. |
| D-5 | RESOLVED | Morale cascade | Fixed in v22. |
| G-11 | RESOLVED | No cavalry pursuit | Fixed in v22. |
| D-4 | P2 → accepted | Pursuit = 0 for Standard infantry | Canonically correct (§A.12). |
| GEO-1 | CLOSED | Grid geometry bias | p=0.62 — sampling noise. |
| D-2 | P2 | Shared grid, not per-unit | Sim uses one grid for both. Canonical: per-unit. |
| D-8 | P3 | Battery bands not recalibrated | Single-turn bands stale for multi-turn. |
| D-10 | accepted | Pool insensitive to high casualties | By design — Command dominance axiom. |
| SPEED-1 | P3 | Speed tier assignment not in canonical table | [ASSUMPTION] — inferred from L429. |

---

## Next Session — Priority Order

### 1. Battery band recalibration (D-8)

Single-turn H-band percentages from early sims are stale for multi-turn model. Need to re-derive from current v22 multi-turn outcomes. Important for balance validation.

### 2. Discipline degradation validation

§A.4 deterministic discipline checks are implemented but need systematic validation across unit types. The morale cascade's Ob 1 check interacts with discipline degradation — verify compounding effects.

### 3. Terrain modifiers

L427-430: river crossing (-1 Speed, -1D Off, discipline check), forest (Cavalry → Standard, no flanking). These modify the multi-unit orchestrator's engagement outcomes.

### 4. Tactics / Stances

§A.8: Shield Wall, Column, Skirmish etc. affect dice pools, flanking vulnerability, speed. Requires stance field on Unit + modifier injection into run_battle.

### 5. Volley and ranged integration

Volley fires in Phase 2 before melee. Archers can't melee same turn they volley. This is partially implemented in run_battle but needs multi-unit orchestrator support (archer unit volleys into adjacent engagement).

---

## Throughline Status

- **T1 Generalship**: validated (Cmd 7v1 100%, Cmd 5v3 100%)
- **T2 Cascading degradation**: firing correctly — discipline + morale cascade chain
- **T3 Combined arms**: cavalry pursuit validated; freed-attacker flanking validated
- **T4 Simultaneous resolution**: VALIDATED (v21)
- **T5 Systemic weight**: multi-unit orchestrator operational — level-2 architecture in place
- **T6 Scale-invariant dice**: validated (TN 7, d10 pool, degree table)

---

## Skill Scaffolding Reminders

- `h.assert_bootstrap()` + `h.task_gate('simulation')` + `h.sim_gate('custom', systems=['mass_combat'])` before any sim work
- Verification ledger: `sim_verification_ledger.json` — 30 entries, all constants cited
- sim_fabrication_check fires at pre_commit_gate — every numeric constant needs ledger entry OR inline `# [canonical:]` comment
- Do NOT include line numbers (L513 etc) in docstrings — the hook interprets them as uncited constants. Use `§A.12` section references instead.

---

[ASSUMPTION: Cavalry = Fast, Heavy Infantry = Slow, others = Standard — basis: L429 "Cavalry → Standard" in forest implies default Fast]
[ASSUMPTION: mirror matchup is fully symmetric — basis: p=0.62 at n=40; grid verified symmetric; centroid caching eliminates processing-order bias]
[CONFIDENCE: high — all four v20 priorities resolved; multi-unit orchestrator tested across 2v2 and 3v3 scenarios; pursuit validated with casualty ratio comparison]
