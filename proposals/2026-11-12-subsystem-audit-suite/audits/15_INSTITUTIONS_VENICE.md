# INSTITUTIONS / VENICE — the merchant republic, the banking house and the league: design and implementation plan

## Status: REFERENCE (a design and plan in proposal form; resolves nothing at runtime, CLAUDE.md §0.05)

## Read at: bb6dfc3 (working tree)

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
permanent `[T: ibid. 1.6; research/governance/conflicts_power_struggles.md §Venice 3.2–3.3]`. The pattern to
carry into the game is the **ratchet**: each failure writes a new clause into a standing instrument, and
the instrument is read at the next accession.

### 1.2 The Doge and his constraints

- **Elected for life, never hereditary; no succession interest.** Sons and brothers of a sitting Doge
  were barred from the main councils and from benefices during his reign `[M]`.
- **The *promissione ducale*.** A written oath enumerating what the Doge may not do, sworn at accession
  and **re-drafted and lengthened at every accession** by the *Correttori alla Promissione Ducale*, whose
  task was to close whatever the last Doge had got away with `[T: governance_modes.md §Venice 1.3]`.
- **Constraints in the text.** He could not open diplomatic letters or receive envoys except with his
  councillors present; could not leave the city, own property abroad, trade, accept gifts, or correspond
  privately with foreign powers; had one vote and no veto `[T: ibid.; M for trade and gifts]`.
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
  political_hierarchy_standing.md §Venice 2.2]`. The body was every adult male patrician (some 1,000 to
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

`[M]` throughout (Lane; Puga and Trefler 2014; Pryor), shapes only.

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

- **A chain of ports, not a territory**: Istria and Dalmatia, Corfu, Modon and Coron ("the eyes of the
  Republic"), Crete, Negroponte, later Cyprus; a *bailo* at Constantinople with jurisdiction over Venetians
  there.
- **Governed by rotation from the centre.** Each place had a **rector** (duke of Candia, *bailo*, *podestà*,
  *castellan*, *provveditore*) elected in the Great Council for about two years, with councillors beside
  him, a written **commission** stating what he may and may not do, **no local marriage, land or trade**,
  and a duty to report by dispatch. Local law and local councils were left in place under him.
- **Audited after the fact**: travelling **syndics** (*sindici inquisitori*) heard complaints from subjects
  against rectors and could try them on return; a rector's final *relazione* was read to the Senate.
- **Split authority** (the tree's X8): in a subject city the *podestà* held justice and the *capitano* the
  garrison and the purse; some verbs rose to the centre, some stayed with the local council.
- **How it broke**: Crete, 1363, the **revolt of St Titus**, in which the *Venetian settlers themselves*,
  holding fiefs for military service, rose with the Greek lords against a new tax levied without their
  consent; put down with a hired army.
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

### 1.9 The ban on armed power at home

`[M]`, with `[T]` for Carmagnola.

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

`[M]` for detail (Preto; Iordanou), `[T]` for the bench.

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

`[M]` (Mueller; Lane; Pezzolo), shapes only.

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
  veduto/seduto]`.
- **Outsider magistrates.** The *podestà* and the Captain of the People were foreigners hired for six
  months with their own staff, forbidden local ties, and **audited at the end of term** (the *sindacato*)
  before they were paid and released `[T: ibid. 1.7; M for sindacato]`.
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

`[M]` (D. Kent; Padgett and Ansell 1993), `[T]` for the pillars.

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

`[M]` (de Roover), shapes only.

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
  a preacher's party a legal instrument (§2.8) `[M]`.

### 2.6 The condottieri

`[M]` (Mallett), `[T]` for Sforza and Carmagnola.

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
  waiting on the border.
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

### 2.9 The wider city-state pattern

- **Milan**: lordship by seizure, legitimated by an imperial vicariate, converted to a hereditary duchy
  **by purchase** (1395); extinct line → a republic with no army → its own hired captain `[T:
  governance_modes.md §Milan]`.
- **Genoa**: a neutral head with no force of his own among armed clan-federations (*alberghi*); chronic
  deposition; **repeated voluntary submission to a foreign lord** as a way out; and the **Casa di San
  Giorgio**, a corporation of the state's creditors that took over revenues and then territories in
  satisfaction of the debt `[T: governance_modes.md §Genoa; M for San Giorgio]`.
- **1494**: none of it survives the arrival of a consolidated kingdom `[T: governance_modes.md §5]`.

---

## 3. How it really worked — the Hanse and the merchant guild

`[M]` (Dollinger; Greif, Milgrom and Weingast 1994; Ogilvie for the sceptical reading); the tree's
treatment is the Kontor as an organisation proposal `[T: research/proactive_governance_scale_research_v1.md O7]`.

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
