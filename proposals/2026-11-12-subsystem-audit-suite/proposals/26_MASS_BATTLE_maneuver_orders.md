# MB · the manoeuvre set as order rows: every historical manoeuvre is a few standing orders, each obeyed by a draw

## Status: PROPOSED

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

```
pool     = commander's Command (the side's general; a unit with an officer adds 1)
obstacle = orders.obey_ob[kind]            # data, below
degree   -> Overwhelming, Success : applied this tick
            Partial               : applied next tick
            Failure               : not applied; the order stays pending and may fire again
                                    when its trigger next holds, once per phase
```

| kind of order | `obey_ob` (seed) | why it differs |
|---|---|---|
| keep doing what the body is doing (`hold`, `stance` unchanged) | 0: no draw | nothing is asked |
| a change of stance, target or route; a weapon switch | 1 | the ordinary order |
| stop or restrain: `hold` on `enemy_broken`; `recall`; a signalled halt | 2 | SQ 4 step 6, SQ 10 step 5: the urge to chase or charge; this is `RECALL_OB`, already 2 (`orchestration.py:2054`) |
| act together on a signal across several units | 1, +1 for each unit beyond three | SQ 7 step 4; DBA's cost of moving separated groups |
| anything, for a body with Discipline 1 or `raw` | +1 | `14_VERBS_MILITARY_D`'s `raw` column, read here |

- The draw is the module's, on the scoped RNG, **whoever issued the order** (a standing order, a decider, a
  replayed intervention), so the draw sequence does not depend on who decided.
  `04_MB_manager_battle_one_resolver.md`'s gate 1 becomes: a decider returning `none` gives an equal outcome
  and an equal draw count; its gate 2 (replay from the interventions list) holds unchanged.
- The values are seeds in `engine/engine_params/battle_orders.json` beside the vocabulary; `obey: off` is the
  control and is today's certainty.
- This is friction where the sources put it. It does not touch the per-battle multiplier
  (`ED-MB-0016`); see the audit's §7 item 2.

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

- No manoeuvre name is read by the resolver. A doctrine row is data that writes orders.
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
| `tools/export_battle_orders.py`, `engine/engine_params/battle_orders.json` | `obey_ob`, the on/off arm, the new triggers and behaviours |
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
`26_MASS_BATTLE_cell_scale_and_time.md`. The Command input is the first audit's §14 (CHAR).
