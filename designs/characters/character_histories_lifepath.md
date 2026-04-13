# VALORIA — Character Histories: Lifepath System
## Status: DESIGN PROPOSAL — requires editorial approval
## Scope: Lifepath-based History generation producing characters with geographic roots, relational depth, and faction texture
## Cross-references: params_core.md, combat_design_v1.md, social_contest_system_v2.md, mass_battle_v3.md, stage6_factions.md, threadwork_redesign_v25.md (Knots, Beliefs, Coherence)
## [EDITORIAL: ED-374 — Character Histories system. Setting/worldbuilding/character content — editorial gate applies.]
## Supersedes: prior occupational Histories list (character_histories.md v1)

---

## Structure

Character creation moves through **four lifepath stages**. Each stage answers a biographical question and grants one History. A character enters play with **four Histories** (one per stage).

| Stage | Question | What It Determines | Starting Skills |
|---|---|---|---|
| 1. Origin | Where were you born and who raised you? | Geographic roots, cultural baseline, starting Certainty, first Knot | 0 (spark only) |
| 2. Formation | How were you educated or shaped? | Intellectual/spiritual framework, institutional exposure, second Knot | 1 |
| 3. Vocation | What were you trained to do? | Professional skills, factional affiliation, third Knot | 2 |
| 4. Catalyst | What happened that put you on this path? | Inciting incident, starting Belief, campaign hook | 0 (spark only) |

**Starting skills: 3 total** (1 from Formation + 2 from Vocation). All start at Level 1 and auto-equip. Origin and Catalyst skills live on their spark lists and are acquired through scene use.

**Recall as skill gatekeeper:**
- **Equip slots:** `max_equipped = Recall` (1–7). All sparked skills retained permanently; only Recall-many active at any time. Swap loadout between scenes.
- **Skill depth:** Skills have Levels 1–3. Level 2 requires History dice_bonus ≥ 3; Level 3 requires dice_bonus ≥ 5. Recall caps dice_bonus, so Recall indirectly caps max level. Recall 4 = Level 2 ceiling. Recall 5+ = Level 3 access.
- **Learning speed:** `floor(Recall/2)` bonus dice on all spark checks.
- **Coherence erosion:** Fragmented = effective Recall −1 (lose 1 slot). Fractured/Severed = effective Recall −2 (lose 2 slots). Practitioners who push Coherence low lose skill access — the cost of Thread practice is erosion of competence.

**Knot generation:** Stages 1–3 each produce a suggested Close Knot — a named relationship that the player defines. Stage 4 produces a starting Belief. The player chooses which Knots to keep as Close Knots (max 3) and which become Distant Knots (background relationships that can be activated in play).

**Certainty:** Stage 1 sets the baseline. Later stages can modify it. Final Certainty is recorded after all four stages.

**Sparking (SaGa-style):** After any meaningful scene roll (Ob ≥ 2), check for skill spark. Overwhelming at Ob 3+ = automatic. Success/Partial/Failure at sufficient Ob = Spirit + Recall/2 check. Sparks prioritise level-ups over new acquisitions. Cross-History hybrid sparks fire when 2+ Histories are used in same scene.

---

## STAGE 1: ORIGIN — Where were you born and who raised you?

Origin establishes the character's geographic and cultural foundation. It determines what "normal" means to them — what the world looks like before education, training, or crisis changes it.

**Origin grants 0 starting skills.** All skills listed below are on the Origin's spark list — they are acquired through scene use, not at character creation. This means Origin skills must be earned in play, reinforcing the idea that your birthplace shapes your potential, not your competence.

---

### 1A. Crown Heartland Child
Born in the eastern lowlands — Valorsplatz, Kronmark, Feldmark, or Stillhelm. Raised within the Crown's institutional orbit. Your family are farmers, tradespeople, minor officials, or soldiers. The river, the farmland, the capital's spires — this is the world as you first knew it.

**Who raised you:** A family embedded in the Crown's civil order. Your father served, your mother served, or both — the Crown is not just a government here, it is the texture of daily life. Markets run on Crown coin, roads are Crown-maintained, disputes go to Crown magistrates.

**Starting Certainty:** 4 (Average Valorian). The Church is present, respected, part of the seasonal rhythm — but the Crown is the institution that shapes your life.

**Suggested Knot:** A family member still living in the heartland — parent, sibling, or childhood friend. They represent the life you left. They write you letters. They worry.

**Spark list** (acquired through scene use, not at creation):

| Skill | Domain | Effect (Level 1) |
|---|---|---|
| **Heartland Roots** (unique) | Faction Play | In Crown-held territories: +1D on Domain Actions involving public order, recruitment, or community relations. This is your country — you know how things work here. |
| **River Knowledge** § | Investigation / Faction Play | +1D on any roll involving river transport, eastern trade routes, or Valorsplatz logistics. The river is the spine of the economy you grew up in. |
| **Sturdy Stock** § | Scene Battle | Stamina base +1 (stacks with formula). Heartland children grow up working. |

**Narrative experiential impact:** The heartland is Valoria's productive core — the food, the trade, the tax base. You were raised inside the system that everyone else is trying to influence, control, or overthrow. Scenes in the Crown heartland feel like homecoming; scenes in the western fjords or the southern territories feel foreign. You carry an unconscious assumption that the Crown's order is the natural state of things, and the campaign will test that assumption.

---

### 1B. Highland Born (Hafenmark)
Born in the northwestern highlands — Gransol, Rendstad, Spartfell, or Halvarshelm. Raised in the landlocked, mineral-rich, Swiss-character territory that Altonia squeezed hardest during the occupation.

**Who raised you:** A highland family — miners, herders, artisans, or minor functionaries in Baralta's constitutional apparatus. Your community is tight, procedural, suspicious of outsiders and central authority alike. The occupation ended generations ago but its shadow shapes everything: the emphasis on law, the distrust of charismatic leaders, the institutional stubbornness.

**Starting Certainty:** 4 (Average Valorian). The Church is present but culturally secondary to Hafenmark's constitutional identity. Faith is private; law is public.

**Suggested Knot:** A community elder, guild master, or extended family figure who embodies Hafenmark's constitutional values. They taught you that procedure is not bureaucracy — it is the wall between civilisation and tyranny.

| Skill | Domain | Effect |
|---|---|---|
| **Highland Toughness** (unique) | Scene Battle / Mass Battle | In cold, high-altitude, or mountainous conditions: no environmental penalties. Others suffer; you were born here. |
| **Institutional Instinct** § | Debate | In any proceeding governed by formal rules (Parliament, Tribunal, Arbitration): +1D on Appraise rolls. You sense procedural irregularities the way other people sense weather changes. |
| **Community Solidarity** § | Faction Play | In Hafenmark-held territories: +1D on Stability-related Domain Actions. Highland communities hold together. |

**Narrative experiential impact:** Hafenmark's identity is constitutional — law over personality, procedure over charisma. You were raised in this worldview, and it gives you a specific strength (resistance to demagogues) and a specific blindness (distrust of action that cannot be procedurally justified). Scenes involving legal argument, institutional politics, or the defence of constitutional order feel natural. Scenes requiring improvisation, moral flexibility, or alliance with extraconstitutional actors (like the Restoration Movement or Niflhel) create productive tension with your upbringing.

---

### 1C. Fjord Child (Varfell)
Born on Varfell's western coast — Sigurdshelm, Halvardshelm, Oastad, or Grauwald. Raised in the Norwegian-character fjord communities connected by sea and separated by mountains.

**Who raised you:** A fjord family — sailors, herders, fisher-folk, or minor retainers of the Vaynard household. Your world is maritime, isolated, practically self-sufficient. Communities are small, interdependent, and aware that the capital considers them provincial. The Einhir presence is strongest here — folk practices survive in the southwest as living tradition, not historical curiosity.

**Starting Certainty:** 3 (Secular) in southern Varfell (Oastad, near the Southernmost), 4 (Average Valorian) in northern Varfell. The Church's reach is thinnest here. Folk knowledge persists.

**Suggested Knot:** A member of your fjord community — a fisher, an elder, a childhood rival who became a friend. They represent the specific, small-scale world that factional politics threatens to swallow.

| Skill | Domain | Effect |
|---|---|---|
| **Sea-Bred** (unique) | Scene Battle | On water or coastal terrain: +1D to Defence. You grew up on boats; unstable footing is normal footing. |
| **Fjord Isolation** § | Investigation | In Varfell territories: +1D on Attunement-based rolls to detect outsiders, unfamiliar activity, or changed patterns. Small communities notice everything. |
| **Practical Self-Reliance** § | Scene Battle / Investigation | When no allies are present in the zone: +1D to one roll per scene (any domain). You learned early that help is far away. |

**Narrative experiential impact:** The fjords are beautiful and isolated. You grew up connected to your community and disconnected from the peninsula's political centre. Scenes on the western coast feel like home; scenes in Valorsplatz or Himmelenger feel like a different country. If you are from southern Varfell (Oastad), the Calamity's influence is part of your childhood — strange happenings near Einhir sites, animals unsettled for no reason, elders who know things they cannot explain. This proximity to the wound shapes your relationship to Thread truth in ways that formal education never could.

---

### 1D. Southern Einhir Descendant
Born in the communities closest to the Southernmost — southern Oastad, the settlements ringing Askeheim, or the scattered hamlets in the territories at node distance 1–2. Raised in the cultural shadow of the Catastrophe.

**Who raised you:** An Einhir-descendant family. This does not mean practitioners — it means people whose grandparents' grandparents spoke a different language, practised different rites, and understood the world through a framework the Church has spent 245 years suppressing. The Forgetting has eroded much of this inheritance, but fragments survive: songs without translatable lyrics, ritual gestures performed at births and deaths, an inherited unease about the Solmund narrative that cannot be articulated but will not dissipate.

**Starting Certainty:** 2–3 (Skeptic to Questioning). The Church's account of reality does not match your inherited experience. You may not be able to say why — the Forgetting makes the alternative inarticulable — but the dissonance is real and lifelong.

**Suggested Knot:** A grandmother, an elder, or a community figure who carries Einhir tradition. They taught you the songs, the gestures, the practices. They could not explain why they matter. They matter anyway.

| Skill | Domain | Effect |
|---|---|---|
| **Inherited Resonance** (unique) | Investigation | Thread Sensitivity +5 at character creation (additive, before any other modifiers). Your exposure to the Calamity's ambient effects since birth has primed your configuration. You are not a practitioner — but you are closer to the threshold than most people will ever be. |
| **Calamity Familiarity** § | Investigation | In territories at node distance 0–2 from Askeheim: +1D on Attunement rolls. The wound is your neighbourhood. |
| **Cultural Memory** § | Debate / Investigation | +1D when engaging with pre-Calamity history, Einhir artefacts, or folk practice. The knowledge comes as recognition — you feel the rightness of things you cannot intellectually justify. |

**Narrative experiential impact:** You carry an inheritance that has been half-erased. Scenes involving Einhir cultural recovery, the Forgetting's effects, or encounters with Thread phenomena resonate differently for you than for characters from the north — not because you understand more, but because you feel more. The Restoration Movement's appeal is personal, not political: they are trying to recover what your family lost. Your relationship to the Church is complicated at best — they are the institution that declared your ancestors' practices heretical and spent 245 years ensuring they could not be remembered.

---

### 1E. Himmelenger Child (Church Territory)
Born and raised in Himmelenger — the Cathedral city, the Church's seat of power, the theological centre of Valoria. Your world is bells, scripture, liturgy, and the towering architecture of institutional faith.

**Who raised you:** A family within the Church's cultural orbit — not necessarily clergy, but people whose lives are structured by the Church's rhythms. Himmelenger is not just a city with a cathedral; it is a city that IS a cathedral. Every institution, every school, every market operates under the Church's moral framework.

**Starting Certainty:** 5 (Orthodox). You were raised in the heart of Solmund's institutional presence. The Church's account of reality is not something you were taught — it is the air you breathed.

**Suggested Knot:** A childhood mentor within the Church — a parish teacher, a seminary instructor, a family confessor. They represent the certainty you grew up inside. Whether that certainty holds or cracks defines your arc.

| Skill | Domain | Effect |
|---|---|---|
| **Cathedral Raised** (unique) | Debate | In Church Tribunal or any proceeding in Church-held territory: +1D to both Appraise and Argue rolls. You know the rituals, the architecture, the rhythms of ecclesiastical authority. This is your house. |
| **Doctrinal Fluency** § | Debate / Investigation | When engaging with Solmund theology, Church history, or liturgical practice: +1D. You absorbed this before you could read. |
| **Institutional Gravity** § | Faction Play | When performing Domain Actions on Church's behalf: strain from failed actions reduced by 1 (minimum 0). The institution absorbs shocks that would break individuals. |

**Narrative experiential impact:** Himmelenger shapes you the way a mould shapes metal — totally, invisibly, from the inside. You do not experience the Church as an institution you belong to; you experience it as the way the world IS. Scenes that challenge this — encounters with Thread truth, practitioners, the Southernmost, or the Restoration Movement — are not intellectual disagreements. They are existential crises. Your Certainty of 5 means the first Coherence loss is nullified by doctrine scaffolding (per params_core), but it also means that when doctrine finally cracks, the fall is further.

---

### 1F. Urban Underclass (Valorsplatz)
Born in the capital's lowest districts. Raised in poverty, in the gap between the Crown's proclaimed justice and its actual reach.

**Who raised you:** A single parent, an extended family of working poor, or effectively no one. The capital's wealth flows through your neighbourhood without stopping. The Crown magistrates' justice does not extend to your street. The Church's charity arrives as condescension. You learned to survive before you learned to read — if you learned to read at all.

**Starting Certainty:** 3–4 (Questioning to Average). The Church is present as charity and judgment; the Crown is present as law enforcement that protects property, not people. Neither institution has earned your faith.

**Suggested Knot:** A childhood friend, a gang member, a street mentor — someone who taught you how to survive the capital's indifference. They may be dead, imprisoned, or still scraping by. They are the person who kept you alive.

| Skill | Domain | Effect |
|---|---|---|
| **Street Sense** (unique) | Investigation | In any urban environment: +1D on Attunement rolls to detect danger, assess intentions, or identify escape routes. You learned to read people for survival. |
| **Scrapper** § | Scene Battle | Unarmed/improvised weapons: TN 7 instead of TN 8. The street teaches fighting without weapons. |
| **Invisible** § | Investigation | When attempting to avoid notice in urban crowds or poor districts: +1D on Agility-based concealment rolls. You know how to be no one. |

**Narrative experiential impact:** You know the capital that the Crown Court pretends does not exist. Scenes involving poverty, urban survival, or the gap between institutional rhetoric and lived reality are viscerally personal. You understand the Restoration Movement's appeal because you are the population they claim to serve. In political scenes, you bring the perspective that everyone else is arguing about — and you know that whatever they decide, it will arrive in your old neighbourhood last.

---

### 1G. Border Settlement Child
Born in one of the northern border territories — Lowenskyst, Spartfell, or Halvarshelm. Raised in the shadow of the Altonian mountains, in communities that exist because a fortress needs people to supply it.

**Who raised you:** A military family or a family that serves the military — blacksmiths, provisioners, innkeepers, farriers. The border is not a metaphor here; it is a physical presence. You grew up watching the mountain passes and learning, from the adults around you, that something will eventually come through them.

**Starting Certainty:** 4 (Average Valorian). The Church and Crown are both present; what dominates is the military reality.

**Suggested Knot:** A garrison soldier, a frontier officer, or a parent who served at the border. They represent the watchfulness that defined your childhood — the specific anxiety of people who live where the threat is geographic.

| Skill | Domain | Effect |
|---|---|---|
| **Border Vigilance** (unique) | Mass Battle / Investigation | Before any engagement or encounter in border territories: +1D on Cognition rolls to detect ambush, assess enemy strength, or identify terrain advantage. You grew up scanning the horizon. |
| **Cold Endurance** § | Scene Battle | No environmental penalty in cold/winter conditions. |
| **Frontier Self-Reliance** § | Investigation / Scene Battle | When no allied faction reinforcements are available (GM confirms): +1D to one roll per scene. The border teaches you that help is days away. |

**Narrative experiential impact:** You were raised at the edge. Scenes involving Altonian threats, border defence, or military preparation are your native environment. You understand the Institutional Pressure clock viscerally — it measures something your family has watched for your entire life. When Altonia finally moves, you will not be surprised. You will be the person who says "I told you so" — if you survive long enough.

---

### 1H. Itinerant / Orphan
Born somewhere. Raised everywhere — or nowhere. Your family was destroyed, displaced, or simply absent. You grew up on the road, in institutions, or in the care of strangers.

**Who raised you:** No one consistent. A series of foster situations, workhouses, charitable institutions, or road families. You learned the peninsula's geography by being moved across it. You have no hometown, no regional accent, no inherited cultural assumptions — or you have all of them, in fragments, none deep enough to call your own.

**Starting Certainty:** 3 (Questioning). No institution has claimed you thoroughly enough to imprint its worldview. You evaluate the Church, the Crown, and every other authority from the outside.

**Suggested Knot:** Another itinerant — a fellow orphan, a traveling companion, a stranger who showed you unexpected kindness during a period when no one else did. They are the person who proved that connection is possible even for someone with no roots.

| Skill | Domain | Effect |
|---|---|---|
| **Nowhere and Everywhere** (unique) | Investigation / Faction Play | No ethical framework modifier applies to you personally when performing Domain Actions — you carry no institutional alignment that could be read as aligned or contradictory. The world has no assumptions about what you should do. |
| **Quick Study** § | Scene Battle / Debate / Investigation | Once per session: declare expertise in a skill you have observed someone else use this session. +1D to one roll using that skill. You learn by watching because no one taught you formally. |
| **Survivor's Instinct** § | Scene Battle | When at half or fewer Health: +1D to Defence. You have been hurt before. You know how to protect what is left. |

**Narrative experiential impact:** You have no hometown scene that feels like homecoming. Every place is equally foreign and equally familiar. Scenes involving identity, belonging, or institutional loyalty create tension because you are the character who has no default answer to "where are you from?" This is both freedom and loss. You can serve any faction without betraying an origin — but you can also be discarded by any faction without anyone noticing.

---

## STAGE 2: FORMATION — How were you educated or shaped?

Formation covers the years between childhood and professional training. It determines the character's intellectual framework, their first encounter with institutional power, and the relationships formed during the period when they were being shaped by forces larger than themselves.

**Formation grants 1 starting skill** (the first skill listed for each Formation). Remaining skills are on the spark list — acquired through scene use.

---

### 2A. Church Schooling
Educated through the Church's school system — the only widespread education infrastructure on the peninsula. Literacy, numeracy, scripture, Solmund history.

**What you learned:** Reading, writing, arithmetic, theology. The Church's educational apparatus is comprehensive and effective. It also embeds a specific worldview: Solmund doctrine, the Church's historical narrative, the moral framework that positions Thread phenomena as heretical. You know how to think — within the categories the Church provides.

**Certainty modifier:** +1 if starting Certainty was below 5 (education reinforces doctrine). Church schooling is the most powerful socialisation tool the Church possesses.

**Suggested Knot:** A school mentor (priest, teacher, librarian) who invested in you personally. They may have been kind, cruel, inspiring, or stifling — but they shaped your intellectual development. Whether you now agree with what they taught defines a live tension.

| Skill | Domain | Effect |
|---|---|---|
| **Literate** (unique — most Valorians are not) | Investigation / Debate / Faction Play | Can read and write. +1D on all rolls involving documents, correspondence, or written records. In a mostly oral society, literacy is power. |
| **Doctrinal Fluency** § | Debate / Investigation | +1D on Solmund theology, Church history, liturgical practice. |
| **Trained Memory** § | Debate | Concentration (Focus + Recall) +2 in social contests. Church education drills retention. |

**Narrative experiential impact:** The Church educated you, which means the Church shaped the categories you think in. Scenes involving intellectual argument, historical analysis, or theological debate are where your Formation pays off. But every piece of Thread truth you encounter will be processed first through the framework the Church gave you — and the tension between what you were taught and what you discover is the engine of character development for anyone who passed through this Formation.

---

### 2B. Ducal Household Education
Educated as part of a noble or ducal household's retinue — Crown, Hafenmark, or Varfell. Tutored alongside the children of the powerful. Exposed to political reality from a young age.

**What you learned:** Courtly protocol, political history, languages, basic military training, and the specific worldview of the household that educated you. Crown households emphasise duty and virtuous governance. Hafenmark households emphasise law and procedure. Varfell households emphasise pragmatism and information advantage.

**Certainty modifier:** None (ducal education does not emphasise theology — it emphasises power).

**Suggested Knot:** A fellow student — a child of the household, another retainer's child, someone your own age who shared your Formation. You may now serve the same faction or opposing ones. The bond was formed before politics intervened.

| Skill | Domain | Effect |
|---|---|---|
| **Political Literacy** (unique) | Debate / Faction Play | +1D on Appraise rolls in any political context (Parliament, court, faction negotiation). You grew up watching power operate — you recognise its patterns instinctively. |
| **Courtly Bearing** § | Debate | In Formal or Grand Contests: immune to the first exchange of strain. You were trained to maintain composure under social pressure. |
| **Patron's Connections** § | Faction Play | +1D on one Domain Action per season when acting within the faction system of the household that educated you. Their network is partially yours. |

**Narrative experiential impact:** You were educated by power. You know how factions think because you grew up inside one. Scenes involving factional politics, court intrigue, or inter-household negotiation are where your Formation is most visible. You carry the worldview of the household that shaped you — Crown virtue ethics, Hafenmark proceduralism, or Varfell consequentialism — as an inherited intellectual framework that you may not have consciously chosen.

---

### 2C. Guild Apprenticeship
Educated through the Guild system — apprenticed to a master, trained in a specific craft, and socialised into the Guilds' pluralistic economic worldview.

**What you learned:** A trade (metalwork, textiles, shipbuilding, brewing, whatever), guild law, commercial arithmetic, and the Guilds' specific moral framework: value is determined by skill, not birth or doctrine. You also learned to argue about money, because that is what guild apprentices do.

**Certainty modifier:** −1 if starting Certainty was 5 (Guild culture is secular; prolonged immersion loosens orthodoxy).

**Suggested Knot:** Your master craftsperson — the person who taught you your trade. They represent professional standards, craft values, and the specific relationship between someone who knows and someone who is learning. Whether they were kind or demanding, the relationship was the most formative of your adolescence.

| Skill | Domain | Effect |
|---|---|---|
| **Craft Expertise** (unique) | Investigation / Faction Play | +2D on any roll involving your specific craft (declared at character creation). Applies to creation, assessment, repair, or identification of craft-related objects and processes. |
| **Economic Reasoning** § | Debate | In any argument involving economic stakes: +1D to Argue pool. You were trained to think in terms of value, cost, and exchange. |
| **Guild Network** § | Faction Play / Investigation | +1D on information-gathering or Domain Actions when interacting with Guild faction members or in territories with high Guild Favour. |

**Narrative experiential impact:** The Guild system taught you that the world runs on skill and trade, not theology or birthright. Scenes involving commerce, craftsmanship, or economic competition are your ground. You evaluate every institution by a practical standard: does it produce anything? The Church produces doctrine; the Crown produces order; the Guilds produce goods. You know which of these you can hold in your hands.

---

### 2D. Self-Taught / Street Education
No formal education. You learned by necessity — observation, imitation, trial and error, and the harsh pedagogy of consequences.

**What you learned:** Whatever you needed to survive. Maybe literacy (scraps, signs, stolen books). Maybe numeracy (counting money, assessing risk). Maybe nothing formal at all — just the deep practical intelligence of someone who has navigated the world without institutional support.

**Certainty modifier:** −1 if starting Certainty was 5 (without institutional education, orthodoxy has no reinforcement structure).

**Suggested Knot:** A street teacher — a criminal, a beggar, a merchant, a wanderer — who taught you something useful at a critical moment. Not a formal mentor; a person who passed through your life and left you with a skill, a warning, or a way of seeing the world that stuck.

| Skill | Domain | Effect |
|---|---|---|
| **Autodidact** (unique) | Any domain | Once per arc: declare that you have self-taught a relevant skill during downtime. +1D on rolls using that skill for the remainder of the arc. You learn by doing, not by instruction. |
| **Street Wisdom** § | Investigation | In urban environments: +1D on Attunement rolls to detect danger or assess intentions. |
| **Hard to Fool** § | Debate | When an opponent uses Obscuring orientation against you: their Doubt Marker effect is reduced by 1 (minimum 0). You have been lied to by experts. |

**Narrative experiential impact:** Nobody taught you — or rather, everyone and everything taught you, in fragments, without coherence. Scenes involving formal education, institutional authority, or expert knowledge create tension because you are aware of what you do not know. But scenes involving practical problem-solving, rapid adaptation, or situations where institutional knowledge fails are where you shine. You are the character who solves problems that educated people cannot solve because educated people cannot see them.

---

### 2E. Military Training
Educated through military service — Crown army, Hafenmark ducal guard, Varfell household troops, or Löwenritter squire training. Your Formation was physical, disciplined, and hierarchical.

**What you learned:** Weapons, formations, chain of command, physical endurance, and the specific military culture of the institution that trained you. Crown training emphasises honour and formation. Hafenmark training emphasises defence and fortification. Varfell training emphasises adaptability and terrain exploitation. Löwenritter training emphasises discipline and operational excellence.

**Certainty modifier:** None (military training does not engage with theology directly).

**Suggested Knot:** A training partner, a drill instructor, or a fellow recruit. The bonds formed under shared physical hardship are among the strongest in the game. This person knows what you can endure because they endured it beside you.

| Skill | Domain | Effect |
|---|---|---|
| **Weapons Training** (unique) | Scene Battle | Choose one weapon type at character creation (from the weapon TN matrix). With that weapon: TN −1 (minimum TN 5). You were trained with this weapon specifically, repeatedly, until it became reflex. |
| **Formation Instinct** § | Mass Battle | Unit containing this character: +1 Discipline starting value (max 7). |
| **Physical Conditioning** § | Scene Battle | Stamina base +1 (stacks with formula). |

**Narrative experiential impact:** Your body was shaped before your mind was. Scenes involving combat, military operations, or physical challenge are where your Formation is most visible. You carry the posture, the instincts, and the vocabulary of the institution that trained you — and you assess every situation for threat before you assess it for anything else. Whether this hypervigilance serves you or limits you depends on what the campaign demands.

---

### 2F. Practitioner Mentorship
Educated by a Thread practitioner — a warden, a solitary practitioner, or a member of one of the peninsula's scattered practitioner communities. Your Formation is the philosophical and practical preparation for Thread practice.

**What you learned:** Approach training, the philosophical framework for understanding rendering and Thread, the discipline of Focus and Attunement, and the specific traditions of your mentor's practice. You may not have Leaped yet — Formation is preparation, not achievement.

**Certainty modifier:** −2 (minimum 0). Practitioner education systematically dismantles the Solmund cosmology. Not through argument — through experience. Your mentor showed you things that the Church's framework cannot contain.

**Suggested Knot:** Your practitioner mentor. This is one of the deepest Knots in the game. They did not just teach you — they showed you what lies beneath rendering. They trusted you with knowledge that the Church would burn you for possessing. Whether they are still alive, still practicing, or still sane defines a major axis of your character arc.

| Skill | Domain | Effect |
|---|---|---|
| **Approach Training** (unique) | Scene Battle (Thread) | Leap roll: +1D. You were trained specifically for the surrender of rendering. This bonus stacks with other Leap pool elements. |
| **Thread Perception** § | Investigation | When Thread Sensitivity ≥ 30: +1D on Attunement rolls to perceive Thread phenomena. |
| **Philosophical Grounding** § | Debate | When arguing about ontology, Thread reality, or the nature of rendering: +1D. You have a framework for what you have experienced. |

**Narrative experiential impact:** Your mentor changed you. Not politically, not intellectually — ontologically. Scenes involving Thread operations, Southernmost expeditions, or encounters with threadcut beings carry specific weight because you were prepared for them in ways that other characters were not. But your preparation also isolated you: the knowledge your mentor gave you cannot be shared with non-practitioners (the Forgetting ensures this), which means you carry a worldview that is functionally incommunicable to most of the people you interact with. This loneliness is part of the practice.

---

### 2G. Monastic Seclusion
Educated in a monastery or isolated Church community — not the urban seminary of Himmelenger, but a remote contemplative house. Your Formation was quiet, rigorous, and divorced from political reality.

**What you learned:** Deep theological knowledge, liturgical practice, contemplative discipline, and the specific worldview of people who have chosen to step outside the world's political contests. Monasteries produce scholars, archivists, and — occasionally — people who have spent so long in silence that they have heard things the urban Church drowns out.

**Certainty modifier:** +1 or −1 (GM's choice during character creation). Monastic seclusion either deepens faith (the contemplative tradition as Solmund's deepest truth) or cracks it (silence reveals questions that doctrine cannot answer). The player does not choose — the GM presents which happened, and the character lives with it.

**Suggested Knot:** A fellow monk, a contemplative, or an abbot/abbess who presided over your Formation. They represent the specific quality of attention that monastic life produces — and the question of whether that attention reveals truth or illusion.

| Skill | Domain | Effect |
|---|---|---|
| **Contemplative Focus** (unique) | Debate / Scene Battle (Thread) | Focus +1 for Contact Duration calculation (does not increase the attribute for other purposes). Years of contemplative discipline taught you to hold rendering at bay slightly longer than your natural Focus would permit. |
| **Archive Access** § | Investigation | +1D on Recall-based rolls when researching documents or historical records. Monasteries have libraries. |
| **Silence Reader** § | Investigation / Debate | Appraise rolls in one-on-one or small-group settings: TN 6 instead of TN 7. You learned to read people in a community where no one spoke. |

**Narrative experiential impact:** The monastery was a world apart. You re-entered a world of politics, violence, and factional competition without the socialisation that other characters received. Scenes involving quiet contemplation, archival research, or theological depth are where you thrive. Scenes involving political maneuvering, urban chaos, or rapid social adaptation are where you struggle. You are the character who pauses before speaking — not from uncertainty, but from a trained habit of attention that the world outside the monastery rarely rewards.

---

## STAGE 3: VOCATION — What were you trained to do?

Vocation is the professional History — the occupation, the factional role, the set of skills that the character uses to operate in the world. This is the closest analog to the occupational Histories in the prior version of this document.

**Vocation determines faction affiliation** (primary or secondary). A character may serve a faction without Vocation aligning — a Crown Heartland Child (1A) with Practitioner Mentorship (2F) and a Church Vocation (3-Church) creates a character who was raised Crown, trained Thread, and works for the Church. The contradictions are the character.

**Vocation grants 2 starting skills** (the first two skills listed for each Vocation). Remaining skills are on the spark list.

---

I am structuring the Vocations by faction. **Each Vocation entry below follows the same format as the Origins and Formations above, with three skills, a suggested Knot, and narrative experiential impact.** For brevity in this proposal, I present the Vocations as a **summary table with skills**, with full narrative write-ups deferred to the next design pass after editorial approval of the four-stage structure.

### Crown Vocations

| Vocation | Skills | Suggested Knot |
|---|---|---|
| **3-CR1: Court Official** | Courtly Grace (unique: +1D Argue before Expert Judge in Crown territory), Read the Room § (Appraise TN 6 in formal settings), Institutional Memory § (+1D to relevant Unique Action) | A rival official — someone who competes for the same patron's attention. Respect and resentment in equal measure. |
| **3-CR2: Crown Soldier** | Riposte § (2 Defence dice as counter-Strike at +1 TN), Formation Discipline § (+1 Discipline start), Garrison Eyes (unique: +1D detect infiltration in posted location) | A squad-mate — the person who stood beside you in formation. You trust them with your life but may not know their politics. |
| **3-CR3: River Trader** | Schoenland Contacts § (+1D Domain Actions involving Schoenland), Haggler's Nerve § (−1 strain in private negotiation), Cargo Sense § (+1D detect forged/smuggled goods) | A Schoenland trading partner — someone across the water who represents both commerce and the foreign perspective. |
| **3-CR4: Crown Magistrate** | Procedural Objection § (force Regroup or +1 Ob once per contest), Paper Trail § (+1D institutional records research), Tax Assessment (unique: +1D on Wealth-targeting DA) | A mentor judge — the magistrate who trained you and whose standards you carry (or reject). |

### Church Vocations

| Vocation | Skills | Suggested Knot |
|---|---|---|
| **3-CH1: Seminary Graduate** | Doctrinal Authority (unique: +3D Recall bonus in Memory genre on theology), Liturgical Composure § (+2 Composure in Church Tribunal), Theological Insight § (+1D analysing theological content) | A seminary rival — someone who argued better than you, or worse, and whose theological positions are the mirror of yours. |
| **3-CH2: Templar** | Smite the Heretic (unique: +1D Offence vs declared heretic/practitioner in Thread ops), Shield of Faith § (+1D Defence in Full Guard), Righteous Conviction § (immune to Doubt Markers in Church Tribunal) | A fellow Templar — the person you trained with, prayed with, and will fight beside. The order's bonds are designed to be absolute. |
| **3-CH3: Parish Priest** | Sermon Delivery (unique: +1 Conviction Track on Revealing win before Crowd), Folk Trust § (−1 Ob on DA involving common population where Church Mandate ≥ 4), Road Survival § (+1D Endurance in unfamiliar territory) | A parishioner — a common person who trusts you personally, not institutionally. They represent what the Church is supposed to be, as distinct from what it is. |
| **3-CH4: Church Archivist** | Forbidden Knowledge (unique: once/arc, suppressed document recall), Paper Trail §, Doctrinal Inconsistency (unique: +1D arguing against Church position in Memory genre) | A fellow archivist who discovered the same suppressed material — and chose differently about what to do with it. |

### Hafenmark Vocations

| Vocation | Skills | Suggested Knot |
|---|---|---|
| **3-HA1: Parliamentary Aide** | Constitutional Precedent (unique: −1 Audience Resistance when citing constitutional clause), Procedural Objection §, Institutional Memory § | A political opponent within the parliamentary system — someone you disagree with on policy but respect for their procedural integrity. |
| **3-HA2: Highland Miner** | Tunnel Fighter (unique: +1D Defence in confined spaces), Stone Reader (unique: +1D assess terrain/fortifications), Stubborn Endurance § (first wound penalty negated) | A mine-shaft partner — the person whose life depended on your attention, and vice versa. Underground bonds are absolute. |
| **3-HA3: Border Guard (Spartfell)** | Fortress Defender (unique: +1D Defence in Fortified positions), Know the Enemy § (+1D identify Altonian forces), Cold Iron § (no cold weather penalty) | A fellow border guard — someone who watches the mountains with you. You share the specific anxiety of people who live where the threat arrives first. |
| **3-HA4: Highland Guide** | Mountain Ambush (unique: −1 Ob one tactic/battle in highland terrain), Sure-Footed § (auto-success Establish Distance in difficult terrain), Weatherwise § (Cognition roll to learn one environmental modifier) | A client you guided through dangerous terrain — someone whose survival created an obligation that became a friendship. |

### Varfell Vocations

| Vocation | Skills | Suggested Knot |
|---|---|---|
| **3-VA1: Intelligence Operative** | Dead Drop (unique: establish covert channel, −1 Ob Intel ops), Smooth Liar § (−1 strain when using Obscuring), Shadow Work § (+1D surveillance/counter-intel) | A handler — the person who gives you orders and evaluates your results. Trust is professional, not personal — which makes it more fragile. |
| **3-VA2: Fjord Sailor** | Sea Legs § (+1D Defence on water), Coastal Navigation (unique: +1D navigation/recon on western coast), Community Voice § (+1D Argue before Crowd for common people) | A captain — the person who commands the ship you serve on. Maritime bonds are forged by shared danger and shared boredom. |
| **3-VA3: Einhir Antiquarian** | Artefact Authentication (unique: +2D assess Einhir objects), Black Market Contacts § (+1D underground networks), Einhir Lore § (+1D pre-Calamity knowledge) | A collector or dealer — someone who shares your obsession with the Einhir past but whose ethics regarding acquisition may differ from yours. |
| **3-VA4: Ducal Retainer** | Vaynard's Confidence (unique: Spirit roll for +1D Thread-related roll when Private Collection used), Read the Room §, Household Authority § (−1 Ob DA in Varfell territories) | A fellow retainer — someone who has noticed the same things you have about the Duke's private interests, and whose silence you rely on. |

### Guild Vocations

| Vocation | Skills | Suggested Knot |
|---|---|---|
| **3-GU1: Guild Factor** | Cross-Border Immunity (unique: −1 ethical framework Ob in foreign territory), Haggler's Nerve §, Cargo Sense § | A business rival who is also a friend — someone you compete with economically and drink with personally. |
| **3-GU2: Guild Enforcer** | Back-Alley Fighter (unique: +1D Stunt in urban environments), Intimidation § (+1D Obscuring in private negotiation/interrogation), Smooth Liar § | A debtor you chose not to collect from — someone whose vulnerability became your conscience. |
| **3-GU3: Master Craftsperson** | Master Craftwork § (once/season craft +1 item), Guild Kinship § (+1D Influence DA with Guilds), Precision Hands § (+1D examining crafted objects) | A journeyman you trained — someone who learned from you and now carries your professional legacy. |

### Niflhel Vocations

| Vocation | Skills | Suggested Knot |
|---|---|---|
| **3-NI1: Dockworker (Niflhel arm)** | Hidden Cargo (unique: −1 Ob smuggling), Scrapper § (unarmed TN 7), Shadow Work § | A fellow dockworker who does not know the full extent of what you move — or who knows and pretends not to. |
| **3-NI2: Quiet Operative** | Silent Kill (unique: +3 flat damage vs unaware target), Vanish (unique: Agility TN 7 Ob 2 to leave zone untracked), Dead Drop § | A former target you did not kill — someone whose life you hold like a debt that can never be repaid. |
| **3-NI3: Reckoner** | Pressure Point (unique: +2D on one roll when financial vulnerability identified), Intimidation §, Urban Navigation § (+1D escape/evasion in urban) | A debtor who became a source — someone whose financial vulnerability you exploited and who now provides information because the alternative is worse. |
| **3-NI4: Fence** | Appraisal (unique: +2D assess value/authenticity any object), Black Market Contacts §, Haggler's Nerve § | A regular buyer — someone whose taste you know and whose discretion you trust. The relationship is transactional but durable. |

### Restoration Movement Vocations

| Vocation | Skills | Suggested Knot |
|---|---|---|
| **3-RE1: Pamphleteer** | Incendiary Rhetoric (unique: +2D Argue before Crowd, Revealing, social justice topics), Underground Distribution (unique: −1 Ob on Restoration DA), Community Voice § | A printer or distributor — someone whose physical safety depends on your discretion. |
| **3-RE2: Community Organiser** | Solidarity (unique: +1D Community Weaving when acting as agent), Community Voice §, Folk Trust § | A community leader you radicalised — or who radicalised you. The relationship is political and personal simultaneously. |
| **3-RE3: Folk Practitioner** | Intuitive Threadwork (unique: Attunement + Spirit TN 8 Ob 3 for minor Weaving, pre-Leap), Folk Healer (unique: +1D Medicine), Einhir Lore § | Your grandmother (or grandmother-equivalent) — the person who taught you the old ways. They may be dead. The practices they gave you are alive in your hands. |

### Löwenritter Vocations

| Vocation | Skills | Suggested Knot |
|---|---|---|
| **3-LO1: Löwenritter Knight** | Elite Discipline (unique: unit Discipline floor 2), Riposte §, Formation Discipline § | A brother/sister knight — the person you trained with and whose loyalty to the Order matches yours. If the Coup Counter reaches 3, you will face each other's choices. |
| **3-LO2: Border Ranger** | Eagle Eyes (unique: Cognition roll to reveal one element of opposing Phase 1), Know the Enemy §, Cold Iron § | A patrol partner — someone who shares the mountain watch. You have spent more time with this person in silence than most people spend with their families in conversation. |
| **3-LO3: Riskbreaker** | Deniable Action (unique: Spirit roll to deflect evidence trail), Silent Kill §, Smooth Liar § | A handler within the Order — someone who gives you missions and who is the only person alive who knows what you have done. This Knot is a secret. |

### Cross-Factional Vocations

| Vocation | Skills | Suggested Knot |
|---|---|---|
| **3-CF1: Mercenary** | Weapon Versatility (unique: switch weapon type between exchanges at no cost), Riposte §, Eagle Eyes § | A former employer — someone who hired you, whose cause you served, and whose money you took without moral commitment. |
| **3-CF2: Wandering Healer** | Field Medicine (unique: −1 Ob stabilise), Folk Healer §, Road Survival § | A patient whose life you saved — someone who exists because of your skill and who remembers it. |
| **3-CF3: Traveling Merchant** | Wide Network (unique: +1D in up to 3 previously-operated territories), Haggler's Nerve §, Road Survival § | A long-route trading partner — someone you see once a season and trust absolutely within the bounds of commerce. |
| **3-CF4: Scribe** | Textual Memory (unique: recall previously-handled documents), Paper Trail §, Forgery Detection (unique: +2D authenticate documents) | An author whose work you copied — someone whose ideas you know better than your own because you transcribed every word. |

---

## STAGE 4: CATALYST — What happened that put you on this path?

The Catalyst is not an occupation — it is an event. It explains why the character is here, now, at the start of the campaign, rather than continuing their ordinary life. Every Catalyst produces a **starting Belief** (the player writes the specific text; the Catalyst provides the shape) and a **campaign hook** (the GM uses this to connect the character to the campaign's opening situation).

**Catalyst grants 0 starting skills.** All skills listed are on the spark list — acquired through scene use. Catalyst skills represent abilities forged by the event, which must be practised to become reliable.

---

### 4A. Witnessed Something Impossible
You saw a Thread phenomenon — a Shifting Object, a Gap, a rendering failure, a threadcut being. Your rendering cracked. The Church's account of reality failed to contain what you experienced.

**Certainty modifier:** −1 (minimum 0).
**Starting Belief shape:** "The world is not what [my institution/my faith/common sense] says it is — I must [investigate/understand/warn others/find someone who knows]."
**Campaign hook:** The GM specifies what you witnessed and where. This connects you to the campaign's Thread-related plotlines.

| Skill | Domain | Effect |
|---|---|---|
| **Shaken Certainty** (unique) | Investigation / Debate | When confronting Thread phenomena: no Composure loss, no surprise round penalty. You have already had this shock. Additionally: Certainty track movement toward 0 costs 1 less from Discovery Events (you are already primed). |
| **Shifting Object Recognition** § | Investigation | Automatic recognition. |
| **Obsessive Recall** (unique) | Investigation | +1D on Recall rolls pertaining to the specific event you witnessed. Your memory of it is unnaturally sharp — the Forgetting has not fully taken hold, which itself is significant. |

---

### 4B. Betrayed by Your Institution
The faction or institution you served failed you — unjust punishment, broken promise, scapegoating, deliberate cruelty. You left or were expelled. You carry knowledge your former institution wishes you did not have.

**Certainty modifier:** −1 if betraying institution was the Church. No change otherwise.
**Starting Belief shape:** "I will never trust [institution] again — and I will [expose their corruption/build something better/survive without them/make them pay]."
**Campaign hook:** The GM specifies the betrayal. The betraying institution becomes a recurring antagonist or complication.

| Skill | Domain | Effect |
|---|---|---|
| **Insider Knowledge** (unique) | Investigation / Faction Play | +2D on Investigation rolls targeting your former faction. You know where the bodies are buried. |
| **Bitter Resilience** § | Debate | Immune to first Rattled mark per session. |
| **Burned Bridge** (unique) | Faction Play | When your former faction performs a Domain Action that you oppose: +1D on your counter-action. Betrayal is a powerful motivator. |

---

### 4C. Lost Someone
A Close Knot died, disappeared, or was taken. The loss is the engine of your action. You are looking for them, avenging them, or carrying what they left behind.

**Certainty modifier:** None (loss does not change cosmology — it changes purpose).
**Starting Belief shape:** "I will [find them/avenge them/complete their work/protect what they loved] — nothing else matters until this is done."
**Campaign hook:** The GM specifies who was lost and the circumstances. The lost Knot is a campaign thread.

| Skill | Domain | Effect |
|---|---|---|
| **Grief-Driven Focus** (unique) | Any domain | Once per session, when pursuing an action directly related to the lost Knot: +2D. The grief is a resource — it burns clean when it has direction. |
| **Knot Memory** (unique) | Debate / Investigation | +1D on rolls when you invoke the lost person's knowledge, skills, or connections. You carry them with you. |
| **Hollow Endurance** § | Scene Battle | When at 1+ Wounds: first wound penalty negated. You have survived worse than any physical injury. |

---

### 4D. Recruited
Someone sought you out. A faction, a practitioner, a Knot — someone identified you as useful, dangerous, or necessary, and brought you into something larger than your ordinary life.

**Certainty modifier:** Depends on recruiter (GM determines).
**Starting Belief shape:** "[Recruiter] believes I can [do something specific] — I will prove them [right/wrong/show them something they did not expect]."
**Campaign hook:** The recruiter is a named NPC with faction affiliation. The recruitment connects to the campaign's opening situation.

| Skill | Domain | Effect |
|---|---|---|
| **New Allegiance** (unique) | Faction Play | +1D on your first Domain Action per season on behalf of the recruiting faction. You are trying to prove yourself. |
| **Quick Adaptation** § | Any domain | Once per session: +1D on a roll in a domain you have no other skill bonuses for. You are learning the new world as fast as you can. |
| **Recruiter's Trust** (unique) | Investigation | +1D on Investigation rolls when pursuing the recruiter's objectives. They showed you what to look for. |

---

### 4E. The First Leap
You attempted the Leap — and succeeded. Your rendering suspended. You experienced what lies beneath consciousness. You returned changed. This Catalyst is only available if Formation included Practitioner Mentorship (2F) or the character has TS ≥ 30 from other sources.

**Certainty modifier:** −1 (permanent, per threadwork_v25 §2.3 First Leap rules).
**Starting Belief shape:** "I have been outside rendering. The world is [not what it seems/more fragile than anyone knows/beautiful in ways language cannot reach] — I must [continue the practice/find the others/fix what is broken]."
**Campaign hook:** The GM specifies where the First Leap occurred and what the character perceived during contact. This perception shapes the character's relationship to Thread practice for the entire campaign.

| Skill | Domain | Effect |
|---|---|---|
| **Post-Leap Clarity** (unique) | Investigation | Thread Perception: +2D on Attunement rolls to perceive Thread phenomena (stacks with Thread Perception §). The First Leap permanently sharpened your configurational sensitivity. |
| **Rendering Memory** (unique) | Debate | When arguing about Thread reality or ontological questions: immune to Doubt Markers. You are not theorising — you are reporting. The Doubt Marker assumes the doubt can be planted; for someone who has been outside rendering, it cannot. |
| **Leap Scar** (unique) | Scene Battle (Thread) | First Leap in each session: −1 Ob (minimum 1). The initial surrender is easier now — your rendering has already learned to let go once. |

---

### 4F. War / Invasion
Altonian forces crossed the border, or a factional conflict erupted into open warfare. You survived. Your ordinary life did not.

**Certainty modifier:** None.
**Starting Belief shape:** "War took [what I had/who I was/where I lived] — I will [never let it happen again/fight until there is nothing left to fight for/build something worth defending]."
**Campaign hook:** The GM specifies which war and which theatre. This connects the character to the Institutional Pressure clock and Altonian plotlines.

| Skill | Domain | Effect |
|---|---|---|
| **Veteran's Eye** (unique) | Mass Battle | +1D on Command tactic rolls. You have seen what works and what does not — not from training but from survival. |
| **Combat Reflexes** § | Scene Battle | Initiative advantage: if Attunement is tied, you act last (information advantage) regardless of Agility tiebreaker. Your reflexes were forged under fire. |
| **War Hardened** (unique) | Debate / Scene Battle | Immune to Morale-related penalties in mass battle and to Composure loss from witnessing violence in social scenes. You have already seen the worst. |

---

### 4G. Religious Crisis
Your faith broke — or deepened — in a way that cannot be undone. Not intellectual doubt but experiential crisis: a miracle that was not miraculous, a prayer that was answered in a way the Church cannot explain, a moment of confrontation with something the doctrine does not cover.

**Certainty modifier:** −2 or +2 (player chooses direction at character creation). The crisis moves you toward Thread acceptance (−2) or deeper orthodoxy (+2). Either way, the comfortable middle ground of Average Valorian certainty is no longer available to you.

**Starting Belief shape:** "The Church is [wrong about what matters most/the only institution standing between us and the abyss] — I will [find the truth they are hiding/defend the faith against those who would destroy it]."
**Campaign hook:** The GM specifies the nature of the crisis. It connects to the Theocracy Counter and Church plotlines.

| Skill | Domain | Effect |
|---|---|---|
| **Crisis-Forged Conviction** (unique) | Debate | +1D to Argue pool when arguing for or against Church doctrine. The crisis destroyed your indifference — you now argue with the force of someone who has been personally tested. |
| **Theological Depth** § | Investigation | +1D on rolls involving Church doctrine, theology, or institutional structure. The crisis forced you to study what you previously took for granted. |
| **Unshakeable** (unique) | Debate | Composure +3 in any context where your specific religious position is under attack. The crisis already did the damage — no debate can shake what the crisis did not destroy. |

---

## Character Creation Summary

1. **Choose Origin** (Stage 1) → establishes geography, culture, starting Certainty, first Knot. 0 starting skills.
2. **Choose Formation** (Stage 2) → establishes intellectual framework, Certainty modifier, second Knot. 1 starting skill.
3. **Choose Vocation** (Stage 3) → establishes profession, faction affiliation, third Knot. 2 starting skills.
4. **Choose Catalyst** (Stage 4) → establishes inciting event, starting Belief, campaign hook. 0 starting skills.
5. **Allocate attributes** (31 points across 10 attributes). Recall determines equip slots and skill depth ceiling.
6. **Resolve Certainty** (base from Origin + modifiers from Formation, Catalyst).
7. **Name Knots** (three suggested; player chooses which are Close, which are Distant).
8. **Write Beliefs** (starting Belief from Catalyst; additional Beliefs from Knot relationships).
9. **Equip skills** (3 starting skills auto-equip; Recall ≥ 3 at creation means all fit).
10. **Allocate History points** (per Recall cap per History).

---

## Example Character Build

**Mira Sondhal** (existing canonical test character, ED-143)

| Stage | Choice | Result |
|---|---|---|
| Origin | 1D: Southern Einhir Descendant | Born near Oastad. Inherited Resonance (+5 TS). Certainty 3. Knot: grandmother who taught folk songs. |
| Formation | 2F: Practitioner Mentorship | Trained by a solitary practitioner. Certainty 3 → 1. Knot: mentor (possibly connected to warden network). |
| Vocation | 3-VA3: Einhir Antiquarian | Works Varfell's antiquities network. Artefact Authentication, Black Market Contacts. Knot: a dealer who knows too much. |
| Catalyst | 4E: The First Leap | First Leap succeeded. Certainty 1 → 0. Post-Leap Clarity, Rendering Memory. Starting Belief: "The wound at Askeheim is killing the rendered world — someone must make the factions understand before it is too late." |

**Result:** Practitioner-Scholar. TS 61 (canonical). Certainty 0. Three Close Knots: grandmother (cultural anchor), mentor (practice anchor), antiquities dealer (information anchor). Four Histories generating 12 skills across all five domains. Campaign hook: the First Leap showed her something about Askeheim's condition that demands action.

---

## Open Editorial Items

- [EDITORIAL: ED-374 — Lifepath system requires user approval. Structural change from occupational to biographical Histories.]
- [EDITORIAL: ED-375 — Skill mechanical effects provisional. Simulation required — Level 1/2/3 effect scaling needs calibration.]
- [EDITORIAL: ED-377 — Intuitive Threadwork and Co-Movement interaction still open.]
- [EDITORIAL: ED-378 — Knot generation from lifepath: confirm that three suggested Knots is the right number.]
- [EDITORIAL: ED-379 — Catalyst stage: should every character have exactly one Catalyst, or can experienced characters have two?]
- [EDITORIAL: ED-380 — Southern Einhir Descendant (1D) grants +5 Thread Sensitivity at creation. Interaction with Approach Training eligibility needs verification.]
- [EDITORIAL: ED-381 — Recall as equip-slot gatekeeper: confirm that Recall 1 = 1 equip slot is not too punishing for low-Recall builds. Minimum-viable character at Recall 3 has 3 slots for 3 starting skills — this is tight but functional.]
- [EDITORIAL: ED-382 — Coherence-based equip slot loss: confirm that auto-unequipping skills at Fragmented/Fractured feels right in play. Should the player choose which skills to drop, or should the system auto-drop most recently equipped?]
- [EDITORIAL: ED-383 — Skill levels 1–3: confirm that Level 3 requiring dice_bonus ≥ 5 (and therefore Recall ≥ 5) is the right gate. This means only high-Recall specialists can master any skill — intentional?]

## Godot Implementation

The mechanical system described above is implemented in `jordanelias/valoria-game`:
- `SkillData.gd` — skill with levels 1–3, equip flag, per-level effects
- `HistoryData.gd` — lifepath stage, spark list, starting_skill_count
- `KnotData.gd` — Close/Distant proximity, strain, anchoring
- `CharacterData.gd` — Recall-based equip slot management
- `SkillSparkingSystem.gd` — SaGa-style scene-use sparking + level-up engine
- `SkillEffectResolver.gd` — applies equipped skill effects to RollContext
- `CharacterCreationManager.gd` — 4-stage lifepath creation flow

See `docs/history_skill_integration.md` in the valoria-game repo for full integration details.
