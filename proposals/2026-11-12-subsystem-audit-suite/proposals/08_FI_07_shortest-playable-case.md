# 08 · FI · 07 — The shortest playable case: a loop on the season's own code path, and the two edits it needs

Reconciled: 2026-11-12, U5c closure (`unified/U5_CONFLICTS_U5c.md` C-24) — §2 (b)'s "deposited at every band" is read with `U5c_FI_residue.md` §8: the gating reads teach at every band and on a refusal; the listed non-gating reads are deposited by band through `finding_terms`, and none at Failure.

## Status: PROPOSED (§1, §3, §4 are harness edits; §2 is two small engine edits; nothing here is design-first)

Carries `audits/08_FI_audit_addendum_B.md` §B3d, F-FI-12 and resolutions R-35, R-37, R-44, R-46. It sits
beside `08_FI_03_playable-inquiry.md` (first FI lane): it changes none of that file's sections except §2's
band gate (R-35), and states the order in which the standing requirement (*a subsystem is a playable game
of its own, on one code path, integrated*) is met soonest.

## What this changes in `engine/season/` at runtime

§2 only. `examine` begins to form on Sites the actor has heard of (today it never forms: 0 folded acts at
seeds 0 to 2 over one to three seasons), and an admitted look deposits its reads to its actor at every
band. Both are declared hash movers on any realm world. §1, §3 and §4 are a scenario builder, a rendering
and an instrument: no engine change.

## The loop, and what each step runs on

| step | act | row or carrier | state |
|---|---|---|---|
| 0 | enter a place where a deed was done unseen and a paper handed on | `harness/scenarios.py::inquiry_world(seed)` (`08_FI_03` §1) | to build (harness) |
| 1 | hold the question *who did this* | a goal with a `deed_doers` object; its standing `need` question | exists (IN-67) |
| 2 | look: `research` the paper, `surveil` the place, `examine` the site | three graded rows; the observation deposit | two form today; §2 |
| 3 | ask: `interview`; the other answers by his own `tell` or `lie` | CP-T06-05 (B10-14) | scheduled |
| 4 | read the board | §3 | to build (harness) |
| 5 | conclude: `reconstruct` utters who | `08_FI_03` §3 | design-first |
| 6 | accuse: `petition`, `carry`, `open_case`, `speak` citing what he holds | `08_FI_05_B`; SC-P3, SC-P8 | SC's |
| 7 | the bench rules; the consequence is witnessed | `determine`; SC-P6 | SC's |
| 8 | the scene ends | `08_FI_03` §5's predicates | to build (harness) |

**Cut A (plays first; no engine change): steps 0, 1, 2 with `research` and `surveil`, 4, 6 without
citation, 8.** A person is seated on `play_surface.dispatching_chooser`; every act is a season row; the
ending is one of four predicates. It is thin by design: one route to the truth, nothing asked, no stated
conclusion, an accusation at the default roll. Its value is that the scenario, the board and the end exist
and run headless, so every later piece lands on something that already plays.
**Cut B (the first that is a detective game): Cut A plus §2 here, B10-14, `08_FI_06`, `08_FI_03` §3, and
`08_FI_05_B` with SC-P3 and SC-P8,** in that order. The order is forced: an answer cannot name a hand
before `08_FI_06`; a conclusion has no value space before a hand can be held by more than eyewitnesses; a
cited case has no bench before SC-P3.

## 1. The case is a goal (R-44)

No case object is added. `inquiry_world` gives the investigator one goal whose `object:` is
`{deed_doers: {kinds: [<the scenario's covert kinds>]}}`, the form `rosters.yaml: goal_object_kinds.forms`
already declares and `person_q.deed_doers` already answers from his own ledger. Its referents are his
suspects: empty until his ledger names someone, then exactly the persons it names, wrongly or rightly. The
candidates that form on them are the ordinary ones (`interview`, `surveil`, `petition`, `challenge`).
`[ASSUMPTION; medium; Jordan to correct]`: a scenario goal is authored in the builder as `build_realm`'s
ambitions are, not drawn.

## 2. Two engine edits

**(a) `examine` forms on a place (R-37, F-FI-12).** `decision/options.py:1213-1214` returns the question's
subject as `site`, and a subject is almost never a Site. Edit: `site` is choice-sourced for `examine`
(`rosters.yaml: choice_sourced`, `marshal`'s precedent through `operand_bags`), ranging over the ids in
`ledger_names(p.ledger)` that his own claims present as a Site: the subjects of his `condition` observation
claims and of `seen` claims deposited at a Site `[ASSUMPTION; medium; Jordan to correct; revert: the
question's subject]`. Person-side, World-free. The fold's existing conjuncts (the Site exists; the actor is
present at it) refuse the rest, and after R-35 that refusal teaches him why.
**(b) An admitted look teaches its reads at every band (R-35).** `08_FI_03` §2's `observes:` column is kept
as a list of non-gating typed reads per inquiry row; its condition *"when the band is `Partial` or better"*
is removed. The reads are attached to the act's Event whenever the act is admitted and deposited to the
actor by the observation deposit that exists (`observation_deposit_mode: actor`). The band governs one
thing only, which `rosters.yaml: finding_terms` already owns: what of a covert trail the finding shows. So
there is one band-keyed table for what an inquiry uncovers, as the register asked (H-218: a degree-keyed
product column *"would be a second owner"*), access is not behind the roll, and a `Failure` is no longer
silence. K-37 is untouched: nothing wrong is ever deposited.

## 3. The board (a rendering; no state)

`engine/season/harness/play_surface.py::board(p, fixtures) -> list[dict]`, read from the person's own
ledger and nothing else:
- one group per `(subject, predicate, value)`, with its claims' `source`, `chain`, `confidence` and `when`;
- per group, its support over distinct origins (`LedgerReader._support` under `ledger_weigh`, the reading
  clause 4 uses, so the board shows what his decisions weigh);
- a flag where two groups share `(subject, predicate)` and differ in value (the pairing `options._pair`
  makes): a contradiction he holds;
- the suspects line: `person_q.deed_doers` for his case goal, each with the claim that names him;
- documents on his `hold`, by kind and what they are about (`content_said`).
It is the archived Case Board's content with no stored connection object: a connection is two claims on
one subject. `headless --play` (SC-P3 edit 4) prints it before each choice.

## 4. The instrument

One summary line per scenario run, computed and not stored: which §5 predicate of `08_FI_03` ended it and
at which tick; whether the concluded or accused person is the Event's actor; and, in place of the archived
Exposure meter (R-46), **how many distinct persons hold a `seen` claim naming the investigator at one of
his inquiries** (a resolver-side read over ledgers at the end of the run; no chooser reads it, no field
holds it). An `aperture` line per inquiry verb (formed / refused / admitted / found) as `08_FI_03` §5 asks.

## Gates (execution artifacts)

- Cut A: `inquiry_world(s)` runs headless at seeds 0 to 19 with the shipped chooser in the investigator's
  seat for four seasons; every run ends by a predicate; two runs of one seed give one content hash; a
  scripted callback that never inquires ends by the budget predicate (the choice is load-bearing).
- §2 (a): `examine` folded > 0 in `build_realm(0..2)` over one season, against 0 today; a planted
  investigator who holds a claim about a Site and stands elsewhere forms it and is refused.
- §2 (b): at seeds 0 to 2 the count of firsthand cell claims deposited from inquiry Events is above 0 at
  every band including `Failure`, against 0 from `Failure` today; the trail deposit is unchanged (the
  tree's own `test_fi03_trail.py` reads the same).
- The board: for the scenario's investigator after one season, every claim in his ledger appears in exactly
  one group, and the suspects line equals `deed_doers` of his goal.

## Falsifiers

- If after §2 (b) clause 4 declines more acts the world would have admitted (stale firsthand cells), the
  `world says True` share of declines rises from today's 1 to 2 in about 460; read it before and after and
  report the pair.
- If `examine` forms on a Site and is refused at the same rate it forms, the bag is naming places he is
  not at; the fix is then the presence-aware decline CP-T06-04 supplies, not a change to the bag.
- If all twenty Cut A runs end by the same predicate, the scenario offers no real choice; say so.

## NERS reading

N: the investigation scale has no playable form and the requirements file records it out of the loop;
top-down (R-05), bottom-up (a goal, three rows, one deposit that all exist), lateral (the board shows what
clause 4 weighs; the accusation enters SC's hearing), vertical (the same rows at played, witnessed and
automatic fidelity). R: three routes to one fact and a board that shows provenance give a player something
to weigh; unattended, NPC investigators run the same loop. S: one band-keyed owner for findings, one pool
reader, one deposit rule; *pauses correctly* is first testable when Cut A exists. E, last: two harness
functions and two small edits against a scale that has never been entered by anyone.

## Cost class

§1, §3, §4: edit (harness). §2: two small edits. Lanes: FI; CHAR owns `operand_bags`; SC owns steps 6 and 7.
