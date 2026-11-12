# The social obstacle: the task's difficulty plus named modifiers, each recorded on the roll

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-01 to C-04, C-33) — four readings change; the term list and the reason trail stand. (1) No term is subtracted: the favourable halves of `evidence`, `reception` and `regard` reach the roll as `proofs` and `favour` levels (Jordan, A-25; `16_PESSIMIST_SC_A_what_the_speaker_brings_is_leverage.md` edits 1 to 5), so edit 1's subtract-after-ceiling step and `proof_step` are not built. (2) The roster, the binding table and the record field are `U5c_SC_one_obstacle_form.md` §1's: one `obstacle_operands` tuple in place of edit 4's field per term. (3) `opposition` is never absent: `obstacle_default` is deleted and every rolled row is `routine` at the control arm, in place of edit 2's `demanding` rows. (4) The Status line's "supersedes `05_SC_opposed_obstacle_parity.md`" no longer holds: Jordan's A-26 un-holds that file and it carries the opposition rate.

## Status: PROPOSED — supersedes `05_SC_opposed_obstacle_parity.md` (SC-P5, HELD BACK). Decision-ready for the implementation lane.

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
- A held score of 2 composes Ob 1.0 and no score composes 2.0 (H-127's inversion, reproduced by the
  first audit and by `10_DICE_one_score_two_roles.md`).
- The room's terms are subtracted before the ceiling, so against a strong opponent they vanish:
  pool 2 against a score of 8, proofs 0 to 4, obstacle 2.842 and odds (0.900, 0.081, 0.019, 0.000) in
  every row (addendum §B7 run 3).
- A hearer's regard for the speaker does not enter `argue`, `tell` or `lie` (H-267); the weight of
  what is sought does not enter `determine`; the room's own standard does not exist.
- The roll's reasons are not kept: `Margin` is `(net, ob)`; `Event` holds the band (first audit
  F-SC-04, H-284).

## The resolution, decided

### The form

```
Ob = bound( difficulty + opposition + standard + subject + stakes + hostile )  −  favourable
```

One owner composes it (`modules/social_contest/roll.py::obstacle`, as `ED-SC-0033` clause 3 rules).
The host carries every operand raw. The ruled sentence of 2026-08-14 (*"their corresponding score/2
plus whatever specific modifiers exist for them in that instance"*) is kept whole: it is the
`opposition` term and the modifiers; what is added is the term it did not name, the task.

### The terms (a closed, ordered roster: `rosters.yaml: obstacle_terms`)

All terms are in obstacle units (net successes; one die nets `MU_PER_DIE` 0.4 on average).

| term | what it is | read from (the single owner of the fact) | value | sign | applies to |
|---|---|---|---|---|---|
| `difficulty` | how hard the act is in itself | `verb_table.yaml`, a `difficulty:` column on every contested or graded row, naming a member of `rosters.yaml: difficulty_levels`; the level's size is the fixture table `difficulty_ob` | proposed `plain` 0, `routine` 1, `demanding` 2, `hard` 3 | + | every rolled act |
| `opposition` | the person acted against | the counterparty's score for the verb's capability, through the one pool reader's base (`10_DICE_one_score_two_roles.md`'s `score()`: the larger of key and attribute, else `pool_default`; never practice), halved by the one owner of the ruled divisor, `sigma_leverage.opposed_ob` (`10_DICE_capability_axiom_map.md` §G edit 5, shared with combat's `core.ob_from_defender`) | score ÷ 2 (ruled) | + | an act with a person counterparty; absent for a non-person subject (a `DocketItem`, a Record, a site) and for a self-plea |
| `standard` | what the room demands before it will be moved | the docketed arrangement row (or its rite), a `standard:` key naming a `difficulty_levels` member | the level's size; `plain` (0) on every seeded row until authored | + | an act heard by a bench (`heard_by: bench`) |
| `subject` | what the thing examined puts in the way | `Record.forgery_quality` of an examined Record (today's operand, unchanged); a cover's quality when FI lands one | as stored | + | graded inquiries |
| `stakes` | the weight of what the act would do to the other party | the fixture table `stakes_ob`, keyed by the Tenure kind the act opens or closes (for `determine`, the kind the row `disposes:` at Success; for `arrest`, `detain`) | proposed `oblige` 0, `detain` 0.5, `ban` 1 | + | acts that open or close a restraint on the counterparty |
| `regard` | how the one acted upon is disposed to the actor | the counterparty's own stance toward the actor, read by its one owner `queries/person_q.py::stance_toward(counterparty, actor)` (Σ valence × weight over his rows naming the actor; his interior, the same kind of read as his score; no ledger), times the fixture `regard_step`, sign reversed | `stance_toward` spans −25…+25 per row (valence −5…+5 × weight 0…5); proposed `regard_step` 0.04, so one full-weight conviction moves the obstacle by at most 1.0; control 0 | − for favour, + for hostility | an act with one person counterparty and no bench (`tell`, `lie`, `argue`, `arrest`, `interrogate`) |
| `capability` | a capability the situation rewards or punishes (a venue that penalises want of Grace) | the `circumstance` rows of `tables.capability_uses` (`10_DICE_capability_axiom_map.md` §A, §C, §G edits 1 and 6), summed host-side and carried raw as one operand | as each row's gain fixture; none ship | − / + | as each row's `when:` |
| `reception` | how the bench is disposed to the actor | `world_q.reception` as SC-02's design re-sources it (the actor's own ledger; the bench's public commits), times `reception_gain` | as today (gain 1.0) | − / + | an act heard by a bench; never together with `regard` |
| `evidence` | what is held, cited and left standing | `proof_step` × (the actor's cited items' weight − the other side's standing answers), per `05_SC_evidence_and_rebuttal_B.md`; until that lands, today's `world_q.proofs` | 0.25 per unit weight | − / + | any act whose row admits `cites` |
| `plea` | a concession's reward, an inapt speech's price | CR-62's `plea_step` operand | CR-62's | − / + | `speak` |

Two things are not obstacle terms and stay where they are: **leverage** (`effort`, DICE's `wounds`,
SC-P7's trait rows) is what the actor brings beyond his pool and remains a μ-shift on the roll; and
the **pool** itself (capability, practice, office weight).

### The bound

`bound(x) = min(x, ceiling)`, the existing `obstacle_ceiling` / `ceiling_per_pool` rule (H-213),
applied to the hard part: difficulty, opposition, standard, subject, stakes and the hostile halves of
regard, reception, capability, evidence and plea. The favourable halves are subtracted **after** the bound, and
the result is floored at `OB_MIN`. The ceiling exists so that no matter becomes impossible; applied
after the favourable terms, as today, it also erases what the actor brought (F-SC-16). This is P4
§3.3's ordering (*"the ceiling bounds only the opposing score"*) taken at its critic's finding 8 as a
modifier, unhalved, outside the ceiling.

### How the reason for an obstacle is read

`queries/inputs.py::Margin` gains `terms: tuple`, `((name, value), …)` in roster order, composed by
the module with the obstacle, plus `("ceiling", −clip)` and `("floor", +lift)` when a bound acted, so
that the values sum to `ob`. `seam/wrappers/sigma.py::resolve` already copies the margin's fields
into its result. SC-P1's `margin_endings` roster carries `terms` in place of its single `room` field,
so every rolled Event says, in the log and after a load, *Ob 3.5 = difficulty 1 + opposition 2.5 +
stakes 0.5 − regard 0.4 − evidence 0.5 + ceiling 0*. The harness prints that line where it prints
the degree. Person-side, `believed_input` fills what a person can know: `difficulty`, `standard` and
`stakes` are public data and always known; `opposition`, `regard`, `reception` and the other side's
answers are his claims or unknown (`10_DICE_believed_odds_have_a_prior.md` decides what unknown
means).

### How an NPC-versus-NPC contest gets its obstacle

By the same function with no branch. The actor is whoever chose the act; the counterparty is the
operand the verb row names (`loop/sides.py::sides_of`). The host builder reads: the row's
`difficulty`; the counterparty's score and his stance toward the actor; the docketed row's
`standard` and `disposes` kind where a bench hears; the actor's cited items (formed as Candidate
variants by the one chooser, `08_FI_05` edit 3) and the other side's standing answers. No field
depends on a player, and none on which of the two is "the NPC": two courtiers arguing in an empty
hall, a prosecutor before a bench of three, and a player's plea are three inputs to one composition.
Where both want to move each other, each makes his own act and each act has its own obstacle; there
is no shared roll.

### What survives of the parity proposal (SC-P5), and what is moot

| SC-P5 item | now |
|---|---|
| option B, price an opponent at `MU_PER_DIE × score` | **not adopted.** The score/2 form is kept as the `opposition` modifier. The divisor stays in its one owner, `sigma_leverage.opposed_ob`, which combat shares; a social-only rate fixture would be two ladders for one quantity (an S defect, §0.06), so none is added. The alternative remains a measurement arm of that function, never a shipped value without a ruling |
| "equal parties should be even" as the target; the audit's §11 item 1 as a survivor for Jordan | **moot.** A contested act is an attempt at a task against resistance, and its difficulty is not the opponent's alone. H-288's swap test stops being a requirement; the row is regraded as answered |
| the rising disadvantage of equal pairs (P(Failure) 0.420 at score 2 to 0.606 at score 12) | **largely removed by the base, measured.** With `difficulty` 1 and no other term, equal pairs fail 0.74, 0.71, 0.71, 0.72, 0.73 at scores 2, 3, 5, 8, 12 (`runs/SC_B/difficulty_odds.txt`): flat within 0.03, and high. The level is the modifiers' to move: one obstacle unit of favour brings the same pairs to 0.42, 0.51, 0.56, 0.61 at 2, 5, 8, 12 |
| H-127's inversion, decided there as "no floor, no edit" | **superseded.** The stand-in `obstacle_default` no longer stands for a person: a person without a score opposes at `opposed_ob(pool_default)` (DICE's proposal), and a non-person subject has no opposition term at all |
| its exact-odds tables | **kept** as the instrument; re-run under this form in the gate |

## Exact edits, by owner

1. `engine/season/rosters.yaml`: rosters `difficulty_levels` (ordered names) and `obstacle_terms`
   (ordered, closed: `difficulty, opposition, standard, subject, stakes, regard, reception,
   capability, evidence, plea`). DICE's map proposes a roster of the same name holding `[capability]`
   (§G edit 1); it is this roster, with `capability` as one member, not a second one.
   `engine/season/data/fixtures.py`: tables `difficulty_ob`, `stakes_ob`, and the scalar
   `regard_step` (0.04; control 0), each with a NUMBER row in `hole_register.yaml` and a three-point
   sweep. No rate fixture: the divisor is `opposed_ob`'s. `obstacle_default` is deleted with H-127's
   row.
2. `engine/season/verb_table.yaml` and `data/verbs.py`: a `difficulty:` column. The loader refuses a
   contested or graded row without one and a row that is neither with one (the refusal shape
   `01_CORE_capability_authoring_surface.md` edit 3 gives `capability:`). Proposed values, all
   `grade: assumption`, chosen so that today's obstacle is reproduced at the control arm: the rows
   whose counterparty is a person (`tell`, `lie`, `argue`, `determine`, `arrest`, `interrogate`) →
   `routine` (1, plus `opposed_ob(pool_default)` 1 = 2); the rows with no person counterparty
   (`speak`, whose subject is a `DocketItem`; `research`, `examine`, `surveil`) → `demanding` (2).
   A designer who judges a lie harder than a telling edits one cell.
3. `engine/season/arrangements.yaml` / `data/arrangements.py`: a `standard:` key (default `plain`),
   read by the host builder; no seeded row changes.
4. `engine/season/queries/inputs.py::SocialContestInput`: add `difficulty`, `standard`, `stakes`,
   `regard`, `regard_step`, `capability_terms` (DICE's `obstacle_terms` float, renamed so the field
   and the roster do not share a name), `rebuttals`; remove `obstacle_default`. `Margin` gains
   `terms`.
5. `modules/social_contest/roll.py::obstacle`: the composition above, returning the obstacle and its
   terms from one helper; it refuses a term name outside the roster it is handed.
6. `engine/season/seam/wrappers/sigma.py::contest_input` / `_frame`: fill the new operands (the row's
   difficulty; the docketed row's standard and disposal kind; the counterparty's stance toward the
   actor); `believed_input`: the three public operands always, the rest from his claims.
7. SC-P1's roster `margin_endings`: `terms` replaces `room`.

## Gate (execution artifacts)

- Unit: over a lattice of quarter-step operands, the returned terms sum exactly to the returned
  obstacle, and every name is a roster member.
- Exact odds (no draw): the table in `runs/SC_B/difficulty_odds.txt` reproduced from the module's own
  `obstacle` and `band_odds`; and F-SC-16's rows re-run: pool 2 against a score of 8, proofs 0 to 4,
  must now give four different obstacles.
- `build_realm(0)`, one season, at the control arm: a printed count of rolled acts whose obstacle
  differs from the base commit, each with its terms; expected only acts against the score-holders.
  At the proposed arm, the same count, every extra row showing a non-zero `regard` or `stakes` term.
- A hand-built fold with no player: two NPCs, one `argue`, the hearer holding one stance row toward
  the arguer, `(arguer, +4, 1)` in one arm and `(arguer, −4, 1)` in the other; the two Events' `terms`
  differ in `regard` alone and by `8 × regard_step`.

## Falsifier

An act with a non-`plain` difficulty whose obstacle equals `opposition` alone. A realm act whose
obstacle moved and whose counterparty holds no score and whose terms show no non-zero modifier (the
"equal at shipped data" claim is then wrong). A pool-2 actor facing a score of 8 whose obstacle is
the same with and without four standing proofs.

## NERS reading

- **N**: top-down a designer sets how hard an act is by naming a level on its row; bottom-up every
  term reads a fact that exists; lateral combat already derives its obstacle from the defender plus
  the instance; diagonal a room's standard and a disposal's weight reach one person's roll.
- **R**: characters differ (score, stance), rooms differ (standard, reception), cases differ
  (evidence, stakes), and each difference is visible afterwards. Complete at its extremes: bounded
  above by the ceiling, below by `OB_MIN`.
- **S**: one composition for a telling, a hearing and an inquiry; the unit is the obstacle's
  throughout; `regard` and `reception` are one quantity at two audiences and never both apply.
- **E**, last: one column, one row key, two small tables and one tuple on the margin, against an
  obstacle a player and a chronicle can read.

## Cost class

Small build. Lanes: SC (the module and its record), IN/CORE (the verb column), DICE (`score()`,
`opposed_ob`, the `capability` circumstance rows), FA (rows that author a `standard`).
