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
- **Defence is real and is not a wall.** Each rank of the defender's training takes about six points off
  an attacker's chance to wound, eight to nine off his chance of a telling (Overwhelming) roll and a sixth
  off his damage; each step of aptitude is one level (0.25σ) against the roller, bounded by the soft cap at
  1.5σ. Two masters do not stall: the rank-7 mirror runs 4.30 turns with 0.4% undecided, the rank-2 mirror
  4.28 with 0.1%, where the half-score takes the same pair from 4.64 to 5.30 turns and 0.5 to 1.9% (§4).

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
mode turns 50 to 62% of Successes and 5 to 17% of Overwhelmings (`config.py:136`: `NEUTRALIZE_PARRY` 0.55,
`_DODGE` 0.62, `_WIND` 0.50, less `NEUTRALIZE_OVERWHELM_DROP` 0.45 on the top band), and with the obstacle on
training alone an attack on an equal wounds 52% of the time. The two contests are therefore even in the
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
| **(c) defence from prowess and aptitude is real, and no big attrition** | per rank of the defender's training: ≥ 4 points off the attacker's wounding share and ≥ 5 off his Overwhelming share. Per step of aptitude: one named level against the roller. Bounds: undecided ≤ 2% in every mirror to rank 7 (the rank ceiling); the longest mirror within half a turn of the shortest; an exchange between equals fails ≤ 25% at every rank to 7; no cell at 0 or 1 | U5b §4's gate (undecided under 2%); the standing rule (both tails open); the pessimist's drift figures |

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

**P2 · the better fighter** (`p2_skill.py`; 1,000 fights a cell, seeds 0 to 999; won / lost / undecided, %).

| arm | 3v2 | 4v2 | 6v2 | 5v4 | 6v4 | 7v5 | 7v3 |
|---|---|---|---|---|---|---|---|
| score / 2, 1.55 (shipped) | 64.9 / 34.8 / 0.3 | 77.0 / 22.8 / 0.2 | 93.4 / 6.3 / 0.3 | 63.8 / 36.0 / 0.2 | 73.7 / 25.7 / 0.6 | 73.5 / 25.9 / 0.6 | 93.0 / 6.6 / 0.4 |
| score / 2, 1.07 | 67.9 / 31.6 / 0.5 | 81.8 / 17.2 / 1.0 | 95.7 / 3.6 / 0.7 | 66.1 / 32.9 / 1.0 | 76.9 / 21.6 / 1.5 | 77.5 / 20.8 / 1.7 | 94.9 / 4.2 / 0.9 |
| **0.4 × score, 1.07 (chosen)** | 65.7 / 33.6 / 0.7 | 78.0 / 21.9 / 0.1 | 92.3 / 6.9 / 0.8 | 63.0 / 36.3 / 0.7 | 75.2 / 24.6 / 0.2 | 74.3 / 25.5 / 0.2 | 91.0 / 8.4 / 0.6 |
| 0.4 × pool − 1.0, 1.07 | 62.0 / 24.1 / 13.9 | 77.7 / 13.1 / 9.2 | 92.7 / 2.9 / 4.4 | 62.4 / 27.0 / 10.6 | 75.1 / 17.0 / 7.9 | 74.7 / 17.6 / 7.7 | 92.3 / 3.5 / 4.2 |
| 0.4 × pool, 1.55 | 55.3 / 20.9 / 23.8 | 69.3 / 10.8 / 19.9 | 90.5 / 1.5 / 8.0 | 54.8 / 24.4 / 20.8 | 69.5 / 14.1 / 16.4 | 69.6 / 16.6 / 13.8 | 90.2 / 1.8 / 8.0 |

Control (the mirror's won share at two disjoint seed sets): shipped 50.5 and 50.8%; chosen 50.8 and 51.4%.
The chosen arm keeps the shipped curve to within two points at every gap. Lowering the scale alone
(row 2) steepens it by three to five points, because more blows give the better man more draws; the 0.4
rate gives that back. The better man's share is the lever no arm moves much; what the arms move is whether
the fight ends.

**P3 · equals by rank** (1,000 fights a cell; turns / blows / lead change % / undecided % / bloodless turns %
/ Failure share of an exchange %).

| arm | rank 0 | rank 2 | rank 5 | rank 7 | rank 12 |
|---|---|---|---|---|---|
| score / 2, 1.55 | 3.24 / 3.26 / 37.8 / 0.2 / 38.5 / 12.7 | 3.37 / 3.21 / 34.8 / 0.2 / 40.2 / 17.5 | 3.75 / 3.13 / 33.8 / 0.4 / 43.6 / 24.0 | 3.91 / 3.12 / 32.4 / 0.5 / 46.1 / 29.1 | 4.37 / 3.06 / 30.6 / 1.3 / 51.5 / 37.8 |
| score / 2, 1.07 | 4.33 / 4.65 / 46.1 / 0.5 / 37.9 / 11.8 | 4.64 / 4.63 / 44.8 / 0.5 / 41.3 / 17.3 | 5.07 / 4.53 / 42.7 / 1.1 / 44.3 / 24.4 | 5.30 / 4.45 / 40.7 / 1.9 / 46.2 / 28.5 | 5.88 / 4.38 / 39.4 / 4.1 / 50.7 / 35.5 |
| **0.4 × score, 1.07** | 4.33 / 4.65 / 46.1 / 0.5 / 37.9 / 11.8 | 4.28 / 4.51 / 44.5 / 0.1 / 37.5 / 13.6 | 4.28 / 4.46 / 43.8 / 0.2 / 39.1 / 18.2 | 4.30 / 4.39 / 43.4 / 0.4 / 39.9 / 20.8 | 4.29 / 4.30 / 42.4 / 0.5 / 39.5 / 24.9 |
| 0.4 × pool − 1.0, 1.07 | 7.96 / 4.93 / 36.7 / 19.4 / 58.3 / 32.2 | 7.50 / 4.81 / 37.7 / 14.8 / 56.8 / 33.9 | 6.95 / 4.62 / 37.9 / 10.1 / 56.1 / 35.9 | 6.68 / 4.53 / 38.7 / 8.3 / 55.2 / 36.9 | 6.29 / 4.35 / 37.8 / 6.3 / 53.8 / 39.1 |

This is the table that answers "without making it a big attrition". Under the half-score, the better two
equals are, the longer they take and the oftener they fail to finish (the fight with A-31's scale alone
goes from 4.33 to 5.88 turns and from 0.5 to 4.1% undecided). Under 0.4 on the score the mirror is the same
fight at every rank, to a twentieth of a turn. The residual rise in the Failure share (11.8 to 24.9%) is
the widening of the curve with a larger pool, not a cost per point.

**P4 · defence is real** (attacker A against defender B, 600 traced fights a cell, chosen arm; per roll of
A: share that wounds / mean damage / Overwhelming share).

| A | B two below | one below | equal | one above | two above | four above |
|---|---|---|---|---|---|---|
| rank 2 | 64.7% / 10.4 / 57.6% | 58.2% / 8.8 / 48.1% | 52.0% / 7.3 / 38.8% | 45.8% / 6.1 / 31.1% | 39.0% / 4.8 / 23.3% | 27.5% / 3.0 / 13.2% |
| rank 5 | 62.6% / 10.1 / 56.5% | 56.6% / 8.6 / 47.6% | 51.6% / 7.4 / 40.9% | 45.2% / 6.2 / 33.8% | 39.2% / 5.1 / 26.3% | 28.5% / 3.5 / 17.1% |

Half-score at the same scale, rank 2 attacking: 64.6, 58.1, 50.9, 41.2, 34.7, 20.7%. So a rank of defence
is worth about six points of the attacker's wounding share under the chosen rate and about eight under the
half-score; the defender four ranks better is still wounded by more than one attack in four (27.5%), where
the half-score leaves one in five. Aptitude (the module's own sigma assembly, defender's attribute raised,
500 fights a cell): Agility 4, 5, 6, 7 gives the attacker 52.8, 46.8, 40.9, 36.1%, a step of Agility being
worth a rank of training; Strength 47.2, 42.9, 39.2% from 5 to 7; Endurance moves the wounding share by a
point a step and the felled share by six to ten (it is Health). Perception is far steeper (one step from its
default of 3 takes the wounding share from 52 to 39%); that is `audits/16_PESSIMIST_PC.md` §2.4's finding
and is left to its lane.

**P6 · two alternatives that keep the base in the opposition, and one that rolls both sides** (`p6_alts.py`,
1,000 fights a cell).

| arm | turns | blows | lead change | undecided | better man (4v2) |
|---|---|---|---|---|---|
| 0.4 × pool with the defence layer's neutralisation cut to 0 (the base opposes once, in the obstacle), 1.55 | 6.11 | 4.14 | 31.4% | 5.6% | 84.2 / 13.1 / 2.7 |
| the same, 1.07 | 7.73 | 5.50 | 35.7% | 15.1% | — |
| a two-sided roll (the defender rolls too) at the blow's centre, 1.07 | 4.08 | 4.15 | 44.8% | 0.1% | **65.9** / 33.7 / 0.4 |
| chosen, same seeds | 4.28 | 4.51 | 44.5% | 0.1% | 78.0 / 21.9 / 0.1 |

Cutting the defence layer to pay for the pool operand still leaves 5.6 to 15.1% of fights undecided and no
more reversals than the shipped fight has, and deletes the parry, the dodge and the riposte as things
that happen. Rolling both sides keeps the length and cuts what skill is worth: two ranks better wins two
in three where the chosen rule gives three in four, because the second roll is noise the better man cannot
buy down; it also adds a draw to every exchange for the port. Under `blood` terms a duel is still
one blow (1.08; first blood is the first wound, which no obstacle changes); under `yield` terms the chosen
arm runs 2.82 turns and 2.55 blows where today's runs 2.15 and 1.51 (800 duels each).

---

## 5. The argument: the same rule on the season's roll

**P5** (`p5_social.py`). The instrument is the repository's closed form (`sigma_leverage.p_success`, the
Normal form of the sampler A-5 orders for every roll) for the four bands, with the pool A-6 orders
(`max(5, score + 6)`). Control, closed form against 200,000 seeded draws through `roll_net_continuous`,
`net_boost` and `degree_from_net` (seed 29): pool 8 at obstacle 3.2: 50.0 / 17.1 / 23.7 / 9.2 closed, 50.2 /
17.2 / 23.5 / 9.1 dealt; at 3.7 with half a level against: 75.9 / 11.5 / 10.5 / 2.1 against 76.1 / 11.4 /
10.3 / 2.1. The closed form is the dealt roll to within a quarter of a point.

Equals by rank, Failure / Partial / Success / Overwhelming, %:

| obstacle | rank 0 | rank 2 | rank 4 | rank 7 |
|---|---|---|---|---|
| half the score, no difficulty | 11.0 / 12.7 / 38.3 / 38.0 | 16.5 / 13.2 / 34.0 / 36.2 | 21.5 / 13.2 / 30.7 / 34.6 | 27.8 / 12.6 / 27.0 / 32.6 |
| 0.4 × score, no difficulty (the blow's obstacle) | 11.0 / 12.7 / 38.3 / 38.0 | 14.4 / 12.4 / 33.7 / 39.5 | 17.1 / 11.9 / 30.4 / 40.6 | 20.3 / 11.1 / 26.9 / 41.8 |
| even line + 0.4 × score (`plain`) | 50.0 / 19.5 / 24.2 / 6.3 | 50.0 / 17.1 / 23.7 / 9.2 | 50.0 / 15.4 / 22.8 / 11.8 | 50.0 / 13.6 / 21.5 / 14.9 |
| **even line + 0.5 + 0.4 × score (`routine`)** | 60.1 / 17.7 / 18.5 / 3.7 | 58.7 / 15.9 / 19.3 / 6.1 | 57.8 / 14.5 / 19.3 / 8.3 | 56.9 / 13.0 / 18.9 / 11.2 |
| even line + 1.0 (`demanding`) | 69.5 / 15.1 / 13.3 / 2.1 | 67.1 / 14.1 / 15.0 / 3.9 | 65.4 / 13.2 / 15.8 / 5.7 | 63.6 / 12.0 / 16.1 / 8.3 |
| even line + 1.5 (`hard`) | 77.8 / 12.1 / 9.0 / 1.1 | 74.6 / 11.9 / 11.1 / 2.3 | 72.3 / 11.5 / 12.4 / 3.8 | 69.8 / 10.8 / 13.4 / 5.9 |

The tuning tables' half-step ladder (`13_SC_tuning_tables.md` T1: 0 / 0.5 / 1 / 1.5) stands unchanged on the
even line: the four levels separate by six to ten points of Failure at every rank (C2, C8), equals at
`routine` fail 56.9 to 60.1% (C1's 0.50 to 0.65) and carry 22.2 to 30.1% (C1's 0.15 to 0.30; a tenth of a
point over at rank 7, which the calibration step reads). The second row shows why the argument cannot
stand where the blow stands: with no even line an argument at an equal carries 69 to 76% of the time.

The better arguer, at `routine` (actor against opponent; then the reverse; then, of one exchange each way,
the share in which exactly one side reaches Success):

| ranks | better argues: Failure / Success-or-better | worse argues | better lands alone / worse lands alone / neither or both | better's share of decided |
|---|---|---|---|---|
| 2, 2 | 58.7 / 25.4 | 58.7 / 25.4 | 18.9 / 18.9 / 62.1 | 50.0% |
| 3, 2 | 51.7 / 32.3 | 65.5 / 20.1 | 25.9 / 13.6 / 60.6 | 65.6% |
| 4, 2 | 45.3 / 39.1 | 71.7 / 15.5 | 33.1 / 9.4 / 57.5 | 77.9% |
| 6, 2 | 34.6 / 51.4 | 82.3 / 8.5 | 47.0 / 4.1 / 48.8 | 92.0% |
| 5, 5 | 57.5 / 28.6 | 57.5 / 28.6 | 20.4 / 20.4 / 59.2 | 50.0% |
| 6, 5 | 51.4 / 34.6 | 63.3 / 23.7 | 26.4 / 15.5 / 58.1 | 63.0% |
| 7, 5 | 45.9 / 40.4 | 68.8 / 19.3 | 32.6 / 11.5 / 55.9 | 73.9% |
| 7, 3 | 35.1 / 51.4 | 80.9 / 9.8 | 46.3 / 4.8 / 48.9 | 90.6% |
| 7, 0 | 21.3 / 67.4 | 95.4 / 1.4 | 66.4 / 0.5 / 33.1 | 99.2% |

Set beside P2's chosen row: the fight's 65.7 / 63.0, 78.0 / 75.2 / 74.3, 92.3 / 91.0 against the argument's
65.6 / 63.0, 77.9 / 73.9, 92.0 / 90.6. **The two contests share one better-one-wins curve to within a point
and a half at every gap measured.** That is not tuned in; it follows from pricing a point of training at
0.4 on both sides of both rolls. The "decided exchange" is arithmetic on the one act that exists, not a
built mechanism: an exchange pair is decided 38 to 51% of the time, so the expected count of pairs to a
decision is 2.0 to 2.6, inside the bound of three. Under today's rate on the same sampler the equals drift
(Failure 60.1, 62.1, 63.9, 66.1% at ranks 0, 2, 4, 7) and the worse arguer is priced harder than the
better is helped (4 against 2: 36.1% and 11.6%).

Aptitude and wounds, as levels against the roller (rank-2 equals at `routine`; `levels_to_net_sigma`, the
soft cap applied by `net_boost`):

| against the roller | net σ (capped) | Failure | Success-or-better |
|---|---|---|---|
| nothing | 0 | 58.7% | 25.4% |
| one `minor` (one step of the opponent's aptitude, or one wound step on the roller) | −0.25 (−0.248) | 68.0% | 18.1% |
| two `minor` | −0.50 (−0.482) | 75.9% | 12.6% |
| three `minor` | −0.75 (−0.693) | 82.0% | 8.8% |
| three `major` (far past any lawful stack) | −3.00 (−1.446) | 95.2% | 1.7% |

One step of aptitude is worth about nine points of Failure at the centre, about one and a half ranks of
training (a rank is 0.4 of an obstacle, 0.18σ at pool 8, against a level's 0.25σ) and unlike training it
saturates: the cap leaves the worst-placed roller 1.7% to carry. The same levels for the roller when the
wounded man is the one argued at: Failure 48.9, 39.7, 31.8% at one, two and three `minor`. A hurt man is
easier to move and worse at moving, by one ladder, in a room and in a fight.

The extremes: rank 0 arguing against rank 7 on a `hard` matter composes 6.7 against a pool of six and
reads 1.4% Partial-or-better before the per-pool ceiling (`roll.py::_chance_floor_cap`, H-213) lifts it to
its floor; the same pair on a `routine` matter reads 4.6%. The ceiling is the argument's bound against a
wall and is `16_PESSIMIST_DICE_soft_ceiling.md`'s to shape. No cell reads 0 or 1.

---

## 6. The candidates against the three targets, and what each loses

| # | form | (a) longer fights, more reversals | (b) the better one wins; equals even | (c) defence real, no attrition | verdict |
|---|---|---|---|---|---|
| 0 | as coded: half the score in both, damage 1.55 | fails: 3.35 turns, 3.20 blows, 35.2% | fight holds; equals drift with rank in both contests | defence real; drift: rank-12 mirror fails 37.8% of exchanges | the control |
| 1 | U5b's default: half the score in the fight, 0.4 in the argument, damage 1.07 | meets: 4.60 / 4.60 / 45.0% | fight curve three to five points steeper; two rules | drift kept: 4.64 to 5.88 turns and 0.5 to 4.1% undecided from rank 2 to 12 | **loses A-71 itself** (two rules) and the flat mirror |
| 2 | 0.4 × the defender's pool in both (`U1` §4, CAP B5 as written) | fails the bloodless bound: 8.4 to 10 turns, 70% of them bloodless, reversals fall to 27% | better man's share falls (two ranks: 69.3%), a fifth undecided | **fails: 29.0 to 49.7% undecided** | the big attrition, measured |
| 3 | 0.4 × pool less a constant of 1 to 2 in the fight | 2.0: meets; 1.0: 7.43 turns, 56% bloodless | holds | 1.5: 5.1%; 1.0: 14.1% undecided, 19.4% at rank 0 | a private constant in the fight, a second regime by another name; only its top value survives, and that value is form 5 with 0.4 added to every obstacle |
| 4 | 0.4 × pool, the defence layer's neutralisation deleted | 6.1 to 7.7 turns, reversals 31 to 36% | steeper (84.2% at two ranks) | 5.6 to 15.1% undecided | **loses the parry, the dodge and the riposte**, and still fails (c) |
| 5 | **0.4 × the defender's trained score; the base is the argument's even line and the fight's defence layer; damage 1.07** | **meets: 4.27 / 4.50 / 45.2%, 39.3% bloodless** | **meets: one curve in both, 66 / 78 / 92; equals 50** | **meets: six points a rank; mirrors flat 4.28 to 4.33; undecided ≤ 0.5%** | **chosen** |
| 6 | a two-sided roll at the same centre | meets: 4.08 / 4.15 / 44.8% | **fails: two ranks better wins 65.9%** | meets | loses the better man's edge and doubles the draws |
| 7 | the defender's training as levels, not obstacle | — (not run) | saturates at the soft cap: beyond about six ranks a better defender is barely harder to hit | bounded by construction | loses A-26's own words (a cost per point) and A-7's assignment (training is dice, talent is levels); not run because the cap decides it by arithmetic (1.5σ ÷ 0.25σ) |

What the chosen form costs, stated: (i) at the shipped realm the fight's obstacle moves from 1.0 to 0.8, so
A-31's *"obstacle left alone"* is honoured in effect (a third of a turn) and not to the letter; A-71 is the
later and specific ruling (ladder step 1). (ii) A defender's rank is worth six points of the attacker's
wounding share where the half-score gave eight: the better fighter's edge is the shipped one, not the
steeper one A-31's scale alone would have produced. (iii) The blow and the argument do not have one centre
(J-29-01). (iv) The Failure share of an exchange between equals still rises from 12 to 25% over twelve
ranks, because a bigger pool is a wider curve; removing that would take an obstacle that scales with the
root of the pool, a second formula for nothing a player would see (the mirrors' length does not move).

### For Jordan

**J-29-01 · Does "the same" reach the centre, or the rule?** Taken: the rule. Option A (taken): one
opposition rule and one better-one-wins curve; a blow at an equal draws blood one time in two, an argument
at an equal on a routine matter fails 59%, half-lands 16% and carries 25%, so a position holds unless
something moves it. Option B: one centre as well, the argument carrying about one time in two; positions
change hands as readily as blood is drawn, and `13_SC_calibration.md` C1 is rewritten. The reverse (the
blow at the argument's centre) is form 2 and is not offered. Nothing else survives the ladder: the rate is
A-26's, the scale A-31's, the two inputs A-7's, the wound A-8's, and the operand is decided by measurement.

---

## 7. The battle's duel round and the hearing

- **Duel round (A-4, A-72).** A field calls one round of the combat module through `nested_entry`
  (`U5b_PC_rulings_in_the_fight.md` §1); the round's exchanges call `ob_from_defender`, so the rule is the
  same by construction, and the only edit is that the round's input carries the rate and the pool pair raw.
- **Order friction and prowess (A-59).** `27_MB_A_command_and_the_obedience_draw.md:53` declares the
  obedience draw `opposed_by: none`: a task on the even line with the ordinary score as its stand-in. The
  melee pair is not opposed (C-U5b-03). The rule therefore has no rating-against-rating site in a field
  today; one that is added later calls `opposed_ob` on the trained score and brings no rate of its own.
- **Hearing** (`05_SC_playable_hearing_B.md`). `argue` is the rule's site (the other side's
  `Speaker.score`); `answer` has no person operand and takes the even line plus its own difficulty, its
  exhibit weights as `proofs` levels; the closing draw and the ballots go through the same composer. Length
  is bounded by effort, structurally.

## 8. Dispositions

| item | where | disposition |
|---|---|---|
| J-U5b-01 (`unified/U5_FINDINGS_CLOSURE_U5b.md` §5.2) | answered by A-71 | closed by this file: neither listed option; one rule on the trained score. Option B as listed there (0.4 of the defender's pool in the fight) is form 2, refused by measurement |
| C-U5b-02 (CAP row B5 against A-31) | U5b decided "two declared regimes" | **superseded** (ladder step 1, A-71): one fixture, one rate; `fight_opposition_rate` is not created. `Folded:` on `U5b_PC_rulings_in_the_fight.md` |
| `U5a_capability_home_and_two_inputs.md` rows B4, B5; `U1` §4 row *the opponent* | the operand is the opponent's pool | **amended** in place (`Folded:`): the operand is the trained score; the pool's base is the even line. Every social figure is unchanged; the fight is what the amendment protects |
| F-PES-PC-01 (a fight is two blows) | `audits/16_PESSIMIST_PC.md` | stands; A-31's scale is the fix; this file's gate 2 reads it at the obstacle it will ship with |
| the pessimist's fourth row of §6.3 (0.4 × pool − 1: 5.65 turns, 3.48 blows, 5.3%) | same | reproduced (5.63, 3.49, 5.5%); it is form 3 at 1.0 |
| `05_SC_opposed_obstacle_parity.md` (the carrier of the rate) | option B's edit 1 | stands with one change: the composed obstacle is the even line plus the product; its whole-dice tables are history |
| `13_SC_tuning_tables.md`, `13_SC_calibration.md` | T1's sizes, C1 to C8 | stand; restated on trained ranks and on the even line; one row added to the test (the better-arguer curve) |
| `03_PC_duel_round_and_approach.md`, `_B.md` | the round's input | gains the three raw fields; §3's readings (taken on the half-score) are re-read after gate 2, as U5b §5 row 7 already orders |
| `10_DICE_one_score_two_roles.md` Edit B | `_opposition_of` returns the score | **restored** as written (U5a B4 had replaced "score" with "the pool") |

Layer 1 rows are graded in the proposal; none is edited or owed. Not read in full: `audits/10_DICE_audit.md`
and its addendum beyond the rows `U5a_DICE_owed_edits.md` carries; `proposals/U5b_PC_residue.md`,
`U5b_MB_*`, `U5c_SC_proceedings_residue.md`; `05_SC_playable_hearing_B.md` below its *Who decides* section;
`04` §A.2's provider row (cited through U5c's reading and marked so in the proposal).

## 9. Evidence log

Scratchpad: `/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/ONE_OPPOSED/`
(each script's output is the `.txt` of the same name). All `PYTHONHASHSEED=0`. Module scale: `wrapper.fight`
through the trace seam, with the helpers of `runs/PES_PC/lib.py` so the figures are comparable with
`audits/16_PESSIMIST_PC.md`. Forms were set by replacing `core.ob_from_defender` and `core.DMG_SCALE` for the
run; nothing tracked was written. Load average 1.7 to 4 on 4 cores.

| probe | what, size | used in |
|---|---|---|
| `olib.py` | the six obstacle forms, the two-sided arm (the defender's zero-mean dice noise added to the attacker's net), the per-exchange reader | — |
| `p1_grid.py` | 6 forms × 2 scales, 1,200 fights a cell (seeds 0–1,199), 300 traced for bands; 3 control rows at seeds 800,000 on | §4 P1 |
| `p2_skill.py` | 5 arms × 7 rank pairs × 1,000; mirror control at two seed sets; mirrors at ranks 0, 2, 5, 7, 12 × 4 arms × 1,000 (+200 traced); defence by rank, 600 traced a cell; attributes, 500 a cell | §4 P2, P3, P4 |
| `p5_social.py` | closed-form bands on the A-5/A-6 roll; control 200,000 seeded draws (seed 29); equals by rank; nine rank pairs; levels; extremes; two-sided roll 100,000 a cell | §5 |
| `p6_alts.py` | the neutralisation cut, the two-sided roll, the half-score at rank 7, 1,000 a cell; `blood` and `yield` terms 800 a cell | §4 P6 |

Reproduced from other lanes as a check on the instrument: the shipped mirror (3.35 turns, 3.20 blows
against the pessimist's 3.36 and 3.18); A-31's scale (4.60 / 4.60 / 45.0% against 4.60 / 4.58 / 43.9%); the
shipped skill curve at 3v2 and 4v2 (64.9 and 77.0% against `pD_skill.txt`'s 64.97 and 76.50%).

Limits, stated. One weapon and one armour (arming sword, light): the season's only fight
(`audits/16_PESSIMIST_PC.md` §1.2). No reading here is a balance claim across the roster; the roster sweep
belongs to U5b §5 row 5's batch. The argument's figures are the roll's own odds, not a realm reading: the
realm reading is `13_SC_calibration.md` step 4's, after the cast holds scores. The 1.07 scale is the
pessimist's seed, not a swept value. The two-sided arm in a fight is an equivalent-in-law construction on
the attacker's net, not a second draw path.
