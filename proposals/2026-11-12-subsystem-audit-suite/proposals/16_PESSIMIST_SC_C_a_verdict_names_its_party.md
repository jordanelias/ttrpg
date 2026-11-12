# 16 · PESSIMIST · SC · C — A verdict names its party: the sentence is witnessed as done to someone, and is credited as the judge is credited

## Status: PROPOSED (not ratified by being written; `CLAUDE.md` §2)

Finding: `audits/16_PESSIMIST_SC.md` F-PES-SC-03 (§2.4, §2.3). Runs: `runs/PES_SC/p4_verdict.py`,
`p3_hearing_ends.py` (b), `realm_sc.py` (seed 1). Edit 1 is SC's; edit 2 touches `person_q.regard`,
whose owner is the telling workplan (lane IN) and is listed for CHAR.

## What it changes in `engine/season/` at runtime

Every person who witnesses or is told of a determination holds a claim that names the person sentenced
(edit 1). A person's regard for someone he knows to be under sentence falls by an amount scaled by how
he regards the judge, and rises if he holds the judge in contempt (edit 2, shipped at its control until
swept). Hashes move in any world where `matter.determined` or `arrest.made` is emitted; declared.

## The problem, measured

`p4_verdict.py`: two real seasons with WITNESS, against a control with the case opened and never
determined. In all three disposal kinds (`oblige`, `detain`, `ban`):

| | after a verdict |
|---|---|
| each of the four other persons' new claims naming the convicted (the convict himself included) | 0 |
| their new claims naming the judge | 3, plus 2 on the edge's own id |
| regard for the convicted | 0.0 → 0.0, every person |
| regard for the judge | 0.0 → +0.18, every person, the convict included |

After a **failed** determination (`p3_hearing_ends.py` (b)) every person alive holds
`(party, matter.undetermined)`. So the accused's name is published exactly when nothing was decided.

Cause, at the owner: `epistemic.claim_subjects` names an act-caused Event's actor and each change's
subject, reading a `hold` edge as its two ends and *"every other edge by its own Tenure id"*
(`epistemic.py::_hold_tenure_ends`; the act's `subject` is named only when the Event changed nothing,
which is why a Failure names the party). `queries/world_q.py:5403-5427` records the consequence itself:
*"`matter.determined` deposits the judge and the disposal edge … no CLOSING claim names the matter, so
nothing he holds says the docket on it ended"*, and drops its DOCKET arm for that reason; `arrest.made`
is recorded there as depositing *"the arrester and the `detain` edge's own id, NEVER THE PRISONER"*.

In the realm (seed 1): the one verdict of three seasons (`p_npc_021` binds `p_npc_004`, Partial) is cited
by 254 `claim.deposited` Events; 0 persons hold a claim of it naming `p_npc_004`; the same judge opens a
second case against him the same season.

## The resolution, decided

1. **A restraint or an imposed service is read as its two ends**, as a `hold` is. The scoping that kept
   `commit`, sworn `oblige`, `succeed`, `tie` and `knot` opaque (a moral fact nobody ruled witnessable,
   `claim_subjects`' own warning) is kept: only `RESTRAINT_KINDS` (`detain`, `ban`) and an edge with
   `Tenure.imposed` (a sentence, `payload[DETERMINED_BY]`) are widened. A sentence is a public act by
   its nature; the Event already travels on the public channel. Ladder step 4 (the `hold` precedent, one
   line over) with step 3 (`world_q`'s named gap).
2. **A sentence is the judge's word about the party, credited as the judge is credited.** No new table:
   the relation a hearer already applies to a teller (`teller_weight`'s
   `relation = 1 + regard_gain × clamp(regard(p, teller) / STANCE_MAX, −1, 1)`, in `[0.5, 1.5]` at the
   shipped gain) is applied to the judge. For each sentence `p` knows of on `x`:

       Δ regard(p, x) = − sentence_gain × relation(p, judge)          (relation = 1 where p cannot name the judge)

   A hearer neutral to the judge lowers his regard for the convicted by one `sentence_gain`, one who
   reveres the judge by 1.5, one who despises him by 0.5 — and, at `regard_gain` 1.0 (the sweep's top),
   by nothing: the convict of a hated court loses no standing. Shipped at `sentence_gain = 0` (the
   control: today's behaviour) until its sweep is read; proposed first live value 1.0 on the stance
   scale (one valence step at weight 1), swept 0 / 1 / 2.
3. **A failed determination stops publishing the accused.** Follows from 1 with SC-P6: once Failure
   writes a `dismissed` stage on the case file (`05_SC_acquittal.md`, G-55), its Event has a change and
   the empty-changes rule no longer lands the claim on the act's subject; the claim names the case file
   and, through `DOCKET_PETITION`, the matter. Until SC-P6 lands the asymmetry stays and is this
   proposal's stated residue.

## Exact edits

1. **`engine/season/epistemic.py::_hold_tenure_ends`** — renamed `_public_edge_ends`; the test becomes

   ```python
   if t is not None and (t.kind == "hold" or t.kind in RESTRAINT_KINDS or t.imposed):
       return (subject,) if t.subject == t.object else (t.subject, t.object)
   ```

   (`RESTRAINT_KINDS` from `data/rosters.py`). Both callers (`claim_subjects`, `seen_subject`) take the
   new name. The docstring's *"any other subject, including a non-`hold` Tenure id … passes through"*
   is narrowed to the kinds that still do.
2. **`engine/season/rosters.yaml` and `queries/person_q.py::PAIRED_KINDS`** — a closed roster
   `patient_kinds` (`matter.determined`, `arrest.made`), unioned into `PAIRED_KINDS`
   (`person_q.py:226`, today *the deed kinds no single row emits*). The reason is that definition's own
   (`:223-225`): a paired kind is one *"whose claim subject may be the doer OR the patient"*, and after
   edit 1 these two are. Without it `attributed_deeds` reads `(party, matter.determined, True)` as an act
   *of* the party (an unpaired kind's subject is its doer, H-192) and would credit the convict with
   judging. With it, the deed is judged once, for the doer named by the `seen.who` pairing, as
   `lean × bond` (`deeds_judged`'s IN-58 rule), and `suffered_deeds(ledger, x)` returns the sentence.
   ⚠ This changes what a verdict earns its judge: today +0.18 from every holder of the same pursuits,
   the convict included; after, `lean × stance_toward(p, convict)`, so the convict's friends resent the
   judge, strangers are unmoved, and the convict's own regard for his judge no longer rises. Declared;
   it removes the inversion measured in the audit's §2.4.
3. **`engine/season/queries/person_q.py::deeds_judged`** — a third returned half, `sentenced`: over
   every deed claim `(referent, k, True)` with `k` in `patient_kinds` that `p` holds and whose paired
   doer (where the pairing names one) is not `referent`, the sum of `−relation`, with
   `relation = 1 + regard_gain × clamp(stance_toward(p, doer) / STANCE_MAX, −1, 1)` when a doer is
   paired and `1` when none is (a told copy carries no sighting today; `08_FI_06_testimony-names-a-hand.md`
   is the edit that lets a told sentence name its judge, and this half reads it when it lands). The
   stored half of regard is used for the doer, so nothing recurses through `deeds_judged`. `regard` adds
   `sentence_gain × sentenced`.
4. **`engine/season/data/fixtures.py`** — `sentence_gain = 0.0` (swept 0 / 1 / 2; hole-register row,
   graded `assumption`: no document gives the magnitude).
5. **`engine/season/queries/world_q.py`** — the DOCKET arm dropped at `:5416-5422` can be restored on
   `matter.determined` as its closing claim; that is a separate edit for the owner of that reading and
   is named, not made, here.

## Gate (an execution artifact)

`p4_verdict.py` after edits 1–2: "new claims naming the party" is at least 1 for every witness in all
three arms, 0 in the control; regard for the judge is 0.0 for a witness with no stance toward the
convicted and non-zero, signed by that stance, for one who holds one. With `sentence_gain = 1`: regard for
the convicted falls for every witness, by more for one given a positive stance toward the Duke and by
less for one given a negative stance (three hearers planted at −25, 0, +25; the run prints three
distinct values in that order). Control: `sentence_gain = 0` leaves every regard as today.

## Falsifier

A determination after which some person co-present or reached by the public channel holds no claim
naming the party. Present today for every person.

## NERS

- **N**: cut edit 1 and a verdict is again a private fact between the gate and one tenure; nothing a
  person can know says who was sentenced. From the other directions: FI (a case's ending becomes a
  claim an inquiry can find), WR (the chronicle can name the convicted), FA (a faction can know its
  member was bound).
- **R**: the no-player half gains the martyr and the disgraced; both are readings of one sum over what
  each person already holds. Complete at the extremes: a hearer who knows nothing of the judge reads
  the neutral value; a judge sentencing himself is refused upstream.
- **S**: the sentence is weighed by the same relation a told claim is; one method.
- **E (ratio)**: one widened test, two roster members, one summed half, one fixture; a player can say
  "people think less of a convicted man in proportion to what they think of the court".

## Cost class

Edit 1–2: edit. Edits 3–4: small build behind a control at 0 (design-first only in its magnitude).
