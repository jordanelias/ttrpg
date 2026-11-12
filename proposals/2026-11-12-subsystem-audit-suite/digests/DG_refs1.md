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
