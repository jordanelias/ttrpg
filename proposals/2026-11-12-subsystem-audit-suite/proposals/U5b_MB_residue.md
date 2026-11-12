# U5b · MB — residue: the mass-battle items no proposal carried

## Status: PROPOSED (a plan for future execution; nothing here is executed by the closing lane)

Author: U5b closure lane (Fable), 2026-11-12. Read at `6910680`. Each section is a resolution of
`audits/04_MB_audit.md`, `04_MB_audit_addendum_B.md` or `16_PESSIMIST_MB.md` that its audit decided and
filed under "none (pointer edit)" or "an edit, no proposal file needed", two lists that two lanes wrote
separately and that must be one, or an item another closure handed to this family. Reference only
(CLAUDE.md §0.05). Sections are independent and commit-sized.

## What it changes in `engine/season/` at runtime

§1 changes which roles a menu offers (no shipped person forms an army verb, so no season moves). §5 lets
the chooser price a `march` by what the marcher believes, behind the shipped `odds_weighting`. §6 refuses
a side past the module's stated ceiling. The rest moves nothing.

## §1 · One list of roles that leave the menu (first audit R-10; pessimist F-PES-MB-08, resolution 7)

Two lanes listed them from two instruments. The first reads `ROLE_INSTRUCTION_PRIMITIVES` (keywords with
no primitive); the second ran each role against no role, friction off, n 60, and counted fields identical
to six places (`p10_edges.py`). The union, decided once:

| role | off which menus | why | returns when |
|---|---|---|---|
| `Pursue` | every menu (cavalry, light cavalry, light infantry) | its instruction `pursue` maps to `None`; identical to no role in 60 of 60 | `16_PESSIMIST_MB_rout_has_two_exits.md` gives `pursue` its primitive (`may_pursue`) |
| `Screen` | every menu | keyword `screen` has no primitive; identical in 60 of 60 | a primitive exists |
| `Harass` | every menu | keyword `harass` has no primitive; its `GappedLine` shape is gone at tick 1 (F-MB-18) | a primitive exists and R-24 holds |
| `Feint` | every menu | reached only through `resolve_feigned_retreat`, which no season path calls; identical in 60 of 60 | `26_MASS_BATTLE_maneuver_orders.md` reaches the feint |
| `VolleyLine` | stays as a shape; its instruction tuple is emptied (`volley`, `loose`, `shoot_move` have no primitive) | identical in 60 of 60 for archers | — |
| `Anvil` (heavy infantry against foot) | stays: it differs against horse (`brace_probe`) | recorded: inert against foot | — |
| `Flanker`, `Shock` | stay: they are behaviours, not no-ops, and both lose (13 against 42; 16 against 41) | the addendum's F-MB-21 class; ride with `04_MB_manager_battle_one_resolver.md` §3's bar (a value returns to a choice surface when it wins somewhere) and are read again after the pair rule changes | — |

Edits: `modules/mass_battle/config.py` (`TROOP_TYPE_ROLES`, `ROLE_SPEC`: the rows above; when the troop
file lands they are the `roles` column of `references/troops.yaml`); the keywords `pin`, `loose`,
`screen`, `pursue`, `volley`, `shoot_move`, `harass` leave `ROLE_SPEC`. This replaces the list in
`04_MB_typed_outcome_and_one_path.md` §2 (its fifth bullet) and the list under F-PES-MB-08.
**Gate.** `p10_edges.py` part (b) re-run: no role on any menu reads "identical in 60 of 60" against no
role; `tools/ci_golden_modes_check.py` digests equal. **Falsifier.** A menu row whose removal changes a
field. **Movers.** None.

## §2 · Pointer, status-line and comment edits (first audit R-12, R-13, R-14, R-23, R-28; addendum R-37, R-38, R-43)

| id | file (owner) | edit |
|---|---|---|
| R-12 | `registers/handoffs/HANDOFF_MB.md` | "a side under 100 troops … is not hurt" is deleted when `04_MB_headcount_grade_and_scale.md` lands (true of the troops, false of the write until then) |
| R-13 | `proposals/2026-10-29-army-phase5-design.md`, M11 | one line: superseded by CR-24 (`field_winner_casualties: engine` shipped); the code governs |
| R-14 | `engine/season/requirements.yaml`, the scales note | "reached via natural computed play" reworded to what the instrument reads: `march` executes; a fought field does not (seeds 0 to 2: 0, 0, 1) |
| R-23 | the plan card of CP-T04-10 | its `levy` / `disband` rows closed as superseded by ED-IN-0306's verbs (`recruit`, `disband_unit`, `discharge_troops`); the larder stock stays held |
| R-28 | none | `videogame_mode_spec.md`'s two resolvers are superseded by Layer 1 §27.2 and A-1; quarantined reference is not edited |
| R-37 | `proposals/mass_battle_fighting_withdrawal_v1.md` Status; `modules/mass_battle/orchestration.py:287` | the Status reads "BUILT, on by default" (`MB_YIELD_*` default `'1'`, `config.py:262-272`); `reform_check`'s docstring states its flag's value (`REFORM_CHECK_ENABLED` defaults `'1'`, `:278`); the "melee sidearm" comment (`troop_types/registry.py:116-122`) goes when `arms` lands |
| R-38 | `architecture/meta/03_VERBS_AND_LOOPS.md:261`, `10_FACTIONS_AND_DEPLOYMENT.md:89` | **Layer 1 text, IN's, owed and not applied here:** the ED-IN-0306 amendment note that `04_CODE_ARCHITECTURE.md:813` already carries is added at both sites. A-2 confirms the ruling it records; the edit decides nothing |
| R-43 | none | the flow skeleton's dead anchors: archived reference, not repaired; `[UNVERIFIED: what tests/valoria/test_flow_skeletons.py still checks of it]` is opened by whoever next touches that test |
| — | `engine/season/hole_register.yaml` | H-250, H-354, H-359, H-308: as `04_MB_headcount_grade_and_scale.md` lists. H-355: closed by A-57 and A-58 (the land passes on an aggressor's win; a routed defender is re-homed). H-151: closed (its own `default:` says so). H-360: pointed at the per-part outcome |

**Gate.** `python -m engine.season.harness.register --requirements` loads; `python tools/freshness_gate.py`
as CI runs it. **Movers.** None.

## §3 · Training Sites go where the realm already has venues named for them (addendum R-44; first audit R-07)

`engine/season/npcs.yaml:114` names a venue `b_s_014_barracks` and the realm holds no Site of kind
`barracks`; site-kind counts for `barracks`, `archery_range`, `stable`, `siege_workshop` are 0
(`rosters.yaml:1913-1946`). The realm data edit (SE's file; `07_SE_campaign_supply_and_muster.md`, U5d's
family) plants each training Site at the settlement whose venue already carries the name
(`b_s_014_barracks`, `b_s_007_barracks`), so one place is one thing. Cross-listed; no MB file changes.
**Gate.** `armyrecord.options` on that realm offers a trained kind beside levy. **Movers.** Declared, at
SE's landing.

## §4 · Test strength handed across by U5a (`audits/01_CORE_audit_addendum_C_tests.md:262`; F-TEST-10 row 6)

1. **The standing `xfail`.** `tests/valoria/test_mass_battle_maneuvers.py:86`: a non-strict `xfail` whose
   own reason says it is left in place because the test is not a reliable pass for one fixture's
   low-base-speed detachment. Decided: after the calibration batch
   (`U5b_MB_rulings_in_the_field.md` §6 row 4) the test is re-run at its seeds; if it passes at every seed
   the marker is deleted; if it fails at some, it becomes `strict=True` with the failing seeds named, on
   `tests/valoria/conftest.py`'s own rule (*"a non-strict xfail would silently absorb a fix"*, `:17`). A
   manoeuvre the pair rule inverted (pessimist §2.4) is expected to change here.
2. **`approx` on conservation claims.** *"35 tests use `approx`, some on conservation claims
   (`_conservation.py:99`)"*. A conservation claim is an exactness claim and `approx` cannot observe its
   failure (CLAUDE.md §0.1 pt 2). Each `approx` on a troop-count conservation becomes an exact comparison
   on the integer count, or on the float with the engine's own epsilon named at the site
   (`resolution.py:101-120`'s), `[UNVERIFIED: which of the 35; the tests lane's scan names them and this
   lane did not open the files]`. Tolerances on win shares and other sampled readings stay.

**Gate.** With one troop removed in process inside `distribute_casualties`, the conservation tests fail.
**Movers.** None. No new test file and no CI row.

## §5 · A commander may weigh a field by what he believes (first audit step 5b; U5a F-DICE-14 Edit C)

`seam/wrappers/sigma.py::believed_chance` answers `None` for a band of another module, and
`field_estimate` is *"the player's display only — no NPC reads it"* (`seam/wrappers/mass_battle.py:465-466`,
AQ-X1). The two are reconciled without letting an NPC read the world's odds:

1. `believed_chance`, for a row whose prize binds the `mass_battle` provider: `field_estimate(…,
   believed=…)` (`04_MB_playable_field_scenario.md` §F), the input built **from the believer's own
   claims** about the defenders' strength and walls; a person who holds no such claim gets `None`
   ("cannot say"), which `10_DICE_believed_odds_have_a_prior.md` Edits A–B (U5a's) already price as a
   prior, not as certainty.
2. The estimate is samples of the one resolver on a private stream; its count for this caller is the
   fixture `believed_field_samples` (seed 40), and a cache keyed on the frozen input is lawful
   (`04_MB_manager_battle_one_resolver.md` §8). No closed form (A-1).
3. AQ-X1's sentence at the wrapper is restated: no NPC reads the **world's** odds; any person may reckon
   on what he believes.

**Gate.** A commander told a false strength marches where one told the truth does not (the first audit's
5b gate), over seeds 0 to 29; `content_hash` is unchanged by an estimate whose act is not chosen.
**Falsifier.** An NPC's estimate built from a strength no claim of his names. **Movers.** Worlds in which
a `march` Candidate is scored under `odds_weighting: believed`.

## §6 · Extremes the pessimist measured (`audits/16_PESSIMIST_MB.md` §3.3)

1. `modules/mass_battle/massbattle.py::resolve_field`: a side past the module's stated ceiling
   (`MAX_TROOPS_PER_UNIT`) is refused with a typed result (`status="SCALE-GAP"`, on `PARTY-GAP`'s shape),
   not resolved. Today 20,000 a side resolves.
2. A field of nobody against nobody, or of two sides below the floor, is the host's `Unopposed` /
   `PARTY-GAP` branch and never reaches the cell engine (today the crash floor of one man a side resolves
   and the attacker "loses"). After `04_MB_headcount_grade_and_scale.md` and the squad entry, the only
   sides that reach `resolve_field` are blocks.

**Gate.** `p11_extremes.py` re-run: 0 and 1 a side never enter `run_battle`; 20,000 a side returns
`SCALE-GAP`. **Movers.** None in shipped play.

## §7 · Plan rows (first audit §6.1; pointer edits in `workplans/`)

| row | edit |
|---|---|
| CL-TROOP | answered against ED-IN-0306 for the stock (the army Record, recruiting and presets exist); what remains is the population cost of raising, which is SE's (`07_SE_population_census.md`, by title); the row is re-scoped to that |
| MB-08 | split: "who marches where" is scheduled (`14_VERBS_PHYSICAL_B` B1's `Field` class; CHAR's cells); the map generator stays LEAVE |
| CR-12 | its hold "for Jordan" is re-pointed to D-35 as adjudicated by `audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md` R-8; the build order is `04_MB_cr12_linear_law.md`'s |
| CR-52 | built after the opportunity-key edit (`14_VERBS_MILITARY_C` Edit 5) |
| CP-T04-04 | unchanged (held on Ask C (b)); the bouts of `26_MASS_BATTLE_cell_scale_and_time.md` §3 give later engagements inside the scene |

## §8 · Cross-listed, another family's write

- **A siege's wear is a fixed fraction** (`loop/effects_economy.py:141-158`, `_fall`;
  `audits/25_GROUNDING_ENGINE.md` G-34). `Invested` wears the garrison by it. The draw is SE's
  (`sabotage`'s owner; U5d's family); `14_VERBS_PHYSICAL_B` §B2 reads the same formula for a burnt town.
- **The estimate's cost** (R-45): carried by `04_MB_manager_battle_one_resolver.md` §8.
- **`modules/mass_battle/` floats** against the port: A-29 (declared floats now); `11_GO_float_contract.md`
  (U5d's). The seam still quantises shares (`04_MB_typed_outcome_and_one_path.md` §1).

## §9 · Three resolutions whose named carrier does not contain them (first audit R-24, R-25, R-29)

The first audit's table names a proposal for each; the text of that proposal holds none of the three
(searched: `rekey_cells`, `GappedLine`, `truncat` across `04_MB_*`).

| id | owner | exact edit | gate |
|---|---|---|---|
| R-24 | `modules/mass_battle/config.py::MIN_DISCIPLINE` (the troop file's header when it lands) | `GappedLine`'s minimum is set to the Discipline of the lightest troop type whose menu offers a `GappedLine` role (2, per the audit's run), so `Skirmish` and `Kite` keep their shape past tick 1; or, where a type is not meant to hold it, the role leaves that type's menu (§1's test) | the audit's one-tick probe: every `GappedLine` role still reads `GappedLine` after tick 1 on each type that offers it |
| R-25 | `modules/mass_battle/hierarchy/units.py::Subunit.rekey_cells` | re-seeds `cell_morale`, `cell_start_troops` and `cell_breakpoint` from the subunit's current aggregate when the cell map is re-keyed. **Carried in fact by `26_MASS_BATTLE_movement_and_fatigue_as_data.md` §4 and its edit row for `units.py`** (the reform order needs the same repair); recorded here so the first audit's pointer resolves | after a drift, every troop id has a morale entry (the audit's "1 of 2" reads 2 of 2) |
| R-29 | `modules/mass_battle/massbattle.py::_run_and_grade`; `FieldOutcome.report` (`04_MB_playable_field_scenario.md` §D) | the count of troops in engagement groups past the fifth depth group, which `run_battle` already returns and `_run_and_grade` drops, rides the report as one figure, `truncated_troops` | a field built to exceed five depth groups reports a non-zero figure; an ordinary field reports 0 |

**Movers.** R-24 and R-25 move fields in which a body drifts (army fields only; none in natural play).
R-29 moves nothing.

## NERS reading (E last)

N: each row is a decision already taken that had no file. R: an NPC commander stops being blind to odds
without becoming omniscient. S: one role list where there were two. E: nine small edits and one fixture.

## Cost class

Edits throughout; §5 a small build after U5a's believed-odds prior.
