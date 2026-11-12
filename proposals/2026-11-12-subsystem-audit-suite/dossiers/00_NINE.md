# Dossier 00 · THE NINE (engine/season/requirements.yaml)

ruled_by: Jordan, 2026-09-05 · ed: ED-IN-0204 · scales: [{'scale': 'character creation / development / chronicling', 'subsystem': ['characters', 'npcs'], 'retention': 'RETAINED (Jordan, 2026-10-02, ED-IN-0283 -- the systems/ folders are the homes of their systems)', 'in_loop': False, 'note': "`Person` carries `pursuits`, `ledger`, `stance`, `capability` — but NOTHING creates or develops a person: no generation, no progression, no chronicle. ⚠ `capability` is EMPTY on 429 of the 430 persons the 143 corpus cases build, and holds `{copying: 3}` on one (NPC-088's `p_a`) -- MEASURED 2026-10-02 with `corpus_run.cast_overlay()` and `build_at`; R-09's `measured:` carries the run. Its one corpus writer is `build_at` seating a cast entry's own authored `capability` (`corpus_run.py:537-540`), which is why R-09's roll varies by seed and not by person in 142 of the 143 cases. W27 is the cast."}, {'scale': 'grand strategy politics', 'subsystem': ['factions', 'settlements', 'world'], 'retention': 'RETAINED (Jordan, 2026-10-02, ED-IN-0283 -- the systems/ folders are the homes of their systems)', 'in_loop': False, 'note': "R-04's opening headline, the pre-`20-ii` reading: 44 of 143 cases UNREPRESENTABLE at faction scale and 10 at world scale. `20-ii` closed that census on 2026-09-30 (R-04's `measured:` carries the run). ⚠ REWRITTEN 2026-10-01: no second driver runs this scale beside the season loop. THIS SCALE HAS NO CODE OF ITS OWN: the old campaign driver (plan position `28-iii`), `systems/factions/` and `game_state.Faction`, the stat-vector dataclass (both `29b`), are deleted (their `FORK:5c5d8ec6` rows). A faction is a resolved VIEW (`engine/season/queries/faction_q.py::Faction`: built at a barrier, never a field of `World`, never `Act.actor`), and a faction's act is a person's act `via` a seat (`Act.via`, `engine/season/state/carriers.py`). Intent, for vocabulary only: Layer 1 PART D rows 1/8/14, which rule out a faction that acts, a stored aggregate and a banner holding territory."}, {'scale': 'social contests / debates', 'subsystem': ['social_contest'], 'retention': 'RETAINED', 'in_loop': 'seam unbuilt', 'note': 'The kernel exists and already rolls through the substrate (`resolver.py` imports `degree_from_net` from `engine/dice_engine/dice_engine.py` and wraps `roll_net` from `engine/dice_engine/sigma_leverage.py`). The loop does NOT reach it. ⚠ REWRITTEN 2026-10-01: this sentence used to add "`parliamentary_vote.py` calls `roll_pool`"; that module and `parliamentary_stay.py` were deleted at `29b` (their `FORK:5c5d8ec6` rows), and nothing under `systems/social_contest` calls `roll_pool` now. 4 of 45 verb rows (46 before IN-11 cut `repudiate`) declare `contests:` — `fight` and `accept` (the body, the combat seam), `march` (a field, the mass-battle seam, `ecacb57`) and `tell` (a standing, resolved on the season side by `seam/wrappers/sigma.py`, not by this kernel). The kernel retires at plan position `2-ii` (`workplans/valoria_master_workplan_v9.md`).'}, {'scale': 'mass battles / strategy warfare', 'subsystem': ['mass_battle'], 'retention': 'RETAINED', 'in_loop': "seam built; reached via a constructed `Question` (`test_march.py`) AND, measured, via natural computed play in `build_realm(0)`/`populated.run` (`harness/aperture.py`); not yet reached naturally in `corpus_run`'s separate 143-case NPC/ARC corpus", 'note': 'The seam exists (`ecacb57`, PR #436): `march` declares `contests: a field` and resolves through `seam/wrappers/mass_battle.py` → the `mass_battle.resolve_field` composition role. `test_march.py::test_a_real_chooser_forms_and_folds_a_march_that_reaches_a_real_field_battle` (plan position `28-ii`, M6) demonstrates a real chosen act reaching it, through the real chooser, off a constructed `Question` naming a settlement referent. ⚠ CORRECTED, the Phase 3 terminal critique\'s reconciliation, 2026-09-30: this note used to say march "still sits in `test_season_shape.py`\'s never-attempted set for the NATURAL corpus" and that "no `questions_for` source in the natural corpus ever supplies march a workable referent" -- measured FALSE for `build_realm(0)`/`populated.run`: `python -m engine.season.harness.aperture 1 0`, run twice reproducibly, shows march forming, being offered, being attempted and executing there via the real, unrestricted chooser, with zero constructed `Question` and zero hand-built `Act` (`hole_register.yaml` H-175). `march` DOES still sit in `test_season_shape.py`\'s never-attempted set, but that set is drawn from `corpus_run`\'s separate, narrower, individually-authored 143-case NPC/ARC corpus, not from the natural corpus generally -- a fresh `corpus_run` this same session re-confirms march is still absent there. `decision/options.py::opening_set`\'s clause 3 applies no referent-kind filter and `operands_for` already carries `march`\'s operands correctly (neither was ever the gap). WHY `corpus_run`\'s 143 cases specifically never supply march a workable referent, while the populated realm does, is UNMEASURED (`hole_register.yaml` H-175\'s `cite:`). `H-151`\'s OWN `cite:` field, not H-175\'s, is where the earlier retraction of a stale "missing `operands_for` arm" citation actually lives.'}, {'scale': 'personal combat / grid-based map combat with units', 'subsystem': ['combat'], 'retention': 'RETAINED, NOT DONE (Jordan, 2026-09-05: "combat engine isn\'t done")', 'in_loop': 'duel only, via combat_seam.py', 'note': "⚠ THE TWO HALVES OF THIS SCALE ARE NOT THE SAME THING. The duel engine is real and the loop already calls it (`combat_seam.py` -> `wrapper.fight`), but it is a CONTINUOUS RANGE model (`combat_systems.py::RANGE_COMMIT_PEAK`, `RANGE_AVAIL_FLOOR`) between two combatants. ⚠ CORRECTED 2026-10-26 (v10 REM-03, B10-01): this note used to say grid-based map combat with units exists nowhere in the tree. `modules/mass_battle` holds a cell battlefield (`config.py:14` `BATTLEFIELD_SIZE`, `:23` `UNIT_GRID_SIZE`); what does not exist is the decision at its scale (commander-chosen orders). THE READING OF THIS ROW [ASSUMPTION; medium; Jordan to correct; revert: commander-chosen orders restored as a third gate]: it reads `in_loop` when, in computed play, (i) a duel resolves (`fight` or `accept` -> the combat seam; true today) and (ii) a fought field (`field.won` or `field.lost`, never `field.unopposed`) resolves on `modules/mass_battle`'s cell battlefield. Commander-chosen orders are not a gate: they are a named residue (the AUTOMATED mode may run the default orders, `massbattle.py:170-178`), whose trigger is a position that designs a typed `Orders` record shared by the PLAYABLE scene and the AUTOMATED planner (MB-08's AI-generals half, LEAVE). R-04 may read `met` at CP-T04's close when conjunct (1) and the other conjuncts also read (`workplans/valoria_master_workplan_v10_part2.md` §5)."}, {'scale': 'settlement management / city building / domain actions', 'subsystem': ['settlements', 'overview'], 'retention': 'RETAINED (Jordan, 2026-10-02, ED-IN-0283 -- the systems/ folders are the homes of their systems)', 'in_loop': False, 'note': "ADDED 2026-09-05 on Jordan's correction — the first draft of this roster missed it. The design surface is substantial and explicit: `settlement_layer_v30.md`, `settlement_generator_v1.md`, `settlements_currency_v1.md`, `march_layer_v30.md`, `governance_play_redesign_v1.md`, `scale_hierarchy_v1.md`. `references/module_contracts.yaml` declares `domain_actions` and `settlement_economy` — BOTH with `doc: null`, two of the nine contracts §6 counts as unimplementable. The loop has `Site`, `stores` and `condition`; `found`, `build`, `restore` and `work` are declared in `verb_table.yaml`; in the realm only `restore` executes (cohorts mending their own settlement's fabric since `24f`), while `found`, `build` and `work` are formed and refused because no computed act declares a works (`H-165`); no domain-action mechanism exists."}, {'scale': 'investigations / detective / interactive fiction', 'subsystem': ['fieldwork'], 'retention': 'RETAINED (Jordan, 2026-10-02, ED-IN-0283 -- the systems/ folders are the homes of their systems)', 'in_loop': False, 'note': 'Six investigation acts exist in `verb_table.yaml` and NONE declares `contests:` — so investigation is not ungraded, it is UNGRADEABLE. ⚠ THE FIRST CLAUSE WAS FALSE UNTIL 2026-09-10 AND IS NOW TRUE: one row spelled `"the six investigation acts"` stood for six, and ED-FI-0009 split it into `examine` · `interview` · `research` · `surveil` · `thread_read` · `reconstruct`. The second clause is unchanged and is a RULING, not an omission — see `rosters.yaml`\'s `THE SEAMS` comment block (*"INVESTIGATION MUST NOT BE MADE A CONTEST TO BECOME GRADEABLE"*; this note cited it by line, `:505-508`, and the lines moved). One composition role targets this subsystem since v9 FI-02/FI-03: `fieldwork.find` (`references/module_contracts.yaml`\'s `composition_roles:` block), the `inquiry` role\'s entry, `step_call`, gated (it runs for a graded finding band whose Event kind a row claims). `fieldwork` is a `rosters.yaml` `modules:` entry, so it is not in the computed `R04_PENDING_SUBSYSTEMS` (`tests/valoria/test_engine_does_not_import_systems.py`); `R04_PENDING_ROLES` is empty.'}]

Instrument: `python -m engine.season.harness.register --requirements`. Full `measured:` blocks are in the file (read them there); below: id, status, statement, measure, blocks.

## R-01 — met

**Statement:** decisions must propagate

**Measure:** python -m engine.season.harness.corpus_run  # check R3 rows + the planted control

**Blocks:** ['IN-10', 'IN-11', 'IN-13', 'H-116', 'IN-50']

## R-02 — met

**Statement:** decisions affect subsequent decisions

**Measure:** python proposals/2026-09-04-degree-sweep/wd_collect.py  # after wd_chunk.py x4 per arm per cell over the 143-case corpus (slices 0 36/36 72/72 108/108 143) -- U6's command, workplans/valoria_master_workplan_v11_part2.md §`11`

**Blocks:** []

## R-03 — met

**Statement:** seasons must tick scene-by-scene, so what occurs after one scene can impact the next scene

**Measure:** python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0  # and `pytest engine/season/tests -q -k test_u2_`, which is what §0.2 accepts

**Blocks:** []

## R-04 — partial

**Statement:** strategic and management actions must be possible, ie decisions at differing scales

**Measure:** python -m engine.season.harness.aperture 4 0  # the per-verb lines: `levy` and the seat-gated rows (about 25 minutes); `corpus_run` prints no 'unrepresentable scales:' line any more, the census is empty

**Blocks:** ['IN-10', 'IN-40', 'FA-01', 'IN-49', 'SC-01', 'IN-46', 'IN-47']

## R-05 — not_met

**Statement:** all verbs must be built out, and doing so requires planning out all the different scales of play required in a season

**Measure:** python -m engine.season.harness.corpus_run  # the 'WHERE THE <n> GO' line, which prints len(VERB_TABLE); the denominator is len(VERB_TABLE) at measurement time (v10 REM-02, `workplans/valoria_master_workplan_v11_part2.md` §6; [ASSUMPTION; medium; Jordan to correct]): a row leaves the table only by a ruling or a ratified design decision cited in its commit, never to move R-05, and every removal is recorded in R-05's `measured:` block; a row in the table but outside resolvable_verbs() counts under 'have no predicate/effect', so a row landed dark raises n. 'Built out' = at least one act formed by the chooser in a seeded run of a shipped builder is admitted, folds its band and emits the row's declared kinds; where the admitted band declares writes, at least one minted receipt has before ≠ after; a verb whose bands write nothing (`speak`, `interrogate`) is built out on execution; a hand-built

**Blocks:** ['H-65', 'IN-09', 'IN-10', 'IN-33', 'IN-45']

## R-06 — partial

**Statement:** characters must be robustly built with goals, ambitions, convictions, moral values, etc

**Measure:** python -m engine.season.harness.corpus_run  # 'RANKING DISCRIMINATION' line

**Blocks:** ['IN-38', 'IN-08', 'IN-18', 'IN-12']

## R-07 — partial

**Statement:** characters must have memories and feelings and attitudes and relationships, and they must only have imperfect knowledge

**Measure:** python -m pytest engine/season/tests -k 'choose_receives_no_world or a_view or r7_two_persons'

**Blocks:** ['IN-38']

## R-08 — partial

**Statement:** decisions must not be omniscient and perfectly rational — characters may not make the optimal decision based upon their epistemic knowledge and personal inclinations

**Measure:** python -m engine.season.harness.corpus_run  # 'RANKING DISCRIMINATION' + tie ordering

**Blocks:** ['SC-01', 'IN-08', 'IN-18', 'IN-12']

**needs_jordan:** False

**disposition:** ⚠ AN EARLIER DRAFT OF THIS ROW FLAGGED `needs_jordan: true` AND WAS WRONG TWICE — corrected here rather than carried. (1) It described the CANDIDATE tie as broken by "an undeclared content-hash tiebreak". It is not; it is alphabetical, and the row's own `measure:` command prints that. The content hash is the WITHIN-SOURCE QUESTION tiebreak (`q.id`, `engine/season/decision.py::make_chooser`), a different mechanism. (2) That question tiebreak is ALREADY DISPOSED: `engine/season/decision.py::make_chooser` records it closing at §0 step 4 on `H-54`'s precedent with `needs_jordan` FALSE. Re-surfacin

## R-09 — partial

**Statement:** chains of events within a scene are probabilistic, not deterministic

**Measure:** python -m engine.season.harness.aperture 4 0

**Blocks:** ['H-98']
