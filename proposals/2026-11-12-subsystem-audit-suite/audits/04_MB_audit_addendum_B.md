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
where the ratified contract asks for a margin or a read state, F-MB-24), and it is the one new item for
Jordan (§B11).

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
| C-8 | §18.1: Ogre Battle "not sourced as a battle referent" | confirmed by a tree-wide search (§B1.3). More of Bannerlord is sourced than the first audit used: speed against party size **and carried weight**, the result screen, desertion of the unpaid and unfed (`tutorials/T02_warband.md:14-22`, tagged V3 there) | §B4.1, §B5.2 |
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
| cells within a subunit are homogeneous | investigation gap 2 | still true | `core/exchange.py:100-109` |
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
| **troops** | directive (b): "the number and quality of troops per cell"; 2026-07-08: "subunit power is the aggregate or derivation of cell power" | the cell as the primitive for morale, facing, damage and troops | a cell: `cell_troops`, `cell_morale`, `cell_facing_vec`, position; type and quality are the unit's, not the cell's (`core/exchange.py:100-109`) |

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
  gains six optional fields. A player can predict that a deeper block holds longer and a wider one
  wraps, which no player can predict of one cell.

