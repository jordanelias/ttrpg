# Grounding note: Paradise Killer (Kaizen Game Works, 2020) — the trial

## Status: FILED — reference, not canon (CLAUDE.md §0.05) · tier 3 (`research/00_INDEX.md` §1) · resolves nothing at runtime
## Date: 2026-11-12 · Lane: IN (grounding lane for `proposals/2026-11-12-subsystem-audit-suite/`) · informs design, never settles it
## What changes in `engine/season/`: nothing.

**Why this note exists.** The suite states at memory grade that in Paradise Killer "the trial can be called at
any time on whatever is held; the verdict follows the case made, not the truth"
(`audits/08_FI_audit_addendum_B.md:249`). The tree held the name only
(`research/by_lane/FI_fieldwork_investigation.md:98`, a self-graded survey row).

Tags as in `../README.md`.

## Sources

| key | source | read |
|---|---|---|
| WP-PK | `https://en.wikipedia.org/wiki/Paradise_Killer` (raw wikitext, rev 1374319160 of 2026-09-11), Gameplay | body, 2026-11-12 |
| AVO | *Indie Developer Interview: Kaizen Game Works*, The Avocado, 2021-04-02, `https://the-avocado.org/2021/04/02/indie-developer-interview-kaizen-game-works` (the studio's own description of the game and its answers) | body, 2026-11-12 |
| FS | Antony de Fault, *Paradise Killer, and designing a gripping courtroom drama*, Film Stories, 2021-03-09 (a Wireframe magazine article republished), `https://filmstories.co.uk/features/paradise-killer-and-designing-a-gripping-courtroom-drama/` | body, 2026-11-12; a critic's analysis, not the developer |

Blocked: `wireframe.raspberrypi.com` (403; FS carries the same article).

## What is established

| # | claim | tag |
|---|---|---|
| 1 | "Although the player can bring the characters to trial at any time, it is more effective to gather more evidence in order to gain a conviction." | [V3 WP-PK 2026-11-12] |
| 2 | The studio's description: "The player can choose how they conduct their investigation, finding clues in any order and what to interrogate suspects about. The player constructs their own truth and accuses whoever they want in an end game trial. **The game never tells the player that they got it wrong or they failed to get a true ending.**" | [V3 AVO 2026-11-12] |
| 3 | The studio on cost: "The biggest design hurdle was the trials ... because of how much freedom we give the player"; the game "started out as a more linear game". | [V3 AVO] |
| 4 | One trial, no required outcome: "By including only a single, momentous trial at the end of the game, it no longer needs a specific outcome, since there's very little post-trial content to branch. The game is utterly open: you can convict everyone or no one, get it blindingly wrong or completely right. There is no failure". | [V3 FS 2026-11-12] |
| 5 | At trial "you can accuse just one person of each crime", so the choice turns on "which of their cases is most provable, and who deserves justice more"; the critic reports pinning crimes falsely on a character already condemned. | [V3 FS] |
| 6 | Testimony is elicited by confronting characters with what has been found; others "either corroborate or contradict it"; discrepancies end where characters "stick to their story and simply insist the others are lying", so "there are multiple possible truths for you to believe". | [V3 FS] |
| 7 | The critic's objection: thorough exploration finds "the smoking guns", "irrefutable, concrete evidence", which returns the result to a foregone conclusion. | [V3 FS] |

## What this note does NOT establish

- **How the court decides.** Rows 1 and 5 show that evidence bears on whether an accusation convicts; no source
  read states the rule (what evidence is required for a conviction on a charge, or whether an unsupported
  accusation fails). `?`. "The verdict follows the case made" is supported in shape by rows 1, 2 and 4; its
  mechanism is not established.
- Whether an underlying true account exists and is discoverable. A search snippet has the developer saying a
  consistent truth sits behind the game [S3 pcgamer.com, not opened]; row 7 (a critic) says smoking-gun
  evidence can be found. Not established at page-read grade from the developer.
- What happens after the trial (endings, executions): not read.
- Any number.

## Bearing on the suite

`08_FI_audit_addendum_B.md:249` is confirmed in its two halves: the trial may be called at any time (row 1)
and the game never grades the player's account against a true one (rows 2 and 4). The clause "on whatever is
held" is row 1's "it is more effective to gather more evidence"; the decision rule itself is not sourced.
