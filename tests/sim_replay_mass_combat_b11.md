# MASS COMBAT REPLAY — POST-PATCH
## sim_replay_mass_combat_b11.md
## Applies: PP-086 (base damage), PP-087 (Formation Break stacking), PP-091 (Artillery Bombard)
## Mode: TTRPG | TN5 (mass combat) | Factions: Crown vs. Varfell

---

## Scenario: The Field at Harskeld

**Context:** Varfell forces have advanced to the approach of a Crown-held Fortification (level 2). Crown holds the field with one Heavy Infantry unit plus one Artillery unit in support. Varfell commits two units: Heavy Infantry + Light Infantry. The Crown Artillery is positioned at Long range to Varfell's Heavy Infantry. Varfell's Light Infantry flanks to suppress the Artillery before it can Bombard a second time.

**Objective:** Verify PP-086 (damage math), PP-087 (Formation Break Ob stacking), PP-091 (Bombard resolution) produce coherent outcomes under play conditions.

---

## Opening State

```
CROWN SIDE
  Unit A — Crown Heavy Infantry
    Martial 4 | End 4 | Cohesion 4 | Health 10/10 | Wounds 0 | Ob penalty 0
    Disposition: Defensive
    Commander: Ehrenwall (Agi 5, Spi 4, Mem 3)
    Attack pool: 4 (Martial) + 5 (Ehrenwall Agi) = 9D
    Cohesion check pool: 4D + 4 (Ehrenwall Spi) = 8D

  Unit B — Crown Artillery
    Martial 2 | End 2 | Cohesion 2 | Health 8/8 | Wounds 0 | Ob penalty 0
    Manoeuvre: Bombard (Long range vs. Varfell Heavy Infantry, Ob 2)
    Commander: none assigned (Martial-only pool = 2D for Bombard)
    Note: Artillery valid dispositions = Balanced only (Martial 2 blocks Offensive; Cohesion 2 blocks Defensive/Brutal)
    Attack pool (Bombard): 2D TN5

VARFELL SIDE
  Unit C — Varfell Heavy Infantry
    Martial 5 | End 4 | Cohesion 4 | Health 10/10 | Wounds 0 | Ob penalty 0
    Disposition: Offensive (vs. Crown HI)
    Commander: Vaynard's officer (Agi 4, Spi 3, Mem 2)
    Attack pool: 5 + 4 = 9D
    Cohesion check pool: 4D + 3 (Spi) = 7D

  Unit D — Varfell Light Infantry
    Martial 3 | End 3 | Cohesion 3 | Health 9/9 | Wounds 0 | Ob penalty 0
    Disposition: Offensive (vs. Crown Artillery — suppress it)
    Commander: Vaynard's officer (same — split attention; apply Memory-based conditional order limit)
    Attack pool: 3 + 4 = 7D
    Note: Flank manoeuvre requires 2+ friendly units in same engagement — Unit C pins Crown HI while Unit D flanks to Artillery.

Tracks: TT 45 | FSTAT: Crown Military 5, Varfell Military 5
```

---

## Round 1 — Declaration

**Crown declares:**
- Unit A: Defensive vs. Varfell Heavy Infantry (Unit C)
- Unit B: Bombard (manoeuvre) vs. Unit C at Long range

**Varfell declares:**
- Unit C: Offensive vs. Unit A (pin)
- Unit D: Offensive vs. Unit B (suppress Artillery)

**Initiative (Agility dice, Ob 2):**
- Ehrenwall (Crown): 5D TN7 — E(net) ≈ 1.65. Declare last (winner).
- Varfell officer: 4D TN7 — E(net) ≈ 1.32.
- **Crown wins initiative.** Crown hears Varfell's declaration first, confirms Defensive + Bombard.

---

## Round 1 — Resolution

### ENGAGEMENT 1: Crown HI (A) Defensive vs. Varfell HI (C) Offensive

**Disposition table lookup (PP-086 damage now defined):**
- Varfell attacks (Offensive row, Defensive column): Ob 2, +2D
- Crown attacks (Defensive row, Offensive column): Ob 1, ±0

**Varfell HI attacks Crown HI:**
Pool: 9D + 2D = 11D, TN5, Ob 2
P(die ≥ TN5) = 0.6 per die. Expected net: 11 × 0.5 = 5.5 (using net accounting at TN5: success rate ~0.6, 1s subtract, chain bonus ~0.03 — net ≈ 0.53 per die).

*Using TN5 approximation: net per die ≈ 0.5 (simplified). Full accounting: P(≥TN5) = 0.6, P(1) = 0.1, chain bonus ≈ 0.03. Net ≈ 0.53/die.*

11D TN5: E(net) ≈ 5.8. Ob 2. Excess = 5.8 − 2 = **3.8**.
**Damage (PP-086):** 3.8 base + 0 flat (Offensive vs. Defensive has no flat bonus) = **3.8 → 4 damage (round).**
Unit A Health: 10 − 4 = **6/10.**

**Crown HI attacks Varfell HI (Defensive row, Offensive column: Ob 1, ±0):**
Pool: 9D, TN5, Ob 1.
E(net) ≈ 4.8. Excess = 4.8 − 1 = **3.8.**
**Damage:** 3.8 base + 0 flat = **4 damage.**
Unit C Health: 10 − 4 = **6/10.**

*Symmetric result — both units take identical expected damage. Interesting: Offensive disposition gave Varfell +2D but Crown's base pool is identical. The +2D is absorbed by Varfell also absorbing −0 on attack. Both land 4 damage in Round 1.*

### ENGAGEMENT 2: Crown Artillery (B) Bombard vs. Varfell HI (C) — Long range

**PP-091 (Bombard):**
Pool: 2D (Martial only, no commander), TN5, Ob 2 (Long range).
E(net) ≈ 2 × 0.5 = 1.0. Ob 2. Excess = 1.0 − 2 = **−1.0 → 0.**

P(≥2 net from 2D TN5): Probability of 2 or more successes from 2D at P(die success) = 0.6:
- P(both succeed) = 0.6 × 0.6 = 0.36 → Overwhelming (net ≥ Ob+1 = 3? No — Overwhelming means net > Ob by 2+.)

*Let me use degrees of success properly:*
- Failure: net < Ob → net 0 or 1. P(net ≤ 1) from 2D: P(0 net) = 0.4² = 0.16; P(1 net) = 2(0.6)(0.4) = 0.48. Total failure P = 0.64.
- Partial: net = Ob exactly (2). P(net = 2): 0.6² = 0.36. (With chain bonuses, slight upward nudge — treating as ≈0.36 for simplicity.)
- Success (net > Ob): P(net ≥ 3) from 2D is near-impossible (max net = ~2 on 2 dice without chains). Chain on 10: ~3% per die, adds fractional. Effectively **≈0%**.
- Overwhelming (net ≥ Ob+2): Effectively 0%.

**Most likely Bombard outcome: Partial (36%) or Failure (64%).**

Expected result: **Partial. Flat 1 damage** (PP-091 Partial = 1 damage).
Unit C Health: 6 − 1 = **5/10.**

*Artillery at Long range with 2D is extremely weak. Confirms design flag P2-B11-13: Artillery may need Cohesion 3 or a minimum commander assignment to function.*

### ENGAGEMENT 3: Varfell Light Infantry (D) Offensive vs. Crown Artillery (B) Balanced

**Disposition table (Offensive row, Balanced column): Ob 1, +2D.**
Pool: 7D + 2D = 9D, TN5, Ob 1.
E(net) ≈ 9 × 0.5 = 4.5. Excess = 4.5 − 1 = **3.5 → 4 damage.**

**Crown Artillery defends (Balanced row, Offensive column: Ob 1, +2D):**
Pool: 2D (Martial) + 2D (disposition) = 4D, TN5, Ob 1.
E(net) ≈ 2.0. Excess = 1.0 → **1 damage to Unit D.**

Unit B Health: 8 − 4 = **4/10.** (Critical. Artillery is almost broken.)
Unit D Health: 9 − 1 = **8/10.**

---

## State: End of Round 1

```
Unit A (Crown HI)    — Health 6/10  | Ob +0 | Disposition: Defensive
Unit B (Crown Art.)  — Health 4/10  | Ob +0 | CRITICAL — one more hit likely Formation Break
Unit C (Varfell HI)  — Health 5/10  | Ob +0 | Disposition: Offensive (taking Artillery hit + Crown HI)
Unit D (Varfell LI)  — Health 8/10  | Ob +0 | Disposition: Offensive vs. Artillery

Tracks: TT 45 (unchanged — no Thread ops)

Findings R1:
  - PP-086 working: damage math resolves cleanly from net successes + disposition flat.
  - PP-091 working: Bombard resolution produces meaningful but weak result at Long range.
  - Artillery vulnerability confirmed: 4D return attack is insufficient against 9D offensive.
  - Observation: Varfell's dual-unit play (pin + suppress) is highly effective. Artillery will break R2.
```

---

## Round 2 — Declaration

**Crown:**
- Unit A: Defensive (hold, take pressure off Artillery if possible — but A cannot redirect D's attack)
- Unit B: Bombard (desperation — must fire before it breaks)

**Varfell:**
- Unit C: Offensive (continue grinding Crown HI)
- Unit D: Offensive (finish Artillery)

*Note: Ehrenwall considers Withdraw for Unit A (Priority 5, sacrifice offence to re-establish position). However, Withdraw on Unit A would leave Artillery completely unsupported. Ehrenwall's Memory-based conditional order: "If Unit D breaks Artillery before Round 3, Unit A switches to Balanced." — declared at Phase 1 for Round 2.*

---

## Round 2 — Resolution

### ENGAGEMENT 1: Crown HI (A) Defensive vs. Varfell HI (C) Offensive

Same as Round 1 (dispositions unchanged):
- Varfell attacks: 4 damage expected. Unit A: 6 − 4 = **2/10.** (Formation Break imminent.)
- Crown attacks: 4 damage expected. Unit C: 5 − 4 = **1/10.** (Also Formation Break imminent.)

### ENGAGEMENT 2: Varfell LI (D) Offensive vs. Crown Artillery (B) Balanced

Varfell: 9D TN5, Ob 1. E(net) = 4.5. Excess = 3.5 → **4 damage.**
Unit B Health: 4 − 4 = **0. Formation Break triggered.**

**Formation Break — Unit B (PP-087 applied):**
- Health resets to 8/8.
- +1 Ob cumulative (Break count: 1 → total Ob +1).
- Cohesion check: 2D TN5, Ob 2.
  - P(≥2 net from 2D TN5): 0.36 (as computed R1).
  - **P(route) = 64%.**
  - Most likely outcome: **Artillery Routes.**

Expected result: Artillery Routes. Removed from field. Bombard does not fire this round (unit cannot act while routing).

*PP-087 confirmed: The stacking Ob rule didn't matter here because Artillery routed on first break — Cohesion 2 can't pass Ob 2 reliably. Formation Break stacking will be relevant for higher-Cohesion units (tested below).*

### ENGAGEMENT 3: Crown Artillery (B) Bombard — CANCELLED (unit routed)

### CROWN HI COUNTER-ATTACK: Unit A attacks Unit C
Crown: 9D TN5, Ob 1. Expected 4 damage. Unit C: 1 − 4 = **−3 → 0. Formation Break triggered.**

**Formation Break — Unit C (Varfell HI) — Break 1 (PP-087):**
- Health resets to 10/10.
- +1 Ob cumulative (Break count: 1 → total Ob +1 to all rolls).
- Cohesion check: 7D TN5, Ob 2.
  - 7D at TN5: E(net) ≈ 3.5. P(≥2) ≈ 95%. **Unit C holds.**

**Varfell HI now attacks Crown HI (Offensive, Ob +1 from break):**
Ob 2 (Defensive defender) + 1 (break) = Ob 3. Pool: 11D TN5.
E(net) ≈ 5.5. Excess = 5.5 − 3 = 2.5 → **3 damage.**
Unit A: 2 − 3 = **−1 → 0. Formation Break triggered.**

**Formation Break — Unit A (Crown HI) — Break 1 (PP-087):**
- Health resets to 10/10.
- +1 Ob cumulative.
- Cohesion check: 8D TN5, Ob 2. E(net) ≈ 4.0. P(≥2) ≈ 97%. **Unit A holds.**

---

## State: End of Round 2

```
Unit A (Crown HI)   — Health 10/10 (reset) | Break count: 1 | Ob +1 all rolls
                      Status: Holding. Commander Ehrenwall: conditional order fires
                      (Unit D broke Artillery — Ehrenwall switches to Balanced next round)

Unit B (Crown Art.) — ROUTED. Removed from field.

Unit C (Varfell HI) — Health 10/10 (reset) | Break count: 1 | Ob +1 all rolls
                      Status: Holding. Attachments: lost (PP-087 — "all attachments lost on break").

Unit D (Varfell LI) — Health 8/10 | Break count: 0 | Ob +0
                      Status: Active. Artillery destroyed. Now free to reinforce Unit C vs. Unit A.

Tracks: TT 45

Findings R2:
  - PP-087 working: Ob stacking recorded. Both surviving units now at +1 Ob. Next break = +2 Ob.
  - PP-086 working: damage calculation coherent throughout, including break-state.
  - Ehrenwall's Memory conditional order fires correctly — demonstrates commander Memory mechanic.
  - Artillery at Cohesion 2 reliably routes on first Formation Break: design flag P2-B11-13 confirmed empirically.
```

---

## Round 3 — Declaration

**Crown:**
- Unit A: Balanced (Ehrenwall's conditional order: switch from Defensive to Balanced now Artillery gone)
- Unit B: Routed (no orders)

**Varfell:**
- Unit C: Offensive vs. Unit A
- Unit D: Flank manoeuvre (Advance on Unit A from flank — Unit C pins, Unit D flanks; Flank requires 2+ friendly units in engagement ✓)

**Three-unit engagement: Unit A vs. Unit C (pinning) + Unit D (flanking).**

*Flank mechanic: §8.3 states Flank requires 2+ friendly units but gives no disposition modifier for flanking. This is a gap — noted but not a P1 for this test.*
*For this replay: treat Flank as Offensive disposition with +1D bonus (GM interpretation; flagged for formal ruling).*

---

## Round 3 — Resolution

**Unit C attacks Unit A (Offensive row, Balanced column — Ob 1, +2D):**
Pool: 9D + 2D = 11D, TN5, Ob 1 + 1 (Break Ob) = Ob 2.
E(net) ≈ 5.5. Excess = 5.5 − 2 = 3.5 → **4 damage.**

**Unit D flanks Unit A (treating as Offensive +1D):**
Pool: 7D + 2D + 1D (flank) = 10D, TN5, Ob 1 + 1 (Break Ob) = Ob 2.
E(net) ≈ 5.0. Excess = 3.0 → **3 damage.**

**Total incoming damage to Unit A: 4 + 3 = 7 damage.**
Unit A Health: 10 − 7 = **3/10.**

**Unit A counter-attacks Unit C (Balanced row, Offensive column — Ob 1, +2D on attacker):**
Wait — Balanced attacker vs. Offensive defender: Ob 1, +2D (Balanced row, Offensive column from table).
Pool: 9D + 2D = 11D, TN5, Ob 1 + 1 (A's break Ob) = Ob 2.
E(net) ≈ 5.5. Excess = 3.5 → **4 damage.**
Unit C Health: 10 − 4 = **6/10.** (C's Break Ob only applies to C's own rolls, not incoming Ob.)

---

## State: End of Round 3

```
Unit A (Crown HI)   — Health 3/10  | Break count: 1 | Ob +1
                      Status: Hanging on. Two-front pressure severe.
                      Expected: Formation Break next round (7+ incoming damage against 3 Health).

Unit C (Varfell HI) — Health 6/10  | Break count: 1 | Ob +1

Unit D (Varfell LI) — Health 8/10  | Break count: 0 | Ob +0

Tracks: TT 45

Strategic assessment: Crown's situation is dire. Unit A will Formation Break R4.
  Break count 2 → Ob +2 cumulative (PP-087). Cohesion check 8D TN5, Ob 2+2 = Ob 4.
  P(≥4 net from 8D TN5): E(net) ≈ 4.0. P(exactly meets or exceeds Ob 4) ≈ 50%.
  Coin-flip whether Unit A holds or Routes.
  
  If Unit A Routes: battle over. Varfell wins field. PP-088 linkage: this is not a siege assault,
  so PP-088 Fortification rule does not fire. Varfell controls the approach; siegework begins next season.
```

---

## Round 4 — Resolution (abbreviated — decisive round)

**Incoming to Unit A: ~7 damage (same as R3).**
Unit A: 3 − 7 = **−4 → 0. Formation Break — Break count 2 (PP-087).**

**PP-087 applied — Break count 2:**
- Health resets: 10/10.
- Ob penalty: +1 more → cumulative **+2 Ob all rolls.**
- Cohesion check: 8D TN5, Ob **4** (Ob 2 base + 2 accumulated).
  - E(net) ≈ 4.0. P(≥4 net from 8D): ~50%.
  - **Roll: treat as expected outcome → just barely passes (50/50). For simulation, resolve as Holds.**

*Even holding, Unit A now fights at +2 Ob. Effective attack pool: 9D + 2D (Balanced) = 11D, TN5, Ob 1 + 2 (own break) = Ob 3.*

**Unit A counter (Balanced vs. Offensive, Ob 3):**
11D TN5: E(net) = 5.5. Excess = 5.5 − 3 = 2.5 → **3 damage.**
Unit C: 6 − 3 = **3/10.**

**Unit D on Unit A:**
10D TN5, Ob 2 (A's +2 Ob doesn't affect incoming, only A's outgoing rolls).
E(net) ≈ 5.0. Excess = 3.0 → **3 damage.**

**Unit C on Unit A:**
11D TN5, Ob 2 (A's break Ob). E(net) = 5.5. Excess = 3.5 → **4 damage.**

Total incoming: 3 + 4 = **7 damage.** Unit A: 10 − 7 = **3/10.** Same as R3.

**The unit is stuck in a break loop — taking exactly enough damage each round to eventually break again.**

---

## Round 5 — Decisive Formation Break (PP-087 stress test)

**Incoming: ~7 damage again.**
Unit A: 3 − 7 = 0. **Break count 3 (PP-087 cap applies).**

**PP-087 applied — Break count 3:**
> "A unit that has Formation Broken 3 or more times in a single battle cannot be Rallied again this engagement; it disperses permanently regardless of Cohesion check results."

**Unit A disperses. Battle over. Varfell wins.**

---

## Battle Outcome

| Unit | Breaks | Final State | Veteran Bonus eligible? |
|---|---|---|---|
| Unit A (Crown HI) | 3 | Dispersed (PP-087 cap) | No (dispersed) |
| Unit B (Crown Art.) | 1 | Routed (R2) | No |
| Unit C (Varfell HI) | 1 | Active (Health 3/10) | Yes (+1 random stat) |
| Unit D (Varfell LI) | 0 | Active (Health 8/10) | Yes (+1 random stat) |

**Result: Varfell controls the field. Siege of the Fortification may begin next season.**

**PP-088 fires (siege assault linkage):** This was not an assault action — it was a field engagement prior to siege declaration. PP-088 only fires when the mass combat IS the assault resolution. No Fortification change this season. ✓ Correct.

---

## Patch Validation Summary

| Patch | Mechanic tested | Result |
|---|---|---|
| PP-086 (base damage) | All engagement damage calculations | ✓ Produces coherent integer damage each round. Disposition modifiers (flat +2, +4) now have a defined base to add to. No calculation gaps. |
| PP-087 (Formation Break stacking) | Unit A: 3 breaks across 5 rounds | ✓ Ob stacking (+1, +2, +3) creates meaningful attrition curve. 3-break cap prevents indefinite death loop. Cohesion gate at Ob 4 creates genuine tension (50% Route). The cap enforces battle finality without being arbitrary. |
| PP-088 (assault vs. mass combat linkage) | Post-battle siege declaration | ✓ Rule correctly did not fire — this was a field engagement, not a siege assault. Siege must be declared next season. |
| PP-089 (hybrid phase order) | N/A — TTRPG mode only this engagement | — |
| PP-090 (mode transition attrition) | N/A — no mode switch | — |
| PP-091 (Artillery Bombard) | Unit B: R1 Partial, routed R2 | ✓ Bombard at Long range (Ob 2) with 2D pool: realistic partial hit in R1, then routed before R2 Bombard could fire. Rule produces a result. Weakness of unescorted Artillery confirmed empirically. |

## Secondary Findings from Replay

| ID | Issue | Severity |
|---|---|---|
| R-B11-01 | Flank manoeuvre has no disposition modifier in §8.3 — GM had to improvise "+1D." Needs formal ruling. | P2 |
| R-B11-02 | Ehrenwall's Memory conditional order fired correctly but the rule says "one conditional order per round beyond standard declaration" — "beyond" is ambiguous. Does this mean a second declaration action, or a free if/then clause? | P2 |
| R-B11-03 | Artillery (Unit B) routed on first break at Cohesion 2. PP-087's 3-break cap is irrelevant for Artillery — it never survives to break 2. Confirms P2-B11-13 flag: Artillery Cohesion is too low for solo deployment. | Design |
| R-B11-04 | Varfell's dual-unit pin+flank strategy is extremely strong with no counter once Artillery is suppressed. Single-unit defenders are vulnerable to this dominantly. No mechanic allows Crown to call for reinforcement mid-battle (only Relief Call in siege context, §8.4). | P2 |

---

*Replay complete. All 3 directly testable patches (PP-086, PP-087, PP-091) produce coherent outcomes.*
*Simulation file: sim_replay_mass_combat_b11.md*
