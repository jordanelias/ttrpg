# The troop stock — part 2: the seam, the cuts, the data, the build, the NERS pass, the decisions

## Status: PROPOSED (2026-10-16). Not ratified; merge ratifies nothing unless Jordan so rules.
## Part 2 of 2. Head, verdict and §1–§3: [`2026-10-16-troop-stock-design.md`](2026-10-16-troop-stock-design.md). Locator conventions as there (`[CHECKED-draft]`, `[RAN]`, `[INFERRED]`, `[UNVERIFIED]`).

---

## 4. ARMY ASSEMBLY AND THE SEAM

### 4.1 Who stands on a side: the muster, extended by one clause

**Today.** `mustered(w, rung, faction)` returns faction members (a live `commit`) present in the
rung's subtree (`world_q.py:1256-1272`) [CHECKED-draft]. A levied company has no `commit`: it serves, it does
not believe (§2.1).

**The edit.** `mustered` returns members **∪ the establishment of the faction's seats**, both
intersected with presence in the subtree. The establishment is `establishment_of(w, seat)` over the
seats whose `faction` is this one (`world_q.py:1508-1533`; `Office.faction`, `carriers.py:887`)
[CHECKED-draft].
- **It is written once, in `mustered`**, so the attacking side (`loop/sides.py:85`) and the defending
  side (`seam/wrappers/mass_battle.py:233`) both get it from one owner [CHECKED-draft].
- **It does not touch membership.** `members` still says "THERE IS NO SECOND ROUTE"
  (`world_q.py:1154`) [CHECKED-draft]. A side in a field is not a membership: it is who stands there for
  the faction, and a seat's sworn men stand for it.

**What the edit sweeps in besides companies, named so nobody is surprised:**
- **Every person obliged to a faction's seat** now stands with it in a field at their place. That
  includes:
  - IN-36's guard cohorts (`_part5.md:158-175`) [CHECKED-draft as a citation]. That is right: guards
    defend.
  - a bench's convicts under a `determine` disposal, which is the H-173 hazard
    (`hole_register.yaml:3765`) [CHECKED-draft]. That is defensible as penal service but unasked, and it is
    recorded as a residual (§8).
- `determine` executes 0 times in the shipped worlds (H-163), so the convict case is latent today.

**Kept unchanged:**
- The attacker's exclusion of a restrained person (`sides.py:86-92`) [CHECKED-draft]. The comment there
  already names `mustered` as "the cleaner home" for it, for both sides. That move is offered to the
  MB lane and not made here.

### 4.2 What a side is: an order of battle, built by the host

`field_input` (`seam/wrappers/mass_battle.py:175-201`) [CHECKED-draft] stops passing `weights`. For each
side it passes an **order of battle**: a frozen tuple the host derives from `World`. The record
`MassBattleInput` (`queries/inputs.py:62-100`) [CHECKED-draft] trades `weights` for `sides`:

```
sides  = (OrderOfBattle_attacker, OrderOfBattle_defender)
OrderOfBattle = ( general: (name, command),
                  officers: ((name, command), …),          -- sorted by name
                  subunits: ((troop_kind, grade_offsets, troops, role, shape, officer), …) )
                                                            -- sorted by (kind, grade, officer)
```

**How the host fills one side** (one function, `order_of_battle(w, pids, general)`, in the host
wrapper, which already reads `World` for every other field):
1. **Troop-bearing persons** are the side's persons with `is_cohort` (J-6, §2.4). Named persons on the
   side contribute command, not troops.
2. **Group** the companies by `(troop_kind_of(w, pid), grade, commander)`.
   - The commander is the holder of the seat named by the company's live levy `oblige`.
   - A company with no such seat (a mustered member cohort, should one ever `commit`) reports to the
     general.
3. **One subunit per group.**
   - `troops = Σ weight × men_per_weight`, an int.
   - `grade_offsets` is that grade's `troop_grades` row.
   - `role` and `shape` come from the march payload's `order` for any company in the group (§4.3),
     else the kind's default in `troop_kinds`.
4. **The general** is the marching actor on the attacking side. On the defending side it is the
   holder of the seat holding the target, or the defending faction's leader present (`leaders`,
   `world_q.py:1165`), else no general (command at the builder's default).
5. **Command.**
   - **The code:** each commander's `command` is `Officer`'s own derivation, `derive_command` from
     charisma and cognition (`hierarchy/units.py:2699-2722`;
     `modules/mass_battle/core/exchange.py:57`) [CHECKED-draft].
   - **The source:** it is read from the person's capability once R-C-1/J-13 names one
     (`00_COMPARATIVE_ANALYSIS.md:584`, R-C-1; `_part5.md:433`, J-13) [CHECKED-draft].
   - **Until then:** `Officer`'s own default, 4 (`units.py:2711`). Even at the default, **who**
     commands matters at once, because the builder's span check bounds how many subunits each
     commander may field (`engine.py:304-345`).

A side whose order of battle holds **no subunit** has no troops:
- **An empty defending side** is `Unopposed`. That widens the existing "nobody mustered" branch
  (`mass_battle.py:235-248`) [CHECKED-draft] from no persons to no troops, under the same reason: the
  wrapper does not "launder" an empty side into a fabricated fight.
- **An empty attacking side** is the existing PARTY-GAP refusal (`mass_battle.py:224-226`) [CHECKED-draft],
  which the fold turns into `march.refused`.

### 4.3 What `march` carries

- **Unchanged:** `subject` (the Rung marched on). The row's `requires_typed`, `contests:`, eligibility
  and degree-keyed `writes` are untouched in shape.
- **Added: one optional payload key, `order`.** It maps company ids to roles. It is **not** a
  `requires_operands` member: it is read "as declared and may be absent", on the precedent of `at`,
  "a key naming none … is read as declared and may be absent" (`rosters.yaml:231-233`) [CHECKED-draft].
  - **Who carries it:** a hand-built act, or a player's act, carries the faction's choice of
    subformation per subunit.
  - **Who does not:** a computed act carries none, so every subunit takes its kind's default role.
  - **What decides the default:** an AI planner choosing roles is MB-08's "AI generals", LEAVE
    (`_part7.md:26-31`) [CHECKED-draft]. This design does not schedule it.
  - **Gating:** a role is gated by `role_allowed(kind, role)` (`registry.py:22-24`) [CHECKED-draft]. An
    `order` naming a role its kind may not take refuses at the builder, and the host turns that into
    the existing PARTY-GAP-shaped refusal, so the fold emits `march.refused` and never raises.
- **The subformation demand (3)** is met by role → shape + instructions (`config.py:582-616`,
  `TROOP_TYPE_ROLES` and `ROLE_SPEC`) [CHECKED-draft].
  - Different companies field different subunits, each in its own formation.
  - ⚠ **The `levy` kind has no menu of its own.** It falls back to `"any": ["Support", "Reserve"]`
    (`config.py:592`) [CHECKED-draft], and both are reserve postures. So the `levy` row's default in
    `troop_kinds` is `shape: Line` with no role. `build_army` accepts a shape without a role
    (`engine.py:373-377`) [CHECKED-draft]. Whether raw levies should get a front-line role menu is an MB
    data question [OPEN].

### 4.4 Where the army builder lives, and how the module uses it

1. **Move the builder into the module.** Move `build_army`, `_centered_line_cols` and `SUBUNIT_CAP`
   from `systems/mass_battle/sim/engine.py:99-173, :213-452` into a new
   `modules/mass_battle/army.py`. Leave a re-export in `engine.py`, so every harness caller (the
   workbench, `bat.py`, `tests/sim/gauge_mb.py` and 44 `tests/valoria` files;
   `grep -rl build_army tests/valoria | wc -l` → 44) [RAN] is unchanged.
   - **This creates no second construction path.** It moves the one that exists to the side of the
     seam the season can reach, per K-MB-2 (`MB_mass_battle.md:716`) [CHECKED-draft].
   - **Out of lane:** `tests/sim/gauge_mb.make_mixed_unit`, the third constructor (T-MB-19), is a
     harness object. Re-pointing it at `army.build_army` is the MB lane's.
2. **Fix the morale defect in its own commit** (§0 item 5). Give each subunit its type's preset morale
   when the spec sets none and the type has a preset. Fall back to the Unit's morale only for a type
   with no preset (DG-4's intent: no `None`). Grade offsets add to the preset.
3. **`resolve_field` builds each side with `build_army`.**
   - **Specs:** `build_army(specs, name, faction='A'|'B', command=general.command,
     officers=officers)`, with one spec per subunit row:
     `{troop_type, troops, concentration, role|shape, officer, discipline, morale}`.
   - **Discipline and morale:** the preset plus the grade offset, computed in the module from
     `stats_for(kind)`. The module owns the presets; the host owns the offsets.
   - **Unit morale-start:** `_morale_start(stance, loyalty, gain)` (`massbattle.py:119-157`), unchanged.
   - **Unknown kinds refuse:** the builder refuses a `troop_type` with no preset (§2.3).
4. **Span of control has one owner.** The host cannot pre-check it without a second copy of
   `build_army`'s check (`engine.py:304-345`). So the module gets one pure function beside it,
   `trim_to_command(specs, officers, command)`:
   - it drops the groups a commander cannot hold, smallest troops first, then by kind;
   - `build_army` calls it first, so the check and the trim are one rule in one file;
   - the dropped groups come back in the result as `unfielded`, and a company left out of a field is
     a fact a witness can learn.

### 4.5 What happens to the stub, to `Person.weight` as input, and to the 4/4 constants

| object | fate |
|---|---|
| `_MVP_SUBUNIT_SHAPE` (`massbattle.py:170-178`) | **deleted.** Shape, troop type, stance and unit type come from the kind and the role |
| `_MVP_UNIT_COMMAND` (`:182-186`) | **deleted.** Command comes from the general (`Officer` rule); discipline from preset plus grade |
| `_SEASON_FORCE_POWER` (`:196`) | **deleted.** Power comes from the kind's preset through `of_type` |
| `_MIN_TROOPS` (`:208`) | **deleted.** No side reaches the module without troops (§4.2) |
| `_weighted_unit` (`:213-230`) | **deleted** at TS-9, after the flip |
| the `[GAP …]` header line (`:32`) | **deleted.** The spec now exists, in code |
| `Person.weight` as battle input | **survives, scaled and filtered:** `troops = weight × men_per_weight` over cohort persons only. `_side_stance`'s weighting by `weight` (`mass_battle.py:126-148`) is unchanged |
| `MassBattleInput.weights` | **replaced** by `sides` (§4.2) |

### 4.6 How a field writes back

**Who lost** is read as today: `res.degree` and `res.result["parties"]`, with `Won` meaning the
defenders lost and `Lost` meaning the attacker did (`effects_combat.py:184-190, :221-226`) [CHECKED-draft].

**On the losing side:**
- **Each company** loses men:
  `weight ← (weight × survivors_permille + 500) // 1000` (§2.7).
  - The per-mille is the losing side's engine survivor ratio (`attacker_size_pct` /
    `defender_size_pct`, read today at `:227`).
  - If the result is 0, `remove_person` runs (`world.py:636`). The company's kit `_shift`s to the
    target rung's stores in the same `Change` (§2.6).
  - The `field_casualty_model` roster (`rosters.yaml:861`) keeps its meaning: `total` → weight 0;
    `none` → weight untouched.
- **Each named person** gets today's body write, unchanged.
- **Stance rows (morale and grudge)** as today, on every loser (`:256-261`).

**On the winning side: nothing**, per the ruled row ("nothing on the WINNING side",
`verb_table.yaml:682`) [CHECKED-draft]. **J-5** asks whether winners take their engine casualties and
whether either side gains experience.
- **Until Jordan rules, experience comes only from `train`.** M-MB-16 is therefore only half closed:
  drill without war.

**Weight on a remnant.** A company left at `weight == 1` is not a cohort (S9). It stops eating (24f)
and stops fielding troops (J-6). It keeps its `oblige`, kit and grade, and a later whole-take can
recall it. This is a residual (§8), not a branch.

### 4.7 Assembling from several settlements, and the commander drawn from persons

A faction assembles an army in four steps:
1. **Levy** at each settlement in its seats' purviews.
2. **Equip** with `transfer` from treasuries that `requisition` filled.
3. **Dispatch** the companies to one settlement, where they `move` themselves.
4. **March** from there.

Everything present at the origin under the marching seat's faction fights (§4.1), each company under
the holder of the seat it serves. A council seat's holder who levied his own men commands them "as
distinct from the council's collective decision-making". That is NPC5's case
(`engine/season/cases/NPC5.yaml:172`, as cited at `NPC_npc_cast.md:470`) [CHECKED-draft as a citation].
His defection takes his companies' commander off the field, and their `oblige` stays live to a seat
someone else now holds.

---

## 5. WHAT IT CUTS AND WHAT IT SUPERSEDES

| item | verdict | reason |
|---|---|---|
| **IN-52** "the levy-to-field feed" (`_part4.md:134-140`) | **withdraw** | Its premise was "`levy` moves stores, not troops … a season field is one troops-sized subunit (J-18)". Demand (4) and the rename remove the first half, and demand (2) rules the second a stub. Nothing was built (§1, item 17) |
| **LF-1** "the feed bounds troops by the treasury, using the larder's ration" | **withdraw** | Troops are persons who already eat at home through the one larder (`subsistence_draw`, `world_q.py:803-866`). Bounding a field by a second ration taken from the same treasury makes **two ladders for one quantity**: feeding the same mouths twice in a season, the S-methodology defect (§8). MB's K-MB-6 keeps the bound with the stock as its input (`MB_mass_battle.md:732`) [CHECKED-draft]; under C the stock is persons the larder already feeds, so the bound's input has gone |
| **LF-2** "the defender's treasury is the nearest held rung's stores" | **withdraw** | It falls with LF-1 and LF-3, which are its only readers |
| **LF-3** "`_eff_march` debits the ration" | **withdraw** | It is the same double draw at the fold. The design's own reason for it, "levy once and you are provisioned for every battle after" (`settlements-computation-modules.md:398-399`), does not arise: a company that is not fed starves at MATTER like any cohort, and a field cannot be fought by the dead |
| the `field_provisioning` fixture and `settlements.provision` | **withdraw** (never built) | §1, item 17 |
| **the lanes' split, X-19** (`00_COMPARATIVE_ANALYSIS.md:152, :219`) | **resolved for SE's cut** | SE cut the bound (`SE_…md:492`); MB kept it (`MB_…md:732`). The comparative put SE's cut at rank (6) with "no rank above". The withdrawal above is the reason that rank lacked: the bound double-counts under persons. **J-4** lets Jordan keep a campaign surcharge instead (§9) |
| **IN-49** (`_part5.md:211-218`) | **keep, re-framed** | It is the store act's question source, and its subject is `requisition`. "`levy` [now `requisition`]" is already written into it. What changes is IN-52's dependency: IN-52 no longer waits on it, and the troop verb needs its **own** question source (TS-7) |
| **H-49** `(Person, weight)` absent (`hole_register.yaml:558-568`) | **closed by TS-4** | `levy` and the field become runtime writers, and `weight.changed` gains a producer |
| **H-163**'s `levy` references (`hole_register.yaml:3543` and the H-163 row) | **re-named, not re-opened** | They name the store act. The rename's follow-through in `hole_register.yaml` and `requirements.yaml` is not done in the tree (`grep -l levy`: both files) [RAN]. That is a separate edit in IN, and this design does not make it |
| **MB-08**'s #445 U-1, "musters with inputs beyond headcount" (`_part7.md:28`) | **closed by TS-5/TS-8** | Kind, grade and commander are those inputs. U-2 (one equipment model for both scales) and U-6 **stay LEAVE**: the kit here is matter kinds that name the module's catalogue classes, and does not merge the catalogues |
| **IN-07/SE-02** (`_part4.md:120-133`) | **unaffected**, except that its design document's §5 is withdrawn | E1–E6 stand |
| **IN-12 step 9 `train`** (`_part5.md:73`) | **depended on** | It is the drill half of experience |
| **FA-01** (`_part7.md:119-126`) | **depended on** | A faction head seated is a head who can levy `via` his seat and march |
| **K-MB-1** (rung stock), **K-SE-13's first shape** (uncoupled kind), **K-FA-13's** whole-cohort commit, **K-IN-13**'s open form | **superseded as forms** by candidate C | Their direction is kept: troops are levied from settlements, fielded, and drawn down |

**The research rows this design closes, or narrows, when built:**
- **Closes:**
  - MB: M-MB-2 (composition), M-MB-6 (the population as soldiers), M-MB-15 (the levied stock),
    M-MB-17 (composition chosen, at the hand-built and player act).
  - SE: M-SE-9.
  - FA: M-FA-10.
  - IN: M-IN-12 (the force) and M-IN-13 (the name, already by the rename).
  - PC: M-PC-12's cohort half, because a company is fought as a subunit, not as one body. The duel
    half, a cohort in a `fight`, is PC's.
  - Composites: C-ARM-2 and C-ARM-4; C-ARM-3's naming half.
- **Narrows:**
  - M-MB-1 (the scale: it becomes one number, `men_per_weight`, Jordan's).
  - M-MB-3, M-NPC-13 and M-IN-1's commander half (who commands is live; how well waits on R-C-1).
  - M-MB-16 (drill only, until J-5).
- **Collisions resolved:** **X-2**, by choosing persons, split (C), over the coupled stock, the
  uncoupled stock and the whole-cohort commit. **X-19**, by cutting the bound.

---

## 6. DATA

Facts the engine reads go in registries code opens at runtime (CLAUDE.md §0.05 clause 1). None goes in
this document.

| fact | home | shape | value |
|---|---|---|---|
| troop kinds | `engine/season/rosters.yaml: troop_kinds` (new table) | ordered rows `{id, kit: {matter_kind: per_weight}, default: {role | shape}}`; the loader refuses a kit kind not in `matter_kinds` | ids ⊆ `TROOP_TYPE_STATS` keys, **excluding `knights_templar`**: its kit is cavalry's, and its higher discipline and morale are grade plus creed, not kit (`registry.py:49`) [CHECKED-draft]. **[OPEN — Jordan tuning]**: the kit table. A proposal to argue from: `levy` {} → `light_infantry` {weapon_light_cut 1, armour_light 1} → `heavy_infantry` {weapon_heavy_cut 1, armour_medium 1} → `pike` {weapon_pike 1, armour_medium 1} → `archers` {weapon_bow 1, armour_light 1} → `crossbow` … → `cavalry` {weapon_heavy_cut 1, armour_heavy 1, horses 1}, ordered most-demanding first |
| the kind → stat mapping | **stays** `modules/mass_battle/troop_types/registry.py: TROOP_TYPE_STATS` (a single Python owner, §0.05) | — | as canon §B.2 (`registry.py:39-57`) |
| equipment classes | `rosters.yaml: matter_kinds` (an open registry by design, `:1281-1288`) [CHECKED-draft] | new rows: one per weapon class and armour class the kit table names, plus `horses` | names mirror `ARSENAL`/`ARMOURY` keys (`weapons.py:36-45`, `armour.py:37-40`) [CHECKED-draft]. **[OPEN]**: whether arms are one kind per class or a coarser three. **No producer exists**: `site_yield` has no arms row, so arms enter only as world-gen stores until an SE row adds one (a `smithy` site kind's yield) **[OPEN — SE content]** |
| grades | `rosters.yaml: troop_grades` (new) | ordered rows `{discipline: +d, morale: +m}`, row 0 = `{0, 0}`; `train`'s cap = an index | **[OPEN — Jordan tuning]**: the ladder's length and offsets. Proposal: raw 0/0, drilled +1/+1 (`train`'s cap), seasoned +1/+2, veteran +2/+2 |
| the grade key | `verb_capability` (IN-12 step 9's mapping) | one key | name **[OPEN]**: `soldiering` proposed |
| men per weight | `data/fixtures.py`, `men_per_weight`, with a hole-register row and a sweep | int | **[OPEN — Jordan tuning]**. ≥ 120 clears the rout floor for one company (§2.4). Sweep: 1 (the control: today's scale), 120, 250 |
| levy amount | fixtures, `levy_amount`, an H-94 operand default | int, weight units | **[OPEN — Jordan tuning]**. At H-170's shipped weight of 2, only 1 is takeable |
| the levy's service term | **reuses** `oblige_term` (`fixtures.py:818`, shipped 4) | — | ⚠ the fixture now sets three things: service, sentence (H-173) and levy. Whether a levy gets its own term is **[OPEN]** |
| survivor conversion scale | **reuses** `condition_scale` (`fixtures.py:182`) | — | 1000 |
| `field_army` | fixtures, temporary arm roster `single_line \| order_of_battle` | — | shipped `single_line` until TS-8; deleted at TS-9 |

---

## 7. BUILD ORDER, EXITS AND FALSIFIERS

Positions use v9's form. Every EXIT is an execution artifact, and every FALSIFIER names its control arm.
**Golden re-records are declared at the position that causes them.**

### TS-1 · move `build_army` into `modules/mass_battle/army.py`
- STATE: unblocked      LANE: MB      R: —
- EDITS: `modules/mass_battle/army.py` (new home), `systems/mass_battle/sim/engine.py` (re-export only)
- EXIT: `python3 tools/ci_golden_modes_check.py` digests unchanged; the `tests/valoria` files that
  import `build_army` (`grep -rl build_army tests/valoria`) green.
- FALSIFIER: any harness digest moves → not a pure move. Control: the same command on the parent commit.

### TS-2 · `build_army` honours the troop type's morale preset
- STATE: after TS-1      LANE: MB
- EDITS: `modules/mass_battle/army.py` (the default at old `engine.py:427`)
- EXIT: the §0 item 5 probe prints `levy … morale 2` and `heavy_infantry … morale 5`.
- FALSIFIER: the probe still prints 6 → not fixed. Control: the same probe on TS-1, which prints 6
  [RAN on the current tree].
- GOLDENS: **declared mover** for any harness battery building a typed troop through `build_army`. Which
  batteries do is **[UNVERIFIED]**: read `bat.py`'s specs at the position.

### TS-3 · the registries and `troop_kind_of`, landed with their first reader (TS-5)
Not a position on its own: a registry with no reader is ID-13's defect (`04:469-475`; invariant 11 at `04:498`).

### TS-4 · `levy` (row, effect, gate basis, `founding` clause, matrix edit)
- STATE: unblocked (it needs a seat with `dispatch`; FA-01's seating is landed)      LANE: IN (SE)
- EDITS: `verb_table.yaml`, `loop/effects_governance.py` (`_eff_levy`), `loop/effects_shared.py`
  (`_draft`), `state/gate.py` (basis `levy`; the `founding` clause), `write_matrix.yaml`
  (`(Person, weight)`), `data/fixtures.py` (`levy_amount`), `hole_register.yaml` (H-49 closed; the
  fixture's row)
- EXIT: `populated.build_realm(0)`, one season through the real driver, with one hand-built `levy`
  act injected at RESOLVE (as `tests/test_u7_remit.py` injects remit acts):
  - `levy.taken` is in `w.log`;
  - a new `Person` exists at the cohort's settlement with `weight == levy_amount` and a live
    `oblige` to the seat;
  - the cohort's weight has fallen by the same amount;
  - **Σ weight over persons and `population(set_…)` are equal before and after.**
- FALSIFIER, against three controls on one tree and one seed:
  - (i) `amount > weight` → `levy.refused` and Σ weight unchanged;
  - (ii) a seat without `dispatch` → `levy.unauthorized`;
  - (iii) no injected act → `World.content_hash()` equal to the pre-TS-4 tree's **unless** the new row
    is formable by the chooser. In that case the hash moves by formation (the H-163 crowding shape),
    and the move is **declared** with the measured per-verb shifts (`aperture 4 0`).

### TS-5 · the order of battle at the seam, behind `field_army` (shipped `single_line`)
- STATE: after TS-1, TS-2, TS-4      LANE: MB (IN)
- EDITS: `queries/world_q.py` (`troop_kind_of`; the `mustered` clause), `queries/inputs.py`
  (`sides`), `seam/wrappers/mass_battle.py` (`order_of_battle`), `modules/mass_battle/massbattle.py`
  (`resolve_field` → `build_army`), `modules/mass_battle/army.py` (`trim_to_command`), `rosters.yaml`
  (`troop_kinds`, `troop_grades`, kit `matter_kinds`), `data/fixtures.py` (`men_per_weight`,
  `field_army`)
- EXIT, in two arms on one tree:
  - (a) `field_army: single_line` → the realm's `content_hash` after four seasons equals TS-4's
    (identical by construction: the composite path is not entered).
  - (b) `field_army: order_of_battle`, a seeded season in which a company is levied, equipped by
    `transfer` with one kit, and marched → the field's order of battle shows that kit's kind with its
    `TROOP_TYPE_STATS` power and discipline.
- FALSIFIER: two arms identical to the tick of the `transfer`, by construction (same seed, same
  injected acts up to it). Arm X has the transfer; arm Y has none, so its company derives `levy`.
  Over N ≥ 50 seeds the band distributions of the two arms' fields must differ (a χ² or exact test,
  declared at the position). Equal distributions → kit does not reach the field.

### TS-6 · write-back: casualties on `weight`, salvage, one survivor conversion
- STATE: after TS-5      LANE: MB (IN)
- EDITS: `loop/effects_combat.py` (`_eff_march`), `write_matrix.yaml` (ENC on `(Person, weight)`)
- EXIT: a seeded lost field lowers each losing company's weight by the integer rule, the kit of a
  destroyed company is on the target rung, and the world's weight and stores sums move by exactly the
  reported casualties and by 0 respectively.
- FALSIFIER: `field_casualty_model: none` (the existing control arm, `rosters.yaml:861`) → no weight
  moves. Then remove the salvage clause and the stores sum falls → it was needed.

### TS-7 · a question source that forms `levy` in computed play
- STATE: after TS-4      LANE: SE (IN)      R: R-04, R-05 (a verb that executes)
- WHAT: IN-49's shape for men instead of goods: a referent that is a cohort in the seat's purview.
  The trigger is **[OPEN]**: a threat claim (`march.declared` or `field.lost` heard of), or the seat's
  own need. Design first, as IN-49 does.
- EXIT: `python -m engine.season.harness.aperture 4 0` shows `levy` executed ≥ 1 with `via`.
- FALSIFIER: a `levy` formed over a cohort outside the seat's purview → fail. `levy` always refused →
  not built.

### TS-8 · flip `field_army` to `order_of_battle`
- STATE: after TS-5, TS-6, TS-7 (without TS-7 no company exists in computed play, and under J-6 every
  attacker has no troops, so the realm stops fighting)      LANE: MB
- EXIT: `aperture 4 0` shows `march` executed with fields whose order of battle holds more than one
  subunit, in at least one seeded world.
- GOLDENS, **declared plainly**: every realm hash that a `march` reaches moves. That covers
  `engine/season/runs/` (TRACE, the run artifacts), the `test_season_shape.py` pins that count `march`
  outcomes or `field.*` kinds, and the realm hashes pinned in `engine/season/tests`. **The re-pin is
  intended.** The control is the same command at `single_line` on the same commit.

### TS-9 · delete the stub
- STATE: after TS-8 is accepted      LANE: MB
- EDITS: delete `_weighted_unit`, `_MVP_*`, `_SEASON_FORCE_POWER`, `_MIN_TROOPS`, the `[GAP]` line and
  the `field_army` fixture with its `single_line` arm.
- EXIT: `grep -n "_weighted_unit\|_MVP_SUBUNIT_SHAPE\|field_army" -r engine modules` → 0; the files
  covering the seam green.
- FALSIFIER: the TS-8 realm hash moves → the deletion changed behaviour.

### TS-10 · experience read at the builder (needs IN-12 step 9 `train`)
- STATE: after TS-5 and `train`      LANE: MB (NPC)
- EXIT: two companies of one kind and weight, one trained to grade 1, fight the same field over N
  seeds with different band distributions. At grade 0 the field reproduces the kind's preset exactly.
- FALSIFIER: identical distributions → grade does not reach the field. Control: grade 0 on both.

---

## 8. NERS PASS ON THE DESIGN (`skills/ners/SKILL.md`, instrument A)

`[SELF-AUTHORED — bias risk]`. The producer is grading its own design. An independent reviewer should
attack §2.1's choice of C over A1 first, then the `mustered` clause (§4.1). **Grade: paper**, with
three read-only probes:
- **P1** (the morale preset) [RAN]: `levy … morale 6`, `heavy_infantry … morale 6`.
- **P2** (the span check) [RAN]: `build_army` with one officer of Command 1 over two subunits raises
  `ValueError: … commands 2 subunits, exceeding their own Command 1`. So the host cannot hand it an
  untrimmed side inside a fold, and `trim_to_command` is needed, not decoration.
- **P3** (role gating) [RAN]: a `levy` spec with role `Hold` raises `role 'Hold' not allowed for
  troop_type 'levy' (allowed: ['Support', 'Reserve'])`, which confirms §4.3's warning.

Nothing in the season was run against the design, because none of it exists.

### 8.1 N — the N-line ledger, six directions, attacks run

| object | N-line | attack | verdict |
|---|---|---|---|
| **`levy` (the verb)** | cut it, and no act turns a settlement's people into an army, so the population never fights, and war costs a place nothing | walk the cut: is anything else a producer of fighting men? `requisition` moves goods (`effects_governance.py:373-412`); `commit` makes members, but a cohort has none (`populated.py:394`) and a `commit` is belief; `migrate`/`move` relocate. No step is carried | **HOLDS.** Directions: bottom-up (settlement → field), vertical (person scale → field scale), diagonal (SE → MB) |
| **the company as a `Person`** (candidate C) | cut it for A1, and the army can no longer desert, defect, witness its defeat, or starve. R-WORLD's unwatched half loses every hook an army throws | attack: does A1 carry any of these? A stock has no `release`, no ledger and no body (AX-1). Narrowing: desertion by `release` is **reachable, not shown**; no chooser has been measured choosing it | **HOLDS, NARROWED.** Restated: *cut it, and an army cannot be the subject of any act or any claim.* Desertion as an observed behaviour is a residual (§8.4) |
| **`troop_kind_of` (derived kind)** | cut it for a stored kind, and two owners exist for one fact: a kind that disagrees with the kit becomes possible | attack: does any reader need a stored kind? The builder needs a kind at field time, and a Query answers then. Disqualifier 1 does **not** fire, because the kit is the carrier, already stored | **HOLDS.** Lateral: kit ↔ field consistency |
| **the grade on `capability`** | cut it, and a host that survived three fields is the host it was when raised (M-MB-16) | attack: is experience already carried? `Person.capability` is the carrier, and this design adds a key, not a store. **Disqualifier 2, no producer, fires partly:** `train` is unbuilt, and battle experience waits on J-5 | **HOLDS, NARROWED** to drill until J-5, with producer `train` (IN-12 step 9, unbuilt) |
| **the commander (holder of the served seat)** | cut it, and command is a constant (4), so who leads changes nothing (M-MB-3, M-NPC-13) | attack: does the commander change anything before R-C-1? Yes: the span check (P2) bounds how many subunits a commander fields, so the commander's **seat** shapes the army now. His **Command** is still 4 | **HOLDS, NARROWED:** identity matters now, capacity waits on R-C-1 |
| **the `mustered` establishment clause** | cut it, and a levied company never stands on a side, so `levy` raises men who never fight | attack: could the levy open a `commit` instead (D's route)? Yes, but that imposes a belief (§2.1). Could `sides_of` read the seat's establishment directly? That is the attacker only, so the defenders need the same read at the provider: **two copies** | **HOLDS.** Horizontal: one owner for both sides |
| **the gate basis `levy`** | cut it, and the levy's `oblige` (owned by the company, not the actor) is refused at F3 | attack: does an existing basis admit it? `T-m` needs the actor to be the owner. `determination` needs a judging seat (`gate.py:826-831`). Neither fits | **HOLDS.** Narrow: it exists for one verb, as `determination` and `warrant` do |
| **`men_per_weight`** | cut it, and every field is fought at single digits against a floor of 80 (M-MB-1) | attack: disqualifier 5, "a flat bonus"? No: it is a unit conversion applied to every side alike, not a bonus to one | **HOLDS** |
| **`trim_to_command`** | cut it, and a side that over-spans its command raises inside the fold (P2) | attack: could the host trim? Only with a second copy of `build_army`'s span rule | **HOLDS** |
| **the salvage clause** | cut it, and a destroyed company's kit sits on an orphaned rung (`world.py:751`) | attack: is that loss acceptable as "destroyed in battle"? Then it needs a receipt, and the clause is the receipt | **HOLDS** |
| **`field_army` (fixture)** | cut it, and TS-5 cannot ship hash-neutral | attack: it is scaffolding, with an N-line only during TS-5..TS-8 | **HOLDS, TEMPORARY.** Deleted at TS-9 |

**False N-lines found in what this design withdraws:**
- **LF-1 (the ration bound):** its claimed loss is "a field unprovisioned fights", but under C the
  larder already starves an unfed company. **Disqualifier 1 fires: the carrier already exists.** §5
  withdraws it.
- **LF-3 (the ration debit):** same disqualifier. It is a second draw on the same mouths.
- **`_SEASON_FORCE_POWER`:** its claimed loss is "headcount no longer feeds quality". But
  `TROOP_TYPE_STATS` is the carrier of quality per kind, and it is cut.

**False N-lines in my own additions (§9b):** none fired. I looked hardest at `troop_grades`, which is
a new table.
- **The attack:** is it a flat bonus (disqualifier 5)?
- **The residue:** it is a per-grade offset to discipline and morale, and those are the engine's own
  quality stats that `TROOP_TYPE_STATS` already sets per kind. The table makes grade a second index
  into the same two stats, not a bonus beside them.
- **The residual:** if Jordan rules a single offset per grade, the table collapses to one column, a
  smaller object.

### 8.2 R — both halves

- **R-COMPLETE:**
  - **The extremes have been walked, on paper:** a cohort at weight 1 (cannot be split, §3.1); a
    company at weight 1 (the S9 remnant, §4.6); a side with no troops (Unopposed or PARTY-GAP, §4.2);
    an over-spanned command (trimmed, §4.4).
  - **The one extreme the design does not close:** population has no producer, so a long war empties
    the realm (§2.5).
  - **FINDINGS:** one residual, named.
- **R-VARIETY:** a faction now chooses how many to levy, where, how to equip them, whom to put in
  command, and, at the player or hand-built act, each subunit's role. The single build (one Line,
  4/4) is gone. **PASS on the shape; NOT SCORABLE on the tree** until TS-8.
- **R-CHOICE:** the seat is the levying and marching seat-holder.
  - **The dominant act:** levying everyone (`amount = weight − 1`) dominates whenever its costs are
    zero.
  - **The cost the design imposes:** headcount kept at home buys nothing, because nothing models
    labour (J-2 default). So **R-CHOICE FINDING**: under J-2's default, the levy amount has no
    opportunity cost beyond the casualties a field may bring.
  - **What restores the choice:** option (b) of J-2 (labour-coupled) is exactly what would. This is
    the strongest argument for (b), and it is J-2's.
- **R-WORLD:** a dismissed company stays a person at its settlement with its kit and grade, and its
  later recall is a whole-take. Veterans persist and can be re-raised. A defeated lord's levy
  shrinks, the place's population falls, and the place's holder may `requisition` the salvage. Each
  of these is an Event a witness can learn, with no player involved. **PASS on the shape**; its hooks
  are reachable, none observed.

### 8.3 S — six directions, pause, methodology

| direction | carried by | verdict |
|---|---|---|
| **S-UP** (a demand filtered by a person) | a threat to a settlement reaches the seat as a claim. Whether the holder levies is his choice (TS-7's question source) | **PASS on the shape**, gated on TS-7 |
| **S-DOWN** (an opportunity to a party with no post) | a company is a party with no post, and its `release` (desertion) and its chooser's answers to a `dispatch` are its own | **PASS on the shape** |
| **vertical** (person scale ↔ field scale) | `troops = weight × men_per_weight`, one conversion. Command from a person through `Officer`. Write-back through `weight` | **PASS** |
| **diagonal** (SE matter → MB field) | `requisition` → `transfer` → `troop_kind_of` → `of_type` | **PASS** |
| **lateral** (sibling verbs) | `levy` and `requisition` share the authority conjunct and the keyed-refusal split | **PASS** |
| **horizontal** (both sides of one field) | one `mustered`, one `order_of_battle`, one `build_army` | **PASS** |
| **pauses correctly** | the field is resolved inside the fold, as today. A played field (a fidelity that pauses the season) is not designed here (M-MB-5) | **N-A**: unchanged by this design |
| **methodology** | **one finding resolved, one created.** Resolved: the ration bound (LF-1/LF-3) would have fed the same mouths twice. **Created:** casualties on a company are integer per-mille on `weight`, while an individual's casualty is still `int(body × float)` (`effects_combat.py:254`), two conversions for one survivor ratio. TS-6 routes both through the per-mille | **FINDINGS → TS-6** |

### 8.4 E — last, as a ratio

- **N and R found** a verb that holds, a carrier that holds, and four narrowed lines.
- **The design adds** one verb, one Query, one Query clause, one basis, one gate clause, one record
  field, one module function and three registry tables.
- **It removes** five module constants, one record field, one unbuilt module design, a fixture that
  never existed and three plan items.
- **E-OVERHEAD: PASS at medium confidence.** The new tables carry facts the engine reads, and each
  replaces a constant that was a decision nobody made.
- **E-LEGIBILITY: PASS on the shape.** A player sees men raised from a town, armed from a treasury,
  led by a named holder, and lost in a field. Each outcome traces to one of those acts.

### 8.5 The design's own falsifier (§8 of the skill)

The design's discipline is that **no fighting man exists unless a levy raised him, and none vanishes
without a receipt.**
- **Hits:** one family. **Named persons fight without being levied**: the general and his officers
  are mustered members.
- **The family is licensed narrowly by J-6.** They command and are not troops, so no troops exist
  without a levy.
- **Borderline:** a whole cohort that `commit`s to a faction on its own (no such path exists today)
  would contribute troops unlevied. That passes by tracing: its own act, a `commit`.

### 8.6 Self-audit

- **9a, backward propagation.** §0 item 6 lists closures. §5 narrows M-MB-3 and M-MB-16 to "in part",
  and §0 says "in part" for both. §2.1's cost list names the S9 remnant, and §4.6 and §8.2 carry it.
  §0 item 3 says `train` drills, and §6/§7 mark it unbuilt. No stale headline found.
- **9b, §3 on my own additions:** done in §8.1. No disqualifier fired on an addition.
  - `field_army` is scaffolding with a deletion position.
  - `levy_amount` is an H-94 operand default and needs a register row.
  - **What an independent reviewer would add:** a measured check that a split company does not crowd
    the chooser (C's cost item 1). I could not run it.

---

## 9. DECISIONS FOR JORDAN

Each decision survived CLAUDE.md §0's five tests:
1. **Superseded?** Nothing later rules it.
2. **Irrelevant?** No: each changes what a field is.
3. **Answered by a design document?** Statements 1–4 set the direction, not the choice.
4. **Answered by precedent?** Precedent leans, and the lean is stated as the default.
5. **Answered by architecture?** Where architecture decides, it is decided in the text, not listed here.

| id | the decision | options, and what each does to the game | default here | what waits on it |
|---|---|---|---|---|
| **J-1** | **what a troop is** | **(C) a company `Person`, split from the population cohort and bound by `oblige`:** armies are people who live somewhere, eat, can desert and die. Layer 1 holds. · **(A1) a stock on the Rung, coupled to population:** war is accounting; levied men leave the census and stop eating; needs `04 §C.5.1` amended. · **(A2) the same, uncoupled:** war costs no population. · **(B) a typed troop row:** a unit class; amends §C.5.1 and T-l. · **(D) the whole cohort commits:** a town fights all or nothing, and a levy imposes a belief | **C** | everything in §7 from TS-4 on |
| **J-2** | **does raising troops draw down population or labour** | **(a) headcount-coupled, labour-uncoupled:** a levy moves people into a company and the census is unchanged. Deaths shrink the population. The levy amount has no peacetime cost (§8.2's R-CHOICE finding). · **(b) labour-coupled:** production scales with unlevied weight. Levying costs harvests, which restores the levy's choice, at the price of a labour reader in the yield pass. · **(c) uncoupled:** troops bought with coin, which is A2's game | **(a)** | the yield pass is untouched under (a); (b) adds one reader to `loop/matter.py`'s yield pass |
| **J-3** | **the store act's name** | **`requisition`** (provisional, in the tree): the ordinary word for goods taken for an army or a state. · **`tax`:** ordinary for a regular, coin-shaped due, which this act is not (it takes any kind, on demand). · **`tithe`:** a tenth, and Church-specific; wrong for a lord | **`requisition`** | IN-49's text, the `hole_register.yaml`/`requirements.yaml` follow-through (§5) |
| **J-4** | **do LF-1..LF-3 stand** | **(a) withdraw all three:** troops are fed by the one larder, and a field costs men, not rations. · **(b) keep LF-1 re-pointed to the companies** (MB K-MB-6): a second ration on the same mouths, a methodology defect (§8.3). · **(c) keep LF-3 alone, as a declared campaign surcharge** (coin or grain per weight marched), named as a cost of marching rather than a feeding: war costs the treasury | **(a)** | IN-52's plan entry; the `march` row's `writes` (only under (c)) |
| **J-5** | **what a fought field writes beyond the losers' casualties, morale and grudge** (ED-IN-0279's ruled row says losses only and nothing on the winner) | **(a) as ruled:** winners untouched; experience only from `train`. · **(b) winners take their engine casualties too** (their companies' weight falls by their own survivor ratio). · **(c) survivors of both sides gain one grade step** (war teaches), with or without (b) | **(a)** until ruled. **Recommended: (b) + (c)**, since statement 1's "experience" most naturally includes war's | TS-6's write set; TS-10's battle half; M-MB-16's closure |
| **J-6** | **who counts as troops** | **(a) cohort persons only** (24f's "only a cohort eats", ED-IN-0255): named persons command. A side with no levied company has no troops. · **(b) every mustered person:** a named lord is `men_per_weight` men, and today's fields keep fighting without any levy | **(a)** | TS-5's `order_of_battle`; TS-8's dependency on TS-7 (under (a), no levy means no fight) |
| **J-7** | **the levy's term** | **(a) reuse `oblige_term`** (one service term for every service). · **(b) a `levy_term` of its own:** feudal service had its own length, and H-173 already warns that one fixture now sets sentences too | **(a)** | TS-4's fixture |

Tuning values, not decisions: `men_per_weight`, `levy_amount`, the `troop_kinds` kit table, the
`troop_grades` ladder, the arms producer (§6). Each is **[OPEN — Jordan tuning]**, with a register row
and a sweep at its position.

---

## 10. LIMITS

**Opened and read, at the lines cited:**
- **Season code:** `engine/season/verb_table.yaml` (`requisition`, `march`, `dispatch`, `give`,
  `transfer`, `release`, `migrate`, `move`, `oblige`, `petition`, `accept`);
  `loop/effects_governance.py` (`_eff_requisition`, `_eff_oblige`); `loop/effects_shared.py`;
  `loop/effects_combat.py` (`_eff_march`); `loop/effects_economy.py` (`_eff_transfer`);
  `loop/sides.py`; `loop/matter.py` (yield); `loop/census.py` (`_individuate`);
  `state/carriers.py` (Person, Rung, Act); `state/gate.py` (the basis list); `state/world.py`
  (`remove_person`); `queries/world_q.py` (`population`, `capacity`, `subsistence_draw`, `members`,
  `mustered`, `establishment_of`, `holder_faction_of`); `queries/inputs.py`; `rosters.yaml`
  (`matter_kinds`, `subsistence_weight`, `requires_operands`, `remit_acts`); `data/fixtures.py`
  (`condition_scale`, the `field_*` fixtures, `oblige_term`); `data/requires.py` (`REQUIRES_STEMS`);
  `write_matrix.yaml` (the Person rows); `harness/populated.py` (`seat_cohorts`);
  `hole_register.yaml` (H-49, H-163, H-170, H-176 and the H-173 text).
- **Mass-battle code:** `seam/wrappers/mass_battle.py`; `modules/mass_battle/massbattle.py`,
  `hierarchy/units.py` (Subunit, `of_type`, Officer, Unit), `troop_types/registry.py`, `equipment/`,
  `config.py` (roles, constants); `systems/mass_battle/sim/engine.py:99-452`.
- **Architecture and canon:** `architecture/meta/04_CODE_ARCHITECTURE.md` §A.1, §B.2, §B.3, §B.13,
  §C.5, §C.5.1, §F.19; `canon/04_game_design_constraints.md` GD-2; `skills/ners/SKILL.md`.
- **Plan and proposals:** the v9 positions IN-07, IN-12 step 9, IN-49, IN-52, MB-07r, MB-08, FA-01
  and J-13; `proposals/2026-10-07-settlements-computation-modules.md` §5;
  `proposals/2026-09-30-character-and-play-surface/08_mass_battle_units.md` §2–§3.
- **Research:** the lane rows named in the brief; C2, C3 (X-2, X-19), C7 J-C-1/J-C-2 and C8
  R-C-1/R-C-2/R-C-25 of `00_COMPARATIVE_ANALYSIS.md`.

**Ran:**
- P1–P3 (§8), each a `python -I` call against `systems.mass_battle.sim.engine.build_army` on the
  current tree;
- the greps quoted with `[RAN]`.

**Could not check:**
- **Whether a computed chooser forms `levy` on a cohort referent, and what that does to scene
  crowding.** The row does not exist. This is TS-4's falsifier (iii).
- **Whether a cohort answers `dispatch` by moving** (§3.2), and whether a `transfer` to a person-rung
  renews a term through `_renewals` (§3.2).
- **Which harness batteries TS-2's morale fix moves** (`bat.py` was not opened).
- **That `march` is folded at ENC.** I read it from the matrix comment (`write_matrix.yaml:227-231`)
  and did not trace it in `loop/resolve.py`.
- **Whether `mustered`'s new clause moves today's realm hash.** It does if any `oblige` edge stands at a
  muster site: IN-36's guard cohorts may be built, and `determine` disposals execute 0 times. Not
  measured.
- **The MB lane's scale probe** (≈120 troops, 0 of 20 wins at ≤ 80) is cited and not re-run.
- **`CURRENT.md` and `HANDOFF_MB.md` were not read** for this design, so the mass-battle head is taken
  from the code.
- **PP and ED provenance** cited through the lane files (ED-IN-0279, ED-IN-0255, ED-MB-0067, ED-1090)
  was not verified against the ledgers.
- **The `.audit/` and `.designs/` trees were not read.**
