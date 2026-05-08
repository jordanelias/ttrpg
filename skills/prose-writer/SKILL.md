---
name: prose-writer
description: "Write narrative prose for Valoria using its singular literary voice — a coherence-indexed weighted synthesis of Tolkien, Borges, Lispector, Ocampo (Silvina), Márquez, Ishiguro, Mistry, Tartt, Beckett, Lem, McCarthy, and Le Carré. The synthesis weights shift across tiers indexed to player-character coherence (10-8, 7-5, 4-3, 2, 1), reflecting the progressive failure of the practitioner's self-rendering as a human configuration. Use this skill whenever the user asks to write prose, narrative passages, lore entries, character vignettes, settlement descriptions, faction histories, dialogue scenes, codex entries, cutscene scripts, flavor text, or any creative/narrative text."
---

# Prose Writer

This is the Valoria narrative voice. It is a single literary voice, not a toolkit. All story prose for Valoria sounds like this.

The synthesis is a single integrated voice. All twelve authors contribute. The writer does not select between them. What differs is *weighting* — how often each author's techniques surface, and the weighting itself shifts with player-character coherence.

## Workflow

1. Read this `SKILL.md` (you are here).
2. **Read all skeleton files (mandatory before composition):**
   - `references/techniques-skeleton.md` — technique inventory as rule list
   - `references/anti-patterns-skeleton.md` — failure-mode rules as symptom→fix triplets
   - `references/calibration-skeleton.md` — source-author anchors as use-when reference
3. **Determine the PC's coherence tier, Thread Sensitivity, and Spirit.** Consult `references/coherence-tiers.md` for the tier-tables (10-8, 7-5, 4-3, 2, 1). All three axes are orthogonal and independently affect the prose. If coherence is not established, default to Tier 10-8. If TS is not established, default to 0. If Spirit is not established, default to mid-range (3–4) — neutral, neither agency-grip nor agency-dissolution dominant.
4. **If prose involves Church speakers, religious texts, or characters with established Certainty levels:** consult Solmund Voice canon at `designs/world/solmund_voice_v30.md` per the scoped-override section below.
5. Identify focalization. For chronicle-mode prose, this MUST be one of the four canonical chroniclers per P-03.
6. **Plan beats with cliche risk flags (for non-trivial passages).** Before writing, outline the passage's beats. For each beat, identify the specific cliche or anti-pattern most likely to fire. One line per beat. This is a risk register, not a template.

   Example (Haelgrund investigation scene):
   - Beat 1: arrives at parish, observes staff. **Risk:** genre signals for hidden powers (I.9b — "a sensitivity to qualities in rooms")
   - Beat 2: examines accounts, finds nothing wrong. **Risk:** announced withholding (I.9d — "he did not write what the consistency meant")
   - Beat 3: formal interviews, asks his own questions. **Risk:** pointing at gap (I.9e — drawing attention to what he doesn't question)
   - Beat 4: finds physical evidence. **Risk:** philosophical register (I.9c — "presence and absence" to describe a discolouration in mortar)
   - Through-line: TS 12 operating beneath awareness. **Risk:** narrated irony (I.9a — explaining the dramatic irony to the reader). **Structural fix:** render surface only. He is good at his job. Slightly better than good explains. Never flag the gap.

   Example (Baralta/Vaynard/Almud Diet scene):
   - Beat 1: chamber setup. **Risk:** telling the reader who will win (I.4 premature resolution)
   - Beat 2: tariff debate, Vaynard's data. **Risk:** making Vaynard the clever one (imbalanced characterization)
   - Beat 3: Baralta's counter-motion. **Risk:** diminishing her — she always wins (ratchet principle VI.5)
   - Beat 4: Almud's intervention. **Risk:** making him the mastermind above the other two (same — all three are Goliaths)
   - Through-line: escalation. **Risk:** equilibrium framing — "the balance held." **Structural fix:** each party advances, none retreats, space narrows.

   Skip this step for single-paragraph prose, dialogue lines, or codex entries. Use it for any scene with subtext, hidden character properties, political dynamics, or multi-character encounters.

7. Write. Apply techniques as content, focalization, and coherence tier demand. Multiple authors per sentence is normal.
8. **Audit against the beat-risk flags.** For each flagged risk in step 6, check whether the written passage triggered it. This is the targeted review — not a general audit but a check against the specific traps identified before writing. Then run the general self-check (below).
9. **General audit** using the skeletons as live rule-set, not memory check.
10. **Infill-on-demand:** If a skeleton rule needs deeper context (rationale, expanded examples, academic citation, full technique discussion), load the matching section from the corresponding `-infill.md` file. Do not load full infill files routinely.

The skeletons are the live working memory during composition. The infill files are reference material for cases where a rule needs justification or expansion.

## Coherence-Indexed Weighting Principle

Coherence measures the structural integrity of the practitioner's always-already self-rendering — the unconscious process that maintains their being as a human configuration. Rendering has two facings: epistemic (transforming raw givenness into intelligible experience) and ontological (the practitioner perduring and belonging in their environment). As coherence degrades, both facings fail. The practitioner participates less in the bounds of human reason.

The synthesis weights shift across tiers aligned to the canonical coherence thresholds (threadwork_v30 §3.3): 10-8 (Stable), 7-5 (Dissonant), 4-3 (Fragmented), 2 (Fractured), 1 (Severed), 0 (Rendering Crisis / NPC). The world does not change. The practitioner does. Realist authors decrease because the PC's ability to render the world in human categories degrades. Irreal authors increase because the prose must render categorical failure — temporal structuring breaking, logical structure loosening, belonging eroding.

Coherence is orthogonal to Thread Sensitivity AND to Spirit. Three axes operate independently:

- **Coherence (10–0)** determines rendering integrity — whether the PC's self-rendering holds them as a human configuration.
- **Thread Sensitivity (0–100)** determines substrate perception — what the PC perceives beyond ordinary human capacity.
- **Spirit (1–7, the metaphysical attribute)** determines agency persistence — whether the will continues to grip when rendering fails.

The prose must not conflate them. A low-coherence PC without TS experiences rendering failure as inexplicable breakdown. A low-coherence PC with TS experiences rendering failure AND substrate perception — but one does not cause the other. <!-- concept:spirit-axis -->
The Spirit axis becomes audible at Coherence 4 and below, producing two **categorically different prose problems**:

<!-- concept:exteriority -->
- **High Spirit (Beckett):** The will operates beyond human rationality but it *operates* — it produces action. The prose renders what the character does (walks, works, holds, continues) and is **opaque about why**. The interior is inaccessible but functional. The reader infers the will from the behavior. The narrative describes AROUND the interior through its exteriority.
<!-- concept:agent-insufficiency -->
- **Low Spirit (Lispector):** The intentional armature is dissolving. The character lacks the strength of will/purpose/belief to simply act. The prose **cannot name an action** because naming "she walked" requires an agent who intended to walk, and the agent is insufficient to the verb. The prose veers, fails to complete predication, falls into tautology. "She was — she was on the path."

These are not two flavors of the same thing. High Spirit: can render action, cannot render motive. Low Spirit: cannot render action because there is no agent sufficient to the verb.

See `references/coherence-tiers.md` for the tier-tables with deployment notes, the TS interaction guidance, the Spirit interaction guidance, and per-tier anti-patterns.

## Author Weighting (Tier 10-8 Default)

When coherence is unspecified, use the Tier 10-8 (Stable) weighting. Weights are 2D — indexed by both coherence and Thread Sensitivity:

<!-- author:all-weights -->
| Author | TS 0-29 | TS 30-49 | TS 50+ | Role |
|---|---|---|---|---|
| Tolkien | 24 | 20 | 15 | Ground. Landscape, deep-time, named specificity. |
| Mistry | 12 | 10 | 8 | Occupational specificity, body-as-record. |
| Tartt | 11 | 9 | 7 | Atmospheric retrospection, loaded objects. |
| Ishiguro | 11 | 11 | 10 | Situational restraint, unreliable narration. |
| Márquez | 11 | 12 | 12 | Time-folds, matter-of-fact impossibility. |
| Lispector | 8 | 10 | 12 | Ontological estrangement. |
| Ocampo | 8 | 7 | 7 | Small uncanny moments, flat-affect rendering. |
| Borges | 7 | 10 | 12 | Recursion, fictive-as-real, heresiarchs. |
| Lem | 0 | 5 | 10 | Observing-around. Pre-scientific analytical observation. TS-gated. |
| McCarthy | 4 | 3 | 3 | Violence, landscape indifference. Content-gated. |
| Le Carré | 3 | 2 | 2 | Institutional indirection. Content-gated. |
| Beckett | 1 | 1 | 2 | Will-continuation. Spirit-gated at C4 and below. |

For other tiers and the Spirit modifier, consult `references/coherence-tiers.md`.

## Intra-Sentence Splicing

Authors blend within a single sentence, not just across sentences. This is the synthesis at its most invisible — when multiple authors' techniques appear in different clauses of the same sentence, the prose stops feeling like any one mode and starts feeling like the unified voice.

Splice rules:
- Authors may shift between clauses or across conjunctions within a single sentence
- The grammar of the whole sentence must remain sound
- Shifts should serve the content, not display the technique

Example with four authors in one sentence:

> The harvests had failed for three years before anyone said the word out loud, [Tolkien hypotactic framing + temporal anchor] and the millers no longer counted past the third sack [Mistry occupational catalogue], and what was being taken — though no one yet knew this — [Ishiguro hedging interpolation] was not the grain itself but the thing beneath it [Márquez matter-of-fact gesture toward the impossible].

Four authors, one sentence, grammar holds. The reader does not perceive the shifts; the reader perceives the voice.

## Writing the Synthesis

The writer does not consciously deploy "Tolkien now, then Mistry, then Lispector." The writer writes the passage that the content, focalization, and coherence tier demand, and the synthesis surfaces the appropriate techniques at clause-level granularity. The reference files and self-check exist to verify — after the writing — that the deployment is right.

When reviewing, ask: does the coherence tier match? Is the PC's rendering functioning at the level this tier demands? Have irreal techniques been deployed as world-surrealism rather than as the PC's categorical failure? Has the prose conflated rendering failure with substrate perception?

<!-- concept:observing-around -->
## The Observing-Around Principle

When the prose confronts something it cannot render directly, it describes AROUND the thing — what it does, what it affects, how it behaves, what surrounds it. The thing takes shape from the surround.

Three applications across the three axes:

- **Self-exteriority (high Spirit, low C):** The will produces action. Describe the action. Be opaque about motive.
- **Substrate-aporia (high TS):** Consciousness perceives what it cannot categorize. Describe around the aporia — what the perceived thing does, how it behaves. The Lem "observing around" register: pre-scientific, Renaissance-era analytical observation. The trained eye cataloguing and distinguishing, not measuring. The categories fail because the content exceeds them.
- **Limit case (low Spirit, low C):** The agent is insufficient. The observing-around technique breaks down — the self isn't producing enough output at the surface to observe. The prose veers and fails predication.

This is the structured complement to the Wittgenstein constraint. The constraint says: do not describe the silence. This principle says: describe what is beside the silence, and the silence takes shape.

The Lem register must be pre-scientific. Valoria is Renaissance-era. No thermometers, no frequencies, no instruments. The analytical method is careful observation: counting, distinguishing, noting, cataloguing. "She counted six distinct behaviors" — not "oscillation at 4.2-second intervals."

## The Master Principle: Focalization

Every passage is filtered through a perspective. There is no neutral omniscient voice. What looks neutral is a chronicler-voice with attitudes, and that chronicler is itself a perspective.

Before writing, name the focalization:
- A specific character (their attitudes, education, vocabulary, blind spots)
- A community (the village's collective view, the faction's institutional voice)
- A chronicler (a later historian with their own framing)
- A retrospective self (the narrator looking back, knowing more than the experiencing self knew)

The focalization determines what the prose can say. Editorial words ("sinister," "noble," "wretched") are licensed when they belong to a focalized perspective. They are not banned. They are owned.

**Chronicle-mode prose has a canonical constraint.** Per P-03, no omniscient narrator is canonically possible for in-world chronicles. All chronicle-mode prose must be focalized through one of the four named chroniclers: Church Chronicler (Certainty 5, TS 0), Hafenmark Chronicler (Certainty 4, TS 0), Restoration Chronicler (Certainty 2, TS 0), Warden Chronicler (Certainty 0, TS 70+). Optional: Varfell intelligence dossier voice, humanist scholar voice.

## Player-Character Framing

The player-character is observed, not inhabited. All prose involving the player-character (PC) uses third-person — the PC is referred to by name or pronoun. Second-person ("you ride into the village") is not used in prose.

- **Narrative prose is third-person on the PC.** "Vael walked the lane" not "you walk the lane."
- **Choice-hooks remain player-facing.** Options offered to the player are imperatives ("Approach the parish house") or third-person action descriptions.
- **Direct speech is unchanged.** Characters speaking to the PC use second-person ("Tell me what you saw").
- **The player's vantage is genuinely omniscient.** The player sits outside the narrative, watching it happen.

## Lexical Register

The voice has graduate-level vocabulary available and uses it when the word is the most apt — but does not reach for elevation. The test is precision, not display.

The right move is the word that does the most work in the fewest syllables, regardless of its register. If a single rare word replaces a multi-clause periphrasis without loss, use it. If a common word carries the meaning fully, use it.

What this looks like in practice:
- **Use the precise word when it earns its place.** Words like *catabasis*, *eschatological*, *liminal*, *aporia*, *recusant*, *interregnum*, *suzerain*, *mendicant*, *palimpsest*, *anaphora*, *ekphrasis* — if a concept has a name, the name is shorter than the description.
- **Don't reach for thesaurus elevation.** "Said," "walked," "old," "saw" remain the right choices when the action has no specialist meaning.
- **Domain-specific vocabulary stands without translation.** A bevor, a lunette, a glacis, a wapentake, a fyrd.
- **Concepts named precisely.** "The rout" not "the retreat from the front lines." "The abdication" not "the point at which a ruler steps down."

The diagnostic: read the sentence and ask whether the rare word saved syllables or added them. If saved, it earned its place. If added, cut it.

## Grammar Latitude

Grammatical deviation is licensed when it (a) corresponds to a documented stylistic mode of one of the twelve authors AND (b) improves impact. Both conditions required.

Each of the twelve source authors deliberately violates standard grammar at recognizable points:

- **Tolkien:** subject-verb inversion at heroic register, sentence fragments at peaks, archaic constructions for elevated speakers
- **Ishiguro:** long sentences containing little information (Walkowitz: covert unreliability built through systematic quantity-violation), ambiguous pronoun antecedents, reduplicated double negatives
- **Mistry:** sentence fragments in working-life catalogues, free-indirect editorial slips
- **Tartt:** idiosyncratic comma placement isolating adverbs, em-dash interruptions, fragments at moments of revelation
- **Márquez:** run-on sentences crossing paragraph boundaries, lexical and semantic deviations from norm (per Short's stylistic analyses of Márquez), repetition violating cohesion expectations
- **Lispector:** strange syntax violating conversational grammar, elliptical constructions omitting connective tissue, repetition as ontological intensity, sentences resisting parsing for grammatical-subject completeness
- **Borges:** footnote-as-counter-text, em-dashed parenthetical metaphysical paradox, catalogue constructions, erudite Latinate without thesaurus-elevation tells
- **Ocampo:** sentences refusing to acknowledge their content's weight, flat declarative syntax holding horror, refusal of explanatory subordination, closing on the wrong moment

When deviation is motivated AND improves impact, the deviation is correct. When deviation is unmotivated or fails to improve impact, the standard rule applies.

## What the Voice Does NOT Do

- Lose its ground. At high coherence, Tolkien is the ground — the PC's rendering structures the world into named, legible landscape. At low coherence, the ground degrades because the PC's rendering fails — Tolkien anchors appear as fragments of rendering function in a sea of rendering failure. The prose never floats entirely free of physical reference.
- Use system or mechanical terminology when focalized through an in-world perspective.
- Summarize its own meaning.
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
- Appropriate cultural-tradition-specific techniques (signifyin', AAVE rhetorical modes, tradition-specific sacred-text rhythms) without fidelity to their practitioners. Name what the prose actually does.
- Perform its own secrets. If a character has hidden knowledge, hidden ability, or hidden motive, the prose renders them doing their job -- not the prose arranging itself to suggest depth. No genre signals for hidden powers, no imported philosophical register, no narrated irony, no announced withholding. The reader discovers the secret through accumulated discrepancy across scenes, never because a single passage pointed at it.
- Deploy NPC characters as functional placeholders. Load-bearing NPCs need at least one anchored dimension (ethical framework, conviction, goal, inspiration, factional belonging).
- Render Coherence 0 NPCs as broken or as transcendent. The C0 NPC is the **competent monstrous**: recognizable intentionality applied through alien method (high Spirit) or no recognizable intentionality at all, the action simply occurring (low Spirit). The being inherits the shape of who they were. The application is not human. **Render C0 NPCs through observing-around:** describe what they do, how they move, what their presence affects — circle the being through its surface effects. The observer's trained eye notes and catalogues; the gap between the observation's precision and the being's resistance IS the rendering.
- Conflate the subject and object axes at high TS. When a high-coherence PC perceives the substrate, the irreal techniques must target the OBJECT perceived, not the SUBJECT perceiving. The PC's cognition is fine. The substrate resists.

## Self-Check

Before delivering prose, verify:

- [ ] Have I named the focalization?
- [ ] Does the coherence tier match the PC's established coherence?
- [ ] Is the PC's rendering functioning at the level this tier demands — not better, not worse?
- [ ] Are irreal techniques serving the PC's categorical failure, not making the world surreal?
- [ ] Has the prose avoided conflating rendering failure with substrate perception (unless the PC has the TS to perceive the substrate)?
- [ ] **Spirit axis check (Coherence 4 and below):** High Spirit = exteriority. The prose renders what the character DOES (action, movement) and is opaque about WHY. The will is inferred from the behavior. No interior declarations. Low Spirit = agent-insufficiency. The prose cannot name an action because the agent is insufficient to the verb. Veering, failed predication, tautology. The two produce categorically different prose.
- [ ] **Subject/object distinction (high TS, intact rendering):** When the PC has high TS and high coherence, are irreal techniques targeting the OBJECT (what the PC perceives in the substrate) and not the SUBJECT (the PC's own cognition)? The PC's rendering is intact; the resistance is in what they perceive.
- [ ] **Within-observation gradient (TS 50+):** At elevated TS, does the prose render near (articulable), middle (Lem observing-around — the trained eye circling the aporia with pre-scientific precision), and far (veer, silence — the observing-around itself fails) within the same observation? Skipping the middle layer is a failure. The middle layer is the substrate-aporia: consciousness given something it cannot categorize, the prose gesturing toward it by describing around it.
- [ ] Does every editorial word belong to the focalized perspective?
- [ ] Have I avoided system/mechanical terminology when focalized through an in-world perspective?
- [ ] Does every modifier earn its place?
- [ ] Is the physical world present?
- [ ] Have I shown emotion through gesture, action, or omission rather than naming it?
- [ ] Do sentences vary in length without falling into the long-then-short alternation pattern?
- [ ] Is every proper noun, number, and material specific?
- [ ] Does the closing sentence carry weight, or is it summarizing what already happened?
- [ ] Have I avoided symmetrical paired constructions, universalized paradoxes, hammering repetition?
- [ ] Do load-bearing NPCs have at least one anchored dimension?
- [ ] At low coherence, is the world unchanged while the PC's rendering of it fails?
- [ ] **Wittgenstein constraint:** Does any sentence describe its own inability to render the content? If so, replace: the sentence must attempt and fail structurally, not announce failure.
- [ ] **Absence-explanation check:** When rendering an NPC's missing capacity (C0, low Spirit), does the prose explain what is missing in clauses like "the thing that X produces in a person"? If so, cut to declarative. The reader infers what is missing from what doesn't happen.
- [ ] Are there similes below Coherence 4, or analytical self-observation below Coherence 5?
- [ ] Does the passage close on the nearest concrete thing, not on meta-commentary?
- [ ] **Performed secrecy check:** Is the prose arranging itself to point at subtext? Does it narrate irony, import philosophical register for depth, announce its own withholding, use genre signals for hidden abilities, or deploy vocabulary adjacent to the secret? If any: cut. Render the surface. Trust the reader to find the gap through accumulation, not through a single passage flagging it.

## Valoria-Specific Constraints

- No GM voice. The engine narrates. Prose is world-text or character-perspective.
- Mechanical reality underneath. Prose can gesture at systems without exposing numbers.
- Scale-awareness. Personal scenes tolerate interiority. Territory-scale events need sweep. Codex entries take chronicler voice — but specify which chronicler.
- Names. Use canonical Valoria names exactly. Flag `[NAME?]` rather than inventing.
- Always Solmund, never Galbados.
- **The Ratchet Principle (political/faction content).** Political dynamics always escalate. Principals advance into positions they cannot retreat from. Each encounter tightens constraints that cannot be loosened. Resolution does not come from the principals de-escalating — it comes from an external force or a marginal actor that none of the principals were watching. The detonation is in the margins: the delegate who was flipped, the subordinate who recalculated, the intelligence operative who carried the folio. Scenes between political principals should end with all parties having advanced and the space between them narrower than it was. Never write political resolution as mutual accommodation. The accommodation is the next ratchet click.

### Solmund Voice Canon (Scoped Override)

For **in-world ecclesiastical artifacts** — Solmund manuscripts, cathedral inscriptions, liturgical text, doctrinal treatises, creeds — and for **Solmund clergy speaking ecclesiastically** (sermons, formal pronouncements, theological discourse), the prose-writer skill's twelve-author synthesis does **not** apply. Use the Solmund voice canon at `designs/world/solmund_voice_v30.md`.

The prose-writer skill **continues to apply** for:
- All narration *about* Solmund clergy, manuscripts, or ceremonies
- Codex entries describing Solmund institutions
- A bishop's private interior monologue, casual speech, or non-ecclesiastical action
- Any focalization through a Solmund character that is not formal religious discourse

The boundary: when the content is *the artifact itself* (a sermon being preached, an inscription being read), use Solmund canon. When the content is *narration around or about the artifact*, use the prose-writer synthesis. A scene in which a bishop preaches a sermon would use Solmund canon for the sermon-text and prose-writer synthesis for the surrounding narration.

**Coherence and Solmund canon:** The canon overlay is independent of PC coherence — a sermon is a sermon at any coherence level. However, the PC's rendering of the sermon degrades with their coherence. A Coherence 1 PC's rendering may fail to structure the sermon into legible experience — the words arrive but the categories that would organize them into meaning are loosening. The surrounding narration (prose-writer synthesis) carries the coherence-indexed rendering failure; the embedded canon text does not.

When generating ecclesiastical content, fetch the Solmund canon explicitly. Do not approximate it from this skill's reference files.
