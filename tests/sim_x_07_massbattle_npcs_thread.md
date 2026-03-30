# SIM-X-07: Mass Battle + Thread — Löwenritter vs Church Templars
## Mode: C (Full Scenario) + D (Edge cases: Coherence retention, FR-D-20 risk, Stage 1 general)
## Mechanics: §8.9 Mass Battle × §15 Thread (W-30, FR-D-20) × Coherence retention roll × §13 NPCs
## Context: Templars (Jarnstal commanding) attempt to seize a Crown-territory fortress to detain practitioner-scholars. Ehrenwall deploys the Löwenritter. Maret Uln (TS est. 50) attached to Löwenritter as a Thread-capable asset.

---

## Force Construction

**Löwenritter (Ehrenwall, CR=5)**
- Unit A: Veterans. CP=5, Strength=5, Cohesion=5, Morale=7 (CR5+unit mod2, cap7).
- Formation: Shield Wall (−1D Off, +2D Def).
- Weapon: Heavy Cut, Armour: Medium.
- Starting Effective Pool: min(CP5,S5)=5D, −1D Off (Shield Wall) = 4D Off, +2D Def = 7D Def.
- Military (Löwenritter): 5. CP ceiling: 5. Starting Cohesion ceiling: min(CR5, Mil5)=5. ✓

**Church Templars (Jarnstal, CR=3)**
- Unit B: Elite Knights. CP=5, Strength=5, Cohesion=3 (min(CR3,Mil4)=3), Morale=5 (CR3+2).
- Formation: Wedge (+2D Off, −1D Def).
- Weapon: Heavy Blunt, Armour: Heavy.
- Starting Effective Pool: min(CP5,S5)=5D, +2D Off (Wedge) = 7D Off, −1D Def (Wedge) = 4D Def.
- Military (Church): 4. CP ceiling: 4. But unit is CP=5 → CONFLICT: Church Military=4 caps CP at 4.

**[P2 Finding F-26]:** Templar CP=5 exceeds Church Military=4 ceiling. Under §8.9: "A faction's Military stat sets the maximum CP ceiling for units it fields." Church Military=4 → Templars max CP=4. This is an editorial note from mass_battle_v3.md; the Church's Military=4 stat means it cannot field CP=5 units.

Correcting Templar CP to 4 (Elite tier capped by Military ceiling).
Templar revised pool: min(CP4,S5)=4D, +2D Wedge = 6D Off, −1D Wedge = 3D Def.

**Practitioner: Maret Uln (TS ~50)**
- Spirit: 4, Attunement: 3, History (Einhir Scholarship 2) → Hist bonus = 5
- TPS = 50÷10 = 5
- Thread pool: Spirit + History + TPS = 4+5+5 = 14D TN7
- W-30 (Territorial Ob4): P(success, 14D Ob4) ≈ ~88%
- FR-D-20 (Wall Dissolution, Territorial Ob7): P(success, 14D Ob7) ≈ ~22%
- Coherence: 10/10. RS: 100.

**Context:** No fortress walls in this engagement — it is a field battle. Maret will attempt W-30 (Phase 5) and evaluate FR-D-20 if a fortification element enters play.

---

## State: Turn 1, Phase 1-3

### Units
Unit A (Löwenritter) — CP5, Strength 5, Cohesion 5, Morale 7. Shield Wall.
  Effective: 4D Off / 7D Def.
Unit B (Templars) — CP4, Strength 5, Cohesion 3, Morale 5. Wedge.
  Effective: 6D Off / 3D Def.

### Generals
Ehrenwall: CR5. Combat Pool 14D. Not in personal combat this turn.
Jarnstal: CR3. Combat Pool est: (Agility3×2)+2+3 = 11D. Not in personal combat yet.

### Tracks
RS: 100 | Maret Coherence: 10/10 | Coup Counter: 0 (assuming pre-threshold)

**Phase 1:** Maret declares W-30 (Cohesion Bolster, Unit A). Fires Phase 5.
**Ehrenwall tactic:** None declared (CR5 allows tactics but Shield Wall is formation enough; CR5 → can execute Ob2 tactic at P(≥2 net from 5D TN7)=3D+≈75%). Saves tactic slot.
**Jarnstal tactic:** Concentration (Ob1, all sub-units on one target, Fibonacci). With only one unit per side, Concentration has no additional effect here. Jarnstal rolls Ob1 tactic execution as a warm-up: CR3 → 3D TN7 vs Ob1. P(≥1)≈63%.

---

## Phase 4: Engagement — Turn 1

**Weapon interaction:** Templars HeavyBlunt vs Löwenritter Medium armour: DR=1 (HeavyBlunt vs Medium = 1 from table). Effective.
Löwenritter HeavyCut vs Templar Heavy armour: DR=5. Near-ineffective.

**This is the critical matchup problem.** Löwenritter (HeavyCut) cannot damage Templars (Heavy armour, DR=5) effectively. Templars (HeavyBlunt) can damage Löwenritter (Medium armour, DR=1) freely.

Expected damage to Unit A from Templar attack:
- B Off: 6D TN7 (HeavyBlunt hit TN). Expected net: 6×0.33 = 2.0.
- A Def: 7D TN7 (HeavyCut def TN). Expected net: 7×0.33 = 2.3.
- Net hits to A: 2.0−2.3 = −0.3 → 0 hits. Shield Wall's defensive bonus holds.

Expected damage to Unit B from Löwenritter:
- A Off: 4D TN6 (HeavyCut hit TN). Expected net: 4×(0.5−0.1) = 1.6.
- B Def: 3D TN7. Expected net: 1.0.
- Net hits to B: 1.6−1.0 = 0.6. Damage: 0.6+4(HeavyCut)−5(HeavyArmour DR)= −0.4 → 0 damage.

**Shield Wall + HeavyBlunt + HeavyArmour creates a stalemate in Turn 1.** Neither side can damage the other effectively. Löwenritter cannot penetrate Heavy armour with HeavyCut; Templars cannot overwhelm Shield Wall's defensive depth.

**Finding F-27 [P1]:** This is a deadlock state. Löwenritter have the wrong weapon type for this matchup (HeavyCut vs Heavy armour = DR5, near-zero damage). Templars have correct weapon (HeavyBlunt) but cannot overwhelm Shield Wall at this engagement geometry. Without a formation change, terrain element, or tactic, this battle produces zero damage for multiple turns.

The correct Löwenritter response: Ehrenwall needs to either (a) deploy a HeavyBlunt sub-unit, (b) use a tactic to change the engagement geometry, or (c) accept that this battle is a war of attrition — whichever side's Morale or Stamina fails first.

---

## Phase 5: Cascade — Turn 1

**Step 1:** No damage applied (zero from both sides).
**Step 2:** Cohesion checks. No Size lost → no Cohesion checks.
**Step 3:** Morale. No triggers. Both units stable.
**Step 4: W-30 fires.** Maret rolls 14D TN7 vs Ob4. P(success)≈88%.

**Most likely: W-30 succeeds.** Unit A Cohesion: 5+2 = **7** (maximum). Remainder of battle.

**Coherence retention roll:** Maret rolls 14D TN7 vs Ob4 (single op). P(retain Coherence)≈88%. Most likely: Coherence stays at 10.

RS: no damage. W-30 mass combat co-movement: RS −3 (flat ×3 multiplier). RS: 100→97.

**Step 5:** Ehrenwall's Phase 5 action: Rally (not needed — Morale at 7). Instead: Ehrenwall redeploys, considers personal combat challenge to Jarnstal to change engagement terms.

### State Delta: Turn 1
Unit A: Cohesion 7, Strength 5, Morale 7. Shield Wall.
Unit B: Cohesion 3, Strength 5, Morale 5. Wedge.
RS: 97. Maret Coherence: 10.

---

## Turn 2: Ehrenwall challenges Jarnstal to personal combat

**Ehrenwall's tactical logic:** The mass battle is a stalemate (wrong weapon type). Jarnstal's personal incapacitation would trigger Stage 1 (CR halved: 3→1, Morale all units −1, floor suspended). A CR1 Templar force cannot execute tactics or maintain Cohesion ceiling — Cohesion ceiling drops to 1, and CP penalty at low Cohesion would reduce Templar pool to near-zero.

This is the decisive lever — not mass battle damage, but general elimination.

**Personal combat: Ehrenwall (14D pool, now post-SIM-X-06: Wound 1, pool 13D) vs Jarnstal**

Jarnstal stat construction:
- Military Cardinal. Agility: 3, STR: 4, Endurance: 4.
- Weapon: Heavy Blunt (Short, mace). Hit TN7, Def TN8, Damage +4.
- Armour: Heavy. DR vs HeavyCut=5, HeavyBlunt=1.
- Combat Pool: (3×2)+2+3=11. Stamina: 4+2+1−2(heavy)=5. Health: 4. Max Wounds: 3.

**Ehrenwall weapon: Heavy Cut (Long). Jarnstal armour: Heavy. DR=5.** Same problem as the mass battle — Ehrenwall's HeavyCut cannot penetrate Jarnstal's Heavy armour effectively.

Ehrenwall expected damage per hit: Excess + STR4 + 4 − 5DR.
At typical excess 1.5: 1.5+4+4−5 = 4.5. Jarnstal Health=4 → Wound on first hit (~100% of hits cause a wound).

P(Ehrenwall hits per round): With 13D vs Jarnstal's defence (~5D TN8):
Ehrenwall Off 8D TN6: expected net 3.2. Jarnstal Def 5D TN8: expected 5×(0.3−0.1)=1.0. Net hits: 2.2. ~85% P(hit).

Ehrenwall damage per hit: 2.2+4+4−5 = 5.2. Jarnstal Health 4 → Wound every hit.

**Jarnstal damage to Ehrenwall:** HeavyBlunt vs Medium armour DR=1.
Jarnstal Off 5D TN7: 5×0.33=1.7. Ehrenwall Def 5D TN7: 1.7. Expected net: 0. Very balanced defensive.

If Jarnstal hits: 0+STR4+4−1DR = 7 damage. Ehrenwall Health 5 → Wound.
P(Jarnstal hits Ehrenwall): ~50% per round (symmetric defence pools).

---

## Personal Combat Rounds (Ehrenwall vs Jarnstal)

**Round 1:** Ehrenwall strikes 8D Off, 5D Def. Jarnstal strikes 6D Off, 5D Def.
- Ehrenwall hits Jarnstal: ~85%. Wound 1 to Jarnstal. Jarnstal pool: 11−1=10D.
- Jarnstal hits Ehrenwall: ~50%. If hit: Ehrenwall Wound 2 (she already had Wound 1). Pool: 13−1=12D.

**Most likely Round 1:** Both wound each other.
Ehrenwall: 12D, Wound 2/3. Jarnstal: 10D, Wound 1/3.

**Round 2:** Ehrenwall 12D (8D Off/4D Def). Jarnstal 10D (6D Off/4D Def).
- Ehrenwall hits: ~82%. Wound 2 to Jarnstal. Jarnstal pool: 10−1=9D.
- Jarnstal hits Ehrenwall: with 6D Off TN7 vs Ehrenwall 4D Def: 6×0.33=2.0 vs 4×0.33=1.3. Net 0.7. ~57% hit.

If Jarnstal hits: Ehrenwall Wound 3/3 → **Incapacitated** (max wounds=3 at End5).

**Critical risk: Round 2 has ~57% chance of Ehrenwall incapacitation.**

**Most likely Round 2:** Ehrenwall takes Wound 3 (incapacitated). Jarnstal takes Wound 2.
Ehrenwall goes down.

### Stage 1 Ehrenwall Incapacitation

Per §8.9 Stage 1:
- Unit A Morale: 7−1 = 6. Morale floor suspended.
- Ehrenwall CR halved: 5→2.
- Stabilise within 1 turn (Medicine Ob2) or Stage 2 fires.

**Unit A at CR=2:** Cohesion ceiling drops to min(CR2, Military5)=2. But Cohesion was 7 (W-30 bolster active).
Does CR reduction retroactively lower Cohesion? §8.9: "Cohesion ceiling applies at deployment only, not retroactively." Therefore Unit A Cohesion stays at 7. W-30's bolster is not reverted.

**Finding F-28 [P3]:** W-30's Cohesion bolster survives Ehrenwall's incapacitation and CR halving (ceiling-at-deployment-only rule). The Thread operation outlasts the general who commissioned it. Correct per written rules; notable interaction.

### Sub-unit Cohesion
Unit A CR=2 means no new sub-units can exceed CR2 for remainder of battle. Existing formation holds.

---

## Turn 3: Ehrenwall incapacitated, Jarnstal near-incapacitation

**Jarnstal: Wound 2/3.** His personal combat with Ehrenwall is over. He returns to commanding.
Jarnstal pool (mass battle): CR3−1 (mid-combat damage to command capacity?) — no, personal wounds don't reduce CR directly. CR is derived from Presence+Cognition÷2, not from physical state. 

**However:** Jarnstal took 2 Wounds. Per §8 personal combat wound rules: −2D to combat pool (personal). CR is unchanged (CR is a derived stat from attributes, not a dice pool penalised by wounds). Jarnstal CR stays at 3 for mass battle purposes.

**Stabilisation of Ehrenwall:** A Löwenritter officer attempts Medicine. Medicine pool estimated: 3D TN7 Ob2. P(≥2 net) ≈ 30%. Most likely: fails. Stage 2 fires at Phase 5 next turn.

---

## Turn 3, Phase 4: Mass engagement continues, Ehrenwall incapacitated

Unit A operates at CR=2 (halved), Cohesion 7 (W-30 still active), Strength 5.
Unit B: CP4, Strength 5, Cohesion 3, Morale 4 (−1 from Ehrenwall's Stage 1 — wait: Stage 1 affects the general's OWN side only. §8.9: "Stage 1: −1 Morale all units [own side]." Jarnstal is not incapacitated — Ehrenwall is. Ehrenwall's Stage 1 affects Löwenritter unit only.

Unit A Morale: 7→6 (Ehrenwall Stage 1). Unit B Morale: unchanged at 4.

Mass engagement Round 3 still zero damage (same matchup problem — weapons haven't changed).

**Maret Uln decision: FR-D-20 (Wall Dissolution)?**
No walls in this engagement — not applicable.

**Maret alternative: P-31 (Formation Loosening, Relational Ob3) — Dissolve Templar formation's tactical coherence.**
Pool: 14D TN7, Ob3. P(success)≈ 88%. Effect: Unit B loses all formation bonuses for 1 round (loses Wedge +2D Off, −1D Def).

Coherence retention: Single op Ob3. Maret pool vs Ob3 (but we need to check if W-30 from Turn 1 is in the same Leap — no, it was in Turn 1's Leap. This is Turn 3, a new Leap. Retention roll: 14D TN7 vs Ob3 only. P(retain)≈88%. Most likely: no Coherence loss.

**P-31 fires.** Unit B loses Wedge for 1 round. Effective: 4D Off / 4D Def.

**Turn 3, Phase 4 damage (with P-31 active):**
Unit A Off (4D TN6): expected 1.6. Unit B Def (4D TN7): expected 1.3. Net hits: 0.3. Damage: 0.3+4−5DR = −0.7 → 0. Still zero. HeavyCut vs Heavy armour remains the wall.

Unit B Off (4D TN7 — Wedge stripped): expected 1.3. Unit A Def (7D TN7): expected 2.3. Net: −1.0 → 0 hits to A. Shield Wall + high Cohesion fully absorbs.

**P-31 has no material effect here because the deadlock is weapon/armour based, not formation-based.**

**Finding F-29 [P2]:** Formation-loosening Thread ops (P-31) are irrelevant when the engagement deadlock is driven by weapon-armour incompatibility. The correct Thread intervention for this matchup would target the Templars' Heavy armour (FR-D-11 Armour Dissolution) or the fortress-equivalent hardening. Thread operations cannot fix a force composition error.

---

## Turn 3, Phase 5

**Stage 2: Ehrenwall killed** (Medicine failed to stabilise in Turn 2).

Per §8.9 Stage 2:
- Unit A Morale: 6−2 (outside cap) = **4**. Morale floor permanently suspended.
- CR=0: Unit A uncommanded. Cannot execute tactics. Cohesion floor=1.
- Cohesion ceiling drops to 0 for CR purposes — but W-30 bolster still active (Cohesion 7, deployment-rule still applies).

Actually re-check: "Units beyond CR limit fight at Line, Cohesion floor = 1, no tactics." At CR=0, all units are effectively beyond the CR limit. Cohesion floor = 1 (not 0) — units don't collapse immediately.

Unit A Morale: 4. Triggers: Size below 50%? No. Cohesion broken? No (Cohesion=7). Allied unit routed? No. General killed (Stage 2): −2 Morale already applied.

Idle army check: no engagements this turn? Turn 3 had an engagement (Phase 4 attempted). Not idle.

**W-30 bolster critical question:** Cohesion=7. Deterministic Cohesion check: Size lost this turn=0 (zero damage). 0 > 7? No → no Cohesion degradation. Unit A Cohesion stays at 7 even at CR=0.

Unit A effectively fighting in Shield Wall, Cohesion 7, Morale 4, Strength 5 — no commander, but structurally intact due to W-30.

**RS: P-31 mass context. Relational scale, co-movement RS−3. RS: 97→94.**
Maret Coherence: retention roll Turn 3 Ob3 → 14D vs Ob3. P(retain)≈88%. Coherence stays 10.

### State: End Turn 3
Unit A: Strength 5, Cohesion 7 (W-30), Morale 4. Uncommanded (CR=0).
Unit B: Strength 5, Cohesion 3, Morale 4. Wedge.
RS: 94. Maret Coherence: 10.
Ehrenwall: **Dead.** Coup Counter: this is a Löwenritter defeat context — if the battle is lost, Coup Counter does not trigger (Ehrenwall is dead). The Coup Counter was tracking Ehrenwall's threshold. Her death ends the Coup Counter mechanic entirely.

**Finding F-30 [P1]:** Ehrenwall's death terminates the Coup Counter. §13 states the Counter is GM-tracked and private to Ehrenwall. Her death removes the actor. The ruleset does not define a successor for the Coup Counter — this is a [GAP: Coup Counter successor on Grandmaster death — no rule defined].

---

## Battle Resolution (Turn 4+)

Both sides at effectively zero damage/turn (weapon incompatibility deadlock). Factors that break the deadlock:
1. **Morale attrition:** Idle army rule — if no engagement occurs for 2 turns, both sides lose 1 Morale/turn. But both sides continue to engage.
2. **Stamina equivalent:** Mass battle doesn't track unit Stamina. No stamina-driven breakdown.
3. **General action:** No Ehrenwall to Rally or reinforce Cohesion. Templars have Jarnstal (CR3, 2 Wounds on personal track) — he can Rally or Reinforce.

**Turn 4+ projection:** Battle stalemated indefinitely under current rules. The deadlock will break only through:
- Player intervention (introducing HeavyBlunt unit to Löwenritter)
- Thread intervention targeting armour (FR-D-11)
- Jarnstal's personal death (Stage 1/2 cascade)
- External faction action (Crown intervention, Hafenmark reinforcement)

**Finding F-31 [P2]:** The mass battle system correctly reflects that force composition (HeavyBlunt vs Heavy armour) is decisive. A battle between HeavyCut and HeavyBlunt-armoured opponents is mechanically frozen — not a design flaw but a realistic abstraction. However, the rules do not define a battle-end mechanism for indefinite stalemates beyond Morale attrition at Idle army rate (which doesn't apply while both sides engage). A stalemate resolution rule may be needed.

---

## Thread Retrospective: Maret's Coherence Budget

| Turn | Op | Ob | Retention Roll | Coherence |
|------|----|----|---------------|-----------|
| 1 | W-30 | 4 | 14D vs Ob4, 88% retain | 10 |
| 3 | P-31 | 3 | 14D vs Ob3, 88% retain | 10 (most likely) |
| RS cost | — | — | RS 100→94 | — |

Maret never loses Coherence in this scenario. Single-op Leaps at TS50 are sustainable.

---

## Findings Summary (SIM-X-07)

| ID | Category | Severity | Description |
|----|----------|----------|-------------|
| F-26 | Rules | P2 | Templar CP=5 exceeds Church Military=4 ceiling; corrected to CP=4 |
| F-27 | Design | P1 | HeavyCut vs HeavyBlunt-armoured opponent: mass battle deadlock when neither side can deal damage — no stalemate resolution mechanism |
| F-28 | Validation | P3 | W-30 Cohesion bolster survives general incapacitation and CR halving (deployment-ceiling rule) |
| F-29 | Design | P2 | Formation-loosening Thread ops irrelevant when deadlock is weapon/armour based |
| F-30 | Gap | P1 | No rule for Coup Counter successor on Grandmaster death — gap in §13 Ehrenwall design |
| F-31 | Design | P2 | Mass battle stalemate (zero damage both sides) lacks a defined resolution mechanism beyond Morale attrition |
