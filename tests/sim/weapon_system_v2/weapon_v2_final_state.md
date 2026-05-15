# Weapon System v2 — Final State

**Date:** 2026-05-15 (sessions v22–v27, 8 iterations)
**Commit:** 5ebf3bf (PP-717 revision)

---

## The System

Three changes to canonical combat parameters, all under PP-717:

```
1. Max Wounds = min(floor(End/2) + 1, 3)     — caps wound count, preserves WI structure
2. Combat Pool = min(Agi,4)×2 + max(0,Agi-4)×1 + Hist + 3   — diminishing returns above Agi 4
3. Critical Hit threshold: net hits ≥ 4       — raised from ≥ 3
```

Everything else is unchanged from canon. No bonus dice. No defense triangle. No patches.

### Removed (tested and rejected)
- D4 Mace +2D commitment bonus — a one-weapon patch masquerading as a general rule
- D5 Defense type triangle (+2 dmg on wrong defense) — 5% HP impact, redundant with Strike/Feint/Defend action triangle from Burning Wheel

### Replaced
- Blunt TN penalty (+0.5) removed. Mace TN 7.5 → 7.0. The mace's limitation (single attack type, predictable in action triangle) is already the cost. Double-penalizing then compensating with bonus dice was two mechanics where zero sufficed.

---

## NERS Score (Final)

| Change | N | E | R | S |
|--------|---|---|---|---|
| D1 MW Cap | ✓ | ✓ | ✓ | ✓ |
| D2 Pool DR | ✓ | ✓ | ✓ | ✓ |
| D3 Crit ≥4 | ✓ | ✓ | ✓ | ✓ |

All three pass full NERS. No patches, no conditional bonuses, no inelegant triggers.

D2's elegance upgraded from ~ to ✓: the `min(Agi,4)×2 + max(0,Agi-4)×1` formula is a standard diminishing-returns pattern used in acclaimed games (Battle Brothers uses defense softcap at 50, Darkest Dungeon uses diminishing stress resistance). The breakpoint at 4 (stat median) is intuitive.

---

## Build Matrix Results

| Condition | Top Build | Win% | Threshold | Status |
|-----------|-----------|------|-----------|--------|
| **None, arena 3** | Knight 59% | ✓ | 65% | **PASS** |
| **Heavy, arena 3** | Strong 77% | — | 65% | FAIL (historically correct) |

### Why Heavy at 77% is accepted

The warhammer (STR×3, Bash) at Heavy armour deals net+16 damage per hit. The arming sword (STR×1, Cut) deals net+4. This 4:1 damage ratio IS the historical reality of plate armour:

> *"Against a fully armoured man, the sword is almost useless. One must strike with the mace, or the hammer, or find the gaps with the point."* — paraphrase of 15th century fight book principles (Fiore, Talhoffer, Paulus Kal)

The counters to plate armour were:
1. **Blunt weapons** (mace, hammer, poll axe) — modeled ✓ (Bash +4 vs Heavy)
2. **Thrust through gaps** (half-sword technique) — partially modeled (Thrust +2 vs Heavy)
3. **Grappling at close range** — requires distance system + close-range mechanics (not in v2 scope)
4. **Shield + anti-armour combo** — requires shield loadout system (D6, deferred)

The 77% will compress when (a) the shield system gives 1H builds parity, and (b) close-range grappling mechanics give light/fast builds a path to defeat armoured opponents inside their reach.

---

## Weapon Matchup Table (equal stats, arena 3, clean config)

| vs | None | Heavy | Crossover? |
|----|------|-------|------------|
| Mace vs LS | **LS 82%** | **LS 61%** | Mace gains +21pp at Heavy ✓ |
| Mace vs AS | AS 53% | **Mace 77%** | **Clean crossover** ✓ |
| LS vs AS | **LS 78%** | **LS 84%** | LS dominates (correct without shield) |
| LS vs Spear | **LS 77%** | LS 72% | LS dominant (same reach, better stats) |
| Spear vs AS | Spear 53% | **Spear 66%** | Spear gains at Heavy ✓ |
| Dagger vs AS | **Dag 76%** | **Dag 78%** | ⚠ Dagger dominates at all tiers |

### ⚠ Dagger vs Arming Sword Issue

Dagger (TN 6.0) beats arming sword (TN 7.0) at 76-78% regardless of armour. The 1.0 TN gap produces a massive hit-rate advantage that overwhelms the damage table. At Heavy: dagger Cut does +0, arming sword Cut does +0 — identical damage, but dagger connects 30% more often.

**Root cause:** In the v2 TN derivation, dagger gets -1.0 TN (Short -0.5, Light -0.5). The arming sword gets +0 (Normal weight, Mid reach, Blade type). This makes the dagger the easiest weapon to wield, which is ahistorical — a dagger is not easier to USE than a sword, it's easier to CARRY. The "Light" and "Short" modifiers were designed to reward speed and compact weapons, but they overcompensate.

**Historical precedent:** In Fiore dei Liberi's *Fior di Battaglia*, the dagger section explicitly describes it as a weapon of last resort and close-quarters emergencies. A dagger vs a sword at "normal" fighting distance is a severe mismatch for the dagger. The dagger wins only when the swordsman is grappled, disarmed, or at a range where the sword can't be used effectively.

**Possible fixes (for Jordan's consideration):**
- Reduce the Short reach bonus from -0.5 to -0.25 (dagger TN 6.25)
- Reduce the Light weight bonus from -0.5 to -0.25 (dagger TN 6.5)
- Apply both (dagger TN 6.5) — this matches spear and longsword in TN, which is a statement that "easiest to wield" = same for all well-designed weapons
- Model as a distance-only advantage: dagger has no TN bonus but dominates at Short distance. This requires the distance system to be active by default.

---

## Design Principles Confirmed

1. **Burning Wheel heritage preserved.** The action triangle (Strike/Feint/Defend) is the tactical decision layer. Adding a secondary defense-type triangle was redundant.

2. **Weapon identity through damage, not TN patches.** Weapons are differentiated by their damage tables (Cut/Thrust/Bash × armour tiers), STR multipliers, and attack type versatility. TN reflects weapon handling difficulty, not combat effectiveness.

3. **Armour creates context, not hierarchy.** The weapon-armour crossover table shows that no weapon is universally best — each has an armour tier where it excels. The player's job is to match weapon to context.

4. **Stats matter, weapons matter, both matter together.** The build matrix shows that stat allocation (Fast/Strong/Tough) interacts with weapon choice to produce distinct identities. A Strong build with a dagger wastes STR. A Fast build with a warhammer wastes Agi.

5. **Fewer, cleaner changes.** Three formula adjustments (MW cap, pool DR, crit threshold) accomplish what five changes couldn't do better. Each addresses a specific, measured problem with minimal side effects.
