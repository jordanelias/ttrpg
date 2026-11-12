# MB · what breaks a body, and what happens to it afterwards: the stand draw, rally, pursuit, the dead and the taken

## Status: PROPOSED

Lane MB (the outcome fields are IN's; captives are the PHYSICAL lane's custody). Carries rows B-4, B-5, B-7,
B-8, R-2, R-3 and R-4 of `audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md`. **Builds on
`16_PESSIMIST_MB_rout_has_two_exits.md`** (rally and pursuit at the end of a field), which is kept and amended
in place; this file adds what that one does not have. Source keys as in the audit (**CR**, **MV**, **SQ**,
**WG**). Reference, not mechanism (`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

With `stand_draw: off` (the control): nothing beyond the amended pessimist proposal. With it on: a body that
is charged, struck in flank or rear, or sees its officer fall may break or give ground at once, whatever its
losses; a general's fall is drawn unit by unit; a body whose opponent breaks during a bout may chase it and
leave the fight; the men a beaten side loses in flight are divided into dead and taken. Declared hash movers
wherever an army field is fought; none in a natural season today.

## The problem

- The sources that were read at the page say a body's will breaks on a **shock**, often with few dead, and
  that the killing follows: "the breaching of their line, a psychological shock such as the death of the
  general, or the sheer accumulation of casualties and fatigue" (CR D1); many clashes "decided at or before
  the first shock" (CR D5); "the most decisive losses on the side of the vanquished only commence with the
  retreat" (CR A12). A beaten hoplite army's whole loss averaged about 14% dead, a victor's 5% (CR A1).
- The engine draws each subunit's breakpoint as a **casualty fraction** between 0.15 and 0.30
  (`modules/mass_battle/config.py:160-183`; the two bounds are Jordan's values). Morale also erodes from flank
  damage and an ally's rout, but the break itself waits on losses. Measured by the suite: in a mirror field
  the loser has lost 37% and the winner 7% when the field stops, 1 : 5.3, at the top edge of Krentz's range
  (1 : 1.7 to 1 : 5.2) before any pursuit (`16_PESSIMIST_MB_rout_has_two_exits.md`, the problem).
- A general removed from command sets every unit's morale to zero: "Command=0 → instant rout"
  (`battle_loop.py:408-413`). The sources have armies that broke when the leader fell (Hastings, Gaugamela)
  and parts of them that did not (the household at Hastings; MV R5, R7). A certainty where a draw belongs.
- Giving ground is built (`yielding`, with emergent entry, rally exit and pocket exit,
  `config.py:255-270`) and is not a result anyone is told about.
- Half of a beaten Roman-era army's loss could be prisoners (CR A6). The field returns one share of `body`;
  there are no captives (`audits/04_MB_audit.md` §7).
- Horse that won its wing and chased was absent until it came back, and that return decided Cannae and Zama
  (MV P5). In the engine a victor is re-targeted for nothing.

## The resolution, decided

### 1. The stand draw

One function, `orchestration.stand_draw(unit, atom, shock) -> str`, returning `stands`, `gives_ground` or
`breaks`. It is a roll of the body's Discipline pool against an obstacle; the ladder's bands map as Success
or better `stands`, Partial `gives_ground`, Failure `breaks`.

| it is called when | once per |
|---|---|
| a charge reaches the body (the first tick of contact by an enemy whose closing speed was above base pace) | charging body |
| the body is first in contact on a flank or rear arc | bout |
| the body's officer is felled or yields (`04_MB_manager_battle_one_resolver.md` §7) | event |
| the army's general is removed from command | unit (replacing the army-wide `set_morale(0.0)`) |

| obstacle term | value (seed) | ground |
|---|---|---|
| base | 1 | — |
| charged by horse while not braced and not holding a pole or pike arm | +1 | MV H1–H3: steady pikes and squares held; unbraced foot did not always |
| struck in flank | +1 | CR D2 |
| struck in rear | +2 | CR D2 |
| shaken already (morale below half its start) | +1 | the engine's own `PC_SHOCK_SHAKEN_GAIN` reading (`research/historical/mass_battle_gauge_grounding.md:83`) |
| re-forming or switching weapons this tick | +1 | MV X2 |
| braced, or in a `Hold` role with a pole or pike arm, against a frontal charge | −1 | SQ 3 step 5 |
| a held reserve of its own side within reach behind it | −1 | CR D3; SQ 3 step 6, SQ 8 |

- `stands`: nothing changes; a frontal charge that did not break a standing body has spent its shock (the
  existing recoil applies).
- `gives_ground`: the body enters `yielding` by the existing switch. This is the state the sources describe
  between holding and running (CR D4).
- `breaks`: the body routs by the existing `rout_resolution` path, at whatever its losses are.
- The values are seeds. The table is data (`troops.yaml: stand`), not constants in the function.
- The casualty breakpoint band stays exactly as it is and remains the *attrition* trigger. Whether a body may
  break below its floor at all is listed for Jordan in the audit's §7 item 1; `stand_draw: off` is option (b)
  there and the control here.

### 2. Giving ground is reported

`FieldOutcome` parts (`04_MB_typed_outcome_and_one_path.md`) carry `gave_ground: bool`; the report's phase
summary says which parts yielded and whether they rallied from it (the existing yield-rally exit) or were
pocketed. No new mechanism.

### 3. Pursuit inside a bout: the victor's own draw

When the body a unit is fighting breaks and the field goes on:

- the victor draws Discipline against Ob 1, **read with its standing order** for the new trigger
  `enemy_broken` (`26_MASS_BATTLE_maneuver_orders.md`): ordered `hold`, a Success or better keeps it in hand
  and it takes its next target; a Partial keeps it but costs it a tick; a Failure sends it after the runners.
  Ordered `pursue`, or with no order and a mounted or `Pursue`-role body, it pursues without a draw. A foot
  body with no order holds without a draw.
- A pursuing body leaves the fight for the rest of the bout, inflicts `pursuit_damage` on the broken body
  (the amended pessimist function), and re-enters the next bout with its columns' stamina reduced by one
  clash's drain per tick it chased (`fatigue.clash_drain`). A commander may recall it at the lull by the
  existing `recall_check`.
- This is what makes the cavalry's return a thing that can fail to happen (MV P5), with no "envelopment"
  rule: the wing that wins and holds is free to turn inward; the wing that wins and chases is gone.

### 4. The dead and the taken

- The field returns, per side and per part: `fight_loss` (share of its men lost before it broke or the field
  ended) and `pursuit_loss` (share lost after it broke), and of the second, `taken` (share of those lost who
  were taken alive).
- `taken` is a draw at the end of the pursuit, per pursued part: the pursuer rolls its pool against Ob 2;
  the share taken is 0 on Failure, a quarter on Partial, a half on Success, three-quarters on Overwhelming.
  `[seeds. The only figures read are single battles: Zama, 20,000 dead and about as many captured;
  Cynoscephalae, 8,000 killed and 5,000 taken; Pharsalus, 6,000 to 15,000 killed and 24,000 taken (CR A6,
  §B). They support "about half, widely varying", and nothing finer.]` A standing order "no prisoners"
  (Courtrai, SQ 3 step 8) sets it to zero.
- **What the season writes.** The men lost in the fight and those killed in the pursuit are written as the
  share of `body` they are today, under `field_casualty_model`. The taken are not hurt by the field: they
  are persons and cohort members in the victor's custody. Named persons among them arrive in custody by the
  PHYSICAL lane's `capture` under its `war` context (`14_VERBS_PHYSICAL_A_custody_and_force.md` A2: custody
  goes to the court or seat whose act it enforces; here the seat that dispatched the march). A cohort's taken
  share is a count on the band Event until SE has a place for prisoners; it is not written into anyone's
  `body`.
- **What the field does not decide:** who among the hurt dies. The historical figures are of the dead; the
  engine's loss is men out of the fight. No dead-to-wounded ratio was established (the audit's §6), so none
  is built; that draw is the season's (`22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn.md`).

### 5. Rally, by what the troops carry

Amending the pessimist proposal's rally roll (Command against Ob 2, once, at the end of the field): the
obstacle takes a step from the routed side's troops, weighted by men: `armour.<tier>.rally_step` in the troop
file, seeds `none: −1`, `light: 0`, `medium: 0`, `heavy: +1`; mounted troops −1. Ground: troops who "simply
turned and ran, and then rallied once they had temporarily outdistanced pursuit", against "it is hard to
envisage more heavily equipped troops succeeding" (MV P1, `[D]`).

## Exact edits

| file (owner) | edit |
|---|---|
| `modules/mass_battle/orchestration.py` | `stand_draw`; the `enemy_broken` handling at the target-assignment step `[UNVERIFIED: the function that re-targets a freed body was not opened; the first audit places pairings at `orchestration.py:2191-2495`]`; `taken` draw beside `pursuit_damage` |
| `modules/mass_battle/battle_loop.py` | the four call sites of section 1; `:408-413` becomes a `stand_draw` per unit, with a unit that `breaks` routed and the others standing |
| `references/troops.yaml` | `stand` (the obstacle table and the on/off arm); `armour.*.rally_step` |
| `FieldOutcome` and its parts (`engine/season/queries/inputs.py`) | `fight_loss`, `pursuit_loss`, `taken`, `gave_ground` (the pessimist proposal's `pursuit_loss` per side becomes per part) |
| `engine/season/loop/effects_combat.py::_eff_march` | writes `body` from `fight_loss` and the untaken part of `pursuit_loss`; puts `taken` on the band Event; hands named captives to the `capture` custody write |

## Gate (execution artifacts)

1. `stand_draw: off`: digests equal to the amended pessimist proposal's tree.
2. `stand_draw: on`, cavalry charging unbraced levy frontally, n 200: some fields end with the levy broken at
   a `fight_loss` below 0.15, some with it giving ground, some with it standing; the same charge on a braced
   pike body breaks it in fewer fields than it breaks the levy, and in more than none over 400 if the seeds
   allow (reported, not forced). `assert checked >= 200`.
3. A general removed at tick 3 of a ten-unit army, n 200: the count of units that break is neither 0 nor 10
   in most fields.
4. A wing of horse that beats its opposite with the order `enemy_broken: hold` is in the fight at the next
   tick in some fields and absent in some; with `pursue` it is absent in all, and the body it chased shows
   `pursuit_loss` above zero.
5. Over 200 routed fields with mounted pursuit: `taken` is zero in some and above zero in some; the season
   fold of one such field leaves the taken persons in custody with `body` unchanged by the pursuit.
6. Rally: a routed side of unarmoured foot rallies in more fields than the same side in heavy armour, same
   seeds, same general.

## Falsifier

A body that never breaks below its casualty floor with the draw on; a general's fall that routs every unit in
every field; a victor that is always available after its opponent breaks; a captive whose `body` was scaled
by the field; any of these draws returning one band at every seed.

## NERS (definitions `CLAUDE.md` §0.06; E last)

- **N.** From history's direction: a charge, a flank and a fallen officer are how battles were decided, and
  none can decide one here. From the player's: horse, a held reserve and a living general each gain a use.
  From the season's: prisoners exist. Laterally: personal combat has yield and capture after a decided
  fight. Cut the stand draw and every battle is an attrition race to a sixth of the men; cut the victor's
  draw and envelopment is free.
- **R.** Keep the horse in hand or let it chase; guard the general; spare or take. With no player: the wing
  that chased and never came back; the levy that ran at the first charge and lived.
- **S.** One draw function, on the module's own ladder, called at four events; existing states for all three
  results; one rearguard constant and one recall rule already in the file.
- **E, against that.** One function, one table, one trigger, four outcome fields; a certainty removed.

## Cost class

Small build, after the amended pessimist proposal and the typed outcome. One declared flip (`stand_draw`).
