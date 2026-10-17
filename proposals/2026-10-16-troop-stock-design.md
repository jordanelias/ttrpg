# The troop stock: a settlement's recruit pool, the levies raised from it, and the season's order of battle

## Status: PROPOSED (2026-10-16). Corrected three times on the same day against three independent critics' reports, and re-based on Jordan's ruling of that day (below). The second correction **changed the default troop body** from a company `Person` (P) to a troop stock (A). The third **restated A's Layer 1 footprint in full** (§2.4), **moved defence onto the garrison Site** (`_part2` §4.1), **named the troop verb `levy`** (§3.1), and **gave the computed levy a producer** (§2.3). All three reconciliation tables are at the end of `_part2`. Not ratified; merge ratifies nothing unless Jordan so rules.
## Lane: MB (the field and the army builder), SE (the recruit pool, the levy stock and its feeding), FA (assembly), IN (the verb row, the registries, the harness subsistence formula, the `levy` follow-through). IDs: none allocated.
## Read at the working tree of 2026-10-16, after the `levy` → `requisition` rename of the store act.
## Parts: this file (head, §0–§3) · [`_part2`](2026-10-16-troop-stock-design_part2.md) (§4–§10 and the three critic reconciliations), read in that order.

**Reference, not mechanism (CLAUDE.md §0.05).** Nothing here changes how the game behaves. Every
behaviour below becomes true only when the code in `_part2` §7 is built and a run shows it. Where this
document and code disagree, the code is right and this document is wrong. Locators are `file:line` in
the tree as read.
- **`[CHECKED]`** means the line was re-opened in the **third** correction pass.
- **`[CHECKED-2]`** means the second correction pass, and not the third.
- **`[CHECKED-1]`** means the first correction pass only.
- **`[CHECKED-draft]`** means it was opened at drafting only.
- **`[RAN]`** means I executed something in the third pass and quote what it printed (commands and
  saved outputs in `_part2` §10). An earlier pass's run is marked `[RAN, second correction]`, etc.
- **`[INFERRED]`** means I reasoned from lines I opened but ran nothing.
- **`[UNVERIFIED]`** means I did not open it.

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

Demand (4) is met by the rename already in the tree: the store act is `requisition`. **The troop verb
is `levy`** (§3.1), Jordan's own word for raising men. Reusing it means re-keying the registers that
still use it for the store act, and that work is a build position, TS-L (`_part2` §7).

---

## 0. VERDICT

1. **Each settlement holds a recruit pool: a store of men it can still raise.**
   - **Where it lives:** a new matter kind, `recruits`, in the settlement rung's `Rung.stores`, through
     the `(Rung, stores)` write-matrix row, which admits MATTER and RESOLVE today
     (`write_matrix.yaml:318-324`) [CHECKED].
   - **Which rungs hold one:** only rungs whose kind is in a new roster, `pool_rung_kinds:
     [settlement]`, on `march_target_kinds`' precedent (`loop/sides.py:114-116`) [CHECKED].
   - **What it derives from:** `recruit_ceiling(w, rung)`, the weight of the cohort persons resident in
     the settlement times a share fixture (§2.2).
   - **How it replenishes:** at MATTER, in its own pass after yield, toward the ceiling and never past
     it. **It starts empty at world-gen and fills by regrowth**, because each regrowth write is what
     tells the settlement's governors the pool exists (§2.3).
   - **What raising does:** `levy` moves men from `recruits` into a troop stock on the same rung. It
     **never writes the population cohort** (R-POOL).
2. **A raised troop is a count, not a person (candidate A, the default).**
   - **What it is:** a troop stock in the same settlement rung's `stores`, one matter kind per
     experience grade (`troops_raw`, …; §2.7). It eats from the larder where it stands, after every
     person there (§2.5). It fights for whoever holds the rung, under that faction's members present
     (`_part2` §4.1). `transfer` moves it, but only between settlement rungs (§2.1).
   - **Why it is the default:** it is the **only** candidate that breaks the content of no Jordan
     ruling (ED-WR-0011, RR-2, J-16, R-POOL, ED-IN-0279's casualty rule, the garrison ruling).
   - **⚠ What A costs, in full (§2.4's table):**
     - **Two Layer 1 sentences are amended.** Each is stated in three ratified documents:
       - "units = persons at weight, no unit class" (`04:793`, `03:261`, `10:89`);
       - "one scale down, the same thing, every combatant a `Person`" (`04:802`, `03:269-270`,
         `10:97-98`).
     - **Three ratified clauses are strained, not contradicted:**
       - the Rung is "the address, never the occupant" (`04:252`, `01:896`);
       - its NEVER list bans "discipline-as-a-stored-value" (`01:910-911`, `04:257`);
       - T-l's stated reason, "two code paths drift" (`01:497-499`).
     - **One ruled verb row's `writes` declaration widens:** `march` (`verb_table.yaml:677-681`).
       ED-IN-0279's content, casualties only on the losing side, is kept.
     - **One code rule is amended:** `24f`'s "only a cohort eats".
     - **That overwrites ratified canon, so it is J-1, escalated (`_part2` §9).**
   - **What a troop loses against a person:** it cannot desert, witness, or carry a grudge.
3. **What the ruling settles, and what it does not:**
   - **Settles J-2.** Raising takes nothing from the cohort. The cohort's `weight` is never written by
     this design, and under scarcity its larder row is protected by draw order (§2.5).
   - **Gives the raise a cost:** the pool and the seasons it takes to regrow, and food, because a stock
     eats at the larder where it stands (§2.5).
   - **Does not settle the troop body.** J-1 carries it (§2.4).
4. **Who stands is unchanged; what they field is new; defence composes on the garrison.**
   - **A side is the members `mustered` already returns.** Jordan ruled that "present at the target"
     means members in the settlement's subtree (`queries/world_q.py:1256-1259`) [CHECKED].
   - **Its men are the troop stocks at the place held by the side's faction:** at the origin for the
     attacker, at the target for the defender.
   - **The defender also fields the settlement's garrison.** Its strength is the garrison Site's
     `condition`, which Jordan ruled is what garrison strength is, "over a cohort-Person alternative"
     (`world_q.py:1275-1278`; `harness/populated.py:799-804`) [CHECKED]. The pool does not defend.
     The third critic's finding 4 showed that the pool defending was close to the alternative Jordan
     rejected.
   - **A defending side with no member present stays `Unopposed`**, as it is today.
   - **An attacking side that fields no men is refused** by a new branch (`_part2` §4.1). The wrapper
     re-derives the origin from the claimants' homes, on `_origin_of`'s precedent
     (`seam/wrappers/mass_battle.py:151-172`) [CHECKED]. No seam parameter is added, so `04:765`
     stands.
5. **Quality has three axes. Computed play reaches one of them.**
   - **Equipment** is matter in the same settlement's `stores`. The module's `kind_for_kit` derives
     each subunit's troop kind from it. `kind_for_kit` reads `TROOP_LOADOUT`
     (`modules/mass_battle/equipment/__init__.py:17-36`) [CHECKED]: an INERT named association, "NOT
     a derivation", and wiring it ends that status (§2.7). **Equipment is not reachable in computed
     play.** Arms have no producer, and no producer deposits a `stores:<arms>` claim either, so a
     computed `transfer`'s `kind` falls back to `grain` (`decision/options.py:874-875`) [CHECKED]. Only
     player and hand-built acts reach it.
   - **Experience** is the grade, carried as which troop kind a man is counted under. ⚠ No computed
     act moves men up a grade until J-5 (c) or a J-13 change (§2.7).
   - **The commander** is reached in computed play: who commands is live. His Command is 4 for every
     season commander until R-C-1 names a source (`_part2` §4.2 step 6).
6. **The verbs:**
   - **One new verb, `levy`,** over a settlement rung (§3.1).
   - **Reused companion acts:** `requisition` fills a treasury with arms; `transfer` moves arms and
     troops between settlements; `march` fields them.
   - **`recruits` is immovable** by every store act. Troop kinds move only between settlement rungs
     (§2.1).
7. **The army builder moves across the seam** (`_part2` §4.4). `build_army` moves out of
   `systems/mass_battle/sim/engine.py:213-452` into `modules/mass_battle/` [CHECKED-draft]. The
   season's one-Line construction (`modules/mass_battle/massbattle.py:170-230`) [CHECKED for `:200-230`]
   is deleted. The host builds each side's order of battle, one subunit per troop kind and kit at the
   place. The record that crosses the seam is a per-side composition, and the module docstring's "no
   `Unit`/`Faction`-shaped object crosses this boundary" (`massbattle.py:321-323`) [CHECKED] is edited
   to say so (§2.4).
8. **A defect tracked on its own, gated on nothing here (TS-2, `_part2` §7):** `build_army` throws
   away the morale preset of every troop type it builds. The default at
   `systems/mass_battle/sim/engine.py:427-428` pre-empts `Subunit.of_type`'s `setdefault` at
   `modules/mass_battle/hierarchy/units.py:726` [CHECKED-1]. A drafting probe printed `levy power 1
   disc 1 morale 6` where the preset row says morale 2 (`troop_types/registry.py:41`) [CHECKED].
9. **Two defects in the harness this design must fix first:**
   - **Men would be sensed as food.** The harness subsistence formula `SUBSIST` sums **every** store
     kind at the person's containing rung (`engine/season/harness/probes.py:144-149`) [CHECKED-2].
     **It bites under dearth, and at no state a deliberation reads otherwise.** At the first
     DELIBERATE, MATTER has already credited yield (`loop/driver.py:432-433`) [CHECKED]. Every cohort
     senses 1000 with or without `recruits` [RAN]. With one rung's larder at `grain: 1` the cohort
     senses 500, and 1000 once `recruits: 2` is added [RAN]. The fix reads only the kinds that carry a
     subsistence weight (§2.5).
   - **Draw order.** `subsistence_draw` walks persons in sorted id order (`world_q.py:858`) [CHECKED].
     Troop stocks draw after every person (§2.5).
10. **What this cuts:**
    - **IN-52's feed and LF-1..LF-3 are withdrawn as forms.** A stock eats at the larder where it
      stands, through `subsistence_draw`, not from a treasury ration (`_part2` §5).
    - **IN-49 is re-framed** as the store act's question source.
    - **Closed:** MB-08's #445 U-1. **Not closed:** H-49 (`Person.weight` gains no writer under A).
11. **Grade: paper.** Nothing in §2–§4 is built. Third-pass runs: `SUBSIST` at the first
    DELIBERATE's state, per-settlement food yield over four real seasons, and an arithmetic
    projection of a levy's growth against food (`_part2` §10). `_part2` §7 gives the build order;
    each step's exit is an execution artifact.

---

## 1. THE PROBLEM AS CODED

Each fact below is at its source. Together they answer the four demands and the ruled constraints.

### 1.1 Who fights a season field

1. **A field's two sides are faction members present at a place.**
   - **Attacker:** `sides_of` musters `mustered(w, origin, faction)`. `origin` is the actor's nearest
     settlement up his `contain` ancestry. `faction` is the faction of the seat the act was exercised
     through, converted by `faction_prop_id` (`engine/season/loop/sides.py:79-85`) [CHECKED].
     **`origin` is computed there and dropped:** `sides_of` returns `(claimants, subject, target)`
     (`:127`) [CHECKED], and the provider is never handed it. "`contest()` hands this provider the
     target rung and never the origin, and no seam parameter is added for it"
     (`seam/wrappers/mass_battle.py:154-155`) [CHECKED].
   - **Defender:** the provider musters `mustered(w, rung, subject)` at the target
     (`mass_battle.py:233`) [CHECKED]. `subject` is the target's holder's faction,
     `holder_faction_of(w, target)` (`sides.py:115-116`; `loop/effects_combat.py:240`) [CHECKED].
   - **An empty defending side is `Unopposed`**, and the module is never called
     (`mass_battle.py:235-248`) [CHECKED]. So `fort_level` and `walls_dr`, which the module reads
     (`modules/mass_battle/massbattle.py:273`, `:342-371`) [CHECKED-2], never engage for it.
   - **An attacking side with no person is PARTY-GAP:** `if not claimants:` (`mass_battle.py:224-226`)
     [CHECKED]. It tests persons, not men.
   - **What `mustered` reads:** "This faction's members present in `rung_id`'s subtree --
     settlement plus everything under it, Jordan's ruling on what 'present at the target' means"
     (`queries/world_q.py:1256-1272`) [CHECKED]. Membership is a live `commit`.
2. **The population never fights.** It is one cohort `Person` per settlement, with no `commit`,
   minted with `contain` and `reside` on the settlement (`harness/populated.py:439-442`) [CHECKED-1].
   Its weight is 2 at all 37 settlements (H-170, `hole_register.yaml:3728-3734`) [CHECKED].
3. **A side is its members' summed `Person.weight`** (`seam/wrappers/mass_battle.py:190-193`)
   [CHECKED]. The input record carries nothing about composition, kit or command
   (`queries/inputs.py:62-100`) [CHECKED-draft].
4. **The march's write-back touches persons only.** `_eff_march` takes the losers' person ids, and
   returns `NO_CHANGE` when none is a person (`loop/effects_combat.py:226-230`) [CHECKED]. Casualties
   land on `body`, through a float, and every loser gets a morale row and a grudge row (`:248-261`)
   [CHECKED]. **The row's `writes` are keyed by outcome and declare only `Person.body` and
   `Person.stance`** (`verb_table.yaml:677-681`, `grade: "ruled"` at `:689`) [CHECKED]. The fold
   gates exactly those pairs (`_pairs = row.writes_at(_degree)`, `loop/resolve.py:442`) [CHECKED].

### 1.2 What the module builds from that

5. **Every side is one Line subunit of bare `infantry`, at power 4, command 4 and discipline 5**
   (`massbattle.py:170-196`), under the module's own label "minimum-viable defaults … no canonical
   spec exists" (`:160-166`) and its `[GAP …]` header (`:32`) [CHECKED-draft]. Demand (2) rules this
   a stub.
6. **Troops are the raw weight sum**, `troops=max(float(weight), _MIN_TROOPS)` (`massbattle.py:226`)
   [CHECKED]. `_MIN_TROOPS` exists because "`Unit.total_troops() == 0` divides by zero" (`:208-210`)
   [CHECKED]. The rout floor is `SUBUNIT_ROUT_FLOOR = 80` (`config.py:117`) [CHECKED-draft]. The MB
   lane's probe: 0 attacker wins in 20 at ≤80 troops, and "one present defender holds any settlement
   against any army the realm can raise" (`research/by_lane/MB_mass_battle.md:434`, M-MB-1)
   [CHECKED-2 as a citation; not re-run].
7. **Morale is the only side quality that reaches the field.** `_side_stance` weights by
   `Person.weight`, "because `resolve_field` sizes the side by the same weights"
   (`seam/wrappers/mass_battle.py:126-148`, the reason at `:136-137`) [CHECKED]. It finds each
   person's faction through `faction_holding`, which reads live `commit` edges only
   (`world_q.py:1436-1438`) [CHECKED-1].
8. **Two terrain clauses are skipped because a season side is one subunit.** WALLS' "no flanking; Slow
   cannot advance" and NARROW_PASS's "1 engagement per side" are not applied, because "a season unit
   is ONE subunit with no tactic" (`massbattle.py:251-259`) [CHECKED]. Subunit armies make both live.

### 1.3 What the harness can build, and the season cannot reach

9. **A composite army constructor exists on the wrong side of the seam:** `build_army(specs, …,
   officers=())` (`systems/mass_battle/sim/engine.py:213-452`), with roles gated by `role_allowed`
   and spans checked against Command and `SUBUNIT_CAP = 11` (`:99`, `:304-345`, `:369-371`)
   [CHECKED-draft]. `modules/mass_battle/` imports nothing from `systems/` (`MB_mass_battle.md:368`)
   [CHECKED-draft as a citation].
10. **Troop-type presets exist, including a `levy` row** (power 1, discipline 1, morale 2;
    `troop_types/registry.py:39-57`, `:41`) [CHECKED for `:41`], applied by `Subunit.of_type`
    (`hierarchy/units.py:712-730`) [CHECKED-draft].
11. **The morale preset is dead on the harness path** (§0 item 8).
12. **Equipment is a catalogue, and an inert one.** `ARSENAL`, `ARMOURY` and `TROOP_LOADOUT`
    (`equipment/__init__.py:13-36`) [CHECKED]. The module says it is "NOT YET WIRED into resolution"
    (`:10-12`), and that `TROOP_LOADOUT` is "INERT (nothing consumes it yet) and intentionally a thin
    NAMED association, NOT a derivation" (`:17-20`) [CHECKED]. `levy` is `light_cut`/`none` (`:22`);
    `archers` and `mounted_archers` share `bow`/`light`; no row names a mount.
13. **Officers derive Command from charisma and cognition only when both are given and
    `COMMAND_SIGMA_ENABLED` is on** (`hierarchy/units.py:2711-2716`; `config.py:530`) [CHECKED-1].
    `Unit.officers` is bookkeeping (`:2793-2797`) [CHECKED-draft]; `build_army`'s span check reads
    `Officer.command`.
14. **Experience has no carrier** (`MB_mass_battle.md:449`, M-MB-16) [CHECKED-draft as a citation].

### 1.4 The verbs, the stock, the claims, and the subsistence model

15. **`requisition` moves goods, conserved, into the seat's treasury.** Eligibility `["remit:issue",
    "presence:<rung>"]`; typed cell `basis` (purview, conjunct `authority`) and `scalar_threshold`
    (`stores`, `key: kind`, `threshold: amount`, conjunct `stores`) (`verb_table.yaml:629-652`)
    [CHECKED-2]. Its effect shifts through `_shift`, "the one body of every act that moves stores
    between two rungs" (`loop/effects_shared.py:117-128`) [CHECKED-1].
16. **The treasury is the seat's rung, of any kind.** `treasury_of` returns the `seat_rung` of the
    holder's live `hold` (`decision/options.py:600-615`) [CHECKED], which can be a territory or the
    realm.
17. **A typed cell's `key:` is an operand, not a literal.** `ScalarThreshold.check` binds `key` from
    the act's operands and observes `f"{scalar}:{k}"` (`engine/season/data/requires.py:295-307`)
    [CHECKED-2].
18. **A computed act's `kind` and `amount` come from one generic chain** (`options.py:846-877`)
    [CHECKED]: a writ claim, then a shortfall claim, then `store_kind_of(p, q)` (the question's own
    `stores:<kind>` claim, `:630-651`) [CHECKED], then the fixtures `default_store_kind = "grain"` and
    `default_transfer_amount = 1` (`:874-877`) [CHECKED]. A per-verb branch in that chain is what its
    docstring forbids (`options.py:763-767`) [CHECKED-2].
19. **A `stores:<kind>` claim has two producers, and neither is a regrowth.**
    - **A cell's read:** WITNESS deposits one claim per `Observation` on an Event. RESOLVE puts a
      refused act's reads there (`observed=_verdict.observed`, `loop/resolve.py:987-990`) [CHECKED].
    - **MATTER's larder debit:** the draw's write carries `observed=short_seen` (`loop/matter.py:495-503`)
      [CHECKED]. Its predicate is `shortfall:<kind>` (`:398-403`) [CHECKED], not `stores:<kind>`.
    - **Yield's credit carries no `observed=`** (`matter.py:530-536`) [CHECKED]. Its Event deposits only
      an event-kind claim, "`predicate = e.kind, value = True`" (`loop/witness.py:561-562`) [CHECKED].
    - **Governors learn only from reads:** "no `stores.changed` of any larder anywhere becomes a
      seat-holder's news; only a read that MATTER actually recorded does" (`witness.py:428-431`)
      [CHECKED].
    - **The actorless route is generic:** any actorless Event's `observed` reaches the seats whose
      purview contains the observed subject (`witness.py:446-456`) [CHECKED].
20. **`march` writes only the losers** (ED-IN-0279, `verb_table.yaml:682`) [CHECKED].
21. **The stock and its clock.** `matter_kinds` is an open registry (`rosters.yaml:1279-1290`)
    [CHECKED-1]. MATTER's per-rung loop iterates **every** rung (`loop/matter.py:485`), credits yield
    from Sites, and `continue`s on a rung that produced nothing (`:521-523`) [CHECKED]. Yield has no
    ceiling.
22. **Only `grain` and `salt` are eaten.** `subsistence_weight` carries those two rows: "timber, ore
    and coin are stored and not eaten" (`rosters.yaml:1371-1387`) [CHECKED]. `subsistence_draw` loops
    over that registry, so an unweighted kind is never drawn (`world_q.py:863-866`) [CHECKED].
23. **The sensed subsistence does not agree.** `SUBSIST` sums every kind in the containing rung's
    `stores` (`harness/probes.py:144-149`) [CHECKED-2]. `sense` feeds it to every person's
    deliberation (`loop/deliberate.py:119`, `:536`) [CHECKED-2]. Coin, timber and ore are already
    sensed as food today.
24. **The draw is one record, keyed by person.** `subsistence_draw` returns `{person id: (home rung,
    {kind: (want, take, source)})}` (`world_q.py:803-805`) [CHECKED]. MATTER builds `draws` and
    `short_by_person` from it (`matter.py:344-353`), stores the second as `w._subsistence_shortfall`
    (`:420`), and falls each short person's `body` (`:442-463`) [CHECKED]. `demanded` and `delivered`
    read each row's home from the value, not the key (`_drawn_under`, `world_q.py:952-964`)
    [CHECKED].
    - **Consumers of `_subsistence_shortfall`:** the harness census report
      (`harness/populated.py:1498`) [CHECKED]; tests pin it to the cohorts exactly
      (`engine/season/tests/test_governance_build.py:521`; `test_territorial_subsistence.py:295`)
      [CHECKED].

### 1.5 The rulings this design must meet

25. **ED-WR-0011, RULED (Option A):** *"A CLOSED AUTHORED CAST … Everyone who will ever matter exists
    at tick 0 and the cast only shrinks"*; *"B requires a producer for Person that A forbids"*
    (`registers/editorial_ledger_wr_archive.jsonl:13-14`) [CHECKED-2]. Jordan's words: *"World-gen
    NPC count, for now, is just the 46 NPCs we built. We will return much later."* The code applies it
    to cohorts: "`ED-WR-0011` option A -- nothing mints one at run time" (`world_q.py:824`) [CHECKED].
    - **The contrary reading:** X-4, "ED-WR-0011 closes the NAMED cast 'for now'; it does not reach a
      cohort's `weight`" (`research/by_lane/00_COMPARATIVE_ANALYSIS.md:204`) [CHECKED-2].
    - **A run-time producer already exists for individuals:** CENSUS individuates a demanded person at
      weight 1 (`loop/census.py:105-112`) [CHECKED-2], licensed by Layer 1's `loop/census` row
      (`04:179`) [CHECKED-2].
26. **RR-2 / ED-SE-0051:** "capacity bounds POPULATION" (`world_q.py:1050-1051`) [CHECKED-2];
    `seat_cohorts` refuses a cohort above capacity (`harness/populated.py:401-432`) [CHECKED-2].
    `population` reads `reside`; `subsistence_draw` reads `contain` through `home_of`
    (`world_q.py:856`) [CHECKED].
27. **J-16 on H-173, delegated-ruled [ASSUMPTION; medium; Jordan to correct]:** "a sentence differs
    from a service `oblige` by term and the basis that opened it, never by a branch on origin"
    (`hole_register.yaml:3772`) [CHECKED-2]. `Term.declared_by` is overwritten by renewal
    (`state/carriers.py:50-51`; `loop/effects_economy.py:309`) [CHECKED-2].
28. **Jordan's garrison ruling:** a settlement's defensive strength is "read off the `garrison`
    Site(s) in `rung_id`'s subtree … Jordan's choice over a cohort-Person alternative (planning round
    2)" (`world_q.py:1275-1278`) [CHECKED]. "Jordan ruled WHAT garrison strength is … a Site's own
    `condition` field" (`harness/populated.py:799-804`) [CHECKED]. Today it is read as `fort_level`,
    and any positive value makes the field WALLS (`world_q.py:1286-1289`) [CHECKED].
29. **Layer 1, RATIFIED (ED-IN-0204; the status line is line 3 of `03_VERBS_AND_LOOPS.md` and of
    `10_FACTIONS_AND_DEPLOYMENT.md`)** [CHECKED]. Every line §2.4's table weighs is quoted there.

### 1.6 The four demands and the ruling against this, in one table

| demand | carried today? | where it fails |
|---|---|---|
| (1a) troops a settlement holds as its own resource | **no** | no store kind is a man (items 2, 21) |
| (1b) a levy that produces them | **no** | the only act that bore the name moved goods (item 15) |
| (1c) quality by equipment, experience, commander | **no** on the season path | constants (item 5); presets and officers are harness-only (items 9–13); experience has no carrier (item 14) |
| (1d) units as the field's input | **no** | the input is a weight tuple (item 3) |
| (2) the 4/4 Line is a stub | **confirmed** | item 5 |
| (3) composite armies with subformations | **built in the harness, unreachable** | items 9, 10; two terrain clauses assume one subunit (item 8) |
| (4) `levy` wrongly names a store act | **fixed in the tree** | item 15 |
| R-POOL: a pool of its own that replenishes, the cohort untouched | **no** | no carrier of raisable men; the one replenishing clock has no ceiling (item 21) |

---

## 2. THE RECRUIT POOL AND THE TROOP BODY

### 2.1 Where the pool lives: four homes, one chosen

| home | what it adds | Layer 1 | what it gets wrong |
|---|---|---|---|
| **S. a `recruits` kind in the settlement rung's `stores` — CHOSEN** | one `matter_kinds` row; a ceiling Query; a capped credit at MATTER; one placement predicate | none for the pool: `(Rung, stores)` already admits `[MAT, RES]` [CHECKED]. The troop stock it feeds is J-1's | a store is movable by `_shift`'s callers, and `SUBSIST` senses it as food (§1.4 item 23). Both are closed below |
| **E. `Rung.envelope`** | a producer for a ratified, unwritten field (H-171); RES added to `(Rung, envelope)` | strains `04:179`, which gives `envelope` to CENSUS alone [CHECKED-2] | its ratified meaning is "the population not individuated as persons" (`world_q.py:1065`) [CHECKED-1], the population itself, not its raisable men; its declared shape is a list of age bands no position built |
| **G. a `muster` Site kind whose `condition` is the pool** | a site kind, its `wear_per_season` and `band_floors` rows (`rosters.yaml:1258-1263`) [CHECKED-1], one Site per settlement | none | a Site is fabric: `restore` and wear would act on a roll of men, and the pool would be a fraction, not a count |
| **F. a new field on `Rung`** | a carrier field, a matrix row, an event kind | **amends** `04:255`'s `Rung := ( …, envelope, exists )` [CHECKED] | costs a Layer 1 amendment for a value `stores` can carry |

**Why S:** it composes on the stock that exists (a debit at RESOLVE, as `requisition`'s; a credit at
MATTER, through yield's write path); it counts men in whole units the grammar can test; the pool itself
amends nothing ratified.

**The case against E** rests on `04:179` (CENSUS is its one writer), its meaning (the population, not
the share of it that can stand in the ranks), and its unbuilt age-band shape.

**Two closures S needs:**
- **Where a man may be put.** One roster and one predicate:
  - **`rosters.yaml: immovable_kinds: [recruits]`.**
  - **`placeable(w, kind, rung)`**, read by `_eff_requisition` and `_eff_transfer` before they write
    (each declines to its own `write` refusal), and asserted by `_shift` as the last line of defence.
    It is false for an immovable kind anywhere. It is false for a troop kind on a rung whose kind is
    not in `pool_rung_kinds`.
  - **Why the second clause** (third critic, finding 11): `requisition`'s destination is the seat's
    treasury, which can be a territory or the realm (§1.4 item 16). A troop stock there would eat
    (§2.5) and never be fielded, because a march's origin and target are settlements. So a
    `requisition` of troops is allowed only when the treasury is a settlement, and a `transfer` of
    troops only to a settlement. Moving a raised levy between settlements is assembly (§3.2).
- **A man is not food.** `SUBSIST` is fixed to sum only the kinds `subsistence_weight` names (§2.5).

### 2.2 What the pool derives from: the ceiling

`recruit_ceiling(w, rung)` is a Query in `queries/world_q.py`, beside `population` and `capacity`:

```
recruit_ceiling(w, rung) = 0                                         if rung's kind ∉ pool_rung_kinds
                         = ( Σ weight of cohort persons resident under rung × recruit_share + 500 ) // 1000
```

- **The base is the settlement's own people:** cohort persons (`Person.is_cohort`) whose `residence_of`
  is in the rung's subtree, read as `population` reads it (`world_q.py:1048-1078`) [CHECKED-2].
  - **Why only cohorts:** a named person at weight 1 commands; he is not men in the ranks (§2.6).
  - **No service filter is needed under A.** A troop stock is not a person and never enters the base.
- **Which rungs hold a pool:** only rungs whose kind is in `rosters.yaml: pool_rung_kinds`, shipped
  `[settlement]`, on `march_target_kinds`' precedent, a closed roster read where the rung is in scope
  (`loop/sides.py:114-116`) [CHECKED]. Without the filter, a territory's ceiling would sum its
  settlements' cohorts again.
- **`recruit_share`** is per-mille. **[OPEN — Jordan tuning]**, with a hole-register row and a sweep
  (`_part2` §6). Integer, half-up, on `condition_scale`'s per-mille convention (`data/fixtures.py:182`)
  [CHECKED-1].
- **At the shipped data every ceiling is equal:** all 37 cohorts weigh 2 (H-170), so every ceiling is
  `2 × recruit_share / 1000`. H-170's own sweep would spread them [CHECKED].
- **Not added:** `capacity` (housing, not people), the garrison's condition, the larder's fill.

### 2.3 How the pool replenishes, and how a seat learns of it

At MATTER, **in its own pass after the yield loop**, over rungs whose kind is in `pool_rung_kinds`,
sorted by id, through the same `w.write("stores", …)` yield uses:

```
growth   = ( recruit_ceiling(w, rung) × recruit_regrowth + 500 ) // 1000
recruits ← min( recruit_ceiling(w, rung), recruits + growth )
```

- **Why its own pass, not inside yield's loop:** yield's loop visits every rung and `continue`s on any
  rung with no yield (`matter.py:485`, `:521-523`) [CHECKED]. Placed after that line, regrowth would
  silently skip every settlement with no producing Site. A separate pass with the kind filter does not.
- **The precedent is yield's write**: a credit to `stores` at MATTER (`matter.py:530-536`) [CHECKED].
  The difference is the ceiling: the pool stops there, so a quiet settlement never banks an army.
- **No write when nothing changes.** A full pool writes and emits nothing.
- **⚠ The write carries what it read** (third critic, finding 3). Regrowth reads the pool to compute
  it, so its write carries `observed=(Observation(rung, "stores:recruits", new value),)`. That is the
  field for "what was read to reach this Event", as MATTER's larder debit uses it
  (`matter.py:495-503`) [CHECKED].
  - **Who learns:** WITNESS routes an actorless Event's observations to every seat whose purview
    contains the subject (`witness.py:446-456`) [CHECKED]. So the settlement's governors receive a
    `stores:recruits` claim about it. It is a read, so it does not breach "no `stores.changed` …
    becomes a seat-holder's news" (`:430-431`).
  - **What it is for:** it is the referent TS-7's computed `levy` needs (§3.1). Without it no producer
    makes the claim, except a cell that already read `recruits`. That would be circular.
  - **[INFERRED]:** that the W-B second deposit (`witness.py:549-580`) [CHECKED] lands the
    observation as a claim for a seat-channel recipient. The comment at `:428-429` says it does. TS-3
    (ix) shows it or fails.
- **World-gen leaves every pool empty**, so each settlement's pool fills by regrowth over its first
  seasons. A pool filled at world-gen would write nothing until a levy debited it, and no seat would
  ever hear of it. **What follows for computed play:** a seat learns of a pool while it fills or
  refills, and a full, untouched pool is silent. The claim decays like any other.
- **`recruit_regrowth`** is per-mille of the ceiling per season. **[OPEN — Jordan tuning]**. Sweep 0
  (the control: a pool that never fills), 250, 1000 (`_part2` §6).
- **Not scaled by `season_factor`.** Tying recruits to the harvest is available and not asked for.
- **This is a new clock write,** counted in §3.5.

### 2.4 The troop body under the pool: the candidates and their full footprint (J-1)

R-POOL fixes where troops come from. It does not fix what a raised troop is. The candidates:
- **P:** a company `Person` minted from the pool.
- **P′:** P without `reside`, with dissolution keyed on state.
- **A:** a troop stock on the rung (**the default**).
- **B:** a typed troop row.

**The second correction said A "violates the fewest ruled things: one … against P's four". That count
was not a measurement** (third critic, finding 1). It counted one Layer 1 line for A and missed five
more, and it counted P's Layer 1 lines as one. The table below lists every ratified or ruled line
each candidate touches.

**Key:**
- **amends:** the line must be rewritten.
- **strains:** the letter holds, and its stated reason or spirit is crossed.
- **violates:** the content of a Jordan ruling is broken.
- **keeps:** the line is not touched.

**Ratified Layer 1 (ED-IN-0204)**, all [CHECKED]:

| line | text, in substance | **A** | **P** | **P′** | **B** |
|---|---|---|---|---|---|
| `04:793` · `03:261` · `10:89` | units = persons at weight; one type; no unit class | **amends** (×3) | keeps | keeps | **amends** (×3) |
| `04:792` · `03:260` · `10:88` | sides = the two factions' `members` rosters | keeps | **amends** (×3): servants who hold no `commit` stand for the lord's faction | **amends** (×3) | keeps |
| `04:802` · `03:269-270` · `10:97-98` | one scale down, the same thing; every combatant a `Person` | **amends** (×3): the mass scale counts men who are not persons | **strains** (×3): every combatant is a person, but the mass muster is no longer the squad's | **strains** (×3) | **amends** (×3) |
| `04:123` · `01:497-499` (T-l) | one `Person` class, no subclass; "a second type means every mechanism has two code paths, and two code paths drift" | **strains:** no `Person` subclass, but the forcing reason is incurred, in a second kind of mouth in `subsistence_draw` and a second casualty path in `_eff_march` | keeps | keeps | **amends** (×2) |
| `04:252` · `01:896` | the Rung is "the address, never the occupant" | **strains:** passes `01:908`'s ADMITS test by its letter (an arrangement of a place, not a choice, a mood or a reputation), but men counted on a Rung are its occupants in ordinary usage | keeps | keeps | depends where the row lives (not designed) |
| `04:257` · `01:910-911` | the Rung's NEVER list: "discipline-as-a-stored-value" | **strains:** a stock stores a count per grade, and the grade's roster row sets a discipline offset (§2.7). A grade is discipline under another name | keeps: grade would live on the company `Person` | keeps | depends |
| `04:765` · `04:780` | `contest(…, claimants : PersonId[], …)`; "a faction as combatant -- `claimants : PersonId[]`, STRUCTURAL" | **keeps:** no seam parameter (`_part2` §4.1); every fought side has a member present, because a side with none is `Unopposed`. A side's strength is now its faction's stocks at the place, which is the leak's spirit, named | keeps | keeps | keeps |

**Rulings and ruled rows:**

| ruling | **A** | **P** | **P′** | **B** |
|---|---|---|---|---|
| **ED-WR-0011** (RULED, Option A) | keeps: mints nobody | **violates** as the code applies it to cohorts (`world_q.py:824`) [CHECKED]. X-4's contrary reading frees a cohort's weight, not a new cohort `Person` | **violates** | keeps if no `Person` is minted |
| **RR-2 / ED-SE-0051** (RULED) | keeps: a stock is not population | **violates:** a minted `reside` is a birth | keeps: no `reside` | keeps |
| **J-16 / H-173** (delegated-ruled) | keeps: no `oblige`, no dissolution | **violates:** `is_company` reads `Term.declared_by`, which renewal overwrites (§1.5 item 27) | **needs J-16's acceptance:** a state only companies have may be an origin branch in disguise | keeps |
| **R-POOL** (Jordan) | keeps, with the draw order of §2.5 | **fails under dearth** unless an order rule is added: the draw walks sorted ids (`world_q.py:858`) [CHECKED], a minted id is 16 hex characters (`state/ids.py:19-21`) [CHECKED], and 13 of 16 leading characters (`0`–`c`) sort before `cohort_…` [INFERRED], so most companies eat first | as P | not designed |
| **ED-IN-0279** (ruled `march` row) | **widens the row's declaration:** `Rung.stores` under `Won` and `Lost`, `Site.condition` under `Won` (`_part2` §4.6). The content, casualties only on the losing side, is kept | keeps: casualties land on a company's `body`, already declared | keeps | not designed |
| **Garrison ruling** (`world_q.py:1275-1278`) | keeps, and extends: the garrison's `condition` also sizes the defence's men (`_part2` §4.1) | keeps | keeps | keeps |
| **"present at the target"** (`world_q.py:1257-1259`) | keeps: members present | keeps the spatial reading; widens who is a member (the `mustered` clause) | as P | keeps |
| **`24f` / ED-IN-0255** (code rule "only a cohort eats") | **amends the code rule, not the ruling:** troop stocks join the draw after persons. The ruling's words exempt lords and guild members, not masses (`world_q.py:815-822`) [CHECKED] | keeps | keeps | not designed |

**What the table supports, and what it does not:**
- **No candidate is cleanest.** "Fewest" is withdrawn.
- **A** violates no ruling's content. It amends **two** Layer 1 sentences, each stated in three
  documents, so six lines. It strains three clauses, and it widens one ruled row's declaration.
- **P′** amends **one** Layer 1 sentence (three lines) and strains one. It overturns ED-WR-0011, and
  it needs J-16's acceptance.
- **P** adds three more ruling breaches to P′'s. Two of them are repairable inside P: RR-2, by P′'s
  form, and R-POOL, by an order rule.
- **B** amends the most Layer 1 (both of A's sentences and T-l). Its rulings are undesigned.
- **The default stays A, for one stated reason:** ED-WR-0011's text forbids exactly what P and P′
  need, "a producer for Person". A's breaches are all of Layer 1 text that was written when a person
  was the only carrier of headcount. **Both are ratified by Jordan, so this weighs one ratified thing
  against another, and J-1 is escalated.**

**The amended text under A**, in substance:
- **`04:793` (and `03:261`, `10:89`):** "units = the `PersonId[]` who stand and command, plus the
  troop stocks the side fields, counted in `Rung.stores`. No unit carrier exists in `World`. At the
  seam, each side's composition crosses as a frozen input record, the order of battle (`_part2`
  §4.2), built from the projection as `MassBattleInput` is today."
  - The second correction's wording, "a troop is a count, never a record", is withdrawn. It
    contradicted the design's own `OrderOfBattle`, a per-side record crossing the seam.
- **`04:802` (and `03:269-270`, `10:97-98`):** "grid squad combat: who stands is the same one scale
  down (`members ∩ present-at-rung`, resolved once). At the squad scale every combatant is a
  `Person`. At the mass scale, persons command counted men."
- **`massbattle.py:321-323`**, a code docstring that restates the old line, is edited with it.

**What A loses, stated as plainly as P's breaches:**
- **A troop cannot choose.** It does not deliberate, so it cannot desert by `release`, defect by
  regard, or witness its lord's orders.
- **A troop carries no grudge.** The morale and grudge rows `_eff_march` writes land on the persons
  present (the commanders), as today (`_part2` §4.1).
- **What survives without a person:** defection follows the rung's holder, so a lord who keeps his
  settlement when he defects takes its levies with him (NPC5, `_part2` §4.7). Hunger takes men off a
  stock that is not fed (§2.5). Kit stays with the town.
- **What A gains besides the rulings:** no chooser load per company; no S9 remnant (a stock of 1 is a
  valid stock); no gate basis, no `founding` clause, no dissolution rule, no `service_faction`, no
  muster edit. The second correction also listed "equipment reachable in computed play". **That is
  withdrawn:** nothing produces arms or a `stores:<arms>` claim (§0 item 5).

**If Jordan takes P instead,** J-1 must also **narrow ED-WR-0011** to the named cast, on X-4's
reading (`00_COMPARATIVE_ANALYSIS.md:204`) [CHECKED-2]. CENSUS's individuation (`census.py:105-112`)
[CHECKED-2] is the precedent for a run-time `Person`. P then needs, at least:
- P′'s no-`reside` form (RR-2);
- a dissolution rule that reads no origin (J-16), or J-16 overturned;
- an explicit draw-order rule (§2.5);
- the `_rehome` safety comments corrected, because they rest on "nothing in `loop/` or an effect
  constructs [a Person]" (`loop/matter.py:108-121`; `state/world.py:792-805`) [CHECKED-2].

P's full apparatus is kept in `_part2` §4.8.

**The contrary reading of demand (1), inside J-1:** "their own resource" reads toward "a rung-held
carrier" (`00_COMPARATIVE_ANALYSIS.md:202`) [CHECKED-2]. The MB lane reads the demand as "the field's
troop count should come from a levied stock" (`MB_mass_battle.md:434`) [CHECKED-2]. A meets both.

### 2.5 What a raise does to the settlement

- **The cohort is untouched.** `levy` writes one rung's `stores`: `recruits` down, a troop kind up, in
  one `Change`. The cohort's `weight`, stance and `subsistence_draw` row are byte-unchanged (R-POOL;
  TS-4's falsifier).
- **A raised levy eats where it stands, after the people.** `subsistence_draw`, the one owner of who
  eats (`world_q.py:803-880`) [CHECKED], gains a second kind of mouth: every troop stock on a rung,
  at `want = subsistence_weight[k] × count`. Stocks are drawn **after every person**, rungs in sorted
  id order.
  - **The record's key type changes** (third critic, finding 9). Today it is `{person id: …}`
    (`world_q.py:804`) [CHECKED]. Stock rows are keyed `(rung, troop kind)` and appended after every
    person row, so the persons' insertion order, and with it the stores-update order MATTER hashes
    (`matter.py:342-343`) [CHECKED], is unchanged on a world with no stock. `_drawn_under` reads
    the home from the value (`world_q.py:959`) [CHECKED], so `demanded`/`delivered` need no change
    beyond their docstrings ("an eater is a COHORT", `:885-887`) [CHECKED].
  - **Why after:** under scarcity the town's people are fed first, so a raise never shortens the
    cohort's row in the season it eats.
  - **A short stock loses men.** MATTER's record loop (`matter.py:348-353`) [CHECKED] splits the
    shortfall in two:
    - `short_by_person`, keyed by person id as today;
    - `short_by_stock`, keyed `(rung, kind)`.
    - **`_subsistence_shortfall` stays person-keyed** (`:420`), so the census report
      (`populated.py:1498`) and the two pins (`test_governance_build.py:521`;
      `test_territorial_subsistence.py:295`) [CHECKED] read what they read today. The pins' worlds
      hold no stock.
    - **The body write loops `short_by_person` only** (`matter.py:443-463`) [CHECKED]. A new loop
      beside it debits each short stock by its unmet share, on §2.8's half-up per-mille rule, through
      `w.write("stores", …)` with the shortfall `observed`. The exact share form is fixed at TS-11
      **[OPEN]**.
  - **A residual, named:** across seasons, a levy can eat a surplus that would have fed the cohort
    later, and the cohort's `body` (never its `weight`) can then fall for dearth. That reads R-POOL
    as protecting the cohort's size, which MATTER never writes. If Jordan reads it wider, a stock must
    eat only from a reserved share, which is a second rule.
- **Men are not sensed as food.** `SUBSIST` (`probes.py:144-149`) [CHECKED-2] sums only the kinds
  with a `subsistence_weight` row.
  - **What the probes show** [RAN; outputs saved, `_part2` §10]:
    - at the first DELIBERATE's state (`build_realm(0)`, then MATTER once), all 37 cohorts sense 1000
      with or without `recruits: 2` at their rung (moved 0);
    - with one rung's larder set to `grain: 1`, its cohort senses 500, and 1000 with `recruits: 2`.
  - The second correction's "bites at the first deliberation" is withdrawn (third critic, finding
    8). The build state it measured is never sensed: the driver runs MATTER, which credits yield,
    before the first DELIBERATE (`driver.py:432-433`) [CHECKED].
  - **This fix moves goldens wherever a deliberating person's rung is short of food and holds coin,
    timber or ore.** Their size is **[UNVERIFIED]**, measured at TS-3.
- **`population` does not change.** A stock is not a resident, so `migrate` is unaffected and RR-2 is
  not engaged.
- **Production does not fall,** because nothing models labour (`matter.py:504-520`) [CHECKED], and
  R-POOL makes that the ruling.

### 2.6 Who counts as troops

**Only troop stocks, plus the defending garrison (`_part2` §4.1). No person fields men.** A named
person at `weight == 1` commands. A cohort person fields nothing either, even if it ever holds a
`commit`: its men are counted in the pool, and fielding its weight too would count them twice.
- **The ladder** (third critic, finding 12 re-laddered J-6): `24f` is about who **eats**, not who
  fights, so it is no precedent here. The answer is R-POOL itself: "available troops to raise should
  be derived from" the settlement's own value. Troops are what is raised from that value, so they are
  the pool's men and never a person's weight. Step 5 agrees: a person fielding his weight beside the
  pool would count one population twice.
- **So `Person.weight` stops being a battle input** (`_part2` §4.5).

### 2.7 Troop kind and grade

- **The grade is the troop stock's matter kind.** `rosters.yaml: troop_grades` lists ordered rows
  `{id, discipline: +d, morale: +m}`; the loader derives one `matter_kinds` row per grade, named
  `troops_<id>` (`troops_raw`, …). One owner, the grade roster; no second list.
  - `levy` always credits grade 0 (`troops_raw`).
  - **Veterans are never diluted** (K-MB-3, `MB_mass_battle.md:717`): two grades on one rung are two
    stocks and two subunits, never averaged.
  - **No computed producer of grade** until J-5 (c) or a J-13 change.
  - **This is the NEVER-list strain of §2.4:** the stored thing is a count per grade, and the grade
    carries a discipline offset.
- **The troop kind is derived by the module from the kit.**
  - **The owner of the kit → kind derivation is a new function, `kind_for_kit(kit, men)`,** beside
    `TROOP_LOADOUT`. It reads `TROOP_LOADOUT`'s named kind → (weapon, armour) association as data. The
    module calls that table "INERT … NOT a derivation" and itself "NOT YET WIRED"
    (`equipment/__init__.py:10-12`, `:17-20`) [CHECKED]. `kind_for_kit` is its first consumer, so
    both sentences are edited in the same position (TS-5), and the table becomes load-bearing.
  - **The host passes kit, not a kind:** for each grade stock at the field's rung, its count and the
    rung's stores of equipment kinds. The seam reaches the module by an entry string, not an import
    (`seam/wrappers/mass_battle.py:72-78`) [CHECKED-2].
  - **The rule:** it walks `TROOP_LOADOUT`'s rows heaviest armour first (`ARMOURY` order), then key
    order. Each row takes as many of the men as the kit covers: one unit of the row's weapon class and
    one of its armour class per weight unit, and armour `none` needs nothing. It returns `((kind,
    men), …)`. The remainder is the module's declared unarmed kind, `UNARMED_KIND = "levy"`.
  - **⚠ One kind reached two ways** (third critic, finding 14). `levy` is both a row armed with
    `light_cut` (`equipment/__init__.py:22`) [CHECKED] and the unarmed remainder. So a `light_cut`
    issued to raw men changes nothing: they field as `levy` either way. **[OPEN — MB]:** add an
    unarmed troop type, or accept that `levy`'s preset already prices the poorest kit and drop
    `light_cut` from its row.
  - **When stocks of two grades share one rung's kit,** the higher grade is equipped first. **[OPEN —
    MB]** if Jordan prefers the reverse.
  - **What the derivation exposes as MB data [OPEN]:** `mounted_archers` is unreachable by kit
    (it shares `archers`' row); `cavalry` needs no horses; `knights_templar` is reached by
    `heavy_blunt`/`heavy` (`equipment/__init__.py:30`) [CHECKED]. A mount column belongs in
    `TROOP_LOADOUT`.
- **Kit is the town's.** It stays in the settlement's `stores` whatever happens in a field. A lost
  battle kills men, not swords. That is an abstraction, named.

### 2.8 Quantity, conservation and integers

**Men per weight.** The pool and the stocks count in `weight` units, the unit cohorts eat in. One
number converts them to men: `men_per_weight`, applied **once**, in the module's build:
`troops = count × men_per_weight`, an int. **[OPEN — Jordan tuning]**. For every falsifier run it is
fixed at **250**: a full shipped pool of 2 is 500 men, clear of `SUBUNIT_ROUT_FLOOR = 80` and of the
≈120-troop scale the MB lane measured (`MB_mass_battle.md:515`, `:521`) [CHECKED-2 as citations].
**The garrison's men** use a second fixture, `garrison_men`: the men a garrison at full `condition`
fields (`_part2` §4.1). **[OPEN — Jordan tuning]**, falsifier value **250**.

**Conservation.** Nothing is minted or lost without a receipt (the W3 lesson, `effects_shared.py:117-128`)
[CHECKED-1]:

| motion | conserved quantity | receipt |
|---|---|---|
| regrowth (MATTER) | `recruits` rises by `growth`, capped: the one **source** of men | `stores.changed` on the rung, with the pool `observed` |
| `levy` | `recruits` falls by `n` and `troops_raw` rises by `n` on the same rung, one `Change` | `levy.raised` |
| `transfer` (troops or kit) | Σ stores per kind, through `_shift`; troops only between settlements | `transfer.made` on both rungs |
| a lost field | the losing stocks fall by the casualties: a **sink**, deaths. A losing defence's garrison `condition` falls by the same per-mille | `field.lost`/`field.won`, `stores.changed`, `condition.worn` |
| an unfed stock | the stock falls by its unmet share: a **sink**, hunger | `stores.changed` with the shortfall `observed` |

**The falsifier for every row is one test: weigh the world.** Sum stores per kind over rungs before
and after; the difference equals the declared sources and sinks.

**Integers.** The pool, a ceiling, a stock, a grade and `troops` are ints. The one float the field
produces is the engine's survivor ratio, converted once at the host to per-mille,
`floor(pct × 1000 + 0.5)`. A stock's survivors are `(count × permille + 500) // 1000`. **One rounding
rule:** half-up per-mille, for the ceiling, the growth, the garrison and the survivors. Today's
individual casualty multiplies `body` by a float (`effects_combat.py:250-255`) [CHECKED]; TS-6 routes
it through the same per-mille.

### 2.9 When does a levy end, and what bounds it?

**Under A there is no service to end.** A stock stands until it is killed in a field, starves, or is
moved. No term, no `oblige`, no dissolution rule (J-16 kept).
- **In the short run the bound is the pool's regrowth, not food** (third critic, finding 7). The
  second correction's "the bound on armies is food" is narrowed.
  - **Measured** [RAN]: on `build_realm(0)` every settlement yields 40 grain and 30 salt a season,
    falling to 38/29 by season 4 as Sites wear. Its cohort at weight 2 eats 4 grain and 2 salt.
  - **Projected, arithmetic, not an engine run** [RAN]: the whole pool raised every season, at the
    falsifier values (ceiling 2, growth 1), yield held at 40/30. The stock reaches 13 in 12 seasons
    and is never short. It is first short in season 34, at 34 units, and then holds at 18.
  - So one settlement's levy is bounded by regrowth for decades of seasons. Food binds sooner where
    levies are **gathered**: a rung's surplus feeds about 18 units at these values, whatever their
    origin. TS-11 (ii) measures both through the real driver.
- **No stand-down act is added.** A seat that wants its men home has no verb for it. That is an
  addition only if Jordan asks (a `levy` inverse, troops → `recruits` up to the ceiling); it is listed
  under J-1, not built.
- **Veterans persist by construction** as grade stocks, so J-5's option (d) becomes moot under A.

### 2.10 A political cost of raising: weighed, not adopted

Two prior sources put an order or compliance cost on conscription:
- **The SE research row:** "RoTK VIII order<25 blocks conscription", and for the old store act
  "Tilly/Levi/Brewer: yield scales with compliance … the compliance mechanism the research isolates
  is absent" (`research/by_lane/SE_settlements_territory_economy.md:97`, `:187`) [CHECKED]. Both rows
  were written against the store act.
- **ED-FA-0010:** a closed design in which conscription cost "PS -1 in the levied province -- the levy
  IS the tax" (`registers/editorial_ledger_fa_archive.jsonl:9`) [CHECKED].
  - Its status is `superseded`. It was closed because its target layer was retired, and it notes
    "the design may re-enter as a verb at the faction or settlement scale".

**Not adopted here, on the ladder:**
- **Step 1:** ED-FA-0010 is superseded.
- **Step 5:** a province-level PS or order value would be a social aggregate on a Rung, which the
  NEVER list bans (`01:910-911`) [CHECKED].
- **The one lawful carrier** is the cohort's own `stance` toward the seat's faction. Writing it would
  break TS-4 (i)'s byte-identity of the cohort, which reads R-POOL narrowly.
- **If Jordan wants raising to cost loyalty,** it is one stance row on the cohort per `levy`, added to
  the row's `writes`. It is listed under J-1's consequences, not built.

---

## 3. THE VERBS

### 3.1 `levy`: raise troops from a settlement's pool

The row below is illustrative, in the table's own shape. It binds nothing until it is written into
`engine/season/verb_table.yaml` and the loader accepts it.

```yaml
- verb:        "levy"
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
  emits:       ["levy.raised"]
  emits_on_refusal:
    eligibility: ["levy.unauthorized"]
    authority:   ["levy.unauthorized"]
    stores:      ["levy.refused"]
    write:       ["levy.refused"]
  grade:       "assumption"
```

**Why `levy`** (third critic, finding 12; the ladder applied):
- **No escalation is needed.** A verb name does not lead to "materially different games".
- **Step 5 and Jordan's own words decide it.** Demand (1) says "troops levied from settlements".
  Demand (4) says the word is wrong only for goods.
- **The brief reserves the *store act's* name to Jordan, not this one.** Its words: "`levy` is the
  natural name for the troop-raising verb … Do not choose the new name for the store act" (the
  session brief's statement 5, which is not in the tree) [CHECKED]. The second correction's "the
  brief reserves it" misread that line.
- **The collision is TS-L's cost, not a decision.** TS-L is a build position before TS-4 (`_part2`
  §7). It costs:
  - **re-keying the store-act text:** 23 `levy` lines in `engine/season/requirements.yaml` and 19 in
    `hole_register.yaml` [RAN, `git grep -c -w`]. They include historical refusal counts under the
    old event kinds `levy.refused` and `levy.unauthorized` (`requirements.yaml:772`;
    `hole_register.yaml:3641`) [CHECKED], which this row's refusals reuse. Each is re-keyed to
    `requisition` with "(then named `levy`)", so the record of what ran stays true;
  - **IN-49's EXIT** (`_part5.md:215`) [CHECKED-1];
  - **the r2 note** "ruled `levy` deleted (§A.20)" (`world_q.py:910-914`) [CHECKED]. That ruling
    deleted a round-one policy clause, not a word. The note gains one sentence saying the troop verb
    is a different act.
- **What `levy` does not collide with:**
  - the module's `levy` troop type (`registry.py:41`; `equipment/__init__.py:22`) [CHECKED], which is
    another namespace and the right word for raw raised men;
  - "Lions' Table: Military coordination, levy operations, Royal Guard" (`rosters.yaml:1582`;
    `goals.yaml:413`) [CHECKED], which already uses the word in the military sense.

**The typed cell is `requisition`'s, conjunct for conjunct:** `basis`/purview as `authority`, and the
`stores` threshold keyed `kind` as `stores` (`verb_table.yaml:637-650`) [CHECKED-2].
- **It differs in eligibility:** `remit:dispatch`, the remit `march` uses (`verb_table.yaml:668`)
  [CHECKED], and no `presence:<rung>` alternative. That alternative is declined for every computed act
  anyway, "because the ARGUMENT IS A PLACEHOLDER" (`options.py:380`, H-75) [CHECKED-2].

**Operands:**
- **`subject`** is the settlement rung.
- **`kind` is an operand, not a literal** (§1.4 item 17). In computed play it comes from the generic
  chain (§1.4 item 18), which yields `grain` unless the question is about a `stores:<kind>` claim. A
  per-verb default there is forbidden (`options.py:763-767`) [CHECKED-2]. So:
  - **the effect declines `kind != "recruits"`** (→ `write` → `levy.refused`). A levy of grain is
    refused, never performed against the pool;
  - **the computed referent is the regrowth's claim** (§2.3). A governor holding a `stores:recruits`
    claim about a settlement has a question whose `store_kind_of` (`options.py:630-651`) [CHECKED]
    yields `recruits`, and whose referent binds `subject` (`options.py:861-862`) [CHECKED]. TS-7
    shows it forms. **The second correction's [INFERRED] premise, that a plain `stores.changed`
    deposits such a claim, was false** (§1.4 item 19). The producer is now designed, not inferred.
- **`amount`** comes from the same chain: a held shortfall claim, else `default_transfer_amount`,
  shipped 1 (`options.py:876-877`) [CHECKED]. Under A a levy of 1 is a valid stock.

**The effect, `_eff_levy`** (in `loop/effects_governance.py`, beside `_eff_requisition`):
1. Resolve the seat (`_exercised_office`) [CHECKED-draft], the settlement `rung`, `kind` and `n`.
2. **Decline** (→ `write` → `levy.refused`) when any of these holds:
   - there is no seat;
   - `kind != "recruits"`;
   - `rung.stores["recruits"] < n`: **the pool is short.** The cell tests the same thing when `kind`
     is `recruits`. The effect re-tests it because it is the write's own guard, and two acts in one
     fold may draw the same pool;
   - `n <= 0`.
3. **Move,** in one `Change` on the one rung: `recruits -= n`, `troops_raw += n`, through
   `w.write("stores", …)`, emitting `stores.changed` and `levy.raised`.

**Writes, and their classes:** `(Rung, stores)` at RES, `[MAT, RES]` already [CHECKED]. No Person, no
Tenure, no gate basis, no `founding` clause. The casualty writes at ENC are `march`'s (`_part2` §4.6).

**Per-clause refusals** (`04 §B.13` invariant 4) [CHECKED-draft]:
- **`levy.unauthorized`** means the SEAT failed: no seat granting `dispatch`, or its purview does not
  reach the settlement.
- **`levy.refused`** means the PLACE failed: the pool is short, or the act asked for something that is
  not the pool.

### 3.2 The companion acts: each needed, and none of them new

| need | act | reused as it stands? | what the troop stock adds to it |
|---|---|---|---|
| fill a treasury with goods, including arms | **`requisition`** (`verb_table.yaml:629-663`) | **yes**, plus the `placeable` refusal | it may move a troop stock into the seat's treasury **only when that treasury is a settlement** (§2.1) |
| equip a levy | **`transfer`** of an arms kind into the settlement where the levy stands | **yes**, plus `placeable` | new `matter_kinds` rows for kit (`_part2` §6). **Not reachable in computed play:** no arms producer, and no `stores:<arms>` claim producer (§0 item 5) |
| bring levies from several settlements to one muster | **`transfer`** of a troop kind to the origin settlement | **yes**, plus `placeable` | in computed play, `from` is the seat's treasury (`options.py:871-872`) [CHECKED], so a computed gathering starts only from a seat whose rung is a settlement holding troops, and its `kind` needs a `stores:troops_<g>` claim, which only a cell's read produces. **Effectively player and hand-built only [INFERRED]** |
| drill a levy | **`train`** (IN-12 step 9, unbuilt) | **no.** J-13 (iii) writes capability only where a case names a vocation (`_part5.md:73`) [CHECKED-1] | nothing until J-5 or J-13 changes |
| field the army | **`march`** (`verb_table.yaml:664-690`) [CHECKED] | **row: one act-declared payload key, `order`, and the widened `writes` (`_part2` §4.6). Effect: the write-back** | the side's composition is read, not chosen at the fold |
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
| a per-verb `kind` or `amount` default | forbidden by `options.py:763-767`; the effect declines and the regrowth claim supplies the referent |
| a season troop-kind table | `kind_for_kit` over `TROOP_LOADOUT` is the one derivation |
| a seam parameter for the origin | it would amend `04:765`; the origin is re-derived from the claimants' homes (`_part2` §4.1) |
| a political cost of raising | weighed in §2.10; Jordan's to ask for |

### 3.4 The corrected role of `requisition`

`requisition` is the store act. It moves goods from a rung in the seat's purview into the seat's
treasury (`effects_governance.py:373-412`) [CHECKED-draft]. It may not move `recruits`, and it may move
a troop stock only into a settlement treasury. The kit chain is `requisition` (arms → treasury) →
`transfer` (arms → the levy's settlement) → `kind_for_kit` → the field.

### 3.5 The meta-rule: every object added, every object cut, counted honestly

Counted per the second critic's finding 13 and the third's finding 5: event kinds, registry rows,
edits to existing rows and docstrings that state a contract, constants, result keys, register rows
and Layer 1 lines each count.

**Added under A (the default):**

| # | object | kind |
|---|---|---|
| 1 | the `levy` row | verb row |
| 2–4 | `levy.raised`, `levy.unauthorized`, `levy.refused` | event kinds (an unregistered kind fails at `log.append`, `04:776`) [CHECKED-2] |
| 5 | `_eff_levy` | effect |
| 6 | `recruits` | `matter_kinds` row |
| 7 | `troop_grades` | roster |
| 8 | one `troops_<id>` `matter_kinds` row per grade (4 at the proposed ladder), derived by the loader | registry rows + a loader derivation |
| 9 | kit `matter_kinds` rows, one per weapon and armour class (count **[OPEN]**) | registry rows |
| 10 | `immovable_kinds` | roster |
| 11 | `placeable(w, kind, rung)`, read in `_eff_requisition` and `_eff_transfer`, asserted in `_shift` | predicate + 3 call-site edits |
| 12 | `pool_rung_kinds` | roster |
| 13 | `recruit_ceiling` | Query |
| 14 | the regrowth pass at MATTER, with its `observed` pool read | clock write |
| 15 | `SUBSIST` reads only weighted kinds | harness edit |
| 16 | `subsistence_draw` feeds troop stocks after persons, keyed `(rung, kind)`; `demanded`/`delivered` docstrings | Query edit |
| 17 | MATTER splits `short_by_stock` from `short_by_person` and debits short stocks | clock write |
| 18 | `(Rung, stores)` gains ENC | matrix edit |
| 19 | `(Site, condition)` gains ENC (a lost defence wears the garrison) | matrix edit |
| 20 | `march`'s `writes`: `Rung.stores` under `Won` and `Lost`, `Site.condition` under `Won` | ruled-row edit (`verb_table.yaml:677-681`) |
| 21 | `_eff_march` writes casualties on stocks and the garrison, reads the origin from `parties`, and returns early only with no losing person **and** no losing stock or garrison | effect edit |
| 22 | `fielded(w, rung, faction)` | Query |
| 23 | `settlement_above(w, rung)`, extracted from `sides.py:82-84`, and `sides_of` calling it | Query + call-site edit |
| 24 | the wrapper's origin re-derivation over the claimants' homes, returned in `parties` | wrapper edit |
| 25 | the attacker-with-no-men branch | wrapper edit (a refusal) |
| 26 | the garrison's men on defence, and `Unopposed` widened to "no member present, or no men" | wrapper edit |
| 27 | `order_of_battle` | host function |
| 28 | `_side_stance` weighted by men commanded, not `Person.weight` | wrapper edit |
| 29 | `MassBattleInput.weights` → `sides` | record edit (an exchange) |
| 30 | `kind_for_kit` | module function |
| 31 | `UNARMED_KIND` | module constant |
| 32 | `equipment/__init__.py`'s "NOT YET WIRED" and "INERT" sentences | module docstring edit |
| 33 | `trim_to_command`, and `unfielded` in the result | module function + result key |
| 34 | `massbattle.py:321-323`'s contract sentence | module docstring edit |
| 35 | the WALLS and NARROW_PASS formation clauses for multi-subunit sides (TS-12) | module edit |
| 36–39 | `recruit_share`, `recruit_regrowth`, `men_per_weight`, `garrison_men` | fixtures |
| 40–47 | one hole-register row per tuning value of `_part2` §9 (8) | register rows |
| 48 | the `order` payload key on `march` | act-declared key |
| 49 | the temporary fixture `field_army` (deleted at TS-9) | scaffolding |
| 50–55 | Layer 1: `04:793`, `03:261`, `10:89`, `04:802`, `03:269-270`, `10:97-98` | Layer 1 lines (J-1) |
| 56–59 | TS-L: `requirements.yaml`, `hole_register.yaml`, IN-49's EXIT, the r2 note at `world_q.py:910-914` | text re-keyed (42 lines in the first two) |

**Cut, on disk:** `_weighted_unit` and four constants (`_MVP_SUBUNIT_SHAPE`, `_MVP_UNIT_COMMAND`,
`_SEASON_FORCE_POWER`, `_MIN_TROOPS`) (`massbattle.py:170-230`): **5 objects.** The world-gen pool
fill the second correction proposed is withdrawn (§2.3); it was never built, so it is not a cut.

**Net:** 59 added (plus the open count of kit kinds) against 5 cut. The second correction's "35"
undercounted: it omitted the `march` row edit, `fielded`, the no-men branch, the origin route, the
`_side_stance` edit, the docstring contracts, the terrain clauses, five Layer 1 lines and five
register rows. **P is not recounted on these rules** [not re-derived]. On the second correction's
narrower rules it was about 38; on these it would gain at least its register rows and its six Layer 1
lines (three amended, three strained), and it drops #17–#19 and #26. `_part2` §8.4 scores E against
these counts.
