# Grounding note: Sherlock Holmes: Crimes & Punishments (Frogwares, 2014) — the deduction board and the conclusion

## Status: FILED — reference, not canon (CLAUDE.md §0.05) · tier 3 (`research/00_INDEX.md` §1) · resolves nothing at runtime
## Date: 2026-11-12 · Lane: IN (grounding lane for `proposals/2026-11-12-subsystem-audit-suite/`) · informs design, never settles it
## What changes in `engine/season/`: nothing.

**Why this note exists.** The suite states at memory grade: "deduction board; a chosen conclusion and a moral
choice, never corrected" (`audits/08_FI_audit_addendum_B.md:251`; also `08_FI_audit.md:971`,
`08_FI_audit_addendum_B.md:218`). The tree held the name only
(`research/by_lane/FI_fieldwork_investigation.md:93`, a self-graded survey row). **A source contradicts
"never corrected" as written** (rows 5 and 6).

Tags as in `../README.md`.

## Sources

| key | source | read |
|---|---|---|
| WP-SH | `https://en.wikipedia.org/wiki/Sherlock_Holmes:_Crimes_%26_Punishments` (raw wikitext, rev 1384346349 of 2026-11-07), Gameplay | body, 2026-11-12 |
| PCG | Andy Kelly, *Sherlock Holmes: Crimes and Punishments review*, PC Gamer, `https://www.pcgamer.com/sherlock-holmes-crimes-and-punishments-review/` (2014; the date was not read from the page) | body, 2026-11-12 |
| GB | *Sherlock Holmes: Crimes and Punishments Review*, GamingBolt, `https://gamingbolt.com/sherlock-holmes-crimes-and-punishments-review` (2014; the date and byline were not read from the page) | body, 2026-11-12 |

## What is established

| # | claim | tag |
|---|---|---|
| 1 | Clues "are added to a 'deduction board', a gameplay mechanic which involves linking pieces of information together"; "Depending on how players interpret the clues, they will have different conclusions. Therefore, the player can fail or succeed in finding the culprit." | [V3 WP-SH 2026-11-12] |
| 2 | "Players also decide whether to absolve or condemn the criminal. The moral choice the player makes will influence the further gameplay. Each case will have 3-5 possible solutions; in total there will be 6-10 different endings for each case." | [V3 WP-SH]; the counts are the article's, uncited there, and are not to be quoted as fact |
| 3 | How the board works: combining two clues forms a deduction; a deduction node may allow more than one reading; chosen readings connect "provided the conclusions drawn by Holmes match up", and enough connected nodes name a suspect. | [V3 GB 2026-11-12]; PCG: "Clues will usually offer two possible outcomes, and by selecting the right (or wrong) ones, they'll connect and give you a likely conclusion" |
| 4 | The game does not announce the answer while the case is open: "There's no 'Ah-ha!' moment from Holmes ... no gentle nudge in the right direction ... the game has the cajones to let you be wrong ... You can convict the wrong suspect". | [V3 GB] |
| 5 | **An optional reveal exists.** "The game continues regardless of your choice, though it will offer to tell you whether you were right or not, and allow you to try again until you get something you're satisfied with." | [V3 GB] |
| 6 | The same, independently: "When a case is done, you can reveal if you were wrong or not ... You can go back and replay the last part of a case if you don't like a choice you've made". The game also compares the player's solutions with other players' when online. | [V3 PCG 2026-11-12] |
| 7 | Cases are self-contained: "Each case is self-contained and apart from in-game achievements, such as moral choices, do not relate to one another." | [V3 WP-SH] |

## What this note does NOT establish

- What a wrong conclusion changes later. Row 7 says cases do not relate to one another; row 2's "will influence
  the further gameplay" is unspecific. `?`.
- Whether the reveal is on by default or behind a prompt; both reviews call it an offer.
- Any claim about the other Frogwares titles.

## Bearing on the suite (a correction)

"Never corrected" is wrong as written. The sourced statement is: the game accepts a wrong conclusion and
continues without correcting it, **and offers the player an optional reveal of whether the conclusion was
right, with a replay of the case's last part** (rows 4 to 6). The design point the suite draws (a committed
conclusion the game does not block) survives; the stronger point (the player is never told) does not hold for
this game. It does hold, on the studio's own word, for Paradise Killer (`paradise_killer.md` row 2) and, with
"right away", for Lacuna (`lacuna.md` rows 1 and 16).
