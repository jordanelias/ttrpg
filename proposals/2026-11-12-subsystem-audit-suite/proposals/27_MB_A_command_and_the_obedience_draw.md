# MB · command: a capability of the commander and his officers, and the draw by which an order takes effect

## Status: PROPOSED

Lane MB (the capability rows and the pool reader are CORE's and DICE's surface, U1; the seat's modifier is
FA's and the institutions kit's; the chooser's side is CHAR's and is `27_MB_D_the_commander_as_chooser.md`).
Serves ruling **A-59** (`unified/DECISIONS_ANSWERED.md:73`) clause (1): *"order friction is a function of
'command' which itself comes from a combination of learned skill/faculty and a function of social/mental
attributes"*. **Extends, and does not replace:** `U5b_MB_rulings_in_the_field.md` §1 rows 3 to 5 (the
commander's record and the `command` capability) and `26_MASS_BATTLE_maneuver_orders.md` §1 (the obedience
draw), both amended in place with a `Folded:` line. Audit: `audits/27_MB_COMMAND_AND_DYNAMIC_STRENGTH.md`.
Read at `faf0cea`. Reference, not mechanism (`CLAUDE.md` §0.05). No code is edited by this file.

## What it changes in `engine/season/` at runtime

Nothing for a side with no orders, no officers and no commander record: that is today's field (`obey: off`
and `commanders: (None, None)` are the controls and are hash-equal). With them: (1) every order that fires in
a field, from any source, takes effect by a draw whose dice are the issuing person's trained `command` and
whose levels are his Presence and his Reason; (2) the draw is harder with distance from the issuer and easier
for an order that was prearranged; (3) the field's result lists each such draw and its band. No natural
season fights an army field today (`audits/04_MB_audit.md` F-MB-03), so no shipped season moves.

## The problem (opened at `faf0cea`)

- A fired order is applied with certainty: `modules/mass_battle/core/contact.py:130-162` walks the order's
  behaviour dict and `setattr`s each field (`:162`). The standing rule names this case
  (`AUDIT_BRIEF.md:56-59`: any "obeyed" effect with no resolution roll).
- Command is a literal. The season builds every side with `command=4` (`modules/mass_battle/massbattle.py:184-188`;
  `orderofbattle.py:75`). `derive_command(charisma, cognition)` exists with weights 2 and 1
  (`core/exchange.py:57-65`; `config.py:528-529`, Jordan directive 2026-06-02) and no season path calls it
  (`audits/04_MB_audit.md` §14 (a)). `Officer` holds a Command "derived the SAME way a general's is" and is
  "bookkeeping only" at resolution (`hierarchy/units.py:2745-2774`, `:2845-2849`).
- `MassBattleInput` carries no capability or attribute (`engine/season/queries/inputs.py:205-260`); the
  capability surface declares the `field` site with no rows (`unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md`
  §8, last paragraph).
- The one stochastic friction in a field is a multiplier on a side's whole pool (`core/exchange.py:147`), which
  the sources read put nowhere: they put friction on orders (delay, reinterpretation, refusal):
  `research/historical/mass_battle_movement_and_behaviour_grounding.md` E1, E3, E4, E5;
  `research/historical/mass_battle_wargame_models_grounding.md` K4, D2, L3 and convergence reading 3.

## The resolution, decided

### 1. Command is one capability row with two inputs

Definition (the home U1 §1 decides, `references/descriptor_registry.yaml: capabilities.rows`; U5b §1 row 4
already names the row and this states its cells):

```yaml
command:
  kind: skill
  gloss: "Gets a body of armed men to do what was ordered, when it was ordered."
  base: attr.social.charisma          # Presence: the governing attribute (the talent input of U1 §4)
  opposed_by: none                    # nobody's rating opposes an order; the task's difficulty does
  scale: [0, 7]
  untrained: default
  grows_by: [train, practice]
  source: "A-59; Jordan directive 2026-06-02 (Charisma primary, Cognition secondary)"
```

Use rows at the site `field` (`engine/season/rosters.yaml: tables.capability_uses`; the first rows of that
site, U1 §9):

```yaml
- {use: field, role: dice, key: command,              side: each, add: pool_add, floor: pool_floor}   # the learned skill
- {use: field, role: edge, key: attr.social.charisma, side: each, level: minor, per: mid}             # the social attribute
- {use: field, role: edge, key: attr.mind.acuity,     side: each, level: minor, per: mid}             # the mental attribute
```

- **Two inputs, as A-7 and U1 §4 assign them:** training gives dice (`pool = max(pool_floor, score + addends +
  pool_add)`); talent gives signed levels by steps from the scale's mid-point. They are never folded into one
  number. `derive_command` and its two weights leave with the harness code, as U5b §1 row 5 already decides.
- **"A function of social/mental attributes" is two `edge` rows**, one on Presence (`attr.social.charisma`)
  and one on Reason (`attr.mind.acuity`, whose registry aliases include `Cognition`:
  `references/descriptor_registry.yaml`, the `mind:` block). No aggregate key and no new compute kind is
  added: the registry's `agg.*` rows are `status: placeholder` and nothing reads them.
- **Decided, by ladder step 4, and reversible in one cell:** both rows ship at `minor` a step, the size U1 §4
  gives every capability's talent (the fixture `talent_level`). The 2026-06-02 directive's 2 : 1 ratio is not
  reproduced at landing, because the level table has no step below `minor`
  (`engine/dice_engine/sigma_leverage.py:103-108`); restoring it is setting the Presence row to `moderate`,
  and the calibration reads both. `config.py:528-529` tags the two weights class-B (tunable).
- `march` stays `capability: none` on its verb row (U1 §5): a commander does not roll the field. The
  `command` capability is the same key `14_VERBS_MILITARY_D_the_order_of_battle.md` Edit 4 gives the four
  army verbs, so a man who drills well and a man who is obeyed in the field are one rating.

### 2. What the field is handed (typed, composed host-side)

`engine/season/queries/inputs.py`, beside `MassBattleInput`:

```python
@dataclass(frozen=True)
class CommandRecord:
    person: str            # the person id, for the report only; the module reads nothing by it
    score: int             # trained rank in `command`, or the untrained score (`pool.py::score`)
    addends: int           # whole dice from the registered pool addends: practice, and a seat's modifier (§5)
    levels: float          # signed sigma: the two talent rows, summed (`sigma.py::advantage_sigma`)
    post: Optional[str]    # the unit he rides with (the commander only); None is the army's rear centre
    fed_by: tuple          # U1 §8's reason trail rows, echoed on the report
```

- `MassBattleInput.commanders: (CommandRecord | None, CommandRecord | None)` (this replaces the
  `(score, talent_levels)` pair of U5b §1 row 3 with the same two numbers plus the three fields the draw
  needs). `pool_add` and `pool_floor` ride the input raw, as U1 §8 has the fight carry them.
- Each unit row of the order of battle carries `officer: CommandRecord | None`, built by the same host
  function for the person the row's `officer` column names (`04_MB_manager_battle_one_resolver.md` §7).
- One host builder, `seam/wrappers/mass_battle.py::command_record(w, person, via)`, called by `field_input`.
  It calls the one pool reader and the one edge reader and holds nothing. `None` (no commander among the
  side, or a headcount side with no acting person) is today's literal: the module reads score 4, no addends,
  no levels (U5b §1 row 5's `None → 4`).

### 3. Who rolls: the chain has two links, and a draw is made by the link that gives the order to the unit

| order | given by | rolled on | distance term |
|---|---|---|---|
| a **standing order** whose trigger is local to the unit (`immediate`, `tick`, `enemy_range`, `ally_at`, `own_strength`, `flanked`, `volleys_spent`, `enemy_broken`, `in_lull`) | it was given before the field; the man on the spot carries it out | the unit's **officer**; a unit with none, the **commander** | none for an officer (he is with the unit); from the commander's post for a unit with none |
| a **signal** the commander fires at a window (`GeneralAction.kind == 'signal'`), or a standing order's `fire_signal` | the commander (or the firing unit's officer) | one draw **per unit waiting on it**, on that unit's officer, else the commander | none inside `obey.signal_reach`; the across-units term of §4 |
| an **improvised order** at a window or a lull (`order`, `rally`, `relieve`, `reform`, `commit`, `withdraw`) | the commander | **the commander**, to the unit's officer or, with none, to the unit; then, for an officered unit, **the officer** once more to his men | from the commander's post to the unit, on the first draw only |

- The rule in one sentence: *an order is drawn once for each person who has to pass it on to the unit.* A
  prearranged order has one such person; an improvised one to an officered unit has two.
- **Officers' ranks enter without a second ladder.** An officer is a person with the same `command` row, the
  same pool rule and the same two talent rows. What his echelon changes is which rows his draw covers (the
  row names him) and the span check the constructor already makes, with "one ladder ... at every echelon"
  (`modules/mass_battle/armies.py:176-180`, `hierarchy/units.py:2745-2749`). There is no table of dice by
  rank.
- The commander's `post` is a column on the army Record (`commander_post`: a unit's name). It is data on the
  record (A-2), it is where distance is measured from, and it is where he is when his unit is struck
  (`26_MASS_BATTLE_rout_pursuit_and_giving_ground.md` §1: a general's fall is a stand draw for each unit).

### 4. The draw

One function, at the one site an order's behaviour is applied:
`modules/mass_battle/core/contact.py::obey(order, roller, unit, ctx, rng) -> str`.

```
pool      = max(pool_floor, roller.score + roller.addends + pool_add)
levels    = roller.levels  (+ `minor` for the roller if the unit's Discipline is 4 or more: A-25, a favourable
                             circumstance raises the roller; 14_VERBS_MILITARY_D's `disciplined`)
obstacle  = obey.task                                   # the one task-obstacle rule, carried as a number (below)
          + obey.step[kind]                             # 26_MASS_BATTLE_maneuver_orders §1's table, as steps
          + obey.distance * bands(roller.post, unit)    # §3's last column; 0 when it says none
          + obey.across  * max(0, units_on_signal - 3)  # 26's row, kept
          + obey.unsteady  (unit `raw`, or Discipline 1)
          + obey.in_contact (the unit has a cell in contact)          # CONTROL 0
net       = roll_net_continuous(pool) + net_boost(levels, pool)       # the one sampler (A-5)
band      = degree_from_net(net, obstacle)                            # the one ladder
```

| band | what happens to the order |
|---|---|
| Overwhelming, Success | **obeyed**: applied this tick |
| Partial | **late**: applied after `1 + bands` ticks. **Misread**, in the one case the data can express: the order came by signal and the unit holds another pending order on a *different* signal; it answers that one instead, now |
| Failure | **not carried out**: the order stays pending and is drawn again when its trigger next holds, at most once a phase. For a restraint (`hold` on `enemy_broken`, `recall`, a signalled halt, a body held for a signal) not carried out is the body doing what it was held from: it chases, or goes in early |

- **Grounds for the three results.** Delay: the Kriegsspiel umpire holds a message "for a round or two" (WG K4;
  MV E5). Misreading: the same umpire "decides how troops would interpret and execute a given order" (WG K4).
  Refusal, and restraint failing: the Hospitallers at Arsuf charged without the signal, the French at Crécy
  pressed on against the plan, Gloucester at Bannockburn attacked on a taunt (MV E4). Command as a scarce draw:
  DBA's die and Lost Battles' die plus army quality (WG D2, L3). Signals few and coarse: MV E3.
- **Misreading is not scripted.** It exists only where a commander has given one unit orders on two signals.
  A plan with one signal cannot be misread and can only be late; a plan with three is fragile. No rule names a
  manoeuvre or an outcome.
- **Distance.** `bands` is the whole number of `obey.reach` cells between the roller's post and the unit's
  centroid, beyond the first. Three independent designs make command local (Lost Battles: a commander spends
  on units in his own zone, WG L3; Field of Glory: command range; Total War: the general's radius, WG T2 and
  the convergence table). **No command delay as a number is established** (MV, "does not establish"), so
  `reach`, `distance` and `signal_reach` are seeds with a control (`distance: 0`).
- **`obey.task`** is the obstacle of a task nobody opposes, by the one rule U1 §4 gives ("nobody opposite":
  the opposition rate times an ordinary person's pool), computed host-side and carried on `MassBattleInput` as
  one number. The module does not read a fixture table and does not restate the rule.
- **One draw per key** (A-30): each draw is keyed on (field, tick, unit, purpose `obey`, link), so the draw
  sequence does not depend on who issued the order, and a replay from the interventions list
  (`04_MB_manager_battle_one_resolver.md` §5) reproduces it.

Data. Authored head: the `orders.obey` block of `references/troops.yaml` when the troop file lands
(`04_MB_unit_loadout_and_weapon_in_hand_B.md` §1); until then a constant block beside `ROLE_SPEC` in
`modules/mass_battle/config.py`. Exported by `tools/export_battle_orders.py` to
`engine/engine_params/battle_orders.json` (the blocking `--check` exists).

```yaml
orders:
  obey:
    arm: off                 # off | on.  off is today's certainty: the control
    step: {keep: none, change: 0, restrain: 1, signal: 0}    # `none` = no draw: nothing is asked
    across: 1
    unsteady: 1
    in_contact: 0            # CONTROL. Flip seed 1. [shape from MV E4; no magnitude sourced]
    reach: 13                # cells in one distance band. SEED: a quarter of the 51-cell field. [no source]
    distance: 1              # per band. CONTROL 0
    signal_reach: 51         # a prearranged signal carries the field at the stated scale (26, S-1). SEED
```

Every number is a seed. The form is what is decided.

### 5. A seat's modifier (A-12)

- It reaches a Command draw as **whole dice in `CommandRecord.addends`**, through `POOL_ADDENDS` in the one
  pool reader, read off the seat the march is made through (`Act.via`): U1 §3 item 6, unchanged. "Rank
  supplies dice" (`architecture/meta/04_CODE_ARCHITECTURE.md` §B.7) is literally what an addend is. The
  amendment text A-12 owes is the unification stage's; nothing here needs it to land first, because a seat
  that declares no modifier adds zero.
- **It is the commander's only.** An officer is a column of a unit row, not an act through a seat, so no
  officer has a seat addend. If the institutions kit makes an officer's post a seat, that is its row and one
  more call of the same builder; no rule here changes.
- **No double count.** The module sees `addends` as one integer. Regard for an office-holder stays in the
  chooser's stance term (U1 §3 item 6); no `edge` row at `field` reads a seat.

### 6. What the other Command reads become

| read today | becomes |
|---|---|
| `recall_check`, `feigned_retreat_recognized`: `roll_pool(pursuer.command)` against Ob 2 (`orchestration.py:2094-2106`) | calls of `obey`'s pool rule on the commander's record, with their stated obstacles as steps over `obey.task` |
| the rally roll (`16_PESSIMIST_MB_rout_has_two_exits.md` step 1) | the same; the commander's, since rally at the end of a field is his act |
| morale erosion's divisor `dmg / (discipline × command)` (`orchestration.py:2342-2343`, `:1151`) and `h_per_size` (`hierarchy/units.py:2867`) | read the span value of **the link that covers the unit** (its officer's, else the commander's), by U5b's `command_span` table. A side-wide integer in every unit's divisor is a static side value; this makes it the unit's own |
| `command <= 0`: every unit's morale set to zero (`battle_loop.py:408-413`) | a stand draw for each unit (`26_MASS_BATTLE_rout_pursuit_and_giving_ground.md` §1) |

## Exact edits

| file (owner) | edit |
|---|---|
| `references/descriptor_registry.yaml` (CORE, via U1) | the `command` row of §1 |
| `engine/season/rosters.yaml: tables.capability_uses` (IN) | the three `field` rows |
| `engine/season/queries/inputs.py` (IN) | `CommandRecord`; `MassBattleInput.commanders`, `.pool_add`, `.pool_floor`, `.obey_task` |
| `engine/season/seam/wrappers/mass_battle.py` (IN) | `command_record`; `field_input` fills the commander's and each officer's |
| `modules/mass_battle/core/contact.py` (MB) | `obey`; `check_orders` calls it before applying a behaviour; a `late` order carries its due tick on the subunit |
| `modules/mass_battle/massbattle.py`, `battle_loop.py` (MB) | window and lull actions go through `obey` (two links where §3 says so) |
| `modules/mass_battle/orchestration.py` (MB) | the four reads of §6 |
| `modules/mass_battle/armyrecord.py`; `rosters.yaml: record_kinds.values.army` (MB, IN) | `commander_post` on the Record; validated against the unit names |
| `tools/export_battle_orders.py`, `engine/engine_params/battle_orders.json` (MB) | the `obey` block |

## Gate (execution artifacts)

1. `obey: off`, `commanders: (None, None)`: `python3 tools/ci_golden_modes_check.py` digests equal; a field
   with orders equals the same field on the tree before these edits, at 200 seeds.
2. `obey: on`, one unit with `(tick:3, {stance: hold})`, n 400: the order is applied at tick 3 in some fields,
   later in some, never in some; all three counts above zero; `assert checked >= 400`.
3. **Command matters, in both inputs.** Same seeds, the unit's officer at score 5 against score 0: the share
   obeyed at once differs beyond two standard errors of the control. Officer at Presence 6 and Reason 6
   against 2 and 2 at equal score: it differs again. Presence alone raised, and Reason alone raised: each
   moves it.
4. **Distance.** A unit with no officer, the commander posted beside it against three bands away: the share
   obeyed at once is lower at distance; with `distance: 0` the two are equal field for field.
5. **Signal.** Four units on one signal against two: the share of fields in which every unit answers at once
   is lower for four. A unit holding orders on two signals answers the wrong one in some fields; a unit
   holding one never does.
6. **The chain.** An improvised `order` to an officered unit consumes two draws and to an unofficered unit
   one, read from the draw trace; replay from `FieldOutcome.interventions` gives an equal outcome and an equal
   draw count at every seed.
7. **A seat.** With a planted addend of 2 on the commander's march seat, his `CommandRecord.addends` reads 2
   and gate 3's share moves; no officer's record changes.
8. `git grep -n "roll_pool(.*\.command)" modules/mass_battle` prints nothing.

## Falsifier

An order that takes effect at its trigger in every one of 400 fields with the draw on. A commander's score, or
either attribute, that moves no obedience share. A draw count that depends on who issued the order. A
misreading on a unit that holds one signal. A second table that maps a rank to dice. A seat read by the module.

## NERS (definitions `CLAUDE.md` §0.06; E last)

- **N.** Top-down: A-59 names this as where the day's chance belongs. Bottom-up: the order queue, the signal
  set and the officer class exist and decide nothing. Lateral: the same capability, pool rule and levels as a
  speech or a fight; the same draw `order_unit` makes in the season. Vertical: a person's sheet reaches a
  field for the first time. Diagonal: a seat's modifier reaches an army by the channel every seat uses.
  Horizontal: both sides, played or not. Cut it and orders are certain and command is the literal 4.
- **R.** Whom to make an officer; where the commander rides; how many signals a plan can bear; a good captain
  under a poor general. With no player: orders miss, wings go early, and the record says which.
- **S.** One site, one sampler, one ladder, one pool rule; the window, the lull and the standing order are
  drawn alike; pauses at the engine's own boundaries.
- **E, against that.** One capability row, three use rows, one record, one function, one table of eight
  seeds; a literal, a derivation with its own weights and two bespoke rolls leave.

## Cost class

Small build, in two parts: the record and the capability rows (with U5a's CAP Part B; hash equal at `None`),
then `obey` (with the orders batch, `U5b_MB_rulings_in_the_field.md` §6 row 5).

## Conflicts with ruled items, named

- The 2026-06-02 directive's 2 : 1 weighting of Charisma over Cognition is not reproduced at landing (§1);
  one cell restores it. Decided by precedent (U1 §4), not escalated.
- A-7's assignment (training the dice, talent the levels) is U1's and is listed for Jordan as
  decided-and-reversible in `unified/U5_CONFLICTS_U5a.md` §2; this file follows it.
