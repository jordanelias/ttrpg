<!-- INFILL — prose/rationale extracted from character_histories_v30.md -->
<!-- Skeleton: character_histories_v30.md -->

# VALORIA — Character Histories: Lifepath System
## Status: CANONICAL — approved 2026-04-17 (editorial batch acceptance)
## Scope: Lifepath-based History generation with SaGa-style sparking, Recall-gated equip slots, skill levels 1–3
## Cross-references: params_core.md, combat_design_v1.md, social_contest_system_v2.md, mass_battle_v3.md, stage6_factions.md, threadwork_redesign_v25.md, calamity_radiation.md
## [EDITORIAL: ED-374 — Character Histories system. Setting/worldbuilding/character content — editorial gate applies.]
## Godot implementation: jordanelias/valoria-game (see docs/history_skill_integration.md)
## Structure
Character creation moves through **four lifepath stages**. Each stage answers a biographical question and grants one History.
**Starting skills: 5 total.** All start at Level 1 and auto-equip. With Recall ≥ 5 at creation, all fit. Recall 3 forces loadout choices from session 1.
**Sub-modifiers:** Origins, Formations, and Vocations that span multiple geographic or institutional variants include sub-modifiers — a secondary selection that adjusts one skill, one Knot detail, or one narrative element. Sub-modifiers do not add a new History; they specialise the existing one.
- **Equip slots:** `max_equipped = Recall` (1–7). All sparked skills retained permanently; only Recall-many active at any time. Swap loadout between scenes.
- **Skill depth:** Skills have Levels 1–3. Level 2 requires History dice_bonus ≥ 3; Level 3 requires dice_bonus ≥ 5. Recall caps dice_bonus, so Recall indirectly caps max level.
**Certainty:** Stage 1 sets the baseline. Later stages modify it. Final Certainty recorded after all four stages.
## STAGE 1: ORIGIN — Where were you born and who raised you?
Origin establishes geographic and cultural foundation. **Grants 1 starting skill** (first skill listed). Remaining skills on spark list.
### 1A. Crown Heartland Child
Born in the eastern lowlands — Valorsplatz, Kronmark, Feldmark, or Stillhelm. The Crown heartland is the granary that feeds the peninsula. Hafenmark cannot feed itself (ED-054). Without Feldmark and Kronmark, the peninsula starves. You grew up understanding food as politics — not abstractly but as the rhythm of your family's labour.
**Who raised you:** A family embedded in the Crown's civil order. Markets on Crown coin, roads Crown-maintained, disputes to Crown magistrates.
**Narrative impact:** You were raised inside the system everyone else is trying to influence, control, or overthrow. You carry an unconscious assumption that the Crown's order is the natural state of things.
### 1B. Highland Born (Hafenmark)
Born in the northwestern highlands — Gransol, Rendstad, Spartfell, or Halvarshelm. Landlocked, mineral-rich, Swiss-character territory that Altonia squeezed hardest during the occupation.
**Who raised you:** Highland family — miners, herders, artisans, or minor functionaries. Tight community, procedural, suspicious of outsiders. The occupation ended generations ago but its shadow shapes everything: emphasis on law, distrust of charismatic leaders, institutional stubbornness.
**Starting Certainty:** 4 (Average Valorian). The Church is present but culturally secondary to Hafenmark's constitutional identity.
**Knot:** A community elder or extended family figure who embodies constitutional values. They taught you that procedure is the wall between civilisation and tyranny. When Baralta invokes Sovereign Authority Doctrine, this person either celebrates (law triumphant) or worries (overreach by a single ruler).
**Narrative impact:** Law over personality, procedure over charisma. Strength against demagogues; blindness to action that can't be procedurally justified.
### 1C. Fjord Child (Varfell)
Born on Varfell's western coast — Sigurdshelm, Halvardshelm, Oastad, or Grauwald. Norwegian-character fjord communities connected by sea, separated by mountains.
**Who raised you:** Fjord family — sailors, herders, fisher-folk. Maritime, isolated, self-sufficient. The Einhir presence is strongest here — folk practices survive in the southwest as living tradition.
**Knot:** A community member — fisher, elder, childhood rival who became a friend. They represent the small-scale world that factional politics threatens. The Maritime Forgetting blocks the southern sea route and your community feels this as economic isolation that can't be rationally explained — you know the route doesn't work, but you can't say why.
### 1D. Southern Einhir Descendant
Born in communities closest to the Southernmost — southern Oastad, settlements ringing Askeheim, hamlets at node distance 1-2.
**Who raised you:** An Einhir-descendant family. Not practitioners — people whose grandparents' grandparents spoke a different language, practised different rites. **245 years of Church institutional suppression** — heresy declarations, text confiscation, practice prohibition, forced conversion of naming conventions — eroded most of this inheritance. What survives does so because it was encoded as folk habit: songs without translatable lyrics, ritual gestures at births and deaths, persistent unease about the Solmund narrative that cannot be articulated. This is not the Forgetting (a metaphysical mechanism localised to Askeheim per calamity_radiation.md). This is cultural destruction by institutional authority, sustained across ten generations, partially successful, never complete.
**Knot:** A grandmother or elder who carries Einhir tradition. They taught you the songs, the gestures. They could not explain why they matter. They may be dead — and what they gave you is the only record that they existed as carriers of something the Church tried to erase.
### 1E. Himmelenger Child (Church Territory)
Born and raised in Himmelenger — Cathedral city, the Church's seat, the theological centre. Bells, scripture, liturgy, towering architecture of institutional faith.
**Who raised you:** A family within the Church's cultural orbit. Himmelenger is not a city with a cathedral; it is a city that IS a cathedral. Every institution operates under the Church's moral framework.
**Starting Certainty:** 5 (Orthodox). The Church's account of reality is not something you were taught — it is the air you breathed.
### 1F. Valorsplatz Underclass
Born in the capital's lower districts. Not a generic urban poor — a resident of specific Valorsplatz geography.
**Who raised you:** Single parent, extended working family, or the street itself. The capital's wealth flows through your neighbourhood without stopping.
**Starting Certainty:** 3 (Questioning). Neither institution has earned your faith. Neither has lost it entirely.
**Modifier: Tideward (river/harbour district)** — The flood-prone lower district between the river and the eastern harbour. Schoenland ships dock at your doorstep. Niflhel's dockworker arm operates the same routes you grew up on.
- *Tideward:* A sibling who works Niflhel's dockworker arm and doesn't know you know — or who knows and pretends not to. Their safety depends on your silence; your conscience depends on not examining what they move.
- *Ashmarket:* A Church charity teacher who taught you to read and whose faith you both respect and resent. They believe the Church saved you. You believe the Church demolished the civilisation whose ruins you grew up on.
### 1G. Border Settlement Child
Born in northern border territories — Lowenskyst, Spartfell, or Halvarshelm. Communities that exist because a fortress needs people to supply it.
**Who raised you:** Military family or military-adjacent — blacksmiths, provisioners, farriers. The border is a physical presence. You grew up watching the mountain passes.
**Starting Certainty:** 4. The Löwenritter are a visible presence — the military order shapes border life as much as the Crown or Church.
**Knot:** A garrison soldier or parent who served at the border — and who specifically remembers what it was like when Altonian forces last probed the pass. They carry a warning that the rest of the peninsula doesn't take seriously enough. When Institutional Pressure rises, they write you letters that grow increasingly urgent.
### 1H. Displaced — No longer generic
Family displaced during the Altonian occupation's aftermath — post-liberation resettlement, collaborator property seizure, destroyed communities.
Knot: A member of another displaced family whose trajectory diverged from yours — they joined Niflhel, or the Restoration, or the Crown army. You share landlessness and nothing else.
Family destroyed by a Calamity event — Shifting Object, rendering failure, threadcut being encounter at the southern edge.
Starting Certainty: 2. Starting skill: ★ **Scarred by the Unreal** (unique) — Immune to Composure loss and surprise-round penalties from Thread phenomena. Thread Sensitivity +3.
Knot: Surviving family member who witnessed the same event and accepted the Church's explanation (natural disaster). Your insistence that something else happened has strained the relationship. They think you're traumatised. You think they're in denial.
Knot: A fellow orphan who chose a different path. The bond is pre-institutional — it exists because you shared a dormitory, not a worldview.
## STAGE 2: FORMATION — How were you educated or shaped?
### 2A. Church Schooling
The only widespread education infrastructure on the peninsula. Literacy, numeracy, scripture, Solmund history.
**Knot:** School mentor who invested in you personally. Whether you now agree with what they taught defines a live tension. They shaped your intellectual development — and they shaped it within the categories the Church provides.
### 2B. Ducal Household Education
Educated as part of a noble or ducal household's retinue — Crown, Hafenmark, or Varfell. Specify which household (affects worldview: Crown = virtue ethics, Hafenmark = proceduralism, Varfell = consequentialism).
**Knot:** A fellow student — someone your age who shared Formation. You may now serve the same faction or opposing ones. The bond was formed before politics intervened.
### 2C. Guild Apprenticeship
Apprenticed to a master. Trained in a specific craft and socialised into the Guilds' moral relativism — value determined by skill, not birth or doctrine.
**Knot:** Your master craftsperson. Professional standards, craft values, the specific relationship between someone who knows and someone who is learning. Whether kind or demanding, the most formative relationship of your adolescence.
### 2D. Self-Taught / Empiricist
No formal education. The Church controls formal education; the Guilds provide trade apprenticeships; ducal households educate retinues. You exist **outside the peninsula's entire epistemological apparatus.** What you learned, you learned by observing the world directly — empirical, fragmented, uncontaminated by institutional framing.
**Certainty modifier:** −1 regardless of starting value. Without institutional education, no framework reinforces any Certainty level. Your Certainty is inherently unstable — it moves in either direction more easily because nothing anchors it.
**Knot:** A specific person who showed you something that contradicted institutional reality — a midwife who treated patients the Church said were cursed, a veteran who told you the occupation ended differently than official history claims. Their specific knowledge gave you reason to trust observation over authority.
### 2E. Military Training
Educated through military service — Crown army, Hafenmark ducal guard, Varfell household troops, or Löwenritter squire training. Specify which institution (affects military culture).
**Knot:** Training partner, drill instructor, or fellow recruit. Bonds formed under shared physical hardship. This person knows what you can endure because they endured it beside you.
### 2F. Practitioner Mentorship
Educated by a Thread practitioner — warden, solitary practitioner, or scattered practitioner community. Philosophical and practical preparation for Thread practice. You may not have Leaped yet.
### 2G. Monastic Seclusion
Educated in a remote contemplative house — not the urban seminary but an isolated monastery. Quiet, rigorous, divorced from political reality.
**Knot:** A fellow monk or abbot/abbess. They represent the quality of attention monastic life produces — and the question of whether that attention reveals truth or illusion.
## STAGE 3: VOCATION — What were you trained to do?
**Grants 2 starting skills** (★ marked). At least 1 of 2 must be unique. Remaining skills on spark list.
**Vocation determines faction affiliation.** Contradictions between Origin/Formation/Vocation produce character tension — a Crown Heartland Child with Practitioner Mentorship and a Church Vocation is a character whose biography is a argument with itself.
### Crown Vocations
### Church Vocations
### Hafenmark Vocations
### Varfell Vocations
### Guild Vocations
### Niflhel Vocations
### Restoration Movement Vocations
### Löwenritter Vocations
### Cross-Factional Vocations
## STAGE 4: CATALYST — What happened that put you on this path?
**Grants 1 starting skill** (★ marked). Remaining skills on spark list. Produces a starting Belief shape.
### 4A. Witnessed Something Impossible
**Canon note on Forgetting:** If the event occurred outside Askeheim (node distance 1+), the Forgetting does not apply — your memory persists because rendering didn't erase it. If at Askeheim (node distance 0), your retention means your TS was high enough for partial retention per the Forgetting Check (stage4_southernmost), which is diagnostically significant.
### 4B. Betrayed by Your Institution
### 4C. Lost Someone
A Close Knot died, disappeared, or was taken. **Anti-fridge clause:** The GM maintains a hidden "ghost sheet" for the lost person — Beliefs, faction affiliations, most important relationships. Knot Memory draws from this sheet. The lost person continues to influence the campaign.
### 4D. Recruited — Faction-Specific
**Belief shape:** "[Recruiter] believes I can [specific task] — I will prove them [right/wrong/something unexpected]."
### 4E. The First Leap
### 4F. War / Invasion — Specified
**4F-i. Spartfell Incident** — Altonian probe force crossed the NW pass 3-5 years pre-campaign. Repelled at Spartfell.
**4F-ii. Templar Suppression** — Church deployed Templars against a southern community suspected of Einhir revival 2-4 years pre-campaign. [ED-390: new setting event — requires approval.]
**4F-iii. Ducal Border Clash** — Hafenmark-Varfell territorial dispute over T10-T11 border escalated to armed skirmish 5-8 years pre-campaign.
### 4G. Religious Crisis
Faith broke or deepened in a way that can't be undone. **GM determines direction** (not player) based on Origin and Formation — institutional scaffolding predicts which way the crisis pushes.
## Thread-Adjacent Spark List Additions (Non-Practitioner Vocations)
Skills that activate when Thread phenomena occur near non-practitioner characters. Not practitioner abilities — cognitive, perceptual, or emotional responses from exposure.
## Skill Level Design Principle
## Character Creation Summary
4. **Choose Catalyst** (Stage 4) → inciting event, starting Belief, campaign hook. 1 starting skill.
## Example: Mira Sondhal (canonical test character, ED-143)
**Result:** Practitioner-Scholar. TS 61 (canonical — 8 from Origin + growth through play). Certainty 0. Three Knots. 5 starting skills equipped (Inherited Resonance, Approach Training, Artefact Authentication, Black Market Contacts, Leap Scar). Recall 5 needed to equip all. Remaining spark list skills (Cultural Memory, Calamity Familiarity, Thread Perception, Philosophical Grounding, Einhir Lore, Post-Leap Clarity, Rendering Memory) develop through scene use.
## Open Editorial Items
- [EDITORIAL: ED-377 — Intuitive Threadwork (3-RE3) + Co-Movement interaction: does folk practice trigger P-01?]
- [EDITORIAL: ED-380 — Southern Einhir Descendant Deep South +8 TS: Leap-eligible with Formation 2F at session 1?]
- [EDITORIAL: ED-390 — War/Invasion specific events (Spartfell Incident, Templar Suppression, Ducal Border Clash): new setting content requires approval]
- [EDITORIAL: ED-391 — Lost Someone "ghost sheet": design-layer requirement or GM-reference recommendation?]
