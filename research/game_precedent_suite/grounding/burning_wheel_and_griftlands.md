# Grounding note: two social-contest referents — Burning Wheel's Duel of Wits (the scaled compromise) and Griftlands (dice replaced by cards)

## Status: FILED — reference, not canon (CLAUDE.md §0.05) · tier 3 (`research/00_INDEX.md` §1) · resolves nothing at runtime
## Date: 2026-11-12 · Lane: IN (grounding lane for `proposals/2026-11-12-subsystem-audit-suite/`) · informs design, never settles it
## What changes in `engine/season/`: nothing.

**Why this note exists.** The suite uses both as the tree carries them (`audits/05_SC_audit.md:528-535`,
`audits/05_SC_audit_addendum_B.md:349`, `:351`, `proposals/05_SC_negotiation_scene.md:10-11`). The tree grades
the Duel of Wits rules "T0 (printed)" with no fetch record and the Griftlands developer quote "T2 ... repo-side
and unverified in v3" (`research/by_lane/SC_social_contest.md:103`, `:284`; `../tables/R4_combat_social_rpgs.md`
for Griftlands' shipped rules, V2/V3 there). This note records what a page read adds. **Neither the printed
rulebook nor the developer quote was reached.**

Tags as in `../README.md`.

## 1. Burning Wheel, Duel of Wits

Sources (both are the publisher's own forum; the posts are players and forum regulars quoting or
paraphrasing the rulebook; forum grade):

| key | source | read |
|---|---|---|
| BWF1 | *Compromise - Half (or thereabouts)*, Burning Wheel Forums, thread of 2012-01-23/24, `https://forums.burningwheel.com/t/compromise-half-or-thereabouts/11671` | body, 2026-11-12 |
| BWF2 | *Confused about the Compromise ranges in Duel of Wits*, Burning Wheel Forums (about the Burning Empires text of the same procedure), `https://forums.burningwheel.com/t/confused-about-the-compromise-ranges-in-duel-of-wits/6100` | body, 2026-11-12 |
| WP-BW | `https://en.wikipedia.org/wiki/The_Burning_Wheel` (raw wikitext, rev 1369594035 of 2026-08-15) | body, 2026-11-12 |

| # | claim | tag |
|---|---|---|
| 1 | Each side has a **Body of Argument**, a total that the other side reduces; the duel is won by the side whose total is not reduced to nothing first. | [V3 BWF1, BWF2 2026-11-12], as the posters use the term |
| 2 | **The compromise the winner owes scales with how much of his own Body of Argument he lost.** "the rules for a compromise say that you get a regular compromise if your opponent's Body of Argument is reduced by half (or thereabouts)"; a reply: "If he lost 5 or more [of 10], it would've been a major compromise"; another: "There's three levels of compromise." | [V3 BWF1]; players quoting and applying the rule |
| 3 | The same shape in the sister game's text: compromise levels keyed to the fraction of the winner's total remaining; "If I started with a BoA of 6 ... and I won the Duel of Wits with 3 remaining, then it's just a compromise. If it's two dice, I owe you a major compromise." Players "get into Duel of Wits that they know they will lose just to get a compromise out of their opponent ... 'playing for the compromise'". | [V3 BWF2] |
| 4 | The game's stated stance: mechanics include "pre-negotiated roll or scene outcomes, the 'Let it Ride' rule, and the absence of hidden information"; negotiation is one of several "complex, but technically optional, sub-systems". | [V3 WP-BW 2026-11-12] |

Not established here: the exact compromise thresholds (the posters disagree on two or three levels and on
where half falls); "stakes declared before the first exchange" beyond row 4's "pre-negotiated ... outcomes"
and one search snippet quoting a rulebook line that the loser abides by "the terms the winning side set forth
at the outset" [S3]; "three volleys to an exchange" (one snippet, an example script of three volleys) [S3];
the manoeuvre list; **the Point-and-Dismiss collapse and its "21-vs-11" figure, which stay
`[UNVERIFIED single actual-play account]` as the lane file marks them.** The printed rules were not read.

## 2. Griftlands

Source: Jody Macgregor, *We lost an open-world Griftlands and gained a card game*, PC Gamer, 2019-07-12,
`https://www.pcgamer.com/we-lost-an-open-world-griftlands-and-gained-a-card-game`. Body read 2026-11-12. A
journalist's hands-on preview.

| # | claim | tag |
|---|---|---|
| 1 | The retooled game is "a narrative RPG where fights and speech checks were replaced by a card game. It basically swaps the invisible dice rolls of attacks and manipulation for a hand of Slay the Spire." | [V3 2026-11-12] |
| 2 | Negotiation and battle use separate decks; consequences enter as cards (an "ulcer" card that wastes space in the negotiation deck; a "slurred speech" card after drinking). | [V3] |
| 3 | Resolve carries from one negotiation to the next; pressing for more money raises the opponent's "Impatience", which strengthens her; a negotiation can be locked off when the player cannot pay, leaving only a threat of violence. | [V3] |

Not established here: **any developer statement that spend-and-roll persuasion was "less fun than fighting".**
One search snippet has Klei's Kevin Forbes describing an earlier build with "dice-roll skill checks in
conversation" [S3 kleiforums.com, not opened]; the quoted judgment was not found. It stays at the tree's
grade (T2, unverified in v3). Griftlands' shipped negotiation rules are `R4` §2 and `../tutorials/T05_social_rpgs.md`,
not this note.

## What this note does NOT establish

Collected from the two sections above: the printed Duel of Wits rules (thresholds, the manoeuvre list, the
length of an exchange, stakes-first at page-read grade); the Point-and-Dismiss collapse; any Klei statement of
why dice were dropped; any figure. Forum posts are folk readings of a rulebook this lane did not open.

## Bearing on the suite

The scaled compromise (the shape `05_SC` SC-P4 uses) is confirmed as the game's rule at forum grade (§1 rows 2
and 3). That dice-rolled speech checks were replaced by cards is confirmed (§2 row 1); *why* is not. No
correction to the suite: it already carries both gaps marked.
