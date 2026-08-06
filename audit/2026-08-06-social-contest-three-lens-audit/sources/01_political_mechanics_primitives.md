# Political Mechanics for a Renaissance-Inflected Videogame
## Research → Primitives → Rules → Content Navigation

**Scope.** Four components: (1) adversarial hearings — court, tribunal, Inquisition, negotiation; (2) parliamentary debate; (3) settlement and territorial governance; (4) diplomacy. Historical bases: Renaissance Italy (Venice above all), Rome (Republic and Church), Aristotle, the Carolingian Empire, Sengoku Japan, imperial China.

**Method.** Two-phase construction. Phase 1 built the primitive catalogue upward from named historical mechanisms and named existing game systems, never from a template of what such a document usually looks like. Phase 2 attacked the result — the audit is §7 and its findings are reported whether or not they were fatal. Phase 3 fixed what Phase 2 broke and re-reviewed. Nothing in §§4–6 is asserted from a general impression of a period; every primitive names the specific institution it came from.

**Source tiers.** Claims are tagged `[T0]` (primary text or original dataset), `[T1]` (authoritative synthesis), `[T2]` (reputable secondary), `[UNVERIFIED]`. Game-mechanic claims are `[T0]` when taken from the published rulebook or the game itself, `[T2]` when from designer commentary or a critical reading. Where the strongest reachable tier is below T0, the entry says so.

**How to read this.** §1 is the frame — why "primitive" is the right unit and what the word is doing. §2 is historical research findings, arranged by *mechanism* rather than by *civilization*, since the object is decomposition. §3 is the survey of games that already model this well and badly. §4 is the primitive catalogue — the core of the document. §5 assembles primitives into the four scenes. §6 covers content navigation and authoring. §7 is the adversarial audit. §8 is the gap register.

---

## §1 — Frame: what counts as a primitive, and why the word "game" is being used loosely

### 1.1 Family resemblance, and the refusal to define "debate mechanic"

Wittgenstein's treatment of "game" is the licence for treating a courtroom, a parliament, a tax assessment, and a marriage negotiation as one design problem. His point is that board games, card games, ball games, and solitary amusements share no single feature common to all; they are held together by a mesh of overlapping similarities, and an exact definition is neither available nor needed for the word to work `[T0 — Philosophical Investigations §§65–71]`. The design consequence is direct: do not look for the mechanic that *is* debate. Look for the overlapping resemblances between a Venetian doge election, a heresy interrogation, and a treaty haggle, and build primitives at the level where the resemblance actually sits.

He also introduces "language-game" for units of language smaller than a whole language, "consisting of language and the actions into which it is woven," in order to insist that speaking is part of an activity, a form of life `[T0 — PI §7, §23]`. That is precisely what a tribunal is. The Inquisition's interrogation is not a conversation with rules bolted on; the rules constitute what the utterances mean. A confession outside the procedure is gossip; inside it, it is legal fact.

### 1.2 Constitutive rules and the lusory attitude

Suits' counter-position matters just as much. Against the "look and see" method, he holds that games are goal-directed, voluntary, and rule-constituted, and that the rules deliberately forbid the most efficient means to the goal; players accept those rules *because* they make the activity possible `[T1 — Suits, The Grasshopper; discussed in Kobiela, Argumenta]`. This is the sharper design tool of the two:

> **Every political institution in this game is a set of constitutive rules that forbids the efficient means.** Assassination is the efficient means; the Senate exists to forbid it. The rules are the content.

Wittgenstein tells you not to over-define. Suits tells you what to build. Use both.

### 1.3 Procedural rhetoric

Bogost's claim — that games make arguments through their processes, not through their text — sets the standard the four components must meet `[T1 — Bogost, Persuasive Games]`. A tribunal scene that resolves by a single Rhetoric check argues that eloquence determines justice. A tribunal that resolves by which faction controls the panel argues something else entirely. Neither is neutral. Decide what each of the four components is arguing before choosing its resolution rule; §5 states the argument for each.

### 1.4 Frames and transactions — the psychological reading of "game"

Two further senses of "game" earn their place:

- **Goffman, frame analysis.** Participants operate inside a frame that tells them what kind of activity is occurring; frames can be broken, and a break is itself an event. A witness who addresses the crowd rather than the panel has broken frame. This is a mechanic, not flavour: frame-breaks should have costs and payoffs. `[T1]`
- **Berne, transactional analysis.** "Games" as repeated covert transactions with a concealed payoff — the ulterior motive underneath the ostensible one. Every senator's stated position and true position differ; the gap is the game. `[T1]`

### 1.5 Caillois, for texture

Caillois's four categories — *agôn* (competition), *alea* (chance), *mimicry* (role-play), *ilinx* (vertigo) — and the paidia/ludus axis from free play to rule-bound play are useful as a *check on the mix*, not as a taxonomy to obey `[T1]`. The historical record is emphatic that political systems mixed *agôn* and *alea* deliberately (§2.2). A design that is pure *agôn* misrepresents its subject.

### 1.6 What "primitive" means here

A primitive is an operation on state that:

1. cannot be decomposed further without losing its political meaning;
2. appears in at least two independent historical systems, or in one historical system and one existing game;
3. can be written as a rule with named inputs, a resolution, and named outputs;
4. composes with other primitives without special-casing.

Criterion (2) is the guard against inventing mechanics and calling them research. Criterion (4) is the guard against the common failure where each scene type gets a bespoke minigame and nothing shares a vocabulary.

---

## §2 — Historical research findings, arranged by mechanism

Arranged by what the institution *does*, not by where it is from. Each entry names its instantiations so the primitive in §4 can be traced back.

### 2.1 Selection: how a body decides who holds power

**Venice, ducal election (codified 1268, unchanged in essentials until 1789).** Ten alternating rounds of sortition and election, all drawn from the Great Council. A boy chosen at random from the street — the *ballottino* — draws the first lots. Thirty are drawn by lot; reduced by lot to nine; the nine elect forty; the forty reduced by lot to twelve; the twelve elect twenty-five; reduced by lot to nine; the nine elect forty-five; reduced by lot to eleven; the eleven elect the forty-one who elect the doge. Supermajorities gate each stage: at least twenty-five of forty-one, nine of eleven or twelve, seven of nine. Family quotas capped how many members of one house could sit on a college, communication with the outside was restricted, and campaigning was forbidden. `[T1 — Dahl 1994 via constitution.org; Mowbray & Gollmann, HP Labs, analysed the protocol formally; corroborated across four independent secondary accounts]`

Three design facts fall out of this and matter more than the pageantry:

- **Alternating narrowing and widening.** Not a funnel. The count goes 30 → 9 → 40 → 12 → 25 → 9 → 45 → 11 → 41. Each widening re-injects names the previous narrowing removed. A player who buys a bloc cannot know it survives to the next widening.
- **Sortition as an anti-corruption device, not a fairness device.** Nobody knows who sits on the next college until minutes before it votes, so bribery has no stable target `[T2]`.
- **Supermajority as a polarization filter.** Requiring 7 of 9 or 25 of 41 does not select the most popular candidate; it eliminates the most divisive `[T2]`.

**Contrast — Florence.** The *signoria* of nine, its head the *gonfaloniere*, drawn by lottery every two months `[T2]`. Same lot-based logic, radically shorter tenure, which produces a different game entirely: nothing can be planned across administrations.

**Contrast — Aristotle's taxonomy of selection.** Aristotle enumerates the axes directly: who selects, from whom, and in what manner, with election and lot as the two manners, and notes that mixing them — some offices by vote, some by lot, drawn either from all citizens or from a pre-selected pool — produces constitutions that are part aristocracy and part free state `[T0 — Politics IV, 1298a and following]`. This is a design space specification written in the fourth century BC. Use it as one.

**Contrast — imperial China.** Selection by examination rather than by lot or vote, combined with the *rule of avoidance* (officials not posted to their home region) and triennial evaluation of officials `[T1 — chinaknowledge.de; Ming Studies 2025]`. Merit-tested entry, geographically enforced disinterest, periodic re-assessment.

### 2.2 Deliberation: how a body converts talk into a decision

The Roman Senate supplies the cleanest procedural vocabulary available, and nearly every term is directly implementable.

- ***Ius agendi cum patribus*** — the right to convene the Senate and put business to it, held by consuls, dictators, praetors, and tribunes. Agenda control is an office power, not a social one. `[T2]`
- ***Relatio*** — the presiding magistrate's formal statement of the question, often with a draft resolution attached. He frames what is being decided. `[T2]`
- ***Sententia*** — a senator's stated opinion, delivered in an order set by the censors' roll (*album senatorum*): *princeps senatus* first, then ex-consuls, then ex-praetors, downward. The president could vary the order to honour or slight, calling a man out of turn or passing him over entirely. A senator could speak in full, or merely assent to a previous speaker (*verbo assentiri*). `[T2 — Dictionary of Greek and Roman Antiquities and derivative accounts]`
- ***Discessio*** — voting by physical division: *"whoever thinks this, go over there; whoever thinks otherwise, to this side."* If several conflicting *sententiae* had been offered, the president put whichever he pleased to the house, voted singly until one carried. **Agenda order is the president's weapon.** `[T2]`
- ***Diem dicendo consumere*** — consuming the day by speaking. A senator could include any other matter he pleased in his remarks, so talking until sunset killed the business. The filibuster is not modern. `[T2]`
- ***Intercessio*** — the tribunician veto, resting on sacrosanctity rather than on superior office. Any magistrate of equal or higher rank than the referring magistrate could also interpose. A veto could block the *relatio* itself, or strip a carried resolution of force. `[T1 — Perseus, Dictionary of Greek and Roman Antiquities, citing Polybius 6.16, Varro, Cicero de Legibus 3.3]`
- ***Senatus auctoritas*** — the *category for a motion that carried but was vetoed*. It has no administrative force and it still exists, on the record, as the expressed will of the house. This is an extraordinarily good game object: a defeated-but-recorded outcome that can be cited later. `[T1 — same]`

**Chinese analogues, which are procedurally sharper in one respect.** The Ming apparatus separated the *drafting* of a decision from its *approval*:

- ***Piaoni*** — the Grand Secretariat received memorials, scrutinized them, and pasted a proposed rescript to the face of the document before submitting it to the emperor. Whoever drafts the response frames the decision. `[T2 — Wikipedia, Grand Secretariat; corroborated by chinaknowledge.de]`
- ***Fengbo*** (sealed refutation, instituted 1384) and ***fenghuan*** (returning an edict sealed) — the Supervising Secretaries of the Six Offices of Scrutiny, and the Grand Secretaries respectively, could return an imperial edict rather than transmit it. A veto exercised by the clerical layer against the sovereign. `[T1 — chinaknowledge.de]`
- ***Yanlu***, "the avenues of criticism" — the censorial system as a named channel that could be open or narrowed, and whose narrowing was itself a political act contested in memorials. `[T1 — Ming Studies 92 (2025); Journal of Chinese History on late-Qing censorial protest]`

**Aristotle's specification of the deliberative element.** It is sovereign over war and peace, forming and dissolving alliances, passing laws, sentences of death, exile and confiscation, electing magistrates, and *auditing their accounts*. These powers may be assigned all to all citizens, all to some, or split — some to all, others to some `[T0 — Politics IV, 1298a]`. Note that audit sits inside the deliberative power, not outside it; §2.4 is therefore a sub-case, not a separate branch.

### 2.3 Adjudication: how a hearing is structured

**Stasis theory — the load-bearing find of this research.** Hermagoras of Temnos (c. 2nd century BC) devised a four-part scheme for locating the crucial issue in a case: *coniectura* (did it happen — an sit), *definitio* (does the admitted act fall under the charge), *qualitas* / *generalis* (the nature, motive, and justification of the act), and *translatio* (objection to the process or the forum itself). Cicero transmits it in *De Inventione* I.8.10; Quintilian and Hermogenes refine it. Hermagoras's own treatise does not survive — the doctrine is known only through later transmission. `[T1 — Sage Sourcebook on Rhetoric; Purdue OWL; ERIC ED358445. T0-provisional for Hermagoras himself: no original fragments preserved, per the Belles Lettres critical edition. [UNVERIFIED] as to Hermagoras's exact wording.]`

The stases are **ordered and gating**. You cannot argue the quality of an act before establishing that it occurred and that it falls under the charge; there is no point disputing how to spend money before establishing that there is money `[T2 — Pullman]`. That is a state machine. It is the single most directly implementable historical artefact in this document, and §4.2 builds on it.

**Inquisitorial procedure.** The *inquisitio* differs from an accusatorial trial in that the tribunal initiates, investigates, and judges. Bernard Gui's *Practica inquisitionis heretice pravitatis* (c. 1323–24) is organized in five parts — heresies, interrogation, evidence, sentencing, appeals — with model forms for abjurations and standardized interrogation questions; Gui oversaw hundreds of trials at Toulouse, 1308–1323. Nicolau Eymerich's *Directorium inquisitorum* (1376) is the later and more theoretically ambitious manual. `[T2 — Derek Hill, *Inquisition in the Fourteenth Century* (Boydell, 2019), the standing scholarly treatment of both manuals; the manuals themselves are T0 but were not read directly for this document. [TIER-FLOOR: T2 — primary manuals not consulted]]`

The mechanically salient asymmetry: **witness names were withheld from the accused.** Lea records the expedients — names supplied on a separate sheet so they could not be matched to testimony, or other names mixed in to confuse the defence, or witnesses sworn in the accused's presence but examined in his absence (sixteen of forty-eight at Bernard Délicieux's 1319 trial; fifteen shown to Hus in his cell in 1414). From withholding names it was a short step to withholding the evidence entirely. `[T2 — H.C. Lea, *History of the Inquisition of the Middle Ages* I.x — a nineteenth-century work with a known polemical slant; treat the specific trial figures as reliable and the framing as partisan]`

That asymmetry is the design gift: **the defence plays with incomplete information about the evidence array, and its moves are guesses about what the tribunal holds.**

**Venetian judicial structure, for the multi-forum problem.** The *Quarantia* (Council of Forty), probably early thirteenth century in its developed form, was for most of Venetian history the court of last resort, split in the fifteenth century into Criminal, Old Civil (Venice and the Dogado), and New Civil (the dominions). The *Avogadori de Comun* — three of them, one-year then sixteen-month terms — acted as public prosecutors and as guarantors of procedural legality, and kept the councils' archives and membership rolls. The Council of Ten (from 1310) held jurisdiction over state security and could punish patricians; the three State Inquisitors, drawn from the Ten, could decide without appeal on any citizen's life, the doge included. `[T1/T2 — Da Mosto's archival index and Maranini via historywalksvenice.com; John Adams's account of the State Inquisitors]`

The crucial structural observation, and one that a game should preserve rather than tidy away: **the Venetian bodies did not separate powers.** The Ten sat as a court, its members voted in the Senate, and the doge and Signoria were part of it. Trying to sort Venetian institutions into executive, legislative, and judicial fails `[T2 — venetianstories.com, making this point explicitly]`. Overlapping jurisdiction is the mechanic, not a flaw to be normalized.

### 2.4 Oversight: the itinerant auditor

This mechanism recurs in three unconnected systems and is therefore a strong primitive.

- **Carolingian *missi dominici*.** From about 802, the empire was divided into *missatica*, inspection circuits, visited in principle four months a year by at least two *missi* — one ecclesiastic, one lay, deliberately assigned outside their own landholdings to prevent nepotism and local capture. They held full investigatory powers, administered the oath of allegiance, promulgated capitularies, audited counts, and reported back. Their wergild equalled that of a member of the royal family. `[T1 — Britannica on *missus dominicus*, drawing on Ganshof; the *Capitulare missorum generale* of 802 is edited in MGH Capitularia I, 91–99 [T0, not read directly]]`
- **Venetian *Sindici Inquisitori*.** Itinerant magistrates whose entire purpose was the periodic on-site inspection of Venetian rule in the subject territories and the gathering of information for the centre. Their 1566 commission required them to bring "grandissima consolatione" to the mainland cities and to audit the rectors. They travelled as a visible cortège of roughly thirty people and proclaimed their arrival — the inspection was theatre as much as audit. Italian scholarship explicitly traces the institutional type back to the *missi dominici*. `[T2 — it.wikipedia, Sindici Inquisitori, citing the Senate commission text]`
- **Ming *Investigating Censors* (*jiancha yushi*).** Thirteen provincial circuits; low-ranking officials wielding great authority on tour, described as "acting on behalf of the Son of Heaven during tours of inspection," empowered to impeach by open memorial or by sealed accusation. `[T2 — Baidu encyclopedia rendering of the Ming *Zhiguan zhi*; corroborated in outline by chinaknowledge.de]`

Convergent features across all three: outsider status enforced by rule; temporary commission; power disproportionate to rank; dual reporting (to the centre and, in effect, to the inspected population as a legitimacy display); and the report itself as the artefact of value.

### 2.5 Territorial governance: assessment, obligation, and the terms of submission

**Sengoku and Momoyama Japan — the assessment shift.** Through most of the Sengoku period, *kandaka* prevailed: land valued by projected cash revenue, often in imported Chinese copper, flexible but non-comparable across domains. The shift to *kokudaka* — valuation in *koku* of hypothetical rice yield — came late, driven by Nobunaga's local surveys in the 1570s and completed by Hideyoshi's *Taikō kenchi*, conducted nationally 1583–1598. The result: every village a single tax unit collectively liable on its combined yield, every daimyō's worth expressed as the sum of his villages' *kokudaka*, and military obligation levied in proportion. The gross national figure in 1598 was just under nineteen million *koku*. `[T1 — Britannica, *Early modern Japan 1550–1850*; corroborated on the kandaka→kokudaka transition by multiple secondary accounts]`

The design point is not the rice. It is that **a survey converts heterogeneous holdings into one comparable number, and that number then becomes the basis of every subsequent obligation.** Conducting the survey is itself the political act.

***Bunkokuhō*** — the house laws individual daimyō promulgated for their own domains, alongside their own weights, measures, and sometimes era names, treating the domain as a *kokka* `[T2]`. Article 20 of the Takeda *Kōshū hatto no shidai* enjoins priority to arms and armour "since the world is in the warring state" `[T2 — Encyclopedia of Japan]`. A ruler who writes his own law code is making a claim; a game where the player drafts domain law is modelling exactly this.

**Hostage-taking as a governance instrument.** The Sengoku practice of demanding high-ranking hostages from vassals and allies was formalized by Hideyoshi (residences and family at Osaka) and then by the Tokugawa as *sankin-kōtai*: alternate residence at Edo, wives and heirs permanently resident as hostages, with the ruinous cost of two establishments and the processions between them as a deliberate financial drain. Punishments available to the centre: reduction of domain, transfer to a different domain, or forced suicide with the lineage demoted. `[T1 — Britannica, *The bakuhan system*; T2 — Nakasendo Way on the Sengoku origins]`

**Carolingian capitularies.** Charlemagne issued roughly half of all known Carolingian capitularies, using them to impose uniformity across a realm too large to administer directly — the *Admonitio generalis* (789) on education and clerical reform, the Programmatic Capitulary of 802 on oaths, judicial procedure, and the fiscal duties of counts. Capitularies were sent to the *missi* for local enforcement, and *missi* compiled their own working books from the parts they found useful. `[T1 — MGH Capitularia; Britannica; McKitterick via secondary summaries]`

The failure is as instructive as the instrument: later capitularies repeatedly re-prohibit the same abuses — magnates seizing land from the poor — which is documentary evidence that promulgation did not equal enforcement `[T2 — 8thcentury.com, summarizing Ganshof, *Frankish Institutions*]`. **A decree should be a state change with a compliance roll, not an automatic effect.**

**Venetian territorial administration — the two-officer model.** Each major subject city received two *rettori*, Venetian patricians elected by the Great Council: a *podestà* over civil administration and justice, a *capitano* over military affairs. Local institutions otherwise continued — Vicenza kept its own great council of 500, a minor council of 150, an assembly of forty, eight *deputati ad utilia*, and a *consolato* court that could impose death and, from 1545, exile from Venetian territory. Above the rectors sat the *provveditori generali*; the *Avogaria di Comun* scrutinized rectors' decisions and could suspend them for review; appeals ran to the Quarantie or the Ten. `[T2 — Brill, *Factional Struggles*, on Vicenza specifically; corroborated on the rettori structure by the Verona university teaching materials]`

Two principles worth extracting: **indirect rule preserves and co-opts local institutions rather than replacing them**, and **the governor is split into two rivalrous offices so that neither can defect alone.**

**Ostrom's design principles**, as the analytic frame for settlement management. From the study of long-enduring common-pool institutions: clearly defined boundaries; rules congruent with local conditions; collective-choice arrangements letting those affected modify the rules; monitoring by monitors accountable to the users; graduated sanctions proportioned to the seriousness and context of the offence; cheap and rapidly accessible conflict resolution; minimal recognition by higher authorities of the right to self-organize; and, for large systems, nested enterprises in multiple layers. `[T1 — Ostrom, *Governing the Commons* (1990), as reported consistently across four independent secondary sources]`

The formal result worth carrying into the design: institutional stability is as sensitive to *certainty of detection* as to *severity of sanction* — high monitoring frequency permits lower, less costly punishments `[T1 — arXiv review of CPR modelling, formalizing the graduated-sanctions principle]`. A game that models only punishment severity gets the politics wrong.

### 2.6 Diplomacy: the resident, the report, and the ceremony

**The resident ambassador.** Mattingly's *Renaissance Diplomacy* (1955) made the resident ambassador in fifteenth-century Italy the hinge of modern diplomacy. Subsequent scholarship has qualified this substantially: Mallett argues the transition from occasional to continuous diplomacy has been over-emphasized and that Italian developments were less isolated from the wider European scene than once thought; the process was slower and less rational than the search for a clean origin suggested. `[T1 — Cambridge, *The Italian Renaissance State*, ch. 21; Fletcher, *Diplomacy in Renaissance Rome* (CUP, 2015)]` Do not build the game on the clean-origin story; build it on the messy one, which is better drama anyway.

**The *relazione*.** Venice required its ambassadors, uniquely among sixteenth-century states, to deliver a final report on recall — a broad synthesis of the political, military, economic, and social condition of the state visited, distinct from a report on the mission's own proceedings, and periodically updated by successive ambassadors. Venice also maintained more permanent representatives than any other European state. `[T1 — Queller, *The Development of Ambassadorial Relazioni*, and Goffman, *Negotiating with the Renaissance State*, both quoted in the Wikipedia entry; Taylor (Penn State) on the uniqueness of the requirement]`

The *relazione* is a **cumulative, inheritable intelligence object**, not a one-shot reward. Successive ambassadors update the same document. That is a strong content structure (§6.3).

**Venice's diplomatic grades**, which give the design its rank ladder for free: *ambasciatore* (in post no more than two years), *inviato straordinario* (single missions), *residente* (below ambassadorial rank) `[T2 — Verona teaching materials]`. Giovanni Emo, Venetian ambassador in Rome in 1480, appears to have been the first to report regularly to the Council of Ten `[T2 — Mallett via researchgate summary]` — i.e. the intelligence channel and the political channel could be separated.

**Ceremonial and precedence.** Diplomatic ceremonial developed both as a mechanism for regulating interaction *and* as the focal point of intense competition between sovereigns; precedence disputes remained a live source of international controversy into the nineteenth century `[T2 — Fletcher]`. Precedence is a zero-sum status resource contested in public — a scarce, visible, non-fungible good. Excellent design material.

### 2.7 Aristotle as the analytic skeleton

Three uses, all direct:

1. **The tripartite division of any constitution** — the deliberative element, the element concerned with the magistracies (what offices exist, over what they have authority, how they are filled), and the judicial element. Order these well and the constitution is well ordered; constitutions differ from each other because these three factors differ. `[T0 — Politics IV, 1298a]` This is the game's schema for describing *any* polity, including invented ones.
2. **The enumeration of variants.** Aristotle does not stop at the three parts; he enumerates how each may be arranged — all citizens deciding at once, or in turns, or magistrates deciding preliminarily with the people ratifying; property qualifications for participation; offices by vote or by lot, from all or from a pre-selected pool. `[T0 — same]` This is a parameter table.
3. **Audit as a deliberative power.** "Elects magistrates and audits their accounts" sits in the same sentence as war and peace `[T0 — same]`. The *euthyna* is not an afterthought.


---

## §3 — What existing games model, and where they fail

Organized by what each one solves. Failures are recorded with equal weight, because a failure mode you can name is a design constraint you can meet.

### 3.1 Tabletop RPG: the only genuinely structured debate system in wide use

**Burning Wheel, *Duel of Wits* (Luke Crane, 2002; Gold ed. 2011).** The closest existing analogue to what component (1) needs.

Structure: each side declares a **Statement of Purpose**. Each rolls a skill appropriate to the register — Oratory for a speech, Rhetoric for a debate on the merits, Persuasion for an intimate discussion, Interrogation for an interrogation — and adds successes to Will to get a **Body of Argument**. Play proceeds in volleys of three rounds; each round both sides *secretly script* one manoeuvre. The manoeuvres are Point, Dismiss (attacks); Avoid, Obfuscate, Rebuttal (defences); Feint, Incite (specials). Reduce the opponent's Body of Argument to zero and you win — but you must offer a **compromise scaled to how much of your own Body of Argument you lost**. Ties produce mutual concession. `[T0 — Burning Wheel Gold; T2 — designer forums, RPGnet]`

Four things it gets right, all of which should be carried forward:

1. **The stakes are declared before the mechanics run.** The Statement of Purpose is the contract; the dice decide who gets it, not what "it" is.
2. **The compromise rule.** Winning ugly costs you. This single rule does more political modelling than most grand-strategy diplomacy systems.
3. **Simultaneous secret scripting** makes it a real prediction game rather than an alternation of checks.
4. **It explicitly binds public performance, not belief.** The rules "only dictate public performance and acknowledgment of the 'truth'" `[T2 — 5e conversion documenting the same principle]`. A losing debater has conceded the floor, not changed his mind. Exactly the distinction a tribunal needs.

**Its documented failure, which is the most valuable single finding in §3.** Players converge on Point and Dismiss because both drive the opponent's Body of Argument down fastest; Obfuscate appears occasionally; **Rebuttal almost never gets used, because so many manoeuvres beat it.** `[T2 — Burning Wheel Forums, subsystem advice thread, 2012]` The manoeuvre set is not balanced, so the rich option space collapses to two verbs.

> **Constraint C1.** If debate manoeuvres are differentiated only by damage output, players will find the two highest-damage ones and stop. Manoeuvres must differ in *what they change about the state of the argument*, not in how much they subtract.

§4.2's stasis-gated design exists specifically to satisfy C1: a manoeuvre's value depends on which stasis is live, so no single verb dominates.

### 3.2 Videogames: contradiction-finding

**Ace Attorney / Danganronpa.** The mechanic is: a testimony is a list of statements; one contradicts an item in your evidence inventory; you select the pair. Danganronpa's *Nonstop Debate* adds a timer and shooting: statements scroll, highlighted ones may be false, you fire a "truth bullet" (an evidence item) at the contradiction. Later refinements let you *lie* by inverting the meaning of the evidence you present, or agree with a point rather than refuting it. `[T2 — Game Developer analysis; Medium video-essay transcript]`

Its structural limit is documented precisely: each round has **one correct statement-and-bullet combination**, and the space is deliberately pruned — two to four statements, one to three available bullets, on normal difficulty `[T2 — Game Developer]`. Some rounds require playing twice: capture a statement as a new bullet on the first pass, use it on the second.

> **Constraint C2.** Contradiction-matching is a puzzle with one solution, not a debate. It produces excellent moment-to-moment tension and zero political modelling. A political trial cannot use it as the primary resolution, because in a political trial the winner is often the side whose evidence is *worse*.

The salvageable part is the **inventory-as-argument** idea: claims are objects you hold, spend, and lose.

**Disco Elysium.** Skills are not modifiers but interlocutors — each has a voice, an agenda, and a personality, and they contradict each other inside the player's head, so an internal conflict generates the external choice `[T2 — multiple system analyses]`. The Thought Cabinet introduces long-running commitments that alter what is sayable.

> **Transferable.** Give the player's *positions* voices. A character who has publicly committed to *libertas ecclesiae* should have that commitment argue with him when expedience beckons. This is Berne's ulterior transaction made mechanical (§1.4).

**Suzerain.** Governs by choice under pressure — internal events, foreign policy, economic policy, superpower management — with cabinet ministers advising in their own interest and choices interlocking so that outcomes surprise `[T2]`. Its strength is that advice is *interested*; its weakness is that resolution is largely branch selection, so the player is choosing between authored futures rather than operating a system.

**Pentiment.** Relevant as a model of *investigation under an authority that will act regardless of truth*: the player's accusation has consequences the game refuses to grade as correct. `[T2 — [UNVERIFIED] as to specific mechanics; included on the strength of general critical consensus, not a rules source. [TIER-FLOOR: T2]]`

### 3.3 Grand strategy: governance at scale

**Victoria 3** is the most explicit modern implementation of parliamentary politics as a system and should be studied closely, including its arithmetic.

- **Interest groups** hold **clout**; the government is composed of some of them; the rest are the opposition. **Legitimacy** (0–100) derives principally from the total clout of governing interest groups, and, where elections exist, from vote share, divided proportionally. Below 25 legitimacy, the government cannot pass any law except one supported by an active movement, and an enactment already in progress makes no progress at all. `[T0 — Victoria 3 game files as documented on the official wiki]`
- **Law enactment is a multi-stage process with a success chance and a stall chance.** Governing interest groups and non-passive movements that support the law add to success; all non-marginalized groups and movements opposing it add to stall. The ruler's stance adds ±5% per step of difference. **Three setbacks over the course of the process and the enactment fails**, locking the law out for two years. Base time is 100 days per stage; governing-principle laws take double, power-distribution and economic-system laws 1.5×; legitimacy above 90 cuts 25%, legitimacy 25–49 adds 50%. `[T0 — official wiki, Laws page; T2 — community guide corroborating the timing multipliers]`
- **Enactment provokes counter-mobilization**: attempting a law raises participation in opposing movements and lowers it in supporting ones; half the increase applies immediately and the rest bleeds in at 1% per week; above 75% participation, revolution begins. `[T2 — namu.wiki, detailed mechanics summary; [UNVERIFIED] against current patch]`

> **Transferable, and this is the single most important structural loan in §3.** A law is not a toggle. It is a *process with duration, a running probability, discrete setbacks, a failure state with a cooldown, and an opposition that grows precisely because you attempted it*. §4.3 generalizes this as the Enactment Clock primitive.

**Crusader Kings III.** Vassal obligations are negotiable **contracts**; **crown authority** has four levels which gate what the liege may do at all — at the lowest, vassals may war on each other and the liege can only ask them to stop; only at level two can succession law be changed or titles revoked `[T2 — gamepressure guide; TV Tropes summary]`. Court positions, councillors, and schemes supply the character layer.

Devereaux's critique is the relevant adversarial reading: CK3 has mechanics for wanting vassals and for vassals making life difficult, but it is "set up so you can generally succeed at things kings wanted to do but were unable to pull off," and personal-opinion bonuses paper over structural factors `[T2 — acoup.blog, *Teaching Paradox* IIa]`.

> **Constraint C3.** If personal relationship modifiers can be raised high enough to dissolve structural conflict, the structure stops mattering. Cap the influence of affection: some conflicts must be *positional* and unbuyable.

**Old World.** Ambitions as victory conditions, generated by the current ruler's attitudes *and* by the desires of the most influential families; when the ruler dies, his outstanding ambitions go on a clock `[T2]`. This is a clean solution to the "what does this character want" problem: goals are emitted by the intersection of a person and the houses around him, and mortality is the pacing device.

### 3.4 Board games: negotiation without enforcement

**Diplomacy (1954).** The foundational insight: a negotiation phase in which players reach agreements, followed by simultaneous execution, with **no mechanism whatever for enforcing an agreement** `[T1]`. Every promise is cheap talk. Everything interesting follows from that one omission.

**The Republic of Rome (Avalon Hill, 1990).** Players are factions in the Senate; play is a series of Senate sessions in which proposals are made and voted — electing consuls, censor, and in emergency a dictator; assigning provincial governorships; funding or disbanding legions; appointing commanders; enacting land reform; and **prosecuting senators for ethical lapses**. Crucially the state itself can lose: foreign threats and popular unrest can destroy Rome, and everyone loses with it. `[T2 — Wikipedia; T2 — retrospective]`

> **Transferable.** A shared-loss condition converts a purely competitive assembly into one where obstruction has a real ceiling. This is the mechanical answer to "why would a self-interested senate ever agree on anything."

**John Company (2017, 2nd ed. 2022).** Takes *Republic of Rome*'s event deck and office structure and adds the key wrinkle: **most successful ventures require the cooperation of several offices held by different players**, forcing negotiation and shifting alliances; there are two voting layers, a chairman election and a Parliament phase that can change the game's own rules `[T2 — TV Tropes; Wikipedia]`.

> **Transferable.** Office powers should be *complementary but distributed*, so that acting at all requires assembling a coalition of officeholders. This is the mechanism that makes offices worth fighting over.

**Kremlin (1986).** Players do not own politicians; they hold *influence* over politicians arranged in a pyramid, and politicians age and die. Win by having your man wave from the rostrum in three non-consecutive years. `[T2 — Wikipedia]`

> **Transferable.** Separating *who holds the office* from *who controls the officeholder* is the cleanest available model of patronage, and mortality is a natural clock.

**Die Macher (1986).** Successive regional elections; parties manipulate real issues, buy media, and manage the gap between their platform and public opinion `[T2]`. Its transferable idea is the **shadow-opinion track**: party positions and public opinion are separate tracks and the distance between them is what scores.

**Pax Renaissance / Pax Pamir 2e.** Two-row card market with positional pricing — the leftmost card free, each further card costing one more, paid by placing coins *on the cards you skip*, so passing over a card subsidizes the next player who takes it `[T0 — Pax Pamir rules]`. Loyalty to one of several coalitions, changeable during play `[T2]`.

> **Transferable.** Positional pricing is a superb model of *political opportunity cost*: taking the alliance you want funds your rival's alternative. And declared, switchable loyalty with a visible dial is a better model of factional allegiance than hidden alignment.

**Machiavelli (Diplomacy variant, Renaissance Italy).** Adds money, bribery, garrisons, three seasons a year, and random plague and famine to the Diplomacy chassis `[T2]`. Bribery as an explicit legal action changes the negotiation from cheap talk to a market.

### 3.5 What nothing in this survey does well

An honest null on one point: **no game in this survey models the *content* of an argument.** Burning Wheel abstracts it into Body of Argument; Ace Attorney reduces it to one correct pair; Victoria 3 replaces it with faction arithmetic; Diplomacy leaves it entirely to the players' mouths. The stasis-gated design in §4.2 is proposed precisely because that space is empty — which also means it is unproven, and §7 attacks it on exactly that ground.


---

## §4 — The primitive catalogue

### 4.0 Shared substrate

Every primitive below operates on five object types. Nothing else is needed.

| Object | Fields | Note |
|---|---|---|
| **Actor** | House, Offices held, Standing (per body), Commitments, Ledger of obligations owed and owing | Standing is *not* one number — see P1 |
| **Body** | Roll (ordered membership), Competence (what it may decide), Procedure (which of P11–P20 apply), Quorum | Competences may overlap. This is deliberate (§2.3) |
| **Office** | Powers, Term, Incompatibilities, Selection method | An office is a bundle of primitives, not an atom |
| **Claim** | Proposition, Stasis level, Premises, Warrant, Provenance, Support | The argument object; see P6 |
| **Record** | Outcome, Body, Date, Status (in force / vetoed / superseded) | Includes P15 recorded defeats — a losing motion is still an object |

Design rule: **no scene type gets its own object model.** A heresy trial, a Senate session, a tax dispute, and a treaty conference all manipulate the same five things. If a scene needs a sixth object, either it is genuinely new (add it globally) or the scene is being special-cased (don't).

---

### 4.1 Family A — Standing and position

**P1 — Standing (indexed).**
*Does:* the weight an actor's speech carries. **Indexed per body**, not global. A censor commands the Senate and nothing in a village assembly.
*Resolution:* modifies every argument and procedure roll made in that body.
*From:* Roman *auctoritas* and the *album senatorum* ordering `[T2]`; Victoria 3 *clout*, which is likewise per-arena `[T0]`.
*Fails when:* collapsed to one global number. Then the game has a protagonist stat instead of a political landscape.

**P2 — Precedence.**
*Does:* a public, ordered, zero-sum rank inside a body. Someone must be first, and raising one actor lowers another.
*Resolution:* determines speaking order (P13), seating, and ceremonial priority; contested by formal claim.
*From:* Renaissance diplomatic ceremonial, a live source of inter-sovereign conflict for centuries `[T2 — Fletcher]`; *princeps senatus* `[T2]`.
*Fails when:* made purely cosmetic. Precedence must gate something — usually P13 — or nobody fights over it.

**P3 — Commitment.**
*Does:* a publicly recorded position. Can be cited against the actor later; contradicting it costs Standing in the body that recorded it.
*Resolution:* an opponent spends an action to cite; the citation is itself a P7 attack on the actor's consistency.
*From:* the *promissione ducale*, the doge's oath enumerating the limits on his own power, sworn on accession and revised by the *Correttori* `[T1]`; Ming memorials citing "ancestral injunctions" against novelty `[T1]`; Disco Elysium's Thought Cabinet, as the mechanical model `[T2]`.
*Fails when:* commitments have no memory. They must persist across scenes and be searchable by opponents — otherwise they are dialogue, not mechanics.

**P4 — Immunity.**
*Does:* a status that makes a specified class of move against the actor *procedurally invalid*, not merely risky.
*Resolution:* the move is rejected before resolution; attempting it is itself an offence.
*From:* tribunician sacrosanctity — the tribunes were not magistrates and held no superior power, relying entirely on inviolability of person `[T1]`; *missi* protected by a wergild equal to the royal family's `[T1]`.
*Fails when:* it is absolute. Every historical immunity was breached; the interesting play is in the breach and its consequences.

---

### 4.2 Family B — Argument (the stasis machine)

This family is the answer to Constraint C1 (§3.1). Manoeuvres differ by *what they change about the state of the argument*, not by damage.

**P5 — Stasis Gate. — the spine of every hearing.**
*Does:* holds the dispute at one of four ordered questions. Argument may only be made at the live stasis. Winning at a stasis advances the gate; the defence's goal is to win at the earliest possible one.
*The four:* **Conjecture** (did it occur?) → **Definition** (does the admitted act fall under the charge?) → **Quality** (what was its nature, motive, justification?) → **Jurisdiction** (*translatio*: may this body hear it at all?).
*Resolution:* each stasis is resolved by the P7/P8 exchange below; resolving in the accuser's favour advances to the next, resolving in the defence's favour ends the hearing at that stasis.
*From:* Hermagoras via Cicero, *De Inventione* I.8.10, refined by Quintilian and Hermogenes `[T1; the doctrine survives only in transmission — [UNVERIFIED] as to Hermagoras's own formulation]`.
*Why it works as a game:* the stases are *inherently ordered* — you cannot evaluate an act before establishing that it happened `[T2]` — so the gate is a state machine that already exists rather than one imposed on the material.
*Fails when:* Jurisdiction is placed last and treated as a desperation move. It is historically last in the sequence but the defence should be able to *raise* it at any point, at the cost of conceding the earlier stases. That trade is the most interesting decision in the family.

**P6 — Claim.**
*Does:* the argument object. Premises + warrant + conclusion, with Provenance (who says so, and how they know) and a Stasis level at which it operates.
*From:* Walton's argumentation schemes — stereotypical defeasible patterns of premises and conclusion `[T1 — Walton 1996; Walton, Reed & Macagno 2008]`. The scheme *from expert opinion* is the canonical example and is exactly what a tribunal's theological assessor supplies.
*Fails when:* claims are undifferentiated. A claim resting on a witness, a document, and a doctrinal authority must be attackable in different ways, or P7 collapses.

**P7 — Attack, in three kinds.** *This replaces "damage."*
- **Undermine** — attack a premise. Removes the premise; the claim may survive on others.
- **Rebut** — attack the conclusion with a contrary claim. Both stand; the body must weigh them.
- **Undercut** — attack the *inference*, not the premises or conclusion. The premises remain true and stop supporting the conclusion.

*From:* Prakken's structured-argumentation framework, in which the three ways of attacking an argument — premise, conclusion, inference — yield undermining, rebutting, and undercutting defeat `[T1 — Prakken 2010, *An abstract framework for argumentation with structured arguments*]`, instantiating Dung's abstract framework ⟨X, A⟩ of arguments and an attack relation `[T1 — Dung 1995]`.
*Why this is the fix for C1:* undercut is strictly better against expert-opinion claims, undermine against eyewitness claims, rebut against claims you cannot touch but can outweigh. **The correct manoeuvre depends on the claim's structure, so no verb dominates.**
*Fails when:* the three are given numeric weights and no structural difference. Then it is Point/Dismiss again.

**P8 — Critical Question.**
*Does:* a scheme-specific challenge that **shifts the burden of proof** rather than defeating anything. Cheap to ask, expensive to answer.
*Resolution:* the questioned party must answer or lose the claim by default; answering costs an action and may expose a new premise to P7.
*From:* Walton's pairing of each scheme with characteristic critical questions, which "provide ways to attack arguments based on the schemes"; the questions correspond to the three attack types `[T1 — Bench-Capon in memoriam Walton; Prakken 2010]`.
*Fails when:* free. Critical questions must consume the asker's action or the hearing becomes an infinite regress of "why?".

**P9 — Burden of Proof.**
*Does:* a single token. Whoever holds it loses the current stasis if the exchange stalls.
*Resolution:* moved by P8, by presumption rules attached to the forum, and by P10.
*From:* the formal dialogue literature on burden of proof `[T1 — Prakken, Reed & Walton, ICAIL-05]`; procedurally, the inquisitorial forum's default placement of the burden on the accused is the historical asymmetry `[T2]`.
*Fails when:* symmetric across forums. **The whole point is that the burden sits differently in an accusatorial court, an Inquisition, a Senate, and a negotiation.** Forum-specific burden placement is what makes forum choice (P10) matter.

**P10 — Forum Challenge (*translatio*).**
*Does:* a move to shift the dispute to a different Body with different Competence, Procedure, and default burden.
*Resolution:* contested by P13 in the current body; success moves the Claim set, resets the stasis gate to Jurisdiction, and re-evaluates every Claim under the new body's evidence rules.
*From:* *translatio* as the fourth stasis `[T1]`; Venetian practice, where the same matter could plausibly land before the Quarantia, the Ten, the Senate, or the Avogadori, with overlapping competence and no separation of powers `[T2]`; appeals from mainland rectors routed to the New Civil Quarantia or the Ten depending on the framing `[T2]`.
*Fails when:* forums are cosmetically distinct. If two bodies apply the same rules, moving between them is a wasted action.

**P11 — Evidence Array (asymmetric).**
*Does:* the tribunal holds a set of evidence items; the defence sees only their count and category, not their content or provenance.
*Resolution:* the defence spends actions to *probe* — each probe reveals one attribute of one item, or a name.
*From:* inquisitorial withholding of witness names, with the documented expedients: names on a separate sheet unmatchable to testimony, decoy names mixed in, witnesses sworn before the accused but examined in his absence — sixteen of forty-eight at Bernard Délicieux's 1319 trial `[T2 — Lea I.x, a partisan but factually careful source]`.
*Game precedent:* Ace Attorney inverts this (the player holds the evidence, the witness lies). Inverting it back is the design move.
*Fails when:* the array is fully random. It must be *authored to be inferable* — the defence should be able to reason from who is absent from the room to who testified.


---

### 4.3 Family C — Procedure

**P12 — Agenda Control (*relatio*).**
*Does:* the right to convene a Body and to state the question put to it, including attaching a draft resolution.
*Resolution:* held by office. The holder chooses the wording; the wording sets which stasis (P5) the body sits at.
*From:* *ius agendi cum patribus* and the *relatio* `[T2]`.
*Fails when:* the question is fixed by the scenario. **The framing is the first move of the scene and it must be a player-contestable one.**

**P13 — Speaking Order.**
*Does:* an ordered call of the roll. Position matters because early speakers set the terms and late speakers can only assent or dissent.
*Resolution:* order derives from P2 (precedence), but the chair may call a member out of turn to honour him or pass him over to slight him — both are actions with Standing consequences. A member may speak in full (*sententiam dicere*) or merely assent to a previous speaker (*verbo assentiri*), which costs nothing and adds weight to that speaker's motion.
*From:* the *album senatorum* ordering and the president's documented discretion to vary it `[T2]`.
*Fails when:* every member gets an equal turn. Then order is noise.

**P14 — Division (*discessio*).**
*Does:* resolution by counting. **If several conflicting motions are live, the chair chooses which to put and in what order, voting each singly until one carries.**
*Resolution:* count Standing-weighted or head-counted according to the Body's Procedure.
*From:* *discessio*, with the presiding magistrate putting "such as he pleased" `[T2]`.
*Fails when:* the order of putting motions is automated. That order is the chair's principal weapon and must be a decision.

**P15 — Veto (*intercessio*).**
*Does:* blocks a motion. Held by office, scoped: some vetoes block the *relatio* before debate, others strip a carried motion of force.
*Resolution:* automatic within scope; the cost is political, paid in Standing and in the Ledger.
*From:* tribunician *intercessio*, and the rule that any magistrate of equal or higher rank than the referring magistrate could also interpose `[T1 — Polybius 6.16; Varro; Cicero, *de Legibus* 3.3.10]`; Ming *fengbo* / *fenghuan*, the returned edict `[T1]`.
*Fails when:* free to use. A veto that costs nothing is used every time; historically the tribune's veto rested on a body he could not replace.

**P16 — Recorded Defeat (*senatus auctoritas*).**
*Does:* a motion that carried but was blocked by P15 persists as a Record with no force and full citability.
*Resolution:* creates a Record with Status = vetoed. Can be cited later as evidence of the body's will (a P6 Claim with strong Provenance), or re-put after the vetoing office turns over.
*From:* exactly this Roman category — a proposal carried and invalidated by *intercessio* was called *senatus auctoritas* `[T1 — Dictionary of Greek and Roman Antiquities, citing Valerius Maximus, Tacitus, Cicero *ad Fam.*]`.
*Why it matters:* it converts defeat into a durable asset and gives losing players a reason to keep pressing. Very few games have this and it is nearly free to implement.

**P17 — Clock Consumption.**
*Does:* spends the session's remaining time to prevent business being reached.
*Resolution:* a speaker may include any matter he pleases in his remarks; each such action consumes a session slot.
*From:* *diem dicendo consumere*, the practice of talking against time until sunset `[T2]`.
*Fails when:* sessions have unlimited slots. The session must be a scarce container or obstruction is impossible.

**P18 — Enactment Clock. — the most important procedural loan.**
*Does:* converts passing a measure from a vote into a *process*: N stages, each of fixed duration, each carrying a running success chance and a stall chance; discrete setbacks accumulate; at the setback cap the measure fails and is locked out for a cooldown.
*Resolution per stage:* Success contribution = Σ clout of supporting factions in government + Σ support of active supporting movements. Stall contribution = Σ from all non-marginalized opposing factions and movements. Ruler stance shifts by a fixed step per degree of difference. Duration scales by measure class and inversely with legitimacy.
*From:* Victoria 3's law enactment, including the three-setback failure with a two-year lockout, the 100-day base stage, the class multipliers (2× for governing principles, 1.5× for power distribution and economic system), and the legitimacy modifiers (−25% above 90, +50% at 25–49) `[T0 — official wiki, Laws]`.
*The half that most designs omit:* **attempting the measure mobilizes the opposition.** Participation in opposing movements rises on attempt, half immediately and the remainder bleeding in over weeks; above a participation threshold, revolt `[T2 — [UNVERIFIED] against current patch]`. Reform must be able to make things worse.
*Fails when:* the running probability is hidden. The player must see the odds moving, or the intermediate stages are dead time.

**P19 — Competence and Quorum.**
*Does:* defines what each Body may decide and how many must be present. **Competences are permitted to overlap.**
*From:* Aristotle's division of powers among the deliberative, magistracies, and judicial elements, with the explicit note that powers may be given all to all, all to some, or split `[T0 — Politics IV, 1298a]`; and the Venetian counter-case, where the Ten sat as court, its members voted in the Senate, and the doge was part of it — so the tripartite sort simply fails `[T2]`.
*Design instruction:* build the Aristotelian schema as the *description language*, then violate it in the specific polities. The gap between the schema and the practice is where the politics is.

**P20 — Drafting Right (*piaoni*).**
*Does:* whoever drafts the response to a submission frames the decision the superior then ratifies or rejects.
*Resolution:* the drafter writes a proposed resolution attached to the petition; the sovereign's choice is reduced to accept / reject / return.
*From:* the Ming Grand Secretariat, which received all memorials, scrutinized them, and pasted a proposed rescript to the face of the document before submission — becoming *de facto* the highest policy-forming body `[T2 — corroborated across two sources]`.
*Why it matters:* it models bureaucratic power without any explicit power stat. The clerk who drafts outranks the minister who signs.

**P21 — Return-Unsigned.**
*Does:* refusal to transmit an instrument, exercised by the clerical layer against the sovereign.
*From:* *fengbo* (1384) and *fenghuan* — Supervising Secretaries of the Six Offices of Scrutiny and Grand Secretaries could return an edict sealed rather than promulgate it; the practice was later called *kecan*, "participation of the Offices" `[T1 — chinaknowledge.de]`.
*Fails when:* modelled as a simple veto. The distinguishing feature is that it is a *low-ranking* power over a *high-ranking* actor, and its exercise is career-threatening — pair it with a personal risk roll.

---

### 4.4 Family D — Selection

**P22 — Sortition.**
*Does:* draws members at random from a defined pool.
*Purpose in design:* not fairness. **Unpredictability of the target.** No one knows who will sit, so influence cannot be pre-bought.
*From:* the Venetian ducal chain; the *ballottino* drawn from the street to make even the first draw uninfluenceable `[T1]`; Florence's bimonthly lottery for the *signoria* `[T2]`; Aristotle's enumeration of lot as one of the two manners of appointment `[T0]`.

**P23 — Threshold Election.**
*Does:* election requiring a stated supermajority.
*Effect:* filters out polarizing candidates rather than selecting popular ones.
*From:* the Venetian gates — 25 of 41, 9 of 11 or 12, 7 of 9 `[T1]`.

**P24 — Alternating Narrow / Widen. — the signature Venetian primitive.**
*Does:* a selection chain that repeatedly contracts by sortition and expands by election, so that each contraction destroys a coalition and each expansion re-admits names the previous stage removed.
*Sequence, as the historical template:* 30 → (lot) 9 → (elect) 40 → (lot) 12 → (elect) 25 → (lot) 9 → (elect) 45 → (lot) 11 → (elect) 41 → doge `[T1]`.
*Why it is a great mechanic and not merely a curiosity:* it makes bloc-building **partially** effective. A player who controls twelve of the Great Council has a real but non-deterministic chance at each stage, and must decide at every widening whether to spend influence on the current college or hold for the next.
*Fails when:* implemented as a cutscene. This must be playable at every stage with a spend decision, or it is a slot machine.

**P25 — Quota.**
*Does:* caps how many members of one House may sit in a given college simultaneously.
*From:* the Venetian family limits on each electoral college, alongside the restrictions on electors' outside communication and the prohibition on campaigning `[T2]`.

**P26 — Term and Rotation.**
*Does:* fixed short tenure, ineligibility for immediate re-appointment, incompatibility between offices.
*From:* Council of Ten members served one year, could hold no other public function during it, and could not be related to one another `[T2]`; Avogadori served one year, later sixteen months `[T2]`; the Florentine two-month *signoria* `[T2]`; the Venetian ambassador capped at two years in post `[T2]`.
*Design effect:* short terms mean nothing can be planned across administrations, which forces short-horizon play and rewards institutional memory (P16, P28) over personal power.

**P27 — Avoidance.**
*Does:* bars an officeholder from serving where he holds interests.
*From:* the Chinese rule of avoidance — officials not posted to their native region `[T1]`; *missi* deliberately assigned outside their own domains, in mixed lay-and-ecclesiastical pairs, expressly to prevent nepotism and local alliance `[T1]`.
*Design effect:* this is the rule that makes an officeholder *legible* to the player as a stranger who must build local relationships from zero.


---

### 4.5 Family E — Information

**P28 — Standing Report.**
*Does:* a persistent, cumulative document object describing another polity or territory: its political, military, economic, and social condition. Successive holders of the post *update the same document* rather than producing new ones.
*Resolution:* accuracy decays with time since last update; the document is readable by whoever has access to the archive, and is itself stealable.
*From:* the Venetian *relazione*, required of every ambassador on recall, distinct from a report on the mission's proceedings, and periodically brought up to date by successive ambassadors `[T1 — Queller; Goffman]`. Venice maintained more permanent representatives than any other sixteenth-century state and was alone in requiring the report `[T1]`.
*Why it is the right content structure:* it gives the player a document whose value grows over a campaign, which is a far better reward for a diplomatic posting than a number.

**P29 — Inspection Circuit.**
*Does:* an itinerant commission that visits localities on a route, samples their true state against their reported state, and publishes findings.
*Resolution:* per locality, compare declared values (P32) with sampled values; the delta produces findings, and findings feed sanction (P34) or vindication.
*From:* three independent convergences — Carolingian *missi dominici* on *missatica* circuits, in mixed lay/clerical pairs, nominally four months a year `[T1]`; Venetian *Sindici Inquisitori*, whose reason for existing was the periodic inspection of the mainland and whose 1566 commission is explicit about the double purpose of audit and of displaying good government to subjects, travelling as a visible cortège of about thirty and proclaiming their arrival `[T2]`; Ming Investigating Censors on thirteen provincial circuits, low-ranked but empowered to impeach `[T2]`.
*Design note:* all three sources make the same point about **theatre**. The inspection's legitimacy effect on the inspected population is separate from, and often larger than, its informational effect. Model both.

**P30 — Sealed Channel.**
*Does:* a private accusation or report route that bypasses the ordinary chain of command.
*Resolution:* the report reaches the sovereign directly; the accused has no notice; the accuser's identity may be protected.
*From:* Ming censors impeaching "either through open memorials and direct impeachments, or through sealed memorials of accusation" `[T2]`; the Qing preference for the palace memorial system, strictly between emperor and memorialist `[T1 — Journal of Chinese History]`; the Venetian ambassador reporting directly to the Council of Ten from 1480 `[T2]`.
*Fails when:* it is the only channel. The interesting decision is **open accusation (costly, public, builds Standing if vindicated) versus sealed (safe, deniable, worth less)**.

**P31 — Rumour and Reputation Drift.**
*Does:* the gap between an actor's real state and what each Body believes about it, decaying toward truth at a rate set by proximity.
*From:* the *relazione* system exists precisely because this gap is expensive `[T1]`; Die Macher's separation of party position and public opinion is the cleanest game analogue `[T2]`.

---

### 4.6 Family F — Obligation and enforcement

**P32 — Assessment.**
*Does:* a survey converting heterogeneous holdings into one comparable number, which then becomes the base of every subsequent obligation.
*Resolution:* conducting it is a political act with resistance; the declared figure and the true figure may differ, and the difference is the game.
*From:* the shift from *kandaka* (land valued in projected cash revenue, flexible, non-comparable across domains) to *kokudaka* (valuation in *koku* of hypothetical rice yield), begun in Nobunaga's local surveys of the 1570s and completed by Hideyoshi's *Taikō kenchi*, 1583–1598; each village became a single tax unit collectively liable on its combined yield, each daimyō's worth the sum of his villages, and military obligation was levied in proportion `[T1 — Britannica]`. Gross national assessment in 1598: just under nineteen million *koku* `[T2]`.
*Design instruction:* **make the survey playable.** Deciding to assess a province, choosing the assessors, and adjudicating the resistance is a better governance scene than any budget screen.

**P33 — Decree with Compliance.**
*Does:* promulgates a rule to N localities. Each locality rolls compliance against its own disposition, distance, and the presence of an enforcing agent.
*From:* Carolingian capitularies — Charlemagne issued roughly half of all known Carolingian capitularies to impose uniformity `[T1]`, transmitted through the *missi* for local enforcement, with *missi* compiling their own working excerpts `[T1]`. **The failure is documented in the record itself:** later capitularies repeatedly re-prohibit the same abuses, evidencing that promulgation did not produce enforcement `[T2 — Ganshof via secondary]`.
*Fails when:* a decree is an instant global state change. That is the single most common error in governance games and it removes the entire enforcement layer.

**P34 — Detection Rate and Graduated Sanction.**
*Does:* two coupled dials — how likely a violation is noticed, and how hard it is punished, with punishment proportioned to seriousness and context.
*The formal result to build on:* institutional stability is as sensitive to certainty of detection as to severity of sanction; high monitoring frequency permits lower and socially cheaper punishments `[T1 — CPR modelling review formalizing Ostrom's graduated-sanctions principle]`.
*From:* Ostrom's design principles 4 and 5 — monitoring by monitors accountable to the users, and graduated sanctions from other users, from officials accountable to them, or both `[T1 — *Governing the Commons*]`.
*Design instruction:* let the player set both dials and let the fiction respond. A regime that punishes savagely but monitors rarely should be *visibly* less stable than one that inspects often and fines lightly. That is procedural rhetoric (§1.3) doing real work.

**P35 — Hostage / Bond.**
*Does:* a pledge held by the centre — a person, a sum, a title — forfeited on defection.
*From:* Sengoku demands for high-ranking hostages from vassals and allies; Hideyoshi's requirement of Osaka residences with wives and heirs relocated; formalized as Tokugawa *sankin-kōtai*, with alternate residence, permanent hostage families at Edo, and the deliberate financial drain of two establishments and the processions between them `[T1]`. Ieyasu himself was a hostage for nearly thirteen years `[T2]`.
*Coupled sanctions available to the centre:* reduction of domain, transfer to a different domain, or forced suicide with the lineage demoted `[T2]`.
*Design note:* the *cost* is the mechanism, not the threat. Model the drain, not just the deterrent.

**P36 — Charter of Submission.**
*Does:* negotiated terms on which a territory is incorporated, specifying which local institutions survive, which are suspended, and what the centre may extract.
*From:* Venetian mainland practice — subject cities kept their own councils and courts (Vicenza retained a great council of 500, a minor council of 150, an assembly of forty, eight *deputati ad utilia*, and a *consolato* that could impose death and, from 1545, exile from Venetian territory), while Venice inserted only its two rectors `[T2]`; and *bunkokuhō*, the domain law codes daimyō promulgated alongside their own weights, measures, and sometimes era names, treating the domain as a *kokka* `[T2]`.
*Design instruction:* conquest should produce a *negotiation*, not a colour change. What you leave standing determines what governing costs for the rest of the game.

**P37 — Split Command.**
*Does:* divides a governorship between two officers with distinct competences who must both act for the territory to act, and each of whom reports independently.
*From:* the Venetian *rettori* — a *podestà* over civil administration and justice, a *capitano* over military affairs, both patricians elected by the Great Council; above them *provveditori generali*, with the *Avogaria di Comun* able to suspend rectors' decisions for review `[T2]`. Also the *missi* in lay-and-ecclesiastic pairs `[T1]`.
*Design effect:* neither officer can defect alone, and the player who holds one must court the other. This is the cleanest available generator of local political texture.

**P38 — Nested Layers.**
*Does:* organizes governance in tiers, with appropriation, monitoring, enforcement, and conflict resolution each operating at multiple levels, and the smallest units at the base.
*From:* Ostrom's principle 8, and the corollary principle 7 — that higher authorities must at minimum *recognize* the lower units' right to devise their own institutions `[T1]`.
*Design instruction:* pair with P36. A charter that recognizes local self-organization costs less to enforce and yields less; one that abolishes it yields more and requires permanent P29 inspection.

---

### 4.7 Family G — Exchange

**P39 — Reservation Value and Overlap.**
*Does:* each party holds a private walk-away value; agreement is possible only where the values overlap, and the negotiation is over the division of that overlap.
*From:* the standard negotiation-analytic frame of best alternative to a negotiated agreement and zone of possible agreement `[T1 — Fisher & Ury, *Getting to Yes*; Raiffa]`.
*Design instruction:* the alternative must be *concretely modelled* — a specific other alliance, a specific campaign — not a number. A player should improve his position in a negotiation by improving his outside option, off-screen, before the scene starts.

**P40 — Side Payment.**
*Does:* a transfer — money, office, marriage, precedence — that shifts a party's stance without persuading it.
*From:* Machiavelli (the Diplomacy variant) making bribery an explicit legal action alongside money and garrisons `[T2]`; Carolingian *honores* as the currency of loyalty `[T2]`.
*Fails when:* it dominates. See Constraint C3: if payment can always clear the gap, positions stop mattering. Some actors must have **unbuyable** positions.

**P41 — Scaled Compromise.**
*Does:* the winner of a contested resolution must concede in proportion to how much he lost while winning.
*From:* Burning Wheel's *Duel of Wits* — the victor offers a compromise scaled by how much of his own Body of Argument was destroyed; a clean win with no compromise is rare; ties produce mutual concession `[T0/T2]`.
*Why it is the most valuable single loan in the document:* it makes *cost of victory* mechanically real, which is the thing political fiction is actually about and almost no system models.

**P42 — Cheap Talk.**
*Does:* agreements with no enforcement mechanism whatsoever, followed by simultaneous execution.
*From:* Diplomacy (1954), whose entire design consists of adding a negotiation phase and then declining to bind it `[T1]`.
*Design instruction:* this must be the *default*, with P43 as the expensive exception. A world where treaties bind automatically has no diplomacy in it.

**P43 — Costly Signal.**
*Does:* makes a commitment credible by making it expensive to fake — a hostage (P35), a dynastic marriage, a public oath before a body that will record it (P3 + P16), or a payment made in advance.
*From:* the *promissione ducale* as an oath recorded and revised by a standing magistracy `[T1]`; hostage practice `[T1]`; oaths of fidelity administered by the *missi* and reported on by count `[T1]`.

**P44 — Positional Pricing.**
*Does:* an array of available options where taking the one you want *pays* for the ones you passed over, subsidizing them for whoever moves next.
*From:* the Pax market — leftmost card free, each subsequent card costing one more, paid by placing a coin on each card you skip `[T0 — Pax Pamir 2e rules]`.
*Why it belongs in a political game:* it is the cleanest available model of political opportunity cost. Seizing the alliance you need funds your rival's second choice.

**P45 — Shared Loss.**
*Does:* a condition under which the polity itself fails and every player loses, regardless of relative standing.
*From:* *The Republic of Rome*, where foreign threats and popular unrest can destroy the state and end the game for everyone `[T2]`.
*Why it is necessary:* without it, an assembly of self-interested actors has no reason ever to agree, and obstruction (P15, P17) has no ceiling. This is the single rule that makes a legislature playable.

---

### 4.8 Composition rules

1. **One vocabulary.** Every scene draws from P1–P45. A scene that needs a new verb needs it added to the catalogue, available everywhere.
2. **Forums differ by parameter, not by minigame.** A tribunal and a Senate differ in which primitives are switched on, where P9 (burden) starts, and which P19 competences apply. They do not differ in resolution system.
3. **Every primitive that grants power must have a cost or a term.** P15 costs Standing; P26 bounds offices; P8 costs an action. An uncosted primitive is exploited within an hour.
4. **Records outlive scenes.** P3, P16, P28 all produce objects that persist and are citable. This is what makes a campaign feel political rather than episodic.
5. **The information layer is not optional.** P28–P31 are what make P32–P38 decisions rather than arithmetic. A governance system with perfect information is a spreadsheet.

---

## §5 — Assemblies: the four components built from primitives

Each assembly states its procedural rhetoric first (§1.3), then its primitive set, then its turn structure.

### 5.1 Component 1 — Adversarial hearing (court, tribunal, Inquisition, negotiation)

**What it argues:** *a hearing decides what may be said about what happened, not what happened.* Truth is an input the forum may ignore.

**Primitives:** P5 Stasis Gate · P6 Claim · P7 Attack ×3 · P8 Critical Question · P9 Burden · P10 Forum Challenge · P11 Evidence Array · P1 Standing · P3 Commitment · P41 Scaled Compromise.

**Turn structure.**

1. **Framing.** The presiding officer exercises P12 to state the charge. The wording fixes the opening stasis. The defence may immediately spend its first action on P10 to contest the forum — cheap now, expensive later.
2. **Stasis loop.** While the gate is open at stasis *S*:
   - The accuser plays a Claim at *S* (P6) drawn from the Evidence Array.
   - The defence may **Undermine** (attack a premise), **Rebut** (offer a contrary claim), **Undercut** (deny the inference), or ask a **Critical Question** (P8, shifts P9 rather than defeating).
   - Or the defence may **Probe** the Array (P11), spending an action for one attribute of one hidden item.
   - Exchange ends when one side cannot or will not act; the holder of P9 loses the stasis.
   - Accuser wins *S* → gate advances. Defence wins *S* → hearing ends here.
3. **Sentence.** If the gate passes Quality, sentence is set by the forum's own rule — which is where the four hearing types diverge and where their politics live (below).
4. **Compromise.** Apply P41: the winner's outcome is reduced in proportion to the actions it cost and the Commitments it forced him to break.

**The four hearing types are the same machine with four parameter sets:**

| | Burden starts with | Array visible to | Sentence set by | Distinctive |
|---|---|---|---|---|
| **Accusatorial court** | Accuser | Both sides | Panel vote (P14) | Symmetric; the fairest and least interesting |
| **Inquisition** | Accused | Tribunal only (P11) | Tribunal alone | Withheld names; abjuration is a *negotiated* outcome, not a loss |
| **Political tribunal** | Whoever has less Standing in this body | Both, but items have Provenance ratings | P14, with the chair choosing motion order | The verdict tracks P1, not P6 |
| **Negotiation** | Neither — no P9 | Neither party's Array is visible | P39 overlap | Stases become the agenda; P41 is the whole point |

Note the last row: **a negotiation is the same scene with the burden token removed.** That is not a metaphor. Remove P9 and the stasis gate stops adjudicating and starts sequencing an agenda — is there a dispute at all, what is it about, what is it worth, and who may settle it — which is exactly what a negotiation's agenda is.

**Inquisition-specific note.** Bernard Gui's manual is organized as heresies / interrogation / evidence / sentencing / appeals with model abjuration forms `[T2]`, which maps directly: category identification, the P5 loop, the P11 array, the sentence rule, and P10. **Abjuration should be modelled as P41 compromise, not as a loss state.** Historically it was the usual outcome of an inquiry `[T2 — Hill, ch. 4]`, and treating it as failure misrepresents the institution.

### 5.2 Component 2 — Parliament

**What it argues:** *procedure is where power is exercised; the vote is a formality that occasionally goes wrong.*

**Primitives:** P12 Agenda · P13 Speaking Order · P14 Division · P15 Veto · P16 Recorded Defeat · P17 Clock · P18 Enactment Clock · P19 Competence · P20 Drafting Right · P2 Precedence · P45 Shared Loss.

**Session structure.**

1. **Convening.** Only holders of P12 may convene. *Who calls the session is already a contest.*
2. **Agenda.** The convener states the *relatio*. Others may move amendments, creating several live motions.
3. **Roll.** P13 calls members in precedence order. Each may speak in full, assent to a prior speaker (free, adds their weight to that motion), consume the clock (P17), or hold.
4. **Division.** The chair selects which live motion to put and in what order (P14). **This selection is the chair's principal power and must be an explicit choice, not an automatic sort.**
5. **Veto window.** P15 holders may block. A blocked motion becomes a P16 Record, in force nowhere and citable everywhere.
6. **Enactment.** A carried measure does not take effect. It enters P18 as a multi-stage process with running success and stall, accumulating setbacks, mobilizing its own opposition as it proceeds.

**Design consequences worth stating explicitly:**

- **Sessions are scarce containers.** Without a fixed number of slots, P17 is meaningless and there is no reason to prioritize.
- **P45 is not optional.** Give the polity a failure condition — foreign threat, unrest, fiscal collapse — that ends the campaign badly for everyone. Otherwise a self-interested assembly never agrees and the component is unplayable. This is *The Republic of Rome*'s solution and it is the correct one `[T2]`.
- **Model the drafting layer.** P20 lets a low-ranking character with no vote shape outcomes by writing the resolution. This is the best available answer to "why would a player care about a clerkship."

### 5.3 Component 3 — Settlements and territories

**What it argues:** *governing is not building; it is the continual purchase of compliance from people who have their own institutions.*

**Primitives:** P32 Assessment · P33 Decree with Compliance · P34 Detection & Sanction · P36 Charter · P37 Split Command · P38 Nested Layers · P29 Inspection Circuit · P35 Bond · P26 Term & Rotation · P27 Avoidance.

**The loop, per territory.**

1. **Charter.** On acquisition, negotiate P36. Which local bodies survive? Which taxes may the centre levy? This is a full negotiation scene (§5.1's fourth column), not a menu.
2. **Assessment.** Decide whether to conduct P32. Conducting it converts the territory's holdings into a comparable figure and unlocks proportional obligation — and provokes resistance from everyone whose declared holdings were understated.
3. **Appointment.** Fill the P37 split command, subject to P26 and P27. The two officers report separately; their reports may disagree.
4. **Decrees.** Issue P33. Each decree lands in each locality with a compliance roll, not an effect.
5. **Inspection.** Dispatch P29 on a circuit. Sample the delta between declared and true. Publish findings — which both informs the centre and performs legitimacy to the governed. Both effects are real and separate `[T2 — the *Sindici Inquisitori* commission is explicit on the second]`.
6. **Sanction.** Apply P34, with the detection dial and the severity dial both under the player's control.

**Three anti-patterns this loop exists to prevent:**

- *The decree that just works.* Cured by P33.
- *Conquest as recolouring.* Cured by P36.
- *The omniscient governor.* Cured by P29 + P31: **you do not know your own province's true state.**

**A design consequence about scale.** P38 means the same loop runs at village, city, and province, with the outputs of the lower layer as the declared inputs of the higher. This is how one system covers "manage a settlement" and "govern a territory" without two rule sets.

### 5.4 Component 4 — Diplomacy

**What it argues:** *nothing binds; everything is remembered.*

**Primitives:** P42 Cheap Talk · P43 Costly Signal · P39 Reservation Value · P40 Side Payment · P41 Scaled Compromise · P28 Standing Report · P2 Precedence · P30 Sealed Channel · P44 Positional Pricing · P16 Record.

**Structure.**

1. **Posting.** Assign a representative by grade — *ambasciatore* (capped at two years in post), *inviato straordinario* (single mission), *residente* (below ambassadorial rank) `[T2]`. Grade sets access, precedence, and how much of P28 the posting generates.
2. **Instructions.** The sending body sets the mandate, its reservation value, and what the envoy may concede without referring home. **The gap between the envoy's discretion and his instructions is the component's central tension** and generates its best scenes: an envoy who exceeds his mandate and is repudiated, or who refers home and loses the moment.
3. **Ceremony.** Resolve P2 before substance. Precedence disputes were a genuine and enduring source of inter-sovereign conflict `[T2 — Fletcher]`; a game that skips them is skipping the part that was contested.
4. **Negotiation.** Run §5.1's fourth column. P39 defines the overlap; P40 can shift a stance without moving a position; P41 scales the settlement to what winning cost.
5. **Instrument.** The agreement is P42 by default — non-binding. Making it bind requires P43: a hostage (P35), a marriage, an advance payment, or a public oath sworn before a body that will record it (P3 + P16).
6. **Report.** On recall, the envoy updates the standing P28 *relazione*. It persists, decays, is inherited by his successor, and can be stolen.

**The multilateral case.** With three or more powers, add P44: alliance options sit in a priced array where taking the one you want funds the alternatives for everyone else. This produces the characteristic Italian pattern — a league forms, and the act of forming it pays for the counter-league.

---

## §6 — Content navigation

Two navigation problems, and they are different: how the **player** moves through political content, and how **you** author and maintain it.

### 6.1 The content graph

Content is not a tree of scenes. It is a graph over the five substrate objects (§4.0), and there are exactly four node types:

- **Positions** — authored stances on authored questions, each tagged with the stasis it lives at and the Bodies competent to hear it. Reusable across scenes.
- **Claims** — authored argument objects with premises, warrants, provenance, and the attack types they are vulnerable to. These are the real content unit; write these, not dialogue.
- **Records** — generated, not authored. Every resolved scene emits one. Records are the campaign's memory and the material for later citation.
- **Frames** — authored scene shells: which Body, which primitives are on, where P9 starts, what the P45 stakes are.

The consequence for writing: **you author Claims and Frames; the game generates Records; Positions connect them.** Dialogue is a rendering of a Claim, not the Claim itself, which is what allows the same Claim to appear as a Senate speech, a tribunal charge, and an ambassador's report with different surface text.

### 6.2 How the player navigates

- **Within a scene:** the stasis gate (P5) *is* the navigation. It tells the player what is currently arguable and what is foreclosed. This is the answer to the standard problem of debate scenes — that the player cannot tell what a given line will do — because the gate publishes the current question.
- **Between scenes:** by Record. A player pursues a matter by finding the forum whose competence covers it (P19) and whose burden placement (P9) favours him. **Forum-shopping is the primary navigation verb of the whole game**, and P10 is its in-scene expression.
- **Across a campaign:** by document. The *relazione* (P28), the domain law code (P36), the register of assessment (P32), and the archive of vetoed motions (P16) are the four persistent documents. A player who reads them plays better. They are also the natural place to put the game's writing.

### 6.3 Authoring economics

The single decision that determines whether this is buildable: **how much is authored and how much is generated.** The recommendation, derived from what §3 shows works:

- **Author:** Claims, Positions, Frames, characters' Commitments, and the charter terms available for each territory type. High density, low volume — a few hundred well-structured Claims beat thousands of lines of branching dialogue, because P7's three attack types multiply each Claim's usable surface by roughly three.
- **Generate:** Records, Assessment figures, compliance outcomes, inspection findings, precedence disputes, and the Enactment Clock's stage events.
- **Never generate:** the framing of a question (P12) or the terms of a charter (P36). Those are where the game's authored voice lives, and procedural versions read as noise.

### 6.4 Pacing

Three clocks, and they should be visibly out of phase with each other:

- **Session clock** (P17) — minutes. Scarce slots inside one sitting.
- **Enactment clock** (P18) — months. A measure grinding through stages while the world moves.
- **Term clock** (P26) — years. Offices turning over, killing plans mid-execution.

Old World's solution to the third is worth copying directly: goals emitted by the intersection of a ruler's attitudes with the desires of the influential houses, and put on a countdown when the ruler dies `[T2]`. Mortality as the pacing device costs nothing and produces constant, legible pressure.

---

## §7 — Adversarial audit

`[SELF-AUTHORED — bias risk]` The same process built §§1–6 and attacked them here. The characteristic failure of that arrangement is attacking what is easy to attack and defending what one is attached to. The end of this section names what an independent reviewer would add that this pass is structurally unlikely to find.

**Verdict: the substrate and the borrowed primitives are sound; the novel core is not yet a mechanic, and the document oversells it.** Eleven findings, severity-ranked.

### Severe

**A1 — The stasis-gate resolution system is unproven and §4.2's fix for Constraint C1 is a content dependency wearing a mechanic's clothes.**
§3.5 correctly reports that nothing in the survey models argument content, and §4.2 proposes filling that space. But the claim that "no verb dominates because the correct attack depends on the claim's structure" holds only if the authored Claim corpus is genuinely varied in structure. If most Claims rest on witness testimony, Undermine dominates and the design has reproduced exactly the Point/Dismiss collapse it cited Burning Wheel to avoid — with more rules and the same outcome. **The fix was asserted at the mechanical layer and actually lives at the content layer, which the document did not say.**
*Remedy:* make Claim-type distribution a testable authoring invariant (no attack type optimal for more than ~40% of the corpus in any given scene's draw), and prototype the loop on paper with 20 Claims before committing to it.

**A2 — P11 plus P5 compound the defence's information deficit across stases, and the Inquisition column is deliberately unwinnable.**
The array is hidden, the gate advances on accuser wins, and each advance costs the defence actions it could have spent probing. Historically that is exactly right — that is why inquisitions convicted. Historical fidelity is not a defence against the scene being unpleasant to play. §5.1 answers this by declaring abjuration a P41 compromise rather than a loss, which is well-grounded historically (abjuration was the usual conclusion of an inquiry `[T2 — Hill]`) but is *asserted, not demonstrated*: nothing in §4 or §5 specifies how much a player can improve his abjuration terms, or whether that improvement is legible while playing.
*Remedy:* specify the compromise ladder for the inquisitorial forum explicitly, and show the player the current terms at all times, so the scene reads as negotiating downward rather than losing slowly.

### High

**A3 — Forty-five primitives is a designer's vocabulary presented as though it were a player's.**
Composition rule 1 claims one vocabulary. Burning Wheel offers seven debate manoeuvres and players collapsed to two `[T2]`. The document never separates player-facing verbs (P7, P8, P10, P11, P13, P17) from designer-facing structures (P19, P32, P38, P44) from world-model state (P1, P31). Presenting them in one flat catalogue makes the design look more usable than it is.
*Remedy:* re-tier the catalogue into Verbs / Structures / State. Player-facing verbs should number under a dozen per scene type.

**A4 — P18's parameters are borrowed with its structure, and they do not transfer.**
The 100-day stage, the 2× and 1.5× class multipliers, and the legitimacy bands are tuned for a nation-state grand strategy running 1836–1936 `[T0 — Victoria 3]`. A character-driven Renaissance game whose parliament is a city council with two-month magistracies (§2.1, Florence) cannot use them. The document presents the numbers as if the loan were total. **The structure transfers; the tuning does not, and only the structure was actually researched.**

**A5 — There is no economy.**
Standing, actions, session slots, money, favours, and time all appear and none is unified. P40 (side payments) and P44 (positional pricing) both presuppose a fungible currency that the catalogue never defines. P8 "costs an action" and P17 "consumes a session slot" without either being specified as the same or different resources. This is a genuine hole, not a level-of-detail choice.
*Remedy:* define the resource set before any further mechanical work. Everything in §4 depends on it and none of it was written against it.

### Medium

**A6 — P1 indexed per body multiplies state without a presentation answer.** N bodies × M actors is a real tracking and display burden and the document offers nothing on it. The primitive is right; its cost is unacknowledged.

**A7 — P24's "spend decision at every widening" is a placeholder.** The document asserts the Venetian chain must be playable at each stage rather than a cutscene, then does not say what the player spends or on what. The primitive's whole claim to being a mechanic rests on this and it is empty.

**A8 — Aristotle is used decoratively.** §2.7 and §4.3 P19 present the tripartite division as the game's description language for any polity. No assembly in §5 is then described in those terms. Either use the schema to specify the four components' constitutions explicitly, or stop claiming it as an analytic skeleton.

**A9 — P45 Shared Loss is a multiplayer solution imported into what is probably a single-player game.** In *The Republic of Rome* the shared-loss condition disciplines *other humans* `[T2]`. In single-player it disciplines AI factions, which requires those factions to model long-horizon self-interest well enough to defect and then relent — a substantially harder problem than the document acknowledges. §5.2 calls P45 "not optional" without noting that its cost is an AI problem, not a rules problem.

### Low

**A10 — The Inquisition sourcing is second-hand.** Gui's *Practica* and Eymerich's *Directorium* were not read; the account rests on Hill's 2019 study `[T2]` and, for the specific trial figures, on Lea `[T2]`, a nineteenth-century work with a known polemical slant. The withheld-names mechanic is securely attested; the procedural detail around it is not first-hand. `[TIER-FLOOR: T2 — primary manuals not consulted]`

**A11 — Hermagoras is doubly transmitted and the document should say so louder.** No original fragments survive; the four-stasis scheme reaches us through Cicero's *De Inventione* and later refinement `[T1]`. §4.2 flags this but §5.1 then treats the four stases as a settled historical object. For game purposes the transmission is fine — Cicero's version is the one that shaped European legal rhetoric for fifteen centuries — but the claim should be stated as "the Ciceronian stasis scheme," not "Hermagoras's."

### What the attack failed to break

Reported as survivals, not as compensating praise. Each was attacked and held.

- **P16 Recorded Defeat.** Attacked for being a curiosity; it is not. *Senatus auctoritas* is a real, named Roman category for a motion carried and stripped of force `[T1]`, it is nearly free to implement, no game in §3 has it, and it solves a concrete problem — giving losing players a durable asset. **Survived.**
- **P41 Scaled Compromise.** Attacked as untested; it is the opposite, having been in print and in play since 2002 `[T0 — Burning Wheel]`, and the documented complaints about that system concern manoeuvre balance, never the compromise rule. **Survived.**
- **P33 Decree with Compliance.** Attacked as adding friction for its own sake; the historical evidence is unusually strong, since the capitulary record itself repeats the same prohibitions, which is documentary proof that promulgation did not equal enforcement `[T2 — Ganshof]`. **Survived.**
- **P37 Split Command.** Attacked as micro-management; it is self-balancing, well-attested in two unconnected systems (Venetian *rettori*, Carolingian *missi* pairs) `[T1/T2]`, and generates local texture at near-zero rules cost. **Survived.**
- **The §4.0 five-object substrate.** Attacked by attempting to find a scene in §5 requiring a sixth object type. None found across four scene families. **Survived.**

### What an independent reviewer would add and this pass structurally could not

`[BIAS: self-review — the following are the blind spots most likely to remain]`

1. **The entire document assumes turn-based, scene-bounded play.** Nothing in the brief said so. If the game is real-time, open-world, or party-based action, §5 largely does not apply and §4 would need re-cutting around continuous rather than discrete resolution. This assumption was made silently in §4.0 and never examined.
2. **No consideration of how any of this is presented.** Every primitive is specified as state and resolution; none is specified as something a player looks at. A system this procedurally dense fails on legibility long before it fails on balance, and the document contains no interface thinking at all.
3. **No player-fantasy check.** The document asks throughout what is historically true and what composes cleanly. It never asks what is *fun to be* — whether players want to be the inquisitor, the accused, the clerk who drafts, or the ambassador, and whether the same system serves all four.

---

## §8 — Gaps and open questions

`[GAP: resource economy — not specified; see A5. Everything mechanical in §4 depends on it]`
`[GAP: presentation and legibility — no interface model; see independent-reviewer note 2]`
`[GAP: play mode — turn-based scene structure assumed without warrant; see note 1]`
`[GAP: AI opposition model — P45 and P18's counter-mobilization both presuppose factions that plan; not addressed]`
`[GAP: primary inquisitorial manuals — Gui and Eymerich not read directly; TIER-FLOOR T2]`
`[GAP: Sengoku bunkokuhō texts — the Takeda *Kōshū hatto no shidai* is cited only through a secondary encyclopedia; the codes themselves would repay direct reading for charter (P36) content]`
`[GAP: Byzantine and Ottoman practice — outside the stated brief but both are strong sources for P29 inspection and P36 charter, and their omission is a choice, not a finding]`

**Three questions the design cannot proceed past without answers from you:**

1. **What is the player's position?** A single character across a life (Old World / CK3), a house across generations (Pax), or a faction with no body (Republic of Rome)? Everything in §4.1 and §5.4 changes shape depending on the answer.
2. **What is the resource economy?** See A5. This blocks further mechanical work outright.
3. **Is this multiplayer?** P45 and P42 are both substantially different rules in single-player, and A9 is only a problem in one of the two cases.

---

### Audit trail

`[READ: available_skills, /mnt/skills/public, /mnt/skills/user — no markdown, research, or game-design skill present; no uploads to read]`
`[SOURCE: T0 — Aristotle, Politics IV 1298a (Perseus); Victoria 3 official wiki (game files); Pax Pamir 2e rulebook; Burning Wheel Gold]`
`[SOURCE: T1 — Britannica (missi dominici, Taikō kenchi, bakuhan); Perseus Dictionary of Greek and Roman Antiquities (intercessio, senatus auctoritas); Prakken 2010; Dung 1995; Walton 1996/2008; Ostrom 1990 via four independent secondaries; chinaknowledge.de (fengbo, piaoni); Ming Studies 92 (2025); Queller and Goffman on relazioni; Mowbray & Gollmann on the ducal protocol]`
`[SOURCE: T2 — Hill 2019 (inquisition manuals); Lea I.x (withheld names, partisan); Brill Factional Struggles (Vicenza); it.wikipedia Sindici Inquisitori (1566 commission); acoup.blog (CK3 critique); Burning Wheel forums (Duel of Wits balance); Game Developer (Danganronpa structure); Fletcher and Mallett (Renaissance diplomacy)]`
`[AGGREGATOR-ONLY: grokipedia, tvtropes, retail listings — used for orientation only; no load-bearing claim rests on them]`
`[CONFLICT: Mattingly's resident-ambassador thesis vs. Mallett/Fletcher's qualification — resolved by tier and recency; the qualified account is reported in §2.6]`
`[UNVERIFIED: Hermagoras's own formulation of stasis (no fragments survive); Victoria 3 counter-mobilization figures against current patch; Pentiment specific mechanics]`
`[CONFIDENCE: high — historical mechanism identification and game-precedent survey. medium — the stasis-gate design in §4.2, per finding A1. low — any parameter value in §5, per A4]`
`[PASS-3: §§1–6 constructed bottom-up from named sources; §7 attacked them and landed eleven findings, five of which the attack failed to break; A1–A5 remain open and are the correct next work. Document is complete against the brief as stated, incomplete against the three questions in §8.]`
