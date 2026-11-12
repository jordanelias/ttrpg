# FA-P1 — a decree that binds: terms reach the addressee, the answer is a choice, defiance is the issuer's occasion

Reconciled: 2026-11-12, U5d closure — folded Jordan's answers (`unified/DECISIONS_ANSWERED.md`). **A-21** rules the decree proclaimed: edit 1's `public_terms: true` is no longer an `[ASSUMPTION … Jordan to correct]` (it is the ruled form; its revert stays as the test arm), and the audit's §11 item 1 is closed. **A-22** (command, not territory) rewrites who is bound: in edit 3, `writs_addressed` forms `comply`, `evade / defy` and `construe` only where the issuing seat commands the addressee (his sworn man, the holder of a seat it may revoke, or an unseated person in its land; the one predicate is `16_PESSIMIST_FA_C_under_the_seat.md`'s as reconciled); a writ whose addressee the seat does not command forms as a petition to him and enters no `suspicion_of` count (edit 4's fold counts commanded addressees only). **A-23**: a holder in custody forms no act through his seat, so `issue` and `revoke` by a detained issuer are refused at formation (the one check is `U5d_FA_owed_edits.md` §2). **A-24 / A-47**: `recall_suspicion` opens the issuer's question and decides nothing; the recall itself is `revoke`'s resistible draw (`14_VERBS_BINDING_C_turnover.md`), and for a Church officer the head's strip (A-35). Steps rewritten: edit 1 (tag), edit 3 (second clause gains the command conjunct), edit 4 (the fold's domain). Edits 2 and 5, the gate and the falsifier are unchanged; one gate arm is added: a writ addressed to the issuer's superior yields no `comply` candidate.

Reconciled: 2026-11-12, wave 3 (W3-3) — applied D-U1-05 (edit 1 becomes the `dispensation: [issue]` entry of lane A's `rosters.yaml: read_to_addressee`; edit 2 is the existing `witness.py::addressee_reads` path, no second loop; this also dissolves R3 §1's AMBIGUOUS reading of edit 2, since `addressee_reads` reads the Record's own kind and verb); D-U1-11h (the kind stays `dispensation`; no rename precedes edit 1); R3 §2 rows on edits 3–4 (A-81 a write per band; the archived "recalls, audits or replaces" sentence follows the head, A-24/A-47); C3-C13 (the petition route is subject to A-63/A-64); the A-21 sentence in "The resolution" (no longer listed for Jordan); 7b-1 (named tests, edit order); 7b-0 (tier); U3 C3-D5 (batch and order). The "What it changes" list, edits 3–5's mechanism, the falsifier's bystander and crowd-out arms are unchanged.

## Status: PROPOSED

Lands in batch: B21 (FA governance), in C3-D5's order: after `14_VERBS_BINDING_C_turnover`'s `revoke` draw at its control, before `16_PESSIMIST_FA_C_under_the_seat`'s command predicate and BIND_C's flip.
Depends on: B01 (implementation lane A's branch: `rosters.yaml: read_to_addressee`, `loop/witness.py::addressee_reads`); `14_VERBS_BINDING_C_turnover.md` (B21, the `revoke` draw); `16_PESSIMIST_FA_C_under_the_seat.md` (B21, the command predicate of A-22); `U5d_FA_owed_edits.md` §2 (B21, custody, A-23); `28_CORE_scene_access_A`–`C` (B28/B38, the petition route only).

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
reading of H-207 (A): a general motive is licensed, a special case is not). The choice between a proclaimed decree and a delivered one is
ruled: A-21, proclaimed (the audit's §11 item 1 is closed).

## Exact edits, by owner

**1. `engine/season/rosters.yaml: read_to_addressee`** (lane A's roster, B01; the one owner of "which
Records' content reaches their addressee without his holding the paper", D-U1-05). Its shape becomes a map
from a `record_kinds` member to the verbs whose mint of that kind is put to the addressee, and it gains
`dispensation: [issue]` beside `challenge: [challenge]`. The verb qualifier is needed because `covenant`
also mints a `dispensation` (`verb_table.yaml:319`) and its counterparty learns the terms only by holding
the Record (A-21 keeps covenants in person). The loader `data/rosters.py` refuses at import (a) a key that
is not a `record_kinds` member, (b) a key whose content keys hold no addressee key (`record_kinds`'
`addressee:` map), (c) a verb that is not a `verb_table.yaml` row or whose effect does not mint that kind.
The ruled form (A-21); the revert drops the `dispensation` entry, and the deposit and the formation both
fall back to today's. The earlier `record_kinds.dispensation.public_terms: true` cell is not made (it would
give one `record_kinds` member a second shape; D-U1-05).

**2. `engine/season/loop/witness.py`: no new loop.** The fourth deposit (`:823-845` on `main`, the one writer
of `content:<kind>` claims) already calls `addressee_reads(rec, pid)` on lane A's branch (`witness.py:86`,
`:826`), which deposits `(rec.id, "content:<kind>", content_value(rec.subject_matter))` to a witnessing
addressee under the existing exact-triple guard. The only change is the predicate's test: the Record's kind is
a key of `READ_TO_ADDRESSEE`, the verb of the act that created it is in that key's list (read off the
creating act as `world_q.py:1582` reads it for `WRIT_MINTING_VERB`), and `world_q.addressed_to(rec.subject_matter,
pid)` (the verb list is `world_q.WRIT_MINTING_VERB`'s filter, `world_q.py:1604`, moved into data). Hash-equal at `{challenge: [challenge]}`. The holder's deposit is
untouched.

**3. `engine/season/queries/world_q.py::writs_held`** becomes `writs_addressed(w, p)`: the Records of a
`RECORD_REFERENT_KINDS` kind for which `p` holds the writ **or** `p`'s own ledger holds a content claim on
it whose addressee key names him (`content_said`, `addressed_to`), minus those he has already answered (a
`compliance.given` or `compliance.withheld` claim of his own doing on the same writ, read from his ledger).
The second clause is the new one; the third closes the standing scene tax the docstring records ("NO
'ALREADY ANSWERED' DECLINE"). `accept`'s `challenge` kind keeps the holding clause only, because a challenge
is not public. Every caller (`questions_for`, `admits_audience`) is renamed with it; `admits_audience`
keeps asking for a *held* writ, since entry on a writ is the paper's.

A write per band (A-81: every graded band of every verb leaves a durable change). The three answers are
emission rows whose write is a claim WITNESS deposits in the actor's own ledger and, where he witnesses it,
the issuer's: `comply` emits `compliance.given`; `evade / defy` emits `compliance.withheld`; `construe` emits
`terms.distorted` (its row's `writes_note`, `verb_table.yaml:1332`: "the construer's reading is a BELIEF …
that deposit is his reading"). A refused answer (`compliance.impossible`, `construal.impossible`) leaves the
actor's own claim of the refusal through the `a_refusal_is_remembered` carrier (A-81 consequence 1,
`16_PESSIMIST_CORE_a_refusal_is_remembered.md`), not a fold-only trace. H-260's "obeying and defying leave
the world identical" is therefore false of the ledgers once this lands, and stays true of the store cells
(what compliance performs is the separate act the terms name, H-44).

**4. Suspicion as a fold, and the recall as an occasion.** The intent is ruled, and the archived design
states it (reference only, `CLAUDE.md` §0.05): a Directive is answered by Comply, Bargain or Defy; a Defy
adds one to a suspicion signal, capped at one a season (`governance_play_redesign_v1.md` §1.4;
`governance_consolidation_v1.md` D5, ED-IN-0046). The archived design then had the superior recall, audit
or replace at a threshold; under A-24 and A-47 the threshold only opens the issuer's question (the recall
occasion below) and decides nothing, and the recall itself is `revoke`'s resistible draw
(`14_VERBS_BINDING_C_turnover.md`). D6
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
That route is subject to A-63 and A-64 (C3-C13): the visited issuer is engaged by a visit, visitors are
seen in an order weighted by rung, a visit may be booked, and a petition kept waiting intensifies
(`28_CORE_scene_access_A_occupancy_and_precedence.md`, `_B_appointments.md`, `_C_the_petition_that_waits.md`).

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

Named tests (7b-1), a new file `engine/season/tests/test_fa_decree_binds.py` (the hole-register text's
`test_in10c_writ_reaches_addressee.py` does not exist on `main`), each loop asserting it asserted
(`assert checked >= N`, CLAUDE.md §0.1 pt 2): `test_a_bystander_is_offered_nothing`,
`test_an_addressee_is_offered_comply_defy_construe`, `test_writs_addressed_nets_an_answered_writ`,
`test_dispensation_absent_from_read_to_addressee_reproduces_the_hash`,
`test_a_covenant_counterparty_holds_no_content_claim` (D-U1-05's falsifier, beside lane A's
`test_b11a_duel_reach.py`), `test_suspicion_floors_at_zero_and_a_complied_season_delays_the_recall`,
`test_a_writ_to_the_issuers_superior_forms_no_comply` (A-22). Edit order: 1, 2, 3, 5, then 4.

## Falsifier

- Control: the `dispensation` entry absent from `read_to_addressee` reproduces the pre-item `content_hash`
  at one and two seasons, realm seed 0.
- A bystander is offered nothing: a person who witnessed the issue and is not an addressee has
  `writs_addressed == ()` (the B10-05 close's defect, a bystander complying, must not return).
- Mutation: drop the `addressed_to` conjunct in `addressee_reads` and a non-addressee holds the content
  claim; the bystander assertion reddens. Drop the verb qualifier and a covenant's counterparty holds
  `content:dispensation`; the covenant test reddens.
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
Tier (CLAUDE.md §10, R3 7b-0): edit 2 `opus` with a `sonnet` critic (the deposit rule is shared by many
proposals); edits 1, 3, 4, 5 `sonnet`.
