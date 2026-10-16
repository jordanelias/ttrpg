# The troop stock — part 2: the seam, the cuts, the data, the build, the NERS pass, the decisions

## Status: PROPOSED (2026-10-16), corrected and re-based on R-POOL the same day. Not ratified; merge ratifies nothing unless Jordan so rules.
## Part 2 of 2. Head, verdict, R-POOL and §1–§3: [`2026-10-16-troop-stock-design.md`](2026-10-16-troop-stock-design.md). Locator conventions as there (`[CHECKED]` = re-opened in the correction pass; `[CHECKED-draft]` = opened at drafting only; `[RAN]`, `[INFERRED]`, `[UNVERIFIED]`).

---

## 4. ARMY ASSEMBLY AND THE SEAM

### 4.1 Who stands on a side: one Query for service, read by the muster and by morale

**Today.** `mustered(w, rung, faction)` returns faction members (a live `commit`) whose `contain` is in
the rung's subtree (`world_q.py:1256-1272`) [CHECKED]. A company has no `commit`: it serves, it does not
believe.

**The new Query, `service_faction(w, pid)`** (in `queries/world_q.py`, beside `faction_holding`):
- **The person holds any live `commit`:** `None`. His side is his belief's, read by `members`.
- **Otherwise:** the faction of the **holder** of each seat he holds a live `oblige` to,
  `faction_holding(w, holder)`. One faction → that one. None, or more than one → `None`.
- **Both choices follow precedent (CLAUDE.md §0's ladder, step 4):**
  - "the holder's faction, not the seat's label" is `holder_faction_of`'s rule: "`faction_holding` on
    ITS holder (a person)" (`world_q.py:1441-1466`) [CHECKED];
  - "none and many both return `None`" is `faction_holding`'s own (`world_q.py:1405-1440`) [CHECKED].

**The edit to `mustered`:** members present **∪** persons present whose `service_faction` is this
faction.
- **One owner for both sides.** It is written once, in `mustered`, so the attacking side
  (`loop/sides.py:85`) [CHECKED] and the defending side (`seam/wrappers/mass_battle.py:233`)
  [CHECKED-draft] both get it.
- **Membership is untouched.** `members` still says "THERE IS NO SECOND ROUTE" (`world_q.py:1154`)
  [CHECKED-draft]. A side in a field is not a membership. It is who stands there for the faction.
- ⚠ **It amends Layer 1's muster line** (part 1, §0 item 4). That amendment is part of J-1.

**The two shipped `oblige` edges are the test** (critic finding 2). Probe on `populated.build_realm(0)`
[RAN]:

```
p_npc_041 1 -> off_restoration_leader seat faction Restoration Movement | obligee commits fac_restoration_movement
p_npc_070 1 -> off_npc_020 seat faction Crown | obligee commits fac_löwenritter
```

(`engine/season/offices.yaml:191`, `:591`; opened by `harness/populated.py:1339`) [CHECKED].
- **NPC-070**, the Löwenritter Grand Master sworn to the Crown's seat (FA-04), holds a `commit` to
  `fac_löwenritter`. So `service_faction` returns `None`, and she stands only with the Löwenritter.
  Under the draft's unrestricted clause she would have stood for the Crown too, on both sides of a
  Crown–Löwenritter field.
- **NPC-041** holds a `commit` to the faction whose seat she serves. She is already a member, and the
  clause adds nothing.
- **So the clause adds nobody to any side at build.** TS-5's arm (a) asserts that `mustered`'s output
  is unchanged at every settlement of the shipped world.

**What the clause still sweeps in, named so nobody is surprised:**
- **Any person in no faction who serves a seat**: IN-36's guard cohorts (`_part5.md:158-175`)
  [CHECKED-draft as a citation], which is right, since guards defend.
- **A bench's convicts under a `determine` disposal who hold no `commit`** (the H-173 hazard,
  `hole_register.yaml:3765`) [CHECKED]. `determine` executes 0 times in the shipped worlds (H-163), so
  this is latent today. It is a residual (§8).

**The morale reader, fixed with the same Query** (critic finding 3; CLAUDE.md §0.1 pt 1, read/write
asymmetry):
- **The defect:** `_side_stance` finds each person's faction through `faction_holding`, which reads
  `commit` only (`seam/wrappers/mass_battle.py:126-148`; `world_q.py:1436-1438`) [CHECKED]. Yet
  `_eff_march` writes `(loser_faction, -1.0, morale_w)` onto every loser (`effects_combat.py:260`)
  [CHECKED]. So a company's morale row is written and never read. A side made mostly of companies
  starts at base morale whatever its losses and loyalty.
- **The fix:** `fac = world_q.faction_holding(w, pid) or world_q.service_faction(w, pid)`. Because
  `service_faction` is `None` for anyone holding a `commit`, the `or` changes nothing for any person
  the reader sees today. A person committed to two factions still reads 0, as now.
- **The falsifier (TS-5):** a side of companies only loses a field. Its `_side_stance` at the next
  field is below 0 by the morale row. **Control:** the same two fields with today's reader, which
  reads 0 both times.

**Two consequences of service the draft omitted** (critic finding 12):
- **Upkeep is per person, not per man.** `_renewals` counts obligees, and `upkeep_of` is what a seat
  pays "EACH PERSON OBLIGED TO IT, PER TERM" (`effects_economy.py:303-308`; `world_q.py:1537-1568`)
  [CHECKED]. A 500-man company costs one man's upkeep. No computed act pays upkeep yet
  (`effects_economy.py:283-290`) [CHECKED], so in computed play every company's term matures at
  `oblige_term` (4 seasons), and it dissolves (part 1, §2.9). A computed army lasts one term. §8.2
  carries the per-person cost.
- **Every company is an informant.** `_ch_post_remit` credits every `establishment_of` member
  standing in the seat's ground with `inferred` knowledge of every act done through the seat
  (`epistemic.py:460-486`; H-173 (2)) [CHECKED]. Soldiers hear their lord's orders. That is plausible,
  but it adds claims, and claims add chooser load. TS-4's falsifier (iii) measures it.

**Kept unchanged:** the attacker's exclusion of a restrained person (`sides.py:86-92`) [CHECKED-draft].

### 4.2 What a side is: an order of battle, one subunit per company

`field_input` (`seam/wrappers/mass_battle.py:175-201`) [CHECKED-draft] stops passing `weights`. For
each side it passes an **order of battle**, a frozen tuple the host derives from `World`.
`MassBattleInput` (`queries/inputs.py:62-100`) [CHECKED-draft] trades `weights` for `sides`:

```
sides  = (OrderOfBattle_attacker, OrderOfBattle_defender)
OrderOfBattle = ( general: (name, command),
                  officers: ((name, command), …),                 -- sorted by name
                  subunits: ((company_id, kit, grade_offsets, troops, role|shape, officer), …) )
                                                                   -- sorted by company_id
```

**How the host fills one side** (one function, `order_of_battle(w, pids, general)`, in the host
wrapper):
1. **Troop-bearing persons** are the side's cohort persons (part 1, §2.6). Named persons contribute
   command, not troops.
2. **One subunit per company** (critic finding 7):
   - The draft grouped companies by kind, grade and commander. That merged a lord's two companies of
     one kind into one subunit, so even a player could not field them as two wings in two formations.
   - Now each company is its own subunit, and `order` (§4.3) names each one's role.
   - **The cost:** more subunits press harder on the span check, so a commander of Command 4 fields at
     most four companies directly (`engine.py:304-345`) [CHECKED-draft]. That is the commander axis
     biting, and it is intended. A lord who wants one larger block raises one larger company.
3. **Each subunit:**
   - `troops = weight × men_per_weight`, an int;
   - `kit` is the company's person-rung stores of equipment kinds;
   - `grade_offsets` is its grade's `troop_grades` row;
   - `role` or `shape` comes from the march's `order` when it names the company, else the module's
     default for the derived kind (§4.3).
4. **The commander** of a company is the holder of the seat its `oblige` names. A cohort with no such
   seat (a member cohort, should one ever `commit`) reports to the general.
5. **The general** is the marching actor on the attacking side. On the defending side it is the holder
   of the seat holding the target, or the defending faction's leader present (`leaders`,
   `world_q.py:1165`) [CHECKED], else no general (command at the builder's default).
6. **Command, and what it does before R-C-1** (critic finding 8):
   - `Officer` derives `command` from charisma and cognition only when both are given **and**
     `COMMAND_SIGMA_ENABLED` is on (`hierarchy/units.py:2711-2716`) [CHECKED]. The flag defaults on,
     from the environment (`config.py:530`) [CHECKED].
   - The season supplies neither attribute until R-C-1/J-13 names a source
     (`00_COMPARATIVE_ANALYSIS.md:584`; `_part5.md:433`) [CHECKED-draft; :433 CHECKED]. So **every
     season commander's Command is the constant 4** (`units.py:2711`) [CHECKED].
   - **What still varies is who commands,** and so how the span check divides a side's companies.
     How well he commands does not vary yet.

**A side whose order of battle holds no subunit has no troops:**
- **An empty defending side** is `Unopposed`. That widens the existing "nobody mustered" branch
  (`mass_battle.py:235-248`) [CHECKED-draft] from no persons to no troops, for the same reason: the
  wrapper does not "launder" an empty side into a fabricated fight.
- **An empty attacking side** is the existing PARTY-GAP refusal (`mass_battle.py:224-226`)
  [CHECKED-draft], which the fold turns into `march.refused`.

### 4.3 What `march` carries

- **Unchanged:** `subject`, the Rung marched on. The row's `requires_typed`, `contests:`, eligibility
  and degree-keyed `writes` keep their shape.
- **Added: one act-declared payload key, `order`.** It maps company ids to roles.
- **Is it a ninth operand? Yes** (critic finding 10). The draft cited `rosters.yaml:231-233` ("a key
  naming none … may be absent"). That governs a minted document's `content:` keys
  (`rosters.yaml:228-233`) [CHECKED], not an act's operands. A structured map on an act is
  ninth-operand territory, which v9 sends back through the ladder (`_part5.md:192`) [CHECKED].
- **The ladder, run:**
  1. **Superseded?** No.
  2. **Irrelevant?** No: demand (3) needs a per-subunit choice.
  3. **Answered by a design document?** No.
  4. **Answered by precedent? Yes.** `confer` reads an act-declared payload `term` that is in no
     operand of the closed eight and is never read by the typed cell: "an act-declared payload
     length, `create_record`'s `stages` precedent, since no operand of the closed eight … carries
     one" (`verb_table.yaml:177`, `writes_note`) [CHECKED].

  So `order` follows `term`'s route: declared by the act, read only by the host's `order_of_battle`,
  absent on every computed act. It carries the same grade, **[ASSUMPTION; medium; Jordan to
  correct]**.
- **Who carries it:** a hand-built act, or a player's act. A computed act carries none, so every
  company takes its kind's default.
  - An AI planner choosing roles is MB-08's "AI generals", LEAVE (`_part7.md:26-31`) [CHECKED-draft].
  - So **demand (3) is met for the player and the hand-built act only.** In computed play no faction
    chooses a formation (critic finding 7, accepted).
- **Gating:** a role is gated by `role_allowed(kind, role)` (`registry.py:22-24`) [CHECKED-draft]. An
  `order` naming a role the derived kind may not take refuses at the builder. The host turns that
  into the existing PARTY-GAP-shaped refusal, so the fold emits `march.refused` and never raises.
- **The defaults live in the module.** Role → shape and instructions are `TROOP_TYPE_ROLES` and
  `ROLE_SPEC` (`config.py:582-616`) [CHECKED-draft].
  - ⚠ The `levy` kind has no menu of its own. It falls back to `"any": ["Support", "Reserve"]`
    (`config.py:592`) [CHECKED-draft], and both are reserve postures.
  - So the module's default for an unarmed company is `shape: Line` with no role, which `build_army`
    accepts (`engine.py:373-377`) [CHECKED-draft].
  - Whether raw levies get a front-line role menu is MB data **[OPEN]**.

### 4.4 Where the army builder lives, and how the module uses it

1. **Move the builder into the module.** Move `build_army`, `_centered_line_cols` and `SUBUNIT_CAP`
   from `systems/mass_battle/sim/engine.py:99-173, :213-452` into a new `modules/mass_battle/army.py`.
   - **Callers stay unchanged:** leave a re-export in `engine.py`, so every harness caller is
     untouched: the workbench, `bat.py`, `tests/sim/gauge_mb.py`, and **22** source files under
     `tests/valoria` (`grep -rl build_army tests/valoria --include='*.py' | wc -l` → 22) [RAN]. The
     draft's 44 counted compiled `__pycache__` files (critic finding 18).
   - **No second construction path:** this moves the one that exists to the side of the seam the
     season can reach, per K-MB-2 (`MB_mass_battle.md:716`) [CHECKED-draft].
   - **Out of lane:** `tests/sim/gauge_mb.make_mixed_unit`, the third constructor (T-MB-19), is a
     harness object. Re-pointing it is the MB lane's.
2. **The morale defect is TS-2, tracked on its own** (part 1, §0 item 9). It does not wait for this
   move.
3. **`resolve_field` builds each side with `build_army`.**
   - **Specs:** `build_army(specs, name, faction='A'|'B', command=general.command,
     officers=officers)`, with one spec per company. Each spec is `{troop_type: kind_for_kit(kit,
     weight), troops, role|shape, officer, discipline, morale}`.
   - **Discipline and morale:** the preset plus the grade offset, computed in the module from
     `stats_for(kind)`. The module owns the presets and the kind; the host owns the offsets.
   - **Unit morale-start:** `_morale_start(stance, loyalty, gain)` (`massbattle.py:119-157`),
     unchanged except that its stance input now sees companies (§4.1).
4. **Span of control has one owner.** The host cannot pre-check it without a second copy of
   `build_army`'s check (`engine.py:304-345`). So the module gets one pure function beside it,
   `trim_to_command(specs, officers, command)`:
   - it drops the companies a commander cannot hold, smallest troops first, then by company id;
   - `build_army` calls it first, so the check and the trim are one rule in one file;
   - the dropped companies come back in the result as `unfielded`, a fact a witness can learn.
   - P2 (drafting) showed it is needed: an over-spanned side raises `ValueError` inside the fold.

### 4.5 What happens to the stub, to `Person.weight` as input, and to the 4/4 constants

| object | fate |
|---|---|
| `_MVP_SUBUNIT_SHAPE` (`massbattle.py:170-178`) | **deleted.** Shape, troop type, stance and unit type come from the kind and the role |
| `_MVP_UNIT_COMMAND` (`:182-186`) | **deleted.** Command comes from the general (`Officer` rule); discipline from preset plus grade |
| `_SEASON_FORCE_POWER` (`:196`) | **deleted.** Power comes from the kind's preset through `of_type` |
| `_MIN_TROOPS` (`:208`) | **deleted.** No side reaches the module without troops (§4.2) |
| `_weighted_unit` (`:213-230`) | **deleted** at TS-9, after the flip |
| the `[GAP …]` header line (`:32`) | **deleted.** The spec now exists, in code |
| `Person.weight` as battle input | **survives, scaled and filtered:** `troops = weight × men_per_weight` over cohort persons only |
| `_side_stance`'s weighting (`mass_battle.py:126-148`) | **kept, with its faction read widened** to `service_faction` (§4.1) |
| `MassBattleInput.weights` | **replaced** by `sides` (§4.2) |

### 4.6 How a field writes back

**Who lost** is read as today: `res.degree` and `res.result["parties"]`, with `Won` meaning the
defenders lost and `Lost` meaning the attacker did (`effects_combat.py:184-190, :221-226`)
[CHECKED-draft].

**On the losing side:**
- **Each company loses men:** `weight ← (weight × survivors_permille + 500) // 1000` (part 1, §2.8).
  - The per-mille is the losing side's engine survivor ratio (`attacker_size_pct` /
    `defender_size_pct`, read today at `:227`) [CHECKED-draft].
  - If the result is 0, the company's kit `_shift`s to the target rung's stores, and then
    `remove_person` runs, in the same `Change` (part 1, §2.8).
  - The `field_casualty_model` roster (`rosters.yaml:861`) keeps its meaning: `total` → weight 0;
    `none` → weight untouched.
- **Each named person** gets today's body write, unchanged.
- **Stance rows (morale and grudge)** as today, on every loser (`effects_combat.py:256-261`)
  [CHECKED]. They are now read back (§4.1).

**On the winning side: nothing**, per the ruled row ("nothing on the WINNING side",
`verb_table.yaml:682`) [CHECKED-draft]. J-5 asks whether winners take their engine casualties, and
whether either side gains experience.
- **Until Jordan rules, experience has no producer in computed play** (part 1, §0 item 5). M-MB-16 is
  narrowed, not closed.

**Weight on a remnant.** A company left at `weight == 1` is not a cohort (S9). It stops eating
(`world_q.py:860`) and stops fielding troops (part 1, §2.6). It keeps its `oblige`, kit and grade
until its service ends, and then it dissolves (part 1, §2.9). At the shipped raise of 2, any loss
between 25% and 75% leaves one. It is a residual (§8), not a branch.

### 4.7 Assembling from several settlements, and the commander drawn from persons

A faction assembles an army in four steps:
1. **Conscript** at each settlement in its seats' purviews, as far as each pool allows.
2. **Equip** with `transfer` from treasuries that `requisition` filled (hand-built or player acts, until
   a question source reaches a company's person-rung).
3. **Dispatch** the companies to one settlement, where they `move` themselves.
4. **March** from there.

Everything present at the origin under the marching seat's faction fights (§4.1), each company under
the holder of the seat it serves.

**NPC5's need, and what the muster rule does to it** (critic finding 16). NPC5 needs a council
commander's levies to give "his personal break with the faction's leader … a material consequence
beyond a changed vote" (`engine/season/cases/NPC5.yaml:172`) [CHECKED].
- **The draft fails it.** The draft mustered companies by the seat's faction, so a lord who defected
  and kept his seat left his men fighting for the faction he left.
- **`service_faction` meets it.** It reads the **holder's** faction (§4.1), so a lord who defects and
  keeps his seat takes his companies with him to the next field.
- **If he loses the seat,** his companies serve its next holder.
- ⚠ **A residual it exposes, not fixed here:** the attacker's faction is still read off the seat's
  label (`Office.faction`, `carriers.py:928`, through `faction_prop_id` at `sides.py:80`) [CHECKED].
  The defender's is read off the holder (`holder_faction_of`, used at `effects_combat.py:240`)
  [CHECKED]. A defected holder marching through his old seat raises his old faction's side, and his
  own companies are not on it. Two readings of "whose side" coexist in the tree today. That is the
  MB lane's to reconcile (§8.3).

---

## 5. WHAT IT CUTS AND WHAT IT SUPERSEDES

| item | verdict | reason |
|---|---|---|
| **IN-52** "the levy-to-field feed" (`_part4.md:134-140`) | **withdraw** | Its premise was "`levy` moves stores, not troops … a season field is one troops-sized subunit (J-18)". Demand (4) and the rename remove the first half, and demand (2) rules the second a stub. Nothing was built (part 1, §1 item 18) |
| **LF-1** "the feed bounds troops by the treasury, using the larder's ration" | **withdraw** | A company is a resident cohort, and the one larder already feeds it (`subsistence_draw`, `world_q.py:852-866`) [CHECKED]. A second ration from a treasury would feed the same mouths twice in a season: two ladders for one quantity (§8.3). MB's K-MB-6 keeps the bound with the stock as its input (`MB_mass_battle.md:732`) [CHECKED-draft]. Under P the stock is persons the larder feeds |
| **LF-2** "the defender's treasury is the nearest held rung's stores" | **withdraw** | It falls with LF-1 and LF-3, its only readers |
| **LF-3** "`_eff_march` debits the ration" | **withdraw** | The same double draw at the fold. A company that is not fed starves at MATTER like any cohort |
| the `field_provisioning` fixture and `settlements.provision` | **withdraw** (never built) | part 1, §1 item 18 |
| **the lanes' split, X-19** (`00_COMPARATIVE_ANALYSIS.md:152, :219`) | **resolved for SE's cut** | SE cut the bound; MB kept it. The comparative put SE's cut at rank (6) with "no statement reaches the ration bound" (`:219`) [CHECKED]. Under P the bound double-counts. **The draft's J-4 is folded into J-1:** if Jordan takes A (a stock nobody feeds), a ration rule returns as a feeding, not a surcharge |
| **IN-49** (`_part5.md:211-218`) | **keep, re-framed** | It is the store act's question source, and its subject is `requisition`. Its EXIT still reads "`levy` row executes" (`:215`) [CHECKED], which is J-3's collision. The troop verb needs its **own** question source (TS-7) |
| **H-49** `(Person, weight)` absent (`hole_register.yaml:558-568`) | **closed by TS-6** | casualties become its runtime writer, and `weight.changed` gains a producer |
| **H-170** the cohort weight | **untouched** | R-POOL leaves the cohort unwritten, and the pool's ceiling reads it (part 1, §2.2). The draft's finding 1 does not arise |
| **H-163**'s `levy` references (`hole_register.yaml:3543` and the row) | **re-named, not re-opened** | They name the store act. The rename's follow-through in `hole_register.yaml` (19 hits) and `requirements.yaml` (23 hits) is not done [RAN]. It is a separate IN edit, and it becomes a position here only if Jordan names the troop verb `levy` (TS-L) |
| **MB-08**'s #445 U-1, "musters with inputs beyond headcount" (`_part7.md:28`) | **closed by TS-5/TS-8** | kind, grade and commander are those inputs. U-2 and U-6 **stay LEAVE** |
| **IN-07/SE-02** (`_part4.md:120-133`) | **unaffected**, except that its design document's §5 is withdrawn | E1–E6 stand |
| **IN-12 step 9 `train`** (`_part5.md:73`) | **not depended on as planned** | J-13's answer (iii) excludes case-less persons, so drill does not reach a company (part 1, §0 item 5) |
| **FA-01** (`_part7.md:119-126`) | **depended on** | a faction head seated is a head who can conscript `via` his seat and march |
| **K-MB-1** (rung stock), **K-SE-13** (both shapes), **K-FA-13** (whole-cohort commit), **K-IN-13**'s open form | **superseded as forms** | their direction is kept: troops come from settlements, are fielded, and are drawn down. K-MB-1's rung-held resource survives as the pool |

**The research rows this design closes, or narrows, when built:**
- **Closes:**
  - **MB:** M-MB-2 (composition), M-MB-6 (the population's men as soldiers), M-MB-15 (the levied
    stock: the pool), M-MB-17 (composition chosen, at the hand-built and player act).
  - **SE:** M-SE-9. **FA:** M-FA-10. **IN:** M-IN-12 and M-IN-13.
  - **PC:** M-PC-12's cohort half.
  - **Composites:** C-ARM-2 and C-ARM-4, and C-ARM-3's naming half.
- **Narrows:**
  - M-MB-1 (the scale becomes one number, `men_per_weight`, Jordan's);
  - M-MB-3, M-NPC-13 and M-IN-1's commander half (who commands is live; how well waits on R-C-1);
  - M-MB-16 (no computed producer until J-5 or J-13).
- **Collisions resolved:** **X-2**, by a rung-held pool raised into persons. **X-19**, by cutting the
  bound under P.

---

## 6. DATA

Facts the engine reads go in registries code opens at runtime (CLAUDE.md §0.05 clause 1). None goes in
this document. Every number below is a sourced fixture with a register row, or marked
**[OPEN — Jordan tuning]**. The **falsifier value** is what §7's runs fix the fixture at. It is a
control setting, not a proposal for the shipped value.

| fact | home | shape | value |
|---|---|---|---|
| the recruit pool | `rosters.yaml: matter_kinds`, a new row `recruits` (an open registry by design, `:1279-1290`) [CHECKED] | whole weight units in a settlement rung's `stores` | derived: filled to the ceiling at world-gen, then regrown (part 1, §2.3) |
| kinds no store act may move | `rosters.yaml: immovable_kinds` (new) | list of `matter_kinds` ids; the loader refuses an id not in `matter_kinds` | `[recruits]` |
| the ceiling's share | `data/fixtures.py`, `recruit_share`, with a hole-register row and a sweep | int, per-mille of the base | **[OPEN — Jordan tuning]**. Sweep 500 / 1000 / 2000. Falsifier value **1000** |
| the regrowth rate | fixtures, `recruit_regrowth`, with a row and a sweep | int, per-mille of the ceiling per season | **[OPEN — Jordan tuning]**. Sweep **0 (the control)** / 250 / 1000. Falsifier value **250** (a ceiling of 2 regains 1 a season) |
| men per weight | fixtures, `men_per_weight`, with a row and a sweep | int | **[OPEN — Jordan tuning]**. Sweep 1 (today's scale, the control) / 120 / 250. Falsifier value **250** (part 1, §2.8) |
| the raise size | fixtures, `conscript_amount`, an H-94 operand default | int, weight units | **2**: the smallest company that is a cohort (S9), derived, not tuned. A larger default is Jordan tuning |
| the service term | **reuses** `oblige_term` (`fixtures.py:818`, shipped 4) [CHECKED] | — | the draft's J-7, answered in §9. ⚠ The fixture now sets service, sentence (H-173) and the levy's term. H-173 already tracks that sharing |
| the kind → stat mapping | **stays** `TROOP_TYPE_STATS` (`registry.py:39-57`) [CHECKED] | — | — |
| the kind → kit mapping | **stays** `TROOP_LOADOUT` (`equipment/__init__.py:21-36`) [CHECKED], the one owner; `kind_for_kit` beside it; the unarmed kind `levy` a constant beside it | — | the draft's season `troop_kinds` table is **dropped** (critic finding 5). Its kit proposal contradicted the owner: it gave `levy` an empty kit where the owner says `light_cut`/`none`, and it excluded `knights_templar` as "cavalry's kit" where the owner says `heavy_blunt`/`heavy` |
| equipment matter kinds | `rosters.yaml: matter_kinds` | new rows, one per weapon and armour class `TROOP_LOADOUT` names, `arms_<class>` and `armour_<class>` | names mirror `ARSENAL`/`ARMOURY` keys (`weapons.py:36-45`, `armour.py:37-40`) [CHECKED-draft]. **[OPEN]**: one kind per class or a coarser three. **No producer exists**: `site_yield` has no arms row (`rosters.yaml:2042-2075`) [CHECKED], so arms enter only as world-gen stores until an SE row adds one **[OPEN — SE content]** |
| grades | `rosters.yaml: troop_grades` (new) | ordered rows `{discipline: +d, morale: +m}`, row 0 = `{0, 0}` | **[OPEN — Jordan tuning]**. Proposal: raw 0/0, drilled +1/+1, seasoned +1/+2, veteran +2/+2 |
| the grade key | `verb_capability` | one key, reserved | name **[OPEN]**: `soldiering` proposed. It has no writer until J-5 or J-13 changes |
| survivor conversion scale | **reuses** `condition_scale` (`fixtures.py:182`) [CHECKED] | — | 1000 |
| `field_army` | fixtures, temporary arm roster `single_line \| order_of_battle` | — | shipped `single_line` until TS-8; deleted at TS-9 |

---

## 7. BUILD ORDER, EXITS AND FALSIFIERS

Positions use v9's form. Every EXIT is an execution artifact, and every FALSIFIER names its control arm.
**Golden re-records are declared at the position that causes them.** Unless a position says otherwise,
its runs fix `recruit_share = 1000`, `recruit_regrowth = 250`, `men_per_weight = 250` and
`conscript_amount = 2` (§6).

### TS-1 · move `build_army` into `modules/mass_battle/army.py`
- STATE: unblocked      LANE: MB
- EDITS: `modules/mass_battle/army.py` (new home), `systems/mass_battle/sim/engine.py` (re-export only)
- EXIT: `python3 tools/ci_golden_modes_check.py` digests unchanged, and the 22 `tests/valoria` files
  that import `build_army` are green.
- FALSIFIER: any harness digest moves → not a pure move. Control: the same command on the parent commit.

### TS-2 · `build_army` honours the troop type's morale preset — independent, gated on nothing here
- STATE: **unblocked; lands before or without every other position**, in
  `systems/mass_battle/sim/engine.py:427-428` where the code is today (or in `army.py` if TS-1 has
  landed)      LANE: MB
- WHAT: give a subunit its type's preset morale when the spec sets none and the type has a preset.
  Fall back to the Unit's morale only for a type with no preset (DG-4's intent: no `None`).
- EXIT: the drafting probe prints `levy … morale 2` and `heavy_infantry … morale 5`.
- FALSIFIER: the probe still prints 6 → not fixed. Control: the same probe on the parent commit, which
  prints 6 [RAN at drafting].
- GOLDENS: **declared mover** for any harness battery building a typed troop through `build_army`. Which
  batteries do is **[UNVERIFIED]**: read `bat.py`'s specs at the position.
- TRACKING: no register row tracks this defect today [RAN, part 1, §0 item 9]. The position is its
  tracking.

### TS-3 · the recruit pool (R-POOL)
- STATE: unblocked      LANE: SE (IN)
- EDITS: `rosters.yaml` (`recruits`, `immovable_kinds`), `queries/world_q.py` (`recruit_ceiling`,
  `movable`), `loop/matter.py` (the capped credit, after yield), `loop/effects_governance.py` and
  `loop/effects_economy.py` (the `movable` declines), `loop/effects_shared.py` (`_shift`'s
  assertion), `data/fixtures.py` (`recruit_share`, `recruit_regrowth`), `harness/populated.py` (the
  world-gen fill), `hole_register.yaml` (a row per fixture)
- EXIT: `populated.build_realm(0)`: every settlement's `recruits` equals `recruit_ceiling`, which is 2
  at the shipped data; four seasons run through the real driver.
- FALSIFIERS, each with its control:
  - **(i) It regrows at the stated rate.** Debit a settlement's pool to 0 by hand. At the next three
    MATTERs it reads 1, 2, 2. **Control:** `recruit_regrowth = 0`, where it reads 0, 0, 0.
  - **(ii) It never passes its ceiling.** Over 8 seasons at `recruit_regrowth = 1000`, assert `recruits
    ≤ recruit_ceiling` at every MATTER, at every settlement, and assert that the check ran 37 × 8
    times (CLAUDE.md §0.1 pt 2). **Control:** remove the `min`, and the same run fails at the first
    MATTER.
  - **(iii) Settlements with different cohorts differ.** Build the realm with two settlements' cohorts
    at weights 2 and 4. The realm builds with every cohort at 4 (probe: 37 cohorts, total weight 148,
    no row refused against capacities 4 to 9) [RAN]. Their ceilings are 2 and 4. **Control:** equal
    weights give equal ceilings.
  - **(iv) A man is not goods.** A hand-built `requisition` of `recruits` → `requisition.refused`, and
    both rungs' stores are unchanged. **Control:** the same act on `grain` executes.
  - **(v) The scene tax is measured, not assumed.** `python -m engine.season.harness.aperture 4 0`
    before and after. A per-verb shift in `requisition`'s refusals is declared with its count.
- GOLDENS: **declared mover.** The world-gen fill writes every settlement's `stores`, so every realm
  `content_hash` moves at build. **The re-pin is intended.** A full pool writes nothing at MATTER, so
  the per-season traces move only through the hash.

### TS-4 · `conscript` (row, effect, gate basis, `founding` clause)
- STATE: after TS-3 (it needs a seat with `dispatch`; FA-01's seating is landed)      LANE: IN (SE)
- EDITS: `verb_table.yaml`, `loop/effects_governance.py` (`_eff_conscript`), `state/gate.py` (basis
  `conscription`; the `founding` clause), `data/fixtures.py` (`conscript_amount`),
  `hole_register.yaml` (the fixture's row)
- EXIT: `populated.build_realm(0)`, one season through the real driver, with one hand-built
  `conscript` act injected at RESOLVE (as `tests/test_u7_remit.py` injects remit acts):
  - `conscript.taken` is in `w.log`;
  - a new `Person` exists at the settlement with `weight == 2` and a live `oblige` to the seat;
  - the settlement's `recruits` fell by 2.
- FALSIFIERS, on one tree and one seed:
  - **(i) R-POOL holds, byte for byte.** The population cohort's `Person` (its `weight`, `stance`,
    `tenures` and `body`) and its row of `subsistence_draw` are identical before and after the act,
    compared by `repr`. The settlement's total `demanded` rises by exactly the company's `want`.
    **Control:** the draft's split design would fail the first clause.
  - **(ii) Men are conserved.** `recruits` plus Σ company weight at the settlement is unchanged across
    the act.
  - **(iii) Refusals keyed per clause:**
    - `amount = 3` against a pool of 2 → `conscript.refused`, and nothing moves;
    - `amount = 1` → `conscript.refused`, because a company of 1 is not a cohort;
    - a seat without `dispatch` → `conscript.unauthorized`.
  - **(iv) The world without the act.** No injected act → `World.content_hash()` equal to TS-3's,
    **unless** the row is formable by the chooser. In that case the hash moves by formation (the
    H-163 crowding shape), and the move is **declared** with the measured per-verb shifts and the
    count of `inferred` claims the companies receive through `_ch_post_remit` (§4.1).

### TS-5 · the order of battle at the seam, behind `field_army` (shipped `single_line`)
- STATE: after TS-1, TS-2, TS-4      LANE: MB (IN)
- EDITS: `queries/world_q.py` (`service_faction`; the `mustered` clause), `seam/wrappers/mass_battle.py`
  (`order_of_battle`; `_side_stance`'s faction read), `queries/inputs.py` (`sides`),
  `modules/mass_battle/massbattle.py` (`resolve_field` → `build_army`), `modules/mass_battle/army.py`
  (`trim_to_command`), `modules/mass_battle/equipment/` (`kind_for_kit`), `rosters.yaml`
  (`troop_grades`, kit `matter_kinds`), `data/fixtures.py` (`men_per_weight`, `field_army`)
- EXIT, in two arms on one tree:
  - **(a) `field_army: single_line`:** the realm's `content_hash` after four seasons equals TS-4's,
    and `mustered(w, s, f)` is unchanged at every settlement `s` and faction `f` of the shipped world,
    the two shipped `oblige` edges included (§4.1).
  - **(b) `field_army: order_of_battle`:** a seeded season in which a company is conscripted, equipped
    by `transfer` with one kit, and marched → the field's order of battle shows `kind_for_kit`'s kind
    with its `TROOP_TYPE_STATS` power and discipline.
- FALSIFIERS:
  - **Kit reaches the field.** Two arms identical to the tick of the `transfer`, by construction. Arm X
    has the transfer; arm Y has none, so its company derives the unarmed kind. Over N ≥ 50 seeds, at
    `men_per_weight = 250`, the band distributions of the two arms' fields must differ (an exact test,
    declared at the position). **Control:** equal distributions → kit does not reach the field. At
    today's scale (1) the test would be blind, because both arms rout every run (critic finding 15).
  - **The vassal rule.** In a hand-built Crown-vs-Löwenritter field at NPC-070's place, she is on the
    Löwenritter side only. **Control:** the draft's unrestricted clause puts her on both.
  - **Morale is read back** (§4.1).

### TS-6 · write-back, dissolution and salvage
- STATE: after TS-5      LANE: MB (IN)
- EDITS: `loop/effects_combat.py` (`_eff_march`), `write_matrix.yaml` (ENC on `(Person, weight)`),
  `queries/world_q.py` (`is_company`), `loop/matter.py` and `loop/effects_*` `release` (dissolution)
- EXIT:
  - a seeded lost field lowers each losing company's weight by the integer rule;
  - the kit of a destroyed company is on the target rung;
  - a company whose term matures dissolves: its weight is back in `recruits` up to the ceiling, its kit
    is on the settlement rung, and `company.dissolved` names what returned and what was absorbed;
  - the world's weight, `recruits` and stores sums move by exactly the declared sources and sinks.
- FALSIFIERS:
  - `field_casualty_model: none` (the existing control arm, `rosters.yaml:861`) → no weight moves.
  - Remove the salvage clause → the stores sum falls, because `remove_person` pops the person-rung
    (`world.py:770-773`) [CHECKED]. So the clause is needed.
  - `oblige_term: None` (H-159's control arm) → no term matures and no company dissolves.
  - A population cohort that obliges itself and later releases → it is **not** dissolved, because
    `is_company` is false.

### TS-7 · a question source that forms `conscript` in computed play
- STATE: after TS-4      LANE: SE (IN)      R: R-04, R-05 (a verb that executes)
- WHAT: IN-49's shape for men instead of goods: a referent that is a settlement in the seat's purview
  with a full pool. The trigger is **[OPEN]**: a threat claim (`march.declared` or `field.lost` heard
  of), or the seat's own need. Design first, as IN-49 does.
- EXIT: `python -m engine.season.harness.aperture 4 0` shows `conscript` executed ≥ 1 with `via`.
- FALSIFIER: a `conscript` formed over a settlement outside the seat's purview → fail. `conscript`
  always refused → not built.
- ⚠ If J-3 names the verb `levy`, this EXIT reads "`levy` executed", which is IN-49's EXIT word for
  word (`_part5.md:215`) [CHECKED]. TS-L must land first.

### TS-8 · flip `field_army` to `order_of_battle`
- STATE: after TS-5, TS-6, TS-7. Without TS-7 no company exists in computed play, and under part 1 §2.6
  every attacker has no troops, so the realm stops fighting.      LANE: MB
- EXIT: `aperture 4 0` shows `march` executed, with fields whose order of battle holds more than one
  subunit, in at least one seeded world.
- GOLDENS, **declared plainly**: every realm hash a `march` reaches moves. That covers
  `engine/season/runs/` (TRACE, the run artifacts), the `test_season_shape.py` pins that count `march`
  outcomes or `field.*` kinds, and the realm hashes pinned in `engine/season/tests`. **The re-pin is
  intended.** The control is the same command at `single_line` on the same commit.

### TS-9 · delete the stub
- STATE: after TS-8 is accepted      LANE: MB
- EDITS: delete `_weighted_unit`, `_MVP_*`, `_SEASON_FORCE_POWER`, `_MIN_TROOPS`, the `[GAP]` line and
  the `field_army` fixture with its `single_line` arm.
- EXIT: `grep -n "_weighted_unit\|_MVP_SUBUNIT_SHAPE\|field_army" -r engine modules` → 0, and the files
  covering the seam are green.
- FALSIFIER: the TS-8 realm hash moves → the deletion changed behaviour.

### TS-10 · experience read at the builder — BLOCKED on J-5 or a change to J-13
- STATE: blocked. No computed act writes a company's grade (part 1, §0 item 5)      LANE: MB (NPC)
- EXIT, on hand-set grades: two companies of one kind and weight, one at grade 1, fight the same field
  over N ≥ 50 seeds at `men_per_weight = 250`, with different band distributions. At grade 0 the field
  reproduces the kind's preset exactly.
- FALSIFIER: identical distributions → grade does not reach the field. Control: grade 0 on both.
- What unblocks it: J-5 (c) (a fought field writes a grade step), or J-13 revisited so that `train`
  writes a vocation `verb_capability` names on a person without a case.

### TS-L · the `levy` follow-through — ONLY if J-3 names the troop verb `levy`
- STATE: before TS-4, if at all      LANE: IN
- EDITS:
  - `engine/season/requirements.yaml`: R-04's acceptance "a `levy` executes with `Act.via` set"
    (`:734-735`) and the historical refusal counts (`levy.refused 19 + levy.unauthorized 4`,
    `:771-772`) [CHECKED] are re-keyed to `requisition`, the act they measured;
  - `hole_register.yaml`'s 19 `levy` hits are re-keyed the same way;
  - v9 IN-49's EXIT (`_part5.md:215`) [CHECKED] is re-keyed;
  - the r2 ruling note at `world_q.py:910-914`, *"ruled `levy` deleted (§A.20)"* [CHECKED], is
    annotated: it names the policy clause, not the troop verb.
- EXIT: `grep -n "levy" requirements.yaml hole_register.yaml` returns only rows about the troop verb.
- FALSIFIER: after TS-4 lands under the name `levy`, R-04's acceptance reads met while `requisition`
  has never executed → the follow-through was skipped.

---

## 8. NERS PASS ON THE DESIGN (`skills/ners/SKILL.md`, instrument A)

`[SELF-AUTHORED — bias risk]`. An independent critic attacked the draft (18 findings; reconciliation at
the end). R-POOL then changed the design's core. The re-based design has not been attacked by anyone
but its author. An independent reviewer should start with §2.1 (the pool's home), §2.9 (dissolution)
and §4.1 (`service_faction`).

**Grade: paper.** Probes run:
- **At drafting:** P1 (the morale preset), P2 (the span check raises on an over-spanned side) and P3
  (role gating).
- **In the correction pass:** the shipped `oblige` edges (§4.1), and the realm built with every cohort
  at weight 4 (TS-3 (iii)).

Nothing in the season was run against the design, because none of it exists.

### 8.1 N — the N-line ledger, six directions, attacks run

| object | N-line | attack | verdict |
|---|---|---|---|
| **`recruits` (the pool)** | cut it, and R-POOL has no carrier: troops come from the cohort (forbidden) or from nothing | could an existing quantity carry it? `envelope` represents the population twice; a Site's `condition` is fabric and a fraction; a new field amends `04:255` (part 1, §2.1) | **HOLDS.** Bottom-up (settlement → field), vertical (rung → person → field) |
| **`recruit_ceiling`** | cut it, and the pool regrows without bound, so a quiet town banks an army | is the ceiling a second copy of `population`? No: it reads unbound resident cohorts only, a narrower set, for a different purpose | **HOLDS.** Narrowed: equal everywhere at the shipped data (H-170) |
| **`immovable_kinds` / `movable`** | cut it, and `requisition` carries men into a treasury as goods | does anything else stop it? No: `_shift` moves any kind | **HOLDS.** Narrow: one kind today |
| **`conscript`** | cut it, and no act turns a settlement's pool into men who fight | is anything else a producer of fighting men? `requisition` moves goods; `commit` makes members and is belief; `oblige` is the person's own act | **HOLDS.** Bottom-up, vertical, diagonal (SE → MB) |
| **the company as a `Person`** (P) | cut it for A, and the army cannot desert, defect, witness its defeat or eat | does A carry any of these? A stock has no `release`, no ledger and no body (AX-1) | **HOLDS, NARROWED:** desertion by `release` is reachable, not shown |
| **`kind_for_kit`** | cut it for a stored kind, and two owners exist for one fact | does any reader need a stored kind? The builder needs one at field time, and a function over the kit answers then | **HOLDS.** It lives with its owner, `TROOP_LOADOUT` |
| **the grade on `capability`** | cut it, and a host that survived three fields is the host it was when raised | is there a producer? **No, in computed play** (J-13 (iii); J-5) | **FAILS in computed play; HOLDS as a carrier.** Disqualifier 2, no producer, fires. Kept because J-5 (c) or a J-13 change gives it one with no further object |
| **the commander** | cut it, and who leads changes nothing | does it change anything before R-C-1? Yes: the span check divides a side's companies by commander | **HOLDS, NARROWED:** identity now, capacity at R-C-1 |
| **`service_faction` + the `mustered` clause** | cut them, and a conscripted company never stands on a side | could the conscription open a `commit` instead (D's route)? That imposes a belief, and D is ruled out by R-POOL. Could `sides_of` read it directly? Attacker only: two copies | **HOLDS.** Horizontal: one owner for both sides and for morale |
| **the `_side_stance` edit** | cut it, and the morale row the fold writes on a company is never read | read/write asymmetry (CLAUDE.md §0.1 pt 1) | **HOLDS** |
| **`is_company` + dissolution** | cut it, and every company persists forever, so persons grow without bound | is persistence acceptable? Only if the pool stopped refilling. Under R-POOL it refills | **HOLDS.** Narrow: the first reader of why an edge was opened |
| **the gate basis `conscription`** | cut it, and the company's `oblige` (owned by the company, not the actor) is refused at F3 | `T-m` needs the actor to be the owner; `determination` needs a judging seat | **HOLDS** |
| **`men_per_weight`** | cut it, and every field is fought at single digits against a floor of 80 | disqualifier 5, "a flat bonus"? No: a unit conversion applied to every side alike | **HOLDS** |
| **`trim_to_command`** | cut it, and an over-spanned side raises inside the fold (P2) | could the host trim? Only with a second copy of the span rule | **HOLDS** |
| **the salvage clause** | cut it, and a destroyed company's kit is destroyed with its person-rung (`world.py:770-773`) | is that acceptable? Then it needs a receipt, and the clause is the receipt | **HOLDS** |
| **the `order` key** | cut it, and no act can choose a formation per company (demand 3) | is it a ninth operand? Yes; ladder step 4, `confer`'s `term` (§4.3) | **HOLDS, NARROWED** to player and hand-built acts |
| **`field_army`** | cut it, and TS-5 cannot ship hash-neutral | scaffolding | **HOLDS, TEMPORARY.** Deleted at TS-9 |

**False N-lines found in what this design withdraws:**
- **LF-1 (the ration bound):** "a field unprovisioned fights" is false under P. The larder already feeds
  a company. **Disqualifier 1 fires: the carrier already exists.**
- **LF-3 (the ration debit):** same disqualifier.
- **`_SEASON_FORCE_POWER`:** "headcount no longer feeds quality" is false. `TROOP_TYPE_STATS` is the
  carrier of quality per kind.

**False N-lines in my own additions:**
- **The grade, in computed play** (above): disqualifier 2 fires. It is kept as a carrier with a named
  unblocking condition, not as a working mechanism.
- **`troop_grades`:** looked at hardest as a possible flat bonus (disqualifier 5). It is a second index
  into the same two stats `TROOP_TYPE_STATS` sets, not a bonus beside them. If Jordan rules one offset
  per grade, it collapses to one column.

### 8.2 R — both halves

- **R-COMPLETE:**
  - **The extremes walked, on paper:**
    - an empty pool (`conscript.refused`);
    - a pool at its ceiling (no write);
    - a company at weight 1 (the remnant, §4.6);
    - a side with no troops (Unopposed or PARTY-GAP);
    - an over-spanned command (trimmed);
    - a company whose term matures (dissolved);
    - `recruit_regrowth = 0` (a pool that never refills: war exhausts a settlement, permanently).
  - **The draft's open extreme closes under R-POOL.** War no longer drains the population.
  - **The new residual:** at the shipped raise of 2, the remnant is common (§4.6).
- **R-VARIETY:** a faction chooses where to raise, how many (up to each pool), how to equip, whom to put
  in command, and, at the player or hand-built act, each company's role. **PASS on the shape; NOT
  SCORABLE on the tree** until TS-8. In computed play only *where*, *how many* and *who commands*
  vary.
- **R-CHOICE:** the draft found the levy amount had no cost. **Under R-POOL it has three:**
  - food (a company eats from the settlement's larder, part 1, §2.5);
  - the pool (a settlement raised dry cannot answer the next threat for `ceiling / growth` seasons);
  - crowding (`migrate` into the settlement is refused sooner).

  ⚠ **The residual cost that is missing is upkeep per man** (§4.1). A seat pays one person's upkeep
  for a company of any size. Scaling `_renewals`' count by weight is the one-owner fix. It changes
  what an army costs a treasury, and it is listed under J-1's consequences, not built here.
- **R-WORLD:**
  - A raised company eats, witnesses its lord's orders, may desert by `release`, and goes home when its
    term runs out.
  - A defeated lord's companies shrink, their kit lies where they fell, and the place's holder may
    `requisition` it.
  - A settlement raised dry is a weakness its neighbours can learn of through `stores.changed`.

  Each is an Event a witness can learn, with no player involved. **PASS on the shape**; reachable,
  none observed.

### 8.3 S — six directions, pause, methodology

| direction | carried by | verdict |
|---|---|---|
| **S-UP** (a demand filtered by a person) | a threat reaches the seat as a claim; whether the holder conscripts is his choice (TS-7) | **PASS on the shape**, gated on TS-7 |
| **S-DOWN** (an opportunity to a party with no post) | a company is a party with no post; its `release` and its answer to a `dispatch` are its own | **PASS on the shape** |
| **vertical** (rung ↔ person ↔ field) | `recruits` → weight → `troops = weight × men_per_weight`, one conversion; write-back through `weight` and back to `recruits` on dissolution | **PASS** |
| **diagonal** (SE matter → MB field) | `requisition` → `transfer` → `kind_for_kit` → `of_type` | **PASS on the shape**; no computed act reaches `transfer` to a company |
| **lateral** (sibling verbs) | `conscript` and `requisition` share the authority conjunct, the stores threshold and the keyed-refusal split | **PASS** |
| **horizontal** (both sides of one field) | one `mustered`, one `service_faction`, one `order_of_battle`, one `build_army` | **PASS**, with one residual: the attacker's faction is read off the seat's label and the defender's off the holder (§4.7) |
| **pauses correctly** | the field is resolved inside the fold, as today. A played field is not designed here (M-MB-5) | **N-A** |
| **methodology** | **Resolved:** the ration bound would have fed the same mouths twice. **One rounding rule:** half-up per-mille for the ceiling, the growth and the survivors. **Two replenishing clocks:** yield (no ceiling) and the pool (a ceiling); the same write, a different bound, stated. **Still open:** an individual's casualty is `int(body × float)` (`effects_combat.py:254`), a second conversion for one survivor ratio | **FINDINGS → TS-6** |

### 8.4 E — last, as a ratio

- **N and R found** a pool and a verb that hold, a carrier that holds, several narrowed lines, and one
  failure in computed play (the grade).
- **The design adds about 22 objects and cuts 6 on disk** (part 1, §3.5).
- **E-OVERHEAD: NARROWED, not passed.** Every addition carries a fact the engine reads or a reader of
  one, and none is a parallel scheme. But additions outnumber cuts by more than three to one, so the
  case for E rests on legibility, not on object count.
- **E-LEGIBILITY: PASS on the shape.** A player sees men raised from a town's pool, the town's pool
  empty and refilling, men armed from a treasury, led by a named holder, lost in a field, and sent home
  when their term ends. Each outcome traces to one of those acts.

### 8.5 The design's own falsifier

The design's discipline is that **no fighting man exists unless a conscription raised him from a pool,
and none vanishes without a receipt.**
- **Hits:** named persons fight without being raised. They are the general and his officers.
- **Licensed narrowly** by part 1 §2.6: they command and are not troops.
- **Borderline:** guard cohorts and convicts in service (§4.1) are troops not raised from a pool. They
  pass by tracing (an `oblige` they or a bench opened), and they are named as residuals.

### 8.6 Self-audit

- **9a, backward propagation.** Part 1 §0 now carries R-POOL, the Layer 1 amendment, the unreachable
  axes, the morale defect and `service_faction`. §5 marks H-170 untouched and IN-12 step 9 not
  depended on. §6 drops `troop_kinds`. §9 marks J-2 answered. The draft's "§0 says 'in part' for
  M-MB-3 and M-MB-16" was checked: both now read "narrowed".
- **9b, §3 on my own additions:** done in §8.1. One disqualifier fired (the grade in computed play).
- **What an independent reviewer would add:** a measured check that companies do not crowd the chooser,
  and of how many claims `_ch_post_remit` adds. Both are TS-4 (iv)'s, and neither was run.

---

## 9. DECISIONS FOR JORDAN

**CLAUDE.md §0's ladder, run per item** (critic finding 9). Only what survives all five steps is
escalated.

| id | the decision | ladder | escalated? |
|---|---|---|---|
| **J-1** | the troop body under the pool | not superseded; not irrelevant; no document decides it; no precedent fits; architecture leans to P but A amends a different Layer 1 line and is cheaper in objects | **yes** |
| **J-2** | does raising troops draw down the population | **step 1, superseded by R-POOL** (2026-10-16): the cohort is not reduced, and the pool replenishes | **no — ANSWERED** |
| **J-3** | the two verbs' names | not superseded; a name is Jordan's (the brief reserves it) | **yes** |
| **J-4** | do LF-1..LF-3 stand | step 5, architecture: under P the larder feeds the company, so a second ration double-counts; under A a feeding rule returns. Its answer follows J-1 (`00_COMPARATIVE_ANALYSIS.md:219`: "no statement reaches the ration bound") [CHECKED] | **no — folded into J-1** |
| **J-5** | what a fought field writes beyond the losers' casualties, morale and grudge, and whether veterans outlive their service | not superseded; it overturns ED-IN-0279's ruled row if anything changes | **yes** |
| **J-6** | who counts as troops | step 4, precedent `24f` (part 1, §2.6) | **no — answered: cohort persons only** |
| **J-7** | the service term | step 5: one fixture for every service; H-173 already tracks that it also sets sentences. No materially different game | **no — answered: reuse `oblige_term`** |
| — | the pool's ceiling base, the regrowth form, the return rule | step 5 (part 1, §2.2, §2.3, §2.9). The return rule's alternative (veterans persist) is an experience question, folded into J-5 | **no — answered in text** |

**The escalated decisions:**

| id | the decision | options, and what each does to the game | default here | what waits on it |
|---|---|---|---|---|
| **J-1** | **what a troop is, once raised from the pool** | **(P) a company `Person`** minted from the pool: armies are people who eat at home, can desert, witness and die. Layer 1's unit sentence holds. **Its muster line (`04:792`, `:802`) is amended** so a person with no `commit` can stand for the faction his lord serves. · **(A) a troop stock** on the seat's rung, moved from the pool: no persons, no chooser load, no muster amendment. It **amends** §C.5.1's unit sentence and §C.5's `claimants : PersonId[]`. Nobody eats, so a ration rule (J-4's LF-1/LF-3) returns as a feeding. Troops can be counted in men, with no `men_per_weight`. · **(B) a typed troop row:** a unit class; amends §C.5.1 and T-l. **The contrary reading of statement 1 belongs here:** "their own resource" reads toward "a rung-held carrier" (`00_COMPARATIVE_ANALYSIS.md:202`) [CHECKED], and "the field's troop count should come from a levied stock, not from a conversion of summed weight" (`MB_mass_battle.md:434`) [CHECKED]. Under the pool, P meets the first and most of the second: the count comes from raised companies, not summed member weight, but through one conversion. A meets both in full. **Also under J-1:** whether upkeep scales by weight (§8.2) | **P** | everything in §7 from TS-4 on |
| **J-3** | **the names** | **The store act:** `requisition` (provisional, in the tree; the ordinary word for goods taken for an army or a state) · `tax` (a regular, coin-shaped due, which this act is not) · `tithe` (a tenth, and Church-specific). **The troop verb:** `conscript` (working name; no hit in `engine`, `modules`, `systems`, `references` or `tools`, `git grep -i conscript`) [RAN] · **`levy`**, Jordan's own word, which collides with: R-04's acceptance text "a `levy` executes with `Act.via` set" and its historical store-act refusal counts (`requirements.yaml:734-735`, `:771-772`) [CHECKED]; IN-49's v9 EXIT "`levy` row executes … `levy.taken` in `w.log`" (`_part5.md:215`) [CHECKED], so the troop verb would mark the store act's requirement met; 19 `hole_register.yaml` hits [RAN]; the r2 note that "`levy`" was "ruled deleted (§A.20)" (`world_q.py:910-914`) [CHECKED]; and the module's `levy` troop type (`registry.py:41`; `equipment/__init__.py:22`) [CHECKED], one word with three meanings. **Choosing `levy` makes TS-L a position that lands before TS-4** | **`requisition`; `conscript`** | IN-49's text; TS-4's row; TS-L |
| **J-5** | **what a fought field writes, and whether veterans persist** (ED-IN-0279's ruled row: losses only, nothing on the winner) | **(a) as ruled:** winners untouched; no computed experience; companies dissolve at term's end (part 1, §2.9). · **(b) winners take their engine casualties too.** · **(c) survivors of both sides gain one grade step** (war teaches): the only computed producer of experience while J-13 (iii) stands. · **(d) veterans persist:** a company whose service ends stays a resident cohort with its kit and grade, a reserve the seat can re-engage by the company's own `oblige`. Persons then grow with every raise, and the ceiling must exclude them | **(a)** until ruled. **Recommended: (b) + (c)**, since statement 1's "experience" most naturally includes war's; (d) only with (c), since without a grade there is nothing for a veteran to keep | TS-6's write set; TS-10; M-MB-16 |

**Tuning values, not decisions:** `recruit_share`, `recruit_regrowth`, `men_per_weight`, a
`conscript_amount` above 2, the equipment kinds, the `troop_grades` ladder, and the arms producer (§6).
Each is **[OPEN — Jordan tuning]**, with a register row and a sweep at its position.

---

## 10. LIMITS

**Re-opened in the correction pass (`[CHECKED]` above):**
- **Season code:** `hole_register.yaml` (H-170, H-171, H-173); `cohorts.yaml`;
  `state/carriers.py` (Person `:700-721`, Office `:885-928`, Rung `:1040-1068`, Term);
  `queries/world_q.py` (`subsistence_draw` `:852-866`, the r2 note `:904-914`, `population`,
  `capacity`, `leaders`, `mustered`, `faction_holding`, `holder_faction_of`, `upkeep_of`);
  `queries/faction_q.py:95-110`; `seam/wrappers/mass_battle.py` (`:72-93`, `_side_stance`);
  `loop/effects_combat.py:240-262`; `loop/effects_economy.py:280-308`; `loop/effects_shared.py:117-128`;
  `loop/matter.py` (`:98-187`, `:480-636`); `loop/census.py:60-110`; `loop/sides.py:60-86`;
  `epistemic.py:460-486`; `data/fixtures.py` (`:180-183`, `:816-818`); `offices.yaml:185-193`,
  `:586-592`; `harness/populated.py` (`:436-442`, `:1325-1339`); `state/world.py:748-773`;
  `verb_table.yaml` (`confer` `:174-177`, `oblige` `:746-751`, `transfer` `:1205-1212`, `release`
  `:828-838`); `rosters.yaml` (`:228-233`, `:1258-1330`, `:2042-2075`); `write_matrix.yaml` (the Rung
  rows); `requirements.yaml:730-736`, `:768-773`; `cases/NPC5.yaml:170-173`.
- **Mass-battle code:** `equipment/__init__.py:18-37`; `troop_types/registry.py:39-57`;
  `hierarchy/units.py:2706-2720`, `:726`; `config.py:530`; `systems/mass_battle/sim/engine.py:226-231`,
  `:424-430`.
- **Architecture:** `04_CODE_ARCHITECTURE.md:179`, `:255`, `:786-796`, `:802`, `:828-836`, `:1166`.
- **Plan and research:** `_part5.md:73`, `:192`, `:215`, `:433`; `00_COMPARATIVE_ANALYSIS.md:202`,
  `:219`; `MB_mass_battle.md:434`.

**Ran in the correction pass:**
- `git status --short` (empty);
- `grep -c levy` on the two registers (23, 19);
- the shipped `oblige` edges on `build_realm(0)`;
- the realm built at cohort weight 2 and 4 (37 cohorts each; total weight 74 and 148; demand 222 and
  444; capacities 4 to 9; build hashes `d3edd90ab3b7` and `754374f85236`);
- the capacity distribution (4 ×16, 6 ×4, 7 ×15, 9 ×2);
- `grep -rl build_army tests/valoria --include='*.py'` (22);
- `grep "_shift("` (two callers);
- `git grep -i conscript` (no hits);
- the untracked-defect grep.

**Could not check:**
- **Whether a computed chooser forms `conscript`,** and what companies do to scene crowding and to
  `_ch_post_remit`'s claim count. The row does not exist (TS-4 (iv)).
- **Whether a typed cell's `key:` may name a literal kind** (part 1, §3.1).
- **Whether a company answers `dispatch` by moving** (part 1, §3.2).
- **Which harness batteries TS-2 moves** (`bat.py` not opened).
- **That `march` is folded at ENC** (read from the matrix comment, not traced in `loop/resolve.py`).
- **Whether IN-36's guard cohorts are built,** and so whether the `mustered` clause adds anyone today
  beyond the two shipped edges, which it does not [RAN].
- **The MB lane's scale probe** (≈120 troops; 0 of 20 at ≤ 80) is cited and not re-run, so the
  falsifier value 250 rests on it.
- **The drafting probes P1–P3** were not re-run in the correction pass.
- **`CURRENT.md` and `HANDOFF_MB.md`** were not read; the mass-battle head is taken from the code.
- **PP and ED provenance** (ED-IN-0279, ED-IN-0255, ED-MB-0067, ED-1090) was not verified against the
  ledgers.
- **R-POOL** is quoted as the coordinator relayed it. I have not seen it at its source.
- **The `.audit/` and `.designs/` trees** were not read.

---

## CRITIC RECONCILIATION

The critic's report (18 findings) against the draft. Each locator was re-opened before any text
changed. "Superseded" means R-POOL removed the object the finding was about.

| # | finding | verdict | where |
|---|---|---|---|
| 1 | weight-2 cohorts: a split of 1 yields two non-cohorts, so C fails at the shipped weight | **applied, then superseded.** Reproduced (`cohorts.yaml`, 37 × 2; `carriers.py:713-721`; `world_q.py:860`). The draft's split is gone under R-POOL. Its arithmetic survives in one place: a company must be minted at `n ≥ 2` (`conscript.refused` below), and casualties leave weight-1 remnants | part 1 §0 items 2–3, §2.4, §3.1; part 2 §4.6 |
| 2 | `mustered` pulls in vassals of other factions (NPC-070, NPC-041); "complies without amending" overstated | **applied.** Probe [RAN]: both obligees hold a `commit`, so `service_faction` excludes both. Layer 1 amendment stated, not denied | part 1 §0 item 4; part 2 §4.1, TS-5 |
| 3 | the morale reader cannot see companies | **applied.** `_side_stance` reads `faction_holding or service_faction`, with a falsifier | part 2 §4.1, TS-5 |
| 4 | experience via `train` excludes case-less persons | **applied.** The axis is unreachable in computed play until J-5 or J-13; TS-10 is blocked; the N-line fails in computed play | part 1 §0 item 5, §3.2; part 2 §8.1, TS-10, J-5 |
| 5 | equipment unreachable; a second loadout table that contradicts `TROOP_LOADOUT` | **applied.** `troop_kinds` dropped; `kind_for_kit` beside `TROOP_LOADOUT`; the levy and `knights_templar` errors named; the unreachability stated | part 1 §0 item 5, §2.7; part 2 §6 |
| 6 | reusing `levy` collides with requirements, the hole register and v9's EXITs | **applied.** Working name `conscript`; the collision laid out in J-3; TS-L is a position if `levy` is chosen | part 1 head; part 2 J-3, TS-7, TS-L |
| 7 | grouping merges a lord's companies; demand (3) overstated | **applied.** One subunit per company; demand (3) met for player and hand-built acts only | part 2 §4.2, §4.3 |
| 8 | Command is constant 4 until R-C-1; `COMMAND_SIGMA_ENABLED` omitted | **applied** | part 1 §1 item 12; part 2 §4.2 step 6 |
| 9 | the §0 ladder was misapplied to J-4, J-6 and J-7 | **applied.** J-6 by precedent; J-7 by architecture; J-4 folded into J-1; J-2 answered by R-POOL; J-1, J-3 and J-5 escalated | part 2 §9 |
| 10 | `order` is a ninth operand, not a `content:` key | **applied.** The ladder run; step 4, `confer`'s `term` | part 2 §4.3 |
| 11 | statement 1's contrary reading not cited | **applied,** inside J-1 and part 1 §2.4 | part 1 §2.4; part 2 J-1 |
| 12 | upkeep per person, not per weight; the witness channel | **applied.** Both stated; upkeep-by-weight listed under J-1; claim count in TS-4 (iv) | part 2 §4.1, §8.2 |
| 13 | `remove_person` pops the person-rung, so kit is destroyed, not orphaned | **applied** (`world.py:770-773`). The salvage clause is kept, with the corrected reason and the general observation | part 1 §2.8; part 2 TS-6 |
| 14 | the illustrative row's `writes` omits `Tenure.term` | **applied** | part 1 §3.1 |
| 15 | TS-5/TS-10 falsifiers blind at scale 1 | **applied.** `men_per_weight = 250` fixed for every run | part 1 §2.8; part 2 §6, §7 |
| 16 | NPC5: a defecting lord who keeps his seat leaves his men behind | **applied.** `service_faction` reads the holder's faction (`holder_faction_of` precedent). Residual named: the attacker's side is still read off the seat's label | part 2 §4.1, §4.7 |
| 17 | the meta-rule net undercounted | **applied.** About 22 added against 6 cut on disk; E-OVERHEAD downgraded to NARROWED | part 1 §3.5; part 2 §8.4 |
| 18 | 22 files, not 44; `Office.faction` at `carriers.py:928`, not `:887` | **applied** (22 [RAN]; `:928` [CHECKED]) | part 2 §4.4, §4.7 |
| — | the morale-preset defect is real and untracked | **applied** as its own position (TS-2), gated on nothing, with the docstring contradiction | part 1 §0 item 9; part 2 TS-2 |

**Rebutted:** none. **Narrowed:**
- **Finding 1** is superseded rather than answered by the original design.
- **Finding 9's** suggestion to keep J-2 escalated is overtaken by R-POOL.
- **Finding 12's** upkeep cost is stated, not fixed.
