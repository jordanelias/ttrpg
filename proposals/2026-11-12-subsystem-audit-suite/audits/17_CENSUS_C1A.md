# Census C1A — unreferenced symbols in the season loop's core packages

## Status: REFERENCE (a census verdict; resolves nothing at runtime)

## Read at: b805fad (working tree; no game-code change since d7bd4ab, where the census was built)

Partition: every row of `census/C1_unreferenced_symbols.md` whose file is under
`engine/season/{loop,state,seam,manifest,decision,queries,data}/`, plus the two top-level files
`engine/season/epistemic.py` and `engine/season/gaps.py`.

| | rows | dead | broken | mislabelled | false positive |
|---|---|---|---|---|---|
| the C1 rows assigned | **187** | **4** | **10** | 0 | **173** |
| extension (names the census could not list, §4) | 48 | 9 (+1 already decided by FA) | 11 | 9 pointer sites (a separate scan) | 27 |

Proposals: `proposals/17_CENSUS_C1A_01_deletion_batches.md`,
`proposals/17_CENSUS_C1A_02_wires_and_corrections.md`.

## 0. Verdict

**The C1 list is, for these packages, a list of private helpers, and 173 of its 187 rows are false
positives: each is used inside its own file by code the season driver, a registry or an import-time
check reaches.** `file-local only` describes a private function correctly and says nothing about whether
it is dead. Four rows are dead and are deleted (`gaps.Ineligible`, `cast.name_of`, and the two listed
halves of `world_q`'s person projection). Ten rows are live as symbols and inert as game: four belong to
the character sheet's spaces, which only tests enter, and six serve effects whose verbs never ran in the
corpus (army, march, found, build, establish).

The larger yield is what a name-based census cannot list. Following every top-level name in the
partition upward to a root (the driver, a registering decorator, a module-level statement, a harness
entry) finds a second population that tests alone keep standing: a client read with no client
(`world_q.projection`), a registry report nobody asks for (`cast.defects`), a validated column on 68 verb
rows that no decision reads (`beneficiary:`), three queries Layer 1 names and nothing calls
(`footprint`, `density`, `sovereign_fraction`), and nine comment pointers to files that moved or were
dropped. None of these changes a seeded run today; each is a place where a reader of the code is told
something works that nothing executes.

## 1. Method, and what the census script cannot see

Each row was followed upward, by AST and by resolved import (not by name), until it reached one of:
a top-level definition in `loop/driver.py`; a function registered by a decorator (`effect_for`,
`requires_predicate`, `provider`, `requirement_form`, `_context`); a module-level statement (a loader or
a check run at import); a harness entry; a test or tool; or nothing. Instrument: a read-only script in the
scratchpad (`c1a/reach6.py`), not in the tree and not proposed for it. Every non-driver verdict was then
read at its site, and the registries were probed once (§5).

Four dispatch forms defeat a name search, and each accounts for rows here:

| form | site | rows it explains |
|---|---|---|
| `globals().get(f"_ch_{c}")`, `globals().get(f"_term_{t}")` | `epistemic.py:698`, `:957` | `cache.TenureIndex`, `_build_tenure_index` (reached from `_ch_document_key`, `_ch_witness_key`) |
| a decorator that fills a dict read by key | `options.py:437-446` (`VIOLENCE_CONTEXT_READERS`, read `:503`); `loop/effects.py` (`EFFECTS`); `manifest/providers.py` (`PROVIDERS`); `data/requires.py:231` | the four `_*_context` rows, `ContainPath`, and every helper under an `_eff_*` or a wrapper's `resolve` |
| a dict of readers keyed by a roster member | `world_q.py:3193` (`_TIE_READERS`, called `:3227`), `:4810` (`_MATTER`, called `:5036`) | `_heir_title_holders`, `_sworn_retainers`, `_claimed_seat`, `_petitioned_matter` |
| `getattr(mod, "load")` over `pkgutil` discovery | `data/__init__.py:50-58` | the `load()` of `cast`, `goals`, `geography` (extension) |

One reading the census gets wrong in the other direction: a mention in a comment or docstring counts as a
use. `data/fixtures.py` names `flow_stakes`, `settle_efforts` and `odds_weight` only in comments, and
`decision/__init__.py` names the sheet's four spaces only in its docstring. The season package has no
composition root outside `harness/` (`populated.run`, `soak`, `storybar`, `corpus_run`, `play_surface`
build the driver and hand it a chooser), so "reached only from `harness/`" is not "dead": it is either the
composition root or an instrument, and §3 says which.

## 2. Findings, by weight

**F-C1A-01 · the person projection is a client read with no client (dead; batch D2).**
`world_q.py:4359-4441` (`_person_or_refuse`, `witnessed`, `PersonProjection`, `projection`; "what a client
reads for that person", v9 PC-06 S-2/L-1) is imported by `tests/test_person_projection.py` and by nothing
else: no harness module, tool, plan, register row or Layer 1 row names it. Its own docstring records an
unanswered contract question (whether an Event a person inferred belongs in `witnessed`).
`11_GO_player_surface_contract_B.md` §3-§4 decides the player's reading the other way: `account` reads the
person's own ledger and nothing else, and `receipt` walks forward from his own act, host-side. A second
shape that hands a client copies of whole Events is the seventh player-view dialect that proposal's
problem 1 counts six of. Cut test: one test file dies, and no run, instrument or proposal loses a reader.
Falsifier: `grep -rn "projection(\|PersonProjection\|witnessed(" engine modules tools --include=*.py`
outside `world_q.py` and `tests/` returns a call site.

**F-C1A-02 · the character sheet's spaces are entered by tests only (broken; W1, carried by GO).**
`decision/sheet.py` (`creation_sheet`, `seat`, `development_space`, `take_ranked`, `chronicle`) is imported
by three test files. `harness/play_surface.py` imports nothing from it; its docstring `:29` says the seam is
covered by tests. The suite needs the file: `11_GO_player_surface_contract.md` and `_B.md` build `Situation`,
`Offer` and `account` on `DevelopmentSheet` and `chronicle`, and B's gate (`:241-242`) is a
`harness.play_surface` entry that seats a person with `take_ranked`. That entry is the missing wire. This
lane adds no second one.

**F-C1A-03 · six helper rows serve effects that never ran (broken; W2, carried by VERBS).** The symbols
are registered and reachable. The corpus run (shared reading, §5) reports `recruit`, `form_unit`,
`assign_troops`, `disband_unit`, `discharge_troops`, `order_unit`, `march` and `establish` among the 30
verbs "foldable but never even attempted", and `found`, `build` among the 13 "only refused". So
`_army`, `_payload`, `_siege`, `_works_named`, `_made_by` and `founded_office_id` have executed in tests
and never in a world. The army verbs are withheld from the chooser by fixture and offered through
`harness/military_menu.py`, which no automated run drives.

**F-C1A-04 · `beneficiary:` is a validated column no decision reads (extension; broken; W4).**
`verb_table.yaml` carries `beneficiary:` on 68 rows; `data/verbs.py:789-811` refuses a bad one at load;
the one runtime reader, `decision/choose.py:281-319 beneficiary_of`, is called by
`tests/test_governance_build.py` only. `score_terms` (`choose.py:193-221`) never asks who an act is for.
The code's own rule for this is quoted in `data/rosters.py:1406-1407`: "a column nobody reads is a column
that silently does nothing". Four suite proposals author new `beneficiary:` values
(`14_VERBS_SOCIAL1_A`, `14_VERBS_SOCIAL2_D` among them) and `01_CORE_capability_authoring_surface.md:78`
cites its loader refusal as the model, so the suite treats the column as live grammar. No suite proposal
reads it.

**F-C1A-05 · three Layer 1 queries have no caller (extension; broken; reader owed, no proposal names
one).** `architecture/holonic_ARCHITECTURE.md:597-598` enumerates `density`, `footprint` and
`sovereign_fraction` as Queries. In code: `world_q.py:2081 footprint` and `:2111 density` are called by
nothing, not even a test; `:2372 sovereign_fraction` and `:2421 provinces_of` by `test_season_shape.py`
only. They are not deleted: Layer 1 names three of them, and `provinces_of` is the ratified province
(`06_FA_audit_addendum_B.md:272, :510`). They are the strategic layer's readings (R-04, `partial`) waiting
for a strategic surface. See §6.

**F-C1A-06 · small dead matter (extension; batch D1, D3).** `cast.defects` (`data/cast.py:408-423`) has no
caller at all; run once, it returns three rows, all `Independent (...)` factions resolving to no roster
name, which is the designed unaffiliated state `populated.py:1312` already handles. `files.SEAM_DIR` and
`files.COMBAT_SEAM_PY` (`data/files.py:246-251`) are read by nothing; `seam/__init__.py:26` still speaks of
the constant as part of a guard. `state/world.py:166` binds `_FIRST, _SECOND` and never uses them.
`person_q.violated_pursuits` and `violated_affiliations` (`:637-670`) are test-only twins of the live pair
`elements_violated_by` + `broken_by`, which `loop/resolve.py::_scar_witnesses` calls and whose docstring
(`:770-773`) states the equivalence.

**F-C1A-07 · nine comment pointers name files that moved or were dropped (extension; mislabelled; C1).**
Of 700 `file.py::symbol` pointers in the partition's comments, a scan found 12 that do not resolve; nine
were confirmed stale at the site (five to `loop/effects.py::_eff_*` after the per-subsystem split, two to
`shape.py::SeasonDriver::…`, two to `tests/test_obligees.py`, dropped at `FORK:217340fc`). Text
corrections in proposal 02.

## 3. The 187 rows

Reading: how the symbol is reached. Decision: one of the four in `CENSUS_BRIEF.md`. Evidence: the chain
(`a <- b` is "b uses a"; `...` elides middle links; `driver SeasonDriver` is a top-level name in
`loop/driver.py`), or the site read by hand.

| row | reading | decision | evidence |
|---|---|---|---|
| `data/affiliations.py:79` `_true_pairs` | private helper of code the driver reaches | False positive | `_true_pairs <-  INCOMPATIBLE ; INCOMPATIBLE <- queries/person_q.py conviction_after_crisis ; ... ; driver SeasonDriver` |
| `data/affiliations.py:84` `_load_incompatibility` | private helper of code the driver reaches | False positive | `_load_incompatibility <-  INCOMPATIBILITY ; INCOMPATIBILITY <- queries/world_q.py commensurate ; ... ; driver SeasonDriver` |
| `data/arrangements.py:107` `_refuse_any_not_in` | private helper of code the driver reaches | False positive | `_refuse_any_not_in <-  _load_arrangement ; _load_arrangement <-  _load ; ... ; driver SeasonDriver` |
| `data/arrangements.py:117` `_parse_floor` | private helper of code the driver reaches | False positive | `_parse_floor <-  _load_arrangement ; _load_arrangement <-  _load ; ... ; driver SeasonDriver` |
| `data/arrangements.py:134` `_load_speech_kind` | private helper of code the driver reaches | False positive | `_load_speech_kind <-  _load ; _load <-  ARRANGEMENTS ; ... ; driver SeasonDriver` |
| `data/arrangements.py:156` `_load_arrangement` | private helper of code the driver reaches | False positive | `_load_arrangement <-  _load ; _load <-  ARRANGEMENTS ; ... ; driver SeasonDriver` |
| `data/arrangements.py:80` `_refuse_unknown` | private helper of code the driver reaches | False positive | `_refuse_unknown <-  _load_arrangement ; _load_arrangement <-  _load ; ... ; driver SeasonDriver` |
| `data/arrangements.py:89` `_refuse_not_in` | private helper of code the driver reaches | False positive | `_refuse_not_in <-  _load_arrangement ; _load_arrangement <-  _load ; ... ; driver SeasonDriver` |
| `data/cast.py:118` `name_of` | one test assertion | Dead: delete (batch D1) | `Person.name` is built from the case row's `name:` (`harness/populated.py:1315`), never from `first_name`/`last_name`; only reader `tests/test_cr30_heritage.py:131`; probe: 83 of 83 persons named at `build_realm(0)` without it |
| `data/cast.py:87` `_rows` | private helper of code the driver reaches | False positive | `_rows <-  row ; row <- data/goals.py _object ; ... ; driver SeasonDriver` |
| `data/files.py:201` `loop_source` | guard corpus anchor | False positive | read by `tests/test_season_shape.py:86,11916`, a Layer 1 script; the function exists for it (docstring `:202-203`) |
| `data/files.py:236` `decision_modules` | guard corpus anchor | False positive | the AX-2 by-path scan's corpus, `tests/test_season_shape.py:2982` |
| `data/fixtures.py:143` `_check_keyed_on_site_kinds` | private helper of code the driver reaches | False positive | `_check_keyed_on_site_kinds <-  _load_capacity_floor ; _load_capacity_floor <-  CAPACITY_FLOORS ; ... ; driver SeasonDriver` |
| `data/goals.py:108` `_where` | private helper of code the driver reaches | False positive | `_where <-  _refuse ; _refuse <-  parse ; ... ; driver SeasonDriver` |
| `data/goals.py:116` `_through` | private helper of code the driver reaches | False positive | `_through <-  _object ; _object <-  parse ; ... ; driver SeasonDriver` |
| `data/goals.py:132` `_text` | private helper of code the driver reaches | False positive | `_text <-  parse ; parse <-  goals ; ... ; driver SeasonDriver` |
| `data/goals.py:139` `_org` | private helper of code the driver reaches | False positive | `_org <-  parse ; parse <-  goals ; ... ; driver SeasonDriver` |
| `data/goals.py:160` `_object` | private helper of code the driver reaches | False positive | `_object <-  parse ; parse <-  goals ; ... ; driver SeasonDriver` |
| `data/goals.py:213` `_pursuits` | private helper of code the driver reaches | False positive | `_pursuits <-  parse ; parse <-  goals ; ... ; driver SeasonDriver` |
| `data/goals.py:230` `_is_orientation` | private helper of code the driver reaches | False positive | `_is_orientation <-  _axis ; _axis <-  parse ; ... ; driver SeasonDriver` |
| `data/goals.py:236` `_thrust_axes` | private helper of code the driver reaches | False positive | `_thrust_axes <-  parse ; parse <-  goals ; ... ; driver SeasonDriver` |
| `data/goals.py:271` `_axis` | private helper of code the driver reaches | False positive | `_axis <-  parse ; parse <-  goals ; ... ; driver SeasonDriver` |
| `data/goals.py:331` `_ancestors` | private helper of code the driver reaches | False positive | `_ancestors <-  parse ; parse <-  goals ; ... ; driver SeasonDriver` |
| `data/goals.py:379` `_stages` | private helper of code the driver reaches | False positive | `_stages <-  _goal_stages ; _goal_stages <-  parse ; ... ; driver SeasonDriver` |
| `data/goals.py:414` `_goal_stages` | private helper of code the driver reaches | False positive | `_goal_stages <-  parse ; parse <-  goals ; ... ; driver SeasonDriver` |
| `data/goals.py:79` `GoalStages` | private helper of code the driver reaches | False positive | `GoalStages <-  Goal ; Goal <-  goal ; ... ; driver SeasonDriver` |
| `data/matrix.py:119` `MatrixRow` | private helper of code the driver reaches | False positive | `MatrixRow <-  matrix_row ; matrix_row <- loop/resolve.py _apply_write ; ... ; driver SeasonDriver` |
| `data/matrix.py:208` `_retirement` | private helper of code the driver reaches | False positive | `_retirement <-  MATRIX_RETIRED ; MATRIX_RETIRED <-  matrix_row ; ... ; driver SeasonDriver` |
| `data/requires.py:144` `_Unknown` | private helper of code the driver reaches | False positive | `_Unknown <-  UNKNOWN ; UNKNOWN <- loop/resolve.py _admits ; ... ; driver SeasonDriver` |
| `data/requires.py:213` `_bound` | private helper of code the driver reaches | False positive | `_bound <-  Existence ; Existence <- data/verbs.py _record_kinds_answered ; ... ; driver SeasonDriver` |
| `data/requires.py:247` `Requirement` | private helper of code the driver reaches | False positive | `Requirement <-  TypedRequires ; TypedRequires <-  evaluate ; ... ; driver SeasonDriver` |
| `data/requires.py:376` `ContainPath` | registered form, named by two verb rows | False positive | `@requirement_form("contain_path")` at `requires.py:374`; `verb_table.yaml:1163,1195` (`form: contain_path`) |
| `data/requires.py:48` `_check_operand_subset` | loader refusal run at import | False positive | `_check_operand_subset <- data/requires.py module stmt L132` |
| `data/requires.py:689` `_observe` | private helper of code the driver reaches | False positive | `_observe <-  Existence ; Existence <- data/verbs.py _record_kinds_answered ; ... ; driver SeasonDriver` |
| `data/requires.py:904` `_check_known_person_claim` | loader refusal run at import | False positive | `_check_known_person_claim <- data/requires.py module stmt L929` |
| `data/requires.py:966` `_check_shortfall_stem` | loader refusal run at import | False positive | `_check_shortfall_stem <- data/requires.py module stmt L990` |
| `data/rosters.py:1119` `_load_strife_kinds` | private helper of code the driver reaches | False positive | `_load_strife_kinds <-  STRIFE_KINDS ; STRIFE_KINDS <- queries/world_q.py CONCLUDING_KINDS ; ... ; driver SeasonDriver` |
| `data/rosters.py:1392` `_load_modules` | import-time loader; roster read by a Layer 1 guard | False positive | `MODULES = _load_modules(...)` at `:1423` (refusal at import); `MODULES` read by `tests/valoria/test_engine_does_not_import_systems.py:710` |
| `data/rosters.py:1432` `EndingRow` | private helper of code the driver reaches | False positive | `EndingRow <-  _load_endings ; _load_endings <-  ENDINGS ; ... ; driver SeasonDriver` |
| `data/rosters.py:1448` `_load_endings` | private helper of code the driver reaches | False positive | `_load_endings <-  ENDINGS ; ENDINGS <- queries/world_q.py endings_reached ; ... ; driver SeasonDriver` |
| `data/rosters.py:753` `check_logged_kinds` | private helper of code the driver reaches | False positive | `check_logged_kinds <-  LOGGED_KINDS ; LOGGED_KINDS <-  STANDING_CROSSED ; ... ; driver SeasonDriver` |
| `data/rosters.py:775` `_check_scale_of_rung` | loader refusal run at import | False positive | `_check_scale_of_rung <- data/rosters.py module stmt L794` |
| `data/verbs.py:1170` `_produced_pairs` | private helper of code the driver reaches | False positive | `_produced_pairs <-  _load_verb_table ; _load_verb_table <-  VERB_TABLE ; ... ; driver SeasonDriver` |
| `data/verbs.py:1213` `_check_duel_terms` | registered by decorator; registry read at runtime | False positive | `_check_duel_terms <-  DUEL_TERMS_BY_VERB ; DUEL_TERMS_BY_VERB <- seam/wrappers/combat.py duel_terms_of ; ... ; resolve @provider('contest', _PROVIDER)` |
| `data/verbs.py:1400` `_load_projection` | private helper of code the driver reaches | False positive | `_load_projection <-  PURSUIT_PROJECTION ; PURSUIT_PROJECTION <- data/pursuits.py to_axes ; ... ; driver SeasonDriver` |
| `data/verbs.py:1445` `_load_role_template_pursuits` | private helper of code the driver reaches | False positive | `_load_role_template_pursuits <-  ROLE_TEMPLATE_PURSUITS ; ROLE_TEMPLATE_PURSUITS <- data/goals.py expected ; ... ; driver SeasonDriver` |
| `data/verbs.py:1495` `_check_deed_kinds` | loader refusal run at import | False positive | `_check_deed_kinds <-  _check_covert_kinds ; _check_covert_kinds <- data/verbs.py module stmt L1562` |
| `data/verbs.py:1567` `_asks_subject_held` | private helper of code the driver reaches | False positive | `_asks_subject_held <-  _derive_holding_record_kinds ; _derive_holding_record_kinds <-  HOLDING_RECORD_KINDS ; ... ; driver SeasonDriver` |
| `data/verbs.py:1599` `_derive_holding_record_kinds` | private helper of code the driver reaches | False positive | `_derive_holding_record_kinds <-  HOLDING_RECORD_KINDS ; HOLDING_RECORD_KINDS <- queries/world_q.py records_held_for_holding_rows ; ... ; driver SeasonDriver` |
| `data/verbs.py:1617` `_derive_declared_classes` | private helper of code the driver reaches | False positive | `_derive_declared_classes <-  DECLARED_CLASSES ; DECLARED_CLASSES <- queries/world_q.py _of_stamped_class ; ... ; driver SeasonDriver` |
| `data/verbs.py:1672` `_load_vocation_sourced` | private helper of code the driver reaches | False positive | `_load_vocation_sourced <-  VOCATION_SOURCED ; VOCATION_SOURCED <-  act_key ; ... ; driver SeasonDriver` |
| `data/verbs.py:1703` `_load_choice_sourced` | private helper of code the driver reaches | False positive | `_load_choice_sourced <-  CHOICE_SOURCED ; CHOICE_SOURCED <-  act_key ; ... ; driver SeasonDriver` |
| `data/verbs.py:1726` `_load_held_document_declines` | registered by decorator; registry read at runtime | False positive | `_load_held_document_declines <-  HELD_DOCUMENT_DECLINES ; HELD_DOCUMENT_DECLINES <- decision/options.py opening_set ; ... ; p11 @probe('P11')` |
| `data/verbs.py:1750` `_load_own_stance_declines` | registered by decorator; registry read at runtime | False positive | `_load_own_stance_declines <-  OWN_STANCE_DECLINES ; OWN_STANCE_DECLINES <- decision/options.py opening_set ; ... ; p11 @probe('P11')` |
| `data/verbs.py:1771` `_load_lie_verbs` | registered by decorator; registry read at runtime | False positive | `_load_lie_verbs <-  LIE_VERBS ; LIE_VERBS <- decision/options.py opening_set ; ... ; p11 @probe('P11')` |
| `data/verbs.py:1796` `_load_own_hold_declines` | registered by decorator; registry read at runtime | False positive | `_load_own_hold_declines <-  OWN_HOLD_DECLINES ; OWN_HOLD_DECLINES <- decision/options.py opening_set ; ... ; p11 @probe('P11')` |
| `data/verbs.py:1820` `_load_own_title_declines` | registered by decorator; registry read at runtime | False positive | `_load_own_title_declines <-  OWN_TITLE_DECLINES ; OWN_TITLE_DECLINES <- decision/options.py opening_set ; ... ; p11 @probe('P11')` |
| `data/verbs.py:1842` `_load_held_edge_declines` | registered by decorator; registry read at runtime | False positive | `_load_held_edge_declines <-  HELD_EDGE_DECLINES ; HELD_EDGE_DECLINES <- decision/options.py opening_set ; ... ; p11 @probe('P11')` |
| `data/verbs.py:1863` `_load_violence_contexts` | registered by decorator; registry read at runtime | False positive | `_load_violence_contexts <-  VIOLENCE_CONTEXTS ; VIOLENCE_CONTEXTS <- decision/options.py opening_set ; ... ; p11 @probe('P11')` |
| `data/verbs.py:1884` `_derive_violent_verbs` | registered by decorator; registry read at runtime | False positive | `_derive_violent_verbs <-  VIOLENT_VERBS ; VIOLENT_VERBS <- decision/options.py VIOLENT_OPPONENT_VERBS ; ... ; _defence_context @_context('defence')` |
| `data/verbs.py:1898` `_derive_rung_remit_acts` | private helper of code the driver reaches | False positive | `_derive_rung_remit_acts <-  RUNG_REMIT_ACTS ; RUNG_REMIT_ACTS <- queries/world_q.py larders_in_purview ; ... ; driver SeasonDriver` |
| `data/verbs.py:1916` `_remit_acts_of_class` | private helper of code the driver reaches | False positive | `_remit_acts_of_class <-  DETAINEE_REMIT_ACTS ; DETAINEE_REMIT_ACTS <- queries/world_q.py detainees_held ; ... ; driver SeasonDriver` |
| `data/verbs.py:1923` `_remit_acts_of` | private helper of code the driver reaches | False positive | `_remit_acts_of <-  CONVENING_REMIT_ACTS ; CONVENING_REMIT_ACTS <- queries/world_q.py matters_awaiting ; ... ; driver SeasonDriver` |
| `data/verbs.py:1989` `_check_alignment_density` | private helper of code the driver reaches | False positive | `_check_alignment_density <-  _load_alignment ; _load_alignment <-  ALIGNMENT ; ... ; driver SeasonDriver` |
| `decision/choose.py:144` `_odds_arm` | registered by decorator; registry read at runtime | False positive | `_odds_arm <-  score_terms ; score_terms <-  make_ranker ; ... ; p31 @probe('P31')` |
| `decision/choose.py:224` `_npc_effort_arm` | registered by decorator; registry read at runtime | False positive | `_npc_effort_arm <-  settle_efforts ; settle_efforts <-  make_ranker ; ... ; p31 @probe('P31')` |
| `decision/options.py:1005` `holds_own_document` | registered by decorator; registry read at runtime | False positive | `holds_own_document <-  opening_set ; opening_set <- decision/__init__.py opening_set ; ... ; p11 @probe('P11')` |
| `decision/options.py:1364` `_person_bags` | registered by decorator; registry read at runtime | False positive | `_person_bags <-  operand_bags ; operand_bags <-  opening_set ; ... ; p11 @probe('P11')` |
| `decision/options.py:440` `_context` | the registering decorator | False positive | fills `VIOLENCE_CONTEXT_READERS` (`options.py:437-446`), read at `:503`; probe: readers == roster members `crime, defence, duel, war` |
| `decision/options.py:450` `_war_context` | registered reader | False positive | `@_context("war")`; called through `VIOLENCE_CONTEXT_READERS[name](...)` at `options.py:503`; import check `:506-510` |
| `decision/options.py:457` `_crime_context` | registered reader | False positive | `@_context("crime")`; as `_war_context` |
| `decision/options.py:473` `_duel_context` | registered reader | False positive | `@_context("duel")`; as `_war_context` |
| `decision/options.py:482` `_defence_context` | registered reader | False positive | `@_context("defence")`; as `_war_context` |
| `decision/options.py:973` `_held_objects` | registered by decorator; registry read at runtime | False positive | `_held_objects <-  opening_set ; opening_set <- decision/__init__.py opening_set ; ... ; p11 @probe('P11')` |
| `decision/sheet.py:116` `DevelopmentSheet` | test-only today | Broken: wire (W1, carried by GO) | `development_space` has no game caller (`harness/play_surface.py` imports nothing from `sheet.py`); `11_GO_player_surface_contract_B.md` builds its `Situation`/`Offer` on it and its gate CLI seats a person through it |
| `decision/sheet.py:166` `take_ranked` | test-only today | Broken: wire (W1, carried by GO) | the control pick; `11_GO_player_surface_contract_B.md:241-242` seats `P` with it from `harness/play_surface` |
| `decision/sheet.py:65` `_frozen` | test-only today | Broken: wire (W1, carried by GO) | used by `creation_sheet`, `development_space`, `chronicle`, all test-only |
| `decision/sheet.py:74` `CreationRow` | test-only today | Broken: wire (W1, carried by GO) | `creation_sheet` read by `tests/test_cr20_attributes.py`, `test_g2_token.py`, `test_rem30_character_sheet.py` only |
| `epistemic.py:152` `_tenure_by_id` | private helper of code the driver reaches | False positive | `_tenure_by_id <-  _hold_tenure_ends ; _hold_tenure_ends <- loop/witness.py witness ; ... ; driver SeasonDriver` |
| `gaps.py:87` `Ineligible` | named by nothing | Dead: delete (batch D1) | no reference in `engine/`, `modules/`, `systems/`, `tools/`, `tests/`; refusal by ineligibility is the Event kind `FOLD_INELIGIBLE` (`loop/resolve.py:88,220`); own docstring `:92-105` says it has no callers |
| `loop/effects_army.py:34` `_army` | registered; its verbs never run | Broken: wire (W2, carried by VERBS) | `recruit`, `form_unit`, `assign_troops`, `disband_unit`, `discharge_troops`, `order_unit`: all in the corpus run's "foldable but never even attempted" |
| `loop/effects_army.py:45` `_payload` | registered; its verbs never run | Broken: wire (W2, carried by VERBS) | as `_army` (six army effects) |
| `loop/effects_combat.py:262` `raised_capability` | registered by decorator; registry read at runtime | False positive | `raised_capability <-  _eff_train ; _eff_train @effect_for('train')` |
| `loop/effects_combat.py:52` `_yielder` | registered by decorator; registry read at runtime | False positive | `_yielder <-  _eff_capture ; _eff_capture @effect_for('capture')` |
| `loop/effects_combat.py:686` `_siege` | registered; its verb never runs | Broken: wire (W2, carried by VERBS) | only user `_eff_march`; `march` never attempted in the corpus run |
| `loop/effects_founding.py:26` `_works_named` | registered; its verbs only refuse | Broken: wire (W2, carried by VERBS) | users `_eff_found`, `_eff_build`; both in "VERBS ONLY REFUSED" |
| `loop/effects_founding.py:45` `_made_by` | registered; its verbs only refuse | Broken: wire (W2, carried by VERBS) | as `_works_named` |
| `loop/effects_information.py:127` `_content_of` | registered by decorator; registry read at runtime | False positive | `_content_of <-  _eff_issue ; _eff_issue @effect_for('issue')` |
| `loop/effects_migration.py:74` `_arrival_only` | registered by decorator; registry read at runtime | False positive | `_arrival_only <-  _eff_migrate ; _eff_migrate @effect_for('migrate')` |
| `loop/matter.py:204` `_HeldBefore` | private helper of code the driver reaches | False positive | `_HeldBefore <-  _standing_crossings ; _standing_crossings <-  matter ; ... ; driver SeasonDriver` |
| `loop/predicates.py:260` `founded_office_id` | registered; its verb never runs | Broken: wire (W2, carried by VERBS) | `office_founded_by` <- `_req_establish` and `_eff_establish` (`effects_governance.py:231`); `establish` never attempted |
| `manifest/registry.py:238` `_check_step_declares` | private helper of code the driver reaches | False positive | `_check_step_declares <-  check_rows ; check_rows <- manifest/__init__.py check_rows ; ... ; driver SeasonDriver` |
| `manifest/registry.py:325` `_as_list` | private helper of code the driver reaches | False positive | `_as_list <-  _bound_verb_contests_it ; _bound_verb_contests_it <-  check_contest_prizes ; ... ; driver SeasonDriver` |
| `manifest/registry.py:387` `check_estimate_providers` | private helper of code the driver reaches | False positive | `check_estimate_providers <-  check_contest_prizes ; check_contest_prizes <- manifest/__init__.py check_contest_prizes ; ... ; driver SeasonDriver` |
| `manifest/registry.py:404` `_takes_module_entry` | private helper of code the driver reaches | False positive | `_takes_module_entry <-  check_graded_inquiries ; check_graded_inquiries <- manifest/__init__.py check_graded_inquiries ; ... ; driver SeasonDriver` |
| `manifest/registry.py:518` `_bound_verb_contests_it` | private helper of code the driver reaches | False positive | `_bound_verb_contests_it <-  check_contest_prizes ; check_contest_prizes <- manifest/__init__.py check_contest_prizes ; ... ; driver SeasonDriver` |
| `manifest/registry.py:534` `_graded_verb_emits_it` | private helper of code the driver reaches | False positive | `_graded_verb_emits_it <-  check_inquiry_modules ; check_inquiry_modules <- manifest/__init__.py check_inquiry_modules ; ... ; driver SeasonDriver` |
| `manifest/registry.py:54` `_contracts` | private helper of code the driver reaches | False positive | `_contracts <-  resolve ; resolve <- manifest/__init__.py resolve ; ... ; driver resolvable_verbs` |
| `queries/cache.py:71` `TenureIndex` | reached by `globals()` roster dispatch | False positive | `tenure_index` <- `epistemic._ch_document_key` (`:537`), `_ch_witness_key` (`:559`); `CHANNEL_PREDICATES` is built by `globals().get(f"_ch_{c}")` (`epistemic.py:698`), read at `:837,1073` |
| `queries/cache.py:86` `_build_tenure_index` | reached by `globals()` roster dispatch | False positive | as `TenureIndex` |
| `queries/faction_q.py:225` `_check_sheet_keys` | loader refusal run at import | False positive | `_check_sheet_keys <- queries/faction_q.py module stmt L245` |
| `queries/person_q.py:288` `_kind_engages` | private helper of code the driver reaches | False positive | `_kind_engages <-  deed_doers ; deed_doers <- queries/world_q.py _goal_referents ; ... ; driver SeasonDriver` |
| `queries/person_q.py:380` `_paired_weight` | private helper of code the driver reaches | False positive | `_paired_weight <-  paired_deed_term ; paired_deed_term <- queries/world_q.py attention_key ; ... ; driver SeasonDriver` |
| `queries/person_q.py:746` `_affiliations_violated_by` | private helper of code the driver reaches | False positive | `_affiliations_violated_by <-  elements_violated_by ; elements_violated_by <- loop/resolve.py _scar_witnesses ; ... ; driver SeasonDriver` |
| `queries/world_q.py:1080` `own_purview` | private helper of code the driver reaches | False positive | `own_purview <-  attention_key ; attention_key <-  questions_for ; ... ; driver SeasonDriver` |
| `queries/world_q.py:1208` `_site_rungs` | private helper of code the driver reaches | False positive | `_site_rungs <-  produce_input ; produce_input <- loop/matter.py matter ; ... ; driver SeasonDriver` |
| `queries/world_q.py:1375` `_larder_parts` | private helper of code the driver reaches | False positive | `_larder_parts <-  subsist_input ; subsist_input <- loop/matter.py matter ; ... ; driver SeasonDriver` |
| `queries/world_q.py:1433` `_draw_dict` | reading of an instrument (harness entry) | False positive | `_draw_dict <-  subsistence_draw ; subsistence_draw <- harness/populated.py census ; ... ; harness/populated.py main` |
| `queries/world_q.py:1439` `_draw_record` | registered by decorator; registry read at runtime | False positive | `_draw_record <-  under_input ; under_input <-  demanded ; ... ; f10 @probe('F10')` |
| `queries/world_q.py:1590` `_creating_act` | private helper of code the driver reaches | False positive | `_creating_act <-  issuing_seat ; issuing_seat <-  admits_audience ; ... ; driver SeasonDriver` |
| `queries/world_q.py:1746` `_refuse_two_residences` | private helper of code the driver reaches | False positive | `_refuse_two_residences <-  residence_of ; residence_of <-  has_room ; ... ; driver SeasonDriver` |
| `queries/world_q.py:1755` `lives_in` | registered by decorator; registry read at runtime | False positive | `lives_in <-  kit_of ; kit_of <- seam/wrappers/combat.py combat_input ; ... ; resolve @provider('contest', _PROVIDER)` |
| `queries/world_q.py:256` `_is_person_id` | private helper of code the driver reaches | False positive | `_is_person_id <-  sittings_before ; sittings_before <-  questions_for ; ... ; driver SeasonDriver` |
| `queries/world_q.py:2609` `EndingReached` | private helper of code the driver reaches | False positive | `EndingReached <-  endings_reached ; endings_reached <- loop/driver.py SeasonDriver ; driver SeasonDriver` |
| `queries/world_q.py:2675` `_ending_edges` | private helper of code the driver reaches | False positive | `_ending_edges <-  endings_reached ; endings_reached <- loop/driver.py SeasonDriver ; driver SeasonDriver` |
| `queries/world_q.py:2701` `_opened_by_acts` | private helper of code the driver reaches | False positive | `_opened_by_acts <-  endings_reached ; endings_reached <- loop/driver.py SeasonDriver ; driver SeasonDriver` |
| `queries/world_q.py:2868` `_goal_referents` | private helper of code the driver reaches | False positive | `_goal_referents <-  goal_referents ; goal_referents <-  questions_for ; ... ; driver SeasonDriver` |
| `queries/world_q.py:2900` `current_stage` | private helper of code the driver reaches | False positive | `current_stage <-  open_stages ; open_stages <-  attention_key ; ... ; driver SeasonDriver` |
| `queries/world_q.py:2949` `_aim_held_by_org_member` | private helper of code the driver reaches | False positive | `_aim_held_by_org_member <-  AIM_RULES ; AIM_RULES <-  _aim_rule ; ... ; driver SeasonDriver` |
| `queries/world_q.py:2965` `_aim_rule` | private helper of code the driver reaches | False positive | `_aim_rule <-  aim_state ; aim_state <-  questions_for ; ... ; driver SeasonDriver` |
| `queries/world_q.py:2974` `check_aim_rules` | loader refusal run at import | False positive | `check_aim_rules <- queries/world_q.py module stmt L2983` |
| `queries/world_q.py:3013` `engaged_poles` | private helper of code the driver reaches | False positive | `engaged_poles <-  opinion_of ; opinion_of <-  opinion_referents ; ... ; driver SeasonDriver` |
| `queries/world_q.py:3172` `_heir_title_holders` | roster-keyed reader table, called by the play surface | False positive | `_TIE_READERS[tie](w, p)` at `world_q.py:3227` in `continuations` <- `harness/play_surface.py:80,95`; `check_continuation_ties()` at `:3210` closes the roster against the table at import |
| `queries/world_q.py:3184` `_sworn_retainers` | roster-keyed reader table, called by the play surface | False positive | as `_heir_title_holders` |
| `queries/world_q.py:3512` `_top_arms` | registered by decorator; registry read at runtime | False positive | `_top_arms <-  kit_of ; kit_of <- seam/wrappers/combat.py combat_input ; ... ; resolve @provider('contest', _PROVIDER)` |
| `queries/world_q.py:362` `_docketing_ref` | private helper of code the driver reaches | False positive | `_docketing_ref <-  lapsing_items ; lapsing_items <- loop/calendar.py calendar ; ... ; driver SeasonDriver` |
| `queries/world_q.py:372` `docketed_by` | private helper of code the driver reaches | False positive | `docketed_by <-  docket_question ; docket_question <-  questions_for ; ... ; driver SeasonDriver` |
| `queries/world_q.py:3753` `open_stages` | private helper of code the driver reaches | False positive | `open_stages <-  attention_key ; attention_key <-  questions_for ; ... ; driver SeasonDriver` |
| `queries/world_q.py:3765` `stage_referents` | private helper of code the driver reaches | False positive | `stage_referents <-  questions_for ; questions_for <- loop/driver.py SeasonDriver ; driver SeasonDriver` |
| `queries/world_q.py:4364` `_person_or_refuse` | helper of a client read nothing calls | Dead: delete (batch D2) | `projection`/`witnessed` are imported by `tests/test_person_projection.py` only; superseded by the ledger-only reading in `11_GO_player_surface_contract_B.md` §3-§4 |
| `queries/world_q.py:4410` `PersonProjection` | record of a client read nothing calls | Dead: delete (batch D2) | as `_person_or_refuse`; no harness, play surface, tool or plan names it |
| `queries/world_q.py:4789` `_claimed_seat` | kind-keyed reader table of an instrument reading | False positive | `_MATTER.get(e.kind)` at `world_q.py:5036` in `_content_matter` <- `flows_in` <- `harness/strife.py`; `check_strife_openers(...)` at `:4841` checks the kinds at import |
| `queries/world_q.py:4798` `_petitioned_matter` | kind-keyed reader table of an instrument reading | False positive | as `_claimed_seat` |
| `queries/world_q.py:4820` `check_strife_openers` | loader refusal run at import | False positive | `check_strife_openers <- queries/world_q.py module stmt L4841` |
| `queries/world_q.py:4896` `flow_capacity` | reading of an instrument (harness entry) | False positive | `flow_capacity <-  presented ; presented <- harness/strife.py strands_block ; ... ; harness/strife.py main` |
| `queries/world_q.py:4938` `Flows` | reading of an instrument (harness entry) | False positive | `Flows <-  flows_in ; flows_in <- harness/strife.py strands_block ; ... ; harness/strife.py main` |
| `queries/world_q.py:4943` `_StrifeReading` | private helper of code the driver reaches | False positive | `_StrifeReading <-  flow_stakes ; flow_stakes <-  questions_for ; ... ; driver SeasonDriver` |
| `queries/world_q.py:5002` `_move_referents` | reading of an instrument (harness entry) | False positive | `_move_referents <-  flows_in ; flows_in <- harness/strife.py strands_block ; ... ; harness/strife.py main` |
| `queries/world_q.py:5033` `_content_matter` | reading of an instrument (harness entry) | False positive | `_content_matter <-  flows_in ; flows_in <- harness/strife.py strands_block ; ... ; harness/strife.py main` |
| `queries/world_q.py:5040` `_parents` | private helper of code the driver reaches | False positive | `_parents <-  _attach ; _attach <-  flows_known ; ... ; driver SeasonDriver` |
| `queries/world_q.py:5045` `_Chain` | private helper of code the driver reaches | False positive | `_Chain <-  _attach ; _attach <-  flows_known ; ... ; driver SeasonDriver` |
| `queries/world_q.py:5068` `_links` | private helper of code the driver reaches | False positive | `_links <-  _attach ; _attach <-  flows_known ; ... ; driver SeasonDriver` |
| `queries/world_q.py:5094` `_attach` | private helper of code the driver reaches | False positive | `_attach <-  flows_known ; flows_known <-  flow_stakes ; ... ; driver SeasonDriver` |
| `queries/world_q.py:5115` `_move_place` | private helper of code the driver reaches | False positive | `_move_place <-  _strand_of ; _strand_of <-  flows_known ; ... ; driver SeasonDriver` |
| `queries/world_q.py:5120` `_strand_of` | private helper of code the driver reaches | False positive | `_strand_of <-  flows_known ; flows_known <-  flow_stakes ; ... ; driver SeasonDriver` |
| `queries/world_q.py:5128` `default_terminal` | reading of an instrument (harness entry) | False positive | `default_terminal <-  flows_in ; flows_in <- harness/strife.py strands_block ; ... ; harness/strife.py main` |
| `queries/world_q.py:5158` `_concluded` | private helper of code the driver reaches | False positive | `_concluded <-  concluded_known ; concluded_known <-  flow_stakes ; ... ; driver SeasonDriver` |
| `queries/world_q.py:5233` `_eras` | reading of an instrument (harness entry) | False positive | `_eras <-  flows_in ; flows_in <- harness/strife.py strands_block ; ... ; harness/strife.py main` |
| `queries/world_q.py:5255` `open_era` | reading of an instrument (harness entry) | False positive | `open_era <-  presented ; presented <- harness/strife.py strands_block ; ... ; harness/strife.py main` |
| `queries/world_q.py:5260` `slot_rank` | reading of an instrument (harness entry) | False positive | `slot_rank <-  presented ; presented <- harness/strife.py strands_block ; ... ; harness/strife.py main` |
| `queries/world_q.py:5344` `_strains` | private helper of code the driver reaches | False positive | `_strains <-  commensurate ; commensurate <- loop/witness.py _credit ; ... ; driver SeasonDriver` |
| `queries/world_q.py:5438` `check_restraint_kinds` | loader refusal run at import | False positive | `check_restraint_kinds <- queries/world_q.py module stmt L5455` |
| `queries/world_q.py:5458` `_ledger_in_order` | private helper of code the driver reaches | False positive | `_ledger_in_order <-  _known_moves ; _known_moves <-  flows_known ; ... ; driver SeasonDriver` |
| `queries/world_q.py:5487` `open_referents_known` | private helper of code the driver reaches | False positive | `open_referents_known <-  concluded_known ; concluded_known <-  flow_stakes ; ... ; driver SeasonDriver` |
| `queries/world_q.py:5508` `concluded_known` | private helper of code the driver reaches | False positive | `concluded_known <-  flow_stakes ; flow_stakes <-  questions_for ; ... ; driver SeasonDriver` |
| `seam/contest.py:94` `_returned` | private helper of code the driver reaches | False positive | `_returned <-  contest ; contest <- seam/__init__.py contest ; ... ; driver SeasonDriver` |
| `seam/wrappers/combat.py:124` `load_error` | test-support on a live probe | False positive | `_probe` is live (`engine()` at `:170`); `load_error` is the skip reason in five test files; module docstring `:31-32` declares it |
| `seam/wrappers/combat.py:187` `_cause_record` | registered by decorator; registry read at runtime | False positive | `_cause_record <-  resolve ; resolve @provider('contest', _PROVIDER)` |
| `seam/wrappers/mass_battle.py:192` `_order_of_battle` | registered by decorator; registry read at runtime | False positive | `_order_of_battle <-  field_input ; field_input <-  resolve ; resolve @provider('contest', _PROVIDER)` |
| `seam/wrappers/mass_battle.py:217` `_standing_order` | registered by decorator; registry read at runtime | False positive | `_standing_order <-  field_input ; field_input <-  resolve ; resolve @provider('contest', _PROVIDER)` |
| `seam/wrappers/mass_battle.py:282` `_causing_act` | registered by decorator; registry read at runtime | False positive | `_causing_act <-  resolve ; resolve @provider('contest', _PROVIDER)` |
| `seam/wrappers/mass_battle.py:289` `_seat_treasury` | registered by decorator; registry read at runtime | False positive | `_seat_treasury <-  resolve ; resolve @provider('contest', _PROVIDER)` |
| `seam/wrappers/mass_battle.py:298` `_defender_treasury` | registered by decorator; registry read at runtime | False positive | `_defender_treasury <-  resolve ; resolve @provider('contest', _PROVIDER)` |
| `seam/wrappers/mass_battle.py:323` `_fielded_by` | registered by decorator; registry read at runtime | False positive | `_fielded_by <-  resolve ; resolve @provider('contest', _PROVIDER)` |
| `seam/wrappers/mass_battle.py:331` `_fed` | registered by decorator; registry read at runtime | False positive | `_fed <-  resolve ; resolve @provider('contest', _PROVIDER)` |
| `seam/wrappers/pool.py:54` `_held_attribute` | private helper of code the driver reaches | False positive | `_held_attribute <-  _authored_attribute ; _authored_attribute <-  faculty ; ... ; driver SeasonDriver` |
| `seam/wrappers/sigma.py:242` `_composed_obstacle` | private helper of code the driver reaches | False positive | `_composed_obstacle <-  _odds_of_input ; _odds_of_input <-  odds_of ; ... ; driver SeasonDriver` |
| `seam/wrappers/sigma.py:250` `_odds_of_input` | private helper of code the driver reaches | False positive | `_odds_of_input <-  odds_of ; odds_of <-  believed_chance ; ... ; driver SeasonDriver` |
| `seam/wrappers/sigma.py:331` `_estimated` | private helper of code the driver reaches | False positive | `_estimated <-  odds_of ; odds_of <-  believed_chance ; ... ; driver SeasonDriver` |
| `state/attribution.py:156` `_cover_for` | private helper of code the driver reaches | False positive | `_cover_for <-  anchor_of ; anchor_of <- state/world.py World ; ... ; driver SeasonDriver` |
| `state/attribution.py:220` `_a_stage_unmatured` | private helper of code the driver reaches | False positive | `_a_stage_unmatured <-  live_cover ; live_cover <-  cover_at_logging ; ... ; driver SeasonDriver` |
| `state/gate.py:1062` `_committed_to` | private helper of code the driver reaches | False positive | `_committed_to <-  may_cede ; may_cede <-  tenure_write_basis ; ... ; driver SeasonDriver` |
| `state/gate.py:1119` `_closes` | private helper of code the driver reaches | False positive | `_closes <-  refuse_unauthored ; refuse_unauthored <- state/world.py World ; ... ; driver SeasonDriver` |
| `state/gate.py:1808` `_nothing` | registered by decorator; registry read at runtime | False positive | `_nothing <-  NO_CHANGE ; NO_CHANGE <- loop/effects_army.py _eff_recruit ; _eff_recruit @effect_for('recruit')` |
| `state/gate.py:370` `_seat_grants` | private helper of code the driver reaches | False positive | `_seat_grants <-  may_determine ; may_determine <- queries/world_q.py WorldReader ; ... ; driver SeasonDriver` |
| `state/gate.py:464` `_ground_reaches` | private helper of code the driver reaches | False positive | `_ground_reaches <-  purview_reaches ; purview_reaches <- queries/world_q.py WorldReader ; ... ; driver SeasonDriver` |
| `state/gate.py:657` `check_revocation_disposal` | loader refusal run at import | False positive | `check_revocation_disposal <- state/gate.py module stmt L681` |
| `state/gate.py:705` `check_filled_by` | loader refusal run at import | False positive | `check_filled_by <- state/gate.py module stmt L729` |
| `state/gate.py:732` `filled_by` | private helper of code the driver reaches | False positive | `filled_by <-  may_fill ; may_fill <- queries/world_q.py vacancies ; ... ; driver SeasonDriver` |
| `state/world.py:169` `_snapshot_fields` | private helper of code the driver reaches | False positive | `_snapshot_fields <-  World ; World <- loop/driver.py SeasonDriver ; driver SeasonDriver` |
| `state/world.py:174` `_TenureSnap` | private helper of code the driver reaches | False positive | `_TenureSnap <-  World ; World <- loop/driver.py SeasonDriver ; driver SeasonDriver` |
| `state/world.py:191` `_payload_holders` | private helper of code the driver reaches | False positive | `_payload_holders <-  World ; World <- loop/driver.py SeasonDriver ; driver SeasonDriver` |
| `state/world.py:255` `_str_bytes` | private helper of code the driver reaches | False positive | `_str_bytes <-  _encode_into ; _encode_into <-  _canonical ; ... ; driver SeasonDriver` |
| `state/world.py:260` `_object_head` | private helper of code the driver reaches | False positive | `_object_head <-  _encode_into ; _encode_into <-  _canonical ; ... ; driver SeasonDriver` |
| `state/world.py:271` `_encode_object` | private helper of code the driver reaches | False positive | `_encode_object <-  _encode_into ; _encode_into <-  _canonical ; ... ; driver SeasonDriver` |
| `state/world.py:279` `_encode_into` | private helper of code the driver reaches | False positive | `_encode_into <-  _canonical ; _canonical <-  World ; ... ; driver SeasonDriver` |
| `state/world.py:336` `_canonical` | private helper of code the driver reaches | False positive | `_canonical <-  World ; World <- loop/driver.py SeasonDriver ; driver SeasonDriver` |

## 4. Extension: what the census could not list

Every top-level name in the 74 partition files was followed upward the same way; 48 that are not C1 rows
reach only a test, a tool, a dynamic dispatch or nothing. Read at the site:

| name(s) | reading | decision | evidence |
|---|---|---|---|
| `world_q.py:4374 witnessed`, `:4434 projection` | the callable halves of F-C1A-01 | Dead: delete (D2) | imported by `tests/test_person_projection.py` only |
| `data/cast.py:408 defects` | a registry report with no caller, test or tool | Dead: delete (D1); its paren check moves into the loader as a refusal (W3) | run once: 3 rows, all unaffiliated NPCs (NPC-001, NPC-010, NPC-075) |
| `data/files.py:246 SEAM_DIR`, `:251 COMBAT_SEAM_PY` | constants nothing reads | Dead: delete (D1) | `grep -rn "COMBAT_SEAM_PY\|SEAM_DIR" engine tests tools` finds the two definitions and one comment |
| `state/world.py:166 _FIRST`, `_SECOND` | constants nothing reads | Dead: delete (D1) | one line; `_itemgetter` (`:41`) has no other use |
| `person_q.py:637 violated_pursuits`, `:657 violated_affiliations` | test-only twins of a live pair | Dead: delete (D3) | 8 uses, all in `tests/test_h11_affiliation_scar.py`; live path is `elements_violated_by` (`:754`) + `broken_by` (`:770`) from `loop/resolve.py` |
| `faction_q.py:189 superiors` | test-only | Dead: delete, **already decided** | `06_FA_hygiene.md:39`; not repeated in this lane's batches |
| `decision/sheet.py`: `creation_sheet`, `seat`, `development_space`, `Chronicle`, `chronicle`, `_LAW` | the rest of F-C1A-02 | Broken: wire (W1, carried by GO) | as the four listed rows |
| `decision/choose.py:281 beneficiary_of` and the `beneficiary:` column | F-C1A-04 | Broken: wire (W4) | `grep -rn "beneficiary_of\|\.beneficiary\b" engine/season --include=*.py` outside `tests/`: the definition and the loader |
| `world_q.py:2081 footprint`, `:2111 density`, `:2372 sovereign_fraction` | Layer 1 queries with no caller | Broken: reader owed; kept (F-C1A-05, §6) | `holonic_ARCHITECTURE.md:597-598`; `grep` finds no call outside tests |
| `world_q.py:2421 provinces_of` | ratified query, test-only | Broken: reader owed; kept | `world_q.py:2424` (the ruling it implements); `06_FA_audit_addendum_B.md:272, :510` |
| `world_q.py:5303 within` | strife reading, test-only (`test_strife_flows.py`) | False positive against deletion: part of the strife reading the WR strand proposals work on; no edit here [UNVERIFIED that a WR proposal calls it] | same family as `flows_in`, read by `harness/strife.py` |
| comment pointers, 9 sites | F-C1A-07 | Mislabelled: correct (C1) | proposal 02 lists old and new text |
| report functions and anchors a test calls: `tenure_kinds_without_an_opener`, `rows_without_a_producer`, `arrangements_without_a_disposal_opener`, `matrix_rows_without_a_field`, `assume_partition_row`, `_load_incompatible`, `ladder_error`, `package_modules`; constants `LADDER_RUNGS`, `PROVIDER`, `STATE_DIR`, `DEGREE_SWEEP_DIR`, `DRIVER_PY`, `DECISION_DIR`, `TEST_PY`, `PROBES_PY`, `HEADLESS_PY`, `MODULE_KINDS`, `_MODULE_FIELDS`, `MODULES` | a check whose executor is the test | False positive | the test asserts the report empty or scans the anchor; that test is the mechanism (`CLAUDE.md` §0.05) |
| `decision/options.py:1259 operands_for` | a two-line "first bag" shim over live `operand_bags` | False positive | 12 call sites in five test files; body is `bags[0] if bags else None` (`:1302-1303`) |
| `cache.tenure_index`, `cache.home_index`, `cast.load`, `goals.load`, `geography.load` | dynamic dispatch (§1) | False positive | `epistemic.py:449, :537, :559`; `data/__init__.py:55-57` |

Not examined, and left to the lanes that own them: registry keys (C3), event kinds (C4), hole-register
pointers (C5), record fields (C2), and rosters whose closed set has no loader refusal beyond the
`cast.faction` case above.

## 5. Evidence log

| what | how | outcome |
|---|---|---|
| reachability of the 187 rows | `c1a/reach6.py` (AST, resolved imports, upward search to a root) | driver 107 · registered 44 · import statement 15 · harness entry 9 · tests only 11 · nothing 1; every non-driver row then read at its site |
| extension | `c1a/ext2.py`, same search over every top-level name in 74 files | 48 names reaching a test, a tool, a dynamic dispatch or nothing; dispositions in §4 |
| registries | one `python -c` at `PYTHONHASHSEED=0` | `VIOLENCE_CONTEXT_READERS` keys == roster members `crime, defence, duel, war`; `EFFECTS` holds `recruit, assign_troops, march, build, issue, migrate, train, capture, establish, found, move`, all in `resolvable_verbs()`; `PROVIDERS` holds `contest` for `personal_combat`, `social_contest`, `mass_battle`, `estimate` for two, `inquiry` for `fieldwork`; `CHANNEL_PREDICATES` has five members |
| `cast.defects()` | one call | 3 rows, all `Independent (...)` |
| person names | `populated.build_realm(0)` | 83 persons, 83 named, none through `cast.name_of` |
| verbs that execute | **not re-run**: read from the CORE lane's `corpus_run` output of this session (`runs/CORE/corpus_run.txt`, 8 min wall) | 23 of 67 executed · 13 only refused · 30 never attempted · 1 with no predicate/effect |
| the nine | read from `runs/CORE/register_requirements.txt` | met 3 · partial 5 · not_met 1 (R-05) |
| comment pointers | regex over the partition for `file.py::symbol`, resolved against `git ls-files` | 700 pointers; 12 unresolved; 9 confirmed stale, 3 are artefacts of the pattern (a hyphenated label, two wrapped test names) |
| `pytest` | not run (brief) | — |

Not verified: that each VERBS proposal named in W2 makes its verb execute (the files were matched by the
verb's name, not read); that a WR proposal calls `world_q.within`.

## 6. For the orchestrator

1. **F-C1A-05 has no owner in the suite.** `footprint`, `density`, `sovereign_fraction` and `provinces_of`
   are Layer 1 or ratified readings with no caller. Ladder step 5: they are the faction-scale view's
   inputs, so the FA lane's strategic surface (`06_FA_playable_scenario.md`) is where a reader belongs;
   this lane did not write that reader, because choosing what a faction's view shows is FA's design. If FA
   declines them, the alternative is a Layer 1 edit, which a census may not make.
2. **W4 changes what NPCs choose** once its arm is switched on; it ships at the control and needs the
   CHAR lane's ranker proposals to absorb it (`02_CHAR_which_ground_moves_whom.md`).
3. **D2 depends on GO-B being accepted.** If `11_GO_player_surface_contract_B.md` is rejected, the
   projection is the only typed client read in the tree and D2 should be held.
