# CENSUS C1B · corrections: one mislabelled row, and the text that rides on the deletions

Reconciled: 2026-11-12, wave 3 lane W3-5b (`unified/work/R5_READ.md` §1 row C1B_03 CONFORMS, §7 COMPLETE but for the tier; `unified/U3_DEPENDENCY_ORDER.md` §1 item 4, §3.1; `unified/U5_CONFLICTS_U5a.md` C-U5a-17). Changed: C-6 is marked carried (`09_WR_threadwork_module.md`'s head now reads its edit 2 as this sentence states); the batch and tier lines. Nothing else.

Depends on: `17_CENSUS_C1B_01_deletions.md` (B03; C-2 to C-5 ride its batches' commits).
Lands in batch: B03 (lane IN): C-1 alone, C-2 with D2a, C-3 with D1, C-4 and C-5 with D3.
Tier: sonnet / high.

## Status: PROPOSED

Carries `audits/17_CENSUS_C1B.md` §3.3 and §4 (X-4). Exact text, old and new. Only C-1 stands alone;
C-2 to C-5 land in the commit of the deletion batch each names (`17_CENSUS_C1B_01_deletions.md`), and
C-6 is an edit to another lane's proposal, listed for the unification stage.

## What it changes in `engine/season/` at runtime

**Nothing.** Comments, docstrings, two register rows and one proposal sentence.

## C-1 · `systems/combat/combat_engine_v1/capabilities.py:24-30` (`_affords_point`) — stands alone

The docstring names a module `systems` three times. The code under it imports `combat_systems`
(`:31`, `import combat_systems as S`), which lives in `modules/combat/` since plan position `31b`.

| old | new |
|---|---|
| `Local import (systems.py sits above this module in the dependency order` | `Local import (combat_systems.py sits above this module in the dependency order` |
| `the weapon's DERIVED afforded-heads set (systems.afforded_heads` | `the weapon's DERIVED afforded-heads set (combat_systems.afforded_heads` |
| `and systems.select_mode already lets it SELECT that spike` | `and combat_systems.select_mode already lets it SELECT that spike` |

The module docstring's phrase it quotes, "pure data; no systems/core at module scope", is left as
quoted (`:20` reads the same); changing one and not the other would make the quotation false.

## C-2 · `modules/mass_battle/hierarchy/units.py:137` — rides D2a

| old | new |
|---|---|
| `generous, non-facing-gated outer bound (see _effective_reach)` | `generous, non-facing-gated outer bound (the facing-gated test is geometry.reach_reaches)` |

## C-3 · `systems/characters/sim/conviction.py:22` and the lines it runs to — rides D1

Delete the paragraph that begins `[ASSUMPTION: cycle resolution — beliefs.revise_belief calls into`.
There is no `beliefs` module in the tree (`git ls-files | grep -c 'beliefs\.py'` is 0), and D1 deletes
the one function the paragraph describes a caller for. Nothing replaces it.

## C-4 · `systems/threadwork/sim/__init__.py:11`, `:13` — rides D3

Delete the two lines

```
  - co_movement: Co-Movement Version C + 15 cards (Part 4)
  - threadcut: Threadcut beings (Part 6)
```

## C-5 · `registers/mechanics_index.yaml`, rows `co_movement` (`:467`) and `threadcut_beings` (`:485`) — rides D3

| old | new |
|---|---|
| `sim_module: systems/threadwork/sim/co_movement.py` | `sim_module: null` |
| `sim_module: systems/threadwork/sim/threadcut.py` | `sim_module: null` |

`test_status: not_implemented` stays and is now true of both. The rows' `canon_sources:` name a
retired path, as most rows of that file do; that pattern is not corrected here (audit X-4b).

Two further pointers to `co_movement.py` go stale with D3 and are corrected in its commit:

| where | old | new |
|---|---|---|
| `engine/season/hole_register.yaml:6110` (H-326, inside `hole:`) | ``the Church-attention pool in `systems/threadwork/sim/co_movement.py`, not read by the season loop`` | ``the Church-attention pool, drafted only in the retired `systems/threadwork/sim/co_movement.py` (`FORK:` row) and never read by the season loop`` |
| `systems/threadwork/sim/operations.py:212` (comment) | ``struck at position 27 in co_movement.py and opposing.py alike`` | ``struck at position 27 in opposing.py`` |

`registers/handoffs/HANDOFF_IN_history.md:1481` also names `co_movement.py`; it is a history file and
stays as written.

## C-6 · `proposals/09_WR_threadwork_module.md`, edit 2 — for the unification stage (U3)

| old | new |
|---|---|
| `` `_practitioner_state`, `_store`, `reset_all` and their siblings in `threadcut.py` and `co_movement.py` are deleted. `collective.py` and `opposing.py` take `tuple[Practitioner, ...]`. `` | `` `_practitioner_state`, `_store` and `reset_all` are deleted. `threadcut.py` and `co_movement.py` are deleted whole before the move (`17_CENSUS_C1B_01_deletions.md` D3: every function in them reads or writes a module store). `collective.py` and `opposing.py` take `tuple[Practitioner, ...]` and are called by `work` through `WorkingInput.helpers` and `WorkingInput.opposed_by` (`17_CENSUS_C1B_02_wires.md` W-3), so they have a caller on the day they move. `` |

A `Reconciled:` line at that proposal's head, per `UNIFICATION_BRIEF.md`'s rule, is the unification
lane's to add; this lane edits only its own files. **Carried:** `09_WR_threadwork_module.md`'s head
(C-U5a-17) reads its edit 2 as amended by this sentence; nothing further is owed here.

## What is deliberately not corrected

- **`[canonical: params/*.md …]`, `[canonical: designs/… ]` and `audit/2026-…` tags in code comments**
  (about 250 lines across 40 files of this lane). Retired paths resolve through
  `references/restructure_ledger.md` by the tree's convention; a comment is reference, not mechanism
  (§0.05); and a pattern in a process-only artifact earns neither a sweep nor a guard (§0.1 pt 5).
- **`registers/mechanics_index.yaml` `canon_sources:` file-wide** (audit X-4b), for the same reason.
- **`references/module_contracts.yaml:114`** (`mass_battle.army_preset`, "shipped off: nothing in the
  season loop calls it"): true today. It becomes false when `04_MB_playable_field_scenario.md` lands,
  and that proposal's commit owns the sentence.

## Gate

`python tools/valoria_local.py --staged` on each commit (cheap, no pytest). For C-5,
`python tools/mechanics_index_gen.py` reports no new warning for the two rows (a `null` `sim_module`
is a declaration there, not a violation: `mechanics_index_gen.py:233`).

## Falsifier

After C-1, `grep -n "systems\.\(afforded_heads\|select_mode\)\|systems\.py" systems/combat/combat_engine_v1/capabilities.py`
returns only the quoted phrase at `:20` and `:25`. After C-4 and C-5,
`grep -rn "threadcut\.py\|co_movement\.py" engine modules systems registers references tests tools`
returns only the two `FORK:` rows, the reworded H-326 sentence and the history line named above.

## NERS reading

Reference text only: nothing here is a design object, so no criterion is scored. The test that
applies is §0.05's: if these lines were deleted the game would behave the same, so they are reference,
and reference that names things which do not exist misleads the next reader.

## Cost class

Edit.
