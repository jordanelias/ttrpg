# The troop stock: a settlement's recruit pool, conscripted companies, and the season's order of battle

## Status: PROPOSED (2026-10-16). Corrected the same day against an independent critic's report and re-based on Jordan's ruling of the same day (below). The reconciliation table is at the end of `_part2`. Not ratified; merge ratifies nothing unless Jordan so rules.
## Lane: MB (the field and the army builder), SE (the recruit pool and the conscription), FA (assembly), IN (the verb row, the gate, the registries). IDs: none allocated.
## Read at the working tree of 2026-10-16, after the `levy` → `requisition` rename (uncommitted when first drafted; the tree is clean at the correction pass, `git status --short` empty [RAN]).
## Parts: this file (head, §0–§3) · [`_part2`](2026-10-16-troop-stock-design_part2.md) (§4–§10 and the critic reconciliation), read in that order.

**Reference, not mechanism (CLAUDE.md §0.05).** Nothing here changes how the game behaves. Every
behaviour below becomes true only when the code in §7 is built and a run shows it. Where this document
and code disagree, the code is right and this document is wrong. Locators are `file:line` in the tree
as read.
- **`[CHECKED]`** means the line was re-opened in the correction pass.
- **`[CHECKED-draft]`** means it was opened at drafting and **not** re-opened in the correction pass.
  The critic's report confirms most of these, but that is the critic's reading, not mine.
- **`[RAN]`** means I executed something and quote what it printed.
- **`[INFERRED]`** means I reasoned from lines I opened but ran nothing.
- **`[UNVERIFIED]`** means I did not open it.

**The troop verb's name in this document is `conscript`** (§3.1). It is a working name, not a claim.
The old store act's name, `levy`, is the word Jordan used, and reusing it collides with live text in
three registers. The collision, and the follow-through reuse would need, are in J-3 (§9).

**Demands (D1, Jordan, 2026-10-16, verbatim, from the session brief):**
- **(1)** "mass battle is supposed to be based on army units that are troops levied from settlements
  as their own resource, and these troops are supposed to differ in quantity and quality based upon
  equipment and experience and their commanders etc"
- **(2)** "this 4/4 one line formation for one unit for mass battles as coded is a stub"
- **(3)** "factions are supposed to be able to assemble armies with different subunits with
  subformations"
- **(4)** "levy typically doesn't refer to goods/stores. that verb is wrong as currently used"

**Ruling (R-POOL, Jordan, 2026-10-16, verbatim, relayed by the coordinator):** "settlement cohort
should not be reduced by troops being raised. available troops to raise should be derived from [the
settlement] with its own value that replenishes over time."

Demand (4) is met by the rename already in the tree. The name `levy` is free as a verb row, but not as
a word in the registers: `engine/season/requirements.yaml` still uses it 23 times and
`hole_register.yaml` 19 times for the store act (`grep -c levy`) [RAN]. So this design does not
reuse it by default (J-3).

---

## 0. VERDICT

1. **Each settlement holds a recruit pool: a store of men it can still raise.**
   - **Where it lives:** a new matter kind, `recruits`, in the settlement rung's `Rung.stores`. It
     composes on the stock that exists, through the `(Rung, stores)` write-matrix row, which already
     admits MATTER and RESOLVE (`write_matrix.yaml`, the `Rung`/`stores` row) [CHECKED]. It adds no
     carrier field and amends no Layer 1 line (§2.1).
   - **What it derives from:** a ceiling read from the settlement's own people, `recruit_ceiling(w,
     rung)`. That is the weight of the resident cohorts under the settlement that serve no seat,
     times a share fixture (§2.2).
   - **How it replenishes:** at MATTER, beside yield, toward that ceiling and never past it (§2.3).
   - **What raising does:** `conscript` debits the pool and **never writes the population cohort**
     (R-POOL). The cohort's weight and its larder demand are byte-unchanged by a raise.
2. **A troop is a person: a company `Person` minted from the pool, not carved from the cohort.**
   - **What it is:** a cohort `Person` at weight `n ≥ 2`, minted by `conscript` at the settlement,
     resident there, and bound to the conscripting seat by an `oblige` edge.
   - **Layer 1:** `units = PersonId[] at weight -- one type. There is NO unit class, at any scale`
     (`architecture/meta/04_CODE_ARCHITECTURE.md:793`) [CHECKED]. A company keeps that sentence. A
     troop stock or a typed troop row does not (§2.4).
   - **J-1 stays Jordan's** (§9): the troop body under the pool, a company `Person` (default) or a
     troop stock.
3. **What the ruling settles, and what it does not:**
   - **Settles J-2.** The draft's population coupling is answered by R-POOL. Raising takes nothing
     from the cohort, so the draft's split, its `_draft` move and the H-170 problem (critic finding 1)
     all fall away.
   - **Settles one cost the draft lacked.** A company resides and eats from the one larder, so the
     settlement's demand rises by exactly the company's want (§2.5). The levy amount now has a cost:
     food, the pool, and the time it takes to regrow.
   - **Does not settle the troop body.** Candidate D (the cohort itself fights) is ruled out, because
     troop quantity must now come from the pool and not from the cohort. A1, A2 and B are re-compared
     against the pool in §2.4.
4. **⚠ The company form amends one line of ratified Layer 1.** A company has no `commit`, so it is not
   in `members`. Fielding it widens `mustered` beyond §C.5.1's *"the squad is `members ∩
   present-at-rung`"* (`04:802`) and `sides = (faction_q.resolve(proj, A), …)` (`04:792`), which
   resolves to `members` (`queries/faction_q.py:107`) [CHECKED]. The draft's claim that the company
   "complies without amending" is withdrawn. The company amends the muster line. A troop stock or a
   typed row amends the unit-class line instead. That trade is part of J-1.
5. **Quality has three axes, each on an existing carrier. In computed play none is exercised yet:**
   - **Equipment** is matter in the company's own person-rung `stores`. The module derives the troop
     kind from `TROOP_LOADOUT` (`modules/mass_battle/equipment/__init__.py:21-36`) [CHECKED], the one
     owner of kind → kit. There is no second table (§2.7). ⚠ Computed play cannot equip a company
     today. No question names a company's person-rung as a `transfer`'s `to`
     (`verb_table.yaml:1211`) [CHECKED], and arms have no producer (§6).
   - **Experience** is a grade in `Person.capability`. ⚠ `train` writes capability only where a case
     names a vocation (J-13 answered (iii), `workplans/valoria_master_workplan_v9_part5.md:73`,
     `:433`) [CHECKED]. A company has no case, so drill does not reach it, and battle experience waits
     on J-5. **The axis is unreachable in computed play** until J-5 or J-13 changes.
   - **The commander** is the person who holds the seat the company serves. His Command is 4 for
     every season commander until R-C-1 names a source (§4.2 step 5).
   - **In computed play,** then, every company fields as the unarmed kind, at grade 0, under Command
     4. What varies is how many men stand and who commands them. Hand-built and player acts reach all
     three axes.
6. **The verbs:**
   - **One new verb, `conscript`** (a working name; J-3), over a settlement rung.
   - **Reused companion acts:** `transfer` equips a company, `dispatch` and `move` assemble companies
     from several settlements, `march` fields them, and `release` plus the oblige term's maturity end
     their service. `train` would drill them only after J-13 changes.
   - **`requisition`** stays the store act that fills the treasury the kit comes from. It may not move
     `recruits`: a man is not goods (§2.1).
7. **Who stands, and whose morale counts, have one owner.** A new Query, `service_faction`, names the
   one faction a person with no `commit` stands for: the faction his seat's holder coheres under, on
   `holder_faction_of`'s precedent (`world_q.py:1441-1466`) [CHECKED].
   - **Readers:** `mustered` adds those persons, and `_side_stance` reads the same Query. So the morale
     row the fold already writes onto a losing company is read back at its next field (§4.1).
   - **Persons who hold a `commit`** stand only where their `commit` puts them. So the two shipped
     `oblige` edges (NPC-070 and NPC-041) add nobody to any side [RAN, §4.1].
8. **The army builder moves across the seam.** `build_army` moves out of
   `systems/mass_battle/sim/engine.py:213-452` into `modules/mass_battle/` [CHECKED-draft].
   - **What is deleted:** the season's one-Line construction: `_weighted_unit`,
     `_MVP_SUBUNIT_SHAPE`, `_MVP_UNIT_COMMAND`, `_SEASON_FORCE_POWER` and `_MIN_TROOPS`
     (`modules/mass_battle/massbattle.py:170-230`) [CHECKED-draft].
   - **What replaces it:** the host builds each side's order of battle, **one subunit per company**,
     and the module builds the Unit through the one constructor (§4).
9. **A defect tracked on its own, gated on nothing here (TS-2, §7):** `build_army` throws away the
   morale preset of every troop type it builds.
   - **Probe [RAN at drafting]:** a `build_army` spec for a `levy` subunit printed `levy power 1 disc
     1 morale 6`.
   - **Expected:** the preset row is morale 2 (`modules/mass_battle/troop_types/registry.py:41`)
     [CHECKED].
   - **Cause:** `build_army` sets `kw['morale']` to the Unit's default when the spec sets none
     (`systems/mass_battle/sim/engine.py:427-428`). That runs before `Subunit.of_type`'s
     `kw.setdefault('morale', preset['morale'])` (`modules/mass_battle/hierarchy/units.py:726`) can
     [CHECKED]. It contradicts `build_army`'s own docstring: a canonical type "draws its §B.2
     Power/Discipline/Morale presets via Subunit.of_type unless the spec overrides them"
     (`engine.py:228-230`) [CHECKED].
   - **Consequence:** on the harness path, troop-type morale is dead. Every harness-built army fights
     at Unit morale 6.
   - **Not tracked anywhere:** a grep for the pattern over `engine`, `registers`, `workplans` and
     `references` finds no row [RAN].
10. **What this cuts:**
    - **IN-52's feed and LF-1..LF-3 are withdrawn.** A company eats from the one larder at home, so a
      field ration from a treasury would feed the same mouths twice (§5).
    - **IN-49 is re-framed** as the store act's question source.
    - **Closed:** H-49 (a runtime writer for `Person.weight`) and MB-08's #445 U-1.
    - **Research rows it closes:** M-MB-2, M-MB-6, M-MB-15, M-MB-17, M-SE-9, M-FA-10, M-IN-12,
      M-IN-13 and M-PC-12 (the cohort half).
    - **Research rows it narrows:** M-MB-1, M-MB-3, M-MB-16 and M-NPC-13 (§5 says how far).
    - **Collisions it resolves:** X-2 (by a pool on the rung and persons in the field) and X-19 (by
      cutting the bound, against MB's keep).
11. **Grade: paper.** Nothing in §2–§4 is built.
    - **Probes run at drafting:** the morale preset (item 9).
    - **Probes run in the correction pass:** the shipped `oblige` edges' factions (§4.1); the realm
      built with every cohort at weight 4, used for the pool's falsifier fixture (§2.2).
    - **Where next:** §7 gives the build order, and each step's exit is an execution artifact.

---

## 1. THE PROBLEM AS CODED

Each fact below is at its source. Together they answer the four demands against the tree.

### 1.1 Who fights a season field

1. **A field's two sides are faction members present at a place.**
   - **Attacker:** `sides_of` musters the attacking side as `mustered(w, origin, faction)`. `origin`
     is the actor's nearest settlement, and `faction` is the faction of the seat the act was
     exercised through, converted by `faction_prop_id` (`engine/season/loop/sides.py:77-85`)
     [CHECKED].
   - **Defender:** the provider musters `mustered(w, rung, subject)` at the target
     (`engine/season/seam/wrappers/mass_battle.py:233`) [CHECKED-draft].
   - **What `mustered` reads:** "This faction's members present in `rung_id`'s subtree"
     (`engine/season/queries/world_q.py:1256-1272`) [CHECKED]. Membership is a live `commit`, and
     "THIS IS THE WHOLE OF MEMBERSHIP AND THERE IS NO SECOND ROUTE" (`world_q.py:1151-1162`)
     [CHECKED-draft].
2. **The population never fights.**
   - **No commit:** the territorial population is one cohort `Person` per settlement, seated with "No
     `commit`, so it is no faction's member" (`engine/season/harness/populated.py:394`)
     [CHECKED-draft]. It is minted as `Person(pid, "the people of …", weight=wt)`, with `contain` and
     `reside` both on the settlement rung (`populated.py:439-442`) [CHECKED].
   - **No size:** its weight is 2 at all 37 settlements. That is the smallest weight S9 calls a
     cohort, "chosen AGAINST inventing a spread" (`engine/season/hole_register.yaml:3722-3732`, H-170;
     `engine/season/cohorts.yaml`, 37 rows) [CHECKED].
3. **A side is its members' summed `Person.weight`.**
   - **The input:** `field_input` passes `weights = (tuple(w.persons[pid].weight …), …)`
     (`seam/wrappers/mass_battle.py:190-193`) [CHECKED-draft].
   - **The record:** the input record carries `weights`, `territory`, `fort_level`, `stances`,
     `walls_dr`, `origin`, `loyalties`, `loyalty_gain` and `geography`, and nothing about
     composition, kit or command (`engine/season/queries/inputs.py:62-100`) [CHECKED-draft].
4. **A person's weight never changes after construction.**
   - **Matrix row:** `(Person, weight)` is stepped `[CEN]`, class `MATTER`
     (`engine/season/write_matrix.yaml:240-246`) [CHECKED-draft].
   - **Register:** H-49 records "There is no runtime writer" (`hole_register.yaml:558-568`)
     [CHECKED-draft].
   - **Carrier:** `Person.__post_init__` refuses `weight < 1` (`state/carriers.py:709-711`) [CHECKED].
   - **Consequence:** a defeat cannot make a body of people smaller.

### 1.2 What the module builds from that

5. **Every side is one Line subunit of bare `infantry`, at power 4, command 4 and discipline 5.**
   - **The constants:** `_MVP_SUBUNIT_SHAPE = dict(shape='Line', troop_type='infantry', tier=2,
     starting_position=(8, 12), advance_dir=1, stance='balanced', unit_type='melee')`
     (`modules/mass_battle/massbattle.py:170-178`); `_MVP_UNIT_COMMAND = dict(command=4,
     discipline=5, discipline_start=5)` (`:182-186`); `_SEASON_FORCE_POWER = 4` (`:196`)
     [CHECKED-draft].
   - **Their own label:** "minimum-viable defaults … no canonical spec exists for army -> Unit
     construction of ANY kind" (`:160-166`). The module header says `[GAP: faction -> unit
     construction lacks canonical spec …]` (`:32`) [CHECKED-draft].
   - **Demand (2) rules this a stub.**
6. **Troops are the raw weight sum.**
   - **The code:** `Subunit(**_MVP_SUBUNIT_SHAPE, troops=max(float(weight), _MIN_TROOPS), …)`
     (`massbattle.py:226`), with `_MIN_TROOPS = 1.0` as a crash floor (`:208`) [CHECKED-draft].
   - **The module's own disclosure:** it does not invent a conversion: "this module is not the place
     to invent one" (`:198-207`) [CHECKED-draft].
   - **The rout floor:** `SUBUNIT_ROUT_FLOOR = 80` (`modules/mass_battle/config.py:117`)
     [CHECKED-draft].
   - **The MB lane's probe:** 0 attacker wins in 20 at ≤80 troops, with both sides routed every run
     (`research/by_lane/MB_mass_battle.md:434`, M-MB-1) [CHECKED as a citation; not re-run].
7. **Morale is the only side quality that reaches the field, and its reader sees members only.**
   - **The feed:** each side's mean stance toward its own faction feeds `_morale_start`
     (`massbattle.py:119-157`) [CHECKED-draft].
   - **The reader:** `_side_stance` weights by `Person.weight` and finds each person's faction through
     `world_q.faction_holding` (`seam/wrappers/mass_battle.py:126-148`) [CHECKED]. That reads live
     `commit` edges only (`world_q.py:1436-1438`) [CHECKED]. A person with no `commit` contributes 0.

### 1.3 What the harness can build, and the season cannot reach

8. **A composite army constructor exists, on the wrong side of the seam.**
   - **What it takes:** `build_army(specs, name, faction, *, power=4, command=4, discipline=5,
     morale=6, …, officers=())` (`systems/mass_battle/sim/engine.py:213-452`) [CHECKED-draft]. Each
     spec sets its own shape or role, `troop_type`, `troops`, quality overrides and an `officer`.
   - **What it checks:** roles are gated by `role_allowed` (`:369-371`). Officers' spans and the
     general's direct reports are checked against Command and `SUBUNIT_CAP = 11` (`:99`,
     `:304-345`) [CHECKED-draft].
   - **How subunits are built:** each one goes through `Subunit.of_type` (`:448`) [CHECKED-draft].
   - **Why the season cannot call it:** `modules/mass_battle/` imports nothing from `systems/`. The MB
     lane records a grep returning 0 (`MB_mass_battle.md:368`, T-MB-19) [CHECKED-draft as a
     citation]. `systems/mass_battle/sim/engine.py` itself star-imports `modules.mass_battle.*`
     (`:6-26`) [CHECKED-draft], so the dependency runs one way only.
9. **Troop-type quality presets exist, including a `levy` row.**
   - **The table:** `TROOP_TYPE_STATS` (`modules/mass_battle/troop_types/registry.py:39-57`)
     [CHECKED]. Its `levy` row is power 1, discipline 1, morale 2 (`:41`).
   - **How a preset is applied:** `Subunit.of_type` fills power, discipline and morale from it
     (`hierarchy/units.py:712-730`) [CHECKED-draft].
   - **Melee or ranged:** `unit_type_for` derives it from the type's weapon
     (`registry.py:151-159`) [CHECKED-draft].
   - **Off the season path:** none of it is reached there.
10. **The morale preset is dead even on the harness path** (§0 item 9). The default at
    `engine.py:427-428` pre-empts the `setdefault` at `units.py:726` [CHECKED]. DG-4 meant to give
    each subunit its own morale instead of `None` (`engine.py:410-426`) [CHECKED-draft]. It did not
    mean to overrule the preset.
11. **Equipment is a catalogue, wired only into `unit_type`.**
    - **The catalogue:** `ARSENAL` (weapon classes) and `ARMOURY` (`none/light/medium/heavy`, with a
      canonical `dr_vs_piercing`) are mutable registries seeded at import
      (`modules/mass_battle/equipment/weapons.py:29-49`, `armour.py:29-42`) [CHECKED-draft].
    - **The loadout table:** `TROOP_LOADOUT` names each troop type's weapon and armour
      (`equipment/__init__.py:21-36`) [CHECKED]. `levy` is `light_cut`/`none`, `cavalry` is
      `heavy_cut`/`heavy`, `knights_templar` is `heavy_blunt`/`heavy`, and `archers` and
      `mounted_archers` share `bow`/`light`. No row names a mount.
    - **The header says "NOT YET WIRED into resolution"** (`equipment/__init__.py:10`)
      [CHECKED-draft]. That is true for DR and speed. `unit_type_for` does read `loadout_for`
      (`registry.py:156`) [CHECKED-draft].
12. **Officers exist and are checked at construction only.**
    - **The class:** `Officer(name, command=4, charisma=None, cognition=None)`. It derives `command`
      only when both attributes are given **and** `COMMAND_SIGMA_ENABLED` is on
      (`hierarchy/units.py:2711-2716`) [CHECKED]. That flag reads an environment variable, default on
      (`modules/mass_battle/config.py:530`) [CHECKED].
    - **What reads it:** `Unit.officers` is "Bookkeeping only … nothing at resolution time reads it"
      (`:2793-2797`) [CHECKED-draft], and `Subunit.officer` likewise (`:637-643`) [CHECKED-draft].
    - **What the check does:** `build_army`'s span check reads `Officer.command`
      (`engine.py:304-345`) [CHECKED-draft], so a commander's Command limits how many subunits he can
      field.
13. **Experience has no carrier.** `grep -rniE "experience|veteran|drill|training"` over
    `modules/mass_battle` finds two comments, and over `engine/season` non-test Python finds nothing
    (`MB_mass_battle.md:449`, M-MB-16) [CHECKED-draft as a citation; not re-run].

### 1.4 The verbs and the stock as they stand

14. **`requisition` moves goods, conserved, from a rung into the seat's treasury.**
    - **The row:** eligibility `remit:issue` and `presence:<rung>`, typed `requires` (purview basis
      plus `stores >= amount`), and `writes: ["Rung.stores", "Rung.stores"]`
      (`engine/season/verb_table.yaml:629-663`) [CHECKED-draft].
    - **Refusals, keyed per clause:** `requisition.unauthorized` and `requisition.refused`
      (`:654-659`) [CHECKED-draft].
    - **The effect:** `_eff_requisition` shifts `amount` of `kind` through `_shift`, "the one body of
      every act that moves stores between two rungs -- `transfer` and … `requisition`"
      (`loop/effects_shared.py:117-128`) [CHECKED]. Its two callers are `effects_governance.py:412`
      and `effects_economy.py:219` (`grep "_shift("`) [RAN].
    - **This is demand (4)'s act, correctly named.** It raises no troops.
15. **`march` fights over a place and writes only the losers.**
    - **The row:** eligibility `remit:dispatch`. The only operand is `subject`, a Rung. Writes are
      `Won`/`Lost` → `Person.body`, `Person.stance`. It is graded `ruled` (`verb_table.yaml:664-690`)
      [CHECKED-draft].
    - **The ruling (ED-IN-0279):** a loss writes "casualties only, decrease in morale, and a grudge
      token", and "nothing on the WINNING side" (`:682`) [CHECKED-draft].
    - **Casualties land on `body`, never on `weight`:** `p.body = max(1, int(p.body * max(0.0, pct
      …)))`, and every loser gets `(loser_faction, -1.0, morale_w)` appended to its stance
      (`loop/effects_combat.py:248-261`) [CHECKED].
16. **The companion acts this design reuses are live rows:**
    - **`transfer`** (`verb_table.yaml:1198`): between two rungs' stores, conserved. Computed, its
      `from` is the actor's own `contain` and its `to` is the question's referent (`:1211`)
      [CHECKED]. It renews an obligee's term when paid via the seat.
    - **`dispatch`** (`:263`, names a person, writes nothing, "their own choose decides")
      [CHECKED-draft].
    - **`release`** (`:822-838`, closes `oblige` among its domain, and `commit` too, `:828`)
      [CHECKED].
    - **`move`** (`:720-734`) [CHECKED-draft].
    - **`train` is not a row today.** It is planned at IN-12 step 9 (B-Q). It writes
      `Person.capability`, which the matrix currently lists as retired (`write_matrix.yaml:395`)
      [CHECKED-draft], and only where a case names a vocation (`_part5.md:73`) [CHECKED].
17. **The stock and its clocks.**
    - **The kinds:** `matter_kinds` holds `grain, salt, timber, ore, coin`, an open registry: "add a
      kind by adding a row, and a draw against an unregistered kind raises" (`rosters.yaml:1279-1290`)
      [CHECKED]. No kind is a man or a weapon.
    - **The one replenishing clock:** MATTER's yield pass credits each rung's `stores` every season
      from its Sites, `base × condition / condition_scale × season_factor`, and writes through
      `w.write("stores", …)`, which emits `stores.changed` (`loop/matter.py:504-536`) [CHECKED].
      Yield has no ceiling: stores accumulate.
    - **The fixed-point scale:** `condition_scale = 1000` (`data/fixtures.py:181-182`) [CHECKED].
    - **A ratified field with no producer:** `Rung.envelope`, "the population not individuated as
      persons" (`queries/world_q.py:1065-1070`; `04:255`; H-171 limit 2) [CHECKED]. §2.1 weighs it as
      the pool's home and declines it.

### 1.5 The plan as it stands

18. **IN-52** ("the levy-to-field feed") is BLK.
    - **Its premise:** "`levy` [now `requisition`] moves stores, not troops … a season field is one
      troops-sized subunit (J-18)".
    - **What it adopts:** LF-1 to LF-3 as delegated-ruled, "[ASSUMPTION; medium; Jordan to correct]"
      (`workplans/valoria_master_workplan_v9_part4.md:134-140`) [CHECKED-draft].
    - **Nothing of it is built.** `field_provisioning` and `settlements.provision` appear in no `.py`
      or `.yaml` file in the tree (`grep -rln`, 0 hits) [RAN at drafting], and `modules/settlements/`
      does not exist (`ls modules/`: `combat mass_battle social_contest`) [RAN at drafting].
19. **IN-49** makes the store act execute from a question source over a full larder in purview
    (`_part5.md:211-218`) [CHECKED-draft]. Its EXIT still names "`levy` row executes ≥ 1 with
    `Act.via` … `levy.taken` in `w.log`" (`_part5.md:215`) [CHECKED].
20. **MB-08** leaves #445 U-1 ("musters with inputs beyond headcount") and U-2 (one equipment model)
    unscheduled (`workplans/valoria_master_workplan_v9_part7.md:26-31`) [CHECKED-draft].

### 1.6 The four demands and the ruling against this, in one table

| demand | carried today? | where it fails |
|---|---|---|
| (1a) troops a settlement holds as its own resource | **no** | no store kind is a man; the population cohort has no `commit` and is never mustered (items 2, 17) |
| (1b) a levy that produces them | **no** | the only act that ever bore the name moved goods; `requisition` now does (item 14) |
| (1c) quality by equipment, experience, commander | **no** on the season path | constants (item 5); presets and officers are reachable only from harnesses (items 8–12); experience has no carrier (item 13) |
| (1d) units as the field's input | **no** | the input is a weight tuple (item 3) |
| (2) the 4/4 Line is a stub | **confirmed** | item 5 |
| (3) composite armies with subformations | **built in the harness, unreachable** | items 8, 9; `march` carries no order of battle (item 15) |
| (4) `levy` wrongly names a store act | **fixed in the tree** | item 14 |
| R-POOL: a pool of its own that replenishes, the cohort untouched | **no** | no settlement carries a value of raisable men, and the one replenishing clock (yield) has no ceiling (item 17) |

---

## 2. THE RECRUIT POOL AND THE TROOP BODY

### 2.1 Where the pool lives: four homes, one chosen

R-POOL asks for a value of the settlement's own that replenishes. The code offers four homes for it:

| home | what it adds | Layer 1 | what it gets wrong |
|---|---|---|---|
| **S. a `recruits` kind in the settlement rung's `stores` — CHOSEN** | one `matter_kinds` row; a ceiling Query; a capped credit at MATTER; one refusal so no store act moves it | none. `(Rung, stores)` already admits `[MAT, RES]`, class `MATTER/ACTS`, emitting `stores.changed` (`write_matrix.yaml`) [CHECKED] | a store is movable by `_shift`'s two callers. A man is not goods, so `_shift`'s callers must decline the kind (below) |
| **E. `Rung.envelope`** | a producer for a ratified, unwritten field (H-171 limit 2); RES added to `(Rung, envelope)`, which today is `[MAT, CEN]` (`write_matrix.yaml`) [CHECKED] | strains `04:179`, which gives `envelope` to CENSUS alone [CHECKED] | its ratified meaning is "the population not individuated as persons" (`world_q.py:1065`) [CHECKED]. Since `24f` the cohort carries the population, so a pool there would represent the same people twice. Its declared shape is a list of age bands that no position built |
| **G. a `muster` Site kind whose `condition` is the pool** | a site kind, and the `wear_per_season` and `band_floors` rows any new kind forces (`rosters.yaml:1258-1263`) [CHECKED]; one Site minted per settlement; a clamp at `condition_scale` in the wear loop | none | the strongest precedent (Jordan put a settlement's fortification on a Site's `condition`, ED-IN-0279 (a), `rosters.yaml:1264-1268`) [CHECKED], but a Site is fabric. `restore` and wear would act on a roll of men, regrowth would emit `condition.worn`, and the pool would be a fraction, not a count |
| **F. a new field on `Rung`** | a carrier field, a matrix row, an event kind | **amends** `04:255`'s ratified `Rung := ( …, envelope, exists )` (`04:255`) [CHECKED] | nothing semantic; it costs a Layer 1 amendment for a value `stores` can carry |

**Why S:**
- **It composes on the stock that exists.** The raise is a debit at RESOLVE, as `requisition`'s is.
  The regrowth is a credit at MATTER, through yield's own write path. The world's weigh-test
  (§2.8) already sums stores per kind.
- **It counts men in whole units,** so the existing grammar can test the pool (§3.1). G's fraction
  cannot be tested that way.
- **It amends nothing ratified.**

**Its one defect, closed by one owner.** `_shift` is "the one body of every act that moves stores
between two rungs" (`effects_shared.py:117-128`) [CHECKED]. Left alone, `requisition` could carry a
town's recruits into a treasury, and men would become goods, which is demand (4) inverted. So:
- a roster, `rosters.yaml: immovable_kinds: [recruits]`;
- a predicate, `movable(w, kind)`, read by `_eff_requisition` and `_eff_transfer` before they write;
  each declines to its own `write` refusal;
- `_shift` asserts it as the last line of defence.

A computed act may still form a `requisition` of `recruits`, if a witnessed `stores.changed` gives a
chooser a claim naming the kind. That is a scene tax, and TS-3's falsifier measures it (§7).

### 2.2 What the pool derives from: the ceiling

`recruit_ceiling(w, rung)` is a Query in `queries/world_q.py`. It is a world read, like `population`
and `capacity`:

```
recruit_ceiling(w, rung) = ( Σ weight of resident cohort persons under rung
                             that hold no live `oblige`  ×  recruit_share  + 500 ) // 1000
```

- **The base is the settlement's own people, read where they are:** the cohort persons whose
  residence (`home_of`'s read of `reside`) is in the rung's subtree, as `population` reads it
  (`world_q.py:1048-1078`) [CHECKED].
  - **Why only cohorts:** a named person at weight 1 is a commander, not a man in the ranks (J-6, §2.6).
  - **Why only those in no service:** a company is a resident cohort and always holds a live `oblige`
    while it exists (§2.9). Counting it would let every raise enlarge the ceiling that fed it.
  - **The residual:** a population cohort that obliges itself to a seat (it may: `oblige` forms on a
    seat the person was told of, `verb_table.yaml:749` area) [CHECKED] drops out of its own base while
    it serves.
- **`recruit_share`** is a per-mille fixture: how much of a settlement's weight can stand in the ranks
  at once. **[OPEN — Jordan tuning]**, with a hole-register row and a sweep (§6). At 1000, a settlement
  can field its people's weight once over.
- **Integer, half-up,** on the per-mille convention `condition_scale` already sets (`fixtures.py:182`)
  [CHECKED]. That is §2.8's one rounding rule.
- **At the shipped data, every ceiling is equal.** All 37 cohorts weigh 2 (H-170), so every ceiling
  is `2 × recruit_share / 1000`. Settlements differ only once H-170's weights differ, which its own
  sweep declares ("half of `capacity(w, rung)` per row", `hole_register.yaml:3730`) [CHECKED].
- **Other readable inputs were considered and not added:**
  - **`capacity(w, rung)`** (dwelling Sites, 4 to 9 at `build_realm(0)` [RAN]) would give a spread at
    the shipped data, but it is housing, not people. R-POOL says the pool derives from the settlement,
    and the people are what the ruling protects.
  - **A garrison's condition, or the larder's fill,** would each be one more reader. Neither is asked
    for.

### 2.3 How the pool replenishes

At MATTER, after yield, in the same per-rung loop and through the same `w.write("stores", …)`:

```
growth   = ( recruit_ceiling(w, rung) × recruit_regrowth + 500 ) // 1000
recruits ← min( recruit_ceiling(w, rung), recruits + growth )
```

- **The precedent is yield's**: a credit to `stores` at MATTER, through the same write and the same
  `stores.changed` emission (`matter.py:504-536`) [CHECKED].
- **The difference is the ceiling.** Yield accumulates without bound. The pool stops at its ceiling,
  so a quiet settlement never banks an army.
- **No write when nothing changes.** A full pool writes nothing and emits nothing, so a realm that
  never conscripts sees no new Event.
- **`recruit_regrowth`** is per-mille of the ceiling per season. **[OPEN — Jordan tuning]**. Its sweep
  is 0 (the control: a pool that never refills), 250 and 1000 (§6). With the falsifier values (§6),
  a ceiling of 2 regains 1 a season.
- **Not scaled by `season_factor`.** Tying recruits to the harvest is a second reading of the
  season's draw. It is available, it is not asked for, and it is not added.
- **World-gen fills every pool to its ceiling.** That is a derived value, not an authored number. It
  is written by `harness/populated.py` after `seat_cohorts`, which is world-gen's existing place for a
  cohort fact.

### 2.4 The troop body under the pool: the candidates re-compared (J-1)

R-POOL fixes where troops come from. It does not fix what a raised troop is. The draft's five
candidates, re-read against the pool:

| | troop body | Layer 1 (ratified) | population and food | who acts | new apparatus, at the shipped data |
|---|---|---|---|---|---|
| **P** — **CHOSEN** | **a company `Person`** at weight `n ≥ 2`, minted by `conscript` at the settlement, resident there, bound to the seat by `oblige` | keeps §C.5.1's unit sentence (`04:793`); **amends** its muster line (`04:792`, `:802`) to field persons with no `commit` (§0 item 4) | the cohort is untouched. The company eats from the one larder and counts in `population`, so a raise costs food and housing room (§2.5) | the company deliberates, witnesses, can `release` its service (desert) and dies through `remove_person` | the verb row; a gate basis; one `founding` clause; `service_faction` and the `mustered` clause; the `_side_stance` edit; the dissolution rule (§2.9). **Works at weight 2:** a raise of 2 mints a cohort |
| **A1/A2** | **a troop stock**: `conscript` moves `recruits` into `stores["troops:<kind>:<grade>"]` on the seat's rung | **amends** §C.5.1's unit sentence and §C.5's *"claimants : PersonId[], STRUCTURAL"* (`04:779-780`) [CHECKED-draft]: troops reach the field as a count | nobody eats unless a ration rule is added. LF-1/LF-3 then come back, as a feeding, not a double draw | nobody: a stock cannot desert, defect, witness or be wounded (AX-1, `04:120`) | composite store keys; a field input that reads stocks beside persons; a kind conversion over stock keys. No Person minting, so no chooser load, no gate basis, no muster clause and no morale-reader edit |
| **B** | a typed troop row (`Company` record) | **amends** §C.5.1 by name and T-l, *"one `Person` class; no subclass exists"* (`04:123`, `:245`) [CHECKED-draft] | whatever its fields say | nobody, unless it gets a verb surface | a carrier, matrix rows, gate bases, a loader schema |
| **D** | the population cohort commits and fights | complies | — | the town | **ruled out by R-POOL.** Troop quantity must come from the pool, and under D it is the cohort's weight |
| *C (the draft)* | a company split off the cohort | — | — | — | **ruled out by R-POOL.** The cohort must not be reduced |

**Why P:**
- **The person's life comes with it.** Desertion, defection by regard, death and witnessing are what
  R-WORLD needs from an army nobody is watching. A stock has none of them.
- **Each quality axis reuses a carrier:** kit is a rung's `stores`, moved by `transfer`'s conserved
  `_shift`; grade is `Person.capability`; the commander is a seat holder, read through
  `establishment_of`'s `oblige` walk (`world_q.py:1508-1533`) [CHECKED-draft].
- **The amendment it needs is the smaller one.** P widens who stands in a field; A and B change what
  a unit is.

**What P costs that A does not:**
1. **More persons.** Every raise mints a `Person` that deliberates every season. That is chooser load,
   and it may crowd other verbs out of scenes, which is the H-163 shape
   (`hole_register.yaml:3543`) [CHECKED-draft]. The dissolution rule (§2.9) bounds it: a company
   exists only while it serves.
2. **The Layer 1 muster amendment** (§0 item 4), plus the `_side_stance` edit that goes with it.
3. **The S9 remnant.** A company worn down to `weight == 1` is no longer a cohort
   (`carriers.py:713-721`) [CHECKED]. It stops eating (`world_q.py:860`) [CHECKED] and, under J-6,
   stops counting as troops. With integer half-up survivors (§2.8), a weight-2 company is left at 1
   by any loss between 25% and 75%. **At the shipped raise size this is common, not an edge.**
   Recorded as a residual (§8), with its option (§2.9).

**The contrary reading of statement 1, inside J-1:**
- The comparative reads *"their own resource"* toward "a rung-held carrier" (`00_COMPARATIVE_ANALYSIS.md:202`)
  [CHECKED].
- The MB lane reads statements 1 and 5 as "the field's troop count should come from a levied stock,
  not from a conversion of summed weight" (`MB_mass_battle.md:434`) [CHECKED].
- **Under the pool, P meets most of both.** The resource is rung-held (`recruits`), and a field's
  troops are the raised companies' weight, not the faction's summed weight.
- **What P keeps that the MB reading rejects:** one conversion, `troops = weight × men_per_weight`.
  A stock counted in men (A) needs none. That is the strongest case for A, and it is J-1's.

### 2.5 What a raise does to the settlement

- **The cohort is untouched.** `conscript` writes the pool, a new Person, its person-rung, its
  `contain`, `reside` and `oblige` edges. It writes nothing on the cohort, so the cohort's `weight`,
  its `want = wt × weight` (`world_q.py:866`) [CHECKED] and its stance are byte-unchanged (R-POOL;
  TS-4's falsifier).
- **The settlement's demand rises by exactly the company's want.** The company is a resident cohort,
  and `subsistence_draw` feeds every resident cohort (`world_q.py:852-866`) [CHECKED]. An army is
  mouths. That is a cost the draft's split did not have. It restores the levy amount's choice (§8.2).
- **`population` rises by the company's weight,** so `migrate` into a settlement crowded by its own
  levies is refused sooner. `conscript` does not check `capacity`. Capacity bounds `migrate`, and an
  army camps.
- **Production does not fall,** because nothing models labour (`matter.py:504-520`) [CHECKED], and
  R-POOL makes that the ruling.
- **War no longer drains the population.** Deaths fall on companies, the cohort is never written, and
  the pool regrows. The draft's residual "population has no producer, so war drains the realm" does
  not arise. What war costs is food, the pool and the seasons the pool takes to refill.

### 2.6 Who counts as troops (the draft's J-6, answered by precedent)

**Only cohort persons** (`Person.is_cohort`, `carriers.py:713-721`) [CHECKED]. A mustered named person
at `weight == 1` commands; he is not men in a subunit.
- **This is CLAUDE.md §0's ladder, step 4.** Plan position `24f`'s rule, "ONLY A COHORT EATS", carried
  one step on Jordan's *"NPC synecdoches that just represent the overall population … i don't think
  having lords and guild members etc worry about subsistence is worthwhile"* (`world_q.py:815-822`,
  ED-IN-0255) [CHECKED-draft]. The synecdoche that eats is the synecdoche that fights.
- **Decided here, not escalated.** The draft listed it as J-6, and the critic is right that its own
  text answered it (finding 9).

### 2.7 Keys: troop kind × grade

- **The troop kind is derived by the module, from `TROOP_LOADOUT`, its one owner.**
  - **The host passes kit, not a kind.** Each company's row in the order of battle (§4.2) carries the
    equipment kinds and counts on its person-rung and its weight. The season names no troop kind and
    keeps no kind table. The seam wrapper reaches the module by an entry string, not an import:
    "`engine/` never imports module code" (`seam/wrappers/mass_battle.py:72-78`) [CHECKED]. So the
    kind must be decided module-side.
  - **The rule** is `kind_for_kit(kit, weight)`, a pure function beside `TROOP_LOADOUT` in
    `modules/mass_battle/equipment/`. A row is *covered* when the kit holds at least `weight` units of
    the row's weapon class and of its armour class. Armour `none` needs nothing.
  - **Ranking:** among covered rows, the heaviest armour wins (`ARMOURY` order), then
    `TROOP_LOADOUT`'s own key order.
  - **No row covered:** the kind is the module's declared unarmed kind, `levy`. That is a constant
    beside `TROOP_LOADOUT`. It cannot be the `levy` row by coverage, because that row names
    `light_cut` (`equipment/__init__.py:22`) [CHECKED]. Raw men fight as levies.
  - **What the single owner exposes as MB data [OPEN]:**
    - `archers` and `mounted_archers` share `bow`/`light`, so `mounted_archers` is unreachable by kit;
    - `cavalry` is reached without horses, because no row names a mount;
    - `knights_templar` is reached by `heavy_blunt`/`heavy` like any kit (`:30`) [CHECKED], with its
      discipline 6 and morale 6 (`registry.py:49`) [CHECKED]. The draft excluded it as "cavalry's
      kit", which was wrong.

    A mount column, or a creed condition, belongs in `TROOP_LOADOUT` or `TROOP_TYPE_STATS`, never in
    a season table.
- **The grade** is `capability.get(GRADE_KEY, 0)`, clamped to the length of `rosters.yaml:
  troop_grades`.
  - **A row** adds a discipline offset and a morale offset to the kind's preset.
  - **Grade 0 adds nothing.** A raw company fights exactly at its kind's preset (the control).
- **Mixing grades is structural, not averaged.** A company is minted at grade 0 with no kit, and
  `conscript` never adds men to an existing company. Veterans are never diluted (K-MB-3,
  `MB_mass_battle.md:717`).

### 2.8 Quantity, conservation and integers

**Men per weight.** The season counts people in `weight` units, and the engine counts men. One number
converts them: `men_per_weight`. It is applied **once**, in the host's order of battle, to every
company's weight: `troops = weight × men_per_weight`, an int.
- **The pool unit is the weight unit.** A raise of `n` takes `n` from `recruits` and mints weight `n`,
  so the pool needs no conversion of its own.
- **Not in the module.** The module "is not the place to invent one" (`massbattle.py:198-207`)
  [CHECKED-draft]. It receives troops already counted.
- **The value is [OPEN — Jordan tuning].** The MB lane puts the scale where strength starts to matter
  at about 120 troops per side (`MB_mass_battle.md:515`) [CHECKED-draft as a citation]. **For every
  falsifier run in §7 it is fixed at 250**, so one weight-2 company is 500 men, clear of
  `SUBUNIT_ROUT_FLOOR`. At 1 (today's scale), sides of 2 to 4 men rout every run, and no band
  distribution can differ (critic finding 15).

**Conservation.** Nothing is minted or lost without a receipt. The W3 lesson, *"six grain left the
world and arrived nowhere"* (`effects_shared.py:117-128`) [CHECKED], applies to men and to kit:

| motion | conserved quantity | receipt |
|---|---|---|
| regrowth (MATTER) | `recruits` rises by `growth`, capped at the ceiling: the one **source** of men | `stores.changed` on the rung |
| `conscript` | `recruits` falls by `n`, and Σ company weight rises by `n`, in one `Change` | `conscript.taken` on the rung, the company and the edge |
| `transfer` (equip) | Σ stores per kind, through `_shift` | `transfer.made` on both rungs |
| a lost field | Σ company weight falls by exactly the casualties: the one **sink**, deaths | `field.lost` plus `weight.changed`; `person.died` on removal |
| a company destroyed | its kit `_shift`s to the rung the field was fought at, in the same `Change`, **before** `remove_person` runs. `remove_person` also pops the person's own `person`-kind rung (`state/world.py:770-773`) [CHECKED], so without the clause the kit would be destroyed with it | `stores.changed` on both rungs |
| a company dissolved (§2.9) | its weight returns to `recruits`, up to the ceiling; any excess is absorbed into the people, a declared sink. Its kit `_shift`s to the settlement rung | `company.dissolved`, naming returned and absorbed |

**The falsifier for every row is one test: weigh the world.** Sum `weight` over persons and stores per
kind over rungs, before and after. The difference must equal the declared sources and sinks.

⚠ **Outside this design, found while checking the salvage row:** any person who dies today with
stores on their own person-rung takes that matter out of the world, because `remove_person` pops the
rung (`world.py:770-773`) [CHECKED]. Persons rarely hold stores there today. This design is the first
to put matter there on purpose, so it carries its own salvage clause. The general case is the
death cascade's, and is not decided here.

**Integers.** Every new season quantity is an `int`: the pool, a ceiling, a weight, a grade, a stores
count and `troops`.
- **The one float the field produces** is the engine's survivor ratio (`massbattle.py:285-286`)
  [CHECKED-draft]. It is converted once, at the host, to per-mille: `permille = floor(pct × 1000 +
  0.5)`.
- **A company's survivors** are `(weight × permille + 500) // 1000`. No float reaches `World`, which
  `World.content_hash()` reads and the port must reproduce.
- **One rounding rule for the design:** half-up per-mille, for the ceiling, the growth and the
  survivors.
- **Out of scope:** today's individual casualty write still multiplies `body` by a float
  (`effects_combat.py:254`) [CHECKED]. TS-6 should route it through the same per-mille, so one
  quantity has one conversion (§8.3).

### 2.9 When service ends: dissolution, death and the return rule

A company exists to serve. When its service ends, it **dissolves**: `remove_person` runs, its weight
returns to its settlement's `recruits` (capped at the ceiling), and its kit `_shift`s to the settlement
rung.
- **When service ends:** its last live `oblige` closes, by the term's maturity at MATTER (plan position
  `17b`, `verb_table.yaml:837`) [CHECKED-draft] or by its own `release` at RESOLVE (desertion).
- **Who is a company:** a person whose first `oblige` was opened by a `conscript` act, read off
  `Tenure.term.declared_by`, the act that wound the clock (`state/carriers.py`, `Term`) [CHECKED].
  That is one Query, `is_company`. It is the first reader to ask *why* an edge was opened, which
  H-173 records no reader does (`hole_register.yaml:3765`) [CHECKED]. It asks for one purpose only,
  and it never reads a population cohort that obliged itself, so no settlement can dissolve its own
  people.
- **Why dissolution and not persistence (CLAUDE.md §0's ladder, step 5):**
  - **The world stays bounded.** A persistent company is a person who eats and deliberates forever.
    With the pool refilling, every settlement could mint one every few seasons, and chooser load
    would grow without limit.
  - **Men are conserved,** with the receipt in §2.8.
  - **Desertion means going home.**
- **What dissolution costs:** veterans do not outlive their service. Kit returns to the settlement's
  stores, where its holder may `requisition` it, but the grade is lost. Whether veterans should
  persist as a living reserve (the draft's default) is a question about experience, so it is folded
  into J-5 (§9).
- **Death.** Men killed in a field do not return. The pool regrows toward its ceiling regardless,
  which is R-POOL's "replenishes over time".
- **The remnant option, not taken:** dissolving a company the moment it stops being a cohort (weight
  1) would close §2.4's remnant at once. It adds a second trigger. It is recorded in §8, not built.

---

## 3. THE VERBS

### 3.1 `conscript`: raise a company from a settlement's pool

`conscript` is the one new verb. The row below is illustrative, in the table's own shape. It binds
nothing until it is written into `engine/season/verb_table.yaml` and the loader accepts it.

```yaml
- verb:        "conscript"
  scale:       "settlement"
  scale_note:  "men are raised from a settlement's recruit pool -- the settlement IS the subject"
  stratum:     "binding_decision"
  eligibility: ["remit:dispatch"]
  beneficiary: "none"            # taken FOR the seat, as `dispatch`/`revoke` read it
  requires:    "the subject is a rung, the seat's purview reaches it, and its recruits cover the amount"
  requires_typed:
    all:
      - {form: existence,        of: subject, kind: Rung,       conjunct: subject}
      - {form: basis,            of: subject, basis: purview,   conjunct: authority}
      - {form: scalar_threshold, of: subject, scalar: stores, key: kind, threshold: amount,
         comparator: ">=",       conjunct: subject}
  writes:      ["Rung.stores", "Person.exists", "Tenure.since", "Tenure.term"]
  emits:       ["conscript.taken"]
  emits_on_refusal:
    eligibility: ["conscript.unauthorized"]
    authority:   ["conscript.unauthorized"]
    subject:     ["conscript.refused"]
    write:       ["conscript.refused"]
  grade:       "assumption"
```

**Operands.**
- **`subject`** is the settlement rung.
- **`amount`** is in weight units. It comes from where every computed `amount` comes from today: a held
  claim, else the fixtures (H-94; `requisition`'s `requires_typed_note`, `verb_table.yaml:650`)
  [CHECKED-draft]. The fixture is `conscript_amount`, **shipped 2**, the smallest company that is a
  cohort.
- **`kind`** is `recruits`, carried as the act's `kind` operand from a fixture, as `transfer` carries
  `default_store_kind`. Whether a typed cell's `key:` may name a literal instead is **[UNVERIFIED]**.
- **No ninth operand.** All three names are in the closed `requires_operands` roster
  (`rosters.yaml:1649`) [CHECKED-draft].

**Eligibility is `remit:dispatch`.** `march` already uses it (`verb_table.yaml:668`) [CHECKED-draft].
Raising and sending men is one remit, and the roster stays at six (`rosters.yaml:311`)
[CHECKED-draft]. A seventh remit act would be a ruling, as `requisition`'s own substitution note says
of itself (`verb_table.yaml:662`) [CHECKED-draft].

**The typed cell** is `requisition`'s, conjunct for conjunct: purview over the subject, and the stores
threshold. So the grammar refuses a short pool before the effect runs, and no new stem is needed.

**The effect, `_eff_conscript`** (in `loop/effects_governance.py`, beside `_eff_requisition`):
1. Resolve the seat (`_exercised_office`, `effects_shared.py:131-136`) [CHECKED-draft], the settlement
   `rung`, and `n`.
2. **Decline** (→ `write` → `conscript.refused`) when any of these holds:
   - `n < 2`. A company of 1 is not a cohort: it would not eat and would not count as troops
     (`carriers.py:713-721`) [CHECKED].
   - There is no seat.
   - The settlement has no resident cohort to house the company with (below).
3. **Mint:** `cid = H(world_seed, tick, actor, f"conscript:{rung}:{a.id}")`, salted on the act, per
   `_eff_oblige`'s pattern (`effects_governance.py:332-340`) [CHECKED-draft].
   - Construct `Person(cid, weight=n, born=…)` and its person-rung `Rung(cid, "person")`.
   - Open `contain` and `reside` to the rungs the settlement's population cohort holds them on: the
     settlement rung itself at world-gen (`populated.py:439-442`) [CHECKED].
4. **Debit** `rung.stores["recruits"] -= n` in the same `Change`.
5. **Bind:** open `Tenure(company → seat, "oblige", since=tick, term=_new_oblige_term(w, a))`, the term
   every service carries (`effects_shared.py:108-114`; fixture `oblige_term`, shipped 4,
   `data/fixtures.py:816-818`) [CHECKED]. The levy reuses that term (the draft's J-7, answered in §9).

**Writes, and their classes:**

| pair | today | change | why |
|---|---|---|---|
| `(Rung, stores)` | `[MAT, RES]`, class `MATTER/ACTS` | none | the debit at RES, as `requisition`'s; the regrowth at MAT, as yield's |
| `(Person, exists)` | `[MAT, RES, CEN]` (`write_matrix.yaml:202-204`) [CHECKED-draft] | none | a mint at RES, which the row already admits. The company is minted at weight `n`, which is construction, not a write to `(Person, weight)` |
| `(Person, weight)` | `[CEN]`, class `MATTER` (`:240-246`) [CHECKED-draft] | `[CEN, ENC]`, class `MATTER/ACTS` | casualties at ENC, the step `_eff_march` writes `stance` at (`:227-231`) [CHECKED-draft]. H-49's missing runtime writer |
| `(Tenure, since)` and `(Tenure, term)` for `oblige` | admitted under `T-m` (own) and `determination` (a bench's disposal) | **one new gate basis, `conscription`**: an OPENING of an `oblige` whose OBJECT is `via` and whose owner was born in this write, by a seat the actor sits in, granted `dispatch`, whose purview reaches the owner's place. It is authority-bound like `T-o` and `determination` (`state/gate.py:805-847`) [CHECKED-draft] | `determination` is a judging seat's (`:826-831`) and does not fit a lord. Widening it would blur the sentence/service distinction H-173 already warns about |
| `(Tenure, since)` for the company's `contain` and `reside` | `founding` admits a born subject's **only `contain`** (`gate.py:848-856`) [CHECKED-draft] | **`founding` widened by one clause:** a subject born in this write may also open its single `reside` | a person born at RES needs a home. Census minting at CEN opens no `reside` at all, so its person is "ABSENT FROM THE MAP" (`census.py:72-76`, H-51) [CHECKED] |

**Per-clause refusals** (`04 §B.13` invariant 4, `04:487-492`) [CHECKED-draft]:
- **`conscript.unauthorized`** means the SEAT failed. The actor exercised no seat granting `dispatch`,
  or the seat's purview does not reach the settlement.
- **`conscript.refused`** means the PLACE failed. The pool is short, the amount is below a cohort, or
  there is nowhere to house the men.

A witness can tell "the lord had no right" from "there was nobody left to take". That is
`requisition`'s split of authority against scarcity (`verb_table.yaml:659`) [CHECKED-draft], applied
to men.

### 3.2 The companion acts: each needed, and none of them new

| need | act | reused as it stands? | what the troop stock adds to it |
|---|---|---|---|
| fill a treasury with goods, including arms | **`requisition`** (`verb_table.yaml:629-663`) | **yes**, plus the `movable` refusal (§2.1) | nothing else. It is the source the kit is drawn from. IN-49 keeps its subject under the new name |
| equip a company | **`transfer`**, `from` = the seat's treasury, `to` = the company's person-rung, `kind` = an equipment kind | **yes**, plus the `movable` refusal. `_eff_transfer` moves between any two rungs, conserved (`effects_economy.py:168-240`) [CHECKED-draft] | new `matter_kinds` rows for kit (§6). ⚠ **Computed play cannot form it**, because the computed `to` is the question's referent (`verb_table.yaml:1211`) [CHECKED], and no question is about a company's person-rung. ⚠ It renews no term: `_renewals` renews obligees whose home is the receiving rung (`effects_economy.py:303-307`) [CHECKED], and a company's home is its settlement, not its person-rung [INFERRED] |
| drill a company | **`train`** (IN-12 step 9, unbuilt) | **no, as planned.** J-13's answer (iii) writes capability only where a case names a vocation (`_part5.md:73`) [CHECKED]. A company has no case | nothing until J-5 or J-13 changes. The grade key is still reserved in `verb_capability` (§6), so the change is one data row when it comes |
| bring companies from several settlements to one muster | **`dispatch`** (`:263`, names a person, writes nothing) + **`move`** (`:720`, the company's own act) | **yes** | nothing. The muster reads presence (§4.1). Whether a company's chooser answers a dispatch by moving is **[UNVERIFIED]** (`dispatch`'s own note: "their own choose decides", `:276`) |
| field the army | **`march`** (`:664-690`) | **row: one act-declared payload key, `order` (§4.3). Effect: the write-back (§4.6)** | the side's composition is read, not chosen at the fold |
| end service | **the term's maturity** (MATTER matures `oblige` terms, `17b`) + **`release`** (`:822-838`, own-eligible: desertion) | **yes**, with the dissolution rule (§2.9) | ⚠ **No lord-side dismissal exists, and that is ruled.** D-5, "second-person lever stays refused" (`verb_table.yaml:838`) [CHECKED-draft]. A lord who wants his levy gone stops paying, and the term runs out |

### 3.3 What is NOT added, and why

| not added | because |
|---|---|
| a `muster` verb | the muster is a Query, `mustered` (§4.1). A verb would write a fact the Query derives |
| an `equip` verb | `transfer` moves kit; a kit is stores |
| a `disband` or `dismiss` verb | D-5 refuses a lord-side closer; the term and `release` already end service |
| a `recruit` verb (troops for coin) | it mints men from matter, which is A2's game. R-POOL names the pool as the source |
| a seventh remit act | `dispatch` covers raising and sending men (§3.1) |
| a merge of companies | not needed. Each company is its own subunit (§4.2), so a lord who wants one big block raises one big company |
| a season troop-kind table | `TROOP_LOADOUT` is the one owner (§2.7) |
| a `Company` type, a troop field on `Rung`, a stored troop kind | §2.1, §2.4 and §2.7 |

### 3.4 The corrected role of `requisition`

`requisition` is the store act and nothing else. It moves goods from a rung in the seat's purview into
the seat's treasury (`effects_governance.py:373-412`) [CHECKED-draft]. It may not move `recruits`. In
this design it is the upstream end of the kit chain:

`requisition` (ore, coin, arms → treasury) → `transfer` (arms → company) → `kind_for_kit` → the field.

Its name is provisional, and J-3 (§9) carries it.

### 3.5 The meta-rule: every object added, every object cut, counted honestly

**Added** (each tested in §8's N-ledger):

| # | object | kind |
|---|---|---|
| 1 | the `conscript` row, with keyed refusals | verb row |
| 2 | `_eff_conscript` | effect |
| 3 | the `recruits` matter kind | registry row |
| 4 | `immovable_kinds` and `movable(w, kind)`, read by two effects and asserted in `_shift` | roster + predicate |
| 5 | `recruit_ceiling` | Query |
| 6 | the capped regrowth credit in MATTER's rung loop | clock write |
| 7 | world-gen fill of every pool | harness step |
| 8 | the gate basis `conscription` | gate basis |
| 9 | one `founding` clause (a born person's `reside`) | gate clause |
| 10 | `(Person, weight)` gains ENC | matrix edit |
| 11 | `service_faction` | Query |
| 12 | the `mustered` clause | Query edit (a Layer 1 amendment, §0 item 4) |
| 13 | `_side_stance` reads `service_faction` | reader edit |
| 14 | `is_company` and the dissolution rule (§2.9) | Query + rule |
| 15 | `order_of_battle` in the host wrapper | host function |
| 16 | `MassBattleInput.weights` → `sides` | record edit |
| 17 | `kind_for_kit` beside `TROOP_LOADOUT` | module function |
| 18 | `trim_to_command` beside `build_army` | module function |
| 19 | `rosters.yaml: troop_grades`, kit `matter_kinds` rows, the grade key in `verb_capability` | registry rows |
| 20 | fixtures `recruit_share`, `recruit_regrowth`, `men_per_weight`, `conscript_amount`, each with a hole-register row | fixtures |
| 21 | the `order` payload key on `march` | act-declared key |
| 22 | the temporary fixture `field_army` (deleted at TS-9) | scaffolding |

**Cut, on disk:**
1. `_weighted_unit` (a function), and `_MVP_SUBUNIT_SHAPE`, `_MVP_UNIT_COMMAND`,
   `_SEASON_FORCE_POWER` and `_MIN_TROOPS` (four constants) (`massbattle.py:170-230`).
2. `MassBattleInput.weights` (replaced by #16, so this is an exchange, not a net cut).
3. The `[GAP …]` line (`massbattle.py:32`).
4. The duplicate `build_army` location, reduced to a re-export.

**Withdrawn, never on disk:** IN-52's design (`settlements.provision`, `field_provisioning`, 0 hits),
LF-1..LF-3 (plan text), K-MB-1's rung stock and SE's uncoupled kind as forms (research text). Closing
H-49 and MB-08's U-1 closes register and plan rows, not code.

**Net, stated plainly:** about 22 objects added against 6 cut on disk. The draft's "one verb, one
Query, one basis and one record field" undercounted its own list (critic finding 17), and the pool
adds six more. §8.4 scores E against this count, not the draft's.
