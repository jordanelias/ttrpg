# The troop stock: conscripted companies, the troop verb, and the season's order of battle

## Status: PROPOSED (2026-10-16), corrected the same day against an independent critic's report (reconciliation table at the end of `_part2`). Not ratified; merge ratifies nothing unless Jordan so rules.
## Lane: MB (the field and the army builder), SE (raising men from a settlement), FA (assembly), IN (the verb row, the gate, the registries). IDs: none allocated.
## Read at the working tree of 2026-10-16, after the `levy` → `requisition` rename (uncommitted when first drafted; the tree is clean at the correction pass, `git status --short` empty [RAN]).
## Parts: this file (head, §0–§3) · [`_part2`](2026-10-16-troop-stock-design_part2.md) (§4–§10, and the critic reconciliation), read in that order.

**Reference, not mechanism (CLAUDE.md §0.05).** Nothing here changes how the game behaves. Every
behaviour below becomes true only when the code in §7 is built and a run shows it. Where this document
and code disagree, the code is right and this document is wrong. Locators are `file:line` in the tree
as read. `[CHECKED]` means the line was re-opened in the correction pass. `[CHECKED-draft]` means it
was opened at drafting and **not** re-opened in the correction pass (the critic's report confirms most
of them; that is the critic's reading, not mine). `[RAN]` means I executed something and quote what
it printed. `[INFERRED]` means I reasoned from lines I opened but ran nothing. `[UNVERIFIED]` means I
did not open it.

**The troop verb's name in this document is `conscript`** (§3.1). It is a working name, not a claim:
the old store act's name, `levy`, is the word Jordan used, and reusing it collides with live text in
three registers. The collision and the follow-through it would need are laid out in J-3 (§9).

**Demands (D1, Jordan, 2026-10-16, verbatim, from the session brief):**
- **(1)** "mass battle is supposed to be based on army units that are troops levied from settlements
  as their own resource, and these troops are supposed to differ in quantity and quality based upon
  equipment and experience and their commanders etc"
- **(2)** "this 4/4 one line formation for one unit for mass battles as coded is a stub"
- **(3)** "factions are supposed to be able to assemble armies with different subunits with
  subformations"
- **(4)** "levy typically doesn't refer to goods/stores. that verb is wrong as currently used"

Demand (4) is met by the rename already in the tree. The name `levy` is free as a verb row, but not as
a word in the registers: `engine/season/requirements.yaml` still uses it 23 times and
`hole_register.yaml` 19 times for the store act (`grep -c levy`) [RAN]. So this design does not
reuse it by default (J-3).

---

## 0. VERDICT

1. **A troop is a person. The troop stock is a set of levied companies.** A company is a cohort
   `Person` at `weight > 1`, split off a settlement's population cohort by `levy` and bound to the
   levying seat by an `oblige` edge. Layer 1 already says what an army is:
   `units = PersonId[] at weight -- one type. There is NO unit class, at any scale`
   (`architecture/meta/04_CODE_ARCHITECTURE.md:793`) [CHECKED-draft]. It also says a cohort is a `Person`
   and no subclass exists (`04:123`, `:245`) [CHECKED-draft]. A stock of troops kept on a `Rung`, or a typed
   troop row, is a unit class. Either one would mean amending ratified Layer 1. A company does not. It
   also gets the person's existing machinery for free: it eats, is housed, witnesses, can desert by
   `release`, and dies through the one death cascade. The representation is still a decision for
   Jordan (**J-1**, §9), because he has not ruled on it. §2.1 weighs it against four alternatives.
2. **Quality has three axes, and each lives on an existing carrier:**
   - **Equipment** is matter held in the company's own person-rung `stores`.
   - **Experience** is a grade in the company's `Person.capability`.
   - **The commander** is the person who holds the seat the company is obliged to.
   The troop kind is never stored. It is a Query over the company's kit, so it cannot disagree with
   the kit (§2.3).
3. **The verbs:**
   - **One new verb:** `levy`.
   - **Reused companion acts:** `transfer` equips a company, `train` drills it (IN-12 step 9),
     `dispatch` and `move` assemble companies from several settlements, `march` fields them, and
     `release` plus the oblige term's maturity dismiss them.
   - **`requisition`** stays what the rename made it: the store act that fills the treasury the kit
     comes from (§3).
4. **The army builder moves across the seam.** `build_army` moves out of
   `systems/mass_battle/sim/engine.py:213-452` into `modules/mass_battle/` [CHECKED-draft]. The season's
   one-Line construction is deleted: `_weighted_unit`, `_MVP_SUBUNIT_SHAPE`, `_MVP_UNIT_COMMAND`,
   `_SEASON_FORCE_POWER` and `_MIN_TROOPS` (`modules/mass_battle/massbattle.py:170-230`) [CHECKED-draft].
   The host builds each side's order of battle from the companies present. The module builds the
   Unit through the one constructor (§4).
5. **A finding the design must fix on the way:** `build_army` throws away the morale preset of every
   troop type it builds.
   - **Probe [RAN]:** a `build_army` spec for a `levy` subunit printed `levy power 1 disc 1 morale 6`.
   - **Expected:** the preset row is morale 2 (`modules/mass_battle/troop_types/registry.py:41`)
     [CHECKED-draft].
   - **Cause:** `build_army` sets `kw['morale']` to the Unit's default (`engine.py:427`) before
     `Subunit.of_type`'s `kw.setdefault('morale', preset['morale'])` (`hierarchy/units.py:726`) can
     run [CHECKED-draft].
   - **Consequence:** on the harness path, troop-type morale is dead. Every harness-built army fights
     at Unit morale 6.
6. **What this cuts:**
   - **IN-52's feed and LF-1..LF-3 are withdrawn.** Troops are no longer bounded by a treasury. LF-1
     and LF-3 would also feed the same persons twice, because the larder already feeds them (§5).
   - **IN-49 is re-framed** as the store act's question source.
   - **Closed:** H-49 (a runtime writer for `Person.weight`) and MB-08's #445 U-1.
   - **Research rows it closes:** M-MB-2, M-MB-6, M-MB-15, M-MB-17, M-SE-9, M-FA-10, M-IN-12,
     M-IN-13 and M-PC-12 (the cohort half).
   - **Research rows it narrows:** M-MB-1, M-MB-3, M-MB-16 and M-NPC-13 (§5 says how far).
   - **Collisions it resolves:** X-2 (by choosing persons) and X-19 (by cutting the bound, against
     MB's keep).
7. **Grade: paper.** Nothing in §2–§4 is built. One probe was run (item 5 above). §7 gives the order
   in which to build it, and each step's exit is an execution artifact.

---

## 1. THE PROBLEM AS CODED

Each fact below is at its source. Together they answer the four demands against the tree.

### 1.1 Who fights a season field

1. **A field's two sides are faction members present at a place.**
   - **Attacker:** `sides_of` musters the attacking side as `mustered(w, origin, faction)`. `origin`
     is the actor's nearest settlement and `faction` is the faction of the seat the act was exercised
     through (`engine/season/loop/sides.py:77-85`) [CHECKED-draft].
   - **Defender:** the provider musters `mustered(w, rung, subject)` at the target
     (`engine/season/seam/wrappers/mass_battle.py:233`) [CHECKED-draft].
   - **What `mustered` reads:** "This faction's members present in `rung_id`'s subtree"
     (`engine/season/queries/world_q.py:1256-1272`) [CHECKED-draft]. Membership is a live `commit`, and
     "THIS IS THE WHOLE OF MEMBERSHIP AND THERE IS NO SECOND ROUTE" (`world_q.py:1151-1162`)
     [CHECKED-draft].
2. **The population never fights.**
   - **No commit:** the territorial population is one cohort `Person` per settlement, seated with
     "No `commit`, so it is no faction's member" (`engine/season/harness/populated.py:394`, minted at
     `:439` as `Person(pid, "the people of …", weight=wt)`) [CHECKED-draft].
   - **No size:** its weight is 2 at every settlement. That is the smallest weight S9 calls a cohort,
     "chosen AGAINST inventing a spread" (`engine/season/hole_register.yaml:3722-3732`, H-170)
     [CHECKED-draft].
3. **A side is its members' summed `Person.weight`.**
   - **The input:** `field_input` passes `weights = (tuple(w.persons[pid].weight …), …)`
     (`seam/wrappers/mass_battle.py:190-193`) [CHECKED-draft].
   - **The record:** the input record carries `weights`, `territory`, `fort_level`, `stances`,
     `walls_dr`, `origin`, `loyalties`, `loyalty_gain` and `geography`, and nothing about
     composition, kit or command (`engine/season/queries/inputs.py:62-100`) [CHECKED-draft].
4. **A person's weight never changes after construction.**
   - **Matrix row:** `(Person, weight)` is stepped `[CEN]`, class `MATTER`
     (`engine/season/write_matrix.yaml:240-246`) [CHECKED-draft].
   - **Register:** H-49 records "There is no runtime writer"
     (`hole_register.yaml:558-568`) [CHECKED-draft].
   - **Carrier:** `Person.__post_init__` refuses `weight < 1` (`state/carriers.py:709-711`)
     [CHECKED-draft].
   - **Consequence:** neither a levy nor a defeat can make a body of people smaller.

### 1.2 What the module builds from that

5. **Every side is one Line subunit of bare `infantry`, at power 4, command 4 and discipline 5.**
   - **The constants:** `_MVP_SUBUNIT_SHAPE = dict(shape='Line', troop_type='infantry', tier=2,
     starting_position=(8, 12), advance_dir=1, stance='balanced', unit_type='melee')`
     (`modules/mass_battle/massbattle.py:170-178`); `_MVP_UNIT_COMMAND = dict(command=4,
     discipline=5, discipline_start=5)` (`:182-186`); `_SEASON_FORCE_POWER = 4` (`:196`) [CHECKED-draft].
   - **Their own label:** "minimum-viable defaults … no canonical spec exists for army -> Unit
     construction of ANY kind" (`:160-166`), and the module header says
     `[GAP: faction -> unit construction lacks canonical spec …]` (`:32`) [CHECKED-draft].
   - **Demand (2) rules this a stub.**
6. **Troops are the raw weight sum.**
   - **The code:** `Subunit(**_MVP_SUBUNIT_SHAPE, troops=max(float(weight), _MIN_TROOPS), …)`
     (`massbattle.py:226`), with `_MIN_TROOPS = 1.0` as a crash floor (`:208`) [CHECKED-draft].
   - **The module's own disclosure:** it does not invent a conversion: "this module is not the place
     to invent one" (`:198-207`) [CHECKED-draft].
   - **The rout floor:** `SUBUNIT_ROUT_FLOOR = 80` (`modules/mass_battle/config.py:117`) [CHECKED-draft].
   - **The MB lane's probe:** 0 attacker wins in 20 at ≤80 troops, with both sides routed every run
     (`research/by_lane/MB_mass_battle.md:434`, M-MB-1) [CHECKED-draft as a citation; not re-run].
7. **Morale is the only side quality that reaches the field.** Each side's mean stance toward its own
   faction feeds `_morale_start` (`massbattle.py:119-157`), and the side stance is weighted by
   `Person.weight` (`seam/wrappers/mass_battle.py:126-148`) [CHECKED-draft].

### 1.3 What the harness can build, and the season cannot reach

8. **A composite army constructor exists, on the wrong side of the seam.**
   - **What it takes:** `build_army(specs, name, faction, *, power=4, command=4, discipline=5,
     morale=6, …, officers=())` (`systems/mass_battle/sim/engine.py:213-452`) [CHECKED-draft]. Each spec
     sets its own shape or role, `troop_type`, `troops`, quality overrides and an `officer`.
   - **What it checks:** roles are gated by `role_allowed` (`:369-371`). Officers' spans and the
     general's direct reports are checked against Command and `SUBUNIT_CAP = 11` (`:99`, `:304-345`).
   - **How subunits are built:** each one goes through `Subunit.of_type` (`:448`) [CHECKED-draft].
   - **Why the season cannot call it:** `modules/mass_battle/` imports nothing from `systems/`. The
     MB lane records a grep returning 0 (`MB_mass_battle.md:368`, T-MB-19) [CHECKED-draft as a citation].
     `systems/mass_battle/sim/engine.py` itself star-imports `modules.mass_battle.*` (`:6-26`)
     [CHECKED-draft], so the dependency runs one way only.
9. **Troop-type quality presets exist, including a `levy` row.**
   - **The table:** `TROOP_TYPE_STATS` (`modules/mass_battle/troop_types/registry.py:39-57`)
     [CHECKED-draft]. Its `levy` row is power 1, discipline 1, morale 2 (`:41`).
   - **How a preset is applied:** `Subunit.of_type` fills power, discipline and morale from it
     (`hierarchy/units.py:712-730`) [CHECKED-draft].
   - **Melee or ranged:** `unit_type_for` derives it from the type's weapon
     (`registry.py:151-159`) [CHECKED-draft].
   - **Off the season path:** none of it is reached there.
10. **The morale preset is dead even on the harness path.**
    - **Probe [RAN]:** I called `build_army([{troop_type:'levy', troops:400, …}, {troop_type:
      'heavy_infantry', …}], 'x', 'A')`. It printed `levy power 1 disc 1 morale 6` and
      `heavy_infantry power 4 disc 4 morale 6`.
    - **Cause:** the default at `engine.py:427` pre-empts the `setdefault` at `units.py:726`
      [CHECKED-draft].
    - **Intent:** DG-4 meant to give each subunit its own morale instead of `None`
      (`engine.py:410-426`) [CHECKED-draft]. It did not mean to overrule the preset.
11. **Equipment is a catalogue, wired only into `unit_type`.**
    - **The catalogue:** `ARSENAL` (weapon classes) and `ARMOURY` (`none/light/medium/heavy`, with a
      canonical `dr_vs_piercing`) are mutable registries seeded at import
      (`modules/mass_battle/equipment/weapons.py:29-49`, `armour.py:29-42`) [CHECKED-draft].
    - **The loadout table:** `TROOP_LOADOUT` names each troop type's weapon and armour
      (`equipment/__init__.py:21-36`) [CHECKED-draft].
    - **The header says "NOT YET WIRED into resolution"** (`equipment/__init__.py:10`) [CHECKED-draft].
      That is true for DR and speed. `unit_type_for` does read `loadout_for` (`registry.py:156`)
      [CHECKED-draft].
12. **Officers exist and are checked at construction only.**
    - **The class:** `Officer(name, command=4, charisma=None, cognition=None)` derives `command` when
      both attributes are given (`hierarchy/units.py:2699-2722`) [CHECKED-draft].
    - **What reads it:** `Unit.officers` is "Bookkeeping only … nothing at resolution time reads it"
      (`:2793-2797`) [CHECKED-draft], and `Subunit.officer` likewise (`:637-643`) [CHECKED-draft].
    - **What the check does:** `build_army`'s span check reads `Officer.command` (`engine.py:304-345`)
      [CHECKED-draft], so a commander's Command limits how many subunits he can field.
13. **Experience has no carrier.** `grep -rniE "experience|veteran|drill|training"` over
    `modules/mass_battle` finds two comments, and over `engine/season` non-test Python finds nothing
    (`MB_mass_battle.md:449`, M-MB-16) [CHECKED-draft as a citation; not re-run].

### 1.4 The verbs as they stand

14. **`requisition` moves goods, conserved, from a rung into the seat's treasury.**
    - **The row:** eligibility `remit:issue` and `presence:<rung>`, typed `requires` (purview basis
      plus `stores >= amount`), and `writes: ["Rung.stores", "Rung.stores"]`
      (`engine/season/verb_table.yaml:629-663`) [CHECKED-draft].
    - **Refusals, keyed per clause:** `requisition.unauthorized` and `requisition.refused`
      (`:654-659`) [CHECKED-draft].
    - **The effect:** `_eff_requisition` shifts `amount` of `kind` from the subject rung to the rung of
      `Act.via`'s office through `_shift`, "the one body of every move between two rungs' stores"
      (`loop/effects_governance.py:373-412`; `loop/effects_shared.py:117-128`) [CHECKED-draft].
    - **This is demand (4)'s act, correctly named.** It raises no troops.
15. **`march` fights over a place and writes only the losers.**
    - **The row:** eligibility `remit:dispatch`. The only operand is `subject`, a Rung. Writes are
      `Won`/`Lost` → `Person.body`, `Person.stance`. It is graded `ruled`
      (`verb_table.yaml:664-690`) [CHECKED-draft].
    - **The ruling (ED-IN-0279):** a loss writes "casualties only, decrease in morale, and a grudge
      token", and "nothing on the WINNING side" (`:682`) [CHECKED-draft].
    - **Casualties land on `body`, never on `weight`:** `p.body = max(1, int(p.body * max(0.0,
      pct …)))` (`loop/effects_combat.py:254`) [CHECKED-draft]. A cohort that loses half its men keeps its
      headcount and loses half its health.
16. **The companion acts this design reuses are live rows:**
    - **`transfer`** (`verb_table.yaml:1198`, between two rungs' stores, conserved, and it renews an
      obligee's term when paid via the seat) [CHECKED-draft].
    - **`dispatch`** (`:263`, names a person, writes nothing, "their own choose decides") [CHECKED-draft].
    - **`release`** (`:822-838`, closes `oblige` among its domain) [CHECKED-draft].
    - **`move`** (`:720-734`) [CHECKED-draft].
    - **`train` is not a row today.** It is planned at IN-12 step 9 (B-Q). It writes
      `Person.capability`, which the matrix currently lists as retired
      (`write_matrix.yaml:395`; `workplans/valoria_master_workplan_v9_part5.md:73`) [CHECKED-draft].
    - **The store rows need equipment kinds:** `matter_kinds` holds `grain, salt, timber, ore, coin`
      (`engine/season/rosters.yaml:1279-1290`) [CHECKED-draft], so no store kind is equipment.

### 1.5 The plan as it stands

17. **IN-52** ("the levy-to-field feed") is BLK.
    - **Its premise:** "`levy` [now `requisition`] moves stores, not troops … a season field is one
      troops-sized subunit (J-18)".
    - **What it adopts:** LF-1 to LF-3 as delegated-ruled, "[ASSUMPTION; medium; Jordan to correct]"
      (`workplans/valoria_master_workplan_v9_part4.md:134-140`) [CHECKED-draft].
    - **What its design rejects:** "Converting stores into troops. That mints persons, and no step
      constructs a `Person`" (`proposals/2026-10-07-settlements-computation-modules.md:401-402`)
      [CHECKED-draft].
    - **That premise is false today.** `(Person, exists)` is stepped `[MAT, RES, CEN]`
      (`write_matrix.yaml:202-204`), and `loop/census.py::_individuate` constructs a `Person` at CEN
      (`:102-107`) [CHECKED-draft].
    - **Nothing of IN-52 is built.** `field_provisioning` and `settlements.provision` appear in no
      `.py` or `.yaml` file in the tree (`grep -rln`, 0 hits) [RAN], and `modules/settlements/` does
      not exist (`ls modules/`: `combat mass_battle social_contest`) [RAN].
18. **IN-49** makes the store act execute from a question source over a full larder in purview
    (`_part5.md:211-218`) [CHECKED-draft]. Its subject is the store act, under its new name.
19. **MB-08** leaves #445 U-1 ("musters with inputs beyond headcount") and U-2 (one equipment model)
    unscheduled (`workplans/valoria_master_workplan_v9_part7.md:26-31`) [CHECKED-draft].

### 1.6 The four demands against this, in one table

| demand | carried today? | where it fails |
|---|---|---|
| (1a) troops a settlement holds as its own resource | **no** | no store kind is a troop; the population cohort has no `commit` and is never mustered (items 2, 16) |
| (1b) a levy that produces them | **no** | the only act that ever bore the name moved goods; `requisition` now does (item 14) |
| (1c) quality by equipment, experience, commander | **no** on the season path | constants (item 5); presets and officers are reachable only from harnesses (items 8–12); experience has no carrier (item 13) |
| (1d) units as the field's input | **no** | the input is a weight tuple (item 3) |
| (2) the 4/4 Line is a stub | **confirmed** | item 5 |
| (3) composite armies with subformations | **built in the harness, unreachable** | items 8, 9; `march` carries no order of battle (item 15) |
| (4) `levy` wrongly names a store act | **fixed in the tree** | item 14 |

---

## 2. THE TROOP STOCK

### 2.1 What carries it: five candidates, one chosen (J-1)

The research lanes filed three carrier forms (`research/by_lane/00_COMPARATIVE_ANALYSIS.md:79`, RC-2;
`:135`, X-2) [CHECKED-draft]. The brief adds a fourth, a typed troop row. I add a fifth, a split of the
third: a levy separates a company from the population instead of enlisting the whole population.

| | candidate | where it lives | Layer 1 (ratified) | population and food | who acts | new apparatus |
|---|---|---|---|---|---|---|
| **A1** | a stock on the Rung, coupled: a levy lowers cohort `weight` and raises `stores["troops:<kind>"]` by the same headcount (MB K-MB-1, `MB_mass_battle.md:715`) | `Rung.stores` | **breaks** §C.5.1, *"There is NO unit class, at any scale"* (`04:793`), and §C.5's *"a faction as combatant — `claimants : PersonId[]`, STRUCTURAL"* (`04:779-780`): troops reach the field as a count, not as persons. It also strains §B.3 *"NEVER: any social aggregate"* (`04:257`), with men held in a larder | levied men leave `population` (`world_q.py:1048-1078`) and stop eating (`subsistence_draw` feeds persons only, `:803-866`). Levying frees housing that `migrate` can refill | nobody: a stock cannot desert, defect, witness or be wounded (AX-1, `04:120`) | composite store keys (`troops:<kind>:<grade>`), a conversion act from kit to kind, a commander field somewhere |
| **A2** | the same stock, **uncoupled** (SE K-SE-13's first shape, `SE_…md:492`): a `matter_kinds` row, "never a person" | `Rung.stores` | as A1 | war costs no population at all: troops come from nothing, or from coin | nobody | as A1, plus a source that mints troops |
| **B** | a typed troop row: a `Company` record or a YAML troop table | a new carrier | **breaks** §C.5.1 by name (a unit class) and T-l, *"one `Person` class; no subclass exists"* (`04:123`, `:245`) | whatever its fields say | nobody, unless it gets a verb surface of its own | a carrier, matrix rows, gate bases, a loader schema |
| **C** | **troops as persons, split** — **CHOSEN** | a cohort `Person` (the company), split from the settlement's population cohort, bound to the seat by `oblige` | **complies**. §C.5.1's own words, *"units = PersonId[] at weight"* | headcount is conserved: the company still lives at the settlement, so `population` and the larder count it. War deaths lower population | the company deliberates like any person (`populated.py:396-401` [CHECKED-draft]: "a Person in full … it witnesses, holds claims and deliberates"). It can `release` its service (desert), and it dies through `remove_person` | a runtime `weight` writer (H-49), one gate basis, one gate clause widened, one verb row (§3.5) |
| **D** | troops as people, **whole cohort** (FA K-FA-13, `FA_…md:571`; SE K-SE-13's second shape): the population cohort commits to the faction | the population cohort itself | complies | the whole town is the army: every loss is the town's, and every soldier is the town | the town | a `weight` writer and a `commit` the levy imposes |

**Why C:**
- **Layer 1.** C is the only candidate that obeys ratified Layer 1 without amending it. A1, A2 and B
  each need `04 §C.5.1` reopened, and Layer 1 is "binding as agent instruction" (`04:3`) [CHECKED-draft].
- **It reuses what exists for each quality axis:**
  - kit → a rung's `stores`, through `transfer`'s conserved `_shift`;
  - grade → `Person.capability`, which IN-12 step 9's `train` writes;
  - commander → a seat holder, read through `establishment_of`'s `oblige` walk
    (`world_q.py:1508-1533`) [CHECKED-draft].
- **The person's own life comes for free.** Desertion, defection by regard, death and witnessing are
  what R-WORLD needs from an army nobody is watching.

**Why C beats D:**
1. **A levy sets the quantity.** Under D a town fights all-or-nothing. Under C a lord raises a share.
2. **Quality can differ within a town.** Veterans and fresh levies of one settlement are different
   persons, so they carry different grades and different kit.
3. **A levy is service, not belief.** D makes the levy impose a `commit`, and a `commit` is a belief
   ("beliefs (a commit to an OUGHT)", `04:239`; `carriers.py:654-656`) [CHECKED-draft]. Imposing a belief by
   decree is a category error. C imposes an `oblige`, which is service. That is what a levy is, and
   the tree already opens one on someone else's behalf: `determine`'s disposal, gate basis
   `determination` (`state/gate.py:826-847`) [CHECKED-draft].

**What C costs that A does not:**
1. **More persons.** Every levy may mint a `Person` that then deliberates every season. That adds
   chooser load and may crowd other verbs out of scenes, which is the H-163/`commit` shape
   (`hole_register.yaml:3543`) [CHECKED-draft].
2. **Units of one weight.** A company's men are counted in the population's own unit, so the field
   needs a men-per-weight scale (§2.4). A needs one too, unless its stock counts men directly.
3. **The S9 edge.** A company worn down to `weight == 1` is, by S9, no longer a cohort
   (`carriers.py:713-721`) [CHECKED-draft]. It stops eating (24f) and, under J-6's default, stops counting
   as troops. A remnant of one weight unit is a squad of officers' servants, not a company. This is
   recorded as a residual (§8), not fixed by special-casing.

**J-1 is Jordan's** (§9), because he has not ruled the representation and the five lead to different
games. Under A1 and A2, war can be run as accounting. Under C and D, an army is people with somewhere
to live, something to want and a way to leave.

### 2.2 What a company is, field by field

A company is **not a new type**. It is a `Person` (`carriers.py:642-721`) [CHECKED-draft] that one act left
in this state:

| fact | carried by | written by | read by |
|---|---|---|---|
| headcount (in population units) | `Person.weight` | `levy` (split and add); a lost field (casualties) — H-49's missing runtime writer | `population`, `subsistence_draw` (unchanged); the order of battle (§4.2) |
| where it is / where it lives | its `contain` and `reside` Tenures, both to the levied cohort's own rungs | `levy` (on a split); `move` / `migrate` | `mustered` (presence); `home_of`, the larder |
| whom it serves | a live `oblige` Tenure, company → the levying seat, with a declared term (T-n) | `levy` | `establishment_of` (`world_q.py:1508`); the muster (§4.1); the commander (below) |
| its commander | **not stored**: the holder of the seat its `oblige` names (`hold_force`) | — | the order of battle → `Officer` |
| its kit | `Rung.stores` of the company's **own person-rung** (every cohort has one: `populated.py:440`, `Rung(pid, "person")`) [CHECKED-draft] | `transfer` (equip); the salvage clause on death (§4.6) | `troop_kind_of` (§2.3) |
| its troop kind | **not stored**: a Query over the kit | — | the order of battle → `Subunit.of_type` |
| its grade (experience) | `Person.capability[<grade key>]`, an int; an absent key is grade 0 | `train` (IN-12 step 9); a fought field only if J-5 rules so | the order of battle → per-subunit discipline and morale offsets |

**One owner per fact.** The kind and the commander are derived, so neither can drift from what it is
derived from. This matches #445's "a label derived from loadout and training, not a preset"
(`proposals/2026-09-30-character-and-play-surface/08_mass_battle_units.md:114`) [CHECKED-draft], and the
same document's "who — its bodies: a cohort `Person` (weight = headcount)" (`:108`) [CHECKED-draft].

### 2.3 Keys: troop kind × grade

- **The troop kind** is
  `troop_kind_of(w, pid) = the first row of rosters.yaml: troop_kinds, in roster order, whose kit
  the person-rung stores of pid cover at pid's weight`.
  - **What a row is:** an id plus `kit: {matter kind: units per weight}`.
  - **The kit test:** `stores[k] >= kit[k] * weight` for every `k`.
  - **Order:** the roster runs from the most demanding kit to the least. The last row has an empty kit
    and is `levy`, so every company has a kind.
  - **The id is a `TROOP_TYPE_STATS` key** (`registry.py:39-57`). The seam module refuses an id it has
    no preset for, loudly, at the builder (§4.4). That replaces `Subunit.of_type`'s silent "an unknown
    type fills nothing" (`units.py:714-718`) on the season path.
  - **Where it lives:** one Query, in `queries/world_q.py`. It is a world read, like `population`.
- **The grade** is `capability.get(GRADE_KEY, 0)`, clamped to the length of
  `rosters.yaml: troop_grades`.
  - **What a row is:** each row adds a discipline offset and a morale offset to the kind's preset.
  - **Grade 0 adds nothing.** A raw levy fights exactly at its kind's preset (the control).
- **Mixing grades is structural, not averaged.** A levy never adds men to a company with a grade
  above 0 or with kit on its rung (§3.1, decline). Veterans therefore stay their own person and are
  never diluted. This answers K-MB-3's dilution question (`MB_mass_battle.md:717`) by representation.

### 2.4 Quantity: the men-per-weight scale

The season counts people in `weight` units; the engine counts men. One number converts them:
`men_per_weight`, applied **once**, in the host's input builder, to every troop-bearing person's
weight (`troops = weight × men_per_weight`, an int).
- **Not in the module.** The module says it "is not the place to invent one" (`massbattle.py:198-207`)
  [CHECKED-draft], and it receives troops already counted.
- **The value is [OPEN — Jordan tuning].** It and H-170's cohort weight (2 per settlement,
  `hole_register.yaml:3722-3732`) set the size of every field.
- **At the shipped weight:** a settlement's cohort of 2 can be levied for at most 1 (the cohort must
  keep weight ≥ 1, `carriers.py:710`).
- **Where the scale bites:** the MB lane's probe puts the scale where strength starts to matter at
  about 120 troops per side (`MB_mass_battle.md:515`) [CHECKED-draft as a citation]. So
  `men_per_weight ≥ 120` lets a one-company side clear `SUBUNIT_ROUT_FLOOR`. A three-company side at
  that scale takes three settlements' levies.

**Who counts as troops (J-6, default):** only cohort persons (`Person.is_cohort`,
`carriers.py:713-721`).
- **What happens to named persons:** a mustered named person at `weight == 1` is a commander or an
  officer, not men in a subunit.
- **This is not a new branch.** It is plan position `24f`'s rule carried one step: "ONLY A COHORT
  EATS", on Jordan's *"NPC synecdoches that just represent the overall population … i don't think
  having lords and guild members etc worry about subsistence is worthwhile"*
  (`world_q.py:815-822`, ED-IN-0255) [CHECKED-draft]. The synecdoche that eats is the synecdoche that
  fights.
- **The alternative:** every mustered person contributes `weight × men_per_weight`. A named lord
  would then be a hundred men.

### 2.5 Population coupling (J-2)

**Default: headcount-coupled, labour-uncoupled.**
- **A levy conserves headcount.** The cohort's weight falls by `n` and the company's rises by `n`.
  Both reside at the same settlement, so `population(w, rung)` is unchanged [INFERRED from
  `world_q.py:1048-1078`: a sum of `weight` over residents of the subtree].
- **The larder's demand is unchanged.** `want = wt × weight` per person is linear in weight
  (`world_q.py:866`) [CHECKED-draft], so a split eats exactly what the whole ate.
- **War costs population.** Casualties lower weight (§4.6), which shrinks `population` and frees
  `capacity` room.
- **Production does not fall when men are levied, because nothing models labour.** The yield pass
  scales each site's base by its `condition` and the season factor (`loop/matter.py:504-520`)
  [CHECKED-draft]. Nothing in production reads `weight`.
- **The residual:** population has no producer. "No position builds one"
  (`00_COMPARATIVE_ANALYSIS.md:37`, C0 item 5) [CHECKED-draft]. So under this default, war drains the
  realm permanently. That is AM-2's "makes M-SE-1 bite" (`:159`) [CHECKED-draft], and it is named, not
  solved, here.

**Alternatives:**
- **(b) Labour-coupled:** production scales with a settlement's unlevied weight. That adds a labour
  reader to the yield pass: one more object, and a second reading of `weight`.
- **(c) Uncoupled:** troops are recruited from coin. That mints persons from matter, which is A2's
  game.

### 2.6 Conservation: nothing minted or lost without a receipt

The W3 audit's lesson, *"six grain left the world and arrived nowhere"*
(`effects_governance.py:382-384`; `effects_economy.py:170-175`) [CHECKED-draft], applies to people and to
kit:

| motion | conserved quantity | receipt |
|---|---|---|
| `levy` (split) | Σ `weight` over all persons is unchanged: the cohort loses `n` and the company gains `n`, in one `Change` naming both persons | `levy.taken` on both persons and on the new edge |
| `levy` (whole-take: `n == weight`) | no weight moves; the subject is bound as it is | `levy.taken` on the person and the edge |
| `transfer` (equip) | Σ stores per kind, through `_shift` (`effects_shared.py:117-128`) | `transfer.made` on both rungs |
| a lost field | Σ `weight` falls by exactly the casualties: the **one sink**, deaths, recorded per company with the count | `field.lost` plus the company's `weight.changed`; `person.died` on removal |
| a company destroyed | its kit is **not** left on an orphaned rung. `remove_person` pops the person and nothing else (`state/world.py:751`) [CHECKED-draft], so without a clause the kit would sit on a rung no one can reach, which is annihilation by another name. The kit `_shift`s to the rung the field was fought at, in the same `Change`: salvage, which whoever holds the place can `requisition` | `stores.changed` on both rungs |

**The falsifier for every row is the same test:** weigh the world. Sum `weight` over persons and
stores per kind over rungs, before and after the act. The difference must equal the declared sink:
zero for a levy or a transfer, and the reported casualties for a field.

### 2.7 Integer encoding

Every new season quantity is an `int`: `weight`, a grade, a stores count and `troops`.
- **The one float the field produces** is the engine's survivor ratio (`massbattle.py:285-286`,
  `effective_size / size_max`) [CHECKED-draft].
- **It is converted once,** at the host, to an integer per-mille on the `condition_scale` the season
  already uses for fixed-point state (`data/fixtures.py:181-182`, 1000) [CHECKED-draft]:
  `permille = floor(pct × 1000 + 0.5)`.
- **A company's survivors** are `(weight × permille + 500) // 1000`, an integer half-up. No float
  reaches `World`, which `World.content_hash()` reads and the port must reproduce.
- **Out of scope:** today's individual casualty write still multiplies `body` by a float
  (`effects_combat.py:254`) [CHECKED-draft]. That is not this design's write, but §7's TS-6 should route
  it through the same per-mille, so one quantity has one conversion (S-methodology, §8).

---

## 3. THE VERBS

### 3.1 `levy`: raise a company from a settlement's people

`levy` is the one new verb. The row below is illustrative, in the table's own shape, and binds nothing
until it is written into `engine/season/verb_table.yaml` and the loader accepts it.

```yaml
- verb:        "levy"
  scale:       "settlement"
  scale_note:  "a levy draws men from a settlement's people -- the cohort levied IS the subject"
  stratum:     "binding_decision"
  eligibility: ["remit:dispatch"]
  beneficiary: "none"            # taken FOR the seat, as `dispatch`/`revoke` read it
  requires:    "the subject is a person, and the seat's purview reaches where that person is"
  requires_typed:
    all:
      - {form: existence, of: subject, kind: Person,  conjunct: subject}
      - {form: basis,     of: subject, basis: purview, conjunct: authority}
  writes:      ["Person.weight", "Person.weight", "Person.exists", "Tenure.since"]
  emits:       ["levy.taken"]
  emits_on_refusal:
    eligibility: ["levy.unauthorized"]
    authority:   ["levy.unauthorized"]
    subject:     ["levy.refused"]
    write:       ["levy.refused"]
  grade:       "assumption"
```

**Operands.**
- **`subject`** is the cohort levied, a `Person` and therefore a question referent: persons are 805
  of the 4,451 referents measured at plan position `14` (`verb_table.yaml:755`) [CHECKED-draft].
- **`amount`** is in weight units. It comes from where every computed `amount` comes from today: a
  held claim, else the fixtures (H-94; `requisition`'s `requires_typed_note`, `verb_table.yaml:650`)
  [CHECKED-draft]. The fixture is `levy_amount` [OPEN — Jordan tuning].
- **No ninth operand.** Both names are in the closed `requires_operands` roster
  (`rosters.yaml:1649`) [CHECKED-draft].

**Eligibility is `remit:dispatch`.**
- **It reuses an existing remit.** `march` already uses `remit:dispatch` (`verb_table.yaml:668`)
  [CHECKED-draft]. Raising and sending men is one remit, and the roster stays at six
  (`rosters.yaml:311`) [CHECKED-draft].
- **The alternative, a seventh remit act `levy`,** is a ruling, as `requisition`'s own substitution
  note says of itself (`verb_table.yaml:662`) [CHECKED-draft].

**The typed cell** is `requisition`'s authority conjunct, read on a person: the seat's purview must
reach the place the subject is at (`world_q.place_of`, the one owner, per `open_case`'s cell,
`verb_table.yaml:764-769`) [CHECKED-draft].

**What the grammar cannot ask, the effect declines.** The grammar cannot ask "the subject's weight is
at least `amount`": there is no `weight` stem in `REQUIRES_STEMS` (`data/requires.py:717-720`)
[CHECKED-draft], and adding one is a grammar change. So the effect declines it, as `_eff_migrate` declines
"room" (`verb_table.yaml:709`) [CHECKED-draft].

**The effect, `_eff_levy`** (in `loop/effects_governance.py`, beside `_eff_requisition`):
1. Resolve the seat (`_exercised_office`, `effects_shared.py:131-136`), the subject `src`, and `n`.
2. **Decline** (→ `write` → `levy.refused`) when any of these holds:
   - `n < 1` or `n > src.weight`;
   - there is no seat;
   - `n == src.weight` and `src` already holds a live `oblige` to this seat;
   - `n < src.weight` and `src` carries a grade above 0 or holds kit. A split never dilutes veterans
     or splits a kit (§2.3). To part-levy a veteran company, its owner releases it first. That case is
     rare, and it is the price of one grade per person.
3. **Whole-take, `n == src.weight`:** `src` itself becomes the company. No weight moves. This is how a
   seat recalls a released company of veterans with its kit and grade intact, and how it takes a
   whole cohort.
4. **Split, `n < src.weight`:** mint `cid = H(world_seed, tick, actor, f"levy:{src}:{a.id}")`, with
   the id salted on the act, per `_eff_oblige`'s pattern (`effects_governance.py:332-340`)
   [CHECKED-draft].
   - Construct `Person(cid, weight=n, born=…)` and its person-rung `Rung(cid, "person")`.
   - Open `contain` and `reside` Tenures to the same rungs as `src`'s.
   - Lower `src.weight` by `n` and raise the new company's weight by the same, in one `Change` that
     names both persons. The conserved move has one body, a person-side `_shift`
     (`_draft(src, dst, n)` in `loop/effects_shared.py`, beside `_shift`, for `_shift`'s reason:
     the W3 lesson is written once).
5. **Bind:** open `Tenure(company → seat, "oblige", since=tick, term=_new_oblige_term(w, a))`. That
   is the term every service carries (`effects_shared.py:108-114`; fixture `oblige_term`,
   `data/fixtures.py:818`) [CHECKED-draft].

**Writes, and their classes:**

| pair | today | change | why |
|---|---|---|---|
| `(Person, weight)` | steps `[CEN]`, class `MATTER` (`write_matrix.yaml:240-246`) | steps `[CEN, RES, ENC]`, class `MATTER/ACTS` | `levy` writes it at RES. A lost field writes it at ENC, the step `_eff_march` writes `stance` at (`write_matrix.yaml:227-231`) [CHECKED-draft]. It is H-49's missing runtime writer, and `weight.changed` finally has a producer |
| `(Person, exists)` | `[MAT, RES, CEN]` (`:202-204`) | none | a split mints at RES, which the row already admits. IN-52's "no step constructs a `Person`" is wrong (§1, item 17) |
| `(Tenure, since)` for `oblige` | admitted under `T-m` (own) and `determination` (a bench's disposal) | **one new gate basis, `levy`**: an OPENING of an `oblige` whose OBJECT is `via` and whose owner is not the actor, by a seat the actor sits in, granted `dispatch`, whose purview reaches the owner's place. It is authority-bound like `T-o` and `determination` (`state/gate.py:805-847`) [CHECKED-draft] | `determination` is a judging seat's (`:826-831`) and does not fit a lord. Widening it would blur the sentence/service distinction H-173 already warns about (`hole_register.yaml:3765`) [CHECKED-draft] |
| `(Tenure, since)` for the company's `contain` and `reside` | `founding` admits a born subject's **only `contain`**, and nothing else (`gate.py:848-856`) [CHECKED-draft] | **`founding` widened by one clause:** a subject born in this write may also open its single `reside` | a person born at RES needs a home. Census minting at CEN does this without an actor (`census.py:102-107`); a split at RES needs the basis |

**Per-clause refusals** (`04 §B.13` invariant 4, `04:487-492`) [CHECKED-draft]:
- **`levy.unauthorized`** means the SEAT failed. The actor exercised no seat granting `dispatch`, or
  the seat's purview does not reach the cohort.
- **`levy.refused`** means the PEOPLE failed. The subject is no person, there are too few to take,
  the subject is already bound, or it is a graded or kitted company that would be split.

A witness can tell "the lord had no right" from "there was nobody left to take". This is
`requisition`'s split of authority against scarcity (`verb_table.yaml:659`) [CHECKED-draft], applied to men.

### 3.2 The companion acts: each needed, and none of them new

| need | act | reused as it stands? | what the troop stock adds to it |
|---|---|---|---|
| fill a treasury with goods, including arms | **`requisition`** (`verb_table.yaml:629-663`) | **yes, unchanged.** Its role after the rename is exactly the store act: it extracts goods from a rung into the seat's treasury. It raises no troops | nothing. It is the source the kit is drawn from. IN-49 (its question source) keeps its subject under the new name |
| equip a company | **`transfer`** (`:1198`), `from` = the seat's treasury, `to` = the company's person-rung, `kind` = an equipment matter kind | **yes.** `_eff_transfer` moves between any two rungs, conserved (`effects_economy.py:168-240`) [CHECKED-draft] | new `matter_kinds` rows for kit (§6). Whether a transfer to the company's person-rung renews its service term through `_renewals` (which needs the obligee "present at the receiving rung") is **[UNVERIFIED]**; the design needs no renewal from it |
| drill a company (experience without war) | **`train`** (IN-12 step 9, B-Q, unbuilt; it writes `Person.capability`, `_part5.md:73`) | **yes, as planned**, with one data row: the grade key in `verb_capability` | the grade key is a vocation like `copying`. `train` on a company raises its grade one step, up to the drill cap in `troop_grades` (§6) |
| bring companies from several settlements to one muster | **`dispatch`** (`:263`, names a person, writes nothing) + **`move`** (`:720`, the company's own act) | **yes** | nothing. The muster reads presence (§4.1). Whether a company's chooser answers a dispatch by moving is **[UNVERIFIED]** (`dispatch`'s own note: "their own choose decides", `:276`) |
| field the army | **`march`** (`:664-690`) | **row: one declared optional payload key, `order` (§4.3). Effect: the write-back (§4.6)** | the side's composition is read, not chosen at the fold |
| dismiss | **the term's maturity** (MATTER matures `oblige` terms, plan position `17b`, `verb_table.yaml:837`) + **`release`** (`:822-838`, own-eligible: the company ends its own service, which is desertion) | **yes** | nothing. ⚠ **No lord-side dismissal exists, and that is ruled.** D-5, "second-person lever stays refused": no creditor or obligee-side closer on an `oblige` (`verb_table.yaml:838`) [CHECKED-draft]. A lord who wants his levy gone stops paying, and the term runs out. A dismissed company stays a person at its settlement with its kit and grade: a pool of veterans a later whole-take can recall |

### 3.3 What is NOT added, and why

| not added | because |
|---|---|
| a `muster` verb | the muster is a Query, `mustered` (§4.1). A verb would write a fact the Query derives |
| an `equip` verb | `transfer` moves kit; a kit is stores |
| a `disband` or `dismiss` verb | D-5 refuses a lord-side closer; the term and `release` already end service |
| a `recruit` verb (troops for coin) | it mints persons from matter: candidate A2's game, which is J-1's and J-2's alternative, not the default |
| a seventh remit act | `dispatch` covers raising and sending men (§3.1) |
| a merge of companies | nothing needs it. Two companies of one kind, grade and commander fight as one subunit already (§4.2) |
| a `Company` type, a troop field on `Rung`, a stored troop kind | §2.1 and §2.3 |

### 3.4 The corrected role of `requisition`

`requisition` is the store act and nothing else. It moves goods from a rung in the seat's purview into
the seat's treasury (`effects_governance.py:373-412`) [CHECKED-draft]. In this design it is the upstream end
of the kit chain:

`requisition` (ore, coin, arms → treasury) → `transfer` (arms → company) → `troop_kind_of` → the field.

Its name is provisional. J-3 (§9) asks Jordan whether `requisition` stands or `tax` or `tithe`
replaces it.

### 3.5 The meta-rule: every object added, every object cut

**Added (each with the N-line §8 tests):**
1. **A verb row,** `levy`, with its keyed refusals.
2. **An effect,** `_eff_levy`, and a conserved person-side move `_draft` beside `_shift`.
3. **A gate basis,** `levy`, and **one clause** of `founding` (a born person's `reside`).
4. **A matrix edit:** `(Person, weight)` gains RES and ENC.
5. **A Query,** `troop_kind_of`, and **an edit to a Query:** `mustered` gains the seat-establishment
   clause (§4.1).
6. **Registry rows:**
   - `rosters.yaml: troop_kinds`, `troop_grades` and equipment `matter_kinds` rows;
   - fixtures `men_per_weight` and `levy_amount`, each with a hole-register row;
   - the temporary fixture `field_army` (deleted at TS-9).
7. **A record edit:** `MassBattleInput.weights` → `MassBattleInput.sides` (§4.2).
8. **A module function,** `trim_to_command`, beside `build_army` in `modules/` (§4.5).

**Cut:**
1. **The one-Line season construction:**
   - `_weighted_unit`, `_MVP_SUBUNIT_SHAPE`, `_MVP_UNIT_COMMAND`, `_SEASON_FORCE_POWER` and
     `_MIN_TROOPS` (`massbattle.py:170-230`);
   - `MassBattleInput.weights`;
   - the `[GAP …]` line (`massbattle.py:32`).
2. **IN-52's design for good:** `settlements.provision`, `field_provisioning` and LF-1..LF-3. None of
   it was built (§5).
3. **The duplicate `build_army` location:** `systems/mass_battle/sim/engine.py` keeps a re-export
   only.
4. **H-49 and MB-08's U-1,** closed.
5. **K-MB-1's rung stock, K-MB-6's re-pointed bound and SE's uncoupled kind,** each withdrawn as a
   form (§5).

**Net:** one verb, one Query, one basis and one record field, against five module constants, one
record field, one unbuilt module design, one fixture and three plan positions.


