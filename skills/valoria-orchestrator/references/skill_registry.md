# Valoria Skill Registry
# Single source of truth for all skills in the project.
# Updated on every commit that adds or modifies a skill file.
# Format: skill name | path | model | triggers | notes

---

## ACTUAL SKILLS ON GITHUB (as of 2026-04-02)

### valoria-orchestrator
- Path: `skills/valoria-orchestrator/SKILL.md` (directory-based, canonical)
- Also: `skills/valoria-orchestrator-SKILL.md` (flat stub — do not use)
- Model: Sonnet 4.6
- Triggers: session start, resume, route, what's the plan, start work, orchestrate
- References: `skills/valoria-orchestrator/references/` (commit_convention, session_protocol, skill_registry, model_routing_table, state_transfer_spec, github_pat)
- Scripts: `skills/valoria-orchestrator/scripts/github_ops.py`

### valoria-simulator
- Path: `skills/valoria-simulator-SKILL.md`
- Model: Sonnet 4.6
- Triggers: stress test, simulate, audit mechanics, edge cases, run scenario, test [mechanic], probability, crunch cascade, cognitive load, flowchart, precedent comparison, cross-mode
- Modes: A (isolation) B (interaction) C (scenario) D (edge case) E (coverage) F (Non-Player Character) G1-G5 (subsystem) H (substitution) I (patch output + commit) J (cognitive load) K (cross-mode delta + transitions) L (precedent) M (flowchart)

### valoria-mechanic-audit
- Path: `skills/valoria-mechanic-audit-SKILL.md`
- Model: Sonnet 4.6
- Triggers: audit, consistency check, mechanic check, gap detection, redundancy, formula check, what's broken, what's missing, cross-reference audit
- Modes: A-G (formula/consistency/contradiction/gap/principles/coverage/cross-mode)

### valoria-canon-guard
- Path: `skills/valoria-canon-guard-SKILL.md`
- Model: Sonnet 4.6
- Triggers: canon, philosophy, foundations, P-01 through P-14, compliance, philosophical violation, lore check
- Note: also invoked automatically before any compilation pass

### valoria-editorial-register
- Path: `skills/valoria-editorial-register/SKILL.md` (directory-based)
- Model: Sonnet 4.6
- Triggers: resolve editorials, editorial register, address editorial flags, propagate decisions, what editorials are pending, dedup editorials, consolidate, strike stale
- Workflows: A (resolve) B (add new) C (propagation pass) D (dedup/consolidate/strike) E (harvest from session)

### valoria-compiler
- Path: `skills/valoria-compiler-SKILL.md`
- Model: Sonnet 4.6
- Triggers: compile, assemble, checkpoint, export, new version, full assembly
- Note: LOWEST PRIORITY. Only run when a system is stable and explicitly requested.

### valoria-chunker
- Path: `skills/valoria-chunker-SKILL.md`
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

---

## SIMULATION COMMAND ROUTING

| User says | Orchestrator routes to | What runs |
|-----------|----------------------|-----------|
| "stress test [specific mechanic]" | valoria-simulator | Mode A + D + J + L |
| "stress test [subsystem]" | valoria-simulator | Mode G-submode + D + J + K + L |
| "stress test [mode]" | valoria-simulator | All G-submodes for that mode — orchestrator stages across sessions |
| "simulate [scenario]" | valoria-simulator | Mode C + M |
| "simulate [ttrpg/hybrid/boardgame]" | valoria-simulator | Mode C + G-suite + M — multi-session |
| "audit [subsystem]" | valoria-mechanic-audit | Modes A-G |
| "canon check [mechanic]" | valoria-canon-guard | Full P-01–P-14 pass |
| "resolve editorials" | valoria-editorial-register | Workflow A |
| "compile" | valoria-compiler | Full compilation pass (only if requested) |

---

## SKILLS REFERENCED IN REGISTRY BUT NOT YET BUILT
None. All entries above exist on GitHub.

## SKILLS PLANNED BUT NOT YET BUILT
None currently. If new skills are added, update this registry in the same commit.
