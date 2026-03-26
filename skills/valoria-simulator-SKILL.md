---
name: valoria-simulator
description: >
  Comprehensive mechanical stress testing for Valoria. Builds scenarios, runs probability analysis,
  tracks all state changes, discovers edge cases, friction points, infinite regressions, and crunch
  cascades. ALWAYS use this skill when simulating mechanics, stress testing, running scenarios,
  testing edge cases, checking what breaks, evaluating probability distributions, or validating
  that mechanics work in play. Trigger on: "simulate", "stress test", "run a scenario",
  "test this mechanic", "edge cases", "what breaks", "probability", "does this work in play",
  "push this to its limits", or when the orchestrator routes a simulation.
---

**Model:** Sonnet 4.6. Requires multi-step mechanical reasoning with full state tracking.
**Input:** Specific mechanics (chunked) + `mechanics_index.md` for dependencies.
**Critical:** Use expected values and probability distributions, NOT random dice rolls.

## 7-Dimension Coverage Tagging — MANDATORY

Every test scenario MUST be tagged across all seven dimensions before execution:

```
Test ID: SIM-[NNN]
Mechanics: [M-xxx, M-yyy, ...]
Game Mode: [TTRPG | BG | HYB]
Temporal: [PAST | PRES | FUT | CROSS]
Tracks: [TT, TC, IP, TS, TD, INT, CERT, COMP, TLK, PI, DD, CE, FSTAT — list all touched]
Factions: [list all involved]
NPCs: [list named NPCs, or "Generic [Faction]" for faction representatives]
Archetypes: [list archetypes represented]
```

### Named NPC Test Requirements
Every named NPC must be tested in scenarios that exercise their unique mechanics:

| NPC | Unique Mechanics | Min Scenarios |
|-----|------------------|---------------|
| Almud | Elevated TS, political paralysis, succession trigger | 2 |
| Lenneth | Covert networks, scholarly TS path, Revolution endowment | 2 |
| Torben | Loyalty Clock, tutoring demand, covert contact, retrieval | 2 |
| Elske | Conviction split, multi-faction recruitment, independence | 2 |
| Himlensendt | Devout Constraint (sincere), TC driver, institutional expansion | 2 |
| Olafsson | Cardinal mechanics, Church politics | 1 |
| Klapp | Cardinal mechanics, intelligence ops | 1 |
| Baralta | Devout + legalist, jurisdiction claim vs Confessor | 2 |
| Vaynard | Secret Thread research, artifact pursuit, Inquisitor risk | 2 |
| Maret Uln | Practitioner, Southernmost, Revolution adjacency | 2 |
| Ehrenwall | Coup trigger, Martial Law, Crown loyalty tracking | 2 |

Additionally: each NPC in at least one cross-faction interaction test.

### Generic Faction Character Requirements
For each of the 8 factions + Schoenland spoiler: create one generic character and test in:
- Domain Actions (where applicable)
- Faction stat changes
- Seasonal accounting
- At least one inter-faction interaction
- Mode-specific operations (TTRPG personal, BG strategic, HYB transition)

## Simulation Modes

### Mode A — Single Mechanic Isolation
Test one mechanic across its full input range.

**Procedure:**
1. Identify all input variables and their valid ranges
2. Calculate output at: minimum, 25th percentile, median, 75th percentile, maximum inputs
3. For dice pools: calculate P(success), P(partial), P(failure), P(overwhelming) at each Ob value
4. Identify: impossible states, degenerate cases (auto-success/auto-fail), plateau effects, cliff effects

**Output format:**
```
## [Mechanic Name] — Isolation Test
### Tags
Mechanics: M-xxx | Mode: [all applicable] | Temporal: [x] | Tracks: [x] | Factions: [if applicable] | NPCs: [if applicable] | Archetypes: [x]
### Input Space
| Variable | Range | Typical | Edge |
### Probability Table
| Pool Size | Ob | P(Overwhelming) | P(Success) | P(Partial) | P(Failure) |
### Findings
- [degenerate cases, cliff effects, etc.]
```

### Mode B — Interaction Chain
Test two or more mechanics that interact.

**Procedure:**
1. Map the interaction: Mechanic A output → Mechanic B input
2. Build representative scenarios where the chain fires
3. Run the chain with varying inputs
4. Find: cascading failures, amplification loops, contradictory results, unexpected emergent behavior

### Mode C — Full Scenario Simulation
Run a complete game situation with full state tracking.

**Scenario types:** Combat encounter, social scene, thread operation sequence, faction turn, mixed scene, multi-session campaign arc, NPC-specific crisis, cross-faction confrontation.

**State tracking format (MANDATORY for every step):**
```markdown
## State: [Round/Phase/Season N]
### Characters
[Name] — Agi [N], End [N], Str [N], Cog [N], Mem [N], Foc [N], Att [N], Bon [N], Pres [N], Spi [N]
  Health [N/max], Wounds [N/max], Composure [N/max]
  Pools: [relevant pre-calculated pools]
  Conditions: [list]

### Tracks
TT [N] | TC [N] | IP [N] | PI [N] | TLK [N] (if applicable)

### Practitioner (if applicable)
[Name] — TS [N], TD [N/20], Intelligibility [N/10], Certainty [N/max], Contact [N rounds remaining]

### Factions (if applicable)
[Name] — Mand[N] Inf[N] Wea[N] Mil[N] Int[N] Stab[N]

### Active Conditions
[list of all active modifiers, penalties, temporary effects]
```

**Resolution format:**
```markdown
## Action: [description]
Pool: [N]D, TN [N], Ob [N]
P(Overwhelming): [%] | P(Success): [%] | P(Partial): [%] | P(Failure): [%]
Expected net successes: [N]
### Most likely outcome: [degree]
[resolve consequences, update state]
### State Delta
[what changed — every track, every condition]
### Findings
[edge cases, friction, issues discovered this step]
```

### Mode D — Edge Case Discovery (EXHAUSTIVE)
Systematic search across nine categories:

| Category | What to Find | Method |
|----------|-------------|--------|
| Boundary | Behavior at 0, max, threshold crossings | Test every track at every threshold value |
| Cascade | Chain reactions that amplify uncontrollably | Trace worst-case propagation paths |
| Regression | Mechanics that reference themselves | Check if output loops back as input |
| Deadlock | States with no valid action | Enumerate all possible actions at extreme states |
| Crunch Cascade | Too many simultaneous calculations for table play | Count resolution steps per round at peak complexity |
| Ambiguity | Rules that don't specify outcomes | Find simultaneous trigger conditions with no priority rule |
| Incoherence | Logically impossible results | Check for mutual exclusion violations |
| Optimal Play | Strategies that trivialize the system | Find dominant strategies, stack exploits |
| Degenerate | Inputs that make mechanics meaningless | Find auto-success and auto-fail thresholds |

### Mode E — Coverage Matrix Update
After every simulation run, update the 7-dimension coverage matrix.

**Matrix format:**
```
| Test ID | Mechanics | Mode | Temporal | Tracks | Factions | NPCs | Archetypes | Status | Findings |
```

### Mode F — NPC Stress Test (NEW)
Dedicated mode for testing named NPCs in their unique mechanical contexts.

**Procedure per NPC:**
1. Load NPC's mechanical profile (stats, unique mechanics, faction position)
2. Run NPC through their defining scenario (e.g., Ehrenwall: Crown loyalty assessment → coup threshold)
3. Run NPC in cross-faction interaction (e.g., Ehrenwall vs Almud compromise count)
4. Track: what breaks, what produces degenerate outcomes, what creates compelling play
5. Verify: NPC's unique mechanics interact correctly with general systems

**Output per NPC:**
```
## NPC: [Name] — Stress Test
### Tags (7-dimension)
### Profile Summary
### Scenario 1: [Defining scenario]
[full state tracking + resolution]
### Scenario 2: [Cross-faction interaction]
[full state tracking + resolution]
### Findings
- Mechanical: [what works, what breaks]
- Narrative: [does the mechanic produce interesting decisions?]
- Cross-system: [unexpected interactions with other mechanics]
```

## Probability Reference (d10 pool)

Pre-computed for efficiency. P(die ≥ TN) per die:
- TN5: 0.6 per die (+ chain on 10)
- TN6: 0.5 per die (+ chain)
- TN7: 0.4 per die (+ chain)
- TN8: 0.3 per die (+ chain)

With 1s subtracting: expected net successes per die at TN7 ≈ 0.33.

| Pool | Expected Net (TN7) | P(≥1 net) | P(≥2 net) | P(≥3 net) |
|------|-------------------|-----------|-----------|-----------|
| 4D | 1.3 | ~80% | ~50% | ~25% |
| 6D | 2.0 | ~92% | ~70% | ~45% |
| 8D | 2.6 | ~97% | ~82% | ~60% |
| 10D | 3.3 | ~99% | ~90% | ~73% |
| 12D | 4.0 | ~99% | ~95% | ~83% |
| 15D | 5.0 | ~99% | ~98% | ~92% |

## Rules
- Always show the math. Never assert an outcome without probability backing.
- Track ALL state changes. Missing a track update invalidates the simulation.
- Tag ALL seven dimensions on every test. Untagged tests are invalid.
- When a finding is P1 severity: immediately flag in the findings section.
- After each simulation: update coverage matrix (Mode E).
- Simulations exceeding 30 resolution steps: checkpoint mid-simulation, summarize state, continue.
- Test named NPCs in their unique-mechanic scenarios, not generic situations.
- Test generic faction characters in faction-relevant mechanics for every faction.
