# ci_checks_registry — history

Companion to `references/ci_checks_registry.yaml`. **That file is the REGISTRY; this one is HISTORY.**

## Why the split (B-X, Jordan 2026-10-06: *"you can extract all edit histories/discussion from .yaml files in references and just make those a supplement"*)

`ci_checks_registry.yaml` is read as TEXT by `tools/broken_dependency_checker.py`
(`_parse_ci_checks_entries` and `check_ci_registry_coverage`, which join every `path:` and `ci_job:` against
the working tree and `.github/workflows/valoria-ci.yml` in both directions). It is read as prose by
`skills/layer-conformance/SKILL.md` (which names the header as the owner of the depth vocabulary) and by
`.claude/commands/close.md` (which sends a reader to a row's `role:` line). No program reads a `notes:` key, a
`known_issues:` item or an `advisory_only:` note (grep of `tools/`, `tests/`, `engine/`, `skills/`, `.claude/`
and `.github/`). Around the rows it had accreted dated incident write-ups, "added on X, measured Y" histories,
retirement obituaries and resolved known-issues. They were carried by every reader of the registry.

**Nothing was deleted.** Every block below is the YAML text as it stood, moved verbatim (for a `notes:` key or a
`known_issues:` block, the original lines; line numbers are those of the file at the split).

**What stayed behind:**

- every `path:`, `args:`, `level:`, `subject:`, `posture:`, `role:` and `ci_job:` value, unchanged. `role:` is
  where CLAUDE.md §4 says a tool's verb is DEFINED, so even a `role:` that carries narrative (for example
  `export_npc_roster`'s, which records a correction to its own wording) was left alone;
- the header's depth vocabulary (`game` / `compliance` / `verification`, postures, the fourth tier that does not
  exist as code, the "ONLY ONE ROW HERE IS `verification`" paragraph, the line an orchestrator must not cross),
  the level ladder, the field definitions and the drift discipline;
- the editor instructions in the drift-detection notes;
- a shorter `notes:` where the original held an operative fact (a reason a tool is deliberately not wired, a
  falsifier's location, a limit). The shortening only removes sentences; the original is here.

**Constraint worth knowing before editing the registry.** `_parse_ci_checks_entries` cuts the `ci_checks:`
section at the first line that begins with a non-space character (`^\S`). Every comment inside the section is
indented for that reason, and a column-0 `#` line inside it would silently truncate the section and drop the
rows after it from the coverage check. The `# ── Level 1-2` banner at column 0 is what ends it on purpose.

**Adding here, not there.** A new row's `notes:` should say what is true of the tool today. Dated provenance,
measurements and retirement records belong in this file.

## History by section of the YAML

### Header: why `layer:` became `subject:` (2026-09-09); line 13 and 18-20 stay  _(was lines 14-17 of the file at the split)_

```yaml
#   Renamed to `subject:` because the two collided on one word while counting in OPPOSITE DIRECTIONS
#   — this file's old `L0` was the game, where governance Layer 2 is the game — so a session reading
#   either cold derived the other's meaning. That is the idempotence failure `CLAUDE.md` §4 names, and
#   `evacuate` already cost real work to it. Nothing read the field, so the rename broke no consumer.
```

### Header: the orchestrator has no subject (Jordan, 2026-08-22: "L2 requires an orchestrator")  _(was lines 53-58 of the file at the split)_

```yaml
# THE ORCHESTRATOR HAS NO SUBJECT, AND THAT IS WHAT KEEPS IT SAFE (Jordan asked 2026-08-22:
# "L2 requires an orchestrator"). It does, and it already exists: `tools/valoria_local.py`, whose
# docstring states the property — "ONE VALIDATOR, MANY CALLERS: this orchestrator shells the
# authoritative validators; it never re-implements a rule." A dispatcher that holds no rule has no
# subject, so it occupies no rung and cannot deepen the stack. `tools/ci_common.py` is the same:
# shared primitives, no subject.
```

### Level ladder: the dangling citation to project-architecture-valoria-v2_2.md (measured 2026-08-22)  _(was lines 68-72 of the file at the split)_

```yaml
# WARNING: `project-architecture-valoria-v2_2.md` RESOLVES NOWHERE on main and has no
# references/restructure_ledger.md row (measured 2026-08-22). The ladder below is cited to a
# document that does not exist — recorded rather than quietly re-sourced, because inventing a
# citation is worse than naming a dangling one. The `subject:` axis above is defined in place
# and depends on nothing absent.
```

### Level ladder: LEVEL 4 retired (2026-08-12, G3 / ED-IN-0159 §1.10)  _(was lines 79-89 of the file at the split)_

```yaml
# LEVEL 4 IS RETIRED (2026-08-12, G3 / ED-IN-0159 §1.10). It read "code hook with
# RuntimeError in valoria_hooks.py (highest, in-session)". That file lived only at
# `deprecated/skills/valoria-orchestrator/scripts/valoria_hooks.py` and was removed by the
# 2026-08-05 evacuation (`cadf9c7`), so the ladder's top-but-one rung described an apparatus
# with no implementation, and three rows below claimed it while being report-only CI tools.
# Disposition is DELETE rather than KEEP-AS-ANTICIPATORY under the rule ED-IN-0163 had to
# state for the opposite case: an absent path is dead only if its SUBJECT was retired, never
# merely because it is absent. Here the subject — the in-session orchestrator hook tier — was
# retired deliberately and is not coming back. The numbering is deliberately left as 1/2/3/5
# with the gap visible; renumbering 5 to 4 would silently rewrite the meaning of every
# `level: 5` row already in this file.
```

### Field definitions: `args` (added 2026-08-23, S6/D2)  _(was lines 93-101 of the file at the split)_

```yaml
#   args             — the invocation flags that select WHICH rule this row is about, when one
#                      script serves more than one row. Added 2026-08-23 (S6/D2) for
#                      `ci_naming_check.py`, which runs blocking for the index's `block` tier and
#                      report-only for its `warn` tier. Declared here because an undeclared field
#                      invented for a single row is a scale-local dialect (CLAUDE.md §10's
#                      shape-divergence guardrail), and because `path` is existence-checked by
#                      `broken_dependency_checker`, so the flags cannot simply be folded into it.
#                      No consumer reads `args` today — it disambiguates the row for a HUMAN, and
#                      two rows sharing a `path` is otherwise unreadable.
```

### Field definitions: `paired_hook` removed  _(was lines 112-115 of the file at the split)_

```yaml
# `paired_hook` WENT WITH IT. Every one of its six non-empty values named a function in
# valoria_hooks.py, and `broken_dependency_checker`'s check (d) — the one that verified them —
# had been silently skipping since the evacuation while walking the entire repo on every run
# of a blocking gate looking for the file. Both are gone.
```

### Registry regeneration, 2026-07-11 (ED-IN-0031, Valoria Audit Ecosystem plan Phase 2 item 11)  _(was lines 123-128 of the file at the split)_

```yaml
# Full regeneration (2026-07-11, ED-IN-0031, Valoria Audit Ecosystem plan Phase 2 item 11):
# the previous 2026-05-10 snapshot listed only 8 of the ~22 checker-shaped tools/*.py scripts
# and only 5 of the workflow's then-19 non-aggregator jobs. Regenerated against the working
# tree post-Phase-2 (25 jobs total incl. ci-summary; 22 tools/*.py invocations across them).
# See tools/broken_dependency_checker.py::check_ci_registry_coverage() for the mechanical
# verifier that now keeps this honest going forward (wired into the `integrity` CI job).
```

### Retired row: tools/ci_hooks_verifier.py  _(was lines 143-143 of the file at the split)_

```yaml
  # RETIRED culling wave 3 (ED-IN-0194, 2026-08-21): tools/ci_hooks_verifier.py
```

### ci_golden_modes_check.py notes, original (ED-IN-0176)  _(was lines 167-167 of the file at the split)_

```yaml
    notes: "Pin list single-owned in the tool's FIELD_PINS; drift-guarded by tests/valoria/test_field_golden_pins.py. Grid modes stay covered by test_mass_battle_byte_exact.py in unit-tests. DELIBERATELY CI-ONLY (ED-IN-0176): every other blocking CI validator now also runs in tools/valoria_local.py's list, report-only, so local-green sees them. This one does not, on cost — measured 2026-08-13 at rc=0 in 275s (~4.6 min), against a local list whose every other entry is under 5s. A 4.6-minute pre-commit step holds unrelated commits hostage, which is the exact reason freshness_gate and ci_wf_harness_check are report-only locally. Recorded HERE because tests/valoria/test_gate_coverage.py's CI_ONLY_BY_DESIGN set requires the reason to live in this registry, not in the test."
```

### lanchester_signature.py notes, original (ED-MB-0050 A6a/A6b)  _(was lines 175-175 of the file at the split)_

```yaml
    notes: "REPORT-ONLY on purpose: the repaired instrument legitimately FAILS (melee fits p~3.20 against a <=1.4 linear bar), which is an engine finding held for plan-v2 fork #2 (two incompatible 2:1 targets), not a regression to gate on. Flips to blocking when that fork is ruled. Before A6a it was neither wired nor correct: its no-rout pin did not disable rout (PC_STOCHASTIC_ROUT keys on casualty fraction), its volley scenario never fired, and its exponent was the scan-grid ceiling."
```

### broken_dependency_checker.py ci_job trailing comment  _(was lines 182-182 of the file at the split)_

```yaml
    ci_job: validators    # collapsed 2026-08-01: was its own `integrity` job
```

### freshness_gate.py notes, original (stale: get_live_sha is defined; see known_issues)  _(was lines 191-191 of the file at the split)_

```yaml
    notes: "Bootstrap currently calls but the function get_live_sha is absent in active session; warning emitted, non-blocking."
```

### canon_coverage_check.py notes, original (re-measurement 2026-08-01)  _(was lines 199-199 of the file at the split)_

```yaml
    notes: "Added 2026-05-10. Ported off the GitHub code-search API onto a working-tree os.walk (ED-IN-0032, doctrine fix). Wired into CI report-only 2026-07-11 (Jordan's ruling, Phase 2 item 9). RE-MEASURED 2026-08-01: 4 unregistered-with-header, 27 registered-no-header. The prior figures (1/28, 2026-07-11) were the LAST READING BEFORE THE INSTRUMENT BROKE -- its scan root was designs/, retired 2026-07-19, so it reported 0/0/0 for 13 days while this note looked like current state. Repointed at systems/."
```

### Retired rows: ci_audit_registry_check.py, audit_registry.py, audit_staleness.py, dashboard_data.py (culling wave 1/2, ED-IN-0194)  _(was lines 201-203 of the file at the split)_

```yaml
  # RETIRED culling wave 1/2 (ED-IN-0194, 2026-08-21): ci_audit_registry_check.py and
  # audit_registry.py, with tools/audit_staleness.py and tools/dashboard_data.py, which this row
  # named as its consumers. All were apparatus-subject.
```

### ci_pp_frozen_check.py notes, original (ED-IN-0190 / ED-IN-0185 Q4)  _(was lines 211-211 of the file at the split)_

```yaml
    notes: "Executes Q4 of ED-IN-0185's ruling agenda. The ruling said 'verify only the format'; a literal format check over PP-\\d+ can never fail, so the intent (frozen vocabulary + provenance resolves at a named ref) is discharged as two rules that CAN fail. Carries its own left-boundary pattern rather than ci_common.PP_ID_PAT, which is bare PP-\\d+ and matches inside OPP-03 -- measured: the owner's pattern produces 34 fabricated findings on one proposals doc. Excludes itself from its own scan after reporting a violation against its own docstring on first run (ED-IN-0159 2.4, the instrument counting itself). Raising PP_FROZEN_CEILING un-freezes a frozen vocabulary and needs its own ED plus a ruling."
```

### Merged row: ci_names_check.py into ci_naming_check.py --warn (S6/D2, ED-IN-0194, 2026-08-23)  _(was lines 229-235 of the file at the split)_

```yaml
  # MERGED 2026-08-23 (S6/D2, ED-IN-0194): tools/ci_names_check.py retired into
  # tools/ci_naming_check.py --warn. One rule -- "an added line must not introduce a deprecated
  # name" -- parameterised by the index's enforce tier, and it had two implementations sharing the
  # same diff machinery and the same path exclusions (the warn tool imported the block tool's
  # is_excluded), differing only in a keyword argument and the output strings. This row stays as a
  # SECOND row because the two tiers are wired to different CI jobs with different policies; the
  # `path:` now names the surviving tool and the invocation that selects the tier.
```

### ci_sim_fabrication_check.py notes, original (ED-IN-0188)  _(was lines 283-283 of the file at the split)_

```yaml
    notes: "Ports valoria_hooks.sim_fabrication_check (deprecated/skills/valoria-orchestrator/) into a standalone validator. Also runs locally via valoria_local.py --staged (blocking). FORK added 2026-08-14 (ED-IN-0188) for citations orphaned by the 2026-08-05 evacuation — mc_v17.py, tests/sim/v17-integration/, engine/params/ — which named live paths that no longer exist and were indistinguishable from invented ones."
```

### ci_claim_provenance_check.py notes, original (ED-PC-0040, widened ED-IN-0087)  _(was lines 292-304 of the file at the split)_

```yaml
      ED-PC-0040. Sibling to ci_sim_fabrication_check and aimed at the gap it leaves: that gate asks whether a
      CONSTANT in code is cited; this asks whether a MEASURED CLAIM in a ledger is reproducible. Built after three
      consecutive PC-lane batches half-stood on adversarial review for the same cause — confident quantitative claims
      written faster than they were measured, with the falsifying scripts ad-hoc and discarded ("spear/yari/estoc ->
      0" for the roster's MOST decisive plate weapon; "a tier the fix was never meant to touch" for a tier it moved 23
      points). Cutover is an ID, not a date (LEDGERS maps ledger -> first bound entry id): every entry in the failing
      arc shares the date of the entry that establishes the rule, so a date cutover would either exempt the rule from
      itself or demand mass-editing an append-only ledger. Currently scoped to the PC lane; widen lane by lane as each
      gains an instrument to point at. LIMIT, stated plainly: it verifies a source is NAMED and PRESENT, not that the
      number is CORRECT — same class of limit CLAUDE.md §7 records for the anti-fabrication gate. Also runs locally
      via valoria_local.py --staged (blocking). WIDENED to the IN lane 2026-07-28 (ED-IN-0087, cutover ED-IN-0087),
      taking this entry's own "widen lane by lane" instruction at its word once the IN lane had an instrument
      (tools/ci_claude_workflow_paths.py) to point at.
```

### Retired rows: ci_claude_workflow_paths.py; ci_workplan_pointer_check.py and the POINTER_*.md files; ci_wf_harness_check.py; ci_supersession_check.py (culling waves 2/3, ED-IN-0194)  _(was lines 306-321 of the file at the split)_

```yaml
  # RETIRED culling wave 3 (ED-IN-0194, 2026-08-21): tools/ci_claude_workflow_paths.py

  # RETIRED culling wave 2 (ED-IN-0194, 2026-08-21): ci_workplan_pointer_check.py together with
  # the 11 workplans/POINTER_*.md files it guarded. The guard was sound; its subject was a pointer
  # convention over this repository's own planning surface, not over the game.
  #
  # The retired row's own text, kept because it records a real and still-open limit: it never
  # checked that every live plan HAS a pointer, because the 2026-07-29 triage MEASURED liveness to
  # be un-inferable — a Status heading is a signal in neither direction (10 of 58 plan-shaped files
  # carry one, 7 of those 10 are dead, 3 of the live plans carry one). That half remains a Jordan
  # docket question and does not become answered by deleting the guard.
  #
  # RETIRED culling wave 3 (ED-IN-0194, 2026-08-21): tools/ci_wf_harness_check.py

  # RETIRED culling wave 2 (ED-IN-0194, 2026-08-21): ci_supersession_check.py — every return in
  # its main() was 0 and :66 said so explicitly, so it could never gate.
```

### compliance_check.py notes, original (ED-1082)  _(was lines 337-337 of the file at the split)_

```yaml
    notes: "CI mode (--check-only --repo-state .) is the live BLOCKING half; NOT in valoria_local.py's local check list, so local-green != compliance-green (ED-1082 correction, CLAUDE.md §8). Its orchestrator-era check_all()/validate_commit() harness paths (github_ops import, /home/claude sys.path insert) remain dead outside CI mode."
```

### Retired rows: review_core.py + registers/review_baseline.yaml (culling wave 2, ED-IN-0194)  _(was lines 339-342 of the file at the split)_

```yaml
  # RETIRED culling wave 2 (ED-IN-0194, 2026-08-21): review_core.py + registers/review_baseline.yaml.
  # Eleven of its twelve signals were apparatus signals. The twelfth, `m1.acceptance`, was the only
  # game-subject signal wired into CI, so it is rewired directly as `m1_acceptance.py --summary` in
  # validators-report — see the row for tools/m1_acceptance.py and the note in valoria-ci.yml.
```

### export_game_constants.py notes, original (added 2026-08-20)  _(was lines 366-366 of the file at the split)_

```yaml
    notes: "Added 2026-08-20. BLOCKING (deterministic, composes on two already-gated exports, no external pins). WHY IT EXISTS: measured the same day, valoria-game read ZERO bytes of any engine_params file and all ~200 constants in its systems/util/Constants.gd were hand-transcribed with no comparer. PAIRS ARE HAND-CONFIRMED, NEVER NAME-MATCHED — a first pass that matched by name produced six divergences and adversarial re-checking found none of them real (four from near-name guessing, two from exact-name collisions where the same word names different quantities), while the two REAL divergences it found later share no name with anything. The tool's COLLISIONS block records the look-alikes so they are not re-derived; DIVERGENCES records real model disagreements that need a ruling, not a value copy, and that list can only shrink."
```

### export_descriptors.py notes, original (added 2026-08-20; plan position 29b)  _(was lines 374-374 of the file at the split)_

```yaml
    notes: "Added 2026-08-20. BLOCKING (deterministic, no external pins). WHY IT EXISTS: measured the same day, references/ was load-bearing on TOOLS AND PROSE ONLY — no module under engine/ or systems/ loaded descriptor_registry.yaml or module_contracts.yaml, every runtime hit was a comment or docstring, and the rosters code ran on were hardcoded twins in engine/autoload/game_state.py. engine/substrate/descriptors.py is the reader that made the registry a root: it loads the cooked artifact this export writes. PLAN POSITION 29b (2026-10-01) RETIRED THE FACTION BLOCK: game_state.py, the Faction dataclass, the import-time assert_faction_roster_is_covered() check, descriptors.faction_bounds()/FACTION_STATS and the six fac.* registry rows were deleted together (architecture/meta/01_AXIOMS.md ID-13: a declared field that reaches no reader is not declared; the block is in git at 5c5d8ec6:references/descriptor_registry.yaml). The export records RATIFIED-BUT-UNIMPLEMENTED items in its `unimplemented` block rather than silently closing them; the block is EMPTY again (its last row, fac_intel_multiplier, died with fac.intel) and an empty register is not evidence the register is complete. Falsifier: tests/valoria/test_descriptors_runtime.py pins the empty set, that the reader reads the cooked artifact, and that the export is current."
```

### export_npc_roster.py notes, original (wired 2026-09-16)  _(was lines 382-382 of the file at the split)_

```yaml
    notes: "⚠ WIRED 2026-09-16, AND THE WIRING IS THE POINT. --check had existed since the tool did and was invoked by NO CI job, NO local hook and NO test — measured by grepping all three. Its six sibling exporters are each gated; this one shipped game content and was gated by nothing, which is exactly the defect tools/ci_common.py:349-358 names against itself: a single-owner comment asserting a property the tree lacks is worse than no comment, and an unrun --check is that property missing. Contrast export_sim_params.py, which has no row here either but IS enforced, via tests/valoria/test_export_sim_params.py calling esp.check() inside the blocking suite — undocumented rather than unguarded. This one was both. Verified green before wiring: 46 NPCs, every row naming a real case, a real place and a seated person. NOT A SECOND HEAD: references/npc_registry.yaml carries identity, convictions and role; npcs.yaml carries placement and wants — disjoint fields, so the two readers cannot disagree about content."
```

### export_composition.py notes, original (plan Act C3 seam 2; plan S5c)  _(was lines 390-390 of the file at the split)_

```yaml
    notes: "Added 2026-08-20 (plan Act C3 seam 2). BLOCKING. It IMPORTS AND RESOLVES every declared target at export time, which is the whole reason import-by-string is safe here: a typo or a moved module reds this gate rather than failing a campaign run. Before this, the campaign driver (engine/mc_v18.py, deleted at plan position 28-iii) imported systems.factions.sim.faction_action and systems.overview.sim.season at module level — the root naming its own dependents, and one half of the live package cycle faction_action -> engine.autoload.game_state -> systems.factions.sim.treaty. Falsifier: tests/valoria/test_engine_does_not_import_systems.py asserts require() RAISES on an undeclared role (no silent default) and that every declared role resolves. The wiring half arrived here in plan S5c because it is the ONLY blocking CI job over this registry — build_contract_index.py, the natural home on subject grounds, is wired into no workflow, so retiring the rules there would have deleted them while appearing to move them. Two of wiring_map_check's five rules are NOT ported and are not lost: 'every wiring tag resolves to a module contract' and 'coverage is 27/27' were checks against a SECOND registry keyed by the same names, and the fold makes them unfailable. Falsifier for the wiring half: tests/valoria/test_wiring_validation.py, hermetic cases over synthetic registries plus one that runs the live file (`pytest` prints the count; the adapter cases retired at plan position 28-iii with the rules they pinned). That file exists because the first version of this row asserted 'mutation-verified' with NO artifact in the tree while the test pinning these rules had just been deleted with wiring_map_check.py -- an unfalsifiable result claim under CLAUDE.md 0.1 pt 3, caught by an adversarial pass the same day."
```

### export_names.py notes, original (added 2026-09-16)  _(was lines 398-398 of the file at the split)_

```yaml
    notes: "Added 2026-09-16. BLOCKING, and a RUNTIME INPUT gate: engine/season/data/cast.py resolves NPC faction strings through the leaf, and engine/season/rosters.yaml derives its `factions` roster from it via `from_names:`, so a stale artifact is a cast with unresolvable factions rather than a drifted document. WHY IT EXISTS: measured 2026-09-16, the vocabulary registers reached tools/ ONLY -- alias_registry's two apparent reads in engine/substrate/descriptors.py are a comment and a docstring, and nothing under systems/ read any of them, which is how `systems/world/sim/npe.py` went on minting NPCs affiliated to 'Church' after Jordan ruled the name is 'Church of Solmund'. The exporter refuses the three shapes that make a term non-idempotent (ED-IN-0179): an alias resolving to two canonicals, an alias that is also another row's canonical, and a legacy tag that is also a live alias. It RECORDS rather than refuses the two real display collisions (Order = conv.order + set.order; Stability = fac.stability + mech.stability) in an `ambiguous` block, and the leaf raises on them -- descriptors.json's `unimplemented` precedent, because merging those rows would delete a real quantity. Falsifier: five mutations run 2026-09-16 -- a ninth faction reaches the season roster (8 -> 9), unclassing Schoenland drops it (8 -> 7), and `values:` beside the pointer, two pointers, and a token_class nobody carries each raise Unspecified."
```

### build_identifier_census.py notes, original (culling wave 5, ED-IN-0194)  _(was lines 406-406 of the file at the split)_

```yaml
    notes: "NO LONGER A FRESHNESS GATE (culling wave 5, ED-IN-0194, 2026-08-22). Its outputs are UNTRACKED, so there is no committed copy for --check to find drift against; the `--check` invocation was removed from the blocking `validators` job and from tools/valoria_local.py in the same commit, because it compares against files git no longer carries and would have red main on the first push. The builder itself is KEPT and is run on demand by the `generated_layer` fixture in tests/valoria/conftest.py, which owns the build order for the whole generated layer. Its hermetic tmp_path falsifiers stay in tests/valoria/test_identifier_census.py and are unaffected — they monkeypatch REPO and never read the real tree. Two claims in the previous note are now stale and are recorded as such rather than carried forward: references/glossary/ is NOT built from this census (no glossary builder exists in tools/; references/glossary.md is authored and tracked), and the -n auto race with test_engine_atlas is moot now that whole-tree freshness is not asserted anywhere."
```

### Retired row: build_test_register.py + references/test_register.json (culling wave 2, ED-IN-0194)  _(was lines 408-410 of the file at the split)_

```yaml
  # RETIRED culling wave 2 (ED-IN-0194, 2026-08-21): build_test_register.py + its 12,638-line
  # references/test_register.json output — an AST census of the test tree, read by nothing in
  # engine/ or systems/, and a standing source of generated-file churn on every test edit.
```

### mechanics_index_gen.py notes, original (Phase 2 item 7)  _(was lines 418-418 of the file at the split)_

```yaml
    notes: "Fully CI-shaped (--strict exit-code contract) but never wired before 2026-07-11 (Phase 2 item 7). Report-only (continue-on-error). Not listed in ci-summary's needs."
```

### validate_ed_citations.py notes, original  _(was lines 426-426 of the file at the split)_

```yaml
    notes: "Blocking as of 2026-06-29 (backlog reconciled 292 -> 0, designs/audit/2026-06-28-ed-citation-triage/02_reconciliation.md)."
```

### ci_vacuous_assertion_check.py notes, original (ED-IN-0118)  _(was lines 434-434 of the file at the split)_

```yaml
    notes: "Wired 2026-08-01 (ED-IN-0118). It shipped with its own pytest suite and NO invoker and NO registry row — a detector nobody runs is the defect it detects, and its own test file says so: 'a switched-off guard is worse than none because the repo still believes it is covered.' Report-only: 18 suspicious findings today, 0 provably vacuous."
```

### Retired rows: ci_program_claim_check.py, scope_ratchet.py + registers/scope_baseline.yaml (culling wave 2, ED-IN-0194), and the ratchet's unreplaced measurements  _(was lines 436-444 of the file at the split)_

```yaml
  # RETIRED culling wave 2 (ED-IN-0194, 2026-08-21): ci_program_claim_check.py (its subject, the
  # workplan pointers, went with ci_workplan_pointer_check above) and scope_ratchet.py +
  # registers/scope_baseline.yaml.
  #
  # ⚠ SCOPE_RATCHET WAS MEASURING SOMETHING REAL AND IS NOT REPLACED. It reported REGRESSED on
  # ed.stale (199 against a ceiling of 76) and ed.needs_jordan_stale (83 against 21) right up to
  # its deletion. Those two numbers are still true; nothing now reports them. They are editorial
  # debt on the ledgers, not apparatus debt, so if they are to be watched again the instrument
  # should be a ledger-subject one, not a five-ceiling repository ratchet.
```

### engine/season/harness/arms.py notes, original (ported 2026-09-29, plan position 28-i, M5)  _(was lines 458-474 of the file at the split)_

```yaml
      Ported 2026-09-29 (plan position `28-i`, M5) from `tools/balance_oracle.py`, which is
      retired (`FORK:6f740d9`, `references/restructure_ledger.md`) -- it drove
      `engine.mc_v18.run_campaign`, a faction/strategic-scale campaign with no season-side
      equivalent, and `rosters.yaml`'s own `field_casualty_models` note says by name that tool
      "cannot observe" an `engine/season`-only mechanic. This is NOT the same comparison the old
      tool ran twice (same-seeds-twice-in-one-process, private-ladder-vs-owner-ladder): that
      mechanic was verified season-unreachable and has no surviving code, even as inert historical
      record (it would add a new nested `engine -> systems` import
      `tests/valoria/test_engine_does_not_import_systems.py`'s `NESTED_BASELINE = 0` ratchet
      forbids). The live arms are now `field_casualty_model`'s `total` (pre-M4 control) vs
      `scaled_by_degree` (the ruled default), read by `loop/effects.py::_eff_march` on a lost
      field battle -- H-148, `ED-IN-0279` clause (a).
      DELIBERATELY NOT WIRED INTO CI, same reason as before: a realm build plus a season run costs
      tens of seconds per seed (measured 2026-09-29: 0.77s build + 46.7s for 2 seasons, one seed),
      so an n>=10 comparison is minutes, and a gate that slow gets skipped. This session did NOT
      run the tool's own default `--n`/`--seasons` invocation end to end -- see the module
      docstring for what that means for anyone citing a result from it.
```

### tools/m1_acceptance.py notes, first paragraph, original (wired 2026-08-21, ED-IN-0194); the second paragraph stays  _(was lines 487-494 of the file at the split)_

```yaml
      Wired directly into CI 2026-08-21 (ED-IN-0194) when culling wave 2 retired review_core.py,
      which had been its only carrier into a CI job. REPORT-ONLY, deliberately: `--check` exits 1
      today because stub_invocations and m1_junctures both fail, which is the true state of the
      milestone. review_core graded it against a ratchet baseline, so it red only on REGRESSION;
      a bare --check has no baseline and would red on arrival, refusing unrelated authors' commits
      for a pre-existing condition. ED-IN-0112 paid for that mistake once. Carved OUT of culling
      wave 1 by Jordan's ruling 2026-08-21 — wave 1 as ratified deleted it, one day before §0.2
      made it the definition of `done`.
```

### tools/fold_ledger_to_latest.py notes, original  _(was lines 524-537 of the file at the split)_

```yaml
      DELIBERATELY NOT WIRED INTO CI, matching `tools/balance_oracle.py`'s precedent (two rows
      above this one — `tools/m1_acceptance.py` sits directly above and IS wired into CI, so
      "immediately above" would misname the sibling this matches): this is a measurement
      instrument for a queue Jordan reviews by hand, not a gate over game state, and nothing
      here should fail a build. Manual invocation only:
      `python tools/fold_ledger_to_latest.py --queue`. Does NOT scan the older, pre-migration
      `registers/archive/*.yaml` corpus, structurally separate from the `.jsonl` ledgers this
      tool reads — a row resolved only there reads as "not found," not as resolved, to `--id`
      (exact-id lookup only; it does not accept a fragment or a prefix). That corpus is not
      reliably all-terminal either: `registers/archive/*.yaml`'s own ED-IN-0245 ruling archives a
      row on EITHER of two criteria (pre-current-month OR terminal status, not terminal status
      alone), so a live, flagged row can in principle sit there — benign today (every such row
      checked has a later, terminal superseding row in the same file) but not something this tool
      itself verifies.
```

### Level 1-2 banner (was "Level 4", retired 2026-08-12)  _(was lines 540-543 of the file at the split)_

```yaml
# ── Level 1-2 (text/skill, supervisory only) ─────────────────────────────────
# Listed for completeness; promotion to Level 5 is the long-term direction. (Was
# "Level 4" — the in-session hook tier, retired 2026-08-12 with valoria_hooks.py; see the
# header. CI is now the only rung above a heuristic check.)
```

### advisory_only: PI core_rules notes, original  _(was lines 550-550 of the file at the split)_

```yaml
    notes: "Backed by CLAUDE.md §2/§8 and the .githooks/ local tier. (Previously read 'largely backed by Level 4 hooks' — those hooks were evacuated 2026-08-05 and the claim outlived them.)"
```

### Drift-detection notes: the ci_hooks_verifier bullet (that tool is retired)  _(was lines 560-562 of the file at the split)_

```yaml
# - The ci_hooks_verifier should ideally read from this file rather than carry its
#   own list (deferred — current state is two sources, this one and the hardcoded
#   set in ci_hooks_verifier.py; reconcile when ci_hooks_verifier is next touched).
```

### known_issues: the three items, all resolved 2026-07-11 (ED-IN-0031)  _(was lines 566-592 of the file at the split)_

```yaml
known_issues:
  - id: ci-import-skeleton_gen
    description: ".github/workflows/valoria-ci.yml syntax-check job runs `py_compile tools/skeleton_gen.py` but that file was renamed to tools/doc_index_gen.py per PP-673. CI may be silently failing this step or skipping it."
    surface: ".github/workflows/valoria-ci.yml syntax-check job"
    proposed_fix: "Replace skeleton_gen.py with doc_index_gen.py in the syntax-check command. One-line CI fix."
    flagged: 2026-05-10
    resolved: true
    resolved_date: 2026-07-11
    resolution_note: "Already fixed in the working tree — .github/workflows/valoria-ci.yml's syntax-check job's py_compile list compiles tools/doc_index_gen.py (line 59); no reference to skeleton_gen.py remains anywhere in the workflow. Verified via grep, ED-IN-0031."

  - id: freshness_gate-get_live_sha-missing
    description: "Bootstrap session-startup tries `freshness_gate.get_live_sha` and warns 'module has no attribute get_live_sha' on every run. Function appears not present in current freshness_gate.py."
    surface: "freshness_gate.py / bootstrap call site"
    proposed_fix: "Add get_live_sha() to freshness_gate.py, or remove the bootstrap call site."
    flagged: 2026-05-10
    resolved: true
    resolved_date: 2026-07-11
    resolution_note: "Already fixed in the working tree — tools/freshness_gate.py:80 defines `get_live_sha = get_blob_sha` as a public alias (comment at line 79: 'Public alias kept for API stability'), directly under get_blob_sha's definition at line 70. Verified by reading the file, ED-IN-0031."

  - id: compliance-doc_index_gen-missing
    description: "compliance_check.py logs '[COMPLIANCE] Auto-fetch failed: No module named doc_index_gen — skipping' on every bootstrap. doc_index_gen.py exists at tools/, but compliance_check is looking for it as an importable module rather than tool path."
    surface: "compliance_check.py auto-fetch path resolution"
    proposed_fix: "Adjust import path or add tools/ to sys.path before the import attempt."
    flagged: 2026-05-10
    resolved: true
    resolved_date: 2026-07-11
    resolution_note: "Already fixed in the working tree — tools/compliance_check.py's _lazy_import() (line 24) walks sys.path/known tool dirs for atomizer.py, resolves a `required = ['atomizer.py', 'doc_index_gen.py', 'index_gen.py']` list (line 41) against them, and only falls back to a GitHub auto-fetch for whatever's genuinely missing (lines 45-68) before `import doc_index_gen as _s` (line 74). doc_index_gen.py resolves correctly when present at tools/. Verified by reading the file, ED-IN-0031."
```
