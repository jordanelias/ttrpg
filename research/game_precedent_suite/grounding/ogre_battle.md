# Grounding note: Ogre Battle (The March of the Black Queen; Ogre Battle 64) as a battle referent

## Status: FILED — reference, not canon (CLAUDE.md §0.05) · tier 3 (`research/00_INDEX.md` §1) · resolves nothing at runtime
## Date: 2026-11-12 · Lane: IN (grounding lane for `proposals/2026-11-12-subsystem-audit-suite/`) · informs design, never settles it
## What changes in `engine/season/`: nothing.

**Why this note exists.** The audit suite used Ogre Battle at memory grade because the tree held nothing on
its battles: every earlier hit was the tarot questionnaire at character creation
(`audits/04_MB_audit_addendum_B.md:82`, `:497-505`; `proposals/04_MB_squad_grid_of_named_characters.md:31-32`,
`:100`). This note records what a page read establishes.

Tags as in `../README.md`: `[V3 url date]` page body read by this lane (raw wikitext or page text fetched and
read, not a search snippet); `[S3]` search snippet only; `[M]` memory; `?` not established.

## Sources

| key | source | what it is | read |
|---|---|---|---|
| WP-OB | `https://en.wikipedia.org/wiki/Ogre_Battle:_The_March_of_the_Black_Queen` (raw wikitext, rev 1377282037 of 2026-09-28), sections Gameplay, Battle, Alignment, Classes | encyclopedia article; its gameplay paragraphs carry no inline citation, so this is a secondary summary, not the manual | body, 2026-11-12 |
| WP-OB64 | `https://en.wikipedia.org/wiki/Ogre_Battle_64` (raw wikitext, rev 1381473342 of 2026-10-22), section Gameplay | same kind | body, 2026-11-12 |
| RPGF | Musashi, *Ogre Battle: The March of the Black Queen* (PlayStation) review, RPGFan, 2000-08-24, `https://www.rpgfan.com/review/ogre-battle-the-march-of-the-black-queen-4/` | a reviewer's description of the PlayStation release | body, 2026-11-12 |
| RPGC | `https://shrines.rpgclassics.com/shrines/snes/ogrebattle/strategy.shtml` | fan strategy page (folk model) | body, 2026-11-12; used only as corroboration |

Not reached: the instruction manual; `strategywiki.org` (403); a GameFAQs mirror (403);
`hardcoregaming101.net` (404 at the guessed address).

## What is established

| # | claim | tag |
|---|---|---|
| 1 | The player organises "multiple squads of five fighters or fewer"; large characters (dragons, griffons) count as two. | [V3 WP-OB 2026-11-12]; agrees with RPGF ("Each unit can fit 5 characters, unless the unit has any large monsters, who count as 2") |
| 2 | Squads move on a map in real time; "If two units move close to each other, a battle ensues" and the view shifts to a close-up of the two units. | [V3 WP-OB] |
| 3 | **The player does not control the fighters.** "During a battle, a player does not directly control their unit, but selects a tactic for the unit to follow (Best, Strong, Weak, Leader), which the characters follow when choosing whom to attack." | [V3 WP-OB] |
| 4 | What the four tactics mean: Best (the enemy posing the greatest threat), Strong (most HP remaining), Weak (fewest HP remaining), Leader (the enemy unit's leader). The tactic can be changed during the exchange. | [V3 RPGF]; RPGF is one reviewer's gloss, not the manual |
| 5 | **A member's row decides what it does.** "Each character has two types of actions they can execute during a skirmish, one they do when they are in the front row, and one for the rear row. For example, a Mage gets 2 attacks with his staff in the front row, but in the rear, he will cast 1 spell that affects all the enemies in the opposing unit." A Knight: 2 sword attacks in front, 1 in the rear. | [V3 RPGF]; corroborated by RPGC (back-row placement advice) and by WP-OB64 ("Many classes are most efficient in certain positions of a unit") |
| 6 | An exchange is one round: "Characters alternate taking actions with the battle ending after one round of combat (many units can attack multiple times per round). The unit that caused the most damage is the victor and forces the other unit to retreat." | [V3 WP-OB]; RPGF adds that the loser "is pushed back a short distance" and that a boss unit wins if its boss survives |
| 7 | During the exchange the player may also play a stored tarot card (damage or a special effect) and may retreat. RPGF: retreat always escapes and counts as a loss. | [V3 WP-OB]; [V3 RPGF] |
| 8 | A unit has a leader and depends on him: once deployed a unit moves "as long as the leader of that unit is still alive. If a unit's leader dies, it no longer follow[s] orders and will automatically go back to your base." | [V3 RPGF] |
| 9 | Up to 10 units deployed at once a side. | [V3 RPGF] |
| 10 | A campaign economy exists at stage scale: "Deploying a squad costs a small amount of money, which must be paid again as maintenance every time a day passes"; liberated towns pay income each day. | [V3 WP-OB] |
| 11 | Ogre Battle 64: a battalion of up to 50, sectioned into units of at most five including a leader; "automatic combat between two outfits". | [V3 WP-OB64] |
| 12 | **Whom a unit strikes is set by its tactic, not by row.** An enemy leader is "usually in the back row", and "Set your tactics in battle to Leader. This makes your spellcasters focus on the leader when casting their spells. If they kill him, the unit will leave for home even if declared victor." | [V3 RPGC], a fan strategy page; consistent with rows 3 and 4. Whether a melee attacker in the front row can reach a rear-row enemy is `?` (the page speaks of spellcasters) |

## What this note does NOT establish

- The exact grid of a unit (how many slots a row, how many rows). `?`. RPGF speaks of a front row and a rear
  row only.
- Any number: damage, the cost of deployment, class statistics. None is quoted here and none may be cited.
- Whether a leader confers a bonus on the squad (as Unicorn Overlord's does). `?`. What is sourced is that a
  unit needs a living leader to take orders (row 8).
- Anything from the instruction manual; none of the above is first-party.
- Any outcome prediction before an exchange. `?` (not found in the sources read).
- **A rule that the rear row cannot be reached while the front stands.** Not found. What is sourced is that a
  row sets the member's own action (row 5) and that targeting follows the unit's tactic (rows 3, 4, 12).

## Bearing on the suite (a judgment about existing text, not a work item)

The three memory-grade statements in `audits/04_MB_audit_addendum_B.md:497-505` (a unit of a few characters
in front and rear rows where a member's row decides what it does; one tactic a unit, whom to strike; change
the tactic, play a card, retreat) are **confirmed** by rows 1, 3, 4, 5 and 7. "Resolved automatically while
the player manages the composition and the orders" (`AUDIT_BRIEF.md`) is confirmed by rows 3 and 6.
