# The troop stock — part 2: the seam, the cuts, the data, the build, the NERS pass, the decisions

## Status: PROPOSED (2026-10-16), corrected twice the same day and re-based on R-POOL. Default troop body since the second correction: **A, a troop stock**. Not ratified; merge ratifies nothing unless Jordan so rules.
## Part 2 of 2. Head, verdict, R-POOL and §1–§3: [`2026-10-16-troop-stock-design.md`](2026-10-16-troop-stock-design.md). Locator conventions as there (`[CHECKED]` = re-opened in the second correction pass; `[CHECKED-1]` = the first pass only; `[CHECKED-draft]` = drafting only; `[RAN]`, `[INFERRED]`, `[UNVERIFIED]`).

---

## 4. ARMY ASSEMBLY AND THE SEAM

### 4.1 Who stands on a side, and what they field

**Who stands is unchanged.** `mustered(w, rung, faction)` returns faction members present in the
rung's subtree (`world_q.py:1256-1272`) [CHECKED-1], for the attacker at the origin
(`loop/sides.py:77-85`) [CHECKED] and for the defender at the target (`seam/wrappers/mass_battle.py:233`)
[CHECKED]. Layer 1's muster lines (`04:792`, `:802`) stand. They command; they field no men (part 1,
§2.6).

**What a side fields is new: one Query, `fielded(w, rung, faction)`** (in `queries/world_q.py`):
- the troop stocks (`troops_<grade>` kinds) in `rung`'s own `stores`, **if** `holder_faction_of(w,
  rung) == faction` (`world_q.py:1441-1450`) [CHECKED], else none. A levy fights for whoever holds the
  walls it stands in.
- **The attacker** fields `fielded(w, origin, attacker_faction)`.
- **The defender** fields `fielded(w, target, subject)` **plus the target's `recruits`, counted as
  grade 0.** `subject` is `holder_faction_of(w, target)` already (`effects_combat.py:240`) [CHECKED], so
  the holder test passes by construction at the target.

**The defence extreme, walked** (second critic, finding 8):

| at the target | today | under A, without the pool on defence | **under A (the design)** |
|---|---|---|---|
| members present, no levy, pool > 0 | members fight at weight 1 each; "one present defender holds any settlement" (`MB_mass_battle.md:434`) [CHECKED] | **no troops → `Unopposed`.** Any levy takes any unraised town; `fort_level` and walls never engage | the pool fights as raw men under the members present; the module is called, so `fort_level` and `walls_dr` engage (`massbattle.py:273`, `:342-371`) [CHECKED] |
| no members present, a levy or a pool | `Unopposed` (`mass_battle.py:235-248`) [CHECKED] | the levy fights; a pool alone: `Unopposed` | the levy and the pool fight with no general, at the builder's default Command |
| nothing: no member, no levy, pool raised dry | `Unopposed` | `Unopposed` | **`Unopposed`.** ED-IN-0279 (a)'s branch is kept, widened from "no persons" to "no persons and no men". Raising a town dry is what leaves it open |
| an unheld settlement (`subject` is `None`) | PARTY-GAP (`mass_battle.py:227-229`) [CHECKED] | same | same; an unheld town's pool defends nobody |

**Why the pool defends (CLAUDE.md §0's ladder, step 5).** R-POOL calls the pool "available troops"
of the settlement's own; reading it at the town's own defence composes on the one carrier and adds
no act. The alternative inverts defence against today and against M-MB-1's own complaint (a town
falls to anything, so the walls are dead data). It overwrites no ruling: ED-IN-0279 (a)'s
`Unopposed` survives for a side with nobody in it. It is Jordan-vetoable and listed in §9.
- **What raising then changes at home:** the same men move from pool to stock, so a town's home
  defence is unchanged by a raise until the levy is moved away or eats itself down. A raise buys
  mobility (only a stock can be moved or march) and costs food (only a stock eats separately).
- **The pool takes casualties on defence** (§4.6): men killed at their own walls are gone, and the
  pool regrows. The cohort is untouched.

**An attacker with no men** — a march whose origin holds no stock of the marching faction — is the
existing PARTY-GAP refusal (`mass_battle.py:224-226`) [CHECKED], which the fold turns into
`march.refused`. The attacker's pool never marches.

**Morale.** `_side_stance` is unchanged: it reads the named persons present
(`seam/wrappers/mass_battle.py:126-148`) [CHECKED-1], and the morale and grudge rows `_eff_march`
writes land on them (`effects_combat.py:256-261`) [CHECKED] and are read back at their next field. A
side with men but no person present starts at base stance 0. The first critic's finding 3 (a company's
row written and never read) has no object under A.

**Two readings of "whose side", a residual:** the attacker's faction is read off the seat's label
(`Office.faction` through `faction_prop_id`, `sides.py:80`) [CHECKED]; `fielded` reads the origin's
holder. A defected holder marching through his old seat raises his old faction's side, and his own
levy at the origin does not field for it. Two readings coexist in the tree today; the MB lane
reconciles them (§8.3).

### 4.2 What a side is: an order of battle

`field_input` stops passing `weights`. `MassBattleInput` (`queries/inputs.py:62-100`) [CHECKED-draft]
trades `weights` for `sides`:

```
sides  = (OrderOfBattle_attacker, OrderOfBattle_defender)
OrderOfBattle = ( general: (name, command) | None,
                  officers: ((name, command), …),                       -- sorted by name
                  stocks:   ((grade_id, count, grade_offsets), …),       -- sorted by grade, highest first
                  kit:      ((matter_kind, units), …),                    -- the rung's kit stores, sorted
                  order:    ((grade_id, kind|None, role|shape, count|None), …) )   -- from `march`'s `order`
```

**How the host fills one side** (`order_of_battle(w, side)`, in the host wrapper):
1. **The stocks** are `fielded`'s (§4.1), as `(grade, count)`; `troops = count × men_per_weight` is
   applied by the module at build, once (part 1, §2.8).
2. **The kit** is the field rung's stores of equipment kinds. The module splits each stock by kit with
   `kind_for_kit` (part 1, §2.7), highest grade first.
3. **Subunits:** one per `(grade, derived kind)` pair with men, unless the march's `order` splits one
   by count (§4.3).
4. **The general** is the marching actor on the attacking side. On the defending side it is the holder
   of the seat holding the target if present, else the defending faction's leader present (`leaders`,
   `world_q.py:1165`) [CHECKED-1], else `None` (the builder's default Command).
5. **Officers** are the side's other named members present, sorted by id. Subunits, in the order of
   step 3, go to officers in id order, each up to his Command, and the general takes the rest up to
   his. **[ASSUMPTION; medium; MB to correct]**: no document assigns subunits to officers.
6. **Command before R-C-1** (first critic, finding 8): every season commander's Command is the
   constant 4, because the season supplies neither charisma nor cognition
   (`hierarchy/units.py:2711-2716`; `config.py:530`) [CHECKED-1]. What varies is who commands and so
   how the span check divides a side.
7. **Span of control** has one owner, `trim_to_command` beside `build_army` (§4.4).

### 4.3 What `march` carries

- **Unchanged:** `subject`, the Rung marched on, and the row's typed cell, `contests:`, eligibility and
  degree-keyed `writes`.
- **Added: one act-declared payload key, `order`,** mapping `(grade, kind)` to a role or shape, with an
  optional count that splits a stock into two subunits (demand 3's subformations).
- **A ninth operand, admitted by precedent** (first critic, finding 10): `confer`'s act-declared
  `term`, "in no operand of the closed eight" (`verb_table.yaml:177`) [CHECKED-1]. Read only by the host;
  absent on every computed act. **[ASSUMPTION; medium; Jordan to correct]**.
- **Demand (3) is met for the player and the hand-built act only.** An AI planner choosing roles is
  MB-08's "AI generals", LEAVE (`_part7.md:26-31`) [CHECKED-draft].
- **Gating:** `role_allowed(kind, role)` (`registry.py:22-24`) [CHECKED-draft]; a refused role becomes
  the PARTY-GAP-shaped refusal, so the fold emits `march.refused` and never raises.
- **Defaults** live in the module (`TROOP_TYPE_ROLES`, `ROLE_SPEC`, `config.py:582-616`)
  [CHECKED-draft]. The `levy` kind falls back to `"any": ["Support", "Reserve"]` (`:592`), so an
  unarmed subunit defaults to `shape: Line` with no role. Whether raw levies get a front-line menu is
  MB data **[OPEN]**.

### 4.4 Where the army builder lives

1. **Move** `build_army`, `_centered_line_cols` and `SUBUNIT_CAP` from
   `systems/mass_battle/sim/engine.py:99-173, :213-452` into `modules/mass_battle/army.py`, leaving a
   re-export so the 22 `tests/valoria` callers are untouched [RAN at the first correction]. Per K-MB-2
   (`MB_mass_battle.md:716`) [CHECKED-draft]. `tests/sim/gauge_mb.make_mixed_unit` is the MB lane's.
2. **The morale defect is TS-2**, gated on nothing (part 1, §0 item 9).
3. **`resolve_field` builds each side with `build_army`**, one spec per subunit: `{troop_type: kind,
   troops, role|shape, officer, discipline, morale}`, discipline and morale being the kind's preset
   (`stats_for`) plus the grade offset.
4. **`trim_to_command(specs, officers, command)`**: drops the subunits a commander cannot hold,
   smallest troops first, then by key, and returns them as `unfielded`. `build_army` calls it first, so
   the check and the trim are one rule in one file. A drafting probe (P2) showed an over-spanned side
   raising `ValueError` inside the fold.

### 4.5 What happens to the stub, to `Person.weight` as input, and to the 4/4 constants

| object | fate |
|---|---|
| `_MVP_SUBUNIT_SHAPE`, `_MVP_UNIT_COMMAND`, `_SEASON_FORCE_POWER`, `_MIN_TROOPS` (`massbattle.py:170-208`) | **deleted** at TS-9 |
| `_weighted_unit` (`:213-230`) | **deleted** at TS-9 |
| the `[GAP …]` header line (`:32`) | **deleted** |
| `Person.weight` as battle input | **cut.** No person fields men (part 1, §2.6) |
| `_side_stance` (`mass_battle.py:126-148`) | **kept unchanged** |
| `MassBattleInput.weights` | **replaced** by `sides` |

### 4.6 How a field writes back

**Who lost** is read as today (`effects_combat.py:225-227`) [CHECKED].

**On the losing side:**
- **Each fielded stock loses men:** `count ← (count × survivors_permille + 500) // 1000`, at the rung
  it stood on (the origin for an attacker, the target for a defender). The per-mille is the losing
  side's engine survivor ratio (`attacker_size_pct` / `defender_size_pct`, `:227`) [CHECKED].
- **The defender's pool** loses the same per-mille when the defender lost. The cohort is not written.
- **`field_casualty_model`** (`rosters.yaml:861`) keeps its meaning: `total` → every losing stock and
  pool to 0; `none` → nothing written; `scaled_by_degree` → the per-mille rule.
- **Each named person** gets today's body write and stance rows, unchanged (`:248-261`) [CHECKED].
- **⚠ The early return must go.** `_eff_march` returns `NO_CHANGE` when no loser is a person
  (`:228-230`) [CHECKED]. A defending side of a pool alone would then lose no men. The return becomes
  "no loser person **and** no losing stock".
- **The write is `(Rung, stores)` at ENC.** The row admits `[MAT, RES]` today [CHECKED-1], so ENC is
  added (part 1, §3.5 #19). That `march` is folded at ENC is read from the matrix comment, **not
  traced** in `loop/resolve.py` **[UNVERIFIED]**.

**On the winning side: nothing**, per the ruled row (`verb_table.yaml:682`) [CHECKED-draft]. J-5 asks
whether winners take casualties and whether anyone gains experience.

### 4.7 Assembling from several settlements, and the commander drawn from persons

A faction assembles an army in four steps:
1. **Conscript** at each settlement in its seats' purviews, as far as each pool allows.
2. **Equip** with `transfer` of arms into those settlements (computed-reachable, part 1, §3.2).
3. **Gather** with `transfer` of the troop kinds to one settlement its faction holds.
4. **March** from there.

**NPC5's need** (`engine/season/cases/NPC5.yaml:172`) [CHECKED-1]: a council commander's break with
his leader should have "a material consequence beyond a changed vote". Under A, a lord who defects and
keeps the settlements he holds takes their levies and pools with him, because `fielded` reads the
holder. If he loses a settlement, its levy serves the next holder. A levy he sent into another
faction's town serves that town's holder: a risk of gathering in an ally's walls, named.

### 4.8 If Jordan takes P: the apparatus it needs

Kept so J-1 can be decided against a complete alternative. None of it is built under A.
- **The muster amendment:** `service_faction(w, pid)` (the faction of the holder of each seat a
  person with no `commit` serves; `None` for none or many), and `mustered` = members present ∪
  persons present whose `service_faction` is the faction. The first correction's probe stands
  [RAN, first correction]: the two shipped `oblige` edges (NPC-070, NPC-041) are both from persons
  holding a `commit`, so the clause adds nobody at build.
- **The morale reader:** `faction_holding(w, pid) or service_faction(w, pid)` in `_side_stance`.
- **The company:** minted by `_eff_conscript` at `weight = n ≥ 2`, with its person-rung and `contain`,
  **without `reside`** (P′; RR-2), bound by an `oblige` under a new gate basis. It still eats at the
  muster town, because the draw reads `contain` (`world_q.py:856`) [CHECKED]. Construct the `Person`
  before adding its tenures, and correct the two `_rehome` comments (`matter.py:108-121`;
  `world.py:792-805`) [CHECKED], which already misstate the tree since `census.py:105` [CHECKED].
- **Ending service:** under J-16 [ASSUMPTION; medium], a rule reading state, not origin: "a cohort
  person with no `reside` whose last `oblige` closes dissolves into the `recruits` of the rung it
  stands on, up to the ceiling". The first correction's `is_company` read `Term.declared_by`, which
  `_renewals` overwrites (`effects_economy.py:309`) [CHECKED], and is withdrawn.
- **Upkeep, corrected** (second critic, finding 3): the first correction said "no computed act pays
  upkeep yet … a computed army lasts one term". That holds only until TS-7: `_renewals`' docstring
  says a computed `transfer` via `remit:issue` already meets clauses 1–2, and the missing piece was
  that "no computed act forms an `oblige`" (`effects_economy.py:283-290`) [CHECKED]. Once a computed
  `conscript` forms one, a computed shortfall `transfer` into the muster town renews every company
  present there (clause 4, `home_of`, `:257-264`, `:302-305`) [CHECKED]. Under P a computed army can
  therefore outlive its term, and upkeep is one person's per company of any size.
- **The draw order:** the company would eat before the cohort (an `H(…)` id sorts before
  `cohort_…` [RAN]), so P also needs "cohorts first" (part 1, §2.5).
- **ED-WR-0011** narrowed by J-1 (part 1, §2.4).

---

## 5. WHAT IT CUTS AND WHAT IT SUPERSEDES

| item | verdict | reason |
|---|---|---|
| **IN-52** "the levy-to-field feed" (`_part4.md:134-140`) | **withdraw** | its premise was the store reading of `levy`, which demand (4) removes; nothing was built [RAN at drafting] |
| **LF-1..LF-3** (a treasury ration bounding troops; its debit at the fold) | **withdraw as forms** | under A a levy eats, through `subsistence_draw`, at the larder where it stands (part 1, §2.5). A treasury ration beside it would be a second ladder for one quantity (§8.3). MB's K-MB-6 bound survives as the larder's |
| `field_provisioning`, `settlements.provision` | **withdraw** (never built) | part 1, §1 |
| **X-19** (`00_COMPARATIVE_ANALYSIS.md:219`) | **resolved** | SE cut the ration bound and MB kept it; under A the bound is the larder, kept, in the one draw |
| **IN-49** (`_part5.md:211-218`) | **keep, re-framed** | the store act's question source; its EXIT still reads "`levy` row executes" (`:215`) [CHECKED-1], which is J-3's collision. The troop verb needs its own source (TS-7) |
| **H-49** `(Person, weight)` has no runtime writer | **untouched under A** | casualties fall on stocks. Under P it would be closed |
| **H-170** the cohort weight | **untouched** | the ceiling reads it; nothing writes it |
| **H-156** (`hole_register.yaml:3540`, its `hole:` at `:3543`) [CHECKED] | **the crowding shape** | the first correction cited `:3543` as H-163; it is H-156's "mere eligibility crowds `release` out of every scene budget" (second critic, finding 11). TS-4 (iv) and TS-7 measure that shape |
| **H-163** (`hole_register.yaml:3631`) [CHECKED] | **re-named, not re-opened** | its 16 `levy` hits (`sed -n 3631,3643p … | grep -o levy`, 16) [RAN] name the store act; the follow-through is TS-L's, only if `levy` is chosen |
| **MB-08**'s #445 U-1 (`_part7.md:28`) | **closed by TS-5/TS-8** | kind, grade and commander are the inputs beyond headcount. U-2 and U-6 stay LEAVE |
| **IN-07/SE-02**, **FA-01** | unaffected / depended on | FA-01's seating gives a seat that can conscript and march |
| **K-MB-1** (rung stock) | **adopted as the form** | A is K-MB-1's rung-held stock, under the pool |
| **K-SE-13**, **K-FA-13**, **K-IN-13**'s open form | **superseded as forms** | their direction is kept: troops come from settlements, are fielded and drawn down |

**Research rows, when built:**
- **Closes:** M-MB-2, M-MB-6, M-MB-15, M-MB-17 (player and hand-built acts); M-SE-9; M-FA-10; M-IN-12,
  M-IN-13; M-PC-12's cohort half; C-ARM-2, C-ARM-4 and C-ARM-3's naming half.
- **Narrows:** M-MB-1 (the scale is one number, `men_per_weight`); M-MB-3, M-NPC-13 and M-IN-1's
  commander half (who commands is live; how well waits on R-C-1); M-MB-16 (no computed grade
  producer).
- **Collisions:** **X-2** resolved by a rung-held pool and a rung-held stock; **X-19** above; **X-4**
  left as it stands, since A grows no cohort and mints no person.

---

## 6. DATA

Facts the engine reads go in registries code opens at runtime (CLAUDE.md §0.05 clause 1). Every
number is a sourced fixture with a register row or marked **[OPEN — Jordan tuning]**. The **falsifier
value** is a control setting for §7's runs, not a proposal for the shipped value.

| fact | home | shape | value |
|---|---|---|---|
| the recruit pool | `rosters.yaml: matter_kinds`, row `recruits` (`:1279-1290`) [CHECKED-1] | whole weight units in a settlement rung's `stores` | derived: filled to the ceiling at world-gen, then regrown |
| rungs that hold a pool | `rosters.yaml: pool_rung_kinds` (new) | closed list of rung kinds | `[settlement]` |
| kinds no store act may move | `rosters.yaml: immovable_kinds` (new); the loader refuses an id not in `matter_kinds` | list | `[recruits]` |
| the ceiling's share | `data/fixtures.py`, `recruit_share`, hole row, sweep | int, per-mille | **[OPEN — Jordan tuning]**. Sweep 500 / 1000 / 2000. Falsifier value **1000** |
| the regrowth rate | fixtures, `recruit_regrowth`, hole row, sweep | int, per-mille of the ceiling per season | **[OPEN — Jordan tuning]**. Sweep **0 (control)** / 250 / 1000. Falsifier value **250** |
| men per weight | fixtures, `men_per_weight`, hole row, sweep | int | **[OPEN — Jordan tuning]**. Sweep 1 (today's scale, control) / 120 / 250. Falsifier value **250** (part 1, §2.8) |
| the raise size | **no fixture.** The generic chain: a shortfall claim, else `default_transfer_amount` (`fixtures.py:495`, shipped 1, H-94) [CHECKED] | — | the first correction's `conscript_amount` is withdrawn (part 1, §3.1) |
| grades | `rosters.yaml: troop_grades` (new) | ordered rows `{id, discipline: +d, morale: +m}`, row 0 `{raw, 0, 0}` | **[OPEN — Jordan tuning]**. Proposal: raw 0/0, drilled +1/+1, seasoned +1/+2, veteran +2/+2 |
| troop stock kinds | derived by the loader from `troop_grades`, `troops_<id>` | one `matter_kinds` row per grade | — |
| what is eaten | **reuses** `subsistence_weight` (`rosters.yaml:1371-1387`) [CHECKED] for cohorts, troop stocks **and** `SUBSIST` | — | grain 2, salt 1 (shipped; H-11) |
| kind → stats / kind → kit | **stay** `TROOP_TYPE_STATS` (`registry.py:39-57`) and `TROOP_LOADOUT` (`equipment/__init__.py:21-36`) [CHECKED-1]; `kind_for_kit` and the unarmed constant `levy` beside the latter | — | the draft's season `troop_kinds` table stays dropped (first critic, finding 5) |
| equipment matter kinds | `matter_kinds`, one row per weapon and armour class `TROOP_LOADOUT` names | — | **[OPEN]**: one kind per class or a coarser three. **No producer**: `site_yield` has no arms row (`rosters.yaml:2042-2075`) [CHECKED-1] |
| survivor conversion scale | **reuses** `condition_scale` (`fixtures.py:182`) [CHECKED-1] | — | 1000 |
| `field_army` | fixtures, temporary arm roster `single_line \| order_of_battle` | — | `single_line` until TS-8; deleted at TS-9 |

---

## 7. BUILD ORDER, EXITS AND FALSIFIERS

Positions use v9's form. Every EXIT is an execution artifact; every FALSIFIER names its control arm.
Golden re-records are declared at the position that causes them. Unless stated, runs fix
`recruit_share = 1000`, `recruit_regrowth = 250` and `men_per_weight = 250`.

### TS-1 · move `build_army` into `modules/mass_battle/army.py`
- STATE: unblocked      LANE: MB
- EXIT: `python3 tools/ci_golden_modes_check.py` digests unchanged; the 22 `tests/valoria` files that
  import `build_army` green.
- FALSIFIER: any harness digest moves → not a pure move. Control: the same command on the parent.

### TS-2 · `build_army` honours the troop type's morale preset — independent
- STATE: unblocked; lands before or without every other position      LANE: MB
- WHAT: a subunit takes its type's preset morale when the spec sets none; the Unit's morale only for a
  type with no preset (DG-4's intent: no `None`).
- EXIT: the drafting probe prints `levy … morale 2` and `heavy_infantry … morale 5`.
- FALSIFIER: still 6 → not fixed. Control: the parent commit prints 6 [RAN at drafting].
- GOLDENS: declared mover for any battery building a typed troop through `build_army` (which ones
  **[UNVERIFIED]**: read `bat.py`'s specs at the position).

### TS-3 · the recruit pool, and the subsistence formula (R-POOL)
- STATE: unblocked      LANE: SE (IN)
- EDITS: `rosters.yaml` (`recruits`, `immovable_kinds`, `pool_rung_kinds`), `queries/world_q.py`
  (`recruit_ceiling`, `movable`), `loop/matter.py` (the regrowth pass after the yield loop),
  `loop/effects_governance.py` and `loop/effects_economy.py` (the `movable` declines),
  `loop/effects_shared.py` (`_shift`'s assertion), `data/fixtures.py`, `harness/populated.py` (the
  fill), `harness/probes.py` (`SUBSIST`), `hole_register.yaml`
- EXIT: `populated.build_realm(0)`: every settlement's `recruits` equals `recruit_ceiling` (2 at the
  shipped data), no other rung holds any; four seasons run through the real driver.
- FALSIFIERS, each with its control:
  - **(i) It regrows at the stated rate.** A settlement's pool debited to 0 by hand reads 1, 2, 2 at
    the next three MATTERs. **Control:** `recruit_regrowth = 0` reads 0, 0, 0.
  - **(ii) It never passes its ceiling.** 8 seasons at `recruit_regrowth = 1000`: `recruits ≤
    recruit_ceiling` at every MATTER and settlement, and the check ran 37 × 8 times. **Control:** remove
    the `min`, and it fails at the first MATTER.
  - **(iii) Only settlements hold a pool.** After 4 seasons no rung outside `pool_rung_kinds` carries
    `recruits`. **Control:** an empty `pool_rung_kinds` filter puts a pool on territory and realm rungs.
  - **(iv) Regrowth does not depend on yield.** A hand-built settlement with no producing Site regrows.
    **Control:** the pass moved inside the yield loop after `if not produced: continue`
    (`matter.py:521-523`) [CHECKED] leaves it at 0.
  - **(v) Settlements with different cohorts differ.** Cohorts at weights 2 and 4 give ceilings 2 and
    4 (the realm builds with every cohort at 4 [RAN, first correction]). **Control:** equal weights,
    equal ceilings.
  - **(vi) A man is not goods.** A hand-built `requisition` of `recruits` → `requisition.refused`,
    stores unchanged. **Control:** the same act on `grain` executes.
  - **(vii) A man is not food, at build and under scarcity.** On `build_realm(0)`, every cohort's
    `SUBSIST` is identical with and without the pool fill, at build and with one rung's larder set to
    `grain: 1`. **Control:** today's formula, which reads 0 → 1000 at build for all 37 and 500 → 1000
    under the `grain: 1` dearth [RAN] (§10).
  - **(viii) The scene tax is measured.** `python -m engine.season.harness.aperture 4 0` before and
    after; a per-verb shift in `requisition`'s refusals is declared with its count.
- GOLDENS: **declared mover.** The fill writes every settlement's `stores`, so every realm
  `content_hash` moves at build, and `SUBSIST`'s edit moves any run in which a deliberating person's
  containing rung held coin, timber or ore. **The re-pin is intended**; its scope is measured here.

### TS-4 · `conscript` (row, effect, event kinds)
- STATE: after TS-3      LANE: IN (SE)
- EXIT: `build_realm(0)`, one season through the real driver, one hand-built `conscript` (`kind:
  recruits`, `amount: 1`) injected at RESOLVE (as `tests/test_u7_remit.py` injects remit acts):
  `conscript.taken` in `w.log`; the settlement's `recruits` fell by 1 and its `troops_raw` rose by 1.
- FALSIFIERS, on one tree and one seed:
  - **(i) R-POOL at the act, byte for byte.** The cohort's `Person` (weight, stance, tenures, body)
    and its `subsistence_draw` row are `repr`-identical before and after. **Control:** P's mint at
    weight 2 changes the settlement's `population`; A's must not.
  - **(ii) Men are conserved.** `recruits + Σ troops_*` at the rung is unchanged across the act.
  - **(iii) Refusals keyed per clause:** `amount = 3` against a pool of 2 → `conscript.refused`;
    `kind = grain` → `conscript.refused` and nothing moves (**control:** the cell alone admits it,
    because the town holds grain, which shows the effect's decline is needed); a seat without
    `dispatch` → `conscript.unauthorized`.
  - **(iv) The world without the act.** No injected act → `content_hash` equal to TS-3's, unless the
    chooser forms the row; then the move is declared with per-verb shifts (H-156's crowding shape).

### TS-11 · a levy eats where it stands, after the people
- STATE: after TS-4; **lands before TS-7**, because a computed levy that does not eat is an
  unbounded one      LANE: SE (IN)
- EDITS: `queries/world_q.py` (`subsistence_draw`; `demanded`/`delivered` docstrings),
  `loop/matter.py` (the stock debit on a short row)
- EXIT: a settlement holding a levy: `demanded` rises by exactly `Σ subsistence_weight[k] × count`.
- FALSIFIERS:
  - **(i) R-POOL under dearth.** With a larder below the cohort's want plus the levy's, the cohort's
    draw row is `repr`-identical to the same world with no levy; the levy's row is short and its stock
    falls. **Control:** the levy drawn before persons → the cohort's row changes. (This is the
    scarcity arm the second critic, finding 6, says TS-4 (i) lacked.)
  - **(ii) Food bounds an army.** One settlement raised by hand every season for 12 seasons at the
    shipped yield: the stock plateaus. **Control:** feeding off, and it grows every season.
  - **(iii) Weigh the world:** stores per kind move by exactly regrowth, raises and hunger.
- GOLDENS: moves only worlds holding a levy, i.e. none until TS-7.

### TS-5 · the order of battle at the seam, behind `field_army` (shipped `single_line`)
- STATE: after TS-1, TS-2, TS-11      LANE: MB (IN)
- EDITS: `queries/world_q.py` (`fielded`), `seam/wrappers/mass_battle.py` (`order_of_battle`; the
  defending pool; the widened `Unopposed` test), `queries/inputs.py` (`sides`),
  `modules/mass_battle/massbattle.py` (`resolve_field` → `build_army`), `modules/mass_battle/army.py`
  (`trim_to_command`), `modules/mass_battle/equipment/` (`kind_for_kit`, the unarmed constant),
  `rosters.yaml` (`troop_grades`, kit kinds), `data/fixtures.py` (`men_per_weight`, `field_army`)
- EXIT: **(a) `single_line`:** the realm `content_hash` after four seasons equals TS-11's. **(b)
  `order_of_battle`:** a seeded hand-built season with a levy raised, armed by `transfer` and marched →
  the field's order of battle shows `kind_for_kit`'s kinds with their `TROOP_TYPE_STATS` presets.
- FALSIFIERS:
  - **Kit reaches the field.** Two arms identical to the tick of the `transfer`; arm Y has none. Over
    N ≥ 50 seeds at `men_per_weight = 250`, the band distributions differ (an exact test, declared at
    the position). **Control:** equal distributions. At today's scale (1) both arms rout every run.
  - **The walls engage.** A target with members present and a pool, no levy: `order_of_battle` calls
    the module. Two arms differing only in `fort_level` give different band distributions over
    N ≥ 50 seeds. **Control:** the same two arms at equal `fort_level`, whose distributions must
    agree.
  - **The defence extreme.** A target with no member, no levy and a pool of 0 → `Unopposed`; with a
    pool of 2 → a fought field. **Control:** the pool clause removed → both `Unopposed`.

### TS-6 · write-back
- STATE: after TS-5      LANE: MB (IN)
- EDITS: `loop/effects_combat.py` (`_eff_march`: stocks, the pool, the early return; per-mille
  survivors for persons' `body` too), `write_matrix.yaml` (ENC on `(Rung, stores)`)
- EXIT: a seeded lost field lowers each losing stock (and a losing defender's pool) by the integer
  rule; the world's stores sums move by exactly the declared sinks.
- FALSIFIERS: `field_casualty_model: none` (`rosters.yaml:861`) → nothing moves. A defending side of a
  pool alone loses men. **Control:** today's early return (`effects_combat.py:228-230`) [CHECKED] → it
  loses none.

### TS-7 · a question source that forms `conscript` in computed play
- STATE: after TS-4 and TS-11      LANE: SE (IN)      R: R-04, R-05
- WHAT: IN-49's shape for men: a referent that is a **`stores:recruits` claim** about a settlement in
  the seat's purview, so `store_kind_of` supplies `kind = recruits` through the generic chain (part 1,
  §3.1). The trigger (a heard `march.declared` or `field.lost`, or the seat's own need) is **[OPEN]**.
  Design first, as IN-49 does.
- EXIT: `python -m engine.season.harness.aperture 4 0` shows `conscript` executed ≥ 1 with `via`, and
  every executed one carries `kind = recruits`.
- FALSIFIER: a `conscript` executed over a settlement outside the seat's purview → fail; `conscript`
  always refused → not built. The `kind != recruits` refusals are counted and declared (the scene tax).
- ⚠ If J-3 names the verb `levy`, this EXIT reads IN-49's word for word (`_part5.md:215`)
  [CHECKED-1]. TS-L must land first.

### TS-8 · flip `field_army` to `order_of_battle`
- STATE: after TS-5, TS-6, TS-7. Without TS-7 no levy exists in computed play and every march is
  refused, so the realm stops attacking (defence still musters the pool)      LANE: MB
- EXIT: `aperture 4 0` shows `march` executed, with fields of more than one subunit, in at least one
  seeded world.
- GOLDENS, declared plainly: every realm hash a `march` reaches moves, including
  `engine/season/runs/` artifacts, the `test_season_shape.py` pins that count `march` outcomes or
  `field.*` kinds, and the realm hashes pinned in `engine/season/tests`. **The re-pin is intended.**
  Control: the same command at `single_line` on the same commit.

### TS-9 · delete the stub
- STATE: after TS-8 is accepted      LANE: MB
- EXIT: `grep -n "_weighted_unit\|_MVP_SUBUNIT_SHAPE\|field_army" -r engine modules` → 0; the seam's
  files green.
- FALSIFIER: the TS-8 realm hash moves → the deletion changed behaviour.

### TS-10 · experience read at the builder — BLOCKED on J-5 or a J-13 change
- EXIT, on hand-set stocks: two stocks of one kind and size, one at grade 1, over N ≥ 50 seeds, give
  different band distributions; at grade 0 the field reproduces the kind's preset exactly.
- FALSIFIER: identical distributions. Control: grade 0 on both.

### TS-L · the `levy` follow-through — ONLY if J-3 names the troop verb `levy`
- STATE: before TS-4, if at all      LANE: IN
- EDITS: R-04's acceptance text and its historical store-act refusal counts in `requirements.yaml`
  (`:734-735`, `:771-772`) [CHECKED-1], `hole_register.yaml`'s 19 `levy` hits, v9 IN-49's EXIT
  (`_part5.md:215`), and the r2 note at `world_q.py:910-914` [CHECKED-1], re-keyed to `requisition`.
- EXIT: `grep -n levy requirements.yaml hole_register.yaml` returns only rows about the troop verb.
- FALSIFIER: R-04 reads met while `requisition` has never executed.

---

## 8. NERS PASS ON THE DESIGN (`skills/ners/SKILL.md`, instrument A)

`[SELF-AUTHORED — bias risk]`. Two independent critics attacked earlier states (18 and 13 findings).
The second correction changed the default body; that change has been attacked by nobody but its
author. A reviewer should start with part 1 §2.4 (the constraint table), §2.5 (the feeding rule) and
§4.1 here (the defending pool).

**Grade: paper.** Nothing in the season was run against the design, because none of it exists.

### 8.1 N — the N-line ledger

| object | N-line | attack | verdict |
|---|---|---|---|
| **`recruits`** | cut it, and R-POOL has no carrier | `envelope` is the population, not its raisable men; a Site is fabric; a field amends `04:255` | **HOLDS** |
| **`pool_rung_kinds`** | cut it, and territories hold pools that count the same men again | could the ceiling's subtree read alone stop it? No: the regrowth pass would still credit them | **HOLDS** |
| **`recruit_ceiling`** | cut it, and the pool regrows without bound | a second copy of `population`? No: cohorts only, for a different quantity | **HOLDS, NARROWED:** equal everywhere at the shipped data |
| **`immovable_kinds` / `movable`** | cut it, and `requisition` carries a town's pool into a treasury | does anything else stop it? No | **HOLDS** |
| **`SUBSIST`'s edit** | cut it, and the pool fill flips every cohort's sensed subsistence at build [RAN] | is it this design's to fix? The defect predates it (coin is sensed as food), but this design is what makes it bite | **HOLDS** |
| **`conscript`** | cut it, and no act turns a pool into a levy | `requisition` moves goods; `commit` is belief | **HOLDS** |
| **the troop stock** (A) | cut it for P, and three ruled things break (part 1, §2.4) | does A lose what made P worth it? Choice, witness, grudge: yes, named | **HOLDS, NARROWED:** R-WORLD's person half is lost |
| **the feeding rule** | cut it, and a levy is free and unbounded | is it a second eater rule? It is the one draw, with a second kind of mouth, after the first | **HOLDS** |
| **the defending pool** | cut it, and an unraised town is `Unopposed` and the walls are dead | is it a special case? No entity is named; every held settlement gets it | **HOLDS** |
| **`kind_for_kit`** | cut it, and two owners exist for kind | the builder needs a kind at field time; a function over the kit answers then | **HOLDS** |
| **the grade kinds** | cut them, and a host that survived three fields is the host it was raised | producer? **None in computed play** | **FAILS in computed play; HOLDS as a carrier** (disqualifier 2) |
| **the commander** | cut it, and who leads changes nothing | the span check divides a side by commander | **HOLDS, NARROWED** |
| **`men_per_weight`** | cut it, and every field is single digits against a floor of 80 | a flat bonus? No, a unit conversion applied to every side | **HOLDS** |
| **`trim_to_command`** | cut it, and an over-spanned side raises inside the fold (P2) | the host cannot trim without a second copy | **HOLDS** |
| **the `order` key** | cut it, and no act chooses a formation (demand 3) | a ninth operand; ladder step 4, `confer`'s `term` | **HOLDS, NARROWED** to player and hand-built acts |
| **`field_army`** | cut it, and TS-5 cannot ship hash-neutral | scaffolding | **HOLDS, TEMPORARY** |

**False N-lines in what this design withdraws:** LF-1/LF-3 (a treasury ration): disqualifier 1, the
carrier (the larder draw) exists. `_SEASON_FORCE_POWER`: `TROOP_TYPE_STATS` carries quality.
**In P's apparatus, now not built:** `is_company` read a field renewal overwrites (finding 2).

### 8.2 R — both halves

- **R-COMPLETE, the extremes walked:** an empty pool (`conscript.refused`); a full pool (no write); a
  stock of 1 (valid, no remnant); a side with no men (§4.1's table: `Unopposed` or PARTY-GAP); a town
  raised dry (open to any levy); an over-spanned command (trimmed); an unfed levy (it shrinks); a seat
  that raises every season (bounded by food, TS-11 (ii)); `recruit_regrowth = 0` (war exhausts a
  settlement permanently).
- **R-VARIETY:** where to raise, how many, how to arm, where to gather, who commands, and (player or
  hand-built) each subunit's role. In computed play: where, how many, arming and who commands. **PASS
  on the shape; NOT SCORABLE** until TS-8.
- **R-CHOICE:** a raise costs the pool and its regrowth seasons, and food every season the levy
  stands. It buys mobility, not home defence (§4.1). The cost the first correction found missing
  (upkeep per man) does not arise under A: the cost scales with men, through the larder.
- **R-WORLD:** a settlement raised dry is a weakness neighbours learn through `stores.changed`; a
  starving levy shrinks without anybody deciding it; a lord who defects with his towns takes their
  men; a town nobody raised still fights at its walls. **Lost against P:** a levy that chooses to
  desert, witnesses its lord's orders, or nurses a grudge. **PASS on the shape**, narrower than P's.

### 8.3 S — six directions, pause, methodology

| direction | carried by | verdict |
|---|---|---|
| **S-UP** | a threat reaches the seat as a claim; whether the holder conscripts is his choice (TS-7) | **PASS on the shape**, gated on TS-7 |
| **S-DOWN** | none under A: a stock is no party | **N-A under A** (P carried it) |
| **vertical** | `recruits` → stock → `troops = count × men_per_weight` → survivors back to the stock; one conversion | **PASS** |
| **diagonal** (SE matter → MB field) | `requisition` → `transfer` → `kind_for_kit` → `of_type`; computed-reachable | **PASS on the shape** |
| **lateral** | `conscript` and `requisition` share the typed cell conjunct for conjunct and the keyed-refusal split | **PASS** |
| **horizontal** | one `mustered`, one `fielded`, one `order_of_battle`, one `build_army` for both sides | **PASS, one residual:** the attacker's faction is read off the seat's label, `fielded` off the holder (§4.1) |
| **pauses correctly** | the field resolves inside the fold, as today | **N-A** |
| **methodology** | **One draw for every mouth** (cohorts, then stocks); **one rounding rule**; **two replenishing clocks**, yield (no ceiling) and the pool (a ceiling), the same write with a different bound, stated. **Fixed here:** `SUBSIST` and `subsistence_draw` disagreed about what is food. **Still open:** an individual's casualty is `int(body × float)` (`effects_combat.py:254`) [CHECKED], routed to per-mille at TS-6 | **FINDINGS → TS-3, TS-6** |

### 8.4 E — last, as a ratio

- **N and R found** a pool, a stock, a verb, a feeding rule and a defence rule that hold; one failure
  in computed play (the grade); one narrowed R-WORLD against P.
- **Count:** 35 added against 5 cut on disk under A; about 38 under P (part 1, §3.5).
- **E-OVERHEAD: NARROWED.** Every addition carries a fact the engine reads or a reader of one, and
  none is a parallel scheme, but additions outnumber cuts seven to one.
- **E-LEGIBILITY: PASS on the shape.** A player sees men raised from a town's pool, the pool refilling,
  the levy armed from the town's stores, gathered, led, killed or starved, and a raised-dry town left
  open. Each outcome traces to one act or one clock.

### 8.5 The design's own falsifier

**No fighting man exists unless he is in a pool, and none vanishes without a receipt.** Named persons
fight without being in a pool: they command and are not men (part 1, §2.6). Guard cohorts and
convicts in service field nothing under A (no person fields men), so the first correction's
borderline cases close.

### 8.6 Self-audit

- **Backward propagation:** part 1 §0 carries the A default, the Layer 1 line, the defence walk and
  the `SUBSIST` defect; §3.5 recounts; §5 marks H-49 untouched; §6 drops `conscript_amount`; §9 states
  J-1 as an overwrite of ratified canon.
- **What an independent reviewer would add:** a run of the feeding rule's plateau (TS-11 (ii)) and of
  the defending pool's effect on how often a march succeeds. Neither was run.

---

## 9. DECISIONS FOR JORDAN

**CLAUDE.md §0's ladder, per item.** Only what survives all five steps is escalated.

| id | the decision | ladder | escalated? |
|---|---|---|---|
| **J-1** | the troop body under the pool | not superseded; not irrelevant; no document decides it; no precedent fits; architecture favours A on the ruled-constraint count (part 1, §2.4), **but A overwrites ratified Layer 1 (`04:793`)** and P overturns or narrows a ruling (ED-WR-0011) | **yes** — every option overwrites ratified canon or a ruling |
| **J-2** | does raising draw down the population | step 1, superseded by R-POOL | **no — ANSWERED** |
| **J-3** | the two verbs' names | a name is Jordan's (the brief reserves it) | **yes** |
| **J-4** | do LF-1..LF-3 stand | step 5: under A a levy eats through the one draw; a treasury ration would double it | **no — folded into J-1** |
| **J-5** | what a fought field writes beyond casualties, morale and grudge | it overturns ED-IN-0279's ruled row if anything changes | **yes** |
| **J-6** | who counts as troops | step 4, precedent `24f` | **no — answered: stocks and the defending pool; no person** |
| **J-7** | the service term | under A there is none; under P, step 5: reuse `oblige_term` | **no — moot under A** |
| — | the ceiling base, the regrowth form, the pool-holding rung kinds | step 5 (part 1, §2.2, §2.3) | **no — answered in text** |
| — | the pool defends its own settlement | step 5 (§4.1); overwrites nothing: ED-IN-0279 (a)'s `Unopposed` survives for an empty side | **no — answered, Jordan-vetoable** |
| — | the levy eats after the people | step 5 plus R-POOL under scarcity (part 1, §2.5) | **no — answered** |

**The escalated decisions:**

| id | the decision | options, and what each does to the game | default here | what waits on it |
|---|---|---|---|---|
| **J-1** | **what a troop is, once raised from the pool** | **(A) a troop stock on the settlement rung** (default): armies are counts that eat where they stand, fight for whoever holds their walls, and are moved by `transfer`. **Amends `04:793`**, Layer 1's unit sentence, to admit a counted stock beside the persons who stand and command (part 1, §0 item 4); the muster lines and `claimants : PersonId[]` stand. Also amends the code rule "only a cohort eats" (`24f`) to "cohorts, then troop stocks", within ED-IN-0255's words. A levy cannot choose, witness or hold a grudge. · **(P) a company `Person`** minted from the pool: armies are people who deliberate, desert, witness and die. **Narrows or overturns ED-WR-0011** as the code applies it to cohorts (`world_q.py:824`; H-170), on X-4's contrary reading (`00_COMPARATIVE_ANALYSIS.md:204`) [CHECKED] and CENSUS's individuation precedent; **amends `04:792`/`:802`**; and needs P′'s no-`reside` form (RR-2), a dissolution rule J-16 can accept, and the draw-order rule (§4.8). · **(B) a typed troop row:** amends `04:793` and T-l (`04:123`). **Under A, three consequences ride with it:** no stand-down verb (a seat cannot send men home; add a `conscript` inverse only if asked); kit stays with the town (a lost field kills men, not swords); the pool defends its settlement (§4.1) | **A** | everything in §7 from TS-4 on |
| **J-3** | **the names** | **The store act:** `requisition` (provisional, in the tree) · `tax` · `tithe`. **The troop verb:** `conscript` (working name). Its absence claim is corrected: `git grep -i conscript` over `engine modules systems references tools` returns nothing [RAN], but `git grep` skips an ignored file, and `systems/_architecture/_identifier_census.yaml:601` (ignored by `.gitignore:46`, untracked) [CHECKED] lists `conscription` as a purpose string of the retired key-type registry: no live collision, but not "no hit". · **`levy`**, Jordan's own word, collides with: R-04's acceptance text and store-act refusal counts (`requirements.yaml:734-735`, `:771-772`) [CHECKED-1]; IN-49's EXIT (`_part5.md:215`) [CHECKED-1]; 19 `hole_register.yaml` hits [RAN, first correction]; the r2 note "ruled deleted (§A.20)" (`world_q.py:910-914`) [CHECKED-1]; the module's `levy` troop type (`registry.py:41`; `equipment/__init__.py:22`) [CHECKED-1]; **and a roster the code reads already uses it in the military sense:** "Lions' Table: Military coordination, levy operations, Royal Guard." (`rosters.yaml:1582`) [CHECKED]. Choosing `levy` makes TS-L land before TS-4 | **`requisition`; `conscript`** | IN-49's text; TS-4's row; TS-L |
| **J-5** | **what a fought field writes** (ED-IN-0279: losses only, nothing on the winner) | **(a) as ruled.** · **(b)** winners take their engine casualties too. · **(c)** survivors of both sides move one grade up: the only computed producer of experience while J-13 (iii) stands. · (d), veterans persisting, is moot under A: a grade stock persists until killed or starved | **(a)** until ruled. **Recommended: (b) + (c)** | TS-6's write set; TS-10; M-MB-16 |

**Tuning values, not decisions:** `recruit_share`, `recruit_regrowth`, `men_per_weight`, the equipment
kinds, the `troop_grades` ladder, the arms producer, and which grade a shared kit equips first. Each
is **[OPEN — Jordan tuning]** with a register row and a sweep at its position.

---

## 10. LIMITS

**Re-opened in the second correction pass (`[CHECKED]`):**
- **Season code:** `data/requires.py:205-220`, `:280-310`; `rosters.yaml:1371-1392`, `:1580-1584`,
  `:1840-1852`; `decision/options.py:372-392`, `:630-651`, `:755-770`, `:840-880`;
  `data/fixtures.py:485-495`; `state/carriers.py:40-75`, `:105-118`; `loop/effects_economy.py:250-312`;
  `hole_register.yaml` (H-156 `:3540-3543`, H-163 `:3631-3643`, H-170 `:3722-3725`, H-173
  `:3762-3775`, and the row index `:3540-3978`); `queries/world_q.py:818-830`, `:850-900`,
  `:990-1002`, `:1044-1078`, `:1441-1450`; `harness/populated.py:398-434`, `:1515-1538`;
  `harness/probes.py:125-152`; `loop/deliberate.py` (grep for `subsistence`); `loop/matter.py:104-123`,
  `:478-540`; `loop/sides.py:60-100`, `:116`; `seam/wrappers/mass_battle.py:215-250`;
  `loop/effects_combat.py:225-262`; `loop/census.py:60-112`; `state/world.py:788-806`;
  `state/containment.py:33-37`; `verb_table.yaml:629-652`; `modules/mass_battle/massbattle.py`
  (grep for `fort_level|walls_dr`: `:233-273`, `:342-371`).
- **Ledgers and research:** `registers/editorial_ledger_wr_archive.jsonl:13-14`;
  `research/by_lane/00_COMPARATIVE_ANALYSIS.md:200-206`; `research/by_lane/MB_mass_battle.md:434`.
- **Architecture:** `04_CODE_ARCHITECTURE.md:118-126`, `:176-181`, `:772-805`.
- **Other:** `systems/_architecture/_identifier_census.yaml:599-603`; `.gitignore:46` via
  `git check-ignore -v`.

**Ran in the second correction pass** (from `/home/user/ttrpg`):
- `git status --short` at the start → three modified `proposals/2026-10-16-character-template*.md`
  files, not this design's (committed during the pass as `74b557e`, as was an intermediate state of
  part 1 as `54012ec`; neither commit was this pass's).
- `python <scratchpad>/probe_subsist.py` on `build_realm(0)`: cohort `cohort_set_s_001`, stores `{}` at
  build; `SUBSIST` shipped 0, with `recruits: 2` 1000; with the larder set to `grain: 1`, 500, and with
  `recruits: 2` added, 1000; empty 0, with `recruits: 2` 1000. A minted id
  `H(seed, tick, "p_npc_001", "conscript:set_s_001:a1")` = `3b5fbcbdce6ac4cc` sorts before
  `cohort_set_s_001`: True.
- `python <scratchpad>/probe_subsist2.py`: at build, 37 cohorts, `SUBSIST` min/max 0/0, with
  `recruits: 2` at each cohort's rung 1000/1000, moved for 37; after one season through
  `populated.run`, 1000/1000 both ways, moved for 0.
- `sed -n 3631,3643p hole_register.yaml | grep -o levy | wc -l` → 16 (H-163); the same over H-156's
  rows → 6.
- `git grep -n -i conscript -- engine modules systems references tools` → no output;
  `grep -rn -i conscript` over the same trees with `--include=*.yaml --include=*.py` → the one hit at
  `_identifier_census.yaml:601`; `git check-ignore -v` → `.gitignore:46`.

**Could not check:**
- **Whether a regrowth `stores.changed` deposits a `stores:recruits` claim** that TS-7's question can
  be about (part 1, §3.1) — **[INFERRED]**.
- **Which seats' `treasury_of` is a settlement**, so whether computed assembly by `transfer` can start
  from a levy's rung (part 1, §3.2).
- **Where MATTER's dearth step reads the draw** for the body write, which the stock debit would sit
  beside (part 1, §2.5).
- **The golden scope of the `SUBSIST` edit** (TS-3 measures it).
- **That `march` is folded at ENC** (read from the matrix comment, not traced).
- **Which harness batteries TS-2 moves** (`bat.py` not opened).
- **The MB lane's scale probe** (≈120 troops; 0 of 20 at ≤ 80), cited and not re-run.
- **The drafting probes P1–P3** and the first correction's probes were not re-run.
- **`CURRENT.md` and `HANDOFF_MB.md`** were not read.
- **PP and ED provenance** other than ED-WR-0011 and H-173's J-16 note (ED-IN-0279, ED-IN-0255,
  ED-SE-0051, ED-MB-0067, ED-1090) was not verified against the ledgers.
- **R-POOL** is quoted as the coordinator relayed it.
- **The `.audit/` and `.designs/` trees** were not read.

---

## CRITIC RECONCILIATION (first critic, 18 findings, against the draft)

Kept as recorded at the first correction. Where the second correction's switch to A removed a
finding's object, the last column says so.

| # | finding | verdict at the first correction | status under A |
|---|---|---|---|
| 1 | weight-2 cohorts: a split of 1 yields two non-cohorts | applied, then superseded by R-POOL | moot: a stock of 1 is valid |
| 2 | `mustered` pulls in vassals of other factions | applied (`service_faction` excludes `commit` holders) [RAN] | moot: the muster is unchanged; kept for P (§4.8) |
| 3 | the morale reader cannot see companies | applied (`faction_holding or service_faction`) | moot: no company; the reader is unchanged |
| 4 | experience via `train` excludes case-less persons | applied; TS-10 blocked | stands: no computed grade producer |
| 5 | equipment unreachable; a second loadout table | applied (`kind_for_kit` beside `TROOP_LOADOUT`) | stands, and equipment becomes computed-reachable |
| 6 | reusing `levy` collides with three registers | applied (`conscript`; J-3; TS-L) | stands; J-3 now also cites `rosters.yaml:1582` |
| 7 | grouping merges a lord's companies; demand (3) overstated | applied (one subunit per company) | re-cast: one subunit per grade × kind, splittable by `order` |
| 8 | Command constant 4; `COMMAND_SIGMA_ENABLED` | applied | stands |
| 9 | the §0 ladder misapplied to J-4, J-6, J-7 | applied | stands |
| 10 | `order` is a ninth operand | applied (`confer`'s `term`) | stands |
| 11 | statement 1's contrary reading not cited | applied | stands; A meets it in full |
| 12 | upkeep per person; the witness channel | applied (stated, not fixed) | moot under A; P's upkeep claim corrected (§4.8) |
| 13 | `remove_person` pops the person-rung, so kit is destroyed | applied (salvage clause) | moot: kit is the town's |
| 14 | the row's `writes` omits `Tenure.term` | applied | moot: no Tenure is written |
| 15 | falsifiers blind at scale 1 | applied (`men_per_weight = 250`) | stands |
| 16 | NPC5: a defecting lord leaves his men behind | applied (holder's faction) | stands, through `fielded`'s holder read |
| 17 | the meta-rule net undercounted | applied (22 vs 6) | superseded by the second critic's finding 13 |
| 18 | 22 files, not 44; `carriers.py:928` | applied | stands |
| — | the morale-preset defect, untracked | applied (TS-2) | stands |

---

## SECOND CRITIC RECONCILIATION (13 findings + an observation, against the first correction)

Each locator was re-opened before any text changed (§10). "Applied" means the finding reproduced and
the text now says what the code does.

| # | finding | verdict | where |
|---|---|---|---|
| 1 | the typed cell cannot name `recruits`; computed `kind` is `grain`; no "pool short" decline | **applied.** Reproduced (`requires.py:303-307`; `options.py:846-875`; `fixtures.py:491`). The effect declines `kind != recruits` and a short pool; TS-7's referent is a `stores:recruits` claim. Also found: the chain's `amount` is `default_transfer_amount` (1), so the first correction's `conscript_amount` was dead; withdrawn | part 1 §1.4 items 15–16, §3.1; part 2 §6, TS-4 (iii), TS-7 |
| 2 | `is_company` reads `Term.declared_by`, which renewal overwrites; J-16 forbids a branch on origin | **applied.** Reproduced (`carriers.py:50-51`; `effects_economy.py:309`; `hole_register.yaml:3772`). Under A there is no company. Under P `is_company` is withdrawn for a state-keyed rule J-16 must accept | part 1 §1.5 item 23, §2.4; part 2 §4.8 |
| 3 | a computed army does not "last one term": TS-7's obliges become renewable | **applied.** The docstring's missing piece is exactly "no computed act forms an `oblige`" (`effects_economy.py:283-290`); the claim is withdrawn and restated for P | part 2 §4.8 |
| 4 | ED-WR-0011 never cited; it weighs toward a body that mints nobody | **applied, and decisive.** Reproduced (`wr_archive.jsonl:13-14`; `world_q.py:824`; H-170). **The default moved from P to A.** Narrowed in one respect: CENSUS already mints a weight-1 person at run time (`census.py:105-112`), so ED-WR-0011 is not absolute in the code; but the code applies it to cohorts by name, and X-4's contrary reading frees a weight, not a cohort `Person` | part 1 §0 item 2, §1.5 item 21, §2.4; part 2 J-1 |
| 5 | capacity bypassed by fiat; eating reads `contain`, not `reside` | **applied.** Reproduced (`world_q.py:1050-1051`, `:856`; `populated.py:401-432`). Moot under A (no resident minted); P′ drops `reside` | part 1 §1.5 item 22, §2.4; part 2 §4.8 |
| 6 | men are sensed as food; draw order puts a company first; R-POOL unshown under scarcity | **applied, and sharper than reported.** [RAN]: the pool fill flips every cohort's `SUBSIST` from 0 to 1000 **at build**, not only under dearth; saturated after one season. `SUBSIST` reads only weighted kinds; levies draw after persons; TS-3 (vii) and TS-11 (i) are the scarcity falsifiers | part 1 §0 item 10, §1.4 items 19–20, §2.5; part 2 TS-3, TS-11 |
| 7 | which rungs hold a pool; regrowth skipped by `if not produced: continue` | **applied.** `pool_rung_kinds: [settlement]`; regrowth in its own pass after the yield loop; falsifiers (iii), (iv) | part 1 §0 item 1, §2.2, §2.3; part 2 §6, TS-3 |
| 8 | defence inverted: no company → `Unopposed`; walls never engage | **applied.** The extreme is walked in a table; the default is that the pool defends its own settlement (ladder step 5, Jordan-vetoable); `Unopposed` survives for a side with nobody in it | part 1 §0 item 7; part 2 §4.1, TS-5, §9 |
| 9 | the case against E applied equally to S | **applied.** E is now declined on `04:179`, its meaning and its shape, not on "twice" | part 1 §2.1 |
| 10 | the cell was not `requisition`'s "conjunct for conjunct" | **applied by making it so:** the `existence` conjunct is dropped and the conjuncts carry `requisition`'s names; the eligibility difference (`remit:dispatch`, no `presence:<rung>`) is stated with its reason | part 1 §3.1 |
| 11 | `hole_register.yaml:3543` is H-156, not H-163 | **applied.** The crowding shape is cited as H-156 (`:3540`, `:3543`); H-163 at `:3631` | part 2 §5, TS-4 (iv) |
| 12 | the `conscript` absence claim is false; J-3 omits `rosters.yaml:1582` | **narrowed, then applied.** The `git grep` was true as run (no output [RAN]): the hit is in an ignored, untracked file (`.gitignore:46`), the retired key-type registry. The claim is restated with its scope; `rosters.yaml:1582` "levy operations" is cited in J-3 | part 2 J-3 |
| 13 | the object count omitted event kinds, edits, constants, result keys, hole rows; "6 cut" padded | **applied.** Recounted for A (35 added, 5 cut) and for P (about 38) | part 1 §3.5; part 2 §8.4 |
| obs. | `_rehome`'s safety rests on "nothing in `loop/` or an effect constructs a Person"; already stale (`census.py:105`) | **applied for P, moot for A.** Reproduced (`matter.py:108-121`; `world.py:792-805`; `census.py:105-112`). A constructs no `Person`. Under P: construct before tenures and correct both comments. The stale comments themselves are outside this design's lane and are not edited here | part 1 §2.4; part 2 §4.8 |

**Rebutted:** none outright. **Narrowed:** finding 4 (CENSUS's run-time individuation exists; ED-WR-0011
still binds cohorts as the code reads it); finding 12 (true as a `git grep`, false as a tree-wide
absence).
