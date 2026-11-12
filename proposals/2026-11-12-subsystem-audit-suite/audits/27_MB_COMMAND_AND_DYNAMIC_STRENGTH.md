# 27 · Mass battle: command, a unit's own prowess, and an army whose strength is where it stands

## Status: REFERENCE (a design adjudication serving rulings A-59 and A-69; resolves nothing at runtime, CLAUDE.md §0.05; queues nothing)

## Read at: `faf0cea` (working tree, 2026-11-12)

Folded: 2026-11-12, rulings **A-77** and **A-78** (`unified/DECISIONS_ANSWERED.md:102-103`), Jordan's answers to this audit's §9. (1) **A-77**: the side-wide multiplier ships at zero when the first arm of the test's criterion passes; the small named level only if it fails. §3 row 13, §6 and §9 item 1 are amended to say so, and `proposals/27_MB_C_dynamic_strength_and_the_residual_chance.md` carries a `Folded:` line. (2) **A-78**: permanent losses are the dead, the captured and the deserters; the injured and those who fled and regrouped are recoverable, and a beaten commander who does nothing still recovers some of them. So this audit's own decision 19 (the fled return only when recalled, taken by ladder step 4) was **wrong and is withdrawn**: the unprompted return is the default, a drawn graded partial process, and a recall, a rally or a muster is a faster arm (ASSUMPTION, reversible). §0, §3 row 19, §7, §9 item 2 and §11 are amended; `proposals/27_MB_E_what_an_army_carries_back.md` carries the change. Still not established: how many of the fled desert and how many regroup, and the rate and window of return. (3) The order difference with `U5b_MB_rulings_in_the_field.md` §6 row 4 is reconciled on this audit's reading (the multiplier's test is read last), recorded by a `Reconciled:` line in `unified/U5_FINDINGS_CLOSURE_U5b.md`. §9 now holds no open item.

Jordan's ruling A-59 (`unified/DECISIONS_ANSWERED.md:73`), verbatim: *"B, and order friction is a function of
'command' which itself comes from a combination of learned skill/faculty and a function of social/mental
attributes.... but also, each unit within subformation will have its own martial prowess based upon quality
of troops and equipment and all impacted by subformation with tactics, and the overall army prowess as a
grand formation of these units is dynamic so a static fighting value is misleading as the overall placement
of units and their instructions relative to opponent is critical"*. B is option (b) of
`audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md` §7 item 2: lower the day's luck once order friction exists.
Ruling A-69 (`:90`) arrived during the pass and is folded as §7.

## 0. Verdict

**The ruling can be served by edits at owners that already exist, and the engine is closer to it than its
surface suggests: strength is already computed per pair and per contact cell from placement, facing, depth,
stance, fatigue and morale. What contradicts A-59 is three things laid over that machinery, and each is
small.** (1) One number drawn before contact multiplies every pool on a side for the whole field
(`modules/mass_battle/core/exchange.py:147`; drawn at `battle_loop.py:51-52` by
`orchestration.py:1725-1736`). At log-SD 1.1 a side it decides an even field: the higher draw wins 275 of
287 decided fields (`audits/16_PESSIMIST_MB.md:219-228`). It is the static side-wide value the ruling calls
misleading. (2) A fired order is applied by `setattr` with certainty (`core/contact.py:130-162`), so there is
no order friction for command to be a function of. (3) Command is the literal 4 on every side
(`massbattle.py:184-188`, `orderofbattle.py:75`), and a side with no army Record fights at a power and
discipline its side lends it. The plan, in five proposals:

- **`27_MB_A`**: command is one capability row with two inputs (trained rank as dice; Presence and Reason as
  levels), carried on the typed input for the commander and each unit's officer; an order takes effect by one
  draw for each person who has to pass it on, harder with distance, easier when prearranged; late, misread
  and not carried out are its lower bands.
- **`27_MB_B`**: a unit's prowess is columns of its own row composed by one function; no commander, no
  headcount and no side value in it.
- **`27_MB_C`**: nothing replaces the multiplier with another number. A six-arm test, with its criterion
  written first, tells removal from lowering; the chance left is the named draws, listed on the result.
- **`27_MB_D`**: what a commander decides, what he is shown, and what each order costs him, through the
  chooser's one interface.
- **`27_MB_E`** (A-69, A-78): the dead, the captured and the deserters are lost for good; the injured and
  those who fled and regrouped return in part, by a draw, whether or not their commander acts; fatigue is
  carried on the one ledger. Every magnitude there is marked not established.

Nothing here adds a resolver, a ladder, a capability scheme or a guard. The two items this audit put to
Jordan are answered (§9): the multiplier ships at zero when the test's first arm passes (A-77), and fled men
drift back unprompted, in part (A-78).

**Vocabulary** (the suite's, `proposals/04_MB_cell_hierarchy_as_data.md` §1): at the designer's surface
**army, unit, subformation, troops**; in code `Unit` (a side's army), `Subunit` (a unit), the subunit's
footprint, the cell. This file uses the designer's words and names the code object where it cites code.

## 1. What the code does today (opened at `faf0cea`)

### 1.1 The terms that are already dynamic

Every row was opened at the line given. This is the table `27_MB_C` §1 builds on.

| term | read at | from |
|---|---|---|
| who is in contact with whom | pairs with their cells, `core/contact.py::find_contacts`; each pair resolved in `orchestration.py::resolve_engagements` (`:710`) | deployment (`orderofbattle._place`), movement and targeting |
| a unit's base pool | `core/exchange.py:124`: `eff_power × eff_size × POOL_QUALITY_SCALE` less a discipline and a stamina term | the unit's own stats, else its side's (`hierarchy/units.py:654-657`) |
| the pool's share in one pair | `core/exchange.py:151-222`: troops in the contact cells plus depth-weighted support by the arm's reach | cell troop counts |
| flank and rear | per-cell arcs as a multiplier on casualties taken, and a factor for each further face struck (`orchestration.py:1320-1344`) | each cell's own facing |
| stance | a signed commitment on both rolls (`orchestration.py:1241-1253`) | the unit's `eff_stance`, set by role, order or strategy |
| brace, charge shock, recoil | `orchestration.py:1158`, `:1211-1220` | instructions, momentum, depth, discipline |
| fatigue | `orchestration.py:1231-1233` | the column ledger |
| morale | `orchestration.py:1229-1230` | per unit, per cell |
| ground | `orchestration.py:1257-1260` | one terrain row a field |
| frontage | `orchestration.py:1358-1361` | the engaged columns |
| the roll | `orchestration.py:1271-1275` | the module's own dice (leaving: U5b §1) |

### 1.2 The static side-wide values

| value | site | removed by |
|---|---|---|
| the multiplier `unit._friction` | `core/exchange.py:147` | `27_MB_C` §2, on its test |
| `Unit.power`, `Unit.discipline` lent to a unit that sets none | `hierarchy/units.py:654-657`; literals at `orderofbattle.py:75`, `massbattle.py:184-198` | `27_MB_B` §3 |
| `Unit.command` in every unit's erosion divisor and in `h_per_size` | `orchestration.py:2342-2343`, `:1151`; `hierarchy/units.py:2867` | `27_MB_A` §6 |
| command zero routs the whole army | `battle_loop.py:408-413` | a stand draw per unit (`26_…_rout_pursuit_and_giving_ground.md` §1) |

On the army path a unit of a canonical kind already takes its own power, discipline and morale
(`Subunit.of_type`, `hierarchy/units.py:628-642`). A statement that "every unit is power 4" would be false
there and true only of the headcount path.

### 1.3 Command and orders

Opened: `core/contact.py:66-162` (six trigger kinds; behaviours applied by `setattr`); `core/exchange.py:44-74`
(`clamp_command`, `derive_command` with weights 2 and 1, unused by any season path); `hierarchy/units.py:2740-2774`
(`Officer`); `armies.py:113-213` (span of control counts officers); `orchestration.py:2054-2106` (recall and
feint recognition roll `pursuer.command` against Ob 2); `seam/wrappers/pool.py:78-100` (`faculty`, the one
pool reader); `queries/inputs.py:205-245` (`MassBattleInput`: no capability field).

### 1.4 The aftermath

Opened: `loop/effects_combat.py:625-657` (casualties as `body`); `armyrecord.py:256-271` and
`seam/wrappers/mass_battle.py:192-214` (strength is assigned counts times the cohort's body share; "`tend`
restores it"); `verb_table.yaml:1565` (`tend` takes the whole headroom). So every loss is recoverable, in
full, with certainty, and no fatigue leaves a field.

## 2. Steelman, then the attack

**The multiplier's best case** (its own comment, `config.py:310-327`): pooled dice average out as numbers
grow, so a large advantage becomes a certainty; one latent draw per battle restores an uncertainty that does
not shrink with size, and it was fitted to a historical win-rate curve.

- *Attack 1, the cheapest observation.* The suite's control already ran: with the multiplier off an even
  field of 600 a side still splits 134 to 136 (`audits/16_PESSIMIST_MB.md:226-228`). The certainty it was built
  to cure lives in the pair rule (winner takes all within a pair), which
  `16_PESSIMIST_MB_partition_and_the_pair_rule.md` replaces. **Survives in part:** at 2 : 1 and above on
  today's pair rule the bare engine is near-certain (`16_PESSIMIST_MB_partition_and_the_pair_rule.md`, the
  problem, item 4: twice the men win 299 of 300 with the multiplier off), so removal must
  be tested on the new pair rule and not assumed. That is why `27_MB_C` §4 is a test.
- *Attack 2.* The curve cannot be re-read: no source for a win probability by force ratio was reached
  (`26_MASS_BATTLE_calibration_targets.md` T-9; audit 26 §6). **The steelman fails on its evidence**, not on
  its statistics.
- *Attack 3.* It is the same for a well-placed army and a badly placed one. **Fails against the ruling.**

**Certain obedience's best case:** an order is the player's decision, and a decision that randomly does not
happen feels like the game taking the controls; Unicorn Overlord and Football Manager execute instructions.

- *Attack.* The sources and three wargames put a battle's uncertainty of command on orders (MV E1, E3 to E5;
  WG K4, D2, L3), the standing rule names an obeyed effect with no roll, and A-59 names order friction.
  **What survives is a constraint on the design:** the odds must be shown before the order is given
  (`27_MB_D` §2), every missed order must be on the report (`27_MB_C` §3), and "keep doing what you are doing"
  is never drawn (`27_MB_A` §4).

**The suite's own earlier design** (`26_MASS_BATTLE_maneuver_orders.md` §1: the commander's Command, plus one
die if the unit has an officer). *Attack:* it reads one input where A-7 and A-59 give two, makes an officer
worth one die whoever he is, and has no distance. **Kept:** its site, its bands' sense, its table of kinds.
**Replaced:** its pool.

## 3. The decisions

| # | question | decision | ladder step | carried by |
|---|---|---|---|---|
| 1 | what command is | one capability row, `command`; dice from the trained rank, levels from two attributes | 1 (A-59, A-7), 4 (U1 §4) | `27_MB_A` §1 |
| 2 | which attributes | Presence (`attr.social.charisma`), the governing one, and Reason (`attr.mind.acuity`) | 4: the code's own `derive_command(charisma, cognition)` | `27_MB_A` §1 |
| 3 | their weights | equal, at U1's `talent_level`; the 2026-06-02 ratio of 2 : 1 is one cell away | 4 (U1 §4); the weights are tagged tunable at `config.py:528-529` | `27_MB_A` §1 |
| 4 | who rolls | each person who must pass the order on: the officer for a standing order; the commander, then the officer, for an improvised one | 5: one rule, two links, no table by rank | `27_MB_A` §3 |
| 5 | officers' ranks | not a number: an echelon is which rows a person's draw covers | 4: "one ladder ... at every echelon" (`armies.py:176-180`) | `27_MB_A` §3 |
| 6 | a seat's modifier | whole dice among the pool addends, the commander's only, read off the march's seat | 1 (A-12), 3 (U1 §3 item 6) | `27_MB_A` §5 |
| 7 | delay, misreading, refusal | Partial is late; Partial on a unit holding two signals is misread; Failure is not carried out, and for a restraint is the thing restrained | 3 (the sources), 5 | `27_MB_A` §4 |
| 8 | signal and distance | a prearranged signal carries the field; an improvised order pays a step a band of distance from the commander's post | 5; magnitudes not established | `27_MB_A` §4 |
| 9 | the commander in a unit's dice | no | 1: Jordan's 2026-07-08 directive; A-59's list of prowess's sources | `27_MB_B` §2 |
| 10 | what a unit's prowess is | `prowess(atom)`: quality times a reference size, less its disorder; numbers, subformation and tactics act through the pair, not through it | 1 (A-59, A-60), 4 (CR-12 step 2) | `27_MB_B` §2 |
| 11 | the headcount body's literal | a troop row, `infantry`, with today's values | 3 (`CLAUDE.md` §0.05: a fact where code reads it) | `27_MB_B` §3 |
| 12 | what replaces the multiplier | nothing | 1 (A-59) | `27_MB_C` §1 |
| 13 | removal or lowering | a test with a criterion; ship nothing before it; **zero when its first arm passes, the named level only if it fails (A-77)** | 1 (A-59's record; A-77) | `27_MB_C` §4 |
| 14 | the residual's form, if any | a capped, named level per side per bout | 3: D-34's option B as written | `27_MB_C` §5 |
| 15 | the report's `fortune` field | withdrawn; `report.draws` in its place | 2: its subject is retired | `27_MB_C` §3 |
| 16 | an unplayed commander's rule at a window | none in the module; absence, or the chooser | 3 (`CLAUDE.md` §10: scripting drift) | `27_MB_D` §4 |
| 17 | where loss is written | the unit row; the read moves with the write | 1 (A-69, A-2); `CLAUDE.md` §0.1 pt 1 | `27_MB_E` §2 |
| 18 | how the injured return | the world's motion draw, with rest, supply, place and the unit's state as terms | 1 (A-69), 4 (A-54) | `27_MB_E` §3 |
| 19 | how the fled return | **unprompted, in part, by the world's motion draw; those still gone at the window are the deserters; a recall, a rally or a muster brings more back or sooner (ASSUMPTION, reversible)**. This row first read "when recalled" by ladder step 4; Jordan ruled otherwise and that reading is withdrawn | 1 (A-78) | `27_MB_E` §3 |
| 20 | carried fatigue | a crossing on the row, turned into `entry_stamina` when the input is built | 4 (D-48) | `27_MB_E` §4 |

## 4. Gates (execution artifacts), by proposal

Each proposal's own list is the gate. The ones that carry the ruling:

- `27_MB_A` gates 2 to 5: an order is obeyed at once, late and not at all, each in some fields; the
  commander's score and each attribute move the share; distance lowers it; a second signal can be misread
  and a single one cannot.
- `27_MB_B` gates 2 and 5: two units of one army differ by their rows; ranks change the result and not the
  prowess.
- `27_MB_C` gates 1, 3, 4: the six-arm table with its four planted defects caught; placement and
  instructions each move the win share beyond the control's band.
- `27_MB_D` gates 1 and 3: the odds shown are the odds drawn; a forward post buys obedience and costs
  exposure.
- `27_MB_E` gates 2 to 6: no loss counted twice; some return and some do not; the dead do not; a second
  field in a round is entered tired.

No gate here is a guard, and none is asked to block a merge (`CLAUDE.md` §0.1 pt 5): each is a test in the
file covering the code it reads, or a row of the calibration instrument.

## 5. Falsifiers and declared hash movers

**Falsifiers** are in each proposal. The four that would show this audit's reading wrong: a win share of 0
or 1 after removal; a choice of `27_MB_C` reading 4 inside its sampling band in every arm; a commander whose
score moves no obedience share; an arm of the test whose draw counts equal another's.

| mover | where it moves | control that is hash-equal |
|---|---|---|
| the multiplier's removal (or the level) | every fought field at default flags, so every season hash with a field; `engine/tests/` goldens with a field; `bat.py`'s two legacy modes | none: re-recorded once with the calibration batch. `ci_golden_modes_check`'s three digests pin it off and do not move |
| `obey: on` | fields in which an order fires | `obey: off` |
| commander and officer records | fields with a commander among the side | `commanders: (None, None)` |
| `prowess` consolidation; the `infantry` row | none | by construction; gate 1 of `27_MB_B` |
| `report.draws` on the band Event | every fought field's Event, so `World.content_hash()` | none |
| `recuperation: on`; carried fatigue | army fields and the rounds after them | `recuperation: off`; `carry: off` |

## 6. Dependencies and landing order

Against `U5b_MB_rulings_in_the_field.md` §6. That file was rewritten during this pass to hand the
commander's inputs, the obedience draw and a unit's prowess to this lane (its §1 row 3), and its §6 row 4 now
places "the multiplier's three-arm test and the obedience draw" just after the sampler. **One difference,
named:** the instrument can be built there, but the reading cannot be taken there. On the present pair rule
the bare engine is a cliff, and the draws that are to carry the chance do not exist until row 4's last steps
and row 5. The test is read last, and the multiplier's value changes in one commit after it. Otherwise that
order stands:

| this plan's part | lands in | needs first |
|---|---|---|
| `27_MB_B` §2, §3 (`prowess`, no lent baseline) | row 4, as CR-12's step 2 | the troop file (row 3) for the `infantry` row |
| `27_MB_A` §1, §2 (the row, the record) | row 10, with U5a's CAP Part B | U1's home for capabilities |
| `27_MB_A` §3, §4 (`obey`) | row 5 | the one sampler (row 4); the manager proposal's §2, §4 |
| `27_MB_D` | after row 5 | CHAR's cells on payload values, for the NPC half |
| `27_MB_C` §4 (the test) | after rows 4, 5 and 10 | every named draw on; the calibration instrument's "results" block |
| `27_MB_C` §2 (the deletion) | one commit, after the test, at the value A-77 rules for the arm that passed | — |
| `27_MB_E` §2, §4 | after row 2 (the typed outcome) and the one-ledger proposal's step 3 | per-part outcomes |
| `27_MB_E` §1, §3 values | not before the source search, or Jordan's values | A-54's motion draw (WR); custody (PHYSICAL) |

Cross-lane edges: CORE and DICE (the capability row, `band_odds`, the keyed draw of A-30, on which the
flip-share reading rests; the even line of an unopposed task, which ruling A-71's lane,
`audits/29_ONE_OPPOSED_RULE.md`, restates and which `27_MB_A` carries as one number without restating); CHAR (the decider's scoring; believed pools); FA and the institutions kit (the
seat's modifier; the A-12 text); WR (the motion draw); SE (a cohort's dead; the ration debit); PC (the carry
leaf; the nested duel).

## 7. A-69: what an army carries back

Carried by `27_MB_E`. In short: a loss has a kind, read off what the field already returns (fight loss,
pursuit loss, the taken, each part's end state) by two season-side draws; the loss is written on the unit's
row, and strength is then read from that row alone; the injured return by the world's motion draw with rest,
supply, place and the unit's state as its terms; the fled return in part by the same motion with nobody
acting (A-78), those still gone when the window closes are the deserters, and a recall, a rally or a muster
brings more back or sooner; the dead, the captured and the deserters are permanent; fatigue is a crossing on
the row that becomes the entry share of a second field in the same round. It amends `16_PESSIMIST_MB_rout_has_two_exits.md`, `26_MASS_BATTLE_rout_pursuit_and_giving_ground.md`,
`16_PESSIMIST_MB_one_stamina_ledger.md` and `26_MASS_BATTLE_movement_and_fatigue_as_data.md` in place.

**Not established** in the tree's research, and so not quoted: the ratio of dead to injured; the rate and
span of recovery; how many of the fled desert and how many regroup; whether acting brings more back or
sooner (taken as yes, reversible); how long a season round is in the fiction (not read by this lane).
`27_MB_E` §5 gives the calibration orderings (T-11 to T-18) and §6 the source search.

## 8. Layer 1 conformance

Graded as `architecture/meta/04_CODE_ARCHITECTURE.md` §0 grades: STRUCTURAL (the shape cannot express the
violation), MECHANICAL (a check fails), CONVENTION (a reader). Nothing in Layer 1 is edited.

| row | what it requires | this plan | grade |
|---|---|---|---|
| `holonic_ARCHITECTURE.md` §27.2 | no second resolver, no auto-resolve formula, no fast path | every draw is inside `resolve_field`; `obey_odds` is the closed form of the same sampler for display, never an outcome; the estimate stays the resolver sampled | CONVENTION by the row's own text ("enforced by a person noticing"); the reach probe (`27_MB_C` gate 5) is its artifact |
| `04` §A.2, adapters row | a module takes typed input, holds no token, reads no `World` | `CommandRecord` and the `obey` constants arrive on `MassBattleInput`; the module imports the dice leaf only | STRUCTURAL (no token); MECHANICAL for imports (the subprocess import test `CLAUDE.md` §3 names) |
| `holonic` §44.3 | a wrapper never holds state, decides, resolves or drives a clock | `command_record` and `field_input` read and build; the injured's recovery is a motion step's draw, not the adapter's | CONVENTION |
| `holonic` §43 | attachment by registry row | no new composition row: `lose` and `restore` are ops of the existing `mass_battle.army` row | STRUCTURAL at boot |
| `04` §B.7 | rank supplies dice and gates nothing (amended by A-12; text owed) | a seat's modifier is whole dice among the addends; no rank table; nothing gated | STRUCTURAL as amended; conformant to the unamended row too |
| `04` §B.13, §G.3.1 | data a loader validates | the `command` row, the three use rows, `orders.obey`, `aftermath`, `fortune` behind exporters' `--check` and the loaders' refusals | MECHANICAL at load |
| `04` §C.5, the return | a `Margin` (narrowed for the field by A-3; text owed) | end state only; `report.draws` explains it | CONVENTION until the text lands |
| `04` §C.11 | the explanation contract | the draws that changed the end state are Observations on the band Event | MECHANICAL (`27_MB_C` gate 6) |
| `04` row for a unit (ED-IN-0306; A-2) | a unit is a row of a Record a person holds | `officer`, `absent`, `last_field` are columns; `commander_post` is a key of the Record | STRUCTURAL (no unit type exists to hold more) |
| A-11 | a capability never gates | `command` gives dice and levels; an untrained commander may order anything | MECHANICAL at load (U1 §3 item 5) |
| A-30 | one draw per key | every draw named in `27_MB_C` §3 is keyed by field, tick, unit and purpose | MECHANICAL (replay gates) |

One tension, named and not resolved: the keyed draw (A-30) is a precondition of the flip-share reading. If
the test is run before A-30 lands, the instrument must build its own per-purpose streams, and that builder
is test code, not engine code.

## 9. For Jordan

1. **If the test says the multiplier can go, does it go?** A-59 says lower, and its record says test removal.
   `27_MB_C` §4 states the criterion in advance. *(a) Ship zero* when the criterion's first arm passes: every
   reversal in a battle then has a cause the report names (an order that came late, a unit that broke on a
   charge, a wing that chased and did not return, the dice of a pair). *(b) Keep a small named level* even
   so: each side's fortune for each bout, capped with morale and fatigue and printed on the result; a
   well-executed plan can still lose to nothing a commander did, by a bounded amount. Recommended: (a) when
   the first arm passes, (b) only when the second does. Shipping zero overwrites a ruled magnitude
   (`ED-MB-0016`) one step past the word "lower", which is why it is asked.
   **ANSWERED, A-77: (a).** Zero when the first arm passes; the named level only if it fails.
2. *(Dropped. This item asked whether fled men return only when recalled or drift back, and recorded
   "recalled" as taken by the ladder.)* **ANSWERED, A-78**, by neither option as it was written: the dead,
   the captured and the deserters are lost for good; the injured and those who fled and regrouped return in
   part with nobody acting. The recalled-only reading is withdrawn everywhere it stood (§3 row 19;
   `27_MB_E` §3). What the ruling leaves unstated is taken, reversibly: acting brings more back or sooner.

Nothing is open. The talent weights (decision 3), the two-link chain (4), the commander's absence from
a unit's dice (9) and the owner of loss (17) are each answered above by a ruling or a precedent. Three
quantities remain **not established** and are parameters with controls, not questions for Jordan until a
source or a value exists: the share of the fled who desert, the rate of return, and its window.

## 10. Decisions folded (each edited file carries a `Folded:` line dated 2026-11-12 naming this audit; no finding of another lane was deleted)

| file | what was folded |
|---|---|
| `proposals/26_MASS_BATTLE_maneuver_orders.md` | §1's pool (Command, plus one for an officer) is replaced by the chain and the two inputs; distance and misreading added; its table of kinds kept as steps |
| `proposals/26_MASS_BATTLE_calibration_targets.md` | §3's last row ("read, not proposed") becomes the six-arm test; rows T-11 to T-18 |
| `proposals/26_MASS_BATTLE_rout_pursuit_and_giving_ground.md` | §4's "the field does not decide who among the hurt dies" has its season-side draw; the fled; the general's fall reads his post |
| `proposals/26_MASS_BATTLE_movement_and_fatigue_as_data.md` | `fatigue.entry.second_field` becomes the fallback; the carried value is the writer |
| `proposals/04_MB_manager_battle_one_resolver.md` | §6's `fortune` withdrawn for `report.draws`; §7's officer rolls; the window view's three fields |
| `proposals/04_MB_unit_loadout_and_weapon_in_hand_B.md` | where each of its terms meets `prowess`; the `infantry` row |
| `proposals/04_MB_cell_hierarchy_as_data.md` | subformation acts through the pair, not as a multiplier; `bands` sums `prowess` by cell |
| `proposals/04_MB_cr12_linear_law.md` | its step 2 function is `prowess`; its planted collapse loses its constant |
| `proposals/04_MB_campaign_party_economy.md` | `experience` enters at `prowess`'s quality; a unit's loss is on its row |
| `proposals/04_MB_playable_field_scenario.md` | the estimate is no longer blind to what decides; the decider reads `obey_odds` |
| `proposals/04_MB_typed_outcome_and_one_path.md` | the per-part outcome gains `stamina_left` and the end-state word; the army path's write moves to the row under the arm |
| `proposals/16_PESSIMIST_MB_rout_has_two_exits.md` | a part that runs has fled men; rally saves them; A-69 |
| `proposals/16_PESSIMIST_MB_one_stamina_ledger.md` | step 3's writers gain the carried value; `stamina_left` per part |
| `proposals/14_VERBS_MILITARY_D_the_order_of_battle.md` | the field-side draw is rolled on the officer or the commander by `27_MB_A`; `order_unit` carries `officer` and `commander_post`; `assign_troops` recalls the fled |
| `proposals/14_VERBS_MILITARY_A_movement.md` | a march's end carries the row's losses and fatigue |
| `proposals/14_VERBS_MILITARY_C_the_muster.md` | muster reads `assigned` after losses; absent men still count against the cohort |
| `proposals/U5b_MB_rulings_in_the_field.md` | its §1 row 3's carriers named; the one difference of order with its §6 row 4 (the test is read last) |
| `audits/04_MB_audit.md` | a dated head statement: F-MB-08 and §11 item 2 are answered by A-59 |
| `audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md` | a dated head statement: §7 item 2 is answered; B-3's owner |

Not edited: `proposals/04_MB_unit_loadout_and_weapon_in_hand.md` (superseded by its `_B`),
`04_MB_headcount_grade_and_scale.md`, `04_MB_squad_grid_of_named_characters.md`,
`26_MASS_BATTLE_cell_scale_and_time.md`, `26_MASS_BATTLE_aggression_and_land.md`,
`14_VERBS_MILITARY_B_train.md`: none assumes a side value or certain obedience.
`16_PESSIMIST_MB_partition_and_the_pair_rule.md` already names this lane's files in its own head.

## 11. Not established (so not quoted, and not built on)

Command delay as a number, and any reach of voice, horn or flag in metres (MV, "does not establish"). Any
magnitude for distance, misreading or refusal. A win probability by force ratio. The ratio of dead to
injured; recovery rates and spans; how many of the fled desert and how many regroup (that some return
unprompted is ruled, A-78). Whether a victor recovers his own
wounded. The length of a season round in the fiction. Every seed in the five proposals is marked as one.

## 12. Reading disclosure and evidence log

**No engine run was made by this lane.** Every measurement above is another suite lane's, cited at its file
and line, and was not re-run. Code opened at `faf0cea`: `modules/mass_battle/core/exchange.py` (whole),
`core/contact.py:66-176`, `config.py:270-470`, `:517-583` (by grep), `orchestration.py:740-1000`,
`:1107-1366`, `:1725-1736`, `:2054-2106` (by grep), `battle_loop.py:29-52`, `:400-420`,
`hierarchy/units.py:393-470`, `:628-690`, `:770-790`, `:925-940`, `:2740-2867` (by grep),
`troop_types/registry.py` (whole), `orderofbattle.py:60-180`, `massbattle.py:176-198`, `:262-282`, `:346-360`,
`armyrecord.py:1-60`, `:256-296`; `engine/season/seam/wrappers/pool.py` (whole), `mass_battle.py:192-216`,
`:463-468`; `queries/inputs.py:205-245`; `loop/effects_combat.py:625-662`; `engine/dice_engine/dice_engine.py:236-311`;
`sigma_leverage.py` (function list and `LEVEL_SIGMA`); `tools/export_battle_orders.py:1-40`;
`architecture/meta/04_CODE_ARCHITECTURE.md` §A.2; `architecture/holonic_ARCHITECTURE.md` §27.2, §43, §44.

Read in full: `AUDIT_BRIEF.md`, `unified/DECISIONS_ANSWERED.md` (to A-69), `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md`,
`audits/26_…`, the proposals `26_MASS_BATTLE_maneuver_orders`, `_calibration_targets`,
`_rout_pursuit_and_giving_ground`, `04_MB_cell_hierarchy_as_data`, `04_MB_manager_battle_one_resolver`,
`04_MB_unit_loadout_and_weapon_in_hand_B`, `04_MB_cr12_linear_law`, `16_PESSIMIST_MB_rout_has_two_exits`,
`16_PESSIMIST_MB_one_stamina_ledger`, `14_VERBS_MILITARY_D`, `U5b_MB_rulings_in_the_field`; the research
notes `mass_battle_movement_and_behaviour_grounding.md` and `mass_battle_wargame_models_grounding.md`.

Read in part (head, and the sections cited): `26_MASS_BATTLE_movement_and_fatigue_as_data` (to line 120),
`16_PESSIMIST_MB_partition_and_the_pair_rule` (to line 110), `14_VERBS_MILITARY_B_train` (to line 60),
`10_DICE_capability_axiom_map` (§C), `16_PESSIMIST_DICE_task_difficulty_and_throughput` (head),
`06_FA_office_capabilities` (head), `audits/04_MB_audit.md` (F-MB-08, §11, §14, §16 and the outline),
`audits/16_PESSIMIST_MB.md` (the friction lines, by grep),
`research/historical/mass_battle_casualties_and_results_grounding.md` (by grep).

**[SKIPPED]**, each named in the charge and not opened: `audits/04_MB_audit_addendum_B.md`;
`audits/14_VERBS_MILITARY.md`; `research/historical/mass_battle_gauge_grounding.md` and
`mass_battle_maneuver_sequences_grounding.md` (relied on through audit 26's rows, which cite them);
`proposals/04_MB_campaign_party_economy`, `_playable_field_scenario`, `_typed_outcome_and_one_path`,
`_headcount_grade_and_scale`, `_squad_grid_of_named_characters`, `26_MASS_BATTLE_cell_scale_and_time`,
`_aggression_and_land`, `14_VERBS_MILITARY_A`, `_C`, and the `10_DICE_*` files other than the two above
(each read at its head line or by grep for the fact cited, not in full); the mass-battle design set under
`.designs/`. A claim above that rests on one of these says which file it is from.

`git status --short` at the close: only files under this suite directory.
