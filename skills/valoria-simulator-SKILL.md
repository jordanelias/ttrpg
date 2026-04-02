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
Update `sim_coverage_matrix.md` (root, canonical copy) after every run.
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

### I — Patch and Editorial Output
After any simulation run, produce structured output for findings:

**Mechanical patches** (Claude executes, no approval needed):
```
[PATCH: SIM-NNN-Px]
Finding: [description]
Mechanic: [ID]
Proposed change: [exact formula or rule text change]
Expected effect: [probability delta or outcome change]
Canon risk: [NONE / LOW / REVIEW-NEEDED]
```

**Editorial gaps** (user approval required):
```
[EDITORIAL: SIM-NNN-Ex — description]
Gap type: [Missing mechanic / Ambiguous rule / Undefined edge case / Content needed]
Blocking: [YES/NO — state what it blocks]
Proposed direction: [1-2 sentence suggestion, illustrative only]
```

Both output types append to `valoria_gap_register_consolidated.md` automatically. Patches also append to `canon/patch_register.yaml` with status: proposed.

## Version Check Protocol (Mandatory)
Before running any mode that uses mechanical values:
1. Read the relevant `references/params_*.md` file(s) for this task.
2. Check the `<!-- version: -->` tag at the top of each params file.
3. Compare against the current ruleset version (stated in `compilation/README.md`).
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
