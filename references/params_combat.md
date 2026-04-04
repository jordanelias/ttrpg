<!-- version: v0.14-AUD5-R1 | sources: designs/combat/combat_design_v1.md | last_updated: 2026-04-03 -->
<!-- CANONICAL SOURCE: combat_design_v1.md supersedes stage8_combat.md -->
<!-- PATCHES APPLIED: PP-086, PP-087, PP-088, PP-091, PP-092, PP-165, PP-172, PP-174, PP-210–218 -->
<!-- PP-232: Health formula revised; Stamina floor 2; armour wield constraint; wound penalty −1D only; -->
<!--         initiative order corrected (initiative holder declares last); tie result corrected; -->
<!--         weapon system rebuilt (Short/Long × Light/Heavy × Blade/Blunt matrix); STR in damage confirmed; -->
<!--         damage formula revised (armour-dependent modifier); Mass Mismatch exemptions corrected; -->
<!--         Close/Far zone terminology flagged ED-129; Stage 1/2 flagged ED-130; Reach zone flagged ED-129. -->

# params_combat.md — Personal Combat

## Pool Formula
Combat Pool = (Agility × 2) + Relevant History + 3 (minimum 5)
Stamina = Endurance + Relevant History + 1 (modified by armour) — minimum 2 (PP-232)
Health = (Endurance + 6) × (wound count + 1) — wound threshold every (Endurance + 6) points (PP-232)

**Armour wield constraint (PP-232):** A character cannot wear armour whose Stamina modifier would reduce their Stamina to 1 or below.

Pool modifiers:
- Wounds: −1D per wound (cumulative). No Ob penalty from wounds. (PP-232)
- Fibonacci group bonus: +dice to Offence allocation only (see below)

## Weapon System (PP-232)

Weapons are defined by three binary axes. Base TN = 7. TN modifiers:

| Axis | Option A | Modifier | Option B | Modifier |
|------|----------|----------|----------|----------|
| Reach | Short | −1 | Long | +0 |
| Weight | Light | −1 | Heavy | +0 |
| Type | Blade | +0 | Blunt | +1 |

Final Hit TN = 7 + reach modifier + weight modifier + type modifier.

**STR minimums:** Each "Heavy" or "Long" axis adds +1 to minimum STR.
| Combination | Min STR |
|-------------|---------|
| Short Light (either type) | 1 |
| Short Heavy or Long Light | 2 |
| Long Heavy (either type) | 3 |
| Long Heavy Blunt | 4 |

Penalty if 1 below minimum: −1D Combat Pool. Cannot wield if 2+ below minimum.

**Blade vs Blunt note:** "Blade" encompasses cutting, piercing, and stabbing weapons. "Blunt" encompasses bludgeoning weapons.

Example weapons by combination:
| Combination | TN | Examples |
|-------------|-----|---------|
| Short Light Blade | 5 | Dagger, knife |
| Short Light Blunt | 6 | Sap, hand axe |
| Short Heavy Blade | 6 | Short sword, arming sword |
| Long Light Blade | 6 | Spear, light lance |
| Short Heavy Blunt | 7 | Club, mace (short) |
| Long Heavy Blade | 7 | Longsword, axe, glaive |
| Long Light Blunt | 7 | Staff, walking stick |
| Long Heavy Blunt | 8 | War hammer, pollaxe |
| Unarmed | 8 | Fists, grappling, improvised |

[EDITORIAL: ED-129 — Ranged weapon TN integration into Short/Long/Light/Heavy/Blade/Blunt matrix pending. Current ranged entries (LP, HP, sling) not yet mapped to new system.]

## Ranged Combat Rules (PP-172)

Ranged weapons require distance from the target to make an Offence roll. At melee range: cannot make a ranged attack. If forced to melee range by an attacker: may defend using full pool (no Offence split). [EDITORIAL: ED-129 — "Close zone" and "Far zone" terminology to be replaced with plain-language distance descriptors consistent with the new weapon reach matrix.]

**Cover:**
| Cover type | vs Light Piercing | vs Heavy Piercing | vs Light Blunt | vs Heavy Blunt |
|------------|------------------|------------------|----------------|----------------|
| Soft (trees, wagon, bale) | +2 DR | +1 DR | +2 DR | +2 DR |
| Hard (stone wall, fortification) | Blocks shot | Blocks shot | Blocks shot | Blocks shot |

**Environmental approach (melee closing):**
| Terrain | Rounds to close | Penalty to closer |
|---------|----------------|-------------------|
| Open ground | 1 round | None |
| Difficult (marsh, rubble, slope) | 2 rounds | +1 Ob to movement actions |
| Shallow river / ford | 2 rounds | +1 Ob, −2D combat while crossing |
| Deep river | 3 rounds + Swim (Ob 2) | Fail = swept back |
| Wall or rampart | Climb (TN 8 Ob 1) | Action lost if climb fails |

**Reload (Heavy Piercing crossbow only):** Full round after each shot. Light Piercing, Light Blunt, Heavy Blunt fire every round.

**Ranged STR minimums:**
| Weapon | Min STR | Penalty if 1 below |
|--------|---------|-------------------|
| Light Piercing (bow) | 2 | −1D |
| Heavy Piercing (crossbow) | 1 | — |
| Light Blunt (stone sling) | 1 | — |
| Heavy Blunt (lead sling) | 2 | −1D |

## Damage Formula (PP-232)

Damage = net hits + STR + weapon modifier vs armour tier (see table below)

STR is confirmed as a damage addition (PP-232, resolves ED-092).

Critical Hit (net hits ≥ 3): weapon modifier doubled before applying armour reduction.

**Weapon modifier vs armour tier:**
| Weapon Class | vs None | vs Light | vs Medium | vs Heavy |
|--------------|---------|----------|-----------|----------|
| Light Blade | +3 | +2 | +1 | +0 |
| Heavy Blade | +6 | +4 | +2 | +0 |
| Light Blunt | +3 | +3 | +3 | +3 |
| Heavy Blunt | +5 | +5 | +5 | +5 |

[EDITORIAL: ED-131 — Exact modifier values require playtesting to confirm. Values above are the design intent from comments; simulation needed before treating as final.]

## Initiative and Pool Allocation (PP-232)

Initiative determines declaration order, not action speed. Higher initiative = more information.

**Declaration order each round:**
1. Lower initiative holder declares Offence/Defence split first.
2. Higher initiative holder sees that split, then declares their own.

Exchange 1 initiative: higher Attunement acts last (highest information). Subsequent rounds: transfers to the exchange winner. Tie result: no damage to either side; initiative stays with current holder.

**Note (PP-232):** Replaces prior "simultaneous reveal" procedure. Initiative holder now declares last, gaining positional knowledge.

## Fibonacci Group Bonus (Offence dice only)
| Attackers | Bonus Dice |
|-----------|-----------|
| 1 | 0 |
| 2 | +1 |
| 3 | +2 |
| 4–5 | +3 |
| 6–7 | +4 |
| 8+ | +5 |

## Wounds / Incapacitation (PP-232)

Health = (Endurance + 6) × (wound count + 1).
Wound threshold = every (Endurance + 6) points of accumulated damage.
Taking a Wound: the wound counter increments; Health resets to (Endurance + 6) × (new wound count + 1).
Example: Endurance 4, 2 wounds → Health = 30; wounds at 20 and 10; incapacitated at 0.
Allows critical hits to deal multiple wounds simultaneously.

Per Wound: **−1D Combat Pool only** (no Ob penalty). (PP-232)

| Endurance | Max Wounds before incapacitation |
|-----------|----------------------------------|
| 1–3 | 2 |
| 4–5 | 3 |
| 6–7 | 4 |

[EDITORIAL: ED-130 — Stage 1 (down) and Stage 2 (dying) incapacitation states need design definition. Prior text was unclear.]

## Mass Mismatch Penalty
Light weapon defender vs Heavy weapon attacker: defensive successes −1 (min 0).
Exempt: Full Guard only. (PP-232 — Long weapon at Close zone exemption removed.)

## Armour (Stamina modifier and wield constraint)
| Armour | STR Min | Stamina Mod |
|--------|---------|-------------|
| None | — | +0 |
| Light | 2 | +0 |
| Medium | 3 | −1 |
| Heavy | 4 | −2 |

Cannot wear armour if it would reduce Stamina to 1 or below (PP-232).
Damage Reduction (DR) is now subsumed into the weapon modifier vs armour tier table above.

## Ranged Damage Reduction (DR) by Armour Tier
| Armour | vs Light Piercing | vs Heavy Piercing | vs Light Blunt | vs Heavy Blunt |
|--------|------------------|------------------|----------------|----------------|
| None | 0 | 0 | 0 | 0 |
| Light | 2 | 1 | 1 | 0 |
| Medium | 3 | 2 | 2 | 1 |
| Heavy | 5 | 3 | 3 | 2 |

Cover DR stacks additively with armour DR.

## Actions Summary
Strike / Establish Distance / Feint / Take a Breath / Full Guard / Disarm / Retrieve Weapon / Reload (Heavy Piercing only) / Dodge (ranged attacks only — forfeit all offensive action; full pool as passive Defence vs one incoming ranged attack; armour DR applies) (PP-215) / Out of Breath (forced at Stamina 0)

## Stamina Minimum (PP-165, revised PP-232)
Stamina minimum: **2**. Cannot wear armour that would reduce Stamina to 1 or below.

<!-- patch_history: references/params_combat_history.md -->
<!-- canonical_sources: references/canonical_sources.yaml -->
