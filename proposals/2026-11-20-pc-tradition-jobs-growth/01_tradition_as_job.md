# Part 1 — What a tradition is, as a job

## Status: PROPOSED. Reference only (CLAUDE.md §0.05): nothing here is a mechanism until code reads it. Words are defined in `00_head.md`.

## 1.1 What the engine already does with a tradition (verified by reading the code, 2026-11-20)

| fact | where | what it means for a job design |
|---|---|---|
| A tradition is a name plus a kit; it carries no weights | `modules/combat/traditions.py:13-24` (`set`, `mode` are "read by nothing as weights"); `traditions.py:35-37` ("no imposition gate or per-tradition preferred node") | a job may not carry a multiplier of its own (ED-PC-0023). Everything a job does must pass through techniques |
| The tradition gates which techniques count; an untaught technique is silently inert | `ability_primitives.py:156-182` (`_invested`: allowed = union of the kits of `known_traditions`, else of `tradition`) | cross-training already exists in the code as `known_traditions`; nothing sets it today |
| A technique acts through one **lever** (a read site in the bout), as a factor (`value ** level`) or a bonus (`value * level`) | `ability_primitives.py:185-207`; lever sites in `combat_systems.py` (e.g. `:787-789` measure, `:932-942` bind, `:1004` read, `:1029` counter choice) and `contact.py:45` | a technique's power is its level, never its tradition |
| Fifteen levers are live | `ability_primitives.py:18-26`; the B18.02 lever family lists the same fifteen (workplan v12 B18.02, copied in the scratchpad `b18.md:82`) | a job's content can only land on these fifteen until a new lever is built |
| Levels are clamped to 0..8 and the composed factor to [1e-4, 1e3] | `ability_primitives.py:151-153`, `:182`, `:207` | eight levels is the ladder's height |
| The tradition name is also read by familiarity: how well one school reads another (1.0 same, 0.93 neighbour, 0.85 other; 1.0 whenever either side is `none`) | `traditions.py:26-48`; read at `combat_systems.py:936,938,990,1002` | the one place a tradition acts without a technique. Note: a `none` fighter reads and is read at 1.0, so having no school costs no familiarity |
| The 21 GENERIC calibration techniques are tagged to traditions by a Latin square (three each, including Chinese and Filipino) | `ability_primitives.py:75-129` | Chinese and Filipino are not empty in the engine: each has three generics; they have no *named* technique |
| The fight receives `traditions`, `techniques`, `axes`, `dispositions` per party; the season fills none | `engine/season/queries/inputs.py:184-206`; `modules/combat/fight.py:58-63,182-185` | the door exists. B18.02 (workplan v12) turns it into numbers per slot and moves the kits and the gate host-side |
| Nothing in a season raises a technique level, and no fight forms in a computed season | `engine/season/hole_register.yaml` H-264 (`fight` formed 0 times in about 3,500 opening sets); H-350 (every person fights as `('arming','light')`) | every job design here is a design for the standalone duel first, and for the season only when a fight forms |

## 1.2 What the reference games call a job (tags carried from the research sheets)

- **Final Fantasy Tactics / Bravely Default (shared job pool).** Any unit can take any job; a job carries stats, equipment access and its command list; abilities learned in one job can be carried into another as a secondary command set or as support. Bravely Default: 24 jobs, job level cap 14, one new ability per job level, JP only to the current job, one secondary job's commands carried, support abilities from any job within a cost limit that grows 1→5 by story [V: Gamerguides B2, B4; Wikipedia B1, in `tactics_ogre_bravely_default.md` §2.1–2.4].
- **Tactics Ogre (class change gated by items and identity).** PSP: classes, not units, level up; a new class starts at level 1; skills carry across, class-specific ones do not [V: S11, S13]. Reborn: unit levels return, class change keeps the level, a Classmark item buys the change, race gates the class list, four skill slots [V: S1, S3, S4, S8]. Original: alignment fixed per unit and gates the class list; a kill count gates Terror Knight and Angel Knight [V: S17, 1998 fan FAQ].
- **Triangle Strategy (bespoke per-character line).** Every unit has one fixed class line of three ranks, no switching; promotions at level 10 + Medal of Bravery and level 20 + Medal of Valor; one fixed weapon with its own upgrade tree, either/or nodes, swappable once unlocked [V: S3, S4, S5, S7, S10 in `triangle_strategy.md` §1–4]. Critics praised that "characters don't step on each other's toes" [V: S3] and objected to "linear" progression and lost hybrid builds [V: S4, S6, S7].
- **Troubleshooter: Abandoned Children (classes plus a mastery board).** Three classes per character (one basic, two advanced; advanced at character level 15); class level cap 16 with class masteries at class levels 1/4/8/12/16; classes switch freely between missions; class masteries stay with the class, learned active abilities carry across [FAN: TroubleMaster data; Steam thread /0/2269195350128982410, in `troubleshooter_characters.md` §2]. Part 6 studies it in detail.

## 1.3 Four variants of "a tradition is a job"

Each is judged on the same axes. "Generated person" means a person the season builds, not one Jordan authored.

| axis | **A. Shared ladder** | **B. Job-swap with a carried secondary** (Bravely Default shape) | **C. Bespoke per-character path** (Triangle Strategy shape) | **D. Shared curriculum, personal path** (recommended) |
|---|---|---|---|---|
| what a tradition teaches | one ordered list of techniques, the same for every member | a command list per tradition; the active one is fully usable, one other is carried | an individual line per notable person, written from their history | one curriculum per tradition (techniques in short lines, with prerequisites); every member may walk any of it |
| how a person advances | levels in the next technique on the ladder, in order | levels only in the active tradition; swap between fights | down their own line, in its order | down their own **path**: an ordered list of curriculum entries, authored for notables, generated from the lifepath for everyone else |
| shared vs bespoke | all shared | all shared; the choice of pair is personal | all bespoke | the curriculum is shared; the order, the teacher and at most one personal set are bespoke |
| identity in a fight | the tradition | whichever tradition is active today | the person | the primary tradition (fixed by history) plus what the person chose to bring |
| mixing | none, or a second ladder | built in: the carried secondary | none (Triangle Strategy allows none: [V: S5] "locked to their class paths") | a second tradition is learnable after a threshold in the first; its techniques sit on the same board |
| generated persons | trivial: everyone of a tradition is the same at a given rung | trivial, but every NPC must also be given a swap rule | impossible without authoring each one | a generator draws a path from the curriculum by lifepath; same schema as an authored path |
| "every build available" (fiat audit, 2026-07-23) | holds: anyone can join any tradition | holds | **breaks** for notables locked to one line, unless the line is only an ordering | holds: a path changes order and price, never what is reachable |
| no tradition weight (ED-PC-0023) | holds | holds, but "active tradition" invites a per-tradition bonus to make the swap matter | holds | holds |
| what the engine must change | nothing beyond B18.02 | the `tradition` name must become per-fight state; familiarity reads the active name, so a swap changes how opponents read you | nothing beyond B18.02 | nothing beyond B18.02 |
| the season's new state | tradition, technique levels | tradition set, active tradition, technique levels | technique levels; the line is static data | primary tradition, any second tradition, technique levels, path; Part 5 sizes it |
| first falsifier | two members of one tradition at equal levels are distinguishable only by kit and stats (the ladder made them the same) | a swap whose fight differs from a non-swap only through familiarity (the swap carried no decision) | a generated person with no line | a notable and a generated person on the same curriculum with the same levels fight byte-identically (the path is only bookkeeping, as it should be at fight time) |

## 1.4 The four, as proposals

### J-A. The shared ladder

- **What it is.** A tradition is one ordered list. A member raises the next technique; the list order is the curriculum.
- **N-line.** Cut it and the tradition remains a bag of techniques with no order, which is today. What it adds is the order alone.
- **Runtime change in `engine/season/`.** A carrier for tradition and technique levels (Part 5) and a composer that fills `techniques`. Nothing else.
- **Falsifier.** Two members at the same rung, same weapon and same stats produce identical slot numbers; if a player cannot tell two German fighters apart except by weapon, the ladder has erased the build choice the fiat audit asks for ("each combatant should have their own feel, emergent from their full stack", `.audit/2026-07-23-combat-fiat-audit/fiat_audit_v1.md`, as quoted in `proposals/2026-11-10-personal-combat-tradition-sets/00_tradition_sets.md:25`).
- **Build order and gates.** (1) curriculum data host-side (after B18.02); (2) carrier; (3) composer. Gate at each: B18.02's hash gate EQUAL (an empty board changes nothing).
- **Hash movers.** None until a person who fights has a level above 0. In a computed season no fight forms (H-264), so the season hash stays EQUAL [UNVERIFIED: not run here]; the standalone duel moves.
- **Cost.** Lowest of the four.
- **Decision it leaves Jordan.** Whether the order of a curriculum is content (his) or design (this proposal's).
- **Lessons.** Tactics Ogre PSP's class-wide level made "never a point where one unit can be the dominate force" and drew criticism as the "2nd most problematic aspect" [V: S13; FAN: S16]; Reborn reverted to unit levels on fan feedback [V: S4, S5]. A ladder shared too tightly erases the person.

### J-B. Job-swap with a carried secondary (Bravely Default)

- **What it is.** A person knows several traditions; before a fight one is *active* (its techniques fully usable, its name read by familiarity) and one other is *carried* (its techniques usable on the board). Swap between fights.
- **N-line.** Cut it and a fighter with two schools fights with both at once (`known_traditions` already unions the kits, `ability_primitives.py:174-177`). What the swap adds is a choice of which school an opponent sees.
- **Runtime change in `engine/season/`.** An `active` field per person; a decision point before each fight; the season's NPC deciders need a rule to pick it.
- **Falsifier.** If, over paired seeds, a swapped fighter's fights differ from the unswapped one's only through the familiarity term, the swap is a label change, not a decision.
- **Build order and gates.** As J-A, plus the active field and its decider. The decider is new apparatus with no current reader.
- **Hash movers.** As J-A.
- **Cost.** Medium: a per-fight decision and an NPC rule.
- **Decision it leaves Jordan.** Whether presenting a different school to an opponent is a thing Valoria's fighters do. History offers fighters trained in more than one school; it offers no source for "choosing which school an opponent reads".
- **Lessons.** Bravely Default's mixing "begs players to experiment" [V: B12], but the job system "necessitated grinding to unlock its full value" [V: B1, GameTrailers] because JP goes only to the current job [V: B2]. Its support-cost limit (1 rising to 5, any job's support abilities) [V: B2, B4] is the useful part and reappears in Part 2 as the board budget, without the swap.

### J-C. Bespoke per-character path (Triangle Strategy)

- **What it is.** Each notable person has one individual line through a tradition, written from their history; no one else walks it.
- **N-line.** Cut it and notable persons are generic members of their school. What it adds is authored identity.
- **Runtime change in `engine/season/`.** Per-person line data and the carrier.
- **Falsifier.** A generated person has no line, so either they fight at level 0 forever or a second system grows them: two systems for one quantity, an S defect (CLAUDE.md §0.06, "calculations consistent in methodology").
- **Build order and gates.** As J-A, with an authored line per notable as content.
- **Hash movers.** As J-A.
- **Cost.** High in content: one line per notable, and nothing for anyone else.
- **Decision it leaves Jordan.** None it can settle: as stated, it breaks "every build available" for notables locked to one line (fiat audit) and has no answer for generated persons.
- **Lessons.** Triangle Strategy's own producer chose fixed lines for legibility ("easy to understand and the same for the characters and the setting") [SNIPPET: N6]; reviewers praised distinct roles [V: S3, S5, S7] and missed hybrid builds and branching [V: S4, S6, S7]. What survives into J-D: a person's line is an *ordering and a price*, not a wall; Triangle Strategy's either/or nodes, swappable once unlocked [V: S3], survive as the board.

### J-D. Shared curriculum, personal path (RECOMMENDED)

- **What it is.** Three pieces of data, one rule.
  1. A **curriculum** per tradition: its techniques grouped into short **lines** (2–4 techniques that build on each other, e.g. a bind line, a counter line, a grappling line), each technique with its prerequisites (`requires`, Part 3). Shared by every member.
  2. A **path** per person: the ordered list of curriculum entries they have learned or will learn next, with the teacher or event each came from. For a notable person Jordan writes it; for a generated person a generator draws it from the curriculum, weighted by the lifepath (B18.05 gives martial lifepaths an `arms` key; the same lifepath picks the lines). Same schema either way, so no special case.
  3. At most one **personal set** per notable person: a named group of existing techniques that the person's history already put together, unlocking one behaviour (Part 3's set rule). Anyone else can assemble the same techniques the slow way; only the name and the head start are personal. This is how Triangle Strategy's bespoke identity coexists with "every build available": the *effect* is available to all, the *route* is personal.
  - **The rule:** a person's **primary tradition** is fixed by their history (it sets familiarity and the fixed baseline, Part 2). A **second tradition** becomes learnable once the person holds a stated number of techniques at a stated level in the first (Pathfinder's "two feats before a second dedication" throttle, carried in the brief §2 from this session's earlier comparison). There is no swap.
- **N-line.** Cut the curriculum and techniques have no order or prerequisites (today). Cut the path and notables and generated persons need two growth systems (J-C's defect). Cut the personal set and notables lose authored identity at no cost to anyone else. Each piece fails a different test when removed.
- **Runtime change in `engine/season/`.** A carrier holding primary tradition, second tradition (optional), technique levels and path position (Part 5 gives the smallest first increment); a host-side composer that reads the person and fills the four `PersonalCombatInput` fields (after B18.02, numbers per slot). The module changes nothing.
- **Falsifier.** (1) A notable and a generated person with the same tradition, the same technique levels, the same board and the same kit fight byte-identically over paired seeds: the path must be bookkeeping at fight time, never a hidden modifier. (2) A person whose path is empty fights byte-identically to today's default fighter. Both are runnable on the module the day the composer exists.
- **Build order, with gates.** (1) B18.02 lands (the slot interface); gate: its own, hash EQUAL. (2) Curriculum data for the anchored traditions, host-side, read by nothing yet; gate: the export round-trip `--check` if it is exported. (3) The carrier, first increment (Part 5); gate: seed-2 one-season hash EQUAL while no generated path is drawn. (4) The path generator at realm build; gate: MOVER(build) declared, recorded. (5) The composer fills the fields; gate: falsifiers (1) and (2) above as tests.
- **Hash movers.** Steps 1–3: EQUAL. Step 4 moves the build hash (new per-person data). Step 5 moves a fight's outcome only where a person with techniques fights; in a computed season none does (H-264), so the season hash should stay EQUAL until a fight forms [UNVERIFIED: not run].
- **Cost.** Medium: three small data schemas, one generator, one composer. The content cost is Jordan's and is the same for every variant.
- **Decision it leaves Jordan.** The throttle on a second tradition (how many techniques at what level), and whether notables get a personal set at all. Both are in Part 9.
- **Lessons, with tags.** Troubleshooter: three classes per character, of which the *advanced* two are gated by character level 15 and the character's own roster, while learned abilities carry across classes [FAN: TroubleMaster data; Steam thread /0/2269195350128982410] — a personal route through shared classes, which is J-D's shape. Its per-character "Individual"/personal masteries, about three per playable character, carrying the character's portrait [FAN: TroubleMaster data; V: user screenshot, `screenshot_mastery_board_irene.md` lines 20, 29] are the personal set. Final Fantasy Tactics' secondary skillset (brief §2, verified this session) and Bravely Default's carried secondary [V: B2] are the second tradition, without the swap.

## 1.5 Ranking

1. **J-D, shared curriculum with personal path** — the only variant that keeps the fiat audit's "every build available", serves generated persons and notables by one schema, and needs no module change.
2. **J-A, shared ladder** — J-D with the path and the personal set removed; the right *first increment* if Jordan wants the smallest build (Part 5).
3. **J-B, job-swap** — adds a per-fight decision with no historical ground and an NPC rule; its useful part (the carried secondary, the support budget) is taken into J-D and Part 2 without the swap.
4. **J-C, bespoke line alone** — breaks "every build available" for notables and leaves generated persons with no growth.
