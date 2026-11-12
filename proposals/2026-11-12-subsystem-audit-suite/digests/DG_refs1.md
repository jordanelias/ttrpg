# Digest refs1
## Status: REFERENCE (a coverage digest; resolves nothing at runtime)

Lane: `references/` registries and ledgers (31 files assigned, in assignment order). Reader lists below come from one grep of `tools/ engine/ modules/ tests/valoria skills/ .github .githooks .claude systems godot` per file name, excluding `.claude/worktrees/` copies (a stale worktree `.claude/worktrees/agent-a737f996de1fa4752/` mirrors the whole tree and pollutes every grep).

### references/D10_INTEGRATION_GUIDE.md
- **What it is:** a 176-line how-to for two skills (valoria-simulator Mode A, valoria-mechanic-audit Mode B) on using `d10_success_probabilities.json`; undated, no author lane.
- **Status:** none stated. Reading: historical / stale (documents a skill integration, not a mechanism).
- **Bears on:** DICE, PROCESS.
- **Content that matters:**
  - States the table assumes 40% success per die (TN7 on d10), 20 trials x 20 successes, binomial CDF, 2-decimal rounding (:3, :69-71, :93).
  - Explicitly "does NOT account for 1s subtracting, chain bonuses, other modifier mechanics" (:94): the table models an older raw-count pool, not the live `d+sigma` / `degree_from_net` resolver (CLAUDE.md §5 names `degree_from_net` in `engine/dice_engine/dice_engine.py` as the live degree owner).
  - Cites SKILL.md line numbers (:21-22, :49 "lines 128-150", "lines 32-41") that cannot be checked here; the example tables (:123-130) use values like 5D/Ob1 = 0.92.
  - Location pointer says GitHub `main/references/d10_success_probabilities.json` (:167-174), a hand-maintained duplicate of the repo path.
- **Conflicts / stale:** `alias_registry.yaml:324-331` gives TN as `6 | 7 | 8` (variable), while this guide freezes TN7. No reader of the guide or the JSON found in `tools/ engine/ tests/valoria skills/` [one grep, zero hits]: orphaned reference.
- **Open items:** whether the 40%/TN7 model is still the oracle for any live resolver (the d10 pool model vs the d+sigma model) is not answered here.

### references/action_vocabulary.yaml
- **What it is:** a 54-line YAML roster of 25 performable domain-action verbs (`verbs:`), `status: provisional`, `blocked_on: ED-FA-0002`.
- **Status:** "STATUS: PROVISIONAL, NOT the authoritative domain-action registry (the `domain_actions` home is unbuilt)" (:8-9, :15). Reading: live-but-provisional data, orphaned from the engine.
- **Bears on:** FA, CORE.
- **Content that matters:**
  - Verb list (:24-54): military Muster/March/Fortify/Blockade/Conquest; governance Govern/Trade/Subsidy/Treaty/Diplomacy; intel Spy/Investigate/Counter-Intelligence; coercive Censure/Embargo/Outlawry/Excommunication/Active Inquisition/Church Seizure/Recognition Challenge/Succession Endorsement/War Authorisation; popular Piety Spread/Community Organising/Martial Governance.
  - Only reader found: `skills/valoria-vector-audit/scripts/vector_audit.py` (token_class `action`). Nothing in `engine/` or `modules/` reads it.
  - `source_note` (:21-23) says curated from `module_contracts.yaml` (ED-FA-0006 verb note, "conquest/muster/govern/uniques" wiring note).
  - Header (:11-14) distinguishes this verb roster (what a player SELECTS) from the `da.*` five-tag OUTCOME taxonomy "emitted Key types" in module_contracts: the Key framing is retired (ED-IN-0232).
- **Conflicts / stale:** the engine's own verb table is `engine/season/` `verb_table` (atomization_rules.yaml:117-119 names `verb_table` among the runtime registries); this 25-verb roster is a second, unconnected roster [UNVERIFIED which verbs the verb_table has]. Points at `references/vocab_history.md` (exists).
- **Open items:** ED-FA-0002 ("domain_actions home") open; `blocked_on` forward-dependency never closed.

### references/alias_registry.yaml
- **What it is:** a 685-line GENERATED mechanic-naming registry (canonical name -> abbreviations/aliases/legacy), built by `tools/vocab_store.py --build` from `references/definitions/vocab_source.yaml` key `registers.alias_registry` (ED-IN-0078).
- **Status:** "GENERATED ... DO NOT EDIT BY HAND" (:1-2); `version: 2`. Reading: live as a vocabulary generated artifact, but its CONTENT is largely pre-v40 mechanics.
- **Bears on:** CHAR, DICE, FA, WR, PROCESS.
- **Content that matters:**
  - Readers: `tools/vocab_store.py`, `tools/export_names.py`, `tools/validate_ed_citations.py`, `tools/ci_naming_check.py`, `engine/substrate/descriptors.py`, `engine/substrate/names.py`, `engine/tests/test_knots_ed912.py`, `tests/valoria/test_conviction_roster_single_owner.py`.
  - Core attributes are seven, range 1-7: Agility, Attunement, Cognition, Endurance, Presence, Spirit, Strength (:21-56). Derived: Health, Stamina, Coherence 10->0, Intelligibility 10->0, Composure, Focus 1-5+, Truth 0-5 (renamed from Certainty, consolidates Piety Track, ED-IN-0075; "players see qualitative bands only, never the number", :102-107), Momentum 0-4.
  - Overwhelming = margin (net - Ob) >= 3 and Partial = margin in [0,1) (Jordan ruling 2026-08-14, ED-IN-0187) at :350-362; TN values 6|7|8 (:331).
  - Mass-battle derived stat formulas (:272-322): Command = ceil((Presence+Cognition)/2); Health per Size = min(Discipline, Command) + DR; Total Health = Size x H; Power replaced Combat Power (PP-232); Size at 0 = unit destroyed.
  - Church Influence milestones 40/55/60/65/80/100 with Mass Seizure P = ((CI-60)/40)^3.3 per season (:160-170); `thread_pool_score = Thread Sensitivity/10`; Locking/Dissolution/Mending need TS 50+, Past-Oriented Pulling TS 70+ (:113-126, :458-472).
- **Conflicts / stale:** `substrate_aliases` (:622-665) defines `key`/`memory_entry` aliases for the RETIRED Key substrate (ED-IN-0232, PP-687); header (:9) says `tools/valoria_collator.py` does not exist so "nothing performs its checks"; `Public Instability` is "replaced by Peninsular Strain (ED-744), now Turmoil" (:189-190); `deprecated_abbreviations` cite `deprecated/tests/...` (:607), a tree that no longer exists; `tc` collision still "resolved_term_partial_corpus" (:580).
- **Open items:** `unresolved: {}` (:596) is empty; the "corpus rename (ED-IN-0075 staged sweep)" of Certainty->Truth is stated pending (:105).

### references/atomization_rules.yaml
- **What it is:** the 388-line size-cap POLICY (`version: 1`, established 2026-04-18): first-match-wins `policies:` rows of `match` globs with `max_tokens`/`on_exceed`.
- **Status:** none; reads as live policy for a process gate. Readers: `tools/compliance_check.py` (loads `policies:` only), `tools/ci_register_size_check.py` (raw-text line scan of three rows' `max_tokens`), `tools/ci_common.py`, `tools/ci_claim_provenance_check.py`.
- **Bears on:** PROCESS.
- **Content that matters:**
  - `defaults:` block (:9-22) has NO reader (`compliance_check.py` reads `policies:` only; comment :13), so `auto_fix_on_violation: true` and all `*_tokens` defaults are inert.
  - `force_skeleton_routing_for_design_docs: false` and sequential-parts-at-15k replace the index+infill default (RULED 2026-07-26, :16-19).
  - Explicit caps: HANDOFF.md 4000 flag_for_split (:134), `registers/handoffs/*.md` 20000 (:152), `canonical_sources.yaml` 14000 (:256), `module_contracts.yaml` 32000 with `on_exceed: warn_only` (:260-263), `npc_registry.yaml` 15000 warn_only (:292), audit files 30000 (:372).
  - Both catch-alls (`**/*.md`, `**/*.yaml`) have `max_tokens` deleted (ED-IN-0220, :379-388); only per-file rows remain.
- **Conflicts / stale:** many rows name dead or renamed trees: `engine/params/*` (dissolved, CLAUDE.md §3; rows :176-204, :287), `arcs/registers/arc_register.md` (:209), `deprecated/**` and `deprecated/archives/**` (:271-279; no `deprecated/` tree exists per CLAUDE.md §1), `audit/**/*.md` (:372; the corpus is now `.audit/`), `references/file_index.md`, `references/design_registry.yaml` (:248-254), `references/proper_noun_triage_round2.yaml`, `references/mechanical_terms_index.md` (:297-306; none of these is in `ls references`), `tools/observability` (retired). Duplicate `references/propagation_map.md` rows (:168 max 10000 AND :230 max 5000 `tables_vs_log`; first match wins, so :168 governs) and duplicate `engine/params/threadwork_superseded.md` rows (:197, :287). The history file confirms `on_exceed: warn_only` is a no-op that grades as a blocking error (`compliance_check.py:179`, recorded 2026-07-29).
- **Open items:** the `warn_only` mis-grading (12 files) was "FILED, NOT FIXED"; `references/splits/params_board_game_split.yaml` is a referenced file for a dissolved tree.

### references/atomization_rules_history.md
- **What it is:** 334-line verbatim HISTORY supplement of `atomization_rules.yaml` comments (B-X split, Jordan 2026-10-06: "extract all edit histories/discussion from .yaml files in references and just make those a supplement").
- **Status:** none; reading: historical, reference only.
- **Bears on:** PROCESS.
- **Content that matters:**
  - Only two readers touch the YAML: `compliance_check.py` (`yaml.safe_load`) and `ci_register_size_check.py` `yaml_max_tokens()` (line scan of `- match:`/`max_tokens:`); no program reads `note` keys (:23-26).
  - Records that the `warn_only` token is a NO-OP: `compliance_check.py:179` reads `severity = 'warn' if on_exceed.startswith('flag') else 'error'` (:244).
  - The ED-IN-0221 lesson: "CUT AT THE FINEST GRANULARITY THE DOCUMENT ALREADY LABELS"; 99,491 tokens of closed narrative moved, zero lines lost (:150-165). HANDOFF_IN.md was ~130k vs 20k cap, root HANDOFF ~16.6k vs 4k (:172).
  - Catch-all deletion measurement: 116 violators, median 20,941 tokens, max 196,463 (:310-318); the §0.1 pt 5 predicate justified deleting an advisory-only gate.
  - Records the dead-scope sweep that "manufactured a fresh dead row": `restructure_ledger.md:1257-1258` records both `designs/audit/` and `audit/` spellings as `FORK:c451bcb` (:270-287), a worked example that `pathres.resolve()`-style prefix matching misleads.
- **Conflicts / stale:** the `defaults:` key `auto_fix_on_violation` note says it is honoured at commit time by `pre_commit_gate_mutating` (:46-53), but the YAML header says its auto-fix half was excised.
- **Open items:** the two gates "already disagree on the register cap (15,000 in the gate vs 10,000 here; ED-IN-0159 §1.8, plan step G6)" (:301), unresolved here.

### references/canonical_sources.yaml
- **What it is:** 248-line index of which docs are authoritative per system, with machine-written `canonical_sha__*` git-blob pins; "Entries here supersede any other documentation they conflict with" (:4).
- **Status:** none; mixed. Readers: `tools/freshness_gate.py`, `ci_generation_consistency.py`, `canon_coverage_check.py`, `broken_dependency_checker.py`, `export_engine_params.py`, `ci_co_file_checker.py`, `build_identifier_census.py`, `ci_register_size_check.py`, `engine/season/goals.yaml`, `tests/valoria/test_flow_skeletons.py`, vector_audit/gen_audit.
- **Bears on:** PROCESS, FA, WR, SE, PC.
- **Content that matters:**
  - About 25 `systems:` entries are bare `archived: ".designs/ - quarantined 2026-09-16 ... Canon for this system is the code"` (e.g. :77, :85, :87, :94...), so the index no longer names a design doc for core_engine, threadwork, factions, victory, mass_combat, scale_transitions, faction_layer, military_layer, etc.
  - Only two pinned design docs survive: `systems/settlements/valoria_geography_v30.yaml` and `valoria_map_v30.svg` (:89-92), plus `references/throughlines_meta.md` + infill (:121-124), `canon/philosophy/06_operations.md`, `04_being_persistence.md` (:132-136), `references/module_contracts.yaml` (:243-247).
  - Combat: `resolution_engine: "modules/combat/"`, "CANONICAL combat_engine_v1 (ratified ED-900; re-ratified ED-904)" (:80-81).
  - Struck canon: VTM (ED-706), Cultural Reformation PP-650 (ED-707), and ALL faction-specific victory paths struck by GD-1 (canon/02 §B, 2026-05-17); sole victory is Peninsular Sovereignty, 11/15 territories sustained 2 seasons (:26-28).
  - `key_substrate` and `key_type_registry` still read `status: canonical` (:161-166) though the Key substrate is RETIRED (ED-IN-0232).
- **Conflicts / stale:** `systems/ui/reference/valoria_ui_ux_v4_1.md` (:237) and `systems/settlements/valoria_geography_v30.yaml` pins: CLAUDE.md §3 says `systems/` holds no `.md` at all, so the `ui_ux` path (:237) is a dead pin [UNVERIFIED by ls]. `holonic_container_doctrine`, `propagation_spec`, `conviction_taxonomy`, `faction_behavior`, `articulation_layer` (:167-187) are "canonical" with no path. `module_contracts` note says "25 extracted + 2 stubs" (:247).
- **Open items:** `knots_unified.contradictions_pending` TIER-DRIFT-001, COMPOSURE-DRIFT-001, TRUNC-DRIFT-001 (:57-60) never closed here; ED-1051 `engine_clock` home doc "open, awaiting Jordan" (:172).

### references/canonical_sources_history.md
- **What it is:** 145-line verbatim HISTORY of comments removed from `canonical_sources.yaml` (B-X split, 2026-10-06).
- **Status:** none; reading: historical.
- **Bears on:** SE, FA, PC, SC, PROCESS.
- **Content that matters:**
  - Names the raw-text scanners that depend on comments: `broken_dependency_checker.py` `extract_file_refs`, `vector_audit.py` `_MD_PATH_RE`, `gen_audit.py` `_mentioned_in_canonical_sources_raw`, `test_flow_skeletons.py` (:22-29).
  - Combat resolver ratification trail (ED-900/901/902; ED-PC-0056 consolidated five docs into combat_reference_v1; modules wrapper/systems/core/config/combatant/geometry/tradition) (:49-53).
  - Social-debate SHA pins 2026-07-01, Contest Stage 2 / Gate B; ED-1055..1061 list (Panel aggregation = weighted-by-standing ED-1057, Panel reachability via Guild Arbitration rebind ED-1059, Terminal Doubt banded/tally split ED-1060, Guilds boost context-derived-from-venue ED-1061) (:61-70).
  - LPS (Legitimacy / Public Support) per-settlement re-grain 2026-05-30: faction Mandate = size-weighted saturating aggregate, W = base(Type)+Prosperity+FacilityTier, K=6; "Mandate x20 meter NOT a defect" because multipliers are per-system (Treasury x100, Reputation x15, Discipline x10, Legitimacy x20) (:134-138).
  - F-RESID: four bare-stat Unique Actions (Royal Decree, Excommunication, Private Collection, Economic Leverage) migrated to the d+sigma resolver, D = max(1,(O-1)*2) (:139).
- **Conflicts / stale:** all the LPS/Mandate content describes pre-v40 design docs now in `.designs/`; "Public Support -> Popular Support" term change 2026-06-04 (:144).
- **Open items:** F-RESID "Hafenmark Doctrine flagged, not migrated" (:139); the NERS-audit "2 Jordan intent/data confirmations (hugeness-premium, Weight redundancy)" (:140).

### references/censured_vocabulary.yaml
- **What it is:** 188-line GENERATED censure list (16 terms with reason, replacement, date, authority, residual counts), built by `tools/vocab_store.py --build` from `vocab_source.yaml` key `registers.censured_vocabulary`.
- **Status:** "GENERATED ... DO NOT EDIT BY HAND" (:1-2). Reading: live as a naming-gate input; residual counts are a 2026-04-30 / 2026-05-08 snapshot (stale).
- **Bears on:** PROCESS, CHAR, SC, FA, MB.
- **Content that matters:**
  - Readers: `tools/vocab_store.py`, `tools/validate_ed_citations.py`, `tools/ci_naming_check.py`.
  - Struck: VTM (ED-706), Cultural Reformation (ED-707), Niflhel-as-faction (ED-764, 23 residuals), Coup Counter -> Löwenritter Graduated Autonomy (ED-781, per-site not 1:1) (:17-129).
  - Silo-isolation renames for the contest: "Conviction Track (contest-context)" -> **Persuasion Track** (0-10 debate score), "Initiative (contest-context)" -> **First to Speak**, territory "Conviction Track" -> Piety Track (PT 0-5), CT and CV abbreviations deprecated (:142-188). 89 residual files for Conviction Track at the audit.
  - Bare `GM` censured (PP-691): "There is no GM -- the engine handles all resolution" (:130-141).
  - CV entry says the territorial track "was absorbed into the affiliation roster (engine/season/rosters.yaml)" (:173-174), the one live-engine pointer in the file.
- **Conflicts / stale:** `alias_registry.yaml:196-199` still lists `conviction_track` with abbreviation `CT` and range 0-10 as canonical under `debate_system`, directly contradicting the censure of CT/Conviction Track for the contest. Residual-concentration paths name dissolved trees (`designs/provincial/`, `engine/params/bg/`). Dates are partial placeholders (`2026-02-XX`, `2026-XX-XX`).
- **Open items:** Rendering Stability residual in `canon/02_foundations_amendment_leap_mechanism.md` "possibly intentional retention; verify before action" (:83-84).

### references/ci_checks_registry.yaml
- **What it is:** 471-line registry of CI/validator tools: `ci_checks:` rows (path, level, subject, posture, role, ci_job, notes), `advisory_only:`, empty `known_issues: []`; `version: 1, generated: 2026-07-11`.
- **Status:** none; reading: live. Readers: `tools/broken_dependency_checker.py` (`_parse_ci_checks_entries`, `check_ci_registry_coverage`, joins `path:` and `ci_job:` to the tree and `.github/workflows/valoria-ci.yml` both ways), `ci_naming_check.py`, `valoria_local.py`, `currency_consistency_check.py`, `engine/season/tests/test_season_shape.py`, `tests/valoria/test_wiring_validation.py`.
- **Bears on:** PROCESS, CORE, MB, CHAR.
- **Content that matters:**
  - Defines two axes: `level:` (1/2/3/5; level 4 retired 2026-08-12) and `subject:` (game / compliance / verification) with postures grow/harden/cap; "NOTHING IN THIS FILE IS `game`" (:24-27) yet two rows are tagged `subject: game` (`export_battle_orders.py` :314, `export_npc_roster.py` :322), a self-contradiction.
  - Game-bearing exporters that feed the engine: `export_engine_params.py` (combat_engine_v1.json vs `modules/combat/config.py`), `export_game_constants.py` (writer half of the ttrpg -> valoria-game constants bridge; "PAIRS ARE HAND-CONFIRMED, NEVER NAME-MATCHED"; a DIVERGENCES list of real model disagreements), `export_descriptors.py` (sole runtime reader `engine/substrate/descriptors.py`), `export_names.py` (feeds `engine/season/rosters.yaml` `from_names:` factions roster), `export_composition.py` (validator of `module_contracts.yaml`, imports and resolves every target), `export_battle_orders.py`, `export_npc_roster.py` (re-derives `engine/season/npcs.yaml` from `cases/NPC*.yaml`, reports rather than fails on hand corrections).
  - `ci_golden_modes_check.py`: CI-only, ~275 s; the two legacy grid MB modes are pinned by nothing since 2026-11-04 (both known-red, ED-MB-0061) (:138).
  - `lanchester_signature.py` is REPORT-ONLY because "the repaired instrument legitimately FAILS (melee fits p~3.20 against a <=1.4 linear bar)": an open MB engine finding held for "plan-v2 fork #2 (two incompatible 2:1 targets)" (:146).
  - `m1_acceptance.py` row names a LOSS: after review_core retirement "NO GAME-FACING SIGNAL CAN NOW FAIL CI ON REGRESSION" (:413-421); `arms.py` is the n-seed two-arm comparison for `field_casualty_model` (`total` vs `scaled_by_degree`, H-148, ED-IN-0279 clause a), deliberately not in CI (:378-396).
- **Conflicts / stale:** no row for `tools/export_sim_params.py`, which is enforced via `tests/valoria/test_export_sim_params.py` (history file :258). `compliance_check.py` role cites `atomization_rules.yaml` thresholds, which name many dead trees. `ci_names_consistency.py` role says it asserts `descriptor_registry.yaml` / `proper_noun_registry.yaml` mirror `names_index.yaml`.
- **Open items:** `ed.stale 199 vs ceiling 76` and `ed.needs_jordan_stale 83 vs 21` were measured by the deleted scope_ratchet and "are not replaced" (history :312-316); the Lanchester fork; restoring a blocking form of m1_acceptance once a juncture passes.

### references/ci_checks_registry_history.md
- **What it is:** 426-line verbatim HISTORY of `ci_checks_registry.yaml` comments/notes (B-X split 2026-10-06).
- **Status:** none; reading: historical.
- **Bears on:** PROCESS, CORE, MB.
- **Content that matters:**
  - `_parse_ci_checks_entries` cuts `ci_checks:` at the first column-0 non-space line, so a column-0 comment silently drops later rows from the existence check (:31-34).
  - Evidence of what reaches the engine: "references/ was load-bearing on TOOLS AND PROSE ONLY" until `engine/substrate/descriptors.py` (:252); the vocabulary registers reached `tools/` only until `export_names.py` (:270), "which is how `systems/world/sim/npe.py` went on minting NPCs affiliated to 'Church' after Jordan ruled the name is 'Church of Solmund'".
  - Plan position 29b (2026-10-01) retired the `fac.*` descriptor block (architecture/meta/01_AXIOMS.md ID-13: "a declared field that reaches no reader is not declared"); the last `unimplemented` row `fac_intel_multiplier` died with `fac.intel` (:252).
  - `engine.mc_v18` / `engine/autoload/game_state.py` / `systems.factions.sim.faction_action` campaign driver were deleted at plan position 28-iii; `tools/balance_oracle.py` retired `FORK:6f740d9` (:264, :322-338). `arms.py` measured 0.77 s build + 46.7 s for 2 seasons, one seed (:335).
  - Retired by culling waves 1-5 (ED-IN-0194, 2026-08-21..23): ci_hooks_verifier, review_core + review_baseline, scope_ratchet, ci_workplan_pointer_check (+11 POINTER_*.md), ci_supersession_check, ci_wf_harness_check, build_test_register (12,638-line test_register.json), observability generators, audit_registry tools.
- **Conflicts / stale:** the ladder's source document `project-architecture-valoria-v2_2.md` "RESOLVES NOWHERE on main and has no restructure_ledger row" (:61-69).
- **Open items:** "whether every live plan HAS a pointer ... remains a Jordan docket question" (:216-220).

### references/d10_success_probabilities.json
- **What it is:** 38-line JSON, 20x20 table of P(>= N successes in M dice) at p = 0.40 per die, 2-decimal rounding.
- **Status:** none; reading: orphaned data (no reader found in `tools/ engine/ tests/valoria skills/`; only the integration guide mentions it).
- **Bears on:** DICE.
- **Content that matters:**
  - `metadata.success_range [7,8,9,10]` on a d10 gives p = 0.40 (:6-7); `table["10"]["5"] = 0.37` (:21, :35).
  - Spot check against binomial: 3 dice, >=1 success = 1-0.6^3 = 0.784, table 0.78 (:14); 5 dice >=3 should be 0.317, table 0.32 (:16): consistent.
  - Row 1 lists `"2": 0.00` and row n lists n+1 keys with 0.00: the "trials n, successes n+1" entries are impossible cells padded in; only "successes <= trials" is meaningful.
- **Conflicts / stale:** no `-1 subtracts` (botch) and no sigma/degree modelling; the live resolver is `engine/dice_engine/dice_engine.py` (CLAUDE.md §5). Values would not match any TN 6 or 8 pool (alias_registry gives TN 6|7|8).
- **Open items:** none stated; a derived numeric table with no generator (hand-transcribed, §0.05 "orphaned or hand-transcribed").

### references/deprecated_terms_registry.yaml
- **What it is:** 99-line GENERATED registry of retired terms (`renamed` 12, `removed` 8, `deprecated_abbreviations` 3, `legacy_frameworks` 9), `total_entries: 32`, source stated as `references/mechanical_terms_index.md §6` (extracted 2026-05-10).
- **Status:** "GENERATED ... DO NOT EDIT BY HAND" (:1-2). Reading: live naming-gate input, partly stale. Readers: `vocab_store.py`, `validate_ed_citations.py`, `ci_naming_check.py`, vector_audit.
- **Bears on:** PROCESS, CHAR, FA, MB.
- **Content that matters:**
  - Renames: Theocracy Counter -> Church Influence (ED-782), Rendering -> Mending Stability (ED-731), Combat Power -> Power, Cohesion -> Discipline, mass-combat Strength -> Size, Command Rating -> Command (all PP-232), Contact Rounds -> Thread Fatigue (ED-694), combat Health -> Vitality (ED-548/694) (:8-44).
  - `EventImpact -> Key (substrate)` and `Memory record -> Memory entry` (PP-687, :27-32) rename INTO the retired Key substrate.
  - Removed/struck: Thread Depth (PP-166), 75-threshold Seizure -> Mass Seizure (CI >= 60 probabilistic), Path C Thread Supremacy (PP-663), Niflhel as faction, VTM, Cultural Reformation, 10-card Co-Movement deck -> 18-card deck (threadwork §7.1) (:45-69).
- **Conflicts / stale:** renames "Health (combat damage track) -> Vitality" contradicts `alias_registry.yaml:57-63` (Health canonical) and the `descriptor_registry.yaml` derived-values list (Health); `source:` points at `references/mechanical_terms_index.md`, absent from `ls references`. Legacy philosophical frameworks map onto the 13 Convictions (:81-99) although the live basis is the 15-pursuit roster (ED-IN-0261, see descriptor_registry).
- **Open items:** none.

### references/descriptor_registry.yaml
- **What it is:** 280-line hand-authored registry of quantified descriptors, `version: v1`, `ratified: 2026-06-06`; the source for `engine/engine_params/descriptors.json` via `tools/export_descriptors.py` and the SOLE runtime reader `engine/substrate/descriptors.py`. Other readers: `export_composition.py`, `quantity_registry.py`, `registry.py`, `descriptor_registry.py`, `definitions_store.py`, `ci_names_consistency.py`, `ci_quantity_vocabulary_check.py`, `engine/season/hole_register.yaml`.
- **Status:** "The 10-attribute roster is IN FLUX until Jordan confirms it" (:9, :32). Reading: live (this is the code-read head).
- **Bears on:** CHAR, DICE, CORE, FA, SE.
- **Content that matters:**
  - **Ten attributes (scale 1-7)**: body Strength/Endurance/Coordination; mind Focus/Reason/Spirit/Perception; social Attunement/Presence/Grace (:37-58). "10 attributes" ruled by Jordan 2026-08-14; the ten named by ED-IN-0328 (2026-11-04, "I think"); keys stable (`attr.mind.acuity` = Reason, `attr.mind.will` = Spirit, `attr.body.agility` = Coordination, `attr.social.charisma` = Presence); Bonds retired but still resolves with `deprecated: true`. `Resolve` is Spirit's derived value, `Composure` is the knot damage track, not an alias of Grace (:27-35).
  - **Pursuit roster**, 15 names: virtue, honour, liberty, justice, wealth, reputation, scholastics, stability, individuality, community, doctrine, happiness, family, love, stewardship (:144-162), ED-IN-0261; reaches the axes only through `engine/season/rosters.yaml: tables.pursuit_projection` (15 x 7).
  - **Seven bipolar axes** in `[-1,+1]`, negative = first-named pole: hierarchical_equal, precedent_substantive, partisan_equitable, selfish_selfless, rigid_flexible, grandiose_humble, deontological_instrumental (:178-189); order is semantic (`engine/season/decision/choose.py` sums per candidate).
  - **Affiliation roster** (5, scale 0-5, player sees bands): solmund_orthodoxy, inner_tradition, thread_truth, einhir_restoration, altonian_civics; `concerns:` grouping church/einhir/altonia is read by `data/cast.py::conviction_of` (:214-228). **Heritage roster** (5): northern/central/southern_einhir, altonian, schoenlander; `engages:` maps southern_einhir->einhir, altonian->altonia (read by `queries/person_q.py::heritage_regard`); "NOT IN FLUX" (:236-247).
  - Settlement stats: Legitimacy 0-7, Popular Support 0-7, Prosperity 0-5, Defense 0-5, Order 0-5, Facility Tier 0-3 (:94-102); territory `terr.fort_level` 0-4 (:83); practitioner TS 0-100+, TPS = floor(TS/10) (:74-75).
- **Conflicts / stale:** the ten attribute names here (Coordination, Reason, Perception, Grace) disagree with `alias_registry.yaml:21-56` (seven: Agility, Attunement, Cognition, Endurance, Presence, Spirit, Strength) and `censured`/`deprecated` lists; two live vocab owners for the same quantity. Category-B scalars cite `module_contracts.yaml` by line number (`:870, :873, :872, :548, :598, :776-777, :745`), brittle; `source:` strings name `engine/params/*` and `.designs`-moved `systems/*/reference/*.md` paths (conviction_taxonomy_v30 etc.) that are quarantined. `by_reference` still lists `conv.*` (13) and `axis.*` (4) but flags them RETIRED (:253-255). The `resonance_style` deprecation carries an unresolved NEEDS-JORDAN correction (ED-IN-0025): the retirement premise "never canonically enumerated" is false (:266).
- **Open items:** Jordan's confirmation of the ten attributes (Godot fields stay unbound until then); `Cognition` -> Reason fold is `[ASSUMPTION]` "Jordan veto" (:46); `inner_tradition` kept as its own affiliation `[ASSUMPTION]` (:201); `clock.season_counter` `engine_clock` is fork-3-gated, ED-1051 open (:129).

### references/descriptor_registry_history.md
- **What it is:** 269-line verbatim HISTORY of `descriptor_registry.yaml` comments (B-X split 2026-10-06; text taken from commit `8b57336`).
- **Status:** none; reading: historical.
- **Bears on:** CHAR, FA, SE, WR, PROCESS.
- **Content that matters:**
  - A measured silent no-op caused by two code rosters of convictions: `systems/characters/sim/conviction.py` (9 names), `systems/world/sim/npe.py` (8 names, 6 in no canonical set), the registry (13 by reference); the only game caller of `apply_conviction_scar` passes `'Loyalty'`, absent from conviction.py's set, "so ED-912 6.1's Close-Knot-break Conviction Scar never landed while the caller reported that it had" (:166-182).
  - Same defect class for the four ethical axes: `engine/substrate/keys.py::AXES` vs `engine/season/rosters.yaml: conviction_axes`, "a fifth axis added to `keys.py` alone left the season engine scoring on four in silence" (:196-211, measured 2026-09-14).
  - Faction stat block (6 rows, `fac.influence/legitimacy/wealth/military/intel/stability`, scale 0-7) retired at plan position 29b (2026-10-01) because its sole reader `engine/autoload/game_state.py::Faction` was deleted; "the season's faction is a set of person acts `via` seats and carries no stat vector of its own" (:118-124); recoverable at `5c5d8ec6:references/descriptor_registry.yaml`.
  - Disambiguations: "Legitimacy (faction, derived)" = Mandate x 20 (0-140); "Discipline (faction)" = Stability x 10 (0-70), distinct from mass-battle Discipline (1-7) (:239-245). Coherence is a `track` (ED-830) though `module_contracts` once tagged it `bucket: pool` (now corrected, :264-268).
  - Political Pool: Church `Mandate+floor(CI/20)`; opponents `max(0, Mandate-floor(CI/30))`, ci_political_v30 §3.4 (:251-254).
- **Conflicts / stale:** the "9 personal attributes" decision of 2026-06-06 (:52) predates the current ten.
- **Open items:** D11 (`pool.knot` / `track.persuasion` cross-link) and D15 (`contracts_bucket` <-> KIND crosswalk) "REJECTED, not filed" (:262-264).

### references/design_rulings_2026-09-06.md
- **What it is:** 333-line record of eight verbatim Jordan rulings (R1-R8) from 2026-09-06, lane IN, with readings and adversarial corrections.
- **Status:** "REFERENCE (CLAUDE.md §0.05). Nothing ratifies on merge; this file is a mechanism for nothing" (:3). Reading: live as the only carrier of these rulings, but its code citations are stale (see below). Readers: `engine/season/hole_register.yaml`, `rosters.yaml`, `data/fixtures.py`, `queries/person_q.py` cite it.
- **Bears on:** CORE, WR, FI, FA, CHAR.
- **Content that matters:**
  - R1 (:24-35): "war supersedes the character, typically"; a casus belli personal to the dead declarer gives the inheritor STANDING in peace talks, not an automatic exit; closes F.32.
  - R2 (:39-50): Jordan's five terminal properties: "dynamic and capable and flexible and emergent and persistent"; the ratified refusals become instrumental and must be argued against these.
  - R4 (:77-91): the world must churn; `Rung.exists`/`Site.exists` had zero producers (F.20); four routes; route 4 (spontaneous generation) needs AX-5 amended; "Do not answer churn with a clock" (T-c, D-17/D-21).
  - R6 (:119-157): Domain Echo is a FACT not a magnitude; death writes `(Person, body)`, `(Person, exists)`, `(Tenure, until)`; office holder is derived from live `hold` Tenures, never stored (`Query.hold_force`, cardinality 1 per object). Missing link: nothing forms a Question about a vacant office; "PROPAGATION WITHOUT REACTION IS A CHRONICLE, NOT A GAME"; `choose` receives no World.
  - R7 (:161-195) THE DECISIVE RULING: "no magnitude carrier is admitted at any scale. Every aggregate is DERIVED, none is PUSHED"; legitimacy/standing/morale are Queries over `stance`/`convictions`; "THERE IS NO SINGLE FACTION-LEGITIMACY NUMBER", a ruler can be wrong about their own standing, the player sees their character's ESTIMATE; news travels at the speed of messengers (propaganda, cover-ups, interception fall out of it).
  - R8 (:198-333): partial observation: identity, act and motive are three independent claims (`who`, `stratum`/act, `why`); shape = one struct claim per (witness, event) with `subject` = the changed thing else the rung, so Q2 raises for everyone in the rung; the "sighting id" alternative was overturned on four counts (:243-264); eyewitness knows who-not-what, record knows what-not-who (:302-308).
- **Conflicts / stale:** the banner (:11-20) says `engine/season/` and `architecture/` "do not exist on main" (PR #371 unmerged): FALSE now, both exist. Every `shape.py:NNNN` citation is stale: `engine/season/shape.py` is gone (split into `loop/`, `state/`, `queries/`, `epistemic.py`; `hold_force` is now `queries/world_q.py:195`). `_ch_document_key` (R5/R8.4) is repaired in `engine/season/epistemic.py:456` (verified). `Person.marks` was deleted 2026-09-24 (ED-IN-0261 item 1; `state/carriers.py:742`); R8's `observation_terms` roster was built (`rosters.yaml`, `epistemic.py:530, 885-980`). So R8.4's four "defects" are at least partly closed. R6's "vacancy forms no Question" and R7's H-62/H-84 status are [UNVERIFIED] against `hole_register.yaml`.
- **Open items:** the consumer "a person who forms a candidate because of what they came to believe" (:287-289, :331-333) is stated as the one remaining work item for R5/R6/R8; whether it now exists is not answered here.

### references/glossary.md
- **What it is:** 305-line hand-maintained glossary (13 PARTS) of term expansions and abbreviations; "Last updated 2026-08-08 ... content last swept 2026-04-30, PP-691".
- **Status:** "Authority: This file is the canonical reference for all term expansions project-wide" (:4). Reading: stale; its own banner flags an unresolved conflict. Only `descriptor_registry.yaml` cites it (as practitioner-stat source); no tool reads it.
- **Bears on:** CHAR, DICE, FA, MB, SC, WR, PROCESS.
- **Content that matters:**
  - The 7-vs-9 attribute conflict is called out here (:53): "Neither file defers to the other, and `names_index.yaml`'s MIRRORS block omits this glossary" (the registry now carries TEN, so it is a 7-vs-10 conflict).
  - Debate tracker has three names: "Piety Track" with abbreviation CT (:114), "Persuasion Track" in `social_contest_v30`, and "Conviction Track" in `alias_registry.yaml`; glossary flags it "unresolved glossary<->social-contest name collision" (:114), while `censured_vocabulary.yaml` censures Conviction Track and CT.
  - Clock table with starts: Mending Stability 60 (TTRPG) / 72 (BG); Church Influence 0 / 28; Institutional Pressure 20 (75/80 = Altonian Vanguard); Public Instability 5 (0 = Parliament dissolved + Löwenritter coup, BG only) (:101-104).
  - Mass-battle stat formulas reappear (:149-155): Command ceil((Presence+Cognition)/2), H = min(Discipline, Command)+DR; SIM-DEBT-03: DR 2 adds 40% more Health at equal Discipline, uncalibrated (:295).
  - "Domain Echo: Faction-level consequence triggered by decisive Debate outcomes" (:190) contradicts design_rulings R6 (Domain Echo is a recorded fact of any scale, e.g. a governor dying in a duel).
- **Conflicts / stale:** Part Eleven canonical docs point to `designs/provincial/...` (dissolved tree) and `systems/_architecture/reference/*` (quarantined to `.designs`); the generated `references/glossary/` views "RETIRED 2026-08-21 (ED-IN-0194)" (:23); the usage rules say `CI` "is no longer used" and "Use CI for the Church clock" in the same bullet (:45), self-contradictory; Part Twelve CI row likewise. Game Master entry says "named Cardinals (Prudence, Justice, Gifts, Temperance)" (:197); Health is "Wound track" (:75) vs deprecated registry "Health -> Vitality".
- **Open items:** SIM-DEBT-03; the bare-`GM` sweep "queued" (:227).

### references/id_reservations.yaml
- **What it is:** 150-line allocator state for ID blocks: frozen flat ED-NNNN (ceiling 1096), frozen PP (726), per-lane `next_free` for `ED-<LANE>-NNNN`; `version: 3`, `updated: 2026-07-01` (header stale; lane_ids updated 2026-07-29 but carries entries to 2026-11-08).
- **Status:** none; reading: live (the allocation source of truth per CLAUDE.md §4). Readers: `tools/validate_ed_citations.py`, `currency_consistency_check.py`, `ci_register_size_check.py`, `ci_common.py`, `build_identifier_census.py`.
- **Bears on:** PROCESS (and, through comments, WR, SC, FA, SE, CHAR).
- **Content that matters:**
  - Current `next_free`: MB 82, PC 60, FI 10, SC 41, FA 40, WR 13, IN 358, GO 3, SE 57 (:85-137). The inline comments are a de facto ruling log. E.g. IN-0350 (2026-11-05) "argue's pool is Presence; Attunement informs the read of reception and the style"; IN-0351 "Jordan withdraws CR-85's ratification and reopens M2 for combat and the social contest: faculty's role; needs_jordan"; IN-0347 "57 attribute rulings of one session recorded as a set; PROVISIONAL: the health sketch"; IN-0352 flow conditioning of decisions, office influence by institutional reach, settlement fabric, canon locations matched to the engine (CR-97..107); IN-0353 "one parliament"; IN-0354 "the Church is transnational, its Holy See at Himmelenger"; IN-0355 "15 territories, the sole victory count; which 15 an [ASSUMPTION]"; IN-0356 "Schoenland is a neutral offshore trade nation that trades with both Altonia and Valoria in war"; IN-0357 "the Queen is the Widow Regent; her remit is contingent on the King's elimination; build open, design-first" (:96-109).
  - Others: IN-0317 "a march needs a casus belli, civil war excepted; interim test cap of one march per season into each territory" (:108); IN-0316 strife master and kind list ratified, `regime_gain` 0.5 (:109); IN-0310 `build_realm` `foreign` default True (:115); IN-0306 armies get an order-of-battle record, AI presets, territory occupation (:118); IN-0304 risk-appetite and decision-horizon ruling (:120); IN-0303 "Match Godot terminology in all instances" (:121); IN-0293 every NPC holds a full pursuit vector plus convictions on Einhir, Altonia, the Church (:129).
  - MB-0079/80/81 (2026-11-01): circle cell body, end-of-tick no-overlap, stress findings needs_jordan, cells turn to face aggressors (:85); PC-0059 (2026-11-06) "the 21 GENERIC calibration abilities and the tempo log-edge; provisional" (:86).
  - Open needs_jordan allocation notes: SC-0040 reception/proofs reading other persons' ledgers at RESOLVE vs 04:250 (:90); IN-0292 founding basis against 04 §C.2 and the vacancy stamp against AX-7 (:130); IN-0297 where a `work` comes from in computed play (:126); IN-0298 how news of coercion travels (:125).
- **Conflicts / stale:** round-1/2/3 block table (A, B, C, D, E, contest_rebuild) is the superseded flat-ED regime (:29-58); `verified_live_max.verified_on 2026-07-02`; `wiring_status.auto_allocation: PARKED` references `github_ops` (a retired orchestrator). A duplicate-key hazard is acknowledged (:79, :134).
- **Open items:** reserved numbers FA-0039, SE-0056, IN-0295/0296 (reserved with no ledger rows, :91, :127, :136).

