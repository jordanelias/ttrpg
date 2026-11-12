# Grounding note: Shadows of Doubt (ColePowered Games, 2024) — what is sourced about how it generates a case

## Status: FILED — reference, not canon (CLAUDE.md §0.05) · tier 3 (`research/00_INDEX.md` §1) · resolves nothing at runtime
## Date: 2026-11-12 · Lane: IN (grounding lane for `proposals/2026-11-12-subsystem-audit-suite/`) · informs design, never settles it
## What changes in `engine/season/`: nothing.

**Why this note exists.** `audits/21_PROCEDURAL_GENERATION.md` §1.1 describes the game's generation method from
three developer posts it read on the web, several search snippets, and the tree's tables. The tables
(`../tables/R5_investigation_information.md` §2; `../tutorials/T06_investigation.md`) cover what the player
does and the Resolution Form; they do not hold the developer posts. This note stores what a page read
establishes and marks what stays at snippet grade.

Tags as in `../README.md`: `[V3 url date]` body read by this lane; `[S3]` snippet; `[M]` memory; `?` not
established.

## Sources

| key | source | read |
|---|---|---|
| DB15 | ColePowered (the developer; the post is signed `@colejefferies`), *Shadows of Doubt DevBlog #15: Moving in the Citizens*, 2019-04-24, `https://colepowered.itch.io/shadows/devlog/78044/shadows-of-doubt-devblog-15-moving-in-the-citizens` | body, 2026-11-12 |
| DB28 | *Shadows of Doubt DevBlog #28: Building the World Through Writing*, 2021-10-01, `https://colepowered.itch.io/shadows/devlog/299526/shadows-of-doubt-devblog-28-building-the-world-through-writing` (written by the game's writer; "Cole and I") | body, 2026-11-12 |
| DB30 | *Shadows of Doubt DevBlog #30: The Top Shadows of Doubt Development Challenges Part I*, 2022-03-04, `https://colepowered.itch.io/shadows/devlog/354045/shadows-of-doubt-devblog-30-the-top-shadows-of-doubt-development-challenges-part-i` | body, 2026-11-12 |
| WP-SoD | `https://en.wikipedia.org/wiki/Shadows_of_Doubt` (raw wikitext, rev 1381496745 of 2026-10-22), Gameplay and Reception | body, 2026-11-12 |

Read and found to carry no method: DevBlog #16 (2019-08-05, a vertical-slice announcement), #18 (2019-11-23)
and #23 (2020-10-24), both video posts whose text says only that a video exists. Blocked: `colepowered.com`
(403), which holds the early posts (#2, #8, #10, #13) the audit quotes at snippet grade.

## What is established

| # | claim | tag |
|---|---|---|
| 1 | "The city's layout, its citizens and their routines, and all murder cases are procedurally-generated per save file, and the player can choose the city's name, size, and seed." | [V3 WP-SoD 2026-11-12] |
| 2 | "The details of each murder case are randomly configured: murders may occur anywhere and at any time, any citizen can be involved"; evidence "can include fingerprints, surveillance camera footage, witness observations"; the player contends with "false leads, time-sensitive evidence". | [V3 WP-SoD] |
| 3 | The resolution form has five fields (suspect's full name, address, evidence placing the suspect at the scene, the weapon, whether the suspect is under arrest). "Only the murderer's name is required for a successful submission, but a cash bonus is rewarded for each optional field that is correctly filled out. If the player accuses the wrong citizen, they will be fined and the real murderer will continue killing." | [V3 WP-SoD]; agrees with `R5` §2 |
| 4 | "Sometime after a murder case is resolved, the game will automatically select another citizen to carry out the next string of killings". | [V3 WP-SoD] |
| 5 | **Routines are goal-based, not pre-computed.** The developer replaced "the previous very basic AI in favour of a new goal-based system" with "a new sims-like stat system that dictates their minor actions throughout the day (needing to eat, drink, sleep etc)"; before, "their routine was almost completely pre-computed", and an interruption "could potentially break their pre-computed routine, meaning the game would have to calculate it again". | [V3 DB15 2026-11-12] |
| 6 | **Cheap unless near.** "the AI's update rate will only be high when nearest the player"; this makes "the performance cost of 95% of the citizens at any one time relatively insignificant". | [V3 DB15] |
| 7 | **Everything is saved because evidence cannot be predicted.** "Due to the nature of the game, we can't always dictate what objects are valuable sources of information for a case. Therefore when we save a game, we have to save everything. Not just objects the player is carrying or is in the immediate vicinity of, but every item in the world!" | [V3 DB30 2026-11-12] |
| 8 | Authoring tool: "Cole has created a custom-made dialogue editor with access to a wide number of procedural fields and variables". "Procedural storytelling is inherently challenging". | [V3 DB28 2026-11-12] |
| 9 | Reception: reviewers found "repetitive dialogue and case design" and "repetitive and bland" interactions exposing "limitations of the game's world". | [V3 WP-SoD, Reception] |

## What this note does NOT establish (stays at the tier the audit gave it, or lower)

- **The order of generation** (places, then companies and homes, then citizens, then a simulated stretch of
  history before play; "12 hours of history"; "x60"): snippet grade in `21_PROCEDURAL` (`[S whynowgaming/Wireframe]`,
  `[S DevBlog #10]`). Not reached here. `?` for the shipped game.
- **How the killer is chosen and how the murder is carried out** ("the AI killer picks an acquaintance", follows
  the victim until alone): snippet grade, and a prototype statement of 2018 or 2019. Not reached here. What a
  page read gives is only row 4 (the game selects another citizen).
- **The location hierarchy** (City > District > Block > Building > Floor > Address > Room > Tile): snippet grade
  (`[S DevBlog #13]`). Not reached.
- **Six killer archetypes with signature evidence**: carried by `R5` §2 from the game's wiki (V2 there); not
  re-read here.
- **Witnesses who lie; fading witness memory**: a 2018 design statement the tables could not verify shipped
  (`R5` open items). Not reached. `?`.
- **Seeds breaking across versions**: carried by `T06` §1; not re-read here.
- Population figures and the count of profile fields: carried by `R5`/`T06`; not re-read here.

## Bearing on the suite

`21_PROCEDURAL` §1.1 rows "Why the trail is true" and "How coherence is kept" (the DevBlog #30 and #15
quotations) are confirmed word for word by rows 5 to 7; the DevBlog #28 quotation by row 8. Its rows on order
and on the selection of the killer rest on snippets and are **not** confirmed; they are leads, as that audit
itself says (`21_PROCEDURAL_GENERATION.md:69-70`).
