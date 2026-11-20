# Part 2 — The tradition board: what a fighter brings to one fight

## Status: PROPOSED. Reference only. Nothing here is built. Words are defined in `00_head.md`.

## 2.1 Two layers on one fighter, named apart

| layer | what it holds | owner in the plan | how it reaches the fight |
|---|---|---|---|
| **loadout** (B18's word) | weapons and armour carried: a primary kit, a secondary weapon, the weapon in hand | workplan v12 B18.04–B18.09 (copied in scratchpad `b18.md:53-60,190-201`) | `PersonalCombatInput.kits` (`engine/season/queries/inputs.py:195`); after B18.09 the weapon in hand is round state (`DuelState.form`, B16's, not in the tree today: `grep -rn DuelState modules engine` finds nothing) |
| **tradition board** | the techniques this fighter brings to this fight | this proposal; PC-21/PC-08 if adopted | `PersonalCombatInput.techniques` and, after B18.02, the lever and axis slot families |

**How they compose: the board never names a weapon; the weapon decides which board entries can act.** This is already true in the engine. `spine_press` acts through `WP.spine(w)` (`combat_systems.py:942`), which is 0 for a double-edged or edgeless blade; `edge_read` through `WP.edge_lines(w)` (`:816`); `choke_control` through `choke_counterbalance` (`:817`), 0 for a compact weapon or a half-sword form. So when B18.09 lets a fighter switch from spear to sword mid-round, the board does not change; the entries that the new weapon in hand can carry start to act, and the others go quiet. No rule is written for it. The same holds for the half-sword switch, which stays a weapon-morphology gate (`affords_halfsword`, `combat_systems.py:742-752`) and is never a board entry (agency proposal §5 Class B: "Morphology gates are the weapon's, not the fighter's").

## 2.2 Three kinds of board entry, one vocabulary

The user's reading of Troubleshooter (brief Addendum 4) and the repo's earlier decomposition (`.designs/systems/combat/combat_engine_v1/reference/tradition_decomposition_v1.md`: ACCESS, BIAS, TENDENCY; archived, vocabulary only) describe the same ground with two word sets. This proposal keeps **one** set:

| kind (this proposal) | what it does | Troubleshooter example | decomposition word it replaces | where it lands in the fight's input (after B18.02) | module change needed |
|---|---|---|---|---|---|
| **modifier** | a value on one lever: a factor or a bonus, scaled by level | number-only masteries, about 479 of 808 by keyword [UNVERIFIED regex count, `guide_2037290423.md` §5] | BIAS and TENDENCY: a preference or propensity is a modifier on a *selection* lever (`counter_select` at `combat_systems.py:1029`; the proposed `guard_prior_*`) | the `lever` slot family (15 members, the live levers) | none |
| **access** | permission to attempt something the engine otherwise refuses, at a gate it already has | Overwatch "acquires Overwatch ability" (an out-of-turn reaction); Iron Wall (a stance); about 139 of 808 grant an ability or behaviour [UNVERIFIED regex, same §5; examples V, `guide_2037290423.md` §4c item 49] | ACCESS (kept) | **a new `gate` slot family**: one member per existing engine `if` that a trained fighter may widen; or, if player-facing, a member of the per-round choice set | yes: one read per gate (§2.3) |
| **board rule** | changes how *other* entries compose, before the fight: lends a property, raises a slot or the budget, counts a technique as taught | Cheerful/Fancy/Powerful Move lend Dance to a non-dancer's abilities; A Strategic Retreat opens a Defence slot; Honesty raises the point maximum (V, `guide_2037290423.md` §4e items 59–65) | none (new) | **none: it never reaches the module**; the host composes it away | none |

- **Why BIAS and TENDENCY are not kinds of their own.** In the live engine a preference is a factor on a choice probability (the counter's reach, `combat_systems.py:1029`, already multiplies `ability_factor(defender, 'counter_select')`). A preferred node *set by label* is the retired imposition gate (`traditions.py:35-37`, ED-PC-0023). So a bias is just a modifier whose lever happens to be a selection lever, and a standing tendency is the `disp` number (the `temper` slot, B18.02). Two words for one thing would be a second owner of the concept.
- **Where an access lands, precisely.** Two places, both existing:
  1. **Engine-side gates** the engine already rolls behind an `if`: the deep-commit gate before the counter and the Indes steal (`wrapper.engagement`, the block the earlier draft found shared, `00_tradition_sets.md:61`); the grab's opening requirement (`contact.grab_available`, agency proposal §5 Class B row 2); the leverage-deficit band in which a withdrawal is attempted (`disengage_attempt_p`, Class B row 3). Each becomes one named member of a `gate` slot family that defaults to today's behaviour. The module reads the slot at the one `if`; it never reads a technique name.
  2. **The per-round choice set**, for anything a player decides: today `TURN_CHOICES = (ENGAGE, WITHDRAW)` (`modules/combat/wrapper.py:552-553`); B16 renames it `ROUND_CHOICES` and B18.09 adds `switch` (scratchpad `b18.md:193,201`). That is the precedent for a granted, player-facing behaviour: a new member, offered only to a fighter whose board grants it, paid for in a unit the engine already debits (B18.09 pays `switch` with `ACT_THRESHOLD`). The brief's Addendum 8 inference that the choice set is "ROUND_CHOICES … where switch and withdraw live" is **half true on today's tree**: the set is `TURN_CHOICES`, `withdraw` is in it, `switch` and `ROUND_CHOICES` are planned (B16, B18.09), not built.
- **What does not transfer: Troubleshooter's outcome-forcing access.** Many of its sets and masteries force an outcome: "Bladestorm will always hit (100% hit)", "Forestallment is always a critical hit", "If your health is below 33%, defend against all attacks" (V, Fandom Mastery Sets, `fandom_wiki.md:1101-1108`). In Valoria every one of these is fiat: it sets a probability directly (agency proposal §5.1 rule 2) or touches `UPSET_FLOOR`/the resolver (Class A). An access may *open a door*; it may never *decide what happens behind it*.

## 2.3 The board's shape

### 2.3.1 Columns: by phase of the bout, derived, never authored

A board has five columns. Each lever (and each future gate) belongs to exactly one column by **where in the bout it acts**; a technique's column follows from its lever, so no one authors it (the earlier draft's rule, `kits_draft.py:124-133`, `SLOT_OF_POINT` "derived from `point`, never authored twice").

| column | plain meaning | live levers in it (sites) | proposed levers (`kits_draft.py:39-71`) |
|---|---|---|---|
| **Distance** | footwork, measure, facing | `measure` (`combat_systems.py:789`), `balance` (`:787-788`, `:1217-1218`), `facing_regime` (`:389`) | `close`, `stophit`, `disengage`, `pursuit` |
| **Reading** | seeing the attack coming | `visual` (`:849-850`, `:1004`, `:1011`), `precommit` (`:1004`) | — |
| **Attack** | committing, hiding the line, keeping the initiative | `tempo` (`:1029`, `:1058`, `:1069`, `:1197`, `:1279`), `anti_overcommit` (`:1039`), `edge_read` (`:816`), `choke_control` (`:817`) | `handling` |
| **Bind and grapple** | what happens when the weapons or bodies meet | `leverage` (`:934`, `:1056`; `wrapper.py:430`), `tactile` (`:936-938`, `:1056`), `spine_press` (`:942`), `edge_grab` (`contact.py:45`) | `grapple_control` |
| **Defence and counter** | the answer to an attack | `counter_select` (`:1029`), `counter_success` (`:1300`) | `guard_prior_parry`, `_dodge`, `_wind` |

**Tested against the two reference slot structures:**

| | Final Fantasy Tactics | Troubleshooter | this board |
|---|---|---|---|
| what a column means | *function*: primary command, secondary command, reaction, support, movement [V: FF wiki, `precedents_other.md` §1.3] | *budget bucket*: Basic, Attack, Ability, Support, Defence; the tag does not match the effect ("A Strategic Retreat is BASIC but opens a DEFENSE slot") [V: `guide_2037290423.md` §5, line 994] | *function*: where in the bout it acts, derived from the engine site |
| slots | 2 action + 1 reaction + 1 support + 1 movement, fixed [V] | per column, rising with character level and with slot-granting masteries [FAN: TroubleMaster; V: tooltips] | per column, rising with growth stage (Part 4) |
| verdict | FFT's single reaction slot is what makes "which reaction" a real choice (two reactions cannot chain: "cannot be used in conjunction with Mana Shield") [V] — **transfers** as one slot in Defence and counter at the novice stage | a bucket that does not match the function is legible only to someone who has learned the exceptions; RPG Fan found the mastery UI "clunky" [V, `troubleshooter_combat_reception.md:113`] — **does not transfer** | |

### 2.3.2 Fixed baseline and equipped entries

- **Fixed baseline.** One or two techniques of the person's *primary* tradition are always on, cost nothing and cannot be taken off. They still have levels and still act only through levels. Troubleshooter's Fandom page: "Every unit in the game has at least 5 innate masteries that cannot be unequipped know as Fixed Masteries" (V, `fandom_masteries.md:19`); in the TroubleMaster data only Leton has character-fixed masteries (FAN, `troubleshooter_characters.md:38`). The two are reconcilable: Fandom counts company, SP-type and class masteries as fixed (`fandom_masteries.md:46-55,492`), TroubleMaster counts only per-character ones. The lesson taken is the *shape* (a pinned foundation plus a chosen layer), not the count.
  - **Why fixed is not fiat:** it adds no effect a level does not already add; it only stops a fighter from leaving their foundation at home. A person with no tradition has no fixed baseline and fights exactly as today.
- **Equipped entries.** Everything else the person knows, chosen per fight, within the slots and the budget.

### 2.3.3 The budget (decision D-A in Part 9)

Troubleshooter runs three limits at once: slots per column, a cost cap per column, and a total Training Point pool (V, user screenshot: five column costs 8+7+7+7+9 = 38 = the pool, caps summing to 47, so the pool binds first, `screenshot_mastery_board_irene.md:14`). Over 39 guide boards the per-column cap is not a function of slots (cap = 2 × slots − 1 holds exactly on 10 of 39 boards; residuals 0/1/2/4) and the pool is level + 0, 2 or 3 with the source of the extra unshown (V, `guide_1349483727_images.md:743-781`).

**Recommended (B-1): two limits, not three.**
1. **Slots per column** — the shape. Starts at one per column for a novice and rises with growth stage (Part 4).
2. **Attention** — one total, the sum of the costs of equipped entries. It answers "how much can this fighter hold in mind in a bout", not "how strong is this fighter". Its source is **Concentration**, which Jordan's 2026-11-07 ruling (PC-22) makes the quantity fight experience writes to: one function of Focus, Spirit and experience. Today the engine computes `conc_max = 3·Focus + 2·Spirit` (`combatant.py:172`, `CFG['CONC_FOCUS']`, `CFG['CONC_SPIRIT']`); the experience term is PC-22's and is not built. **Proposed rule [ASSUMPTION; low; Jordan to correct]: attention = ⌊Concentration ÷ 3⌋**, which gives 5 for a default fighter (Focus 3, Spirit 3: 9 + 6 = 15). The sheets in Part 8 compute it from the engine's `conc_max` and label it.
3. **Cost of an entry [ASSUMPTION; low]:** a modifier costs 1, an access 2, a board rule 1. An entry at level 6 or above costs one less (minimum 0): what is drilled no longer takes attention, which is why a veteran holds more than a novice of the same Focus. A 0-cost entry still occupies a slot, so the slots still bound it.
4. **One technique per lever on a board [ASSUMPTION; low].** Two techniques on one lever multiply (`ability_factor` takes the product, `ability_primitives.py:203-207`). Computed by `sheets.py` for Ysolde Marr (Part 8, sheet 5): Half-time and the crosswise cut at level 4 each give ×3.842 on the reach for a counter, together ×14.758; the site multiplies a base of 0.45 by it (`combat_systems.py:1029`, `config.py:247`), so the reach is certain long before that. The earlier draft held the same line within one tradition ("no second ability on a lever within a tradition", `00_tradition_sets.md:141`); mixing makes it a board rule. The stacking sweep the plan already owns is B15.13 (`ED-SC-0001`, workplan v12 part 18 `:80`), which this rule anticipates and does not replace.
- **Why no per-column cost cap.** On the user's board the pool binds before the caps (above). In Valoria the slot count already shapes the spread across columns, so a per-column cap would be a third number doing the slot count's job: overhead with no decision behind it (§0.06 E).
- **Why this survives the fiat audit** ("expressive availability, not parity", Jordan 2026-07-23, as quoted at `00_tradition_sets.md:25`): attention is the fighter's own quantity, read from their own attributes and experience; nothing is computed to make two builds equal. It limits breadth, never the strength of what is held (strength is the level, Part 4).
- **Why it does not contradict PC-22:** the ruling says fight experience writes "mainly to composure/Concentration … not increased technique and martial prowess itself" (`00_tradition_sets.md:135`). Here experience raises *how many* techniques a fighter can hold, never *how good* any one is. Sparring, which PC-22 caps, therefore raises attention up to its own ceiling.
- **Where it would live (§0.05).** The attention rule and the costs are host-side authoring data next to the curriculum (Part 5); the module never sees a cost or a budget. It sees the composed numbers per slot.

### 2.3.4 Saved boards, and who chooses

- **Three saved boards per person** (Troubleshooter: "You may save 3 preset mastery boards for each character, with additional pages unlockable with coins", V, `fandom_masteries.md:29`). Switching between saved boards between fights is free.
- **No Training-Manual analogue.** Troubleshooter charges a consumable to unequip; its developer said "unrestricted freedom is like a cheat key", players answered that the manuals "actively stop the player from engaging with the game's best system" and "encourage guide building instead of experimentation" (V, Steam thread T66, `discussions_builds.md:305-308`). Valoria's preparation is already priced by *time*: a fighter who knows the fight is coming (a challenge, `duel_terms`) can choose a board; one who is ambushed fights with the board they have. That price exists without a currency.
- **No GM: who chooses for an NPC.** A deterministic host-side composer, one rule for everyone: fill the fixed baseline, then each column with the highest-level entries the slots and attention allow, ties by a stated order. A notable person's authored saved boards override it. The player's chooser (`harness/play_surface.py::dispatching_chooser`, cited at `2026-10-24-character-progression-adjudication.md:268`) may pick among saved boards; nothing else changes in the decision path.
- **Cadence.** Choosing a board is a build decision (agency proposal §2's T0), made between fights. Inside the fight the player still makes one decision per engagement (T1) and the engine resolves every beat (T2). A board entry that is a player-facing access adds a member to that one per-engagement choice; it never adds a per-beat menu.

## 2.4 Proposals on the board, ranked

### B-1. Five phase columns, slots plus attention, fixed baseline, three saved boards (RECOMMENDED)

- **N-line.** Cut the columns and the board is a bag again (FFT lens: "not a bag of abilities — five orthogonal choices", agency proposal §21 A.4). Cut attention and the only limit is the slot count, so a fighter's Focus and experience stop mattering to what they bring. Cut the fixed baseline and a tradition is a list one may leave entirely at home. Cut saved boards and NPCs need a composer anyway while the player re-builds every fight.
- **Runtime change in `engine/season/`.** A host-side composer that turns (person, chosen board) into per-slot numbers in `seam/wrappers/combat.py::combat_input`; per-person saved boards on the carrier (Part 5). The module: none for modifiers; one `gate` slot family and one read per gate for access (§2.2).
- **Falsifier.** (1) An empty board (no tradition, nothing equipped) produces numbers identical to today's defaults, and the fight is byte-identical over paired seeds. (2) Two boards differing only in an entry whose lever the weapon in hand cannot carry (e.g. a spine technique on a rapier) fight byte-identically. (3) A board over budget is refused by the composer by name, never trimmed silently.
- **Build order, with gates.** (1) B18.02 (slot interface). (2) Column table and cost table as authoring data, read by a test only; gate: falsifier (1). (3) The composer for modifiers only; gate: falsifiers (1)–(3), B18.02's seed-2 hash EQUAL. (4) The `gate` family, one gate at a time, each default-closed; gate per item: byte-identity with the gate closed, the agency proposal's §8 RNG-stream rule (a closed gate draws nothing). (5) Saved boards on the carrier.
- **Hash movers.** (1)–(3): EQUAL (the season fills no technique). (4): EQUAL while closed. (5): MOVER(build) only when boards are seeded at build.
- **Cost.** Small for (2)–(3); medium for (4), which touches `modules/combat/` and is the one module change in this whole proposal.
- **Decision it leaves Jordan.** D-A (budget), D-D (gates). Part 9.
- **Lessons.** FFT's orthogonal slots and single reaction slot [V]; Troubleshooter's pinned foundation, saved boards and binding total pool [V/FAN as tagged above]; Bravely Default's support budget rising 1 → 5 with story [V: B2, B4] (a budget that grows, independent of the active job).

### B-2. No equip step: everything learned is on (today's model, made explicit)

- **N-line.** The cheapest board: `equipped` is everything the person knows. What dies: preparation for a known opponent.
- **Runtime change.** Composer only. **Falsifier.** As B-1 (1). **Hash.** EQUAL until a carrier fills techniques. **Cost.** Smallest.
- **Ranked second, and recommended as B-1's first increment.** It is exactly right while a person knows fewer techniques than the slots would hold; it becomes wrong only when cross-training makes the pool larger than the board (D-B).

### B-3. Troubleshooter's three budgets, ported

- Slots, per-column caps, a total pool tied to a character level. Valoria has no character level, so this needs one invented; the per-column cap duplicates the slot shape (§2.3.3). **Dies on E (overhead), not on fiat.** Ranked third.

### B-4. A power budget: equal total investment per growth stage

- Every person of a stage gets the same number of points to spread over levels. **Dies under the fiat audit**: its purpose is parity, which Jordan ruled is the wrong target ("expressive availability, not parity"). Listed so it is not re-proposed.
