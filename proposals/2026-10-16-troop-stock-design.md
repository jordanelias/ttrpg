# The troop stock: a settlement's recruit pool, the levies raised from it, and the season's order of battle

## Status: PROPOSED (2026-10-16). Corrected twice on the same day against two independent critics' reports, and re-based on Jordan's ruling of that day (below). The second correction **changed the default troop body** from a company `Person` (P) to a troop stock (A); §2.4 says why. Both reconciliation tables are at the end of `_part2`. Not ratified; merge ratifies nothing unless Jordan so rules.
## Lane: MB (the field and the army builder), SE (the recruit pool, the levy stock and its feeding), FA (assembly), IN (the verb row, the registries, the harness subsistence formula). IDs: none allocated.
## Read at the working tree of 2026-10-16, after the `levy` → `requisition` rename. At the second correction `git status --short` lists three modified files, all `proposals/2026-10-16-character-template*.md`, none of them read or cited here [RAN].
## Parts: this file (head, §0–§3) · [`_part2`](2026-10-16-troop-stock-design_part2.md) (§4–§10 and both critic reconciliations), read in that order.

**Reference, not mechanism (CLAUDE.md §0.05).** Nothing here changes how the game behaves. Every
behaviour below becomes true only when the code in §7 is built and a run shows it. Where this document
and code disagree, the code is right and this document is wrong. Locators are `file:line` in the tree
as read.
- **`[CHECKED]`** means the line was re-opened in the **second** correction pass.
- **`[CHECKED-1]`** means it was re-opened in the first correction pass and not in the second.
- **`[CHECKED-draft]`** means it was opened at drafting only.
- **`[RAN]`** means I executed something and quote what it printed (commands in `_part2` §10).
- **`[INFERRED]`** means I reasoned from lines I opened but ran nothing.
- **`[UNVERIFIED]`** means I did not open it.

**The troop verb's name in this document is `conscript`** (§3.1). It is a working name, not a claim.
`levy` is the word Jordan used, and reusing it collides with live text in three registers (J-3, §9).

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

Demand (4) is met by the rename already in the tree. `levy` is free as a verb row but not as a word in
the registers: `engine/season/requirements.yaml` still uses it 23 times and `hole_register.yaml` 19
times for the store act [RAN at the first correction].

---

## 0. VERDICT

1. **Each settlement holds a recruit pool: a store of men it can still raise.**
   - **Where it lives:** a new matter kind, `recruits`, in the settlement rung's `Rung.stores`, through
     the `(Rung, stores)` write-matrix row, which already admits MATTER and RESOLVE [CHECKED-1].
   - **Which rungs hold one:** only rungs whose kind is in a new roster, `pool_rung_kinds:
     [settlement]`, on `march_target_kinds`' precedent (`loop/sides.py:116`) [CHECKED]. A territory or
     the realm holds no pool, so no man is counted twice up the tree (§2.2).
   - **What it derives from:** `recruit_ceiling(w, rung)`, the weight of the cohort persons resident in
     the settlement times a share fixture (§2.2).
   - **How it replenishes:** at MATTER, in its own pass after yield, toward the ceiling and never past
     it (§2.3).
   - **What raising does:** `conscript` moves men from `recruits` into a troop stock on the same rung.
     It **never writes the population cohort** (R-POOL).
2. **A raised troop is a count, not a person (candidate A, the default since the second correction).**
   - **What it is:** a troop stock in the same settlement rung's `stores`, one matter kind per
     experience grade (`troops_raw`, …; §2.7). It eats from the larder where it stands, after every
     person there (§2.5), fights for whoever holds the rung (§4.1), and is moved by `transfer`.
   - **Why it replaced P:** P (a company `Person` minted from the pool) breaks three ruled things that
     A does not touch: ED-WR-0011's closed cast, RR-2's capacity bound on births, and J-16's "never a
     branch on origin". Both candidates amend one line of Layer 1. A violates the fewest ruled
     things (§2.4).
   - **⚠ What A costs:** Layer 1's unit sentence, `units = PersonId[] at weight -- one type. There is
     NO unit class, at any scale` (`architecture/meta/04_CODE_ARCHITECTURE.md:793`) [CHECKED], is
     amended so a side's quantity is a count of troop stocks while its persons still stand and
     command. **That overwrites ratified canon, so it is J-1, escalated (§9).** A troop also loses
     what a person has: it cannot choose to desert, witness, or carry a grudge.
3. **What the ruling settles, and what it does not:**
   - **Settles J-2.** Raising takes nothing from the cohort. The cohort's `weight` is never written by
     this design, and under scarcity its larder row is protected by draw order (§2.5).
   - **Gives the raise a cost:** the pool and the seasons it takes to regrow, and food, because a stock
     eats at the larder where it stands (§2.5).
   - **Does not settle the troop body.** J-1 carries it (§2.4, §9).
4. **⚠ Layer 1 amendment, stated exactly (J-1).** Under A, `04:793` changes and nothing else in §C.5
   or §C.5.1 does:
   - **Kept:** `sides = (faction_q.resolve(proj, A), …)` (`04:792`), the squad line `members ∩
     present-at-rung` (`04:802`), and `claimants : PersonId[]` (`04:780`) [CHECKED]. Who stands on a
     side is unchanged: faction members present.
   - **Amended:** `04:793` would read, in substance, *"units = PersonId[] (who stands and commands) +
     the troop stocks the side fields, counted in `Rung.stores`. A troop is a count, never a record:
     there is still no unit class."*
   - **Under P instead,** `04:793` stays and `04:792`/`:802` are amended (a person with no `commit`
     stands for his lord's faction), **and** ED-WR-0011 must be narrowed (§2.4).
5. **Quality has three axes, and the default reaches two of them in computed play:**
   - **Equipment** is matter in the same settlement's `stores`. The module derives each subunit's
     troop kind from `TROOP_LOADOUT` (`modules/mass_battle/equipment/__init__.py:21-36`)
     [CHECKED-1], the one owner of kind → kit (§2.7). **Reachable in computed play:** a computed
     `transfer`'s `to` is the question's referent (`verb_table.yaml:1211`) [CHECKED-1], and a
     settlement can be a referent [INFERRED]. Under P it was not reachable. Arms still have no
     producer (§6).
   - **Experience** is the grade, carried as which troop kind a man is counted under. ⚠ No computed
     act moves men up a grade until J-5 (c) or a J-13 change (§2.7).
   - **The commander** is the side's general. His Command is 4 for every season commander until
     R-C-1 names a source (`_part2` §4.2 step 6).
6. **The verbs:**
   - **One new verb, `conscript`** (working name; J-3), over a settlement rung (§3.1).
   - **Reused companion acts:** `requisition` fills a treasury with arms; `transfer` moves arms and
     troops between rungs; `march` fields them.
   - **`recruits` is immovable** by every store act. Troop kinds are movable: moving soldiers between
     rungs is assembly (§2.1, §3.2).
7. **Who stands is unchanged. What they field is new.** A side is the members `mustered` already
   returns. Its troops are the stocks on the field's rungs held by the side's faction: at the origin
   for the attacker; at the target for the defender, **plus the target's own `recruits`** (§4.1).
   - **The defence extreme is walked** (second critic, finding 8). Without the pool on defence, a
     settlement nobody had raised would be `Unopposed` to any levy, and `fort_level` and the walls
     would never engage. With it, every held settlement defends with its own men (`_part2` §4.1).
   - **No `service_faction`, no `mustered` clause, no `_side_stance` edit** are needed under A. They
     were P's (§2.4).
8. **The army builder moves across the seam** (`_part2` §4.4). `build_army` moves out of
   `systems/mass_battle/sim/engine.py:213-452` into `modules/mass_battle/` [CHECKED-draft]. The
   season's one-Line construction (`modules/mass_battle/massbattle.py:170-230`) [CHECKED-draft] is
   deleted. The host builds each side's order of battle, one subunit per troop kind and kit at the
   place.
9. **A defect tracked on its own, gated on nothing here (TS-2, `_part2` §7):** `build_army` throws
   away the morale preset of every troop type it builds. The default at
   `systems/mass_battle/sim/engine.py:427-428` pre-empts `Subunit.of_type`'s `setdefault` at
   `modules/mass_battle/hierarchy/units.py:726` [CHECKED-1]. A drafting probe printed `levy power 1
   disc 1 morale 6` where the preset row says morale 2 (`troop_types/registry.py:41`) [CHECKED-1].
10. **Two defects in the harness this design must fix first (second critic, finding 6):**
    - **Men would be sensed as food.** The harness subsistence formula `SUBSIST` sums **every** store
      kind at the person's containing rung (`engine/season/harness/probes.py:144-149`) [CHECKED], and
      it is injected into every realm run (`harness/populated.py:1534`) [CHECKED]. On
      `build_realm(0)` every cohort senses 0 at build; putting `recruits = 2` at each cohort's rung
      makes all 37 sense 1000 [RAN]. The fix reads only the kinds that carry a subsistence weight
      (§2.5).
    - **Draw order.** `subsistence_draw` walks persons in sorted id order
      (`queries/world_q.py:858`) [CHECKED]. Troop stocks draw after every person (§2.5).
11. **What this cuts:**
    - **IN-52's feed and LF-1..LF-3 are withdrawn as forms.** A stock eats at the larder where it
      stands, through `subsistence_draw`, not from a treasury ration (`_part2` §5).
    - **IN-49 is re-framed** as the store act's question source.
    - **Closed:** MB-08's #445 U-1. **Not closed:** H-49 (`Person.weight` gains no writer under A).
    - **Research rows:** listed in `_part2` §5.
12. **Grade: paper.** Nothing in §2–§4 is built. Probes run: the morale preset (drafting); the
    shipped `oblige` edges and the realm at cohort weight 4 (first correction); `SUBSIST` with and
    without `recruits`, at build and after one season, and the draw-order id comparison (second
    correction). §7 gives the build order; each step's exit is an execution artifact.

---

## 1. THE PROBLEM AS CODED

Each fact below is at its source. Together they answer the four demands and the ruled constraints.

### 1.1 Who fights a season field

1. **A field's two sides are faction members present at a place.**
   - **Attacker:** `sides_of` musters `mustered(w, origin, faction)`. `origin` is the actor's nearest
     settlement up his `contain` ancestry, and `faction` is the faction of the seat the act was
     exercised through, converted by `faction_prop_id` (`engine/season/loop/sides.py:77-85`)
     [CHECKED].
   - **Defender:** the provider musters `mustered(w, rung, subject)` at the target
     (`engine/season/seam/wrappers/mass_battle.py:233`) [CHECKED]. `subject` is the target's holder's
     faction, `holder_faction_of(w, target)` (`loop/effects_combat.py:240`) [CHECKED].
   - **An empty defending side is `Unopposed`**, and the module is never called
     (`mass_battle.py:235-248`) [CHECKED]. So `fort_level` and `walls_dr`, which the module reads
     (`modules/mass_battle/massbattle.py:273`, `:342-371`) [CHECKED], never engage for it.
   - **What `mustered` reads:** "This faction's members present in `rung_id`'s subtree"
     (`queries/world_q.py:1256-1272`) [CHECKED-1]. Membership is a live `commit`.
2. **The population never fights.** It is one cohort `Person` per settlement, with no `commit`,
   minted with `contain` and `reside` on the settlement (`harness/populated.py:439-442`) [CHECKED-1].
   Its weight is 2 at all 37 settlements (H-170, `hole_register.yaml:3722-3734`) [CHECKED].
3. **A side is its members' summed `Person.weight`** (`seam/wrappers/mass_battle.py:190-193`)
   [CHECKED-draft]. The input record carries nothing about composition, kit or command
   (`queries/inputs.py:62-100`) [CHECKED-draft].
4. **The march's write-back touches persons only.** `_eff_march` takes the losers' person ids, and
   returns `NO_CHANGE` when none is a person (`loop/effects_combat.py:225-230`) [CHECKED]. Casualties
   land on `body`, through a float (`:254`), and every loser gets a morale row and a grudge row
   (`:256-261`) [CHECKED].

### 1.2 What the module builds from that

5. **Every side is one Line subunit of bare `infantry`, at power 4, command 4 and discipline 5**
   (`massbattle.py:170-196`), under the module's own label "minimum-viable defaults … no canonical
   spec exists" (`:160-166`) and its `[GAP …]` header (`:32`) [CHECKED-draft]. Demand (2) rules this
   a stub.
6. **Troops are the raw weight sum**, `troops=max(float(weight), _MIN_TROOPS)` (`massbattle.py:226`),
   against `SUBUNIT_ROUT_FLOOR = 80` (`config.py:117`) [CHECKED-draft]. The MB lane's probe: 0
   attacker wins in 20 at ≤80 troops, both sides routed every run, and "one present defender holds any
   settlement against any army the realm can raise" (`research/by_lane/MB_mass_battle.md:434`, M-MB-1)
   [CHECKED as a citation; not re-run].
7. **Morale is the only side quality that reaches the field.** `_side_stance` weights by
   `Person.weight` and finds each person's faction through `faction_holding`, which reads live
   `commit` edges only (`seam/wrappers/mass_battle.py:126-148`; `world_q.py:1436-1438`) [CHECKED-1].

### 1.3 What the harness can build, and the season cannot reach

8. **A composite army constructor exists on the wrong side of the seam:** `build_army(specs, …,
   officers=())` (`systems/mass_battle/sim/engine.py:213-452`), with roles gated by `role_allowed`
   and spans checked against Command and `SUBUNIT_CAP = 11` (`:99`, `:304-345`, `:369-371`)
   [CHECKED-draft]. `modules/mass_battle/` imports nothing from `systems/` (`MB_mass_battle.md:368`)
   [CHECKED-draft as a citation].
9. **Troop-type presets exist, including a `levy` row** (power 1, discipline 1, morale 2;
   `troop_types/registry.py:39-57`, `:41`) [CHECKED-1], applied by `Subunit.of_type`
   (`hierarchy/units.py:712-730`) [CHECKED-draft].
10. **The morale preset is dead on the harness path** (§0 item 9).
11. **Equipment is a catalogue:** `ARSENAL`, `ARMOURY` and `TROOP_LOADOUT`
    (`equipment/__init__.py:21-36`) [CHECKED-1]. `levy` is `light_cut`/`none`; `archers` and
    `mounted_archers` share `bow`/`light`; no row names a mount.
12. **Officers derive Command from charisma and cognition only when both are given and
    `COMMAND_SIGMA_ENABLED` is on** (`hierarchy/units.py:2711-2716`; `config.py:530`) [CHECKED-1].
    `Unit.officers` is bookkeeping (`:2793-2797`) [CHECKED-draft]; `build_army`'s span check reads
    `Officer.command`.
13. **Experience has no carrier** (`MB_mass_battle.md:449`, M-MB-16) [CHECKED-draft as a citation].

### 1.4 The verbs, the stock, and the subsistence model

14. **`requisition` moves goods, conserved, into the seat's treasury.** Eligibility `["remit:issue",
    "presence:<rung>"]`; typed cell `basis` (purview, conjunct `authority`) and `scalar_threshold`
    (`stores`, `key: kind`, `threshold: amount`, conjunct `stores`) (`verb_table.yaml:629-652`)
    [CHECKED]. Its effect shifts through `_shift`, "the one body of every act that moves stores
    between two rungs" (`loop/effects_shared.py:117-128`) [CHECKED-1].
15. **A typed cell's `key:` is an operand, not a literal.** `ScalarThreshold.check` binds `key` from
    the act's operands and observes `f"{scalar}:{k}"` (`engine/season/data/requires.py:295-307`)
    [CHECKED]. `operands()` returns it, checked at load against the form's `needs:`
    (`requires.py:215`, `:288-289`; `rosters.yaml:1847`) [CHECKED].
16. **A computed act's `kind` and `amount` come from one generic chain** (`decision/options.py:846-875`)
    [CHECKED]: a writ claim, then a shortfall claim, then `store_kind_of(p, q)` (the question's own
    `stores:<kind>` claim, `:630-651`) [CHECKED], then the fixtures `default_store_kind = "grain"` and
    `default_transfer_amount = 1` (`data/fixtures.py:491`, `:495`) [CHECKED]. A per-verb branch in
    that chain is what its docstring forbids: "a per-verb table would be the special case `G2` is
    actually about" (`options.py:763-767`) [CHECKED].
17. **`march` writes only the losers** (ED-IN-0279, `verb_table.yaml:682`) [CHECKED-draft].
18. **The stock and its clock.** `matter_kinds` is an open registry (`rosters.yaml:1279-1290`)
    [CHECKED-1]. MATTER's per-rung loop iterates **every** rung (`loop/matter.py:485`), credits yield
    from Sites, and `continue`s on a rung that produced nothing (`:521-523`) [CHECKED]. Yield has no
    ceiling.
19. **Only `grain` and `salt` are eaten.** `subsistence_weight` carries those two rows: "timber, ore
    and coin are stored and not eaten" (`rosters.yaml:1371-1387`) [CHECKED]. `subsistence_draw` loops
    over that registry, so an unweighted kind is never drawn (`world_q.py:863-866`) [CHECKED].
20. **The sensed subsistence does not agree.** `SUBSIST` sums every kind in the containing rung's
    `stores` (`harness/probes.py:144-149`) [CHECKED]; `sense` feeds it to every person's deliberation
    (`loop/deliberate.py:119`, `:536`) [CHECKED]. Coin, timber and ore are already sensed as food
    today; any new stored kind would be too.

### 1.5 The rulings this design must meet

21. **ED-WR-0011, RULED (Option A):** *"A CLOSED AUTHORED CAST … Everyone who will ever matter exists
    at tick 0 and the cast only shrinks"*; *"B requires a producer for Person that A forbids"*
    (`registers/editorial_ledger_wr_archive.jsonl:13-14`) [CHECKED]. Jordan's words: *"World-gen NPC
    count, for now, is just the 46 NPCs we built. We will return much later."* The code applies it to
    cohorts: "`ED-WR-0011` option A -- nothing mints one at run time" (`world_q.py:824`) [CHECKED];
    H-170, "authored at world-gen and never minted by a clock" (`hole_register.yaml:3725`) [CHECKED].
    - **The contrary reading:** X-4, "ED-WR-0011 closes the NAMED cast 'for now'; it does not reach a
      cohort's `weight`" (`research/by_lane/00_COMPARATIVE_ANALYSIS.md:204`) [CHECKED]. Even X-4
      licenses a cohort's weight growing, not a new cohort `Person`.
    - **A run-time producer already exists for individuals:** CENSUS individuates a demanded person at
      weight 1 (`loop/census.py:105-112`) [CHECKED], licensed by Layer 1's `loop/census` row
      (`04:179`) [CHECKED].
22. **RR-2 / ED-SE-0051:** "capacity bounds POPULATION (its floor is *'applied here to births rather
    than acts'*)" (`world_q.py:1050-1051`) [CHECKED]; `seat_cohorts` refuses a cohort above capacity
    (`harness/populated.py:401-432`) [CHECKED]. `population` reads `reside`; `subsistence_draw` reads
    `contain` through `home_of` (`world_q.py:856`, `:994-1002`) [CHECKED].
23. **J-16 on H-173, delegated-ruled [ASSUMPTION; medium; Jordan to correct]:** "a sentence differs
    from a service `oblige` by term and the basis that opened it, never by a branch on origin"
    (`hole_register.yaml:3772`) [CHECKED]. `Term.declared_by` is "the opening act, or the act that
    last RENEWED the term" (`state/carriers.py:50-51`) [CHECKED], and `_renewals` replaces it with the
    paying act (`loop/effects_economy.py:309`) [CHECKED].

### 1.6 The four demands and the ruling against this, in one table

| demand | carried today? | where it fails |
|---|---|---|
| (1a) troops a settlement holds as its own resource | **no** | no store kind is a man (items 2, 18) |
| (1b) a levy that produces them | **no** | the only act that bore the name moved goods (item 14) |
| (1c) quality by equipment, experience, commander | **no** on the season path | constants (item 5); presets and officers are harness-only (items 8–12); experience has no carrier (item 13) |
| (1d) units as the field's input | **no** | the input is a weight tuple (item 3) |
| (2) the 4/4 Line is a stub | **confirmed** | item 5 |
| (3) composite armies with subformations | **built in the harness, unreachable** | items 8, 9 |
| (4) `levy` wrongly names a store act | **fixed in the tree** | item 14 |
| R-POOL: a pool of its own that replenishes, the cohort untouched | **no** | no carrier of raisable men; the one replenishing clock has no ceiling (item 18) |

---

## 2. THE RECRUIT POOL AND THE TROOP BODY

### 2.1 Where the pool lives: four homes, one chosen

| home | what it adds | Layer 1 | what it gets wrong |
|---|---|---|---|
| **S. a `recruits` kind in the settlement rung's `stores` — CHOSEN** | one `matter_kinds` row; a ceiling Query; a capped credit at MATTER; one immovability roster | none: `(Rung, stores)` already admits `[MAT, RES]` [CHECKED-1] | a store is movable by `_shift`'s callers, and `SUBSIST` senses it as food (§1.4 item 20). Both are closed below |
| **E. `Rung.envelope`** | a producer for a ratified, unwritten field (H-171); RES added to `(Rung, envelope)` | strains `04:179`, which gives `envelope` to CENSUS alone [CHECKED] | its ratified meaning is "the population not individuated as persons" (`world_q.py:1065`) [CHECKED-1], which is the population itself, not its raisable men; and its declared shape is a list of age bands no position built |
| **G. a `muster` Site kind whose `condition` is the pool** | a site kind, its `wear_per_season` and `band_floors` rows (`rosters.yaml:1258-1263`) [CHECKED-1], one Site per settlement | none | a Site is fabric: `restore` and wear would act on a roll of men, and the pool would be a fraction, not a count |
| **F. a new field on `Rung`** | a carrier field, a matrix row, an event kind | **amends** `04:255`'s `Rung := ( …, envelope, exists )` [CHECKED-1] | costs a Layer 1 amendment for a value `stores` can carry |

**Why S:** it composes on the stock that exists (a debit at RESOLVE, as `requisition`'s; a credit at
MATTER, through yield's write path); it counts men in whole units the grammar can test; it amends
nothing ratified.

**The first draft's case against E was overstated** (second critic, finding 9). It said a pool in
`envelope` "would represent the same people twice". Under P that objection applied to S equally: S's
pool also derives from the cohort's weight, and P's minted company was added to `population`. Under A
neither S nor E adds a person or a resident, so "twice" decides nothing. What still decides against E
is `04:179` (CENSUS is its one writer), its meaning (the population, not the share of it that can
stand in the ranks), and its unbuilt age-band shape.

**Two closures S needs:**
- **A man in the pool is not goods.** A roster, `rosters.yaml: immovable_kinds: [recruits]`; a
  predicate, `movable(w, kind)`, read by `_eff_requisition` and `_eff_transfer` before they write
  (each declines to its own `write` refusal); `_shift` asserts it as the last line of defence. Troop
  kinds are **not** in the roster: moving a raised levy between rungs is assembly (§3.2).
- **A man is not food.** `SUBSIST` is fixed to sum only the kinds `subsistence_weight` names (§2.5).

### 2.2 What the pool derives from: the ceiling

`recruit_ceiling(w, rung)` is a Query in `queries/world_q.py`, beside `population` and `capacity`:

```
recruit_ceiling(w, rung) = 0                                         if rung's kind ∉ pool_rung_kinds
                         = ( Σ weight of cohort persons resident under rung × recruit_share + 500 ) // 1000
```

- **The base is the settlement's own people:** cohort persons (`Person.is_cohort`) whose `residence_of`
  is in the rung's subtree, read as `population` reads it (`world_q.py:1048-1078`) [CHECKED].
  - **Why only cohorts:** a named person at weight 1 commands; he is not men in the ranks (§2.6).
  - **No service filter is needed under A.** The first correction excluded cohorts holding a live
    `oblige`, so a minted company could not enlarge its own ceiling. A troop stock is not a person and
    never enters the base. (Under P the filter is still needed, and the second critic, finding 2,
    shows a renewed company slipping through it; §2.4.)
- **Which rungs hold a pool** (second critic, finding 7): only rungs whose kind is in
  `rosters.yaml: pool_rung_kinds`, shipped `[settlement]`, on `march_target_kinds`' precedent, a
  closed roster read where the rung is in scope (`loop/sides.py:93-116`) [CHECKED]. Without the
  filter, a territory's ceiling would sum its settlements' cohorts again.
- **`recruit_share`** is per-mille. **[OPEN — Jordan tuning]**, with a hole-register row and a sweep
  (§6). Integer, half-up, on `condition_scale`'s per-mille convention (`data/fixtures.py:182`)
  [CHECKED-1].
- **At the shipped data every ceiling is equal:** all 37 cohorts weigh 2 (H-170), so every ceiling is
  `2 × recruit_share / 1000`. H-170's own sweep would spread them [CHECKED].
- **Not added:** `capacity` (housing, not people), a garrison's condition, the larder's fill.

### 2.3 How the pool replenishes

At MATTER, **in its own pass after the yield loop**, over rungs whose kind is in `pool_rung_kinds`,
sorted by id, through the same `w.write("stores", …)` and `stores.changed` emission yield uses:

```
growth   = ( recruit_ceiling(w, rung) × recruit_regrowth + 500 ) // 1000
recruits ← min( recruit_ceiling(w, rung), recruits + growth )
```

- **Why its own pass, not inside yield's loop** (second critic, finding 7): yield's loop visits every
  rung and `continue`s on any rung with no yield (`matter.py:485`, `:521-523`) [CHECKED]. Placed
  after that line, regrowth would silently skip every settlement with no producing Site. Placed
  before it, regrowth would run on every rung kind. A separate pass with the kind filter does
  neither.
- **The precedent is yield's write**: a credit to `stores` at MATTER (`matter.py:525-536`) [CHECKED].
  The difference is the ceiling: the pool stops there, so a quiet settlement never banks an army.
- **No write when nothing changes.** A full pool writes and emits nothing.
- **`recruit_regrowth`** is per-mille of the ceiling per season. **[OPEN — Jordan tuning]**. Sweep 0
  (the control: a pool that never refills), 250, 1000 (§6).
- **Not scaled by `season_factor`.** Tying recruits to the harvest is available and not asked for.
- **World-gen fills every pool to its ceiling**, in `harness/populated.py` after `seat_cohorts`. That is
  a derived value, not an authored number.
- **This is a new clock write,** not "no new mechanism" (second critic, check (a)). It is counted in
  §3.5.

### 2.4 The troop body under the pool: the candidates re-compared (J-1)

R-POOL fixes where troops come from. It does not fix what a raised troop is. The second critic showed
that the first correction chose P without weighing three ruled constraints in its path. Re-run,
honestly, against every ruled thing:

| ruled constraint | **P** — a company `Person` minted from the pool | **A** — a troop stock on the rung (**DEFAULT**) | **P′** — P without `reside`, dissolution keyed on state | **B** — a typed troop row |
|---|---|---|---|---|
| **ED-WR-0011** (RULED, Option A) | **violates** as the code reads it for cohorts (`world_q.py:824`; H-170) [CHECKED]. X-4's contrary reading frees a cohort's weight, not a new cohort `Person`. CENSUS's weight-1 individuation is the nearest precedent and is not a cohort | **complies:** mints nobody | **violates,** as P | complies |
| **RR-2 / ED-SE-0051** (RULED) | **violates as written:** a minted `reside` is a birth, and P skipped the capacity check by fiat ("an army camps") | **complies:** a stock is not population | **complies:** no `reside`, so not a resident; it still eats, because the draw reads `contain` (`world_q.py:856`) [CHECKED] | complies |
| **J-16 / H-173** (delegated-ruled) | **violates:** `is_company` reads why the edge was opened, and reads it off `Term.declared_by`, which renewal overwrites (§1.5 item 23). After one paid term a company stops being a company and never dissolves | **complies:** no `oblige`, no dissolution | **narrowed:** "a cohort with no `reside` whose last `oblige` closes dissolves at the rung it stands on" reads state, not origin. Whether a state only companies have is an origin branch in disguise is J-16's to say | complies |
| **04 §C.5.1** (RATIFIED, ED-IN-0204) | **amends** the muster lines `04:792`, `:802` | **amends** the unit line `04:793` | amends `:792`, `:802` | **amends** `:793` and T-l, "one `Person` class; no subclass exists" (`04:123`) [CHECKED] |
| **R-POOL** (Jordan) | complies at surplus. **Under dearth it fails:** a minted id from `H(…)` sorts before `cohort_…` [RAN], and the draw walks sorted ids, so the company eats first | **complies,** with the draw order specified in §2.5 | as P unless the order changes | depends on fields |
| **ED-IN-0279** (RULED) | complies | complies | complies | complies |
| **ED-IN-0255 / `24f`** (only a cohort eats) | complies: a company is a cohort | **amends the code rule, not the ruling:** troop stocks join the draw after persons. The ruling's words exempt lords and guild members, not masses (`world_q.py:815-822`) [CHECKED] | complies | — |
| **ruled things violated** | **4** (two fixable inside P: RR-2 by P′, R-POOL by draw order) | **1** (Layer 1), plus a code-rule amendment | **3** | **2** |

**The default is A**, because it violates the fewest ruled things: one, Layer 1's unit line, against
P's four. P′ shows that two of P's breaches can be repaired, but its two that cannot (ED-WR-0011 and a
Layer 1 amendment of its own) still out-count A's one.

**What A loses, stated as plainly as P's breaches:**
- **A troop cannot choose.** It does not deliberate, so it cannot desert by `release`, defect by
  regard, or witness its lord's orders. P had all three.
- **A troop carries no grudge.** The morale and grudge rows `_eff_march` writes land on the persons
  present (the commanders), as today, and are read back through them (`_part2` §4.1).
- **What survives without a person:** defection follows the rung's holder, so a lord who keeps his
  settlement when he defects takes its levies with him (NPC5, `_part2` §4.7). Hunger takes men off a
  stock that is not fed (§2.5). Kit stays with the town.
- **What A gains besides the rulings:** equipment is reachable in computed play (§0 item 5); no chooser
  load; no S9 remnant (a stock of 1 is a valid stock); no gate basis, no `founding` clause, no
  dissolution rule, no `service_faction`, no muster or morale-reader edit; the first critic's
  findings 2, 3, 13 and 16 lose their object.

**If Jordan takes P instead,** J-1 must also **narrow ED-WR-0011** to the named cast, on X-4's reading
(`00_COMPARATIVE_ANALYSIS.md:204`) [CHECKED], with CENSUS's individuation (`census.py:105-112`) as the
precedent for a run-time `Person`. It then needs, at least: P′'s no-`reside` form (RR-2); a dissolution
rule that reads no origin (J-16), or J-16 overturned; the draw-order rule of §2.5; the `_rehome`
safety comments corrected, because they rest on "nothing in `loop/` or an effect constructs [a
Person]" (`loop/matter.py:108-121`; `state/world.py:792-805`) [CHECKED], already false since
`census.py:105`, and `_eff_conscript` would be the first act effect to do it (construct the `Person`
before adding its tenures). P's full apparatus is kept in `_part2` §4.8.

**The contrary reading of demand (1), inside J-1:** "their own resource" reads toward "a rung-held
carrier" (`00_COMPARATIVE_ANALYSIS.md:202`) [CHECKED]; the MB lane reads the demand as "the field's
troop count should come from a levied stock, not from a conversion of summed weight"
(`MB_mass_battle.md:434`) [CHECKED]. A meets both: the stock is rung-held, and the count is the stock,
converted once (`men_per_weight`, §2.8) and never from summed member weight.

### 2.5 What a raise does to the settlement

- **The cohort is untouched.** `conscript` writes one rung's `stores`: `recruits` down, a troop kind up,
  in one `Change`. The cohort's `weight`, stance and `subsistence_draw` row are byte-unchanged
  (R-POOL; TS-4's falsifier).
- **A raised levy eats where it stands, after the people.** `subsistence_draw`, the one owner of who
  eats (`world_q.py:850-880`) [CHECKED], gains a second kind of mouth: every troop stock on a rung, at
  `want = subsistence_weight[k] × count`, drawn **after every person** at every rung, rungs in sorted
  id order. Its rows are keyed by `(rung, troop kind)`, never by a person id.
  - **Why after:** under scarcity the town's people are fed first, so a raise never shortens the
    cohort's row in the season it eats. That is R-POOL kept under dearth, not only at surplus
    (second critic, finding 6).
  - **A short stock loses men.** MATTER's dearth step, which falls a short person's `body`, debits a
    short stock in proportion to its unmet want, on §2.8's half-up per-mille rule. The exact form
    is fixed at TS-11 **[OPEN]**; the sink is named and receipted (§2.8). Where in `loop/matter.py`
    the body write reads the draw is **[INFERRED]** from `matter.py:485-503` [CHECKED], not traced.
  - **`demanded` and `delivered`** sum the draw, so a settlement's need now includes its levies. Their
    docstrings, which say an eater is a cohort, are edited with the rule.
  - **A residual, named:** across seasons, a levy can eat a surplus that would have fed the cohort
    later, and the cohort's `body` (never its `weight`) can then fall for dearth. That reads R-POOL
    as protecting the cohort's size, which is what MATTER never writes. If Jordan reads it wider, a
    stock must eat only from a reserved share, which is a second rule.
- **Men are not sensed as food.** `SUBSIST` (`probes.py:144-149`) [CHECKED] sums only the kinds with a
  `subsistence_weight` row. Probe on `build_realm(0)` [RAN]: at build every cohort senses 0 (the
  larders are empty until the first yield); `recruits = 2` at each cohort's rung moves all 37 to
  1000. After one season all 37 sense 1000 with or without it (saturated). So the defect bites at the
  first deliberation and under dearth. **This fix moves goldens**, because coin, timber and ore stop
  being sensed as food too; the size of that move is **[UNVERIFIED]**, measured at TS-3.
- **`population` does not change.** A stock is not a resident, so `migrate` is unaffected and RR-2 is
  not engaged.
- **Production does not fall,** because nothing models labour (`matter.py:504-520`) [CHECKED], and
  R-POOL makes that the ruling.
- **War costs food, the pool, and the seasons the pool takes to refill.** Deaths fall on stocks; the
  cohort is never written.

### 2.6 Who counts as troops

**Only troop stocks, plus the pool on defence (`_part2` §4.1). No person fields men.** A named person
at `weight == 1` commands. A cohort person fields nothing either, even if it ever holds a `commit`: its
men are counted in the pool, and fielding its weight too would count them twice.
- **CLAUDE.md §0's ladder, step 4:** `24f`'s "ONLY A COHORT EATS", on Jordan's *"NPC synecdoches that
  just represent the overall population"* (`world_q.py:815-822`, ED-IN-0255) [CHECKED]. The mass is
  the pool and the stock, never a person.
- **So `Person.weight` stops being a battle input** (`_part2` §4.5).

### 2.7 Keys: troop kind × grade

- **The grade is the troop stock's matter kind.** `rosters.yaml: troop_grades` lists ordered rows
  `{id, discipline: +d, morale: +m}`; the loader derives one `matter_kinds` row per grade, named
  `troops_<id>` (`troops_raw`, …). One owner, the grade roster; no second list.
  - `conscript` always credits grade 0 (`troops_raw`).
  - **Veterans are never diluted** (K-MB-3, `MB_mass_battle.md:717`): two grades on one rung are two
    stocks and two subunits, never averaged.
  - **No computed producer of grade** until J-5 (c) (a fought field moves survivors one grade up) or
    a J-13 change. Hand-built and player acts can move men between grade kinds only through a future
    `train`; none is designed here.
- **The troop kind is derived by the module from the kit, from `TROOP_LOADOUT`, its one owner.**
  - **The host passes kit, not a kind:** for each grade stock at the field's rung, its count and the
    rung's stores of equipment kinds. The seam reaches the module by an entry string, not an import
    (`seam/wrappers/mass_battle.py:72-78`) [CHECKED-1], so the kind is decided module-side.
  - **The rule** is `kind_for_kit(kit, men)`, beside `TROOP_LOADOUT`: it walks `TROOP_LOADOUT`'s rows
    heaviest armour first (`ARMOURY` order), then key order, and gives each row as many of the men as
    the kit covers (one unit of the row's weapon class and one of its armour class per weight unit;
    armour `none` needs nothing). It returns `((kind, men), …)`. The remainder is the module's
    declared unarmed kind, `levy`, a constant beside `TROOP_LOADOUT`.
  - **When stocks of two grades share one rung's kit,** the higher grade is equipped first. That is a
    rule, not an accident of the store; **[OPEN — MB]** if Jordan prefers the reverse.
  - **What the single owner exposes as MB data [OPEN]:** `mounted_archers` is unreachable by kit;
    `cavalry` needs no horses; `knights_templar` is reached by `heavy_blunt`/`heavy`
    (`equipment/__init__.py:30`) [CHECKED-1]. A mount column belongs in `TROOP_LOADOUT`.
- **Kit is the town's.** It stays in the settlement's `stores` whatever happens in a field. A lost
  battle kills men, not swords. That is an abstraction, named.

### 2.8 Quantity, conservation and integers

**Men per weight.** The pool and the stocks count in `weight` units, the unit cohorts eat in. One
number converts them to men: `men_per_weight`, applied **once**, in the host's order of battle:
`troops = count × men_per_weight`, an int. **[OPEN — Jordan tuning]**. For every falsifier run it is
fixed at **250**: one weight unit is 250 men, and a full shipped pool of 2 is 500 men, clear of
`SUBUNIT_ROUT_FLOOR = 80` and of the ≈120-troop scale the MB lane measured (`MB_mass_battle.md:515`, `:521`) [CHECKED-draft as citations; the second critic re-opened
them]. The weight unit is a dwelling's worth of people (H-170), and capacity and subsistence read it
too, so `men_per_weight` is the one bridge between the season's people and the engine's men.

**Conservation.** Nothing is minted or lost without a receipt (the W3 lesson, *"six grain left the
world and arrived nowhere"*, `effects_shared.py:117-128`) [CHECKED-1]:

| motion | conserved quantity | receipt |
|---|---|---|
| regrowth (MATTER) | `recruits` rises by `growth`, capped: the one **source** of men | `stores.changed` on the rung |
| `conscript` | `recruits` falls by `n` and `troops_raw` rises by `n` on the same rung, one `Change` | `conscript.taken` |
| `transfer` (troops or kit) | Σ stores per kind, through `_shift` | `transfer.made` on both rungs |
| a lost field | the losing stocks fall by the casualties, and the defending pool by its share: a **sink**, deaths | `field.lost`, `stores.changed` |
| an unfed stock | the stock falls by its unmet share: a **sink**, hunger | `stores.changed` with the shortfall `observed` |

**The falsifier for every row is one test: weigh the world.** Sum stores per kind over rungs before
and after; the difference equals the declared sources and sinks.

**Integers.** The pool, a ceiling, a stock, a grade and `troops` are ints. The one float the field
produces is the engine's survivor ratio (`massbattle.py:285-286`) [CHECKED-draft], converted once at
the host to per-mille, `floor(pct × 1000 + 0.5)`. A stock's survivors are `(count × permille + 500)
// 1000`. **One rounding rule:** half-up per-mille, for the ceiling, the growth and the survivors.
Today's individual casualty still multiplies `body` by a float (`effects_combat.py:254`) [CHECKED];
TS-6 routes it through the same per-mille.

### 2.9 When does a levy end?

**Under A there is no service to end.** A stock stands until it is killed in a field, starves, or is
moved. No term, no `oblige`, no dissolution rule and no read of why anything was opened (J-16 kept).
- **The bound on armies is food.** The pool refills, so a seat could raise every season. Each raise
  adds mouths at that rung (§2.5), and a larder that cannot feed them sheds men. Yield is finite, so
  the stock is bounded by what the place produces. TS-11's falsifier measures the bound.
- **No stand-down act is added.** A seat that wants its men home has no verb for it. That is an
  addition only if Jordan asks (a `conscript` inverse, troops → `recruits` up to the ceiling); it is
  listed under J-1, not built.
- **Veterans persist by construction** as grade stocks, so J-5's option (d) becomes moot under A.

---

## 3. THE VERBS

### 3.1 `conscript`: raise a levy from a settlement's pool

The row below is illustrative, in the table's own shape. It binds nothing until it is written into
`engine/season/verb_table.yaml` and the loader accepts it.

```yaml
- verb:        "conscript"
  scale:       "settlement"
  scale_note:  "men are raised from a settlement's recruit pool -- the settlement IS the subject"
  stratum:     "binding_decision"
  eligibility: ["remit:dispatch"]
  beneficiary: "none"            # taken FOR the seat, as `dispatch`/`revoke` read it
  requires:    "the seat's purview reaches the subject, and the subject's stores of `kind` cover the amount"
  requires_typed:
    all:
      - {form: basis,            of: subject, basis: purview, conjunct: authority}
      - {form: scalar_threshold, of: subject, scalar: stores, key: kind, threshold: amount,
         comparator: ">=",       conjunct: stores}
  writes:      ["Rung.stores"]
  emits:       ["conscript.taken"]
  emits_on_refusal:
    eligibility: ["conscript.unauthorized"]
    authority:   ["conscript.unauthorized"]
    stores:      ["conscript.refused"]
    write:       ["conscript.refused"]
  grade:       "assumption"
```

**The typed cell is `requisition`'s, conjunct for conjunct** (second critic, finding 10, applied by
making it so): `basis`/purview as `authority`, and the `stores` threshold keyed `kind` as `stores`
(`verb_table.yaml:637-650`) [CHECKED]. The first correction's `existence` conjunct is dropped:
`requisition` carries none, and the purview basis already fails on a subject that is not a rung.
**It differs in eligibility:** `remit:dispatch` (raising men is the remit `march` uses,
`verb_table.yaml:668`) [CHECKED-draft], and no `presence:<rung>` alternative. That alternative is
declined for every computed act anyway, "because the ARGUMENT IS A PLACEHOLDER" (`options.py:380`,
H-75) [CHECKED].

**Operands, and the `kind` defect** (second critic, finding 1, applied):
- **`subject`** is the settlement rung.
- **`kind` is an operand, not a literal** (§1.4 item 15). In computed play it comes from the generic
  chain (§1.4 item 16), which yields `grain` unless the question is about a `stores:<kind>` claim. A
  per-verb default there is forbidden (`options.py:763-767`) [CHECKED]. So:
  - **the effect declines `kind != "recruits"`** (→ `write` → `conscript.refused`). A conscription of
    grain is refused, never performed against the pool;
  - **TS-7's question source makes the referent a `stores:recruits` claim** about a settlement, so
    `store_kind_of` (`options.py:630-651`) [CHECKED] yields `recruits` through the chain as it
    stands. Claims of the form `stores:<kind>` are what WITNESS deposits for a stores observation
    (`loop/witness.py:161`, `:564`) [CHECKED]; that a regrowth `stores.changed` deposits one naming
    `recruits` is **[INFERRED]**, and TS-7's exit shows it or fails.
- **`amount`** comes from the same chain: a held shortfall claim, else `default_transfer_amount`,
  shipped 1 (`fixtures.py:495`) [CHECKED]. **The first correction's `conscript_amount` fixture is
  withdrawn:** the chain never reads a per-verb fixture, so it would have been dead, and under P the
  shipped `1` would have been refused as below a cohort. Under A a levy of 1 is a valid stock.

**The effect, `_eff_conscript`** (in `loop/effects_governance.py`, beside `_eff_requisition`):
1. Resolve the seat (`_exercised_office`) [CHECKED-draft], the settlement `rung`, `kind` and `n`.
2. **Decline** (→ `write` → `conscript.refused`) when any of these holds:
   - there is no seat;
   - `kind != "recruits"` (above);
   - `rung.stores["recruits"] < n` — **the pool is short.** The cell tests the same thing when `kind`
     is `recruits`; the effect re-tests it because it is the write's own guard, and two acts in one
     fold may draw the same pool (second critic, finding 1: the first correction omitted it, so a
     pool could go negative);
   - `n <= 0`.
3. **Move,** in one `Change` on the one rung: `recruits -= n`, `troops_raw += n`, through
   `w.write("stores", …)`, emitting `stores.changed` and `conscript.taken`.

**Writes, and their classes:** `(Rung, stores)` at RES, `[MAT, RES]` already [CHECKED-1]. No Person, no
Tenure, no gate basis, no `founding` clause. The casualty write at ENC is `march`'s, not this verb's
(`_part2` §4.6).

**Per-clause refusals** (`04 §B.13` invariant 4) [CHECKED-draft]:
- **`conscript.unauthorized`** means the SEAT failed: no seat granting `dispatch`, or its purview does
  not reach the settlement.
- **`conscript.refused`** means the PLACE failed: the pool is short, or the act asked for something
  that is not the pool.

### 3.2 The companion acts: each needed, and none of them new

| need | act | reused as it stands? | what the troop stock adds to it |
|---|---|---|---|
| fill a treasury with goods, including arms | **`requisition`** (`verb_table.yaml:629-663`) | **yes**, plus the `movable` refusal for `recruits` | nothing else. It may also move a troop stock into the seat's rung, which is assembly by another name and is allowed |
| equip a levy | **`transfer`** of an arms kind into the settlement where the levy stands | **yes**, plus the `movable` refusal. `_eff_transfer` moves between any two rungs, conserved [CHECKED-draft] | new `matter_kinds` rows for kit (§6). **Reachable in computed play:** the computed `to` is the referent (`verb_table.yaml:1211`) [CHECKED-1], and a settlement is a referent [INFERRED] |
| bring levies from several settlements to one muster | **`transfer`** of a troop kind to the origin settlement | **yes** | nothing. Whether a computed `from` can be a settlement holding troops depends on `treasury_of(seat)` (`options.py:869-870`) [CHECKED], which is the seat's rung; **[UNVERIFIED]** for which seats that is a settlement |
| drill a levy | **`train`** (IN-12 step 9, unbuilt) | **no.** J-13 (iii) writes capability only where a case names a vocation (`_part5.md:73`) [CHECKED-1] | nothing until J-5 or J-13 changes |
| field the army | **`march`** (`:664-690`) | **row: one act-declared payload key, `order`. Effect: the write-back (`_part2` §4.6)** | the side's composition is read, not chosen at the fold |
| end a levy | none needed | — | casualties, hunger, or a transfer away (§2.9) |

### 3.3 What is NOT added, and why

| not added | because |
|---|---|
| a company `Person`, a gate basis, a `founding` clause, `service_faction`, `is_company`, a dissolution rule | P's apparatus; A needs none of it (§2.4) |
| a `muster` verb | the muster is a Query, `mustered`, plus the stocks at the place (`_part2` §4.1) |
| an `equip` verb | `transfer` moves kit |
| a `disband` / stand-down verb | not needed for boundedness (§2.9); Jordan's to ask for |
| a `recruit` verb (troops for coin) | it mints men from matter; R-POOL names the pool as the source |
| a seventh remit act | `dispatch` covers raising and sending men |
| a per-verb `kind` or `amount` default | forbidden by `options.py:763-767`; the effect declines and the question source supplies the referent |
| a season troop-kind table | `TROOP_LOADOUT` is the one owner |

### 3.4 The corrected role of `requisition`

`requisition` is the store act. It moves goods (and, being a conserved move, a troop stock) from a rung
in the seat's purview into the seat's treasury (`effects_governance.py:373-412`) [CHECKED-draft]. It
may not move `recruits`. The kit chain is `requisition` (arms → treasury) → `transfer` (arms → the
levy's settlement) → `kind_for_kit` → the field. Its name is provisional (J-3).

### 3.5 The meta-rule: every object added, every object cut, counted honestly

Counted per the second critic's finding 13: event kinds, registry rows, edits to existing rows,
constants, result keys and hole rows each count.

**Added under A (the default):**

| # | object | kind |
|---|---|---|
| 1 | the `conscript` row | verb row |
| 2–4 | `conscript.taken`, `conscript.unauthorized`, `conscript.refused` | event kinds (an unregistered kind fails at `log.append`, `04:776`) [CHECKED] |
| 5 | `_eff_conscript` | effect |
| 6 | `recruits` | `matter_kinds` row |
| 7 | `troop_grades` | roster |
| 8 | one `troops_<id>` `matter_kinds` row per grade (4 at the proposed ladder), derived by the loader | registry rows + a loader derivation |
| 9 | kit `matter_kinds` rows, one per weapon and armour class (count **[OPEN]**) | registry rows |
| 10 | `immovable_kinds` | roster |
| 11 | `movable(w, kind)`, read in `_eff_requisition` and `_eff_transfer`, asserted in `_shift` | predicate + 3 call-site edits |
| 12 | `pool_rung_kinds` | roster |
| 13 | `recruit_ceiling` | Query |
| 14 | the regrowth pass at MATTER | clock write |
| 15 | world-gen fill of every pool | harness step |
| 16 | `SUBSIST` reads only weighted kinds | harness edit |
| 17 | `subsistence_draw` feeds troop stocks after persons; `demanded`/`delivered` docstrings | Query edit |
| 18 | MATTER's dearth step debits a short stock | clock write |
| 19 | `(Rung, stores)` gains ENC | matrix edit |
| 20 | `_eff_march` writes casualties on stocks and the pool, and no longer returns early with no person loser | effect edit |
| 21 | the defending pool and the widened `Unopposed` test in the wrapper | wrapper edit |
| 22 | `order_of_battle` | host function |
| 23 | `MassBattleInput.weights` → `sides` | record edit (an exchange) |
| 24 | `kind_for_kit` | module function |
| 25 | the unarmed-kind constant | module constant |
| 26 | `trim_to_command`, and `unfielded` in the result | module function + result key |
| 27–29 | `recruit_share`, `recruit_regrowth`, `men_per_weight` | fixtures |
| 30–32 | one hole-register row per fixture | register rows |
| 33 | the `order` payload key on `march` | act-declared key |
| 34 | the temporary fixture `field_army` (deleted at TS-9) | scaffolding |
| 35 | the `04:793` amendment | Layer 1 line (J-1) |

**Cut, on disk:** `_weighted_unit` and four constants (`_MVP_SUBUNIT_SHAPE`, `_MVP_UNIT_COMMAND`,
`_SEASON_FORCE_POWER`, `_MIN_TROOPS`) (`massbattle.py:170-230`): **5 objects.** Not counted as cuts: the
`[GAP …]` comment line, the `weights` → `sides` exchange (#23), and the `build_army` move.

**Net:** 35 added (plus the open count of kit kinds) against 5 cut. Under P the same count was about
38: P drops #8's derivation, #17–#18 and #21, and adds the company `Person` mint, a gate basis, a
`founding` clause, `service_faction`, the `mustered` clause, the `_side_stance` edit, `is_company`, the
dissolution rule with its `release` row and effect edits, the `company.dissolved` event kind,
`(Person, weight)` gaining ENC, `conscript_amount` with its hole row, and the salvage clause. The first
correction's "22 added against 6 cut" undercounted (finding 13). `_part2` §8.4 scores E against these
counts.
