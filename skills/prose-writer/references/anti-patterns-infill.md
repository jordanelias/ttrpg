# Anti-Patterns — AI Prose Failure Catalogue

Expanded rationale and examples for the rules in `anti-patterns-skeleton.md`. Eight-author roster: Tolkien, Márquez, Ishiguro, Mistry, Tartt, Lispector, Borges, Ocampo. For the Wittgenstein constraint and coherence-mismatch rules, see the skeleton.

Three layers of evidence: the LAMP taxonomy from professional editors (Chakrabarty et al., CHI 2025), academic research on LLM creative writing limitations (multiple studies 2022–2026), and stylometric analysis of LLM idiosyncrasies. All major models exhibit these failures. The patterns are structural, not superficial. Vocabulary tells evolve as specific words get scrubbed; structural habits persist.

---

## Part I — The LAMP Seven (Professional Editor Consensus)

Eighteen professional writers edited 1,057 LLM-generated paragraphs and converged on seven failure categories. These are the editorial-craft failures that human writers reflexively correct.

### 1. Cliché

LLM prose defaults to received phrases. Not just "delve" and "tapestry" — any phrase the reader has encountered often enough to stop seeing it.

**Surface clichés:** delve, intricate, tapestry, testament, vibrant, rich cultural heritage, underscore, commendable, nuanced, multifaceted, in the annals of, stood as a beacon, a testament to, it's worth noting, at the end of the day. (Vocabulary tells evolve. As "delve" fades, replacements like "core" and "modern" surge. Structural patterns are more reliable indicators than any fixed word list.)

**Structural clichés:**
- Ironic understatement endings: "And the day had barely begun." "It was going to be a long night."
- Universalized paradox: "something no one could name but everyone recognized."
- Rule of three with escalation: third item is the punchline.
- Meaningful weather: rain at sad moments, sun at hope.
- Named emotion with physical correlate: "A wave of grief washed over her." "Anger coiled in his stomach."
- "Most recent item on a long list" stock phrasing.

**Fix:** Replace received phrases with specific detail. What did the person actually do? Specificity is the antidote.

### 2. Unnecessary/Redundant Exposition

LLMs over-explain. They state what the scene shows. They narrate significance after depicting events.

**Symptoms:**
- "This was a sign that things were changing."
- "The significance of this moment was not lost on her."
- Explaining motivation right after showing the demonstrating behavior.
- Providing historical background the scene doesn't require.
- Closing a paragraph with a sentence that summarizes what the paragraph already showed.

**Fix:** Delete the explaining sentence. If the scene works without it, it was redundant.

### 3. Purple Prose

Overwrought writing where decoration obscures content.

**Symptoms:**
- Similes that exist for their own sake: "hung in the air like something you could lean against."
- Stacked adjectives: "the ancient, weathered, grey stone wall."
- Metaphors that announce the writer's cleverness rather than illuminate the subject.
- Describing a simple object with more language than it can bear.

**Fix:** Cut adjectives until only load-bearing ones remain.

### 4. Poor Sentence Structure (Homogeneity)

LLM prose tends toward uniform sentence length and structure.

**Symptoms:**
- Five consecutive sentences of similar length.
- Every sentence beginning subject-verb-object.
- No fragments. No single-word sentences.
- Every paragraph having the same number of sentences.
- The "long-then-short" alternation pattern repeated throughout.

**Fix:** Cluster three short sentences. Run two long sentences in sequence. Drop a fragment. Read aloud.

### 5. Lack of Specificity and Detail

LLM prose substitutes abstractions for concrete particulars.

**Symptoms:**
- "The market was busy."
- "She felt a deep connection to the land."
- "A sense of unease settled over the village."
- "Something older than sorrow."

**Fix:** Name the thing. Give the number. Identify the material. If you cannot be specific, the sentence has no content — cut it.

### 6. Awkward Word Choice and Phrasing

Words technically correct but contextually wrong, OR words elevated without earning the elevation.

**Symptoms:**
- Latinate where Germanic belongs *and the Latinate adds no precision*: "commenced" for "began," "perambulated" for "walked," "illumination" for "light." The test is whether the rare word *saves syllables* or adds them. If it adds, cut it.
- Modern corporate language in historical settings: "stakeholders," "leverage."
- Thesaurus syndrome: unusual synonyms drawing attention to themselves.
- AI-marker words: "delve," "underscore," "commendable," "nuanced."

**The Valoria voice is comfortable with graduate-level vocabulary.** Words like *catabasis*, *aporia*, *recusant*, *palimpsest*, *interregnum*, *suzerain* are correct when they replace a longer periphrasis. The failure is reaching for register without earning it. "Sesquipedalian" is the right word for "given to long words"; "perambulated" is wrong for "walked."

**Fix:** For each modifier, verb, or noun, ask: is this the most apt word, or is it just a more impressive word? If it's the most apt, keep it regardless of register. If it's just more impressive, replace with the simpler accurate word.

### 7. Tense Inconsistency

LLMs drift between past and present, especially in descriptive passages.

**Fix:** Choose a tense and hold it. Make any shift deliberate and visible.

---

## Part II — Academic Research Findings on LLM Prose

Each finding below is grounded in peer-reviewed or preprint research. These describe deeper, structural failures that operate beneath the LAMP categories.

### Lower Uncertainty / Aporia Failure

LLMs produce prose with significantly lower uncertainty than professional writers (Sui et al., McGill 2026). They converge toward a single coherent ground truth. But literary insight resides in aporia — the irresolvable internal contradiction, the deferred meaning, the "free play" of signification that resists grounding in a single answer.

The post-training that reduces hallucination also reduces literary capacity. Convergent prose feels deterministic. Real literature tolerates contradiction.

**Manifestation in prose:**
- A scene resolves into a single clear meaning instead of holding multiple readings.
- A character's motivation is rendered legible when it should be opaque.
- Symbols are decoded rather than left active.
- The narrator never doubts its own framing.

**Fix:** Allow contradiction. Let two readings of a scene coexist. Refuse to resolve what doesn't need resolution. The seneschal may have refused the summons from principle or from temperament — the prose should not always tell us which.

### Subtext Failure

Across multiple studies (Mirowski et al. 2023; Subbiah et al. 2024 "Reading Subtext"; Columbia narrative summarization research) LLMs consistently fail at producing or interpreting subtext. Models flatten implicit character portrayal into explicit statement. They miss unreliable narration. They fabricate motivation when narrative has deliberately left it implicit.

**Manifestation in prose:**
- Characters say what they mean.
- Conflicts are explicit rather than performed through indirection.
- Tension is resolved through dialogue rather than withheld through omission.
- The reader is told what to feel rather than positioned to infer it.

**Fix:** Build scenes where what characters do not say carries the weight. Two NPCs negotiating a betrayal while discussing trade routes. A confession arriving as an aside. Keep the surface clean; let depth accumulate beneath.

### Cultural Ghosting / Register Flattening

LLMs systematically erase culturally and class-marked linguistic features (Navneet et al. 2026). Prose gets "professionalized" — distinct varieties of English collapse toward Western middle-class register. Identity-linked markers are flattened while semantic content is preserved.

**Manifestation in prose:**
- All characters speak in similar registers regardless of background.
- Vernacular forms get smoothed into standard prose.
- Working-class and educated-class characters sound interchangeable.
- Regional or institutional idiom is lost.
- Indigenous, untranslated, or culturally specific terms are replaced with translations.

**Fix:** Preserve distinct registers across characters. Use untranslated terms (with context teaching the reader). Maintain class-marked speech in dialogue. The fishmonger and the seneschal should not sound the same.

### Failure to Sustain Dramatic Tension

LLMs struggle to build and hold tension over a passage (Tian et al. 2024). Conflict gets resolved too quickly. The escalation curve flattens. Suspense is established and then released within the same paragraph.

**Manifestation in prose:**
- Setup and payoff occur in adjacent sentences.
- The narrative does not let the reader sit with not-knowing.
- Emotional escalation reaches a peak and immediately releases rather than holding.

**Fix:** Hold the tension. Resolve later than feels natural. Insert digression between setup and payoff. Trust that the reader will carry the unresolved question across paragraphs.

### Plot Template Convergence

Narrative arcs converge to common templates regardless of prompt (Padmakumar & He 2024; Xu et al. 2025). Recognizable LLM plot structures: the redemptive arc that resolves cleanly, the villain who exists to be defeated, the emotional epiphany at the three-quarter mark, the moral lesson at the close.

**Manifestation in prose:**
- Endings that resolve too neatly.
- Antagonists rendered as obstacles rather than people.
- Character growth that arrives on schedule.
- Themes that surface as moral conclusions.

**Fix:** Resist the template. Let conflicts persist. Let characters fail to grow. Let endings open rather than close.

### Long-Range Coherence Failure

Across long-form narrative, LLMs lose track of character continuity, motif tracking, and callbacks (Gurung & Lapata 2025; Pham et al. 2025). The hero who feared spiders on page five has one as a pet on page fifty. Magical objects work for the wrong people. Foundational structural conventions break.

**Manifestation in prose:**
- A character's earlier-established trait disappears.
- Setup elements never pay off; payoffs never have setups.
- Names, places, or facts shift between mentions.
- Promised consequences don't arrive.

**Fix:** For Valoria specifically: track named entities, established traits, and previously-stated facts. If a character has been characterized one way, do not contradict without acknowledging the contradiction.

### Lower Lexical Diversity / Heavy Nominalization

Stylometric analysis identifies LLM prose by reduced lexical diversity, heavy nominalization (verbs becoming nouns), and reliance on generic abstract nouns: ecosystem, framework, dynamic, landscape, navigation. Verbs converge on a small set: leverage, unlock, navigate, optimize.

**Manifestation in prose:**
- "The implementation of the strategy" instead of "they did it."
- "The cultural landscape" instead of "the city."
- "Navigate the complexities" instead of any specific action.
- Repetitive verb choice across passages.

**Fix:** Prefer concrete verbs. "She walked" or "she ran" or "she crossed" before "she navigated." Prefer concrete nouns. "The walled district" before "the urban environment."

### Reduced Sentiment Modulation

LLM prose maintains uniform emotional pitch across passages. Real human prose has abrupt sentiment shifts — humor breaking grief, mundanity interrupting horror, tenderness within violence. LLMs smooth these transitions or avoid them entirely.

**Manifestation in prose:**
- A grim passage stays grim from start to finish.
- A comic passage maintains its tone.
- Tonal mixing feels deliberate rather than organic.

**Fix:** Place absurdity beside suffering without commentary. Let humor surface in tragedy. Let grief leak into routine. The mixing is the technique.

### The "Not Just X But Y" / Negative Parallelism Habit

Stylometric studies (Washington Post analysis of 328k ChatGPT messages) identify negative parallelism — "Not just X, but Y" / "Not merely A but also B" — as one of the most persistent structural tells. Even after specific words are scrubbed, this construction recurs.

**Manifestation:** Any sentence built on the "not just / but also" frame. Any sentence using negation to set up a "more important" affirmation.

**Fix:** Affirm directly without the negative setup. The construction usually adds nothing the affirmation alone wouldn't carry.

### Hypotaxis-Parataxis Indecision

Real writers commit. Hemingway commits to parataxis (clauses placed side by side, no subordinate logic). Faulkner commits to hypotaxis (long subordinated sentences building cohesion). Tolkien commits to parataxis with biblical resonance. LLMs split the difference, producing sentences that subordinate weakly without committing to either pattern. Result: prose that reads as competent but lacks the structural conviction of real style.

**Fix:** Commit. The Valoria voice's default is paratactic — short clauses, "and" as connector, causation supplied by reader. When it goes hypotactic, it goes deeply hypotactic, with cascading subordination held to a single arc. No middling subordination.

---

## Part III — Structural AI Tells (Beyond LAMP)

These are observed in this skill's own outputs and in published critiques.

### Excessive Symmetry

Balanced constructions used reflexively. "Some did X; others did Y." "Where once there was A, now there was B." Used once: fine. Used repeatedly: mechanical.

### The Reaction Shot

After every event, the LLM describes how characters react emotionally. Real prose often skips the reaction. The event is stated; the next scene begins.

### Thematic Announcement

LLMs state themes. "In a world where trust was rare, she had learned to rely on herself." Real prose embeds theme in event and image.

### The Summarizing Final Sentence

LLMs end paragraphs with sentences that summarize or reflect. End on the strongest image or the most important fact, never on a gloss.

### Hammering Repetition

Repeating a phrase or word for emphasis when one instance carries the weight. "It was there. It was always there." The second sentence adds nothing. (Distinguish from anaphora, which is structural repetition across sections, and from Ishiguro's repetition-with-variation, which returns to the same scene with new detail.)

### Second-Person Drift in Player-Character Prose

The player-character is observed in third person. Prose drifting into second-person ("you see," "you walk," "you understand") referring to the PC breaks the synthesized voice. Every "you" pulls chronicle distance into immediate self-address, which cannot tolerate Tolkien's parataxis, Ishiguro's restraint, or chronicler perspectives.

**Symptom:** Narrative prose mixing third-person with embedded "you" pronouns referring to the PC.

**Fix:** Convert all PC references to name or pronoun. Choice-hooks may stay second-person imperatives ("Approach the parish house") or convert to third-person action descriptions ("Vael will need names"). Direct speech from NPCs to the PC stays second-person — that is dialogue, not narration. The narrative prose itself must be uniform.

This applies to all narrative content involving the PC: pop-up events, arc narrative beats, portraits where the PC is the subject, and any chronicle or season-summary entry referring to the PC.

### Editorial Stance Without Focalization

Editorial words ("sinister," "noble," "wretched") floating from a non-existent neutral narrator. These words require a perspective. When focalization is established, editorial words are licensed. When it isn't, they are AI tells.

**Fix:** Either establish the focalization that licenses the word, or replace with condition-words ("rusted," "abandoned," "patched") that imply judgment without announcing it.

### Single-Author Dominance Without Cause

The Valoria voice is a coherence-indexed blend of eight authors: Tolkien, Márquez, Ishiguro, Mistry, Tartt, Lispector, Borges, Ocampo. Weighting shifts with coherence tier — see `coherence-tiers.md`. When a passage's texture is overwhelmingly one author's techniques without the content demanding it, the synthesis has collapsed into pastiche.

This is *not* a rule that every passage must contain all eight authors. Some passages legitimately lean heavily on one (a restrained interior monologue may be 60% Ishiguro by texture). The failure is when the dominance is unmotivated — when a passage drifts entirely into one mode because the writer fell into rhythm, not because the content called for it.

**Symptoms:**
- A passage's sentences are all subordinated and hedged, in content that doesn't require restraint.
- A passage is interior aestheticism throughout, in content that needs landscape or chronicle weight.
- A passage is sensory catalogue without scale-shift or temporal anchor, in content that includes generations or distance.
- A passage's matter-of-fact impossibility runs without grounding, in content where grounding is needed.
- A passage strikes Tartt-punch repeatedly when no single moment earns the weight.
- A passage has no Tolkien-derived techniques anywhere despite Tolkien being the highest-weighted author.

**Fix:** Diagnose what the content needs. If the content involves landscape, chronicle, or scale-shift, Tolkien-derived techniques should be visible somewhere. If the content involves time-folding or the impossible, Márquez-derived techniques should surface. If a passage feels mono-author, splice another author's technique into a clause or sentence — without forcing it. The synthesis tolerates a heavily-weighted-toward-one passage; it does not tolerate the absence of the synthesis.

### Mechanical-Term Leakage in Focalized Prose

When prose is focalized through an in-world character, system or mechanical terminology breaks the focalization. The character does not know they are inside the Conviction Track or the Church Influence clock or the Ehrenwall Counter. They experience the consequences in human terms.

**Symptoms:**
- "The Conviction Track drifted in unexpected directions."
- "Church Influence had reached the threshold."
- "The Mending Stability registered a drop."

**Fix:** Translate to focalized experience. The Conviction Track becomes "the agreement that had held the Capital steady." Church Influence becomes "the Church's reach." Mending Stability becomes "the world's hold" or "what kept things together." The character names the experience, not the system.

This rule applies only to in-world focalization. A pure design document may use mechanical terminology directly. A codex entry framed as in-world chronicle should not.

### Flat-Affect Omniscience

Prose written from a "neutral all-knowing narrator" position. Produces no perspective, no stance, no relation to material. Reads as AI even when sentences are clean.

**Fix:** Identify focalization before writing. There is no neutral narrator.

### Workshop Closings

Endings that announce themselves as endings. The ironic understatement ("the day was barely started"). The pivoting reflection ("she would remember this moment"). The thematic gesture ("nothing would be the same"). Creative-writing-class tics. End on the strongest specific detail.

### Too-Clever Constructions

Sentences drawing attention to their own cleverness. "It worked, but not in the same way" is plain. "It simply worked differently" is too neat — the "simply" is condescending and the construction symmetrical. Real prose is rougher.

### Mechanical-Term Leakage in Focalized Prose

When prose is focalized through an in-world character, system or mechanical terminology breaks the focalization. The character does not know they are inside the Conviction Track, the Church Influence clock, the Threadwork Co-Movement matrix, the Ehrenwall counter. Naming these systems in the character's voice or in narration filtered through their consciousness shatters the perspective frame.

**Symptoms:**
- A practitioner narrator referring to "the Conviction Track" instead of "the agreement holding the Capital steady" or "the equilibrium."
- A villager character noticing "Church Influence rising" instead of "the bishop's notices appearing on more doors each spring."
- A retrospective narrator describing the past in mechanical bookkeeping terms ("our CI reduction held for three seasons").

**Fix:** The character speaks the world they live in. They feel pressure, they see notices, they hear bells. They do not see clocks ticking up. Replace any system name with what the character would actually perceive or call the thing.

**Exception:** Codex/chronicler voice operating from outside the immediate scene may use system-adjacent terminology IF that chronicler is positioned (e.g., a scholar of statecraft writing centuries later may name the institutions, though even then would not name the mechanical resolution structures). Default: paraphrase.

### Closing Sentence Drift

Closing sentences are the highest-risk position for AI tells. The skill's own audits repeatedly find borderline cases at the close: ironic understatement, retrospective gloss, thematic gesture. The structural pull toward "closing on meaning" is strong even when the rule is known.

**Heuristic:** When in doubt about a closing sentence, end one sentence earlier. The penultimate sentence is almost always more concrete and specific. The final sentence is almost always where the writer reaches for resonance — and resonance reached-for reads as AI.

---

## Part IV — Author-Specific Mannerism Risk

Each source author has techniques that, individually effective, become mannerisms when overused.

- **Tolkien:** Inverted syntax ("Great was the ruin"). Once: weighty. Repeatedly: costume.
- **Ishiguro:** "perhaps as it should have been," "I cannot now recall." Once: restrained. Repeatedly: tic.
- **Mistry:** Sensory catalogues. Once: immersive. Repeatedly: tour.
- **Tartt:** Three-word punch sentences. Once: weight. Repeatedly: drumbeat.
- **Lispector:** "This instant-now" temporal shift. Once: rendering failure. Repeatedly: affectation.
- **Borges:** Infinite recursion / mirror metaphor. Once: the paradox holds. Repeatedly: the trick is visible.
- **Ocampo:** Flat-affect horror. Once: devastating. Repeatedly: monotone.
- **Tartt:** Atmospheric long sentences. Once: immersion. Repeatedly: fog.
- **Márquez:** Hyperbolic precision. Once: comic gravity. Repeatedly: schtick.

The synthesis discipline: borrow techniques in rotation. Do not use any single source's signature move twice in the same passage.

---

## The Master Rule

If a sentence could appear in any story about any settlement/character/event, it belongs to no story. Cut it.

- "The weight of history pressed down upon them." — Could appear anywhere. Cut.
- "Three of the four granary locks had rusted shut." — Belongs only to this place. Keep.
