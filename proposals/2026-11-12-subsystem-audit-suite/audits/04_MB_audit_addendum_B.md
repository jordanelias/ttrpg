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
behaviours: pike is heavy infantry to six decimal places in 340 of 340 fields, because the weapon it differs
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

