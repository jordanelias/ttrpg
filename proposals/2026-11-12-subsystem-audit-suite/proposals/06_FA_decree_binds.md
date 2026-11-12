# FA-P1 — a decree that binds: terms reach the addressee, the answer is a choice, defiance is the issuer's occasion

## Status: PROPOSED

Source: `audits/06_FA_audit.md` F-FA-01, F-FA-02, F-FA-05, §6.2 R-01 to R-03, §11 item 1, §13 (NPC-083,
NPC-038, ARC-17), §15; hole rows H-260, H-207 (A), H-203; plan position CR-54.

## What it changes in `engine/season/` at runtime

1. A person who learns that a writ was issued, and whom the writ names as an addressee, also receives its
   terms as a content claim. Today only a holder does.
2. `comply`, `evade / defy` and `construe` form on a writ the person's own ledger names him an addressee of.
   Today they form only on a writ he holds, which in computed play is never.
3. An issuer whose suspicion of a subordinate, folded from his own claims of defied and obeyed writs, has
   reached a threshold carries, on the question he answers, that person and the seats he holds as classed
   referents (the recall).
4. `revoke` reads its office from `subject` as `confer` does, so the row can execute on such a referent.

No stored state, carrier, verb or remit act is added. No hold is minted to anyone but a Record's maker, so
ED-IN-0292 (1) stands as written. Each numbered change is a declared hash mover and ships behind its own
revert.

## The problem (evidence)

At `601e715`, `PYTHONHASHSEED=0` (audit §12, E-3 to E-5):

- Realm, seeds 0, 1 and 2, three seasons: 29, 21 and 41 `dispensation.issued`; 0 writs held by an addressee;
  0 persons for whom `world_q.writs_held` is non-empty; 0 `compliance.given`, 0 `compliance.withheld`.
- Spine, seeds 0 to 4, four seasons: 19 writs, the same zeros.
- `aperture 2 0`: `comply` attempted 33 and refused 33 on `exists:dispensation=0` (it formed on other
  Records); `evade / defy` 5 of 5; `construe` 7 of 7; `revoke` formed for 5 persons, attempted 0.
- Cause, in the code's own words (`queries/world_q.py:3234-3260`): "a writ is minted into its maker's hand …
  A writ reaches its addressee only by a `give`. `()` for nearly everyone." `give` executed once.
- Part E's cell for `comply`, kept on the row as `requires:`, is "a claim of the dispensation's terms is in
  the actor's own ledger". It never asked him to hold the paper; the holding test arrived with the
  formation (v9 IN-09, an `[ASSUMPTION; medium; Jordan to correct]`).
- H-260 (measured on hand-placed writs): obeying and defying leave the world identical.

## The resolution, decided

A writ made by `issue` is a public instrument: it is a `binding_decision`, already told to everyone the
chronicle channel reaches. Its terms travel with that news, to its addressees only. What the addressee then
does is his own act, chosen by his own ranking. What defiance costs is whatever the issuer, now holding a
claim of it, chooses to do: the chain is two persons' decisions, not a counter. `covenant` is unchanged: its
row says it "must not be read as a public writ", and its terms still reach only a holder.

Ladder: step 3 (Part E's cell) for the formation; step 5 for the route (WITNESS already deposits content
claims; the addressee test `person_q.addressed_to` and the claim reader `person_q.content_said` already
exist person-side); step 1 for what defiance costs (D5, D6 and E11 are ruled, ED-IN-0046 and ED-IN-0047;
the carrier question is superseded by ED-IN-0343 to ED-IN-0345); step 4 for the motive (CR-54's ratified
reading of H-207 (A): a general motive is licensed, a special case is not). The choice between a proclaimed decree and a delivered one is listed for
Jordan in the audit's §11 item 1, because the two are different games.

## Exact edits, by owner

**1. `engine/season/rosters.yaml: record_kinds`** (owner of what a Record kind carries). The `dispensation`
row gains `public_terms: true`. Loader `data/rosters.py` exposes `PUBLIC_TERMS_KINDS`, refusing the key on a
kind with no `addressee` content key. `[ASSUMPTION; medium; Jordan to correct; revert: drop the key — the
deposit and the formation both fall back to today's]`.

**2. `engine/season/loop/witness.py`, the fourth deposit** (`:823-845`, the one writer of `content:<kind>`
claims). Beside `newly_held`, collect per Event the Records it created whose kind is in `PUBLIC_TERMS_KINDS`
and whose creating act's verb is `WRIT_MINTING_VERB` (`issue`; the constant exists). In the deposit loop,
for each such Record, when `addressed_to(rec.subject_matter, pid)` and `pid` is being deposited this Event
by any admitting channel, deposit the same `(rec.id, "content:<kind>", content_value(rec.subject_matter))`
claim, with the admitting channel's `src` and `conf`, under the existing exact-triple guard. One loop, one
predicate; the holder's deposit is untouched.

**3. `engine/season/queries/world_q.py::writs_held`** becomes `writs_addressed(w, p)`: the Records of a
`RECORD_REFERENT_KINDS` kind for which `p` holds the writ **or** `p`'s own ledger holds a content claim on
it whose addressee key names him (`content_said`, `addressed_to`), minus those he has already answered (a
`compliance.given` or `compliance.withheld` claim of his own doing on the same writ, read from his ledger).
The second clause is the new one; the third closes the standing scene tax the docstring records ("NO
'ALREADY ANSWERED' DECLINE"). `accept`'s `challenge` kind keeps the holding clause only, because a challenge
is not public. Every caller (`questions_for`, `admits_audience`) is renamed with it; `admits_audience`
keeps asking for a *held* writ, since entry on a writ is the paper's.

**4. Suspicion as a fold, and the recall as an occasion.** The intent is ruled, and the archived design
states it (reference only, `CLAUDE.md` §0.05): a Directive is answered by Comply, Bargain or Defy; a Defy
adds one to a suspicion signal, capped at one a season; at a threshold the superior recalls, audits or
replaces (`governance_play_redesign_v1.md` §1.4; `governance_consolidation_v1.md` D5, ED-IN-0046). D6
(ED-IN-0047) makes the accrual cumulative on Jordan's condition that it has a symmetric counter: *"if there
is a way to advance suspicion from non-compliance, there must be a way to reduce suspicion by
over-compliance and consistency/predictability."* The verb table records that this waited on "a suspicion
carrier `engine/season/` does not have". ED-IN-0343 to ED-IN-0345 since ruled that such a quantity is an
accumulation of events, which CR-89 builds as a fold of the log with no stored value. So:

- `engine/season/queries/person_q.py::suspicion_of(p, other) -> int`, person-side and computed when read:
  over `p`'s own ledger, plus one for each season in which he holds a claim that `other` withheld compliance
  on a writ `p` made (at most one a season, the ruled cap), minus one for each season in which he holds a
  claim that `other` complied and none that he withheld (E11), floored at zero; distinct origins once
  (ED-IN-0322, as CR-89's believed fold). Nothing is written.
- `engine/season/queries/world_q.py::recalls(w, p)`, `vacancies`' shape: for each `other` with
  `suspicion_of(p, other) >= fx.recall_suspicion`, the person (classed `Person`) and each seat he holds that
  `may_revoke` admits through one of `p`'s seats (classed `Office`), stamped on `out[0]` by the one stamp
  site. It asks the gate's own predicate, so it names no seat the gate would refuse.
- `engine/season/data/fixtures.py: recall_suspicion`, shipped `3`, swept `{1, 3, 5}`, with its register row
  graded `assumption`: the design names a threshold and gives no number; its audit escape is worth two, so
  the threshold is read as above two `[ASSUMPTION; medium; Jordan to correct; revert: None, the occasion
  off]`.

Not built here, and named: the Recall as a scene in which the recalled officer answers (SC's hearing); the
`Submit to audit` escape; Bargain, whose nearest built verb is a `petition` to the issuer naming the writ.

**5. `engine/season/verb_table.yaml: revoke`** gains `referent_named: true` beside its existing
`referent_class: Office`; **`loop/predicates.py::_req_revoke`** and **`loop/effects_governance.py::_eff_revoke`**
read `office_named_by(a)` in place of `payload['office']` (`office` still wins where both are present, so
no hand-built act changes meaning). `office_named_by`'s docstring loses its "`revoke` IS NOT A CALLER"
paragraph. This is CR-54's `office_named_by` change; H-207 (A) is honoured because nothing scores `revoke`
specially: it forms only on a seat whose holder defied the actor's own writ, and competes on its ordinary
alignment cells.

## Gate (execution artifact)

`fa_probe`'s reading, or `aperture`'s per-verb block, on the spine at seeds 0 to 4 for four seasons and the
realm at seeds 0 to 2 for three:

- at least one `compliance.given` and one `compliance.withheld` whose actor is an addressee of the writ;
- at the sweep arm `recall_suspicion: 1`, after a `compliance.withheld` the issuer's next delivered question
  carries the defier's seat as an `Office`-classed referent (read with the spy `harness/heir_hears.py`
  already uses on `questions_for`); at the shipped `3` the same after three defied seasons on a hand-built
  world, and a complied season between them delays it by one (E11 observed);
- `revoke` attempted at least once pooled over the realm seeds; if it executes, `aperture` prints it with
  `Act.via` a seat whose `revocation` admits it. If it is attempted and never executes, that is recorded
  and the row stays an R-05 residue: the proposal is kept for the triple, not for `revoke`.

## Falsifier

- Control: `public_terms` absent reproduces the pre-item `content_hash` at one and two seasons, realm seed 0.
- A bystander is offered nothing: a person who witnessed the issue and is not an addressee has
  `writs_addressed == ()` (the B10-05 close's defect, a bystander complying, must not return).
- Mutation: drop the addressee test in edit 2 and a non-addressee holds the content claim; the bystander
  assertion reddens.
- Crowd-out: the executed counts of `issue`, `transfer`, `tell` and `speak` pooled over realm seeds 0 to 2
  are read before and after and printed; a fall is reported, not asserted against (rule V2).

## What it does not do

No stored suspicion carrier: D6's accrual and E11's reduction are a fold. No delivery of paper. No new consequence written by
`comply` itself: what compliance performs is still the separate act the writ's terms name (H-44). No change
to `covenant`, `petition` or `challenge`.

## NERS reading

- **N.** From above: a ruler's decree now has addressees who answer. From below: a governor has an order to
  weigh against her settlement. Laterally: the issuer's response uses verbs that already exist (`revoke`,
  `open_case`, `arrest`). Diagonally: a Church writ on Crown ground is answered or defied by Crown officers.
  Removing it returns the 91-writs, zero-answers reading.
- **R.** A real choice with two readers (the addressee's regard for the issuer; the issuer's response), and
  drama with no player: orders defied and offices lost for it. Complete at the extremes: a writ naming a
  dead man forms for nobody; an answered writ stops being offered.
- **S.** One methodology: a standing occasion stamping classed referents, as `vacancies` and `writs_held`
  already do. It pauses nothing and hands to SC (`open_case`) and PC (`arrest`) by existing seams.
- **E, last.** One roster key, one deposit clause, one widened Query, one fold, one occasion, one fixture,
  one reader swap. One new noun, suspicion, which the design already uses in its ordinary sense. Against
  what N and R buy, small.

## Cost class

Small build. CORE reviews edit 2 (`witness.py`); CHAR's regard decides how often anyone defies.
