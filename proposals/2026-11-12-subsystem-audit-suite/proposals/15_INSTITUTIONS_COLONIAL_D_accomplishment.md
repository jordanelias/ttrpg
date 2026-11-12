# COLONIAL-D — rank as a ledger of accomplishment: the Secession War as three seeded deeds, presumption that passes down the seat, homage as an instrument, and conquest as the way an `annex` seat is filled

Reconciled: 2026-11-12 by `audits/15_INSTITUTIONS_SYNTHESIS.md` §2 (X-03, X-05, X-06, X-07, X-08) — this file's design (three founders as persons, their deeds as Events, standing down the seat at `presumption_gain` per holder) is the kit's and is carried by `15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger.md`, with three changes: no second function `person_q.accomplishment` is added, the recursion is one term of the existing `person_q.legitimacy` (edit 1 replaced), cut at a holder believed to have taken the seat by force; the two `homage` instruments are rows of `instruments.yaml: seeded`, recite their founders' deeds and are kept by the Chief Parliamentary Clerk, so `obligees:` keeps bare ids and edit 3's mapping form is not added; `recognition` is not a form (a certificate is the `recites` key). `presumption_gain` ships 0 with sweep {0, 0.5, 0.75, 1.0}. Edits 2, 4 and 5 stand. Every finding below stands.

Re-grounded: 2026-11-12 against the tree's research (`unified/RESEARCH_MAP_INSTITUTIONS_B.md`; audit §16). No edit of this file's is changed. What changed: edit 3's `homage` rested on the audit's memory of the fief; the tree holds a worked vassal contract and it has a clause the audit lacked: the lord's favour is either **confirmation of what the vassal holds** or **a new grant**, owed for service, and a won war that takes nothing leaves the lord unable to pay it (`research/governance/political_hierarchy_standing.md:457-461`). For a house founded by ranked accomplishment in war that is the nearer half of the bargain: accomplishment is owed something. It is added to the `homage` form as a second grantor `due`, by `15_INSTITUTIONS_COLONIAL_grounding_F_what_the_tree_adds.md` edit 2, and gives this file's three seeded oaths one more content cell each (the reward's amount, an assumption for Jordan). Also sourced: confirmation at each succession for a fee (`research/fa_se_historical_precedent_research_v1.md:138`); the heritable office conceded at Quierzy (`research/governance/governance_modes.md:154`); an elective crown one house wins repeatedly (`:188`), which this file's reading of Varfell already used.

Reconciled: 2026-11-12, U5d closure — folded **A-17 / A-18**, **A-19** and the land rulings. The part held back in the Status line (the counts in edit 2 depend on the audit's §11 item 1) is released on option A: the south fought, ranked third, and its founding deed is held realm-wide at the third confidence; the counts stay `[ASSUMPTION; Jordan to correct]`, only the order is ruled. Edit 5 (`FILLED_BY["annex"]` gains a taking basis) is rewritten: a won march's arrival fills nothing by itself, because a victor chooses to seize, occupy or withdraw (A-66); when he seizes a place its seats pass to him in the seizure's own write (A-58; `U5d_FA_land_and_seats_pass_on_a_won_march.md` edit 2), so the `annex` taking basis is needed only as that proposal's named revert (seats close and stand vacant for the seizer's conferral) and is not built otherwise; `place.surrendered` under a `capitulation` carries the seats the same way. An empty throne is claimed in the deed race (A-19), which reads this file's accomplishment ledger.

Reconciled: 2026-11-12, wave 3 lane W3-4b — applied `R4_READ.md` §1.7 (COL_D: `accomplishment` stale, replaced by SYNTHESIS-B's chain; e5 not built, A-66, A-58), §2 (A-17/A-18; the per-regime gate row), §7 (INCOMPLETE: edit 1 replaced; test file stale), 7b.0, 7b.7; `U3_DEPENDENCY_ORDER.md` §4 row 86 (the split: the ledger reading in B33, the founders' prehistory in B39), §6 (`test_accomplishment.py` MISSING and its function gone); `U3_CONFLICT_LEDGER.md` C3-L12 (title moves only by the act the victor forms). Changed: the Status line follows A-17 (the held-back part is released on option A; the counts stay `[ASSUMPTION]`); **edits 1, 2, 3 and 5 are removed from the body** and replaced by pointers (1, 2, 3 are SYNTHESIS-B's, as this file's first `Reconciled:` line says; 5 is not built, as its U5d line says), so no second statement stands beside the rule; edit 4's vacant title cites BYZANTINE-A's vacant-row edit; the test is `test_inst_col_d_ledger.py`.

## Status: PROPOSED (the part once held back is released by A-17/A-18; the seeded counts stay `[ASSUMPTION; Jordan to correct]`, only the order is ruled)

**Implementation block (W3-4b; `R4_READ.md` 7b.0).** Lands in two batches (`U3_DEPENDENCY_ORDER.md` §4 row 86): **B33**, after COLONIAL-C, edit 4 and the gate's chain reading; **B39**, the founders' prehistory reading with `12_ARCS_case_on_the_realm.md` (SYNTHESIS-B §2 lands there). Depends on: `15_INSTITUTIONS_SYNTHESIS_B` (B32/B39), `15_INSTITUTIONS_COLONIAL_A` (B32), `15_INSTITUTIONS_BYZANTINE_A` (B32, the vacant-row edit), `12_ARCS_case_on_the_realm.md` (B39). Lane tag: FA. Tier: `sonnet`, effort `medium` (edit 4) and `high` (the test); one `opus` read of the per-regime ordering. Named test: `engine/season/tests/test_inst_col_d_ledger.py` (replaces `test_accomplishment.py`, whose function is not added). Standing sentences: *Pool*, *Failure writes*, *Draw keys* — no roll, contested row or draw is added (A-6 to A-8, A-81, A-30).

Source: Jordan, 2026-11-12, as `INSTITUTIONS_BRIEF.md` records it: *"current kingdom royalty is because
of nobility by deed/achievement"*; *"Royalty by noble conquest, i.e. the first king had the greatest
accomplishment in the secession war, followed by the first Duke of Hafenmark and the first Duke of
Varfell."* Audit §5, §12 batch C-4. Cross-lane: the crown lane owns succession and recognition; FA owns
`offices.yaml`'s seat rows and `state/gate.py::FILLED_BY`; ARCS owns the prehistory route
(`12_ARCS_case_on_the_realm.md`); CHAR owns `deeds_judged`'s weights. This file states what the colonial
family needs of each and authors only the parts no lane owns. Nothing is ratified by being written.

## What it changes in `engine/season/` at runtime

1. (SYNTHESIS-B §1.) A person's estimate of another's standing includes a discounted share of the deeds
   of those who held the same seat before him, **as the estimating person's own ledger holds them**: the
   chain term of `person_q.legitimacy`.
2. (SYNTHESIS-B §2.) A built realm holds three dead founders and their Secession deeds as `ROOT`-caused
   build-time Events whose product is the cast's told claims (A-51). Declared hash mover.
3. (SYNTHESIS-B §3.) Two of the three built vassal oaths are held under seeded `homage` instruments; the
   Grand Master's has none.
4. `off_duchess_hafenmark` is filled by inheritance through a title nobody holds at build.
5. (Not built.) A won march fills no seat by itself (A-66); a seizure carries the seats in its own write
   (A-58).

## The problem (evidence)

- `canon/03_canonical_timeline.md:80-92`: deed-monarchy, deed-families, a rebuttable presumption the
  heir inherits and must prove. `engine/season/` carries none of it: no founder is a person, no
  Secession deed is an Event or a claim, and no fact orders the three houses (audit §5.2 row 5; probe
  E-1: 83 persons, 70 Propositions, none of the war).
- `queries/person_q.py::deeds_judged(p, referent)` (`:97`) values a referent by **his own** deeds in
  `p`'s ledger. Almud, who "has not personally earned the deed-claim" (canon :117), therefore reads as
  a man of no accomplishment to everyone, and so does every heir after any succession.
- `rosters.yaml: conferral_bases` note: "which act fills an `elected` or an `annex` seat is not ruled".
- `offices.yaml:213-224`: `off_duchess_hafenmark.conferral: null`; `:226-237`: `off_duke_varfell`
  `elected` (reconciled with Jordan's statement by reading, audit §5.2 row 3: founded by conquest,
  filled by election; no edit).
- The three oaths are termless edges with no content (`offices.yaml:132-133`, `:196`).

## The resolution, decided

**Standing passes down the seat, not the blood** (ladder step 3: canon :92 and :145, "loyal to Crown as
institution, not bloodline"; step 4: `successions` already passes a seat by title, not kinship). **No
world-level rank exists**: every reading is one person's, from his own ledger (Layer 1's person-side
rule), so two persons rank the houses differently and a house's standing is contested by telling.
**Nothing here decides who rules.** The ledger sets odds and occasions; a seat changes hands only by a
rolled hearing, a rolled field, or persons releasing and swearing oaths.

## Exact edits, by owner

**1.** (Replaced by SYNTHESIS-B §1: no `person_q.accomplishment`; the recursion is one term of the
existing `person_q.legitimacy(p, holder, window, seat, fx)`, cut at a holder `p` believes took the seat
by force; `presumption_gain` ships 0, sweep {0, 0.5, 0.75, 1.0}. Its readers (`standing_crossed`;
`reception` where the subject of the act is a seat) call `legitimacy` with the seat.)

**2.** (Replaced by SYNTHESIS-B §2, B39: three founders, deeds 3, 2, 1, `ROOT`-caused build-time Events
whose only product is told claims, A-51. A-17/A-18 decided the south's part: Varfell's deed is held
realm-wide at the third confidence; the earlier "option B, zero in northern ledgers" is superseded.)

**3.** (Replaced by SYNTHESIS-B §3: the two `homage` instruments are `seeded:` rows reciting their
founders' deeds, kept by the Chief Parliamentary Clerk; `obligees:` keeps bare ids and the mapping form
is not added.)

**4. `offices.yaml: off_duchess_hafenmark.conferral: null → inheritance`; `rosters.yaml: successions`
gains `off_duchess_hafenmark: off_heir_hafenmark`; `offices.yaml` gains the title seat
`off_heir_hafenmark` (`post: "Heir of Hafenmark"`, `rung: {duchy: "Hafenmark"}`, `conferral: appointed`,
`remit_acts: []`, `holder: null`).** `[ASSUMPTION; medium; Jordan to correct; revert: the three edits
together]`. Ladder step 4: `off_king`'s shape (IN-61). Canon gives Baralta no heir (:143), so the title
is vacant at build and **Hafenmark's succession is open from the first season**: whom she designates,
and whether a deed-claimant petitions instead, is play. Settled at the tree (was `[UNVERIFIED]`): the
build refuses a row with `holder: null` today (`harness/populated.py:1771-1776`); BYZANTINE-A's vacant-row
edit (B32) admits it.

**5.** (Not built; this file's U5d line.) A won march's arrival fills nothing by itself: the victor
chooses to seize, occupy or withdraw (A-66), and title moves only by the act he forms (`seize`; C3-L12);
when he seizes, the place's seats pass in the seizure's own write (A-58;
`U5d_FA_land_and_seats_pass_on_a_won_march.md` edit 2). `FILLED_BY["annex"]`'s taking basis exists only
as that proposal's named revert (seats close and stand vacant for the seizer's conferral).
`place.surrendered` under a `capitulation` carries the seats the same way.

## Gate (execution artifact)

- `engine/season/tests/test_inst_col_d_ledger.py` (B33): on a hand-built world, through
  `legitimacy(p, holder, window, seat, fx)` at `presumption_gain` 0.5: an heir whose predecessor `p` knows
  of reads own + 0.5 × predecessor's; an heir whose predecessor `p` has never heard of reads own;
  `presumption_gain: 0` reads own for both; a three-holder chain reads 0.25 of the founder. The vacant
  title `off_heir_hafenmark` builds (BYZANTINE-A's edit).
- Realm (B39, after SYNTHESIS-B §2): SYNTHESIS-B's gate 2 (per cast person, the ordering of the three
  seat-holders; a majority king, Hafenmark, Varfell and at least one person not; reported per regime,
  A-87 to A-91). Not repeated here.
- After two seasons at seeds 0–2: the orderings are printed again; the count of persons whose ordering
  changed is reported (not asserted: it is zero today if no deed is done, and that is a finding about
  the realm, not this edit).

## Falsifier

- Planted: reverse two seeded counts; the majority ordering reverses.
- Planted: read the predecessor from the world's Tenures instead of `p`'s claims; the "never heard of"
  assertion reddens.
- Control: `presumption_gain: 0` and no seeded founders reproduce the base hash.

## What it does not do

No legitimacy scalar, no Mandate, no Coup Counter (struck; ARCS §6 row 7). No blood claim: kinship
enters only through an heir title. No rule that the highest accomplishment rules. No certification
mechanism beyond naming it (`recognition` is the crown and Church lanes' instrument row; audit §5.3 (c)).

## NERS reading

- **N.** Above: a king's authority rests on what people believe his house did. Below: a villager who has
  heard only of the duke's founder rates the duke above the king. Lateral: Baralta's claim is legible as
  a number-two deed against a number-one heir. Diagonal: a southerner's ledger and a northerner's
  disagree about Varfell. Remove it and every heir is a nobody and deed-monarchy is flavour.
- **R.** A player's deed can out-rank a dynasty in some ledgers; the world tells and forgets founders by
  itself; complete at the extremes (unknown predecessor: own deeds only; no deeds: zero).
- **S.** One fold on the one deed reader; the same unit; no second standing ladder.
- **E, last.** Three content cells and one gate entry here; the function, fixture and seeded persons are
  SYNTHESIS-B's.

## Cost class

Edit (edit 4, content in FA's files) and the test; the fold and the seeding are SYNTHESIS-B's.
