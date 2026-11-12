# MB · the manoeuvre set as order rows: every historical manoeuvre is a few standing orders, each obeyed by a draw

## Status: PROPOSED

Folded: 2026-11-12 by `audits/27_MB_COMMAND_AND_DYNAMIC_STRENGTH.md` (ruling A-59; decisions 4 to 8). Nothing here is deleted. §1's site, its bands' sense and its table of kinds stand; three things in §1 are amended, and `27_MB_A_command_and_the_obedience_draw.md` carries the detail. (1) **The pool.** "The commander's Command; a unit with an officer adds 1" reads one input and makes every officer worth one die. A-59 makes command a learned skill with social and mental attributes (two inputs, A-7), so the pool is the one pool rule on the roller's trained `command` and his Presence and Reason enter as levels; the roller is each person who has to pass the order on: the unit's officer for a standing order, the commander and then the officer for an improvised one. (2) **Distance and signal.** An improvised order pays a step for each band of distance from the commander's post; a prearranged signal carries the field. (3) **The bands.** Partial is late, by one tick plus the distance bands; on a unit that holds orders on two signals a Partial answers the wrong one (misreading, and only there); Failure is as written. The `obey_ob` values become steps over the one task obstacle (`27_MB_A` §4), because under A-6 a pool of score plus six passes an obstacle of 1 almost always. "It does not touch the per-battle multiplier" (last bullet of §1) is now answered: A-59 lowers it and `27_MB_C_dynamic_strength_and_the_residual_chance.md` tests its removal. §3's doctrine rows gain a default post for the commander (`27_MB_D` §1).

Reconciled: 2026-11-12, wave 3 rewrite lane W3-1 — rows applied: `R1_READ.md` §2 row A-6/A-7/A-59 and §6.1 (e) (§1's pool and absolute obstacle are retracted by `27_MB_A` §4: the pseudocode is replaced by the one pool rule on the roller's trained `command` with talent as levels and `orders.obey.step` over the one task obstacle; the table of kinds keeps its rows as steps), §2 row A-30 ("the scoped RNG" → keyed draws), A-59/A-77 (the multiplier sentence answered and removed), §1.2 D-27a watch (no proper noun in a doctrine row), U1 §4 M-08 (the owner of the obedience data is `references/troops.yaml: orders.obey`, exported to `battle_orders.json`), D-U1-11g (the Command input is `27_MB_A`'s `command` capability); test 9 (tests, lands-it, tier; `Depends on:` / `Lands in batch:`).

**Depends on:** `04_MB_manager_battle_one_resolver.md` §2 and §4 (B20); `26_MASS_BATTLE_cell_scale_and_time.md` §3 (B19, the bouts and the lull); `27_MB_A_command_and_the_obedience_draw.md` (B19, `obey`); `11_GO_one_draw_owner.md` (B06).
**Lands in batch:** B20 (`B20-mb-orders`, MB), with `04_MB_manager_battle_one_resolver.md` §2–§6.

Lane MB (the chooser's side is CHAR's). Carries rows B-2, B-3, B-9 and B-13 of
`audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md`. **Extends `04_MB_manager_battle_one_resolver.md`** §2
(standing orders) and §4 (the general's action), which are kept and amended in place. The sequences are in
`research/historical/mass_battle_maneuver_sequences_grounding.md` (**SQ** with its section number).
Reference, not mechanism (`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

Nothing for a side with no standing orders and no decider. Otherwise: (1) an order that fires takes effect
by a draw, at once, a tick late, or not at this trigger; (2) two new triggers and three lull actions exist;
(3) a doctrine row can give an unplayed commander any of the manoeuvres below, so two commanders differ in
what their armies do. No natural season fights an army field today.

## The problem

- The engine's order vocabulary is nearly sufficient (six trigger kinds, a closed set of behaviours, go-code
  signals: `modules/mass_battle/hierarchy/units.py:271-290`, `:309`), and a season can produce one order
  (`04_MB_manager_battle_one_resolver.md`, the problem).
- A fired order is applied with certainty (`setattr` at the one site, `core/contact.py::check_orders`, as
  `units.py:321-325` describes). The standing rule lists "any 'binds'/'obeyed' effect with no resolution
  roll" as a known case (`AUDIT_BRIEF.md:56-59`), and the MILITARY verb lane hands exactly this to MB
  (`14_VERBS_MILITARY_D_the_order_of_battle.md` §5: "standing orders obeyed in the field, which is the
  resolver's draw").
- The sources put a battle's uncertainty of command on orders: a signal fixed beforehand and a charge loosed
  without it (Arsuf), knights pressing on against the plan (Crécy), a recall by trumpet that worked (Zama);
  the Kriegsspiel umpire delays and reinterprets; DBA and Lost Battles make command a die
  (`…_movement_and_behaviour_grounding.md` E1–E5; `…_wargame_models_grounding.md` K4, D2, L3).
- The tree's research and its earlier audit both warn against a named-manoeuvre button
  (`research/pre_firearms_formations/14_methodology_audit.md:77`; the 2026-07-26 audit's finding that the
  "emergent" envelopment was a script, as `04_MB_cell_hierarchy_as_data.md` §3 records).

## The resolution, decided

### 1. The obedience draw

At the one place an order's behaviour is applied (`core/contact.py::check_orders`), and for a general's
`signal` and `order` actions:

*(Reconciled, W3-1: the pool and obstacle are `27_MB_A_command_and_the_obedience_draw.md` §4's, which
retracts this section's first form, "the commander's Command; a unit with an officer adds 1" over an absolute
`obey_ob`.)* The roller is each person who has to pass the order on (the unit's officer for a standing order;
the commander and then the officer for an improvised one); his pool is the one pool rule on his trained
`command` (A-6, A-7), his Presence and Reason enter as levels; the obstacle is the one task obstacle plus the
step for the kind of order below (`orders.obey.step`); the draw is `core/contact.py::obey`, keyed
`(field, tick, unit, "obey", link)` (A-30). The bands keep this section's sense:

```
degree   -> Overwhelming, Success : applied this tick
            Partial               : applied late (one tick plus the distance bands; on a unit holding orders
                                    on two signals, the wrong one: 27_MB_A §4)
            Failure               : not applied; the order stays pending and may fire again
                                    when its trigger next holds, once per phase
```

| kind of order | step over the task obstacle (`orders.obey.step`, seed) | why it differs |
|---|---|---|
| keep doing what the body is doing (`hold`, `stance` unchanged) | 0: no draw | nothing is asked |
| a change of stance, target or route; a weapon switch | 1 | the ordinary order |
| stop or restrain: `hold` on `enemy_broken`; `recall`; a signalled halt | 2 | SQ 4 step 6, SQ 10 step 5: the urge to chase or charge; this is `RECALL_OB`, already 2 (`orchestration.py:2054`) |
| act together on a signal across several units | 1, +1 for each unit beyond three | SQ 7 step 4; DBA's cost of moving separated groups |
| anything, for a body with Discipline 1 or `raw` | +1 | `14_VERBS_MILITARY_D`'s `raw` column, read here |

- The draw is the module's, keyed (A-30), **whoever issued the order** (a standing order, a decider, a
  replayed intervention), so the draws do not depend on who decided.
  `04_MB_manager_battle_one_resolver.md`'s gate 1 becomes: a decider returning `none` gives an equal outcome
  and an equal draw count; its gate 2 (replay from the interventions list) holds unchanged.
- The values are seeds authored in `references/troops.yaml: orders.obey` and exported to
  `engine/engine_params/battle_orders.json` beside the vocabulary (U1 M-08); `obey: off` is the control and is
  today's certainty.
- This is friction where the sources put it. *(A-59, A-77: the per-battle multiplier (`ED-MB-0016`) is
  lowered and ships at zero when `27_MB_C`'s first test arm passes.)*

### 2. Two triggers, three lull actions

- Triggers added to `_ORDER_TRIGGER_KINDS`: `enemy_broken` (the body this unit is fighting has routed) and
  `in_lull` (the bout has ended drawn and a lull is open). With `flanked` and `volleys_spent` from
  `04_MB_unit_loadout_and_weapon_in_hand_B.md`, the set is ten.
- Behaviours added to the standing-order set: `pursue: true | false`, `reform: {shape, ranks, files}`
  (`26_MASS_BATTLE_movement_and_fatigue_as_data.md` §4), `feign: true` (the existing `feign_retreat`
  pseudo-field, `units.py:326-330`, under its plain name).
- Lull actions added to `GeneralAction.kind` (legal only in a lull,
  `26_MASS_BATTLE_cell_scale_and_time.md` §3): `relieve` (two units of one post exchange lines), `reform`,
  `commit` (a `reserve` post takes a place in the line). Each is drawn as an order of the second row above.
  In a lull a reform costs no ticks; relief moves the fresher unit's columns to the front and that is all it
  does.

### 3. The manoeuvres, as rows

Each is a doctrine entry (`troops.yaml: doctrines`, the first MB lane's step 5a): which units get which
orders. Nothing below is a new mechanism; a row that needs one names it.

| manoeuvre | units and orders | the draws that can undo it | SQ |
|---|---|---|---|
| **Stand and receive** | front: `(immediate, {stance: hold})` with a pole or pike arm; missile units behind an obstacle | the stand draw (`26_…_rout_pursuit_and_giving_ground.md` §1) | 3, 5 |
| **Shoot, then close** | missile units: `(volleys_spent, {in_hand: secondary})`, `(enemy_range:2, {in_hand: secondary})` for those who should not wait | obedience; the switch tick | 5 |
| **Hold the horse, then loose it** | horse on a `rear` or `reserve` post: `(signal:charge, {stance: aggressive})`; the general fires `charge` at a window | obedience on the signal (a Failure is a charge that does not come; a unit with Discipline 1 may go early: the fourth row of §1 applied to its `hold`) | 4 |
| **Refuse to chase** | every foot unit: `(enemy_broken, {pursue: false})` | the restrain row: Ob 2 | 4 step 3, 6, 10 |
| **Feigned flight** | the bait: `(tick:N, {feign: true, stance: retreat})`, then `(enemy_range:D, {stance: aggressive})`; a waiting unit: `(signal:turn, …)` | (i) the bait's own Discipline against Ob 1 or its flight is real (new, one call of `stand_draw` with no shock terms); (ii) the enemy recognises the feint (`feigned_retreat_recognized`, built); (iii) the pursuer's Discipline (`feigned_retreat_check`, built) | 6 |
| **Envelopment** | centre: `(immediate, {yielding: true})`; wings on `left` and `right` posts: `(signal:close, {route: inward, stance: aggressive})`; horse: `(enemy_broken, {pursue: false})` then the general's `order` to turn on the rear; the general fires `close` | the centre's stand draws while yielding; obedience on the signal across units; each wing's own fight; the horse's restraint | 7 |
| **Refused flank** | the weak wing: `post: rear`, `(immediate, {stance: hold})`; the strong wing deep (`ranks`) and `aggressive` | the weak wing's stand draw | 7 step 7 |
| **Line relief** | second line on a `rear` post, `(in_lull, …)` reserved for the general's `relieve` | obedience; it needs a lull, so it needs the first line to have held one bout | 8 |
| **Reserve against a turning movement** | a unit on `reserve` behind the threatened flank: `(ally_at:D, {stance: aggressive})` keyed on the flanking enemy's approach, or `(signal:…)` | obedience | 7 step 7, 3 step 6 |
| **Fighting withdrawal** | every unit `(own_strength:F, {yielding: true})`, the general's `withdraw` at a window or a lull; a rearguard unit `(immediate, {stance: hold})` | each yielding unit's stand draws; the pocket exit if the way back is shut (built) | 9 |
| **Pursue to destruction** | horse and `Pursue`-role units: `(enemy_broken, {pursue: true})` | none to start; the recall at the lull if the commander wants them back | 10 |
| **Storm a walled place** | no order row: the `storm` posture on a `walls` field, at the dice the terrain row already gives | — | 11 |

### 4. What is deliberately not built

- No manoeuvre name is read by the resolver. A doctrine row is data that writes orders. Doctrine row keys
  name manoeuvres (`envelopment`, `refused_flank`), never a battle or a person: the proper nouns of the
  sources (Cannae, Arsuf, Crécy) stay in this prose and out of `troops.yaml` (`04` D-27a).
- No view of the enemy's orders. The commander sees his own side and what is in contact
  (`04_MB_manager_battle_one_resolver.md` §4), which the tree's own research asks for
  (`research/pre_firearms_formations/16_historical_vs_gamedesign_audit.md:66-68`).
- No drill for wedge, maniple, tercio or column-to-square. No period manual was reached
  (`…_maneuver_sequences_grounding.md`, "does not establish"), and the shapes the engine has are enough for
  the rows above.

## Exact edits

| file (owner) | edit |
|---|---|
| `modules/mass_battle/core/contact.py::check_orders` | the obedience draw; the two triggers' tests |
| `modules/mass_battle/hierarchy/units.py` | `_ORDER_TRIGGER_KINDS` gains two; `_ORDER_SAFE_FIELDS` gains `pursue`, `reform`; `feign` as the accepted spelling of the pseudo-field |
| `references/troops.yaml: orders.obey`, `tools/export_battle_orders.py`, `engine/engine_params/battle_orders.json` | the `step` table, the on/off arm (U1 M-08); the new triggers and behaviours |
| `modules/mass_battle/massbattle.py` | the three lull actions, applied between bouts |
| `references/troops.yaml: doctrines` | the rows of §3 as named doctrine entries, each a list of `(class of unit, post, standing_orders)`; `balanced` stays today's and has none |
| `modules/mass_battle/orchestration.py` | the bait's own draw before `feigned_retreat_recognized` is asked |

## Gate (execution artifacts)

1. `obey: off`: digests equal to the manager proposal's tree. `obey: on`, an army with a single order
   `(tick:3, {stance: hold})`, n 200: the order is applied at tick 3 in some fields, at tick 4 in some, and
   later or never in some; `orders_fired` records which.
2. Same seeds, the order issued as a standing order, by a decider at the same tick, and from a replayed
   interventions list: equal outcomes and equal draw counts.
3. Feigned flight against an enemy with `pursue: true`, n 200: the pursuer is overextended in some fields,
   recognises the feint in some, and the bait's flight turns real in some. All three counts above zero.
4. The envelopment doctrine against the `balanced` doctrine, equal armies, n 200, against the same-run
   mirror: its win share and the share of fields in which the wings never closed are both reported; the
   second is above zero. No target.
5. `relieve` in a lull: the unit that comes forward reads higher column stamina than the one it replaced, and
   the next bout's loss on that post differs from the unrelieved control beyond the control's spread.
6. `git grep -n "envelop\|cannae\|refused" modules/mass_battle/massbattle.py modules/mass_battle/battle_loop.py`
   prints no branch on a manoeuvre's name.

**Tests (W3-1).** `tests/valoria/test_conditional_orders.py::test_obey_on_spreads_the_applied_tick`
(gate 1, `assert checked >= 200`), `::test_three_issuers_equal_outcomes` (gate 2);
`tests/valoria/test_mass_battle_maneuvers.py::test_feigned_flight_three_outcomes`,
`::test_envelopment_wings_sometimes_never_close`, `::test_relieve_brings_the_fresher_unit_forward` (gates
3–5); gate 6's grep in the commit body. **Hash movers:** none with `obey: off`; the flip moves every army field
with orders. **Lands:** an IN-lane implementation session under `/methodology-execute` with MB review;
`sonnet`, the doctrine readings `haiku` read by `opus`.

## Falsifier

An order that takes effect at its trigger in every one of 200 fields with the draw on; a draw count that
depends on who issued an order; a doctrine whose manoeuvre succeeds in every field; the resolver reading a
doctrine's name.

## NERS (definitions `CLAUDE.md` §0.06; E last)

- **N.** From the manager's seat: composition and standing orders are the whole game, and a plan that always
  executes is not a plan. From history: every decisive manoeuvre read was a conjunction of orders, one of
  which could fail. From the architecture: the standing rule names this case. Cut the draw and the
  envelopment row is the button the tree's own research forbids.
- **R.** Choosing a plan the army can execute (drilled troops for a signalled wheel; raw levy for standing
  still); a commander's Command matters every tick an order fires; with no player, armies misfire.
- **S.** One draw at one site for every source of an order; triggers for a unit and conditions for a squad
  member remain one idea; a lull is a window like the others.
- **E, against that.** One draw, one small table, two triggers, three behaviours, three lull actions, a
  dozen doctrine rows of data.

## Cost class

Small build, after `04_MB_manager_battle_one_resolver.md` §2 and the bouts of
`26_MASS_BATTLE_cell_scale_and_time.md`. The Command input is `27_MB_A`'s `command` capability (D-U1-11g).
