# INSTITUTIONS · BYZANTINE — the court of precedence, the bureaux and the provincial chain, adapted to a conquest-founded order

## Status: REFERENCE (a design and plan in proposal form under `INSTITUTIONS_BRIEF.md`; resolves nothing at runtime)

## Read at: 84d2a02 (working tree)

Family: the Byzantine empire and its bureaucratic influence, with its cousins (Abbasid, Ottoman, Chinese
examination bureaucracy) where they sharpen a mechanism. Expressed in Valoria in two places the tree
already holds: **the Altonian Empire** (a foreign faction, two seats) and **the imperial apparatus the
Crown inherited from two centuries of Altonian rule** (the organs canon names Imperial Court, Court
Parliament, Ministries, Rectorates and Praefectures). Jordan's fixed point of 2026-11-12 governs the
whole: the crown and the two ducal houses were won by accomplishment in the Secession War, in the order
king, first Duke of Hafenmark, first Duke of Varfell. The exact edits are in six proposals,
`proposals/15_INSTITUTIONS_BYZANTINE_A` to `_F`, listed in §12.

Sourcing marks: `[TREE path]` a finding the repository's research records (itself tier 3); `[MEMORY]`
supplied from general knowledge of the standard literature, not re-verified here, so a shape and never
a figure; `[UNVERIFIED]` not checked. Engine statements cite the file opened. Every instrument reading
names its command and seed in §16.

## 0. Verdict

**The engine can already carry almost the whole of a Byzantine-pattern state, and carries none of it
today, for two reasons that are content and reach, not architecture.** The four things that made that
state work are each an existing primitive: an office is a seat with a remit; a dignity is a seat with
none (the tree's own precedent is the heir, "a TITLE, designated by an ordinary `confer`",
`offices.yaml:258`); the annual stipend that bound the court to the throne is a seat's upkeep paid by
`transfer`, renewing the termed oaths of the persons sworn to it (`loop/effects_economy.py::_renewals`,
with `oblige_term` shipped at 4 seasons, which is one year); and the paperwork chain is a `Record` with
dated `stages` that mature at MATTER (`loop/effects_information.py::_declared_stages`). Rank by
accomplishment is also built: `queries/person_q.py::legitimacy` is a person's stored stance toward a
holder plus what his own pursuits make of the holder's deeds he has heard of. What is absent is that
(a) no seat declares an upkeep, no oath carries a term, and the fisc is empty (`build_realm(0)`: four
live oaths, none termed; `r_valoria`, `terr_T1` and the Altonian post all hold `{}`; E-1), so nobody is
paid and nothing lapses; (b) a decree passes through no hand, so a clerk has nothing to delay; (c) the
founding order Jordan states exists nowhere a person can read it (13 persons hold a stance toward the
King, none toward either duke; no founding record exists, though case NPC-008 turns on the custody of
one; E-1); (d) the empire is two persons with no superior, so nothing can be sandbagged, exceeded or
recalled. **The single largest obstacle is the one the FA lane measured: governance acts execute and
bind nobody (`audits/06_FA_audit.md` F-FA-01, F-FA-02).** A court of precedence built on acts that bind
nobody would be decoration, so this design lands after, and on, the FA lane's three mechanism
proposals. It adds no verb, no carrier and no stored aggregate: three keys on seat rows, one record
kind, one roster key, one arrangement row, three fixtures, and content.

**Nothing in it is decided by rank (the standing rule of `AUDIT_BRIEF.md`, Jordan 2026-11-12: "we do
not do deterministic").** Every procedure the institution runs, an investiture, a recall, a document
passing a hand, a tax collected, an accession, is a draw on the four-band ladder through the one
contest seam, with a recoverable result in every band. Five existing rows that are certain today are
given a draw: `confer`, `revoke`, `carry`, `requisition`, `succeed` (§7.0). The order of precedence
and the founding order are read in exactly two ways: as the amount a seat owes its sworn (arithmetic,
a ledger) and as terms in a draw's odds. Neither is ever a gate, a tie-break or a result. A man of
the first dignity is refused sometimes, and a clerk's protégé is sometimes passed over. What is
arithmetic stays arithmetic: stores are conserved, a term's clock ticks, an eligibility check admits
or refuses the attempt.

## 1. What the tree says these holdings are

### 1.1 The empire

| fact | where | grade |
|---|---|---|
| Altonia conquered the peninsula and ruled it about 150 to 200 years; it "contained" the Church of Solmund by granting it Himmelenger with tax-exempt lands, schooling, archives and charity in exchange for quiescence; it destroyed Valnese records and monuments | `canon/03_canonical_timeline.md:54-68` | canon |
| The three duchies are Altonian colonial provinces renamed; their boundaries are administrative overlays | `.designs/systems/world/reference/worldbuilding_v30.md:219-229` | archived design, D-2 resolved |
| Altonia is a faction since v9 IN-36, seated only by `build_realm(foreign=True)`, with one minted territory `ALT` and one settlement `ALT-1` | `rosters.yaml: foreign_cast`; `offices.yaml: foreign_seats` | code-read data |
| Two seats: `off_katepano` (NPC-089, remit `[dispatch, issue]`) and `off_kommerkiarios` (NPC-090, `[issue]`), both with `conferral: null`, `revocation: null`: "canon names no way the empire fills or strips the post" | `offices.yaml:607-632` | `[ASSUMPTION; medium; Jordan to correct]` |
| A third Altonian, the Doux Alexios Laskaris (NPC-011), is cast and unseated; his goals include "Sandbag imperial directives"; the case seats "the Altonian imperial authority" as a person with no office | `references/npc_registry.yaml:464-506`; `cases/exercises/NPC-011.yaml` | registry; case |
| `altonian_civics` is the fifth affiliation, political and not religious: "the Altonian imperial order as the political structure one wants" | `references/descriptor_registry.yaml:205-228` (ED-IN-0293) | ruled |
| The empire's goal is "Altonia conquers Valoria"; the Katepano presses the capital through Lowenskyst; the Kommerkiarios enforces "the ancient trade treaties" | `goals.yaml:450-493` | code-read data |
| The archetypes the registry names: Basil Boioannes (Katepano), the Book of the Eparch (Kommerkiarios), Manuel II Palaiologos (Doux, "Byzantine governance-as-moral-cultivation") | `npc_registry.yaml` rows above | registry text |
| Altonia's own church, the Almaic Kyriakos, "could not stamp out the Church but could quarantine it"; it appears only in pre-project lore | `.designs/…/geography_v30_infill.md:29`; `worldbuilding_canon_audit_v30_infill.md:40` | archived; no engine carrier |

### 1.2 The inherited apparatus inside the Crown

| fact | where |
|---|---|
| The Crown's organs are named in imperial style: **Imperial Court** ("Advisory. Informal power arena."), **Court Parliament** ("Recommends policies, nominates Ministers/Rectorates/Magistrates."), **Ministries** ("Execute government services."), **Rectorates** ("Judicial. Execute law."), **Praefectures** ("Local governance. Administer regions.") | `rosters.yaml: office_bodies` (`:2219-2276`), quoting `worldbuilding_v30.md` §6.1 |
| The ministry services are Law, Taxation, Guilds, Water/Granaries; a retired patch named the fiscal ministry **Logothetes** | `rosters.yaml:2244-2262` (the Ministries ruling) |
| One Ministries seat is built: the Chief Parliamentary Clerk (NPC-008), remit `[issue]`, whose case is the "custody of the sole surviving record of the founding settlement's terms"; his registry row reads `altonian_civics: 2` because "a bureaucratic order leans Altonian" | `offices.yaml:317-328`; `cases/exercises/NPC-008.yaml`; `npc_registry.yaml:381-384` |
| The Lord Steward (NPC-009) "personally absorbs nearly every important administrative task"; the Lord Treasurer (NPC-037) holds the treasury post | `cases/NPC4.yaml` |
| Hafenmark's "cultural emphasis on institutional order" is attributed to concentrated Altonian oversight | `.designs/…/geography_v30_infill.md:18` |
| Canon's event card "Ministry Collapse: one Ministry ceases to function for 1 season" | `worldbuilding_v30.md:207-213`, `:304` |
| Two thrust axes already name the politics of the residue: `purge_altonia` against `altonian_ascendancy` | `rosters.yaml:2358-2368` |

So the Crown is a kingdom of deed-nobles running an empire's offices. That is the subject of this
design, and it is a known historical configuration (§2.14).

### 1.3 The fixed point, located, and where the tree disagrees with it

Jordan, 2026-11-12: *"current kingdom royalty is because of nobility by deed/achievement"*; *"Royalty by
noble conquest, i.e. the first king had the greatest accomplishment in the secession war, followed by
the first Duke of Hafenmark and the first Duke of Varfell."*

**Where the tree agrees.** `canon/03_canonical_timeline.md:78-92`: "Authority is entirely earned through
wartime deeds"; "Cadet branches as deed-families … The Baralta family's ducal status was earned through
wartime deeds"; "The deed-monarchy stabilises into hereditary monarchy within one generation … But the
deed-presumption is rebuttable"; Almud "has not personally earned the deed-claim — inherits the
presumption his father created". The archived faction canon says the same of the present
(`faction_canon_v30.md:444-449`, intent only): "each successor must continually re-earn it". In code,
`person_q.legitimacy` (`:537-563`) is exactly that sentence: a stored stance with no date, plus the
holder's deeds a person holds claims of **from a window**, so earned standing ages out and presumed
standing does not. `offices.yaml:523` already names one deed certifier: "any Deed-Claim succession in
Varfell needs the Skald-Chief's endorsement".

**Where the tree disagrees, named and not resolved (Jordan's word governs the world; the code governs
the engine).**

| # | the tree says | against the fixed point | what this design does |
|---|---|---|---|
| D-1 | "The coalition is primarily northern — the southern provinces (Lupicco) are geographically peripheral and culturally stigmatised"; the caste is "the structural consequence of the south's exclusion from the war coalition's leadership" (`03_canonical_timeline.md:76`, `:96`) | a first Duke of Varfell whose accomplishment ranked third in that war was not excluded from it | carries the order as stated (third), and makes *who credits it* a content dial (§14 item 2) |
| D-2 | `off_duke_varfell.conferral: elected`, "first among the Jarls, not a monarch" (`offices.yaml:226-237`) | a house won by conquest | no conflict once the standing is the **seat's**: the founding deed attaches to the seat and passes to whoever lawfully fills it, by election as by blood. That is nobility by deed, not by blood |
| D-3 | `off_duchess_hafenmark.conferral: null` and `off_duke_valorsmark.conferral: null`: two founding seats with no rule for how they are filled | a house's standing must be able to pass or fail to pass | named as content debt; `off_duke_valorsmark` is CP-T09-06's edit (`null` → `inheritance`, FA audit R-18); Hafenmark needs an heir title Jordan has not cast |
| D-4 | archived faction canon: "a war of unification" (`faction_canon_v30.md:444`) | the Secession War | wording; canon's timeline governs |
| D-5 | in the built realm 13 persons hold a stance toward the King and none toward either duke; mean regard 0.720, 0.000, 0.000 (E-1) | a ranked order of three | the founding claims of proposal A |
| D-6 | no Record of the founding settlement exists (`records by kind {'works': 2}`, E-1) though NPC-008's case is its custody | "rank as a ranked ledger" | the Roll, proposal A |

## 2. How it really worked

The intricacies are the point. Each subsection ends with **the mechanism**, the one sentence a designer
can build from. Figures are leads (the sourcing floor).

### 2.1 The taxis: two tracks, office and dignity

The order of the court was written down. The *Kletorologion* of Philotheos (899) is a seating list for
imperial banquets, compiled by the official who placed the guests, and it distinguishes **dignities
conferred by insignia** (a codicil, a staff, a collar handed over by the emperor: honorific, for life,
not heritable, about eighteen grades from *spatharios* through *protospatharios*, *patrikios* and
*magistros* up to *kaisar*) from **offices conferred by word** (about sixty posts: generals, domestics,
judges, bureau heads, revocable at will and vacated on dismissal) `[TREE .audit/2026-07-09-comparative-governance-research/comparative_governance_research_v1.md:27; grades and counts MEMORY: Bury 1911, Oikonomides 1972]`.
An office usually came with a dignity; losing the office did not lose the dignity. So the court
produced two states a single ladder cannot: the dismissed man who still outranks his successor at
table, and the favourite in high office with no standing `[TREE ibid. :153, BYZ-1]`. Precedence was
enacted physically: order of entry, of seating, of who is addressed first, of who may sit. A promotion
was a ceremony before the assembled order, with set acclamations.
**The mechanism:** two tenures per person, one revocable and powerful, one sticky and paid; rank is
public, ordered and performed in front of the others.

### 2.2 The roga: salary as a personal bond

Dignity-holders drew an annual stipend in gold, the *roga*, paid in the week before Palm Sunday.
Liudprand of Cremona watched Constantine VII pay it in 950: over three days the emperor handed each
of the highest dignitaries his bags of coin and his robes personally, in rank order; lesser ranks were
paid the following week by the chamberlain `[MEMORY: Antapodosis VI.10; firm]`. A dignity could be
**bought**: an investiture payment in return for the title and a stipend for life, in effect an annuity
the state sold, at a return low for the plain title and higher for supplementary stipends; the cleric
Ktenas paid heavily for a *protospatharios*'s stipend he lived two years to draw
`[TREE ibid. :28; rates MEMORY: Oikonomides, "Title and Income"; figures are leads]`. The stipend was
the throne's largest discretionary outlay and its leash: when eleventh-century emperors debased the
coin and then could not pay, the bond went with the money `[MEMORY]`.
**The mechanism:** the holder of the throne pays, in person, on a yearly clock, by rank; a title is an
income the fisc owes; an unpaid court is an unbound court.

### 2.3 The sekreta: narrow bureaux, each with its own registers

Central government was a set of bureaux (*sekreta*), each under a *logothetes* or equivalent with a
narrow mandate and its own clerks (*chartoularioi*, *notarioi*): the *genikon* (the land tax: its
cadastre, assessment and collection), the *stratiotikon* (the army's rolls and pay), the *dromos* (the
post, foreign envoys, and internal intelligence), the *eidikon* and *vestiarion* (stores, workshops,
the mint), the *sakellarios* as general controller over all their accounts, the *protasekretis* heading
the chancery that drafted, the master of petitions (*epi ton deeseon*), and the keeper of the imperial
inkstand (*epi tou kanikleiou*) `[TREE ibid. :29; roster MEMORY: Bury; Oikonomides]`. No bureau shared
staff with another and none could act on another's matter: the division was a check on accumulation,
and it meant any one act of state needed several bureaux `[TREE ibid. :158, BYZ-5]`. In the Komnenian
period a coordinating *logothetes ton sekreton* was added, a first minister in all but name.
**The mechanism:** authority is split by matter; nobody below the throne can finish anything alone.

### 2.4 The paperwork chain and its delays

A grant or order of the first class, a chrysobull, went through fixed hands: a petition reached the
master of petitions; the chancery drafted; the emperor wrote the validating words in red ink, which
only he might use; the keeper of the inkstand held that ink and so stood at the last step; a gold seal
was hung; and the document was **registered in each bureau it touched**, each adding its own note that
it had been entered. An unregistered privilege could not be claimed against a tax collector who had no
entry of it `[MEMORY: Dölger and Karayannopulos on the imperial chancery; firm as shape]`. Each hand
took a customary fee (*synetheia*), which was most of an official's real income. The chain's delays
were its politics: a bureau that did not enter a grant had refused it without saying so. The Ming
analogue is exact and better documented in the tree: a memorial went to the Grand Secretariat for a
draft rescript and then to the Directorate of Ceremonial, whose seal-holding eunuch added the
vermilion endorsement, so a man holding no office of state controlled what the emperor had "decided"
`[TREE ibid. :50, CHN-7]`. Zhang Juzheng's answer (1573) was three copies of every order with a
deadline, one held by the supervising office that struck it off when the act was reported done
`[TREE ibid., CHN-9 Kaochengfa]`.
**The mechanism:** a decision is in force when it has passed named hands and been entered; each hand
can pass it, sit on it, or change it; the entry is the proof.

### 2.5 The fisc

The land tax was assessed on a cadastre by inspectors (*epoptai*) and collected by others
(*dioiketai*): assessment and collection were separate careers so that neither could invent the
other's numbers. A village was jointly liable: neighbours paid for a defaulter's land (*allelengyon*),
and land abandoned thirty years reverted to the fisc. Collectors added lawful surcharges for their own
pay `[MEMORY: Oikonomides in *The Economic History of Byzantium*; firm as shape]`. Three things
hollowed it. **Exemptions**: a chrysobull of immunity (*exkousseia*) took an estate or a monastery out
of the collector's reach for ever, and each emperor bought support with them. **Tax farming**: from
the eleventh century the right to collect a district was sold for a fixed sum up front, and the farmer
kept the difference; the tree's research has the Roman, Ottoman and French cases and the general
finding that the farmer's incentive is to strip the district within his term
`[TREE research/fa_se_historical_precedent_research_v1.md; .audit/…/comparative_governance_research_v1.md:15]`.
Justinian had already said why when he banned the sale of governorships in 535: a governor who paid
for his post recoups it from the governed `[TREE ibid. :37, Novel 8]`. **The revenue grant**: from
Alexios I the state paid soldiers and officials with *pronoia*, the revocable right to collect a named
district's taxes for life in return for service, which was not ownership and became it within a few
generations `[TREE ibid. :31, :160 BYZ-7; research/rise_to_power_roster_system_research_v1.md:524 for the Ottoman malikane variant]`.
**The mechanism:** income rises from places to the centre through appointed hands; every shortcut that
pays someone with the *source* instead of the *proceeds* is cheap today and permanent tomorrow.

### 2.6 The themes and the provincial chain

A theme was a province under a *strategos* who held both the civil and the military power, with its
soldiers settled on inalienable military lands they held for service `[TREE research/fa_se_historical_precedent_research_v1.md:154]`.
The checks on him were structural. His fiscal officer (the theme's *protonotarios*) and his muster
officer (its *chartoularios*) answered to the bureaux in the capital, not to him; he served a few
years and was moved; large themes that had rebelled were split `[TREE research/proactive_governance_scale_research_v1.md:142, X2; reporting lines and tenure MEMORY: Oikonomides, Treadgold]`.
From the later tenth century several themes and their garrisons were grouped under a *doux* or
*katepano*, stronger against an invader and more dangerous to the throne
`[TREE .audit/…/comparative_governance_research_v1.md:32; proactive_governance :263: consolidation is one setting of a civil/military flag, and the dangerous one]`.
Mountain passes had their own small commands (*kleisourai*) held by settler-soldiers at no cost to the
treasury `[TREE proactive_governance :104]`. The capital kept professional guard regiments (*tagmata*),
created by Constantine V after a theme's army had put its general on the throne, expressly as a
second army loyal to the centre `[TREE .audit/… :34]`.
**The mechanism:** a governor is strong when one man holds sword and purse; the centre's hold on him is
the men under him who are sworn elsewhere, the clock on his posting, and a paid army at home.

### 2.7 The palace: the bedchamber and the throne-barred servant

The emperor's household (the *koiton*) was staffed by eunuchs with their own ladder of dignities and
their own reserved posts: the *parakoimomenos* who slept across the door, the keeper of the wardrobe,
the master of the table, the *praipositos* who ran ceremony. They could never be emperor, which is
why they could be trusted with everything else; Basil Lekapenos governed for five emperors from the
chamberlain's post and was removed in a day when Basil II decided to rule for himself
`[TREE .audit/… :33, BYZ-8; .audit/2026-07-12-governance-compendium/40_roster_officer_system.md:376, D9]`.
Their power was access: a petition, a face, a paper reached the emperor through them. The Ottoman
Chief Harem Eunuch turned the same position into an endowment income of his own; the Ming case ended
in a purge of the whole credentialled class by the man at the chokepoint, and in his own destruction
on the next accession `[TREE compendium 40 :391 E5, :426 G4, :443 H4]`. The tree's standing naming
note: do not call the role "eunuch official"; "Chamberlain", "palace advisor", "oath-bound
administrator" `[TREE research/rise_to_power_roster_system_research_v1.md:394, :440]`.
**The mechanism:** a class of servant made safe by a bar it cannot cross, powerful by standing between
the ruler and everyone else, and destroyed with its patron.

### 2.8 Emperor and patriarch

The patriarch was chosen by the emperor from three names the synod put forward, and emperors
sometimes ignored the list `[TREE .audit/… :36]`. Emperors deposed patriarchs. But the office kept
three weapons: only the patriarch crowned; he could bar the emperor from the church (Polyeuktos made
John Tzimiskes do penance and send away his accomplice before he would crown him, 969; Nicholas
Mystikos shut the doors on Leo VI over a fourth marriage and was deposed for it, 907); and a deposed
patriarch's partisans could refuse communion with his successor for a generation (the Arsenites, after
Michael VIII blinded the boy John IV Laskaris in 1261) `[MEMORY; firm]`. "Caesaropapism" names the
emperor's appointing hand; the record shows a contest the emperor usually won and always paid for.
**The mechanism:** the ruler names the head of the church from a short list the church controls, and
the church's consent to a reign is given once, publicly, at a price.

### 2.9 Succession: by acclamation, by coup, by blinding

There was no law of succession. An emperor was made by the acclamation of army, senate and people and
by coronation; a reigning emperor could crown a son co-emperor, and birth in the purple chamber gave a
child a presumption no usurper had. A successful usurper was emperor; a failed one was a "tyrant".
Usurpers therefore married into the old house or ruled as guardians of its children (Romanos I,
Nikephoros II, John I beside the Macedonian heirs), and the capital could rise for the house against
the man: in 1042 the city's crowd deposed and blinded Michael V for exiling the born-in-the-purple
Zoe `[MEMORY; firm]`. A rival was removed without killing him: **blinding** or other mutilation
disqualified him for the throne for ever, and **tonsure** removed him into a monastery; the tree's
research records the paired Roman finding that usurpation needed two triggers at once, strain and a
legitimating occasion `[TREE research/governance/00_MANIFEST.md:59; conflicts_power_struggles.md]`.
The tree also holds the long consequence: each civil war was the next invader's opening, the invader
"enters as an ally of one side … then remains" `[TREE research/historical/precedents_analysis.md:66]`.
**The mechanism:** legitimacy is success, recognised by three constituencies and one priest; the old
house keeps a presumption the successful man must borrow; the loser is made ineligible, not dead.

### 2.10 The demes of the hippodrome

The Blues and Greens were organised bodies of the capital's populace with officers, funds and a place
in every ceremony: they performed the acclamations. The hippodrome was the one room in which emperor
and people were both present, so it was where the people shouted for a minister's dismissal or a
tax's repeal, and where in 532 the two factions joined and nearly ended a reign. By the tenth century
their role was ceremonial and salaried, which is its own lesson: a crowd given a part in the ritual
is a crowd the ritual can count `[MEMORY; Alan Cameron, *Circus Factions*; firm as shape]`.
**The mechanism:** a public occasion with an open floor where standing is performed to the crowd and
the crowd answers.

### 2.11 Guard, army and throne

Three armed bodies stood in different relations to the emperor: provincial armies loyal to their
general, the capital's regiments loyal to their pay, and from 988 a foreign guard (the Varangians)
sworn to the throne itself, noted for serving whoever lawfully sat on it `[MEMORY; firm as shape]`.
The eleventh century's politics was the provincial military houses against the capital's civil
officials, each starving the other: the bureaux cut the armies' pay, the generals took the throne
(1057, 1081) and governed through their kin `[TREE .audit/… :35, the Komnenian *sebastos* titles as a kinship-distance ladder]`.
**The mechanism:** an oath to a person, an oath to a paymaster, and an oath to a seat are three
different loyalties, and a coup is the moment they diverge.

### 2.12 Power at a distance

The empire governed its neighbours with paper, titles and guests more than with armies. Foreign
rulers were given court dignities and the stipends that went with them, which made them clients on
the roll; their sons were educated at court, as guests and as hostages; brides were sent out
sparingly; and trade was let in through named gates only, where *kommerkiarioi* with their own seals
took the duty and enforced the treaty's lists `[MEMORY: *De Administrando Imperio*; the Book of the Eparch is TREE .audit/… :30]`.
A treaty of privilege was a chrysobull like any other grant, and it decayed like one: the exemption
from duty given to Venice in 1082 for a fleet starved the customs and the native merchants for a
century and ended in 1204 `[MEMORY for 1082; TREE research/fa_se_historical_precedent_research_v1.md:45 for 1204 as the tree's anchor]`.
Orders to a frontier governor took weeks; he acted on the last one he had.
**The mechanism:** clientage by title and stipend; heirs as pupils; trade through a gate with a named
keeper; and a governor far enough away that his orders are always old.

### 2.13 The cousins, for what each adds

| tradition | what it adds to the Byzantine shape | source |
|---|---|---|
| Abbasid | an **audit bureau** set over the others; the ruler's or vizier's **court of complaints** against officials (*mazalim*); the routine **fining of a dismissed official** to recover what he took; the post-master as the centre's eyes in each province; slave soldiers who became the government | `[MEMORY]` |
| Ottoman | servants of the ruler who can found no house (the *kul*); revenue grants rotated so they do not root (*timar*); tax farms sold for life (*malikane*) and the entrenchment race that follows; the grand vizier as the scapegoat who absorbs a failure; the guard's revolt as a veto | `[TREE research/governance/*.md; rise_to_power :524; FA lane file T-FA-3]` |
| Chinese examination state | office by **credential**, earned in stages and held by cohort; the **rule of avoidance** (no man governs his home district); the magistrate whose formal power is whole and whose real capacity is his unranked clerks; orders in triplicate with deadlines; the censor who may accuse anyone | `[TREE .audit/… :41-51, CHN-1..9]` |

The tree's standing limit on the last: the Mandate of Heaven is history only and never a Valoria
mechanic `[TREE research/governance/00_MANIFEST.md]`. This design uses none of it; legitimacy here is
deed.

### 2.14 A conquest-founded order on an imperial apparatus

The case Valoria is, by canon and by Jordan's fixed point, is a recurring one. The Ostrogothic kings
kept the Roman bureaux and staffed them with Romans while Goths held the army; the Norman kings of
Sicily, crowned in 1130 with a papal party's blessing, kept the Greek and Arabic fiscal offices with
their registers of land and men, staffed them with Greeks, Arabs and palace eunuchs, and kept beside
them a roll of what each baron owed in knights; Serbian and Bulgarian rulers handed Byzantine
dignities to their own war-nobility `[MEMORY: Cassiodorus' *Variae*; Johns, *Arabic Administration in Norman Sicily*; the *Catalogus Baronum*; firm as shape, no figure used]`.
The shape is constant across them:

1. **The conquerors hold land and arms by deed, in an order fixed at the conquest** and recorded as
   service owed. Rank among them is what each did, and each house is owed its place.
2. **The inherited bureaux hold the registers, the routine and the memory.** The clerks have no deed
   and no arms; the barons cannot read the cadastre. Each needs the other and each resents it.
3. **The king is the only person in both orders**, and uses each against the other: offices and
   stipends to bind nobles to the court, clerks who can found no house to check them. His chief
   minister is the first man the barons kill (Maio of Bari, 1160).
4. **The founding order goes stale.** Sons hold what fathers won; new men do new deeds and are not on
   the roll; the court's titles drift from the war's ranking. Renewal is by a new entry, bought by a
   new deed, and it passes through the clerks.
5. **The church consecrates the first king and is paid for it for ever.** Canon's own parallel is the
   Carolingian one (`03_canonical_timeline.md:84`).

Points 1 to 5 are what §6 builds.

*(continues)*
