# Anti-Patterns — Infill

Additional examples and operational detail for rules in `anti-patterns-skeleton.md`. The skeleton is always loaded first and owns every rule; an entry here adds only what the skeleton does not. Vocabulary tells evolve as words get scrubbed; structural habits persist, so prefer the structural signature over any word list.

| Skeleton rule | Entry here |
|---|---|
| I.1 Language & Register | Cliché; Awkward Word Choice; Register Flattening; Nominalization; Negative Parallelism |
| I.2 Sentence Architecture | Sentence Homogeneity; Hypotaxis-Parataxis |
| I.4 Over-Explanation & Premature Resolution | Redundant Exposition; Purple Prose; Aporia; Subtext; Tension; Plot Templates; Sentiment Modulation; Closings and Announcements |
| I.7 Content Leakage | Second-Person Drift; Mechanical-Term Leakage |
| I.8 Long-Range Coherence | Long-Range Coherence |
| V.6 Borges | Too-Clever Constructions |
| V.13 Single-Author Dominance | Single-Author Dominance |
| Master Rule | Master Rule examples |

---

## I.1 Language & Register

### Cliché
**Further surface clichés:** rich cultural heritage, in the annals of, stood as a beacon, a testament to, it's worth noting, at the end of the day. As "delve" fades, replacements like "core" and "modern" surge.

**Structural-cliché examples:**
- Ironic understatement endings: "And the day had barely begun." "It was going to be a long night."
- Named emotion with physical correlate: "A wave of grief washed over her." "Anger coiled in his stomach."
- Rule of three with escalation: the third item is the punchline.
- "Most recent item on a long list" stock phrasing.

**Fix:** What did the person actually do?

### Awkward Word Choice
The test is whether the rare word *saves syllables* or adds them ("illumination" for "light" adds them).

**The Valoria voice is comfortable with graduate-level vocabulary.** *Catabasis*, *aporia*, *recusant*, *palimpsest*, *interregnum*, *suzerain* are correct when they replace a longer periphrasis. "Sesquipedalian" is the right word for "given to long words"; "perambulated" is wrong for "walked."

**Fix:** For each modifier, verb or noun, ask: is this the most apt word, or just a more impressive one? If most apt, keep it regardless of register; if only more impressive, use the simpler accurate word.

### Register Flattening
Also lost: regional or institutional idiom; untranslated or culturally specific terms replaced with translations. Maintain class-marked speech in dialogue — the fishmonger and the seneschal should not sound the same.

### Nominalization
"The implementation of the strategy" instead of "they did it." "The cultural landscape" instead of "the city." "Navigate the complexities" instead of any specific action. Verbs converge on leverage, unlock, navigate, optimize. Prefer "she walked", "she ran", "she crossed" before "she navigated"; "the walled district" before "the urban environment."

### Negative Parallelism
Covers any sentence using negation to set up a "more important" affirmation; it survives after specific words are scrubbed.

## I.2 Sentence Architecture

### Sentence Homogeneity
Also: no single-word sentences anywhere; every paragraph carrying the same number of sentences.

### Hypotaxis-Parataxis
Real writers commit: Hemingway to parataxis, Faulkner to hypotaxis, Tolkien to hypotaxis as default and parataxis as marked register at moments of biblical resonance. Weak, uncommitted subordination reads as competent prose without the conviction of style. The Valoria default is long subordinated sentences building cohesion across temporal and spatial clauses, cascading subordination held to a single arc; parataxis surfaces at heroic peaks, ruined cities, deep-time framings.

## I.4 Over-Explanation & Premature Resolution

### Redundant Exposition
"This was a sign that things were changing." "The significance of this moment was not lost on her." Explaining motivation immediately after the behaviour that showed it. **Test:** delete the explaining sentence; if the scene works, it was redundant.

### Purple Prose
A simile that exists for its own sake ("hung in the air like something you could lean against"); stacked adjectives ("the ancient, weathered, grey stone wall"); a simple object described with more language than it can bear.

### Aporia
Also: the narrator never doubts its own framing. Refuse to resolve what doesn't need resolution: the seneschal may have refused the summons from principle or from temperament — the prose should not always say which.

### Subtext
The reader is told what to feel rather than positioned to infer it. Model: two NPCs negotiating a betrayal while discussing trade routes; a confession arriving as an aside. Keep the surface clean; let depth accumulate beneath.

### Tension
Also: emotional escalation peaks and immediately releases; the reader is never left to sit with not-knowing. Trust the reader to carry the unresolved question across paragraphs.

### Plot Templates
Recognizable defaults: the redemptive arc that resolves cleanly, the villain who exists to be defeated, the epiphany at the three-quarter mark, the moral lesson at the close; antagonists as obstacles rather than people; growth on schedule. Let conflicts persist, characters fail to grow, endings open. Scene-level Valoria templates: I.14.

### Sentiment Modulation
Where tonal mixing does occur, it reads as deliberate rather than organic. Let humour surface in tragedy and grief leak into routine; the mixing is the technique.

### Closings and Announcements
- **Reaction Shot.** Real prose often skips the reaction. The event is stated; the next scene begins.
- **Thematic Announcement.** Embed theme in event and image.
- **Workshop Closings.** Also: the pivoting reflection ("she would remember this moment"); the thematic gesture ("nothing would be the same").
- **Closing Sentence Drift.** The close is the highest-risk position: ironic understatement, retrospective gloss, thematic gesture recur there even when the rule is known. The final sentence is where the writer reaches for resonance, and resonance reached-for reads as AI. End on the strongest image or the most important fact, never on a gloss.

## I.7 Content Leakage

### Second-Person Drift
Rule: SKILL.md "Player-Character Framing." Every "you" pulls chronicle distance into immediate self-address, which cannot tolerate Tolkien's parataxis, Ishiguro's restraint or chronicler perspectives. **Scope:** pop-up events, arc beats, portraits of the PC, any chronicle or season-summary entry referring to the PC. Choice-hooks may also be third-person action descriptions ("Vael will need names").

### Mechanical-Term Leakage
The character does not know they are inside the Piety Track, the Church Influence clock, the Threadwork Co-Movement matrix or the Ehrenwall counter. They feel pressure, see notices, hear bells; they do not see clocks ticking up.

- "The Piety Track drifted" → "the agreement that had held the Capital steady" / "the equilibrium."
- "Church Influence had reached the threshold" → "the Church's reach"; "the bishop's notices appearing on more doors each spring."
- "The Mending Stability registered a drop" → "the world's hold" / "what kept things together."
- A retrospective narrator's "our CI reduction held for three seasons" → what the narrator saw happen.

**Scope:** in-world focalization only; a design document may use mechanical terms, a codex entry framed as in-world chronicle may not. **Exception:** a chronicler positioned outside the scene (a scholar of statecraft centuries later) may name institutions, never the mechanical resolution structures. Default: paraphrase.

## I.8 Long-Range Coherence
The hero who feared spiders on page five has one as a pet on page fifty; magical objects work for the wrong people.

## V.6 — Too-Clever Constructions
"It worked, but not in the same way" is plain. "It simply worked differently" is too neat.

## V.13 — Single-Author Dominance
Not every passage must contain all twelve authors: a restrained interior monologue may legitimately be 60% Ishiguro by texture. The failure is unmotivated dominance. Symptoms:
- All sentences subordinated and hedged, in content that doesn't require restraint.
- Interior aestheticism throughout, in content that needs landscape or chronicle weight.
- Sensory catalogue without scale-shift or temporal anchor, in content that spans generations or distance.
- Matter-of-fact impossibility running without grounding where grounding is needed.
- Tartt-punch struck repeatedly when no single moment earns the weight.
- No Tolkien-derived technique anywhere despite Tolkien being the highest-weighted author.

## Master Rule — examples
- "The weight of history pressed down upon them." — Could appear anywhere. Cut.
- "Three of the four granary locks had rusted shut." — Belongs only to this place. Keep.
