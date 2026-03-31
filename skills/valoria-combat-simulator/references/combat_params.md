# Valoria Combat — Canonical Parameters
*Source of truth for all simulation runs. Update this file when ruleset patches land.*
*Last updated: 2026-03-31 — stage8_combat.md sync*

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
- Combat Pool = (Agility × 2) + Relevant History + 3 (minimum 5)
- Stamina = Endurance + Relevant History + 1 (modified by armour — see Armour table)

**Proficiency → History points:**

| Level | Points | Pool contribution ((Agi×2) + points + 3) |
|---|---|---|
| Untrained | 0 | (Agi×2) + 3 |
| Beginner | 1 | (Agi×2) + 4 |
| Competent | 2 | (Agi×2) + 5 |
| Veteran | 3 | (Agi×2) + 6 |

---

## Weapons

**Weight axis** — governs damage bonus, attack TN, parry TN:

| Type | Hit TN | Def TN | Damage Modifier |
|---|---|---|---|
| Light Cut | 5 | 6 | +1 |
| Heavy Cut | 6 | 7 | +4 |
| Light Blunt | 6 | 7 | +1 |
| Heavy Blunt | 7 | 8 | +4 |
| Unarmed | 8 | 9 | +0 |

**Reach axis:**

| Reach | Attack band | Notes |
|---|---|---|
| Short | Close range only | Cannot attack at Far zone |
| Long | Far range only | Can fight at Close zone at −1D Offence and half damage (rounded up) |
| Projectile | Projectile range only | Cannot use at Short or Long melee range |

**Strength minimums:**

| Weapon Weight | Str min | 1 below | 2+ below |
|---|---|---|---|
| Light Cut / Light Blunt | 1 | — | — |
| Heavy Cut | 3 | −1D Combat Pool | Cannot wield |
| Heavy Blunt | 4 | −1D Combat Pool | Cannot wield |

**Critical Hit:** excess successes ≥ 3 → weapon modifier doubled.

---

## Armour

Per-weapon-type DR table (from §8.6):

| Armour | STR Min | Stamina Mod | vs Light Cut | vs Heavy Cut | vs Light Blunt | vs Heavy Blunt |
|---|---|---|---|---|---|---|
| None | — | +0 | 0 | 0 | 0 | 0 |
| Light | 2 | +0 | 2 | 1 | 1 | 0 |
| Medium | 3 | −1 | 4 | 3 | 2 | 1 |
| Heavy | 4 | −2 | 6 | 5 | 3 | 1 |

**Stamina = Endurance + Relevant History + 1 + Stamina Mod (minimum 1)**

**Pool penalties (armour):**
- 1 below Str min: −1D Combat Pool
- 2+ below Str min: Cannot wear

---

## Damage Formula

**Damage = excess successes + Str + weapon modifier − armour DR (vs weapon type) (minimum 0)**

Excess attack successes = attacker net successes − defender net successes (minimum 0).

**Critical Hit** (excess ≥ 3): weapon modifier is doubled.
`Damage = excess + Str + (weapon modifier × 2) − DR`

---

## Combat Pool Split

Each round, fighter secretly splits Combat Pool between Offence and Defence:
- Minimum 1 die in each if engaging in both attack and defence
- All-offence = reckless (no defence)
- All-defence = Full Guard (no attack; opponent gains +2D Offence)
- **Manoeuvre declared = offensive action consumed.** No attack that round.

**Simulation default split:** pool // 2 offence, remainder defence (optimal baseline).

---

## Wound System

- Health = End + 6
- At Health 0: take a Wound, Health resets to full
- Each Wound: −1D to Combat Pool (cumulative)
- Incapacitation threshold: End 1–3 = 2 Wounds; End 4–5 = 3 Wounds; End 6–7 = 4 Wounds

---

## Stamina and Out of Breath

- **Stamina** = End + Relevant History + 1 + armour Stamina Mod (minimum 1)
- Stamina depletes by 1 each round any action is taken
- At Stamina 0: **Out of Breath** (forced) — Stamina restores to maximum, half pool, Defence only, opponent +2D Offence
- **Take a Breath** (voluntary): roll Offence at TN 7; each success restores 1 Stamina (capped at max). Fails if hit.
- **Full Guard** and **Out of Breath** both give opponent +2D Offence

---

## Starting Range

- Ranged weapons present → projectile range
- No ranged, combatants not adjacent → **Far zone** (Long reach preferred, default)
- Combatants already adjacent → **Close zone**

---

## Range and Reach

Range is tracked per fighter pair: **Close zone** or **Far zone**.

- Short weapons: attack at Close only; cannot attack at Far
- Long weapons: attack at Far; can attack at Close at −1D Offence and half damage (rounded up)
- Projectile: cannot use at Close or Far melee range

**Zone collapse (group combat):** When one ally has established Close zone against a target, subsequent Short-reach fighters enter Close zone automatically.

---

## Manoeuvre Contest (Reach Management)

**Establish Distance** (wrong range):
- Roll Offence dice at TN 7
- Succeed if successes ≥ opponent's Offence successes AND not hit
- On success: range shifts, gain initiative
- Auto-succeeds if opponent not attacking (Ob = 0)

**Establish Distance roll: Defence dice at TN 7** (not Offence).
Succeed if your successes > opponent's successes. Tie → Long holds (Far zone).

**Long weapon AI:** attempts Establish Distance whenever at Close zone, EXCEPT:
- Opponent is one strike from incapacitation (press the attack instead), OR
- Fighter is in Full Guard waiting for rescue (all dice on defence; no manoeuvre).

