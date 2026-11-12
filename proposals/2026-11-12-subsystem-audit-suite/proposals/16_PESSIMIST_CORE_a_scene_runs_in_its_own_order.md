# 16 · PESSIMIST · CORE — a scene runs in its own order, and its second step may depend on its first

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` §1) — **no longer held.** Jordan answered D-09 on 2026-11-12 (A-9): a scene is a short sequence (Option B). Edits 1–4 are the plan. Edit 5 (the Layer-1 text: #353 §27's order restated over scenes) is drafted by the unification stage and applied only by Jordan's amendment, never by an implementation lane. The rival-acts precedence draw (`18_DETERMINISM_rival_acts_in_one_fold.md`) re-orders scenes, not acts, once this lands.

Folded: 2026-11-12 by `audits/28_SCENE_ACCESS.md` (rulings A-63, A-64). Nothing here is deleted; the engagement half this file left without an edit is carried by `28_CORE_scene_access_A_occupancy_and_precedence.md`, at two of this file's sites. (1) **Edit 1's scene order gains a rivalry key**: the scenes that claim one person's round (his own, and each scene holding a face-to-face interaction that names him) are re-ordered among the positions they already hold by a precedence draw weighted by office rank and a kept appointment. (2) **Edit 3's fold gains a second new clause beside `sequence`, `engaged`**: a face-to-face interaction whose counterparty is already in another scene this round, or has no scene action left this season, is refused and emits `visitor.kept_waiting`, which WITNESS deposits as a claim about the person he came to see in both their ledgers (A-81: the refused call is not a still scene); a row whose prize is `the body` is never refused there (A-80: a closed door stops talk, not force); a person received before his own scene folds has that scene deferred to his next round, and the scene he was received in is subtracted by the budget Query (A-62: no stored number, no receipt). (3) **The figure in this file's source is restated**: 62 of 87 reproduces at `e1d6180` and counts every executed act whose payload names a person (`create_record` 46, `utter` 28, `reconstruct` 25); by the verb row's `counterparty:` it is 32 of 50, and by the rows whose cell requires the two in one place the realm executes 24, 42 and 31 meetings in two seasons at seeds 0, 1, 2 (audit §1). (4) This file's control arm is also engagement's: `engagement: off` must reproduce this file's hashes.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: `R5_READ.md` §2 (Status after A-9; edit 3 under A-81
and A-62), §1 (P:1 resolved by A-9, `04` not edited; P:2 the `sequence` clause declared per `04` §B.13 inv. 4; P:3
VIOLATES as written against `04` §C.4 `:668-676`, rewritten so a step after a deferred prize is deferred with it),
§7/§7b (encoding of `after`, `act_of` located, tests, tier); U3 B08, C3-K8 (this file's edit 1 is the first of three
edits to `_canonical_order`), §4.1 row 32; U1 glossary *interaction* (prose says "interaction"; "step" only where A-9
is quoted). Changed: the Status line; "The two options" marked SUPERSEDED (kept as the finding); edits 2-3; gate.
Corrected from R5 7b: the `sequence` kind is not one roster key in `verb_table.yaml` (that file holds only `verbs:`);
it is a clause the loader already knows how to require, per row (`data/verbs.py:340-358`).
Reconciled: 2026-11-12, wave-3 mop-up (`unified/work/W3_2_DONE.md` last row; `unified/U1_GLOSSARY.md` *occupy*): the folded lane-28 sentences say *engaged* (clause `engaged`, fixture `engagement: off`) where they said `occupied` / `occupancy: off`; the file name of the 28A head keeps "occupancy".

## Status: PROPOSED (A-9 taken: Option B is the plan; edit 5 is Layer 1 text drafted by the unification stage, owed in `unified/OWED_TO_UNIFICATION.md` §A row 1, applied only by Jordan)

Lands in batch: **B08** (IN; one re-pin). Depends on: nothing unlanded for edits 1-4 (A-9 is the authority for the
code; the Layer 1 restatement is the spec's catch-up and the code lands behind `interactions_per_scene = 1` as the
control until it is applied). Serial edge on `loop/resolve.py::_canonical_order` (C3-K8): this file's edit 1 first,
then `18_DETERMINISM_rival_acts_in_one_fold.md` (B08), then `28_CORE_scene_access_A_occupancy_and_precedence.md`'s
person key (B28).

Carries F-PES-CORE-06 of `audits/16_PESSIMIST_CORE.md` (§1.1). Reference only (CLAUDE.md §0.05).

## What it changes in `engine/season/` at runtime (first)

RESOLVE folds each scene's interactions contiguously and in the order the chooser composed them, and an
interaction may declare that it is attempted only if the one before it reached a named band (A-9: "a
scene's steps apply in the chooser's order and a step may hang on the band of the one before"). Scenes are
ordered among themselves by the present key (stratum, then the content hash), read off each scene's first
interaction.

## The problem (evidence; `build_realm(0)`, two seasons, hash `bacd687f…`)

- `loop/resolve.py:51-58` sorts every act of a round by `(stratum_of(a), H(seed, tick, actor,
  "order:verb:act id"))` over one global array. The scene an act belongs to is not a key.
- 525 scenes with two or three folded interactions: **120 (23%) fold in the scene's own order**, which is
  what chance gives. A scene composed `create_record, challenge, utter` resolves in whatever order the
  hash deals.
- All of a scene's interactions are chosen before any resolves (`decision/choose.py::pack_scenes` returns
  the whole `Scene`), so no interaction can be conditional on the outcome of an earlier one.
- **R-09's statement** (`requirements.yaml:1567`): *"chains of events within a scene are probabilistic,
  not deterministic."* There is no chain within a scene: the unit has no internal order and no internal
  dependence, so the requirement's subject does not exist in the engine. The row's `partial` is measured
  on whether a roll reaches a single act.
- The strata, which are what the global order protects, decided nothing at seed 0: with every act in one
  stratum, 0 of 821 acts changed outcome in a season; with the hash order reversed inside each stratum,
  1 of 175 round-0 acts did (`ordp.py 0 1`).

## The two options (SUPERSEDED by A-9, 2026-11-12: Jordan took B; kept as the finding)

**Option A — a scene is a budget unit, and stays one.** Keep the global order. A scene is "one to three
things a person does this round, simultaneously with everyone else's". Then R-09's wording is re-pointed
at chains *across* scenes (round to round), the word *scene* is defined at both sites (CLAUDE.md §4) as a
budget unit with no internal order, and the play surface must not show a player his three picks as a
sequence. Cost: an edit to two definitions. What is lost: the tabletop scene (*I question him; if he
breaks, I accuse him; if not, I leave*), which is the unit the detective and trial precedents in
`AUDIT_BRIEF.md` are made of.

**Option B — a scene is a short sequence (this proposal's edits).** The chooser's order is the order of
resolution, and a later step can hang on an earlier one's band. Then R-09 has a subject: a three-step
scene is a chain of up to three draws, each conditioning the next. What is lost: the property that all
acts of a round fold over one array keyed only by stratum and hash (#353 §27; the roster `strata` in
`architecture/meta/08_DATA_AND_KEYS.md:16`), and with it the guarantee that a `movement` act anywhere
precedes a `social` act anywhere. Measured, that guarantee decided no outcome in a season.

**This lane's recommendation: B**, on three grounds: R-09 is a ruled requirement and has no subject
under A; the standing rule (*a thing that could go either way goes by a draw*) wants more chained draws,
not fewer; and the ordering it gives up is, by execution, not doing anything. It is Jordan's because it
edits what Layer 1 ratifies.

## Exact edits, by owner (Option B)

1. **`engine/season/loop/resolve.py::_canonical_order`** — order *scenes*, then flatten:
   key each scene by `(stratum_of(first interaction), H(seed, tick, actor, "order:scene:<scene id>"))`;
   an act with no scene (`a.scene is None`, the pre-`W17` bare Act) is its own one-act scene, so every
   existing caller and probe is unchanged. `encounter.py` imports the same function and inherits it.
2. **`engine/season/state/carriers.py::Act`** — one optional field,
   `after: Optional[tuple[str, ...]] = None`: the band labels (members of
   `engine/dice_engine/dice_engine.py::DEGREE_LABEL`'s values, the strings the verb table keys degrees by) of
   the scene's previous interaction at which this one is attempted (`None`: always, today's behaviour). Read
   by the fold only (ID-13: a field with its reader in the same commit).
3. **`engine/season/loop/resolve.py::resolve`** — before folding an act whose `after` is set, read the
   degree the previous interaction of its scene just produced (the driver holds `self.act_of`,
   `loop/driver.py:324`, and the Events in hand); outside the named bands, emit the row's refusal kind for a
   new clause `sequence`, so the skipped interaction is in the log and costs its slot.
   - **The clause is declared, not invented at the fold** (`04` §B.13 inv. 4; `data/verbs.py:340-358`,
     `refusal_for`: a keyed row raises on an unkeyed clause). `data/verbs.py` gains `SEQUENCE_CLAUSE =
     "sequence"` beside `ELIGIBILITY_CLAUSE`, `WRITE_CLAUSE`, `COUNTERPARTY_CLAUSE`; a **flat** row answers its
     flat kind for it already; a **keyed** row must key `sequence:` and the loader refuses one that does not
     (the count is reported in the commit; every keyed row can be a second interaction, so the rule is
     per row, not per verb named).
   - **The refusal Event carries no `changes[]`** (A-62: the budget is a Query). The scene is not still
     (A-81): its first interaction already wrote, or emitted at `Failure: []` (`04` `:724-728`, "the act
     still **emits**"), and that Event is the scene's durable write.
   - **A deferred prize defers what hangs on it** (`04` §C.4 `:668-676`: a contested prize that defers to a
     later step is folded at RESOLVE "at its declared band, writing nothing", and the real contest runs when
     the same fold runs again from ENCOUNTER). If the previous interaction's prize is deferred, an act whose
     `after` is set is deferred with it, and its `after` is read against the degree ENCOUNTER produces;
     `encounter.py` re-runs the same fold, so no second code path is built. Without this, the step would
     hang on a band that was never fought.
4. **`engine/season/decision/choose.py::pack_scenes`** — when packing a contested interaction followed
   by one on the same subject, set `after` from the row's own `writes_by_degree` (the bands in which the
   first wrote anything). No verb is named; the rule reads the row.
5. **`architecture/meta/`** (Layer 1; only on Jordan's amendment, A-9 having ruled the substance) — the §27
   order restated as *strata and hash over scenes*; `04` §C.4 `:662`'s key `(stratum, actor-hash,
   intra-person position)` read over scenes. Drafted by the unification stage (`OWED_TO_UNIFICATION.md` §A
   row 1); no implementation lane edits `04`.

Order of edits: 2 (the field) → 3 (its reader, with the loader clause) → 1 (the scene key) → 4 (the
chooser sets `after`), each its own commit; one re-pin at the batch close.

## Gate (an execution artifact, §0.2)

NEW `engine/season/tests/test_scene_sequence.py`: `test_scene_folds_contiguously_in_chooser_order`,
`test_second_step_skipped_when_first_misses_band_logs_sequence_refusal` (the refusal Event's `changes` is
empty and the first interaction's Event stands), `test_deferred_first_step_defers_second` (a planted
`[challenge, fight]` scene at the deferred band), `test_keyed_row_without_sequence_key_is_refused_at_load`,
`test_one_interaction_per_scene_hash_equals_today`. Command:
`python -m pytest engine/season/tests/test_scene_sequence.py -q`; then
`python -m engine.season.harness.report && python -m engine.season.harness.delta HEAD`. The table's readings
are read by `harness/aperture.py` `[ASSUMPTION: the nearest existing per-act census — basis: the harness
listing]`; the `ordp.py` arm was lane scratch (not in the repository, U3 §6.2) and is reported only if
re-written as a committed reading. When `harness/access.py --null-scenes` lands (28A, B28) it counts a scene
whose second interaction was skipped as not null (its first interaction's Event is the write).

| reading (`build_realm(0)`, two seasons) | today | passes when |
|---|---|---|
| multi-interaction scenes folded in their own order | 23% | 100% |
| acts with `after` set that were skipped because the prior interaction missed its band | — | greater than 0, and each has a logged refusal with clause `sequence` |
| control: `after` never set and one-act scenes only (`interactions_per_scene = 1`) | — | content hash equal to today's at that fixture |
| the strata-cut arm (`ordp.py`, scratch) | 0 flips | reported, whatever it is, once committed |

## Falsifier

At `interactions_per_scene = 1` the hash moves: the re-keying changed more than the order within scenes.

## NERS reading (E last)

- **N.** Cut within-scene order (today's state) and what dies is the chain R-09 names. From the top
  (the requirement), from the bottom (the chooser already composes an order that is then discarded), and
  laterally (the fight module resolves exchanges in order inside one act; a scene is the same idea one
  level up): three directions.
- **R.** A scene whose second step is conditional is the smallest unit in which a person's plan can go
  wrong in the middle, with nobody watching.
- **S.** *Zooms out and in*: a scene becomes the same shape as a bout (ordered exchanges, each a draw).
- **E.** One sort key and one optional field, against a unit whose name promises an order it does not
  have.

## Cost class

Small build (the ruling is A-9). Golden re-record at any fixture with more than one interaction per scene:
say so plainly. Hash movers declared: every seeded result with more than one interaction per scene (one
re-pin at B08's close); control `interactions_per_scene = 1` hash-equal. Tier: `opus` for the deferred-prize
case and the `after` encoding (the judgment node), then `sonnet`, effort `high`, for the edits and tests.
Lands it: B08, before `18_DETERMINISM_rival_acts_in_one_fold.md`.
