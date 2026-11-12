# INST-SYN-C — the crossings: what one institution's instrument does inside another institution's draw

## Status: PROPOSED

Source: `audits/15_INSTITUTIONS_SYNTHESIS.md` §5 (the interlock map; the chains of §5.2) and §6; Jordan,
as `INSTITUTIONS_BRIEF.md` records it: *"which sanctions and favours cross institutions (excommunication
against a duke, a loan against a throne, a charter against a rival, a deed certified by one body and
contested by another)"*. Composes on `15_INSTITUTIONS_SYNTHESIS_A` (the registry, `forborne`, `owed_to`),
`15_INSTITUTIONS_VENICE_A` (`obligation`), `15_INSTITUTIONS_PAPACY_D` (the sentence, the writ, the
answer), `15_INSTITUTIONS_COLONIAL_A` (`kept`, `breaches`), `15_INSTITUTIONS_VENICE_B` (`debt_suit`),
CR-60 (a bench's `scope`), CR-88 (the duty decline), SC's evidence weight. Batch I-7. Ratifies nothing.

## What it changes in `engine/season/` at runtime

Seven small edits, each at the seam between two families' proposals, where neither family wrote the whole
rule because half of it belonged to the other.

1. A person who has chosen to shun a man, or who holds a breach against him, is **excused**: his own
   oath to that man's seat no longer weighs in that man's favour, and CR-88's duty decline no longer bars
   his own `release` of it. One person-side predicate, two readers.
2. A complier with an `avoidance` does not seat the avoided man: the secular arm is each conferrer's own
   answer.
3. A suit for debt may be docketed before any bench that sits over the debtor. No code; stated because
   it is how a bond reaches a throne.
4. Two certificates for one seat on opposite sides of a hearing stand against each other, item by item.
5. A grant that forbears a levy is `evidence` against that levy, when the levied know of it.
6. A hand may belong to another faction than the seat whose paper it passes.
7. A sanction's publication addresses everyone on the issuing seat's ground; an order addresses only
   those the seat commands. One key on the form row.

With no `avoidance` complied with, no instrument breached and no certificate cited, nothing moves.

## The problem (evidence)

- `15_INSTITUTIONS_VENICE_A` gives `obligation` a lift: "a live `ban` on the actor whose seat's faction is
  the counterparty's … count 0". `15_INSTITUTIONS_PAPACY_D` §3 gives the excluded man's sworn men a
  different effect: after his own `comply`, "CR-88's duty decline does not bar his `release`".
  `15_INSTITUTIONS_COLONIAL_A` §4.2 gives a breached party a third: `release` of his own oath "which a
  known breach makes cost him no regard". Three statements of one idea (a man is excused from what he
  owes someone who is under sentence, or who broke faith first), keyed three ways, in three files.
- `06_FA_seat_terms_and_turnover.md` edit 6 scopes a `ban` to the banning seat's purview. A Church
  bench with a realm `scope` (CR-60) still acts only where its `rung` reaches (`15_INSTITUTIONS_PAPACY_A`
  edit 3: "judging reach, not acting reach"). So after both land, a man excommunicated at Himmelenger may
  be seated in any crown seat: the sentence bars him from Church seats and from nothing else, and no
  proposal says what stops a king appointing him.
- `15_INSTITUTIONS_VENICE_B`: recourse on a lapsed bond is a suit "before a bench whose purview reaches
  the debtor". For a debtor who holds a realm seat no file says which bench that is.
- `15_INSTITUTIONS_PAPACY_C` and `15_INSTITUTIONS_BYZANTINE_A` each let a body certify a deed; neither
  says what happens when two bodies' certificates meet in one room.
- `15_INSTITUTIONS_COLONIAL_B` §2 gives a levy favourable `evidence` (an assessment; the instrument that
  confers the collector's seat). `15_INSTITUTIONS_COLONIAL_A`: "an immunity is not a wall". Nothing makes
  an immunity matter at the moment it is breached, except afterwards in `kept`.

## The resolution, decided

Ladder step 5 throughout: each is the one-owner statement of a rule two lanes wrote halves of. The
sanction's force stays where `15_INSTITUTIONS_PAPACY_D` put it: in other people's answers, each drawn.

## Exact edits, by owner

### 1. `engine/season/queries/person_q.py::excused(p, holder_id) -> bool`

Person-side, computed when read, no World:

```python
def excused(p, holder_id) -> bool:
    """Is `p` excused from what he owes `holder_id`?  True when EITHER
    (a) `p` shuns him: among `p`'s own live `oblige` Tenures carrying OBEYED_WRIT, one obeys a writ whose
        form has a `forbears` clause `over: named` and whose content (in `p`'s own claim of it) names
        `holder_id`;                                                    -- he chose to comply; it was a draw
    (b) `p` holds a breach against him: `kept(p, r) < 0` for a live instrument `r` in `p`'s ledger whose
        bound party is `holder_id`.                                     -- the other side broke faith first
    Nothing is written.  A man who never heard of the sentence or the breach is not excused."""
```

Two readers and no third:

- **`person_q.owed_to`** (`15_INSTITUTIONS_VENICE_A` edit 3): an edge toward a seat whose holder, as
  `p`'s own ledger names him, `p` is excused from counts 0. This replaces VEN-A's ban-keyed lift.
  `[UNVERIFIED]` that a person can read who holds a seat he is sworn to: `20_NARRATIVE_CHURN.md`
  F-NARR-04 finds no `held_by` claim is deposited today; the reading is the one `14_VERBS_BINDING_C`
  edit 9 adds (his newest `tenure.opened` claim naming the seat). Until that lands the predicate takes
  the seat and reads the avoided or breaching person from the writ or instrument, which names him.
- **CR-88's duty decline** (when built; `15_INSTITUTIONS_PAPACY_D` edit 8, generalised): it does not
  decline `p`'s own `release` of an `oblige` to a seat whose holder `p` is excused from. Whether he
  releases is his own score.

An oath is never dissolved by rule. `gate.py::purview_reaches`' oath clause is untouched: the oath still
puts the vassal's ground under his lord until the vassal himself releases it.

### 2. `engine/season/instruments.yaml: forms.avoidance` — the secular arm

One clause more (carried in `15_INSTITUTIONS_SYNTHESIS_A`'s row): `{by: addressee, kind: tenure.opened,
over: named}`. A conferrer who has complied has every `confer` on the avoided man declined from his own
opening set (`forborne`). A conferrer who defied, construed or never heard may seat him, and that
appointment is a deed the sentencing faction's goals act against. FA-P3's scoping of a `ban` to the
banning seat's purview stands: the Church bars him from its own seats by law and from everyone else's by
persuasion.

### 3. The forum of a suit (no code)

`debt_suit` (`15_INSTITUTIONS_VENICE_B` edit 6), `audit` and `quo_warranto`
(`15_INSTITUTIONS_COLONIAL_C`) are docketed by `open_case` before a bench for which `may_determine`
holds, which asks `sits_over(seat, home_of(party))` (`state/gate.py:899-978`, as
`15_INSTITUTIONS_PAPACY.md` §1.1 reads it). The creditor, the grantor and the complainant choose the
bench. For a party who holds a realm seat the benches that sit over him are his own judges and, after
CR-60 and `15_INSTITUTIONS_PAPACY_A` edit 3, the three Church benches of realm scope. Stated in
`arrangements.yaml`'s header comment for `debt_suit`: *"a suit is brought where a bench sits over the
debtor; for a holder of a realm seat that is his own court or the Church's."* A `ban` disposed there is a
Church `ban` and may be published by an `avoidance`.

### 4. Rival certificates — a request to SC's evidence owner (not edited)

`05_SC_evidence_and_rebuttal_B.md` already has the arithmetic: items filed `for` the docket are `proofs`,
items filed `against` are `rebuttals`, and the `evidence` term is `proof_step × (rebuttals − proofs)`. A
rival's deeds do not contradict the claimant's (they are different cells), so nothing is struck; they
stand against. The one sentence asked of that file's owner: **a Record carrying `recites` for a seat is
admissible on either side of any docketed matter whose petition names that seat**, each recited deed
filed as one item (`15_INSTITUTIONS_SYNTHESIS_B` edit 4). A certificate does not outrank another by who
made it: a bench's disposition to the body that made it is already in `reception`, and an impeachment
that draws Overwhelming strikes every item of the forged paper's origin by that file's rule 1.

### 5. A grant against a levy — a request to the MATERIAL lane (not edited)

On `requisition` and `seize` (`14_VERBS_MATERIAL_B` §4, `14_VERBS_MATERIAL_D` §6), the `evidence` term
has two halves: for the actor, a held assessment and the instrument that confers the exercised seat
(`15_INSTITUTIONS_COLONIAL_B` §2); **against** him, a live instrument one of whose `forbears` clauses
names this act's success kind over this ground, when the levied cohort or holder holds its content
claim. Unit: SC's `proof_step` per instrument. An immunity nobody on the ground has heard of protects
nothing; one the whole town holds makes the levy harder and its taking a known breach.

### 6. `engine/season/data/rosters.py::_load_offices` — a hand's faction is free

`passes_through` (`15_INSTITUTIONS_BYZANTINE_C` edit 1) admits a body or a seat of any faction, and the
loader does not compare factions. `15_INSTITUTIONS_BYZANTINE_D` edit 5 already relies on it (a Guild
seat's paper across the gate passes the Altonian trade prefect's hand). The basis rule `hand` in
`data/requires.py` asks only that the actor hold the named seat or a seat of the named body; BYZ-C's
further conjunct ("drawn up at a rung the issuing seat's purview reaches") is about the issuing seat and
stands.

### 7. `engine/season/instruments.yaml: forms[].basis` — a publication is not a command

`14_VERBS_BINDING_D_orders.md` edits 3 to 5 narrow `issue`'s addressees from purview over a person's
place to **command**: a seat's sworn men, the holders of seats it may revoke, and the unseated within
its purview (that audit's §13.4 decision 1, listed for Jordan). `15_INSTITUTIONS_PAPACY_D` §3 addresses a
writ of avoidance "to the persons its issue reaches". Under command a see could not address a lord's
seated vassals at all, and they are the persons the sanction is aimed at.

Decided: the basis is a property of the **form**. A form row carries `basis: command | purview`
(default `command`); `issue`'s `authority` conjunct asks the basis the chosen form names, and the bare
decree (no form) asks `command`. `avoidance` is `purview`: a sentence is published to everyone on the
issuing seat's ground, and it orders nobody to do anything (its clauses are all forbearances). `interdict`
and `tithe` stay `command`: they address the issuer's own seat-holders. If Jordan takes territorial
authority for every writ (that decision's option A), the key reads `purview` on every row and is inert.
One conjunct, one reader, no second predicate: both basis values are that proposal's. A form whose
`basis` is `purview` is a publication in the other sense too: its terms reach its addressees with the
news of its issue (`06_FA_decree_binds.md` edit 2's deposit), whichever way Jordan rules on whether an
*order* must be delivered by hand (`audits/06_FA_audit.md` §11 item 1; `audits/14_VERBS_SOCIAL1.md` §15
D1). A sentence handed from parish to parish one paper at a time is not a sentence.

Ladder step 5: the distinction is the instrument's, and `instruments.yaml` is where an instrument's facts
live. `[UNVERIFIED]` that the `authority` conjunct can read a value sourced from the act's `form`
operand; if a `requires` cell cannot be keyed by an operand, `issue` gains a second row alternative for
published forms, which is the table's existing way to say "either".

## Gate (execution artifacts)

Hand-built worlds through the real fold, `PYTHONHASHSEED=0`.

1. **Excused by his own compliance.** A lord, a vassal sworn to his seat, a published `avoidance` naming
   the lord. Arm A: the vassal's `comply` drew Success. Arm B: it drew Failure. The lord then `petition`s
   the vassal: the recorded term list carries `obligation` at 0 in A and at `obligation_step` in B. Arm
   C: the vassal never received the writ: as B.
2. **The oath stays his.** Over 200 seeds of arm A with CR-88's decline built: the vassal's `oblige`
   closes only by his own `release`; a vassal with a planted grievance releases more often than one
   without, and neither always nor never (`15_INSTITUTIONS_PAPACY_D`'s gate, now through `excused`).
3. **Excused by a breach.** A duke under a seeded `homage`; the King's `requisition` inside the duchy
   succeeds and the duke witnesses it. `kept` as the duke reads it is below zero; `excused(duke, king)`
   is True; the King's next ask of him carries `obligation` at 0. Control: the levy unwitnessed by the
   duke and untold: `excused` False.
4. **The secular arm.** Two conferrers addressed by one `avoidance`; one complies, one defies. The
   first has no `confer` candidate naming the avoided man; the second has, and its Event is a deed the
   issuer's faction holds.
5. **A bond before the Church.** A `debt` lapsed whose debtor holds a realm seat. `open_case` under
   `debt_suit` is admitted before a bench of realm scope and refused (`may_determine`) before a ducal
   bench. Over 200 seeds all four bands occur; a `ban` disposed there reads CH on the strife instrument.
6. **Rival paper.** A consecration hearing with the claimant's certificate cited, with and without a
   rival's certificate for the same seat cited against it: exact odds printed; the advantage shrinks.
7. **The immunity in the levy.** 400 seeded levies on a ground under a seeded `immunity` the cohort
   holds a claim of, and 400 on a like ground without: Failure's share is higher inside; each arm holds
   at least three bands. Control: the cohort holds no claim of the grant: the arms' shares are equal
   within sampling.

## Falsifier

- An `oblige` that closes with no `release` act of its owner.
- A man excused who holds no claim of the writ, the sentence or the breach.
- Every vassal of a sentenced lord releasing in every seed (the sanction is a switch).
- A complier seating the avoided man; a defier unable to.
- A suit admitted before a bench that does not sit over the debtor.
- An immunity that refuses a levy at the gate.

## What it does not do

It gives no institution a power over another. It adds no sanction: every sanction here is
`15_INSTITUTIONS_PAPACY_D`'s `ban` and writ, `15_INSTITUTIONS_VENICE_B`'s suit, or
`15_INSTITUTIONS_COLONIAL_C`'s calling-in. It does not try usury: a bond whose `amount` exceeds what was
advanced in the same kind at the same place is a fact an inquiry can reconstruct
(`15_INSTITUTIONS_VENICE_B`), and a goal row that acts on it needs a deed pairing no reader has; it is
recorded as not built. It does not decide who may judge the Confessor (audit §10 item 3).

## NERS reading

- **N.** From above: a sentence on a duke works if his men choose it to. From below: a vassal weighs a
  writ against his lord, and a town weighs a charter against a collector. Laterally: a banker, a bishop
  and a king meet in one suit. Diagonally: a hearth's knowledge of an immunity moves a realm officer's
  levy. Remove these six and each family's sanction stops at its own border: an excommunicate may be
  appointed chancellor, a king cannot be sued, and an immunity is noticed only after it is broken.
- **R.** Every crossing is a choice with a draw behind it and another person's choice after it. With no
  player, a sentence on a loved lord and on a hated one play out differently from one rule. Complete at
  the extremes: nobody complies, nothing happens; everyone complies, the man is alone, alive, and can
  swear a penance.
- **S.** One predicate where three keyed lifts stood; one forum rule (the gate's own); `evidence` with
  two halves in SC's one term. Nothing pauses differently: each crossing is a hearing, an ask or a levy
  like any other.
- **E, last.** One predicate, one clause, two requests, two sentences of comment. The player's rule of
  thumb: *a sanction is worth what the people around its target decide it is worth.*

## Cost class

Small build (edit 1); edit (2, 3, 6); two requests to other lanes (4, 5).
