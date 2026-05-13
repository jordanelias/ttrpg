# Architecture C — Duel System Proposed Design v3b + Stress Test Results
## Date: 2026-05-13
## Status: PROPOSED (not canonical; pending Jordan ratification)
## Iteration: v3b (Fiore triangle + Fühlen bind + 2D distance)
## Sources: historical fencing manuscripts (Fiore dei Liberi ~1410, Liechtenauer ~14th c.), canonical params/combat.md + designs/scene/combat_v30.md, 2026-05-01 synthesis (E5/E7), R1-R10 decisions

---

## 1. Design Summary

Architecture C is a specialized duel architecture for 1v1 set-piece combat. Three modifications to canonical combat:

**E5 revised — Fiore stance triangle.** Replaces v1's flat Aggressive/Balanced/Defensive with a rock-paper-scissors triangle derived from Fiore dei Liberi's guard classification (*Fior di Battaglia*, ~1410):

| Stance | Historical basis | Pool split | Wins against | Payoff |
|---|---|---|---|---|
| **Pulsativa** (Striking) | Committed attack in progress | 75% Off / 25% Def | Instabile (catches mid-transition: priority attack, +1 momentum, no counter allowed) | 72.7% win rate |
| **Stabile** (Stable) | Strong defensive guard | 35% Off / 65% Def | Pulsativa (absorbs → **riposte**: free counter at +50% defense-pool bonus) | 76.4% win rate |
| **Instabile** (Mutable) | Provocative, baiting position | 50% Off / 50% Def | Stabile (provokes out of guard → **Meisterhau**: +2 bonus dice, defender at 2/3 defense) | 75.9% win rate |

Mirror matches: Pulsativa×Pulsativa → both strike + **bind contest** (Fühlen). Stabile×Stabile → probing, minimal damage, drains stamina slowly. Instabile×Instabile → probing.

Lower-initiative player declares stance first (canonical §3). Higher-initiative player reads and counters.

**E7 — Posture-as-yield.** Unchanged from v1. Stamina=0 ends duel in yield. Fires 15–45% of duels depending on Endurance level.

**Fühlen (bind contest).** When both combatants choose Pulsativa simultaneously, blades meet in a bind. Contested Endurance roll (not Agility) at TN7 determines who wins the bind → winner gets +2D advantage next round + initiative. Bind pulls combatants to Krieg (close) range and costs extra stamina. Derived from Liechtenauer's concept of sensing pressure when blades cross.

**2D distance.** Three bands: Zufechten (approach, >2.0 — no combat), Striking (1.0–2.0 — full exchanges), Krieg (close, <1.0 — bind range). Duels start at 2.5 (approach). Advancing costs 2 stamina per step; retreating costs 2 but covers less ground. Creates a 1–2 round approach phase before combat begins.

**All canonical combat math unchanged:** Combat Pool, Stamina, Health/Wounds/Wound Interval, Feint (PP-294), initiative transfer, damage formula, weapon TN matrix, armour DR.

---

## 2. Triggers, Flow, Post-Duel

Unchanged from v1. Six trigger conditions (T-Wager / T-Cultural / T-Boss / T-Thread / T-Hero-Officer / T-Honor-call). Refusal costs Reputation tag. Post-duel: §13.2 Reputation Cascade, Wager Obligation.

---

## 3. Stress Test Results (v3b, N=5000)

### 3.1 Triangle validation — PASS

Triangle legs balanced within 5pp of each other (72.7–76.4%). No degenerate strategy. Nash equilibrium (1/3 each) produces all three special mechanics firing: 0.5 binds, 0.9 ripostes, 0.9 Meisterhau per duel.

### 3.2 Protocol comparison

| Matchup | A wins | B wins | Interpretation |
|---|---|---|---|
| Adaptive vs Adaptive | 50.6% | 49.4% | Symmetric — no first-mover bias |
| Berserker vs Turtle | 17.0% | 76.4% | **Defensive play rewarded** (v1 had 74% aggressor wins — fully reversed) |
| Berserker vs Counter-fighter | 71.2% | 25.8% | Counter-fighter's alternating pattern predictable vs pure commitment |
| Trickster vs Adaptive | 35.4% | 62.7% | Pure instabile not viable alone |
| Counter-fighter vs Adaptive | 38.7% | 61.3% | Rigid strategy loses to flexibility |
| Nash vs Nash | 48.7% | 47.6% | Symmetric; all mechanics fire |
| Distance-weighted vs Adaptive | 59.3% | 36.5% | Distance awareness confers ~10pp edge |

### 3.3 Stat asymmetry

| Matchup | Advantage | Win % | Assessment |
|---|---|---|---|
| Agi 5 vs 3 | Pool 15 vs 11 (+36%) | 93.9% | Too dominant — pool is linear in Agi via (Agi×2) |
| End 6 vs 3 | Stam 30vs15, HP 60vs27, MW 4vs2 | 94.8% | Too dominant — End triple-dips |
| End 5 vs 4 | Stam 25vs20, HP 44vs40 | 67.6% | Significant for 1 point; may be acceptable |
| STR 6 vs 3 | +3 damage per hit | 61.1% | Moderate — healthy range |

### 3.4 Duration by Endurance

| End | Stamina | HP | Rounds | Yield% | Incap% |
|---|---|---|---|---|---|
| 2 | 10 | 24 | 2.9 | 45% | 55% |
| 3 | 15 | 27 | 3.5 | 27% | 73% |
| 4 | 20 | 40 | 4.3 | 26% | 74% |
| 5 | 25 | 44 | 4.8 | 15% | 85% |
| 6 | 30 | 60 | 5.9 | 19% | 81% |
| 7 | 35 | 65 | 6.4 | 12% | 88% |

Duels are 3–6 rounds (18–60 seconds narrative). At End 4 (default), ~26% yield, ~74% incap. E7 fires most at low Endurance where Stamina runs out before Health.

---

## 4. NERS Audit

### Fiore Triangle (E5 revised)
- **N (Necessary):** Yes — without it, aggressive dominates and defense is unrewarded. Triangle creates meaningful per-round choice with rock-paper-scissors counter dynamics.
- **R (Robust):** Yes — balanced legs (72–77%), multiple viable protocols, no degenerate strategy. Player can choose approach (aggressive, defensive, tricky, adaptive, mixed) and each has different matchup profiles.
- **S (Smooth):** Mostly — integrates onto canonical pool-split cleanly; stance IS the pool-split, named and visible. Bind integrates with initiative. Distance integrates with historical Zufechten/Krieg mapping. Remaining gap: weapon reach not yet differentiated in distance model.
- **E (Elegant):** Yes — three stances, one payoff matrix, one decision per round. Player can intuit: "I'm defending → they'll bait me → I should attack" = the triangle.

### Fühlen Bind
- **N:** Marginal — fires 0.5/duel at Nash. Statistically rare. BUT: "blades lock, you feel their strength" is a high-drama moment. May be necessary for feel even if rare.
- **R:** Yes — produces interesting sub-decision (who wins the bind → next round initiative + advantage).
- **S:** Yes — uses END (physical grapple, not speed), produces Krieg range, costs extra stamina.
- **E:** Yes — one contested roll, one outcome.

### 2D Distance
- **N:** Partial — creates approach phase and Zufechten→Krieg mapping. But Long vs Short weapons produce identical results because reach advantage isn't implemented.
- **R:** Partial — distance-weighted protocol wins at 59% over adaptive, showing awareness helps. But distance decisions are shallow.
- **S:** Clean integration with historical source concepts.
- **E:** Yes — one axis, three bands, simple.

---

## 5. Throughline: Pirates! → Historical → Fiore Triangle

| Element | Pirates! origin (v1) | Historical grounding (v3b) | Canonical integration |
|---|---|---|---|
| Visible stance commit | 3 guards (high/mid/low) | Fiore's 12 guards → 3 classifications (Stabile/Pulsativa/Instabile) | = canonical pool-split, named |
| Read-and-counter | Attack/block per guard | Liechtenauer Vor/Nach/Indes — lower-init declares first | = canonical initiative transfer §3 |
| "Defense creates opportunity" | Not in Pirates! | Riposte (Liechtenauer: "good parries apply a thrust in opposition") | NEW mechanic |
| "Deception provokes error" | Not in Pirates! | Meisterhau (Fiore: Instabile guards "often deceive the other guards") | NEW mechanic; replaces Feint as deceptive option in 1v1 |
| Blades meet | Not in Pirates! | Fühlen (Liechtenauer: sensing pressure in the bind) | NEW mechanic |
| Stamina → yield | Misattributed to Pirates! in v1; actually Sekiro | Sekiro posture-as-yield (correctly attributed) | E7 modification to canonical Stamina |
| Distance bands | Edge-push / positioning | Zufechten / Krieg / Abzug (Liechtenauer) | Maps to canonical Establish Distance §5 |

**R2 decision (cognitive-only, no motor-skill layer) still holds.** The triangle is a cognitive pre-commit — choose your stance, see your opponent's stance, resolve per matrix. No timing/animation skill required. This maps to Valoria's canonical "phase-based, blind declaration, then resolution" structure.

---

## 6. Remaining Issues

### P2 (balance concerns)
1. **Stat dominance at 2:1 ratios.** Both Agi (93.9%) and End (94.8%) produce near-auto-wins at 5 vs 3. This is a property of canonical stat formulas (Pool = Agi×2; Stamina = End×5; Health = (End+6)×(MW+1)), not specific to Architecture C. Possible C-specific mitigations: flat Stamina in duels (15 + End×2 instead of End×5), or cap Pool advantage in C. Jordan decision.
2. **End 5 vs 4 = 67.6%.** One stat point produces a 35pp swing. May be acceptable (End is "the duel stat" — conditioning matters) or may indicate Stamina formula scales too steeply. Explore alternative: Stamina = 10 + End×3 in C.

### P3 (unmodeled)
3. **Weapon reach.** Long vs Short weapons produce identical results. Reach advantage at Zufechten range (Long can strike, Short must close first) is canonical (§5) but not implemented in the sim.
4. **Stunt opportunities.** Arena-tagged environmental actions (§4 Stunt, max +5D) not modeled.
5. **Mirror-match pacing.** Stabile vs Stabile goes 8 rounds of probing into mutual yield — correct behavior (two turtles should stalemate) but may feel tedious in-game. UI should accelerate or auto-resolve stalemate mirrors.

### Gaps
6. **§13.2 Reputation Cascade integration.** Canonical values verified but not exercised in sim.
7. **Wager resolution.** R5 C5.1 stake severity not modeled.
8. **General Duel (§3.7) pacing.** Mass-battle zoom-in (1 exchange per turn, max 5) not modeled.
9. **Feint (PP-294) in Architecture C.** Not modeled in v3b — Meisterhau replaces Feint's role as the deceptive option. Should PP-294 Feint remain available as a 4th action in C, or does Instabile subsume it? Jordan decision.

### Design questions for Jordan
1. Stat dominance mitigation: flat Stamina in C, or accept that Agi/End are "duel stats"?
2. Feint in C: keep PP-294 as 4th action alongside triangle, or Instabile replaces it?
3. Mirror-match stalemate: auto-resolve after N rounds of probing, or force escalation?

---

## 7. Version History

- **v1 (2026-05-13):** Pirates!-inspired Aggressive/Balanced/Defensive. P2: defense unrewarded, feint never optimal, End dominant. Committed as 3b1c497.
- **v2 (2026-05-13):** Fiore triangle + Fühlen + 2D. Agi replaced End as dominant stat. Meisterhau too strong (95%). Triangle directionally correct but unbalanced.
- **v3 (2026-05-13):** Nerfed Meisterhau too hard — Stabile dominant (beat both Pulsativa AND Instabile). Triangle broken.
- **v3b (2026-05-13):** Meisterhau at +2 bonus + 2/3 defense. Pulsativa +1 momentum. **Triangle balanced: 72–77% on all three legs.** Defensive play rewarded. No degenerate strategy.

---

## 8. References
- Fiore dei Liberi, *Fior di Battaglia* (~1410) — Stabile/Pulsativa/Instabile guard classification. Web-verified 2026-05-13.
- Johannes Liechtenauer, *Zettel* (~14th c.) — Vor/Nach/Indes, Fühlen (feeling in the bind), Zufechten/Krieg. Web-verified 2026-05-13.
- `params/combat.md` — Combat Pool, Stamina, Health, Feint, weapons, armour
- `designs/scene/combat_v30.md` — §1-§4 resolution, §13.2 Reputation Cascade
- `designs/scene/derived_stats_v30.md §4.1` — PP-716 Health, wound penalty
- `tests/stress/combat_videogame_arch_2026-05-01/` — E5/E7 synthesis
- `tests/sim/combat_arch_residual_stress_01/` — R1-R10 decisions
