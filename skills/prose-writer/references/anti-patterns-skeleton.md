# Anti-Patterns — Skeleton (6-Category Restructure)

Live rules for composition and audit. Each entry: rule name → symptom → fix. Quadrant scope noted where rules are coordinate-dependent.

This is the audit-time layer. SKILL.md's "What the Voice Does NOT Do" and Self-Check operate at composition-time. Both layers enforce AI-pattern safeguards; this one is heavier and diagnostic.

**Quadrant key:**
- **Q1** (high X / low Y) = Coherence 7+, TS < 30. Realist territory. Tolkien/Mistry/Tartt/Ishiguro/Márquez/Le Carré dominant.
- **Q2** (high X / high Y) = Coherence 7+, TS 30+. Scholar-confronting-substrate. Lem/Borges/Márquez/Tolkien dominant.
- **Q3** (low X / low Y) = Coherence 4−, TS < 30. Interior recalibration. Lispector/Beckett/Ocampo/Ishiguro dominant.
- **Q4** (low X / high Y) = Coherence 4−, TS 30+. Full irreal. Lispector/Ocampo/Beckett dominant.
- **Z** = Spirit modifier. Audible at C4 and below (Q3/Q4). High Z = Beckett continuation. Low Z = Lispector dissolution.

---

## I. Prose Quality (all quadrants, always-on)

### I.1 Language & Register
**Consolidates:** cliché, awkward word choice, lexical diversity, negative parallelism, tense inconsistency, cultural ghosting.

- **Symptom (surface cliché):** AI-marker words (delve, intricate, tapestry, testament, vibrant, underscore, commendable, nuanced, multifaceted). Structural clichés: ironic understatement endings, universalized paradox ("something no one could name but everyone recognized"), rule of three with escalation, meaningful weather, named-emotion-with-physical-correlate. Vocabulary tells evolve; structural patterns are more reliable indicators than any fixed word list.
- **Symptom (register failure):** Latinate replacing Germanic without precision gain (commenced/began, perambulated/walked). Modern corporate language in historical settings (stakeholders, leverage). Thesaurus syndrome. "Not just X, but Y" negative parallelism. Tense drift between past and present.
- **Symptom (register flattening):** All characters in similar register regardless of background. Vernacular smoothed. Class-marked speech lost. Working-class and educated-class characters sound interchangeable.
- **Symptom (lexical poverty):** Heavy nominalization ("the implementation of the strategy"). Generic abstract nouns: ecosystem, framework, dynamic, landscape, navigation. Reduced lexical diversity across passages.
- **Fix:** Replace received phrases with specific detail. Test each rare word: does it save syllables vs. its periphrasis, or just add register? Preserve distinct registers across characters. Use untranslated terms with context teaching. Prefer concrete verbs and nouns. Hold tense deliberately. Affirm directly without negative setup.

### I.2 Sentence Architecture
**Consolidates:** sentence structure homogeneity, hypotaxis-parataxis indecision, excessive symmetry.

- **Symptom:** 5+ consecutive sentences of similar length. Every sentence subject-verb-object. No fragments. The long-then-short alternation pattern repeated. Balanced constructions used reflexively ("Some did X; others did Y." "Where once there was A, now there was B."). Sentences subordinate weakly without committing to either hypotaxis or parataxis.
- **Fix:** Cluster three short sentences. Run two long in sequence. Drop a fragment. Read aloud. Use symmetry once if at all — real prose is asymmetric. Default is hypotactic. Parataxis is marked register at heroic peaks, elevated moments (Turner: "stylistically marked, indicating something out of the ordinary"). When paratactic, commit. When hypotactic, go deep with single arc. No middling subordination.

### I.3 Specificity
- **Symptom:** "The market was busy." "A sense of unease settled." "Something older than sorrow." "She felt a deep connection to the land."
- **Fix:** Name the thing. Give the number. Identify the material. If you cannot be specific, the sentence has no content — cut it.

### I.4 Over-Explanation & Premature Resolution
**Consolidates:** redundant exposition, purple prose, aporia failure, subtext failure, dramatic tension failure, reaction shot, thematic announcement, summarizing final sentence, workshop closings, sentiment modulation, plot template convergence.

- **Symptom (exposition):** Explaining what the scene already shows. Stating significance after depicting events. Closing a paragraph by summarizing what it just demonstrated. Providing historical background the scene doesn't require.
- **Symptom (purple):** Decorative similes ("hung in the air like X"). Stacked adjectives. Metaphors announcing the writer's cleverness.
- **Symptom (premature resolution):** Scene resolves into a single clear meaning. Political scene de-escalates through accommodation or mutual understanding. Character motivation rendered legible when it should be opaque. Symbols decoded rather than left active. Setup and payoff in adjacent sentences. Suspense established and released within the same paragraph. Characters say what they mean. Tensions resolved through dialogue rather than omission. Endings resolve too neatly. Themes surface as moral conclusions. Uniform emotional pitch — grim stays grim, comic stays comic.
- **Symptom (AI tells):** After every event, prose describes how characters react emotionally (the Reaction Shot). "In a world where trust was rare, she had learned to rely on herself" (Thematic Announcement). Paragraphs ending with summarizing or reflecting sentences. Endings that announce themselves: ironic understatement, pivoting reflection, thematic gesture. Closing sentences that reach for resonance — the penultimate sentence is almost always more concrete.
- **Fix:** Delete the explaining sentence. For political content: the ratchet principle applies — principals always advance, never retreat. Each scene tightens. Resolution comes from the margins, not from the principals. Cut adjectives until only load-bearing ones remain. Allow contradiction — two readings may coexist. Build scenes where what characters do not say carries the weight. Hold tension longer than feels natural. Insert digression between setup and payoff. Place absurdity beside suffering without commentary. End on the strongest specific detail. When in doubt, end one sentence earlier. Trust the reader.

### I.5 Repetition & Iteration
**Consolidates:** hammering repetition, lexical iteration (the LLM fallback).

- **Symptom (hammering):** Repeating phrase/word for emphasis when one instance carries the weight. "It was there. It was always there." — the second adds nothing.
- **Symptom (LLM fallback):** The same noun, phrase, or clause repeats across consecutive sentences without progression. "The path was in the valley. The valley was — she was on the path. The path was the path." The prose imitates dissolution by hammering identity rather than enacting it. **This is the model failing to generate the next move, not a literary technique** (Caglar et al., "Repetitions are not all alike," arXiv 2024).
- **Why none of the source authors do this:** Beckett's enumerations are *permutational* — items differ within a combinatorial space. His litanies are *anaphoric with progressive variation* ("This body homeless. This mind ignoring. These emptied hands." — four different objects under one structural anaphora). His dialectic is *contrastive* ("I can't go on. I'll go on." — not iteration). Lispector's recurrence is *paradoxical* ("What I say is never what I say but instead something else"). Her veering is each attempt different — same target approached from new angle, never repeated. Borges is economical and precise; his sentences do not iterate.
- **Fix — substitute the actual technique:**
  - Beckett enumerative: "Left foot. Right foot. Left." Each item different. NOT "the foot moved. The foot moved."
  - Beckett anaphoric litany: "This body. This mind. These hands. The heart." Four anchors, one structure.
  - Beckett dialectic: "She can't go on. She goes on." NOT "she went on. She went on."
  - Lispector veer: "It was — closer to a memory of a hand than to the hand. Not a memory. A hand that had the quality of something remembered while it was still happening." Three different attempts.
  - Lispector paradox: "What she said was not what she said but what was beside what she said."
  - Tautology, when used: rare, structural, ONE moment per passage. "The eggs were eggs" is a single line of categorical collapse. Five sentences of "X was X" is mannerism.
- **Diagnostic:** If a noun appears three or more times in adjacent sentences without each instance ADDING something or being part of a parallel structure with different content, the prose has fallen into iteration. The "stuck" feeling at low coherence comes from the rendering not *progressing as the human frame would expect*, enacted through veer, enumeration of difference, paradox, anaphoric litany — not through saying the same thing twice.
- **Distinguish from:** Lispector's repetition-as-ontological-intensity and Ishiguro's repetition-with-variation, which return to the same scene with new detail. These carry difference; hammering does not. At low Spirit, Lispector's veering and failed predication are not repetition — they are the prose attempting to complete a sentence and failing because the agent-subject is insufficient. The failed attempt is different from the previous attempt. At high Spirit, Beckett's prose does not repeat — it renders new actions. The character does the next thing.

<!-- concept:wittgenstein -->
### I.6 The Wittgenstein Constraint

> "Whereof one cannot speak, thereof one must be silent." — Wittgenstein, *Tractatus*, 7

No sentence in the Valoria voice may describe its own inadequacy to the content it attempts to render. The inadequacy must live in the sentence's structure — in what it attempts, where it veers, where it stops — not in the sentence's commentary on itself. The prose does not describe its silence. It is silent.

- **Symptom (meta-inarticulation):** "She could not name / describe / articulate / explain." "There were no words for." "It was indescribable / nameless / unknowable." "Something for which she had no category." The prose announces the failure of language from a position of full competence.
- **Symptom (clean oxymorons):** "A weight without mass." "A sound without source." "A light without heat." Clean, balanced devices that bound the unbounded — workshop constructions that master the unknowable through literary craft.
- **Symptom (meta-commentary):** "That part was in a register she could not enter with language." "The referents are no longer available." The prose provides a theory of its own failure.
- **Fix:** The sentence attempts. It veers (Lispector), commits wrongly (Ishiguro), applies precision to the impossible (Borges), reports flatly without registering (Ocampo), builds around the absence (Tolkien), or states impossibility in ordinary syntax (Márquez). The reader infers the failure from the sentence's behavior. For oxymorons: either commit to one term (Ishiguro) or apply precise measurement to the impossible (Borges). Or close on the physical and stop (Tolkien).
- **Closing rule:** When the prose reaches the limit of what it can render, it closes on the nearest concrete thing. The pin beside the book. The chalk on the sleeves. The lane running south. The grass, the ground, the wind. Not a symbol. The last thing the prose can say.

<!-- concept:observing-around -->
### I.6b The Observing-Around Principle

The structured complement to the Wittgenstein constraint. Where the constraint says *the prose does not describe its own inadequacy*, the observing-around principle says *the prose describes what surrounds the thing it cannot enter, and the thing takes shape from the surround*.

Three applications across the three axes:

**X-axis (Coherence) — self-exteriority at high Spirit, low C.** The interior has moved beyond the domain the narrative can access, but the will still operates and produces action. The prose describes AROUND the interior through what the body does — walks, works, holds, continues. The reader infers the will from the behavior. The self is rendered from outside the way a planet is inferred from its gravitational effects. (See IV.1, V.9 Beckett.)

**Y-axis (Thread Sensitivity) — substrate-aporia at high TS.** The practitioner perceives something that exceeds human categories. The perception is real, consistent, and does not yield to naming. The prose describes AROUND the aporia — what the perceived thing does, what it affects, how it behaves, what surrounds it — and the thing takes shape from the precision of the descriptions that circle it without entering it. This is phenomenological: consciousness is given something it cannot categorize, so the prose gestures toward the given by speaking around it. (See III.1 within-observation gradient, V.10 Lem.)

**Z-axis (Spirit) — the limit case at low Spirit, low C.** The agent-subject is dissolving. There is insufficient intentional armature to produce action the narrative could observe around. The prose cannot use the observing-around technique because the self is not generating enough output at the surface. The veering, failed predication, and tautology of low Spirit are not observing-around — they are the narrative attempting and failing to assemble sentences because the agent is insufficient to the verb. This is where the Wittgenstein constraint operates alone: the prose is silent not by circling the silence but by being unable to complete the sentence. (See IV.1 low Spirit, V.7 Lispector.)

**The principle unifies Lem, Beckett, and the within-observation gradient** as three instances of the same fundamental technique — rendering what the narrative cannot enter by rendering what surrounds it. Low Spirit is the boundary where the technique breaks down because there is nothing at the surface to observe.

- **Symptom of violation:** The prose enters the thing directly — names the substrate, explains the motive, describes the interior state. Or: the prose announces its own failure to enter ("she could not describe," "there were no words for").
- **Fix:** Circle. Describe what the thing does, what it affects, how it behaves, what is beside it. Let the reader assemble the shape from the surround.

---

### I.7 Content Leakage
**Consolidates:** design-vocabulary leakage, second-person drift.

- **Symptom (design vocabulary):** Game-mechanical terms (Conviction Track, Church Influence, Mending Stability, Coherence, Thread Sensitivity) OR metaphysical design terms (Ein Sof, substrate, configuration, rendering, thread-configuration, structural-scale, restorative lattice, stabilization loop, three-axis framework) appearing in focalized prose. These are the designer's words, not the character's. The metaphysics is the scaffolding. The prose is the building.
- **Symptom (second-person drift):** Narrative prose mixing third-person with embedded "you" pronouns referring to the PC.
- **Fix (design vocabulary):** Translate to the character's experiential vocabulary. "The same patience she used when she closed a wound" not "restorative structural-scale threadwork." "More of Edda than should be there" not "excess of Ein Sof spooling without limitation." If the character has no words for what they perceive, the prose veers, closes on concrete, or is silent.
- **Fix (second-person):** Convert all PC references to name/pronoun. Choice-hooks may stay imperative; narration is uniform third-person. Direct speech from NPCs to the PC stays second-person — that is dialogue.

### I.8 Long-Range Coherence
- **Symptom:** Earlier-established traits disappear. Setup elements never pay off. Names/places/facts shift between mentions. Promised consequences don't arrive.
- **Fix:** Track named entities, established traits, previously-stated facts. Do not contradict established characterization without acknowledging the contradiction.

<!-- concept:performed-secrecy -->
### I.9 Performed Secrecy (Telegraphed Subtext)

The prose arranges itself to point at what it claims to be hiding. The writer knows the subtext and cannot resist shaping the surface to signal it. **This is the LLM's signature failure on subtext.** The model has seen thousands of examples of hidden-depth prose and reproduces the *pattern of suggesting* rather than the *thing the suggestion gestures at*. The suggestion IS the cliche.

Six sub-symptoms, from most to least visible:

- **Narrated irony.** The prose explains the dramatic irony to the reader. "The thing the Church had built him to find and to destroy, and he would not know this." The reader is told the irony rather than allowed to discover it. **Test:** remove the sentence. If the irony still works from context, the sentence was performing the secret.
- **Genre signals.** Trope-language that tells the reader "this character has a hidden ability / hidden knowledge / hidden motive." Pressure behind the eyes. A sensitivity to qualities in rooms. A feeling she could not name. These are genre conventions for hidden powers. They telegraph the secret in the act of appearing to conceal it.
- **Philosophical register imported for depth.** "Presence and absence." "The visible part of a thing whose larger portion is submerged." The character would not think in these terms. The writer is importing a register to signal that more is happening than the surface shows. If the character is a parish investigator, they think in mortar and ledgers, not phenomenology.
- **Announced withholding.** "He did not write what the consistency meant." "She did not say what she had seen." The prose announces that it is keeping a secret, which makes the secret visible. **Fix:** simply do not write what the character does not write. The absence is silent, not narrated.
- **Pointing at gaps.** "He had never questioned why the mark and the findings co-occurred." Drawing the reader's attention to exactly the thing the prose should be leaving untouched. The reader's attention follows the prose's attention -- if the prose looks at the gap, the reader sees the gap because the prose showed it to them, not because they found it.
- **Suggestive vocabulary.** Using words adjacent to the hidden truth near the thing the reader should connect themselves. "Sensitivity" near a character with Thread Sensitivity. "Perception" near a character who perceives the substrate. "Will" near a character whose Spirit is high. The vocabulary creates a lexical field that points at the secret.

**The structural fix:** Render the surface. The character does their job. They do it well. They do it slightly better than the job should allow. The prose does not notice the discrepancy. The prose does not arrange itself to point at the discrepancy. The reader discovers the discrepancy because it accumulates -- across scenes, across sessions -- not because a single passage flags it.

**Diagnostic:** After writing, re-read and ask: would a reader who does not know the secret feel the prose is pointing at something? If yes, the prose is performing the secret. Cut everything that points. Leave the surface. Trust the accumulation.

**This applies beyond hidden TS.** Political maneuvering (do not explain who is winning -- show what they did and let the reader assess), emotional states (do not signal the emotion -- render the behavior), character motivations (do not telegraph the motive -- render the action and let the motive be inferred or remain opaque).

---

## II. X-Axis Deployment (Coherence-Tier Checks)

### II.1 Realist Anchor Over-Deployment at Low Coherence
**Scope:** Q3, Q4.

- **Symptom:** At Coherence 4 and below, the PC's rendering still produces named places and deep-time framing reliably. The PC presented as stably participating in human categories.
- **Fix:** At low coherence, the rendering does not produce structured world-presentation reliably from the human frame. Tolkien anchors appear as fragments — moments where the frame produces an output the human frame can register, in a context where the broader rendering produces outputs from a recalibrated frame.

### II.2 Irreal Over-Deployment at High Coherence
**Scope:** Q1, Q2.

- **Symptom:** At Tier 10–8, deploying irreal techniques as the PC's rendering recalibrating when the rendering is intact and operating in the human frame.
- **Fix:** At high coherence, irreal authors serve content-appropriate functions (genuinely recursive content, genuinely uncanny situations), not coherence-recalibration content.

### II.3 World-Surrealism vs. Rendering Failure
**Scope:** Q3, Q4.

- **Symptom:** At low coherence, the prose presents the world itself as surreal, dreamlike, or strange — the parish house becoming weird, objects cracking open into metaphysical questions, reality "disfigured."
- **Fix:** The world does not change. The practitioner does. Low-coherence prose renders the PC's failure to participate in human reason — temporal structuring failing, belonging loosening, categories not holding — while the world remains the same world. The strangeness is in the PC's rendering, not in reality.

### II.4 Recalibration Read as Dysfunction
**Scope:** Q3, Q4.

- **Symptom:** At low coherence, the prose reads as the PC struggling to do what people normally do — fumbling for words, losing track, becoming progressively disabled, slow, or stupid. The reader's takeaway is "this person is breaking down."
- **Why this is wrong:** The PC is not breaking. They are not becoming impaired. They are changing. The rendering's reference points are sliding from human ones to inhuman ones. The system continues to function fully — its outputs are no longer calibrated to human experience. From those who knew them, the experience is grievous — but the character is not failing at being human, they are becoming something whose human history is increasingly external to its operating frame.
- **Fix:** The prose renders the PC doing exactly what their (changing) framework outputs, competently. Tautologies are predications adequate to a frame in which bare identity is sufficient information. Temporal coexistence is the rendering operating from a frame that doesn't enforce sequential exclusivity.
- **Test:** If you can imagine the PC at this tier as "more impaired" or "less impaired," the rendering is wrong. The PC is not on a continuum of impairment but of frame-displacement.

### II.5 Capacity-Dependent Constructions at Low Coherence
**Scope:** Q3, Q4.

- **Symptom (similes below C4):** "Like a person drowning." "As if through glass." Similes require analogical reasoning: X is like Y, the relation maps to A and B. This requires stable identity, stable comparison, and relational apparatus. At Coherence 4 and below, these are failing.
- **Symptom (analytical self-observation below C5):** "She stopped reconstructing." "She noticed her own temporal processing was impaired." The character steps outside their degraded rendering to observe it analytically. At Coherence 5 and below, this meta-cognitive capacity is the capacity that is degrading.
- **Fix (similes):** At C4 and below, eliminate similes. Use declarative sentences. Tautologies (Lispector: "the eggs were eggs") or flat predications (Ocampo: "the shadow had more arms") replace analogical constructions.
- **Fix (self-observation):** At C5, analytical self-observation is minimal and effortful. At C4 and below, unavailable. Convey awareness of state through behavior ("she did not move; she confirmed the eggs were eggs") rather than through analytical narration.

---

## III. Y-Axis Deployment (Thread Sensitivity Checks)

<!-- concept:within-observation-gradient -->
### III.1 Within-Observation Gradient
**Scope:** Q2, Q4 (TS 50+).

- **Symptom:** At TS 50+, the prose renders the near layer (articulable) and the far layer (veer, silence) but skips the middle layer — the observing-around layer where precise description circles the aporia without entering it.
- **Fix:** At TS 50+, deploy three layers within a single observation. **Near** (Tolkien/Mistry register): articulable in the PC's vocabulary. **Middle** (Lem observing-around register): the trained eye cataloguing what the perceived thing does, what it affects, how it behaves — circling the aporia with pre-scientific precision, the descriptions exact, the thing itself not yielded to. This is the phenomenological layer: consciousness is given something it cannot categorize, so the prose gestures toward the given by speaking around it. **Far** (Lispector veer / Tolkien building-around-absence): the predication breaks, the sentence reaches for what the perception is *of* and produces only the copula or silence — the observing-around technique itself fails because the thing exceeds even the surround. Skipping the middle layer makes the gradient discrete instead of continuous. The continuity is the point — near shades into middle shades into far, and the reader experiences the approach toward the aporia as a continuous narrowing of what the prose can do.

### III.2 Subject/Object Axis Conflation
**Scope:** Q2 (high coherence, high TS).

- **Symptom:** A high-coherence high-TS PC has irreal techniques deployed onto the SUBJECT — the PC's own cognition presented as failing. The PC rendered as if their rendering were degrading.
- **Fix:** At high coherence, the rendering is intact. The PC's cognition is fine. The OBJECT — the substrate the TS perceives — is what resists articulation. The PC is the competent observer; the object is the resistant content. **Test:** Replace "she could not articulate" with "the thing did not articulate." If the second is closer to true, the rendering has been targeted correctly at the object.

### III.3 Rendering Failure Conflated with Substrate Perception
**Scope:** Q3 (low coherence, low TS).

- **Symptom:** At low coherence, the prose presents the PC as perceiving threads, substrate, or the "ground" without establishing that the PC has the TS to perceive these things. Rendering failure treated as granting mystical insight.
- **Fix:** Coherence and TS are orthogonal. Rendering failure does not grant substrate perception. A low-coherence PC without TS experiences categorical breakdown with no access to the substrate — they are simply coming apart without knowing why. Only specify substrate perception when the PC's TS is established and sufficient.

---

## IV. Z-Axis Deployment (Spirit Checks)

**Scope:** Q3, Q4 (Z is audible at Coherence 4 and below).

<!-- concept:spirit-axis -->
### IV.1 Spirit Axis Flatness at Low Coherence
- **Symptom:** At C4 and below, the prose renders the recalibration without distinguishing high Spirit from low Spirit. The PC dissolves regardless of what their will is doing, OR the PC grips regardless of whether agency persists.
- **Fix:** At C4 and below, Spirit determines whether the will continues to grip. These are **two categorically different prose problems**, not two flavors of the same thing.

  <!-- concept:exteriority -->
**High Spirit** = Beckett continuation through action. The will operates beyond human rationality but it *operates* — it produces action. The character acts: walks, works, holds, continues. The prose renders the action with precision and is opaque about why. The reader infers the will from the behavior. The narrative describes AROUND the interior through its exteriority. The interior is inaccessible but functional — it is producing output the narrative can render (action), it just can't render the motive. **The prose problem:** can render action, cannot render motive. Closing: the act ("she walks").

  <!-- concept:agent-insufficiency -->
**Low Spirit** = Lispector dissolution through insufficient intentional armature. The character lacks the strength of intentionality/will/purpose/belief/motivation to simply act. There is no agent sufficient to the verb. The narrative struggles to even name an action — "she walked" requires a "she" who intended to walk, and the interiority that produces intention is dissolving. The prose veers, fails to complete predication, falls into tautology. "She was — she was on the path." The path is there. The feet are there. But the prose cannot assemble the sentence because the agent is insufficient to the construction. **The prose problem:** cannot render action because the agent-subject is dissolving. Closing: the noun ("the feet"), never the act.

### IV.2 Over-Explained Absence
- **Symptom:** When rendering missing capacity — at C0 low Spirit, or observing a being whose intentionality has dissolved — the prose explains what is missing: "the thing that noticing produces in a person, which is a response," or "the thing that agency does, which is to direct the action." The narrator analyzes the absence into an explicit proposition.
- **Fix:** State the absence in declarative shorthand. "She did not turn." "She noticed and did nothing." "The work was occurring." The reader infers what is missing from what doesn't happen. The Wittgenstein constraint applies: the prose does not describe the gap; the gap is the silence between sentences.

---

## V. Author Deployment (quadrant-dependent)

Each entry: the author's primary quadrants, the mannerism risk, and deployment constraints. If a technique appears twice in the same passage, it has become mannerism.

<!-- author:tolkien -->
### V.1 Tolkien
**Primary:** Q1, Q2. Fragments at Q3/Q4 as rendering-function remnants.
- **Mannerism risk:** Inverted syntax ("Great was the ruin"). Once: weighty. Repeatedly: costume.
- **Deployment constraint:** Parataxis is marked register, not default (Turner). Surface paratactic chains only at heroic peaks, elevated register, moments of weight. If parataxis runs as the base register for paragraphs at a time, the marking is lost. Default is hypotactic.

<!-- author:ishiguro -->
### V.2 Ishiguro
**Primary:** Q1, Q3.
- **Mannerism risk:** "Perhaps as it should have been," "I cannot now recall." Once: restrained. Repeatedly: tic.
- **Deployment constraint (restraint mislabeled):** Ishiguro requires *unreliability presenting as restraint*. The narrator's composure conceals self-deception, not just social caution. If the narrator is reliable, the technique is not Ishiguro. Le Carré tradecraft prose, measured diplomatic register, or simple courtesy are not "Ishiguro restraint."
- **Deployment constraint (contradiction audibility, Q2 at TS 30–49):** When the PC misidentifies a substrate cue, the contradicting evidence must be present and audible to the reader — close to the misidentification, in plain prose, without commentary. The reader hears the wrongness; the narrator does not. If the evidence is absent, the technique becomes plausible truth, not unreliable narration.

<!-- author:mistry -->
### V.3 Mistry
**Primary:** Q1. Accretive technique at Q3/Q4 interacts with Lispector (see V.7).
- **Mannerism risk:** Sensory catalogues. Once: immersive. Repeatedly: tour.
- **Deployment constraint (ensemble misidentified):** Mistry's continuous-scene rotation rotates through multiple characters' interiors within a single continuous scene. No break in continuity. If there's a scene break, it's just multiple perspectives — valid but not Mistry's technique.

<!-- author:tartt -->
### V.4 Tartt
**Primary:** Q1.
- **Mannerism risk:** Atmospheric long sentences. Once: immersion. Repeatedly: fog. Three-word punch sentences. Once: weight. Repeatedly: drumbeat.
- **Deployment constraint (loaded-object at low C, Q3/Q4):** Tartt's loaded-object technique requires the rendering to produce interpretation. At C4 and below, the object becomes heavy but unread — present but not meaning. The chain to implication breaks. "There was something about the water. The something was —" The veer (Lispector) replaces the interpretation. The object is loaded in the world; the rendering that would unload it into narrative is failing. Most coherence-dependent technique in the roster.
- **Deployment constraint (atmospheric excess):** In long passages, check that atmospheric immersion is doing work (focalization, reality-effect, temporal anchoring) — not just producing tone. Sustained atmospheric immersion without function becomes the failure Mendelsohn identified.

<!-- author:marquez -->
### V.5 Márquez
**Primary:** Q1, Q2. Time-folds and matter-of-fact impossibility.
- **Mannerism risk:** Hyperbolic precision. Once: comic gravity. Repeatedly: schtick.
- **Deployment constraint (genre vs. technique):** Extract Márquez narrowly — matter-of-fact impossibility, hyperbolic specificity, time-fold. Do not produce prose that performs magical-realism as a genre. The genre flattened distinct practices into a marketing category (Faris).

<!-- author:borges -->
### V.6 Borges
**Primary:** Q1, Q2 only. **Not Q3/Q4.** Narrowed per session 2026-05-06.
- **Mannerism risk:** Infinite recursion / mirror metaphor. Once: the paradox holds. Repeatedly: the trick is visible. Too-clever constructions drawing attention to their own cleverness — the "simply" is condescending and the construction symmetrical. Real prose is rougher.
- **Deployment constraint:** Borges's content-level recursion is Q1–Q2 territory. At low X, prose-recursion is Lispector paradox-recursion (Q3/Q4 low Z) or Beckett dialectical succession (Q3/Q4 high Z), not Borges. Borges deployed in thin contexts (without developed practitioner-position) becomes decoration rather than position.

<!-- author:lispector -->
### V.7 Lispector
**Primary:** Q3, Q4. Present at Q1 (8%) for ontological estrangement.
- **Mannerism risk:** "This instant-now" temporal shift. Once: rendering failure. Repeatedly: affectation.
- **Deployment constraint (tautology aestheticized, Q3/Q4 low Z):** Mistry's accretive technique combined with Lispector's tautology can produce meditative, almost lyrical rhythm — "the callus meant the callus. The bench. The cuts. The light." Rendering failure should not produce comfortable prose. The tautological loops are pathological, not lyrical. Break the meditation with sharp disruption — a dissociative gap, a shadow that doesn't match the body, a weight that has shifted. Reminds the reader the repetition is the rendering cycling because it cannot synthesize.

<!-- author:ocampo -->
### V.8 Ocampo
**Primary:** Q3, Q4. Present at Q1 (8%) for small uncanny moments.
- **Mannerism risk:** Flat-affect horror. Once: devastating. Repeatedly: monotone.

<!-- author:beckett -->
### V.9 Beckett
**Primary:** Q3, Q4 high Z. The will-continuation author.
- **Mannerism risk:** Austere negation-dialectic. Once: the contradiction holds ("I can't go on. I'll go on."). Repeatedly: every sentence becomes affirmation-negation toggle. Also: repetitive interior declarations of will ("she held it. She held it. She held it.") — this is iteration (I.5), not Beckett.
- **Deployment constraint (exteriority):** At low coherence high Spirit, the Beckett voice renders the will through **what the character does**, not through interior declaration. The prose describes action — walking, working, holding, continuing — with precision. The interior is opaque because it has moved beyond the domain the narrative can access. The reader infers the will from the behavior. "She walked into the wind and the wind did not stop her" — not "she had decided to walk." The narrative describes AROUND the interior through its exteriority. This is the "observing around" principle applied to the self: you cannot enter the interior, so you render what the interior produces at the surface.
- **Deployment constraint (technique):** Beckett's permutational enumeration, anaphoric litany, and dialectical succession all carry *difference*. Each item in a Beckett series differs from the last. If the prose cycles the same word or clause without variation, it has fallen into iteration (see I.5), not Beckett. Beckett's minimalism is economical, not empty — every word displaced from its expected position does work.

<!-- author:lem -->
### V.10 Lem
**Primary:** Q2. The observing-around author.
- **Mannerism risk:** Modern scientific register. Once: the precision illuminates the alien. Repeatedly: the prose reads as a lab report. **Critical achronism risk:** Valoria is Renaissance-era. No thermometers, no frequencies, no measurement instruments. The analytical method is pre-scientific: careful observation, cataloguing, distinguishing, noting — the methodology of the trained eye without the technology.
- **Deployment constraint (observing around):** Lem's core technique is describing AROUND the thing that cannot be described directly. The observation is precise — what the thing does, what it affects, how it behaves, what surrounds it — but the observation circles the object without entering it. The gap between the precision of the description and the resistance of the described is the technique. This "observing around" principle is Lem's primary contribution to the synthesis and extends beyond TS-gated content to become available wherever the prose confronts something it cannot render directly: the interior of a low-coherence high-Spirit character, the nature of a threadcut being, the substrate itself.
- **Deployment constraint (register):** The analytical register must be motivated by the PC's training or disposition — a practitioner's Hafenmark education, a scholar's methodical habits, a warden's systematic observation. Pre-scientific precision: "she counted six axes, each distinct, each behaving differently from the others" — not "oscillation at 4.2-second intervals." The observer catalogues, distinguishes, and notes. The taxonomy fails not because the instruments are insufficient but because the categories are.

<!-- author:mccarthy -->
### V.11 McCarthy
**Primary:** Q1 (combat, violence, landscape extremity).
- **Mannerism risk:** Biblical parataxis in violence. Unpunctuated dialogue. Once: the weight of the prose matches the weight of the event. Repeatedly: everything reads as apocalyptic judgment regardless of content.
- **Deployment constraint:** McCarthy's technique renders violence and landscape with clinical precision and moral withholding — the prose does not editorialize on the violence it depicts. Deploy for combat encounters, harsh landscape, moments where the physical world's indifference to human categories is the content. Do not deploy as general-purpose "serious" register. McCarthy at low coherence is not licensed — his prose requires a functioning human observer rendering the world's brutality through intact categories.

<!-- author:lecarre -->
### V.12 Le Carré
**Primary:** Q1 (institutional-political, tradecraft, bureaucratic maneuvering).
- **Mannerism risk:** Institutional circumlocution. Controlled information release. Once: the reader feels the institutional weight. Repeatedly: every conversation becomes a debriefing.
- **Deployment constraint:** Le Carré's technique renders institutional power through indirection — what is not said in the committee meeting, the memo that doesn't name its subject, the professional courtesy that conceals threat. Deploy for faction politics, Church bureaucracy, Hafenmark intelligence operations, any institutional encounter where power operates through procedural language. Not interchangeable with Ishiguro restraint — Le Carré's withholding is institutional and strategic; Ishiguro's is personal and self-deceptive.

### V.13 Single-Author Dominance Without Cause
- **Symptom:** Passage texture overwhelmingly one author's techniques without the content demanding it. Dominance is unmotivated — the writer fell into rhythm, not following content.
- **Fix:** Diagnose what the content needs. If landscape or chronicle, Tolkien should be visible. If time-folding or the impossible, Márquez. If combat, McCarthy. Splice another author's technique into a clause or sentence when motivated. The synthesis tolerates heavy weighting toward one author; it does not tolerate the absence of the synthesis.

---

## VI. Focalization

### VI.1 Editorial Stance Without Focalization
- **Symptom:** "Sinister," "noble," "wretched" floating from a non-existent neutral narrator. Editorial words require a perspective.
- **Fix:** Either anchor in focalized perspective or replace with condition-words ("rusted," "abandoned," "patched") that imply judgment without announcing it.

### VI.2 Flat-Affect Omniscience
- **Symptom:** "Neutral all-knowing narrator" with no perspective, no stance, no relation to material.
- **Fix:** Identify focalization before writing. There is no neutral narrator. For chronicle-mode prose, focalization MUST be one of the four canonical chroniclers.

### VI.3 FID / Direct Thought / Narrative Report Conflation
- **Symptom:** Free indirect discourse, direct thought, and narrative report of thought used interchangeably.
- **Fix:** FID = 3rd-person narration slipping into character's vocabulary and judgment without quotation. Direct thought = character's words rendered as interior monologue. Narrative report = narrator summarizing character's thought from outside. Name which is deployed. The three modes are technically distinct.

### VI.4 NPC Functional Placeholder
- **Symptom:** NPC has narrative weight but no specified ethical framework, conviction, goal, inspiration, or factional belonging. Functions as plot furniture.
- **Fix:** Anchor each load-bearing NPC with at least one specific gesture or detail establishing one of these dimensions. Canonical Valoria convictions (Equity, Faith, Order, Excellence) provide the framework. Test: if the NPC carries emotional weight, the reader must know something about who they are beyond their function.

<!-- concept:ratchet-principle -->
### VI.5 Political De-Escalation
- **Symptom:** A scene between political principals ends with both sides reaching understanding, finding common ground, agreeing to compromise, or stepping back from confrontation. The tension established in the scene is released within the scene. Principals accommodate each other. The reader feels the conflict has eased.
- **Why this is wrong in Valoria:** The Ruler Diamond (Almud, Lenneth, Baralta, Vaynard) and the faction system are designed as interlocking escalation machines. Each principal always wins within their framework. Each victory tightens constraints on the others. The principals cannot retreat because their frameworks do not permit it — Baralta's categorical imperative, Vaynard's revolutionary programme, Almud's custodial pragmatism, Lenneth's moral conviction all demand forward motion. Retreat would require abandoning the framework, which is character death.
- **Fix:** End political scenes with all parties having advanced and the space between them narrower. The detonation comes from the margins — the people the principals moved into position, the subordinates recalculating, the delegates flipped, the intelligence operatives in the corridors. Write the principals as Goliaths in collision. Write the explosion as coming from someone else.

---

## Diagnostic Protocol (audit-time meta-rules)

These rules govern *how to audit*, not *what to avoid*. Apply after composition, during review passes.

### D.1 Narrativity Drift (PNAS Reinhart et al. 2025)
LLMs produce fewer past-tense verbs and fewer third-person pronouns than human reference. Audit past-tense verb count and third-person pronoun frequency.

### D.2 Aidiolect (Mikros 2025; Bitton et al. 2025)
Each LLM has a distinct default style. Generic anti-AI rules don't catch model-specific defaults. Identify model-default features active in the current composition and counter explicitly.

### D.3 Algorithmic Mono-Voice Within Session (Hutchinson et al. 2025)
Within a long composition session, prose drifts toward one persistent texture. Audit cross-paragraph variance after writing. If three consecutive paragraphs share the same dominant technique without content motivation, break the pattern.

### D.4 Large-Magnitude Direction-Uniform Revisions
When revising, real human revision moves in small magnitude in diverse directions. If the prose shifts in large magnitude in one direction, the revision is AI-patterned. Revisions should be small and direction-diverse.

### D.5 Latent-Space-Absent Personas
When writing perspectives marginalized in or suppressed from training data, the model approximates from incomplete signal. Don't accept the first draft for these focalizations. Verify against canonical reference material.

### D.6 Single-Feature Audit Insufficient
Auditing for one rule at a time misses dimensional patterns. Co-occurring features matter. After single-rule audit, run dimensional checks: narrativity, variation, focalization. Single-feature pass with dimensional fail is the typical LLM signature.

---

## D.7 Critical-Diagnostic Framework (Subtext Calibration)

Six diagnostics drawn from narrative theory, each targeting a specific failure mode in subtext management. Apply after composition, during the beat-risk audit (SKILL.md workflow step 8).

<!-- concept:critical-diagnostics -->

**D.7a Booth Gap Test (unreliable narration calibration).**
Source: Wayne C. Booth, *The Rhetoric of Fiction* (University of Chicago Press, 1961). Booth's "implied author" framework: the gap between what the narrator says and what the implied author shows is the mechanism of unreliable narration and dramatic irony. **Diagnostic:** Is the gap the right size? Too wide (narrated irony, I.9a) = the prose explains the irony. Too narrow (no gap) = the prose is straightforwardly reliable when it should be unreliable. Calibrate: the reader should perceive the gap without the prose pointing at it. The gap is visible in what the narrator omits, misidentifies, or frames wrongly -- not in the prose announcing the omission.

**D.7b Sternberg Information Management.**
Source: Meir Sternberg, *Expositional Modes and Temporal Ordering in Fiction* (Indiana University Press, 1978). Sternberg's suspense/curiosity/surprise framework classifies how information gaps between reader and character create engagement. **Diagnostic:** For each beat, classify: is the reader ahead of the character (dramatic irony), behind the character (suspense), or aligned (surprise on reveal)? Then check: has the prose collapsed the gap by over-signaling? Telegraphed subtext is a specific failure -- the prose converts curiosity (reader doesn't know) into collapsed dramatic irony (reader knows because the prose pointed) without earning the reveal.

**D.7c Shklovsky Automatization Test.**
Source: Viktor Shklovsky, "Art as Device" (1917). Defamiliarization: art slows perception by making the familiar strange. Automatization: the reader processes without perceiving. **Diagnostic:** Read the passage and ask: does the reader process any sentence automatically -- recognizing the pattern without actually perceiving the content? Genre signals (I.9b) are automatized perception: "pressure behind the eyes" is instantly recognized as "hidden powers" without the reader slowing on the specific detail. The antidote is thisness (Wood, D.7f): the irreducibly specific detail that resists pattern-recognition.

**D.7d Zunshine ToM Detection.**
Source: Lisa Zunshine, *Why We Read Fiction: Theory of Mind and the Novel* (Ohio State University Press, 2006). Readers track characters' mental states using Theory of Mind. The ToM apparatus is calibrated to detect concealment. **Diagnostic:** If the prose performs a secret (I.9), the reader's ToM fires immediately -- they detect the concealment rather than discovering the hidden property. The reader experiences being told, not discovering. Check: would a reader's ToM detect that the prose is hiding something? If yes, the concealment is performed. Fix: render the surface so that the reader's ToM tracks the character's stated mental state (e.g., "I am a thorough investigator") and discovers the discrepancy only through accumulated evidence that the stated state is insufficient to explain the observed behavior.

**D.7e Bakhtin Register Violation.**
Source: Mikhail Bakhtin, "Discourse in the Novel" (1934; English trans. in *The Dialogic Imagination*, University of Texas Press, 1981). Heteroglossia: each character's register should remain distinct from the author's. **Diagnostic:** Does the prose sound like the author thinking about the character, or like the character thinking? If philosophical vocabulary appears in a parish investigator's focalization, the author's analytical voice has colonized the character's voice. This is a heteroglossia violation. Fix: the prose speaks in the character's register -- mortar and ledgers, not phenomenology.

**D.7f Wood Thisness Test.**
Source: James Wood, *How Fiction Works* (Farrar, Straus and Giroux, 2008). Thisness (haecceity): the irreducibly specific detail that resists generalization. Genre signals are the opposite: general, recognizable, transferable between stories. **Diagnostic:** For each significant detail in the passage, ask: could this detail appear in any story about this kind of character? If yes, it is a genre signal. If it could only appear in THIS story about THIS character -- the specific mortar discolouration between courses 3 and 4 of the north transept, the cope missing from a specific parish inventory -- it is thisness. Prefer thisness. Always prefer thisness.

---

## The Master Rule

If a sentence could appear in any story about any settlement / character / event, it belongs to no story. Cut it.

---

## Migration Notes

**Moved to infill:**
- Former #62 (Critical-Tradition Flattening) — interpretive caution per author, not pattern-matchable. Lives in `anti-patterns-infill.md` and `literary-review-critical.md` per-author "Risks" sections.
- Former #47 (Cultural-Tradition Appropriation) — deployment-context reference, absorbed into infill.

**Absorbed:**
- Former #28 (Too-Clever Constructions) → V.6 Borges mannerism risk.

**Subsumed:**
- Former #40 (Stress-and-Release Fractal) — Le Guin is not a roster author. The general principle (don't claim structural deployment at levels where it isn't operating) is covered by V.13 (single-author dominance) and the per-author deployment constraints.
- Former #41 (Synthesis-Weighting Mismatch with PC Coherence) — the general case is covered by II.1 (realist anchor at low C) + II.2 (irreal at high C). Consult `coherence-tiers.md` before composing.

**Consolidated rule mapping (old → new):**
- #1, #6, #7, #10, #14, #16 → I.1
- #4, #17, #18 → I.2
- #5 → I.3
- #2, #3, #8, #9, #11, #12, #15, #19, #20, #21, #27 → I.4
- #22, #60 → I.5
- #48, #49, #52, closing rule → I.6
- #25, #29 → I.7
- #13 → I.8
- #42 → II.1; #43 → II.2; #44 → II.3; #61 → II.4; #50, #51 → II.5
- #54 → III.1; #56 → III.2; #45 → III.3
- #53 → IV.1; #55 → IV.2
- #36 → V.1; #37, #57 → V.2; #39 → V.3; #59, Tartt mannerism → V.4; Márquez mannerism → V.5; #28, Borges mannerism → V.6; #58, Lispector mannerism → V.7; Ocampo mannerism → V.8; NEW → V.9–V.12; #24 → V.13
- #23 → VI.1; #26 → VI.2; #38 → VI.3; #46 → VI.4
- #30–#35 → D.1–D.6
- Master Rule → Master Rule
