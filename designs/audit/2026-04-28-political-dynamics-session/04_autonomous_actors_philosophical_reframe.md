<!-- [PROVISIONAL: 2026-04-28 session — d964fd13158349fa] -->
<!-- STATUS: PROVISIONAL — design exploration, not canonical mechanic -->
<!-- TITLE: NPCs as Autonomous Actors: Philosophical Reframe -->
<!-- POSITION IN ARC: see designs/audit/2026-04-28-political-dynamics-session/00_session_index.md -->
<!-- VETTING: see 07_armature_system_vetting.md for canonical framework assessment -->

# NPCs as Autonomous Actors: Reframing the Political System

## The Core Shift

The previous proposals — even the revised v2 — still treated NPCs as *computed entities*. They had RP balances, Alignment Scores, AI priority trees. They evaluated inputs and produced responses. The player was the protagonist; NPCs were sophisticated reactive systems.

This document reframes NPCs as **persons who happen to be in the game**. Persons have feelings. Persons have opinions about each other. Persons have private lives the player will never see. Persons remember things. Persons are sometimes wrong about themselves. Persons pursue projects that have nothing to do with the player.

The player is not the protagonist of NPC lives. The player is one actor in a political environment populated by other actors who would exist whether the player existed or not.

This shift has mechanical consequences that the previous proposals miss.

---

## What Changes: The NPC Inner-Life Architecture

Each named NPC carries five inner-state structures beyond the existing Conviction/Belief/Disposition framework:

### 1. Concerns (Active Questions)

A Concern is a question the NPC is currently trying to answer. Concerns are not computed — they are *seeded* by events and persist until resolved.

Examples of Concerns the engine might generate:
- "Why did Almud agree to the Varfell alliance?" (Confessor, after the treaty)
- "Is Torben ready to rule, or am I deluding myself out of grief?" (Marshal Ehrenwall, mid-campaign)
- "Has my brother forgiven me for the Eshlund affair?" (any NPC, persistent backstory concern)
- "Is the player loyal to the Crown, or are they cultivating Varfell contacts?" (Spymaster, after observed cross-faction interaction)

Concerns drive NPC behavior. An NPC with the Concern "Why did Almud agree to the Varfell alliance?" will: investigate (Read the player who supported the treaty), conversation (approach other NPCs who might know), worry (mood shifts toward anxious during Outreach scenes). The Concern is the *reason* for the action, not just a stat trigger.

Concerns resolve when the NPC reaches a tentative answer. The answer may be wrong. The Confessor investigating Almud's motives might conclude "the player has been whispering heresy to the king" — which is false but actionable. The Confessor's subsequent behavior is shaped by this false belief until something confronts them with evidence.

**Mechanically:** Each NPC carries 1–3 active Concerns. Each Concern has a "salience" value (how much it shapes current behavior) that decays over time if no events touch it. When an NPC has scene actions available (Outreach, intelligence, council attendance), Concerns are evaluated as primary motivators alongside the existing AI priority tree.

### 2. Projects (Personal Agendas)

A Project is something the NPC is trying to *accomplish* over multiple seasons, independent of the player and faction-level imperatives.

Each named NPC has 1–2 active Projects at any time. Projects are seeded at character creation and replaced as they complete or fail. Examples:

- **Marshal Ehrenwall:** "Train Torben to be a war-leader before Almud dies." (Multi-season Project. Generates: clandestine meetings with Torben, requisitioning training resources, building Disposition with the prince.)
- **Cardinal Klapp:** "Find the scholarly Thread evidence that will let me confront Himlensendt without breaking my oath." (Long-term Project. Generates: Investigation actions in libraries, Knot-mediated counsel attempts with sympathetic NPCs, careful avoidance of public confrontation.)
- **Vossen:** "Get my movement recognized as a legitimate political body before my health fails." (Personal urgency Project. Generates: alliance-seeking with sympathetic Crown NPCs, settlement organizing, willingness to make tactical compromises she'd refuse otherwise.)
- **An obscure inner-circle NPC:** "Find a husband for my niece who isn't a Hafenmark fortune-hunter." (Private Project. Generates: occasional social scenes with eligible bachelors, distraction from political duties when family pressures peak.)

Projects produce *agency* — NPCs initiate actions to advance their Projects without player involvement. The player can support, oppose, exploit, or be irrelevant to each Project. The NPC's response to the player is shaped significantly by whether the player has helped or hindered their Projects.

**Mechanically:** Projects are tracked as multi-step state machines with seasonal evaluation. When an NPC has discretion in their AI priority tree (a tiebreaker, an unconstrained scene action), they advance their Project. Project progress is partly visible to the player through observation (Read action can detect what an NPC is *trying to do*, not just their current Disposition).

### 3. Opinions (Characterized Assessments)

An Opinion is what an NPC *thinks* of another NPC or the player — but as content, not as a number.

Each NPC carries 2–4 strong Opinions about politically relevant others. Opinions have:

- **Subject** (the person being assessed)
- **Affect** (positive, negative, mixed, or specific complex emotion like "respectful but wary")
- **Story** (the narrative the NPC tells themselves about why they hold this Opinion)
- **Evidence** (specific events or observations the NPC associates with this Opinion)

Example Opinions Marshal Ehrenwall might hold:

- *About Almud:* Affect: respectful, grieving. Story: "He was a great king once. The crown is too heavy for him now, and he knows it." Evidence: the way he hesitates in council, the way he asks her opinion more often than he used to, the moment three years ago when he confessed he was tired.
- *About the Confessor:* Affect: wary, slightly contemptuous. Story: "He believes everything he says, which makes him more dangerous than any liar." Evidence: the Heresy Investigation against the librarian Edda, his unyielding sermon at the Solstice, his refusal to consider that the Eshlund border massacre was anything other than divine providence.
- *About the player (Crown Lieutenant):* Affect: provisionally trusting, watchful. Story: "Promising. Energetic. I don't know yet if they understand what we're up against, but they're listening, which is more than most." Evidence: their handling of the Vaynard delegation, their question about the Riskbreakers in their first council, their visible distress at the report from Stillhelm.

Opinions are referenced in dialogue. When the Marshal speaks about the player to another NPC, she doesn't say "Disposition +2." She says "Promising, but watch them." The Opinion is the source.

Opinions *change* through events, but not easily. Strong Opinions exhibit hysteresis. A player who does one impressive thing doesn't immediately reset a long-held wary Opinion — but a player who does *consistent* impressive things over seasons gradually rewrites the Story.

**Mechanically:** Opinions are stored as semi-structured records. Engine logic that generates dialogue, evaluates social actions, or processes NPC decisions consults Opinions when they apply. The same player action produces different consequences with different NPCs because each NPC interprets the action through their own Opinion of the player.

### 4. Mood (Current Emotional State)

Mood is the NPC's short-term emotional weather. It shifts faster than Opinions and affects decision tiebreakers.

Mood states (not exhaustive):

- **Steady** (default)
- **Anxious** (heightened threat sensitivity, more likely to choose conservative options)
- **Confident** (lowered threat sensitivity, more likely to take political risks)
- **Grieving** (slowed reactions, withdrawal from social engagement, occasional unexpected vulnerability)
- **Vindicated** (recently saw a held belief confirmed, more aggressive in pursuing Project)
- **Humiliated** (recent public loss of status, retaliation-prone or withdrawal-prone depending on personality)
- **Distracted** (private life concerns, less attentive to political dynamics, more likely to make mistakes)
- **Resolved** (decision recently made, less open to persuasion)

Mood changes based on events:
- A successful Domain Action proposal → Confident for 1–2 seasons.
- A treaty contradicting their Conviction → Anxious or Humiliated depending on whether they advocated against it.
- A Knot partner's death → Grieving for 2–4 seasons.
- A Conviction confrontation in social Contest, regardless of outcome → Distracted for 1 season.

Mood affects NPC behavior at the margin. An Anxious Cardinal Klapp will refuse to attempt the scholarly investigation his Project requires this season. A Vindicated Vaynard will push for an aggressive Domain Action that a Steady Vaynard would defer. The same NPC, same conditions, different mood = different outcome. **This is where game-state determinism breaks.**

**Mechanically:** Mood is one of 8 states. Mood modifies AI priority tree evaluation by ±1 to specific action types. The current Mood is observable through Read action (detects "current emotional state" per fieldwork §5.2) and through dialogue tone in scenes.

### 5. Memories (Specific Events with Affect)

Memories are events the NPC remembers with attached emotional weight. Memories are not infinite — each NPC retains 5–10 high-salience Memories at any time. New high-salience events displace older ones (or merge with them — "another disappointment from the Crown" rather than retaining separate disappointments).

Memories influence Opinions and Concerns. The Confessor's Opinion of the player is partly built on Memories: "The player attended the Solstice service. The player asked a thoughtful question about the Heresy Trials. The player was seen entering the Varfell embassy at dusk."

Memories have a *valence* and a *strength* that decays slowly. Strong Memories don't disappear — they recede into the NPC's background context. The Confessor will remember "the player attended the Solstice service" for the entire campaign, even if it stops being salient after the second season.

**Why this matters:** Memories give NPCs continuity. An NPC the player betrayed in Year 2 remembers that betrayal in Year 5. They may have forgiven the player publicly. They may even have rebuilt Disposition. But the Memory persists, and it shapes their tiebreaker decisions in ways the player can't directly access.

**Mechanically:** Memories are timestamped event records with affective tags. Engine logic that evaluates Opinion shifts, scene generation, or NPC dialogue tone consults relevant Memories. A player who acts consistently against a Memory's emotional weight (e.g., consistently treating a wary NPC well) gradually buries the Memory — but the burial is slow.

---

## What This Changes in Each Proposal

### P-1 Reframed: Regard as Opinion, Not Score

The RP balance was a number. Replace it with **mutual Opinions**. Each named NPC holds an Opinion about each other politically-relevant NPC, with affect, story, and evidence.

**What this changes practically:**

A "rivalrous" relationship is not RP −4 — it's that NPC-A's Opinion of NPC-B has affect "contemptuous", story "He thinks bookishness is a substitute for spine. He'll fold the moment Hafenmark applies real pressure", and evidence "his weak position on the Stillhelm crisis, his refusal to back the eastern campaign, the way he avoided me at the Cardinal's funeral."

The mechanical effect of this Opinion is similar to RP −4 — NPC-A obstructs NPC-B's projects, badmouths him to the player, may form a Bloc against him. But the *texture* is different:

- The player who Reads NPC-A receives the Opinion as content: "She thinks the Cardinal is a coward. She traces it back to the Stillhelm crisis." This is *intelligence the player can use*. They can probe NPC-B about Stillhelm, present NPC-B with an opportunity to demonstrate spine, or use the rift strategically.

- NPC-A's actions toward NPC-B are *legible*. When NPC-A obstructs NPC-B's Domain Action, the obstruction has a reason that other NPCs can interpret. NPC-C, observing the obstruction, evaluates whether NPC-A's stated reasoning is fair (which might shift NPC-C's own Opinion).

- NPC-A's Opinion can be *wrong*. Her assessment of NPC-B as a coward may be unfair. If the player engineers a situation where NPC-B publicly shows spine (perhaps even at cost to NPC-A's interests), NPC-A's Opinion has to update. The update is slow — she'll first try to explain it away ("he was forced into it") — but consistent contradictory evidence eventually rewrites the Story.

**The political consequence:** Reconciliation between rivals is no longer a Reconcile action with an Ob. It's the *gradual rewriting of an Opinion through accumulated evidence*. The player who wants to bring NPC-A and NPC-B into productive cooperation must understand *why* NPC-A holds her Opinion of NPC-B, and engineer events that contradict the Story she tells herself.

### P-2 Reframed: Promotion as Felt Event

Promotion is not a stat threshold — it's a moment that *feels different* to each affected NPC.

When the player is promoted to Standing 4 over Lt. Hafgrim, who expected the position:

- Hafgrim's Mood shifts to Humiliated. His Opinion of the player gains affect "envious, but trying to be fair" with story "They're younger than me, less experienced, and I taught them half of what they know. Yet here we are." Evidence: this specific event.
- A Memory is created: "The day the player was promoted over me." High salience, slowly decaying.
- A Concern is generated: "Was I passed over because of my age, or did I fail somewhere I haven't identified?" This Concern drives Hafgrim's behavior — he investigates, he asks discreet questions of trusted colleagues, he reviews his own recent decisions with painful scrutiny.
- His Project may shift. If his prior Project was "Earn Standing 5 before retirement," he may pivot to "Determine whether this institution still rewards merit, or whether I should leave." Both Projects produce different actions over the next 2–4 seasons.

The player who knows about Hafgrim's situation (through Read or through other NPCs gossiping) has options that aren't reducible to "increase Disposition":

- Acknowledge the slight publicly. ("I would not have been ready for this without your mentorship.") This addresses Hafgrim's Concern by validating his role. The Memory remains but its affect softens.
- Privately offer Hafgrim a meaningful sub-command. This addresses his Project by giving him forward momentum.
- Ignore Hafgrim's situation entirely. This is permitted but Hafgrim's slow drift away from the institution is a political consequence the player will face later.

**No proposal-mechanic specifies "say the right thing to soothe a humiliated colleague." The player figures out what to do based on their understanding of who Hafgrim is.**

### P-3 Reframed: Treaty as Personal Trauma

The treaty does not produce Alignment Scores. It produces *individual reactions* shaped by each NPC's Conviction, Mood, Projects, and Opinions.

When the Crown-Varfell alliance is signed:

- **The Confessor.** Reaction sequence: shock → anger → search for explanation → identification of explanation. He reads the treaty draft, his hands shake (Mood: Anxious). He asks his secretary to confirm the signatures (Anxious Mood seeking certainty). That night, he sits in his chapel and prays for guidance (off-screen private life). The next morning, he has constructed an explanation: Almud has been deceived. Someone influenced him. The Confessor's Concern becomes "Identify the influence and remove it." His Opinion of Almud shifts (affect "betrayed by, or betrayed for?" — story "He would not have done this on his own. Someone got to him.") Importantly, his Opinion of Almud does not become hostile — it becomes *protective*. He believes the king is being manipulated, and his duty is to save him.

This is fundamentally different from the v2 model where Alignment Score −2 → "Active opposition." The Confessor is not opposing Almud. He is opposing whoever he believes manipulated Almud. The player may be his target, even if the player wasn't centrally involved.

- **Marshal Ehrenwall.** Reaction sequence: cold pragmatic assessment → identification of military implications → recognition that this might actually be useful → suppressed concern about Löwenritter response. Her Mood is unchanged (Steady). Her Opinion of Almud might subtly improve (affect "more decisive than I thought, lately"). But her Project (training Torben) is now harder — Torben has to learn to navigate this alliance, which means she has to teach him about Varfell, which she knows little about. New Concern: "Who can teach Torben about Varfell without compromising him politically?" This may lead her to seek out Maret Uln through intermediaries — a cross-faction contact she would never have considered without the treaty.

- **Cardinal Klapp.** Reaction sequence: emotional ambiguity → tentative interest → professional caution. Klapp is a scholar who has long suspected that the Church's hardline position on Varfell is theologically overdetermined. The treaty creates space for him to pursue his Project (find scholarly Thread evidence) more openly — Varfell scholars may now be politically tolerable contacts. His Mood shifts toward Confident. But he must hide this Mood from the Confessor, who would interpret his interest as confirmation of his worst fears about Klapp.

Three NPCs in the same faction, same treaty, three entirely different inner reactions. Each produces different downstream behavior.

### P-4 Reframed: Succession as Felt Time

NPCs do not experience succession as a clock value. They experience it as the slow loss of a specific person and the slow approach of an unknown future. Both of these are emotional states, not numerical conditions.

For each NPC who has served the aging leader:

- They watch the leader age. They notice things the player wouldn't notice. The Marshal sees Almud's hands tremble during a council session. She remembers when those hands were steady. She files this Memory away.
- They imagine the future. Each potential successor has *a face* in their imagination. The Marshal imagines Torben as king and feels both hope and fear. Hope because she has trained him and believes in him. Fear because she knows his weaknesses and worries about who else will be in his ear when she is gone.
- They begin acting on the imagined future. Not strategically positioning — *actually preparing*. The Marshal begins teaching Torben specific lessons about specific advisors. "When this man tells you something, ask yourself who else has spoken to him this week. He repeats what he hears most recently." This is mentorship, not political maneuvering — but it produces the political consequence (Torben becomes harder to manipulate after he becomes king) without being "Succession Positioning."

The player who has Disposition +3 with the Marshal and asks her about Torben gets actual content: "He has his father's instincts and none of his father's caution. He is afraid of Ehrenwall — yes, of me — because I knew his mother. He needs to learn to be afraid of fewer people."

**The player engaging with succession is not navigating a clock. They are participating in the lives of people who are afraid for the future and trying to do something about it.**

### P-5 Reframed: Discovery as Personal Failure

When the player's cross-faction contact is discovered, the faction leader's response is shaped by their personality, their Opinion of the player, and their current Mood — not by a Demand-scene template.

**Almud (Virtue Ethics, paternal, Mood: Anxious from succession concerns):** discovery produces *grief*. He liked the player. He had hopes. He summons them, but the meeting is not a confrontation — it is a slow, painful conversation. "I want to understand. Help me understand." His Disposition shift is not −1 — it is the beginning of a Memory that will require years to overcome. He may give the player a chance to explain, but the Opinion he forms in this moment will shape every subsequent interaction.

**Baralta (Categorical Imperative, formal):** discovery produces *constitutional concern*. The contact is not just disloyal — it is a category violation. Her response is procedural, not emotional. The player faces a hearing, possibly with Hafenmark legal advisors present. Baralta's Opinion of the player gains affect "useful but unreliable" — useful because they have demonstrated initiative, unreliable because they have demonstrated inability to maintain institutional boundaries. She will employ them for tasks where the boundaries are clearer, and never for tasks where loyalty is paramount.

**Himlensendt (Divine Command, Mood: Vindicated by recent CI advance):** discovery produces *theological certainty*. The player's behavior confirms his suspicion that the Crown court has been infiltrated by heretical sympathies. His response is not a Demand scene — it is the opening of a Heresy Investigation. The investigation has its own AI logic, its own NPC dynamics (Cardinal Klapp may be assigned to investigate, and Klapp may secretly hope the investigation produces nothing because his Project requires Crown-court tolerance), and its own pacing.

The same player action (discovered cross-faction contact with Vaynard) produces three categorically different consequences not because of stat differences but because of *who is doing the responding*.

### P-6 Reframed: Influence as Psychological Pressure

Insinuate operations are not stat reductions. They are *manufactured experiences* that the target NPC has to interpret.

When the player Insinuates against Spymaster Kolbrun (target relationship: Kolbrun's Disposition with Almud), the operation is implemented as: the player engineers a situation in which Kolbrun has to deliver Almud bad news while Almud is in a bad Mood. The bad news leads to Almud reprimanding Kolbrun. Kolbrun feels the reprimand was unfair. Kolbrun's Memory of the moment is "Almud questioned my competence in front of two junior officers." Kolbrun's Opinion of Almud begins to shift — slowly, with hysteresis, but in a specific direction.

The same Insinuate against the same target on the same Disposition can be implemented differently:
- Through false rumor (Almud hears that Kolbrun has been seeking patrons elsewhere)
- Through engineered failure (Kolbrun is given an intelligence task that the player ensures fails, making her appear less competent)
- Through staged disrespect (the player publicly questions Kolbrun's recent recommendation in council, undermining her authority)

Each implementation creates *different* Memories and engages *different* parts of Kolbrun's inner life. The player chooses the implementation based on what they know about Kolbrun (gathered through Read and Appraise).

Kolbrun's response to the manufactured experience is shaped by her *personality*. She is high-Cog, Conviction Autonomy, with active Project "Discover the identity of the surviving Niflhel-successor brokers." Her response to feeling Almud is questioning her competence is not collapse — it is to redouble her independent operations, accept fewer formal taskings, and begin building plausible-deniability infrastructure for her Project. She may, in fact, *appear* more loyal in the short term (she avoids the council where Almud might question her again) while *actually* drifting further from institutional control. The Insinuate produced behavior the player wanted (decreased Almud Disposition) and behavior the player didn't anticipate (Kolbrun building a private operational base the player can't access).

**Outcomes are not predictable from inputs because NPCs interpret events through their own minds.**

### P-7 Reframed: Settlement as Community

A settlement's resilience under threat is the choices its inhabitants make. The mayor, the merchant, the priest, the militia captain — each has their own Conviction, their own Project (smaller in scope than national NPCs but real), their own Opinion of the governor.

When a hostile force approaches:
- The mayor is afraid for his children. His Project is "Survive this. Keep the town intact for the next generation." His Opinion of the governor (built over the seasons of the player's governance) shapes whether he believes the governor will defend them or use them. If the governor has shown personal courage, the mayor will organize defense. If the governor has been distant, the mayor will negotiate independently.
- The merchant has ledgers. Her Project is "Preserve my position as the major creditor of the regional economy." Her Opinion of the governor is shaped by whether the governor has respected her commercial interests. If yes, she funds the militia. If no, she ships her gold east before the attack arrives.
- The priest believes God is testing the community. Their Project is "Be present at the moment of greatest need." Their behavior is largely indifferent to the governor's governance — they will preach courage regardless — but the *content* of the preaching depends on whether they believe the governor is righteous or fallen.

The settlement's resilience emerges from these individual choices. **The player's governance is not building a stat — it is building Opinions in specific people whose subsequent choices will shape outcomes.**

### P-8 Reframed: Drift as Visible Lives

A Reason-aligned governor in a Church-controlled settlement does not produce abstract Framework Tension. They produce *visible behavior* that local Faith-aligned NPCs *experience*:

- The local priest notices that the governor never attends Solstice services. After the third missed service, the priest's Opinion of the governor gains evidence: "absent at the holy days, present at the lecture circuits." Affect: "wary, beginning to move toward distrustful."
- The parish school stops receiving the customary autumn tithing supplement. The schoolmaster (a minor NPC the player may never have met) feels the slight personally — he had three students who needed those funds for winter. He talks to the priest. The Opinion network spreads through gossip channels.
- A scholarly debate is hosted in the governor's residence. Local Faith-aligned NPCs hear about it. Some attend out of curiosity. Some attend with hostile intent. One — a junior cleric named Brother Eyvind — finds the arguments unsettling and goes home to pray. His Mood shifts to Anxious. His Concern becomes "Are these arguments true?" His Concern leads him to read books his bishop would disapprove of. His secret Project becomes "Determine for myself what is true," which may produce unexpected outcomes — Eyvind may eventually become a Reason-converted asset, or he may panic and report the governor to the Church.

The settlement is not "drifting." It is *changing* in granular, person-by-person ways that produce different outcomes depending on which specific people experience which specific events.

---

## What the Player Sees vs. What the Engine Computes

### What the Engine Holds

For each named NPC at any time:
- Conviction (existing)
- Beliefs (existing)
- Disposition with player (existing)
- Conviction Scars (existing)
- Arc state (existing)
- **Concerns** (1–3 active questions)
- **Projects** (1–2 active goals)
- **Opinions** (2–4 characterized assessments of others)
- **Mood** (1 current state)
- **Memories** (5–10 high-salience event records with affect)

### What the Player Experiences

The player never sees the engine's data structures. They experience NPCs through:

1. **Dialogue with reference content.** When an NPC mentions another NPC, the dialogue references the speaker's Opinion. ("I respect Ehrenwall. She has been the only honest voice in council these past years.") The player learns about NPC-NPC relationships through what NPCs say about each other.

2. **Observable behavior.** NPCs initiate actions based on Concerns and Projects. The player notices: the Cardinal has been spending unusual time in the archives; the Marshal has been seen with Torben at unusual hours; the Spymaster is cancelling routine briefings. These behavioral patterns are *legible* — the player can investigate (Read, Appraise, Investigation) to understand what the NPC is up to.

3. **Mood-shifted scenes.** The same NPC engages differently with the player depending on their current Mood. An Anxious Confessor receives the player coldly; a Steady Confessor receives them warmly. The player learns to read the mood and adapt.

4. **Outreach with subjective framing.** NPC-initiated scenes don't say "the Confessor wants to discuss the treaty." They say "the Confessor has asked you to come to the chapel after evening prayers. He seems weary." The framing communicates the NPC's inner state.

5. **Wrongness.** NPCs sometimes act on incorrect Opinions or false Concerns. The player may witness an NPC acting on a misunderstanding the player can correct — or exploit. This is realistic political life.

### Worked Example: A Season in Cardinal Klapp's Inner Life

To make this concrete, here is one named NPC across one season, showing how the inner-state architecture produces emergent political dynamics.

**Cardinal Klapp at Season 12:**
- Conviction: Reason (primary), Faith (secondary, suppressed)
- Beliefs: "Solmund's word may be incomplete. Honest scholarship is a path to understanding, not heresy." / "Himlensendt is a good man trapped by his own certainty."
- Disposition with player: +2 (the player attended his lecture last season, asked a thoughtful question)
- Concerns: "Where is the Stillhelm Codex referenced in the Brother Aldric letters?" / "Is it safe to invite the player into my private library?"
- Projects: "Find scholarly Thread evidence I can show Himlensendt without breaking my oath."
- Opinions: 
  - Of Himlensendt: respectful, grieved. Story: "He taught me what rigor means. He has stopped applying his own teaching."
  - Of the player: cautiously hopeful. Story: "They ask better questions than most of my colleagues. They might be a real interlocutor — or an opportunist."
  - Of Cardinal Fortitude: contemptuous. Story: "He confuses obedience with virtue. He will be the one who reports me when this all comes out."
- Mood: Steady (no recent disruption)
- Memories: top-3 currently salient: (1) the Solstice when Himlensendt preached against scholarly inquiry without naming Klapp, but everyone knew. (2) The day Brother Aldric's papers arrived from Stillhelm. (3) The lecture where the player asked the question.

**Season 12 events:**
- The Crown-Varfell treaty is signed (P-3 fires).
- Himlensendt enters arc transition (Crisis of Faith branch, +1 Scar).
- The player invites Klapp to a private dinner.

**Klapp's responses:**
- The treaty's signing creates space for Reason-aligned scholarship to be politically tolerable (Mood shifts toward Confident; Opinion of Almud subtly improves). Klapp's Project becomes more accessible — he can now correspond with Varfell scholars without it being a crime.
- Himlensendt's arc transition is *terrifying*. Klapp's Opinion of Himlensendt updates: "He is breaking. He may need me, or he may turn on me." A new Concern emerges: "If Himlensendt asks for my counsel, do I tell him what I actually think?" Klapp's Mood shifts to Anxious.
- The player's dinner invitation arrives. Klapp's Concerns activate: "Is it safe to invite the player into my private library?" combined with "Should I tell Himlensendt what I actually think?" The player has been at +2 Disposition for two seasons, has shown intellectual rigor, has not associated with the Inquisition. Klapp's Opinion of the player (cautiously hopeful) tips toward action.

Klapp accepts the dinner. During the dinner — if the player handles it well — Klapp shares one piece of his Project: he is looking for the Stillhelm Codex. This is a gift. The player now has a Concern of their own ("How do I find the Stillhelm Codex for Klapp?") that, if resolved, produces a strong faction-level political asset.

If the player handles the dinner badly (talks too freely about scholarly inquiry in earshot of the household, or pushes too quickly for political commitment), Klapp's Mood shifts to Anxious, his Opinion of the player updates with new evidence ("they don't understand discretion"), and he closes off. The political asset is lost — possibly forever, because Klapp's Concern "Is it safe to invite the player into my private library?" now has a definitive answer: no.

**The same season, different player handling, totally different downstream political consequences.** Not because of stat differences, not because of pre-scripted branches, but because Klapp is a person who is making decisions based on his own inner life, and the player's actions are evidence he interprets through his own Concerns and Opinions.

---

## Why This Matters for the Game

The previous proposals would have produced a more sophisticated political simulation than the current design — but it would still have been a simulation of *systems*. The player would learn to optimize stat thresholds, exploit RP balances, and game alignment scores.

Reframing NPCs as autonomous actors with feelings and opinions produces a different player experience: the player learns to understand *people*. They figure out who Cardinal Klapp is. They notice what he cares about. They build a relationship with him as a person, which produces political consequences because he is also a political actor — but the political consequences emerge from the personal relationship, not from a system.

This is what the inspiration document was reaching for in its opening critique: the design described "vendor relationships" rather than political ones. A vendor relationship is transactional — services in exchange for goods. A political relationship is *personal* — it involves feelings, opinions, memories, and projects that exceed any single transaction.

Mechanically, this requires the engine to track per-NPC state structures (Concerns, Projects, Opinions, Mood, Memories) that the player never directly sees. The player interacts with the *outputs* of these structures (NPC dialogue, behavior, scene generation), and learns to infer the *inputs* through observation and engagement. The political game is the game of understanding people well enough to act effectively.

This is also what makes the ripple effects genuinely emergent rather than pattern-matched. When Cardinal Klapp's Opinion of the player shifts from "cautiously hopeful" to "they don't understand discretion," the consequences are unpredictable in the strict sense: they depend on what Klapp does next, which depends on his Project, his Concerns, his current Mood, and his Memories. The same shift in a different NPC produces different consequences. The same shift in the same NPC at a different time produces different consequences because his other inner states have evolved.

The political environment is dynamic because the people in it are *alive*.
