# Valoria Combat — Canonical Parameters
*Source of truth for all simulation runs. Update this file when ruleset patches land.*
*Last updated: session 2026-03-27 — weapon damage rebase, armour penalty correction*

---

## Dice Engine

- **Die type:** d10
- **Success:** die result ≥ TN
- **Default TN:** 7 (non-combat rolls, dodge, manoeuvre contests)
- **Weapon TN:** varies by weight (see below)
- **Contested rolls:** each side rolls pool, higher net successes wins; ties use tiebreak rule

---

## Attributes (fixed for a given run)

| Attribute | Abbreviation | Typical range |
|---|---|---|
| Strength | Str | 1–7 |
| Endurance | End | 1–7 |
| Agility | Agi | 1–7 |

**Derived:**
- Health = End + 6
- Combat Pool = Agi + weapon proficiency History (points + 3)
- Stamina = see Armour table

**Proficiency → History points:**

| Level | Points | Pool contribution (+ Agi) |
|---|---|---|
| Untrained | 0 | Agi + 3 |
| Beginner | 1 | Agi + 4 |
| Competent | 2 | Agi + 5 |
| Veteran | 3 | Agi + 6 |

---

## Weapons

### Axes

**Weight axis** — governs damage bonus, attack TN, parry TN, speed:

| Weight | Damage Bonus | Attack TN | Parry TN | Speed |
|---|---|---|---|---|
| Light | +1 | 5 | 6 | Fast (3) |
| Medium | +2 | 6 | 7 | Standard (2) |
| Heavy | +3 | 7 | 8 | Slow (1) |

Speed numeric: higher = faster. Fast resolves before Standard before Slow when same range.

**Reach axis** — governs which range band the weapon can attack from:

| Reach | Attack band | Notes |
|---|---|---|
| Short | Close range only | LOCKED at Long range |
| Long | Long range only | LOCKED at Close range |
| Versatile | Either range | −1D to offensive pool at any range (flexibility cost) |
| Ranged | Projectile only | Priority 2; LOCKED at Close or Long melee range |

**Strength minimums:**

| Weight | Str min | 1 below | 2+ below |
|---|---|---|---|
| Light | None | — | — |
| Medium | 3 | −1D Combat Pool | Cannot wield |
| Heavy | 4 | −1D Combat Pool | Cannot wield |

**Valid weapon profiles (melee):** 9 profiles — Short/Long/Versatile × Light/Medium/Heavy

**Special property — Versatile:** Can attack at either Short or Long range at −1D to offensive pool. Does not bypass opponent's right to contest range via manoeuvre.

---

## Armour

| Armour | DR | Str min | 1 below | 2+ below | Stamina max |
|---|---|---|---|---|---|
| None | 0 | — | — | — | End + 1 |
| Light | 1 | 2 | −1D Combat Pool | Cannot wear | End + 1 |
| Medium | 2 | 3 | −1D Combat Pool | Cannot wear | End |
| Heavy | 3 | 4 | −2D Combat Pool | Cannot wear | End − 2 |

**Note:** Heavy armour penalty is −2D (not −1D). All other armours −1D at one below minimum.

Stamina minimum = 1 regardless of armour or End.

---

## Damage Formula

**Damage = Weapon damage bonus + excess attack successes − armour DR (minimum 0)**

Excess attack successes = attacker net successes − defender net successes (minimum 0).

Strength does not add to damage. Accuracy (pool size via Agility) determines damage through excess successes.

---

## Combat Pool Split

Each round, fighter secretly splits Combat Pool between Offence and Defence:
- Minimum 1 die in each if engaging in both attack and defence
- All-offence = reckless (no defence)
- All-defence = full guard (no attack)
- **Manoeuvre declared = offensive action consumed.** No attack and no offence allocation that round.

**Simulation default split:** pool // 2 offence, remainder defence (optimal baseline).

---

## Wound System

- Health = End + 6
- At Health 0: take a Wound, Health resets to full
- Each Wound: +1 Ob to all rolls (cumulative)
- Incapacitation threshold: End 1–3 = 2 Wounds; End 4–5 = 3 Wounds; End 6–7 = 4 Wounds

*Note: Wound Ob penalties not currently modelled in simulation (Run 1/2). Flag for Run 3.*

---

## Stamina and Catch Breath

- **Stamina** decrements by 1 each round a character Moves, Manoeuvres, or Attacks
- At Stamina 0: **Catch Breath** next round — Combat Pool halved (rounded up), defence only
- After Catch Breath: Stamina restored to max
- **Breather** (voluntary before Stamina 0): defence only, Stamina restored

---

## Starting Range

- Ranged weapons present → projectile range
- No ranged, combatants not adjacent → **Long range** (default)
- Combatants already adjacent → **Short range** (narrative determination)

---

## Manoeuvre Contest (Reach Management)

**Trigger:** Fighter at wrong range for their weapon.

**Reorient / Withdraw:**
- Initiator spends offensive action (cannot attack this round)
- Opponent may spend their offensive action to contest
- **Contested:** Agility vs Agility, TN 7; higher net successes wins
- **Tie → Long reach holds** (Long fighter wins ties)
- **Unopposed:** Initiator succeeds automatically; opponent may attack freely
- Winner sets range band; neither attacks if both contested

**Versatile fighters:** Never LOCKED; always pay −1D to attack. Still subject to opponent Reorient/Withdraw attempts.

**Ranged fighters at melee range:** Must Withdraw to projectile range before firing. Opposed by melee fighter's Agility.
