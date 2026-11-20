# Part 6 — Troubleshooter: Abandoned Children, in detail

## Status: PROPOSED. Reference only. Tags are carried from the research sheets in the session scratchpad (`research/` and `research/steam/`): **[V]** read on a page or image; **[FAN]** a fan site, forum or fan data extract (the TroubleMaster planner parses the game's own data files but is one unofficial source); **[SNIPPET]** a search summary only; **[UNVERIFIED]** a count or reading the research agent itself flagged. Sheet names below are short for files under `/tmp/claude-0/-home-user-ttrpg/ca7d06d5-bb15-5e33-a7a2-8cba108a73a8/scratchpad/research/`.

## 6.1 The game

A turn-based tactics game by Dandylion, released in full on Steam on 23 April 2020; "Very Positive, 92% of 3,429 English reviews" when fetched on 2026-11-20 [V: Steam, `troubleshooter_combat_reception.md:13`]. Twelve playable characters [FAN: TroubleMaster, `troubleshooter_characters.md:21-36`]. The store page claims "over 1,000 masteries plus more than 500 additional" [V: Steam].

## 6.2 Its systems, as facts

**Turn economy.** Two actions per turn, a move and a full action [V: Turn Based Lovers]. Turn order runs on Action Time: a fan guide derives AT = 36 × (0.5 + 100 / Speed) + the cast delay of the moves used, floored at 36 during one's own turn [FAN: gameplay.tips, `troubleshooter_combat_reception.md:37-46`]. Masteries that cut Action Time on a kill, a block or a dodge are pervasive (Executioner −15 per kill, Bloodbath −30, Sword of Protection −20 when blocking) [FAN, same guide]. Players name speed and AT reduction as the main power axis: "well-built characters can act 2 to 5 times for each enemy turn" [FAN: Steam thread, `troubleshooter_combat_reception.md:92`].

**Classes (the jobs).** Each character has three classes: one basic and two advanced, advanced from character level 15; a class levels to 16 and grants one class mastery at class levels 1, 4, 8, 12 and 16 [FAN: TroubleMaster data, checked on 37 character-class pairs; Steam thread, `troubleshooter_characters.md:44-64`]. Classes switch freely between missions; "Masteries unlocked in one class are usable only in that class, but unlocked abilities/skills are shared across classes" [FAN: Steam thread, two posters, `troubleshooter_characters.md:47`].

**Where active abilities come from (the brief's open point, settled).** From three sources: the class or character, equipped gear (a Spray grants Shaking Shot), and some masteries ("grantedBy", e.g. Call of Wind grants Air Blast) [FAN: TroubleMaster data, `troubleshooter_characters.md:81`]. Most masteries are not abilities. Of 808 transcribed tooltips, a keyword classification puts about 139 as granting an ability, a behaviour, an immunity or capacity, about 190 as modifying another ability or applying a status, and 479 as number-only [UNVERIFIED regex counts; examples V: `steam/guide_2037290423.md` §5, lines 976-990]. **So "mastery = skill" is wrong as a general equation; a mastery is usually a modifier and sometimes an access gate** (the user's Addendum 4 point: Overwatch "The character acquires Overwatch ability"; Iron Wall; Serial Shot [V: `steam/guide_2037290423.md` §4c item 49]).

**The board.** Five columns, Basic, Attack, Ability, Support and Defence, plus a Mastery Set area [V: user screenshot, `steam/screenshot_mastery_board_irene.md:8-20`]. Three limits run at once:
- **slots per column**, opened by character level on a schedule (Basic at levels 1, 6, 11, 16, 22, 32, 42, 52 and so on) [FAN: TroubleMaster data, `troubleshooter_characters.md:99`];
- **a cost cap per column** ("property limit"); a mastery that opens a slot raises that column's cap by 2, and six masteries raise every cap by 1 [V: tooltips, `steam/guide_2037290423.md:1001-1003`]; the fan formula cap = 2 × slots − 1 holds exactly on 10 of 39 guide boards (residuals 0, 1, 2 and 4 over 195 column readings) and the same character at the same maximum shows different caps on different boards [V: 39 boards read, `steam/guide_1349483727_images.md:743-749`];
- **a total Training Point pool** equal to character level plus 0, 2 or 3, never below the level, the source of the extra not shown [V: 26 character sheets, `steam/guide_1349483727_images.md:751-781`]; one mastery adds 3 to the maximum and three add 3 to the "maximum mastery point" [V: tooltips].
- On the user's own board the five columns spend 8 + 7 + 7 + 7 + 9 = 38 of 38 points while the caps sum to 47: **the pool binds first; the caps shape the spread** [V: arithmetic on the screenshot].
- **The column tag does not match the effect:** "A Strategic Retreat is BASIC but opens a DEFENSE slot; Hard Bone is ABILITY but opens a BASIC slot" [V: `steam/guide_2037290423.md:994`].

**Costs.** 1 to 4 on the user's board [V]; among 725 transcribed mastery costs, 0: 12, 1: 190, 2: 372, 3: 141, 4: 10 [UNVERIFIED parse]. A mastery cannot be levelled, and duplicates cannot be equipped [FAN: Steam thread `/0/5296777170378528709`].

**Fixed masteries.** "Every unit in the game has at least 5 innate masteries that cannot be unequipped know as Fixed Masteries" [V: Fandom, `steam/fandom_masteries.md:19`]; these include company masteries and each element's base rule [V: same file `:46-55`, `:492`]. The TroubleMaster data lists character-fixed masteries for Leton only [FAN: `troubleshooter_characters.md:38`]; the two count different things.

**Sets.** "Mastery Sets are unique masteries that are automatically equipped when a specific combination of masteries are equipped" [V: Fandom Mastery Sets, `steam/fandom_wiki.md:19`]. 179 of 181 Fandom recipes are exactly four masteries, filed under class and element headings [V: `steam/fandom_wiki.md:27-30`]; the TroubleMaster data counts 611 sets, 602 of four and 9 of three [FAN]. Members come from different columns (Bloodbath = Hemorrhage + Bloodshed + Blood Scent + Blood Thirst) [V: `steam/fandom_wiki.md:1090`]. **A set's effect both reshapes its members and adds a flat bonus** [V: `:1091`], and many force an outcome: "Bladestorm: Attacks activated by Bladestorm will always hit (100% hit)"; "Forestallment is always a critical hit"; "If your health is below 33%, defend against all attacks" [V: `:1102-1107`]. Recipes are hidden until discovered: "not shown anywhere until you discover them" [V: RPG Codex thread, `troubleshooter_combat_reception.md:98`]; one save shows "Acquired Mastery Set 481/481" [V: image, `steam/guide_1349483727_images.md:149`].

**Lending a property across jobs.** Cheerful, Delicate, Fancy and Powerful Move: "if the holder is not a Dancer or Superstar, that Dance type is added to an ability at positions a multiple of 3/2/4/1" [V: tooltips, `steam/guide_2037290423.md:960`]. A class behaviour reaches a non-member by a rule on the board.

**Acquisition and changing a board.** Masteries drop from defeated enemies (drop chance raisable by +50%), are researched (crafted) from other masteries, granted at class levels, and given by story choices and achievements [FAN: Steam threads; steamah, `troubleshooter_characters.md:93`]. Unequipping costs a consumable: "Training manual: Item that consumed when unequipping Mastery in Mastery Board" [V: tooltip in image, `steam/guide_1349483727_images.md:137`]. "You may save 3 preset mastery boards for each character, with additional pages unlockable with coins" [V: Fandom, `steam/fandom_masteries.md:29`].

**Personal masteries and sets.** About three personal masteries per playable character, shown with the character's portrait [FAN: TroubleMaster owner counts; V: user screenshot, `steam/screenshot_mastery_board_irene.md:20,29`]; personal sets exist ("Repetitive Training D D fist Irene-portrait; I Am the Hero Irene! 4 Irene portraits") [V: image, `steam/guide_1349483727_images.md:789`].

## 6.3 What players and reviewers said

| | quote or finding | tag |
|---|---|---|
| praise | "most of its build combinations viable even on its hardest difficulties" | [V: RPG Codex review, `troubleshooter_combat_reception.md:89`] |
| praise | "The Mastery system in this game is one of the best build systems ever devised by any developers, anywhere" | [FAN: Steam T66, `steam/discussions_builds.md:305`] |
| praise | players "can make most characters fill other roles, such as turning the healer into a tank" | [V: RPG Codex forum, `troubleshooter_combat_reception.md:97`] |
| complaint | grind: "intensely grindy"; "definitely some grinding" | [V: RPG Codex; RPG Fan, `troubleshooter_combat_reception.md:113`] |
| complaint | 800+ choices "dizzying"; the mastery UI "clunky and not always instinctive"; the reviewer "couldn't tell if newer masteries beat older" | [V: RPG Fan, same line] |
| complaint | "Picking from 30 options is fun, picking from 130…" | [FAN: Steam, `steam/discussions_builds.md:244`] |
| complaint | hidden sets: a player "Doesn't want to permutate 500+ combinations and lacks training manuals" | [FAN: `steam/discussions_builds.md:165`] |
| complaint | "pulling one mastery can break other synergies so players often restart a build"; "real issue is discarding the whole build to switch approaches" | [V: RPG Codex thread, `troubleshooter_combat_reception.md:97`; FAN: `steam/discussions_builds.md:228`] |
| dispute | Training Manuals: "So far I have seen literally nobody who liked Training Manuals"; "it encourages guide building instead of experimentation"; against: "Weight lends credence to the choices you make"; the developer: "unrestricted freedom is like a cheat key" | [FAN; developer statement on the forum, `steam/discussions_builds.md:306-308`] |
| complaint | category limits called "arbitrary" | [V: one blogger, `troubleshooter_combat_reception.md:99`] |
| finding | "with meta builds the game is easy, even on the highest difficulty"; speed and AT reduction the most-cited power lever | [FAN, `troubleshooter_combat_reception.md:88,115`] |
| dispute | role identity: "Albus is worse in all roles than his teammates" against defenders of his builds | [FAN: `steam/discussions_builds.md:389`] |

## 6.4 Point-by-point transfer to Valoria

| Troubleshooter fact | verdict | reason |
|---|---|---|
| masteries as the main build system, separate from the class | **transfers** | the board is a layer beside the tradition, exactly as masteries sit beside the class |
| a mastery is usually a modifier, sometimes an access gate, sometimes a rule over other masteries | **transfers**, as the three kinds of Part 2 §2.2 | the live engine has the first (levers); the second maps onto gates it already rolls; the third is host-side |
| five columns that are budget buckets, tag ≠ effect | **transfers with change**: columns by phase of the bout, derived from the engine site | a bucket whose name lies about its content is legible only after learning the exceptions; a derived column cannot lie |
| three limits: slots, per-column cap, total pool | **transfers with change**: two limits (slots, attention) | the user's own board shows the pool binding before the caps; in Valoria slots already shape the spread |
| total pool = character level + 0/2/3 | **does not transfer** as written | Valoria has no character level; the pool's role (a capacity that grows with experience) is taken by attention from Concentration (PC-22) |
| costs 0–4 per mastery, fixed | **transfers with change**: cost by kind, falling when drilled | Valoria's techniques have levels; a mastered technique taking less attention is the one honest use of the level in the budget |
| masteries cannot be levelled | **does not transfer** | Valoria's levels are the live model (ED-PC-0024) and the only thing that carries efficacy |
| fixed masteries that cannot be unequipped | **transfers** as the fixed baseline | a pinned foundation plus a chosen layer is legible and costs no new rule |
| sets: four named masteries, automatic | **transfers** | the shape the user named; n-ary is what pairwise relations lacked |
| set effects: flat stat bonus plus reshaped members | **does not transfer** | a set filed under a tradition that adds magnitude is a tradition weight (ED-PC-0023) |
| set effects that force an outcome (always hit, always crit, defend against all) | **does not transfer** | fiat: it sets a probability or bypasses a contest (agency proposal §5.1 rule 2; Class A) |
| set effects that change a behaviour or open a state (Bloodbath restores action points on a kill; Skilled Hunt changes what Chase is) | **transfers with change**: a set opens one gate | the Valoria form of "behaviour, not number" |
| recipes hidden until discovered | **does not transfer** | players report permutation and guide-reading; a visible goal is the legible one |
| hundreds of recipes | **does not transfer** | a ceiling of three per tradition (Part 3 §3.3 rule 5) |
| Dance lent to a non-dancer by a board rule | **transfers** as the board-rule kind | a cross-tradition lend that never touches the engine |
| class levels unlocking class masteries at 1/4/8/12/16 | **transfers with change** as `requires` levels down a line | a curriculum with prerequisites is the same shape |
| learned abilities carry across classes; class masteries stay | **transfers** as mixing (Part 3 §3.6) | a second tradition lends its techniques, not its foundation |
| class switch between missions | **does not transfer** | Valoria's tradition is history, not a costume (Part 1, J-B ranked third) |
| three saved boards per character | **transfers** | cheap, legible, and gives NPCs authored variety |
| Training Manuals to unequip | **does not transfer** | Valoria prices preparation by notice (challenge versus ambush), not by a consumable |
| drops from defeated enemies; research | **does not transfer** | technique from defeating someone is growth by fighting, against the 2026-11-07 ruling |
| story and achievement masteries | **transfers** as story events teaching a technique | Part 4 §4.2 item 4 |
| personal masteries and personal sets with the portrait | **transfers with change** as the personal set of the bespoke path | the effect stays reachable by anyone holding the members |
| Action Time and AT-reduction stacking as the dominant axis | **does not transfer**; a warning | Valoria's tempo is already a lever (`tempo`) and a lever that compounds on turn order is the shape of a dominant build; the one-technique-per-lever rule (Part 2) is the cheap guard against it |
| EXP-boost masteries (Learning, Understanding, Insight) | **does not transfer** | there is no experience currency to boost |
| per-character element (SP type) adding a slot to one column | **does not transfer** | no element; the personal set carries individuality instead |
| grid, cover, height | **does not transfer** | the duel is two parties on a continuous measure axis (agency proposal §21 A.3: "zone-based, no maps or grids"). `grep -n grid modules/combat/*.py` finds calibration grids in `config.py` and one mention of "the grid mode's suspension" at `wrapper.py:541`, no spatial grid. A grid of named characters is a mass-battle proposal (`proposals/2026-11-12-subsystem-audit-suite/proposals/04_MB_squad_grid_of_named_characters.md`, not read) |
