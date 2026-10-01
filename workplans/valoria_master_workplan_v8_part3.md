# Valoria — Master Workplan v8, part 3: orchestration · the pre-flight · Batch 0 (remainder) · Batch 1 (landed)

## Status: PROPOSED 2026-10-01 — directed by Jordan; adoption on merge (ED-1094). Same status and held-back list as `valoria_master_workplan_v8.md`; this part carries no decision of its own.
## Reads after `workplans/valoria_master_workplan_v8_part2.md`. Owns THE ORDER: the batches, the serial edges, the file census, and the spec of Batch 0's remainder (Batch 1 landed: `## B1`).
## Grade under `CLAUDE.md` §0.2: `paper`. Line numbers drift; re-derive every site by its symbol (`CLAUDE.md` §0.1 pt 3).

---

## O. ORCHESTRATION

### O.1 The batches, in dependency order

| batch | items, in serial order (`{…}` = a parallel lane in its own worktree) | R-rows moved | golden / hash moves (declare each) | close |
|---|---|---|---|---|
| **0** | **LANDED** — `B0-CI` for `tests/valoria` (PR #450), `B0-CI-b` (PR #451); what remains is `unit-tests` reading green on `main` once #451 merges | — (CI green on `main`) | `B0-CI-b`: moved, declared (`_part6` §H.1) | `/code-review` only; no terminal critique (a seat/commit data fix whose own test is the falsifier) |
| **1** | **LANDED (PR #450); records in `_part6` §H.** Its tail, `29d-ii` and `20-v`, landed in PR #451 (`_part6` §H.1) | — | — | — |
| **2** | **open — the telling workplan's Batch 2 closed and merged (PR #449, `fd321c81`; main §0.6)**. IN: `11-fix` → `11` (baseline) → `8` → `ED-FI-0009` → `14` (+ `R05-THREAD`) → `17` → `13`-rest → `13d-iii` → `11` (re-take) → `21`-rest; `{WR: 27}`; `{MB/PC: LADDER-MBPC}` (`_part5` §J, "not on the queue") | R-01, R-02 (measured), R-04, R-05, R-06 (reason 1), R-07, R-09 | `8`: none (assert equal); `ED-FI-0009`, `14`, `17`, `13`-rest: corpus/realm pins move (declared per step); `13d-iii`: `build_realm` census + hash (declared) | full `methodology-close`; terminal critique **proportionate** — `14` is a judgment node and `11` is a number nobody else reproduces |
| **3** | SC: `22` steps 11–16 → `22a` → `23` → `22b`; IN: `29f` → `29e` → `29a`-ms → `2-ii`; `{SE: 24h P5}`; `24h` P6 after `22`'s `verb_table.yaml` edits | R-05 (`speak`, `determine`), R-09 (a fourth graded chain), M2 (THE BAR) | `22`: corpus + realm hash move (declared); `2-ii`: none (byte-identity control) | full `methodology-close`; terminal critique **proportionate** — `22` is the largest new mechanism in the plan |
| **4** | one sub-batch per Jordan ruling, as each lands: cells commit (J-1) → H7 → H3 → H9 → `12` → H10 (C3) → H11 (C4) → `12e`; `19b` (J-2); J-3's verbs; `9` (J-7); `24g` (J-6); `24h` P7 (J-10); `26` (J-9) | R-05, R-06, R-08; R-04 (J-3) | cells commit: headless + corpus hash move, `resolvable_verbs()` count moves (declared) | cells commit: full pipeline, terminal critique **proportionate**; `24g`, `26`, `24h` P7: `/code-review` + `/simplify` only — one value or one record each |

**Why this order.** Batch 1 ran first because it was gate-free and purely subtractive: every later batch
touches less code now the spine is gone. Batch 2's IN chain is serial because five of its positions
share `rosters.yaml`/`verb_table.yaml`/`test_season_shape.py` (O.3). `11` runs **twice** in Batch 2 —
once on HEAD after `11-fix` (the baseline the row needs today), once after the verb set has moved — so
the second number has a control taken by the same instrument on a declared earlier tree. Batch 3 waits
on Batch 2 because `22`'s `determine` needs `13d-iii`'s rung purview, and `24h` P6 / `29f` need `14`.
Batch 4 opens only on rulings.

### O.2 Hard serial edges (live ones only)

Carried from the retired 2026-09-18 plan (§3.9) and 2026-09-28 plan (§3.5); edges both of whose ends
are finished are spent and omitted (`_part6` §H lists them). `isolation: worktree` defers an edge to
the merge; it never removes it.

| # | edge | why | origin |
|---|---|---|---|
| E2 | `27` → `29a`-ms; `27` → `29f` | `threadwork/sim/{co_movement,opposing}.py` import `ms_track.apply_ms_delta` and `knots.sustain_knot` | 09-28 §3.5.2 |
| E3 | `14` → `29f` → `29e` | the `tie / knot` effect first; then `conviction.py` ← `knots.py` | 09-28 §3.5.3 |
| E4 | `22` → `2-ii` | the prize-row repoint | 09-28 §3.5.4 |
| E5 | the cells commit ↔ `8`, `9` | same `fight` row and combat wrapper. Either order; never interleaved | 09-18 §3.9.10 |
| E7 | `8` → `ED-FI-0009` | both edit `seam/ladder.py` | new |
| E8 | `8` → `ED-FI-0009` → `14` → `17` → `13d-iii` | shared `rosters.yaml`, `verb_table.yaml`, `engine/season/tests/test_season_shape.py` pins | new |
| E9 | `14` → `24h` P6 | the `repudiate` row and its effect | new |
| E10 | `11-fix` → `11` → `21`-rest | the instrument, then the number, then the records quoting it | new |
| E11 | `13d-iii` → `22` steps 11–12 | `determine`'s bench is a purview read; rungless seats make it empty | new |
| E14 | telling T4 → `14` | `14`'s distinct-operand fix builds on T4's `operand_bags` / counterparty target; both edit `decision/options.py` and `verb_table.yaml` | carve-out (main §0.6) |
| E15 | `11` baseline ∉ (telling T3a … T6); `11` re-take after both Batch 2s | T3a–T5 move the claim channel `11` measures; a baseline taken across them has no control | carve-out |
| E16 | telling T6 → the AX-7 wiring (reopen only then) | same Claim producers and reader | carve-out |
| E13 | every position → its own forward sweep's `requirements.yaml` / `hole_register.yaml` edits | the shared record files; never edited from two worktrees at once | §0.4 |

### O.3 File census — open positions × shared files

| file | edited by | consequence |
|---|---|---|
| `engine/season/verb_table.yaml` | telling T4 (`tell` row), `14`, `R05-THREAD`, `ED-FI-0009`, `22` (`speak`, `determine`), `24h` P6, `19b`, cells commit | serial in the IN/SC chains (E8, E9) |
| `engine/season/rosters.yaml` | telling T4 (`known_person_operands`), `8`, `14`, `13d-iii` (`titles` block deleted), `22` (prize rows, `chronicle`), cells commit | serial (E8) |
| `engine/season/seam/ladder.py` | `8`, `ED-FI-0009`, `2-ii` (veto `extension=`) | E7; `2-ii` is Batch 3 |
| `engine/season/loop/effects_combat.py` | cells commit | E5 |
| `engine/season/loop/effects_information.py` | `14`, `ED-FI-0009`, `22` | serial |
| `engine/season/loop/effects_governance.py` | `14` | — |
| `engine/season/decision/options.py` | telling T1, T3a, T4; then `14` | E14 |
| `engine/season/queries/person_q.py` | telling T1, T2, T3a, T6, G1; then `17`, cells commit | carve-out first; Batch 2 vs 4 |
| `engine/season/queries/world_q.py` | telling T4 (`with`), `24h` P5 | the carve-out vs Batch 3; never interleaved |
| `engine/season/harness/populated.py` | `13d-iii` | — |
| `engine/season/harness/corpus_run.py` | `17` | — |
| `engine/season/cases/exercises/*.yaml` | `13`-rest | parallel authoring; merges after `17` |
| `engine/season/offices.yaml` | `13d-iii` | — |
| `engine/season/tests/test_season_shape.py` | telling T2, T4; then `8`, `14`, `17`, `13`-rest, `22` | every pin re-taken serially |
| `loop/witness.py`, `state/carriers.py`, `data/verbs.py`, `data/requires.py`, `loop/resolve.py`, `engine/season/tests/test_told_by_channel.py` | the telling workplan only | no v8 position edits them while a telling position is open |
| `engine/season/requirements.yaml`, `engine/season/hole_register.yaml` | every forward sweep; `11`, `21`-rest | E13 |
| `references/restructure_ledger.md` | `29a`-ms, `29e`, `29f`, `2-ii` | serial; appended rows conflict at the file end |
| `.github/workflows/valoria-ci.yml` | `2-ii` (the job folds) | — |
| `tests/valoria/test_engine_does_not_import_systems.py` | `2-ii` | E4 |
| `systems/threadwork/sim/*` | `27`, `29a`-ms (import site), `29f` (import site) | E2 |

**Parallel lanes this census permits:** Batch 2 `{WR: 27}` (only `systems/threadwork/` and
`tests/valoria/test_coherence_elastic_plastic.py`) and `{MB/PC: LADDER-MBPC}` (only
`registers/editorial_ledger_{mb,pc}.jsonl`); Batch 3 `{SE: 24h P5}` (`queries/world_q.py` or
`faction_q.py`, read-only Query). Nothing else runs in parallel. Fable proposed FI `ED-FI-0009` as a
parallel lane; it shares `verb_table.yaml` and `effects_information.py` with `14`, so it is serial
here (a departure, recorded in the receipt).

### O.4 The run discipline every batch uses

- **Driver:** `methodology-execute` (`CLAUDE.md` §9): `valoria-author` builds and commits each
  position cheaply; `methodology-close`'s pipeline (agonist/antagonist → `/code-review` → `/simplify`
  → `layer-conformance` → terminal Opus critique where O.1 says proportionate) and the pytest suite run
  **once per batch**. The per-step cadence (main file §0.4) runs inside each step, minus the suite.
- **Share the reading** (`CLAUDE.md` §10): one Haiku `valoria-measure` extract per batch, from the
  batch's reading list, handed to every producer. Fire one producer, await its first token, then fan
  out.
- **Receipt (fixed, every producer):** `POSITION <handle> | COMMIT <sha> | FILES <paths> | RAN
  <commands, exit codes> | FALSIFIER <test::name → pass/fail> | HASH <unchanged | moved old→new,
  declared> | HOLES <H-ids touched> | NOT DONE <named remainders>`.
- **Commit shape:** `[scope] <≤72-char subject naming the handle>`; body cites `PP`/`ED`; scopes per
  `CLAUDE.md` §2. Ids from `references/id_reservations.yaml` `next_free` at allocation time, never
  max+1.
- **Tiers:** `haiku` extraction and measurement; `sonnet` bounded builds, deletions, re-hosts; `opus`
  judgment nodes (verify, critique, any effect body with a design choice). Per step below.
- **Stopping rule:** main file §0.5. Revert and register; never widen.

---

## P. PRE-FLIGHT — the checks Fable could not settle read-only

**Settled 2026-10-01 while writing this plan** (no re-run needed unless the tree moves):

| # | check | outcome |
|---|---|---|
| S-1 | `cat .git/shallow` | full clone in the writing container; re-check in yours |
| S-2 | `register --requirements`; `m1_acceptance --summary` | met 1 · partial 5 · not_met 3; M1 NOT MET, row 3 FAIL 1/9 [RAN, 29 s] |
| S-3 | `python -m pytest engine/season/tests -q -k we_only_a_verb_that_declares_contests_can_be_graded_today` (Fable's suspected known-red) | **1 passed** — not red; no Batch-0 fix for it |
| S-4 | `gh run list --branch main --limit 3` + `gh run view 36803379833 --log-failed` | `unit-tests` FAILS on `main` (7 tests) — the `B0-CI` row |
| S-5 | `ls systems/social_contest/sim/contest` | present, 16 files — `2-ii` still has its subject |
| S-6 | `grep -n "GD-1\|victory" engine/season/hole_register.yaml` | nothing — GD-1 was not registered; `28-iii` registered it as `H-176` |
| S-7 | `grep -rn "def ambitions\|def stance_delta" engine/season` | nothing — `17` is unbuilt; `stance_delta` is built nowhere, by design (the telling workplan computes regard at read, main §0.6) |
| S-8 | invariant 4's per-conjunct `emits_on_refusal` schema | **built at `19`**: `data/verbs.py` reads a clause-keyed mapping into `refusals_by_clause`; `engine/season/tests/test_u7_remit.py` asserts it. `23`'s "invariant 4 widened" reduces to whatever row still uses the flat form where a conjunct is failable — re-check there |
| S-9 | `references/module_contracts.yaml` `composition_roles` | **25 keys** when written (Fable read 26): 1 survivor (`mass_battle.resolve_field`), 7 spine role rows, 10 `snapshot_state.*`, `world_gen_settlements`, 3 `parliamentary_*`, 3 orphans (`rs_track_delta`, `territory_transfer_candidate/proposal`). Read after Batch 1: exactly 1 key, the survivor |
| S-10 | `write_matrix.yaml` `(Person, stance)` | `steps: [RES, ENC]`, `class: ACTS`, `social: "true"` — the row the telling workplan's spine honours: `tell` writes no stance (main §0.6) |

**Consumed in Batch 1 (PR #450) — results only:**

| # | what it decided | result |
|---|---|---|
| P-1 | `28-iii`'s baseline: which `engine/tests` pass before deletion | `engine/tests` 967 passed before `28-iii` |
| P-2 | `ALLOWED_IMPORTERS` and `NESTED_BASELINE` before `28-iii` | 21 passed (`test_mc_v18_is_deprecated.py`, `test_engine_does_not_import_systems.py`) |
| P-3 | the composition export round-trips before `28-iii` edits it | `export_composition --check` OK |
| P-5 | why ENCOUNTER refuses all 11 realm marches | H-149's target-kind check refuses all 11 (a ruling, not a missing defender or `_survives`); recorded in H-149's `cite:` |
| P-7 | `28-i`'s successor instrument runs before `28-iii` deletes the oracle it replaced | `python -m engine.season.harness.arms` ran end to end; both arms identical |
| P-8 | the container's known-red set | `tests/valoria` 1789 passed, 0 failed, at the sub-batch 1a close |

**Still open — Batch 2's; run these first, record outputs in the first receipt that needs them:**

| # | command | what it decides |
|---|---|---|
| P-4 | `cd proposals/2026-09-04-degree-sweep && python wd_chunk.py none default 0 36 && python wd_chunk.py none default 0 36` (same cell twice) | `11-fix`'s determinism attack: if `probed` differs between two runs of the SAME arm, the break is a determinism defect, not a property — stop and register |
| P-6 | for one `corpus_run` case, list the `questions_for` referents offered to a seated person, and compare with `build_realm(0)` (H-175) | why the 143 cases never give `march` a referent — a measurement for R-04's table, not a build |

---

## B0. BATCH 0 — LANDED (PR #450, PR #451)

`B0-CI` landed for `tests/valoria` in PR #450 and `B0-CI-b` in PR #451; records are `_part6` §H.1. What
remains is observational: `unit-tests` should read green on `main` once #451 merges (`gh run list --branch main`).
A red `main` hides every later regression, so read it before the next batch merges.

---

## B1. BATCH 1 — LANDED (PR #450)

Records are `_part6` §H.1, one line per position, each with its evidence; the batch's dispositions
(which season-native code replaced which deleted file) are `_part6` §D, rows marked DONE. Two follow-ups
Batch 1 found, `29d-ii` and `20-v`, landed in PR #451.

**The control Batch 1 used is the pattern for any later deletion batch:** record `build_realm(0)`'s
one-season `World.content_hash()` before the first deletion and reproduce it exactly after every deletion
commit — a move is a failure, not a re-pin — and check the deletion with an `ast` walk over every tracked
`.py` for imports of the deleted modules (before: some; after: none). The cost Batch 1 accepted stands:
deleting `mc_v18` removed the last campaign-scale regression oracle, and `CLAUDE.md` §7 records that gap as
open.
