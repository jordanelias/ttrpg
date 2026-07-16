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

## Input Validation (MANDATORY BEFORE ANY SIMULATION)

Before running any simulation mode, read the following from the working tree:

- `references/canonical_sources.yaml` — confirm which design doc is canonical
- the canonical design doc for the target system (from `canonical_sources.yaml`)
- `references/params_<system>.md` — mechanical values
- `canon/02_canon_constraints.md` — P-01–P-15

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

**Forward-only findings-disposition discipline:** every finding above must resolve to either a
filed `ED-<LANE>-NNNN` id (per `references/id_reservations.yaml`'s allocation protocol) or an
explicit no-action line (e.g. "no action — working as intended," "no action — superseded by
PP-NNN"). P1 findings must be filed as ED entries, not merely flagged in the findings section.
Mirrors the disposition-table discipline added to `valoria-mechanic-audit` and
`valoria-vector-audit`'s output contracts in the same audit-ecosystem consolidation batch.
Applies going forward only.

### Mode F — Fieldwork Simulation (G-FW)

Simulate fieldwork operations across investigation, exploration, and socializing tracks.

**Params source:** `params/fieldwork.md`
**Design source:** `designs/scene/fieldwork_v30.md`

**Test categories:**
1. Evidence Track progression rates (Depth 1–5, by action type)
2. Exposure accumulation vs Cover threshold pacing
3. Thread-Read vs mundane investigation efficiency (P1-16 gate: Evidence limited to Depth ≥ 4)
4. Contest Escalation boundary (§5.7 Disposition→CT offset)
5. NPC Disposition trajectory over multi-season investigation
6. Survey action Ob curve by Proximity Rating
7. Church Attention Pool feed rate from fieldwork Exposure (§6.5 caps)
8. Niflhel social toolkit +2 Exposure cost-benefit
9. Combined Findings in Contest (+1D per Finding, max +2D)
10. Cross-territory investigation (one track, per-territory Exposure)

**State tracked:** Evidence Track, Exposure (per territory/character), Disposition (per NPC), Cover level, Church Attention Pool, Finding count/reliability.

### Mode G — Incremental Build Protocol (MANDATORY for multi-module simulations)

**When to use this mode:** Any simulation that requires building new code spanning more than one mechanical system. Examples: full-stack campaign sim, multi-phase combat simulator, integrated threadwork+combat interaction test. Single-module sims (dice engine test, isolated probability distribution) do NOT require this protocol.

**Why this mode exists:** The `sim_v2` failure (2026-04-18) happened because a full-stack simulation was built in a single session, with canonical sources read at index-depth only, and mechanical constants invented to fill gaps in unread sections. Every mechanical assumption in that sim was suspect — the audit found 24 correct / 15 partial / 8 wrong / 5 fabricated / 19 missing assumptions. This mode structurally prevents that failure by decomposing the build across sessions, one module at a time, with canonical verification gated at every step.

---

#### Protocol

**Step 1 — Module decomposition (first session).**

Before writing any code, produce a module manifest at `sim/sim_module_manifest.md`. Each module is a self-contained mechanical layer that can be built, verified, and tested in one session.

Canonical modules for a full-stack Valoria sim (as one example):

| Module | Depends On | Canonical Sources | Est. Session Budget |
|---|---|---|---|
| 1. Dice engine | — | `params/core.md` | 1 session |
| 2. Territory map | — | `designs/world/geography_v30.md`, `params/bg/geography.md` | 1 session |
| 3. Faction layer | dice, territory | `designs/provincial/faction_layer_v30.md`, `params/factions/stats_1_7_scale.md` | 1 session |
| 4. Clock system | faction | `designs/provincial/clock_registry_v30.md`, `params/bg/clocks.md`, `params/bg/tracks.md` | 1 session |
| 5. TC system | clocks, faction | `designs/provincial/tc_political_v30.md`, `params/bg/tc_seizure.md` | 1 session |
| 6. Turmoil + Accord | faction, territory | `designs/provincial/peninsular_strain_v30.md` | 1 session |
| 7. Faction acquisition toolkits | all above | `peninsular_strain_v30 §5`, faction-specific designs | 1–2 sessions |
| 8. Universal victory condition | all above | `peninsular_strain_v30 §6` | 1 session |
| 9. NPC AI priority trees | faction, clocks | `params/bg/npc_priority_trees.md`, `designs/npcs/npc_behavior_v30.md` | 1–2 sessions |
| 10. Phase resolution loop | all above | `params/bg/phases.md` | 1 session |
| 11. Zoom-in personal resolution | combat, thread, social | respective design docs | 2–3 sessions |
| 12. Integration + batch runner | all above | — | 1 session |

The manifest must list: module number, name, dependencies, canonical source paths (resolved via `canonical_sources.yaml`, not guessed), and estimated session budget. Commit the manifest to `tests/sim/<sim-name>/module_manifest.md`.

**Step 2 — Per-module session protocol.**

Each module gets its own session. The session protocol:

1. Read the module manifest from the working tree.
2. Identify the current module (next unchecked in manifest).
3. Read every canonical source listed for this module in FULL — read the whole file, not just the index/headers.
4. Build the verification ledger (e.g. `sim_verification_ledger.json`). Every mechanical constant used in this module must have a ledger entry (sim_variable, value, canonical_source, section, quoted_text). Quoted_text must actually appear in the file content — verify with a string search before adding the entry.
5. Write the module code. Every mechanical constant carries an inline `# [canonical: path §section]` comment OR corresponds to a ledger entry. The fabrication check verifies this at commit.
6. Run module in isolation against known inputs. Outputs logged.
7. Commit the module file with an updated `tests/sim/<sim-name>/module_manifest.md` that marks the module `status: verified`.
8. Record in the relevant `registers/handoffs/HANDOFF_<LANE>.md`: module completed, ledger entries added, next module to build. (Root `HANDOFF.md` only for genuinely cross-cutting items — CLAUDE.md §1/§2.)

**If a session cannot complete a module:** write a checkpoint to the relevant `registers/handoffs/HANDOFF_<LANE>.md` with exactly which canonical sources are read/verified and where the partial code is. Next session resumes from checkpoint.

**Step 3 — Inter-module integration.**

Once all modules in the manifest are marked `status: verified`, a dedicated integration session wires them together. This session does not add new mechanics — only imports and integrates existing module files. If integration reveals that a module was built incorrectly (API mismatch, unverified assumption), flag the module for rebuild; do NOT patch it inline without returning to the canonical sources.

**Step 4 — Batch testing.**

After integration, run the sim against a batch of seeds (10+, ideally 50+). Analyze outcomes for: victory distribution, clock ranges, faction elimination rates, any results that contradict canonical design intent. Findings go into the standard Mode D edge-case format.

---

#### Rules that override other Modes

These are non-negotiable for incremental build sims:

- **No multi-module code in a single session.** If the module takes more than one session, checkpoint and resume. Never finish a module by compressing or skipping reads.
- **No mechanical constant without a ledger entry OR inline citation.** `sim_fabrication_check()` enforces this at commit. Do not try to work around it by using variables named after the value.
- **No assumption that a previously-built module is correct.** Each session re-verifies the imports it uses by re-reading the canonical source from the working tree for the specific values being read from upstream modules.
- **No cross-module "fixing" in integration.** If integration reveals a module is wrong, the module is flagged for rebuild in its own session. Do not patch.
- **All sims that use Mode G commit to `tests/sim/<sim-name>/` as a directory.** Module files, manifest, ledger snapshot, and batch outputs all live there.

---

#### Anti-patterns (what sim_v2 did — do not repeat)

| Anti-pattern | Why it failed | What to do instead |
|---|---|---|
| Build a "v1" sim across a single session covering all systems | Canonical sources get read at index depth because there's no time to infill everything | Module decomposition, one system per session |
| Read only the index/headers of design docs, build mechanics from section titles | Section titles imply structure but not mechanical values; code gets built on inference | Always read the full design doc for docs used in a module's canonical source list |
| Invent victory conditions, elimination rules, and clock thresholds because they "sound right" | Violates canonical system in non-obvious ways; produces superficially valid outputs | Every mechanic traced to a verified ledger entry; if the ledger can't cite it, the mechanic isn't built yet |
| Run 50-seed batches on a sim that failed validation | Compounds the fabrication: bad results look statistically rigorous and get trusted | No batch runs before all modules pass `status: verified` in the manifest |
| Assume "the structure is right, I'll fix values later" | Never happens; the sim gets committed and used as reference | The structure IS the values — fix at commit time or don't commit |

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
- All mechanical values must be sourced from the working-tree params or design doc. Never use remembered values.

## Dashboard registry logging (MANDATORY on completion)

When this skill's run concludes — pass, fail, or partial — append one record to the
Valoria audit/simulation-run registry (`references/audit_registry.jsonl`) so the
GitHub Pages dashboard and `tools/ci_audit_registry_check.py` can see it. Do this
every time, not only on request — a skipped append is what makes the dashboard's
verdict table go stale.

```bash
python tools/audit_registry.py append \
  --audit-type simulation_balance \
  --subsystem <personal_combat|mass_battle|social_contest|faction_political|settlement_territory|threadwork|fieldwork_investigation|architecture|cross_cutting|corpus_wide> \
  --skill valoria-simulator \
  --date <YYYY-MM-DD> \
  --folder "<designs/audit/... path this run's output actually lives at>" \
  --scope "<one-line: what was audited>" \
  --verdict <this skill's own verdict, mapped to PASS|FAIL|PARTIAL|CONFORMANT|NON_CONFORMANT|OPEN|MIXED|CLOSED> \
  --verdict-detail "<one-line context, e.g. a PR number or ratification note>"
```

Pick `--subsystem` from what the run actually targeted (`cross_cutting` if it
genuinely spans several, `corpus_wide` only for a whole-corpus pass). See
`tools/audit_registry.py`'s module docstring for the full field/vocabulary
reference — this is the single source of truth for the schema, not this note.
