# Valoria Skill Registry
# All on-demand skills. Fetched from GitHub when dispatched.
# Format: skill name | GitHub path | model tier | trigger keywords

---

## Tier 1: Subsystem Simulators

### valoria-sim-combat
- Path: `skills/valoria-sim-combat/SKILL.md`
- Model: Sonnet 4.6
- Triggers: combat, fight, attack, weapon, armour, armor, wound, initiative, melee, ranged, damage, parry, pool split, offence, defence, zone combat, mass combat at personal scale
- NOT for: mass battle (armies) → use valoria-sim-mass-battle

### valoria-sim-threadweaving
- Path: `skills/valoria-sim-threadweaving/SKILL.md`
- Model: Sonnet 4.6
- Triggers: thread, weaving, pulling, mending, leap, TS, TD, TT, coherence, certainty, co-movement, dissolution, thread tension, thread substrate, practitioner, thread operation, past-oriented, discovery cascade

### valoria-sim-social
- Path: `skills/valoria-sim-social/SKILL.md`
- Model: Sonnet 4.6
- Triggers: social, rhetoric, debate, grand debate, appeal, negotiation, impression track, composure, knot, rattled, conviction, presence, reading exchange, parliamentary vote

### valoria-sim-mass-battle
- Path: `skills/valoria-sim-mass-battle/SKILL.md`
- Model: Sonnet 4.6
- Triggers: mass battle, siege, army, unit, garrison, fortification, cohesion, military, attacker, defender, disposition, formation, terrain, sortie, relief

---

## Tier 2: Mode Simulators

### valoria-sim-ttrpg
- Path: `skills/valoria-sim-ttrpg/SKILL.md`
- Model: Sonnet 4.6
- Triggers: TTRPG scene, full scene, register shift, personal scale, faction turn, multi-scale, NPC scene, character scene
- Invokes Tier 1 params directly (not SKILL.md files)

### valoria-sim-boardgame
- Path: `skills/valoria-sim-boardgame/SKILL.md`
- Model: Sonnet 4.6
- Triggers: board game turn, BG turn, seasonal accounting, faction order, territory, NPC AI, campaign arc, 10-season, strategic, victory condition, clock drift

### valoria-sim-hybrid
- Path: `skills/valoria-sim-hybrid/SKILL.md`
- Model: Sonnet 4.6
- Triggers: hybrid, zoom in, zoom out, mode transition, state transfer, interruption, TTRPG to board game, board game to TTRPG, mode boundary

---

## Tier 2.5: Sim Orchestrator

### valoria-sim-orchestrator
- Path: `skills/valoria-sim-orchestrator/SKILL.md`
- Model: Sonnet 4.6
- Triggers: coverage, coverage matrix, cascade, cross-subsystem, campaign arc dispatch, batch dispatch, NPC test requirements, faction test matrix, what hasn't been tested, simulation plan
- Modes: Route · Coverage · Cascade · Campaign-arc

---

## Tier 3: Analysis

### valoria-canon-guard
- Path: `skills/valoria-canon-guard/SKILL.md`
- Model: Sonnet 4.6
- Triggers: canon, philosophy, foundations, P-01 through P-14, compliance, philosophical violation, setting check, NPC conviction, lore check, integration check
- Modes: Mechanical · Setting · Integration
- Also invoked automatically by Canon Gate protocol

### valoria-mechanic-audit
- Path: `skills/valoria-mechanic-audit/SKILL.md`
- Model: Sonnet 4.6
- Triggers: audit, consistency, mechanic check, cross-reference, formula, number system, interaction, what's broken, what's missing, gap detection, redundancy

### valoria-dice-model
- Path: `skills/valoria-dice-model/SKILL.md`
- Model: Haiku 4.5
- Triggers: probability, dice math, expected value, success rate, roll odds, Monte Carlo, distribution, TN, Ob

---

## Tier 4: State Management

### valoria-editorial-ledger
- Path: `skills/valoria-editorial-ledger/SKILL.md`
- Model: Sonnet 4.6
- Triggers: editorial decision, lore decision, affects list, propagation, ledger entry, E-NNN, NOT_APPLIED, setting confirmed, name confirmed
- Also invoked automatically by Editorial Decision Protocol

### valoria-compiler
- Path: `skills/valoria-compiler/SKILL.md`
- Model: Sonnet 4.6
- Triggers: compile, assemble, checkpoint, export, new version, CP15, full assembly, manifest, diff

### valoria-chunker
- Path: `skills/valoria-chunker/SKILL.md`
- Model: Haiku 4.5
- Triggers: chunk, section map, index, large document, 500 lines, prepare for analysis, extract sections
