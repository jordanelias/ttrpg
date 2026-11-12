# MB · a rout has two exits: rally and pursuit, each a draw, inside the one engagement a season fights

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` Part 2) — three joins. (1) **A-5, A-6, A-7**: `rally_roll` and `recall_check` draw on the one sampler; their pool comes from the general's **command** (a learned skill with social and mental attributes, A-59: `proposals/27_MB_*`, another lane's), where the text has `roll_pool(unit.command)`; the sampler is `U5b_MB_rulings_in_the_field.md` §1. A-61 confirms the stand draw beside the 15% band (`26_MASS_BATTLE_rout_pursuit_and_giving_ground.md` §1). (2) **A-3, A-57, A-58**: a rallied side is still the field's loser, so the band is `Won` for the other and, on land the loser held, the land and its seats pass; rally saves men, not the place (`26_MASS_BATTLE_aggression_and_land.md` §2). (3) The two per-side fields ride the typed `FieldOutcome` (`04_MB_typed_outcome_and_one_path.md` as reconciled), and men taken in a pursuit reach custody only through `14_VERBS_PHYSICAL_A`'s custody write. `Pursue` returns to the menus with this proposal (`U5b_MB_residue.md` §1).

## Status: PROPOSED

Folded: 2026-11-12 by `audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md` (rows B-7, B-8, R-3, R-4, R-10). Nothing here is deleted. **The sources read at the page confirm the finding**: the decisive losses of the beaten came after they broke, by pursuit or encirclement, and where pursuit was limited the beaten lost about a seventh (Krentz; Sabin: `research/historical/mass_battle_casualties_and_results_grounding.md` A1, A4, A6, A7, A12). Five amendments, detailed in `26_MASS_BATTLE_rout_pursuit_and_giving_ground.md`. (1) **Rally by what the troops carry**: step 1's Ob 2 takes a step from the routed side's armour and mounts (unarmoured and mounted easier, heavy foot harder), on Sabin's reading that light troops ran, outdistanced pursuit and rallied and heavy troops rarely could. (2) **The dead and the taken**: `pursuit_loss` is divided by a draw into killed and taken alive (about half of a beaten Roman-era army's loss could be prisoners); the taken are not written as `body` loss and go to the custody `14_VERBS_PHYSICAL_A_custody_and_force.md` owns. Both fields become per part. (3) **The pursuer pays**: a pursuing body is out of the fight and re-enters the next bout tired; the commander may recall it at the lull by the `recall_check` this proposal already uses. (4) **Pursuit inside a bout**: when a body's opponent breaks and the field goes on, the victor draws Discipline (read with its standing order on `enemy_broken`) to hold or chase; step 2's end-of-field pursuit stands for what is left. (5) **Magnitude**: the measured 73% of survivors lost in one pursuit call puts the loser's loss with pursuit near the top of what the sources support (two to five times the loss without); `26_MASS_BATTLE_calibration_targets.md` T-3 reads it, and the falsifier below already names the constant to re-read. Also: under rulings A-57 and A-58 "a rallied side is still the field's loser" has a consequence this file should carry: on a march onto land another holds, a rallied defender has lost the land (`26_MASS_BATTLE_aggression_and_land.md` §2).

Lane MB (the outcome's two new fields are IN's, on the record the first MB lane proposes). Carries
resolution 5 of `audits/16_PESSIMIST_MB.md` §5 and its finding F-PES-MB-03. Depends on nothing; composes
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

Both exits run **once, at the end of `run_battle`, when exactly one side is routed**, in this order,
under the same scoped RNG. Each is a draw; neither is a fixed function of state (`AUDIT_BRIEF.md`,
the standing rule).

1. **Rally.** The routed side rolls its general's Command against Ob 2 (`roll_pool(unit.command)`,
   the form and the obstacle `recall_check` already uses for the same officer making the same kind of
   call). A side whose general is out (`command <= 0`) does not roll. Graded on the module's ladder:
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
   already reads.
4. **Foot pursues at a cost.** A body that pursues by instruction and is not mounted rolls at
   `REARGUARD_PENALTY` fewer dice. One constant, already in the file, read twice.
5. **The outcome says what happened.** `resolve_field`'s return gains, per side, `rallied: bool` and
   `pursuit_loss: float` (the share of its men lost after it routed). The host's band is unchanged
   (`Won` / `Lost`); the two fields ride on the band Event for the report and for any later reader.

Values named here (`Ob 2`, `REARGUARD_PENALTY`, "one step above zero") are the file's own existing
constants or the smallest non-zero step; they are seeds, and they are Jordan's to tune. The form is
what is decided.

## Exact edits

| file · owner | edit |
|---|---|
| `modules/mass_battle/orchestration.py::rally_check` | stays the phase-boundary hook and stays empty; its docstring says rally is the end-of-field draw and names `rally_roll`. (A per-phase rally inside a field is the manager proposal's "general's action", not this.) |
| `modules/mass_battle/orchestration.py` | new `rally_roll(unit) -> str` (the degree), beside `recall_check`; `pursuit_damage(pursuer_unit, pursuer_atom, routing_unit, *, rearguard=False)` with the predicate of step 3; new `may_pursue(atom) -> bool`, the one owner of that predicate |
| `modules/mass_battle/battle_loop.py::run_battle` | after the tick loop and before `winner` is computed: the sequence of steps 1 and 2; the return gains `a_rallied`, `b_rallied`, `a_pursuit_loss`, `b_pursuit_loss` |
| `modules/mass_battle/hierarchy/units.py::ROLE_INSTRUCTION_PRIMITIVES` | `'pursue': ('pursuit', 'orchestration.may_pursue')` |
| `modules/mass_battle/massbattle.py::_grade` | passes the four values through; a rallied side is still the field's loser (it left the field) |
| `engine/season/queries/inputs.py` (the typed outcome, when `04_MB_typed_outcome_and_one_path.md` lands) | the two fields per side |
| `modules/mass_battle/orchestration.py::run_multi_unit_battle` | calls the new signature; no behaviour change intended there beyond the predicate |

No new verb, no new Event kind, no new fixture. Where the beaten army goes afterwards is the first
audit's F-MB-11 and its proposal, not this one.

## Gate (execution artifact)

`p6_rout.py`'s rows, re-run on the changed tree, as one test in the file that covers `run_battle`
(`tests/valoria/`; the mass-battle marker): over 200 seeded mirror fields that end in a rout,

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

Small build.
