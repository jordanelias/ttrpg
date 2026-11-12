# VERBS · MILITARY · D — the order of battle: `form_unit`, `assign_troops`, `disband_unit`, `order_unit`

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` Parts 3–4; `U5b_VERBS_military_physical_residue.md`) — (1) **Layer 1**: the four rows write one cell on every band, so each is a task row with **flat** `writes:` and `emits:` (residue §1, shape (a)); `unit.unformed`, `assign.balked`, `unit.balked` and `order.unheeded` are the `draw` clause of `emits_on_refusal`; `disband_unit`'s Partial emits `army.disbanded` only and carries the half that went home as an Observation (`discharged`), not as a second kind; the band still reaches the module as `args['band']`. The roster is `graded_tasks`. (2) **A-5, A-6, A-7, A-25**: one sampler; the pool rule on `command`; `disciplined` is a named level for the roller. (3) **D-36** is closed by the ladder: three organising verbs. **A-2**: `raw` is a column of the unit row. **A-1**: every battle runs the one resolver on what these rows wrote, so `order_unit` matters to a battle nobody watches. (4) Whether a standing order is obeyed in the field now has an owner: the obedience draw of `26_MASS_BATTLE_maneuver_orders.md` (audit 26 B-3).

## Status: PROPOSED

Folded: 2026-11-12 by `audits/27_MB_COMMAND_AND_DYNAMIC_STRENGTH.md` (rulings A-59 and A-69). Nothing here is deleted. (1) **Who rolls the field-side draw.** The obedience draw audit 26 gave an owner is rolled, for a standing order, by the unit's **officer** on his own `command`, and by the commander only for a unit with none or for an order he improvises (`27_MB_A_command_and_the_obedience_draw.md` §3). The capability is the one Edit 4 gives these four verbs, defined once, with Presence and Reason as its talent. So two columns of the unit row become choices `order_unit` carries: `officer`, and on the army's own row `commander_post`, where he rides (`27_MB_D_the_commander_as_chooser.md` §1). (2) **`raw` and Discipline** are read by that draw as the `unsteady` step and the `disciplined` level, the same two terms Edit 4's table gives `order_unit`. (3) **Edit 1's `raw`, and `experience` and `arrears`, are a unit's own prowess** in A-59's sense: columns of its row, read by one function (`27_MB_B_unit_prowess_on_the_row.md`). (4) **A-69**: `assign_troops` on a unit with men who fled is their recall, drawn as this file draws it, with the cohort's stance toward the commander and the unit's arrears as terms; `options()` reports units with absent men; `understrength` and `disband` read `assigned` after losses are written to the row (`27_MB_E_what_an_army_carries_back.md` §2, §3). Whether fled men return without a recall is not established and is the other arm of that file's switch.

Folded: 2026-11-12 by `audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md` (rows B-3, M-5, S-1). Nothing here is deleted. (1) **§5's "standing orders obeyed in the field, which is the resolver's draw (listed for MB)" now has an owner**: an order that fires in the field takes effect by a draw on Command and Discipline, at the one site an order is applied (`26_MASS_BATTLE_maneuver_orders.md` §1). **`raw` is read there too**: a raw body's orders are a step harder to obey, beside the one step of Discipline Edit 1 gives it. The season-side draw of this proposal (`order_unit` taken in whole, in part, or not) and that field-side draw are two different acts and do not double-count: one is whether the order was given to the body, the other whether the body carries it out under contact. (2) The doctrine rows this proposal's `step` reads gain the manoeuvre set as data (same file §3); `off_doctrine` compares against them unchanged. (3) The unit row's `ranks` and `files`, which this proposal leaves to `04_MB_cell_hierarchy_as_data.md`, have sourced seeds there now (two cell rows for sword and spear foot, four for pike).

Grounded: 2026-11-12 by `audits/25_GROUNDING_ENGINE.md` (G-04) — a typed conjunct cannot be waived by a payload key; the proposal's stated fallback is now the edit.

Batch M-D of `audits/14_VERBS_MILITARY.md` (§4, §5.3, §6). Source: F-VM-03; `audits/04_MB_audit.md`
F-MB-03, F-MB-13, F-MB-16; `audits/04_MB_audit_addendum_B.md` §B3.3, §B4.3, §B5.4;
`AUDIT_BRIEF.md` "Standing rule" and the mass-battle intent (army, unit, subformation, troops; orders
set in advance; one resolver). It lands after proposal C, whose mechanism (the class, `army_state`,
the doctrine step, the keys, the Observations) it reuses without restating. Nothing is ratified by
being written.

## 1. What it changes in `engine/season/` at runtime

1. The holder of an `army` Record forms the four rows on it through the one chooser, each only when
   the army's state calls for it (troops with no body; troops in no body; a body under the rout
   floor; orders that differ from the doctrine's or a footing that differs from the faction's).
2. Each is one draw, written by band: a body is formed steady or raw; men join in whole or in
   part; a body is broken up, or breaks and half go home, or will not be broken; an order is taken
   in whole, in part, or not.
3. The unit row gains `raw`; the field reads a raw body one Discipline lower.
4. With `armies_at_build: off` (shipped) nothing forms; hashes EQUAL.

## 2. The problem (evidence)

- `aperture 2 0`: the four rows formed 0; `army.formed`, `army.assigned`, `army.disbanded`,
  `army.ordered` never emitted. `disband_unit`, `discharge_troops` and `order_unit` have no caller
  outside tests and the menu (`harness/army_presets.py` gives `recruit`, `form_unit`,
  `assign_troops` only).
- `probe_army_s0.txt`: by hand each executes with certainty; a repeated order is
  `order_unit.refused` (the module's no-op decline), the one refusal that already teaches nothing
  to anyone, since `Fixtures withheld_verbs` keeps every person from forming it.
- `armyrecord.options` already computes `subformation_routs`, `army_routs`, `unassigned` and
  `levy_never_closes` for the menu's display; no NPC reads them
  (`audits/04_MB_audit.md` F-MB-16).
- Trained troops in no subformation do not fight (`armyrecord.to_order_of_battle`), so an army an
  NPC only recruits never fields anybody.

## 3. Exact edits, by owner

**Edit 1 — the module** (`modules/mass_battle/armyrecord.py`; owner MB).

- The subformation row gains `raw: bool` (default `False`; `validate` accepts its absence).
  `to_order_of_battle` passes it to `orderofbattle.Subformation`, which lowers the built unit's
  Discipline by one, floor 1. `[ASSUMPTION; medium; Jordan to correct; revert: the field unread.]`
  One number, in the troop table when it lands (`raw_discipline_step`), in `config.py` until then.
- `options(q)` gains three booleans beside proposal C's two: `unformed` (trained troops of a kind
  with no subformation and a free slot), `understrength` (the existing `subformation_routs` test),
  `off_doctrine` (a subformation whose role, stance, target or fall-back differs from its doctrine
  row's, or `facts.footing_wanted != record['footing']`). `unassigned` is the existing advisory.
- `step(record, op, facts)` for the four ops. `form`: one subformation per kind in `trained` that
  has none, named `<kind>-<n>`, role from the doctrine (`presets.ROLE_OF` today). `assign`: every
  trained trooper into the subformations of its kind, filling the weakest first. `disband`: every
  subformation under `SUBUNIT_ROUT_FLOOR`. `order`: for each subformation, the fields that differ
  from the doctrine row's; and `footing` set to `facts.footing_wanted`.
- `_apply` honours `args['band']` for the four (the host passes the ladder's band name, an opaque
  string the module compares to its own exported tuple `BANDS`):

  | op | Overwhelming | Success | Partial | (Failure never reaches the module) |
  |---|---|---|---|---|
  | `form` | formed, `raw: False` | formed, `raw: False` | formed, `raw: True` | |
  | `assign` | all move; the body's `raw` cleared | all move | half move (rounded up); a body whose strength more than doubles turns `raw` | |
  | `disband` | removed; all to the pool | removed; all to the pool | removed; half to the pool, half discharged | |
  | `order` | set; `raw` cleared | set | `role` and `stance` set, the other fields left | |

- `order` accepts `footing` alone and `doctrine` alone, as it accepts `strategy` alone
  (`armyrecord.py:324-327`). MB's `standing_orders` (§B4.3) ride the same op when that proposal
  lands; nothing here anticipates their shape.

**Edit 2 — stems** (`engine/season/data/requires.py`): `unformed`, `unassigned`, `understrength`,
`off_doctrine`, relation stems of `subject` and the actor, answered by `world_q.army_state`
(proposal C, Edit 2); none world-only. `footing_wanted` is `war` when `world_q.at_war` holds for the
army's faction against any faction, else `peace`; with FA's `06_FA_war_lives_in_seats_B.md` that is
a seat's word.

**Edit 3 — the rows** (`engine/season/verb_table.yaml:1945-2059`). Each keeps its stratum,
beneficiary and first two conjuncts, takes `recruit`'s class column (proposal C, Edit 4) and
eligibility `["own"]` unchanged (FA: organising and ordering are the roll-holder's, not a seat's),
and changes as follows.

```yaml
  - verb:        "form_unit"
    referent_class: Record
    requires_typed:
      all:
        - {form: existence, of: subject, kind: army, conjunct: army}
        - {form: relation,  of: subject, relation: held_by,  conjunct: command}
        - {form: relation,  of: subject, relation: unformed, conjunct: need}
    writes: {Overwhelming: ["Record.subject_matter"], Success: ["Record.subject_matter"], Partial: ["Record.subject_matter"], Failure: []}
    emits:  {Overwhelming: ["army.formed"], Success: ["army.formed"], Partial: ["army.formed"], Failure: ["unit.unformed"]}
    emits_on_refusal: {army: ["form_unit.refused"], command: ["form_unit.refused"], need: ["form_unit.refused"], write: ["form_unit.refused"]}

  - verb:        "assign_troops"
    referent_class: Record
    requires_typed:
      all:
        - {form: existence, of: subject, kind: army, conjunct: army}
        - {form: relation,  of: subject, relation: held_by,    conjunct: command}
        - {form: relation,  of: subject, relation: unassigned, conjunct: need}
    writes: {Overwhelming: ["Record.subject_matter"], Success: ["Record.subject_matter"], Partial: ["Record.subject_matter"], Failure: []}
    emits:  {Overwhelming: ["army.assigned"], Success: ["army.assigned"], Partial: ["army.assigned"], Failure: ["assign.balked"]}
    emits_on_refusal: {army: ["assign_troops.refused"], command: ["assign_troops.refused"], need: ["assign_troops.refused"], write: ["assign_troops.refused"]}

  - verb:        "disband_unit"
    referent_class: Record
    requires_typed:
      all:
        - {form: existence, of: subject, kind: army, conjunct: army}
        - {form: relation,  of: subject, relation: held_by,       conjunct: command}
        - {form: relation,  of: subject, relation: understrength, conjunct: need}
    writes: {Overwhelming: ["Record.subject_matter"], Success: ["Record.subject_matter"], Partial: ["Record.subject_matter"], Failure: []}
    emits:  {Overwhelming: ["army.disbanded"], Success: ["army.disbanded"], Partial: ["army.disbanded", "army.discharged"], Failure: ["unit.balked"]}
    emits_on_refusal: {army: ["disband_unit.refused"], command: ["disband_unit.refused"], need: ["disband_unit.refused"], write: ["disband_unit.refused"]}

  - verb:        "order_unit"
    referent_class: Record
    requires_typed:
      all:
        - {form: existence, of: subject, kind: army, conjunct: army}
        - {form: relation,  of: subject, relation: held_by,      conjunct: command}
        - {form: relation,  of: subject, relation: off_doctrine, conjunct: need}
    writes: {Overwhelming: ["Record.subject_matter"], Success: ["Record.subject_matter"], Partial: ["Record.subject_matter"], Failure: []}
    emits:  {Overwhelming: ["army.ordered"], Success: ["army.ordered"], Partial: ["army.ordered"], Failure: ["order.unheeded"]}
    emits_on_refusal: {army: ["order_unit.refused"], command: ["order_unit.refused"], need: ["order_unit.refused"], write: ["order_unit.refused"]}
```

**The `need` conjunct binds a doctrine step only.** A command with a payload is the commander
saying what he wants whether or not the doctrine calls for it (a player re-roling a body the
doctrine is content with). `[GROUNDED, 25 G-04: a typed conjunct cannot be waived by a payload key
without a new form (`data/requires.py:1027-1030`: a clause is one `form` of the closed
`requires_forms` roster and nothing else). So the conjunct is asked only at formation (`belief_contradicts`)
and in the effect for a payload-less act, `surrender`'s precedent of a faction test asked by the
effect and not the cell; the refusal key is then `write`.]`

**Edit 4 — the draw** (`engine/season/rosters.yaml`). `graded_inquiries.values` gains the four;
`verb_capability` gains each as `command`. Obstacle rows (SC-B's table; every number
`[ASSUMPTION; medium; Jordan to correct]`):

| verb | difficulty | modifiers |
|---|---|---|
| `form_unit` | the kind's `drill_difficulty` (troop table; until it lands, `recruit`'s stand-in) | `no_training_place` +1 (no Site of the kind's training kind where the commander stands) |
| `assign_troops` | 1 | `influx_exceeds_body` +1 · `body_raw` +1 |
| `disband_unit` | 1 | `body_experienced` +1 a step (MB R-42's `experience`, 0 until it lands) · `arrears` +1 |
| `order_unit` | 1 | `many_fields` +1 (more than two fields change) · `body_raw` +1 · `disciplined` −1 (the kind's Discipline 4 or more) · `undisciplined` +1 (Discipline 1) |

**Edit 5 — effects** (`engine/season/loop/effects_army.py`). `_apply(w, a, op, args, kind, res)`
gains `res`: on `Failure` the band's kind and no write; otherwise `args['band']` from the ladder
and, for a payload-less act, `facts` from `army_state`. Every Event carries the four state
Observations after the write (proposal C's shape), so the commander's belief follows his own acts.

**Edit 6 — fixtures.** `withheld_verbs` drops the four. `rosters.yaml: army_verbs`' note loses its
"no person forms one" sentence.

**Edit 7 — the unplayed commander.** `harness/army_presets.py::install` stays as the
`armies_at_build: mustered` arm. Its docstring's "the plan is deterministic: it draws nothing"
becomes false of the result (its folds now draw) and stays true of the plan; it says so.

## 4. Gate and falsifier

- **Execution artifact.** `aperture 3 s`, s = 0 to 2, `armies_at_build: empty`, after MB's
  `04_MB_headcount_grade_and_scale.md`: all six `army.*` kinds leave the never-emitted list; at
  least one faction's army holds a subformation with troops assigned by acts that passed through
  DELIBERATE; `_order_of_battle` returns an order of battle for it. With PHYSICAL's `march`
  formation landed: one `field.won`, `field.lost` or `field.drawn` fought from such an army.
- **The draw.** One hand-built act of each of the four on `build_realm(0)`, 200 seeds: all four
  bands occur for each; the record after each band is the table's (a Partial `form` is `raw: True`;
  a Partial `disband` leaves the pool half the body's men; a Partial `order` changes `role` and
  `stance` only).
- **State sets the odds, and people differ.** Two commanders, `command` 5 and none, equal cohorts
  and doctrine, three seasons, 50 seeds: the count of steady (not raw) bodies with troops differs
  between them beyond sampling error. A reading of mechanism.
- **Downstream.** A field between two equal armies, one all `raw`, n 200 through
  `massbattle.resolve_field`: the raw army's win share is lower, and not 0. If it is 0 or equal,
  the `raw` step is mis-sized or unread; both are failures of this proposal's one number.
- **Control.** `armies_at_build: off`: hashes EQUAL. The route rows removed: each act is certain.
- **Falsifier (planted).** `raw` not passed to `Subformation`: the downstream gate reads equal
  shares. `off_doctrine` always true: a commander orders the same body every season (the act store
  shows a repeat with no change of record). The `band` argument ignored: two record outcomes, not
  three.

## 5. Layer 1, and what is not built

`audits/14_VERBS_MILITARY.md` §6 names the two passages. This build stays on the amended text
(ED-IN-0306, `04_CODE_ARCHITECTURE.md:813`): a body is a row of a Record a person holds; `raw` is a
column; nothing but a person acts; the field is the one resolver, run on what these rows wrote. Not
built here, each with its owner: posts and formations as data, ranks and files (MB,
`04_MB_cell_hierarchy_as_data.md`); the second weapon and `in_hand` (MB `_B`, PC
`03_PC_loadout_and_carry.md`), which will ride `order_unit`'s payload and the standing orders;
`officer` on the row (MB R-40), which is what puts a named person with a body; standing orders
obeyed in the field, which is the resolver's draw (listed for MB in the audit's §0.5).

## 6. NERS reading (E last)

- **N.** From below: `to_order_of_battle` fields only assigned troops, so without these rows a
  raised army is nobody. From above: Jordan's manager (composition and orders set in advance, the
  battle resolved from them). Laterally: the player's menu and the NPC's cell ask one function.
  Across scales: a commander's season act becomes the field's starting state.
- **R.** Composition and orders are a commander's signature and can miscarry; a veteran body may
  refuse to be broken; with no player, armies are drilled well or badly by the people who hold
  them. Complete at the extremes: an order to a body that does not exist is refused by name; a
  twelfth body is refused; a failed act leaves the roll exactly as it was.
- **S.** One state function; one band table in the module; the same draw as every graded act; the
  unit row's new field is read where the unit is built and nowhere else.
- **E, against that.** One field, three booleans, four stems, four route rows, one band argument.
  A player can predict: a good commander with a drill ground makes steady bodies; a poor one in
  the field makes raw ones.

## 7. Cost class

Small build (module, rows, one effect body). No mover at the shipped fixtures. The field gate
depends on MB's scale and grade and on a `march` that reaches a defended place.
