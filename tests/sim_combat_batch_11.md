# VALORIA SIMULATION — COMBAT & MASS COMBAT STRESS TESTS
## Batch 11 | Mode C (Scenario) + Mode D (Edge Cases)
## Mechanics targeted: §8.1–8.5 personal combat, mass combat, siege, supply, scale transitions (§11)
## Threadweaving excluded per session directive.
## TN7 unless otherwise noted. Mass combat TN5.

---

# PART I — PERSONAL COMBAT EDGE CASES

---

## TEST C-B11-01: THE FIBONACCI WALL
**Setup:** Eight attackers vs. one defender (Agility 4, no weapon drawn, no armour).
**Mode:** TTRPG | **Temporal:** PRES | **Tracks:** none | **Archetype:** generic combatants

### State: Round 1 — Declaration Phase
```
Defender — Coord [4], End [4], Health [10/10], Wounds [0]
  Pool: Combat History = 5D (Agility 4 + Hist 1 baseline)
  Conditions: surrounded

8 Attackers (generic) — Combat pool 4D each
  Fibonacci bonus (8+ vs 1): +5D each → effective pool 9D each
```

**Resolution: Fibonacci bonus application**

Pool: 9D (each attacker), TN7, Ob = defender net successes

Expected net per attacker at 9D TN7: 9 × 0.33 = **2.97 net**

Defence pool (5D) must split across 8 attackers simultaneously. Defender must declare split before Offence pools are revealed (§8.1 group defence rule).

Optimal defender allocation: 1D to each of 6 attackers, 2D to 2 attackers (or any 5+0+0 split — any allocation is brutal).

**1D defence vs 9D offence:**
- Attacker: E(net) = 2.97; Defender: E(net) = 0.33
- Excess successes = 2.97 − 0.33 = **2.64**
- Damage = Power (3) + weapon (+1, assuming medium) + 2.64 excess − armour (0) = **6.64 expected per hit**

**2D defence vs 9D offence:**
- Defender: E(net) = 0.66; Excess = 2.31
- Damage ≈ 5.31

**8 simultaneous hits, expected damage total (1D defence on 6, 2D on 2):**
- 6 hits × 6.64 = 39.84 damage
- 2 hits × 5.31 = 10.62
- Total: **~50.5 expected damage in one round**

**Single-hit cap analysis (§3.8):**
- Each hit can inflict at most 2 Wounds
- 8 simultaneous hits = potential 16 Wounds attempted
- §3.8: cap is per-hit, not per-round — 8 × 2 = max 16 Wounds possible in one round
- Defender incapacitated at 2 Wounds (Endurance 4 → threshold 3 Wounds per §3.8 table)

### State Delta
Health 10 → 0 → reset → 0 → reset → 0 [incapacitated after 3 Wounds]
In practice: first hit likely delivers 2 Wounds. Second hit: already incapacitated.

### Findings

#### EDGE CASE [Crunch Cascade]: Defence split declaration timing
**Setup:** Defender must declare 1D-per-attacker split simultaneously with offence pool reveal. 8 attackers = 8 allocations to track simultaneously.
**Mechanism:** §8.1 says allocation "cannot be changed after Offence pools are revealed." With 8 attackers revealing simultaneously, there is no moment between reveal and lock — defender is splitting blindly regardless of the rule's intent.
**Severity:** P2 — produces confused table play, not game-breaking
**Frequency:** Rare (8v1 is unusual) but possible in any ambush scenario
**Proposed fix:** Clarify that defender allocates before any offence is revealed (blind), not "simultaneously." The rule already implies this but the word "simultaneously" creates apparent contradiction.

#### EDGE CASE [Degenerate]: Fibonacci cap at 8+
**Setup:** What happens at 13 attackers vs 1?
**Mechanism:** Table caps at 8+ → +5D. A 13th attacker adds no additional bonus. The system is correctly capped — this is a design confirmation, not a bug.
**Severity:** P3 (minor) — players may expect continued scaling
**Proposed fix:** None needed mechanically. Suggest a sidebar noting "the table caps at 8+ because beyond that point, the bottleneck is the defender's incapacitation, not attack probability."

#### EDGE CASE [Incoherence]: Single-hit cap in pile-on
**Setup:** 8 hits simultaneously, each capped at 2 Wounds. Defender has Endurance 4 (incapacitates at 3 Wounds).
**Mechanism:** First hit delivers 2 Wounds. Second hit: defender is at 2 Wounds, not yet incapacitated (threshold = 3). Second hit delivers up to 2 more. Defender now at 4 Wounds — incapacitated after 3rd Wound. Hits 3–8 resolve against an incapacitated character.
**Rules question:** Do hits 3–8 still roll? Can you Coup de Grâce an already-incapacitated character while 5 more attacks are incoming this priority?
**Severity:** P2 — no ruling for "attacks against incapacitated mid-pile-on"
**Proposed fix:** Add: "Once a character is incapacitated, subsequent attacks in the same priority resolve as uncontested Coup de Grâce at GM discretion. Roll is not required — the GM determines narrative outcome."

---

## TEST C-B11-02: THE DUEL OF MISMATCHED WEAPONS (REACH HELL)
**Setup:** Character A — 7 Agility, Light weapon (dagger, Fast speed). Character B — 1 Agility, Heavy weapon (halberd, Slow speed, Reach 5–10').
**Mode:** TTRPG | **Temporal:** PRES | **Archetype:** two generic combatants

### State: Round 1 — Declaration
```
Char A (Dagger) — Agi [7], Combat pool 8D, Light weapon (Reach: Adjacent, Speed: Fast)
Char B (Halberd) — Agi [1], Combat pool 5D, Heavy weapon (Reach: 5–10', Speed: Slow, Reach priority advantage)
```

**Initiative:**
- A: 7D TN7, E(net) ≈ 2.31
- B: 1D TN7, E(net) ≈ 0.33
- A wins decisively. A **declares last** (hears B's plan first).

**Priority analysis:**

*Assuming both start at standard combat distance (5–10' — halberd range):*

At this range, B has reach priority. **B attacks at Priority 3 before A can close** (§8.1 reach priority rule: longer weapon gets one priority attack before shorter reaches).

- B attacks: 5D TN7, Ob = A's defence net
- A defends (Dodge Backwards): 7D − armour penalty (0) = 7D, E(net) = 2.31
- B's attack: E(net) = 1.65; Excess = max(0, 1.65 − 2.31) = 0 expected excess
- P(B excess > 0) ≈ 35% (B occasionally wins)

*If B misses (65% of the time): A closes to adjacent range.*

At adjacent range, weapon **speed** determines order: Fast (A) before Slow (B).
- A now attacks first at standard Priority 3.
- B attacks second at Priority 3 but is at a speed disadvantage.

**Round 2+ (A successfully closed):**
- A attacks: 8D TN7, E(net) = 2.64
- B defends (1D Agility): E(net) = 0.33
- Excess ≈ 2.31; Damage = Power(3) + 0 (light) + 2.31 = **5.31**
- B Health = Endurance + 6 = 7 (Endurance 1). 5.31 damage → B reaches 0 on first hit reliably.

### State Delta (expected)
Round 1: 65% chance A closes, 35% chance B lands priority hit.
Round 2 (if A closed): A incapacitates B with high probability.

### Findings

#### EDGE CASE [Boundary]: Reach priority + initiative interaction
**Setup:** B has reach priority (longer weapon) but loses initiative (A declares last).
**Mechanism:** A, declaring last, hears that B will attack with the halberd. A can then declare: **Withdraw** at Priority 5 (sacrifice offence, re-establish reach advantage). But Withdraw is Priority 5 — after B's Priority 3 attack with reach priority. A cannot prevent B's reach priority attack even with full tactical awareness.
**Severity:** P3 — functions as designed. Reach priority is meaningful.
**Proposed fix:** None. Confirm: initiative advantage does not negate reach priority. This is correct.

#### EDGE CASE [Boundary]: Closing distance — what triggers "same range"?
**Setup:** §8.1 says "once both are at the same range, weapon speed determines order." But range has three states (Adjacent / 5' / 5–10') and two ranges for reach (Adjacent and 5–10' for heavy weapons).
**Mechanism:** When A closes from 5–10' to Adjacent: they are now at Adjacent range. B's halberd wants 5–10'. Are they "at the same range"? They are at A's optimal range, not B's.
**Severity:** P2 — ambiguity. The rule implies "same range" means both within their weapon's optimal range. Halberd at adjacent range is sub-optimal for B.
**Proposed fix:** Add: "When a shorter weapon closes to adjacent range against a longer weapon, the shorter weapon fights at its optimal range. The longer weapon is now at a disadvantage — it applies no damage bonus and loses reach priority for as long as both remain adjacent."

#### EDGE CASE [Degenerate]: Agility 1 defender
**Setup:** B defends with 1D (Agility 1, no armour). Against any pool of 6D+, B auto-fails defence with near-certainty.
**Expected A damage on B:** Power(3) + weapon(0) + excess(≈2.3) = 5.3 per round. B Health = 7. A kills B in ≤2 rounds regardless of B's attack success.
**Severity:** P3 — degenerate but expected. High-skill combatant destroys unskilled quickly.
**Note:** Confirms system works — skill dominates equipment as intended.

---

## TEST C-B11-03: STUNT EXPLOIT — CRITICAL WINDOW MANIPULATION
**Setup:** Player declares a Stunt with critical success range 1–10 (full range of a d10), meaning critical failure range also expands to 1–10.
**Mode:** TTRPG | **Archetype:** any

### Mechanic analysis:
§8.1 Stunts: "Player sets their own critical success range (up to 11–20); the critical failure range expands by the same amount."

**Key phrase: "up to 11–20."** The scale runs 11–20, meaning:
- Default: no stunt declared (range 0, no crit success or failure)
- Stunt (1): crit success on 20, crit failure on 1
- Stunt (2): crit success on 19–20, crit failure on 1–2
- Stunt (10): crit success on 11–20, crit failure on 1–10
- **Stunt (11+):** impossible — "up to 11–20" caps it.

### Edge case test: Maximum stunt (range 10, i.e., 11–20)
On any d10: P(crit success) = 10/20 = 50%; P(crit failure) = 10/20 = 50%; P(normal partial) = 0%.

**Expected outcome at max stunt:**
- Every die result is either a crit success or a crit failure. No partials.
- A pool of 8D TN7 with stunt 10 active: each die is independently either crit or crit-fail.
- This effectively reduces every roll to a binary gamble with a 50/50 split.

### Finding

#### EDGE CASE [Degenerate]: Max stunt eliminates normal resolution
**Setup:** Player declares max stunt range (11–20) on every roll, every round.
**Mechanism:** With no partial zone, every roll outcome is extreme. A player who consistently max-stunts will either dominate spectacularly or catastrophically. Over time, EV of max-stunt vs. no-stunt is equal in terms of success probability — but the variance is maximised.
**Severity:** P2 — not a rules break (the player is accepting equal failure risk), but it produces incoherent narrative rhythm. A character who always swings wildly makes targeted gameplay feel random.
**Proposed fix:** None mechanically required. Clarify: "The GM may limit Stunt declarations to once per scene or require narrative justification for each stunt." Alternatively, add a fatigue cost: each consecutive Stunt-heavy round adds +1 Ob to the next roll (overextension).

#### EDGE CASE [Ambiguity]: Stunt range and dice chain (10s)
**Setup:** A die shows 10 (normally triggers chain roll). In a max-stunt setup, 10 is in the crit success range. Does it also chain?
**Mechanism:** §1 (dice engine) says 10s chain. Crit success is a narrative condition, not a dice replacement. These operate on different layers.
**Ruling needed:** Does a 10 in a crit-success range BOTH chain and crit? Or does crit supersede?
**Severity:** P2 — actual interaction undefined.
**Proposed fix:** Add: "A die showing 10 within the critical success range chains as normal AND counts as a critical success. The chain die result is added to the pool total before the critical determination is applied to the action's narrative outcome."

---

## TEST C-B11-04: THE ESCAPE PARADOX
**Setup:** Character attempts to escape combat while simultaneously being the target of a Rescue manoeuvre from an ally and a Tie Up from an enemy.
**Mode:** TTRPG | **Temporal:** PRES | **Archetype:** generic

### Priority sequence:
- Priority 3A: Manoeuvres resolve first. Tie Up vs Rescue both fire here.
- Priority 5: "The Escape" (full-round action, §5 — the Thread operation). Wait — Escaping Combat is an Agility check, not specified at which Priority.

### Rules reading:
§8.1 Escape: "Declare intent at Phase 1." No priority number given.
The character declared escape. Tie Up fires at Priority 3A. Rescue fires at Priority 3A.

**Sequence:**
1. Tie Up (Priority 3A) resolves first. Tie Up vs opponent's Power.
   - If Tie Up succeeds: weapons locked, no damage either party this round.
   - Can you escape while tied up? §8.1 Tie Up effect: "Lock weapons; no damage to either this round." It says nothing about preventing escape.
2. Rescue (Priority 3A, same priority as Tie Up): Redirect attack from ally to self. But the escaping character isn't being attacked this round — they're trying to leave.
   - Does Rescue apply to the Escape attempt itself? Rescue says it redirects "melee / Priority 4+ attacks." Escape is not an attack.

### Finding

#### EDGE CASE [Ambiguity]: Escape during Tie Up
**Setup:** Enemy locks weapons via Tie Up at Priority 3A. Escaping character declared escape at Phase 1.
**Mechanism:** Tie Up succeeds. Both characters are weapon-locked. Escaping character still wants to flee. Escape requires Agility check. Does the Tie Up prevent the Agility check?
**Severity:** P2 — Tie Up description is silent on immobilisation vs. escape.
**Proposed fix:** Add: "A character who succeeds at Tie Up against an escaping target forces the escape to fail automatically this round. The escaping character re-declares at Phase 1 of the next round. A Tie Up does not physically restrain — on the following round, the escaping character may escape without the weapon-lock penalty since weapons are no longer the binding factor."

#### EDGE CASE [Ambiguity]: Rescue scope vs. non-attack declared actions
**Setup:** Ally declares Rescue to protect the escaping character. But escape is not an attack — Rescue redirects attacks.
**Mechanism:** Rescue cannot logically redirect an escape attempt. The ally has burned their Priority 3A action on a Rescue that has no valid target this round.
**Severity:** P2 — wasted action from rules gap.
**Proposed fix:** Add: "Rescue only applies when the ally is the target of an attack. If declared against a non-attacking action, the Rescue fails automatically and the ally loses their offensive action for this round."

---

## TEST C-B11-05: WOUND ACCUMULATION + OB STACKING CLIFF
**Setup:** Character with Endurance 5 (incapacitates at 3 Wounds) takes Wounds progressively. Track Ob accumulation.
**Mode:** TTRPG | **Temporal:** PRES | **Archetype:** any

### Ob stacking analysis:
| Wounds | Ob added | Total Ob penalty | Notes |
|--------|----------|-----------------|-------|
| 0 | +0 | +0 | Baseline |
| 1 | +1 | +1 | All rolls at +1 Ob |
| 2 | +1 | +2 | Combat pool at +2 Ob — 8D pool now needs 3+ net just to match prior 1+ net expectation |
| 3 | +1 | +3 | Incapacitated threshold (End 4–5). Character reaches incapacitation and is still rolling at +3 Ob? |

**Question:** Does a character at exactly 3 Wounds (incapacitated threshold for Endurance 4–5) still act, or are they immediately incapacitated?

§3.8: "An incapacitated character is unconscious or otherwise unable to act." But the 3-Wound threshold triggers incapacitation. The 3rd Wound itself applies +1 Ob before incapacitation is checked? Or does incapacitation occur at the moment of the 3rd Wound?

### Finding

#### EDGE CASE [Ambiguity]: Incapacitation timing — does the 3rd Wound act first?
**Setup:** End 4–5 character. 2 Wounds + 2 Ob penalty active. Takes damage sufficient for 3rd Wound.
**Mechanism:** Wound 3 threshold = incapacitation. Does the character get to complete their declared action this round at +3 Ob, then fall, or do they fall immediately on taking the 3rd Wound?
**Severity:** P2 — determines whether a character can resolve their "dying action."
**Proposed fix:** Add: "A character who reaches their incapacitation Wound threshold mid-round completes any currently-resolving action at +1 Ob for the new Wound, then falls incapacitated at the end of that priority step. Declared but not-yet-resolved actions are cancelled."

#### EDGE CASE [Boundary]: Ob stacking cap (10) vs. Wounds
**Setup:** §1 says "Ob stacking caps at Ob 10." At 3 Wounds (Ob +3), base Ob 1 combat roll = Ob 4. Approaching cap requires 7+ simultaneous Ob sources.
**Mechanism:** Can Wounds + terrain + wounds + zone conditions + scale all stack to reach Ob 10?
- 3 Wounds = +3 Ob
- Heavy terrain = +1 Ob
- Night/fog = +1 Ob
- Mass combat scale = not applicable at personal scale
- Thread-adjacent zone = GM +1 Ob (possible)
- That's Ob 6 on a base Ob 1 action = Ob 7. Still below cap but reachable.
- At Ob 10: character essentially cannot succeed on any action (needs 10+ net successes, impossible with reduced pools).
**Severity:** P3 — extreme corner case. System handles it correctly via cap.
**Proposed fix:** None. Confirm: Ob cap at 10 prevents infinite penalty stacking.

---

# PART II — MASS COMBAT EDGE CASES

---

## TEST C-B11-06: TRIPLE BRUTAL — ALL THREE SIDES OFFENSIVE BRUTAL
**Setup:** Three-way mass combat. All three factions independently declare Offensive Brutal simultaneously.
**Mode:** TTRPG | **Temporal:** PRES | **Tracks:** TT | **Factions:** Crown, Revolution, Löwenritter

### State: Round 1
```
Crown Unit — Martial 4, End 4, Cohesion 4, Health 10, Disposition: Offensive Brutal
  Commander: Ehrenwall (Agi 5, Spi 4, Mem 3)
  Attack pool: 4 (Martial) + 5 (Ehrenwall Agi) = 9D

Revolution Unit — Martial 3, End 3, Cohesion 4, Health 9, Disposition: Offensive Brutal
  Commander: generic (Agi 3, Spi 3, Mem 2)
  Attack pool: 3 + 3 = 6D

Löwenritter Unit — Martial 5, End 5, Cohesion 6, Health 11, Disposition: Offensive Brutal
  Commander: Ehrenwall (assume separate contingent, Agi 5)
  NOTE: Löwenritter vs. Crown is an anomaly — flag editorial.

Tracks: TT 45
```

**[EDITORIAL: Three-way Löwenritter vs. Crown engagement requires user confirmation of political context.]**

### Disposition table resolution (§8.3):
Each pair attacks simultaneously. Three attacking pairs: Crown→Revolution, Revolution→Löwenritter, Löwenritter→Crown (or some configuration).

Per table, Brutal attacker vs. Brutal defender: **Ob 1, +3D, +4 flat damage on success.**

**Crown attacks Revolution (Brutal vs Brutal):**
- Pool: 9D + 3D = 12D, Ob 1, TN5 (mass combat), +4 damage on success
- At TN5: P(die ≥ 5) = 0.6; Expected net per die ≈ 0.5 (TN5 is considerably more forgiving)
- 12D TN5: E(net) ≈ 6.0; Ob 1: easily exceeded
- P(success) ≈ 99%+
- Damage: E(net) − Ob + base power (units don't have explicit Power — §8.3 only lists "damage reduces Health")

**CRITICAL GAP FOUND:**

§8.3 disposition table lists "+2 flat damage" for Brutal on any success, "+4 flat damage" for Brutal vs Brutal. But §8.3 does not define what the BASE damage is for a mass combat hit. Personal combat uses Power + weapon bonus + excess successes. Mass combat has no Power equivalent and no base damage number.

**Where does the flat damage add onto?** The table says "+2D +2 dmg" for Balanced vs Brutal, "+3D +4 dmg" for Brutal vs Brutal. This implies the modifier adds to some base — but that base is never stated.

### Findings

#### EDGE CASE [Incoherence / P1]: Mass combat base damage undefined
**Setup:** Any mass combat engagement.
**Mechanism:** §8.3 disposition table lists damage modifiers (+2 flat, +4 flat) but the base damage of a successful mass combat attack is never stated. Is base damage 1 per net success (like personal combat)? Is it a flat 1? Is it Martial ÷ 2?
**Severity:** P1 — the core mass combat resolution loop is incomplete without a base damage number.
**Frequency:** Every mass combat engagement.
**Proposed fix:** Add explicit base damage rule to §8.3. Recommendation: "A successful mass combat attack deals damage equal to net successes over Ob. Flat damage bonuses from disposition add to this total. On Partial (exactly Ob met), deal 1 damage." This mirrors personal combat logic and makes the disposition modifiers coherent.

#### EDGE CASE [Cascade]: Triple Brutal in three-way — all three sides attack simultaneously
**Setup:** All three sides attack simultaneously (§8.3: "all attacks resolve simultaneously").
**Mechanism:** If all three sides deal comparable damage:
- Round 1: All three units take ~3–5 damage (with undefined base, using net successes only)
- None break formation (Health 9–11, losing 3–5 on turn 1)
- Round 2: Same. TT meanwhile climbing.
- Round 3–4: Multiple Formation Breaks likely occurring simultaneously.

**Formation Break cascade (§8.3):** Health hits 0 → reset, +1 Ob. Cohesion check Ob 2. Failure = Routes.
- Crown (Cohesion 4): 4D vs Ob 2, P(success) ≈ 87%
- Revolution (Cohesion 4): same ≈ 87%
- Löwenritter (Cohesion 6): 6D vs Ob 2, P(success) ≈ 97%

**If two units route simultaneously in a three-way:**
- The third (Löwenritter) is now in a battle with no valid opponents.
- §8.3 three-way procedure: "apply disposition table for each attacking pair independently." With two pairs gone, the remaining pair dissolves.
- Does the surviving unit get full season accounting credit for "winning"? Rules silent.
**Severity:** P2 — no ruling on three-way conclusion when 2/3 parties route simultaneously.
**Proposed fix:** Add: "If two or more parties route in the same round of a three-way mass combat, the surviving party wins the engagement outright. They receive veteran bonus as if they had inflicted the routing."

#### EDGE CASE [Boundary]: Brutal disposition requirements check
**Brutal requires Cohesion 4+** (§8.3 formation constraints).
- Revolution unit: Cohesion 4. Exactly at threshold. ✓ Legal.
- **TC interaction:** If TC ≥ 70 and Church observes Brutal against civilians, TC +1 automatic.
- In this military engagement (not civilian), TC trigger does not fire. ✓

---

## TEST C-B11-07: THE IMPOSSIBLE RALLY — ROUTING UNIT RALLIED WHILE COMMANDER IS ENGAGED IN PERSONAL DUEL
**Setup:** A unit Routes. Its commander is currently engaged in a personal duel (Priority 8 personal action from prior mass combat round). Can the commander Rally the unit and continue the duel?
**Mode:** TTRPG | **Temporal:** PRES → CROSS | **Archetype:** Faction Leader + Löwenritter Knight

### State: Round 2 post-Formation-Break
```
Routing Unit (Revolution Light Infantry) — Health 9/9 (reset after break), +1 Ob all actions, Routed
  Cannot take ordered actions.

Commander (generic, Agi 4, Spi 3) — engaged in personal duel with Crown officer
  Priority 8 action: ongoing personal duel exchange 2/unlimited
```

**Rally mechanics (§8.3):** Requires officer with Agility 4+ to spend their action. Spirit roll, Ob 2.

**Question:** The commander is mid-duel at Priority 8. Is a Priority 8 personal action considered "spending their action"? Does the commander have a mass combat action available while using their Priority 8 personal action?

**Scale transitions (§11.3):** Mass → Personal handoff: "Any character may take a Personal Action at Priority 8. Limit: one exchange per mass combat round."

**The rule only specifies limit on personal actions, not on mass combat actions while personal is active.**

### Finding

#### EDGE CASE [Ambiguity]: Commander spending mass combat action while in personal duel
**Setup:** Commander is at Priority 8 personal duel. Routed unit needs Rally (commander spends action, Spirit roll).
**Mechanism:** §11.3 limits personal actions to "one exchange per mass combat round." Rally is not a personal action — it's a mass combat command. But the commander is physically in a duel. Do they have a free mass combat command action while fighting?
**Severity:** P2 — creates unrealistic situation (shouting a rally command while locked in a sword fight is narratively awkward, mechanically permitted).
**Proposed fix:** Add to §11.3: "A commander engaged in a Priority 8 personal action cannot spend their mass combat action in the same round. Choose: personal exchange OR mass combat command."

#### EDGE CASE [Cascade]: Routed unit + commander's Contested Figure
**Setup:** Commander's duel opponent is rendered non-threatening (e.g., Disarmed). Per §8.3, they become a Contested Figure resolving after the round. Meanwhile the routed unit takes no ordered actions. Next round: commander can Rally, but the Contested Figure scene must first resolve.
**Mechanism:** Contested Figure scene adds a social/personal scene between mass combat rounds. During that scene, the unit remains Routed and may flee further (no ordered actions = possible narrative escalation).
**Severity:** P2 — no rule on whether Routed units drift during Contested Figure resolution.
**Proposed fix:** Add: "Routed units hold position (do not further disperse) during Contested Figure or personal-scale scene resolution between mass combat rounds unless explicitly narrated otherwise by GM."

---

## TEST C-B11-08: THE UNIT THAT WILL NOT DIE — RALLY LOOP
**Setup:** A unit with Cohesion 6 Formation Breaks, rallies, Formation Breaks again in the same battle, three times in succession.
**Mode:** TTRPG + BG | **Temporal:** PRES | **Archetype:** Faction Leader (commander)

### State tracking:

**Round 4 — First Formation Break:**
```
Knights Templar (Church) — Martial 5, End 5, Cohesion 6, Health 11 → 0 (reset to 11)
  +1 Ob all actions after break
  Cohesion check: 6D, Ob 2, TN5, P(success) ≈ 97%
  Result: Holds (does not Route)
```

**Round 6 — Second Formation Break:**
```
Health → 0 again. Reset to 11. +1 Ob (now stacking? or same penalty?)
  Ob accumulation: §8.3 says "all subsequent actions at +1 Ob" per break.
  Two Formation Breaks = +2 Ob cumulative? Rules say "+1 Ob" without clarifying whether it stacks.
  Cohesion check now: 6D, Ob 2 + Ob modifier?
```

**Gap:** §8.3 Formation Break says "+1 Ob" but doesn't clarify whether multiple Formation Breaks in one battle stack or overwrite.

**Round 8 — Third Formation Break:**
```
If stacking: +3 Ob all actions. Cohesion check: 6D, Ob 2+3 = Ob 5.
  6D TN5, Ob 5: E(net) ≈ 3.0. P(≥5 net) ≈ 15%. High route probability.
If non-stacking (overwrite): +1 Ob. Cohesion: 6D Ob 2. P(≥2 net) ≈ 97%. Rarely routes.
```

**Rally mechanics per break:**
Each rally requires: commander Agi 4+, Spirit roll Ob 2, commander spends their action.
Three rallies = commander spends three mass combat actions total (one per break round).
In a battle with only one commander, that commander contributed nothing offensive in rally rounds.

### Findings

#### EDGE CASE [Ambiguity / P1]: Formation Break Ob stacking not specified
**Setup:** Any unit that Formation Breaks multiple times.
**Mechanism:** The Ob penalty is stated as "+1 Ob" without a stacking rule. Two valid interpretations:
1. **Stacks:** Second break = +2 Ob. A unit can functionally be ground down to uselessness.
2. **Overwrites:** Always +1 Ob regardless of break count. Knights Templar become unkillable tanks who Formation Break indefinitely.
**Severity:** P1 — mass combat attrition is entirely different between these two readings.
**Proposed fix:** Specify: "Formation Break Ob penalties stack. Each break adds +1 Ob (cumulative) to all unit rolls for the remainder of the battle. A rallied unit retains accumulated Ob penalties — rally only removes Routed status, not Ob penalties."

#### EDGE CASE [Optimal Play]: Knights Templar rally abuse
**Setup:** KT have +1D Cohesion vs Thread events and immunity to Brutal morale effects. With high Cohesion (6) and a dedicated rally commander, they can Formation Break and rally repeatedly with high success probability.
**Mechanism:** If Formation Break Ob does NOT stack: KT are functionally immortal in battle — they can Form Break and rally indefinitely as long as their commander is alive and can pass Spirit Ob 2.
**Severity:** P2 — not a rules break but a dominant strategy. Any Crown/Church player with KT + high-Agility commander has an unkillable frontline unit.
**Proposed fix:** Enforce stacking Ob per fix above. Additionally: "A unit that has Formation Broken 3+ times in one battle cannot be Rallied again this engagement — they are too shattered to reform."

---

## TEST C-B11-09: SCALE TRANSITION NIGHTMARE — PERSONAL DUEL INSIDE A MASS COMBAT INSIDE A SIEGE
**Setup:** Three simultaneous scales: ongoing siege (§8.4), active mass combat assault (§8.3), and a personal duel between Ehrenwall (defending) and a named Varfell officer (attacking) at Priority 8.
**Mode:** Hybrid (TTRPG personal + BG siege outer layer) | **Temporal:** PRES+CROSS | **Factions:** Crown, Varfell | **NPCs:** Ehrenwall | **Archetype:** Faction Leader, Löwenritter Knight

### State: Siege Season 3, Assault Phase Round 5
```
SIEGE SCALE:
  Fortification: 2 (down from 3 — Sappers succeeded Season 1)
  Crown garrison Health: reduced (not defined — siege has no garrison health stat)
  Varfell attacking force: Military 5, conducting Assault action

MASS COMBAT SCALE:
  Crown Heavy Infantry unit — Martial 4, End 4, Coh 4, Health 10, Disposition: Defensive
  Varfell Heavy Infantry unit — Martial 5, End 4, Coh 4, Health 10, Disposition: Offensive
  Round 5 resolution active.

PERSONAL SCALE:
  Ehrenwall — Agi 5, Spi 4, Combat pool 9D (Löwenritter Knight archetype)
  Varfell Officer (Vaynard's agent) — Agi 4, Combat pool 7D
  Priority 8 — personal duel exchange 1
```

### Three-scale interaction analysis:

**Scale 1 (Siege):** Assault action resolves seasonally (§8.4). The current mass combat IS the assault resolution — "Success: breach attempt, mass combat at standard Ob." So the mass combat is embedded inside the siege action resolution.

**Scale 2 (Mass combat):** Currently active. Priority table applies. Ehrenwall is commanding Crown unit (Commander contribution: +5D attack) but is also in personal duel at Priority 8.

**§11.3 Handoff conflict:** If Ehrenwall is in a Priority 8 personal duel, does his Commander Contribution (Agi dice to unit attacks) still apply?

Rules say Commander Contribution adds dice to unit rolls. No rule specifies the commander must be exclusively commanding (not personally fighting) to contribute dice.

**Scale 3 (Personal at Priority 8):** Duel resolves. Ehrenwall wins decisively (9D vs 7D, expected).

**Domain Echo potential:** If Ehrenwall incapacitates the Varfell officer mid-battle, does this produce a Domain Echo? The Varfell officer's incapacitation is a personal outcome. The Varfell unit's morale might be affected — but no mechanic directly links named NPC incapacitation to unit Cohesion in §8.3.

**Siege conclusion interaction:** If the mass combat assault ends (Varfell wins or loses), the siege action for this season resolves. §8.4: "Success: breach attempt, mass combat at standard Ob. Overwhelming: walls breached." The mass combat IS the breach attempt. If Varfell's unit wins the mass combat (Crown unit Routes), Fortification drops again? Or does breach = success of the assault Domain Action?

### Findings

#### EDGE CASE [Ambiguity]: Commander in personal duel still contributing dice
**Setup:** Ehrenwall in personal duel at Priority 8. His unit attacks at Priority 3 with his Agility contribution.
**Mechanism:** No rule withdraws commander contribution during personal combat. Mechanically, Ehrenwall is simultaneously contributing to a mass combat roll AND personally fighting.
**Severity:** P2 — simulationally odd (a man in a duel is also directing unit tactics).
**Proposed fix:** Add: "A commander engaged in a Priority 8 personal action continues to contribute their dice to unit rolls in the same round — they have already issued orders in the Declaration Phase. However, their Memory-based conditional order is unavailable in any round they take a personal action."

#### EDGE CASE [Incoherence]: Siege assault result vs. mass combat result
**Setup:** Assault (Domain Action, seasonal) generates a mass combat. Who determines whether the seasonal assault "succeeded"?
**Mechanism:** §8.4 Assault: "Success: breach attempt, mass combat at standard Ob." This implies the seasonal roll determines whether the mass combat happens at standard Ob. But then what determines whether the siege assault itself "succeeded" — the Domain Action roll or the mass combat outcome?
**Severity:** P1 — the siege procedure conflates the Domain Action roll with the mass combat outcome without specifying how mass combat results feed back into siege resolution.
**Proposed fix:** Clarify: "The Assault Domain Action roll determines whether a breach attempt occurs and at what Ob. The mass combat outcome (Crown/Varfell win/loss) determines whether the attacker achieves a Fortification −1 result: if the attacking unit wins (Crown unit Routes or destroyed), Fortification drops by 1. If the defending unit wins, Fortification holds."

#### EDGE CASE [Ambiguity]: Named NPC incapacitation and unit morale
**Setup:** Ehrenwall incapacitates the Varfell officer in personal duel. Does the Varfell unit react?
**Mechanism:** §8.3 personal actions in mass combat produce "Contested Figures" but no morale link. However, the death/incapacitation of a commander logically destroys unit coordination.
**Severity:** P2 — no mechanic links named NPC incapacitation to unit stat change.
**Proposed fix:** Add: "If the commanding officer is incapacitated or rendered a Contested Figure during a mass combat round, the unit immediately loses their Commander Contribution dice for the remainder of that battle (not just that round). The unit may designate a new commander (if available) at Priority 1 of the next round."

---

## TEST C-B11-10: SUPPLY LINE CUT DURING ACTIVE COMBAT
**Setup:** A unit's supply line is cut (Intelligence Domain Action by an enemy) during the same season as an active battle. Does the supply penalty apply immediately (this battle) or from next season's accounting?
**Mode:** BG + HYB | **Temporal:** PRES+FUT | **Tracks:** FSTAT | **Faction:** Hafenmark (attacking) vs. Guilds (defending)

### Mechanic analysis:
§8.5 Supply: "Supply status is checked at seasonal accounting for each unit."

"Checked at seasonal accounting" = the penalty applies at the start of the NEXT season's actions, not retroactively within the current season.

But: Domain Action for supply interdiction (§8.5) states: "Success: one enemy supply route blocked 1 season."

**Timing gap:** If the interdiction succeeds during the Strategic Phase of Season 3, and the battle occurs during the same season:
- Seasonal accounting for Season 3 hasn't happened yet.
- Supply check is at seasonal accounting (end of Season 3 / start of Season 4).
- The unit fights Season 3's battle at full supply.

This means supply interdiction has a 1-season delay before affecting combat. **Intentional? Probably.** But:

**Hybrid mode wrinkle:** In hybrid, the Strategic Phase (BG orders) and Personal Phase (TTRPG scenes) occur in the same season. If a PC performs supply interdiction as a TTRPG scene mid-season (Personal Phase), does it affect the Strategic Phase's mass combat?

§11.7 hybrid mode: "Strategic Phase uses board game orders; Personal Phase uses TTRPG Domain Echoes." No timing specified for which resolves first.

### Findings

#### EDGE CASE [Ambiguity]: Hybrid phase ordering within a season
**Setup:** Hybrid mode, Season 3. Personal Phase PC interdicts enemy supply (succeeds). Strategic Phase battle occurs same season. Does supply penalty apply to the battle?
**Mechanism:** No rule specifies whether Personal Phase or Strategic Phase resolves first within a season. If Personal Phase goes first, the interdiction might logically apply to the same-season battle. If Strategic Phase goes first, it doesn't.
**Severity:** P1 — the entire hybrid mode's internal season sequencing is unspecified.
**Proposed fix:** Add to §11.7: "Within each season, the resolution order is: (1) Strategic Phase (BG orders declared and resolved), (2) Personal Phase (TTRPG scenes). This means Personal Phase outcomes of Season N take effect from Season N+1 onward for faction-level consequences. Exception: Personal Phase social scenes that produce Domain Echoes apply immediately if the scene precedes the Strategic Phase (at GM's discretion for narrative coherence)."

#### EDGE CASE [Regression]: Supply interdiction used against self
**Setup:** A faction interdicts their own supply line (e.g., to deny an enemy occupying the route, or a traitor within the faction).
**Mechanism:** §8.5 interdiction: "Intelligence vs defender's Military ÷ 2." The "defender" is the faction controlling the supply route. If you interdict your own route, you are both attacker and defender. Who rolls? Do you roll against yourself?
**Severity:** P3 — exotic but conceivable (traitor scenario, scorched earth).
**Proposed fix:** Add: "A faction may voluntarily declare their own supply line cut (no roll required). This is a Domain Action consuming their Intelligence allocation for that season. Treat as Overwhelming success on interdiction."

---

## TEST C-B11-11: BOARD GAME MODE — DISPOSITION TABLE WITHOUT COMMANDER
**Setup:** Board game mode engagement between two faction units. Neither faction has assigned a commander this season (e.g., the commander was lost in a previous engagement and no replacement was appointed before the season's Strategic Phase).
**Mode:** BG | **Temporal:** PRES | **Factions:** Niflhel vs. Revolution | **Archetype:** Faction Leader (absent)

### Analysis:
§8.3 Commander Contribution: "The commanding officer's attributes directly modify unit rolls." Board game mode doesn't specify what happens to these dice when no commander is present.

No commander = Agility 0 (no bonus dice to attack), Spirit 0 (no bonus dice to Cohesion checks), Memory 0 (no conditional orders).

**Attack pool without commander:** Martial only. Niflhel Light Infantry: Martial 3 → attack pool = 3D, TN5, no modifier.

**Cohesion check without commander:** Cohesion dice only (no Spirit bonus). Cohesion 3 → 3D, Ob 2. P(≥2 net) at TN5 ≈ 74%.

This is mechanically functional. The gap is whether "no commander" is a valid game state in BG mode.

**[EDITORIAL: What is the standard rule for appointing commanders in BG mode? Is it mandatory per season?]**

### Finding

#### EDGE CASE [Deadlock]: Commander death with no replacement during a Season
**Setup:** Both factions' commanders are incapacitated in the same personal-scale scene before the seasonal battle resolves.
**Mechanism:** Both units fight with Martial only (no commander bonuses). If both have identical Martial, identical Cohesion, and fight symmetrically — who wins?
**Resolution:** Highest net successes wins. With symmetric pools, it reduces to pure variance. Average engagement length increases (lower damage output = more rounds). Not a deadlock — just slow and grim.
**Severity:** P3 — unpleasant but functional.
**Proposed fix:** None mechanically. Narrative suggestion: "Leaderless battles resolve as Brutal regardless of declared disposition (troops fight without coordination)." This is optional flavour.

---

## TEST C-B11-12: MODE CHANGE MID-SIEGE (TTRPG → BOARD GAME → HYBRID)
**Setup:** A siege begins in full TTRPG mode (multi-season procedure with scenes). Mid-siege, the group switches to board game mode (faction turns only). Then switches back to hybrid for the final assault.
**Mode:** TTRPG → BG → HYB | **Temporal:** CROSS | **Factions:** Crown (defending) vs. Varfell (attacking)

### State: Start of switch
```
TTRPG Phase (Seasons 1–2 complete):
  Fortification: 3 → 2 (Sappers succeeded Season 1)
  Garrison Endurance: 4 → 3 (Starve succeeded Season 2)
  Crown Stability: 7 → 5 (two Stability losses from siege)
  Varfell Military: 5 (unchanged)

Switch to BG mode for Season 3:
  BG mode siege: "Siege order vs. Fortification (single roll)" per §11.7
```

**BG siege resolution (Season 3):**
Varfell declares Assault. Roll Military (5D TN5) vs. Ob = Fortification (2) + 2 = Ob 4.
E(net) = 5 × 0.5 = 2.5. Ob 4: P(≥4 net) from 5D TN5 ≈ 31%.

If success: mass combat at standard Ob (§8.4) → in BG mode this is single-roll.
If failure: season wasted.

**State after BG Season 3 (expected: Assault fails ~69% of the time):**
Most likely outcome: Fortification stays at 2, season wasted.

**Switch to Hybrid (Season 4):**
§11.7: "Board game roll; TTRPG scenes for infiltration or breakout."

**Gap: The garrison Endurance loss from TTRPG Starve actions — does it carry into BG/Hybrid?**

§8.3: Starve → "Defender: −1 Endurance to garrison." This is a unit stat. In BG mode, unit stats are tracked on faction sheets. The TTRPG-derived Endurance loss should carry forward.

**But:** BG mode doesn't have a "garrison Endurance" stat — it has Fortification. The Starve effect reduces garrison Endurance, which affects the garrison unit's Health and Cohesion check thresholds. In BG mode (single-roll siege), there is no garrison unit with Health — just Fortification vs. Military.

### Findings

#### EDGE CASE [Incoherence]: Garrison unit stats vs. BG mode's stat-less siege
**Setup:** TTRPG siege reduces garrison Endurance (a unit stat). Mode switches to BG.
**Mechanism:** BG mode siege has no garrison unit — only Fortification (territory stat). The Endurance damage disappears when switching modes because BG has no stat to store it.
**Severity:** P1 — mode switching destroys accumulated attrition state.
**Proposed fix:** Add to §11.7 mode transition rules: "When switching from TTRPG siege to BG siege mid-campaign, convert accumulated garrison attrition: each point of garrison Endurance lost reduces Fortification by an additional 0.5 (round down). This bridges the stat systems across modes."

#### EDGE CASE [Incoherence]: Seasonal cap across mode boundaries
**Setup:** §11.5: "Faction attributes may not change by more than ±2 per season regardless of how many sources target them in either phase." A TTRPG Domain Echo reduces Crown Stability −1 in Season 3's Personal Phase. Then a BG Siege Starve action reduces Stability −1 more in Season 3's Strategic Phase.
**Mechanism:** Both are −1, total −2. At cap. A third source this season (e.g., a failed Rally that costs a province) cannot reduce Stability further.
**Severity:** P2 — seasonal cap functions correctly in principle. But who tracks cross-mode cap utilisation?
**Proposed fix:** Add explicit instruction: "The GM tracks the ±2 seasonal cap for each faction attribute on a summary sheet updated after both Strategic and Personal Phases each season. The cap is enforced at the moment of application — if a result would breach it, the excess is discarded."

#### EDGE CASE [Ambiguity]: TTRPG → BG → HYB continuity of Scene outcomes
**Setup:** In TTRPG Season 2, PCs completed a Negotiate scene with the besieged Crown commander. The commander agreed to surrender "if Varfell reaches the gates." Now in HYB Season 4, Varfell assaults. Does the negotiated condition still apply?
**Mechanism:** The agreed condition is a narrative outcome of a TTRPG scene. In HYB, the siege is resolving as a board game roll for its outer frame. No mechanic carries narrative agreements between modes.
**Severity:** P2 — narrative continuity is entirely GM-dependent.
**Proposed fix:** Add to §11 (or §8.4): "Formal agreements reached in TTRPG social scenes persist across mode changes. The GM records the condition as a Pending Agreement, which resolves the moment its trigger condition is mechanically satisfied in any mode."

---

## TEST C-B11-13: THE AMBUSH WITHIN A ROUTING UNIT
**Setup:** A Routed unit (cannot take ordered actions) is being ambushed by a pursuing enemy at the personal scale. Multiple pursuers (Priority 8 personal actions from several characters) attack fleeing soldiers.
**Mode:** TTRPG | **Temporal:** PRES | **Archetype:** Inquisitor (pursuing), generic routing soldiers

### Analysis:

§8.1 Ambush: Ob = ambusher's Tactics History + environment modifier (Ob 1–3). Routing soldiers are fleeing — does their status affect the Ambush Ob?

Routing soldiers cannot take "ordered actions." Is self-defense an ordered action? Probably not — individual self-defense is instinctive. But routing soldiers are not under command coordination.

§8.3 Routed: "Cannot take ordered actions." Personal combat is not an ordered action (it's personal scale). Routing soldiers can likely still defend themselves personally — they're just not fighting as a unit.

**[Interesting implication]:** A Routing unit's individual soldiers can still resist an ambush at personal scale (Priority 8), even though the unit itself cannot take ordered actions. This creates a scale split within the Routing unit.

**Ambush setup by Inquisitors (5 attackers vs. 2 routing soldiers):**
- Ambush Ob = Tactics History 3 (Inquisitor with History) + environment (forest, Ob 1) = Ob 4? No: Ob = ambusher's Tactics History plus environment modifier.
- Wait: the Tactics History is the pool, not a flat number. Re-reading: "Ob = ambusher's Tactics History + environment modifier (Ob 1–3)." This uses "History" as a quantity — likely the History point value.
- Inquisitor Tactics History 3 + environment Ob 1 = Ob 4. But the text says "Ob = ambusher's Tactics History + environment modifier" which is ambiguous — is the Tactics History an Ob modifier added to a base Ob? Or is the formula: Ob FOR DETECTION = Tactics History value + environment Ob?
- Most natural reading: the defender's Ob to detect the ambush = attacker's Tactics History points + environment modifier. So Ob 4 to detect.

**Defender detection:** highest-Cognition routing soldier. Cognition 3. 3D TN7, Ob 4: P(success) ≈ 15%. Very likely the ambush succeeds undetected.

On ambush success: "attackers get one free Priority 2 round and initiative." 5 attackers vs 2 defenders with Fibonacci bonus (5+ vs 1 = +3D each) and free ranged attacks at Priority 2.

### Finding

#### EDGE CASE [Incoherence]: Ambush formula — History as Ob source
**Setup:** §8.1 Ambush: "Ob = ambusher's Tactics History + environment modifier."
**Mechanism:** This formula uses a History value (a skill point number, 1–5) as an Ob component. All other Ob values in the system derive from defined sources (scale, attribute, track values). Using a History point count directly as Ob is inconsistent — it makes higher-skilled ambushers harder to detect, which is correct logically, but the formula mixes a skill metric with a difficulty number.
**Severity:** P2 — functional but inconsistent with how Ob is derived elsewhere.
**Proposed fix:** Clarify with example: "Ob for detection = ambusher's Tactics History level (1–5) + environment modifier (0–3), maximum Ob 7." Add example: "A skilled ambusher with Tactics History 4 in dense fog (modifier +2) creates an Ob 6 detection check."

---

## TEST C-B11-14: ARTILLERY UNIT — THE SINGLE-POINT-OF-FAILURE PROBLEM
**Setup:** An Artillery unit (Martial 2, Endurance 2, Cohesion 2, Health 8) serves as the primary siege bombardment asset.
**Mode:** BG + TTRPG | **Temporal:** PRES | **Factions:** Guilds (operating Artillery)

### Artillery stats analysis:
Artillery requires: Wealth Ob 4 + 1 season construction. Lowest stats of any unit type.

**Formation Break analysis:**
- Health = Endurance + 6 = 8. Lowest of any standard unit.
- Cohesion 2: fails Formation Break check (§8.3 requires Cohesion check Ob 2).
  - 2D TN5, Ob 2: E(net) ≈ 1.0. P(≥2 net) ≈ 37%.
  - Artillery routes ~63% of the time on first Formation Break.
- **Brutal formation constraint:** Requires Cohesion 4+. Artillery has Cohesion 2 — **cannot declare Brutal.** ✓
- **Defensive constraint:** Requires Cohesion 3+. Artillery has Cohesion 2 — **cannot declare Defensive.** 
- **Artillery's valid dispositions:** Balanced or Offensive only.

**Disposition table for Artillery (Cohesion 2, Martial 2):**
- Offensive: requires Martial 3+. Artillery has Martial 2. **Cannot declare Offensive.**
- **Artillery's only valid disposition:** Balanced.

Artillery is locked into Balanced disposition forever. It cannot declare Defensive, Offensive, or Brutal. No disposition flexibility.

**Bombard manoeuvre:** Artillery can declare Bombard. But there's no Bombard entry in the disposition interaction table. §8.3 Manoeuvres list: "Advance / Hold / Withdraw / Flank / Bombard." The Bombard manoeuvre exists but its mechanical effect is not defined in the disposition table.

### Findings

#### EDGE CASE [Incoherence / P1]: Bombard manoeuvre has no resolution mechanic
**Setup:** Artillery unit declares Bombard manoeuvre.
**Mechanism:** §8.3 lists Bombard as a manoeuvre option but the disposition interaction table only covers Advance/Hold/Withdraw/Flank. Bombard has no corresponding entry. There is no rule for what Bombard does.
**Severity:** P1 — Artillery's primary combat action has no defined mechanic.
**Frequency:** Every Artillery engagement.
**Proposed fix:** Add Bombard resolution to §8.3: "Bombard: the unit does not engage in standard melee exchange. Instead, roll Martial (no commander Agility bonus) vs. Ob = distance tier (0–3). Success: target unit takes flat 3 damage, ignoring disposition table. Overwhelming: flat 5 damage. Partial: flat 1 damage. Bombard unit is not subject to incoming melee attacks from the target unit this round (they are not in contact). Artillery cannot Bombard if in melee contact with any unit."

#### EDGE CASE [Degenerate]: Artillery unit is always Balanced — locked disposition
**Setup:** Martial 2 (cannot declare Offensive), Cohesion 2 (cannot declare Defensive or Brutal).
**Mechanism:** Artillery has exactly one valid disposition. Any enemy who declares Defensive against an Artillery Balanced attack faces: "Balanced attacker vs. Defensive defender: Ob 2, ±0." Attacker pool = 2D (Martial) + commander Agility. Against a Defensive unit with any reasonable Cohesion, Artillery rarely lands hits.
**Severity:** P2 — Artillery is extremely fragile and locked. This may be intentional (artillery is support, not frontline). But it means Artillery requires escort or it Routes on first contact.
**Proposed fix:** Flag for design review: "Is Artillery intended as a pure siege/support asset that routs immediately if engaged directly? If yes, add explicit note. If not, consider raising Cohesion to 3 (enabling Defensive) to allow Artillery to hold a position under escort."

---

## TEST C-B11-15: PARLEYS AND SOCIAL SCENES AT TT 80 / IP 75 (EXTREME TRACKS)
**Setup:** Mid-mass-combat parley attempt at extreme track values. TT 80, IP 75.
**Mode:** TTRPG | **Temporal:** PRES | **Tracks:** TT, IP | **NPCs:** Ehrenwall, Himlensendt

§8.3: "Social actions in mass combat: Parleys, surrenders, and ultimata use the standard social rules. Default disposition for an enemy commander approached mid-battle: Cool (Ob 3)."

**Prior ruling R-B10-04:** TC80+IP75 same season = military (tier4) before political (tier5).

### Parley attempt:
Ehrenwall approaches Himlensendt mid-battle (simultaneous engagement). Himlensendt's default disposition: Cool (Ob 3). Ehrenwall uses Presence + relevant History.

**Track interactions:**
- TT 80: High Thread Tension. Does TT affect social rolls? Not specified in §8.3 or social rules directly. TT affects practitioners and Thread operations. Social rolls are unaffected unless a rule explicitly applies TT.
- IP 75: Altonian Pressure at near-threshold. F-B10-11 flag (from prior session): "Diplomatic IP Resolution locked out above TT 60."

**F-B10-11 interaction:** If TT 80 locks diplomatic IP resolution, then Ehrenwall cannot use the parley to reduce IP regardless of social success. The parley can still achieve other outcomes (surrender, conditional ceasefire) but not IP reduction.

**TT 80 + mass combat environment:** "Thread operation effects from prior rounds manifest at Priority 1." At TT 80, any Thread operation in this mass combat generates TT × 3 = massive TT gain. Even without threadweaving in this test, the ambient TT affects the battlefield atmosphere but has no mechanical effect on combat or social rolls per current rules.

### Finding

#### EDGE CASE [Ambiguity]: TT as ambient battlefield modifier — no mechanic defined
**Setup:** TT 80 in an active mass combat zone.
**Mechanism:** High TT is defined as affecting practitioners and Thread operations. No rule specifies whether high TT imposes penalties or conditions on non-practitioners in a combat environment.
**Severity:** P2 — missing rule for TT environmental effects at high values in combat.
**Proposed fix:** Add to §8.3 (or §5/Clocks): "If TT exceeds 70, all Cohesion checks in mass combat suffer +1 Ob (troops are disturbed by ambient Thread activity even if they cannot perceive it directly). This applies regardless of whether Thread operations are being performed."

---

# PART III — SUMMARY OF FINDINGS

## P1 Findings (Game-Breaking)

| ID | Location | Issue | Fix Required |
|----|----------|-------|-------------|
| P1-B11-01 | §8.3 | Mass combat base damage undefined — disposition table adds to nonexistent base | Define base damage as net successes over Ob |
| P1-B11-02 | §8.3 | Formation Break Ob stacking not specified — two valid interpretations produce radically different mass combat attrition | Specify: stacking, cumulative, persists through rally |
| P1-B11-03 | §8.4 | Assault (siege Domain Action) vs. mass combat outcome — unclear which determines breach result | Specify: mass combat win = Fortification −1 |
| P1-B11-04 | §11.7 | Hybrid season phase order undefined — Personal Phase vs. Strategic Phase sequence not specified | Specify: Strategic first, then Personal, with explicit carryover rules |
| P1-B11-05 | §11.7 | Mode-switch mid-siege destroys garrison attrition state | Conversion rule: each Endurance lost = −0.5 Fortification |
| P1-B11-06 | §8.3 | Artillery Bombard manoeuvre has no resolution mechanic | Define Bombard: flat damage, no melee exchange, distance Ob |

## P2 Findings (Bad Play Experience)

| ID | Location | Issue | Proposed Fix |
|----|----------|-------|-------------|
| P2-B11-01 | §8.1 | Defence split declaration timing unclear for 8+ attacker pileup | "Defender allocates blind before any offence revealed" |
| P2-B11-02 | §8.1 | Reach priority — "same range" ambiguity when shorter weapon closes | Define: shorter at adjacent = fights at own optimal range; longer loses priority |
| P2-B11-03 | §8.1 | Stunt + chain die interaction on crit success range | Chain dice still chain; crit success applies to narrative outcome separately |
| P2-B11-04 | §8.1 | Max stunt eliminates partial resolution entirely | Optional: consecutive Stunt cost +1 Ob or require narrative justification |
| P2-B11-05 | §8.1 | Escape during Tie Up — Tie Up silent on preventing escape | Tie Up = escape blocked this round; retry next round |
| P2-B11-06 | §8.1 | Rescue declared against non-attack action — wasted action, no ruling | "Rescue fails if no incoming attack exists; action is lost" |
| P2-B11-07 | §8.1 | Incapacitation timing — does dying character complete their action? | "Complete currently-resolving action; fall at end of that priority step" |
| P2-B11-08 | §8.3 | Three-way combat — no resolution when 2/3 parties route simultaneously | Surviving party wins; receives veteran bonus |
| P2-B11-09 | §8.3 | Commander in duel still contributing dice — narratively odd | Confirm: dice contribute (orders already issued); Memory conditional order unavailable |
| P2-B11-10 | §8.3 | Commander in duel cannot also Rally | "Commander in Priority 8 personal action cannot spend mass combat action same round" |
| P2-B11-11 | §8.3 | Routed unit drifts during Contested Figure resolution | "Routed units hold position during inter-round scene resolution" |
| P2-B11-12 | §8.3 | Named NPC incapacitation has no unit morale link | "Commanding officer incapacitated = unit loses Commander Contribution for remainder of battle" |
| P2-B11-13 | §8.3 | Artillery locked into Balanced disposition — may be unintentional | Flag for design review: intended or oversight? |
| P2-B11-14 | §8.3 | KT rally loop abuse if Formation Break Ob non-stacking | Enforce stacking; cap at 3 breaks before permanent rout |
| P2-B11-15 | §8.4 | Siege assault vs. mass combat resolution conflated | Clarify assault roll vs. mass combat outcome relationship |
| P2-B11-16 | §8.5 | Hybrid: Personal Phase interdiction vs. same-season battle | Personal Phase applies N+1 by default; GM exception for scene-before-battle |
| P2-B11-17 | §11.4 | Cross-mode seasonal cap tracking — no designated tracker | Explicit GM tracking sheet instruction |
| P2-B11-18 | §11 | Narrative agreements from TTRPG scenes not preserved across mode switch | "Pending Agreement" record; resolves on trigger in any mode |
| P2-B11-19 | §8.3 | TT 80+ has no defined effect on combat | +1 Ob Cohesion checks at TT 70+ |
| P2-B11-20 | §8.1 | Attacks 3–8 in pile-on against already-incapacitated character — no ruling | "Subsequent attacks resolve as uncontested Coup de Grâce" |
| P2-B11-21 | §8.1 | Ambush formula: Tactics History used as Ob component inconsistently | Clarify with example; specify cap at Ob 7 |

## P3 Findings (Minor)

| ID | Location | Issue |
|----|----------|-------|
| P3-B11-01 | §8.1 | Fibonacci table cap at 8+ — players may expect continued scaling; add sidebar note |
| P3-B11-02 | §8.1 | Ob 10 cap reached via extreme stacking — correct per rules, confirm design intent |
| P3-B11-03 | §8.3 | Commander death + leaderless unit fight — slow and grim but functional; no fix needed |
| P3-B11-04 | §8.5 | Self-interdiction (traitor/scorched earth) — exotic but possible; add voluntary cut rule |

## Design Confirmations
- Fibonacci cap at 8+: correct and sufficient. Auto-incapacitation bottleneck before bonus matters.
- Skill-dominates-equipment: confirmed across all duel scenarios.
- Reach priority: functions as intended. Informed initiative cannot negate it.
- Supply line 1-season delay: likely intentional. No fix needed unless confirmed otherwise.

---

## Coverage Matrix Updates

| Mechanic | ID | Isolation | Interaction | Scenario | Edge Cases | Status |
|---|---|---|---|---|---|---|
| Personal Combat (core) | M-008 | ✓ prior | ✓ prior | ✓ B11 | ✓ B11 | Issues found |
| Mass Combat | M-020 | ✓ prior | ✓ prior | ✓ B11 | ✓ B11 | P1 Issues found |
| Scale Transitions | M-025 | ✓ prior | ✓ B11 | ✓ B11 | ✓ B11 | P1 Issues found |
| Siege | M-021 | ✓ B11 | ✓ B11 | ✓ B11 | ✓ B11 | P1 Issues found |
| Supply Lines | M-022 | ✓ B11 | ✓ B11 | — | ✓ B11 | Issues found |
| Wound System | M-005 | ✓ prior | ✓ B11 | — | ✓ B11 | Issues found |
| Group Attacks (Fib.) | M-009 | ✓ B11 | ✓ B11 | — | ✓ B11 | Issues found |
| Mode Transitions | M-050 | — | — | ✓ B11 | ✓ B11 | P1 Issues found |

---

*Batch 11 simulation complete. 6 P1 findings, 21 P2 findings, 4 P3 findings, 2 design confirmations.*
*Next: Patch proposals to be drafted for P1 items. M-036 (Parliamentary Vote) and M-037 (Grand Debate) remain open from prior session plan.*
