# MB · the army between battles: veterancy and upkeep on the unit row, by the owners the campaign already has

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` Part 2) — two changes. (1) **The standing rule** (`audits/14_VERBS_MILITARY.md` §0.5 lists this file's fixed rule): a unit that stood does not gain `experience` with certainty; the write in §1 is one draw for each eligible unit on the one sampler, the gain on Success or better (`U5b_MB_rulings_in_the_field.md` §5). The conditions for eligibility, the reset on destruction and the dilution rule stand as bookkeeping. Arrears stay arithmetic (they set odds); what unpaid men do is drawn in `14_VERBS_MILITARY_C_the_muster.md` (`discharge_troops`' Failure band; the dispersal draw). (2) **A-2** confirms the carrier: `experience` and `arrears` are columns of the unit row (the ruling's own list names experience); no unit holds a history of its own.

## Status: PROPOSED

Lane MB for the two data columns and the two battle-side effects; FA and SE own the acts that pay and
supply (named below, not designed here). Carries R-42 of `audits/04_MB_audit_addendum_B.md` §B6 and its
§B5.2. Depends on the troop file (`04_MB_unit_loadout_and_weapon_in_hand_B.md` stage 1) and on the first
MB lane's typed outcome with per-unit parts (`04_MB_typed_outcome_and_one_path.md`). Reference, not
mechanism (`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

With the two columns at their seeds (`experience` 0 on every unit, `upkeep` 0 on every troop row):
nothing. With veterancy on: a unit that fights and survives on a side that did not lose fights its next
field one step of Power better, up to two steps, and a unit that is destroyed starts again. With an
`upkeep` above 0 on a troop row and the arrears rule on: a unit whose troops went unpaid for a season
starts its next field one step of Discipline lower. Both are declared movers behind closed rosters with
today's behaviour as the control. No natural season fights an army field today.

## The problem

- Jordan's referent: "a campaign-scale party and army economy (troops recruited, trained, tiered, upkept
  and lost; companions; a commander whose own fighting and leadership matter)" (`AUDIT_BRIEF.md:315-317`).
  What the corpus sources of Bannerlord (`research/game_precedent_suite/tutorials/T02_warband.md:16-20`,
  `tables/R2_warband_sandbox.md` rows F1, E6, A5): recruits from settlement notables; upgrades bought with
  a troop's experience, coin and, for cavalry, a horse; food and wages drawn every day, and "unpaid or
  unfed troops lose morale, then desert"; party speed falling with size and carried weight; a result
  screen of kills, upgrades, dead, wounded and routed. Total War and Field of Glory II Medieval carry the
  same persistence (`tables/R6_mass_battle_campaign.md` rows E6, M3: upkeep each turn; a core army that
  gains experience, and "units with no losses gain no experience").
- The archived design already has both rules in its own words (intent only): **Experience** as Fresh,
  Seasoned, Veteran, +1 Power a step within the faction's ceiling, gained by surviving a battle the
  faction won or drew, lost with the unit, the higher kept on a merge
  (`military_layer_v30.md` §1.6); and **unpaid professionals lose Discipline** each season while levy and
  light troops do not, with no automatic recovery (§1.7).
- In the code: recruiting by training site is built (`troop_types/recruitment.py`); a veteran and a
  recruit of one type are identical (first audit §14 (d): "no advancement"); nothing pays an army
  (`engine/season/hole_register.yaml` H-158 is about a seat's upkeep of the persons obliged to it, and the
  FA audit reads "no computed act pays upkeep"); the one ration debit is shipped off
  (`settlements.provision`, SE audit).
- Losses are already real and already land where they should: a field scales the bodies of the cohorts an
  army drew from (`parties["fielded"]`), so "lost" needs nothing.

## The resolution, decided

### 1. Veterancy: `experience` on the unit row

- Army Record, unit row: `experience: 0 | 1 | 2` (default 0). No new Record kind, no unit object: a fact
  on the row the amendment of ED-IN-0306 already makes a typed record
  (`architecture/meta/04_CODE_ARCHITECTURE.md:813`).
- Troop file header: `veterancy: {arm: off | steps, power_per_step: 1, max_steps: 2}`; `off` is the
  control. The values are the archived design's, transcribed as seeds.
- **Read:** `armyrecord.to_order_of_battle` hands each unit's `experience` on; `orderofbattle._spec_for`
  adds `power_per_step * experience` to the troop row's `power` for that unit. One addition, at the one
  place a unit's stats are assembled.
- **Write:** `engine/season/loop/effects_combat.py::_eff_march`, on a band that is not `Lost` for the
  unit's side, for each unit whose part in `FieldOutcome.parts` (a) lost troops and (b) did not rout:
  *(Reconciled, the standing rule: one draw for each eligible unit, pool the unit officer's `command` score by the one pool rule, else the commander's, else the untrained default; obstacle `veterancy.ob` plus one a step already held; on Success or better)* `experience += 1` up to the cap, through the army verbs' one write path
  (`armyrecord.apply`). A unit whose part is destroyed (share 0) is reset to 0. Condition (a) is the
  Field of Glory rule (a unit that stood in reserve and was never touched learns nothing) and keeps the
  write from being a clock.
- **Dilution, so that recruits matter:** `assign_troops` into a unit with `experience > 0` lowers it by
  one step when the troops added exceed half the unit's strength after the assignment. One rule, in
  `armyrecord.assign`. (The archived design keeps the higher of two merged units; that makes experience
  free to launder, so the lower-on-majority rule is proposed instead and marked as a departure.)

### 2. Upkeep: a column, and one consequence

- Troop row: `upkeep` (whole units of the treasury's coin per hundred troops per season; seed 0 for
  every row, so nothing is charged at landing). The archived design's distinction is expressed by the
  rows: levy and light troops at 0, professionals above it.
- **Who pays, and how, is not designed here.** The campaign has an owner for "a seat pays, per term,
  those it keeps" (`queries/world_q.py::upkeep_of`, `loop/effects.py::_renewals`, H-158
  `[UNVERIFIED beyond the register row: neither function was opened]`). The edge mass battle needs from
  FA and SE is one query: *for this army, were its troops paid last season?* The cheapest faithful form
  is for the army's holder's seat to owe `sum(upkeep x troops / 100)` through that same path, to the
  cohorts the troops were drawn from.
- **The consequence mass battle owns:** an `arrears: int` on the unit row (seasons unpaid, written by the
  campaign side), read at `_spec_for` as `discipline -= min(arrears, discipline - 1)` for a row whose
  `upkeep` is above 0. Paying resets it. A unit at Discipline 1 through arrears is the "lose morale, then
  desert" shape with the engine's own consequences: it advances slowly, cannot hold a demanding shape and
  breaks early. Desertion itself (troops leaving the row) is `discharge_troops`, an existing verb, given
  by the cohort; whether a cohort chooses it is the chooser's.
- Supply stays SE's: when `field_provisioning` is on and the stores bound a side's fielded troops, that
  side's morale-start drops by one (the stance row that already feeds it), so "unfed" has its
  consequence without a second supply model. One line in `seam/wrappers/mass_battle.py::field_input`.

### 3. What is named and not built

- **Speed against carried weight on the march** (sourced, Bannerlord). A `march` resolves in the round it
  is declared (`ED-IN-0301`); there is no march clock to slow, so the loadout's weight cannot bite at
  campaign scale. It needs travel time first, which is CORE's.
- **Companions with roles** (scout, surgeon, quartermaster, engineer): persons holding posts in an army
  are the manager proposal's `officer`; further posts are capability content (CHAR).
- **Prisoners and ransom** (sourced, Warband): the custody edge exists and a field writes none (first
  audit §5.5); the squad proposal's outcome names the fallen, which is the input a `capture` needs.
- **Tiers as an upgrade tree** (recruit → veteran → elite as different troop rows): not proposed. With
  `experience` a unit improves in place; a tree would need a rule for changing a unit's troop row, coin
  and a training Site, and belongs with the troop-stock design held on M3
  (`proposals/2026-10-16-troop-stock-design.md`).

## Exact edits

| file (owner) | edit |
|---|---|
| `references/troops.yaml` (MB) | header `veterancy`; column `upkeep` |
| `modules/mass_battle/armyrecord.py` (MB) | unit row gains `experience`, `arrears`; `assign` applies the dilution rule; `to_order_of_battle` carries both |
| `modules/mass_battle/orderofbattle.py` (MB) | `Subformation.experience`, `.arrears`; `_spec_for` applies them to `power` and `discipline` |
| `engine/season/loop/effects_combat.py::_eff_march` (IN) | the experience write, per part |
| `engine/season/rosters.yaml: record_kinds.values.army` (IN) | the unit row's key set |
| `engine/season/seam/wrappers/mass_battle.py::field_input` (IN) | the unfed step on morale-start, under `field_provisioning` |
| FA, SE | the payment path and the `arrears` write: their proposals |

## Gate (execution artifacts)

1. `veterancy.arm: off`, every `upkeep` 0: `python3 tools/ci_golden_modes_check.py` digests equal; the
   season pins unchanged.
2. A hand-built army field folded twice with `steps`: after the first, the unit that lost troops and
   stood reads `experience` 1 and the untouched reserve reads 0; in the second, that unit's subunit is
   built at `power + 1`; a unit destroyed in the second reads 0 after it.
3. Module, n 200 against the same-run control: the same army with its line at `experience` 2 wins more
   than at 0, beyond the control's spread (a reading of mechanism, not a balance target).
4. `assign_troops` adding more than half a unit's strength lowers `experience` by one; adding less does
   not.
5. A unit row with `upkeep` above 0 and `arrears` 2 is built at `discipline - 2` (floor 1); the same
   troop row at `upkeep` 0 is not.
6. With `field_provisioning` on and stores bounding one side, that side's morale-start is one lower than
   in the same field with full stores.

## Falsifier

Experience gained by a unit that took no losses, or kept by one that was destroyed; a veteran unit that
fights exactly as a fresh one; arrears that lower a levy; any result that moves with the arm `off` and
every `upkeep` 0; a second payment path beside the seat's.

## NERS (definitions `CLAUDE.md` §0.06)

- **N.** From the campaign down: without something worth keeping, an army is a number to spend, and a
  commander has no reason to refuse a battle. From the battle up: the outcome already says which unit
  stood. Lateral: `train` raises a person's capability and nothing raises a unit's. Cut it and the
  Bannerlord referent is a recruiting rule and nothing else.
- **R.** A veteran unit is worth protecting (the archived design's phrase); a war chest decides what kind
  of army can be kept; the world's armies age into different things with nobody watching.
- **S.** Two facts on a row that already exists, read at the one place a unit's stats are assembled and
  written at the one place a field's result is; payment rides the seat's existing path.
- **E, last.** Two columns, one header row, two effects of one line each. A player can say why the old
  guard held: they had stood before.

## Cost class

Section 1: small build, after the typed outcome's per-unit parts. Section 2: an edit on this side;
design-first on FA's and SE's. Section 3: none.

## Conflicts with ruled items, named

- The 2026-07-08 directive puts troop quality in the pool ("troop type, quality and numbers");
  `experience` is quality and enters as Power, which is consistent with it.
- CL-TROOP and CP-T04-10 (the troop stock; raise and keep a force) are held on M3. This proposal adds no
  stock and no verb; it should be read with the first audit's disposition of those rows.
