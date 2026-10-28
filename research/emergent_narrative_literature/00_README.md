# Emergent narrative, dynamic storytelling, narrative craft and procedural generation — a read literature and a vetting apparatus

## Status: FILED — reference, not canon (CLAUDE.md §0.05) · tier 3 (`research/00_INDEX.md` §1) · resolves nothing at runtime
## Date: 2026-10-28 · Lane: IN (cross-cutting) · Written against `15593ac`
## What changes in `engine/season/`: nothing. If this directory were deleted the game would behave identically.

**What this is.** A corpus of 42 sources (44 retrieved files) on emergent narrative, dynamic storytelling, narrative craft as it bears on player engagement, and procedural generation. Each source was read in full from locally extracted text and written up as an entry with its **thesis**, **core arguments**, **argument structure**, **key terms**, **verbatim anchors**, **tests a reviewer can put to a design**, and **what it does not license**. The tests are then regrouped into one cross-source instrument, `07_apparatus.md`.

**Why it exists.** The earlier survey of this literature was `audit/2026-06-28-narrative-state-articulation/02_prior_art_and_methodology.md` (deleted in `cadf9c75`; read it with `git show cadf9c75^:audit/2026-06-28-narrative-state-articulation/02_prior_art_and_methodology.md`), and its conclusions fed `.audit/2026-07-05-emergent-narrative-engine/`. By its own provenance note it was read from search excerpts for all but two sources, and `research/by_lane/WR_world.md` already grades that precedent as *named, not studied*. This corpus replaces named with read, and checks the earlier claims against the text (below).

**What it does not do.** It passes no verdict on Valoria or any other design. No test has been run against a design, so every row in the apparatus is a *question*, not a measurement. Evidence classes `rater`, `player` and `ablation` need people or a control run.

## Contents

| file | what it holds |
|---|---|
| `01_foundations_narrative_vs_play.md` | Juul (2001, 2002), M.-L. Ryan, Jenkins, Aylett (1999), Mateas (2001) |
| `02_interactive_drama_and_agency.md` | Aylett (2000), Louchart & Aylett, Mateas & Stern (2003, 2005), Wardrip-Fruin et al. (agency), Mawhorter et al. (choice poetics), Riedl & Bulitko, Wardrip-Fruin (Tale-Spin) |
| `03_retelling_and_the_concordia_cluster.md` | Eladhari, **Sych (2020)**, Kreminski et al. (2019 retellings), Lessard & Paré-Chouinard, Kybartas et al. (tension space), Kreminski & Mateas (history) |
| `04_sifting_curation_and_simulation.md` | Felt, Winnow, Select the Unexpected, Caves of Qud, Adams on Dwarf Fortress, Short on Ryan's thesis (**S**), RimWorld coverage (**S**) |
| `05_procedural_generation_and_choice_structure.md` | Compton, Smith & Whitehead, Togelius et al., Smith (2014), Short (beyond branching; storylets), Ashwell |
| `06_engagement_space_and_craft.md` | Ryan/Rigby/Przybylski (SDT), MDA, Fernández-Vara, Carson, Hocking, Booth (Left 4 Dead), Koster |
| `07_apparatus.md` | the instrument: 75 rows in 12 gates, the disagreements, and the crosswalk to the 26–28 Oct working survey |
| `08_not_read.md` | every candidate attempted and blocked, skipped, or only named — with the reason |

## How to read an entry

`Read` carries the **reading tag** (the working survey's vocabulary): **P (full)** primary text read in full, minus the stated skips; **P (partial)** names what was read; **S** a secondary account (journalism, a blog summarising someone else's work) — arguments are attributed to the writer read, not the person summarised; **A** abstract only (none appears in `01`–`06`; abstract-only candidates are in `08`).
`Verbatim anchors` are the only quoted source text (≤15 words each). `Apparatus` tests are `<ID>.Qn`, each with *Passes if / Fails if / Detects*. `Does not license` names what a reviewer must not conclude from the source. `Prior-claim check` compares an earlier claim about the source with the text.

## Method, and what was and was not checked

1. **Retrieval.** Open-access copies fetched 2026-10-28 to a scratch folder outside the repository, text-extracted locally (PDF reading-order text; HTML with navigation and scripts removed). SHA-256 of each fetched file is in the ledger. Five sources are Internet Archive copies of a live page that refused scripted fetches; two further hosts returned a bot-challenge page, which was not worked around (`08`).
2. **Reading.** Six Sonnet readers, one per topical batch, each reading its sources in full and writing entries as they went. The reader was told the earlier claims to check but not the working survey's entries. A shared brief fixed the format and the quote rules.
3. **Mechanical check (the falsifier for quotation).** Every verbatim anchor was checked against the extracted text of its own source: present after normalising whitespace, ligatures and dashes; ≤15 words; two or three per entry; at least one in the first half and one in the second half of the post body (comment threads, reference lists and endnotes excluded). **126 of 126 anchors passed.** The checker's control was run first: a genuine quote passes; a one-word-altered quote, a 16-word quote and a fabricated quote each fail. This checks *that the quoted words are in the source*, not that the entry reads the source correctly.
4. **Two absence claims re-tested by the orchestrator** (the cheapest claims to make wrong): "narrative paradox" is not in Aylett 1999 (text search ignoring spaces: the string occurs once in the 2000 paper and four times in Louchart & Aylett 2003, never in 1999); "ludonarrative dissonance" occurs in Hocking's post only at its title and headings.
5. **One independent critic pass** (a read-only Opus agent that saw the staged files and the source texts, never the readers' reasoning) re-tested all 29 verdicts that overturn an earlier claim, read eight entries (E02, E15, G01, T13, E10, T12, E11, T03a) against their sources for faithfulness of thesis, argument and numbers, and spot-checked ten apparatus rows. **All 29 verdicts were confirmed.** It found twelve defects, none high: wrong row ids in the crosswalk, two overclaiming rows in the disagreements table, a thesis clause that attributed to the self-determination authors a contrast they do not draw (and the test built on it), and smaller slips in links and limits. All twelve were fixed in this change; the fixes were not audited again.
6. **Briefing errors.** The prompts given to readers contained four wrong assumptions of the orchestrator's own: that Mateas (2001) uses four Aristotelian causes (it uses two), that *Agency Reconsidered* distinguishes "local" and "global" agency (it does not use the terms), that Louchart & Aylett worked from interviews with several Game Masters (one GM, sessions), and that Fernández-Vara's contrast is with "embedded narrative" (the phrase is not in the text). The readers corrected each against the source. They are not errors of the earlier survey and are not listed below.

**Known limits.** PDFs lose table cells and figures (the SDT coefficients were taken from running text; one Riedl & Bulitko figure and the Aylett 1999 word spaces are garbled). **Only 8 of the 42 entries had their thesis and arguments checked against the source by someone other than their reader**; the other 34 rest on the reader's own reading plus the anchor check, so treat them as one careful reading, not as audited. Entries average about 1,000 words, longer than the 450–700 asked; they were not trimmed. The Sych thesis and Ryan's thesis are not read (`08`).

## Corrections to the earlier notes

Each row compares a claim in the June survey (path above) with the text. *Corrected* means the claim as stated is not supported by the cited source; it does not mean the underlying fact is false elsewhere.

| claim | finding | entry |
|---|---|---|
| Aylett "coined 'emergent narrative' in 1999" | The paper uses and defines the term (18 occurrences) but does not claim to have introduced it; calls the combination with social presence "little explored". Priority was not assessed. | T01 |
| Aylett introduced the "narrative paradox" | The phrase is not in the 1999 paper; it appears in Aylett (2000) and Louchart & Aylett (2003). The 1999 paper describes the clash without the name. | T01, T11, T12 |
| Juul: games are present-tense, so recount-prose suits only a past-tense chronicle | Present-tense timing is Juul's; the conclusion about chronicle prose is not his. | T06 |
| Jenkins: "four modes" | Confirmed: evoked, enacted, embedded, emergent (functions in the introduction, modes in the headings). | T05 |
| Sych: tellability is a success criterion; Heidegger breakdown is a criticality dial; "storytelling partnership", "generative friction" and *MENU NEW GAME+* | In the 2020 paper Sych argues a wedge: critical retellings do not track system quality. The word *tellability* does not occur; breakdown appears only in the abstract in its ordinary sense; the Heidegger dial, *MENU NEW GAME+* and the exact phrase *generative friction* are not in it. "Storytelling partnership" and "friction" appear, credited to Kreminski. The thesis, which may carry the rest, is unread. | E02 |
| "Evaluating AI-based games through retellings" (2022) | AIIDE **2019**, Kreminski, Samuel, Melcer & Wardrip-Fruin. | E11 |
| Felt = Datalog-style queries with variable binding, attribute, temporal and negative constraints (and recursive causal rules); Winnow incremental; Select the Unexpected ranks by improbability | Confirmed, with one qualification: Felt offers recursive causal rules as an example of what its rule layer allows, not as something shown or used in a case study. Select the Unexpected's form: score = mean frequency of a match's properties among matches of the same pattern, lowest preferred; evaluated on 15 pairs by three raters (38/45 agree). | E08, E09, E10 |
| Caves of Qud: grammar over a ~40k-word corpus; Markov register for corrupted text; sultan = 8 events from a pool of 17 | "Over 40,000 words" is the game's whole text corpus, not a grammar input; the Markov register and the 8-of-17 structure are not in the paper. Generate-then-rationalise is confirmed. | E15 |
| Tarn Adams: "write the stories you want, then build the engine"; "the player is the official will" | Neither is in his Game AI Pro chapter, which advises building iteratively and enjoying what emerges. Not tested against his other writing. | E17 |
| Compton's "10,000 Bowls of Oatmeal"; fixes include named kinds and Expressive Range Analysis | The post is titled *So you want to build a generator…*; the oatmeal argument is one named paragraph; the fixes and ERA are not in it. | P01 |
| Expressive Range Analysis validates coverage | Smith & Whitehead sample a generator on metric axes (linearity, leniency) and plot density; it shows a distribution, not coverage, and the phrase *Expressive Range Analysis* is not in the 2010 paper. | P02 |
| Short: quality-, salience-, waypoint-based structure | Confirmed; *salience-based* and *waypoint* are Short's own coinages (QBN is Failbetter's). | G07 |
| Sylvester: labels and apophenia; storyteller as pacing director | Confirmed in part, as the articles report him (two journalistic pieces; Sylvester himself unread). | G13, G14 |
| J. Ryan: emergent narrative is nonfiction; simulate richly, then curate | Confirmed *as Short reports it*; the dissertation is unread. | E12bcd |

## Cross-check against the 26–28 October working survey

Jordan's working survey (not in the repository) was supplied mid-session. Its sources overlap this corpus at eight points; the readers did not see its entries. Where both readings can be compared they agree on the numbers: Façade (about 2,500 dialogue behaviours, 27 beats with about 15 per run, at most 25% of content per run, about three person-years) and the retellings study (20 coded per game, a 10-code book, two student participants). Differences: the survey's A1 entry places "narrative paradox" in the 1999 paper (it is not there, above); its A3 entry gives "two three-hour interviews" with one Game Master, where the extracted text says only "sessions" with one named GM and gives no durations; its A10 (Riedl & Bulitko) is abstract-only and is read in full here; its A9 (Ryan) is blocked by the same repository wall as here. Its Part B (overbuild) and Part C (human capacity) are outside this corpus.

## Source ledger

Fetched 2026-10-28. `tok` is the extracted-text size in thousands of tokens (characters ÷ 4). `sha256` is the first 12 hex digits of the fetched file.

| id | citation (as written in the entry) | tag | tok | sha256 | fetched from |
|---|---|---|---|---|---|
| `E01_eladhari2018` | Eladhari, M. P. (2018). Re-Tellings: The Fourth Layer of Narrative as an Instrument for Critique | P (full) | 9k | `6480e398a6de` | https://mkremins.github.io/refs/Retellings.pdf |
| `E02_sych2020` | Sych, S. (2020). When the Fourth Layer Meets the Fourth Wall: The Case for Critical Game Retellings | P (full) | 6k | `4e378c0e7ff6` | https://www.lablablab.net/wp-content/uploads/2020/09/FourthWallCameraReady-1.pdf |
| `E04_lessard2022` | Lessard, J. & Paré-Chouinard, S. (2022). Dramatic Situations for Emergent Narrative System Authorship | P (full) | 9k | `2ca734390bc5` | https://www.lablablab.net/papers/ICIDS_Lessard_Situations.pdf |
| `E05_tension2020` | Kybartas, B., Verbrugge, C. & Lessard, J. (2020). Tension Space Analysis for Emergent Narrative | P (full) | 21k | `31956fe5a57e` | https://arxiv.org/pdf/2004.10808 |
| `E07_iens2021` | Kreminski, M. & Mateas, M. (2021). A Coauthorship-Centric History of Interactive Emergent Narrative | P (full) | 10k | `55ce282924de` | https://mkremins.github.io/publications/IENHistory_ICIDS2021.pdf |
| `E08_felt2019` | Kreminski, Dickinson & Wardrip-Fruin (2019). Felt: A Simple Story Sifter | P (full) | 11k | `806d30bbce87` | https://mkremins.github.io/publications/Felt_SimpleStorySifter.pdf |
| `E09_winnow2021` | Kreminski, Dickinson & Mateas (2021). Winnow: A Domain-Specific Language for Incremental Story Sifting | P (full) | 10k | `3165ab859b3c` | https://ojs.aaai.org/index.php/AIIDE/article/download/18903/18668/22669 |
| `E10_stu2022` | Kreminski, Dickinson, Wardrip-Fruin & Mateas (2022). Select the Unexpected: A Statistical Heuristic for S | P (full) | 11k | `880f5353e632` | https://mkremins.github.io/publications/StU_ICIDS2022.pdf |
| `E11_retellings2019` | Kreminski, M., Samuel, B., Melcer, E. & Wardrip-Fruin, N. (2019). Evaluating AI-Based Games through Retel | P (full) | 9k | `0e43c25b02b7` | https://cdn.aaai.org/ojs/5223/5223-52-8321-1-10-20190920.pdf |
| `E12b_short_ryan_ch1-3` | Short (2019) on Ryan (2018), Curating Simulated Storyworlds | S | 2k | `715ca25867ca` | https://emshort.blog/2019/05/21/curating-simulated-storyworlds-james-ryan/ |
| `E12c_short_ryan_ch4-5` | Short (2019) on Ryan (2018), Curating Simulated Storyworlds | S | 3k | `96a92ea91a0c` | https://emshort.blog/2019/05/23/curating-simulated-storyworlds-james-ryan-2/ |
| `E12d_short_ryan_ch6f` | Short (2019) on Ryan (2018), Curating Simulated Storyworlds | S | 1k | `cc6f2dc2ad9b` | https://emshort.blog/2019/05/28/curating-simulated-storyworlds-james-ryan-ch-6f/ |
| `E15_qud2017` | Grinblat & Bucklew (2017). Subverting Historical Cause & Effect: Generation of Mythic Biographies in Cave | P (full) | 8k | `7245a1975af9` | https://freeholdgames.com/papers/Generation_of_mythic_biographies_in_Cavesofqud.pdf |
| `E16_riedl2013` | Riedl & Bulitko (2013). Interactive Narrative: An Intelligent Systems Approach | P (full) | 9k | `76f45ea64f5b` | https://faculty.cc.gatech.edu/~riedl/pubs/aimag.pdf |
| `E17_adams_gameaipro` | Adams (2015). Simulation Principles from Dwarf Fortress (Game AI Pro 2, ch. 41) | P (full) | 1k | `c3feed47dd05` | https://www.gameaipro.com/GameAIPro2/GameAIPro2_Chapter41_Simulation_Principles_from_Dwarf_Fortress.pdf |
| `G01_sdt2006` | Ryan, Rigby & Przybylski (2006). The Motivational Pull of Video Games: A Self-Determination Theory Approa | P (full) | 19k | `3541204dae64` | https://selfdeterminationtheory.org/SDT/documents/2006_RyanRigbyPrzybylski_MandE.pdf |
| `G03_mda` | Hunicke, LeBlanc & Zubek (2004). MDA: A Formal Approach to Game Design and Game Research | P (full) | 4k | `f024c53fde7d` | https://users.cs.northwestern.edu/~hunicke/MDA.pdf |
| `G04_fernandez2011` | Fernández-Vara (2011). Game Spaces Speak Volumes: Indexical Storytelling | P (full) | 10k | `a9c97b0b275b` | https://dl.digra.org/index.php/dl/article/download/512/512 |
| `G05_carson2000` | Carson (2000). Environmental Storytelling: Creating Immersive 3D Worlds Using Lessons Learned from the Th | P (full) | 6k | `bbb08358b6aa` | https://www.gamedeveloper.com/design/environmental-storytelling-creating-immersive-3d-worlds-using-lessons-learned-from-the-theme-park-industry |
| `G06_hocking2007` | Hocking (2007). Ludonarrative Dissonance in Bioshock | P (full) | 9k | `3d9a87757c61` | https://web.archive.org/web/2012id_/http://clicknothing.typepad.com/click_nothing/2007/10/ludonarrative-d.html (archive copy) |
| `G07_short2016` | Emily Short (2016). Beyond Branching: Quality-Based, Salience-Based, and Waypoint Narrative Structures | P (full) | 7k | `5d8189f23e92` | https://emshort.blog/2016/04/12/beyond-branching-quality-based-and-salience-based-narrative-structures/ |
| `G09_ashwell2015` | Sam Kabo Ashwell (2015). Standard Patterns in Choice-Based Games | P (full) | 4k | `0f827299b7a7` | https://heterogenoustasks.wordpress.com/2015/01/26/standard-patterns-in-choice-based-games/ |
| `G10_booth2009` | Booth (2009). The AI Systems of Left 4 Dead | P (full) | 5k | `6ae1af1ff2b1` | https://steamcdn-a.akamaihd.net/apps/valve/2009/ai_systems_of_l4d_mike_booth.pdf |
| `G11_short_storylets` | Emily Short (2019). Storylets: You Want Them | P (full) | 2k | `71dbf641be25` | https://emshort.blog/2019/11/29/storylets-you-want-them/ |
| `G12_koster2012` | Koster (2012). Narrative is not a game mechanic | P (full) | 16k | `4bdacb536a91` | https://www.raphkoster.com/2012/01/20/narrative-is-not-a-game-mechanic/ |
| `G13_rps_rimworld` | Wiltshire, Rock Paper Shotgun (n.d.), reporting Tynan Sylvester. How RimWorld Generates Great Stories | S | 2k | `fd6eed808dd4` | https://www.rockpapershotgun.com/how-rimworld-generates-great-stories |
| `G14_sylvester_gd` | Game Developer staff (2016). How RimWorld fleshes out the Dwarf Fortress formula | S | 2k | `86746f167a6f` | https://www.gamedeveloper.com/design/how-i-rimworld-i-fleshes-out-the-i-dwarf-fortress-i-formula |
| `P01_compton2016` | Kate Compton (2016). So you want to build a generator… | P (full) | 6k | `fc874b0c0f1a` | https://web.archive.org/web/20230524210809id_/https://galaxykate0.tumblr.com/post/139774965871/so-you-want-to-build-a-generator (archive copy) |
| `P02_smith2010` | Gillian Smith & Jim Whitehead (2010). Analyzing the Expressive Range of a Level Generator | P (full) | 6k | `39648bd9593e` | https://www.pcgworkshop.com/archive/smith2010analyzing.pdf |
| `P03_togelius2011` | Julian Togelius, Georgios N. Yannakakis, Kenneth O. Stanley & Cameron Browne (2011). Search-based Procedu | P (full) | 22k | `e86cc21a73ba` | https://web.archive.org/web/2023id_/http://julian.togelius.com/Togelius2011Searchbased.pdf (archive copy) |
| `P04_smith2014` | Gillian Smith (2014). Understanding Procedural Content Generation: A Design-Centric Analysis of the Role  | P (full) | 13k | `9fc675a029d2` | https://www.cas.mcmaster.ca/~carette/CAS761/Understanding%20PCG-A%20Design%20Centric%20Analysis.pdf |
| `T01_aylett1999` | Ruth Aylett (1999). Narrative in Virtual Environments — Towards Emergent Narrative | P (full) | 5k | `99e481ae85b0` | https://cdn.aaai.org/Symposia/Fall/1999/FS-99-01/FS99-01-014.pdf |
| `T02_mateas2001` | Michael Mateas (2001). A Preliminary Poetics for Interactive Drama and Games | P (full) | 11k | `f7f8e8cc1904` | https://www.cs.uky.edu/~sgware/reading/papers/mateas2001preliminary.pdf |
| `T03a_facade_gdc03` | Mateas & Stern (2003). Façade: An Experiment in Building a Fully-Realized Interactive Drama | P (full) | 19k | `97887a4370e0` | https://faculty.cc.gatech.edu/~isbell/classes/reading/papers/MateasSternGDC03.pdf |
| `T03b_facade_aiide05` | Mateas & Stern (2005). Structuring Content in the Façade Interactive Drama Architecture | P (full) | 8k | `8335c4c9aeb6` | https://cdn.aaai.org/AIIDE/2005/AIIDE05-016.pdf |
| `T04_juul2002` | Jesper Juul (2002). The Open and the Closed: Games of Emergence and Games of Progression | P (full) | 4k | `23ec8d98891a` | https://www.jesperjuul.net/text/openandtheclosed.html |
| `T05_jenkins2004` | Henry Jenkins (2004). Game Design as Narrative Architecture | P (full) | 11k | `cccdbfc39a7b` | https://web.mit.edu/~21fms/People/henry3/games&narrative.html |
| `T06_juul2001` | Jesper Juul (2001). Games Telling Stories? A brief note on games and narratives | P (full) | 8k | `43a813b604cc` | https://web.archive.org/web/2023id_/http://www.gamestudies.org/0101/juul-gts/ (archive copy) |
| `T07_ryan2001` | Marie-Laure Ryan (2001). Beyond Myth and Metaphor: The Case of Narrative in Digital Media | P (full) | 12k | `2b9e586b8c2c` | https://web.archive.org/web/2023id_/http://www.gamestudies.org/0101/ryan/ (archive copy) |
| `T08_agency2009` | Wardrip-Fruin, Mateas, Dow & Sali (2009). Agency Reconsidered | P (full) | 11k | `38b4b8dad3f4` | https://www.cs.uky.edu/~sgware/reading/papers/wardripfruin2009agency.pdf |
| `T10_choicepoetics` | Mawhorter, Mateas, Wardrip-Fruin & Jhala (2014). Towards a Theory of Choice Poetics | P (full) | 12k | `e7b0eca6702c` | https://cs.wellesley.edu/~pmwh/research/papers/towards-choice-poetics-fdg-2014.pdf |
| `T11_aylett2000` | Aylett (2000). Emergent Narrative, Social Immersion and "Storification" | P (full) | 9k | `bf9976d78bd0` | https://www.macs.hw.ac.uk/~ruth/Papers/narrative/NILE00.html |
| `T12_louchart2003` | Louchart & Aylett (2003). Solving the narrative paradox in VEs – lessons from RPGs | P (full) | 3k | `3f677a3bad90` | http://www.macs.hw.ac.uk/~ruth/Papers/narrative/IVA03-Louchart-Aylett.pdf |
| `T13_wardripfruin2008` | Wardrip-Fruin (2008). Reading Digital Literature: Surface, Data, Interaction, and Expressive Processing | P (full) | 13k | `f8a2f8f34f9d` | https://companions.digitalhumanities.org/DLS/content/9781405148641_chapter_8.html |
