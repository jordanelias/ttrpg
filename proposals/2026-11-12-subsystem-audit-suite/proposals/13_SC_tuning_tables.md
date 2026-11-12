# SC — the social roll's tuning tables: one table per thing a designer tunes, on SC-B's terms

Folded: 2026-11-12, lane 29 (`audits/29_ONE_OPPOSED_RULE.md` §5; `proposals/29_DICE_one_opposed_rule_form_and_tuning.md`), on Jordan's A-71 — the recomputation the U5c line below orders is done for T1 and the opposition rate. T1's half-step ladder (0 / 0.5 / 1 / 1.5) **stands unchanged**, read above the *even line* (`MU_PER_DIE × pool_add`, 2.4), with the opposition at `MU_PER_DIE` a point of trained score. Closed form on the bell curve, equals at ranks 0 / 2 / 4 / 7: `plain` fails 50.0% at every rank; `routine` 60.1 / 58.7 / 57.8 / 56.9; `demanding` 69.5 / 67.1 / 65.4 / 63.6; `hard` 77.8 / 74.6 / 72.3 / 69.8. "What is deliberately not a table: the opposition rate" is superseded by A-26 and A-71 (one fixture, shared with the fight). T3 (regard) and T5 (evidence) arrive as levels (U5c §3): one `minor` level moves Failure by about nine points at the centre. T2 and T4 are not recomputed here.

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-01 to C-04, C-13, C-33, C-35) — five changes; the tables' shape and the order of commits stand. (1) T3's reader `person_q.regard(counterparty, actor, fx)` opens the counterparty's ledger at RESOLVE (`04` §B.2, F8): the reader is `person_q.stance_toward(counterparty, actor)` clamped at `STANCE_MAX`, its hostile half the `regard` term and its favourable half a `favour` level. (2) No table subtracts from the obstacle (Jordan, A-25). (3) Row values: every rolled row `routine` at the control arm; at commit 2 only `interrogate` is `demanding`. (4) Every number here is whole-dice arithmetic at the half-score rate. Jordan's A-5, A-6, A-7 and A-26 move the sampler, the pool rule and the opposition rate, so the tables are recomputed in one step (`U5c_SC_one_obstacle_form.md` §4 step 5). T4's bench modifier stands (A-12). (5) Citations of `05_SC_evidence_and_rebuttal.md` read `05_SC_evidence_and_rebuttal_B.md`.

## Status: PROPOSED

Written by the contest-interrogation lane (`audits/13_SC_contest_interrogation.md` §4–§5, §8 R-1..R-10).
Composes on `05_SC_obstacle_difficulty_and_modifiers_B.md` (SC-B: the obstacle as difficulty plus named
terms, one composer, a term list on `Margin`), `05_SC_capability_surface.md` (SC-P7: the missing
`verb_capability` rows), `05_SC_evidence_and_rebuttal.md` (SC-P8: cited items), CHAR's
`02_CHAR_scar_cap_and_regard_unit.md` (regard in the stance unit, clamped) and
`02_CHAR_which_ground_moves_whom.md` (susceptibility as advantage). It adds no second system: every
table below is a row, a column or a fixture on an owner that exists or that SC-B creates. Ratifies
nothing; reference under `CLAUDE.md` §0.05.

## What it changes in `engine/season/` at runtime

Landed in two commits. **Commit 1 (control arm, no mover):** the tables exist with SC-B's sizes for
`difficulty_levels` (0 / 1 / 2 / 3), every arrangement row's `standard` at `plain`, `regard_step` 0,
`standing_dice` 0, and admission filtering off; every world hash is the hash SC-B's own landing gives.
**Commit 2 (the calibrated arm, a declared mover):** the half-step sizes, the authored row standards,
`regard_step` 1.0, `standing_dice` 1, admission on. Every rolled social act's obstacle can move; in the
shipped realm today (no scores held, almost no stance rows, no arrangement docketed) the moves are
confined to the difficulty level of each verb and to `speak`'s room, measured in the gate.

## The problem, with evidence

Measured in the audit (scripts under the lane's scratch `runs/SC_INT/`):

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
  (SC-B edit 2), naming a member of `rosters.yaml: difficulty_levels` (SC-B edit 1); the level's size in
  the fixture table `difficulty_ob` (`data/fixtures.py`, one NUMBER row in `hole_register.yaml`).
- **Keys**: the levels `plain`, `routine`, `demanding`, `hard` (ordered, closed).
- **Unit**: obstacle units (net successes; one die nets `MU_PER_DIE` 0.4 on average).
- **First values (calibrated arm)**: `plain` 0, `routine` 0.5, `demanding` 1.0, `hard` 1.5. **Control
  arm**: SC-B's 0 / 1 / 2 / 3, which reproduces today's 2.0 for every unscored counterparty under
  DICE's `pool_default` opposition. Basis: §3.4 — at the half-step sizes, equals at `routine` fail
  0.58–0.64 (target 0.50–0.65), the four levels separate at pool 2 as 0.42 / 0.58 / 0.74 / 0.83, and
  overmatched at `routine` sits 0.83–0.90 (target 0.80–0.90).
- **Row values** (`grade: assumption` each): `tell`, `argue`, `speak`, `lie`, `determine`, `arrest` →
  `routine`; `interrogate`, `research`, `examine`, `surveil` → `demanding`. Basis: SC-B's assignments,
  kept; the level sizes are what moves.
- **Floor**: the composed obstacle is floored at `OB_MIN` after every term (SC-B's bound), which removes
  the Ob 0.0 cell a held score of 0 gives today (audit degenerate cell 3).
- **Sweep**: the size ladder at {0/1/2/3, 0/0.5/1/1.5, 0/0.75/1.5/2.25}; exact grid at pools 2–8.
- **Falsifier**: an act whose row names a level other than `plain` and whose term list shows
  `difficulty 0`; or, at the calibrated arm, two adjacent levels giving the same P(Failure) at equals for
  any pool in 2–6.

### T2 — venue standard

- **Owner**: `engine/season/arrangements.yaml`, a `standard:` key on each arrangement row (SC-B edit 3),
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

- **Owner**: the fixture `regard_step` (SC-B edit 1) applied to `person_q.regard(counterparty, actor,
  fx)` read in CHAR's stance unit and clamped at `STANCE_MAX` (`data/cast.py:507`, 25) as
  `decision/options.py:1778` already clamps it for a teller: `regard_term = regard_step ·
  clamp(regard / STANCE_MAX, −1, 1)`, subtracted (favour) after the bound or added (hostility) inside it.
- **Unit**: Ob per full clamp. **First value**: `regard_step` 1.0 (±1.0 Ob at the clamp); control 0.
  Basis: one full unit of favour moves equals at `routine` by 0.16–0.28 (§3.4, `equals+favour1`), the
  same order as two levels of effort at pool 2 (0.74 → 0.42): a devoted friend is worth a sustained
  effort, not a certainty.
- **Affiliation and faction ties enter here and nowhere else**: `regard` already carries
  `heritage_regard` (CR-31, creed and caste at `heritage_gain` 0.5) and the judged and told deeds; a
  second affiliation term would count the same holding twice (audit R-4).
- **Never with a bench**: an act a bench hears reads `reception` instead (SC-B's rule).
- **Realm note, stated rather than hidden**: in the seeded realm the regard a counterparty holds toward
  the actor is between −0.36 and +0.64 in all but a few rolls (stance rows give 4.0 and 12.5), so at
  the clamp unit T3 moves an act by under 0.03 Ob until relations are authored
  (`02_CHAR_relations_have_a_ground.md`). That is the content's gap, not the table's.
- **Sweep**: `regard_step` 0 / 0.5 / 1.0 / 2.0 over a planted ±25 grid.
- **Falsifier**: SC-B's two-NPC fold (hearer's stance +4×5 vs −4×5): the two Events' term lists differ
  in `regard` alone, by `2 · regard_step · 0.8`.

### T4 — standing and stakes

- **Stakes** — owner: fixture table `stakes_ob` (SC-B), keyed by Tenure kind; values kept from SC-B:
  `oblige` 0, `detain` 0.5, `ban` 1.0 (Ob). Read for `determine` (the docketed row's `disposes:`) and
  `arrest` (`detain`). Sweep 0 / 0.5× / 1× / 2×.
- **Standing** — owner: one pool addend registered through `seam/wrappers/pool.py::register_pool_addend`
  (the one door into the pool), reading a fixture `standing_dice` (whole dice). It adds `standing_dice`
  to the actor's pool when he holds a live office hold whose seat sits on the bench of the room the act
  is heard in (`judging_set(w, room)` contains him by his seat); 0 otherwise and for unheard acts.
  First value 1; control 0. Basis: *"Rank supplies dice and gates nothing"* (`rosters.yaml:
  verb_capability` source line, `03 §A.2`): standing is the actor's resource, a die, never a bar on
  the act and never an obstacle term.
- **Falsifier**: a seat-holder's `speak` before his own bench whose `pool` equals the same person's
  before a foreign bench, at `standing_dice` 1.

### T5 — evidence

- **Owner**: the existing fixture `proof_step` (0.25, H-216) on SC-B's `evidence` term (today's
  `world_q.proofs` until SC-P8's cited items land), plus the arrangement row's existing `proofs:` column
  as the **admission filter**: a proof whose kind the docketed row does not admit weighs 0. The kind of
  a deed claim is its `source` mapped to the `proofs` roster (`record`, `testimony`, `oath`,
  `confession`); the mapping is a roster row beside `proofs`, not a code literal.
- **First value**: `proof_step` 0.25 kept; admission on. Basis: H-216's named limit (*"the arrangement's
  admitted `proofs` column is not read here"*) closed at the owner.
- **Subject term** (inquiries): `Record.forgery_quality`, unchanged.
- **Sweep**: `proof_step` 0 / 0.25 / 0.5 with admission on and off.
- **Falsifier**: a `speak` under `parliamentary_debate` (admits no proofs) whose term list shows a
  non-zero `evidence`.

### What is deliberately not a table

- **Temperament and susceptibility**: advantage, not obstacle, through CHAR's
  `02_CHAR_which_ground_moves_whom.md` on the existing `advantage_sources` roster (audit R-9).
- **Venue building kind** (`venues.yaml`): no term (R-3).
- **Season and territory conditions**: no term (R-6).
- **The opposition rate**: ruled `score/2`; SC-B's `opposition_rate` fixture keeps 0.4 as a swept arm.
  The audit measured that 0.4 flattens the equals drift (0.51–0.52 at every pool) and records it; it is
  not re-raised.

## Exact edits, by owner

1. `engine/season/data/fixtures.py`: `difficulty_ob` (two arms: `scb` and `half`, shipped `scb` in commit
   1, `half` in commit 2), `regard_step` (0 → 1.0), `standing_dice` (0 → 1), `proof_admission` (`off` →
   `on`); each with its `H-` NUMBER row and its sweep in `hole_register.yaml`.
2. `engine/season/arrangements.yaml` + `data/arrangements.py`: `standard:` on all nine rows (commit 1:
   all `plain`; commit 2: the T2 values); the key added to `_ARRANGEMENT_KEYS`.
3. `engine/season/rosters.yaml`: a `proof_kind_of_source` row beside `proofs` (claim source → proof kind).
4. `engine/season/queries/world_q.py::proofs`: filter by the docketed row's `proofs:` when
   `proof_admission` is `on` (the row is passed in by the host builder; `world_q` reads no arrangement
   itself).
5. `engine/season/seam/wrappers/pool.py`: register the standing addend (its reader in
   `queries/world_q.py`, beside `practice`).
6. `engine/season/seam/wrappers/sigma.py::contest_input`: fill `regard` from `person_q.regard` in the
   clamp unit (SC-B edit 6 already names the operand).
7. `engine/season/verb_table.yaml`: the `difficulty:` values (SC-B edit 2, unchanged).

## Gate (execution artifacts)

- Exact: the audit's `calibrate.py` re-run against the module's own `obstacle` after SC-B lands
  (rather than the audit's re-statement of it): the calibrated arm meets every target in
  `13_SC_calibration.md` §2.
- Commit 1: `build_realm(0)` and `(1)`, two seasons: hashes equal to SC-B's landing.
- Commit 2: the same runs, printed per verb as the audit's `tap_summary` (pool, Ob, terms, bands); the
  obstacle distribution has more than two values for every rolled verb with ≥ 5 rolls.
- The planted grid (`planted_grid.py`) re-run after SC-P7 and commit 2: `lie` and `interrogate` move
  with the counterparty's score; `speak` moves with T2 under a docketed row; no cell is moved by
  temperament (advantage is CHAR's).

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
  difference is in the term list afterwards. Complete at the extremes: bounded by the cap and by
  `OB_MIN`, and the calibration names where the cap flattens (overmatched = hopeless at the chance floor).
- **S**: one ladder of sizes for the verb and the room; regard and reception are one quantity at two
  audiences; standing is dice, as rank is everywhere else; one composer.
- **E** (last, against N and R): five tables, four of them a single column or fixture, and a term list
  a player reads as a sentence.

## Cost class

Small build on SC-B (commit 1 is data and two reads; commit 2 is values). Lanes: SC (module, host
builder), IN/CORE (verb column, fixtures), FA (arrangement standards), CHAR (regard unit, clamp).
