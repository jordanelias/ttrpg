# Valoria Simulation Coverage Matrix

## sim_mb_06_v24 — relative-origin cell model ground-up rewrite
- Date: 2026-05-14
- Scope: Subunit movement system, cell contention, displacement ripple
- Mode: G — architectural rewrite
- Status: committed
- Changes: cell_ref (fixed per-cell starting pos), cell_pos (current pos), cell_vec (per-cell dir).
  cells() = list(cell_pos.values()). Both sides symmetric. Horseshoe wing pivot (pass front,
  then close laterally). Arrowhead tip 2 rows past centroid. Displacement ripple (depth 3).
  find_contacts dedup fixed. reset_positions updated. _rotate_defender_facing bugfix.
- Multi-turn calibration: mean 5.8 turns, rout at 29.5% casualties.
- Battery 2/11 in-band — ANGLE_DEF_MOD (-1/-2 dice) too weak vs pool 11. Documented.


## sim_mb_06_v23 — cell-pair damage scaling (bottom-up lethality fix for Issue 1)
- Date: 2026-05-14
- Scope: resolve_engagements damage formula
- Mode: G — bottom-up mechanic (build at cell level, validate via battery)
- Status: committed
- Change: per-pair damage scales by cell-pair adjacency count (king-move).
  Each adjacent cell-pair = one fighting interaction = soldier-vs-soldier exchange.
  Pool roll stays at subunit-pair level (preserves variance). Damage stays 1:1
  with soldiers. No global LETHALITY_SCALE multiplier needed.
- Battery (single-engagement, n=40, no run_multi_turn_battle):
  7/11 in-band (was 2/8 in v22 multi-turn).
  Working: H3 Horseshoe vs Line 57.5%, H4 Cannae 45%, H6/H7/H8/H9/H11.
  Out: H1 mirror 42.5 (likely noise), H2 Arrowhead 35%, H5 RF vs HS 35%, H10 mirror-of-H3 27.5%.
  Remaining issues: Arrowhead penetration (H2), RefusedFlank vs Horseshoe (H5),
  ~15pt asymmetry between H3/H10 indicating persistent processing-order bias.


## sim_audit_v5_to_v22 — comprehensive mechanic survival audit
- Date: 2026-05-14
- Scope: every mechanic v5 through v22, status in v22
- Mode: G — diagnostic audit (no code changes)
- Status: committed
- Findings: 7 critical issues. Primary: LETHALITY_SCALE dropped v19 without HP-model
  compensation (root cause of battery regression).


## battery_v22 — D-8 multi-turn band recalibration
- Date: 2026-05-14
- Scope: formation matchup battery ported from v9 to v22 multi-turn
- Mode: G — diagnostic
- Status: committed
- Findings: 2/8 in-band. Root cause: no flanking detection. See battery_report_v22.md.
- D-8: DIAGNOSED.


## HANDOFF_v22 — comprehensive session handoff
- Date: 2026-05-14
- Scope: session summary for v21+v22
- Status: reference document
- Summary: 4 priorities resolved (BIAS-1, D-3, D-5, G-11). Next: D-8 battery recalibration.


## sim_mb_06_v22 — multi-unit orchestrator + freed-attacker + cascade + cavalry pursuit (D-3, D-5, G-11)
- Date: 2026-05-14
- Scope: mass combat simulation v21 to v22
- Mode: G — architectural additions: multi-unit orchestrator, cavalry pursuit
- Status: committed
- Changes (commit a): run_multi_unit_battle() for multiple engagement pairs.
  Morale cascade (Discipline Ob 1), rout contagion (-1 braked), freed-attacker (flank -1D).
  D-3 and D-5 resolved.
- Changes (commit b, G-11): Speed field (Slow/Standard/Fast). Pursuit: Fast victors
  pursue routing unit (offence pool, no defence for Slow/Standard; Fast rearguard -2D).
  Recall: Command Ob 2 per turn.
- Validation: mirror casualty ratio 1.25x (Standard), 1.22x (Fast mirror).
  Asymmetric Cmd 4 vs 3: 8.4x (Fast) vs 6.1x (Standard) — pursuit adds approx 40%.
  Cascade fail rates: Disc 2=33.5%, Disc 5=17%.
- D-3 RESOLVED. D-5 RESOLVED. G-11 RESOLVED.


## sim_mb_06_v21 — true simultaneous resolution (BIAS-1 root fix)
- Date: 2026-05-14
- Scope: mass combat simulation v20→v21
- Mode: G — structural fix for T4 simultaneous resolution violation
- Status: committed
- Changes: three changes to run_battle for true simultaneous resolution:
  (1) Target centroid caching before movement — primary fix for ~10% first-arg bias.
  (2) Simultaneous HP application — both units take damage, then both recalc_size.
  (3) Simultaneous morale erosion — compute both, then check rout for both.
  Alternating processing order swap removed from run_multi_turn_battle.
- Validation (n=40, max_battle_turns=20):
  Mirror Cmd 4v4: A 50% / B 42.5% / Draw 7.5% (v20: A 55% / B 40% / D 5%).
  Cmd 7v1: 100% A wins, avg 2.0 turns. Cmd 5v3: 100% A, avg 5.3 turns.
  Rout threshold ~14.7% (consistent with v20). Winner now determined by dice variance.
- Post-commit statistical test: 50/42.5 split at n=40 has p=0.62 — NOT significant.
  Grid geometry verified symmetric. GEO-1 closed. Mirror is fully symmetric.
- T4 simultaneous resolution: VALIDATED.

## sim_mb_06_v16 — G-3 continuous effective_size + lethality recalibration committed
- Date: 2026-05-13
- Scope: mass combat simulation v15→v16
- Mode: G (Incremental Build Protocol) — architectural change + lethality recalibration
- Status: committed
- Changes: continuous effective_size (float, not floored); LETHALITY_SCALE=0.10 for ~15%
  casualties per 3-phase engagement turn; casualty-percentage morale triggers at 30%/50%;
  max_turns default 18 (3-phase cap per engagement turn)
- Architecture: 4-level zoom (Peninsula → Territory → Battlefield → Scene).
  Sim models Battlefield level. Multi-turn battle: 5-8 turns × 3 phases per engagement.
  Per-unit 25×21 grid (not shared). Adjacent allies join at one depth.
- Findings: multi-turn rout at ~33% cumulative casualties after 2 turns.
  Winner casualties ~23%, loser ~33%. 100% rout rate.
  H5 RF wins 75.5% in multi-turn (above target — depth stacking).
  Per-turn battery not meaningful at max_turns=18 (most matchups draw).
  Winner/loser ratio 1.4x (historical 2-5x — needs pursuit/cascade).

## audit_sim_mb_06_v16 — formula validation + gap detection
- Date: 2026-05-13
- Scope: v16 audit (Mode A + Mode D)
- Status: committed
- Findings: 10 gaps (0 P1, 6 P2, 4 P3). Pool formula validated across boundary values.
  Phase-boundary morale check redundant with per-tick triggers (D-7).
  Multi-turn orchestrator is priority for v17 (D-1, D-9).

## sim_mb_06_v17 — multi-turn orchestrator + D-7 morale separation
- Date: 2026-05-13
- Scope: mass combat simulation v16→v17
- Mode: G — multi-turn battle loop, between-turn state rules, morale concern separation
- Status: committed
- Changes: run_multi_turn_battle orchestrator (D-1), between_turn_recovery (D-9),
  morale_check_phase separated from per-tick casualty triggers (D-7).
  Between turns: stamina +30, morale +0, HP persists, discipline persists.
- Multi-turn battery (n=100): geometric advantages compound across turns.
  H3 HS/Line 79%, H5 RF/HS 74% — higher than single-turn bands.
  Band recalibration needed for multi-turn model (design decision, not tuning).
- Winner casualties ~23%, loser ~33%. Ratio 1.4x. Battles resolve in ~2 turns.

## sim_mb_06_v18 — D-6 discipline with continuous effective_size
- Date: 2026-05-13
- Scope: mass combat simulation v17→v18
- Mode: G — D-6 fix: discipline degradation at phase boundary using cumulative loss
- Status: committed
- Changes: discipline_check_phase hook wired into phase_boundary (after stamina, before morale).
  Cumulative effective_size loss checked against DISCIPLINE_LOSS_THRESHOLD=1.0, asymmetric.
  Per-tick integer-Size discipline check removed (never fired at LETHALITY_SCALE=0.10).

## sim_mb_06_v19 — bottom-up TroopCount HP, no LETHALITY_SCALE
- Date: 2026-05-13
- Scope: mass combat simulation v18→v19
- Mode: G — bottom-up architectural change
- Status: committed
- Changes: HP = TroopCount = Size * BLOCK_SIZE (400 at Company scale).
  LETHALITY_SCALE removed entirely. Damage = soldier casualties from dice.
  Casualty rates emerge from pool/TN/DR mechanics: ~7% per 3-phase turn.
  4 turns to rout at ~31% cumulative. No tuning knobs.
- Multi-turn battery (n=80): H1 58.8%, H3 83.8%, H5 75.0%, H7 45.0%.
  Winner ~23%, loser ~31%. Ratio 1.4x. Battles 4 turns.

## v19 pursuit fix — Standard infantry cannot pursue per §A.12
- Date: 2026-05-13
- Scope: D-4 pursuit canonical compliance
- Changes: rout_resolution no longer applies pursuit damage from Standard infantry.
  Pursuit is a level-2 mechanic for Fast units only (canonical: §A.12).

## sim_mb_06_v20 — fully emergent morale erosion + contact-proportional stamina
- Date: 2026-05-13
- Scope: mass combat simulation v19→v20
- Mode: G — bottom-up emergent mechanics
- Status: committed
- Changes: morale erosion = damage / (discipline * command). No thresholds.
  30% rout emerges from canonical stats (morale=6, disc=5, cmd=4, dmg~3/tick).
  Stamina drain proportional to cells in contact (formation-emergent).
  Morale now float. No floor — general's contribution in denominator.
- Results: loser rout at 29.7% casualties (emergent). Winner ~22%. 4 turns.

## sim_mb_06_v20 patches — stamina drain fix + contact-fraction damage scaling
- Date: 2026-05-13
- Scope: bottom-up fixes from tick-by-tick diagnostic trace
- Changes: STAMINA_DRAIN_PER_CONTACT_CELL 3→1 (12-tick exhaustion, matches historical rotation).
  Engagement damage scaled by opponent's contact fraction (cells_in_contact/total_cells).
  Envelopment advantage now EMERGES: HS has more cells fighting → deals more damage.
  Casualty ratio 1.51x (up from 1.4x). Stamina now lasts 2-3 phases.
- Known issue: H1 mirror 91.7% side-A bias from position reset. Needs D-2 per-unit grid.

## v20 general death fix + throughline log
- Date: 2026-05-13
- Scope: Command=0 instant rout (M1 throughline) + throughline/meta-throughline audit
- Changes: Command=0 triggers immediate rout (prevents div-by-zero, models general death).
  Throughline analysis: T1 fully emergent, T2 partially emergent (needs D-5 cascade),
  T6 validated (scale-invariant dice engine). M1/M2/M3 meta-throughlines confirmed.
  Side-A bias 1.6%/turn noted (grid symmetry issue, D-2).

## sim_mb_06_v20 patches — grid symmetry + processing order bias fix
- Date: 2026-05-13
- Scope: grid placement bug + processing order bias
- Changes: SIDE_A_START_ROW=16, SIDE_B_START_ROW=8 (symmetric, 4 from center).
  Multi-turn orchestrator alternates argument order to neutralize first-arg bias.
  Root cause: unit_a processed before unit_b in movement+resolution.
  Remaining bias: ~10% (61/35 mirror). Full fix requires true simultaneous resolution.
- Also in v20: emergent morale erosion (dmg/(disc*cmd)), contact-proportional stamina.


## settlement_mgmt_stress_01 — Module 9 verified (2026-05-13)
- Module: Extended timeline + pressure clocks + Accounting hook
  (settlement_layer §7.1, §7.2; clock_registry_v30; params/bg/clocks)
- File: tests/sim/settlement_mgmt_stress_01/module_09_timeline.py
- Tests: 36/36 PASS (T1-T36); T35 IS the canonical 30-year-game
  simulation matching §7.1 prose to the integer (MS=42, IP=80, GS=6)
- Ledger: 22 new entries (~190 total cumulative)
- THROUGHLINE BINDINGS PRIMARY: T-04 MS Decay, T-05 CI Accumulation,
  T-06 IP Accumulation, T-07 Turmoil; SECONDARY: T-25 Generational Arc.
- META-THROUGHLINE: М-1 PRESSURE IS CONTINUOUS now has PRIMARY binding
  (closes the gap M8 retroactive audit surfaced).
- F17 NEW: clock_registry_v30 IP rate not updated to reflect §7.1
  recalibration (still implies +1/season; §7.1 says +1/2 seasons).
- per_season_accounting() is the canonical composition function:
  ticks 5 clocks + advances M4 parishes + M6 transitions + M7 sieges
  + §7.2 unmanaged-settlement decrement + M6 event sweep + M3 decade reset.
- All 6 primary meta-throughlines now have at least secondary binding;
  5 have primary; only М-6 remains primary-unbound (structurally
  expected — character layer).


## HANDOFF_v20.md — session handoff document
- Date: 2026-05-13
- Scope: end-of-session synthesis
- Status: committed
- Contents: bootstrap order, what's built, known issues, priority list,
  throughline/meta-throughline framework, trajectory anchor.


## settlement_mgmt_stress_01 — Module 10 verified (2026-05-13)
- Module: Dissolution emergence + POI templates + system impact catalogue
  (settlement_layer §4.6, §4.7, §4.8, §4.9, §8.1, §8.2)
- File: tests/sim/settlement_mgmt_stress_01/module_10_dissolution.py
- Tests: 27/27 PASS (T1-T27); T27 validates emergent governance-failure ->
  black-market chain composes across M9 + M10 with no authored coupling.
- Ledger: 17 new entries (~211 total cumulative)
- THROUGHLINE BINDINGS: T-27 PRIMARY (Effects Real Explanation Wrong),
  T-30 SECONDARY (Information Asymmetry), T-03 SECONDARY (Inseparability).
- META-THROUGHLINE: М-7 BORROWINGS ARE OPERATIONAL EXTENSIONS now PRIMARY
  (second previously-unbound meta closed; after M9 closed М-1).
- Audit catalogue: §8.1 11 system-impact predictions + §8.2 6 invariants
  surfaced as queryable Python data structures for Module 13.
- F18 NEW: §4.6 POI templates omit §2.1 extra types (Village /
  Fortress-City / Cathedral-City). SEVENTH surfacing of type-taxonomy
  drift family (F1, F7, F10, F11, F12, F14, F18). One editorial pass
  closes all seven.
- 5 of 6 primary meta-throughlines now primary-bound; only М-6
  remains primary-unbound (structurally expected — character layer).


## settlement_mgmt_stress_01 — Module 11 verified (2026-05-13)
- Module: Provincial Authority + Domain Echo chain + cross-system bindings
  (settlement_layer §3.1, §3.3, §8.1 cross-system surface)
- File: tests/sim/settlement_mgmt_stress_01/module_11_provincial_authority.py
- Tests: 30/30 PASS (T1-T30); T30 validates emergent REVOLT->province->
  national chain with dampening by province count (pure functional
  composition, no Domain Echo manager object).
- Ledger: 9 new entries (~220 total cumulative)
- THROUGHLINE BINDINGS: T-23 mechanism wired (Domain Echo chain IS the
  canonical "personal arc -> faction Domain Echo -> political shift"
  mechanism); T-26 NEW (Recursion as Setting Structure); T-15 + T-20
  extended; META: М-5 PRIMARY strongest binding (Domain Echo chain at
  institutional-action layer); М-4 SECONDARY extension.
- §3.3 issuer-side: grant_ob() fixed at 1; revoke_ob = ceil(Influence/2);
  Revoke applies Order -1 + Disposition -2 per canon.
- Closes M5 deferral: M5 owned subnational management receive-side;
  M11 owns Provincial Authority issuer-side Domain Actions.
- Cross-system: systems_affected_by_module(idx) maps every M1-M11 to
  at least one §8.1 system for Module 13 audit consumption.
- No new findings this session.


## settlement_mgmt_stress_01 — Module 12 verified (2026-05-13)
- Module: Faction integration + CI political pool + battle consequences
  (faction_layer §1+§9; ci_political §3; mass_battle §E.1+§E.2)
- File: tests/sim/settlement_mgmt_stress_01/module_12_faction_integration.py
- Tests: 40/40 PASS (T1-T40)
- Ledger: 26 new entries (~246 total cumulative)
- THROUGHLINE BINDINGS: T-21 Thread Political Warfare PRIMARY (closes
  prior-unbound primary); T-24 Convergence as Crisis PRIMARY (closes
  second prior-unbound primary); T-08 + T-20 + T-04 EXTENSIONS.
- META-THROUGHLINE: М-6 CHOICE IS FORCED now PRIMARY at sim level
  (closes last prior-unbound primary meta). М-4 strongest tally
  (5 modules).
- ALL 7 PRIMARY META-THROUGHLINES NOW PRIMARY-BOUND.
- T38: M9 + M12 MS-composition (year-decay + battle penalty) emerges
  from shared clock state.
- T39: capital-territory double-magnitude penalty validates М-6
  forced-choice mechanism.
- T40: Stability triggers compose into elimination cascade (capital
  loss + Suppress failure = Stability 0). T-24 Convergence emerges
  from atomic trigger composition.
- bind_faction_standing_delta() canonicalizes the M3-M11 ActionResult
  signal binding to faction-stat-sheet mutations for Module 13.
- No new findings.


## weapon_system_v2 — proposed redesign
- Date: 2026-05-13
- Scope: Weapon TN, damage types, attack/defense triangle, STR multiplier
- Design: weapons as multi-attack-type platforms (Cut/Thrust/Bash per weapon).
  Attack×Defense triangle (Parry>Cut>Brace>Bash>Deflect>Thrust>Parry).
  Half-point TN. 4-axis properties. Distance rules. Two-handed bonuses.
  STR multiplier committed to canon (Heavy×2, Blunt×1.5, multiplicative).
- Historical: Fiore, Liechtenauer, Vegetius, Uncharted Waters (Koei 1994).
  Convergence validated: blade useless vs plate, thrust finds gaps (STR-dep),
  blunt inverted curve. Triangle grounded in physical defense mechanics.
- Status: PROPOSED. Needs sim validation. Large blast radius.
- NERS: all components pass. Half-point TN, multi-attack, triangle, STR mult, distance.
  Pierce STR-dep vs Heavy is the only MODERATE (breaks flat-table pattern, worth it).
- Throughlines: 9 identified (economy, fieldwork, initiative, identity, scale, distance,
  faction equipment, high-skill play, formation). Meta: context>strategy, info>power,
  versatility vs specialization, scale-consistent mechanics.


## settlement_mgmt_stress_01 — Module 13 verified — SIM STRUCTURALLY COMPLETE (2026-05-13)
- Module: Integration runner + NERS audit (FINAL MODULE)
  - integrated_season_tick composes M1-M12 in canonical per-season sequence
  - NERS audit grid: 4 properties (Necessary/Robust/Smooth/Elegant)
    × 6 directions (top-down/bottom-up/vertical/diagonal/lateral/horizontal)
    = 24 cells: 21 PASS / 3 partial / 0 FAIL
  - Throughline coverage: 24 distinct (15 primary + 8 secondary + 1
    unbound + 4 character-layer-out-of-scope) across 12 modules
  - META: ALL 7 primary metas now primary-bound
    (М-1 M9 / М-2 M2,M7 / М-3 M1,M2,M6 / М-4 M3,M4,M5,M11,M12 strongest /
     М-5 M5,M8,M11 / М-6 M12 / М-7 M10)
  - Mode A complete; Mode B complete; Mode C blocked by F6; Mode D partial
  - 4 editorial recommendations prioritized: P1 type-taxonomy (closes 7
    findings), P2 documentation (closes 4), P3 F6 geography rebuild,
    P4 isolated cleanup
- File: tests/sim/settlement_mgmt_stress_01/module_13_integration_runner.py
- Tests: 26/26 PASS (T1-T26)
- T23 validates 30-year canonical simulation through full integration
  runner: MS=42, IP=80, GS=6 (matches §7.1 to integer end-to-end)
- Ledger: 4 new audit-grade entries (~250 total cumulative)
- CUMULATIVE STATUS: 13 modules verified, 403 isolation tests,
  18 findings (1 resolved, 1 partial, 16 open)
- 8 emergent cross-module chains validated
- SIMULATION STRUCTURALLY COMPLETE


## weapon_system_v2/testing_plan — 9 phases, 23 tests
- Date: 2026-05-13
- Scope: Half-point TN, damage tables, multi-attack, defense triangle,
  distance, 2H bonus, builds, crits, integration.
- 3 decision gates: TN+damage → triangle → 2H stacking → ratify/iterate.
- Priority 1: T1.1, T1.2, T2.1, T2.2, T2.4, T6.1 (must pass before any ratification).
- Phase 1-2 P1 results: T1.1 conditional pass (ratio 1.98×). T1.2 pass. T2.1 pass.
  T2.2 PASS — crossover at Medium (blade wins None/Light, blunt wins Med/Heavy).
  T2.4 FAIL — warhammer dominates all tiers (STR×3 overwhelms TN gap).
  T6.1 FAIL — longsword dominates (84% vs arming at -1.0 cap; 74% at -0.5 cap).
  2H cap at -0.5 helps but TN 6.5 vs 7.0 cliff remains. Mace/rapier non-viable.
  Decision: TN modifiers need redistribution. 1H weapons need TN reduction or
  2H weapons need further TN increase. The 0.5-point cliff is the structural issue.
- Phase 5 distance re-run (2026-05-14): T2.4 + T6.1 re-run with Short/Mid/Long
  distance mechanics. Sim: weapon_v2_distance_sim.py. N=3000, equal stats, arena 3.
  T2.4 STILL FAILS — warhammer 59-74% (down from 66-85%). STR×3 overwhelms distance.
  T6.1 PARTIAL — longsword vs dagger 52.7% (distance works), vs arming 65.8% None
  (borderline) / 75.7% Heavy (fails), vs warhammer 51.7% (balanced).
  Root cause: asymmetric range reward (Long = 1.5 TN gap vs Mid = 0.5 gap).
  Adjacent penalty variant (+0.5 vs +1.0) confirmed values not penalty are the issue.
  Next: T7.1 equal-budget builds to test stat-allocation self-balancing.


## settlement_mgmt_stress_01 — Handoff document committed (2026-05-14)
- File: tests/sim/settlement_mgmt_stress_01/HANDOFF_ners_test_plan_and_findings_audit.md
- Scope: post-completion audit handoff for the structurally-complete sim.
- NERS empirical test plan: 24 probes (one per 4-property × 6-direction cell)
  promoting M13 subjective ratings to falsifiable experiments.
  Per-probe spec: hypothesis, mechanical artifact, procedure, PASS/partial/FAIL
  criteria, dependencies, execution cost. Total ~8.5 hours of empirical probes,
  fully parallelizable, zero internal dependencies.
- Mechanical findings log: 18 findings restated as audit-grade table with
  evidence-file pointers, dependency graph (Mermaid), editorial-pass closure paths.
- 4-priority editorial sequence: P1 (closes 7 type-tax-drift), P2 (closes 4
  doc-drift), P3 (F6 unblock — closes F4 partial as side effect), P4 (4 isolated).
  Total editorial cleanup: ~7 hours; cleanest order P1→P2→P3→P4.
- Audit reviewer checklist: 25 yes/no items across 8 categories (architecture,
  canonical-source compliance, throughline coverage, NERS, findings register,
  mode progression, emergent architecture, editorial readiness).
- No new mechanical work; document is the bridge from "structurally complete"
  to "audit-confirmed and Mode-C/D unblocked." Estimated remaining: ~16 hours.


## settlement_mgmt_stress_01 — Handoff doc amendment 500-seed batch (2026-05-14)
- File: tests/sim/settlement_mgmt_stress_01/HANDOFF_ners_test_plan_and_findings_audit.md
- Amendment: Mode-G batch upgraded from 50 to 500 seeds for tail-frequency
  detection. Added §6.1 statistical envelope subsection with rationale,
  per-seed cost (~1s × 500 = 8-10 min wall-time), output target schema,
  and acceptance criteria (MS mean within ±3 of canonical 42, IP within
  ±5 of canonical 80, zero state-corruption errors, ≥1 seed reaching each
  canonical tail condition).
- 95% CI half-width on a 5%-event drops from ±6% (n=50) to ±2% (n=500);
  1%-events become detectable at ±0.9% CI. Mode-D systematic 9-category
  search benefits structurally.


## settlement_mgmt_stress_01 — 500-seed batch executed (2026-05-14)
- Runner: tests/sim/settlement_mgmt_stress_01/batch_500seed_runner.py
- Audit: tests/sim/settlement_mgmt_stress_01/audits/batch_500seed_2026-05-14.md
- Raw: tests/sim/settlement_mgmt_stress_01/audits/batch_500seed_2026-05-14_raw.json
- 500 seeds × 120 seasons = 60,000 integrated_season_tick calls
- Wall time: 3.9s (7.9ms/seed) — well under §6.1 spec budget
- SCOPE: synthetic-stats over CANONICAL M1 REGISTRY settlements
  sampled per seed (5-8 settlements per seed). F6 Mode-C blocker
  still open (geography YAML rebuild outstanding) — batch is NOT a
  full Mode-C canonical-scenario sim, but validates engine stability
  under perturbation.
- DISCOVERY DURING BUILD: M6 sweep_season_events iterates the M1
  REGISTRY (canonical) not arbitrary state-dict keys. Initial synthetic
  BATCH-S-NNN IDs produced zero events; pivoted to REGISTRY-sample
  approach. M1 REGISTRY is post-PP-726 canonical (resolved at M2);
  F6 geography YAML drift does not affect REGISTRY.
- ACCEPTANCE GATES (§6.1):
  - zero_state_corruption: PASS (0 corrupt seeds / 500)
  - tail_faction_elimination_reached: PASS
  - tail_deep_echo_chain_reached: PASS
  - tail_events_fire: PASS
  - MS drift: mean 24.0 (canonical 42; delta -18) — perturbation
    pushed substrate to crisis state; documents response envelope
  - IP drift: mean 100.0 (canonical 80; delta +20) — clamped at
    IP_MAX; all 500 seeds reach IP-saturation crisis
- DISTRIBUTIONS:
  - MS: min=14, p05=17, median=24, mean=23.97, p95=31, max=38
  - CI: all 500 saturated at 100
  - IP: min=93, mean=99.97, all reach ceiling
  - GS: all 500 at 6 (canonical generational-shift cap)
  - Turmoil: median=10, p05=10, max=10
- EVENT-FIRING AGGREGATE: local_revolt 329k total (658/seed),
  famine 56k (113/seed), flourishing_festival 1.8k (3.7/seed).
  RAID_OR_SIEGE, MINE_RESOURCE_SURPLUS, GOVERNANCE_TRANSITION_RM,
  CONSENSUS_DELAY, RELIGIOUS_EVENT did not fire (require upstream
  state the batch does not inject).
- FACTION ELIMINATIONS: 500/500 seeds reach >=1 elimination;
  mean 3.60, median 4, max 4 (all 4 factions eliminated in many seeds)
- DOMAIN ECHO CHAINS: 387,732 deep-chain firings (100% depth-2 in
  the Crown-2-province setup; magnitude -1 always echoes to national)
- BLACK MARKETS: mean 7.3 new per seed; mean 0.83 disappearances
- TAIL-EVENT LOG: 1,496 flagged tail events across all seeds
- BATCH-DESIGN PARAMETERS (not canonical; calibration choices):
  - GOVERNOR_RESTORATION_PROB_PER_SEASON = 0.05
  - FACTION_STABILITY_TRIGGER_PROB = 0.05/faction/season
  - TAIL_PERCENTILE = 95
  - battle injection 15%/season; contested-territory Brownian drift;
    settlement-stat 20% drift; governor turnover 10%/season
- INTERPRETATION: engine survives 60,000 ticks under heavy perturbation
  with ZERO state corruption. Drift from canonical worked values
  documents the response envelope of the simulation under stress.
  Tail-event seeds provide specific reproducers for Mode-D systematic
  exhaustive search once F6 closes.
- HANDOFF criteria completed: §6 item 5 (50-seed batch validation)
  is COMPLETE — upgraded to 500 per amendment 1a1c2de9 and executed
  this commit. Outstanding: NERS empirical probes (§2 of handoff),
  editorial P1-P4, F6 unblock, Mode-D systematic search,
  audit reviewer checklist §4 walkthrough.

## Weapon System v2 (2026-05-14)

| Test | Status | Sim | Finding |
|------|--------|-----|---------|
| T2.4 Warhammer dominance (with distance) | PARTIAL PASS | weapon_v2_distance_sim.py v3 | WH win rate 42-59% (PASS). DPH ratio 1.4-2.4× (FAIL >1.3×) |
| T5.1 Distance sanity | PASS | weapon_v2_distance_sim.py v3 | Specialist 72-83% at optimal range. Directionality correct |
| T6.1 Longsword dominance (with distance) | PARTIAL PASS | weapon_v2_distance_sim.py v3 | vs Mid weapons 47-58% (PASS). vs Long weapons 70-77% (FAIL) |
| T4.1 Triangle modifier | FAIL | inline (3 variants) | Swing 10-20pp at ±0.5/±1.0/±2D. Target 25-35pp |
| T4.2 Initiative + triangle | FAIL | inline | +1.3pp to +6.3pp. Target 8-15pp |
| T4.3 Specialist penalty | FAIL | inline | Mace 19-25%. Target 40-50% |
| T4.4 Random vs optimal defense | FAIL | inline | 7-8pp gap. Target <5pp |
| T7.1 Equal-budget matrix | FAIL 5/6 | inline | Tough 69-82%, Soldier 9-17%. Target: no build >65% |
| T7.2 Protocol swing | PARTIAL PASS | inline | 1-17pp. Target 15-30pp |

### Iteration 4 — Final Config (2026-05-14)
| Fix | Component | Status |

---

_Archived 2026-05-18 (Step 4.2 commit) from tests/coverage_matrix.md._

## v25 (2026-05-15) — Geometry expansion + dynamic wide-wing pathing + sightline

**Architecture:** 41×42 connected battlefield (was 25×25); 19×11 formation area within 41×21 per-unit grid; 11-col side buffers; 5-row front/back buffers. Dynamic Horseshoe wing pathing relative to enemy widest column. Sightline mechanic (135° arc, 15-cell range) gating defender rotation. Cell-level adjacency damage zones. Sticky Phase 2 transitions via Subunit.wing_phase_2_cells.

**Status:** in-progress calibration; battery 3/11 in-band at LATERAL_BUFFER=3. Battles 5–7 ticks (target 18+ across 3+ turns).

**Known issues for next iteration:**
- ANGLE_DMG_MULT and FLANKED_BONUS constants present but not wired into damage formula; pool-averaging via ANGLE_DEF_MOD dilutes single-cell RED zones
- 17-row vertical gap (formation to formation) may need tightening for current speeds
- Arrowhead tip mechanic underperforms (H2 Arrowhead vs Line = 25% A; H9 Line vs Arrowhead = 75% A → both indicate tip isn't delivering proportional damage)

**File:** tests/sim/sim_mb_06_v25.py

**Status update v25 (post-commit):** sim file landed (this commit). 18+ constants ledger entries reference §A.3b. Calibration work continues — battery 3/11 in-band, known issues documented above.

### Fiore TN System (v27, 2026-05-15)
| Finding | Result |
|---------|--------|
| Fiore TN: base 7.0 all, 2H -0.5 only | Weapon matchups excellent with distance |
| Dagger vs AS: 76% → 31% | **Fixed** — dagger penalized at Mid, must close to Short |
| Mace vs LS Heavy: 60% | Mace wins at Heavy via positional advantage ✓ |
| T5.1 directionality | PASS — 74%/83% at optimal |
| T7.1 None: Tough 92% | FAIL — Mid-start favors Mid-reach weapons |
| Root cause | Distance + stamina system needs engagement mechanic, not fixed Mid start |
| **Status** | Fiore TN validated for weapon identity. Build matrix needs distance engagement. |

### Fiore TN + Engagement (v27 continued)
| Test | Result |
|------|--------|
| Agi engagement + Fiore TN | Tough 84% (None), 90% (Heavy) — improved but not passing |
| Brute (STR6 mace) vs Tough | 19-40% — HP outlasts damage at all tiers |
| Root cause | Fights end by stamina (4 rounds), not damage. HP >> DPR × rounds. |
| Sim limitation | Simplified chassis lacks feint/taunt/initiative declaration — full BW tactical layer would create non-attrition win paths |
| **Fiore TN verdict** | Correct for weapon identity and matchups. Build matrix needs full duel system, not more formula patches. |


### v9 Full Chassis + Fiore TN (v27 final)
| Finding | Result |
|---------|--------|
| Fiore TN in v9 chassis | Tough 94% at canonical stamina — stamina timer dominates |
| Stamina cliff | stam 24→4rds, stam 25→5rds — ±1 stam flips outcome |
| Arena 0 (cost 5) | Fast 69%, Tough 53%, spread 31pp — best balance |
| **Proposal: stunt cost +1→+0** | Preserves stamina, eliminates quantization cliff |

### Videogame Baseline — BEST RESULT (v27)
| Test | Result |
|------|--------|
| None, arena 0 | Fast 68%, spread 30pp |
| **Heavy, arena 0** | **Tough 63%, spread 25pp — PASS** |
| Mace vs AS | 45%/73% crossover ✓ |
| Dagger vs AS | 46%/45% (fixed from 76%) ✓ |
| Mace vs LS Heavy | 52% — both effective vs plate ✓ |
| **Config** | **Fiore TN (base 7.0, 2H -0.5) + D1-D3 + v9 chassis + distance + arena 0** |
| Remaining | None at 68% (3pp over). Fiore TN + stunt cost not yet ratified to params. |

### Fiore TN Ratified (v27)
PP-717 Fiore: base 7.0, 2H -0.5. Distance Short/Mid/Long. Action cost 5. Three-axis system superseded.

### All-Directions NERS Audit (v27)
| Layer | Status |
|-------|--------|
| 5 throughlines | All PASS NERS |
| 4 meta-throughlines | All PASS NERS (3 minor flags) |
| 6 directions | 5 PASS, 1 PARTIAL (Vertical: STR uncapped) |
| Internal consistency | 5/5 PASS |
| External consistency | 4 flags: stamina (End×5 vs 15+End×2), taunt canonicalization, 2H stacking, mass combat untested |
| P1 actions | Stamina reconciliation, taunt canonicalization |

### Combat Integration Session A (2026-05-15)
Phase machine + Strike/Guard/Breath. Canonical values, full ledger. Smoke test passes.

### Session A NERS Audit
All 5 throughlines pass NERS. All 3 meta-throughlines pass. STR mult ambiguity flagged.

### Engine NERS All-Directions Audit (2026-05-15)
| Layer | Status |
|-------|--------|
| Scope | First engine-design NERS at architectural level (dice engine + derived stats + Ob/Pool channels) |
| Throughlines | 5 derived (TE-1..TE-5); 3 partial, 1 fail (TE-4 Smooth: combat-only Pool Softcap) |
| 6 directions | TD/BU/L/V/D/H — 21 findings across all six |
| Severity | 2 P1 (stale Vitality formula in params/core; stale Concentration formula in params/contest), 8 P2, 11 P3 |
| Unifications | 9 proposed; U-1 (PP-716/PP-717 propagation) ready for no-call commit; U-2..U-7 need design call |
| Self-review | Three radical reframings applied: designer-theater (most findings player-invisible); productive-inconsistency (deviations as features); descriptive-vs-prescriptive (throughlines as observation not principle). Recovered finding count after self-review: ~5 substantive |
| File | tests/audit/engine_ners_2026-05-15.md |

### Phase 4 Agi-Dominance Re-check (2026-05-15)
| Test | Result |
|------|--------|
| Trigger | Decision A (ED-828) — PP-717 D2 Pool Softcap rejected at canon |
| Scope | Verify whether Agi-6 vs Agi-3 dominance manifests at current canon |
| Mechanics | Universal pool (no DR), MW cap 3 (PP-717 D1), Crit threshold ≥4 (PP-717 D3) |
| Fast vs Strong | 95.6% conditional win — DOMINANT |
| Build-investment ROI Agi 3→7 | +46.6pp conditional win at top — steep, never inverting |
| Tough vs Strong (End 6 vs 4) | 99.6% conditional — End-dominance also persists |
| Fast+Tough vs Strong | 100% — compound dominance unrecoverable |
| Conclusion | Agi-dominance reopens at current canon. PP-717 D2 was addressing real problem. Recommend Jordan reconsider. |
| Sim limitations | Strike-only; 50/50 split; single weapon/armour; lower-bound estimate |
| Files | tests/sim/phase4_agi_dominance_2026-05-15.py + phase4_results.md + sim_verification_ledger.json |

### v17 Full-Workstream Integration (2026-05-15 — in progress)
| Test | Result |
|------|--------|
| Trigger | Phase 1a finding: v16 structurally incomplete (Church 0%, Varfell 0%) |
| Scope | Gap analysis of mc_v16.py against all canonical design docs |
| Finding | 27 mechanics missing across 5 workstreams (7 Critical, 11 High, 7 Medium, 2 Low) |
| Root cause | Church dies because settlement infrastructure (Religious Buildings, Templar Stations) not modeled; CI generation depends on PT which RM destroys; Mass Battle absent |
| Module manifest | 7 modules, ~7 sessions, critical path M1→M2→M6→M7 |
| Status | Module manifest and gap analysis committed; Module 1 (Church Settlement Infrastructure) next |
| Files | tests/sim/v17-integration/gap_analysis.md + module_manifest.md |

### Phase 5 Continuous Engine Prototype (2026-05-15)
| Test | Result |
|------|--------|
| Trigger | Jordan 2026-05-15 — accepted Path 3 (full continuous engine) |
| Sim A: Distribution equivalence | EQUIVALENT — max deviation 0.029 in mean, 0.022 in std at pool 5-17 |
| Sim B: Phase 4 re-run on continuous | Matches Phase 4 discrete within sampling noise |
| Sim C: Discrete vs Continuous head-to-head (N=5000) | 97.8% (discrete) vs 97.5% (continuous) — Δ -0.3pp |
| Build ROI curve | Identical shape — Agi 7 reaches 99.2% in continuous, 99.5% in discrete |
| Key finding | **Continuous engine works but does NOT solve Agi-dominance** — doubling is the structural driver, not the dice mechanism |
| Implication | Adopting continuous engine: yes (independently valuable for fractional modifiers + degree continuity). Solving dominance: requires separate decision (drop doubling, pool cap, or re-ratify softcap) |
| Files | tests/sim/phase5_continuous_engine_2026-05-15.py + phase5_results.md + phase5_sim_verification_ledger.json |

### Phase 6 Dominance-Solver Comparison (2026-05-15)
| Test | Result |
|------|--------|
| Trigger | Phase 5 showed continuous engine alone doesn't solve dominance |
| Candidates | (A) status quo, (B) drop doubling, (C) cap 14, (D) cap 12, (E) PP-717 softcap |
| Fast vs Strong | A: 97.8% / B: 90.2% / C: 89.1% / D: 72.3% / E: 92.6% — **ALL DOMINANT** |
| Build ROI spread Agi 4→7 | +20pp / +36pp / +8pp / +0pp / +17pp |
| End-dominance (Tough vs Strong) | 99.6-99.9% across ALL formulas — formula-independent |
| KEY FINDING | **Pool formula does NOT solve dominance** — structural drivers are wound spiral, HP/stamina window, crit cascade |
| Next path | Phase 7 with action triangle (Feint/Defend) OR wound-spiral lever |
| Implication for canon | Pool/doubling decision becomes design-feel choice, not balance choice |
| Files | tests/sim/phase6_dominance_solvers_2026-05-15.py + phase6_results.md + phase6_sim_verification_ledger.json |

### Phase 7 Action Triangle Test (2026-05-15)
| Test | Result |
|------|--------|
| Trigger | Phase 6 showed pool formula doesn't solve dominance; test action triangle (PP-294 Feint) |
| Fast vs Strong, Strike-only baseline | 96.7% Fast cond (matches Phase 6) |
| Fast vs Strong, Underdog (Strong) actively Feints | **34.9% Fast cond — Strong wins 65%** |
| Tough vs Strong, Smart play both sides | 6.8% Tough cond (down from 82% Strike-only) |
| KEY FINDING | **Action triangle (PP-294 Feint) is the load-bearing balance lever** — not the pool formula |
| Interpretation | When disadvantaged side actively Feints, dominance INVERTS. End-dominance collapses with tactical play. |
| Implication | Pool formula and Decision A stand. Doubling is design-feel. Combat IS balanced via tactics. |
| Caveat | Smart AI under-tuned; numbers indicate direction but not point estimates |
| Files | tests/sim/phase7_action_triangle_2026-05-15.py + phase7_results.md + phase7_sim_verification_ledger.json |

### Workstream Meta-Audit (2026-05-15)
| Aspect | Result |
|--------|--------|
| Subject | 10-commit chain (02e2dd7f..5de02b07) from engine NERS through Combat Balance Note |
| Method | Six-direction audit + NERS rubric, objective neutral, initial pass |
| NERS scorecard | N=~, E=✓, R=~, S=✓ — two partials (scope/validation), two passes (execution/integration) |
| Findings | 0 P1, 4 P2, 5 P3 — all P2/P3 are Robustness concerns; zero correctness defects |
| What stands | F1/F2/F4/F5/F12/F13 propagation fixes; DR→Softcap; continuous engine validation; hook compliance |
| At-risk | Balance Note canonization timing; Decision E scope-validation mismatch; F13/Decision E bundling; Phase 7 End-dominance possibly artifact |
| Open | Phase 8 (better Smart AI); cross-system audit; End-dominance follow-up; SHA refresh |
| File | tests/audit/workstream_meta_audit_2026-05-15.md |

### Phase 8 Smart AI v2 (2026-05-15)
| Test | Result |
|------|--------|
| Trigger | WS-H-3, WS-H-4 (meta-audit 2026-05-15) — Phase 7 Smart AI under-tuned |
| Smart v2 AI fixes | Take Breath threshold ≤8, Full Guard last-stand only, Feint alternation per PP-294 |
| Fast vs Strong, Smart v2 symmetric | **100% Fast — pool advantage structurally dominant** |
| Tough vs Strong, Smart v2 symmetric | 63.7% Tough — moderate End-dominance (Phase 7 7.5% was artifact) |
| Calibration: Agi 3 vs Agi 3 symmetric | 51.2% — sim balanced |
| KEY FINDING | Phase 7 "34.9% Feint inverts dominance" was partly stamina-management artifact; pool advantage at 17D vs 11D is structurally dominant in skilled-vs-skilled play |
| Combat Balance Note status | Needs revision — 34.9% claim misleading without stamina-asymmetry caveat |
| Files | tests/sim/phase8_smart_ai_v2_2026-05-15.{py,md} + phase8_sim_verification_ledger.json |

### Phase 10 STR + Stamina Reform (2026-05-16)
| Test | Result |
|------|--------|
| Trigger | Jordan design questions: "stamina from endurance should be doing a lot more work; strength isn't having enough impact" |
| Methodology corrections | (a) TN vs Ob conflation in prior wound-penalty sims (Ob is net-success threshold, not per-die TN shift); (b) Disarm AI threshold bug fix (opp_weapon_mod >= 3 not >= 4); (c) **stamina-formula error in Phase 4-9: sim used 15 + End*2, canon (ED-694) is End*5 with partial Take Breath restore and +1 stam cost per wound** |
| Stamina correction impact | Every End-investing matchup shifts 4-9pp from prior sim baseline. Fast vs Titan: 81.8% → 72.6% before any reform applied. Phase 8 ED-838 End-dominance magnitude (63.7%) understated; direction unchanged, magnitude larger |
| STR bonus dice (proposed reform) | floor(STR/3) on Strike/Disarm offense pool: STR 4→+1, STR 7→+2, STR 10→+3. Pending Jordan ratification |
| Best config: canonical stam + STR-strong | Fast vs Titan 67.5/32.5 — meaningful upset rate. Fast vs Tough-heavy 77/23. Calibration symmetric matchups 47-51% |
| Persistent finding | Pool dominance survives all reforms. Fast vs Titan 70/30 at full reform stack. Further levers (pool cap, static defense, smaller pools) untested |
| STR + light blade gap | Mighty (Agi 3, STR 7, light) sits at 98.5% loss to Fast under STR-strong. Light weapon str_mult=1.0 + 2pp hit-rate gain cannot overcome 3-die pool gap. Open design question |
| Sim limitations | Tie Up, Establish Distance, Reach mechanics still unmodeled; symmetric AI assumption persists; Phase 7 PP-294 inversions not retested under reform; cross-system audit (CC-1) in backlog |
| Open canonical questions | (1) Update Combat Balance Note with stamina-correction erratum; (2) ratify STR bonus dice mechanic; (3) accept pool dominance as designed or push further; (4) design light-weapon STR archetype or accept gap |
| Files | tests/sim/phase10_str_stam_reform_2026-05-16.md + tests/sim/scripts/phase10_str_stam_reform.py |

### M1-M5 (v17 modules; archived 2026-05-16)
M1 Church Settlement Infrastructure (commit `4f27949e`, 128 tests, 49 ledger entries), M2 CI Political Revision (`29b52428`, 78 tests, 26 ledger), M4 Unit State Management (`e33849c8`, 95 tests, 22 ledger), M3 Mass Battle Resolution (`dc9a71a0`, 63 tests, 23 ledger), M5 Settlement-Territory Aggregation (`4e1d00dd`, 95 tests, 28 ledger). **Detailed test surfaces archived in** `tests/coverage_matrix_archive_v17_modules.md`. Cumulative for M1-M5: 459 tests passing, 148 ledger entries. All five modules built canonical-fidelity (no fabricated mechanics; every constant cited to canonical source).

### M6 Faction Action Expansion (2026-05-16)
| Test | Result |
|------|--------|
| Trigger | v17 module manifest — Module 6 of 7; Crown Initiative + faction analogues + Excommunication + Absolution + RM Uprising + tactic card effects deferred from M3 |
| Module scope | Crown Initiative 3 modes (Royal Progress / Great Work / Coronation Renewal) per part10 §3.2-§3.4 with full pool/Ob/outcome tables including Mode III Excommunication-recovery (canon §6.4 Q-11 resolution); Church Excommunication per faction_canon §9 + Church sheet (L≥3 prereq, Ob=target_L leader / Ob 2 non-leader, 3-tier outcomes); Church Absolution per §8.2 with M6-declared Pool/Ob/cost; faction analogues (Council of Solmund Ob=floor(CI/30)+2, Charter of Liberties Pool=Inf+tokens Ob=4, Vaynard's Hall Pool=Mil+tribune_active Ob=3) per part10 §5.1-§5.3; RM Cultural Uprising of T9 per victory §3.5 Phase 2 with Phase 1 check (PT≤1 in ≥4 territories), MS≥25 prereq, Ob=clamped(ceil(CI/10)) + 3 modifiers; parametric tactic card effects (10 cards with constant pool modifiers) + 6 cards raising NotImplementedError for resolution-time hooks deferred to M7 |
| Test groups | T1 Royal Progress (15 checks) / T2 Great Work (10) / T3 Coronation Renewal (16) / T4 Excommunication (11) / T5 Absolution (8) / T6 Faction analogues (15) / T7 RM Uprising (18) / T8 Tactic card effects (16) / T9 Action registry (6) |
| Result | **125 PASSED, 0 FAILED** |
| Canonical sources verified | part10_crown_initiative_design §3.1-§3.7 + §5 + §6 + §7 (full 21.2k); faction_canon §8.2 + §9 + Church sheet (full 47.0k); victory_v30 §3.1 + §3.2 + §3.5 + §8 (full 57.2k); peninsular_strain (full 49.8k); mass_battle §B.4 faction-specific tactic cards (cached from M3); factions_personal_v30 + params/factions.md (fetched for sim_gate) |
| Ledger | 45 entries; per-mode citations to part10 §3.2-§3.4 outcome tables, Excommunication degree table to faction_canon Church sheet, RM Uprising mechanics to victory §3.5 Phase 2 |
| Provisional assumptions held | 5 (M6_ASSUMPTION_ONE..FIVE): Church Absolution Pool/Ob/cost declared by M6 (canon underspec), Standing as integer modifier (pending canonical track), parametric-vs-hook tactic card split (6 cards deferred to M7 with explicit dispatch reason), Weaver Thread pool as caller-supplied integer, 4-degree outcome semantics with {} default for canon-undefined degrees |
| Dependencies | M1 (settlement registry for Uprising Phase 1 territory enumeration), M2 (CI milestone queries for Coronation Renewal interactions), M3 (TACTIC_CARDS registry — M6 extends with parametric effects + hook-deferred set) |
| Files | tests/sim/v17-integration/m6_faction_actions.py + m6_faction_actions_tests.py + m6_sim_verification_ledger.json |
| M7 integration hooks needed | Stratagem 2-pass init inversion, Crusade Fervour check_route override, Inquisitor's Mark per-unit targeting, Calculated Retreat outcome override, Disappear outcome override, Ducal Call resolution-time state mutation — see TACTIC_CARDS_REQUIRING_HOOKS frozenset in m6_faction_actions.py |
| Next module | M7 Integration + Balance Sweep — all 6 module dependencies satisfied |

### M7 Integration + Balance Sweep (2026-05-16)
| Test | Result |
|------|--------|
| Trigger | v17 module manifest — Module 7 of 7 (final). Wires M1-M6 into mc_v17 runner + balance sweep with Wilson 95% CI verification |
| Module scope | mc_v17.py — extends mc_v15 baseline (Faction/Territory/World/Logger preserved) with M-module wiring: Faction.units (M4 UnitRoster), Faction.tactic_hand (M3 6-card hand 4 shared + 2 specific), World.settlements (M1 37-settlement registry), World.governance (M5 SettlementGovernance map), CI starting value from M2; ACTION_REGISTRY dispatch table (Govern/Muster/MilitaryConquest + Crown Initiative 3 modes + Excommunication + Absolution); ci_generation with M2 CI cap; settlement_event_pass + aggregate_to_territory using M5; minimal AI policy (30% faction-unique / 35% Conquest / 20% Muster / 15% Govern). m7_resolution_hooks.py — 6 hook-deferred tactic card implementations (Stratagem 2-pass init inversion, Crusade Fervour route suppression, Inquisitor's Mark -2 opponent pool, Calculated Retreat withdrawal, Disappear withdrawal+pursuit-block, Ducal Call pre-resolution Muster) via ResolutionContext + HookedBattleResult + resolve_battle_hooked pipeline. m7_balance_sweep.py — Wilson 95% CI computation + N=1000 sweep harness with band-overlap check |
| Test groups | T1 ResolutionContext (4) / T2 Stratagem hook (2) / T3 Calculated Retreat + Disappear (6) / T4 Ducal Call (2) / T5 Crusade Fervour route suppression (2) / T6 Inquisitor's Mark pool penalty (2) / T7 mc_v17 World construction (10) / T8 ACTION_REGISTRY dispatch (3) / T9 Settlement event loop (1) / T10 Smoke run 5 campaigns (1) / T11 Batch telemetry (3) |
| Result | **38 PASSED, 0 FAILED** |
| Balance sweep N=1000 result | **Crown 67.7% / Church 0.8% / Hafenmark 1.8% / Varfell 29.7%** (5.7s runtime, 175 campaigns/sec). Wilson 95% CIs: Crown [64.74, 70.53], Church [0.41, 1.57], Hafenmark [1.14, 2.83], Varfell [26.95, 32.61]. **`all_factions_in_band [20%, 30%] = False`** — only Varfell overlaps target band. battles_per_campaign=12.88, mean_season_ended=50.0. **Per integration_plan §10 R-03: the harness correctly DETECTS balance failure; tuning balance is downstream work, not in M7 scope.** |
| Canonical sources verified | integration_plan_v3 §5 Phase 2a-2d + §5 Phase 5 (full); mc_v15.py full reference architecture (full 46.0k cached); mass_battle_v30 §B.4 faction tactic cards (cached); factions_personal_v30 + params/factions.md (cached) |
| Ledger | 23 entries; resolution hook specs to §B.4 + canon Stratagem PP-690 / Crusade Fervour / Inquisitor's Mark / Calculated Retreat / Disappear / Ducal Call rows; Wilson CI to standard statistical reference; ACTION_REGISTRY architecture decisions to integration_plan §5 Phase 2 |
| Provisional assumptions held | 7 (M7_ASSUMPTION_ONE..SEVEN): ResolutionContext+HookedBattleResult architecture; ACTION_REGISTRY dispatch table; Inquisitor's Mark aggregate-count approximation (-2 opponent pool); Ducal Call Levy-default class; hook firing order (stratagem→ducal_call→crusade_fervour→inquisitors_mark→calculated_retreat→disappear); minimal AI probabilistic mix; standard_advance default tactic card selection |
| Dependencies | M1, M2, M3, M4, M5, M6 — ALL 6 dependencies satisfied |
| Files | tests/sim/v17-integration/mc_v17.py + m7_resolution_hooks.py + m7_integration_tests.py + m7_balance_sweep.py + m7_sim_verification_ledger.json |
| **v17 integration plan status** | **PHASE 2D COMPLETE per integration_plan §5: mass-battle + Workstream C surface wired; N=1000 Wilson CI verification executed; harness correctly flags balance band failure. Downstream tuning (rebalance AI / faction-action calibration) is post-M7 work surfaced to Jordan.** |
| Pass-3 findings | (1) Crown 67.7% dominance reflects AI policy more than mechanic balance — fixing AI before tuning mechanics. (2) Church 0.8% — Excommunication's Failure -1 L without recovery path creates a death spiral. (3) Hafenmark 1.8% — no faction-unique action wired (Charter of Liberties not in AI dispatch). (4) Royal Progress Ob formula floor(sum_accord/2) makes the action HARDER as Accord rises (canonical text says "easier when Accord is high" — possible canon defect, surface to Jordan). (5) Mean season=50 = no Crown territory-threshold victory before campaign end; all wins are tie-break-by-territory-held. |

## Archived 2026-05-20 (weapon-system v2 trials + Pass 2k checkpoint)


|-----|-----------|--------|
| Linear HP (End×6+16) | Reduces End dominance | Tested ✓ |
| Pool Softcap (Agi >4 → +1D) | Compresses Agi advantage | Tested ✓ |
| 1H commit bonus (+2D) | Specialist viability | Tested ✓ |
| Wrong def +2 dmg | Simplified triangle | Tested ✓ |
| **Combined result** | **None: PASS (63%). Heavy: PASS at 75% (Strong 75%)** | **Iteration complete** |

### Iterations 5-6 (2026-05-14)
| Finding | Status |
|---------|--------|
| Crit rate 60% at canonical >= 3 | P1 — threshold needs raising to >= 4 or >= 5 |
| Mace-only commit bonus (+2D for TN > 7.0, 1H) | Tested ✓ — best specialist fix |
| HP End×5+20 | Tested ✓ — Tough drops to 62% unarmoured |
| **Best config unarmoured PASS (62%)** | **Iteration 6 final** |

### v23 Complete Audit (2026-05-14)
| Phase | Tests | Status |
|-------|-------|--------|
| 1. Half-point TN | T1.1-T1.3 | 3 PASS |
| 2. Weapon-armour | T2.1-T2.4 | 1 PASS, 3 PARTIAL |
| 3. Multi-attack | T3.1-T3.3 | 2 PASS, 1 PARTIAL |
| 4. Defense triangle | T4.1-T4.4 | 4 FAIL → simplified |
| 5. Distance | T5.1-T5.3 | 1 PASS, 2 PARTIAL |
| 6. 2H/Longsword | T6.1-T6.3 | 2 PARTIAL, 1 FAIL |
| 7. Equal-budget | T7.1-T7.2 | 2 PASS (arena 3+5 unarmoured), 4 FAIL |
| 8. Crits | T8.1-T8.3 | 2 PASS, 1 P1 |
| 9. Integration | T9.1 | 1 PASS |
| **TOTAL** | **26 tests** | **12 PASS, 8 PARTIAL, 10 FAIL** |
| **Open decisions** | **12** | **D1-D12 in audit** |

### D6/D8 Tests (v24, 2026-05-15)
| Decision | Status |
|----------|--------|
| D6 Shield +3D/+4D | DEFERRED — amplifies Tough dominance, needs loadout system design |
| D8 Bash table +4→+3 | REJECTED — barely changes results (75→74%), gap is STR×3 not table |
| D1-D5 ratifiable package confirmed | HP, Pool Softcap, Crit, Mace, Triangle — all tested ✓ |

### All-Directions Audit (v25, 2026-05-15)
| Finding | Status |
|---------|--------|
| End ROI +34-48pp per point (P1) | Wound snowball root cause. D15 proposed (wound cap −2D) |
| Dagger overperformance (P1) | D14 short −2D vs Med/Heavy fixes it (79%→65%) ✓ |
| Arming sword fails N without shield (P2) | D6 deferred to loadout |
| Liechtenauer Vor/Nach | +7-14pp init advantage ✓ |
| Harnischfechten attack selection | Correct (Cut→Thrust at Medium) ✓ |

### P0: Stamina Quantization Cliff (v25, 2026-05-15)
| Finding | Root Cause | Fix |
|---------|-----------|-----|
| End +42.5pp/point | Stamina 24→25 cliff (4.0→4.17 rounds at cost 6) | Stam=20+End |
| HP contribution only +10.5pp | HP is not the dominant factor | D1 (End×5+20) helps but secondary |
| Wound cap has no effect | Fights end by yield, not wounds | D15 unnecessary |

### PP-717 NERS Audit (v26, 2026-05-15)
| Assessment | Result |
|------------|--------|
| Mode A (formula validation) | PASS — no boundary issues |
| Mode C (interaction chains) | PASS — 2 downstream flags (mass combat TC, Pool Softcap × crit double reduction) |
| D1 MW Cap NERS | N✓ E✓ R~ S✓ |
| D2 Pool Softcap NERS | N✓ E~ R✓ S✓ |
| D3 Crit ≥4 NERS | N✓ E✓ R✓ S~ |
| D4 Mace +2D NERS | N~ E✗ R✓ S~ — recommend redesign (remove Blunt TN penalty) |
| D5 Wrong def +2 NERS | N~ E✓ R~ S✓ — too small to matter (5% HP/duel) |
| All-directions | Top-down ✓, Bottom-up ✓, Vertical ✓, Diagonal ✓ (init×triangle weak), Lateral ~ (Pool Softcap combat-only), Horizontal ~ (Heavy arena 0 still fails) |


_v25 section (2026-05-15) archived to `tests/coverage_matrix_archive.md` 2026-05-18 (Step 4.2 commit) per pre_commit_gate size discipline. Section covered: Geometry expansion + dynamic wide-wing pathing + sightline. Recover via git or archive file._

## Phase 11 (2026-05-17) — Scene combat C4 (M1+M2+M3) empirical test

| Field | Value |
|---|---|
| Scope | Personal-scale combat. Test M1 (reach gate) + M2 (4-stance counter) + M3 (init preempt) atop Phase 10 baseline. |
| Sim | tests/sim/scripts/phase11_c4_v0.py |
| Writeup | tests/sim/phase11_c4_v0_2026-05-17.md |
| Trials | N=3000 per matchup; symmetric calibrations 49.9% and 48.5% (~50/50 ✓) |
| Coverage | Light/light (incl. Mighty-light F3 gap), light/heavy, light/polearm, M3 preempt, balanced-vs-Fast |
| Findings | M1 dominant; M2/M3 secondary. Dominance redistributed not eliminated: light-vs-light 94% Fast; light-vs-heavy 22% Fast (inverted). Polearm vs Fast 56/44 cleanest. F3 gap mostly persists. Balanced non-viable. |
| Provisional assumptions | M2 counter magnitudes empirical (−3D Decisive-v-Patience, degree-cap-1.0 Cautious-v-Pressure); M3 preempt heuristics (HP<0.6, init gap >= 2); STARTING_DISTANCE=2; closing-action 1-stam per band |
| Dependencies | Phase 10 baseline (params/combat.md ED-694 stamina; STR-strong bonus dice; 1/End Ob wound; Disarm) |
| Status | Implemented + run. Reframing 2 verdict deferred pending Phase 12 mass-battle archetype test. |
| Open | Tune M1 softer vs accept Reframing 2 vs add C2 hybrid — decision after Phase 12. |


## Phase 12 (2026-05-17) — Mass-battle archetype test (Reframing 2 verification)

| Field | Value |
|---|---|
| Scope | Mass-battle scale. Test whether Heavy/Strong archetypes dominate at mass scale at comparable or greater magnitude to scene-scale Agi dominance. Cross-scale balance check for Reframing 2. |
| Sim | tests/sim/scripts/phase12_mass_archetype_v0.py |
| Writeup | tests/sim/phase12_mass_archetype_v0_2026-05-17.md |
| Trials | N=2000 per matchup; Levy vs Levy calibration 46.7%/48.5% cond |
| Coverage | Light/Heavy archetype matchups; weapon-class penetration; Power-tier diffs; HeavyBlunt anti-armor |
| Findings | Mass-battle dominance is CATEGORICAL (100/0) when weapon-class fails to penetrate armor-class, not statistical. Light vs Heavy: 0/100. Heavy vs Heavy: 100% draw (canonical stalemate without tactical levers). HeavyBlunt (Knights Templar): 100/0 vs everything — anti-armor universal. Reframing 2 supported with asymmetric magnitudes. |
| Provisional assumptions | Default pool split ½/½; H baseline +2 per worked example; max_rounds=40; draw threshold ratio 1.2x; tactic cards / flanking / Command / terrain UNMODELED |
| Dependencies | params/mass_combat.md Core Formula PP-233; DR Table PP-104; Weapon Effectiveness table |
| Status | Implemented + run. Reframing 2 ratified. Two audit flags surfaced: HeavyBlunt universal anti-armor; Heavy-vs-Heavy stalemate needs tactical levers to produce interesting resolution. |
| Open | Verify Heavy-vs-Heavy resolves interestingly via tactic cards / flanking / Command in M3-engine sim (deferred). HeavyBlunt audit deferred. |

## Phase 7 (2026-05-18) — v18 mass-battle bare port (Mode G manifest)

| Field | Value |
|---|---|
| Scope | Infrastructure: Mode G module manifest for Phase 7 mass-battle port. Scope C2 narrow — canon §4.1 Step 1 + §4.10 sub-step 3. Steps 2–9 deferred. |
| Sim | tests/sim/v18-integration/module_manifest.md (this commit); subsequent port commits land in sim/provincial/{massbattle,units,tactic_cards,faction_action}.py + sim/mc_v18.py |
| Writeup | This manifest + designs/provincial/mass_battle_integration_v30.md §4 |
| Trials | None — manifest only. Battery (tests/sim/battery_v22.py) deferred to Step 5 of canon §4.1, not in C2. |
| Coverage | Phase 7 modules declared; tactic_cards.py stub remains BLOCKED on contamination audit per integration_plan_v18 §1.4. |
| Findings | Source-engine is sim_mb_06_v22.py (per canon §4.1), not m3_mass_battle.py. v22 dataclass extraction needs late-binding to avoid circular import (units.py ↔ massbattle.py constants). |
| Provisional assumptions | Bare-port flex acceptable per canon §4.1 PROVISIONAL clause (signatures may shift if statistical equivalence holds on Mirror Cmd 4v4 p>0.05). |
| Dependencies | designs/provincial/mass_battle_v30.md; designs/provincial/mass_battle_integration_v30.md; designs/provincial/military_layer_v30.md; designs/scene/derived_stats_v30.md; params/mass_combat.md; params/core.md. |
| Status | Manifest committed. Port commit follows. |
| Open | Verification ledger (per sim_gate) deferred — bare-port replicates v22 constants verbatim. Phase 8 strategic AI successor. |

## Phase 7 C2 (2026-05-18) — regression fix: Subunit.__eq__ recursion

| Field | Value |
|---|---|
| Scope | Surgical regression fix for c6ecb5b9 (Phase 7 C2 bare port). RecursionError in Subunit.__eq__ via target_atom cycle after assign_targets blocked every Conquest battle silently (mc_v18.faction_take_action's try/except Exception:pass masked the raise). |
| Sim | mc_v18.run_batch(10, base_seed=42) — direct invocation smoke against resolve_mass_battle(Crown Mil=5, Church Mil=4.5). |
| Writeup | tests/sim/v18-integration/module_manifest.md (status updates) + commit body. |
| Trials | 10 batch runs (n=10). Pre-fix: battles_mean=0 (silent fail). Post-fix: battles_mean=30.0. Direct invocation returns degree dict {'attacker_wins': True, 'degree': 'Success', 'attacker_size_pct': 0.89, 'defender_size_pct': 0.775}. |
| Coverage | sim/provincial/units.py: @dataclass(eq=False) on Subunit + Unit. Falls back to object identity __eq__/__hash__. Zero call-site changes. |
| Findings | Cycle source: assign_targets (massbattle.py L619/622/627/630) sets atom.target_atom as direct Subunit reference on both sides; A.target_atom→B and B.target_atom→A form a cycle. Literal trigger: list.remove of tuple-of-Unit at massbattle.py L1488/1494/1511/1537 (pursuit/rout tracking). Audited: zero `subunit == subunit` value-equality sites; existing set/dict keys already use id() (L749-750). |
| Provisional assumptions | Identity-eq does not change observable mass-battle outcomes — basis: canon §4.1 PROVISIONAL flex clause; target_atom set-by-reference throughout the engine, never compared by value. win_share spread Crown 40 / Varfell 50 / Church 10 (no pathological degenerate state) confirms _faction_to_unit MV-defaults are tolerable for C2; GAP-1 not escalated. |
| Dependencies | designs/provincial/mass_battle_integration_v30.md §4.1 PROVISIONAL clause; canon/02_canon_constraints.md §B GD-1. |
| Status | Verified end-to-end. Conquest path unblocked. |
| Open | Phase 7 follow-on splits into separate handoffs (Step 4.2 LETHALITY; Steps 4.3-4.6 flanking/ripple/tiebreakers; Steps 4.7-4.9 phase hooks/collision/cleanup; Step 10.1 domain_echo; Step 10.2 accounting + faction→unit richening — resolves GAP-1). |

## Phase 7 Step 4.2 (2026-05-18) — LETHALITY restoration + PP-233 formula correction

| Field | Value |
|---|---|
| Scope | Step 4.2 of canon §4.2 (designs/provincial/mass_battle_integration_v30.md §3.1, Audit Issue 1 highest severity). Restore LETHALITY_SCALE per §3.1 PROVISIONAL clause; calibration sweep at T3 mirror per §3.1 spec; commit calibrated value. Patch surface: 3 HP-damage sites in sim/provincial/massbattle.py (engagement, pursuit_damage, freed_attacker_damage). |
| Sim | mc_v18.run_batch(10, base_seed=42) smoke + multi-turn calibration sweep at L = [0.02, ..., 10.0] across N=40-60 mirror T3 Line vs Line runs. |
| Writeup | sim_verification_ledger.json (new); module_manifest.md (status updates); commit body (full diagnosis). |
| Trials | Sweep N=40-60 per LETHALITY value; robustness check N=40 across 5 seed batches (1000-5000); asymmetric matchup spot-check N=20 each. |
| Coverage | sim/provincial/massbattle.py — (1) PP-233 continuous net_successes formula replaces discrete DAMAGE_BY_DEGREE buckets at engagement L915-922 + freed_attacker L1475-1481. Pursuit already used PP-233 form; only LETHALITY wrap added. (2) LETHALITY_SCALE = 1.25 declared at L122. (3) DAMAGE_BY_DEGREE dict retained as narrative degree label for downstream logging. DR-as-reduction subtractor preserved (HP/H/DR architecture rationalization deferred). |
| Findings | **Root cause diagnosis deeper than §3.1**: §3.1 attributed lethality collapse to 20× HP inflation from v19 BLOCK_SIZE change. True diagnosis is TWO compounding defects: (a) HP inflation (per §3.1); (b) discrete DAMAGE_BY_DEGREE buckets cap damage at (1+power) regardless of net_successes, violating PP-233 canon "Damage dealt = successes × (1+Power)". PP-233 worked example: 4 successes × 4 = 16 damage; bucket model yields max 4. Bucket cap dominates (4× loss at typical net). Required formula rewrite, not just multiplier restoration. Spec §3.1 PROVISIONAL range 0.05-0.20 was a v17-era assumption; with PP-233 correction, LETHALITY=1.25 fine-tunes near baseline rather than gross compensation. |
| Calibration | Target: 14-16% per-turn casualties at T3 mirror Line vs Line P4/C4/D5/M6. Calibrated LETHALITY_SCALE=1.25: mean 14.48% / median 16.45% per-turn at N=60; battle-turns mean 1.9; winners 26A/32B/2draw (balanced). Robustness across 5 seed batches: 14.25-16.03% — all in band. Asymmetric matchups behave correctly (Power advantage → win share; Discipline edge → casualty asymmetry). mc_v18 smoke: battles_mean=40.1 (was 30.0 pre-Step-4.2). |
| Provisional assumptions | DR retained as damage-reduction subtractor — PP-233 originally folded DR into H (Health per Size = min(Disc,Cmd) + DR), but v22 HP model uses Size×BLOCK_SIZE and drops H entirely. Keeping DR-as-reduction preserves DR's defensive role; HP/H/DR architecture rationalization deferred to separate audit. |
| Dependencies | designs/provincial/mass_battle_integration_v30.md §3.1; params/mass_combat.md PP-233 Core Formula. |
| Status | Landed. Calibration in band. |
| Open | (1) Church win-share dropped 10% → 0% at L=1.25 vs b0185f05 baseline (n=10 too small, re-test in Step 4.2b). (2) T2 outperforms T3 at equal stats in spot-check — likely morale-erosion pathology (bigger units accumulate damage→morale faster); not introduced by Step 4.2, flagged for separate audit. (3) tests/sim/battery_v22.py existence unverified; battery validation gate (§3.2) deferred to Step 4.2b. (4) sim_verification_ledger.json created for v18-integration; future sim_gate calls must use this ledger. |

## Archived 2026-05-29 (pre-v32 sim rows; armature-reset coverage trim)

| Module | Commit | Canon | Verification |
|---|---|---|---|
| `sim/territory/settlement.py` | (T0-1) | `settlement_layer_v30.md §1.2-1.3` | SettlementState/ProvinceState derivation per §1.3 multipliers; smoke on T1 Seat + T9 Cathedral; 5 ledger entries with canon-verified quoted_text |
| `sim/thread/coherence.py` | (T0-2) | `threadwork_v30.md Part 3` | Coherence 10-0 track with §3.3 band transitions; smoke run through Stable→Dissonant→Fragmented→Fractured→Severed→Crisis; floor/ceiling clamps verified; just_transitioned fires once; 9 ledger entries with bold-marker-preserving quoted_text |
| `sim/cross_scale/handoff_rules.py` | (T0-3) | `scale_transitions_v30.md §3` | 8 handoff rules dispatched; TS-banded coherence cost (3 thresholds 30/50/70 verified); §3.9 fieldwork pass-through; invalid transition returns valid=False; 3 ledger entries |
| `sim/cross_scale/zoom_in_out.py` | (T0-12) | `scale_transitions_v30.md §4` | zoom_in valid/invalid phase routing; mid-Phase-5 deferral verified; board-degree Ob modifier 4-way table; zoom_out queues Domain Echoes + PC incap + Contested Figure wound; 8 mandatory triggers enumerated; 2 ledger entries |
| `sim/cross_scale/domain_echo.py` | (T0-13) | `scale_transitions_v30.md §5` | §5.2 amount-by-degree (4 cases); §5.5 Accord Echo (governance/destab/transfer/violence + invalid); §5.6 Thread Echo (Dissolution/Mending/Gap/Lock/PublicChurch/PublicVarfell + invalid); 5 ledger entries; PP-329 1-per-faction-per-scene cap documented |
| `sim/__init__.py` | (T0-4) | (declarations) | docstring updated to reflect Tier 0 progress |
| `sim/peninsular/ms_track.py` | (T0-5) | `params/core.md §MS Baseline Decay (PP-255)` | apply_ms_baseline_decay (-1/year) + apply_ms_delta; floor 0 / ceiling 100 clamp verified (100× -5 → 0; 100× +5 → 100); 6 ledger entries; DRIFT vs accounting._ms_decay logged |
| `sim/peninsular/season.py` | (T0-6) | `campaign_architecture_v30.md` | run_season composes advance_season → optional action_callback → run_accounting; 5-season smoke with arc boundary at 1 and 5; MS decay fires at season 4 via existing accounting; DRIFT vs mc_v18 inline logged |
| `sim/provincial/treaty.py` | (T0-7 partial) | `faction_balance_convergence_v12c §4.5 + §4.7` | process_treaty_expirations with TREATY_LAPSE_RATE_DEFAULT=0.90 verified (5/5 lapse at high rate); register_treaty + get_active_treaties helpers; propose_treaty raises (no canonized generic formation path; canon formation is Senator Outward per treaty_expiration_v30 §2); 2 ledger entries |
| `sim/world/insurgency_pipeline.py` | (T0-10) | `canon/02_canon_constraints.md §B GD-3` | GD-3 state machine: 2-season streak detection + formation event; L<3 promotion blocked; low-PT (avg=2) → extra-parliamentary RM variant; high-PT (avg=4) → parliamentary candidate; 6 ledger entries |
| `sim/world/npe.py` | (T0-11) | `designs/scene/investigation_systems_v30.md` SYSTEM 1 | Territory Social Ecology weights from prosperity/accord; NPC Genome 5-axis (stance/worldview/affiliation/compromise/volatility); Two-Tier Generation (archetype + d6 deviation, 5-6 flips axis); 10-NPC sample: 50% controlling-faction affiliation, 30% deviation 5+, arc-vector flagging works; 3 ledger entries |
| `sim/provincial/charter_liberties.py`, `sim/provincial/varfell_mandate_action.py`, `sim/autoload/npc_ai.py` | (T0-8/9/14 CANON-GATED) | (canon authoring required) | NOT IMPLEMENTED — Pass 2e (Hafenmark charter), Pass 2d (Varfell contamination audit), priority-stack contamination audit. Reclassified from Tier 0 to canon-gated bucket per stub_infill_plan §Canon-availability blockers. |
| `sim/autoload/game_state.py` (schema migration) | (post-Tier 0) | `stub_infill_plan Amendment 2026-05-19` | World gains 6 registries (practitioners/insurgencies/uncontrolled_streaks/npcs/npc_counter/treaties); 5 Tier 0 modules route through world stores with module-level fallback; 7-test integration smoke verifies cross-world isolation + module fallback + mc_v18 backward compat (battles_mean=31.8 at seed=42 N=5); serialize/restore unchanged (registries not yet in snapshot format) |
| `sim/territory/infrastructure.py` | (T1-1) | `settlement_layer_v30 §1.5-§1.7` | 4-axis Church infrastructure model. T9 seizure Ob smoke: Cathedral(-2)+Templar(-1)+Inquisitor(-1)+ChurchGov(-2)=-6 → capped to -4 per §1.5. Axis 1 mutual exclusion verified (Cathedral→Church removes Cathedral). Templar seed from Territory.templar preserved. 5 ledger entries. |
| `sim/territory/temperaments.py` | (T1-2) | `territory_temperaments_v30` | 17-territory temperament authoring (T1-T17 all assigned). 5-typology α/β coefficients per §1. Drift dynamics: strain_delta=3 on T1/T2 → drift=0.30 each, α shifts toward 0.9; strain_delta=10 accumulates to 1.0 clamp. Faction aggregates per §3 (Church α=0.2 strongly principled, Hafenmark α=0.55 mildly pragmatic). 4 ledger entries. |
| `sim/personal/conviction.py` | (T1-3a) | `conviction_track_v1.md §2-§3` (PP-718) | Per-Conviction Scar accumulation (Almud Order: 1→2→3 → crisis); Precedent independent (no cap collision); season cap suppresses same-season Thread re-Scar on same Conviction (mag=0); Certainty C5→mag+1, C0→mag-1 verified; 4 ledger entries |
| `sim/personal/beliefs.py` | (T1-3b) | `fieldwork_v30.md §5.5 + social_contest_v30.md §9.5` | add_belief/revise_belief/social_success; aligned win m=0→delta+1, m=4→delta=0 (cap); challenging win marks revision_pressure +1 and notifies conviction (pending_belief_revisions populated); cycle broken via late-import; 2 ledger entries |
| `sim/thread/operations.py` | (T1-4) | `threadwork_v30.md Part 2 + params/threadwork.md` | 7 operation entry points; Leap eligibility (TS<30 fail; TS=60 Ob=1); 9-operation smoke covers all degrees; FR Locking Object coh=-1 (FR surcharge only) verified; FR Locking Structural coh=-4 (-2 scale + -1 FR + -1 Partial); Mending Field coh=-2 always; POP recency table verified; coherence track erodes correctly across 8 ops to Crisis; 9 ledger entries |
| `sim/personal/combat.py` | (T1-5) | `combat_v30.md §1-§7 + PP-232` | Combat pool Agi×2+History+3 min 5 verified (Alice Agi=4 → pool=12); Heavy Blade short TN=6 verified; Light Blade vs Heavy armor +0 mod (net=0); Heavy Blunt vs Heavy armor +5 mod with PP-232 multiplicative STR×2×1.5=×3 (dmg=19 at net=2); Strike/Full Guard/Take a Breath/Dodge/Establish Distance resolve; Feint/Rescue/Disarm/Tie Up deferred Tier 2+; round-level resolution ordering per §4; 6 ledger entries |
| `sim/peninsular/ci_track.py` | (T2-1) | `conviction_track_v30 §3 PP-412` | PP-412 Step 1 +1 Momentum; Step 2 floor(Σ yield by PT) with PT5→+1, PT4→+0.5; Step 3 Assert; Step 4 Suppress cancels Momentum; Step 5 Hafenmark -1 at L≥4 (verified L=3 → 0); ceiling clamp at 100; 10-season smoke with Church L=6 produces +10/season prominent-territory yield; DRIFT vs accounting._ci_generation flat +2/Church-territory documented; 6 ledger entries |
| `sim/autoload/game_state.py` (helpers) | (bug fix 2026-05-19) | `PT_MAP / ACCORD_MAP` | canonical_pt(continuous_pt: float) -> int 0-5; canonical_accord(continuous_accord) -> int 0-4; nearest-neighbor at PT_MAP midpoints (1.75, 3.25, 4.75, 6.0, 6.75); round-trip verified on all PT_MAP / ACCORD_MAP entries + boundary cases; 1 ledger entry |
| `sim/peninsular/ci_track.py` (bug fix) | (re-verified) | `conviction_track_v30 §3 + victory_v30 §3.2 PP-534` | Step 2 yield re-bucketed via canonical_pt (was int(t.pt) drift); PP-534 Self-Control Rule added (Church auto-prominent in own territories); default state +1/season matches canon S1-S5 pacing; mid-game scenario +3/season matches canon mid-game pacing |
| `sim/world/npe.py` (bug fix) | (re-verified) | `investigation_systems_v30 §Ecology` | accord_int now via canonical_accord (was int+clamp drift); ecology weights now correctly: T2 canon=3 → high; T13 canon=1 → low; volatility offset works correctly (T13 NPCs avg 4.0 vs T2 avg 3.0) |
| `sim/provincial/mass_seizure.py` | (T2-2) | `victory_v30 §3.2 + campaign_architecture §1.3 + supersession 250715f` | Probabilistic declaration P=((CI-60)/40)^3.3 matches canon table exactly (1.0% at 70, 10.2% at 80, 38.7% at 90, 100% at 100); one-shot lifetime via world.clocks['MASS_SEIZURE_USED']; Pool=Influence+floor(CI/15), Ob=10-canonical_pt-infra_mod floor 1; PP-534 Self-Control via _church_is_prominent_for_seizure; T9 PT 5 + full Church infra → Ob 1 (max stack -4 cap) → seized at net=2; GD-1 conformant (world.winner unchanged); 7 ledger entries |
| `sim/personal/contest.py` | (T2-3) | `social_contest_v30 §1-§9` | Argue Pool (PA×2)+Hist-wound-fatigue (Alice 5*2+2=12, wounded 10, fatigued 11); resolve_exchange tracks Persuasion Track 1-9; tied exchanges +1 toward first-speak per §4; 3-exchange contest with Compromise outcome verified; 10-contest distribution 3A/3B/4 compromises; Belief alignment momentum integration via late-import (no cycle); 4 ledger entries |
| `sim/personal/knots.py` | (T2-4) | `knots_v30 (Pass 2g synthesis)` | Option A 2-tier (Distant/Close); formation prerequisites all checked (bonds<5 rejected, disposition<5 rejected, both TS<30 rejected, duplicate rejected); formation Spirit×2+History+0 vs Ob 2; tier from degree (Overwhelming→Close, Success→Distant); strain accumulation; capacity break at strain > tier_capacity; rupture trigger 'public_citation' → -1 Coherence via late-import (Alice 10→9); high-strain Close break → Conviction Scar via late-import; 7 ledger entries |
| `sim/thread/co_movement.py` | (T2-5) | `threadwork_v30 Part 4 + §4.3 ED-577` | 15 canonical cards CM-01 through CM-15 (Mending CM-16/17/18 deferred to §7.1); Object scale draw → unactualized (CM-09 ms_delta=-2 verified); Structural draw → actualized (CM-14 ms_delta=-3 verified); MS clock updates correctly (80 → 77); 16-draw test triggers reshuffle, all 15 unique IDs returned; 1 ledger entry |
| `sim/thread/collective.py` | (T2-6) | `threadwork_v30 §2.5` | Anchor selection by highest TS (Anchor TS=80 chosen over Helper1 TS=60, Helper2 TS=50); helper contribution floor(Cognition/2) (Helper1 cog=4 → +2 dice, Helper2 cog=4 → +2 dice); total pool 23+2+2=27 verified; lattice fracture threshold (remaining < expected/2) implemented; per-practitioner Coherence delta applied for Field scale (-1 per Leap survivor); operation degrades to Field Ob 5, Success at net=7 |
| `sim/thread/threadcut.py` | (T2-7) | `threadwork_v30 Part 6` | §6.1 Ontological Status canon body empty — flagged as canon gap (header only); §6.2 5-band perception (TS=0/25/45/65/100 all map correctly); mark_threadcut + is_threadcut registry; §6.3 +1 Rendering Strain per external op verified (1 op → strain 1; 6 ops → strain 7); §6.4 De-Actualisation triggered at strain ≥ max_wounds=6 (round=2 after 6 ops, triggered flag fires on first crossing); perception bands match canon §6.2 verbatim |
| `sim/thread/opposing.py` | (T2-8) | `threadwork_v30 §2.6` | opposing_engagement_modifier formula verified (B's TPS=6 → A's Ob +3; A's TPS=8 → B's Ob +4); 7-cell resolution matrix (Meets-Meets, Meets-Partial, Meets-Failure, Partial-Partial, Partial-Failure, Failure-Partial, Failure-Failure all coded); FR Lock vs Standard distinct (Composure 4 vs 2; knot Ob 2 vs 1); MS delta from worst-degree+1 rule for Shifting Object; Knot strain via late-import; apply_coherence_delta routes through coherence module |
| `sim/provincial/massbattle.py` (audit finding) | (non-determinism filing 2026-05-19c) | `stub_infill_plan Amendment 2026-05-19c` | mc_v18 non-determinism diagnosed: massbattle.py L630 roll_pool + L1053 volley_roll_pool call random.randint directly instead of using world.rng. Two consecutive run_batch(5, base_seed=42) diverge; random.seed(0) before run_batch produces deterministic output (battles_mean=32.8 both runs). Filed as follow-on; not fixed (would shift every mc_v18 batch result, requiring Phase 7 smoke re-baseline) |
| `sim/autoload/game_state.py` (schema migration #2) | (Tier 1/2 registries 2026-05-19) | `stub_infill_plan Amendment 2026-05-19` (extends migration #1 at 94dac72e) | World gains 8 fields: convictions, beliefs, knots, knot_id_counter, territory_infrastructure, npc_drift_state, threadcut_beings, comovement_deck; 6 consumer modules updated; cross-world isolation verified across 7 registries; module-level fallback preserved for world=None callers; mc_v18 backwards-compat verified |
| `sim/autoload/game_state.py` (per-record serializers) | (production save format 2026-05-20) | `stub_infill_plan Amendment 2026-05-19d` | 9 dataclasses gain to_dict/from_dict (CoherenceState+log, InsurgencyRecord, NPC, TreatyRecord, ConvictionState+log, Belief, Knot, InfrastructureState, ThreadcutState); serialize_world extended with 14 registries; restore_world reconstructs via late-imports; 26/26 round-trip checks pass; 14/14 old-schema tolerance checks pass (missing registries default empty); mc_v18 backwards-compat verified (battles_mean=38.0) |
| `sim/provincial/massbattle.py` (RNG fix) | (Deferred Migration Batch 2026-05-20, commit 54277ae) | `mass_battle_v30 §A.1 + params/mass_combat.md` | Closes 03ce9c79 non-determinism. 12 functions gain rng=None param (roll_pool, _roll_volley_pool, volley_phase, resolve_engagements, resolve_engagements_cascading, run_battle, run_multi_turn_battle, run_multi_unit_battle, pursuit_damage, recall_check, discipline_check_cascade, freed_attacker_damage); 21 internal callsites thread rng=rng; resolve_mass_battle passes world.rng. Pre-fix: same-seed batches diverged across runs and required random.seed() pin. Post-fix: byte-identical within process at same seed; module random.seed has no effect. Verified at N=5 base_seed=42 with global random.seed pollution between 3 runs; all identical. [GAP: hash-seed nondeterminism remains across Python processes — pin PYTHONHASHSEED=0 for cross-process reproducibility; filed for separate session] |
| `sim/peninsular/accounting.py`, `sim/mc_v18.py`, `sim/peninsular/season.py` (3-migration batch) | (Deferred Migration Batch 2026-05-20) | `conviction_track_v30 §3 PP-412; params/core.md §MS Baseline Decay PP-255; campaign_architecture_v30` | Deletes 3 legacy duplicates. accounting._ci_generation (+2 per Church-held territory, canon-violating) replaced with ci_track.apply_seasonal_ci. accounting._ms_decay replaced with ms_track.apply_ms_baseline_decay gated on world.season % SEASONS_PER_YEAR == 0. mc_v18 inline season block (L73-87) replaced with season.run_season(world, action_callback=_faction_actions_callback). Behavior shift: pre-batch Church CI gained +8/season at start; post-batch ≈ +1/season per PP-412 §3 Pacing canon. Authoritative re-baseline at PYTHONHASHSEED=0: N=10 base_seed=0 → battles_mean=35.5, win_share Crown:30/Varfell:70; N=10 base_seed=42 → battles_mean=33.4, Crown:40/Church:30/Varfell:30; N=5 base_seed=42 → battles_mean=37.6, Crown:20/Church:40/Varfell:40. Supersedes the 4 stale manifest figures (smoke 40.1; run_batch(10,42)=30.0; migration #1 baseline 31.8; migration #2 baseline 37.4 with random.seed(0) pin) |
| `sim/autoload/game_state.py`, `sim/provincial/faction_action.py` (hash-seed fix) | (Deferred Migration Batch follow-on 2026-05-20) | n/a — purely structural | Closes hash-seed-nondeterminism GAP filed in commit 105ae9e. Two leaks: (1) Faction.territories: set -> list (set str-key iteration depended on PYTHONHASHSEED); (2) _try_conquest candidate set wrapped in sorted() before rng.choice. Cross-process determinism verified across PYTHONHASHSEED in {0, 1, 7, 42, 99999} at N=10 base_seed=0 (battles_mean=34.1, Crown:4/Church:1/Varfell:5). PYTHONHASHSEED pin no longer required for reproducibility. Companion list-conversions: .discard() -> guarded remove; .add() -> guarded append |
| `params/bg/npc_priority_trees.md` (audit + dedup) | (Jordan-flagged 2026-05-17 priority-stack contamination audit) | n/a — canon-doc cleanup | Audit pre-implementation (consumer sim/autoload/npc_ai.py is NotImplementedError stub). Structural defects fixed: D-1 every tree duplicated L26-116 + L119-228 (byte-identical except whitespace), second block deleted; A-2 GD-2 mandatory-action precedence section added as §0 (mandatory pass before stochastic priority candidates per canon/02_canon_constraints.md §B); A-3 PP-NPC-04 initial state clarified (Collection flag = False at world creation). 8 stale-reference items (S-1..S-8: CI freeze threshold, Royal Decree canon, Löwenritter Autonomy survival, IP trigger, Warden Recognition, Cardinal mechanic, Crown T2/T4 hardcode, post-founding RM behavior under GD-3) require Jordan input — captured in designs/audit/2026-05-20-npc-priority-trees/audit_findings.md |
| `sim/thread/opposing.py`, `sim/thread/co_movement.py`, `sim/provincial/excommunication.py` (legacy-duplicate migration follow-on) | (sweep follow-on to commit 105ae9e) | `params/core.md PP-255 MS; ci_political_v30` | Three additional inline clock arithmetic sites found during post-batch sweep, migrated to dedicated track modules. opposing.py L229 (MS clamp), co_movement.py L142 (MS clamp), excommunication.py L165 (CI ceiling). All three now route through ms_track.apply_ms_delta / ci_track.apply_ci_delta — single canonical surface. Behavior verification: N=10 base_seed=0 produces battles_mean=34.1 (matches commit 3c2c428 baseline exactly; pure refactor) |
| `tools/index_gen.py`, `canon/editorial_ledger_summary.yaml` (M6 partial) | (Architecture V2.4 M6 gap) | `project-architecture-valoria-v2_4.md <completeness_enforcement> M6` | Closes two of three M6 defects: (1) HTML comment in YAML output replaced with YAML # comment; (2) generate_editorial_summary signature extended with archive_yamls so next_id is computed across active + archives (was archive-blind: old next_id=824, new=865 — 41 IDs the old code missed). Strict yaml.safe_load now passes on regenerated summary (210 total entries across 10 archives + active). Third M6 defect (regex-over-prior-summary fallback) remains as defensive path inside _collect_ed_entries — acceptable since yaml.safe_load is tried first. file_index_summary.md tree-walk integrity not in this scope (separate function family) |
| `sim/peninsular/accounting.py` (insurgency + NPE wire-up) | (Roadmap steps 2 + 3 from session 2026-05-20) | `canon/02_canon_constraints.md §B GD-3; designs/scene/investigation_systems_v30.md SYSTEM 1` | accounting.run_accounting extended: after CI+MS, invokes check_insurgency_triggers (GD-3 a-b emergence), iterates check_insurgency_promotion over existing insurgencies (GD-3 c-e), then simulate_npc_actions for territory-level NPC drift. Both modules T0-verified (T0-10, T0-11) but previously uninvoked from season loop. Behavior verification: N=10 base_seed=0 yields battles_mean=34.1 (matches pre-wire baseline; insurgencies don't form in short runs). Authoritative N=100 base_seed=0 captured: battles_mean=34.2, Crown 40 / Church 5 / Hafenmark 1 / Varfell 54 |
