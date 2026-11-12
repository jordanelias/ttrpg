# 18 · DETERMINISM · A — every consequential verb draws: the uncontested fold becomes bookkeeping only

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-07, C-U5a-10, C-U5a-13) — three changes. (1) Item 3 and the gate follow `16_PESSIMIST_DICE_task_difficulty_and_throughput.md`: a task nobody has ranked is `plain`; the route never ships on `obstacle_default`; gate item 5. (2) Item 4 is rewritten to `04` §B.13 invariant 12 and §C.4 (a `Degree`-keyed column belongs to a verb that declares `contests:`): a `task` row keeps flat `writes:` and `emits:`, scales its magnitude by `task_fraction`, and carries its failed draw as the keyed `emits_on_refusal` clause `draw`, which is the form the three graded inquiries already have; a verb whose bands write different cells declares `contests:`. (3) The roll is the one sampler (A-5); the pool is the one pool rule (U1 architecture §4), at the uses-table site `task`.

Reconciled: 2026-11-12, wave 3 lane W3-5b (`unified/OWED_TO_UNIFICATION.md` §B "item 2 contradicts item 4"; `unified/work/R5_READ.md` §1 row task_draw (AMBIGUOUS, three readings), §2 rows item 2 vs 4, item 3, A-81, §7, 7b; `unified/U3_CONFLICT_LEDGER.md` §9 cross-cutting (item 4 decides, C-22), C3-R1, C3-D3, C3-C2, C3-N27; `U5c_VERBS_residue_and_governance_owner.md` §1 (shapes (a), (b), inquiry); `unified/U1_OWNERS_AND_VOCABULARY.md` D-U1-04, D-U1-07, D-U1-09, D-U1-11i, -11j, -11l; U1 capability site `task`; `unified/U3_DEPENDENCY_ORDER.md` §1 item 8). Changed: (1) item 2's loader text, which still described the pre-C-U5a-10 shape ("a routed row's `writes:` is degree-keyed"), is replaced by item 4's: only the second refusal (`data/verbs.py:872-876`) is edited, by a `form: inquiry | task` field on each route row; the first (`:848-851`) is invariant 12 and stays, because a row whose bands write different cells declares `contests: "a task"` (shape (b)) and passes it unedited. U3's C3-R1 and §1 item 8 say "the two loader refusals edited"; at the tree (`data/verbs.py:848-851` read here) the first needs no edit once shape (b) declares `contests:`, so that wording is corrected here; (2) item 3 gains the stand-in clause for a task with nobody opposite and takes the pool from the `task` site (U1), not `verb_capability`; (3) item 4 names A-81 and the durable write of a Failure; (4) the draws use the one `Draw` owner (C3-D3); (5) gate 1 no longer cites a scratch probe: it is a named test; tests, failure kinds and the roster row shape are named; the control pins carry C3-N27's note; (6) batch and tier lines. A lost task draw keeps the clause name `draw` and its `emits_note` says it is a loss, not a refusal (04 §C.4 `:727-728`; R5 §1 reading (2)), so the refusal-rate readings count it as a loss.

Depends on: `13_SC_tuning_tables.md` T1 and OBS §4 step 1a (B05: the `difficulty:` column, D-U1-04); `16_PESSIMIST_DICE_task_difficulty_and_throughput.md` (B05 code part; its text amendments land here, U3 §4.1 row 19); U1's capability block (B04: the `task` site); the one sampler (B05) and the keyed draw `engine/dice_engine/draw.py` (B06, C3-D3).
Lands in batch: B07 (lane IN; one re-pin), first item of the batch; `U5c_VERBS_residue_and_governance_owner.md` §1-§2, `U5b_VERBS_military_physical_residue.md` §1 and `13_SC_draw_for_unrolled_contests.md` follow it in B07. Every verb proposal whose rows rely on a route or a task contest names this file as its dependency (C3-R1).
Tier: opus for the loader and roster design (the Layer 1 reading, taken above); sonnet / high for the 22 rows, the effects and the tests.

## Status: PROPOSED

Grounded: 2026-11-12 by `audits/25_GROUNDING_ENGINE.md` (G-01, L-10) — step 2 names the two loader refusals (`data/verbs.py:848-851`, `:872-876`) that today refuse a routed row that writes (only the second is edited: see the wave 3 line above); step 3's pool reader is `seam/wrappers/pool.py::faculty`. The resolution is unchanged.

Source: `audits/18_DETERMINISM_SWEEP.md` C-01, C-03, C-05, C-08, C-09, C-15 (and D-05, D-10). Standing
rule: `AUDIT_BRIEF.md` (Jordan, 2026-11-12, *"we do not do deterministic"*). Reference only (CLAUDE.md
§0.05); not ratified by being written.

## What it changes in `engine/season/` at runtime (first)

Every act of a verb that writes or finds something a person in the fiction could see go otherwise now
rolls once through the route `research` already takes, and folds at the band it gets. In the realm
that is about 727 outcomes in five seasons over three seeds that today take effect on eligibility
alone (`reconstruct`, `tend`, `forge`, `conceal`, `issue`, `move`, `survey`, `open_case`, `interview`,
`migrate`, `carry`, `requisition`, `thread_read`, `release`), plus every act of the rows refused today
once they are admitted (`train`, `sabotage`, `raze`, `seize`, `found`, `build`, `confer`, `pardon`,
`establish`). Pure bookkeeping (writing one's own record, uttering, committing oneself, scheduling,
moving one's own stores) is declared and stays draw-free. A hash mover for every world in which any
converted verb executes: every realm and case golden.

## The problem (evidence)

- `engine/season/loop/resolve.py:1079-1111`: an act goes to the seam only if its row has `contests:`
  or a `graded_inquiries` route; otherwise `_fold(w, token, a)` runs with `resolution=None`, and
  `_fold`'s own docstring says that is *"every uncontested act, which is every act the corpus
  produces"*: the effect applies once `_admits` passes.
- 53 of the 67 verb rows take that path (11 contested, 3 graded): `…/scratchpad/runs/DET/verbs.txt`.
- Realm probe (`…/scratchpad/det_probe.py`; seeds 0 ×1 season, 1 and 2 ×2 seasons; 3,826 resolved
  acts): 2,159 success events, of which 1,995 carry no degree (92 %). Per verb, success events without a
  draw: `reconstruct` 244, `tend` 118, `forge` 90, `conceal` 72, `issue` 49, `move` 45, `survey` 32,
  `open_case` 23, `interview` 18, `migrate` 13, `carry` 8, `requisition` 6, `thread_read` 5,
  `release` 4 (plus bookkeeping: `create_record` 645, `utter` 350, `commit` 142, …).
- `_eff_tend` (`loop/effects_combat.py:767-790`) restores a body to its ceiling; `_eff_forge` mints every
  forgery at `Fixtures.default_forgery_quality`; `_seize_rung` *"asks nothing of the defenders"*;
  `_eff_succeed`: *"the first valid claim wins"*.

## The resolution, decided

Ladder step 4 (precedent: `research`, `examine`, `surveil` already roll through `graded_inquiries` →
`seam.grade` → `social_contest.roll` → `degree_of` → `_fold(…, Resolution)`) and step 5 (one route, one
roller, one loader refusal; no second resolver).

1. **Three resolution classes, one per writing row, derived — not a new column.** `contest` = the row
   has `contests:`; `task` = the row has a route in the roster below; `bookkeeping` = the row is a
   member of a new closed roster `bookkeeping_verbs`, each with a `why:` line. A row that writes or
   emits a finding and is in none of the three is **refused by the verb loader** (`data/verbs.py`),
   naming the verb. The loader also refuses a `bookkeeping` row whose `writes:` touch `Person.body`,
   `Person.capability`, `Person.exists`, `Person.body_ceiling`, a seat-`hold` Tenure, a Tenure whose
   holder is not the actor, or `Rung.stores` of a rung the actor does not hold, or whose `emits:`
   include `finding.made`. This is the loader's refusal per data family (CLAUDE.md §0.05), not a
   tree-wide guard.
2. **The route roster is renamed for what it now holds.** `rosters.yaml: graded_inquiries` →
   `graded_tasks` (`GRADED_INQUIRIES` → `GRADED_TASKS` in `data/rosters.py`, its three readers updated);
   its three rows carried unchanged; `check_graded_inquiries` → `check_graded_tasks`, same three
   refusals. Every `task` row is `{provider: "social_contest", module_entry: "social_contest.roll"}`,
   the pair a prize row already binds, so **no roll and no resolver is added** (the provider's name is
   historical; the roll is the generic pool-against-obstacle draw, `engine/dice_engine` underneath).
   **One loader refusal is edited in the same commit, or no converted route row loads** (grounded,
   `audits/25_GROUNDING_ENGINE.md` G-01; the shapes of `U5c_VERBS_residue_and_governance_owner.md` §1).
   Each `graded_tasks` row carries `form: inquiry | task`. The second refusal (`data/verbs.py:872-876`,
   `if _graded and (not emits_by_degree or row.writes): raise SystemExit`) becomes: a `form: inquiry`
   row (`research`, `examine`, `surveil`, carried unchanged) keys `emits:` by Degree and writes nothing,
   as today; a `form: task` row may carry a flat non-empty `writes:` and a flat `emits:`, must declare
   `emits_on_refusal` keyed with the clause `draw`, and must not declare `contests:` (a route row with a
   Degree-keyed `writes:` or `emits:` is refused, naming the verb). The first refusal
   (`data/verbs.py:848-851`, a Degree-keyed `writes:` with no `contests:`) is **not edited**: it is
   `04` §B.13 invariant 12 (`:504-506`), and a verb whose bands write different cells declares
   `contests: "a task"` (shape (b), VRES §1) and passes it as it stands. Roster row shape:
   `graded_tasks: {tend: {provider: social_contest, module_entry: social_contest.roll, form: task},
   research: {provider: social_contest, module_entry: social_contest.roll, form: inquiry}, ...}` (the 22
   `task` rows of item 5, the 3 inquiry rows unchanged). The name `graded_tasks` is U1's (D-U1-11i). The
   fold needs no edit: `_grade` hands its `Resolution` to `_fold` (`loop/resolve.py:897`), which selects
   `row.writes_at(degree)` (`:450`) and calls each effect with it (`:967`).
3. **Odds, from state; outcome, from the draw.** Pool: the `task` site's rows of
   `rosters.yaml: tables.capability_uses` (U1's site table: as `social_roll`), through the one pool rule
   read by `seam/wrappers/pool.py::faculty` (`:78`; the verb's capability from its row's `capability:`
   cell, D-U1-07, which replaces the `verb_capability` side roster; an untrained actor reads
   `pool_default`, D-U1-11j). Obstacle = `roll.py::obstacle` — the task's difficulty
   (the row's `difficulty:` level, a member of `rosters.yaml: difficulty_levels`, D-U1-04; `plain` where
   the owning verb lane has stated none; the route lands with or after the column OBS §4 step 1a and
   `13_SC_tuning_tables.md` T1 put on the verb row, never on `obstacle_default`, which D-U1-11j deletes)
   plus the named modifiers that already exist (a person subject's opposition, the room). **Where nobody
   stands opposite** (a task with no person subject), the opposition term is the stand-in
   `opposed_ob(pool_default, opposition_rate)`, the untrained score through the one owner
   `sigma_leverage.opposed_ob` (`16_PESSIMIST_DICE_task_difficulty_and_throughput.md` (a), as that file's
   wave 3 line words it under D-U1-02; U1 site `task`: `opposes` reads the stand-in); the composer's even
   line `even_line(pool_add)` is its own leading term, never part of the opposition. Each term lands in `Margin.terms` (the reason trail), unchanged machinery. Every draw goes
   through the one `Draw` owner `engine/dice_engine/draw.py` (B06; C3-D3), keyed `H(seed, tick, actor,
   "task:" + a.id)` (A-30). A task row carries no `rate` row: its capability enters through this draw
   alone (D-U1-09, C3-C2).
4. **Graded, recoverable effects.** A converted `task` row keeps its flat `writes:` and `emits:`
   (`04` §B.13 invariant 12: a `Degree`-keyed column belongs to a verb that declares `contests:`); its
   magnitude is scaled by `task_fraction`, and its failed draw is the row's keyed `emits_on_refusal`
   clause `draw` (the form `finding.none` already has for the three graded inquiries); the clause's
   `emits_note` says the Event reports a lost draw, not a refusal (04 §C.4 `:727-728`: a refusal is a
   precondition failed, a loss is a contest that went against you), and the refusal-rate readings
   (`harness/corpus_run.py`'s graded-loss count) count it as a loss. A verb whose bands
   must write different cells declares `contests: "a task"` and is a contest row (shape (b)). Default band map, used where the owning verb lane has not stated one —
   **the verb lane's row supersedes this default** (one owner per row). **A-81 (no scene is still)
   holds at every band:** this file carries 53 of A-81's measured gap ("the 53 owed a draw": 22 `task`
   rows, 20 `bookkeeping` or outside rows, 11 `contest` rows owed to their lanes); the Failure band
   writes no typed cell, and its durable write is the `<verb>.failed` Event and the claims WITNESS
   deposits of it (those present hold it; an actor alone deposits his own firsthand claim of it, VRES §1),
   which the no-null-scene reading counts:

   | band | writes | emits |
   |---|---|---|
   | Failure | none | `<verb>.failed` (a new kind per row, so the act is witnessed and can be retried; the kinds are `tend.failed`, `train.failed`, `recruit.failed`, `work.failed`, `restore.failed`, `build.failed`, `found.failed`, `raze.failed`, `sabotage.failed`, `requisition.failed`, `forge.failed`, `conceal.failed`, `survey.failed`, `reconstruct.failed`, `thread_read.failed`, `open_case.failed`, `carry.failed`, `marshal.failed`, `issue.failed`, `destroy_record.failed`, and `travel.failed` for both travel rows `move` and `migrate` (below); `EVENT_KINDS` derives them, 04 §B.13 inv. 7) |
   | Partial | the effect at half magnitude where it has one (the `f(degree)` hook H-164 already names in `effects_economy.py::_rise`: `task_fraction: {Failure: 0, Partial: 0.5, Success: 1, Overwhelming: 1}`, one roster); for a finding, the claim at half confidence and the hand withheld (`_found_claims`' existing Partial shape); for a document, a flawed one (below) | the success kind |
   | Success | as today | as today |
   | Overwhelming | as today (13 measured Overwhelming at 0 of 284 at pool 2: nothing is hung on it) | as today |

   Magnitude rows read `res.degree` through that one fraction: `tend` (D-05), `work`, `restore`,
   `requisition` (the share of `amount` taken), `train` (Partial: no point, a `practice` mark the
   practice addend already reads), `recruit` (turnout; `14_VERBS_MILITARY` states its own map). Quality
   rows: `forge` and `conceal` write their band as the document's or cover's quality
   (`Record.forgery_quality = forge_quality[band]`, a roster replacing the constant
   `default_forgery_quality`; the examining draw already reads it as obstacle). Travel rows (`move`,
   `migrate`): Partial arrives one leg short, Failure stays (`travel.failed`).
5. **The classes, as decided here** (the verb lanes may move a row between `task` and `contest`; none
   may leave a consequential row unrolled):

   | class | rows |
   |---|---|
   | bookkeeping | `create_record`, `utter`, `commit`, `oblige`, `convene`, `dispatch`, `petition` (filing; the addressee's answer is his act), `give`, `transfer`, `exchange` (consent is each side's sampled choice), `form_unit`, `assign_troops`, `disband_unit`, `discharge_troops`, `order_unit`, `forgive`, `tie / knot`; rows writing nothing and finding nothing (`comply`, `construe`, `evade / defy`) are outside the refusal; their outcome is the obedience draw `14_VERBS_SOCIAL1_B` gives them |
   | task | `tend`, `train`, `recruit`, `work`, `restore`, `build`, `found`, `raze`, `sabotage`, `requisition`, `forge`, `conceal`, `survey`, `reconstruct`, `thread_read`, `move`, `migrate`, `open_case`, `carry`, `marshal`, `issue`, `destroy_record` |
   | contest (owed to the lane named) | `seize`, `confer`, `revoke`, `succeed`, `pardon`, `release`, `establish`, `surrender` (`14_VERBS_BINDING_*`); `interview`, `covenant`, `challenge` (13, `14_VERBS_SOCIAL*`) |

## Exact edits, by owner

1. `engine/season/rosters.yaml` — `graded_inquiries` renamed `graded_tasks`, every row gaining
   `form: inquiry | task`, the `task` rows added (one line each, the pair above plus `form: task`); new rosters `bookkeeping_verbs` (`{verb: why}`), `task_fraction`,
   `forge_quality`; `default_forgery_quality` retired from `data/fixtures.py` (its reader reads
   `forge_quality`).
2. `engine/season/data/rosters.py` — `GRADED_TASKS`, `BOOKKEEPING_VERBS`, `TASK_FRACTION` exported;
   `GRADED_INQUIRIES` deleted (readers: `loop/resolve.py`, `manifest/registry.py`, `data/verbs.py`).
3. `engine/season/data/verbs.py` — at load: item 1's two class refusals (a writing row in no class; a
   `bookkeeping` row touching the listed cells), and item 2's one edit of the route refusal at `:872-876`
   (by `form:`); `:848-851` unedited.
4. `engine/season/verb_table.yaml` — for each `task` row: the `<verb>.failed` kind keyed under
   `emits_on_refusal` clause `draw` (item 4); the flat `writes:` and `emits:` are unchanged; `EVENT_KINDS`
   gains the new kinds.
5. `engine/season/loop/effects_*.py` — each magnitude/quality effect reads `res.degree` through
   `TASK_FRACTION` / `forge_quality`; no effect names a band.
6. `engine/season/loop/resolve.py` — `_route = GRADED_TASKS.get(a.verb)`; nothing else (the branch
   exists).
7. `engine/season/data/fixtures.py` — `task_draw_arm: on | off` (off = today's flat fold, the
   control), shipped `on` once the gate reads.

## Gate (execution artifacts)

Tests: NEW `engine/season/tests/test_task_draw.py`, written as the batch item's first commit:
`test_converted_verb_resolves_in_at_least_two_bands` (gate 1; the loop asserts `checked >= 10` verbs),
`test_task_draw_arm_off_reproduces_the_pinned_hash` (gate 2),
`test_trained_tender_fails_less_than_default_and_neither_is_zero` (gate 3),
`test_bookkeeping_row_that_writes_a_body_is_refused_at_load` and
`test_task_row_without_a_route_is_refused_at_load` (gate 4), and
`test_loader_accepts_shapes_a_and_b_and_refuses_a_band_keyed_route_row` (gate 6). Run that file, then
`engine/season/tests/test_season_shape.py -k graded` for the renamed roster's readers.

1. Realm, `PYTHONHASHSEED=0`, seeds 0, 1, 2, two seasons each, read by
   `test_converted_verb_resolves_in_at_least_two_bands`, which counts each Event carrying a `degree` by
   the verb of the act in its `causes` (the scratch probe `…/scratchpad/det_probe.py` that first measured
   this is not in the repository and is replaced by this test): for every converted verb with ≥ 10
   resolved acts, at least two bands occur, and no such verb is 100 % one band; success events carrying
   a degree rise from 164 to at least 90 % of non-bookkeeping success events.
2. Control: `task_draw_arm: off` reproduces the pinned hashes of seed 0 (one season) and seeds 1, 2 (two
   seasons). At the working tree before B01 they read `5ab73af282d0779646c38839fbab85d8`,
   `8aae8412c221edb44ffd45d91bae2671` and `891092133b77dfb4fc789fb9bd9446c2`; every such pin moves at B01
   and at B05/B06's re-pins, so the test reads the pins current at B07, not these strings (C3-N27).
3. Odds respond to state: `tend` by a tender holding `healing` 3 against `pool_default`, 200 planted
   `tend` acts each — the trained tender's Failure share is lower, and neither is 0.
4. Loader: plant `tend` into `bookkeeping_verbs` → load refuses naming `tend`; delete `reconstruct`'s
   route → load refuses naming `reconstruct`.
6. Loader shapes (U3 §1 item 8; VRES §1 gate): the loader accepts every converted row in shape (a) and
   (b), and refuses three planted rows: a band-keyed `writes:` on a route row, a flat `writes:` on a
   `contests:` row, a writing row in no class.

5. Throughput (from `16_PESSIMIST_DICE_task_difficulty_and_throughput.md` (d)): for each converted verb,
   the count of Events at each band per season with `task_draw_arm` on, beside its success Events with
   the arm off, seeds 0 to 2, two seasons, in the landing commit's body. The arm does not ship `on` while
   any converted verb with ten or more off-arm successes has zero Success-or-better Events on-arm.

**Declared hash movers:** every realm, spine and case world in which a converted verb executes (all
goldens); re-pinned once, in the landing commit, saying so.

## Falsifier

A converted verb that resolves in one band in all of ≥ 10 acts at three seeds; a `bookkeeping` row that
writes another person's body, tenure or stores and loads; an effect that names a band literal.

## NERS reading

- **N**: from the top, the standing rule; from the bottom, the route, the roller, the band columns and
  the fraction hook all exist; laterally, `research` already works this way; diagonally, a tended man
  who stays wounded is a standing fact others can act on.
- **R**: a forgery's quality, a steward's mending, a journey's arrival become things that go wrong
  without a player; the extremes hold (Failure writes nothing and is witnessed; Overwhelming is
  today's write).
- **S**: one route, one roller, one fraction, one loader refusal; the methodology of a `tend` is that of
  a `research`.
- **E** (last): two rosters and a rename against 727 outcomes per five realm seasons brought under the
  rule.

## Cost class

Medium build (one loader refusal, one rename, about twenty band rows, five effects reading a fraction),
with or after 13's `difficulty` column for the obstacle's task term (it never ships on `obstacle_default`).
