# INSTITUTIONS / VENICE — the merchant republic, the banking house and the league: design and implementation plan

Reconciled: 2026-11-12 by `audits/15_INSTITUTIONS_SYNTHESIS.md` §2 — where this file's names, homes or shapes differ from that ledger, the ledger governs: "roll" keeps this file's meaning for the whole kit (X-04); `debt` is a Record kind and also a form, read by the kit's one set of instrument readers (X-09); the trade charter of §6.1 part 5 is the form `staple` and no `charter` obstacle term is added (X-10); warrant and commission are forms (X-11); the exit audit is the row `audit` under the key `audit_at_exit` (X-12); part 3's ballot is SC's ballot with `obligation` among its terms, and `pledge_step` is not added (X-15); `obligation` is lifted by `excused`, not by a bare ban (X-31); the scenario is a case file (X-32). The four disagreements of §4.4 are each decided in the synthesis's §4.5, with canon amendment text drafted in its §4.6. Of §14.2: all three are closed in the synthesis's §10 with their ladder steps. Every finding below stands.

Re-grounded: 2026-11-12 against the tree's own research (Jordan: *"Research should have been found in /research or /proposals"*), map and claim table in `unified/RESEARCH_MAP_INSTITUTIONS_B.md` (rows V-1 to V-50). What changed in this file: the sourcing key gains the mark `[T+]`; of the forty-two claims marked `[M]` in whole or part, twenty-six now cite a tree source at path:line for the whole or for part, and sixteen stay wholly memory-grade (listed, with the still-memory parts of the others, in §17.3); **seven statements are corrected** where the tree's source differs (§17.1: when the Ten became permanent; what the 1297 *Serrata* enacted; the Arsenal's two figures; the Arsenal men's part in 1355; where the tree's sumptuary magistracy sits; the motive of the Pazzi's backer; the mechanism of Savonarola's fall) and three figures or dates are replaced by the tree's (rectors' terms; the Bruges blockades; the *condotta*'s second phase); **thirteen mechanisms the research describes and this design lacked are added** (§17.2), with their exact edits in `proposals/15_INSTITUTIONS_VENICE_grounding_E_what_the_tree_adds.md`; §15's nulls are restated against the game-precedent suite, which is now opened; E-4's skip of `.audit/2026-07-09-comparative-governance-research` is withdrawn as wrong. No finding of this lane or of the synthesis is deleted; the five parts, the fourteen resolutions and the three survivors stand.

## Status: REFERENCE (a design and plan in proposal form; resolves nothing at runtime, CLAUDE.md §0.05)

## Read at: bb6dfc3 (working tree); re-grounded at 62dbc8b

Family: **VENICE** — the Republic of Venice; Medici-era Florence and the Italian city-state world; the
Hanse and merchant guilds where the tree's research treats them. Work order:
`proposals/2026-11-12-subsystem-audit-suite/INSTITUTIONS_BRIEF.md`. Proposals carrying the exact edits:
`proposals/15_INSTITUTIONS_VENICE_*.md` (listed in §13).

**Sourcing key.** `[T: file §]` = the tree's research, opened at that section this session. `[CONT]` =
Contarini as transcribed in `research/social_contest_procedures/01_venice_procedure.md` (a patrician's
idealised account of the rules, not a record of practice; that file says so). `[M]` = my memory of the
standard secondary literature (Lane, Finlay, Chojnacki, Mueller, Puga and Trefler for Venice; de Roover,
Rubinstein, Kent, Najemy, Padgett and Ansell, Mallett for Florence and the condottieri; Dollinger and
Greif for the Hanse and guilds), **not opened this session and therefore memory-grade**: shapes are the
finding, every figure and date tagged `[M]` is a lead. No web source was fetched for this file.
`[T+: file:line]` = added by the re-grounding pass of 2026-11-12: the tree's research, opened at that
line, either supporting a claim first written from memory or correcting it; short names as in
`unified/RESEARCH_MAP_INSTITUTIONS_B.md` (`GM`, `PHS`, `CPS` the three governance files; `CGR`
`.audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md`; `PMP`
`.audit/2026-08-06-social-contest-three-lens-audit/sources/01_political_mechanics_primitives.md`; `FASE`,
`PGS`, `HCC`, `RTP`, `DPC` the precedent, proactive-governance, historical-concerns, rise-to-power and
decision-procedure files). Where `[M]` still stands beside a `[T+]`, the `[T+]` covers part of the bullet
and §17.3 says which part is still memory. All of it is tier 3: it informs, it settles nothing.

---

## 0. Verdict

*(Written first, revised last; see the end of §0 for what changed on revision.)*

The engine can already carry the **skeleton** of a merchant republic, a banking house and a league,
because its governance primitives are the right ones: a seat is a row with a rung, a body, a remit, a
conferral basis and a revocation basis (`engine/season/offices.yaml`); a proceeding is thirteen
parameters (`engine/season/arrangements.yaml`), including `disposal: declared` with a `quorum`, a sealed
or open `floor`, and `records_dissent`; obligations, bans, detentions and holds are Tenures; claims and
deeds are stored facts persons read. What it cannot yet carry is the part that made these three
institutions *what they were*: **(1) the term** (rotation, cooling-off, the audit at exit), **(2) the
roll** (who is on the list from which seats are filled, and who edits the list), **(3) the lot** (a
draw between vetted names as a conferral step), **(4) the credit line** (a debt as an obligation with a
principal, a term and a default, held by a person or a house against a person, a seat or a treasury), and
**(5) the charter of a place held at distance** (a seat appointed from the centre for a short term over a
subject settlement, with an auditor sent after it). The single largest obstacle is (4): the tree has no
stored debt between persons that another person can read, call, sell or default on, so "a loan against a
throne", the Medici's whole method, the commenda and the Venetian public debt all have nowhere to sit.
Everything else in this family is a data edit or a small build on a primitive that exists.

A sixth gap sits under all five and is the cheapest to close: **(6) no tie changes any odds.** An oath, a
debt or a favour is an edge that exists and that no roll reads, so patronage, the one mechanism the
Medici ruled by, has no effect at the moment it is tested. One obstacle term (`obligation`) repairs it
for every institution family at once. And under the standing rule (*we do not do deterministic*) every
election, vote, repayment, favour and plot in this design resolves by a draw whose odds come from
persons, seats, ties and the room (§6.2).

The design below adds **no new institution type and no faction special case**. Venice, Florence and the
Hanse come out as *configurations* of five reusable parts on existing owners, and are placed in the world
on Hafenmark, the Guilds and the Schoenland interface (§5), not as imported polities.

---

## 1. How it really worked — the Republic of Venice

### 1.1 The design problem the constitution answers

Venice's constitution is one answer to one question asked for six centuries: *how does a small ruling
class of trading families govern itself without any one family, any one man or the crowd taking the
state?* Every mechanism below is a countermeasure with a date and a named abuse behind it. The Doge
lynched in 1172 produced the Great Council and the six councillors `[T: research/governance/governance_modes.md §Venice 1.2]`; the
attempted hereditary dogeship of 976 produced election for life with no succession `[T: ibid. 1.3]`; the
deadlocked election of 1229 produced the 1268 lot-and-ballot protocol `[T: ibid. 1.8]`; the
Tiepolo–Querini conspiracy of 1310 produced the Ten; the Doge's own conspiracy of 1355 made the Ten
permanent `[T: ibid. 1.6; research/governance/conflicts_power_struggles.md §Venice 3.2–3.3]`.
**Corrected `[T+: GM:310, against GM:345]`:** the tree disagrees with itself here. The body text dates
permanence to 20 July 1355; the verifier's note quoted at the head of the same section orders "1334
(commonly; some sources 1335)", and the fix was quoted, not applied. On the verified reading the Ten was
already permanent when it tried and beheaded a Doge; 1355 is the first use of the standing bench against
the capstone, not its founding. The pattern to
carry into the game is the **ratchet**: each failure writes a new clause into a standing instrument, and
the instrument is read at the next accession. The ratchet does not depend on the date.

### 1.2 The Doge and his constraints

- **Elected for life, never hereditary; no succession interest.** Sons and brothers of a sitting Doge
  were barred from the main councils and from benefices during his reign `[M]`.
- **The *promissione ducale*.** A written oath enumerating what the Doge may not do, sworn at accession
  and **re-drafted and lengthened at every accession** by the *Correttori alla Promissione Ducale*, whose
  task was to close whatever the last Doge had got away with `[T: governance_modes.md §Venice 1.3]`.
- **Constraints in the text.** He could not open diplomatic letters or receive envoys except with his
  councillors present; could not leave the city, own property abroad, trade, accept gifts, or correspond
  privately with foreign powers; had one vote and no veto `[T: ibid.; M for trade and gifts]`
  `[T+: GM:326-328: letters, envoys, leaving the palace unescorted, private correspondence with powers
  or kin abroad, no veto; property abroad, trade and gifts are not in the tree]`.
- **The six ducal councillors** (one per *sestiere*, short terms) co-signed every act; with the three
  heads of the Forty they formed the **Signoria** of ten, which, not the Doge, held the sovereign
  capacity. A councillor could put a motion the Doge opposed; the Doge could not act with fewer than a
  set number of them present `[T: ibid. 1.5; M for the presence rule]`.
- **Audit at exit.** On his death the *Inquisitori sopra il Doge defunto* reviewed the whole reign against
  the oath and could fine the estate before the heirs took it `[T: ibid. 1.3]`.
- **What the office was for.** Continuity, ceremony, presiding, and the informal weight of the one man who
  sat in every council for life while everyone else rotated. A strong Doge ruled by being the best-informed
  person in each room, not by command (Finlay's reading `[M]`).

### 1.3 The Great Council: the roll, the lot and the ballot

- **The roll.** The *Serrata* of 1297 fixed membership to those who had sat in the previous four years and
  their descendants; the *Libro d'Oro* (formal from 1506) made nobility a matter of a registered birth
  verified by the Avogadori (*prova di nobiltà*) `[T: governance_modes.md §Venice 1.4;
  political_hierarchy_standing.md §Venice 2.2]`. **Narrowed `[T+: GM:311]`:** the verifier's note strikes
  the hereditary clause from the 1297 act itself: the ordinance confirmed those who had sat in the
  preceding four years, balloted by the Forty; descent as the test is the later hardening (the
  registration of 1315 to 1318, the book of 1506, `GM:334`). So the closure was **a ballot on sitting
  members first and a birth register after**, which is §5.2's adapted form (enrolment by a body's ballot)
  more nearly than the audit knew. A yearly lot (the *Balla d'Oro*) admitted some young men early
  `[T+: PHS:346]`. The body was every adult male patrician (some 1,000 to
  2,500 at different dates `[M]`); its business was **election**, not debate.
- **Election by lot and ballot** `[CONT p.22–39]`, stage by stage:
  1. Doors shut; the Grand Chancellor reads the vacancies; Avogadori and the Heads of the Ten sit apart as
     watchers.
  2. **Lot picks the nominators.** Benches are called by lot; each man draws from a pot; a gold ball sends
     him to a second pot; gold again makes him an elector. Thirty-six electors in four groups of nine
     ("hands"). Kin of an elector may not stand; no two of one family in one hand.
  3. **Nominators name, and are liable.** In a closed room each of the nine draws a number, names a man for
     the office of that number, and the nine ballot him; six of nine confirm. *The nominator stands surety
     for his nominee's handling of public money.*
  4. **Up to four competitors per office** go to the floor; competitors and their kin leave the hall.
  5. **Secret ballot** with linen balls into a double urn (silent, so the choice cannot be heard or seen);
     the winner must have the most **and more than half**; otherwise the office is void until the next
     session.
- **The 1268 Doge protocol** alternates lot and election nine times (30 → 9 → 40 → 12 → 25 → 9 → 45 → 11 →
  41), ending in 41 electors who need 25 votes `[T: governance_modes.md §Venice 1.8]`. Lot breaks
  prearranged coalitions between stages; election keeps judgment.
- **What rules it produced around itself.** *Contumacia* (a cooling-off equal to the term before
  re-election), *divieto* (kin may not sit together), the *debt-bar* (a noble in arrears to the treasury
  holds no office), short terms almost everywhere `[T: political_hierarchy_standing.md §Venice 2.6]`.
- **How it was gamed.** *Broglio*: canvassing in the square before sessions, illegal and universal; vote
  trading between houses; and, late, the *barnabotti*, poor nobles with a full vote and no income, who
  sold it `[T: ibid. 2.6; conflicts_power_struggles.md §Venice 3.8]`. The roll was sold outright three
  times in fiscal emergency (1381 after Chioggia; 1646–1718, about 100,000 ducats a family) `[T:
  political_hierarchy_standing.md §Venice 2.5]`.
- **Refusal was punished.** Election to an expensive or dangerous post (an embassy, a distant rectorship)
  could be refused only on payment of a fine or loss of eligibility `[M]`. Office was a burden laid on the
  class by itself, which is why the lot was tolerable.

### 1.4 The Senate, the College and the menu of opinions

- **The Collegio** (Signoria plus sixteen *Savi* in three orders: great, mainland, sea) received
  petitioners and letters each morning, deliberated, and wrote **each Savio's opinion down separately**
  `[CONT p.70–73]`.
- **The Senate** (*Pregadi*; about 120 elected plus ex-officio members, some 230 voting `[CONT p.66–68;
  T: 01_venice_procedure.md §2.1]`) heard the **whole menu of written opinions**, not one motion. Savi
  spoke first; an ordinary senator could speak only after them and **could not put his own motion**: a
  member of the College had to carry it `[CONT p.74–75]`.
- **The ballot**: one pot per opinion plus a green (reject all) and a red (doubtful); if none has half,
  drop the lowest and re-ballot until one does `[CONT p.75–76]`.
- **Why this shape.** Agenda power sits in a small rotating college whose members serve six months;
  decision power in a large body that cannot initiate; neither both proposes and disposes
  `[T: governance_modes.md §Venice 1.5]`.

### 1.5 The Ten, the Inquisitors and the Avogadori

- **The Council of Ten**: ten elected for a year, no two of one family, not re-eligible at once; the Doge
  and six councillors sit with them (17); three *Capi* rotate monthly and set the agenda; an Avogador
  attends without a vote and may suspend `[CONT p.78–81; T: 01_venice_procedure.md §1.4]`. A *Zonta* of
  fifteen or twenty senators was added for grave cases until 1582–83, when the Great Council refused to
  elect it and cut the Ten back to security matters `[T: conflicts_power_struggles.md §Venice 3.6]`.
- **Its rite** is the inquisitorial one: written secret denunciation (the *bocca di leone*), a threshold
  vote to accept it, spies to verify before witnesses are examined, the accused never in the room, no copy
  of the evidence, no counsel in the hall, secret ballot in a fixed order of office, no appeal `[T:
  01_venice_procedure.md §1.1, §1.4]`.
- **The three State Inquisitors** (two from the Ten, one ducal councillor; standing from 1539) act only
  **unanimously**; one inquisitor's urgent arrest is void if the other two dissent; a heavier penalty goes
  up to the Ten `[T: ibid. §1.5]`.
- **The Avogadori di Comun**: sole public accusers before the Forty; keepers of the nobility register;
  present in every council with the power to **suspend an act as unlawful** (*intromissione*) and to
  prosecute a magistrate, the Doge included `[T: ibid. §1.6]`. What happens after a suspension the tree's
  research could not source `[T: ibid. Gaps 2]`; nor can I.
- **Self-correction and its price.** Antonio Foscarini, strangled 1622 on informers' evidence, publicly
  exonerated by the Ten in 1623 `[T: ibid. §3.6]`. A secrecy-optimised bench makes this error and can only
  repair it by publishing its own mistake.

### 1.6 Commenda and colleganza: the contract that made the class

`[M]` throughout (Lane; Puga and Trefler 2014; Pryor), shapes only. **Still memory-grade after the
re-grounding pass:** the word *commenda* occurs in no file of the tree (the work order's own grep for it
matches "recommendation"), nor does *colleganza* or the sea loan. Three analogues are in the tree and
are what the design can lean on: the Mongol ***ortoq***, a ruler's capital placed with merchants who
carry a portable privilege and return a share `[T+: HCC:165]`; **the pledge of a future yield** to a
financier for cash now, with the creditor's own ruin when the debtor is a prince who defaults
`[T+: HCC:148]`; and **the loan secured on a named right** `[T+: HCC:161; CGR:190]`.

- **Two parties, one voyage.** A **sedentary partner** (*stans*) puts up capital; a **travelling partner**
  (*tractator*) takes it to sea, trades, returns and renders account. The contract names the capital, the
  destination or a free hand, and the split, and is **liquidated on return**.
- **Unilateral form**: the stans supplies all the capital and takes about three quarters of the profit; the
  traveller takes a quarter and risks only his labour. **Bilateral form (*colleganza* proper)**: the stans
  two thirds of capital, the traveller one third, profit split evenly.
- **Liability**: the investor's loss is capped at his stake (loss by sea or enemy falls on capital); the
  traveller is liable for fraud and for departing from instructions. The **account on return** is the
  enforcement point: a traveller who does not render it is pursued in the merchant court and loses the
  ability to raise the next voyage.
- **Its social effect**: a young man with no capital could become rich in a few voyages; investors spread
  small stakes across many travellers and voyages. This is the channel by which new families rose before
  1297, and the *Serrata* and the fourteenth-century restrictions on who might ship on the state galleys
  closed it: the class that had risen by open contract made the best trade a privilege of the roll (Puga
  and Trefler's thesis).
- **Predecessor and sibling**: the **sea loan** (repayable only if the ship arrives, at a high premium),
  and, later, resident agents on commission as trade became regular.

### 1.7 The *stato da mar* and the galley system

`[M]` for the detail; the tree holds the rettori shape `[T: research/proactive_governance_scale_research_v1.md X8]`.
**Re-grounded:** the tree holds much more than the shape. The file this lane skipped (E-4) carries a
thirteen-row table on exactly this subject `[T+: CGR:87-103]`, and the primitives study carries the
two-officer model, the syndics and the report `[T+: PMP:119, :138-140, :150-152]`.

- **A chain of ports, not a territory**: Istria and Dalmatia, Corfu, Modon and Coron ("the eyes of the
  Republic"), Crete, Negroponte, later Cyprus; a *bailo* at Constantinople with jurisdiction over Venetians
  there. `[M]` for the list and the *bailo*.
- **Near and far were governed differently** (added `[T+: CGR:102]`). Mainland rectors were civilians
  under "dense, fast Senate oversight"; the sea state was under a **Provveditore Generale da Mar**, a
  senior governor with civil and military authority together. Distance bought the far officer the
  combined command the near one was refused.
- **Governed by rotation from the centre.** Each place had a **rector** (duke of Candia, *bailo*, *podestà*,
  *castellan*, *provveditore*) elected in the Great Council for about two years, with councillors beside
  him, a written **commission** stating what he may and may not do, **no local marriage, land or trade**,
  and a duty to report by dispatch. Local law and local councils were left in place under him.
  `[T+: CGR:99: terms of 16, 24 or 36 months, fixed, with no self-succession; legislation "regularly
  forbade rectors from close, informal contact with their subjects"; PHS:358. The figure is the tree's
  and still a lead; the written commission and the marriage bar are not in the tree.]` The rector in
  practice was **a broker** between the Senate's demands and the subjects, using his court as the place
  of negotiation and his family's ties across the dominion `[T+: CGR:95, O'Connell]`; and a rectorship
  was a rung on a graded ladder of postings for the patrician, promotion turning on how the last term
  ended `[T+: CGR:101]`.
- **By pact, not by annexation** (added `[T+: CGR:94; PMP:508-511; GPC:195-199]`). The mainland cities
  came in by negotiated ***dedizione***: statutes, tax exemptions, guild privileges and communal
  councils "formally preserved" in exchange for loyalty and the centre's appellate supremacy. Vicenza
  kept a great council of 500, a lesser of 150 and a court that could impose death; Venice inserted its
  two rectors and left the rest. The tree's rule from it: *conquest should produce a negotiation, not a
  colour change.*
- **Audited after the fact**: travelling **syndics** (*sindici inquisitori*) heard complaints from subjects
  against rectors and could try them on return; a rector's final *relazione* was read to the Senate.
  `[T+: PMP:119: the 1566 commission charges them to bring "grandissima consolatione" to the cities and
  to audit the rectors; they travel as a visible cortège of about thirty and proclaim their arrival:
  "the inspection was theatre as much as audit"; CGR:100: the exit report "gates reassignment", and the
  syndics are a second, independent layer. PMP:150-152: the ambassador's *relazione* is one cumulative
  document that successors update.]`
- **Split authority** (the tree's X8): in a subject city the *podestà* held justice and the *capitano* the
  garrison and the purse; some verbs rose to the centre, some stayed with the local council.
  `[T+: PMP:138-140: "the governor is split into two rivalrous offices so that neither can defect
  alone"; above them the *provveditori generali*, and the Avogaria could suspend a rector's decision.]`
- **Settled as well as garrisoned** (added `[T+: CGR:103]`): Crete was colonised under a charter of 1211
  with Venetian families holding land in two grades, the greater for mounted service and the lesser for
  foot: a rooted militia of landholders under a separately rotating governor.
- **How it broke**: Crete, 1363, the **revolt of St Titus**, in which the *Venetian settlers themselves*,
  holding fiefs for military service, rose with the Greek lords against a new tax levied without their
  consent; put down with a hired army. `[M]`: the settlers' tenure is sourced above, the revolt is not
  in the tree. The mainland broke otherwise and is sourced: after the defeat of 1509 the subject cities
  opened their gates, the battle and "decades of resented rectorial administration" arriving together
  `[T+: CPS:314]`.
- **The merchant galleys (*mude*).** The state **built and owned** the great galleys in the Arsenal and
  each year **auctioned the charter** of each galley on each line (Romania and the Black Sea, Alexandria,
  Beirut, Flanders and England, Barbary) to the highest patrician bidder. The Senate fixed the sailing
  dates, the route, the freight rates, the crew and the armament; the winning *patron* had to carry any
  qualified merchant's goods at the published rate. Convoys sailed under a state captain. Posts as
  "bowmen of the quarterdeck" gave poor young nobles a free passage and a small trading allowance.
- **What that is, mechanically**: a public monopoly on the *means* (hull, schedule, protection), a
  competitive auction for the *operation*, a common-carrier rule that kept the profit open to the whole
  class, and a welfare seat for its poor. Bulk goods went by private round ship outside the system.

### 1.8 The Arsenal

`[M]`. A walled state shipyard with a standing, salaried, hereditary-leaning workforce (the *arsenalotti*;
"16,000" is the famous figure and almost certainly a peak or an exaggeration; a few thousand is safer),
standardised frames and fittings, a reserve of hulls kept in store, and the ability to fit out a galley
from stock in hours as a set piece for visitors. Run by elected patrician *Patroni* and *Provveditori* on
short terms over permanent foremen (the *proti*), the usual pairing of rotating noble and career expert.
The *arsenalotti* were also the Republic's **only trusted armed body at home**: the Doge's guard, the
guard of the Great Council in session and of the palace during an interregnum, the fire watch, with
ceremonial privileges and no vote `[T: political_hierarchy_standing.md §Venice 2.1]`.

**Corrected `[T+: CGR:91, Davis]`:** the tree does not choose between the figures; it keeps both:
"wholly state-owned, at peak employed ~16,000 workers (arsenalotti) with a stable skilled core of ~2,000
backed by surge/unskilled labor — confirmed by multiple independent sources", with standardised
production. So "a few thousand" is the core and "16,000" the surge; both are leads. The yard was fed by
**state forests** the Republic took into its own ownership on the mainland, over communal and feudal
claims, under six statutes ending in 1476 `[T+: CGR:92]`: a named supply chain from a subject province
to one works. The comparative pass kept both as mechanics: a works with **a wage liability that falls
due every season whether or not it is used**, and a levy tied to a named dependent site
`[T+: CGR:198-199]`. **Corrected `[T+: CPS:306]`:** "only trusted armed body" overstates it. In 1355 the
Doge's fellow conspirators against the patriciate were Arsenal men and craftsmen. The body the class
trusted with the palace was the one a Doge could raise against the class.

### 1.9 The ban on armed power at home

`[M]`, with `[T]` for Carmagnola. `[T+]`: *provveditori* as "civil-military overseers of frontier
territories and fleets" are `PHS:358`; the contract and its phases are `CGR:110` (§2.6); the rule that no
patrician commands on land, the pay chest, Pisani and the ban on foreign fiefs are not in the tree.

- **No patrician commands a land army.** The mainland was held by **hired foreign captains** under
  contract (Carmagnola, Gattamelata, Colleoni), with patrician ***provveditori*** attached to the camp as
  the state's commissaries: they held the pay chest, countersigned orders and reported to the Senate.
- **The captain is watched and can be killed.** Carmagnola, suspected of slack campaigning and of dealing
  with Milan, was invited to Venice to confer, arrested, tried by the Ten and beheaded in 1432 `[T:
  political_hierarchy_standing.md §Milan, routes down]`.
- **Fleet command stays inside the class but under account**: an admiral who lost was tried on his return
  (Vettor Pisani, imprisoned after Pola, released at the crowd's demand in the Chioggia crisis).
- **No private force, no foreign tie.** Nobles might not hold fiefs or titles from foreign princes, accept
  their gifts, or keep armed retinues; ambassadors surrendered gifts on return.
- **Why it held**: the class's wealth was in trade and state debt, both of which a coup would destroy.

### 1.10 The spy system

`[M]` for detail (Preto; Iordanou), `[T]` for the bench. `[T+]`: the *relazione* as a required final
report, unique to Venice, cumulative and inherited, is `PMP:150-152` (Queller); the grades of envoy
(ambassador capped at two years, extraordinary envoy, resident) and an ambassador reporting straight to
the Ten from 1480 are `PMP:154`: **the intelligence channel and the political channel could be
separated**; the sealed route against the open accusation is `PMP:471-475`; the citizen secretaries who
"drafted and often substantively conducted diplomacy that patrician ambassadors (who rotated too fast to
master a brief) merely fronted" are `PHS:362`; informers and the denunciation slots are `GM:345`. The
tree's cipher bureau is Milan's, under one long-serving secretary who survived his masters
(`CGR:112`); a Venetian cipher office stays memory-grade.

- **Three feeds**: (a) every ambassador and rector writes regular **dispatches** and reads a formal
  ***relazione*** to the Senate on return, an institutional memory in the secret chancery; (b) the Ten and
  the Inquisitors run **paid informers** and take **secret denunciations**; (c) merchants, consuls and the
  *bailo* abroad report as a duty of the class.
- **Handling**: a secret archive, career **cittadini** secretaries sworn to silence, a cipher office;
  disclosure of council business is a capital matter; patricians are forbidden to speak with foreign
  envoys outside office (Foscarini's charge) `[T: 01_venice_procedure.md §3.6]`.
- **Verification before action**: two or three spies check a denunciation before witnesses are examined;
  unsigned accusations are admitted only above a high vote threshold, and the thresholds conflict across
  sources `[T: ibid. §1.4, Gaps 4]`.
- **The cost**: the informer who lies. The system pays for accusations and tries them without the accused.

### 1.11 The ledger of the state

`[M]` (Mueller; Lane; Pezzolo), shapes only. **Still memory-grade for Venice:** the tree has no line on
the Monte, the *estimo* or the forced loan. It has the same shape elsewhere, and that is what the design
may lean on: the Spanish crown's ***juros*** and the suspensions of 1557, 1560, 1575 and 1596, where
"default isn't a terminal state but a scripted restructuring": short debt converted to long, the
bankers writing down part `[T+: CGR:130]`; the 1381 admission of new families "in exchange for war-loan
contributions" `[T+: CPS:310]`: at Venice a loan to the state bought the roll; and the lender's ruin when
the borrower is a prince `[T+: HCC:148]`.

- **Forced loans, not taxes, on the rich.** Each household was assessed (the *estimo*) and required to lend
  a percentage; the loan was entered in the **Monte** (from 1262), paid a fixed interest (5% nominal), was
  never due for repayment, and was **transferable**, so a secondary market priced the state's credit. In
  war the levies rose, interest was suspended and the price collapsed (the Chioggia war); in peace the
  state bought back.
- **What the debt did politically**: the creditors of the state *were* the electorate. A patrician's
  interest in the Republic's survival was a line in a ledger, and so was his exposure when the Senate voted
  for war.
- **Other ledgers**: the Grain Office took deposits and lent them to the state; the Procurators of San
  Marco held estates and trusts; the salt monopoly and customs were farmed or run directly; double-entry
  accounts were the trade's ordinary practice (Pacioli calls it the Venetian method, 1494).
- **The debt-bar** closes the loop: arrears to the treasury suspend political rights `[T:
  political_hierarchy_standing.md §Venice 2.6]`.

### 1.12 How it decayed, was corrupted, projected power and was resisted

- **Decay**: the roll outgrew the wealth that backed it (*barnabotti*); offices became livelihoods; votes
  were sold; the Republic ended in 1797 without a coup `[T: conflicts_power_struggles.md §Venice 3.8]`.
- **Corruption**: *broglio*; scope creep of the secret bench until the class cut it back (1582–83, 1628,
  1762) `[T: ibid. 3.6]`; the paid false informer.
- **Power at distance**: rotation, the written commission, the dispatch, the syndic, the auctioned galley
  line, the hired captain with a commissary at his elbow.
- **Resistance**: settler revolt (Crete 1363); a league of every neighbour at once (Cambrai, Agnadello
  1509, after which the mainland cities' *nobles* opened their gates and their *commoners* fought for
  Venice) `[T: ibid. 3.5]`; the Papal interdict of 1606, which failed because the local clergy obeyed the
  state `[T: 01_venice_procedure.md §3.5]`.

---

## 2. How it really worked — Medici Florence and the Italian city-state world

### 2.1 The republic the Medici ruled from behind

- **Legitimacy by guild, not blood.** The Ordinances of Justice (1293) barred named magnate families from
  office and made them collectively liable; standing came from membership of one of 21 guilds, seven major
  and fourteen minor `[T: governance_modes.md §Florence 1.1–1.2]`.
- **The Signoria**: eight priors and the Standard-Bearer of Justice, **two-month terms**, living shut in
  the palace for the term, flanked by two colleges (the Twelve and the Sixteen) whose consent was needed,
  and by *pratiche*, invited advisory sittings of leading citizens whose speeches were minuted `[T: ibid.
  1.2]`.
- **Scrutiny and the bags.** Every few years a commission voted on each eligible citizen (the *squittinio*);
  names that passed went on slips into **bags** (*borse*), one set per office; at each vacancy a name was
  **drawn** (*tratta*). A drawn name was checked against the disqualifications: the *divieto* (he or his kin
  had sat too recently), **the *specchio*** (he was in arrears with his taxes), age, absence. A man drawn
  and disqualified was "seen" (*veduto*); a man drawn and seated was *seduto*; being *veduto* for the high
  offices was itself a mark of standing a family counted `[T: ibid. 1.3; M for specchio and
  veduto/seduto]` `[T+: DPC:57: "a drawn man is *veduto* ('seen'), and he is *seduto* ('seated') only if
  he clears the *divieti* (office held too recently, a relative in office, under age, absent, in tax
  arrears)"; the bags were locked in a sacristy and their contents known to the scrutineers alone; the
  loading of a purse of loyal names dates from about 1387, before the Medici. The word *specchio* is
  not in the tree.]`
- **Outsider magistrates.** The *podestà* and the Captain of the People were foreigners hired for six
  months with their own staff, forbidden local ties, and **audited at the end of term** (the *sindacato*)
  before they were paid and released `[T: ibid. 1.7; M for sindacato]` `[T+: CGR:109, and the judgment
  on it at CGR:207: the *sindacato*'s finding of malfeasance "bills the appointing faction's Legitimacy,
  not just the podestà": **the appointer is liable for his man**, a mechanism this design lacked
  (§17.2 item 3). `GM:277` adds the failure state: the outsider was sometimes captured by whichever
  local party hired him.]`
- **The party weapon before the Medici**: the Parte Guelfa's *ammonizione*, a ban from office on suspicion,
  with no trial `[T: ibid. 1.4]`.

### 2.2 The party-and-*balìa* mechanism

How a private citizen rules a republic without changing its laws `[T: governance_modes.md §Florence 1.5;
conflicts_power_struggles.md §Florence, 1433–34; M: Rubinstein]`:

1. **A friendly Signoria is drawn** (or waited for: with two-month terms one comes round).
2. It rings the bell for a ***parlamento***: the citizens in the square, the entrances held by armed
   supporters, a yes shouted to a question read from the palace steps.
3. The parlamento grants a ***balìa***: a commission of named citizens with full powers for a fixed period.
4. The balìa **exiles the opponents** (to named places, for terms of years, with sureties), bars their kin
   from office, and orders a **new scrutiny**.
5. It appoints ***accoppiatori***, who are meant only to fill the bags after a scrutiny, and extends their
   commission so that they fill the bags of the Signoria ***a mano***: choosing the few names that go in for
   each draw. The draw still happens; the bag holds only friends.
6. The police magistracy (the Eight) is given balìa powers over political offences.
7. The emergency is renewed every five years, then made a council (the Hundred, 1458), then a life senate
   (the Seventy, 1480) `[T: governance_modes.md §Florence 1.5]`.

Cosimo held ordinary office rarely. The method needs: one sympathetic draw, control of the square for an
afternoon, and thereafter control of **who edits the list**. The tree's own synthesis says it in one line:
in all four Italian cases *"the decisive lever is who controls the list, not the nominal selection
procedure"* `[T: political_hierarchy_standing.md §The standing currency, compared]`.

### 2.3 Patronage and the *gente*

`[M]` (D. Kent; Padgett and Ansell 1993), `[T]` for the pillars. `[T+]`: the tree cites both authors
and states the finding, twice. `RTP:68-71` (Padgett and Ansell 1993 named): the method is to **"capture
the gate, not the seat"**; what makes the capture last is reach across many ladders ("multivocality");
and its failure is specific: a narrow, coherent rival cannot out-organise it but can force **one public
exposure that ties the scattered edges into a single scandal**. `RTP:452-455` (Kent and Rubinstein
named): the bias sits in whatever generates the slate, and it is **one pointer that changes hands in one
event**: the Albizzi used it to exile Cosimo in 1433 and he used the same lever on them a year later
(`CPS:252`: "whoever drew the current Signoria decided who got exiled next"). `PHS:283`: the favours
were marriage alliances, debts forgiven and dowries subsidised. The three named kinds of tie and the
marriage-against-business pattern stay memory-grade.

- **Three kinds of tie** made a following: kin (*parenti*), neighbours of the same ward (*vicini*) and
  friends (*amici*), the last meaning clients and allies bound by favours.
- **The favours were specific**: a loan, a dowry, a lower tax assessment, a name put into a bag, a letter of
  recommendation to a branch manager or a foreign court, a benefice for a son, standing surety, a marriage
  arranged. Each created a debt of gratitude that was called in as a vote, a speech in a *pratica*, or
  silence.
- **Structure, not size, was the Medici advantage**: they married into old families of *other* quarters and
  did business with new men of *their own* quarter, so their followers were tied to them and **not to each
  other**. The rival oligarchs were densely intermarried and could not act without one another. A patron at
  the only junction between groups can be read differently by each (Padgett and Ansell's "robust action").
- **Its limits**: gratitude decays; a client with two patrons chooses; the patron who must refuse loses
  more than the one who was never asked.

### 2.4 The Medici bank: partnership branches and credit

`[M]` (de Roover), shapes only. **Mostly still memory-grade:** the tree holds no account of the bank's
partnership form, the bill of exchange, the discretionary deposit, the papal depositary or the alum
farm. What it holds: that the bank was the second pillar of the regime, financing "allies' dowries,
debts, and tax (*catasto*) burdens, buying loyalty without any formal office" `[T+: GM:269]`; that exile
"did not touch the Medici bank's international correspondent network or its Florentine debtors", which
is why exile failed `[T+: CPS:252]`; an archived design note that branch managers ran "practically an
independent fiefdom … on personal relationships" `[T+: .designs/systems/npcs/reference/npc_roster_v30_infill.md:62,
intent only]`; and, for the failure, the general case with other names: Edward III's default broke the
Peruzzi in 1343 and the Bardi in 1346, "Creditor Collapse" when the exposure is concentrated
`[T+: HCC:148]`; the Fugger loan for the imperial election bought mining rights and a climbing claim on
office `[T+: HCC:161]`; and the Fugger house kept its factors honest by **a standing, scheduled audit of
its own branches** `[T+: PGS:76]`, which is this section's "general manager who stopped reading the
branch books", stated as an institution.

- **A partnership of partnerships.** The family and one or two senior partners held the capital of a
  parent firm in Florence; **each branch** (Rome, Venice, Milan, Geneva then Lyon, Bruges, London, Avignon,
  Pisa) **was its own partnership** between the parent and a **branch manager**, who put in a small share of
  the capital and took a much larger share of the profit, was forbidden to lend to princes or gamble, had to
  send his books to Florence yearly, and could be dismissed at the contract's renewal. The loss of one
  branch did not in law sink the others.
- **The instrument was the bill of exchange.** Money advanced in one city in one currency, repayable in
  another city in another currency after a customary delay; the lender's gain sat in the rate. It moved
  funds without shipping coin and it was credit that the Church's usury rule did not reach. A bill drawn
  and redrawn with no trade behind it (*dry exchange*) was a plain loan in disguise.
- **Deposits at discretion.** Great men, cardinals above all, lodged money with the bank and received a
  yearly "gift" at the bank's discretion; in bad years, no gift. The depositor's name was often kept out of
  the books.
- **The Rome branch followed the Curia** and was the engine: as **Depositary General** it received the
  papal revenues from all Christendom through the other branches and advanced the Pope money against them;
  bishops paid their appointment fees through it, and **a prelate who did not pay his banker could be
  excommunicated for it**. From 1466 the bank farmed the papal **alum** monopoly, with the Pope forbidding
  the import of Turkish alum on pain of spiritual penalties.
- **What a branch was politically**: an intelligence post, an embassy the state did not pay for, and a
  means of obliging foreign princes and local grandees.
- **How it failed**: loans to princes who could not be dunned (the London branch to Edward IV, Bruges under
  Portinari to Charles the Bold); a general manager who stopped reading the branch books; a head of the
  house who used the bank for the state's ends; the loss of the papal account in 1478; dipping into public
  funds; and, in 1494, expulsion and confiscation. A house that rules by credit dies of bad debts.

### 2.5 Tax and sumptuary law as weapons

- **The *catasto* (1427)**: every household declares its property and debts; a rate is applied after fixed
  deductions. It replaced assessment by neighbourhood committees, which had been openly partisan; under the
  Medici the assessment again became a way to ruin an enemy or spare a friend `[M]`.
- **Forced loans and the Monte**: as at Venice, the rich lent under compulsion and were credited in a funded
  debt whose shares traded; a **dowry fund** (the *Monte delle Doti*, 1425) let fathers buy a future dowry
  from the state, tying every family with daughters to the state's solvency `[M]`.
- **The tax-debtor's bar (*specchio*)** removed a man from eligibility at the moment his name was drawn
  (§2.1): a fiscal fact with a constitutional effect.
- **Sumptuary law**: statutes limiting dress, feasts, weddings and funerals, enforced by a magistracy with
  fines and by denunciation; they license display by rank, raise revenue by fine or dispensation, and give
  a preacher's party a legal instrument (§2.8) `[M]`. **Corrected in placement `[T+: PGS:121]`:** the
  instance the tree holds is **Venice's** sumptuary magistracy, a standing office in a named city,
  tightened from 1476 to 1562, drawing fines and petitions for exemption from the wealthy. The Florentine
  use stays memory-grade.

### 2.6 The condottieri

`[M]` (Mallett), `[T]` for Sforza and Carmagnola. `[T+]`: the contract is in the tree. `CGR:110`: a
captain contracted "for a specified count of 'lances' at a set stipend, structured in phases", a
*ferma* and an *aspetto*; the judgment on it (`CGR:208`; compendium `tier3_proposal_status_closure.md:103`)
names the life cycle ***Ferma → Aspetto → Lapsed***: bound service; then **a reserve at reduced pay in
which the captain may be poached**; then lapse, with a period in which he may not turn on the late
employer. **This corrects the sense of the first bullet below:** the second phase is not only the
employer's option, it is the window in which a rival's offer is lawful. The structural conflict is
`research/pre_firearms_formations/05_late_med_renaissance_europe.md:480-484` ("a condottiere's company is
his livelihood"); the army as a bought instrument paid whether or not it prospers is `FASE:192-196`
(Redlich); arrears turning the men on their own host is `HCC:67` (Antwerp, 1576: unpaid three seasons,
they sacked the town that lodged them, "and every loyalist settlement that hears" trusted garrisons
less); Sforza's marriage claim, which his employer twice tried to dissolve, is `RTP:340-343`; the general
who feeds his army from the land and is brought down through his own sub-commanders is `RTP:345-348`.
The muster inspection and the advance stay memory-grade.

- **The *condotta***: a written contract between a state and a captain for a stated number of **lances**
  (a unit of three: man-at-arms, squire, page) and foot, for a **fixed term** (*ferma*) and an **option
  term** at the employer's choice (*di rispetto*), with an advance (*prestanza*), a monthly rate, rules for
  booty and ransoms, and a clause against serving the employer's enemies for a period after.
- **Retainer in peace** (*in aspetto*): half pay to stay available.
- **The muster** (*mostra*): the state's inspectors count and record men, horses and arms; missing men are
  fined off the pay; **civilian commissaries** travel with the army.
- **The structural conflict**: the captain's capital is his company, so he avoids destroying it; the
  employer wants decisive battle and pays late. Arrears, an expiring contract and a better offer are the
  three roads to defection; a captain owed money takes a town as security.
- **The ladder**: contract → captain-general → a fief or a city in vicariate → a title. **Francesco Sforza**
  was hired by the Ambrosian Republic, turned its army on it and became Duke (1450) `[T:
  governance_modes.md §Milan]`. **Carmagnola** was beheaded by his employer (1432). The employer's two
  answers were Venice's (watch, pay regularly, kill on suspicion) and Florence's (short contracts, many
  captains, chronic arrears, and Machiavelli's contempt).

### 2.7 The Pazzi conspiracy: the failure mode of informal rule

`[T: conflicts_power_struggles.md §Pazzi; political_hierarchy_standing.md §Florence, routes down]`, with `[M]`.

- **The parties**: a rival banking house (the Pazzi, who had just taken the papal account); the Pope's
  nephew, who wanted a state; an archbishop kept out of his see by the regime; a hired captain's troops
  waiting on the border. **Corrected `[T+: CPS:257]`:** the tree gives the Pope's motive as fury "over
  Lorenzo's blocking of a Pazzi-financed papal land purchase at Imola": a rival house's **loan to a
  third power, refused passage by the man who ruled from behind**. The papal account's transfer is
  memory-grade. The tree's reading of the sequel is this section's: reprisals "ferocious and
  extra-legal", then the Seventy under "the crisis's political cover".
- **Why assassination**: a man who holds no office cannot be voted out, impeached or left out of the next
  draw. The tree's heading is exact: *"informal power has no institutional recourse, so rivals go outside
  the system entirely."*
- **26 April 1478**, at High Mass: Giuliano killed, Lorenzo wounded and away. The archbishop goes to seize
  the palace; the Standard-Bearer arrests him. Jacopo de' Pazzi rides through the streets calling *"People
  and liberty"*; **no one rises**; the crowd answers with the Medici cry. The archbishop is hanged from the
  palace window in his robes the same day; some eighty die.
- **The second act is institutional**: hanging an archbishop brings **excommunication of Lorenzo, an
  interdict on Florence and a papal–Neapolitan war**; Lorenzo sails to Naples and makes a personal peace
  with the King (1479–80); on return he creates the Seventy. **A failed strike converts informal rule into
  chartered rule.**

### 2.8 Savonarola: the other failure mode

`[T: governance_modes.md §Florence 1.6; conflicts_power_struggles.md §Savonarola]`, with `[M]`.

- **No seat.** A preacher whose authority is prophecy that came true (the French invasion, 1494). After
  the Medici fall he shapes a **Great Council** on the Venetian model and never sits in it.
- **Instruments**: the pulpit; a party (the *Frateschi*, mocked as *Piagnoni*) that wins draws and
  elections; bands of boys enforcing the sumptuary laws door to door; the bonfires of vanities.
- **The opposition has three roots**: the old oligarchs, the young bloods (*Compagnacci*), and Rome.
- **The mechanism of the fall**: excommunication (1497), which he defies; then the **threat of an interdict
  on the city**, which exposes every Florentine merchant abroad to seizure of his goods and so turns the
  merchants; a challenged **ordeal by fire** that collapses into a wrangle and a rainstorm before a crowd
  that had come for a miracle; and a hostile Signoria **drawn by lot** at the turn of the term. Arrest,
  torture, the gallows and the fire, 23 May 1498.
- **The shape**: charismatic standing with no office is high leverage and has no floor; it is stripped by
  the one authority it never held (the sacramental one) acting through the interest it never served (the
  merchants' goods abroad).
- **Corrected in mechanism `[T+: CPS:277; RTP:539-542]`:** the tree's account has **two independent
  blows, and both were needed**: the excommunication of May 1497, which struck the one pillar he could
  not route round, and the collapsed ordeal of 7 April 1498, which destroyed his standing with the crowd
  "in a single afternoon"; only then did a Signoria "he had never formally controlled" arrest him. The
  interdict's threat to merchants' goods and the hostile draw are this lane's memory and stay marked.
  For the design the tree's version is the better one: two draws by two different actors, neither
  sufficient alone, and no rule that the second follows the first.

### 2.9 The wider city-state pattern

- **Milan**: lordship by seizure, legitimated by an imperial vicariate, converted to a hereditary duchy
  **by purchase** (1395); extinct line → a republic with no army → its own hired captain `[T:
  governance_modes.md §Milan]`.
- **Genoa**: a neutral head with no force of his own among armed clan-federations (*alberghi*); chronic
  deposition; **repeated voluntary submission to a foreign lord** as a way out; and the **Casa di San
  Giorgio**, a corporation of the state's creditors that took over revenues and then territories in
  satisfaction of the debt `[T: governance_modes.md §Genoa; M for San Giorgio]` `[T+: the submissions
  are GM:290-291 and CPS:267-268 (to Milan 1421 to 1435, to France 1396 to 1409 and 1458 to 1461), read
  there as "a legitimate … de-escalation move available to a collapsing Territory"; the fixed roll of 28
  *alberghi* of 1528 is PHS:310. San Giorgio survives in the tree only as a trace: the verifier's note
  at GM:248 begins "(4) Casa di San Giorgio — REMOVE Chios from its administered colonie[s]", and the
  corrected body does not mention it. A lead, not a source.]`
- **1494**: none of it survives the arrival of a consolidated kingdom `[T: governance_modes.md §5]`.

---

## 3. How it really worked — the Hanse and the merchant guild

`[M]` (Dollinger; Greif, Milgrom and Weingast 1994; Ogilvie for the sceptical reading); the tree's
treatment is the Kontor as an organisation proposal `[T: research/proactive_governance_scale_research_v1.md O7]`.
`[T+]`: the tree's treatment is wider than that one row. **The Kontor** `PGS:78`: a self-governing
enclave inside a host settlement with "own treasury/law/seal", its alderman elected (liked locally,
weakly controlled) or appointed (the reverse), and **the host's governor "literally loses Hold Court
jurisdiction" over its members**; `PGS:23` frames the whole kind: a body of members with branches
"physically sitting inside settlements the organization has no sovereignty over", whose standing
problems are branch drift, a factor who skims, and friction with the host. **Withdrawal** `FASE:119`,
`:236-240`: "a merchant corporation with no army coerced territorial princes routinely"; the dates the
tree gives for Bruges are **1358 and 1451 to 1457** (the 1388 and the Norwegian 1284 in the bullet below
are this lane's memory and stay leads); the act is private, "no vote, no Mandate minimum, which is
exactly its historical character". **How it ended** `HCC:55` (Novgorod closed the Kontor in 1494, once
the Hanse's hinterland had weakened of itself), `HCC:160` (the Steelyard's privileges revoked in 1598 on
a rival domestic guild's petition, there being no reciprocal privilege abroad). **Rule without conquest**
`research/historical/precedents_warfare.md:147`: cities that wanted the network accepted its commercial
law. **The staple** `PGS:123` (Lübeck: granted once by the superior, administered by the town) and
**portability** `PGS:84` (the Merchant Adventurers: threatening to carry the privilege to a rival host
is the leverage). **The local guild** `CGR:97` (Venetian guilds elect a steward, a treasurer, assessors,
syndics and a scribe, and rule apprenticeship, quality and discipline, but **no guild statute takes
force without one outside magistracy's assent**); `CGR:116` (the wool guild held import, allocation to
some 300 workshops, prices and wages for a workforce that had no place in it); `CGR:117` (**the
Mercanzia: the guilds jointly paid for their own merchant court with its own enforcement**); `PGS:77`
(consuls drawn by lot for four months, which throttles any one leader and makes his precedents easy to
reverse); `CGR:129` (Spanish guilds write their rules, the town or crown sanctions them); and the
archived Guild ladder to Comptroller with entry by guarantors and mastership by purchase
(`.designs/systems/factions/reference/faction_politics_v30.md:566-585`, intent only). The diet, the
thirds, bound envoys, the war levy, Stralsund, the expulsion of a member town and the
commitment-device argument are not in the tree and stay memory-grade.

- **A league with no state.** No seal of its own, no standing treasury, no fleet, no permanent officers.
  A **diet** (*Hansetag*) met irregularly, usually at Lübeck; towns sent envoys **bound by instructions**;
  its recesses bound a town only so far as the town chose to carry them out. Regional thirds held their own
  diets.
- **Its property was privilege abroad.** The Hanse existed to obtain and defend **charters from foreign
  rulers**: lower customs, its own law among its merchants, a walled compound.
- **The *Kontor***: Bruges, London (the Steelyard), Bergen, Novgorod (the Peterhof). A corporation of the
  visiting merchants with elected aldermen, its own statutes and court, a common chest, and a rule of life
  (residence inside the walls, no marriage with locals, curfew, in Bergen and Novgorod a near-monastic
  discipline for apprentices). It negotiated with the host ruler as one body.
- **The weapon was withdrawal.** A ruler who broke the charter faced the **removal of the Kontor and a
  blockade** by every member (Bruges 1358 and 1388; Norway 1284). A town that broke the boycott, or defied
  the diet, was **put out of the Hanse** (*Verhansung*): no member might trade with its merchants.
- **Why this works** (Greif, Milgrom and Weingast): a ruler's promise to protect foreign merchants is not
  credible when each merchant is small, because he can rob a few and the rest still come. A guild that can
  make **all** of them leave makes the promise worth keeping. The guild is a **commitment device for the
  ruler**, not only a cartel. (Ogilvie's caution: it was a cartel as well, and excluded outsiders by the
  same means.)
- **War when it had to**: a levy on trade (*Pfundzoll*) paid for a fleet under the Confederation of
  Cologne (1367); the Peace of Stralsund (1370) gave the towns fortresses, revenues and a **say in the
  Danish succession**.
- **Decay**: territorial princes absorbed the towns; Dutch and English shippers undercut; members defected
  one by one because the league could not compel.
- **The local guild** (the Florentine *Arte*, any craft guild): a roll of masters; entry by apprenticeship,
  fee and masterpiece; elected consuls on short terms; statutes over quality, price and hours; a court for
  members' disputes; a chest for burials and widows; a militia company; and, in guild republics, **the
  gate to political eligibility** (§2.1).

---

## 4. What the tree already holds (read at the owner; code is the mechanism)

### 4.1 Primitives that exist and that this family reuses

| primitive (brief's word) | owner in the tree | state, verified this session |
|---|---|---|
| **seat** | `engine/season/offices.yaml` rows → `state/carriers.py::Office` (`rung`, `body`, `faction`, `remit_acts`, `conferral`, `revocation`, `binds`, `upkeep`) | 34 seats at `build_realm(0)`: 18 `appointed`, 8 `elected`, 1 `inheritance`, 7 null (probe E-1). No seat on a `hearth` or `community` rung, though the title ladder is total down to *Family Head: hearth* (`offices.yaml: titles.domains`) |
| **body** | `rosters.yaml: office_bodies` (`faction`, `function`) | 19 rows; `Guild` → Guilds; `Inner Council` → Hafenmark; no Schoenland body |
| **procedure** | `engine/season/arrangements.yaml`, thirteen keys (`disposal`, `quorum`, `floor`, `records_dissent`, `order`, `proofs`, `disposes`, `appeal_basis`, `interposed`, …) | nine rows; `disposal: declared` with `quorum` is live on one row (CR-34). `01_venice_procedure.md` already tabulates nine Venetian procedures in these keys |
| **term** | `state/carriers.py::Term` on `Tenure` (`matures_at`, `declared_by`), matured at MATTER (`T-n`); a seat-row `term:` is FA-P3's (`proposals/06_FA_seat_terms_and_turnover.md`), which rows carry it FA-B3's | 0 termed live tenures at build (probe E-1); the mechanism is proposed, not landed |
| **obligation / patron-client edge** | Tenure kind `oblige : Person → Office`, opened by the joiner's own `oblige`, termed (`oblige_term` 4), renewed by the seat's `transfer` of `upkeep` to the obligee's home rung (`_renewals`, `may_renew`); read by `purview_reaches`' oblige clause (a sworn holder brings his ground) and `establishment_of` | 4 live `oblige` edges at build, all vassal oaths to `off_king` or the Restoration seat (probe E-1) |
| **instrument / document** | `Record` kinds `dispensation [terms, to, at]`, `petition`, `works`, `faction_sheet`, `cover`, `challenge`, `order_of_battle`, `army` (`rosters.yaml: record_kinds`); one mint (`_mint_document`); `Record.stages` matured at MATTER; held, given, seized, forged, concealed | 2 Records at build, both `works` |
| **covenant** | verb `covenant` (`remit:issue` through a seat; mints a `dispensation` whose `terms` is an uttered Proposition; in force by both parties' `commit`) | readers deferred; 0 of 41 executed (plan `v11_part2:23`, read at the line, not re-run) |
| **claim / deed** | `Claim` ledgers per person; deed kinds partitioned `dominance` / `prestige` (`rosters.yaml: standing_routes`), read by `world_q.reception` | exists; no ledger ranks houses |
| **treasury** | `Rung.stores` at the seat's rung (`Tenure.seat_rung`), moved by `transfer`, `exchange`, `requisition` | **empty everywhere at build** (probe E-1: stores total `{}`); `coin` is a registered matter kind "produced by no site and held by" nobody (`data/fixtures.py:613-632`) |
| **jurisdiction** | `purview_reaches` (containment of the seat's rung, plus one sworn edge deep); `judging_set` (`scope_rung`) | exists |
| **sanction** | Tenure kinds `ban`, `detain` (opened by `determine`, `revoke`, `arrest`; closed by `pardon`); `ban` bars seating (`_eff_confer`) and service (`_req_oblige`) | exists; FA-P3 scopes a ban to the banning seat's purview |
| **the draw** | `state/ids.py::draw_factory` (`draw(subject_id, purpose)`); contested acts through `social_contest.roll` with degree-keyed writes; obstacle as difficulty plus named terms (`proposals/05_SC_obstacle_difficulty_and_modifiers_B.md`, roster `obstacle_terms`) | exists; the term roster is proposed |
| **election** | planned, not built: CR-35 (an `elected` seat filled by its faction's bench through `determine`), CR-36 (nominate-then-confirm, basis `nominated`, Record kind `resolution`), CR-37 (deposition) (`workplans/valoria_master_workplan_v11_part12.md:140-141`) | no election executes today; all 8 `elected` seats are fillable only by `confer` |
| **debt** | **designed and deferred**: #453 K-14, "a Record kind with an `amount` key, minted by `covenant`", with "`seize` on a lapse" as its reader (`proposals/2026-10-03-verb-coverage-and-gap-fill.md:1478`, `:2685-2693`, `:4495`); `rosters.yaml:2427` reserves `kind` and `amount` operands for "the deferred `debt`" | absent |

### 4.2 Two rulings that bound the design

- **D-5 (Jordan, 2026-09-06, "second-person lever stays refused").** *"No creditor verb, no `call_in`, no
  obligee-side closer on an obligation exists or will"* (`state/gate.py:1415-1417`; #453 §8.3). An
  obligation is an edge its **subject** owns and discharges. Every credit, patronage and contract design
  below is built on the debtor's, client's or contractor's own edge, and the other party's only powers are
  the ordinary ones: ask, sue, tell, refuse the next favour. This is also how it was: a Florentine banker
  had no lever on a king.
- **We do not do deterministic (Jordan, 2026-11-12; `AUDIT_BRIEF.md` "Standing rule").** Every outcome that
  could go either way for the people in the fiction goes by a draw with a graded, recoverable result.
  §6.2 states, for each procedure of this family, where the draw is, what sets the odds and what each band
  does. Arithmetic that is bookkeeping (a term maturing, stores conserved, a count of ballots already
  drawn) and eligibility (who may stand) stay rules.

### 4.3 Where the family sits in the world

No polity is imported. Three places in the world already have the shape:

| historical family | where it lives in Valoria | basis in the tree |
|---|---|---|
| the Venetian constitution, the galley lines, the Arsenal, the secret bench, the state ledger | **Schoenland**, "a neutral offshore trade nation" and island republic that trades with both Altonia and Valoria at war or not, arms included (`canon/03_canonical_timeline.md` §Schoenland; ED-IN-0356; geography `T16`, "Island Republic"); a `foreign_factions` member with **no seat authored** and no `foreign_cast` row | M-ABROAD (`audits/12_ARCS_adjudication.md` §4 rank 13): a power beyond the map must be persons in seats; ARC-25, NPC-090 |
| the guild republic, the Signoria, scrutiny and the bags, the *balìa* | **Hafenmark's communes and its council** ("Hafenmark retains parliamentary traditions", timeline §The Settlement; `off_commune_rep_hm`, `elected`; the faction's lean to precedent and procedure) under a Duchess who "IS the institution" | Tilly's capital-intensive type is already read onto Hafenmark (`research/fa_se_historical_precedent_research_v1.md:95`) |
| the Hanse, the guild, the banking house | **the Guilds**: a league across territories, "a rotating Guildmaster Council — no single leader", burgher status as the gate to political participation (`office_bodies: Guild`), headless by design (FA-B3); the house is **Feldhaus's** (NPC-007, Guild Comptroller, who in ARC-15 funds both sides of a war) | ARC-08, ARC-15, NPC-007, NPC-084, NPC-085 |

### 4.4 Jordan's fixed points, located and reconciled

*"Current kingdom royalty is because of nobility by deed/achievement"*; *"royalty by noble conquest, i.e.
the first king had the greatest accomplishment in the secession war, followed by the first Duke of
Hafenmark and the first Duke of Varfell."*

- **Where the tree agrees.** `canon/03_canonical_timeline.md:78-92`: the first Almqvist held "no
  pre-existing royal claim … authority is entirely earned through wartime deeds"; "the Baralta family's
  ducal status was earned through wartime deeds"; the deed-presumption passes to heirs and is
  **rebuttable**; Almud "has not personally earned the deed-claim". `rosters.yaml: standing_routes`
  partitions deed kinds and `world_q.reception` reads them.
- **Disagreements, named and not resolved here** (Jordan's word governs the world; the code governs the
  engine; the crown and synthesis lanes own the repair):
  1. The timeline says the coalition was "primarily northern" and speaks of "the south's exclusion from
     the war coalition's leadership" (`:76`, `:96`). Jordan's order gives the first Duke of Varfell the
     third-greatest accomplishment of the war. Both can stand only if he accomplished much without being
     admitted to the leadership; the timeline does not say so.
  2. `offices.yaml: off_duke_varfell` is `conferral: elected` ("first among the Jarls, not a monarch"),
     and FA-B3 keeps it a life seat removed by the Jarls. A ducal *house* founded by conquest whose
     standing passes to heirs is a different fact from an elective first-among-equals seat; whether the
     present Duke is of the first Duke's line is not stated anywhere I opened `[UNVERIFIED]`.
  3. `off_duchess_hafenmark` has `conferral: null` and no `successions` row: the engine has no way to
     fill the second house's seat at all, by deed or by blood.
  4. **Nothing in code ranks accomplishment.** Deeds are claims persons hold; no query orders houses.
- **What this family adds to the reckoning** (§5.3): in a republic a deed does not make rank until **a body
  certifies it**. Venice did exactly this in 1381, admitting thirty families to the Great Council for
  service in the Chioggia war `[T: political_hierarchy_standing.md §Venice 2.5]`, and sold the same
  admission in 1646. The play-facing form is enrolment on a roll by a drawn ballot in which the deed is
  **evidence** (§6.1 part 2), so the same act serves a merchant's son, a war hero and a purchaser, and an
  heir must be enrolled in his own right with his ancestor's deed as his best exhibit.

---

## 5. Adaptation to Valoria: what is kept, what is changed, and why

### 5.1 Kept (because the mechanism *is* the institution)

1. **Rotation with a cooling-off and an audit at exit.** Short terms, no immediate re-election, a routine
   hearing on the outgoing holder. This is what makes a republic generate turnover and accusation with no
   player. (FA-P3/B3's term; this lane's `cooling_off` and `audit_at_exit`.)
2. **The roll, and capture at the roll.** Eligibility for a body's seats is membership of a list a named
   seat keeps. The decisive act is editing the list, and that act belongs to a person.
3. **Lot, then ballot.** A draw among the enrolled chooses who nominates (Venice) or who serves (Florence);
   a ballot confirms. Lot breaks arrangements; ballot keeps judgment.
4. **Secret suffrage as a rule of the room.** A sealed ballot weakens every tie that depends on the
   patron seeing the vote. One existing arrangement key carries it.
5. **Proposer is not disposer.** A college drafts; a larger body, which cannot initiate, votes on a menu;
   a legality officer may suspend.
6. **Debt as the debtor's own undertaking, evidenced by a document the creditor holds, transferable, with
   the gain hidden in the amount, the kind and the place.** No rate; no creditor lever (D-5).
7. **The house.** A family firm is a place with a head, a chest and sworn dependants; a branch is another
   such place whose manager is sworn to the head.
8. **Rule from behind.** A person with no seat who holds the debts and oaths of those with seats.
9. **The hired captain with a commissary at his elbow**, and his three roads to defection.
10. **Withdrawal as the league's weapon**, and the charter as what it defends.
11. **Self-correction at a price**: a secrecy-optimised bench that convicts on a liar's word and must
    publish its own error.

### 5.2 Changed, and why

| historical feature | change | reason |
|---|---|---|
| Nine alternations of lot and election for the Doge | **one** lot stage and one ballot stage | One alternation carries the property (a coalition must hold the bag *and* the room). Eight more add nothing a player can perceive or an instrument can show (NERS-E as a ratio; cut test §6.3) |
| Closed hereditary patriciate (*Libro d'Oro*) | the roll is **by warrant**, not by blood; an heir is enrolled in his own right, with his house's deeds as evidence | Jordan's fixed point: rank is by deed and the presumption is rebuttable. A blood-closed roll would be a second nobility system (the brief forbids it) and contradicts P-level canon on earned standing |
| Profit-sharing commenda (3/4 : 1/4) | the **sea-loan form**: a fixed amount owed, in a stated kind at a stated place, whose non-payment after a loss by force is a defence in the suit | The engine has stores at rungs and no per-venture account; a profit ratio needs a new carrier that nothing else reads. The sea loan is the commenda's own predecessor and keeps capital, labour, liquidation on return and the account as enforcement |
| Ships, convoys, the Arsenal's hulls | a galley **line** is a termed seat with a charter over a foreign market; the Arsenal is a works site with a sworn establishment | "Naval affairs [NO MECHANICS]" is canon's own flag (`office_bodies: Lions' Helm`). The institution's content is the *auctioned right to operate a public means*, which a seat and a charter carry; hulls wait for a naval design |
| Coin | every instrument is denominated by `kind`, any registered matter kind | Coin has no producer and no holder in the built world (§4.1). Grain against the harvest is credit's commonest historical form. Minting is the SE lane's (§13 dependency) |
| The interdict on a merchant city, excommunication for debt | imported from the Church lane as a `ban` whose bench is a Church seat; this lane supplies what it bites on (goods abroad, the debt-bar) | one sanction, one carrier |
| Assassination as *the* answer to informal rule | one option among the ordinary verbs, each link a draw | no scripted outcome; a Pazzi plot must be able to fail in the square as the real one did |
| Usury doctrine | **derived**, not a rule: a debt whose `amount` exceeds the principal advanced *in the same kind at the same place* is a fact an inquiry can find and a Church bench can try | the bill of exchange then works for the reason it worked: a different kind and place leave nothing to compare |

### 5.3 Legitimacy and rank by deed, in a republic and a house

- **What counts as a deed**: any deed kind a person holds a claim of (`data/verbs.py::DEED_KINDS`),
  prestige or dominance route. For this family the telling ones are a debt met, a charter won, a line
  operated, an office served out and audited clean, a town supplied in famine, a war financed.
- **Who certifies it**: the keeper of a roll, by putting the name to the body's ballot. The deed enters the
  ballot as the `evidence` term (cited claims), never as an entitlement.
- **What it costs to claim**: standing for enrolment exposes the candidate to the roll's bars (arrears, a
  live ban) and to rebuttal by a rival's contrary claim (`05_SC_evidence_and_rebuttal_B.md`).
- **How it passes**: it does not pass by itself. An heir holds his ancestor's deed as a told claim (weaker
  than a witnessed one, and fading: `01_CORE_claim_fade_as_read.md`), and is enrolled or not on that and
  his own. This is canon's rebuttable presumption, with a mechanism.
- **How a rival's deed unseats it**: at the next scrutiny or the next election, by the same ballot. In a
  rotating body that is every few seasons, with no special procedure.
- **Purchase** is composed, not a basis: a `transfer` to the roll-keeper's treasury, then his warrant
  (#453 row 38's ruling for a bribe: "carried composed, never converted"). Nothing binds the seller. An
  inquiry can reconstruct the pair, which is what makes venality and simony *findable*.

---

## 6. The play-facing model

### 6.1 Five parts, each on an existing owner

The whole family is five reusable parts. Each is stated as: what a person does, what is written, who
reads it. Exact edits are in the proposals named.

**Part 1 — The ask, and the `obligation` term** (`proposals/15_INSTITUTIONS_VENICE_A_obligation_and_the_ask.md`).
One contested roll form covers every case in which one person asks another to do what he owes: a patron
calling a favour, a canvasser asking a vote, a creditor presenting a bond, a league ordering a boycott, an
employer holding a captain to his contract, a centre holding a rector to his commission. The act is an
existing verb (`petition`, `argue`, `speak`, `issue`); the roll is `social_contest.roll`; the obstacle is
SC's form, with **one new term in the roster `obstacle_terms`: `obligation`**, favourable when the one
asked holds a live edge toward the asker (an `oblige` to a seat the asker holds, a `commit` to a
Proposition whose instrument the asker holds), hostile when he holds one toward the asker's opponent. The
term is **scaled to zero where the room does not record how each member acted** (`records_dissent:
false`): a tie that cannot be checked cannot be collected. A good patron still loses some asks; a stranger
still wins some.

**Part 2 — The roll** (`…_C_roll_lot_ballot.md`). A roll is the establishment of a seat (the persons with a
live `oblige` to it, `establishment_of`). A second `binds_bases` member, `members_by_warrant`, admits a
joiner only if he holds a `dispensation` from that seat naming him. The keeper edits the list by `issue`
(a warrant) and by letting terms lapse unrenewed (D-5's own expulsion rule: "the seat withholding
renewal"). A seat row may name `eligible_from: <seat id>`: only persons on that roll may be seated in it.
Enrolment where the body must agree is a ballot (part 3) on the candidate, with his deeds as evidence.

**Part 3 — Lot and ballot** (`…_C_roll_lot_ballot.md`). A fifth `conferral_bases` member, `lot`: the seat
is filled by `confer` through the presiding seat, and the conferee is **drawn** among the eligible on the
roll by the one draw owner; a drawn name that is barred is "seen, not seated", deposits that as a claim,
and the draw repeats. The presiding officer chooses *when*; the bag chooses *who*. A **ballot** is
`determine` under an arrangement with `disposal: declared`: each bench member's ballot is a roll at the
sitting (for, doubtful, against), and the count of drawn ballots against the row's `quorum` and majority
gives the matter's band. Venice's election is two seats: a one-season nominating seat filled by `lot`, and
the office filled by CR-36's nominate-then-confirm with a drawn ballot. Florence's is one seat filled by
`lot` from a roll kept by warrant.

**Part 4 — The debt** (`…_B_debt_instrument.md`). K-14 un-deferred as designed: a Record kind `debt:
[terms, to, kind, amount, at]`, minted by `covenant`. The **debtor** is whoever holds a live `commit` to
its `terms`; the **creditor** is whoever holds the Record. Discharge is the debtor's `transfer` of `kind`
to `at`. At the last stage's maturity an unmet debt emits `debt.lapsed`. The creditor's recourse is the
reckoning (part 1's ask, with `obligation` in his favour), a suit before a bench (a `debt_suit`
arrangement row whose disposal by band is a new stage, an `oblige`, a `ban` or a `detain`), a warranted
distraint by the bench's officer, telling others, and giving the bond away. Handing the bond to the debtor
cancels it.

**Part 5 — The seat held at distance, and the house** (`…_D_houses_charters_and_content.md`). No new
carrier. A **house** (firm, bank, Kontor, guild chapter, counting-house) is a `hearth` rung with a head
seat (title *Family Head*, already on the ladder), a chest (`Rung.stores`) and an establishment (`oblige`
with `upkeep`). A **branch** is another such rung whose manager is sworn to the head; the head's purview
then reaches it by the oblige clause, one edge deep, which is the partnership-of-partnerships exactly (a
branch's own dependants are not the head's). A **rector** is an appointed, termed seat on a subject
settlement's rung with a commission (a `dispensation`), `cooling_off`, and `audit_at_exit`. A **charter**
is a `dispensation` whose `terms` names a market rung; holding one is a favourable term on the rate roll
of an `exchange` at that market, and trading without one is attempted at worse odds, never refused.

### 6.2 Where the draw is (the standing rule, applied to every procedure of this family)

| outcome | the act and who rolls | what sets the odds (obstacle terms; pool is the actor's capability for the verb) | bands (graded, recoverable) |
|---|---|---|---|
| **an election by lot** | the presiding seat's `confer` on a `lot` seat; the draw owner picks the name | the composition of the roll (who was enrolled, who lapsed, who is barred); uniform among the eligible | a name seated; or a barred name "seen" and the draw repeated; an empty bag leaves the seat vacant to the next sitting |
| **a ballot** (election, enrolment, a senate's decree, a threshold vote to take up a denunciation) | `determine` under a `declared` row; **one roll per bench member** | per member: `regard` for the candidate or proposer, `obligation` (zero under a sealed ballot), `evidence` (deeds and proofs cited, less rebuttals standing), `standard` (the row's), `capability` rows for the venue, the rival's `opposition` | matter band from the count: Overwhelming (two thirds: carried with a mandate, a prestige deed for the proposer), Success (more than half: carried), Partial (no majority: lowest option dropped, matter stays on the docket for the next sitting), Failure (rejected: the proposer may not bring it again this term) |
| **canvassing a vote** (*broglio*) | the canvasser's `argue` at one elector | `regard`, `obligation`, the elector's rival ties, `stakes` | Overwhelming: he commits and speaks for it; Success: he commits; Partial: he is doubtful (no commit, a lean); Failure: he commits against and may tell |
| **a favour called** | the patron's `petition` to the client | `obligation` (a live `oblige`, how lately renewed), `regard`, `stakes` of the thing asked, publicity of the room | Overwhelming: done, and he brings another; Success: done; Partial: the least he can (an abstention, a delay); Failure: refused; a public refusal is a deed against the patron |
| **a loan granted** | the borrower's `petition` to the lender | the lender's `regard`, `evidence` (a held claim that the borrower met or failed a debt), `stakes` by amount, a surety's `obligation` | Overwhelming: the full sum on the easiest terms; Success: the full sum; Partial: part, or a surety demanded; Failure: refused |
| **a loan repaid** (the reckoning) | at a stage's maturity the creditor's (or his factor's) `petition` to the debtor, the bond cited | `obligation` (the debtor's live `commit`), `evidence` (the bond; a forgery's quality is the `subject` term against it), `regard`, `stakes` by the amount against the debtor's stores, the room | Overwhelming: paid in full, standing unhurt; Success: paid in full; Partial: part paid and a new stage wound (an extension); Failure: refused, and `debt.lapsed` follows at the clock. What is paid can never exceed what the debtor's rung holds (arithmetic) |
| **a suit for debt** | `determine` under `debt_suit` | SC's whole form; the defence of loss by force is a cited claim (`rung.seized`, `requisition.taken`, `field.lost`) | by SC-P4's band-keyed `disposes:`: a new stage; an `oblige` to the creditor's seat; a `ban` (the debt-bar) or `detain`; Failure is an acquittal (SC-P6) |
| **a distraint** | the officer's `requisition` on the debtor's rung under the lapsed bond | `opposition` of whoever holds the rung, `regard` of the place for the officer's seat, armed presence | the amount, part of it, nothing, or a refusal that is an unrest deed |
| **a venture's return** | the traveller's `exchange` at the foreign market | the MATERIAL lane's (`audits/14_VERBS_MATERIAL.md`): this lane requires only that the rate be band-keyed, never fixed | profit, par, loss; conservation holds (goods move between rungs; nothing is minted) |
| **a denunciation taken up and tried** | the secret bench's threshold ballot, then `surveil` / `interview`, then `determine` under a closed-floor row | the informer's `regard` and record, `evidence`, `subject` (a forgery's quality) | proceed, verify first, dismiss; then conviction, a lesser restraint, acquittal. A conviction on a false word stands until an inquiry finds the lie (the Foscarini case is a *band of the system*, not a script) |
| **an audit at exit** | the auditor seat's `open_case` and the bench's `determine` on the outgoing holder | subjects' told complaints as `evidence`, his deeds in office, `regard`, his house's obligations on the bench (zero if sealed) | clean (a prestige deed), a fine as a debt to the treasury, a `ban` from the body's seats, a `detain` |
| **a captain kept or lost** | a rival's `petition` to the captain (a better offer) against the employer's standing ask | `obligation` (his live `oblige` to the employer's seat: renewed, or in arrears), `regard`, `stakes`, the commissary's presence | stays and tells; stays; stands idle (the term runs out unrenewed); goes over |
| **a league's order to withdraw** | the league seat's `issue` to its members; each member's answer is his own roll | `obligation` (his `oblige` to the league seat), his own stores at the market (`stakes`), `regard`, whether answers are recorded | complies and reports a breaker; complies; trades quietly; defies openly |
| **a conspiracy** | no verb of its own: recruiting (`tell`, `argue`), concealment against `surveil`, the strike (`fight`, `arrest`, `seize`), the appeal to the square (`speak` in an open venue) | each link's own terms; the square's answer is the hearers' `regard` for the regime against their `regard` for the speaker | each link graded; a plot can succeed at the altar and fail in the square |

**Deterministic resolutions found in text this design depends on, listed for their owning lanes** (the
standing rule's instruction): (1) CR-34's `vote` conjunct counts live `commit`s and admits `determine` at
`quorum` (`arrangements.yaml:265-271`; `world_q.declared_votes`): a count decides; this lane's part 3
replaces the count of commits by a count of **drawn ballots** with a commit as an odds term (SC and FA
lanes). (2) `audits/14_VERBS_BINDING.md` §1: "`confer` is uncontested by design … No degree" (VERBS
lane); a conferral by lot or after a ballot is drawn here; a plain appointment's *taking effect at
distance* is not, and should be. (3) `proposals/06_FA_decree_binds.md` by title; a writ's obedience is the
addressee's roll with `obligation` in the issuer's favour (FA lane) `[file not opened beyond its title and
the citations of it in `14_VERBS_BINDING.md`]`. (4) FA-B3's plan sentence that a life seat's holder is
removed on three named facts (absence, custody, unanswered writs) reads as a fixed rule; removal is the
body's ballot with those facts as evidence (FA lane).

### 6.3 New versus reused, with the cut test for each new piece

| piece | new? | cut test: what dies without it |
|---|---|---|
| seat, body, term, remit, purview, `oblige`, `upkeep`, `dispensation`, `covenant`, `commit`, `transfer`, `give`, `ban`, `detain`, arrangement rows, the draw owner | reused | — |
| obstacle term `obligation` | **new** (one roster member, one reader in the one obstacle owner) | Every tie in the game stops mattering at the moment it is tested. Patronage, vassalage, debt, vows and contracts become edges that exist and change no odds; the Medici method, the feudal oath and the monastic vow all lose their one mechanical effect. It is also what lets the sealed ballot mean anything |
| Record kind `debt` and Event kind `debt.lapsed` | **new, already designed** (K-14) | No stored credit: no loan against a throne, no public debt, no commenda, no condotta arrears, no fine, no tax arrears, no ARC-15. The single largest obstacle in §0 |
| `binds_bases: members_by_warrant` | **new** (one roster member, one clause in `_req_oblige`) | A list anyone may put himself on is not a list. Capture "at the list-editing layer", the tree's own cross-civilisation finding, has no layer |
| seat-row key `eligible_from` | **new** (one optional key, one gate reader) | Guild-gated office, the patriciate, the cursus, "burgher status … qualify for political participation" (canon's own cell) stay prose |
| `conferral_bases: lot` | **new** (one roster member, one branch in `_eff_confer`'s conferee) | Sortition cannot be expressed; the roll has no pay-off distinct from an election; Florence collapses into Venice |
| seat-row keys `cooling_off`, `audit_at_exit` | **new** (two optional keys beside FA-P3's `term`) | Rotation without a cooling-off is re-election of the incumbent every term; without the exit audit the rector at distance has no account to render and the republic's characteristic accusation never starts |
| a `charter` term on the rate roll of `exchange`, and a `standard` on a market's venue row | **new** (one term on the MATERIAL lane's roll; no Record kind: a charter is a `dispensation`; no refusal: an unchartered trade is rolled at worse odds) | Monopoly, privilege, embargo and the league's weapon have nothing to bite on; the colonial lane's company has no charter either |
| a `purchased` conferral basis | **not taken** | Nothing: purchase is `transfer` then warrant or `confer`, and is better findable composed |
| a kin-bar (*divieto*) | **not taken now** | It needs kinship as a typed edge; `tie` has no opener (`tenure_kinds_without_an_opener`) and CHAR's `02_CHAR_relations_have_a_ground.md` owns the ground. Added as one `seat_bars` value when that lands |
| a profit-sharing venture account | **not taken** | §5.2 |
| a new verb | **none** | every act above is one of the 67 |

---

## 7. Verbs and contests, mapped to `verb_table.yaml`

No verb is added. Verbs that gain behaviour or content in this family, and the lane that owns the row:

| verb | what this family needs of it | owner / dependency |
|---|---|---|
| `covenant` | mints a `debt` when the act names `kind` and `amount`; otherwise as today | this lane (B) |
| `commit` | the debtor's undertaking; the elector's promise (an odds term, not a vote) | exists |
| `transfer` | discharge of a debt at `at`; `upkeep` to clients (exists); a purchase price | this lane (B) for the discharge read; `14_VERBS_MATERIAL` |
| `give` | hand a bond on (assignment), hand it back (cancellation), deliver a warrant or a charter | exists |
| `petition` | the ask: a loan sought, a bond presented, a favour called, a better offer made | this lane (A) adds the term; row unchanged |
| `argue`, `speak` | canvassing; the appeal to the square; pleading in the suit | SC lane; this lane adds the term |
| `issue` | the warrant of enrolment; the commission; the charter; the league's order | exists; FA-P1 for the answer |
| `comply`, `evade / defy` | the member's, rector's or captain's answer, by roll | FA lane (the repair in §6.2 item 3) |
| `oblige` | joining a roll (by warrant), a house, a captain's company, a league | this lane (C) adds the clause |
| `confer` | by `lot`: the conferee is drawn | this lane (C); FA-P3, CR-35/36 |
| `determine` | drawn ballots under a `declared` row; `debt_suit`; the exit audit | this lane (C, B); SC-P4, SC-P6 |
| `convene`, `open_case` | the sitting; the auditor's and the Avogador's intake | `14_VERBS_BINDING` B; this lane stamps `audit.due` |
| `establish` | found a house's head seat, a branch, a line, a Kontor's alderman | `14_VERBS_BINDING` A; FA `06_FA_office_capabilities.md` |
| `exchange` | the venture; a band-keyed rate; a held charter as a favourable term | `14_VERBS_MATERIAL` owns the roll; this lane (D) the term |
| `requisition`, `seize` | distraint under a lapsed bond; the forced loan | SE `06_FA_levy_through_the_seat_B.md`; this lane (B) the warrant read |
| `survey`, `tell`, `surveil`, `interview`, `reconstruct`, `forge`, `conceal`, `lie` | the *relazione*, the dispatch, the denunciation, the double ledger and its detection (ARC-15, ARC-08) | FI lane (`08_FI_*`); nothing added |
| `dispatch`, `march`, `marshal`, `recruit`, `train` | the hired company; the commissary sent to the camp | `14_VERBS_MILITARY`, CP-T09-08 |
| `release` | a debtor's repudiation, a client's leaving, a captain's quitting: each the subject's own act | exists |
| `revoke`, `pardon` | recall of a rector; lifting the debt-bar | exists; FA-P1 |

---

## 8. Commensurability: one ladder, one roll form, one clock, one currency model

Every number below is `[ASSUMPTION; medium; Jordan to correct]` with its owner and sweep. None is a balance
claim; none has been run.

| quantity | unit | owner file (one) | proposed | sweep | control arm |
|---|---|---|---|---|---|
| `obligation_step` (the term's size per live edge) | obstacle units (net successes) | `data/fixtures.py`, read only by `modules/social_contest/roll.py::obstacle` | 0.5 | {0, 0.25, 0.5, 1.0} | 0: the composed obstacle equals the pre-item one on every act |
| `obligation_arrears` (a renewed edge counts whole; one whose term has under a season left counts half) | fraction | same | 0.5 | {0.5, 1.0} | 1.0 |
| `sealed_obligation` (scale under `records_dissent: false`) | fraction | same | 0 | {0, 0.5} | 1.0 (no secrecy effect) |
| seat `term`, `cooling_off` | seasons | `offices.yaml` row | per row; council seats 4 and 4 (FA-B3's year) | {4, 8} | null |
| ballot bands | fractions of the bench present | `arrangements.yaml` row (`quorum` exists; a `carries:` key is **not** added: more than half and two thirds are the ladder's Success and Overwhelming for every `declared` row, in the one tally function) | 1/2, 2/3 | — | — |
| `debt.amount`, `debt.kind` | whole units of a `matter_kinds` member | the Record | by the act | — | — |
| `credit_terms` (owed ÷ advanced, by the loan roll's band) | ratio, applied when a computed act names no amount | `data/fixtures.py` | Overwhelming 1.1, Success 1.25, Partial 1.5 | {flat 1.0; these; steeper} | flat 1.0 |
| `stakes_ob` rows for `debt` | obstacle units | SC's fixture table `stakes_ob` | amount ÷ the asked rung's stores of that kind, capped at 2 | {off, on} | off |
| `upkeep` of a house's head seat | units per obligee per term | `offices.yaml` row (`Office.upkeep`) | 1 (the fixture default) | — | — |

- **One ladder**: Overwhelming, Success, Partial, Failure for every row in §6.2, through `degree_from_net`.
- **One roll form**: SC's composed obstacle; this lane adds one term and no second composer.
- **One clock**: `Tenure.term` and `Record.stages`, both matured at MATTER.
- **One set of scales**: a house is a hearth, a guild chapter or quarter a community, a commune a
  settlement, a league a faction's seats across territories, the republic a foreign settlement with realm
  reach by treaty. The same five parts at each.
- **One currency model**: stores of a `kind` at a rung, conserved. A debt moves no stores by itself.

---

## 9. Tuning dimensions

`audits/13_SC_contest_interrogation.md` did not exist when this was written; the dimensions are stated
against SC's obstacle roster instead.

| dimension | where it enters | owner |
|---|---|---|
| **venue** | open square, guildhall, sealed council chamber: `floor`, `records_dissent`, `venue_min_rank` on the arrangement row; `capability` circumstance rows per venue | `arrangements.yaml`, `venues.yaml`, `tables.capability_uses` |
| **personality** | the chooser's pursuits decide *whether* a person lends, canvasses, defects or informs; a patient creditor extends, a proud debtor refuses in public | `goals.yaml`, `rosters.yaml: pursuits`; CHAR lane's statement |
| **affiliation** | a creditor of another creed; the Church's view of gain | `data/affiliations.py`, `rosters.yaml: incompatible`, the `regard` term |
| **office** | the seat exercised sets purview, treasury and remit; a rector's commission narrows it | `offices.yaml` |
| **evidence** | the bond, the warrant, the charter, the ledger, a deed cited, a forgery's quality | SC `05_SC_evidence_and_rebuttal_B.md`; FI `08_FI_05_evidence-interface_B.md` |
| **publicity** | recorded or sealed; a demand made in the market or in the counting-house | `records_dissent`, `disposal_reach` |
| **season** | harvest sets what a rung can pay; a term's last season weakens an obligation; war on the route | `Rung.stores`, `Term`, `world_q.at_war` |
| **relationship** | `regard`, and the `obligation` edge itself (whose, how long, how lately renewed) | `person_q.stance_toward`; this lane's term |

---

## 10. Emergent narrative with no player, and the instrument for each

Each is a pattern the five parts produce from persons' acts. For each: the condition, and a reading that
could show it happened and could fail. The instrument is one read-only harness script over the event log
(`harness/strife.py`'s shape: kinds counted per seed with a control), not a new guard.

| story | arises when | reading that shows it (and can fail) |
|---|---|---|
| **Capture of a republic from behind** | one person holds live obligations (clients' `oblige`, debtors' `commit`) of more than half a roll or a bench, and holds no seat on it | per season: the largest share of a bench's members with a live edge to one person, and that person's seats. Fails if no share ever passes the control world's (obligation term off) |
| **A banking collapse** | a creditor house's bonds lapse faster than its own debts fall due | chains of `debt.lapsed` in which the debtor of one is the creditor of the next, within N seasons. Fails at chain length 1 |
| **A loan against a throne, and a default** | a seat-holder borrows through his seat and dies or repudiates | `debt.lapsed` whose debtor held a realm or duchy seat; the successor's `commit` or its absence |
| **The debt-bar empties a council** | arrears or a lost suit puts a `ban` on a sitting member | `tenure.closed` or a refused `confer` citing a `ban` whose opening act cites a `debt` Record |
| **A rigged lottery found out** | a roll shrinks to the keeper's clients and a drawn officer is challenged | roll size and the share obliged to the keeper, per sitting; an `open_case` naming the keeper |
| **A captain turns** | an `oblige` to the employer's seat matures unrenewed while a rival's offer stands | `tenure.closed` (term) on a military obligee followed by his `oblige` elsewhere or a `rung.seized` by him |
| **The league withdraws** | a charter is refused or lapses and the league seat orders its members out | a fall in `exchange.made` at one market by obligees of the league seat after a `dispensation.issued` to them, against the control |
| **A wrongful conviction published** | the secret bench convicts on a told claim later found a lie | a `detain`/`ban` opened under a closed-floor row, closed by `pardon` after a `finding` on the informer |
| **A plot that wins at the altar and loses in the square** | any failed `speak` in an open venue following a `person.died` by the speaker's party | the two kinds in one chain with opposite bands |
| **Both sides funded** (ARC-15) | one house holds bonds of two parties whose factions are at war | two live `debt` Records held by one person whose debtors' factions satisfy `at_war` |
| **Two rectors, two reports** (added on re-grounding, §17.2 item 1) | a subject place's two officers `tell` the centre differently about one season | per season: claims about one referent told to the conferring seat by its two officers with opposite content; then which one the centre's next act follows. Fails if the two never differ against a one-officer control |
| **The pledge that was never redeemed** (§17.2 item 10) | a debtor hands over a held instrument with his bond and the debt lapses | a bearer instrument `give`n by a debtor to his creditor in the season of the `debt`'s minting, still held by the creditor after `debt.lapsed` |
| **The captain bought in reserve** (§17.2 item 8) | a `condotta` is in its second stage and a rival offers | an `oblige` by a military obligee to a second seat opened while his first is in its reserve stage, with no breach claim deposited |
| **The unpaid company turns on its host** (§17.2 item 8; `HCC:67`) | the employer misses the `due` and the company is lodged in a stocked town | `requisition.taken` or `rung.seized` by an obligee at the settlement he resides in, within two seasons of his `oblige` closing unrenewed |
| **The appointer answers for his man** (§17.2 item 4) | an audit condemns a rector and the Record recites who conferred him | the `regard` of persons holding that Record toward the conferrer, before and after, against a control whose Record does not recite |

---

## 11. Provided arcs and characters that depend on this family

Against `audits/12_ARCS_adjudication.md` §3 (statuses there are that lane's; this column is what this
family's parts supply). No case is claimed simulable on this lane's changes alone.

| case | need that turns on this family | part | other lanes first |
|---|---|---|---|
| **ARC-15 The Banker's War** | N1: fund two hostile sides for profit from each unit of conflict (M-STORES, "declared, not reached") | part 4: two `debt` Records held by one house; profit is the amount owed over the amount advanced | FI (three detection paths, the curated lie), M-AIM (holding knowledge as a choice), coin or in-kind stores at build |
| **ARC-08 What the Guilds Know** | a body that possesses intelligence and chooses what to release | part 5: factors' `survey` Records and told dispatches gathered at the house; no faction stat (that lane's §6 row 2) | FI `08_FI_02_rumour-that-travels.md` |
| **ARC-R18 The Tied Vote** | N1: a multi-round formal vote between two coalitions (M-SIT, **absent**) | part 3: a drawn ballot whose Partial band keeps the matter on the docket | SC hearing B; CR-35 |
| **ARC-25 The Schoenland Pivot** | N1: a neutral third party evaluates and aligns (M-ABROAD) | §4.3 and proposal D: Schoenland's seats and its senate's ballot | WR (the off-map place), M-CASE |
| **NPC-007 Annika Feldhaus** | N2: a supply chain that can be cut; N3: two actors who each built one half | part 4 (a venture financed), part 5 (a house with branches) | SE trade; M-LATENT |
| **NPC-084 Frieda Kessler** | holds and argues a position against her own body's line | part 3: a rotating council seat by lot, a recorded division | FA-P2 (her seat's row) |
| **NPC-085 Nessa Grindvold** | N1: a guild's privileges challenged in a venue (M-SIT) | part 5: the charter is a document; the challenge is a suit on it | SC hearing B; `12_ARCS_cited_evidence.md` |
| **NPC-090 Stephanos Doukas** | N1: a trade relationship between polities that can be suspended or altered (M-REC) | part 5: the charter term on `exchange`'s rate roll and the market's `standard`; his seat issues or withholds the one and may raise the other | WR; BYZANTINE lane (his office) |
| **NPC-037 Annalie Reichard** | N2: the treasury-oversight post (M-STORES) | part 4: the forced loan and the state as debtor; the exit audit | SE `07_SE_treasury_granary_B.md` |
| **SCN-12** (a succession that trades a present benefit for a future claim) | N2 (M-REC) | part 4: the claimant's bond to a backer | FA succession |

Order in which this family brings cases up: NPC-084 (C alone, on FA-P2 and FA-P3) → NPC-037 (B on SE's
treasury) → ARC-R18 (C on SC's hearing) → NPC-085, NPC-090 (D) → ARC-15 (B, with FI and M-AIM) → ARC-25.

---

## 12. Interfaces to other institutions

Named primitives and verbs. **Exports** are what this family defines and others use; **imports** are what
it uses and others define. One name, one owner.

### 12.1 To and from the crown (and nobility by deed)

| | primitive / verb | meaning at the seam |
|---|---|---|
| export | `debt` (Record) + `commit` | a loan against a throne: the borrower commits through his seat; the bond dies with him unless the successor commits. The crown's forced loan is the same instrument with the treasury seat as debtor |
| export | `obligation` (obstacle term) | the vassal's `oblige` to `off_king` becomes odds on every royal ask (a writ, a muster, a vote), not a certainty |
| export | `eligible_from`, `members_by_warrant` | a court roll or a peerage as a list a seat keeps; ennoblement by deed is a warrant after a ballot |
| export | `cooling_off`, `audit_at_exit` | available to any appointed crown seat |
| export | charter (a `dispensation` naming a market) | the crown grants or withholds a town's or a league's privilege; `revoke` and non-renewal are the crown's side |
| import | deed claims, `world_q.reception`, `standing_routes` | accomplishment as evidence in enrolment and election |
| import | `successions`, `succeed`, `inheritance` | untouched; a house's standing is *not* a succession |
| import | `rung_above_in_holdings`, `revoke` | recall of a rector or a chartered seat |
| structural conflict | the crown needs credit and resents creditors; a creditor house needs the crown's courts to collect and fears its default. Neither can do without the other (the brief's "a loan against a throne") |

### 12.2 To and from the Church

| | primitive / verb | meaning at the seam |
|---|---|---|
| export | `debt` + `debt.lapsed` | the prelate's unpaid appointment fee; the Church as depositor and as debtor; tithe arrears |
| export | usury as a **derived fact** (`amount` over principal, same `kind`, same `at`) | what a Church inquiry can find and a Church bench can try; the different-kind, different-place instrument is the lawful dodge |
| export | goods and bonds abroad | what an interdict on a merchant commune bites on: its members' stores at foreign rungs and the bonds they hold there |
| export | the crown-gate pattern of §3.7 of `01_venice_procedure.md` | a Church bench on a commune's ground with lay assessors holding the arrest and execution steps: two `interposed: [office]` entries on the Church's arrangement row |
| import | `ban` by a Church seat (excommunication; `excommunication_deliberation`), interdict | lifts the `obligation` term toward the banned (an oath to an excommunicate does not bind) and bars seating under that bench's purview |
| import | sacramental standing as `regard` and `affiliation` | Savonarola's leverage and its loss |
| import | benefices as seats | a house places a son in one; composed (`transfer`, then the Church seat's `confer`): simony is findable, as venality is |
| structural conflict | the Church condemns the gain it banks; the house finances the Church it fears. A preacher with no seat against a banker with no seat is the purest form |

### 12.3 To and from the Byzantine-style bureaucracy (Altonia)

| | primitive / verb | meaning at the seam |
|---|---|---|
| export | charter | the Kommerkiarios (`off_kommerkiarios`, remit `[issue]`) issues, renews or withholds the dispensation whose holder trades at his market on better odds, and may raise the market's `standard` (an embargo) |
| export | the house as a foreign enclave (a hearth rung with a head seat inside another faction's settlement) | the Kontor; the bureau's counterpart is the enclave's alderman |
| export | `survey` Records and told dispatches | the *relazione*: what a merchant republic knows of the empire, held as documents that can be seized or forged |
| import | the sequence of offices, seals and delays (that lane's procedure rows and `interposed:` chains) | a charter passes through it; each step is a seat that can be asked (`obligation`, gifts composed) |
| import | rank by appointment and examination | the capped career of the republic's own secretaries is the same ladder; no second one is built here |
| structural conflict | the bureau sells access and fixes terms; the merchants need the market and can leave together. Both sides keep ledgers the other wants to read |

### 12.4 To and from colonial companies

| | primitive / verb | meaning at the seam |
|---|---|---|
| export | the rector at distance (appointed, termed, commissioned, `cooling_off`, `audit_at_exit`) | the company's governor and factor |
| export | `debt` as a transferable bond | the company's stock is a bond the company seat owes its holders; a share is a `debt` Record handed on by `give` |
| export | charter and its term on `exchange`'s rate roll | the monopoly, as an advantage that can be undercut and not as a wall |
| export | the line as a termed seat over a foreign market | the chartered voyage |
| export | the hired company (`oblige` to the employer's seat, renewed by `upkeep`) with a commissary | the company's troops |
| import | the peoples under a charter (that lane's seats and rolls for subject communities) | who sues a rector at his exit audit |
| import | settlement founding at distance (`found`, `establish`) | the factory |
| structural conflict | the rector's commission against his own trade (no local ties, enforced only by the audit); the settlers against the centre's tax (Crete, 1363) |

### 12.5 What the synthesis lane should reconcile

One list of obstacle terms (this lane adds `obligation` and nothing else); one instrument family
(`dispensation` for warrant, commission and charter; `debt` for everything owed in a stated amount); one
set of seat-row keys (`term`, `cooling_off`, `eligible_from`, `audit_at_exit`); one roll mechanism
(`members_by_warrant`); one ballot (drawn, under `disposal: declared`).

---

## 13. Implementation plan

Batches are linked by a shared file or gate (`methodology-execute`'s unit). Cost classes: edit / small
build / design-first.

| batch | proposal | what lands | cost | depends on | gate (execution artifact, with control) |
|---|---|---|---|---|---|
| **A** | `proposals/15_INSTITUTIONS_VENICE_A_obligation_and_the_ask.md` | `obstacle_terms` gains `obligation`; three fixtures; the host carries the edge count raw; the term is recorded on the roll | small build | SC `05_SC_obstacle_difficulty_and_modifiers_B.md` (the composer and the roster), SC-P1 (terms on the Event) | spine and realm, seeds 0–2: at `obligation_step: 0` the content hash equals the pre-item hash; at 0.5 the four vassals' answers to `off_king`'s asks carry the term, and the band distribution of asks to obliged against unobliged persons is **read and reported** over the three seeds (a reading, not a balance claim) |
| **B** | `…_B_debt_instrument.md` | `record_kinds: debt`; `covenant` mints it; discharge read in `_eff_transfer`; `debt.lapsed` at MATTER; `arrangements.yaml: debt_suit`; the lapsed bond as a `warrant_sourced` warrant | small build | A; SC-P4, SC-P6; SE `07_SE_treasury_granary_B.md` (stores at build) | hand-built fold: mint, part payment, extension, lapse, suit, each with its Event; seeded: a fixture with one stocked house, seeds 0–2, six seasons: debts minted, reckoning bands and lapses **read and reported**; control: no `debt` kind in the roster → hash EQUAL to pre-item |
| **C** | `…_C_roll_lot_ballot.md` | `binds_bases: members_by_warrant`; row keys `eligible_from`, `cooling_off`, `audit_at_exit`; `conferral_bases: lot`; drawn ballots under `declared` | small build; the ballot is **design-first** (it changes CR-34's shipped conjunct) | FA-P3 (the `term` key and loader), CR-35, CR-36; SC hearing B | spine, a three-seat rotating council with a roll of eight: over twelve seasons every seat turns over by lot, no holder is re-seated inside his cooling-off, at least one exit audit is opened by a person; control: all new keys null → hash EQUAL; planted failure: the lot ignoring `eligible_from` seats a stranger |
| **D** | `…_D_houses_charters_and_content.md` | content: house head seats for the Guilds, Schoenland's seats and body, council rows for a Hafenmark commune; three arrangement rows (two more named, waiting on CR-35 and CR-36); the `venue` anchor form; the charter term; the scenario fixture | edit (content) + small build (anchor form, fixture); the charter term is held until `exchange` is rolled | A–C; FA-P2 (`off_guild_leader`), FA `06_FA_office_capabilities.md`; WR (Schoenland's place); `14_VERBS_MATERIAL` (`exchange`) | the playable scenario below, headless, seeds 0–2, with its control |
| **E** (added on re-grounding, §17) | `proposals/15_INSTITUTIONS_VENICE_grounding_E_what_the_tree_adds.md` | content: the paired officers on a subject place; the commune's pact; the secretary order and its roll; the brotherhood; the Arsenal's `upkeep`; the guild's rule-making remit moved to its hall seat. One form row `condotta`; one arrangement row (`guild_debt_suit`); the audit Record's recital of the conferrer; the exit report's hand-over | edit (content) + small build (the recital; the form row's stage) | D; COLONIAL C-1 (`instruments.yaml`), C-3 (`audit`) | spine, one subject town with two officers and a pact, seeds 0–2, eight seasons: the two officers' told claims are **read and reported** against a one-officer control; a hand-built fold for the pledge (given, returned, kept) and the contract's three stages; control: batch E's rows absent → hash EQUAL to the post-D hash |

**The first playable scenario: "The Counting-House"** (standing requirement; proposal D §5). A guild town
of one settlement on the spine fixture. The player-proxy is the head of a house with a stocked chest, two
sworn factors and a seat on nothing. Around it: a three-seat rotating council filled by lot from the
guild's roll, a roll-keeper, a lord who needs grain before the harvest, a rival house. Choices each season
through the ordinary aperture: lend (to whom, how much), pay clients' upkeep or let them lapse, seek
enrolment, canvass, present a bond or extend it, sue, tell. Stakes: the chest, the roll, the council.
Endings: the house holds a majority of the council's obligations (it rules from behind); the house's
bonds lapse and its own fall due (it fails); the head is barred for arrears; or twelve seasons pass
(a stable continuation, scored by nothing). The same module code and the same loop run it; nothing is
scripted; the instrument is §10's reading. A smaller first cut needs only A and B: one loan, one harvest,
one reckoning.

**Dependencies on other lanes, as edges**: SC obstacle B → A; A → B → D; FA-P3 → C; CR-35/CR-36 → C's
ballot; SE treasury → B's seeded gate; FA-P2 → D's Guild rows; WR M-ABROAD → D's Schoenland rows;
MATERIAL `exchange` → D's venture; CHAR relations → the kin-bar (not scheduled).

---

## 14. Resolutions decided, and what survives for Jordan

### 14.1 Resolutions (the five-step ladder, in order)

| # | inconsistency, gap or unclear passage | resolution | step | carried by |
|---|---|---|---|---|
| 1 | `debt` deferred "with its reader" (K-14) while ARC-15, NPC-037 and the brief's "a loan against a throne" need it | un-defer, in K-14's own shape, with the readers designed here | 3 (the design document names the shape), 5 | B |
| 2 | Does a creditor get a lever? | No: D-5 stands. Recourse is the ask, the suit, telling, assignment | 1 (ruled) | B |
| 3 | `covenant` "in force when both holders are committed — a reading nothing performs yet" | the `debt` kind's readers perform it for debts; treaties stay deferred | 5 | B |
| 4 | CR-34's count of commits decides a `declared` matter | ballots are drawn at the sitting; a commit is an odds term | 1 (the standing rule) | C; listed for SC, FA |
| 5 | `conferral_bases` note: "which act fills an `elected` … seat is not ruled" | unchanged: CR-35's; this lane adds `lot` beside it | 3 (the plan) | C |
| 6 | `binds_bases` has one value and concedes it | a second value arrives "WITH its rule in `_req_oblige`", as the roster's note requires | 4 (the roster's own stated precedent) | C |
| 7 | FA-P3's first authoring (eight elected rows at `term: 8`) against FA-B3 (three rows at 4) | FA-B3 stands (it says it supersedes); this lane adds `cooling_off` on the same rows only | 1 | C |
| 8 | Schoenland: "its persons act from their own seats" (canon) and no seat authored | author them as content (proposal D), marked assumption | 3 | D |
| 9 | The Guilds are "headless by design" and ARC-15 needs "the faction" to fund both sides | the actor is a house head (a person in a hearth seat), as `12_ARCS` §6 row 2 already rules for "the Guilds' choice" | 1 | D |
| 10 | Coin has no producer; a bank needs money | instruments are denominated by `kind`; nothing here waits on coin | 5 | B |
| 11 | Purchase of rank or office as a conferral basis | not a basis; composed `transfer` then warrant or `confer` | 4 (#453 row 38) | — |
| 12 | The compendium's C10 and I6 (registered-lineage gate; emergency rank buy-in) "speculative pending a Venice-style faction actually being authored" (`.audit/…/40_roster_officer_system.md:588-589`) | superseded: the roll by warrant covers both without `marriage_registered` or a buy-in flag | 1 | C |
| 13 | The research hooks written against Keys ("appointment Key", "exit Key", "watcher Key-emitter") | irrelevant as mechanism (the Key substrate is retired, ED-IN-0232); the insight is kept as `audit_at_exit` and the suspending officer's `open_case` | 2 | C |
| 14 | What happens after an Avogador suspends an act (the research's own gap) | the suspended matter returns to the same body's docket for a fresh ballot at the next sitting; no higher body | 5 | D (arrangement row note) |

Resolutions decided: **14**.

### 14.2 Survivors for Jordan (each survived the ladder; two options, two games)

1. **Is a roll in this world ever closed by blood?** (a) *No*: every roll is by warrant; an heir is
   enrolled in his own right with his house's deeds as evidence (this design; follows "nobility by
   deed"). The world then has no closed caste anywhere, and a *Serrata* cannot happen. (b) *A body may
   vote to close its own roll to descendants of present members*: one more `binds_bases` value, reachable
   only by a ballot of the body. Then oligarchic closure is a thing a commune can do to itself and a
   player can fight, at the price of a hereditary standing that is not by deed. These are different
   worlds; (b) overwrites the reading of the fixed point, so it is not taken.
2. **What is Schoenland's constitution?** (a) *The Venetian shape* (an elected, bound head; a senate that
   votes on a college's menu; a sealed security bench; lines auctioned by term): proposal D, authored as
   assumption. (b) *Leave it unseated*: a spoiler whose acts come from one or two authored persons with
   goals and no institutions. (a) makes the neighbour a place a player can corrupt, lend to and be banned
   from; (b) keeps it a limit on the map. Canon says only "neutral offshore trade nation"; the name
   *Island Republic* is geography's.
3. **May a house's head seat exist on a hearth with no faction?** `office_faction` refuses a seat that
   belongs to nothing. (a) Every house belongs to a faction, authored on its row's `faction:` (Feldhaus's
   to the Guilds; a titled post may not sit in a body, `refuse_a_title_in_a_body`); a foreign factor's to
   his own. (b) A private house is its own small faction ("factions can be of any
   scale", Jordan, 2026-09-18). (a) is taken (no roster change); (b) would let a banking house outgrow
   and leave its guild, which is the Medici's actual arc, and it is a real fork.

---

## 15. Research transfer

**Changes what to build**: the roll as the capturable resource (`political_hierarchy_standing.md` §The
standing currency, compared) → parts 2 and 3; rotation, *contumacia* and the exit audit (`governance_modes.md`
§Venice 1.3; §Florence 1.7) → part 5's keys; the secret ballot (`01_venice_procedure.md` §1.3 step 11) →
the `sealed_obligation` scale; the menu of opinions with lowest-dropped re-ballot (§2.1 steps 3–6) → the
Partial band of a ballot; the Hanse's withdrawal (`fa_se_historical_precedent_research_v1.md:119`, `:239`)
→ the league's order as an ask; the rettori (`proactive_governance_scale_research_v1.md` X8) → the rector;
Tilly's capital-intensive type (`:95`) → placement on Hafenmark; the non-sincere ballot (`:308`, CP-3) →
the "doubtful" ballot.

**Decorative, or not transferred**: the nine-stage Doge election (depth without perceptible effect); the
Marriage of the Sea and the civic myth (colour for a venue, no mechanism); every figure (terms, sizes,
thresholds, prices), which the sourcing floor makes leads; the composite standing score
(`political_hierarchy_standing.md` §Venice 2.7), which would be a stored aggregate Layer 1 refuses.

**Nulls**: I know of no shipped game in which patronage is an edge whose effect is *odds on an ask* and
which a sealed ballot switches off; none in which a debt is the debtor's own undertaking with no creditor
action; none that models capture at a roll rather than at a vote. Crusader Kings III's hook is the nearest
and is the lever D-5 refuses (#453 rows 40, 48). These are unproven designs, not adaptations.
`research/game_precedent_suite/tables/R9_policy_court_sims.md` was not opened this session `[SKIPPED: not
needed for a decision made]`.

**Nulls restated on re-grounding (2026-11-12; the suite's throughlines and the two relevant tables now
opened).** The three nulls hold, more narrowly, and one sentence above was wrong to be stated unchecked.
(1) *A debt as the debtor's own undertaking*: the suite's own row for the obligation token
(`research/game_precedent_suite/THROUGHLINES.md:30`, `:79`) lists Crusader Kings III's hooks, Frostpunk
2's and Suzerain's promises and Jagged Alliance 2's term contracts, and grades the engine PARTIAL on
`oblige` alone; none is a transferable bond with no creditor verb. The null stands. (2) *Capture at a
roll*: none found; the companion says outright that its territorial model "is carried almost entirely
by Venice rather than by any game" (`research/valoria_game_precedent_companion_v1_part5.md:240-244`).
The null stands. (3) *Patronage as odds on an ask that a sealed ballot switches off*: none found. The
null stands. **What was missed:** three shipped games do model this family's ladder, and the audit named
none. **Patrician IV** (`research/game_precedent_suite/tables/R8_npc_life_economy.md:81-110`): a Hanse
trader's rank is a threshold on wealth, ships, counting houses and workers; rank opens the council
(propose, then run for mayor, then for alderman); the mayor sets the head tax and guarantees prices from
the town chest; loans are had at the tavern; hoarding a scarce good costs standing in that town. **The
Guild 2 and 3** (`research/game_precedent_suite/tutorials/T14_squad_settlement.md:228`, `:281-313`):
titles bought in sequence, offices elected. **John Company**
(`research/valoria_game_precedent_companion_v1_part6.md:165-175`; `_part7.md:41`): offices held by
different players whose powers are "complementary rather than sufficient", so a venture needs several
to cooperate, "and the Company can fail while you win". The transfer from these is one line each and is
decorative for the five parts: a ladder by accumulated stock is the thing §5.3 refuses (rank by warrant
and ballot, not by a wealth threshold); John Company's complementary offices are §1.4's proposer and
disposer, already kept.

---

## 16. Evidence log

| id | command or reading | outcome |
|---|---|---|
| E-1 | `PYTHONPATH=. PYTHONHASHSEED=0 python scratchpad/runs/INST_VENICE/probe_build.py` (read-only; `populated.build_realm(0)`); output `scratchpad/runs/INST_VENICE/probe_build.txt` | 34 offices (seats by rung kind: territory 17, duchy 10, realm 4, settlement 2, none 1; **no hearth or community seat**); conferral: appointed 18, elected 8, inheritance 1, null 7; live tenures: contain 411, reside 83, commit 148, hold 52, **oblige 4**; **termed live tenures 0**; Records: 2 (`works`); rungs: 211 hearths, 60 communities, 38 settlements; **stores empty on every rung; no coin**; fixtures `default_upkeep` 1, `oblige_term` 4 |
| E-2 | files opened at the cited lines: `offices.yaml` (whole), `arrangements.yaml` (whole), `governance_spine.yaml` (whole), `rosters.yaml` (`tenure_kinds`, `remit_acts`, `eligibility_kinds`, `record_kinds`, `record_sourced_operands`, `matter_kinds`, `factions`, `office_bodies`, `conferral_bases`, `successions`, `continuation_ties`, `revocation_bases`, `binds_bases`, `standing_routes`, `strife_kinds`, `foreign_factions`, `site_yield`), `state/carriers.py` (`Term`, `Tenure`, `Office`, `Rung`), `state/gate.py` (`purview_reaches`, `sworn_to`, `may_fill`, the determination clause), `loop/effects_information.py` (`_declared_stages`, `_mint_document`, `_eff_issue`, `_eff_covenant`, `_eff_seize`), `verb_table.yaml` (header; `covenant`, `exchange`, `forgive`, `give`, `oblige`, `transfer`, `determine`'s contest cell) | as cited |
| E-3 | not run: `pytest`; `aperture`; `corpus_run` (its readings are taken from `12_ARCS_adjudication.md` and `14_VERBS_BINDING.md` at the line and marked) | — |
| E-4 | not opened and relied on only by title or by another lane's citation: `06_FA_decree_binds.md`, `06_FA_office_capabilities.md`, `06_FA_remit_grant_by_row.md`, `07_SE_treasury_granary_B.md`, `05_SC_evidence_and_rebuttal_B.md`, `08_FI_*`, CR-88's entry, `world_q.declared_votes`' body, `_renewals`' body, `data/fixtures.py` beyond `:613-634`; the digests `digests/DG_*` `[SKIPPED: the governance sources were read at their own files instead]`; `.audit/2026-07-09-comparative-governance-research` and `_workings_joined.md` `[SKIPPED: grep only; superseded in content by `research/governance/`, per its manifest]` | every claim resting on one of these is a design dependency, not a statement of code behaviour |
| E-5 | `git status --short` before handback | recorded in the receipt |
| E-6 | re-grounding pass, 2026-11-12, at `62dbc8b`: the work order's grep over `research proposals` (624 files) and `.designs .audit` (260), then exact-term greps for each `[M]` claim; files and depths in `unified/RESEARCH_MAP_INSTITUTIONS_B.md` §1.1 | **E-4's skip of `.audit/2026-07-09-comparative-governance-research` was wrong**: the manifest it relied on says the governance corpus "reorganizes and deepens" the earlier dockets (`research/governance/00_MANIFEST.md:5-10`), not that it contains them; the skipped file's `:87-117` is the tree's source for the Arsenal, the rectors' terms, the syndics, the *dedizione*, the citizen secretaries, the Venetian guilds, the podestà's audit, the *condotta* and the Mercanzia. No instrument was run; no file outside this suite was edited |

*Revision of §0 on completion:* the verdict's five missing parts stand. Two things changed while
writing: the term is FA's (proposed, not this lane's), so this lane's own additions are four parts and one
obstacle term; and the standing rule moved the ballot from a count of commits to a count of drawn
ballots, which makes part 3's ballot design-first rather than a data edit.

---

## 17. Re-grounding against the tree's research (2026-11-12)

Jordan: *"Research should have been found in /research or /proposals."* This lane wrote most of §1.6 to
§3 from memory and said so. The tree holds a source for much of it. The claim-by-claim table is
`unified/RESEARCH_MAP_INSTITUTIONS_B.md` §2.1 (rows V-1 to V-50), not repeated here; this section records
what changed in the design because of it. Everything cited is tier 3.

### 17.1 Corrections (the tree's source differs from what this file said)

| # | section | this file said | the tree says | effect on the design |
|---|---|---|---|---|
| 1 | §1.1 | the Faliero conspiracy of 1355 made the Ten permanent | permanent 1334 or 1335 by the verifier's note (`GM:310`); 1355 in the unpatched body (`GM:345`) | none: the ratchet is the mechanism, not the date. A caution on the source: the governance corpus's fixes are quoted at each section's head and were not applied to its body |
| 2 | §1.3 | the 1297 act closed the Council to sitting members "and their descendants" | 1297 confirmed sitting members by a ballot of the Forty; descent came with later registration (`GM:311`, `:334`) | strengthens §5.2: closure by a body's ballot is the original act, and it is the form this design keeps |
| 3 | §1.8 | "16,000 … a few thousand is safer" | a stable core of about 2,000 and a peak of about 16,000, both kept (`CGR:91`) | none (no number is taken); the works gains a standing wage liability (§17.2 item 9) |
| 4 | §1.8 | the Arsenal men were "the only trusted armed body" | they were the Doge's accomplices in 1355 (`CPS:306`) | adds a story to §10: the guard is an establishment like any other and can be asked by its head |
| 5 | §2.5 | sumptuary law placed under Florence | the tree's instance is Venice's magistracy, 1476 to 1562 (`PGS:121`) | none |
| 6 | §2.7 | the Pazzi "had just taken the papal account" | the Pope was angered by Lorenzo's blocking of a Pazzi-financed land purchase (`CPS:257`) | sharpens §10: the quarrel began over **a loan refused passage**, which part 4 can express and an account cannot |
| 7 | §2.8 | the fall ran through the interdict's threat to merchants and a hostile draw | two independent blows, both required: excommunication, then the failed ordeal (`CPS:277`; `RTP:539-542`) | §6.2's last row is confirmed as built: each link its own draw; nothing makes the second follow |
| 8 | §1.7 | rectors served "about two years" | fixed terms of 16, 24 or 36 months (`CGR:99`) | §8's `term` sweep {4, 8} seasons brackets it; no change |
| 9 | §3 | blockades of "Bruges 1358 and 1388; Norway 1284" | Bruges 1358 and 1451 to 1457 (`FASE:119`) | none |
| 10 | §2.6 | the contract's second term is "at the employer's choice" | a reserve phase at reduced pay in which the captain may be poached, then a lapse with non-aggression (`CGR:110`, `:208`) | changes §6.2's row "a captain kept or lost": see §17.2 item 8 |

### 17.2 Mechanisms the research describes that this design did not carry

Each is stated as the brief asks (who acts, what verb, what is written, who reads it), on the five
parts and the kit's registries; none adds a carrier, a verb or an obstacle term. Exact edits, gates and
falsifiers: `proposals/15_INSTITUTIONS_VENICE_grounding_E_what_the_tree_adds.md`. Under the standing
rule each outcome is a draw; where a row below says "reads", it is an odds term or evidence, never a
result.

| # | mechanism | source | in the engine's terms | what it generates with no player |
|---|---|---|---|---|
| 1 | **Two officers over one subject place** | `PMP:138-140`, `:513-516`; `PGS:148`; `CGR:99` | two appointed, termed seats on the subject settlement's rung with **disjoint `remit_acts`**: one holds `open_case` and `determine` (justice), the other `dispatch` and the purse (`transfer`, `requisition`). Each `tell`s the centre separately. Content rows in proposal D's shape; no key | two reports of one place that disagree; a governor who must court his colleague to act; the centre choosing whom to believe |
| 2 | **Near split, far combined** | `CGR:102` | a content convention, not a rule: a seat row at a place one hop from its conferrer is one of a pair; a seat far off (the colonial lane's `remove`) holds both remits. The combined seat is the stronger and the more dangerous | the over-mighty officer arises where the centre could not afford to split him |
| 3 | **The submission pact** | `CGR:94`; `PMP:508-511`; `GPC:195-199`; compendium `tier3:147` | the subject commune's head seat holds a `capitulation` or `charter` (the kit's forms) whose `forbears` name the rector's `revoke` and `confer` over the commune's own seats and his `requisition` above an agreed amount. A breach is a claim in the commune's ledgers (the colonial lane's `kept`) | the rector who levies past the pact; the commune that opens its gates to a rival because of it (`CPS:314`) |
| 4 | **Appointer liability, and the inspection as theatre** | `CGR:109`, `:207`; `PMP:119`, `:465-469` | the `audit` row's Record (admonition or condemnation) **recites the seat that conferred the audited seat**; persons who hold it judge the appointer by it (`deeds_judged`), no rule. The open floor on the governed ground is witnessed by the cohort; the reading is the cohort's regard for the centre's seat before and after | the centre that stops sending its friends; the syndic sent to be seen |
| 5 | **The standing report** | `PMP:150-152`, `:459-463`; `CGR:100` | at exit the outgoing holder's `survey` Record of the place is `give`n to his conferrer's rung, where it sits with its predecessors: a held, stealable, forgeable, fading document. A favourable term for the next holder's first acts there (as `evidence`); a proof in his own audit | an archive worth stealing; a successor misled by a predecessor's flattering report |
| 6 | **The capped second order** | `PHS:362`, `:341-343`; `CGR:96` | a second roll (`members_by_warrant`) whose members are `eligible_from` for secretary seats **without a `term`** and for no council seat. The secretary holds the body's Records (he is the archive's keeper) and drafts: the college's menu of opinions (§1.4) is `issue`d through his seat | the man who has sat in every council for thirty years and can never preside; the rotating noble who signs what he is handed |
| 7 | **The channel split** | `PMP:154`, `:471-475` | an envoy's or rector's `tell` may go to the secret bench's seat and not to the body that sent him. No mechanism: `tell` has an addressee. The story is which addressee he chose | the Senate learning that the Ten knew |
| 8 | **The contract in phases** | `CGR:110`, `:208`; `tier3:103`; `HCC:67` | a form `condotta` in `instruments.yaml` (`made_by: covenant`): the captain's `oblige` to the employer's seat; `due` by the employer, `upkeep` each season; a second stage at half `upkeep` (the reserve), in which the `obligation` term toward the employer counts half (this file's `obligation_arrears` already says so) and **a rival's offer is no breach**; `forbears` by the captain for a term after lapse: `march` against the late employer. Arrears are the employer's missed `due`, which the captain reads as a breach | the captain bought in the reserve season; the unpaid company that takes its wages from the town it is lodged in |
| 9 | **The works that must be paid whether used or not** | `CGR:91`, `:198` | the Arsenal as proposal D has it (a works site with a sworn establishment), with the `upkeep` of its establishment set above the default: a standing charge on the chest. Content only | the yard that eats the treasury in peace; the Doge who asks its men a favour |
| 10 | **The pledge** | `HCC:161`; `CGR:190`; `tier3:95` | at the making of a `debt` the debtor `give`s the creditor a bearer instrument he holds (a `staple`, a `farm`, a `warrant`); the creditor hands it back at discharge. No clause, no lien, no creditor verb (D-5 holds): possession is the security, and a creditor who keeps a pledge after payment has breached | the house that ends up holding the mines; the prince who cannot pay and cannot get his toll back |
| 11 | **The merchants' own court** | `CGR:117`; `GM:201-202` | `debt_suit` is given a second row that sits in the guildhall (`venue_min_rank: hearth`, `disposal_reach: body`), its bench the guild's `determine` seat anchored there; a suit may be opened before either, and where the benches' members differ their `regard` and `obligation` terms differ. Forum is the suitor's choice. Held if the judging set at a hall cannot be told from the town's (the proposal marks it) | the debtor who is safe in the commune's court and ruined in the guild's |
| 12 | **A guild's rule needs an outside assent** | `CGR:97`, `:129`, `:223` | composed, no key: a statute `issue`d through the guild's hall seat reaches its sworn members only (purview: the hall, one edge deep); to bind the town the head `petition`s the commune's justice seat, whose answer is the ratification, an ask rolled with `obligation` and `regard`. One content condition: the guild's `issue` remit must sit on the hall seat, not on proposal D's duchy-anchored roll seat | the magistrate bought; the entry rule that hardens an exclusion into the town's law |
| 13 | **The body of the excluded** | `CGR:98`; `PGS:81` | a `community`-rung brotherhood with an elected head, a chest and an establishment, whose roll is by warrant and whose head seat is `eligible_from` its own roll only. No tie to the council | the rich citizen's rise where the council's roll is closed to him; a rival establishment in the same town |

**Not taken, with the reason:** a wealth-threshold rank ladder (Patrician IV): rank is by warrant and
ballot (§5.3). A stored tag on a purchased house (`RTP:504`): Layer 1 refuses a stored social quantity; a
purchaser's reception is each person's judgment of his deeds. Scope decay on the secret bench
(`CPS:318`): a row's matter is already what its threshold ballot takes up (§6.2), and a count of
"uncited security cases" would be a second owner of that. The lot for early entry (`PHS:346`): one more
use of `lot`, with no story the roll's own ballot lacks.

### 17.3 What stays memory-grade in this file

Rows V-3, V-5 to V-9, V-14 (the revolt only), V-15, V-18 to V-20, V-22 (for Venice), V-27, V-28, V-31
to V-35, V-38 (the muster), V-41, V-43, V-44, V-47, V-48 of the map, and the parts of V-4, V-10, V-21,
V-29, V-30, V-42, V-46 its table names. In one sentence: the *commenda* and the sea loan, the merchant
galleys, the Monte, the bill of exchange and the bank's legal form, the *catasto* and dowry fund, the
Hanse's constitution, and a list of particulars (family bars, fines, sizes, the muster). The design takes
no number from any of them. §5.2's choice of the fixed-amount debt over the profit-sharing contract was
made on the engine's shape, not on the history, and stands with its source still unopened.

### 17.4 What this does to the plan

Nothing in batches A to D is withdrawn; one remit D authored is narrowed (item 12: the guild's `issue`
moves from the duchy-anchored roll seat to the hall seat, marked as an assumption for FA or Jordan). A
fifth batch, **E**, carries §17.2 (content for items 1 to 7, 9 and 13; one form row for item 8; one
arrangement row for item 11; items 10 and 12 are composed and need only gates). It depends on D, on the colonial lane's `instruments.yaml` (C-1) for items 3, 8 and 10,
and on its `audit` row (C-3) for item 4. The first playable scenario gains one choice and one ending
from items 10 and 8: the head of the house may take a pledge with a loan, and may hire a captain in his
reserve season.
