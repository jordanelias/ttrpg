# VERBS SOCIAL1 · C — persuasion and deceit: `argue`, `lie`, `conceal` drawn with a reason on every band

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-15, C-26) — three changes. (1) `argue`'s Partial write is withdrawn: the band is `argument.held` and nobody moves (`16_PESSIMIST_SC_D_an_argument_moves_someone.md` edit 1). (2) `lie`: the capability is `deception`; the `contradiction` term is dropped, because it opens the hearer's ledger at RESOLVE (`04` §B.2) and a hearer who knows better is already handled at WITNESS (`16_PESSIMIST_SC_E_an_honest_teller_is_not_marked.md` edit 1); `deceit.exposed` at Failure stands. (3) `conceal`'s `notoriety` term is the roster member `watch`, read from presence and not from other people's ledgers; `a cover` is not a prize (`U5c_VERBS_residue_and_governance_owner.md` §1, §2).
Reconciled: 2026-11-12, wave-3 rewrite lane W3-4a — the head's three changes applied to the body (`unified/work/R4_READ.md` §1.5, 7b.6): `argue`'s Partial write and `argue_shift_by_band` deleted (C-15); `evidence` is the `proofs` leverage source, not an obstacle term (C-01, A-25); `lie`'s capability `deception` (U1 capability architecture §5), `contradiction` and `contradiction_ob` struck (C-26; `04` §B.2), `opposed_by` placed on the capability row as OBS §2 reads it; `conceal` is shape (a) (one Record, the band sets its quality; no prize `a cover`), `notoriety`/`notoriety_step` → `watch`/`watch_step` (U1 R-23), and the `concealment` score term and `conceal_rank_step` are deleted (`unified/U3_CONFLICT_LEDGER.md` C3-L10; the gate that read them re-reads formation); A-81, A-30, U3 batch B28, R4 7b.0 block.

Reconciled: 2026-11-12, unification lane U4c (test 9; opened at the tree) — the `[UNVERIFIED]` on the corpus check's definition is settled: `harness/corpus_run.py::bands_that_differ` (`:908-916`) counts only `VerbRow.writes_at` differences between a contested row's bands (`:915`). So this file takes its stated fallback: the gate reads the per-band `emits` difference (`VerbRow.emits_at(degree)`, `data/verbs.py:363`), and the edit is a second key set beside `bands_that_differ`, over `emits_at`, in the same function's module, reported in the corpus line `harness/corpus_run.py:1180`.

## Status: PROPOSED

Lands in batch: B28 (`unified/U3_DEPENDENCY_ORDER.md` §3.1), after `14_VERBS_SOCIAL1_D_grievance_and_settlement.md` in the same batch.
Depends on: `05_SC_obstacle_difficulty_and_modifiers_B.md` and `U5c_SC_one_obstacle_form.md` (B05; `watch` lands in B12 with `14_VERBS_MATERIAL_A`); `16_PESSIMIST_SC_D_an_argument_moves_someone.md` edit 1 (the `argument.held` band) and `16_PESSIMIST_SC_E_an_honest_teller_is_not_marked.md` edit 1 (WITNESS's handling of a hearer who knows better); lane A (B01: persons hold scores); `14_VERBS_SOCIAL1_D` (B28: commit degree); `18_DETERMINISM_task_draw_for_uncontested_verbs.md` items 2, 4 (B07: `conceal` joins `graded_tasks`).
Lane: SC. Tier (R4 7b.0 (1)): `sonnet` producer, effort `high`; `lie`'s told-deposit confidence `opus`; one `opus` read of the two-arm band tables. Test file: `engine/season/tests/test_vm_s1_c_persuasion.py` (one function per two-arm fold).
Standing (R4 7b.0 (4)): the pool is the one pool rule (`sigma_leverage.pool_of`, D-U1-08) on the actor's skill score (A-6); the governing attribute as levels (A-7); a wound a level against the roll (A-8); the opposition is the counterparty's skill score through `opposed_ob` (A-79, D-U1-02). Draws: `H(w.world_seed, w.tick, <actor id>, "argue.standing")`, `"lie.standing"`, `"conceal.task"` (A-30). **A-81:** `argue`'s Failure deposits `argument.lost` to the hearer; `lie`'s Failure deposits `deceit.exposed` naming the liar; `conceal`'s failed draw `cover.failed` is witnessed by those present.

Batch S1-C of `audits/14_VERBS_SOCIAL1.md` §14. Authored in part by Fable; completed by Opus after the
Fable usage limit (2026-11-12). Reference only (CLAUDE.md §0.05). Read at `84d2a02`. Needs SC-OB
(`05_SC_obstacle_difficulty_and_modifiers_B.md`) and lane A steps 3–4 (persons hold scores; one score,
two roles).

## What it changes in `engine/season/` at runtime

`argue` gains a `commitment` obstacle term (its Partial is `argument.held`: nobody moves, C-15). `lie`
gains its own skill, an opposing key, a confidence that follows the band, and a Failure that deposits
a deed. `conceal` becomes drawn (cover quality by band, a failed draw that is witnessed); it is ranked by
its alignment cells and stance, as every verb is. Declared hash mover.

## The problem, with evidence

- `argue`: Partial emits `argument.won` and writes nothing (`verb_table.yaml:133` row; `_eff_argue` runs
  only on bands whose `writes:` is non-empty); pool 2 for every actor (`aperture 1 0` POOLS ROLLED); a
  hearer's commitments do not enter the roll.
- `lie`: `[corpus]` "bands that differ: False"; Failure (110 of 138 graded) deposits nothing but
  `news.untold`; no skill row; the hearer's own firsthand knowledge of the cell does not enter the roll
  (H-183 counts it against the liar only after the fact).
- `conceal`: "RANKING EXCLUDES" (no celled axis: chosen by the draw's tie-break, not a reason); cover quality
  does not exist, so an inquiry cannot be harder against a better cover; the mint is certain — a fixed
  function of state, against `AUDIT_BRIEF.md`'s Standing rule.

## The resolution, decided

### 1. `argue`

- *(W3-4a, C-15: the Partial write and `argue_shift_by_band` are withdrawn.)* The row's `writes:` are
  unchanged; Partial emits `argument.held` (`16_PESSIMIST_SC_D_an_argument_moves_someone.md` edit 1) and
  nobody moves; `person_q.argued_pursuits` keeps its band test.
- Obstacle: OBS's terms (`difficulty: routine`, `opposition`, `regard` or `reception`), plus `commitment`
  (OBS member 12, first read here): `commitment_ob` (fixture, proposed 1.0, control 0) × the weight of the
  hearer's live `commit` to a Proposition contrary to the argued one (contrary: `faction_q`'s existing test
  for opposed Propositions, `[UNVERIFIED]` its name; degree weight from S1-D, 1.0 until then). What the
  arguer brings (`evidence`) is the `proofs` leverage source, levels for the roller, not an obstacle term
  (C-01, A-25; OBS §3).
- Failure: unchanged write (none); WITNESS already deposits `argument.lost` firsthand to the hearer, which
  is the record of the arguer's position. No edit.

### 2. `lie`

- Skill `deception` (U1 capability architecture §5; W3-4a: was `deceit`; until `deception`'s
  definition row lands the row carries `capability: none` with a note). The opposing key is `opposed_by:
  perception` on the `deception` **skill row** (OBS §2: "the skill the verb's skill row
  names as `opposed_by`"; `copying.opposed_by: none` is the precedent), read only by the one pool reader's
  `score()` for the counterparty's `opposition` (DICE's `10_DICE_one_score_two_roles.md`); a skill
  without it opposes with its own key, as today. No verb-row column is added.
- Obstacle: `routine` + `opposition` + `regard`. *(W3-4a, C-26: the `contradiction` term and
  `contradiction_ob` are struck: the term opened the hearer's ledger at RESOLVE, which `04` §B.2 forbids; a
  hearer who knows better is handled at WITNESS, `16_PESSIMIST_SC_E_an_honest_teller_is_not_marked.md`
  edit 1.)*
- Bands: the told deposit's confidence = `said.confidence + lie_confidence_by_band[band]` (fixture table:
  `Overwhelming 0, Success −1, Partial −2`, floored at 1); read once in `loop/witness.py`'s told deposit
  from the Event's degree. Failure: no false deposit; emits `deceit.exposed` † (in the row's Failure
  `emits:` beside `news.untold`), deposited firsthand to the hearer naming the liar as doer; its `deed:`
  alignment cells (`rosters.yaml`) lean against honesty-weighted pursuits, so `deeds_judged` and `regard`
  read it and it can ground a dispute.
- The `contests: a standing` column is unchanged; `writes:` stays empty at every band (the deposit is
  WITNESS's, by ruling, `deposit-only`), but the bands now differ in what is deposited — the corpus
  check "bands that differ" counts `emits` and deposit, and is extended to count a band-keyed fixture
  read (`harness/corpus_run.py`; `[UNVERIFIED]` its current definition counts only `writes_at`; if so the
  gate reads `emits` difference instead).

### 3. `conceal`

- Drawn, shape (a) (VRES §1 item 4: the band is the quality of one Record; no prize `a cover`): skill
  `tradecraft`; obstacle `routine` + `watch` (OBS member 22, `watch_step`, landed with
  `14_VERBS_MATERIAL_A`: the persons present at his place less himself, read from presence, never from
  other people's ledgers; W3-4a: was `notoriety`). Row: flat `writes: ["Record.exists"]`, flat `emits:` (the
  row's existing kind), a member of `graded_tasks`; the band sets `quality` 3 / 2 / 1 (a new `cover` content
  key, `rosters.yaml: record_kinds`); the failed draw is the `draw` refusal clause `cover.failed`,
  witnessed by those present.
- `_eff_conceal` reads `res.degree` → quality from a fixture table `cover_quality_by_band` (a quality step
  on one field, not a share table).
- Readers: OBS's `subject` term (member 4) reads a cover's `quality` for an inquiry whose target deed is
  anchored on a cover (`attribution.live_cover`); owner of that read: the host builder; FI's inquiry
  effects own the unmasking (named consumer).
- Ranking. *(W3-4a, C3-L10: the `concealment` score term and `conceal_rank_step` are deleted.)* `conceal`
  is ranked by its alignment cells in `rosters.yaml: tables.alignment` (CHAR's to author,
  `02_CHAR_choice_alignment.md`) and the actor's stance, `architecture/ARCHITECTURE_V2.md` §F2's score;
  what it would hide enters through formation (it forms on a referent he holds that names him), not as a
  score term. Until CHAR authors the cells, the row stays out of the ranking ("RANKING EXCLUDES").

## Exact edits, by owner, in landing order

1. `rosters.yaml`: skill cells (`lie`'s row `capability: deception` once defined, `conceal:
   tradecraft`; D-U1-07 moves them to the verb rows' `capability:` column at CAP A2/A3); `cover` key
   `quality`; `obstacle_terms` member `commitment` (OBS member 12; this file is its first reader);
   `deed:` cells for `deceit.exposed`; `graded_tasks` gains `conceal`.
2. `data/fixtures.py`: `commitment_ob`, `lie_confidence_by_band`, `cover_quality_by_band` (each a NUMBER
   row, control named). *(Deleted: `argue_shift_by_band`, `contradiction_ob`, `notoriety_step` — the one
   fixture is `watch_step` — and `conceal_rank_step`.)*
3. The skill surface (`references/descriptor_registry.yaml: capabilities`, D-U1-07): `deception` gains
   `opposed_by: perception` (the loader refuses an unknown skill key); `verb_table.yaml`: rows `lie`
   (Failure emits) and `conceal` (shape (a), `difficulty: routine`).
4. *(Deleted: `person_q.argued_pursuits` keeps its band test, C-15.)*
5. `seam/wrappers/sigma.py::contest_input`: the `commitment` operand (`watch` is already read).
6. `loop/witness.py`: the told deposit's confidence by band; `loop/effects_information.py::_eff_conceal`.
7. *(Deleted: no `decision/choose.py` edit, C3-L10.)*

## Gate (execution artifact)

- Hand-built two-arm folds, no player, 20 seeds each: (a) `argue` with the hearer holding a contrary commit
  vs not — Events' `terms` differ in `commitment` alone and the band distribution shifts; (b) `lie` at the
  four bands — the told deposit's confidence differs by band and a Failure deposits `deceit.exposed`;
  (c) `conceal` at a place where five vs zero persons stand — differ in `watch`, and quality distributions
  differ.
- Corpus run: `lie`'s bands differ; `argue`'s Partial emits `argument.held` and writes nothing (C-15).
- `aperture 2 s`: `conceal` formed and attempted counts reported; its formation set (a referent he holds
  that names him) is the reading, not a score term (C3-L10).

## Falsifier

A `lie` Failure with no `deceit.exposed` in the hearer's ledger; a Partial `argue` that writes (C-15); a
cover whose quality is the same for every band; a `lie` term that reads the hearer's ledger at RESOLVE;
any of the three whose band distribution does not move when its named term moves. Control: every new
fixture 0 reproduces the post-SC-OB hash.

## NERS reading

- **N:** persuasion and deceit are the social contest's two most-formed verbs (corpus 947 and 138 graded);
  their bands must mean different things.
- **R:** a caught liar pays; a committed hearer resists; a well-made cover protects; each with nobody
  watching, each by a draw.
- **S:** one obstacle composition; one told channel; quality enters inquiries through SC-OB's existing
  `subject` term.
- **E, last:** one new term, one capability-row key, a handful of band tables.

## Cost class

Small build. Lanes: SC (seam operands), DICE (`opposed_by`, keys), FI (consumer).
