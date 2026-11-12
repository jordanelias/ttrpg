# INST-BYZ-E — accession, recall and the crowd: a throne is claimed before people and may be refused; a recall may be defied; one open-floor occasion

Reconciled: 2026-11-12 by `audits/15_INSTITUTIONS_SYNTHESIS.md` §2 (X-06, X-19, X-21 to X-23) — `succeed`'s and `revoke`'s rows, bands, `provisional_term` and Failure kinds (`succession.contested`, `revocation.resisted`) are `14_VERBS_BINDING_C_turnover.md`'s; this file's "opposition" over three sets is that row's `reception` with those three audiences, each member reading `person_q.legitimacy(q, claimant, seat)` (the chain of `15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger.md`); a rival is `opposition` only when he has docketed a claim; the dignity steps are dropped; `procedure_draws` is not added. This file's Partial for `revoke` (the hold closes at the season's end and the ruled disposal with it) is the form the synthesis assumes and is listed for the BINDING lane, whose Partial drops the disposal ruled on 2026-10-21. The `acclamation` row and edits 2, 5 and 6 stand. Every finding below stands.

Re-grounded: 2026-11-12 (audit §18) — no edit of this file changes; one reading is added (who stayed away from a sitting under `acclamation`: `15_INSTITUTIONS_BYZANTINE_grounding_mechanisms.md` item 3; source `research/by_lane/SC_social_contest.md:59`, "`attend / not attend` as the lever"). The accession now has a tree source: "No formal rule existed; hereditary succession was custom, not law", the stages, and the failure mode "rival simultaneous acclamations; the acclamation often only ratified a fait accompli" (`research/social_contest_procedures/04_decision_procedure_catalog.md:71`, which also says of the Senate's part "I don't know it"). The tree's sourced blinding is Carolingian and cost its author a public penance (`research/governance/political_hierarchy_standing.md:191`); Byzantine blinding, tonsure, the hippodrome factions, 1042 and the emperor-patriarch confrontations stay memory-grade. The interface to the papacy lane is named: the Crown acts on a Church election through the Archbishop's Representative's seat, as a term in ballot odds and never an override (audit §18.4 item 10; the tree's BYZ-9 as refined, `.audit/2026-07-12-governance-compendium/tier3_proposal_status_closure.md:120`).

Reconciled: 2026-11-12, U5d closure — folded **A-19**, **A-35**, **A-36** and **A-15**. Accession to a failed royal line is the deed race (heir, consort, princess and both houses' heads; odds from what others believe of each claimant's deeds; the founding order a head start), which is this file's "opposition over three sets" read through `14_VERBS_BINDING_C`'s `succeed` row. The recall of a Cardinal by the Confessor (edit 3's draw) is un-held (A-35); no recall reaches the Confessor (A-36). Natural death (A-15) supplies the vacancies this file's accession needs.

Reconciled: 2026-11-12, wave 3 lane W3-4b — applied `R4_READ.md` §1.7 (BYZ_E: body `opposition` over three sets and `favourable` steps VIOLATE C-01; `revoke` Partial VIOLATES `04` §B.8 T-n and conflicts with BINDING-C), §2 (A-14, A-19, A-35, A-36 rows; the BIND_C `revoke` row: "BIND_C governs"), §6 (C3-N20: the "tenth row"), §7, 7b.0, 7b.7 ("Failure kinds `succession.contested`, `revocation.resisted` (BIND_C); Partial `revoke` per BIND_C (unseat without the disposal); delete `hostile`/`favourable` step lists"); `U3_CONFLICT_LEDGER.md` C3-C10, C3-N20; `U1_OWNERS_AND_VOCABULARY.md` D-U1-01 (a seat helps only as the exercised seat's `modifier:`; one above stands against as `rank_gap`), F-33 (`provisional_term` is BINDING-C's). Changed: the body now follows this file's first `Reconciled:` line, which it had not (`reception` over three audiences; a docketed rival as `opposition`; BINDING-C's kinds and term); the step lists become levels and named members; **`revoke`'s Partial takes BINDING-C's form** (the hold closes, no disposal): an actorless opening of a `ban` at a later tick has no basis (`04` §B.8 T-n: a term only closes), so the first `Reconciled:` line's "the form the synthesis assumes" is superseded by `R4_READ.md` §2; the ordinal "tenth" is gone; §2 and §6 follow A-19, A-14, A-35.

Reconciled: 2026-11-12, unification lane U4c (test 9; opened at the tree) — both `may_claim` marks are settled. `engine/season/state/gate.py:769-788` has three conjuncts and names no person: the seat's conferral basis is opened by the claim, its `successions` title is among `titles`, and no live `hold` but `besides`; the caller's `titles` is `{t.object for t in w.seat_holds(a.actor)}` (`loop/predicates.py:195`), so who may claim the crown is whoever holds a seat that is the title, which is data (A-19's set), not a branch in `may_claim`. And `may_claim` asks no ban: the ban is asked one step earlier, by `_req_succeed` (`loop/predicates.py:193`, `if restrained(w, a.actor, BAN_KIND): return False`), so §5's "a banned person's claim is refused at eligibility" holds through the precondition and no ban predicate is added to `may_claim`.

## Status: PROPOSED

**Implementation block (W3-4b; `R4_READ.md` 7b.0).** Lands in batch: **B32**, after BYZANTINE-A (`U3_DEPENDENCY_ORDER.md` §1 item 32), with `22_HAPPENINGS_B` edit 3 (the deed race's odds, A-19; §4 rows 75, 76). Depends on: `14_VERBS_BINDING_C_turnover.md` (B21: `succeed`'s and `revoke`'s rows, bands, kinds and `provisional_term`), `05_SC_arrangement_rows_that_bind.md` (B27), `15_INSTITUTIONS_BYZANTINE_A` and `_SYNTHESIS_B` (B32: `legitimacy`'s chain); CR-35, CR-37, CR-91 are v11 plan positions, MISSING until `STAGES.md` step 5 (§2's widening of `may_claim` waits on CR-35). Lane tag: FA. Tier: `opus` for edits 1 and 3's terms (contested rows whose bands decide a story); `sonnet` for edit 4. Named test: `engine/season/tests/test_inst_byz_e.py`. Standing sentences: *Pool* — `succeed`'s and `revoke`'s pools are BINDING-C's, the one pool rule on the actor's skill score (A-6); the governing attribute enters as levels (A-7); a wound is a level (A-8). *Failure writes* — `succession.contested` and `revocation.resisted` are witnessed by those present and deposited to them; the resisted recall is a deed a later `arrest` or `march` can cite (A-81). *Draw keys* — BINDING-C's: `H(w.world_seed, w.tick, <seat id>, "succeed.draw")`, `H(w.world_seed, w.tick, <holder id>, "revoke.draw")` (A-30).

Source: `audits/15_INSTITUTIONS_BYZANTINE.md` §2.8 to §2.11, §3, §7.0, §17; the standing rule of
`AUDIT_BRIEF.md` ("the ruled-in `succession` rules wherever the tree resolves an heir by a fixed
order"). Batch E. Depends on proposal A (the presumption term), on the BINDING verb lane for the row
text of `succeed` and `revoke`, and on `05_SC_arrangement_rows_that_bind.md`. Amends two planned
positions (CR-35, CR-37) by one clause each. Ratifies nothing.

## What it changes in `engine/season/` at runtime

1. `succeed` is a draw. Today an eligible claim opens the seat with certainty
   (`loop/effects_governance.py::_eff_succeed`, `:145-182`).
2. `revoke` is a draw. Today an admitted revocation closes the hold with certainty. The ruled
   disposal (an appointed seat revoked costs a ban, 2026-10-21, `gate.py::REVOCATION_DISPOSAL`) is
   kept at Overwhelming and Success; at Partial the hold closes without it (BINDING-C's Partial).
3. `arrangements.yaml` gains the row `acclamation`. Data only until a `convene` names it.
4. With the roll pinned (the control; `procedure_draws` is not added) both verbs resolve as today.

## The problem (evidence)

- `rosters.yaml: successions` is `{off_king: off_heir}`; the title's holder claims and the seat
  opens; "the first valid claim wins" (FA audit §5.2). An accession cannot be refused, cannot be
  provisional, and reads nothing about the claimant but his title. FA audit E-5, E-6:
  `succession.claimed` 0 in every run; the throne vacated at one seed of three in four seasons.
- `revoke`: formed for 5 persons, attempted 0, and "a computed `revoke` is refused at its first
  clause by construction" (FA audit §4). When FA's R-03 makes it executable, it will close the hold
  whenever the basis admits it: a governor is recalled by a sentence.
- `arrangements.yaml` header: `public debate` (`disposal: none`) is unseeded because its source wrote
  `disposes: standing`, outside the enum. No row has an open floor at settlement rank with no bench.
  So there is no occasion at which a person addresses a crowd.
- FA audit §11 item 3: seven Church and Löwenritter seats are strippable by nobody (ruled `null`).

## The resolution, decided

The Byzantine finding is that a ruler is made by recognition, the old house's presumption is an
advantage a claimant has or borrows, and the loser is made ineligible. In engine terms: the claim is
`succeed`, drawn against the regard of the people who are there; the title and the presumption are
odds; ineligibility is the existing `ban`. A recall is the same contest run downward. Ladder step 5,
under the standing rule.

## Exact edits

**1. `succeed`** (row text: BINDING lane). `contests: a standing`; no `counterparty:` (the opposition
is a set, as a bench is).

| term | reads |
|---|---|
| pool | BINDING-C's row: the one pool rule on the claimant's skill score for `succeed`'s skill (`[ASSUMPTION; medium]`: `argue`, a claim is made before people) |
| `difficulty` | by the rung kind of the seat's rung |
| `reception` (OBS member 8, hostile half) | three audiences, each member `q` reading `legitimacy(q, claimant, seat)` (SYNTHESIS-B's chain, his own ledger; the resolver sums as `world_q.reception` sums a bench): the live holders of seats on the seat's rung and the rungs directly beneath it; the persons sworn to the seat (`gate.py::sworn_to`); the persons, cohorts by weight, residing where the seat's holder last resided. An empty audience is left out |
| `opposition` (OBS member 2) | a rival who has docketed a claim on the same seat (A-19's deed race: heir, consort, princess and both houses' heads may claim); his skill score; none without a docketed rival |
| `standard` | raised one step at an open floor under `acclamation` (more eyes, and a wider telling on success) |
| levels (leverage, C3-C10) | `favour` from the favourable half of the same three audiences' `legitimacy`, and from a live occasion under `acclamation` at his place; `office` from the title seat he exercises (`Act.via` names the `successions` title; its row's `modifier:`, D-U1-01a; none ships). The dignity step is dropped (this file's first `Reconciled:` line) |

| degree | writes | emits |
|---|---|---|
| Overwhelming | the hold opens; the title closes | `succession.claimed`, `tenure.closed` |
| Success | the same | the same |
| Partial | the hold opens with `Term(tick + provisional_term · season)` (BINDING-C's one fixture, shipped 2); the title stays | `succession.claimed` |
| Failure | nothing; the title stays; the seat stays vacant | `succession.contested` (BINDING-C's name) |

A provisional holder may `succeed` again while his term runs; a Success or better removes the term
and closes the title. Every band is recoverable.

**2. Who may claim (a clause for CR-35, not built here).** Eligibility stays the gate's
(`gate.py::may_claim`). CR-35 schedules the contested arm; this file asks that it widen `may_claim`
to any person who holds a claim on the seat (CR-91's grounds) and not only the title's holder, so
that the title is a large term in the odds and not the gate. For the crown A-19 rules the set: when the
line fails, heir, consort, princess and both houses' heads may claim, the founding order a head start
(SYNTHESIS-B's ledger), which `22_HAPPENINGS_B` edit 3 carries. `offices.yaml:193`'s own mark on
`off_king.conferral: inheritance` is `[ASSUMPTION; medium; Jordan to correct]`; RS-27 rules that the
heir "still has to claim", and is silent on who else may. `[UNVERIFIED]` `may_claim`'s body
(`gate.py:770-786`, not opened).

**3. `revoke`** (row text: BINDING lane; with FA's R-03). `contests: a standing`; `counterparty: to`
(the holder).

| term | reads |
|---|---|
| pool | BINDING-C's row: the one pool rule on the revoker's skill score (`[ASSUMPTION; medium]`: `argue`) |
| `difficulty` | by the rung kind of the stripped seat's rung |
| `reception` (hostile half) | one audience: the persons sworn to **his** seat (`establishment_of`), each reading his regard for the holder: a governor's own men |
| `rank_gap` (OBS member 6) | where a seat the holder holds stands above the revoker's exercised seat; the dignity-grade step is dropped (D-U1-01) |
| levels (leverage, C3-C10) | `proofs` for a deed claim the revoker holds against the holder from the window (a writ returned at his hand, a `compliance.withheld`, FA's suspicion fold). The step for "a person sworn to the revoker's seat is present where the holder is" has no OBS §3 source and is dropped; listed for U1 with the other unplaced members (`R4_READ.md` 7b.8) |

| degree | writes | emits |
|---|---|---|
| Overwhelming, Success | the hold closes now; the ruled disposal opens | `tenure.closed` |
| Partial | the hold closes now; no disposal (BINDING-C's Partial: unseated without the ban) | `tenure.closed` |
| Failure | nothing closes; the effect emits `revocation.resisted` (BINDING-C's name), WITNESS deposits it to the revoker and those present | `revocation.resisted` |

No recall reaches `off_confessor` (A-36: `revocation: null`).

`revocation.resisted` is the ground a later `arrest` or `march` can cite. It is not a dominance kind.
(`recall.defied` is not added: F-R4-11.)

**4. `arrangements.yaml`** — appended last:

```yaml
  # ── acclamation — a person before a crowd; nobody decides, and everybody was there ────────────
  # INST-BYZ-E. The one row with an open floor, no bench and no disposal: what it produces is what
  # those present heard. `interposed: [ceremony]` (`interposition_kinds` has the member; no row used
  # it but `excommunication_deliberation`). [ASSUMPTION; medium; Jordan to correct; revert: delete
  # the row -- a data edit, no code reads a row by name.]
  - id:               acclamation
    disposal:          none
    bench_basis:        none
    floor:              open
    records_dissent:    false
    venue_min_rank:     settlement
    term_required:      false
    appeal_basis:       none
    interposed:         [ceremony]
    order:              rank
    proofs:             [testimony]
    disposes:           none
    disposal_reach:      settlement
```

The loader accepts `disposal: none` and `disposes: none` (`data/arrangements.py:64`, `:68`).
`[UNVERIFIED]` whether it requires `bench_basis: none` to pair with `disposal: none` as it pairs
`quorum` with `declared`. What a `speak` at this occasion does to those present (the speaker's cited
deeds reaching their ledgers as told claims, by `speak`'s degree) is the social verb family's and
SC's to write; this file asks for it and reads one fact, "a live occasion under `acclamation` at the
claimant's place", in edit 1.

**5. Disqualification: nothing.** A bench's `determine` under `tribunal` or `inquisition_hearing`
disposes a `ban`; a ban bars openings (H-294; FA audit R-06 scopes it to the banning seat's purview),
and `succeed` opens a hold, so a banned person's claim is refused at eligibility while the ban lives;
`pardon` ends it. That is the function blinding and the tonsure served. `[UNVERIFIED]` that
`may_claim` asks the ban; if it does not, it asks `gate.py`'s existing ban predicate.

**6. Interface for the papacy lane (not built here).** *Short list, then appointment:* a seat filled
by a body's vote from which a second seat confers is one existing shape used twice: a `declared`
disposal (each member's ballot a draw inside the presiding act, A-14; quorum as on
`excommunication_deliberation`) that makes eligible the persons it carries, then a drawn `confer` by the
appointing seat among them. *Consecration:* a held certificate cited by the claimant is a `proofs`
level in edit 1 (PAPACY-C as reconciled). FA audit §11 item 3 is ruled (A-35, `head_of_faction`): the
recall of a Cardinal by the Confessor is edit 3's draw; nobody recalls the Confessor (A-36).

## Gate (execution artifacts)

1. *Accession.* 400 seeds, a hand-vacated throne, the title-holder claiming: all four bands occur;
   the Success-or-better rate with the title exceeds the rate for the same person with the title
   stripped (the title is odds); with `presumption_gain` raised from its shipped 0 to 0.5 both rates
   rise (the house's standing is odds). With the roll pinned to Success every seed opens the hold.
2. *Recall.* 400 seeds, a hand-placed `revoke` of a governor with three men sworn to his seat, in two
   arms (their regard for him high, low): `revocation.resisted` occurs in both and is more frequent in
   the first; no Partial seed opens a `ban` at any tick.
3. *In play.* FA's `succession` situation (`06_FA_playable_scenario.md`) under the auto chooser,
   seeds 0 to 19: the distribution of bands, of provisional holds confirmed, and of seasons the seat
   stood vacant.

## Falsifier

Seat a title-holder whom every person present regards at the minimum, and a rival-free field: if he
is seated in every seed, the `reception` term is not read. A Partial `revoke` that opens a `ban` at any
later tick (an actorless opening): the edit is wrong.

## NERS

N: without the draw a throne passes by a table lookup and a governor falls by a sentence; no
contested accession, no defiant governor, no provisional reign can occur. Holds top-down (recall),
bottom-up (a crowd's regard is a third of the opposition), laterally (rival claimants). The
`acclamation` row holds top-down only until `speak` writes at it: **narrowed**. R: when to claim,
where (at an open floor or not), and whom to recall first are choices with different odds; the
no-player half is the contested accession. Completeness: a seat nobody is eligible for stays vacant
and the season runs. S: the contest seam, the obstacle form, `legitimacy`, the gate's bases and the
ruled disposal are unchanged owners. E, against that: two rows' terms, one arrangement row, no new
kind and no fixture of its own (`provisional_term` is BINDING-C's).

## Cost class

Small build. Movers: any run in which a `succeed` or a `revoke` resolves. The arrangement row moves
nothing until a `convene` names it.
