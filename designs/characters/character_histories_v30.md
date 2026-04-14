<!-- v30 baseline — renamed from designs/characters/character_histories_lifepath.md on 2026-04-13 -->
# VALORIA — Character Histories: Lifepath System
## Status: DESIGN PROPOSAL — requires editorial approval
## Scope: Lifepath-based History generation with SaGa-style sparking, Recall-gated equip slots, skill levels 1–3
## Cross-references: params_core.md, combat_design_v1.md, social_contest_system_v2.md, mass_battle_v3.md, stage6_factions.md, threadwork_redesign_v25.md, calamity_radiation.md
## [EDITORIAL: ED-374 — Character Histories system. Setting/worldbuilding/character content — editorial gate applies.]
## Godot implementation: jordanelias/valoria-game (see docs/history_skill_integration.md)

---

## Structure

Character creation moves through **four lifepath stages**. Each stage answers a biographical question and grants one History.

| Stage | Question | What It Determines | Starting Skills |
|---|---|---|---|
| 1. Origin | Where were you born and who raised you? | Geographic roots, cultural baseline, starting Certainty, first Knot | 1 |
| 2. Formation | How were you educated or shaped? | Intellectual framework, institutional exposure, second Knot | 1 |
| 3. Vocation | What were you trained to do? | Professional skills, factional affiliation, third Knot | 2 |
| 4. Catalyst | What happened that put you on this path? | Inciting event, starting Belief, campaign hook | 1 |

**Starting skills: 5 total.** All start at Level 1 and auto-equip. With Recall ≥ 5 at creation, all fit. Recall 3 forces loadout choices from session 1.

**Sub-modifiers:** Origins, Formations, and Vocations that span multiple geographic or institutional variants include sub-modifiers — a secondary selection that adjusts one skill, one Knot detail, or one narrative element. Sub-modifiers do not add a new History; they specialise the existing one.

**Recall as skill gatekeeper:**
- **Equip slots:** `max_equipped = Recall` (1–7). All sparked skills retained permanently; only Recall-many active at any time. Swap loadout between scenes.
- **Skill depth:** Skills have Levels 1–3. Level 2 requires History dice_bonus ≥ 3; Level 3 requires dice_bonus ≥ 5. Recall caps dice_bonus, so Recall indirectly caps max level.
- **Learning speed:** `floor(Recall/2)` bonus dice on all spark checks.
- **Coherence erosion:** Fragmented = effective Recall −1. Fractured/Severed = effective Recall −2. Practitioners who push Coherence low lose equipped skill access.

**Knot generation:** Stages 1–3 each produce a suggested Close Knot. Stage 4 produces a starting Belief. Player chooses which Knots are Close (max 3) vs Distant. Every Knot must answer: what does this person want from you? What does maintaining the relationship cost? What happens if it breaks?

**Certainty:** Stage 1 sets the baseline. Later stages modify it. Final Certainty recorded after all four stages.

**Sparking (SaGa-style):** After any meaningful scene roll (Ob ≥ 2), check for skill spark. Overwhelming at Ob 3+ = automatic. Success/Partial/Failure at sufficient Ob = Spirit + floor(Recall/2) check. Sparks prioritise level-ups over new acquisitions. Cross-History hybrid sparks fire when 2+ Histories used in same scene at Ob 2+ and Success+.

**Skill levels:** Level 1 = base effect. Level 2 = quantitative enhancement. Level 3 = qualitative unlock (new action or immunity). Level-up requires History dice_bonus ≥ 3 (Level 2) or ≥ 5 (Level 3) plus spark at corresponding Ob.

**Literacy model:**

| Formation | Literacy |
|---|---|
| 2A Church Schooling | Full (starting skill) |
| 2B Ducal Household | Full (tutors; assumed, not a skill slot) |
| 2C Guild Apprenticeship | Trade (contracts, ledgers, guild marks; not scripture) |
| 2D Self-Taught | Illiterate unless backstory specifies; literacy available as spark |
| 2E Military Training | Functional (orders and dispatches) |
| 2F Practitioner Mentorship | Full (philosophical texts required) |
| 2G Monastic Seclusion | Full (monastic libraries) |

---

## STAGE 1: ORIGIN — Where were you born and who raised you?

Origin establishes geographic and cultural foundation. **Grants 1 starting skill** (first skill listed). Remaining skills on spark list.

---

### 1A. Crown Heartland Child
Born in the eastern lowlands — Valorsplatz, Kronmark, Feldmark, or Stillhelm. The Crown heartland is the granary that feeds the peninsula. Hafenmark cannot feed itself (ED-054). Without Feldmark and Kronmark, the peninsula starves. You grew up understanding food as politics — not abstractly but as the rhythm of your family's labour.

**Who raised you:** A family embedded in the Crown's civil order. Markets on Crown coin, roads Crown-maintained, disputes to Crown magistrates.

**Starting Certainty:** 4 (Average Valorian).

**Modifier: River District (Valorsplatz)** — Born along the river-sea junction. Trade, not agriculture. Replace Heartland Roots with **River Mouth** (unique): +1D on Domain Actions involving Schoenland or eastern maritime trade. Knot shifts to a dockside trader or river-barge family.

**Modifier: Breadbasket (Feldmark/Kronmark)** — Born on productive farmland. Replace River Knowledge with **Harvest Leverage** (unique): +1D on Domain Actions or investigation involving food supply, agricultural economics, or territorial Prosperity.

| Skill | Domain | Effect |
|---|---|---|
| ★ **Heartland Roots** (unique) | Faction Play | In Crown-held territories: +1D on Domain Actions involving public order, community relations, or supply logistics. |
| **River Knowledge** § | Investigation / Faction Play | +1D involving river transport, eastern trade routes, or Valorsplatz logistics. |
| **Sturdy Stock** § | Scene Battle | Stamina base +1. |

**Knot:** A parent or sibling who still works the land or the river — and who depends on the political stability you are now entangled in. When the Crown's Mandate drops, your family's safety drops with it. Every factional action that weakens the Crown threatens the person who raised you.

**Narrative impact:** You were raised inside the system everyone else is trying to influence, control, or overthrow. You carry an unconscious assumption that the Crown's order is the natural state of things.

---

### 1B. Highland Born (Hafenmark)
Born in the northwestern highlands — Gransol, Rendstad, Spartfell, or Halvarshelm. Landlocked, mineral-rich, Swiss-character territory that Altonia squeezed hardest during the occupation.

**Who raised you:** Highland family — miners, herders, artisans, or minor functionaries. Tight community, procedural, suspicious of outsiders. The occupation ended generations ago but its shadow shapes everything: emphasis on law, distrust of charismatic leaders, institutional stubbornness.

**Starting Certainty:** 4 (Average Valorian). The Church is present but culturally secondary to Hafenmark's constitutional identity.

**Note on Thread absence:** Hafenmark is where Einhir cultural suppression was most thorough during occupation (concentrated Altonian oversight; mineral wealth was the priority). You come from the place where not-knowing about Thread was most systematically enforced. The highlands are node distance 4-5 — even at low RS, Calamity effects barely reach here.

| Skill | Domain | Effect |
|---|---|---|
| ★ **Highland Toughness** (unique) | Scene Battle / Mass Battle | In cold, high-altitude, or mountainous conditions: no environmental penalties. |
| **Institutional Instinct** § | Debate | In proceedings governed by formal rules: +1D on Appraise rolls. |
| **Community Solidarity** § | Faction Play | In Hafenmark-held territories: +1D on Stability-related Domain Actions. |

**Knot:** A community elder or extended family figure who embodies constitutional values. They taught you that procedure is the wall between civilisation and tyranny. When Baralta invokes Sovereign Authority Doctrine, this person either celebrates (law triumphant) or worries (overreach by a single ruler).

**Narrative impact:** Law over personality, procedure over charisma. Strength against demagogues; blindness to action that can't be procedurally justified.

---

### 1C. Fjord Child (Varfell)
Born on Varfell's western coast — Sigurdshelm, Halvardshelm, Oastad, or Grauwald. Norwegian-character fjord communities connected by sea, separated by mountains.

**Who raised you:** Fjord family — sailors, herders, fisher-folk. Maritime, isolated, self-sufficient. The Einhir presence is strongest here — folk practices survive in the southwest as living tradition.

**Starting Certainty:** 4 (Average Valorian) in northern Varfell.

**Modifier: Southern (Oastad)** — Certainty drops to 3 (Secular). Add **Calamity Familiarity** § to spark list: +1D on Attunement rolls at node distance 0-2. The Calamity's influence is part of your childhood — animals unsettled, elders who know things they can't explain.

| Skill | Domain | Effect |
|---|---|---|
| ★ **Sea-Bred** (unique) | Scene Battle | On water or coastal terrain: +1D to Defence. Unstable footing is normal footing. |
| **Fjord Isolation** § | Investigation | In Varfell territories: +1D to detect outsiders or changed patterns. Small communities notice everything. |
| **Practical Self-Reliance** § | Scene Battle / Investigation | When no allies present in zone: +1D to one roll per scene. Help is far away. |

**Knot:** A community member — fisher, elder, childhood rival who became a friend. They represent the small-scale world that factional politics threatens. The Maritime Forgetting blocks the southern sea route and your community feels this as economic isolation that can't be rationally explained — you know the route doesn't work, but you can't say why.

---

### 1D. Southern Einhir Descendant
Born in communities closest to the Southernmost — southern Oastad, settlements ringing Askeheim, hamlets at node distance 1-2.

**Who raised you:** An Einhir-descendant family. Not practitioners — people whose grandparents' grandparents spoke a different language, practised different rites. **245 years of Church institutional suppression** — heresy declarations, text confiscation, practice prohibition, forced conversion of naming conventions — eroded most of this inheritance. What survives does so because it was encoded as folk habit: songs without translatable lyrics, ritual gestures at births and deaths, persistent unease about the Solmund narrative that cannot be articulated. This is not the Forgetting (a metaphysical mechanism localised to Askeheim per calamity_radiation.md). This is cultural destruction by institutional authority, sustained across ten generations, partially successful, never complete.

**Starting Certainty:** 2 (Skeptic). The Church's account does not match your inherited experience.

**Modifier: Askeheim-Adjacent (T6 Stillhelm / T13 Oastad — node distance 1)** — Add **Wound Proximity** (unique) to spark list: when RS crosses a threshold band, you feel it as physical unease before anyone announces it. +1D on Attunement rolls at node distance 1.

**Modifier: Deep South (near Askeheim — node distance 0-1)** — Inherited Resonance TS bonus +8 (instead of +5). Starting Certainty drops to 1 (Transitional). Songs that produce involuntary weeping. Gestures that calm animals too effectively.

| Skill | Domain | Effect |
|---|---|---|
| ★ **Inherited Resonance** (unique) | Investigation | Thread Sensitivity +5 at creation. Ambient Calamity exposure since birth primed your configuration. Not a practitioner — but closer to the threshold than most. |
| **Calamity Familiarity** § | Investigation | At node distance 0-2: +1D on Attunement rolls. The wound is your neighbourhood. |
| **Cultural Memory** § | Debate / Investigation | +1D engaging with pre-Calamity history, Einhir artefacts, or folk practice. Knowledge as recognition, not intellect. |

**Knot:** A grandmother or elder who carries Einhir tradition. They taught you the songs, the gestures. They could not explain why they matter. They may be dead — and what they gave you is the only record that they existed as carriers of something the Church tried to erase.

---

### 1E. Himmelenger Child (Church Territory)
Born and raised in Himmelenger — Cathedral city, the Church's seat, the theological centre. Bells, scripture, liturgy, towering architecture of institutional faith.

**Who raised you:** A family within the Church's cultural orbit. Himmelenger is not a city with a cathedral; it is a city that IS a cathedral. Every institution operates under the Church's moral framework.

**Starting Certainty:** 5 (Orthodox). The Church's account of reality is not something you were taught — it is the air you breathed.

| Skill | Domain | Effect |
|---|---|---|
| ★ **Cathedral Raised** (unique) | Debate | In Church Tribunal or any proceeding in Church-held territory: +1D to both Appraise and Argue. This is your house. |
| **Doctrinal Fluency** § | Debate / Investigation | +1D on Solmund theology, Church history, liturgical practice. |
| **Institutional Gravity** § | Faction Play | Domain Actions on Church's behalf: strain from failed actions reduced by 1. |

**Knot:** A childhood mentor within the Church — parish teacher, seminary instructor, family confessor. They represent the certainty you grew up inside. Whether that certainty holds or cracks defines your arc. When Thread truth reaches Himmelenger (and it will, as RS drops), this person's reaction will either anchor you or devastate you.

**Narrative impact:** Certainty 5 means the first Coherence loss per session is nullified by doctrine scaffolding (params_core). When doctrine finally cracks, the fall is further. Node distance 4 — at RS 60, Himmelenger is untouched. The wound hasn't reached you yet.

---

### 1F. Valorsplatz Underclass
Born in the capital's lower districts. Not a generic urban poor — a resident of specific Valorsplatz geography.

**Who raised you:** Single parent, extended working family, or the street itself. The capital's wealth flows through your neighbourhood without stopping.

**Starting Certainty:** 3 (Questioning). Neither institution has earned your faith. Neither has lost it entirely.

**Modifier: Tideward (river/harbour district)** — The flood-prone lower district between the river and the eastern harbour. Schoenland ships dock at your doorstep. Niflhel's dockworker arm operates the same routes you grew up on.

Starting skill: ★ **Tideward Rats** (unique) — +1D on all Investigation rolls in Valorsplatz. You know the sewers, warehouses, smuggling routes. Additionally: +1D to detect Niflhel activity specifically (they use the same routes you do).

**Modifier: Ashmarket (inland slum on Einhir foundations)** — Built over the ruins of a pre-occupation Einhir quarter. The foundations occasionally produce objects that should not exist — not through Thread activity (node distance 3, no Calamity effects at RS 60) but through simple archaeology: things buried 245+ years ago occasionally become unburied.

Starting skill: ★ **Foundations** (unique) — Once per arc, an object from the pre-occupation Einhir quarter surfaces. Roll Cognition TN 7 Ob 2. Success: the GM provides one piece of information about the Einhir presence that predated the current city. You don't understand significance. You understand market value.

| Skill | Domain | Effect |
|---|---|---|
| ★ **Tideward Rats** or **Foundations** (per modifier) | Investigation | See above |
| **Scrapper** § | Scene Battle | Unarmed/improvised: TN 7 instead of TN 8. |
| **Invisible** § | Investigation | Avoiding notice in urban crowds: +1D on Agility concealment. |

**Knot (choose per modifier):**
- *Tideward:* A sibling who works Niflhel's dockworker arm and doesn't know you know — or who knows and pretends not to. Their safety depends on your silence; your conscience depends on not examining what they move.
- *Ashmarket:* A Church charity teacher who taught you to read and whose faith you both respect and resent. They believe the Church saved you. You believe the Church demolished the civilisation whose ruins you grew up on.

---

### 1G. Border Settlement Child
Born in northern border territories — Lowenskyst, Spartfell, or Halvarshelm. Communities that exist because a fortress needs people to supply it.

**Who raised you:** Military family or military-adjacent — blacksmiths, provisioners, farriers. The border is a physical presence. You grew up watching the mountain passes.

**Starting Certainty:** 4. The Löwenritter are a visible presence — the military order shapes border life as much as the Crown or Church.

| Skill | Domain | Effect |
|---|---|---|
| ★ **Border Vigilance** (unique) | Mass Battle / Investigation | In border territories: +1D on Cognition to detect ambush, assess enemy strength, identify terrain advantage. |
| **Cold Endurance** § | Scene Battle | No penalty in cold/winter conditions. |
| **Frontier Self-Reliance** § | Investigation / Scene Battle | No allied reinforcements available: +1D to one roll per scene. |

**Knot:** A garrison soldier or parent who served at the border — and who specifically remembers what it was like when Altonian forces last probed the pass. They carry a warning that the rest of the peninsula doesn't take seriously enough. When Institutional Pressure rises, they write you letters that grow increasingly urgent.

---

### 1H. Displaced — No longer generic

**1H-i. Occupation Displaced**
Family displaced during the Altonian occupation's aftermath — post-liberation resettlement, collaborator property seizure, destroyed communities.

Starting Certainty: 3. Starting skill: ★ **Nowhere to Return** (unique) — No ethical framework modifier on Domain Actions. +1D on rolls involving displacement, refugee communities, or post-conflict resettlement.

Knot: A member of another displaced family whose trajectory diverged from yours — they joined Niflhel, or the Restoration, or the Crown army. You share landlessness and nothing else.

**1H-ii. Calamity Orphan**
Family destroyed by a Calamity event — Shifting Object, rendering failure, threadcut being encounter at the southern edge.

Starting Certainty: 2. Starting skill: ★ **Scarred by the Unreal** (unique) — Immune to Composure loss and surprise-round penalties from Thread phenomena. Thread Sensitivity +3.

Knot: Surviving family member who witnessed the same event and accepted the Church's explanation (natural disaster). Your insistence that something else happened has strained the relationship. They think you're traumatised. You think they're in denial.

**1H-iii. Church Ward**
Raised in a Church orphanage. Parents unknown or dead.

Starting Certainty: 4 or 5 (GM determines). Starting skill: ★ **Institutional Child** (unique) — +1D on all rolls involving Church infrastructure, personnel, or procedures. You grew up inside the institution.

Knot: A fellow orphan who chose a different path. The bond is pre-institutional — it exists because you shared a dormitory, not a worldview.

---

## STAGE 2: FORMATION — How were you educated or shaped?

**Grants 1 starting skill** (★ marked). Remaining skills on spark list.

---

### 2A. Church Schooling
The only widespread education infrastructure on the peninsula. Literacy, numeracy, scripture, Solmund history.

**Certainty modifier:** +1 if starting Certainty below 5. The most powerful socialisation tool the Church possesses.

| Skill | Domain | Effect |
|---|---|---|
| ★ **Literate** (unique) | Investigation / Debate / Faction Play | Can read and write. +1D on all rolls involving documents, correspondence, written records. In a mostly oral society, literacy is power. |
| **Doctrinal Fluency** § | Debate / Investigation | +1D on Solmund theology, Church history, liturgical practice. |
| **Trained Memory** § | Debate | Concentration (Focus + Recall) +2 in social contests. |

**Knot:** School mentor who invested in you personally. Whether you now agree with what they taught defines a live tension. They shaped your intellectual development — and they shaped it within the categories the Church provides.

---

### 2B. Ducal Household Education
Educated as part of a noble or ducal household's retinue — Crown, Hafenmark, or Varfell. Specify which household (affects worldview: Crown = virtue ethics, Hafenmark = proceduralism, Varfell = consequentialism).

**Certainty modifier:** None.

| Skill | Domain | Effect |
|---|---|---|
| ★ **Political Literacy** (unique) | Debate / Faction Play | +1D on Appraise in any political context. You grew up watching power operate. |
| **Courtly Bearing** § | Debate | In Formal or Grand Contests: immune to first exchange of strain. |
| **Patron's Connections** § | Faction Play | +1D on one Domain Action per season within the educating household's faction system. |

**Knot:** A fellow student — someone your age who shared Formation. You may now serve the same faction or opposing ones. The bond was formed before politics intervened.

---

### 2C. Guild Apprenticeship
Apprenticed to a master. Trained in a specific craft and socialised into the Guilds' moral relativism — value determined by skill, not birth or doctrine.

**Certainty modifier:** −1 if starting at 5. Guild culture is secular; prolonged immersion in an institution that recognises no universal moral principles loosens orthodoxy through exposure, not argument.

| Skill | Domain | Effect |
|---|---|---|
| ★ **Craft Expertise** (unique) | Investigation / Faction Play | +2D on any roll involving your specific craft (declared at creation). Creation, assessment, repair, identification. |
| **Economic Reasoning** § | Debate | +1D to Argue pool in arguments involving economic stakes. |
| **Guild Network** § | Faction Play / Investigation | +1D when interacting with Guild faction or in high Guild Favour territories. |

**Knot:** Your master craftsperson. Professional standards, craft values, the specific relationship between someone who knows and someone who is learning. Whether kind or demanding, the most formative relationship of your adolescence.

---

### 2D. Self-Taught / Empiricist
No formal education. The Church controls formal education; the Guilds provide trade apprenticeships; ducal households educate retinues. You exist **outside the peninsula's entire epistemological apparatus.** What you learned, you learned by observing the world directly — empirical, fragmented, uncontaminated by institutional framing.

**Certainty modifier:** −1 regardless of starting value. Without institutional education, no framework reinforces any Certainty level. Your Certainty is inherently unstable — it moves in either direction more easily because nothing anchors it.

| Skill | Domain | Effect |
|---|---|---|
| ★ **Empiricist** (unique) | Any | When presented with a claim that contradicts your direct observation: +1D on any roll to verify, investigate, or challenge the claim. You trust your eyes over anyone's authority. |
| **Street Wisdom** § | Investigation | In urban environments: +1D on Attunement to detect danger or assess intentions. |
| **Hard to Fool** § | Debate | Opponent's Doubt Marker effect reduced by 1 when used against you. You've been lied to by experts. |

**Knot:** A specific person who showed you something that contradicted institutional reality — a midwife who treated patients the Church said were cursed, a veteran who told you the occupation ended differently than official history claims. Their specific knowledge gave you reason to trust observation over authority.

---

### 2E. Military Training
Educated through military service — Crown army, Hafenmark ducal guard, Varfell household troops, or Löwenritter squire training. Specify which institution (affects military culture).

**Certainty modifier:** None.

| Skill | Domain | Effect |
|---|---|---|
| ★ **Weapons Training** (unique) | Scene Battle | Choose one weapon combination (Reach × Weight × Type). With that weapon: +1D to Offence allocation. Trained specifically, repeatedly, until reflex. |
| **Formation Instinct** § | Mass Battle | Unit containing this character: +1 Discipline starting value (max 7). |
| **Physical Conditioning** § | Scene Battle | Stamina base +1. |

**Knot:** Training partner, drill instructor, or fellow recruit. Bonds formed under shared physical hardship. This person knows what you can endure because they endured it beside you.

---

### 2F. Practitioner Mentorship
Educated by a Thread practitioner — warden, solitary practitioner, or scattered practitioner community. Philosophical and practical preparation for Thread practice. You may not have Leaped yet.

**Certainty modifier:** −2 (minimum 0). Practitioner education systematically dismantles Solmund cosmology through experience, not argument.

| Skill | Domain | Effect |
|---|---|---|
| ★ **Approach Training** (unique) | Scene Battle (Thread) | Leap roll: +1D. Trained specifically for the surrender of rendering. |
| **Thread Perception** § | Investigation | When TS ≥ 30: +1D on Attunement to perceive Thread phenomena. |
| **Philosophical Grounding** § | Debate | +1D arguing about ontology, Thread reality, or rendering. |

**Knot:** Your practitioner mentor. One of the deepest Knots in the game. They showed you what lies beneath rendering and trusted you with knowledge the Church would burn you for. Whether they are still alive, still practicing, or still sane (their Coherence state is a dramatic variable) defines a major axis of your arc.

---

### 2G. Monastic Seclusion
Educated in a remote contemplative house — not the urban seminary but an isolated monastery. Quiet, rigorous, divorced from political reality.

**Certainty modifier:** +1 or −1 (GM determines). Monastic seclusion either deepens faith or cracks it. The player does not choose.

| Skill | Domain | Effect |
|---|---|---|
| ★ **Contemplative Focus** (unique) | Debate / Scene Battle (Thread) | Focus +1 for Contact Duration calculation only. Years of discipline taught you to hold rendering at bay slightly longer. |
| **Archive Access** § | Investigation | +1D on Recall-based rolls researching documents or records. Monasteries have libraries. |
| **Silence Reader** § | Investigation / Debate | Appraise in one-on-one or small-group: TN 6 instead of TN 7. You read people in a community where no one spoke. |

**Knot:** A fellow monk or abbot/abbess. They represent the quality of attention monastic life produces — and the question of whether that attention reveals truth or illusion.

---

## STAGE 3: VOCATION — What were you trained to do?

**Grants 2 starting skills** (★ marked). At least 1 of 2 must be unique. Remaining skills on spark list.

**Vocation determines faction affiliation.** Contradictions between Origin/Formation/Vocation produce character tension — a Crown Heartland Child with Practitioner Mentorship and a Church Vocation is a character whose biography is a argument with itself.

---

### Crown Vocations

| Vocation | Starting Skills (★) | Third Skill (spark) | Knot |
|---|---|---|---|
| **3-CR1: Court Official** | ★ Courtly Grace (unique: +1D Argue before Expert Judge in Crown territory) · ★ Read the Room § (Appraise TN 6 in formal settings) | Institutional Memory § (+1D to relevant Unique Action) | A rival official who holds evidence of a procedural error you made. They have never used it. You don't know if this is mercy, leverage, or indifference. |
| **3-CR2: Crown Soldier** | ★ Riposte § (counter-Strike after successful Defence) · ★ Formation Discipline § (+1 Discipline start) | Garrison Eyes (unique: +1D detect infiltration in posted location) | A squad-mate who deserted. You know where they went. The Crown does not. Reporting them is duty. Silence is choice. |
| **3-CR3: River Trader** | ★ Schoenland Contacts § (+1D DA involving Schoenland) · ★ Haggler's Nerve § (−1 strain in private negotiation) | Cargo Sense § (+1D detect forged/smuggled goods) | A Schoenland trading partner whose neutrality you depend on and whose self-interest you understand — they will sell to Altonia if the price is right. |
| **3-CR4: Crown Magistrate** | ★ Procedural Objection § (force Regroup or +1 Ob once/contest) · ★ Paper Trail § (+1D institutional records) | Tax Assessment (unique: +1D Wealth-targeting DA) | A mentor judge whose standards you carry — and whose one unjust ruling you witnessed and never reported. |
| **3-CR5: Crown Farmer** | ★ Harvest Leverage (unique: +1D on DA involving food supply/Prosperity) · ★ Seasons Reader § (+1D Cognition for weather/terrain/agriculture) | Community Backbone § (+1D Stability DA in territory you've lived 1+ seasons) | A neighbour whose family has worked alongside yours for generations. When territory changes hands, their survival depends on which faction takes control. |

### Church Vocations

| Vocation | Starting Skills (★) | Third Skill (spark) | Knot |
|---|---|---|---|
| **3-CH1: Seminary Graduate** | ★ Doctrinal Authority (unique: +3D Recall bonus in Memory genre on theology) · ★ Liturgical Composure § (+2 Composure in Church Tribunal) | Theological Insight § (+1D analysing theological content) | A seminary rival whose theological positions are the mirror of yours. Their arguments are the ones that kept you awake. |
| **3-CH2: Templar** | ★ Smite the Heretic (unique: +1D Offence vs declared heretic/practitioner in Thread ops) [ED-388: intra-party hostility potential — intentional?] · ★ Shield of Faith § (+1D Defence in Full Guard) | Righteous Conviction § (immune to Doubt Markers in Church Tribunal) | A fellow Templar whose faith is deeper than yours — or shallower. You trained together. The order's bonds are designed to be absolute. They may not survive what comes. |
| **3-CH3: Parish Priest** | ★ Sermon Delivery (unique: +1 Conviction Track on Revealing win before Crowd) · ★ Folk Trust § (−1 Ob DA involving common population where Church Mandate ≥ 4) | Road Survival § (+1D Endurance in unfamiliar territory) | A parishioner who trusts you personally, not institutionally. They represent what the Church is supposed to be. When the Church fails them, you are the face of that failure. |
| **3-CH4: Church Archivist** | ★ Forbidden Knowledge (unique: once/arc suppressed document recall) · ★ Paper Trail § (+1D institutional records) | Doctrinal Inconsistency (unique: +1D arguing against Church position in Memory genre) | A fellow archivist who discovered the same suppressed material — and chose differently about what to do with it. |
| **3-CH5: Church Investigator** | ★ Inquisitorial Method (unique: +1D Investigation targeting heresy/Thread practice/Einhir activity) · ★ Suppressed Exposure (unique: TS +3 from occupational handling of confiscated Einhir texts and practitioner testimony) [ED-389: occupational TS gain — canonical?] | Doctrinal Fluency § | A subject of a past investigation — someone you investigated and either prosecuted or quietly released. If prosecuted: the weight of what you did. If released: the secret you share. Certainty modifier from Vocation: −1 or +1 (GM determines). |

### Hafenmark Vocations

| Vocation | Starting Skills (★) | Third Skill (spark) | Knot |
|---|---|---|---|
| **3-HA1: Parliamentary Aide** | ★ Constitutional Precedent (unique: −1 Audience Resistance when citing constitutional clause) · ★ Procedural Objection § | Institutional Memory § | A political opponent who once saved your career by voting against their own faction to protect a procedural principle. They lost standing. You owe a debt neither of you can publicly acknowledge. |
| **3-HA2: Highland Miner** | ★ Tunnel Fighter (unique: +1D Defence in confined spaces) · ★ Stone Reader (unique: +1D assess terrain/fortifications) | Stubborn Endurance § (first wound penalty negated) | A mine-shaft partner whose life depended on your attention. Underground bonds are absolute. |
| **3-HA3: Border Guard (Spartfell)** | ★ Fortress Defender (unique: +1D Defence in Fortified positions) · ★ Know the Enemy § (+1D identify Altonian forces) | Cold Iron § (no cold weather penalty) | A fellow border guard who watched the mountains with you. You share the specific anxiety of people who live where the threat arrives first. |
| **3-HA4: Highland Guide** | ★ Mountain Ambush (unique: −1 Ob one tactic/battle in highland terrain) · ★ Sure-Footed § (auto-success Establish Distance in difficult terrain) | Weatherwise § (Cognition roll to learn one environmental modifier) | A client whose survival through dangerous terrain created an obligation that became a friendship — and who now holds a position of authority that requires your discrete silence about how they nearly died. |

### Varfell Vocations

| Vocation | Starting Skills (★) | Third Skill (spark) | Knot |
|---|---|---|---|
| **3-VA1: Intelligence Operative** | ★ Dead Drop (unique: establish covert channel, −1 Ob Intel ops) · ★ Smooth Liar § (−1 strain when using Obscuring) | Shadow Work § (+1D surveillance/counter-intel) | A handler who gives orders and evaluates results. Trust is professional, not personal — which makes it more fragile than either of you admit. |
| **3-VA2: Fjord Sailor** | ★ Sea Legs § (+1D Defence on water) · ★ Coastal Navigation (unique: +1D navigation/recon on western coast) | Community Voice § (+1D Argue before Crowd for common people) | A captain who sailed too close to the southern Maritime Forgetting zone and came back changed — quieter, distracted, prone to staring at water. Seamanship undiminished. Humanity in question. You're the only crew who noticed. |
| **3-VA3: Einhir Antiquarian** | ★ Artefact Authentication (unique: +2D assess Einhir objects) · ★ Black Market Contacts § (+1D underground networks) | Einhir Lore § (+1D pre-Calamity knowledge) | A collector whose ethics regarding acquisition differ from yours. The trade in Einhir artefacts is covert by necessity — the Church classifies it as heretical. Your shared enterprise is your shared risk. |
| **3-VA4: Ducal Retainer** | ★ Vaynard's Confidence (unique: Spirit roll for +1D Thread-related roll when Private Collection used) · ★ Read the Room § | Household Authority § (−1 Ob DA in Varfell territories) | A fellow retainer who has noticed the same things about the Duke's private interests. Whose silence you rely on — and who relies on yours. |

### Guild Vocations

| Vocation | Starting Skills (★) | Third Skill (spark) | Knot |
|---|---|---|---|
| **3-GU1: Guild Factor** | ★ Cross-Border Immunity (unique: −1 ethical framework Ob in foreign territory) · ★ Haggler's Nerve § | Cargo Sense § | A business rival whose family you bankrupted through a legitimate but ruthless manoeuvre. They rebuilt. They never mentioned it. Their silence is more unsettling than anger. |
| **3-GU2: Guild Enforcer** | ★ Back-Alley Fighter (unique: +1D Stunt in urban) · ★ Intimidation § (+1D Obscuring in private negotiation) | Smooth Liar § | A debtor you chose not to collect from — someone whose vulnerability became your conscience. They don't know you protected them. If they find out, the power dynamic changes. |
| **3-GU3: Master Craftsperson** | ★ Master Craftwork § (once/season craft +1 item) · ★ Guild Kinship § (+1D Influence DA with Guilds) | Precision Hands § (+1D examining crafted objects) | A journeyman you trained who surpassed you. Their work is better. You're proud and envious simultaneously. They still call you "master" and each time it costs you something you can't name. |

### Niflhel Vocations

| Vocation | Starting Skills (★) | Third Skill (spark) | Knot |
|---|---|---|---|
| **3-NI1: Dockworker (Niflhel arm)** | ★ Hidden Cargo (unique: −1 Ob smuggling) · ★ Scrapper § (unarmed TN 7) | Shadow Work § | A fellow dockworker who doesn't know the full extent of what you move — or who knows and pretends not to. Each Thread Tension +0.5 from Niflhel's Southernmost harvesting flows through your hands without your knowledge. |
| **3-NI2: Quiet Operative** | ★ Silent Kill (unique: +3 flat damage vs unaware target) · ★ Vanish (unique: Agility TN 7 Ob 2 to leave zone untracked) | Dead Drop § | A former target you did not kill — someone whose life you hold like a debt that can never be repaid. Their existence is evidence of your disobedience. |
| **3-NI3: Reckoner** | ★ Pressure Point (unique: +2D when financial vulnerability identified) · ★ Intimidation § | Urban Navigation § (+1D escape/evasion in urban) | A debtor who became a source — someone whose vulnerability you exploited and who now provides information because the alternative is worse. The relationship is coercion wearing the mask of mutual benefit. |
| **3-NI4: Fence** | ★ Appraisal (unique: +2D assess value/authenticity any object) · ★ Black Market Contacts § | Haggler's Nerve § | A regular buyer whose discretion you trust. Transactional but durable. If they are arrested, they know enough to destroy you. This fact keeps you both honest. |

### Restoration Movement Vocations

| Vocation | Starting Skills (★) | Third Skill (spark) | Knot |
|---|---|---|---|
| **3-RE1: Pamphleteer** | ★ Incendiary Rhetoric (unique: +2D Argue before Crowd, Revealing, social justice) · ★ Underground Distribution (unique: −1 Ob Restoration DA) | Community Voice § | A printer whose physical safety depends on your discretion. Every pamphlet is evidence of sedition. |
| **3-RE2: Community Organiser** | ★ Solidarity (unique: +1D Community Weaving when acting as agent) · ★ Community Voice § | Folk Trust § | A community leader you radicalised — or who radicalised you. Political and personal simultaneously. If the movement is crushed, this person is arrested first. |
| **3-RE3: Folk Practitioner** | ★ Intuitive Threadwork (unique: Attunement + Spirit TN 8 Ob 3 for minor Weaving, pre-Leap) [ED-377: does this trigger Co-Movement per P-01?] · ★ Folk Healer (unique: +1D Medicine) | Einhir Lore § | Your grandmother or equivalent — the person who taught you the old ways. They may be dead. The practices are alive in your hands. |

### Löwenritter Vocations

| Vocation | Starting Skills (★) | Third Skill (spark) | Knot |
|---|---|---|---|
| **3-LO1: Löwenritter Knight** | ★ Elite Discipline (unique: unit Discipline floor 2) · ★ Riposte § | Formation Discipline § | A brother/sister knight whose loyalty to the Order matches yours. If the Coup Counter reaches 3, you face each other's choices. |
| **3-LO2: Border Ranger** | ★ Eagle Eyes (unique: Cognition roll to reveal one element of opposing Phase 1) · ★ Know the Enemy § | Cold Iron § | A patrol partner — someone who shares the mountain watch. More time in silence together than most people spend with family in conversation. |
| **3-LO3: Riskbreaker** | ★ Deniable Action (unique: Spirit roll to deflect evidence trail) · ★ Smooth Liar § | Silent Kill § | A handler within the Order — the only person alive who knows what you have done. This Knot is itself a secret. |
| **3-LO4: Patrol Officer (Threadcut Encounter Veteran)** | ★ Anomaly Recognition (unique: +1D Cognition to assess threadcut being threat/movement/constraints) · ★ Classified Knowledge (unique: once/arc invoke classified info for +2D; risks Order exposure) | Know the Enemy § | Your commanding officer who ordered you to file the false report ("anomalous wildlife"). Protecting you or containing you — you're not sure which. |

### Cross-Factional Vocations

| Vocation | Starting Skills (★) | Third Skill (spark) | Knot |
|---|---|---|---|
| **3-CF1: Mercenary** | ★ Weapon Versatility (unique: switch weapon type between exchanges at no cost) · ★ Riposte § | Eagle Eyes § | A former employer whose cause you served and whose money you took without moral commitment. They may call the debt of loyalty you never offered. |
| **3-CF2: Wandering Healer** | ★ Field Medicine (unique: −1 Ob stabilise) · ★ Folk Healer § | Road Survival § | A patient whose life you saved with a folk remedy the Church classifies as heretical. They recovered. They reported you. The investigation was dropped — but the Church file exists. |
| **3-CF3: Traveling Merchant** | ★ Wide Network (unique: +1D in up to 3 previously-operated territories) · ★ Haggler's Nerve § | Road Survival § | A trading partner you suspect of moving goods for Niflhel. You've never asked. Your trade route depends on their connections. Your conscience depends on not knowing. |
| **3-CF4: Scribe** | ★ Textual Memory (unique: recall previously-handled documents) · ★ Paper Trail § | Forgery Detection (unique: +2D authenticate documents) | An author whose work you copied — someone whose ideas you know better than your own because you transcribed every word. They don't know you exist. |
| **3-CF5: Diplomat / Envoy** | ★ Diplomatic Protocol (unique: ethical framework Ob penalties reduced by 1 when formally representing a faction) · ★ Read the Room § | Treaty Language (unique: +1D Recall on prior agreements/diplomatic precedent) | Your counterpart — the diplomat from the other side. Professional opponents, personal respect. If war breaks, this relationship becomes impossible to maintain and devastating to lose. |
| **3-CF6: Independent Criminal** | ★ Opportunist (unique: once/scene after any other character's roll revealed, +2D on next roll exploiting outcome) · ★ Slippery § (Escape −1 Ob; +1D pursuit evasion in urban) | Fence Contacts § (+1D underground trade with non-Niflhel networks) | A mark who became a friend — or a friend who became a mark. The relationship is built on a deception you've either confessed (survived) or maintained (dread). |

---

## STAGE 4: CATALYST — What happened that put you on this path?

**Grants 1 starting skill** (★ marked). Remaining skills on spark list. Produces a starting Belief shape.

---

### 4A. Witnessed Something Impossible
You saw a Thread phenomenon. Your rendering cracked.

**Canon note on Forgetting:** If the event occurred outside Askeheim (node distance 1+), the Forgetting does not apply — your memory persists because rendering didn't erase it. If at Askeheim (node distance 0), your retention means your TS was high enough for partial retention per the Forgetting Check (stage4_southernmost), which is diagnostically significant.

**Certainty modifier:** −1. **Belief shape:** "The world is not what [institution/faith/common sense] says — I must [investigate/understand/warn]."

| Skill | Domain | Effect |
|---|---|---|
| ★ **Shaken Certainty** (unique) | Investigation / Debate | Immune to Composure loss and surprise-round penalty from Thread phenomena. Certainty movement toward 0 from Discovery Events costs 1 less. |
| **Shifting Object Recognition** § | Investigation | Automatic recognition. |
| **Obsessive Recall** (unique) | Investigation | +1D on Recall about the specific event witnessed. If event at Askeheim: TS confirmed 10+ minimum (Forgetting partial failure is diagnostic). |

---

### 4B. Betrayed by Your Institution

**Certainty modifier:** −1 if Church; none otherwise. **Belief shape:** "I will never trust [institution] again — I will [expose/build/survive/repay]."

| Skill | Domain | Effect |
|---|---|---|
| ★ **Insider Knowledge** (unique) | Investigation / Faction Play | +2D Investigation targeting your former faction. |
| **Bitter Resilience** § | Debate | Immune to first Rattled mark per session. |
| **Burned Bridge** (unique) | Faction Play | +1D on counter-actions opposing your former faction's Domain Actions. |

---

### 4C. Lost Someone
A Close Knot died, disappeared, or was taken. **Anti-fridge clause:** The GM maintains a hidden "ghost sheet" for the lost person — Beliefs, faction affiliations, most important relationships. Knot Memory draws from this sheet. The lost person continues to influence the campaign.

**Certainty modifier:** None. **Belief shape:** "I will [find/avenge/complete their work/protect what they loved] — nothing else matters."

| Skill | Domain | Effect |
|---|---|---|
| ★ **Grief-Driven Focus** (unique) | Any | Once per session, pursuing an action related to the lost Knot: +2D. Grief burns clean when it has direction. |
| **Knot Memory** (unique) | Debate / Investigation | +1D invoking the lost person's knowledge, skills, or connections. GM draws from ghost sheet. |
| **Hollow Endurance** § | Scene Battle | At 1+ Wounds: first wound penalty negated. |

---

### 4D. Recruited — Faction-Specific

**4D-i. Crown** — Certainty: none. ★ **Crown Mandate** (unique): +1D first DA/season on Crown's behalf.
**4D-ii. Church** — Certainty: +1. ★ **Ecclesial Trust** (unique): +1D first DA/season on Church's behalf.
**4D-iii. Niflhel** — Certainty: none. ★ **Shadow Allegiance** (unique): +1D first covert DA/season.
**4D-iv. Restoration** — Certainty: −1. ★ **Movement Trust** (unique): +1D first Restoration-aligned DA/season.
**4D-v. Practitioner** — Certainty: −1. ★ **Marked for Practice** (unique): +1D on First Leap attempt. Stacks with Approach Training.

All variants share spark list: Quick Adaptation § (once/session +1D in a domain with no other skill bonuses), Recruiter's Trust (unique: +1D Investigation pursuing recruiter's objectives).

**Belief shape:** "[Recruiter] believes I can [specific task] — I will prove them [right/wrong/something unexpected]."

---

### 4E. The First Leap
Attempted the Leap and succeeded. Prerequisite: Formation 2F or TS ≥ 30 from other sources.

**Certainty modifier:** −1 (permanent, per threadwork_v25 §2.3). **Belief shape:** "I have been outside rendering. The world is [not what it seems/more fragile/beautiful beyond language] — I must [continue/find others/fix what's broken]."

| Skill | Domain | Effect |
|---|---|---|
| ★ **Leap Scar** (unique) | Scene Battle (Thread) | First Leap per session: +1D (not −1 Ob, to avoid OB_FLOOR interaction at high TS). |
| **Post-Leap Clarity** (unique) | Investigation | +2D on Attunement to perceive Thread phenomena (stacks with Thread Perception §). |
| **Rendering Memory** (unique) | Debate | Immune to Doubt Markers when arguing about Thread reality. You're reporting, not theorising. |

---

### 4F. War / Invasion — Specified

**4F-i. Spartfell Incident** — Altonian probe force crossed the NW pass 3-5 years pre-campaign. Repelled at Spartfell.
**4F-ii. Templar Suppression** — Church deployed Templars against a southern community suspected of Einhir revival 2-4 years pre-campaign. [ED-390: new setting event — requires approval.]
**4F-iii. Ducal Border Clash** — Hafenmark-Varfell territorial dispute over T10-T11 border escalated to armed skirmish 5-8 years pre-campaign.

**Certainty modifier:** None. **Belief shape:** "War took [what I had] — I will [prevent/fight/build]."

| Skill | Domain | Effect |
|---|---|---|
| ★ **Veteran's Eye** (unique) | Mass Battle | +1D on Command tactic rolls. Not from training — from survival. |
| **Combat Reflexes** § | Scene Battle | Attunement tied: you act last regardless of Agility tiebreaker. |
| **War Hardened** (unique) | Debate / Scene Battle | Immune to Morale penalties in mass battle; immune to Composure loss from witnessing violence. |

---

### 4G. Religious Crisis
Faith broke or deepened in a way that can't be undone. **GM determines direction** (not player) based on Origin and Formation — institutional scaffolding predicts which way the crisis pushes.

**Certainty modifier:** −2 or +2 (GM determines). **Belief shape:** "The Church is [wrong/the only defence] — I will [find truth/defend faith]."

| Skill | Domain | Effect |
|---|---|---|
| ★ **Crisis-Forged Conviction** (unique) | Debate | +1D Argue for or against Church doctrine. The crisis destroyed indifference. |
| **Theological Depth** § | Investigation | +1D on Church doctrine, theology, institutional structure. |
| **Unshakeable** (unique) | Debate | Composure +3 when your specific religious position is under attack. |

---

## Thread-Adjacent Spark List Additions (Non-Practitioner Vocations)

Skills that activate when Thread phenomena occur near non-practitioner characters. Not practitioner abilities — cognitive, perceptual, or emotional responses from exposure.

| Vocation | Spark Skill Added | Effect |
|---|---|---|
| 3-CR2: Crown Soldier | **Uncanny Discipline** | Thread phenomenon during combat: unit ignores Morale penalty from Thread. +1D Morale checks in Thread presence. |
| 3-CH2: Templar | **Heresy Sense** | After prolonged anti-heresy service: +1D Attunement to detect active Thread operations in zone. |
| 3-HA2: Highland Miner | **Deep Wrong** | Underground: +1D Attunement to sense Thread instability or configurational wrongness in stone. |
| 3-LO2: Border Ranger | **Patrol Anomaly** | +1D Cognition to distinguish natural phenomena from Thread-related. |

---

## Skill Level Design Principle

| Level | Gate | Design |
|---|---|---|
| 1 | Any | Base effect |
| 2 | dice_bonus ≥ 3 + spark at Ob 3+ | Quantitative enhancement |
| 3 | dice_bonus ≥ 5 + spark at Ob 5+ | Qualitative unlock (new action or immunity) |

| Skill | Level 1 | Level 2 | Level 3 |
|---|---|---|---|
| Riposte § | 1 Defence die as counter-Strike at +1 TN | 2 dice counter-Strike at +1 TN | 2 dice at normal TN + Overwhelming counter → Disarm |
| Smooth Liar § | −1 strain using Obscuring | −2 strain | −2 strain + immune to Appraise revealing emotional state |
| Eagle Eyes § | Cognition roll reveals 1 opposing Phase 1 element | Reveal 1 at TN 6 | Reveal 2 + auto-identify counter-tactic |
| Dead Drop § | Covert channel, −1 Ob Intel ops | Channel persists 2 seasons before discovery | Permanent channel + mid-scene information passing |
| Approach Training | +1D Leap | +1D Leap + Partial no longer imposes +1 Ob on operation | +2D Leap + first operation at −1 Ob |
| Fortress Defender | +1D Defence in Fortified | +1D + DR +1 from fortification | +1D + DR +1 + once/battle Fortress Stand (cannot be routed this turn) |
| Grief-Driven Focus | +2D once/session on lost-Knot action | +2D + action doesn't consume Stamina | +3D + on Overwhelming, +1 Momentum AND GM reveals ghost sheet detail |

---

## Character Creation Summary

1. **Choose Origin** (Stage 1) → geography, culture, Certainty base, first Knot. 1 starting skill.
2. **Choose Formation** (Stage 2) → intellectual framework, Certainty modifier, second Knot. 1 starting skill.
3. **Choose Vocation** (Stage 3) → profession, faction, third Knot. 2 starting skills.
4. **Choose Catalyst** (Stage 4) → inciting event, starting Belief, campaign hook. 1 starting skill.
5. **Allocate attributes** (31 points). Recall determines equip slots and skill depth ceiling.
6. **Resolve Certainty** (base from Origin + modifiers).
7. **Name Knots** (three suggested; assign Close vs Distant).
8. **Write Beliefs** (Catalyst provides shape; Knots provide additional Belief material).
9. **Equip skills** (5 starting; Recall ≥ 5 equips all).
10. **Allocate History points** (per Recall cap per History).

---

## Example: Mira Sondhal (canonical test character, ED-143)

| Stage | Choice | Result |
|---|---|---|
| Origin | 1D: Southern Einhir Descendant + Deep South modifier | Born near Oastad. Inherited Resonance (+8 TS). Certainty 1. **Starting skill: Inherited Resonance.** Knot: grandmother who taught folk songs — practices alive in her hands, now in yours. |
| Formation | 2F: Practitioner Mentorship | Trained by a solitary practitioner. Certainty 1 → 0 (clamped). **Starting skill: Approach Training.** Knot: mentor, possibly connected to warden network, Coherence state unknown. |
| Vocation | 3-VA3: Einhir Antiquarian | Works Varfell's covert antiquities network. **Starting skills: Artefact Authentication, Black Market Contacts.** Knot: a dealer whose ethics differ and whose shared enterprise is shared risk. |
| Catalyst | 4E: The First Leap | Leap succeeded. Certainty 0 (already there). **Starting skill: Leap Scar.** Belief: "The wound at Askeheim is killing the rendered world — someone must make the factions understand before it is too late." |

**Result:** Practitioner-Scholar. TS 61 (canonical — 8 from Origin + growth through play). Certainty 0. Three Knots. 5 starting skills equipped (Inherited Resonance, Approach Training, Artefact Authentication, Black Market Contacts, Leap Scar). Recall 5 needed to equip all. Remaining spark list skills (Cultural Memory, Calamity Familiarity, Thread Perception, Philosophical Grounding, Einhir Lore, Post-Leap Clarity, Rendering Memory) develop through scene use.

---

## Open Editorial Items

- [EDITORIAL: ED-374 — Lifepath system requires user approval]
- [EDITORIAL: ED-375 — Skill effects provisional — Level 1/2/3 scaling needs simulation]
- [EDITORIAL: ED-377 — Intuitive Threadwork (3-RE3) + Co-Movement interaction: does folk practice trigger P-01?]
- [EDITORIAL: ED-378 — Confirm 3 Knots is the right lifepath count]
- [EDITORIAL: ED-379 — Can experienced characters take 2 Catalysts?]
- [EDITORIAL: ED-380 — Southern Einhir Descendant Deep South +8 TS: Leap-eligible with Formation 2F at session 1?]
- [EDITORIAL: ED-381 — Recall 1 = 1 equip slot: too punishing for low-Recall builds?]
- [EDITORIAL: ED-382 — Coherence equip slot loss: player choice vs auto-drop?]
- [EDITORIAL: ED-383 — Level 3 requiring Recall ≥ 5: intentional specialist gate?]
- [EDITORIAL: ED-385 — Starting skills 5: Recall ≥ 5 equips all. Confirm tension level]
- [EDITORIAL: ED-386 — Ashmarket modifier (1F): Einhir objects at node distance 3 — archaeological, not Thread-active, at RS 60]
- [EDITORIAL: ED-388 — Templar "Smite the Heretic": intra-party hostility intentional?]
- [EDITORIAL: ED-389 — Church Investigator occupational TS +3: canonical?]
- [EDITORIAL: ED-390 — War/Invasion specific events (Spartfell Incident, Templar Suppression, Ducal Border Clash): new setting content requires approval]
- [EDITORIAL: ED-391 — Lost Someone "ghost sheet": design-layer requirement or GM-reference recommendation?]
