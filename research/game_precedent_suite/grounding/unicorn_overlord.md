# Grounding note: Unicorn Overlord (Vanillaware / Atlus, 2024) — the unit grid

## Status: FILED — reference, not canon (CLAUDE.md §0.05) · tier 3 (`research/00_INDEX.md` §1) · resolves nothing at runtime
## Date: 2026-11-12 · Lane: IN (grounding lane for `proposals/2026-11-12-subsystem-audit-suite/`) · informs design, never settles it
## What changes in `engine/season/`: nothing.

**Why this note exists.** The tree sources this game well (`../tutorials/T19_tactics_narrative.md:79-155`) with
one gap it marks itself: "Grid shape 2x3 [M]" (`T19:153`). The suite repeats the shape at that grade
(`audits/04_MB_audit.md:1357`, `audits/04_MB_audit_addendum_B.md:75`, `:499`). This note records the attempt to
close the gap. **It did not close at page-read grade.**

Tags as in `../README.md`.

## Sources

| key | source | read |
|---|---|---|
| WP-UO | `https://en.wikipedia.org/wiki/Unicorn_Overlord` (raw wikitext, rev 1364573866 of 2026-07-17), Gameplay | body, 2026-11-12 |
| ME | *Building the dream team: the squad system of Unicorn Overlord*, matchstickeyes.com (a player's blog), 2024-08-11, `https://matchstickeyes.com/tag/unicorn-overlord` | body, 2026-11-12; one player's account |
| snippets | a retailer listing (zatu.com) and a review (godisageek.com), seen only as search-result text | snippet, 2026-11-12 |

Blocked or empty: `unicornoverlord.atlus.com/system.html` (403); the official landing page (no system text);
`godisageek.com`, `primagames.com`, `dotesports.com`, `progameguides.com` (403); `zatu.com` (page body
truncated before the description).

## What is established

| # | claim | tag |
|---|---|---|
| 1 | "Parties are made up of up to five characters with an assigned character class. During the early game units are limited to two characters, but more character slots can be unlocked using a currency called Honors." | [V3 WP-UO 2026-11-12]; agrees with `T19:153` |
| 2 | "Units are arranged in a grid, with their position influencing their abilities and combat efficiency." | [V3 WP-UO] |
| 3 | "Battles play out automatically based on character attributes and player-set behaviors." Movement is in real time with a pause "to change strategy and check on units". | [V3 WP-UO] |
| 4 | A unit has a front row and a back row: a player describes "the two front-row characters ... soaking incoming damage" and "back row characters" in a five-member squad; "Squads battle automatically, based on the tactics set up by the player". | [V3 ME 2026-11-12] |
| 5 | The grid is **two rows of three slots** (a front rank and a back rank of three each). | **[S3]** zatu.com listing ("a two by three grid (a front and back rank of three slots each)"); **[S3]** godisageek.com review ("a 3-by-2 grid"). Two snippets that agree; neither page was opened |

## What this note does NOT establish

- The 2 x 3 shape at page-read grade: row 5 is snippet-only and stays `[S3]`. It is an upgrade from `[M]` to
  two agreeing snippets and no more. A first-party statement was not reached.
- Row 5's review snippet says "up to six characters", which conflicts with row 1 and with Atlus text as `T19:153`
  records it; the member cap is five (rows 1 and `T19`), the slot count is six `[S3]`.
- Targeting rules (who can strike the back row): one snippet only (zatu.com); not recorded as a claim.

## Bearing on the suite

The suite's "grid 2 x 3 (memory)" may be restated as "two rows of three slots, snippet grade". Nothing in the
suite's proposals depends on the shape: `proposals/04_MB_squad_grid_of_named_characters.md` adopts a row rule,
which rows 2 and 4 support at page-read grade.
