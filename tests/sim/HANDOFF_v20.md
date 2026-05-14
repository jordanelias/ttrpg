# Handoff: Valoria Mass Battle Sim — End of v20 Session

**Date:** 2026-05-13
**Last commit:** `e15e3bc` (v20 grid symmetry + processing order fix)
**Status:** v20 stable. 9 commits this session. Bottom-up emergent core achieved.
**Next priority:** true simultaneous resolution (eliminates 10% side bias, structural fix for T4)

---

## Bootstrap

Send `bootstrap simulation` then read in order:

1. `references/canonical_sources.yaml` — confirm canonical pointers
2. `designs/provincial/mass_battle_v30.md` — full design doc
3. `params/mass_combat.md` — extracted params (PP-NNN, ED-NNN)
4. `tests/sim/sim_mb_06_v20.py` — current sim
5. `tests/sim/audit_sim_mb_06_v16.md` — 10 gaps identified, priorities set
6. `tests/sim/sim_mb_06_v16_manifest.md` — manifest for last formal version
7. `tests/coverage_matrix.md` — recent sim history (trimmed; older entries archived in git)
8. This handoff: `tests/sim/HANDOFF_v20.md`

---

## What's Built (v20)

**Bottom-up emergent core:**
- HP = TroopCount = Size × BLOCK_SIZE (100). At Company scale: Size 4 = 400 soldiers = 400 HP.
- Damage = soldier casualties from dice (pool/TN/DR). No scaling knobs.
- effective_size = HP / BLOCK_SIZE (continuous float). Pool: `floor(min(eff_size, Command) + Command + penalties)`.
- Morale erosion: `damage / (discipline × command)` per tick. Morale is float. **No threshold, no floor.**
- 30% rout EMERGES from canonical stats: morale=6, dmg~3/tick, disc=5, cmd=4 → erosion 0.15/tick × 40 ticks × 0.75% dmg/tick = 30% casualties to rout.
- Stamina drain: proportional to cells in contact (formation-emergent). Recovery: per reserve rank at phase boundary.
- Multi-turn battle orchestrator: 3-phase cap per engagement turn, alternating processing order between turns.
- Discipline degradation: phase-boundary check using cumulative effective_size loss, asymmetric.
- Standard infantry cannot pursue (canonical §A.12). Pursuit deferred to G-11 (Fast units).

**Imposed constants remaining (8):**
STAMINA_MAX (100), STAMINA_DRAIN_PER_CONTACT_CELL (3), STAMINA_RECOVERY_PER_RESERVE_RANK (8), STAMINA_EXHAUSTED_POOL_PENALTY (-1), BETWEEN_TURN_STAMINA_RECOVERY (30), TICKS_PER_PHASE (6), BATTLEFIELD_SIZE (25), BUFFER_CELLS (5). All structural or stamina-tuning. Down from 15 at start of session.

---

## What's Verified

- T1 Generalship dominance: Cmd 7 vs 1 = 100% win in 1.4 turns. Cmd 5 vs 3 = 100% in 4.8 turns. Cmd 4 vs 4 mirror = 61/35 (post-fix).
- 30% rout threshold: emerges from formula, validated at 29.7-29.8% across matchups (n=80).
- Winner casualties ~22%, loser ~30%. Ratio 1.4x (historical 2-5x — pursuit closes this gap, deferred).
- 100% rout rate (battles end by morale, not HP destruction).
- Battle length: 4 turns to rout at default stats. ~6 turns with grid symmetry adjustment.

---

## What's Broken / Known Issues

| ID | Severity | Issue | Notes |
|---|---|---|---|
| BIAS-1 | P2 | First-arg processing order bias in `run_battle` | unit_a takes ~1% more damage/turn. Alternating processing fixes 100/0 → 61/35 in mirror. **Root fix: true simultaneous resolution.** |
| D-4 | P2 | Pursuit damage = 0 for Standard infantry | Canonically correct (§A.12) but kills winner/loser casualty divergence. Cavalry (G-11) needed. |
| D-5 | P2 | Morale cascade prototyped but not committed | Discipline check Ob 1 — professionals resist 92%, levy fails 36%. Flat -1 morale on failure. **Real cascade mechanism is freed-attacker, not morale check.** |
| D-2 | P2 | Shared grid, not per-unit | Sim uses one 25×21 grid for both units. Canonical: per-unit grids with boundary interaction. |
| D-3 | P2 | No multi-unit engagements | 2v1, 3v1, 2v2 not modeled. Adjacent allies should join. |
| D-8 | P3 | Battery bands not recalibrated for multi-turn | Single-turn battery (H1-H13) draws at max_turns=18. Multi-turn amplifies formation advantages (HS/Line 80%+). |
| D-10 | accepted | Pool insensitive to high casualties | At eff_size 0.5, pool still 4. Command dominance axiom — by design. |

---

## Next Session — Priority Order

### 1. True simultaneous resolution (BIAS-1 root fix)

**Why first:** unresolved T4 violation, polluting all multi-turn results. Until fixed, asymmetric matchups are skewed ~10% in favor of first-argument unit.

**Mechanism:** In `run_battle`, calculate ALL effects for both units (damage, movement, stamina, morale erosion) BEFORE applying any. Currently the loop processes unit_a fully then unit_b fully.

**Implementation:**
- Refactor the tick loop: collect all damage values for both sides, apply them simultaneously
- Move resolution into two phases: COMPUTE (gather all damage/effects) then COMMIT (apply to state)
- Test: mirror matchup should produce 50/50 ± noise

### 2. Freed-attacker mechanic

**Why:** When one unit routs, the victor is FREE to attack adjacent enemies from the flank. This is the actual Cannae mechanism. More impactful than the morale cascade check (which rarely fires for professionals).

**Mechanism:** In multi-unit orchestrator, when unit X routs in engagement pair (X vs Y), Y becomes a "free attacker." On the next battle turn, Y joins an adjacent engagement as a reinforcement (2v1).

**Prerequisite:** Multi-unit orchestrator (D-3) needs proper state. Currently prototyped but not committed.

### 3. Multi-unit engagement orchestrator (D-3, D-5)

**Why:** The actual battle architecture. Single 1v1 engagement is a building block; multi-unit is the level-2 layer.

**Mechanism:** `run_multi_unit_battle(pairs)` where pairs is a list of engagement pairs. Each turn:
1. All pairs run their 3-phase engagement (parallel or alternating)
2. After all complete, check for new routs
3. Apply morale cascade to adjacent allies (Disc check Ob 1, fail = -1 morale)
4. Apply freed-attacker (winning unit from routed pair joins adjacent engagement)
5. Between turns: stamina recovery, no HP recovery

Prototype exists in chat history — needs to be promoted to sim file and tested.

### 4. Cavalry (G-11)

**Why:** Creates the historical 2-5x winner/loser casualty divergence through pursuit. Currently 1.4x because Standard infantry can't pursue.

**Mechanism:** Speed attribute (Slow/Standard/Fast). Fast units:
- Get charge bonus on first contact (impact phase)
- Can pursue routed units (each turn: routed unit loses Size = pursuer net Offence successes)
- Recall: Command Ob 2 (over-pursuit risk per §A.12)

### 5. Battery band recalibration (D-8)

**Why:** Multi-turn model amplifies formation advantages (Cannae-style envelopment SHOULD win 80%+ at equal stats). Old v14 bands (H3 50-65%) were single-turn. New bands need to reflect strategic composition dominance (M3 throughline).

**Mechanism:** Jordan design decision. Propose new bands per matchup based on multi-turn results.

---

## Skill Scaffolding Reminders

- `h.assert_bootstrap()` at session start
- `h.task_gate('simulation')` before any sim work — fetches required files
- `h.sim_gate('custom', systems=[...])` requires ledger entries for all constants
- `h.safe_commit(additions, deletions, message)` — only valid commit path
- Commit message format: `[scope] description — PP-NNN / ED-NNN`. Valid scopes: bugfix, cleanup, compilation, editorial, fix, godot, infrastructure, patch, phase, simulation, skill
- `g.safe_session_close(new_log, bootstrap_log)` at end
- Ledger: `/home/claude/sim_verification_ledger.json` — every mechanical constant needs `sim_variable`, `value`, `canonical_source`, `quoted_text`
- Forbidden token grep: never `Galbados`. Use `Solmund`.
- Pre-commit hook checks: sim_fabrication_check, forbidden_token_gate, commit_message_gate, co-file rules

---

## Throughline / Meta-Throughline Framework

Use for next session's prioritization:

**Throughlines:** T1 Generalship (validated, structural), T2 Cascading degradation (firing correctly), T3 Combined arms (well-served), T4 Simultaneous resolution (VIOLATED — fix priority 1), T5 Systemic weight (level-2 architecture pending), T6 Scale-invariant dice (validated)

**Meta-throughlines:** M1 General IS the army (structural via T1+T2+T5), M2 One-directional degradation (working), M3 Strategic composition > tactics (working, amplified in multi-turn)

**Methodological:** bottom-up > top-down (constant), canonical + emergent (constant), historical + gameplay (constant), validation cycle (constant), granular logging (constant)

---

## Trajectory Anchor

**Started:** lethality too high (units die in 7 ticks), 15 imposed constants, single-turn battles, no architectural clarity.

**Now (v20):** 8 imposed constants, multi-turn battles with 4-zoom architecture, 30% rout emergent from canonical stats, bottom-up TroopCount HP, T1 validated empirically.

**Heading:** True simultaneous resolution → freed-attacker → multi-unit → cavalry → battery recalibration. Each step removes a knob or adds emergent depth. The 1.4x casualty ratio closes toward 2-5x historical with pursuit.

---

[GAP: side bias — root cause identified (processing order), partially mitigated (alternating turns), full fix requires simultaneous resolution refactor]
[ASSUMPTION: 8 imposed constants are the structural minimum — basis: stamina parameters and grid dimensions cannot be derived from canonical stats; further reduction requires changing the underlying game model]
[CONFIDENCE: high — emergent morale erosion formula validated across asymmetric stat matchups; 30% rout point stable at 29.7-29.8% across H1/H3/H5/H7 matchups]
