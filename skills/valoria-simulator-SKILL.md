# valoria-simulator

Stress testing: probability analysis, state tracking, edge case discovery, coverage matrix maintenance.

**Model:** Sonnet 4.6.
**Input:** Specific mechanics (chunked) + `mechanics_index.md` for dependencies.
**Rule:** Use expected values and probability distributions, NOT random dice rolls.

## 7-Dimension Tagging — Mandatory on Every Test

```
Test ID: SIM-[NNN]
Mechanics: M-xxx, M-yyy | Mode: TTRPG/BG/HYB | Temporal: PAST/PRES/FUT/CROSS
Tracks: [all touched] | Factions: [all involved] | NPCs: [named or "Generic [Faction]"]
Archetypes: [all represented]
```

Track codes: TT, TC, IP, TS, TD, INT, CERT, COMP, TLK, PI, DD, CE, FSTAT

## Modes

### A — Isolation
One mechanic, full input range. Calculate at min/25th/median/75th/max. For dice pools: P(success/partial/failure/overwhelming) per Ob. Flag: impossible states, degenerate cases, plateaus, cliffs.

### B — Interaction Chain
Two+ interacting mechanics. Map A→B, run with varying inputs. Find: cascades, amplification loops, contradictions, emergent behavior.

### C — Full Scenario
Complete game situation with mandatory state tracking every step:
```
## State: [Round/Phase/Season N]
[Name] — [10 attrs], Health/Wounds/Composure, Pools, Conditions
Tracks: TT/TC/IP + practitioner tracks if applicable + faction stats if applicable
## Action: [description]
Pool: [N]D TN[N] Ob[N] — P(Overwhelming/Success/Partial/Failure) — Expected net: [N]
### Most likely outcome → resolve → State Delta → Findings
```

### D — Edge Case Discovery
Nine categories: Boundary (0/max/threshold), Cascade (uncontrolled amplification), Regression (self-reference), Deadlock (no valid action), Crunch Cascade (too many calcs), Ambiguity (no priority rule), Incoherence (impossible results), Optimal Play (dominant strategies), Degenerate (auto-success/fail).

### E — Coverage Matrix Update
Update `tests/coverage_matrix.md` (root, canonical copy) after every run.
```
| Test ID | Mechanics | Mode | Temporal | Tracks | Factions | NPCs | Archetypes | Status | Findings |
```

### F — NPC Stress Test
Per NPC: load profile → run defining scenario → run cross-faction interaction → track what breaks/degenerates/creates compelling play.

**NPC minimum scenarios:**

| NPC | Unique Mechanics | Min |
|-----|------------------|-----|
| Almud | Elevated TS, political paralysis, succession trigger | 2 |
| Lenneth | Covert networks, scholarly TS, Revolution endowment | 2 |
| Torben | Loyalty Clock, tutoring demand, covert contact, retrieval | 2 |
| Elske | Conviction split, multi-faction recruitment, independence | 2 |
| Himlensendt | Devout Constraint (sincere), TC driver, expansion | 2 |
| Olafsson | Cardinal mechanics, Church politics | 1 |
| Klapp | Cardinal mechanics, intelligence ops | 1 |
| Baralta | Devout + legalist, jurisdiction vs Confessor | 2 |
| Vaynard | Secret Thread research, artifacts, Inquisitor risk | 2 |
| Maret Uln | Practitioner, Southernmost, Revolution adjacency | 2 |
| Ehrenwall | Coup trigger, Martial Law, Crown loyalty | 2 |

**Generic faction characters:** One per faction (8 + Schoenland), each tested in: Domain Actions, faction stat changes, seasonal accounting, inter-faction interaction, mode-specific operations.

## Probability Reference (d10 pool, 1s subtract)

Expected net per die at TN7 ≈ 0.33.

| Pool | E[Net] TN7 | P(≥1) | P(≥2) | P(≥3) |
|------|-----------|-------|-------|-------|
| 4D | 1.3 | ~80% | ~50% | ~25% |
| 6D | 2.0 | ~92% | ~70% | ~45% |
| 8D | 2.6 | ~97% | ~82% | ~60% |
| 10D | 3.3 | ~99% | ~90% | ~73% |
| 12D | 4.0 | ~99% | ~95% | ~83% |
| 15D | 5.0 | ~99% | ~98% | ~92% |

## Rules
- Show math. No unsubstantiated outcomes.
- Track ALL state changes. Missing update = invalid simulation.
- Tag all 7 dimensions. Untagged = invalid.
- P1 findings: flag immediately.
- >30 resolution steps: checkpoint mid-sim.

### G — Subsystem Simulation
Dedicated modes for subsystems that require state structures not covered by Mode C.
Call the appropriate submode; do not use generic Mode C for these.

**G1 — Mass Combat**
State block per unit group:
```
## State: Season N / Battle Round N
[Unit] — Type, Size, Morale, Wounds, Commander TS/TD
Clocks: TC=[N] | Seasonal Stability=[N]
## Action: [manoeuvre]
Pool: [N]D TN[N] Ob[N] → outcome
### Casualties → Morale check → Routing condition? → State Delta
```
Track: unit attrition rates, commander wound propagation, clock interactions, retreat/rout triggers.
Flag: mass combat actions that resolve faster than personal combat (pacing mismatch → P2), Ob values that make routing near-automatic at average unit quality (→ P1).

**G2 — Debate**
State block:
```
## Debate Round N
[Participant] — Composure=[N], Rhetoric pool=[N], Stance=[Offense/Defense/Redirect]
Appeal type: [Logos/Pathos/Ethos] | Target: [Belief/Position]
Pool: [N]D TN[N] Ob[N] → outcome
### Composure damage → Concession threshold? → State Delta
```
Track: composure degradation curve, dominant strategy detection (is one appeal type always optimal?), stalemate conditions.
Flag: debate that terminates in <3 rounds at median pools (too fast → P2), debates with no path to resolution (stalemate → P1).

**G3 — Threadwork**
State block:
```
## Thread Operation
Practitioner — TS=[N], TD=[N], Coherence=[N], Active Knots=[list]
Operation: [type] | Target: [thread descriptor]
Co-movement: Temporal auto-effect=[N] | Epistemic=[N] | Actual=[N]
Pool: [N]D TN[N] Ob[N] → outcome
### All three auto-effects resolve → State Delta → Gap formation check
```
Track: all three dimensional auto-effects fire on every operation (P-01 compliance check embedded). Flag: any operation path where an auto-effect can be skipped → P1 (canon violation).

**G4 — Faction Play (Seasonal)**
State block:
```
## Season N
[Faction] — Stats: M/E/I/C/L=[N] | Stability=[N] | Domain Actions=[N]
## Domain Action: [type]
Resolution: [roll or auto] → effect
### Faction stat change → Clock impact → Inter-faction consequence → State Delta
```
Run full seasonal cycle: all 8 factions + Schoenland AI. Track: clock accumulation rates, faction collapse conditions, first-mover advantages, dominant strategies.
Flag: any faction with no viable domain action at median stats (→ P1), any clock that reaches threshold in <3 seasons without player action (→ P2).

**G5 — Board Game Mode**
Use BG state structure from `compilation/v0.14/stage_bg_board_game_mode.md`.
Run: full turn sequence for 3-player game, 4-player, max-player. Track: turn length estimate (human time), action count per player per round, information load (face-up vs hidden).
Flag: any turn sequence exceeding 8 minutes at median play speed → P2. Any player with no meaningful action for 2+ consecutive rounds → P1.

### H — Substitution Analysis
Test whether NPCs and factions can be mechanically substituted without breaking scenarios.

**Per named NPC:** Run their defining scenario once with the canonical NPC, once with a Generic [Faction] substitute. Compare: outcome distribution, mechanical pressure points, narrative branch availability. Flag if substitution produces meaningfully different mechanical outcomes (→ NPC's mechanics are load-bearing, note it) or identical outcomes (→ NPC mechanics are cosmetic, flag as P3 simplification candidate).

**Per faction:** Run one seasonal cycle with canonical faction, once with a faction swapped to adjacent political position. Flag: scenarios that only work with specific faction identity → document as hard dependency.

### I — Patch, Editorial Output, and Mandatory Commit

**This mode is not optional. It runs after EVERY simulation. No exceptions.**

After completing any simulation run, execute this protocol in order:

**Step 1 — Classify all findings:**
- Mechanical patch (P1/P2): Claude executes, no approval needed
- Editorial gap (requires user decision): flag and add to ledger
- Provisional decision: Claude makes defensible choice, marks `[PROVISIONAL]`, flags for user review
- Confirmed working: note in coverage matrix, no action

**Step 2 — Apply mechanical patches immediately:**
For each P1/P2 mechanical finding:
```
[PATCH PP-NNN]
Finding: [description]
Source: SIM-[NNN]
Change: [exact rule text — quote the new sentence(s)]
Applied to: designs/[path] (NOT compilation/)
Canon risk: NONE | LOW | REVIEW-NEEDED
```
Apply the patch text directly to the relevant design document. Update `references/params_*.md` if the patch affects extracted values.

**Step 3 — Add to patch register:**
Append to `canon/patch_register.yaml`:
```yaml
- id: PP-NNN
  date: YYYY-MM-DD
  severity: P1 | P2 | P3
  description: "[one line]"
  finding_id: "SIM-NNN-Fx"
  source: simulation
  affects: [designs/path/to/file.md]
  status: applied
  applied_commit: "pending"
```

**Step 4 — Add editorial items to ledger:**
For each editorial finding, append to `canon/editorial_ledger.yaml` with next ED-NNN id.
For provisional decisions made by Claude, use `status: provisional` and mark text with `[PROVISIONAL: ...]`.

**Step 5 — Update coverage matrix:**
Append row to `tests/coverage_matrix.md`. Include all 7 dimensions and link to findings.

**Step 6 — UPDATE PROPAGATION MAP (mandatory, before commit):**
For every design doc patched in Step 2:
1. Check `references/propagation_map.md` — does a row exist for this file?
2. If yes: verify all listed propagation targets are included in this commit (or explicitly noted as `[no-prop: reason]`).
3. If no row exists: add one now using the auto-update rules in the map's DEPENDENCY RULES section.
4. For each new cross-reference identified by this simulation finding: add it to the map.
Never skip this step. A commit that adds a new design relationship without updating the map breaks the propagation chain.

**Step 7 — ATOMIC COMMIT (mandatory):**
One commit containing: test file (tests/) + patched design doc(s) + params file(s) + patch_register + editorial_ledger + coverage_matrix + **propagation_map**.
```
Commit message: [simulation] sim_[system]_[N] — PP-NNN applied, ED-NNN added, SIM-DEBT flagged if applicable
```
If the commit is not made, the simulation is incomplete. Do not proceed to the next task.

**Step 8 — Report to user:**
```
Sim complete: [N] findings. P1: [N] (patched). P2: [N] (patched). Editorial: [N] (logged). Provisional: [N] (flagged).
Prop map: [N] new entries added.
Committed: [short hash]
```

**Step 7 — Report to user:**
```
Sim complete: [N] findings. P1: [N] (patched). P2: [N] (patched). Editorial: [N] (logged). Provisional: [N] (flagged).
Committed: [short hash]
```



### J — Cognitive Load and Time Audit

Per mechanic under test, measure and report:

**Cognitive load score (1–10):**
Count per single resolution:
- Mandatory decisions (player must choose between options): +1 per decision
- Mandatory lookups (player must reference a table, formula, or condition list): +1 per lookup
- Parallel tracks (values held in working memory simultaneously): +1 per track
- Sequential dependencies (B cannot resolve until A is known): +1 per dependency

Score: total count. Flag at ≥ 5 (borderline), ≥ 7 (problem), ≥ 9 (redesign).

Compare against precedent: BW Duel of Wits = 6, TI4 combat = 4, D&D 5e spell slot combat = 5.

**Time estimate (human minutes at table):**
- Novice (first 3 sessions): N minutes per resolution
- Experienced (10+ sessions): N minutes per resolution
- Expert (campaign-level): N minutes per resolution

Estimate method: count decision points × 30 seconds (novice) / 15 seconds (experienced) / 8 seconds (expert) + lookup time (45s/15s/5s each) + arithmetic time (20s/10s/5s per calculation).

Flag: any mechanic where novice time > 3 minutes per single resolution (P2), > 5 minutes (P1).

Output format:
```
[MODE J: mechanic name]
Decisions: N (list them)
Lookups: N (list them)
Parallel tracks: N (list them)
Sequential dependencies: N (list them)
Load score: N/10 — [OK / BORDERLINE / PROBLEM / REDESIGN]
Time (novice/experienced/expert): Nm / Nm / Nm
Flag: [NONE / P2: reason / P1: reason]
```

### K — Cross-Mode Delta and Transition Stress Test

Two sub-modes. Run both for any mechanic that spans multiple game modes.

**K1 — Cross-Mode Delta:**
Run the mechanic in TTRPG, then Hybrid, then Board Game.
For each mode, record:
- Pool/formula used
- Resolution steps
- Outcome distribution (expected values)
- Strategic incentives produced (dominant strategies, dead choices)
- What information the player needs vs what is available

Output a delta table:
```
| Property        | TTRPG | Hybrid | Board Game |
|----------------|-------|--------|------------|
| Pool/formula   |       |        |            |
| Steps          |       |        |            |
| E[outcome]     |       |        |            |
| Dominant strat |       |        |            |
| Dead choice?   |       |        |            |
| Info available |       |        |            |
```

Flag: any property where BG and TTRPG produce opposite strategic incentives (P1), any mode where a choice becomes mechanically irrelevant (P2).

**K2 — Transition Stress Test:**
Test the handoff at each mode boundary using the state transfer spec (see `references/state_transfer_spec.md`).

For each transition type (TTRPG→Hybrid, BG→Hybrid, Hybrid→TTRPG, Hybrid→BG, and within-TTRPG Register Shifts):

1. **State inventory check:** List all variables active at point of transition. Verify each is handled: transferred, converted, suspended, or discarded. Any variable not explicitly handled = P1 gap.

2. **Interruption test:** Trigger the transition at each possible phase/step of the source mode. Verify: source mode state is correctly preserved or resolved, target mode receives complete starting state, no orphaned actions or pending resolutions remain.

3. **Zoom In/Out fidelity:** Run a Zoom In from BG battle to TTRPG personal combat. Track: which BG unit state variables convert to TTRPG character state. Run the TTRPG scene. Zoom Out. Verify BG state correctly reflects TTRPG outcomes.

4. **Register Shift test (within TTRPG):** Trigger a Register Shift mid-scene (personal → faction, faction → mass combat). Verify: personal scale state persists correctly, faction-level consequences fire correctly, no scale-crossing variable is double-counted or lost.

Flag every broken handoff as P1.

### L — Precedent Comparison

For the mechanic under test, identify 2–3 analogue mechanics in precedent games. For each:

```
[PRECEDENT: Game — Mechanic name]
What it does: [one sentence]
How Valoria's version differs: [one sentence]
Justification for difference: [one sentence — cite Foundations, design intent, or mode requirement]
Risk: [NONE / design drift / unjustified complexity / flavour without function]
```

Precedent game library (use these in priority order when analogues exist):
- **Burning Wheel** — belief/instinct system, Duel of Wits, resource cycles, advancement
- **A Song of Ice and Fire RPG** — intrigue system, house rules
- **Twilight Imperium 4** — faction asymmetry, political phase, strategic card play
- **Root** — asymmetric faction design, board game/narrative hybrid
- **Here I Stand / Virgin Queen** — political/military/religious clock systems
- **Crusader Kings (TTRPG adaptation)** — succession, dynasty, character-faction binding
- **Pendragon** — trait/passion system, generational play
- **Blades in the Dark** — faction clocks, position/effect, crew advancement

If no analogue exists in the library: flag as `[NO PRECEDENT — this mechanic is novel; verify it carries its own weight]`.

Flag: any case where Valoria's version is more complex than the precedent without justification (P2), or where the precedent's solution is strictly superior (P1 — redesign candidate).

### M — Narrative Flowchart Generator

Produces a branching flowchart for a defined scenario seed. This mode generates the full emergent narrative space, not a single path.

**Input:** A trigger event, faction state, and list of named participants.

**Output structure:**

```
## FLOWCHART: [scenario name]
## Seed: [trigger event]
## Mode: TTRPG / Hybrid / BG (all three must be mapped)
## Tracks at seed: [all relevant clock/stat values]

### NODE 0: [Trigger event description]
State: [all relevant tracks]
Branch conditions: [what determines which path fires]

  ├── BRANCH A: [condition — e.g. "Church TC ≥ 40 at season start"]
  │   State delta: [what changes]
  │   → NODE A1: [next event]
  │       Branch conditions: [next split]
  │       ├── BRANCH A1a: [...]
  │       │   → NODE A1a1: [...]
  │       └── BRANCH A1b: [...]
  │           → NODE A1b1: [...]
  │
  ├── BRANCH B: [condition]
  │   State delta: [what changes]
  │   → NODE B1: [next event]
  │
  └── BRANCH C: [condition — e.g. "PC intervenes"]
      State delta: [what changes]
      → NODE C1: [next event]
```

**Rules for Mode M:**
- Minimum 3 branch conditions per node (usually: high roll / median roll / low roll, OR faction A wins / faction B wins / stalemate, OR PC intervenes / PC observes / PC is absent)
- Minimum 3 nodes deep before reaching terminal states
- Terminal states labeled: STABLE / UNSTABLE (escalates) / COLLAPSE / PC-DEPENDENT (requires player action to resolve)
- Every node must track: relevant clock values, which NPCs are present/affected, which mode is active, and any pending editorial items
- Flag any branch that produces an undefined state (no rule covers it) as `[GAP: ...]`
- Flag any branch that produces the same terminal state regardless of player action as `[DEAD BRANCH — player agency lost]`

**Cross-mode flowchart:**
For hybrid scenarios, map the same seed across all three modes. Show where mode-specific rules produce different branch conditions or terminal states. This is the primary test for whether the mode-transition rules produce coherent narrative across scales.

**Link to existing scenario documents:**
After generating a flowchart, check `designs/ttrpg/valoria_emergent_scenarios.md` and `designs/ttrpg/valoria_narrative_scenario_chains.md` for overlap. Note whether the flowchart confirms, extends, or contradicts existing scenarios.

**Output location:** Commit to `designs/gm_ref_cp14/flowcharts/` as `flowchart_[scenario_name].md`. If the directory does not exist, create it. Link the flowchart from `designs/ttrpg/valoria_emergent_scenarios.md` cross-reference section.

## SIM-DEBT Register
Track calibration values that need re-verification due to parameter changes.

| ID | Description | Blocking? | What to Re-run |
|----|-------------|-----------|----------------|
| SIM-DEBT-01 | Debate stress tests calibrated with Cognition+History pool; now using (Presence×2)+History. Strain/Composure/tracker values need re-verification. | No — can simulate, results directionally valid but not final | Mode G2 full Grand Debate re-run |

Add new SIM-DEBT items whenever a parameter change invalidates prior calibration.

## Provisional Decision Protocol
When a blocker requires a decision to proceed:
1. Make the most mechanically defensible choice based on design context
2. Mark in-text as `[PROVISIONAL: <brief rationale>]`
3. Add to editorial_ledger with `status: provisional`
4. Note in simulation output: `[PROVISIONAL ASSUMPTION: ...]`
5. Surface at next session start for user review

## Read Protocol — Mandatory Before Any Mode
Load params files, not stage files. Stage files are verbose source documents; params files are extracted mechanical values.

1. Always read `references/params_core.md` first (dice engine, TN, Ob, degrees).
2. Then read only the params files relevant to the subsystem being simulated/audited:

| Subsystem | Params File |
|-----------|-------------|
| Core dice/TN/Ob | `references/params_core.md` |
| Personal combat | `references/params_combat.md` |
| Mass combat | `references/params_mass_combat.md` |
| Debate | `references/params_debate.md` |
| Threadwork | `references/params_threadwork.md` |
| Factions (TTRPG or BG) | `references/params_factions.md` |
| Board game mode | `references/params_board_game.md` |
| Scale/mode transitions | `references/params_scale_transitions.md` |

3. For each params file loaded, check the `<!-- version: -->` tag. If it does not match the current ruleset version (see `compilation/README.md`), halt and flag: `[STALE PARAMS: <file> is <version>, current ruleset is <version> — update params before proceeding]`.
4. Do NOT read stage files or design files to get mechanical values. If a value is missing from params, flag it as a gap and request a params update rather than reading the source document mid-simulation.
5. Exception: when specifically auditing a new design document (not yet parameterised), read that document directly and note that params are incomplete for that subsystem.

## Version Check Protocol (Mandatory)
Before running any mode that uses mechanical values:
1. Read the relevant `references/params_*.md` file(s) for this task.
2. Check the `<!-- version: -->` tag at the top of each params file.
3. Compare against the current ruleset version (stated in `compilation/README.md`). If params version tag contains "design-ST" or higher, it is current for simulation purposes.
4. If params version ≠ current ruleset version: **halt, flag as `[STALE PARAMS: <file> is v0.XX, current ruleset is vX.XX — update params before proceeding]`**, and do not proceed until the user confirms or params are updated.
5. If params version matches: proceed. Cost: ~200 tokens per params file read. No GitHub API call required.

Params files and their skill usage:
| Params file | Used by |
|-------------|---------|
| `references/params_core.md` | All skills (dice engine baseline) |
| `references/params_combat.md` | simulator Mode G1, combat-simulator |
| `references/params_mass_combat.md` | simulator Mode G1 |
| `references/params_debate.md` | simulator Mode G2 |
| `references/params_threadwork.md` | simulator Mode G3 |
| `references/params_factions.md` | simulator Mode G4, mechanic-audit |
| `references/params_board_game.md` | simulator Mode G5 |
| `references/params_scale_transitions.md` | simulator Mode G (cross-mode), mechanic-audit Mode G |
