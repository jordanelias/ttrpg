# MB · one scale for the cell, the tick and the battle: sixteen men, four seconds, bouts with lulls

## Status: PROPOSED

Lane MB (the scene sequence is IN's). Carries rows S-1, B-9, R-5 and R-6 of
`audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md`. Amends, and does not replace,
`04_MB_cell_hierarchy_as_data.md` (the `deployment` header), `04_MB_unit_loadout_and_weapon_in_hand_B.md`
(per-arm `range`) and `04_MB_playable_field_scenario.md` §C. Sources:
`research/historical/mass_battle_movement_and_behaviour_grounding.md` (**MV**),
`…_casualties_and_results_grounding.md` (**CR**), `…_maneuver_sequences_grounding.md` (**SQ**),
`…_wargame_models_grounding.md` (**WG**). Reference, not mechanism (`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

Three things, each behind its own control. (1) Nothing: the scale is written down and read by the report
only. (2) With per-arm ranges and the approach rule on: a field with missile troops starts a missile range
apart, so shooting happens before contact and not through it. (3) With `max_bouts` above 1: a field that is
drawn after one bout is fought again in the same scene, on what is left, until one side breaks, a commander
withdraws, or the bouts run out. Each is a declared hash mover wherever an army fights; none moves a natural
season today (`audits/04_MB_audit.md` F-MB-03).

## The problem

- The engine has no stated scale. `troop_types/registry.py:92-93` declines "an unratified
  meters-per-lattice-unit conversion". Its constants imply two different ones.

  | constant | fits a cell of about 4 m, 16 men | fits a cell of about 25 m, 200 men |
  |---|---|---|
  | men a cell | 11–23 in the tier table every instrument fights (`04_MB_cell_hierarchy_as_data.md`) | `CELL_CAP = 200` (`config.py:39`), the season's packing today |
  | support depth 1, 2, 3 cell rows for sword, spear, pike (`…_B.md` §2) | 4, 8 and 12 ranks: a Roman line of about six, the hoplite eight, the phalanx sixteen (MV F3) | 25 to 75 m of men behind the front: nothing |
  | volley 2–8 cells (`config.py:188-189`) | 8–32 m: a javelin (20–25 m, ACOUP in CR) | 50–200 m: a bow (about 200 m, SQ 5) |
  | field 51 cells (`config.py:14`) | about 200 m: room for 900 men eight deep | 1.3 km: room for 10,000 |
  | one cell a tick on foot (`geometry.py:328-338`) | a tick of about 4 s at 57 m a minute (MV M3, snippet tier) | a tick of about 26 s |
  | 18 ticks (`config.py:425`) | about 70 s: one clash | about 8 minutes |

- Season armies are 60 to 900 men (`recruitment.under_arms_cap`, weight x 30:
  `04_MB_headcount_grade_and_scale.md`). Only the left column gives such an army ranks, and the suite's
  arrangement proposal already chooses it (16 a cell). On that column the volley range is wrong for bows and
  the three-row approach (`orderofbattle.py:67`) is about twelve metres: there is no missile phase, which is
  why reached archers shoot through the melee (`audits/04_MB_audit.md` F-MB-19).
- The tree's research proposes a 50 m tile and a 5-minute turn (`research/pre_firearms_formations/14_…:89`,
  `15_…:311-318`). On this engine that is foot at 0.6 km/h. It was written for another design.
- A battle took hours and was mostly stand-off between brief clashes (CR C1–C5; MV T1, `[D]`). The season
  fights one 18-tick engagement and returns. Measured by the first MB lane: an even engagement is usually
  indecisive, and still so over four engagements' worth of ticks (`04_MB_playable_field_scenario.md`).

## The resolution, decided

### 1. The scale, written once

`references/troops.yaml`, in the `deployment` header `04_MB_cell_hierarchy_as_data.md` adds:

```yaml
deployment:
  cell_troops: 16          # that proposal's seed; this is why
  scale:                   # what the numbers stand for. Read by the report; by no resolver.
    cell_m: 4              # 16 men at about 3 ft of front and of depth each: four files by four ranks (MV F1)
    tick_s: 4              # one cell at an ordinary marching pace (MV M3; snippet tier: a seed)
    bout_ticks: 18         # ROUTE_BUDGET_TICKS; a bout is one clash, about seventy seconds
    bout_minutes: 30       # a bout and the stand-off before the next, as the report tells it
  max_bouts: 1             # the control: today's field. Seed for the flip: 6
```

- `cell_m` is derived, not measured: Sabin's reading of Polybius and Vegetius is three to six feet of front a
  man (`[D]`); three feet each way gives 16 men a 3.7 m square. It is the only one of these with a
  page-read source. `tick_s` rests on a snippet and says so. `bout_minutes` and `max_bouts` are chosen so that
  a full battle reads as about three hours, Vegetius's upper figure as Sabin reports it (CR C2), and are
  seeds.
- **Abstraction that is right:** the hours of stand-off are not simulated; they are the lull. The board shows
  the last fifty metres of the approach, not the last four hundred.
- The 50 m tile and 5-minute turn are not adopted.

### 2. Missile range per arm, and deployment a missile range apart

- `arms.<key>.range` (`…_B.md` §2, where every missile arm is `[2, 8]`) takes the stated scale's values:

  | arm | range, cells | ground | tier |
  |---|---|---|---|
  | `javelin` | `[1, 6]` | 20–25 m for the heaviest javelins | `[T]` ACOUP |
  | `bow`, `crossbow` | `[2, 40]` | about 200 m; some say 300 for the longbow | `[T]` W-CRE |
  | `sling`, `siege` | `[2, 8]` | **not established**; today's value kept | — |

  `[2, 8]` for every arm stays as the control arm.
- `formations.<name>.approach_rows` becomes a rule with a floor: the longest `range[1]` among the missile
  arms on either side, capped so both lines fit the field, floor 3. Two armies with no missiles start three
  rows apart as now. An army facing bows starts in range and must cross it.
- A bow's rate against a crossbow's is sourced ("up to ten arrows per minute" against "about twice a minute",
  W-CRE). `volleys` per arm (`…_B.md`) stays 10 for both until Jordan sets it: at four seconds a tick neither
  rate is a volley a tick, and the engine's volley is a tick's worth of shooting, not one arrow.
- With bows reaching the board, ammunition is what ends the shooting, which is what the page read says of
  Agincourt (SQ 5 step 5). The `volleys_spent` trigger of `…_B.md` then has something to fire on.

### 3. A battle is bouts with lulls

- A field scene is a sequence of at most `max_bouts` calls of the one entry, `massbattle.resolve_field`. A
  later bout is fought when the one before folded `Drawn` and neither commander withdrew. Its input is the
  first bout's with three things carried: each part's surviving troops, each part's stamina
  (`entry_stamina`, per part), each part's morale. Nothing else is state.
- **The lull between bouts is the commander's window.** In it a played or chooser-served commander takes
  one `GeneralAction` (`04_MB_manager_battle_one_resolver.md` §4); the lull adds three that only make sense
  out of contact, each a row of `26_MASS_BATTLE_maneuver_orders.md`: `relieve` (two units of one post swap
  lines), `reform` (shape, ranks, files, weapon in hand), `commit` (a `reserve` post joins the line). Rested
  columns recover in the lull by the column ledger's existing between-turn rule.
- The scene's end state is ruling A-3's, read at the last bout: won, lost, or drawn when the bouts run out
  ("night ends it": SQ 10 step 7). Ruling A-9 is what makes a scene a short sequence whose step may hang on
  the band before it; this is that, for the field.
- **One resolver** (ruling A-1): every bout is the same call. A delegated battle runs the same sequence with
  standing orders in place of the commander's lull actions. Replay holds bout by bout from the interventions
  list.
- This amends `04_MB_playable_field_scenario.md` §C, which left a drawn field to the next season round's
  acts. Those acts remain for a battle that is still drawn after the last bout.
- The season calls the entry once per bout. `run_multi_turn_battle` is not revived; the first MB lane's
  removal of it from `modules/` stands.

## Exact edits

| file (owner) | edit |
|---|---|
| `references/troops.yaml`, `tools/export_troops.py` | `deployment.scale`, `deployment.max_bouts`; per-arm `range` values; `approach_rows: auto` with the floor |
| `modules/mass_battle/orderofbattle.py::_place` | reads the approach rule; `_APPROACH_ROWS` becomes the floor's default |
| `engine/season/queries/inputs.py::MassBattleInput` | `entry_stamina`, entry troops and entry morale may be given per part (the per-side form of `16_PESSIMIST_MB_one_stamina_ledger.md` is the one-part case) |
| `engine/season/seam/wrappers/mass_battle.py::resolve` | the bout loop: call, read the band, stop or build the next input from the outcome's parts; forwards the lull to `host.decide` |
| `FieldOutcome` (`04_MB_typed_outcome_and_one_path.md`) | `bouts: int`; `report` is per bout; a duration line is `bouts x bout_minutes` |

## Gate (execution artifacts)

1. `max_bouts: 1`, every range `[2, 8]`, approach 3: `tools/ci_golden_modes_check.py` digests equal.
2. Bows at `[2, 40]` against foot, n 200: volley events before first contact are above zero in every field;
   with the control ranges they are at most two ticks' worth.
3. An archer body with no switch order: its volley count after its first tick in contact is zero (with the
   contact rule of `…_B.md` as amended).
4. A javelin body does not shoot at an enemy seven cells off; a bow body does.
5. `max_bouts: 6` on an even field, seeds 0 to 199 against the same seeds at 1: the share of fields ending
   `Drawn` falls; no field calls the entry more than six times; a field decided in bout 1 is field-for-field
   equal to the one-bout run.
6. A delegated six-bout field and the same field replayed from its recorded interventions: equal in every
   part. The report's duration reads between 30 and 180 minutes.

## Falsifier

A second battle loop anywhere under `modules/`; a bout whose input carries anything but troops, stamina and
morale; a resolver constant that reads `scale`; shooting through a melee by the body being fought.

## NERS (definitions `CLAUDE.md` §0.06; E last)

- **N.** From the designer: no constant can be judged without a scale, and two lanes had started to assume
  different ones. From the player: an archer's range and a pike's depth are now on one ruler. From history:
  the lull is where a commander did his work. Cut the bouts and the field is a draw machine or an attrition
  machine, which are the two things the sources say a battle was not.
- **R.** Reserves, relief and re-forming become decisions; a defender can make an attacker cross a beaten
  zone; complete at the extreme of one bout (today).
- **S.** One entry called several times; pauses at a boundary that already exists; the same methodology as a
  duel's rounds.
- **E, against that.** Five numbers, one rule for the approach, one loop in the wrapper.

## Cost class

Section 1: edit. Section 2: edit plus one declared flip. Section 3: small build, after the `Drawn` band and
the typed outcome. Calibration after rulings A-5 and A-6 move the sampler, not before.
