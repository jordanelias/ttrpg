# 27 · Mass battle: command, a unit's own prowess, and an army whose strength is where it stands

## Status: REFERENCE (a design adjudication serving ruling A-59; resolves nothing at runtime, CLAUDE.md §0.05; queues nothing)

## Read at: `faf0cea` (working tree, 2026-11-12)

Jordan's ruling A-59 (`unified/DECISIONS_ANSWERED.md:73`), verbatim: *"B, and order friction is a function of
'command' which itself comes from a combination of learned skill/faculty and a function of social/mental
attributes.... but also, each unit within subformation will have its own martial prowess based upon quality
of troops and equipment and all impacted by subformation with tactics, and the overall army prowess as a
grand formation of these units is dynamic so a static fighting value is misleading as the overall placement
of units and their instructions relative to opponent is critical"*. B is option (b) of
`audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md` §7 item 2: lower the day's luck once order friction exists.

## 0. Verdict

**The ruling can be served by edits at owners that already exist, and the engine is closer to it than its
own surface suggests: strength is already computed per unit, per pair and per contact cell from placement,
facing, depth, stance, fatigue and morale; what contradicts A-59 is three things laid over that machinery,
and each is small.** (1) One number drawn before contact multiplies every pool on a side for the whole day
(`core/exchange.py:147`, set at `orchestration.py:1725-1736`, drawn at `battle_loop.py:51-52`): at log-SD
1.1 a side the ratio of the two sides' draws moves by a factor of about 4.7 at one standard deviation
(`audits/04_MB_audit.md` F-MB-08), so it is the static side-wide value the ruling calls misleading, and it
is larger than anything placement or orders can do. (2) A fired order is applied by `setattr` with certainty
(`core/contact.py:130-162`), so there is no order friction for command to be a function of. (3) The season
hands every unit the same three literals, power 4, command 4, discipline 5 (`orderofbattle.py:75`,
`massbattle.py:184-188`), so no unit has its own prowess and no commander has command. The plan in the four
`proposals/27_MB_*.md` files: command becomes one capability row with two inputs (trained score, and talent
on a social and a mental attribute) read by the one pool reader and carried on the typed input; an order
takes effect through one obedience draw whose obstacle rises with distance from the issuer and falls with a
prearranged signal; a unit's pool is composed from columns of its own row (troop quality, arm in hand,
armour, experience, subformation) by the one closed form the engine already has; the side-wide multiplier
is shipped at **zero** behind a three-arm test (1.1, 0.55, 0) whose controls can tell removal from lowering,
with a small named per-side level kept only if the test's stated criterion calls for it. Nothing here adds a
resolver, a second ladder or a guard. One item survives the ladder for Jordan (§9): whether an officer's
command reaches his unit's fighting through its steadiness only (decided here) or also through its dice.

**Vocabulary** (the suite's, `proposals/04_MB_cell_hierarchy_as_data.md` §1): at the designer's surface
**army, unit, subformation, troops**; in code `Unit` (a side's army), `Subunit` (a unit), the subunit's
footprint, the cell. This file uses the designer's words and names the code object where it cites code.

## 1. What the code does today, opened at `faf0cea`

### 1.1 Where strength is read (the terms that are already dynamic)

