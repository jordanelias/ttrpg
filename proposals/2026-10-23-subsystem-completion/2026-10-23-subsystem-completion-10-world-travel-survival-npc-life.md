# World, travel, survival and NPC life — completion proposal (T10 · lane IN)
## Status: PROPOSED. Merging this file ratifies nothing (ED-1094's loud exception); every item and ask is held back for Jordan's adoption, item by item, as edits to the v9 parts it names.
## Lane: IN (cross-cutting). A proposal for edits to `workplans/valoria_master_workplan_v9*.md`, not a second plan (`CLAUDE.md` §2). **Home of v10 positions** since the v10 adoption (`ED-IN-0299`): this file holds the full spec of the v10 positions whose plan row names it (rows: `workplans/valoria_master_workplan_v10_part3.md` §1; handles: `workplans/valoria_master_workplan_v10_part12.md` §1; where `workplans/valoria_master_workplan_v10_part13.md` amends a home, the amendment governs), and is deleted with a `FORK:` row when its last position lands (v10 head §9 step 6).
## Grade under `CLAUDE.md` §0.2: `paper`. Nothing here executes. What it changes in `engine/season/`: nothing, until adopted.
## Written against: HEAD `2decf4a`. Inputs: `proposals/2026-10-22-system-description/…-11-t10-world-travel-survival-npc-life.md` (T10), `…-00-overview.md` §3, §5.2, §6 (OV); `research/game_precedent_suite/dispositions/D_T10.md` (D) and `D_T10_also.md` (DA); `research/game_precedent_suite/THROUGHLINES.md` (TL); `proposals/2026-10-16-verbs/…-17-lexicon-world-travel-and-survival.md` (L17), `…-18-lexicon-npc-life-and-persons.md` (L18), `…-19-gap-register-pc-and-np.md` (G19, NP half), `…-23-gap-register-ec-and-wt.md` (G23, WT half); `proposals/2026-10-21-v9-remediation/` parts 02–04 (REM2, REM3, REM4); `skills/ners/SKILL.md`; code opened where cited.

Abbreviations follow T10's: `es/` = `engine/season/`; `VT` = `es/verb_table.yaml`; `ROS` = `es/rosters.yaml`; `FX` = `es/data/fixtures.py`;
`WQ` = `es/queries/world_q.py`; `MAT` = `es/loop/matter.py`; `EM` = `es/loop/effects_migration.py`; `EC` = `es/loop/effects_combat.py`;
`GEO` = `systems/settlements/valoria_geography_v30.yaml`. `D:#n` is row n of `D_T10.md`, `DA:#n` row n of `D_T10_also.md`. Evidence grades
(RUNS-IN-LOOP, TESTS-ONLY, DESIGN-ONLY, "at control") are T10's and the dispositions', carried and never upgraded. Code lines are at HEAD
`2decf4a` where this file says "opened"; T10's line numbers are at `51d7b05` and are marked `T10:` when quoted.

**The fixed ground this file designs on.**
- **Births are set aside** (ED-WR-0011, Option A, RULED 2026-09-13: a closed authored cast of 46, no season-tick generation, "we will return
  much later"; DA:#2 DIFFERS, DA:#3). The ruling is **provisional** ("for now"), and the ruled row itself says a session may not "cite
  this row as settling world generation as a subject" (`registers/editorial_ledger_wr_archive.jsonl:14`); this file designs within it
  and treats it as a standing constraint, not a closure. Every item below works on a cast that can only shrink while it stands. That
  makes **every death expensive and every survivor's succession a live question**, which is the design lever this proposal pulls.
  (Validator note, once: `tools/validate_ed_citations.py::_is_resolved` (`:215-232`) does not accept the status `ruled`, so a basis
  keyword beside this id reads as OPEN_AS_BASIS; that is the validator's vocabulary, outside this file's task.)
- **Named persons do not eat** (ED-IN-0255; D:#1, DA:#10, DA:#16 DIFFERS). Hunger is a settlement's, carried by the cohort.
- **Hunger never enters the score** (L1-6 option B; DA:#36 DIFFERS). Survival reaches choice through body bands, the budget and Events.
- **Ageing, illness and hunger ship at zero by fixture** (`body_step` 0, `age_step` 0.0, `illness_rate` 0.0; `FX` per T10 §0a). Their
  rates are Jordan's (#457 D2). An item here may turn one on or give a reader to what exists **only with its control arm stated**: the
  zero arm is today's game and stays a selectable fixture.
- **RB-5 (hunger, the settlement hunger Query, `body_step` live) and the H-125 body clock are the remediation's**. This file builds on them
  and repeats neither (§5).

## §0 The genre loop

The yardstick is life/legacy and expedition play (The Sims 4, Wildermyth, Anno 1800's NPC economy, Patrician IV, Pathologic 2, Sunless
Sea, Battle Brothers' expeditions, Don't Starve). Each row is a play opportunity a player of that genre expects: what a person chooses, at
what cost, with what lasting consequence. "Today" is the as-built grade with its evidence grade.

| # | play opportunity | precedent evidence | today | evidence grade |
|---|---|---|---|---|
| G1 | **A journey is a priced leg.** Near is cheap, far is dear, a road is cheaper than a mountain; which route to take is a choice | D:#26, #47, #62 LACKS; DA:#4, #9, #35 LACKS; TL P06, P20; TM10 | **PARTIAL**: `move` executes, but every destination costs one flat leg point (`budget.py:60`); adjacency and terrain have no reader (T10 §1) | `move` RUNS-IN-LOOP; routes DESIGN-ONLY |
| G2 | **The road has risk.** A leg through bad country or bad weather can hurt the traveller; safer and riskier routes differ | D:#2 LACKS; DA:#9 LACKS; TL P23, P37; TM10 | **ABSENT**: the only moment of risk is arrival (T10 §5c "Being seen"); exposure and the journey roll are L17's M-WT-3/-4 | DESIGN-ONLY |
| G3 | **The year turns.** Seasons of the year change what land yields, what people need and what threatens them; winter is a thing you prepare for | D:#32 HAS (at control); DA:#13, #46 LACKS; DA:#20 HAS (at control); TL P41; TM11 | **PARTIAL**: one season-factor hook, keyed per season of year, ships empty: no year, factor 1.0 (`WQ` season factor; `FX`) | RUNS-IN-LOOP at control |
| G4 | **Keep your people fed or watch the town shrink.** Larder against mouths; a short season costs bodies; a starving place loses people | D:#21, #31; DA:#14, #24, #33, #48; TL P20, P01; TM08 | **PARTIAL**: the draw runs; at `body_step` 0 nothing is hurt, and cohort weight has no writer (T10 §5b) | RUNS-IN-LOOP at control; RB-5 designs the rest |
| G5 | **A wound costs time and care.** Recovery is slow, quicker with a carer, a bed or supplies; bad wounds can leave a mark | D:#3, #15, #23, #28, #33, #38, #48 DIFFERS; DA:#11 DIFFERS; TL P40, P32; TM01, TM10 | **PARTIAL**: one unpriced `tend` heals 1 → 1000 (code-flagged [ASSUMPTION]); no passive recovery; no upward crossing Event | `tend` TESTS-ONLY (0 of 75) |
| G6 | **People age.** Life stages change what a person can do; the old slow down and die; a ruler's age is a clock the court watches | D:#19, #45, #50 LACKS; DA:#1 HAS (at control), #19 LACKS, #26 DIFFERS; TL P31; TM05 | **ABSENT** in effect: every built person has `born` 0, the hazard is shipped at 0, age reaches nothing else | RUNS-IN-LOOP at control |
| G7 | **Kin, marriage and household.** Who is whose spouse, child, sibling; who shares a roof; ties that make a death or a betrayal land | D:#22, #44 (HAS, carrier only), #46, #49 LACKS; TL P11; TM05 | **ABSENT**: no kin, spouse or household edge; `tie`/`knot` declined (`VT` `tie`); stance moved only by `forgive` and a lost field | DESIGN-ONLY |
| G8 | **A death passes something on.** The heir inherits holdings, documents and grudges; a line, a house or a seat continues | D:#5 (recovery half), #24, #29, #55, #90 LACKS; DA:#7, #21 LACKS; TL P30; TM05 | **ABSENT**: death closes every edge and passes nothing (`world.py` `remove_person`); `succeed` declined; 7 of 32 seats can never refill | RUNS-IN-LOOP (the loss runs) |
| G9 | **Settle where there is room and reason.** People move toward food and safety and away from want; a host can be overrun by an inflow it cannot feed | D:#9, #18 (HAS), #53, #76, #89 LACKS/DIFFERS; DA:#12 HAS, #33 HAS, #60 LACKS; TL TM08 | **PARTIAL**: `migrate` 0 of 367 (destination set ignores room); presence-only crowding of a host larder is reachable through `move` | `migrate` TESTS-ONLY |
| G10 | **The world acts while nobody watches.** Illness, deaths of age, feuds, a killer remembered, a town in decline — drama for persons no player picks, keyed to the state of the world | D:#12, #57, #58 (HAS), #61, #65, #96 LACKS; DA:#25, #41, #43–#45, #54 LACKS/HAS-at-control; TL P38, P03; TM11; throughline 6 | **PARTIAL**: NPC-on-NPC acts run every round (D:#58); MATTER, the actorless channel, takes no random draw at shipped values (DA:#44) and no clock binds within the horizon (D:#51) | acts RUNS-IN-LOOP; ambient channel at control |

Ten opportunities: none AFFORDED, six PARTIAL (G1, G3, G4, G5, G9, G10), four ABSENT (G2, G6, G7, G8). G10's acted half (persons
acting on persons every round) is the one piece that runs as the genre expects. The common shape: **the carriers and hooks exist and the
readers do not**, or the reader is set to a control value. Most of this proposal gives an existing carrier a reader and a non-zero arm,
each beside its zero arm.

**Not in the yardstick, on purpose.** Discovery of authored places (Sunless Sea's ports, `explore`, M-WT-5) is parked in §1 (gap F):
`poi_catalog` holds counts, not places, and minting places from counts would invent content. Routines below the season (a schedule you
tail someone along) need a unit below the season, which the one clock refuses (D:#68 HAS).

## §1 Gap ledger

Scope: every LACKS and DIFFERS row of `D_T10.md` (37 LACKS, 15 DIFFERS) and `D_T10_also.md` (24 LACKS, 13 DIFFERS) — **89 rows**, all
addressed below; I did not sort DIFFERS rows into "risk" and "justified", I disposed of all 15 + 13. The nine CONTRADICTS rows (D:#36,
#73–#75, #86, #87; DA:#3, #38, #61) are edits to the description and the attachments, not gaps; they are out of this file's scope, except
DA:#3, which this file takes as ground (births ruled). Each gap ends in one disposition. "Five-step" answers cite the `CLAUDE.md` §0 step.

| gap | rows | disposition |
|---|---|---|
| **A. Distance is free.** Every destination costs one leg; the map has no reader | D:#6, #26, #47, #62 (distance half), #77 (distance half); DA:#4, #9 (price half), #35 (price half) | **closed by CP-T10-01**. The score half of DA:#35 (a person preferring what is near) is T02's chooser reading consequence (§5 demand D-1) |
| **B. The road has no risk** | D:#2 (risk half), #62 (hazard half); DA:#9 (risk half) | **closed by CP-T10-02**. D:#2's "between places" half (a lord *on* the road, waylaid): **declined**, step 5 — it needs a location that is not a Rung, which amends ratified Layer 1 (`contain : Rung → Rung`; L17 §3.9 item 2 recommends keeping journeys within the season); nothing here proposes it, so nothing is asked |
| **C. Named persons outside survival pressure (rulings)** | D:#1, #40, #54; DA:#10, #16 (all DIFFERS on ED-IN-0255) | **declined**, step 1 (ruled: named persons do not eat). The risk D:#1 names — the 46 choosers with pursuits feel no survival pressure — is answered *without* making them eat by CP-T10-05's place terms (a named person standing in a starving, crowded town falls ill) and CP-T10-02 (exposure) |
| **D. No year; no seasonal pressure** | D:#77 (season half); DA:#13, #25 (seasonal-sickness half), #46 | **closed by CP-T10-03** (with CP-T10-05 for illness by season) |
| **E. Hunger, famine, a town that shrinks** | D:#21, #65; DA:#14, #24 | **closed by RB-5** (REM-50 the Query, REM-51 its reach, REM-52 `body_step` 10) with **JQ-6** (the ratio); not repeated here. DA:#14's depopulation-by-departure half: **parked** as P-1 (§2), trigger JQ-6 answered (c) with cohort weights above 2. D:#65 (a lagged demographic loop): **declined** while ED-WR-0011's provisional ruling stands (gap K): no births, so no demographic loop |
| **F. Needs, moods and storytellers** | D:#8, #12, #13, #14, #43, #52, #69, #78, #96 (escalation half); DA:#25 (need half), #36, #45, #53 | **declined**. Needs and mood: step 1, L1-6 option B (RULED 2026-10-21: hunger never enters the score; REM-44 deletes `urgency`) and RB-5 route C (dropped by Jordan's clarification: hunger is a settlement attribute, not a person's). Storyteller and threat-by-wealth: step 3, T-WR-2 ("generate on demand, never on a clock; a threshold may change options, never act", `research/by_lane/WR_world.md:270`) and #457's cut of the event decks (WT-G39); a threat is some person's act (FA/MB). The licensed state-keyed composition (P38 over the existing hazard Query, no deck, no act) is CP-T10-05 |
| **G. Wounds heal in one free act; recovery is silent** | D:#3, #15, #23, #28, #33, #37, #38 (partial-damage half), #48, #84, #85 (H-211 half); DA:#11, #55 (`tend.refused` half) | **closed by CP-T10-04** (time and care) and **CP-T10-05** (illness that wounds, so triage has a subject). D:#38's permanent-mark half (P32): **declined here**, step 4 — a combat mark is PC's (T03 §0 G6); §5 demand D-3 fixes the boundary. D:#85's `urgency` half: REM-44. DA:#55's `migrate` half: REM-29. DA:#37 (one wound can take 3 of 5 points, where DF's ratio is robust): **declined**, step 4 — one band scheme on one quantity (H-38, "`Site.condition` is the model", `budget.py:71-83`) |
| **H. No ageing or illness that does anything** | D:#19, #45, #50; DA:#5, #8 (illness and mortality shipped at exactly 0, so "low" and "none" are one setting), #19, #26 | **closed by CP-T10-05** for the structure (age reaches the body, so the old do less before they die, as GK2's Body Points). The **values** (rates and every person's starting age; `references/npc_registry.yaml` holds `age: null` or no key on all 46 rows) are H-208's, owner Jordan (#457 D2): an existing ask, not a new one |
| **I. No kin, marriage, household or bond** | D:#22, #46 (marriage half), #49 | **closed by CP-T10-06** (kin), **CP-T10-08** (`marry`) and **CP-T10-09** (deeds done to me and mine). Household needs no object: co-residence is the live `reside` edge, and no reader needs a household Query (ID-13). D:#46's births half: **declined** while ED-WR-0011 stands (gap K) |
| **J. Death only subtracts** | D:#24, #29, #55, #90; DA:#7, #21 (successor half) | seats: **left to v9 IN-61** (succession, GV's), which is **stopped** at H-230, so the seat half is open, not closed; T02's CP-T02-01 (H-230 arm 2) is its unblocking work; this file builds beside it and repeats nothing; estates (Records, landholdings): **closed by CP-T10-07**. DA:#21's "a vacant throne ends nothing" half: gap M |
| **K. The cast never renews** | D:#56; DA:#2, #57, #59 | **declined for now**: ED-WR-0011's ruled Option A, provisional ("for now … we will return much later"; "everyone who will ever matter exists at tick 0 and the cast only shrinks", `registers/editorial_ledger_wr_archive.jsonl:14`). Not a step-1 closure: the row forbids citing it as settling world generation. Not re-asked: Jordan has said he will return to it, and nothing here waits on it |
| **L. Migration that steers** | D:#9, #53, #76, #89; DA:#22, #60 | `migrate`'s room becomes learnable: **closed by REM-29** (D:#89, DA:#22's alert half, DA:#60). D:#9, #76 (migrants follow wealth, danger, standing): **declined**, step 5 — an admission that reads a store or danger is the engine deciding options (AX-1; RB-5 §2.5b.4 refuses the same conjunct for hunger); a person's reason to go is the chooser's (T02). D:#53: step 1 (RR-2, "`found` is the throttle") |
| **M. No ending** | D:#16, #70; DA:#21 (loss half), #27 | **declined**, step 3: not this lane's. The victory layer is deleted (ERRATA G17) and `endings_reached` is a read owned by IN/FA (`world_q.py:1768`) |
| **N. The world's slow clocks** | D:#96 (visible-clock half); DA:#23, #54 | DA:#23 (structures repaired): **declined**, step 3 — `restore`/`work` are GV/EC's (T08). The doom clock (TM11) is v9 **IN-35** (the Calamity coupling, TW's, batch B-S); CP-T10-01's route Query supplies the distance order IN-35's own falsifier needs ("band crossings reach territories in order of distance"). D:#96, DA:#54 (visible clocks): **declined**, step 5 — the clock is already Queries (`season_of_year`, REM-50's `cover`); what a seated player is shown is IN-47's (RB-3) |
| **O. Grudges, killers, feuds** | D:#57, #61; DA:#41 | D:#57, DA:#41 (the killer is never written): **declined here**, step 3 — PC's repair (overview §6 #7, L09 M1; T03 builds on it). D:#61 (grudges never fade): **declined**, step 3 — `forgive` is the release valve (R-9 (a) adopted, L18 Suite C) and the write matrix refuses a `(Person, stance)` write at MATTER (`state/world.py:58-61`, T10 §2.6); a fade would be a fourth licensed clock |
| **P. Population without structure** | D:#17; DA:#29, #34 | **declined**, step 1: S9 (one Person carrier; a cohort is a Person at weight > 1) and ED-IN-0255; DA:#34's levy pyramid also needs births (ED-WR-0011) and is MB's |
| **Q. The player position** | D:#88, #94 | **declined**, step 1: D-2 RULED (the seat is IN-47, RB-3); orders that bind nobody are T09's (`dispatch`, CP-T09-08; an FA host row) |
| **R. Routines below the season** | DA:#15, #65, #66 | **declined**, step 5: one clock (D:#68 HAS; 9T dir. 6); a sub-season unit is a second clock |
| **S. Why a starvation happened** | DA:#49 | **declined here**, step 3: attribution of MATTER writes is IN's (`causes`, G1b); REM-51's Observation is the surfaced half |

Count (each row counted once, in the first gap that names it): **89 rows addressed — 34 closed** by an item here (gaps A, B, D, G, H,
I); **6 closed only in part** (gap J: the estate half by CP-T10-07; the seat half waits on v9 IN-61, which is stopped at H-230, so it is
not counted as closed); **6 closed by named remediation items** (RB-5: 3; REM-29: 3); **43 declined** with the reason given (gap K's 4
"for now", on a provisional ruling). A row split across two gaps (D:#2, #38, #62, #77, #85, #96; DA:#9, #14, #21, #25, #35, #55) has each half disposed of where it
sits. **No row raises a Jordan ask** (§6).

**Two L17 asks, answered rather than carried.** L17 §3.9 item 1 ("does the road cost a named person anything but time?"): answered at
step 3 — option (a), only Calamity territory exposes a named traveller; ED-IN-0255's reasoning (subsistence is "a territorial issue") and
XSC §6.4's Calamity-only exposure point the same way, and (b) would need a weather-on-person carrier nobody owns; CP-T10-02 builds (a).
L17 §3.9 item 2 (between places): not asked, because nothing here proposes it (gap B).

**One trap kept, not "fixed".** Schoenland (T16) is a second root, so journeys into it are `travel.blocked` (T10 §2.2). That is the
border by construction (`harness/populated.py:835-845`: "a `contain` edge into `r_valoria` would assert it is part of the realm";
`:859`: "THAT ABSENCE IS THE BORDER; crossing it is a `march`'s arrival leg"). CP-T10-01 therefore keeps `contain_path` as a conjunct
and prices only journeys it already admits.

## §2 Items

Nine items and two parked rows. Every item binds **Layer 2** (code and data under `engine/season/`, plus the cast registry
`references/npc_registry.yaml` that `data/cast.py` reads); none touches Layer 1 text. Every new magnitude is a fixture or roster value
marked **[ASSUMPTION; medium; Jordan to correct]**, with its revert, on H-125's precedent; every item ships a **control arm that is
today's game** and reproduces the base hash (`build_realm(s)`, s = 0, 1, 2, two seasons, `World.content_hash()`). Figures marked
"probe" come from my read-only, uncommitted `python3 -I` reads of `GEO` at HEAD (Dijkstra over `settlement_adjacency`, terrain by
point-in-polygon on settlement `coords`); they are illustrative until the item's own test computes them.

### CP-T10-01 · The journey is priced by its route

- **Adds.** A Query `route(w, a, b) -> (path, cost)` in `queries/world_q.py`: shortest path over `GEO: settlement_adjacency` (55 edges,
  one component of 37, diameter 8 edges; probe), each edge costing `terrain_cost_matrix[t]` of the settlement entered, where `t` is the
  terrain polygon containing its `coords` (`plains` where none does: 8 of 37, probe). A rung's route node is the settlement at or above it
  (a settlement rung is `set_` + its geography id, `harness/populated.py:850`); a rung above settlement kind, or a journey inside one
  settlement, costs the floor. **Leg points** = `max(1, ceil(cost / leg_unit))`, `leg_unit` a fixture **[ASSUMPTION: 2.0]**. Ties break on
  sorted ids, so the path is deterministic.
  - `_relocate` (`loop/effects_migration.py:119`, the one RESOLVE writer; `_eff_march` reaches it too) appends
    `(dest, points, path)` to `Person.travel_leg` on the on arm, where `path` is the tuple of settlement ids `route` returned (the
    origin is otherwise only on the closed `contain` edge, and a person may make several journeys a season, so MATTER could not recover
    it: the leg carries it, for CP-T10-02). On the off arm it appends the bare `dest`, as today. `budget.py:60` subtracts the sum of
    points × `budget_leg_penalty`, a bare id counting 1 point.
  - **Every leg writer goes through `_relocate`.** For a leg charged without a move (T04's siege leg: the army sits and pays), `_relocate`
    takes a `relocate=False` flag: the priced leg is appended and no `contain` edge closes or opens; the path is `route(origin, dest)` all
    the same. T09's `dispatch` (a dispatched man's journey) is acknowledged on the same terms: it calls `_relocate`, and the leg is
    priced on the person who travels.
  - **A journey that changes no presence is not formed, and one injected is declined** (`travel.blocked`, keyed `same_place`). H-140 is
    a RULING-kind row; it is answered at step 4 by precedent: IN-45 stopped `migrate` forming on a place "he already lives under" and
    `_eff_migrate` declines "a migration that changes no residence" (H-168; L17 S1 disposition 2).
  - `contain_path` stays a conjunct, so the border (§1) holds. The `move` → `travel` rename (L17, R-10) is not needed for this and is not
    bundled.
- **Owner artifacts.** `queries/world_q.py::route` (one owner of path and cost); `data/geography.py` (the season's existing reader of
  `GEO`, extended to `settlement_adjacency`, `terrain`, `terrain_cost_matrix`). `GEO` has **two** readers today: world-gen parses it
  independently in `harness/populated.py:773` (`_load(GEOGRAPHY)`), and `data/geography.py` reads it for the battle field. This item adds
  no third: `route` reads through `data/geography.py`, and routing world-gen's read through it too is a consolidation this item does not
  bundle. The file's own ownership move out of `systems/` is not this item's; fixtures `leg_unit`, `route_pricing` (the arm switch) in `data/fixtures.py`.
- **Primitives.** P05 (the budget is the price), P06 (a verb's price set by its object), TM10's leg.
- **Asymmetry (§0.1 pt 1).** `budget()` changes what it computes. Assignments of `Person.travel_leg` at HEAD: `effects_migration.py:119`
  (append), `loop/matter.py:651` (clear), `harness/probes.py:2942` (a probe sets bare strings: rewritten, or a bare id reads as 1 point).
  Readers: `budget.py:60`, `loop/deliberate.py:520` (the fingerprint; tuples stay hashable), `harness/soak.py:214`.
- **Decision handed to the chooser.** Go yourself or act where you stand; near business before far; a far journey early eats the season
  (a 4-point leg in round 0 leaves a budget-5 person nothing from round 1). **Unwatched:** officers who travel far act less that season;
  distance becomes who meets whom.
- **Falsifier** (`engine/season/tests/test_route_leg.py`, new): S-001 → S-002 prices 1 point; S-001 → S-013 (Aschenbach) prices
  `ceil(7.0 / 2.0) = 4` (probe: 5 edges, cost 7.0); after a round-0 journey to S-013 a hold-less person's `budget()` is 1; a same-place
  `move` forms no Candidate; a journey into T16 is still `travel.blocked`. Mutation: `route` returns cost 1 → the S-013 assertion reds.
- **Control.** `route_pricing` off → `_relocate` writes bare ids, so the leg's repr and the write deltas (both folded into
  `content_hash`, `state/world.py:1392-1393`) are unchanged → flat 1 point per leg → base hash at seeds 0–2, **except** for the same-place
  rule, which forms fewer `move`s and is a declared mover on both arms (it is not behind the switch). Paired arm (on vs off, same seeds): acts per acting
  person (act-store basis) and executed `move`s to a place other than the mover's own, which must rise from 16/16, 16/17, 10/12 "to own
  place" (T10 §9) — the observable the same-place rule exists for.
- **Hash.** Mover on the on arm (the leg's tuple repr is hashed, and budgets move); the same-place rule moves both arms. **Revert:** the
  fixture off; then the code. **Size:** M.

### CP-T10-02 · The Calamity costs the traveller

- **Adds.** At MATTER's leg-end pass (`loop/matter.py:643-655`), each ending leg charges the traveller's body the sum, over the
  settlements on its route (the `path` the leg itself carries, CP-T10-01; the first settlement, the origin, is not charged), of `exposure_body[band]`, the band of each settlement's territory in
  `GEO: radiation_bands` (band 0 epicentre T15, band 1 T6 and T13, … band 5). A new `rosters.yaml: exposure_body` row keyed by band
  **[ASSUMPTION: band 0: 300, band 1: 150, others 0]**. The write goes through MATTER's body writer in the hunger write's shape
  (`matter.py:524-531`), calls `_crossings`, and death at 0 goes through `_die`. No draw: this lane rolls no dice, and the XSC "Endurance
  check" needs a capability source (J-13's remainder) that does not exist.
- **This is L17 §3.9 item 1, option (a)** (only Calamity territory exposes a named traveller), answered at step 3 (§1).
- **Owner.** The leg-end pass in `loop/matter.py`; the band's one owner is whatever IN-35 names as the territory's Calamity band once it
  lands (TW's), and `GEO: radiation_bands` read through `data/geography.py` until then — never two copies.
- **Primitives.** P20 (a draw on the body per leg), P01, P02, TM10.
- **Asymmetry.** Writes `Person.body` at MAT (licensed `[MAT, RES]`); assignments listed under CP-T10-04.
- **Decision.** Business in Stillhelm, Aschenbach, Oastad or Salgrund (the four settlements in band-1 territories; probe) costs body as
  well as acts; send someone else, or go and be tended after. **Unwatched:** officers and cohorts return hurt from the Calamity's edge;
  `tend` acquires subjects; a marching army's legs pass through `_relocate` too (MB join).
- **Falsifier** (`test_exposure.py`): a traveller from S-001 to S-013 (path through S-012 and S-013, both T6, band 1; probe) ends the
  next MATTER at body 700 with a `body.changed` whose causes reach `travel.ended`; a traveller to S-002 is unchanged. Mutation: charge
  only the destination's band → 850 → red.
- **Control.** All `exposure_body` entries 0 → base hash. **Hash:** mover on the on arm. **Revert:** zero the row. **Size:** S.

### CP-T10-03 · The year turns

- **Adds.** A fixture `year_length` read by `season_of_year` (`world_q.py:958`), decoupled from `season_factor_draw` (M-WT-2): `0`
  means "the draw table's length, if any", so every existing fixture world keeps its calendar; a declared draw table must then hold
  `year_length` entries or raise `Unspecified`. A `rosters.yaml: season_terms` row, one entry per season of the year, each with three
  multipliers: `yield` (on `season_factor_of`'s result, `world_q.py:967`, its one owner), `want` (on the per-head want inside
  `subsistence_draw`, `world_q.py:1024`, its one owner, so REM-50's `hunger` and MATTER's draw cannot disagree) and `illness` (read by
  CP-T10-05). **[ASSUMPTION: year 4; winter yield 0.25, want 1.5, illness 2.0; other seasons 1.0.]**
- **Cut from L17's M-WT-2:** the storm season refusing `sail`. The one `sea` edge (S-001 ↔ S-037) crosses the border, so the refusal has
  no reachable reader (§3).
- **Primitives.** P41 (the calendar presses), P20 (the draw scales), TM11's clock.
- **Asymmetry.** `season_of_year`'s result is unchanged wherever `year_length` is 0. Its readers: `season_factor_of` (today), and after
  this `subsistence_draw` and `body_hazard`.
- **Joins.** RB-5 (want → `demanded` → `hunger`; JQ-6's M-H2 sweep gains a season arm, the same instrument, no new one); EC (yield in
  the year); MB (a campaign season reads `season_of_year`).
- **Decision.** Stock before winter; travel in summer; a governor's relief `transfer` before the lean season. **Unwatched:** winter draws
  rise, REM-51's hunger crossings reach governors in winter, and sickness (CP-T10-05) rises with it.
- **Falsifier** (`test_calendar.py`): at `year_length` 4, tick 3 is season 3; a weight-2 cohort wants grain 6 at a winter tick and 4 at
  tick 0; `hunger(w, S)`'s cover falls in winter on unchanged stores. Mutation: apply `want` in MATTER instead of `subsistence_draw` →
  the Query and the draw disagree → red.
- **Control.** `year_length` 0 and `season_factor_draw` `()` → base hash; `test_season_weather.py`'s three-hash equality unchanged.
  **Hash:** mover on the on arm. **Revert:** `year_length` 0. **Size:** M.

### CP-T10-04 · Recovery costs time and care

- **Adds.**
  0. **The cap is one quantity, owned by PC.** Every rise here — this arm and `tend` — heals toward the person's `body_ceiling`
     (T03 CP-T03-07: a per-person `Person.body_ceiling`, built at `condition_scale`, lowered by T03's permanent marks), or toward
     `condition_scale` where no ceiling is set. T10 owns the time-driven rising arm; T03 owns the ceiling and the marks. So this arm never
     heals a mark away.
  1. **A rising arm** in MATTER's body pass (H-211 cause 1; r2 §A.4's signed step): a living person below his `body_ceiling` who is not
     short this season gains `recovery_step` **[ASSUMPTION: 50 a season]**, capped at the ceiling. A cohort rises only when fed (no entry
     in the draw's shortfall record); a named person always (he does not eat). Hunger therefore blocks healing.
  2. **Upward crossings** (H-211 cause 2): `_crossings` (`matter.py:39-86`) gains `before < floor <= after`, same kind
     `condition.band_crossed`, its antecedent the rising write. H-211's own control: the per-season count of downward site crossings is
     unchanged.
  3. **`tend` heals a share of the headroom**, the revert the code names (`effects_combat.py:378-379`: "a swept fixture fraction of the
     headroom — #453's 'fast partial and slow full form', C-48"): fixture `tend_share` **[ASSUMPTION: 0.5]** of the headroom to
     `body_ceiling`.
  4. **`tend.refused` keyed by clause** (dead or absent / not with / whole), on `migrate`'s keyed-refusal precedent (DA:#55).
- **Owner.** `loop/matter.py` (body pass, `_crossings`); `loop/effects_combat.py::_eff_tend`; fixtures. Reads T03's
  `Person.body_ceiling` (`state/carriers.py`, T03's field). **Primitives.** P40 (recovery priced in acts and presence), P01, P02.
- **Asymmetry.** Assignments of `Person.body`: `matter.py:525` (hunger), `effects_combat.py:389-392` (`tend`), the combat writes in
  `_eff_kill` and `_eff_march` (T10 §2.6), and this arm. Readers: `budget.py:59` (bands), `deliberate.py`'s fingerprint, the PC seam's
  wound state (T10 §0a: wound → body → `end` → next fight), so a recovering fighter's `end` rises over seasons (PC join).
- **Decision.** Tend now (one act, and you must be "with" the patient) or let time do it; whom to tend first once CP-T10-05 makes the
  sick. **Unwatched:** the wounded mend over seasons, and the mend is news (a crossing witnesses can hold).
- **Falsifier** (`test_recovery.py`): a fed cohort at 450 rises 50 a season and crosses `limited` (500) upward once, emitting one
  `condition.band_crossed` (MW-11 green); a short cohort does not rise; `tend` at 250 with `body_ceiling` 1000 gives 625, and at
  250 with `body_ceiling` 799 (a T03 mark) gives `250 + 0.5 × 549 = 524`, never 1000; a marked person at 799 gains nothing from the
  rising arm. Mutations: the rising write lands on a copy → `budget()` unchanged → red (LB-3b's pairing of crossing and budget); the
  arm or `tend` reads `condition_scale` instead of `body_ceiling` → the marked person rises past 799 → red.
- **Control.** `recovery_step` 0 and `tend_share` 1.0 → the behaviour of today (the upward predicate fires on nothing at control, since no
  MATTER write rises). **Hash:** not hash-equal off: `body_ceiling` is a new `Person` field, so the hash moves by **schema** alone (H-208's
  precedent: a new `Person` field changes its repr) — declared a SCHEMA mover, landed with T03's CP-T03-07, which owns it; the on arm is
  also an outcome mover. **Revert:** the two fixtures. **Size:** M.

### CP-T10-05 · The bodies clock wounds before it kills, and reads the world

- **Adds.**
  1. **A hazard hit wounds.** MATTER's bodies pass (`matter.py:549-554`) writes `body -= hazard_body` **[ASSUMPTION: 400]** through the
     body writer, with crossings; death only at 0, through `_die` (unchanged owner). `hazard_body = condition_scale` is today's
     kill-on-hit, kept as a swept arm.
  2. **The illness term reads the person's world.** `body_hazard` (`world_q.py:999`, the one owner) multiplies `illness_rate` by
     (a) `season_terms.illness` (CP-T10-03); (b) crowding where he stands: `population / capacity` of the settlement at or above
     `place_of(p)`, above 1 → `1 + crowding_gain × (ratio − 1)` **[ASSUMPTION: crowding_gain 1.0]**; (c) that settlement's hunger band
     (REM-50's `hunger`), through a `rosters.yaml: illness_by_hunger` row **[ASSUMPTION: starving 3, hungry 2, lean 1.5, fed 1]**. The age
     term `age_step × age` is unchanged; cohorts keep hazard 0 (SE-01's split: only a cohort hungers, only an individual sickens).
- **Why this shape.** The age half becomes GK2's (DA:#19): the old take more hits, fall through the bands and do less before they die,
  through `budget()`'s existing band penalty and with no age term in a function that reads no clock. The illness half is the one P38
  composition T-WR-2 licenses: no deck, no act, a hazard Query read by the actorless bodies clock (AX-5's second motion). And it reaches
  the 46 named persons through where they stand, which answers D:#1's risk without making them eat.
- **Values.** The rates and starting ages stay H-208's (owner Jordan, #457 D2); this item adds no rate.
- **Asymmetry.** `body_hazard` changes what it computes; its one reader is the bodies pass (`age_of` and `body_hazard` are the only
  readers of `Person.born`, `world_q.py:992-997`). Assignments of `Person.born`: `carriers.py:687` (default), `census._individuate`.
  `Person.body`: as CP-T10-04.
- **Joins.** RB-5 (REM-50 must land first); GV (capacity: `found`/`build` lowers crowding, so housing is health); PC/NP (`tend`).
- **Decision.** Leave a crowded, hungry town in winter; tend the sick; send relief, which now also protects the officials standing
  there. **Unwatched:** sick seasons in crowded towns (at build `set_s_001` holds 12 residents against capacity 9, T10 §9), officials who
  sicken and recover or die, and the vacancies that follow.
- **Falsifier** (`test_bodies_hazard.py`): at `illness_rate` 0.25, a hit leaves 600 with `body.changed` and one crossing, and the person
  lives; a third hit kills through `_die`. Two identical persons, one standing in a settlement at ratio 2: the crowded one's hazard is
  double. Mutation: crowding counted from presence (`contain`) instead of residence (`reside`) → a crowd of visitors raises the hazard →
  red.
- **Control.** `illness_rate` 0 and `age_step` 0 → no draw → base hash. Paired arm: `hazard_body = condition_scale` reproduces IN-34's
  kill-on-hit (`test_in34_bodies_clock.py` is re-pinned to that arm, declared). **Hash:** mover on the on arms. **Revert:** `hazard_body`
  to `condition_scale` and the multipliers to 1. **Size:** M.

### CP-T10-06 · Kin

- **Adds.**
  1. **A `kin` Tenure kind** (L18 M9): Person → Person, directed, its content from a `rosters.yaml: kin_roles` row
     `[spouse, parent, child, sibling]`, added to `tenure_kinds` (`rosters.yaml:130`). **Not** in `release`'s domain, on the `reside` and
     `detain` precedent (`rosters.yaml:105-129`): nobody resigns being someone's son. (L18 says the loader forces `release`'s domain to
     take it; the `reside` note shows a kind can stay outside it. [UNVERIFIED] at the loader.)
  2. **Authored only from canon.** An optional `kin:` field on rows of `references/npc_registry.yaml` (`{to: NPC-nnn, as: <kin_role>}`),
     loaded by `data/cast.py` (which already raises on a malformed row) and minted by `harness/populated.py` beside the person. A row
     whose text states no relation gets none: inventing a relation is the fabrication ED-WR-0011 and `npcs.yaml`'s header refuse for
     persons. The registry's `role:` lines name a royal family (King, Queen "Widow Regent if Almud eliminated", Prince "Heir Apparent",
     Princess "married to Doux Alexios Laskaris"; `references/npc_registry.yaml:577, 666, 705, 744`); only the Princess–Doux marriage is
     stated outright, so the rest are [UNVERIFIED] until a canon source is cited row by row.
  3. **A `kin` witness channel**: a sixth `rosters.yaml: witness_channels` member, its predicate in `epistemic.py` beside
     `_ch_witness_key` (`:543`): a person holding a live kin edge to an Event's subject or anchor receives it, source `told_by`, for the
     kinds in a closed `rosters.yaml: kin_news_kinds` row `[person.died, body.changed, condition.band_crossed, marriage.made]`.
     Precedence: after the told channels, before `post_remit` **[ASSUMPTION]**.
- **Readers** (so the carrier is not ID-13): the channel; CP-T10-07 (the heir); CP-T10-08; CP-T10-09; FA's IN-70 opinion (its kin term,
  FA's to take). **Not** seat succession: RS-27/RS-29 ruled the heir a title.
- **Primitives.** P11 (pairwise record), P27 (news that travels by relation), P30's input.
- **Hazard named.** H-209: a dead man's claim never becomes a question (he has no place). Nothing here depends on a question about the
  dead; CP-T10-07 forms from its own estate stamper and CP-T10-09 reads claims in `regard`.
- **Falsifier** (`test_kin.py`): the authored Princess–Doux pair gives two kin edges at build; the Doux dies far away and the Princess
  holds a `person.died` claim naming him, source `told_by`, while a non-kin beside her holds none. Mutation: drop the channel → red. A
  `kin:` row naming an absent id raises at load.
- **Control.** No `kin:` rows → no edges → the channel admits nobody → base hash. **Hash:** mover once rows are authored. **Revert:** the
  rows. **Size:** M.

### CP-T10-07 · An estate passes by its heir's claim

- **Adds.**
  1. **A separate, non-broadcast estate record.** Seats are not this item's: T02's CP-T02-01 owns H-230's arm 2 (one `tenure.closed`
     Event per **Office** hold a death empties, broadcast by the chronicle), and this item neither widens it nor shares its change. A
     dead man's Record and Rung holds must not be listed among a broadcast Event's changes (that is H-206's option (b), unbuilt because
     those edges leave with him, `hole_register.yaml:4502`; broadcasting them would put every dead man's case files in every living
     ledger). Instead, inside the one death cascade (`World.remove_person`), before the dead man's own edges leave, the objects of his
     live `hold`s whose kind is in `estate_object_kinds` are recorded on a World-side record `w._estates[dead] = (objects, tick)`, on the
     precedent of `_departed` (where he stood, H-206, `state/world.py:757`). Nothing is deposited by it.
  2. **`heir_of(w, dead, obj)`** in `queries/world_q.py`: the first living person, by a `rosters.yaml: estate_heir_order` row
     `[spouse, child, sibling, parent]`, among those who **own** a kin edge naming `dead` that closed at his death; ties by id. It reads
     heir-owned edges only: the cascade sets `until` on every edge naming the dead (`state/world.py:755-759`), and an edge the survivor
     owns stays on the survivor's list, whereas the dead man's own edges leave with him (H-230, `hole_register.yaml:4814`).
  3. **How the heir comes to claim** (AX-2): he holds the death claim (CP-T10-06's kin channel). A stamper `estates_named(w, p)` on
     REM-21's `STAMPERS` registry offers, on that question, the objects of `w._estates[dead]` to `p` only when `p == heir_of(w, dead, obj)`
     — a person's own family's holdings as his own purview, on `larders_in_purview`'s shape (`world_q.py:2269`) **[ASSUMPTION; medium]**.
  4. **GV's `succeed`** (re-specified by IN-61 as the heir's own claim, GV's row by R-11) **accepts an estate object**, a Record or a Rung
     (a `rosters.yaml: estate_object_kinds` row `[Record, Rung]`), under the `inheritance` basis admitting exactly `heir_of` for an object
     in `w._estates[dead]`. The act opens the claimant's `hold` in one write (`give`'s shape). Offices stay on IN-61's `successions` route; Propositions are excluded (an
     utterance is its maker's).
- **Why a claim, not a transfer at MATTER.** RS-27 ("designated heir is not a verb but a status or title. the heir still has to claim
  their throne", quoted at `workplans/valoria_master_workplan_v9_part5.md:211`) is the precedent; one methodology for seats and estates
  (S); and `(Tenure, since)` is licensed at `[RES, ENC]` only (`write_matrix.yaml`), so an automatic opening at MATTER would need a new
  licence. The heir learns of the death through his own ledger (CP-T10-06's channel), and only he is offered the estate: nobody else's
  ledger fills with the dead man's papers.
- **Primitives.** P30 (heir transfer), P05 (each claimed hold is +1 budget point, so an inheritance buys acts).
- **Joins.** GV (IN-61, the `succeed` row, the `inheritance` basis); T02 (CP-T02-01's Office-only death Event is adopted as is for
  seats); FI (inherited case files and forged papers go to the heir,
  so evidence outlives its holder); FA (land held across a faction line by a widow).
- **Decision.** Claim the dead man's papers and land, or leave them; marry with an estate in view. **Unwatched:** holdings follow kin
  when nobody is looking; a dead minister's case file reaches his sister, who now holds the evidence.
- **Falsifier** (`test_estate.py`): a holder of a Record and a landholding dies far from his spouse; `w._estates` records both; she
  (and nobody else) is offered both; her `succeed` on the Record opens her `hold` and raises her `budget()` by 1; a person standing at
  the death holds the `person.died` claim but no claim naming the Record; a non-kin's claim is `succession.refused`; with a spouse and a
  child alive, the child's claim is refused. Mutations: `heir_of` ignores the order → the child is admitted → red; the estate objects
  ride the `person.died` Event's changes → the bystander holds a claim naming the Record → red.
- **Control.** `estate_object_kinds: []` → `_estates` is never written, no estate claim forms → base hash. **Hash:** mover on the on
  arm. **Revert:** the roster empty. **Size:** M.

### CP-T10-08 · `marry`

- **Adds** a verb row (L18 Suite E, on CP-T10-06's kind). Eligibility `own`; the counterparty is `subject`, a Person "with" the actor
  (`requires_typed: all: [existence(subject, Person), relation(subject, with)]`, `tend`'s and `give`'s cell shape); a negation that
  neither holds a live `spouse` edge (the predicate route, as `release`'s); both individuals (weight 1: an `individual` CELL stem on the
  `room`/`with` precedent [UNVERIFIED that no stem covers it]). **This item owns the `individual` stem** (one entry in
  `data/requires.py::REQUIRES_STEMS`, read through `Person.is_cohort`, `state/carriers.py:726`, never a second weight test); T03's
  CP-T03-10 uses it and does not define its own. Consent: the subject's `regard` toward the actor at or above
  `marry_consent_floor` **[ASSUMPTION: 0.0]**, read at the fold (P24; ED-IN-0210 ruling 1's counterparty/obstacle shape, as L18
  proposes). The effect opens two `kin` edges with content `spouse` in one write and emits `marriage.made`; refusals `marry.refused`,
  keyed by clause. Alignment cells on the pursuits `family` and `love` (the registry's convictions carry `family` weights), authored in
  the IN-08 cells pass **[ASSUMPTION]**.
- **Readers.** The kin channel; `heir_of` (spouse first); CP-T10-09. `wed` culled, `betroth`, `court`, `rear` stay PARKED (L18).
- **Decision.** Marry for an estate, a bridge between houses, or regard. **Unwatched:** NPC marriages that change where holdings flow at
  the next death and who grieves whom.
- **Falsifier** (`test_marry.py`): two co-located individuals with regard above the floor → `marriage.made` and two edges; below →
  refused keyed `consent`; an already married actor → refused keyed `spouse`. L18's own: "a `marriage.made` whose `kin` edges nothing
  reads fails" — `test_estate.py`'s spouse case reads them.
- **Control.** Row not resolvable → base hash. **Hash:** mover once resolvable. **Revert:** the row's `effect_decline_note`. **Size:** M.

### CP-T10-09 · Deeds done to me and mine

- **Adds.** In `person_q.regard`'s judged half (`person_q.py:393`, the one owner): a deed claim whose patient is the judge, or a person
  the judge holds a live kin edge to, adds `patient_gain × patient_valence[kind]` toward the deed's doer. A `rosters.yaml:
  patient_valence` row **[ASSUMPTION: `body.tended` +1, `record.given` +1, `person.died` −2, a fight's `body.changed` −1]**; fixture
  `patient_gain` **[ASSUMPTION: 0.5, the size of `judged_gain`]**. For the paired kinds (death, wound) the doer comes from IN-58's pairing
  in `deeds_judged`, the one route; [UNVERIFIED] that every listed kind's claim exposes its patient as `subject`.
- **Why it is not a second thumb** (NERS disqualifier 4): `deed_valence` (`person_q.py:371-379`) is the judge's pursuit lean on the
  kind and is blind to who received the deed; this is L18's M13 (a gift's effect on the receiver) and M10's kin slice.
- **Readers.** `regard` → `teller_weight` (`options.py:1515-1522`) and the score's regard term (IN-18 G1/G2). Vengeance as a *choice*
  still needs M6 (ED-IN-0296's declared arm, already Jordan's); not repeated.
- **Decision.** Tend, give and protect to earn trust; harm a man's kin and his whole house reads you lower. **Unwatched:** a healer's
  patients believe her; a dead man's brother distrusts the killer and everyone the killer tells him.
- **Falsifier** (`test_deeds_to_me.py`): A tends B → B's regard of A rises by `patient_gain` beyond the lean, while C (same pursuits,
  present) moves by the lean alone; A kills B's sibling → B's regard of A falls by `2 × patient_gain`. Mutation: key the term on the
  witness instead of the patient → C moves → red.
- **Control.** `patient_gain` 0 → base hash. **Hash:** mover on the on arm. **Revert:** the fixture. **Size:** S.

### Parked

| id | what | why parked | trigger |
|---|---|---|---|
| P-1 | Cohort weight migration (L17 M-WT-6): part of a starving cohort's weight moves to a fed settlement's cohort, against `capacity` | every one of the 37 cohorts has weight 2 and `is_cohort` is `weight > 1` (`state/carriers.py:726`), so any departure leaves a cohort of weight 1, which the code then reads as an individual | JQ-6 answered (c), with cohort weights above 2 |
| P-2 | `explore` and authored places (L17 M-WT-5) | `poi_catalog` holds per-territory counts, not places; minting places from counts invents content | authored POI entities (a Site or a Record per catalogue entry, from canon) |

### The write matrix, and what each item reads

| item | reads | writes (field, step) | new owner object |
|---|---|---|---|
| 01 | `GEO` via `data/geography.py`; containment; fixtures | `Person.travel_leg` (RES, element type), cleared at MAT as today | Query `route`; fixtures `leg_unit`, `route_pricing` |
| 02 | the leg's route; the territory band | `Person.body` (MAT) | roster `exposure_body` |
| 03 | `w.tick` | none (multipliers on existing writes) | fixture `year_length`; roster `season_terms` |
| 04 | the draw's shortfall record; `body` | `Person.body` (MAT up; RES `tend`) | fixtures `recovery_step`, `tend_share` |
| 05 | `place_of`, `population`, `capacity`, REM-50 `hunger`, `season_terms` | `Person.body` (MAT), death via `_die` | fixtures `hazard_body`, `crowding_gain`; roster `illness_by_hunger` |
| 06 | the cast registry | `Tenure` `kin` (world-gen only) | tenure kind `kin`; rosters `kin_roles`, `kin_news_kinds`; one witness channel |
| 07 | heir-owned closed `kin` edges; `w._estates` | `w._estates` (inside the death cascade, MAT or RES, not broadcast); `Tenure.since` (RES, through GV's `succeed`) | Query `heir_of`; stamper `estates_named`; World record `_estates`; rosters `estate_heir_order`, `estate_object_kinds` |
| 08 | `regard`; `with`; live `spouse` edges | `Tenure` `kin` (RES) | verb row `marry`; fixture `marry_consent_floor`; stem `individual` |
| 09 | deed claims; live `kin` edges | none (a Query term) | roster `patient_valence`; fixture `patient_gain` |

## §3 NERS

Instrument A only: nothing here resolves by a draw except CP-T10-05's existing keyed hazard draw, whose shape (one Bernoulli per person
per season) is unchanged, so `resolution-diagnostic` has nothing new to stress. `[SELF-AUTHORED — bias risk]`: the orchestrator's
critic pass is the independent half.

**N — the cut on each item, and what dies.**

| item | cut it, and the game can no longer… | directions the loss falls in | verdict |
|---|---|---|---|
| 01 route | …make distance a choice: the capital and the far fjord cost one point, so where things happen carries no strategy (T10 §5d) | all six: bottom-up (who meets whom), top-down (a seat's reach), lateral (SC/FI acts need presence), vertical (MB `march`, EC `haul`), diagonal (IN-35's distance order), horizontal (`move`/`migrate` share it) | **holds** |
| 02 exposure | …make a place dangerous to visit | diagonal (TW's Calamity × travel), lateral (`tend` demand), bottom-up | **holds, narrowed**: four settlements lie in band-1 territories, none in band 0 (probe), and the chooser cannot weigh it (OV §6 #1), so for NPCs it is a cost without a choice until D-1; restated: *"the Calamity's edge hurts whoever goes there, and a seated player can choose not to"* |
| 03 year | …make winter come: yield, need and sickness are the same every season | top-down (governors' relief timing), vertical (MB campaign season), diagonal (CP-05) | **holds, narrowed**: the `want` term binds nothing at today's magnitudes (RB-5 measures ~20 seasons of food on hand; JQ-6 owns the ratio); restated: *"yield and sickness follow the year; need follows it once JQ-6 makes hunger bind"* |
| 04 recovery | …make a wound cost time, or make recovery news; H-211 stays red (MW-11) | bottom-up, lateral (PC's next fight), horizontal (`tend` and the rising arm share the body) | **holds** |
| 05 hazard | …make sickness a thing that happens to the 46 choosers, or age a decline rather than a coin toss | bottom-up, top-down (housing and relief protect officials), diagonal (RB-5 × GV × NP) | **holds** for illness; **the age half is a false N-line today** (disqualifier 2: no producer — every built person is age 0, `npc_registry.yaml` holds no age); it becomes live with H-208's answer and costs nothing to carry |
| 06 kin | …have families: no news by blood, no heir by blood, no house to offend | lateral, bottom-up, top-down (houses as alliances via 08) | **holds**. Attack: could `knot` (FI's) or `tie` carry it? `knot` is fieldwork's partner channel with strain and rupture (`epistemic.py:543-560`) and `tie` is unilateral by axiom; overloading either is shape divergence, so the attack fails |
| 07 estate | …make a death hand anything on: holdings die with the holder (D:#90) | bottom-up, lateral (FI papers travel), top-down (land) | **holds**; IN-61 carries seats only |
| 08 `marry` | …choose kin: the family set is fixed at build | lateral, top-down | **holds, narrowed**: in a closed adult cast its consequence is rerouted estates, news and regard, not children (ED-WR-0011); restated accordingly |
| 09 deeds to me | …make care earn trust, or harm to a son reach the father | bottom-up, lateral | **holds, narrowed**. Attacks: disqualifier 4 (the ranking already weights care) fails because the lean is patient-blind (`person_q.py:371-379`); disqualifier 5 (a flat bonus) fails because the term is per pair and per deed, not a pool. Residual: its magnitude mirrors `judged_gain` by assumption |

**False N-lines found, and cut in this file.** (1) A life-stage roster and an `age_onset` fixture: no producer of ages, and the onset is a
second parameter on one curve (disqualifiers 2, 5) — cut; CP-T10-05 keeps `age_step × age` as the one curve. (2) The storm season
refusing `sail` (M-WT-2): its only edge crosses the border, no reachable reader (disqualifier 2) — cut. (3) A household Query: co-residence
is the live `reside` edge and nothing reads a household (ID-13) — never added. (4) Cohort migration (M-WT-6): no producer of cohort
weight above 2 — parked (P-1). (5) `explore`: no authored places — parked (P-2).

**R.**
- *R-COMPLETE, at the extremes.* A route dearer than the budget floors at 1 (the season is spent, not refused). A hazard or exposure larger
  than the body kills through `_die`. Recovery caps at the person's `body_ceiling` (T03's; `condition_scale` where none is set). A dead man with no living kin leaves his estate unheld (today's
  state). Two kin heirs of one rank tie by id (a rule, stated). A `tend` on a whole body is refused, keyed. No branch is unwritten that I
  found; that is an upper bound.
- *R-WORLD.* Unwatched, the world after this proposal throws: officers back from the Calamity's edge hurt; winter sickness in the
  crowded capital; deaths by sickness among office-holders, then estates claimed by widows and brothers; kin learning of a death
  three settlements away and distrusting the killer; marriages between houses. Each is an Event a witness can hold.
- *R-CHOICE* at a seat a player can occupy (IN-47): **staying dominates travelling** wherever presence earns nothing; the price is now
  real, so travel is chosen for a purpose (to `tend`, to be `with`, to witness). That is the intended shape, not a dominance defect. **R
  for every item here depends on the act economy** (skill §6.3): a point is 1–2 acts (T10 §2.5), so a 4-point leg is most of a season.
- *R-VARIETY.* Several ways to keep someone alive (tend, time, relief, leaving a sick town); several ways to gain holdings (create,
  claim an estate, marry toward one).

**S.**
- *Methodology.* One price ladder (budget points; route cost converts to points once, at `_relocate`). One band scheme (`band_floors["body"]`)
  for hunger, exposure, sickness and recovery. One crossing function (`_crossings`) both ways. One death route (`_die`). One body writer at
  MATTER. One recovery cap (`body_ceiling`, T03's) for every rise. `GEO: march_budget` (`valoria_geography_v30.yaml:800-803`) has no
  code reader (grep of `engine/`, `modules/`, `systems/*/sim`: none), so it is unread data, not a second live ladder: delete it or
  ignore it.
- *S-UP.* An estate is claimed by a person who pays an act and can be refused at the gate; no threshold transfers it. PASS on shape.
- *S-DOWN.* Kin news is published to whoever holds the relation, through a channel, refracted as `told_by`; nobody addresses it by name.
  PASS on shape.
- *Pauses correctly.* Journeys complete inside their season (no between-places state), so MATTER, RESOLVE and ENCOUNTER need not yield
  to travel. PASS.
- *Score the tree separately:* every item is `paper`.

**E, scored last, as a ratio.**
- *E-OVERHEAD, counted.* In: 2 Queries (`route`, `heir_of`), 1 stamper (`estates_named`), 1 World record (`_estates`), 1 Tenure kind,
  1 witness channel, 1 verb row, 1 stem, 8 roster rows, 9 fixtures, 1 registry field, 1 field-type change, 1 `_relocate` flag
  (`body_ceiling` is T03's, read here). Out: the flat leg, same-place journeys, kill-on-hit, the one-act full mend, the year's
  dependence on the weather table, and two cut objects (above). The vocabulary grows by `kin` and `marry`. By the meta-rule this is
  presumed failed and argues its way out: seven of nine items add **no system**, they give readers to carriers that exist and are unread
  (adjacency and terrain, the season hook, the hazard Query, H-211, `tend`'s named revert); the two that add a carrier (06, 08) answer a
  floor the game has no carrier for at all (G7). The denominator is the nine magnitudes Jordan must eventually set, each with a revert.
- *E-LEGIBILITY.* A player can intuit the outcomes from the choices: far costs more; the Calamity hurts; winter starves and sickens;
  crowded, hungry towns are sick towns; families inherit and grieve. Where intuition fails: the chooser does not see the price (D-1).
- **Ratio:** most of the gain (G1, G2, G3, G5, G6, G10) is bought with readers on existing carriers; G7/G8 cost two carriers and earn
  three readers each. Nothing is cut that would make it more elegant without losing an R-WORLD hook.

**Self-audit.** 9a: §0's grades, §1's counts and §2's figures were re-checked against each other after the last edit; §1's gap E text
was corrected when DA:#5 and #8 moved to gap H. 9b: §3 turned on this file's own additions found the five false N-lines above and cut
or parked each. An independent reviewer would most likely attack CP-T10-09 (a regard term is easy to make a second thumb) and the
estate stamper's claim to pass AX-2 (`estates_named` reads a World record for one person).

## §4 One season, after

Illustrative except where marked: magnitudes are the **[ASSUMPTION]** defaults of §2; route figures are probe figures; the budget
arithmetic is `budget.py:57-61` and the packing is T10 §2.5's.

**The person.** A named officer of the court, standing and living at Valorsplatz (S-001), one live hold (budget 6, so 9 acts), body 1000.
The year arm is on (`year_length` 4) and it is the last season before winter. `illness_rate` is set to some non-zero value (H-208's,
illustrative); every other fixture is at §2's default.

1. **CALENDAR, MATTER.** The season factor is drawn; the larders are drawn; nobody at S-001 is short; at the court the hazard's crowding
   term reads `set_s_001`'s 12 residents against capacity 9 (T10 §9): ratio 1.33, so his illness term is ×1.33. No hit this season.
2. **What reached him.** A kin-channel claim: his brother, a landholder at Aschenbach (S-013), has died. The cascade recorded the dead
   man's Record and landholding in `w._estates`; the widow, first by `estate_heir_order`, is offered both; he, a sibling, is not, and
   nobody else's ledger names the papers.
3. **DELIBERATE, round 0.** His ranked acts put `move` to S-013 in the first chunk (the chooser does not price it: D-1). The route is 5
   edges, cost 7.0 (probe), so the leg is `ceil(7.0 / 2.0) = 4` points. He releases chunk 1 (3 acts, cost 2).
4. **Round 1.** `budget()` = 6 + … − 4 = 2; spent 2; remainder 0. Nothing more this season: **3 acts instead of 9.** The journey took his
   season. At S-013 he is "with" his brother's widow.
5. **Meanwhile, unwatched.** At the capital, a court official is hit by sickness: body 1000 → 600, one band down, one point off his budget
   and a crossing everyone at the court can witness. A cohort at Stillhelm (S-012) is fed, so its old wound rises 50.
6. **Next MATTER (winter).** His leg ends. Exposure: the route entered S-012 and S-013, both in T6, band 1: 2 × 150, so body 1000 → 700,
   one band, budget 5 next season. Winter's `want` × 1.5 raises every cohort's draw; at today's magnitudes no larder fails (JQ-6). The
   winter illness term doubles: the court official, at 600, is hit again (200, two bands below), and a court `tend` (one act, share 0.5)
   lifts him to 600.
7. **Next season.** The widow `succeed`s to her husband's Record and landholding (GV's row, `inheritance` basis): two holds, her budget +2.
   His own body mends 50 a season (700 → 750). He travels home, another 4 points; the way back enters only one band-1 settlement
   (S-012), so 150 more at the next MATTER (750 → 600).
   A seated player would not have gone in person, or would have gone and stayed. An NPC goes, because nothing prices the trip for him.

**What the world did without anyone watching:** a death passed holdings along kin, a sickness moved through a crowded court, a
journey to the Calamity's edge cost a body, and the court's acts thinned for two seasons.

## §5 Order and dependencies

**Within the proposal.** CP-T10-04 → CP-T10-05 (sickness must heal, or it is slow death) ; CP-T10-03 → CP-T10-05 (the season term; the
hazard item can land with the term at 1) ; CP-T10-01 → CP-T10-02 (the path) ; CP-T10-06 → CP-T10-09, CP-T10-07, CP-T10-08. CP-T10-08
lands last.

**On remediation and v9.** CP-T10-04 and CP-T10-05 after RB-5 (REM-52 edits the body pass; REM-50 is CP-T10-05's hunger input), serial
on `loop/matter.py` with B-Q, B-S, B-T as RB-5 is. CP-T10-03 after REM-50 (both touch `subsistence_draw`'s consumers). CP-T10-01 after
REM-26 and REM-29 (same file, same rows). CP-T10-07 after IN-61's `succeed` (its estate record does not wait on T02's CP-T02-01,
which it neither shares nor widens). CP-T10-04 lands with or after T03's CP-T03-07 (`body_ceiling`). REM-44 (deleting `urgency`) is independent of all nine.

**Interface demanded from other subsystems** (stated as I expect it; none waits for their files):

| # | from | the interface |
|---|---|---|
| D-1 | T02 chooser | a person-side reading of a leg's price (CP-T10-01's points) through a channel AX-2 allows (the params registry, or a held claim), so persons weigh distance; and M6 (ED-IN-0296's declared arm, already asked) for vengeance as a choice |
| D-2 | T08 GV | IN-61's `succeed` accepting an estate object (Record, Rung) under `inheritance` admitting exactly `heir_of` for an object in `w._estates`; `found`/`build` as the lever that lowers crowding |
| D-2b | T02 | none for seats: CP-T02-01's Office-only `tenure.closed` broadcast is adopted unchanged; CP-T10-07's estate route is separate and must not be folded into it |
| D-3 | T03 PC | `Person.body_ceiling` (CP-T03-07), which CP-T10-04's arm and `tend_share` read, declared a SCHEMA mover in both files; T03 cites CP-T10-04 as the one rising writer; permanent marks on PC's carrier; R-M1 (CP-T03-00, both parties written), which raises `tend` demand; CP-T03-10 uses CP-T10-08's `individual` stem |
| D-4 | T04 MB | `march`'s legs pass through `_relocate`, so they are route-priced and exposed: accept, or call `route` explicitly. The siege leg is written through `_relocate(..., relocate=False)` (CP-T10-01). No demand on `march_budget`: it is unread data |
| D-5 | T07 TW | IN-35's territory Calamity band as a Query CP-T10-02 reads (one owner; T07 now exposes it); the Forgetting zone's personnel effect stays TW's |
| D-5b | T09 FA | `dispatch`'s travel leg goes through `_relocate`, priced on the dispatched person (acknowledged in CP-T10-01) |
| D-6 | T08 EC | if `transfer`/`haul` price distance, they read `route`; seasonal yield reads `season_terms` |
| D-7 | T09 FA | IN-70 opinion's kin term; `defect` across a kin line read by CP-T10-09's patient term |

**What this gives them.** `route` (MB, EC, TW's IN-35 distance order); a year (`season_of_year` with `year_length`) for MB's campaign
season and EC; `heir_of` and `kin` for GV and FA; the one body-rising arm and upward crossings for PC; kin news as a witness channel
for FI's information model.

## §6 Jordan asks

**None survives the five steps.** The would-be asks, answered:

| would-be ask | step | answer |
|---|---|---|
| should births return, since the cast only shrinks? | — | not re-asked: ED-WR-0011's Option A is a provisional ruling ("for now … we will return much later"), so the question is already Jordan's and already scheduled by him; it is not a step-1 closure (the row forbids citing it as settling world generation). Designed within (estates, kin, IN-61) |
| does the road cost a named person more than time? (L17 §3.9 item 1) | 3 | (a): Calamity only (ED-IN-0255's reasoning; XSC §6.4) — CP-T10-02 |
| may a person be between places? (L17 §3.9 item 2) | — | not proposed; nothing waits on it |
| is a journey to where one stands a no-op? (H-140) | 4 | yes, by IN-45 and H-168's precedent — CP-T10-01 |
| how much does one `tend` heal? | 3 | the code's named revert (C-48, "fast partial and slow full form") — CP-T10-04 |
| estates by rule at death, or by the heir's claim? | 4 | the claim (RS-27's precedent; `Tenure.since` is licensed at RES/ENC only) — CP-T10-07 |
| who is whose kin? | 4 | only what canon states ("none is invented", H-207; `npcs.yaml`'s header) — CP-T10-06 |
| the starting ages and the ageing and illness rates | — | already Jordan's (H-208, #457 D2); not a new ask |
| how scarce is the world? | — | JQ-6 (remediation); CP-T10-03 only adds a season arm to its M-H2 sweep |
| the nine new magnitudes | 5 | fixtures **[ASSUMPTION; medium; Jordan to correct]** with reverts, on H-125's precedent; JQ-3 holds the class |

**Rulings these items touch** (none overwritten): ED-WR-0011 (designed within); ED-IN-0255 (named persons still do not eat); L1-6
option B (nothing enters the score); RR-2 and ED-SE-0051 (crowding reads `capacity`); RS-27/RS-29 (seats are IN-61's; the estate claim
follows its shape); #457 D2 and H-208 (rates and ages); H-125 and REM-52 (`body_step`); T-WR-2 (no deck, no clock-made act).

## §7 Risks, and what this deliberately does not do

**Risks.**
- **The cast thins faster.** The 46 only shrink, and the control run already kills 9, 6 and 11 persons in two seasons at seeds 0–2,
  all by combat (T10 §2.4; I1 verification). CP-T10-02 and CP-T10-05 add body loss; CP-T10-04 and CP-T10-05's "wound, not kill" arm
  reduce lethality. The net is unmeasured: every on-arm reading must report deaths per season beside its control.
- **Cost without choice.** Until D-1, NPCs pay route and exposure prices they cannot weigh; R-WORLD gains hooks, but NPC travel does not
  become strategic. A seated player's does.
- **Nine magnitudes.** Each is an assumption with a revert; together they are a tuning surface Jordan has not seen.
- **Kin may be thin.** If canon states few relations, CP-T10-06's channel and CP-T10-07's heirs reach few persons; `marry` is then the
  only producer.
- **Hash churn.** Nine movers, each behind its own switch; every seeded realm pin is re-pinned per item, and a re-recorded golden is said
  plainly (`CLAUDE.md` §7).
- **IN-61 is stopped** (H-230). CP-T10-07's claim waits on it; its estate record does not.
- **`is_cohort` is a weight test.** Anything that ever lowers a cohort's weight must keep it above 1 (P-1's reason).

**Deliberately not done.** Births, children, `rear`, generation of persons on demand or on a clock (ED-WR-0011); a between-places
state, ambush on the road, `camp` (Layer 1 `contain : Rung → Rung`); needs, moods, a storyteller or an event deck (L1-6, T-WR-2,
#457); routines below the season; permanent injury (PC's); divorce and betrothal (parked); discovery of places (P-2); a world-clock
display (IN-47's); renaming `move` to `travel` (R-10's, not needed here); any guard — no item proposes one, and none is earned.
