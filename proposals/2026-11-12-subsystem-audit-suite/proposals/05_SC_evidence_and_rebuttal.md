# SC-P8 — evidence cited, evidence answered: proofs as typed items on the case file, and rebuttal by a held contradiction

## Status: PROPOSED

Source: `audits/05_SC_audit.md` §16 (the detective and noir precedent) and F-SC-14. Builds on SC-P3
(the hearing; the case file as the hearing's record) and on the plan's CR-61 (the case file) and
SC-02 (the re-source). It adds one roster reader, one payload shape and one rule; it makes no code
read `.designs/` or `.audit/`.

## What it changes in `engine/season/` at runtime

A `speak` on a docketed matter may cite named items it holds; each cited item is entered on the
matter's case file; a later `speak` by another person may strike an entered item by citing a held
item that contradicts it; `hearing` (the verdict's room operand) counts the items standing. With
no item cited (every computed `speak` today, until the chooser forms the variants) nothing moves.

## The problem (evidence)

Asked of the engine as built (audit §16 has the reads):

1. **Evidence is typed where it is held and untyped where it is used.** A `Claim` carries subject,
   predicate, value, source, chain and confidence; a `Record` carries kind, content and
   `forgery_quality`. The contest receives one float: `SocialContestInput.proofs` =
   `Σ remove_weight(c.source)` over the speaker's unmirrored deed claims about the subject
   (`queries/world_q.py:852-879`). No act names which item it relies on, so nothing can be answered,
   struck, examined or remembered item by item.
2. **Only `speak` takes evidence at all.** `argue`, `determine`, `arrest`, `interrogate`, `tell` and
   `lie` read no proof (`seam/wrappers/sigma.py::contest_input`: the room terms are filled only for
   a prize `heard_by: bench`).
3. **A document is not evidence in a hearing.** `rosters.yaml: proofs` is `[record, testimony, oath,
   confession]` and each arrangement row lists the kinds it admits; neither is read
   (`world_q.proofs`' named limit: *"the arrangement's admitted `proofs` column is not read here"*).
   A forged Record's quality enters only an `examine` (and is clipped by the fixed ceiling).
4. **Refutation is silence.** The one answer to a proof is the mirror: the opponent HOLDS a claim
   with the same subject and predicate and the proof counts zero, whoever he is and whether or not
   he speaks. It is total in play (H-216: 49 of 49), because WITNESS deposits a doer's own act to
   him. Nobody can present a contradiction, and a contradiction changes nothing.
5. **A case is not built or answered.** NPCs gather (`research` rolled 639 times and `surveil` 236
   in `corpus_run`; found deposits were 0 in three seeds at D_T06's probe `[not re-run]`), docket
   (`petition`, `carry`, `open_case`) and speak; no speech refers to another, and the verdict reads
   none of them (audit F-SC-05).

## The resolution, decided

One carrier, the case file (a World `Record`, CR-61), holds what was cited; three small rules act
on it. Ladder: step 3 for the carrier (CR-61 already makes the case file the proceeding's held,
forgeable record); step 4 for citing (`tell` already requires and names the held claim it says —
`payload["said"]`, the `holds` conjunct); step 5 for the rest.

## Exact edits, by owner

1. **Citing (`speak`'s `proofs` operand, SC-P3 edit 2, made typed).** Each entry is
   `{kind: <rosters.yaml: proofs member>, ref: <id>}`:
   - `testimony` → a deed `Claim` in the speaker's OWN ledger about the subject (firsthand or told);
   - `record` → a `Record` the speaker HOLDS (`hold` Tenure), whose content names the subject;
   - `oath` → a live `commit` of the speaker's to a HOLDS Proposition about the subject;
   - `confession` → a `confession.*` Event claim he holds (`interrogate`'s bands).
   The row's precondition gains one typed conjunct per entry (`claim.held` / `held_by` / `relation`
   — stems that exist), so an item not held is refused at the cell before any draw, as `tell`'s is.
   `seam/wrappers/sigma.py::contest_input` counts only cited entries whose `kind` the docketed
   arrangement row's `proofs:` admits — the first reader of that key and of the roster.
2. **Entering.** A `speak` at `Success` or better appends, beside SC-P3's band stage, one stage per
   cited entry to the case file: `(tick, "proof:<kind>", ref, act id)`. `Record.stages` is the
   carrier; no new field.
3. **Answering.** A `speak` on the same matter by a different person may carry
   `answers: [<stage index>, …]` with its own cited entries. An answer STANDS when the answering
   item contradicts the entered one: same subject and predicate, a different value — asked of the
   single owner of *pairs and disagrees* (`decision.agreement`, which `loop/matter.py::
   _standing_crossings` already calls resolver-side). A standing answer at `Success` or better
   appends `(tick, "struck", <stage index>, act id)`. A struck proof stops counting. The mirror is
   then what SC-02's design makes it — the opponent's public commit on that pair — and an unspoken
   mirror no longer zeroes anything.
4. **Counting.** `queries/world_q.py::hearing(w, matter, venue)` (CP-T05-02 (i), on SC-P3's
   carrier) = the band stages as that position weighs them, plus `proof_step` per standing proof
   stage, signed by side. One reader, one Record.
5. **Forgery.** A cited `record` whose Record carries `forgery_quality > 0` counts as any other
   until examined. An `examine` of that Record whose finding names it forged (the interface below)
   is an answering item of kind `record` against every stage citing it: the stages are struck, and
   the finding's Event deposits, as it already does, a deed claim about the forger to those present
   — which is what lowers the citer's later weight as a teller (`decision/options.py::record`,
   `teller_weight`). Nothing new is written for trust.
6. **Concealment.** A concealed Record is not held by the speaker and cannot be cited; no rule.

## Interface this needs from fieldwork's evidence model (for the FI lane)

1. **A citeable item has a stable id and a kind** from one roster (`rosters.yaml: proofs`), and FI
   says which of its products is which kind: a finding's deposited claim is `testimony`; a document
   (survey sheet, case file, forged or not) is `record`.
2. **A finding on a Record says whether it is forged**, as a term of the finding
   (`rosters.yaml: finding_terms`), on the Event `find_trail` already produces — so SC reads an
   Event kind and a term, never a Record's hidden field, and never a ledger other than the actor's.
3. **"Contradicts" has one owner** importable below `seam/` and `queries/` (today
   `decision.agreement`; if FI's model moves it, SC follows the owner).
4. **Examination of a cited Record is an ordinary inquiry** (`examine`'s row), not a contest: the
   ruling *investigation must not be made a contest* is untouched. SC adds no prize to an inquiry.

## Conflicts with ruled items — named, not resolved

- **`ED-SC-0034` (3), "pool only it is"** places interposition/latitude in the pool, and the ruled
  obstacle form is *score/2 plus instance modifiers*. Proofs here stay where the built code puts
  them (an instance modifier on the obstacle, through `hearing`); the archived design's *"+1D per
  Finding cited"* (`scale_transitions_v30` §3, intent only) would put them in the pool. The code's
  placement is kept; the difference is stated.
- **No verifier oracle (axiom, cited in D_T06 rows 3 and 12).** A contradiction check compares two
  HELD items; it never asks the Event log which is true. A false item that contradicts a true one
  strikes it. That is intended and is the risk the forger runs in edit 5.
- **F8.** Every read above is the actor's own ledger, a World `Record`, a `Tenure` or an Event.

## Gate (execution artifact)

On SC-P3's `build_hearing` world: (a) an accuser cites two held deed claims and a held Record; the
case file gains three `proof:` stages; `hearing` rises by `3 × proof_step`. (b) The accused answers
one with a held contradicting claim at a planted `Success`: one `struck` stage; `hearing` falls by
one step. (c) A third person examines the cited Record, planted forged: its stage is struck and the
accuser's `teller_weight` in the examiner's eyes falls. Control: the same world with nothing cited
reproduces SC-P3's `--auto` hash.

## Falsifier

An answer citing an item that does NOT contradict (same value) must strike nothing. A cited item
the speaker does not hold must be refused before the draw. If `hearing` moves when an item of a kind
the row does not admit is cited, the admission read is wrong.

## NERS reading

- **N**: top-down a trial is evidence answered; bottom-up the items, the roster, the Record and the
  contradiction rule all exist; lateral it is `tell`'s held-claim rule applied to `speak`; diagonal,
  fieldwork's product becomes the hearing's input and the hearing's record becomes fieldwork's object.
- **R**: a case can be built over seasons and broken in one; which item to hold back is strategy; a
  forgery is a bet. Without a player: an NPC who holds the contradiction strikes the proof.
- **S**: one carrier; no second proof arithmetic; the persistent board the three-lens audit asked
  for (a non-stationary per-turn decision) with general verbs able to reduce every state.
- **E**: one payload shape, one roster read, two stage labels, against evidence that can be argued.

## Cost class

Small build, after CR-61, SC-02 and SC-P3.
