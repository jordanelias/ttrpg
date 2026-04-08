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

**Model:** Sonnet 4.6. Never route to Haiku or Opus.

---

## Step 1 — Input Validation (MANDATORY, BLOCKING)

Fetch the following from GitHub before writing any simulation code or reading any mechanical value:

```python
required = [
    'references/canonical_sources.yaml',  # confirm current design doc
    'references/params_combat.md',        # ALL mechanical values — source of truth
    'references/params_core.md',          # dice engine baseline
]
files = g.read_files_graphql(required)
for path, content in files.items():
    if content is None:
        raise RuntimeError(f"GitHub fetch failed: {path} — cannot proceed")
```

**Fetch log (emit before any analysis):**
```
## FETCH LOG
canonical_sources.yaml: ✓ fetched ([N] lines)
[canonical design doc path]: ✓ fetched ([N] lines)
references/params_[system].md: ✓ fetched ([N] lines) / ✗ missing
```
If any required file is missing from this log, stop — the analysis is invalid.

**Version check:** Confirm `<!-- version: -->` tag in `references/params_combat.md` matches current ruleset version in `compilation/README.md`. If mismatch: flag `[STALE PARAMS: params_combat.md is vX.XX, current ruleset is vY.YY — update params before proceeding]` and stop.

**Memory contamination warning:** userMemories may contain mechanical values (track values, territory data, faction stats, etc.) that feel current but are not fetched from GitHub. Do not use any value from memory as a source for mechanical analysis. Fetch only.

**No hardcoded values.** Every mechanical value (weapon stats, armour DR, pool formulas, TN values, threshold values) must be read from the fetched `references/params_combat.md`. Never use remembered values from previous sessions or skill body text.

---

## Step 2 — Confirm Run Configuration

| Parameter | Default |
|---|---|
| Str / End / Agi | Must be specified |
| Proficiency level | Competent (pool formula from params_combat.md) |
| Weapon scope | All melee / Ranged / All / Specific subset |
| Armour scope | All valid / Specific subset |
| N fights (Monte Carlo) | 5,000 (balance) / 10,000 (precision) |
| Max rounds per fight | 30 |
| Run label | Run N (increment from last recorded run) |

---

## Step 3 — Build Valid Build List

A build = (weapon_profile, armour_type). Use weapon Str minimums and armour Str minimums from fetched `references/params_combat.md`. A build is valid if:
1. Str ≥ weapon Str minimum, OR Str = minimum − 1 (penalty applies per params)
2. Str ≥ armour Str minimum, OR Str = minimum − 1 (penalty applies per params)
3. NOT 2+ below either minimum (cannot wield / cannot wear)
4. Light armour exception: per params_combat.md specification

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

Robust testing must verify manoeuvre mechanics are consistent with simulation assumptions. Check each manoeuvre class using values from fetched `references/params_combat.md`:

### Defensive
- **Defend!** — Full pool defence. Verify: pool shift works, Overwhelming holds-at-bay fires
- **Rescue** — Endurance roll. Verify: failure splits damage correctly

### Reach Management
- **Reorient / Withdraw** — Agility vs Agility. Verify: tie → Long holds; Stamina decrements

### Offensive
- **Disarm** — Agility vs Agility. Verify: weapon landing, backup weapon draw
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

Write to `/home/claude/sim_results_runN.md`. Commit to `tests/sim_results_runN.md` via `g.atomic_commit()`.
Update `session_log_current.md`.

---

## Patch Proposals

```
PP-SIM-NNN: [component] — [finding] — [proposed fix] — Priority P1/P2/P3
```

Log to `canon/patch_register.yaml`.

---

**Pre-commit (run before every `atomic_commit()` call):**
```bash
python3 tools/freshness_gate.py --update
python3 tools/broken_dependency_checker.py
python3 tools/patch_propagation_checker.py
```
Exit 0 required on all three. On non-zero exit: fix the reported issue before committing.

**Post-commit verification:** after `atomic_commit()` returns a SHA, re-fetch all files modified in that commit and confirm content matches what was committed. If content differs: flag immediately, do not proceed.

**Re-fetch after writes:** after any `atomic_commit()` call, re-fetch all modified files before referencing them again in the same session. The in-context version and the committed version may differ.

## Version Check Protocol (Mandatory)

Before running any mode that uses mechanical values:
1. Read the relevant `references/params_*.md` file(s) from GitHub.
2. Check the `<!-- version: -->` tag at the top of each params file.
3. Compare against the current ruleset version (stated in `compilation/README.md`).
4. If params version ≠ current ruleset version: **halt**, flag as `[STALE PARAMS: <file> is vX.XX, current ruleset is vY.YY — update params before proceeding]`, and do not proceed until the user confirms or params are updated.

---

## References

| File | Purpose |
|---|---|
| `references/params_combat.md` | Canonical mechanical values — only source |
| `references/params_core.md` | Dice engine baseline |
| `references/sim_protocol.md` | State machine, manoeuvre contest protocol |
| `references/findings_template.md` | Output structure |
| `scripts/combat_sim.py` | Runnable simulation script |
