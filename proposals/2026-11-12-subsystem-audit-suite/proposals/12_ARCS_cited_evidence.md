# ARCS 04 — evidence that is held and cited: what the cases require of a hearing

Reconciled: 2026-11-12, U5d closure — folded the standing rule (A-24; `audits/18_DETERMINISM_SWEEP.md` D-01, D-02) and the reconciliation this file's own Status line asks for. "The arrangement admits; a contradiction strikes" are not fixed functions of state: admission rides the citing draw (`19_LACUNA_admission_rides_the_citing_draw.md`) and a contradiction is a rebuttal that is itself drawn (`05_SC_evidence_and_rebuttal_B.md`, which supersedes the hearing proposal this file names). This file's `proofs` edit is carried as one member of the one obstacle form (`U5c_SC_one_obstacle_form.md`); the typed interface between a held Record and a room is `08_FI_05_evidence-interface_B.md`. Kept from this file: a held Record counts; possession can be found out. An appeal is admitted on new grounds only (A-39), which is what gives a newly found Record its use after a verdict.

## Status: PROPOSED — to be reconciled with the SC lane's hearing proposals (`05_SC_playable_hearing.md`, `05_SC_contest_record_on_event.md`, `05_SC_arrangement_rows_that_bind.md`), which this lane did not open. Ownership of proceedings is ruled (ED-SC-0033..0039) and is not changed.

Source: `audits/12_ARCS_adjudication.md` §4 (M-REC), §10 (e1–e6).

## What changes in `engine/season/` at runtime

`queries/world_q.py::proofs` counts held Records as well as held deed-claims, admits them by the
arrangement's own `proofs` column, and distinguishes a contradiction from a mirror. Holding a Record
becomes something another person can find out. With the two new fixtures at their controls the game is
unchanged.

## The problem, with evidence

- 51 cases turn on a reveal, an investigation, an accusation or a hearing; 25 need an argument to cite
  a held item (audit §10).
- Today a contested act's room terms are `reception` and `proofs`
  (`seam/wrappers/sigma.py:189-204`). `proofs` (`world_q.py:852-866`) counts the speaker's own
  deed-claims about the opponent, weighed by remove, and counts zero where the opponent holds a claim
  with the same subject and predicate. Its docstring names its limits (H-216): every attributed deed
  counts whatever the matter; the mirror keys on subject and predicate alone; the arrangement's `proofs`
  column is not read.
- A Record is no input to any contest. `forge` writes `Record.forgery_quality` and `conceal` writes
  `Record.exists`; neither reaches a room. `destroy_record` cannot fire for any actor (H-75).
- Possession has no consequence: NPC-088's defining risk (holding the copy is the charge) needs someone
  to learn who holds what.

## Resolution (decided)

1. **A held Record is a proof.** `proofs` adds, for each Record the speaker holds (a `hold` tenure) whose
   `subject_matter` names the opponent or the docketed matter, one unit at the weight of a firsthand
   claim. A forged Record counts at `forgery_quality` until a finding about it is held by the bench.
2. **The arrangement admits.** Only proof kinds in the sitting's arrangement row count (closing H-216's
   third limit at the owner, `data/arrangements.py`). A venue that admits "its own registers only" is a
   row of data, which is the asymmetry ARC-04, ARC-35 and EMG-X6 need.
3. **Contradiction is not a mirror.** Same subject and predicate with the *same* value: zero, as today.
   Same subject and predicate with a *different* value held by the opponent at lower remove: the
   speaker's unit is struck and the opponent's counts. A statement can be refuted by what the other
   side holds.
4. **Possession can be found.** A graded inquiry at the place a Record is kept (`examine`, `research`)
   that finds deposits a claim *about the holder* (`holds(person, record)`), which is then an ordinary
   deed-claim usable under item 1 and tellable. No new verb.
5. **Corroboration by independent roots (e2) is not decided here.** It needs the claim's source chain,
   which is the telling lane's (`08_FI_02_rumour-that-travels.md`); the six cases that need it wait.

## Edits, by owner

- `queries/world_q.py::proofs`: items 1 and 3, behind fixtures `record_proof_weight` (control 0) and
  `contradiction_rule` (control `mirror`).
- `data/arrangements.py`: pass the row's admitted kinds to the reader (item 2).
- the graded-inquiry deposit (item 4) `[UNVERIFIED site: the fieldwork provider's finding is deposited
  at WITNESS; the FI lane names the function]`. That a Record is held by a `hold` tenure is the reading
  `cases/exercises/NPC-088.yaml` records, not one I traced in `state/`.
- `hole_register.yaml`: H-216 and H-75 regraded when the gates below read.

## Gate (execution artifact)

NPC-086 on the realm, seeds 0, 1, 2: Bergvall's hearing resolves against a lower obstacle when he holds
his survey Record than when it has been seized beforehand (off-arm), and against a higher one when the
opponent holds a contradicting finding. NPC-088: an inquiry at her workshop deposits a claim about her in
the inquirer's ledger; with the Record given away first, the claim names the new holder.

## Falsifier

If the obstacle is equal with and without the Record, the proof is not read. If a forged Record and a true
one are indistinguishable to the bench forever, forgery has no risk; the forged arm must be reversible by
a finding.

## NERS reading

**N**: from the investigation side (a find matters later), from the hearing side (a case is what you
hold), from the record side (custody is power: NPC-008). **R**: building a case, suppressing one and
forging one are strategies for player and NPC alike; an NPC can be answered by another NPC's holding.
**S**: one count, one reader, one obstacle; no second resolution ladder. **E (last)**: "what you hold and
can show lowers what stands against you; what they hold against it raises it."

## Cost class

Small build behind two fixtures; hash EQUAL at the controls.
