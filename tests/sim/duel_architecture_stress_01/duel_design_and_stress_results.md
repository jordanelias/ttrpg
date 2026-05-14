# Architecture C — Duel System Design
## Date: 2026-05-13
## Status: PROPOSED — pending Jordan ratification
## Iterations: 14 (v1→v9, this session)
## Canonical basis: params/combat.md, designs/scene/combat_v30.md, designs/scene/derived_stats_v30.md

---

## 1. Core Principle

**The duel IS scene combat.** Same pool, same actions, same damage, same resolution. No parallel engine. The duel is a context layer — a different way to engage the same game.

A fight between two people in an alley is scene combat. A duel between two people in a courtyard with an audience is scene combat with stakes, witnesses, and spectacle. The mechanics are identical; the meaning is different.

---

## 2. Duel Context Layer

Four modifications to canonical scene combat when Architecture C fires:

### 2.1 Flat Stamina (C-specific)
**Duel Stamina = 15 + Endurance × 2** (replaces canonical End × 5 for C only).

Compresses the Endurance advantage: End 5 vs 4 goes from 97% to ~57%. End still matters (Health and Wound Interval scale canonically) but doesn't auto-decide. Duels reward technique over conditioning.

Does not affect scene combat outside C triggers.

### 2.2 Free-Rider Taunt (new action)
Declared alongside Strike. Not a separate action — you fight and provoke simultaneously.

- **Roll:** Cognition vs opponent's Composure, both TN 7
- **Cost:** +1 stamina over the base strike cost
- **On success:** opponent gains Rattled +1 (cumulative, max -1D pool penalty)
- **Cooldown:** 3 rounds between taunts
- **Historical basis:** Viking flyting (verbal combat during physical combat), Fiore's guard-as-provocation ("come against me and feel the pain" — Posta di Donna), Liechtenauer's psychological pressure during Zufechten

Rattled reduces the opponent's effective Combat Pool like wounds do. Stacks with wound penalty and Feint debuff (PP-294). Pool minimum 5 (ED-203) still applies.

Makes Cognition a meaningful duel stat without creating a dominant strategy.

### 2.3 Arena Stunt (canonical, contextualised)
Canonical Stunt (§4, +N dice to Offense, max +5, GM sets N) applied as arena rating.

Each duel location has an arena rating (0–5) representing environmental opportunities: furniture to kick, crowd to play to, terrain to exploit. The arena bonus applies to every strike-type action at +1 stamina cost.

**Arena changes the game character:**
- Arena 0: long fights (5+ rounds), stamina management dominates, light weapons favored
- Arena 3: moderate fights (3–4 rounds), balanced between technique and power
- Arena 5: short brutal fights (2–3 rounds), burst damage dominates, heavy weapons favored

### 2.4 E7 Yield
At Stamina 0, the combatant automatically receives a Yield offer per PP-634. They may accept (duel ends, yielder loses) or refuse (continue fighting at -2D OOB per canonical §7).

Creates non-lethal resolution. At End 4, ~26% of duels end in yield vs ~74% incapacitation.

---

## 3. All Canonical Actions Available

No actions are removed or modified (except PP-238, see §8). The full action palette:

| Action | Duel relevance |
|---|---|
| **Strike** | Core damage action. Pool split = the player's primary decision each round. |
| **Feint (PP-294)** | Commit N dice (min 3), remainder to defense. Opponent loses [margin]D next round. Punishes passive play. Feinter beats Defensive at 57–66%. |
| **Full Guard** | All dice to defense. Beats aggression via stamina attrition (82%). Vulnerable to Feint. |
| **Take a Breath** | Recovers (End + History) × 2 stamina. The strongest duel action — one breath buys 2+ strike rounds. |
| **Establish Distance** | Contested Agility to control range. Not modeled in sim; canonical §5. |
| **Tie Up** | Close range, both -2D. Historical "bind" (Fühlen). |
| **Disarm** | Offense vs STR+Agility. High-skill finisher. |
| **Stunt** | Arena-dependent bonus. See §2.3. |
| **Yield (PP-634)** | Declare at Phase 1. Opponent accepts or refuses. See §2.4. |
| **Disengage** | Agility contest. Escape the duel (with Reputation consequences). |

---

## 4. Triggers

Architecture C fires when both conditions are met:
1. Exactly 2 participants
2. One of six conditions: T-Wager / T-Cultural / T-Boss / T-Thread / T-Hero-Officer / T-Honor-call

If either fails → Architecture A (general scene combat). Refusal: Reputation/Conviction tag ("ducked the duel").

---

## 5. Emergent Dynamics (from 14 iterations, N=3000–5000 per test)

### 5.1 No imposed triangle
Win rates emerge from canonical dice resolution. The system produces an advantage web, not a clean RPS:

| Winner | Loser | % | Mechanism |
|---|---|---|---|
| Guard | Aggressive | 82% | Stamina attrition outlasts brute force |
| Feinter | Defensive | 57–66% | Pool reduction punishes passivity |
| Duellist | Feinter | 68% | Reactive reads counter deception |
| Adaptive | Aggressive | 62% | Reads + breath management |
| Aggressive | Defensive | 63% | Raw offense overcomes weak defense |

### 5.2 Protocol matters more than stats
Same build, different protocol = 20–43pp swing. A Tough character (End 6) using ADAPTIVE beats a Precise duellist (Agi 5, COG 5) 69%. The same Tough character using STAMINA_FIGHTER loses 6%. The game rewards tactical decisions on top of stat investment.

### 5.3 Arena controls the balance landscape
| Matchup | Arena 0 | Arena 3 | Arena 5 |
|---|---|---|---|
| Cunning vs Tough | Cunning **57%** | Even (46/49) | Tough **57%** |
| Fast vs Cunning | Fast **78%** | Fast **60%** | Fast **70%** |

Low arena: psychological pressure wins. High arena: raw stats win. The arena is the encounter-designer's balance dial.

### 5.4 Weapon choice is arena-dependent
Light weapons (dagger TN5) dominate low-arena duels — more hits per die, precision wins. Heavy weapons benefit from high-arena Stunt dice — extra dice amplify the damage modifier gap (HeavyBlade +6 vs LightBlade +3). The player who reads the arena and chooses their weapon accordingly has an advantage.

### 5.5 Stat hierarchy for duels
Agi > COG ≈ End > STR. Agility (pool) is universally dominant (+2D per point). Cognition (Taunt) and Endurance (Health/Stamina) trade off depending on arena and protocol. Strength (+1 flat damage) is the weakest duel stat — it matters more in group combat where Fibonacci bonus provides dice volume.

---

## 6. UI Presentation — Stance Labels

Pool-split bands are labeled in the UI as named stances. These are presentation only — no mechanical effect beyond the pool split itself.

| Pool split | Label | Description |
|---|---|---|
| ≥65% Offense | **Striking** | Committed attack. High risk, high reward. |
| 35–64% Offense | **Measured** | Balanced approach. Read and react. |
| ≤34% Offense | **Guarding** | Strong defense. Wait for the opening. |
| 0% Offense | **Full Guard** | All defense. No attack this round. |

These labels appear in the duel UI alongside the pool-split slider. The player sees "You are in a Striking stance" when they commit 70% to offense. The label has no mechanical weight — it's flavor derived from the player's actual decision.

Historical basis: Fiore's Pulsativa/Stabile/Instabile classification mapped to pool-split bands. The guards "speak" — they tell the opponent what you intend. Making the stance visible is the duel's read-and-counter dynamic.

---

## 7. Post-Duel

- **§13.2 Reputation Cascade:** guaranteed (duel context ensures 3+ witnesses). Public victory: +1 Combat Reputation. Kill: +1 additional. Overwhelming: +1 additional. Defeat: -1.
- **Wager Obligation:** resolves per contest type (R5 decision C5.1).
- **§13.1 Domain Echo:** fires if opponent holds faction office.
- **§13.3 Death Cascade:** fires if opponent killed.

---

## 8. Editorial: PP-238 vs PP-294

**PP-238** (params/combat.md L190): "Feint commits full Combat Pool to Offence; Defence = 0 this round."

**PP-294** (combat_v30.md §4 L95): "allocate N dice (minimum 3) to Offence for the feint; remaining dice available for Defence this round."

These contradict. PP-294 is newer, more detailed, and produces better gameplay (Feint as risk/reward decision vs. suicide). **Jordan directive: PP-294 governs. PP-238 Defence=0 is overruled.** Needs editorial commit to resolve the contradiction in params/combat.md.

---

## 9. References

### Canonical
- `params/combat.md` — Combat Pool, Stamina, Health, Feint, weapons, armour, initiative
- `designs/scene/combat_v30.md` — §1-§4 resolution, §7 Stamina, §13.2 Reputation Cascade
- `designs/scene/derived_stats_v30.md §4.1` — PP-716 Health, Wound Interval, wound penalty
- `designs/architecture/scale_transitions_v30.md §3.7` — General Duel (mass→personal)

### Historical fencing manuscripts
- Fiore dei Liberi, *Fior di Battaglia* (~1410) — Stabile/Pulsativa/Instabile guard classification; guard-as-provocation ("come against me and feel the pain")
- Johannes Liechtenauer, *Zettel* (~14th c.) — Vor/Nach/Indes (initiative flow); Fühlen (feeling in the bind); Zufechten/Krieg (approach/close combat phases); "Before and After, these two things, are to all skill a well-spring"

### Acclaimed games
- Sid Meier's Pirates! (2004) — visible stance, read-and-counter, arena backdrops. Initial inspiration, then surpassed by historical grounding.
- Sekiro: Shadows Die Twice (2019) — posture-as-yield, psychological pressure compounds with physical
- For Honor (2017) — free-action mind games during combat, directional guard commitment

### Stress test
- `tests/sim/duel_architecture_stress_01/duel_stress_test.py` — v9 consolidated sim
- `tests/sim/duel_architecture_stress_01/duel_design_and_stress_results.md` — this document
- 14 iterations, 13 commits, N=3000–5000 per hypothesis
