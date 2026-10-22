# Game precedent suite

## Status: FILED — reference, not canon (CLAUDE.md §0.05) · tier 3 (`research/00_INDEX.md` §1) · resolves nothing at runtime
## Date: 2026-10-22 · Lane: IN (cross-cutting) · Written against `51d7b05`
## What changes in `engine/season/`: nothing. If this directory were deleted the game would behave identically.

**What this is.** A checked body of precedent from about seventy videogames (and Pax Pamir), built so that Valoria's system description (`proposals/2026-10-22-system-description/`) can be compared with what other games do, in three layers:

| directory | what it holds | how to read it |
|---|---|---|
| `tables/` | ten capability tables (`R1`..`R9`, `R3a`, `R3b`): per game, per capability id (A1..M5, the checklist below), YES / PART / NO / `?` with a clause on how | the **what a game supports** layer. Cells carry a tag; `Still unknown` and `Sources` close each file. |
| `tutorials/` | nineteen files (`T01`..`T19`), one `### <Game> - facts line` section per game with eight headings: setup choices, the loop, the choice menu, first hour, what changes later, failure and ending, consequential vs cosmetic choices, open items | the **how it plays** layer: what a player decides, in what order, at what cost |
| `dispositions/` | thirteen files `D_T01`..`D_T10` (+ `also` files) and two records of claims checked | the **what it means for Valoria** layer: every precedent item compared with a named part of the Valoria suite |

**The rule this suite was built under.** Everything researched is used as a surface for comparative improvement, even if read and discarded. So each item routed to a Valoria tutorial (T01..T10 = suite files 02..11) has a disposition:
**HAS** (Valoria does it; cite code), **LACKS** (no equivalent; what the precedent shows), **DIFFERS** (Valoria does it otherwise on purpose; cite the ruling), **CONTRADICTS** (a claim in the suite, the repo or an upload is wrong or stale; this became an edit), **DISCARD** (no bearing; one-line reason).
866 rows: 176 HAS, 323 LACKS, 155 DIFFERS, 94 CONTRADICTS, 118 DISCARD. The corrections that CONTRADICTS rows required were applied to the Valoria suite in the same change; only the judgments (Part 1 and the coverage statement of each file) are kept here. A DISCARD or LACKS row is a judgment about an existing artifact, not a task. No LACKS row passed the five-step test of `CLAUDE.md` §0 on its own: all stay design-level, reference only.

## Tags (carried by every claim; never upgraded)

`[V2 <url> <date>]` / `[V3 <url> <date>]` read in a fetched page body (the table pass and the tutorial pass); `[S2]` / `[S3]` search snippet only, page not opened; `[M]` memory, not re-checked; `?` not established; `[CONTESTED]` sources disagree. In `tutorials/`, `v2` means the capability tables and `v3` the tutorial pass; "v1" in the tables means the first-draft table this file replaced (not kept).

## Method and limits

- Eleven table agents and nineteen tutorial agents (Sonnet, high effort) wrote from pages they opened; fandom wikis blocked the fetch tool, so MediaWiki `api.php` / `action=raw`, Steam's news API, Wikipedia, public game-data mirrors and official manuals carried most of it. A shared search allowance ran out in several runs, so "latest patch" statements are not exhaustive.
- Thirteen Opus critics (Opus, high effort) compared each routed item with the Valoria tutorial, the code (read-only probes) and the I1 verification of Valoria's capability inventory.
- Wikis, guides and forums are folk models of closed systems: they are the right thing to compare for design shape and the wrong thing to trust for any specific constant. Every figure is version-stamped where a version was found.
- Games change. Dates in each file's facts line say what was read when.
- Not covered: tabletop titles other than Pax Pamir; Skyrim; the sections of the first-draft tables that made unverified claims about Valoria (dropped; the verified Valoria side is the I1 inventory and the dispositions).
- `dispositions/ATTACHMENTS_CROSSCHECK.md` and `dispositions/repo_claims_checked.md` record what four uploaded survey documents (not in the repo) and the repo's own precedent claims said, against the verified tables.

## The capability checklist (ids used in `tables/` and the tutorials' capability lines)

A character & agency (A1 control a character, A2 creation, A3 progression, A4 inventory, A5 companions) · B roster & personnel (B1 manage roster, B2 recruit/dismiss, B3 appoint, B4 assign duties, B5 standing orders, B6 loyalty/morale, B7 succession) · C settlement & territory (C1 found/claim, C2 build, C3 upgrade/repair, C4 zoning, C5 production chains, C6 logistics, C7 garrison) · D policy & governance (D1 laws, D2 taxes/budgets, D3 council, D4 legitimacy/unrest, D5 votes, D6 justice) · E economy (E1 stockpiles, E2 markets, E3 trade routes, E4 currency/debt, E5 crafting, E6 upkeep) · F mass military (F1 raise/disband, F2 compose armies, F3 deployment, F4 in-battle control, F5 auto-resolve, F6 sieges, F7 supply, F8 morale/rout) · G personal combat (G1 control, G2 weapon depth, G3 injury/death, G4 duels, G5 stealth) · H social & diplomacy (H1 dialogue, H2 opinion, H3 schemes, H4 marriage/alliances, H5 hostages/tribute, H6 war/peace) · I information (I1 clues, I2 deduction, I3 rumour, I4 espionage, I5 deception, I6 fog) · J special systems (J1 powers with cost, J2 religion, J3 corruption/sanity) · K world & survival (K1 overland, K2 terrain/weather, K3 hunger/disease, K4 exploration, K5 rest) · L NPC life (L1 persistent personality, L2 ageing/death, L3 families, L4 emergent stories, L5 NPC autonomy) · M meta (M1 ending, M2 authored scenarios, M3 persistent consequences, M4 legibility, M5 zoom).

## Index of games

Tables: R1 CK3, Victoria 3, Old World, Pathfinder: Kingmaker · R2 Bannerlord, Warband, Battle Brothers, Kenshi · R3a Dwarf Fortress, RimWorld, Songs of Syx · R3b Manor Lords, Frostpunk 1/2, Banished · R4 Disco Elysium, Griftlands, Baldur's Gate 3, Kingdom Come: Deliverance · R5 Obra Dinn, Shadows of Doubt, Pentiment, L.A. Noire (+ Disco, CK3 espionage) · R6 Total War, Field of Glory II, Ultimate General, Hearts of Iron IV · R7 Darkest Dungeon II, Sunless Sea, Eternal Darkness, Don't Starve, Pathologic 2, Bloodlines · R8 The Sims 4, Anno 1800, Patrician IV, Wildermyth · R9 Tropico 6, Suzerain, Dragon Age: Inquisition, Democracy 4.
Tutorials: T01 realm (CK3, Vic3, Old World, Kingmaker) · T02 warband (Bannerlord, Warband, Battle Brothers, Kenshi) · T03 DF, RimWorld, Songs of Syx · T04 Manor Lords, Frostpunk 1/2, Banished · T05 Disco, Griftlands, BG3, KCD · T06 Obra Dinn, Shadows of Doubt, Pentiment, L.A. Noire · T07 Total War, FoG II, Ultimate General, HOI4 · T08 Darkest Dungeon II, Sunless Sea, Eternal Darkness · T09 Don't Starve, Pathologic 2, Bloodlines · T10 Sims 4, Anno 1800, Patrician IV, Wildermyth · T11 Tropico 6, Suzerain, DAI, Democracy 4 · T12 CK2, Imperator, Rome II, Oriental Empires · T13 RTK, Nobunaga, Genghis Khan II, Knights of Honor II · T14 Jagged Alliance 2, Medieval Dynasty, Dawn of Man, The Guild 2/3 · T15 Against the Storm, Pax Pamir, Empires in Arms, Nemesis (Shadow of Mordor/War) · T16 Football Manager, Caves of Qud, King of Dragon Pass / Six Ages · T17 EU4, Dominions 5/6, Heroes of Might and Magic · T18 Shadow Empire, Stellaris, XCOM, Brigandine · T19 Triangle Strategy, Unicorn Overlord, Ace Attorney, Lacuna.
