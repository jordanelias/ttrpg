"""The v10 batch map: which position belongs to which batch, and each batch's card.

STATE AFTER THE DEPENDENCY SEQUENCE (`2026-10-24-v10-09-build-00-sequence.md`): the batch assignments, ORDER and CARDS below follow the final cut in `-03` (NM-W3 and SC-06 moved to B10-01, NM-W0 to B10-02; CP-T02-06 is in B10-10 since the NERS fold; CL-EVENTS was added by it), and after the review round (REM-45 moved from B10-03 to B10-Z, held on M18; CP-T05-04 after REM-25 in B10-05; B10-09 cut in two closes; SC-02 design-first; CP-T10-08 last in B10-18), and after the fold of PR #506 (CR-14 and CR-15 added to B10-02, CR-14 after REM-11 in lane 1 and CR-15 after REM-15 in lane 2, REM-16 needing both; CL-THRUST added to B10-19; the questions are M1 to M21), and after the decision round: 24 new positions (CR-16 to CR-29; GO-07 to GO-16 in the new GO dict), three new batches (the sub-batches B10-03b and B10-07b and the port gate B10-20, after B10-18 and before B10-19), REM-52 to B10-05, REM-45 to B10-15, IN-45 to B10-06, SE-06 to B10-07b, GO-01, GO-05 and GO-06 to B10-20, PC-05 to B10-03, NM-W2 to B10-05, CL-CHAR to B10-10, CL-EVENTS to B10-18; 208 positions in 23 batches. B10-01 then CLOSED (its ten rows and card left `-03` at its net-deleting close, P3): it left SPINE, CARDS and ORDER, and its twelve handles (the ten, NM-W3 and SC-06) map to CLOSED; 196 positions in 22 open batches. Then the second decision round (Jordan's six items of 2026-10-26): 15 new positions (CR-41 to CR-44 to B10-08; CR-30 and CR-33 to B10-10; CR-34 and CR-31 to B10-13; CR-40 to B10-16; CR-32, CR-35, CR-36, CR-37 to B10-17, which is cut in two closes at batch open; CR-38 to B10-19; CR-39 to B10-Z); CL-EVENTS gains commits (3) and (4) in B10-18; 211 positions in 22 open batches. A "landing" in ORDER is a commit of a row that lives in another batch, not a member. The cut handles REM-40, REM-41, REM-51, CP-T02-04, CP-T02-08, CP-T05-05, CP-T06-06 and CP-T07-01 are kept as keys, mapped to CUT, so the coverage run still knows them; their dispositions are in `-07` section 2. The plan files are the record: where this file and `-03` differ, `-03` wins.

This file is the author's judgment in one place; it is not a plan."""

# Closed batches leave SPINE, CARDS and ORDER at their net-deleting close (P3); their handles stay as keys, mapped
# to CLOSED, so the coverage run still knows them (`-07` section 1 keeps every handle and records the batch CLOSED).
CLOSED_BATCHES = ["B10-01"]
CLOSED = "closed: B10-01 (`-07` section 1)"

SPINE = ["B10-02", "B10-03", "B10-03b", "B10-04", "B10-05", "B10-06", "B10-07", "B10-07b",
         "B10-08", "B10-09", "B10-10", "B10-11", "B10-12", "B10-13", "B10-14", "B10-15", "B10-16",
         "B10-17", "B10-18", "B10-20", "B10-19", "B10-Z"]

CARDS = {
 'B10-02': dict(name='INSTRUMENTS THAT CAN SEE THE FAILURES', lanes='IN', code=True,
   gate='merged: B10-01',
   exit='after REM-16 and before CR-01/IN-18: World.content_hash() at build_realm(0) and after aperture 1 s (s=0,1,2) against the base commit; python -m engine.season.harness.report && python -m engine.season.harness.delta <base sha> -> hashes EQUAL; PROBE FLIPS 0; the three-seed baselines for B10-05 and B10-06 recorded in the close commit body; CR-14 reproduces the register P1, P2, P4 and P10 at seeds 0-4 and its shipped arms arm is byte-identical; CR-15 default storybar reading unchanged byte-for-byte and its executed_only reading reproduces P7; CL-THRUST B0.1 hash EQUAL at empty data with TL section 8 falsifier and instrument; git status --short clean after every harness run',
   hash='mixed (movers: CR-01 (test-file pins only); IN-18 (only if G5 builds))',
   shared='engine/season/harness/corpus_run.py (attribute, run_case); engine/season/harness/aperture.py (REM-11, CR-14); engine/season/harness/arms.py (CR-14); engine/season/harness/decision_spread.py; engine/season/harness/storybar.py and harness/chronicle.py (CR-15); the other readers of resolved REM-10 decides under -08 HR-8 (harness/populated.py run, harness/soak.py, harness/scarce.py); engine/season/loop/predicates.py (TRACE lines only); engine/season/requirements.yaml (measured: paragraphs); modules/combat/ and tests/valoria/test_combat_lever_sign_safety.py (CR-01); engine/season/loop/witness.py (IN-18, only if G5 builds); CL-THRUST B0.1 harness module',
   build='2026-10-24-v10-09-build-B10-02.md'),
 'B10-03': dict(name='CONFORMANCE A: NO-HASH DELETIONS AND CORRECTIONS', lanes='IN', code=True,
   gate='merged: B10-02; M11 answered (a), ED-IN-0300: DEF-9 and GO-14 build in the batch, each with its CLAUDE.md hunk (the L0-1 hunk for DEF-9; H-L0-5 for GO-14, after the tree is deleted)',
   exit='per item (home); build_realm(0) hash against the base commit; pathres.load_alias_map() for each deleted path; pytest tests/valoria once at close; GO-14: git ls-files godot/skeleton | wc -l and python tools/export_composition.py --check -> hash EQUAL; an exact-file FORK row per deleted path (skeleton paths included); suite green; 0; OK; ED-PC-0013 superseding row',
   hash='E',
   shared='engine/dice_engine/sigma_leverage.py; engine/season/loop/resolve.py and engine/season/state/world.py (CR-06); engine/season/runs/ (untrack) and engine/season/tests/test_season_shape.py (the two test_w15 tests); tools/evacuation_plan.py and tests/valoria/test_engine_params_bridge.py; references/restructure_ledger.md (FORK rows); engine/engine_params/params_tables.yaml and CLAUDE.md 5 (DEF-9, held); godot/skeleton/; references/module_contracts.yaml (combat, golden_path:); registers/editorial_ledger_pc.jsonl',
   build='2026-10-24-v10-09-build-B10-03.md'),
 'B10-03b': dict(name='THE PORTABLE DIGEST', lanes='GO, IN', code=True,
   gate='merged: B10-03, B10-04 (a declared-mover sub-batch after B10-03 closes, because B10-03 is EQUAL)',
   exit="GO-07's falsifier and controls; the commit body lists every hash pin and every baseline B10-02's close recorded, old to new",
   hash='M (digest format only)',
   shared='engine/season/state/world.py (_entity_digest, content_hash, the log fold); every committed hash pin and golden digest',
   build='2026-10-24-v10-09-build-B10-03b.md'),
 'B10-04': dict(name='HUNGER', lanes='SE, IN', code=True,
   gate='merged: B10-02',
   exit='python -m pytest engine/season/tests/test_hunger.py -q; census hunger_by_settlement on build_realm(0) and on harness/scarce.build -> bands move as the falsifier states; a scarce world reads below fed; build_realm(0) hash EQUAL',
   hash='E',
   shared='engine/season/queries/world_q.py (hunger); engine/season/harness/populated.py (census); engine/season/data/fixtures.py (hunger_band_floors); engine/season/hole_register.yaml (one NUMBER row); engine/season/tests/test_hunger.py (new)',
   build='2026-10-24-v10-09-build-B10-04.md'),
 'B10-05': dict(name='FORMATION: ACTS FORM ONLY ON WHAT THEY CAN REACH', lanes='IN', code=True,
   gate="merged: B10-02, B10-04, B10-03b; layer-conformance Lens B has answered TL :462-467's two Layer 1 questions before the CL-THRUST B2.x and B3.1 landings",
   exit="PYTHONHASHSEED=0 python -m engine.season.harness.aperture 1 s (s=0,1,2) per item; register --requirements; CR-14 pooled census and wrong-kind column over seeds 0-4 (-08 HR-9; the per-item base stays aperture 1 s, s=0,1,2); CR-28's falsifier; REM-52's re-pins (grep -rn body_step engine/season/tests: test_governance_build.py, test_in22_shortfall_reach.py, test_territorial_subsistence.py, test_se03_body_bands.py, test_season_shape.py, every seeded realm hash pin); CL-EVENTS (1) at (); B2.x and B3.1 at empty data; NM-W2's row deleted with HR-9 control (4)'s reading quoted -> each classed verb exists:<Kind>=0 refusals fall to 0 (base 3,137 over three seeds, a lower bound); the wrong-kind-at-admission share per act falls (base 4,620 of 16,116, 28.7%, four seasons; 2,385 of 7,402, 32.2%, two); controls: pooled per-verb EXECUTED within P1 seed-to-seed range, questions delivered / claims deposited / scenes do not fall, every removed candidate force-admitted refuses on its kind; CL-EVENTS (1), B2.x and B3.1 EQUAL; no claim that R-05 moves",
   hash='mixed (movers: REM-22; REM-23; CR-28; REM-24; REM-25; CP-T05-04; REM-2C; REM-52 (its own declared-mover commit, body_step = 10))',
   shared='engine/season/verb_table.yaml; engine/season/rosters.yaml (referent_classes; thrust_axes); engine/season/queries/world_q.py (questions_for splice, own_referents_of_class, the CR-28 stamper term); engine/season/data/verbs.py (DECLARED_CLASSES; VerbRow.scale removal); engine/season/decision/options.py; count pins: engine/season/tests/test_governance_build.py, test_season_shape.py (len(VERB_TABLE) == 56; executed and always-refused sets); engine/season/tests/test_referent_class_stamps.py (new); engine/season/data/fixtures.py (body_step); engine/season/loop/matter.py; engine/season/queries/inputs.py (ProduceInput.factor); modules/settlements/produce.py; engine/season/goals.yaml; engine/season/data/goals.py; the five body_step test files',
   build='2026-10-24-v10-09-build-B10-05.md'),
 'B10-06': dict(name='REACH, SCARCITY AND RESTORES', lanes='IN', code=True,
   gate='merged: B10-02, B10-05',
   exit="aperture 1 s per item; at close the R-01/R-02 re-take: proposals/2026-09-04-degree-sweep wd_chunk.py x (3 arms x 3 fixture points x 4 slices) then wd_collect.py; then corpus_run -> reconvergence below 96% at 2x3 with none >= default; march reaches a field (field.won/lost/unopposed at aperture 1 s, field.unopposed printed beside field.won + field.lost) or the failed link is named (the residue list gains 'defended'); confer and oblige read before and after REM-2B; CR-23's falsifier, its control (stock_report = off reproduces the base hash) and requisition formation at seasons 5-8, seeds 0-2, at crossing and at season; IN-45's falsifier and R-05's found/build/work lines (aperture 4 0, seeds 0-2)",
   hash='mixed (movers: REM-27; CR-23; REM-29; REM-2B; IN-45 (build_realm and realm pins only); REM-26 and REM-28 only where a row is classed)',
   shared="engine/season/verb_table.yaml; engine/season/rosters.yaml; engine/season/loop/effects_*.py; engine/season/loop/sides.py (REM-27); engine/season/data/requires.py (REM-29 room stem); engine/season/queries/world_q.py (fields_named, has_room; requisitionable, larders_in_purview, works_sites); modules/mass_battle/ (read only); engine/season/loop/matter.py and data/fixtures.py (stock_report) (CR-23); engine/season/venues.yaml (planned_works:) and harness/populated.py (build_realm's reader) (IN-45); one HR row",
   build='2026-10-24-v10-09-build-B10-06.md'),
 'B10-07': dict(name="CONFORMANCE B: THE CHOOSER'S DEAD SENSATION", lanes='IN', code=True,
   gate="merged: B10-06; holds: nothing (M11 answered (a), ED-IN-0300); REM-44 lands with L1-6 and L1-7; B10-07b follows as its own batch",
   exit='rg -n subsistence engine/season/{decision,state/carriers.py,loop/deliberate.py,loop/driver.py}; realm 2-season hash at seeds 0-2 before and after -> only comments recording the deletion; hash equal or re-pinned old to new with the count of saved re-deliberations',
   hash='M (movers: REM-44 (declared candidate: the fingerprint skip))',
   shared='engine/season/decision/choose.py, decision/__init__.py; engine/season/loop/deliberate.py; engine/season/loop/driver.py; engine/season/state/carriers.py (Sensation); every harness caller of SeasonDriver.season; architecture/meta/04_CODE_ARCHITECTURE.md B.10, C.3 and architecture/meta/01_AXIOMS.md D.10 (L1-6, L1-7)',
   build='2026-10-24-v10-09-build-B10-07.md'),
 'B10-07b': dict(name="THE CHOOSER'S DIALS AND CELLS", lanes='IN, SE', code=True,
   gate='merged: B10-06, B10-07',
   exit="SE-06's source reading (and decision_spread --persons if it builds); CR-21's and CR-16's falsifiers and controls; at close corpus_run's RANKING line and decision_spread --decisions read for zero-score ties (R-08) and conviction_spread re-read (R-06) -> no threshold claimed",
   hash='M (movers: SE-06 (if built); CR-21 commit 1; CR-16 commit 2)',
   shared="engine/season/cohorts.yaml; engine/season/harness/populated.py (seat_cohorts); engine/season/rosters.yaml (cells, pursuit_axes); engine/season/decision/options.py (subject_is_opponent, refuses); engine/season/data/fixtures.py (stance_polarity); references/restructure_ledger.md (the drafts' FORK rows); the five provenance-comment files; HR rows H-54, H-146, H-194, H-202, H-205",
   build='2026-10-24-v10-09-build-B10-07b.md'),
 'B10-08': dict(name='DICE: ONE FACULTY, ONE ODDS FUNCTION, ONE CEILING', lanes='IN', code=True,
   gate='merged: B10-02, B10-03, B10-06, B10-07b',
   exit="each item falsifier and paired-seed control as its home states; band_odds(2, 2) == (0.74, 0.19, 0.07, 0.0) and the 200,000-roll arm; H-213 re-measure; CR-18's falsifier and the pools line (aperture 4 0, seed 0); the editorial pass: CR-41's and CR-42's greps and controls, CR-43's falsifier, python tools/export_names.py --check, python tools/definitions_store.py --check, python tools/vocab_store.py --check, python -m pytest tests/valoria/test_vector_audit.py -q, CR-44's new loader test and its corpus control (load_cases counted at build, equal before and after) -> as the homes state; the shipped practice arm byte-equal at practice_cap = 0 stays the control",
   hash='mixed (movers: CP-T01-04 (corpus draws at Ob 1.5); CP-T01-06 (every seed where a hostile term or a forged Record is met); CR-18 (commit 1, every seeded realm hash); CR-41, CR-42, CR-43 and CR-44 EQUAL)',
   shared='engine/season/seam/wrappers/sigma.py; engine/season/seam/ladder.py; engine/dice_engine/sigma_leverage.py (band_odds, settle_margin); modules/social_contest/roll.py (obstacle); engine/season/rosters.yaml (and the office_bodies note, CR-41); engine/season/loop/resolve.py (_contest); engine/season/loop/deliberate.py and state/carriers.py (CP-T01-05 slot, if built); engine/season/data/fixtures.py; engine/season/harness/aperture.py (CR-18 pools line); the editorial pass (CR-41 to CR-44): references/names_index.yaml; references/definitions/vocab_source.yaml; engine/engine_params/names.json (re-derived); references/definitions/definitions.yaml and references/alias_registry.yaml (re-derived); tests/valoria/test_vector_audit.py; references/ci_checks_registry.yaml; references/lane_assignments.yaml; engine/engine_params/params_tables.yaml (one comment); engine/season/harness/populated.py; engine/season/harness/invariants.py; engine/season/harness/run_cases.py; engine/season/tests/test_season_shape.py',
   build='2026-10-24-v10-09-build-B10-08.md'),
 'B10-09': dict(name='PERSONS: DEATH NAMES SEATS, THE KNOWN, THE SUCCESSOR', lanes='IN, SC, SE, WR', code=True,
   gate='merged: B10-05, B10-07b, B10-08',
   exit="two closes, decided at batch open (close one ends at IN-61; close two runs IN-58, CR-03, CR-10, CR-11, CR-25, CR-17; ctl/ and -01 deleted only at close two); each item falsifier and control as its home states; corpus_run over three seeds for CR-10; IN-61's import check (a FILLED_BY missing a conferral basis and a basis missing from REVOCATION_DISPOSAL refused) and its one-act claim falsifier (two vacant seats keyed on the heir's title: one succeed opens both and closes the title); CR-26's pass and planted arm; IN-12's python -m pytest engine/season/tests -q -k test_u2_; CR-25's R-04 line (aperture 4 s, s=0-2, establish ex >= 1 with Act.via a confer-granting seat); CR-17's falsifier and tau line -> as the homes state; the test_arrangements.py hold-disposing tripwire is re-recorded at CR-35 (B10-17), not here",
   hash='M (movers: CP-T02-01; CP-T02-02 (every pin naming off_npc_* re-records); CP-T03-00 (size measured at the commit, seeds 0-2, two seasons); CP-T02-03; CP-T02-05; IN-61; CR-10; CR-25; CR-17; IN-12 EQUAL in the realm (claimed); CR-26 and the CL-THRUST B3.2 landing EQUAL)',
   shared='engine/season/state/world.py; engine/season/loop/census.py; engine/season/offices.yaml; engine/season/decision/options.py; engine/season/data/verbs.py; engine/season/queries/person_q.py; engine/season/queries/world_q.py; engine/season/rosters.yaml; engine/season/decision/questions.py; engine/season/state/carriers.py; engine/season/seam/ladder.py and loop/effects_combat.py (CP-T03-00); engine/season/harness/play_surface.py; engine/season/state/gate.py (IN-61, IN-12); engine/season/loop/predicates.py; engine/season/loop/driver.py; engine/season/data/fixtures.py (odds_weighting, choice_temperature); engine/season/verb_table.yaml (interrogate, establish); engine/season/tests/test_in61_heir_hears_vacancy.py (new)',
   build='2026-10-24-v10-09-build-B10-09.md'),
 'B10-10': dict(name='SCALE BUILDS (D-2: THE DESIGNS STAY HELD)', lanes='IN, PC, MB', code=True,
   gate='merged: B10-09',
   exit="REM-31: AUTOMATED and PLAYABLE-with-scripted-choices-equal-to-the-chooser at one content_hash, a differing choice moves it, the permutation falsifier with the callback on; REM-30: a creation arm switched off reproduces the pre-build hash; REM-32: a real fold reaches Won at a fixture above 1; CR-20's and CR-19's falsifiers; CR-30's falsifier and control (tools/export_descriptors.py --check OK; the combined Person repr re-pin, old to new); CR-33's falsifier, control and train reading (aperture 4 0); CL-CHAR's row deleted on CR-20's exit, its piece check reading CR-33 as well; CP-T02-06's roster -> as stated; REM-32 EQUAL at k = 1",
   hash="M (movers: REM-31 (every seeded season that fights); REM-30 (where its creation arm is on); CR-20 (schema: Person's repr) with CR-30 in one combined re-pin; CR-33 (where a cast row carries a lifepath); CR-19 (where a value exists); CP-T01-05's NPC half (if built))",
   shared='engine/season/loop/driver.py; engine/season/loop/deliberate.py (REM-31 callback); engine/season/seam/wrappers/combat.py; modules/combat/wrapper.py, modules/combat/fight.py; modules/mass_battle/massbattle.py (REM-32); engine/season/state/carriers.py and decision/ (REM-30); engine/season/harness/play_surface.py (CP-T02-06); the seeded goldens; engine/season/state/carriers.py (Person.attributes; Person.heritage); engine/season/seam/wrappers/sigma.py (faculty); engine/season/rosters.yaml (vocation_attribute; lifepath_templates; the observation_terms note); engine/season/data/cast.py (heritage_of; the lifepath: expansion); engine/season/decision/options.py (refracted_confidence); references/descriptor_registry.yaml (heritage_roster, IN FLUX); engine/engine_params/descriptors.json (re-derived); engine/substrate/descriptors.py; engine/season/epistemic.py (_term_marks); engine/season/harness/populated.py cohort_rows (only if a cohort row authors a heritage)',
   build='2026-10-24-v10-09-build-B10-10.md'),
 'B10-11': dict(name='PERSONAL COMBAT (T03)', lanes='PC', code=True,
   gate='merged: B10-08, B10-09, B10-10; held positions: CP-T03-10 (parked/cut/withdrawn/leave); CP-T03-11 (parked/cut/withdrawn/leave)',
   exit="per item as its home states; aperture 1 s per verb added; PC-10's accept/challenge lines; CR-14's death census (accept deaths without a held challenge, pooled seeds 0-4); the interrogate re-read (aperture 4 0, interrogate attempted) -> as stated; 0; > 0",
   hash='M (movers: CP-T03-01 (stem + cohort bound); CP-T03-02; CP-T03-09; PC-10 (wherever a challenge forms); CP-T03-03; CP-T03-04; CP-T03-07 and CP-T03-08 (body_ceiling is a schema mover); CP-T03-06 (when built))',
   shared='modules/combat/; engine/season/seam/wrappers/combat.py; engine/season/loop/effects_combat.py; engine/season/verb_table.yaml; engine/season/data/requires.py (the individual stem; the names: stem); engine/season/rosters.yaml (duel_terms; challenge_terms, record_kinds); engine/season/state/gate.py (CP-T03-09 detain opener); engine/engine_params/pc_matchup.json and tools/export_pc_matchup.py (deleted by CP-T03-05)',
   build='2026-10-24-v10-09-build-B10-11.md'),
 'B10-12': dict(name='MASS BATTLE (T04)', lanes='MB', code=True,
   gate='merged: B10-05, B10-10, B10-11; held positions: CP-T04-04 (M4 Ask C (b)); CP-T04-10 (M3); CP-T04-09 (cut)',
   exit="per item as its home states; each exit reports the fought-field count it was measured on; CR-12: python3 -m systems.mass_battle.sim.lanchester_signature on both per-cell arms before and after; CR-24's falsifier; at CP-T04's close R-04's combat scales: row (i)+(ii) and R-07 conjunct (3) read -> EQUAL at the shipped arms; a mover on each flip, declared",
   hash='mixed (movers: CR-24 (wherever a defended field is fought); MB-07r (golden digests); CP-T04-06 (besiege roster flip, own commit); CR-12 (when built); CP-T04-04 (when M4 Ask C (b) releases it))',
   shared='modules/mass_battle/ (massbattle.py, orchestration.py, config.py); engine/season/loop/encounter.py; engine/season/seam/wrappers/mass_battle.py; engine/season/verb_table.yaml (march; marshal, besiege, surrender rows); engine/season/loop/sides.py (CP-T04-04, held); engine/season/loop/effects_information.py (CP-T04-07); tools/ci_golden_modes_check.py and engine/tests goldens (MB-07r, CR-12); engine/season/loop/effects_combat.py (_eff_march) and data/fixtures.py (field_winner_casualties) (CR-24)',
   build='2026-10-24-v10-09-build-B10-12.md'),
 'B10-13': dict(name='SOCIAL CONTEST AND PROCEEDINGS (T05)', lanes='SC', code=True,
   gate='merged: B10-05, B10-06, B10-08, B10-12',
   exit="per item on its hand-built falsifier worlds (the realm forms about three determine in twelve seed-seasons); tell attempts, news.told and chained-claim counts per season before and after CP-T05-03, seeds 0-2; CR-27's falsifier and its realm reading (reported, not thresholded); R-05 reads lie's execution; CR-34's falsifier and three controls, its realm reach recorded as 0 with the residue and trigger named (aperture 4 0's determine row not used as a control); CR-31's falsifier and control (heritage_gain 0 reproduces CR-30's tree's hash) -> as stated; the chained-claim fall is the price, recorded; one close",
   hash='M (movers: SC-02 (re-source, once its design is approved); CP-T05-01; CP-T05-02; CP-T05-03; CR-27 (lie_offered ships True); CR-31 (at the shipped heritage_gain where a heritage is authored and seen); CR-34 EQUAL in every seeded realm, by construction)',
   shared="engine/season/seam/wrappers/sigma.py (contest_input); engine/season/queries/world_q.py (reception, proofs, hearing; judging_set, CR-34); engine/season/loop/effects_governance.py; engine/season/arrangements.yaml (excommunication_deliberation to disposal: declared, CR-34); engine/season/data/ (rosters.py DEGREE_STEP read; arrangements.py quorum; for CR-34 the file that owns determine's quorum conjunct, located by symbol at the re-base); engine/season/loop/witness.py and data/verbs.py (CP-T05-03 tell.refused kind); engine/season/queries/person_q.py (lie_said_of; heritage_regard, CR-31); engine/season/decision/options.py (opening_set; teller_weight's relation term, CR-31); engine/season/rosters.yaml (lie's cells); engine/season/data/fixtures.py (lie_offered; heritage_gain, CR-31); engine/season/verb_table.yaml (the lie row) and the verb-step pins; HR rows H-161 and the new heritage_gain row",
   build='2026-10-24-v10-09-build-B10-13.md'),
 'B10-14': dict(name='FIELDWORK AND INFORMATION (T06)', lanes='FI', code=True,
   gate='merged: B10-02, B10-05, B10-06, B10-13; held positions: CP-T06-08 (JA-1); CR-29 released from M11 (ED-IN-0300)',
   exit='per item as its home states; test_fi03_trail.py re-recorded and declared; the (kind, place) found-vs-logged count per seed for CP-T06-02; CP-T06-05 without its M9 limit sentence (CR-27 landed at B10-13) -> as stated',
   hash='M (movers: CP-T06-09; CP-T06-01; CP-T06-04; CP-T06-02; CP-T06-07; CP-T06-05; CP-T06-03 wherever a retry forms; CR-29 commit 2 when released)',
   shared='engine/season/loop/witness.py; engine/season/epistemic.py; engine/season/state/attribution.py; engine/season/loop/effects_information.py; engine/season/state/world.py (_on_logged index); engine/season/rosters.yaml (record_kinds cover; covert_kinds); engine/season/data/rosters.py (COVER_KEY, COVER_AS); engine/season/verb_table.yaml (sabotage class; interview retype); engine/season/tests/test_fi03_trail.py (declared re-record)',
   build='2026-10-24-v10-09-build-B10-14.md'),
 'B10-15': dict(name='THREADWORK (T07)', lanes='WR, PC', code=True,
   gate='merged: B10-05, B10-14; held positions: WR-01 (BLK on its own condition)',
   exit="per item as its home states; CR-13: a Leap at Partial and at Failure each net 0 Coherence, Weaving keeps the blanket penalty; REM-45's falsifier and EQUAL control; IN-32's stopping rule (aperture 1 0 tie / knot offered and executed; fanned deliberations with a tie-only partner; tie_known True against False content_hash) -> as stated; CR-13, REM-45 and the shipped () tuple of CP-T07-07 hash EQUAL",
   hash='mixed (movers: CP-T07-02 (schema: Person.coherence); CP-T07-03 (schema: Site.locked); CP-T07-09, -04, -06, -10, -08, -11 per working; IN-32; REM-45 EQUAL)',
   shared='systems/threadwork/sim/operations.py (CR-13, REM-45); engine/season/seam/wrappers/threadwork.py (new host); engine/season/state/carriers.py (Person.coherence; Site.locked); engine/season/write_matrix.yaml; engine/season/rosters.yaml (thread_scales, cells); engine/season/verb_table.yaml (weave, lock, mend, ward, thread_read, tie / knot); engine/season/loop/matter.py (locked-Site yield); engine/season/queries/world_q.py (in_equilibrium, held_load); engine/season/decision/budget.py (coherence_band_floors); engine/season/loop/effects_information.py (_eff_tie); engine/season/decision/options.py (operand_bags); engine/season/data/fixtures.py (tie_known); engine/season/seam/wrappers/sigma.py (the Will addend)',
   build='2026-10-24-v10-09-build-B10-15.md'),
 'B10-16': dict(name='SETTLEMENTS, GOVERNANCE AND ECONOMY (T08)', lanes='SE', code=True,
   gate="merged: B10-04, B10-06, B10-15 (CR-23 and IN-45 landed at B10-06; CR-23 owns H-163 limit 3(a)); held positions: SE-04 part (b) (released from M11, in B10-Z, unscheduled); IN-52's retirement (M3, confirmed at the default); CP-T08-09 (withdrawn)",
   exit="per item as its home states; CP-T08-06's compliance reader, CP-T08-07, CP-T08-08 and IN-52's flip credited in computed play where CR-23's exit recorded requisition executing, otherwise on harness/scarce.governed only, and never as R-04 conjunct (1) (aperture 4 0 is its reader); CR-40's falsifier and control, python -m pytest engine/season/tests/test_mass_battle_module.py tests/valoria/test_mass_battle_terrain.py -q, the freshness-gate diff showing one pin line moved, the identifier census re-derived -> off arms EQUAL; on arms declared; CR-40 EQUAL",
   hash="mixed (movers: IN-14 (budget moves); CP-T08-08 (declared candidate); CP-T08-07's on arm; IN-52's flip (declared); CR-40 EQUAL)",
   shared='modules/settlements/ (produce.py ProduceInput); engine/season/loop/matter.py; engine/season/queries/world_q.py (labour, price_of, unrest); engine/season/queries/person_q.py (stability read); engine/season/data/fixtures.py; engine/season/rosters.yaml; engine/season/decision/budget.py (IN-14, CP-T08-10); engine/season/loop/driver.py (IN-14 rounds); engine/season/loop/effects_economy.py (CP-T08-08 upkeep_due); engine/season/tests/test_season_shape.py (test_n3 floor re-take); systems/settlements/valoria_geography_v30.yaml, references/canonical_sources.yaml (pin, re-derived) and systems/settlements/_identifier_census.yaml (re-derived) (CR-40)',
   build='2026-10-24-v10-09-build-B10-16.md'),
 'B10-17': dict(name='FACTIONS, WAR AND DIPLOMACY (T09)', lanes='FA', code=True,
   gate="merged: B10-05, B10-06, B10-08, B10-09, B10-10 (CR-30), B10-12, B10-13 (CR-34), B10-16; CR-35's gate arm and H-217 clause and CR-37 build in the ordinary way (H-L0-8 and H-L0-9 applied, PR #507); two closes, decided by the batch's first reading at open (close one IN-30 to CP-T09-06; close two CR-32, CR-35, CR-36, CR-37 and IN-48); held positions: IN-36 (M1's residue: H-233; the foreign/guards defaults); FA-01's clause (released from M11; needs CR-29); no position adds a casus-belli conjunct to march (M10 (b))",
   exit="per item as its home states; CP-T09-02, -03, -04 and -08 count their chain teeth only on an observed army.arrived or rung.seized after a computed act on a term-(c) target, seeds 0-2; CP-T09-04's falsifier (5) and readings (rung.seized, uncontrolled_in_realm, endings; seeds 0-2, eight seasons); IN-30's faction_props readings; CP-T09-06's one-claim falsifier; CR-32's, CR-35's, CR-36's and CR-37's falsifiers and controls; CR-35's confer ex re-read on the post-item tree (aperture 4 s, s=0-2) against the pre-item tree; the test_arrangements.py hold-disposing tripwire red and re-recorded at CR-35 -> as stated",
   hash='M (movers: IN-30 + CP-T09-04 (re-records test_faction_q.py and test_march.py pins); CP-T09-05; CP-T09-02; CP-T09-03; CP-T09-07; CR-09; CP-T09-08; CP-T09-06; CP-T09-01 and CP-T09-09 bodies if built; CR-32; CR-35 (when shipped on); CR-36; CR-37 (when built))',
   shared='engine/season/offices.yaml; engine/season/harness/populated.py; references/npc_registry.yaml; engine/season/verb_table.yaml (declare, recruit, conspire, dispatch); engine/season/loop/sides.py; engine/season/loop/effects_shared.py (occupying_faction); engine/season/queries/world_q.py (seat_people_at, own_purview, opinion_of, uncontrolled caller; faction_props; judging_set matter); engine/season/state/gate.py (may_muster oblige clause; the election arm, FILLED_BY, REVOCATION_DISPOSAL, REVOCATION_RULES); modules/social_contest/roll.py (obstacle terms); engine/season/arrangements.yaml (election, succession); engine/season/loop/effects_information.py (_disposal hold literal; _eff_determine Record site); engine/season/loop/predicates.py (_req_confer, _req_revoke); engine/season/rosters.yaml (conferral_bases, revocation_bases, record_kinds, concurring_bodies, factions.creed); engine/season/state/world.py (_grant_remit); engine/season/epistemic.py (_term_marks); engine/season/decision/options.py (rank); engine/season/tests/test_arrangements.py',
   build='2026-10-24-v10-09-build-B10-17.md'),
 'B10-18': dict(name='WORLD, TRAVEL, SURVIVAL AND NPC LIFE (T10)', lanes='WR, IN', code=True,
   gate='merged: B10-02, B10-04, B10-05, B10-06, B10-09, B10-17; CP-T10-04 and CP-T10-05 released from M11 (ED-IN-0300)',
   exit='per item as its home states; CP-T10-03 ships year_length 0, hash EQUAL (year_length 0 or every season_terms multiplier at 1.0 reproduces the base hash), then its flip as a declared mover; CL-EVENTS (2) falsifier (two territories at one tick draw different factors; () reproduces the base hash); CR-08 writer (grep -rn "weight.changed" engine/season finds it); CR-22 exit (the arms read, the season-0 floor rule, the eaters fed from a larder above their own settlement, the strict-top share at CR-17 tau as a reading); CL-EVENTS (3) loader refusals, draw and scale falsifier and its two controls (python -m pytest engine/season/tests/test_tensions.py -q; engine/season/tests/test_season_weather.py); CL-EVENTS (4) falsifier and seeding refusals, and its readings (STORY-BAR on against off; TL B0.1 ARC rate if landed; card 1 fight on the King), recorded, not a pass condition -> as stated; CL-EVENTS (3) and (4) EQUAL',
   hash="M (movers: CP-T10-06; CP-T10-07 (a new hashed collection); CP-T10-09; CP-T10-08; CP-T10-01 (the same-place rule on both arms; the leg tuple on the ON arm); CP-T10-02; CP-T10-03's year_length flip (its own commit); CL-EVENTS (2); CR-08; CR-22; CP-T10-04 and CP-T10-05 (when released); CL-EVENTS (3) and (4) EQUAL, switch off)",
   shared="engine/season/state/world.py (World.estates, remove_person); engine/season/loop/census.py; engine/season/data/fixtures.py; engine/season/data/geography.py; engine/season/queries/world_q.py (_larder_parts want; heir_of; estates_named; season_factor_of); engine/season/queries/person_q.py (_bond); modules/mass_battle/terrain.py (terrain_type_at); references/module_contracts.yaml (route query role); engine/season/verb_table.yaml (release domain; marry); engine/season/loop/effects_migration.py (_relocate); engine/season/rosters.yaml (subsistence_weight; tension_effects); engine/season/write_matrix.yaml; engine/season/loop/matter.py; engine/season/tensions.yaml (new); engine/season/data/tensions.py (new); engine/season/data/files.py (TENSIONS_YAML); engine/season/harness/populated.py (build_realm(tensions=)); engine/season/data/goals.py (read through parse); engine/season/tests/test_tensions.py (new)",
   build='2026-10-24-v10-09-build-B10-18.md'),
 'B10-20': dict(name='THE PORT GATE', lanes='GO, IN', code=True,
   gate="merged: B10-18 (and every batch before it closed); ED-GO-0002 on main (PR #467 merged, or B10-01's fallback); SC-05 slotted or listed in the freeze row; the Layer 0/1 hunks the exit lines read are applied (H-L0-2, H-L0-3) or land with their positions (GO-14's H-L0-5 in B10-03; GO-10's C.12 hunk); listed: GO-06 (HELD, BLK, another repository)",
   exit="(1) game_constants.json engine_series; git grep -nE \"Godot 4\\.6\" -- README.md references/glossary.md CURRENT.md (the CLAUDE.md part: H-L0-2, applied); (2) python tools/export_oracle_pins.py --check; (3) PYTHONHASHSEED=0,1,2 python -m engine.season.harness.port_oracle --slice 1 --seed 0; (4) the seven existing --checks (export_sim_params, export_engine_params, export_game_constants, export_descriptors, export_composition, export_npc_roster, export_names) and export_season_registries --check, export_oracle_draws --check; (5) python tools/m1_acceptance.py --summary; (6) grep -c key-log references/module_contracts.yaml (git ls-files godot/skeleton and the engine_clock doc: null grep wait on the held-back PR); (7) python tools/validate_ed_citations.py; (8) pytest tests/valoria, engine/season/tests, engine/tests once at the close; (9) valoria-game CI (Jordan's side) -> 4.7; nothing; OK with the oracle SHA = git rev-parse HEAD; three identical lines equal to the pin; OK x9; same-seed hash PASS and zero invariant violations PASS; 0; 0 violations and the last ED-GO- row is the freeze row (oracle SHA, pins digest, draw log digest, freeze list with CR-29 on it); CI green on the freeze commit; a 4.7.x build and a parity job replaying oracle_draws.json; the freeze row also lists M16's fourth motion (not needed by CL-EVENTS (3) and (4)), the tensions on-arm flip (build_realm(tensions=)'s default beside IN-36's foreign/guards defaults), CR-35's gate arm and H-217 clause (H-L0-8) and CR-37 (H-L0-9) while the held-back PR is unmerged, FILLED_BY's elected narrowing if it waits on an election executing, CR-38 and CR-39 if CR-38 is unapproved when B10-18 closes (the interim two-seat bench named and frozen), and the answers to -05 section 1a (a), (b), (c) read at the open",
   hash='E',
   shared='tools/export_season_registries.py; tools/export_oracle_pins.py; tools/export_oracle_draws.py; tools/export_game_constants.py and references/engine_series.yaml (GO-01); engine/engine_params/ (season_registries.json, oracle_pins.json, oracle_draws.json, game_constants.json, composition.json); references/module_contracts.yaml (GO-11); engine/season/loop/resolve.py and loop/predicates.py (GO-10); modules/mass_battle/rngsource.py, config.py, hierarchy/units.py (GO-12); engine/season/state/ids.py (GO-16); engine/season/harness/port_oracle.py; CI validators job; registers/editorial_ledger_go.jsonl (the freeze row)',
   build='2026-10-24-v10-09-build-B10-20.md'),
 'B10-19': dict(name='DESIGN-FIRST CLUSTERS (NARRATION, CHARACTER, TROOP, EVENT DECK, THRUST LADDERS)', lanes='IN, WR, MB, SC', code=False,
   gate="no batch; the questions below; CR-38 drafted in a worktree beside B10-13 and approved before B10-18 closes (ED-1094's merge default unless its PR holds it back): approved, its build runs by R8 as its own sub-batch before B10-20 opens; unapproved, it is on B10-20's freeze row as a declared post-freeze mover with the interim two-seat bench named; holds: J-T2 (CL-ATTR), M3 (CL-TROOP), M1's residue (CL-THRUST B5.2); CL-THRUST B4.x on determine and covenant executing, B6.n on content; NM-W5 held on NM-W1 only; no member is held on a narration decision",
   exit='the question answered, then the member own position list is slotted into the next unopened batch by R8; CL-THRUST pieces in TL section 8 order (B0.1 in B10-02, B2.x and B3.1 in B10-05, B3.2 in B10-09), each with its falsifier, control and instrument, hash EQUAL at empty data -> no code until then',
   hash='E',
   shared='proposals/ (design files only)',
   build='2026-10-24-v10-09-build-B10-19.md'),
 'B10-Z': dict(name='HELD AND LEAVE', lanes='all', code=False,
   gate='no batch; the questions below; holds: CR-39 on CR-38; IN-44 rows 2-16 and SE-04 (b) released from M11, unscheduled, slotted by R8 (trigger: CR-38 lands a Court Parliament bench); SC-05 held on nothing Jordan owes (A1-58)',
   exit="per entry: B10-Z <item> RULED <date>: <ruling, verbatim>; slotted to B10-<id> by R8; MB-08's row records the orders residue's trigger -> n/a",
   hash='E',
   shared='n/a',
   build='2026-10-24-v10-09-build-B10-Z.md'),
}

CUT = "cut (`-07` section 2)"

# handle -> batch (order inside a batch is ORDER below)
REM = {
 "REM-01": CLOSED, "REM-02": CLOSED, "REM-03": CLOSED, "REM-04": CLOSED, "REM-05": CLOSED,
 "REM-06": CLOSED, "REM-08": CLOSED, "REM-09": CLOSED,
 "REM-10": "B10-02", "REM-11": "B10-02", "REM-12": "B10-02", "REM-13": "B10-02", "REM-14": "B10-02",
 "REM-15": "B10-02", "REM-16": "B10-02",
 "REM-42": "B10-03", "REM-45": "B10-15", "REM-46": "B10-03", "REM-47": "B10-03",
 "REM-50": "B10-04", "REM-51": CUT, "REM-52": "B10-05",
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
 "IN-36": "B10-17", "IN-44": "B10-Z", "IN-45": "B10-06", "IN-48": "B10-17", "IN-52": "B10-16",
 "IN-58": "B10-09", "IN-61": "B10-09", "SC-02": "B10-13", "SC-04": "B10-13", "SC-05": "B10-Z",
 "SC-06": CLOSED, "SC-07": "B10-Z", "SE-04": "B10-16", "SE-06": "B10-07b", "MB-07r": "B10-12",
 "MB-08": "B10-Z", "PC-05": "B10-03", "PC-06": "B10-Z", "PC-08": "B10-Z", "PC-10": "B10-11",
 "WR-01": "B10-15", "GO-01": "B10-20", "GO-05": "B10-20", "GO-06": "B10-20", "FA-01": "B10-17",
 "FA-03": "B10-Z", "FA-07": "B10-Z",
}
# v9 handles that v10 treats as another handle (alias) or as finished (stale index row)
ALIAS = {"IN-09": "REM-2B", "IN-33": "REM-2B", "IN-46": "REM-31", "IN-47": "REM-30", "SE-05": "IN-30",
         "FA-02": "IN-30", "FI-05": "IN-32"}
STALE = {"SC-03b": "landed d855576b (B-O); listed open in v9's state index", "SC-08": "landed 59ca2055 (B-O); listed open in v9's state index",
         "IN-38": "landed 1dcfce10 (B-V); the row stays open in v9 as 'narrowed' with no remaining work named",
         "GO-03": "landed at B-C (the `godot_conversion_strategy_v1.md:138` heading string removed; `-04` part 2, GO-01's LANDED ALREADY); named once GO-\\d\\d entered the coverage pattern"}
CR = {
 "CR-01": ("B10-02", "The 1-ULP drift in `test_combat_lever_sign_safety` (`bear_spear` `bind_sigma`): isolate the operation, then make the pin platform-independent or key it"),
 "CR-02": (CLOSED, "Correct the record: v9's stale state-index rows, `HANDOFF_IN.md`'s stale H-188 line, `CURRENT.md`'s stamp, `CLAUDE.md` §5's missing `dice_engine` path"),
 "CR-03": ("B10-09", "Acquaintance: half of the persons know no one for four seasons; measure how the known set forms and what build-time source is lawful"),
 "CR-04": ("B10-02", "Horizon: run the soak and the census at 12 and 24 seasons; ledger saturation, decay balance, told-claim rate"),
 "CR-05": ("B10-02", "The 35 `skip`/`xfail` markers: read each reason, record whether its condition still holds"),
 "CR-06": ("B10-03", "The gate sees an effect body that changes a tenure by itself (H-137)"),
 "CR-07": ("B10-05", "Retire the stored `scale:` column (H-89; A1-46)"),
 "CR-08": ("B10-18", "`(Person, weight)` has a matrix row and no writer (H-49): the CENSUS writer, a cohort loses weight when its body floors (M6 taken)"),
 "CR-09": ("B10-17", "`own_purview` and the oblige clause agree (H-101)"),
 "CR-10": ("B10-09", "The own-act screen spares tier-1 echoes, arm D2 (IN-57; A1-05)"),
 "CR-11": ("B10-09", "A computed `establish`: where the office it founds is described (design-first; H-94 residue, H-132, H-144, H-156); its design records CR-25's derivation"),
 "CR-12": ("B10-12", "Melee attrition back to the locked linear law (ED-MB-0045): measure, then design-first"),
 "CR-13": ("B10-15", "The Leap is not charged for failing (C-TW-3); the depth gate gets its reader (ED-WR-0005)"),
 "CR-14": ("B10-02", "The pooled census and the other aperture and arms readings: aperture --seeds with two wrong-kind-at-admission columns, ANSWERED-BY-SOURCE, the death census; arms.run_arm takes fixture or build-kwarg arms (PR #506 G-08, G-11, G-12, G-20, G-29)"),
 "CR-15": ("B10-02", "storybar.read gains an executed_only reading beside the current one; chronicle --executed-only (PR #506 G-27)"),
 "CR-16": ("B10-07b", "The chooser's polarity: the `subject_is_opponent` repair and `stance_polarity: declared` (M1)"),
 "CR-17": ("B10-09", "Believed odds weight the alignment term; tau re-derived as its last commit (M1, AQ-X1 (b))"),
 "CR-18": ("B10-08", "Practice ships live; the pools reader for R-09 (M2; the tenth attribute stays unnamed)"),
 "CR-19": ("B10-10", "AX-7's competence reads Attunement (H-200)"),
 "CR-20": ("B10-10", "The attribute carrier lands with character creation (nine keys; M2; CL-CHAR's and CL-ATTR's build)"),
 "CR-21": ("B10-07b", "The cell-value and cosine pass: four value changes plus `thread_read`'s owed cells (M14)"),
 "CR-22": ("B10-18", "Hunger binds: the per-head need chosen by a reading rule (M6)"),
 "CR-23": ("B10-06", "A larder's stock reaches the seats over it, at its crossings (M17)"),
 "CR-24": ("B10-12", "Winners take their engine casualties (M4 Ask B (b))"),
 "CR-25": ("B10-09", "A computed `establish` founds an office over a holding (CR-11's build; M8's H-132 (b), H-144 (b))"),
 "CR-26": ("B10-09", "The heir hears the vacancy (IN-61 check (4), executed)"),
 "CR-27": ("B10-13", "`lie`: a spoken falsehood on a held cell claim (M9)"),
 "CR-28": ("B10-05", "G-04(a): own-ledger Propositions stamp as class `Proposition` (M19)"),
 "CR-29": ("B10-14", "REACH: the event-kind reach channel, then `chronicle`'s paired deletion (released from M11, ED-IN-0300)"),
 "CR-30": ("B10-10", "`Person.heritage`: descent as a read-off field; the `marks` term gets its carrier"),
 "CR-31": ("B10-13", "The caste estimate: a heritage regard term (`heritage_gain`)"),
 "CR-32": ("B10-17", "Standing ladders as posts on seats; livery in `marks`; `rank` within one scale (H-181)"),
 "CR-33": ("B10-10", "The 34 lifepaths as creation templates (`lifepath:`, `lifepath_templates`)"),
 "CR-34": ("B10-13", "The declared disposal is read: a vote counts live commits (C-7; H-161)"),
 "CR-35": ("B10-17", "An elected seat is filled by its faction's bench; the contested succession (H-217); H-L0-8 applied"),
 "CR-36": ("B10-17", "Nominate-then-confirm: the `nominated` basis and the `resolution` Record"),
 "CR-37": ("B10-17", "The throne revoked by joint concurrence; `depose` closed (H-L0-9 applied)"),
 "CR-38": ("B10-19", "Court Parliament's bench (design-first)"),
 "CR-39": ("B10-Z", "Promotion of an emerged creed (HELD on CR-38)"),
 "CR-40": ("B10-16", "One grain for Prosperity: delete `starting_pros`"),
 "CR-41": ("B10-08", "Record the ministry ruling at `office_bodies`"),
 "CR-42": ("B10-08", "No faction count is written: re-word the stale 'eight'"),
 "CR-43": ("B10-08", "`PI` names nothing; one row per meaning; the CI start value and gloss"),
 "CR-44": ("B10-08", "Case ids are series-prefixed; a collision is recorded (`CASE_SERIES`)"),
}
# the port gate's new positions (GO-01, GO-05 and GO-06 are v9 handles, in V9)
GO = {
 "GO-07": "B10-03b", "GO-08": "B10-20", "GO-09": "B10-20", "GO-10": "B10-20", "GO-11": "B10-20",
 "GO-12": "B10-20", "GO-13": CLOSED, "GO-14": "B10-03", "GO-15": "B10-20", "GO-16": "B10-20",
}
NM = {f"NM-W{n}": "B10-19" for n in range(10)}
NM["NM-W0"] = "B10-02"
NM["NM-W2"] = "B10-05"
NM["NM-W3"] = CLOSED
CL = {"CL-CHAR": "B10-10", "CL-ATTR": "B10-19", "CL-TROOP": "B10-19", "CL-EVENTS": "B10-18", "CL-THRUST": "B10-19"}

# In-batch order of the final cut ('->' is serial; 'held:' members wait on the question named and slot in by rule R8;
# 'landing' is a commit of a row that lives in another batch, not a member)
ORDER = {
 'B10-02': 'REM-10 -> REM-11 -> REM-13 -> REM-14 -> REM-12 -> REM-15 -> CR-15 -> landing CL-THRUST B0.1 -> CR-14 -> CR-05 -> CR-04 -> REM-16 -> NM-W0 -> CR-01 -> IN-18',
 'B10-03': 'REM-42 -> REM-46 -> REM-47 -> CR-06 -> GO-14 (with H-L0-5) -> PC-05 (EDIT row) -> DEF-9 (with L0-1)',
 'B10-03b': 'GO-07',
 'B10-04': 'REM-50',
 'B10-05': 'REM-21 -> REM-22 -> REM-23 -> CR-28 -> REM-24 -> REM-25 -> CP-T05-04 -> REM-2C -> CR-07 -> landings CL-THRUST B2.1/B2.2 -> landing CL-THRUST B3.1 -> REM-52 -> landing CL-EVENTS (1) -> NM-W2 (EDIT row)',
 'B10-06': 'REM-26 -> REM-27 -> REM-28 -> CR-23 -> REM-29 -> REM-2A -> REM-2B -> IN-45',
 'B10-07': 'REM-44 (with L1-6 and L1-7)',
 'B10-07b': 'SE-06 (MEASURE, then BUILD if values exist) -> CR-21 -> CR-16',
 'B10-08': 'CR-41 -> CR-42 -> CR-43 -> CR-44 -> CP-T01-03 -> CP-T01-04 -> CP-T01-06 -> CP-T01-05 -> CP-T01-01 -> CP-T01-02 -> CR-18',
 'B10-09': 'CP-T02-01 -> CP-T02-02 -> CP-T03-00 -> CP-T02-03 -> CP-T02-05 -> CP-T02-07 -> IN-12 -> CR-26 -> IN-61; close two: IN-58 -> CR-03 -> CR-10 -> landing CL-THRUST B3.2 -> CR-11 -> CR-25 -> CR-17',
 'B10-10': 'landing CP-T01-05 NPC half (conditional) -> REM-31 -> REM-30 -> CR-20 -> CR-30 (one combined Person repr re-pin with CR-20) -> CR-19 -> CR-33 -> CL-CHAR (row deleted at close) -> REM-32 -> CP-T02-06',
 'B10-11': 'CP-T03-01 -> CP-T03-02 -> CP-T03-05 -> CP-T03-09 -> PC-10 -> CP-T03-03 -> CP-T03-04 -> CP-T03-07 -> CP-T03-08 -> CP-T03-06; held: CP-T03-10 (parked), CP-T03-11 (cut)',
 'B10-12': 'CP-T04-01 -> CP-T04-05 -> CR-24 -> CP-T04-02 -> CP-T04-03 -> CP-T04-08 -> CP-T04-06 -> CP-T04-07 -> MB-07r -> CR-12; held: CP-T04-04 (M4 Ask C (b)), CP-T04-10 (M3), CP-T04-09 (cut)',
 'B10-13': 'SC-02 (design) -> CP-T05-02 (ii)(iii) -> CP-T05-03 -> SC-04 -> CR-34 -> [SC-02 re-source -> CP-T05-01 -> CP-T05-02 (i), on approval] -> CR-27 -> CR-31; one close',
 'B10-14': 'CP-T06-09 -> CR-29 (released from M11) -> CP-T06-01 -> CP-T06-03 -> CP-T06-04 -> CP-T06-02 -> CP-T06-07 -> CP-T06-05; held: CP-T06-08 (JA-1)',
 'B10-15': 'CR-13 -> REM-45 -> CP-T07-02 -> CP-T07-03 -> CP-T07-05 -> CP-T07-09 -> CP-T07-04 -> CP-T07-06 -> CP-T07-07 -> CP-T07-10 -> CP-T07-08 -> CP-T07-11 -> IN-32 -> WR-01 (BLK, own condition)',
 'B10-16': "CR-40 -> CP-T08-01 -> CP-T08-03 -> CP-T08-02 -> CP-T08-05 -> CP-T08-06 -> CP-T08-07 -> CP-T08-08 -> IN-14 -> CP-T08-10 -> CP-T08-04 -> IN-52 (the flip); held: SE-04 part (b) (in B10-Z), IN-52's retirement (M3, confirmed at the default), CP-T08-09 (withdrawn)",
 'B10-17': "IN-30 -> CP-T09-04 -> CP-T09-01 -> CP-T09-05 -> CP-T09-02 -> CP-T09-03 -> CP-T09-07 -> CR-09 -> CP-T09-08 -> CP-T09-09 -> CP-T09-06 -> CR-32 -> CR-35 -> CR-36 -> CR-37 -> FA-01's clause (after CR-29) -> IN-48 (two closes: close one IN-30 to CP-T09-06; close two CR-32 to IN-48); held: IN-36 (M1's residue, confirmed at the default)",
 'B10-18': "CP-T10-06 -> CP-T10-07 -> CP-T10-09 -> CP-T10-01 -> CP-T10-02 -> CP-T10-03 -> CP-T10-03's flip -> CL-EVENTS (commit 2) -> CR-08 -> CR-22 -> CL-EVENTS (commit 3) -> CL-EVENTS (commit 4) -> CP-T10-04 -> CP-T10-05 -> CP-T10-08",
 'B10-20': 'GO-09 -> GO-10 -> GO-11 -> GO-12 -> GO-16 -> GO-01 -> GO-05 -> GO-08 -> GO-15; listed: GO-06 (HELD, BLK, another repository)',
 'B10-19': "held: NM-W1, NM-W4, NM-W5 (behind NM-W1), NM-W6, NM-W7, NM-W8, NM-W9, CL-ATTR (J-T2), CL-TROOP (M3), CL-THRUST (B4.x on its gates; B5.2 on M1's residue; B6.n content); DESIGN-FIRST: CR-38 (drafted beside B10-13; approved before B10-18 closes, else on B10-20's freeze row)",
 'B10-Z': 'held or LEAVE: FA-03, FA-07, MB-08, PC-06, PC-08, IN-44 (rows 2-16 released from M11), SC-05, SC-07, CR-39 (on CR-38)',
}

# Remediation DEF rows that the plan itself says are work, not deferrals (rev. 4; D-1 was relayed, and is confirmed by the superseding row of ED-IN-0300, 2026-10-26: M11 answered (a); the data below is unchanged)
DEF = {"DEF-9": ("B10-03", "Delete `engine/engine_params/params_tables.yaml` with a `FORK:` row and `CLAUDE.md` §5's sentence (NERS X3; L0-1); D-1 confirmed (ED-IN-0300)")}
