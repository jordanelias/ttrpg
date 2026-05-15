# Weapon System v2 — All-Directions Audit

**Date:** 2026-05-15 (session v25)
**Method:** All directions per canon_terms — top-down, bottom-up, vertical, diagonal, lateral, horizontal
**Historical sources:** Fiore dei Liberi (*Fior di Battaglia*, c.1409), Johannes Liechtenauer (Zettel, 14th c., via Ringeck/von Danzig glosses), *Le Jeu de la Hache* (c.1460), Royal Armouries Ms. I.33 (c.1300)

---

## TOP-DOWN: Design Intent → Mechanical Verification

### Intent (from canon_terms)
The weapon system should produce a "positive feedback loop between player decisions and mechanics" that is **necessary, robust, smooth, and elegant** (N×R×S×E).

### Evaluation against N×R×S×E

**Necessary (N):** Every weapon occupies a distinct role that would leave a gap if removed.

| Weapon | Role | Removable? | Source |
|--------|------|------------|--------|
| Dagger | Close-quarters lethal | No — grappling/stealth niche | Fiore: *daga* section, unarmed-to-dagger transitions |
| Arming sword | Military baseline | Yes — longsword subsumes it | MS I.33: sword+buckler was the standard, not the sword alone |
| Mace | Anti-armour specialist | No — only 1H blunt option | 14th-15th c. adoption curve tracks plate armour |
| Longsword | Versatile dueling | No — the hub weapon | Liechtenauer: core curriculum; Fiore: primary weapon |
| Spear | Range control | No — only ranged melee | Fiore: *lancia* section, spear as first engagement |
| Warhammer | Heavy anti-armour | No — 2H blunt niche | Poleaxe tradition (*Le Jeu*): armour-breaching par excellence |

[GAP: Arming sword alone is subsumed by longsword. Historically it was ALWAYS paired with a shield or buckler (I.33). The shield loadout is what makes the arming sword necessary. Without shields, the arming sword fails N.]

**Robust (R):** Player thinks strategically; variety in approach and resolution.

Sim finding: the smart attack-type protocol selects Cut vs unarmoured, Thrust vs plate — this IS the Harnischfechten transition (Liechtenauer: *Bloßfechten* → *Harnischfechten*). The system rewards reading the opponent's armour and selecting the correct attack. PASS.

But the defense triangle (wrong-def +2) provides only 2 damage (on ~33% of hits) — too small to create meaningful strategic decisions around defense type. The triangle is currently decorative, not strategic. PARTIAL.

**Smooth (S):** Integrates cleanly; zooms across scales.

The weapon system inherits the d10 pool engine from core.md. Half-point TN integrates cleanly — T1.1 PASS confirms monotonic hit rates. Cut/Thrust/Bash damage tables are a simple lookup. The system is smooth at the personal scale.

Vertical integration (personal → mass combat) is untested. Does a unit of mace-wielders correctly outperform a unit of swordsmen vs armoured opponents? [GAP: No mass combat sim with weapon v2.]

**Elegant (E):** Logically simple; easy to intuit; complex outcomes from simple choices.

The v1 system (3 binary axes) is more elegant than v2 (4 axes with half-point TN). V2 adds complexity (half-point TN, mordhau penalty, Cut/Thrust/Bash tables) for marginal benefit. The key question: does the added complexity produce meaningfully different outcomes?

Sim finding: Cut/Thrust/Bash tables produce correct armour-dependent attack selection (Cut at None, Thrust at Heavy). This IS meaningfully different from v1, which uses a flat modifier per weapon class. V2 elegance: the player chooses Cut or Thrust based on opponent armour. Simple choice, complex outcome. PASS.

---

## BOTTOM-UP: Sim Data → Design Implications

### P1 Finding: Endurance ROI

| Stat | Marginal value of +1 point (4→5) |
|------|----------------------------------|
| Agi | +6 to +8pp |
| STR | +4 to +8pp |
| **End** | **+34 to +48pp** |

End provides 5-8× the marginal value of Agi or STR. This persists even with the proposed linear HP formula (End×5+20). Root cause: the wound system creates a compound advantage.

With End 4 (HP 40, WI 10, MW 3): takes wound at 10 damage, incapacitated at wound 4.
With End 5 (HP 45, WI 11, MW 3): takes wound at 11 damage, still incapacitated at wound 4.

The +5 HP AND +1 WI means End 5 absorbs ~25% more damage before the first wound, and wounds happen later. Since each wound costs −1D (snowball), the End 5 fighter has a larger pool for more rounds, landing more hits and taking fewer.

**This is a formula interaction bug, not a design bug.** The wound interval (WI = End+6) AND the HP total both scale with End, creating a multiplicative effect. Fixing HP alone (D1) doesn't fix the wound interval scaling.

**Proposed fix (D13):** Flat wound interval. WI = 10 (constant). HP = End × 5 + 20. MW = (HP / WI) − 1 = (End×5+20)/10 − 1. This makes HP the only scaling dimension, removing the WI compound.

| End | HP | WI (flat) | MW | Wounds before incap |
|-----|----|-----------|----|---------------------|
| 3 | 35 | 10 | 2.5→2 | 2 |
| 4 | 40 | 10 | 3 | 3 |
| 5 | 45 | 10 | 3.5→3 | 3 |
| 6 | 50 | 10 | 4 | 4 |

With flat WI, End 5 vs End 4: +12.5% HP, same wound count (both MW=3). The compound advantage disappears.

### Weapon Type Parity

| Weapon | Win rate range across 4 armour tiers (vs AS) |
|--------|----------------------------------------------|
| Dagger | 76-79% (3pp range) — dominant at all tiers |
| Longsword | 72-81% (9pp range) — dominant at all tiers |
| Warhammer | 68-87% (18pp range) — armour-dependent ✓ |
| Mace | 44-74% (30pp range) — armour-dependent ✓ |
| Spear | 51-64% (13pp range) — slightly armour-dependent |

Dagger and longsword are FLAT dominant (win at every tier). This is historically incorrect: daggers are near-useless vs plate except in grappling, and longswords require half-sword technique vs plate (Fiore: *spada en arme* is a distinct discipline from *spada a dui mani*).

[GAP: The dagger's TN 6.0 advantage overwhelms its damage disadvantage at all tiers. The dagger should lose vs armoured opponents. The sim uses Thrust +2 vs Heavy which keeps the dagger competitive when it shouldn't be.]

**Proposed fix (D14):** Short weapons suffer −2D vs Medium/Heavy armour (can't reach gaps in plate without grappling). This models the historical reality that daggers against plate require wrestling to close and find joints — a different combat mode, not a faster version of the same mode.

---

## VERTICAL: Personal Scale → Settlement → Territory

### Personal → Unit (mass combat)

The weapon system defines individual matchups. Mass combat uses unit composition. The key vertical question: does the personal weapon balance produce correct unit composition incentives?

If mace-wielders dominate vs armoured units and sword-wielders dominate vs unarmoured, then army composition becomes an equipment decision — which is historically correct. The medieval arms race between armour and weapons produced exactly this dynamic: as plate improved, maces/hammers became standard issue.

[ASSUMPTION: The mass combat sim (sim_mb_06_v21.py) inherits weapon damage from params/combat.md. If the weapon system v2 ratifiable package changes damage formulas, the mass combat sim must be updated to match. — basis: mass combat sim reads canonical params.]

### Unit → Settlement

Weapon availability is a settlement-level resource. Smithing capacity determines which weapons the settlement can produce. A settlement with access to heavy blunt weapons has a strategic advantage vs armoured opponents. This creates a vertical feedback loop: settlement investment → weapon availability → unit effectiveness → territory control.

[GAP: No sim validation of this vertical chain. The weapon system v2 tests are personal-scale only.]

---

## DIAGONAL: Cross-System Interactions

### Weapon × Armour × Stat × Protocol

The four-way interaction produces the game's tactical depth. Tested interactions:

| Systems | Finding | Status |
|---------|---------|--------|
| Weapon × Armour | Correct crossover (blade vs blunt) | ✓ |
| Weapon × Stat (STR) | STR multiplier creates weapon-stat synergy | ✓ |
| Weapon × Stat (Agi) | Higher Agi → initiative → triangle exploitation | ✓ |
| Weapon × Stat (End) | End dominates ALL weapon matchups | ✗ P1 |
| Armour × Stat (End) | End + Heavy = near-invulnerable | ✗ Compounds P1 |
| Protocol × Weapon | Smart protocol rewards versatile weapons | ✓ |
| Distance × Weapon | Reach creates positional game | ✓ |
| Distance × Agi | Agi controls distance (+15-20pp) | ✓ (large but correct) |

### Liechtenauer Vor/Nach (Before/After) in the sim

Liechtenauer's core principle: "Before and After, these two things, are to all skill a well-spring." The sim models this as initiative → declare last → see defense → pick counter.

Sim result: Agi 5 vs Agi 3 with longsword: +7.8pp (None) to +13.8pp (Heavy). Initiative is more valuable vs armoured opponents because attack type selection matters more (Cut +0 vs Thrust +2 vs Heavy). This is elegant: Vor/Nach is a tactical skill, and tactical skill matters more in constrained environments (armour forces harder choices).

Control: Mace vs mace (Agi 5 vs 3): +10.4pp — this is pure pool advantage (init doesn't help a specialist). The initiative advantage for versatile weapons is +3.4pp over pool advantage alone. Small but correct.

---

## LATERAL: Peer Comparison at Personal Scale

### Weapon Hierarchy: Sim vs Historical

| Rank | Sim (unarmoured duel) | Historical (Bloßfechten) | Aligned? |
|------|----------------------|--------------------------|----------|
| 1 | Dagger (76%) | Longsword | ✗ |
| 2 | Longsword (72%) | Sword+buckler | ✗ (no shield) |
| 3 | Warhammer (68%) | Spear (at distance) | ~ |
| 4 | Spear (51%) | Dagger (in grappling) | ✗ |
| 5 | AS (50% baseline) | Arming sword (sidearm) | ~ |
| 6 | Mace (44%) | Mace (anti-armour) | ✓ |

**The sim overvalues the dagger.** In historical sources, the dagger is a last-resort weapon in unarmoured combat — Fiore's *daga* section is about unarmed defenses against dagger attacks, not dagger-as-primary. The dagger's dominance in the sim comes from TN 6.0 (easiest to hit with), which overwhelms its damage disadvantage.

| Rank | Sim (armoured duel) | Historical (Harnischfechten) | Aligned? |
|------|---------------------|------------------------------|----------|
| 1 | Warhammer (87%) | Poleaxe (*Le Jeu*) | ✓ |
| 2 | Longsword (81%) | Half-sword/mordhau | ✗ (too high) |
| 3 | Dagger (79%) | Dagger (in grappling only) | ✗ |
| 4 | Mace (74%) | Mace | ✓ |
| 5 | Spear (64%) | Spear (limited vs plate) | ✓ |
| 6 | AS (50% baseline) | Sword (useless vs plate) | ✓ (AS should be lower) |

**Longsword and dagger both too strong vs armour.** The longsword should shift to a distinct *spada en arme* mode vs plate (historical: shortened grip, half-sword thrusting at joints). The dagger should require grappling range to be effective. Neither transition is modeled.

---

## HORIZONTAL: Progression Timeline

### Character Progression Impact

As characters advance (stats 3→4→5→6→7), which stat investments produce the largest capability jumps?

Per ROI data: End is overwhelmingly dominant at every investment level. A character who raises End from 4→7 gains ~180% more survivability. One who raises STR 4→7 gains ~24pp more offense. One who raises Agi 4→7 gains ~18pp more pool.

**This creates a degenerate progression path:** every rational player raises End first, regardless of build concept. A "fast duelist" concept (high Agi) is strictly dominated by a "tough duelist" concept (high End) at every stage of progression.

**Historical check:** In real medieval combat, physical conditioning (End) WAS the most important factor — but it was a prerequisite, not a dominant strategy. Liechtenauer's emphasis on *Fühlen* (feeling the blade), timing, and initiative suggests that skill (mapped to Agi/Cog in the game) should provide comparable returns to conditioning.

---

## FINDINGS REGISTER

### P1 (Critical)
1. **End ROI dominance:** +34-48pp per point vs +6-8pp for other stats. Wound system compounds HP advantage. Proposed: flat WI = 10 (D13).
2. **Dagger overperformance:** TN 6.0 dominates at all armour tiers. Should be restricted vs Medium/Heavy. Proposed: Short weapon penalty vs plate (D14).

### P2 (Important)
3. **Arming sword fails N without shield.** The weapon has no niche on its own. Shield system (D6) is prerequisite for AS viability.
4. **Longsword too strong vs armour (81%).** Harnischfechten mode shift not modeled. Half-sword should be a distinct action, not automatic.
5. **Defense triangle decorative (+2 dmg, ~33% of hits).** Too small to drive strategic decisions. Accept or redesign as tempo mechanic.

### P3 (Monitor)
6. Spear slightly strong vs Heavy (64%) — Thrust +2 vs Heavy may need reduction.
7. Arena is load-bearing for the duel model (arena 0 = pure attrition).
8. Crit rate at canonical ≥3 is 60% with arena stunt — crits are the norm, not special.

### Decisions Added

| # | Decision | Proposal | Impact |
|---|----------|----------|--------|
| D13 | Flat wound interval | WI = 10 (constant) | Fixes End ROI dominance |
| D14 | Short weapon armour penalty | Short weapons −2D vs Med/Heavy | Fixes dagger overperformance |


---

## Appendix: D13 + D14 Test Results

### D13: Flat WI=10

| Formula | End 5 vs 4 (None) | End 5 vs 4 (Heavy) |
|---------|-------------------|---------------------|
| Canonical WI (End+6) | +33.8pp | +48.4pp |
| Flat WI=10 | +26.4pp | +44.3pp |

Reduces End ROI by ~7pp but End remains dominant. Root cause: wound snowball (−1D/wound) compounds HP advantage.

### D14: Short weapon -2D vs Medium/Heavy

| Armour | Dagger (no penalty) | Dagger (−2D) |
|--------|---------------------|--------------|
| None | 77% | 77% (unchanged) |
| Medium | 79% | 65% (−14pp ✓) |
| Heavy | 79% | 65% (−14pp ✓) |

Correctly differentiates dagger across armour tiers.

### T7.1 with all fixes (D1-D5 + D13 + D14)

| Armour | Top | Spread | Pass 65%? |
|--------|-----|--------|-----------|
| None | Tough 61% | 43pp | ✓ |
| Medium | Strong 74% | 59pp | ~ (pass 75%) |

### Proposed D15: Wound cap at −2D

Root cause of End dominance is wound snowball, not HP/WI formula. Proposed: wound penalty caps at −2D regardless of wound count. Not yet tested.
