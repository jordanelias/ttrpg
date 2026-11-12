# U5b — findings closure: PC, MB, and the MILITARY and PHYSICAL verb families

## Status: REFERENCE (a closure table for the suite; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Read at: 6910680 (working tree). Lane: U5b, a Fable unification-closure lane (UNIFICATION_BRIEF.md, "Closure rule").

`git diff --stat 601e715 HEAD -- modules engine systems tools references architecture` is empty, so every
code reading the family's audits took (at `601e715`, `2c24c81`, `2eba83c` and later suite heads) holds at
this head.

Every row closes one finding, correction, resolution row, survivor, verb verdict or adjudication row of
the documents this family owns, with exactly one disposition:

- **RESOLVED-BY** — a proposal in `proposals/` carries the exact edit at the single owner and a gate;
- **SUPERSEDED** — a later finding, ruling or reconciliation replaces it (cited);
- **STALE / FALSE-POSITIVE** — evidence at HEAD shows it no longer holds or never held;
- **DISPUTED** — this lane's evidence against it; the finding stays in its document, marked;
- **JORDAN** — two defensible options that survive the five-step ladder (CLAUDE.md §0).

A resolution is a plan for a later lane or session (the brief: *"Resolve is a plan, not an edit"*):
nothing here was executed against code, a registry or canon. Proposal paths are relative to
`proposals/2026-11-12-subsystem-audit-suite/proposals/`. Rulings are cited by their id in
`unified/DECISIONS_ANSWERED.md` (A-1 to A-56 and the ladder-closed D-rows); they supersede any lane
document. **Held, not closed here:** battle luck (D-34) and numbers in the melee dice (D-35), which
`audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md` and `proposals/26_MASS_BATTLE_*` (another lane, being
written; not on disk at this head) adjudicate. Rows that turn on either are closed SUPERSEDED to that
adjudication and name what they wait for.

Short names: `es/` = `engine/season/`; `mc/` = `modules/combat/`; `mb/` = `modules/mass_battle/`.

## Proposals this lane wrote (carriers for findings that had none, and the rulings folded)

| file | what it carries |
|---|---|
| `U5b_PC_rulings_in_the_fight.md` | the rulings that land inside `modules/combat/` and its seam and had no file: the nesting cap and the declared class of person-supplied callables (A-4); the fight's two inputs and the pool rule (A-6, A-7; U5a's CAP row B7, handed across); the wound carried into a fight as a level (A-8); the damage scale and the one combat calibration batch (A-31); the first-exchange edge on an unexpected opener (D-41 B, after A-16); the landing order of every PC proposal |
| `U5b_PC_residue.md` | PC items with no carrier: the slope bound and the read's literal scale; the grapple's names; the roster census before an inventory; the same-id refusal; the unseeded fallback; stale instrument text; the tempo flat-top's position; the lasting mark as a draw; the believed estimate of a fight; the test-strength items handed across by U5a |
| `U5b_MB_rulings_in_the_field.md` | the rulings that land inside `modules/mass_battle/` and its seam and had no single file (listed in Part 2) |
| `U5b_MB_residue.md` | MB items with no carrier (listed in Part 2) |
| `U5b_VERBS_military_physical_residue.md` | verb verdicts of the two families with no carrier (listed in Parts 3 and 4) |

Abbreviations for carriers. PC: **P1** = `03_PC_duel_chain_reach.md`; **P2** =
`03_PC_typed_outcome_one_door.md`; **P3** = `03_PC_exits_withdrawal_recovery.md`; **P4** =
`03_PC_person_inputs_content.md`; **P5** = `03_PC_duel_round_and_approach.md`; **PB** =
`03_PC_duel_round_and_approach_B.md`; **PX** = `03_PC_weapon_records_in_the_export.md`; **PF** =
`03_PC_weapon_form_at_round_start.md`; **PL** = `03_PC_loadout_and_carry.md`; **PES-A…D** =
`16_PESSIMIST_PC_A…D_*.md`; **18-D** = `18_DETERMINISM_no_certain_matchup.md`; **18-A** =
`18_DETERMINISM_task_draw_for_uncontested_verbs.md`; **PHY-A…D** = `14_VERBS_PHYSICAL_A…D_*.md`;
**MIL-A…D** = `14_VERBS_MILITARY_A…D_*.md`; **CAP** = `U5a_capability_home_and_two_inputs.md`; **DOE** =
`U5a_DICE_owed_edits.md`; **U1** = `unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md`; **RUL-PC** =
`U5b_PC_rulings_in_the_fight.md`; **RES-PC** = `U5b_PC_residue.md`; **RUL-MB** =
`U5b_MB_rulings_in_the_field.md`; **RES-MB** = `U5b_MB_residue.md`; **RES-V** =
`U5b_VERBS_military_physical_residue.md`. "plan" = a position of the active master workplan, cited by id.
Files of other closure families are cited by title and not re-closed.

---

# Part 1 — PC

## 1.1 `audits/03_PC_audit.md` — findings

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| F-PC-01 | computed play almost never reaches personal combat, and never by a duel | RESOLVED-BY | P1 (Exact edits: `referent_class: Person`, the person-side `dispute` decline, Record-kind formation); the missing occasions: `22_HAPPENINGS_C_a_killing_is_a_crime_someone_commits.md` (A-16; U5d's, by title) and plan CR-91 (the war context) | audit E7, E7b, E12 (`aperture 2 0`: `challenge` 84 of 84 refused, `fight` formed 0) |
| F-PC-02 | every person is the same fighter | RESOLVED-BY | P4 Parts A–D as reconciled (home and schema are U1 §1–§3; the pool slot is two inputs, A-7); RUL-PC §2 | audit E8 (83 of 83 default) |
| F-PC-03 | a fight's consequences reach other subsystems only as a death and a body | RESOLVED-BY | P2 Part A (`DecisiveBeat`, `fell_to`); PES-C (the scene's shape, `fell_to_hand`); the survivor's regard stays plan CP-T03-06 with CHAR (`02_CHAR_scar_is_a_wound.md`, U5a's, by title) | audit E3 (0 stance rows in 400 fights), E11 |
| F-PC-04 | a plain `fight` is binary for its loser; the roll is top-heavy | RESOLVED-BY | P3 Part B as reconciled (adopts PHY-A A3, the mortal-wound draw and `context_terms`); PES-A (the yield as a draw under every term); the roll's top-heaviness: RUL-PC §4 (A-31, the damage scale) | audit E3 (a death in 200 of 200), E5 |
| F-PC-05 | the one in-fight choice is free, and only a played person has it | RESOLVED-BY | P3 Part A (the contested withdrawal); PB §4–§5 (every party has a decider) | audit E6 (52.0% → 14.3%) |
| F-PC-06 | the module returns an untyped dict; the seam returns twelve keys, the fold reads two; `winner` contradicts the scene | RESOLVED-BY | P2 Part A as reconciled (the flip is replaced by 18-D's tracked riposte, so `result` and the trackers agree by construction) | audit E3 (11 of 200), E11 |
| F-PC-07 | one engine, two doors; the registered door is the narrower | RESOLVED-BY | P2 Part B | `workbench/server.py:15-37`; `mc/fight.py:55-56` |
| F-PC-08 (a) | `core.resolve` inlines `net_boost` | RESOLVED-BY | P2 Part C, R-PC-17 | audit E10 |
| F-PC-08 (b) | nine bespoke Bernoulli or logistic gates beside the ladder | SUPERSEDED | the bands are ruled exempt (audit §5); the one gate that decided an outcome by fiat, the upset flip, is 18-D's; the yield threshold is PES-A's; the armour average is PES-D's. The remaining gates are in-fight draws (the standing rule asks a draw, and they are draws); their move onto the ladder is not ordered by any ruling | `mc/wrapper.py:344-357`, `:434`, `:622` |
| F-PC-08 (c) | the Ob a person is attacked against reads the fallback and practice; SC's opposition reader excludes both | RESOLVED-BY | CAP Part B row B5 (`opposed_ob`, one owner, one `opposition_rate`); RUL-PC §2 (what the combat seam passes as the opposition) | `mc/core.py:102-124` |
| F-PC-08 (d) | `core.py:58` rounds the pool to an integer | RESOLVED-BY | RUL-PC §2 edit 3 (the pool is carried raw; A-5's bell curve takes a fractional pool) | `mc/core.py:58` (`int(round(faculty))`, re-read at HEAD) |
| F-PC-09 | the tradition, ability and lever layer is unreachable from the season and near-silent in the module | RESOLVED-BY | P4 Part A (the layer becomes authoring data composed host-side into `lever` and `skill` slots, U1 §2–§3); nothing is added to it before a carrier exists (R-PC-19); the decision to adopt or cut is plan PC-21 | audit E5 (47.8% against a 46.1–49.3 band) |
| F-PC-10 | 18 engine constants outside `CFG` and the export | SUPERSEDED | by F-PC-15 (addendum C-8: 64 constants and every weapon field); carried by PX and P2 Part C R-PC-18 | addendum E-B1, E-B3 |
| F-PC-11 | flat-module and prose debt (path inserts, dead citations, handoff pointers, CR-85 Status, the tempo flat-top) | RESOLVED-BY | P2 Part C (R-PC-15, R-PC-16); RES-PC §6 (the flat-top named on plan PC-08's Phase-C row; the workbench `trace.py` shadow). The path inserts are the declared shrink-only seam (`engine/substrate/pc_engine.py`, CLAUDE.md §3) and get no edit | audit E10 (16 dead citations) |
| F-PC-12 | no unarmed fighter; "holds no arms" means an arming sword | RESOLVED-BY | P4 Part C | audit E2 |
| F-PC-13 | the duel and the grid round are not one path: no round entry, no approach | RESOLVED-BY | PB as reconciled (§2 the round, §3 the approach, §7 the order), with RUL-PC §1 (the nesting cap) and §5 (the order behind A-31) | `mc/wrapper.py:576-615`; addendum §B3 |
| F-PC-14 | inside a fight an NPC is not an agent | RESOLVED-BY | PB §5 (`choose.approach_of`, one decider per claimant); PES-A (the concession); P3 Part A (the withdrawal) | `mc/wrapper.py:586-592` (`decide=None`) |

## 1.2 `audits/03_PC_audit.md` — §5 disagreements, §6.1 dispositions, §6.2 resolutions

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| §5 "no matchup is ever certain" | the cap moves `result`; the fold reads trackers | RESOLVED-BY | 18-D (the riposte through the one damage site) | `mc/wrapper.py:618-624` (re-read at HEAD) |
| §5 a wound's persistence | `party_end` cuts Endurance by band; the tracker starts clean | RESOLVED-BY | RUL-PC §3 (A-8: the carried wound is a level against the wounded fighter's rolls, the Endurance cut retired; one ladder for one quantity) | `es/seam/wrappers/combat.py:143-152` |
| §5 the beaten yield, flee or die | plain `fight` is lethal | RESOLVED-BY | P3 Part B as reconciled; PES-A | audit E3 |
| §5 every fighter differs | mechanisms present, sources empty | RESOLVED-BY | P4 | audit E8 |
| §5 the player decides once per engagement over six intents | one binary choice per turn | SUPERSEDED | by the 2026-11-12 intent and R-PC-27/R-PC-40 (three approaches over three phases); carried by PB §3–§4 | addendum §B3 |
| H-97 | body lands on `end` (assumption) | RESOLVED-BY | RUL-PC §3 (A-8 answers what the CR-85 §4 step 2 question was waiting on) | `combat.py:143-152` |
| H-98 | the fourth band | RESOLVED-BY | P2 Part C, R-PC-01 (register edit) | audit E3 (90 untouched, 110 wounded) |
| H-119 | two degree surfaces | RESOLVED-BY | P2 Part A (the deleted keys); 18-D | audit E3 |
| H-123 | wound magnitude; stale `site:` | RESOLVED-BY | P2 Part C, R-PC-15 | — |
| H-184, H-258 | the Wounded edge; the lasting mark, closed as assumptions | SUPERSEDED | H-258 by `audits/25_GROUNDING_ENGINE.md` G-22 (the mark is a certainty at the gate) and RES-PC §7 (the mark as a draw); H-184 stands closed | `es/loop/effects_combat.py:394-424` |
| H-251 | odds sample size; clients not opened | SUPERSEDED | by addendum C-9 (opened: a fight is never priced by believed odds); carried by RES-PC §8 | `seam/wrappers/sigma.py` (`believed_chance`) |
| H-263 | no exit but death | RESOLVED-BY | P3 Part B as reconciled; PES-A | audit E3 |
| H-265 | no unarmed fighter | RESOLVED-BY | P4 Part C | audit E2 |
| H-266 | the log's gaps | RESOLVED-BY | P2 Part A, R-PC-05; PES-C | audit E4 |
| H-348 | the victor reads `undecided` | RESOLVED-BY | P2 Part A (`standing`) | audit E3 |
| H-349 | none against light armour, not re-measured | SUPERSEDED | by `16_PESSIMIST_PC.md` §2.3 (re-measured: light is worth 1.5 points; plate is a certainty), carried by PES-D | pessimist `pC_armour.py` |
| H-350 | one kit for all | RESOLVED-BY | P4 Part B | audit E8 |
| H-240 | `accept` binds a challenge: closed in mechanism, unreached | RESOLVED-BY | P1 edit 4 | audit E7 |
| H-64 | the probe corpus invented `fight` | STALE / FALSE-POSITIVE | `fight` is a table row (`es/verb_table.yaml:733`); the row's own text marks the stale symbol; the register edit rides RES-PC §9 | audit §6.1 |
| H-147, H-212, H-342, H-355, H-360 | filed under PC by path; subject is `_eff_march` | SUPERSEDED | closed in Part 2 (MB) of this file | — |
| H-304, H-338, H-340 | filed under PC by path; `_eff_tend`, `_eff_forgive` | SUPERSEDED | H-304 by P3 Part C as reconciled (`tend` a graded draw); H-338 and H-340 by CHAR's closure (U5a) | — |
| CP-T03-06 | the survivor's grudge | RESOLVED-BY | PES-C part 2 (the killer's name, which the regard needs first); the regard side is CHAR's (U5a) | pessimist `pS2.py` S7 |
| CP-T03-10, CP-T03-11 | rescue parked; guards cut | SUPERSEDED | accepted as the plan records them; no edit | plan card |
| CL-SLICE | ratified design, no client | RESOLVED-BY | audit §8 step 4 on the round entry (PB step 1), ordered in RUL-PC §5 | `PlayHost(` constructed only at `es/tests/test_rem31_grid_suspension.py:80` |
| PC-21, PC-22, CR-95 | design-first positions | SUPERSEDED | plan positions stand; CR-95's adverse body modifier is answered by A-8 (`10_DICE_advantage_sources_for_the_arcs.md` Edits B–D, U5a's) | — |
| PC-06 K-1 | landed, unreached | RESOLVED-BY | P4 Part D | audit E8 |
| PC-06 K-5, PC-08 | leave | SUPERSEDED | accepted; PC-08 gains the flat-top by name (RES-PC §6) | — |
| CR-85 build | built on an unratified design | RESOLVED-BY | P2 Part C, R-PC-16 (Status line); the design question itself is answered by A-6, A-7, A-8 (RUL-PC §2–§3) | `mc/attributes.py:29-37` |
| R-PC-01 | close H-98; re-point R-09's `blocks:` | RESOLVED-BY | P2 Part C | — |
| R-PC-02 | delete `winner`, `result`, `unresolved` from the seam | RESOLVED-BY | P2 Part A | audit E11 |
| R-PC-03 | keep the flip as the workbench's rule; a comment | SUPERSEDED | by 18-D edit 3 (the flip is deleted; the comment edit is replaced) and survivor 3's closure below | 18-D "Exact edits" 3 |
| R-PC-04 | `standing` in `fight_endings` | RESOLVED-BY | P2 Part A | — |
| R-PC-05 | H-266 corrected; carry the decisive beat | RESOLVED-BY | P2 Part A | — |
| R-PC-06, R-PC-07, R-PC-08 | `challenge` on persons with a dispute; `accept` on challenge Records | RESOLVED-BY | P1 | — |
| R-PC-09 | a frozen `CombatOutcome` | RESOLVED-BY | P2 Part A | — |
| R-PC-10 | widen the record; workbench through the entry; trace sink a parameter | RESOLVED-BY | P2 Part B | — |
| R-PC-11 | the turn-level withdrawal through `disengage_clean_p` and the pursuit strike | RESOLVED-BY | P3 Part A | — |
| R-PC-12 | a starter inventory and seeding | RESOLVED-BY | P4 Parts B, D (content `[ASSUMPTION]`, Jordan's to correct; admitted only with RES-PC §3's census) | — |
| R-PC-13 | an `unarmed` record | RESOLVED-BY | P4 Part C | — |
| R-PC-14 | `tend` restores a body whole | RESOLVED-BY | P3 Part C as reconciled (D-05: a graded draw through 18-A's route) | `effects_combat.py:766-790` |
| R-PC-15, R-PC-16, R-PC-17, R-PC-18, R-PC-20 | stale locators; CR-85 Status; `net_boost`; constants into `CFG`; `state_graph.py` docstring | RESOLVED-BY | P2 Part C | — |
| R-PC-19 | the tradition layer recorded as oracle-side; no edit | RESOLVED-BY | P4 Part A (the slot interface makes the layer authoring data); plan PC-21 | — |
| R-PC-21 | the tempo flat-top folded into PC-08 by name | RESOLVED-BY | RES-PC §6 (the plan-row edit, which no file carried) | `mc/combat_systems.py:107-113` |
| R-PC-22 | expose the engagement as `fight.round` with a `DuelState` | RESOLVED-BY | PB §2, step 1 (state in the calling loop's frame, R-PC-30) | — |
| R-PC-23 | three approaches as a lean on the disposition hooks | SUPERSEDED | by R-PC-28 (own coefficients; the drift never moved); PB §3 | addendum F-PC-17 |
| R-PC-24 | per-party deciders | RESOLVED-BY | PB §5, step 4 | — |
| R-PC-25 | the field's adapter calls `combat.round` on a contact | SUPERSEDED | by R-PC-30 and A-4: the field module is handed a `duel` callable and the call is a nested contest counted against the cap; PB §4, step 5; RUL-PC §1 | addendum F-PC-19 |
| R-PC-26 | one `carry_demand` leaf; `in_hand`; `switch` | RESOLVED-BY | PL as reconciled (addendum §B7's three amendments; the unit side is `04_MB_unit_loadout_and_weapon_in_hand_B.md`) | — |

## 1.3 `audits/03_PC_audit.md` — §11 survivors, named conflicts, §13 arcs, §14, §15

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| §11 item 1 | does a beaten fighter in a plain `fight` have an exit? | SUPERSEDED | answered by the standing rule (`audits/18_DETERMINISM_SWEEP.md` D-04) and A-16; carried by P3 Part B as reconciled, PHY-A A3, PES-A | P3:102-117 |
| §11 item 2 | the one input to a combat pool and its obstacle | SUPERSEDED | answered: A-7 (two numbers), A-6 (score plus a base, floor five), A-8 (the wound); carried by CAP Part B and RUL-PC §2–§3 | `DECISIONS_ANSWERED.md` A-6, A-7, A-8 |
| §11 item 3 | is any matchup certain? | SUPERSEDED | answered by the standing rule (sweep D-11, C-13); carried by 18-D (decided fights), PES-D (armour), RES-PC §3 (the weapon census) | 18-D |
| named: the suspension and the grid map | a grid battle cannot run inside one decider | SUPERSEDED | by addendum C-4/R-PC-33 (one build: the cell field at weight 1, one provider call) and A-9 (a turn is a short sequence; unblocks the per-phase approach); the in-round consult is PB §4 with RUL-PC §1 edit 4 | `architecture/meta/04_CODE_ARCHITECTURE.md:811` |
| named: R-04's grid reading | two builds | STALE / FALSE-POSITIVE | Layer 1 names it one build (addendum C-4) | `04_CODE_ARCHITECTURE.md:811` |
| named: CR-85 §4 step 2 | a round entry needs carried damage, which is held | SUPERSEDED | A-4 took nesting (the state stays in the calling frame, no carrier in the world); between scenes the carry is A-8's level (RUL-PC §3) | — |
| named: ED-PC-0007's reopen condition | three approaches are a menu | SUPERSEDED | the condition is met by Jordan's own intent of 2026-11-12 and D-40 (leans first, the transfer behind a dial at zero); PB step 3c | `DECISIONS_ANSWERED.md` ladder table, D-40 |
| named: `videogame_mode_spec.md` zones, and its formula | no grid; a simplified formula | SUPERSEDED | by Layer 1 §27.2 and `04:811` (R-PC-41), and A-1 | — |
| named: NPC-088, ARC-31 against ED-IN-0337 | a killing with no institutional context | SUPERSEDED | by A-16 (yes, rarely; lifts the conflict for criminal contexts); carried by `22_HAPPENINGS_C_a_killing_is_a_crime_someone_commits.md` (U5d's) and RUL-PC §6 (D-41) | `DECISIONS_ANSWERED.md` A-16 |
| §13 ARC-53 (persisting injury; recovery act) | represented | STALE / FALSE-POSITIVE | not a defect: the audit's own "yes" rows; no edit | audit E3, E7 |
| §13 ARC-53 (the wound degrades faction-scale rolls) | in part | RESOLVED-BY | CAP Part B row B6 and `10_DICE_advantage_sources_for_the_arcs.md` Edits B–D (A-8: a level against every roll of the wounded) | `es/seam/wrappers/pool.py:38-50` |
| §13 SCN-03 (incapacitation varies by attribute) | in the module; unreached | RESOLVED-BY | P4 Part D | audit E5, E8 |
| §13 SCN-03 (two recoveries) | no | RESOLVED-BY | P3 Part C as reconciled | — |
| §13 SCN-03 (a second depleting resource) | inside a fight only | STALE / FALSE-POSITIVE | represented for the fight; the case's season reading is not PC's need (audit's own row) | `mc/wrapper.py:286-288` |
| §13 SCN-03, SCN-01 (channelled action; two tracks) and SCN-10 (harm by entity type) | no; design-first with WR | SUPERSEDED | WR's closure (U5d) owns the mechanism; PC's precondition (round state) is PB §2 | — |
| §13 ARC-23 (capture over death) | yes at personal scale | RESOLVED-BY | PHY-A A1–A3; P3 Part B; inside a battle PB step 5 | audit E4 |
| §13 ARC-23 (a commander's incapacitation penalises the force) | no | RESOLVED-BY | PB step 5 (the contact result) with RUL-MB (what the field does with it); see Part 2 | — |
| §13 ARC-23 (a skill gates an attempt) | wrongly stated against Layer 1 | SUPERSEDED | by A-11 (training never gates; the need is re-read as "far likelier") | `DECISIONS_ANSWERED.md` A-11 |
| §13 NPC-010, NPC-035 (killable) | yes by hand | RESOLVED-BY | P1; `22_HAPPENINGS_C_*` (the context) | audit E3 |
| §13 NPC-088 (found and killed with no institutional process) | conflicts with a ruling | SUPERSEDED | by A-16 | — |
| §13 NPC-006 (high combat stats, no numbers) | wrongly stated | RESOLVED-BY | P4 Part D (authored attributes and an `arms` key on his cast entry; values are content) | — |
| §13 NPC-040, ARC-16, NPC-081/020/031/009, EMG-C4 | not PC's mechanism | SUPERSEDED | CHAR (U5a), FA (U5d), SC (U5c) closures | — |
| §13 ARC-31 (a covert lethal attempt in a formal scene) | no | SUPERSEDED | A-16 supplies the attempt (`22_HAPPENINGS_C_*`); the interruption of a proceeding is SC's (U5c) | — |
| §13 SCN-14 (a personal action inside a battle changes the mass scale) | no | RESOLVED-BY | PB step 5; RUL-PC §1; RUL-MB | — |
| §13 ARC-07 | not PC | SUPERSEDED | Part 2 (MB) of this file; A-2 | — |
| §14 (a)–(e) the capability surface for combat | slots; rule in code; doubled Ob; no carriers | RESOLVED-BY | U1 §2–§4 and §8 (the home, the roles, the reader); P4 Part A; CAP Part B row B7 specified by RUL-PC §2 | audit §14 table |
| §14 (d) item 10 | "a capability may gate an attempt" is refused by Layer 1 | SUPERSEDED | A-11 confirms the refusal | — |
| §15 (a)–(e) NPCs and the chooser in a fight | hard-coded NPC rules in module and seam | RESOLVED-BY | PB §5; PES-A; P3 Part A | audit §15 (c) |

## 1.4 `audits/03_PC_audit_addendum_B.md`

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| C-1 | the off-hand slot is a closed scope call, not a gap | SUPERSEDED | by ED-PC-0055's last row (R-PC-35); no edit; P5 §1's "no off-hand or shield slot" is marked in P5's `Reconciled:` line | `mc/core.py:217-220` |
| C-2 | the test is exact equality, not agreement in expectation | RESOLVED-BY | PB step 4 (R-PC-32); A-1 confirms Layer 1 §27.2 and §C.4 unchanged | `architecture/meta/03_VERBS_AND_LOOPS.md:146-153` |
| C-3 | the free withdrawal is a one-agent-kind breach | RESOLVED-BY | P3 Part A as reconciled (its ground restated) | — |
| C-4 | the grid is one build | RESOLVED-BY | PB §4 (the cell field at weight 1) | `04_CODE_ARCHITECTURE.md:811` |
| C-5 | `videogame_mode_spec.md` is superseded on both points | SUPERSEDED | Layer 1; A-1; no edit (R-PC-41) | — |
| C-6 | disposition is monotone because of one hook | RESOLVED-BY | PB step 3e (`DISP_INIT_K = 0`) | addendum E-B4, E-B10 |
| C-7 | `DuelState` has a fifth field; an adapter holds nothing | RESOLVED-BY | PB §2; PF (which removes the fifth field if it lands first) | addendum E-B7 |
| C-8 | 64 constants and every weapon field are outside the export | RESOLVED-BY | PX | addendum E-B1, E-B3 |
| C-9 | a fight is never priced by believed odds in the chooser | RESOLVED-BY | RES-PC §8 (the `believed_chance` answer for the `personal_combat` band: the resolver sampled on a private stream; `10_DICE_believed_odds_have_a_prior.md` Edit C names it for this lane) | `es/seam/wrappers/sigma.py` |
| C-10 | the FFT precedent is in the held proposal's Appendix A, unsurveyed | SUPERSEDED | recorded as a null; nothing is built from it (addendum §B3 "Against the research") | — |
| F-PC-15 | the export carries the weapons' names and nothing else | RESOLVED-BY | PX | addendum E-B1 |
| F-PC-16 | the half-sword form persists across engagements | RESOLVED-BY | PF | addendum E-B7, E-B8 |
| F-PC-17 | the monotone advantage of aggression is the initiative drift | RESOLVED-BY | PB §3, step 3e; composed with PES-B (the deep tier) in RUL-PC §5 | addendum E-B10 |
| F-PC-18 | "phase" is the engagement's own phase | RESOLVED-BY | PB §3–§4 (R-PC-27) | `systems/combat/combat_engine_v1/state_graph.py::INJECTION_POINTS` |
| F-PC-19 | round state on an adapter cannot be built | RESOLVED-BY | PB §2, §4 (R-PC-30); A-4 | `architecture/holonic_ARCHITECTURE.md:1679-1686` |
| F-PC-20 | the roster MB proposes as the only one is melee only | RESOLVED-BY | PX item 6 (pike as content; ranged classes carry `mass` only until a ranged resolution exists) | addendum E-B1 |
| F-PC-21 | four skill axes are real, two are not; the weapon erases the build | RESOLVED-BY | P4 Part A as reconciled (R-PC-43: `technique` and `grab` are not exposed as slots until a sweep shows them; skills bounded where authored); RES-PC §1 (the slope bound) | addendum E-B5 |
| F-PC-22 | six stale texts in instruments and comments | RESOLVED-BY | RES-PC §5 (R-PC-39's edits, which no file carried) | addendum E-B15 |
| F-PC-23 | the workbench owns a third copy of the roll | RESOLVED-BY | P2 Part C as reconciled (R-PC-42 added beside R-PC-17) | `workbench/probabilities.py::degree_distribution` |
| §B4 row 1 | the adapter row: person-supplied callables | SUPERSEDED | by A-4 (read as one declared class of adapter input); the declaration is RUL-PC §1 edit 3 | `es/seam/wrappers/combat.py:331-332` |
| §B4 row 2 | nested resolution under §39.3 | SUPERSEDED | by A-4 (option (a): a nested contest, counted against the cap); the cap's default is RUL-PC §1 edit 1 | `holonic_ARCHITECTURE.md:1397-1402` |
| §B4 row 3 | the upset flip after the engagement | RESOLVED-BY | 18-D | — |
| §B4 row 4 | the quarantined auto-resolve formula | SUPERSEDED | Layer 1 §27.2; A-1 | — |
| §B6 | what the chooser must do to pick an approach | RESOLVED-BY | PB §5, step 4; the CHAR loader-rule sentence ("refuse a key outside `CHOICE_RANGES`") is CHAR's (`U5a_CHAR_owed_amendments.md`, by title) | `es/decision/choose.py:193-197`, `:441-454` |
| §B7 | the loadout rule's individual side: three amendments | RESOLVED-BY | PL as reconciled; PX item 6 | addendum E-B1 |
| §B7 fourth matter | which weapons may be carried where (carry context) | SUPERSEDED | held with `proposals/2026-07-26-personal-combat-player-agency-and-tradition-curriculum.md` §12 (a legality rule across PC, SE, FA); no ruling orders it | — |
| R-PC-27 … R-PC-34 | phase, own coefficients, drift, state in the frame, form, exact gate, one grid, the person's decider | RESOLVED-BY | PB §2–§5, §7 | — |
| R-PC-35 | off-hand closed | SUPERSEDED | ED-PC-0055 | — |
| R-PC-36, R-PC-37, R-PC-38 | the export's sections; forms; ranged | RESOLVED-BY | PX | — |
| R-PC-39 | six stale texts | RESOLVED-BY | RES-PC §5 | — |
| R-PC-40 | cadence and "is disposition a trade" | SUPERSEDED | answered by the 2026-11-12 intent; PB | — |
| R-PC-41 | `videogame_mode_spec.md` | SUPERSEDED | Layer 1; A-1 | — |
| R-PC-42 | the workbench re-derives the roll | RESOLVED-BY | P2 Part C as reconciled | — |
| R-PC-43 | two skill axes move nothing; skills uncapped | RESOLVED-BY | P4 Part A as reconciled; RES-PC §1 | — |
| §B10 item 4 | is intensity a declared term or only a lean? | SUPERSEDED | by the ladder (D-40: A now; B behind a dial at zero, set after D-39); PB step 3c; RUL-PC §5 | `DECISIONS_ANSWERED.md` ladder table |
| §B10 named: ED-IN-0304, J-15 | risk appetite as the temperament carrier; one act or scenes | SUPERSEDED | ED-IN-0304 stays CHAR's open ask (no new carrier, PB §8.6); J-15 is answered for the nested case by A-4 (a battle stays one act) and left as recorded for the unwatched duel | — |

## 1.5 `audits/16_PESSIMIST_PC.md`

| id | claim (one line) | disposition | carrier · section | evidence |
|---|---|---|---|---|
| F-PES-PC-01 | a fight is two blows | RESOLVED-BY | RUL-PC §4 (A-31: the damage scale lowered so a Success is one Wound Interval; obstacle left alone) | pessimist `pF_story.py` F1, `pK_scale2.py` |
| F-PES-PC-02 | the per-phase approach has nothing to decide | RESOLVED-BY | PES-B, then RUL-PC §4, then PB step 3 with the added gate (R-6), in the order RUL-PC §5 fixes | pessimist `pP_window.py`, `pI_approach2.py` |
| F-PES-PC-03 | whether a wounded man gives up is a threshold | RESOLVED-BY | PES-A | pessimist `pB_yield.py` |
| F-PES-PC-04 | the commit window is [2, 4.03]; the deep tier sits at 4.0 | RESOLVED-BY | PES-B | pessimist `pF_story.py` F3 |
| F-PES-PC-05 | the world keeps a verdict, not a fight | RESOLVED-BY | PES-C part 1 | pessimist `pS_season.py` S1 |
| F-PES-PC-06 | a killing in self-defence has no killer | RESOLVED-BY | PES-C part 2 | pessimist `pS2.py` S7 |
| F-PES-PC-07 | armour is an average; its top step is a certainty | RESOLVED-BY | PES-D | pessimist `pC_armour.py`, `pQ2_gap.py` |
| F-PES-PC-08 | one attribute outweighs the levers the intent names | RESOLVED-BY | RES-PC §1 (R-7: isolate the term, lift the read's literal scale into `CFG`, the slope bound as the calibration rule) | pessimist `pN_att.py` |
| F-PES-PC-09 | eight false or narrowed N-lines | RESOLVED-BY | no edit of its own; it is the evidence for the order (RUL-PC §5) and for what the port does not carry yet (RES-PC §2) | pessimist `pE_cuts2.py`, `pE3_default.py` |
| F-PES-PC-10 | names that promise events the engine does not have | RESOLVED-BY | RES-PC §2 (the grapple's names); P2 Part A (`standing`); "first blood" is restated by PES-A's burst-breaker edit | pessimist §1.3 |
| F-PES-PC-11 | the opener has no edge, and neither does the watch | RESOLVED-BY | RUL-PC §6 (D-41 B: a first-exchange level on an opener the target did not expect); the watch: PHY-A A1–A2 | pessimist `pL_misc.py`, `pS_season.py` S2 |
| F-PES-PC-12 | a spear against a sword is 99.2 to 99.8% | RESOLVED-BY | RES-PC §3 (R-9: the census gates each weapon's admission to `arms_kinds`) | pessimist `pE_cuts_base800.txt` |
| F-PES-PC-13 | extremes: same-id fight, fractional and negative faculty, a form as a kit | RESOLVED-BY | RES-PC §4 (the `PARTY-GAP` refusal); RUL-PC §2 edit 3 (the raw pool and its floor); PX item 4 (forms) | `es/seam/wrappers/combat.py:257` |
| §1.4 N-lines 1–8 | each quoted necessity, cut | SUPERSEDED | by F-PES-PC-09's closure | — |
| §1.6 S (i) | one ladder centred at two places | RESOLVED-BY | CAP Part B (one pool rule, one opposed divisor across combat and everything else, A-5/A-6/A-26); RUL-PC §2 | pessimist `pJ_roll.py` |
| §1.6 S (ii)–(v) | armour an average; the yield a threshold; "deep" an absolute; two verbs for taking a man | RESOLVED-BY | PES-D; PES-A; PES-B; PHY-A A1–A2 | — |
| §2.5 premises nobody asked for | the opener; disarm/throw/pin; the watch; `undecided`; first blood | SUPERSEDED | by F-PES-PC-10 and F-PES-PC-11's closures | — |
| §3.7 stories that cannot happen | twelve rows | SUPERSEDED | each row is closed by the finding it cites (ambush: RUL-PC §6; yield: PES-A; refused surrender: PES-A "Acceptance"; NPC breaks: P3 Part A with PB §5; the famous swordsman, vengeance: PES-C and CHAR; missile, shield, bare hand: PX item 6, ED-PC-0055, P4 Part C); "two men kill each other", "a third man joins" and "a named wound" are recorded limits with no ruling ordering them (ED-PC-0055; CP-T03-11 cut) | — |
| §5 standing-rule table | ten fixed functions of state | SUPERSEDED | each row by its named carrier above; the lasting mark by RES-PC §7; one point of `arms` per fight by 18-A (sweep C-15, U5a's) | — |
| R-1, R-2 | the yield is a draw; NPC concession no longer Jordan's | RESOLVED-BY | PES-A | — |
| R-3 | the tier follows the window | RESOLVED-BY | PES-B | — |
| R-4 | the bare zone drawn per blow | RESOLVED-BY | PES-D | — |
| R-5 | the scene's shape and `fell_to_hand` | RESOLVED-BY | PES-C | — |
| R-6 | the approach is built after PES-B and J-1 | RESOLVED-BY | PB §7 as reconciled (the order and the added gate); RUL-PC §5 | — |
| R-7 | a slope bound; the read's scale into `CFG` | RESOLVED-BY | RES-PC §1 | `mc/combat_systems.py:1145` |
| R-8 | the grapple's names | RESOLVED-BY | RES-PC §2 | `mc/contact.py:60-77` |
| R-9 | a census before `arms_kinds` is populated | RESOLVED-BY | RES-PC §3; P4 Part B as reconciled | — |
| R-10 | `resolve` takes the same-id refusal | RESOLVED-BY | RES-PC §4 | `es/seam/wrappers/combat.py:257` |
| R-11 | the twelve-turn cap kept | SUPERSEDED | by the 2026-06-02 ruling (an undecided fight is legitimate); PES-D makes it rarer | — |
| J-1 | how long is a fight? | SUPERSEDED | answered: A-31 (B, longer); RUL-PC §4 | `DECISIONS_ANSWERED.md` A-31 |
| J-2 | does opening a fight give an edge? | SUPERSEDED | answered by the ladder: D-41 B, following A-16; RUL-PC §6 | `DECISIONS_ANSWERED.md` ladder table |

## 1.6 Handed across to PC by other closures

| from | item | disposition | carrier · section |
|---|---|---|---|
| U5a C5 | a second unseeded-generator fallback at `mc/wrapper.py:565` | RESOLVED-BY | RES-PC §4 edit 2 (`rng` required; re-read at HEAD: `rng=rng or random.Random()`) |
| U5a CAP row B7 | combat's pool and attribute terms as the same two inputs | RESOLVED-BY | RUL-PC §2 |
| U5a F-DICE-14 Edit C | the fight's believed estimate | RESOLVED-BY | RES-PC §8 |
| U5a DICE addendum §5.2 | the duel round from the dice side (an approach is an `edge` row, never a pool rule) | RESOLVED-BY | PB §3 (a lean is a prior on a gate; no pool term) |
| U5a DICE addendum §5.3 | the carry cost is the `threshold` role, one leaf | RESOLVED-BY | PL |
| U5a H-264 | (PC's) | RESOLVED-BY | RES-PC §9 (register rows this family owns, by id) |
| U5a tests §4 | PC's ten all-conditional loops | RESOLVED-BY | RES-PC §10 |
| U5a sweep C-12 | a felling is a death | RESOLVED-BY | PHY-A A3 (adopted by P3 Part B) |
| U5c `challenge` | forms but is refused | RESOLVED-BY | P1 |

