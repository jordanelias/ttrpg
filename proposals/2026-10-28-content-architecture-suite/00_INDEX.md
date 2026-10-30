# Valoria review suite: index

## Status: PROPOSED (2026-10-28 session; reconstructed 2026-10-30) — HELD BACK IN FULL. Reference under CLAUDE.md §0.05: not a mechanism; merging ratifies nothing.
## Lane: IN

## Provenance

The index. Base: `write_072830_00_INDEX.md`, the session's final write of the index (07:28:30); no later patch touches it. An earlier write, `write_071053_00_INDEX.md`, is superseded and was not used. The index's own text is unchanged except for the added header (the Status and Lane lines and this Provenance section) and the added section 'What is in this directory, and what is not recovered'. No patch script was replayed on it. The suite was written in a session of 2026-10-28 that committed nothing; its files existed only in that session's scratchpad. This directory is a reconstruction from the session transcript's surviving reads and patch scripts, not the original files. Recovered in a second pass (2026-10-30), each with its own provenance: parts 05 and 07a to 07d, and the lens-3 (directive-compliance) critic report (`critic_lens3.md`). Still not recovered: part 06 and appendices A1 to A5 (see `00_INDEX.md`). Edits the session made by tools other than Bash heredocs (Edit-tool calls) were not captured, so the text may differ from the session's final file in ways not recorded here. Where this text and the tree disagree, the tree wins; every figure and line citation is as of the session's HEAD (`ttrpg` be24c71) and is unre-verified.

---

Repo state: `ttrpg` at be24c71 (2026-10-28); branch `claude/game-content-systems-review-r9ce5q`. Nothing in the repo was edited, committed or pushed; this suite is review material only. Part 01 opens with a one-paragraph glossary of the repo's words (seat, rung, verb row, claim, Record, field, query).

## The answer in one page

The engine is a lawful society simulator, not yet a game. It has a seeded realm (83 persons, 37 settlements, 32 offices, 38 goals), a season loop and resolvers for combat, Proceedings, fieldwork and mass battle. It has no human seat, no capability values, no authoring layer, no authored situations and no words. Workplan v10 reaches a ported simulator and says content is not its job. Five gaps block play, in this order: a seat for a human, capability, an authoring layer, situations, words (part 01 §0).

Your constraints shape every recommendation. Only a person acts on the world (AX-1), but the player also gets an abstract management surface that costs no scene budget. Each subsystem is a minigame on the one season-loop seam. Templates are permitted, so an unfilled instance is not "missing content". Storylines, set pieces and event decks are wanted, scripted as openings and sequences and never as whole arcs.

## Map of the suite

| part | file | what it answers |
|---|---|---|
| 01 | `01_MAIN_REPORT.md` | Q1 to Q8 answered; §8 storylines; §11 your decisions and the 12 rulings; §12 reliability; §13 management surface; §14 minigames; §15 later directives |
| 02 | `02_P1_templates.md` | Three template proposals (character, faction, settlement, event deck, set piece, troop, kit) |
| 03 | `03_P2_attributes_skills_histories.md` | Three proposals for attributes, skills, histories, progression, plus a ten-score variant |
| 04 | `04_P3_player_surface.md` | Three proposals for the player surface, with per-subsystem cards |
| 05 | `05_A7_subsystem_merit.md` | What each subsystem is worth alone and in the world; order of becoming playable |
| 06 | `06_A6_attribute_demand.md` | Attribute set derived from what the verbs and subsystems demand |
| 07a to 07d | `07a..07d_ADJ*.md` | Adjudication of 754 recorded conflicts, by cluster (parts 01 to 05 follow it, as corrected by the review) |
| appendix | `appendix/A1..A5` | Analyst reports: content census, character, faction and settlement, subsystems, events and arcs |

## What is in this directory, and what is not recovered

Present: this index; part 01 in two files (`01_MAIN_REPORT.md` for sections 0 to 9 and `01_MAIN_REPORT_part2.md` for sections 10 to 15, split because the whole was about 58 KB); `02_P1_templates.md`, `03_P2_attributes_skills_histories.md`, `04_P3_player_surface.md`; and, from the second pass (2026-10-30), `05_A7_subsystem_merit.md`, `07a_ADJ1_character_verbs.md`, `07b_ADJ2_faction_settlement.md`, `07c_ADJ3_events_arcs_clocks.md`, `07d_ADJ4_subsystems_ui_process.md` and `critic_lens3.md` (the lens-3 critic's hand-back, with the brief it was given). Each file's own Provenance says which write or read its text came from and which patch scripts were replayed. Parts 05 and 07a to 07d are as the session left them at 07:28: every Edit-tool call and heredoc against them was found and replayed, and their sizes match the sizes the session recorded.

Recovered in the third pass (2026-10-30): **part 06** (`06_A6_attribute_demand.md`), its evidence (`06b_A6_matrix_and_probe_evidence.md`: the 104-moment matrix scripts, the P2 probe and their printed output) and **appendices A1 to A5** (`appendix_A1_content_census.md`, `appendix_A2_character.md`, `appendix_A3_faction_settlement.md`, `appendix_A4_subsystems_playable.md`, `appendix_A5_events_and_arcs.md`; the map above lists them as `appendix/A1..A5`, and they are flat files here). Each was rebuilt from the session's Write, Edit and heredoc calls, the replayed size equal to the size the session recorded. The session's separate A6 and A7 analyst reports are not extra files: the A6 report is part 06, and part 05 is the suite's copy of A7. Still not recovered: the session's pre-06:05 events (the half before the analysts' dispatch) were not paged beyond what these files needed, so the digests (about 3 MB of source) the analysts read are not reproduced. `fragments_of_unrecovered_parts.md` is superseded by the recovered files and kept only as a record of the second pass. Two notes the session wrote into A1 and 07a after the three-lens review applied to the appendix too: the refusal percentages 77.8% and 58.8% are withdrawn, and the 45-of-56 figure for an unseated person is superseded by part 04 §1 (41 rows every person has, plus the seat's own); so is the claim that appointing starts at a duchy seat (which orders a seat offers depends on its remit list).

## The three proposal sets and the recommended package

| | A | B | C |
|---|---|---|---|
| Templates and storylines (part 02) | the baseline: starting facts only, the same stories in every world | **story openings drawn from pools when the world is built, each opened only by a person's own choice** | dated beats and arcs as templates (reopens two axioms and scripts whole arcs) |
| Attributes (part 03) | **the plan's nine, with Thread Sensitivity counted as the tenth** | a demand-derived eight | six used as floors and ceilings |
| Player surface (part 04) | a text menu of the seat's real options | **a management console plus scenes, built on A's text client** | a map of the realm as the home screen |

Part 03 also names a ten-score variant (split Attention, fold Focus into Will, keep Bonds, count Thread Sensitivity) as the cheap revert for A. Recommended: **P1-B + P2-A + P3-B**, first playable slice at personal combat and a Proceedings hearing, with the first seated person at rung 1 or 2 (choose a seat whose remit includes `confer`, such as the Confessor).

## Rulings needed from you (12)

Part 01 §11 states each as a choice with what each side means. In short: (1) a stored troop count under a commander; (2) which attribute list; (3) the training rule; (4) who owns a sword; (5) story openings drawn at world build; (6) mass-battle command, plan or live; (7) founding factions in play; (8) Mayor seats; (9) a dying or a misunderstood world; (10) the management surface, weak or strong reading, and who gets free orders; (11) odds shown for acts other than combat; (12) what the console may show. Rulings 1, 2 and 5 reopen defaults you confirmed on 2026-10-26.

Not choices: Altonia's default is closed (confirmed off); the CLAUDE.md §3 wording and the `valoria-game` Godot move are housekeeping (part 01 §11).

Owed, not done (not requested this session): ledger rows for your three "yes" decisions, the no-forecast combat directive and the troop and equipment directions.
