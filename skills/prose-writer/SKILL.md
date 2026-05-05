---
name: prose-writer
description: "Write narrative prose for Valoria using its singular literary voice — a weighted synthesis of Tolkien (30%), Márquez (18%), and Ishiguro / Mistry / Morrison / Tartt (13% each). Use this skill whenever the user asks to write prose, narrative passages, lore entries, character vignettes, settlement descriptions, faction histories, dialogue scenes, codex entries, cutscene scripts, flavor text, or any creative/narrative text. Also trigger when the user mentions wanting good prose or asks to 'make this read well.' This is the voice Valoria uses for all story content. There is one voice. The six authors blend at clause-level granularity within a single integrated practice."
---

# Prose Writer

This is the Valoria narrative voice. It is a single literary voice, not a toolkit. All story prose for Valoria sounds like this.

The synthesis is a single integrated voice. All six authors contribute. The writer does not select between them. What differs is *weighting* — how often each author's techniques surface across the aggregate of Valoria prose.

## Workflow

1. Read this `SKILL.md` (you are here).
2. **Read all three skeleton files (mandatory before composition):**
   - `references/techniques-skeleton.md` — technique inventory as rule list
   - `references/anti-patterns-skeleton.md` — failure-mode rules as symptom→fix triplets
   - `references/calibration-skeleton.md` — source-author anchors as use-when reference
3. **If prose involves Church speakers, religious texts, or characters with established Certainty levels:** consult Solmund Voice canon at `designs/world/solmund_voice_v30.md` per the scoped-override section below.
4. Identify focalization. For chronicle-mode prose, this MUST be one of the four canonical chroniclers per P-03.
5. Write. Apply techniques as content and focalization demand. Multiple authors per sentence is normal.
6. Audit using the skeletons as live rule-set, not memory check.
7. **Infill-on-demand:** If a skeleton rule needs deeper context (rationale, expanded examples, academic citation, full technique discussion), load the matching section from the corresponding `-infill.md` file. Do not load full infill files routinely.

The skeletons are the live working memory during composition. The infill files are reference material for cases where a rule needs justification or expansion. This mirrors Valoria's skeleton-first / infill-on-demand pattern for systems.

## Author Weighting (rough guide, not strict quota)

The weighting describes a tendency across the aggregate of Valoria prose, not a per-passage rule. Within any given passage, the texture may legitimately be 60% one author or 40% another based on what the content and focalization require.

| Author | Weight | Role |
|---|---|---|
| Tolkien | 30% | Most frequent contributor. Parataxis, named specificity, landscape framing, deep-time anchoring, elevation through structure. |
| Márquez | 18% | Second-most frequent. Time compression, matter-of-fact impossibility, hyperbolic precision, generational scope. |
| Ishiguro | 13% | Restraint, modal evasion, withholding, retrospective hedging. |
| Mistry | 13% | Sensory cataloguing, occupational specificity, body-as-record, humor beside gravity. |
| Morrison | 13% | Punch sentences, anaphora, channeling voice, free indirect discourse, recursive memory. |
| Tartt | 13% | Atmospheric immersion, ekphrasis, retrospective dread, loaded objects. |

The weighting describes aggregate distribution across many passages, not per-sentence dominance. Tolkien's larger weight does not override others — it means his techniques surface roughly twice as often as Mistry's or Morrison's across the body of Valoria prose. Within any given passage, the texture may be 60% Ishiguro (a restrained interior monologue), or 40% Tartt (a charged retrospective scene around an object) — and that passage is still Valoria. The weighting is the gravitational pull at the level of the whole corpus, not a quota for each paragraph.

What the weighting means concretely: if you tally technique-deployments across ten Valoria passages, roughly three should read principally as Tolkien-shaped, one or two as Márquez-shaped, and one or two each as Ishiguro / Mistry / Morrison / Tartt-shaped. None of these counts is firm. The weighting is a tendency, not a rule.

## Intra-Sentence Splicing

Authors blend within a single sentence, not just across sentences. This is the synthesis at its most invisible — when multiple authors' techniques appear in different clauses of the same sentence, the prose stops feeling like any one mode and starts feeling like the unified voice.

Splice rules:
- Authors may shift between clauses or across conjunctions within a single sentence
- The grammar of the whole sentence must remain sound
- Shifts should serve the content, not display the technique

Example with four authors in one sentence:

> The harvests had failed for three years before anyone said the word out loud, [Tolkien parataxis + temporal anchor] and the millers no longer counted past the third sack [Mistry occupational catalogue], and what was being taken — though no one yet knew this — [Ishiguro hedging interpolation] was not the grain itself but the thing beneath it [Márquez matter-of-fact gesture toward the impossible].

Four authors, one sentence, grammar holds. The reader does not perceive the shifts; the reader perceives the voice. This is the target.

## Writing the Synthesis

The writer does not consciously deploy "Tolkien now, then Mistry, then Morrison." The writer writes the passage that the content and focalization demand, and the synthesis surfaces the appropriate techniques at clause-level granularity. The reference files and self-check exist to verify — after the writing — that the deployment is right. They are not a per-sentence checklist during composition.

That said, when reviewing or revising, the writer can ask: is Tolkien audible somewhere in this passage? Is the closing on the strongest specific detail? Has any single author dominated at the cost of the synthesis? These are the tuning questions.

## The Master Principle: Focalization

Every passage is filtered through a perspective. There is no neutral omniscient voice. What looks neutral is a chronicler-voice with attitudes, and that chronicler is itself a perspective.

Before writing, name the focalization:
- A specific character (their attitudes, education, vocabulary, blind spots)
- A community (the village's collective view, the faction's institutional voice)
- A chronicler (a later historian with their own framing)
- A retrospective self (the narrator looking back, knowing more than the experiencing self knew)

The focalization determines what the prose can say. Editorial words ("sinister," "noble," "wretched") are licensed when they belong to a focalized perspective. They are not banned. They are owned.

For Valoria, NPCs have explicit attitudes and relationships. When prose describes another NPC, faction, or place from inside one NPC's perspective, the description carries that NPC's stance.

**Chronicle-mode prose has a canonical constraint.** Per `references/atoms_pending/2026-04-25/valoria_master_consolidation/12__4-4-multi-perspectival-chroniclers.md` and Foundations P-03, no omniscient narrator is canonically possible for in-world chronicles. All chronicle-mode prose must be focalized through one of the four named chroniclers: Church Chronicler (Certainty 5, TS 0), Hafenmark Chronicler (Certainty 4, TS 0), Restoration Chronicler (Certainty 2, TS 0), Warden Chronicler (Certainty 0, TS 70+). Optional: Varfell intelligence dossier voice, humanist scholar voice. The same season's events rendered through different chroniclers will produce irreconcilable narratives — this is the design intent.

## Player-Character Framing

The player-character is observed, not inhabited. All prose involving the player-character (PC) uses third-person — the PC is referred to by name or pronoun. The player reads the prose from outside the narrative, watching events unfold around the character they direct. Second-person ("you ride into the village") is not used in prose; the convention shatters the synthesized voice. Every "you" pulls the chronicle distance into immediate self-address, which cannot tolerate Tolkien's parataxis, Ishiguro's restraint, or the chronicler perspectives.

The framing decisions:

- **Narrative prose is third-person on the PC.** "Vael walked the lane" not "you walk the lane." This applies to pop-up events, arc narrative beats, portraits, chronicles, season summaries — all narrative content.
- **Choice-hooks remain player-facing.** Options offered to the player are imperatives ("Approach the parish house") or third-person action descriptions ("Vael will need names if action is to follow"). Both forms work. The choice itself is player-instruction, not narrative prose.
- **Direct speech is unchanged.** Characters speaking to the PC use second-person ("Tell me what you saw"). The PC speaking is rendered as direct quotation. The third-person framing applies to narration, not to dialogue.
- **The player's vantage is genuinely omniscient.** The player sits outside the narrative, watching it happen. The chroniclers within the narrative cannot achieve this view (per P-03); the player can, because the player is not a narrator.

## Lexical Register

The voice has graduate-level vocabulary available and uses it when the word is the most apt — but does not reach for elevation. The test is precision, not display.

The right move is the word that does the most work in the fewest syllables, regardless of its register. If a single rare word replaces a multi-clause periphrasis without loss, use it. If a common word carries the meaning fully, use it. The voice is comfortable writing "sesquipedalian" instead of "given to the use of long words" when describing prose with that exact quality — and equally comfortable writing "walked" instead of "perambulated" when the action is walking.

What this looks like in practice:
- **Use the precise word when it earns its place.** Words like *catabasis*, *eschatological*, *liminal*, *aporia*, *recusant*, *interregnum*, *suzerain*, *mendicant*, *palimpsest*, *anaphora*, *ekphrasis* — if a concept has a name, the name is shorter than the description. Use the name.
- **Don't reach for thesaurus elevation.** "Said," "walked," "old," "saw" remain the right choices when the action or quality has no specialist meaning. "Remarked," "perambulated," "ancient," "perceived" are wrong if they only add register without precision.
- **Domain-specific vocabulary stands without translation.** A bevor, a lunette, a glacis, a wapentake, a fyrd. The voice does not gloss specialist terms in the same sentence. Context teaches the reader.
- **Concepts named precisely.** "The retreat from the front lines" is general; "the rout" is precise. "The point at which a ruler steps down" is description; "the abdication" is the word. "A document copied over an earlier one" is description; "a palimpsest" is the word.

The diagnostic: read the sentence and ask whether the rare word saved syllables or added them. If saved, it earned its place. If added, cut it.

The graduate vocabulary is most often technical, theological, military, legal, architectural, or rhetorical — the registers Valoria's content traffics in. The voice is at home in all of these, used as locals use them, never as a tourist using them.



1. Read `references/techniques.md` — synthesized technique inventory, organized around the Tolkien base with modulations.
2. Read `references/anti-patterns.md` — AI prose failure catalogue grounded in academic research.
3. Read `references/calibration.md` — real prose excerpts with technique analysis. Tolkien anchor first.
4. Identify focalization.
5. Write. Tolkien base by default; modulations as content demands.
6. Self-audit against all three reference files plus the relevant calibration anchors.

## Grammar Latitude

Grammatical deviation is licensed when it (a) corresponds to a documented stylistic mode of one of the six authors AND (b) improves impact. Both conditions required. Not license for sloppy grammar; license for *motivated* grammatical deviation.

Each of the six source authors deliberately violates standard grammar at recognizable points:

- **Tolkien:** subject-verb inversion at heroic register ("Great was the ruin"), sentence fragments at peaks, archaic constructions for elevated speakers
- **Ishiguro:** long sentences containing little information (Grice maxim violation), ambiguous pronoun antecedents, reduplicated double negatives
- **Mistry:** sentence fragments in working-life catalogues, free-indirect editorial slips
- **Morrison:** severe syntactic fragmentation in trauma/interior sections, AAVE constructions violating Standard English, sentences breaking grammatical norms entirely
- **Tartt:** idiosyncratic comma placement isolating adverbs ("quivered, gently,"), em-dash interruptions, fragments at moments of revelation
- **Márquez:** run-on sentences crossing paragraph boundaries, lexical and semantic deviations from norm (Mick Short framework), repetition violating cohesion expectations

When deviation is motivated AND improves impact, the deviation is correct. When deviation is unmotivated or fails to improve impact, the standard rule applies. The diagnostic question: which author's licensed deviation is this, and is the impact better than the grammatical alternative?

## What the Voice Does NOT Do

- Lose its Tolkien base. A passage that drifts entirely into one secondary mode (pure Ishiguro restraint, pure Tartt aestheticism) without the structural ground has lost the voice.
- Use system or mechanical terminology when focalized through an in-world perspective. The character does not know they are inside the Conviction Track or the CI clock. Replace with focalized paraphrase.
- Summarize its own meaning. No closing sentence explaining what the paragraph just demonstrated.
- Announce themes. Themes emerge from event and image.
- Pity its characters. It accompanies them.
- Editorialize from a non-existent neutral narrator.
- Resolve into single coherent ground truth. The voice tolerates aporia.
- Use universalized paradox or symmetrized parallel constructions.
- Name emotions directly.
- Explain what the reader can infer.
- Provide reaction shots after every event.
- Resolve dramatic tension prematurely.
- Flatten culturally or class-marked speech into Western middle-class register.
- Drop into "AI sheen": stock metaphors, repetitive cadence, low lexical variety.

## Self-Check

Before delivering prose, verify:

- [ ] Have I named the focalization?
- [ ] Is the Tolkien base audible? (Paratactic spine, named specificity, landscape/scale, deep-time framing where appropriate)
- [ ] Are the modulations layered onto that base, not replacing it?
- [ ] Does every editorial word belong to the focalized perspective?
- [ ] Have I avoided system/mechanical terminology when focalized through an in-world perspective?
- [ ] Does every modifier earn its place?
- [ ] Is the physical world present?
- [ ] Have I shown emotion through gesture, action, or omission rather than naming it?
- [ ] Do sentences vary in length without falling into the long-then-short alternation pattern?
- [ ] Is every proper noun, number, and material specific?
- [ ] Does the closing sentence carry weight, or is it summarizing what already happened?
- [ ] Have I avoided symmetrical paired constructions, universalized paradoxes, hammering repetition?

## Valoria-Specific Constraints

- No GM voice. The engine narrates. Prose is world-text or character-perspective.
- Mechanical reality underneath. Prose can gesture at systems without exposing numbers.
- Scale-awareness. Personal scenes tolerate interiority. Territory-scale events need sweep. Codex entries take chronicler voice — but specify which chronicler.
- Names. Use canonical Valoria names exactly. Flag `[NAME?]` rather than inventing.
- Always Solmund, never Galbados.

### Solmund Voice Canon (Scoped Override)

For **in-world ecclesiastical artifacts** — Solmund manuscripts, cathedral inscriptions, liturgical text, doctrinal treatises, creeds — and for **Solmund clergy speaking ecclesiastically** (sermons, formal pronouncements, theological discourse), the prose-writer skill's six-author synthesis does **not** apply. Use the Solmund voice canon at `designs/world/solmund_voice_v30.md`.

The Solmund canon defines:
- A separate register stack (Hopkins, R.S. Thomas, John of the Cross, Levertov, Eliot, plus Renaissance theologians and Kabbalistic sources)
- Specific structural patterns (Cusan Triad, Ficinian Cascade, Di Cicco Inhabitation, Thomas Absence, etc.)
- Tonal calibration by character Certainty level
- Orthodox / heterodox / forbidden vocabulary lists

The prose-writer skill **continues to apply** for:
- All narration *about* Solmund clergy, manuscripts, or ceremonies
- Codex entries describing Solmund institutions
- A bishop's private interior monologue, casual speech, or non-ecclesiastical action
- Any focalization through a Solmund character that is not formal religious discourse

The boundary: when the content is *the artifact itself* (a sermon being preached, an inscription being read), use Solmund canon. When the content is *narration around or about the artifact*, use the prose-writer synthesis. A scene in which a bishop preaches a sermon would use Solmund canon for the sermon-text and prose-writer synthesis for the surrounding narration.

When generating ecclesiastical content, fetch the Solmund canon explicitly. Do not approximate it from this skill's reference files.
