# SIM-X-01: Personal Combat + Thread (Coherent Strike)
## Mode: C (Full Scenario) + B (Interaction Chain)
## Mechanics: §8 Personal Combat × W-24 (Coherent Strike)
## Question: Does a practitioner-combatant using W-24 mid-combat produce broken outcomes?

---

## Setup

**Character A: Practitioner-fighter (Mira)**
- Agility 4, Spirit 4, Endurance 3, STR 3, Attunement 3, TS 50
- Weapon: Light Cut (Long — spear). Hit TN 5, Def TN 6, Damage +1
- Armour: Light (DR vs LightCut = 2)
- Combat Pool = (Agility×2) + History + 3 = 8+2+3 = 13
- Stamina = End + History + 1 = 3+2+1 = 6 (no armour mod)
- Health = End = 3, Max Wounds = 2
- TPS = TS÷10 = 5
- Thread pool (W-24) = Spirit + History + TPS = 4+2+5 = 11D, TN7

**Character B: Armoured veteran (Kaspar)**
- Agility 4, STR 5, Endurance 5
- Weapon: Heavy Cut (Long — longsword). Hit TN 6, Def TN 7, Damage +4
- Armour: Medium (DR vs LightCut = 4, vs HeavyCut = 3)
- Combat Pool = (4×2) + 3 + 3 = 14
- Stamina = 5+3+1 −1 (medium armour) = 8
- Health = 5, Max Wounds = 3

**Expected values (TN7, from simulator reference):**
- Pool 13D: expected net ≈ 4.3, P(≥1)=~99%, P(≥2)=~97%, P(≥3)=~92%
- Pool 11D: expected net ≈ 3.6
- W-24 pool 11D at TN7: P(Overwhelming, ≥4 net) ≈ ~75%, Success ≥ ~93%

**W-24 mechanic:**
- Requires Leap round (Priority 5) preceding attack round
- +2 damage on next successful hit (consumed on use)
- Leap roll: Attunement + History + TPS = 3+2+5 = 10D at TN7
  - P(Success/Overwhelming) from 10D TN7: ~99%, P(Partial) ~1%

---

## State: Round 0 (Diagnosis + Declaration)

### Characters
Mira — Agility 4, End 3, Health 3/3, Wounds 0/2, Stamina 6/6
  Pools: Combat 13D, Thread 10D (Leap)
  Conditions: None

Kaspar — Agility 4, End 5, Health 5/5, Wounds 0/3, Stamina 8/8
  Conditions: None

### Tracks
RS: 100 | Mira Coherence: 10/10

**Round 0 plan:** Mira declares Thread operation (W-24) — Leap round.
Kaspar cannot know the operation is occurring (TS < 50 assumed — observer rule: Diagnosis not detectable below TS 50).
Kaspar declares Strike (split: Offence vs opponent Defence).

**Interaction chain question:** Does Kaspar's Strike connect during the Leap round, cancelling the Thread op?
Per §15.1.2: "Only reactive defence (Parry/Dodge Backwards) is available" during Leap round.
Mira has NO offence allocation — full pool goes to Defence.

Kaspar (14D, full offence): expected net offence = 14 × 0.33 = 4.6
Mira (13D, full defence): expected net defence = 13 × 0.33 = 4.3

---

## Action: Round 0 — Kaspar Strike during Mira's Leap round

Pool (Kaspar): 14D offence, TN6 (Heavy Cut hit TN). P(net≥1) ≈ 99%
Pool (Mira defence): 13D, TN7. Expected net defence 4.3

Expected outcome: Kaspar hit rate = P(Kaspar net offence > Mira net defence)

At TN6, Kaspar: P(die success) ≈ 0.5 (TN6). Expected net ≈ 14×(0.5−0.1) = 5.6
Mira at TN7 defence: expected 4.3

P(Kaspar hits): ~60% (he has ~+1.3 advantage in expected successes)
Excess successes on hit: ~1.3 on average → Damage = 1.3 + STR5 + 4 = ~10.3 raw
After DR (Medium vs HeavyCut = 3): expected damage ≈ 7.3
Mira Health = 3 → First hit of this magnitude: likely Wound.

**Most likely outcome:** Kaspar hits for ~7 damage. Mira takes a Wound. Health resets to 3.
W-24 is cancelled — Mira was hit.

### State Delta: Round 0
Mira: Health 3→Wound threshold hit→Wound 1/2, Health reset to 3. Stamina 6→5.
Kaspar: Stamina 8→7 (action taken).
W-24 cancelled. Leap failed due to hit interrupt.

### Findings (Round 0)
**F-01:** The Leap round creates a predictable vulnerability window. Mira exposed all 13D to defence, Kaspar had full offence — the probability of being hit is ~60%. This is a real cost for Thread combat.
**F-02:** Kaspar's damage output (expected ~7.3 after DR) is high relative to Mira's Health=3. Single Wound per contact is likely. The practitioner's combat effectiveness is already impaired before the Thread operation fires.

---

## State: Round 1

Mira — Health 3/3 (post-reset), Wounds 1/2, Stamina 5/6
  Conditions: Wound taken
Kaspar — Health 5/5, Wounds 0/3, Stamina 7/8

Mira's revised plan: Strike this round (forgo W-24 after wound), reassess.
Split estimate: Mira 7D Off / 6D Def (aggressive, need to apply pressure).
Kaspar: 8D Off / 6D Def (standard aggressive split against wounded opponent).

---

## Action: Round 1 — Strike vs Strike

**Mira offence:** 7D, TN5 (Light Cut). P(die≥5) = 0.6, P(chain on 10) small bonus.
Expected net offence (TN5) = 7×(0.6−0.1) = 3.5 successes

**Kaspar offence:** 8D, TN6. Expected = 8×(0.5−0.1) = 3.2 successes

**Mira defence:** 6D, TN7. Expected = 6×0.33 = 2.0 successes
**Kaspar defence:** 6D, TN7. Expected = 2.0 successes

Mutual hit check:
- Mira hits Kaspar if Mira net Off > Kaspar net Def: 3.5 vs 2.0 → advantage +1.5 → ~65% hit chance
- Kaspar hits Mira if Kaspar net Off > Mira net Def: 3.2 vs 2.0 → advantage +1.2 → ~60% hit chance
- Mutual hit probability: ~0.65 × 0.60 = ~39%

**Most likely outcome:** Mira hits (~65%), Kaspar hits (~60%).

Mira damage on Kaspar: excess ≈ +1.5 + STR3 + 1 = 5.5 raw, DR(Medium vs LightCut) = 4 → ~1.5 net damage
Kaspar damage on Mira: excess ≈ +1.2 + STR5 + 4 = 10.2 raw, DR(Light vs HeavyCut) = 1 → ~9.2 net damage

Mira Health=3, incoming ~9.2 → second Wound this round likely (>3 damage → Wound threshold).

### State Delta: Round 1
Mira: Second Wound → Wounds 2/2 → **Incapacitated** (max wounds reached)
Kaspar: ~1.5 damage absorbed, Health 5→3.5 (no Wound yet; needs >5 to wound).

### Findings (Round 1)
**F-03:** Mira is incapacitated at end of Round 1 without ever landing W-24. The Leap round vulnerability + high damage output of Heavy Cut vs Light armour creates a near-certain loss for the practitioner attempting W-24.
**F-04 [P2]:** W-24 setup cost (1 full Leap round, Composure/Stamina expenditure) is too expensive against a melee opponent who has initiative and TN6 weapon. The operation is only viable if: (a) Mira has range advantage (initiates from wrong range, Kaspar cannot attack during Leap), or (b) allies create cover during the Leap round.

---

## Scenario Variant: W-24 with Range Advantage

**Setup:** Mira at Far zone with spear (Long reach). Kaspar at Close zone with longsword (wrong range — Long at Close = −1D Off, half damage).

Round 0 (Leap round): Kaspar attacking at wrong range.
Kaspar offence at Close zone: (14−1)D = 13D, TN6, half damage.
Expected Kaspar net off: 13×0.4 = 5.2, half damage modifier means: even on hit, damage = (excess + STR5 + 4)÷2.

Mira full defence 13D. Expected net def: 4.3.

P(Kaspar hits) ≈ ~58%
But damage on hit: (excess~0.9 + 5 + 4)÷2 = ~5 → after DR(Light vs HeavyCut=1) = ~4 → still likely 1 Wound.

**Finding:** Range advantage reduces Kaspar's damage by half but doesn't prevent the wound. W-24 still difficult unless Kaspar cannot attack at all (wrong range with no attack available — Short weapon at Far zone).

**Corrected scenario:** Kaspar using Short Heavy Blunt (hand-and-a-half grip, Short reach). At Far zone with Mira: Kaspar cannot attack. Mira completes Leap undisturbed.

Round 0: W-24 fires. Leap roll 10D TN7. P(Success/Overwhelming) = ~99%.
**W-24 activates.** +2 damage on next successful hit.

Round 1: Mira Strike. 13D pool, TN5 (Light Cut).
Mira off 8D TN5: expected net = 8×0.5 = 4.0 (after 1s: 8×(0.6−0.1)=4.0 net)
Kaspar defence (Kaspar must now Establish Distance or fight): if he Strike at wrong range, −1D Off.
Kaspar 13D pool, split 6/7: 6D Off (TN6, half damage), 7D Def TN7.

Mira hits: P(4.0 vs 2.3) ~65%.
Damage: excess ~1.7 + STR3 + 1 (weapon) + 2 (W-24) = 7.7 raw. DR(Medium vs LightCut)=4 → 3.7 net damage.
Kaspar Health=5, takes 3.7 → no Wound yet.

### State Delta (Variant Round 1)
Kaspar: Health 5→1.3 (no Wound, but very close — one more hit wounds)
W-24 consumed.
Mira: Stamina 6→5 (Leap) →4 (Strike). Coherence −0 (Object scale op).

### Findings (Variant)
**F-05:** W-24 is effective when the Leap round is protected (opponent cannot attack). Damage increase from 5.5→7.7 raw is meaningful — tips Kaspar toward wounding threshold faster.
**F-06:** RS impact of W-24: Object scale, Weaving — RS unchanged on Success per degree table. Coherence −0 (Object scale). **The operation is functionally free** in RS/Coherence terms. This may be under-costed for +2 damage.

---

## Co-Movement Check (W-24)

Per P-11: co-movement fires on every operation. W-24 is Object/Personal scale.
Temporal auto-effect fires in world (d6 narrative), not as personal Coherence loss.
Coherence: −0 (Object scale, §3.2).

**Finding F-07:** W-24's co-movement consequence is entirely narrative — no mechanical cost in RS or Coherence on Success. Combined with the +2 damage bonus and ~99% Leap success rate, this operation has very high expected value when safely executed. The mechanic is balanced only by the Leap round vulnerability — remove that vulnerability (range protection, ally cover) and W-24 is a near-costless damage amplifier.

---

## Summary Table

| Scenario | W-24 Fires? | Outcome | Key Factor |
|----------|------------|---------|-----------|
| Standard melee (no range advantage) | No (hit during Leap) | Mira incapacitated R1 | Leap vulnerability |
| Far zone, Kaspar Short-reach at wrong range | Yes | Kaspar near-wounded R1 | Range control |
| Far zone, Kaspar Long at Close (half damage) | Borderline | Still risky | Half-damage insufficient protection |

## P1/P2 Findings

| ID | Category | Severity | Description |
|----|----------|----------|-------------|
| F-01 | Crunch | P3 | Leap round = predictable full-defence round; tactically legible |
| F-02 | Crunch | P3 | Practitioner-combatant needs allies or range to safely use W-24 |
| F-04 | Balance | P2 | W-24 near-costless if Leap protected: 0 RS, 0 Coherence, +2 damage |
| F-06 | Balance | P2 | Object scale Thread operations effectively free in resource terms — only cost is round economy |
| F-07 | Balance | P2 | W-24 balance entirely depends on Leap vulnerability; no RS/Coherence gate |

**No P1 findings.**
