# Persons, attributes and verbs: the v2 synthesis — part 17: Part VI.9, world, travel and survival (WT)

## Status: PROPOSED (2026-10-17). Reference, not canon (`CLAUDE.md` §0.05): nothing here binds the game or is read by it. Merging ratifies nothing unless Jordan so rules. Static reading and static lookup only; no run.
## Parts, in reading order: [head](2026-10-16-v2-person-troop-attribute-synthesis.md) (§0, Part I Persons) · [`_part2`](2026-10-16-v2-person-troop-attribute-synthesis_part2.md) (Part II Attributes) · [`_part3`](2026-10-16-v2-person-troop-attribute-synthesis_part3.md) and [`_part4`](2026-10-16-v2-person-troop-attribute-synthesis_part4.md) (Part III Verbs: standards, roster, reconciliation; critics, etymology audit, gap coverage, named mechanics, decisions) · [`_part5`](2026-10-16-v2-person-troop-attribute-synthesis_part5.md) and [`_part6`](2026-10-16-v2-person-troop-attribute-synthesis_part6.md) (Part IV What verbs do to the world) · [`_part7`](2026-10-16-v2-person-troop-attribute-synthesis_part7.md) (§5 Roadmap, §6 Reliability ledger, §7 Sources) · [`_part8`](2026-10-16-v2-person-troop-attribute-synthesis_part8.md) (Part V: engine findings carried from the first-pass trial) · Part VI, the lexicon by subsystem: [`_part9`](2026-10-16-v2-person-troop-attribute-synthesis_part9.md) PC · [`_part10`](2026-10-16-v2-person-troop-attribute-synthesis_part10.md) MB · [`_part11`](2026-10-16-v2-person-troop-attribute-synthesis_part11.md) SC · [`_part12`](2026-10-16-v2-person-troop-attribute-synthesis_part12.md) FI · [`_part13`](2026-10-16-v2-person-troop-attribute-synthesis_part13.md) TW · [`_part14`](2026-10-16-v2-person-troop-attribute-synthesis_part14.md) GV · [`_part15`](2026-10-16-v2-person-troop-attribute-synthesis_part15.md) FA · [`_part16`](2026-10-16-v2-person-troop-attribute-synthesis_part16.md) EC · **this file** WT · [`_part18`](2026-10-16-v2-person-troop-attribute-synthesis_part18.md) NP · Part VII, the verb gap register (the evidence behind Part VI's coverage tables): [`_part19`](2026-10-16-v2-person-troop-attribute-synthesis_part19.md) PC+NP · [`_part20`](2026-10-16-v2-person-troop-attribute-synthesis_part20.md) MB+FA · [`_part21`](2026-10-16-v2-person-troop-attribute-synthesis_part21.md) SC+GV · [`_part22`](2026-10-16-v2-person-troop-attribute-synthesis_part22.md) FI+TW · [`_part23`](2026-10-16-v2-person-troop-attribute-synthesis_part23.md) EC+WT.

**How to cite this Part.** The lane's own sections are numbered 3.1 to 3.9; cite them as `WT §3.n` (for example `WT §3.9` for its items for Jordan). Gap ids (`WT-G01` …) resolve in Part VII (`_part23`). Abbreviations such as `VT`, `VCD`, `v2-p3` are defined in the lane's opening paragraphs; `v2-p3`, `v2-p4`, `v2-p8` are the first-pass v2 parts as filed at `716c253`. Mechanic ids (`M1`, `M-1`, `M-WT-1`) are this lane's own.

**Rulings that override this section** (`_part3` §III.5; where this section and the roster disagree, the roster governs):

- R-08: `forage` is **MB's** row; WT keeps `camp` (parked, hosting `encamp`).
- R-09: `explore` is WT's.
- R-10: `move` → `travel` is adopted in the rename batch.
- R-27: `hunt` is a content of EC's `work`.

---

# WT — world, travel and survival

Built 2026-10-16 from the working tree at `716c253`. Inputs: `the lane brief.md`; gap register `gaps/L5_EC_WT.md`
(WT-G01…WT-G43; EC rows skimmed for collisions); critics `L_lexicon.md`, the v2-claims critic (Part III §III.7); v2 `_part4.md`
§WT (:300-347) and `_part8.md` §V.3 WT (:512-522), §V.2.13 (:350-362), §V.4 (:555-604), closest calls
(:658-696). Every `file:line` below was opened in this session unless tagged. Nothing here is a mechanism
(CLAUDE.md §0.05): it proposes rows and names the code they would need.

Abbreviations: VT = `engine/season/verb_table.yaml`; WQ = `engine/season/queries/world_q.py`; GEO =
`systems/settlements/valoria_geography_v30.yaml`; FX = `engine/season/data/fixtures.py`; M-WT-n = a
mechanic in §3.7. Game precedents from my own knowledge are tagged `[MEMORY]` with the mechanic named.

---

## 3.1 Subsystem mechanic

**What runs.** One journey body and one clock. `move` (VT:743) and `migrate` (VT:719) share
`_relocate` (`loop/effects_migration.py`): close the traveller's live `contain` Tenure, open one to `to`,
append `to` to `Person.travel_leg`. `migrate` also re-homes `reside`, emits `residence.changed`, and is
throttled by `WQ.capacity` (VT:732, :739). `march` (VT:683, MB's) reuses the same body for the arriving
army (VT:701). Preconditions: `contain_path` (`data/requires.py:374`) asks only whether the two places
share an ancestor in the containment tree; `World.contain_ascends` (`state/world.py:292`) checks the kind
ladder. Neither reads distance. Price: `decision/budget.py:60` subtracts `len(travel_leg) ×
budget_leg_penalty` (FX:500, value 1); the next MATTER empties the leg and emits `travel.ended`
(`loop/matter.py:540-580`). Custody declines both verbs (`effects_migration.py:73-83`). Clock: `w.tick`
is the season. `WQ.season_of_year` (:738-744) exists only when `season_factor_draw` declares a table, and
it ships empty (FX:442), so **the shipped world has no year**. The weather draw's one reader is yield
(`matter.py:291-293`). Bodies fall only in the body pass (`matter.py:454`; `body_step` 0, FX:567), and
**only a cohort eats** (WQ:816-829, ED-IN-0255, ruled).

**What it lacks.** A world to travel through. `data/geography.py` parses GEO only for the battle field.
`modules/mass_battle/terrain.py` reads `provinces`/`terrain`/`water` in code; it names
`terrain_cost_matrix` and `settlement_adjacency` only in comments (:61, :123, :162). By my grep, nothing
in `engine/`, `modules/` or `systems/*/sim` reads these GEO keys: `settlement_adjacency` (:594),
`terrain_cost_matrix` (:760), `vision_range` (:775), `march_budget` (:800), `bridges` (:821),
`forgetting_zone` (:835), `radiation_bands` (:842), `poi_catalog` (:893). So the engine has no distance,
no route, no water passage, no seasonal window, no exposure and no discovery.

---

## 3.2 Convention floor

These are the acts a player of a game with a strategic travel layer and personal-scale survival
expects. Status: *shipped* = a VT row; *designed* = v2/VCD/XSC only; *absent* = nowhere.

| # | floor act | precedent (in-tree path:§ / named game [MEMORY] + its mechanic) | status |
|---|---|---|---|
| F1 | **Travel** from place to place, paying time | XSC §6.4 :664 ("adjacent territory = 1 scene of travel"); COMP-5 :144 (CK3 levies rationed "temporally (muster travel time)"); Mount & Blade [MEMORY: the party crosses the campaign map at a speed set by its slowest troops, horses and terrain]; CK3 [MEMORY: travel plans with a route, a duration and a travel leader] | shipped (`move`) |
| F2 | **Go farther or faster by road, mount or water**: distance and terrain cost | GEO :760-804 (terrain cost, march budget with `cavalry_modifier` 1.5); PW §1.3a :36; Mount & Blade [MEMORY: mounted troops raise party speed; forest and snow lower it]; Total War [MEMORY: movement points per turn, reduced by terrain, extended by roads] | absent (the data exists; nothing reads it) |
| F3 | **Find the way** (pathfinding, guiding, not getting lost) | AFS2 :259 ("Find the way (navigate, track)"); The One Ring 2e [MEMORY: journey roles Guide, Scout, Hunter, Look-out; the Guide's roll sets fatigue and hazards]; Dungeon World [MEMORY: "Undertake a Perilous Journey": trailblazer, scout and quartermaster each roll]; Torchbearer [MEMORY: a Pathfinder test to cross wilderness, failure brings a twist or a condition] | designed (V162; cut, `_part8.md:516`) |
| F4 | **Cross water**: ford, bridge, sail | GEO :806-833 (navigable river, lake, two bridges); HCC §2.8 :133-141 (Flota Scheduling, Storm-Season Withdrawal); CK3 [MEMORY: armies embark at sea, with attrition risk on long voyages] | designed (V164 reader, `_part8.md:518`) |
| F5 | **Move house / emigrate**, throttled by room | RR-2 (VT:713-717 quote: "accept people who move settlements"); FASE SE-10 :298-302 (Hirschman exit); Dwarf Fortress [MEMORY: migrant waves arrive each season, capped by the fortress's population cap]; Banished [MEMORY: nomads arrive and need housing] | shipped (`migrate`) |
| F6 | **Feed a force off the land** (supply, attrition, foraging) | PW §1.3a :34-43 ("Campaign Supply"); CK3 [MEMORY: county supply limit; armies above it, in hostile land or in winter, take attrition]; Total War Rome II / Attila [MEMORY: a raiding stance feeds the army and damages the region]; Hearts of Iron IV [MEMORY: supply hubs and lines; units out of supply lose strength] | designed (V110 → `requisition`, `_part8.md:411`) |
| F7 | **Hunt / forage for one's own party** | Oregon Trail [MEMORY: hunting fills the wagon's food, limited by carry weight]; Torchbearer [MEMORY: hunger and thirst as conditions; a survivalist test finds food] | **excluded by ruling**: ED-IN-0255 (Jordan: subsistence is "a territorial issue"; named persons do not eat, WQ:816-820) |
| F8 | **Camp / rest / winter quarters** | PW §1.3a :36 (campaigns May–October); Dungeon World [MEMORY: "Make Camp" consumes a ration and heals]; Torchbearer [MEMORY: the camp phase recovers conditions]; Mount & Blade [MEMORY: waiting in camp heals the wounded over days] | designed (V108 encamp, cut, `_part8.md:409`) |
| F9 | **Weather and hazard on the road** | XSC §6.4 :664-665 (Calamity territory: "Endurance check Ob 1 per territory or take 1 Exposure"); GEO :835-873 (Forgetting zone, radiation bands); Oregon Trail [MEMORY: weather and river crossings cost health and goods]; Frostpunk [MEMORY: temperature drops as the dominant pressure] | designed (XSC); not a chosen act (§3.3 S1) |
| F10 | **Explore and discover** | XSC §6.4 :661-669 (Discovery Procedure; POI types); GEO :893-913 (`poi_catalog`); Civilization [MEMORY: scouts lift fog of war and find huts and wonders]; Pathfinder *Kingmaker* [MEMORY: hex exploration reveals sites and resources]; Battle Brothers [MEMORY: locations appear when the party travels near] | designed (XSC); absent in code |
| F11 | **Seasons**: a year whose winter changes what travel and war cost | GEO :792-796 (`season_factor` spring…winter on vision); PW §1.3a :36; Banished [MEMORY: winter stops crops and kills the unclothed]; CK3 [MEMORY: winter severity raises attrition] | partly shipped (tick; the year is off by default) |

Beyond the floor (precedent but no convention): evacuation and relocation (HCC §2.4 :77-89), route
infrastructure (PGS T1/T3/T6/T19), quarantine (HCC §2.7). These are argued on NERS in §3.3 and §3.6.

---

## 3.3 Suites

There are five suites. Four are WT hosts (one is PARKED) and one is shared. The fold test asks three
things: **A** same actor? **M** same subsystem mechanic? **P** a difference of parameter or content
only? A fold is legitimate only if all three are yes.

### S1 — The journey · host `travel` (the shipped `move`, renamed)

**Folded acts.**

| act | A | M | P | line |
|---|---|---|---|---|
| `navigate` (choose the route; lead off-road) | yes | yes | yes | It is the same traveller on the same `_relocate`. Only the route changes (road, off-road, water) and who leads it. The route's price and risk are M-WT-1 and M-WT-3. |
| `ride` (travel mounted) | yes | yes | yes | It is the same journey. A mount lowers the leg price per edge (M-WT-1), and kit comes from J-T5. No act is needed beyond choosing to take the horse. |
| `sail` (travel by water) | yes | yes | yes | It is the same journey over `coastal`/`sea` edges (GEO :552, :644) and the navigable river (:814-819). It is refused in the storm season (M-WT-2) and exposed to weather (M-WT-4). |

An army sailing is `march` over the same water edges (MB). Cargo by water is EC's `transfer` priced by
distance (`haul`, EC-G37). Neither is folded here.

**World effect.** It writes `Person.travel_leg`, `Tenure.until`/`since` (`contain`) and emits
`travel.moved`, `travel.blocked` and `travel.ended` (VT:753-755; `matter.py:577-580`). **It lacks:** a
route and its price (M-WT-1), so any place under the realm is one leg away; a refusal by season (M-WT-2);
a risk off-road (M-WT-3); and exposure (M-WT-4). There are two defects in the row:
- A journey to the place the traveller already stands is executed, not caught (H-140). The leg grows and
  a Tenure churns.
- The name `move` is the ordinary word for moving house, which is `migrate`'s act (§3.4).

**NERS.**
- **N HOLDS, all six directions.** Presence is the epistemic gate (VCD:1163; witnesses are whoever stands
  there).
  - Bottom-up: where a person is decides what he witnesses.
  - Top-down: a seat's agents must be placed.
  - Vertical: `march` and `migrate` compose on this body.
  - Lateral: meeting a person is how SC and FI acts become eligible.
  - Diagonal: travelling to a Calamity territory meets TW's hazard (once M-WT-4 exists).
  - Horizontal: `move` and `migrate` share one body.
  - Cut it and no person can change where he is. No false N-line: nothing else re-homes one's own
    `contain`. `march` moves others through a seat (VT:687).
- **R, narrowed.** Choosing where to be is strategic, but the choice is flat: every destination costs one
  leg (`budget.py:60`). Completeness fails at the extremes: a journey across the realm costs what a walk
  across town does. R-WORLD: arrivals throw hooks (witnessing), and distance adds none.
- **S, mixed.** It passes calculations-consistent: one body serves three verbs, and the leg is priced in
  the one budget. It fails S-ladder: GEO has two movement models (edges at :594, pixels at :800), and the
  engine reads neither (WT-G07). It fails "pauses correctly": nothing makes a journey take longer than a
  season.
- **E (ratio).** It is simple and has no overhead. But "intuit complex outcomes" fails, because distance
  is invisible. E rises once the edge count is the price. That needs no new verb, only a Query.

**Precedent.** F1–F4 in §3.2.

**Gaps closed.** WT-G01, -G03, -G06, -G07, -G08, -G10, -G11, -G12, -G13, -G20, -G21, -G28, -G29 (half),
-G37 (each once its mechanic exists; §3.6). **Left open:** WT-G02 is disputed (§3.6).

**Disposition. REBUILD** (the row stands):
1. **Rename `move` → `travel`.** The events are already `travel.moved`/`.blocked`/`.ended`, and so is the
   carrier `travel_leg`. The rename aligns the verb with its own emissions.
2. **Do not form or execute a journey that changes no presence.** This answers H-140 by precedent:
   `_eff_migrate` declines "a migration that changes no residence" (VT:739, H-168), `_eff_transfer`
   refuses a self-transfer, and IN-45 stopped `migrate` forming on a place "he already lives under"
   (VT:725).
3. **Price the leg by route (M-WT-1).**

*Falsifier:* if a usage check shows ordinary English "move to X" more often means a visit than a change
of home, the rename's reason fails. `[CONFIDENCE: medium — no corpus count run]`

### S2 — Resettlement · host `migrate`; second row `evacuate`

**Folded acts.**

| act | A | M | P | line |
|---|---|---|---|---|
| emigrate / flee dearth | yes | yes | yes | Same row. The motive is the destination channel's content (`places_named`, VT:725), not a new act. |
| settle a founded hearth | yes | yes | yes | Same row. The destination is a newly founded Rung with room. Founding it is `found`/`build` (GV/EC). |
| `evacuate` (a seat moves a population out ahead of a shock) | **no** | yes | no | The actor is the seat, through a remit, moving others. This is `march`'s relation to `move` (VCD:449: "an army (`march`, through a seat)"). **Fold fails, so it is its own row.** |

**World effect.**
- `migrate` writes `Person.travel_leg` and `Tenure.until`/`since` on both `contain` and `reside`, and
  emits `residence.changed`. It has keyed refusals: `path` → `travel.blocked`, `write` → `migrate.refused`
  (VT:733-739).
- It **lacks** movement of a cohort's people. Only a whole Person migrates. A cohort's `weight` (the
  population, H-170) never moves, so famine cannot empty a town (M-WT-6).
- `evacuate` would write the same edges for the evacuated weight (M-WT-6) and emit `evacuation.ordered`.
  It needs a warning to act on. Under T-WR-2 (`WR_world.md:270`, "a threshold may change options, never
  act"), that warning is a band-crossing Event, which already exists (WT-G23).

**NERS — `migrate`.**
- **N HOLDS.** RR-2 ruled it "a verb persons take" (VT:713-717), and it is the only act that re-homes `reside`.
  - Bottom-up: dearth moves people (`WR_world.md:53`, *cura annonae*, 1315).
  - Top-down: a seat's capacity (`build`) draws settlers.
  - Lateral: a migrant arrives as a stranger, so reception is priced (VCD:860).
  - Vertical: population feeds yield and levy pools (TSD).
  - Diagonal: emptying a town feeds GV legitimacy.
  - Horizontal: it shares `travel`'s body.
  - False-N check: could `travel` + a `reside` parameter carry it? That was v2's first pass (`_part4.md:335`).
    It is answered: the row's alignment cells differ (`_part4.md:338-340`), and RR-2's ruling names the
    verb. It is not false.
- **R.** Exit is the R-WORLD hook with no player in it: people leave neglected places. The R gap is
  cohort scale (M-WT-6).
- **S.** It is consistent: one body, and the capacity throttle reads the same `population` Query
  (WQ:1049, :1097).
- **E.** High. It is one extra Tenure pair and one throttle.

**NERS — `evacuate`.** It is beyond the floor.
- **N narrowed:** it holds only lateral and top-down. A seat saves a population from a telegraphed
  shock (HCC §2.4, Val di Noto; WR T-WR-1, "every fix has a fuse").
- **R:** it is a strong seat choice (abandon the town, or hold).
- **S:** it composes on `_relocate` and M-WT-6.
- **E:** fair.
- Today it is a false N-line by disqualifier 5 (no producer). Nothing moves a cohort and no shock
  telegraphs to a seat. So it is PARKED, not built.

**Precedent.** F5; HCC §2.4 :77-89; PGS F13 :132 (Relocate Capital: this is GV's, §3.8).

**Gaps closed.** WT-G03, -G04 (once M-WT-6); WT-G43 is parked.

**Disposition.**
- `migrate`: **KEEP-AS-IS.** *Falsifier:* a ruling that withdraws RR-2's "verb persons take".
- `evacuate`: **PARK.** Trigger: M-WT-6 exists *and* a hazard band-crossing reaches a seat as an Event
  it can read. Revival form: a seat row, eligibility `remit:dispatch`, writing M-WT-6's weight transfer.

### S3 — Living off the land · host `forage` (NEW ROW, force scale)

**Fold tests against the candidate hosts v2 used.**

| into | A | M | P | line |
|---|---|---|---|---|
| `requisition` (VT:646) | no | no | no | `requisition` is a seat officer under `remit:issue` with a purview basis, moving a Rung's stores **into the seat's treasury** (VT:648-652). Forage is a commander, by presence, meeting **a standing force's draw** from the land around it. The destination, the basis and the mechanic all differ. **Fails.** (VT:650 also lists `presence:<rung>` in `requisition`'s eligibility, but its `requires_typed` still demands the `purview` basis (VT:656-660), so an occupier without purview is refused.) |
| `seize` (VT:898) | no | no | no | `seize` moves title (`Tenure.until`/`since`) and "never takes a seat". It moves no stores (`_part8.md:354-356`, checked against VT:898-912). **Fails.** |
| `march` (VT:683) | yes | no | no | `march` contests a field and arrives. Forage writes stores while standing still. **Fails.** |
| hunt (game rather than grain) | yes | yes | **no carrier** | `Rung.stores` does not tell wild food from farmed. With no carrier for the difference, "hunt" as content would change nothing. Not folded; see the culls. |

**The act.** Under the troop-stock design a raised stock "eats from the larder where it stands, after
every person there" (TSD :56-58, :79-80; a draft). Feeding a force is therefore **automatic** (M-WT-8),
and a verb that only fed it would be a false N-line: the automatic draw already does it. What `forage`
adds is the **choice**: the force eats **before** the residents and reaches **one route edge out**
(PW §1.3a :35, "~10 miles"). The cost is the land's stores and the residents' disposition. This is the
Total War raiding stance [MEMORY], and it is the historical chevauchée (MB lane, `MB_mass_battle.md:288`).

**World effect (proposed).**
- Eligibility: `presence:<rung>`, one of VT's four kinds (VT:33). This answers v2's blocking condition
  "one basis rule (the grammar has no `any`)" (`_part8.md:411`): presence needs no purview disjunction.
- Writes: `Rung.stores` of the standing rung and its route neighbours, debited ahead of residents in
  `subsistence_draw`'s order (WQ:804-829). The forager's troop stock is then fed.
- Emits `forage.taken`. Its witnesses are the residents' cohort, which gives the grudge `march` already
  writes (VCD:1161) a second producer.
- **Lacks:** M-WT-8 (a force that eats away from home), and the troop stock itself (TSD J-1, escalated
  there).

**NERS.**
- **N HOLDS, NARROWED** to the choice between restraint and stripping the land.
  - Top-down: a seat's war costs its own and enemy towns.
  - Bottom-up: a cohort's hunger has a named cause.
  - Lateral: the grudge feeds SC/FA.
  - Diagonal: a devastated rung "cannot be supplied" (PW :43), so stripping is self-limiting.
  - Vertical: troop stock ↔ settlement stores.
  - Horizontal: it sits beside `requisition` as the force-side taking.
  - Without it, war costs only battles (PW :39, "conquest is 'too cheap'").
- **R.** It is strategic (feed now, lose the land later). R-WORLD: famine follows armies with no player
  involved.
- **S.** It reuses the one larder walk and one draw order. It adds no second ladder. It pauses correctly
  only once M-WT-2 gives winter.
- **E (ratio).** One row with one parameter (draw order and reach) buys a whole logistics trade-off.
  That is good.

**Precedent.** F6 (§3.2); PW §1.3a; HCC §2.3 :66 (Magdeburg, contributions; EC-G34).

**Gaps closed.** WT-G15, -G16, -G17 (once M-WT-8).

**Disposition. NEW ROW**, owner WT (it answers M-WT-8). The actor is MB's commander (§3.8).
*Falsifier:* if TSD's automatic draw is ruled to put the force first already, `forage`'s parameter
vanishes and it should be CULLED.

### S4 — Halting and shelter · host `camp` (PARKED)

**Folded acts.**

| act | A | M | P | line |
|---|---|---|---|---|
| `encamp` / winter quarters (a force halts) | yes | yes | yes | The same person halts with the company he leads. It writes the same sheltered posture. Company size is a parameter. Unlike `march`, it moves nobody, so it needs no `remit:dispatch`. |
| rest / recover | no | no | — | This is `tend` of oneself, NP's B10 row (`_part8.md:538`). It is not folded; see §3.8. |

**World effect.** It would write a sheltered posture for the season that M-WT-8's attrition term and
M-WT-4's exposure read. It emits `camp.made`. **It lacks** both readers, and above all **a place between
settlements**. Every person and force always stands at a Rung, and a leg ends at the next MATTER
(`matter.py:540-580`). So "in the open" does not exist yet, and halting is presence, as v2 said
(`_part8.md:409`).

**NERS.**
- **N.** False today, by disqualifier 5 (no producer: nothing makes the open season cost anything). Once
  M-WT-2, M-WT-3 (multi-season journeys) and M-WT-8 exist, it holds top-down (winter quarters as a
  campaign decision, PW :36) and bottom-up (a party that halts loses the season and spares the body).
- **R.** It is the classic tempo choice: press on or winter.
- **S.** It would read the same clock and attrition term as `forage`.
- **E.** One row.

**Precedent.** F8.

**Gaps.** WT-G19 and -G35 are parked.

**Disposition. PARK.** It is a floor act, so it keeps its name. Trigger: a journey can span a MATTER on a
route edge (M-WT-3) *and* the open season has a cost (M-WT-2 + M-WT-8). Revival form: own row,
eligibility `own`, writing the posture read by M-WT-8. *Falsifier for the park:* a shipped reader of
"sheltered" that exists today. None does: `grep -rni shelter engine/season --include=*.py` outside the
tests gives 0 hits (run).

### S5 — Discovery · host `explore` (NEW ROW)

**Folded acts.**

| act | A | M | P | line |
|---|---|---|---|---|
| scout the land (find a site of interest) | yes | yes | yes | Same act. The POI category found (resource, secret, remnant, anomaly; GEO :893) is content. |
| reconnoitre a settlement or force | no | no | — | This is FI's watching of a known place (`surveil`/`reconnoitre`, `_part8.md:579`). Not folded; see §3.8. |
| `track` a quarry | no | no | — | This is FI's `reconstruct` (`_part8.md:579`). Not folded. |

**World effect (proposed).** Eligibility `presence:<rung>` at the territory explored. It resolves through
XSC §6.4's Discovery Procedure (Ob per depth, on the one dice engine). On success it reveals one of the
territory's authored POIs (M-WT-5): a Site, or for a "secret" a Record, becomes known to the explorer,
deposited as a belief. It emits `site.discovered`. Its readers are already the owners of what is found:
- a resource → Site yield (EC);
- a remnant or anomaly → TW;
- a secret → FI.

**It lacks** M-WT-5. `poi_catalog` holds counts, not entities, and nothing reads it.

**NERS.**
- **N HOLDS, NARROWED** (until M-WT-5 it has no producer).
  - Bottom-up: a person finds what a faction lacks.
  - Top-down: a seat sends explorers for resources.
  - Diagonal: anomalies lead to Calamity and threadwork.
  - Lateral: secrets lead to FI.
  - Vertical: a POI raises Prosperity (XSC :669).
  - Horizontal: it is the one act that makes the map grow.
  - False-N check against FI's `survey`: it fails as a host. `survey` now means a faction sheet
    (EC-G48; VT:966), and it does not take a territory by presence.
- **R.** It throws world hooks, including R-WORLD ones (a rival finds the remnant first).
- **S.** It uses one engine (XSC's pool) and one carrier (Site).
- **E.** Good, provided POIs are authored at world-gen, not minted by a clock (T-WR-2, ED-WR-0011
  option A's shape).

**Precedent.** F10.

**Gaps closed.** WT-G29, -G30 (once M-WT-5).

**Disposition. NEW ROW**, owner WT. FI may claim the procedure (§3.8). *Falsifier:* if the Godot design
fixes POIs as visible from the start (no fog), discovery has nothing to reveal and the row should be
CULLED.

### Culled at the season scale (no suite)

| verb | why it is not a WT verb | what carries the floor act |
|---|---|---|
| `endure` | No one chooses to endure, so there is no chooser and no act. It is a resistance step inside a hazard. Criterion 6: it is an outcome. | XSC's "Endurance check" is a step of M-WT-4. The battle sense goes to MB's `withstand` (`_part8.md:522`). |
| `climb` | It is scene scale (escalade, cliffs). At season scale a mountain is impassable (GEO :768, cost 999) and a pass costs 2.0 (:767). | Route cost (M-WT-1); escalade goes to MB `storm`/PC. |
| `swim` | It is scene scale. A river at season scale is an edge cost (GEO :769-770, `river_crossing_*`). | Route cost (M-WT-1); the PC scene. |
| `hunt` | A person's own food is ruled out (ED-IN-0255). Wild food is a Site's yield (EC). The hunt as pastime is a social occasion (NP/SC). A force's hunting is foraging, with no carrier to tell game apart. | `forage` (force); EC Site yield; NP. |

---

## 3.4 Lexicon table

**Sources.**
- Wikt = en.wiktionary, read through `etym_tool.py en|la`.
- L&S = Lewis & Short, read through `etym_tool.py ls`.
- A link I could not check is tagged `[UNVERIFIED]`.

**Fit** is judged by ordinary current usage (ED-IN-0179). No design claim in §3.3 rests on a root sense.

| verb | suite | status | mechanic and world effect (carrier) | etymology chain with sources | fit | rename |
|---|---|---|---|---|---|---|
| `travel` | S1 host | NEW NAME for SHIPPED `move` | `_relocate`: closes and opens a `contain` Tenure, appends to `Person.travel_leg`, emits `travel.moved`/`.blocked`/`.ended` (VT:753-755; `matter.py:577`). Leg priced in `budget.py:60`; by route once M-WT-1 exists | travel ← ME *travelen*, an alteration of *travaillen* 'to toil' (Wikt) ← OF *travailler* 'torment, toil' (the noun *travail* is deverbal from it; Wikt OF) ← VL \**tripāliāre* 'to torment' (Wikt OF) ← LL *tripālium* 'a torture instrument of three stakes' (Wikt la: "tentative"; from *tripālis* 'of three stakes') ← *trēs* + *pālus* 'stake' ← PIE \**tréyes* 'three' and \**peh₂ǵ-* 'fasten' (Wikt's PIE templates on *travel*). The sense moved from 'toil' to 'journey' in ME (Wikt's note; it gives no century). Not a Latin verb: Latin supplies only the noun *tripālium*, from which the Vulgar Latin verb was derived | FITS: 'go on a journey'. It does not imply a change of home, which is exactly the row | (this *is* the rename) |
| `move` | S1 | SHIPPED, rename proposed | as `travel` | move ← ME *moven*/*meven* ← AN *mover*, OF *moveir* ← L *moveō, movēre, mōvī, mōtum* 'to move, stir, set in motion; to shake, disturb, remove' (L&S) ← PIE \**m(y)ewh₁-* (Wikt) | STRAINED: "move to X" commonly means moving house, which is `migrate`'s act. VCD:346 said FITS without the pair test | `travel` |
| `migrate` | S2 host | SHIPPED | `_relocate` plus `reside` re-homed, throttled by `WQ.capacity`. Emits `residence.changed`; refusals `travel.blocked`/`migrate.refused` (VT:733-739) | migrate (1623, Wikt) ← L *migrātus*, perfect passive participle of *migrō, migrāre, migrāvī, migrātum* 'to remove from one place to another, to depart, flit, migrate' (L&S, "etym. dub."); Wikt la: 'depart to another place, change residence' ← PItal \**migros* ← PIE \**h₂migʷrós* ← \**h₂meygʷ-* 'change' (Wikt). L&S (1879): etym. dub.; Wikt gives \*h₂meygʷ- without hedge | FITS: Wikt sense 2 "to change one's geographic pattern of habitation"; current use covers persons resettling | — |
| `navigate` | S1 | FOLDED (route parameter of `travel`) | route choice and leader on the journey roll (M-WT-1, M-WT-3); a lost journey deposits `contain.path:<to>` False (VT:732) | navigate (1588, Wikt) ← L *nāvigātus*, participle of *nāvigō, nāvigāre, nāvigāvī, nāvigātum* 'to sail, set sail; to go by sea' (L&S) ← *nāvis* 'ship' (← PIE \**néh₂us*, Wikt) + *-igō* ← *agō* 'drive' (PIE \**h₂eǵ-*, Wikt's root template). Latin sense: 'sail'. Current sense: 'plan and direct a course; find one's way' (Wikt); the shift date is not stated | FITS: 'find one's way' is the ordinary current sense, by land too | — |
| `ride` | S1 | FOLDED (mount parameter of `travel`) | lower leg cost per edge (M-WT-1) given kit (J-T5) | **Germanic, no Latin path.** ride ← ME *riden* ← OE *rīdan* ← PWGmc \**rīdan* ← PGmc \**rīdaną* ← PIE \**Hreydʰ-* (Wikt). Wikt names no Latin cognate | FITS | — |
| `sail` | S1 | FOLDED (water path of `travel`) | travel over `coastal`/`sea`/river edges; refused in the storm season (M-WT-2) | **Germanic, no Latin path.** sail (v.) ← ME *sailen*/*seilen* ← OE *seġlan* ← PWGmc \**siglijan* ← PGmc \**siglijaną*, from \**seglą* 'sail' (Wikt). **No secure PIE root** (Wikt gives none) | FITS | — |
| `forage` | S3 host | NEW | presence-eligible draw on the standing rung's and its route neighbours' `Rung.stores`, ahead of residents, to feed the forager's troop stock; emits `forage.taken` (needs M-WT-8) | **Frankish, no Latin path.** forage ← ME *forage* 'fodder' ← OF *fourage*/*forage*, derived from *fuerre* 'fodder' ← Frankish \**fōdar* ← PGmc \**fōdrą* ← PIE \**peh₂-* (Wikt). Wikt says it is unrelated to modern French *forage* 'drilling'. The verb comes from the noun via OF *fourrager* `[UNVERIFIED]`. L *pāscō* 'feed' is a cognate through \**peh₂-* 'protect, shepherd' (Wikt la; cognate, not ancestor) | FITS: "(of an army) collect provisions from the countryside" is ordinary, if dated | — |
| `camp` | S4 host | PARKED (floor act) | a sheltered posture for the season, read by M-WT-8/M-WT-4; emits `camp.made` | camp (n.) ← ME *kampe* ← OE *camp* (via PWGmc \**kamp*) ← L *campus* 'open level land, a plain, a field' (L&S) ← PIE \**kh₂em-* 'bend' (Wikt: "traditionally"; alternatively a substrate word, so **disputed**). It was reinforced c. 1520 by MF *camp* from the same Latin (Wikt). The verb's source is **disputed**: Wikt en derives it from ME *campen*, OE *campian*, *compian* (one block covering 'live in a tent' and, obsolete, 'fight'; cf. G. *kämpfen*); the link to MF *camper* is `[UNVERIFIED]` | FITS: 'stay in a camp; lodge temporarily in the open' | — |
| `encamp` | S4 | FOLDED into `camp` (company size) | as `camp`, with the commander's company | encamp ← *en-* + *camp* (Wikt) | FITS: ordinary for an army settling in a camp | — |
| `explore` | S5 host | NEW | presence in a territory → XSC §6.4 Discovery → reveals an authored POI (Site/Record) to the explorer; emits `site.discovered` (needs M-WT-5) | explore ← MF *explorer* ← L *explōrō, explōrāre, explōrāvī, explōrātum* 'to search out, seek to discover, examine, investigate, explore' (L&S); also 'to spy out, reconnoitre' (Wikt la) ← *ex-* + *plōrō* 'cry out' (Wikt: "said to be originally a hunters' term"; alternatively from *pluō*). **No secure PIE root** (the second element is disputed) | FITS: 'travel through an unfamiliar area to learn about it' | — |
| `evacuate` | S2 | PARKED | seat-ordered `_relocate` of cohort weight (M-WT-6); emits `evacuation.ordered` | evacuate (1526, Wikt) ← L *ēvacuātus*, participle of *ēvacuō, ēvacuāre, —, ēvacuātum* 'to empty out' (L&S: post-Augustan, no perfect) ← *ex-* + *vacuō* 'empty out' ← *vacuus* (Wikt) ← PIE \**h₁weh₂-* (Wikt's root template). Latin sense: 'empty'. English 'remove people from danger' is a later sense; the source gives no date | FITS: 'remove people from a dangerous place' | — |
| `endure` | — | CULLED (an outcome, not an act) | none: XSC's Endurance check is a step of M-WT-4 | endure ← ME *enduren* ← OF *endurer* ← L *indūrō, indūrāre, indūrāvī, indūrātum* 'to make hard, harden'; figuratively 'to harden, steel' (L&S: "poet. and post-Aug.") ← *in-* + *dūrō* 'harden; (intr.) last, endure' (Wikt la) ← *dūrus* 'hard' ← PIE \**dweh₂rós* 'long' or \**drew-* (Wikt gives both: **disputed**). The 'last, bear' sense is *dūrō*'s, not *indūrō*'s | FITS as a word; it fails as a verb because no one chooses it | — |
| `climb` | — | CULLED (scene scale) | none at season scale | **Germanic, no Latin path.** climb ← ME *climben* ← OE *climban* ← PWGmc \**klimban* ← PGmc \**klimbaną*, a nasalised variant of \**klibaną* ← PIE \**gley-* (Wikt) | FITS | — |
| `swim` | — | CULLED (scene scale) | none at season scale | **Germanic, no Latin path.** swim ← ME *swymmen* ← OE *swimman* ← PWGmc \**swimman* ← PGmc \**swimmaną* ← PIE \**swem(bʰ)-* (Wikt) | FITS | — |
| `hunt` | — | CULLED from WT (§3.8: NP, EC) | none in WT | **Germanic, no Latin path.** hunt ← ME *hunten* ← OE *huntian* ← PWGmc \**huntōn*, "possibly" ← PIE \**ḱent-* (Wikt; **no secure PIE root**). Related to OE *hentan* 'seize' (Wikt) | FITS | — |

---

## 3.5 Deduplication and culls

### Near-synonym groups and the discriminator kept

Each group is separated by the row's reads and writes, then checked against ordinary usage.

| group | discriminator | result |
|---|---|---|
| `move` / `migrate` / `march` | `move` re-homes one's own `contain`; `migrate` also `reside`, throttled (VT:733-739); `march` moves others through `remit:dispatch` and contests a field (VT:687, :695) | All three stay. **Rename `move` → `travel`.** Reason: "move" and "migrate" are near-synonyms in ordinary English ("we moved to the capital" = resettled), while "travel" and "migrate" are not (a visit against a new home). The rename also matches the row's own emissions (`travel.*`). |
| `navigate` / `explore` / reconnoitre / `track` | The object: one's own route (`navigate`); an unknown site in a territory (`explore`); a known place watched (FI `surveil`/reconnoitre); a person's whereabouts (FI `reconstruct`) | `navigate` is FOLDED into `travel`. `explore` is a NEW ROW. The other two are FI's (§3.8). |
| `forage` / `requisition` / `seize` / sack / provision | Who takes, by what basis, and to where: `forage` = a force present, before the residents, into its own draw; `requisition` = seat purview → treasury (VT:646-652); `seize` = title, no stores (VT:898-912); sack = MB's taking after a storm; provision = a seat's `transfer` to its force (EC) | `forage` is a NEW ROW. v2's MERGE → `requisition` (`_part8.md:411`) is **rejected**: the fold test fails on actor, mechanic and parameter (§3.3 S3). |
| `camp` / `encamp` / rest (`tend`) | `camp`/`encamp` = the same posture for a party or a force; rest = recovery of the body, NP's `tend` | `encamp` is FOLDED into `camp`. Rest is NP's. |
| `endure` / `withstand` | `withstand` is MB's chosen battle response; `endure` on the road has no chooser | `endure` is CULLED (season sense); the battle sense goes to MB. |
| `evacuate` / `migrate` / relocate | Actor: a seat moving others (`evacuate`); oneself (`migrate`); a seat moving its own seat (relocate capital, GV) | Kept apart. `evacuate` is PARKED; relocate goes to GV. |
| `ride` / `sail` / `swim` / ford | Mode of one journey, over a road, water or river edge | `ride` and `sail` are FOLDED. `swim` is CULLED. Ford is not named: it is the river edge's cost. |

### Culls — fold test and floor check

| culled | fold test | floor check: nothing a floor act needs dies because… | falsifier |
|---|---|---|---|
| `endure` | Not an act. No chooser exists, so A, M and P are all void (criterion 6: an outcome). | F9's hazard is carried by M-WT-4, whose resistance step *is* XSC's Endurance check (:664-665). No precedent game in F9 makes enduring a chosen verb: Oregon Trail and Frostpunk impose weather [MEMORY]. | A design in which a traveller can *choose* to push through a hazard for a gain. That would be a `travel` parameter, still not a row. |
| `climb` | A yes, M no (scene scale), P no | At season scale, mountains and passes are route costs (GEO :767-768). F2 and F4 are carried by M-WT-1. Escalade is MB `storm`/PC. | A season-scale route edge that is passable only by a climbing roll. That would make it a M-WT-3 parameter. |
| `swim` | A yes, M no, P no | F4 is carried by river edges (GEO :769-770) and `sail`. | As `climb`. |
| `hunt` (from WT) | A yes, M yes, P **has no carrier** (`Rung.stores` does not tell wild from farmed) | F7 is excluded by ruling (ED-IN-0255, WQ:816-820). F6 is carried by `forage`. Food from the wild at settlement scale is EC's Site yield. The hunt as an occasion is NP's. | A ruling that named persons eat. That would reopen F7 and make `forage`/`hunt` own-eligible. |

**v2 dispositions reversed or re-reasoned.**
- `navigate` and `ride` were CUT with "no route graph exists" and "speed changes nothing a reader sees"
  (`_part8.md:516-517`). The route graph **exists as data**: GEO :594 has 56 edges per its own comment
  (:602), plus territory adjacency at :548. What is missing is a **reader**. By criterion 6 that is a
  named gap (M-WT-1), not a reason to hide the act. Both become FOLDED modes of `travel`, gated on
  M-WT-1.
- `encamp` was CUT ("halting is presence", `_part8.md:409`). It is correct today, but camping is a floor
  act, so it is PARKED with a trigger rather than cut.
- `hunt` was CUT on W8. W8 is real: `yield` at MATTER is the one minter of matter (`architecture/PLAN.md:1045-1049`).
  The decisive reason, though, is ED-IN-0255.

### Critic findings that concern WT verbs

| finding | verdict | reason |
|---|---|---|
| L-01 (root sense used as design intent) | **applied** | No WT disposition rests on a root sense. Two examples: `navigate`'s Latin 'sail' is not used to confine it to water, and `forage`'s 'fodder' is not used to make it a horse ration. |
| L-12 ("`march` moves nobody" is stale) | **applied** | `march` now arrives through `_relocate` (VT:701). §3.1 and S3 rely on the current row. |
| L "Upheld": `move`, `migrate` FITS | **answered, partly rejected** | Each etymology holds (checked: L&S *moveō*, *migrō*). Each word fits alone. As a **pair**, `move` fails the ordinary-use test, because "move" covers resettling. The rename is to `travel`. |
| V-02 (endure classed "reversed") | **applied** | In substance, the season sense is cut, as at the first pass. Only the battle sense moved (to MB). WT records `endure` as CULLED. |
| V-12 / V-13 ("march (tread)" → "ration", `_part5.md:254`, :258) | **applied** | No WT node is derived from *march*'s root, which is disputed (Frankish \**markōn* against LL; VCD:4188 hedged it). Ration is GV's (§3.8). |
| V-18 (hunt→work among the "reversed") | **applied** | `hunt` does not go into `work`. `work` writes only `Site.condition` (VT:1278; L-06 shows the row holds two senses already). |

---

## 3.6 Gap coverage table

Every WT row of the register appears once, with exactly one disposition. "Once M-WT-n" means that
mechanic in §3.7 must exist first.

| gap id | closed by | PARKED (trigger) | OUT OF SCOPE (why) | STALE (cite tree) | DISPUTED (why) |
|---|---|---|---|---|---|
| WT-G01 | `travel` (REBUILD: form no journey to where one stands; precedent VT:725, :739) | | | | |
| WT-G02 | | | | | The rows are consistent. `move` has one clause, so its flat `travel.blocked` (VT:755) is keyed in effect. `migrate` keys two clauses, and its `path` emits the same `travel.blocked` (VT:736-739). The residue, whether a refusal travels as news, is IN's H-111. |
| WT-G03 | `travel` + `migrate` (both kept; RR-2 ruled `migrate` "a verb persons take", VT:713-717) | | | | |
| WT-G04 | `migrate` once M-WT-6. The destination half has landed: IN-45's `places_named` channel (VT:725; WQ:1773) | | | | |
| WT-G05 | | | Births are NP's. Capacity is GV's lever (`build`). WT's half, cohort weight moving, is WT-G04/M-WT-6 | | |
| WT-G06 | `travel` once M-WT-1 | | | | |
| WT-G07 | `travel` once M-WT-1, which keeps **one** unit, the edge. The pixel `march_budget` (GEO :800-804) is retired or derived from it, so there is no second ladder (S) | | | | |
| WT-G08 | `travel` (with `ride` as a mode) once M-WT-1 | | | | |
| WT-G09 | | | | Leg lifetime is ruled in code: the next MATTER ends it and emits `travel.ended` (`loop/matter.py:540-580`). Ownership defaults to the subject (H-27, graded `assumption`). The clock half is WT-G37 | |
| WT-G10 | `navigate` (folded into `travel`) once M-WT-1 and M-WT-3 | | | | |
| WT-G11 | `ride` (folded) once M-WT-1, plus kit (J-T5, v2 head) | | | | |
| WT-G12 | `sail` (folded) once M-WT-1 (water edges) and M-WT-2 | | | | |
| WT-G13 | `travel` once M-WT-1 (river and mountain edge costs, GEO :767-770). `climb` and `swim` are culled to scene scale | | | | |
| WT-G14 | | | ED-IN-0255 (persons do not eat). Wild food is EC's Site yield; the hunt as an occasion is NP's | | |
| WT-G15 | `forage` (NEW) once M-WT-8 | | | | |
| WT-G16 | `forage` once M-WT-8. M-WT-8 is H-212's named MATTER reader. The besieged-town half needs M-WT-7 | | | | |
| WT-G17 | `forage` once M-WT-8 (and M-WT-1 for terrain). TSD withdraws LF-1..LF-3 as forms (TSD :138-139) | | | | |
| WT-G18 | | | `ration` is GV's (v2 PARK, `_part8.md:482`). It is a draw policy, not travel | | |
| WT-G19 | | `camp` (with `encamp` folded). Trigger: M-WT-3 multi-season legs + M-WT-2 + M-WT-8 | | | |
| WT-G20 | `travel` (sail mode) once M-WT-2 and M-WT-4. "Withdrawal" is not sailing; the hazard window prices it, so no verb is needed | | | | |
| WT-G21 | `travel` once M-WT-4, which makes the season's weather draw (WQ:747-769) its second reader | | | | |
| WT-G22 | | | The wear-loop coupling (IN-35, FORCE-HAZARD) is TW/EC's (`mend`/`restore`). WT's own hazard is WT-G29 | | |
| WT-G23 | | | It is a ruled refusal: hazard-rate thresholds before a collective act are refused (AX-5, T-c; T-WR-2 at `WR_world.md:270`). The band-crossing Event is the warning, and `evacuate` (PARKED) reads it | | |
| WT-G24 | | | `body_step` is a fixture (H-125, FX:567). `endure` is not an act (§3.5) | | |
| WT-G25 | | | Ruled: ED-IN-0255 (WQ:816-829) | | |
| WT-G26 | | | Ageing and illness are NP's (H-208; FX:579-581) | | |
| WT-G27 | | | It is GV's, and the register records it as ruled "a balance number, not a blocker" | | |
| WT-G28 | `travel` once M-WT-4. The Endurance check is M-WT-4's resistance step; `endure` is culled | | | | |
| WT-G29 | `explore` + `travel` once M-WT-4 and M-WT-5 | | | | |
| WT-G30 | `explore` once M-WT-5 | | | | |
| WT-G31 | | Trigger: news latency that reads distance (the road's only payoff, which PGS concedes), and M-WT-1. The act of record is EC/GV `build` of a route edge | | | |
| WT-G32 | | Trigger: M-WT-7. Redundancy is a property of the route graph, and its lever is `build` of a second edge (EC/GV) | | | |
| WT-G33 | `march` (MB: occupation interdicts a route) once M-WT-7 | | | | |
| WT-G34 | | | It is PC's `fight` (`_part8.md:555`). A traveller can be waylaid only once M-WT-3 gives him a place on the road (§3.9 item 2). The row is single-source | | |
| WT-G35 | | `camp` (as WT-G19). Recovery is NP's `tend` | | | |
| WT-G36 | | | It is FI's (`reconstruct`, `_part8.md:579`) | | |
| WT-G37 | `travel` (and `sail`) once M-WT-2. Partly stale: `w.tick` and `season_of_year` exist (WQ:738-744); only the shipped year is missing | | | | |
| WT-G38 | | | It is a statement about evidence, not a verb. This lane substitutes game precedents tagged `[MEMORY]` (§3.2) | | |
| WT-G39 | | | It concerns an events system: T-WR-2 rules "generate on demand, never on a clock". WT verbs answer world motion; they do not generate it | | |
| WT-G40 | | Trigger: a contagion carrier (`illness_rate` > 0 spreading along M-WT-1's routes). Its form is then a GV `issue`d edict closing a route edge, read by `travel`'s refusal | | | |
| WT-G41 | | | HCC itself says the Cooling flag is "design-taste, author last". It would be a parameter of the weather draw, not a verb. Adopt Local Practice is a GV policy | | |
| WT-G42 | | | Founding a colony is GV/EC's `found`. WT's half, settlers arriving, is `migrate` | | |
| WT-G43 | | `evacuate`. Trigger: M-WT-6 + a hazard warning a seat can read. Relocating a capital is GV's | | | |

Tally: closed 20 · parked 6 · out of scope 15 · stale 1 · disputed 1 = **43**.

---

## 3.7 Mechanics this subsystem needs (named gaps)

Each one must pass the NERS meta-rule ("a fix that adds a system has failed"), so each says what
existing owner it extends.

| id | mechanic | what it writes / answers | extends | verbs waiting |
|---|---|---|---|---|
| M-WT-1 | **Route Query**: a path and its cost between two Rungs over `settlement_adjacency` (GEO :594) and `adjacency` (:548). Rungs map to geography ids by `harness/populated.py`'s `set_` + id rule. The cost is edges weighted by the `terrain_cost_matrix` of the territory entered (:760-771), with bridges at :821. **One unit (the edge)**; the pixel `march_budget` is retired or derived | Writes nothing (a Query). Answers `contain_path`'s "is there a road" as a route rather than a shared ancestor. Prices the leg in `budget.py:60` (legs × edge cost, not × 1) | `data/geography.py`'s existing one read; `budget.py`'s existing penalty | `travel`, `navigate`, `ride`, `sail`, `migrate`, `forage` (reach), `explore`; MB `march`; EC `haul` (EC-G37) |
| M-WT-2 | **Calendar**: a declared year length as a params row, read by `season_of_year`, **decoupled** from `season_factor_draw`. The shipped world then has seasons while the weather draw stays at its control | Writes nothing. Answers "which season is it" in the shipped world | `WQ.season_of_year` (:738-744): one fixture | `sail` (storm-season refusal), `camp`, `forage` (winter term), M-WT-4, MB `march` (campaign season) |
| M-WT-3 | **Journey roll** for an off-road, water or Calamity leg: an unopposed draw against an Ob set by route terrain (XSC §6.4 shape), on the one dice engine (`degree_from_net`). The bands are: arrive / delayed (the leg does not end at the next MATTER) / lost (`travel.blocked`, with `contain.path:<to>` False deposited) | `Person.travel_leg` (extra legs), `contain` arrival, a belief deposit | the `travel` row's resolution; `matter.py`'s leg-end pass | `navigate`, `ride`, `sail`, `camp` (needs delayed legs), PC `fight` (ambush) |
| M-WT-4 | **Exposure**: a leg through `radiation_bands`/`forgetting_zone` territory (GEO :835-873; canon PP-703, personnel-layer Forgetting), plus weather if §3.9 item 1 rules so. Its resistance step is the Endurance check | `Person.body` through the body pass's one writer (`matter.py:454`), or TW's Forgetting/coherence carrier | the body pass; the season weather draw (WQ:747) as its second reader | `travel`, `sail`, `explore`, `camp` |
| M-WT-5 | **POI carrier**: `poi_catalog`'s per-territory counts (GEO :893-913) become authored, hidden Sites (resource, remnant, anomaly) or Records (secret), minted at world-gen by `populated.py`, never by a clock | Site/Record existence; a belief deposit on discovery | the existing Site and Record carriers; world-gen | `explore`; read by EC yield, TW, FI |
| M-WT-6 | **Cohort weight migration**: part of a cohort's `weight` moves to another rung's cohort, checked against `capacity`. It moves people and mints none | `Person.weight` on two cohorts; `residence.changed` | `WQ.population`/`capacity` (:1049, :1097); `_relocate` | `migrate` (dearth push), `evacuate` |
| M-WT-7 | **Route dependency**: the larder walk (`nearest_store`, WQ:689) follows M-WT-1's routes and stops at a rung where an enemy force is mustered (the occupation Query, H-212) | Writes nothing new. A cut route makes the dependent draw fall short, through the existing shortfall | `nearest_store`; `WQ.mustered` (:1257) | MB `march` (blockade); WT-G32/G33 |
| M-WT-8 | **Campaign supply**: a troop stock eats where it stands (TSD :56-58, a draft), with a season term from M-WT-2 and a hostile-ground term from the occupation Query (PW §1.3a :41) | `Rung.stores` debited; the stock's strength (MB/TSD carrier) when unfed | `WQ.subsistence_draw` (:804) and its draw order; H-212's named owner | `forage`, `camp`/`encamp`, MB `march` |

---

## 3.8 Cross-subsystem flags

| other lane | verb | the collision or dependency |
|---|---|---|
| MB | `forage` | WT proposes owning the row, because it answers M-WT-8. Its actor is MB's commander and its eater is MB's troop stock (TSD, whose J-1 is escalated there). v2 merged it into `requisition`; WT rejects that merge (§3.3 S3). MB may claim the row. If so, the fold test and the presence eligibility still stand. |
| MB | `encamp` | WT folds it into `camp`, as the same posture with company size as a parameter. v2's alternative was "a third `march` posture" (`_part8.md:409`). WT objects: a halt moves nobody, so it is not a march. |
| MB | `march` | It should read M-WT-1 (route and price) in place of GEO's pixel `march_budget`, M-WT-2 (campaign season) and M-WT-7 (blockade). An army at sea is `march` over water edges. |
| MB | `withstand` | It receives `endure`'s battle sense (v2). WT holds no row for it. |
| EC | `requisition`, `haul`, provision, Contribution System | `requisition` stays the seat's purview taking into the treasury. `haul` (EC-G37) waits on M-WT-1. Provision is EC's `transfer` to a force. The Contribution System (EC-G34; HCC §2.3 :66) is the seat's organized version of foraging under occupation. That is `requisition` by an occupation basis, not `forage`. |
| EC | `hunt` as yield | A hunting-ground Site kind (`site_yield`) carries wild food at settlement scale. |
| FI | `explore` | XSC places Discovery under fieldwork, and the GEO comment says "Discovery via Survey action" (:892). `survey` is now a faction sheet (VT:966; EC-G48), so WT hosts `explore`. FI may claim the procedure. |
| FI | `track`, reconnoitre | Not WT's. Tracking is `reconstruct` (V134); reconnoitring is FI's watching of a known place. |
| NP | `tend`, `hunt` (occasion), bodies | Rest and recovery are `tend` of oneself (NP B10). The hunt as a social occasion is NP/SC's. Ageing and illness are H-208's. |
| GV | `evacuate`, relocate capital, `ration`, quarantine, `found` | `evacuate` is a seat's act, PARKED in WT because it resolves on `_relocate` and M-WT-6. GV owns the remit and may claim it. Relocating a capital is GV's re-seating. `ration` is GV's. Quarantine is a GV `issue` closing a route edge. A colony is `found` (GV/EC). |
| TW | M-WT-4 | Exposure in the Forgetting zone writes TW's Forgetting/coherence carrier. FORCE-HAZARD (WT-G22) is TW/EC's. |
| PC | `fight` (ambush), `climb`, `swim` | Waylaying a traveller needs M-WT-3's place on the road. Climbing and swimming are scene acts. |
| IN | rename `move` → `travel`; H-111 | The rename touches the VT row (:743), `@effect_for("move")` (`loop/effects_migration.py:24`), `rosters.yaml` and `requirements.yaml` (grep run on non-test `.py`/`.yaml`), plus the tests and goldens. A re-recorded golden must be said plainly (CLAUDE.md §7). Refusal-as-news (WT-G02) is H-111. |

---

## 3.9 For Jordan

Before escalating, I tried the five-step ladder on each candidate: superseded, irrelevant, answered by a
design document, answered by precedent, answered by architecture. Two survive.

1. **Does the road cost a named person anything but time?**
   - ED-IN-0255 settles subsistence ("a territorial issue"; named persons do not eat). It does not
     settle weather or hazard.
   - **(a)** Only Calamity territory (the Forgetting zone and radiation bands, canon PP-703, GEO :835)
     exposes a named traveller. Weather reaches cohorts and troop stocks only.
   - **(b)** Weather on the road also wears named travellers.
   - These lead to different games. Under (a), lords travel safely except into the Calamity. Under (b),
     a journey is a survival risk for characters, and `camp` gains a person-scale purpose.
   - The ladder does not settle it. XSC §6.4 names Calamity only. The reasoning of ED-IN-0255 leans
     (a). CK3's character travel dangers [MEMORY] lean (b).
   - Recommendation: (a).
2. **Can a person or force be *between* places?**
   - Today `contain` is Rung → Rung, and a leg ends at the next MATTER. Every journey completes in its
     season, and absence is one season's budget.
   - A journey that spans seasons on a route edge would have consequences:
     - a lord on the road is absent from his seat and from court;
     - he can be waylaid (WT-G34);
     - he must camp (WT-G19, -G35).
   - That is a different political game.
   - It needs a location that is not a Rung, which **amends ratified Layer 1** (`contain : Rung → Rung`,
     H-27's cite of #353 :539). It therefore cannot be answered by architecture.
   - Recommendation: keep (a), journeys complete in their season, until a playtest shows absence is
     wanted. `camp` and ambush stay PARKED under that answer.
