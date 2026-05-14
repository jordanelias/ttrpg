# Valoria Simulation Coverage Matrix

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
- Status: PROPOSED. Needs sim validation. Large blast radius (replaces PP-232 weapon system).
