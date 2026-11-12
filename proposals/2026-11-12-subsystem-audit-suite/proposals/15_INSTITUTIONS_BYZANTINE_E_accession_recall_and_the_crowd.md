# INST-BYZ-E — accession, recall and the crowd: a throne is claimed before people and may be refused; a recall may be defied; one open-floor occasion

## Status: PROPOSED

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
   kept in every band in which the hold closes.
3. `arrangements.yaml` gains a tenth row, `acclamation`. Data only until a `convene` names it.
4. With `procedure_draws: off` (the control arm) both verbs resolve as today.

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
| pool | `faculty(w, p, "succeed")`; `verb_capability.succeed` → `argue` `[ASSUMPTION; medium]` (a claim is made before people) |
| `difficulty` | by the rung kind of the seat's rung |
| `opposition` | minus the mean, over three sets, of each set's mean `legitimacy(q, claimant, seat)` (proposal A's function, each `q` reading his own ledger; the resolver sums as `world_q.reception` sums a bench): the live holders of seats on the seat's rung and the rungs directly beneath it; the persons sworn to the seat (`gate.py::sworn_to`); the persons, cohorts by weight, residing where the seat's holder last resided. An empty set is left out of the mean |
| `hostile` | one step per other person eligible to claim the same seat who is alive |
| `favourable` | one step each: the claimant holds the seat's `successions` title; he holds a dignity; a live occasion under `acclamation` stands at his place |
| `standard` | raised one step at that open floor (more eyes, and a wider telling on success) |

| degree | writes | emits |
|---|---|---|
| Overwhelming | the hold opens; the title closes | `succession.claimed`, `tenure.closed` |
| Success | the same | the same |
| Partial | the hold opens with `Term(tick + provisional_term · season)`; the title stays | `succession.claimed` |
| Failure | nothing; the title stays; the seat stays vacant | `succession.unrecognised` |

A provisional holder may `succeed` again while his term runs; a Success or better removes the term
and closes the title. Every band is recoverable.

**2. Who may claim (a clause for CR-35, not built here).** Eligibility stays the gate's
(`gate.py::may_claim`). CR-35 schedules the contested arm; this file asks that it widen `may_claim`
to any person who holds a claim on the seat (CR-91's grounds) and not only the title's holder, so
that the title is the largest term in the odds and not the gate. `offices.yaml:193`'s own mark on
`off_king.conferral: inheritance` is `[ASSUMPTION; medium; Jordan to correct]`; RS-27 rules that the
heir "still has to claim", and is silent on who else may. `[UNVERIFIED]` `may_claim`'s body
(`gate.py:770-786`, not opened).

**3. `revoke`** (row text: BINDING lane; with FA's R-03). `contests: a standing`; `counterparty: to`
(the holder).

| term | reads |
|---|---|
| pool | `faculty(w, p, "revoke")` → `argue` `[ASSUMPTION; medium]` |
| `difficulty` | by the rung kind of the stripped seat's rung |
| `opposition` | the mean regard for the holder among the persons sworn to **his** seat (`establishment_of`): a governor's own men |
| `favourable` | one step each: the revoker holds a deed claim against the holder from the window (a writ returned at his hand, a `compliance.withheld`, FA's suspicion fold); a person sworn to the revoker's seat is present where the holder is |
| `hostile` | one step if the holder also holds a dignity of grade 4 or above (the disgraced man still outranks his judges) |

| degree | writes | emits |
|---|---|---|
| Overwhelming, Success | the hold closes now; the ruled disposal opens | `tenure.closed` |
| Partial | the hold closes at the season's end (`Tenure.until` set ahead); the ruled disposal opens then | `tenure.closed` at that tick |
| Failure | nothing closes; the revoker holds a firsthand deed claim `(holder, recall.defied, True)` | `recall.defied` |

`recall.defied` is a new deed kind; it is the ground a later `arrest` or `march` can cite. It is not
a dominance kind.

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
disposal (the body's members `commit` to candidates, quorum as on `excommunication_deliberation`)
that makes eligible the persons committed to, then a drawn `confer` by the appointing seat among
them. *Consecration:* a named `favourable` term in edit 1, for the papacy lane to define and own. This
file defines neither, and takes no position on FA audit §11 item 3; under option (B) there
(`head_of_faction`), the recall of a Cardinal by the Confessor is edit 3's draw.

## Gate (execution artifacts)

1. *Accession.* 400 seeds, a hand-vacated throne, the title-holder claiming: all four bands occur;
   the Success-or-better rate with the title exceeds the rate for the same person with the title
   stripped (the title is odds); with `presumption_gain: 0` both rates fall (the house's standing is
   odds). With `procedure_draws: off` every seed opens the hold.
2. *Recall.* 400 seeds, a hand-placed `revoke` of a governor with three men sworn to his seat, in two
   arms (their regard for him high, low): `recall.defied` occurs in both and is more frequent in the
   first.
3. *In play.* FA's `succession` situation (`06_FA_playable_scenario.md`) under the auto chooser,
   seeds 0 to 19: the distribution of bands, of provisional holds confirmed, and of seasons the seat
   stood vacant.

## Falsifier

Seat a title-holder whom every person present regards at the minimum, and a rival-free field: if he
is seated in every seed, the opposition term is not read. Remove the ruled disposal from the Partial
band: a planted assertion that a closed appointed hold always carries a ban fails, which shows the
ruling is kept only by the edit as written.

## NERS

N: without the draw a throne passes by a table lookup and a governor falls by a sentence; no
contested accession, no defiant governor, no provisional reign can occur. Holds top-down (recall),
bottom-up (a crowd's regard is a third of the opposition), laterally (rival claimants). The
`acclamation` row holds top-down only until `speak` writes at it: **narrowed**. R: when to claim,
where (at an open floor or not), and whom to recall first are choices with different odds; the
no-player half is the contested accession. Completeness: a seat nobody is eligible for stays vacant
and the season runs. S: the contest seam, the obstacle form, `legitimacy`, the gate's bases and the
ruled disposal are unchanged owners. E, against that: two rows' bands, one arrangement row, two
emitted kinds, one fixture (`provisional_term`, shared with proposal A).

## Cost class

Small build. Movers: any run in which a `succeed` or a `revoke` resolves. The arrangement row moves
nothing until a `convene` names it.
