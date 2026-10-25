"""The v10 batch map: which position belongs to which batch, and each batch's card.

STATE AFTER THE DEPENDENCY SEQUENCE (`2026-10-24-v10-09-build-00-sequence.md`): the batch assignments, ORDER and CARDS below follow the final cut in `-03` (NM-W3 and SC-06 moved to B10-01, NM-W0 to B10-02; CP-T02-06 is in B10-10 since the NERS fold; CL-EVENTS was added by it). The cut handles REM-40, REM-41, REM-51, CP-T02-04, CP-T02-08, CP-T05-05, CP-T06-06 and CP-T07-01 are kept as keys, mapped to CUT, so the coverage run still knows them; their dispositions are in `-07` section 2. The plan files are the record: where this file and `-03` differ, `-03` wins.

This file is the author's judgment in one place; it is not a plan."""

SPINE = ["B10-01", "B10-02", "B10-03", "B10-04", "B10-05", "B10-06", "B10-07", "B10-08", "B10-09",
         "B10-10", "B10-11", "B10-12", "B10-13", "B10-14", "B10-15", "B10-16", "B10-17", "B10-18",
         "B10-19", "B10-Z"]

CARDS = {
 'B10-01': dict(name='ADOPT AND CORRECT THE RECORD', lanes='IN', code=False,
   gate='adoption by Jordan (the steps are the `-03` card and `-00` section 9)',
   exit='python tools/currency_consistency_check.py; python -m engine.season.harness.register --requirements; python tools/validate_ed_citations.py; grep -c ^## Status: per plan file; register --check --rule R0,R1,R2,R3; grep -c valoria_master_workplan_v9 references/lane_assignments.yaml -> no drift; exit 0; clean; 1 per file; no new violation after CR-02 (f); 0',
   hash='E',
   shared='engine/season/requirements.yaml; CURRENT.md; HANDOFF.md; registers/handoffs/HANDOFF_IN.md; registers/handoffs/HANDOFF_<LANE>.md Open rows; engine/season/hole_register.yaml (text only); references/lane_assignments.yaml; references/definitions/vocab_source.yaml; CLAUDE.md 5 (one sentence, proposed text until M11)',
   build='2026-10-24-v10-09-build-B10-01.md'),
 'B10-02': dict(name='INSTRUMENTS THAT CAN SEE THE FAILURES', lanes='IN', code=True,
   gate='merged: B10-01',
   exit='after REM-16 and before CR-01/IN-18: World.content_hash() at build_realm(0) and after aperture 1 s (s=0,1,2) against the base commit; python -m engine.season.harness.report && python -m engine.season.harness.delta <base sha> -> hashes EQUAL; PROBE FLIPS 0; the three-seed baselines for B10-05 and B10-06 recorded in the close commit body',
   hash='mixed (movers: CR-01 (test-file pins only); IN-18 (only if G5 builds))',
   shared='engine/season/harness/corpus_run.py (attribute, run_case); engine/season/harness/aperture.py; engine/season/harness/decision_spread.py; engine/season/harness/storybar.py; engine/season/loop/predicates.py (TRACE lines only); engine/season/requirements.yaml (measured: paragraphs); modules/combat/ and tests/valoria/test_combat_lever_sign_safety.py (CR-01); engine/season/loop/witness.py (IN-18, only if G5 builds)',
   build='2026-10-24-v10-09-build-B10-02.md'),
 'B10-03': dict(name='CONFORMANCE A: NO-HASH DELETIONS AND CORRECTIONS', lanes='IN, WR', code=True,
   gate='merged: B10-02; held positions: DEF-9 (M11)',
   exit='per item (home); build_realm(0) hash against the base commit; pathres.load_alias_map() for each deleted path; pytest tests/valoria once at close -> hash EQUAL; an exact-file FORK row per deleted path; suite green',
   hash='E (movers: REM-45 (threadwork oracle history cap; engine/tests goldens declared if they move))',
   shared='engine/dice_engine/sigma_leverage.py; engine/season/loop/resolve.py and engine/season/state/world.py (CR-06); systems/threadwork/sim/operations.py; engine/season/runs/ (untrack); tools/evacuation_plan.py and tests/valoria/test_engine_params_bridge.py; references/restructure_ledger.md (FORK rows); engine/engine_params/params_tables.yaml and CLAUDE.md 5 (DEF-9, held); CURRENT.md:27 (L0-2, proposed text)',
   build='2026-10-24-v10-09-build-B10-03.md'),
 'B10-04': dict(name='HUNGER', lanes='SE, IN', code=True,
   gate='merged: B10-02; held positions: REM-52 (M6)',
   exit='python -m pytest engine/season/tests/test_hunger.py -q; census hunger_by_settlement on build_realm(0) and on harness/scarce.build -> bands move as the falsifier states; a scarce world reads below fed; build_realm(0) hash EQUAL',
   hash='E (movers: REM-52 (held on M6; lands later as its own declared-mover commit))',
   shared='engine/season/queries/world_q.py (hunger); engine/season/harness/populated.py (census); engine/season/data/fixtures.py (hunger_band_floors; body_step held); engine/season/hole_register.yaml (one NUMBER row); engine/season/tests/test_hunger.py (new)',
   build='2026-10-24-v10-09-build-B10-04.md'),
 'B10-05': dict(name='FORMATION: ACTS FORM ONLY ON WHAT THEY CAN REACH', lanes='IN', code=True,
   gate='merged: B10-02, B10-04',
   exit='PYTHONHASHSEED=0 python -m engine.season.harness.aperture 1 s (s=0,1,2) per item; register --requirements -> each classed verb exists:<Kind>=0 refusals fall to 0 (base 3,137 over three seeds, a lower bound); no claim that R-05 moves',
   hash='mixed (movers: REM-22; REM-23; CP-T05-04; REM-24; REM-25; REM-2C)',
   shared='engine/season/verb_table.yaml; engine/season/rosters.yaml (referent_classes); engine/season/queries/world_q.py (questions_for splice, own_referents_of_class); engine/season/data/verbs.py (DECLARED_CLASSES; VerbRow.scale removal); engine/season/decision/options.py; count pins: engine/season/tests/test_governance_build.py, test_season_shape.py (len(VERB_TABLE) == 56; executed and always-refused sets); engine/season/tests/test_referent_class_stamps.py (new)',
   build='2026-10-24-v10-09-build-B10-05.md'),
 'B10-06': dict(name='REACH, SCARCITY AND RESTORES', lanes='IN', code=True,
   gate='merged: B10-02, B10-05',
   exit='aperture 1 s per item; at close the R-01/R-02 re-take: proposals/2026-09-04-degree-sweep wd_chunk.py x (3 arms x 3 fixture points x 4 slices) then wd_collect.py; then corpus_run -> reconvergence below 96% at 2x3 with none >= default; march reaches a field (field.won/lost/unopposed at aperture 1 s) or the failed link is named; confer and oblige read before and after REM-2B',
   hash='mixed (movers: REM-27; REM-29; REM-2B; REM-26 and REM-28 only where a row is classed)',
   shared='engine/season/verb_table.yaml; engine/season/rosters.yaml; engine/season/loop/effects_*.py; engine/season/loop/sides.py (REM-27); engine/season/data/requires.py (REM-29 room stem); engine/season/queries/world_q.py (fields_named, has_room); modules/mass_battle/ (read only)',
   build='2026-10-24-v10-09-build-B10-06.md'),
 'B10-07': dict(name="CONFORMANCE B: THE CHOOSER'S DEAD SENSATION", lanes='IN', code=True,
   gate='merged: B10-06; holds (whole batch): M11; held positions: REM-44 (M11)',
   exit='rg -n subsistence engine/season/{decision,state/carriers.py,loop/deliberate.py,loop/driver.py}; realm 2-season hash at seeds 0-2 before and after -> only comments recording the deletion; hash equal or re-pinned old to new with the count of saved re-deliberations',
   hash='M (movers: REM-44 (declared candidate: the fingerprint skip))',
   shared='engine/season/decision/choose.py, decision/__init__.py; engine/season/loop/deliberate.py; engine/season/loop/driver.py; engine/season/state/carriers.py (Sensation); every harness caller of SeasonDriver.season; architecture/meta/04_CODE_ARCHITECTURE.md B.10, C.3 and architecture/meta/01_AXIOMS.md D.10 (L1-6, L1-7)',
   build='2026-10-24-v10-09-build-B10-07.md'),
 'B10-08': dict(name='DICE: ONE FACULTY, ONE ODDS FUNCTION, ONE CEILING', lanes='IN', code=True,
   gate='merged: B10-02, B10-03, B10-06',
   exit='each item falsifier and paired-seed control as its home states; band_odds(2, 2) == (0.74, 0.19, 0.07, 0.0) and the 200,000-roll arm; H-213 re-measure -> as the homes state; the shipped practice arm byte-equal at practice_cap = 0',
   hash='mixed (movers: CP-T01-04 (corpus draws at Ob 1.5); CP-T01-06 (every seed where a hostile term or a forged Record is met))',
   shared='engine/season/seam/wrappers/sigma.py; engine/season/seam/ladder.py; engine/dice_engine/sigma_leverage.py (band_odds, settle_margin); modules/social_contest/roll.py (obstacle); engine/season/rosters.yaml; engine/season/loop/resolve.py (_contest); engine/season/loop/deliberate.py and state/carriers.py (CP-T01-05 slot, if built); engine/season/data/fixtures.py',
   build='2026-10-24-v10-09-build-B10-08.md'),
 'B10-09': dict(name='PERSONS: DEATH NAMES SEATS, THE KNOWN, THE SUCCESSOR', lanes='IN, SC, SE, WR', code=True,
   gate='merged: B10-05, B10-08',
   exit='each item falsifier and control as its home states; corpus_run over three seeds for CR-10; IN-61 tripwire test_arrangements.py::test_a_hold_disposing_row_is_reported_by_c1_until_determine_can_open_a_hold -> as the homes state; the tripwire goes red the day IN-61 site exists and is re-recorded in that commit',
   hash='M (movers: CP-T02-01; CP-T02-02 (every pin naming off_npc_* re-records); CP-T03-00 (size measured at the commit, seeds 0-2, two seasons); CP-T02-03; CP-T02-05; IN-12; IN-61; CR-10)',
   shared='engine/season/state/world.py; engine/season/loop/census.py; engine/season/offices.yaml; engine/season/decision/options.py; engine/season/data/verbs.py; engine/season/queries/person_q.py; engine/season/queries/world_q.py; engine/season/rosters.yaml; engine/season/decision/questions.py; engine/season/state/carriers.py; engine/season/seam/ladder.py and loop/effects_combat.py (CP-T03-00); engine/season/harness/play_surface.py; engine/season/state/gate.py (IN-61, IN-12)',
   build='2026-10-24-v10-09-build-B10-09.md'),
 'B10-10': dict(name='SCALE BUILDS (D-2: THE DESIGNS STAY HELD)', lanes='IN, PC, MB', code=True,
   gate='merged: B10-09; held positions: CP-T02-06 (M7)',
   exit='REM-31: AUTOMATED and PLAYABLE-with-scripted-choices-equal-to-the-chooser at one content_hash, a differing choice moves it, the permutation falsifier with the callback on; REM-30: a creation arm switched off reproduces the pre-build hash; REM-32: a real fold reaches Won at a fixture above 1 -> as stated; REM-32 EQUAL at k = 1',
   hash='M (movers: REM-31 (every seeded season that fights); REM-30 (where its creation arm is on))',
   shared='engine/season/loop/driver.py; engine/season/loop/deliberate.py (REM-31 callback); engine/season/seam/wrappers/combat.py; modules/combat/wrapper.py, modules/combat/fight.py; modules/mass_battle/massbattle.py (REM-32); engine/season/state/carriers.py and decision/ (REM-30); engine/season/harness/play_surface.py (CP-T02-06); the seeded goldens',
   build='2026-10-24-v10-09-build-B10-10.md'),
 'B10-11': dict(name='PERSONAL COMBAT (T03)', lanes='PC', code=True,
   gate='merged: B10-08, B10-09, B10-10; held positions: CP-T03-07 (M6); CP-T03-08 (M6); CP-T03-03 (M2); CP-T03-04 (M2); CP-T03-06 (M1); CP-T03-10 (parked/cut/withdrawn/leave); CP-T03-11 (parked/cut/withdrawn/leave)',
   exit='per item as its home states; aperture 1 s per verb added -> as stated',
   hash='M (movers: CP-T03-01 (stem + cohort bound); CP-T03-02; CP-T03-09; PC-10 (wherever a challenge forms); CP-T03-07 and CP-T03-08 (when M6 releases them: body_ceiling is a schema mover))',
   shared='modules/combat/; engine/season/seam/wrappers/combat.py; engine/season/loop/effects_combat.py; engine/season/verb_table.yaml; engine/season/data/requires.py (the individual stem); engine/season/rosters.yaml (duel_terms); engine/season/state/gate.py (CP-T03-09 detain opener); engine/engine_params/pc_matchup.json and tools/export_pc_matchup.py (deleted by CP-T03-05)',
   build='2026-10-24-v10-09-build-B10-11.md'),
 'B10-12': dict(name='MASS BATTLE (T04)', lanes='MB', code=True,
   gate='merged: B10-05, B10-10, B10-11; held positions: CP-T04-04 (M4); CP-T04-10 (M3); CP-T04-09 (M1)',
   exit='per item as its home states; each exit reports the fought-field count it was measured on; CR-12: python3 -m systems.mass_battle.sim.lanchester_signature on both per-cell arms before and after -> EQUAL at the shipped arms; a mover on each flip, declared',
   hash='mixed (movers: MB-07r (golden digests); CP-T04-06 (besiege roster flip, own commit); CR-12 (when built); CP-T04-04 (when M4 releases it))',
   shared='modules/mass_battle/ (massbattle.py, orchestration.py, config.py); engine/season/loop/encounter.py; engine/season/seam/wrappers/mass_battle.py; engine/season/verb_table.yaml (march; marshal, besiege, surrender rows); engine/season/loop/sides.py (CP-T04-04, held); engine/season/loop/effects_information.py (CP-T04-07); tools/ci_golden_modes_check.py and engine/tests goldens (MB-07r, CR-12)',
   build='2026-10-24-v10-09-build-B10-12.md'),
 'B10-13': dict(name='SOCIAL CONTEST AND PROCEEDINGS (T05)', lanes='SC', code=True,
   gate='merged: B10-05, B10-06, B10-08, B10-12',
   exit='per item on its hand-built falsifier worlds (the realm forms about three determine in twelve seed-seasons); tell attempts, news.told and chained-claim counts per season before and after CP-T05-03, seeds 0-2 -> as stated; the chained-claim fall is the price, recorded',
   hash='M (movers: SC-02 (re-source); CP-T05-01; CP-T05-02; CP-T05-03)',
   shared='engine/season/seam/wrappers/sigma.py (contest_input); engine/season/queries/world_q.py (reception, proofs, hearing); engine/season/loop/effects_governance.py; engine/season/arrangements.yaml; engine/season/data/ (rosters.py DEGREE_STEP read); engine/season/loop/witness.py and data/verbs.py (CP-T05-03 tell.refused kind)',
   build='2026-10-24-v10-09-build-B10-13.md'),
 'B10-14': dict(name='FIELDWORK AND INFORMATION (T06)', lanes='FI', code=True,
   gate='merged: B10-02, B10-05, B10-06, B10-13; held positions: CP-T06-08 (parked/cut/withdrawn/leave)',
   exit='per item as its home states; test_fi03_trail.py re-recorded and declared; the (kind, place) found-vs-logged count per seed for CP-T06-02 -> as stated',
   hash='M (movers: CP-T06-09; CP-T06-01; CP-T06-04; CP-T06-02; CP-T06-07; CP-T06-05)',
   shared='engine/season/loop/witness.py; engine/season/epistemic.py; engine/season/state/attribution.py; engine/season/loop/effects_information.py; engine/season/state/world.py (_on_logged index); engine/season/rosters.yaml (record_kinds cover; covert_kinds); engine/season/data/rosters.py (COVER_KEY, COVER_AS); engine/season/verb_table.yaml (sabotage class; interview retype); engine/season/tests/test_fi03_trail.py (declared re-record)',
   build='2026-10-24-v10-09-build-B10-14.md'),
 'B10-15': dict(name='THREADWORK (T07)', lanes='WR, PC', code=True,
   gate='merged: B10-03, B10-05, B10-14; held positions: WR-01 (M2)',
   exit='per item as its home states; CR-13: a Leap at Partial and at Failure each net 0 Coherence, Weaving keeps the blanket penalty -> as stated; CR-13 and the shipped () tuple of CP-T07-07 hash EQUAL',
   hash='mixed (movers: CP-T07-02 (schema: Person.coherence); CP-T07-03 (schema: Site.locked); CP-T07-09, -04, -06, -10, -08, -11 per working; IN-32)',
   shared='systems/threadwork/sim/operations.py (CR-13); engine/season/seam/wrappers/threadwork.py (new host); engine/season/state/carriers.py (Person.coherence; Site.locked); engine/season/write_matrix.yaml; engine/season/rosters.yaml (thread_scales, cells); engine/season/verb_table.yaml (weave, lock, mend, ward, thread_read, tie / knot); engine/season/loop/matter.py (locked-Site yield); engine/season/queries/world_q.py (in_equilibrium, held_load); engine/season/decision/budget.py (coherence_band_floors); engine/season/loop/effects_information.py (_eff_tie)',
   build='2026-10-24-v10-09-build-B10-15.md'),
 'B10-16': dict(name='SETTLEMENTS, GOVERNANCE AND ECONOMY (T08)', lanes='SE', code=True,
   gate='merged: B10-04, B10-06, B10-15; held positions: CP-T08-07 (M17); CP-T08-04 (M5); IN-45 (M5); IN-52 (M17, M3); SE-04 (M1, M11); SE-06 (M1); CP-T08-09 (parked/cut/withdrawn/leave)',
   exit='per item as its home states, on harness/scarce.governed for CP-T08-06 compliance, CP-T08-08; aperture 4 0 is the R-04 conjunct (1) reader and is NOT credited by hand-built greens -> off arms EQUAL; on arms declared',
   hash='mixed (movers: IN-14 (budget moves); CP-T08-08 (declared candidate))',
   shared='modules/settlements/ (produce.py ProduceInput); engine/season/loop/matter.py; engine/season/queries/world_q.py (labour, price_of, unrest); engine/season/queries/person_q.py (stability read); engine/season/data/fixtures.py; engine/season/rosters.yaml; engine/season/decision/budget.py (IN-14, CP-T08-10); engine/season/loop/driver.py (IN-14 rounds); engine/season/loop/effects_economy.py (CP-T08-08 upkeep_due); engine/season/tests/test_season_shape.py (test_n3 floor re-take)',
   build='2026-10-24-v10-09-build-B10-16.md'),
 'B10-17': dict(name='FACTIONS, WAR AND DIPLOMACY (T09)', lanes='FA', code=True,
   gate='merged: B10-05, B10-06, B10-08, B10-09, B10-12, B10-16; held positions: IN-36 (M1); FA-01 (M11)',
   exit='per item as its home states; CP-T09-02, -03, -04 and -08 count their chain teeth only on an observed army.arrived or rung.seized after a computed act on a term-(c) target, seeds 0-2 -> as stated',
   hash='M (movers: IN-30 + CP-T09-04 (re-records test_faction_q.py and test_march.py pins); CP-T09-05; CP-T09-02; CP-T09-03; CP-T09-07; CR-09; CP-T09-08; CP-T09-06; CP-T09-01 and CP-T09-09 bodies if built)',
   shared='engine/season/offices.yaml; engine/season/harness/populated.py; references/npc_registry.yaml; engine/season/verb_table.yaml (declare, recruit, conspire, dispatch); engine/season/loop/sides.py; engine/season/loop/effects_shared.py (occupying_faction); engine/season/queries/world_q.py (seat_people_at, own_purview, opinion_of, uncontrolled caller); engine/season/state/gate.py (may_muster oblige clause); modules/social_contest/roll.py (obstacle terms)',
   build='2026-10-24-v10-09-build-B10-17.md'),
 'B10-18': dict(name='WORLD, TRAVEL, SURVIVAL AND NPC LIFE (T10)', lanes='WR, IN', code=True,
   gate='merged: B10-02, B10-04, B10-05, B10-06, B10-09, B10-17; held positions: CP-T10-04 (M11, M6); CP-T10-05 (M11, M6); CR-08 (M6)',
   exit='per item as its home states -> as stated; CP-T10-03 EQUAL at want 1.0',
   hash='M (movers: CP-T10-06; CP-T10-07 (a new hashed collection); CP-T10-09; CP-T10-08; CP-T10-01 (travel_leg schema); CP-T10-02; CP-T10-04 and CP-T10-05 (when released))',
   shared='engine/season/state/world.py (World.estates, remove_person); engine/season/loop/census.py; engine/season/data/fixtures.py; engine/season/data/geography.py; engine/season/queries/world_q.py (_larder_parts want; heir_of; estates_named); engine/season/queries/person_q.py (_bond); modules/mass_battle/terrain.py (terrain_type_at); references/module_contracts.yaml (route query role); engine/season/verb_table.yaml (release domain; marry); engine/season/loop/effects_migration.py (_relocate)',
   build='2026-10-24-v10-09-build-B10-18.md'),
 'B10-19': dict(name='DESIGN-FIRST CLUSTERS (NARRATION, CHARACTER, TROOP, EVENT DECK)', lanes='IN, WR, MB', code=False,
   gate='no batch; the questions below; holds (whole batch): M2, M3, M12, M16, narration decisions 1-4 (-05)',
   exit='the question answered, then the cluster own position list is slotted into the next unopened batch by R8 -> no code until then',
   hash='E',
   shared='proposals/ (design files only)',
   build='2026-10-24-v10-09-build-B10-19.md'),
 'B10-Z': dict(name='HELD AND LEAVE', lanes='all', code=False,
   gate='no batch; the questions below; holds (whole batch): M13, M2, M11, M15, SM-15 timing',
   exit='per entry: B10-Z <item> RULED <date>: <ruling, verbatim>; slotted to B10-<id> by R8 -> n/a',
   hash='E',
   shared='n/a',
   build='2026-10-24-v10-09-build-B10-Z.md'),
}

CUT = "cut (`-07` section 2)"

# handle -> batch (order inside a batch is ORDER below)
REM = {
 "REM-01": "B10-01", "REM-02": "B10-01", "REM-03": "B10-01", "REM-04": "B10-01", "REM-05": "B10-01",
 "REM-06": "B10-01", "REM-08": "B10-01", "REM-09": "B10-01",
 "REM-10": "B10-02", "REM-11": "B10-02", "REM-12": "B10-02", "REM-13": "B10-02", "REM-14": "B10-02",
 "REM-15": "B10-02", "REM-16": "B10-02",
 "REM-42": "B10-03", "REM-45": "B10-03", "REM-46": "B10-03", "REM-47": "B10-03",
 "REM-50": "B10-04", "REM-51": CUT, "REM-52": "B10-04",
 "REM-21": "B10-05", "REM-22": "B10-05", "REM-23": "B10-05", "REM-24": "B10-05", "REM-25": "B10-05", "REM-2C": "B10-05",
 "REM-26": "B10-06", "REM-27": "B10-06", "REM-28": "B10-06", "REM-29": "B10-06", "REM-2A": "B10-06", "REM-2B": "B10-06",
 "REM-40": CUT, "REM-41": CUT, "REM-44": "B10-07",
 "REM-30": "B10-10", "REM-31": "B10-10", "REM-32": "B10-10",
}
CP = {}
for n in range(1, 7): CP[f"CP-T01-{n:02d}"] = "B10-08"
for n in range(1, 9): CP[f"CP-T02-{n:02d}"] = "B10-09"
CP["CP-T03-00"] = "B10-09"
for n in range(1, 12): CP[f"CP-T03-{n:02d}"] = "B10-11"
for n in range(1, 11): CP[f"CP-T04-{n:02d}"] = "B10-12"
for n in range(1, 6): CP[f"CP-T05-{n:02d}"] = "B10-13"
CP["CP-T05-04"] = "B10-05"
CP["CP-T05-05"] = CUT
for n in range(1, 10): CP[f"CP-T06-{n:02d}"] = "B10-14"
CP["CP-T06-06"] = CUT
for n in range(1, 12): CP[f"CP-T07-{n:02d}"] = "B10-15"
CP["CP-T07-01"] = CUT
for n in range(1, 11): CP[f"CP-T08-{n:02d}"] = "B10-16"
for n in range(1, 10): CP[f"CP-T09-{n:02d}"] = "B10-17"
for n in range(1, 10): CP[f"CP-T10-{n:02d}"] = "B10-18"
CP["CP-T02-06"] = "B10-10"
CP["CP-T02-04"] = CUT
CP["CP-T02-08"] = CUT

# v9-origin positions still open (kept under their v9 handle) and the new CR positions
V9 = {
 "IN-12": "B10-09", "IN-14": "B10-16", "IN-18": "B10-02", "IN-30": "B10-17", "IN-32": "B10-15",
 "IN-36": "B10-17", "IN-44": "B10-Z", "IN-45": "B10-16", "IN-48": "B10-17", "IN-52": "B10-16",
 "IN-58": "B10-09", "IN-61": "B10-09", "SC-02": "B10-13", "SC-04": "B10-13", "SC-05": "B10-Z",
 "SC-06": "B10-01", "SC-07": "B10-Z", "SE-04": "B10-16", "SE-06": "B10-16", "MB-07r": "B10-12",
 "MB-08": "B10-Z", "PC-05": "B10-Z", "PC-06": "B10-Z", "PC-08": "B10-Z", "PC-10": "B10-11",
 "WR-01": "B10-15", "GO-01": "B10-Z", "GO-05": "B10-Z", "GO-06": "B10-Z", "FA-01": "B10-17",
 "FA-03": "B10-Z", "FA-07": "B10-Z",
}
# v9 handles that v10 treats as another handle (alias) or as finished (stale index row)
ALIAS = {"IN-09": "REM-2B", "IN-33": "REM-2B", "IN-46": "REM-31", "IN-47": "REM-30", "SE-05": "IN-30",
         "FA-02": "IN-30", "FI-05": "IN-32"}
STALE = {"SC-03b": "landed d855576b (B-O); listed open in v9's state index", "SC-08": "landed 59ca2055 (B-O); listed open in v9's state index",
         "IN-38": "landed 1dcfce10 (B-V); the row stays open in v9 as 'narrowed' with no remaining work named"}
CR = {
 "CR-01": ("B10-02", "The 1-ULP drift in `test_combat_lever_sign_safety` (`bear_spear` `bind_sigma`): isolate the operation, then make the pin platform-independent or key it"),
 "CR-02": ("B10-01", "Correct the record: v9's stale state-index rows, `HANDOFF_IN.md`'s stale H-188 line, `CURRENT.md`'s stamp, `CLAUDE.md` §5's missing `dice_engine` path"),
 "CR-03": ("B10-09", "Acquaintance: half of the persons know no one for four seasons; measure how the known set forms and what build-time source is lawful"),
 "CR-04": ("B10-02", "Horizon: run the soak and the census at 12 and 24 seasons; ledger saturation, decay balance, told-claim rate"),
 "CR-05": ("B10-02", "The 35 `skip`/`xfail` markers: read each reason, record whether its condition still holds"),
 "CR-06": ("B10-03", "The gate sees an effect body that changes a tenure by itself (H-137)"),
 "CR-07": ("B10-05", "Retire the stored `scale:` column (H-89; A1-46)"),
 "CR-08": ("B10-18", "`(Person, weight)` has a matrix row and no writer (H-49); held on M6"),
 "CR-09": ("B10-17", "`own_purview` and the oblige clause agree (H-101)"),
 "CR-10": ("B10-09", "The own-act screen spares tier-1 echoes, arm D2 (IN-57; A1-05)"),
 "CR-11": ("B10-09", "A computed `establish`: where the office it founds is described (design-first; H-94 residue, H-132, H-144, H-156)"),
 "CR-12": ("B10-12", "Melee attrition back to the locked linear law (ED-MB-0045): measure, then design-first"),
 "CR-13": ("B10-15", "The Leap is not charged for failing (C-TW-3); the depth gate gets its reader (ED-WR-0005)"),
}
NM = {f"NM-W{n}": "B10-19" for n in range(10)}
NM["NM-W0"] = "B10-02"
NM["NM-W3"] = "B10-01"
CL = {"CL-CHAR": "B10-19", "CL-ATTR": "B10-19", "CL-TROOP": "B10-19", "CL-EVENTS": "B10-19"}

# In-batch order of the final cut ('->' is serial; 'held:' members wait on the question named and slot in by rule R8)
ORDER = {
 'B10-01': 'REM-01 -> REM-02 -> REM-03 -> REM-04 -> REM-05 -> REM-06 -> REM-08 -> REM-09 -> NM-W3 -> SC-06 -> CR-02',
 'B10-02': 'REM-10 -> REM-11 -> REM-13 -> REM-14 -> REM-12 -> REM-15 -> CR-05 -> CR-04 -> REM-16 -> NM-W0 -> CR-01 -> IN-18',
 'B10-03': 'REM-42 -> REM-45 -> REM-46 -> REM-47 -> CR-06; held: DEF-9 (M11)',
 'B10-04': 'REM-50; held: REM-52 (M6)',
 'B10-05': 'REM-21 -> REM-22 -> REM-23 -> CP-T05-04 -> REM-24 -> REM-25 -> REM-2C -> CR-07',
 'B10-06': 'REM-26 -> REM-27 -> REM-28 -> REM-29 -> REM-2A -> REM-2B',
 'B10-07': 'held: REM-44 (M11)',
 'B10-08': 'CP-T01-03 -> CP-T01-04 -> CP-T01-06 -> CP-T01-05 -> CP-T01-01 -> CP-T01-02',
 'B10-09': 'CP-T02-01 -> CP-T02-02 -> CP-T03-00 -> CP-T02-03 -> CP-T02-05 -> CP-T02-07 -> IN-12 -> IN-61 -> IN-58 -> CR-03 -> CR-10 -> CR-11',
 'B10-10': 'REM-31 -> REM-30 -> REM-32; held: CP-T02-06 (M7)',
 'B10-11': 'CP-T03-01 -> CP-T03-02 -> CP-T03-05 -> CP-T03-09 -> PC-10; held: CP-T03-07 (M6), CP-T03-08 (M6), CP-T03-03 (M2), CP-T03-04 (M2), CP-T03-06 (M1), CP-T03-10, CP-T03-11',
 'B10-12': 'CP-T04-01 -> CP-T04-05 -> CP-T04-02 -> CP-T04-03 -> CP-T04-08 -> CP-T04-06 -> CP-T04-07 -> MB-07r -> CR-12; held: CP-T04-04 (M4), CP-T04-10 (M3), CP-T04-09 (M1)',
 'B10-13': 'SC-02 -> CP-T05-01 -> CP-T05-02 -> CP-T05-03 -> SC-04',
 'B10-14': 'CP-T06-09 -> CP-T06-01 -> CP-T06-03 -> CP-T06-04 -> CP-T06-02 -> CP-T06-07 -> CP-T06-05; held: CP-T06-08',
 'B10-15': 'CR-13 -> CP-T07-02 -> CP-T07-03 -> CP-T07-05 -> CP-T07-09 -> CP-T07-04 -> CP-T07-06 -> CP-T07-07 -> CP-T07-10 -> CP-T07-08 -> CP-T07-11 -> IN-32; held: WR-01 (M2)',
 'B10-16': 'CP-T08-01 -> CP-T08-03 -> CP-T08-02 -> CP-T08-05 -> CP-T08-06 -> CP-T08-08 -> IN-14 -> CP-T08-10; held: CP-T08-07 (M17), CP-T08-04 (M5), IN-45 (M5), IN-52 (M17, M3), SE-04 (M1, M11), SE-06 (M1), CP-T08-09',
 'B10-17': 'IN-30 -> CP-T09-04 -> CP-T09-01 -> CP-T09-05 -> CP-T09-02 -> CP-T09-03 -> CP-T09-07 -> CR-09 -> CP-T09-08 -> CP-T09-09 -> CP-T09-06 -> IN-48; held: IN-36 (M1), FA-01 (M11)',
 'B10-18': 'CP-T10-06 -> CP-T10-07 -> CP-T10-09 -> CP-T10-08 -> CP-T10-01 -> CP-T10-02 -> CP-T10-03; held: CP-T10-04 (M11, M6), CP-T10-05 (M11, M6), CR-08 (M6)',
 'B10-19': 'held: NM-W1, NM-W2, NM-W4, NM-W5 (M12), NM-W6, NM-W7, NM-W8, NM-W9, CL-CHAR (M2), CL-ATTR (M2), CL-TROOP (M3), CL-EVENTS (M16)',
 'B10-Z': 'held: FA-03, FA-07, GO-01 (M13, M2), GO-05 (M13), GO-06, MB-08, PC-05 (M13), PC-06, PC-08, IN-44 (M11, M15), SC-05, SC-07',
}

# Remediation DEF rows that the plan itself says are work, not deferrals (rev. 4: D-1 ruled yes)
DEF = {"DEF-9": ("B10-03", "Delete `engine/engine_params/params_tables.yaml` with a `FORK:` row and `CLAUDE.md` §5's sentence (NERS X3; L0-1); pairs with D-1 (M11)")}
