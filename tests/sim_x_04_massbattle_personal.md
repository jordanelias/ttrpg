# SIM-X-04: Mass Battle + Personal Combat (General Duel during Engagement)
## Mode: C (Full Scenario) + D (Edge Case — General Death cascade)
## Mechanics: §8.9 Mass Combat × §8 Personal Combat × Stage 1/2 General Death rules
## Question: Does the general duel interrupt/interact with mass battle in a mechanically coherent way?

---

## Setup

**Battle context:** Two-unit engagement. Lowenritter (A) vs Rebellion (B). Both generals decide to settle the matter by personal combat during Phase 4.

**General A: Harnak (Lowenritter)**
- CR=5. Presence 5, Cognition 4. Agility 4, STR 4, Endurance 4.
- Weapon: Heavy Blunt (Long, war hammer). Hit TN7, Def TN8, Damage +4.
- Armour: Heavy. STR min for Heavy Blunt = 4 ✓.
- Combat Pool = (4×2)+3+3 = 14. Stamina = 4+3+1−2(heavy armour) = 6. Health=4, Max Wounds=3.
- Mass battle role: Morale floor for Unit A = 1 while present. Unit Morale starting = CR+unit modifier = 5+1=6.

**General B: Davan (Rebel)**
- CR=2. Presence 3, Cognition 3. Agility 3, STR 3, Endurance 3.
- Weapon: Light Cut (Long, spear). Hit TN5, Def TN6, Damage +1.
- Armour: Light.
- Combat Pool = (3×2)+2+3 = 11. Stamina = 3+2+1 = 6. Health=3, Max Wounds=2.
- Mass battle role: Unit B Morale floor = 1 while present.

**Mass battle state (entering Turn 2):**
Unit A: CP5, Strength 5, Cohesion 5, Morale 6. Formation: Line.
Unit B: CP2, Strength 4, Cohesion 3, Morale 4. Formation: Line.

---

## Phase 4 — Simultaneous: Mass Engagement + Personal Duel

**Per §8.9:** "General in personal combat: Phase 5 action consumed each turn until resolved. Mass battle continues at reduced command efficiency. CR suspended."

**Interaction chain:**
- During duel: CR suspended → no CR-based bonuses (no +1D per 2CR to unit pool, no tactic execution).
- Phase 5 general action consumed by duel status → no Rally, no Reinforce Cohesion.
- Morale floor remains (general still present, just occupied).

**Mass engagement (proceeding without CR bonus):**
Unit A: Effective pool without CR bonus: min(CP=5, Strength=5)=5D. Formation Line (normal). Off split: 3D, Def: 2D. TN6 (HeavyCut).
Unit B: min(CP=2, Strength=4)=2D. Off: 1D, Def: 1D. TN5 (LightCut).

Unit A hits on Unit B:
- A Off: 3D TN6. Expected net = 3×0.4 = 1.2 (TN6: 0.5 per die − 0.1 = 0.4)
- B Def: 1D TN6 (LightCut def TN). Expected = 0.4.
- Net hits: 1.2−0.4 = 0.8. Damage: 0.8+4(HeavyCut)−1(LightArmour vs HeavyCut)= 3.8. Strength B: 4−4 = 0.

Unit B at Strength ≤0 = destroyed this turn even without the general fight.

**Finding F-15:** Mass battle outcome is determined regardless of general duel status. This is correct — a CR2 vs CR5 engagement is structurally decided. The duel is dramatically meaningful but mechanically redundant in this matchup.

---

## Personal Combat: Harnak vs Davan

**Round 1:**

Harnak Pool: 14D. Expected split: 8D Off / 6D Def (aggressive).
Davan Pool: 11D. Expected split: 6D Off / 5D Def.

**Harnak Off:** 8D, TN7 (Heavy Blunt hit TN). P(die≥7) = 0.4. Expected net = 8×(0.4−0.1) = 2.4.
**Davan Def:** 5D, TN8 (Heavy Blunt def TN). P(die≥8) = 0.3. Expected net = 5×(0.3−0.1) = 1.0.

Mass Mismatch: Davan (Light weapon) defending vs Harnak (Heavy Blunt): −1 to Davan's defensive successes. Davan def: max(0, 1.0−1) = 0.

Net hits to Davan: 2.4−0 = 2.4. Damage: 2.4+STR4+4(HeavyBlunt) = 10.4. DR(Light armour vs HeavyBlunt) = 0. Net damage: **10.4**.
Davan Health = 3 → Wound 1 (health reset to 3). Still has Wound threshold remaining (max 2).

**Davan Off:** 6D, TN5 (Light Cut). P(die≥5) = 0.6. Expected net = 6×(0.6−0.1) = 3.0.
**Harnak Def:** 6D, TN7. Expected = 2.0.

Net hits to Harnak: 3.0−2.0 = 1.0. Damage: 1.0+STR3+1(LightCut) = 5.0. DR(Heavy armour vs LightCut) = 6. Net damage: max(0, 5.0−6) = **0**.

**Finding F-16:** Heavy armour against Light Cut: DR=6 against expected damage~5 → zero damage. Davan's weapon is completely ineffective against Harnak's armour. This is consistent with §8.5 design (LightCut vs Heavy armour: "Effectively useless for damage").

### State Delta: Round 1 (Duel)
Davan: Health 3→Wound1, Health reset to 3. Stamina 6→5.
Harnak: Health 4→4 (0 damage). Stamina 6→5.

---

## Round 2 (Duel)

Harnak same split (8/6). Expected same: 2.4 hits on Davan, 0 damage to Harnak.
Davan options: Davan cannot penetrate Heavy armour. Must either:
(a) Accept losses (Wound 2 → incapacitated) — happening anyway.
(b) Switch to Disarm attempt (doesn't require penetrating armour).
(c) Feint to gain initiative.

**Disarm attempt by Davan:**
Disarm roll: Offence vs Defender Defence. Success: opponent loses weapon.
Davan Off: 6D TN5. Expected net: 3.0. Harnak Def: 6D TN7. Expected net: 2.0. Davan wins disarm by expected +1.0 → ~60% disarm success.
But: Harnak is also Striking simultaneously (simultaneous resolution). If Harnak hits first → Davan takes Wound 2 → incapacitated. The Disarm is irrelevant if Davan is incapacitated.

Mutual resolution: Harnak hits (~85% based on 2.4 vs 0 effective defence), Davan disarms (~60%).

If both fire:
- Harnak expected damage: 10.4 → Wound 2 → Davan **incapacitated**
- Davan disarms: Harnak loses war hammer

**Most likely outcome (Round 2):** Davan incapacitated, Harnak disarmed (must use unarmed next round, irrelevant since duel is over).

---

## Stage 1 General Death: Davan Incapacitated

Per §8.9:
> Stage 1 (incapacitated): −1 Morale all units, CR halved, Morale floor suspended.
> Stabilise Phase 5 with Medicine Ob 2 within 1 turn or Stage 2 fires.

**Unit B immediate effects:**
- Morale: 4−1 = 3.
- CR halved: 2÷2 = 1 (round down = 1).
- Morale floor suspended: Unit B can now rout below 1.

**Stabilisation:** Nobody near Davan with Medicine (skirmish line). No Medicine roll available. Stage 2 fires next Phase 5.

---

## Stage 2 General Death (Turn 3, Phase 5)

> Stage 2 (killed): −2 Morale (outside cap), CR=0, all units uncommanded.

Unit B Morale (already at 3): 3−2 = **1**.
At Morale 1: not yet rout, but one trigger away.
CR=0: Units fight at Line, no tactics, Cohesion floor=1.

Unit B state: Strength ~0 (destroyed in Phase 4), but if we evaluate the cascade on a surviving unit:
- At Strength 0: already destroyed. Stage 2 cascade fires on top of physical destruction.

**Finding F-17:** Stage 1→Stage 2 cascade fires correctly. The Morale −2 (outside −3/phase cap) is significant but Unit B was already effectively destroyed. In a scenario where Unit B had Strength remaining, Stage 2 would push Morale to near-rout, likely triggering contagion to adjacent units.

---

## General Death Cascade Test (Hypothetical: Harnak dies instead)

**Suppose Davan lands a miraculous critical hit (overwhelming success, excess≥3): excess + STR3 + 1 = min 4+ damage → through DR6 = 0. Even crits don't penetrate Heavy armour with LightCut.** 

This is a degenerate case: LightCut cannot kill Harnak regardless of dice result while he wears Heavy armour. Maximum theoretical crit damage: if all 6D succeed (6 net) + STR3 + 1 = 10 raw, −6 DR = 4 net. Harnak Health=4 → Wound. Not Stage 1.

For Stage 1 to occur: Harnak needs to take Wound → Wound → Wound (3 wounds). At 0 damage per hit from LightCut vs Heavy armour, this is mechanically impossible.

**Finding F-18 [P3]:** A general in Heavy armour with Heavy Blunt cannot be incapacitated or killed in personal combat by an opponent with Light Cut. The armour system creates absolute matchup hard-stops. This is consistent with design intent but produces a degenerate personal combat scenario where the outcome is predetermined before initiative is rolled.

---

## Interaction Summary: Mass Battle ↔ Personal Combat

| Interaction | Fires correctly? | Issue? |
|-------------|----------------|--------|
| CR suspension during duel | Yes — mass battle proceeds at base pool | No issue |
| Phase 5 action consumed | Yes — no Rally/Reinforce while dueling | No issue |
| Morale floor during Stage 1 | Yes — suspended on incapacitation | No issue |
| Stage 1→Stage 2 timing | Yes — 1 turn window for Medicine | No issue |
| Mass battle outcome independent of duel | Yes — predetermined by CP/Strength disparity | Design correct |
| Armour hard-stop (LightCut vs Heavy) | Yes — zero damage | P3 only |

---

## All Findings Summary (SIM-X-04)

| ID | Category | Severity | Description |
|----|----------|----------|-------------|
| F-15 | Interaction | P3 | Mass battle outcome predetermined in CR5 vs CR2 matchup; general duel is dramatically meaningful but mechanically redundant |
| F-16 | Validation | P3 | LightCut vs Heavy armour zero-damage confirmed — consistent with design intent |
| F-17 | Validation | P3 | Stage 1→Stage 2 cascade fires correctly; Morale outside-cap penalty significant |
| F-18 | Degenerate | P3 | LightCut opponent mathematically cannot incapacitate or kill Heavy armour general; outcome predetermined |

**No P1 or P2 findings.** Cross-mechanic interaction (mass battle ↔ personal combat) is coherent.
