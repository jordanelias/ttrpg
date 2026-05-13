# Architecture C — Duel System Proposed Design + Stress Test Results
## Date: 2026-05-13
## Status: PROPOSED (not canonical; pending Jordan ratification)
## Sources: 2026-05-01 combat videogame architecture synthesis, R1-R10 decisions (all verified 2026-05-10), canonical params/combat.md + designs/scene/combat_v30.md

---

## 1. Design Summary

Architecture C is a specialized duel architecture for 1v1 set-piece combat. It composes onto canonical combat math with two modifications:

**E5 — Stance commit.** The canonical pool split (Offense/Defense allocation) is named and made visible to the opponent. Three named stances:
- **Aggressive** — 70% Offense / 30% Defense
- **Balanced** — 50% / 50%
- **Defensive** — 30% Offense / 70% Defense

Lower-initiative player declares stance first (canonical §3). Higher-initiative player sees the commit and chooses their own. This is the read-and-counter loop — the same mechanic as canonical pool-split, visualized as a Pirates!-style stance UI.

**E7 — Posture-as-yield.** When a combatant's Stamina reaches 0, the duel ends in yield (surrender). In canonical combat, Stamina=0 gives −2D OOB and combat continues. In Architecture C, Stamina depletion IS the duel-ender — you can lose without dying.

**All other canonical math unchanged:** Combat Pool = (Agi×2) + History + 3 (min 5). Stamina = End×5. Health = (End+6)×(MaxWounds+1). Wound Interval = End+6. Wound penalty = −1D per wound. Feint = PP-294 versus roll. Initiative transfers to exchange winner. Damage = net hits + STR + weapon mod − DR. Crit at excess ≥3 doubles damage.

---

## 2. Trigger Conditions

Architecture C fires when **both** conditions are met:
1. Exactly 2 participants
2. One of six trigger types:
   - **T-Wager** — formal stakes declared (Conviction / Renown / item / life)
   - **T-Cultural** — cultural challenge (honor, faction custom, territorial challenge)
   - **T-Boss** — named antagonist encounter
   - **T-Thread** — threadwork confrontation at personal scale
   - **T-Hero-Officer** — hero vs named officer during mass battle
   - **T-Honor-call** — explicit demand for single combat

If either condition fails → Architecture A (general scene combat).

**Refusal:** Either party may refuse. Cost: Reputation/Conviction tag ("ducked the duel"). NPC refusal per AI temperament.

---

## 3. Duel Flow

**Pre-duel:** Trigger fires → arena selected (determines Stunt opportunities, audience size for §13.2 Reputation Cascade) → participants may refuse.

**Per round (6–10 seconds narrative):**
1. Lower-initiative player declares stance (visible)
2. Higher-initiative player declares stance (sees opponent's commit)
3. Both declare actions: Strike / Feint / Establish Distance / Full Guard / Stunt / etc.
4. Resolution per canonical §4 priority order
5. Damage application → Health → Wound check → −1D per wound (PP-716)
6. Stamina drain per action cost (Strike: 5, Feint: 5, Defensive: 3)
7. End-of-round checks:
   - Stamina ≤ 0 → YIELD (duel ends; yielder loses but survives)
   - Health ≤ 0 at max wounds → INCAPACITATED (canonical Stage 1)
   - Both simultaneously exhausted → whoever has more remaining Health wins
8. Initiative transfers to exchange winner

**Post-duel:** §13.2 Reputation Cascade fires (if 3+ witnesses). Wager Obligation resolves per contest type (R5 decision C5.1).

---

## 4. Stress Test Battery — Results

Sim: `duel_stress_test.py`, 5000 duels per hypothesis, canonical constants verbatim from `params/combat.md`.
Default stats: Agi 4, STR 4, End 4, History 2. Combat Pool = 13.

### H1 — Mirror (same stats, LightCut, no armour, Balanced vs Balanced)
- **A 47.9% / B 48.6% / Draw 3.5%** — symmetric, as expected
- Rounds: mean 4.8, range 3–5
- End reasons: 72% mutual yield (health tiebreaker), 28% incapacitation
- Wounds at duel end: 1.5 mean per side

### H2 — Agility advantage (A: Agi 5 vs B: Agi 3; Pool 15 vs 11)
- **A 82.1% / B 15.4%** — Agility strongly decisive (+4 dice = +30% win rate over mirror)
- 39% incap, 56% mutual yield

### H3 — Endurance advantage (A: End 6 vs B: End 3; Stamina 30 vs 15, Health 60 vs 27)
- **A 99.8% / B 0.2%** — Endurance **dominates**
- B yields in 3.9 rounds (Stamina 15 / cost 5 = 3 rounds); A has 15 Stamina remaining
- **[P2 FINDING]** Endurance is too decisive. It controls Stamina AND Health AND Wound Interval simultaneously. A 2:1 End ratio produces a near-guaranteed outcome.

### H4 — Weapon asymmetry (HeavyCut vs LightCut)
- **HeavyCut loses: 35.6% vs 61.7%**
- Higher TN (6/7 vs 5/6) means fewer hits; higher damage per hit doesn't compensate
- Heavy weapons designed for group combat (Fibonacci bonus); 1v1 is their worst case

### H5 — Protocol: Aggressive vs Defensive
- **Aggressive wins: 74.0% vs 22.4%**
- Defensive stance increases blocking but reduces damage output; attacker wins the mutual-yield health comparison
- **[P2 FINDING]** Defensive play is not rewarded. The read-and-counter dynamic (E5) lacks a mechanism where reading correctly and choosing Defensive produces an advantage beyond damage avoidance.

### H6 — Protocol: Feint-heavy (feint every 3rd round) vs Balanced
- **Feint-heavy loses: 13.4% vs 85.0%**
- PP-294 makes feinters vulnerable (Defense=0 on feint round); pool reduction next round doesn't compensate for damage taken
- **[P2 FINDING]** Feint is never optimal in 1v1. The canonical Feint design (commit to 0 defense, gain pool reduction next round) is too punishing in Architecture C. Feint works in group combat (allies cover you while you feint); in 1v1, the trade is always negative.

### H7 — Protocol: Adaptive vs Balanced
- **A 47.9% / B 48.6%** — identical to mirror (H1)
- Adaptive doesn't differentiate from Balanced in symmetric matchups

### H8 — E7 comparison: yield-at-0 ON vs OFF (Aggressive vs Defensive)
| Mode | A wins | Rounds mean | Rounds range |
|---|---|---|---|
| E7 ON (yield) | 74.0% | 4.8 | 3–5 |
| E7 OFF (canonical) | 83.2% | 7.3 | 3–23 |
- E7 OFF: duels are 52% longer and 9pp more lethal for the loser (−2D death spiral)
- E7 ON: duels are shorter and the loser survives (yield), which is the design intent

### H9 — Armour: Heavy armour + HeavyBlunt vs None + LightCut
- **Heavy armour loses: 33.4% vs 64.9%**
- DR protects against damage but the heavier weapon's TN + armour stamina constraints offset it
- **[P3 FINDING]** Armour doesn't help in duels. The weapon-TN penalty associated with heavy loadouts exceeds the DR benefit. May be intentional (armour is for battlefield, not dueling).

### H10 — Feint-spam (every round feint) vs Balanced
- **Spammer wins 0.0%**
- 0 Defense every round → destroyed before pool reduction matters
- Feint is correctly non-exploitable; PP-294 design is robust

### H11 — Counter-puncher vs Aggressive
- **Counter-puncher loses: 26.7% vs 70.4%**
- Waiting for opponent's Stamina to drop doesn't work; aggressive player kills you first

### H12 — Long HeavyCut vs Short LightCut
- Same result as H4 (35.6% for heavy) — reach mechanics not modeled in this sim
- **[GAP]** Establish Distance / range advantage not simulated; Long weapons should have an approach-phase advantage per canonical §5

### Duration by Endurance (Balanced mirror, LightCut, E7 ON)

| End | Stamina | Health | MaxW | Rounds mean | Yield% | Incap% |
|---|---|---|---|---|---|---|
| 2 | 10 | 24 | 2 | 3.0 | 72% | 28% |
| 3 | 15 | 27 | 2 | 3.8 | 63% | 37% |
| 4 | 20 | 40 | 3 | 4.8 | 72% | 28% |
| 5 | 25 | 44 | 3 | 5.7 | 65% | 35% |
| 6 | 30 | 60 | 4 | 6.9 | 79% | 21% |
| 7 | 35 | 65 | 4 | 7.8 | 75% | 25% |

Duel duration scales linearly with Endurance (~1 round per End point). Yield is the primary outcome at all End values (65–79%). Incapacitation happens 21–37% of the time — these are the "fights to the death."

---

## 5. Findings Summary

### What works
1. **E7 (yield-at-0) produces shorter, less lethal duels** — design intent achieved. Duels are 3–8 rounds (18–80 seconds narrative). The loser survives in 65–79% of cases.
2. **Mirror matchups are symmetric** (47.9/48.6/3.5 draw) — no first-mover bias when yield checks are simultaneous.
3. **Feint is non-exploitable** — PP-294's "0 defense on feint round" prevents spam. The canonical design is robust.
4. **Agility advantage is meaningful but not crushing** (82.1% at +4 dice) — stat investment pays off without producing auto-wins.

### What doesn't work (P2 issues)
1. **Endurance too dominant** — controls three duel axes simultaneously (Stamina timer, Health pool, Wound Interval). A 2:1 End ratio produces 99.8% win rate. Fix candidates: decouple Stamina from End in duels (flat Stamina pool in C), or cap the End-advantage multiplier.
2. **Defensive play unrewarded** — Aggressive stance beats Defensive at 74/22. E5's read-and-counter dynamic needs a payoff for correct defense: counter-attack bonus when you correctly read the attacker's stance? Riposte mechanic?
3. **Feint never optimal** — designed for group combat (allies cover). In 1v1, PP-294's cost (0 defense) always exceeds the benefit (pool reduction next round). Fix candidates: reduce feint vulnerability in C (half defense, not zero), or add a feint payoff (immediate counter-strike on successful read).

### Gaps not modeled
1. **Establish Distance / range** — Long weapon approach-phase advantage per §5 not simulated. Long weapons should win the opening; Short weapons should win at Close range.
2. **Stunt opportunities** — arena-tagged environmental finishers (canonical §4 Stunt, max +5D) not modeled.
3. **Reputation Cascade integration** — §13.2 audience wiring verified canonical values but not exercised in the sim.
4. **Wager resolution** — R5 C5.1 stake severity not modeled.
5. **General Duel surface (§3.7)** — mass-battle zoom-in pacing (1 exchange per turn, max 5) not modeled.

### Design questions for Jordan
1. **Endurance dominance:** accept (End SHOULD be the duel stat), or fix (decouple Stamina from End in C)?
2. **Defensive play reward:** add a C-specific riposte mechanic (successful defense → free counter-attack at reduced dice)? Or accept that aggression dominates duels?
3. **Feint in C:** reduce vulnerability (half defense in C instead of 0)? Add a feint-specific payoff (successful feint = immediate damage, not just pool reduction)? Or accept feint is a group-combat tool?
4. **Three-swords loadout (Pirates! reference):** the synthesis missed this — Rapier/Longsword/Cutlass with attack/defense speed tradeoffs. Partial overlap with canonical weapon matrix. Surface as C-specific pre-duel choice, or leave as standard weapon selection?

---

## 6. References
- `params/combat.md` — canonical Combat Pool, Stamina, Health, Feint, weapons, armour
- `designs/scene/combat_v30.md` — §1-§4 resolution, §13.2 Reputation Cascade
- `designs/scene/derived_stats_v30.md §4.1` — PP-716 Health formula, wound penalty
- `designs/architecture/scale_transitions_v30.md §3.7` — General Duel (mass→personal)
- `tests/stress/combat_videogame_arch_2026-05-01/` — synthesis (01–07)
- `tests/sim/combat_arch_residual_stress_01/` — R1–R10 decisions
- Pirates! mechanics: web-verified 2026-05-13 (see manifest §Pirates! verification)
