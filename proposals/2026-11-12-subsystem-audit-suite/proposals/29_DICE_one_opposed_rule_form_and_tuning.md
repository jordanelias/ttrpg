# 29 · DICE — the one opposed-contest rule: its form, its one owner, its tuning and its gates (A-71)

## Status: PROPOSED (a decided plan for future execution; nothing here is executed by the authoring lane; not ratified by being written, `CLAUDE.md` §2)

Author: lane 29 (Fable), 2026-11-12. Read at `5c0a353`. Carries Jordan's A-71
(`unified/DECISIONS_ANSWERED.md`): *"make social contest and personal combat same...but I don't know how to
tune it so that we can extend fights and make better arguers win while also making someone's
aptitude/prowess allowing them to defend better without making it a big attrition"*. Bound by A-5, A-6,
A-7, A-8, A-12, A-25, A-26, A-31, A-59, A-72. Evidence and the rejected forms:
`audits/29_ONE_OPPOSED_RULE.md` (**AUD**). Reference only (`CLAUDE.md` §0.05).

Reconciled: 2026-11-12, wave 3 rewrite lane W3-1 — rows applied: `U3_CONFLICT_LEDGER.md` C3-L1 (the "Layer 1 rows graded" table gains `04` D-29, conforming through `U5a_DICE_owed_edits.md` §1's quantised margin; "no Layer 1 text is owed" now holds), `U1_OWNERS_AND_VOCABULARY.md` D-U1-08 (`faculties` → `scores` + `addends`: item 29-2 steps 2, 4, 6 and 8 and the edit table's row 5 read `defender.score`), `OWED_TO_UNIFICATION.md` §B (the edit table's row 3 rewritten to match item 29-2, which governs), `U1_GLOSSARY.md` *aptitude* / *prowess* (for a person the attribute is **talent** and the trained rank is **training**; prowess is a unit's), `U3_CONFLICT_LEDGER.md` §10 (J-29-01 answered by A-79: CLOSED), U3 §6.1–§6.2 (the two missing test files are written as the batch's first commits; the scratch `p1_grid.py` and `p7_scale.py` readings are carried by `tests/valoria/test_combat_opposed_rule_shape.py`, so no probe is written separately), item 29-5's round half completed from `03_PC_duel_round_and_approach_B.md` as reconciled (the rate rides on `DuelRoundInput.fighters`; the hearing half stays INCOMPLETE); `Depends on:` / `Lands in batch:` from U3 (C3-D4; §4.1 row 22). U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "fought scene" → "fight" (glossary *scene*); "ordinary score" → "untrained score" (glossary *untrained score*); "aptitude" for the attribute → "talent" (glossary *aptitude*, *talent*).

**Depends on:** `U5a_capability_home_and_two_inputs.md` Part A (B04) for row 1; Part B, `U5a_DICE_owed_edits.md` §1 and `U5c_SC_one_obstacle_form.md` steps 0–5 (B05) for rows 2–4, 8; `U5b_PC_rulings_in_the_fight.md` §5 rows 4–5 (B15) for rows 5–7, 9; `03_PC_duel_round_and_approach_B.md` (B16) and `05_SC_playable_hearing_B.md` (B24) for item 29-5.
**Lands in batch:** row 1 / item 29-1 in B04; rows 2–4 and 8 / items 29-2 (control) and 29-4 in B05; rows 5–7, 9 / item 29-3 in B15; item 29-5 in B30 (U3 §4.1 row 22, SPLIT).

It **supersedes three sentences** and adds no second system:
`U5a_capability_home_and_two_inputs.md` row B4 and row B5 (the operand: the opponent's *pool*), `U1` §4's row
*the opponent* (the same), and `U5b_PC_rulings_in_the_fight.md` §2 edit 4 (a second rate for the fight,
which A-71 supersedes by name). The two proposals carry a `Folded:` line; `U1` §4's row is owed the same
one-word amendment (pool to trained score) and was not edited by this lane. Every other edit of those files
stands.

## What it changes in `engine/season/` at runtime

At the control arm, nothing (`opposition_rate` 0.5 is today's half-score in both modules, byte for byte for
every score ≥ 0). At the live arm: every exchange of every fight is rolled against
`0.4 × the defender's trained score` where it was `score / 2` (1.0 becomes 0.8 at the season default), in
the combat calibration batch that already re-records every combat golden once (U5b §5 row 5); every social
and task roll is composed as `U1` §4 already orders, with its constant now named (the even line), in the
batch that already moves every seeded result once (U5a Part B). This proposal adds **no re-pin of its own**.

## The rule (decided)

```
opposed_ob(score, rate)  =  rate × max(0, score)                       # the one owner, engine/dice_engine/sigma_leverage.py
even_line(pool_add)      =  MU_PER_DIE × pool_add                      # same module; derived, never typed (2.4 at 6)

the argument, the task   ob = even_line + difficulty level + opposed_ob(opponent's trained score, or the untrained score) + hostile terms
the blow                 ob = opposed_ob(defender's trained score)
every roll               roll_net_continuous(pool) + net_boost(levels for − levels against, pool);   degree_from_net(roll, ob)
```

| the defender's … | enters as | size | ruling |
|---|---|---|---|
| **training** (the trained rank of the capability that opposes the verb; "prowess" is kept for a unit's quality, U1 glossary) | the obstacle | `opposition_rate` = `MU_PER_DIE` a point, read from the owner | A-26 |
| **base** (the `pool_add` dice everyone holds) | never as opposition. In an argument it is the even line the difficulty ladder stands on; in a fight it is spent by the module's defence layer (`modules/combat/wrapper.py:340-357`) and is in no obstacle | — | A-6, A-71 |
| **talent** (the attribute; "aptitude" is a capability kind, U1 glossary) | named levels against the roller, `per: mid`, under the soft cap (`M_MAX` 1.5σ). In a fight: the module's own sigma assembly (`wrapper.py:316-320`), no host term | `talent_level` = `minor` a step | A-7 |
| **wounds** | named levels: against the bearer when he rolls, for the roller when the bearer defends (combat's bilateral precedent, `combat_systems.py:1049-1050`). Never an obstacle term | `wound_level` per `wound_step` | A-8 |
| **circumstance** | favourable: levels for the roller. Hostile: non-negative obstacle terms | per `U5c_SC_one_obstacle_form.md` §2, §3 | A-25 |
| **seat** | the `office` level source | per U5c §3 | A-12 |

Nothing lowers an obstacle, in either module. No floor is applied to the blow's obstacle (a rank-0 defender
puts nothing in the way but his defence layer; a floor at `OB_MIN` would make ranks 0, 1 and 2 defend
alike, and the shipped realm lives there). In the social composer the even line is always present, so
U5c §2's `max(OB_MIN, …)` never binds and is left as written.

## The tuning (decided; every value has a control arm, and each gate re-reads it at landing)

| dial | owner | control | live | what it buys (AUD §4, §5) |
|---|---|---|---|---|
| `opposition_rate` | `engine/season/data/fixtures.py` (one fixture, both modules) | 0.5 | `MU_PER_DIE` | equals read alike at every rank: fight mirrors 4.28 to 4.33 turns from rank 0 to 12 (half-score: 4.33 to 5.88, undecided 0.5 to 4.1%) |
| the operand | `seam/wrappers/pool.py::score` | — | the trained score, no base, no practice addend | 0.1% undecided where the pool operand gives 49.7% |
| `pool_add`, `pool_floor` | fixtures (U5a B2) | 0, 0 | 6, 5 | the even line is 2.4 |
| `DMG_SCALE` | `modules/combat/core.py:168` (U5b §4) | 1.55 | 1.07 seed (a Success is one Wound Interval) | 3.20 to 4.50 blows; lead change 35.2 to 45.2% |
| the argument's difficulty ladder | `difficulty_ob` (`13_SC_tuning_tables.md` T1) | 0 / 1 / 2 / 3 | 0 / 0.5 / 1 / 1.5 **above the even line** | equals at `routine` fail 56.9 to 60.1% over ranks 0 to 7, inside `13_SC_calibration.md` C1; Success-or-better 22.2 to 30.1%, at C1's upper edge (0.30) at rank 7, which the calibration step reads |
| `talent_level` | fixture (U5a B2) | `None` | `minor` | one step of talent against: Failure 58.7 to 68.0%, Success-or-better 25.4 to 18.1% (rank-2 equals, `routine`) |

Read together at the live arm:

| target | reading | instrument |
|---|---|---|
| (a) fight length | 4.27 turns, 4.50 blows, lead change 45.2%, 0.1% undecided, 39.3% bloodless turns (shipped: 3.35, 3.20, 35.2%, 0.2%, 40.9%) | 1,200 fights, seeds 0–1,199; control seeds 800,000 on: 4.18, 4.50, 41.6%, 0.5% |
| (b) the better one wins | fight, felled shares: +1 rank 65.7 / 63.0%; +2: 78.0 / 75.2 / 74.3%; +4: 92.3 / 91.0%; equals 50.8 and 51.4%. Argument, share of decided exchanges: +1: 65.6 / 63.0%; +2: 77.9 / 73.9%; +4: 92.0 / 90.6%; equals 50% | 1,000 fights a cell; closed form checked against 200,000 seeded draws |
| (c) defence is real | per rank of the defender's training: 6 points off the attacker's wounding share (64.7, 58.2, 52.0, 45.8, 39.0, 27.5% against ranks 0, 1, 2, 3, 4, 6), 8 to 9 off his Overwhelming share, a sixth off his damage a roll. Per step of Agility: 6 points (52.8, 46.8, 40.9, 36.1%) | 600 and 500 traced fights a cell |
| (c) no big attrition | mirrors at ranks 0, 2, 5, 7, 12: 4.33, 4.28, 4.28, 4.30, 4.29 turns; undecided 0.5, 0.1, 0.2, 0.4, 0.5%; an exchange fails 11.8, 13.6, 18.2, 20.8, 24.9% (half-score at the same scale: 4.33 to 5.88 turns, 0.5 to 4.1% undecided, 11.8 to 35.5%) | 1,000 fights a cell; band shares from 200 traced fights |

## Exact edits, by owner (in landing order)

| # | owner | exact edit | lands in |
|---|---|---|---|
| 1 | `engine/dice_engine/sigma_leverage.py` | `opposed_ob(score: float, rate: float) -> float` returning `rate * max(0.0, float(score))`; `even_line(pool_add: float) -> float` returning `MU_PER_DIE * float(pool_add)`. Pure; no default for `rate` (a caller cannot skip the fixture, as `core.resolve`'s `ob` is required, ED-PC-0058). This is the function `10_DICE_capability_axiom_map.md` §G edit 5 names; its operand is fixed here as the trained score | U5a Part A row A6 (hash EQUAL) |
| 2 | `engine/season/seam/wrappers/pool.py` | `score(w, p, verb)` as U5a B1. Its opposing form (the `opposed_by` capability where the row names one) is what `_opposition_of` returns: **the trained score, never the pool** (replaces U5a B4's *"returns the opponent's pool"*); no practice addend; a person always has one (the untrained score) | U5a Part B |
| 3 | `engine/season/queries/inputs.py` | *(W3-1: matched to item 29-2, which governs.)* `SocialContestInput` carries `opposition_rate: float`, `pool_add: int`, `pool_floor: int` raw from the fixtures; `PersonalCombatInput` carries `opposition_rate: Optional[float] = None` (`None`: the module's own constant) beside `scores`, `addends`, `pool_add`, `pool_floor` (D-U1-08); `DuelRoundInput` (`03_PC_duel_round_and_approach_B.md`) carries them once, on its `fighters: PersonalCombatInput`. `fight_opposition_rate` (U5b §2 edit 4) **is not created** | U5a Part B; U5b §5 row 4 |
| 4 | `modules/social_contest/roll.py::obstacle` | `hard = even_line(inp.pool_add) + difficulty + opposed_ob(opposition if a person opposes else inp.pool_default, inp.opposition_rate) + Σ raw_i × step_i`, then U5c §2's bounds unchanged. `terms` gains the leading entry `("even", even_line)` so the terms still sum to `ob`; `rosters.yaml: obstacle_terms` gains the member `even` first; its host function in `sigma.py::OBSTACLE_TERMS` is the one that carries `pool_add` onto the record (so U5c §1's member-to-function pairing holds), and the value is derived in the module from that field and `MU_PER_DIE` | U5c §4 step 5 (the joint calibration step) |
| 5 | `modules/combat/core.py::ob_from_defender(defender, cfg)` | `return SL.opposed_ob(defender.score, cfg.get('OPPOSITION_RATE', OPPOSITION_RATE))` (the trained score, D-U1-08); the three call sites (`wrapper.py:213`, `:243`, `:331`) and `core.py:665` pass `cfg` (item 29-2 below has the full route). The docstring's *"Score/2"* and *"two ladders for one quantity"* paragraphs are replaced by one sentence naming the owner and A-71. `BASE_POOL`, `POOL_FLOOR` stay as the workbench's defaults (U5b §2 edit 3) | U5b §5 row 4 at the control rate (hash EQUAL) |
| 6 | `engine/season/data/fixtures.py`, `hole_register.yaml` | `opposition_rate`: one NUMBER row, grade `ruled` (A-26, A-71), sweep `0.5 / MU_PER_DIE / 0.3`, with the targets of this file as what it was set to. Flip to the live arm for the fight **first in U5b §5 row 5** (before the scale's sweep, so `DMG_SCALE` is swept on the obstacle it will ship with) and for the social roll at U5c §4 step 5 | as named |
| 7 | `modules/combat/core.py:168` | `DMG_SCALE = 1.07`: decided. An arming sword's Success against light armour is exactly one Wound Interval (9) for every scale from 0.99 to 1.08 (`core.strike` is deterministic; `p7_scale.py`), so U5b §4's rule is met without a further sweep | U5b §5 row 5 |
| 8 | `engine/season/tests/test_sc_calibration_targets.py` (`13_SC_calibration.md` edit 1) | the grid is stated on trained ranks 0, 2, 4, 7 (pools 6, 8, 10, 13), not on pools 2 to 8; "equals" is equal trained rank. Two rows are added: the even contest (`plain`, equal ranks: P(margin ≥ 0) within 0.005 of 0.5 at every rank) and the better-arguer curve (gate 6 below) | U5c §4 step 4 (red), 5 (green) |
| 9 | `re-derived, never by hand` | `engine/engine_params/combat_engine_v1.json` (`tools/export_engine_params.py`); the combat goldens and the armour reference, once, at the end of U5b §5 row 5 | as U5b §4 edit 3 |

No edit is made to `architecture/`. No `.md` under `systems/` is written. No new fixture is created: the
even line is derived, and the fight's second rate is withdrawn.

## How the battle's duel round and the hearing use it

- **The duel round inside a field (A-4, A-72).** `nested_entry("combat.round", depth=1, fx)` (U5b §1) runs the
  combat module's round entry; its exchanges call `ob_from_defender`, so a duel between two officers on a
  field is opposed by the same function at the same rate as a duel in a street. The one edit is row 3: the
  round's input carries the three raw fields, so the field passes numbers and composes nothing. The
  officers' scores are their trained `arms` scores from the one pool reader.
- **Orders and prowess in the field (A-59).** The obedience draw names `opposed_by: none`
  (`27_MB_A_command_and_the_obedience_draw.md:53`): nobody's rating opposes an order, so it is a task and
  reads the composer's *nobody opposite* arm (the untrained score through `opposed_ob`, on the even line). The
  melee pair is not opposed (C-U5b-03). So the rule has two sites in a battle, the duel round and the
  obedience draw's stand-in; any later contest of one commander's command against another's calls
  `opposed_ob` on the trained command score and composes no private rate.
- **The hearing** (`05_SC_playable_hearing_B.md`). `argue`: the mover's pool against
  `roll.py::obstacle` with `opposition` = the other side's `Speaker.score`, whose comment becomes *"what
  `opposed_ob` reads"*. `answer`: a roll with no person operand; its obstacle is the even line plus
  `answer_ob` as its difficulty, and the weights of the two exhibits arrive as `proofs` levels (U5c §3),
  never as a signed term. The closing draw and each ballot: the determiner's or the seat's roll through the
  same composer, the board entering as levels. A sitting's length is bounded by effort (that file's
  *How a sitting runs*, step 3), so the hearing's bound on rounds is structural.

## Gates (execution artifacts; each number is a target with its control, and the landing commit quotes the reading)

1. **Control.** With `opposition_rate` 0.5: `engine/tests/` combat goldens byte-equal; `build_realm(0..2)`
   season hashes EQUAL to the commit before.
2. **The fight's shape** (season-default mirror, death terms, 1,200 fights at seeds 0–1,199 and again at
   800,000 on, AUD's `p1_grid.py` shape): mean turns in 4.0 to 5.0; mean wounding blows ≥ 4.3; a lead change
   in ≥ 40% of decided fights; undecided ≤ 2%; bloodless turns ≤ 45%; an attack on an equal wounds in 45 to
   57% of rolls.
3. **The better fighter** (1,000 fights a cell, ranks 3v2, 4v2, 6v2, 5v4, 6v4, 7v5, 7v3): +1 in 60 to 70%,
   +2 in 72 to 82%, +4 in 88 to 95%; the mirror inside 50 ± 3 at two disjoint seed sets.
4. **No attrition by rank** (mirrors at ranks 0, 2, 5 and 7, the rank ceiling, 1,000 fights each; rank 12
   read beside them, not gated): the longest mean within 0.5 turn of the shortest; undecided ≤ 2% in every
   cell; an exchange's Failure share ≤ 25% in every cell.
5. **Defence is real** (attacker rank 2 and rank 5 against defenders from two below to four above, 600
   traced fights a cell): the attacker's wounding share falls at every step, by ≥ 4 points a rank between
   two below and two above; his Overwhelming share by ≥ 5.
6. **The argument** (exact, through `roll.py::obstacle` and `sigma_leverage.band_odds` after U5a-DOE §1; no
   draw): equal ranks at `plain` meet the obstacle 0.50 ± 0.005 at ranks 0, 2, 4, 7; at `routine`
   P(Failure) in 0.50 to 0.65 and within 6 points across those ranks; of exchange pairs in which exactly
   one side reaches Success, the better arguer is that side in 60 to 70% at +1, 72 to 82% at +2, 88 to 95%
   at +4 (the fight's windows, deliberately the same); one `minor` level against moves P(Failure) by ≥ 0.05.
7. **Both tails open.** No gated cell at probability 0 or 1; rank 7 against rank 0 in a fight is not 100%
   (`18_DETERMINISM_no_certain_matchup.md` owns the upset inside the fight; this gate reads its result).
8. **One owner.** Read at the two functions: `ob_from_defender` and `obstacle` hold no arithmetic on the
   opposing score but the call to `opposed_ob`; `git grep -n "opposed_ob" modules engine/season` shows the
   two module call sites and no third.
9. **`python tools/export_engine_params.py --check`** green after row 9.

## Falsifiers

- Equals drift: P(Failure) of an exchange between equals differs by more than 13 points between rank 0 and
  rank 7 in the fight (measured 9.0 at the chosen arm, 16.7 at the half-score, same scale), or by more than
  6 between ranks 0 and 7 in the argument at `routine`. Then the rate is not what flattens it.
- The two curves part: at any gap in gate 3 and gate 6 the fight's and the argument's better-one-wins
  shares differ by more than ten points. Then "the same" is false in the one place a player can see it.
- A fight mirror at any rank to 7 with more than 2% undecided, or more than 45% bloodless turns: the big
  attrition has arrived by this rule.
- The even line found in a fight's obstacle (observable: the mirror's undecided share near 29%), or absent
  from an argument's `terms`.
- A defender's rank that moves no attacker's wounding share; a wound or an attribute found as an obstacle
  term in either module; a favourable circumstance that lowers an obstacle; a hash that moves at the
  control arm.

## Hash movers

None at the control arm. Live: every fight and every combat golden (inside U5b §5 row 5's one
re-record); every graded social and task roll (inside U5a Part B's one re-pin). `terms` gains one entry on
every social Event that records it (U5c §4 step 2 is already a declared mover for that tuple).

## Dependencies and order

Row 1: after `01_CORE_tests_one_golden_owner.md`, with U5a Part A. Rows 2 to 4 and 8: with U5a Part B,
`U5a_DICE_owed_edits.md` §1 (the one sampler) and `U5c_SC_one_obstacle_form.md` steps 0 to 5. Rows 5 to 7
and 9: `U5b_PC_rulings_in_the_fight.md` §5 rows 4 and 5, with the rate's flip placed first in row 5. The
approach's coefficients (U5b §5 row 7), `03_PC_duel_round_and_approach_B.md` §3's readings and the E-B10 to
E-B14 readings U5b cites from `audits/03_PC_audit_addendum_B.md` (not opened by this lane) are swept after
gate 2 reads green, as U5b already orders. Lanes: DICE (row 1), IN and SC (2 to 4, 8), PC
(5 to 7, 9). Nothing waits on Jordan.

## Layer 1 rows graded (`skills/layer-conformance`, Lens B; rows opened at the line)

| row | reading | grade |
|---|---|---|
| `holonic_ARCHITECTURE.md` §27.2 (`:984-990`), *no second resolver, no auto-resolve formula, no fast path* | one sampler, one ladder, one opposition function for both modules; the fight's second rate is withdrawn | conforms; CONVENTION (Layer 1 itself: *"enforced by a person noticing"*) |
| `holonic` §27.4 (`:996-998`), *an attempt at `Ob > 2 × Pool` is refused* | the largest person-opposed obstacle at the rank ceiling is 2.4 + 1.5 + 2.8 = 6.7 against a floor pool's 10; reachable only with more than 3.3 of hostile terms, where the per-pool ceiling binds first | conforms; the refusal stays with the host adapter |
| `04_CODE_ARCHITECTURE.md` PART D row 30 (`:1057`), *one `seam/ladder`; subsystems return a `Margin`* | both modules grade by `degree_from_net`; the social module returns `Margin`; combat's end-state exemption (2026-09-03) is untouched | conforms; CONVENTION, as the row says |
| `04` `:777`, *a MARGIN, never a winner* | `opposed_ob` returns a number into an obstacle; no winner is derived from two scores | conforms |
| `04` §A.2, the provider row (not re-opened here; read as `U5c_SC_one_obstacle_form.md` records it) | each module composes its own obstacle from its typed input and imports the dice engine and the record types only | conforms, on U5c's reading |
| `CLAUDE.md` §0.05, §5 | the rate, the base and the floor are fixtures and one Python owner; the combat value crosses to the port through the exporter's `--check` | conforms |
| `04` PART D row 29 (`:1056`), *"`condition`, `stores`, `margin` are integers"*; `04:903` *"Fixed point for … `margin`"* *(added by W3-1, C3-L1)* | the gate readings are on continuous nets; the margin graded by the ladder is quantised once to integer milli-units by `U5a_DICE_owed_edits.md` §1 row 1 | conforms through U5a §1's quantised margin; STRUCTURAL for the sum |

No Layer 1 text is edited or owed by this proposal.

## For Jordan (one item; the tuning itself is decided above) — **CLOSED** by A-79 (*"same rule only"*: Option A, as taken)

**J-29-01 · Does "the same" reach the centre, or the rule?** Taken: **the rule** (ladder step 3:
`13_SC_calibration.md` C1 and the per-verb `difficulty` column already say an argument has a difficulty of
its own). It is listed because A-71's word could be read either way and the two are different games.

- **Option A (taken).** One opposition rule and one better-one-wins curve; the act's difficulty differs. A
  blow at an equal draws blood one time in two. An argument at an equal on a routine matter fails 59%,
  half-lands 16%, carries 25%. A position holds unless effort, evidence, favour or skill moves it.
- **Option B.** One centre as well: an argument at an equal carries as often as a blow wounds, about one
  time in two (the argument's rows sit one success *below* the even line). Positions change hands as
  readily as blood is drawn; `13_SC_calibration.md` C1 is rewritten; an equal's argument carries twice as
  often (25% to about 50%). The reverse (the blow at the argument's centre) is not offered: it is the measured
  attrition, 29 to 50% of fights undecided.

## Instructions to code it (workplan v12 batch items; `AUDIT_BRIEF.md`, the standing charge of 2026-11-12)

Five items. Each is written to be followed without re-deriving anything; where it names a symbol that does
not exist in the tree at `5c0a353` it says which proposal creates it. The edit table above is the summary;
**where the two differ, this section governs** (it fixes how the rate reaches the combat module, which the
table left as "the carried rate"). Tier is `CLAUDE.md` §10's; "lands it" is the lane and the agent role.

### Item 29-1 · the owner (hash EQUAL) — DICE lane · `valoria-author` on `sonnet` · cost: edit

1. `engine/dice_engine/sigma_leverage.py`, directly after `net_boost` (the block *Core σ-leverage
   primitives*), two pure functions:
   `def opposed_ob(score: float, rate: float) -> float: return float(rate) * max(0.0, float(score))` and
   `def even_line(pool_add: float) -> float: return MU_PER_DIE * float(pool_add)`. `rate` has no default.
   Docstrings name A-26 and A-71, and say: the operand is a trained score, never a pool.
2. New file `engine/tests/test_opposed_ob.py`, four tests:
   `test_opposed_ob_at_half_is_score_over_two_exactly` (scores 0 to 20 in halves, `==`, no `approx`);
   `test_opposed_ob_clamps_a_negative_score_to_zero`; `test_opposed_ob_refuses_a_missing_rate`
   (`TypeError`); `test_even_line_is_the_owner_mean_times_the_base` (`even_line(6) == dice_engine.MU_PER_DIE * 6`).
3. Run `engine/tests/test_sigma_leverage_parity.py`. It is expected green untouched (it calls functions by
   golden row, `_call(fn, args)`); if it enumerates the module's names, add no golden row and say so in the
   commit.

**Gate.** `python -m pytest engine/tests/test_opposed_ob.py engine/tests/test_sigma_leverage_parity.py -q`
green. **Control and falsifier.** No caller exists, so `headless --case NPC-088 --seasons 2 --seed 0` prints
the hash of the commit before; a different hash falsifies "no caller". **Hash movers.** None.
**Depends on.** Nothing. (It is the function `U5a_capability_home_and_two_inputs.md` row A6 schedules.)

### Item 29-2 · the fight reads the owner, at the control rate (hash EQUAL) — PC lane · `sonnet` · cost: edit

In this order:

1. `modules/combat/core.py`, beside `BASE_POOL`: `OPPOSITION_RATE = 0.5` with the comment
   *"control (today's half-score); flips to DE.MU_PER_DIE at item 29-3 (A-71)"*.
2. `modules/combat/core.py::ob_from_defender` becomes `ob_from_defender(defender, cfg)` and returns
   `SL.opposed_ob(defender.score, cfg.get('OPPOSITION_RATE', OPPOSITION_RATE))` (W3-1, D-U1-08: the trained
   score, carried as `PersonalCombatInput.scores`; never the addends). The docstring's
   *"Score/2 …"* opening and its *"two ladders for one quantity"* paragraph are replaced by: the owner
   (`sigma_leverage.opposed_ob`), the ruling (A-71), and that `cfg['OPPOSITION_RATE']` is an arm's override.
   The paragraph *"NO INSTANCE MODIFIER IS ADDED HERE"* is kept.
3. Call sites, each gaining `cfg` (in scope at all four): `modules/combat/wrapper.py:213`
   (`core.ob_from_defender(longer, cfg)`), `:243` (`shorter`), `:331` (`defender`);
   `modules/combat/core.py:665` inside `strike` (`ob_from_defender(defender, cfg)`).
4. `engine/season/queries/inputs.py::PersonalCombatInput`: `opposition_rate: Optional[float] = None`
   (`None`: the module's own constant), documented beside `scores` and `addends` (D-U1-08; they replace
   `faculties`).
5. `engine/season/data/fixtures.py`: `opposition_rate=0.5`, with its `[JUSTIFIED: hole_register …]` comment;
   `engine/season/hole_register.yaml`: one NUMBER row, the next free `H-` id by the register's own
   allocation, `site: Fixtures opposition_rate`, `grade: ruled` (A-26, A-71), `default: 0.5 (control)`,
   sweep `0.5 / MU_PER_DIE / 0.3`, `cite:` this file's targets and gates 2 to 6.
6. `engine/season/seam/wrappers/combat.py::combat_input` (`:197`): fills
   `opposition_rate=fx.get("opposition_rate")` beside `scores=` and `addends=` (where `faculties=` is today,
   `:229`).
7. `modules/combat/fight.py::fight` (`:55`): before the call at the `try:` block,
   `cfg = wrapper.CFG if inp.opposition_rate is None else dict(wrapper.CFG, OPPOSITION_RATE=inp.opposition_rate)`,
   and the call becomes `wrapper.fight(A, B, cfg=cfg, rng=rng, terms=terms, decide=turn_choice)`.
8. Tests changed: `tests/valoria/test_combat_ob_from_defender_consumers.py`, the five calls at `:65`, `:117`,
   `:156`, `:204`, `:225` gain `config.CFG`; `test_set_attr_faculty_7_reads_pool_13_ob_3_5_and_no_sigma_moves`
   keeps `(13, 3.5)` (the control). Tests added, same file:
   `test_the_fight_obstacle_is_opposed_ob_at_the_cfg_rate` (a fight with
   `cfg=dict(CFG, OPPOSITION_RATE=0.4)`, scores 2 and 3: every `roll` event's `ob` is `0.4 ×` the struck
   party's trained score; `assert checked >= 1`); and in `engine/season/tests/test_cr85_faculty_replaces_history.py`:
   `test_the_record_carries_the_opposition_rate_to_the_module` (a hand-built `PersonalCombatInput` with
   `opposition_rate=0.4`: the trace's `ob` values are `{0.8, 1.2}`; with `None`: `{1.0, 1.5}`).
9. Re-derive: `python tools/export_engine_params.py` (the `core` section gains `OPPOSITION_RATE`), then
   `python tools/export_engine_params.py --check`.

**Gate.** The two test files green; `engine/tests/` combat goldens byte-equal; `build_realm(0..2)` season
hashes EQUAL; `--check` green. **Falsifier and control.** A combat golden or a season hash that moves at
this item (the control is the commit before). **Hash movers.** None (the exported JSON gains one key; it is
an artifact, not a world hash). **Depends on.** 29-1. Independent of U5a and U5b's other rows; if U5b §2
edits 1 to 3 land first, `opposition_rate` joins their three fields in the same record.

### Item 29-3 · the flip and the scale (declared MOVER) — PC lane · `sonnet` for the edit, `opus` for the gate reading · cost: edit inside the calibration batch

This is the first step of `U5b_PC_rulings_in_the_fight.md` §5 row 5; the goldens, the armour reference and
the export are re-recorded once, at the end of that row, not here.

1. `modules/combat/core.py`: `OPPOSITION_RATE = DE.MU_PER_DIE` (derived; no literal).
2. `engine/season/data/fixtures.py`: `opposition_rate` reads `dice_engine.MU_PER_DIE` (imported from the
   owner; no literal), the hole-register row's `default:` updated with the reading of the gate below.
3. `modules/combat/core.py:168`: `DMG_SCALE = 1.07`. **This value is decided, not left to a sweep:**
   `core.strike` is deterministic, and an arming sword's Success against light armour deals exactly the
   Wound Interval (9) for every scale from 0.99 to 1.08, 10 at 1.10 and above, 8 at 0.98 (`p7_scale.py`);
   1.07 is the pessimist's measured seed inside that window. The comment at `:168` is restated:
   *"even Success = 1 WI at the season default kit (holds for 0.99..1.08); A-31"*.
4. New file `tests/valoria/test_combat_opposed_rule_shape.py`, marked `combat`, fixed seeds, arming sword and
   light armour, death terms, module scale (`wrapper.fight` with the trace seam); every test ends
   `assert checked >= <cells>`:
   - `test_a_success_is_one_wound_interval` (`core.strike(A, B, 'success', CFG) == B.wt.wi` for default fighters);
   - `test_season_mirror_length_blows_and_reversals` (score 2 both, seeds 0–1,199: mean turns in [4.0, 5.0];
     mean wound events ≥ 4.3; lead-change share of decided fights ≥ 0.40; undecided ≤ 0.02; bloodless turns
     ≤ 0.45; the attacker's wounds per roll in [0.45, 0.57]). Expected reading: 4.27, 4.50, 0.452, 0.001,
     0.393, 0.516;
   - `test_the_better_fighter_wins_on_the_stated_curve` (1,000 fights a cell, seeds 0–999; 3v2 and 5v4 in
     [0.60, 0.70]; 4v2, 6v4, 7v5 in [0.72, 0.82]; 6v2, 7v3 in [0.88, 0.95]). Expected: 0.657, 0.630; 0.780,
     0.752, 0.743; 0.923, 0.910;
   - `test_the_mirror_is_level_across_ranks` (ranks 0, 2, 5, 7; 1,000 fights each: longest mean turns within
     0.5 of the shortest; undecided ≤ 0.02 each; Failure share of rolls ≤ 0.25 each). Expected: 4.33, 4.28,
     4.28, 4.30; 0.005, 0.001, 0.002, 0.004; 0.118, 0.136, 0.182, 0.208;
   - `test_each_rank_of_defence_lowers_the_wounding_share` (attacker rank 2 against defender ranks 0, 1, 2, 3,
     4; 600 traced fights each: strictly falling, each step ≥ 0.04). Expected: 0.647, 0.582, 0.520, 0.458,
     0.390.
   The lead-change and wounds-per-roll readers are the ones in the scratchpad's `runs/PES_PC/lib.py::summary`
   and `runs/ONE_OPPOSED/olib.py::exch`; they are copied into the test file as private helpers (the
   scratchpad is not a dependency). Runtime about 60 to 90 s; it runs with `-m combat` and at the batch gate,
   not in an inner loop.
5. Text only: `tests/valoria/test_degree_ladder_single_owner.py:244` (the registry string naming
   `defender.history/2`) and the docstring of `engine/season/tests/test_cr85_faculty_replaces_history.py`
   (`:7`, `:13`) are restated to the owner and the rate; `test_set_attr_faculty_7_reads_pool_13_ob_3_5…` is
   renamed for and re-pinned to `(13, DE.MU_PER_DIE * 7)` (no typed 2.8: the product is 2.8000000000000003),
   said plainly in the commit.

**Gate.** The new file green with its readings quoted in the commit beside a second run at seeds 800,000
on (the control for sampling: expected 4.18 turns, 4.50 blows, 0.416). **Falsifier and control.** Any of
this file's five falsifiers; the control arm is `cfg=dict(CFG, OPPOSITION_RATE=0.5)` with `DMG_SCALE` 1.55,
which must reproduce 3.35 turns, 3.20 blows, 0.352 at the same seeds. **Hash movers.** Every fight;
every combat golden; `workbench/data/combat_armour_reference.json`; `engine/engine_params/combat_engine_v1.json`.
**Depends on.** 29-2; `03_PC_typed_outcome_one_door.md` (U5b §5 row 1), as row 5 already requires.

### Item 29-4 · the argument reads the owner on the even line — IN and SC lanes · `sonnet` · cost: edit inside U5a Part B and U5c step 5

This item edits functions that U5a and U5c rewrite in the same batch. It is stated against the tree as it
is and against their end state; the lander applies whichever form is present.

1. `engine/season/seam/wrappers/sigma.py::_opposition_of` (`:117`): the returned value is the subject's
   trained score. Against today's body: the `held` list keeps `_capability(person, verb)` and drops
   `_opposing_attribute(person, verb)` (A-7: the attribute is a level, not a score), and a person with no
   key returns `float(w.fixtures.get("pool_default"))` (the untrained score; never `None` for a person).
   Against U5a's end state: it returns `pool.score(w, person, opposing verb)`, not the pool.
2. `engine/season/queries/inputs.py::SocialContestInput`: `opposition_rate: float`, `pool_add: int` carried
   raw (U5a row A6 and B2 create both; this item fixes that the record carries them and that
   `obstacle_default` is replaced by `pool_default`, as U5c §2 orders).
3. `modules/social_contest/roll.py::obstacle` (`:141`): the first line becomes
   `ob = even_line(inp.pool_add) + difficulty + opposed_ob(inp.opposition if inp.opposition is not None else inp.pool_default, inp.opposition_rate)`,
   importing both names from `engine.dice_engine.sigma_leverage`; `difficulty` is `inp.difficulty`
   (U5c §1's field; `0.0` until it lands); the room's subtraction at `:142-143` is
   removed by U5c step 1b, not by this item. With U5c's `terms`, the first entry is `("even", even_line(...))`.
4. Data rows: `engine/season/rosters.yaml: obstacle_terms` gains `even` as its first member (U5c step 1a
   creates the roster); its entry in `sigma.py::OBSTACLE_TERMS` is the function that carries `pool_add`.
   `engine/season/data/fixtures.py: difficulty_ob` live arm `0 / 0.5 / 1 / 1.5` (T1, unchanged).
5. The wound's defending half (A-8), an amendment to `10_DICE_advantage_sources_for_the_arcs.md` Edit B:
   `_wound_levels(fx, operands)` returns `([level] * n_subject, [level] * n_actor)`, where `n_subject` is
   computed from `operands["subject_body"]` and `operands["subject_body_ceiling"]` by the same step and cap;
   `contest_input` adds those two operands when the subject is a person; `believed_input` leaves them out
   (another person's body is not the believer's to know without a claim).
6. Tests: `engine/season/tests/test_sc_calibration_targets.py` (created by `13_SC_calibration.md` edit 1)
   gains `test_equal_ranks_meet_a_plain_matter_half_the_time` (ranks 0, 2, 4, 7: `1 − band_odds(...)[0]`
   within 0.005 of 0.5), `test_the_better_arguer_wins_on_the_fights_curve` (the decided-pair share from two
   `band_odds` calls: 3v2 and 6v5 in [0.60, 0.70]; 4v2 and 7v5 in [0.72, 0.82]; 6v2 and 7v3 in [0.88, 0.95];
   expected 0.656, 0.630, 0.779, 0.739, 0.920, 0.906), and C3 and C4 restated on ranks: an opponent four
   ranks better at `routine` fails the actor in [0.75, 0.90] (expected 0.823, 0.809); one four ranks worse,
   at most 0.45 (expected 0.346, 0.351). `engine/season/tests/test_social_contest_module.py` gains
   `test_the_obstacle_is_even_line_plus_difficulty_plus_opposed_ob` (a hand-built record: `pool_add` 6,
   `plain`, opposition 2, rate `MU_PER_DIE`: `obstacle == even_line(6) + opposed_ob(2, MU_PER_DIE)`, which is
   3.2, and its `terms` sum to it).
   `engine/season/tests/test_sc01_obstacle_ceiling.py` is re-pinned by U5a-DOE §1 row 3 (the closed-form
   cap), not here.

**Gate.** The three files green; gate 6 above read from the first. **Falsifier and control.** Control: with
`opposition_rate` 0.5 and `pool_add` 0 the composed obstacle of every record in
`test_social_contest_module.py` equals today's. Falsifier: equal ranks at `plain` off 0.5 by more than
0.005 at any rank. **Hash movers.** Every graded social and task roll, inside U5a Part B's one re-pin.
**Depends on.** 29-1; `U5a_capability_home_and_two_inputs.md` rows A6, B1, B2; `U5a_DICE_owed_edits.md` §1
(`band_odds` as the closed form); `U5c_SC_one_obstacle_form.md` steps 0 to 5;
`13_SC_calibration.md` edit 1.

### Item 29-5 · the nested round and the hearing carry the rate — **round half complete (W3-1); hearing half INCOMPLETE**

*(W3-1.)* The round half, from `03_PC_duel_round_and_approach_B.md` §2 as reconciled: `DuelRoundInput.fighters`
**is** a `PersonalCombatInput`, so the rate, the scores and the addends ride there once and nothing is added
to `DuelRoundInput`; `modules/combat/fight.py::round` builds its `cfg` by item 29-2 step 7's line, reading
`inp.fighters.opposition_rate`. Test: `engine/season/tests/test_combat_module.py::test_round_opposes_at_the_record_rate`
(a hand-built round input with `opposition_rate` 0.4: every `roll` event's `ob` is `0.4 ×` the struck party's
score). Lands in B30 with the nested duel. The hearing half below stays as written.

The rule reaches both by construction, but the records it must be written on do not exist in the tree:
`DuelRoundInput` (`03_PC_duel_round_and_approach_B.md` step 1), `HearingInput` and `Speaker`
(`05_SC_playable_hearing_B.md`), and the field's `duel` window (`U5b_PC_rulings_in_the_fight.md` §1 edit 4).
What is fixed here, for those proposals' own batches: `DuelRoundInput` carries
`opposition_rate: Optional[float]` exactly as `PersonalCombatInput` does in item 29-2 and the round entry
builds its `cfg` by the same line; `Speaker.score` is the trained score `_opposition_of` returns and the
`argue` move builds a `SocialContestInput` whose `opposition` is that score; `answer` builds one with
`opposition=None`. **Missing, and why it cannot be completed here:** the files, line numbers, call sites
and test names of three unbuilt entries; they are owed by the closure lanes of those proposals
(U5b for the round, U5c for the hearing), each of which now carries a `Folded:` line naming the field.

### What is not carried as an item, and why

J-29-01 is a question, not an edit; at its taken answer nothing is coded beyond items 1 to 4. `U1` §4's
one-word amendment is prose and is the U5a closure lane's. The Perception lever's steepness (AUD §4, P4) is
`audits/16_PESSIMIST_PC.md`'s finding and has no edit here.

## NERS reading (E last)

- **N.** Without it the fight and the argument price a defender in two units, and the suite's written form
  breaks the fight. Top-down: one sentence (*his training is what stands against me, a point for a point*).
  Bottom-up: one function over one score. Lateral: fight, argument, hearing move, duel round. Vertical: a
  person's rank reaches a field through his duel. Diagonal: a seat, a wound and an attribute reach the same
  roll by the level channel and cannot be counted in the obstacle as well. Horizontal: the port carries one
  rate.
- **R.** Training, talent and injury are three different things about a person and read differently
  afterwards. Complete at the extremes: levels are soft-capped, the rank ceiling bounds the obstacle, the
  mirror is level at every rank, both tails stay open. With no player present, a master and a novice, two
  masters and two novices each produce a fight with a middle.
- **S.** One rate in the unit the dice are in; one ladder; one channel for everything that is not training.
  The fight keeps its defence layer and stops paying for the defender's base twice.
- **E, against that.** Two pure functions, one fixture, three carried fields; one fixture and one docstring
  paragraph retire; a player can say the rule.

## Cost class

Rows 1 to 6, 8: edits. Row 7 and the gates: inside the two calibration batches already planned. No build.
