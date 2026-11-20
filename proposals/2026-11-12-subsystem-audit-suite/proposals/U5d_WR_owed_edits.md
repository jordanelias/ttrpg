# U5d-WR — owed edits: the WR resolutions decided with no proposal file

Reconciled: 2026-11-12, wave 3 (W3-3) — R3 §1 found it CONFORMS and R3 §2 found no ruling it contradicts. Added: batches (U3 B12 for §2 (a), §3, §4; §2 (c) in B37, cut edges §4.1 rows 49–50; §1 placed in B12 beside §3 `[ASSUMPTION: U3 places no batch for §1; it is a one-line harness reading]`); §2 (c) names U1 ledger F-42 (one fixture set for illness and age, `22_HAPPENINGS_A`'s; `16_PESSIMIST_WR_C`'s fixtures and its `born` write are withdrawn by the WR rewrite lane of R5, not here); tier (R3 7b-0).

## Status: PROPOSED (a plan for a later implementation lane; nothing here was executed)

Lands in batch: B12 (world motion and ground) for §1, §2 (a), §3, §4, after `16_PESSIMIST_GAME_the_world_draws` (U3 §1 item 13); §2 (c) in B37 (happenings) with `22_HAPPENINGS_A`.
Depends on: `16_PESSIMIST_WR_B` (B12); `22_HAPPENINGS_A` (B37) for §2 (c).

Author: U5d closure lane (Fable), 2026-11-12. Carries `audits/09_WR_audit.md` R-06 (H-257);
`audits/09_WR_audit_addendum_B.md` F-WR-23; `audits/16_PESSIMIST_WR.md` R-4; and the sequencing the
rulings A-15 and A-54 add to WR's files. Land order: §4 (text), §1, §3, §2.

## What it changes in `engine/season/` at runtime

§3: `tend` and a body's recovery write a body Observation, so a believed wound can be cleared. §1 and
§2 change harness readings only. §4 is roster text.

## §1 — a real execution reads as a killing (R-06, H-257)

- **Owner.** `engine/season/harness/strife.py` (`:85`, `readers_for.victim_held`).
- **Edit.** The reader reads the death's `body` change as well as `exists` (one line; the audit's own
  decision). The other half of H-257 (telling an execution from a killing by its lawful basis) is an
  interface need, not built: it waits on SC's verdict naming its party (A-38).
- **Gate.** `python -m engine.season.harness.strife 2 0` on a hand-built execution: the move reads XE.
- **Falsifier.** The same world still reads KL. Movers: none (harness).

## §2 — the order in which WR's draws land (A-54, A-15)

No new edit: an ordering constraint on existing carriers, written so no builder flips a fixed-function
arm. (a) `16_PESSIMIST_WR_B_the_calamity_strains_and_breaks.md` edits 1–2 before `09_WR_world_motion.md`
edit 1's non-zero lattice weight (else the flip is an exponential collapse nobody stops, F-PES-WR-02).
(b) `09_WR_B_draws_not_thresholds.md` edits 1–2 before the weather arm of
`09_WR_B_weather_with_memory_and_the_year.md` (one ladder for wear, hunger and harvest, A-54). (c)
`22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn.md` edit 1 (authored ages) before any non-zero
`illness_rate` or `age_step` (A-15's own condition), with
`16_PESSIMIST_WR_C_illness_on_the_body_ladder.md` as the bout's graded form, reduced to one fixture set,
`22_HAPPENINGS_A`'s (U1 ledger F-42; C3-K4). Gate for each: the
control arm reproduces the base hash before the flip; the flip is one declared re-pin.

## §3 — a believed wound is cleared (F-WR-23; owed at PC's and CHAR's owner)

- **Owner.** `engine/season/loop/` `_eff_tend` and MATTER's recovery write; the reader is
  `queries/world_q.py::wounded_with` (`:3806-3812`, whose docstring states the limit and the fix).
- **Edit.** `_eff_tend` and the recovery step write a `(pid, "body", v)` Observation as `_eff_kill`
  does, carrying the ceiling, so a witness's claim of the wound is superseded by a claim of the mended
  body. Lands before `09_WR_provided_arcs.md` edit 2 and plan CP-T10-04 (each makes bodies rise and
  would otherwise leave stale beliefs and a growing `tend` tax).
- **Gate.** The docstring's measurement re-run (pairs forming `tend` on a healed man: 0, 3, 9 at seeds
  0 to 2 today) reads 0 after a recovery is witnessed.
- **Falsifier.** A `NoOpReceipt` refusal of `tend` on a man a witness saw mended.
- **Movers.** Every run with a `tend`. Declared.

## §4 — one roster sentence (PES-WR R-4)

`engine/season/rosters.yaml:1903-1906` says `restore` executes on the realm; `verb_table.yaml`'s
`restore` row and eight arms read 0. Text for the orchestrator's next WR commit: the sentence reads
"formed nowhere since REM-22". Same reading as `U5d_SE_owed_edits.md` §1 (one decision, two rows).

## NERS (E last)

N: each has no other carrier. R: mended bodies stop drawing care they do not need. S: the draws land in
an order that never ships a fixed outcome. E: one code edit, one harness line, two notes.

## Named tests and call sites (repair R-B; decided from the tree)

- §1: new function `engine/season/tests/test_strife_execution.py::test_a_hand_built_execution_reads_xe`, in the file that already drives `harness/strife.py::readers_for(w).victim_held` over each route's real tenure (`test_strife_execution.py:34-36`, `:175-180`). It plants a lawful execution whose `person.died` Event carries the `body` change, and asserts `victim_held` is true; control: the same Event with only the `exists` change (today's reader) is the failing reading the falsifier names. Call site: `harness/strife.py:85` (`victim_held`), returned by `readers_for` (`:76`).
- §3: new function `engine/season/tests/test_season_shape.py::test_a_witnessed_recovery_clears_a_believed_wound` (the file holds five `wounded_with` mentions; the measurement the docstring at `queries/world_q.py:3806` states is its pair count). Plants a believed wound, runs `_eff_tend` to a recovery, and asserts the pair count of `tend` formed on the healed man reads 0; control: the same world without the Observation write reads the old non-zero count. Call sites: `loop/effects_combat.py:767` (`_eff_tend`) and MATTER's recovery step write the `(pid, "body", v)` Observation as `_eff_kill` does.
- §2 and §4: no test (an ordering constraint; roster text). The hash gate in §2 is the control arm's equality with the base hash, run by the batch's own close.

Reconciled: 2026-11-12, repair lane R-B (`unified/U6_VERDICT_AND_REPAIRS.md` finding 1) — the file named no test for its two code edits (§1, §3); the covering files are named above from `engine/season/tests/` and the sites from `queries/world_q.py:3806-3812` and `harness/strife.py:85`; a function name is a proposal, the file and site are read.

## Cost class

Edits. Tier: `sonnet` (R3 7b-0).
