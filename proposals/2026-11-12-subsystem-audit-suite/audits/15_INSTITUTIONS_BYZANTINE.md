# INSTITUTIONS · BYZANTINE — the court of precedence, the bureaux and the provincial chain, adapted to a conquest-founded order

Reconciled: 2026-11-12 by `audits/15_INSTITUTIONS_SYNTHESIS.md` §2 — where this file's names, homes or shapes differ from that ledger, the ledger governs: no Record kind `roll` and no `offices.yaml: founding:` section (X-01, X-03, X-04: the founding papers are seeded instruments, and "the Roll" is the Settlement in the clerk's keeping); the founding order is three founders' seeded deeds, and the presumption of §6.2 is the chain term of `legitimacy`, discounted per holder (X-05, X-06); the five draws of §7.0 are their verb lanes' rows, with this file's odds sources as named terms (X-19, X-23 to X-27); the far superior is one seat shared with the colonial lane (X-13); the stipend is billed in `default_store_kind` (X-30); the scenarios are case files (X-32). Of §14: item 2 is the synthesis's §10 item 1; items 1, 3 and 4 are closed there with their ladder steps. Every finding below stands.

Re-grounded: 2026-11-12 against the tree's own research (Jordan: *"Research should have been found in /research or /proposals"*). What changed: (1) the §15 null "the tree has no Byzantine research of its own depth" is corrected in §18.1: the three-file governance corpus omits Byzantium by its own manifest, and nine other files treat it (map: `unified/RESEARCH_MAP_INSTITUTIONS_A.md` §1); (2) every `[MEMORY]` mark in §2 now carries either its tree source at `path:line` or the words "stays memory-grade" with the search that found nothing (§18.2); (3) five statements are corrected where the tree's source differs (§18.3: the later verdicts on BYZ-1, BYZ-7, BYZ-8, BYZ-9; Basil Lekapenos' fall; the Liudprand date; the Laskaris archetype; X1's over-claim); (4) eleven mechanisms the research describes and this design lacked are added in §18.4, with the executable plan in `proposals/15_INSTITUTIONS_BYZANTINE_grounding_mechanisms.md`; (5) what remains memory-grade is listed in §18.5. No finding of this file is deleted; marks are amended in place and the additions are §18.

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
(a) no seat declares an upkeep, nothing tells a seat-holder that a term sworn to his seat is falling
due, and the fisc is empty (`build_realm(0)`: four live oaths, none termed; `r_valoria`, `terr_T1` and
the Altonian post all hold `{}`; E-1), so nobody is paid for anything; (b) a decree passes through no hand, so a clerk has nothing to delay; (c) the
founding order Jordan states exists nowhere a person can read it (13 persons hold a stance toward the
King, none toward either duke; no founding record exists, though case NPC-008 turns on the custody of
one; E-1); (d) the empire is two persons with no superior, so nothing can be sandbagged, exceeded or
recalled. **The single largest obstacle is the one the FA lane measured: governance acts execute and
bind nobody (`audits/06_FA_audit.md` F-FA-01, F-FA-02).** A court of precedence built on acts that bind
nobody would be decoration, so this design lands after, and on, the FA lane's three mechanism
proposals. It adds no verb, no carrier, no tenure kind and no stored aggregate: four keys on seat rows
(`dignity`, `upkeep`, `passes_through`, `hand_term`), one section of `offices.yaml` (`founding`), one
record kind (`roll`), one roster map, one arrangement row, five fixtures, and content.

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
was a ceremony before the assembled order, with set acclamations
`[RE-GROUNDED: TREE proposals/2026-09-05-proceedings-subsystem/source/06-part-V-dossiers.md:39 (Liudprand, 968: "the seating below a Bulgarian envoy"); research/by_lane/SC_social_contest.md:59 ("Seating, precedence and audience are negotiated before speech", graded sound, with `attend / not attend` as the lever); research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md:123, :502 (the scripted imperial oration, which "excludes anything ambiguous or disputed"). The grades and counts above stay memory-grade: the tree's row is abridged]`.
**The mechanism:** two tenures per person, one revocable and powerful, one sticky and paid; rank is
public, ordered and performed in front of the others.

### 2.2 The roga: salary as a personal bond

Dignity-holders drew an annual stipend in gold, the *roga*, paid in the week before Palm Sunday.
Liudprand of Cremona watched Constantine VII pay it in 950: over three days the emperor handed each
of the highest dignitaries his bags of coin and his robes personally, in rank order; lesser ranks were
paid the following week by the chamberlain `[MEMORY: Antapodosis VI.10; firm. RE-GROUNDED: stays memory-grade. The tree holds Liudprand in 23 files, always for the receptions: the embassy "of 949 under Constantine VII" (*Antapodosis*) and of 968 (*Relatio*), proposals/2026-09-05-proceedings-subsystem/source/03-part-II-scenario.md:73; no file describes the payment of the stipend, and the tree's date for the embassy is 949]`. A dignity could be
**bought**: an investiture payment in return for the title and a stipend for life, in effect an annuity
the state sold, at a return low for the plain title and higher for supplementary stipends; the cleric
Ktenas paid heavily for a *protospatharios*'s stipend he lived two years to draw
`[TREE ibid. :28; rates MEMORY: Oikonomides, "Title and Income"; figures are leads. RE-GROUNDED: the tree's row does carry the price, "60 litrai of gold (~19.4 kg, roughly 60x the annual roga owed to a protospatharios)", a lead; "lived two years" is not in the tree's (abridged) cell and stays memory-grade]`. The stipend was
the throne's largest discretionary outlay and its leash: when eleventh-century emperors debased the
coin and then could not pay, the bond went with the money `[MEMORY. RE-GROUNDED: the Byzantine debasement stays memory-grade; the mechanism has tree sources in other polities: "The standing currency debases when rank-holders outrun it" (research/governance/political_hierarchy_standing.md:20); the Kamakura bond that "required the shogun to have a continuous supply of confiscatable/conquerable land to keep paying out … or the bond decayed" (:457); and one shipped game: RTK XIV, "stipend rises with the officer's Civil Service/Title … lowering a service lowers loyalty" (research/game_precedent_suite/tutorials/T13_koei.md:78)]`.
**The mechanism:** the holder of the throne pays, in person, on a yearly clock, by rank; a title is an
income the fisc owes; an unpaid court is an unbound court.

### 2.3 The sekreta: narrow bureaux, each with its own registers

Central government was a set of bureaux (*sekreta*), each under a *logothetes* or equivalent with a
narrow mandate and its own clerks (*chartoularioi*, *notarioi*): the *genikon* (the land tax: its
cadastre, assessment and collection), the *stratiotikon* (the army's rolls and pay), the *dromos* (the
post, foreign envoys, and internal intelligence), the *eidikon* and *vestiarion* (stores, workshops,
the mint), the *sakellarios* as general controller over all their accounts, the *protasekretis* heading
the chancery that drafted, the master of petitions (*epi ton deeseon*), and the keeper of the imperial
inkstand (*epi tou kanikleiou*) `[TREE ibid. :29; roster MEMORY: Bury; Oikonomides. RE-GROUNDED: the tree's row names the *genikon*, the *dromos* and the coordinating *logothetes ton sekreton* only, on Wikipedia pages; the rest of the roster stays memory-grade. The archived design had already applied the form inside Valoria: "Each Cardinal Arm manages a Dicastery (Byzantine-style Sekretum)", .designs/systems/factions/reference/faction_politics_v30.md:965]`. No bureau shared
staff with another and none could act on another's matter: the division was a check on accumulation,
and it meant any one act of state needed several bureaux `[TREE ibid. :158, BYZ-5. RE-GROUNDED: that line is the judgment pass CUTTING BYZ-5 ("Redundant-in-kind with HAB-4"), confirmed keep-cut at .audit/2026-07-12-governance-compendium/tier3_proposal_status_closure.md:151; the history is the tree's, the mechanic was refused there]`. In the Komnenian
period a coordinating *logothetes ton sekreton* was added, a first minister in all but name.
**The mechanism:** authority is split by matter; nobody below the throne can finish anything alone.

### 2.4 The paperwork chain and its delays

A grant or order of the first class, a chrysobull, went through fixed hands: a petition reached the
master of petitions; the chancery drafted; the emperor wrote the validating words in red ink, which
only he might use; the keeper of the inkstand held that ink and so stood at the last step; a gold seal
was hung; and the document was **registered in each bureau it touched**, each adding its own note that
it had been entered. An unregistered privilege could not be claimed against a tax collector who had no
entry of it `[MEMORY: Dölger and Karayannopulos on the imperial chancery; firm as shape. RE-GROUNDED: stays memory-grade (no file holds *chrysobull*, *protasekretis*, *kanikleiou* or *synetheia*). The tree's sourced chains are cousins: the Ming draft-then-vermilion chain (ibid. :50); the Ottoman *nişancı* and the recallable seal (research/governance/governance_modes.md:68-69); the papal chancery's five-part letter and the petition whose carrier "shaped its success" (research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md:242-253, :305); the fee-taking hand as a purchased toll-post (research/rise_to_power_roster_system_research_v1.md:493-497)]`. Each hand
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
pay `[MEMORY: Oikonomides in *The Economic History of Byzantium*; firm as shape. RE-GROUNDED: stays memory-grade (no file holds *allelengyon*, *epoptai*, *dioiketai* or *exkousseia*). Joint liability is tree-grounded elsewhere: the Book of the Eparch's guarantors (ibid. :30, BYZ-3) and the five-household groups (ibid. :64); a survey that fixes a baseline usable as evidence is T7 (.audit/2026-07-12-governance-compendium/41_proactive_scale_menus.md:157)]`. Three things
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
soldiers settled on inalienable military lands they held for service `[TREE research/fa_se_historical_precedent_research_v1.md:154; RE-GROUNDED: also research/pre_firearms_formations/03_early_medieval.md:22 ("the state grants land that produces soldiers"; its "roughly 30 themes … 4,000–10,000 troops" is a lead)]`.
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
`[RE-GROUNDED, corrected: the tree gives no "in a day". research/rise_to_power_roster_system_research_v1.md:256-258 (D9): "he served five"; the 985 removal was "distinctively non-violent … the adult ruler exercising ordinary authority once the regency need lapsed"; :406-408 (G7): the fall is triggered "not by a rival or succession but by the new ruler's own ambition", a "soft, near-inevitable, gentle/exile-grade fall". §18.4 item 4 builds from that reading]`
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
Michael VIII blinded the boy John IV Laskaris in 1261) `[MEMORY; firm. RE-GROUNDED: stays memory-grade (no file holds Polyeuktos, Mystikos or the Arsenites). The tree's sourced forms of the same bargain: Leo I "the first crowned by the Patriarch" (research/social_contest_procedures/04_decision_procedure_catalog.md:71); the anointings of 751 and 754 and the 799–812 dispute after the coronation of 800 (research/governance/governance_modes.md:142-147); and the Ecumenical Patriarch under the Ottomans as "simultaneously religious authorities and state-recognized civil administrators" (:76), which is canon's containment of the Church at Himmelenger in another empire's hands]`. "Caesaropapism" names the
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
Zoe `[MEMORY; firm. RE-GROUNDED in part: "No formal rule existed; hereditary succession was custom, not law", the routes by army, people, Senate and king-maker, the stages (proclamation in camp or Hippodrome, the shield, coronation by the Patriarch) and the failure mode "rival simultaneous acclamations; the acclamation often only ratified a fait accompli" are TREE research/social_contest_procedures/04_decision_procedure_catalog.md:71, which also says of the Senate's part "I don't know it". The marriages into the old house and 1042 stay memory-grade]`. A rival was removed without killing him: **blinding** or other mutilation
disqualified him for the throne for ever, and **tonsure** removed him into a monastery; the tree's
research records the paired Roman finding that usurpation needed two triggers at once, strain and a
legitimating occasion `[TREE research/governance/00_MANIFEST.md:59; conflicts_power_struggles.md. RE-GROUNDED: at :14 ("a frontier defeat or fiscal shock *plus* a legion's acclamation ritual"); a single-source shape, graded "UNREACHED (one source)" with "no game corroborates two signals" at research/by_lane/FA_faction_actions.md:283. The tree's sourced blinding is Carolingian, not Byzantine: Bernard of Italy, 818, "a mitigation of a death sentence", of which he died and for which the king did public penance (research/governance/political_hierarchy_standing.md:191); tonsure as deposition is Childeric III, 751 (governance_modes.md:142). Byzantine blinding and tonsure stay memory-grade]`.
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
is a crowd the ritual can count `[MEMORY; Alan Cameron, *Circus Factions*; firm as shape. RE-GROUNDED: stays memory-grade. The tree has the Hippodrome only as a place of proclamation (research/social_contest_procedures/04_decision_procedure_catalog.md:71) and "circus factions with a claimant" as one strife family (proposals/2026-11-04-strife-flows/00_MASTER.md:34)]`.
**The mechanism:** a public occasion with an open floor where standing is performed to the crowd and
the crowd answers.

### 2.11 Guard, army and throne

Three armed bodies stood in different relations to the emperor: provincial armies loyal to their
general, the capital's regiments loyal to their pay, and from 988 a foreign guard (the Varangians)
sworn to the throne itself, noted for serving whoever lawfully sat on it `[MEMORY; firm as shape. RE-GROUNDED: the date and the paid capital regiments are TREE research/pre_firearms_formations/03_early_medieval.md:24 ("the imperial Varangian Guard from ~988 onward"); the guard's loyalty to the seat stays memory-grade. What the divergence of the three loyalties looks like on a field is also the tree's: Manzikert, 1071, "a doctrinally adequate army losing because internal politics or unclear command produces non-execution" (04_high_medieval.md:156)]`.
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
took the duty and enforced the treaty's lists `[MEMORY: *De Administrando Imperio*; the Book of the Eparch is TREE .audit/… :30. RE-GROUNDED: the protocol is TREE research/rhetoric_oratory_contest/rhetoric_oratory_contest_research.md:127 ("a graded protocol of precedence, gifts, and staged audience — diplomacy as ritual hierarchy rather than free negotiation"); the clientage by payment is proposals/2026-09-05-proceedings-subsystem/source/06-part-V-dossiers.md:39 ("Payments made to avoid war were recorded as imperial largesse"; "the excerpts on embassies constitute a precedent file"); hostage heirs have a sourced cousin in *sankin-kotai* (.audit/… :63). The *kommerkiarioi* and their seals stay memory-grade]`.
A treaty of privilege was a chrysobull like any other grant, and it decayed like one: the exemption
from duty given to Venice in 1082 for a fleet starved the customs and the native merchants for a
century and ended in 1204 `[MEMORY for 1082; TREE research/fa_se_historical_precedent_research_v1.md:45 for 1204 as the tree's anchor]`.
Orders to a frontier governor took weeks; he acted on the last one he had.
**The mechanism:** clientage by title and stipend; heirs as pupils; trade through a gate with a named
keeper; and a governor far enough away that his orders are always old.

### 2.13 The cousins, for what each adds

| tradition | what it adds to the Byzantine shape | source |
|---|---|---|
| Abbasid | an **audit bureau** set over the others; the ruler's or vizier's **court of complaints** against officials (*mazalim*); the routine **fining of a dismissed official** to recover what he took; the post-master as the centre's eyes in each province; slave soldiers who became the government | `[MEMORY]`. RE-GROUNDED: the Abbasid particulars stay memory-grade (no file holds *mazalim*); each mechanism has a tree source in another polity: the audit set over the others is the Censorate and the residencia (`research/fa_se_historical_precedent_research_v1.md:127-128`); recovery from a departed official is the Venetian posthumous audit, with fines "against his estate before his heirs could inherit" (`research/governance/governance_modes.md:329`) |
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
dignities to their own war-nobility `[MEMORY: Cassiodorus' *Variae*; Johns, *Arabic Administration in Norman Sicily*; the *Catalogus Baronum*; firm as shape, no figure used. RE-GROUNDED: these three cases stay memory-grade (no file treats them). The tree holds the configuration in three other places, each sourced: the Salian *ministeriales*, an unfree service class staffed "as a deliberate counterweight to over-mighty free princes", whose elevation was itself the grievance of the Saxon revolt and who rose into the nobility within two centuries (research/governance/governance_modes.md:233-235; conflicts_power_struggles.md:208-209); Venice's *cittadini originari*, "formally barred from patrician political office" with "an effective monopoly on the professional civil service" (.audit/… :96); and the Carolingian household-as-state (governance_modes.md:150)]`.
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

## 3. Adaptation: what is kept, what is changed, and why

| piece | kept | changed | why |
|---|---|---|---|
| Office and dignity (§2.1) | two tenures per person; the dignity outlives the office | no `Title` type: a dignity is a seat row with `remit_acts: []` and a `dignity:` grade, exactly as `off_heir` already is | Layer 1 §B.7 ("there is no `Title` type", `offices.yaml:8`); IN-61's precedent |
| Promotion by ceremony | public, before the order, citing why | the "why" is a **deed the conferrer holds a claim of**; the ceremony is the draw of `confer` and what it publishes | the fixed point: rank is recognised accomplishment; §0.05: the reason must be a thing code reads |
| The roga (§2.2) | yearly, by rank, from the conferring seat, in person | no ceremony object: `transfer` through the seat, renewing termed oaths | `_renewals` is built; `oblige_term` is already a year |
| Purchase of dignity | possible, and corrosive | no purchase rule: a payment is itself a deed (`transfer.made`) a conferrer may cite; each observer judges that deed by his own pursuits | no second route to rank (an S defect); the corruption is legible because the citation is public |
| The sekreta (§2.3) | no seat finishes an act of state alone | not seven bureaux: **the bodies canon already names**, with one seat each until a seat needs more | the Ministries ruling (`rosters.yaml:2261`): "ONE `Ministries` ROW STANDS until a seat needs a ministry" |
| The paperwork chain (§2.4) | named hands; entry is proof; a hand may pass, hold or return | hands are `Record.stages` labels; passing is the existing verb `carry`, drawn; fees are not a rule (a gift moves the clerk's regard, which sets his odds and his ranking) | reuse; fees as a rule would be a second currency |
| The fisc (§2.5) | income rises through appointed hands; the shortcut that pays with the source is the decay | `requisition` drawn and graded; no cadastre object beyond `survey`'s Record; tax-farm and revenue-grant are **later, design-first** | they need SE's stores to mean something first (`07_SE_treasury_granary_B.md`) |
| Themes (§2.6) | one man with sword and purse is strong and dangerous; the centre holds him by other men's oaths, a clock and a home army | "consolidated command" is a seat row naming both `dispatch` and `issue`; the centre's line is an `oblige` from the provincial fiscal seat to the central one | `06_FA_remit_grant_by_row.md` makes remit a row's; `gate.py::purview_reaches`' oath clause (IN-40) is the reporting line |
| The throne-barred servant (§2.7) | safe because barred, strong by access, falls with the patron | no body, no mutilation: a **bar the person takes on by oath** (a seat row whose `binds` names it). Named "chamberlain" | the tree's naming note; AX-1 (a person's own act); whether the Crown has such an order at all is §14 item 4 |
| Emperor and patriarch (§2.8) | short list, then appointment; consent given once, at a price | **not built here**: stated as an interface to the papacy lane; the Church of Solmund is co-sovereign in canon, so caesaropapism is a position persons hold (Baralta), not the realm's rule | canon (`03_canonical_timeline.md:82`, `:105`); FA audit §11 item 3 |
| Succession (§2.9) | legitimacy is success recognised by constituencies; the old house's presumption; ineligibility, not death | acclamation is the draw of `succeed`; the heir's title is odds, not outcome; blinding and tonsure are the existing `ban` | the standing rule; RS-27 ("the heir still has to claim their throne"); `ban` is built |
| The demes (§2.10) | an open-floor occasion where standing is performed to a crowd that answers | cohorts are the crowd (`cohorts.yaml`); one arrangement row, `acclamation`; no faction of the circus | ED-IN-0255 (a population is a person at weight above one) |
| Guard and army (§2.11) | oath to person, to pay, to seat | all three are `oblige` edges differing in object and term; nothing new | `offices.yaml:196` already swears the Grand Master to `off_king`, the seat |
| Power at distance (§2.12) | titles and stipends to clients; heirs as pupils; a gate with a keeper; old orders | the centre is **one authored person** off the map; distance is the term of a hand; the treaty is `covenant` | ARCS adjudication row 12 ("generate a person"); FA's CP-T09-03 |
| Mandate of Heaven; a state church for Altonia; eunuchs as a caste; the hippodrome as a place | nothing | cut | the tree's own limit; no carrier in canon; the naming note; no venue need the `acclamation` row does not meet |

**Canon check (P-01 to P-15, `canon/02_canon_constraints.md:42-56`).** The foundations govern the
Thread, rendering and monstrosity; this design touches three. *P-08 and P-13* (the Forgetting is an
epistemological barrier, not record destruction): the Roll and every register are `mundane` knowledge
(`rosters.yaml: knowledge_kinds`); no document here carries, restores or gates Thread knowledge, and the
Altonian destruction of records stays a political grievance (`03_canonical_timeline.md:66`). *P-04* (no
alignment): the empire is an order some persons want (`altonian_civics`) and others want purged; no
row marks it villainous. *GD-1* (`04_game_design_constraints.md:27`): one victory path; nothing here
adds an ending, and "Altonian Theocracy" stays struck. No conflict found.

## 4. Commensurate: every quantity in a unit the engine already has

| institutional quantity | engine unit | owner (the file code reads) | sweep |
|---|---|---|---|
| a deed | an event-kind claim `(doer, kind, True)` in a ledger, scored by `deed_term` | `queries/person_q.py`; kinds from `data/verbs.py::DEED_KINDS` | none (exists) |
| a founding deed | the same claim with a **seat** as its subject | authored once in `offices.yaml: founding`, deposited at build | confidence by order: 1.0 / 0.8 / 0.6 of full (A); flat (control) |
| presumption | a term of `legitimacy`, `presumption_gain` × Σ founding claims | `data/fixtures.py: presumption_gain` (new) | 0 (control) / 0.5 / 1.0 |
| dignity grade | an int 1 to 5 on a seat row | `offices.yaml: seats[].dignity` (new key) | 3, 5, 7 grades |
| stipend | units of `coin` per sworn person per term | `offices.yaml: seats[].upkeep` → `Office.upkeep` (field exists, `carriers.py:1052`) | H-158's 0 / 1 / 3 as the base; by grade 1, 1, 2, 3, 5 |
| the pay year | 4 seasons | `fixtures: oblige_term` (exists, shipped 4, H-159) | None / 1 / 4 |
| a hand's patience | seasons a document may sit with a body | `rosters.yaml: office_bodies.term` (new map), default `fixtures: record_stage_term` (exists, 1) | 1 / 2 / 4 |
| distance to the centre | the same: the term of the body that carries the post | same | 1 / 2 / 4 |
| tax | units of a `matter_kinds` member moved rung to rung | `requisition` (`Rung.stores`, conserved) | amount by degree: 1, 1, ½, 0 |
| degree of any procedure | Overwhelming · Success · Partial · Failure | `engine/dice_engine/dice_engine.py::degree_from_net` | none |
| odds of any procedure | pool = `faculty(w, p, verb)`; obstacle = difficulty + named modifiers | `seam/wrappers/pool.py`; `modules/social_contest/roll.py::obstacle` in the form `05_SC_obstacle_difficulty_and_modifiers_B.md` gives it | per term, as that proposal sweeps |
| scale | the seat's rung, a `rung_kinds` member | `offices.yaml: seats[].rung` | none |
| publicity | an arrangement's `floor` and who is present | `arrangements.yaml` | open / closed |

One ladder of degrees, one pool-and-obstacle form, the eight rungs, the season, the five matter kinds.
Nothing is denominated in a private unit: there is no "prestige", "influence" or "court favour" stock.
Favour is one person's regard for another, computed when read (`person_q.regard`).

## 5. The play-facing model: primitives reused, and the three additions with their cut tests

| primitive | exists as | this design's use |
|---|---|---|
| seat | `Office` row (`offices.yaml`) | offices, dignities, hands of the chain, the centre |
| body | `rosters.yaml: office_bodies` | the bureaux; a hand is a body |
| procedure | `arrangements.yaml` row | `acclamation` (new row); enrolment under `parliamentary_debate` |
| instrument | `Record` of a `record_kinds` kind, with `stages` | writs, petitions, treaties, the Roll |
| claim | `Claim` in a ledger | deeds, founding deeds, a clerk's reason for a return |
| obligation | `oblige` Tenure with a `term` | the stipend bond; the reporting line; the guard's oath |
| patron-client edge | no edge: `regard` (stance + deeds) plus an `oblige` where sworn | patronage is regard earned by conferrals and gifts, read by the odds and by the chooser |
| treasury | `Rung.stores` at the seat's rung | the fisc |
| jurisdiction | `gate.py::purview_reaches` (containment plus oath) | who may tax, enter, confer |
| sanction | `ban`, `detain`; a closed `hold` | disqualification; recall |

**New, with the cut test (NERS: what dies without it).**

1. **Record kind `roll`** (`rosters.yaml: record_kinds`, keys `[entries]`). *Cut:* the founding order
   then lives only in ledgers. Nothing can be held, withheld, consulted, forged, seized or amended, so
   NPC-008's custody (a `core` need) has no object, "who certifies a deed" has no answer, and a house
   can be raised only by fiat. N holds bottom-up (a clerk's power), top-down (a parliament amends it),
   laterally (`research`, `forge`, `destroy_record` reach it with no new row).
2. **Seat-row keys `dignity:`, `passes_through:` (with `hand_term:`), and the section `founding:`**
   (`offices.yaml`; `upkeep:` is a key for a field `Office` already has). *Cut `dignity`:* stipends
   cannot differ by rank and the court is flat. *Cut `passes_through`:* every writ is answerable at
   issue, the clerk has no hand, and NPC-008, NPC-009 and NPC-011's delay all die. *Cut `founding`:*
   the two ducal houses read 0.000 (E-1) and the fixed point is prose.
3. **Arrangement row `acclamation`.** *Cut:* no open-floor occasion exists at which a deed is told to
   a crowd; ceremony has no room and publicity is a constant.

Considered and **not** added: a patron-client tenure kind (regard and `oblige` already say it; a
third edge would be two ladders for one quantity); a `dignity` or `prestige` stock (Layer 1 refuses a
stored aggregate); a `countersign`, `acclaim`, `audit`, `enrol` or `blind` verb (§8); a bureau type; a
faction-level "bureaucracy" stat; the Key-based directive enum of the compendium (retired, ED-IN-0232).

## 6. Legitimacy in a conquest-founded order: deed, dignity, office, stipend

This section answers the fixed point. It extends `person_q.legitimacy`, the deed claims, `confer` and
`succeed`; it adds no nobility system.

### 6.1 Four things that are easy to confuse, each with one carrier

| thing | what it is | carrier | whose truth | does it age? |
|---|---|---|---|---|
| **deed** | something a person did | a deed claim about him in someone's ledger | each observer's, by his own pursuits | yes: `legitimacy` reads a window |
| **founding deed** | the deed a seat was won by | a deed claim whose subject is the **seat** | each observer's | no |
| **dignity** | a deed the court has recognised | a `hold` on a seat row with no remit | the world's | for life |
| **office** | power delegated | a `hold` on a seat row with a remit | the world's | revocable, often termed |
| **stipend** | what the conferring seat owes the holder | a termed `oblige`, renewed by `transfer` | the world's (conserved) | yearly |

A deed is private opinion until recognised. A dignity is the recognition: it does not add to anyone's
regard by existing; it **publishes the deed** it cites, and the published deed moves regard through
`deeds_judged`'s told half, as any heard deed does. So the court of precedence, in a deed order, is
one thing: the machine that turns what a man did into what everybody has heard he did, and pays him
for it.

### 6.2 The rule, in one formula

```
legitimacy(p, holder, seat) = stance_toward(p, holder)                                   (stored; exists)
                            + Σ deed_term(p, c)  over holder's deeds p holds from the window   (exists)
                            + presumption_gain · Σ deed_term(p, c) · c.confidence/full
                                   over the founding claims about `seat` p holds               (new term)
```

The third term is read **unless `p` holds a claim that `holder` took the seat by force** (a
`standing_routes: dominance` deed of `holder`'s whose subject is the seat or its rung). It is
person-side (no World, AX-2): a villager who has not heard of the coup still credits the throne. The
scoring is `deed_term`, the weighting by confidence is `world_q.reception`'s own, so no second
methodology enters (NERS-S).

What each clause of the fixed point becomes:

| the fixed point asks | answer |
|---|---|
| what counts as a deed | any `DEED_KINDS` claim; what it is *worth* is each observer's pursuits against the `alignment` table. A field won is worth most to those who prize honour; a granary filled, to those who prize stewardship |
| who certifies it | a seat whose holder `confer`s a dignity citing it (the Crown; a duke for his duchy; the Confessor for the Church's own); for the **founding order**, the Roll, amended only by a determination of the Court Parliament |
| what it costs to claim it | the conferrer: a stipend for life out of his seat's rung. The claimant of a place on the Roll: a `petition`, a clerk's hand, a hearing, and the draw at each |
| how it passes to heirs | the founding claim's subject is the seat, so it serves whoever fills the seat lawfully (by `succeed`, by election, by conferral). It is a presumption, and the second term still ages: an heir who does nothing is credited only with what his house did |
| how it fails to pass | a holder known to have taken the seat by force reads no presumption; a dignity is not heritable at all (it is a `hold` that ends with its holder) |
| how a rival's deed unseats it | a rival's own windowed deeds, widely told, can exceed presumption plus the holder's deeds in enough persons' eyes; those persons' readings are the odds of his claim (§7.0, `succeed`) and of every recall and defiance on the way. No threshold fires anything |
| how a new accomplishment raises a house | enrolment: a deed is petitioned, carried, heard and determined onto the Roll; from then it is a founding claim for that seat, which does not age. Enrolment converts a deed that fades into a presumption that does not |
| what a conquest-founded house owes and is owed | owes: an oath to the seat above (`offices.yaml:196`: both dukes and the Grand Master are sworn to `off_king`), which carries **no term** (E-1): it was won, not bought, and ends only by the swearer's own `release`. Is owed: its place on the Roll. A court dignity is the opposite bond: sworn in play on `oblige_term`'s yearly clock, and kept only while paid. A house may hold both, and then the Crown has bought a second, weaker hold on a man it could not command by the first |
| the ranked order | `founding: {order: 1 | 2 | 3}` on the three seats; read as the confidence of the founding claim. It sets how much presumption a seat carries. It decides nothing |

### 6.3 How appointment, title and salary interact with rank by accomplishment

1. **A noble by deed needs the court for only one thing: that the deed be heard and outlast him.**
   Without a dignity his deed ages out of the window and his son inherits nothing. So the war-nobility
   comes to court, and the court's price is an oath.
2. **The Crown needs the court because conquest gave it land and no hands.** Offices go to those who
   can run them (the clerks of the inherited bureaux, whose seats carry no dignity and whose persons
   lean `altonian_civics`); dignities go to those who have done something. The King is the only person
   who confers both.
3. **Title without office** is the loyal opposition: paid, ranked, heard first, commanding nothing.
   **Office without title** is the clerk: he enters or returns every decree, and nobody rises when he
   comes in. **Both** is the over-mighty subject. **Neither**, with deeds, is the general on the
   frontier whom everyone has heard of and the Roll has not. All four arise from two independent
   `hold`s and one ledger; none is a state anyone stores.
4. **Salary is the test of the whole.** Each dignity conferred is a yearly debt of the conferring
   seat. A king who honours every deed cannot pay; one who honours none is surrounded by men whose
   deeds are aging. Unpaid, a term matures, the oath ends (`term.matured`, built), and the seat's
   purview no longer reaches that man's people (`purview_reaches`' oath clause). The court shrinks
   from the bottom of the roll upward only if the payer chooses that order: `_renewals` pays
   soonest-maturing first, and whom to pay when the fisc is short is a choice.
5. **The clerks are the founding order's custodians and its hostages.** They hold the Roll. A petition
   to enrol a new deed passes their hand; they may be regarded, courted, replaced, or purged as
   Altonian residue (`purge_altonia`), at which point nothing can be entered at all.

### 6.4 Why this is not a second ladder

The only numbers stored are a seat row's `dignity` (read for the stipend) and a founding entry's
`order` (read for a claim's confidence). Standing itself is never stored: it is computed per observer,
when read, by the function that already computes it. Two persons disagree about who outranks whom,
and both readings are real. The Roll is a document and can be wrong.

## 7. Expression in play

### 7.0 The five draws

Each is an existing row given `contests:`, a `counterparty:` where one exists, per-degree `writes:` and
`emits:` (the shape `arrest` and `determine` already have), a pool from `verb_capability` and an
obstacle in the SC lane's form. The rows belong to the verb lanes (`14_VERBS_BINDING` for `confer`,
`revoke`, `succeed`; `14_VERBS_MATERIAL` for `requisition`; the social family for `carry`); where a
lane's text makes one of these a fixed function of state, this section is the correction the standing
rule orders, and the receipt lists it for that lane. A fixture `procedure_draws: on | off` (shipped
`on`) exists only so a gate has a control arm that reproduces today's hash.

| verb | the draw | Overwhelming | Success | Partial | Failure (recoverable) |
|---|---|---|---|---|---|
| `confer` (investiture) | conferrer's pool against the receiving order | hold opens; the cited deed is published at full confidence to all the channel reaches | hold opens; deed published | hold opens **provisional**: a term of `provisional_term` seasons whatever the row says; a second conferral confirms it | no hold; `conferral.declined`; the seat stays open and the man is not barred; try again next season |
| `revoke` (recall) | revoker's pool against the holder's standing | hold closes now | hold closes now | hold closes at the season's end; the holder acts until then | hold stands; `recall.defied`; the revoker holds a deed claim against him (the ground for an `arrest` or a `march`) |
| `carry` (a hand of the chain) | the clerk's pool against the document | entered; the next hand's term is halved | entered; passes to the next hand | **held over**: the hand's term re-winds once; nothing lost but a season | **returned** to its maker unentered, with the clerk's reason as a claim; the maker may issue again |
| `requisition` (collection) | the collector's pool against the place | full amount; emits `requisition.rendered` (not a dominance kind) | full amount; `requisition.taken` | half the amount; the remainder stands as a shortfall claim the seat holds | nothing moves; `requisition.resisted`; the place's people hold the attempt as a deed |
| `succeed` (accession) | the claimant's pool against the seat | hold opens; no live rival claim survives | hold opens | hold opens **provisional** (termed); rival claims stay live | no hold; the title is not spent; the seat stays vacant and any eligible person may claim next season |

The odds, by source (every term is a named obstacle term or the pool; none is a flat office bonus,
which Layer 1 §B.7 refuses):

| source | enters as | read from |
|---|---|---|
| the person acting | the pool | `faculty(w, p, verb)`: `verb_capability` → `vocation_attribute`; `06_FA_office_capabilities.md` adds the governance vocations |
| the task | `difficulty` | by the rung kind of the seat or place acted on (a realm seat is harder to fill than a hearth's), and for `requisition` the amount against the place's stores |
| the counterparty's standing | `opposition` | the body's or the place's regard for the counterparty, `world_q.reception`'s sum |
| patronage | `favourable` / `hostile` | the counterparty's `regard` for the actor; a live `oblige` between them |
| venue | `standard` | the arrangement's `floor` (an open floor raises it) and how many are present |
| affiliation | `favourable` / `hostile` | `conviction_stand(p, altonian_civics)` for an act of procedure; `INCOMPATIBLE` pairs between actor and counterparty |
| evidence | `favourable` | a cited deed claim, weighed as `world_q.proofs` weighs one; a held Record of the matter |
| precedence | `favourable` | the conferee's or claimant's live dignity grade and the seat's founding confidence, each one step at most |
| the season | `stakes` | the place's `hunger_bands` band for a collection |

### 7.1 Piece by piece

| piece | who acts | verb | venue | roll | written | who reads it, and decides differently |
|---|---|---|---|---|---|---|
| honour a deed | a seat-holder with `confer` | `confer` on a dignity row, citing a deed claim he holds | his seat's rung; an `acclamation` if convened | §7.0 | a `hold` (the conferee's own termed `oblige` to the conferring seat is required first: homage before investiture); told deed claims | everyone reached: `regard` for the conferee rises or falls by their own pursuits; rivals with unrecognised deeds hold the conferral as a deed of the conferrer's |
| pay the court | the holder of the paying seat | `transfer` through the seat | the seat's rung | none (conservation; a term's clock) | stores moved; terms renewed, soonest first | the paid: `transfer.made` is a deed of the payer's. The unpaid: at maturity the oath ends and they are free of the seat's purview |
| fill the fisc | a seat with `issue` whose purview reaches the place | `requisition` | the place | §7.0 | stores moved up to the seat's rung; a shortfall claim on Partial | the place's people (`stability` counts a `requisition.taken`); the seat above, which sees its own stores |
| send an order | a seat with `issue` | `issue` | his rung | `issue`'s own | a writ with one stage per body in the seat's `passes_through` | the clerks of the first body, who are now offered `carry` on it |
| enter or return it | a seat-holder of the body named by the open stage | `carry` | the body's rung | §7.0 | the stage passed, re-wound or closed as returned | on the last entry the writ becomes **answerable**: its addressees are offered `comply`, `evade / defy`, `construe` (`06_FA_decree_binds.md`), each itself a choice and a draw |
| sit on it | the same clerk | no act | — | none: a clock | at the stage's maturity MATTER returns the writ to its maker | the issuer learns his writ came back; his regard for that body's seat-holders moves; `revoke` becomes worth ranking |
| petition | anyone | `petition`, then `carry` by a hand | where he is | §7.0 for each hand | a docket item when the last hand enters it | the bench at the next sitting |
| enrol a deed | a petitioner; a clerk; the Court Parliament | `petition` → `carry` → `speak` → `determine` under `parliamentary_debate` | a convened sitting, open floor | `determine`'s own | an entry on the Roll; founding claims deposited on those the Record's channel reaches | every later reading of that seat's holder |
| consult the Roll | anyone present where it is held | `research` | the clerk's rung | graded inquiry, obstacle raised by `forgery_quality` | finding claims | a claimant deciding whether to press; a rival deciding whether to `forge` |
| govern at a distance | the centre's seat; the frontier seat | `issue` through `passes_through: [the post]`; `comply` and its siblings | two places | as above | a writ that is answerable seasons after it was written | the governor acts on the last order he has; the centre judges him on one he never got |
| inspect a governor | a seat with `dispatch`; the person sent | `dispatch`, then `survey` or `research`, then `tell` | the province | the inquiry's own | a `faction_sheet` Record; claims | the centre's next `revoke` or `confer` |
| keep a treaty | two trade seats | `covenant`; `petition` for an exception; `seize` on a breach | the gate | their own | a covenant Record; a petition; a seized cargo | the counterparty official; both treasuries |
| acclaim | a claimant; the crowd | `convene` an `acclamation`; `speak`; `commit` | an open floor in the capital | `speak`'s own; then `succeed`, §7.0 | told deed claims; commits | the guard, the court and the crowd, each a set of persons whose regard is the claim's opposition term |
| disqualify a rival | a bench | `determine` under `tribunal` (disposes `ban`) | closed or admitted floor | `determine`'s own | a `ban` scoped to the banning seat's purview (FA audit R-06) | the banned man's `succeed` and any `confer` on him are refused at eligibility; `pardon` can undo it |

## 8. Verbs and contests, against the 67

No verb is added. Twenty-three rows are used; five gain a draw (§7.0); one is widened.

| need | verb | state today (`audits/06_FA_audit.md` E-3; `14_VERBS_BINDING.md` §0) | what this design asks of it |
|---|---|---|---|
| appoint, honour | `confer` | formed 5, attempted 0 | the draw; a dignity row requires a cited deed (`own_ledger`); the conferee's termed oath |
| recall | `revoke` | formed 5; refused by construction | the draw; FA's R-03 (reads `subject`) |
| accede | `succeed` | formed 0 at the horizon | the draw; the title as odds |
| pay | `transfer` | executes; no seat-holder has an occasion to pay the terms sworn to his seat (`_renewals`' docstring: H-158's `unblocks:`) | `upkeep` by row; the bill as a shortfall claim |
| tax | `requisition` | attempted 1, refused 1 | the draw and its four bands |
| order | `issue` | executed 19 of 26; binds nobody | stages from `passes_through` |
| enter a document | `carry` | petition-only | **widened** to any Record with an open hand stage whose body the actor holds a seat of; the draw |
| answer an order | `comply`, `evade / defy`, `construe` | 0 of 33, 0 of 5, 0 of 7 | FA's; formed when the writ is answerable |
| ask | `petition` | 20 of 20 | none |
| treat | `covenant` | 0 of 10 | CP-T09-03 |
| inspect | `dispatch`, `survey`, `research`, `tell` | execute; `dispatch` writes nothing | CP-T09-08 |
| assemble | `convene`, `open_case`, `speak`, `determine` | `convene` 12; `determine` 0 | SC's proposals; a Record disposal site for `parliamentary_debate` (CR-36) |
| believe, swear, leave | `commit`, `oblige`, `release` | 65 of 65; 26 of 26; 0 of 15 | none |
| falsify, destroy, take | `forge`, `destroy_record`, `seize` | built | `forge` able to make a `roll` or a writ (today it makes a `faction_sheet` only): a later edit |
| disqualify, restore | `determine` (`ban`), `pardon` | built, hand-built reach | none |

**Candidates folded, with the cut test.** *countersign*, *register*, *seal*: each is `carry` on a
named stage; a separate verb would differ only in the label. *acclaim*: `speak` at an `acclamation`
and `commit`; nothing an acclaim verb would write is not written by those. *audit*: `dispatch` plus
`survey` or `research`. *enrol*: `determine` disposing a Record. *blind*, *tonsure*: `ban`; a
mutilation that cannot be pardoned is a ban no seat may pardon, which is content. *bribe*: `give`,
whose effect on the clerk's regard is the whole of what a bribe does. *farm a tax*: a `covenant` whose
terms name a `requisition` right, design-first (§12, batch G).

## 9. Tuning dimensions

`audits/13_SC_contest_interrogation.md` did not exist at this reading; the terms below are named in
the SC lane's obstacle form (`05_SC_obstacle_difficulty_and_modifiers_B.md`) so that file can adopt or
correct them. Each has one owner and is data.

| dimension | what it changes here | owner |
|---|---|---|
| venue | an investiture or accession at an open floor reaches more ledgers and draws against a higher `standard`; a closed council is easier and tells fewer | `arrangements.yaml: floor`; the `acclamation` row |
| personality | which deeds a person honours (his pursuits against `alignment`); whether a clerk enters or sits (his ranking, sampled at his temperature) | `Person.pursuits`; `rosters.yaml: tables.alignment` |
| affiliation | `altonian_civics`: a holder favours procedure (entering, complying, collecting by writ) and is scarred by its breach; `purge_altonia` against `altonian_ascendancy` orients whole factions toward or against the bureaux | `descriptor_registry.yaml: affiliation_roster`; `rosters.yaml: tables.affiliation_engagement`, `thrust_axes` |
| office | never a bonus. The seat decides what may be attempted (remit), where (purview), what is owed (upkeep) and whose hand a paper needs (`passes_through`) | `offices.yaml` |
| evidence | a cited deed, a held Roll entry, a forged one (its `forgery_quality` is the examiner's obstacle) | `Claim`; `Record`; SC's `05_SC_evidence_and_rebuttal*.md` for citation in a hearing |
| publicity | whether a conferral's cited deed is told to the room, the rung or the realm | the witness channel of the act (`rosters.yaml: witness_channels`); CR-29 owns narrowing `chronicle` |
| season | the pay year (4); a hand's patience; a governor's term; the hunger band at collection | `fixtures: oblige_term`; `office_bodies.term`; `offices.yaml: term` (FA); `hunger_bands` |

## 10. What it generates with no player

Each story is a pattern an observer reads off the log; none is a carrier, a trigger or a script. "It
arises when" states conditions on persons' states, never an event that fires. "Reading" is the line
the digest of proposal F prints, and what would show the story did **not** occur.

| story | it arises when | reading that can fail |
|---|---|---|
| **The unpaid court** | the stipend bill of a seat exceeds what its holder can or will collect; he pays some and not others | `sworn terms: renewed n · matured m`; fails at `m = 0` over every seed |
| **The clerk's veto** | a writ's hand is held by a person whose pursuits or regard rank other work above entering it | `writs: entered · held over · returned · lapsed`, by body; fails if every writ is entered |
| **The single point of failure** | most hands of a body resolve to one person (NPC-009), whose scene budget is the body's throughput | share of a body's entries made by its busiest seat-holder; lapses in the season he is wounded, travelling or dead |
| **The overlooked general** | a person's deeds are widely held and no dignity cites them, while a lesser deed is honoured | for each person, told-deed claims held about him by others against dignities citing them; a `release` of his oath or a `succeed` attempt following |
| **Title inflation** | a conferrer honours faster than his fisc grows | bill against stores, per seat, per season |
| **The tax revolt** | collections draw Partial and Failure in a hungry place; the attempts are held as deeds by its people | `requisition` by band and place; `person_q.stability` readings of that place falling |
| **The stale order** | the centre's writ is answerable seasons after issue and the frontier has moved | lag in ticks from `dispensation.issued` to answerable; acts by the addressee in between |
| **The sandbagging prince** | the hand between the centre and the realm is a person whose regard for someone in the realm outweighs his `altonian_civics` | the Doux's entries against his hold-overs and returns, set beside his regard for Elske |
| **The purge of the residue** | persons holding `purge_altonia` come to hold the seats that confer and revoke the Ministries | Ministries seats vacant; then every writ of a seat that passes through them lapsing. Canon's "Ministry Collapse" card, arrived at by persons |
| **A house raised** | a deed is petitioned onto the Roll and the hearing draws Success | Roll entries at season N against build; the seat's presumption in others' readings before and after |
| **The forged Roll** | someone holds the Roll, or a copy, and a reason | `record.forged` of kind `roll`; a later `research` finding against it (batch G) |
| **A contested accession** | a seat falls vacant with a title-holder of low standing and another person of high | `succeed` attempts by band; provisional holds; live rival claims |

## 11. Provided arcs and characters that depend on it

From `audits/12_ARCS_adjudication.md` (rows at `:168`, `:229-263`, `:323-326`, `:368`) and
`audits/06_FA_audit.md` §13. "Unlocks" names the need by its number in the case file.

| case | need (short) | hardness | what in this design carries it | proposal | depends on |
|---|---|---|---|---|---|
| NPC-008 Almstedt | an office-holder holds institutional memory others must consult (N4); passively obstructs reform (N1, restated by FA as "a reform needs a Record only he holds, or his seat's confirmation") | core | he holds the Roll; reforms that amend it pass his hand; he may enter, hold over or return | A, C | CR-36 (Record disposal) |
| NPC-009 Strand | performs an unusual volume of other roles' tasks (N1); a single point of failure (N4); indispensability rises and falls with whether tasks need him (N3) | core / important | he holds a seat in the body most hands name; his share of entries is the measure | C | his row's `body` |
| NPC-009 Strand | a weakness makes one kind of approach easier (N2) | core | not here: CHAR's capability surface (a trait as a named `favourable` term) | — | `02_CHAR_capability_definitions.md` |
| NPC-011 Laskaris | receives directives from a nominal superior and delays, dilutes or fails to execute them without rebellion (N4) | important | he is a hand on the centre's instruments; his three answers are entered, held over, returned | D | C |
| NPC-011 Laskaris | pursues a personal goal with his polity's authority inside another's territory (N3); visits and leaves (N1) | core | not here: movement abroad (ARCS' M-ABROAD) | — | CORE / WR |
| NPC-089 Palaiologina | whether she decides alone or needs authorisation (UNCLEAR N6) | important | resolved: she is addressed by the centre's writs, which arrive late; she acts on the last she has | D | the centre's person |
| NPC-090 Doukas | a treaty constrains what trade officials may change (N1); a specific dispute the two officials resolve (N4); strictness the counterparty can anticipate (N3) | core / important | the covenant; a petition for an exception passing his hand, drawn, with his `altonian_civics` and `stability` as odds | D | CP-T09-03 |
| NPC-037 Reichard | the treasury post affects the Crown's material resources (N2) | core | her seat's rung is the fisc; she collects and pays | B | SE stores |
| NPC-083 (governor under orders) | a seasonal order she may comply with, bargain down or defy | core | unchanged from FA; this design adds only that the order reaches her through hands | — | `06_FA_decree_binds.md` |
| NPC-020, NPC-031 | the throne passes by claim; the heir is a status | important | the accession draw; the title as odds | E | `14_VERBS_BINDING` |
| NPC-050 Baralta | a campaign toward a higher seat, attemptable when the seat is weak | core | the comparison is `legitimacy` with and without presumption; her house is second on the Roll | A | CR-91, CR-37 |
| ARC-45 | a diplomatic demand suppressed while an intermediary withholds it | core | the centre's demand is an instrument with the Doux as a hand | D | CR-29 |
| ARCS row 12 | off-map superiors decide things | — | one authored person, one seat, one place | D | Jordan's names |

Soonest: NPC-037 and the unpaid court (batch B, on the spine); then NPC-008 and NPC-009 (batch C);
then NPC-011, NPC-089 and ARC-45 together (batch D).

## 12. Implementation plan

Six proposals, in landing order. Each lists exact keys, the gate (a seeded run with a control arm) and
the planted failure. Every gate on a draw reports **band frequencies over seeds**; a single seed is a
trajectory, not a rate (§0.1 pt 4).

| batch | proposal | what lands | depends on | cost |
|---|---|---|---|---|
| A | `15_INSTITUTIONS_BYZANTINE_A_dignities_and_the_roll.md` | `founding:` and the Roll; dignity rows in the body `Imperial Court`; the presumption term; `confer` drawn, citing a deed; oath before investiture | `06_FA_remit_grant_by_row.md`; `14_VERBS_BINDING` (`confer`); `06_FA_office_capabilities.md` for the pool | small build |
| B | `…_B_the_roga_and_the_fisc.md` | `upkeep` on rows; `upkeep_owed`; the bill as a shortfall claim; `requisition` drawn (the built oaths stay untermed) | A; `07_SE_treasury_granary_B.md` (stores that exist); `14_VERBS_MATERIAL` | small build |
| C | `…_C_the_hands_of_the_chain.md` | `passes_through`; `office_bodies.term`; `carry` widened and drawn; return at maturity; answerable on the last entry | `06_FA_decree_binds.md` (the triple and the content deposit) | small build |
| D | `…_D_the_empire_at_a_distance.md` | the centre: one place, two seats, one person; the Doux seated as a hand; the treaty hand; `altonian_civics` engagement cells | C; CP-T09-03; CP-T09-08; Jordan's names | edit (content) + small build |
| E | `…_E_accession_recall_and_the_crowd.md` | `succeed` and `revoke` drawn; the `acclamation` row; interfaces to CR-35, CR-37 and the papacy lane | A; `14_VERBS_BINDING`; `05_SC_arrangement_rows_that_bind.md` | small build |
| F | `…_F_playable_scenarios_and_reading.md` | two scenarios on FA's runner; digest lines; the band reading | `06_FA_playable_scenario.md`; A to C | small build |
| G | none written: design-first | revenue grant and tax farm; rule of avoidance; new dignities by `establish`; `forge` of a `roll` or a writ; `construe` at a hand; the chamberlain's bar (§14 item 4) | B and C in play, measured | design-first |

Order: A before B (a stipend needs a grade); B before C (a clerk's choice to enter or sit matters once
persons have something at stake in the writ); C before D (distance is a hand); E can land beside C.
G waits for readings from A to C: every item in it is a counter-pressure, and a counter-pressure to a
pressure not yet measured is apparatus.

**Dependencies on other lanes, by edge.** FA: P1 (remit by row), P2 (the decree's answers), P3 and B3
(terms), P4 and B4 (the runner and digest), P6 (vocations). SC: the obstacle form B; rows that bind;
the Record disposal site (CR-36). SE: stores at seat rungs (treasury-is-the-granary B). CORE: the
question slot (H-54), CR-29 (the chronicle channel), the reason trail. CHAR: relations with a ground
(the founding stance rows are one use of it), capability definitions. Verb lanes: BINDING, MATERIAL
and the social family for the five drawn rows. Papacy lane: the short list and the consecration.

## 13. The playable scenarios

Both run on `harness/governance_spine.py::play` (FA-P4), through `harness/play_surface.py`, on the
season loop: one code path, no fork. Detail in proposal F.

**`roga` (the first playable; needs A and B).** The player is the spine's Sovereign for eight
seasons. At tick 0, by the game's own effects: four dignity seats under him, two held by sworn men
whose terms mature in season 4, two vacant; two duchies with stores; a fisc that holds 4 against a
bill of 5; one person who gave more to the fisc than either and holds no dignity and no oath. *He
sees:* the bill, the fisc, who is owed and when, whose deeds he has heard of. *He chooses:* whom to
tax and how hard (`requisition`, drawn), whom to pay first (`transfer`), whether to honour the giver
and add to next year's bill (`confer`, drawn, and only if the man will swear), whom to leave unpaid. *Consequences:* a term that matures frees a man
and his people from his purview; a collection that draws Failure is remembered where it was tried.
*Ends:* FA's three (no seat; season count; `endings_reached`), plus **the court lapsed** (more than
half the terms sworn to his seat matured unpaid) and **the court kept** (none did, at the count).
*Control:* the same seed with the auto chooser in his seat.

**`chancery` (needs C).** The player holds the seat the Sovereign's writs pass through (on the spine
a hand is a seat, since the fixture may invent no body).
Each season: the documents in his hand, each with its maker, its age and its terms. He enters, holds
over or returns (a draw each time he acts), on a budget that does not cover them all. *Ends:* recalled
(the Sovereign's `revoke` draws Success or better); kept at the count; or the body empty.

## 14. Decisions that survive to Jordan

Four. Each was put through the five steps; the step that failed to answer it is named.

**1. When is an order answerable: at issue, or at entry?** (Extends `audits/06_FA_audit.md` §11 item 1;
not superseded, since that item is open; no design document or precedent decides it.)
- *(A) At issue, for every seat.* An order reaches its addressees as soon as it is made. Rulers have
  direct voice; clerks have no hand; delay exists only as distance.
- *(B) At entry, for a seat that declares `passes_through`.* An order is paper until each named body
  has entered it. Clerks hold real power; a frontier seat with no chancery is fast and unaccountable;
  purging the bureaux silences the Crown. Proposal C is written for (B) and collapses to (A) when no
  row declares the key.

Under either, obeying is a choice and a draw; nothing "binds" (the standing rule).

**2. Who credits the first Duke of Varfell's deed?** (D-1: canon's timeline and the fixed point pull
apart; a later ruling would settle it; none exists.)
- *(A) Everyone, at the third confidence.* The founding order is one fact held realm-wide. The caste
  is a separate thing from the house's standing.
- *(B) The south at full, the north discounted.* `founding.credited_in` names where the claim is
  seeded whole. The caste becomes a gradient in legitimacy itself: Vaynard is a great lord at home and
  a tolerated one at court, which is the ground of his arc.

**3. The empire's centre: the names.** ARCS row 12 decided the shape by precedent (a person, a seat,
a place); only Jordan can author who sits there, what the seat is called and where the Doux governs.
- *(A) Author them* (proposal D carries placeholders marked for replacement). Altonia becomes an
  institution with an inside: orders that arrive late, a prince who sits on them, a governor who can
  be recalled.
- *(B) Leave the Katepano the last word.* Altonia is one person's temperament; NPC-011's fourth need
  and ARC-45's suppression stay unreached.

**4. Do the Crown's bureaux have a barred order?** (The tree's BYZ-8, `needs_jordan` since 2026-07-09;
not superseded; canon is silent on who staffs the Ministries.)
`[RE-GROUNDED, narrowed: "not superseded" holds for the question and not for the form. The 2026-07-12 closure ruled the form: BYZ-8 is MERGE, "Author the oath-of-renunciation as a second collateral-type within the … succession-oath unification … not new … scaffolding", and its barred-office half "is closer to CUT" (.audit/2026-07-12-governance-compendium/tier3_proposal_status_closure.md:123). Option (B) below is that form (an oath that bars). The tree also holds a non-eunuch historical model for (B), Venice's *cittadini originari* (§2.14's re-grounding note), and the two ways such a servant falls (§18.4 item 4)]`
- *(A) No.* Ministry seats are filled from the same people as every other seat. The barons-and-clerks
  axis exists only as `altonian_civics` against `purge_altonia`.
- *(B) Yes: an oath that bars.* A person who takes a seat of the named bodies swears off the founding
  seats; `succeed` and a founding seat's `confer` refuse him at eligibility while the oath lives. The
  Crown gets servants it can trust with everything except the thing they cannot want, and a class
  that falls with its patron. Not built in A to F; batch G if taken.

## 15. Research transfer, nulls, and a NERS reading

**Changed what to build.**
- *Office and dignity are two tenures* (Kletorologion; the tree's BYZ-1, judged KEEP). Transfers
  whole, and costs nothing: the heir row was already the precedent.
  `[RE-GROUNDED, corrected: KEEP is the 2026-07-09 judgment; the 2026-07-12 closure regraded BYZ-1 DISTILL ("supplies no missing rung"; "retire the standalone … two-track section; preserve only the decoupled-prestige kernel", .audit/2026-07-12-governance-compendium/tier3_proposal_status_closure.md:115). This design is that distilled form: no second ladder, a remit-less seat. §18.3]`
- *The stipend is the bond, and it is yearly and personal* (the roga). Transfers whole onto
  `_renewals`; it is the reason `oblige_term: 4` is the right number and not only a swept one.
- *A decision is in force when entered* (the chancery; the Ming vermilion endorsement; Zhang
  Juzheng's deadlines). Transfers as shape: named hands, a clock on each, return on lapse.
- *Consolidation is one setting of a split* (themes, doux; `proactive_governance_scale_research_v1.md:263`).
  Transfers as "a row names both acts", with no flag.
- *The centre's hold is other men's oaths* (thematic officers answering to the bureaux). Transfers
  onto the oath clause of `purview_reaches` with no edit.
- *A conquest order keeps the old bureaux and resents them* (§2.14). This is the frame; it is why the
  bureaux are politically marked and why the two existing thrust axes are the right carriers.

**Decorative, or tried and not transferred.**
- The seven-bureau roster, the eighteen grades, the insignia: names and counts; canon names five
  bodies and the Ministries ruling says add none until a seat needs one.
- BYZ-2's purchase rule and the compendium's "title-inflation homeostat": a payment cited as a deed
  does the first; the bill does the second.
- BYZ-5 and HAB-4's coordination penalty: a flat modifier on a counter the code retired.
- The circus factions as factions: cohorts and one arrangement row carry what they did.
- Every hook in `research/governance/*.md` as written: they are in the retired Key and Directive
  idiom (`research/by_lane/FA_faction_actions.md:36`); the patterns transfer, the hooks do not.

**Nulls.**
- **The tree has no Byzantine research of its own depth.** `research/governance/` omits Byzantium
  ("its research agent was interrupted", `00_MANIFEST.md:28`); the only treatment is eleven table rows
  and nine proposals in the quarantined `.audit/2026-07-09-comparative-governance-research/`. §2 is
  therefore mostly `[MEMORY]`. It should be read as shapes; no number in this design rests on it.
  `[RE-GROUNDED, corrected: the first sentence is true of research/governance/ only. Nine other files treat Byzantium, four of them at procedure depth (acclamation; court rhetoric and protocol; the reception dossier; the army and its two loyalties): unified/RESEARCH_MAP_INSTITUTIONS_A.md §1. After re-grounding, of the nineteen [MEMORY] marks in §2, seven are sourced in whole or in part, and twelve stay memory-grade with a sourced cousin named beside each: §18.2]`
- **No source in the corpus treats a decree's entry as distinct from its issue**, in games or
  history, beyond the Ming row. Decision 1 rests on the shape alone.
- **No shipped game models a paperwork chain as persons with budgets.** The nearest the tree records
  are Republic of Rome's agenda control and the Ming piaoni row (`digests/DG_research1.md:552`).
  `[RE-GROUNDED: two further nulls and one presence. Null: of the four policy and court sims the suite verified, none rolls a governance act to fail except, partly, Dragon Age: Inquisition (research/game_precedent_suite/tables/R9_policy_court_sims.md:8-18), so §7.0's five draws have no shipped precedent. Null: the convergence the tree cites for office against dignity (X1) is graded OVER-CLAIMED at research/by_lane/NPC_npc_cast.md:386. Presence: the roga does have a shipped precedent, RTK XI "Ranks by Deeds" and RTK XIV's stipend by title (research/game_precedent_suite/tutorials/T13_koei.md:29, :78)]`
- **Nothing in the tree says what the Altonian church is in play.** Not designed here.

**NERS (definitions `CLAUDE.md` §0.06; E last, as a ratio).**
- *N.* Dignity rows: removable only by losing the unpaid court, the overlooked general and any use of
  the Imperial Court body, which has no seat today. Hands: removable only by losing three provided
  characters. The Roll: §5. Holds top-down (a king's bill), bottom-up (a petitioner's wait), lateral
  (two clerks of one body), diagonal (a provincial officer sworn to the centre). The `acclamation` row
  holds in one direction only (top-down ceremony) until cohorts answer at it: **narrowed**.
- *R.* Strategic (whom to pay, whom to honour, which paper to enter); customisable by rows; the
  no-player half is §10. Completeness at the extremes: an empty fisc lapses terms and nothing breaks;
  a body with no living seat-holder returns every paper, which is the purge story and must be shown
  not to deadlock the season (gate C).
- *S.* One degree ladder, one obstacle form, one treasury, one clock; the presumption is scored by
  `deed_term` and weighted as `reception` weighs. Pauses: a hearing on the Roll is SC's scene and
  returns a determination. Zoom: a hand is a person; a body is the persons in its seats.
- *E, against that.* Four row keys, one section, one record kind, one roster map, one arrangement
  row and five fixtures buy the court, the fisc, the chancery and the empire's distance. A player can intuit the
  outcomes from four sentences: honours cost money every year; unpaid men leave; paper needs hands;
  far orders arrive old.

## 16. Evidence log

`PYTHONHASHSEED=0`, at `84d2a02`; output under
`/tmp/claude-0/-home-user-ttrpg/7351887f-4cbe-51b5-ba88-a8b84f6cb379/scratchpad/runs/INST_BYZANTINE/`.

| id | command | seed · seasons | outcome |
|---|---|---|---|
| E-1 | `probe_build.py` (read-only; `populated.build_realm(0)`, no season) | 0 · 0 | 83 persons, 34 offices, 414 rungs, 2 Records (both `works`), 70 Propositions. Live `oblige`: 4 (`p_npc_041` → `off_restoration_leader`; `p_npc_050`, `p_npc_052`, `p_npc_070` → `off_king`), **none with a term**. Persons holding a stance row toward the King 13 (sum 59.00), toward the Duchess of Hafenmark 0, toward the Duke of Varfell 0; mean regard 0.720, 0.000, 0.000. No office declares `upkeep`; `default_upkeep` 1, `oblige_term` 4, `record_stage_term` 1. Stores at `r_valoria`, `terr_T1`, `duchy_valorsmark`, `set_alt_1`, `terr_ALT`: `{}`. `content_hash` `600d8b27147478e158553552cc1409a5` (`probe_build.txt`) |
| E-2 | a `python -` read of `verb_table.yaml` | n/a | 67 rows; the row shapes of `arrest`, `determine`, `speak` (per-degree `writes` and `emits`); `carry`, `confer`, `requisition`, `succeed`, `revoke` carry no `contests:` |
| E-3 | a `python -` read of `rosters.yaml` | n/a | `record_kinds`, `tenure_kinds`, `conferral_bases`, `successions`, `continuation_ties`, `standing_routes`, `matter_kinds`, `interposition_kinds`, `vocation_attribute` as quoted |

Not run: any season (the FA and verb lanes' `aperture 2 0` and `2 1` readings are cited at their
files); `pytest`; `corpus_run` (cited from `audits/06_FA_audit.md` E-7).

**Read in full:** `CLAUDE.md`; the three briefs; `offices.yaml`; `governance_spine.yaml`;
`arrangements.yaml`; `data/affiliations.py`; `audits/06_FA_audit.md` §0 to §13 (to `:807`);
`audits/02_CHAR_audit.md` §0A; the two verb audits present. **Read at the cited lines:**
`person_q.py` (`deeds_judged`, `attributed_deeds`, `deed_term`, `regard`, `heritage_regard`,
`legitimacy`, `stability`); `world_q.py::upkeep_of`; `effects_economy.py::_renewals`;
`effects_information.py::_declared_stages`, `_mint_document`; `state/carriers.py` (field lists);
`rosters.yaml` (`office_bodies`, `foreign_cast`, `thrust_axes`, `standing_routes`,
`continuation_ties`); `goals.yaml` (Altonia); `npc_registry.yaml` (NPC-008, -011, -089, -090);
`canon/03_canonical_timeline.md:54-126`; the comparative governance research's Byzantine and Chinese
tables and judgments. **Heads only:** the FA, SC, SE, CHAR and CORE proposals cited.
**`[SKIPPED]`:** `audits/06_FA_audit_addendum_B.md`, the SC and SE audits and addenda (their proposals'
heads were read instead); `audits/06_FA_audit.md` §14 onward; the three `research/governance/` bodies
beyond the manifest and line searches; `rise_to_power` and `proactive_governance` beyond line
searches; `.audit/2026-07-12-governance-compendium` beyond line searches; `.designs/systems/factions`
beyond line searches of four files; `verb_table.yaml` beyond the rows named; `gate.py`;
`decision/`; `loop/matter.py`; the digests beyond line searches. Reason: reading budget. What rests
on an unread path is marked `[UNVERIFIED]` in the proposals at the edit it affects.

## 17. The standing rule, checked against this file and listed for other lanes

Checked in this file: every procedure outcome is a draw (§7.0); the two stored orders decide nothing
(§6.4); what is certain is conservation, a clock, or eligibility. Three things in it are clocks whose
effect a reader might take for an outcome, so they are stated: a term maturing unpaid ends an oath
(the swearer's obligation ran out; whether he then leaves, stays or swears again is his choice); a
hand's stage maturing returns a paper (nobody acted; the maker may issue again); a provisional hold
maturing vacates a seat.

Found deterministic in the code or in another lane's text, for the owning lane:

| where | what is a fixed function of state | owner |
|---|---|---|
| `verb_table.yaml`: `confer`, `revoke`, `succeed` (no `contests:`); `_eff_succeed` (the first valid claim opens the seat) | appointment, recall, accession | `14_VERBS_BINDING`; FA |
| `verb_table.yaml: requisition` (`stores >= amount`, then the whole amount moves) | a tax collected | `14_VERBS_MATERIAL`; SE |
| `verb_table.yaml: carry` | a petition docketed | the social verb family; SC |
| `rosters.yaml: successions` read as outcome (`off_king: off_heir`) | an heir by fixed order | FA (the row is right as eligibility and as odds; §7.0) |
| `06_FA_decree_binds.md` by its title and §11 item 1 (A) "binds" | obedience | FA (its answers are the addressee's acts; this file asks only that each be drawn) |
| `gate.py::REVOCATION_DISPOSAL` (an appointed seat revoked costs a ban, always) | the cost of a fall | FA; ruled 2026-10-21, so named and not changed: §7.0 keeps the ban in every band in which the hold closes |
