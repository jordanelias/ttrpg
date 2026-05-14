# Architecture C — Duel System: Final Proposed Design (v9)
## Date: 2026-05-13
## Status: PROPOSED — 12 iterations validated. Pending Jordan ratification.
## Commits: 3b1c497 → 306a391 → d3779e2 → bdcbb18 → 9569ae5 → 3ad66b2 → 71f21d4 → fef7722 → f02612e

---

## 1. Design thesis

A duel is scene combat with context. Same pool, same actions, same resolution. The duel system adds five context layers — no parallel engine, no imposed outcomes, no top-down triangle.

**What makes a duel different from a fight:** stakes, audience, arena, psychology, and read. A bar brawl has none of these. A formal duel has all five. The system scales along these axes.

---

## 2. The five duel axes

### 2.1 Stakes (E7 yield)
At Stamina 0 in Architecture C, the combatant receives an automatic Yield offer per PP-634. They can accept (lose the duel, survive) or refuse (continue at −2D OOB, risk death). This creates a non-lethal exit that scene combat doesn't provide by default.

**Canonical basis:** PP-634 Yield + Stamina OOB (designs/scene/combat_v30.md §7). No new rules.

### 2.2 Audience (§13.2 Reputation Cascade)
Duel triggers guarantee 3+ witnesses (public combat), so §13.2 Combat Reputation always fires. Wager Obligation resolves per R5 C5.1 (contest-type stakes). The social consequences of the duel are mechanical, not narrative decoration.

**Canonical basis:** designs/scene/combat_v30.md §13.2. No new rules.

### 2.3 Arena (Stunt)
The duel arena provides consistent Stunt opportunities. Canonical Stunt: +N dice to Offense (GM sets N, max +5), declared with Strike. In duel context, arena rating (0–5) represents the richness of the environment for crowd-pleasing, terrain-using, dramatic combat.

**Emergent finding:** Arena rating changes the optimal weapon. At arena 0, light weapons (low TN) dominate because precision matters more with fewer dice. At arena 3–5, heavy weapons benefit more because Stunt dice amplify damage modifiers. Arena inverts the weapon meta.

**Cost:** +1 stamina per Stunt Strike (6 total vs 5 for plain Strike).

**Canonical basis:** designs/scene/combat_v30.md §4 Stunt. Extended with arena-rating parameter.

### 2.4 Psychology (Taunt — new, free-rider)
Taunt is declared alongside Strike (same principle as Stunt alongside Strike). You fight AND trash-talk. Not instead of fighting.

**Mechanic:** Roll COG vs opponent's Composure at TN 7 as a secondary check during your Strike round. Success: opponent gets cumulative −1D to Combat Pool (maximum −3D). Let It Ride: 3-round cooldown after each Taunt attempt (success or failure).

**Cost:** +1 stamina on the Taunt-Strike round (6 total, or 7 for Taunt-Stunt-Strike).

**Emergent finding:** COG 3→7 = ~2pp win rate difference. Composure 3→7 = ~3pp. Neither stat dominates — they're secondary channels alongside the primary combat stats (Agi, End, STR). Taunt debuff accumulates over fight length: 0.4 debuff/duel in short fights (End 3, 2.8 rounds) → 0.9 debuff/duel in long fights (End 6, 5.8 rounds). Psychology rewards patient fighters.

**Historical basis:** Liechtenauer's principle that every action contains both attack and defense. "Fighting is a conversation" — trash talk is part of the conversation. Talhoffer's judicial duels were social performances where verbal dominance mattered alongside martial skill.

### 2.5 Read (initiative information advantage)
Canonical §3: lower-initiative combatant declares pool split first. Higher-initiative combatant sees the commit and reacts. This is the core read-and-counter mechanic.

**Emergent finding:** Initiative info advantage is worth ~3pp per round. Over a 4-round duel, the combatant who consistently has initiative accumulates a ~12pp total advantage. Agi controls initiative → Agi controls reads → Agi is the duel's primary skill stat.

**Historical basis:** Liechtenauer's Vor/Nach/Indes. "Before and After, these two things, are to all skill a well-spring." The fighter who acts in the Vor (with initiative) sees the opponent's Nach (response) and acts Indes (immediately, with full information).

---

## 3. Duel-specific parameter: flat Stamina

**Formula:** Duel Stamina = 15 + Endurance × 2 (range 17–29).

**Why:** Canonical Stamina = End × 5 (range 5–35) makes Endurance too dominant in the stamina-management game that defines duels. One End point = ~50pp win rate under canonical formula. Flat Stamina compresses this to ~7pp per End point.

**Effect on End asymmetry:**

| Gap | Canonical | Flat |
|---|---|---|
| End 5 vs 4 | 97.1% | 57.3% |
| End 6 vs 3 | 100% | 85.8% |

End still matters (conditioning SHOULD matter) but no longer auto-wins. At 3+ End point gap, End still dominates — primarily through Health and Wound Interval, not Stamina. This is correct: a massive conditioning gap should be decisive.

**Scope:** Architecture C duels only. Canonical Stamina unchanged for scene combat and mass battle.

---

## 4. PP-238 / PP-294 resolution

PP-238 states Feint Defense = 0. PP-294 (newer, in combat_v30 §4) states "remaining dice available for Defence this round." These contradict.

**Resolution per Jordan directive:** PP-294 governs. Feint commits N dice (minimum 3) to the versus roll; remainder defends. Defense = 0 was always wrong. Feint is a risk/reward decision (commit more = higher margin but less defense), not a suicide pact.

**Effect:** Feint win rate as a strategy improved from 0% (v1, Defense=0) to ~46% (v9, defense retained). Feint is now a viable setup tool, not a guaranteed loss.

**Editorial action needed:** Flag PP-238/PP-294 contradiction in `params/combat.md` for canonical resolution. Recommend: PP-238 superseded by PP-294.

---

## 5. Trigger conditions (unchanged from synthesis)

Architecture C fires when both conditions are met:
1. Exactly 2 participants
2. One of: T-Wager / T-Cultural / T-Boss / T-Thread / T-Hero-Officer / T-Honor-call

Refusal: Reputation/Conviction tag ("ducked the duel"). NPC refusal per AI temperament.

If either condition fails → Architecture A (scene combat). No context layers apply except standard §13.2 (if witnesses present).

---

## 6. NERS audit

### Scene combat chassis
- **N:** Cannot be removed. One combat system for all contexts reduces cognitive load, implementation cost, balance surface.
- **R:** All canonical actions available. Multiple viable strategies emerge bottom-up.
- **S:** Zero mechanical friction with existing combat. Player already knows the system.
- **E:** "It's just combat, but it matters more." Immediate player comprehension.

### E7 yield
- **N:** Provides non-lethal exit. Fires 15–45% of duels depending on Endurance.
- **R:** Creates distinct pacing — yield-or-die pressure point. Player chooses.
- **S:** Uses canonical Stamina + PP-634 Yield.
- **E:** "Your arms are lead. Yield, or be cut down." One threshold, one choice.

### Arena (Stunt)
- **N:** Differentiates duel environments. High arena = short/lethal/spectacular.
- **R:** +3D = 69% win rate. Arena inverts weapon meta (emergent, not imposed).
- **S:** Canonical Stunt mechanic. Arena rating is a parameter, not a new rule.
- **E:** "Use the environment." Intuitive.

### Taunt (free rider)
- **N:** Makes COG relevant in combat. Differentiates duels from fights (psychology).
- **R:** COG 3→7 = 2pp. Composure 3→7 = 3pp. Neither dominant. Cumulative −1D rewards patience.
- **S:** Declared with Strike. Same resolution channel as pool reduction. Cost: +1 stamina.
- **E:** "You fight AND trash-talk." One secondary roll per Taunt round.

### Flat Stamina
- **N:** Fixes End dominance (97% → 57% at End 5v4).
- **R:** End still matters. 3+ point gap still decisive (via Health/WI).
- **S:** One formula change, C-specific.
- **E:** "Duels reward technique over raw conditioning."

---

## 7. Historical throughlines

| Source | Concept | Mechanical mapping |
|---|---|---|
| Liechtenauer (~14th c.) | Vor/Nach/Indes — initiative IS the fight | Initiative info advantage (§3: declare last, see commit) |
| Liechtenauer | "Every action contains attack AND defense" | Taunt as free rider (declared with Strike, not instead of) |
| Liechtenauer | Fühlen — feeling in the bind | Tie Up mechanic (canonical §4) at close range |
| Liechtenauer | Zufechten/Krieg/Abzug — three distances | Establish Distance (canonical §4) + zone rules (§5) |
| Fiore (~1410) | Stabile/Pulsativa/Instabile — guard intent | UI labels on pool-split bands (Guarding / Striking / Measured) |
| Fiore | "Instabile guards often deceive the other guards" | Feint (PP-294) provokes defensive overcommit |
| Silver (1599) | "True fight: time, place, advantage" | Initiative (time), arena (place), stat reads (advantage) |
| Talhoffer (1467) | Judicial duel = social performance | §13.2 Reputation Cascade + audience + Taunt |
| Pirates! (2004) | Weapon selection, advantage meter, arena | Weapon TN choice, Stamina, Stunt |
| Sekiro (2019) | Posture-as-yield | E7: Stamina 0 → yield offer |
| For Honor (2017) | Directional guard, feats | Pool split visualization, Stunt as passive ability |

### Meta-throughlines

**"Fighting is a conversation."** Every round, both combatants act and react. The initiative system creates an information asymmetry that rewards the better reader. Taunt extends the conversation to the psychological dimension. The duel is a dialogue of steel and words.

**"The weapon shapes the fight."** Light weapons (low TN) reward precision in resource-scarce environments. Heavy weapons reward power when extra dice (Stunt, Fibonacci) are available. The player's weapon choice reflects their build and their read of the arena.

**"The arena shapes the fight."** High-arena environments (rich terrain, dramatic setting) produce short, lethal, spectacular duels. Low-arena environments produce grinding, technical attrition contests. The arena is a design knob for encounter pacing.

**"Conditioning underpins but doesn't dominate."** Stamina management is the dominant strategy. But flat Stamina ensures that technique (Agi → pool → initiative), psychology (COG → Taunt), and arena mastery (Stunt) can overcome a conditioning gap.

---

## 8. Emergent advantage web (not a triangle)

No imposed rock-paper-scissors. Win rates emerge from canonical resolution:

| Strategy | Beats | Beaten by | Why |
|---|---|---|---|
| Feint | Defensive play | Aggressive play | Pool reduction punishes passivity; defense=retained prevents suicide |
| Guard / Stamina play | Aggressive play | Feint, Taunt | Patience outlasts brute force; but feint/taunt erode the guard |
| Aggressive | Feinter (via tempo) | Guard, Reactive play | Committed offense is fast but predictable; reads exploit commitment |
| Reactive (Duellist) | Most strategies | Equal-pool brute force | Info advantage + taunt pressure compound; fails vs equal stats + higher damage |

The web isn't perfectly balanced — that's correct. Real fighting isn't balanced. The player's task is to read their opponent and choose the right approach.

---

## 9. Open items

1. **English stance labels** — Striking (≥65% offense), Guarding (≥65% defense), Measured (middle). UI layer only, no mechanical effect.
2. **PP-238 editorial** — flag contradiction with PP-294 in canonical params.
3. **Weapon reach** — Long weapons should have approach-phase advantage per §5. Not modeled in sim. Design consideration for implementation.
4. **General Duel (§3.7)** — mass-battle zoom-in pacing (1 exchange per turn, max 5). Separate surface from scene-scale duels. Not tested.
5. **Taunt interaction with NPC Composure** — how does NPC Composure generation work? Does it use the Composure from derived_stats? Verify against canonical.
6. **Arena rating authoring** — who sets arena rating? Scene author? Random per zone? Needs guidance for encounter design.

---

## 10. Version history

| Version | Key change | Result |
|---|---|---|
| v1 | Pirates!-style flat stances | Aggression dominant, defense unrewarded |
| v3b | Fiore-imposed triangle | Balanced but top-down — not emergent |
| v4 | Scene combat chassis | No natural RPS; stamina management dominant |
| v5 | Initiative info advantage modeled | ~3pp value; PP-294 Feint fix |
| v6 | Duellist protocol iterated | Builds differentiate; Stunt bug found |
| v7b | Arena Stunt integrated | Arena inverts weapon meta |
| v8 | Forced-action Taunt tested | COG dead — effect too weak as standalone action |
| v8b | Taunt priority fix | COG still dead — action-economy cost too high |
| v9 | **Free-rider Taunt** | **COG differentiates. System validated.** |
