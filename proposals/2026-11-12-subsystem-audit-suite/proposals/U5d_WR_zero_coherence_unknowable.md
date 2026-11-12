# U5d-WR — at zero coherence a person cannot be understood: legibility as the one dial on what others read of him

Reconciled: 2026-11-12, wave 3 (W3-3) — R3 §1 and §2, C3-L4 (3): reader 1 and gate (a) no longer cite `world_q.projection` (deleted by `17_CENSUS_C1A_01` D2); the per-holder view is `account`, the person's own ledger (`11_GO_player_surface_contract_B.md`). U1 §2 (one interface for the player view): edit 4's `legible` is a slot of `state/carriers.py::View`'s one closed list, added by GO with its reader, not a field this file coins. U3 §6.3: `Person.coherence` has no writer and no carrier in the suite; the readers ship and read nothing until one exists (INCOMPLETE, as the file already states). Batch and tier added (U3 B35; R3 7b-0).

## Status: PROPOSED, design-first (a plan for a later implementation lane; nothing here was executed)

Lands in batch: B35 (WR thread), last in U3 §1 item 35.
Depends on: `01_CORE_reason_trail_in_the_act_store.md` (B09); `10_DICE_believed_odds_have_a_prior.md` (B05); `11_GO_player_surface_contract_B.md` (B34, `account` and the `View` list); a writer of `Person.coherence` (CP-T07-02; no carrier in the suite, U3 §6.3).

Author: U5d closure lane (Fable), 2026-11-12, on Jordan's answer A-43 (D-58), which took neither offered
option. Carries the D-58 question of `unified/DECISIONS_FOR_JORDAN.md` and
`audits/09_WR_audit_addendum_B.md` F-WR-18's other half (what **others** read of a practitioner; what he
reads of himself is `09_WR_B_threadwork_session_and_practitioner.md` edit 3, R-25).

## The ruling, quoted

*"zero coherence means that the person is no longer able to be understood within the bounds of human
rationality. they may still hold their seats and offices and stuff, but they become radically unknowable
as their being of being has changed fundamentally"*

Read: continuity is kept (seats, offices, goals; ARC-28, ARC-29, ARC-30 stand). He is not dead, not
dissolved, and not merely garbled in speech. What changes is how others, and the player, can **know**
him. Coherence is the dial.

## What it changes in `engine/season/` at runtime

Nothing until `Person.coherence` has a writer: the field is declared and unproduced
(`write_matrix.yaml:200-206`; the host is plan B10-15's CP-T07-02). Once it does, one person-side
function scales every reading another person makes of him, and at zero those readings return what a
stranger would get.

## The resolution, decided as a shape (each step marked where the tree could not ground it)

One function, one owner: `queries/person_q.py::legibility(coherence) -> float` in `[0, 1]`, 1 at full
coherence, 0 at zero, monotone; the curve between is a fixture `[ASSUMPTION; Jordan to author; control:
1.0 everywhere, which is today's game]`. It is applied at the four ordinary readers the ruling's record
names, each at its single owner:

1. **Reasons.** What a witness learns of *why* he acted. The reason trail is
   `01_CORE_reason_trail_in_the_act_store.md`'s; the per-holder view is `account`, the holder's own
   ledger (`11_GO_player_surface_contract_B.md`; `world_q.projection` is deleted by `17_CENSUS_C1A_01`
   D2). At legibility 0 his acts are still seen (an Event is an Event) and carry no reason for any other
   holder.
2. **Prediction.** What another person expects him to do. The reader is
   `10_DICE_believed_odds_have_a_prior.md`'s believed odds: the weight on what the believer holds about
   him is multiplied by legibility, so at 0 the estimate is the prior alone (no better than a draw).
3. **Regard.** `person_q.regard(p, referent)` (`:424`) and `opinion` read deeds attributed to him. His
   deeds stay attributed; what they *mean* to the reader (the deed's lean on the reader's axes,
   `deed_term`) is scaled by legibility, so people can fear what he did and cannot place him.
   `[unverified]` that scaling `deed_term` is the right cell; the alternative is to scale the claim's
   confidence at deposit. One of the two, never both.
4. **Telling.** What he says (`tell`, `argue`, `speak`; `person_q.said_of`, `:1165`) deposits to a
   hearer at a confidence scaled by legibility; at 0 his speech deposits nothing a hearer can use.
   What others say **about** him is unchanged (rumour of an unknowable man still travels).

Not touched: his own chooser (he still ranks and acts on his own sheet; A-34 makes his self-knowledge a
belief, and R-25 keeps his own Coherence from him); his holds and seats; `thread_read` on him, which
finds his state (CP-T07-10) and is the one way to learn why he is unreadable.

For the player: the player surface shows, for a person at low legibility, his acts and no reasons, and
marks the prediction it offers as unconditioned. If the player's own character reaches zero, the same
function applies to what the surface tells the player of him; that case is not ruled and is listed
below.

## Exact edits, by owner, in order (to be re-derived at build; the field has no writer today)

1. `data/fixtures.py`: `legibility_curve`, control `()` (legibility 1.0 for everyone).
2. `queries/person_q.py::legibility`, beside `regard`.
3. The four readers above, each gaining one multiplicand read from the *other* person's coherence as
   the reader **believes** it (a claim in his own ledger; AX-2), never from World truth. A reader who
   holds no claim about his coherence reads legibility 1.0 and is simply wrong in his predictions: the
   unknowable man is discovered by being wrong about him.
4. `11_GO_player_surface_contract_B.md`'s view: one slot of `View`'s closed list (U1 §2), `legible`, a
   band per shown person, added by the GO lane with its reader (`person_q.legibility` over the viewer's
   own claim), not coined here.

## Gate (execution artifact)

On a hand-built world with one person's coherence written to 0 and a witness holding a claim of it:
(a) the witness's `account` row of his next act carries no reason; (b) the witness's believed odds for his
next act equal the prior; (c) his `tell` deposits no usable claim; (d) his seat-`hold`s are unchanged
and he still acts. Control: the same world with coherence at ceiling reproduces today's readings.

## Falsifier

Any tenure of his closing because of coherence; his own chooser changing; a second witness with no
claim of his coherence reading him as unknowable (it must come through what the witness believes).

## Not decided here (unstated by A-43; marked)

The curve; whether legibility falls gradually or only at zero (the ruling speaks of zero; the record
says "coherence is the dial"); the player's own character at zero; whether an unknowable holder's writs
are still understood by their addressees (a decree's terms are public under A-21; this plan leaves them
readable, since the paper is not the man).

## NERS (E last)

N: without it zero coherence has no effect a player can meet (ARC-28 to ARC-30 need a state that is
neither death nor a speech penalty). R: a king nobody can read is a political fact generated by the
Thread, with nobody watching. S: one function, four readers, no new carrier; composes with A-34 and
A-40. E: "you can see what he does and no longer why" is a rule a player can hold.

## Cost class

Design-first; small build once `Person.coherence` is written. Tier: `sonnet` (R3 7b-0).
