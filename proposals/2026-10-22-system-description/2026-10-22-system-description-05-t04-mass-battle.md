# Tutorial: Mass Battle — send an army at a place, and learn what the battle engine rewards once two armies meet

Repo `jordanelias/ttrpg` at HEAD `a4ca9a5`; revised in round 3 against `51d7b05` and the precedent suite (`research/game_precedent_suite/`); the
corrections are listed in `### Round-3 corrections`, at the end of §8. Path abbreviations: `MM/` = `modules/mass_battle/`, `MB.py` = `MM/massbattle.py`,
`SW` = `engine/season/seam/wrappers/mass_battle.py`, `EC` = `engine/season/loop/effects_combat.py`, `VT` = `engine/season/verb_table.yaml`,
`RY` = `engine/season/rosters.yaml`, `cfg` = `MM/config.py`, `orch` = `MM/orchestration.py`, `units` = `MM/hierarchy/units.py`.

## 0 Before you start

**The frame.** The code has no player character and no GM. Every person is a chooser that picks scene actions each season from a closed table
of verbs. "You" means the acting person: a player's character if one is seated later, an NPC today. The tutorial teaches what an actor can
do, what the rules do with it, and what the actor has to arrange to reach a goal. Rules that exist only in a proposal are marked
**[PROPOSED]** and kept in §7.

**Action economy.** `budget()` returns scene actions (`decision/budget.py:18-61`):
`max(1, 5 + 1 per live hold − body bands − 1 per travel leg)`. A scene holding more than one act costs 2, and the driver releases at most one
scene per round over 5 rounds. So a budget of 5 buys 2 + 2 + 1 = 7 acts and a budget of 6 buys 9 (round-2 ruling C1).

**Two primitives used throughout.**

- A **Rung** is any node of the world's containment ladder: person, hearth, community, settlement, territory, duchy, realm. Every place is a
  Rung.
- A **Tenure** is the one edge type joining an entity to a Rung or an office. Its kinds include `contain` (where a person is), `hold`
  (title) and `commit` (membership of a faction).

A **faction** is a `fac_*` Proposition plus the `commit` Tenures pointing at it. There is no Faction object.

**Two games under one name.**

1. **The battle engine** (`MM/`, about 10,150 lines, plus about 3,090 under `systems/mass_battle/`): a tick-by-tick simulation of two armies on
   a 51 × 51 cell field, with formations, troop types, contact, support ranks, volleys, charges, flanks, stamina, discipline, morale and rout.
   It has its own dice. You can play it directly in Python by building both armies yourself.
2. **The season path**: one verb, `march`, which hands the engine two armies built almost entirely from defaults.

**What you need from other subsystems.**

- **A seat whose office grants `remit:dispatch`.** In the shipped realm build this comes from `remit_default`, which is "NOT CANON. A TESTING
  FIXTURE" that hands every seated office every remit act (`RY:324-334, 376`). It gives 25 of the 32 offices in `build_realm(0)`. The tree
  contradicts itself on whether that roster is closed: `RY:315` says "the CLOSED five" and `RY:316` says `open: true`.
- **Faction members whose home is under the settlement you march from.**
- **A target settlement.**

**Status: TESTS-ONLY.**

- In the control run (`ctl/realm_seed*_2seasons.txt`, two seasons; "attempted" = acts admitted to the fold), `march` reaches the fold and is
  declared at seeds 0, 1 and 2, with attempted/ok of 21/21, 10/10 and 4/4.
- The "ok" counts the `Declared` event. Every declared march is then refused, so no field is fought in the control run at any seed:
  `field.won`, `field.lost`, `field.unopposed` and `army.arrived` are 0 in all three.
- The engine itself runs only under tests, harnesses and direct calls, but the season loop reaches it whenever an act names a settlement held
  by another faction with members present (`loop/sides.py:108-132`; `SW:236-262`). A hand-built `march {subject: set_s_036}` by `p_npc_033` via
  `off_npc_033`, folded through RESOLVE and ENCOUNTER on `build_realm(0)`, `(1)` and `(2)`, gives `march.declared` then `field.lost` (2 attackers,
  Σ weight 2, against 6; each attacker's body 1000 → 20). Run again inside one full season, with `harness/play_surface.py:41`
  (`dispatching_chooser`) handing `p_npc_033` the act and every other person on the shipped chooser, it gives `field.lost` once at each of seeds
  0-2. `engine/season/tests/test_march.py:368-456` has the real chooser form the act when a `Question` names the settlement. No act the shipped
  chooser formed at seeds 0-2 names a settlement (§3.3). The grade stays TESTS-ONLY (errata G1).
- **Natural play and callback play, as this tutorial uses the words.** *Natural play*: the shipped chooser (`make_chooser` over
  `resolvable_verbs()`, as `populated.run` builds it) forms every act; this is the control run. *Callback play*: a client hands a named person's act
  in (`dispatching_chooser`), or a test hand-builds it (`_march_act` in `test_march.py`); the loop folds it with the same RESOLVE and ENCOUNTER.
  §3.3 and §5 label each claim with one of the two.

## 0a How it plays

One march from the actor's choice to what is left afterwards, as built at `51d7b05`. Everything that exists only in a design is in the
`[PROPOSED]` block at the end. Precedent cites are to `research/game_precedent_suite/tutorials/` (tier 3 reference, `CLAUDE.md` §0.05):
`T07_mass_battle.md` (Total War, Field of Glory II), `T17_repo_strategy_a.md` (Dominions) and `T19_tactics_narrative.md` (Unicorn Overlord).

**Setup choices.**
- *At world build (seed).* `build_realm(seed)` fixes everything a field reads: who lives where (each person's `weight`, 1 or 2; §1), which
  faction holds each territory (`holder_faction_of`, §1), and each settlement's garrison condition, which is above 0 on all 37, so every realm
  field is WALLS (`MB.py:272-273`; §1). No troop type, formation, unit stance or general is chosen: `resolve_field` builds one fixed shape
  (`MB.py:170-186, 213-232`).
- *At DELIBERATE (natural play: the shipped chooser; callback play: the client).* One choice: the target Rung. The army is whoever of the seat's
  faction is mustered at the actor's home settlement (`loop/sides.py:115`), less anyone detained (`:122`).

**The loop.** One season is CALENDAR → MATTER → five rounds of (DELIBERATE → RESOLVE → ENCOUNTER → WITNESS) → CENSUS (overview §2.1). A march:
1. DELIBERATE: the chooser forms `march` against a Rung, scored on four value axes (§2.2 step 1).
2. RESOLVE: the typed cell checks only that the subject is a Rung; the act folds at Declared, emits `march.declared` and writes nothing (§2.2 step 2).
3. ENCOUNTER, same round: a non-settlement target gets an empty army and is refused (`loop/sides.py:108`); a target held by your own faction, or
   by nobody, names no defender (`:132`).
4. Provider: no defender present → Unopposed, no battle (`SW:238-249`); otherwise `resolve_field` runs the full engine, `run_battle(..., max_turns=18)`
   (`MB.py:283`).
5. Grade: `attacker_wins = not a.routed and (b.routed or a% > d%)` (`MB.py:287`) → Won or Lost; ties and mutual routs go to the defender.
6. Writes, losers only: body scaled (`EC:298-299`), a grudge row and a morale row (`EC:300-305`); on Won or Unopposed the movers relocate
   (`EC:257, 291`).

Automated: everything after the target pick. There is no pause, no withdraw, no choice of fidelity, no aftermath screen.

**The choice menu.** The two middle columns are the point: what the shipped chooser does, and what a callback can make the loop do.

| verb | cost and effect | natural play (ctl, seeds 0-2) | callback play (run at `51d7b05`) | grade |
|---|---|---|---|---|
| `march` at a settlement held by another faction, members present | one scene action. Won: defenders' bodies scaled, rows, you arrive (a travel leg each). Lost: your bodies scaled, rows, you stay | never formed: declared subjects are persons, hearths and territories (§3.3) | `set_s_036`, 2 v 6: `field.lost`, body 1000 → 20, at seeds 0-2. No Won field has been fought; Won is exercised only through a constructed `Resolution` (`test_march.py:254`) | TESTS-ONLY |
| `march` at a settlement with no opposing holder, or none of the holder's people present | one scene action. Unopposed: your mustered members arrive (a travel leg each); no battle, no casualty, no row | never formed (`army.arrived` 0) | `set_s_014` → `set_s_003`, seeds 0-2: `field.unopposed`, `army.arrived`, bodies unchanged | TESTS-ONLY |
| `march` at any other Rung (person, hearth, territory) | one scene action; Declared, then `march.refused` | every natural march: declared 21 / 10 / 4, refused 25 / 10 / 4 | refused the same way (`test_march.py`, hearth target; not re-run here) | RUNS-IN-LOOP (the refusal only) |
| do nothing (defend) | none; presence defends and walls apply by themselves | always; the defender has no chooser | same | — |
| engine-direct options (formation, stance, troop type, Orders, officers, multi-unit, pursuit) | a Python call (§3.2) | not offered | not offered; a designer only | TESTS-ONLY |

**First season, step by step.**
- *Natural play* (two seasons; `ctl/realm_seed0_2seasons.txt:20, 41-46`): 21 `march` acts reach the fold and all 21 are declared; `march.refused` is
  25 (the 4 extra failed the typed cell at RESOLVE, §3.3); `field.won`, `field.lost`, `field.unopposed` and `army.arrived` are all 0. Seeds 1 and 2:
  10 and 4 declared, 0 fields (`realm_seed1_2seasons.txt:22, 42-47`; `realm_seed2_2seasons.txt:21, 42-47`).
- *Callback play, a traced field* (identical at seeds 0-2; the pair `test_march.py:82-136` uses):
  1. RESOLVE: `p_npc_033` (Crown) via `off_npc_033` declares `march {subject: set_s_036}`; `march.declared`.
  2. ENCOUNTER: `set_s_036` is a settlement. Attackers are the Crown members mustered at his home settlement `set_s_014`: `p_npc_033` and
     `p_npc_035` (Σ weight 2). The defending faction is the Church of Solmund, with 6 members present (Σ 6).
  3. `fortification_of(set_s_036)` = 1.0, so WALLS: defender DR 1 + 3 = 4 (`MB.py:272-273`).
  4. `run_battle`: one Line infantry block of 2 troops against one of 6, both from (8, 12). Both have hp < 100, so `size = 0` and both rout on
     tick 1 (`units:2930-2938`); a mutual rout goes to the defender (`MB.py:287`): Lost.
  5. Writes: each attacker's body 1000 → `int(1000 × 0.02)` = 20 (`EC:299`), plus `(fac_church_of_solmund, −1, 1)` and `(fac_crown, −1, 1)`
     (`EC:300-305`). The six defenders are untouched.
  6. Next season: body 20 is under all three band floors (800 / 500 / 100), so `p_npc_033`'s budget falls from 6 to max(1, 5 + 1 hold − 3) = 3
     (measured), i.e. 3 acts instead of 9 (§3.1; errata Part 2 C1), and his next morale start is 4 (§3.1).

**What changes later.** As built, nothing compounds. Walls never decay (garrison wear 0, §5c). At realm weights a body rises only by `tend`, which
executed 0 of 34 times at seed 0 (overview §3 NP row). Musters change when a `contain` or `commit` edge changes. A lost field's grudge rows feed the
chooser's stance toward the winning faction (§5e). No army has experience, a recruit pool, pay or supply: none of the 53 verb rows is `levy`, `muster`,
`recruit`, `supply` or `forage` (`VT`).

**Failure and ending.**
- A field's failure is Lost: the losers' bodies are scaled (floor 1; nobody dies under the default `scaled_by_degree`, `EC:299`), two stance rows are
  written, and attackers stay at their origin. Only the `total` setting removes them (`EC:316`).
- Inside a battle: the 18-tick clock; rout at size 0, subunit morale ≤ 0 or under 80 troops, the 60% army line (inert for one subunit, `cfg:116`),
  or command 0 (never set during a battle, `units:2717, 2722, 2811`). Routed units never rally: `rally_check` is empty (`orch:288-290`).
- The season now reports endings (`world_q.endings_reached`, `world_q.py:1764`: a read over holds and seats, never an actor), and the realm as built
  reaches none. A field writes no `hold` (§2.2 step 8), so no field result is an input to it.

**Consequential vs cosmetic choices.**
- *Consequential in the season:* whether the target is a settlement (else refused); whether its holder has anyone present (else Unopposed). Summed
  weight (400 v 200: 66.0% against 44.0%) and walls (29.0%) are consequential in the season-shaped runs of `resolve_field` (§3.2), which no realm
  weight reaches: at realm weights every opposed field is Lost (§3.1).
- *Cosmetic in the season:* the morale start (stance −2: 43.5% and 44.5%, no measurable change); UPHILL and RIVER_CROSSING (noise), and never reached
  in the realm because WALLS takes precedence (§2.2 step 6).
- *Engine-direct only (a Python call, never a season act):* tier, power, the knights preset and command 0 move the win share beyond noise. Discipline 2
  and an Arrowhead without a charge order lower it by 6-8 points, at the edge of the ±7 margin. The other arms are noise (§3.2).

**[PROPOSED]** (§7; nothing here executes).
- *Player command.* No played mass battle is designed: IN-46 is a played, paused personal fight (overview §2.1), and whether a player may command a
  field is open (J-C-31, §7). A seated player could, at most, pick the target.
- *What precedent puts at this step* [precedent: reference only]: army composition and a recruit choice (T07 Total War §1, §3), force selection to a
  cap (T07 Field of Glory II §1), an Army Setup with orders and spell scripts set before a battle that is always simulated (T17 Dominions §2), and
  per-character Tactics (T19 Unicorn Overlord §2). The season has none of these; §7's `levy`, `muster` and `marshal` are the proposed entries.
- *Later:* REM-27 narrows `march` to settlements the marcher has been told of; REM-32/JQ-4 adds a weight-to-troop conversion, which must lift a side to
  100 troops or more; Suite 1 `levy`, `muster`, `drill`, `disband` (M-2, M-8); Suite 2 `marshal` with `rally`, `pursue`, `retreat`, `withstand`
  (M-3, M-4, M-5); Suite 3 `storm`, `besiege`, `supply`, `forage` (M-1, M-6); Suite 4 `surrender`.

## 1 The pieces

| term | what it is | numbers / limits | where it lives |
|---|---|---|---|
| **field** | the prize `march` contests: routed to `mass_battle`, declared at RESOLVE, fought at ENCOUNTER | `step: ENCOUNTER`, `declares: Declared` | `RY:1278-1283` |
| **battlefield** | cell grid | 51 × 51; side A starts at row 34, side B at row 15 | `cfg:16, 27-28` |
| **cell** | a grid square holding troops | fights up to 200 troops (100 for cavalry and knights) | `cfg:41` |
| **Unit** | one army: power, command, discipline, morale, dr (armour), hp, size, stance, speed, stamina, volleys, officers | `dr` default 1; `hp` = troops; `size = floor(hp / 100)` | `units:2728, 2930-2938` |
| **Subunit** | one block in a Unit: shape, troop type, tier or `troops`, per-cell troop and morale grids, role, orders | inherits power/discipline/morale/dr from its Unit when its own value is None | `units:479, 739-742` |
| **tier** | block size used when `troops` is not given | 1:100, 2:200, 3:400, 4:800 | `cfg:33` |
| **troop type** | stat preset (power/discipline/morale), applied only through `Subunit.of_type` or `build_army` | levy 1/1/2; light inf 3/3/4; heavy inf and pike 4/4/5; cavalry 5/5/5; knights_templar 5/6/6; archers, crossbow 3/3/3; sling, artillery 2/2/3 | `MM/troop_types/registry.py:39-57`; `units:713-728` |
| **reach** | the only equipment fact the engine reads | levy/light/infantry 0.1; heavy and cavalry 0.2; pike 0.3 | `registry.py:62-75` |
| **formation (shape)** | cell pattern | Line, Arrowhead, GappedLine, Column (Column = Line transposed); falls back to Line below `MIN_DISCIPLINE` (1/4/5/3) | `MM/geometry.py:21-48`; `cfg:201`; `units:2983` |
| **role** | named job that sets shape and instructions | ShieldWall (Line, brace + hold), Shock (Arrowhead, charge), Skirmish (GappedLine, loose + harass), … | `cfg:582, 600` |
| **instruction** | primitive behind a role | wired: brace, envelop, sweep, kite, reserve, hold, push/charge, lure. Unwired: pin, loose, harass, screen, pursue, volley, shoot_move | `units:71-100` |
| **stance** | commitment and speed | aggressive (+1 speed, +1), balanced (0, 0), hold (speed −99, −1), retreat (0, −1) | `cfg:279, 290` |
| **Order** | timed or conditional behaviour change | triggers `immediate`, `tick:N`, `enemy_range:D`, `ally_at:D`, `own_strength:FRAC`, `signal:NAME` | `units:399` |
| **Officer** | a leader | command default 4; `derive_command(charisma, cognition)` when enabled | `units:2700`; `MM/core/exchange.py:57` |
| **tick / phase** | one loop step; six ticks = one phase | battle = 18 ticks = 3 phases | `orch:1815`; `cfg:155` |
| **friction** | per-army luck, drawn once per battle, multiplying its pool | `exp(gauss(0, 1.1))`; middle half about 0.48-2.1 | `orch:1742`; `cfg:335` |
| **pool** | dice an army part rolls in a contact | `power × size × 0.5 + discipline penalty + stamina penalty`, × friction, floor 1; **command is not read** | `exchange.py:77, 100-124`; `cfg:576` |
| **support ranks** | troops behind the contact line adding to the pool | 1.0 / 0.7 / 0.5 by depth, floor 0.3 | `cfg:139`; `exchange.py:151` |
| **degree** | outcome of one exchange | margin < 0 Failure, < 1 Partial, ≥ 3 Overwhelming, else Success | `MM/resolution.py:104` |
| **damage by degree** | the blow before armour | Overwhelming 1 + power, Success power, Partial 1, Failure 0; minus target DR, floor 0 | `cfg:307-308`; `orch:1377-1378` |
| **angle (octagon)** | where a blow lands relative to facing | under 45° GREEN ×1.0, under 90° YELLOW ×1.5, else RED ×2.0 | `geometry.py:142-178`; `cfg:219` |
| **stamina** | endurance | 100; −1 per cell in contact per tick; at 0, −1 die | `cfg:158-159` |
| **morale** | will to stay | season start 1-7; rout at ≤ 0 | `MB.py:93-101, 119` |
| **rout** | leaving the fight | **army: `hp < 100` (size 0), checked every tick first**; then subunit morale ≤ 0 or under 80 troops; army command ≤ 0, 60% of troops in routed subunits (`ROUT_CASCADE_FRAC`, `cfg:116`, whose note calls it inert for any one-subunit army, so for every season army), or total morale ≤ 0 | `units:2930-2938`; `orch:2205-2206, 2262-2268`; `units:2876, 2893` |
| **terrain row** | one modifier per field | OPEN_FLAT, WALLS, UPHILL, RIVER_CROSSING, FOREST_BROKEN, NARROW_PASS | `MM/terrain.py:45-50, 109` |
| **`march`** | the one season verb: settlement scale, contested, needs `remit:dispatch` | bands Declared / Won / Lost / Unopposed | `VT:803-834` |
| **mustered** (query) | members of a faction present in a Rung's subtree | weight-summed | `engine/season/queries/world_q.py:1473` |
| **holder_faction_of** | faction of the nearest **held** Rung at or above the target | seeded settlements are not held directly, so the walk reaches the territory's holder | `world_q.py:1659-1681` |
| **fortification** | mean condition of the garrison Sites in a settlement's subtree, 0-1 | > 0 makes the field WALLS; 37 of 37 realm settlements > 0; garrison wear 0 | `world_q.py:1493`; `RY:1451-1470` |
| **Person.weight** | the season's headcount for one person | realm: 1 (46 named) or 2 (37 cohorts) | measured, `build_realm(0)` |
| **Person.body** | physical condition | 1000 for all 83 at build; budget band floors 800 / 500 / 100 | measured; fixture `band_floors.body` |

## 2 How it works

### 2.1 The engine, in the order a battle runs (`orch:1815-2300`)

**Setup.** Each army draws one friction factor. The caller's `rng` is scoped over the battle (`MM/rngsource.py`).

**Each tick, in order:**

1. Stop if either army has routed.
2. **Volleys.** Each ranged subunit with ammunition (10 volleys) fires at a target 2-8 cells away. Its pool is `max(1, power − penalty)` (0 at
   discipline ≥ 5, 1 at 3-4, 2 at 1-2). Net successes are reduced by the target's DR (2 if none) and scaled by `0.25 × size` and by density
   (`mean / 80`, clamped 0.5-2). Volley hp loss is ×3 (`cfg:15`).
3. **Orders and movement.** Orders fire and targets are assigned. Subunits advance, with step speed multiplied by 1.0 at discipline ≥ 5, 0.7 at
   3-4 and 0.4 below 3 (`units:1823`). The same factor is the cohesion weight that lets ragged formations deform. Measured closing is slower
   than the multiplier alone (§3.2).
4. **Contact.** Two cells are in contact within `(0.5 + reach_a) + (0.5 + reach_b)`. A subunit in contact loses 1 stamina per contacting cell.
5. **Melee, per contact pair** (`orch:727`):
   - *Pool*: the base pool is spread over the contacting troops plus the support ranks.
   - *Net*: a fractional d10 roll at TN 7 (face 1 = −1, 2-6 = 0, 7-9 = +1, 10 = +2; the fractional part of the pool is one extra die rolled with
     that probability), plus a σ boost `1.5·tanh(Δσ/1.5) × 0.8 × √pool`. Δσ sums momentum and puncture (cap 3), charge shock, brace recoil
     (6 × preparation × 0.2), morale, fatigue, stance intent `(cA·0.5 + cB·1.0) × 0.2` and terrain `(offence dice − defence dice) × 0.2`.
   - *Degree*: each side is graded against the other's net (minimum 1) as obstacle.
   - *Casualties*: `12 × strength × max(0, damage(degree, power) − target DR) × angle multiplier`. Strength is engaged columns × (troops per
     cell / 100) / 4. There is +50% per extra side in contact (`cfg:230, 515-519`).
6. **Losses applied** and ranks closed. Then `recalc_size`: `size = floor(hp / 100)`, and **size 0 routs the whole army** (`units:2930-2938`).
   This runs before the 80-troop subunit check, so for a one-subunit army **the binding rout line is 100 troops**. A side of 80-99 troops
   routs on tick 1.
7. **Command 0** sets morale to 0, an instant rout (`orch:2221-2225`; its comment: "M1: general IS the army"). Nothing writes command during a
   battle: inside `modules/` and `engine/` the only writers are the constructors at `units:2717, 2722, 2811`, and a validator fixture sets it on a
   test unit (`systems/mass_battle/sim/validators.py:287`). So a general never falls mid-fight; the rule fires only on an army built at command 0.
   Measured: command 0 against 4 is routed in 200 of 200 seeds.
8. **Envelopment shock**: a unit struck in the flank or rear that fails a discipline roll takes a morale hit.
9. **Per-tick subunit rout**: morale ≤ 0 or under 80 troops (`orch:2262-2268`).
10. **Every sixth tick, a phase boundary** (`orch:337`):
   - stamina recovers by 8 per reserve rank;
   - **at most one** discipline −1 per boundary, and only while you have lost more than the enemy and your losses reach the next 100 troops
     (`MM/core/state.py:228-237`);
   - morale erosion: +1 below 50% cohesion, +1 below 25%, +1 if broken, plus an exhaustion term `1/(discipline × command)` at stamina 0;
     capped at 3 and multiplied by 0.7, so at most 2.1 per boundary (`state.py:90-117`);
   - yield (below 50% cohesion, discipline ≥ 3);
   - a stochastic break, at a point between 15% and 30% losses biased by starting discipline and morale;
   - then rout resolution, the empty `rally_check`, `reform_check` (+1 discipline for an unengaged unit, only if command ≥ discipline + 1,
     i.e. 6 at the default discipline 5; `orch:318-328`) and the empty `threadwork_check`.

**The engine's own winner** is A if B routed and A did not, B in the converse case, otherwise a draw (`orch:2290`). At 400 v 400, 146 of 200 battles
are draws.

### 2.2 The season path, step by step

1. **DELIBERATE.** A seated person whose office grants `remit:dispatch` may form `march` against a subject Rung (`VT:807`). The chooser scores it
   on four of the seven value axes: hierarchical −0.5, partisan −0.4, grandiose −0.4 and instrumental +0.4 (`RY:3120, 3206, 3358, 3419`).
2. **RESOLVE.** The typed cell is `form: existence, of: subject, kind: Rung` (`VT:809-813`). It does not narrow to settlements. If it passes,
   the act folds at `Declared`, emits `march.declared` and writes nothing.
3. **ENCOUNTER** (`loop/encounter.py`), same round. `sides_of` (`loop/sides.py:41-131`) then works out the sides:
   - the target must be a `settlement` (`march_target_kinds`, `RY:918-931`). Otherwise the army is empty, and the act is refused by
     `_refuse_party_gap` (`loop/resolve.py:787-788`) before the provider is reached;
   - **attackers** are the members of the seat's faction mustered at the actor's nearest settlement above his home, less anyone under
     `detain`;
   - **the defending faction** is `holder_faction_of(target)`. When that is `None`, or is the actor's own faction, there is no defending
     side.
4. **Provider** (`SW:178-273`). The defenders are the defending faction's members mustered at the target. If there are none, or no defending
   faction, the result is **Unopposed** with no engine call. Otherwise the provider builds a `MassBattleInput` and calls `resolve_field`.
5. **`resolve_field`** (`MB.py:306`) builds per side **one Unit, one Line subunit of `infantry`**:
   - `troops = Σ weight` (at least 1.0), power 4, command 4, discipline 5, DR 1;
   - morale start = `clamp(round_half_up(5 + stance toward own faction + gain × loyalty), 1, 7)`, with gain 0 as shipped (`MB.py:119-232`);
   - both sides come from the same position dict, so they start on the same cell, (8, 12).
6. **Terrain** (`terrain.py:109`): an unknown territory gives OPEN_FLAT. `fort_level > 0` gives **WALLS** (defender DR +3). Otherwise a river
   crossing (attacker −1 offence die; checked only at `fort_level ≤ 0`), otherwise a polygon lookup (UPHILL ±1 die; FOREST and NARROW_PASS
   change nothing the battle reads). **Why WALLS bites at power 4:** walled DR is 1 + 3 = 4, so a Success (damage 4) and a Partial (damage 1) do
   nothing to the defender. Only an Overwhelming (5 − 4 = 1) hurts it.
7. **Grading** (`MB.py:285-293`):
   - `a% = effective_size / size_max` (`size_max` at least 1, i.e. 100 troops), and likewise `d%`;
   - **`attacker_wins = attacker not routed AND (defender routed OR a% > d%)`**. A tie and a mutual rout go to the defender;
   - the season ignores the engine's own four labels. `field_degree` (`seam/ladder.py:185`) gives Won, Lost or Unopposed.
8. **Writes** (`EC:183-320`), on the **losing** side only:
   - body becomes `max(1, int(body × that side's size share))` under `field_casualty_model = scaled_by_degree` (`total` sets 0 and removes
     the person; `none` leaves body alone);
   - two stance rows: −1 × 1 toward the winning faction (grudge), and −1 × 1 toward one's own faction (next morale start −1);
   - on Won or Unopposed, the attackers not already under the target are relocated and `army.arrived` is emitted. If nobody moves and
     nobody falls, the act declines to `march.refused` (`EC:257-263`; `VT:828`);
   - the winner is never written. No `hold` moves and no stores move. Under the default setting body is floored at 1, so **a lost field kills
     nobody**.

### 2.3 What each layer can teach a designer

- **The standalone engine** is a battle laboratory. Numbers, quality (power, armour), discipline (which is also speed), formation footprint,
  stance, walls, Orders, officers and multi-subunit armies all act, and a 200-seed sweep shows each one's size (§3.2).
- **What it teaches about battle:**
  - casualties need a degree that beats armour;
  - battles are mostly undecided after 18 ticks and are graded on surviving size;
  - closing distance is a resource;
  - a single block's command matters only at 0.
- **The season** teaches none of that. Its only varying inputs are summed weight, a morale start that showed no measurable effect, and a terrain
  row that is WALLS on every realm settlement. At realm weights both sides rout on tick 1. What the season does teach is the strategic
  shell: who may march, from where, at whom, and what a loss writes.
- **One resolver, and what precedent says about it** (reference only, `CLAUDE.md` §0.05). The season's field is the same `run_battle` the
  engine-direct path runs (`MB.py:283`), so there is no fast path to diverge from a played one. Total War's own first-party texts warn that its
  fast path is worse for the player (M2TW manual p21: casualties "may be heavier" and the General can die; 3K's Delegate "ignores many possible
  player inputs") [V3 manual p21; fandom Battle] (T07 Total War §3, `research/game_precedent_suite/tutorials/T07_mass_battle.md`). The verified
  single-resolver precedents are Dominions (battles always simulated from a pre-set Army Setup, orders and spell scripts, replayed next turn)
  [V3] (T17 Dominions §2, `.../tutorials/T17_repo_strategy_a.md`) and Field of Glory II (no auto-resolve in its 227-page manual) [V3] (T07
  Field of Glory II §8). Football Manager's "instant ≈ played" is not established (T16 FM §8, `.../tutorials/T16_managers_narrative.md`). What
  Dominions has and the season lacks is the pre-battle intent step, §7's `marshal`.

## 3 A worked example

Read-only runs of the real code (`python -I`; scripts in §9). N = 200 seeds (`random.Random(0..199)`), with the same seeds in every arm. **At a win
share near 45%, the 95% margin is about ±7 points.** Smaller differences are noise.

### 3.1 Two equal armies, season-shaped (`resolve_field`, territory unknown → OPEN_FLAT)

| matchup (Σ weight) | attacker wins | engine labels | mean a% / d% |
|---|---|---|---|
| **3 v 3** (realm-sized) | **0.0%** | Failure 200 | 0.029 / 0.028 |
| **6 v 2** (largest realm muster against a small one) | **0.0%** | Failure 200 | 0.059 / 0.017 |
| 200 v 200 | 45.0% | Success 90, Partial 37, Failure 73 | 0.825 / 0.813 |
| 400 v 400 | 44.0% | Overwhelming 28, Success 60, Partial 11, Failure 101 | 0.700 / 0.737 |

**Why a realm-sized field is always Lost.** Both sides have hp under 100, so `size = 0` and both rout on tick 1, whatever the blows. Mutual rout
goes to the defender. Seed 0, 6 v 2: `a% = 0.06`, the attacker's full 6 troops / 100 with nothing lost; `d% = 0.0092`; `attacker_wins = False`.

**What it writes.** Under 100 troops a side's share is `Σ weight / 100` before any blow lands, so each loser's body becomes about
`1000 × Σ weight / 100 = 10 × the side's summed weight`. For the 6 attackers that is 1000 → 60 each. Body 60 is below all three band floors, so
that attacker's budget becomes `max(1, 5 + holds − 3)`:

- with no `hold`: 2, which buys 2 acts (one extended scene, or two single ones);
- with one `hold` (the seat): 3, which buys 2 + 1 = 3 acts;
- before the loss, the seat-holder's budget was 6, which buys 9 acts.

Each attacker also gains a grudge row toward the defending faction, and his next morale start is 4. In the other direction, a 250-troop side reads
`2.5 / 2 = 1.25` unhurt, so a losing side's body could grow.

### 3.2 Engineered advantages

**Season-shaped**, 400 v 400 unless stated:

| change | attacker wins | vs 44.0% |
|---|---|---|
| 400 v 200 | 66.0% | +22 |
| 200 v 400 | 25.0% | −19 |
| WALLS (defender DR 1 → 4) | **29.0%** | −15 |
| UPHILL | 39.5% | noise |
| RIVER_CROSSING | 41.0% | noise |
| attacker stance −2 (morale start 3) | 43.5% | no measurable change |
| defender stance −2 | 44.5% | no measurable change |

**Engine-direct.** These use `systems/mass_battle/sim/engine.py::build_unit`, with tier 3 (400) unless stated, deployment rows 34 and 15, and
baseline P4 C4 D5 M5 DR1. "A wins" uses the season rule; the engine winner column gives the engine's own counts.

| A's change (B baseline) | A wins | engine winner A / B / draw | mean A% / B% |
|---|---|---|---|
| none | 43.5% | 28 / 26 / 146 | 0.91 / 0.92 |
| tier 4 (800) v tier 3 (400) | **70.0%** | 94 / 0 / 106 | 0.97 / 0.79 |
| power 5 | 54.0% | 45 / 22 / 133 | 0.91 / 0.88 |
| knights_templar 5/6/6 v heavy infantry 4/4/5 | 53.5% | 34 / 7 / 159 | 0.94 / 0.90 |
| DR 2 | 47.0% | 28 / 7 / 165 | 0.93 / 0.92 |
| GappedLine | 46.0% | 36 / 21 / 143 | 0.92 / 0.90 |
| stance hold | 45.5% | 0 / 0 / 200 | 0.97 / 0.97 |
| morale 2 | 43.5% | 29 / 50 / 121 | 0.90 / 0.92 |
| command 2 | 43.5% | 28 / 26 / 146 | 0.91 / 0.92 |
| **command 0** | **0.0%** | 0 / 200 / 0 | 1.00 / 1.00 |
| stance aggressive | 42.0% | 34 / 44 / 122 | 0.88 / 0.91 |
| discipline 2 | 37.5% | 1 / 5 / 194 | 0.94 / 0.96 |
| Arrowhead (no charge instruction) | 36.0% | 3 / 10 / 187 | 0.92 / 0.95 |
| **tier 4: Line v Line** | 47.0% | 47 / 50 / 103 | 0.88 / 0.89 |
| **tier 4: Column v Line** | 44.0% | 9 / 13 / 178 | 0.91 / 0.93 |
| heavy infantry 4/4/5 v levy 1/1/2 | 0.0% | 0 / 0 / 200 | 1.00 / 1.00 |
| levy v heavy infantry | 0.0% | 0 / 0 / 200 | 1.00 / 1.00 |

**Reading the table.**

- **Numbers and walls dominate.** Doubling the troops or adding +3 DR shifts the win share by 15-26 points; power +1 and the knights preset by
  about 10.
- **Command** is not in the pool (`exchange.py:103-124`), and `reform_check` needs command ≥ discipline + 1. So command 2 matches the baseline
  draw for draw, and only command 0 acts.
- **Column at tier 3 is the same footprint as Line.** A 5 × 5 square transposed is itself (`geometry.py:21-33`; measured, identical 25 cells), so
  that arm tested nothing. At tier 4 (a 7 × 5 Line against a 5 × 7 Column) the win share does not move beyond noise (44.0% v 47.0%), but routs
  fall sharply: 178 draws v 103. A deep column fights a slower, less decisive battle.
- **Morale start**: no measurable effect on win share in this one single-subunit configuration. Rout counts do shift (29 / 50 / 121), so this is
  a null on one setup, not a rule that morale is inert.
- **Low discipline and contact.** In heavy infantry v levy, and in discipline 2 v 2, the armies never meet. Traced with seed 0
  (`t04_trace.py`), the fronts start 15 rows apart:

  | arms | rows closed in 18 ticks | per tick | contact |
  |---|---|---|---|
  | D5 v D5 | 1 per tick each | about 2.0 | about tick 8 |
  | hold v balanced | 15 (B alone, at 1.0 per tick) | about 1.0 | tick 15 |
  | D4 v D1 | 12 (A 9, B 3) | about 0.67 | none (gap 2 rows at tick 18) |
  | D2 v D2 | 6 (3 + 3) | about 0.33 | none |

  So contact does track the measured closing speed. Units below discipline 5 move slower than the nominal 0.7/0.4 multiplier; why, beyond the
  cohesion factor, I did not trace. With no contact, the tie goes to the defender.

### 3.3 Why no field is fought in the seeded realm, and what happens when one is

Two kinds of run, kept apart (defined in §0 Status). **Natural play**: the shipped chooser forms every act. **Callback play**: a client hands a
person's act in, or a test hand-builds it.

**Natural play** (`t04_probe_march.py` over `build_realm(seed)`, two seasons; re-run at `51d7b05` with the same counts):

- **Seed 0.** 25 `march` acts were formed. 4 failed the typed cell at RESOLVE (`exists:Rung = 0`: the subject was a person id) and are not in
  ctl's "attempted". 21 were declared: 16 at `person` Rungs, 3 at `hearth` Rungs, and 2 whose subject did not resolve to a Rung after the run.
  All 21 were refused at ENCOUNTER.
- **Seed 1.** 10 were declared: 6 at `territory` Rungs, 3 at `person` Rungs and 1 whose subject did not resolve. All were refused.
- **Seed 2.** 4 were declared: 3 at `territory` Rungs and 1 whose subject did not resolve. All were refused.
- **No act at seeds 0-2 targeted a settlement.** Natural play at these seeds fights no field: every march is a declared act at a non-settlement,
  then refused with an empty army.

**Callback play** (nothing the chooser formed; run at `51d7b05`):

- **An opposed field.** A hand-built `march {subject: set_s_036}` by `p_npc_033` via `off_npc_033` (Crown, home settlement `set_s_014`; the pair
  `test_march.py:82-136` uses), folded through RESOLVE and ENCOUNTER on `build_realm(0)`, `(1)` and `(2)`, gives `march.declared` then `field.lost`.
  The attackers are `p_npc_033` and `p_npc_035` (Σ weight 2) against 6 (Σ 6, Church of Solmund); `fortification_of(set_s_036)` is 1.0, so WALLS.
  Each attacker's body goes 1000 → 20 and gains `(fac_church_of_solmund, −1, 1)` and `(fac_crown, −1, 1)`; the defenders are untouched; each
  attacker's `budget()` falls from 6 to 3. The same act handed in by `dispatching_chooser` inside one full season, with everyone else on the shipped
  chooser, gives `field.lost` once at each of the three seeds.
- **An unopposed march.** The same actor and seat to `set_s_003` (Crown-held; none of the holder's people mustered there) gives `march.declared`,
  `field.unopposed` and `army.arrived`; both attackers arrive and their bodies stay at 1000 (all three seeds).
- **A chooser-formed act.** `test_march.py:368-456`: the real chooser forms `march` when a constructed `Question` names `set_s_036`, and the fold
  gives `field.lost`. That chooser is restricted to `march` (`verbs=frozenset({"march"})`), so it does not show that the unrestricted chooser would
  rank the act first (§8 trap 1).
- **A Won field has not been fought.** `test_march.py:254` exercises Won through a constructed `Resolution`; its own note is that the reverse
  pairing (6 attackers against 2) still resolved Lost, because corpus-scale forces rout on contact.

The largest realm muster is 6 weight (`set_s_036`, Church of Solmund). The next is 5 (`set_s_001`, Crown), and the other 26 non-empty musters are 2
or 1. So every opposed field would be Lost (§3.1), and WALLS, because all 37 settlements are fortified. One pair was run; for every other pair
that is inference from §3.1 and these musters, not a run.

## 4 What you can do

There is **one act**. Defence is not an act: it is a state, being present.

| act | who | prerequisites | cost | outcome by band | writes |
|---|---|---|---|---|---|
| **`march`** | a seated person whose office grants `remit:dispatch` (in the shipped build, every seated office, by the `remit_default` test fixture) | typed: the subject is an existing Rung. At ENCOUNTER: the subject is a `settlement`, and your faction has members mustered under your home's settlement who are not already under the target | one scene action within the budget (§0); each mover gains a travel leg (−1 budget) | **Declared**: nothing. **Unopposed**: your mustered members arrive. **Won**: the defenders are scaled and given rows; you arrive. **Lost**: you are scaled and given rows; you stay at your origin. Marching on a place you already stand under: refused | Won: losers' `Person.body`, `Person.stance`; movers' `Tenure.until/since`, `Person.travel_leg`. Lost: body, stance. Unopposed: tenures, legs. Events: `march.declared`, `field.won`, `field.lost`, `field.unopposed`, `army.arrived`, `march.refused` (`VT:814-829`) |

**Engine-direct (Python only, not an in-game act).** You set every option in §1 yourself and call `run_battle`, `build_unit` or `build_army`.
`run_multi_turn_battle` and `run_multi_unit_battle` add pursuit (`pursuit_damage`, Fast units only, `orch:2549`), recall (`orch:2585`) and feigned
retreat. None of these is reachable from `march`.

## 5 Pursuing goals here

**(a) Goals and how the code represents them.**

| goal | represented by | not represented |
|---|---|---|
| take a place | Won or Unopposed: your people are relocated under the target (`contain` Tenures, travel legs) | title (`hold`) moves only by `seize`, `give`, `release` or death |
| break an army | Won: defenders' bodies scaled; grudge and morale rows | deaths by name (body floored at 1), pursuit, prisoners |
| defend | nothing you do: being a present member of `holder_faction_of(target)`, behind garrison condition > 0 | any defender choice; the defender has no chooser |
| deter | nothing | a show of force has no act |

**(b) The honest plays.** A commander's real options are **march, or nothing**.

1. **March where nobody can oppose you.** The target is a settlement whose `holder_faction_of` is your faction or None, or whose holding
   faction has nobody present. No engine call is made and you arrive. You must not already stand under the target, or the act is refused.
   This is the only march the rules reward.
2. **March into an opposed field.** Today this is a certain loss: both sides are under 100 troops, so both rout on tick 1, and a mutual rout
   goes to the defender. It costs each attacker body down to 10 × the side's weight, and 2-3 acts a season afterwards.
3. **Do nothing.** Not marching dominates play 2.

Prepare by being where the army is. Attackers are counted at your home settlement, so the only way to raise "army size" is to have more of
your faction's members living there. Nothing lets you choose formation, stance or troop type.

**(c) Costs, risks, counter-play, what blocks you.**

- **Blocks**:
  - a seat granting `dispatch`;
  - a settlement target;
  - members at home;
  - in the realm, the chooser never forms the act on a settlement (§3.3).
- **Walls** never decay: garrison wear is 0 (`RY:1451-1470`).
  - `sabotage` lowers a `Site.condition` when its actor stands at the Site (`VT:1030-1035`), and `restore` raises it.
  - A fortification of 0 would make the river and polygon rows reachable, but no measured seed did this.
  - A hearth made by `found` gets no Sites (`loop/effects_founding.py:109`); whether a founded settlement would, I did not check.
- **Counter-play**: the defender's only counter is presence. Walls apply automatically.

**(d) What the rules reward and punish.**

- An opposed march is a dominated option at realm scale.
- Summed weight is the only army input that varies.
- Ties, mutual routs and no-contact draws all go to the defender, so attacking is penalised even at engine scale (about 44% between equal
  armies).
- The winner pays nothing except the travel leg.

**(e) What success leaves in the world.**

- Your people stand under the target, each with a travel leg (−1 budget).
- `army.arrived` is witnessed.
- If you won, the defenders keep reduced bodies, a grudge toward your faction and a lower next morale start. The grudge rows feed the chooser's
  stance toward your faction.
- Nothing records the place as yours.

## 6 How it connects

| subsystem | you draw from it | you feed into it |
|---|---|---|
| Governance (GV) | the seat and its `remit:dispatch` (from the test fixture); garrison condition through `fortification_of`; `sabotage` and `restore` on Site condition | nothing (no title, no Site write) |
| Factions (FA) | `holder_faction_of(target)`; `seat_faction(a.via)`; membership through `commit` | grudge rows toward the winning faction |
| Persons / NPC life (NP) | `Person.weight`; stance rows (morale start); loyalty (gain 0) | losers' body (budget bands) and stance rows, which the chooser reads |
| World / travel (WT) | home and containment (where an army musters) | relocation through `_relocate` (`loop/effects_migration.py`); travel legs |
| Personal combat (PC) | nothing | the same `Person.body` that duels wound |
| Information (FI) | nothing in battle | `field.*` and `army.arrived` events, fanned out by WITNESS |
| Threadwork (TW) | nothing: `threadwork_check` is empty (`orch:333`) | nothing |

**Combinations.**

- `march` then `seize` is the "take a place" sequence: the march moves presence, `seize` moves title.
- `forgive` is, with `march`, the only runtime writer of `Person.stance` (`EC:426`). It is the counter to accumulated grudge rows.

## 7 Playing it as proposed

All of the following is **[PROPOSED]** (`proposals/2026-10-16-verbs/…-10-lexicon-mass-battle.md` and the v9 remediation plan). Nothing here
executes. Where a lexicon's body and its rulings disagree, the rulings (verbs-03 §III.5) govern. Gap-register ids name gaps, not built rules.

**Getting a field fought.**

- **REM-27** (RB-2b) gives `march` the setting `referent_class: Rung`, so the chooser is offered only settlements in `march_target_kinds` that the
  marcher has been told of. Its own risk note: a Won or Lost field still needs "a defended settlement of another faction in a marcher's ledger".
- **REM-32 / JQ-4** injects one weight-to-troop conversion (a `hole_register.yaml` NUMBER row, Jordan's), shipped at a value equal to today's
  behaviour. For an opposed field to be winnable at all, the conversion must lift a side to **100 troops or more** (§2.1 step 6), not 80.

**Raising and keeping forces** (Suite 1; waits on M-2, a recruit pool and graded troop stock, and M-8, the costs of raising):

- `levy`: raise by obligation, costing consent (a cohort stance row). By R-01, coin recruitment is a terms parameter of `levy`; `recruit` the
  word goes to FA.
- `muster`: move stock between places in your purview; it absorbs `garrison`.
- `drill`: raise a stock's grade, capped below the top (J-5 (c)); cost OPEN.
- `disband`: return troops to the pool.
- Default service and pay: no term, no upkeep.

**Ordering the battle** (Suite 2; waits on M-3, an `order_of_battle` Record):

- `marshal` writes formation, stance, roles, who leads and the reserve release, so the engine's options in §2.3 would reach the season.
- Its contents:
  - `rally` fills `rally_check`: a Command pool against Ob 2 restores a fraction of lost morale (M-4);
  - `pursue` reaches `pursuit_damage` (M-4; deaths by name M-7, K-MB-9);
  - `retreat`, including the feigned form (M-5, R-7);
  - `withstand` (hold and brace);
  - the reserve release replaces `RESERVE_COMMIT_TURN = 2`.
- `command` is a stat (`derive_command`, M-10), not a verb. This would give the defender a chooser.

**Campaigning** (Suite 3; waits on M-1, a field force that travels with its marchers, which amends ratified Layer 1 and rides J-1, Jordan's):

- `march` gains postures: `storm` (walls graded by condition, H-150) or `besiege` (a siege state, M-6).
- `supply` (`provision`, and `equip`, which waits on M-11).
- `forage`, with `sack` only after a `storm`; MB's by R-08, with `sack`'s tone held for Jordan.
- `encamp` is WT's and parked (R-08).
- `reconnoitre` and the MB half of `ambush` are PARKED.

**Ending a war** (Suite 4): `surrender` (MB's by R-19) emits `place.surrendered`; `raze` is GV's (R-03).

**Open decisions.**

- Does a march require war? (K-MB-5 / MB-G15, "two games".)
- The death policy (J-C-19).
- Winners' wounds and experience (J-C-4).
- Whether a player may command a field (J-C-31).
- Grading on one margin (K-MB-8).
- The mutual-rout tie-break (MB-G38).

**Stubbed or inert today.**

- `rally_check` and `threadwork_check` are empty (`orch:288-290, 333-335`).
- `tactic_cards.py:33` is an empty dict, and `altonian_reinforcements.py:21` raises `NotImplementedError`. Both are under
  `systems/mass_battle/sim/`.
- Equipment is unwired except reach.
- Forest and river speed effects are inert; NARROW_PASS applies nothing.
- `field_morale_loyalty_gain = 0`.
- Every declared realm `march` is refused.

## 8 Common mistakes and traps

1. **"`march` 21/21 means fields were fought."** The "ok" is the `Declared` event. Field events are 0 at seeds 0-2.
2. **"`troop_type='infantry'` gives infantry stats."** Stats apply only through `Subunit.of_type`, and `infantry` has no preset. The season army
   is P4 D5 M5 by Unit defaults.
3. **"The loser's body scales by the survivor share."** It scales by `effective_size / size_max`, with `size_max` floored at 100 troops. Under 100
   troops this is `Σ weight / 100` unhurt (6 → 0.06, so body → 60). Above, it can exceed 1 (250 → 1.25).
4. **"Armies rout below 80."** A one-subunit army routs when hp falls under 100 (`size = 0`), checked every tick before the 80-troop subunit
   floor. At realm weights both sides rout on tick 1, and mutual rout goes to the defender.
5. **"A lost field kills."** Not under the default `scaled_by_degree` setting (body floor 1). Only `total` kills.
6. **"Winning takes the place."** It moves presence only; `seize` moves title.
7. **"The season deploys two armies."** Both are built from one position dict, (8, 12), and a 200-troop side occupies that one cell on both
   sides.
8. **"Defend is an action."** It is not. The defenders are whoever of `holder_faction_of(target)` is present.
9. **"The defending faction is the settlement's holder."** Seeded settlements are not held directly. `holder_faction_of` walks up to the nearest
   held Rung, usually the territory, so the "defender" is the territory holder's faction.
10. **"Morale and command do not matter."** Command is outside the pool and matters only at 0. The morale-start null is one configuration's
   result over 200 seeds, not a rule.
11. **"Discipline only scales speed by 0.7 or 0.4."** Measured closing is slower than that (D4 about 0.5 per tick, D1 about 0.17 per tick, seed 0). Also, the comment
   at `units:1847` says "disc3 → 0.4" while the code at `:1823` gives 0.7 at discipline 3. The code wins.
12. **`cfg:108`**: `MB_CELL_MORALE` is commented "RETRACTED to OFF", but its default is `'1'`, on. **`CLAUDE.md` §5** names
   `engine/autoload/dice_engine.py`, which does not exist. The engine's ladder is a local copy (`resolution.py:104`), held equal by a test.
13. **Draft A3 corrections:**
   - (i) LOC: errata G14 gives 10,154 + 3,089, not "~13,500".
   - (ii) A3 called MB-G35 ("every realm field is WALLS") stale. On a fresh realm it holds: 37 of 37 settlements are fortified, and the river
     check runs only at `fort_level ≤ 0`.
   - (iii) A3 did not say why marches are refused; §3.3 does.
   - (iv) Per errata C2, morale start and a terrain row also vary on the season path.
   - (v) Per G5, the field reads `attacker_wins`, not the margin ladder.
   - (vi) Per G19, R-01, R-03 and R-08 govern; they are not open conflicts.
   - (vii) Seed 2 added: 4 declared, 4 refused, 0 fields.

**§8 Round-2 corrections** (audit K_T04, CROSS, L). I opened each cited line before accepting.

- **F1, accepted** (`units:2930-2938`; `orch:2205-2206, 2262-2268`): the binding rout line is 100 troops. This changes §1, §2.1 step 6,
  §3.1, §5b and §7 (REM-32 must clear 100).
- **F2, accepted** (`sides.py:131-132`): a same-faction field cannot happen, because `subject` is None and the result is Unopposed. I removed my
  "−2 morale in a same-faction field" claim. The H-151 note in `MB.py:139-142` is stale.
- **F3, partly disagreed.** The auditor read contact as non-monotone in nominal closing speed (4 v 1 is 0.7 + 0.4 = 1.1, more than hold v
  balanced at 1.0). My seed-0 trace shows the measured closing for 4 v 1 is about 0.67 rows a tick, below the 1.0 of hold v balanced. So contact
  is monotone in actual closing speed. The cause is distance not covered in 18 ticks. Why the measured speed falls below the multiplier is
  untraced.
- **F4, accepted.** The tier-3 Column arm was void: the footprint is identical. I replaced it with a tier-4 arm (fewer routs, win share
  unchanged). Command is explained by `exchange.py:103-124` and `orch:318-328`.
- **F5, accepted** (`cfg:307-308`; `orch:1377-1378`): added the WALLS mechanism, Overwhelming-only damage.
- **F6, accepted in part:** wear 0 (`RY:1451-1470`); `sabotage` lowers condition (`VT:1030-1035`). The `found` point is narrowed:
  `effects_founding.py:109` speaks of a founded hearth.
- **F7, accepted** (`RY:324-334, 376`; C4): dispatch comes from the test fixture, and the roster's open/closed status contradicts itself.
- **F8, accepted** (`resolve.py:787-788`): the empty army is refused before the provider.
- **F9, accepted**: the terrain constants are at `terrain.py:45-50`.
- **F10, accepted** (`EC:257-263`): marching on a place you already stand under is refused.
- **F11, accepted** (`state.py:90-117, 228-237`): one discipline step per boundary, a 2.1 morale cap and an exhaustion term.
- **F12, accepted**: body → 10 × the side's summed weight.
- **F13, accepted**: seed 1's tenth act was a subject that did not resolve.
- **F14, accepted**: comment and code mismatch, trap 11.
- **X1 / C1**: the budget arithmetic is re-done in acts.
- **X11**: holds, not offices.
- **X22**: `holder_faction_of` walks up; trap 9.
- **L's teaching notes**: I defined Rung and Tenure in §0; §4 now lists one act; §5b is restated as march-or-nothing; §2.3 is new.

## 9 Checks

- **Opened**:
  - `MB.py:60-305`, `SW:100-273` and `loop/sides.py:1-144`;
  - `EC:183-348` (`_not_yet_under` 333) and `loop/encounter.py`;
  - `loop/resolve.py:780-788`;
  - `VT:803-834, 1030-1036`;
  - `RY:312-335, 374-378, 890, 918-931, 1278-1298, 1451-1470, 3034-3360`;
  - `world_q.py:1470-1510, 1656-1680`;
  - `decision/budget.py:18-75`;
  - `units.py:700-760, 1785-1850, 2928-2940`;
  - `orch:285-292, 318-330, 1374-1380, 2198-2270`;
  - `core/exchange.py:100-126` and `core/state.py:90-118, 228-238`;
  - `cfg:305-309` plus a grep of the constants;
  - `MM/troop_types/registry.py:30-60`, `MM/geometry.py:21-39` and `MM/terrain.py:45-50, 272-289`;
  - `seam/ladder.py:185-197` and `systems/mass_battle/sim/engine.py:176-212`;
  - `loop/effects_founding.py:105-111`.
- **Ran** (all `python -I`, under ):
  - `t04_field.py`: season-shaped, 11 arms × 200 seeds;
  - `t04_engine.py`: engine-direct, 15 arms × 200 seeds;
  - `t04_engine2.py 30`: discipline contact;
  - `t04_trace.py`: row positions by tick, seed 0;
  - `t04_column.py`: tier-4 Column, and command 0;
  - `t04_probe_march.py 0` and `1`: march targets and refusals;
  - footprint check: tier-3 Line and Column give the identical 25 cells, rows 34-38, columns 25-29;
  - a one-off: 6 v 2 seed 0 gives `{False, 0.06, 0.0092}`, body → 60;
  - a realm measurement on `build_realm(0)`: weights, bodies, musters (top 6 and 5), fortified 37 / 37, dispatch 25 / 32, band floors 800 / 500 / 100.
- **Ran** `python -m pytest engine/season/tests/test_mass_battle_provider.py -q`: 11 passed.
- **Read**: the `ctl/` files; `audit/ERRATA.md`; `audit2/CROSS.md`, `K_T04.md`, `L_cross_tutorial.md`.
- **Not confirmed**:
  - why measured closing speed falls below the discipline multiplier;
  - what the 3 unresolved march subjects were;
  - whether a settlement founded by `found` carries a garrison Site.
