# 16 · PESSIMIST · FI · C — What a deed leaves behind: a trail at the place, the ending in the requirement's own words, and no reading of who is truly where

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-20) — edit 4 lands as one change to `questions_for` with `08_FI_01_claim-sourced-referents.md` edits 2 to 5 (`U5c_FI_residue.md` §1); one function, one commit, one gate.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: `R5_READ.md` §1 (CONFORMS; edit 4 moves toward `04` PART D
2 and 42), §7/§7b (edit 2 moved off the v11 workplan line onto the v12 card, per STAGES.md: this session's content wins
over v11; tests; tier); U3 C3-K6 (this file adds the three `covert_kinds` members in B11; `21_PROCEDURAL_C` adds the
per-kind keys `leaves`, `fade`, `channels` to every member, these three included, in B39), B11, §6.2; A-33 (news of a
death travels by presence, trail and telling: this file is the trail); U1 glossary *rung* ("his own ladder" → "his own
chain of seats"). Changed: edit 2's target, edit 4's wording, the gate's probe rows.
Reconciled: 2026-11-12, wave-3 mop-up (`unified/work/W3_5b_DONE.md` "For another lane", W3-3 item): edit 1 states the `leaves` channels of the three members (PROC_C's draft, taken as this file's, `[ASSUMPTION]`).

## Status: PROPOSED

Lands in batch: **B11** (FI; IN for edit 4). Depends on: `08_FI_01_claim-sourced-referents.md` edits 2-5 (B11; edit 4 lands
with them as one change to `questions_for`, C-20), `08_FI_02_rumour-that-travels.md` edit 5 (`present_persons`, B11), and
CP-T06-04 (a v11 plan position, MISSING as code until v12 disposes it; only the gate's last row waits on it).

Carries `audits/16_PESSIMIST_FI.md` F-PES-FI-01 (§2.4) and F-PES-FI-04 (§2.5). Extends two scheduled
B10-14 cards (CP-T06-01, CP-T06-02) by data and by one sentence each; depends on `08_FI_02` edit 5
(`present_persons`) for edit 4 and on CP-T06-04 for the gate's last row.

## What this changes in `engine/season/` at runtime

1. A killing, a wounding, a sabotage and a razing leave a trail an inquiry **at the place where they
   were done** can uncover, graded by the existing bands (`finding_terms`): `Partial` learns the deed
   and its object, a better band the hand.
2. A witness of an ending (a person killed, a rung razed, a record destroyed) holds it in the
   vocabulary a requirement reads (`exists:<Kind>` at 0) beside the event-kind claim.
3. The question loop stops reading whether a claim's subject still exists and where it truly is. A
   person learns that a man is gone or has left by seeing, by being told, or by being refused.

Declared hash mover.

## The problem, with evidence

`p5_crime.py` (tiny world, shipped fixtures, real acts): after a killing with no bystander, the killer
alone holds `(King, person.died)`; everyone alive holds `(the King's seat, tenure.closed)` by the
`chronicle` channel; a visitor one tick later learns nothing; `surveil` of the place (40 acts, 12
`finding.made`), `interview` of the killer (40 of 40 `finding.made`) and `reconstruct` (40 of 40) teach
nothing about the death; `trail_of` is empty for the place, the killer and the victim. After a
sabotage with no bystander (condition 900 → 0), `examine` of the site (40 acts, 15 `finding.made`)
leaves the examiner holding that the site exists. `rosters.yaml: covert_kinds` is `[record.forged]`
against thirteen harm-shaped deed kinds.

`p1_belief.py`, `p1c_exists.py`, `p1d_where.py` (the subject's ledger identical in each pair):

| arm (against its control) | the subject's candidates |
|---|---|
| the King deleted on the World: no Event, no WITNESS | −28, every one about the King |
| the King's containment moved to another realm, the same way | naming the King: 38 → 10 |
| the subject instead *believes* `(King, person.died, True)`, the King alive | +28, every one about the King (`challenge`, `interview`, `tell`, …) |
| the subject believes `(King, exists:Person, 0)`, the King alive | `challenge`, `interview`, `train` and the cell lies declined; `tell`, `move`, `speak`, `surveil`, `transfer`, `tie / knot` still formed |

Owner of the leak: `queries/world_q.py::questions_for`, the claim loop: `c.subject in R` and
`place_of(w, c.subject) in R` with `R = reach(w, p)`, all read from the World. The tree's decision on
this class is recorded (ED-IN-0292, last row, TAKEN-ARCH: a fact reaches a person as a claim through
the channels, not as a world stamp); `08_FI_01` builds it for seats and vacancies and leaves this loop
(its audit's R-04).

## Resolution, decided

One rule in three places: **what happened to a thing is knowable where it happened, in the words the
requirements use, and nowhere else by default.** Ladder: step 1 for edit 4 (ED-IN-0292's last row);
step 3 for edits 1 and 2 (B10-14's CP-T06-01 and -02 already schedule the trail's widening; this
completes its object list); step 4 for edit 3 (the observation deposit already writes `exists:<Kind>`
readings into an actor's ledger: `p4_detective.py`'s `(paper, exists:Record, 1)` after a `research`,
`p1c_exists.py`'s `(King, exists:Person, 0)` after a refused `challenge`).

## Edits, by owner

1. **`engine/season/rosters.yaml: covert_kinds`** gains the deeds done **to a person**:
   `person.died`, `body.changed`, `person.captured`. Each member also names where its trail lies, in the `leaves`
   map `21_PROCEDURAL_C_prologue_and_case_seeds.md` (f) adds for every member (C3-K6): `person.died:
   [body_changed, co_located, site_changed]`, `body.changed: [body_changed, co_located]`, `person.captured:
   [co_located, tenure_closed]`, from that file's closed channel set. `[ASSUMPTION: the three maps are PROC_C's
   draft, taken here as this file's own — basis: PROC_C (f) says this lane corrects them and each channel is a
   thing the kind's own write changes: a death writes a Person's body and happens at a place, a capture closes
   or opens a custody edge; reversible by editing the three lines.]` (Data. `trail_of` already keeps only Events a
   person did, so MATTER's `body.changed` from hunger is no trail; `holds_trail` already excludes a
   finder who witnessed the deed.) B10-14 schedules the place and alias deeds (CP-T06-01: *"a deed
   that writes a place or an alias leaves a trail"*, so `site.damaged`, `rung.razed`, `cover.assumed`)
   and the place index (CP-T06-02: *"`surveil` finds the covert deeds done at the place it watches (the
   latest per kind and place only)"*). Neither card reaches a killing: it writes a Person, not a place.
2. **The v12 card for CP-T06-01** (not the v11 line `workplans/valoria_master_workplan_v11_part3.md:119`,
   which this session's content supersedes, STAGES.md) carries the third object: *"a deed that writes a
   place, an alias **or a person** leaves a trail; `examine` reads the place side as `surveil` does"* (for
   the Site's rung, once F-FI-12's operand repair lets `examine` form). No index beyond CP-T06-02's own.
   This is a plan edit for the v12 author, not a code edit.
3. **`engine/season/loop/witness.py::witness`**, at the event-kind deposit: for each change of the
   Event that ended an entity (the write-matrix field `<Kind>.exists`, set false), deposit
   `(entity, exists:<Kind>, 0)` to the same witness, same source and confidence. Keyed on the field
   written, never on an event kind or a verb.
4. **`engine/season/queries/world_q.py::questions_for`, the claim loop.** Clause 1 keeps `reach(w, p)`
   for Rungs and for what he holds (a man knows his own chain of seats and lands: `08_FI_01`'s R-03). For a
   Person subject, clauses 1 and 2 are replaced by a person-side test: the subject is in
   `person_q.present_persons(p.ledger, p.id)` (`08_FI_02` edit 5's reader: those he has seen since he
   last moved) or is named by a claim that landed since `floor`, and his newest `exists:Person` claim on
   the subject, if any, is not 0. `place_of` leaves this loop. The fold's `with` and `kind` conjuncts
   refuse what is no longer possible, and the refusal's `exists` observation teaches him
   (`p1c_exists.py` (ii): candidates 38 → 16 after one refused `challenge`).

## Gate (execution artifact)

`p5_crime.py`, `p1_belief.py`, `p1c_exists.py`, `p1d_where.py`, `p4_detective.py` were lane scratch (not in the
repository, U3 §6.2). Written first as NEW `engine/season/tests/test_deed_trail_at_place.py`:
`test_surveil_at_the_place_of_a_killing_finds_the_deed_at_partial`, `test_bystander_holds_exists_person_zero`,
`test_examine_finds_site_damaged`, `test_questions_for_does_not_read_place_of_for_a_person_subject` (the
`p1d_where` pair: relocate a person with no Event, the subject's candidates are unchanged),
`test_unevented_deletion_moves_no_candidate` (the `p1_belief` pair). Re-record
`engine/season/tests/test_fi03_trail.py::test_the_realm_seed_twice_in_one_process_gives_one_hash_and_reaches_no_find`
(`:793`, exists), said plainly in the commit. Command:
`python -m pytest engine/season/tests/test_deed_trail_at_place.py engine/season/tests/test_fi03_trail.py -q`.

| reading (the scratch scripts' cases, committed as the tests above) | today | after |
|---|---|---|
| `p5_crime.py` (a): visitor's `surveil` at the place, 40 acts | holds nothing of the King | at `Partial`: `(King, person.died)`, hand withheld; at `Success`: the killer named |
| `p5_crime.py` (a), bystander arm | hold `person.died` | also hold `(King, exists:Person, 0)`; their candidates naming him decline by clause 4 |
| `p5_crime.py` (b): `examine`, 40 acts | holds `exists:Site` | at `Partial` or better: `(harbour, site.damaged)` |
| `p1_belief.py` `dead-silent` | −28 | 0 lost |
| `p1d_where.py`, King relocated | 38 → 10 | 38 → 38 |
| `p1c_exists.py` (ii), `interview` on the deleted King | teaches nothing | teaches `exists:Person 0` (with CP-T06-04) |
| `test_fi03_trail.py::test_the_realm_seed_twice_…_reaches_no_find` | pins 0 finds | re-recorded, said plainly: the realm's `surveil` (80 acts in three seasons at seed 0) now has something to find wherever a `capture` felled a man |

## Falsifier

Any pair of worlds that differ only by an un-evented edit to another person's existence or place, in
which the subject's candidate set differs. And: a seeded three-season realm in which a person killed by
another's act is held dead by nobody who was not present, after a `surveil` at that place has graded
`Success`.

## NERS reading

N: without a trail at the place, twelve of thirteen harms are unsolvable by construction and every
inquiry verb but `research` has nothing to find (`audits/16_PESSIMIST_FI.md` §1, cut X-FI-4); with it,
the six inquiry rows acquire a subject. Top-down (R-05, R-07), bottom-up (one more key on one index),
lateral (SC's hearing gets a homicide it can try: `19_LACUNA` §6's second scenario), vertical (a
seat's vacancy and its cause are now two facts with two speeds). R: the no-player half: a body is
found a season late by someone who was not looking for it. S: one ladder (`finding_terms`) for every
trail; ending is said once, in the requirement's vocabulary, so belief and fold ask the same cell. E,
last: four roster rows, one index key, one deposit, one loop clause replaced by an existing reader; no
new verb, no new carrier.

## For the standing rule

Nothing here resolves by a fixed function of state: the trail is uncovered by the inquiry's graded
draw; the witness's deposit rides whatever notice rule WITNESS has (`18_DETERMINISM_notice_is_a_draw.md`
makes it a draw); edit 4 removes a certainty (the engine telling a man who is where).

## Cost class

Edit (1, 3, 4); small build (2, inside CP-T06-01). Lanes FI; IN for edit 4 with `08_FI_01`. Tier: `opus` for
edit 4 (the judgment: which readings stay world reads), `sonnet`, effort `high`, for edits 1 and 3. Hash movers
declared: every seeded world (edit 3's deposits, edit 4's question set); one re-pin at B11's close. Lands it:
B11, after FI_A and SC_E (C3-K1), before `18_DETERMINISM_notice_is_a_draw.md`; order 1 → 3 → 4 (with `08_FI_01`
edits 2-5).
