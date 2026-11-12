# SC-P2 — SC-05 decided: retire the kernel whole, forward nothing, after the hearing entry lands

## Status: PROPOSED

Source: `audits/05_SC_audit.md` F-SC-02, F-SC-08, F-SC-09; executes `ED-SC-0033` clause 2 (RULED:
*"orphaned social contest code: retire it"*). Carries `workplans/valoria_master_workplan_v11_part5.md`
SC-05, and corrects two statements in its carried block.

## What it changes in `engine/season/` at runtime

Nothing. The season loop imports nothing from `systems/social_contest/sim/contest/`; the content hash
is stationary. It deletes 16 files (about 6,700 lines) the game does not execute, four test files'
kernel imports, and 31 exported parameters no engine code reads.

## The problem (evidence)

1. **Two owners, one name.** The loop's social contest is `modules/social_contest/roll.py` (166
   lines). The kernel models the same facts a second way: its own proceeding roster (`modes.py`
   `PROCEEDINGS`, eight rows) beside `engine/season/arrangements.yaml` (nine rows); its own obstacle
   (`resolver.py::Venue.base_ob = 2.0`) beside `roll.py::obstacle`; its own bench ballot
   (`resolver.py::VoteAtClose`) beside `world_q.declared_votes`; its own evidence (`primitives.py::
   Dossier`) beside `world_q.proofs`; its own standing (`primitives.py::Standing`) beside
   `decision.standing_of`.
2. **Unreached.** `grep -rnE "^\s*(from|import) systems\.social_contest"` over `engine modules tools
   tests` finds four importers, all tests: `engine/tests/test_contest_kernel.py:74`,
   `engine/tests/test_sigma_leverage_parity.py:52`, `tests/valoria/test_band_extension_seam.py:133`,
   `tests/valoria/test_degree_ladder_single_owner.py:143` (run at `601e715`).
3. **Not adoptable as an entry.** Re-measured: `resolve_contest`'s parameters are
   `contest, game, policy_a, policy_b, record` — no generator; one call moves the process-global
   `random` stream (probe: `random.seed(123)`, the next `random.random()` differs after one
   `resolve_contest`); it returns `(('committee', 'win'), bout)`, a winner and not a `Margin`. Each is
   refused by Layer 1 (`04` §C.12 rejection 4; §A.2's wrapper row) and by `sigma.resolve`'s `Margin`
   hold. `roll.py`'s docstring records the same at SC-01 step 15.
4. **SC-05's carried block mis-states the live path.** It schedules *"relocate the veto
   (`degree_extension.py`) as a forwarded `extension=` at `seam/ladder.py`'s degree site"*, with
   *"Hash: none"* and the falsifier *"a planted `tell` contest the old extension demoted: red before
   the move, green after"*. `seam/ladder.py::degree_of` grades a margin as
   `label[ladder(result["settled_margin"], 0)]` (`:262-264`) — no `extension=`, no `pool=`. No live
   contest is demoted by `PoolDesaturation` today, so there is nothing to keep green; forwarding it
   would ADD a demotion to live play and move hashes at pools of 8 and over (`crossover_pool(2.0)`).
   The extension's stated reason (`degree_extension.py:22-25`: `resolver._advance` uses the band as a
   numeric magnitude) is a property of the kernel and dies with it.
5. **Stale registry row.** `references/module_contracts.yaml:464-486` (`module: social_contest`)
   reads `sim_module: systems/social_contest/sim/contest/`, `resolver: dice_pool`, a `persuasion_track`
   state row and the note *"Agon kernel built (1 of 4 games); reached live only via
   emergency_council"*. The provider registers `_RESOLVER = "d10_sigma"` (`sigma.py:110`) and no
   `emergency_council` exists outside that file. `seam/contest.py:285-287` interpolates `resolver` and
   `doc` from this row into a refusal message.
6. **Exported parameters of unexecuted code.** `engine/engine_params/sim_params.json` carries 31
   `social_contest` keys, among them `_kernel_tests.py` constants (`GOLDEN_TRACE`, `GOLDEN_TRACE_SEED`,
   `_N`). A port that binds to them binds to the kernel (CLAUDE.md §5).
7. **The kernel holds the subsystem's only played mode.** `agon_harness.py` is the one place a human
   chooses inside a social contest (`research/game_precedent_suite/dispositions/D_T05.md` row 74 ran
   it: exit 0, nine prompts over three exchanges). Deleting first removes the only standalone play
   surface the standing requirement can point at.

## The resolution, decided (ladder)

- **Step 1, superseded/ruled:** retirement is ruled (`ED-SC-0033` cl. 2); the scheduling call is the
  plan's (A1-58). Nothing here is Jordan's to answer.
- **Step 5, architecture:** delete the directory whole; forward nothing. `dice_engine.BandExtension`
  (the seam, `ED-SC-0032`) stays in its owner with a test double, because the ruling is about HOW a
  system modifies the ladder, not that the contest must.
- **Order:** after SC-P3's `hearing` entry and its play harness are green (so the played mode moves
  before its only host is deleted), and after B10-18c's CR-60 to CR-62 as the plan already orders.

## Exact edits, by owner

1. `git rm -r systems/social_contest/sim/contest/` (re-derive the set from `git ls-files`), and
   `systems/social_contest/sim/__init__.py` if nothing remains beneath it. Write the exact-file
   `FORK:` rows in `references/restructure_ledger.md`.
2. Tests: delete `engine/tests/test_contest_kernel.py` (its subject is gone; `FORK:` row).
   `engine/tests/test_sigma_leverage_parity.py`, `tests/valoria/test_band_extension_seam.py:133` and
   `tests/valoria/test_degree_ladder_single_owner.py:143` replace `CONTEST_DEGREE_EXTENSION` with a
   local `BandExtension` double defined in the test (the seam's contract is what they assert).
3. `references/module_contracts.yaml` `module: social_contest`: `sim_module:
   modules/social_contest/`, `resolver: d10_sigma`, delete the `persuasion_track` state row and the
   `wiring.note`; keep the row (the loop's prize rows key on the name).
4. `engine/engine_params/sim_params.json`: re-derive with `python tools/export_sim_params.py --build`
   after the deletion; never hand-edit. Its `--check` is the gate.
5. `workplans/valoria_master_workplan_v11_part5.md` SC-05: strike "relocate the veto … as a forwarded
   `extension=`", its falsifier and "Lens B: the veto relocation only"; replace the EXIT's `rg` clause
   with item 6 below.
6. `registers/handoffs/HANDOFF_SC.md`: the kernel row closes; `CURRENT.md`'s social contest row names
   `modules/social_contest/` as the head.

## Gate (execution artifact)

- `python -m engine.season.harness.headless --case NPC-088 --seasons 2 --seed 0` and
  `build_realm(0)` one-season content hashes equal before and after (the deletion is unreachable).
- `python tools/export_sim_params.py --check` green; `python tools/freshness_gate.py` green.
- `tests/valoria/test_engine_does_not_import_systems.py` green with the `systems.social_contest`
  fixture re-pointed.

## Falsifier

If any content hash moves, the kernel was reached and finding 2 is wrong: stop and find the importer.
If `test_band_extension_seam.py` cannot be written against a double, the extension seam has no
contract of its own and `BandExtension` should go with the kernel (report, do not decide in the batch).

## What is carried forward, and what is not

Carried (as design input to SC-P3, not as code): the exchange loop's shape, the fault clinch (defeat
by a named fault), the room/verdict split (`VoteAtClose`), the bout chronicle's shapes
(`narrative.py`: ROUT, REVERSAL, COLLAPSE, SPLIT_DECISION) — as a reader of SC-P1's record. Not
carried: the eight-proceeding roster, `Adjudicator` profiles (all `[SEED]`), `Standing`/`Reserve`,
the armature and CR4/CR5 (authored against `.designs/` documents; RATIFIED at Gate C for the kernel,
which is the thing retiring). §11 of the audit lists that last point for Jordan.

## NERS reading

- **N**: the kernel cannot be removed "without worsening the gameplay experience" only if something
  plays it. Nothing in the season does; one harness does, and SC-P3 moves that. After SC-P3 the cut
  loses nothing a season can reach.
- **R**: neutral at runtime; positive for completeness (one roster of proceedings, one obstacle).
- **S**: removes the second ladder for one quantity (two obstacle sites, two bench ballots).
- **E**: 6,700 lines, 389 script checks and 31 exported parameters removed against zero runtime loss.

## Cost class

Small build (deletion wave with registry repoints), cross-lane on `references/`.
