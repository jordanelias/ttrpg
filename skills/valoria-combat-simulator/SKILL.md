---
name: valoria-combat-simulator
description: >
  Run statistical combat simulations for the Valoria TTRPG ruleset. ALWAYS use
  this skill when asked to: simulate combat, run weapon matchups, test combat
  balance, calculate win/loss/draw probabilities, stress-test the combat system,
  or compare weapon and armour combinations. Trigger on: "simulate combat",
  "run matchups", "weapon probabilities", "combat balance", "test weapon combos",
  "win rates", "run the simulation", "rerun", "Run 2", "Run N", or any request
  to test how characters fight each other. This skill owns all combat simulation
  work — never reconstruct the parameter block or simulation logic inline.
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
flag the discrepancy and ask the user to confirm before proceeding.

---

## Step 2 — Confirm Run Configuration

Ask the user (or read from session context) for:

| Parameter | Default |
|---|---|
| Str / End / Agi | Must be specified |
| Proficiency level | Competent (pool = Agi + History(points+3)) |
| Weapon scope | All melee / All ranged / All / Specific subset |
| Armour scope | All valid / Specific subset |
| N fights (Monte Carlo) | 20,000 |
| Max rounds per fight | 30 |
| Run label | Run N (increment from last recorded run) |

Valid Str/End/Agi values: 1–7. Str gates weapon and armour access (see params).

---

## Step 3 — Build Valid Build List

A build = (weapon_profile, armour_type). A build is valid if:

1. Str ≥ weapon Str minimum, OR Str = weapon Str minimum − 1 (−1D penalty)
2. Str ≥ armour Str minimum, OR Str = armour Str minimum − 1 (−1D penalty)
3. Str is NOT 2+ below either minimum (cannot wield / cannot wear)

Apply all −1D penalties to Combat Pool before simulation.

---

## Step 4 — Run Simulation

Use `scripts/combat_sim.py`. Pass the run configuration as arguments or
edit the CONFIG block at the top of the script.

**If the script does not exist or is out of date:** reconstruct it from
`references/combat_params.md` following the protocol in `references/sim_protocol.md`.

```bash
python3 /home/claude/valoria-combat-simulator/scripts/combat_sim.py \
  --str 3 --end 3 --agi 3 \
  --proficiency competent \
  --n-fights 20000 \
  --max-rounds 30 \
  --run-label "Run-2" \
  --output /home/claude/sim_results_run2.md
```

---

## Step 5 — Interpret Results

After the simulation completes, apply the findings framework from
`references/findings_template.md`:

1. **Armour dominance check** — does any armour tier produce >80% avg win rate
   independent of weapon choice? Flag as P1 balance issue.
2. **Reach lockout check** — are Short-reach builds achieving <20% win rate
   against Long-reach builds even with manoeuvre modelled? If yes: manoeuvre
   contest probability may need rebalancing.
3. **Versatile tax check** — do Versatile builds consistently underperform
   same-weight Long builds by >20%? Flag for review.
4. **Weapon weight graduation** — does each weight tier produce a meaningful
   win rate gradient? If Light/Medium/Heavy are within 5% of each other
   in same-reach matchups: damage differential is too small.
5. **Mirror matchup symmetry** — all identical builds must be ~50%/50%.
   Any deviation >2% indicates a model bug.

---

## Step 6 — Output

Write results to `/home/claude/sim_results_runN.md` using the findings
template. Push to GitHub at `tests/sim_results_runN.md`.

Then update `session_log_current.md` with run label and top findings.

---

## Patch Proposals

Any finding that indicates a balance issue generates a patch proposal in
this format:

```
PP-SIM-NNN: [component] — [finding] — [proposed fix] — Priority P1/P2/P3
```

Log to `valoria_patch_proposals.md` on GitHub.

---

## References

| File | Purpose |
|---|---|
| `references/combat_params.md` | Canonical mechanical values — read first |
| `references/sim_protocol.md` | Manoeuvre contest, stamina, range band state machine |
| `references/findings_template.md` | Output structure for findings |
| `scripts/combat_sim.py` | Runnable simulation script |
