# PART TEN: COMBAT

Combat in Valoria operates at two scales simultaneously: **personal combat** (individual characters) and **mass combat** (military units). Both use the same dice system and share the same priority table. The personal and mass scales can zoom into each other mid-scene.

---

## 10.1 Priority Table

All combatants act within a round using the priority table. Lower number = earlier in round.

| Priority | Action |
|---|---|
| 1 | Thread operation effects manifest (from previous round's Priority 5 roll) |
| 2 | Ranged attacks |
| 3 | Manoeuvres (Defend!, Disarm, Trip, Tie Up, Rescue, Reorient, Withdraw) — resolve before attacks within Priority 3 |
| 4 | Standard actions (Diagnosis; draw backup weapon; non-combat single actions) |
| 4 | Melee attacks (within Priority 4: reach advantage resolves first, then weapon speed) |
| 5 | Move actions; Thread operation rolls (Leap, Weaving, Pulling, FR roll) |
| 6 | Full-round actions (Forced Resolution resolution; Coup de Grâce; second actions; reload after firing) |

**Thread operation timing:** The Leap and operation roll occur at Priority 5. The effect manifests at Priority 1 of the *following* round. There is always a one-round delay between rolling and effect.

---

## 10.2 Personal Combat

### Attack and Defence

**Attack pool:** Combat History pool (primary attribute included — use the pre-printed pool value on the character sheet).

**Defence:** Defender rolls against Ob = attacker's net successes (Versus structure).

| Defence Option | Pool | Notes |
|---|---|---|
| Dodge Backwards | Coordination − armour penalty | Standard evasion |
| Duck and Weave | Coordination − armour penalty | Higher stakes; if defender wins by 2+: attacker loses next action |
| Parry | Combat History pool | Melee only. If Parry declared and ranged attack arrives: auto Dodge Backwards instead |
| Shield | Coordination | Shield TN applies; no armour penalty |

### Damage

**Formula:** Power + weapon damage bonus + excess attack successes − armour (minimum 0)

*Excess attack successes = attacker's net − defender's net, minimum 0.*

*Example: Attacker net 5, defender net 3 = 2 excess → Power 3 + weapon +1 + 2 = 6 damage before armour.*

**Exploding damage:** A damage die showing 10 → re-roll. Failure = +1 damage. Success = +2 damage and re-roll. Continue until failure.

### Reach Priority (Priority 3B)

When a shorter weapon is closing against a longer weapon: the longer weapon gets one priority attack.
- Hit: shorter weapon stops at extended range (cannot close this round)
- Miss: shorter weapon closes regardless

Once both weapons are at the same range, weapon **speed** determines attack order within Priority 4.

### Ranged Characters in Melee

A ranged character in melee at Priority 4 without a melee weapon drawn:
- Defend at Coordination Ob 2
- Draw weapon at Priority 4 (same priority as attacks — declare before rolling)
- Use ranged weapon at Priority 6 only

---

## 10.3 Combat Manoeuvres

All manoeuvres resolve at Priority 3A (before attacks). All use Combat History pool unless noted.

| Manoeuvre | Rolls Against | Effect |
|---|---|---|
| Defend! | Coordination (defender's) | Hold target at bay; deny target's move action next round |
| Disarm | Coordination vs Coordination | Target drops weapon; may retrieve at Priority 4 next round |
| Trip | Coordination vs Coordination | Target prone: −2D attack; attacks vs prone +2D; costs double movement to stand |
| Tie Up | Power | Lock weapons; no damage to either this round; both must re-engage next round |
| Rescue | Endurance | Redirect any melee or Priority 4+ attack from ally to self. *Cannot redirect Priority 2 ranged attacks* — those resolve before Priority 3 |
| Reorient | Cognition | Manipulate relative positioning; establish or deny reach/cover advantage |
| Withdraw | Coordination | Sacrifice attack this round; re-establish reach or range advantage |

### Group Attacks

Multiple attackers on a single target add bonus dice to the group's attack pool:

| Attackers | Bonus Dice |
|---|---|
| 2 | +2D |
| 3 | +3D |
| 4 | +5D |
| 5 | +8D |

### Stunts

A player may declare a Stunt before rolling. The player sets their own critical success range (up to 11–20) — the critical failure range expands equally downward. A result in neither zone: Partial with GM-assigned complication. Stunts apply on both attack and defence.

---

## 10.4 Wounds and Health

**Health = Endurance × 2.** Tracks damage within a fight.

**Wound:** When Health reaches 0, a Wound fires. Health resets fully to maximum. Excess damage carries over. Each Wound: +1 Ob to all rolls.

**Bloodied** (Health ≤ 25% of maximum): Narrative only. Does not restrict Thread operations. Does not impose mechanical penalties beyond the descriptive.

**Wound carry-over cap:** Maximum 2 Wounds per single hit. 3× Health cap on cumulative damage before incapacitation. (MO-6)

**Quick Rest:** Heals Wounds (Endurance dice, one Wound per success) AND restores Health to maximum. Requires a break in active danger.

**Incapacitation threshold:** Varies by character. Wound count × situation. GM sets the point at which further Wounds cause incapacitation; typically 3 Wounds for most characters.

---

## 10.5 Mass Combat

Mass combat resolves at the unit scale. Units are represented by three stats, all on the 1–7 scale.

| Stat | Represents |
|---|---|
| Martial | Fighting effectiveness and training |
| Endurance | Staying power; aggregate Health = Endurance × 2 |
| Cohesion | Morale, order, and formation integrity |

Casualties are narrated, not tracked individually. Aggregate Health tracks the unit's capacity to continue fighting.

### Commander Contribution

A named officer commanding a unit contributes:
- Coordination → adds dice to unit attack pool
- Heart → adds dice to Cohesion checks
- Memory → one conditional order per round (pre-declared contingency)

### Disposition Table

Both commanders declare Disposition at the start of each round (simultaneously, revealed together). All unit attacks use base Ob 2. The table modifies attack pool and, for Defensive defenders, raises attacker Ob to 3.

| Attacker \ Defender | Balanced | Defensive | Offensive | Brutal |
|---|---|---|---|---|
| **Balanced** | Ob 2, ±0D | Ob 3, ±0D | Ob 2, +2D | Ob 2, +1D |
| **Defensive** | Ob 2, −2D | Ob 3, −2D | Ob 2, ±0D | Ob 2, −1D |
| **Offensive** | Ob 2, +2D | Ob 3, +2D | Ob 2, +2D | Ob 2, +3D |
| **Brutal** | Ob 2, +2D | Ob 3, +2D | Ob 2, +2D | Ob 2, +3D |

**Attack pool** = Martial + Commander Coordination ± table modifier.

**Brutal disposition:** +2 raw damage before armour on any success (in addition to table modifier).

### Formation Break and Routing

**Formation Break:** Aggregate Health reaches 0. Consequences:
1. Health resets fully
2. All unit actions +1 Ob for remainder of battle
3. Immediate Cohesion check: pool = Cohesion dice, Ob 2. Failure = Routes

**Routing:** Unit withdraws from the field. Does not fight this round or any subsequent round unless Rallied.

**Rally:** A named officer spends their action. Pool = Heart score in d10s, Ob 2. Success: Rout cancelled; unit returns to Formation Break state (still has +1 Ob penalty).

### Three-Way Combat

Initiative: all three commanders roll Coordination. Highest declares last (most information). Resolve each attacking pair independently using the disposition table. A unit with no target and no attacker this round does not roll.

### Thread Operations in Mass Combat

Thread operations in mass combat use the standard rules with one modification: replace the scale TT multiplier with a flat ×3 multiplier. Total TT gain from any single mass combat Thread operation is **capped at +15** regardless of calculation. Excess converts to narrative consequence at GM discretion (regional site destabilisation, Locked zone expansion). (M-1)

**Representative mass combat Thread operations:**
- Pulling a commander's resolve (Personal scale, Ob 2–3): reduces Heart contribution to Cohesion checks by 2 for duration of contact window
- Weaving unit Cohesion (Territorial scale, Ob 4): +2 to one Cohesion check

### Personal Actions During Mass Combat

A named character may Zoom In at Priority 5 (full-round action): one personal combat exchange. Non-incapacitated targets become Contested Figures — their ultimate fate resolves post-battle based on the exchange outcome.

---

## 10.6 Sieges

Fortified territories require sustained siege operations rather than a single battle.

**Duration:** 1–3 seasons depending on Fortification level and defender resources.

**Each siege season, the defending faction chooses one response:**
- **Sortie:** Battle resolves on the defender's terms (defender chooses terrain and disposition first)
- **Seek Relief:** A second friendly army attempts to break the siege; if it arrives, a field battle resolves normally
- **Negotiate Surrender:** Stability preserved (no forced drop); terms set by negotiation

**Siege resolution:**
- Successful siege (attacker holds for full duration without relief): Defending faction Stability drops to 1 in that territory; territory control transfers
- Negotiated surrender: Stability preserved; terms negotiated (Circles or social scene)
- Relief army arrives and wins: siege lifted; attacker may not re-siege for 1 season

**Fortification as Ob modifier:** Attacker Ob for assault = base Ob 2 + Fortification level of territory.

---

## 10.7 Terrain Effects (Battlefield)

When two armies meet in a territory, the tactical engagement takes place within the territory's terrain. Terrain modifies movement and attack Ob within the tactical round.

| Terrain | Movement Cost | Attacker Ob Modifier | Special |
|---|---|---|---|
| Open | 1 | — | — |
| Forest | 2 | +1 | −2D ranged within forest |
| Hill | 2 | +1 | +1D ranged attacks from hill |
| River crossing | 3 | +2 | No defensive formation while crossing |
| Ruins / Einhir site | 2 | +1 | Einhir site effects apply (see §9.1) |
| Mountain | Impassable | — | Designated passes only |

**Einhir sites on the battlefield:** Practitioners within the area gain +1D on all Thread operations. Units occupying an Einhir ruins position make a Cohesion check (Ob 1) at the start of each round — the configurational wrongness is perceptible even to non-practitioners.

---

*End of Stage 8 compilation. Stage 9 (Social: Debate, Appeal, rhetoric styles, Composure, Reading Exchange) follows.*
