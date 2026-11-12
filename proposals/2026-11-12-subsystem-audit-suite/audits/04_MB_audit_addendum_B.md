# MB — adversarial steelman audit, addendum B

## Status: REFERENCE (an audit addendum; resolves nothing at runtime)

## Read at: 6eff039 (working tree)

Addendum to `audits/04_MB_audit.md` (§0 to §18, read at `601e715`), written by a second lane with a fresh
reading budget. It does not repeat that audit. It takes what that audit reported as NOT READ (its §12 and
§18.4), reads it, corrects the first audit where the reading or a run shows it wrong, continues its
numbering (`F-MB-20` onward; resolutions `R-30` onward), and adds the sections the work order names:
the cell-based hierarchy, the manager-style battle, and the interfaces with the duel round, the campaign
layer and the shared roller. Proposals written by this lane are listed in §B6. The first audit and its five
proposals are not edited.

Section numbers here are prefixed `B` so that a citation of "§B3" cannot be mistaken for the first
audit's §3.

## B0. Verdict of the addendum

**The first audit's verdict stands, and it is too kind to the cell layer and too hopeful about the levers.**
Three things it could not see without the reading and the runs done here. First, the cell-based battlefield
exists in the engine and **is not what a season fights on**: every season constructor packs troops at the
cell cap, so at realm scale a body is one to four cells in a single rank and a whole army is six to eight
cells, while every instrument the engine was calibrated with builds bodies of 9 to 35 cells in three to five
ranks from a second generator (F-MB-20). Second, the manager's levers that do reach a season field are not
neutral noise, as the first audit read them, but include a **trap**: of the three army strategies, `advance`
and `defend` both lose heavily to the default `line` in an even field (20 wins to 77, and 30 to 56, against a
control of 59 to 49 at n 200; F-MB-21), so a decider built on that roster, as the first lane's step 4a
proposes, would punish the player for deciding. Third, the troop table is fourteen names over at most nine
behaviours: pike is heavy infantry to six decimal places in 440 of 440 fields, because the weapon it differs
by is read nowhere that a one-rank body can reach (F-MB-22). On the structure Jordan asked for, the reading
is better than the first audit's: the four words (army, unit, subformation, troops) are **three containers
and an arrangement**, the engine has all three containers with their own orders and state, and what is
missing is narrow and nameable: the unit's subformation is not a datum the season can author, a unit cannot
hold more than one troop kind, and the army's formation is one hard-coded rule. The data model that closes
those three, with the loadout, is in §B3 and its proposal. Layer 1's "no second resolver, no auto-resolve
formula, no fast path" and Jordan's "fight or auto-resolve" are reconcilable without touching the rule, and
are reconciled in §B5.4; one true Layer 1 non-conformance is found on the way (the field returns a winner
where the ratified contract asks for a margin or a read state, F-MB-24), and it is the third of the three
items listed for Jordan (§B11).

## B1. What this lane read

Marked **F** (read in full, to the end), **S** (read in sections, the sections named), **G** (read by search
only; every hit opened in context). Anything not listed was not read. This list was written as the reading
went, so the order is the order of reading.

### B1.1 The mass-battle design set (`.designs/systems/mass_battle/reference/`)

| document | how | what it holds that the first audit did not have |
|---|---|---|
| `military_layer_v30.md` | F | the campaign-side unit: a token with Type, Size, Discipline and **Experience** (Fresh, Seasoned, Veteran; +1 Power a step, capped by the faction's Military); muster output and prerequisites by territory Prosperity, Wealth and a **named officer's history** (cavalry, ranged); merging of same-type units; unpaid professionals lose Discipline; a siege action with a five-season cap and garrison supply; Accord gating muster. Half the file (§3) is the Church Influence formula and is not mass battle |
| `military_layer_v30_index.md` | F | generated index, no content |
| `mass_battle_flow_skeleton_v1.md` | F | a traced call graph of the engine as of `dcf38ef`, re-traced 2026-09-26. **Stale at HEAD**: its adapter (`resolve_mass_battle`, `_faction_to_unit`), its caller (`systems/factions/sim/faction_action.py`) and its driver (`engine/mc_v18.py`) no longer exist (`ls` fails on both paths). Its engine half is still an accurate outline of `run_battle`'s tick |
| `mass_battle_v30_index.md`, `_infill.md` | F | a generated heading index, and an infill that is a list of headings with nine stray sentences. The infill adds nothing the skeleton lacks; the one rule only it carries is PP-570's weight-of-numbers morale check, marked provisional |
| `mass_battle_v30.md` §A.1 to §A.14, Part B, Part D, Part E | F (re-read: this addendum's §B3 and §B4 are judged against it) | the first audit read it; re-read here for the hierarchy (§A.3, §A.3b, §A.4's sub-unit text, §A.5's span of control and ED-1090), the turn structure (§A.7), officers (§D.2) and the aftermath (§D.1) |

### B1.2 Live proposals

| document | how | bearing |
|---|---|---|
| `proposals/2026-09-25-squad-engagement-synthesis.md` (RULED 2026-09-25) | F | the tree's manager document: Part A's build slate (routes, perception-limited triggers, officers, signals, role instincts, ammunition, terrain), Part B's refusals, Part C's six rulings (per-cell movement and facing; one span-of-control ladder; fog with a recognition roll; faction state sets the morale baseline), Part D's unbuilt coupling design |
| `proposals/2026-09-25-squad-engagement-concept-v5.md` | F | the concept the synthesis reconciled. Carries **Jordan's directives a to d verbatim**, of which (a) is the source of this audit's hierarchy question: *"FM and Total War inform the overall formation. FM informs subunit roles the way it informs a player's role. A subunit's shape is formation arrangement at a smaller scale."* Its §1 is "one formation grammar at two scales" |
| `proposals/multiunit_envelopment_plan.md` (PROPOSED, un-adopted) | F | several `Unit`s on one field (Path B, confirmed by Jordan 2026-06-22, never started). Written before ED-1090 lifted a `Unit` to eleven `Subunit`s |
| `proposals/mass_battle_fighting_withdrawal_v1.md` | F | the yield state. Its Status line says "GATED OFF"; the three flags default to `'1'` at HEAD (`config.py:262-272`) |
| `proposals/pc_formation_system.md` (PARTIALLY SUPERSEDED) | F | the three-level surface (army doctrine, unit shape, subunit role and instructions), "formations grant no flat bonuses", an intervention cadence of "~5–20 intervention windows per battle … not per-tick control", the kiting build and its measured dependence on field size and battle length |
| `proposals/weapon_physics_and_concentration_model.md` | F | the located-mass weapon model the personal engine built; no ranged weapon and no carried load in it |
| `proposals/2026-09-30-character-and-play-surface/08_mass_battle_units.md` (PROPOSED) | F | "a unit should be composed, not authored": who (cohort), what they carry (loadout), who leads (officer as a person), how they fight (role), what kind (derived). U-1 to U-6 |
| `proposals/2026-10-29-army-phase5-design.md`, `2026-11-08-cr12-melee-attrition-design.md`, `2026-10-16-troop-stock-design*.md` | not re-read | the first lane read the first two in full; the troop-stock pair stays Status-line only (PROPOSED, held on M3) |

### B1.3 Research and the five referents

| source | how | what it supports |
|---|---|---|
| `research/game_precedent_suite/tutorials/T19_tactics_narrative.md` (Unicorn Overlord, `:79-155`) | F for that section | squads of up to five on a formation grid (the grid's 2 x 3 shape is memory-grade there), a leader whose effect applies to the squad, per-character Tactics (a priority list, up to two conditions each), an outcome prediction in the stage preview, automatic exchange on contact, Optimize as the delegate, unit count and size bought with Honors |
| `tutorials/T16_managers_narrative.md` (Football Manager 26, `:5-84`) | F for that section | two formations (in and out of possession), roles, duties and team instructions; shouts, substitutions and shape changes during play; match review after; delegation of jobs to staff; tactical familiarity; "Instant Result" **not established** as the same simulation |
| `tables/R2_warband_sandbox.md` (Bannerlord rows, `:6-90`), `tutorials/T02_warband.md` (`:6-45`) | F for the Bannerlord sections | recruit at settlements from notables, upgrade with experience, coin and a horse; daily food and wages, with morale loss then desertion; party speed falling with size and carried weight; a result screen of kills, upgrades, dead, wounded and routed; formation orders by number key with a delegate-to-sergeant key; the fight, send-troops or auto-resolve menu is memory-grade there |
| `tables/R6_mass_battle_campaign.md` | F (lines over 520 characters cut) | Total War, Field of Glory II Medieval, Ultimate General, Hearts of Iron IV: muster, upkeep, deployment, auto-resolve by comparing statistics, siege, attrition, army break at 60% routed, battle-to-campaign persistence in all four |
| `dispositions/D_T04.md` | G (rows 27, 30, 40 to 49, 57, 58, 65, 66 opened) | the dispositions of the above against the code; row 27 names **Dominions** as "the closest verified precedent to Valoria's shape (one automatic resolver)", whose missing half here is the pre-battle intent step |
| `research/by_lane/MB_mass_battle.md` | not re-read | relied on as the first lane reported it |
| `research/pre_firearms_formations/` (17 files, about 590 KB) | G only, for carried secondary weapons | `05_late_med_renaissance_europe.md:194`, `:218` and `12_moment_by_moment_dynamic_spacing.md:545` (archers out of arrows draw mallets, swords and daggers and take the flank of a packed column); `01_ancient.md:78` (the hoplite's short sword "as backup"); `05…:537` (sword-and-buckler men working through pike lines) |
| **Ogre Battle** | searched (`grep -ril` over `research proposals .designs .audit`) | **not sourced as a battle referent anywhere in the tree.** Every hit is its character-creation questionnaire (`.designs/systems/characters/reference/character_generation_questionnaire_v30.md:20`; `research/by_lane/NPC_npc_cast.md:130`, `PC_personal_combat.md:90`). §B4 uses it only at memory grade, marked |

### B1.4 The earlier audits (`.audit/`)

| audit | how |
|---|---|
| `2026-07-26-mass-battle-fable-audit/01_findings_register.md` | F; every finding relied on is re-verified in §B2.3 |
| `2026-07-22-mass-battle-stress-test/hierarchical_units_investigation.md`, `ratified_but_unbuilt_backlog.md`, `orphaned_mechanics_audit_v1.md` | F |
| `2026-07-22-mass-battle-stress-test/README.md` | S (`:1-48`) |
| `2026-07-08-mass-battle-gauge-architecture-audit/01_wave1_synthesis.md` | S (§0 and root cause 1) |
| `2026-07-04-mass-battle-cannae-gauge-audit/README.md` | G (the root causes and decision gates by heading, the DG-3 and DG-4 rulings) |
| `2026-07-02-mass-battle-movement-pathing-audit/README.md` | S (`:1-30`) |

### B1.5 Code, tests, harnesses

Read in full, with comments: `modules/mass_battle/armies.py`, `orderofbattle.py`, `troop_types/registry.py`,
`presets.py`, `recruitment.py`, `equipment/__init__.py`, `weapons.py`, `armour.py`,
`core/exchange.py:80-222`, `armyrecord.py:1-140`, `massbattle.py:400-470`, the `Subunit`, `Officer` and
`Unit` field lists and `ROLE_INSTRUCTION_PRIMITIVES` in `hierarchy/units.py`, `config.py:585-626`,
`engine/season/seam/ladder.py:186-272`. Everything else in the module rests on the first lane's reading.

Tests: the 43 files (9,872 lines) were **surveyed mechanically** (lines, test count, skips, `approx`,
reloads, counted-assertion guards; table in the scratchpad's `tests.txt` run) and three were opened where a
finding turns on them: `tests/valoria/test_reach_weapon_class.py:58-213`, the test names of
`test_mass_battle_officers.py` and `test_army_battle.py`, the skips of `test_charge_momentum_impulse.py`.
Harnesses under `systems/mass_battle/sim/`: outlines only (function lists of `stress.py`, `validators.py`,
`bat.py`, `lanchester_signature.py`).

### B1.6 Layer 1, the sibling audits and proposals

`architecture/holonic_ARCHITECTURE.md:976-996` (§27.2); `architecture/meta/03_VERBS_AND_LOOPS.md:140-156`
(§C.4) and `:244-292` (§E.2.1, §E.3); `architecture/meta/04_CODE_ARCHITECTURE.md:770-826` (§C.5, §C.5.1);
`10_FACTIONS_AND_DEPLOYMENT.md:89`, `:97`; `registers/editorial_ledger_in.jsonl:88` (ED-IN-0306);
`digests/DG_canon_arch1.md` (the rows that cite these). `proposals/03_PC_loadout_and_carry.md` (F),
`03_PC_duel_round_and_approach.md` §2 and §5 to §6 (F for those), `audits/03_PC_audit_addendum_B.md` (head),
`proposals/10_DICE_one_roller_one_fraction_rule.md:1-60`, `audits/10_DICE_audit.md` (G), `audits/06_FA_audit.md`
and `07_SE_audit.md` (G), `06_FA_audit_addendum_B.md` and `07_SE_audit_addendum_B.md` (heads; both were still
being written, and neither yet held its mass-battle section).

### B1.7 Not read (the reading budget ran out before the list did)

- `[NOT READ: research/pre_firearms_formations/ beyond the search above; research/historical/ (three files); research/emergent_narrative_literature/ (nine files)]`
- `[NOT READ: .audit — findings_full.json (135 KB); the gauge audit's README and wave 2; the Fable audit's remediation and execution plans; 44 of the stress test's 48 files; the Cannae and movement READMEs beyond what §B1.4 names]`
- `[NOT READ: 40 of 43 test files beyond the mechanical survey; the harness bodies]`
- `[NOT READ: the cross-cutting .designs set, except by search of eight documents for mass battle, auto-resolve, zoom and officers: scale_transitions_v30.md §3.7, §3.8, §4.1, §4.3.2; complete_systems_reference.md Part 6]`
- `[NOT READ: research tables R4, REPO_MENTIONS; the companion parts; research/by_lane/MB_mass_battle.md]`

Nothing below rests on an unread document; where a claim would, it is marked.

## B2. Corrections to the first audit, and new findings

Runs are in §B7. Every figure is a reading at `6eff039`, Python 3.13, `PYTHONHASHSEED=0`, seeds `0..n-1`
through `random.Random(seed)` under `rngsource.using`, on bodies built by `orderofbattle.build_unit` (the
season's army constructor) and fought by `battle_loop.run_battle(..., max_turns=18)` (the season's loop).

### B2.1 Corrections

| # | the first audit says | reading here | effect |
|---|---|---|---|
| C-1 | F-MB-17, §5.7: the hierarchy is "three levels, not four"; no fourth container; "the officer [is] the thing that makes a subformation a unit" | The four words are three containers and an arrangement. Jordan's own earlier statements fix the reading: directive (a), *"A subunit's shape is formation arrangement at a smaller scale"* (`proposals/2026-09-25-squad-engagement-concept-v5.md:7`), and the 2026-07-22 investigation he directed, *"troops form subunits in a subformation with instructions; subunits form an army in a formation with overall instructions"* (`.audit/2026-07-22-mass-battle-stress-test/hierarchical_units_investigation.md:3-5`). So: **army = `Unit`; unit = `Subunit`; subformation = the `Subunit`'s shape, frontage, depth and density gradient; troops = cells.** No level is missing between army and unit. What is missing is inside the unit (§B3) | the first audit's "decided reading" is replaced; its evidence stands |
| C-2 | proposal `04_MB_playable_field_scenario.md`, "The problem": an even 18-tick engagement "is usually indecisive", from one seed | Measured: a single-body mirror of 600 is decided by rout in 287 of 300 fields (heavy infantry; mean 8.2 ticks) and 271 of 300 (spearmen; 9.9 ticks). A three-body combined-arms mirror (spearmen 300, archers 150, cavalry 150 a side) is drawn in 92 of 200. Decisiveness falls with the number of bodies, because an army routs by its share of broken bodies | `Drawn` (R-03) is the common ending for an army and the rare one for a single line; the proposal's conclusion survives for armies, its evidence does not |
| C-3 | proposal `04_MB_unit_loadout_and_weapon_in_hand.md` §1: "the surviving roster is personal combat's … `ARSENAL` and `ARMOURY` are deleted" | `modules/combat/weapons.py` holds 54 melee records and **no bow, crossbow, sling, javelin, pike, lance, shield or engine** (key list in §B7). Six of `ARSENAL`'s ten classes have nothing to merge into, and an archer's primary weapon has no record at all | the merge cannot be executed as written; superseded by the `_B` proposal (§B3.5) |
| C-4 | §8 step 4a and proposal 3 §B: a phase decider choosing `advance`, `line` or `defend` | two of those three values lose to the third (F-MB-21) | the decider is kept; its choice set is not (§B4.4) |
| C-5 | §4.1: the two degree ladders, "[UNVERIFIED: whether a test pins them equal]" | the DICE lane opened it: `tests/valoria/test_degree_ladder_single_owner.py:302-309` sweeps only exactly representable values, and the copies differ at 6 of 10,000 tenth-step cells (`audits/10_DICE_audit.md` F-DICE-07; `proposals/10_DICE_one_roller_one_fraction_rule.md`) | cite, do not redo (§B5.3) |
| C-6 | §5.2: "a field is graded on the one ladder … acceptable: `field_degree` is one owner" | Layer 1 does not accept it: "a subsystem returning a winner has not met the contract" (`architecture/meta/04_CODE_ARCHITECTURE.md:786`; `03_VERBS_AND_LOOPS.md:286-289`). Combat's read-off-the-scene form is a ruled exemption (`seam/ladder.py:193`, Jordan 2026-09-03); the field has none | F-MB-24; §B11 |
| C-7 | §1.1: "a cell-based tactical battle simulator on a 51 x 51 field … each cell carrying troops, morale, facing" | true of the engine; on the three season constructors every cell is filled to the cap, so the field is fought by a handful of cells (F-MB-20) | the steelman's item 6 ("rich where history says richness matters") fails further than the first audit found: not only below 100 troops, but at every army size the realm can raise |
| C-8 | §18.1: Ogre Battle "not sourced as a battle referent" | confirmed by a tree-wide search (§B1.3). More of Bannerlord is sourced than the first audit used: speed against party size **and carried weight**, the result screen, desertion of the unpaid and unfed (`tutorials/T02_warband.md:16-20`, tagged V3 there) | §B4.1, §B5.2 |
| C-9 | §18.2: `rally_check` "kept as the commander's hook" | agreed, and the archived design gives the hook more than a rally: one general's action a turn out of rally, reinforce Discipline, stabilise, fight in person (`mass_battle_v30.md` §A.7 phase 6 step 4), and `pc_formation_system.md` §7 sets the cadence at 5 to 20 windows a battle | §B4.4 |

### B2.2 New findings

#### F-MB-20 · blocks the stated intent · at the scale a season fights, the cell grid is not the battlefield

- **Claim.** All three season constructors lay troops out by `footprint_for` at the densest density the
  engine allows, so a body's cell count is `ceil(troops / cap)`: one cell for up to 200 foot or 100 horse.
  A realm army (600 to 900 troops, the first audit's presets) is six to eight cells, every body one rank
  deep. Shape, depth, rank support, a flank distinct from a front, a local break that spreads: none has
  anything to act on in a body of one or two cells. The unit's subformation is supported by the engine
  (`Subunit.shape`, `width`, `depth`, `distribution`) and is not a field of the season's record.
- **Evidence.** `massbattle.py:279` and `:329` (`concentration=float(CELL_CAP)`, both headcount constructors); `orderofbattle.py:151-152`
  (`concentration=float(cell_cap_for(sf.troop_type))`); `geometry.py:117-121` (the clamp);
  `hierarchy/units.py:449-462` (`troops`, `concentration`, `width`, `depth`, `distribution`);
  `armies.py:300-306` (the builder forwards all five); `orderofbattle.py:78-94` (`Subformation`: name,
  type, troops, role, stance, target, fall-back; nothing about arrangement).
  Run (`cells_probe`): the preset doctrine on a faction of weight 20 with every training site: heavy
  infantry 270 → 2 cells in 1 rank; crossbow 150 → 1 cell; cavalry 120 → 2 cells; levy 60 → 1 cell; the army
  6 cells. Weight 30: 3, 2, 2, 1; the army 8 cells. At 5,000 troops: 12, 7, 10 and 3 cells, 2 or 3 ranks.
- **The instruments are calibrated on a different body.** The gauge, the law instrument and the reach
  tests build with `build_unit('Line', tier, …)`, the tier table. Run (`generators_probe`):

  | troops | tier table (the oracle's bodies) | `footprint_for` at the cap (the season's bodies) |
  |---|---|---|
  | 100 | 9 cells, 3 ranks x 3 files, 11 a cell | 1 cell |
  | 200 | 15 cells, 3 x 5, 13 a cell | 1 cell |
  | 400 | 25 cells, 5 x 5, 16 a cell | 2 cells, 1 rank |
  | 800 | 35 cells, 5 x 7, 23 a cell | 4 cells, 2 ranks |

  The tier table's cells hold 11 to 23 troops, under the engine's own floor of 40; the season's hold 200.
  Every magnitude tagged CALIBRATED-DEBT was fitted on the left column and is exercised on the right.
- **It matters to outcomes.** Run (`density_probe`, 600 heavy infantry a side, n 40, side A packed at the
  cap): against a single rank of twelve cells at 50 a cell, the packed side wins 22, the thin side 0, 18
  drawn, losses 3.6% against 26%. Against 6 x 2 or 3 x 4 at the same density the result is inside the
  control's spread (17 to 16, 18 to 14; control 15 to 24, and the 300-seed mirror is 133 to 154 with 13
  drawn, so no side bias is established). Arrangement is a real lever with a dominated corner, which is
  what a designer's choice should look like, and nobody can pull it.
- **Falsifier.** A season-built body of 900 troops or fewer with more than one rank. None in the probe
  but `Arrowhead` (cavalry `Shock`, 300 troops: 3 cells in 2 rows).
- **Old finding, re-verified.** The 2026-07-08 gauge synthesis's root cause 1 (two unreconciled cell-count
  generators; a 133 to 200 troop body "collapses to 1 cell"; `Unit.ncells` set once) is still true at HEAD
  (`units.py:2872`) and the season sits on the collapsing generator at its densest setting. The 2026-07-22
  investigation's gap 1 ("subformation legibility is troop-count-dependent … a design question for Jordan")
  was never answered; §B3.4 answers it by the ladder.
- **Touches.** R-04, R-06; the cell-based intent; the port (a renderer has two to eight things to draw).
- **Minimal fix.** The unit's arrangement becomes data on the troop row and the subformation (§B3.3):
  ranks and a density, from which frontage follows; the season constructors stop passing the cap.

#### F-MB-21 · blocks the stated intent · two of the three army strategies lose to the third

- **Claim.** `orderofbattle.STRATEGIES` offers `line`, `advance` and `defend`. In an even combined-arms
  field the two non-default values make their own side lose: pressing costs about twice the casualties,
  and holding gives up the win without saving men.
- **Evidence.** `orderofbattle.py:53-57`. Run (`lever_probe`, spearmen 300, archers 150 `VolleyLine`,
  cavalry 150 `Flanker` a side; n 200; only side A's setting changes):

  | side A | A wins | B wins | drawn | A's loss | B's loss |
  |---|---|---|---|---|---|
  | control (`line`) | 59 | 49 | 92 | 14.1% | 14.6% |
  | `advance` | 20 | 77 | 103 | 21.2% | 10.2% |
  | `defend` | 30 | 56 | 114 | 17.0% | 11.8% |
  | cavalry as `Shock` | 57 | 58 | 85 | 18.0% | 16.4% |
  | spear line as `Hold` | 54 | 43 | 103 | 12.1% | 14.7% |
  | every body `target: weakest` | 41 | 42 | 117 | 17.0% | 15.4% |
  | every body `fall_back_at` 0.7 | 59 | 49 | 92 | 14.0% | 14.6% |

  A binomial standard deviation at these counts is about 5 wins. `advance` and `defend` are 6 and 4
  deviations from the control; the roles and targeting are inside it; the fall-back order at 0.7 never
  fires at a 14% mean loss.
- **Why (read, not run).** `advance` is the `aggressive` stance, a signed commitment that buys offence
  with defence (`config.py:286`); `defend` is `hold`, which freezes the body (`STANCE_SPEED_MOD['hold']`
  is -99) and was measured net-negative when it was built (`proposals/pc_formation_system.md` §11: "the
  hold-stance was net-negative (traded offense for too little protection)").
- **Falsifier.** A matchup in which `advance` or `defend` beats `line` beyond sampling error. Not searched
  beyond this one field; `hole_register.yaml` H-361 records the same direction for `Shock` on a headcount
  line. `[UNVERIFIED: an uneven field, a walled defence or a missile-heavy enemy, where holding should pay]`
- **Corrects** the first audit's F-MB-08 in one respect: the levers are not all swamped by the friction
  draw. Composition moves the field far beyond it (below); strategy moves it the wrong way.
- **Touches.** R-04, R-08; the Football Manager referent (an instruction that always hurts is not an
  instruction); the first lane's step 4a.
- **Minimal fix.** No constant is changed here. The strategy roster leaves the choice surface until each
  value wins somewhere (the PC lane set the same bar for the duel's approaches:
  `proposals/03_PC_duel_round_and_approach.md` §3, "in a mirror, no approach beats `normal` by more than
  the disjoint-seed band and each approach beats one other in some matchup"). §B4.4.

**The control for F-MB-21: composition does move an even field** (same run, same n):

| side A's change, same 600 troops | A wins | B wins | drawn |
|---|---|---|---|
| heavy infantry in place of spearmen | 72 | 44 | 84 |
| levy in place of spearmen | 8 | 44 | 148 |
| no cavalry (spearmen 450) | 27 | 76 | 97 |

So what an army *is* decides more than what it is *told*; the Total War half is understood and the
manager half is, where it acts at all, perverse.

#### F-MB-22 · degrades narrative · troop types that differ only by their weapon are one type

- **Claim.** Pike and heavy infantry, and spearmen and light infantry, carry identical stat lines by
  design, "so reach is the sole, isolated differentiator" (`troop_types/registry.py:55-61`, `:66-68`). In a
  season-built body that differentiator does nothing.
- **Evidence.** Run (`pike_probe`, `brace_probe`): the same army with a pike line and with a heavy-infantry
  line gives the same winner and the same surviving troops on both sides **to six decimal places in 200 of
  200 fields** at 600 a side, **40 of 40** at 3,000 a side (bodies two ranks deep), and **100 of 100** each
  under `ShieldWall` and `Anvil` against a cavalry `Shock` charge. Spearmen and light infantry against the
  same charge read 25, 72, 3 each. `tests/valoria/test_reach_weapon_class.py:144` asserts
  `math.isclose(pike_hp, heavy_hp, abs_tol=1e-6)` and its docstring (`:132-137`) says where the two part:
  under the shipped support-rank cap "the pike's longer supported depth makes it out-retain heavy". That is
  a third rank, on the tier table's five-rank body. The season deploys one rank, or two.
- **Consequence for the count.** By stat line and class the fourteen troop types are at most nine
  behaviours: levy; light infantry and spearmen; heavy infantry and pike; cavalry; knights templar; light
  cavalry; archers and crossbow; mounted archers; sling, skirmishers and artillery. `[UNVERIFIED: whether
  crossbow and archers, or sling and artillery, part on a path this probe did not take; the weapon
  keywords have no reader, first audit F-MB-10]`
- **Falsifier.** One field in which swapping pike for heavy infantry changes a troop count. None in 440.
- **Touches.** R-06; the weapon-carry intent (a second weapon cannot matter where the first does not).
- **Minimal fix.** Not a new constant: F-MB-20's fix (ranks as data) gives the third rank its body, and
  the loadout's weapon record becomes the source of reach and support depth (§B3.5), so a type differs by
  what it carries or not at all.

#### F-MB-23 · hygiene, with a designer's cost · troop behaviour is keyed on type names, and one type has two answers

- **Claim.** A new troop type cannot be added as a row, because four behaviours are selected by spelling:
  charge penetration is 3 for `'cavalry'` and 0 for everything else (`hierarchy/units.py:943`); the fast
  enveloping wheel is `'cavalry'` or `'light_cavalry'` (`:1491`); the charger in the brace-recoil gate must
  be `'cavalry'` (`orchestration.py:1213`, `:1217`); the stand-off default is `'mounted_archers'` in two
  files (`armies.py:267`, `orderofbattle.py:150`). And "is it mounted" has two owners that disagree on
  knights templar: `MOUNTED_TYPES` says no (`registry.py:75`: no speed, deployed in the front line by
  `orderofbattle.class_of`), `TROOP_TYPE_DENSITY_CAP` says yes (`config.py:125`), its lance reach and its
  stable say yes.
- **Old finding, re-verified.** The 2026-07-26 Fable audit's §4.4 falsifier ("add 'cataphracts' to
  `TROOP_TYPE_STATS`: charge, recoil and wheel will not follow from its stats") still fires at HEAD. One of
  its three name lists has since been given an owner (`is_mounted`).
- **Falsifier.** A troop type added by one row that charges, recoils a charge and wheels as cavalry does.
- **Touches.** §14 (the designer's surface); scripting drift in the first audit's sense is avoided only
  because the names are types, not entities.
- **Minimal fix.** The four become columns of the troop row (`mounted`, `charge`, `wheel`,
  `default_role`), §B3.3.

#### F-MB-24 · Layer 1 non-conformance · the field returns a winner

- **Claim.** The ratified seam contract is that a provider returns a margin and the one ladder reads the
  degree; "a subsystem returning a winner has not met the contract — a type assertion", "nothing may mint
  the missing bands on its behalf: an undecided outcome is a legitimate result". The mass-battle provider
  returns `attacker_wins`, and `field_degree` mints `Won` or `Lost` from it.
- **Evidence.** `architecture/meta/04_CODE_ARCHITECTURE.md:774-786` and `:1050` (row 24: "the return type is `Margin`"); `03_VERBS_AND_LOOPS.md:273-289`;
  `engine/season/seam/ladder.py:198-222`, and `:234-241`, which says of itself that the provider's result
  "is still a survivor-ratio classification, not a margin" and that reconciling it "stays open MB-lane
  work". Combat's third shape is a ruled exemption ("the degree is READ OFF THE SCENE", `:151`, `:167`, `:193`); the
  field's is not ruled.
- **The first lane's R-03 does not cure it.** `FieldOutcome.verdict` (`won`, `lost`, `drawn`) is still a
  winner computed inside the module, with a draw added.
- **Falsifier.** A ruling or a Layer 1 row exempting the field as combat is exempted. None found in
  `HANDOFF.md`'s rulings, `HANDOFF_MB.md`, or `04` §C.5.
- **Touches.** R-09; the port (the ladder is the one thing every subsystem's result passes through).
- **Minimal fix.** R-31 (§B6): the module returns the field's end state and nothing that names a winner;
  the host's `field_degree` reads the band off that state, as `combat_degree` reads a scene. Listed in §B11
  because the other reading (a margin, four graded bands) is defensible and a different game.

#### F-MB-25 · hygiene · reference surfaces that say the opposite of the code

| surface | says | code |
|---|---|---|
| `proposals/mass_battle_fighting_withdrawal_v1.md` Status | emergent entry, rally exit and pocket exit "all GATED OFF" | `MB_YIELD_EMERGENT`, `MB_YIELD_RALLY`, `MB_YIELD_POCKET` default `'1'` (`config.py:262-272`) |
| `orchestration.py:287` (`reform_check` docstring) | "Flag-gated default OFF" | `REFORM_CHECK_ENABLED` defaults `'1'` (`:278`) |
| `.designs/…/mass_battle_flow_skeleton_v1.md` | every claim "carries a `path:line symbol` anchor" | its adapter, caller and driver files do not exist |
| `architecture/meta/03_VERBS_AND_LOOPS.md:261`, `10_FACTIONS_AND_DEPLOYMENT.md:89` | "units … persons, at weight. One type; there is no unit class" | amended for armies by ED-IN-0306, recorded at `04_CODE_ARCHITECTURE.md:813` only (§B5.4) |
| `troop_types/registry.py:116-122` | ranged types have "a 0.1 melee sidearm" | no second weapon exists (first audit F-MB-19) |

Dispositions in §B6 (R-37, R-38). None is a mechanism; each misleads the next reader.

#### F-MB-26 · blocks the stated intent · the manager's vocabulary is built in the engine and has no carrier in the season

- **Claim.** The synthesis's Part A is built (`HANDOFF_MB.md`): routes with waypoints, triggers limited to
  what a body can see, go-code signals, conditional orders on tick, range, ally position and own strength,
  ammunition, officers as a count. The army Record can say, for a subformation: role, stance, target
  preference, one fall-back fraction. Nothing else crosses.
- **Evidence.** Engine: `hierarchy/units.py:271-290` (`_ORDER_SAFE_FIELDS`: stance, instructions, role,
  targeting, escort, yield, route), `:309` (six trigger kinds), `:550` (`route`), `:2844`
  (`fired_signals`). Record: `armyrecord.py:13-19` (`KEYS` and the subformation's seven fields);
  `orderofbattle.py:165-168` (the one `Order` the record can produce). Officers: `armies.py:204-245`
  validates a span and nothing reads `Subunit.officer` or `Unit.officers` afterwards (`grep` over the
  module: two comment hits). Order latency is not built (`core/contact.py:144`: "no messenger latency is
  modelled").
- **Falsifier.** A season field in which a body follows a route, waits on a signal or acts on a trigger
  other than its own strength. The record has no field to carry one.
- **Touches.** R-04, R-05; Unicorn Overlord's Tactics and Football Manager's instructions, which are
  exactly a list of condition and response per member.
- **Minimal fix.** `standing_orders` on the subformation row: an ordered list of `(trigger, behaviour)`
  over the engine's own closed sets (§B4.3). No engine edit.

### B2.3 Earlier `.audit` findings, re-verified at HEAD before use

| old finding | source | at HEAD | how checked |
|---|---|---|---|
| the law instrument is red and unwired | Fable S1.1 | wired report-only and red, per the first audit; not re-run | relied on the first audit |
| a one-ulp error zeroes an exchange | Fable S1.2 | fixed by a tolerance in the copy (`resolution.py:101-120`); the tolerance is now why the copy and the owner differ (DICE F-DICE-07) | first audit; DICE audit |
| engagements past the fifth depth group dropped silently | Fable S1.3 | counted, and the count dropped at the seam | first audit R-29 |
| `check_drift` re-keys one of ten maps | Fable S1.4 | fixed except three morale maps | first audit F-MB-18, by run |
| `reform_check` is never enabled | Fable S2.5 | **now false**: on by default | `orchestration.py:278` |
| pursuit is never called in the measured mode | Fable §4.2 | still true for a season field: `pursuit_damage`'s one call site is `run_multi_unit_battle` | `orchestration.py:2266` |
| feigned retreat has "zero hits" in the sim | backlog A7 | **now false** as code, still true as play: `resolve_feigned_retreat` exists and its one call site is the multi-unit loop | `orchestration.py:2125`, `:2430` |
| the reserve instruction has no consumer | backlog A6 | consumed by `unit_in_reserve`, called only from the multi-unit loop | `orchestration.py:2119`, `:2222` |
| waypoints unbuilt | backlog A1 | built (`Subunit.route`); no season carrier | F-MB-26 |
| cavalry density cap unbuilt | backlog A8 | built and on: a cavalry cell caps at 100 | `config.py:123-132`; `cells_probe` |
| entity special-casing by type name | Fable §4.4 | still true, four sites | F-MB-23 |
| "delete the cell layer … little shipped behaviour changes" | Fable §4.4 | stronger on the season path | F-MB-20 |
| armour is unwired; `dr` is a free scalar defaulting to 1 | Fable §5.5 | still true: the damage line reads `eff_dr` (`orchestration.py:1360-1366`) and nothing maps an armour tier to it | grep; first audit's loadout run |
| two cell-count generators; footprint collapse; static `ncells` | gauge synthesis #1 | still true; now the season's path | F-MB-20 |
| cells within a subunit are homogeneous | investigation gap 2 | still true | `core/exchange.py:114-118` |
| cap of 11 against Command 1 to 7 | investigation gap 4 | officers built as a span check; inert at resolution | F-MB-26 |
| fighting withdrawal residuals gated off | proposal Status | false: on | F-MB-25 |
| the shipped default has no regression oracle | Fable S1.5 | `[UNVERIFIED]`: not opened | — |
| two contradictory ranged DR tables | backlog C (ED-MB-0008) | `[UNVERIFIED]`: not opened | — |

## B3. The cell-based hierarchy: army → unit → subformation → troops

### B3.1 What the four words mean, from the sources

| level (Jordan, 2026-11-12) | earlier statement that fixes it | the archived design | the code |
|---|---|---|---|
| **army**: "a deployment of all its units in a formation on that grid" | directive (a): Football Manager and Total War "inform the overall formation"; 2026-07-22: "subunits form an army in a formation with overall instructions" | several units on a battle map; the general's strategy declaration each turn; ED-909: an army formation is where the bodies are put and what they are told, never a shape of its own | `hierarchy/units.py::Unit`; `orderofbattle.OrderOfBattle`; deployment by `orderofbattle._place` |
| **unit**: "has its own subformation and its own troop types" | directive (a): "subunit roles the way [FM] informs a player's role"; ED-1090: up to eleven | "a unit is composed of up to three sub-units", each with its own Morale, Discipline and rout (`mass_battle_v30.md` §A.4, ED-1019); one named officer a unit (§D.2); a unit token with Type, Size, Discipline and Experience (`military_layer_v30.md` §1.1) | `Subunit`; `orderofbattle.Subformation`; the Record's `subformations` row |
| **subformation** | directive (a): "a subunit's shape is formation arrangement at a smaller scale"; 2026-07-22: "troops form subunits in a subformation with instructions" | "each cell within a formation holds a player-assigned troop count with min/max bounds. The player shapes the formation's distribution … at muster" (§A.3b); ED-907's adjustable allocation surface (`pc_formation_system.md` §2, L2) | `Subunit.shape`, `width`, `depth`, `distribution`, `concentration`; `geometry.footprint_for` |
| **troops** | directive (b): "the number and quality of troops per cell"; 2026-07-08: "subunit power is the aggregate or derivation of cell power" | the cell as the primitive for morale, facing, damage and troops | a cell: `cell_troops`, `cell_morale`, `cell_facing_vec`, position; type and quality are the unit's, not the cell's (`core/exchange.py:114-118`) |

The record names the second level "subformation" where Jordan says "unit" and uses no word for the third.
That is a naming fork between `armyrecord.py` and the intent, and it is why the first audit counted a
missing level. Resolved at R-30.

### B3.2 Is each level real in the data model and in the resolver?

| level | its own formation | its own orders | its own state | read by the resolver | verdict |
|---|---|---|---|---|---|
| army | **no datum.** One rule in code: melee in front, missile behind, horse alternating on the flanks, three rows from the enemy (`orderofbattle.py:180-226`, an ASSUMPTION "Jordan to correct"). Envelopment and refused flank are builders in `systems/mass_battle/sim/engine.py`, which a season cannot reach | `strategy` (three values, two of them traps, F-MB-21); go-code signals exist and nothing on the record fires one | friction draw; `fired_signals`; rout by share of bodies broken (`ROUT_CASCADE_FRAC` 0.6); Command, a literal | yes | **real in the resolver, flat in the data.** An army is a list |
| unit | shape from its role; frontage and depth supported by the engine and **not carried** (F-MB-20) | role, stance, target, one fall-back fraction; the engine's orders, routes and signals **not carried** (F-MB-26) | morale, discipline, stamina, ammunition, routed, broken, yielding: all per unit, all live | yes: targeting, orders, rout, pools, volley are per unit | **real in both**, narrow in what the season may say |
| subformation | it *is* the formation; four shapes | none of its own (it has none in any source) | per-cell offsets, facing, morale | yes above about ten cells; **at season scale it is one to four cells in one rank** | **real in the engine, absent in a season** |
| troops | — | — | count, morale, facing, position per cell; **kind, quality, armour and weapon are the unit's** | count and facing: yes. Morale: yes when cells exist | **real for count, not for kind** |

**Flattened at resolution time?** On the shipped path, yes, twice: the headcount constructors make one unit
of one stand-in type (the first audit's F-MB-17), and on every path the subformation is flattened to the
cap (F-MB-20). The resolver itself does not flatten: given a body with ranks it resolves per cell.

### B3.3 The data model that makes it designer-editable (decided)

One authored file, one exporter, one loader. The shape follows the tree's own precedent: the order
vocabulary is already exported by `tools/export_battle_orders.py` to
`engine/engine_params/battle_orders.json` behind a `--check`.

- **Authored head:** `references/troops.yaml`. **Export:** `engine/engine_params/troops.json`
  (`tools/export_troops.py`, `--check` round-trip). **Reader:** one loader in
  `modules/mass_battle/troop_types/`, which refuses an unknown key by name; `TROOP_TYPE_STATS`,
  `TROOP_TYPE_REACH`, `MOUNTED_TYPES`, `TROOP_TYPE_DENSITY_CAP`, `TROOP_TYPE_ROLES`, `TROOP_LOADOUT`,
  `TRAINING_SITE`, `ARM_SHARES`, `ROLE_OF`, `ARSENAL`, `ARMOURY` and the four name tests of F-MB-23 become
  reads of it. The module reads a data file and imports no `engine` code, as now.
- **Four sections**, each a closed table:

  | section | one row is | columns | replaces |
  |---|---|---|---|
  | `arms` | something a soldier carries to fight with | `class` (`non_pole`, `pole`, `pike`, `missile`: the ruled P-DEC-1 map gives reach 0.1, 0.2, 0.3 and the support depth 1, 2, 3); for a missile `range` and `volleys`; **mass**: read from personal combat's export when the key is in its roster, authored here (`mass_kg`) only when it is not, and refused if stated in both | `ARSENAL`, `TROOP_TYPE_REACH`, `support_ranks_for`, `VOLLEY_*` per type |
  | `troops` | a kind of soldier | `power`, `discipline`, `morale`, `strength`; `mounted`, `charge`, `wheel`, `default_role`; `cell_cap`, `ranks`; `primary`, `secondary`, `armour`; `roles`; `training_site`, `min_site_condition` | seven tables and four name tests |
  | `formations` | a way of deploying an army | for each post (`front`, `rear`, `left`, `right`, `reserve`): the line it stands in and its offset; `approach_rows`; which troop classes default to which post | the rule inside `orderofbattle._place`; the harness-only envelopment and refused-flank builders become rows |
  | `doctrines` | what an unplayed commander raises | the share of each class and the order of preference | `presets.ARM_SHARES`, `ROLE_OF` (the first audit's step 5a) |

- **The army Record's unit row** (`armyrecord.KEYS` is unchanged; the row gains fields, each optional
  with today's behaviour as its default):

  | field | meaning | default |
  |---|---|---|
  | `post` | where in the army's formation the unit stands | by its class, as `_place` does now |
  | `ranks`, `files` | the subformation: depth, and frontage if the designer fixes it (else it follows from troops) | the troop row's `ranks` |
  | `secondary` | overrides the troop row's second weapon for this unit | the troop row's |
  | `standing_orders` | an ordered list of `(trigger, behaviour)` over the engine's closed sets (§B4.3) | `()` |
  | `officer` | the person who leads it | none |
  | `experience` | 0, 1 or 2 (§B5.2) | 0 |
  | `arrears` | seasons its troops went unpaid (§B5.2) | 0 |

- **What a designer edits.** A new troop type: one `troops` row. A new weapon for troops: one `arms` row
  (or nothing, if personal combat has it). Pikemen or archers with arming swords: one cell, `secondary:
  arming`. A deeper pike block: `ranks`. A new way to deploy: one `formations` row. No Python.

Full text, seeds and gates: `proposals/04_MB_unit_loadout_and_weapon_in_hand_B.md` (the troop file, arms,
loadout, the weapon in hand) and `proposals/04_MB_cell_hierarchy_as_data.md` (arrangement, scale,
formations, kinds within a unit).

### B3.4 The scale question the 2026-07-22 investigation left for Jordan, answered by the ladder

*"A minimum cells-per-subunit floor, or a UI that renders sub-cell formations at low counts?"* Neither.
Step 3 (a design document): the archived design makes the troops in a block a function of the battle's
**scale** (`mass_battle_v30.md` §A.3: ten soldiers a Size at skirmish scale, a hundred at company scale),
not a constant. Step 4 (precedent): every calibration in the engine was made on the tier table's bodies,
which hold about 16 troops a cell at 400. So: **the season lays a body out at the density the engine was
calibrated at, by an explicit ranks-by-files grid (`footprint_for`'s `width`, `depth` arm, which already
exists and bypasses the cap), with one number, troops a cell at deployment, in the troop file's header;
the cap stays as the control arm.** A realm army of 600 is then some forty cells in bodies three to five
ranks deep: the bodies the gauge fights. This is a declared mover for every army field (none occurs in
natural play today) and it must land with the first audit's scale and grade proposal, not before it.

### B3.5 The weapon-carry trade-off, point by point

| Jordan's test | reading | where it goes |
|---|---|---|
| is the loadout a per-unit, per-troop-type datum | a troop type names one weapon and one armour in a Python dict; the resolver reads only whether the weapon is melee or missile (first audit F-MB-19, confirmed: armour never becomes `dr`, §B2.3) | `troops` row: `primary`, `secondary`, `armour`; unit row may override `secondary` |
| is the weapon in hand a state the resolver reads and an order or trigger changes | no: `unit_type` is fixed at construction; reached archers keep shooting (first audit, by run) | `Subunit.in_hand`, an order-settable field; two new trigger kinds, `flanked` and `volleys_spent` (the second is the archer's historical switch: `research/pre_firearms_formations/05_late_med_renaissance_europe.md:194`, `:218`) |
| are the penalties derived from the loadout by one rule, as data | no rule exists at either scale; fatigue and speed have no equipment term | one function, personal combat's `carry_demand` (`proposals/03_PC_loadout_and_carry.md`), evaluated by the host; the module is handed factors |
| consistent with an individual's kit | cannot be today: two rosters, and personal combat's has no missile weapon, pike or lance at all (C-3) | one owner a fact: mass lives with whichever roster holds the weapon; the leaf takes masses (§B5.1) |
| does the cost bite in play | **fatigue:** saturates in one engagement (first audit); **speed:** first contact differs only by Discipline and by horse; **pursuit:** season-unreachable; **forced march:** no march cost exists to slow `[UNVERIFIED beyond `_eff_march`]`; **supply:** one ration debit, shipped off | the drain and recovery factors (battle), the step factor (approach, kite, envelop), and, at campaign scale, the sourced Bannerlord shape, speed falling with carried weight, named for FA and SE in §B5.2 because no march clock exists to carry it |
| one rule over any troop type, primary and secondary | — | yes: no branch on a type name; the pike's sword and the archer's sword are the same column and the same order |

One thing the weapon-carry intent depends on that neither first-lane proposal names: **a second weapon
can matter only where the first does** (F-MB-22). A pike unit that draws swords changes reach class from
`pike` to `non_pole`; on a one-rank body that changes nothing, as pike against heavy infantry shows. The
loadout therefore lands after the arrangement (§B3.4), or its gates cannot go green.

### B3.6 More than one troop kind in a unit

"Its own troop types" is plural. Two readings: a unit of one kind with two weapons (covered above), and a
unit whose ranks are of different kinds (a pike block with shot behind it; veterans in front of levy).
The second has a ruled direction (2026-07-08, quoted in §B3.1), a named seam (`subunit_combat_pool`'s
closed form is "sum-over-cells(cell_power x cell_troops)" and `pair_pool_contribution` already walks
cells) and a falsifier written by the synthesis ("a sub-unit whose cells differ in Q pools differently
from its troop-weighted mean Q"). It is specified in `proposals/04_MB_cell_hierarchy_as_data.md` §4 as a
`bands` list on the unit row, front to rear, and **staged last**: with eleven units an army, two bodies
one behind the other already say most of it, and the NERS reading of a band is N-narrowed until a body
has ranks for it to occupy.

### B3.7 NERS reading of the hierarchy as designed (E last)

- **N.** Army formation as data: holds from above (a commander's plan is the deployment), below (the
  engine already places by post) and laterally (the same idea as the unit's shape, one grammar at two
  scales). Subformation as data: holds from every direction once bodies have cells; from the season's
  direction today it is unreachable, which is the finding, not a reason to cut it. Bands: narrowed (§B3.6).
- **R.** Customisation of settlements' and factions' forces by row; strategic thought in post, depth and
  loadout; completeness at the extremes fails today (a one-cell body) and is what §B3.4 repairs.
- **S.** One methodology for a body's cells on both paths (today two generators); one roster for a
  weapon's mass; the scale stated once.
- **E, against that.** Twelve tables and four name tests become one file of four sections; the record
  gains eight optional fields. A player can predict that a deeper block holds longer and a wider one
  wraps, which no player can predict of one cell.

## B4. The manager-style battle, as one cell resolver for the commanded and the delegated mode

### B4.1 The five referents, sourced, against what a manager does

`sourced` means read in a page body by the research suite (its V2 or V3 tags); `memory` means the suite
itself marks it [M] or the tree has nothing. Shapes are the finding; no figure is relied on.

| what the manager does | Football Manager | Unicorn Overlord | Ogre Battle | Total War | Bannerlord | in the code |
|---|---|---|---|---|---|---|
| **builds the side from individuals** | squad, roles, duties (sourced, `T16:22`) | up to five named characters a squad, a leader whose effect applies to the squad (sourced, `T19:104-105`); grid 2 x 3 (memory) | **memory, unsourced in the tree**: a unit of a few characters in front and rear rows, where a member's row decides what it does | units mustered to a general (sourced, `R6` F1) | troops recruited from notables, upgraded with experience, coin and a horse; companions in four roles (sourced, `R2` F1, A5) | the army Record over cohort headcounts: built, dark. Named persons: weight only (first audit F-MB-14) |
| **sets instructions in advance** | two shapes, team instructions (sourced) | Tactics: a priority list per character, up to two conditions each; an unconditional entry placed first starves the rest (sourced, `T19:146`) | memory: one tactic a unit (whom to strike) | secret deployment, stances (sourced, `R6` F3) | formations by number key; "your troops do nothing until told" (sourced, `T02:19`) | role, stance, target, one fall-back fraction on the record; the engine's triggers, routes and signals have no carrier (F-MB-26) |
| **sees a prediction** | — | an outcome prediction in the stage preview (sourced, `T19:90`) | — | projected result at contact (first audit) | — | `field_estimate`, the player's only (first audit §16) |
| **lets it resolve** | match engine (sourced as a loop; that Instant Result is the same engine is **not established**, `T16:79`) | automatic exchange on contact (sourced) | memory | auto-resolve "compares the statistics of all the units": a second calculation (sourced, `R6` F5) | simulated battles (sourced, `R2` F5) | one engine, one call |
| **intervenes during play** | shouts, substitutions, change of shape (sourced, `T16:24`) | swap, rest, a Valor skill, deploy another squad (sourced, `T19:94`) | memory: change the tactic, play a card, retreat | real-time orders, pause (pause is memory) | fights in person; orders by key; delegate to a sergeant (sourced, `R2` F4) | nothing (first audit F-MB-15) |
| **reads why** | ratings, match review (sourced, `T16:25`) | — | — | — | a result screen: kills by unit, upgrades, dead, wounded, routed (sourced, `T02:20`) | a band and, on one arm, one name |
| **keeps a campaign economy** | wages, contracts, training, familiarity with a tactic (sourced) | Honors buy squad count and size (sourced) | memory | upkeep each turn, replenishment on friendly ground (sourced, `R6` E6, M3) | daily food and wages, then morale loss, then desertion; speed falls with party size and carried weight (sourced, `T02:16-17`) | recruiting by site: built, dark. No wage, no upkeep, no experience, no load (§B5.2) |

**A sixth precedent the brief does not name and the corpus rates highest:** Dominions, "the closest
verified precedent to Valoria's shape (one automatic resolver)" (`D_T04` row 27): army setup, squad
placement and scripted orders before the battle, the battle never played live. It is the existence proof
that the delegated mode alone can be a game, provided the intent step is rich. Here that step is four
fields.

**Nulls.** No surveyed game shows a commanded battle and its delegated resolution agreeing exactly;
Total War's own manual documents two calculations, and Football Manager's claim is unverified (first
audit §7). Valoria's answer cannot be borrowed. It has to be built from the one-entry rule, and Layer 1
says the same thing in stronger words (§B5.4).

### B4.2 Understood or named, with the full design set

The first audit's short judgment ("Total War is understood; Football Manager is named") is confirmed and
sharpened by three documents it did not have.

- The squad-engagement concept states the manager's surface as **keeps, arranges, plans, writes,
  commands** (`concept-v5:39-45`), and the synthesis built the engine half of *plans* and *writes*
  (routes, perception-limited conditions, signals) and none of the carrier.
- `pc_formation_system.md` §2 gives the three levels a manager works at (army doctrine, unit shape,
  subunit role with instructions) and §7 the cadence: "deploy → set doctrine → assign roles → ~5–20
  intervention windows per battle (Command actions: rally / reinforce / execute stratagem / adapt
  doctrine), not per-tick control". The archived design's turn has the same slot: one general's action in
  the cascade phase (`mass_battle_v30.md` §A.7).
- The measured levers (F-MB-21): composition decides, roles do not register, strategy backfires.

So the precedent is **understood as vocabulary and as engine primitives, and not as a game**: the
manager's decisions that exist are either unreachable (orders, routes, signals, arrangement) or wrong
(strategy), and the ones that work (who is in the army) are the Total War half.

### B4.3 Standing orders: the delegated battle's decisions, made in advance

The engine already has the primitive (`hierarchy/units.py::Order`: a trigger and a behaviour dict,
validated at construction, evaluated every tick by `core/contact.check_orders`). The record gains its
carrier, and nothing else:

```
standing_orders: ((trigger, behaviour), ...)        # per unit row, in priority order, at most 4
trigger   ∈ immediate | tick:N | enemy_range:D | ally_at:D | own_strength:F | signal:NAME
            | flanked | volleys_spent                # the two added by the loadout proposal
behaviour ⊂ { stance, target_condition, yielding, conceded, route, in_hand, fire_signal }
            # a subset of hierarchy/units.py::_ORDER_SAFE_FIELDS, exported beside ORDER_ROLES
```

`armyrecord.order` validates both against the exported closed sets and refuses by name;
`orderofbattle._spec_for` turns each row into an `Order`, as it turns `fall_back_at` into one today
(`orderofbattle.py:167-168`); `fall_back_at` becomes the row `(own_strength:F, {stance: retreat})` and
leaves the record. The cap of four keeps a unit's orders readable, the concern Unicorn Overlord's own
example raises (an unconditional first entry starves the rest): `immediate` is legal only as the last row.

This is Unicorn Overlord's Tactics and Football Manager's instructions in the engine's own terms, and it
is what an unplayed commander's doctrine writes for him.

### B4.4 The commanded battle: the same call, with a general's action at each window

The first audit's step 4a is kept in structure (`resolve_field(inp, rng, *, decide=None)`, called where
`phase_boundary` is called, the combat module's REM-31 shape) and changed in content.

| | first audit, step 4a | here |
|---|---|---|
| what the decider returns | an army-wide approach, `advance`, `line` or `defend`, or a retreat | **one general's action**, or none |
| the closed set | the strategy roster (F-MB-21: two traps) | `signal(NAME)`: release every order waiting on that go-code · `order(unit, behaviour)`: one behaviour from the standing-order set, to one unit · `rally(unit)`: the commander's hook (`rally_check`), a Command check restoring morale toward its start · `withdraw`: the retreat the engine already has · `none` |
| why these | the names existed | each is an existing primitive (`Unit.fired_signals`, `_ORDER_SAFE_FIELDS`, the `rally_check` slot, `_retreat_orders`); none is a new number; `signal` is the cheap, prepared act and `order` the improvised one, which is the concept's own trade (`concept-v5:359`) |
| windows | the two phase boundaries | the same two for an 18-tick engagement; the count is the troop file's (`pc_formation_system.md` asks for 5 to 20 over a battle of several engagements, which `Drawn` supplies) |
| a side nobody plays | no decider | no decider is the default; an NPC commander **may** be given one through the same parameter, filled by the chooser over the same closed set. That is CHAR's to build; the interface does not distinguish them |

**Three conditions make the two modes one slice and not two that agree on average** (they are the gates):

1. One entry. No function under `modules/mass_battle/` is reached by one mode and not the other.
2. A decider reads a frozen view of its own side, draws nothing and holds nothing. So `decide=None` and a
   decider that always returns `none` give the same outcome **and the same draw count**.
3. A commanded battle's actions are data: `((window, action), ...)`. Handed back as
   `MassBattleInput.interventions` with no decider, the delegated call returns the **identical**
   outcome. The played battle is then the delegated battle of a commander who happened to decide those
   things, and a recorded battle can be replayed, summarised or shown at any depth.

Condition 3 is what the genre lacks and what Layer 1 §C.4 asks for by name (§B5.4).

### B4.5 The explanation afterwards

The first audit's `FieldOutcome.report` (per phase, per part: share lost, broke or held, flanked) is kept.
Three additions, each derived from what the engine already records:

- **which standing order fired, and when** (one trace event at the point `check_orders` applies a
  behaviour): "the reserve never moved: its trigger was the enemy within four, and the enemy broke at
  six" is the sentence a manager needs and a casualty table cannot say;
- **the interventions taken**, from condition 3's list;
- **the day's fortune**, the two sides' friction draws as a ratio reported in three words (with us,
  even, against us), by bands in the troop file's header. The draw is the largest single cause of most
  results at the ruled magnitude (first audit F-MB-08); a report that omits it explains a result by its
  smaller causes. Disclosing it changes no number and is the honest reading of a ruled item, not a
  re-raising of it.

Written to the band Event as Observations, as the first audit specifies.

### B4.6 The squad of named characters on a formation grid

The realm's actual fields are two to six named persons a side (first audit §15). That is the Ogre Battle
and Unicorn Overlord scale, and Layer 1 already says where it lives: "one scale down, unchanged: a squad
is the members of a faction present at a rung, resolved once, every combatant a `Person`"
(`03_VERBS_AND_LOOPS.md:269-270`). It is not a mass-battle unit of anonymous cells and must not be built
as one. The first audit's scale rule is adopted (a side with no cohort member and no army Record is a
squad), and the missing design is supplied in `proposals/04_MB_squad_grid_of_named_characters.md`:

- **the grid**: two rows (front, rear) of three files a side. The row decides who can be struck and who
  can strike (a front member screens the file behind him; a missile or pole weapon strikes from the
  rear). The 2 x 3 shape is memory-grade in the corpus and is proposed as a seed, not cited as fact;
- **the resolver**: none of its own. An exchange is a set of pairings, each one call of the duel round
  the PC lane proposes (`combat.round`); outnumbering is more rounds against one fighter's carried state;
- **standing orders**: per member, rows of `(condition, approach or target)` over the turn view, as
  `03_PC_duel_round_and_approach.md` §5.1 already specifies, evaluated host-side into the same decider a
  player or the chooser supplies;
- **the leader**: one member is the leader; what a leader adds is a capability read through the
  capability surface, not a rule here;
- **the outcome**: the same `FieldOutcome` a field returns, its parts the persons, so `_eff_march` writes
  one way for both scales.

So the commanded-or-delegated symmetry holds at both scales with one shape: standing orders in advance,
a decider at windows, a report after; cells and troop rows above the line, persons and duel rounds below.

### B4.7 NERS reading of the manager battle (E last)

- **N.** From the player's direction: without orders that reach the field and an action during it, the
  battle is a draw of lots he may only watch. From the world's: an unplayed commander's standing orders
  are what make two commanders differ (R-06, R-08) and they cost no chooser call. From the architecture's:
  the decider is the combat module's shape reused, and the interventions list is what lets fidelity be a
  rendering. From the referents': all five have the intent step; three have the window.
- **R.** Customisation by data (orders, posts, loadouts); a prepared plan against an improvised one;
  completeness: a side with no orders and no decider is today's field exactly.
- **S.** One call at any depth; it pauses at the engine's own boundaries; the same three-part shape at
  squad scale; one vocabulary of triggers for a unit and, at squad scale, conditions for a person.
- **E, against that.** One field on the record, one closed set of five actions, one list on the input,
  three kinds of line in the report. What a player can intuit: "they will fall back when a third are
  down" is a rule he wrote.

## B5. Interfaces

Each sibling lane's design is cited, not redone. What is stated here is what mass battle needs across the
edge and where the sibling's text has to change for the two to meet.

### B5.1 With the personal-combat duel round (`audits/03_PC_audit.md`, `03_PC_audit_addendum_B.md`; `proposals/03_PC_*`)

| edge | PC lane's design | what mass battle needs, or supplies | status |
|---|---|---|---|
| a duel inside a field | `03_PC_duel_round_and_approach.md` §5: the field reports a contact between two named persons; the host adapter calls `combat.round`; "one field turn is one duel round"; the field receives `DuelContactResult` | **a named person must be somewhere on the field for a contact to exist.** Today he is nowhere (first audit F-MB-14). With `officer` on the unit row he is *with a unit*; the contact is two officers whose units are in contact at a window. The window, not the tick, is the duel round's clock (two a engagement), which matches the archived cadence: "one mass combat turn = one personal combat exchange", at most five (`scale_transitions_v30.md` §3.7, PP-111) | designed on both sides; needs `officer` (§B3.3) and the window (§B4.4) |
| what a duel does to the field | "a person's effect on a unit is a fraction of the unit's own cohesion, never a flat amount" (PC §5, from `research/by_lane/PC_personal_combat.md` T-PC-15) | accepted. The carrier already exists: an officer felled or yielded is a morale erosion on his unit through `cascade_morale_hit` (`hierarchy/units.py:2966`), scaled by that unit's own discipline, the form the engine uses for a freed attacker (`orchestration.py`, quoted in the synthesis Part D). No army-wide instant rout: the engine's command-zero rout (`battle_loop.py:411-413`) is the failure shape the corpus warns of (first audit §7) | one line in the manager proposal |
| squads | PC §5.1: a squad exchange is pairings of duel rounds; `StandingOrder` rows; "its owner is the lane that owns squads and orders (MB…)" | owned here: `proposals/04_MB_squad_grid_of_named_characters.md` (§B4.6). Pairing is the host's policy; combat is unchanged | proposal |
| the carry rule | `03_PC_loadout_and_carry.md`: `carry_demand(weapons: tuple, armour: str)`, reading keys of personal combat's export | **the keyed form cannot serve a troop**, whose primary may be a bow or a pike that the roster lacks (C-3). Needed: the same leaf exposes the mass form, `carry_demand_of(masses: tuple, armour: str)`, which the keyed form calls. One rule, two spellings of its argument; no second function | a one-line amendment the PC lane owns; stated in the `_B` proposal |
| the weapon in hand | PC: `DuelState.in_hand`; `switch` costs the next action's readiness; an NPC's trigger reads `close_unwieldiness` | the unit's form: `Subunit.in_hand`; the switch costs a tick; triggers `enemy_range`, `flanked`, `volleys_spent`. Same state name, same "costs the next action" rule at both scales (NERS-S) | consistent |
| the approach | PC: `aggressive`, `normal`, `defensive` per round, calibrated so "no approach beats `normal` … and each approach beats one other in some matchup" | the first audit proposed one roster for both scales. **Not yet:** the unit-scale stance fails exactly the PC lane's bar (F-MB-21). Share the *bar*, not the roster, until the stance passes it | corrected |
| the grid | PC §6 item 2: the requirements row's "grid-based map combat with units" is read two ways (mass battle's cell field; a tactics grid of individuals) | both exist as different things: the cell field (this subsystem) and the squad grid (§B4.6). The requirements row should name which it counts | cross-listed; CORE's row |

### B5.2 With the campaign layer (`audits/06_FA_audit.md`, `07_SE_audit.md`; their addenda were being written and held no mass-battle section when read)

| what a field needs from the campaign | reading in the sibling audit | reading here | owner |
|---|---|---|---|
| a reason for a war and a commander who marches | FA F-FA-03: 26 of 33 seats may `march`; the marchers at seed 0 were a treasurer, a legal advisor, a guild representative and a skald. F-FA-04: "war has no producer and draws no response" | confirms the first audit's F-MB-03 from the other side: the army's holder is its commander (`effects_army.py`), and nothing ties `march` to holding one. Once armies exist, `march` with an army should require its holder; that is FA's grant-by-row (`proposals/06_FA_remit_grant_by_row.md`) | FA |
| training sites | SE: site kinds `barracks`, `archery_range`, `stable`, `siege_workshop` exist with counts of 0 (`rosters.yaml:1913-1946`) | the realm has **venues** named barracks (`engine/season/npcs.yaml:114`, `b_s_014_barracks`) and no **Site** of kind `barracks`: two things with one name, and only the second trains troops. The first audit's R-07 (plant a training Site at each seat) should plant them where the venues already are | SE (data) |
| supply | SE: `settlements.provision` built, shipped off; R-SE-22: its ration is a minimum over every eaten kind | unchanged; the Bannerlord shape (unfed, then demoralised, then deserting) needs only the middle link here: a field whose provision bounded its troops starts at a lower morale, by the stance row that already feeds morale-start | SE flips; MB reads |
| upkeep and desertion | FA H-158: "no computed act pays upkeep" | the archived design has the rule (unpaid professionals lose Discipline each season; levy unaffected: `military_layer_v30.md` §1.7). No carrier exists. Proposed as an `upkeep` column on the troop row and one consequence, in `proposals/04_MB_campaign_party_economy.md`; who pays and from what is FA's and SE's | MB datum; FA, SE acts |
| veterancy | not in either audit | the archived design's Experience (Fresh, Seasoned, Veteran; +1 Power a step; lost when the unit is destroyed, `military_layer_v30.md` §1.6) and Bannerlord's tiers are the same shape. Carrier: `experience` on the unit row, written by `_eff_march` | MB |
| the cost of a heavy army on the march | — | sourced shape (Bannerlord: speed falls with size and carried weight). **No march clock exists to slow** (a `march` resolves in the round it is declared, `ED-IN-0301`), so the carry cost cannot bite at campaign scale today. Named, not built: it needs CORE's travel time first | CORE, then MB |
| captives | first audit §5.5 | unchanged; the squad proposal's outcome names the fallen persons, which is what a `capture` act needs | PC |

### B5.3 With the shared roller (`audits/10_DICE_audit.md` F-DICE-07, F-DICE-08; `proposals/10_DICE_one_roller_one_fraction_rule.md`)

The DICE lane's proposal is accepted as written: mass battle's `roll_pool`, `roll_pool_fractional`,
`compute_degree` and its sigma functions become calls to the dice engine, with the tolerance moved to the
owner. Three notes from this side.

1. **It is the first `engine` import in the module.** `modules/mass_battle/` imports nothing from
   `engine.*` today; the other two registered modules already import the dice engine
   (`modules/combat/core.py:20-21`, `modules/social_contest/roll.py:60`, as the DICE audit cites). That
   settles the first audit's open question in §15 for an engine leaf. It does not settle module-to-module
   import, which the squad grid avoids by going through the composition role.
2. **Order of landing.** The DICE gate is "mass-battle goldens and the season hash byte-equal". The
   arrangement change (§B3.4) and the first audit's scale and grade change both move every fought field.
   DICE's edit should land first, against today's goldens, so that its byte-equality can be read.
3. **The fractional die and one-cell bodies.** `roll_pool_fractional` is reached twice a fought field
   (DICE audit). At today's one-to-four-cell bodies a single pair roll decides a body's tick; at
   calibrated bodies many pairs do. The fraction rule's variance matters more on today's bodies than it
   will after §B3.4; a calibration made before the arrangement change will not carry over it.

### B5.4 Jordan's stated intent against ratified Layer 1: what each requires, and whether they reconcile

Two Layer 1 rules bear on the intent. Both passages were opened at the lines given. Layer 1 is not edited
by this lane; where a Layer 1 file needs a change, it is named with its owner.

**(a) "No second resolver. No auto-resolve formula. No fast path."**

| | text | at |
|---|---|---|
| Layer 1 | "**No second resolver. No auto-resolve formula. No fast path.**" and: "THIS IS THE REFUSAL WITH NEITHER A MECHANISM NOR A CHEAP TEST. It is enforced by a person noticing." | `architecture/holonic_ARCHITECTURE.md:984-990` (§27.2) |
| Layer 1 | "A scene is a slice whatever depth it is played at: summarised in a line, narrated, or expanded into its own contest … If a played scene and a summarised one were different objects, they would need to agree *on average* — which is the twenty-year complaint against every auto-resolve in the genre. **They agree exactly, because they are the same slice.**" | `architecture/meta/03_VERBS_AND_LOOPS.md:146-153` (§C.4) |
| Layer 1 | "no second resolver … CONVENTION" | `04_CODE_ARCHITECTURE.md:761`, `:788` |
| Jordan, 2026-11-12 | "the choice to **fight a battle or auto-resolve it**, with the two kept consistent" (Total War); "the player may **command, join or auto-resolve**" (Bannerlord); "**resolved automatically** while the player manages the composition and the orders" (Ogre Battle, Unicorn Overlord); and: "**One path.** The cell-level battle that a player commands and the auto-resolved battle … must run the same cell-based resolver" | `AUDIT_BRIEF.md:245-246`, `:311-326` |

*What each side requires.* Layer 1 requires that there be one function that decides a field, at every
depth, and that a shallower rendering be the same slice, not an estimate of it. Jordan requires that a
battle can be left to resolve itself and can be commanded, and that the two be consistent.

*Reconcilable without breaking the rule?* **Yes, completely, and Jordan's own "one path" sentence is the
reconciliation.** "Auto-resolve" names who supplies the decisions, never a formula: the delegated battle
is `resolve_field` with every decision supplied in advance (standing orders, or a chooser); the commanded
battle is the same call with a decider at windows. §B4.4's three conditions are what make that "the same
slice" in Layer 1's sense: one entry, a decider that draws nothing, and a recorded command list under
which the delegated call returns the identical outcome. The third is the part Layer 1 asks for and the
genre does not have.

*What Layer 1 forbids that the referents themselves do.* Total War's auto-resolve "compares the statistics
of all the units" (`R6` F5): a second calculation, the exact thing §C.4 calls the genre's complaint. If the
referent is read for that shape and not for the choice it offers the player, the intent contradicts
§27.2 and cannot be reconciled. That reading is put in §B11 with its two options; this lane's reading is
that the brief excludes it.

*Where the code is on the wrong side of the rule today.*

1. `run_multi_turn_battle` and `run_multi_unit_battle` in the registered tree are a second resolution
   path with rules the first has not (pursuit by a linear damage form, freed-attacker damage, rally,
   reserve commitment), and the interactive workbench plays that one by default. The first audit's F-MB-05
   and R-05 are therefore Layer 1 conformance, not only tidiness.
2. `field_estimate` is conformant: it is samples of the one resolver on a private stream. The pressure
   on it is real, though: at about 20 ms a field of 600 a side, 400 samples is some eight seconds, and
   more after §B3.4. The conformant answers are fewer samples, a cache keyed on the frozen input, or a
   coarser display; a closed-form estimate would be the auto-resolve formula under another name. Named
   here because §27.2 says of itself that only a person noticing enforces it.
3. `_grade`'s four-way label on survivor thresholds is a second ladder (DICE audit, resolution 22). It
   has no reader; the first audit's R-03 deletes it.

**(b) "Units are persons, at weight. One type; there is no unit class."**

| | text | at |
|---|---|---|
| Layer 1 | "**units** — persons, at weight. One type; there is no unit class" · "One scale down, unchanged: a squad is the members of a faction present at a rung, resolved once, every combatant a `Person`." | `03_VERBS_AND_LOOPS.md:258-270` (§E.2.1); the same row at `10_FACTIONS_AND_DEPLOYMENT.md:89`, `:97` |
| Layer 1 | "`units = PersonId[] at weight` — one type. There is NO unit class, at any scale" | `04_CODE_ARCHITECTURE.md:802` (§C.5.1) |
| Layer 1, amended | "**AMENDED BY ED-IN-0306 (Jordan, 2026-10-28), for armies only.** An army is no longer only `PersonId[] at weight`: a faction's order of battle (formations, subformations, troop-type assignments, tactic, strategy) is a typed record the season loop reads. The freeze above is unchanged" | `04_CODE_ARCHITECTURE.md:813`; ledger `registers/editorial_ledger_in.jsonl:88` ("This overturns the part of … section C.5.1 … for armies") |
| Jordan, 2026-11-12 | "army → unit → subformation → troops", each unit with "its own subformation and its own troop types"; from Ogre Battle and Unicorn Overlord, "units are small squads of named, distinct characters" | `AUDIT_BRIEF.md:220-230`, `:311-315` |

*What each side requires.* Layer 1 requires that the season hold no unit object: sides are faction
views, combatants are persons, and (since the amendment) an army's composition is a typed record frozen
with the sides. Jordan requires a nested battlefield structure with designer-editable troop types and
loadouts, and squads of named characters.

*Reconcilable without breaking the rule?* **Yes, on the amended text, in three parts.**

1. *In season state a unit is a row, not a class.* The army is a `Record`; its unit rows name cohort
   `Person`s and headcounts (`armyrecord.py:13-19`). Everything proposed here adds optional columns to
   that row (post, ranks, files, secondary, standing orders, officer, experience, arrears) and tables to a
   data file.
   No new kind of thing enters the `World`, nothing but a person acts, and the amendment's own list
   ("formations, subformations, troop-type assignments, tactic, strategy") covers each column but
   `experience` and `arrears`, which are facts about the record's own row, written by `_eff_march` and by
   the campaign's payment path.
2. *Inside the module, `Unit` and `Subunit` are values built from the frozen input and discarded at
   return.* The roster contract governs what the seam is handed ("what it actually forbids: handing the
   wrapper anything that is not the projection", `04:810`), not the resolver's internals.
3. *The squad of named characters is the un-amended rule, not an exception to it.* "Every combatant a
   `Person`" is exactly Ogre Battle's and Unicorn Overlord's squad. That is why §B4.6 puts it on the duel
   round and not in cells: built as a mass-battle unit it would be the unit class the rule refuses.

*What does not reconcile, and is not proposed.* A unit as a first-class thing with identity in the world
(something a person can hold a claim about, name, remember, swear to): ARC-07's "condition on a unit" asks
for it, and the first audit re-read that need as claims in the men's ledgers for this reason. It would
need a further amendment of §C.5.1. Listed in §B11 as the named conflict.

*An inconsistency inside Layer 1, named at the site.* `03_VERBS_AND_LOOPS.md:261` and
`10_FACTIONS_AND_DEPLOYMENT.md:89` state the rule without the amendment that `04:813` carries. Two rows
decide one thing differently; the later ruled row governs (ED-IN-0306). The pointer edit to those two
files is IN's (R-38); it needs no ruling, since the ruling exists.

**(c) The one true non-conformance found on the way: the field returns a winner** (F-MB-24). Layer 1 asks
for a margin graded on the one ladder (`04:774-786`, `:1050`; `03:273-289`); the field returns a winner
and the host mints two bands from it. This is not a conflict between Jordan's intent and Layer 1; it is
code against Layer 1, and by `CLAUDE.md` §0.05 the code changes. How it changes has two defensible forms
(§B11 item 3).

## B6. Resolutions and proposals

### B6.1 Resolutions (continuing the first audit's table; ladder steps as there)

| id | kind | what | decided resolution | step | proposal |
|---|---|---|---|---|---|
| R-30 | unclear | "unit" and "subformation" name different levels in the intent and in `armyrecord.py` | the intent's words win at the designer's surface: the troop file and the menu say **unit** for a body and **subformation** for its arrangement. The record's key `subformations` keeps its spelling (a rename is a hash mover for nothing); `armyrecord.py`'s docstring states the mapping once | 5 | `04_MB_cell_hierarchy_as_data.md` |
| R-31 | inconsistency | the field returns a winner; Layer 1 asks for a margin or, by the combat ruling, a read state (F-MB-24) | the module returns the field's end state per side (`routed`, `conceded`, `share`) and no `verdict`; `seam/ladder.py::field_degree` reads `Won`, `Lost` or `Drawn` off it, as `combat_degree` reads a scene. This amends the first audit's R-03 and R-04 in one field | 4 (the combat exemption, Jordan 2026-09-03) | `04_MB_manager_battle_one_resolver.md`; §B11 item 3 |
| R-32 | gap | the season packs every body at the cell cap; the oracle calibrates on another generator (F-MB-20) | explicit ranks-by-files bodies at one stated deployment density, the tier table's; the cap is the control | 3, 4 | `04_MB_cell_hierarchy_as_data.md` |
| R-33 | gap | the army's formation is one hard-coded rule | `formations` rows and a `post` per unit; today's rule is the row `line`; the harness's envelopment and refused-flank builders become rows | 5 | same |
| R-34 | inconsistency | two of three strategies lose to the third (F-MB-21) | `strategy` leaves the record's choice surface and the menu; `line` is what an army does; the stance stays settable per unit by a standing order. It returns as a roster when each value wins somewhere, the PC lane's bar | 4 (the PC lane's calibration rule) | `04_MB_manager_battle_one_resolver.md` |
| R-35 | inconsistency | troop types that differ only by weapon are identical (F-MB-22); behaviour keyed on type names; "mounted" has two owners (F-MB-23) | reach and support depth derive from the weapon in hand's class; `mounted`, `charge`, `wheel`, `default_role` are columns; knights templar is mounted in one place | 5 | `04_MB_unit_loadout_and_weapon_in_hand_B.md` |
| R-36 | inconsistency | "one weapon roster: personal combat's" cannot hold a troop's missile weapon or pike (C-3) | one owner a fact, not one file: an arm's mass lives in personal combat's export when its key is there and in `troops.yaml`'s `arms` when it is not; the loader refuses a key stated in both; the carry leaf takes masses | 5 | same |
| R-37 | inconsistency | stale surfaces (F-MB-25): the fighting-withdrawal Status; `reform_check`'s docstring; the "melee sidearm" comment | correct each at its site when its file is next touched: the Status line to "BUILT, on by default"; the docstring to the flag's value; the comment goes when `arms` lands | 1 | none (pointer and comment edits) |
| R-38 | inconsistency | `03_VERBS_AND_LOOPS.md:261` and `10_FACTIONS_AND_DEPLOYMENT.md:89` lack the ED-IN-0306 amendment `04:813` carries | the later ruled row governs; add the same amendment note at both sites. A Layer 1 edit, IN's, not made here | 1 | none |
| R-39 | gap | the manager's vocabulary has no carrier (F-MB-26) | `standing_orders` on the unit row over the engine's exported closed sets; `fall_back_at` becomes one such row | 4 (`fall_back_at` is already an `Order`) | `04_MB_manager_battle_one_resolver.md` |
| R-40 | gap | officers are counted and read by nothing | `officer` on the unit row names a person; three reads, in order: his unit's contact makes a duel contact (§B5.1); his fall erodes his unit's morale; the general's span counts officers (built). Command from the commander is the first audit's §14 | 3 (the archived design's §D.2), 5 | same; `04_MB_squad_grid_of_named_characters.md` |
| R-41 | unclear | where the squad of named characters lives | on the duel round, by a host pairing policy over a two-row grid; not in cells | 3 (Layer 1 §E.2.1), 4 (PC §5.1) | `04_MB_squad_grid_of_named_characters.md` |
| R-42 | gap | no veterancy, no upkeep | `experience` on the unit row (0 to 2, +1 Power a step, lost with the unit); an `upkeep` column and one consequence for arrears | 3 (`military_layer_v30.md` §1.6, §1.7) | `04_MB_campaign_party_economy.md` |
| R-43 | unclear | the flow skeleton's anchors are dead | superseded: its adapter and callers were deleted; it is archived reference and is not repaired. `[UNVERIFIED: what `tests/valoria/test_flow_skeletons.py` still checks of it]` | 2 | none |
| R-44 | unclear | the first audit's R-07 plants training Sites "at each faction seat" | plant them where the realm already has venues named for them (`b_s_014_barracks`, `b_s_007_barracks`), so one place is one thing | 4 | none (SE's data; cross-listed) |
| R-45 | gap | the estimate's cost invites a formula | fewer samples, or a cache keyed on the frozen input; never a closed form (§B5.4) | 3 (Layer 1 §27.2) | `04_MB_manager_battle_one_resolver.md` |

Resolutions decided in this addendum: **16** (R-30 to R-45). With the first audit's 29: 45.

### B6.2 Proposals written by this lane

All under `proposals/2026-11-12-subsystem-audit-suite/proposals/`, Status PROPOSED.

| file | carries | supersedes |
|---|---|---|
| `04_MB_unit_loadout_and_weapon_in_hand_B.md` | the troop file (`arms`, `troops`), the loadout, the weapon in hand, the carry factors, the columns that replace the name tests; R-35, R-36 | `04_MB_unit_loadout_and_weapon_in_hand.md` (the first lane's; left unedited) |
| `04_MB_cell_hierarchy_as_data.md` | the unit's arrangement, the deployment density, `formations` and `post`, kinds within a unit; R-30, R-32, R-33 | nothing |
| `04_MB_manager_battle_one_resolver.md` | standing orders, the general's action, the interventions list, the report, the end state in place of a winner, the estimate; R-31, R-34, R-39, R-40, R-45 | §B of `04_MB_playable_field_scenario.md` (its `PhaseOrder`) and the `verdict` field of `04_MB_typed_outcome_and_one_path.md`; the rest of both stands |
| `04_MB_squad_grid_of_named_characters.md` | the squad scale; R-41 | nothing |
| `04_MB_campaign_party_economy.md` | veterancy and upkeep; R-42 | nothing |

### B6.3 Order, against the first audit's §8

The first audit's steps 1 and 2 (scale, grade, typed outcome) still come first, with R-31 folded into
step 2. Then: DICE's roller (byte-equal against today's goldens); the troop file as data with no
behaviour change (the `_B` proposal's stage 1); the arrangement (§B3.4), which is the mover that makes
the cell grid the battlefield; then standing orders and the general's action; then the loadout's second
weapon; then squads; then veterancy and upkeep. Kinds within a unit are last. The first audit's step 7
(CR-12) should be measured after the arrangement, not before: its exponent is fitted on tier-table
bodies, which is where the season will then be.

## B7. Evidence log

Python 3.13 (the container's), `PYTHONHASHSEED=0`, read-only. Scripts and outputs:
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/MB_B/`. No `pytest`,
no `aperture`, nothing written to a tracked file. Bodies by `orderofbattle.build_unit` (or
`armies.build_army` where an explicit grid is needed), fought by `battle_loop.run_battle(max_turns=18)`
under `rngsource.using(random.Random(seed))`.

| run | seeds, size | outcome |
|---|---|---|
| `cells_probe.py` | none (construction only) | preset armies: weight 20 → 2, 1, 2, 1 cells (6 in all); weight 30 → 3, 2, 2, 1 (8); levy 600 → 3; a 5,000 army → 12, 7, 10, 3 in 2 to 3 ranks; cavalry `Shock` 300 → 3 cells, `Arrowhead`, 2 rows |
| `generators_probe.txt` | none | tier table Line: 9, 15, 25, 35 cells (3 x 3, 3 x 5, 5 x 5, 5 x 7) at 100, 200, 400, 800 troops; `footprint_for` at the cap: 1, 1, 2, 4. (The script's last line, a call of `_weighted_unit` with a wrong argument, raised; nothing depends on it) |
| `density_probe.py` | 0 to 39; 600 heavy infantry a side; A at the cap | against the cap 15, 24, 1 (A, B, drawn); concentration 100: 14, 24, 2; concentration 50: 16, 18, 6; 6 x 2: 17, 16, 7; 3 x 4: 18, 14, 8; 12 x 1: 22, 0, 18, losses 3.6% and 26% |
| `mirror_probe.py 300` | 0 to 299; identical single bodies of 600 | heavy infantry: A 133, B 154, drawn 13; losses 25% and 21%; 8.2 ticks. Spearmen: 134, 137, 29; 19% and 18%; 9.9 ticks. No side bias established (1.2 standard deviations) |
| `lever_probe.py 200` | 0 to 199; spearmen 300, archers 150, cavalry 150 a side | tables in F-MB-21; about 20 ms a field |
| `pike_probe.py` | 0 to 199 at 600 a side; 0 to 39 at 3,000; 0 to 99 for single bodies of 600 against cavalry `Shock` | pike against heavy infantry: identical winner and both sides' troops (rounded to 1e-6) in 200 of 200 and 40 of 40; cells 2, 1, 2 in one rank and 8, 4, 8 in two. Against cavalry: pike 35, 59, 6; heavy infantry 35, 59, 6; spearmen 25, 72, 3; light infantry 25, 72, 3 |
| `brace_probe.py` | 0 to 99; 600 against cavalry 600 `Shock` | `ShieldWall`: pike 38, 60, 2; heavy infantry 38, 60, 2; spearmen 22, 72, 6. `Anvil`: 38, 59, 3; 38, 59, 3; 25, 72, 3. Pike identical to heavy infantry in 100 of 100 under each |
| `tests.txt` survey | 43 files | 9,872 lines; two of the three tests in `test_charge_momentum_impulse.py` have a `pytest.skip` path; reloads in `test_feigned_retreat.py` (15) and `test_octagon_damage.py` (5) |
| greps at HEAD | — | type-name tests (`units.py:943`, `:1491`; `orchestration.py:1213`, `:1217`; `armies.py:267`; `orderofbattle.py:150`); `REFORM_CHECK_ENABLED` and the three `MB_YIELD_*` flags default `'1'`; `Unit.ncells` assigned once (`units.py:2872`); call sites of `pursuit_damage`, `resolve_feigned_retreat`, `unit_in_reserve` all inside `run_multi_unit_battle`; 91 `os.environ` reads under `modules/mass_battle/` (the first audit's count, confirmed) |
| personal combat's weapon keys | `grep` of `modules/combat/weapons.py` | 54 keys: rapier, arming, longsword, greatsword, sabre, dagger, paired_short, spear, staff, mace, poleaxe, yari, the polearm and East Asian families, the half-sword forms. None of bow, crossbow, sling, javelin, pike, lance |
| referent search | `grep -ril "ogre battle\|unicorn overlord\|bannerlord" research proposals .designs .audit` | Ogre Battle: every hit is the character-creation questionnaire |

**Controls and limits.** Every lever figure is read against the same-run control and a binomial standard
deviation of about 5 at n 200; the single-body side bias was checked at n 300 before any A-against-B
figure was used. One field only was probed for F-MB-21 (an even, open, combined-arms field); the claim is
stated for that field. No balance claim is made from any of it: these are readings of mechanism, at one
size.

`git status --short` before finishing: this lane's changes are this file and five proposal files and
nothing else. HEAD moved from `6eff039` to `f8a629b` while this was written (the orchestrator's interim
commits of the suite's drafts, which also began tracking these six files part-way through);
`git diff --stat 6eff039 HEAD -- modules engine systems tools tests references architecture research
.designs .audit` is empty, so every reading above holds at the new HEAD.

## B11. Survivors for Jordan (additions to the first audit's §11)

Three. Each is here because the brief requires a conflict with ratified Layer 1 or a ruled item to be
listed with its two options, not because the ladder left it open; this lane's reading is given with each.

1. **Auto-resolve: a mode of the one resolver, or a calculation of its own.** (§B5.4 (a).)
   - *(a) A mode.* The delegated battle is the cell resolver run on standing orders; the commanded one is
     the same call with a general's action at windows; a recorded battle replays exactly. Layer 1 §27.2
     and §C.4 stand untouched. Every unwatched battle costs a full resolution, and an estimate costs
     samples of it. War is the same thing whether or not anyone is looking.
   - *(b) A calculation.* A cheaper comparison of the two armies for battles nobody plays, as Total War
     does. Unwatched war is fast and the estimate is free; the played and the delegated battle agree only
     on average, standing orders and arrangement stop mattering to any battle the player skips, and
     §27.2 is amended. *This lane's reading:* (a); the brief's "one path" sentence and the 2026-07-08
     doctrine both say it. Nothing here builds toward (b).
2. **A unit: a row on the army's record, or a thing in the world.** (§B5.4 (b).)
   - *(a) A row.* Units are groupings of cohort persons' headcounts with columns (kind, arrangement,
     loadout, orders, officer, experience). Layer 1 as amended by ED-IN-0306 stands. A unit has no
     memory but its officer's and its men's; "the army that stayed" is a story about persons.
   - *(b) A thing.* A unit has identity: persons hold claims about it, swear to it, fear it; it carries
     its own history and conditions. Regiments become characters of the world. §C.5.1 is amended again
     and the knowledge model gains a kind. *This lane's reading:* (a), as ruled on 2026-10-28; listed
     because ARC-07's need is worded for (b).
3. **What a field returns: its end state, or a margin.** (F-MB-24, R-31.)
   - *(a) The end state, read off as combat's scene is.* Bands `Won`, `Lost`, `Drawn` (with `Unopposed`
     and `Invested`), read by the host off which side broke or conceded. A battle is won or it is not;
     how hard it was shows in the casualties and the report. Extends the 2026-09-03 combat exemption to
     the field: a narrowing of Layer 1's "the return type is `Margin`" that needs Jordan's word, as
     combat's did.
   - *(b) A margin on the one ladder.* The field returns a net (for instance the difference of the two
     sides' broken shares on the ladder's scale) and the ladder grades four bands: an overwhelming
     victory, a victory, a partial, a failure, each with its own writes. Battles then differ in *kind* by
     how decisively they are won (a crushing win could move title where a narrow one moves presence),
     and mass battle joins every other contest on one grading. Layer 1 holds as written; the four bands'
     writes are new design. *This lane's resolution:* (a), by the combat precedent, because the module's
     own four-way split is thresholds nobody calibrated and (b) would need them.

Nothing else from this addendum survives the ladder. The scale of a cell (§B3.4), the meaning of the four
words (C-1), the strategy roster (R-34), the weapon roster (R-36), where squads live (R-41) and the
stale surfaces are answered above.
