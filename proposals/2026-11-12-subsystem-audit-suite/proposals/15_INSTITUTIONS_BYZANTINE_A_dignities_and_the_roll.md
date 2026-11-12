# INST-BYZ-A — dignities and the Roll: the founding order where persons can read it, and an honour that cites a deed

Reconciled: 2026-11-12 by `audits/15_INSTITUTIONS_SYNTHESIS.md` §2 (X-01, X-03 to X-08, X-19, X-21 to X-23) — the founding order is carried once, as three founders' seeded deeds (3, 2, 1) in a prehistory block, not as `offices.yaml: founding:` with `order` and `founding_confidence` (edits 1, 4's second fixture and 5 are withdrawn); no Record kind `roll` is added (edit 2 withdrawn): a certificate is any Record carrying `recites`, and what this file calls the Roll is the Settlement, two seeded `homage` instruments in the Chief Parliamentary Clerk's keeping (`instruments.yaml: seeded`); the presumption is the chain term of `person_q.legitimacy` in `15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger.md`, discounted per holder and read from the predecessors' deeds, not from claims whose subject is a seat (edit 6 is replaced), and `presumption_gain` ships 0; `confer`'s row, bands and Failure kind (`appointment.resisted`) are `14_VERBS_BINDING_C_turnover.md`'s, as is `provisional_term`; the "favourable" steps are the named terms `evidence`, `regard` and `reception`, and the dignity step is dropped; `procedure_draws` is not added (a contest row's control is the pinned roll). Edits 3 and 7's two conjuncts on a dignity row, the telling of the cited deed, and `dignity_grades` stand. Every finding below stands.

Re-grounded: 2026-11-12 (audit §18) — no edit of this file changes. Its history now has tree sources: the two tenures (`.audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md:27`), with the correction that BYZ-1 was regraded from KEEP to DISTILL (`.audit/2026-07-12-governance-compendium/tier3_proposal_status_closure.md:115`: keep "the decoupled-prestige kernel" only), which this file's remit-less seat row already is; a shipped precedent for rank by deed and a stipend by title (`research/game_precedent_suite/tutorials/T13_koei.md:29`, `:78`); and a caution for later batches: the tree grades the "holder is not controller" convergence over-claimed and records a reverted build (`research/by_lane/IN_infrastructure.md:142`), so a dignity stays a `hold` on a seat row and never a control relation. The grades and counts of the historical order stay memory-grade (§18.5).

Reconciled: 2026-11-12, U5d closure — folded **A-12** and **A-17 / A-18**. A dignity's "precedence" step, withdrawn by X-19 because a seat could add no modifier, is lawful again as a seat's modifier (A-12); it is not re-added here and may return as a named term through the one obstacle composer. The founders' seeded deeds follow the ruled order (Varfell third, realm-wide at the third confidence).

Reconciled: 2026-11-12, wave 3 lane W3-4b — applied `R4_READ.md` §1.7 (BYZ_A: e3 CONFORMS once A-12/A-13 land; e7's deposit AMBIGUOUS; "withdrawn edits 1, 2, 4 (second fixture), 5, 6 still in the body"), §2 (A-12 row; F-R4-10, F-R4-11), §7, 7b.0, 7b.7 ("delete the withdrawn edits …; e7's deposit wording …; `presumption_gain` is SYN_B's (ships 0)"); `U1_OWNERS_AND_VOCABULARY.md` D-U1-01/01a (a dignity's precedence returns only as the seat row's `modifier:`), F-33 (`provisional_term` is BINDING-C's one fixture), F-34; `U3_CONFLICT_LEDGER.md` C3-C10 (favourable terms are levels), F-R4-11 (BINDING-C's kind names). Changed: **edits 1, 2, 4's two withdrawn fixtures, 5 and 6 are removed from the body**, each replaced by a one-line pointer to SYNTHESIS-B (they were withdrawn by this file's own first `Reconciled:` line and stood beside it); "What it changes" and gate 1 follow; edit 7's deposit is WITNESS's, its favourable steps are levels, its Partial term is BINDING-C's `provisional_term` and its Failure kind `appointment.resisted`; the `[UNVERIFIED]` on vacant rows is settled at the tree and **this file carries the vacant-row build edit** for the four files that need it (SYNTHESIS-B, COLONIAL-D, PAPACY-E); the `[UNVERIFIED]` on the row reader is settled (it refuses no unknown row key today). A-98 vocabulary lane (2026-11-12, A-98; ledger `unified/work/A98_SWEEP.md`): "trained score/rank" → skill score (1); "talent" → attribute or governing attribute (1).

## Status: PROPOSED

**Implementation block (W3-4b; `R4_READ.md` 7b.0).** Lands in batch: **B32**, after SYNTHESIS-B and `22_HAPPENINGS_B` edit 3 (`U3_DEPENDENCY_ORDER.md` §1 item 32). Depends on: `06_FA_office_capabilities.md` (B04), `06_FA_remit_grant_by_row.md` (B21), `14_VERBS_BINDING_C_turnover.md` (B21: `confer`'s row and draw, `provisional_term`), `15_INSTITUTIONS_SYNTHESIS_A`, `_B` (B32). Lane tag: FA. Tier: `sonnet` producer, effort `high`; `opus` for edit 7's obstacle and leverage terms (a contested row whose bands decide a story, `R4_READ.md` 7b.0 (1)). Named test: `engine/season/tests/test_inst_byz_a.py`. Standing sentences: *Pool* — `confer`'s pool is the one pool rule on the conferrer's skill score (A-6); the governing attribute enters as levels (A-7); a wound is a level (A-8). *Failure writes* — a Failure emits `appointment.resisted`, witnessed by those present and deposited to them; the conferee holds it as a slight (A-81). *Draw keys* — `confer`'s draw is BINDING-C's, keyed `H(w.world_seed, w.tick, <conferee id>, "confer.draw")` (A-30).

Source: `audits/15_INSTITUTIONS_BYZANTINE.md` §1.3 (D-2, D-5, D-6), §5, §6, §7.0; Jordan's fixed point
of 2026-11-12 (`INSTITUTIONS_BRIEF.md`); the standing rule of `AUDIT_BRIEF.md`. Batch A of six.
Depends on `06_FA_remit_grant_by_row.md` (remit by row), on the BINDING verb lane for `confer`'s row
text, and on `06_FA_office_capabilities.md` for the pool. Ratifies nothing.

## What it changes in `engine/season/` at runtime

1. (Withdrawn: the founding order and its paper are SYNTHESIS-B's seeded deeds and `homage`
   instruments; no Record kind `roll`.)
2. (Withdrawn: the presumption is SYNTHESIS-B's chain term in `legitimacy`; `presumption_gain` ships 0.)
3. **Seat rows may carry `dignity:`.** Six such rows are authored in the body `Imperial Court`, vacant
   at build. A `confer` on one requires the conferee's live oath to the conferring seat and a deed
   claim the conferrer holds about him; the cited deed is what the investiture publishes.
4. **`confer` is a draw** on the four-band ladder (BINDING-C's row). Its control is the pinned roll
   (`procedure_draws` is not added).
5. **A seat row may name no holder** (`holder: null`): it is built vacant. This file carries that build
   edit for the kit.

## The problem (evidence)

- `build_realm(0)` (audit E-1): 13 persons hold a stance row toward the King (sum 59.00), **none**
  toward the Duchess of Hafenmark or the Duke of Varfell; mean regard 0.720, 0.000, 0.000. The world
  holds two Records, both `works`. The founding order Jordan states is nowhere a person can read, and
  the record case NPC-008 turns on does not exist.
- `canon/03_canonical_timeline.md:78-92`: the crown and the ducal houses are deed-families; the
  presumption is inherited and rebuttable. `person_q.legitimacy` (`:537-563`) has the rebuttable half
  (a window over the holder's deeds) and no inherited half but a stance row.
- The body `Imperial Court` (`rosters.yaml: office_bodies`) has no seat.
- `confer` carries no `contests:` (audit E-2): an appointment is a fixed function of the conferral
  basis. `06_FA_office_capabilities.md` records that the conferee is positional (the lowest id the
  conferrer knows).

## The resolution, decided

The founding order is authored once, in `offices.yaml`, and reaches persons twice from that one
owner: as a document (the Roll) and as claims (what everybody was told). A dignity is a seat row
with no remit (ladder step 4: `off_heir`, `offices.yaml:252-263`, and Layer 1 §B.7's "there is no
`Title` type"). An honour publishes a deed and is paid for; it adds nothing to anyone's regard by
existing. The order decides no outcome (the standing rule): it is the confidence of a claim.

## Exact edits

**1.** (Withdrawn, X-05/X-06: no `offices.yaml: founding:` section. The order is SYNTHESIS-B §2's
seeded deeds, 3, 2, 1, in `rosters.yaml: prehistory`.)

**2.** (Withdrawn, X-04: no Record kind `roll`. What this file called the Roll is SYNTHESIS-B §3's two
`homage` instruments in the Chief Parliamentary Clerk's keeping.)

**3. `engine/season/offices.yaml: seats` — one new optional key, `dignity:`**, an int in
`[1, dignity_grades]`. A row carrying it must have `remit_acts: []` and `revocation: null` (the
loader refuses otherwise: a dignity with a remit is an office; a revocable one is not for life).
Settled at the tree (was `[UNVERIFIED]`): `data/rosters.py::_load_offices` (`:152-180`) refuses no unknown
row key today; the kit's one seat schema (SYNTHESIS-A §3) adds that refusal, and `dignity` is in it. A
dignity's precedence on a roll, if authored, is the row's `modifier:` (A-12; D-U1-01a), never a step.

Six rows, appended to `seats:` (posts are placeholders; canon names no court dignity, and research
never supplies a canon name: `rosters.yaml`'s source-precedence ruling):

```yaml
  - {id: off_dignity_1a, post: "[PLACEHOLDER] Dignity of the fifth grade",  rung: {territory: "T1"}, body: "Imperial Court", faction: null, remit_acts: [], dignity: 5, conferral: appointed, revocation: null, holder: null, obligees: [], source: "INST-BYZ-A; Jordan names", note: "[NEW]. Vacant at build."}
  - {id: off_dignity_2a, post: "[PLACEHOLDER] Dignity of the fourth grade", rung: {territory: "T1"}, body: "Imperial Court", faction: null, remit_acts: [], dignity: 4, conferral: appointed, revocation: null, holder: null, obligees: [], source: "INST-BYZ-A", note: "[NEW]."}
  - {id: off_dignity_2b, post: "[PLACEHOLDER] Dignity of the fourth grade", rung: {territory: "T1"}, body: "Imperial Court", faction: null, remit_acts: [], dignity: 4, conferral: appointed, revocation: null, holder: null, obligees: [], source: "INST-BYZ-A", note: "[NEW]."}
  - {id: off_dignity_3a, post: "[PLACEHOLDER] Dignity of the third grade",  rung: {territory: "T1"}, body: "Imperial Court", faction: null, remit_acts: [], dignity: 3, conferral: appointed, revocation: null, holder: null, obligees: [], source: "INST-BYZ-A", note: "[NEW]."}
  - {id: off_dignity_3b, post: "[PLACEHOLDER] Dignity of the third grade",  rung: {territory: "T1"}, body: "Imperial Court", faction: null, remit_acts: [], dignity: 3, conferral: appointed, revocation: null, holder: null, obligees: [], source: "INST-BYZ-A", note: "[NEW]."}
  - {id: off_dignity_4a, post: "[PLACEHOLDER] Dignity of the second grade", rung: {territory: "T1"}, body: "Imperial Court", faction: null, remit_acts: [], dignity: 2, conferral: appointed, revocation: null, holder: null, obligees: [], source: "INST-BYZ-A", note: "[NEW]."}
```

Anchored at `T1`, the capital, as the Inner Circle's appointed seats are: those are the rows a seat
on the realm rung can fill today (`offices.yaml:58-60`, H-207: "at build only the six Crown T1 seats
are satisfiable"); a dignity on the realm rung itself would sit beside the King's seat and not
beneath it. A closed number, deliberately: a place at the table is scarce, and it falls free only by
a death or a `release`.

**The vacant-row build edit (carried here for the kit; settled at the tree, was `[UNVERIFIED]`).**
`harness/populated.py`'s minted-seat loop (`:1767-1776`) slugs `row["holder"]` into a person id and raises
`Unspecified` when that person is not built, so a row with `holder: null` is refused today. Edit, in that
loop, before the person lookup: a row whose `holder` is `None` builds its `Office` from the row exactly as
a held row does and opens **no** `hold` (the seat is vacant, as a dead holder's seat is). `data/rosters.py:204`
(`OFFICES_BY_HOLDER`) skips a `None` holder. The refusal of a named holder who is not built stays.
SYNTHESIS-B §6, COLONIAL-D edit 4 and PAPACY-E's sees cite this edit. Test:
`test_inst_byz_a.py::test_a_vacant_row_builds_vacant` (red before the edit: `Unspecified` naming
`off_dignity_1a`; green after: the Office exists and no Tenure has it as object).

**4. `engine/season/data/fixtures.py`** — one fixture: `dignity_grades`, shipped 5, swept 3 / 5 / 7,
read by the `offices.yaml` loader. (Withdrawn: `presumption_gain` is SYNTHESIS-B's, shipped 0, F-34;
`founding_confidence` is not added, X-06.)

**5.** (Withdrawn: SYNTHESIS-B §2's prehistory block deposits the founding claims; no build-time Roll.)

**6.** (Replaced by SYNTHESIS-B §1: `legitimacy`'s chain term, read from the predecessors' deeds and not
from claims whose subject is a seat; `took_by_force` is applied at each link there.)

**7. `confer` on a dignity row** (`loop/predicates.py::_req_confer`; `loop/effects_governance.py::_eff_confer`;
the row's text is the BINDING lane's):

- two more conjuncts, asked only where the object row carries `dignity`: the conferee holds a live
  `oblige` to the exercised seat (`gate.py::sworn_to`: homage before investiture, and the oath is the
  swearer's own act, AX-1); and the payload's `cites` names a deed claim about the conferee in the
  conferrer's own ledger (`own_ledger` of `to`, the form `survey` and `tell` use). A computed act
  binds `to` from the persons the conferrer holds deed claims about and ranks them by his own
  `deeds_judged`, which replaces the positional conferee for these rows.
- the draw is `14_VERBS_BINDING_C_turnover.md`'s row (its `contests:`, pool and bands; X-23). This file
  supplies, for a dignity row only, the terms in the SC form (C3-C10: what helps is levels): obstacle
  `difficulty` by the rung kind of the seat's rung and the `reception` of the live holders of seats of
  the row's body toward the conferee (hostile half; an empty body: none), `standard` raised at an open
  floor; the conferrer's levels: `proofs` for a `cites` claim held firsthand, `favour` for the
  conferee's regard for the conferrer above zero. The conferee's own highest live dignity is **not** a
  level here: a seat helps a roll only as the actor's exercised seat's `modifier:` (D-U1-01), and the
  conferee is not the actor.
- by degree: Overwhelming and Success open the `hold`, and the effect emits the investiture Event
  carrying the cited deed as an Observation; **WITNESS deposits the told claim** through its `told_by`
  channel to every person the kind's reach admits (`04` §A.2: `loop/witness` is the only writer of
  claims; full confidence on Overwhelming, the conferrer's own on Success); Partial opens it with
  `Term(tick + provisional_term·season)` (BINDING-C's one fixture, shipped 2, swept 1 / 2 / 4; F-R4-10);
  Failure opens nothing, emits `appointment.resisted` (BINDING-C's name; F-R4-11), and closes nothing.

No new emitted kind (`conferral.declined` is not added).

## Gate (execution artifacts)

1. *Build.* The six dignity rows build vacant (the vacant-row test above); the founding order's
   reading is SYNTHESIS-B's gate 2, reported per regime (A-87 to A-91), not repeated here.
2. *Draw.* 200 seeds, one hand-placed `confer` of `off_dignity_3a` by the King on a sworn person with
   one firsthand deed: all four bands occur; no band exceeds 0.9; with the roll pinned to Success every
   seed opens the hold (the control).
3. *Reach.* Realm, seeds 0 to 9, eight seasons: the count of `tenure.opened` on dignity rows and of
   `appointment.resisted` on them, reported, with the cited deed among the conferee's told claims in at least
   one other person's ledger after an opening. A zero count is a finding against reach (F-FA-02's
   cause b, the question slot), not against this mechanism, and is reported as such.

## Falsifier

Delete the `cites` conjunct: a seeded conferral names a person the conferrer holds no deed of. Write the
cited deed's claim from the effect instead of WITNESS: a person outside the kind's reach holds it.
Delete the vacant-row edit: the build raises. If any plant leaves its reading unmoved, the rule is not
read. (The founding order's falsifiers are SYNTHESIS-B's.)

## NERS

N: cut `dignity` and the Imperial Court stays seatless (the Roll and the founding claims are now
SYNTHESIS-B's and carry NPC-008's custody). Holds top-down, bottom-up (a petitioner consults
the Roll), laterally (two houses compared by one formula). R: the conferrer chooses whom to honour and
is bound to pay (B); complete at the extremes (no deed known: no candidate forms; a seat taken by
force reads no presumption). S: `deed_term` and `reception`'s confidence weighting; no new scoring.
E, against that: one key, one fixture, six content rows, one build edit.

## Cost class

Small build. Declared movers: the build hash (six vacant seats); any run in which a `confer` on a
dignity resolves.
