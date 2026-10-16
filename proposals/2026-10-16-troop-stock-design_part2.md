# The troop stock — part 2: the seam, the cuts, the data, the build, the NERS pass, the decisions

## Status: PROPOSED (2026-10-16), corrected three times the same day and re-based on R-POOL. Default troop body: **A, a troop stock**. Not ratified; merge ratifies nothing unless Jordan so rules.
## Part 2 of 2. Head, verdict, R-POOL and §1–§3: [`2026-10-16-troop-stock-design.md`](2026-10-16-troop-stock-design.md). Locator conventions as there (`[CHECKED]` = re-opened in the third correction pass; `[CHECKED-2]` = the second pass only; `[CHECKED-1]` = the first pass only; `[CHECKED-draft]` = drafting only; `[RAN]`, `[INFERRED]`, `[UNVERIFIED]`).

---

## 4. ARMY ASSEMBLY AND THE SEAM

### 4.1 Who stands on a side, what they field, and who defends

**Who stands is unchanged.** `mustered(w, rung, faction)` returns faction members present in the
rung's subtree (`world_q.py:1256-1272`) [CHECKED], for the attacker at the origin
(`loop/sides.py:79-85`) [CHECKED] and for the defender at the target (`seam/wrappers/mass_battle.py:233`)
[CHECKED]. They command; they field no men (part 1, §2.6). Layer 1's muster lines (`04:792`) stand;
the squad parallel (`04:802`) is amended (part 1, §2.4).

**What a side fields is new: one Query, `fielded(w, rung, faction)`** (in `queries/world_q.py`). It
returns the troop stocks (`troops_<grade>` kinds) in `rung`'s own `stores`, **if**
`holder_faction_of(w, rung) == faction` (`world_q.py:1441-1450`) [CHECKED-2], else none. A levy fights
for whoever holds the walls it stands in.

**The origin, re-derived, not passed** (third critic, finding 2). The wrapper never sees the origin
(`mass_battle.py:154-155`) [CHECKED]; `sides_of` computes it at `sides.py:82-84` and drops it [CHECKED].
Three readers need it: `fielded` at the origin, `order_of_battle`, and `_eff_march`'s casualty write on
the origin's stocks. Two routes:
- **(R) Re-derive it from the claimants' homes — CHOSEN**, on `_origin_of`'s precedent
  (`mass_battle.py:151-172`) [CHECKED], which re-derives the origin *territory* the same way.
  - **One owner:** `sides.py:82-84`'s inline "nearest settlement up the ancestry" becomes a Query,
    `settlement_above(w, rung)`.
  - **Two callers:** `sides_of` calls it on the actor's home, as today. The wrapper calls it on each
    claimant's home. The origin is the one settlement they all name, else `None`.
  - **They agree on the season path by construction:** `sides_of` musters the claimants in the
    origin's subtree, so every claimant's home is under it.
  - **The wrapper returns it** in its result's `parties` (beside `claimants` and `subject_members`,
    `mass_battle.py:234`) [CHECKED], so `_eff_march` reads it there and does not derive it a third
    time.
  - **Cost:** one extracted Query, one `sides_of` edit, one wrapper helper. `04:765` stands.
  - **Failure mode:** a caller handing claimants from several settlements gets no origin, so its
    side fields no men and is refused. Only `march` is `mass_battle`-routed (`sides.py:107-109`)
    [CHECKED], and `sides_of` never builds such a side.
- **(S) A seam parameter `origin`.** It amends `contest(proj, place, prize, claimants, depth,
  max_depth)` (`04:765`) [CHECKED], a seventh Layer 1 line, and every provider's signature, for a
  value the claimants already carry. **Declined.**

**Whose men the attacker fields.** Let `H = holder_faction_of(w, origin)`. The attacker fields
`fielded(w, origin, H)` **only if every claimant is a member of `H`** (`world_q.members`, the one
owner). Otherwise it fields no men.
- **This closes the second correction's "two readings of whose side" residual.** The claimants were
  mustered under the seat's label (`sides.py:79-80`) [CHECKED]. A defected holder marching through his
  old seat musters his old faction, which does not hold the origin, so he takes no men.

**The attacker with no men is a new branch, not PARTY-GAP** (third critic, finding 2). `if not
claimants:` (`mass_battle.py:224-226`) [CHECKED] tests persons. An origin with members present and no
stock passes it, and `_MIN_TROOPS`, which section 3.5 deletes, exists because zero troops "divides by
zero" (`massbattle.py:208-210`) [CHECKED].
- **The new branch,** after the `rung` check: no origin, or the attacker fields no men → return the
  PARTY-GAP-shaped refusal `why="the attacking side fields no men"`.
- **The fold turns that shape into `march.refused`:** `sides.py:99-101` [CHECKED] names "`_contest`'s
  PARTY-GAP catch (M4) refuses it gracefully". That `_contest` does so is read from that comment,
  **not traced** in `loop/resolve.py` **[UNVERIFIED]**.
- **TS-8 stands on this branch:** with no computed levy, every march is refused here, and the realm
  stops attacking.

**Who defends: composed on the garrison Site** (third critic, finding 4). Jordan ruled what garrison
strength is: the garrison Site's `condition`, "Jordan's choice over a cohort-Person alternative"
(`world_q.py:1275-1278`; `harness/populated.py:799-804`) [CHECKED]. The second correction made the
target's `recruits` pool defend. That was a second carrier of standing defence made of the population's
men, close to the alternative Jordan rejected, and it never weighed the garrison. It is withdrawn. The
defender fields:
- **`fielded(w, target, subject)`**, the holder's levies stationed there. `subject` is
  `holder_faction_of(w, target)` already (`sides.py:115-116`) [CHECKED], so the holder test passes by
  construction;
- **the garrison:** `garrison_troops = (c × garrison_men + 500) // 1000`, where `c` is the mean
  garrison `condition` in the target's subtree on `condition_scale` (per-mille), read through the
  same Sites `fortification_of` reads (`world_q.py:1291-1296`) [CHECKED]. The garrison's men are grade
  0, equipped from the target's kit after the stocks.
  - **⚠ This extends the ruling's reading, and says so.** Today `condition` is read only as the walls
    (`fort_level` → WALLS). Here it is also read as men. One quantity, garrison strength, has two
    effects. Jordan ruled what the strength *is*, not that it may only be walls. **[ASSUMPTION;
    medium; Jordan to correct]**.

**Who stands for the defence** stays Jordan's ruled reading: members present
(`world_q.py:1257-1259`) [CHECKED]. **A defending side with no member present is `Unopposed`, as
today.** A levy or a garrison with nobody of the holder's faction there does not hold the town.

**The defence table, walked honestly row by row** (third critic, finding 4: the second correction's
row 2 hid that today is already `Unopposed` there):

| at the target | today | **under A (this design)** | changed? |
|---|---|---|---|
| members present, no levy, garrison `condition` > 0 | members fight at their summed weight (1 each); "one present defender holds any settlement" (`MB_mass_battle.md:434`) [CHECKED-2]; WALLS at any positive condition | the garrison fights under the members; WALLS and `walls_dr` engage as today | **yes:** the men are the garrison's, sized by its condition, not the members' weight |
| members present, a levy, garrison > 0 | as above | the levy and the garrison fight under the members | yes: the levy adds men |
| members present, no levy, garrison worn to 0 | members fight at their weight; no WALLS (a garrison at 0 "is no wall", `populated.py:808-809`) [CHECKED] | **`Unopposed`:** the side has persons and no men. The widened test is "no member present, **or** no men" | **yes, inverted:** a town whose garrison is worn out and holds no levy falls to any levy |
| no members present, a levy and/or a garrison | `Unopposed` (`mass_battle.py:235-248`) [CHECKED] | **`Unopposed`** | **no.** ED-IN-0279 (a)'s branch and Jordan's "present at the target" both kept |
| an unheld settlement (`subject` is `None`) | PARTY-GAP (`mass_battle.py:227-229`) [CHECKED] | same | no |

**What raising then changes at home:** nothing in the town's defence while the levy stays and a member
is present. The levy adds men beside the garrison. A raise buys mobility, because only a stock can be
moved or march, and costs food, because only a stock eats separately.

**Morale is weighted by the men each commander leads** (third critic, finding 10). `_side_stance`'s
stated reason for weighting by `Person.weight` is "because `resolve_field` sizes the side by the same
weights" (`mass_battle.py:136-137`) [CHECKED]. Under A the side is sized by stocks and garrison, so
keeping `Person.weight` would size one way and weigh morale another, an S defect in methodology.
- **The edit:** `_side_stance(w, pids, referent, men)` weighs each person's stance by the men
  `order_of_battle` assigns to him (step 5 below). The general carries the remainder, the garrison
  included. The side's morale is `Σ stance_i × men_i / Σ men_i`.
- **A side with men always has a person**, because a side with no member present is `Unopposed`. So
  no fought side reads the empty-side 0.
- **The loyalty row** (`_creed_referent`, `:199`) [CHECKED] takes the same weights.
- **The morale and grudge rows** `_eff_march` writes still land on the persons
  (`effects_combat.py:248-261`) [CHECKED] and are read back at their next field.

### 4.2 What a side is: an order of battle

`field_input` stops passing `weights`. `MassBattleInput` (`queries/inputs.py:62-100`) [CHECKED-draft]
trades `weights` for `sides`:

```
sides  = (OrderOfBattle_attacker, OrderOfBattle_defender)
OrderOfBattle = ( general:  (name, command),
                  officers: ((name, command, men_led), …),               -- sorted by name
                  stocks:   ((grade_id, count, grade_offsets), …),       -- sorted by grade, highest first
                  garrison: count,                                        -- 0 for the attacker
                  kit:      ((matter_kind, units), …),                    -- the rung's kit stores, sorted
                  order:    ((grade_id, kind|None, role|shape, count|None), …) )   -- from `march`'s `order`
```

This is a per-side composition record. It crosses the seam as `MassBattleInput` does today: frozen,
built from the projection, never stored in `World`. Part 1 §2.4's amended `04:793` says so, and
`massbattle.py:321-323`'s "no `Unit`/`Faction`-shaped object crosses this boundary" [CHECKED] is
edited with it.

**How the host fills one side** (`order_of_battle(w, side)`, in the host wrapper):
1. **The stocks** are `fielded`'s (§4.1), as `(grade, count)`; on defence, plus `garrison_troops`.
   `troops = count × men_per_weight` is applied by the module at build, once (part 1, §2.8).
2. **The kit** is the field rung's stores of equipment kinds. The module splits each stock by kit with
   `kind_for_kit` (part 1, §2.7), highest grade first, the garrison last.
3. **Subunits:** one per `(grade, derived kind)` pair with men, unless the march's `order` splits one
   by count (§4.3).
4. **The general:**
   - **attacking side:** the marching actor if he is among the claimants, else the first claimant by
     id;
   - **defending side:** the holder of the seat holding the target if present, else the defending
     faction's leader present (`leaders`, `world_q.py:1165`) [CHECKED-1], else the first member
     present by id.
   - Every fought side has a member present, so the second correction's "no general" case is gone.
5. **Officers** are the side's other named members present, sorted by id. Subunits, in the order of
   step 3, go to officers in id order, each up to his Command, and the general takes the rest up to
   his. `men_led` is what each commands, and it feeds `_side_stance` (§4.1). **[ASSUMPTION; medium; MB
   to correct]**: no document assigns subunits to officers.
6. **Command before R-C-1:** every season commander's Command is the constant 4, because the season
   supplies neither charisma nor cognition (`hierarchy/units.py:2711-2716`; `config.py:530`)
   [CHECKED-1]. What varies is who commands and so how the span check divides a side.
7. **Span of control** has one owner, `trim_to_command` beside `build_army` (§4.4).

### 4.3 What `march` carries

- **Unchanged:** `subject`, the Rung marched on, the row's typed cell, `contests:` and eligibility.
- **Widened:** the degree-keyed `writes` (§4.6).
- **Added: one act-declared payload key, `order`,** mapping `(grade, kind)` to a role or shape, with an
  optional count that splits a stock into two subunits (demand 3's subformations).
- **A ninth operand, admitted by precedent:** `confer`'s act-declared `term`, "in no operand of the
  closed eight" (`verb_table.yaml:177`) [CHECKED-1]. Read only by the host; absent on every computed
  act. **[ASSUMPTION; medium; Jordan to correct]**.
- **Demand (3) is met for the player and the hand-built act only.** An AI planner choosing roles is
  MB-08's "AI generals", LEAVE (`_part7.md:26-31`) [CHECKED-draft].
- **Gating:** `role_allowed(kind, role)` (`registry.py:22-24`) [CHECKED-draft]; a refused role becomes
  the PARTY-GAP-shaped refusal, as the no-men branch does (§4.1).
- **Defaults** live in the module (`TROOP_TYPE_ROLES`, `ROLE_SPEC`, `config.py:582-616`)
  [CHECKED-draft]. The `levy` kind falls back to `"any": ["Support", "Reserve"]` (`:592`), so an
  unarmed subunit defaults to `shape: Line` with no role. Whether raw levies get a front-line menu is
  MB data **[OPEN]**.

### 4.4 Where the army builder lives

1. **Move** `build_army`, `_centered_line_cols` and `SUBUNIT_CAP` from
   `systems/mass_battle/sim/engine.py:99-173, :213-452` into `modules/mass_battle/army.py`, leaving a
   re-export so the 22 `tests/valoria` callers are untouched [RAN at the first correction]. Per K-MB-2
   (`MB_mass_battle.md:716`) [CHECKED-draft].
2. **The morale defect is TS-2**, gated on nothing (part 1, §0 item 8).
3. **`resolve_field` builds each side with `build_army`**, one spec per subunit: `{troop_type: kind,
   troops, role|shape, officer, discipline, morale}`, discipline and morale being the kind's preset
   (`stats_for`) plus the grade offset.
4. **`trim_to_command(specs, officers, command)`** drops the subunits a commander cannot hold,
   smallest troops first, then by key, and returns them as `unfielded`. `build_army` calls it first,
   so the check and the trim are one rule in one file. A drafting probe (P2) showed an over-spanned
   side raising `ValueError` inside the fold.
5. **Whether `run_battle` fights a multi-subunit `Unit` on the season's terrain rows** is
   **[UNVERIFIED]**. TS-5 (b)'s EXIT shows it.

### 4.5 What happens to the stub, to `Person.weight` as input, and to the 4/4 constants

| object | fate |
|---|---|
| `_MVP_SUBUNIT_SHAPE`, `_MVP_UNIT_COMMAND`, `_SEASON_FORCE_POWER`, `_MIN_TROOPS` (`massbattle.py:170-210`) | **deleted** at TS-9 |
| `_weighted_unit` (`:213-230`) [CHECKED] | **deleted** at TS-9 |
| the `[GAP …]` header line (`:32`) | **deleted** |
| `Person.weight` as battle input | **cut.** No person fields men (part 1, §2.6) |
| `_side_stance` (`mass_battle.py:126-148`) | **edited:** weighted by men led, not `Person.weight` (§4.1) |
| `MassBattleInput.weights` | **replaced** by `sides` |
| `massbattle.py:321-323`'s contract sentence | **edited** (§4.2) |

### 4.6 How a field writes back

**Who lost** is read as today (`effects_combat.py:225-227`) [CHECKED].

**On the losing side:**
- **Each fielded stock loses men:** `count ← (count × survivors_permille + 500) // 1000`, at the rung
  it stood on: the origin (read from `parties`, §4.1) for an attacker, the target for a defender. The
  per-mille is the losing side's engine survivor ratio (`attacker_size_pct` / `defender_size_pct`,
  `:227`) [CHECKED].
- **A losing defence wears its garrison:** each garrison Site's `condition` falls by the same
  per-mille. Its men were killed, and its `condition` is what their strength is. **[ASSUMPTION;
  medium; Jordan to correct]** that this is "casualties", the only loss ED-IN-0279's ruling admits.
- **`field_casualty_model`** (`rosters.yaml:861`) [CHECKED-2] keeps its meaning: `total` → every losing
  stock and garrison to 0; `none` → nothing written; `scaled_by_degree` → the per-mille rule.
- **Each named person** gets today's body write and stance rows, unchanged (`:248-261`) [CHECKED].
- **⚠ The early return must go.** `_eff_march` returns `NO_CHANGE` when no loser is a person
  (`:228-230`) [CHECKED]. It becomes "no losing person **and** no losing stock **and** no garrison".

**The row and the matrix** (third critic, finding 5):
- **The `march` row declares only `Person.body` and `Person.stance`** under `Won` and `Lost`
  (`verb_table.yaml:677-681`) [CHECKED]. The fold gates exactly those pairs (`loop/resolve.py:442`)
  [CHECKED], and the effect runs once, on the first pair (`:462-467`) [CHECKED].
  - **The edit:** `Won` (the defenders lost) gains `Rung.stores` and `Site.condition`. `Lost` (the
    attacker lost) gains `Rung.stores`. The row is graded `ruled` (`:689`) [CHECKED], so this is J-1's
    widening of a ruled declaration (part 1, §2.4).
  - **Whether the gate refuses an effect's write outside the declared pairs** was not traced
    **[UNVERIFIED]**. The design declares them either way.
- **Two matrix rows gain ENC:**
  - `(Rung, stores)`, `[MAT, RES]` today (`write_matrix.yaml:318-324`) [CHECKED];
  - `(Site, condition)`, `[MAT, RES]` today (`:332-338`) [CHECKED].
  - **The precedent** is `(Person, body)`, which gained ENC at M4 because "`march`'s prize row defers
    there" (`:161-163`) [CHECKED]. That ENCOUNTER shares RESOLVE's write class is read from that
    comment, **not traced** in `data/matrix.py` **[UNVERIFIED]**.

**On the winning side: nothing**, per the ruled row (`verb_table.yaml:682`) [CHECKED]. J-5 asks whether
winners take casualties and whether anyone gains experience.

### 4.7 Assembling from several settlements, and the commander drawn from persons

A faction assembles an army in four steps:
1. **Levy** at each settlement in its seats' purviews, as far as each pool allows.
2. **Equip** with `transfer` of arms into those settlements (player and hand-built only; part 1, §3.2).
3. **Gather** with `transfer` of the troop kinds to one settlement its faction holds (`placeable`
   refuses any non-settlement destination).
4. **March** from there.

**What computed play reaches** [INFERRED from part 1, §1.4 items 16–19, and §3.2]: step 1, once TS-7
lands, and step 4. Steps 2 and 3 have no computed referent producer, so a computed army is the levy
of the one settlement its general marches from.

**NPC5's need** (`engine/season/cases/NPC5.yaml:172`) [CHECKED-1]: a council commander's break with
his leader should have "a material consequence beyond a changed vote". Under A, a lord who defects and
keeps the settlements he holds takes their levies with him, because `fielded` reads the holder. If he
loses a settlement, its levy serves the next holder. A levy he sent into another faction's town serves
that town's holder: a risk of gathering in an ally's walls, named.

### 4.8 If Jordan takes P: the apparatus it needs

Kept so J-1 can be decided against a complete alternative. None of it is built under A. Its tags are
the second correction's and were not re-opened in this pass.
- **The muster amendment:** `service_faction(w, pid)` (the faction of the holder of each seat a
  person with no `commit` serves; `None` for none or many), and `mustered` = members present ∪
  persons present whose `service_faction` is the faction. It amends `04:792`, `03:260` and `10:88`
  (part 1, §2.4). The first correction's probe stands [RAN, first correction]: the two shipped
  `oblige` edges (NPC-070, NPC-041) are both from persons holding a `commit`, so the clause adds
  nobody at build.
- **The morale reader:** `faction_holding(w, pid) or service_faction(w, pid)` in `_side_stance`.
- **The company:** minted by `_eff_levy` at `weight = n ≥ 2`, with its person-rung and `contain`,
  **without `reside`** (P′; RR-2), bound by an `oblige` under a new gate basis. It still eats at the
  muster town, because the draw reads `contain` (`world_q.py:856`) [CHECKED]. Construct the `Person`
  before adding its tenures, and correct the two `_rehome` comments (`matter.py:108-121`;
  `world.py:792-805`) [CHECKED-2].
- **Ending service:** under J-16 [ASSUMPTION; medium], a rule reading state, not origin: "a cohort
  person with no `reside` whose last `oblige` closes dissolves into the `recruits` of the rung it
  stands on, up to the ceiling". The first correction's `is_company` read `Term.declared_by`, which
  `_renewals` overwrites (`effects_economy.py:309`) [CHECKED-2], and is withdrawn.
- **Upkeep:** once a computed `levy` forms an `oblige`, a computed shortfall `transfer` into the
  muster town renews every company present there (`effects_economy.py:257-264`, `:283-305`)
  [CHECKED-2]. Under P a computed army can outlive its term, and upkeep is one person's per company of
  any size.
- **The draw order** (third critic, finding 13): a minted id is 16 hex characters (`state/ids.py:19-21`)
  [CHECKED]. Ids whose first character is `0`–`c` (13 in 16) sort before `cohort_…`, and those
  starting `d`, `e` or `f` (3 in 16) sort after [INFERRED]. The one sampled id sorted before [RAN].
  So which eats first is arbitrary per id, and P needs an explicit "cohorts first" rule either way
  (part 1, §2.5).
- **ED-WR-0011** narrowed by J-1 (part 1, §2.4).

---

## 5. WHAT IT CUTS AND WHAT IT SUPERSEDES

| item | verdict | reason |
|---|---|---|
| **IN-52** "the levy-to-field feed" (`_part4.md:134-140`) | **withdraw** | its premise was the store reading of `levy`, which demand (4) removes; nothing was built [RAN at drafting] |
| **LF-1..LF-3** (a treasury ration bounding troops; its debit at the fold) | **withdraw as forms** | under A a levy eats, through `subsistence_draw`, at the larder where it stands (part 1, §2.5). A treasury ration beside it would be a second ladder for one quantity (§8.3). MB's K-MB-6 bound survives as the larder's |
| `field_provisioning`, `settlements.provision` | **withdraw** (never built) | part 1, §1 |
| **X-19** (`00_COMPARATIVE_ANALYSIS.md:219`) | **resolved** | SE cut the ration bound and MB kept it; under A the bound is the larder, kept, in the one draw |
| **IN-49** (`_part5.md:211-218`) | **keep, re-framed** | the store act's question source. Its EXIT still reads "`levy` row executes" (`:215`) [CHECKED-1]; TS-L re-keys it to `requisition`. The troop verb's question source is TS-7's |
| **H-49** `(Person, weight)` has no runtime writer | **untouched under A** | casualties fall on stocks and the garrison |
| **H-170** the cohort weight | **untouched** | the ceiling reads it; nothing writes it |
| **H-156** (`hole_register.yaml:3540`, its `hole:` at `:3543`) [CHECKED-2] | **the crowding shape** | "mere eligibility crowds `release` out of every scene budget". TS-4 (iv), TS-3 (ix) and TS-7 measure that shape |
| **H-163** (`hole_register.yaml:3631`) [CHECKED for `:3634`, `:3641`] | **re-keyed by TS-L** | its `levy` hits name the store act, including the historical `levy.refused`/`levy.unauthorized` counts |
| **MB-08**'s #445 U-1 (`_part7.md:28`) | **closed by TS-5/TS-8** | kind, grade and commander are the inputs beyond headcount. U-2 and U-6 stay LEAVE |
| **IN-07/SE-02**, **FA-01** | unaffected / depended on | FA-01's seating gives a seat that can levy and march |
| **K-MB-1** (rung stock) | **adopted as the form** | A is K-MB-1's rung-held stock, under the pool |
| **K-SE-13**, **K-FA-13**, **K-IN-13**'s open form | **superseded as forms** | their direction is kept: troops come from settlements, are fielded and drawn down |
| **ED-FA-0010** (conscription costs PS in the levied province) | **not revived** | superseded already; a province value would breach the Rung's NEVER list (part 1, §2.10) |

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
| the recruit pool | `rosters.yaml: matter_kinds`, row `recruits` (`:1279-1290`) [CHECKED-1] | whole weight units in a settlement rung's `stores` | derived: **0 at world-gen**, then regrown toward the ceiling (part 1, §2.3) |
| rungs that hold a pool, and the only rungs a troop kind may stand on | `rosters.yaml: pool_rung_kinds` (new) | closed list of rung kinds | `[settlement]` |
| kinds no store act may move | `rosters.yaml: immovable_kinds` (new); the loader refuses an id not in `matter_kinds` | list | `[recruits]` |
| the ceiling's share | `data/fixtures.py`, `recruit_share`, hole row, sweep | int, per-mille | **[OPEN — Jordan tuning]**. Sweep 500 / 1000 / 2000. Falsifier value **1000** |
| the regrowth rate | fixtures, `recruit_regrowth`, hole row, sweep | int, per-mille of the ceiling per season | **[OPEN — Jordan tuning]**. Sweep **0 (control)** / 250 / 1000. Falsifier value **250** |
| men per weight | fixtures, `men_per_weight`, hole row, sweep | int | **[OPEN — Jordan tuning]**. Sweep 1 (today's scale, control) / 120 / 250. Falsifier value **250** (part 1, §2.8) |
| the garrison's men at full condition | fixtures, `garrison_men`, hole row, sweep | int | **[OPEN — Jordan tuning]**. Sweep 0 (control: walls only) / 120 / 250. Falsifier value **250** |
| the raise size | **no fixture.** The generic chain: a shortfall claim, else `default_transfer_amount` (`options.py:876-877`, shipped 1, H-94) [CHECKED] | — | — |
| grades | `rosters.yaml: troop_grades` (new) | ordered rows `{id, discipline: +d, morale: +m}`, row 0 `{raw, 0, 0}` | **[OPEN — Jordan tuning]**. Proposal: raw 0/0, drilled +1/+1, seasoned +1/+2, veteran +2/+2 |
| troop stock kinds | derived by the loader from `troop_grades`, `troops_<id>` | one `matter_kinds` row per grade | — |
| what is eaten | **reuses** `subsistence_weight` (`rosters.yaml:1371-1387`) [CHECKED] for cohorts, troop stocks **and** `SUBSIST` | — | grain 2, salt 1 (shipped; H-11) |
| kind → stats / kind → kit | **stay** `TROOP_TYPE_STATS` (`registry.py:39-57`) and `TROOP_LOADOUT` (`equipment/__init__.py:21-36`) [CHECKED]; `kind_for_kit`, the one kit → kind derivation, and `UNARMED_KIND` beside the latter | — | `levy` reached two ways is **[OPEN — MB]** (part 1, §2.7) |
| equipment matter kinds | `matter_kinds`, one row per weapon and armour class `TROOP_LOADOUT` names | — | **[OPEN]**: one kind per class or a coarser three. **No producer**: `site_yield` has no arms row (`rosters.yaml:2042-2075`) [CHECKED-1], an existing gap this design does not close |
| survivor conversion scale | **reuses** `condition_scale` (`fixtures.py:182`) [CHECKED-1] | — | 1000 |
| `field_army` | fixtures, temporary arm roster `single_line \| order_of_battle` | — | `single_line` until TS-8; deleted at TS-9 |

---

## 7. BUILD ORDER, EXITS AND FALSIFIERS

Positions use v9's form. Every EXIT is an execution artifact; every FALSIFIER names its control arm.
Golden re-records are declared at the position that causes them. Unless stated, runs fix
`recruit_share = 1000`, `recruit_regrowth = 250`, `men_per_weight = 250` and `garrison_men = 250`.

**Order:** TS-1, TS-2 (independent) → TS-3 → TS-L → TS-4 → TS-11 → TS-5 → TS-12, TS-6 → TS-7 → TS-8 →
TS-9; TS-10 blocked.

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

### TS-3 · the recruit pool, its regrowth claim, placement, and the subsistence formula (R-POOL)
- STATE: unblocked      LANE: SE (IN)
- EDITS: `rosters.yaml` (`recruits`, `immovable_kinds`, `pool_rung_kinds`), `queries/world_q.py`
  (`recruit_ceiling`, `placeable`), `loop/matter.py` (the regrowth pass after the yield loop, with its
  `observed`), `loop/effects_governance.py` and `loop/effects_economy.py` (the `placeable` declines),
  `loop/effects_shared.py` (`_shift`'s assertion), `data/fixtures.py`, `harness/probes.py`
  (`SUBSIST`), `hole_register.yaml`
- EXIT: `populated.build_realm(0)`: every settlement's `recruits` is 0 at build; after the first
  MATTER it is `growth` (1 at the falsifier values), after the second the ceiling (2); no other rung
  holds any; four seasons run through the real driver.
- FALSIFIERS, each with its control:
  - **(i) It regrows at the stated rate.** A settlement's pool debited to 0 by hand reads 1, 2, 2 at
    the next three MATTERs. **Control:** `recruit_regrowth = 0` reads 0, 0, 0.
  - **(ii) It never passes its ceiling.** 8 seasons at `recruit_regrowth = 1000`: `recruits ≤
    recruit_ceiling` at every MATTER and settlement, and the check ran 37 × 8 times. **Control:** remove
    the `min`, and it fails at the second MATTER.
  - **(iii) Only settlements hold a pool.** After 4 seasons no rung outside `pool_rung_kinds` carries
    `recruits`. **Control:** an empty `pool_rung_kinds` filter puts a pool on territory and realm rungs.
  - **(iv) Regrowth does not depend on yield.** A hand-built settlement with no producing Site regrows.
    **Control:** the pass moved inside the yield loop after `if not produced: continue`
    (`matter.py:521-523`) [CHECKED] leaves it at 0.
  - **(v) Settlements with different cohorts differ.** Cohorts at weights 2 and 4 give ceilings 2 and
    4. **Control:** equal weights, equal ceilings.
  - **(vi) A man is not goods, and a troop stands only in a settlement.** A hand-built `requisition`
    of `recruits` → `requisition.refused`, stores unchanged. A hand-built `requisition` of
    `troops_raw` by a seat whose treasury is a territory → `requisition.refused`. **Control:** the
    first act on `grain` executes; the second through a seat whose treasury is a settlement executes.
  - **(vii) A man is not food, under dearth** (re-worded; third critic, finding 8). On
    `build_realm(0)` after one MATTER, with one rung's larder set to `grain: 1`, that rung's cohort's
    `SUBSIST` is identical with and without `recruits: 2`. **Control:** today's formula reads 500 →
    1000 [RAN] (§10). The at-build arm is dropped: no deliberation reads that state
    (`driver.py:432-433`) [CHECKED], and at the first DELIBERATE all 37 read 1000 both ways [RAN].
  - **(viii) The scene tax is measured.** `python -m engine.season.harness.aperture 4 0` before and
    after; a per-verb shift in `requisition`'s and `transfer`'s refusals on `stores:recruits` claims
    is declared with its count.
  - **(ix) The regrowth tells the governors.** After the first MATTER, every live seat whose purview
    contains a settlement holds a `stores:recruits` claim about it, of value `growth`. **Control:** the
    regrowth write without `observed=` → no `stores:recruits` claim in any ledger.
- GOLDENS: **declared mover.** Regrowth writes every settlement's `stores` at the first two MATTERs and
  deposits claims, so every realm `content_hash` moves. `SUBSIST`'s edit moves any run in which a
  deliberating person's rung is short of food and holds coin, timber or ore. **The re-pin is
  intended**; its scope is measured here.

### TS-L · the `levy` follow-through
- STATE: after TS-3, **before TS-4**      LANE: IN
- EDITS:
  - R-04's acceptance text and its historical store-act refusal counts in `requirements.yaml`
    (`:734-735`, `:771-772`) [CHECKED-1; `:772` CHECKED];
  - `hole_register.yaml`'s 19 `levy` hits, including H-163's (`:3634`, `:3641`) [CHECKED];
  - v9 IN-49's EXIT (`_part5.md:215`);
  - the r2 note at `world_q.py:910-914` [CHECKED].
  - Each store-act mention is re-keyed to `requisition`; a historical count keeps its old event
    kind, marked "(then named `levy`)".
- **Cost:** 42 lines in two registers [RAN, `git grep -c -w levy`] plus two notes. No code.
- EXIT: `git grep -n -w levy -- engine/season/requirements.yaml engine/season/hole_register.yaml`
  returns only rows about the troop verb or rows marked "(then named `levy`)".
- FALSIFIER: R-04 reads met while `requisition` has never executed. Control: R-04's status before the
  edit.

### TS-4 · `levy` (row, effect, event kinds)
- STATE: after TS-L      LANE: IN (SE)
- EXIT: `build_realm(0)`, two seasons through the real driver (so the pool is full), one hand-built
  `levy` (`kind: recruits`, `amount: 1`) injected at RESOLVE (as `tests/test_u7_remit.py` injects remit
  acts): `levy.raised` in `w.log`; the settlement's `recruits` fell by 1 and its `troops_raw` rose by 1.
- FALSIFIERS, on one tree and one seed:
  - **(i) R-POOL at the act, byte for byte.** The cohort's `Person` (weight, stance, tenures, body)
    and its `subsistence_draw` row are `repr`-identical before and after. **Control:** P's mint at
    weight 2 changes the settlement's `population`; A's must not.
  - **(ii) Men are conserved.** `recruits + Σ troops_*` at the rung is unchanged across the act.
  - **(iii) Refusals keyed per clause:** `amount = 3` against a pool of 2 → `levy.refused`;
    `kind = grain` → `levy.refused` and nothing moves (**control:** the cell alone admits it, because
    the town holds grain, which shows the effect's decline is needed); a seat without `dispatch` →
    `levy.unauthorized`.
  - **(iv) The world without the act.** No injected act → `content_hash` equal to TS-3's, unless the
    chooser forms the row; then the move is declared with per-verb shifts (H-156's crowding shape).

### TS-11 · a levy eats where it stands, after the people
- STATE: after TS-4; **lands before TS-7**, because a computed levy that does not eat is an
  unbounded one      LANE: SE (IN)
- EDITS: `queries/world_q.py` (`subsistence_draw`'s stock rows; `demanded`/`delivered` docstrings),
  `loop/matter.py` (`short_by_stock` and its debit loop beside the body write, `:443-463`)
- EXIT: a settlement holding a levy: `demanded` rises by exactly `Σ subsistence_weight[k] × count`.
- FALSIFIERS:
  - **(i) R-POOL under dearth.** With a larder below the cohort's want plus the levy's, the cohort's
    draw row is `repr`-identical to the same world with no levy; the levy's row is short and its stock
    falls. **Control:** the levy drawn before persons → the cohort's row changes.
  - **(ii) What bounds a levy, measured through the real driver** (re-worded; third critic, finding 7).
    The second correction's "the stock plateaus within 12 seasons" was asserted with no instrument, and
    the arithmetic projection says it fails (part 1, §2.9):
    - **arm A, one settlement raised at the pool's full rate:** run until its stock is first short,
      or 60 seasons. The projection [RAN] at constant yield says first short in season 34, then
      holding at 18. Site wear moves this earlier, and that is what the run measures.
    - **arm B, gathered:** five settlements' levies transferred each season to one. The projection
      says the gathering rung holds about 18 units whatever arrives.
    - **Control:** feeding off → neither arm is ever short.
    - **What fails the claim:** arm A never short in 60 seasons, or arm B growing past twice the
      projection.
  - **(iii) Weigh the world:** stores per kind move by exactly regrowth, raises and hunger.
  - **(iv) The pins hold.** `test_governance_build.py:521` and `test_territorial_subsistence.py:295`
    green, with `_subsistence_shortfall` still person-keyed.
- GOLDENS: moves only worlds holding a levy, i.e. none until TS-7.

### TS-5 · the order of battle at the seam, behind `field_army` (shipped `single_line`)
- STATE: after TS-1, TS-2, TS-11      LANE: MB (IN)
- EDITS: `queries/world_q.py` (`fielded`, `settlement_above`), `loop/sides.py` (`settlement_above`'s
  call), `seam/wrappers/mass_battle.py` (the origin re-derivation and `parties['origin']`; the no-men
  branch; the garrison's men; the widened `Unopposed` test; `order_of_battle`; `_side_stance`'s
  weights), `queries/inputs.py` (`sides`), `modules/mass_battle/massbattle.py` (`resolve_field` →
  `build_army`; the `:321-323` sentence), `modules/mass_battle/army.py` (`trim_to_command`),
  `modules/mass_battle/equipment/` (`kind_for_kit`, `UNARMED_KIND`, the INERT/NOT YET WIRED
  sentences), `rosters.yaml` (`troop_grades`, kit kinds), `data/fixtures.py` (`men_per_weight`,
  `garrison_men`, `field_army`)
- **⚠ Every wrapper edit is gated on `field_army == order_of_battle`** (third critic, finding 15):
  the origin re-derivation, `fielded`, the no-men branch, the garrison's men, the widened
  `Unopposed` test and `_side_stance`'s new weights. Under `single_line` the wrapper runs today's
  path, byte for byte. `settlement_above` is a pure extraction.
- EXIT: **(a) `single_line`:** the realm `content_hash` after four seasons equals TS-11's. **(b)
  `order_of_battle`:** a seeded hand-built season with a levy raised, armed by `transfer` and marched
  → the field's order of battle shows `kind_for_kit`'s kinds with their `TROOP_TYPE_STATS` presets,
  and `run_battle` fights more than one subunit on a side.
- FALSIFIERS:
  - **Kit reaches the field.** Two arms identical to the tick of the `transfer`; arm Y has none. Over
    N ≥ 50 seeds, the band distributions differ (an exact test, declared at the position).
    **Control:** equal distributions. At today's scale (1) both arms rout every run.
  - **The garrison defends.** A target with members present, no levy, the garrison at full
    `condition` → a fought field. Two arms differing only in garrison `condition` (1000 against 500)
    give different band distributions over N ≥ 50 seeds. **Control:** equal `condition`, equal
    distributions.
    - ⚠ `condition` drives both the walls and the men, so a third arm at `field_walls_dr = 0` (the
      swept control, `massbattle.py:237-239`) [CHECKED] isolates the men.
  - **The defence extremes, all three rows that change or must not.**
    - No member present, a levy and a garrison → `Unopposed`.
    - Members present, garrison `condition` 0, no levy → `Unopposed`.
    - **Control:** `single_line` fights the second and leaves the first `Unopposed`.
  - **The attacker with no men.** An origin with members present and no stock → `march.refused`.
    **Control:** `single_line` fights it at weight.
  - **A defected holder takes no men.** Claimants not all members of the origin's holder faction →
    `march.refused`. **Control:** the same world with the holder's faction matching → fought.
  - **Morale is weighted by men led.** A side with two commanders of opposite stance, one leading
    nine-tenths of the men: the side's morale start leans to his. **Control:** `Person.weight`
    weighting gives the unweighted mean.

### TS-12 · the formation clauses of WALLS and NARROW_PASS for subunit armies
- STATE: after TS-5; **before TS-8**      LANE: MB
- WHY: WALLS' "no flanking; Slow cannot advance" and NARROW_PASS's "1 engagement per side" are skipped
  because "a season unit is ONE subunit with no tactic" (`massbattle.py:251-259`) [CHECKED] (third
  critic, finding 6). Since `20-iv` every settlement march target with a positive garrison is a WALLS
  field (`populated.py:803-804`) [CHECKED]. So flipping TS-8 without this position would fight nearly
  every season field with flanking that the terrain forbids.
- EXIT: a seeded WALLS field with a three-subunit attacker records no flank engagement and no advance
  by a Slow subunit; a NARROW_PASS field records one engagement per side per round.
- FALSIFIER: the clauses removed → flank engagements on WALLS. **Control:** a one-subunit side, where
  the clauses change nothing (the docstring's own claim, re-shown). That `run_battle` exposes flank
  and advance at all is **[INFERRED]** from `:251-252`'s wording.
- GOLDENS: none at `single_line`.

### TS-6 · write-back
- STATE: after TS-5      LANE: MB (IN)
- EDITS: `loop/effects_combat.py` (`_eff_march`: stocks at the origin from `parties` and at the
  target, the garrison's `condition`, the early return; per-mille survivors for persons' `body` too),
  `verb_table.yaml` (`march`'s `writes`, part 2 §4.6), `write_matrix.yaml` (ENC on `(Rung, stores)`
  and `(Site, condition)`)
- EXIT: a seeded lost field lowers each losing stock (and a losing defence's garrison `condition`) by
  the integer rule; the world's stores sums move by exactly the declared sinks.
- FALSIFIERS: `field_casualty_model: none` (`rosters.yaml:861`) → nothing moves. A defending side
  whose men are only its garrison loses `condition`. **Control:** today's early return
  (`effects_combat.py:228-230`) [CHECKED] → it loses none. The row without `Rung.stores` declared →
  the fold writes no stock (shows the declaration is load-bearing, or shows it is not; either is
  recorded).

### TS-7 · the computed `levy`
- STATE: after TS-3 (ix), TS-4 and TS-11      LANE: SE (IN)      R: R-04, R-05
- WHAT: no new question source. The referent is the regrowth's `stores:recruits` claim (part 1,
  §2.3), so `store_kind_of` supplies `kind = recruits` and the referent binds `subject`. The position
  measures whether the chooser forms `levy` from it, and the scene tax of `requisition`/`transfer`
  forming on the same claim and being refused by `placeable`.
- **The design's reach in computed play** [INFERRED]: a seat levies while a pool it governs is filling
  or refilling; a full, untouched pool is silent; equipment and gathering are not reached.
- EXIT: `python -m engine.season.harness.aperture 4 0` shows `levy` executed ≥ 1 with `via`, and every
  executed one carries `kind = recruits`.
- FALSIFIER: a `levy` executed over a settlement outside the seat's purview → fail. **Control:** the
  regrowth without `observed=` → `levy` never forms. The `kind != recruits` refusals are counted and
  declared.

### TS-8 · flip `field_army` to `order_of_battle`
- STATE: after TS-5, TS-6, TS-7, TS-11, TS-12. Without TS-7 no levy exists in computed play, and every
  march is refused by TS-5's no-men branch, so the realm stops attacking      LANE: MB
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

---

## 8. NERS PASS ON THE DESIGN (`skills/ners/SKILL.md`, instrument A)

`[SELF-AUTHORED — bias risk]`. Three independent critics attacked earlier states (18, 13 and 15
findings). This pass's changes (the full footprint, the garrison defence, the origin route, the
regrowth claim, `levy`) have been attacked by nobody but their author. A reviewer should start with
part 1 §2.4 (the footprint table) and §2.3 (the regrowth claim), and §4.1 here (the garrison and the
no-men branch).

**Grade: paper.** Nothing in the season was run against the design, because none of it exists. The
third pass ran read-only probes on today's code (§10).

### 8.1 N — the N-line ledger

| object | N-line | attack | verdict |
|---|---|---|---|
| **`recruits`** | cut it, and R-POOL has no carrier | `envelope` is the population; a Site is fabric; a field amends `04:255` | **HOLDS** |
| **`pool_rung_kinds`** | cut it, and territories hold pools that count the same men again, and troops sit where they can never march | could the ceiling's subtree read alone stop it? No: regrowth would still credit them | **HOLDS** |
| **`recruit_ceiling`** | cut it, and the pool regrows without bound | a second copy of `population`? No: cohorts only, for a different quantity | **HOLDS, NARROWED:** equal everywhere at the shipped data |
| **the regrowth's `observed`** | cut it, and no computed `levy` ever forms (the referent is circular) | is it a read? Yes: regrowth reads the pool to compute it | **HOLDS, [INFERRED]** until TS-3 (ix) |
| **`immovable_kinds` / `placeable`** | cut it, and `requisition` carries a town's pool into a treasury, and troops into a territory where they eat and never march | does anything else stop it? No | **HOLDS** |
| **`SUBSIST`'s edit** | cut it, and men count as food under dearth [RAN] | is it this design's to fix? The defect predates it (coin is sensed as food), but a pool makes it bite | **HOLDS, NARROWED:** dearth only, not at build |
| **`levy`** | cut it, and no act turns a pool into a levy | `requisition` moves goods; `commit` is belief | **HOLDS** |
| **the troop stock** (A) | cut it for P, and ED-WR-0011 breaks | does A lose what made P worth it? Choice, witness, grudge: yes, named. Does it cost more Layer 1? Yes: two sentences, three strains | **HOLDS, NARROWED:** R-WORLD's person half is lost; Layer 1 cost is J-1's |
| **the feeding rule** | cut it, and a levy is free | is it a second eater rule? It is the one draw, with a second kind of mouth, after the first | **HOLDS** |
| **the garrison's men** | cut it, and a town with no levy has persons and no men, so `Unopposed`, and the walls are dead | is it a second carrier? No: Jordan's ruled one, read for a second effect | **HOLDS, [ASSUMPTION]** on the reading |
| **the origin route** | cut it, and no reader knows where the attacker's men stand | a seam parameter would do it at a Layer 1 cost | **HOLDS** |
| **the no-men branch** | cut it, and a march with no men divides by zero or fights a phantom | does PARTY-GAP cover it? No: it tests persons | **HOLDS** |
| **`kind_for_kit`** | cut it, and two owners exist for kind | the builder needs a kind at field time; a function over the kit answers then | **HOLDS, NARROWED:** `levy` reached two ways |
| **the grade kinds** | cut them, and a host that survived three fields is the host it was raised | producer? **None in computed play** | **FAILS in computed play; HOLDS as a carrier** (disqualifier 2) |
| **the commander** | cut it, and who leads changes nothing | the span check divides a side by commander; morale is weighted by men led | **HOLDS, NARROWED** |
| **`men_per_weight`** | cut it, and every field is single digits against a floor of 80 | a flat bonus? No, a unit conversion applied to every side | **HOLDS** |
| **`trim_to_command`** | cut it, and an over-spanned side raises inside the fold (P2) | the host cannot trim without a second copy | **HOLDS** |
| **the `order` key** | cut it, and no act chooses a formation (demand 3) | a ninth operand; `confer`'s `term` | **HOLDS, NARROWED** to player and hand-built acts |
| **TS-12's terrain clauses** | cut them, and WALLS fields allow flanking once sides have subunits | scaffolding? No: A.9's own clauses | **HOLDS** |
| **`field_army`** | cut it, and TS-5 cannot ship hash-neutral | scaffolding | **HOLDS, TEMPORARY** |

**False N-lines in what this design withdraws:** LF-1/LF-3 (a treasury ration): disqualifier 1, the
carrier exists. `_SEASON_FORCE_POWER`: `TROOP_TYPE_STATS` carries quality. The pool on defence: the
garrison is the ruled carrier. The world-gen fill: it silenced the only claim producer.

### 8.2 R — both halves

- **R-COMPLETE, the extremes walked:**
  - an empty pool → `levy.refused`;
  - a full pool → no write, no claim;
  - a stock of 1 → valid, no remnant;
  - an attacker with no men → refused (§4.1);
  - a defence with no member present → `Unopposed`;
  - a defence with members, no levy and a worn-out garrison → `Unopposed`;
  - an over-spanned command → trimmed;
  - an unfed levy → it shrinks;
  - a seat that raises every season → bounded by regrowth for decades of seasons, by food only after
    (TS-11 (ii));
  - `recruit_regrowth = 0` → no pool ever, so no army ever, in computed play.
- **R-VARIETY:** where to raise, how many, how to arm, where to gather, who commands, and (player or
  hand-built) each subunit's role. **In computed play:** where and how many, and who commands. **PASS
  on the shape; NOT SCORABLE** until TS-8.
- **R-CHOICE:** a raise costs the pool and its regrowth seasons, and food every season the levy
  stands. It buys mobility, not home defence (§4.1).
- **R-WORLD:** a starving levy shrinks without anybody deciding it; a lord who defects with his towns
  takes their men; a worn garrison leaves a town open; a governor hears his town's pool refilling and
  may raise. **Corrected** (third critic, finding 3): "neighbours learn through `stores.changed`" was
  false. Only the settlement's governors learn, through the regrowth's read (part 1, §2.3), and
  persons at or holding the rung witness the write. **Lost against P:** a levy that chooses to desert,
  witnesses its lord's orders, or nurses a grudge. **PASS on the shape**, narrower than P's.

### 8.3 S — six directions, pause, methodology

| direction | carried by | verdict |
|---|---|---|
| **S-UP** | a pool's refill reaches the seat as a claim; whether the holder levies is his choice (TS-7) | **PASS on the shape**, [INFERRED] until TS-7 |
| **S-DOWN** | none under A: a stock is no party | **N-A under A** (P carried it) |
| **vertical** | `recruits` → stock → `troops = count × men_per_weight` → survivors back to the stock; one conversion | **PASS** |
| **diagonal** (SE matter → MB field) | `requisition` → `transfer` → `kind_for_kit` → `of_type` | **PASS on the shape for player acts; FAILS in computed play** (no arms producer, no arms claim) |
| **lateral** | `levy` and `requisition` share the typed cell conjunct for conjunct and the keyed-refusal split | **PASS** |
| **horizontal** | one `mustered`, one `fielded`, one `settlement_above`, one `order_of_battle`, one `build_army` for both sides | **PASS.** The second correction's residual (the seat's label against the holder) is closed by the members-of-`H` test (§4.1) |
| **pauses correctly** | the field resolves inside the fold, as today | **N-A** |
| **methodology** | **One draw for every mouth** (cohorts, then stocks); **one rounding rule**; **morale weighted by the same men that size the side** (fixed here, third critic finding 10); **two replenishing clocks**, yield (no ceiling) and the pool (a ceiling), the same write with a different bound, stated. **One quantity, two effects:** garrison `condition` sets the walls and the men; stated, and TS-5's third arm separates them. **Still open:** an individual's casualty is `int(body × float)` (`effects_combat.py:250-255`) [CHECKED], routed to per-mille at TS-6 | **FINDINGS → TS-3, TS-5, TS-6** |

### 8.4 E — last, as a ratio

- **N and R found** a pool, a stock, a verb, a feeding rule, a garrison defence and an origin route
  that hold; one failure in computed play (the grade) and one diagonal failure (equipment); one
  narrowed R-WORLD against P.
- **Count:** 59 added against 5 cut on disk under A (part 1, §3.5). P is not recounted on these rules.
- **E-OVERHEAD: NARROWED, toward failing.** Every addition carries a fact the engine reads or a reader
  of one, and none is a parallel scheme. But additions outnumber cuts about twelve to one, and eleven
  of the 59 are text the change forces elsewhere: six Layer 1 lines, four TS-L re-keys and one
  module docstring.
- **E-LEGIBILITY: PASS on the shape.** A player sees men raised from a town's pool, the pool refilling,
  the levy armed from the town's stores, gathered, led, killed or starved, and a town with a worn
  garrison left open. Each outcome traces to one act or one clock.

### 8.5 The design's own falsifier

**No fighting man exists unless he is in a pool or a garrison, and none vanishes without a receipt.**
Named persons fight without being in a pool: they command and are not men (part 1, §2.6). Guard
cohorts and convicts in service field nothing under A.

### 8.6 Self-audit

- **Backward propagation:** part 1 §0 carries the full footprint, the garrison, the origin route, the
  regrowth claim and `levy`; §2.4 carries the table; §3.5 recounts; §5 marks ED-FA-0010; §6 adds
  `garrison_men` and drops the fill; §7 adds TS-12, re-words TS-3 (vii) and TS-11 (ii), and re-orders
  TS-L; §9 re-ladders J-3 and J-6.
- **What an independent reviewer would add:** a run of the regrowth claim through WITNESS (TS-3 (ix)),
  and of the garrison defence's effect on how often a march succeeds. Neither was run.

---

## 9. DECISIONS FOR JORDAN

**CLAUDE.md §0's ladder, per item.** Only what survives all five steps is escalated.

| id | the decision | ladder | escalated? |
|---|---|---|---|
| **J-1** | the troop body under the pool | not superseded; not irrelevant; no document decides it; no precedent fits; architecture prefers A on ED-WR-0011's explicit text, **but A amends two ratified Layer 1 sentences (six lines) and strains three clauses, and P/P′ break ED-WR-0011** | **yes:** every option overwrites ratified canon or a ruling |
| **J-2** | does raising draw down the population | step 1, superseded by R-POOL | **no — ANSWERED** |
| **J-3** | the troop verb's name | step 5 and Jordan's words: `levy` (part 1, §3.1). The store act's name is in the tree (`requisition`), reserved to Jordan by the brief, not reopened | **no — ANSWERED: `levy`; TS-L carries the cost** |
| **J-4** | do LF-1..LF-3 stand | step 5: under A a levy eats through the one draw; a treasury ration would double it | **no — folded into J-1** |
| **J-5** | what a fought field writes beyond casualties, morale and grudge | it overturns ED-IN-0279's ruled content if anything changes | **yes** |
| **J-6** | who counts as troops | re-laddered (third critic, finding 12): `24f` is about who eats. Answered by R-POOL ("available troops to raise … derived from" the settlement) and step 5 (no double count) | **no — answered: stocks and the defending garrison; no person** |
| **J-7** | the service term | under A there is none; under P, step 5: reuse `oblige_term` | **no — moot under A** |
| — | who defends a town | step 4: Jordan's garrison ruling (`world_q.py:1275-1278`) and "present at the target" (`:1257-1259`). The pool-defends default is withdrawn. Reading `condition` as men too is **[ASSUMPTION; medium; Jordan to correct]** | **no — answered, Jordan-vetoable** |
| — | the origin route | step 4: `_origin_of`'s precedent; step 5: no Layer 1 line | **no — answered** |
| — | pools start empty | step 5: a filled pool would silence the only computed referent producer | **no — answered** |
| — | troops only on settlements | step 5: elsewhere they eat and never march | **no — answered** |
| — | a political cost of raising (ED-FA-0010; the SE research row) | step 1: ED-FA-0010 superseded; step 5: a province value breaches the NEVER list; the lawful carrier, the cohort's stance, is available if asked | **no — answered, not adopted** |
| — | the ceiling base, the regrowth form, the pool-holding rung kinds | step 5 (part 1, §2.2, §2.3) | **no — answered in text** |
| — | the levy eats after the people | step 5 plus R-POOL under scarcity (part 1, §2.5) | **no — answered** |

**The escalated decisions:**

| id | the decision | options, and what each does to the game | default here | what waits on it |
|---|---|---|---|---|
| **J-1** | **what a troop is, once raised from the pool** | **(A) a troop stock on the settlement rung** (default). Armies are counts that eat where they stand, fight for whoever holds their walls, and move between settlements by `transfer`. **Footprint (part 1, §2.4):** it amends `04:793`/`03:261`/`10:89` (units) and `04:802`/`03:269-270`/`10:97-98` (one scale down); it strains `04:252`/`01:896` (address, not occupant), `04:257`/`01:910-911` (NEVER discipline-as-a-stored-value) and T-l's reason (`01:497-499`); it widens the ruled `march` row's `writes` (`verb_table.yaml:677-681`); it amends `24f`'s code rule within ED-IN-0255's words. `04:765` and `04:780` stand. A levy cannot choose, witness or hold a grudge. · **(P) a company `Person`** minted from the pool. Armies are people who deliberate, desert, witness and die. **Overturns or narrows ED-WR-0011**; amends `04:792`/`03:260`/`10:88`; strains the scale-down parallel; violates RR-2 and J-16, and R-POOL under dearth, unless P′'s form and an order rule are added (§4.8). · **(P′)** P without `reside`: ED-WR-0011 still broken; J-16 must accept a state-keyed dissolution; Layer 1 as P. · **(B) a typed troop row:** amends A's two sentences and T-l (`04:123`, `01:497`). **Under A, consequences that ride with it:** no stand-down verb; kit stays with the town; the garrison's `condition` is read as men; raising has no political cost unless asked (part 1, §2.10) | **A** | everything in §7 from TS-4 on |
| **J-5** | **what a fought field writes** (ED-IN-0279: losses only, nothing on the winner) | **(a) as ruled.** · **(b)** winners take their engine casualties too. · **(c)** survivors of both sides move one grade up: the only computed producer of experience while J-13 (iii) stands. · (d), veterans persisting, is moot under A | **(a)** until ruled. **Recommended: (b) + (c)** | TS-6's write set; TS-10; M-MB-16 |

**Tuning values, not decisions** (eight, each **[OPEN — Jordan tuning]** with a register row and a
sweep at its position; part 1, §3.5 #40–47): `recruit_share`, `recruit_regrowth`, `men_per_weight`,
`garrison_men`, the `troop_grades` ladder, the equipment kinds, which grade a shared kit equips first,
and how the unarmed remainder is typed. **Not a value:** the arms producer, an existing gap
(`site_yield` has no arms row) that this design names and does not close.

---

## 10. LIMITS

**Re-opened in the third correction pass (`[CHECKED]`):**
- **Layer 1:** `04_CODE_ARCHITECTURE.md:120-125`, `:250-258`, `:760-805`; `03_VERBS_AND_LOOPS.md:1-4`,
  `:255-272`; `10_FACTIONS_AND_DEPLOYMENT.md:1-4`, `:84-100`; `01_AXIOMS.md:494-500`, `:892-912`.
- **Season code:** `loop/sides.py:60-130`; `seam/wrappers/mass_battle.py:120-260`;
  `queries/world_q.py:800-830`, `:850-964`, `:1244-1296`; `harness/populated.py:790-812`,
  `:1490-1505`, `:1522-1532`; `loop/witness.py:140-175`, `:415-480`, `:540-580`;
  `loop/resolve.py:430-500`, `:825-855`, `:980-1000`; `decision/options.py:598-655`, `:840-880`;
  `loop/matter.py:335-545`; `loop/driver.py:420-445`; `loop/effects_combat.py:222-262`;
  `verb_table.yaml:664-690`, `:1207-1213`; `write_matrix.yaml:155-163`, `:210-219`, `:318-338`;
  `data/verbs.py:376-401`; `rosters.yaml:1371-1387`; `hole_register.yaml:3634`, `:3641`,
  `:3728-3734`; `requirements.yaml:772`; `state/ids.py:15-21`;
  `tests/test_governance_build.py:515-525`; `tests/test_territorial_subsistence.py:75-79`, `:290-296`.
- **Module:** `modules/mass_battle/equipment/__init__.py:1-40`; `massbattle.py:200-262`, `:315-326`.
- **Ledgers and research:** `research/by_lane/SE_settlements_territory_economy.md:97`, `:187`;
  `registers/editorial_ledger_fa_archive.jsonl:9`.
- **Other:** the session brief's statement 5 (not in the tree).

**Ran in the third correction pass** (from `/home/user/ttrpg`; scripts and outputs under the session
scratchpad, `/tmp/claude-0/-home-user-ttrpg/3f6de207-94f6-530b-a5b4-52aac53c2712/scratchpad/`, outputs in
its `tmpl/`):
- `python probe_subsist.py` → `tmpl/probe_subsist.out`: cohort `cohort_set_s_001`, stores `{}` at
  build; `SUBSIST` 0, with `recruits: 2` 1000; larder `grain: 1` 500, plus `recruits: 2` 1000; empty
  0, plus `recruits: 2` 1000; the sampled `H(…)` id `3b5fbcbdce6ac4cc` sorts before
  `cohort_set_s_001`: True. Exit 0.
- `python probe_subsist2.py` → `tmpl/probe_subsist2.out`: at build, 37 cohorts, base 0/0, with
  `recruits: 2` 1000/1000, moved 37; after one season through `populated.run`, 1000/1000 both ways,
  moved 0. Exit 0.
- `python probe_subsist3.py` → `tmpl/probe_subsist3.out`:
  - after one MATTER (the first DELIBERATE's state), 37 cohorts, 1000/1000 both ways, moved 0;
    `set_s_001`'s stores `{grain: 40, ore: 50, salt: 30, timber: 10}`; dearth `grain: 1` 500, plus
    `recruits: 2` 1000;
  - per-settlement yield over four real seasons: every one of 37 settlements grain 40/39/39/38,
    salt 30/29/29/29 (totals 1480, 1443, 1443, 1406 and 1110, 1073, 1073, 1073);
  - the arithmetic projection over 12 seasons: `[2, 3, …, 13]` at every settlement. Exit 0.
- `python probe_plateau.py` → `tmpl/probe_plateau.out` (arithmetic only): first short in season 34 at
  34 units, then 18 from season 34 to 60.
- `git grep -c -w levy -- engine/season/requirements.yaml engine/season/hole_register.yaml` → 23 and
  19. `git grep -n -w levy -- engine modules` outside the two registers → the module troop type, the
  r2 note, `rosters.yaml:1582`, `goals.yaml:413`, two test comments and `engine_params` captures.

**Could not check:**
- **That the W-B deposit lands a seat-channel observation as a claim** a question can be about (part 1,
  §2.3) — **[INFERRED]** from `witness.py:428-429`.
- **That `_contest` turns a PARTY-GAP-shaped refusal into `march.refused`** — read from a comment
  (`sides.py:99-101`).
- **Whether the gate refuses an effect's write outside the row's declared pairs**, and **that ENC
  shares RESOLVE's write class** (`data/matrix.py` not opened).
- **Whether `run_battle` fights multi-subunit `Unit`s on the season's terrain rows**, and whether it
  exposes flank and advance for TS-12.
- **The golden scope of the `SUBSIST` edit and of the regrowth claims** (TS-3 measures them).
- **The food bound through the real driver** — the projection holds yield constant; TS-11 (ii)
  measures it.
- **Which harness batteries TS-2 moves** (`bat.py` not opened).
- **The MB lane's scale probe** (≈120 troops; 0 of 20 at ≤ 80), cited and not re-run.
- **The drafting probes P1–P3** and the first correction's probes were not re-run.
- **`CURRENT.md` and `HANDOFF_MB.md`** were not read.
- **PP and ED provenance** other than ED-WR-0011, H-173's J-16 note and ED-FA-0010 was not verified
  against the ledgers.
- **R-POOL** is quoted as the coordinator relayed it.
- **The `.audit/` and `.designs/` trees** were not read.

---

## CRITIC RECONCILIATION (first critic, 18 findings, against the draft)

Kept as recorded at the first correction. The last column is updated where a later correction changed
a finding's status.

| # | finding | verdict at the first correction | status now |
|---|---|---|---|
| 1 | weight-2 cohorts: a split of 1 yields two non-cohorts | applied, then superseded by R-POOL | moot: a stock of 1 is valid |
| 2 | `mustered` pulls in vassals of other factions | applied (`service_faction` excludes `commit` holders) [RAN] | moot: the muster is unchanged; kept for P (§4.8) |
| 3 | the morale reader cannot see companies | applied (`faction_holding or service_faction`) | moot: no company; the reader is re-weighted by men led (§4.1) |
| 4 | experience via `train` excludes case-less persons | applied; TS-10 blocked | stands: no computed grade producer |
| 5 | equipment unreachable; a second loadout table | applied (`kind_for_kit` beside `TROOP_LOADOUT`) | **stands as found:** equipment is not computed-reachable (third critic, finding 3) |
| 6 | reusing `levy` collides with three registers | applied (`conscript`; J-3; TS-L) | re-decided: the verb is `levy`; the collision is TS-L's cost (third critic, finding 12) |
| 7 | grouping merges a lord's companies; demand (3) overstated | applied (one subunit per company) | re-cast: one subunit per grade × kind, splittable by `order` |
| 8 | Command constant 4; `COMMAND_SIGMA_ENABLED` | applied | stands |
| 9 | the §0 ladder misapplied to J-4, J-6, J-7 | applied | stands; J-6 re-laddered again (third critic, finding 12) |
| 10 | `order` is a ninth operand | applied (`confer`'s `term`) | stands |
| 11 | statement 1's contrary reading not cited | applied | stands; A meets it in full |
| 12 | upkeep per person; the witness channel | applied (stated, not fixed) | moot under A; P's upkeep claim corrected (§4.8) |
| 13 | `remove_person` pops the person-rung, so kit is destroyed | applied (salvage clause) | moot: kit is the town's |
| 14 | the row's `writes` omits `Tenure.term` | applied | moot: no Tenure is written. The `march` row's `writes` now widen instead (third critic, finding 5) |
| 15 | falsifiers blind at scale 1 | applied (`men_per_weight = 250`) | stands |
| 16 | NPC5: a defecting lord leaves his men behind | applied (holder's faction) | stands, through `fielded`'s holder read |
| 17 | the meta-rule net undercounted | applied (22 vs 6) | superseded twice; now 59 vs 5 |
| 18 | 22 files, not 44; `carriers.py:928` | applied | stands |
| — | the morale-preset defect, untracked | applied (TS-2) | stands |

---

## SECOND CRITIC RECONCILIATION (13 findings + an observation, against the first correction)

Kept as recorded at the second correction. Where the third correction changed an outcome, the third
table says so; the rows affected are 1 (the referent), 6 (the build-state reading), 8 (the defending
pool) and 13 (the count).

| # | finding | verdict | where |
|---|---|---|---|
| 1 | the typed cell cannot name `recruits`; computed `kind` is `grain`; no "pool short" decline | **applied.** The effect declines `kind != recruits` and a short pool; TS-7's referent is a `stores:recruits` claim. The first correction's `conscript_amount` was dead; withdrawn | part 1 §1.4, §3.1; part 2 §6, TS-4 (iii), TS-7 |
| 2 | `is_company` reads `Term.declared_by`, which renewal overwrites; J-16 forbids a branch on origin | **applied.** Under A there is no company. Under P `is_company` is withdrawn for a state-keyed rule J-16 must accept | part 1 §1.5, §2.4; part 2 §4.8 |
| 3 | a computed army does not "last one term": TS-7's obliges become renewable | **applied**, restated for P | part 2 §4.8 |
| 4 | ED-WR-0011 never cited; it weighs toward a body that mints nobody | **applied, and decisive.** The default moved from P to A. Narrowed: CENSUS already mints a weight-1 person at run time | part 1 §1.5, §2.4; part 2 J-1 |
| 5 | capacity bypassed by fiat; eating reads `contain`, not `reside` | **applied.** Moot under A; P′ drops `reside` | part 1 §1.5, §2.4; part 2 §4.8 |
| 6 | men are sensed as food; draw order puts a company first; R-POOL unshown under scarcity | **applied.** `SUBSIST` reads only weighted kinds; levies draw after persons; TS-3 (vii) and TS-11 (i) | part 1 §2.5; part 2 TS-3, TS-11 |
| 7 | which rungs hold a pool; regrowth skipped by `if not produced: continue` | **applied.** `pool_rung_kinds: [settlement]`; regrowth in its own pass | part 1 §2.2, §2.3; part 2 TS-3 |
| 8 | defence inverted: no company → `Unopposed`; walls never engage | **applied** as "the pool defends its own settlement" | part 2 §4.1 |
| 9 | the case against E applied equally to S | **applied** | part 1 §2.1 |
| 10 | the cell was not `requisition`'s "conjunct for conjunct" | **applied by making it so** | part 1 §3.1 |
| 11 | `hole_register.yaml:3543` is H-156, not H-163 | **applied** | part 2 §5 |
| 12 | the `conscript` absence claim is false; J-3 omits `rosters.yaml:1582` | **narrowed, then applied** | part 2 J-3 (since superseded: the verb is `levy`) |
| 13 | the object count omitted event kinds, edits, constants, result keys, hole rows | **applied** (35 vs 5) | part 1 §3.5 |
| obs. | `_rehome`'s safety rests on "nothing … constructs a Person"; already stale | **applied for P, moot for A** | part 1 §2.4; part 2 §4.8 |

---

## THIRD CRITIC RECONCILIATION (15 findings + observations, against the second correction)

Every locator below was re-opened in this pass before any text changed (§10).

| # | finding | verdict | where |
|---|---|---|---|
| 1 | "under A, `04:793` changes and nothing else"; the 1-vs-4 count is not a count | **applied.** Reproduced: `03:261`, `10:89` restate `04:793`; `03:269-270`, `10:97-98` restate `04:802`; `04:252`/`01:896`, `04:257`/`01:910-911` and T-l's reason (`01:497-499`) are crossed; `OrderOfBattle` contradicted the proposed "never a record"; `massbattle.py:321-323` states the old contract. The count is replaced by a per-line table for A, P, P′ and B; "fewest" is withdrawn; the amended text now names the order of battle as a seam record. **Narrowed in one respect:** `04:780` is kept in letter under the new defence (every fought side has a member present), with its spirit named | part 1 §0 item 2, §2.4, §3.5; part 2 §4.2, §9 J-1 |
| 2 | the attacker-with-no-men refusal does not exist; the wrapper never sees the origin | **applied.** Reproduced (`mass_battle.py:154-155`, `:224-226`; `sides.py:82-84`; `massbattle.py:208-210`). Route (R) chosen: re-derive from claimants' homes through one extracted Query, `settlement_above`, returned in `parties`; (S) a seam parameter declined for its `04:765` cost. A new branch refuses a side with no men; TS-8 now stands on it | part 1 §0 item 4, §3.5 #23–25; part 2 §4.1, TS-5, TS-8 |
| 3 | the computed referent for the levy and for kit has no producer | **applied.** Reproduced (`resolve.py:987-990`; `matter.py:495-503`, `:530-536`; `witness.py:428-431`, `:561-562`). Regrowth's write now carries its pool read as `observed`, which the generic actorless route (`witness.py:446-456`) delivers to governors; pools start empty so the claim is produced. Equipment is **not** reachable in computed play; the gain is withdrawn. Whether the W-B deposit lands the claim stays [INFERRED], with TS-3 (ix) as its falsifier | part 1 §0 item 5, §1.4 item 19, §2.3, §2.4, §3.1, §3.2; part 2 §4.7, TS-3, TS-7, §8.2 |
| 4 | the pool defends; Jordan already ruled the garrison Site and "present at the target" | **applied.** Reproduced (`world_q.py:1257-1259`, `:1275-1278`; `populated.py:799-804`). The pool no longer defends; the garrison's `condition` sizes the defence's men (an extension of the ruling's reading, marked [ASSUMPTION]); a side with no member present stays `Unopposed`. The table is walked row by row, and row 4 is shown unchanged from today | part 1 §0 item 4, §1.5 item 28; part 2 §4.1, TS-5, §9 |
| 5 | the `march` row's `writes` edit is uncounted; `fielded` and the no-men branch missing; register rows undercounted | **applied.** Reproduced (`verb_table.yaml:677-681`, `:689`; `resolve.py:442`). The row edit, `fielded`, the branch, the origin route and eight register rows (one per tuning value) are counted: 59 added | part 1 §3.5; part 2 §4.6, §9 |
| 6 | WALLS and NARROW_PASS formation clauses stay unapplied for subunit armies | **applied as a position,** TS-12, before TS-8. Reproduced (`massbattle.py:251-259`) | part 1 §1.2 item 8; part 2 TS-12, TS-8 |
| 7 | "the bound on armies is food" and TS-11 (ii) asserted with no instrument | **applied, and the estimate confirmed.** [RAN] yields are 40 grain/30 salt per settlement per season; the arithmetic projection reaches 13 units in 12 seasons with no shortfall, first short in season 34. The claim is narrowed (regrowth bounds the short run), and TS-11 (ii) is re-worded with arms, a control and a stated failure | part 1 §2.9; part 2 TS-11; §10 |
| 8 | the at-build `SUBSIST` state is never sensed | **applied.** Reproduced (`driver.py:432-433`); [RAN] after one MATTER all 37 read 1000 both ways. TS-3 (vii) keeps only the dearth arm | part 1 §0 item 9, §2.5; part 2 TS-3 |
| 9 | wrong dearth-step locator; unlisted consumers; pinned tests; the record's key type changes | **applied.** Reproduced (`matter.py:344-353`, `:420`, `:443-463`; `populated.py:1498`; `test_governance_build.py:521`; `test_territorial_subsistence.py:295`; `world_q.py:804`, `:959`). The shortfall splits into a person-keyed and a stock-keyed dict, so `_subsistence_shortfall` and its pins are unchanged; stock rows append after persons | part 1 §1.4 item 24, §2.5; part 2 TS-11 (iv) |
| 10 | `_side_stance`'s reason dies: sized one way, morale read another | **applied.** Reproduced (`mass_battle.py:136-137`). Morale is weighted by the men each commander leads; an S-methodology finding closed | part 2 §4.1, §4.2, §4.5, TS-5, §8.3 |
| 11 | troops requisitioned into a territory or realm treasury can never be fielded | **applied: forbidden.** Reproduced (`options.py:600-615`). `placeable` admits a troop kind only on a `pool_rung_kinds` rung | part 1 §2.1, §3.2, §3.4; part 2 TS-3 (vi) |
| 12 | J-3 and J-6 do not meet the escalation test | **applied.** J-3: the verb is `levy` (Jordan's words; the brief reserves the store act's name, not this one); TS-L is a position with its cost stated (42 register lines [RAN]). J-6: re-laddered onto R-POOL and step 5 | part 1 §3.1, §2.6; part 2 TS-L, §9 |
| 13 | "a minted id sorts before `cohort_…`" generalised one sample | **applied.** Reproduced (`state/ids.py:19-21`): 13 of 16 leading characters sort before, 3 after; P needs an order rule either way | part 1 §2.4; part 2 §4.8 |
| 14 | `TROOP_LOADOUT` is INERT and "NOT a derivation"; `levy` is both armed and the remainder | **applied.** Reproduced (`equipment/__init__.py:10-20`, `:22`). `kind_for_kit` is the derivation's owner and `TROOP_LOADOUT` its data; both module sentences are edited at TS-5; the two routes to `levy` are an [OPEN — MB] item | part 1 §1.3 item 12, §2.7; part 2 §6, TS-5 |
| 15 | TS-5 (a)'s hash-neutral exit holds only if every wrapper change is gated | **applied.** Every wrapper edit is named as gated on `field_army` | part 2 TS-5 |
| obs. | RR-2: men bounded by food, never dwellings | **noted:** A complies by definition; §2.9 shows the bound is regrowth, then food | part 1 §2.9 |
| obs. | a compliance term (SE research) and ED-FA-0010's PS cost | **weighed, not adopted** on the ladder; the lawful carrier is named for Jordan | part 1 §2.10; part 2 §5, §9 |
| obs. | the heading "Keys: troop kind × grade" reads as the retired Key substrate | **applied:** "Troop kind and grade" | part 1 §2.7 |

**Rebutted:** none. **Narrowed:** finding 1 (`04:780` survives in letter under the new defence).
