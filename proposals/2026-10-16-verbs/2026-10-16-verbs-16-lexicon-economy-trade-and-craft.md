# Verbs, v2 — part 16: Part VI.8, economy, trade and craft (EC)

## Status: PROPOSED (2026-10-17). Reference, not canon (`CLAUDE.md` §0.05): nothing here binds the game or is read by it. Merging ratifies nothing unless Jordan so rules. Static reading and static lookup only; no run.
## Parts, in reading order: [head](2026-10-16-verbs-01-thesis-and-persons.md) (§0, Part I Persons) · [`verbs-02`](2026-10-16-verbs-02-attributes.md) (Part II Attributes) · [`verbs-03`](2026-10-16-verbs-03-standards-roster-and-reconciliation.md) and [`verbs-04`](2026-10-16-verbs-04-critics-etymology-gaps-and-decisions.md) (Part III Verbs: standards, roster, reconciliation; critics, etymology audit, gap coverage, named mechanics, decisions) · [`verbs-05`](2026-10-16-verbs-05-what-verbs-do-to-the-world-1.md) and [`verbs-06`](2026-10-16-verbs-06-what-verbs-do-to-the-world-2.md) (Part IV What verbs do to the world) · [`verbs-07`](2026-10-16-verbs-07-roadmap-reliability-and-sources.md) (§5 Roadmap, §6 Reliability ledger, §7 Sources) · [`verbs-08`](2026-10-16-verbs-08-engine-findings-from-the-first-trial.md) (Part V: engine findings carried from the first-pass trial) · Part VI, the lexicon by subsystem: [`verbs-09`](2026-10-16-verbs-09-lexicon-personal-combat.md) PC · [`verbs-10`](2026-10-16-verbs-10-lexicon-mass-battle.md) MB · [`verbs-11`](2026-10-16-verbs-11-lexicon-social-contest.md) SC · [`verbs-12`](2026-10-16-verbs-12-lexicon-fieldwork-and-inquiry.md) FI · [`verbs-13`](2026-10-16-verbs-13-lexicon-threadwork.md) TW · [`verbs-14`](2026-10-16-verbs-14-lexicon-settlements-and-governance.md) GV · [`verbs-15`](2026-10-16-verbs-15-lexicon-faction-actions.md) FA · **this file** EC · [`verbs-17`](2026-10-16-verbs-17-lexicon-world-travel-and-survival.md) WT · [`verbs-18`](2026-10-16-verbs-18-lexicon-npc-life-and-persons.md) NP · Part VII, the verb gap register (the evidence behind Part VI's coverage tables): [`verbs-19`](2026-10-16-verbs-19-gap-register-pc-and-np.md) PC+NP · [`verbs-20`](2026-10-16-verbs-20-gap-register-mb-and-fa.md) MB+FA · [`verbs-21`](2026-10-16-verbs-21-gap-register-sc-and-gv.md) SC+GV · [`verbs-22`](2026-10-16-verbs-22-gap-register-fi-and-tw.md) FI+TW · [`verbs-23`](2026-10-16-verbs-23-gap-register-ec-and-wt.md) EC+WT.

**How to cite this Part.** The lane's own sections are numbered 3.1 to 3.9; cite them as `EC §3.n` (for example `EC §3.9` for its items for Jordan). Gap ids (`EC-G01` …) resolve in Part VII (`verbs-23`). Abbreviations such as `VT`, `VCD`, `v2-p3` are defined in the lane's opening paragraphs; `v2-p3`, `v2-p4`, `v2-p8` are the first-pass v2 parts as filed at `716c253`. Old file names such as `…synthesis_part8.md` or `_part8` in the body also mean those first-pass files; the suite was later renamed `2026-10-16-verbs-NN-…`. Mechanic ids (`M1`, `M-1`, `M-WT-1`) are this lane's own.

**Rulings that override this section** (`verbs-03` §III.5; where this section and the roster disagree, the roster governs):

- R-01: `hire` is EC's row, for a person or a company.
- R-03: `found`, `build` and `raze` are **GV's** rows; EC keeps `work`, `craft`, `restore`, `transfer`, `exchange`, `hire`, `borrow`, `lend`.
- R-04: `tax` is GV's own row; EC's folding of `tax` into `requisition` is overridden.
- R-26: `restore` is fabric repair only; TW's `mend` is Mending.
- R-27: `hunt` is `work` at a wild site.

---

# EC — economy, trade and craft

Lane file for the v2 rewrite (Part III by subsystem, Part V's EC table). Read at HEAD `716c253`
(after the `levy` → `requisition` rename, #482). Static reading only: no engine run was made for this
file. Every `file:line` below was opened unless it is tagged. Gap ids are `L5_EC_WT.md`'s.

---

## 3.1 Subsystem mechanic (what the engine has, what it lacks)

**Carriers.** `Rung.stores` (matter by kind; `rosters.yaml:1297-1308` registers grain, salt, timber,
ore, coin); `Rung.yield`; `Site.condition` on `site_kinds` harbour, seam, body, dwelling, garrison
(`rosters.yaml:1264-1295`); the `works` Record (`plan`, `at`); `Tenure.term` on `oblige` edges.
**Source.** MATTER mints yield, keyed on the Site: `site_yield` × `condition/condition_scale` ×
`season_factor` (`rosters.yaml:2169-2196`; written at `loop/matter.py:504-536`). Only harbour (grain,
salt) and seam (ore, timber) produce; **no cell produces coin or arms**.
**Sinks and moves.** `subsistence_draw` (`queries/world_q.py:804`); `_shift`, the one conserved
two-rung move (`loop/effects_shared.py:126`); `works_cost` consumed by `build`, moved by `found`
(`rosters.yaml:1389-1413`).
**Shipped verbs that write these carriers** (`engine/season/verb_table.yaml`): `transfer` (:1247,
`Rung.stores` ×2 + `Tenure.term`; renews upkeep terms, `loop/effects_economy.py:240-309`);
`requisition` (:646, ×2 into the seat's treasury, `loop/effects_governance.py:374`); `exchange`
(:312, declared, **no effect, no typed cell**); `work` (:1278) and `restore` (:862), both staging
`_rise` on `Site.condition` (`effects_economy.py:101-130`); `build` (:390) and `found` (:367)
(`loop/effects_founding.py:92, :185`).
**Lacks** (grep of `loop/ state/ queries/ data/ decision/` for debt, hire, wage, price, recipe,
workshop returns only `works_cost`'s "price"): no price or value; no labour term in yield; no
conversion of goods; no credit Record; no hiring opener; no storage bound; no coin producer; no
distance cost; `exchange` cannot name its second side.

## 3.2 Convention floor

| floor act | precedent (in-tree path:line; game [MEMORY] with the mechanic) | state today |
|---|---|---|
| **produce** (labour at a producing place) | `research/historical_concerns_action_catalogue_v1.md` §2.6 :104-115 (harvest as the hinge of famine); Banished [MEMORY]: labourers assigned to a field or mine, output scales with workers; Medieval Dynasty [MEMORY]: villagers assigned to a farm or mine produce per worker | **shipped as yield, no verb**: MATTER mints without labour; `work` does not produce (its effect advances a works) |
| **make / craft** (convert goods) | `research/by_lane/FA_faction_actions.md:64` (Arte della Lana, via the register, not opened); Dwarf Fortress [MEMORY]: a workshop job consumes named inputs (bars, logs) for one product the player orders; Anno [MEMORY]: production chains, a processing building needs its input good | **absent** (v2 V154: a Site-kind data row, p8:503) |
| **build** (place a new structure) | `research/proactive_governance_scale_research_v1.md` S1 :51, S5 :55 (Develop, phased canal ring); Civilization [MEMORY]: city builds a building from production; Banished [MEMORY]: place a building, builders raise it over time from stocked materials | **shipped**: `build` mints a Site at condition 0; the raising is on `work`/`restore` |
| **found** (a new settlement or hearth) | `research/fa_se_historical_precedent_research_v1.md` T8 :152-160 (via the register, not opened); Civilization [MEMORY]: "Found City" is a distinct unit action, not a building | **shipped**: `found` mints a Rung |
| **improve / repair** | `proactive_governance_scale_research_v1.md` S7 :57 (Fortify: Code); Civilization V/VI [MEMORY]: a worker/builder repairs a pillaged improvement as its own action; Total War [MEMORY]: a damaged building is repaired at a cost | **shipped** (`restore`); upgrade: **absent** |
| **raze** | `research/historical_concerns_action_catalogue_v1.md` §2.3 :70 (via the register); Total War [MEMORY]: occupy / sack / raze on capture | **designed** (v2 p3:254) |
| **stockpile** | `fa_se_historical_precedent_research_v1.md` SE-2 :250-255 (granary level gates Open Granary); PGS S10 :60 (Standing Reserve); Banished [MEMORY]: stockpiles and barns have a capacity; Caesar III [MEMORY]: granaries and warehouses hold a bounded stock | **absent** (no storage bound; keeping is the default) |
| **trade / buy / sell** | HCC §2.10 :157-169 (Hanse, Fugger); PGS F4 :123 (Stapelrecht); Patrician / Port Royale [MEMORY]: buy and sell at each town's own price, set by its stock; Mount & Blade [MEMORY]: town prices by local production, trade between towns is profit | **shipped row, THIN**: `exchange` has no effect |
| **price** | PGS S8 :58 (Assize of Bread), S9 :59 (narh); FASE SE-2 :252 (Fix Prices); Patrician [MEMORY]: price falls as a town's stock rises | **absent** |
| **hire labour** | FASE FA-2 :192-196 (muster as purchase, Redlich); Mount & Blade [MEMORY]: hire troops and pay a weekly wage, desertion when unpaid; Medieval Dynasty [MEMORY]: hire a villager, he works the building you assign | **absent** (v2 V158: `oblige` + upkeep `transfer`) |
| **lend / borrow** | HCC §2.9 :146-155 (Bardi and Peruzzi default, funding and assumption); PGS F7 :126 (Solon's debt cancellation); CK3 [MEMORY]: borrow gold from a holy order, repay or lose standing; EU4 [MEMORY]: take a loan with interest, default is bankruptcy | **absent** (v2 V157: a `debt` Record kind) |
| **tax** | FASE T1 :89-97, FA-1 :186-191 (Levi's compliance; the missing rate decision); Caesar III [MEMORY]: a collector walks past houses and takes tax by rate; CK3 [MEMORY]: holdings pay tax each month at a rate set by contract | **designed** (v2 V145: content of `issue`); **shipped extraordinary twin**: `requisition` |
| **upkeep** | `research/by_lane/SE_settlements_territory_economy.md:100` (Wealth-0 handling across Rome II, Shogun 2, CK, KOEI, JA2); Civilization [MEMORY]: per-turn gold upkeep of buildings and units | **shipped**: `transfer` through a seat renews `oblige` terms at `upkeep_of` (`effects_economy.py:240-309`) |
| **haul** (carriage costs distance) | `research/historical/precedents_warfare.md` §1.3a :37 (via the register); Patrician [MEMORY]: convoys take days by sea lane | **absent** (adjacency read by no season module) |

## 3.3 Suites

Ten suites. Each host is judged first against the floor (3.2) and precedent, then deduplicated.
"Fold test" = **same actor? / same subsystem mechanic? / differs only in a parameter or content?**

### S1 · Production — host `work` (REBUILD)

**What is wrong today (L-06, applied).** The row's precondition reads "work" as exploiting a site
(`condition >= floor`, the floor being the least demanding *site-use* in `band_floors`,
`verb_table.yaml:1283-1290`; `rosters.yaml:2198-2208` says those keys are site-uses such as
deep_mining). Its effect reads "work" as advancing a works (`_rise`, `verb_table.yaml:1292`;
`loop/effects_economy.py:59-98`). The effect is a strict subset of `restore`'s (same `_rise`, only at
a works' fabric). So the row has two senses and no effect of its own (H-105, via the register).
**Rebuild.** Keep the precondition (the exploit sense is the one the floor table already types). Move
the works-advance to `build` (S3). Give `work` the production effect: the worker's labour is staged on
the Site for the season and MATTER's yield reads it (`yield = site_yield × condition/scale ×
season_factor × labour factor`). A cohort Person counts its weight (R-C-9).

| folded act | fold test | line |
|---|---|---|
| `cultivate` (till a field) | Y / Y / Y | labour at a site whose kind yields grain; the site kind is the content. Needs a `field` site kind (today grain comes from `harbour`, `rosters.yaml:2190-2192`) |
| `mine` (dig a seam) | Y / Y / Y | labour at `seam`; the site-use (`deep_mining`) is the content the floor already keys on |
| `fish` | Y / Y / Y | labour at `harbour` under the `fishing` use |

**World effect.** Writes a per-season labour tally on the Site, read once by MATTER's yield write
(`loop/matter.py:504-536`), then cleared. Emits `site.worked` (kept); refusal `work.unavailable`
(kept). **Lacks:** the labour tally and its reader (3.7 M1); a site-use operand so the floor is typed
to the intended use (`verb_table.yaml:1290`, H-08/H-94); a `field` kind.
**NERS.**
- **N:** cut it and no person act touches what a place produces. Bottom-up: a hearth cannot raise its
  harvest by hands; top-down: a seat's labour (S7) has nothing to buy; vertical: depopulation never
  costs output (EC-G41); lateral: two hearths do not compete for one seam's hands; diagonal: a levy
  taken from `recruits` never empties the fields (MB → EC). *False-N attack:* `restore` raises
  `condition`, which scales yield, so labour already reaches yield, until the fabric is at full scale,
  after which more hands change nothing and fewer hands cost nothing. The step "fewer hands, less
  food" has no carrier. N HOLDS.
- **R:** R-WORLD: the Banished spiral (deaths remove the hands that gather food) arises with no
  player; R-CHOICE: grain against ore against timber; R-COMPLETE: zero hands gives zero yield, so the
  factor must ship at a control arm (factor ≡ 1) or every corpus world starves.
- **S:** pauses correctly: the act stages, MATTER reads, in the order "resolve FIRST, then bodies,
  larders, yield" (`loop/matter.py:284`). Methodology: the labour share reuses `share` (the commons
  rule `_rise` uses, `effects_economy.py:110-112`), not a second ladder.
- **E (ratio):** rows 1 → 1; one duplicate effect body deleted (`work` no longer calls `_rise`); one
  term added to an existing formula. The player predicts "more hands at the mine, more ore".
**Precedent.** Banished [MEMORY]: workers assigned per building, output by headcount; Medieval
Dynasty [MEMORY]: villagers assigned to a farm or mine; Anno 1800 [MEMORY]: a production building
needs its workforce or slows; `research/by_lane/SE_settlements_territory_economy.md:105` (Banished's
labour spiral, from the teardown).
**Gaps.** Closes EC-G12, EC-G13, EC-G40, EC-G41 (once M1), EC-G42 (once M6). Leaves EC-G15's degree
term open.
**Disposition: REBUILD.** *Falsifier:* a two-arm run (labour factor on against ≡ 1) in which a
rung's yield does not fall when its working cohort shrinks.

### S2 · Making — host `craft` (NEW ROW)

**Why its own row (brief caution 6, applied).** v2 made craft "a workshop Site-kind data row with a
`site_yield`" (p8:503). A `site_yield` row has **no inputs**: a smithy keyed that way mints arms from
nothing, which is a source and not a conversion. Making turns named goods into other goods, and the
maker chooses the product. Neither is a parameter of `work`.

| folded act | fold test | line |
|---|---|---|
| `mint` (strike coin) | Y / Y / Y | `craft` at a mint Site, product `coin` from `ore` |
| arms-making (smith) | Y / Y / Y | `craft` at a smithy, product an arms kind (TSD2 §9 names no arms producer) |
| vs `work` | Y / **N** / N | `work` adds labour to a yield from nothing; `craft` consumes stores and makes another kind in the act. Not a fold |

**World effect.** Operands: `site` (the workshop), `kind` (the product), `amount`. Precondition: the
actor is present at a workshop whose kind admits the recipe, its condition clears the product's
floor, and the workshop's rung holds the recipe's inputs × amount. Writes `Rung.stores` at that one
rung (inputs down, product up; the matrix pair exists, `verb_table.yaml:383`). Emits `goods.made`;
refusal `craft.refused` (the scarcity channel, VT header :13-16). **Lacks:** a `recipes` roster and
workshop site kinds (3.7 M2); arms and tool matter kinds.
**NERS.**
- **N:** cut it and nothing converts goods. Vertical: no arms producer, so a levy cannot be equipped
  in computed play (`proposals/2026-10-16-troop-stock-design.md:101-104`); diagonal (EC → MB): ore
  never becomes a field army's kit; lateral: no rung adds value to a neighbour's raw ore, so trade
  (S6) has nothing but raw kinds to move; top-down: coin has no producer (EC-G21). *False-N attack:*
  a workshop `site_yield` row gives the output with no act; the step "the ore is used up" has no
  carrier there. N HOLDS.
- **R:** R-CHOICE: arms or tools from one smithy's ore; R-WORLD: a rung without ore must trade for
  it; R-COMPLETE: inputs short → `craft.refused`, never a partial product.
- **S:** the conversion is debited at RESOLVE like `build`'s `works_cost` (`rosters.yaml:1394-1400`),
  the same "one-sided lawful sink" shape, now with a product.
- **E:** +1 row, +1 roster. Buys three floor acts (make, arm, mint) and closes three gaps.
**Precedent.** Dwarf Fortress [MEMORY]: a job at a workshop consumes listed inputs for one ordered
product; Anno [MEMORY]: a processing building turns an input good into an output good; Medieval
Dynasty [MEMORY]: crafting at a bench from carried materials.
**Gaps.** Closes EC-G38, EC-G39, EC-G21 (with a coin seed at world build), once M2. EC-G26
(debasement) stays PARKED.
**Disposition: NEW ROW.** *Falsifier:* a run in which a workshop produces its kind while its
rung's input store does not fall.
[ASSUMPTION: "persons do not mint stores (W8)" (v2 p8:521) governs `Rung.yield`, whose only writer
is MATTER (`loop/matter.py:504`, "#353 §25's *only here* row"); `craft` writes `Rung.stores`, as
`build` already consumes them in an act. If W8 is read as covering any new unit of a kind, `craft`
stages the conversion for MATTER instead: same row, same verdict. Answered by precedent, not
escalated: stores already change inside RESOLVE by act (`transfer`, `requisition`, `build`), and
MATTER runs after RESOLVE (`loop/matter.py:284`).]

### S3 · Construction — host `build` (REBUILD); siblings `found` (KEEP-AS-IS), `raze` (NEW ROW)

**Rebuild.** `build` today mints a Site at condition 0 and consumes `works_cost`
(`verb_table.yaml:390-412`; `loop/effects_founding.py:185`). The raising of that fabric toward its
works' ceiling sits on `work` and `restore` (`effects_economy.py:59-71`, :150-154). Move the advance
here: on a works whose Site exists, `build` stages `_rise` to the works' ceiling; on one whose Site
does not, it mints. "Work on the walls" in ordinary English is "build the walls" (L-06's own
concession), and r2's ruling that "a rival may finish what somebody else began"
(`effects_economy.py:153-154`) is kept by moving the holding clause from the cell into the mint
branch of the effect (the grammar has no disjunction, `verb_table.yaml:859`).
[ASSUMPTION: medium; an effect-side decline is the precedent `seize` set, `verb_table.yaml:911`.]

| folded act | fold test | line |
|---|---|---|
| raise the courses (advance a works) | Y / Y / Y | `_rise` to the works' ceiling; the stage is the parameter |
| `fortify` | Y / Y / Y | a works planning a `garrison` Site (Jordan's 2026-09-28 choice, `rosters.yaml:1282-1287`); `references/action_vocabulary.yaml:28`'s `Fortify` lands here (EC-G49) |
| `improve` (upgrade) | Y / Y / Y | a works planning a higher ceiling on a Site that exists; needs M4 |
| vs `found` | Y / **N** / N | `found` mints a Rung, its `contain` edge and the founder's `hold`, under the `founding` gate basis, and moves its stake two-sided (`verb_table.yaml:382-383`); `build` mints a Site and consumes. Different carriers, different gate basis |
| vs `restore` | Y / Y / Y | passes (same `_rise`, ceiling source differs); **not folded**, on fit: see S4 |

**`found` (KEEP-AS-IS).** It is the floor act "found a settlement or hearth". Civilization [MEMORY]
keeps "Found City" a unit action distinct from building. Its cost, holder and ascent landed at IN-28
(`verb_table.yaml:371, :383`). L-07 (`found`/`establish` near-synonyms) is GV's to answer (3.8).
**`raze` (NEW ROW; v2 filed it under MB, p3:254).** Ends a Site (`Site.exists` closed) or a Rung
(closes its `contain` and holds). Eligibility: the holder of the place, or a seat whose purview
reaches an occupied place (`seize`'s occupation reading, `verb_table.yaml:911`). Emits `site.razed` /
`rung.razed`. The matrix rows exist; the close is the inverse of `build`/`found`'s mint.
**World effect (suite).** `Site.exists`, `Site.condition`, `Rung.exists`, `Tenure.since/until`,
`Rung.stores` (cost). **Lacks:** a computed producer of works Records (`create_record` of kind works
forms from no question today, EC-G46: 3.7 M5); upgrade works (M4); raze's effect.
**NERS.**
- **N:** `build` — cut and no place is ever added (`ARCH F.20`, quoted at `verb_table.yaml:350-351`:
  "the world only decays"). `raze` — cut and no place ever ends but by neglect; `found`/`build` have no
  inverse (H-166, via the register); conquest cannot burn a town (S-diagonal MB → EC). *False-N
  attack on `raze`:* wear lowers `condition` to 0, but a Site at 0 still exists, still counts toward
  `capacity` and still names its works. N HOLDS.
- **R:** R-CHOICE: what to build where, with whose timber; R-WORLD: a rival finishes an abandoned
  works; a garrison raised before a march. R-COMPLETE: a works with no `works_cost` row refuses
  (`rosters.yaml:1401-1402`).
- **S:** one formula (`_rise`) for raising and repairing (S's methodology clause). Vertical: a
  seat's `build` pays from the works' rung, which is how Develop and Sponsor differ (EC-G51).
- **E:** rows unchanged for build/found; +1 (`raze`); the advance leaves `work`, so no row carries a
  second sense.
**Precedent.** Banished [MEMORY]: a placed building is raised by builders from stocked materials;
Civilization [MEMORY]: Found City vs build; Total War [MEMORY]: occupy, sack or raze;
`research/proactive_governance_scale_research_v1.md` S1 :51, S2 :52, S5 :55 (Develop, Sponsor,
phased works).
**Gaps.** EC-G45, EC-G46, EC-G47, EC-G49, EC-G51.
**Disposition:** `build` REBUILD; `found` KEEP-AS-IS; `raze` NEW ROW. *Falsifiers:* `build` — a
works whose fabric reaches its ceiling with no `build` or `restore` staged on it; `raze` — a place
that leaves the world by any route other than `raze` (if one exists, `raze` is redundant).

### S4 · Repair — host `restore` (REBUILD: narrowed to Site fabric)

**Rebuild.** `restore` raises any fabric the actor stands at, to the works' ceiling or to full scale
(`effects_economy.py:133-164`). After S3 takes the works-advance, `restore` is repair of wear on a
Site that no live works names. It keeps `own | presence:<site>` and its typed cell
(`verb_table.yaml:864-876`).
**Fold test against `build`:** Y / Y / Y: it passes. **Kept apart on ordinary usage:** "build the
harbour" does not mean "repair the harbour", and a host must name its folded act's sense; game
convention separates the two (Civilization V/VI [MEMORY]: a worker repairs a pillaged improvement as
its own action; Total War [MEMORY]: a damaged building is repaired at a cost).
**World effect.** `Site.condition` (`_rise` to full scale); `site.restored` / `restore.refused`.
**Lacks:** the degree term (H-164, `effects_economy.py:113-121`).
**NERS.** N: cut and wear is answered only by a new works (a stake, a `works_cost`), so the cheap
repair dies. *False-N attack:* `build` could repair if a works were planned on the worn Site; the
step "repair without a plan or a cost" has no other carrier. N HOLDS, narrowed (it holds in the
bottom-up and lateral directions; vertically a seat can always plan a works). R-WORLD: the wear loop
(`wear_per_season`) has a person-driven recovery arm. S: same `_rise`. E: kept at MEDIUM confidence
(watchlist, 3.5): one row for a sense the host's word does not carry.
**Gaps.** EC-G13, EC-G14 (once TW takes Mending to `mend`, 3.8).
**Disposition: REBUILD.** *Falsifier:* a run in which a worn, unplanned Site regains condition with
no `restore` staged.

### S5 · Moving stores — host `transfer` (KEEP; operand derivation REBUILD)

**Today.** `transfer` is the one conserving mover between two rungs (`Rung.stores` ×2), and through a
seat it renews `oblige` terms at `upkeep_of` apiece (`verb_table.yaml:1247-1266`;
`effects_economy.py:167-309`). A computed transfer derives `to` as the giver's own hearth and is
refused (EC-G11; H-94, H-136 via the register).

| folded act | fold test | line |
|---|---|---|
| `pay` (upkeep, wages) | Y / Y / Y | shipped: a transfer through a seat to an obligee's home renews his term (`effects_economy.py:247-264`) |
| `repay` | Y / Y / Y | a transfer citing a `debt` Record; full payment closes it (S8), as `pay` already writes a second carrier (`Tenure.term`) |
| `haul` | Y / Y / Y | not a content but a cost every transfer between non-adjacent rungs pays (M3); "haul" names the carrying |
| `relieve` | Y / Y / Y | a transfer to a rung in shortfall, earning `relief.given` (v2 V149, GV's content; 3.8) |
| tribute (paying it) | Y / Y / Y | `pay` under a covenant term; the term is FA's (3.8) |
| `smuggle` | Y / Y / Y | a transfer past a held ban: **PARKED**, trigger: a ban term exists (M7) |

**World effect.** `Rung.stores` ×2, `Tenure.term`; `transfer.made`, `term.renewed`; refusal
`transfer.refused`. **Lacks:** a `to` derivation naming another rung (3.7 M8); distance (M3); the
`debt` close (M9).
**NERS.** N: cut and matter cannot move between places by consent: no upkeep, no relief, no
delivery. *False-N attack:* `give` moves holds, not stores (`verb_table.yaml:433`); `requisition`
moves stores only into a seat's treasury and only by authority (:670-671). N HOLDS in all six
directions (vertical: seat → obligees; lateral: hearth → hearth). R-WORLD: embezzlement already
falls out (`effects_economy.py:273-277`). S: one move body (`_shift`). E: 1 row carries five named
acts.
**Precedent.** Patrician [MEMORY]: a convoy carries goods between towns at a time cost; Civilization
[MEMORY]: per-turn gold upkeep; `SE_settlements_territory_economy.md:100` (Wealth-0 handling).
**Gaps.** EC-G09, EC-G10, EC-G11, EC-G34, EC-G37; EC-G22 waits on 3.9 item 1.
**Disposition: KEEP** (row); **REBUILD** of its computed operand derivation. *Falsifier:* a
transfer that ends with total store mass changed (the F10 conservation check,
`effects_economy.py:199-208`).

### S6 · Trade — host `exchange` (REBUILD)

**Today.** Declared, `Rung.stores` ×2, no effect, no typed cell; IN-33 coined the second side's two
operands and was reverted at 0 executions (`verb_table.yaml:312-329`). v2 would retire it into
`covenant`'s goods terms (p8:245, :502).
**v2's retirement, tested.** `covenant` binds seats to future terms (FA's mechanic); a trade is a
present swap between any two holders. Fold test `exchange` → `covenant`: actor N (anyone vs a seat),
mechanic N (a swap now vs a term binding later). **Rejected.** A trade treaty is a covenant whose
terms are performed by `exchange`/`transfer`; that composition is FA's (3.8).
**Rebuild.** One new operand, `return_kind`; the return amount is read off a **price Query**,
`price_of(rung, kind)`, computed on demand from the rung's stores against what it must draw
(`subsistence_draw`, `queries/world_q.py:804`; upkeep) and stored nowhere (3.7 M10). The counterparty
must be co-located (`give`'s `with` stem, `verb_table.yaml:427-430`) and accepts when the swap clears
his own rung's prices: his consent is a precondition read from his own state, not a second act.

| folded act | fold test | line |
|---|---|---|
| `trade` | Y / Y / Y | synonym; the game word |
| `buy` | Y / Y / Y | the actor gives `coin` |
| `sell` | Y / Y / Y | the actor takes `coin` |
| `barter` | Y / Y / Y | neither side is `coin` |
| `bargain` (haggle) | Y / Y / Y | the price moved within a band by a contest's degree instead of read off the Query: a parameter |

**World effect.** `Rung.stores` ×4 (two per side); emits `exchange.made`; refusals
`exchange.refused` (a side cannot cover: scarcity) and `exchange.declined` (the price is not met).
**Lacks:** M10 (price), the `return_kind` operand, M14 (`requires_operands` is closed,
`verb_table.yaml:654` "the closed eight stand"), the bargain contest (SC's).
**NERS.**
- **N:** cut it and a settlement can be given to or taken from, never buy (EC-G18). Lateral: no
  specialisation pays; vertical: a seat cannot buy grain for a starving rung; diagonal: a siege
  (MB) cannot raise a town's price. *False-N attack:* two `transfer`s by two parties compose a trade,
  but that composition needs the other party's reply as a second act (the workaround the brief
  forbids) and is not atomic: a refused half must undo the other (v2's own "honest cost", p4:285).
  N HOLDS.
- **R:** R-WORLD: a dearth raises a rung's grain price and a merchant hauls grain there, or the poor
  cannot pay (Sen's entitlement failure, FASE T3 :105-111 via the register); R-CHOICE: what to sell,
  where; R-COMPLETE: no stock → refused; no coin → barter still runs.
- **S:** the price is a compute-on-demand aggregate of existing carriers, not a stored gauge (NERS
  §7.4's attack passes); Fix Prices and assize become one cap the Query reads (GV's).
- **E:** rows 1 → 1; +1 operand; +1 Query. Five floor words (trade, buy, sell, barter, bargain) on
  one row.
**Precedent.** Patrician / Port Royale [MEMORY]: each town buys and sells at its own price, set by
its stock; Mount & Blade [MEMORY]: town prices follow local production, carrying goods between towns
is profit; `research/historical_concerns_action_catalogue_v1.md` §2.10 :157-169;
`research/proactive_governance_scale_research_v1.md` F4 :123.
**Gaps.** EC-G16, EC-G18, EC-G19, EC-G28 (reader half), EC-G44 (Fix Prices half).
**Disposition: REBUILD.** *Falsifier:* a run in which a rung in dearth receives no more grain by
`exchange` than a rung in surplus, across seeds (the price does not steer).

### S7 · Hiring — host `hire` (NEW ROW)

**Why its own row (V-06, applied).** v2 merges hire into "`oblige` + the upkeep `transfer`" (p8:507).
`oblige`'s actor is the joiner (`verb_table.yaml:759-762`, `beneficiary: actor`); in English the
subject of *hire* is the employer. The merge makes hiring the hireling's act plus the employer's
later payment: two actors, two acts, the workaround the brief names.
**The row.** Actor: the employer (`own`, or through a seat by `remit:issue`, `transfer`'s
alternative, `verb_table.yaml:1249-1250`). Operands: the hireling (`to`, co-located: `with`), `kind`
and `amount` (the wage per term). Precondition: the employer's rung covers the first wage; the
hireling holds no live service to the employer and no `ban` (`rosters.yaml:124`); the wage clears his
own need (read from his shortfall claim). Writes: the hireling's service edge (an `oblige`-kind
`Tenure.since` with `Tenure.term`, the wage as its upkeep), and the first wage (`Rung.stores` ×2).
Emits `labour.hired`; refusal `hire.refused`.
**Fold test.** vs `oblige`: N / Y / N (other actor). vs `transfer`: Y / N / N (it opens an edge).
**Ending.** No dismissal verb: D-5 refuses an obligee-side closer (`verb_table.yaml:861`). The
employer stops paying and the term lapses at MATTER, which emits; the hireling may `release`.
**World effect lacks.** The gate admits an edge opened by someone other than its owner only on a
basis (`give`'s `handover`, `verb_table.yaml:434`); hiring needs one, "the wage paid in the same
write" (3.7 M11). What the hired hand does with his season (his `work`/`build` at the employer's
sites) is the chooser's reading of his obligation (NP, 3.8).
**NERS.** N: cut and wealth cannot become labour or soldiers by the payer's choice: Tilly's
capital-intensive path (FASE T1 :89-97) and the fiscal-military purchase (FASE FA-2 :192-196) have no
act. *False-N attack:* `oblige` + `pay` reach the same edge, but only if the hireling moves first;
"the employer acts" has no carrier. N HOLDS. R-WORLD: a rich hearth hires the poor in a dearth; an
unpaid company lapses. R-CHOICE: hire hands or buy grain. S: the term, upkeep and lapse are
`oblige`'s shipped mechanics (`effects_economy.py:240-309`), reused. E: +1 row; no new carrier.
**Precedent.** Mount & Blade [MEMORY]: hire troops in a tavern, weekly wages, desertion when unpaid;
Medieval Dynasty [MEMORY]: hire a villager and assign him to a building; CK3 [MEMORY]: hire a
mercenary company for gold and monthly upkeep.
**Gaps.** EC-G33; EC-G22 (with 3.9 item 1).
**Disposition: NEW ROW.** *Falsifier:* a hired service edge that exists without a wage moving in the
same write.

### S8 · Credit — `borrow` and `lend` (NEW ROWS, one effect owner)

**The rows.** One mechanic, written by either party: the creditor's rung advances `amount` of `kind`
to the debtor's (`Rung.stores` ×2) and a `debt` Record is minted, held by the creditor, naming the
debtor, the sum due and the season it falls due (`Record.exists`). `borrow`: the debtor acts; the
creditor's consent is read from his surplus and the debtor's record. `lend`: the creditor acts; the
debtor's consent is read from his need. Emits `debt.made`; refusal `credit.refused`.
**Fold test** `borrow` ↔ `lend`: actor **N** / mechanic Y / content Y. Two rows, because the brief
folds only on the same actor; one effect owner, so the arithmetic lives once.
**Repayment and default.** `repay` is a content of `transfer` (S5). At the due season MATTER marks
the debt lapsed and emits `debt.lapsed` (silence is not allowed to win, NERS §6). The creditor's
remedies are `open_case` → `determine` (v2 p8:506) or distraint (GV's; 3.8).
**NERS.** N: cut and no seat can spend ahead of its yield; insolvency is a refusal, never a
decision. *False-N attack:* `transfer` + a `covenant` term could carry a loan, but a covenant binds
seats and nothing reads a repayment against it; "the debtor owes this creditor this much by then"
has no carrier (`Term` has no amount, EC-G24). N HOLDS. R-WORLD: a banker gains a hold over a crown
(HCC §2.10 :161, Fugger); a default sours a creditor. R-CHOICE: borrow for walls now, or wait. S:
due date read at MATTER, as `oblige` terms mature (`verb_table.yaml:860`). E: +2 rows, +1 Record kind;
the second row is the cost of naming each act in its actor's voice (watchlist, 3.5).
**Precedent.** CK3 [MEMORY]: borrow gold from a holy order and repay within a term; EU4 [MEMORY]:
take a loan, pay interest, default is bankruptcy; HCC §2.9 :148 (Edward III's default),
:153 (funding and assumption); PGS F7 :126 (Solon's debt cancellation).
**Gaps.** EC-G24; EC-G44 (Foreign Loan).
**Disposition: NEW ROW ×2.** *Falsifier:* a `debt` that reaches its due season and emits nothing.

### S9 · Revenue — host `requisition` (KEEP; owner GV), folded `tax`

The act is an act of governance, exercised through a seat (`remit:issue` + `purview`,
`verb_table.yaml:650-669`), so the brief hands it to GV. EC owns the store move it writes (`_shift`)
and the Query it reads. Recorded here because the register's rows are EC's.

| folded act | fold test | line |
|---|---|---|
| `tax` | Y / Y / Y | same seat, same move into the treasury; the amount is a rate × the rung's yield as the seat knows it, the earned kind `tax.collected` (customary) beside `requisition.taken` (extraordinary) |
| fiscal stance (Light / Standard / Extraction) | Y / Y / Y | the rate itself: a parameter of `tax` (EC-G53) |
| gauge-indexed levy | Y / Y / Y | a rate on yield already moves with `season_factor`, which yield reads (`rosters.yaml:2180-2185`); nothing to add (EC-G27) |
| `toll` | Y / Y / Y | a `tax` at a route rung on what passes: **PARKED**, trigger M3 (adjacency) |
| tax farming, debasement | — | **PARKED** (3.6) |

**World effect.** `Rung.stores` ×2 into the seat's treasury; `requisition.taken` / `tax.collected`;
keyed refusals (`verb_table.yaml:673-678`). **Lacks:** the rate and the seat's assessed yield (a claim
from witnessed `yield.taken`, so the tax reads what the taxer can know, NERS C3); the pricing of
taking in dearth (a `deed:` cell, GV/SC).
**NERS.** N: cut and no seat has income but by gift. R-WORLD: the taxed rung in dearth bears a
grievance (once priced). S: one move body; the rate makes the extraction decision a parameter, not a
second verb. E: `tax` costs no row.
**Precedent.** Caesar III [MEMORY]: tax collected by rate from housing; CK3 [MEMORY]: holdings pay
by a contract rate; FASE T1 :89-97, FA-1 :186-191 (Levi's quasi-voluntary compliance; the missing
rate decision).
**Gaps.** EC-G03, EC-G05, EC-G06, EC-G07, EC-G27, EC-G53.
**Disposition: KEEP** (`requisition`, GV-owned); `tax` FOLD. Which word heads the row is GV's (3.8).
*Falsifier:* a `tax` whose amount does not fall when the rung's yield falls.

### S10 · Storage — no host verb (`hoard` PARKED)

Stockpiling is the floor act; keeping is the default (`Rung.stores` persists). What the floor
convention means by it is **bounded storage** (Banished, Caesar III [MEMORY]). That is `build` of a
storehouse or granary Site kind (S3) plus a capacity bound on `Rung.stores` read from it (3.7 M12),
and `transfer` into it (S5). A verb "stockpile" would write nothing no other verb writes (brief
criterion 6). **`hoard`** (withholding stores from those who would draw on them) and WT's `ration`
(limiting the draw) are the two signs of one missing mechanic, a draw policy at a larder
(`subsistence_draw` walks to the nearest store, `queries/world_q.py:689`, :804): **PARKED together**,
trigger: a draw-policy ruling (v2 V148's trigger, p8:482).
**Gaps.** EC-G31, EC-G43, EC-G44 (Open Granary).

### Culled and out of the suites

- **`appraise` — CULLED.** Price is a Query (S6), read by presence at the rung; valuing an estate or
  a ransom is FI's `examine` content. The word also collides with the churn survey's "appraisal"
  (EC-G20). Fold test vs `examine`: actor Y / mechanic N (FI) / content N.
- **`steal` — OUT OF SCOPE** (crime; v2 REJECT "refused by the plan", p4:256; VCD K-51). NP/FI.

---

## 3.4 Lexicon table

Sources: **Wikt** = en.wiktionary via `etym_tool.py en|la` (run 2026-10-16/17); **L&S** = Lewis &
Short via `etym_tool.py ls`. A link not returned by either is tagged `[UNVERIFIED]`. "cognate, not
ancestor" marks a Latin word reached only through PIE. Status: SHIPPED = a `verb_table.yaml` row.

| verb | suite | status | mechanic and world effect (carrier written) | etymology chain, with sources | fit (ordinary current usage) | rename |
|---|---|---|---|---|---|---|
| `work` | S1 | SHIPPED (REBUILD) | labour staged on a Site, read by MATTER's yield (`Site` labour tally → `Rung.yield` → `Rung.stores`); M1 | **Germanic.** ModE work ← ME *werken*, *worchen* ← OE *wyrċan*, Mercian *wircan* ← PGmc \**wurkijaną* ← PIE \**wr̥ǵyéti*, root \**werǵ-* (Wikt). No Latin path; no Latin cognate given | **FITS** once rebuilt: "work a mine, work the land" is labour that produces. Today STRAINED (L-06) | — |
| `cultivate` | S1 | FOLDED (work) | `work` at a field Site | ← ML *cultīvātus*, ppp. of *cultīvō* ← *cultīvus* ← *cultus*, ppp. of L *colō, colere, coluī, cultum*, L&S "to cultivate, till, tend, take care of a field, garden" ← PIE \**kʷel-* 'turn' (Wikt). ME stage: none; a 17th-c. learned borrowing [UNVERIFIED date] | **FITS**: grow crops | — |
| `mine` | S1 | FOLDED (work) | `work` at a seam under `deep_mining` | verb from the noun ← OF *mine* ← LL *mina* ← Gaulish ← PCelt \**meinis* (Wikt). **Celtic, entered through Late Latin**; no Latin root | **FITS** | — |
| `fish` | S1 | FOLDED (work) | `work` at a harbour under `fishing` | **Germanic.** OE *fiscian* ← PWGmc \**fiskōn* ← PGmc \**fiskōną* (Wikt). L *piscis* is a cognate, not ancestor (Wikt en noun block: "Compare ga *iasc*, la *piscis*") | **FITS** | — |
| `craft` | S2 | NEW | conversion at a workshop: `Rung.stores` inputs down, product up; `goods.made`; M2 | **Germanic.** ME *craft* ← OE *cræft* 'strength, power; skill, art' ← PWGmc \**kraftu* ← PGmc \**kraftuz*, "further origin obscure" (Wikt). Wikt en gives *craft* a single etymology block, which covers the verb. No Latin path; no secure PIE root | **FITS**: "craft a sword", and the genre's word (crafting) | — |
| `mint` | S2 | FOLDED (craft) | `craft` at a mint, product `coin` | verb from the noun ← ME *mynt*, *munet* ← OE *mynet* ← PWGmc \**munit* ← L *monēta* (Wikt; L&S *Monēta*: the mother of the Muses, the temple of Juno Moneta where coin was struck) ← *moneō* ← PIE \**men-* 'think' (Wikt). **Latin entered Germanic early**, then English | **FITS**: strike coin | — |
| `build` | S3 | SHIPPED (REBUILD) | mints a Site (`Site.exists`, `Rung.stores` cost) or raises a works' fabric (`Site.condition`, `_rise`) | **Germanic.** ME *bilden* ← OE *byldan* ← PWGmc \**buþlijan* ← PGmc \**buþlą* 'dwelling' ← PIE \**bʰuH-* 'be, become, grow' (Wikt). No Latin path; L *fuī* is a cognate: the f- forms of *sum* (*fuī*, *fore*) and *fīō* are from PIE \**bʰúHt* 'become' (Wikt la *sum*) | **FITS**: "build the walls" covers beginning and continuing | — |
| `fortify` | S3 | FOLDED (build) | `build` of a garrison works | ME *fortifien* ← OF *fortifier* ← LL *fortificō* ← L *fortis* + *-ficō* (Wikt) ← PIE \**bʰerǵʰ-* or \**dʰerǵʰ-* (Wikt, disputed) | **FITS** | — |
| `improve` | S3 | FOLDED (build) | `build` of an upgrade works (M4) | AN *emprouwer* ← OF *en-* + *prou* 'profit' ← VL *prōde* (Wikt) [*prōde* is a reanalysis of *prōdest* 'is useful', third person of *prōsum* (Wikt la *prode*)] | **FITS**: "improve the harbour" | — |
| `found` | S3 | SHIPPED | mints a Rung, its `contain` edge, the founder's `hold`; moves the stake | ME *founden* ← OF *fonder* ← L *fundō, fundāre, fundāvī, fundātum*, L&S "to lay the bottom, keel, foundation of a thing, to found" ← *fundus* 'bottom' (L&S); *fundus* ← PIE \**bʰudʰmḗn* 'bottom' (Wikt la). Not *fundō, fundere* 'pour' (L&S *fundo*¹), a homograph | **FITS**: "found a town" | — |
| `raze` | S3 | NEW (v2: MB, p3:254) | ends a Site or a Rung (`Site.exists`/`Rung.exists`, `Tenure.until`) | ME *rasen* ← AN/OF *raser* ← VL \**rāsō* ← *rāsus*, ppp. of L *rādō, rādere, rāsī, rāsum*, L&S "to scrape, scratch, shave, rub, or smooth" ← PItal \**razdō*; **no secure PIE root** (Wikt: "perhaps" related to *rōdō*). The sense 'level to the ground' is English, from 'scrape' [century UNVERIFIED] | **FITS**: "raze a town" | — |
| `restore` | S4 | SHIPPED (REBUILD) | raises a worn Site no works names (`Site.condition`, `_rise` to full scale) | ME *restoren* ← OF *restorer* ← L *restaurō, restaurāre, restaurāvī, restaurātum*, L&S "to restore, repair, rebuild (perh. only post-Aug.)" ← *re-* + \**staurō* ← PItal \**stauros* ← PIE \**steh₂-* 'stand' (Wikt) | **FITS** for buildings; collides with TW's Mending (V-01) | — (TW renames its arm, 3.8) |
| `transfer` | S5 | SHIPPED | `Rung.stores` ×2; through a seat, `Tenure.term` | ← L *trānsferō, trānsferre, trānstulī, trānslātum*, L&S "to bear across; to carry or bring over; to convey over, transport, transfer" ← *trāns* + *ferō* ← PIE \**bʰer-* 'carry' (Wikt). Wikt en gives "From la trānsferō" directly, with no ME or French stage | **FITS**; overlaps `give` only by object (L-10, 3.5) | — |
| `pay` | S5 | FOLDED (transfer); behaviour shipped | `transfer` through a seat renewing `oblige` terms | ME *payen* ← OF *paiier* ← ML *pācāre* 'satisfy (a creditor)' ← L *pācō, pācāre* (Wikt: "to make peaceful, pacify … subdue"; LL/ML "to settle, satisfy") ← *pāx, pācis* ← PIE \**peh₂ḱ-* 'join, attach' (Wikt la). L&S *pāco*²: "to bring into a state of peace and quietness, to make peaceful, to quiet, pacify, subdue, soothe" (class.). Displaced OE *ġieldan* (Wikt) | **FITS**: pay wages, pay upkeep | — |
| `repay` | S5 | FOLDED (transfer) | `transfer` citing a `debt`; closes it on full payment | ← OF *repaier* ← *re-* + *paiier* (Wikt), then as `pay` | **FITS** | — |
| `haul` | S5 | FOLDED (transfer) | the distance cost on a transfer (M3) | ME *halen* ← OF *haler* ← Frankish \**halōn* or MDu *halen*, merging with OE \**halian* ← PGmc \**halōną* ← PIE \**kelh₁-* 'call' (Wikt). **Germanic via French**; L *calō* is a cognate (← PIE \**kelh₁-* 'call, shout', Wikt la) | **FITS**: carting goods | — |
| `relieve` | S5 | FOLDED (transfer); GV content | `transfer` to a rung in shortfall; `relief.given` | ME *releven* ← OF *relever* ← L *relevō, relevāre, relevāvī, relevātum*, L&S "to lift up, raise"; Wikt adds 'lighten, relieve' ← *re-* + *levō* (Wikt); *levō* ← *levis* 'light' ← PIE \**h₁lengʷʰ-* (Wikt la) | **FITS**: famine relief | — |
| `tribute` (to pay) | S5 | FOLDED (pay); term FA's | `pay` under a covenant term | noun: ME *tribut* (14th c.) ← MF *tribut* ← L *tribūtum*, ppp. of *tribuō, tribuere, tribuī, tribūtum*, L&S "to assign, impart, allot, bestow, give" ← *tribus* (Wikt); PIE of *tribus* disputed (Wikt header names \**tréyes* and \**bʰuH-*) | STRAINED as a verb (one "pays tribute") | "pay tribute" (a content, no row) |
| `smuggle` | S5 | PARKED (ban term, M7) | `transfer` past a held ban | earlier *smuckle* ← Du *smokkelen* or LG *smuggeln* ← PWGmc \**smeugan* (Wikt); further origin uncertain. **No Latin** | **FITS** | — |
| `exchange` | S6 | SHIPPED (REBUILD) | swap of two rungs' stores at the price (`Rung.stores` ×4); M10 | ME *eschaungen* ← AN *eschaungier*, OF *eschangier* ← VL \**excambiō* ← *ex* + LL *cambiō, cambiāre* (Wikt: "to exchange, barter; change"; L&S *cambio, īre*: "to exchange, barter … post-class. and very rare") ← *cambium*, **Gaulish**; no secure PIE root. Displaced OE *wrixlan* (Wikt) | **FITS**: "exchange grain for salt" | — (keep; no retrofit) |
| `trade` | S6 | FOLDED (exchange) | as `exchange` | **Germanic.** ME *trade* 'track, course' ← MLG *trade* ← OS *trada* ← PGmc \**tradō* ← PIE \**dreh₂-* (Wikt: "introduced into English by Hanseatic merchants"). The sense 'buying and selling' is later [century UNVERIFIED] | **FITS**: the genre's word | — |
| `buy` | S6 | FOLDED (exchange) | `exchange` giving `coin` | **Germanic.** ME *byen* ← OE *bycġan* ← PGmc \**bugjaną*, "of uncertain origin", perhaps PIE \**bʰūgʰ-* or \**bʰewgʰ-* (Wikt) | **FITS** | — |
| `sell` | S6 | FOLDED (exchange) | `exchange` taking `coin` | **Germanic.** ME *sellen* ← OE *sellan* ← PGmc \**saljaną* ← PIE \**selh₁-* (Wikt). OE *sellan* 'to give; to give up for money, betray; to sell' (Wikt OE) | **FITS** | — |
| `barter` | S6 | FOLDED (exchange) | `exchange` with no `coin` side | late ME ← OF *barater* (Wikt); further origin not given [UNVERIFIED] | **FITS** | — |
| `bargain` | S6 | FOLDED (exchange) | price set by a contest's degree (SC) | ME *bargaynen* ← OF *bargaigner* ← Frankish \**borganjan* ← PGmc \**burgijaną* ← PIE \**bʰergʰ-* (Wikt). **Germanic via French**; same root as `borrow` | **FITS**: haggle | — |
| `hire` | S7 | NEW | the hireling's service edge (`Tenure.since`, `Tenure.term`) + the first wage (`Rung.stores` ×2); M11 | **Germanic.** ME *hiren* ← OE *hȳrian*, from the noun OE *hȳr* ← PWGmc \**hūʀiju* ← PGmc \**hūzijaną* ← PIE \**kewHs-* (Wikt; an alternative root is left unnamed). It eclipsed ME *souden* ← OF *souder* 'pay soldiers' (Wikt). No Latin path | **FITS**, in the employer's voice (V-06) | — |
| `borrow` | S8 | NEW | advance (`Rung.stores` ×2) + a `debt` Record (`Record.exists`); M9 | **Germanic.** ME *borwen* ← OE *borgian* ← PGmc \**burgōną* ← PIE \**bʰergʰ-* (Wikt); the noun *borrow* meant 'a pledge, surety' (Wikt) | **FITS** | — |
| `lend` | S8 | NEW | as `borrow`, the creditor acting | **Germanic.** earlier *len* ← ME *lenen* ← OE *lǣnan* ← PGmc \**laihnijaną* ← \**laihną* 'loan' ← PIE \**leykʷ-* 'leave' (Wikt). L *linquō* a cognate, not ancestor (Wikt en cognate list: la *linquō*, grc *λείπω*) | **FITS** | — |
| `requisition` | S9 | SHIPPED (GV) | `Rung.stores` ×2 into the seat's treasury, under `purview` | ME *requisicion* ← OF *requisicion* ← ML *requīsītiō* ← L *requīrō, requīrere, requīsīvī, requīsītum*, L&S "to seek again; to look after, to seek or search for; to seek to know"; Wikt "ask for, request; need or miss" ← *re-* + *quaerō* 'seek', of uncertain origin (Wikt: per Nussbaum and De Vaan perhaps PIE \**kʷeh₂y-*) | **FITS**: a demand for supplies by authority | — |
| `tax` | S9 | FOLDED (requisition); GV | the rate on yield, `tax.collected` | ME *taxen* ← AN *taxer* ← L *taxō, taxāre, taxāvī, taxātum*, L&S "to touch sharply, to feel, handle"; Wikt adds "to rate, to appraise, to value, to estimate" ← probably PIE \**teh₂g-* 'touch' (Wikt). Displaced OE *gafol* 'tribute, rent' (Wikt) | **FITS** | — |
| `toll` | S9 | PARKED (M3) | `tax` at a route rung | ME *toll* ← OE *toll*, *toln* ← PGmc \**tullaz* ← PIE \**del-* 'count' (Wikt); **disputed**: alternatively ← ML *tolōneum* ← L *telōnium* ← Gk *telṓnion* (Wikt) | **FITS** (noun use; "to toll" is rare) | "levy a toll" as content |
| `hoard` | S10 | PARKED (draw policy) | withholding stores from a larder's draw | **Germanic.** ME *horden* ← OE *hordian* ← PWGmc \**hoʀdōn*; noun ← PGmc \**huzdą*, unknown origin, possibly PIE \**(s)kewH-* 'hide'; L *custōs* a cognate, not an ancestor (Wikt) | **FITS** | — |
| `appraise` | — | CULLED | — | ME *apreisen* ← OF *aprisier* ← LL *appretiō* ← *ad-* + *pretium* (Wikt); *pretium*: L&S "that for or by which any thing is bought or sold"; Wikt "worth, price, value, cost; pay, hire, wage" ← PIE \**per-* (Wikt, "perhaps") | FITS, but collides with "appraisal" (EC-G20) | — |

*Not verbs, recorded for the reader:* **price** (ME *price* ← OF *pris* ← L *pretium*, Wikt) is a
Query (M10); **debt** (ME *dette* ← OF *dete* ← ML *dēbita* ← L *dēbitum* ← *dēbeō* ← *dē* + *habeō*,
Wikt; PIE \**gʰeh₁bʰ-*, Wikt) is a Record kind (M9).

---

## 3.5 Deduplication and culls

### Groups that cover one act, and what was done

| group | ordinary-English overlap | discriminator kept (from reads/writes/emits, not roots) | action |
|---|---|---|---|
| `work` / `restore` / `build` | "work on the walls", "restore the walls", "build the walls" | `work` → labour read by yield; `build` → mint or raise a works' fabric; `restore` → raise a worn, unplanned fabric | `work`'s works-advance moved to `build`; one formula (`_rise`) for raising and repair |
| `transfer` / `give` (L-10) | "give grain", "transfer a deed" | `give` moves a Record's `hold` between co-located persons (`verb_table.yaml:433`); `transfer` moves stores between rungs (:1261) | kept both; the split is by object, a declared convention the words do not carry; `give` is SC/MB's |
| `transfer` / `exchange` / `requisition` / `give` (EC-G09) | all "move things" | one-way by consent (`transfer`); two-way by both consents (`exchange`); one-way by authority into a treasury (`requisition`); a Record hold (`give`) | kept four; each writes a different consent shape |
| `requisition` / `tax` / tribute (EC-G03) | all "take for the seat" | `tax` = rate × known yield, customary; `requisition` = a demanded amount from stores, extraordinary; tribute = a covenant term paid by `pay` | `tax` folded into `requisition` (GV); tribute to FA |
| `trade` / `buy` / `sell` / `barter` / `bargain` / `exchange` | one act seen from either side, with or without coin | the `coin` side and the price source are parameters | one row, `exchange` |
| `lend` / `borrow` | one transaction, two voices | the initiating party | two rows, one effect owner |
| `hire` / `oblige` (V-06) / `recruit` | "join" vs "take on" | `hire` = employer opens the hireling's edge and pays; `oblige` = the joiner opens his own | `hire` NEW; `oblige` unchanged (its rename to `pledge`, L-02, is NP/FA's) |
| `found` / `build` / `establish` (L-07) | "found a town", "build a town", "establish an office" | `found` mints a Rung; `build` a Site; `establish` an Office | `found`/`build` kept apart; `establish` GV's |
| `restore` / `mend` (V-01) | "mend the wall" | `restore` writes `Site.condition`; `mend` (TW) is Mending | `restore` narrowed to fabric; Mending to TW's `mend` |
| `craft` / `forge` (smith) | "forge a blade" | the shipped `forge` mints a false `faction_sheet` (`verb_table.yaml:330-348`) | smithing is said `craft`; `forge` keeps the forgery sense (a reader may stumble; L-11's leak is separate) |
| `craft` / TW `weave` | "weave cloth" | TW's `weave` is threadwork | cloth is a `craft` product; no economic `weave` |
| `haul` / `carry` (EC-G08) / `transfer` | "carry goods" | `carry` docks a petition (`verb_table.yaml:105-127`); `haul` is a cost on `transfer` | no row for carriage; `carry` → `lodge` is SC's (L-04) |
| `appraise` / `examine` / `survey` | "assess" | price is a Query; valuation is FI's `examine`; assessment is FI's `survey` | `appraise` culled |
| `hoard` / `ration` / `conceal` | "hold back" | one missing draw policy | `hoard` parked with `ration`; hiding stores is `conceal`'s (FI) |
| `due` / `debt` (V-19) | "dues" ≈ "debts" | no `due` writ remains (tax is not an `issue` content here) | only `debt` survives |

### Culls, each with its fold test and floor check

| cull | fold test | what dies | floor check |
|---|---|---|---|
| `appraise` (CULL) | vs `examine`: Y / N / N | an act of valuing that writes nothing but a belief | nothing a floor act needs dies: price (floor) is a Query a person at the rung reads by presence; a remote price arrives in a telling of `exchange.made`, whose Event carries the amounts [ASSUMPTION: that a telling's claim carries the amount; basis: tellings relay witnessed Events, `verb_table.yaml:985` row]. *Falsifier:* a player who cannot learn a rung's price without an act |
| `work`'s works-advance arm (moved, not culled) | into `build`: Y / Y / Y | nothing | — |
| `smuggle`, `toll`, `hoard` (PARKED, not culled) | each folds on its host when its trigger lands | — | floor kept: trade, tax, stockpile are carried by `exchange`, `requisition`/`tax`, `build` + M12 |
| v2's retirement of `exchange` (REVERSED) | `exchange` → `covenant`: N / N / N | — | trade is floor; a covenant is FA's binding, not a swap |

### Over-distillation watchlist (NERS §5.2)

| watched | the N it protects | verdict |
|---|---|---|
| `restore` kept beside `build` though the fold test passes | repair without a works or a cost | kept, MEDIUM: a host must name its folded act; if `build` were read as "raise any fabric", `restore` is redundant |
| `borrow` and `lend` as two rows | the creditor's and the debtor's initiative | kept, MEDIUM: one row with an initiator parameter is the alternative, and it names one party in the wrong voice |
| `bargain` folded into `exchange` | a contested price | folded, MEDIUM: if SC builds a bargaining contest of its own, the degree enters `exchange` as a parameter and no row is needed |
| `tax` folded into `requisition` | the customary/extraordinary distinction | folded, MEDIUM: GV may head the row with `tax` instead (3.8) |
| `mint` folded into `craft` | coinage as a prerogative | folded, LOW: if minting must be a seat's act alone, the seat clause is a GV eligibility, not a new row |

### Critics' findings on EC verbs

| finding | disposition |
|---|---|
| **L-01** root sense as design intent | **applied.** No merge here rests on a root. *taxō* has the attested sense "to rate, to appraise" (Wikt), close to `appraise`; nothing is built on that |
| **L-02** `oblige` runs the wrong way | **applied** to `hire` (employer's voice); the rename itself is NP/FA's |
| **L-03** `levy` reassigned; the hole register still says `levy` | **applied, with a caution.** Counted: `grep -c levy engine/season/hole_register.yaml` = 19 lines, `requisition` = 0. Some rows use `levy` in the troop sense (`hole_register.yaml:592`, "`levy` naming hands" as a demand source): re-key by sense, not by string (EC-G02) |
| **L-04** `carry` reads as adoption | **answered**: not EC's row; the transport sense lives on `transfer` (haul) |
| **L-06** `work` holds two senses | **applied** (S1, S3) |
| **L-07** `found` / `establish` / `build` | **answered** for `found`/`build` (carrier and gate basis differ; Civilization keeps Found City apart); `establish` is GV's |
| **L-10** `give` / `transfer` | **answered**: kept by object; both words fit; no rename |
| **L-11** `forge` leaks its falsity | **noted**; adds the smithing-sense collision with `craft` |
| **L-18** `remit:issue` gates `requisition`, `seize`, `transfer` | **answered** (architecture, §0 step 5): a requisition, a tax and a payment out of a treasury are each *issued*; the substitution is the tree's own precedent on three rows; GV to confirm (EC-G06) |
| **V-01** `mend` / `restore` double cover | **applied**: `restore` keeps the fabric only |
| **V-06** hire in the hireling's voice | **applied**, further than the critic: not "`tell` + `oblige` + `transfer`" but one employer's row |
| **V-15** `tax` waits on `evade / defy` | **answered**: `tax` is no longer an `issue`d writ answered by `comply`; the store moves when the act executes. The answer to extraction stays GV/SC's (EC-G04 PARKED) |
| **V-16** ransom → `pardon` + `transfer` | **noted**: FA's; the payment half is `pay` |
| **V-19** `due` / `debt` | **applied**: no `due` |
| **V-20** `yield` homonymy | **noted**: `Rung.yield` is EC's carrier name; a duel term `yield` beside it is PC's to rename |
| **V-11** `invest` as a siege posture | **supported**: EC now has `lend`/`borrow`/`debt`, so the economic sense of "invest" would mislead |
| **V-21** `Trade`, `Fortify` in `action_vocabulary.yaml:28, :33` | **applied**: Trade → `exchange`; Fortify → `build` (garrison works) |

---

## 3.6 Gap coverage table

One disposition per row. "once Mn" names the 3.7 mechanic the verb waits on.

| gap id | closed by (verb / suite) | PARKED (trigger) | OUT OF SCOPE (why) | STALE (cite tree) | DISPUTED (why) |
|---|---|---|---|---|---|
| EC-G01 | | | | the rename landed: `verb_table.yaml:646` is `requisition` (36b951c); the troop verb `levy` is MB's (`troop-stock-design.md` §3.1) | |
| EC-G02 | | | an editorial re-key of `hole_register.yaml` (19 lines say `levy`, 0 say `requisition`, counted), IN's; re-key by sense: `:592` uses the troop sense | | |
| EC-G03 | S9: `tax` folded into `requisition`; tribute paid by `pay` (S5), its term FA's | | | | |
| EC-G04 | | `evade / defy` made resolvable (GV/SC; V-15); EC's store half exists | | | |
| EC-G05 | `requisition` / `tax` once M16 | | | | |
| EC-G06 | `requisition`, answered by architecture: a requisition is issued; `remit:issue` gates `seize` (`verb_table.yaml:902`) and `transfer` (:1249) too; GV to confirm | | | | |
| EC-G07 | `requisition` once M15 | | | | |
| EC-G08 | | | SC's `carry` (rename `lodge`, L-04); the transport sense is `transfer`'s haul cost | | |
| EC-G09 | 3.5's discriminators (S5, S6, S9) | | | | |
| EC-G10 | `transfer`'s named contents with earned kinds (`term.renewed`, `debt.repaid`, `relief.given`); `bribe` is FI/SC's row | | | | |
| EC-G11 | `transfer` once M8 | | | | |
| EC-G12 | `work` (REBUILD: the effect becomes production, and the name then fits) | | | | |
| EC-G13 | the S1 / S3 / S4 split (`work` produces, `build` raises a works, `restore` repairs) | | | | |
| EC-G14 | `restore` (narrowed to fabric) once TW moves IN-35's arm to `mend` (3.8) | | | | |
| EC-G15 | | a ruling on whether an uncontested act takes a degree (H-164; `effects_economy.py:113-121`); IN | | | |
| EC-G16 | `exchange` once M10 and M14 | | | | |
| EC-G17 | | | ransom is FA's (v2 V152); office sale is GV's `confer` (a seat is a `hold`, not stores) | | |
| EC-G18 | `exchange` once M10 | | | | |
| EC-G19 | `exchange` once M10 (price and value; no floor act needs quality) | | | | |
| EC-G20 | the cull of `appraise` (3.5) | | | | |
| EC-G21 | `craft` (mint) once M2, with a coin seed at world build | | | | |
| EC-G22 | | | | | the unpaid-upkeep outcome splits precedent and changes the game: 3.9 item 1 |
| EC-G23 | | | a value, not a verb: `default_upkeep=1`, swept 0/1/3 (`data/fixtures.py:856-868`, H-158) | | |
| EC-G24 | `borrow` / `lend` once M9 | | | | |
| EC-G25 | | `tax` built and a GV seat conferrable as a collection right | | | |
| EC-G26 | | M10 reads coin and M2 mints it | | | |
| EC-G27 | `tax`: a rate on yield moves with `season_factor`, which yield already reads (`rosters.yaml:2180-2185`) | | | | |
| EC-G28 | | | the proclaiming act is GV/FA's; EC's reader is `exchange` refusing across a held ban (M7) | | |
| EC-G29 | | toll: M3; staple right and licence: M7 (GV/FA charters) | | | |
| EC-G30 | | M7 (a held ban term) | | | |
| EC-G31 | | a draw-policy ruling, with WT's `ration` (v2 V148's trigger, p8:482) | | | |
| EC-G32 | | | crime; NP/FI; refused by the plan (VCD K-51) | | |
| EC-G33 | `hire` once M11 | | | | |
| EC-G34 | `pay` (arrears) once 3.9 item 1 is ruled; the Contribution System is `requisition` under occupation (WT/MB's forage basis) | | | | |
| EC-G35 | | | FA's: a guild withdrawal is a ban on `exchange` with a faction (M7); a protected tributary is a covenant | | |
| EC-G36 | | | FA's covenant term; the paying half is `pay` | | |
| EC-G37 | `transfer` (haul cost) once M3 | | | | |
| EC-G38 | `craft` once M2 | | | | |
| EC-G39 | `craft` (arms) once M2 and arms matter kinds | | | | |
| EC-G40 | `work` (cultivate) once M1 and M6 | | | | |
| EC-G41 | `work` once M1 | | | | |
| EC-G42 | `work` once M6 | | | | |
| EC-G43 | `build` (a storehouse kind) once M12 | | | | |
| EC-G44 | S5 / S6 / S8: Open Granary and Relief = `transfer` (`relieve`); Provision = `transfer`; Foreign Loan = `borrow`; Fix Prices = a GV cap read by M10 | | | | |
| EC-G45 | `raze` (the closer) once M13; cost and holder landed at IN-28 (`verb_table.yaml:371, :383, :406`) | | | | |
| EC-G46 | `build` / `found` once M5 (`work` no longer needs a works) | | | | |
| EC-G47 | `raze` once M13 (`sabotage` is FA/FI's, 3.8) | | | | |
| EC-G48 | | | FI's `survey`; EC depends on it through M15 (tax on the seat's assessed yield) | | |
| EC-G49 | `build` (fortify: a works planning a `garrison`) | | | | |
| EC-G50 | | M11, and a GV ruling on corvée as a seat's unpaid labour demand | | | |
| EC-G51 | `build`: through a seat (Develop) or from one's own stores (Sponsor), paid from the works' rung (`rosters.yaml:1394-1396`) | | | | |
| EC-G52 | | M9 and M10 built; charters are GV's `confer` of a monopoly (M7) | | | |
| EC-G53 | `tax` (the rate is its parameter) | | | | |

Count: 53 rows; closed 33 · PARKED 9 · OUT OF SCOPE 9 · STALE 1 · DISPUTED 1 (counted by script
over this table; each row has exactly one filled disposition).

---

## 3.7 Mechanics this subsystem needs (named gaps)

| id | mechanic | what it must write | verbs waiting |
|---|---|---|---|
| M1 | a per-season labour tally on a Site, read by MATTER's yield (factor ≡ 1 as the control arm) | a staged labour count per Site; `Rung.yield` reads it | `work` (cultivate, mine, fish) |
| M2 | `recipes` roster and workshop `site_kinds` (smithy, mint, mill …), plus arms and tool `matter_kinds` | the loader's tables; `Rung.stores` conversion in `craft`'s effect | `craft`, `mint` |
| M3 | a season Query over `settlement_adjacency` pricing distance | a carriage cost on `transfer` and `exchange` between non-adjacent rungs | `haul`, `toll`, `smuggle` |
| M4 | a works planning an upgrade of a Site that exists | a higher ceiling on that Site | `improve` |
| M5 | a computed producer of works Records (a question a planner answers with `create_record` of kind works) | `Record.exists` (works) | `build`, `found` in computed play |
| M6 | production geography: a `field` kind and site kinds by settlement type | `site_kinds`, `site_yield` rows; world-build placement | `work` (cultivate) |
| M7 | a ban term (a held writ forbidding trade across named rungs or factions) | a Record content read by `exchange`'s and `transfer`'s preconditions | `smuggle`; GV/FA's embargo, staple, guild withdrawal |
| M8 | `transfer`'s computed `to`: a rung other than the giver's own (a referent's rung or an obligee's home) | the act's operand | `transfer`, `pay`, `relieve` |
| M9 | a `debt` Record kind (creditor, debtor, kind, sum due, due season) matured at MATTER | `Record.exists`; `debt.lapsed` at the due season; closed by `repay` | `borrow`, `lend`, `repay` |
| M10 | `price_of(rung, kind)`: a Query from stores against draw and upkeep, stored nowhere, capped by a GV edict where one is held | nothing (a read); `exchange` reads it | `exchange` and its folds |
| M11 | a gate basis admitting an edge opened by the employer when the wage moves in the same write (`handover`'s shape) | `Tenure.since` + `Tenure.term` on the hireling's edge | `hire` |
| M12 | a storage bound on `Rung.stores` read from storehouse Sites | a cap the yield and `transfer` writes respect, refusing above it | stockpile (via `build`) |
| M13 | `raze`'s effect | `Site.exists` / `Rung.exists` closed; dependent `contain` and `hold` edges closed | `raze` |
| M14 | one operand, `return_kind`, added to the closed `requires_operands` (`verb_table.yaml:654`) | the act's operand | `exchange` |
| M15 | yield observed: `yield.taken` carries `observed` so a seat holds a claim of a rung's yield | a ledger claim | `tax`, `requisition` (EC-G07) |
| M16 | a `deed:` cell reading a take from a rung in shortfall as a grievance (GV/SC own the cell) | witness deposits | `requisition`, `tax` (EC-G05) |

---

## 3.8 Cross-subsystem flags

| other lane | verb | the collision or dependency |
|---|---|---|
| **GV** | `requisition`, `tax` | Acts of governance through a seat: GV owns the row; EC owns `_shift` and M10/M15. GV picks the head word (`requisition` shipped and just renamed; `tax` is the floor word); EC recommends keeping `requisition` with `tax` as a content to avoid a second rename |
| GV | `relieve` (v2 V149) | a `transfer` content; GV owns the `deed:relief.given` cell |
| GV | Fix Prices, Set Assize, narh | an edict whose cap M10 reads; no EC row |
| GV / FA | embargo, staple right, licence, guild withdrawal | each is a ban term (M7) a seat or faction proclaims; EC reads it in `exchange`/`transfer` preconditions |
| GV | corvée / Mit'a (EC-G50) | the unpaid, compelled form of `hire`; parked on M11 |
| GV | distraint on a lapsed `debt` | widen `seize` (a Record or Rung today, `verb_table.yaml:911`) to stores, or give `requisition` a debt basis; EC does not build it |
| GV | `establish` (L-07) | `found`/`build` keep their discriminator; the `establish`/`amend` split is GV's |
| GV | `mint` | whether coinage is a seat's prerogative (an eligibility on `craft` at a mint) or open to anyone present |
| GV / SC | `evade / defy` (V-15, EC-G04) | the taxed rung's answer; EC-G04 parked on it |
| **FA** | `covenant` goods terms | v2's "retire `exchange` with `covenant`'s goods keys" is **rejected** here (S6): a trade treaty's terms are performed by `exchange`/`transfer`; FA owns the binding |
| FA | tribute, protected tributary | a covenant term paid by `pay` (EC-G36) |
| FA | ransom (V152) | the payment half is `pay`; the release is FA's |
| FA / FI | `sabotage` (v2 FA, p4:215) | lowers `Site.condition`; reads EC's fabric, not EC's row |
| **MB** | `raze` | v2 filed it under MB (p3:254); one row either way: EC writes the place carriers, MB's occupier is a common actor. Agree the owner |
| MB | `levy` (troops) / `requisition` | the hole register's 19 `levy` lines must be re-keyed by sense (EC-G02); MB's `levy` takes the troop sense |
| MB | arms for `equip` | `craft` makes arms (S2); the troop design's "arms have no producer" (`troop-stock-design.md:101-104`) closes on M2 |
| MB / FA | mercenary hire | `hire` over a captain whose troop stock then serves the employer's seat, or MB's own act: MB to say whether a company is hired as a person or bought as stock |
| MB / WT | forage, contribution, sack | `requisition` under an occupation basis (v2 V110, V088) |
| **WT** | `haul` / M3 | the adjacency Query is shared with `move`/`march` (WT-G06, WT-G08) |
| WT | `hunt` (V167, CUT on W8) | with M1, hunting is `work` at a wild site and MATTER mints the yield: W8 holds and the verb survives as a content |
| WT | `ration` / `hoard` | one draw policy; parked together |
| WT | `provision` (V111) | a `transfer` to a force's seat |
| WT | Plant Colony / frontier charter (WT-G42) | a `found` content |
| **TW** | `restore` / `mend` (V-01) | EC keeps `restore` for Site fabric only; TW should take IN-35's Mending arm to `mend` |
| TW | `weave` | cloth is a `craft` product; no economic `weave` |
| **SC** | `bargain` | a contest whose degree moves `exchange`'s price; SC owns the contest |
| SC | `give` / `transfer` (L-10) | kept apart by object |
| SC / FI | `bribe` (V140) | composes on `transfer`'s store write; not EC's row |
| **FI** | `appraise`, `survey` | valuation is `examine`'s content; tax reads a yield the seat knows (M15), which a cadastral `survey` would supply |
| FI | `forge` | the smithing sense of "forge" collides with the forgery row; EC says smithing with `craft` |
| FI | `conceal` | hiding stores is `conceal`'s, not `hoard`'s |
| **NP** | `oblige` → `pledge` (L-02) | the hireling's own joining act; `hire` opens the same edge kind from the employer's side |
| NP | the hireling's season | the chooser must read a service edge to direct `work`/`build` to the employer's sites |
| NP | `borrow` | formed from a need (`rosters.yaml:584`, question sources `claim_landed`, `need`) |
| **PC** | duel term `yield` (V-20) | homonym of `Rung.yield`; PC to rename its term |
| **IN** | `requires_operands` | +1 member (`return_kind`, M14); H-164 (degree on uncontested acts); W8's scope |

## 3.9 For Jordan

1. **What happens when upkeep goes unpaid (EC-G22, H-159).** (a) The term lapses and service ends:
   the shipped shape (MATTER matures an `oblige` term, `verb_table.yaml:860`), Mount & Blade's
   desertion [MEMORY]. (b) The unpaid term becomes arrears, a `debt` (M9) the seat owes the obligee;
   service continues under a grievance until a cap: recoverable insolvency, as in the Wealth-0
   handling the SE lane lists (`SE_settlements_territory_economy.md:100`) and CK3's debt [MEMORY].
   *Tried first:* superseded (no later ruling found; H-159 is open per the register); irrelevant (no:
   the term is shipped); design document (PMM :397-402 against :511 contradict, per the register,
   not opened by me); precedent (splits); architecture (both run on shipped carriers; (b) adds M9,
   which S8 needs anyway). The choice decides whether a broke seat loses its men at once or slides
   into a debt spiral, and so what EC-G34's arrears and mutiny are.

No other item survives the five tests: the head word of the revenue row is GV's; `raze`'s owner is a
lane agreement; W8's scope for `craft` is answered by precedent (S2); coinage as prerogative is GV's.

---

## Self-audit (NERS §9) and limits

- **Backward propagation, run.** S2's pointer to a 3.9 item was withdrawn when that item was answered
  by precedent; S5's EC-G22 claim was narrowed to match 3.6 (DISPUTED); 3.6's count was re-taken by
  script (33 closed, not 34). [SELF-AUTHORED: bias risk.] An independent reviewer would test the
  three judgment calls marked MEDIUM in 3.5's watchlist and the `exchange` consent model (a
  counterparty's acceptance read from his own rung's price is a design claim with no shipped instance).
- **Disqualifier 3 on this file's additions.** `craft` (v2: data row), `hire` (v2: merge), `lend`/
  `borrow` (v2: `debt` content of `transfer`) and the `exchange` rebuild (v2: retire) each re-add what
  v2 merged; each names v2's disposition and why the fold test fails it.
- **Not done.** No engine run; no execution counts re-measured (the register's are carried as its
  sources state them). Not opened: PMM, `.designs/`, the `research/by_lane/FA_*.md` line for Arte
  della Lana, PW §1.3a, FASE T3/T8 (cited "via the register"). L&S for *pācō* failed to fetch.
- **Rows after assessment (EC-owned):** `work`, `craft`, `build`, `found`, `raze`, `restore`,
  `transfer`, `exchange`, `hire`, `borrow`, `lend` = 11 (6 shipped, 5 new); plus `requisition`
  (shipped, handed to GV). Named folded acts: 17 (cultivate, mine, fish, mint, fortify, improve,
  pay, repay, haul, relieve, tribute, trade, buy, sell, barter, bargain, tax). PARKED: `smuggle`, `toll`, `hoard`. CULLED:
  `appraise`.

