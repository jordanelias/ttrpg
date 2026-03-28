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

| Weight | Dmg | Atk TN | Parry TN |
|---|---|---|---|
| Light | +1 | 5 | 6 |
| Medium | +2 | 6 | 7 |
| Heavy | +4 | 7 | 8 |

| Armour | DR | Str Min | Pool Pen | Stamina Max |
|---|---|---|---|---|
| None | 0 | — | — | End+1 |
| Light | 1 | None | None | End+1 |
| Medium | 2 | 3 | −1D | End |
| Heavy | 3 | 4 | −2D | End−2 |

Versatile reach: −2D offensive pool at any range.

---

## References

| File | Purpose |
|---|---|
| `references/combat_params.md` | Canonical mechanical values |
| `references/sim_protocol.md` | State machine, manoeuvre contest protocol |
| `references/findings_template.md` | Output structure |
| `scripts/combat_sim.py` | Runnable simulation script |
