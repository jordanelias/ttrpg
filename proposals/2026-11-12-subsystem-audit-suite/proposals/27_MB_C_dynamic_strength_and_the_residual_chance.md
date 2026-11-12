# MB · an army's strength is where it stands: the side-wide multiplier leaves, the named draws carry the chance, and one test tells removal from lowering

## Status: PROPOSED

Folded: 2026-11-12, ruling **A-77** (`unified/DECISIONS_ANSWERED.md:102`), Jordan's answer to audit 27 §9 item 1: *ship zero when the first test arm passes*; the small named level is used only if the first arm fails. So §4's criterion is no longer a recommendation awaiting his word: it is the rule. Its first arm passing licenses the deletion of §2 at zero, in the commit that carries the test's table; its second arm (§5's level) is reached only on the first arm's failure; its third arm (neither) is unchanged. This overwrites `ED-MB-0016`'s magnitude one step past "lower", on his word. The last section ("Conflict with a ruled item") and §5's third bullet are amended below to say so. Nothing else changes: the test is still run, the criterion is still written before the run, and nothing ships before the table exists.

Lane MB (the report's fields ride the typed outcome, IN's). Serves ruling **A-59**
(`unified/DECISIONS_ANSWERED.md:73`) clauses (3) and its answer B: *"the overall army prowess as a grand
formation of these units is dynamic so a static fighting value is misleading as the overall placement of
units and their instructions relative to opponent is critical"*; B is "lower the day's luck once order
friction exists", and the record adds that the calibrating lane "should test removing it". It decides
`audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md` §7 item 2 and `audits/04_MB_audit.md` §11 item 2 as far as
a lane can, and takes over the last row of `26_MASS_BATTLE_calibration_targets.md` §3, which read the
multiplier and proposed nothing. Audit: `audits/27_MB_COMMAND_AND_DYNAMIC_STRENGTH.md`. Read at `faf0cea`.
Reference, not mechanism (`CLAUDE.md` §0.05). No code is edited by this file.

## What it changes in `engine/season/` at runtime

Every fought field, once: the per-side multiplier stops being drawn. `MB_FRICTION` is on by default
(`modules/mass_battle/config.py:328`), so this is a declared hash mover wherever a field is fought at the
default flags, including the few `field.*` a natural season produces. The three digests of
`tools/ci_golden_modes_check.py` pin the multiplier off (`config.py:321-327`) and do not move. It lands in one
commit, after the named draws ship on, never before (B's own condition).

## The problem (opened at `faf0cea`; measurements are the suite's, cited)

- **The multiplier.** `battle_loop.py:51-52` draws, once per battle and per side,
  `math.exp(gauss(0, MB_FRICTION_SIGMA))` (`orchestration.py:1725-1736`), log-SD 1.1 (`config.py:331`; ruled,
  `ED-MB-0016`). `core/exchange.py:147` multiplies every unit's pool on that side by it for the whole field.
- **What it does.** In an even field of 600 a side the winner is the side with the higher draw in 275 of 287
  decided fields; where the draws differ by more than a factor of two (199 of 287) the higher draw wins 199 of
  199. The control: with the multiplier off the same field still splits 134 to 136 with 30 undecided
  (`audits/16_PESSIMIST_MB.md:219-228`). A field's result is known from the two draws 96 times in 100 (same
  file `:567`). Every row of the role menu, from pike to spearmen, holds 30 to 36 of 60 against a charge:
  "the role, the troop type and the direction of the charge are all inside one draw" (`:422`).
- **It is a static side-wide fighting value.** It does not move when a unit is placed, flanked, relieved,
  ordered or tired. It is drawn before any of those things exist.
- **It is not on the sampler** (A-5): a bespoke log-normal beside the one roll (`audits/16_PESSIMIST_MB.md:90`).
- **Its calibration cannot be re-read.** `config.py:317-330` cites a win-rate curve by force ratio; no source
  for a win probability by force ratio was reached by the suite (`26_MASS_BATTLE_calibration_targets.md` T-9;
  audit 26 §6), and the grounding it names sits in the hidden audit corpus.
- **Other side-wide fighting values**, found by reading every site that multiplies or divides by a `Unit`
  field: the inherited `Unit.power` and `Unit.discipline` (removed by `27_MB_B` §3); `Unit.command` in each
  unit's erosion divisor and the command-zero rout of a whole army (`27_MB_A` §6). The side's terrain dice
  (`orchestration.py:1257-1260`) are the ground's, not the side's, and stay (audit 26 §4: one terrain row a
  field is the right abstraction).

## The resolution, decided

### 1. Nothing replaces the multiplier with another number

An army's strength is not stored, not computed and not returned. What the ruling lists is already read by
the one resolver, per tick, per pair, per contact cell. The table is the answer to "what replaces it"; the
right-hand column is where each is read today, and the proposal that changes the read, if any.

| the ruling's term | what the resolver reads | where (at `faf0cea`) | changed by |
|---|---|---|---|
| placement of units against the opponent's | which cells of which units are in contact, as pairs | `core/contact.py::find_contacts`; deployment `orderofbattle._place`; movement and targeting in `hierarchy/units.py`, `core/contact.py::assign_targets` | formation rows and posts (`04_MB_cell_hierarchy_as_data.md` §3) |
| frontage | the engaged front of each side in the pair | `core/attrition.py::_lanchester_strength`, called at `orchestration.py:1358-1361` | a cell in `m` pairs counts `1/m` (pair rule, edit 4) |
| depth | ranks behind the contact rank, by the arm's support ranks; depth damping a column's fatigue; depth absorbing shock and resisting a wrap | `core/exchange.py:188-222`; `config.py:359`, `:372-373`, `:401` | ranks and files as data; support ranks from the arm's class |
| flank and rear exposure | each struck cell's arc as a multiplier on what it takes; the number of faces a body is struck on | `orchestration.py:1320-1344` (`_octagon_cell_mods`, `_compute_atom_sides`) | the stand draw is called on first flank or rear contact (`26_…_rout_pursuit_and_giving_ground.md` §1) |
| instructions in force | each unit's stance as a signed commitment on its own and its enemy's roll; brace; yielding; the arm in hand; the order queue | `orchestration.py:1241-1253`, `:1211-1220`; `core/exchange.py:139-140`; `core/contact.py::check_orders` | orders take effect through `obey` (`27_MB_A`); `in_hand` (`…_B.md` §4) |
| fatigue | the engaged columns' stamina as a level | `orchestration.py:1231-1233` | the one ledger, entered tired, drained by speed and load |
| morale | the unit's morale as a level; a cell's own break; a neighbour's pull | `orchestration.py:1229-1230`; `config.py:111-112`, `:334` | the stand draw |
| each unit's own prowess | the base term | `core/exchange.py:124` | `prowess(atom)` (`27_MB_B` §2) |
| chance | the roll of each pair, each tick | `orchestration.py:1271-1275` | the one sampler (U5b §1) |

So the army's strength at any tick is the set of pairs it is in and what each pair's two units bring to it.
Move a unit, turn one, tire one or change its orders and the set changes; nothing else needs to.

### 2. The edit

- `core/exchange.py:141-147`, `orchestration.py:1725-1736`, `battle_loop.py:44-52`, `config.py:310-331`:
  the multiplier, its draw, its two constants and its `__all__` entries are deleted **in the commit the test
  of §4 licenses, and with the value that test's criterion selects** (§5). Until then nothing here edits
  `MB_FRICTION_SIGMA`.
- `tools/ci_golden_modes_check.py`'s `FIELD_PINS` loses the pin with it; `systems/mass_battle/sim/bat.py`'s
  two legacy modes, which did not pin it (`config.py:324-327`), stop differing for that reason.
- `04_MB_cr12_linear_law.md`'s gate uses `MB_FRICTION_SIGMA=4` as its planted collapse; with the constant
  gone that plant becomes the fortune level's seed set to its maximum, or, if no residual ships, a planted
  `PAY_PER_NET` of zero. The owner of that gate picks; it is named here so the deletion does not strand it.

### 3. Where the chance in a field is, after

Every one is on the one sampler and the one ladder, inside the one call, keyed (A-30), and listed on the
result.

| draw | once per | odds from | proposal |
|---|---|---|---|
| a pair's roll | pair, tick | the two units' prowess, engaged share and levels | U5b §1; the pair rule |
| obedience | order, link | the issuing person's command; distance; steadiness | `27_MB_A` |
| the stand | shock event, unit | Discipline; the shock's kind | `26_…_rout_pursuit_and_giving_ground.md` §1 |
| a body's breakpoint | cell, bout | the ruled band (0.15 to 0.30) | built; unchanged (A-61) |
| hold or chase | broken opponent, unit | Discipline; its standing order | same file §3 |
| rally, recall | end of field; lull | the commander's command; the troops' armour | `16_PESSIMIST_MB_rout_has_two_exits.md`; `27_MB_A` §6 |
| pursuit, and the taken | pursuing body | its prowess | same; `26_…` §4 |
| a nested duel | officers in contact, window | personal combat's | `U5b_MB_rulings_in_the_field.md` §3 |
| the feint's three draws | feint | Discipline; command | `26_MASS_BATTLE_maneuver_orders.md` §3 |

**The report.** `FieldOutcome.report.draws: ((tick, side, unit, kind, band), ...)`, written by one
`trace_event('draw', …)` at each of those sites but the pair's roll and the cell breakpoints (which are
summarised per unit per bout: nets above and below zero; cells broken). This **replaces** the `fortune:
(word_a, word_b)` field of `04_MB_manager_battle_one_resolver.md` §6, which disclosed the multiplier and has
nothing to disclose once it is gone. A-59's record: "the remaining chance in a field is the sum of those
named draws, reported on the result".

### 4. The test that separates removal from lowering

Run on the tree **after** the field calibration batch and the orders batch
(`U5b_MB_rulings_in_the_field.md` §6 rows 4 and 5) and with commander records supplied (row 10), because
before them the named draws do not exist and the reading would be of the old pair rule. `PYTHONHASHSEED=0`;
the same seeds in every arm; n at least 400 a scenario; the scenarios and constructors of
`26_MASS_BATTLE_calibration_targets.md` §2, which are the season's own.

**Arms.**

| arm | multiplier log-SD | named draws (`obey`, `stand_draw`, pursuit and rally) | fortune level (§5) | what it is |
|---|---|---|---|---|
| K | 1.1 | off | off | today, on the new pair rule: the control |
| A | 1.1 | on | off | audit 26's option (a) |
| L | 0.55 | on | off | lowered |
| R | 0 | on | off | **removed** |
| R0 | 0 | off | off | the bare engine: how much chance the pairs' dice alone carry |
| F | 0 | on | 0.25, and 0.5 | a small named level in place of the multiplier |

**Readings**, each with its same-run control.

1. **Not certain** (calibration T-7): every scenario's win share lies strictly inside (0, 1).
2. **Upsets**: the smaller side's share of decided fields at 1 : 1 (which must be side-fair within the sampling
   band), 3 : 2, 2 : 1 and 3 : 1 on a frontage that fits both. Reported beside `config.py:317`'s cited band as
   a flag, never as a target: no source for it was reached.
3. **Whose draw decided it: the flip share.** For each source `s` of §3's table and for the multiplier or the
   fortune level, re-run each field with the draws of `s` alone re-keyed and everything else fixed, and count
   the fields whose end state changes. `F_s` is that share. This is what A-30's keyed draw makes possible:
   one purpose is re-keyed and no other draw moves. In arm R the multiplier's flip share is zero by
   construction, and the instrument must show it.
4. **Do choices show:** five paired comparisons, each a choice against its mirror, win-share shift against two
   standard errors of the control: the envelopment doctrine against `balanced`
   (`26_MASS_BATTLE_maneuver_orders.md` gate 4); a commander at score 5 against 0; a flank detachment against
   none (`16_PESSIMIST_MB_partition_and_the_pair_rule.md`); a side entering at half stamina
   (T-8); a pike line against heavy infantry on the grid arm.
5. The ten rows of `26_MASS_BATTLE_calibration_targets.md` §1, in every arm.

**The criterion, written before the run and not edited after it.**

- **Remove (ship arm R)** if, in R: reading 1 holds in every scenario; in reading 2 the even field is side-fair
  and the smaller side at 2 : 1 wins a share above zero; and all five comparisons of reading 4 exceed their
  band.
- **Lower to a named level (ship arm F at the smaller seed that passes)** if R fails reading 1 or 2, F passes
  them, and reading 4 still passes in F with `F_fortune` below the sum of the flip shares of obedience, the
  stand and hold-or-chase.
- **Neither** if no arm passes readings 1, 2 and 4 together. Then the named draws are mis-sized: that is a
  finding about their seeds, reported with the table, and it is **not** a ground for keeping the multiplier.
- **What tells removal from lowering.** Arm L against arm R on readings 1 and 2, same seeds. If no row differs
  beyond the sampling band, the residual does no work the named draws do not already do, and removing it
  loses nothing (the cut test of N: remove it and see what worsens). If a row does differ, the difference is
  exactly what the residual is for, and arm F is asked whether a capped, named level can do it. Arm A against
  arm K shows what order friction adds while the multiplier still swamps it; R0 against R shows how much of
  the chance is the named draws and how much the pairs' dice.

**Controls against a fake reading** (`CLAUDE.md` §0.1 pts 3, 4; §7's warning on identical arms).

- The arms must differ in what ran: the count of multiplier draws consumed is 2 a field in K, A and L and 0
  in R, R0 and F, asserted from the draw trace, not from the flag.
- Planted defects, each of which a named reading must catch: the multiplier left at 1.1 inside arm R (reading
  3 shows a non-zero multiplier flip share); `obey` returning Success at every seed (`F_obey` is zero and
  `27_MB_A` gate 2 fails); the fortune level applied to one side (reading 2's side-fairness fails); the
  winner's and loser's seeds swapped between arms (the same-seed pairing shows no field in common).
- Two runs at the same seeds print the same table.
- No band of `26_MASS_BATTLE_calibration_targets.md` is edited in the commit that changes the constant (that
  file's own falsifier).

**The instrument** is the "results" block that file adds to `tests/sim/gauge_mb.py`, with the arms as a
parameter and reading 3 as one added function. It writes nothing tracked and gates no merge.

### 5. What may stay: a named level, and only if the criterion asks for it

If arm F ships: `fortune` is one signed level per side **per bout**, drawn on the scoped RNG at the bout's
start as a normal value in sigma units with spread `fortune.sigma`, added to that side's levels in every pair
and capped with them by the sampler's one soft cap (`engine/dice_engine/sigma_leverage.py::soft_cap`, ceiling
1.5). It is listed in `report.draws` by name. Data: `deployment.fortune: {sigma: 0}` in the troop file's
header, where zero is removal.

- It differs from the multiplier in four ways: it is bounded with every other level; it is drawn again each
  bout, so it is not the day's; it adds to a roll and does not scale a pool; it is on the result.
- It is still a value belonging to a side and not to where anything stands. That is why it ships only on the
  criterion's second arm. Jordan has ruled it so (A-77): zero when the first arm passes, this level only if
  it fails.
- This is the form D-34's option B was written in ("a signed amount of 'fortune of the day' that enters
  through the same capped channel as morale and fatigue, and is reported afterward",
  `unified/DECISIONS_FOR_JORDAN.md`, D-34).

## Exact edits

| file (owner) | edit |
|---|---|
| `tests/sim/gauge_mb.py` (MB) | the arms and reading 3, in the "results" block of `26_MASS_BATTLE_calibration_targets.md` §2 |
| `modules/mass_battle/core/exchange.py`, `orchestration.py`, `battle_loop.py`, `config.py` (MB) | §2's deletion, in the licensed commit |
| `modules/mass_battle/` draw sites (MB) | one `trace_event('draw', …)` each |
| `engine/season/queries/inputs.py::FieldOutcome` (IN) | `report.draws`; `fortune` withdrawn |
| `engine/season/loop/effects_combat.py::_eff_march` (IN) | writes the draws that changed the end state as Observations on the band Event |
| `references/troops.yaml: deployment.fortune` (MB) | only if arm F ships |
| `tools/ci_golden_modes_check.py` (MB) | the pin removed with the constant |
| `registers/editorial_ledger_mb.jsonl` (MB) | a superseding row on `ED-MB-0016` citing A-59, A-77 and the test's table, in the same commit |

## Gate (execution artifacts)

1. The instrument prints the six arms by five readings with n, band and control for each row, and the four
   planted defects are each caught by the reading named for them.
2. After the licensed commit: `git grep -n "_friction\|MB_FRICTION" modules/ engine/ tools/ systems/` prints
   nothing; a field's draw trace holds no draw whose key has no unit and no purpose.
3. **Placement decides.** Two equal armies, same rows, same seeds; one deploys by the `line` formation and one
   by `refused_flank` against a wider enemy: the win shares differ beyond the control's band, and both lie
   inside (0, 1).
4. **Instructions decide.** The same two armies, one with its centre ordered to `yield` and its wings on a
   signal, against the same army with no orders: reported with the share of fields in which the signal was
   late or missed, which is above zero.
5. **One resolver.** No function under `modules/mass_battle/` is entered by a played field and not by a
   delegated one (the reach probe of `04_MB_manager_battle_one_resolver.md` gate 7), and none takes or returns
   a side's strength: `git grep -n "army_strength\|side_strength\|force_ratio" modules/mass_battle engine/season` prints nothing outside the instrument.
6. **End state.** Every field of the run folds to `Won`, `Lost` or `Drawn` through `seam/ladder.py::field_degree`
   from `routed` and `conceded` alone; `report.draws` is non-empty whenever a draw changed which side broke.
7. Seasons: `python tools/m1_acceptance.py --summary` runs; every seeded golden that includes a fought field
   is re-recorded once, said plainly in the commit, with the calibration batch's.

## Falsifier

After removal: a scenario whose win share is 0 or 1; an even field that is not side-fair; a choice of
reading 4 inside its band; a multiplier flip share above zero. Before it: a criterion edited after the
table was printed; an arm whose draw counts equal another's; the constant changed in a commit with no table.

## NERS (definitions `CLAUDE.md` §0.06; E last)

- **N.** Top-down: Jordan's word that a static value is misleading. Bottom-up: the engine computes strength
  per cell and then multiplies it by one number. Lateral: every other contest in the game reports what
  decided it. Vertical: a commander's season acts (composition, orders, officers) reach the result.
  Diagonal: the estimate becomes worth showing, since the thing it cannot see is gone. Horizontal: both sides
  alike. Cut the multiplier and, by the control already measured, an even field still splits; what dies is
  the reversal with no cause.
- **R.** Strategy in where to stand and what to order; with no player, battles turn on a wing that went
  early or a line that gave ground, and the record can say so. Complete at the extremes: reading 1 is the
  standing rule's own test.
- **S.** One sampler; one ladder; chance at the sites where the fiction has it; the two modes are still one
  call.
- **E, against that.** A draw, two constants and a report field leave; one list arrives; one instrument
  function is added to an instrument that exists.

## Cost class

The test: small build (one function in one block). The deletion: edit, in the calibration batch's
re-record. The level, if shipped: edit.

## Conflict with a ruled item, named

`ED-MB-0016` (the multiplier, log-SD 1.1; closed again at `ED-MB-0080`) is a ruled magnitude. A-59 licenses
lowering it and asks for removal to be tested. Shipping zero goes one step past the word "lower", and that
step is now ruled: **A-77**, zero when §4's first arm passes, the named level of §5 only if it fails. The
superseding ledger row on `ED-MB-0016` cites A-59, A-77 and the test's table. This file still ships nothing
before the table exists.
