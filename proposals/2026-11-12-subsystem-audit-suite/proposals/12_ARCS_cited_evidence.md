# ARCS 04 — evidence that is held and cited: what the cases require of a hearing

Reconciled: 2026-11-12, U5d closure — folded the standing rule (A-24; `audits/18_DETERMINISM_SWEEP.md` D-01, D-02) and the reconciliation this file's own Status line asks for. "The arrangement admits; a contradiction strikes" are not fixed functions of state: admission rides the citing draw (`19_LACUNA_admission_rides_the_citing_draw.md`) and a contradiction is a rebuttal that is itself drawn (`05_SC_evidence_and_rebuttal_B.md`, which supersedes the hearing proposal this file names). This file's `proofs` edit is carried as one member of the one obstacle form (`U5c_SC_one_obstacle_form.md`); the typed interface between a held Record and a room is `08_FI_05_evidence-interface_B.md`. Kept from this file: a held Record counts; possession can be found out. An appeal is admitted on new grounds only (A-39), which is what gives a newly found Record its use after a verdict.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-2 (`unified/work/R2_READ.md` §1.6 row ARCS-04 (SUPERSEDED in part), §2 row ARCS-04, §7, §7b-T; `unified/U1_OWNERS_AND_VOCABULARY.md` ledger S-01, S-02, S-22, S-26, D-U1-06 (a); `unified/U3_CONFLICT_LEDGER.md` §9). The body follows the head: resolution items 1–3 and their edits are superseded and replaced by pointers (item 1 a held Record as a proof → EVID_B's `cites` of a Record and the `proofs` leverage source, OBS §3; item 2 admission → the arrangement's `proofs:` filter in EVID_B/T13 T5 and ADM's band; item 3 "the speaker's unit is struck" with certainty → the drawn answer, EVID_B rule 2, which the standing rule requires); item 4 (possession can be found) stands and its site is named (`loop/witness.py::_found_claims` through `rosters.yaml: finding_terms`); the Status line's "to be reconciled" is done; the gate and falsifier read levels, not a lowered obstacle (A-25); named tests, lands-it and tier.

**Lands in batch:** B24 (item 4 with the evidence cycle; it needs `cites` of a Record). **Depends on:** `05_SC_evidence_and_rebuttal_B.md`, `19_LACUNA_admission_rides_the_citing_draw.md` (B24), `08_FI_03_playable-inquiry.md` §2 (B11, graded inquiries' finding terms).

## Status: PROPOSED (item 4 only; items 1–3 superseded by `05_SC_evidence_and_rebuttal_B.md`, `19_LACUNA_admission_rides_the_citing_draw.md` and `U5c_SC_one_obstacle_form.md`). Ownership of proceedings is ruled (ED-SC-0033..0039) and is not changed.

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

Items 1–3 are **superseded** (head line); where each now lives:

| item | now |
|---|---|
| 1 a held Record is a proof | a Record on the citer's live `hold` is a citable item of kind `record`, weight 1 (FI E-1; EVID_B); it reaches the roll as `proofs` levels (OBS §3); a forged Record counts as any until answered |
| 2 the arrangement admits | the arrangement row's `proofs:` admission filter (`13_SC_tuning_tables.md` T5; EVID_B), and entry by the citing band (ADM) |
| 3 contradiction is not a mirror | an answer is a drawn act graded by its band (EVID_B `standing` rule 2); same value is agreement (rule 3); nothing is struck with certainty (the standing rule) |

4. **Possession can be found.** A graded inquiry at the place a Record is kept (`examine`, `research`)
   that finds deposits a claim *about the holder* (`holds(person, record)`), which is then an ordinary
   deed-claim usable under item 1 and tellable. No new verb.
5. **Corroboration by independent roots (e2) is not decided here.** It needs the claim's source chain,
   which is the telling lane's (`08_FI_02_rumour-that-travels.md`); the six cases that need it wait.

## Edits, by owner

- Items 1–3: no edit here (their owners' edits).
- Item 4, the graded-inquiry deposit: the site is `engine/season/loop/witness.py::_found_claims` (`:297`),
  which deposits what a look teaches by band through `rosters.yaml: finding_terms` (band → `observation_terms`
  members; loaded by `data/rosters.py::_load_finding_terms`, `:1073`). Edit: one `observation_terms` member
  `holder` `[ASSUMPTION: the member name; U1 ledger S-26 owns the roster]`, added to `finding_terms` at
  `Partial` and above for an inquiry at a place where a Record is kept; `_found_claims` deposits
  `(holder person, holds, record id)` to the finder. It names a holder, not a doer, so D-U1-06 (a)'s
  `supplied_by: who` constraint does not bind it `[ASSUMPTION — basis: a holding is a state, not an act's
  hand]`. That a Record is held by a `hold` tenure is the reading `cases/exercises/NPC-088.yaml` records
  `[UNVERIFIED: not traced in `state/`; the executing session opens `state/carriers.py` for the Record's
  holder field before the edit]`.
- `hole_register.yaml`: H-216 and H-75 regraded when the gates below read.

## Gate (execution artifact)

NPC-086 on the realm, seeds 0, 1, 2: Bergvall's hearing reads more `proofs` levels for his side when he
cites his survey Record than when it has been seized beforehand (off-arm), and the opponent holding a
contradicting finding can answer it by a drawn act (EVID_B). NPC-088: an inquiry at her workshop that
grades `Partial` or better deposits a `holds` claim about her in the inquirer's ledger; with the Record
given away first, the claim names the new holder. Named tests (new,
`engine/season/tests/test_arcs_possession_found.py`): `test_an_inquiry_finds_who_holds_the_record`,
`test_a_given_away_record_names_the_new_holder`, `test_a_failed_inquiry_deposits_no_holds_claim`.

## Falsifier

If the `proofs` levels are equal with and without the cited Record, the proof is not read; if the obstacle
moves with it, a favourable term was subtracted (A-25). If a forged Record and a true
one are indistinguishable to the bench forever, forgery has no risk; the forged arm must be reversible by
a finding.

## NERS reading

**N**: from the investigation side (a find matters later), from the hearing side (a case is what you
hold), from the record side (custody is power: NPC-008). **R**: building a case, suppressing one and
forging one are strategies for player and NPC alike; an NPC can be answered by another NPC's holding.
**S**: one count, one reader, one obstacle; no second resolution ladder. **E (last)**: "what you hold and
can show raises you; what they hold can be put against it, by a draw."

## Cost class

Item 4: edit (one roster member, one `finding_terms` cell); hash EQUAL until a graded inquiry finds a held
Record.

**Lands it and tier.** The B24 batch, an FI `valoria-author` session on `sonnet` (`high`), closed by B24's
`methodology-close`. **Hash movers.** Every world in which a graded inquiry at a Record's place grades
`Partial` or above (declared).
