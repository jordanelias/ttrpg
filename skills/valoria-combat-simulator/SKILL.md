---
name: valoria-combat-simulator
description: >
  Run statistical combat simulations for the Valoria TTRPG ruleset. ALWAYS use
  this skill when asked to: simulate combat, run weapon matchups, test combat
  balance, calculate win/loss/draw probabilities, stress-test the combat system,
  compare weapon and armour combinations, or test any manoeuvre. Trigger on:
  "simulate combat", "run matchups", "weapon probabilities", "combat balance",
  "test weapon combos", "win rates", "run the simulation", "rerun", "Run N",
  "robust testing", "test all mechanics", or any request to test how characters
  fight each other. This skill owns all combat simulation work — never
  reconstruct the parameter block or simulation logic inline.
---

# Valoria Combat Simulator

## Purpose
Statistically simulate personal combat between two characters across all valid
weapon × armour build combinations. Produces win/loss/draw probabilities,
identifies balance flags, and generates patch proposals.

**Model:** Sonnet 4.6 (this skill). Never route to Haiku or Opus.

---

## Step 1 — Load Canonical Parameters

Read `references/combat_params.md` before writing any simulation code.
All mechanical values live there. Never hardcode from memory.

If `references/combat_params.md` does not match the current ruleset checkpoint,
flag the discrepancy before proceeding.

---

## Step 2 — Confirm Run Configuration

| Parameter | Default |
|---|---|
| Str / End / Agi | Must be specified |
| Proficiency level | Competent (pool = Agi + History(points+3)) |
| Weapon scope | All melee / Ranged / All / Specific subset |
| Armour scope | All valid / Specific subset |
| N fights (Monte Carlo) | 5,000 (balance) / 10,000 (precision) |
| Max rounds per fight | 30 |
| Run label | Run N (increment from last recorded run) |

---

## Step 3 — Build Valid Build List

A build = (weapon_profile, armour_type). A build is valid if:
1. Str ≥ weapon Str minimum, OR Str = minimum − 1 (−1D penalty applies)
2. Str ≥ armour Str minimum, OR Str = minimum − 1 (penalty applies)
3. NOT 2+ below either minimum (cannot wield / cannot wear)
4. **Light armour exception:** no Str minimum, no pool penalty — always valid

---

## Step 4 — Run Simulation

Use `scripts/combat_sim.py`. Pass config as arguments.

```bash
python3 /path/to/scripts/combat_sim.py \
  --str 3 --end 3 --agi 3 \
  --proficiency competent \
  --n-fights 5000 \
  --max-rounds 30 \
  --run-label "Run-N" \
  --output /home/claude/sim_results_runN.md
```

**Robust testing** (when requested): run ALL stat brackets:
- Str 2 / End 2 / Agi 2 (low)
- Str 3 / End 3 / Agi 3 (baseline)
- Str 4 / End 4 / Agi 4 (high)
- Str 4 / End 3 / Agi 4 (high Str/Agi, low End — skirmisher)
- Str 3 / End 4 / Agi 3 (high End — endurance fighter)

---

## Step 5 — Manoeuvre Coverage

Robust testing must also verify manoeuvre mechanics are consistent with
simulation assumptions. Check each manoeuvre class:

### Defensive
- **Defend!** — Full pool defence. Verify: pool shift works, Overwhelming holds-at-bay fires
- **Rescue** — Endurance roll. Verify: failure splits damage correctly

### Reach Management  
- **Reorient / Withdraw** — Agility vs Agility. Verify: tie → Long holds; Stamina decrements

### Offensive
- **Disarm** — Agility vs Agility. Verify: weapon landing, backup weapon draw at P4
- **Trip** — Verify: prone penalties apply, stand = Priority 5 action
- **Tie Up** — Power check. Verify: Overwhelming → Grapple transition
- **Grapple** — Power vs Power. Verify: reach restriction, unarmed damage, escape cost
- **Shove** — Power vs Agility. Verify: range band push, terrain Overwhelming
- **Called Shot** — +Ob 2. Verify: location effects, Heavy armour negation

### Psychological
- **Feint** — Combat History vs Cognition. Verify: advantage delayed to next round, repeat detection
- **Intimidate** — Presence vs Composure. Verify: one-use per opponent, Devout resistance

### Environmental
- **Exploit Terrain** — Cognition. Verify: diminishing returns on repeat use

---

## Step 6 — Interpret Results

Apply findings framework from `references/findings_template.md`:

1. **Armour dominance** — any armour tier >80% avg win rate independent of weapon?
2. **Reach lockout** — Short builds <25% avg vs Long even with manoeuvre modelled?
3. **Versatile tax** — Versatile >20% below same-weight Long in same-reach matchups?
4. **Weapon weight graduation** — meaningful win rate gradient Light → Medium → Heavy?
5. **No-armour viability** — unarmoured builds competitive or legitimately weak?
6. **Mirror symmetry** — identical builds within 2% of 50/50?

---

## Step 7 — Output

Write to `/home/claude/sim_results_runN.md`. Push to `tests/sim_results_runN.md`.
Update `session_log_current.md`.

---

## Patch Proposals

```
PP-SIM-NNN: [component] — [finding] — [proposed fix] — Priority P1/P2/P3
```

Log to `valoria_patch_proposals.md`.

---

## Current Canonical Values (quick reference — read combat_params.md for full spec)

**Combat Pool = (Agi × 2) + History + 3 (min 5)**
**Stamina = End + History + 1 + armour mod (min 1)**
**Health = End + 6**
**Wounds: −1D Combat Pool each (cumulative)**

| Weapon Type | Hit TN | Def TN | Dmg Bonus |
|---|---|---|---|
| Light Cut | 5 | 6 | +1 |
| Heavy Cut | 6 | 7 | +4 |
| Light Blunt | 6 | 7 | +1 |
| Heavy Blunt | 7 | 8 | +4 |
| Unarmed | 8 | 9 | +0 |

**Critical Hit:** excess ≥ 3 → weapon modifier doubled.

**DR per armour vs weapon type:**

| Armour | Str Min | Stamina Mod | vs LightCut | vs HeavyCut | vs LightBlunt | vs HeavyBlunt |
|---|---|---|---|---|---|---|
| None | — | +0 | 0 | 0 | 0 | 0 |
| Light | 2 | +0 | 2 | 1 | 1 | 0 |
| Medium | 3 | −1 | 4 | 3 | 2 | 1 |
| Heavy | 4 | −2 | 6 | 5 | 3 | 1 |

**Reach:** Short (Close only) / Long (Far preferred; Close at −1D off + half dmg) / Projectile (no melee range)
**Versatile reach removed** — see stage8_combat.md reach rules.

---

## References

| File | Purpose |
|---|---|
| `references/combat_params.md` | Canonical mechanical values |
| `references/sim_protocol.md` | State machine, manoeuvre contest protocol |
| `references/findings_template.md` | Output structure |
| `scripts/combat_sim.py` | Runnable simulation script |


## Read Protocol — Mandatory Before Any Mode
Read `references/glossary.md` for all term definitions and permitted abbreviations before using any game-specific term or abbreviation.

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
