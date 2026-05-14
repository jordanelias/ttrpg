# Architecture C — Duel System v4: Scene Combat Chassis + Context Layer
## Date: 2026-05-13
## Status: PROPOSED — canonical chassis validated, context layer in iteration
## Iteration: v4 (replaces v3b's imposed triangle with bottom-up emergence)

---

## 1. Design Thesis

The duel IS scene combat. Same pool, same actions, same damage, same resolution. The "duel" is a context layer:

1. **Trigger:** 2 participants + narrative condition (T-Wager / T-Cultural / T-Boss / T-Thread / T-Hero-Officer / T-Honor-call)
2. **E7 yield:** Stamina=0 → automatic Yield offer (PP-634)
3. **Taunt (new action):** Cognition vs Composure → opponent must declare pool split first next round
4. **Audience:** §13.2 Reputation Cascade guaranteed (3+ witnesses)
5. **Arena Stunts:** environment-specific Stunt flavor

No imposed triangle. No hardcoded stance→outcome lookup. Win rates emerge from canonical dice engine.

---

## 2. What the Canonical System Actually Produces (N=5000)

### 2.1 Pool-split dynamics — no natural RPS

| A's split | B's split | A wins | B wins | Interpretation |
|---|---|---|---|---|
| 75/25 (aggressive) | 30/70 (defensive) | **59.8%** | 31.9% | Offense dominates raw exchanges |
| 75/25 (aggressive) | 50/50 (balanced) | 48.3% | 43.6% | Marginal aggressive edge |
| 30/70 (defensive) | 50/50 (balanced) | 27.5% | **48.8%** | Defensive alone is never optimal |
| 50/50 mirror | — | 45.7% | 46.5% | Symmetric |
| Full Guard (0/100) | 75/25 (aggressive) | **89.6%** | 10.4% | **Stamina attrition crushes aggression** |

**Finding:** The canonical system has two modes, not three:
- **Offense race:** more dice to offense → more hits → win before stamina runs out. Aggressive > Defensive > Balanced in raw striking.
- **Stamina attrition:** Full Guard / Take a Breath + defensive play outlasts pure aggression. The aggressor burns 5 stamina/round striking; the defender burns 3/round guarding and can Take a Breath to recover.

This isn't RPS — it's a continuum where the optimal split depends on your stamina runway vs your opponent's. The "triangle" lives in the player's read of this tradeoff, not in the stance label.

### 2.2 Canonical actions in duel context

| Matchup | A wins | Mechanism |
|---|---|---|
| Feinter (every 3rd round) vs Balanced | 26.1% | PP-294 Defense=0 exposure too punishing for the margin gain |
| Feint-spam vs Balanced | 0.0% | Confirmed non-exploitable (PP-238 correct) |
| Stamina-fighter (Take a Breath) vs Aggressive | **79.5%** | **Stamina management is the dominant duel strategy** |
| Brawler (Tie Up) vs Balanced | 37.5% | Tie Up -2D both sides; doesn't differentially advantage the initiator |

**Finding:** Take a Breath is the strongest duel action. Recovers (End + History) × 2 stamina at cost of one round's offense — at End 4, History 2, that's 12 stamina recovered. One breath buys 2+ more strike rounds. The player who manages breath timing wins.

**Finding:** Feint (PP-294) is correctly a high-risk/high-reward group-combat tool. In 1v1, the Defense=0 exposure round is too costly. But the 0.82 feints landed per duel at Feinter protocol shows it DOES land — it just doesn't compensate for the damage taken on the exposed round.

**Throughline to Fiore/Liechtenauer:** This matches historical swordplay. Liechtenauer emphasizes that every defensive action should simultaneously threaten (Meisterhau); purely defensive actions that create no threat are "bad parries." The canonical system agrees — Full Guard creates no threat but wins via attrition. Historical masters would call that a stalemate, not a victory. The interesting play is in the read: "my opponent is tired, I can commit more offense NOW" — that's Vor.

### 2.3 Taunt (new duel action) — currently broken

| Matchup | A wins | Issue |
|---|---|---|
| Taunter vs Balanced | 92.1% | Taunt + defensive split = stamina-efficient dominance |
| Taunter vs Adaptive | 94.2% | Adaptive can't counter the stamina advantage |
| Taunter (COG 6) vs Balanced | 92.4% | COG boost barely changes outcome — the issue is cost, not effectiveness |

**Diagnosis:** Taunt costs 3 stamina (same as defensive stance) but produces a compound advantage: forces opponent to declare first (losing initiative information) + Taunter uses 30/70 defensive split on Taunt rounds (conserving health). The Taunter protocol is effectively Stamina-fighter + initiative disruption. The issue is the stamina cost/benefit ratio, not the mechanic concept.

**Fix candidates (to test next iteration):**
- Raise Taunt stamina cost to 5 (same as Strike) — you're exerting to provoke
- Require minimum offense allocation on Taunt round (can't Full Guard while Taunting — you have to show something)
- Make Taunt contested differently: Cognition vs opponent's Cognition (not Composure) — smarter opponents resist better
- Limit Taunt to once every 3 rounds (like Let It Ride on maneuvers per §11.5)

### 2.4 Build archetypes — End dominance, weapon selection

| Build A | Build B | A wins | Finding |
|---|---|---|---|
| Duellist (COG 6, Agi 5, End 3) | Brawler (STR 6, End 5, Agi 3) | **0%** | End 3 = Stamina 15 = dead in 3 rounds regardless of skill |
| Duellist (default stats) | Adaptive (default stats) | 98.2% | Duellist protocol works IF End isn't crippled |
| Counter-puncher (End 6, Agi 3) | Aggressive (Agi 5, End 3) | **100%** | End advantage absolutely dominates |
| Agi 5 vs Agi 3 | — | 72.4% | Pool advantage is meaningful (15 vs 11) but not crushing |
| End 5 vs End 4 | — | **91.6%** | ONE point of End = 91.6%. Stamina 25 vs 20 = one more round. |
| STR 6 vs STR 3 | — | 56.8% | Moderate. Healthy range. |

**Finding:** Endurance dominance is canonical, not duel-specific. The formula Stamina = End × 5 produces a linear stamina curve where each End point = 5 more stamina = 1 more round of strikes. In a system where stamina management IS the dominant strategy, the stat that controls stamina IS the dominant stat.

**Decision-shaped finding for Jordan:** This is a CANONICAL BALANCE question, not a duel question. Options:
- Accept: End IS the duel stat. High End = better duelist. Builds must invest End or lose.
- Mitigate in C only: duel Stamina = flat base + small End scaling (e.g., 15 + End × 2 instead of End × 5). Flattens the curve without changing canonical combat.
- Mitigate canonically: change the Stamina formula globally. Much larger blast radius.

### 2.5 Weapon matchups — light weapons dominate duels

| Matchup | A wins | TN difference |
|---|---|---|
| Dagger TN5 vs Longsword TN7 | **76.7%** | +2 TN gap = more hits per die |
| Arming sword TN6 vs Longsword TN7 | **68.5%** | +1 TN gap |
| Arming sword TN6 vs Warhammer TN8 | **90.0%** | +2 TN gap |
| Dagger TN5 vs Mace TN7 | **79.4%** | +2 TN gap |

**Finding:** Light, fast weapons (low TN) dominate 1v1 duels. Heavy weapons are designed for group combat — the damage modifier vs armour tier (+6 Heavy Blade vs None) doesn't compensate for TN 7 missing more often than TN 5. This is canonical and intentional: the Fibonacci group bonus (+5D cap at 8+) offsets the TN penalty in group combat.

**Throughline to historical manuscripts:** This matches real-world dueling history. Renaissance dueling favored the rapier (fast, thrusting, low-TN equivalent) over the longsword (slower, heavier, designed for battlefield). Fiore's system covers both but his rapier/sword-in-one-hand sections are explicitly labeled for single combat. The canonical weapon system already encodes this.

**Implication for player builds:** A duel-specialist build wants ShortLightBlade (TN 5) and invests in Agility (pool) and Endurance (stamina). A battlefield build wants LongHeavyBlade (TN 7) and relies on allies for Fibonacci bonus. These are DIFFERENT BUILDS for different contexts — the game creates build tension naturally.

### 2.6 Duration and pacing

| End | Stamina | Rounds | Primary end condition | Feints/duel |
|---|---|---|---|---|
| 2 | 10 | 2.8 | Yield (80%) | 0 |
| 3 | 15 | 3.3 | Yield (56%) / Incap (44%) | 0.24 |
| 4 | 20 | 4.6 | Yield (75%) / Incap (25%) | 0.39 |
| 5 | 25 | 5.4 | Mixed | 0.40 |
| 6 | 30 | **10.2** | Incap (90%) | 0.72 |
| 7 | 35 | **11.6** | Incap (88%) | 1.13 |

**Finding:** Duel duration bifurcates at End 5/6. Below End 5, stamina runs out before health — yield is primary. Above End 5, stamina lasts long enough that the fight becomes a health attrition contest (incap dominates). The transition happens because Stamina = End × 5 means End 6 = 30 stamina = 6 strike rounds, while Health at End 6 = 60 with Wound Interval 12 = can absorb ~5 wounds. The stamina pool outlasts the health pool at high End.

**Design implication:** Duels between low-End characters (End 2–4) are short and often end in yield — narratively satisfying, less lethal. Duels between high-End characters (End 6–7) are prolonged slugfests that usually end in incapacitation — more brutal. The game can use End as a pacing dial: NPC duelist with End 3 creates a 3-round quick draw; boss duel with End 6 creates a 10-round endurance test.

---

## 3. NERS Audit

### Duel-as-scene-combat (the chassis)
- **N (Necessary):** YES. No parallel engine. One combat system for all contexts. Reduces cognitive load, implementation cost, and balance surface.
- **R (Robust):** YES. All canonical actions available (Strike, Feint, Full Guard, Take a Breath, Establish Distance, Tie Up, Disarm, Stunt, Yield, Disengage). Multiple viable strategies (offense-race, stamina attrition, feint setup). Builds differentiate (Agi→pool, End→stamina, STR→damage, COG→taunt).
- **S (Smooth):** EXCELLENT. Zero new resolution mechanics. Player already knows combat; duel is the same thing with higher stakes and audience. Transitions seamlessly from/to scene combat (no state migration).
- **E (Elegant):** YES. "It's just combat, but it matters more." One new action (Taunt). Everything else is canonical.

### E7 (yield at Stamina 0)
- **N:** YES at low End (End 2–4 where yield fires 56–80%). Provides non-lethal duel resolution. Questionable at high End where stamina outlasts health.
- **R:** YES. Creates distinct pacing — the "yield or die" pressure point. Player can choose to keep fighting at -2D OOB (canonical) instead of yielding.
- **S:** CLEAN. Uses canonical Stamina rules + canonical Yield (PP-634). No new formula.
- **E:** YES. "Your arms are lead. Yield, or be cut down." One threshold, one choice.

### Taunt (new action)
- **N:** QUESTIONABLE in current state (92% win rate = degenerate). Concept is necessary — social pressure IN combat is the duel-vs-fight distinction. Implementation needs rebalancing.
- **R:** NO — currently dominant strategy. Must be fixed.
- **S:** Clean mechanically (Cognition vs Composure). But the effect (forced first declaration) interacts badly with defensive pool splits.
- **E:** YES in concept. "Get in their head." Intuitive for players.

### Stances as labels (Fiore vocabulary)
- **N:** NO as mechanics (v3b's imposed triangle was top-down). YES as UX vocabulary — naming the player's pool split "Pulsativa" (offense-heavy) or "Stabile" (defense-heavy) adds flavor without adding mechanics.
- **R:** N/A — labels don't affect resolution.
- **S:** CLEAN — just UI presentation.
- **E:** YES — historical flavor at zero mechanical cost.

---

## 4. Throughlines

### Historical fencing → canonical combat → duel

| Historical concept | Canonical mechanic | Duel context |
|---|---|---|
| **Vor/Nach** (Before/After — initiative) | Initiative holder declares LAST (§3) | Same — the read-and-counter is already here |
| **Fühlen** (feeling in the bind) | Tie Up (§4) — close range, both -2D, escape requires STR contest | Same — bind IS Tie Up |
| **Meisterhau** (parry that simultaneously strikes) | Having initiative + reading opponent's commit → optimal pool split allocation | Same — the init holder's advantage IS the Meisterhau |
| **Stabile** (strong defensive guard) | Full Guard (§4) — all dice to defense | Same, renamed |
| **Pulsativa** (committed attack) | High offense split (70%+ to offense) | Same, labeled |
| **Instabile** (provocative, baiting) | Feint (PP-294) — sacrifice defense for next-round advantage | Same — Feint IS the provocation |
| **Zufechten/Krieg** (approach/close) | Establish Distance (§4) + zone rules (§5) | Same |
| **Stamina/conditioning** | Stamina = End × 5; Take a Breath; OOB -2D | E7 adds yield-at-0 for duels |
| **Taunt/provocation** | NOT in canonical combat | **NEW: Taunt action (Cognition vs Composure)** |

### Pirates! → historical → canonical — what survived

| Element | Pirates! (v1) | Historical (v3b) | Canonical (v4) | Status |
|---|---|---|---|---|
| Visible stance commit | 3 guards | 3 classifications | Pool-split IS the stance; UI labels it | ✓ — label layer |
| Imposed triangle | Not in Pirates! | Hardcoded in v3b | **Removed** — emergence only | ✓ — correct |
| Read-and-counter | Position-based | Vor/Nach | Initiative §3 | ✓ — already canonical |
| Feint/deception | Not modeled | Meisterhau (imposed) | PP-294 Feint (canonical) | ✓ — already canonical |
| Stamina → yield | Misattributed | Sekiro (E7) | Stamina + PP-634 Yield | ✓ — E7 |
| Taunt/provocation | Not in Pirates! | Not in v3b | **NEW action** (needs rebalancing) | ⚠ — WIP |

---

## 5. Remaining Issues

### P1 (blockers before ratification)
1. **Taunt is broken-strong** (92% win rate). Must rebalance before shipping. See §2.3 fix candidates.

### P2 (balance concerns)
2. **End dominance at all ratios.** End 5v4 = 91.6%. Canonical formula issue. Jordan decision: accept, mitigate in C, or mitigate globally.
3. **Feint never optimal in 1v1.** PP-294's Defense=0 is too punishing. This is canonical and intentional (group combat tool). In duel context: is this acceptable, or should C modify Feint (e.g., Defense = floor(Pool × 0.25) instead of 0)?

### P3 (unmodeled)
4. **Weapon reach** — Long weapons should have approach-phase advantage per §5 (can strike at distance Short weapons can't). Not simulated.
5. **Arena Stunts** — max +5D from environmental narrative. Not modeled.
6. **§13.2 Reputation Cascade** — canonical, verified, not exercised in sim.
7. **Wager Obligation** — R5 C5.1, not modeled.
8. **Composure track** — referenced in FF stress conditions; how does it interact with Taunt?

### Design questions for Jordan
1. **Taunt rebalance:** which fix? (Cost increase / offense requirement / frequency cap / contested differently)
2. **End dominance:** accept as "the duel stat," mitigate in C only, or canonical rebalance?
3. **Feint in C:** accept PP-294 as-is, or modify Defense floor for duels?
4. **Stance labels:** use Fiore vocabulary (Pulsativa/Stabile/Instabile) as UI labels on pool splits, or translate to Valoria-native terms?

---

## 6. Version History

- **v1** — Pirates! flat stances. Aggressive dominant, defense unrewarded. Committed 3b1c497.
- **v2** — Fiore triangle imposed. Meisterhau too strong, Agi dominant.
- **v3** — Overnerfed Meisterhau. Stabile dominant.
- **v3b** — Triangle balanced at 72–77%. But top-down: hardcoded outcome matrix, not emergent. Committed 306a391.
- **v4** — Scene combat chassis. No imposed triangle. Bottom-up emergence. Finds: no natural RPS; stamina management is THE duel strategy; Taunt needs rebalancing; End dominance is canonical. This version.
