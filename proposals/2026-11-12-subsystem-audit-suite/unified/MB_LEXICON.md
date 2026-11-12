# The mass-battle lexicon: one word for each part of an army, its order, the field and the battle

## Status: PROPOSED (A-95, Jordan 2026-11-12: *"we need to formally determine mass battle lexicon for armies"*; decided by the five-step ladder of CLAUDE.md §0 under Jordan's direction of this session; reference, resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Read at: the working tree of 2026-11-12. Lane: MB lexicon. Parts: this file (§1 principle, §2 lexicon groups A–D), `MB_LEXICON_part2.md` (§2 groups E–G), `MB_LEXICON_part3.md` (§3 ladder decisions, §4 the ordered rename batches with coding instructions, §5 what was swept and what is owed).

**What this settles.** A-95 asks for one vocabulary for armies, used the same way by the suite, the tree and,
later, the player. Until this lands the glossary's MB rows stand (A-95's consequence line); from now the
glossary's section **J. Mass battle lexicon** (`U1_GLOSSARY.md`) points each term here, and the rows of §E that
disagreed have been corrected in place. Ruled words (Jordan's own, `DECISIONS_ANSWERED.md`) are not renamed
(STAGES.md, "Terms mean what ordinary English says"); **subformation** is settled in Jordan's sense by A-94.

## §1 · The principle

### 1.1 What the lexicon governs

Every noun and verb that names **an army, a part of an army, how it is ordered, the ground it fights on, the
course of a battle, its clocks, its end and what the army carries away**. Three readers use it:

1. **The suite's prose** uses the lexicon word. Where the tree's identifier differs, the prose gives the
   identifier in backticks once per section (STAGES.md rule) and the word thereafter.
2. **The tree** keeps its identifiers until a v12 batch renames them (§4). A design lane renames nothing.
3. **The player**, later, sees the lexicon word and never an identifier (the GO surface reads this file's
   "game's meaning" column as its call-site text, CLAUDE.md §4).

### 1.2 The test every row passes (STAGES.md; CLAUDE.md §4, RULED ED-IN-0179)

(a) A reader with no memory of this repository, given the word in its sentence, lands on the game's meaning.
(b) The word is used that way outside the repository, in ordinary English or in the military English of the
period the game draws on. (c) **One word, one thing, at every scale where both appear in one sentence**: where
two things must share an ordinary word, the lexicon fixes the qualifier ("unit formation", "army formation";
"season tick", "field tick") and the bare word is refused. (d) Coin nothing a plain word covers. A row that
fails (a) or (b) for a tree name becomes a rename candidate (§4); for a suite coinage it is renamed here and
in the documents (§5); for one of Jordan's words it is listed for him.

### 1.3 The levels (largest to smallest)

| level | the word | one sentence a stranger lands on | where it lives |
|---|---|---|---|
| 1 | **realm** | the kingdom: every territory under one `realm` place | `Rung` kind `realm` (T) |
| 2 | **faction** | a house, Church or movement that holds land and may raise one army | `rosters.yaml: factions` (T) |
| 3 | **army** | a faction's fighting force: the men it has raised and organised into units under one commander | the `army` Record (T, ED-IN-0306): one per faction (`effects_information.py::_army_mintable`, `world_q.army_of`) |
| 3′ | **side** | the men who fight on one side of one battle: the attacker's or the defender's | the season's `claimants` / `subject` sides (T); the engine's `Unit` (T, **a tree name that fails**, §4 L2-1) |
| 4 | **subformation** | a group of units that stands at one post of the army's formation and fights by one set of tactics; led by the officer its units name when one man leads them all | Jordan's word (A-59, A-94). Not in code: proposed as a **read** over the unit rows' `post` (§3 D-1). The code's `Subformation` names one unit, not this (§4 L1-2) |
| 5 | **unit** | a row of the army Record: men of one troop type, with a name, an officer, a role, a posture and orders (A-2) | army Record key `subformations` (T, **fails**, §4 L1-1); `orderofbattle.Subformation` (T, **fails**, L1-2); the engine's `Subunit` (T, **fails**, L2-1); the season verbs `form_unit`, `order_unit`, `disband_unit` (T, pass) |
| 6 | **cell** | the smallest square of the field the battle resolves, and the men standing on it | engine footprint cell (T: 40 to 200 men, `config.CELL_FLOOR`/`CELL_CAP`); proposed 16 men on about 4 m square (`26_MASS_BATTLE_cell_scale_and_time.md` §1, P*) |
| 7 | **rank / file** | a rank is a line of men side by side; a file is a line of men one behind another | period words only (MV F1, F3). The engine counts cells, not men: its "rank" is a row of cells, its "file" a column of cells (`hierarchy/units.py:42`, `COL_WIDTH`); prose says **cell row** / **cell column** for those (§2 C) |

Beside the ladder, not on it: the **squad** (a handful of named characters fighting as one group on a small
grid, `04_MB_squad_grid_of_named_characters.md`), the scale below a unit where named persons fight, reached
from a battle by the duel round (A-4, A-72).

### 1.4 Scale words

- **Army scale** is the scale of this lexicon; it is not a fifth scale of play. A battle is fought at the
  person and army scales together (A-4's nesting; `U1_OWNERS_AND_VOCABULARY.md` §3, *scale of play*).
- **Strength** is how many men are present and fit to fight (§2 D). It is never a fighting value: A-59 says a
  static side-wide fighting value is misleading, and the lexicon has no word for one because the game stores
  none.
- **Size words** (`company`, `battalion`, `regiment`, `host`, `banner`) are **not** game terms: the game has no
  fixed-size echelon between unit and army. They are refused in prose (§2 A rows) so that a reader never infers
  one.

### 1.5 Source keys used in the "period meaning" column

| key | file (all opened by this lane) | tier |
|---|---|---|
| MV | `research/historical/mass_battle_movement_and_behaviour_grounding.md` (rows A–H) | sourced note, pages read |
| SQ | `research/historical/mass_battle_maneuver_sequences_grounding.md` (§n step k) | sourced note |
| CR | `research/historical/mass_battle_casualties_and_results_grounding.md` (rows A–D, table B) | sourced note |
| WG | `research/historical/mass_battle_wargame_models_grounding.md` | sourced note (designs, not history) |
| GA | `research/historical/mass_battle_gauge_grounding.md` | self-authored, cited for the tree's own usage only |
| PF | `research/pre_firearms_formations/04_high_medieval.md`, `06_renaissance_islamic_steppe.md` | memory tier, self-described (`13_verification_corrections.md`); cited only where the sourced notes say nothing |
| OB, UO, BL | `research/game_precedent_suite/grounding/ogre_battle.md`, `unicorn_overlord.md`, `bannerlord_encounter_menu.md` | game precedent |

**Not established anywhere in the filed research:** *host*, *retinue*, *banner* (as a body of men),
*company*, *constable*, *marshal* (as a military office), *muster* (the historical practice), *camp* (as an
institution). For these the period column says so and the row rests on ordinary English alone.

### 1.6 How to read a row in §2

**term** · ordinary English · period meaning (source) · the game's meaning · owner (T tree, P a suite
proposal, P* a proposed file) · code identifier now → proposed (rename id, cost) · rejected words and refused
senses · suite documents that use it wrongly (file §section; "grep" where the hit was read at its line only).

## §2 · The lexicon

### A. The army and its parts

| term | ordinary English | period meaning | the game's meaning | owner | code now → proposed | rejected / refused | used wrongly in |
|---|---|---|---|---|---|---|---|
| **army** | an organised force of soldiers | a field force under one command (MV E6 "both Commanders"; CR table B) | a faction's one fighting force: the men it has raised, in units, under the commander who holds its Record | the `army` Record (T, `rosters.yaml: record_kinds.army`; `armyrecord.KEYS`) | `army` Record (passes); engine `Unit` = one side's army in a battle → `Army` (L2-1) | **host** (the tree's "host" is the season side that hosts a module, `seam/wrappers/`: "host input builder"); "force" as a noun for the Record | none found |
| **side** | one of two opposing parties | — | the men who fight on one side of one battle: the **attacker** (the side that marched) or the **defender** (the side at the place marched on) | `loop/sides.py` (T); engine side `'A'` attacker, `'B'` defender (`orderofbattle._SIDE_DIR`) | passes | "party" for a battle's side (glossary *party*); "army" when allies or a headcount line fight on one side | none found |
| **subformation** | a formation within a larger formation | — (not in the filed research; ordinary British military "formation" is a body above a unit) | **a group of units at one post of the army's formation, fighting by one set of tactics; led by the officer its units name when one man leads them all** (A-59: "each unit within subformation ... impacted by subformation with tactics") | Jordan's word (A-59, A-94). Carried by the unit rows' `post` (P, `04_MB_cell_hierarchy_as_data.md` §3) and the officer column (P, `27_MB_A` §3); the engine's `Officer` already leads "one or more Subunits" under C5's span rule (T, `hierarchy/units.py::Officer`, ED-MB-0073) | none in Jordan's sense. Proposed: one read, `orderofbattle.subformations(oob) -> ((post, unit names), ...)` (§4 L1-6), landing **after** L1-1/L1-2 free the word | "formation post group" (D-U1-11o's coinage, retired here); the code's sense (one unit, §4 L1-1, L1-2); a unit's cell arrangement (that is its **unit formation**) | `27_MB_B_unit_prowess_on_the_row.md` §1 table row 4, §2 (two bullets), gate 5 (read as the unit's arrangement: **swept**, §5); `04_MB_cell_hierarchy_as_data.md` Folded line 1 item (1), §1 (**swept**); `U1_OWNERS_AND_VOCABULARY.md` D-U1-11o (**pointer added**) |
| **unit** | a body of soldiers that is part of a larger force | a sub-unit of a line (SQ §8 step 2, Sabin's "forward sub-units"); OB row 11: a battalion "sectioned into units of at most five" | **a row of the army Record: men of one troop type with a name, an officer, a role, a posture, a target and a fall-back point; its prowess is data on the row** (A-2, A-59) | army Record rows (T); verbs `form_unit`, `assign_troops`, `order_unit`, `disband_unit` (T) | Record key `subformations` → `units` (L1-1); `orderofbattle.Subformation` → `UnitRow` (L1-2); engine `Subunit` → `Unit` (L2-1) | "subformation", "subunit" (tree names), "body" and "block" for a unit (a *body* is `Person.body`; a *block* is the engine's hundred men, `config.BLOCK_SIZE`), "company", "regiment", "battalion", "banner" | "body" for a unit: `14_VERBS_MILITARY_D` (19, grep), `26_MASS_BATTLE_rout_pursuit_and_giving_ground` (26, grep), `26_MASS_BATTLE_movement_and_fatigue_as_data` (15, grep), `04_MB_unit_loadout_and_weapon_in_hand_B` (13, grep), and 18 other MB files (owed, §5); "subunit" in prose: `27_MB_B` (14, grep), `27_MB_A` (5) (owed) |
| **cell** | a small compartment; a small group within a larger body | — (the sourced note gives frontage per man, MV F1, from which the proposed 4 m square is derived) | the smallest square of the field the battle resolves, and the men on it; today 40 to 200 men; proposed 16 men on about 4 m square | engine footprint (T: `config.CELL_FLOOR` 40, `CELL_CAP` 200); `troops.yaml: deployment.cell_troops` 16 (P*) | passes | "grid place" is the squad grid's word for its slots (glossary *cell*) | none found |
| **squad** | a small group of soldiers | OB (units of five with a leader), UO (parties of up to five on a grid) | a handful of named characters fighting as one group on a small grid; the scale below a unit, reached from a battle by the duel round | `04_MB_squad_grid_of_named_characters.md` (P) | none yet (P: `modules/mass_battle/squad.py`) | "unit" for a squad (in the game a unit is a Record row; OB's and UO's "unit" is a squad) | none found |
| **troops** (and **men**) | soldiers, collectively | — | the men of an army or unit, counted | `Subformation.troops` (T, a headcount); the army Record's `trained` (T) | passes | **trooper** for any soldier (ordinary "trooper" is a cavalryman; `armyrecord.disband` docstring says "every trooper") | `armyrecord.py` docstrings (tree prose, owed to L1-1's commit) |
| **troop type** | — | GA :153: armies separated "by type (heavy infantry, light infantry, cavalry, ...)" | the kind of soldier a unit is made of (`levy`, `spearmen`, `pike`, `heavy_infantry`, `cavalry`, `archers`, ...), each with its stats, reach, roles and kit | `troop_types/registry.py::TROOP_TYPE_STATS` (T) | `troop_type` passes | "troop kind" as a second word (prose in `04_MB_cell_hierarchy`, `27_MB_B`, glossary *loadout / kit*: owed, §5) | `04_MB_cell_hierarchy_as_data.md` §1, §4; `27_MB_B` §1 (grep) |
| **levy** | (n.) men conscripted for service; (v.) to raise them | GA :153 uses "levy" as a **quality** (levy / average / veteran); medieval sense, men raised by obligation, not in the filed research | **the troop type `levy`**: the lowest-grade foot (power 1, discipline 1, morale 2). The **act** of raising men is **recruit** (below), never "a levy of 60" | `TROOP_TYPE_STATS['levy']` (T) | passes as a troop type | "levy" for the act or for a draft of men (say **recruit**, **the men recruited**); FA's proposed gate name `may_levy` (P, `06_FA_levy_through_the_seat_B.md`) is FA's and stays a gate name (ordinary "levy troops"), but MB prose about it says "may recruit from" | `14_VERBS_MILITARY_C_the_muster.md` §1 item 3, §4 ("one levy of 60"), refusal Event `levy.shirked` (P → `recruit.shirked`, §5) |
| **retinue** | the attendants of an important person | PF 06:139 ("the king's personal retinue", memory tier); MV R7: "a household may stand and die around its lord" | **not a game term.** A lord's own followers are his **sworn men** (A-22, glossary *sworn*) or a unit his officer leads | — | — | "retinue", "household troops" as an entity | none found |
| **host**, **company**, **banner**, **battalion**, **regiment** | host: a large army (archaic); company: about a hundred men under a captain; banner: a lord's flag and the men under it | PF 04:22 (a *conroi* "under a single banner", memory tier); `config.BLOCK_SIZE = 100` cites "Company scale" | **not game terms**: the game has no fixed-size echelon between unit and army (§1.4) | — | `BLOCK_SIZE` (T) is a hundred men, the size below which an army does not take the field (`armyrecord.options`: `army_routs`); it names no echelon | all five as names of anything in the game | none found |

### B. People and command

| term | ordinary English | period meaning | the game's meaning | owner | code now → proposed | rejected / refused | used wrongly in |
|---|---|---|---|---|---|---|---|
| **commander** | the person in command of a force | MV E6 ("the chief point to be looked at by both Commanders"), E4 | **the person who holds the army Record**; "an army is where its commander is" | `world_q.hold_force(w, army id)` (T); `seam/wrappers/mass_battle.py::_order_of_battle` docstring (T) | passes. Proposed class `GeneralAction` (P, `04_MB_manager_battle_one_resolver.md` §4) → `CommanderAction` (§5) | **general** (a rank; the suite uses it for the commander), **captain**, **marshal**, **constable** as the army's leader | "general" for the commander: `26_MASS_BATTLE_rout_pursuit_and_giving_ground` (11, incl. §1 table "the army's general is removed from command"), `16_PESSIMIST_MB_rout_has_two_exits` (8, steps 1–2), `04_MB_manager_battle_one_resolver` (title, §4), `26_MASS_BATTLE_maneuver_orders` (6), `27_MB_A` (4), `04_MB_playable_field_scenario` (2), `26_MASS_BATTLE_cell_scale_and_time` §3 (`GeneralAction`) (all owed, §5) |
| **officer** | a person holding a commission; one who leads soldiers | MV E4 (the Hospitallers' officers); WG (command range) | **the person a unit row names to lead the unit**; one officer may lead several units, up to his `command` (C5, "max commanded = Command at every echelon") | `hierarchy/units.py::Officer` (T, ED-MB-0073); the unit row's `officer` column (P, `27_MB_A` §3) | passes | "captain" (a rank), "lieutenant"; a seat-holder is a **holder**, not an officer (glossary *officer*) | none found |
| **general, captain, marshal, constable** | ranks and titles of command | **marshal** and **constable**: not in the filed research | **not roles in the army.** *Marshal* is (1) the season verb `marshal`, to set a side's standing order (below), passes: "to arrange troops in order"; (2) a canon seat title (Valorsmark's Marshal, A-91), a seat like any other | verb `marshal` (T, `verb_table.yaml`) | `marshal` passes | all four as names for the commander or an officer | see *commander* |
| **command** | (n.) authority over a force; the skill of exercising it | MV E1–E5: orders few, coarse, slow and sometimes disobeyed | **the capability by which an order takes effect**: the learned score gives dice, Presence and Reason give levels (A-59, A-7) | DR `capabilities` (P, `27_MB_A` §1) | engine `Unit.command`, `Officer.command` integers 1..7 and `derive_command` (T) are retired by D-U1-11g; `command_span` keeps its name | "Command Rating"; "command" for the authority to order (that is **command basis**) | none found |
| **command basis** | — | — | **whom a seat may order** (A-22: its sworn men, holders of seats it may revoke, the unseated in its land; a writ to a superior is a petition) | `basis: command` (P) | — | "chain of command", "command authority" (say command basis) | none found |
| **order** (n.) | a command | MV E3 (sound and sign), E4 (disobeyed) | one instruction to a unit. Three kinds: a **standing order** (given before the battle: a trigger and a behaviour, at most `standing_order_cap` a unit); an **improvised order** (given by the commander at a window or a lull, `27_MB_A` §3); a **signal** (fired by the commander, releasing every standing order that waits on it) | `hierarchy/units.py::Order`, `_ORDER_TRIGGER_KINDS` (T); `battle_orders.json` (T) | passes | "command" for an order; "instruction" for an order (an instruction is a role's built-in behaviour, `config.ROLE_SPEC`) | none found |
| **issue / dispatch** | to give out formally / to send off | — | the season verbs of a **seat**: `issue` mints a writ or decree; `dispatch` sends a person. Neither gives an order to an army: an army is ordered through its Record (`order_unit`) and in the field | `verb_table.yaml` (T) | pass | "issue an order to the army", "dispatch a unit" | none found |
| **window** | an interval when something may be done | MV E5 (an umpire holds a message "for a round or two") | a moment inside a bout (today an engine phase boundary, two in a bout) at which a commander may take one action | `04_MB_manager_battle_one_resolver.md` §4 (P) | `FieldWindowView.window` (P) | "turn" for a window | `04_MB_playable_field_scenario.md` :47 ("a general's action each turn", grep) |
