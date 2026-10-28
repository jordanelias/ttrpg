# Procedural generation and the structure of choice-based narrative — emergent-narrative literature, read entries

## Status: FILED — reference, not canon (CLAUDE.md §0.05) · tier 3 (`research/00_INDEX.md` §1) · resolves nothing at runtime
## Date: 2026-10-28 · Lane: IN (cross-cutting) · Written against `15593ac`
## What changes in `engine/season/`: nothing. If this directory were deleted the game would behave identically.

How to read an entry, what the reading tags mean, and the source ledger: `00_README.md`. Tests are numbered `<ID>.Qn`; the cross-source instrument that groups them is `07_apparatus.md`.

## Procedural generation, and how choice-based narrative is structured

### P01_compton2016 — Kate Compton (2016). *So you want to build a generator…*
- **Read:** `P (full)` · blog post (Tumblr, self-described beginner advice essay of about 4000 words) · personal blog, no venue · skipped: the notes list of likes/reblogs and the link list in the Conclusions · domain: PCG
- **Thesis:** What generator you should build depends on first writing down, concretely, what a good and a bad artifact of your kind is; the method follows from those properties and constraints. The commonest failure is not breakage but output that is mathematically distinct yet perceptually samey, so the real target is perceptual, not combinatorial, variety.
- **Core arguments:**
  1. Start by listing the properties of a good artifact and the properties of a bad one, with deal-breakers starred as constraints; generators are easiest where good is a set of concrete properties and most reliable where constraints are concrete (§What are you making?).
  2. The designer must also choose how wide a range of artifacts is wanted, since a generator that makes one perfect artifact repeatedly is not the goal (§What are you making?).
  3. Generative methods (distribution, parametric, tile-based, grammars, constraint solvers, agents/simulations) are each described by which of five skills they give the machine: encapsulating options, creating structure, conditional rules, variable structure, and self-checking against constraints (§From rules to generative methods and following sections).
  4. Each method has a named weakness: distribution lacks structure, parametric yields new but never surprising, tile-based loses large-scale control, grammars cannot express cross-branch constraints, solvers are bulky and hard to integrate (method sections).
  5. Generate and test fails when passing content is rare or when constraints accumulate, and some constraints (I know it when I see it) cannot be written down at all; the remedy is to make the generator less able to produce the bad thing, at a cost to possibility space (§Ways that generators fail).
  6. Interest fails through the 10,000 Bowls of Oatmeal problem: unique-in-fact output is seen as one thing; she separates perceptual differentiation (this is not identical to the last) from perceptual uniqueness (this is memorable) (§Aesthetics: the toughest challenge).
- **Argument structure:** The essay is an organising taxonomy built from the author's practitioner experience: it poses questions, matches each answer to a method family, then lists failure classes. Evidence is anecdote and example (Spore, No Man's Sky, Tracery, Dwarf Fortress); there is no measurement and she says herself it is probably full of errors and omissions. The oatmeal argument is one paragraph with a thought experiment, not a study. Weakest link: the claim that perceptual uniqueness is the real metric is asserted, and she offers no way to measure it, only observations about what humans like to perceive (traces of process, memorable cities).
- **Key terms:**
  - `artifact` — whatever the generator makes (a level, a story, a recipe).
  - `possibility space` — all the artifacts a generator can produce.
  - `generate and test` — regenerate until a computable constraint passes.
  - `10,000 Bowls of Oatmeal problem` — unique outputs that look alike to the user.
  - `perceptual differentiation` vs `perceptual uniqueness` — not-identical-to-the-last vs memorable.
  - `Artist-in-a-box` — encoding how a human maker would make the thing.
- **Verbatim anchors:**
  - "The most reliable generators are the ones where you can concretely describe constraints." (§"What are you making?")
  - "But the user will likely just see a lot of oatmeal." (§"Aesthetics: the toughest challenge")
  - "Perceptual uniqueness is the real metric, and it’s darn tough." (§"Aesthetics: the toughest challenge")
- **Apparatus — tests for a design:**
  - **P01_compton2016.Q1** *Does the design state, per generated artifact kind, a list of what makes one good and a list of deal-breaking properties, in checkable terms?* Passes if each artifact kind has named properties and starred constraints a reviewer can test on a sample. Fails if good or interesting is left undefined. Detects: unspecified success criteria.
  - **P01_compton2016.Q2** *Show 20 consecutive outputs to someone who has not seen the generator; can they tell them apart and name how?* Passes if differences are perceived on named axes. Fails if differences exist only in underlying values (seeds, small numeric offsets). Detects: the oatmeal problem (unique in fact, same in perception).
  - **P01_compton2016.Q3** *For each constraint, is it enforced by construction, by generate-and-test, or not at all, and what is the rejection rate?* Passes if each has a mechanism and the rejection rate is known to be tolerable. Fails if constraints are listed but nothing enforces them or most output is discarded. Detects: unenforced or unreachable constraints.
  - **P01_compton2016.Q4** *Which skill (structure, conditional rules, variable structure) does the chosen method lack, and does the design need it?* Passes if the gap is named and covered. Fails if the design needs cross-part relationships (foreshadowing, consistency) from a method she says cannot encode them. Detects: method-requirement mismatch.
- **Does not license:** That oatmeal-style sameness is measured or common; it is a diagnosis from the author's experience, not a finding. It gives no metric for perceptual uniqueness. It is beginner-level advice with explicitly incomplete coverage, not a survey, and dated (2016) on solvers (new, bulky). It does not discuss narrative content except in passing.
- **Links:** names Gillian Smith's work on range (cf. P04_smith2014) and Michael Cook; does not mention Expressive Range Analysis (cf. P02_smith2010) by name. Related to the PCG textbook she links (cf. P03_togelius2011) [reader's inference].
- **Prior-claim check:**
  - Title 10,000 Bowls of Oatmeal: CORRECTED: the post is titled So you want to build a generator…; the oatmeal argument is present as a named paragraph in §Aesthetics: the toughest challenge, not as a separate post.
  - Mathematical uniqueness is not perceptual uniqueness: CONFIRMED (§Aesthetics).
  - Fixes: vary on perceivable/consequential axes, cluster outputs into named kinds, validate with Expressive Range Analysis: NOT-IN-SOURCE (no such prescription; she discusses only perceptual differentiation/uniqueness and characterful artifacts among background ones; ERA is not mentioned).

### P02_smith2010 — Gillian Smith & Jim Whitehead (2010). *Analyzing the Expressive Range of a Level Generator*
- **Read:** `P (full)` · workshop paper (about 6 pages; PCG Workshop at FDG 2010, ACM footer PCGames 2010) · UC Santa Cruz Expressive Intelligence Studio · skipped: reference list, permission notice · domain: PCG
- **Thesis:** A level generator should be judged by the range and style of what it can produce, not by speed or quantity. Measuring generated samples on a few emergent global metrics and plotting them as 2D histograms exposes the generator's peaks, holes and unintended biases, and shows how parameters move them.
- **Core arguments:**
  1. Speed and volume statistics are insufficient: a generator producing tens of thousands of effectively identical levels is useless, so judge the style and variety of output (§1).
  2. The method is four steps: pick metrics, generate a large sample, visualise the metric scores as 2D histograms, and compare the histograms under changed parameters (§2).
  3. Metrics should be global and emergent from the generator's point of view, not the same quantities used as its inputs, so parameter effects stay visible (§2, §4.2).
  4. Applied to their grammar-based platformer generator Launchpad, using linearity (regression fit of platform midpoints) and leniency (hand-assigned per-component scores), the histogram of 10,000 levels showed an unintended bias toward linear levels traced to a late repeat a chosen component tweak (§4.2, §4.3).
  5. Varying rhythm type, density, length and geometry weights each shifted the histograms, and filtering by critics left about 100 of 10,000 levels yet kept spread on one critic and not the other (§4.4, §4.5).
  6. Expressivity can be unintentional and does not imply creativity; the system cannot evaluate its output beyond its pre-defined fitness functions (§5).
- **Argument structure:** Premise: counts and curated examples cannot show range. Move: define a procedure and demonstrate it on one in-house generator; the demonstration's payoff is the discovered linearity bias. Evidence is a single case study with two metrics, with hypotheses for causes (the authors say we hypothesize) not tested by intervention. Weakest links: the metrics are the authors' choice, leniency is built on intuitive hand-set weights, and the paper itself says the two metrics are not sufficient and that no player model is used.
- **Key terms:**
  - `expressive range` — the style and variety of content a generator can produce.
  - `metric` — a numeric score on a global property of a generated artifact (here linearity, leniency).
  - `2D histogram` — counts of generated artifacts per bin of two metric scores; shows peaks and holes.
  - `critic` — a test over a whole level for a global constraint, used to filter generated candidates.
  - `over-generation` — grammars produce outputs violating global design constraints.
- **Verbatim anchors:**
  - "we call this quality of a generator its expressive range." (§1)
  - "The linearity bias is an unintended side effect of this design decision." (§4.3)
  - "it is possible for a system to be expressive without necessarily being creative." (§5)
- **Apparatus — tests for a design:**
  - **P02_smith2010.Q1** *Has the generator been run at volume (the paper uses 10,000 samples) and its output scored on at least two metrics that are not its own input parameters, then plotted jointly?* Passes if a joint distribution exists and has been inspected for peaks and holes. Fails if the evidence is hand-picked examples, counts, or speed. Detects: unmeasured output range.
  - **P02_smith2010.Q2** *Does any region of the metric plane the design intends to reach have zero or near-zero density?* Passes if every intended region is populated or its emptiness is accepted explicitly. Fails if a promised kind of output never occurs. Detects: holes in expressive range.
  - **P02_smith2010.Q3** *For each late-added rule or tweak, was the histogram regenerated before and after?* Passes if side effects on distribution were checked. Fails if distributions were measured once or never. Detects: unintended bias from minor changes (the paper's own finding).
  - **P02_smith2010.Q4** *Are the metrics validated against player-perceived differences, or only against designer-chosen proxies?* Passes if some link to perception or play is shown. Fails if range is claimed from proxy scores alone. Detects: proxy-metric overreach.
- **Does not license:** That ERA measures quality, fun, or perceived variety; the paper explicitly says expressivity is not creativity and that its metrics are insufficient. It has one generator (offline, search-based, platformer levels) and says online generators that respond to player action make what to compare unclear. It covers no narrative content. The histogram shows density of outputs, not whether any output is good.
- **Links:** cites Togelius et al. 2007 on personalised fitness (cf. P03_togelius2011 [reader's inference]); the problem it names is the one P01_compton2016 credits to Smith; its range framing is used in P04_smith2014 [reader's inference].
- **Prior-claim check:**
  - Claim that ERA measures how much of a possibility space a generator covers via metrics and histograms: CORRECTED: it measures the distribution of generated samples over chosen metric axes (style and variety), a sampled picture of density, not coverage of the full possibility space; the term Expressive Range Analysis itself does not appear, only "expressive range" and "analysis" (§1, §2). Metrics used: linearity and leniency (§4.2). Cannot show: quality, difficulty, player experience, online or adaptive behaviour (§5).

### P03_togelius2011 — Julian Togelius, Georgios N. Yannakakis, Kenneth O. Stanley & Cameron Browne (2011). *Search-based Procedural Content Generation: A Taxonomy and Survey*
- **Read:** `P (full)` · survey article with taxonomy (about 14 pages; the extracted text names no journal and no year, but its own reference list shows the IEEE Transactions on Computational Intelligence and AI in Games as the series, and it is consistent with the IEEE TCIAIG article [reader's inference]) · authors confirmed as given · skipped: reference list (text lines 224 to the end, beyond line 226 of the extraction), figure fragments · domain: PCG
- **Thesis:** Procedural content generation can be dissected along a small number of mostly continuous distinctions, and search-based PCG is the special case of generate-and-test in which a graded evaluation function steers the next candidates. The two hard design decisions in that case are how content is represented and how its quality is evaluated; the survey of 14 projects shows both are under-explored.
- **Core arguments:**
  1. Five distinctions place any PCG method: online vs offline, necessary vs optional content, random seed vs parameter vector (degrees of control), stochastic vs deterministic, constructive vs generate-and-test; most are continua (§II).
  2. Necessary content must always be correct, whereas optional content may fail, and which class a content type falls in depends on the specific game and its fiction, so it must be decided game by game (§II-B).
  3. Search-based PCG differs from plain generate-and-test in two ways: the test grades candidates with a real number or vector, and new candidates depend on earlier grades (§III).
  4. Representation shapes the search space: direct encodings reach every point but suffer dimensionality; indirect ones are compact but may leave regions unreachable; a representation needs locality (small genotype change, small phenotype and fitness change) (§III-A, maze example of five encodings).
  5. Evaluation functions come in three classes: direct (features mapped to fitness, theory-driven or data-driven), simulation-based (an agent plays, static or dynamic) and interactive (player behaviour or affect, explicit or implicit); designing one is ill-posed because fun and other states are hard to formalise (§III-B).
  6. Open problems include avoiding catastrophic failure, speed, representation principles, player models in evaluation, and assessing generators, where expressive range is named alongside competitions; narrative is deliberately not surveyed, with a call to hybridise bottom-up search with top-down planning (§V, §IV-A5).
- **Argument structure:** Premise: the field lacks a shared vocabulary. Move: propose distinctions, define the search-based subset, then classify every known published search-based paper under those distinctions and tally the result (of 14 projects, 6 direct, 6 simulation-based, 2 interactive evaluation; 12 single or fixed linear fitness). Evidence is a literature survey of the authors' own judgement of coverage (all published papers known to the authors), with no outcome comparison between methods. Weakest link: the taxonomy's usefulness is shown by classifying papers rather than by predicting which choice works; the authors say other distinctions will be needed and that these are chosen to clarify search-based PCG.
- **Key terms:**
  - `necessary vs optional content` — content the player must pass through vs content the player can avoid.
  - `generate-and-test` — candidate generated, then tested, then regenerated until good enough.
  - `evaluation function` — maps content to a fitness scalar or vector.
  - `direct / simulation-based / interactive` — the three evaluation classes above.
  - `direct vs indirect encoding` — genotype size and mapping to the content.
  - `locality` — small genotype changes cause small phenotype and fitness changes.
- **Verbatim anchors:**
  - "necessary content always needs to be correct" (§II-B)
  - "Designing the evaluation function is ill-posed" (§III-B)
  - "The importance of reliability depends partly on whether the content generated is optional or necessary" (§V)
- **Apparatus — tests for a design:**
  - **P03_togelius2011.Q1** *For each generated content type, does the design state whether it is necessary or optional to progress, and is the failure tolerance consistent with that?* Passes if each type is classified and required types have a guarantee (by construction, by test, or by fallback). Fails if a progression-critical output can be generated unusable or out of step with the rest. Detects: catastrophic failure on necessary content.
  - **P03_togelius2011.Q2** *Where content is chosen by scoring, what does the evaluation function actually compute (features, a simulated play-through, or player behaviour), and is that what the design claims to want?* Passes if the scored quantity is named and its link to the intended experience is argued or tested. Fails if the function scores a proxy (e.g. counts) while the design claims it optimises an experience such as interest. Detects: evaluation-function mismatch.
  - **P03_togelius2011.Q3** *Can every kind of output the design promises be produced by the chosen representation, and does a small change to the generating input produce a small change in output?* Passes if reachability and locality are shown for a sample. Fails if parts of the intended space have no encoding, or if tuning one parameter changes outputs unpredictably. Detects: unreachable regions and low locality.
  - **P03_togelius2011.Q4** *Is the amount of randomness (stochastic vs deterministic, seed vs parameter control) chosen on purpose, and can a given output be reproduced?* Passes if reproducibility and the player- or designer-facing control are stated. Fails if outcomes cannot be reproduced or tuned and no decision was recorded. Detects: uncontrolled variation.
- **Does not license:** That search-based PCG is the right method for any particular design: it surveys it as a research field in 2010-era prototypes (mostly evolutionary algorithms) and says many take days to run. It does not survey narrative or story generation at all, so it provides no evidence about story content beyond naming planning as the usual approach. The 14-project tallies are counts of research papers, not of shipped games. Its evaluation-function claim is that formalising fun is unsolved, not that any function validates experience.
- **Links:** cites expressive range work (reference [78], cf. P02_smith2010) as one way to assess generators (§V); its generate-and-test definition matches P01_compton2016's use of the term; points to Wardrip-Fruin for story-generation history (cf. P04_smith2014 [reader's inference]).
- **Prior-claim check:**
  - Authors and venue: CONFIRMED for authors (header); venue and year are not stated in the extracted text (see Read line).

### P04_smith2014 — Gillian Smith (2014). *Understanding Procedural Content Generation: A Design-Centric Analysis of the Role of PCG in Games*
- **Read:** `P (full)` · conference paper (CHI 2014, 10 pages, session Understanding and Designing Games) · ACM CHI · skipped: reference list · domain: PCG
- **Thesis:** Replayability is too broad and incomplete a justification for using procedural generation. Sorting a PCG system's mechanical features (what it builds with, when it runs, what the player controls, whether it designs for experience) against the dynamics and aesthetics they produce shows several distinct payoffs, only one of which a large pool of human-authored content could not supply.
- **Core arguments:**
  1. A common design vocabulary for PCG is needed that joins the researcher's concern (how the generator works) to the designer's (what the player experiences) (§Introduction).
  2. Five technical approaches (optimisation, constraint satisfaction, grammars, content selection, constructive) have different design tradeoffs; the paper counts content selection as PCG when it procedurally builds what the player experiences (§Background).
  3. Using MDA, the mechanics layer has four aspects: building blocks (experiential chunk, template, component pattern, subcomponent, ordered by decreasing authorial burden), game stage (offline or online), player interaction with the generator (none, parameterized, preference, direct manipulation) and awareness of player experience (indirect, compositional, experiential) (§Mechanics, Table 1).
  4. The dynamics layer is the generator's relationship to other mechanics (core, partial framing, decorative) plus five player dynamics: memorization vs reaction, building generator strategies, searching a vast world, practicing in different environments, and community interaction (§Dynamics, Table 2); these in turn support the aesthetics of discovery, challenge and fellowship (§Aesthetics).
  5. Replayability then splits into three dynamics (reacting in a surprising environment, building generator strategies, practicing in different environments); the first and third could plausibly be obtained with large amounts of human-authored content, while building generator strategies is unique to what PCG offers (§Conclusions).
  6. Dropping necessity from Togelius et al.'s taxonomy, the paper argues that no content is unnecessary from a dynamics point of view because all content shapes experience (§Dynamics, Decorative; §Background).
- **Argument structure:** Premise: designers cite replayability without analysis. Move: derive categories by examining several games and research systems under MDA, illustrate each with named examples (Civilization IV, Borderlands, Galactic Arms Race, Endless Web), then work one extended example. Evidence is conceptual analysis with illustrative cases; the paper says it is not a survey, and the framework is not claimed to be mutually exclusive or formal enough to synthesise a game. The replayability conclusion rests on thought-comparison of each PCG game with an imagined hand-authored equivalent, never tested with players. Weakest link: claims of what human authoring could plausibly achieve (e.g. Animal Crossing, Picross) are asserted by example, not measured on cost or effect.
- **Key terms:**
  - `MDA` — mechanics (rules and algorithms), dynamics (mechanics interacting with player input), aesthetics (desired emotional responses), after Hunicke et al.
  - `experiential chunk` — a human-authored building block large enough to be experienced alone.
  - `awareness of player experience` — whether and how the generator designs for an experience: indirect, compositional, experiential.
  - `building generator strategies` — the player learns and steers the generator to get what they want.
  - `memorization vs reaction` — static content invites memorising; random/generated content demands reacting.
  - `core / partial framing / decorative` — how much of the player experience depends on the generated content.
- **Verbatim anchors:**
  - "this notion of replayability is both overly broad and incomplete as a motivation" (Abstract)
  - "Building a strategy around the generator is, clearly, only possible with an actual content generator" (§Dynamics, Building Generator Strategies)
  - "Both the first and third dynamics could be plausibly attained" (§Conclusions)
- **Apparatus — tests for a design:**
  - **P04_smith2014.Q1** *If the design justifies a generator by replayability or endless content, which of the three dynamics (react to unforeseen content, build strategies around the generator, practice in varied settings) does play actually exercise, and could a hand-authored set of comparable size produce it?* Passes if the specific dynamic is named and the generator is shown to be needed for it. Fails if the justification stops at volume or variety. Detects: unanalysed replayability claim.
  - **P04_smith2014.Q2** *Can a player learn a mapping from their action or settings to what the generator then produces?* Passes if there is a legible link between player input and generator behaviour that a player can exploit. Fails if the player sees only indirect, unlearnable variation yet the design claims strategic play against the generator. Detects: claimed generator-strategy dynamic without a learnable mapping.
  - **P04_smith2014.Q3** *Is the generator core, framing or decorative, and does the design's weight on it match?* Passes if reliance level is stated and effort is proportionate. Fails if a decorative or framing generator is credited with carrying the player experience. Detects: misplaced load on generated content.
  - **P04_smith2014.Q4** *At what level does the generator build (chunks, templates, components, subcomponents), and are the recurrence patterns visible to a player at that level?* Passes if the designer has checked that large-grained building blocks do not produce recognisable repeats. Fails if chunk-level output is called surprising without checking whether players spot the pattern (the paper warns chunk and template patterns are easy to detect). Detects: perceptible repetition.
- **Does not license:** That PCG is unnecessary for replay: the paper says only that two dynamics are plausibly obtainable from human authoring and that this is a plausible claim. It rests on illustrative examples of platformers, roguelikes and strategy map generators; it contains no player data and no narrative case, and the author calls the framework not a survey and not formal enough to synthesise a game. The community dynamic cites forum discussions and an anecdote.
- **Links:** builds on and critiques P03_togelius2011 (necessity, offline/online, directness of representation); uses the Launchpad generator also analysed in P02_smith2010 (its worked example, Endless Web, uses it); cites Hunicke et al.'s MDA. The reference list also confirms the Togelius et al. venue as IEEE Transactions on Computational Intelligence and AI in Games 3(3), 2011 (cf. P03 Read line).
- **Prior-claim check:**
  - How it uses MDA: CONFIRMED (§Background, Hunicke et al.'s MDA framework... forms the foundation; §Mechanics, §Dynamics, §Aesthetics sort the properties; only three of MDA's eight aesthetics, discovery, challenge, fellowship, are used).
  - Conclusion on the replayability justification: see Core argument 5 (§Conclusions).

### G07_short2016 — Emily Short (2016). *Beyond Branching: Quality-Based, Salience-Based, and Waypoint Narrative Structures*
- **Read:** `P (full)` · blog post · Emily Short's Interactive Storytelling (WordPress) · skipped: the 52-comment thread (including her replies about tuning King of Chicago scores), pingback list, share/footer boilerplate (text from 52 thoughts on) · domain: NARR
- **Thesis:** Branching is only one answer to the question of which piece of authored content to show next. Three others, each deciding that selection differently (player chooses among unlocked items; system picks the best-fitting; system paths back toward authored beats), avoid branching's combinatorial penalty at the cost of new bookkeeping and tuning burdens.
- **Core arguments:**
  1. The framing problem is selection: story made of content pieces, how to choose the next one; she limits scope to options giving the player moderate to high control over outcome and not primarily built on a complex simulation (§opening).
  2. Quality-based narrative (QBN) is Failbetter Games' term for narratives built from storylets unlocked by qualities; a storylet is a paragraph or two plus a choice and outcome text, and qualities are numeric variables covering inventory, skill and story progress (§QBN).
  3. QBN's strengths: many short stories slot together; resource chains weave unplanned sidequests under player control; later stories can add callbacks; it handles any-order acquisition (three clues) with four storylets, one gated, where naive branching repeats (§QBN). Its trade-offs: dull until there are many storylets, overwhelming lists at large scale, and manual hand-tracking of story progression with qualities (§QBN).
  4. Salience-based narrative (her coinage) picks from a large pool the content judged most applicable to current testable world state, so the system rather than the player decides; ties are broken at random (§Salience, Left 4 Dead/Firewatch dialogue example).
  5. Salience's strengths: build broad defaults and add more specific content later with no uniform coverage promise, and low secondary effects; its trade-offs: used where dialogue has little consequence and a separate gameplay arc supplies shape, and in a plot-sequencing form (The King of Chicago) it risks an accidental, poorly timed ending, which she suggests could be addressed by arc-aware state variables and mass randomised playthroughs (§Salience).
  6. Waypoint narrative (her coinage, from her game Glass) attaches lines to transitions between conversation topics and has NPCs pathfind toward trigger topics; player topic changes divert it, used transitions are down-weighted, and more content makes the story heal more efficiently, though the player's agency is deliberately limited (§Waypoint).
- **Argument structure:** She reasons from her own practice (Fallen London content, Glass) and named examples (Left 4 Dead, Firewatch, King of Chicago), comparing each structure against a common problem and listing advantages and then costs. Evidence is practitioner experience and case description, with no measurement; the only ranking is her stated preferences. Weakest link: salience and waypoint are terms she admits she made up and generalises from three games, two of whose uses she says are for lightly consequential dialogue; claims about easier authoring are impressions.
- **Key terms:**
  - `quality-based narrative (QBN)` — Failbetter's term: storylets unlocked by numeric qualities; the qualities are the world state.
  - `storylet` — a short unit: text, choice, outcome, with unlock conditions on qualities.
  - `salience` — how well a content item's conditions fit the current world state; best fit wins.
  - `waypoint narrative` — a topic or state graph where the system pathfinds toward authored trigger points.
  - `story healing` — returning from the player's off-path input to the next authored beat.
- **Verbatim anchors:**
  - "How do I choose which piece to show the player next?" (§opening)
  - "In contrast, in a QBN system, the qualities are the world state." (§Salience)
  - "the story engine is constantly trying to heal the story" (§Waypoint)
- **Apparatus — tests for a design:**
  - **G07_short2016.Q1** *For each unit of authored content, is there a stated selection rule (player-chosen from unlocked options, system-chosen by best fit, or system-routed toward a beat), and which?* Passes if the rule is named and testable in a log. Fails if content appears by an unstated mixture of random and flag checks. Detects: undefined selection structure.
  - **G07_short2016.Q2** *Under the design's selection rule, does writing new content increase or decrease the authoring and testing burden on existing content?* Passes if added content can be dropped in without re-checking the rest (her mid-range QBN, salience defaults) or the cost is stated. Fails if each addition commits to more content downstream. Detects: combinatorial explosion.
  - **G07_short2016.Q3** *If the system, not the author, selects scenes from world state, is there a source of dramatic shape (an authored arc, or arc-based variables) outside the matching, and has a large batch of randomised runs been inspected for never-hit and over-hit content and mistimed outcomes?* Passes if both exist. Fails if climactic or terminal content can trigger by accidental condition satisfaction, or coverage was never run. Detects: accidental ending and dead or dominant content.
  - **G07_short2016.Q4** *Where state must track progression across many content pieces, who maintains it: the engine, or the author by hand?* Passes if progression state is automated or its manual cost is budgeted. Fails if every arc needs hand-set state flags and gating mistakes are untested. Detects: bookkeeping debt.
- **Does not license:** That any of the three structures yields quality of story: the post compares authoring mechanics, not reader experience. Salience and waypoint are the author's informal coinages (she says she made them up), not established categories; QBN's name has been dropped by Failbetter itself (footnote). It excludes simulation-based storytellers by scope, so it says nothing about whether simulation yields narrative. Statements about machine learning for tuning are speculation.
- **Links:** names Ashwell's post on choice-based structures (cf. G09_ashwell2015) as the standard branching reference; storylets are developed further in G11_short_storylets [reader's inference from the pingback]; The King of Chicago, Left 4 Dead and Firewatch are cited cases, not corpus entries.
- **Prior-claim check:**
  - Quality-based narrative = storylets unlocked by numeric qualities (Failbetter's term): CONFIRMED (§QBN; footnote notes Failbetter has stopped using the name).
  - Salience-based = the system picks the best-fitting content for the world state: CONFIRMED, with a correction: the term is Short's own coinage, not an established one (§Salience).
  - Waypoint structures = ...: her definition is in Core argument 6: lines attached to topic transitions, NPCs pathfind to trigger topics, player diverts, used paths down-weighted (§Waypoint).

### G11_short_storylets — Emily Short (2019). *Storylets: You Want Them*
- **Read:** `P (full)` · blog post (short, about 900 words; the extracted text gives no date, so the year 2019 is the label supplied) · Emily Short's Interactive Storytelling (WordPress) · skipped: 29-comment thread and pingbacks (comments reply that card/deck analogy weakens as storylets grow complex; not counted as the post's argument), share/footer boilerplate · domain: NARR
- **Thesis:** A storylet (content, prerequisites, world-state effects) is a small enough, recombinable unit that most classic narrative structures can be expressed in it, and storylet systems are a good bet for games that must last, accept additions and mesh with other systems. The main structure that wastes the approach is the fully branching time cave.
- **Core arguments:**
  1. A storylet has three parts: a piece of content, prerequisites that decide when it can play, and effects on world state after it plays; other systems call them events or snippets (§opening definition).
  2. The definition deliberately leaves open how much content a storylet holds, how it is structured and how it is selected, so storylet systems range from index-card prototypes to ambitious AI-driven concepts (§opening).
  3. Classic branching shapes (gauntlet, branch-and-bottleneck, sorting hat, loop-and-grow) can be replicated if the author adds a progress stat and perhaps a menace stat (§Common Branching Structures).
  4. Time caves, where every piece of content depends on the exact route taken, are the worst fit: each piece needs a unique identifier flag and the author loses extensibility, interlocking and generalising discipline (§Common Branching Structures).
  5. Video-game structures (levels, resource gathering, grinds, casual-game progression, geography-based areas) can also be expressed, and gameplay choices between levels can be paid off narratively (§Common Video Game Structures).
  6. What storylets buy beyond replication: unusual solutions such as narrative deckbuilding and crafting, extension after writing, interlocking with other narrative circumstances in the same storyworld (§closing).
- **Argument structure:** A short advocacy piece: define the unit, show by diagrammed examples (not reproduced in the text extraction) that it subsumes older structures, note the exception, then list the benefits that follow from modularity. Evidence is the author's consulting experience (very frequently...) and named titles (StoryNexus, Fallen London, Bee, Lily's Garden); no comparison against alternatives is measured. Weakest link: can be replicated shows expressiveness, not that the result is better for players or authors, and the closing durability claim is asserted. She promises detail later.
- **Key terms:**
  - `storylet` — content plus prerequisites plus effects on world state.
  - `quality` — a numeric or flag variable that prerequisites test and effects set.
  - `time cave` — branching with no recombination; each content item depends on the full route.
  - `branch-and-bottleneck` — variation channelled back for critical moments.
  - `loop-and-grow` — the same seasons repeated with accumulating change.
- **Verbatim anchors:**
  - "Storylets are simple, atomic, robust, and recombinable." (§opening)
  - "you’re not getting most of the value of using storylets" (§Common Branching Structures)
  - "Storylet-based stories can be extended after they’ve been written." (§closing)
- **Apparatus — tests for a design:**
  - **G11_short_storylets.Q1** *Can every narrative unit in the design be stated as content + prerequisites + effects on named state, and do prerequisites and effects reference the same world-state variables the rest of the game uses?* Passes if each unit's gate and consequence are explicit and shared. Fails if units depend on hidden route history or private flags. Detects: opaque or private unit state.
  - **G11_short_storylets.Q2** *Can a new unit be added without editing existing units?* Passes if adding content needs only new prerequisites and effects. Fails if inserting content requires changes to predecessors or successors. Detects: poor extensibility (the benefit she claims for storylets).
  - **G11_short_storylets.Q3** *Is any portion of the content dependent on the exact path taken to reach it (route identifiers as gates)?* Passes if such dependence is limited to small embedded segments. Fails if a large share of content is route-keyed. Detects: time-cave structure and its combinatorial cost.
  - **G11_short_storylets.Q4** *Is there a defined way for gameplay performance to change the narrative state units test, so that consequences of play can be paid off?* Passes if play events write to the qualities that gate story units. Fails if story state and gameplay state are separate. Detects: story disconnected from play.
- **Does not license:** That storylets are adequate for everything: she names time caves as a poor fit and says the definition leaves out how content is structured and selected. It does not say storylet selection produces coherent drama, pacing or arcs (pacing is the subject of a separate post referenced in comments). The evidence is practitioner experience from interactive-fiction tools, not a study; the durability claim (good bet for years) is asserted.
- **Links:** builds on G07_short2016 (quality- and salience-based structures) and points back to it as Beyond Branching; cites Max Kreminski's survey of storylet design (not in this corpus); names branching structure types of the kind catalogued in G09_ashwell2015 (gauntlet, branch-and-bottleneck, time cave, sorting hat, loop-and-grow) [reader's inference that these names come from his post; this post does not credit him].
- **Prior-claim check:**
  - No prior claims supplied. Her definition and the stated benefits and pitfalls are in Core arguments 1, 4 and 6.

### G09_ashwell2015 — Sam Kabo Ashwell (2015). *Standard Patterns in Choice-Based Games*
- **Read:** `P (full)` · blog post (posted 26 January 2015; diagrams not in the extraction) · These Heterogenous Tasks (WordPress) · skipped: site navigation, comment/pingback list, archives, categories · domain: NARR
- **Thesis:** Choice-based works fall into a small set of recurring structural patterns, each with typical shape, state-tracking needs and a characteristic effect on how the player experiences freedom, time, world and authorial cost. The patterns are not discrete categories and many works mix them.
- **Core arguments:**
  1. Time cave: heavy branching with roughly equal-weight choices, little re-merging and so no need for state-tracking, many endings; it suits freedom and fantastic open possibility, gives short but replay-encouraging runs, and leaves the player with velocity but little grasp (§Time Cave).
  2. Gauntlet: a mostly linear central thread pruned by deadly or friendly side-branches; easiest to author, shows most players most of the important content, and conveys a hazardous or constrained world, with the meaning of side-branches mattering a great deal (§Gauntlet).
  3. Branch and bottleneck: branches regularly rejoin at events common to all versions and rely on heavy state-tracking so past choices still count; suits reflecting character growth, with similar early play that diverges as choices accumulate, and needs a fairly large piece (§Branch and Bottleneck).
  4. Quest, open map and sorting hat: quest is geography-organised modular clusters converging on few endings, giving episodic, fragmentary stories; open map makes travel reversible, giving a static, slower-paced, less directed world; sorting hat branches and rejoins early to assign the player to one of several linear tracks, giving influence at the cost that the author effectively writes several games (§Quest, §Open Map, §Sorting Hat).
  5. Floating modules: no trunk or through-line, with encounters offered by state or randomly; hard to write, collapses into a linear system without large content, and gives an incentive to expose stats (and possibly grinding) (§Floating Modules).
  6. Loop and grow: a central thread loops with state-driven unlocking and closing, emphasising regularity and momentum at the price of openness, needing a justification for repetition; spoke-and-hub is a variant (§Loop and Grow).
- **Argument structure:** A classification built from the author's earlier analysis of CYOA works: each pattern gets a structural description, a stated effect on the player, and examples. The only evidence is the author's reading of named works; the effects are interpretations, not player data. He states that the categories overlap, can simulate each other, and that his diagrams are simpler than real works. Weakest link: the experience claims (e.g. grasp, velocity, atmosphere) are critical readings with no measurement of players, and the pattern boundaries are admitted to be soft.
- **Key terms:**
  - `time cave` — heavily branching, little re-merging, no state-tracking.
  - `gauntlet` — linear thread pruned by branches that fail or rejoin quickly (deadly vs friendly).
  - `branch and bottleneck` — branches that rejoin at common events, carried by state-tracking.
  - `floating modules` — encounters available by state or chance with no trunk; computer-only.
  - `loop and grow` — a repeating thread whose options change by state each pass.
  - `state-tracking` — remembering earlier choices so later content reflects them.
- **Verbatim anchors:**
  - "The player has velocity but little grasp, vast freedom but little ability to comprehend it." (§Time Cave)
  - "the author may end up effectively having to write several different games." (§Sorting Hat)
  - "Without a large amount of content, the method tends to collapse into a linear system." (§Floating Modules)
- **Apparatus — tests for a design:**
  - **G09_ashwell2015.Q1** *Which pattern, or declared mixture, does the narrative structure follow, and does the claimed player experience match that pattern's stated effects?* Passes if the structure is identifiable and the intended effect fits (e.g. a growth story uses delayed branching with state, not a bare gauntlet). Fails if the design claims openness and consequence while its structure is a gauntlet in disguise (state not kept, branches rejoin without memory). Detects: choice illusion.
  - **G09_ashwell2015.Q2** *Where branches rejoin, does later content read the choices made before the rejoin (state-tracking), and what fraction of earlier choices have any visible downstream effect?* Passes if rejoin points consume earlier state. Fails if choices are wiped at bottlenecks. Detects: obliterated consequence.
  - **G09_ashwell2015.Q3** *For a state-driven, trunkless (floating-module) design, has content volume been counted against the claim that no through-line is needed, and do play logs show runs diverging rather than collapsing to one sequence?* Passes if distinct play-throughs share little of their content sequence. Fails if most runs show the same order of events. Detects: collapse to a linear system.
  - **G09_ashwell2015.Q4** *Is the authoring cost multiplier of the structure stated (e.g. sorting hat writes several tracks; time cave sees most content missed)?* Passes if cost and expected content seen per run are estimated. Fails if breadth is promised without a budget for what any single player will see. Detects: unreviewed unseen content.
- **Does not license:** That these eight patterns are exhaustive (he calls the list non-exhaustive) or that every work fits one. It describes hand-authored choice fiction (CYOA, Twine, Choice of Games); it makes no claim about systems that simulate worlds or generate events, apart from the floating-module remarks. The player-experience effects are the author's interpretation, not tested on players. The post is from 2015 and diagrams are missing from the extracted text.
- **Links:** cited by G07_short2016 as the standard reference on CYOA structures; its floating-module and loop-and-grow descriptions refer to Failbetter's quality-based narrative and to Short's tentative categorisation of floating modules (cf. G07_short2016, G11_short_storylets); G11 names several of the same shapes (gauntlet, branch-and-bottleneck, sorting hat, loop-and-grow, time cave) [reader's inference that G11 takes them from this post].
- **Prior-claim check:**
  - No prior claims supplied. Patterns named: time cave, gauntlet (deadly/friendly), branch and bottleneck, quest, open map, sorting hat, floating modules, loop and grow (with spoke and hub), each with its effect in Core arguments 1 to 6.
