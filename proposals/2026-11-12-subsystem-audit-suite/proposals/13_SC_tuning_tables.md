# SC — the social roll's tuning tables: one table per thing a designer tunes, on the one obstacle form's terms

Folded: 2026-11-12, lane 29 (`audits/29_ONE_OPPOSED_RULE.md` §5; `proposals/29_DICE_one_opposed_rule_form_and_tuning.md`), on Jordan's A-71 — the recomputation the U5c line below orders is done for T1 and the opposition rate. T1's half-step ladder (0 / 0.5 / 1 / 1.5) **stands unchanged**, read above the *even line* (`MU_PER_DIE × pool_add`, 2.4), with the opposition at `MU_PER_DIE` a point of trained score. Closed form on the bell curve, equals at ranks 0 / 2 / 4 / 7: `plain` fails 50.0% at every rank; `routine` 60.1 / 58.7 / 57.8 / 56.9; `demanding` 69.5 / 67.1 / 65.4 / 63.6; `hard` 77.8 / 74.6 / 72.3 / 69.8. "What is deliberately not a table: the opposition rate" is superseded by A-26 and A-71 (one fixture, shared with the fight). T3 (regard) and T5 (evidence) arrive as levels (U5c §3): one `minor` level moves Failure by about nine points at the centre. T2 and T4 are not recomputed here.

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-01 to C-04, C-13, C-33, C-35) — five changes; the tables' shape and the order of commits stand. (1) T3's reader `person_q.regard(counterparty, actor, fx)` opens the counterparty's ledger at RESOLVE (`04` §B.2, F8): the reader is `person_q.stance_toward(counterparty, actor)` clamped at `STANCE_MAX`, its hostile half the `regard` term and its favourable half a `favour` level. (2) No table subtracts from the obstacle (Jordan, A-25). (3) Row values: every rolled row `routine` at the control arm; at commit 2 only `interrogate` is `demanding`. (4) Every number here is whole-dice arithmetic at the half-score rate. Jordan's A-5, A-6, A-7 and A-26 move the sampler, the pool rule and the opposition rate, so the tables are recomputed in one step (`U5c_SC_one_obstacle_form.md` §4 step 5). T4's bench modifier stands (A-12). (5) Citations of `05_SC_evidence_and_rebuttal.md` read `05_SC_evidence_and_rebuttal_B.md`.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.4 row T13, §2 row T13, §7, §7b-T; `unified/U1_OWNERS_AND_VOCABULARY.md` D-U1-01, D-U1-01a, D-U1-02, D-U1-04, ledger R-17 to R-21, R-25, R-26; `unified/U1_GLOSSARY.md` *modifier*, *standing*, *difficulty level*; `unified/U3_CONFLICT_LEDGER.md` §9; `unified/U3_DEPENDENCY_ORDER.md` §6.2). The body is brought to its two head lines and to the decisions: the composition is `U5c_SC_one_obstacle_form.md`'s (OBS), not SC-B's; T1's row values are OBS §4's (all `routine` at control; only `interrogate` `demanding` at commit 2) and its basis is lane 29's closed form, the whole-dice figures marked history; T3 reads `person_q.stance_toward` (C-03), hostile half the `regard` term, favourable half the `favour` level, nothing subtracted (A-25); **T4's "standing" die is replaced by the seat row's `modifier:`** read by the `office` leverage source off `Act.via` (D-U1-01, D-U1-01a; the reader `judging_set(w, room)` is not used: one reader), so `standing_dice` and the pool addend are not created and A-12's bench modifier stands as a level; T5 is the `proofs` leverage source (`proof_level`; `proof_step` deleted, OBS §3) with the admission filter kept; "the opposition rate: ruled `score/2`" is replaced by A-26/A-79 (one fixture `opposition_rate`); the gate's scratch probes become named tests; lands-it and tier added. Not applied: C3-N6's "replace 'holds'" for this head — this head makes no C1 claim (row wrong at the tree); the C1 caveat is in `13_SC_calibration.md`. A-12's Layer 1 text (`04` §B.7) is owed (D-U1-01's draft), not applied.

**Lands in batch:** B05 (commit 1 at OBS §4 step 3; commit 2 at step 5). **Depends on:** `U5c_SC_one_obstacle_form.md` (B05), `13_SC_calibration.md` (its test file first, B05), `02_CHAR_scar_cap_and_regard_unit.md` item 2 (the stance unit, B10; at control `regard_step` 0 the term reads nothing), U1 §11 U1-D (the seat row's `modifier:` column; T4's values ride commit 2).

## Status: PROPOSED

Written by the contest-interrogation lane (`audits/13_SC_contest_interrogation.md` §4–§5, §8 R-1..R-10).
Composes on `U5c_SC_one_obstacle_form.md` (OBS: the obstacle as the even line, difficulty, the opposition
and named hostile terms, one composer, a term list on `Margin`; it superseded SC-B's composition), U1 §5's
`capability:` column (which carries what SC-P7 asked of `verb_capability`), `05_SC_evidence_and_rebuttal_B.md`
(cited items), CHAR's
`02_CHAR_scar_cap_and_regard_unit.md` (regard in the stance unit, clamped) and
`02_CHAR_which_ground_moves_whom.md` (susceptibility as advantage). It adds no second system: every
table below is a row, a column or a fixture on an owner that exists or that SC-B creates. Ratifies
nothing; reference under `CLAUDE.md` §0.05.

## What it changes in `engine/season/` at runtime

Landed in two commits. **Commit 1 (control arm, no mover):** the tables exist with the control sizes for
`difficulty_levels` (0 / 1 / 2 / 3), every arrangement row's `standard` at `plain`, `regard_step` 0, no
seat row carrying `modifier:`, and admission filtering off; every world hash is the hash OBS step 2 gives.
**Commit 2 (the calibrated arm, a declared mover; OBS §4 step 5, with A-5, A-6, A-7 and A-79):** the
half-step sizes above the even line, the authored row standards, `regard_step` 1.0, the bench seats'
`modifier:` first value, admission on. Every rolled social act's obstacle can move; in the
shipped realm today (no scores held, almost no stance rows, no arrangement docketed) the moves are
confined to the difficulty level of each verb and to `speak`'s room, measured in the gate.

## The problem, with evidence

Measured in the audit (scripts under the lane's scratch `runs/SC_INT/`, not in the repository; whole-dice
history at the half-score rate):

1. In the realm, 270 of 284 rolled social acts (seeds 0–1, two seasons each) roll pool 2 against
   Ob 2.0; the other fourteen move only by a bench's reception or a forged record (audit §3.2).
2. A 54-cell planted grid (venue × temperament × affiliation relation × stance) moves no verb's
   obstacle; a held score of 6 moves `tell`, `argue`, `speak` and does not move `lie`, `determine`,
   `interrogate` or `arrest`, which have no capability key (§3.3).
3. Under SC-B's level sizes (`routine` 1), a contest between equals fails 0.71–0.74 at pools 2–8 and
   `demanding` and `hard` give the same cell (0.85–0.90 vs 0.90) (§3.4).
4. The room's modifiers saturate at the floor and the cap: at pool 2 every favourable room composes
   1.0 and every hostile one 2.842 (§3.1).

Nobody can tune what has no row. SC-B gives the obstacle its seats; this file gives each seat a table
a designer edits, a first value with its basis, and the sweep that would set it.

## The resolution, decided

### T1 — verb base difficulty

- **Owner**: `engine/season/verb_table.yaml`, a `difficulty:` column on every contested or graded row
  (D-U1-04; SC-B Edit A as reconciled), naming a **difficulty level**, a member of `rosters.yaml:
  difficulty_levels`; the level's size in the fixture table `difficulty_ob` (`data/fixtures.py`, one NUMBER
  row in `hole_register.yaml`). Lane A's `rosters.yaml: task_difficulty` retires into it (D-U1-04).
- **Keys**: the levels `plain`, `routine`, `demanding`, `hard` (ordered, closed).
- **Unit**: obstacle units (net successes; one die nets `MU_PER_DIE` 0.4 on average).
- **First values (calibrated arm)**: `plain` 0, `routine` 0.5, `demanding` 1.0, `hard` 1.5, above the
  even line. **Control arm**: 0 / 1 / 2 / 3, which reproduces today's 2.0 for every unscored counterparty
  under the `pool_default` stand-in. Basis (the head's closed form on the bell curve, equals at trained
  ranks 0 / 2 / 4 / 7): `plain` fails 50.0% at every rank; `routine` 60.1 / 58.7 / 57.8 / 56.9;
  `demanding` 69.5 / 67.1 / 65.4 / 63.6; `hard` 77.8 / 74.6 / 72.3 / 69.8 (target C1 0.50–0.65 for
  `routine`). The audit's whole-dice basis (§3.4) is history.
- **Row values** (`grade: assumption` each; OBS §4, C-04): every rolled row `routine` at the control arm;
  at commit 2 `interrogate` → `demanding`, the inquiries stay `routine`.
- **Floor**: the composed obstacle is floored at `OB_MIN` after every term (OBS §2), which removes the Ob
  0.0 cell a held score of 0 gave (audit degenerate cell 3).
- **Sweep**: the size ladder at {0/1/2/3, 0/0.5/1/1.5, 0/0.75/1.5/2.25}; exact grid at trained ranks 0, 2,
  4, 7.
- **Falsifier**: an act whose row names a level other than `plain` and whose term list shows
  `difficulty 0`; or, at the calibrated arm, two adjacent levels giving the same P(Failure) at equals for
  any pool in 2–6.

### T2 — venue standard

- **Owner**: `engine/season/arrangements.yaml`, a `standard:` key on each arrangement row (OBS §2 member 3),
  naming a `difficulty_levels` member; `data/arrangements.py` adds it to `_ARRANGEMENT_KEYS` and refuses a
  value outside the roster.
- **Keys**: the nine rows. **Unit**: as T1 (the same table of sizes; no second ladder).
- **First values**: `arbitration`, `interrogation`, `negotiation` `plain`; `parliamentary_debate`,
  `council_of_state`, `legal_trial` `routine`; `tribunal`, `excommunication_deliberation` `demanding`;
  `inquisition_hearing` `hard`. Basis: one level per formal layer the row's `interposed:` names among
  `procedure`, `office`, `document`, `ceremony` (`person`, an advocate, is help, not a layer). The rule is
  the first reading only; the authored value is the fact, so a designer overrides any row.
- **Publicity** (`floor: open`) is not a term: a row whose open floor should make it harder carries a
  higher `standard`. Calibration step 3 sweeps it (+1 level on open-floor rows) to see whether it earns
  the authored bump.
- **Reach**: read only for an act a bench hears on a docketed matter whose item names the row; until
  computed dockets name a row (SC audit F-SC-06; SC-P4), T2 is inert in the realm and live in planted
  hearings.
- **Sweep**: each row's standard at its level ± 1, in a planted hearing per row.
- **Falsifier**: a docketed `speak` or `determine` under a non-`plain` row whose term list lacks
  `standard`.

### T3 — the hearer's disposition (regard)

- **Owner**: the fixture `regard_step` (OBS §2 member 7) applied to `person_q.stance_toward(counterparty,
  actor)` (the counterparty's stance rows naming the actor: his interior, not his ledger; C-03) in the
  stance unit and clamped at `STANCE_MAX` (`data/cast.py:507`, 25) as `decision/options.py:1778` already
  clamps it for a teller: the hostile half is the obstacle term `regard = regard_step ·
  clamp(−stance / STANCE_MAX, 0, 1)`; the favourable half is the `favour` leverage level (OBS §3). Nothing
  is subtracted (A-25).
- **Unit**: Ob per full clamp. **First value**: `regard_step` 1.0 (±1.0 Ob at the clamp); control 0.
  Basis: one full unit of favour moves equals at `routine` by 0.16–0.28 (§3.4, `equals+favour1`), the
  same order as two levels of effort at pool 2 (0.74 → 0.42): a devoted friend is worth a sustained
  effort, not a certainty.
- **Affiliation and faction ties**: `person_q.regard` carries `heritage_regard` (CR-31) and the judged
  and told deeds, but it opens the counterparty's ledger and is not read at RESOLVE (C-03); the obstacle
  reads stance rows only, so an affiliation tie reaches this term only as a stance row the counterparty
  holds (audit R-4: never a second affiliation term).
- **Never with a bench**: an act a bench hears reads `reception` instead (SC-B's rule).
- **Realm note, stated rather than hidden**: in the seeded realm the regard a counterparty holds toward
  the actor is between −0.36 and +0.64 in all but a few rolls (stance rows give 4.0 and 12.5), so at
  the clamp unit T3 moves an act by under 0.03 Ob until relations are authored
  (`02_CHAR_relations_have_a_ground.md`). That is the content's gap, not the table's.
- **Sweep**: `regard_step` 0 / 0.5 / 1.0 / 2.0 over a planted ±25 grid.
- **Falsifier**: SC-B's two-NPC fold (hearer's stance +4×5 vs −4×5): the two Events' term lists differ
  in `regard` alone, by `2 · regard_step · 0.8`.

### T4 — the seat's modifier and stakes

- **Stakes** — owner: fixture table `stakes_ob` (OBS §2 member 5), keyed by Tenure kind; first values:
  `oblige` 0, `detain` 0.5, `ban` 1.0 (Ob). Read for `determine` (the docketed row's `disposes:`) and
  `arrest` (`detain`). Sweep 0 / 0.5× / 1× / 2×.
- **The seat's modifier (A-12)** — owner: the seat's own row, `engine/season/offices.yaml` key
  `modifier: <a LEVEL_SIGMA name> | null` (D-U1-01a; U1 §11 U1-D), read by one host function, the `office`
  member of `sigma.py::ADVANTAGE_SOURCES`, off `Act.via`, where the act's prize row's `heard_by` names a
  bench or body the actor sits on or presides over; it gives the actor **one level**, never dice, never an
  obstacle term (D-U1-01). First value: `minor` on the bench seats (the former `standing_dice` 1, restated
  once in the level unit at OBS §4 step 5); control: no seat row carries one. No fixture `standing_dice`
  and no pool addend are created; `judging_set(w, room)` is not read (one reader: `Act.via`). A seat held
  above the actor's by the person acted on stands against the act as `rank_gap` (OBS §2 member 6). The
  `04` §B.7 amendment text is owed (D-U1-01's draft), not applied.
- **Falsifier**: a seat-holder's `speak` before his own bench whose `office` level equals the same
  person's before a foreign bench, his seat row carrying `modifier: minor`; or a seat found in his pool or
  his opposition.

### T5 — evidence

- **Owner**: the `proofs` leverage source (OBS §3: one `proof_level` per whole unit of weight standing for
  the actor's side; `proof_level` first value `minor`, control `None`; `proof_step` is deleted), over
  today's `world_q.proofs` until `05_SC_evidence_and_rebuttal_B.md`'s cited items land, plus the arrangement
  row's existing `proofs:` column as the **admission filter**: a proof whose kind the docketed row does not admit weighs 0. The kind of
  a deed claim is its `source` mapped to the `proofs` roster (`record`, `testimony`, `oath`,
  `confession`); the mapping is a roster row beside `proofs`, not a code literal.
- **First value**: `proof_level` `minor`; admission on. Basis: H-216's named limit (*"the arrangement's
  admitted `proofs` column is not read here"*) closed at the owner.
- **Subject term** (inquiries): `Record.forgery_quality`, unchanged.
- **Sweep**: `proof_level` `None` / `minor` / `moderate` with admission on and off.
- **Falsifier**: a `speak` under `parliamentary_debate` (admits no proofs) whose `levels` show a non-zero
  `proofs`.

### What is deliberately not a table

- **Temperament and susceptibility**: advantage, not obstacle, through CHAR's
  `02_CHAR_which_ground_moves_whom.md` on the existing `advantage_sources` roster (audit R-9).
- **Venue building kind** (`venues.yaml`): no term (R-3).
- **Season and territory conditions**: no term (R-6).
- **The opposition rate**: one fixture `opposition_rate` shared with the fight (A-26, A-71, A-79; carried by
  `05_SC_opposed_obstacle_parity.md`): control 0.5, live `MU_PER_DIE`, on the opponent's trained score
  (D-U1-02). It is not a table here.

## Exact edits, by owner

1. `engine/season/data/fixtures.py`: `difficulty_ob` (two arms: `control` 0/1/2/3 and `half`, shipped
   `control` in commit 1, `half` in commit 2), `regard_step` (0 → 1.0), `proof_level` (`None` → `minor`),
   `proof_admission` (`off` → `on`); each with its `H-` NUMBER row and its sweep in `hole_register.yaml`.
   No `standing_dice`.
2. `engine/season/arrangements.yaml` + `data/arrangements.py`: `standard:` on all nine rows (commit 1:
   all `plain`; commit 2: the T2 values); the key added to `_ARRANGEMENT_KEYS`.
3. `engine/season/rosters.yaml`: a `proof_kind_of_source` row beside `proofs` (claim source → proof kind).
4. `engine/season/queries/world_q.py::proofs`: filter by the docketed row's `proofs:` when
   `proof_admission` is `on` (the row is passed in by the host builder; `world_q` reads no arrangement
   itself).
5. `engine/season/offices.yaml`: commit 2 authors `modifier: minor` on the bench seats (the column and its
   `office` reader land in U1 §11 U1-D); no pool addend.
6. `engine/season/seam/wrappers/sigma.py::obstacle_operands`: fill `regard` from
   `person_q.stance_toward(counterparty, actor)` in the clamp unit (C-03).
7. `engine/season/verb_table.yaml`: the `difficulty:` values (OBS §4: `routine` everywhere at commit 1;
   `interrogate` `demanding` at commit 2).

## Gate (execution artifacts)

- Exact: the audit's `calibrate.py` (scratch, not in the repository) is restated as
  `engine/season/tests/test_sc_calibration_targets.py` (`13_SC_calibration.md`), run against the module's own
  `obstacle`: the calibrated arm meets every target in `13_SC_calibration.md` §2 (green at commit 2, red on
  C1 and C8 at commit 1).
- Commit 1: `build_realm(0)` and `(1)`, two seasons: hashes equal to OBS step 2's landing.
- Commit 2: the same runs, printed per verb from SC-P1's record (pool, Ob, terms, levels, bands); the
  obstacle distribution has more than two values for every rolled verb with ≥ 5 rolls (named test
  `test_sc_calibration_targets.py::test_every_rolled_verb_with_five_rolls_shows_more_than_two_obstacles`).
- The planted grid (`planted_grid.py`, scratch) is restated as
  `engine/season/tests/test_sc_tuning_tables.py::test_planted_grid_moves_lie_interrogate_and_speak` (new):
  after the capability column and commit 2, `lie` and `interrogate` move with the counterparty's trained
  score; `speak` moves with T2 under a docketed row; no cell's obstacle is moved by temperament (that is
  leverage, CHAR's). `::test_a_bench_seat_modifier_is_one_level_for_its_own_bench_only` (T4).

## Falsifier

Any table above whose key changes value at the calibrated arm and whose grid reading does not change in
any cell: that table is decoration and should be deleted.

## NERS reading

- **N**: from the top a designer names a level per verb and per room; from the bottom each term reads a
  fact a person or a row already holds; laterally combat's obstacle already comes from the defender and
  the instance; diagonally a room's formality and a friend's regard reach one person's roll. Remove
  T1 and every contest is again one cell.
- **R**: the same lie is easier among friends, a trial harder than a quarrel, a seat-holder stronger in
  his own chamber; characters differ by score and stance, rooms by standard and admission; each
  difference is in the term list or the levels afterwards. Complete at the extremes: bounded by the cap and by
  `OB_MIN`, and the calibration names where the cap flattens (overmatched = hopeless at the chance floor).
- **S**: one ladder of sizes for the verb and the room; regard and reception are one quantity at two
  audiences; a seat's help is one level on the leverage channel and a seat above stands against as
  `rank_gap`, one channel per side (D-U1-01); one composer.
- **E** (last, against N and R): five tables, four of them a single column or fixture, and a term list
  a player reads as a sentence.

## Cost class

Small build on OBS (commit 1 is data and two reads; commit 2 is values). Lanes: SC (module, host
builder), IN/CORE (verb column, fixtures), FA (arrangement standards; seat `modifier:` values), CHAR
(regard unit, clamp).

**Lands it and tier.** The B05 batch: commit 1 at OBS §4 step 3 (`sonnet`, `valoria-author`, hash-equal),
commit 2 at step 5 (`sonnet` for the values, `opus` for the calibration read), one `methodology-close` for the
batch. **Hash movers.** Commit 2 (declared, re-pinned once with B05).
