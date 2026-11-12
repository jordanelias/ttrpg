# The social obstacle: the task's difficulty plus named modifiers, each recorded on the roll

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-01 to C-04, C-33) — four readings change; the term list and the reason trail stand. (1) No term is subtracted: the favourable halves of `evidence`, `reception` and `regard` reach the roll as `proofs` and `favour` levels (Jordan, A-25; `16_PESSIMIST_SC_A_what_the_speaker_brings_is_leverage.md` edits 1 to 5), so edit 1's subtract-after-ceiling step and `proof_step` are not built. (2) The roster, the binding table and the record field are `U5c_SC_one_obstacle_form.md` §1's: one `obstacle_operands` tuple in place of edit 4's field per term. (3) `opposition` is never absent: `obstacle_default` is deleted and every rolled row is `routine` at the control arm, in place of edit 2's `demanding` rows. (4) The Status line's "supersedes `05_SC_opposed_obstacle_parity.md`" no longer holds: Jordan's A-26 un-holds that file and it carries the opposition rate.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.4 row SC-B, §2 row SC-B, §3 rows *obstacle form*, *roster*, *row difficulty values*, *margin_endings*; `unified/U1_OWNERS_AND_VOCABULARY.md` D-U1-02, D-U1-04, ledger R-16 to R-20, R-29; `unified/U1_GLOSSARY.md` *difficulty level*; `unified/U3_CONFLICT_LEDGER.md` C3-L5, §9). **SUPERSEDED in part by `U5c_SC_one_obstacle_form.md` (OBS).** The stale body is removed, not left beside the head: the form `bound(…) − favourable`, the ten-member term table, the bound-then-subtract rule, the parity survival table (its score/2 premise is overtaken by A-26 and A-79) and edits 1, 3, 4, 5 and 6 are deleted and replaced by a pointer table to OBS. Two edits survive and are stated here: the verb row's `difficulty:` column (as D-U1-04 decides it: control `routine` on every rolled row, OBS §4 step 1a, replacing this file's `demanding` rows) and `Margin.terms` (the reason line, OBS §5, carried on the Event by SC-P1). The NPC-versus-NPC paragraph and the reason-line example stand, the example restated with no subtracted term. Lands-it and tier added. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "Ob" → "obstacle" in prose (glossary *obstacle*).

**Lands in batch:** B05 (with OBS steps 1a and 2). **Depends on:** `U5c_SC_one_obstacle_form.md` (B05); `05_SC_contest_record_on_event.md` (B05); `01_CORE_capability_authoring_surface.md` (B04, the column's refusal shape).

## Status: PROPOSED (two edits: the `difficulty:` column and `Margin.terms`; the rest SUPERSEDED by `U5c_SC_one_obstacle_form.md`)

Source: Jordan's clarification of 2026-11-12, as relayed to this lane by the orchestrator: *the social
contest obstacle is defined by the difficulty of the task and all associated modifiers; it is not a
flat 2 and not the opponent's score alone*. This lane has not seen it in a ledger; the orchestrator
owns its recording. Also `audits/05_SC_audit_addendum_B.md` §B8 and F-SC-16; `audits/05_SC_audit.md`
F-SC-03, F-SC-04; hole rows H-127, H-213, H-267, H-288.

## What it changes in `engine/season/` at runtime

Every contested social act and graded inquiry composes its obstacle as
`difficulty + modifiers`, in one function, and returns the terms it summed. At the control arm
(`regard_step` 0, every `stakes_ob` entry 0, every `standard` `plain`) the composed obstacle equals
today's (2) for every act in the shipped realm whose counterparty holds no score, for every `speak`
(its subject is a `DocketItem`, so it has no opposition today or after) and for every graded
inquiry. It moves (declared) for an act against a person who holds a score (two of 83 persons at
seed 0, first audit §12 run 11) and, at the proposed arm, for any act whose counterparty holds a
stance row toward the actor or whose disposal is `detain` or `ban`. Every Event of a rolled act
gains the term list (with SC-P1).

*Corrected on completion (Opus, 2026-11-12):* an earlier text of this paragraph listed the self-plea
as moving and edit 2 gave `speak` `routine` and `interrogate` `demanding`. Checked against
`verb_table.yaml` (`speak.requires_typed` is `kind: DocketItem`, no `counterparty:`;
`interrogate.counterparty: subject`, a held person) and `sigma.py::contest_input:210`: those values
would have moved every `speak` from 2 to 1 and every `interrogate` from 2 to 3 at the control arm.
Edit 2 now carries the values that reproduce today's obstacle.

## The problem (evidence)

- `modules/social_contest/roll.py::obstacle` (`:141`) starts from `opposition / 2.0`, or from
  `obstacle_default` (2) where the subject has no score. The act itself contributes nothing: a lie,
  a plea before a tribunal and a question to a neighbour share one base. In the realm nobody holds a
  score, so the base is the flat 2 everywhere (first audit F-SC-03).
- A held score of 2 composes obstacle 1.0 and no score composes 2.0 (H-127's inversion, reproduced by the
  first audit and by `10_DICE_one_score_two_roles.md`).
- The room's terms are subtracted before the ceiling, so against a strong opponent they vanish:
  pool 2 against a score of 8, proofs 0 to 4, obstacle 2.842 and odds (0.900, 0.081, 0.019, 0.000) in
  every row (addendum §B7 run 3).
- A hearer's regard for the speaker does not enter `argue`, `tell` or `lie` (H-267); the weight of
  what is sought does not enter `determine`; the room's own standard does not exist.
- The roll's reasons are not kept: `Margin` is `(net, ob)`; `Event` holds the band (first audit
  F-SC-04, H-284).

## The resolution, decided

The form, the roster, the bound and the leverage channel are OBS's (`U5c_SC_one_obstacle_form.md` §1–§3):
`hard = even + difficulty + opposed_ob(trained score or pool_default, opposition_rate) + Σ raw_i × step_i`,
`ob = max(OB_MIN, min(hard, cap(pool)))`; nothing is subtracted (A-25); what a party brings is leverage.
What this file first wrote, and where each part now lives:

| first written here | now |
|---|---|
| `Ob = bound(… + hostile) − favourable` | OBS §2 (A-25: nothing lowers the obstacle) |
| the ten-member `obstacle_terms` roster | OBS §2's roster, `even` first (C-02); `evidence` is leverage (`proofs`, OBS §3) |
| `opposition` as score ÷ 2, "never practice", "the larger of key and attribute" | `opposed_ob(skill score, opposition_rate)`, 0.4 per point at the live arm (A-26, A-79, D-U1-02); no attribute in the score (A-7) |
| `regard` signed, `regard_step` 0.04 | OBS §2 member 7 (hostile half only) and the `favour` level (OBS §3); `regard_step` sized at OBS §4 step 5 |
| `evidence` and `proof_step` | the `proofs` leverage source; `proof_step` deleted (OBS §3) |
| the bound applied before subtracting | OBS §2 (the bound acts on the composed obstacle; leverage is soft-capped separately) |
| SC-P5's survival table | void: `05_SC_opposed_obstacle_parity.md` is un-held by A-26 and carries the rate |
| `SocialContestInput` per-term fields (edit 4) | one `obstacle_operands` tuple (OBS §1) |

### Edit A · the `difficulty:` column (surviving edit 2, as decided)

`engine/season/verb_table.yaml` and `data/verbs.py`: a `difficulty:` column on every rolled row, naming a
**difficulty level**, a member of `rosters.yaml: difficulty_levels` (`plain, routine, demanding, hard`);
each level's size is `Fixtures.difficulty_ob` (control 0 / 1 / 2 / 3, NUMBER row in `hole_register.yaml`). The
loader refuses a contested or graded row without one and a row that is neither with one (the refusal shape
`01_CORE_capability_authoring_surface.md` edit 3 gives `capability:`). At the control arm **every rolled
row is `routine`** (OBS §4 step 1a; C-04): `routine` 1 + the stand-in `opposed_ob(pool_default)` 1.0 = 2.0,
today's obstacle, for a row with no person opposite as for one with an unscored person opposite. Lane A's
interim `rosters.yaml: task_difficulty` retires into this column in the same commit (D-U1-04). A designer
who judges a lie harder than a telling edits one cell; the calibrated values are OBS §4 step 5's.

### Edit B · `Margin.terms` (surviving)

`queries/inputs.py::Margin` gains `terms: tuple`, `((name, value), …)` in roster order, composed by the
module with the obstacle, plus `("ceiling", −clip)` and `("floor", +lift)` when a bound acted, so that the
values sum to `ob`; `sigma.resolve`'s result gains `levels` (OBS §5). SC-P1's roster `margin_endings` carries
`terms` and `levels` in place of its single `room` field (C-06), so every rolled Event says, in the log and
after a load, *obstacle 3.7 = even 2.4 + difficulty 0.5 + opposition 0.8; leverage: proofs +2, favour +1*. The
harness prints that line where it prints the degree. Person-side, `believed_input` fills what a person can
know: `difficulty`, `standard` and `stakes` are public data and always known; `opposition`, `regard`,
`reception` and the other side's answers are his claims or unknown (`10_DICE_believed_odds_have_a_prior.md`
decides what unknown means).

### How an NPC-versus-NPC contest gets its obstacle

By the same function with no branch. The actor is whoever chose the act; the counterparty is the
operand the verb row names (`loop/sides.py::sides_of`). The host builder reads: the row's
`difficulty`; the counterparty's skill score and his stance toward the actor; the docketed row's
`standard` and `disposes` kind where a bench hears; the actor's cited items (formed as Candidate
variants by the one chooser, `08_FI_05` edit 3) and the other side's standing answers. No field
depends on a player, and none on which of the two is "the NPC": two courtiers arguing in an empty
hall, a prosecutor before a bench of three, and a player's plea are three inputs to one composition.
Where both want to move each other, each makes his own act and each act has its own obstacle; there
is no shared roll.

## Gate (execution artifacts)

- Edit A: `build_realm(0)`, one season, at the control arm: a printed count of rolled acts whose obstacle
  differs from the base commit, each with its terms; expected zero, or only acts against a holder of the read
  key (OBS gate 3, named test `engine/season/tests/test_obstacle_form.py::test_step_1a_composes_todays_obstacle_at_control`).
  `test_a_rolled_row_with_no_difficulty_is_refused` (new, same file).
- Edit B: over a lattice of quarter-step operands the returned terms sum exactly to the returned obstacle
  and every name is a roster member (OBS gate 1, `test_obstacle_form.py::test_terms_sum_to_ob`).
- A hand-built fold with no player: two NPCs, one `argue`, the hearer holding one stance row toward
  the arguer, `(arguer, +4, 1)` in one arm and `(arguer, −4, 1)` in the other; the hostile arm's `terms`
  show `regard`, the friendly arm's `levels` show `favour` and its `terms` show no `regard` (OBS gate 5).

## Falsifier

A rolled row the loader admits with no `difficulty:`. A realm act whose obstacle moved at the control arm and
whose counterparty holds no score. A `terms` tuple that does not sum to `ob`, or that holds a negative entry
other than `ceiling`.

## NERS reading

- **N**: top-down a designer sets how hard an act is by naming a level on its row; bottom-up every
  term reads a fact that exists; lateral combat already derives its obstacle from the defender plus
  the instance; diagonal a room's standard and a disposal's weight reach one person's roll.
- **R**: characters differ (score, stance), rooms differ (standard, reception), cases differ
  (evidence, stakes), and each difference is visible afterwards.
- **S**: one composition for a telling, a hearing and an inquiry (OBS's); `regard` and `reception` are one
  quantity at two audiences and never both apply.
- **E**, last: one column and one tuple on the margin, against an obstacle a player and a chronicle can read.

## Cost class

Edit A: edit (a column and a loader refusal; hash-equal at control). Edit B: small build (with OBS steps 1a–2).

**Lands it and tier.** The B05 batch with OBS, SC and IN lanes: `valoria-author` on `sonnet` (`high`), one
`methodology-close` with its terminal `opus` critique for the batch. **Hash movers.** Edit A none at control;
Edit B is OBS step 2's declared mover (every Event of a social roll gains the tuple).
