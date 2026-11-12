# VERBS SOCIAL1 · C — persuasion and deceit: `argue`, `lie`, `conceal` drawn with a reason on every band

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-15, C-26) — three changes. (1) `argue`'s Partial write is withdrawn: the band is `argument.held` and nobody moves (`16_PESSIMIST_SC_D_an_argument_moves_someone.md` edit 1). (2) `lie`: the capability is `deception`; the `contradiction` term is dropped, because it opens the hearer's ledger at RESOLVE (`04` §B.2) and a hearer who knows better is already handled at WITNESS (`16_PESSIMIST_SC_E_an_honest_teller_is_not_marked.md` edit 1); `deceit.exposed` at Failure stands. (3) `conceal`'s `notoriety` term is the roster member `watch`, read from presence and not from other people's ledgers; `a cover` is not a prize (`U5c_VERBS_residue_and_governance_owner.md` §1, §2).

## Status: PROPOSED

Batch S1-C of `audits/14_VERBS_SOCIAL1.md` §14. Authored in part by Fable; completed by Opus after the
Fable usage limit (2026-11-12). Reference only (CLAUDE.md §0.05). Read at `84d2a02`. Needs SC-OB
(`05_SC_obstacle_difficulty_and_modifiers_B.md`) and lane A steps 3–4 (persons hold scores; one score,
two roles).

## What it changes in `engine/season/` at runtime

`argue`'s Partial band writes; `argue` gains a `commitment` obstacle term. `lie` gains its own capability,
an opposing key, a `contradiction` term, a confidence that follows the band, and a Failure that deposits a
deed. `conceal` becomes drawn (cover quality by band, a Failure that is witnessed) and is ranked by what it
would hide. Declared hash mover.

## The problem, with evidence

- `argue`: Partial emits `argument.won` and writes nothing (`verb_table.yaml:133` row; `_eff_argue` runs
  only on bands whose `writes:` is non-empty); pool 2 for every actor (`aperture 1 0` POOLS ROLLED); a
  hearer's commitments do not enter the roll.
- `lie`: `[corpus]` "bands that differ: False"; Failure (110 of 138 graded) deposits nothing but
  `news.untold`; no capability row; the hearer's own firsthand knowledge of the cell does not enter the roll
  (H-183 counts it against the liar only after the fact).
- `conceal`: "RANKING EXCLUDES" (no celled axis: chosen by the draw's tie-break, not a reason); cover quality
  does not exist, so an inquiry cannot be harder against a better cover; the mint is certain — a fixed
  function of state, against `AUDIT_BRIEF.md`'s Standing rule.

## The resolution, decided

### 1. `argue`

- Row `writes:` Partial gains `Person.pursuits`; `emits:` unchanged (Partial's `argument.won` now has a
  write behind it). `person_q.argued_pursuits` takes the band's factor from a fixture table
  `argue_shift_by_band` (`Overwhelming 2, Success 1, Partial 0.5`), replacing the band test inside it.
- Obstacle: SC-OB's terms as listed there (`difficulty: routine`, `opposition`, `regard` or `reception`,
  `evidence`), plus `commitment` †: `commitment_ob` (fixture, proposed 1.0, control 0) × the weight of the
  hearer's live `commit` to a Proposition contrary to the argued one (contrary: `faction_q`'s existing test
  for opposed Propositions, `[UNVERIFIED]` its name; degree weight from S1-D, 1.0 until then).
- Failure: unchanged write (none); WITNESS already deposits `argument.lost` firsthand to the hearer, which
  is the record of the arguer's position. No edit.

### 2. `lie`

- `verb_capability`: `lie: deceit`. New row column `opposed_by:` (`lie: perception`), read only by the one
  pool reader's `score()` for the counterparty's `opposition` (DICE's `10_DICE_one_score_two_roles.md`); a
  row without it opposes with its own key, as today.
- Obstacle: `routine` + `opposition` + `regard` + `contradiction` †: `contradiction_ob` (proposed 1.0,
  control 0) when the hearer holds the lied-about cell firsthand (the host builds the counterparty's side
  and may read his ledger; SC-OB "how an NPC-versus-NPC contest gets its obstacle").
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

- Drawn: `verb_capability: conceal: tradecraft`; obstacle `routine` + `notoriety` † (`notoriety_step`
  × the number of persons at his place holding a firsthand claim of him — read by the host at the act's
  place; control 0). Row made Degree-keyed: Overwhelming/Success/Partial write `Record.exists` with
  `quality` 3/2/1 (a new `cover` content key, `rosters.yaml: record_kinds`); Failure writes nothing and
  emits `cover.failed` †, deposited to those present.
- `_eff_conceal` reads `res.degree` → quality from a fixture table `cover_quality_by_band`.
- Readers: SC-OB's `subject` term reads a cover's `quality` for an inquiry whose target deed is anchored on
  a cover (`attribution.live_cover`); owner of that read: SC-OB's host builder; FI's inquiry effects own the
  unmasking (named consumer).
- Ranking: `decision/choose.py` adds a `concealment` term for `conceal` Candidates = the largest
  `violated_affiliations`/`violated_pursuits` weight among the same person's other Candidates in this
  deliberation (person-side; no celled axis invented; `conceal_rank_step`, control 0 = today's tie-break).

## Exact edits, by owner, in landing order

1. `rosters.yaml`: `verb_capability` rows (`lie: deceit`, `conceal: tradecraft`); `cover` key `quality`;
   `obstacle_terms` members `commitment`, `contradiction`, `notoriety`; `deed:` cells for `deceit.exposed`.
2. `data/fixtures.py`: `argue_shift_by_band`, `commitment_ob`, `contradiction_ob`,
   `lie_confidence_by_band`, `notoriety_step`, `cover_quality_by_band`, `conceal_rank_step` (each a NUMBER
   row, control named).
3. `data/verbs.py` + `verb_table.yaml`: the `opposed_by:` column (loader refuses an unknown capability key);
   rows `argue` (Partial write), `lie` (`opposed_by`, Failure emits), `conceal` (Degree-keyed, `contests:
   "a cover"`, `difficulty: routine`).
4. `queries/person_q.py::argued_pursuits` (band factor from the table).
5. `seam/wrappers/sigma.py::contest_input`: `commitment`, `contradiction`, `notoriety` operands.
6. `loop/witness.py`: the told deposit's confidence by band; `loop/effects_information.py::_eff_conceal`.
7. `decision/choose.py`: the `concealment` term.

## Gate (execution artifact)

- Hand-built two-arm folds, no player, 20 seeds each: (a) `argue` with the hearer holding a contrary commit
  vs not — Events' `terms` differ in `commitment` alone and the band distribution shifts; (b) `lie` with the
  hearer holding the cell firsthand vs not — differ in `contradiction` alone; (c) `conceal` at a place where
  five vs zero persons know him — differ in `notoriety`, and quality distributions differ.
- Corpus run: `lie`'s bands differ; `argue`'s Partial writes `pursuit.moved`.
- `aperture 2 s`: `conceal` attempts co-occur with a judgeable act in the same deliberation in ≥ 0.8 of
  attempts versus the control (`conceal_rank_step` 0).

## Falsifier

A `lie` Failure with no `deceit.exposed` in the hearer's ledger; a Partial `argue` with no write; a cover
whose quality is the same for every band; any of the three whose band distribution does not move when its
named term moves. Control: every new fixture 0 reproduces the post-SC-OB hash.

## NERS reading

- **N:** persuasion and deceit are the social contest's two most-formed verbs (corpus 947 and 138 graded);
  their bands must mean different things.
- **R:** a caught liar pays; a committed hearer resists; a well-made cover protects; each with nobody
  watching, each by a draw.
- **S:** one obstacle composition; one told channel; quality enters inquiries through SC-OB's existing
  `subject` term.
- **E, last:** three new terms, one column, a handful of band tables.

## Cost class

Small build. Lanes: SC (seam operands), DICE (`opposed_by`, keys), CORE (`choose`), FI (consumer).
