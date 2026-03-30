# valoria-orchestrator

Orchestrate multi-skill workflows. Run at session start, on "resume"/"start work"/"what's the plan", or when routing between skills.

## Session Start

1. Read all skills from GitHub `skills/` directory. This is mandatory — `/mnt/skills/user/` copies may be stale.
2. Read `session_log_current.md` from GitHub. Report status ≤3 lines.
3. Read `valoria_gap_register_consolidated.md` — P1 count only.
4. Confirm task. Produce routing table before executing.

If either file is absent: treat as new session, flag to user.

## Canonical Project Status

`valoria_scope_map.md` is the single canonical project status document. It inventories all systems, tracks simulation coverage, and maps open gaps/patches per system.

**Update triggers (mandatory):**
- Session Close — update scope map before committing session log
- After any simulation batch — update coverage columns
- After gap register changes — update gap status columns
- After patch propagation — update patch columns
- After design work — update "Untested" counts and gap status

**Update procedure:**
1. Read current `valoria_scope_map.md` from GitHub
2. Apply deltas from session work (new sims, closed gaps, applied patches, new systems)
3. Recalculate Coverage Summary table
4. Update "CRITICAL BLOCKERS" section
5. Update "PRIORITIZED AUDIT PLAN" if priorities shifted
6. Commit updated file

## Skill Registry

| Skill | Model | Trigger |
|-------|-------|---------|
| valoria-chunker | Haiku 4.5 | Input >500 lines |
| valoria-canon-guard | Sonnet 4.6 | New mechanic, audit finding, compilation stage |
| valoria-mechanic-audit | Sonnet 4.6 | Consistency, gaps, formulas, interactions |
| valoria-simulator | Sonnet 4.6 | Stress test, edge case, scenario, probability |
| valoria-compiler | Sonnet 4.6 | Assembly, patching, checkpoint export |
| valoria-dice-model | Haiku 4.5 | Probability tables, EV, opposing rolls, pool splits, balance checks |

**Anti-pattern:** Doing skill work inline. If about to chunk, formula-check, assemble inline, or compute dice probabilities — STOP and route to the skill.

## Workflows

| Workflow | Sequence |
|----------|----------|
| Full Mechanical Audit | chunker(A,C,E) → canon-guard → mechanic-audit(A–E) → gap register → report |
| Philosophy Check | chunker(target) → canon-guard |
| Stress Test Suite | chunker(mechanics+deps) → simulator(A then D) → report |
| Comprehensive Simulation | chunker(A–E) → simulator(E→A→B→C→D) → coverage update → report |
| Targeted Repair | canon-guard → mechanic-audit → [EDITORIAL GATE] → compiler |
| New Mechanic | canon-guard(pre) → mechanic-audit(integration) → simulator(stress) → [EDITORIAL GATE] → compiler |
| Ruleset Assembly | chunker → compiler → canon-guard(final) → export |
| Phase 3 Gate | simulator(Mode E: load coverage matrix) → verify all gate requirements → block if unmet |
| Dice Balance Check | dice-model(Task 1–6) → mechanic-audit(interpretation) → gap register update |

## Phase 3 Gate Requirements

All must pass before final compilation:
- Every M-001–M-056 tested in Isolation + Interaction
- All three game modes covered per applicable mechanic
- All 9 factions tested with generic character
- All named NPCs tested in unique-mechanic scenarios
- All archetypes tested in archetype-defining mechanics
- All tracks tested at: starting / mid-range / threshold / terminal
- Zero untested P1 interactions from dependency graph

## Session Close

1. Update `valoria_scope_map.md` with session deltas (coverage, gaps, patches, blockers).
2. Archive previous `session_log_current.md` → `session_log_archive.md`. Replace current with:

```yaml
session_close: YYYY-MM-DDTHH (use sequence if multiple same-day: T01, T02)
checkpoint: [N]
completed_stages: []
next_action:
  skill: name
  model: required_model
  input_file: filename
editorial_decisions_pending: []
gap_register_delta:
  opened: []
  closed: []
blockers: []
scope_map_updated: true
```

## Editorial Gate

User retains exclusive authority over: setting, worldbuilding, characters, narrative, tone, faction behavior, ambiguous design intent. Flag: `[EDITORIAL: requires user approval — description]`. Claude may execute without approval: formula corrections, consistency fixes, formatting, audits, simulations, dice probability analysis.
