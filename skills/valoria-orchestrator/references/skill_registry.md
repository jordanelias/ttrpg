# Valoria Skill Registry — markdown companion
#
# CANONICAL FORM: `skill_registry.yaml` (this directory).
# This file is a human-readable companion to that yaml; the hook checks
# both stay in sync (`pre_commit_gate` co-file rule, Level 4).
#
# When adding/renaming/removing a skill, update both files in the same commit.
# Format: skill name | path | model | triggers | notes

---

## ACTUAL SKILLS ON GITHUB (as of 2026-06-10)

### valoria-orchestrator
- Path: `skills/valoria-orchestrator/SKILL.md` (directory-based, canonical)
- Also: `skills/valoria-orchestrator/SKILL.md` (flat stub — do not use)
- Model: Sonnet 4.6
- Triggers: session start, resume, route, what's the plan, start work, orchestrate
- References: `skills/valoria-orchestrator/references/` (commit_convention, session_protocol, skill_registry, model_routing_table, state_transfer_spec, github_pat)
- Scripts: `skills/valoria-orchestrator/scripts/github_ops.py`

### valoria-simulator
- Path: `skills/valoria-simulator/SKILL.md`
- Model: Sonnet 4.6
- Triggers: stress test, simulate, audit mechanics, edge cases, run scenario, test [mechanic], probability, crunch cascade, cognitive load, flowchart, precedent comparison, cross-mode
- Modes: A (isolation) B (interaction) C (scenario) D (edge case) E (coverage) F (Non-Player Character) G1-G5 (subsystem) H (substitution) I (patch output + commit) J (cognitive load) K (cross-mode delta + transitions) L (precedent) M (flowchart)

### valoria-mechanic-audit
- Path: `skills/valoria-mechanic-audit/SKILL.md`
- Model: Sonnet 4.6
- Triggers: consistency check, mechanic check, gap detection, redundancy, formula check, what's broken, what's missing  (D1: bare "audit" is NOT a trigger — routes to nothing; "NERS audit" → valoria-resolution-diagnostic)
- Modes: A-G (formula/consistency/contradiction/gap/principles/coverage/cross-mode)

### valoria-canon-guard
- Path: `skills/valoria-canon-guard/SKILL.md`
- Model: Sonnet 4.6
- Triggers: canon, philosophy, foundations, P-01 through P-14, compliance, philosophical violation, lore check
- Note: also invoked automatically before any compilation pass

### valoria-editorial-register
- Path: `skills/valoria-editorial-register/SKILL.md` (directory-based)
- Model: Sonnet 4.6
- Triggers: resolve editorials, editorial register, address editorial flags, propagate decisions, what editorials are pending, dedup editorials, consolidate, strike stale
- Workflows: A (resolve) B (add new) C (propagation pass) D (dedup/consolidate/strike) E (harvest from session)

### valoria-compiler
- Path: `skills/valoria-compiler/SKILL.md`
- Model: Sonnet 4.6
- Triggers: compile, assemble, checkpoint, export, new version, full assembly
- Note: LOWEST PRIORITY. Only run when a system is stable and explicitly requested.

### valoria-chunker
- Path: `skills/valoria-chunker/SKILL.md`
- Model: Haiku 4.5
- Triggers: chunk, section map, index, large document (>500 lines), prepare for analysis, extract sections
- Note: must run before any analysis skill receives >500 lines of input

### valoria-arc-generator
- Path: `skills/valoria-arc-generator/SKILL.md` (directory-based)
- Model: Sonnet 4.6
- Triggers: generate arc, campaign arc, Non-Player Character arc, emergent scenario, arc sequence

### valoria-combat-simulator
- Path: `skills/valoria-combat-simulator/SKILL.md` (directory-based)
- Model: Sonnet 4.6
- Triggers: combat simulation, Python combat sim, Monte Carlo combat, statistical combat analysis
- References: `skills/valoria-combat-simulator/references/` (combat_params, findings_template, sim_protocol)
- Scripts: `skills/valoria-combat-simulator/scripts/combat_sim.py`
- Note: for probabilistic/statistical analysis; simulator Mode G1 for scenario-based combat

### valoria-dice-model
- Path: `skills/valoria-dice-model/SKILL.md` (directory-based)
- Model: Haiku 4.5
- Triggers: dice math, probability, expected value, success rate, TN, Ob, pool size, d10
- Scripts: `skills/valoria-dice-model/valoria_dice.py`

### valoria-vector-audit
- Path: `skills/valoria-vector-audit/SKILL.md` (directory-based)
- Model: Sonnet 4.6 (full pipeline) / Haiku 4.5 (single-mode runs over precomputed graphs)
- Triggers: topographic audit, vector audit, corpus audit, find weaknesses, find debt, implied connections, what's missing, what's notional, where are the gaps, rerun topographic, validate against corpus, surface non-obvious structural properties
- Modes: A (multi-graph hubs) B (implied-but-missing) C (notional edges) D (cascade-without-return) E (sparse-context) F (throughline orphans) G (vocabulary debt) H (multi-graph isolates)
- References: `skills/valoria-vector-audit/references/` (methodology, diagnostic_modes, v1_v2_v3_history)
- Scripts: `skills/valoria-vector-audit/scripts/vector_audit.py`
- Note: v3 multi-graph triangulation methodology; supersedes v1+v2 one-off pipelines. Self-exempting on Ω/Μ vetting (Class A analytic instrument). Reference run: designs/audit/2026-04-29-topographic-analysis/. PP-676 / ED-762.

### valoria-atomizer
- Path: `skills/valoria-atomizer/SKILL.md`
- Model: Sonnet 4.6
- Triggers: atomize, index, infill, split design doc, extract index, extract prose, separate mechanics from prose, when a design doc fails the Index Ruleset Principle (>400 lines with explanatory content)
- Purpose: Split a v30 design doc into index (mechanical-only spec) + infill (prose, rationale, examples, history). Updates `references/design_registry.yaml` atomized field.
- Input: v30 design doc path from design_registry.yaml
- Output: `{name}_v30.md` (index) + `{name}_v30_infill.md` + updated registry entry
- Pre-requisite: design doc exists at canonical_v30 path in design_registry.yaml

### prose-writer
- Path: `skills/prose-writer/SKILL.md`
- Voice canon: `designs/world/narrative_voice_canon_v30.md` — lexical register, grammar latitude (twelve authors), and voice constraints externalized 2026-06-09 (D-3); skill provides procedure.
- Model: Sonnet 4.6
- Triggers: write narrative prose, lore entry, character vignette, settlement description, faction history, dialogue scene, codex entry, cutscene script, flavor text, any creative/narrative text
- Purpose: Valoria's singular literary voice — coherence-indexed weighted synthesis (Tolkien, Borges, Lispector, Ocampo, Márquez, Ishiguro, Mistry, Tartt, Beckett, Lem, McCarthy, Le Carré). Synthesis weights shift across coherence tiers (10-8, 7-5, 4-3, 2, 1).
- References: `skills/prose-writer/references/` (techniques-skeleton, anti-patterns-skeleton, calibration-skeleton, coherence-tiers)
- Scripts: `skills/prose-writer/scripts/consistency_check.py` (Solmund/Galbados Level 2 enforcement; mirrored at Level 4 by valoria_hooks.forbidden_token_gate)
- Note: Solmund Voice canon at `designs/world/solmund_voice_v30.md` is a scoped override for Church speakers / religious texts / characters with established Certainty levels.


### valoria-resolution-diagnostic
- Path: `skills/valoria-resolution-diagnostic/SKILL.md`
- Model: Opus
- Scope: ROLLING ENGINES ONLY — any mechanism resolving an outcome by a draw (dice, U[0,1), card). NOT a general "any mechanic" auditor; non-rolling systems (character sheet, pure ledger, static stat block, bare clock) are OUT OF SCOPE -> valoria-mechanic-audit.
- Triggers: is this rolling engine NERS compliant, diagnose this resolver, stress test this roll, NERS audit, is this sigma-leverage or deterministic+stochastic, does this resolution scale, leverage non-uniformity, clamp/Ob-floor conflict
- Purpose: Tests a rolling engine against five engine properties (legible odds / in-band uniform leverage / bounded+monotonic / graded recoverable / right engine for the pool regime), using two current canonical instances — sigma-leverage (Continuous Engine) and deterministic+stochastic (Domain Action resolver, ratified ED-874) — plus a [NEW ENGINE] branch for any third/novel rolled mechanic. Pipeline: Stage 0 validate the skill vs adjudicated cases (ED-874/884/ER-2) -> Phase 0–6 stress test -> lesson/property mapping -> per-engine NERS verdict -> Stage 4 re-test.
- Relationship: runs AFTER valoria-mechanic-audit (consistency); checks rolling-engine resolution fitness under stress and the loops/cliffs a rolling engine drives.
- Note: raw d10-vs-Ob is legacy TTRPG-mode only (a defect flag in videogame canon). Non-rolling components inside a composite are recognized-and-routed-out, not diagnosed.


---


### valoria-module-adjudicator
- Path: `skills/valoria-module-adjudicator/SKILL.md` (directory-based)
- Model: Opus 4.6
- Triggers: module contract, wrapper conformance, is this system keyed, input/output keys, adjudicate the architecture, interface audit, key wiring, interdependency check, does the graph close, scale coverage, enforce the wrappers
- Stages: 0 (scope) 1 (extract — index-first reads; stubs carry zero edges) 2 (adjudicate — machine checks A1-A12 + judgment J1-J3) 3 (verdict — per-module CONFORMANT/NON-CONFORMANT, graph CLOSED/OPEN, all-directions coverage table, NERS-N mapping) 4 (enforce — remediation routed to owning canon mechanism, re-run until clean or [OPEN — Jordan])
- Scripts: `skills/valoria-module-adjudicator/scripts/contract_adjudicator.py` (tests: `tests/contracts/test_contract_adjudicator.py`); `contract_flowchart.py` (derived views: flowchart / state graph / flattened pipeline map)
- Contract registry: `references/module_contracts.yaml` (anchored in canonical_sources)
- Note: judges the BOUNDARIES between systems, not single-mechanic balance (that is valoria-mechanic-audit / valoria-resolution-diagnostic). Code-architecture sibling of valoria-canon-guard's prose-canon conformance. PP refs: key_substrate §2.3/§4/§8, key_type_registry §10, scale_transitions §3/§5, derived_stats §11.

## SIMULATION COMMAND ROUTING

| User says | Orchestrator routes to | What runs |
|-----------|----------------------|-----------|
| "stress test [specific mechanic]" | valoria-simulator | Mode A + D + J + L |
| "stress test [subsystem]" | valoria-simulator | Mode G-submode + D + J + K + L |
| "stress test [mode]" | valoria-simulator | All G-submodes for that mode — orchestrator stages across sessions |
| "simulate [scenario]" | valoria-simulator | Mode C + M |
| "simulate [ttrpg/hybrid/boardgame]" | valoria-simulator | Mode C + G-suite + M — multi-session |
| "check consistency [subsystem]" / "find gaps" | valoria-mechanic-audit | Modes A-G  (bare "audit" → nothing, D1) |
| "topographic audit" / "vector audit" | valoria-vector-audit | Stages 1-7 + all 8 diagnostic modes |
| "corpus audit" / "find structural weaknesses" | valoria-vector-audit | Full pipeline |
| "vocabulary debt" / "find struck terms still in use" | valoria-vector-audit | Mode G only (fast) |
| "find isolates" / "what's disconnected" | valoria-vector-audit | Modes E + H |
| "find implied connections" | valoria-vector-audit | Modes B + C |
| "NERS audit" / "is this NERS compliant" / "diagnose this resolver" | valoria-resolution-diagnostic | Full Stage 1–5 pipeline |
| "stress test resolution" / "small pool problem" / "death spiral" | valoria-resolution-diagnostic | Stage 1 diagnostic or full pipeline |
| "canon check [mechanic]" | valoria-canon-guard | Full P-01–P-14 pass |
| "resolve editorials" | valoria-editorial-register | Workflow A |
| "compile" | valoria-compiler | Full compilation pass (only if requested) |
| "atomize [doc]" / "split design doc" | valoria-atomizer | Index/infill split + registry update |
| "write [prose/scene/codex/dialogue]" | prose-writer | Coherence-tiered narrative composition |
| "module contract" / "adjudicate the architecture" / "is this system keyed" | valoria-module-adjudicator | Stages 0-4 (extract → adjudicate A1-A12 + J1-J3 → verdict → enforce) |
| "key wiring" / "does the graph close" / "enforce the wrappers" | valoria-module-adjudicator | Stage 2-3 over existing contracts (assessor run + verdict) |

---

## SKILLS REFERENCED IN REGISTRY BUT NOT YET BUILT
None. All entries above exist on GitHub.

## SKILLS PLANNED BUT NOT YET BUILT
None currently. If new skills are added, update this registry in the same commit.
