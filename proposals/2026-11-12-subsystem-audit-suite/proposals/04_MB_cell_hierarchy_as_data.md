# MB · the cell hierarchy as data: a unit's subformation, the scale of a cell, the army's formation, kinds within a unit

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` Part 2) — order and conformance only. (1) The `arm: grid` flip is a step of the one field calibration batch and lands **after** the pair rule changes (`16_PESSIMIST_MB_partition_and_the_pair_rule.md`: on the present rule every added body is a loss, and the grid multiplies bodies), on the one sampler (A-5) (`U5b_MB_rulings_in_the_field.md` §6 row 4). (2) A-2: `post`, `ranks`, `files` and `bands` are columns of the unit row; R-30's wording (a row of `subformations` is a unit) is the ruling's. (3) A-1: the harness's envelopment and refused-flank builders becoming formation rows is what keeps the season and the oracle on one deployment rule.

## Status: PROPOSED

Folded: 2026-11-12 by `audits/27_MB_COMMAND_AND_DYNAMIC_STRENGTH.md` (ruling A-59, clauses 2 and 3). Nothing here is deleted. (1) **Subformation is not a multiplier on a unit's dice.** `ranks`, `files`, `shape` and `distribution` decide which of a unit's cells are in a pair, how many ranks support them, which arcs are exposed and how fast a column tires; the unit's base dice are the same at any depth (`27_MB_B_unit_prowess_on_the_row.md` §2; its gate 5 is this file's gate 4 read from the other side). (2) **§4's `bands`**: the sum over cells that replaces the closed form is a sum of `prowess` by cell kind; the function is one. (3) **§3's formation rows and posts are what an army's strength is made of.** A-59: a static side-wide fighting value is misleading, the placement of units and their instructions relative to the opponent decide. Nothing computes or stores an army's strength; `27_MB_C_dynamic_strength_and_the_residual_chance.md` §1 lists where the resolver reads each term, and its gate 3 reads two formations of the same army against the same enemy. A formation row also gives a default post for the commander (`27_MB_D` §1).

Folded: 2026-11-12 by `audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md` (rows S-1, M-5, B-9). Nothing here is deleted; three things are added and one seed is questioned. (1) **The scale is stated**: `cell_troops: 16` is sixteen men in close order on about four metres square (four files by four ranks at three feet a man, Sabin on Polybius and Vegetius, read at the page: `research/historical/mass_battle_movement_and_behaviour_grounding.md` F1), a tick about four seconds, an 18-tick engagement one bout; the block `deployment.scale` and `max_bouts` are in `26_MASS_BATTLE_cell_scale_and_time.md` §1. (2) **`approach_rows`** stops being left at 3: it is the longest missile range on the field with a floor of 3 (same file §2), because at this scale three rows is twelve metres and there is no missile phase. (3) **`ranks` seeds against the sourced depths** (same note, F3): a cell row is four men deep, so `ranks: 2` is the hoplite's eight and a Roman line's six to ten, `ranks: 4` the phalanx's sixteen. The seeds proposed below (4 for foot, 3 for missile troops, 2 for horse) come from the tier table and make ordinary foot sixteen deep; the sourced seeds are **2 for sword and spear foot, 4 for pike, 2 for horse**, missile troops not established. Section 2's gate 4 (depth is a lever) is the reading that decides between them; both are seeds. (4) `ranks` and `files` become order-settable out of contact, at a cost in ticks (`26_MASS_BATTLE_movement_and_fatigue_as_data.md` §4).

Lane MB (the record edits are IN's). Carries R-30, R-32, R-33 of
`audits/04_MB_audit_addendum_B.md` §B6 and its §B3. Depends on the troop file of
`04_MB_unit_loadout_and_weapon_in_hand_B.md` (stage 1) and on the first MB lane's
`04_MB_headcount_grade_and_scale.md`. Reference, not mechanism (`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

Every field fought by an army, and nothing else. Today a season army of 600 to 900 troops is six to eight
cells, each body one rank deep at 200 troops a cell. After this change the same army is some forty to
sixty cells in bodies three to five ranks deep, laid out as the engine's own instruments lay theirs out,
so depth, rank support, flanks and local breaks have something to act on. A declared hash mover wherever
an army fights; no natural season fights one today (first audit F-MB-03). The cap arm reproduces today
exactly and stays as the control.

## The problem (addendum F-MB-20, F-MB-22; §B3.2)

- All three season constructors lay a body out at the densest density allowed (`massbattle.py:279`,
  `:329`; `orderofbattle.py:152`), so `cells = ceil(troops / cap)`. Run: the preset army of a weight-20
  faction is heavy infantry 2 cells, crossbow 1, cavalry 2, levy 1.
- The gauge, the law instrument and the reach tests build from the tier table: 9, 15, 25 and 35 cells in
  3 or 5 ranks at 100, 200, 400 and 800 troops (11 to 23 troops a cell). `footprint_for` at the cap gives
  1, 1, 2 and 4. Every calibrated magnitude was fitted on the first and is exercised on the second.
- Arrangement is a real lever that nobody can pull: 600 heavy infantry in one rank of twelve cells lose
  to the same 600 packed, 0 wins to 22 at n 40, with seven times the losses; 6 x 2 and 3 x 4 are inside the
  control's spread. `Subunit.width`, `depth` and `distribution` exist (`hierarchy/units.py:449-462`) and
  `armies.build_army` forwards them (`armies.py:300-306`); `orderofbattle.Subformation` has no such field.
- With one or two ranks, a weapon's reach class does nothing: pike and heavy infantry are identical in 440
  of 440 fields. The pike's edge is its third supporting rank
  (`tests/valoria/test_reach_weapon_class.py:132-144`).
- The army's formation is one rule in code (`orderofbattle.py:180-226`), marked an ASSUMPTION; the
  envelopment and refused-flank deployments live in `systems/mass_battle/sim/engine.py`, which a season
  cannot reach.

## The resolution, decided

### 1. Words (R-30)

At the designer's surface the levels are **army, unit, subformation, troops**, as Jordan states them:
an army is a deployment of units in a formation; a unit is a body with a troop kind, an officer and
orders; its subformation is how its troops are arranged in cells; troops are what a cell holds. In code:
`Unit`, `Subunit`, the subunit's footprint, the cell. The Record's key `subformations` keeps its spelling
(renaming a `subject_matter` key moves hashes for no behaviour) and `armyrecord.py`'s docstring states the
mapping once: *a row of `subformations` is a unit.*

### 2. The unit's subformation, and the scale of a cell (R-32)

Troop file header (`references/troops.yaml`):

```yaml
deployment:
  cell_troops: 16        # troops a cell at deployment. SEED: the tier table's density at 400 troops (25 cells)
  arm: grid              # grid | cap.  `cap` is today's packing and the control arm
```

Troop row: `ranks` (seed: 4 for foot, 3 for missile troops, 2 for horse; the tier table uses 3 and 5).
Unit row on the army Record (both optional): `ranks`, `files`.

Rule, in `orderofbattle._spec_for` and the two headcount constructors (one function, three callers):

```
ranks = unit.ranks or troop.ranks
files = unit.files or max(1, round(troops / (ranks * deployment.cell_troops)))
spec  = dict(width=files, depth=ranks)          # footprint_for's explicit-grid arm, which exists today
```

- Under `arm: cap` the constructors pass the cap as now.
- `footprint_for`'s explicit arm ignores the floor and cap by design ("per-cell density = troops/(width ·
  depth) falls out of the choice"), which is why it can reach the calibrated density and the
  concentration arm cannot (`geometry.py:114-121`).
- **Ladder.** Step 3: the archived design makes the soldiers in a block a function of the battle's scale
  (`mass_battle_v30.md` §A.3), and gives the player the per-cell count "within bounds … at muster"
  (§A.3b). Step 4: the tier table is the body every instrument in the tree fights. The 2026-07-22
  investigation's question to Jordan ("a minimum cells-per-subunit floor, or a UI …") is answered by
  those two; nothing is escalated.
- `cell_troops` is one number with a control. It is not a balance claim: the gate below reads mechanism
  (does depth exist, does the pike part from heavy infantry), not win rates.

### 3. The army's formation (R-33)

Troop file section:

```yaml
formations:
  line:                       # today's rule, transcribed: the control
    approach_rows: 3
    posts:
      front:   {rank_line: 0, across: centre}
      rear:    {rank_line: 1, across: centre}     # one clear row behind the front's depth
      left:    {rank_line: 0, across: left}
      right:   {rank_line: 0, across: right}
      reserve: {rank_line: 2, across: centre}
    default_post: {melee: front, missile: rear, mounted: [left, right]}   # alternating, as now
  envelopment:                       # the harness's build_envelopment, as a row
    approach_rows: 3
    posts: {front: {rank_line: 0, across: centre}, left: {rank_line: 0, across: wide_left}, right: {rank_line: 0, across: wide_right}, ...}
  refused_flank: { ... }             # the harness's build_refused_flank, as a row
```

- `OrderOfBattle.formation: str = 'line'`; the Record's `strategy` key carries it (see
  `04_MB_manager_battle_one_resolver.md`, which retires the stance strategies).
- Unit row: `post` (`front`, `rear`, `left`, `right`, `reserve`), default by the troop's class.
- `orderofbattle._place` becomes the reader of a formation row: it places each line by the depth of the
  line in front of it, and each post across the field, exactly as it does now for the one rule. It still
  degrades to one centred line when a layout does not fit.
- The timed release that makes an envelopment an envelopment (wings hold, then wheel) is not part of the
  formation row. It is a standing order on the wing units (`signal:` or `tick:`), which is where the
  2026-07-26 audit said the "emergent" envelopment's script really lives.

### 4. More than one troop kind in a unit (staged last; design-first)

Unit row, optional: `bands: ((troop_type, ranks), ...)`, front to rear; default one band of the unit's
`troop_type`. The engine seam is the one its own comments name:

- `Subunit.cell_kind: Dict[cell, troop_type]`, set at construction from `bands`, re-keyed with the other
  cell maps;
- `core/exchange.py::subunit_combat_pool`: the closed form `eff_power * eff_size` becomes the sum over
  cells of `power(cell_kind) * cell_troops / BLOCK_SIZE`, which it equals when every cell is one kind
  (the function's own comment, `:114-118`);
- reach, brace and support depth read the kind of the contact rank; the volley reads the cells whose arm
  in hand is a missile weapon; discipline and morale presets seed per cell (`cell_morale` already is).
- Ruled direction: Jordan, 2026-07-08, "subunit power is the aggregate or derivation of cell power"
  (`core/exchange.py:114`). Falsifier, from the synthesis: "a sub-unit whose cells differ in Q pools
  differently from its troop-weighted mean Q".

It is last because two units one behind the other already express most of it, and because it needs
bodies with ranks (section 2) before a band has a rank to occupy.

## Exact edits

| file (owner) | edit |
|---|---|
| `references/troops.yaml`, `tools/export_troops.py` (MB) | `deployment`, `formations`; `ranks` on each troop row |
| `modules/mass_battle/orderofbattle.py` (MB) | `Subformation` gains `post`, `ranks`, `files`; `OrderOfBattle` gains `formation`; `_spec_for` computes the grid; `_place` reads a formation row; `_rows_of` and `_spec_span` already take `width`, `depth` |
| `modules/mass_battle/massbattle.py` (MB) | `_weighted_unit`, `_person_unit` call the same grid function in place of `concentration=float(CELL_CAP)` |
| `modules/mass_battle/armyrecord.py` (MB) | `order` accepts `post`, `ranks`, `files`, validated against the exported sets; `to_order_of_battle` carries them |
| `engine/season/rosters.yaml: record_kinds.values.army` (IN) | the unit row's key set gains the three (the test that pins it to `armyrecord` follows) |
| `systems/mass_battle/sim/engine.py` (MB) | `build_envelopment`, `build_refused_flank` become thin callers of the formation rows, so the harness and the season deploy by one rule |

## Gate (execution artifacts)

1. `arm: cap`: `python3 tools/ci_golden_modes_check.py` digests equal; the addendum's `cells_probe`
   prints today's counts.
2. `arm: grid`: the same probe prints, for the weight-20 preset army, bodies of at least three ranks for
   every foot unit and an army of at least thirty cells.
3. **The pike parts from heavy infantry.** The addendum's `pike_probe` re-run on `grid`: the count of
   fields identical between a pike line and a heavy-infantry line is below 200 of 200.
4. **Depth is a lever.** Two equal heavy-infantry bodies, one at `ranks: 2`, one at `ranks: 6`, n 200
   against the same-run control: the win counts or the loss shares differ beyond the control's spread, in
   either direction; the result is recorded, not targeted.
5. A unit posted `left` in `line` starts left of the front line's left edge; an army with
   `formation: envelopment` starts with both wings wide of the centre, and the harness's own envelopment
   builder produces the same starting cells.
6. The law instrument and the gauge are re-read after the flip, because they and the season then fight
   the same bodies; their readings are reported, not gated.
7. Stage 4 (bands): the synthesis's falsifier, run.

## Falsifier

After the flip, a season-built foot unit of 200 or more troops in one rank; a field whose result under
`arm: cap` differs from today's; a formation whose season deployment differs from the harness's for the
same row; any gate above read as a balance target.

## NERS (definitions `CLAUDE.md` §0.06)

- **N.** Top-down: Jordan's structure names a subformation and the season has none. Bottom-up: the engine
  already resolves per cell and is handed one. Lateral: the instruments and the season fight different
  bodies; this makes them one. Diagonal: the loadout's second weapon cannot matter until this lands.
  Cut it and the cell layer stays what the 2026-07-26 audit called it: not load-bearing.
- **R.** Strategic thought (deep against wide, where to post the horse), customisation by row and by
  unit, completeness at the small end (a body of 100 is six cells in two or three ranks, not one cell).
- **S.** One cell-count methodology on every path (today two); one formation rule for the harness and
  the season; the scale stated once, with its control.
- **E, last.** One number, one column, three optional fields and a table of formations; in exchange the
  largest module in the tree fights on its own grid. A player can see why a line held: it was six deep.

## Cost class

Sections 1 to 3: small build plus one declared flip (`arm: grid`), after
`04_MB_headcount_grade_and_scale.md`. Section 4: design-first.

## Conflicts with ruled items, named

None found. ED-909 (an army formation is an emergent composition, never a subunit shape) is kept: a
formation row places units and gives them no shape. ED-1090 (eleven units) is unchanged. The stress
finding that "the 15-row approach leaves an 18-tick engagement about one tick of fighting" at 5,000 a side
(`ED-MB-0080`) bears on `approach_rows`, which becomes a datum here and is left at 3.
