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

## Input Validation (MANDATORY BEFORE ANY SIMULATION)

Before running any simulation mode, verify the following have been fetched from GitHub this session:

```python
# Required files — fetch via g.read_files_graphql() if not already in context
required = [
    'references/canonical_sources.yaml',       # confirm which design doc is canonical
    '<canonical design doc for target system>', # from canonical_sources.yaml
    'references/params_<system>.md',            # mechanical values
    'canon/02_canon_constraints.md',            # P-01–P-15
]
```

**Memory contamination warning:** userMemories may contain mechanical values (track values, territory data, faction stats, etc.) that feel current but are not fetched from GitHub. Do not use any value from memory as a source for mechanical analysis. Fetch only.

**If any required file was not fetched from GitHub this session:** STOP. Fetch it. Do not substitute memory or local file content.

**Fetch log (emit before any analysis):**
```
## FETCH LOG
session token: [16-char hex — from g.assert_fetched() call above]
canonical_sources.yaml: ✓ fetched ([N] lines)
[canonical design doc path]: ✓ fetched ([N] lines)
references/params_[system].md: ✓ fetched ([N] lines) / ✗ missing
```
If any required file is missing from this log, or session token is absent, stop — the analysis is invalid.

**Version check:** confirm `<!-- version: -->` tag in each fetched params file matches current ruleset version in `compilation/README.md`. If mismatch: flag `[STALE PARAMS: <file> is vX.XX, current is vY.YY]` and stop.

**If `canonical_sources.yaml` is not loaded:** STOP. You cannot know which design doc is current.

## Simulation Modes

### Mode A — Single Mechanic Isolation
Test one mechanic across its full input range.

**Procedure:**
1. Identify all input variables and their valid ranges
2. Calculate output at: minimum, 25th percentile, median, 75th percentile, maximum inputs
3. For dice pools: calculate P(success), P(partial), P(failure), P(overwhelming) at each Ob value
4. Identify: impossible states, degenerate cases (auto-success/auto-fail), plateau effects, cliff effects

**Output:** `sim_[mechanic]_isolation.md`
```
## [Mechanic Name]
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

**Output:** `sim_[chain_name]_interaction.md`

### Mode C — Full Scenario Simulation
Run a complete game situation with full state tracking.

**Scenario types:** Combat encounter, social scene, thread operation sequence, faction turn, mixed scene, multi-session campaign arc.

**State tracking format (MANDATORY for every step):**
```markdown
## State: [Round/Phase/Season N]
### Characters
[Name] — Coord [N], End [N], Health [N/max], Wounds [N/max], Composure [N/max]
  Pools: [relevant pre-calculated pools]
  Conditions: [list]

### Tracks
TT [N] | TC [N] | IP [N]

### Practitioner (if applicable)
[Name] — TS [N], TD [N/20], Taint [N/10], Certainty [N/max], Contact [N rounds remaining]

### Factions (if applicable)
[Name] — M[N] R[N] W[N] S[N]

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

**Output:** `sim_scenario_[name].md`

### Mode D — Edge Case Discovery (EXHAUSTIVE)
Systematic search across nine categories:

| Category | What to Find | Method |
|----------|-------------|--------|
| **Boundary** | Behavior at 0, max, threshold crossings | Test every track at every threshold value |
| **Cascade** | Chain reactions that amplify uncontrollably | Trace worst-case propagation paths |
| **Regression** | Mechanics that reference themselves | Check if output loops back as input |
| **Deadlock** | States with no valid action | Enumerate all possible actions at extreme states |
| **Crunch Cascade** | Too many simultaneous calculations for table play | Count resolution steps per round at peak complexity |
| **Ambiguity** | Rules that don't specify outcomes | Find simultaneous trigger conditions with no priority rule |
| **Incoherence** | Logically impossible results | Check for mutual exclusion violations |
| **Optimal Play** | Strategies that trivialize the system | Find dominant strategies, stack exploits |
| **Degenerate** | Inputs that make mechanics meaningless | Find auto-success and auto-fail thresholds |

**For each finding:**
```markdown
### [Category]: [Brief title]
**Setup:** [what conditions produce this]
**Mechanism:** [how it happens mechanically]
**Severity:** P1 (breaks game) / P2 (produces bad play experience) / P3 (minor oddity)
**Frequency:** [how likely in normal play]
**Proposed fix:** [if obvious — otherwise flag for mechanic-audit]
```

**Output:** `sim_edge_cases_[domain].md`

### Mode E — Coverage Matrix
Track which mechanics have been tested in which modes.

**Output:** `sim_coverage_matrix.md` (persistent — updated after each simulation)
```
| Mechanic ID | Name | Isolation | Interaction | Scenario | Edge Cases | Status |
```
Status: Not started / In progress / Complete / Issues found

## Probability Reference (d10 pool, TN7)

Pre-computed for efficiency. P(die ≥ TN) per die:
- TN5: 0.6 per die (+ chain on 10)
- TN6: 0.5 per die (+ chain)
- TN7: 0.4 per die (+ chain)
- TN8: 0.3 per die (+ chain)

With 1s subtracting: P(net success per die at TN7) ≈ 0.3.
Expected net successes per die at TN7 ≈ 0.33.

Quick reference:
| Pool | Expected Net (TN7) | P(≥1 net) | P(≥2 net) | P(≥3 net) |
|------|-------------------|-----------|-----------|----|
| 4D | 1.3 | ~80% | ~50% | ~25% |
| 6D | 2.0 | ~92% | ~70% | ~45% |
| 8D | 2.6 | ~97% | ~82% | ~60% |
| 10D | 3.3 | ~99% | ~90% | ~73% |
| 12D | 4.0 | ~99% | ~95% | ~83% |
| 15D | 5.0 | ~99% | ~98% | ~92% |

*For critical edge cases, compute exact binomial distributions.*

## Rules
- Always show the math. Never assert an outcome without probability backing.
- Track ALL state changes. Missing a track update invalidates the simulation.
- P1 findings: immediately flag in findings section.
- After each simulation: update `sim_coverage_matrix.md` and commit findings.
- Simulations exceeding 30 resolution steps: checkpoint mid-simulation, summarize state, continue.
**Pre-commit (run before every `atomic_commit()` call):**
```bash
python3 tools/freshness_gate.py --update
python3 tools/broken_dependency_checker.py
python3 tools/patch_propagation_checker.py
```
Exit 0 required on all three. On non-zero exit: fix the reported issue before committing.

**Post-commit verification:** after `atomic_commit()` returns a SHA, re-fetch all files modified in that commit and confirm content matches what was committed. If content differs: flag immediately, do not proceed.

**Re-fetch after writes:** after any `atomic_commit()` call, re-fetch all modified files before referencing them again in the same session. The in-context version and the committed version may differ.

- All mechanical values must be sourced from the GitHub-fetched params or design doc. Never use remembered values.
