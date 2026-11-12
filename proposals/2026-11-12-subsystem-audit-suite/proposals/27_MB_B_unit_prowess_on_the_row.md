# MB · a unit's own prowess: columns of its row, one function that composes its pool, and no baseline lent by its side

## Status: PROPOSED

Lane MB (the Record's key set is IN's; the carry leaf is PC's). Serves ruling **A-59**
(`unified/DECISIONS_ANSWERED.md:73`) clause (2): *"each unit within subformation will have its own martial
prowess based upon quality of troops and equipment and all impacted by subformation with tactics"*, with A-2
(a unit is a row of data) and A-60 (numbers act through frontage, depth and endurance, not the dice).
**Adds no mechanism.** It states, in one place, the arithmetic that five earlier proposals each change a part
of, names the one function that owns it, and removes the side-level baseline a unit can still borrow. Those
five are amended in place with a `Folded:` line and are not restated: `04_MB_unit_loadout_and_weapon_in_hand_B.md`
(the troop file, the arm in hand, the carry cost), `04_MB_cell_hierarchy_as_data.md` (ranks, files, bands),
`04_MB_cr12_linear_law.md` with `16_PESSIMIST_MB_partition_and_the_pair_rule.md` (the pool and the pair),
`04_MB_campaign_party_economy.md` (experience, arrears), `26_MASS_BATTLE_movement_and_fatigue_as_data.md`
(pace, fatigue). Audit: `audits/27_MB_COMMAND_AND_DYNAMIC_STRENGTH.md`. Read at `faf0cea`. Reference, not
mechanism (`CLAUDE.md` §0.05). No code is edited by this file.

## What it changes in `engine/season/` at runtime

At the seeds: nothing (the function is a consolidation, and every new column is at its neutral value). What
it makes true: a unit's dice, steadiness, armour, reach and endurance come from its own row and its troop
kind's row and from nowhere else, so two units of one army differ in a field because their rows differ. On
the **headcount path** (a side with no army Record) the single body today fights at a literal the side lends
it; that literal becomes a troop row with the same values, so nothing moves there either.

## The problem (opened at `faf0cea`)

- **The pool has three writers of quality and a side-level fallback.** `core/exchange.py::subunit_combat_pool`
  reads `atom.eff_power` and `atom.eff_discipline` (`:88`, `:124`); each falls back to the parent `Unit`'s
  value when the subunit sets none (`hierarchy/units.py:654-657`), and the season sets the parent to the
  literals 4 and 5 (`orderofbattle.py:75`; `massbattle.py:184-198`). On the army path a unit of a canonical
  kind takes its own preset (`Subunit.of_type`, `units.py:628-642`); on the headcount path the body is the
  side's literal.
- **Equipment is read for one bit.** The arm a kind carries decides melee or missile and nothing else; armour
  never becomes `dr` (`04_MB_unit_loadout_and_weapon_in_hand_B.md`, the problem, item 2: a pike line and a
  heavy-infantry line agree to six places in 440 of 440 fields).
- **The same quantity is composed in two functions** (`subunit_combat_pool` and `Unit.base_combat_pool`,
  `units.py:3004-3023`), which `04_MB_cr12_linear_law.md` step 2 already consolidates.
- **Nothing says what a unit's prowess is.** A designer reading the troop file after the five proposals land
  would find `power`, `discipline`, `morale`, `strength`, `armour`, `primary`, `secondary`, `ranks`, `pace`,
  `experience`, `raw`, `arrears`, `in_hand`, with their effects in five files.

## The resolution, decided

### 1. Where each term lives (data, one owner each)

| A-59's word | term | owner cell | read at |
|---|---|---|---|
| quality of troops | `power` (the kind's quality) | `references/troops.yaml: troops.<kind>.power` | the base term (§2) |
| | `experience` (0, 1, 2) | the unit row (`04_MB_campaign_party_economy.md` §1) | added to `power` at `orderofbattle._spec_for`, `power_per_step` a step |
| | `discipline` (steadiness) | the troop row; lowered one by the unit row's `raw` (`14_VERBS_MILITARY_D` Edit 1) and by `arrears` | the order term (§2); the stand draw; `obey`'s `unsteady` |
| | `morale` at the start | the troop row, moved by the side's stance rows (`MassBattleInput.stances`) | the morale level |
| | drilled cohort | the cohort person's `arms` rank (`14_VERBS_MILITARY_B_train.md` §1 item 3) | a step on `power`, at `_spec_for`, **when MB's read lands**; absent, zero |
| equipment | the arm in hand: `primary` or `secondary`, with its `class` | troop row, unit row override of `secondary`; state `Subunit.in_hand` | reach, support ranks, melee or missile (`…_B.md` §2, §4) |
| | `armour` tier | troop row | die-equivalents against the attacker's net (`16_PESSIMIST_MB_partition_and_the_pair_rule.md` edit 3); the rally step |
| | the load | `strength` against the masses carried | `(fatigue_factor, step_factor)` on the column ledger's drain and rest and on the step (`…_B.md` §5; `26_MASS_BATTLE_movement_and_fatigue_as_data.md`) |
| subformation | `ranks`, `files`, `shape`, `distribution`, `bands` | unit row, defaults on the troop row (`04_MB_cell_hierarchy_as_data.md` §2, §4) | frontage, support depth, fatigue damping, shock absorbed, the wrap resisted |
| tactics | `role` and its instructions, `stance`, `standing_orders`, `post` | unit row | the stance term, brace, yield, targeting; applied through `obey` (`27_MB_A`) |

Nothing in the table is new except the last column's statement of where it is read.

### 2. The arithmetic, in one function

`modules/mass_battle/core/exchange.py::prowess(atom) -> float` is the base-term function
`04_MB_cr12_linear_law.md` step 2 creates. After that proposal's step 3 and the one-ledger proposal's step 1:

```
quality  = troop.power + power_per_step * unit.experience  (+ the drill step, when read)
order    = clamp((5 - discipline) * 0.5, 0, 2)                    # today's `pen` (exchange.py:101), unchanged
prowess  = quality * REFERENCE_SIZE * POOL_QUALITY_SCALE - order  # dice; no headcount, no commander, no side factor

for one pair, one tick:
pool     = prowess * engaged_share(pair)            # the unit's cells in this pair, a cell in m pairs counting 1/m
           * YIELD_POOL_MULT   if yielding and not pocketed
           = 0                 on the tick it changes the arm in hand, and while it re-forms
levels   = morale + fatigue + stance (own and the enemy's) + ground - the enemy's armour
           + charge shock - brace recoil + (a missile arm in hand, hand to hand)        # summed, capped once
net      = roll_net_continuous(pool) + net_boost(levels, pool)
dealt    = K_LINEAR * frontage(pair) * PAY_PER_NET * max(0, net) * (1 + quality)
           * the struck cells' arc multiplier * the multi-side factor
```

- Every line but the first three is another proposal's, cited at its owner in the audit's §3 table. What this
  file decides is that **`prowess` is the only place a unit's quality becomes dice**, that it takes the unit
  and reads its row, and that nothing multiplies it by a value belonging to the side.
- **The commander is not in it.** Jordan's 2026-07-08 directive took the commander out of the pool
  (`config.py:533-552`), and A-59 lists troops, equipment and subformation as prowess's sources. A person's
  two inputs reach obedience, steadiness and rally (`27_MB_A` §4, §6), never the dice of a pair. An officer
  changes what his unit does and whether it stands; he does not add to its dice.
- **Numbers are not in it** (A-60). They are in `frontage(pair)`, in the depth that rests a column, and in how
  long the body lasts.
- **Subformation and tactics are not multipliers on prowess.** They decide which of the unit's cells are in
  the pair, how many ranks support them, which arcs are exposed and which levels apply. That is the sense in
  which prowess is "impacted by subformation with tactics": the same row fights differently four deep than
  one deep, braced than advancing.

### 3. No baseline lent by the side

- The season's constructors (`orderofbattle.build_unit`, `massbattle._weighted_unit`, `_person_unit`) give
  every `Subunit` its own `power`, `discipline` and `morale` from its troop row. `Unit.power` and
  `Unit.discipline` are not set by the season, and `eff_power` / `eff_discipline` raise, on a season-built
  unit, where they would have inherited. The inheritance stays for the harness until that code leaves
  (`04_MB_typed_outcome_and_one_path.md` §2).
- **The headcount path** (a side of persons at weight, no army Record) builds its one body as the bare kind
  `infantry`, which has no stat row, and so fights at the side's literals (`massbattle.py:176-198`, `:279-282`;
  the stand-in `light_infantry` at `:355` is used only when the other side has an order of battle). The troop
  file gains the row `infantry`, "an unmustered body", carrying today's literals transcribed (`power: 4`,
  `discipline: 5`; its morale still comes from the side's stance rows), and the constructor reads it. The
  move is hash-equal and the literal becomes a cell a designer can see and change.
- `_UNIT_POWER`, `_UNIT_COMMAND`, `_UNIT_DISCIPLINE`, `_SEASON_FORCE_POWER`, `_MVP_UNIT_COMMAND` are deleted
  (the command literal by `27_MB_A` §2).

### 4. What the player and the designer are shown

`modules/mass_battle/troop_types/table.py::readout(row) -> dict`: quality dice (`prowess` at full order),
steadiness, armour tier, reach class and support ranks of the arm in hand, pace, and the two carry factors,
each computed by the function the resolver calls. It is a description of one unit. **No function sums it
over an army**, and the surface shows no army strength: what an army can do against another is the estimate,
which is the resolver sampled (`04_MB_manager_battle_one_resolver.md` §8).

## Exact edits

| file (owner) | edit |
|---|---|
| `modules/mass_battle/core/exchange.py` (MB) | `prowess(atom)` as §2; `subunit_combat_pool` is `prowess × the yield and switch factors`; the `raw *= getattr(unit, '_friction', 1.0)` line is `27_MB_C`'s to remove |
| `modules/mass_battle/orderofbattle.py`, `massbattle.py` (MB) | §3: per-unit stats from the troop row on all three constructors; the five literals deleted |
| `modules/mass_battle/hierarchy/units.py` (MB) | `eff_power`, `eff_discipline`: a season-built subunit with no value of its own raises naming the unit |
| `modules/mass_battle/troop_types/table.py` (MB; created by `…_B.md` stage 1) | `readout` |
| `references/troops.yaml` (MB) | the row `infantry` (the unmustered body) carrying today's literals; `power_per_step` in the header |

## Gate (execution artifacts)

1. After CR-12 step 2 and this file's §3: `python3 tools/ci_golden_modes_check.py` digests equal, and 200
   seeded headcount fields equal the tree before, field for field.
2. **A unit is its own row.** An army of two heavy-infantry units, one at `experience` 2: over 200 fields with
   its same-run control, the experienced unit's share lost differs from its sibling's beyond the control's
   spread. Swapping which unit holds the experience swaps the reading.
3. **Nothing is borrowed.** A season-built unit whose troop row lacks `power` is refused at load by name.
   `git grep -n "_SEASON_FORCE_POWER\|_UNIT_POWER\|_UNIT_DISCIPLINE" modules/ engine/` prints nothing.
4. **Equipment reaches the dice.** The loadout proposal's stage 4 gates and the pair rule's armour row, read
   through `prowess`'s callers: raising a kind's `armour` one tier lowers the net its attacker rolls and
   leaves the kind's own `prowess` unchanged (asserted by calling both).
5. **Subformation is not a multiplier.** The same row at `ranks: 2` and `ranks: 6` returns one `prowess`; the
   two bodies' results differ (`04_MB_cell_hierarchy_as_data.md` gate 4).
6. `readout(row)['quality_dice']` equals `prowess` of a unit built from that row at Discipline 5, asserted by
   calling it; no caller of `readout` sums its values.

## Falsifier

A quality term read anywhere but `prowess`. A unit whose result changes when its sibling's row changes and
nothing else does. A function returning one number for an army's strength. A commander's or an officer's
score changing a pair's pool.

## NERS (definitions `CLAUDE.md` §0.06; E last)

- **N.** From the designer: one place says what makes a unit good. From the player: composition is a decision
  only if units differ for stated reasons. From the cell up: the engine already resolves per cell; the row is
  what a cell's troops are. Laterally: a person's kit and a unit's load are one carry function. Cut it and
  the five proposals each remain correct and nobody can say what prowess is.
- **R.** Customisation by row; veterans, raw levies, unpaid men and a second weapon all act through named
  terms; complete at the extremes (a unit with nothing set is its kind's row).
- **S.** One methodology for quality at every scale of the field; the readout and the resolver call one
  function.
- **E, against that.** One function and one readout; five literals and a fallback leave.

## Cost class

Edit (§2, §3; hash equal). `readout`: edit, after the troop file's loader.
