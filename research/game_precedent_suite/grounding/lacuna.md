# Grounding note: Lacuna (DigiTales Interactive, 2021) — the developer's design devlog

## Status: FILED — reference, not canon (CLAUDE.md §0.05) · tier 3 (`research/00_INDEX.md` §1) · resolves nothing at runtime
## Date: 2026-11-12 · Lane: IN (grounding lane for `proposals/2026-11-12-subsystem-audit-suite/`) · informs design, never settles it
## What changes in `engine/season/`: nothing.

**Why this note exists.** `audits/19_LACUNA_investigation_to_proceedings.md` §1 rests on a developer devlog it
read from the web and did not file. The tree's own Lacuna section
(`../tutorials/T19_tactics_narrative.md:228-298`) was built from reviews and a Steam record and does not hold
the devlog. This note stores the devlog's statements so the suite can cite a repository path.

Tags as in `../README.md`: `[V3 url date]` page body read by this lane; `[S3]` snippet; `[M]` memory; `?` not
established.

## Sources

| key | source | read |
|---|---|---|
| GWO | Julian Colbus (CEO, DigiTales Interactive), *Detective game design problems*, Game World Observer, 2020-11-08 (first published on the studio's blog), `https://gameworldobserver.com/2020/11/08/detective-game-design-problems` | body, 2026-11-12; every quotation below was checked against the fetched text |
| GD | Julian Colbus, *Detective Game Design: Puzzles vs. Story (Lacuna Devlog)*, Game Developer, 2020-09-28, `https://www.gamedeveloper.com/design/detective-game-design-puzzles-vs-story-lacuna-devlog-` | body, 2026-11-12; the quotations in the second table were checked against the fetched text |

Both pieces were written about seven months before release (2021-05-20); they describe the design as
intended, not the shipped game. The shipped game is covered by `T19:228-298`.

## What is established (GWO, body read)

| # | statement | tag |
|---|---|---|
| 1 | Two stated principles: **"no takebacks"** ("the player only get[s] one shot at every decision, dialog, and puzzle. The game auto-saves and doesn't allow you to go back") and **"limited feedback"** ("the player often isn't told immediately whether a solution was correct and what the consequences of their actions and decisions will be"). | [V3 GWO 2026-11-12] |
| 2 | **"Principle 1: Many channels out, few channels back in."** Out: "dialogs, objects, environments, the news, and e-mails (with all sorts of attachments)". In: "cloze texts we like to call 'Case Sheets' and (to a lesser degree) dialog choices". | [V3 GWO] |
| 3 | The answer space should be large and plausible, against guessing: avoid "a high probability to succeed by picking a random answer"; later Case Sheets "allow for 256 (4x4x4x4) or even more possible answers". The first case has four options, accepted "given that the player has only one shot". | [V3 GWO] |
| 4 | The Sheet is issued early and may be submitted at any time after: "This way, the player cannot know when exactly they possess enough information to solve it correctly. It also allows them to just submit any random solution if they completely get stuck". The first Sheet reads "The shot was fired from ____". | [V3 GWO] |
| 5 | Clues are mixed with "fluff, world-building, or even red herrings". Harder cases need "testimonies, news articles etc. from earlier levels", "and some cases span multiple levels". | [V3 GWO] |
| 6 | A wrong Sheet is **not blocked** ("It allows brute-forcing"; "It doesn't make sense that the Case Sheet or the person reviewing it knows the right answer and is withholding it"); there is **no game over** ("they break the immersion"); wrong answers are **not built out as dead-end levels**. | [V3 GWO] |
| 7 | What a wrong answer does in the example: the player boards a train, is then told of "an anonymous tip made by someone at Sakura Hotel" and sent there; the developer's own word for it is that the player "just got railroaded back to the correct path". | [V3 GWO] |
| 8 | **Cascade:** "every incorrectly solved case makes it more likely (or even inevitable) that the player will fail the bigger ongoing case. Failing the first act's overarching case will in turn lead to information not being obtainable in the second act, which in turn prevents the player from getting one of the two 'best' endings". | [V3 GWO] |
| 9 | The developer names the cost: "the player may find it unfair or, even worse, not realize at all that they cannot know the solution to a later puzzle due to having failed an earlier one". | [V3 GWO] |
| 10 | Checklist at the close of the article: one shot at the Sheet; "the player can always submit their Case Sheet, which ends the level and starts the next one"; hints are "Highlight Mode (which highlights new information sources) and redundant clues (i.e. multiple ways to obtain the same information)"; "the Case Sheet does not ask how they arrived at the conclusion". | [V3 GWO] |

## What this note does NOT establish

- That the shipped game matches the 2020 design in every point. Shipped behaviour is `T19:228-298` (reviews,
  an achievement guide, the Steam record).
- Reply timers: not in GWO. `T19` carries them from reviews.
- Any effect of tone (agreeable or aggressive) on the plot: `?`, as `T19` and `19_LACUNA` §1.2 already say.
- Anything systemic. The devlog describes authored cases with an answer key; it is a design argument by the
  game's author, one studio, one game.

## What is established (GD, body read)

| # | statement | tag |
|---|---|---|
| 11 | **Dialogues are single-play.** "Dialogs in adventures often loop back to one central node ... In Lacuna, each dialog can only be played a single time. Dialogs branch based on player decisions, which oftentimes lead to consequences later in the game". | [V3 GD 2026-11-12] |
| 12 | Saving: "an automatic save system ... that always overrides your previous save file (in that slot)"; "three save slots"; "the game only saves after each level". | [V3 GD] |
| 13 | No notice of what matters: "we were never fans of 'x will remember this'"; the game "doesn't disclose which decisions matter more than others, quietly adapting to the player's behavior"; "the reasons for certain consequences need to be made clear later to mitigate frustration". | [V3 GD] |
| 14 | Searching is not the challenge: Investigation Mode recognises and highlights nearby objects "because we don't consider searching things a particularly interesting type of challenge". Highlight Mode puts "colored outlines on evidence and people holding new information" and so also tells the player when nothing new remains. | [V3 GD] |
| 15 | A clue can open a dialogue: investigating a locked cupboard "unlocks a new dialog with a witness who gives the player the keys". | [V3 GD] |
| 16 | "The player isn't told (right away) if their answer was right or wrong, even though they're always sent to the right building." | [V3 GD] |
| 17 | After a wrong first answer: a squad-mate follows up the wrong building, "and they will later learn that it turned out to be a dead end. Plus, Gary will make a snarky comment about the player's misstep in the next level." | [V3 GD]; the same sentence is in GWO |

## Bearing on the suite

`19_LACUNA` §1.1 to §1.5 rows tagged `[P GWO]` or `[P GD]` are confirmed by rows 1 to 17 (each quotation that
audit gives was found in the fetched text). Rows it tags `[T19 ...]`, `[V ...]` or `[S ...]` are outside this
note and keep their own tier.
