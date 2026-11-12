# Census (REST) 1 — deletion batches: fields, a dead clock's dependants, a stub with no caller, two phantom contracts

## Status: PROPOSED

Author: Fable census lane, PART=REST. Source: `audits/17_CENSUS_REST.md` §1, §4, §5a, §7, §9. Read at
`4995824` (working tree). Ordered by risk, lowest first. Each batch lands alone with its own test edits.

## What it changes in `engine/season/` at runtime

**Nothing.** Every item is unread, unwritten or uncalled; D1, D2 and D4 move no `World.content_hash()`
(the control for each batch is the same-seed hash before and after: `python tools/m1_acceptance.py
--summary`'s hash row, or `harness/populated.run(3, 0)` → `52ff67bc45c5b956cd99215f6ba3097f` at this
tree, `PYTHONHASHSEED=0`). D3 deletes a module the season never imports.

## The problem

The static census (C2, C6) and the extended passes found declared things with no reader, and one clock
(`Record.ttl`) whose deletion another proposal already decides but whose dependants it does not list.
A field nobody reads is not neutral: `Order.waypoint_ref` (wiring proposal W1) shows what an unread
declaration costs when someone finally uses it.

## D1 — six dead fields (no reader in game code; five have no reader at all)

Cut test for each: delete the field, run the one file named, same-seed hash unchanged.

| # | field | exact edit | test edit | file to run |
|---|---|---|---|---|
| 1 | `RollResult.pool_size` | `engine/dice_engine/dice_engine.py:143` delete the field; `:215` drop `pool_size=effective_pool,` | `tests/valoria/test_dice_engine_properties.py:56-58`: delete the three-line assertion; `:59-61` already asserts `len(result.rolls) == expected_effective`, the same fact | `tests/valoria/test_dice_engine_properties.py` |
| 2 | `Office.body_function` | `engine/season/state/carriers.py:1061` delete the field; `:1091-1092` delete the two-line write; drop `BODY_FUNCTION` from the import at `:34`. **Keep** `data/rosters.py:1324 BODY_FUNCTION` and the `function:` map (`rosters.yaml:2270`) | none (`test_season_shape.py:10017-10020` reads the roster, not the field) | `engine/season/tests/test_season_shape.py -k office` |
| 3 | `Subunit.merged_cells` | `modules/mass_battle/hierarchy/units.py:434` delete the field; `:1121` drop `; self.merged_cells = set()`; `:1149` delete the line; `:1103` drop the name from the docstring list | none | `tests/valoria/test_mass_battle_maneuvers.py` |
| 4 | `ConvictionThresholdState.destabilised` | `systems/characters/sim/conviction.py:165` field; `:249` docstring line; `:255` the local; `:261` the keyword | none | `engine/tests/test_knots_ed912.py` |
| 5 | `ConvictionThresholdState.any_crisis` | same file `:168` field; `:252` docstring line; `:264` the keyword | none | same |
| 6 | `CoMovementCard.card_id` | `systems/threadwork/sim/co_movement.py:65` field; `:128`, `:132` the keyword; keep the tuple unpack at `:124` (the catalogue rows carry the id as their first element; rename the local `_card_id`) | none | `tests/valoria/test_threadwork_mending_parity.py` |

Notes on risk.

- **#1 has one condition.** `10_DICE_one_roller_one_fraction_rule.md` changes how a fractional pool is
  rolled. If that lands first and the dice rolled can differ from the pool asked, `pool_size` then
  carries a fact `len(rolls)` does not, gains a reader in that proposal's receipt, and this row is
  withdrawn. At this tree `pool_size == len(rolls)` by construction (`dice_engine.py:211-215`).
- **#4, #5** trim a retained oracle (ED-IN-0283 keeps the scar model; `02_CHAR_audit.md` §6 row 27).
  The retention is of the model. `scar_counts`, which a test reads, stays.
- **#6** is moot if `09_WR_threadwork_module.md` lands first and rewrites the card record; then the
  rule is the same one stated there: an outcome field with no reader at landing is not carried.
- No `FORK:` row: no file is deleted (CLAUDE.md §1 retires *files*).

**Gate:** each named file green; `python -m engine.season.harness.register --requirements` unchanged;
same-seed hash equal. **Falsifier:** a reader exists that the grep missed; the named test file, or an
`AttributeError` at import, shows it. The greps run are in the audit's evidence log (P-3).

## D2 — `Record.ttl`'s dependants (contingent on `08_FI_04_small-edits.md`, R-24)

`08_FI_04` deletes `Record.ttl` and its `write_matrix.yaml` row. Four things exist only because that row
does, and none is in that proposal's edit list:

| # | dependant | exact edit |
|---|---|---|
| 1 | `rosters.yaml: conditional_emission_rows` (`:1745-1762`), whose one value is `"Record.ttl"` | delete the roster |
| 2 | the exemption branch in the gate, `state/world.py:1337-1346` (`conditional = roster("conditional_emission_rows")` and the `and f"{record_kind}.{fieldname}" not in conditional` clause) | delete the comment block and the clause; the D22 refusal then applies to every MATTER row with a declared kind, which is H-12 as ruled |
| 3 | `record.expired` in `EVENT_KINDS` | nothing to edit: it is derived from the matrix row and leaves with it (`data/verbs.py::derive_event_kinds`) |
| 4 | `harness/probes.py:1815-1822` (the probe that writes `(Record, ttl)`), `loop/matter.py:489` (a comment citing the roster), `tests/test_season_shape.py:4446` (`assert "Record.ttl" in roster("conditional_emission_rows")`) | delete the probe and the assertion; reword the comment to cite H-12 directly |

H-86 (the column's ambiguity) closes as **irrelevant** (ladder step 2: its only instance is retired);
the hole-register row's `cite:` gains the deleting commit.

**Gate:** `engine/season/tests/test_season_shape.py` green; a MATTER write on a declared row with
`emits=None` still raises `Forbidden("… D22")` (`test_season_shape.py:4729-4731` describes the run that refusal stopped; `[UNVERIFIED: the exact test name was not opened]`). **Falsifier:** a
second row needs the exemption; then item 2's deletion fails that row's MATTER write at the first season
of `harness/populated.run(1, 0)`. (Checked statically: `(Site, condition)` declares two kinds and its
writer names one on every write, 966 times in the three-season run.)

## D3 — `engine/substrate/stubwire.py` (contingent on `05_SC_sc05_kernel_disposition_B.md`)

`stub_resolve` has two callers, both in `systems/social_contest/sim/contest/` (`wrapper.py:227`,
`dictionaries.py:48`); that directory is retired whole by SC disposition B. After it, the module has no
caller.

Delete, in the commit that deletes the kernel or the next:

- `engine/substrate/stubwire.py`
- `tests/valoria/test_stubwire.py`
- the name in `engine/substrate/__init__.py:6`'s docstring list
- `skills/valoria-vector-audit/scripts/structure_audit.py:199-201, 381-385, 851-855`: the `stub_wired`
  report section, which lists importers of a module that no longer exists
- `modules/social_contest/roll.py:34`: the parenthesis naming `engine/substrate/stubwire.py`

`FORK:` rows (the ref is the parent of the deleting commit; `references/restructure_ledger.md`, exact
file rows, CLAUDE.md §1):

```
| `engine/substrate/stubwire.py` | `FORK:<parent sha>` | FORKED (<date>, retired with its only caller, `systems/social_contest/sim/contest/` (ED-SC-0033 clause 2); ED-IN-0093's self-flagging stub has no stub left to flag) |
| `tests/valoria/test_stubwire.py` | `FORK:<parent sha>` | FORKED (<date>, retired with `engine/substrate/stubwire.py`) |
```

**Gate:** `test_importing_every_engine_module_pulls_in_no_subsystem` green;
`grep -rn stubwire engine modules systems tools skills tests` → the ledger rows only.
**Falsifier:** a module added between now and then that returns a `StubResult`; the grep shows it.

## D4 — two phantom contract rows in `references/module_contracts.yaml`

`settlement_economy` (`:677-690`) and `campaign_architecture` (`:952-959`): `sim_module: none`,
`wiring.godot: retire`, `port_rank: 9`; their own notes read "phantom (in-3/out-0); ED-SE-0005 folds it
into settlement_layer" and "reclassified: a consolidation doc, not a runtime module".

- Delete both rows. Edit the head comment at `:27` (`status: EXTRACTED_STAGE1   # campaign_architecture
  stub remains`) to drop the trailing comment. `references/canonical_sources.yaml:108`'s
  `campaign_architecture` entry points at the quarantined document, not at this row, and stays.
- The other 16 code-less rows stay: each declares itself code-less (`sim_module: none`,
  `wiring.build: design|deferred`) and is the design ledger the IN → resolver → OUT reading uses
  (CLAUDE.md §9). Their stale narration is accepted and nothing is written (§0.1 pt 5).

**Gate:** `python tools/export_composition.py --check` → `OK — 16 role(s) … wiring valid for 24
module(s)` (26 today); `python tools/ci_quantity_vocabulary_check.py` unchanged in verdict.
**Falsifier:** a `with:` join or a `transitions:` row in a surviving contract names either module;
`grep -n "settlement_economy\|campaign_architecture" references/module_contracts.yaml` after the edit
shows it (before: the two rows, the `:27` comment and one history note at `:783`).

## Deleted by other proposals, listed so no lane double-counts

| what | rows | deleting proposal |
|---|---|---|
| 28 C2 fields in `systems/social_contest/sim/contest/` | audit §1c | `05_SC_sc05_kernel_disposition_B.md` |
| `Record.ttl`, its matrix row | audit §5a, §7 | `08_FI_04_small-edits.md` |

## NERS reading

N: each item fails the cut test in every direction tried (top-down: no requirement or case names it;
bottom-up: no reader; lateral: no sibling module; across scales: not on any typed input or outcome that
is read). R: nothing a player or an NPC can do changes. S: D2 removes a second ladder for one question
(when does a write expire: `stages`/`matured` is the one clock after it). E, last: six fields, one
roster, one gate branch, one module, two contract rows; no behaviour lost.

## Cost class

Edit, all four batches. D1 and D4 can land today; D2 and D3 wait for the proposals named.
