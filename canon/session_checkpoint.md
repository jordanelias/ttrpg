---
schema_version: 1
session_token: 6a51d0a7a54a8ce3
created_at: '2026-04-20T02:25:29.184099+00:00'
status: active
task_scope: Full campaign simulation — Session 1 done, Session 2 pending
context_tokens_at_checkpoint: 50361
files_verified:
- tests/sim/valoria_full_campaign_sim.py
- /home/claude/sim_verification_ledger.json
- params/bg/core.md
- params/bg/clocks.md
- params/factions/stats_1_7_scale.md
- designs/provincial/factions_personal_v30.md
sim_ledger_present: true
commits_this_session:
- 129f2f2b
completed:
- ED-667 / ED-717 / ED-632 / ED-633 / ED-721 all closed in ledger
- 'canonical_sources.yaml systems: block populated (17 full_stack + 6 supporting)'
- tests/sim/campaign_simulation_readiness_2026-04-19.md published
- Session 1 foundation committed (129f2f2b) — 623 lines, all smoke tests pass
- 103-entry sim_verification_ledger.json covering all Session 1 constants
pending:
- 'Session 2: Territory model (T1-T15 with Proximity/PV/SW/Accord)'
- 'Session 2: Domain Action framework + canonical DAs (6+ starter actions)'
- 'Session 2: Piety Yield + CI political pool bonus'
- 'Session 2: Peninsular Strain propagation'
- 'Session 2: Mass combat (simplified) + Contest system'
- 'Session 2: Faction AI stub (priority-based DA selection)'
- 'Session 2: 40-season smoke test with real DAs'
- 'Session 3: Threadwork, Victory, Scale transitions'
- 'Session 3: NPC priority trees (7 major NPCs) + Arc transitions'
- 'Session 3: Royal Assassination fuse, Tensions Deck activation'
- 'Session 3: Deterministic test corpus (sim_var_01-06 regression)'
decisions_made:
- Single-file sim structure (valoria_full_campaign_sim.py) preferred over multi-module
  package
- 'Ledger-first discipline: inline canonical comments + /home/claude/sim_verification_ledger.json'
- Default seed 42 for smoke tests
- Session 1 scope = foundation only; DA stub retained for Session 2
open_questions:
- Ministry NPC design doc still not located (flagged in params/bg/core.md NPC-Only
  Factions)
next_bootstrap_actions:
- Re-fetch params/factions/stats_1_7_scale.md §Domain Action Table and faction_politics_v30.md
  §2 for DA catalog
- Read designs/territory/settlement_layer_v30.md to extract T1-T15 canonical data
- Read designs/provincial/ci_political_v30.md §1 for Piety Yield formula
- Extend valoria_full_campaign_sim.py with §6 Territory, §7 Domain Actions, §8 Contests
- Append ledger entries for each new constant
---

# Session Checkpoint — 2026-04-20 02:25 UTC

**Task scope:** Full campaign simulation — Session 1 done, Session 2 pending
**Session token:** `6a51d0a7a54a8ce3`
**Context at checkpoint:** ~50,361 tokens

## Narrative

## Session 1 foundation — COMMITTED

tests/sim/valoria_full_campaign_sim.py landed at commit 129f2f2b. Contains:
- §1 Core engine: dice pool (d10, TN 7, face values 1/7-9/10 = -1/+1/+2), contest(),
  resolve_degree() with PP-179 + PP-249 thresholds and Ob 10 exception.
- §2 Faction model: 6-stat 1-7 scale, ±2/season cap, Military cap (ED-039),
  starting_factions() with all 7 active factions (Niflhel dissolved).
- §3 Clocks: RS/CI/IP/PI/AER/Torben/Elske/WR/WC/Strain/Autonomy; CI ±5/season
  uniform cap (PP-504, ED-721 Option A); PI +2/season accrual cap; Strain 0-10;
  Mass Seizure gate at CI >= 60.
- §4 Seasonal loop: accounting_phase() with CI auto-advance, battle
  consequences, Strain decay, PI accrual/recovery, Mandate recovery, Autonomy
  check, endgame (Rupture, PI 20).
- §5 Smoke tests: dice engine verified; 10-season peaceful run verifies state.

Verification ledger at /home/claude/sim_verification_ledger.json has 103
entries covering 43 distinct values. sim_fabrication_check PASSES.

Session 2 pending. Canonical docs for Session 2 already fetched this session
(large — pushed context to 75%); next session should re-fetch on demand
rather than preemptively. See pending work below.

## What must come next

Session 2 "Middle Layer" scope:
1. Territory model — 15 territories (T1-T15) with Proximity rating 0-5,
   PV (Prosperity Value), SW (Spiritual Weight), Accord 0-3, controller faction.
   See designs/territory/settlement_layer_v30.md for canonical territory data.
2. Domain Action framework — DataClass: name, actor, cost, stat, Ob,
   degree-outcome map. Start with Royal Decree (Crown, stats_1_7_scale §Domain
   Action Table L79), Assert/Suppress (Church), Sovereign Authority Doctrine
   (Hafenmark/Baralta), Private Collection (Varfell/Vaynard), Community
   Weaving (RM), Trade Deal (Guilds). See params/factions/stats_1_7_scale.md
   §Domain Action Rules and faction_politics_v30.md for full catalog.
3. Territory control — seize action, contest action, loss triggers, Mass
   Seizure (CI >= 60 one-shot), Assert (Church), occupation PV zeroing.
4. CI / Piety Yield mechanics — Piety Yield formula from ci_political_v30
   §1 (CI from Piety Yield = Σ(PT tier × SW factor) per prominent territory,
   SW factor = SW/5; T9 counts uniformly per ED-721 Option A).
5. Church political pool bonus — floor(CI/20) bonus dice; opposing Mandate
   -floor(CI/30) per ci_political §7.2.
6. Peninsular Strain propagation — battle +1, faction elimination +2, revolt
   +1, peaceful -1.
7. Mass combat (simplified) — mass_battle_v30. Needed for battle resolution.
8. Contest system (simplified) — params/contest.md Grand Debate 5-exchange
   structure for Parliament/theological contests.
9. Faction AI stub — priority tree: if Mandate < starting, repair; else if
   threatened, defensive; else expand. Full priority trees from npc_behavior_v30
   §7-8 in Session 3.
10. Smoke test: 40-season run, factions take DAs, verify endgame lands
    plausibly (some faction wins or shared loss fires).

Implementation note: keep single-file structure (valoria_full_campaign_sim.py).
Append new sections §6-§10. Ledger grows incrementally — add entries for each
new canonical value read.

## Session 3 "Top Layer + Tests" scope (for reference)

- Threadwork mechanics (Thread Tension, Coherence, Leap, Weaving)
- Victory conditions (all 8 factions, Peninsular Sovereignty)
- Scale transitions (personal → faction → strategic)
- NPC priority trees (Almud, Himlensendt, Baralta, Vaynard, Ehrenwall, Torben,
  Edeyja) per npc_behavior_v30 §7-8
- Arc transitions per npc_behavior_v30 §5.2 Arc Maps + arc_expansion_v30
- Royal Assassination fuse activation (params/bg/royal_assassination.md)
- Tensions Deck card activations (params/bg/tensions_deck.md)
- Deterministic-seed test corpus reproducing sim_var_01 through sim_var_06
  scenarios
- Regression tests against the narrative sims sim_x_01 through sim_x_36+

## Completed this session

- ED-667 / ED-717 / ED-632 / ED-633 / ED-721 all closed in ledger
- canonical_sources.yaml systems: block populated (17 full_stack + 6 supporting)
- tests/sim/campaign_simulation_readiness_2026-04-19.md published
- Session 1 foundation committed (129f2f2b) — 623 lines, all smoke tests pass
- 103-entry sim_verification_ledger.json covering all Session 1 constants

## Pending (in order)

1. Session 2: Territory model (T1-T15 with Proximity/PV/SW/Accord)
2. Session 2: Domain Action framework + canonical DAs (6+ starter actions)
3. Session 2: Piety Yield + CI political pool bonus
4. Session 2: Peninsular Strain propagation
5. Session 2: Mass combat (simplified) + Contest system
6. Session 2: Faction AI stub (priority-based DA selection)
7. Session 2: 40-season smoke test with real DAs
8. Session 3: Threadwork, Victory, Scale transitions
9. Session 3: NPC priority trees (7 major NPCs) + Arc transitions
10. Session 3: Royal Assassination fuse, Tensions Deck activation
11. Session 3: Deterministic test corpus (sim_var_01-06 regression)

## Decisions made

- Single-file sim structure (valoria_full_campaign_sim.py) preferred over multi-module package
- Ledger-first discipline: inline canonical comments + /home/claude/sim_verification_ledger.json
- Default seed 42 for smoke tests
- Session 1 scope = foundation only; DA stub retained for Session 2

## Open questions

- Ministry NPC design doc still not located (flagged in params/bg/core.md NPC-Only Factions)

## Next bootstrap actions

*(When a new session bootstraps, these are the first steps to take.)*

1. Re-fetch params/factions/stats_1_7_scale.md §Domain Action Table and faction_politics_v30.md §2 for DA catalog
2. Read designs/territory/settlement_layer_v30.md to extract T1-T15 canonical data
3. Read designs/provincial/ci_political_v30.md §1 for Piety Yield formula
4. Extend valoria_full_campaign_sim.py with §6 Territory, §7 Domain Actions, §8 Contests
5. Append ledger entries for each new constant

