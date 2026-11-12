# NARRATIVE CHURN — eras, regimes and strife against allegiance, office, obligation, pursuit and conviction

## Status: REFERENCE (an audit; resolves nothing at runtime)

## Read at: d4ee8a4 (working tree)

Lane: narrative systems. Jordan, 2026-11-12: *"Fable to interrogate how eras, regimes, strife work
alongside faction allegiances, office duties, obligations and demands, pursuits and convictions, with the
goal to improve our emergent narrative basis to construct legible narratives and drive plot points
dynamically with compelling contributing worldly churn WITHOUT determinism."* Every reading below is a
dated reading of a command in §11 (`PYTHONHASHSEED=0`; seed and season count stated with it). Design
documents are cited for intent and vocabulary only (`CLAUDE.md` §0.05). The other lanes' audits and
proposals are cited, not redone; where this file repeats one of their numbers it says whose it is.

Vocabulary, as the tree uses it (so no reader takes a word in its ordinary political sense):

- **era**: the realm's one strife flow, a scope over every strife move under the realm rung
  (`queries/world_q.py::Era`, `_eras`; `strife-00` §4, R11). Not a calendar period.
- **regime**: Foucault's regime of truth (`strife-00` R13, R17), "an assemblage of institutions with
  commensurate dominant modes of understanding and behaving, not a political regime". In code it is one
  function and one fixture: `world_q.commensurate(w, a, b)` and `Fixtures regime_gain`.
- **strife**: an Event whose kind is in `rosters.yaml: strife_kinds` (`opens`, `joins`), linked into
  strands by `world_q._links`.
- **allegiance**: a live `commit` Tenure from a person to a faction's Proposition (`world_q.members`,
  `faction_of`) or to an organisation's goal (`goals.yaml`, `world_q.ambitions`).
- **office duty**: what a seat's holder may do (`offices.yaml: seats[].remit_acts`), and the `oblige`
  Tenure a person swears to a seat (`effects_governance._eff_oblige`). §1 shows these are the only two
  senses the code has.
- **obligation and demand**: `oblige` (with a `Term`), `petition`/`carry` (a Record, a docket item),
  `issue` (a writ: a `dispensation` Record), `comply` / `evade / defy`, `covenant`, `requisition`,
  `transfer`, `exchange`.
- **pursuit**: a weight on the canonical fifteen (`Person.pursuits`), projected to seven axes and dotted
  with a verb's alignment cells (`decision/choose.py::score_terms`).
- **conviction**: `Person.conviction`, an intensity 0 to 5 on each of five affiliations
  (`data/affiliations.py`); **scar**, a count per violated element (`loop/resolve.py::_scar_witnesses`).

## 0. Verdict

*(Written last; see the end of the file's build order in §11. Placed here.)*

VERDICT_PLACEHOLDER

## 1. The eleven things, as coded

One row per thing the direction names: its single owner, what the season loop reads of it, and what
reads it back. "Loop reader" means a step of `loop/` or a function `questions_for` or `choose` calls; a
harness or a test is not a loop reader.

| thing | owner (code reads this) | written by | loop reader | shipped state |
|---|---|---|---|---|
| season of the year | `world_q.season_of_year` (`:1169`): `tick % len(season_factor_draw)` | nothing (read off the tick) | `season_factor_of` → MATTER's yield | **no year exists**: `season_factor_draw = ()` (`data/fixtures.py:535`), so `season_of_year` is `None` every tick (E-N02) |
| calendar | `loop/calendar.py` (`Date.fired`, the docket) | `convene` (`date.scheduled`), CALENDAR | `sittings_before`, `docket_question` → a judge's question | live; fires sittings whose matters then lapse by clock (WR F-WR-13) |
| era | `world_q._eras`, `Era` (`:4929`, `:5233`) | nothing (recomputed from the log) | **none** (`world_q.py:4749-4752`: "NO CONSUMER IN THE LOOP") | one era per run, never concluded (E-N03) |
| ending | `rosters.yaml: endings` → `world_q.endings_reached` | nothing | the season summary only; halts nothing | `[]` in every run here; victory unreachable (WR F-WR-06) |
| regime | `world_q.commensurate` (`:5317`) over `data/affiliations.py::INCOMPATIBILITY`; `Fixtures regime_gain` 0.5 | nothing | `loop/witness.py::_credit` (`:240`), on a told claim's confidence, once, at deposit | live and **degenerate** (F-NARR-01) |
| strife | `rosters.yaml: strife_kinds`; `world_q.flows_in` (world), `flows_known` (person) | every verb whose row emits a move kind | `flow_stakes` → `questions_for` (the stamp, `stamp_flow_stakes` True) | live; reaches 0 to 28% of persons by seed (WR F-WR-07) |
| allegiance | `commit` Tenures; `world_q.members`, `faction_of`, `ambitions`; `goals.yaml` | `commit`, `release`; world-gen | `questions_for` Q4 (`need`), `attention_key` tiers 0 and 3 (salience), `opinion_referents` | live as attention; never changes hands (E-N05) |
| office duty | `offices.yaml: seats[]` (`remit_acts`, `conferral`, `revocation`, `obligees`); `state/gate.py` remit grant | `confer`, `succeed`, `revoke`, `establish`; world-gen | `Act.via`, `own_purview` (attention tier 1), `reach` | a **licence only**: no row says what a seat owes, to whom, or by when (F-NARR-03) |
| obligation | `oblige` Tenure + `Term` (`oblige_term` 4); the docket; writ Records | `oblige`, `transfer` (renews), MATTER (matures) | `establishment_of` → the obligee channel; `writs_held` → `comply` | terms mature unpaid by clock; `comply` never executes (E-N06) |
| demand | `petition` Record → `carry` → docket → `determine`; `issue` → writ; `requisition` | those verbs; MATTER lapses a docket item at `docket_lapse` 4 | `docket_question`, `sittings_before`, `matters_awaiting` | petitions accumulate and lapse (E-N06; WR F-WR-13; SC F-SC-01) |
| pursuit | `Person.pursuits`; `tables.alignment`; `decision/choose.py::score_terms` | `determine`/`argue` (`pursuit.moved`), scar shift (off) | the score's first term, every candidate | live; reads the verb only (CHAR F-CHAR-01) |
| conviction | `Person.conviction`; `tables.incompatible`, `tables.affiliation_engagement` | `conviction_after_crisis` (scar ≥ 3) | `crisis_weights` (the `doctrine` weight), `opinion_terms`, `heritage_regard`, `commensurate`; `confliction` damp (weight 0, off) | live in four small places; removing it changes nothing a story reading sees (E-N07) |
| scar | `Person.scar`; `loop/resolve.py::_scar_witnesses` | every witnessed act that violates a held element | `conviction_after_crisis`; `scar_weight_shift` (0, off) | runs away (CHAR F-CHAR-04); E-N05 |

**How a season joins them.** `calendar` → `matter` → five rounds of `deliberate → resolve → encounter →
witness` (`loop/driver.py::season`). The only place the eleven meet is `questions_for`
(`world_q.py:4031-4283`): a person's questions are (Q2) each new claim in his ledger whose subject his
`reach` covers, (Q4) one `need` per live `commit` to an OUGHT Proposition, the sitting and docket
questions, and then the standing occasions stamped on the first question as classed referents
(vacancies, seats named, writs held, places, matters awaiting, larders, holdings, propositions heard,
stage referents, the wounded, flow stakes). `attention_key` (`:3857`) orders them in five tiers. The
chooser then scores each candidate `(verb, referent)` as `pursuit + stance` (`choose.py:193-221`). So:

- allegiance, office and strife enter as **which referents a person is handed and in what order**;
- pursuit and (through `doctrine` and `regard`) conviction enter as **how a verb scores**;
- obligation enters as one referent class (`Record`, for `comply`) and one channel (the obligee's);
- era, the year and endings enter **nowhere**;
- regime enters one step earlier, as how firmly a told claim is held.

Nothing in that path asks *why* a referent matters to the person: a referent is a referent, whether it
is the lord who failed him or a granary he walked past. That is the subject of §3 and §5.

## 2. The edge map, each edge with an executed reading

Readings are E-N04 unless marked: `narr_probe.py <seed> 4 shipped`, seeds 0, 1, 2, four seasons, shipped
fixtures, 83 persons at build (46 cast with convictions, 37 cohort persons with none), written `a / b /
c` in seed order. States: **live** (executes and something reads it), **thin** (executes, small),
**starved** (built, its input almost never arrives), **degenerate** (executes, returns one value),
**clock** (resolved by MATTER's count, no person), **inert** (built, never executes or has no reader),
**missing** (no code). An edge another lane measured carries that lane's id and is not re-argued.

### 2.1 The weather: year, era, ending, regime, strife

| # | edge | owner | executed reading | state |
|---|---|---|---|---|
| W1 | year → harvest | `world_q.season_factor_of` | `season_of_year` is `None` at tick 1, 2, 4 and 6 in every run; every rung reads the bare `season_factor` 1.0 | **inert**: the calendar has no year unless the weather arm is on (F-NARR-06) |
| W2 | year → when things are done | none | 23 / 19 / 11 dates scheduled, all by `convene` acts, none keyed to a season | **missing** |
| W3 | era → anyone | `world_q._eras` | 1 era per run, `OPEN`, at four seasons and at six (WR E-08); its "opening kinds beneath" is `petition.filed` at seed 0 (E-N03) | **inert**: no reader, and it never concludes |
| W4 | ending → anyone | `world_q.endings_reached` | `[]` at every season of every run | **inert** (WR F-WR-06) |
| W5 | regime → belief | `witness._credit` × `world_q.commensurate` | told claims held at the end, by sign of `commensurate(hearer, last teller)`: −1: 20 / 8 / 14 (mean confidence 28.9 / 34.5 / 42.9); 0: 5 / 5 / 9 (78.6 / 94.0 / 82.6); +1: 0 / 0 / 7 (66.1). Over all pairs of convinced persons at build: −1 1,031, 0 none, +1 4 (E-N01) | **degenerate** (F-NARR-01) |
| W6 | regime → choice | none, by ruling (`ED-IN-0352`: "REGIME conditions belief at WITNESS … and is not read into the field") | control arm `regime_gain 0`: E-N08 | **missing by ruling**; see §2.6 |
| W7 | strife → the aware (the stamp) | `world_q.flow_stakes` | persons holding a flow in their own reading 1 / 8 / 23 of 83 / 82 / 81; with a stamped stake 1 / 7 / 15 | **starved** (WR F-WR-07; reproduced) |
| W8 | strife → the unaware | planned: CR-100 | not built | **missing**, scheduled |
| W9 | strand ↔ fault line | `world_q.incompatible_span` | `True` for every strand of every run (4 / 2 / 1 strands); same-size random parties read `True` with probability 0.54 to 1.00 (300 draws each) | **degenerate**: the base rate |
| W10 | strand → conclusion | `world_q.concluded` | strands concluded 0 / 0 / 0 at four seasons; largest strand 97 moves 23 doers / 72 moves 26 doers / 129 moves 29 doers | **inert** (WR F-WR-02) |

### 2.2 Allegiance

| # | edge | owner | executed reading | state |
|---|---|---|---|---|
| A1 | allegiance → what he attends to | `questions_for` Q4, `attention_key` | executed acts answering a `need` question: 92 / 96 / 107 of 1,569 / 1,734 / 1,799 (5.9% / 5.5% / 5.9%). Of those: a standing occasion with no ambition 38 / 37 / 43, his own want 26 / 29 / 25, **his faction's creed 25 / 27 / 36, an organisation's authored goal 3 / 3 / 3** (by subtraction; the `goals.yaml` rows) | **thin**: under 2.5% of what people do answers a faction |
| A2 | allegiance → how a verb scores | none (`choose.py:215` reads the verb) | CHAR F-CHAR-01; CHAR's `02_CHAR_goal_lean_on_its_own_question.md` proposes the term | **missing**, proposed |
| A3 | allegiance → changing sides | `commit`, `release` | persons whose `faction_of` differs between build and end: **0 / 0 / 0**. `commit` edges opened in play 80 / 134 / 90, every one to an uttered OUGHT Proposition, none to a faction; closed 0 / 1 / 1; `commitment.ended` 0 / 1 / 1 | **inert**: nobody joins or leaves a faction |
| A4 | allegiance → war | `world_q.at_war` | open-referent arm `at_war 0` (E-N03); no WAR Proposition is built (FA F-FA-04, FA_B E-B1) | **inert** |
| A5 | allegiance ↔ conviction | `world_q.opinion_of` (`:3029`), its affiliation term over `engaged_poles` | at build (E-N13): 4 of 43 members hold an opinion of their **own** faction below indifference, and 27 of 43 rate another faction above their own; but the affiliation term is zero for 8 of 9 factions (only the Church's goals engage a pole: 2 of 38 goal rows carry `engaging:`), and `opinion_of`'s one caller (`opinion_referents`, `:3113`) asks it only of the faction of a deed's doer, never of the person's own. At "stands for" the Crown's faction is split (2 orthodox, 1 Restoration, 8 neither) (E-N01) | **inert**: computed, never asked of one's own side (F-NARR-05) |
| A6 | faction → a head who can act for it | `faction_q.head` | FA F-FA-16: five of ten factions have no head | **thin** |

### 2.3 Office

| # | edge | owner | executed reading | state |
|---|---|---|---|---|
| O1 | office → what its holder may do | `Act.via`, the remit grant | acts carrying a seat: attempted 290 / 233 / 290, executed 93 / 82 / 113; executed through a seat: `issue` 40 / 23 / 47, `convene` 23 / 19 / 11, `dispatch` 16 / 13 / 22, `open_case` 7 / 13 / 7, `march` 5 / 7 / 11, `determine` 1 / 2 / 1; never: `covenant`, `raze`, `seize`, `pardon`, `revoke`, `confer` | **live** as a licence |
| O2 | office → what its holder owes | none | no key of `offices.yaml: seats[]` states a duty; the 33 seat-holders' most executed verbs are `create_record` 177, `utter` 77, `reconstruct` 73, `commit` 43, `issue` 40 (seed 0), the first four also the non-holders' top four | **missing** (F-NARR-03; FA F-FA-05 for the choice half) |
| O3 | office → changing hands | `confer`, `succeed`, `revoke`, MATTER | seat holds closed 0 / 0 / 0; opened after build 0 / 0 / 0; `confer` 0 of 8 at seed 2, `revoke` 0 of 11 at seed 0, `succeed` never formed | **inert** (FA F-FA-02) |
| O4 | seat → regard for the one in it | `choose.py::stance_term`, the `ABSENT: H-195 holder` marker | 0 persons hold a `held_by` claim (H-195's reading, re-read: the stem has no depositor, `grep held_by engine/season` E-N12). Marcher against the governing holder of the rung marched on: `commensurate` −1 in 37 / 7 / 6, 0 in 3 / 3 / 5, no holder 0 / 5 / 14 of 40 / 15 / 25 marches: the base rate | **missing** (F-NARR-04) |

### 2.4 Obligation and demand

| # | edge | owner | executed reading | state |
|---|---|---|---|---|
| B1 | oath → the seat's household | `_eff_oblige`, `establishment_of` | `oblige` executed 46 / 39 / 89 of 219 / 91 / 157; every edge's object a seat; edges at the end 50 / 45 / 93 | **live** |
| B2 | oath → service | none | executed acts by a sworn person on the seat he is sworn to or on its holder: 106 / 63 / 134, of which the oath itself 46 / 39 / 89 and the rest `create_record`, `utter`, `reconstruct`; `comply` 0 | **inert**: an oath obliges nothing |
| B3 | oath → pay → renewal | `_eff_transfer`, `Term` | `term.renewed` 0 / 0 / 0; `transfer` executed 2 / 3 / 7 of 98 / 129 / 108 | **inert** (FA H-158) |
| B4 | unpaid oath → lapse | `loop/matter.py:428-435` | none by season four; at season six the `oblige_term` 4 matures them together (WR_B §3.2: `tenure.closed` 27, 27 at seeds 0, 1). E-N10 | **clock** |
| B5 | writ → the one it binds | `writs_held` → `comply` | `issue` executed 40 / 23 / 47; `comply` 0 of 66 / 64 / 63; `evade / defy` 0 of 9 / 9 / 8; `compliance.impossible` 75 / 73 / 71 | **inert** (FA F-FA-01) |
| B6 | petition → answer | `carry`, the docket, `determine` | filed 35 / 44 / 44; carried 5 / 3 / 5; `matter.determined` 0 / 2 / 0; docket at the end 23 / 25 / 20 items | **starved**, then **clock** (WR F-WR-13; SC F-SC-01) |
| B7 | bargain | `covenant` | 0 of 24 / 23 / 20 | **inert** (SC, FA_B) |
| B8 | market | `exchange` | 0 / 1 / 0 of 93 / 91 / 85 | **inert** (SE F-SE-01, F-SE-07) |
| B9 | levy on stores | `requisition` | 0 / 2 / 7 of 9 / 8 / 14 | **thin** |
| B10 | a due unmet → a grievance against whoever owed it | none | no Event of a lapse names a person: `tenure.closed` by maturity has `subject = the edge id`, `causes = [the oath]` (`matter.py:431-435`); `matter.lapsed` cites the docketing Event | **missing** (F-NARR-02) |

### 2.5 Pursuit, conviction, scar

| # | edge | owner | executed reading | state |
|---|---|---|---|---|
| P1 | pursuit → choice | `score_terms` | CHAR F-CHAR-01, F-CHAR-02 | **live**, verb-only |
| P2 | argument → pursuit | `determine`, `argue` (`pursuit.moved`) | persons whose pursuits changed 3 / 0 / 1 | **thin** (CHAR F-CHAR-03) |
| P3 | conviction → choice | `crisis_weights` (the `doctrine` weight), `regard` | ablation, every conviction cleared at build (E-N07): see §4.3 | **inert for story** (F-NARR-07) |
| P4 | deed → scar → crisis → changed conviction | `_scar_witnesses`, `_conviction_crisis`, `conviction_after_crisis` | scar total 0 → 34,977 / 33,330 / 35,058; persons whose conviction changed **6 / 8 / 8**; Events emitted for those changes **0** (`resolve.py:707-709`: "Nothing is emitted"); draws made 0 (`person_q.py:903-904`: "ROLLS NOTHING") | **live, silent and undrawn** (F-NARR-08; CHAR F-CHAR-04 for the scar) |
| P5 | conviction → refusing an act | `affiliation_engagement` | executed acts whose verb violates the actor's own affiliation: 21 / 25 / 24, all `forge` but two `thread_read` | **thin**: two verbs carry a cell |

### 2.6 What the map says, in one paragraph

Of thirty-five edges, six are live, six thin, and twenty-three are starved, degenerate, by clock, inert
or missing. The live ones are the ones a clerk needs: a seat licenses a writ, a person swears to a seat,
a pursuit ranks a verb, a deed scars a witness. Every edge that would carry a **crossing** (a demand
against the one who owes it, a duty against its holder, a stand against a side, a new holder against an
old oath, a rising against a fault) is missing or reads a constant. The systems run beside each other.

## 3. Failed links, ranked

Each: severity · claim · evidence · falsifier and its outcome · requirement touched · consequence ·
minimal fix at the owner. Steelman first where one exists.

### F-NARR-01 · degrades narrative · the regime is one value

**Steelman.** CR-79 is ruled, built behind a guard, has a control arm and a test that the realm reaches
it; R13's definition is in the code as `commensurate`. **Attack:** print what it returns.
**Claim.** `commensurate` returns −1 for 1,031 of the 1,035 pairs of persons it can distinguish, so the
credit term is a flat discount on hearsay inside the cast and R13's "assemblage … with commensurate
dominant modes" has one assemblage in it.
**Evidence.** §2 W5, W9; E-N01. Cause: `world_q._held` (`:5339`) reads intensity above zero, and
`ED-IN-0293 (2)` gives every NPC a low intensity on three concerns (90 of 148 holdings are 1, which
`person_q.conviction_stand` reads as standing *against*). Three readers, three readings of one number
(`20_NARRATIVE_A_stands_for.md`, the table). At "stands for" (intensity above the midpoint) the same
realm reads −1 130, 0 779, +1 126, and the sets follow the factions.
**Falsifier.** A run in which told claims between convinced persons land at more than one sign. Seeds 0
and 1: none (−1 only). Seed 2: seven at +1, all inside the four pairs of the realm that read +1. The
test `test_the_realm_reaches_commensurate…` passes throughout; it asserts a call, not a spread.
**Touches.** R-07, R-08 (what a person credits); strife R8, R13, L4.
**Consequence.** Era and regime were to be the weather. The regime half is a drizzle that falls on
everyone alike; a Restoration man discounts a fellow Restoration man's word exactly as he discounts a
Cardinal's.
**Fix.** `20_NARRATIVE_A_stands_for.md`.

### F-NARR-02 · blocks the plot points asked for · an omission has no author

**Steelman.** `04` F.3 and AX-5 are met: a matured term "cites the act that wound it", so "a lapse is a
story with an author" (`matter.py:402-404`). Nothing is triggered; T-n forbids a term nobody can end.
**Attack:** ask whom the lapse blames.
**Claim.** Three of the five crossings Jordan names are omissions (a demand unmet, a duty failed, an
obligation not kept). The log records acts. When a due lapses, the Event names the edge or the docket
item and cites the act of the party who *asked* (the oath, the docketing), never the person who owed
and did nothing. No claim that anyone holds says who let it lapse, so no regard moves, and nothing in
any later season can be read as an answer to it.
**Evidence.** `matter.py:428-435` (`subject=t.id`, `causes=[t.term.declared_by]`: the declarer is the
*obligee* who swore, or the last payer); `:437-…` (`matter.lapsed`, cause the docketing Event);
`epistemic.claim_subjects` reads only a `hold` edge as its two ends, so the deposit is a claim about a
Tenure id (`world_q.py:5403-5415` states this for `detain`); `seen_of` gives an actorless Event an
all-`None` sighting (`epistemic.py:1049-1066`), so `person_q.deed_doer` can pair it with nobody;
`person_q.deeds_judged`'s own note: "THE SWORN-TO HALF IS NOT BUILT … what is missing is the PAIRING"
(`:121-126`). Run: petitions filed 35 / 44 / 44, determined 0 / 2 / 0 (B6); writs 40 / 23 / 47, complied
0 (B5); oaths 46 / 39 / 89, renewed 0 (B3). At four seasons none of these has yet lapsed (the terms are
4); what the lapses occasion at six seasons is E-N10, §4.4.
**Falsifier.** A ledger claim, in any run, whose predicate is a lapse kind and whose pairing names a
person. None can be deposited, by the two code facts above.
**Touches.** R-01, R-02, R-06; NERS-R (no-player half).
**Consequence.** The realm's commonest ending is an expiry (WR F-WR-13: 23 lapsed against 3 determined)
and an expiry is nobody's fault. Neglect, the cheapest source of grievance in every history the strife
study read (its category C and H openers: a burden, pay owed), produces none.
**Fix.** `20_NARRATIVE_B_a_lapse_has_a_door.md`.

### F-NARR-03 · degrades narrative · an office is a licence and owes nothing

**Claim.** "Office duty" has no carrier. A seat row holds what its holder *may* do (`remit_acts`), how
it is filled and stripped, and who is sworn to it. Nothing states what the seat owes: to hear what is
docketed before it, to pay its sworn, to keep its people fed. Each of those exists as a *standing
occasion* on the holder (`matters_awaiting`, the upkeep `transfer`, `larders_in_purview`), and each
expires unanswered with no trace on him (F-NARR-02).
**Evidence.** `offices.yaml:186-200` and every seat row (keys: `id, post, rung, body, faction,
remit_acts, conferral, revocation, holder, obligees, source, note`); O2's reading; FA F-FA-05.
**Falsifier.** A key on a seat row, or a predicate, that a holder can fail. `grep -n "duty" offices.yaml
governance_spine.yaml`: none; `duty.taken` / `duty.refused` are `oblige`'s kinds, the sworn person's.
**Touches.** R-04, R-06.
**Fix.** No new "duty" object. The three dues that already reach a holder are made answerable
(`20_NARRATIVE_B`); what a seat pays is BYZ's `15_INSTITUTIONS_BYZANTINE_B_the_roga_and_the_fisc.md`
(`seats[].upkeep`), cited, not redone.

### F-NARR-04 · degrades narrative · nobody knows who holds what, so nothing is aimed

**Steelman.** AX-2 and AX-7 forbid a person reading the world's `hold` edges; H-195 records the gap and
its trigger honestly. **Attack:** read what marches are occasioned by.
**Claim.** A person's regard for a seat or a rung reads 0 or stray deed claims about the place, never
his regard for the person he believes holds it, because no ledger holds a `held_by` claim and nothing
deposits one. So a grudge cannot aim a march, an oath is not weighed by who now sits in the seat, and a
change of holder is not news about a person.
**Evidence.** H-195 (`hole_register.yaml:4415-4426`); no depositor of the stem (E-N12). Occasions of
the 80 `march` acts formed over the three runs (E-N04; the probe prints the seven commonest per seed,
66 of the 80): a sighting claim (`seen`) 45, `finding.made` 7, `transfer.refused` 4, `travel.blocked` 2,
`commitment.made` 2, and one or two each of `record.forged`, a grain store, `tell.refused`,
`establish.refused`, `case.opened`. None is of a kind that names who holds the rung marched on, and no
such kind can be held. Marcher against that holder by `commensurate`: the base rate (O4).
**Falsifier.** A march whose occasion is a claim naming the target rung's holder. None in the 66
printed; none possible while the stem has no depositor.
**Touches.** R-01, R-06, R-08; H-195; strife's "opening on a fault line".
**Consequence.** "A regime change meeting an obligation" cannot register even if a seat changed hands
(it does not, O3): the sworn man's stance toward the seat he is sworn to has no person in it.
**Fix.** `20_NARRATIVE_C_who_holds_what.md`.

### F-NARR-05 · degrades narrative · allegiance is fixed and no stand can cross it

**Claim.** Membership of a faction never changes in computed play. A member's opinion of his own
faction is computable and is never asked; its conviction term is zero for eight factions of nine.
**Evidence.** A3 (0 / 0 / 0 persons changed faction; no `commit` to a faction opened or closed); A5
(27 of 43 members rate another faction above their own at build, and none moves in four seasons).
`rosters.yaml: strife_kinds.never` holds `commitment.made`, `commitment.ended` and `stance.moved`
(`:3394-3395`), so a defection could not open or join a strand if one occurred, and the study's DA
links (`DA>WA`, `WN>DA`) print UNREACHABLE (E-N03). The Crown's own seat row calls the Grand Master's
`release` of her oath "the Split" (`offices.yaml`, `off_king`'s `obligees:` comment); `release` executed 4 / 10 / 5 times, on what the
probe did not resolve `[UNVERIFIED]`, and `faction_of` moved for nobody.
**Falsifier.** A person whose `faction_of` differs at the end. None at three seeds, four seasons.
**Touches.** R-02, R-06; strife category D and F.
**Fix.** Two halves, two owners. The fault line becomes readable under `20_NARRATIVE_A`. The occasion
to leave is `20_NARRATIVE_C` edit 3 (a change of holder is put to the sworn). Whether a defection is a
strife move is the kind list's (ratified `strife-01` §6 ruling; §10 item 2 below).

### F-NARR-06 · degrades legibility · the calendar has no year and the era has no reader

**Claim.** The engine cannot say what season of the year it is, and the one object called an era is a
scope no step reads and no run concludes.
**Evidence.** W1 to W4. `world_q.season_of_year` (`:1169-1175`) takes the year's length from
`season_factor_draw`, a *weather* arm that ships `()`: the calendar exists only when it rains. The
chronicle (`harness/chronicle.py`) prints a season index and nothing else (WR F-WR-14).
**Falsifier.** `season_of_year(w)` not `None` at shipped fixtures. `None` in every run (CALENDAR line).
**Touches.** R-03 (legibility of the tick); NERS-S (zooms across scales of time).
**Fix.** `20_NARRATIVE_D_the_year_and_the_reason.md` edit 1. The era's reading is WR's and the plan's
(CR-97 to CR-103); what this lane adds is that those positions will read a constant regime and a
one-strand realm unless `20_NARRATIVE_A` and `09_WR_strand_conclusion.md` land first (§9).

### F-NARR-07 · degrades narrative · conviction can be removed and no story reading moves

*(evidence in §4.3; written when E-N07 completed.)*

### F-NARR-08 · degrades narrative (R-09) · a change of conviction is silent and decided by rule

**Claim.** The engine's most personal event, a person's creed breaking, happens 6 to 8 times a run,
emits no Event, deposits no claim, reaches no chronicle and is decided by a fixed rule.
**Evidence.** P4. `loop/resolve.py:707-709`: "Nothing is emitted … an Event here would deposit claims
about every observer"; `person_q.py:903-904`: "THE ENGINE CHOOSES PER CASE, BY A RULE OVER STATE … AND
ROLLS NOTHING" (`ED-IN-0261`'s superseding row, Jordan 2026-10-06); the same docstring: under the
shared column "the selector … folds the HIGHER-held creed into the lower", so a zealot's creed transfers
to the creed he stood against. Which six persons, and into what, the first runs did not print; E-N10 prints them.
**Falsifier.** An Event of any kind whose changes name `Person.conviction`. `grep` of the KINDS lines:
none in any run.
**Touches.** R-06, R-07, R-09; the standing rule (a thing that could go either way for the person).
**Fix.** `20_NARRATIVE_D` edit 3; it overwrites a ruled item and is listed in §10.
