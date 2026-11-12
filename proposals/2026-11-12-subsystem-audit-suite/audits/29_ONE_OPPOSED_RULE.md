# ONE OPPOSED RULE — the form and the tuning of the opposed contest, for the argument and the fight (A-71)

## Status: REFERENCE (a design audit with measurements; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Read at: 5c0a353 (working tree), 2026-11-12. Lane 29 (Fable). Serves `unified/DECISIONS_ANSWERED.md` A-71.

The executable plan is `proposals/29_DICE_one_opposed_rule_form_and_tuning.md`. This file holds the verdict,
the measurements and what each rejected form loses. Probes: scratchpad `runs/ONE_OPPOSED/` (§9); every run
`PYTHONHASHSEED=0`, seeds stated; nothing tracked was edited (module attributes were patched in-process).

---

## 0. Verdict

**One rule serves both, and it is tunable to Jordan's three goals at once: a defender's *training* stands
against the roll at what his dice of it would net (`MU_PER_DIE` = 0.4 a point of trained score), his
*aptitude* and his *wounds* reach the roll as named levels under the soft cap, and the six base dice both
sides hold are never part of the opposition.** Measured on the repository's own engine:

- **The fight** (0.4 × the defender's score, `DMG_SCALE` 1.07 as A-31 orders): 4.27 turns and 4.50 wounding
  blows where the shipped fight has 3.35 and 3.20; a lead change in 45.2% where it has 35.2%; 0.1% undecided;
  an attack on an equal draws blood 52% of the time, at rank 2 and at rank 5 alike.
- **The better man wins at one curve in both contests.** One rank better wins about two in three, two ranks
  three in four, four ranks nine in ten: the fight reads 65.7 / 78.0 / 92.3% (felled shares, 1,000 fights a
  cell); the argument reads 66 / 78 / 92% of decided exchanges (closed form). Equals are 50.8% and exactly
  50%.
- **Defence is real and is not a wall.** Each rank of the defender's training takes about four to five
  points off an attacker's chance to wound and about seven off his chance of a telling (Overwhelming) roll;
  each step of aptitude is one level (0.25σ) against the roller, bounded by the soft cap at 1.5σ. Two
  masters do not stall: the rank-7 mirror runs 4.6 turns with 0.3% undecided (§4).

**What the measurement refuses is the form the suite had written down.** `U1` §4 and
`U5a_capability_home_and_two_inputs.md` row B5 put 0.4 on the defender's *pool* (score plus the base). In an
argument that is right and is kept, restated: the base's mean is the *even line* the difficulty ladder
stands on. In a fight it is the big attrition Jordan named: 8.4 turns, 70.7% of turns bloodless and **29.0%
of fights undecided** at twelve turns (49.7% with A-31's scale). The cause is structural and is in the code:
a fight already spends the defender's base competence in its defence layer (`modules/combat/wrapper.py:340-357`,
the parry, dodge and wind that turn a share of clean rolls), so charging it again in the obstacle counts it
twice. The single largest obstacle to the rule is therefore not a number: it is saying once, at one owner,
*which part of a defender is opposition* (his training) and which is not (the base everyone has).

The trade Jordan is owed, in one sentence: **the blow and the argument share the whole opposition rule and
the same better-man curve, and differ by one declared row, the act's own difficulty: a blow at an equal
draws blood one time in two and fells nobody alone; an argument at an equal on a routine matter fails six
times in ten and carries outright one time in four** (§6, J-29-01).

---

## 1. What is coded today (the two half-scores, and why they are not one rule)

| consumer | call site | pool | obstacle from the defender | sampler | talent | a wound |
|---|---|---|---|---|---|---|
| the fight | `modules/combat/core.py:102-124` `ob_from_defender`; `wrapper.py:331-332` | `max(5, faculty + 6)` (`core.py:51-58`) | `faculty / 2` | `roll_net_continuous` (`core.py:62`) | six attributes through the module's sigma assembly (`wrapper.py:316-320`) | sigma on attack and defence (`WOUND_ATK_OB`, `WOUND_DEF_OB`) |
| the argument | `modules/social_contest/roll.py:89-154` `obstacle`; `:157-166` `roll` | the larger of attribute and key, else `pool_default` (`seam/wrappers/pool.py:78-100`) | `opposition / 2`, else `obstacle_default`; the room subtracted; a per-pool ceiling | whole dice `roll_net` (`roll.py:165`) | folded into the pool by `max` | none |

Both halve a score, and they are still two rules: different operands (the fight halves the same number its
pool is built from; the argument halves a number its pool may not contain), different samplers, and one
has a base of six dice where the other has none. `core.py:113-116` says so itself: *"two ladders for one
quantity"*.

The half-score has one defect in both (measured before, reproduced here): a die nets 0.4 and an opponent's
point costs 0.5, so equals drift toward failure as they improve. Fight, shipped: an exchange between equals
fails 11.9% at rank 0 and 37.7% at rank 12 (`audits/16_PESSIMIST_PC.md` `pD_skill.txt`); argument, on the
re-centred sampler: P(Failure) for equals 60.1% at rank 0 and 66.1% at rank 7 (§5, P5.2). Skill makes a
contest between equals slower. That is the seed of attrition, and it is in the rate, not in any dial.

---

## 2. The rule (decided; the exact edits are in the proposal)

```
opposed_ob(score, rate = MU_PER_DIE)  =  rate × max(0, score)          # one owner: engine/dice_engine/sigma_leverage.py

obstacle  =  what the act itself asks                                  # the argument: even line + its difficulty level; the blow: nothing
           + opposed_ob(the defender's trained score)                  # PROWESS: 0.4 a point (A-26)
           + hostile terms                                             # A-25; each non-negative
roll      =  roll_net_continuous(pool) + net_boost(levels for − levels against, pool)       # A-5; soft-capped at 1.5σ
pool      =  max(pool_floor, trained score + addends + pool_add)       # A-6: 6 and 5
levels    :  the roller's talent for him, the defender's talent against him (APTITUDE, A-7);
             a wound against its bearer when he rolls and for the roller when he defends (A-8);
             favourable circumstance, a seat's modifier (A-25, A-12)
band      =  degree_from_net(roll, obstacle)                           # the one ladder
```

Three sentences a player can hold: *his training is what stands against me, a point for a point; what he
is and what has been done to him tilt my dice, never the bar; what the act asks is the same whoever I face.*

**The even line.** `MU_PER_DIE × pool_add` (2.4 at the shipped pair) is the mean of the base dice. An
argument's obstacle stands on it (so an untrained person meets a plain matter against an untrained person
half the time, and A-26's *an even contest is even* holds at every rank: P5.1, row 3, 50.0% at ranks 0, 2,
4, 7). A blow's obstacle does not, because the fight is the one contest with a defence layer: the defender's
mode turns 55 to 62% of Successes and 10 to 17% of Overwhelmings (`config.py:136`), and with the obstacle on
training alone an attack on an equal wounds 51.6% of the time. The two contests are therefore even in the
same sense (one chance in two of an effect on an equal) by the route each already has. The even line is one
derived value read from two owners (`MU_PER_DIE`, `pool_add`), never typed.

Numerically, for every social and task roll, this is `U1` §4's obstacle unchanged (`0.4 × the opponent's
pool` = even line + `0.4 × score`). What changes is the attribution, and with it what the fight reads.

---

## 3. The three targets (derived from Jordan's words and the tree's figures)

Each target is a measurable reading with a stated instrument; the proposal's gates carry them.

| goal (A-71) | target | where the number comes from |
|---|---|---|
| **(a) longer fights** | season-default mirror, death terms: mean turns in 4.0 to 5.0; mean wounding blows ≥ 4.3; a lead change in ≥ 40% of decided fights; bloodless turns ≤ 45% | A-31's own reading (`audits/16_PESSIMIST_PC.md` §6.3: 4.60 turns, 4.58 blows, 43.9%); shipped 3.35 / 3.20 / 35.2% / 40.9%. The bloodless bound says the length is bought with blows, not misses |
| **(b) the better one wins; equals are even** | of decided contests, one rank better wins 60 to 70%, two ranks 72 to 82%, four ranks 88 to 95%; equals 50% ± the sampling band; **the same window for the fight and the argument**; equals read the same at every rank (range ≤ 6 points over ranks 0 to 7) | the shipped fight's curve at the season default (64.9 / 77.0 / 93.4%, P2), which is the only better-man curve the tree has ever calibrated; A-26's premise for the flatness |
| **(c) defence from prowess and aptitude is real, and no big attrition** | per rank of the defender's training: ≥ 3 points off the attacker's wounding share and ≥ 5 off his Overwhelming share. Per step of aptitude: one named level against the roller. Bounds: undecided ≤ 2% in every mirror to rank 7; the rank-7 mirror within one turn of the rank-2 mirror; an exchange between equals fails ≤ 25% at every rank to 12; no cell at 0 or 1 | U5b §4's gate (undecided under 2%); the standing rule (both tails open); the pessimist's drift figures |

For the argument, "rounds to decision" has no built carrier (the sitting of exchanges is
`05_SC_playable_hearing_B.md`, proposed), so its bound is stated on the one act that exists and as arithmetic
on it: P(Failure) for equals at `routine` inside `13_SC_calibration.md` C1's window (0.50 to 0.65), flat
across ranks, and the expected number of exchange pairs until exactly one side lands ≤ 3.

---

## 4. The fight: candidate forms against the targets

**P1** (`p1_grid.py`; 1,200 fights a cell, seeds 0 to 1,199; band shares and bloodless turns from 300 traced
fights; season-default mirror, arming sword, light armour, score 2 both, death terms).
`c` is the mean margin of an exchange between equals.

| form of the defender's obstacle | c | `DMG_SCALE` | turns | exchanges | blows | lead change | first wounded wins | undecided | bloodless turns | exchange F / P / S / O | wound per roll |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **score / 2** (shipped; control) | 2.2 | 1.55 | 3.35 | 6.37 | 3.20 | 35.2% | 24.2% | 0.2% | 40.9% | 17.5 / 12.9 / 33.5 / 36.1 | 0.511 |
| 0.4 × score | 2.4 | 1.55 | 3.17 | 6.07 | 3.17 | 37.7% | 25.0% | 0.2% | 39.9% | 14.6 / 13.8 / 33.0 / 38.6 | 0.521 |
| 0.4 × pool − 2.0 | 2.0 | 1.55 | 3.67 | 6.83 | 3.25 | 34.3% | 24.0% | 0.5% | 43.3% | 19.3 / 13.7 / 34.0 / 33.1 | 0.479 |
| 0.4 × pool − 1.5 | 1.5 | 1.55 | 4.60 | 8.30 | 3.40 | 33.4% | 23.6% | 2.1% | 50.9% | 26.0 / 16.1 / 32.6 / 25.3 | 0.417 |
| 0.4 × pool − 1.0 | 1.0 | 1.55 | 5.63 | 9.97 | 3.49 | 31.7% | 24.2% | 5.5% | 56.9% | 34.1 / 17.3 / 30.1 / 18.5 | 0.353 |
| 0.4 × pool (`U1` §4, CAP B5 as written) | 0 | 1.55 | 8.38 | 14.10 | 3.25 | 27.6% | 21.5% | **29.0%** | 70.7% | 51.4 / 17.6 / 21.9 / 9.1 | 0.223 |
| score / 2 (U5b's default: A-31 alone) | 2.2 | 1.07 | 4.60 | 9.19 | 4.60 | 45.0% | 28.6% | 0.5% | 41.5% | 17.5 / 12.7 / 32.8 / 37.0 | 0.517 |
| **0.4 × score (chosen)** | 2.4 | 1.07 | **4.27** | 8.65 | **4.50** | **45.2%** | 27.2% | **0.1%** | 39.3% | 14.7 / 13.0 / 34.4 / 38.0 | 0.516 |
| 0.4 × pool − 2.0 | 2.0 | 1.07 | 4.92 | 9.65 | 4.60 | 43.6% | 28.5% | 1.1% | 43.3% | 19.7 / 14.0 / 33.0 / 33.4 | 0.480 |
| 0.4 × pool − 1.5 | 1.5 | 1.07 | 5.97 | 11.35 | 4.71 | 39.3% | 24.0% | 5.1% | 50.3% | 25.4 / 16.0 / 33.7 / 24.9 | 0.411 |
| 0.4 × pool − 1.0 | 1.0 | 1.07 | 7.43 | 13.69 | 4.81 | 37.1% | 26.2% | 14.1% | 56.5% | 34.0 / 16.6 / 30.5 / 18.9 | 0.349 |
| 0.4 × pool | 0 | 1.07 | 10.00 | 17.32 | 4.01 | 27.2% | 17.5% | **49.7%** | 69.8% | 50.6 / 17.3 / 22.8 / 9.2 | 0.235 |

Controls at disjoint seeds (800,000 on): shipped 3.32 turns, 3.19 blows, 32.0%, 0.2%; chosen 4.18, 4.50,
41.6%, 0.5%; 0.4 × pool at 1.07: 9.96, 4.07, 26.2%, 49.8%. The lead-change share carries a sampling band of
about four points between seed sets; turns and blows about a tenth.

**Readings.** (1) The two dials are separable, as the pessimist found: the damage scale buys blows and
reversals; the centre buys misses. Every step of the centre toward the argument's even line adds turns
without adding blows, lowers the lead-change share and raises the undecided share. (2) The pessimist's
3.2-blow fight reproduces (3.20), and A-31's reading reproduces (4.60 / 4.60 / 45.0%). (3) Moving the rate
from 0.5 to 0.4 on the score at the season default is nearly free: the obstacle goes from 1.0 to 0.8, a
third of a turn shorter, the same blows, the same reversals. (4) The form the suite had written (0.4 on the
pool) fails target (c) by an order of magnitude and target (a)'s bloodless bound; no value of the damage
scale repairs it, because the fights it leaves undecided are undecided for want of blows landing.
