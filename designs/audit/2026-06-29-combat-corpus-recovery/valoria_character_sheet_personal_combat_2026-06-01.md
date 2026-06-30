# Valoria — Personal-Combat Character Sheet
**2026-06-01 · combat slice**

> Scope: this sheet covers the stats and derived values the **personal-combat engine** reads. The full
> canonical character model (background, threadwork affinity, social/faction stats, non-martial skills)
> is broader — pull from character canon when the complete sheet is needed. Every formula below is from
> this session's verified mechanics (`derived_stats §4.1`, R1/S1, the r8/m5/m1/m3 modules).

---

## Stat block

Six base parameters (range 1–7) plus a martial background value.

| Stat | Feeds | σ-leverage channel |
|---|---|---|
| **Strength (Str)** | wield (heavy weapons), bind/stagger, **armour-defeat** | pressure `+0.0312/pt` + leverage (bind · stagger-setup · armour-defeat) |
| **Agility (Agi)** | who strikes first each phase | initiative `+0.0625/pt` |
| **Endurance (End)** | Health, Stamina | durability + press-duration |
| **Cognition (Cog)** | reading the opponent | Reading = f(Cog, Att) |
| **Attunement (Att)** | reading the opponent | Reading = f(Cog, Att) |
| **Spirit (Spr)** | Stamina (press-duration) | feeds stamina, not Health |
| **History (Hist)** | combat dice pool, martial tradition | pool depth + tradition coherence |

## Derived combat values

```
Combat Pool   = History + 6                  (min 6)
Wound Interval = End + 6                       (damage per wound tier)
Max Wounds    = min(End ÷ 2 + 1, 3)           (discrete wound tiers — integer)
Health        = Wound Interval × (Max Wounds + 1)
Stamina       = 3·End + 2·Spirit
```

> Health note (pending Jordan ratification — see session B): the discrete `Max Wounds` step at End4
> produces a Health cliff (End3:27 → End4:40). Proposed σ-leverage fix derives Health *linearly* in End
> (`≈ 24 + 5.6·(End−2)`), keeping wound tiers discrete but the capacity smooth. Numbers below use the
> **current canonical** formula; they shift if the smooth derivation is ratified.

## Gear line

- **Weapon** — sets reach/tempo and damage mode. *Cut/thrust* and *point/thrust* are mobile (fast tempo); *war-hammer* is slow but delivers **percussion that defeats plate**.
- **Armour** — none / light / medium / heavy(plate). Plate is combat-dominant against non-armour-defeat weapons; it is gated by **cost** and **availability/context** (you are rarely standing in fresh plate for an unplanned bout), not by an in-combat nerf.

## Context matters

The same fighter is balanced or lopsided depending on context:
- **Personal bout** (no/light armour, the common case): Str / Agi / End are **equal investment value (~50% each)**. The differentiator is skill (History · Reading · tradition).
- **Armoured battlefield** (everyone in plate, war-hammers): **Strength-led and intended so** — armour-defeat is a strength-and-technique game; Agi's tempo edge shrinks when everyone is slow; rotation handles rest, so endurance matters less.

---

## Build 1 — "The Duelist" (balanced personal fighter)

| Str | Agi | End | Cog | Att | Spr | Hist |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 4 | 4 | 4 | 3 | 3 | 3 | 3 |

- **Pool** 9 · **Health** 40 (WI 10 × MW 3 +1) · **Stamina** 18 · **Reading** ~3 (neutral)
- **Gear** long thrust / light armour
- **Reads as** the ~50% baseline. No single channel dominates; an even, mobile duelist. This is the chassis the equal-value target is measured against.

## Build 2 — "The Man-at-Arms" (armoured battlefield)

| Str | Agi | End | Cog | Att | Spr | Hist |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 5 | 2 | 5 | 3 | 3 | 3 | 4 |

- **Pool** 10 · **Health** 44 (WI 11 × MW 3 +1) · **Stamina** 21 · **Reading** ~3
- **Gear** war-hammer / heavy plate
- **Reads as** the battlefield archetype: dumps Agility, leans Str + End, wears plate, carries an armour-defeat weapon. Dominant in the armoured context; would be a slow, readable target in a light personal duel — which is the intended trade.

## Build 3 — "The Master" (skill is the differentiator)

| Str | Agi | End | Cog | Att | Spr | Hist |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 4 | 4 | 4 | 5 | 5 | 3 | 6 |
*+ one named technique-set (coherence)*

- **Pool** 12 · **Health** 40 · **Stamina** 18 · **Reading** ~5 (strong)
- **Gear** long thrust / light armour
- **Reads as** the **same physical body as the Duelist**, separated only by mastery — deeper pool, strong Reading, a trained set. Under the multi-phase engine this build beats the Duelist ~99%. It is the proof that the differentiator is skill, not stats. (How steep that skill advantage *should* be is an open design call — session C.)

---

### Notes
- All three sit at End4–5, so all read Max Wounds 3; the Health spread (40 vs 44) is from Wound Interval, not the cliff. Drop a build to End3 and the current formula cliffs it to 27 — the case the proposed smooth derivation fixes.
- Multi-phase: each of these fighters resolves a bout over ~4 approach/engage/break phases; wounds and stamina accumulate across them, initiative and stance reset each phase.
