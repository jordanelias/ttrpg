# VALORIA — Research Corpus: Rhetoric, Oratory, Debate, Appeals, Assemblies, Trials & Negotiation

<!-- STATUS: RESEARCH — multilingual historical grounding; not a design doc, not canonical mechanic. -->
<!-- Feeds: social_contest_v30 (+ RATIFIED_2026-06-01 redesign), Parliamentary Vote/Stay, Excommunication Tribunal, investigation/evidence, articulation layer, diplomacy/treaty work. -->
<!-- Proposed repo home: research/rhetoric_oratory_contest/ (mirrors research/pre_firearms_formations/). -->
<!-- Method: primary treatise → structural pattern → cross-tradition throughline → Valoria mapping. -->
<!-- Date: 2026-06-02. -->

---

## 0. MANIFEST

### 0.1 Why this corpus exists (the gap)

The repository already grounds its **military** systems in a deep historical corpus (`research/pre_firearms_formations/`, 17 files) and grounds **political-structural** dynamics in `references/historical/precedents_analysis.md` and the 2026-04-28 political-dynamics session. It does **not** have an equivalent corpus for **rhetoric, oratory, debate, appeals, assemblies, trials, and negotiation** — despite the fact that the social-contest system is *already built on named rhetorical theory*:

- `designs/audit/2026-06-01-contest-redesign/RATIFIED_2026-06-01.md` CR4 keys the whole resolution surface to **Ciceronian stasis × genre**.
- CR5 grounds self-gating obstruction in **Quintilian / Nyāya**.
- "Face" is **Aristotelian ethos** reified as a tracker.
- The Excommunication Tribunal (§7.1 of `social_contest_v30`) and the Parliamentary Vote/Stay (§10/§10.1) are forensic and deliberative venues with no underlying source study.

So the design cites Cicero, Quintilian, and Nyāya by name with nothing behind the names. This corpus supplies that substrate, multilingually, and maps it back to the live systems.

`[READ: designs/scene/social_contest_v30_index.md — full index (42 headings)]`
`[READ: designs/audit/2026-06-01-contest-redesign/RATIFIED_2026-06-01.md — full]`
`[READ: references/historical/precedents_analysis.md — §1 + structure (57k chars, partial)]`
`[READ: designs/audit/2026-04-28-political-dynamics-session/02_initial_proposals_with_historical_precedents.md — Proposals 1–2 + structure (30k chars, partial)]`

### 0.2 Scope

Two axes, crossed.

**Genres** (the user's targets): treatises on the art of persuasion; royal appeals / petitions; parliamentary & assembly debate; public / ceremonial speech; trials & forensic pleading; negotiation & diplomacy.

**Traditions** (the multilingual reach): Greek, Latin, Byzantine Greek, Arabic, Classical Chinese, Sanskrit, medieval Latin and the European vernaculars, Old Norse. The setting's Norse-flavoured naming (Solmund, Niflhel) and its Crown/Church/Parliament/territory structure make the medieval-European and Norse strands load-bearing; the non-European strands are included because they *isolate variables the European tradition fuses* (see §4 dyadic persuasion, §5 self-gating).

### 0.3 Method

Per the project-owner contract's top-down anchor: each tradition is read for its **primary treatises** (title, author, date, language), reduced to the **structural pattern** it models, abstracted to a **cross-tradition throughline**, and mapped to the **Valoria system** it can validate or inform. Mechanical mappings in §9 are proposals built bottom-up from the sources and are **Jordan-vetoable**; none rewrites authored canon, metaphysics, world, or character.

**On "multilingual" — interpretation stated.** This corpus reads *multilingual* as **coverage across language-traditions** (Greek, Latin, Arabic, Classical Chinese, Sanskrit, the medieval vernaculars, Old Norse), with each tradition's primary terms and titles given in their **source script or transliteration** (鬼谷子, *balāgha*, *nyāya*, τελικὰ κεφάλαια, etc.). It does **not** claim that the sources *consulted this session were read in those original languages*: the session's verification drew predominantly on **English-language scholarship about** these traditions (encyclopaedic, academic, and reference sources; see §11). If the intended sense was *primary-source reading in each language*, this document is a structured **secondary-source map** that identifies the primary texts to read — not a substitute for reading them. **Update (2026-06-02, two passes):** §12 now carries **primary-language academic scholarship across eight traditions** — Arabic, Chinese, French, German (§§12.1–12.4) and Byzantine Greek, Hindi/Sanskrit, Italian, Old Norse/Icelandic (§§12.5–12.8) — each capturing framing the English reception flattens. Remaining English-only strands are peripheral (e.g. the broader Latin theoretical tradition, whose primary texts are themselves the works listed in §10). `[ASSUMPTION resolved: "multilingual" read as tradition-coverage with primary-language *scholarship* per Jordan's clarification; reading every primary text in its original language is still not separately claimed.]`

### 0.4 Confidence & contested attributions

Grounding is **not uniform** across this corpus, and the document marks which is which rather than letting polish imply uniform verification.

**Web-verified this session (2026-06-02; see §11 source register for search→claim mapping):** the Greco-Roman spine — the three genres (deliberative/forensic/epideictic), the three *pisteis* (ethos/pathos/logos), the five canons, the four classical stases including *translative = jurisdiction*, the canon of ten Attic orators, Lysias as master logographer, and the Demosthenes→Cicero *Philippics* lineage; Arabic *balāgha* (the Jurjānī→Sakkākī→Qazwīnī lineage and the *maʿānī/bayān/badīʿ* tripartition) and chancery *inshāʾ* (al-Qalqashandī's *Ṣubḥ al-aʿshā*, 1412); the Chinese persuasion-school (*Guiguzi*, Han Feizi's *Shuinan*); Nyāya formal debate (*vāda/jalpa/vitaṇḍā*, *nigrahasthāna*); the *ars dictaminis* five-part letter; the English petition corpus; and the ambassador literature.

**Recall-level (standard reference knowledge, NOT re-verified by a returned source this session — treat as high-confidence-but-uncited, not as session-grounded):**
- `[UNVERIFIED]` Cicero's individual forensic speech titles (*In Verrem*, *Pro Milone*, *Pro Caelio*, *Pro Roscio*) — the corpus is canonical and the attribution is standard, but no search this session returned these specific titles.
- `[UNVERIFIED]` the term *ethopoeia* for Lysias's character-fitting — standard, not echoed by a returned source this session.
- `[CONFIDENCE: medium]` *ars arengandi* corpus specifics (Matteo dei Libri / Jacques de Dinant) — drawn from standard reference knowledge, less web-verified this session.

**Corrected this session (was overstated in the first draft):**
- `[CONFIDENCE: low]` **The deliberative "final headings."** §1.4 originally presented a clean six-item list (legality/justice/usefulness/possibility/honour/consequences) as canonical "deliberative stases." This is a **conflation** and is downgraded. What *is* verified: Aristotle's deliberative special topics are **the good and the advantageous** (in paired form, *Rhet.* 1.4–8; cf. *Cic. De Inv.* 2.52–58), and **the honourable/shameful is the *epideictic* axis, not the deliberative one**. A later doctrine of *practical/final headings* (τελικὰ κεφάλαια) resembling the six-item list does exist in the Hermogenic/Byzantine tradition, **but its exact membership and its attribution to Hermogenes as "deliberative stases" were not verifiable this session** — and "stasis" is properly the *forensic* terrain doctrine, distinct from deliberative *topoi/kephalaia*. Do not treat the six-item list as confirmed canon; see §1.4 and §9.2.

**Academic re-grounding pass (2026-06-03):** a self-audit found §12's citations uneven — roughly half peer-reviewed, half tertiary (Wikipedia / blogs / forums), with two strands (Byzantine §12.5, Nyāya §12.6) resting on blogs/Wiktionary even where the underlying facts were standard, and several academic names cited second-hand. In response: §12.1 (Arabic), §12.5 (Byzantine), §12.6 (Nyāya) were regrounded on peer-reviewed scholarship (Larkin / Abu Deeb; Russell & Wilson / Loeb Menander / Omissi & Ross / Kennedy; Matilal / Vidyabhūṣaṇa / Dharmakīrti); **Heath (1994) was fetched and read directly**, correcting §1.4 / §12.4 — Hermagoras *excluded* the legal/textual questions from the staseis, so the *status legales* "axis" is later Latin/Hermogenic systematization, not his own. §10 is now split into **§10.A (consulted)** vs **§10.B (field bibliography, not all consulted)**, and a per-strand **source-tier table** (`[PR]`/`[REF]`/`[PRIM]`/`[TER]`) sits in **§11.5**. Second-hand citations (Barwick, Braet) are flagged as via-Heath. Net: the spine and the French/German/Italian strands were already academically sourced; this pass brought Arabic, Byzantine, and Nyāya up to the same standard and made the tertiary material corroborating rather than load-bearing.

**Contested attributions (scholarly dispute, flagged inline at point of use):**
- `[CONFIDENCE: medium]` *Guiguzi* authorship/dating (traditional 4th c. BC attribution to "Master of Ghost Valley"; text likely Warring-States→Han composite).
- `[CONFIDENCE: medium]` du Rosier as "first" Western ambassador treatise (Mattingly's claim; Lucas de Penna's *De legationibus* commentary and Martino Garati da Lodi are contested rivals).
- `[CONFIDENCE: medium]` *Modus Tenendi Parliamentum* exact date/purpose (Edward I vs Edward II; manifesto vs treatise vs reform-programme — unsettled).
- `[CONFIDENCE: medium/low]` exact membership and origin-date of the **canon of ten Attic orators** — the ten names are stable, but the canon's formation is debated (Alexandrian attribution to Aristophanes of Byzantium / Aristarchus vs A. E. Douglas's argument that it crystallised only in the 2nd c. CE).

---

## 1. CLASSICAL GREECE & ROME — the source code

Everything downstream (Byzantine, Arabic via translation, medieval Latin, the European vernaculars) is a reception of this layer. It is the system's actual ancestor: the RATIFIED redesign's vocabulary is Greco-Roman.

### 1.1 Greece: the sophists, Isocrates, Plato, Aristotle

Rhetoric as a teachable *technē* begins in 5th-c. BCE Sicily and Athens (Corax/Tisias by tradition; Gorgias of Leontini as the dazzling practitioner). The sophists sold persuasion as power; **Plato** attacked it as cosmetic flattery in the *Gorgias* and then, in the *Phaedrus*, conceded a "true rhetoric" disciplined by dialectic and a knowledge of souls. **Isocrates** (*Against the Sophists*, *Antidosis*) institutionalised rhetoric as civic education (*paideia*).

**Aristotle's *Rhetoric*** (three books, mid-4th c. BCE) is the foundational systematic treatise and supplies the spine the whole field still uses:
- **Three modes of proof (pisteis):** *ethos* (the speaker's projected character), *pathos* (the audience's emotional state), *logos* (the argument itself, via *enthymeme* — the rhetorical syllogism — and *paradeigma* — the example).
- **Three genres,** keyed to audience-role and time: **deliberative** (*symbouleutikon*; an assembly deciding future action; the question is the advantageous/harmful), **forensic/judicial** (*dikanikon*; a court judging a past act; the just/unjust), **epideictic** (*epideiktikon*; an audience as spectator in the present; the honourable/shameful — praise & blame).
- **Topoi** (commonplaces): the reusable seats of argument.

### 1.2 The three genres as a typology of "contests"

This is the single most important inheritance for Valoria: persuasion is not one activity but three, distinguished by **who judges and what they decide.** A parliamentary vote is deliberative; a tribunal is forensic; a coronation oration or a funeral eulogy is epideictic. The genres do not share a win condition. (Valoria's CR4 "genre = stance," authored as Memory/Projection, is a deliberate compression of this; see §9.)

### 1.3 The five canons; the orator's pipeline

Roman pedagogy fixed the production pipeline as five **canons**: **inventio** (finding the arguments), **dispositio** (arranging them), **elocutio** (style/wording), **memoria** (memorisation), **pronuntiatio/actio** (delivery — voice and body). This is a *process model*, not a content model — it describes the stages a speaker moves through, which is exactly the shape of a turn-structured resolution system.

### 1.4 Stasis / status — the doctrine the redesign runs on

**Hermagoras of Temnos** (2nd c. BCE; antecedents in Gorgias) invented **stasis theory** (*stasis*, pl. *staseis*; Latin *status* / *constitutio*): a method for locating the precise **point on which a dispute turns**, so the arguer knows which line of argument is even relevant. The four classical stases:

1. **Conjectural** (*an sit* — "did it happen?"): a question of **fact**.
2. **Definitional** (*quid sit* — "what is it?"): a question of **classification/naming** — granted the act, is it *this* crime or another?
3. **Qualitative** (*quale sit* — "what kind / was it justified?"): a question of **evaluation** — granted the act and its name, was it warranted, mitigated, defensible?
4. **Translative** (*translatio* — "is this the right venue/procedure?"): a question of **jurisdiction** — should this case even be heard here, now, by these judges?

The fullest surviving accounts are **Latin**: the anonymous **_Rhetorica ad Herennium_** (c. 80s BCE — the earliest complete Latin rhetoric, and the source of the memory-palace), **Cicero's _De Inventione_** (1.10–19), with later refinements in his *De Oratore*, *Topica*, *Partitiones Oratoriae*, and **Quintilian's _Institutio Oratoria_** (3.5–6, 7.2). **Hermogenes of Tarsus** (*On Issues / Peri staseōn*, 2nd c. CE) and Zenon elaborated the forensic system to **13 status** — but German *Staseislehre* scholarship shows these were tailored for *fictional declamation in the rhetoric schools*, not forensic practice (the imperial forum had declined); Quintilian, by contrast, worked at a *practicable reduction* (§12.4). Hermagoras himself, however, **excluded** the legal/textual questions (*nomika zētēmata* — letter vs. intent, ambiguity, conflicting statutes) **from** the staseis; their packaging as a parallel set of *status legales* is the **later Latin/Hermogenic systematization** (corrected in §12.4, via Heath read directly) — though as a statutory-dispute vocabulary it remains directly relevant to a game with edicts. **Deliberative argument was organised separately** — by *topoi* and, in the later tradition, **final/practical headings** (τελικὰ κεφάλαια), *not* by stases. A practical-headings list resembling *legality / justice / advantage / feasibility / honour / outcome* circulated in the Hermogenic/Byzantine tradition, **but its exact membership and its attribution were not verifiable this session** `[CONFIDENCE: low — see §0.4]`. What is verified for the deliberative genre is narrower: Aristotle's deliberative topics are **the good and the advantageous** (*Rhet.* 1.4–8), with the honourable belonging to the *epideictic* genre. Stasis itself (the forensic terrain doctrine) stayed central to the rhetorical curriculum for the whole pre-modern period; the clean *four*-stasis scheme is the canonical textbook form, though Hermagoras's own system was more elaborate and the tidy four owes much to Ciceronian transmission `[CONFIDENCE: medium]`.

> **Why it matters mechanically:** stasis is a *terrain* mechanic. Before you choose a tactic you must diagnose what the fight is actually about, because arguments appropriate to a fact-dispute are useless in a justification-dispute. Valoria CR4 ("stasis = terrain; definitional = higher-order reframe; translative = pre-merits jurisdiction = the Stay") is a direct lift — and this corpus **confirms it is well-founded** (the four stases and *translative = jurisdiction* are session-verified; CR4's canonical wording was re-read this session). Separately, the later **deliberative final headings** (τελικὰ κεφάλαια) *might* furnish a ready-made vocabulary for the Parliamentary layer — but that list is `[CONFIDENCE: low / UNVERIFIED]` (§0.4), so §9.2 carries it as a candidate to confirm, **not** as established canon to lift.

### 1.5 The Attic orators & forensic logography; Roman forensic practice

Theory had a practitioner wing. Athens produced the **canon of ten Attic orators** (Antiphon, Andocides, **Lysias**, Isocrates, Isaeus, Aeschines, Lycurgus, **Demosthenes**, Hyperides, Dinarchus). Because litigants had to speak for themselves, a profession of **logographers** (ghost-writing speechwriters) arose; **Lysias** was its master, prized for fitting the speech to the speaker's character (*ethopoeia*) — an ethos engine. **Demosthenes'** *Philippics* are the deliberative monument; his forensic and political speeches the rest. At Rome, **Cicero's** courtroom corpus (*In Verrem*, *Pro Milone*, *Pro Caelio*, *Pro Roscio*) is the applied stasis-and-ethos textbook: each is legible as a stasis choice plus a character contest.

### 1.6 Throughline

Persuasion = (1) diagnose the **stasis** (what is this fight about?), (2) marshal **ethos / pathos / logos** against the relevant heads, (3) inside a **genre** that fixes the judge and the win condition, (4) through a staged **pipeline** of invention→arrangement→style→delivery. This four-part skeleton is the master template; every later tradition is a variation, a specialisation, or a re-emphasis of one limb.

---

## 2. BYZANTINE GREEK & THE PROGYMNASMATA LADDER

The Eastern Roman continuation matters for two reasons: it produced the **graded-exercise curriculum** (a progression system) and the **ceremonial / diplomatic-protocol** literature (a court system).

### 2.1 The progymnasmata — rhetoric as a skill tree

The **_progymnasmata_** were a fixed ladder of preliminary composition exercises, each harder than the last, taught for a millennium. The surviving manuals are by **Aelius Theon** (1st c. CE), **(ps.-)Hermogenes**, **Aphthonius of Antioch** (4th–5th c. — by far the most influential, the standard schoolbook into the Renaissance), and **Nicolaus the Sophist**. Aphthonius' fourteen exercises, in ascending difficulty: *fable, narrative, chreia (anecdote), maxim (gnōmē), refutation, confirmation, commonplace, encomium, invective, comparison (synkrisis), ethopoeia (speech-in-character), ekphrasis (vivid description), thesis (abstract debate), and proposal/refutation of a law.*

> **Why it matters:** this is a **competence ladder** — the historical model for how a persuader is *trained up*, and a clean reference if Valoria ever wants character-progression in the social domain to feel grounded rather than arbitrary (e.g., low-skill actors can only manage narrative/chreia-grade moves; reframing/*ethopoeia* unlocks higher). The exercises also pre-name several Valoria move-types: *synkrisis* (comparison) and *ethopoeia* (arguing as another's character — a Mask move).

### 2.2 Ceremonial & court oratory; the basilikos logos

**Menander Rhetor** (3rd c. CE) codified epideictic into recipe-form, including the **_basilikos logos_** — the imperial encomium, a step-by-step template for praising a ruler. Byzantine court culture ran on this scripted praise. It is the ancestor of the coronation oration and the formal address-to-the-sovereign — the *ceremonial* register of "royal appeals" (§8).

### 2.3 Diplomatic protocol

Constantine VII Porphyrogenitus' **_De Ceremoniis_** (10th c.) and **_De Administrando Imperio_** document the Byzantine theory of dealing with foreign powers as a graded protocol of precedence, gifts, and staged audience — diplomacy as ritual hierarchy rather than free negotiation. A useful contrast-case for §8.3.

### 2.4 Throughline

Byzantium turns rhetoric into (a) a **trainable ladder** and (b) a **court protocol**: persuasion embedded in fixed ceremonial slots. Where Athens improvised in open assembly, Byzantium scripted. Both poles are useful — the open contest and the slotted ceremony.

---

## 3. THE ARABIC–ISLAMIC TRADITION

Three distinct strands, only one of which (the chancery) is usually noticed by game designers — and that one is the direct analogue of *royal appeals*.

### 3.1 ʿilm al-balāgha — the science of eloquence

Arabic rhetorical theory (*balāgha*) crystallised around the doctrine of Qur'anic **inimitability** (*iʿjāz*) but produced a general analytic of persuasive language. The lineage is well-attested:
- **ʿAbd al-Qāhir al-Jurjānī** (d. 471/1078), *Dalāʾil al-iʿjāz* ("Proofs of Inimitability") and *Asrār al-balāgha* ("Secrets of Eloquence") — the foundational theory of *naẓm* (construction/word-order as the seat of meaning). The deep insight: meaning lives in syntactic arrangement, not in isolated words.
- **Fakhr al-Dīn al-Rāzī** (d. 606/1209), *Nihāyat al-iʿjāz* — systematised al-Jurjānī.
- **al-Sakkākī** (d. 626/1229), *Miftāḥ al-ʿulūm* ("The Key to the Sciences") — fixed the **canonical tripartite division** of *balāgha*: **ʿilm al-maʿānī** (the science of meanings — how syntax fits situation/context), **ʿilm al-bayān** (clarity — simile, metaphor, metonymy), **ʿilm al-badīʿ** (figures of embellishment).
- **al-Qazwīnī** (d. 739/1338, "the orator of Damascus"), *Talkhīṣ al-Miftāḥ* (a memorisable digest) and *al-Īḍāḥ* (its expansion) — these became *the* madrasa textbooks of rhetoric across the Islamic world for centuries.

Notably, **ʿilm al-maʿānī** is a theory of **fitting utterance to context (*muqtaḍā al-ḥāl*, "the requirement of the situation")** — a near-exact parallel to the audience-conditioning the Caraka/Nyāya tradition formalises (§5) and to "format follows context" (social_contest §1).

### 3.2 The oratorical / *adab* strand

Older and more directly about *speaking*:
- **al-Jāḥiẓ** (d. 255/868–9), *al-Bayān wa-l-tabyīn* ("Clarity and Clarification") — the great anthology-cum-treatise on eloquence, oratory (*khuṭba*), the speech of preachers and envoys, fluency vs. stammering, the ethics of speech.
- **Qudāma ibn Jaʿfar** (d. c. 337/948), *Naqd al-shiʿr* — critical method.
- **Ibn al-Muqaffaʿ** (d. c. 139/756), *Kalīla wa-Dimna* (from the Sanskrit *Pañcatantra*) — statecraft and persuasion taught through animal fable; a mirror-for-princes by indirection.

### 3.3 The chancery / *inshāʾ* — the analogue of royal appeals

This is the Arabic counterpart to the Latin *ars dictaminis* (§6.1), and the most directly relevant strand for petitions to power. The **secretary (*kātib*)** was a high officer; the **art of composition (*inshāʾ*)** governed official correspondence, decrees, and petitions:
- **ʿAbd al-Ḥamīd al-Kātib** (d. 132/750), founder of Arabic chancery prose; his *Risāla ilā l-kuttāb* ("Epistle to the Secretaries") is the genre's charter, defining *inshāʾ* and the rules for **supplication (duʿāʾ)** and formal address.
- **al-Ṣūlī** (d. 335/946), *Adab al-Kuttāb*; **Ibn Mammātī**, *Qawānīn al-dawāwīn* (chancery regulations).
- **al-Qalqashandī** (d. 821/1418), **_Ṣubḥ al-aʿshā fī ṣināʿat al-inshāʾ_** (completed 1412; 14 volumes) — the encyclopaedic culmination: composition formulae, titulature, the protocol of how a petitioner of each rank addresses each rank of authority, the structure of grievances and requests. More than fifty *inshāʾ* manuals appeared across the five centuries from al-Ṣūlī to al-Qalqashandī.

> **Why it matters:** *Ṣubḥ al-aʿshā* is, functionally, a **rank-indexed protocol table for petitioning power** — exactly the data a "submit an appeal to the Crown / to the Church" system needs. The required register, formula, and deference-level are a *function of the petitioner's standing relative to the addressee* — i.e., a self-gating-by-standing mechanic (cf. §5, §9.1).

### 3.4 Throughline

Arabic gives three gifts: (1) **maʿānī** = persuasion as situation-fitting (context-conditioned utterance); (2) **al-Jāḥiẓ's** practical oratory/envoy lore; (3) the **chancery** as a rank-and-register protocol for appeals — the single best historical template for a structured petition-to-sovereign subsystem.

---

## 4. THE CHINESE TRADITION — persuasion as a two-body problem

The Chinese material is the most valuable *contrast* case, because it isolates a variable the Greek tradition fuses: it theorises persuasion as a **dyadic** act — one persuader, one ruler — rather than as **public** oratory before a crowd. (Scholarship on the Guiguzi states this contrast directly: European rhetoric grew up in the assembly and the courtroom; the Guiguzi's strategies focus on the individual counterpart.)

### 4.1 The School of Diplomacy (*zonghengjia* 縱橫家)

The **_Guiguzi_** 鬼谷子 ("Master of Ghost Valley"; traditionally 4th c. BCE, `[CONFIDENCE: medium]` on dating/authorship — likely a Warring-States→Han composite, later absorbed into the Daoist canon) is the founding text of the **School of Vertical and Horizontal Alliances**. Its art is **covert** persuasion: silent observation, assessing the counterpart's disposition (*qing* 情), and steering so the decision *appears self-made*. Core devices include *bai-he* 捭闔 (opening and closing — when to draw out vs. shut down the interlocutor). The school's two named masters embody its strategy: **Su Qin** 蘇秦 (the *zong* 縱 "vertical" alliance — uniting weaker states against the strongest, Qin) and **Zhang Yi** 張儀 (the *heng* 橫 "horizontal" — peeling states off to side with the strong). Persuasion here *is* grand strategy: alliances made and broken by speech.

### 4.2 Han Feizi, "The Difficulties of Persuasion" (*Shuinan* 說難)

The **_Han Feizi_** 韓非子 (Legalist, 3rd c. BCE) chapter **"Shuinan"** 說難 is the tradition's sharpest single essay on counsel. Its thesis: the difficulty of persuasion is **not** knowing the truth or arguing well — it is *reading the listener's concealed heart* and not triggering his fear or pride. The persuader must know which arguments flatter the ruler's self-image and which expose him; the same true advice can win favour or get you executed depending on timing and the ruler's hidden agenda. (Sima Qian read it as righteous-persuader counsel; later commentators as a *critique* of the amoral persuasion-arts.)

### 4.3 Persuasion anthologies

- **_Zhanguo ce_** 戰國策 ("Strategies/Intrigues of the Warring States") — a compilation of the set-piece persuasion **speeches** of the roving diplomats; the applied corpus behind the *zonghengjia*.
- **_Huainanzi_** 淮南子, chapters "Shuilin" 說林 and "Shuishan" 說山 ("Forest" and "Mountain of Persuasions") — handbooks of stock arguments for advisers who knew they'd be called to speak, letting a ruler sort genuinely new ideas from rehearsed talking points.

### 4.4 The literary wing (brief)

**Liu Xie** 劉勰, **_Wenxin Diaolong_** 文心雕龍 ("The Literary Mind and the Carving of Dragons", c. 501–502 CE) — the great systematic work of Chinese literary theory, including genre analysis of memorials, edicts, and persuasions. More belletristic than the persuasion-school texts but the closest Chinese analogue to a comprehensive *treatise* on composition.

### 4.5 Throughline

The Chinese axis = **persuasion as reading-and-steering a single powerful listener**, where success is invisible (the target thinks the idea was his) and the stakes are personal survival. This is the **Outreach / Read / private-audience** half of Valoria, and it is *exactly the half the Greek tradition under-theorises.* It validates a design that distinguishes **dyadic persuasion of an NPC** (read the *qing*, steer covertly) from **public contest before an audience** (Greek/assembly) — see §9.4. It also independently supports CR5's "indirect → attack opponent Face" via *bai-he* and the concealed-heart model.

---

## 5. THE INDIAN TRADITION — the formal theory of debate and its self-gating

Sanskrit gives the most **rule-formalised** debate system of any pre-modern tradition, and it is the explicit anchor of the redesign's CR5. It is also the only tradition that builds the **audience and the opponent's relative standing directly into the rules** for which kind of argument is licit — i.e., self-gating.

### 5.1 The Nyāya-sūtra — *kathā* and its three modes

The **_Nyāya-sūtra_** of Gautama (Akṣapāda; c. 2nd c. CE) founds the *Nyāya* school of logic and lists **sixteen categories (*padārtha*)** whose mastery yields liberation. Several are a complete debate-theory:
- **Debate (*kathā*) splits three ways:** **vāda** (honest discussion aimed at **truth**, between parties of comparable standing, bound to use valid means of knowledge — *pramāṇa* — and *tarka*, non-contradiction with accepted doctrine — *siddhānta* — and the full five-membered syllogism); **jalpa** (wrangling aimed at **victory**, where any winning device is permitted); **vitaṇḍā** (cavilling — pure **refutation with no counter-thesis of one's own**).
- **The defeat machinery:** **nigrahasthāna** (clinching "points of defeat" — the formal ways you lose), **chala** (quibbles — exploiting ambiguity), **jāti** (futile/sophistical rejoinders), **hetvābhāsa** (fallacious reasons / pseudo-probans). A debate is structured as **pakṣa** (thesis) vs **pratipakṣa** (counter-thesis), and victory is awarded against the side that incurs a *nigrahasthāna*.

The later commentators — **Vātsyāyana** (*Nyāya-bhāṣya*), **Uddyotakara** (*Nyāya-vārttika*), **Vācaspatimiśra** — refine when each mode is appropriate.

### 5.2 The Caraka-saṃhitā — the earliest debate manual, and an audience model

The medical compendium **_Caraka-saṃhitā_** (Vimānasthāna 8) contains the oldest systematic debate manual in India and the part most relevant to Valoria. Before agreeing to debate, the practitioner is told to assess:
- the **type of debate** — *anuloma/sandhāya sambhāṣā* (friendly) vs *vigṛhya sambhāṣā* (hostile);
- the **opponent's relative standing** — superior / equal / inferior;
- the **assembly (*pariṣad*)** — learned vs ignorant; and each of these as friendly / indifferent / hostile.

Strategy is then **conditioned on that triage**: against a weaker opponent before a hostile, ignorant crowd you may legitimately use *jalpa* devices; against an equal before a learned assembly you owe honest *vāda*.

### 5.3 The ethics of when to debate (Vācaspati)

**Vācaspatimiśra** adds the moral dimension the redesign cites: *jalpa* — stooping to fallacy to "refute" a powerful person spouting dangerous falsehoods before a dependent crowd — is licensed only under specific conditions; the ethical stakes and the interlocutor's moral quality bound what is permissible. **Obstruction is bounded by your own standing and the situation.**

### 5.4 Kauṭilya's *Arthaśāstra* — the negotiation half

For **negotiation/diplomacy**, the **_Arthaśāstra_** of Kauṭilya (Mauryan; compiled by the early centuries CE) is the Sanskrit monument:
- **Envoys (*dūta*)** are typed by latitude: *nisṛṣṭārtha* (plenipotentiary), *parimitārtha* (limited brief), *śāsanahara* (mere message-bearer).
- **The four expedients (*upāya*):** *sāma* (conciliation), *dāna* (gifts/concession), *bheda* (sowing dissension), *daṇḍa* (force) — escalating instruments of statecraft.
- **The six measures of foreign policy (*ṣāḍguṇya*):** *sandhi* (peace/treaty), *vigraha* (hostility), *āsana* (neutrality), *yāna* (preparing to strike), *saṃśraya* (seeking shelter/alliance), *dvaidhībhāva* (double policy) — set within *maṇḍala* ("circle of states") theory: your neighbour is your enemy, your neighbour's neighbour your friend.

### 5.5 Throughline

The Indian axis gives Valoria three things no other tradition supplies as cleanly: (1) a **formal thesis/counter-thesis (pakṣa/pratipakṣa) structure with explicit defeat conditions (nigrahasthāna)** — a clock-and-loss machine; (2) **self-gating** — what argument is *licit* depends on your standing and the assembly's composition, the exact mechanism CR5 invokes; (3) a **structured negotiation grammar** (dūta types, the four *upāya*, the six *ṣāḍguṇya*) for any treaty/alliance system. This is the most directly mineable tradition in the corpus.

---

## 6. MEDIEVAL EUROPEAN *ARTES* — formulae as generative templates

The medieval West fragmented classical rhetoric into three practical arts (the *artes*), each a how-to with **fill-in-the-slots structure**. For a videogame this is the most *implementable* layer: these are already templates.

### 6.1 *Ars dictaminis* — the art of the letter (→ royal appeals)

The medieval art of composing letters and official documents, and the direct Latin analogue of the Arabic chancery (§3.3). Antecedents: C. Julius Victor's *Ars rhetorica*, Cassiodorus' *Variae epistolae*, the Greek epistolary type-lists (ps.-Demetrius' *Typoi epistolikoi*, ps.-Libanius). The medieval discipline begins with **Alberic of Monte Cassino** (d. 1088), whose *Dictaminum radii / Breviarium de dictamine* and *Flores rhetorici* (c. 1080s) are the earliest treatises; his pupil John of Gaeta carried the art into the Papal Chancery. It was then systematised by the **Bolognese school**: Adalbertus Samaritanus (*Praecepta dictaminum*, c. 1115), Hugh of Bologna, **Boncompagno da Signa** (*Rhetorica antiqua / Boncompagnus*, 1215; *Palma*), **Guido Faba** (*Summa dictaminis*, *Dictamina rhetorica*), and **Pier della Vigna** at the chancery of Frederick II.

The codified **five-part letter**:
1. **salutatio** — the greeting, *rank-indexed* (the form depends on the relative status of sender and addressee — a self-gating-by-standing rule baked into the very first line);
2. **exordium / *captatio benevolentiae*** — "the securing of goodwill," the move that disposes the recipient favourably (this *is* ethos/pathos, weaponised as a fixed slot);
3. **narratio** — the statement of facts;
4. **petitio** — **the request** (the operative ask);
5. **conclusio** — the close.

Plus the **cursus** (rhythmic prose cadences) for high style. The genre's logical endpoint is **Lawrence of Aquilegia's _Practica sive usus dictaminis_**, which literally **converts the model letter into a series of connected slots, each filled from a table of options** — a medieval procedural-generation engine for correspondence.

> **Why it matters:** the *salutatio → captatio → narratio → petitio → conclusio* arc is a ready-made **structure for a "submit an appeal/petition" interaction**, and Lawrence of Aquilegia's slot table is a literal blueprint for generating such appeals from a few player choices (addressee rank → permissible salutation; chosen ethos-move → captatio variant; grievance type → narratio; ask → petitio). See §9.5.

### 6.2 *Ars arengandi* — the art of the public speech (→ assemblies / parliament)

`[CONFIDENCE: medium — less web-verified this session]` The art of the **formal public address (*arenga / arringa*)**, developed for the **communal assemblies** of the Italian city-states — the closest medieval analogue to live deliberative oratory. The standard reference figures are **Matteo dei Libri** (Bologna, 13th c.; vernacular *Arringhe* — model speeches for civic occasions: taking office, welcoming dignitaries, swearing peace, pleading a cause) and **Jacques de Dinant**. These manuals supply *occasion-typed* speech templates — the public-speaking counterpart to the letter-templates of §6.1.

### 6.3 *Ars praedicandi* — the art of preaching (→ mass persuasion / the Church)

The art of the **thematic ("university") sermon**, e.g. **Robert of Basevorn's _Forma praedicandi_** (1322). Structure: a scriptural **theme**, its **division** into parts, and the systematic **amplification (dilatatio)** of each. This is mass persuasion under institutional authority — directly relevant to the **Church** as a persuasive actor (Mass Seizure, the pulpit as an instrument), and a contrast to secular contest (the preacher's authority is *borrowed from the source*, not contested).

### 6.4 The vernacular reception of Cicero

**Brunetto Latini** (Dante's teacher), *La Rettorica* (an Italian commentary on Cicero's *De Inventione*) and the encyclopaedic *Li Livres dou Trésor* (in French), carried classical rhetoric — stasis, the genres, the canons — into the lay, civic, vernacular world of the late-medieval commune. The bridge by which the Greco-Roman source code reached the political class that actually governed city-states.

### 6.5 Throughline

The medieval West's contribution is **rhetoric-as-template**: the classical art compressed into rank-indexed, occasion-typed, slot-fillable forms (*ars dictaminis* for appeals, *ars arengandi* for assembly speech, *ars praedicandi* for the pulpit). Two mechanically golden features fall out: (1) **standing is encoded in the form itself** (the *salutatio* you may use is a function of relative rank), and (2) the **petitio/captatio structure** is a turnkey appeal generator. This is the layer to mine for UI-facing structure.

---

## 7. ASSEMBLIES, PARLIAMENTS & TRIALS — the venues that resolve

Treatises describe the *art*; institutions supply the *engine*. For a no-GM videogame where "the engine resolves," the institutional rules are as load-bearing as the rhetoric. Two families: deliberative bodies (→ Parliamentary Vote/Stay) and forensic venues (→ Tribunal, investigation).

### 7.1 Deliberative bodies

- **The Roman Senate.** Procedure by **relatio** (the presiding magistrate frames the question), **sententiae** (opinions delivered in strict order of rank — *princeps senatus* first; the lower ranks often never reached), and decision by **discessio** (physical division — walking to one side). Persuasion was bounded by a rigid speaking-order that *was itself a function of standing*.
- **The Anglo-Saxon witenagemot** — the council of "wise men" advising the king; consultative, consensus-seeking, ancestor of the king-in-council.
- **The Norse *þing* / Icelandic *Alþingi*** (est. 930 at *Þingvellir*). The presiding **Lawspeaker (*lögsögumaðr*)** recited the law from memory at the **Lögberg** ("Law Rock") and chaired the **lögrétta** (law council); assent could be expressed by *vápnatak* (the clashing of weapons). A *memory-anchored, orally-recited* legal order with a single authoritative voice — directly resonant with the setting's Norse register (and a clean model if the Parliament wants a "Lawspeaker/Speaker" role-actor).
- **The *Modus Tenendi Parliamentum*** (England, c. 1294–1327; `[CONFIDENCE: medium]` on date/purpose) — 26 chapters describing an *idealised* parliamentary procedure: the orders summoned, precedence, and (ch. 17, *De casibus et iudiciis difficilibus*) how to handle hard cases. Scholarship reads it as projecting Parliament as **neutral ground for accord between warring factions** — i.e., the assembly as a *contested arena that itself constrains the contest.*
- **Sir Thomas Smith, _De Republica Anglorum_** (1562–65, written while ambassador to France) — the Elizabethan description of English institutions, courts, and parliamentary procedure for foreign readers; an early systematic account of how the deliberative machine actually worked.

### 7.2 Forensic venues

- **Athenian *dikasteria*.** Mass citizen juries (hundreds of jurors), speeches timed by the **water-clock (*klepsydra*)**, no professional judges or lawyers — hence the logographers (§1.5). Persuasion under a hard **clock** before a **large, swayable lay audience**.
- **Roman *quaestiones perpetuae*.** Standing jury-courts; the arena of Cicero's forensic corpus; the applied home of stasis.
- **The romano-canonical *ordo iudiciarius*.** The medieval procedural synthesis of Roman and canon law (e.g., **Tancred's _Ordo iudiciarius_**, c. 1216): the **libellus** (written complaint), *litis contestatio* (joinder of issue), a graded **hierarchy of proof** (the notorious "two witnesses = full proof," confession as "queen of proofs"), and the *positiones/articuli* (formal assertions to be proved). A *rule-bound evidentiary contest* — the structural ancestor of an Evidence-clock system.
- **The *inquisitio* / heresy process.** The inquisitorial procedure (e.g. **Bernard Gui's _Practica inquisitionis heretice pravitatis_**, 1323–24) — investigation, interrogation, the manual of categories and questions. Directly relevant to the **Excommunication Tribunal** and the heresy-investigation lifecycle already in the repo (`f3_heresy_investigation_lifecycle`).

### 7.3 Throughline

The venue is the engine. Each institution supplies (a) a **framing authority** (who poses the question — relatio, the Lawspeaker, the presiding magistrate), (b) a **standing-indexed speaking order** (rank gates *when and whether* you speak), (c) a **decision rule** (discessio, vote, weighted proof, jury verdict), and (d) often a **clock** (the klepsydra; staged procedure). This is precisely the "wrapper = praetor/magister; deterministic accounting around a small stochastic surface" shape of CR1 — the institution is the deterministic wrapper, the speeches the stochastic core.

---

## 8. ROYAL APPEALS, PETITIONS & NEGOTIATION

### 8.1 Petition & supplication — the appeal to the sovereign

The best-documented historical "appeal to the Crown" system is the English **petition** corpus. The National Archives' **"Ancient Petitions" (class SC 8)** — over **17,000** documents, concentrated c. 1270s–1450s — are appeals to the crown for **redress**, split into **complaints** (injustices not resolvable at common law) and **requests** (for royal favour: a grant, an office, a pardon). Key structural findings (session-verified):
- **Common vs private petition:** matters of general/communal grievance vs individual asks — a distinction that maps onto faction-level vs character-level appeals.
- **The shift to "high style"** (c. 1350–1405): as Parliament became a *stately* occasion where the king met "the community of the realm," petitions moved from blunt legal instruments to **expressions of loyalty and deference** — supplicants no longer "complained" but "**showed**" (*moustre*) their grievance and "**prayed**" (*prie*) for remedy. Form tracked the ceremonialisation of power.
- **"Government by grace" (*gouvernement par la grâce*):** the petition was a primary channel mediating subject↔sovereign across Latin Christendom (Millet, *Suppliques et Requêtes*; Koziol on the rites of supplication). It had **performative/intercessory** qualities — *who carried the petition* (proctors, intercessors, well-placed patrons) shaped its success.
- **The French *requête / supplication*:** the humble register ("*supplient et remontrent très humblement*") and the closing **prayer-formula** (the petitioner promises to "pray God for the continuation of Your Majesty's prosperity and health"). A fixed deference-frame around the ask.
- **The secular/ecclesiastical split:** royal petitions and **papal/canon-law petitions** ran in parallel systems — directly relevant to a world with both a **Crown** and a **Church** as petitionable authorities.

### 8.2 Remontrance & *appel comme d'abus* — deference-wrapped critique

The **Parlement of Paris** developed the **_remontrance_**: a formal protest to the King, technically an **"appeal against abuse" (*appel comme d'abus*)**, in which the magistrates *insist the King fulfil his duty* — criticism delivered inside an envelope of deference (Flammermont, *Remonstrances du Parlement de Paris au XVIIIe siècle*). The remontrance is a distinctive move-type: **opposition that affirms the legitimacy of the authority it opposes** — a way to push back on power without rebelling against it.

### 8.3 Negotiation & the ambassador literature (→ treaties/alliances)

- **The Amarna letters** (14th c. BCE, Akkadian as diplomatic *lingua franca*) — the earliest corpus of inter-state diplomatic correspondence; the grammar of "brotherhood," gift-exchange, and grievance between Great Kings.
- **Kauṭilya's _Arthaśāstra_** — the Sanskrit negotiation grammar (envoy types, the four *upāya*, the six *ṣāḍguṇya*; §5.4).
- **Bernard du Rosier**, *Ambaxiatorum brevilogus* (1435–36) — `[CONFIDENCE: medium]` often called "the first Western manual of diplomatic practice" (Mattingly; contested by Lucas de Penna's *De legationibus* commentary and Martino Garati da Lodi). Divides missions into **ceremonial vs negotiation**, and **short-term vs long circular legations**; lists the diplomat's tasks (honour the Church/Crown, protect the realm's rights, conclude peace, remove future grievances, reduce rebels to obedience).
- **Ermolao Barbaro**, *De officio legati* (c. 1490) — the humanist statement of the envoy's office (and, less guardedly than du Rosier, of political utility).
- **Alberico Gentili**, *De Legationibus libri tres* (1585) — the juristic treatment of ambassadorial **status and immunity** (a founding text of the law of nations).
- **Abraham de Wicquefort**, *L'Ambassadeur et ses fonctions* (1681).
- **François de Callières**, *De la manière de négocier avec les souverains* (1716) — long regarded as the finest manual of negotiating method: the resident-ambassador system, negotiation as patient relationship-building and reputation, "the secret of negotiation is to harmonise the interests of the parties."

### 8.4 Throughline

Two move-classes the contest engine doesn't yet name: (1) **the asymmetric appeal** — a petition *up* a power gradient, where the form is rank-indexed, the register is deference, success depends partly on an **intercessor**, and the secular/ecclesiastical addressee split mirrors Valoria's Crown/Church; and (2) **negotiation as a bounded, reputation-laden exchange** — typed envoys with typed latitude, escalating instruments (conciliation→concession→dissension→force), structured into a small set of policy stances. Both are *contests with a different topology* than the symmetric debate the social system models.

---

## 9. THROUGHLINES → VALORIA (synthesis; proposals are Jordan-vetoable)

`[SELF-AUTHORED — bias risk]` This section assesses systems the project (and prior Claude sessions) authored. An independent reviewer would warn that confirming "the design's classical citations are well-founded" is exactly the conclusion a session is biased to reach. Treated accordingly: validations below are stated as *the historical record supports X*, and every proposed addition is flagged as needing Jordan's design call, not asserted as canon. Valoria claims here are scoped to what was read this session (`social_contest_v30_index`, `RATIFIED_2026-06-01`, `precedents_analysis`, the political-dynamics precedents doc) — **not** to canonical internals I did not open.

### 9.1 Cross-tradition invariants (what recurs everywhere)

| Invariant | Where it appears | Valoria touchpoint |
|---|---|---|
| **The audience/judge is the real target** (not the opponent) | Aristotle's three genres; Athenian juries; Caraka's *pariṣad*; the "stately" English Parliament | Audience boost; the adjudicator; "format follows context" |
| **Diagnose the issue before arguing** (stasis) | Hermagoras→Hermogenes; Cicero; Quintilian; (echoed in *maʿānī* "requirement of the situation") | **CR4 stasis × genre** — confirmed well-founded |
| **Character/standing is a usable resource** (ethos) | Aristotle; Lysias' *ethopoeia*; the rank-indexed *salutatio*; Roman *sententiae* order | **CR3/CR5 "Face"** — confirmed cross-traditionally robust |
| **Licit tactics are bounded by your own standing/situation** (self-gating) | Nyāya *jalpa/vitaṇḍā* + Caraka triage + Vācaspati ethics; Quintilian's *vir bonus* | **CR5 self-gating** — confirmed; Nyāya is the precise anchor |
| **Thesis vs counter-thesis with formal defeat conditions** | Nyāya *pakṣa/pratipakṣa* + *nigrahasthāna* | The exchange structure + Persuasion/merits clock |
| **Form is rank-indexed** (the structure encodes who you are to whom) | *ars dictaminis salutatio*; *Ṣubḥ al-aʿshā* titulature; senate order | Asymmetric Proceedings (§7); a petition system (proposed §9.5) |
| **Persuasion-of-one ≠ persuasion-of-many** | Guiguzi/Han Feizi (dyadic) vs Greek (public) | Outreach/Read (dyadic) vs Contest (public) — see §9.4 |

### 9.2 Parliamentary Vote / Stay (deliberative)

The repo's Parliamentary layer (`social_contest_v30` §10/§10.1; `parliamentary_transfer_v30`; the `parliamentary_vote/stay/transfer` sims) has a **candidate** argument-type vocabulary it could draw on: the later-tradition **deliberative final headings** (τελικὰ κεφάλαια) — a practical-headings set resembling *legality / justice / advantage / feasibility / honour / outcome* (§1.4). `[CONFIDENCE: low — this list's exact membership and attribution were NOT verified this session (§0.4); confirm a source before adopting it.]` What *is* securely verified for the deliberative genre is narrower: Aristotle's paired deliberative topics, **the good and the advantageous**, which alone already split motions into legible argument types (is it *right*? is it *advantageous*?). The **Roman *relatio* + ranked *sententiae*** model and the **Norse Lawspeaker** (§7.1) are two concrete framing-authority designs for *who poses the question and in what order members may speak* — a standing-gated turn order that is historically the heart of assembly procedure. `[Proposed — Jordan call: adopt a deliberative argument-type axis? The Aristotelian good/advantage pair is the verified minimum; the six-head τελικὰ-κεφάλαια list needs source-verification first.]`

### 9.3 Excommunication Tribunal & investigation/Evidence (forensic)

The Tribunal (§7.1) and the heresy-investigation lifecycle are forensic. The **romano-canonical *ordo iudiciarius*** (§7.2) supplies a historically exact structure — *libellus* (charge) → *litis contestatio* (issue joined) → graded proof hierarchy → verdict — and **Bernard Gui's inquisitorial manual** supplies the interrogation/category structure. The classical stasis ladder *is* the forensic defence tree: deny the fact (conjectural) → contest the label (definitional) → justify/mitigate (qualitative) → challenge the venue (translative = the **Stay**). The investigation Evidence-clock (3/5/8) is well-modelled by the *positiones/articuli* + proof-accumulation pattern. `[This validates the existing forensic design; surfaces the proof-hierarchy as a possible Evidence-weighting refinement — Jordan call.]`

### 9.4 The dyadic/public axis (a genuine gap surfaced)

The strongest *new* finding: the corpus splits persuasion into **dyadic** (Chinese: read and steer one ruler; success invisible) vs **public** (Greek/assembly: sway a judging crowd). Valoria already has both halves — **Outreach/Read** (dyadic) and **Contest/Vote** (public) — but they are not yet theorised as *different games with different win conditions* (covert influence vs. visible victory before an audience). `[Open question — Jordan: should dyadic NPC persuasion and public contest be mechanically distinct sub-systems rather than one engine with an "audience" parameter? The historical record says they are different arts.]`

### 9.5 Royal appeals — likely a missing subsystem (proposed, not canon)

**No petition / appeal-to-sovereign subsystem exists in the repository** — and this negative is now *tested*, not assumed. A recursive scan of all **1,605 repo files** (filename axis), the **declared canonical sources** in `canonical_sources.yaml`, and the **content of the two most likely host documents** (`social_contest_v30_index`, `parliamentary_transfer_v30`) returned **zero** matches for *petition / appeal / grievance / supplication / remonstrance / redress / requête / intercession / clemency* — the only raw hits were false positives from `writ` ⊂ `writer` / `rewrite`. `[CONFIDENCE: high that no such *named* subsystem exists; residual: a petition mechanic embedded inside some third document under entirely different vocabulary cannot be fully excluded, but the design-doc naming convention and the canonical-source list argue against it.]` Yet it is the single best-documented historical mechanism (§3.3 chancery; §6.1 *ars dictaminis*; §8.1 the SC 8 petitions). The historical form is turnkey for a videogame: a **rank-indexed, slot-fillable appeal** (Lawrence of Aquilegia's literal option-tables), with **Crown vs Church** addressees (the secular/ecclesiastical split), a **deference register** (*captatio benevolentiae* / *duʿāʾ* / the French prayer-close), an **intercessor** whose standing modifies success (mapping cleanly onto the existing **NPC Regard / Reconcile mediation** mechanic in the political-dynamics doc), and the **remontrance** as a distinctive "deference-wrapped critique" move. `[Proposed new subsystem — explicitly Jordan's call to accept, defer, or reject. Built bottom-up from the chancery/dictaminis/petition sources; not invented, but also not authorised. Does not touch metaphysics/world/characters.]` **Primary-language refinement (§12.3):** French scholarship splits this into *two* instruments — the *supplique* (subject→sovereign, seeks *grâce*) and the *remontrance* (institution→Crown, a legitimated check) — with a concrete *jussion → remontrances itératives → lit de justice* escalation ladder; the stronger design builds it as two mechanics, not one.

### 9.6 Negotiation / treaties

For any alliance/treaty system (cf. `sim_negotiations_alliances_treaties`, `sim_diplomacy_*`): **Kauṭilya's grammar** (envoy latitude types; the four *upāya*; the six *ṣāḍguṇya* with *maṇḍala* "neighbour = enemy" geometry) and **Callières' relationship/reputation model** are the two anchors. Negotiation is a *bounded reputation-laden exchange*, topologically distinct from debate. `[Anchor set for future treaty design; no claim about current canon.]`

### 9.7 What the corpus does *not* license

It does not justify changing the metaphysics, the world, the characters, or the tone/vibe (project-owner contract, creative tier). It does not retcon any authored value. Where it suggests the redesign's coefficients (lever magnitudes, Face/Concentration tuning — CR6) those remain sim-validation questions, not historical ones; history validates the *structure* (stasis/ethos/self-gating), never the *numbers*.

---

## 10. SOURCE REGISTER

Two registers, kept honestly distinct. **§10.A** lists what was *actually consulted* in building this corpus — read directly, or read in substantive extract / translation / abstract / review. These carry the claims. **§10.B** is a **field bibliography**: the primary texts and scholarship the corpus is *oriented by* and names, but which were **not all opened directly** — further-reading, not evidence consulted. (§11 maps specific searches to specific claims; §11.5 gives per-strand source tiers.)

### 10.A Consulted this session (directly read, or read in substantive extract)

- **Read in full / at length (open-access):** M. Heath, "The Substructure of stasis-theory from Hermagoras to Hermogenes," *CQ* 44 (1994), White Rose PDF `[PR]`.
- **Primary text read as extract (translation):** Menander Rhetor, *Treatise* 2.1 (Loeb) — the *basilikos logos* passage `[PRIM]`; al-Jurjānī, *Dalāʾil al-iʿjāz* p.78 (Abu Deeb's translation, quoted in an open-access article) `[PRIM]`; *Nyāya-sūtra* 1.1.1 / 1.2.1–2 (via citation of the sūtras) `[PRIM]`; *Grágás* (Old Norse, via wikisource) `[PRIM]`.
- **Scholarship read as abstract / extract / review (search-surfaced):** SEP "Aristotle's Rhetoric" `[REF]`; Omissi & Ross, *Imperial Panegyric from Diocletian to Honorius* (2020), open-access intro `[PR]`; Nuti, *GRBS* 56 (2016) `[PR]`; Larkin, *The Theology of Meaning* (1995), JAOS review `[PR]`; Abu Deeb, *Al-Jurjānī's Theory of Poetic Imagery* (1979), via quotation `[PR]`; Tsung (UC eScholarship, adv. Larkin), open-access dissertation abstract `[PR]`; Matilal, *The Character of Logic in India* (1998), via quotation `[PR]`; Vidyabhūṣaṇa, *A History of Indian Logic* (1921), via citation `[PR]`; Russell & Wilson, *Menander Rhetor* (Oxford 1981), via scholarly citation `[PR]`; Kazhdan & Jeffreys, *ODB* `[REF]`. Plus the §11.3–11.4 primary-language sources (Conseil constitutionnel *Cahiers*; PUR/OpenEdition; rheton/Schirren *HSK*; Stroh; ASJP; Tsinghua; *Carte Romanze* / Artifoni; etc.) at snippet/abstract depth — tiers in §11.5.

### 10.B Field bibliography (orientation; not all consulted directly)

**Greco-Roman.** Aristotle, *Rhetoric*; Plato, *Gorgias*, *Phaedrus*; Isocrates, *Against the Sophists*, *Antidosis*; *Rhetorica ad Herennium* (anon., c. 80s BCE); Cicero, *De Inventione*, *De Oratore*, *Orator*, *Topica*, *Partitiones Oratoriae*; Quintilian, *Institutio Oratoria*; Hermagoras of Temnos (frr., ed. Matthes); Lysias, Demosthenes (Attic orators). Stasis scholarship: M. Heath, *Hermogenes On Issues* (1995) [his CQ 1994 article is in §10.A]; R. Nadeau (GRBS 1959); A. Braet (1987).

**Byzantine.** Aphthonius, Theon, (ps.-)Hermogenes, Nicolaus — *Progymnasmata* (tr. G. Kennedy); Menander Rhetor (*basilikos logos*); Constantine VII, *De Ceremoniis*, *De Administrando Imperio*.

**Arabic.** al-Jurjānī, *Dalāʾil al-iʿjāz*, *Asrār al-balāgha*; al-Rāzī, *Nihāyat al-iʿjāz*; al-Sakkākī, *Miftāḥ al-ʿulūm*; al-Qazwīnī, *Talkhīṣ al-Miftāḥ*, *al-Īḍāḥ*; al-Jāḥiẓ, *al-Bayān wa-l-tabyīn*; Qudāma ibn Jaʿfar, *Naqd al-shiʿr*; Ibn al-Muqaffaʿ, *Kalīla wa-Dimna*; ʿAbd al-Ḥamīd al-Kātib, *Risāla ilā l-kuttāb*; al-Ṣūlī, *Adab al-Kuttāb*; Ibn Mammātī, *Qawānīn al-dawāwīn*; al-Qalqashandī, *Ṣubḥ al-aʿshā fī ṣināʿat al-inshāʾ* (1412).

**Chinese.** *Guiguzi* 鬼谷子; *Han Feizi* 韓非子 ("Shuinan" 說難); *Zhanguo ce* 戰國策; *Huainanzi* 淮南子 ("Shuilin"/"Shuishan"); Liu Xie, *Wenxin Diaolong* 文心雕龍. (Su Qin 蘇秦, Zhang Yi 張儀 — *zonghengjia* 縱橫家.)

**Sanskrit.** Gautama/Akṣapāda, *Nyāya-sūtra*; Vātsyāyana, *Nyāya-bhāṣya*; Uddyotakara, *Nyāya-vārttika*; Vācaspatimiśra; *Caraka-saṃhitā* (Vimānasthāna 8); Kauṭilya, *Arthaśāstra*.

**Medieval Latin / vernacular.** Alberic of Monte Cassino, *Breviarium de dictamine*, *Flores rhetorici*; Adalbertus Samaritanus, *Praecepta dictaminum*; Boncompagno da Signa, *Rhetorica antiqua*; Guido Faba, *Summa dictaminis*; Pier della Vigna; Lawrence of Aquilegia, *Practica sive usus dictaminis*; Matteo dei Libri, *Arringhe*; Robert of Basevorn, *Forma praedicandi*; Brunetto Latini, *La Rettorica*, *Li Livres dou Trésor*; Tancred, *Ordo iudiciarius*; Bernard Gui, *Practica inquisitionis*. Scholarship: M. Camargo, *Ars dictaminis, ars dictandi*; J. J. Murphy, *Rhetoric in the Middle Ages*.

**Assemblies / petitions / diplomacy.** *Modus Tenendi Parliamentum* (ed. Hardy 1846); Thomas Smith, *De Republica Anglorum* (1562–65); the Icelandic *Grágás* / *Alþingi* tradition; The National Archives, "Ancient Petitions" SC 8; G. Dodd & W. M. Ormrod (eds.), *Medieval Petitions: Grace and Grievance*; H. Millet (ed.), *Suppliques et Requêtes*; J. Flammermont, *Remonstrances du Parlement de Paris au XVIIIe siècle*; the Amarna letters; Bernard du Rosier, *Ambaxiatorum brevilogus* (1436); Ermolao Barbaro, *De officio legati*; A. Gentili, *De Legationibus* (1585); A. de Wicquefort, *L'Ambassadeur* (1681); F. de Callières, *De la manière de négocier avec les souverains* (1716); G. Mattingly, *Renaissance Diplomacy*.

---

## 11. SESSION VERIFICATION REGISTER (search → claim → source)

Maps the web searches behind this corpus to the claims they ground, so each assertion's evidence is checkable rather than asserted. Domain-level source lists (representative, not exhaustive).

### 11.1 This session (2026-06-02) — Greco-Roman §1 verification + the §9.2 correction

| Search | Grounds | Key sources |
|---|---|---|
| *Hermagoras stasis · four staseis · conjectural/definitional/qualitative/translative* | §1.4 four classical stases; **translative = jurisdiction/legal process**; Cicero's *constitutio* (*De Inventione*) | en.wikipedia.org/wiki/Hermagoras_of_Temnos · cambridge.org (CQ, "Substructure of stasis-theory") · files.eric.ed.gov/ED358445 · parlormultimedia.com (*The Writing Instructor*) |
| *five canons · inventio dispositio elocutio memoria pronuntiatio* | §1.3 five canons; Cicero *De Inventione / De Oratore / Orator*; Quintilian expanded them | en.wikipedia.org/wiki/Orator_(Cicero), /Inventio, /Dispositio, /Elocutio, /Pronuntiatio · artofmanliness.com |
| *Aristotle Rhetoric three genres · ethos pathos logos* | §1.1 three genres (deliberative=future/advantageous · forensic=past/just · epideictic=present/honourable); three *pisteis* | plato.stanford.edu/entries/aristotle-rhetoric (SEP) · en.wikipedia.org/wiki/Deliberative_rhetoric · wilson.fas.harvard.edu |
| *deliberative final headings · telika kephalaia* | **§9.2 CORRECTION** — the clean six-item list did **not** verify; Aristotle's deliberative topics = **good + advantageous** (pairs); **honourable = epideictic** axis | plato.stanford.edu/entries/aristotle-rhetoric · rhetoric.byu.edu (Silva Rhetoricae; cites *Arist. Rhet.* 1.4–8, *Cic. De Inv.* 2.52–58) · en.wikipedia.org/wiki/Deliberative_rhetoric |
| *ten Attic orators · Lysias logographer · Demosthenes/Cicero Philippics* | §1.5 the ten-orator canon (names stable; formation debated); Lysias as master logographer; Demosthenes *Philippicae* → Cicero's | en.wikipedia.org/wiki/Attic_orators, /Lysias · brill.com (canonisation) · academia.edu ("Remark on the Canon of the Attic Orators") |

Repo re-confirmation this session (canon, not web): `[READ: designs/scene/social_contest_v30_index.md]` → `§7.1 Excommunication Tribunal (ED-625 — approved 2026-04-17)`, `§10.1 Parliamentary Stay (ED-631)`, `§10 Board Game Parliamentary Vote`; `[READ: designs/audit/2026-06-01-contest-redesign/RATIFIED_2026-06-01.md]` → `CR4 | Ciceronian stasis x genre … conjectural/definitional/qualitative/translative = terrain`, `CR5 … self-gating`; `[READ: canonical_sources.yaml + recursive tree of 1,605 files]` → petition/appeal/grievance subsystem absent on all three axes (§9.5).

### 11.2 Prior session (pre-compaction) — non-Western, medieval, assembly, petition, diplomacy

| Search | Grounds | Key sources |
|---|---|---|
| *Arabic balāgha · al-Jāḥiẓ/Jurjānī/Sakkākī/Qazwīnī · Miftāḥ/Talkhīṣ* | §3.1 *balāgha* lineage and the *maʿānī/bayān/badīʿ* tripartition | en.wikipedia.org/wiki/Miftah_al-Ulum, /Talkhis_al-Miftah, /Jalal_al-Din_al-Qazwini · academia.edu ("Canonical Formulation of ʿIlm al-Balāghah"; "Legacy of al-Jurjānī") · suheillaher.wordpress.com |
| *Islamic chancery inshāʾ · adab al-kātib · ʿAbd al-Ḥamīd · Qalqashandī Ṣubḥ al-aʿshā* | §3.3 chancery/*inshāʾ* as the royal-appeals analogue; *Ṣubḥ al-aʿshā* (1412) | iranicaonline.org (ʿAbd al-Ḥamīd b. Yaḥyā) · eprints.soas.ac.uk/29385 · researchgate.net & academia.edu (Selections from *Ṣubḥ al-Aʿshā*) · lancaster.ac.uk/jais (Umayyad epistolography) |
| *Guiguzi 鬼谷子 · zonghengjia · Han Feizi "Shui Nan"* | §4.1–4.2 dyadic ruler-persuasion; *bai-he*; the Difficulties of Persuasion | researchgate.net ("Rhetoric as the Art of Listening … Guiguzi"; "The Difficulty with the Difficulties of Persuasion") · link.springer.com · chinnect.org · gutenberg.org/ebooks/7209 |
| *Nyāya-sūtra · vāda/jalpa/vitaṇḍā · tarka · Caraka-saṃhitā* | §5.1–5.3 the three debate modes, *nigrahasthāna*, audience-triage, ethics of when to debate | psyche.co (Nyāya — which debates are worth having) · sreenivasaraos.com (saṃvāda/vāda/jalpa/vitaṇḍā) · wisdomlib.org (Caraka-saṃhitā) · indiafacts.org |
| *Hermagoras/Hermogenes On Issues · Cicero De Inventione* (prior pass at §1.4) | §1.4 stasis lineage Hermagoras→Hermogenes (re-verified independently this session, 11.1) | cambridge.org (CQ, "Substructure of stasis-theory") · eprints.whiterose.ac.uk (M. Heath) · en.wikipedia.org/wiki/Hermogenes_of_Tarsus · bmcr.brynmawr.edu |
| *ars dictaminis · Alberic of Monte Cassino · ars arengandi · Guido Faba* | §6.1–6.2 the five-part letter, *captatio benevolentiae*, slot-fill templates | en.wikipedia.org/wiki/Ars_dictaminis, /Alberic_of_Monte_Cassino · books.google.com (Camargo, *Ars Dictaminis, Ars Dictandi*) · ocw.mit.edu · alim.unisi.it |
| *Modus Tenendi Parliamentum · Thomas Smith · Icelandic Alþingi/lawspeaker* | §7.1 deliberative bodies; framing-authority / turn-order; the Lawspeaker | en.wikipedia.org/wiki/Modus_Tenendi_Parliamentum · tandfonline.com (10.1080/03044181.2022.2131601) · archive.org · ancient-origins.net (Alþingi) |
| *ambassador treatises · du Rosier · Gentili · Callières* | §8.3 the ambassador literature; relationship/reputation negotiation model | academia.edu & researchgate.net (Rosier, in *Encyclopedia of Diplomacy*) · classicsofstrategy.com (Callières) · books.openedition.org/efr/2907 |
| *medieval petition · supplication · common petition · French remontrance · appeal to sovereign* | §8.1–8.2 petition/supplication, *requête*, remontrance, *appel comme d'abus* | cambridge.org (*Historical Journal*, "From Requête to Petition: Petitioning the Monarch Between Empires") |

`[CONFIDENCE: high]` on the 11.1 mappings (re-verified this session). `[CONFIDENCE: medium]` on 11.2 — these reflect the prior session's searches recovered from the session transcript; the texts themselves are listed in §10, and the contested-attribution flags in §0.4 apply.

### 11.3 Primary-language scholarship (2026-06-02 follow-up pass — grounds §12)

| Search (language) | Grounds | Key sources |
|---|---|---|
| *naẓm · al-Jurjānī · Dalāʾil al-iʿjāz · ʿilm al-maʿānī · muqtaḍā al-ḥāl* **(Arabic)** | §12.1 — *naẓm* as توخي معاني النحو; meaning-in-relations | habous.gov.ma (دعوة الحق) · asjp.cerist.dz (ASJP, 2 articles) · ar.wikipedia.org/wiki/نظرية_النظم · bhoth.net · makkahnews.sa |
| *鬼谷子 · 捭阖 · 揣摩 · 纵横家 · 说难* **(Chinese)** | §12.2 — 捭阖 open/close, 阳言/阴言, 量权/揣情 | sem.tsinghua.edu.cn · tuiir.tsinghua.edu.cn (王鹏 & 郭莹, 纵横家的联盟思想, PDF) · zhihu.com · bbs.pinggu.org |
| *supplique · requête au roi · remontrance · grâce · évocation* **(French)** | §12.3 — *supplique* vs *remontrance*; escalation ladder; jurisdiction-decides | fr.wikipedia.org/wiki/Droit_de_remontrance · conseil-constitutionnel.fr · books.openedition.org/pur (PUR) · univ-droit.fr (colloque) · metahodos.fr (M. de Cazals) |
| *Statuslehre · Hermagoras · Stasislehre · status rationales/legales* **(German)** | §12.4 — *rationales* vs. (later-systematized) *legales*; fallback ladder; *krinomenon*; 13=declamation — **corrected via Heath** | de.wikipedia.org/wiki/Statuslehre_(Rhetorik) · rheton.at (Schirren, *HSK* 31.1) · stroh.userweb.mwn.de (W. Stroh) · Barwick *Philologus* 105/108/109 (1961–65), Braet *Mnemosyne* — *via Heath, not direct* |

`[CONFIDENCE: high]` on the §12 readings; sources are primary-language academic/reference works. My rendering of each into English is faithful to the cited sources; where a reading is the mainstream interpretation rather than an explicit source statement, §12 flags it inline.

### 11.4 Primary-language scholarship — extension pass (2026-06-02 — grounds §12.5–§12.8)

| Search (language) | Grounds | Key sources |
|---|---|---|
| *eloquenza politica · ars arengandi · concione · Matteo dei Libri · Artifoni* **(Italian)** | §12.7 — the *concione*; Brieflehre→Redelehre; *bene comune* | academia.edu (E. Artifoni: "…la concione"; "Preistorie del bene comune"; "Orfeo concionatore"; Boncompagno/Bologna) · riviste.unimi.it (Montefusco & Bischetti, *Carte Romanze*) · donzelli.it |
| *lögsögumaður · Alþingi · Lögrétta · Grágás · þingsköp · goði* **(Icelandic / Old Norse)** | §12.8 — Lawspeaker (procedural/session-bound); Lögrétta geometry; consensus→lot→majority | is.wikisource.org/Grágás (*Lögsögumannsþáttur*, *Lögréttuþáttur*) · thingvellir.is · althingi.is · skemman.is (B.A. thesis) · is.wikipedia.org/Lögsögumaður |
| *βυζαντινή ρητορική · προγυμνάσματα · βασιλικὸς λόγος · Μένανδρος* **(Greek)** | §12.5 — epideictic dominance; *κάτοπτρο ἡγεμόνος*; the 12 progymnasmata | spacezilotes.wordpress.com (Βυζαντινή Λογοτεχνία) · ddikaios.blogspot.com (κάτοπτρο ηγεμόνος, Thomas Magistros) · ecourse.uoi.gr (Βυζαντινή Ρητορική, Ε. Καλτσογιάννη) · en.wikipedia (Menander Rhetor) |
| *न्याय · शास्त्रार्थ · वाद/जल्प/वितण्डा · निग्रहस्थान · छल · जाति* **(Hindi / Sanskrit)** | §12.6 — 16 *padārthas*; degeneration ladder; *nigrahasthāna* defeat-conditions | hi.wiktionary.org/न्याय · nyaydarshannotes.blogspot.com (*Nyāya-sūtra* 1.1.1) |

Note: the Greek and Hindi searches each returned substantial unrelated medical-preprint noise (Devanagari/Greek-script query artifacts); those hits were ignored and are not sourced above.

---

### 11.5 Academic re-grounding pass (2026-06-03) — source tiers for §12

A self-audit found §12's citations uneven (some peer-reviewed, much tertiary). The weak strands were regrounded on peer-reviewed scholarship, and **Heath (1994) was fetched and read directly**, yielding one correction (§12.4: Hermagoras *excluded* legal questions from the staseis; *status legales* is later systematization). **Tier key:** `[PR]` peer-reviewed article / academic-press monograph / critical edition · `[REF]` scholarly reference (handbook, encyclopedia, university course, official) · `[PRIM]` primary source in edition/translation · `[TER]` tertiary/popular (Wikipedia, blog, forum, news) — corroborating only.

| Strand | Carrying sources (now consulted) | Tier | Tertiary (corroborating only) |
|---|---|---|---|
| §12.1 Arabic | Larkin 1995; Abu Deeb 1979; Tsung diss. (UC); al-Azmeh 1986; al-Jurjānī *Dalāʾil*/*Asrār* | PR ×4 + PRIM | ASJP, habous.gov.ma, ar.wikipedia |
| §12.2 Chinese | Tsinghua study (王鹏 & 郭莹, *zonghengjia* alliance thought); *Guiguzi* / *Han Feizi* | PR + PRIM | zhihu, bbs.pinggu, 163 |
| §12.3 French | Conseil constitutionnel *Cahiers*; PUR (OpenEdition); univ-droit colloque; de Cazals | PR/REF ×3 | fr.wikipedia, metahodos, histoire-itinerante |
| §12.4 German+Heath | **Heath 1994 (read directly)**; Schirren *HSK*; Matthes (Hermagoras frr.); Cicero/Quintilian | PR ×3 + PRIM | de.wikipedia; *Barwick/Braet via Heath, not direct* |
| §12.5 Byzantine | Russell & Wilson 1981; Loeb Menander II; Omissi & Ross 2020; Nuti *GRBS*; Kennedy 1983; *ODB* | PR ×5 + REF + PRIM | spacezilotes, ddikaios, uoi.gr |
| §12.6 Nyāya | Matilal 1998; Vidyabhūṣaṇa 1921; Dharmakīrti *Vādanyāya*; Preisendanz 2009; *Nyāya-sūtra* | PR ×4 + PRIM | dharmawiki, anaadi, hi.wiktionary |
| §12.7 Italian | Artifoni (several); Montefusco & Bischetti, *Carte Romanze*; Donzelli | PR ×2 + REF | Gutenberg ed. = PRIM |
| §12.8 Old Norse | *Grágás* (wikisource); skemman.is (univ. thesis); althingi.is; thingvellir.is | PRIM + REF ×3 | ferlir, is.wikipedia |

Honest residual: §12.2 (Chinese) and §12.8 (Old Norse) lean more on a single academic anchor plus reference/official sources than the others; §12.7's Artifoni papers are academic but accessed as academia.edu offprints, not via a library. After this pass the tertiary column nowhere *carries* a claim — it corroborates.

---

## 12. PRIMARY-LANGUAGE SCHOLARSHIP — divergent insight

*Added in the 2026-06-02 follow-up pass, per Jordan: "even academic writing in the primary language gives different insight." Each strand records what scholarship written **in** the tradition's own language adds beyond the English summaries in §§1–8 — not new primary texts, but the framing the Anglophone reception flattens. Language-tagged; design implications stay Jordan-vetoable; nothing here rewrites canon. The extension and academic re-grounding passes now cover eight traditions (§12.1–§12.8); per-strand source tiers are consolidated in §11.5.*

### 12.1 Arabic — *balāgha* is construction, not ornament (deepens §3.1)

Arabic scholarship on al-Jurjānī's *naẓm* (نظم) is far more precise than the English "word-order matters." The standard academic treatments — **Margaret Larkin, *The Theology of Meaning: ʿAbd al-Qāhir al-Jurjānī's Theory of Discourse*** (American Oriental Society, 1995) and **Kamal Abu Deeb, *Al-Jurjānī's Theory of Poetic Imagery*** (1979) — establish that *naẓm* (construction) is the **basis of eloquence**: not a random combination of sounds but the mind's ordering of words, such that **the structure of a composition is determined by its meaning, and eloquence lies in the interrelationship of syntax and semantics** (so the abstract of an open-access UC dissertation supervised by Larkin summarises al-Jurjānī's claim). Al-Jurjānī's own formula — *inna al-lafẓa tābiʿun li-l-maʿānī fī l-naẓm*, "the word follows the meanings in construction," words ordered in speech *according to the order of their meanings in the mind* (Abu Deeb's translation, *Dalāʾil* p.78) — makes the point exactly: **excellence (*al-maziyya*) is never in the isolated word but in the relations among words**, realised through the concrete, enumerable operations of grammar (*maʿānī al-naḥw*) — تقديم/تأخير fronting, حذف/ذكر ellipsis, تعريف/تنكير definiteness, إضمار implicitness — fitted to *muqtaḍā al-ḥāl*, the requirement of the situation. Aziz al-Azmeh judged the theory "one of the most sustained, refined, rigorous and durable attempts to construct a theory of the production of meaning … in any language and at any time." **Design implication:** if Valoria ever models *how* an argument is phrased (not just which stasis/genre), *balāgha* supplies a clean primitive — a small set of *structural* choices, each altering the force of the *same* propositional content, fitted to the audience-situation: "construction = meaning," not "ornament points." `[CONFIDENCE: high — regrounded on peer-reviewed scholarship; the earlier Arabic-web sources now corroborate, not carry, the claim.]`
**Sources:** Larkin 1995 `[PR]`; Abu Deeb 1979 `[PR]`; Tsung (UC eScholarship, adv. Larkin), open-access diss. `[PR]`; al-Azmeh, *Arabic Thought and Islamic Societies* (1986) `[PR]`; al-Jurjānī, *Dalāʾil al-iʿjāz* (ed. Shākir) / *Asrār al-balāgha* (ed. Ritter 1954) `[PRIM]`; ASJP article, habous.gov.ma, ar.wikipedia `[REF/TER — corroborating]`.

### 12.2 Chinese — the dyadic art has its own internal structure (deepens §4, §9.4)

Chinese scholarship on the 鬼谷子 (*Guiguzi*) and 縱橫家 (*zonghengjia*) gives the dyadic method a structure my English §4 only gestured at. **捭阖 (bǎi-hé)** is a yin-yang pair of speech operations — 捭 *open* (actively draw the interlocutor out; yang/active) vs. 阖 *close* (make him withhold/shut; yin/static) — coupled with two opposite registers: **阳言 (yáng-yán)**, persuading via what the target *desires* (longevity, wealth, fame, ease), and **阴言 (yīn-yán)**, moving him via what he *fears* (death, calamity, punishment, loss). The matching rule is character-typed: lofty/yang speech for the noble (君子), low/yin speech for the base (小人). The speech is preceded by a two-variable assessment — 《鬼谷子·揣》's **量权 (liàng-quán, weigh [external] power)** and **揣情 (chuǎi-qíng, estimate [inner] disposition)**: "weigh the power of all-under-heaven, and estimate the disposition of the lords." Chinese academic work (e.g. the Tsinghua study of the *zonghengjia*'s alliance thinking) stresses what separates this from Confucian rhetoric: it is **individual-level, pragmatic, success-metered** — the aim is to gain position by successfully advising the ruler, and the speech "need not conform" to conventional morality. **Design implication:** the dyadic art is a *distinct game* with its own loop — **scan (power + disposition) → open or close → desire- or fear-register, matched to character** — separate from the public-contest stasis/genre machinery. Concrete support for treating §9.4's dyadic/public split as two mechanics, not one engine with an "audience" toggle. `[CONFIDENCE: high on the bǎi-hé / chuǎi-mó structure; sources Chinese; the 趋利避害 desire/fear framing is the mainstream reading.]`

### 12.3 French — the appeal to power is *two* instruments, with an escalation ladder (deepens §8.2; restructures §9.5)

French legal-historical scholarship sharply distinguishes two things English lumps as "petition":
- the **placet / supplique / requête** — "extremely reverential writings addressed to the king or a minister to obtain a *grâce* or a *faveur*" (M. de Cazals): a bottom-up appeal for grace / pardon / grant / office. (The form is ancient — Dioscorus of Aphrodito's 6th-c. "requête et supplique.")
- the **droit de remontrance** — the right of the *Parlements* (sovereign courts), **not** private subjects, to **contest a royal edict before registering it** if judged contrary to the realm's fundamental laws, returning it with motivated objections and *praying the king to re-examine*. French scholarship frames it exactly as "art de gouverner et contestation légitime" — constitutionally-sanctioned critique, the nearest Ancien-Régime analogue to a pre-enactment amendment/veto.

The remontrance carries a **ready-made escalation ladder**: the Parlement remonstrates → the king issues a **lettre de jussion** (command to register) → the Parlement files **remontrances itératives** → the king imposes a **lit de justice** (appears in person and forces transcription). Separately, the **évocation** (the Crown pulling a case to a court of its choosing) plus the maxim that *in the Middle Ages it is the **jurisdiction**, more than the justice of the cause, that decides the outcome* independently corroborate CR4's translative-stasis = **the Stay** (§9.3) — now from French legal history, not classical rhetoric. **Design implication for §9.5:** the proposed appeal subsystem should be **two instruments** — *supplique* (subject→sovereign, seeks *grâce*; bottom-up) and *remontrance* (institution→Crown, contests a measure; a legitimated check with the jussion → itérative → lit-de-justice standoff) — not one. `[CONFIDENCE: high; sources French.]`

### 12.4 German (corrected via Heath) — Hermagoras's system, the *status legales* question, and stasis as a fallback ladder (corrects/deepens §1.4, §9.3)

German *Staseislehre* scholarship is the most rigorous on the spine, but one claim I drew from it needs correcting against the primary scholarship. **Hermagoras of Temnos** founded the *status* doctrine (his lost *Technai rhetorikai*, reconstructible from Cicero's *De inventione* and Quintilian's *Institutio* III; fragments ed. Matthes). The familiar **four "rational" stases** — fact / definition / quality / jurisdiction (*status rationales*) — analyse a dispute "according to the underlying structure" so the rhetor can pick a strategy fit for *that kind* of dispute: as **Malcolm Heath** puts it, "patterns of argument appropriate to a question of fact … may be irrelevant in an evaluative dispute" (*CQ* 44, 1994 — **read directly**). **Correction to my earlier draft:** I had called Hermagoras's system "two-axis," pairing the four *rationales* with a parallel set of *status legales*. Heath shows the opposite for Hermagoras *himself*: he **excluded** the legal/textual questions (*nomika zētēmata*, those *peri rhētou* — about the letter of a law: ambiguity, letter-vs-intent, conflicting statutes) **from** the system of staseis, because they do not grasp the *hypokeimenon pragma* (the underlying matter). Packaging those legal questions as a co-equal *status legales* axis is the **later Latin/Hermogenic systematization**, not Hermagoras's own — and Heath's larger thesis is that Hermagoras's *aition–sunekhon–krinomenon* substructure progressively **broke down** (Cicero's shifting positions track the breakdown; Zeno and Hermogenes abandoned the scheme). The **krinomenon** — the precise point the case turns on — is the operational heart (Hermogenes ascertains stasis by inspecting it, though, Heath notes, he never defines it). German scholarship adds two further readings: *status* as a **graded fallback ladder** (Lausberg's "Kampflage" / combat-stance — deny the act → deny the law applies → admit-but-justify), and the **13 status** of Hermogenes/Zeno as tailored *not* for forensic practice (the imperial forum had declined) but for **fictional declamation in the rhetoric schools**, while Quintilian sought a *practicable reduction*. **Design implications:** (1) a **statutory-dispute layer** (ambiguity / letter-vs-intent / conflicting edicts) is real and well-attested in the tradition (Cicero *De inv.*; Quintilian *Inst.* III) — a natural fit for the Parliamentary/tribunal layer `[Proposed — Jordan call]` — but present it as the *legal-questions* set the **Latin tradition systematized**, not as a native Hermagorean second axis; (2) §9.3's forensic tree is more exactly a **strongest-tenable-rung fallback ladder**; (3) the **13-status = declamation inflation** is a NERS-Elegance guardrail with historical authority; (4) the ancients' **Quintilian-reduction vs. Hermogenes-network** tension is a precedent for the resolution-diagnostic's elegance-vs-completeness tradeoff. `[CONFIDENCE: high; Heath read directly; this corrects the prior German-Wikipedia-derived overstatement.]`
**Sources:** Heath, "The Substructure of stasis-theory from Hermagoras to Hermogenes," *CQ* 44 (1994), open-access (White Rose) — **read directly** `[PR]`; Schirren, "Statuslehre," *HSK* 31.1 (2008) `[PR/REF]`; D. Matthes ed., Hermagoras fragments (*Lustrum* 3, 1958) `[PR]`; Calboli Montefusco, *La dottrina degli status* (1986); Barwick, *Philologus* 105/108/109 (1961–65) — **cited within Heath, not consulted directly** `[PR, second-hand]`; Cicero *De inventione* / Quintilian *Inst.* III `[PRIM]`; de.wikipedia *Statuslehre* `[TER — corroborating]`.

### 12.5 Byzantine Greek — regime decides the load-bearing genre (deepens §2; relates §9.4)

Greek/Byzantine scholarship makes a point the English summary blurs. Of antiquity's three genres — συμβουλευτικό (deliberative), δικανικό (forensic), ἐπιδεικτικό (epideictic) — **Byzantium cultivated overwhelmingly the epideictic**, the ceremonial rhetoric of praise and blame. With no deliberative civic assembly and a bureaucratic-imperial order, the *living* prestige genre was the **βασιλικὸς λόγος** (imperial oration / encomium of the emperor), whose parameters were fixed by **Menander Rhetor** and edited as the scholarly standard by **D. A. Russell & N. G. Wilson, *Menander Rhetor*** (Oxford 1981, 76–95). Menander's own text is revealing — the royal oration "is an encomium of the emperor … it excludes anything ambiguous or disputed … base your composition on qualities acknowledged to be good" (Loeb, *Treatise* 2.1): i.e. it is *pure* epideictic, the **opposite** of a stasis-driven contest, since nothing is *at issue*. Recent scholarship reads Menander as **descriptive** — condensing third-century panegyric practice into guidelines rather than inventing them (Omissi & Ross, *Imperial Panegyric from Diocletian to Honorius*, 2020) — and the genre's Byzantine afterlife is well studied (e.g. *GRBS* 56 on Chrysoloras's funeral-oration-as-*basilikos logos*; the *Oxford Dictionary of Byzantium*, Kazhdan–Jeffreys). For political *counsel*, the cognate genre is the **mirror of princes**: Agapetus the Deacon's *Ekthesis* to Justinian (6th c.) is the locus classicus, with late examples such as Thomas Magistros's *On Kingship* to Andronikos II — delivering *deliberative content (advice on right rule)* in epideictic form to a sovereign who cannot be openly debated. The school ladder stayed the **12 progymnasmata** (μῦθος, διήγημα, χρεία … ἐγκώμιον/ψόγος … νόμου εἰσφορά), Hermogenes's corpus organising it (Kennedy, *Greek Rhetoric under Christian Emperors*, 1983). **Design implication:** the **political regime determines which genre is load-bearing** — a republic/commune runs on *deliberative* oratory (the concione, §12.7), an autocracy on *epideictic* (ceremonial standing + the mirror-of-princes), and both keep *forensic* for trials. For Valoria's venues the same actor plays different rhetorical games by venue: before the Crown, advise-by-encomium (dyadic, ceremonial — cf. §12.2, §9.5); before Parliament, deliberative; before the tribunal, forensic. Weight genre by the venue's political form. `[CONFIDENCE: high — regrounded on peer-reviewed scholarship + the Loeb primary text. The epideictic-dominance thesis is standard; the specific *kátoptron* framing rests on the standard examples (Agapetus, Thomas Magistros) and is reference-tier.]`
**Sources:** Russell & Wilson, *Menander Rhetor* (Oxford 1981) `[PR]`; Menander Rhetor, *Treatise* 2 (Loeb) `[PRIM]`; Omissi & Ross (eds.), *Imperial Panegyric from Diocletian to Honorius* (2020), open-access (Glasgow) `[PR]`; Nuti, *GRBS* 56 (2016) `[PR]`; Kennedy, *Greek Rhetoric under Christian Emperors* (1983) `[PR]`; Kazhdan & Jeffreys, *Oxford Dictionary of Byzantium* (1991) `[REF]`; Agapetus *Ekthesis* / Thomas Magistros *Peri basileias* `[PRIM]`; spacezilotes, ddikaios, uoi.gr course `[REF/TER — corroborating]`.

### 12.6 Hindi / Sanskrit — debate as a truth-procedure with defeat-conditions (deepens §5; relates §9.3)

Academic Indology and the Sanskrit primary text embed the debate theory in a frame the English reception strips out. The *Nyāya-sūtra* opens (1.1.1) by listing **sixteen categories** (*padārtha*) whose true knowledge yields *liberation* (*niḥśreyasa / mokṣa*): *pramāṇa* (means of knowledge), *prameya*, *saṃśaya*, *prayojana*, *dṛṣṭānta*, *siddhānta*, *avayava*, *tarka*, *nirṇaya*, **vāda / जल्प jalpa / वितण्डा vitaṇḍā**, *hetvābhāsa*, **chala, jāti, nigrahasthāna (निग्रहस्थान)**. So debate is one limb of an *epistemology* (*pramāṇa → nirṇaya*) whose telos is truth-ascertainment and ultimately liberation — **a truth-procedure, not a persuasion contest** (sharply unlike the Greek audience-model and the Chinese ruler-model). The three modes are defined in the sūtras: **vāda** (NS 1.2.1) is honest debate — one's thesis defended by genuine *pramāṇa*, the opponent's refuted by *tarka* — the cooperative truth-seeking of teacher and disciple; **jalpa** (NS 1.2.2) adds *chala* (quibbling) and *jāti* (false similarity-rejoinder) — *vāda* turned to winning; **vitaṇḍā** is refutation-only, with no counter-thesis of its own. **B. K. Matilal** (*The Character of Logic in India*, 1998) labels the latter two the "j-type" and "v-type" hostile debate, and notes — quoting Uddyotakara — that one studies these "bad tricks" precisely *to avoid them oneself and detect them in the opponent*. The procedure **terminates by defined defeat-condition**: the *Nyāya-sūtra* enumerates **22 *nigrahasthāna*** (so **Vidyabhūṣaṇa**, *A History of Indian Logic*, 1921, 84–90) — "clinchers" / points of defeat such as self-contradiction, evasion, or silence when pressed — at which the debate is force-closed and one side declared defeated; the Buddhist **Dharmakīrti** later rebuilt the list in his *Vādanyāya*. **Design implication:** Nyāya supplies a **defeat-by-defined-condition** resolution distinct from "accumulate persuasion to a threshold" — a debate/tribunal can end the moment the opponent *incurs a named fault*, an enumerable **loss-condition catalogue** adjudicated against a checklist, not a knife-edge roll (a clean fit for a deterministic engine — cf. the resolution-diagnostic's preference for conditions/clocks over fragile small-pool rolls). It also *formalises* §12.2's self-gating: resorting to *chala/jāti* is itself a defeat-trigger. And the **vāda vs. jalpa/vitaṇḍā** split is a mode distinction — cooperative truth-seeking vs. adversarial win-at-all-costs — i.e. different win-conditions on one engine (cf. §9.4). `[CONFIDENCE: high — regrounded on Matilal + Vidyabhūṣaṇa + the NS primary text; the earlier Wiktionary/blog sources now corroborate, not carry.]`
**Sources:** B. K. Matilal, *The Character of Logic in India* (ed. Ganeri & Tiwari, 1998) `[PR]`; S. C. Vidyabhūṣaṇa, *A History of Indian Logic* (1921) `[PR]`; Dharmakīrti, *Vādanyāya* (ed./tr. Gokhale) `[PR/PRIM]`; *Nyāya-sūtra* 1.1.1 / 1.2.1–2 with Vātsyāyana's *bhāṣya* `[PRIM]`; Preisendanz (2009) on Caraka's *saṃbhāṣā* `[PR]`; dharmawiki, anaadi.org, hi.wiktionary `[REF/TER — corroborating]`.

### 12.7 Italian — the *concione*, and rhetoric grown from letter to speech (deepens §6.2; relates §7.1, §9.5)

Italian scholarship (Enrico Artifoni, the leading authority) recovers a form the English summary barely names: the **concione** — the public political harangue before the civic assembly in the 13th-c. communes. Its key insight is a *genealogy*: the **ars arengandi** (art of public speech) grew **out of the ars dictaminis** (art of the letter) — *dalla* Brieflehre *alla* Redelehre, from letter-doctrine to speech-doctrine, captured in the slogan *"parla come scrivi"* / "speak as you write." The progression runs from the *Oculus pastoralis* and Boncompagno's *Rhetorica novissima* through "ars dictaminis with address-variations" and conduct-manuals-with-model-speeches to "pure *artes arengandi*"; Artifoni calls the 13th-c. ars arengandi a *"scuola di comunicazione"* for the commune, bound to an ideology of the **bene comune** (common good) and the self-governing city (Brunetto Latini's vernacular Cicero "alongside the *auctoritas*"; Albertano da Brescia's civic sermons). **Design implication:** the **concione** is a sourced model for *public deliberative oratory before a civic body* — distinct from the private appeal and the tribunal — and the **letter→speech genealogy** lets one *compositional engine* drive two delivery modes: the **written** appeal (supplique / ars dictaminis, §12.3/§9.5) and the **spoken** address (concione / ars arengandi, the Parliamentary floor). The tie to *bene comune* gives civic deliberation a venue-specific ethos resource — legitimacy by appeal to the common good — distinct from the Crown-encomium register (§12.5). `[CONFIDENCE: high; sources Italian (with a German study of Artifoni's work).]`

### 12.8 Old Norse / Icelandic — procedural, session-bound authority (deepens §7.1; relates §9.2; on-theme for the Norse setting)

Icelandic scholarship and the Old Norse *Grágás* law-text itself sharpen the assembly model the English summary only sketched. The **lögsögumaður (Lawspeaker)** was the commonwealth's (*þjóðveldi*) **only paid official**, elected by the **Lögrétta** for **three-year terms**; his office was to **hold the law in memory** and **recite a third of it aloud each year** at the **Lögberg** (Law Rock), reciting the **þingsköp** (standing orders / assembly procedure) *every* year, and to answer questions on the law (he could consult *lögfróðir menn*, law-wise men, before pronouncing). Crucially his authority was **procedural and session-bound, not executive**: at the Alþingi "the most powerful man in the land," but *between* assemblies "formally powerless" — a chair/reciter (*fundarstjóri*), not a ruler or judge. The **Lögrétta** (law-council — legislative, dispute-resolving, and dispensation-granting) seated **48 *goðar* (chieftains), each flanked by two advisors** he could consult during the session, deciding by a **consensus → lot (by quarter) → majority (*afl ráða*)** cascade, with three-marks fines for procedural failure (*Grágás*, *Lögsögumannsþáttur* / *Lögréttuþáttur*). The **Lögberg** was an open platform where *anyone* could step forward to speak on important matters — distinct from the closed Lögrétta. **Design implications (and on-theme, given Valoria's Norse setting):** (1) the lögsögumaður models a **procedural, session-bound framing-authority** — a Speaker/chair whose power is to recite the rules, chair, and rule on procedure, real *only* during the assembly and bounded away from outcomes — distinct from the Crown (cf. §9.2 "who poses the question and in what order members speak"); (2) **law-as-recited-memory** (a third per year) is a striking pre-literate mechanic — the rules are an in-world artifact re-established each session; (3) the **goði + two counsellors** seat is a distributed-deliberation primitive (bounded consultation per voter); (4) the **consensus → lot → majority** cascade is a sourced decision procedure; (5) the **open Lögberg vs. closed Lögrétta** is a two-venue split — public proclamation/speech vs. closed law-making — mirroring the concione/council distinction (§12.7). `[CONFIDENCE: high; sources Icelandic + Old Norse (Grágás).]`

<!-- END OF CORPUS -->





