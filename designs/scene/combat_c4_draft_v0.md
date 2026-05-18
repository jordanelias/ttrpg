# Combat C4 — Draft Specification (v0)

**Date:** 2026-05-17
**Status:** DRAFT — Jordan review pending. Not yet canonical.
**Sim validation:** Phase 11 (`tests/sim/phase11_c4_v0_2026-05-17.md`) + Phase 12 (`tests/sim/phase12_mass_archetype_v0_2026-05-17.md`)
**Authorized by:** ED-864
**Supersedes:** post-ratification, this doc's content merges into `designs/scene/combat_v30.md` and `params/combat.md`.

---

## Purpose

C4 adds three mechanics to scene combat that address Agility-pool dominance without abandoning the d10 pool grammar: **M1 reach/distance gate**, **M2 stance × stance counter-table**, **M3 initiative preemption**. Layered atop the Phase 10 baseline (undoubled pool + 1/End Ob wound + Disarm + canonical stam + STR-strong).

Reframing 2 (cross-scale archetype dominance) is the canonical position post-C4: each archetype has a domain it wins. Agility dominates scene combat within weapon class; Strength dominates scene combat across weapon classes via reach; Endurance dominates mass-battle survival.

---

## M1 — Reach / Distance Gate

### Concept

Combat rounds track a **Distance Band** between fighters. Weapons have **Reach** values. Attacks made when distance exceeds attacker's weapon reach use a degraded pool (`1D + relevant History`), not the full Combat Pool. Closing distance is a tactical action that trades a turn of offense for positional shift.

### Distance Bands (0-3)

| Band | Name | Effect |
|---|---|---|
| 0 | Grappled | Close combat. All weapons in range. Special grapple/throw mechanics may apply. |
| 1 | Engaged | Sword-length. Light blades, daggers, fists in range. |
| 2 | Spaced | One-step-back. Heavy weapons, longswords, axes in range. |
| 3 | Reach | Polearm-length. Polearms, spears, pikes in range. |

**Starting distance:** Band 2 (Spaced). Tactical opener; both sides can choose to close or open.

### Weapon Reach Values

| Weapon class | Reach | In-range bands |
|---|---|---|
| Unarmed / grapple | 0 | 0 only |
| Light blade (dagger, short sword) | 1 | 0, 1 |
| Standard sword, axe, mace | 2 | 0, 1, 2 |
| Long weapon (longsword two-handed grip, war-axe) | 2 | 0, 1, 2 |
| Polearm (spear, halberd, glaive, pike) | 3 | 0, 1, 2, 3 |
| Ranged (bow, crossbow, sling) | 3 | any (separate range mechanics) |

### Out-of-Range Penalty

Attack made at distance > weapon reach: offence pool collapses to **`1D + relevant History`** (not Agi × 2 + History + 3). Defence is unaffected.

Empirical magnitude: this is the load-bearing C4 mechanic. Phase 11 sim shows it produces light-vs-heavy 78/22 dominance favoring the longer-reach side. Magnitude is intentionally large — soften to 2D+History if play testing reveals over-dominance.

### Distance-Change Actions

Both can be declared instead of Strike / Feint / Disarm / Take Breath. Cost = action cost 5 (standard).

- **Close** — reduce distance by 1 band. Cannot reduce below 0.
- **Open** — increase distance by 1 band. Cannot exceed 3.

If both fighters Close simultaneously, distance reduces by 2 (both close). If one Closes and one Opens, distance does not change. Movements resolve before attack pools roll.

### Reach × Build Interaction

The reach gate makes weapon choice load-bearing. Light-weapon Agi-builds dominate at Bands 0-1 but spend turns Closing against polearm/heavy opponents who hit them with 1D+History attacks during the closing phase. Heavy/polearm builds dominate at Bands 2-3 but lose initiative-economy when forced into grapple-band.

**This is the structural fix to Agi-OP within the weapon class.** Within-same-class matchups still favor higher Agi (Fast vs Strong light-light: 94% Fast). Across-class matchups now favor reach (Fast-light vs Tough-heavy: 22% Fast).

---

## M2 — Stance × Stance Counter-Table

### Concept

Each round, both fighters **simultaneously declare a stance** before action selection. Stance defines the base pool split (offence/defence) AND interacts with opponent's stance via a counter-table that applies flat pool reductions, degree caps, or special effects independent of net successes.

### Four Stances

| Stance | Base off/def split | Tactical purpose |
|---|---|---|
| **Pressure** | +2 off, -1 def | Aggressive — extra offense, vulnerable defense |
| **Patience** | -1 off, +2 def | Defensive — sacrifice offense for resilience |
| **Decisive** | +1 off, 1 def (floor) | All-in commitment — bypasses some defenses, no fallback |
| **Cautious** | half off, +1 def | Hedge — caps incoming damage, low output |

Declaration is simultaneous. Both fighters reveal stance, then choose action (Strike/Feint/Disarm/Take Breath/Close/Open) given their stance and the revealed counter.

### Counter Effects

| Mine vs Theirs | Effect on me |
|---|---|
| Patience vs **Decisive** | I impose −3D on Decisive opponent's offense pool (overcommitment punished) |
| Pressure vs Cautious | My offense is degree-capped at Partial Success (net ≤ 1) — Cautious denies critical hits |
| Decisive vs **Cautious** | I bypass Cautious's degree cap (commitment beats hedging) |
| Pressure vs **Patience** | Patience cannot Take Breath this round (drawn into engagement) |
| Pressure vs Pressure | Both fighters incur +1 stamina cost (drain race) |
| Same stance other than Pressure mirror | No counter; raw pool resolution |
| Cross-stance other than listed above | No counter; raw pool resolution |

**Bolded counters are the asymmetric leverage points.** Decisive is punished by Patience but bypasses Cautious; Cautious is punished by Decisive but degree-caps Pressure; Pressure denies Patience's recovery.

### Why simultaneous reveal

Mirrors Contest!'s genre+orientation declaration and BattleCON's Style+Base simultaneity. Removes the information-advantage that turn-order alone provides. Stance is mind-game depth, not pool depth.

### Magnitudes are tunable

Phase 11 sim used these specific magnitudes (−3D for Decisive-vs-Patience, degree cap at net ≤ 1 for Cautious-vs-Pressure). These are empirical first-pass values. Playtesting may justify tighter or looser values. Whichever values ship, the counter-table's *shape* is the design — flat pool reductions independent of net success comparison.

---

## M3 — Initiative Preemption

### Concept

Higher-Initiative fighter can spend stamina to **cancel opponent's action this round** — opponent loses pool roll entirely, takes 3 stamina penalty (frustrated). Available once per duel.

### Mechanics

- **Eligibility:** must have higher Initiative (per `params/combat.md` Initiative formula — currently Attunement-based). Tie: no preemption available.
- **Trigger:** must be at or below 60% HP (genuine pressure context, not free interrupt) AND Initiative gap ≥ 2 (preemption is for build-asymmetric matchups, not minor edges).
- **Cost:** 2 stamina to the preempting fighter.
- **Effect:** opponent's chosen action does not occur this round. Opponent loses 3 stamina (frustration penalty). Distance changes still resolve, but no Strike/Feint/Disarm rolls; no damage; no Pool spent.
- **Frequency:** once per duel.

### Why this exists

Init-build (Attunement) currently has no scene-combat application beyond initiative order. M3 gives Att/Foc archetypes a real combat lever. Modest effect — Phase 11 sim shows Init-build (Att 8) holding 26.7% vs Fast (up from 5-8% pre-reform), not dominance.

---

## Sim Validation (Phase 11)

```
Calibration symmetric                              ~50/50 ✓

Within-weapon-class (light-light):
  Fast (Agi 6) vs Strong (Agi 3)                   94.1% Fast
  Fast vs Tough (Agi 3, End 6)                     67.3% Fast
  Fast vs Mighty-l (Agi 3, STR 7, light)           87.9% Fast    ← F3 gap test
  Fast vs Init-build (Att 8)                       73.3% Fast    ← M3 modest

Across weapon class (M1 reach gate active):
  Fast vs Tough-heavy                              22.3% Fast    ← inversion via reach
  Fast vs Titan (heavy)                            11.9% Fast
  Fast vs Mighty-heavy                             60.4% Fast
  Fast vs Polearm                                  55.9% Fast    ← cleanest matchup

Balanced (Agi 5, STR 5, light) vs Fast              17.8% Bal    ← committed beats balanced
```

Mass-battle cross-check (Phase 12): Heavy/Strong archetypes dominate mass scale at 100/0 categorical when weapon-class fails to penetrate armor-class. Cross-scale balance supports Reframing 2.

---

## Open Canonical Questions

1. **M1 reach gate severity.** 1D+History is aggressive (full pool collapse). Alternatives:
   - 2D+History (moderate)
   - Full pool at TN 8 instead of TN 7 (mild)
   - Pool/2 (medium)
   - Confirm 1D+History or specify alternative.

2. **M2 counter magnitudes.** Phase 11 used −3D for Decisive-vs-Patience, degree cap at net ≤ 1 for Cautious-vs-Pressure. Confirm or specify alternative magnitudes.

3. **M3 preempt parameters.** 2 stam cost, 3 stam frustration penalty, HP ≤ 60% trigger, Init gap ≥ 2, once per duel. Tune if needed.

4. **Stance count.** 4 stances (Pressure/Patience/Decisive/Cautious) per spec; alternatively 2 stances (Aggressive/Defensive) for simpler player UX. 4 gives mind-game depth; 2 reduces decision load.

5. **Distance Band 0 (Grappled).** Specced as "all weapons in range" but special grapple/throw mechanics not specified here. Either confirm "no special grapple mechanics; just close-range pool resolution" OR draft separate Grapple subsystem.

6. **Ranged weapons + M1.** Spec says ranged "any band, separate range mechanics." Drafting separate ranged-distance system (bow effective at Bands 2-3 only? bow has minimum range?) is deferred. Confirm.

7. **Pool split fixed at stance default vs player choice.** Current spec: stance determines split. Alternative: stance offers default; player can override within stance bounds. Player override adds tactical depth but slows decision.

---

## Implementation Notes

### params/combat.md changes (post-ratification)

- Add "Distance Band" section to combat phase structure
- Add "Reach" column to weapon table
- Add "Stance" declaration phase before action selection
- Add stance × stance counter-table
- Add M3 preemption rules under "Initiative" section

### designs/scene/combat_v30.md changes

- Update "Combat resolution" section: stance + distance dimensions
- Update build/character-creation guidance: weapon-class choice now has tactical consequences (reach), stance preference is a build-style consideration
- Note Reframing 2 implication: build choice affects scale-of-encounter advantage

### Sim Phase 13 (post-ratification)

- Implement tuned magnitudes (whatever Jordan ratifies)
- Add Heavy-vs-Heavy tactical-lever sim to verify Phase 12 stalemate resolves via tactic cards / Command (separate audit from C4)
- Cross-check mass-battle integration: do C4 scene-combat dynamics propagate cleanly to mass-battle resolution via personal-scale Champion duels?

---

## Related

- ED-864 — C4 direction set
- ED-838 — Phase 8 Agi dominance baseline
- ED-839 — Phase 10 reform-stack baseline
- `tests/sim/scripts/phase11_c4_v0.py` — sim implementation
- `tests/sim/scripts/phase12_mass_archetype_v0.py` — Reframing 2 verification
- `designs/audit/2026-05-17-scene-combat-contest/decisions.md` — audit decision record
- `designs/audit/2026-05-17-scene-combat-contest/battlecon_extraction.md` — BattleCON mechanic source
