# Grounding note: Mount & Blade II: Bannerlord — the encounter menu ("Attack" or "Send troops")

## Status: FILED — reference, not canon (CLAUDE.md §0.05) · tier 3 (`research/00_INDEX.md` §1) · resolves nothing at runtime
## Date: 2026-11-12 · Lane: IN (grounding lane for `proposals/2026-11-12-subsystem-audit-suite/`) · informs design, never settles it
## What changes in `engine/season/`: nothing.

**Why this note exists.** The tree marks the contact menu `[M]`: "Fight = play it yourself, send troops, or let
the game auto-resolve [M]" (`../tutorials/T02_warband.md:18`), and the suite carries it at that grade
(`audits/04_MB_audit.md:1349-1350`, `audits/04_MB_audit_addendum_B.md:77`,
`proposals/04_MB_playable_field_scenario.md:29-30`). This note records what could be read. **Only forum-grade
sources were reached; no first-party page.**

Tags as in `../README.md`.

## Sources

| key | source | read |
|---|---|---|
| ST1 | Steam Community discussion, Mount & Blade II: Bannerlord, thread of 2022-12-11 on using "send troops", `https://steamcommunity.com/app/261550/discussions/0/3712685279023308920` | body, 2026-11-12; players' posts (folk model) |
| ST2 | Steam Community discussion, same game, a bug thread, `https://steamcommunity.com/app/261550/discussions/0/2264689848039477418` | body, 2026-11-12; players' posts |
| WP-BL | `https://en.wikipedia.org/wiki/Mount_%26_Blade_II:_Bannerlord` (raw wikitext), Gameplay | body, 2026-11-12 |

Not reached: any TaleWorlds page (the tree records `taleworlds.com` News as 403, `../tables/R2_warband_sandbox.md:3`);
the Gamer Guides "Tactics" page was fetched and its body text on simulated battles was not located.

## What is established

| # | claim | tag |
|---|---|---|
| 1 | At contact a menu offers **Attack** and **Send Troops**: "The window on the left which usually has Attack and Send Troops options". | [V3 ST2 2026-11-12], one player's post |
| 2 | **Send Troops is the simulated battle**: players call it "auto resolve" and "Battle-Simulations (send troops)". | [V3 ST1 2026-11-12], players' posts |
| 3 | Players report that the simulated result differs from the fought one in kind: "Send Troops is pure RNG ... there's always a chance that someone will die"; "You get more prisoners with Send Troops, and you don't have any enemies getting away"; "There are Skill bonuses which will affect Battle-Simulations (send troops) which you won't get with actual Battles". | [V3 ST1], players' claims, untested |
| 4 | "battles being played out on battlefields that allow the player to personally engage in combat alongside their troops". | [V3 WP-BL 2026-11-12] |
| 5 | Wages: the tree already holds a page-read source: each day the game "pays wages (unpaid or unfed troops lose morale, then desert)" (`T02:17`, `[V3 B2]`, a Gamer Guides page updated 2022-12-21). `R2` row E6 marks wages `[M]`; `T02:17` is the stronger citation. | tree, V3 there |

## What this note does NOT establish

- **A three-way menu.** Two options are sourced (rows 1 and 2). `T02:18`'s third ("let the game auto-resolve"
  as distinct from "send troops") was not found; rows 1 and 2 suggest "send troops" *is* the automatic
  resolution, so the menu as sourced is two-way plus leaving. The brief's "command, join or auto-resolve" is
  not established as a menu: `?` for "join" as a separate option.
- That the simulation and the fought battle are one calculation. Row 3 is players saying they are not; it is
  folk evidence, not a measurement and not a developer statement. (`R2` F5 carries "simulated battles" at V2.)
- Any number, any current-patch behaviour.

## Bearing on the suite

The suite's "memory-grade for the three-way menu" becomes: Attack or Send Troops, forum-grade page read; the
third option not established. Its "Bannerlord's wages are memory-grade ... not relied on"
(`audits/07_SE_audit_addendum_B.md:237`, `proposals/07_SE_campaign_supply_and_muster.md:48`,
`audits/04_MB_audit.md:1349`) overlooks `T02:17`, which sources wages at page-read grade (row 5).
