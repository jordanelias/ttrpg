# 08 · FI · 02 — A rumour that travels: what a person passes on, to whom, and the broadcast's retirement first

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-14, C-19) — `said_slants` has one text across three proposals, `[newest, valence, unshared, unshared_first]`, and edits 2 to 4 are read with `U5c_FI_residue.md` §6. Edit 5's `present_persons` is the one reader of believed co-location for every family. CR-29's gate gains the `march` and `migrate` reading (`U5c_FI_residue.md` §2 row 2). The `reach` roster carries two rows Jordan has answered: seat changes realm-wide (A-32), a death by presence, trail and telling (A-33).

## Status: PROPOSED

Carries audit `audits/08_FI_audit.md` F-FI-02, F-FI-05 and resolutions R-05, R-06, R-18, R-28.

## What this changes in `engine/season/` at runtime

(1) B10-14 is re-ordered so CR-29 (the event-kind `reach` channel and `chronicle`'s deletion) runs first.
(2) `queries/person_q.py::said_of` gains a third slant, `unshared`, which never passes on the transport's
own event kinds and prefers what the room did not see. (3) A telling is offered to the people the teller
has seen since he last moved, not to everyone he has ever heard of. Each is a fixture arm with its control.
Declared hash movers.

## The problem, with evidence

`dynamics.py` (scratchpad `runs/FI/`), `build_realm(s)`, one season, `PYTHONHASHSEED=0`:

| seed | `tell`+`lie` admitted | `tell.refused` | `news.untold` | `news.told` | told claims held (with a teller) | of all `told_by` |
|---|---|---|---|---|---|---|
| 0 | 6 | 20 | 4 | 2 | 7 | 6,040 |
| 1 | 13 | 43 | 12 | 1 | 0 | 4,049 |
| 2 | 2 | 4 | 2 | 0 | 0 | 3,746 |

No chain is longer than one hop (also at seed 0 over two seasons: 12 chained claims, all one hop;
`hole_register.yaml` H-272 reads the same over 13 worlds). Three attritions, each at a call site:
**absent hearer** (a `tell` forms for every person in `known_persons`; presence is the world's to answer,
so he cannot decline and the fold refuses); **the roll** (`a standing`, at the default pool); **nothing new
to say** (`said_of` picks the newest non-`seen` claim, which the room usually holds; the exact-triple
guard drops it; and after a telling the hearer's newest claim on the topic is `(topic, news.told, True)`,
which is what he would retell).

## Edits, by owner

1. **`workplans/valoria_master_workplan_v11_part3.md`, B10-14 "Order inside".** CR-29 first (it is third).
   Reason: speakerless `told_by` is 37–49% of everything held; while it names everyone to everyone, neither
   this proposal nor `08_FI_01` can be measured. CR-29's `reach` roster also answers H-234 (R-18): a row for
   the unrest kinds keyed by rung kind, not a sixth channel; and audit §11 item 1 (a row for seat changes).
2. **`engine/season/rosters.yaml: said_slants`** gains `unshared`, with two data keys:
   `excludes_kinds_of: [tell, lie]` (verb names, validated at load against the table as `lie_verbs` is; the
   excluded predicates are those rows' `emits` and `emits_on_refusal`, derived, never spelt), and
   `prefers: [told, inferred, cell, other]` (an ordered tier list).
3. **`queries/person_q.py::said_of`**, at `_slant(fx) == "unshared"`: drop from the pool every claim whose
   predicate is an excluded kind; then pick, by the existing comparator (`LedgerReader._best`), within the
   first non-empty tier: claims with a non-empty `chain` (what he was told); `source == "inferred"` (what he
   found or learned from his office); cell claims (`is_cell`); anything else. A `seen` claim remains last
   resort, as today. No ledger but the teller's is read; no draw is spent. The echo is already damped: a
   retelling to its own origin is dropped by the same-origin clause of the exact-triple guard
   (`loop/witness.py`, T5).
4. **`engine/season/data/fixtures.py: said_slant`**: swept `newest` (control) / `valence` / `unshared`;
   ships `unshared` once the gate reads.
5. **`decision/options.py::opening_set`, the counterparty fan for rows whose cell carries a `with`
   conjunct on `to`** (`tell`, `lie`, `give`): fan over `person_q.present_persons(ledger, actor)` — the
   subset of `known_persons` the actor holds a firsthand `seen` claim naming at a `(when, round)` no older
   than his own newest movement claim. A new reader beside `known_persons`, World-free. Fixture
   `telling_hearers`: `known` (control) / `seen_since_move`. He may still be wrong (the man left this
   round); the fold still refuses that.
6. **Not edited here, named:** the telling's roll is SC's (`verb_capability: tell → copying`,
   `obstacle_default`). At 2 / 1 / 0 successes of 6 / 13 / 2 admitted tellings it is the second attrition;
   whether an ordinary telling between two people who are together should fail two times in three is a
   question for the SC lane's audit.

## §4. What is told, and whether it is confided, are the teller's choices (audit F-FI-10, R-30)

Today `said_of` picks one claim for everyone alike and `_circle_of` decides confidence by a world draw, so
a gossip and a discreet man with the same ledger say the same thing, and a player-proxy seated on a
person cannot choose what to tell (the Candidate has no operand for it).

7. **`rosters.yaml: choice_sourced`** gains `said` for the rows whose cell carries an `own_ledger`
   conjunct with a counterparty (`tell`, `lie`), on `marshal`'s precedent (`operand_bags` ranges a
   payload key over a closed set). The set is the top `said_choices` claims `said_of`'s slant ranks for
   that subject (a fixture; `1` is the control and is today's single pick). One Candidate per hearer and
   per claim; the existing score terms (pursuit alignment, `deed_valence` of the claim by the teller's own
   projected pursuits, the believed odds) rank them. No new scoring term.
8. **Confiding is an operand, not a draw.** The same rows gain a choice-sourced `in_confidence` in
   `{false, true}`; `loop/witness.py::_circle_of` reads the act's own operand where it now draws on
   `telling_privacy`, which remains as the swept share for a chooser that declares none (control 0).
   Who hears is unchanged (presence; private whispers are not built, by ruling).
9. **Left as declared defaults:** which key a forgery falsifies and which way a lie moves a number. Both
   need an operand channel a computed act does not have (`H-94`); named, not built.

Gate for §4: at seeds 0–2, two persons holding the same claims about one subject and differing in
pursuits tell different claims in at least one case; control `said_choices = 1` reproduces today's hash.
One interface for an NPC and a player-proxy: both pick among the same Candidates.

## Gate (execution artifact)

`dynamics.py`-shaped reading at seeds 0–2, two seasons, shipped fixtures plus the two new arms:
chained claims with two or more hops > 0 in at least two of three seeds, against the `newest`/`known` control
reading 0; told claims deposited per `news.told` ≥ 1; `tell.refused` per admitted telling falls. At
`telling_privacy` 1.0 (an arm, not shipped): `confidence.broken` > 0 (H-204's break path, R-28).

## Falsifier

Both arms on and two-hop chains still 0: then the binding attrition is the roll (edit 6's question), and
this proposal moved formation without moving traffic. Report it as such; do not tune the slant further.

## NERS reading

N: the hop discount, the noisy-OR over origins, the teller's record, the lossy copy and confidences all
exist to grade rumour and have no input; removing rumour's carrier leaves them inert, so the carrier is
necessary to five built mechanisms. R: this is the no-player half of R itself: the world generating drama
by misreport. S: one owner (`said_of`), one more arm on an existing roster; `present_persons` sits beside
`known_persons`. *Pauses correctly*: untouched. E, last: two readers and one roster row against five
dormant mechanisms.

## Cost class

Edit (2–5) on top of a scheduled small build (CR-29). Lanes: FI; SC for edit 6's question.
