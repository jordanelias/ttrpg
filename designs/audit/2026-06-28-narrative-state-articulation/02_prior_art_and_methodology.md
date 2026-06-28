<!-- STATUS: ANALYSIS — external prior-art survey. Sources cited inline; see provenance note. -->
# 02 — Prior Art & Methodology

How acclaimed narrative and emergent games — and the academic literature — actually produce legible story. **The convergent law:** none generate text at runtime. Authored and emergent alike author a finite, *voice-bearing* fragment/template corpus, tag each unit with **conditions over game state**, and at runtime only **select → substitute → splice**.

*Provenance: WebFetch was 403-blocked in this environment; the two Steven Sych papers were read in full from user-provided PDFs, all other items are WebSearch-excerpt-confidence. Load-bearing quotes flagged ⚑ for verbatim re-check.*

## A. Authored CRPGs — density without generation

**Disco Elysium.** ~1M-word script authored in articy:draft. The 24 skills are authored *as speakers* in the dialogue graph (voice-as-focalization). Two-tier checks: **passive** (no dice; line fires iff `skill + mods ≥ difficulty`) and **active** (white = retryable/no permanent fork; red = one-shot). ~211 **anti-passives** fire on *failure* — failure is authored content, not absence. "Micro-reactivity" (writer Justin Keenan, GDC 2021 ⚑): tag a memorable moment with a boolean; later lines read the flag (shaved beard → Kim's aftershave callback). Thought Cabinet = a second state layer that rewrites which text is legal.
- discoelysium.wiki.gg/wiki/Skills · /wiki/Thought_Cabinet · gamedeveloper.com (".../micro-reactive...") · articy.com/en/showcase/disco-elysium/

**Planescape: Torment.** Infinity Engine `.dlg` files *are* finite-state machines: the engine picks the first state whose condition is true; each reply is gated by a trigger (`CheckStatGT(LastTalkedToBy,12,CHR)`). Memory/callbacks via global variables. Stat-check thresholds harmonized (~90% clear at value 16) so investment pays evenly.
- gibberlings3.github.io/iesdp/file_formats/misc_formats/d.htm · forums.beamdog.com (Dialogs Stats Checks Analysis)

**Esoteric Ebb** (2026, verified). DE-like; collapses the skill-voices onto the **six D&D ability scores**, each a personified ideological inner voice; passive checks gate voice lines; active checks dramatized as turn-based dice; a feat/Thought-Cabinet hybrid at quest end. "Exhaustive pre-authoring + condition-gating, done by one author."
- en.wikipedia.org/wiki/Esoteric_Ebb · games.gg/esoteric-ebb (skills guide) · pcgamer.com review

**Transfer:** condition-gated fragment libraries; **voice-as-focalization solves the assembly/glue problem** (the voice tag *is* the transition; contradictory/uncertain fragments coexist as opinion); first-class failure fragments; once-only vs. repeatable guards.

## B. Emergent systems — simulation → legible story

**Dwarf Fortress.** Typed `history_event` records: `id, year, seconds72, type` + FK references (`hfid`, `site_id`, `artifact_id`) + type-specific fields — *a Key by another name*. Legends prose = a **per-event-type template function** switching on subtype (40+ `hf_died` causes) filling fixed clauses with names resolved by ID, wrapped "In [year+season], …". Named-entity anchors + color hyperlinks make Legends a browsable **narrative graph**; base game has **no notability ranking** (the thing Valoria's significance fn adds). Tarn Adams' method ⚑: "write the stories you want the game to produce, then build the engine — like drawing example maps when designing a map generator"; "the player is the official will, the dwarves are actors in their own stories."
- dwarffortresswiki.org/Legends · github.com/DFHack/df-structures (df.history.xml) · github.com/robertjanetzko/LegendsBrowser2 · *Procedural Storytelling in Game Design* ch. "Emergent Narrative in Dwarf Fortress"

**Caves of Qud** (Grinblat & Bucklew, FDG'17 ⚑). **State machine + Tracery-like replacement grammar over a ~40k-word authored corpus** "codifies their diction and repackages it procedurally… in the game's voice." **Generate-events-first, rationalize-ex-post.** **Dual register:** clean replacement-grammar for canonical gospels vs. **order-2 Markov** for deliberately "corrupted" books/graffiti — corruption framed as in-world drift. Sultan structure: origin → 8 core events (pool of 17) → ascension → death, with cross-event state chaining (relic gained in Marriage lost in later Battle). Secrets distributed via shrines/painted objects + the water-ritual exchange. "No AI; hand-written rules."
- dl.acm.org/doi/10.1145/3102071.3110574 · freeholdgames.com/papers/Generation_of_mythic_biographies_in_Cavesofqud.pdf · wiki.cavesofqud.com/wiki/Markov_chain · /wiki/Sultan_histories

**Crusader Kings 2/3.** Thousands of scripted events; text = **localization keys with scope/data-function substitution** (`[ROOT.Char.GetFirstName]`, `[scope:target.GetTitledName]`), gated by trigger/weight/MTTH; story emerges from traits + relationships + event scripting. The canonical "parameterized event text at scale."

**RimWorld AI Storyteller** (Cassandra/Phoebe/Randy). A **pacing director**: incidents scheduled by mean-time-between adjusted by colony **wealth** (threat-point budget) and tension curves, with post-loss adaptation. Tynan Sylvester ⚑: "we supply these labels — a person's *sister* — … people's brains just take over… no more complicated than a children's book." Direct model for closing PP-688's deferred D11 pacing.
- rimworldwiki.com/wiki/AI_Storytellers · rockpapershotgun.com (How RimWorld Generates Great Stories)

**Wildermyth / Shadow of Mordor Nemesis.** Per-entity persistent memory record → templated, parameter-substituted barks/titles/showdowns; on re-encounter, select dialogue by the entity's stored encounter history (patent US10,926,179: "faction event record" → "dialog identifier"). Entity-scale micro-reactivity; dialogue authored to be **quotable/shareable** (de Plater ⚑). Scars are encounter-history flags → mesh overlays.
- patents.google.com/patent/US10926179B2 · gamedeveloper.com (Designing/Upgrading the Nemesis system) · GDC 2018 "Helping Players Hate (or Love) Their Nemesis" (Chris Hoge)

## C. Theory + the academic deterministic-NLG state of the art

- **Jenkins**, "Game Design as Narrative Architecture" — four modes: evocative / enacted / embedded / emergent (designer builds spaces that *afford* story).
- **Marie-Laure Ryan** (story = cognitive construct) + **Juul** (games are present-tense → recount-prose only for past-tense chronicle).
- **Aylett** (coined "emergent narrative," 1999) — the **"narrative paradox"** (player freedom vs. narrative coherence) is Valoria's exact problem. cdn.aaai.org/Symposia/Fall/1999/FS-99-01/FS99-01-014.pdf
- **James Ryan, curationism** (*Curating Simulated Storyworlds*, 2018): simulate richly, then **curate/sift**; "emergent narrative is nonfiction — it actually happened"; pipeline **chronicler → chronicle → sifter → narrativizer** = PP-688's spine. escholarship.org/uc/item/1340j5h2
- **Story sifting** (Kreminski et al., **Felt** 2019 / **Winnow** 2021): sifting patterns = **Datalog queries over the event log** (`?variable` binding + attribute/temporal/negative constraints + recursive causal rules). **"Select the Unexpected"** (2022): rank matches by statistical improbability. github.com/mkremins/felt · ojs.aaai.org/index.php/AIIDE/article/view/18903
- **Steven Sych** (read in full): **retelling/tellability** as the success criterion; **critical retellings** (irony/breakdown surfaced as immanent critique); **breakdown** (Heidegger ready-to-hand → present-at-hand) as the criticality dial; **storytelling partnership** + generative friction; MENU NEW GAME+ as the evocative-space limit case. spectrum.library.concordia.ca/id/eprint/991374/
- **Mateas & Stern, Façade** — a **drama manager** sequencing beats to an Aristotelian arc (a pacing-director precedent). users.soe.ucsc.edu/~michaelm/publications/mateas-gdc2003.pdf
- **Compton**, "10,000 Bowls of Oatmeal" — mathematical ≠ perceptual uniqueness; fixes = vary on perceivable/consequential axes, cluster into named kinds, Expressive Range Analysis. galaxykate0.tumblr.com/post/139774965871
- **Reiter & Dale** classical NLG (aggregation, referring-expression generation, discourse relations) — cheap "feels-written" levers.
- **Horswill** (CatSAT constraint-safe PCG; **STEP** text-gen language unifying CFG/templates/logic/HTN; TED/Simulog story-sifting at scale; *City of Gangsters* shipped logic-programming social model) — proof the no-LLM realizer is mature, buildable tech, not a compromise. ojs.aaai.org/index.php/AIIDE/article/view/13026

## D. Transfer table → Valoria

| Prior-art mechanism | Valoria hook |
|---|---|
| Condition-gated fragment library | fragment conditions over Keys + flags + armature state |
| Voice-as-focalization (DE/EE) | 4 chroniclers + protagonist frame (P-03); Conviction armature |
| Micro-reactivity boolean tags (DE) | `awareness` / `causes[]` flags on memorable Keys |
| Per-event-type template fn (DF) | slot-template per Key-type × significance-length |
| Replacement grammar over voice corpus (Qud) | offline-baked X/Y/Z lexicon overlay |
| Dual register clean/Markov (Qud) | Coherence-indexed clean vs. degraded rendering (self-rendering amendment) |
| Localization-key + scope substitution (CK) | template slots filled from Key payload/`targets[]` |
| Wealth-scaled pacing director (RimWorld) | significance/tension scheduler → PP-688 D11 |
| Per-entity memory → showdown text (Nemesis) | NPC memory/armature → Tier-2 fragment selection |
| Story sifting (Felt/Winnow) | significance fn + arc detection as Datalog over Key log |
| Tellability / retellings (Sych/Eladhari) | sifting heuristic + evaluation instrument |
| Labels → player's brain (RimWorld) | surface Bonds/Knots/Convictions/Disposition labels |
