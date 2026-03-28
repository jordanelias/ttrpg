# Simulation Protocol

## State Machine — Per Fight

```
Initial state:
  hpA = hpB = HEALTH
  stamA = STAMINA_MAX[arA]
  stamB = STAMINA_MAX[arB]
  range_band = 'Long'  (default engagement opening)
  catchA = catchB = False

Per round (up to MAX_ROUNDS):
  1. Check Catch Breath
  2. Determine range intentions
  3. Resolve manoeuvre or attack
  4. Apply damage
  5. Decrement Stamina
  6. Check termination
```

---

## Step 1 — Catch Breath Check

If stamA == 0 at round start:
- catchA = True
- stamA = stamina_max(arA)
- effPoolA = ceil(poolA / 2)
- A may only defend this round (no attack, no manoeuvre)

Same for B.

---

## Step 2 — Range Intentions

```python
A_correct = at_correct_range(reachA, range_band)
B_correct = at_correct_range(reachB, range_band)

def at_correct_range(reach, band):
    if reach == 'Versatile': return True   # always can attack
    return reach == band                   # Short at Short, Long at Long

A_wants_manoeuvre = (not A_correct) and can_act_A
B_wants_manoeuvre = (not B_correct) and can_act_B
```

---

## Step 3 — Manoeuvre or Attack Resolution

### Case A: One fighter wants to manoeuvre

**Initiator** spends offensive action (cannot attack).
**Opponent** chooses: contest (spends offensive action, cannot attack) or let it succeed (opponent attacks freely).

*Simulation models opponent always contests (rational default).*

If both can act:
```python
sA = roll(AGI, TN=7)
sB = roll(AGI, TN=7)
if sA > sB:   winner = initiator
elif sB > sA: winner = defender
else:         winner = 'Long'  # tie → Long holds

if winner == initiator: range_band = initiator_preferred_range
# else range unchanged
# Neither attacks this round
```

If opponent is catching breath → initiator succeeds unopposed; opponent cannot attack either (catching breath).

### Case B: Both fighters want to manoeuvre simultaneously

(Can occur after range flip when both are now at wrong range.)
Treat as Case A with A as initiator. Winner gets their preferred range.

### Case C: Neither wants to manoeuvre (both at correct range or Versatile)

Both attack normally.

---

## Step 4 — Attack Resolution

For each fighter who attacks:

```python
pen = 1 if reach == 'Versatile' else 0
off = max(1, pool // 2 - pen)
defn = pool - off  # defender uses remaining dice

atk_successes = roll(off, weapon_atk_tn)
def_successes = roll(opponent_defn, opponent_parry_tn)

if atk_successes > def_successes:
    excess = atk_successes - def_successes
    damage = max(0, weapon_dmg_bonus + excess - opponent_DR)
    opponent_hp -= damage
```

Both fighters resolve simultaneously.

---

## Step 5 — Stamina Decrement

Decrement stamina by 1 for each fighter who attacked or manoeuvred this round.
Stamina floor = 0 (triggers Catch Breath next round).

---

## Step 6 — Termination

```python
if hpA <= 0 and hpB > 0: wins_B += 1
elif hpB <= 0 and hpA > 0: wins_A += 1
elif hpA <= 0 and hpB <= 0: draws += 1  # simultaneous kill
elif round == MAX_ROUNDS: draws += 1     # timeout
```

---

## Output Aggregation

After N_FIGHTS:
```
p_win_A = wins_A / N_FIGHTS
p_win_B = wins_B / N_FIGHTS
p_draw  = draws  / N_FIGHTS
```

---

## Balance Thresholds

| Flag | Threshold |
|---|---|
| P1 balance issue | Any non-mirror matchup >85% win rate |
| P2 balance issue | Any non-mirror matchup 70–85% win rate |
| Mirror symmetry check | Any mirror matchup deviation >2% from 50/50 |
| Reach lockout | Short builds avg win rate <25% vs Long builds |
| Versatile tax | Versatile avg win rate >20% below same-weight Long |
