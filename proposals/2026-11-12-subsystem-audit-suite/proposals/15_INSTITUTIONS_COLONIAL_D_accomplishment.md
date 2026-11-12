# COLONIAL-D — rank as a ledger of accomplishment: the Secession War as three seeded deeds, presumption that passes down the seat, homage as an instrument, and conquest as the way an `annex` seat is filled

Reconciled: 2026-11-12 by `audits/15_INSTITUTIONS_SYNTHESIS.md` §2 (X-03, X-05, X-06, X-07, X-08) — this file's design (three founders as persons, their deeds as Events, standing down the seat at `presumption_gain` per holder) is the kit's and is carried by `15_INSTITUTIONS_SYNTHESIS_B_the_deed_ledger.md`, with three changes: no second function `person_q.accomplishment` is added, the recursion is one term of the existing `person_q.legitimacy` (edit 1 replaced), cut at a holder believed to have taken the seat by force; the two `homage` instruments are rows of `instruments.yaml: seeded`, recite their founders' deeds and are kept by the Chief Parliamentary Clerk, so `obligees:` keeps bare ids and edit 3's mapping form is not added; `recognition` is not a form (a certificate is the `recites` key). `presumption_gain` ships 0 with sweep {0, 0.5, 0.75, 1.0}. Edits 2, 4 and 5 stand. Every finding below stands.

Re-grounded: 2026-11-12 against the tree's research (`unified/RESEARCH_MAP_INSTITUTIONS_B.md`; audit §16). No edit of this file's is changed. What changed: edit 3's `homage` rested on the audit's memory of the fief; the tree holds a worked vassal contract and it has a clause the audit lacked: the lord's favour is either **confirmation of what the vassal holds** or **a new grant**, owed for service, and a won war that takes nothing leaves the lord unable to pay it (`research/governance/political_hierarchy_standing.md:457-461`). For a house founded by ranked accomplishment in war that is the nearer half of the bargain: accomplishment is owed something. It is added to the `homage` form as a second grantor `due`, by `15_INSTITUTIONS_COLONIAL_grounding_F_what_the_tree_adds.md` edit 2, and gives this file's three seeded oaths one more content cell each (the reward's amount, an assumption for Jordan). Also sourced: confirmation at each succession for a fee (`research/fa_se_historical_precedent_research_v1.md:138`); the heritable office conceded at Quierzy (`research/governance/governance_modes.md:154`); an elective crown one house wins repeatedly (`:188`), which this file's reading of Varfell already used.

Reconciled: 2026-11-12, U5d closure — folded **A-17 / A-18**, **A-19** and the land rulings. The part held back in the Status line (the counts in edit 2 depend on the audit's §11 item 1) is released on option A: the south fought, ranked third, and its founding deed is held realm-wide at the third confidence; the counts stay `[ASSUMPTION; Jordan to correct]`, only the order is ruled. Edit 5 (`FILLED_BY["annex"]` gains a taking basis) is rewritten: a won march's arrival fills nothing by itself, because a victor chooses to seize, occupy or withdraw (A-66); when he seizes a place its seats pass to him in the seizure's own write (A-58; `U5d_FA_land_and_seats_pass_on_a_won_march.md` edit 2), so the `annex` taking basis is needed only as that proposal's named revert (seats close and stand vacant for the seizer's conferral) and is not built otherwise; `place.surrendered` under a `capitulation` carries the seats the same way. An empty throne is claimed in the deed race (A-19), which reads this file's accomplishment ledger.

## Status: PROPOSED — one part HELD BACK for Jordan (the counts in edit 2 depend on `audits/15_INSTITUTIONS_COLONIAL.md` §11 item 1)

Source: Jordan, 2026-11-12, as `INSTITUTIONS_BRIEF.md` records it: *"current kingdom royalty is because
of nobility by deed/achievement"*; *"Royalty by noble conquest, i.e. the first king had the greatest
accomplishment in the secession war, followed by the first Duke of Hafenmark and the first Duke of
Varfell."* Audit §5, §12 batch C-4. Cross-lane: the crown lane owns succession and recognition; FA owns
`offices.yaml`'s seat rows and `state/gate.py::FILLED_BY`; ARCS owns the prehistory route
(`12_ARCS_case_on_the_realm.md`); CHAR owns `deeds_judged`'s weights. This file states what the colonial
family needs of each and authors only the parts no lane owns. Nothing is ratified by being written.

## What it changes in `engine/season/` at runtime

1. A person's estimate of another's standing includes a discounted share of the deeds of those who held
   the same seat before him, **as the estimating person's own ledger holds them**.
2. A built realm holds three dead founders and their Secession deeds as Events the cast has been told
   of. Declared hash mover.
3. The three built vassal oaths (`off_king.obligees`) are made under a `homage` instrument.
4. `off_duchess_hafenmark` is filled by inheritance through a title nobody holds at build.
5. A seat whose `conferral` is `annex` is filled by the holder of the seat through which its ground was
   taken. No seat in the built realm declares `annex`, so nothing moves until content does.

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

**1. `engine/season/queries/person_q.py::accomplishment(p, q, fx) -> float`.**

```
accomplishment(p, q) = own(p, q) + presumption_gain × Σ over seats s that p believes q holds
                                     accomplishment(p, predecessor(p, s, q))
```

- `own(p, q)`: the sum of `deeds_judged(p, q)`'s two parts (judged and told), unchanged.
- "seats `p` believes `q` holds" and `predecessor(p, s, q)`: read from `p`'s own claims of
  `tenure.opened` and `tenure.closed` on `s` (the person whose closing claim is the latest before `q`'s
  opening claim). A seat whose history `p` does not know contributes nothing: an heir is a nobody to a
  stranger.
- Recursion ends when `p` knows no predecessor; depth is bounded by the claims held.
- `data/fixtures.py: presumption_gain = 0.5` (dimensionless; sweep {0, 0.5, 0.75}; NUMBER row, graded
  `assumption`; `0` is the control and reproduces `own`).
- **Readers** (each an existing site that reads `deeds_judged` for a seat-holder's standing; this edit
  swaps the call, adds no site): the `rank`/standing gap behind `standing.band_crossed`
  (`queries/world_q.py::standing_crossed`) and `world_q.reception` where the speaker is heard *as the
  holder of a seat* [UNVERIFIED: which of `reception`'s terms reads `deeds_judged`; CHAR's
  `02_CHAR_scar_cap_and_regard_unit.md` owns the unit].

**2. Three founders and their deeds, seeded through the gate (HELD BACK: the counts).**
`engine/season/harness/populated.py::build_realm`, in the prehistory block ARCS' proposal adds (acts and
witnessed Events before tick 0, never constructed Claims): for each of `off_king`,
`off_duchess_hafenmark`, `off_duke_varfell`, a founder person (a `references/npc_registry.yaml` row,
`status: proposed`, dead at build), a `hold` on the seat opened and closed in prehistory, and `field.won`
Events with the founder as doer: **three, two and one** `[ASSUMPTION; the counts carry Jordan's order and
nothing else; under §11 item 1 option B Varfell's is zero in northern ledgers and one in southern]`. The
cast receives them `told_by` at build by the existing acquaintance route, each person weighing them by
his own pursuits. The first Almqvist's death (canon :116, "widely suspected assassination", perpetrator
TBD) is a `person.died` with no doer in anyone's ledger.

**3. `homage`.** `offices.yaml: off_king.obligees` rows become `{case: "NPC-050", form: homage}` (the
loader accepts a bare id as today; a mapping names an `instruments.yaml` row). `build_realm` mints one
`dispensation` per such oath (maker: the King; `to`: the vassal; `form: homage`; held by both) beside the
`oblige` it already opens. The Grand Master's oath (NPC-070) keeps a bare id: the Löwenritter's bond is
the crown lane's to name.

**4. `offices.yaml: off_duchess_hafenmark.conferral: null → inheritance`; `rosters.yaml: successions`
gains `off_duchess_hafenmark: off_heir_hafenmark`; `offices.yaml` gains the title seat
`off_heir_hafenmark` (`post: "Heir of Hafenmark"`, `rung: {duchy: "Hafenmark"}`, `conferral: appointed`,
`remit_acts: []`, `holder: null`).** `[ASSUMPTION; medium; Jordan to correct; revert: the three edits
together]`. Ladder step 4: `off_king`'s shape (IN-61). Canon gives Baralta no heir (:143), so the title
is vacant at build and **Hafenmark's succession is open from the first season**: whom she designates,
and whether a deed-claimant petitions instead, is play. [UNVERIFIED: that the loader admits a seat row
with `holder: null`; six rows are minted from the row alone, `offices.yaml:124-131`, each with a holder.]

**5. `state/gate.py::FILLED_BY["annex"]`** gains the taking basis: a `hold` on an `annex` seat may be
opened for the person who holds the seat `Act.via` of the act that took the seat's rung, in the same act
(`seize` at Overwhelming or Success under `…_B_distance.md`; a won `march`'s arrival; a
`place.surrendered` under a `capitulation`). Today `FILLED_BY` keeps `conferral` for `annex`
(`rosters.yaml: conferral_bases` note). `[ASSUMPTION; medium; Jordan to correct — this narrows a ruled
roster's unruled half; ladder step 4 on Jordan's statement that the founding seats were won by conquest;
revert: the mapping's entry]`. Owner: FA.

## Gate (execution artifact)

- `engine/season/tests/test_accomplishment.py`: on a hand-built world, an heir whose predecessor `p`
  knows of reads `own + 0.5 × predecessor's`; an heir whose predecessor `p` has never heard of reads
  `own`; `presumption_gain: 0` reads `own` for both; a three-holder chain reads `0.25` of the founder.
- Realm: `build_realm(0)` after edits 1–2: the probe prints, per cast person, his ordering of the three
  seat-holders by `accomplishment`. Pass: a majority order them king, Hafenmark, Varfell, **and at least
  one person does not** (the ledger is each person's own; unanimity would mean pursuits are not read).
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
- **E, last.** One function, one fixture, three seeded persons, five content cells, one gate entry.

## Cost class

Small build (the fold and its test); the seeding is a declared mover with re-pins; edits 3–5 are content
in FA's files.
