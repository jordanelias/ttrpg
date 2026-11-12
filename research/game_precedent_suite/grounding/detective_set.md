# Grounding note: six detective referents the tables do not cover — The Case of the Golden Idol, Outer Wilds, Her Story, Danganronpa, Blade Runner (1997), Heavy Rain

## Status: FILED — reference, not canon (CLAUDE.md §0.05) · tier 3 (`research/00_INDEX.md` §1) · resolves nothing at runtime
## Date: 2026-11-12 · Lane: IN (grounding lane for `proposals/2026-11-12-subsystem-audit-suite/`) · informs design, never settles it
## What changes in `engine/season/`: nothing.

**Why this note exists.** The audit suite names these six in its detective precedent
(`audits/08_FI_audit.md:956-977`, `audits/08_FI_audit_addendum_B.md:215-252`, `audits/16_PESSIMIST_FI.md:838`,
`audits/21_PROCEDURAL_GENERATION.md:111`). Before this note the tree held, for each, at most a row of an
unattributed, self-graded survey (`research/by_lane/FI_fieldwork_investigation.md:21`, `:93-99`), and for Her
Story and Heavy Rain nothing. One file holds all six because each rests on one page; games with more than one
source have their own note in this directory.

**Every row below is a single encyclopedia article's gameplay section**: a secondary summary, read in body as
raw wikitext, good for the shape of a mechanic and not for any figure. Tags as in `../README.md`.

## 1. The Case of the Golden Idol (Color Gray Games, 2022)

Source: `https://en.wikipedia.org/wiki/The_Case_of_the_Golden_Idol`, rev 1367915385 of 2026-08-05, Gameplay. Body read 2026-11-12.

| # | claim | tag |
|---|---|---|
| 1 | Each level is "a frozen point in time"; in Exploring mode the player clicks characters, objects and documents "to collect key words of interest, such as names, places, verbs, and items". | [V3] |
| 2 | In Thinking mode "words of interest are used to piece together a narrative of what has occurred, through filling in blank slots against an incomplete description of events and characters". | [V3] |
| 3 | **The machine grades by segment and reports nearness**: "slots are completed in segments, with the player being notified when the words in that segment are either entirely correct, in which case the segment is locked in, or when the segment has more or less than two incorrect words allocated" (the article's wording of the second case is unclear as written). | [V3]; the exact threshold is `?` |

Not established: whether a wrong fill has any cost; the sequel's rules.

## 2. Outer Wilds (Mobius Digital, 2019)

Source: `https://en.wikipedia.org/wiki/Outer_Wilds`, rev 1383784780 of 2026-11-04, Gameplay. Body read 2026-11-12.

| # | claim | tag |
|---|---|---|
| 1 | The loop resets on death and "regardless after 22 minutes". | [V3] |
| 2 | **Knowledge is what persists**: "Nothing is brought back with the Hatchling when the time loop resets, with the exception of the data on the spacecraft's computer, which displays the information and mysteries that the player has found so far, organized either by location or in a web of connections." | [V3] |
| 3 | Places change within a loop, "making some areas only accessible from specific points in the time loop". | [V3] |

Not established: that knowledge alone opens every gate (the suite's "knowledge gates traversal"). Rows 2 and 3
support it in shape; the article does not state it as a rule. The developer's GDC talk and thesis that the
article cites were not opened.

## 3. Her Story (Sam Barlow, 2015)

Source: `https://en.wikipedia.org/wiki/Her_Story_(video_game)`, rev 1375576708 of 2026-09-18, Gameplay. Body read 2026-11-12.

| # | claim | tag |
|---|---|---|
| 1 | A database of 271 short clips from seven police interviews; "The interviews are unable to be watched in their entirety". | [V3]; the counts are the article's |
| 2 | **Access is by what the player thinks to search for**: answers are transcribed "and the player can find clips by searching in the database for words from the transcriptions, attempting to solve the case by piecing together information". The player may add their own tags, which become searchable. | [V3] |
| 3 | A "database checker" shows how many clips have been viewed. | [V3] |

Not established: whether a search returns every matching clip or only some (the gameplay section does not
say; not stated here from memory); any verdict or grading (the gameplay section describes none).

## 4. Danganronpa: Trigger Happy Havoc (Spike, 2010)

Source: `https://en.wikipedia.org/wiki/Danganronpa:_Trigger_Happy_Havoc`, rev 1384033957 of 2026-11-06, Gameplay. Body read 2026-11-12.

| # | claim | tag |
|---|---|---|
| 1 | "stylistically similar to Capcom's *Ace Attorney* series by being centered around investigation and finding contradictions, albeit with an emphasis on faster gameplay". | [V3] |
| 2 | Evidence and testimony gathered are stored in the player's e-Handbook; the Class Trial follows once all evidence is found. | [V3] |
| 3 | **Nonstop Debate**: characters talk, "weak points" are highlighted; the player holds "Truth Bullets" (evidence) and "must find a lie or contradiction amongst the weak points and shoot it with a bullet containing the evidence that contradicts it". Sometimes a classmate's remark is absorbed and used as ammunition against another. | [V3] |
| 4 | Errors cost Influence (hearts); "The game ends if the player loses all of their Influence, or if they run out of time during a segment." | [V3] |

Agrees with the tree: `../tutorials/T19_tactics_narrative.md:226` and `../dispositions/D_T05.md` row 40 already
assign "one correct pair per round, the space pruned" to this game's Nonstop Debate and not to Ace Attorney.
Not established: the pruning counts (2 to 4 statements, 1 to 3 bullets), which stay the companion's unsourced
figures.

## 5. Blade Runner (Westwood Studios, 1997)

Source: `https://en.wikipedia.org/wiki/Blade_Runner_(1997_video_game)`, rev 1384597603 of 2026-11-09, Gameplay and Development. Body read 2026-11-12.

| # | claim | tag |
|---|---|---|
| 1 | "Which characters are replicants is randomized each time a new game is started." | [V3] |
| 2 | The player chooses what to do with a tested subject (kill, arrest, let go), "with the decision influencing the rest of the storyline". | [V3] |
| 3 | Questioning has a manner: one of five demeanour settings (Polite, Normal, Surly, Erratic, User Choice). | [V3] |
| 4 | Other characters act on their own: "as McCoy investigates and gathers clues, the NPC characters are doing the same, completing their own objectives"; "NPC behavior was not scripted. Instead, each NPC is assigned certain goals to accomplish based upon whether they are a replicant or a human." | [V3]; the first cites the manual, the second a making-of article, neither opened |

**Precision for the suite.** What is randomised is *which characters are replicants*, over an authored cast.
"Randomised culprit" is a fair short form only in that sense. Not established: that evidence is generated to
match (the suite's "evidence must therefore be generative"); the article does not say how clues follow the
randomisation.

## 6. Heavy Rain (Quantic Dream, 2010)

Source: `https://en.wikipedia.org/wiki/Heavy_Rain`, rev 1384520746 of 2026-11-08, Gameplay. Body read 2026-11-12.

| # | claim | tag |
|---|---|---|
| 1 | "an interactive drama and action-adventure game in which the player controls four different characters"; "Each playable character may die depending on the player's actions, which create a branching storyline". | [V3] |

Nothing in the article's gameplay section describes an investigation mechanic the suite could use, and the
suite makes no claim about this game (`08_FI_audit_addendum_B.md:252`, `:384`: "no claim"). This section exists
so that the name in the brief resolves to a repository path. It establishes nothing about evidence or deduction.

## What this note does NOT establish (all six)

Any figure; any first-party statement; anything about sequels or later patches; any claim about how these
designs were received. One article per game is one source: none of these rows counts as a convergence.
