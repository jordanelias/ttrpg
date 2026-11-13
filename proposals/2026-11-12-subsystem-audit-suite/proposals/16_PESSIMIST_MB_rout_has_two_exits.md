# MB · a rout has two exits: rally and pursuit, each a draw, inside the one engagement a season fights

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` Part 2) — three joins. (1) **A-5, A-6, A-7**: `rally_roll` and `recall_check` draw on the one sampler; their pool comes from the general's **command** (a learned skill with social and mental attributes, A-59: `proposals/27_MB_*`, another lane's), where the text has `roll_pool(unit.command)`; the sampler is `U5b_MB_rulings_in_the_field.md` §1. A-61 confirms the stand draw beside the 15% band (`26_MASS_BATTLE_rout_pursuit_and_giving_ground.md` §1). (2) **A-3, A-57, A-58**: a rallied side is still the field's loser, so the band is `Won` for the other and, on land the loser held, the land and its seats pass; rally saves men, not the place (`26_MASS_BATTLE_aggression_and_land.md` §2). (3) The two per-side fields ride the typed `FieldOutcome` (`04_MB_typed_outcome_and_one_path.md` as reconciled), and men taken in a pursuit reach custody only through `14_VERBS_PHYSICAL_A`'s custody write. `Pursue` returns to the menus with this proposal (`U5b_MB_residue.md` §1).

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: `R5_READ.md` §1 (a): "under the same scoped RNG" replaced by
keyed draws (A-30); §2 (A-69, A-78, A-3: the outcome's fields are per part with the part's end state, the pursuit loss
split into permanent and recoverable kinds) as narrowed by U1 D-U1-11e (`FieldOutcome`'s fields are declared once:
`rallied`, `pursuit_loss`, `taken` by `26_MASS_BATTLE_rout_pursuit_and_giving_ground.md`; the end state is the band,
`field_degree_bands`; this file supplies the values and re-declares no field) and C3-L11 (fled and injured are kinds on
the army Record's loss ledger, recovered when read, `27_MB_E`); §7/§7b (test file, tier); U3 B19. **DISPUTED, R5 §1 (b)**
("graded on the module's ladder is the second ladder D 30 refuses; grade on `degree_from_net` via `seam/ladder.py`"):
`modules/mass_battle/resolution.py::compute_degree` (`:104-119`) is the ruled ladder spelled out on purpose (the module
takes no `engine.*` import), held equal to `degree_from_net` by `tests/valoria/test_degree_ladder_single_owner.py`, and
`seam/ladder.py` is host-side, which a module may not import; so it is one ladder, guard-held, not a second, and the
rally is graded on it. Changed: step 1's draw and grade wording, step 5 and the edits-table outcome row, the "depends on
nothing" sentence, the gate's test file. A-98 vocabulary lane (2026-11-12, A-98; ledger `unified/work/A98_SWEEP.md`): "trained score/rank" → skill score (1).

## Status: PROPOSED

Reconciled: 2026-11-12, A-100/A-101 supersession pass (MBA-04 step 5; `master/mb_abstraction/MBA_DESIGN_part3.md` §8.1): this file STANDS except the **pursuit damage law, NARROWED** (step 2's `pursuit_damage` "as coded" and step 3's pool `subunit_combat_pool(unit, atom)`): pursuit casualties are the contact draw under the `pursuit` matchup row, one law; `may_pursue`, `rally_roll`, `recall_check` and the rout's two exits are unchanged. `freed_attacker_damage` and `run_multi_unit_battle` leave with the legacy harness, not converted.

Lands in batch: **B19** (MB), last before the calibration targets (U3 §1 item 19). Depends on:
`04_MB_typed_outcome_and_one_path.md` (B17, the typed outcome), `14_VERBS_PHYSICAL_A_custody_and_force.md` (B15, custody
for the taken), `26_MASS_BATTLE_rout_pursuit_and_giving_ground.md` and `27_MB_A_command_and_the_obedience_draw.md` (B19:
the outcome fields and the Command draw).

Folded: 2026-11-12 by `audits/27_MB_COMMAND_AND_DYNAMIC_STRENGTH.md` (rulings A-69 and A-59). Nothing here is deleted. (1) **A-69** (`unified/DECISIONS_ANSWERED.md:90`): some losses are injury or flight and not death, so some numbers recuperate. This file's three rally bands are what decide flight: a side that is **rallied** or that **withdraws in order** has no fled men; a side that **runs** loses a drawn share of its survivors to flight, who are alive, off the strength, and may return later (`27_MB_E_what_an_army_carries_back.md` §1, §3). "Rally saves men, not the place" (the Reconciled line) is therefore literal. Men lost to `pursuit_loss` stay dead or taken. The outcome's per-side fields become per part and gain the part's end-state word. **Ruled since, A-78** (`unified/DECISIONS_ANSWERED.md:103`): the dead, the captured and the deserters are permanent; the injured and those who fled and regrouped return in part even when the beaten commander does nothing. So step 2's `taken` are permanent to the loser, and the men who ran are not all lost: some regroup and drift back, some desert. **Not established** in the tree's research: the share that flees, how many of them desert, and the rate and window of return; each is a parameter with a control and no shipped value. (2) **A-59**: `rally_roll` and `recall_check` are Command draws on the commander's `CommandRecord` (trained `command` as dice; Presence and Reason as levels), their obstacles steps over the one task obstacle (`27_MB_A_command_and_the_obedience_draw.md` §6). They are among the named draws that carry a field's chance once the side-wide multiplier is lowered or removed, and each is listed on the result (`27_MB_C` §3).

Folded: 2026-11-12 by `audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md` (rows B-7, B-8, R-3, R-4, R-10). Nothing here is deleted. **The sources read at the page confirm the finding**: the decisive losses of the beaten came after they broke, by pursuit or encirclement, and where pursuit was limited the beaten lost about a seventh (Krentz; Sabin: `research/historical/mass_battle_casualties_and_results_grounding.md` A1, A4, A6, A7, A12). Five amendments, detailed in `26_MASS_BATTLE_rout_pursuit_and_giving_ground.md`. (1) **Rally by what the troops carry**: step 1's Ob 2 takes a step from the routed side's armour and mounts (unarmoured and mounted easier, heavy foot harder), on Sabin's reading that light troops ran, outdistanced pursuit and rallied and heavy troops rarely could. (2) **The dead and the taken**: `pursuit_loss` is divided by a draw into killed and taken alive (about half of a beaten Roman-era army's loss could be prisoners); the taken are not written as `body` loss and go to the custody `14_VERBS_PHYSICAL_A_custody_and_force.md` owns. Both fields become per part. (3) **The pursuer pays**: a pursuing body is out of the fight and re-enters the next bout tired; the commander may recall it at the lull by the `recall_check` this proposal already uses. (4) **Pursuit inside a bout**: when a body's opponent breaks and the field goes on, the victor draws Discipline (read with its standing order on `enemy_broken`) to hold or chase; step 2's end-of-field pursuit stands for what is left. (5) **Magnitude**: the measured 73% of survivors lost in one pursuit call puts the loser's loss with pursuit near the top of what the sources support (two to five times the loss without); `26_MASS_BATTLE_calibration_targets.md` T-3 reads it, and the falsifier below already names the constant to re-read. Also: under rulings A-57 and A-58 "a rallied side is still the field's loser" has a consequence this file should carry: on a march onto land another holds, a rallied defender has lost the land (`26_MASS_BATTLE_aggression_and_land.md` §2).

Lane MB (the outcome's fields are IN's, declared by `26_MASS_BATTLE_rout_pursuit_and_giving_ground.md`). Carries
resolution 5 of `audits/16_PESSIMIST_MB.md` §5 and its finding F-PES-MB-03. Depends on the B19 files named above; composes
with `04_MB_typed_outcome_and_one_path.md` (the typed outcome) and with the addendum's
`04_MB_manager_battle_one_resolver.md` (a commander's action at a window). Reference, not mechanism
(`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

Every field that ends with one side routed, and nothing else. Today such a field stops, the routed
side keeps about two-thirds of its men and stays where it stood. After this change, before the field
returns: the routed side's commander may stop the rout (a draw), and if he does not, the winner's
mounted bodies may ride the routed down (a draw each, recallable). A declared hash mover wherever a
field is fought to a rout; in natural play today that is no field at the shipped scale (first audit
F-MB-01, F-MB-03).

## The problem (evidence: `audits/16_PESSIMIST_MB.md` §2.7; run `p6_rout.py`)

- The premise "a routed army can be rallied or destroyed in pursuit" fails at every depth.
- `orchestration.rally_check` is `pass`. A routed side un-routed in 0 of 60 trials of three further
  between-turn recoveries, phase boundaries and engagement turns. The only code that clears a rout,
  `reset_morale_between_battles`, does so with no roll and has no caller in `engine/` or `modules/`.
- `orchestration.pursuit_damage` is called only by `run_multi_unit_battle`, which no season path
  reaches. It is gated on `pursuer.speed == "Fast"`; a side of cavalry, light cavalry or mounted
  archers built by `orderofbattle.build_unit` has `Unit.speed == 'Standard'`, so the gate is one no
  season unit can pass. With the speed set by hand, one call removes a mean 73% of the routed side's
  survivors (zero in 1 of 115); with speed `Standard`, nothing in 115 of 115.
- The role `Pursue` is on three troop types' menus (`config.TROOP_TYPE_ROLES`) and its instruction
  `pursue` is mapped to `None` in `hierarchy/units.py::ROLE_INSTRUCTION_PRIMITIVES`.
- At the end of a mirror field the loser has lost 37% of his men (n 200) and the winner 7%.

## The resolution, decided

Both exits run **once, at the end of `run_battle`, when exactly one side is routed**, in this order.
Each is a draw keyed by its purpose (A-30; `04` PART D 35): the rally `H(seed, tick, field id,
"rally:<side>")`, each pursuit `H(seed, tick, field id, "pursuit:<body id>")`, through the one keyed-draw
owner the module receives on its input; no generator is threaded. Neither is a fixed function of state
(`AUDIT_BRIEF.md`, the standing rule).

1. **Rally.** The routed side's commander makes a Command draw on his `CommandRecord` (`command` skill score as
   dice, Presence and Reason as levels; its obstacle a step over the one task obstacle, with the armour and
   mounts step of `26_MASS_BATTLE_rout_pursuit_and_giving_ground.md` (1): `27_MB_A_command_and_the_obedience_draw.md`
   §6), on the one sampler (A-5). A side whose general is out does not roll. Graded on the module's
   `compute_degree`, the ruled ladder held equal to `degree_from_net` by
   `tests/valoria/test_degree_ladder_single_owner.py`:
   Success or better, the side is **rallied**: `routed` clears, morale is set to one step above zero
   (not to its start), it does not re-enter the fight this field, and it is not pursued. Partial: it
   is not rallied but withdraws in order, and pursuit against it rolls at the rearguard penalty the
   file already has (`REARGUARD_PENALTY`, 2 dice). Failure: it runs.
2. **Pursuit.** For each unrouted body of the winning side that may pursue, in body order: the
   winner's general rolls `recall_check` if that side's standing order says "do not pursue" (default:
   no such order, no recall roll); a body not recalled rolls `pursuit_damage` against the routed side
   as coded, and the damage is applied to the routed side's cells by the existing
   `distribute_casualties`. A feint declared by the routed side is resolved first by the existing
   `resolve_feigned_retreat`, which is thereby reached for the first time.
3. **Who may pursue** is read from the troop registry, not from `Unit.speed`: a body pursues if
   `registry.is_mounted(troop_type)` or it carries the `pursue` instruction (the `Pursue` role, which
   thereby gets its primitive: light infantry told to pursue do, at foot pace, see step 4).
   `pursuit_damage` takes the pursuing **subunit**; its `pursuer.speed != "Fast"` test is replaced by
   that predicate, and its pool is `subunit_combat_pool(unit, atom)`, the owner every melee pair
   already reads. *(NARROWED by A-100, MBA-04 step 5: there is no pool; the predicate stands, the damage is the contact draw under the `pursuit` row.)*
4. **Foot pursues at a cost.** A body that pursues by instruction and is not mounted rolls at
   `REARGUARD_PENALTY` fewer dice. One constant, already in the file, read twice.
5. **The outcome says what happened.** `resolve_field` supplies, per part, the values of the typed fields
   `26_MASS_BATTLE_rout_pursuit_and_giving_ground.md` declares on `FieldOutcome` (D-U1-11e: `rallied`,
   `pursuit_loss` divided by a draw into killed and `taken`); the part's end state is the field's band
   (`field_degree_bands`, A-3: a rallied side is still the loser). The men who ran from an unrallied side
   are written as the `fled` kind on the army Record's loss ledger and the wounded as `injured`; both are
   recoverable and their recovery is computed when read (`27_MB_E_what_an_army_carries_back.md`, C3-L11; A-78:
   some return even if the beaten commander does nothing). The shares that flee, desert or are injured are
   **not established** in the tree's research: parameters with a control (0) and no shipped value. This file
   declares no field; the values ride the band Event's `observed` as `observation_terms` members for the
   report (D-U1-06).

Values named here (`REARGUARD_PENALTY`, "one step above zero") are the file's own existing constants or the
smallest non-zero step; they are seeds, and they are Jordan's to tune. The earlier `Ob 2` is replaced by
`27_MB_A` §6's obstacle form. The form is what is decided.

## Exact edits

| file · owner | edit |
|---|---|
| `modules/mass_battle/orchestration.py::rally_check` | stays the phase-boundary hook and stays empty; its docstring says rally is the end-of-field draw and names `rally_roll`. (A per-phase rally inside a field is the manager proposal's "general's action", not this.) |
| `modules/mass_battle/orchestration.py` | new `rally_roll(unit) -> str` (the degree), beside `recall_check`; `pursuit_damage(pursuer_unit, pursuer_atom, routing_unit, *, rearguard=False)` with the predicate of step 3; new `may_pursue(atom) -> bool`, the one owner of that predicate |
| `modules/mass_battle/battle_loop.py::run_battle` | after the tick loop and before `winner` is computed: the sequence of steps 1 and 2; the return gains `a_rallied`, `b_rallied`, `a_pursuit_loss`, `b_pursuit_loss` |
| `modules/mass_battle/hierarchy/units.py::ROLE_INSTRUCTION_PRIMITIVES` | `'pursue': ('pursuit', 'orchestration.may_pursue')` |
| `modules/mass_battle/massbattle.py::_grade` | passes the values through; a rallied side is still the field's loser (it left the field) |
| `engine/season/queries/inputs.py::FieldOutcome` | no edit here: the fields are `26_MASS_BATTLE_rout_pursuit_and_giving_ground.md`'s (D-U1-11e); this file fills them per part |
| `modules/mass_battle/orchestration.py::run_multi_unit_battle` | calls the new signature; no behaviour change intended there beyond the predicate |

No new verb, no new Event kind, no new fixture. Where the beaten army goes afterwards is the first
audit's F-MB-11 and its proposal, not this one.

## Gate (execution artifact)

`p6_rout.py` was lane scratch, not in the repository. Its rows become NEW `tests/valoria/test_mass_battle_rout.py`
(the mass-battle marker): `test_rallied_in_some_not_all`, `test_cavalry_pursues_infantry_without_pursue_role_does_not`,
`test_pursued_loser_loses_more_than_unpursued`, `test_rally_and_pursuit_draws_are_keyed_by_purpose` (the same field id
and side give the same draw whatever else ran). Command: `python -m pytest tests/valoria/test_mass_battle_rout.py -q -m mass_battle`.
Over 200 seeded mirror fields that end in a rout,

1. the routed side is rallied in some and not in all (both counts above zero);
2. a winner holding a cavalry body inflicts `pursuit_loss > 0` in some fields and 0 in some; a winner
   of heavy infantry with no `Pursue` role inflicts 0 in all; with the role, above 0 in some;
3. mean loss of an unrallied, pursued loser exceeds that of an unpursued one;
4. `assert checked >= 200` on the fields counted (`CLAUDE.md` §0.1 pt 2).

Goldens that include a rout move and are re-recorded, said plainly in the commit.

## Falsifier

A seeded field in which a routed side with a standing general is neither rallied, nor withdrawn, nor
exposed to a pursuit roll by a mounted enemy body. Or: rally succeeding in every field, or pursuit
destroying the loser in every field (either is a certainty, which the standing rule excludes; the
first measured pursuit magnitude, 73% of survivors with one zero in 115, is close enough to certain
that the gate's row 2 may fail on it, in which case `CASUALTY_SCALE`'s use in `pursuit_damage` is the
value to re-read, not the form).

## NERS (definitions `CLAUDE.md` §0.06; E last)

- **N.** Top-down: a field that ends in a rout has a second act, so a defeat and a destruction are
  different results. Bottom-up: mounted troops and a general's Command gain a use they do not have.
  Lateral: personal combat has yield and capture after a decided fight; the field gets its like.
  Vertical: the season receives a loss that depends on what both commanders had (horse; a living
  general). Diagonal: a standing order ("do not pursue") reaches a result. Horizontal: both sides run
  the same two steps. Cut it and what dies is the only consequence of having cavalry after the line
  breaks.
- **R.** A reason to keep horse in reserve; a reason to protect one's general; a story with no player
  (the pursuit that destroyed them; the stand that saved them).
- **S.** One pool owner, one recall rule, one rearguard constant; pauses correctly (it runs after the
  fight and before the return, so the season sees one outcome).
- **E, against that.** Two short functions and a predicate, replacing two dead hooks and a gate no
  unit can pass.

## Cost class

Small build. Tier: `sonnet`, effort `high`; the flight and desertion shares are parameters at a control with no
shipped value (not established). Hash movers declared: every field fought to a rout; goldens re-recorded once in
B19, said plainly. Lands it: B19, order `may_pursue` → `rally_roll` → `pursuit_damage`'s new signature → `run_battle`'s
sequence → `_grade` and the outcome values.
